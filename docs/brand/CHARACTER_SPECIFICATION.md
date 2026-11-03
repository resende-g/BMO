# d-BMO — Especificação visual do personagem

**Versão:** 2.0 (especificação conceitual)  
**Status:** direção visual escolhida em 2026-11-02 (variação 1); CAD e dimensões físicas pendentes

## 1. Conceito

O d-BMO é um videogame portátil retrô de emulação que também funciona como assistente pessoal. O rosto aparece na tela do próprio aparelho. A leitura principal é de dispositivo eletrônico real, não de robô humanoide nem de personagem de desenho animado.

A referência de gênero é a categoria de portáteis verticais de emulação, como o R36S. A forma vertical é comum nessa categoria e não pertence a um produto específico. O d-BMO não reproduz logotipo, texto de marca nem detalhes exclusivos de nenhum console existente.

Referência visual: [assets/dbmo-referencia-conceitual-v1.jpeg](assets/dbmo-referencia-conceitual-v1.jpeg) (ver §9).

O aparelho físico que implementa esta especificação é desenvolvido em [resende-g/d-BMO-body](https://github.com/resende-g/d-BMO-body) (hardware, firmware do rosto e carcaça).

## 2. Silhueta e componentes

Características obrigatórias:
- corpo vertical com cantos arredondados e espessura perceptível;
- tela 4:3 grande na metade superior, com moldura preta generosa;
- rosto digital exibido na tela;
- cruz direcional à esquerda e quatro botões de ação em losango à direita, abaixo da tela;
- **dois controles analógicos** na parte inferior, um em cada lado;
- botões pequenos de select e start no centro inferior;
- grade de alto-falante entre os analógicos;
- gatilhos de ombro no topo;
- **sem membros**: em repouso, o aparelho fica num suporte inclinado grafite.

A silhueta deve permanecer reconhecível em vista frontal e em tamanho reduzido.

### 2.1 Elementos de distinção

Os elementos abaixo diferenciam o d-BMO de personagens existentes em forma de videogame e não devem ser removidos:
- os dois analógicos e os gatilhos de ombro;
- a paleta prata, grafite e vermelho (§5);
- botões monocromáticos em grafite ou prata;
- o rosto em blocos de pixel vermelho, sem traços finos;
- a ausência de braços e pernas.

### 2.2 Elementos vedados

- corpo verde-água ou em tons de ciano;
- braços e pernas finos;
- botões coloridos de formas geométricas diferentes;
- fenda de cartucho na face frontal;
- rosto feito de pontos e traços finos sobre tela clara;
- logotipo, texto ou detalhe de marca de console real.

Antes de aprovar uma nova vista ou ilustração, mostrar a imagem a quem conhece personagens de videogame e de animação, sem dar contexto. Se a pessoa associar a imagem a um personagem existente, revisar.

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

Na referência v1, o ponto vermelho entre a cruz direcional e os botões de ação ainda não tem função definida. Decidir se ele será LED de estado (recomendado: pequeno e embutido) ou se será removido.

## 9. Referência visual

| Campo | Registro |
|---|---|
| Arquivo | `assets/dbmo-referencia-conceitual-v1.jpeg` |
| Origem | imagem gerada no Gemini em 2026-11-02 e recortada da variação 1 de uma folha com 4 variações |
| Natureza | referência conceitual; não é arte final, vetor nem desenho cotado |
| Autoria | gerada por IA a partir de prompt do mantenedor; a arte final deve ser redesenhada ou vetorizada por autor humano |

**Render do corpo, v1** (`assets/dbmo-body-render-v1.jpg`): gerado no Gemini em 2026-11-02 a partir da variação 1, recortado na vista frontal. Os símbolos dos botões de ação foram apagados na edição, para cumprir a §2.2. Os olhos ainda aparecem em formato de "+": o desenho de referência do rosto é o do firmware (`d-BMO-body/firmware/rosto/`), em blocos 2 × 3. Mesma natureza e autoria da referência acima.

A licença Apache-2.0 do repositório não cobre esta imagem nem o personagem: todos os direitos reservados (ver `README.md`).
