# BMO Model Lab — Protocolo de Avaliação de Modelos

## 1. Objetivo

Estabelecer um processo reproduzível para comparar modelos locais e registrar limitações. O objetivo inicial é selecionar um modelo utilizável no hardware de referência, não treinar um modelo do zero.

## 2. Estado atual

Há registros históricos de inferência isolada com `qwen2.5:3b` e `qwen3:1.7b`, além de um smoke test QLoRA e uma avaliação A/B exploratória em 2026-11-02. O experimento QLoRA validou a execução técnica do pipeline, mas não demonstrou ganho de qualidade. A avaliação A/B apresenta uma diferença de tokenizer/template entre as condições e precisa ser repetida antes de qualquer conclusão causal. Consulte `STATUS.md` e o [registro detalhado](experiments/2026-11-02-qwen3-1.7b-qlora-smoke.md).

Não há neste repositório harness de avaliação, dataset de treinamento ou JSON de resultados versionados. Os artefatos locais permanecem fora do Git.

## 3. Categorias de avaliação

Manter resultados separados para:

1. **Inferência:** latência, throughput, consumo de RAM/VRAM e estabilidade.
2. **Qualidade:** correção, completude, aderência à instrução e calibração.
3. **RAG:** fidelidade às fontes, recuperação e abstenção.
4. **Tool calling:** validade de argumentos, escolha de ferramenta e respeito a permissões.
5. **Contexto:** degradação com aumento do contexto e recuperação de informações relevantes.
6. **Segurança:** resistência a prompt injection em documentos, recusa de ações não autorizadas e não exposição de segredos.
7. **Adaptação:** comparação controlada entre modelo-base e adapter.

## 4. Protocolo de comparação

Para cada experimento registrar:
- identificador e data;
- modelo, tag, quantização e hash quando disponível;
- versão do runtime e sistema;
- hardware e uso concorrente;
- tokenizer e chat template (identificador/hash, quando possível);
- template de prompt;
- parâmetros de geração;
- tamanho do contexto;
- dataset e versão;
- número de repetições;
- métricas, falhas e observações;
- decisão e limitações.

Comparar modelos com as mesmas perguntas, instruções, tokenizer/chat template, parâmetros equivalentes e condições de execução. Quando uma configuração não puder ser igualada, declarar a diferença e não atribuir causalmente o resultado à única variável pretendida.

Em comparação base-versus-adapter, o tokenizer e o chat template devem ser idênticos entre condições, salvo quando a alteração de template for a variável explicitamente estudada. A carga do adapter deve ser a única diferença relevante no teste de efeito do LoRA.

## 5. Métricas mínimas

| Dimensão | Métrica ou evidência |
|---|---|
| Latência | tempo até primeiro token e tempo total |
| Throughput | tokens/s, quando mensurável |
| Memória | pico de RAM e VRAM; distinguir memória do processo e memória total da placa |
| Estabilidade | erros, timeouts e interrupções |
| Qualidade | rubrica humana com exemplos e justificativa |
| RAG | Hit@k, suporte textual e abstenção |
| Tool calling | taxa de argumentos válidos e seleção correta |
| Segurança | taxa de bloqueio de ações não autorizadas; testes de injection |

Não condensar tudo em uma única nota sem explicar pesos e critérios. Métricas automáticas não substituem revisão humana. Registrar truncamento por limite de tokens como falha de completude, não como resposta integral.

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

O Qwen3-1.7B utilizado no smoke test de 2026-11-02 não foi selecionado como modelo-base definitivo do BMO.

## 8. Fine-tuning, LoRA e QLoRA

Fine-tuning não substitui RAG. Usar adaptação somente quando houver:
- tarefa estável e bem delimitada;
- dataset legalmente utilizável e representativo;
- baseline do modelo base;
- métrica de sucesso definida;
- conjunto de validação/teste separado;
- comparação de regressões e capacidade de rollback.

Registrar base model, adapter, parâmetros, dataset, seed quando aplicável, hardware, tempo, consumo, loss e avaliação antes/depois. Um treino que termina sem erro demonstra apenas execução do pipeline, não ganho de qualidade.

### 8.1 Registro: QLoRA smoke test de 2026-11-02

- Base: Qwen/Qwen3-1.7B, revisão `70d244cc86ccca08cf5af4e1e306ecf908b1ad5e`.
- Método: QLoRA NF4 4-bit com double quantization e LoRA.
- Dataset: 8 exemplos; SHA-256 `6264401aa997c90daed7062aff53305d1e3d055f44fd60902694d44fd3e6bbdb`.
- Passos: 2.
- Parâmetros treináveis: 8.716.288 (aprox. 0,504%).
- Loss final registrada: 4,376685.
- Pico de VRAM reportado: 2,13 GiB.
- Adapter SHA-256: `2c707c951ef31ff8d3d31107ca581cfd61bacdc34afb85668af8a291cdbcb040`.

O treino concluiu e salvou o adapter. O resultado valida o pipeline técnico, não aprendizado conceitual nem melhoria. O dataset é pequeno e há alto risco de sobreajuste. O adapter e os dados permanecem no ambiente local e não são publicados por padrão.

### 8.2 Avaliação A/B exploratória de 2026-11-02

Foram executados oito prompts em cada condição (fidelidade textual, interpretação, extrapolação e abstenção), totalizando 16 gerações sem erro. A avaliação qualitativa não observou melhora consistente do adapter. Ambos os modelos erraram questões de fidelidade/extrapolação e ambos se abstiveram adequadamente em duas perguntas sem evidência.

**Validade limitada:** a execução carregou tokenizer do modelo-base em A_base e tokenizer do diretório do adapter em B_adapter. O adapter contém um chat template personalizado de treinamento. Essa diferença confunde a comparação; não atribuir os resultados ao efeito do LoRA. Além disso, respostas foram limitadas a 220 tokens e algumas ficaram truncadas.

Antes de repetir:
1. carregar tokenizer e chat template do modelo-base nas duas condições;
2. manter iguais prompt, parâmetros de geração e perguntas;
3. aumentar o limite de geração para evitar truncamento;
4. usar rubrica explícita para fidelidade, precisão conceitual, suporte documental e abstenção;
5. registrar resultados completos e manter os artefatos privados fora do Git.

O registro detalhado está em [experiments/2026-11-02-qwen3-1.7b-qlora-smoke.md](experiments/2026-11-02-qwen3-1.7b-qlora-smoke.md).

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
  revision: ""
  quantization: ""
tokenizer:
  source: ""
  chat_template_hash: ""
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
