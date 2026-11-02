# Sistema de Skills do BMO

## 1. Objetivo

Skills são unidades modulares de capacidade que descrevem uma tarefa, seus contratos, ferramentas e permissões. O sistema deve permitir adicionar funcionalidades sem alterar continuamente o núcleo do BMO Brain.

**Estado:** Planejado. Nenhuma das skills abaixo está implementada neste repositório.

## 2. Princípios

- Uma skill não é um agente com autoridade irrestrita.
- O Brain controla o ciclo de execução.
- O Policy Gate decide permissões fora do modelo.
- Argumentos e saídas devem obedecer a esquemas.
- Conteúdo externo e saídas de ferramentas são dados não confiáveis.
- A skill não pode conceder permissões a si própria.
- Ações sensíveis exigem confirmação humana.
- Skills de segurança operam apenas em ativos próprios ou autorizados, com escopo explícito.

## 3. Contrato mínimo

Cada skill deve declarar:

| Campo | Descrição |
|---|---|
| `id` | identificador estável |
| `version` | versão da especificação/implementação |
| `purpose` | objetivo |
| `scope` | limites e ativos permitidos |
| `inputs` | parâmetros tipados e validações |
| `outputs` | estrutura de resultado |
| `tools` | ferramentas necessárias |
| `permissions` | permissões solicitadas |
| `risk_level` | classificação de risco |
| `confirmation` | quando exige autorização |
| `constraints` | proibições e limites |
| `validation` | testes e critérios de sucesso |

A implementação futura deve validar manifesto antes de registrar a skill. Segredos não devem ser definidos no manifesto.

## 4. Fluxo de execução

1. Brain recebe a intenção.
2. Skill Registry apresenta skills compatíveis.
3. Brain valida escopo, entradas e pré-condições.
4. Policy Gate avalia permissões.
5. Se necessário, solicita autorização explícita.
6. Executor isolado executa somente as ferramentas autorizadas.
7. Saída é validada pelo esquema e limites.
8. Auditoria registra decisão, ferramenta, duração e resultado.
9. Brain apresenta resultado e limitações.

## 5. Catálogo inicial

### `system-audit`

- **Objetivo:** inventariar e diagnosticar o sistema local.
- **Entradas:** alvo local, categorias de inventário, profundidade.
- **Saídas:** inventário estruturado, avisos e evidências.
- **Ferramentas:** leitura de informações do sistema e comandos de diagnóstico allowlisted.
- **Permissões:** leitura local; sem elevação por padrão.
- **Restrições:** não alterar configurações, instalar pacotes ou coletar segredos.
- **Validação:** inventário consistente, comandos dentro da allowlist e ausência de alterações no sistema.

### `network-recon`

- **Objetivo:** mapear ativos e serviços em rede com autorização.
- **Entradas:** CIDR/hosts explicitamente autorizados, janela e intensidade.
- **Saídas:** hosts e serviços observados, timestamps e escopo executado.
- **Ferramentas:** utilitários de descoberta e sondagem aprovados.
- **Permissões:** rede restrita ao escopo autorizado; confirmação explícita antes de iniciar.
- **Restrições:** proibido ampliar escopo automaticamente, explorar vulnerabilidades, evadir controles ou executar ações disruptivas.
- **Validação:** bloquear alvos fora do escopo; registrar autorização e parâmetros; limitar taxa e duração.

### `security-assessment`

- **Objetivo:** realizar avaliação de segurança controlada em ativos próprios ou autorizados.
- **Entradas:** ativo, evidência de autorização, escopo, exclusões e janela.
- **Saídas:** achados, severidade justificada, evidências minimizadas e recomendações.
- **Ferramentas:** scanners e verificações não destrutivas aprovados.
- **Permissões:** leitura/sondagem restrita; testes intrusivos exigem autorização específica e análise separada.
- **Restrições:** não explorar além do escopo, persistir acesso, exfiltrar dados ou interromper serviços.
- **Validação:** cada achado ligado a evidência; falsos positivos identificados; escopo auditável.

### `code-review`

- **Objetivo:** analisar código em busca de defeitos, riscos e problemas de manutenção.
- **Entradas:** repositório/diretório autorizado, linguagem, foco e baseline.
- **Saídas:** achados priorizados, arquivo/linha, impacto, confiança e correção sugerida.
- **Ferramentas:** leitura de arquivos, testes e analisadores estáticos.
- **Permissões:** leitura por padrão; nenhuma alteração automática.
- **Restrições:** não enviar código privado a serviços externos; não executar scripts desconhecidos sem sandbox.
- **Validação:** achados reproduzíveis, referência precisa e distinção entre certeza e hipótese.

### `report-generator`

- **Objetivo:** converter evidências e achados em relatório técnico.
- **Entradas:** dados estruturados, público-alvo, formato e classificação.
- **Saídas:** relatório com escopo, método, evidências, limitações e recomendações.
- **Ferramentas:** templates e geradores de documentos locais.
- **Permissões:** leitura dos resultados autorizados e escrita apenas no diretório de saída aprovado.
- **Restrições:** não inventar evidências, métricas ou conclusões; não incluir segredos.
- **Validação:** rastreabilidade entre afirmações e evidências, revisão de dados sensíveis e consistência do formato.

## 6. Matriz inicial de permissões

| Skill | Leitura local | Rede | Escrita em arquivos | Alteração de sistema |
|---|---:|---:|---:|---:|
| system-audit | Sim, escopo limitado | Não por padrão | Não | Não |
| network-recon | Configuração necessária | Sim, escopo autorizado | Relatório aprovado | Não |
| security-assessment | Escopo autorizado | Sim, escopo autorizado | Relatório aprovado | Não por padrão |
| code-review | Repositório autorizado | Não por padrão | Não | Não |
| report-generator | Evidências autorizadas | Não | Diretório aprovado | Não |

A tabela é uma política-alvo. A implementação deve negar permissões não declaradas e não usar a matriz como substituto de autorização contextual.

## 7. Manifesto ilustrativo

```yaml
id: code-review
version: 0.1.0
purpose: "Analisar código local autorizado"
scope:
  filesystem: "explicit_paths_only"
inputs:
  - name: repository_path
    type: string
    required: true
outputs:
  format: structured_findings
tools:
  - source_reader
permissions:
  filesystem: read
  network: deny
risk_level: low
confirmation: false
constraints:
  - "Não alterar arquivos"
  - "Não enviar código para serviços externos"
validation:
  - "Cada achado referencia arquivo e linha"
  - "Separar evidência de hipótese"
```

Este exemplo é especificação ilustrativa, não um manifesto já aceito por um runtime.