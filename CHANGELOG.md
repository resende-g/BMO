# Changelog

Mudanças relevantes do projeto e da documentação. Este arquivo não substitui o histórico Git.

## [2026-11-02] — Nome do projeto e consistência documental

### Alterado
- Nome do projeto unificado como **d-BMO** (por extenso: BE MORE DARK), substituindo "Beemon (BMO)". A camada de interface passa a ser **d-BMO Interface**; módulos internos mantêm o prefixo BMO (Brain, Heart, Knowledge, Model Lab).
- Estado do BMO Model Lab alinhado entre `README.md`, `ARCHITECTURE.md` e `STATUS.md`.
- `STATUS.md` deixa de apontar para branch de trabalho já mergeada.

### Alterado (repositórios)
- Repositórios renomeados no GitHub: `resende-g/BMO` → `resende-g/d-BMO` e `resende-g/dark-BMO` → `resende-g/d-BMO-body`. Links e nomes atualizados.
- Licença do hardware alinhada: `d-BMO-body` passa a usar Apache-2.0 (com AGPL-3.0 no firmware derivado do Bruce e CERN-OHL-P-2.0 para arquivos de projeto de hardware).

### Adicionado
- Ligação com o hardware em [resende-g/d-BMO-body](https://github.com/resende-g/d-BMO-body): componente "d-BMO-body (corpo físico)" no README e no `STATUS.md`, seção 4.11 da `ARCHITECTURE.md` (cliente da API local, sem acesso ao Heart, ferramentas de RF/NFC/IR fora das skills) e referência na spec do personagem.
- `.gitignore` cobrindo segredos, dados pessoais e de treino, modelos, adapters, índices, embeddings, backups e logs, conforme `SECURITY.md`.
- `LICENSE` Apache-2.0 para código e documentação. Nome, logotipo e personagem ficam fora da licença (§6).
- Personagem redesenhado como videogame portátil de emulação, sem membros, com dois analógicos (`CHARACTER_SPECIFICATION.md` v2.0) e referência conceitual em `docs/brand/assets/`.

## [2026-11-02] — Identidade visual do d-BMO

### Adicionado
- Documentação de marca em `docs/brand/`: diretrizes, design tokens, especificação do personagem e diretrizes de interface (PR #1).

## [2026-11-02] — Registro do smoke test QLoRA e avaliação A/B

### Adicionado
- Registro do experimento QLoRA Qwen3-1.7B com revisão, hashes, dataset, adapter, configuração e métricas reportadas.
- Registro das oito perguntas A/B, observações qualitativas e limitações.
- Documentação explícita da diferença de tokenizer/chat template entre A_base e B_adapter.
- Requisito de tokenizer e chat template idênticos em comparações base-versus-adapter.
- Ressalva de que Qwen3-1.7B é modelo experimental, não seleção definitiva do BMO.

### Não realizado
- Nenhum código de treinamento ou avaliação incorporado ao repositório.
- Nenhum dataset, adapter, JSON de respostas, log ou dado pessoal publicado.
- Nenhum novo teste executado durante esta atualização documental.
- Nenhuma alteração no ambiente local do mantenedor.

## [2026-11-02] — Documentação arquitetural publicada

### Adicionado
- Consolidação da arquitetura modular do Beemon/BMO.
- Definição de responsabilidades para d-BMO, BMO Brain, BMO Heart, BMO Knowledge e BMO Model Lab.
- Registro do Hermes como infraestrutura de agente opcional integrada por adaptador.
- Registro de Ollama, Docker, NetBird, SQLite/FTS5, embeddings locais, Python e Git como tecnologias candidatas ou de suporte, não decisões irreversíveis.
- Formalização de política de segurança, isolamento de coleções, permissões e auditoria.
- Definição de protocolo de avaliação de modelos, RAG, skills e roadmap incremental.
- Preservação dos resultados históricos como registros não reexecutados, sem convertê-los em evidência de implementação atual.

### Não realizado
- Nenhum código de produção implementado.
- Nenhuma dependência instalada.
- Nenhuma configuração do sistema operacional alterada.
