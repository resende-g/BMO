# Changelog

Mudanças relevantes do projeto e da documentação. Este arquivo não substitui o histórico Git.

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
