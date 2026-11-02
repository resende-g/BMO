# d-BMO — Especificação visual do personagem

**Versão:** 1.0 (especificação conceitual)  
**Status:** geometria de referência; CAD e dimensões físicas pendentes

## 1. Conceito

O d-BMO é um pequeno computador antropomórfico. Sua arquitetura corporal deve preservar a leitura de dispositivo eletrônico pessoal, e não se transformar em robô humanoide convencional.

## 2. Silhueta e componentes

Características obrigatórias:
- corpo retangular vertical;
- cantos arredondados;
- tela frontal integrada à parte superior;
- rosto digital exibido na tela;
- controles físicos abaixo ou ao redor da tela;
- dois braços laterais simples;
- duas pernas curtas e pés arredondados.

A silhueta deve permanecer reconhecível em vista frontal e em tamanho reduzido.

## 3. Consistência entre vistas

As vistas frontal, traseira, lateral e em perspectiva devem representar o mesmo objeto. Devem manter:
- mesma proporção geral do corpo;
- mesma posição e dimensão relativa da tela;
- mesma disposição de controles;
- mesmos pontos de conexão dos braços e pernas;
- continuidade de superfícies, espessuras e encaixes.

Não inventar detalhes traseiros ou mecânicos que não tenham sido definidos. Marcar elementos desconhecidos como pendentes, em vez de completar por suposição.

## 4. Tela e expressões

O rosto é digital e deve usar pixels vermelhos sobre fundo escuro. A biblioteca prevista contém dez estados:
1. `IDLE` — ocioso;
2. `THINKING` — pensando;
3. `SCANNING` — escaneando;
4. `ANALYZING` — analisando;
5. `SUCCESS` — operação concluída;
6. `ALERT` — alerta;
7. `ERROR` — erro;
8. `PROTECTING` — proteção ativa;
9. `CURIOUS` — curioso;
10. `OFFLINE` — desconectado.

As expressões devem compartilhar grade, escala de pixels, área segura e alinhamento. A expressão não deve mudar a geometria física da tela.

## 5. Materiais e acabamento

Direção material:
- prata metálica e prata industrial no corpo;
- grafite e preto em tela, junções e detalhes;
- vermelho nos elementos digitais e acentos;
- off-white apenas quando necessário para legibilidade.

O acabamento pode combinar superfícies metálicas e polímeros escuros. A especificação final depende do protótipo físico e dos materiais escolhidos.

## 6. Requisitos para modelagem 3D e impressão

Esta especificação não é um modelo CAD nem autoriza alterar dimensões de um protótipo existente.

Antes de gerar ou modificar STL/STEP, obter e preservar:
- dimensões externas medidas;
- espessuras mínimas compatíveis com o processo;
- furos, encaixes e tolerâncias;
- posições de parafusos e conectores;
- volumes reservados para placa, tela, bateria e cabos;
- orientação de impressão e limitações de suporte.

Não modificar geometria funcional, dimensões, furos, encaixes, espessuras ou conexões sem instrução explícita e validação do mantenedor.

Renders e imagens geradas servem como referência estética, não como prova dimensional. Validar malha, manifold, escala e tolerâncias no CAD antes de fabricar.

## 7. Entregáveis técnicos futuros

- folha ortográfica com vistas frontal, traseira, lateral e superior;
- desenho cotado;
- modelo CAD paramétrico;
- exportações STEP e STL;
- mapa de materiais e acabamentos;
- biblioteca de expressões em vetor ou pixel art;
- registro de versão e compatibilidade com hardware.

## 8. Pendências

A geometria detalhada, dimensões, disposição exata dos controles, componentes internos e interfaces mecânicas ainda precisam ser confirmadas a partir do protótipo e de seus arquivos-fonte. Não inferir essas informações a partir de uma prancha de identidade.
