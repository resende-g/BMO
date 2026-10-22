# Estado e roadmap do BMO

- **Atualizado em:** 22/10/2026
- **Estado geral:** documentação inicial; o MVP ainda não é reproduzível a partir deste repositório.

## Base desta documentação

Os registros abaixo vêm de três origens, mantidas separadas de propósito:

- **Registro de conversa:** informação fornecida pelo mantenedor a partir de saídas compartilhadas em conversas do projeto. Não foi reexecutada nem reconferida ao escrever este documento e não prova que o ambiente continua igual. É a origem de todos os itens de "Concluído/configurado" e "Testado".
- **Inspeção do repositório:** a página pública do remoto (`github.com/resende-g/BMO`) foi consultada em 22/10/2026, sem autenticação, e informava que o repositório estava vazio. O clone local (branch, `git status`, arquivos rastreados) não foi inspecionado ao redigir este documento: conferir esses pontos antes de depender destas afirmações.
- **Testes desta sessão:** nenhum teste da aplicação foi executado. Foram feitas apenas verificações textuais da documentação (caminhos absolutos, IPs privados, nomes de usuário, chaves e tokens) e do `.gitignore`.

Os scripts de consulta, inferência, avaliação e validação do protótipo estão fora deste repositório e não foram copiados nem executados durante esta revisão.

## Concluído/configurado

Origem de todos os itens: registro de conversa.

- **Acesso remoto:** o Ubuntu local ficou acessível por SSH. O NetBird foi configurado para o acesso entre os dispositivos registrados e a conexão foi relatada como ativa; um diagnóstico anterior, porém, mostrou o peer de um dos dispositivos sem handshake naquele instante. **A conectividade atual deve ser revalidada de ponta a ponta antes de depender dela.**
- **Armazenamento e cópia:** um disco externo registrou 932 GB totais, 324 GB usados e 608 GB livres. Foi criada a estrutura `BMO-Backup/`, com `bmo-files/`, `logs/`, `ollama-models/` e `system-info/`. Há registro de cópia do diretório BMO e dos dados de modelos do Ollama; a restauração não foi demonstrada.
- **Inferência local:** o Ollama foi usado com `qwen2.5:3b` e `qwen3:1.7b` (medições em "Testado").
- **Protótipo local:** existem fora deste repositório uma busca local sobre o Manifesto, scripts de inferência, um conjunto de avaliação com 12 perguntas (8 respondíveis e 4 sem resposta no documento) e um validador de isolamento. O script de busca foi alterado para separar a coleção do Manifesto da coleção pessoal; essa correção ainda não foi comprovada na versão implantada no Ubuntu.

## Testado

Origem de todos os resultados: registro de conversa. Nenhum deles foi reexecutado nesta sessão.

| Área | Resultado registrado | Limite do resultado |
|---|---|---|
| Inferência `qwen2.5:3b` | Uma resposta em **3,384 s**. | Uma pergunta por execução; não mede qualidade nem constitui benchmark comparável. O script antigo gravava a resposta do modelo no log JSON. |
| Inferência `qwen3:1.7b` | Uma resposta em **2,347 s**. | Uma pergunta por execução; não é comparável ao teste anterior sem prompts e condições idênticos. |
| Consulta ao Manifesto | Uma consulta local foi executada pelo protótipo de busca. | A revisão encontrou erro factual e afirmações sem apoio suficiente. O critério do MVP não foi atendido. |
| Isolamento de coleções | O validador reportou separação entre a coleção do Manifesto e um canário sintético, índices distintos e permissões locais `700/600`. | Os embeddings foram simulados: não mede qualidade semântica nem verifica a versão implantada no Ubuntu. |
| Treino LoRA de fumaça | Execução concluída em 2 passos, com loss registrada de 4,6103 e pico de VRAM de 2,13 GiB. | Teste técnico do pipeline, sem avaliação de qualidade. O adapter não foi avaliado como melhoria e está fora do MVP. |

### Problema de escopo encontrado na busca

Uma versão anterior da busca padrão misturou conteúdo pessoal com a consulta ao Manifesto. O script local foi alterado para separar as coleções e houve uma validação com canário sintético. Como a validação usou embeddings simulados e a versão corrigida ainda não está neste repositório, a correção precisa ser revalidada antes de incluir qualquer conteúdo pessoal.

## Planejado

1. **Fixar o escopo:** manter o Manifesto como única coleção padrão. A coleção pessoal permanece opcional, separada e local; nenhum documento pessoal entra no Git.
2. **Comparar modelos:** testar, sob as mesmas perguntas e configurações, `qwen3:1.7b` Q4_K_M e `llama3.2:1b-instruct-q4_K_M`. Confirmar as tags e quantizações exatas antes de registrar uma escolha.
3. **Medir a recuperação:** executar os 12 casos preparados (8 respondíveis e 4 sem resposta) com embeddings reais do Ollama e registrar o `Hit@4`: perguntas respondíveis com pelo menos um trecho esperado entre os quatro primeiros ÷ 8. A meta proposta para o conjunto é 8/8; ela não substitui a revisão das respostas.
4. **Revisar as respostas:** exigir suporte textual para as afirmações e abstinência nas 4 perguntas sem resposta. Critério proposto: 8/8 respostas respondíveis apoiadas pelos trechos exibidos e 0/4 respostas sem evidência que afirmem fatos como se estivessem no documento.
5. **Revalidar a privacidade:** executar o validador com embeddings reais e canário sintético; confirmar que a coleção pessoal só é lida quando selecionada explicitamente, que os índices permanecem separados e que logs persistentes não guardam perguntas nem respostas.
6. **Fechar a operação:** versionar neste repositório o código e as fixtures públicas ou sintéticas, documentar a instalação e a execução, revisar logs e arquivos locais para excluir dados privados e testar a restauração do backup.

As metas e os critérios acima são propostas; nenhum foi medido.

## Pendente

- Conferir o clone local (branch, `git status`, arquivos rastreados e remoto) e ajustar esta documentação se houver código ou trabalho local não registrado aqui.
- Incorporar ao repositório o código do protótipo e o conjunto de avaliação de 12 perguntas, sem documentos pessoais, índices, logs nem modelos.
- Executar a avaliação completa e reproduzível (recuperação e revisão das respostas); ela ainda não passou.
- Confirmar a correção de isolamento na versão que será publicada e na versão implantada no Ubuntu.
- Revisar os logs locais antes de publicá-los ou de copiar qualquer arquivo deles para o repositório.
- Revalidar o acesso SSH via NetBird e testar a restauração do backup.
- Escolher o modelo final e a quantização e escrever instruções reproduzíveis de instalação e execução.
- Decidir a licença do projeto: ainda não foi escolhida, e nenhuma foi adotada automaticamente.
- Se o texto do Manifesto for versionado, registrar a edição ou tradução usada e confirmar que ela pode ser redistribuída.

## Critério de saída do MVP

Marcar o MVP como concluído somente quando o código estiver neste repositório, a execução local puder ser repetida, os critérios propostos de recuperação e resposta forem atingidos, a coleção pessoal passar pelo teste de isolamento e os arquivos locais com dados privados estiverem excluídos do conjunto de publicação.