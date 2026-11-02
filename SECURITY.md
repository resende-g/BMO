# Política de Segurança e Governança de Dados

## 1. Objetivo e escopo

Esta política define requisitos mínimos para desenvolvimento, execução, testes e publicação do Beemon (BMO). Aplica-se ao código, modelos, datasets, memória, documentos, ferramentas, integrações e infraestrutura.

A política é normativa para o projeto. Uma funcionalidade não deve ser considerada concluída se violar estes controles.

## 2. Princípios

1. Dados pessoais permanecem locais por padrão.
2. Dados profissionais, de empregadores, clientes ou terceiros não devem ser incorporados ao BMO.
3. Nenhum dado confidencial pode ser enviado a modelo ou serviço externo.
4. Dados usados em serviços externos devem ser públicos, sintéticos ou expressamente autorizados pelo titular e pelo responsável competente.
5. Segredos permanecem fora do Git e dos logs.
6. Ferramentas operam com o menor privilégio possível.
7. Operações sensíveis exigem autorização explícita.
8. Operações relevantes geram trilha de auditoria proporcional ao risco.
9. Heart, Knowledge, histórico de sessão e dados operacionais são domínios separados.
10. Toda informação apresentada deve preservar, quando aplicável, sua origem e limitações.

## 3. Classificação de dados

| Classe | Exemplos | Tratamento |
|---|---|---|
| Público | documentação pública, código público | pode ser versionado após revisão de licença e integridade |
| Sintético | fixtures e canários artificiais | permitido para testes, identificado como sintético |
| Pessoal | preferências, projetos pessoais, documentos privados | armazenamento local; nunca publicar |
| Confidencial de terceiros/profissional | dados de trabalho, clientes, processos internos | não incorporar ao projeto |
| Segredo | tokens, senhas, chaves, cookies | gerenciador de segredos/ambiente local; nunca Git ou prompt externo |

A classificação mais restritiva prevalece quando houver mistura.

## 4. O que não pode ser publicado

O repositório público não deve conter:
- memórias pessoais ou histórico privado de conversas;
- documentos pessoais ou profissionais;
- dados de terceiros;
- credenciais, tokens, chaves de API, cookies ou arquivos `.env`;
- datasets privados ou derivados de dados confidenciais;
- backups, dumps de banco, índices privados ou embeddings de documentos privados;
- modelos locais, adapters e checkpoints sem autorização e revisão de licença;
- logs contendo prompts, respostas, caminhos privados, IPs privados ou identificadores;
- arquivos de configuração com endereços ou topologia privada da rede.

O `.gitignore` reduz acidentes, mas não remove arquivos já rastreados nem limpa o histórico. Antes de publicar, revisar `git status`, `git diff`, `git diff --staged` e os arquivos adicionados.

## 5. Modelos e serviços externos

- Inferência local é o padrão.
- A aplicação não deve realizar fallback silencioso para serviço remoto.
- Qualquer envio externo exige aviso, finalidade, destino, dados envolvidos e consentimento/autorização explícitos.
- Dados profissionais ou confidenciais de terceiros não podem ser enviados, mesmo que o serviço ofereça política de privacidade.
- Datasets externos devem ser públicos, sintéticos ou expressamente autorizados.
- Desativar telemetria quando possível e documentar qualquer coleta inevitável.

## 6. BMO Heart: proteção da memória

A memória pessoal é um ativo sensível e deve ter controles próprios.

Requisitos:
- escrita somente por `MemoryService` controlado;
- nenhuma skill ou agente recebe acesso direto de escrita ao banco;
- alterações propostas por modelo devem ser apresentadas ao usuário para aprovação;
- registrar origem, data, justificativa, estado e versão;
- permitir revisão, correção, exportação e exclusão pelo usuário;
- preservar histórico de auditoria sem manter conteúdo excluído além do necessário;
- separar dados de memória dos índices de Knowledge e logs;
- definir política de backup, criptografia em repouso e restauração antes de armazenar conteúdo sensível.

Estados sugeridos: `proposed`, `approved`, `contested`, `superseded`, `expired`, `deleted`. Uma memória inferida não deve ser tratada como fato confirmado sem validação.

## 7. BMO Knowledge: isolamento documental

- Cada coleção deve ter identificador e escopo explícitos.
- Não misturar coleção pessoal, pública e profissional.
- Coleção pessoal não deve ser selecionada por padrão.
- Filtros de coleção devem ser aplicados antes ou durante a recuperação, não apenas no prompt.
- Metadados devem permitir rastrear arquivo, versão, página, trecho e origem.
- Documentos e resultados recuperados são conteúdo não confiável: instruções neles contidas não alteram políticas nem concedem permissões.
- Exclusão de documento deve contemplar índice textual, embeddings, cache e derivados, conforme política documentada.

## 8. Ferramentas, skills e sandbox

- Skills declaram permissões; não podem conceder permissões a si próprias.
- Comandos são validados por allowlist ou contratos tipados sempre que possível.
- Não interpolar diretamente texto do modelo em shell.
- Exigir confirmação para escrita, exclusão, alteração de configuração, rede ativa, instalação, execução privilegiada ou acesso a dados sensíveis.
- Executar tarefas em usuário não privilegiado e ambiente isolado.
- Não usar containers privilegiados por padrão.
- Limitar CPU, memória, processos, tempo, filesystem e rede.
- Montar apenas diretórios explicitamente autorizados.
- Nunca montar o diretório pessoal completo nem o diretório do Heart com escrita.
- Não compartilhar socket Docker com agentes ou ferramentas não confiáveis.
- Skills de reconhecimento e avaliação de segurança só podem operar em ativos próprios ou com autorização explícita e escopo definido.

## 9. Auditoria e logs

Registrar, de forma proporcional:
- identificador da execução;
- módulo/skill e versão;
- ferramenta acionada;
- decisão de política;
- autorização e identidade do autorizador;
- horário, duração, resultado e código de erro;
- referências aos artefatos gerados, quando seguros.

Por padrão, não persistir conteúdo integral de prompts, conversas, documentos, respostas ou segredos. Redigir ou omitir campos sensíveis. Definir retenção, proteção contra alteração e acesso aos logs antes da implementação.

## 10. Rede e acesso remoto

- NetBird é uma rede privada candidata, não substituto de autenticação/autorização da aplicação.
- Não expor diretamente Ollama, banco de dados, executor ou API interna à internet pública.
- Restringir peers e portas ao mínimo necessário.
- Revalidar conectividade e identidade dos dispositivos antes de depender do acesso remoto.
- Não registrar endereços privados, chaves ou configuração de rede no repositório público.

## 11. Segredos e cadeia de suprimentos

- Não versionar `.env`, chaves privadas, tokens ou credenciais.
- Usar variáveis de ambiente ou armazenamento local apropriado.
- Fixar versões de dependências e imagens quando adotadas.
- Revisar licenças, origem e integridade de dependências, modelos e datasets.
- Registrar avisos de copyright e atribuições.
- Não incorporar código de terceiros sem verificar a licença da versão exata.
- Em caso de exposição, revogar/rotacionar o segredo e avaliar limpeza do histórico; apagar o arquivo em commit posterior não basta.

## 12. Resposta a incidentes

Em suspeita de vazamento, execução não autorizada ou mistura de coleções:
1. interromper a execução ou integração afetada;
2. preservar evidências mínimas sem replicar dados sensíveis;
3. identificar escopo, origem e destinos;
4. revogar credenciais e sessões afetadas;
5. remover dados expostos dos sistemas controlados e avaliar histórico Git;
6. corrigir a causa e criar teste de regressão;
7. documentar incidente e decisão de retomada.

## 13. Checklist antes de publicar

- [ ] Nenhum segredo, dado pessoal, profissional ou de terceiro.
- [ ] Nenhum log, backup, índice, embedding ou modelo local indevido.
- [ ] Licenças e atribuições verificadas.
- [ ] `git status` e diffs revisados.
- [ ] `.gitignore` revisado; arquivos já rastreados verificados.
- [ ] Testes de isolamento executados com dados sintéticos.
- [ ] Documentação não revela caminhos, endereços ou topologia privada.
- [ ] Revisão humana concluída.