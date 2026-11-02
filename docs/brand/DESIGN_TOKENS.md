# d-BMO — Design tokens

**Versão:** 1.0 (tokens iniciais)  
**Status:** paleta definida; tipografia e medidas ainda em validação

## 1. Cores

| Token | Nome | HEX | Uso |
|---|---|---|---|
| `color.silver.metallic` | Metallic Silver | `#D5D7D9` | superfícies metálicas e elementos principais |
| `color.silver.industrial` | Industrial Silver | `#AEB3B8` | elementos secundários e variações metálicas |
| `color.red.signal` | Signal Red | `#D92332` | destaque, estados ativos e rosto digital |
| `color.red.dark` | Dark Red | `#8F1722` | sombras e detalhes de ênfase |
| `color.black` | Black | `#090A0C` | fundo principal |
| `color.graphite` | Graphite | `#24272B` | superfícies, painéis e estruturas |
| `color.offwhite` | Off-White | `#F2F0EB` | texto e elementos claros |

### Regras

- Vermelho é cor de sinalização; usar com parcimônia.
- Não usar cores não previstas como cores centrais da marca.
- Não depender apenas da cor para comunicar estado; combinar cor com texto, ícone ou forma.
- Validar contraste de texto e controles para cada combinação real antes de publicar componentes.

## 2. Tipografia

A família tipográfica definitiva ainda não foi selecionada. Não inventar nomes de fontes nem declarar uma família como oficial sem verificar disponibilidade, licença e renderização.

Requisitos:
- títulos: geometria tecnológica/industrial, sem sacrificar legibilidade;
- corpo: sans-serif altamente legível;
- dados técnicos e terminal: fonte monoespaçada;
- pesos e espaçamentos consistentes;
- suporte a português, acentos e caracteres técnicos.

Registrar futuramente família primária, fallback, licença, pesos e arquivos utilizados.

## 3. Escala inicial de espaçamento

A escala abaixo é uma convenção inicial para implementação, não uma medida extraída da prancha:

| Token | Valor |
|---|---:|
| `space.1` | 4 px |
| `space.2` | 8 px |
| `space.3` | 12 px |
| `space.4` | 16 px |
| `space.6` | 24 px |
| `space.8` | 32 px |
| `space.12` | 48 px |

## 4. Forma e profundidade

Direção visual:
- cantos arredondados moderados;
- contornos discretos;
- superfícies grafite;
- prata para hierarquia e materialidade;
- sombras e brilhos sutis, sem efeito luminoso excessivo.

Raios, espessuras de borda e sombras devem ser consolidados durante a implementação dos componentes, com tokens explícitos e testes em diferentes densidades de tela.

## 5. Movimento e estados

Movimento deve ser funcional e breve. Evitar animações contínuas que distraiam ou sugiram atividade inexistente.

Estados previstos para o personagem e a interface:
- idle;
- thinking;
- scanning;
- analyzing;
- success;
- alert;
- error;
- protecting;
- curious;
- offline.

A interface deve sempre oferecer alternativa textual ou visual para usuários que não percebam animações.

## 6. Convenção de implementação

Quando houver frontend, manter tokens em uma fonte única de verdade (por exemplo, CSS custom properties ou configuração equivalente). Evitar repetir valores de cor em componentes isolados.

Os tokens deste documento são a referência inicial; qualquer alteração deve atualizar este arquivo e registrar a motivação no changelog.
