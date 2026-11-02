# BMO Model Lab — Protocolo de Avaliação de Modelos

## 1. Objetivo

Estabelecer um processo reproduzível para comparar modelos locais e registrar limitações. O objetivo inicial é selecionar um modelo utilizável no hardware de referência, não treinar um modelo do zero.

## 2. Estado atual

Há registros históricos de inferência isolada com `qwen2.5:3b` e `qwen3:1.7b`, além de um teste LoRA de fumaça. Esses registros não constituem benchmark comparável e não demonstram melhoria de qualidade. Consulte `STATUS.md`.

Não há neste repositório harness de avaliação, dataset versionado ou resultados reproduzíveis.

## 3. Categorias de avaliação

Manter resultados separados para:

1. **Inferência:** latência, throughput, consumo de RAM/VRAM e estabilidade.
2. **Qualidade:** correção, completude, aderência à instrução e calibração.
3. **RAG:** fidelidade às fontes, recuperação e abstenção.
4. **Tool calling:** validade de argumentos, escolha de ferramenta e respeito a permissões.
5. **Contexto:** degradação com aumento do contexto e recuperação de informações relevantes.
6. **Segurança:** resistência a prompt injection em documentos, recusa de ações não autorizadas e não exposição de segredos.
7. **Adaptação:** comparação controlada entre modelo base e adapter.

## 4. Protocolo de comparação

Para cada experimento registrar:
- identificador e data;
- modelo, tag, quantização e hash quando disponível;
- versão do runtime e sistema;
- hardware e uso concorrente;
- template de prompt;
- parâmetros de geração;
- tamanho do contexto;
- dataset e versão;
- número de repetições;
- métricas, falhas e observações;
- decisão e limitações.

Comparar modelos com as mesmas perguntas, instruções, parâmetros equivalentes e condições de execução. Quando uma configuração não puder ser igualada, declarar a diferença.

## 5. Métricas mínimas

| Dimensão | Métrica ou evidência |
|---|---|
| Latência | tempo até primeiro token e tempo total |
| Throughput | tokens/s, quando mensurável |
| Memória | pico de RAM e VRAM |
| Estabilidade | erros, timeouts e interrupções |
| Qualidade | rubrica humana com exemplos e justificativa |
| RAG | Hit@k, suporte textual e abstenção |
| Tool calling | taxa de argumentos válidos e seleção correta |
| Segurança | taxa de bloqueio de ações não autorizadas; testes de injection |

Não condensar tudo em uma única nota sem explicar pesos e critérios. Métricas automáticas não substituem revisão humana.

## 6. Dataset inicial do MVP documental

O conjunto descrito no `README.md`/`STATUS.md` contém 12 perguntas: 8 respondíveis e 4 sem resposta no documento.

Critérios propostos:
- `Hit@4 = 8/8` nas perguntas respondíveis;
- 8/8 respostas respondíveis apoiadas pelos trechos exibidos;
- 0/4 respostas sem evidência que afirmem fatos como se estivessem no documento.

A meta é proposta e ainda não foi atingida. O conjunto deve ser versionado somente após revisão de licença e remoção de conteúdo privado. Registrar resposta esperada, trechos de referência e rubrica de avaliação.

## 7. Candidatos e hardware

Hardware informado: Ryzen 3 3300X, GTX 1050 Ti 4 GB e 24 GB RAM. Candidatos registrados historicamente incluem `qwen2.5:3b`, `qwen3:1.7b`, `qwen3:1.7b` Q4_K_M e `llama3.2:1b-instruct-q4_K_M`.

Esses nomes são candidatos históricos, não recomendação definitiva. Confirmar tags e quantizações disponíveis no runtime antes de executar. A avaliação deve medir CPU offload, memória e velocidade real no equipamento.

## 8. Fine-tuning, LoRA e QLoRA

Fine-tuning não substitui RAG. Usar adaptação somente quando houver:
- tarefa estável e bem delimitada;
- dataset legalmente utilizável e representativo;
- baseline do modelo base;
- métrica de sucesso definida;
- conjunto de validação/teste separado;
- comparação de regressões e capacidade de rollback.

Registrar base model, adapter, parâmetros, dataset, seed quando aplicável, hardware, tempo, consumo, loss e avaliação antes/depois. Um treino que termina sem erro demonstra apenas execução do pipeline, não ganho de qualidade.

## 9. Critérios de seleção

Selecionar modelo apenas quando:
- couber no orçamento de RAM/VRAM com margem;
- responder com qualidade aceitável no conjunto relevante;
- apresentar comportamento previsível de abstenção;
- tool calling for confiável para o escopo habilitado;
- limitações e condições estiverem documentadas.

## 10. Modelo de registro

```yaml
experiment_id: "bmo-eval-YYYYMMDD-001"
date: "YYYY-MM-DD"
model:
  name: ""
  tag: ""
  quantization: ""
runtime:
  name: "ollama"
  version: ""
hardware:
  cpu: ""
  gpu: ""
  ram_gb: 0
dataset:
  name: ""
  version: ""
prompt_template: ""
generation:
  temperature: 0
  context_length: 0
runs: 0
metrics:
  latency_ms: null
  tokens_per_second: null
  peak_ram_mb: null
  peak_vram_mb: null
  task_score: null
limitations: []
decision: "pending"
```

Os campos nulos devem ser preenchidos com medições; não estimar valores.