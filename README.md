# BMO

Projeto pessoal experimental de um assistente local para consultar documentos com modelos executados pelo [Ollama](https://ollama.com). Começou no Ubuntu e prioriza execução local, referências verificáveis e separação entre coleções de documentos.

> **Estado:** o MVP ainda não está concluído. Este repositório contém, por enquanto, a documentação inicial do projeto; os scripts do protótipo estão em outra pasta local e ainda não foram incorporados aqui. Clonar este repositório, por enquanto, não instala nem executa o BMO.

Origem dos registros, limites de cada resultado e roadmap: [STATUS.md](STATUS.md).

## Objetivo do MVP

Entregar uma ferramenta de linha de comando, local no Ubuntu e baseada no Ollama, que responda perguntas sobre o Manifesto do Partido Comunista usando trechos recuperados localmente e mostre esses trechos com suas fontes. Uma coleção pessoal poderá ser consultada somente quando selecionada explicitamente e deverá manter arquivos e índice separados da coleção pública e fora do Git.

O MVP será considerado pronto quando:

- a execução puder ser reproduzida a partir do código versionado e do Ollama local;
- a coleção padrão contiver apenas o documento público definido para a avaliação;
- cada consulta mostrar os trechos recuperados, o arquivo e o número do trecho;
- o BMO declarar quando não houver evidência suficiente, sem completar lacunas com fatos inventados;
- a avaliação reproduzível de 12 perguntas (8 respondíveis e 4 sem resposta no documento) atingir os critérios propostos abaixo;
- um canário sintético da coleção pessoal não aparecer na busca padrão e a busca pessoal permanecer opt-in;
- perguntas e respostas não forem gravadas em logs persistentes.

### Critérios propostos para a avaliação

São metas propostas; nenhuma foi medida até agora.

- **Recuperação:** `Hit@4` igual a 8/8. O `Hit@4` é o número de perguntas respondíveis com pelo menos um trecho esperado entre os quatro primeiros resultados, dividido por 8.
- **Perguntas respondíveis:** revisão humana confirmando que as 8 respostas são apoiadas pelos trechos exibidos.
- **Perguntas sem resposta no documento:** 0/4 respostas que afirmem fatos como se estivessem no documento.

O `Hit@4` mede apenas a recuperação e não substitui a revisão das respostas.

## Fora do MVP

Interface web ou móvel, serviço público na internet e uso do adapter LoRA ficam fora do primeiro MVP.

## Estado atual

Resumo. Os registros de ambiente, backup e testes vêm de saídas compartilhadas em conversas do projeto e não foram reexecutados ao escrever esta documentação; números e limites estão em [STATUS.md](STATUS.md).

- Houve testes isolados de inferência com `qwen2.5:3b` e `qwen3:1.7b`, com uma pergunta por execução. Não são um benchmark comparável nem medem a qualidade geral das respostas.
- Uma consulta local ao Manifesto foi executada e revisada: a revisão encontrou erro factual e afirmações sem apoio suficiente. O critério do MVP ainda não foi atendido.
- O conjunto de 12 perguntas foi preparado, mas ainda não está neste repositório nem foi executado como avaliação completa.
- Uma versão anterior da busca padrão misturou conteúdo pessoal com a consulta ao Manifesto. O script local foi alterado para separar as coleções, mas a correção ainda precisa ser revalidada, com embeddings reais e na versão implantada, antes de usar qualquer conteúdo pessoal.
- Um treino LoRA de fumaça foi concluído para verificar o pipeline. O adapter não foi avaliado como melhoria de qualidade e não faz parte do MVP.
- O acesso remoto ao Ubuntu local deve ser revalidado, e a restauração do backup em disco externo ainda não foi comprovada.

## Como executar

Ainda não há instruções de instalação ou execução, porque o código do BMO não está neste repositório. Elas serão adicionadas quando o código for incorporado e a execução puder ser reproduzida.

## Privacidade e publicação

- Não versionar documentos pessoais, índices, embeddings, modelos, adapters, logs de execução, chaves, endereços privados nem caminhos absolutos do computador.
- Usar apenas dados públicos e fixtures sintéticas no repositório. O contexto pessoal, se habilitado localmente, deve permanecer fora do Git.
- Revisar os logs locais antes de publicar: um script antigo de inferência gravava a resposta do modelo no arquivo JSON de log, e não há confirmação sobre o conteúdo dos demais logs existentes.
- O validador de isolamento registrado usou um canário sintético e embeddings simulados. Isso verifica separação básica, mas não mede qualidade semântica nem substitui a conferência da versão implantada no Ubuntu.
- O `.gitignore` reduz o risco de commits acidentais, mas não remove arquivos já rastreados nem apaga o histórico. Conferir `git status` e `git diff --staged` antes de cada commit.

## Modelos

`qwen2.5:3b` e `qwen3:1.7b` aparecem em testes de inferência; a escolha final depende de avaliação controlada. `qwen3:1.7b` com quantização `Q4_K_M` e `llama3.2:1b-instruct-q4_K_M` foram sugeridos como candidatos para comparação via Ollama. Não há evidência de que ambos tenham sido avaliados com o mesmo conjunto de prompts e métricas.

## Licença

Ainda não definida: a escolha é uma decisão pendente do mantenedor. Enquanto não houver um arquivo de licença, o projeto não declara licença de uso, cópia ou distribuição.