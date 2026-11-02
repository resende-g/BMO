# Roadmap do d-BMO

Este roadmap organiza a evolução em marcos verificáveis. A sequência é uma referência: não obriga implementar todos os módulos antes de validar o MVP documental.

## Estado resumido

| Marco | Escopo | Estado |
|---|---|---|
| M0 | Diagnóstico e preparação | Parcial; documentação histórica disponível, verificações atuais pendentes |
| M1 | Inferência local | Testes isolados registrados; avaliação controlada pendente |
| M2 | Agente e orquestração | Planejado |
| M3 | Execução segura | Planejado |
| M4 | Conhecimento e skills | Protótipo externo; integração versionada planejada |
| M5 | Memória e acesso remoto | NetBird configurado historicamente; Heart planejado |
| M6 | Interface e evolução | Planejado |

## M0 — Diagnóstico e preparação

**Objetivo:** conhecer e estabilizar o ambiente e o estado do repositório.

Tarefas:
- [ ] Inventariar hardware, sistema, drivers e versões.
- [ ] Confirmar instalação e versão do Ollama.
- [ ] Conferir modelos e armazenamento local.
- [ ] Verificar backup e realizar teste de restauração.
- [x] Inspecionar árvore pública e documentação atual do GitHub.
- [ ] Conferir clone local, branch, `git status`, arquivos rastreados e diferenças não publicadas.
- [ ] Revisar logs e artefatos locais antes de qualquer publicação.
- [x] Definir licença do projeto (Apache-2.0).

**Conclusão:** inventário datado, riscos identificados, backup restaurável e repositório sem dados privados.

## M1 — Inferência local

**Objetivo:** estabelecer baseline de inferência e selecionar modelo inicial.

Tarefas:
- [ ] Fixar versões de Ollama, modelo e quantização.
- [ ] Comparar candidatos sob prompts, contexto e parâmetros idênticos.
- [ ] Medir latência, RAM, VRAM, tokens/s quando disponível e falhas.
- [ ] Avaliar qualidade factual, abstenção e tool calling.
- [ ] Registrar condições e resultados no Model Lab.

**Conclusão:** relatório reproduzível e modelo selecionado com limitações conhecidas. Testes históricos isolados não substituem este marco.

## M2 — Agente e orquestração

**Objetivo:** criar o fluxo mínimo do Brain e decidir a integração do Hermes.

Tarefas:
- [ ] Definir contratos de sessão, inferência, ferramenta e erro.
- [ ] Construir um fluxo simples de solicitação-resposta.
- [ ] Avaliar Hermes em ambiente de teste.
- [ ] Implementar adaptador sem acoplar o domínio d-BMO ao framework.
- [ ] Validar tool calls e limites de iteração.

**Conclusão:** uma tarefa simples executada ponta a ponta, com runtime substituível e sem permissão implícita para operações sensíveis.

## M3 — Execução segura

**Objetivo:** executar ferramentas sob controle explícito.

Tarefas:
- [ ] Definir matriz de permissões por skill.
- [ ] Implementar Policy Gate e confirmação humana.
- [ ] Integrar executor isolado.
- [ ] Configurar usuário não privilegiado, limites de CPU/RAM/processos, filesystem mínimo e rede restrita.
- [ ] Bloquear acesso de escrita ao Heart.
- [ ] Registrar auditoria sem persistir conteúdo sensível desnecessário.

**Conclusão:** testes demonstram que operações não autorizadas são negadas, limites são aplicados e ações aprovadas são auditáveis.

## M4 — Conhecimento e skills

**Objetivo:** disponibilizar RAG local e capacidades modulares iniciais.

Tarefas:
- [ ] Versionar código de ingestão e fixtures públicas/sintéticas.
- [ ] Implementar metadados de documento e referências a página/trecho.
- [ ] Implementar busca lexical com SQLite FTS5.
- [ ] Avaliar embeddings locais somente se a busca lexical for insuficiente.
- [ ] Implementar registro e validação de skills.
- [ ] Criar `system-audit`, `code-review` e `report-generator` em escopo inicial seguro.
- [ ] Planejar skills de rede apenas com escopo autorizado e ambiente de laboratório.

**Conclusão:** consulta reproduzível com fontes, isolamento de coleções validado e skills com permissões testadas.

## M5 — Memória e acesso remoto

**Objetivo:** implementar memória pessoal revisável e confirmar acesso privado.

Tarefas:
- [ ] Definir esquema, proveniência e estados de memória.
- [ ] Implementar proposta, aprovação, correção, versionamento e exclusão.
- [ ] Aplicar controles de acesso e trilha de auditoria.
- [ ] Garantir que ferramentas não escrevam diretamente no armazenamento.
- [ ] Testar isolamento de memória e Knowledge.
- [ ] Revalidar NetBird e autenticação da aplicação.
- [ ] Testar backup e restauração do Heart.

**Conclusão:** usuário controla ciclo de vida da memória, alterações são rastreáveis e acesso remoto não expõe serviços publicamente.

## M6 — Interface e evolução

**Objetivo:** desenvolver a d-BMO Interface e melhorar a experiência integrada.

Tarefas:
- [ ] Definir API local do Brain.
- [ ] Construir interface conversacional.
- [ ] Apresentar estado, autorização, erros e fontes.
- [ ] Construir dashboard de atividade.
- [ ] Expor controles de memória e Knowledge.
- [ ] Integrar Model Lab para consulta de resultados.
- [ ] Avaliar necessidade de novos processos, agentes ou serviços.

**Conclusão:** fluxo completo utilizável, estados claros, controles acessíveis e sem duplicar regras de negócio na interface.

## Critérios transversais de saída

Nenhum marco é concluído apenas por “funcionar uma vez”. Exigir:
- instruções reproduzíveis;
- testes adequados ao risco;
- versões e configurações registradas;
- ausência de segredos e dados privados no Git;
- documentação atualizada;
- limitações conhecidas;
- evidência verificável.

## Próxima prioridade recomendada

Fechar M0 e M1 antes de iniciar uma integração ampla com Hermes. Em paralelo, consolidar a separação de coleções do protótipo documental, pois o histórico registra uma falha anterior nesse limite.