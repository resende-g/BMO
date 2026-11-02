# d-BMO — Diretrizes de identidade visual

**Versão:** 1.0 (documentação inicial)  
**Projeto:** Beemon (BMO)  
**Status:** direção visual de referência; ativos finais pendentes

## 1. Propósito

O d-BMO (Dark BMO) é a identidade visual, o personagem e a camada de apresentação do Beemon. Sua função é tornar o sistema reconhecível e comunicar uma inteligência pessoal, local e orientada à privacidade.

Assinatura verbal:

> **d-BMO — DARK BMO**  
> LOCAL INTELLIGENCE. PRIVATE BY DESIGN.

O slogan expressa a intenção arquitetural do projeto. Não constitui, por si só, garantia de que toda operação já esteja implementada localmente.

## 2. Posicionamento visual

A linguagem combina:
- computador pessoal retrô e robótica antropomórfica;
- estética industrial minimalista;
- referências retrofuturistas e cyberpunk controladas;
- superfícies metálicas, grafite e contraste vermelho;
- interfaces funcionais, legíveis e discretas.

Evitar aparência militarizada, agressiva, excessivamente ornamental ou de robô humanoide genérico.

## 3. Personalidade

O personagem deve comunicar uma presença:
- observadora e analítica;
- curiosa e confiável;
- reservada, sem ser fria;
- amigável, com humor sutil;
- não agressiva nem ostensivamente antropomórfica.

A expressão deve apoiar o estado da interação, sem sugerir emoções humanas complexas ou autonomia que o sistema não possua.

## 4. Elementos centrais

### 4.1 Personagem

Computador antropomórfico pequeno, retangular e vertical, com cantos arredondados, tela frontal integrada na parte superior, controles físicos abaixo ou ao redor da tela, braços laterais simples e pernas curtas. A especificação detalhada está em [CHARACTER_SPECIFICATION.md](CHARACTER_SPECIFICATION.md).

### 4.2 Símbolo

A direção aprovada é uma letra minúscula **d** estilizada, integrada a um rosto digital sorridente construído com pixels vermelhos. A letra e o rosto devem constituir uma única marca, não dois elementos independentes justapostos.

O desenho vetorial definitivo ainda precisa ser produzido e revisado. Não inferir proporções exatas a partir de uma imagem rasterizada.

### 4.3 Logotipo

Grafia principal: `d-BMO`.  
Identificação complementar: `DARK BMO`.

Não distorcer caracteres, inventar variações ortográficas ou alterar o slogan. Versões horizontal, vertical, monocromática e reduzida devem derivar do mesmo desenho-mestre.

## 5. Paleta

A paleta normativa está em [DESIGN_TOKENS.md](DESIGN_TOKENS.md). Cores principais: prata metálica, prata industrial, vermelho, vermelho escuro, preto, grafite e off-white.

Não introduzir ciano, turquesa, dourado, amarelo, roxo ou azul como cores da marca sem revisão explícita desta diretriz.

## 6. Composição e materiais

- Priorizar contraste e legibilidade.
- Usar vermelho como sinalização e destaque, não como preenchimento indiscriminado.
- A prata deve sugerir material metálico, mas aplicações digitais precisam preservar contraste textual.
- Texturas, brilho e efeitos 3D são recursos secundários; não podem comprometer reconhecimento do símbolo.
- Em tamanhos pequenos, simplificar detalhes e preservar a silhueta.

## 7. Aplicações

A identidade pode ser aplicada a:
- interface conversacional;
- terminal e dashboard;
- ícone de aplicativo e favicon;
- documentação e materiais do projeto;
- personagem físico e futuras peças impressas em 3D.

As regras de interface estão em [UI_GUIDELINES.md](UI_GUIDELINES.md). Imagens conceituais não substituem ativos vetoriais, arquivos de interface ou CAD.

## 8. Governança dos ativos

Ativos oficiais devem ser versionados em `docs/brand/assets/` ou diretório equivalente, com:
- nome e versão;
- formato e dimensões;
- autoria e origem;
- licença ou autorização de uso;
- indicação de arquivo-fonte e exportações;
- status: rascunho, aprovado ou obsoleto.

Não publicar imagens ou materiais de terceiros sem verificar direitos de uso. Não tratar saídas de IA como vetores editáveis ou modelos CAD.

## 9. Critérios de aprovação

Uma aplicação é consistente quando:
1. preserva a construção reconhecível do símbolo;
2. respeita a paleta;
3. mantém a geometria do personagem;
4. usa tipografia legível e licenciada;
5. não contradiz o posicionamento local-first e privado;
6. diferencia claramente conceito visual de funcionalidade implementada.

## 10. Pendências

- vetorizar e aprovar o símbolo-mestre;
- selecionar famílias tipográficas reais e verificar licenças;
- receber e versionar a prancha de referência aprovada;
- produzir folha de personagem com vistas consistentes;
- definir ativos oficiais de expressão;
- validar contraste e escalabilidade em interface;
- desenvolver modelo CAD/3D independente, com dimensões verificadas.
