# d-BMO — Diretrizes de interface

**Versão:** 1.0 (diretrizes conceituais)  
**Status:** proposta visual; interface não presumida como implementada

## 1. Objetivo

Aplicar a identidade d-BMO a interfaces funcionais do projeto, mantendo legibilidade, previsibilidade e transparência sobre o estado real do sistema.

A interface é uma camada de apresentação. Regras de negócio, autorização, memória e execução pertencem aos módulos correspondentes do BMO Brain e serviços especializados.

## 2. Princípios

- local-first visível e verificável;
- privacidade por padrão;
- hierarquia clara entre conteúdo, controles e estado;
- feedback explícito para ações e erros;
- confirmação humana para operações sensíveis;
- acessibilidade e contraste;
- ausência de telemetria ou atividade fictícia.

## 3. Linguagem visual

Usar a paleta definida em [DESIGN_TOKENS.md](DESIGN_TOKENS.md):
- preto e grafite para fundos e superfícies;
- prata para estrutura, contornos e hierarquia;
- off-white para texto;
- vermelho para alertas, ações críticas e estados ativos.

Evitar brilho excessivo, ruído decorativo, excesso de painéis e estética de centro de comando militar. A aparência cyberpunk deve permanecer subordinada à função.

## 4. Superfícies previstas

### Interface conversacional
Deve apresentar mensagens, fontes quando aplicável, estado do modelo, indicação de processamento local/remoto e controles claros para interromper ou confirmar ações.

### Terminal/CLI
Deve privilegiar legibilidade, saída estruturada, identificação de comandos e distinção entre simulação, execução e erro. Não executar texto arbitrário produzido pelo modelo sem validação e política de autorização.

### Dashboard
Pode apresentar, quando efetivamente disponível:
- estado do runtime e modelo;
- uso de CPU, RAM e GPU;
- armazenamento;
- estado de conectividade privada;
- módulos e serviços ativos;
- execuções de ferramentas;
- estado de memória e Knowledge.

Não preencher telas com métricas inventadas, dados simulados não identificados ou mapas globais que sugiram vigilância indiscriminada.

### Memória e documentos
Exibir claramente a coleção consultada, proveniência e controles de revisão. Separar visualmente BMO Heart, BMO Knowledge, histórico de sessão e logs operacionais.

## 5. Estados e feedback

Estados devem combinar rótulo textual, ícone e cor:
- ocioso;
- processando;
- aguardando autorização;
- concluído;
- alerta;
- erro;
- offline.

Não usar animação como único indicador. Uma operação só pode aparecer como concluída após confirmação do serviço responsável.

## 6. Segurança e confiança

- Mostrar escopo e permissões antes de ações sensíveis.
- Exigir confirmação para escrita, exclusão, instalação, alteração de configuração, acesso a dados privados e operações de rede ativa.
- Informar quando uma solicitação será encaminhada a serviço externo.
- Não realizar fallback remoto silencioso.
- Não expor segredos em telas, logs ou notificações.
- Permitir interromper tarefas e consultar resultado/auditoria quando suportado.

## 7. Acessibilidade e responsividade

- Contraste suficiente para texto e controles.
- Estados não dependentes apenas de cor.
- Alvos de interação adequados a mouse e toque.
- Layout adaptável a telas pequenas.
- Tipografia legível e escalável.
- Respeitar preferência por redução de movimento quando aplicável.

## 8. Componentes futuros

A biblioteca pode incluir:
- botões primários, secundários e destrutivos;
- campos e seletores;
- cartões de módulo;
- indicadores de estado;
- painel de autorização;
- visualizador de fontes;
- histórico de execução;
- componentes de memória e coleção;
- avatar/expressões do d-BMO.

Cada componente deve ter estados, comportamento, acessibilidade e testes definidos antes de ser considerado implementado.

## 9. Critérios de revisão

Uma interface está alinhada quando:
1. utiliza tokens compartilhados;
2. comunica estado verdadeiro;
3. não sugere funcionalidades inexistentes;
4. preserva distinção entre módulos;
5. apresenta fontes e permissões quando relevantes;
6. funciona em telas pequenas e com contraste adequado.
