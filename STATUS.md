# STATUS — Estado verificável do BMO

- **Data desta revisão documental:** 2026-11-02
- **Repositório inspecionado:** `resende-g/BMO`
- **Branch remota consultada:** `main`
- **Estado geral:** documentação arquitetural publicada; não há código de aplicação versionado na árvore remota inspecionada.
- **Limite da inspeção:** a revisão consultou a árvore e os arquivos da branch remota. O clone local, seu `git status`, arquivos não rastreados e alterações ainda não publicadas não foram inspecionados.

## 1. Estado do repositório remoto

A árvore Git consultada antes desta publicação continha somente `README.md` e `STATUS.md`. Este commit acrescenta a documentação arquitetural listada no README. Não foram encontrados código-fonte, scripts, manifests de dependências, testes, configuração de containers ou workflows de CI na árvore remota consultada.

O README original informa que os scripts do protótipo permanecem em uma pasta local e ainda não foram incorporados. A documentação arquitetural desta revisão foi publicada na branch `main`; as implementações descritas continuam sendo propostas e não funcionalidades disponíveis.

## 2. Estados por componente

| Componente/capacidade | Estado | Evidência e limite |
|---|---|---|
| Documentação inicial | Implementado | README e STATUS já estavam na branch remota |
| d-BMO | Planejado | Nenhuma implementação encontrada na árvore |
| BMO Brain | Planejado | Nenhuma implementação encontrada na árvore |
| BMO Heart | Planejado | Nenhuma implementação encontrada na árvore; dados pessoais não devem ser publicados |
| BMO Knowledge | Planejado / protótipo externo relatado | Scripts externos mencionados em documentação anterior, não versionados |
| BMO Model Lab | Planejado | Há relato histórico de teste LoRA, sem harness versionado |
| Hermes Agent | Em avaliação | Nenhuma integração versionada |
| Ollama | Testado historicamente | Uso relatado em conversas; runtime e versão atuais não foram revalidados nesta revisão |
| Docker | Planejado | Nenhuma configuração encontrada |
| NetBird | Configurado historicamente | Conectividade atual não revalidada |
| Skills | Planejado | Nenhum manifesto ou executor versionado |
| Licença | Pendente | Nenhum arquivo de licença encontrado |

## 3. Registros históricos não reexecutados

Os resultados a seguir foram registrados em documentação anterior com origem em saídas compartilhadas pelo mantenedor. Não foram reexecutados nesta revisão e não devem ser tratados como benchmark atual.

| Área | Resultado histórico | Limitação |
|---|---|---|
| `qwen2.5:3b` | Uma resposta em 3,384 s | Uma pergunta isolada; não mede qualidade nem é benchmark comparável |
| `qwen3:1.7b` | Uma resposta em 2,347 s | Uma pergunta isolada sob condições não demonstradas como idênticas |
| Consulta ao Manifesto | Uma consulta local revisada | Revisão encontrou erro factual e afirmações sem suporte suficiente |
| Isolamento de coleções | Validador relatou separação e canário sintético | Embeddings simulados; não valida a versão implantada com embeddings reais |
| LoRA de fumaça | 2 passos, loss registrada 4,6103 e pico de VRAM 2,13 GiB | Demonstra execução de pipeline, não melhoria de qualidade |

## 4. Riscos e pendências prioritárias

1. **Isolamento documental:** houve relato de mistura anterior entre coleção pessoal e consulta pública. A correção relatada precisa ser revalidada com embeddings reais e na versão efetivamente implantada antes de inserir qualquer conteúdo pessoal.
2. **Logs:** um script antigo teria gravado respostas em log JSON. O conteúdo dos demais logs não foi verificado; revisar localmente antes de publicar ou compartilhar.
3. **Reprodutibilidade:** código, dependências, fixtures públicas/sintéticas e conjunto de 12 perguntas ainda não estão no repositório.
4. **Avaliação:** o conjunto de 12 perguntas (8 respondíveis e 4 sem resposta) e os critérios de Hit@4/abstenção ainda não foram executados integralmente conforme protocolo reproduzível.
5. **Backup:** há registro histórico de cópia para disco externo, mas restauração não demonstrada.
6. **Acesso remoto:** NetBird/SSH foi configurado historicamente; conectividade deve ser revalidada de ponta a ponta.
7. **Ambiente:** hardware e versões são referências informadas pelo mantenedor, não medições executadas nesta revisão.
8. **Licença:** decisão pendente. Não presumir licença do projeto ou compatibilidade de dependências.

## 5. Próximas ações

A ordem e os critérios detalhados estão em [ROADMAP.md](ROADMAP.md). Prioridades imediatas:

- conferir o clone local e alterações não publicadas;
- revisar logs e artefatos locais sem copiar dados privados para o Git;
- revalidar isolamento de coleções com dados sintéticos e embeddings reais;
- versionar apenas código e fixtures autorizados;
- executar avaliação controlada e documentar resultados;
- testar restauração de backup;
- selecionar licença e revisar dependências antes de publicação.

## 6. Proveniência desta revisão

A árvore remota foi consultada em 2026-11-02 e atualizada por um commit documental nesta data. Nenhum teste de aplicação, inferência, RAG, rede, backup ou sandbox foi executado nesta revisão. Nenhum dado local foi inspecionado. A ausência de arquivos na árvore remota não permite concluir que não existam protótipos no computador do mantenedor.