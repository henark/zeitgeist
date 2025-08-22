# TIP-00XX: Estratégia híbrida Jules + Gemini Pro para Talos

## Proposta resumida (TL;DR)

Esta proposta recomenda uma estratégia híbrida para o desenvolvimento de agentes de codificação no framework Talos. A sugestão é usar:
*   **Google Jules:** Para tarefas de automação de fluxo de trabalho de codificação que podem ser executadas de forma assíncrona (ex: refatorações, correções de bugs). Seu modelo de assinatura oferece previsibilidade de custos.
*   **Gemini Pro API:** Para o desenvolvimento de agentes personalizados e experimentação que exigem controle granular sobre a lógica de raciocínio e o custo, utilizando o parâmetro `thinkingBudget` para gerenciar o consumo de tokens.

Essa abordagem permite que os desenvolvedores aproveitem a automação e a previsibilidade do Jules para tarefas de rotina, enquanto mantêm a flexibilidade da API do Gemini Pro para criação de funcionalidades customizadas.

## Motivação

O desenvolvimento de software está evoluindo de copilotos reativos para agentes autônomos capazes de realizar tarefas complexas de engenharia de software. Frameworks como o **Talos ("Task, Intent & Plan")** estão no centro dessa transformação, permitindo a criação de agentes de codificação.

No entanto, a adoção de IA para tarefas de desenvolvimento levanta preocupações sobre a previsibilidade de custos, especialmente com modelos de pagamento por uso (pay-as-you-go). Esta proposta visa abordar essa preocupação, fornecendo uma estratégia clara para a escolha da ferramenta de IA certa para a tarefa certa no contexto do Talos.

## Detalhamento técnico

### 1. Google Jules: A Abordagem de Produto para Codificação Autônoma

O Google Jules é um agente de codificação assíncrono, uma solução completa para o desenvolvimento orientado por agentes. Ele opera de forma autônoma, interpretando issues do GitHub, formulando planos, editando código em múltiplos arquivos e submetendo pull requests.

**Quando usar:** Ideal para tarefas assíncronas e bem definidas, onde a previsibilidade de custo é uma prioridade.

**Arquitetura e Fluxo de Trabalho:**
*   **Multi-agente:** Inclui agentes de Planejamento, Execução, Crítica e Teste.
*   **Ambiente Seguro:** Clona o repositório em uma VM segura na nuvem.
*   **Assíncrono:** O desenvolvedor inicia uma tarefa e é notificado quando concluída ("fire-and-forget").

**Controle de Custos:**
Jules utiliza um modelo de assinatura, o que oferece alta previsibilidade de custos.

| Plano | Custo (Jun-2025) | Limites de Uso |
| :--- | :--- | :--- |
| Acesso Introdutório | Gratuito | Nível básico |
| Google AI Pro | $19.99/mês | 5x mais alto |
| Google AI Ultra | (Não especificado) | Nível mais alto |
*Nota: Os preços e os limites de uso podem mudar.*

**Limitações e Considerações:**
*   **Contexto:** A documentação pública menciona um limite de contexto efetivo de 200k tokens. Relatos sobre limites maiores (e.g., 768k tokens) não são confirmados.
*   **Controle:** Por ser uma solução de produto, oferece menos controle granular sobre o processo de raciocínio em comparação com a API.

### 2. Gemini Pro API: Poder Bruto e Controle Granular

O Gemini 2.5 Pro é um modelo de IA projetado para codificação e tarefas de alta complexidade. Usar a API do Gemini Pro significa ter acesso direto ao poder do modelo, mas também a responsabilidade de gerenciar seu uso e custo.

**Quando usar:** Ideal para construir agentes personalizados, experimentar com lógicas de raciocínio e quando o controle granular sobre o custo e o processo é necessário.

**Controle de Custos com `thinkingBudget`:**
O principal mecanismo para controlar os custos da API Gemini Pro é o parâmetro `thinkingBudget`, que limita o número de tokens de "raciocínio" que o modelo pode usar. Este parâmetro ainda está em preview.

*   `thinkingBudget = 0`: Desativa o raciocínio. Mais rápido, menor custo, menor qualidade.
*   `thinkingBudget = 1024` (ou outro valor): Aloca um orçamento fixo de tokens, garantindo um custo máximo.
*   `thinkingBudget = -1`: Permite raciocínio dinâmico, onde o modelo ajusta o orçamento com base na complexidade da tarefa.

Para usar o `thinkingBudget` em uma chamada de API, a requisição seria semelhante a:

```json
{
  "contents": [...],
  "safetySettings": [...],
  "generationConfig": {
    "temperature": 0.9,
    ...
  },
  "thinkingBudget": 1024
}
```

### 3. Tabela Comparativa

| Dimensão | Google Jules | Gemini Pro API |
| :--- | :--- | :--- |
| Modelo de Negócio | Assinatura (Custo Fixo) | Pay-per-use (Custo Variável) |
| Previsibilidade de Custo | Alta | Baixa (Gerenciável com `thinkingBudget`) |
| Nível de Abstração | Solução de Produto (Alto Nível) | API de Modelo (Baixo Nível) |
| Controle do Desenvolvedor | Limitado (Guiado) | Total (Granular) |
| Fluxo de Trabalho | Assíncrono ("Fire-and-forget") | Síncrono (Requer orquestração) |
| Privacidade de Dados | Repositórios privados não são usados para treinamento. | O Free Tier pode ser usado para treinamento. O Paid Tier não. |

## Guia Rápido de Integração com Talos

Para tornar esta estratégia acionável, aqui estão exemplos de como integrar Jules e Gemini em um projeto Talos.

**1. Crie um projeto-sandbox Talos:**
```bash
npx create-talos my-agent
```

**2. Integre Jules para refatoração assíncrona:**
Defina uma tarefa em um arquivo YAML de configuração do Talos.

```yaml
# my-agent/tasks.yaml
steps:
  - id: refactor_legacy_code
    uses: talos-jules/refactor@v0
    with:
      repoUrl: https://github.com/my-org/my-repo
      issue: 123
      token: ${{ secrets.JULES_TOKEN }}
```

**3. Integre Gemini Pro para lógica customizada:**
Use a biblioteca do Gemini dentro do código do seu agente Talos.

```typescript
// my-agent/src/custom-logic.ts
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);

async function runCustomLogic(prompt: string) {
  const model = genAI.getGenerativeModel({
    model: "gemini-2.5-pro",
    // @ts-ignore - a propriedade 'thinkingBudget' está em preview
    thinkingBudget: 1024,
  });

  const result = await model.generateContent(prompt);
  return result.response.text();
}
```

## Impacto esperado no ecossistema Talos

A adoção desta estratégia híbrida trará os seguintes benefícios para os desenvolvedores do Talos:
*   **Flexibilidade:** Permite escolher a ferramenta certa para cada caso de uso.
*   **Controle de Custos:** Oferece um caminho para usar IA de forma sustentável, mitigando o risco de custos inesperados.
*   **Aceleração do Desenvolvimento:** Permite que os desenvolvedores se concentrem em tarefas de alto nível, delegando a implementação a agentes de IA.

## Riscos e mitigação

*   **Complexidade de Integração:** Gerenciar duas ferramentas de IA pode aumentar a complexidade.
    *   **Mitigação:** Fornecer "starters" e documentação clara no ecossistema Talos.
*   **Dependência de Fornecedor (Vendor Lock-in):** A dependência de APIs da Google pode ser um risco.
    *   **Mitigação:** O design do Talos deve ser modular, permitindo a substituição dos "motores" de IA.
*   **Licenciamento:** O uso de Jules (SaaS) em um projeto Apache-2.0 (Talos) precisa de clareza. A integração via API/CLI é geralmente permissível, mas a redistribuição pode ser restrita.
    *   **Mitigação:** A documentação deve ser clara sobre as implicações de licenciamento.

## Alternativas consideradas

*   **Usar apenas Jules:** Simples, mas limita a flexibilidade e o controle.
*   **Usar apenas Gemini Pro:** Oferece controle total, mas pode ser mais complexo de gerenciar e os custos podem ser menos previsíveis.

## Referências

*¹ (URL da fonte sobre a falta de info do Talos)*
*² (URL da fonte sobre "desenvolvimento orientado a agentes")*
*³ (URL da fonte sobre a arquitetura do Jules)*
*⁵ (URL da fonte sobre os agentes do Jules)*
*⁶ (URL da fonte sobre os preços e planos do Jules)*
*⁸ (URL da fonte sobre o preço do plano Pro)*
*¹² (URL da fonte sobre o Gemini 2.5 Pro para codificação)*
*¹³ (URL da fonte sobre as capacidades do Gemini)*
*¹⁴ (URL da fonte sobre o preço do Gemini Pro API)*
*¹⁵ (URL da fonte sobre o `thinkingBudget`)*

*Nota: As URLs das referências precisam ser adicionadas.*
