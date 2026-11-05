# STATUS — Estado verificável do d-BMO

- **Data desta revisão:** 2026-11-02
- **Repositório:** `resende-g/d-BMO`
- **Branch:** `main` (atualização via PR #2, `docs/model-lab-qlora-smoke-20261102`, já mergeado)
- **Estado geral:** documentação arquitetural publicada; código de aplicação e scripts do protótipo continuam fora da árvore Git consultada.
- **Modelo-base definitivo:** ainda não selecionado.
- **Limite da inspeção:** esta atualização registra resultados fornecidos pelo mantenedor e inspeciona arquivos da branch remota. Não inspeciona o clone local, arquivos não rastreados, logs locais ou integridade dos artefatos locais.

## 1. Estado do repositório

O repositório contém documentação de arquitetura, segurança, RAG, avaliação, roadmap, skills e identidade visual. Não há implementação de aplicação versionada na árvore remota consultada. Os scripts de treinamento e avaliação mencionados neste documento permanecem no ambiente local do mantenedor e não foram adicionados ao Git.

As funcionalidades descritas nos documentos arquiteturais são propostas ou protótipos externos, salvo quando explicitamente identificadas como implementadas e verificadas.

## 2. Estado por componente

| Componente/capacidade | Estado | Evidência e limite |
|---|---|---|
| Documentação arquitetural | Publicada | Documentos Markdown na branch principal |
| d-BMO Interface | Planejado | Nenhuma implementação de interface versionada |
| BMO Brain | Planejado | Nenhuma implementação de orquestração versionada |
| BMO Heart | Planejado | Nenhuma implementação versionada; dados pessoais não devem ser publicados |
| BMO Knowledge | Protótipo externo relatado; integração versionada planejada | Scripts externos não estão no repositório; RAG ainda precisa de avaliação reproduzível |
| BMO Model Lab | Protocolo documentado; experimento local concluído | Registro do smoke test e A/B em `experiments/2026-11-02-qwen3-1.7b-qlora-smoke.md`; harness não versionado |
| Hermes Agent | Em avaliação | Nenhuma integração versionada |
| Ollama | Testado historicamente | Runtime e versão atuais não revalidados nesta revisão |
| Docker | Planejado | Nenhuma configuração encontrada |
| NetBird | Configurado historicamente | Conectividade atual não revalidada |
| d-BMO-body (corpo físico) | Hardware em montagem; integração planejada | Repositório próprio ([resende-g/d-BMO-body](https://github.com/resende-g/d-BMO-body)); modo agente não implementado |
| Skills | Planejado | Nenhum executor versionado |
| Licença | Definida | Apache-2.0 para código e documentação; nome, logotipo e personagem excluídos (§6) |

## 3. Experimentos de modelos

### 3.1 Registros históricos anteriores

Os resultados abaixo foram registrados em documentação anterior e não foram reexecutados nesta revisão. Não são benchmarks comparáveis.

| Área | Resultado histórico | Limitação |
|---|---|---|
| `qwen2.5:3b` | Uma resposta em 3,384 s | Uma pergunta isolada |
| `qwen3:1.7b` | Uma resposta em 2,347 s | Uma pergunta isolada sob condições não demonstradas como idênticas |
| Consulta ao Manifesto | Uma consulta local revisada | Foram identificados erro factual e afirmações sem suporte suficiente |
| Isolamento de coleções | Validador relatou separação e canário sintético | Embeddings simulados; não valida versão implantada com embeddings reais |
| LoRA anterior | 2 passos, loss 4,6103 e pico de VRAM 2,13 GiB | Smoke test, não demonstra ganho de qualidade |

### 3.2 QLoRA smoke test e avaliação A/B — 2026-11-02

Foi concluído um teste técnico de QLoRA no Qwen3-1.7B e uma avaliação exploratória de oito perguntas no modelo-base e no modelo com adapter.

- Base experimental: `Qwen/Qwen3-1.7B`, revisão `70d244cc86ccca08cf5af4e1e306ecf908b1ad5e`.
- Adapter: `qwen3-1.7b-manifesto-smoke-v3`; SHA-256 `2c707c951ef31ff8d3d31107ca581cfd61bacdc34afb85668af8a291cdbcb040`.
- Dataset de treinamento: 8 exemplos; SHA-256 `6264401aa997c90daed7062aff53305d1e3d055f44fd60902694d44fd3e6bbdb`.
- Método: QLoRA NF4 4-bit; 2 passos; 8.716.288 parâmetros treináveis (aprox. 0,504%); loss final 4,376685; pico de VRAM reportado 2,13 GiB.
- Avaliação: 8 prompts em cada condição (16 gerações); todas concluíram sem erro.
- Resultado qualitativo: não foi observada melhora consistente do adapter. Persistiram erros de fidelidade textual, interpretação e extrapolação. Os dois modelos se abstiveram adequadamente em duas perguntas sem evidência.

**Ressalva metodológica:** a avaliação A/B utilizou tokenizer/template diferentes entre condições: o tokenizer do modelo-base em A_base e o tokenizer salvo no diretório do adapter em B_adapter. Como o adapter contém um template personalizado para treinamento, a comparação está confundida e não permite atribuir diferenças ao LoRA. Além disso, respostas foram truncadas pelo limite de 220 tokens. A avaliação deve ser repetida com tokenizer/template idênticos e limite de geração maior.

O Qwen3-1.7B foi utilizado apenas como base experimental para validar o pipeline. **Não é o modelo-base definitivo do d-BMO.** O JSON integral, o dataset e o adapter permanecem locais; não foram publicados no repositório.

Detalhes: [registro do experimento](experiments/2026-11-02-qwen3-1.7b-qlora-smoke.md).

## 4. Riscos e pendências prioritárias

1. **Isolamento documental:** houve relato de mistura anterior entre coleção pessoal e consulta pública. Revalidar com embeddings reais e na versão implantada antes de inserir conteúdo pessoal.
2. **Logs:** um script antigo teria gravado respostas em log JSON. Revisar localmente antes de publicar ou compartilhar.
3. **Reprodutibilidade:** código, dependências, fixtures públicas/sintéticas e harness ainda não estão versionados.
4. **Avaliação de RAG:** o conjunto de 12 perguntas (8 respondíveis e 4 sem resposta) e critérios de Hit@4/abstenção ainda precisam de execução reproduzível.
5. **Avaliação de fine-tuning:** repetir A/B com tokenizer/template idênticos, limite de geração maior e rubrica explícita.
6. **Seleção de modelo:** comparar candidatos adequados ao hardware; Qwen3-1.7B não foi selecionado como base definitiva.
7. **Backup:** há registro histórico de cópia para disco externo, mas restauração não demonstrada.
8. **Acesso remoto:** NetBird/SSH foi configurado historicamente; conectividade deve ser revalidada.
9. **Ambiente:** hardware e versões são referências informadas pelo mantenedor, não medições executadas nesta revisão.
10. **Licença e propriedade intelectual:** projeto sob Apache-2.0; compatibilidade de dependências ainda deve ser verificada por versão. O d-BMO possui conceito, personagem e identidade visual próprios, desenvolvidos independentemente. Não é derivado, adaptação ou extensão do personagem BMO de *Adventure Time* (*Hora de Aventura*), nem possui vínculo ou associação com a franquia ou seus titulares. Manter a documentação de autoria e a verificação de direitos dos ativos visuais.

## 5. Próximas ações

- [ ] Conferir clone local, branch, `git status`, arquivos rastreados e diferenças não publicadas.
- [ ] Revisar logs e artefatos locais sem copiar dados privados para o Git.
- [ ] Corrigir tokenizer/template da avaliação A/B e repetir o teste.
- [ ] Avaliar candidatos alternativos de modelo separadamente.
- [ ] Revalidar isolamento de coleções com dados sintéticos e embeddings reais.
- [ ] Versionar somente código e fixtures autorizados.
- [ ] Executar avaliação RAG controlada e documentar resultados.
- [ ] Testar restauração de backup.
- [x] Selecionar licença (Apache-2.0).
- [ ] Revisar licenças das dependências antes de publicação.
- [ ] Manter documentadas a autoria independente e a proveniência dos ativos originais do d-BMO.

## 6. Proveniência

Os resultados de QLoRA e A/B foram transcritos das saídas e do JSON fornecidos pelo mantenedor em 2026-11-02. Não foram reexecutados durante a atualização documental. Nenhum teste de aplicação, inferência, RAG, rede, backup ou sandbox foi executado nesta revisão. Nenhum dado local foi inspecionado. A atualização não altera o código nem os artefatos de treinamento no computador do mantenedor.
