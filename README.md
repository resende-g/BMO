# Dark BMO (d-BMO)

**d-BMO (BE MORE DARK)** é um projeto pessoal de assistente de inteligência artificial local-first. Seu objetivo é evoluir de um protótipo de consulta documental para uma infraestrutura pessoal modular, auditável e controlada pelo usuário, capaz de integrar modelos locais, memória persistente, conhecimento documental e ferramentas com permissões explícitas.

O nome **Dark BMO** pode ser utilizado como denominação do projeto; **d-BMO** permanece a sigla e identidade principal. **d-BMO** designa a futura interface e identidade visual. **BMO Heart** é o módulo de memória pessoal.

> **Estado atual do repositório:** documentação inicial. Não há código de aplicação versionado nesta branch. Os scripts do protótipo mencionados em `STATUS.md` permanecem externos ao repositório. Portanto, clonar este projeto ainda não instala nem executa um assistente d-BMO.

## Princípios

- **Local-first:** inferência e processamento de dados pessoais devem ocorrer localmente.
- **Privacidade por padrão:** nenhum dado pessoal ou confidencial é enviado a serviços externos automaticamente.
- **Modularidade:** componentes independentes, com contratos explícitos e substituíveis.
- **Portabilidade:** o d-BMO não depende estruturalmente de um modelo, runtime ou framework de agentes.
- **Segurança:** menor privilégio, isolamento de execução, autorização humana e auditoria.
- **Transparência:** origem, estado e alterações relevantes devem ser rastreáveis.
- **Evolução incremental:** implementar o menor componente que resolva uma necessidade demonstrada.
- **Reprodutibilidade:** registrar versões, configurações, datasets e resultados.
- **Controle humano:** ações sensíveis não são executadas sem autorização explícita.

## Arquitetura em desenvolvimento

A arquitetura proposta separa responsabilidades:

| Componente | Responsabilidade | Estado |
|---|---|---|
| d-BMO | Interface, identidade visual e dashboard | Planejado |
| BMO Brain | Orquestração, sessões, contexto e fluxo de ferramentas | Planejado |
| BMO Heart | Memória pessoal persistente, revisável e auditável | Planejado |
| BMO Knowledge | Ingestão, indexação e recuperação documental (RAG) | Planejado |
| BMO Model Lab | Avaliação e experimentação de modelos | Planejado |
| Adaptador Hermes | Integração opcional com infraestrutura de agente | Em avaliação |
| Ollama | Primeiro runtime candidato para inferência local | Testado historicamente; integração no repositório não implementada |
| Docker | Isolamento de ferramentas e tarefas | Planejado |
| NetBird | Conectividade privada para acesso remoto | Configurado historicamente; estado atual não revalidado |

A arquitetura detalhada, os limites de confiança e as relações entre módulos estão em [ARCHITECTURE.md](ARCHITECTURE.md).

## MVP documental atual

O escopo original do protótipo é uma ferramenta local de consulta ao *Manifesto do Partido Comunista*, usando Ollama e recuperação de trechos, com exibição de fontes. A coleção pessoal deve ser separada e habilitada apenas por seleção explícita.

O MVP não deve ser considerado concluído até que:
1. o código esteja versionado e a execução seja reproduzível;
2. a coleção padrão contenha somente o documento público definido para avaliação;
3. as respostas exibam trechos e referências verificáveis;
4. o sistema se abstenha quando não houver evidência suficiente;
5. a avaliação documentada seja executada e revisada;
6. a separação entre coleções seja validada com embeddings reais;
7. perguntas e respostas não sejam persistidas em logs sem decisão explícita e controles próprios.

Os critérios e resultados históricos estão descritos em [STATUS.md](STATUS.md). As etapas futuras estão em [ROADMAP.md](ROADMAP.md).

## Documentação

- [ARCHITECTURE.md](ARCHITECTURE.md): arquitetura lógica, módulos, interfaces e fluxos.
- [ROADMAP.md](ROADMAP.md): etapas, prioridades e critérios de conclusão.
- [SECURITY.md](SECURITY.md): privacidade, segurança, permissões e governança.
- [MODEL_EVALUATION.md](MODEL_EVALUATION.md): protocolo de avaliação de modelos.
- [RAG.md](RAG.md): pipeline documental e recuperação.
- [SKILLS.md](SKILLS.md): contrato e catálogo inicial de habilidades.
- [STATUS.md](STATUS.md): evidências históricas, limitações e pendências do protótipo.
- [CHANGELOG.md](CHANGELOG.md): mudanças relevantes na documentação e no projeto.
- [docs/brand/README.md](docs/brand/README.md): documentação da identidade visual do d-BMO, tokens, personagem e interface.

## Ambiente conhecido

As informações abaixo são a configuração de referência informada pelo mantenedor, não requisitos universais nem uma inspeção executada nesta revisão:

- Ubuntu 26.04.1; kernel 7.0.0-38.
- AMD Ryzen 3 3300X (4 núcleos / 8 threads).
- NVIDIA GTX 1050 Ti (4 GB VRAM).
- 24 GB RAM.
- Ollama como runtime local inicial.

A seleção de modelos deve considerar VRAM, RAM, contexto, latência e qualidade de uso de ferramentas. Não há modelo final selecionado.

## Início

Ainda não existem instruções de instalação ou execução válidas. Não execute comandos presumidos de instalação. A documentação de instalação será adicionada quando o código, as dependências e os testes estiverem versionados e forem reproduzíveis.

## Segurança e dados

O repositório público deve conter somente código, documentação e dados públicos ou sintéticos autorizados. Memórias pessoais, documentos privados, dados profissionais, históricos de conversa, índices, embeddings privados, modelos locais, adapters, logs e backups devem permanecer fora do Git.

Consulte [SECURITY.md](SECURITY.md) antes de adicionar dados, integrações ou ferramentas.

## Licença

A licença do projeto ainda não foi definida. Não presuma autorização de uso, cópia ou redistribuição até que uma licença seja escolhida e publicada. A integração de componentes de terceiros exige verificação das licenças e avisos aplicáveis às versões efetivamente utilizadas.
