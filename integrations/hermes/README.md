# Integração com o Hermes Agent

**Estado:** em uso experimental. Seção 4.3 da [ARCHITECTURE.md](../../ARCHITECTURE.md).

O d-BMO roda como um **perfil** do [Hermes Agent](https://github.com/NousResearch/hermes-agent). O Hermes fornece o laço de agente, o gateway de mensagens (Telegram), o cron e as ferramentas. A identidade, a política e as skills do d-BMO ficam nesta pasta. O Hermes não é a identidade do d-BMO nem a autoridade sobre memória e política.

## Versão fixada

| Item | Valor |
|---|---|
| Hermes Agent | v0.22.7 (2026.9.24), commit `b200f5bc` |
| Licença do Hermes | MIT (verificar de novo a cada atualização) |
| Máquina de teste | macOS, Apple M1 Pro, 16 GB |

Ao atualizar o Hermes, registre a versão nova aqui e repita a verificação abaixo.

## Arquivos

| Arquivo | Papel |
|---|---|
| `SOUL.md` | identidade e regras do d-BMO; o perfil aponta para ele por symlink |
| `config.dbmo.yaml` | chaves de config do perfil (modelo local, política de aprovação, bloqueios, skills) |
| `skills/` | skills do d-BMO, lidas pelo Hermes via `skills.external_dirs` |

Nada aqui contém segredo nem dado pessoal. Tokens (Telegram, OAuth do Google) ficam no `.env` e na pasta do perfil, fora do git. Rotinas agendadas com prompt pessoal (por exemplo, o briefing diário) ficam só no cron do perfil.

## Instalação

```bash
hermes profile create dbmo --no-skills --description "Assistente pessoal d-BMO"
P=~/.hermes/profiles/dbmo
{ cat integrations/hermes/config.dbmo.yaml; echo '_config_version: 52'; } > "$P/config.yaml"
rm "$P/SOUL.md" && ln -s "$PWD/integrations/hermes/SOUL.md" "$P/SOUL.md"
printf 'HERMES_WRITE_SAFE_ROOT=%s\n' "$P" >> "$P/.env"

# Modelo local: llama.cpp com Metal. GGUFs ficam em ~/.hermes/models (pasta da
# máquina; o Hermes move para lá qualquer models/ criado dentro de um perfil).
brew install llama.cpp
M=~/.hermes/models/Qwen3.5-9B-Q4_K_M.gguf
curl -L --fail -o "$M" https://huggingface.co/unsloth/Qwen3.5-9B-GGUF/resolve/main/Qwen3.5-9B-Q4_K_M.gguf
echo "03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8  $M" | shasum -a 256 -c

# Servidor como agente do launchd: sobe no login e reinicia se cair.
# --sleep-idle-seconds descarrega o modelo após 10 min sem uso.
cat > ~/Library/LaunchAgents/dbmo.llama-server.plist <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>dbmo.llama-server</string>
  <key>ProgramArguments</key>
  <array>
    <string>/opt/homebrew/bin/llama-server</string>
    <string>-m</string><string>$M</string>
    <string>--alias</string><string>qwen3.5-9b</string>
    <string>--host</string><string>127.0.0.1</string>
    <string>--port</string><string>8080</string>
    <string>-c</string><string>65536</string>
    <string>-np</string><string>1</string>
    <string>--jinja</string>
    <string>-fa</string><string>on</string>
    <string>--reasoning</string><string>off</string>
    <string>--sleep-idle-seconds</string><string>600</string>
  </array>
  <key>RunAtLoad</key><true/>
  <key>KeepAlive</key><true/>
  <key>StandardOutPath</key><string>$HOME/Library/Logs/dbmo-llama-server.log</string>
  <key>StandardErrorPath</key><string>$HOME/Library/Logs/dbmo-llama-server.log</string>
</dict>
</plist>
EOF
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/dbmo.llama-server.plist
```

O Hermes acha o servidor sozinho na porta 8080 e lê o contexto pelo `/props`. Ele exige no mínimo 64K (`MINIMUM_CONTEXT_LENGTH` em `agent/model_metadata.py`); por isso `-c 65536`.

Com o `KeepAlive`, matar o processo não adianta: o launchd sobe outro. Para parar, `launchctl bootout gui/$(id -u)/dbmo.llama-server`; para voltar, repetir o `bootstrap`.

Ajuste em `config.dbmo.yaml` o caminho de `external_dirs` se o clone não estiver em `/Users/BMO`.

### Telegram

```bash
dbmo gateway setup     # Telegram → [2] token manual do BotFather; allowlist só com o seu user id
hermes gateway install --start-on-login --start-now
hermes gateway restart # depois do install: troca o gateway manual pelo serviço do launchd
```

Existe um único gateway por máquina: o do perfil principal também atende o `dbmo`. Enquanto um gateway manual estiver rodando, o serviço instalado não sobe e sai com código 75 a cada ~30 s; o `restart` resolve isso. Não use a opção automática [1] do setup, porque ela cria o bot por um serviço de onboarding do Hermes. Quem não está na allowlist recebe `decline` (ver `config.dbmo.yaml`).

### Google Agenda (em andamento)

```bash
cp -R ~/.hermes/hermes-agent/skills/productivity/google-workspace "$P/skills/productivity/"
```

A skill `google-workspace` desta versão não tem `--services` e pede de uma vez Gmail (com envio), Drive, Docs, Sheets e Contatos. Na cópia do perfil, a lista `SCOPES` de `scripts/setup.py` fica reduzida a `https://www.googleapis.com/auth/calendar`. Para incluir o e-mail, a decisão precisa ser explícita.

O cliente OAuth é do tipo **App para computador**, num projeto GCP pessoal, com público **Externo** e publicado em produção. No modo Teste, o token vence em 7 dias. Com público **Interno**, a conta @gmail recebe `Erro 403: org_internal`. As dependências entram com `setup.py --install-deps`, rodado com o Python do Hermes; depois, `hermes gateway restart`.

## Mapeamento para a arquitetura

| d-BMO (ARCHITECTURE/SKILLS) | Hermes |
|---|---|
| Policy Gate / autorização humana | `approvals.mode: manual`, `cron_mode: deny`, `approvals.deny` |
| Escrita restrita | `HERMES_WRITE_SAFE_ROOT` no perfil |
| Inferência local (Ollama candidato) | `model.provider: llamacpp` apontando para um `llama-server` local (Qwen3.5-9B) |
| BMO Heart | ainda não implementado; a memória do Hermes (`MEMORY.md`/`USER.md` do perfil) é provisória |
| Manifesto de skill (§3 de SKILLS.md) | frontmatter do `SKILL.md`; campos `permissions`, `risk_level` e `confirmation` ainda não têm equivalente executável |

## Limitações conhecidas

- `approvals.deny` filtra comandos do terminal; não é sandbox. A ferramenta de leitura de arquivos ainda alcança o resto do usuário. Isolamento real: `terminal.backend: docker` ou um usuário separado do sistema.
- Em modo perfil, o Hermes usa o `auth.json` do perfil principal como reserva para providers sem credencial no perfil. Por isso, o modelo do `dbmo` precisa ficar fixo num provider local. Nunca selecione um provider de nuvem nele sem decisão explícita.

## Medições no Mac de teste

**2026-11-05: Colibri (`0a5504a1`) + Qwen3.6-35B-A3B int4, só CPU (sem Metal para esse motor), contexto de 16K, RAM ocupada por outros apps.**

| Teste | Prompt | Até o 1º token | Decode |
|---|---|---|---|
| Pergunta curta (primeira chamada) | 25 tokens | 209,6 s | 2,39 tok/s |
| Leitura de texto | 1.463 tokens | 521,9 s (~2,8 tok/s de prefill) | 1,75 tok/s |
| Chamada de ferramenta (lembrete com data relativa) | 345 tokens | 154,8 s | n/d |

A chamada de ferramenta acertou o nome e a data (`2026-11-06T09:00:00-03:00`). Já o prompt fixo do `dbmo` tem ~30,5 KB (~8 mil tokens) e, nesse ritmo de prefill, levaria por volta de 45 min até a primeira resposta de cada sessão nova, sem contar cada página lida pela web. **Conclusão:** a qualidade serve, mas a velocidade não sustenta o agente nesta máquina.

**2026-11-05: llama.cpp 0.9.0 (Homebrew, Metal), contexto de 64K, `-np 1`, flash attention.** Só modelos híbridos entram: num modelo denso de 8B, o cache de 64K passaria de 9 GB.

| Teste | Granite 4.0 H Tiny Q4_K_M | Qwen3.5-9B Q4_K_M (`--reasoning off`) |
|---|---|---|
| Pergunta curta: até o 1º token / decode | 0,9 s / 47 tok/s | 0,6 s / 21 tok/s |
| Leitura de texto (~2k tokens): até o 1º token | 3,3 s | 7,2 s (~200 tok/s de prefill) |
| Chamada de ferramenta (lembrete) | correta | correta |
| Memória do `llama-server` | 2,4 GB | 7,1 GB (sobraram 16% de RAM livre) |
| `dbmo`: "como está o projeto d-BMO?" | inventou resposta genérica, 0 ferramentas | 102 s, 7 ferramentas (skill, arquivos, `git`/`gh`), fatos conferidos |
| `dbmo`: rodar `git log -3` e dizer o último commit | rodou, mas apontou o commit errado | correto, 8 s |

**Escolha:** Qwen3.5-9B. O Granite é rápido, mas não segura o papel de agente (inventa em vez de consultar). O custo do Qwen é memória: com ele ligado, sobra pouca RAM para o resto do Mac. Se apertar, o próximo passo é cache KV em `q8_0` (`-ctk q8_0 -ctv q8_0`), que corta ~1 GB.

**Sono por ociosidade (`--sleep-idle-seconds`), 2026-11-05:** dormindo, o processo cai de 7,3 GB para 50 MB. O `/props` continua respondendo com `n_ctx` 65536, então o Hermes detecta o servidor sem acordá-lo. A primeira chamada depois do sono acordou e respondeu em 2 s, com o arquivo no cache de disco; logo após um boot, conte com ~9 s, que é o tempo de subida a frio.

## Verificação

```bash
dbmo auth status anthropic   # deve dizer que logins externos não são adotados
dbmo skills list             # dbmo-projeto (external) e google-workspace
dbmo config                  # provider llamacpp
```

As regras de `approvals.deny` foram testadas em 2026-11-05 contra `claude`, `gcloud`, `bq`, `hermes`, credenciais do perfil principal e o vault de trabalho (bloqueados), e contra `gh`, `git` e a própria pasta do perfil (liberados).
