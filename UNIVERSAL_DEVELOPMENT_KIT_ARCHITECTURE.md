# Arquitetura do Kit de Desenvolvimento Universal (UDK)

## 1. Visão Geral

O Kit de Desenvolvimento Universal (UDK) é um sistema projetado para fornecer um ambiente de desenvolvimento aumentado por IA que seja agnóstico de linguagem e framework. Ele atua como uma ponte entre um agente de IA (como eu) e qualquer ambiente de desenvolvimento local, fornecendo contexto, ferramentas e diretrizes para permitir a assistência ao desenvolvimento de alta qualidade.

Este sistema é a síntese e generalização dos conceitos explorados em protótipos anteriores como o "TimeKeeper Boost" e estudos de caso como o `laravel/boost`.

## 2. Componentes Principais

A arquitetura do UDK é modular e consiste em cinco componentes principais:

### 2.1. UDK Server (Servidor UDK)

- **Função**: O núcleo do sistema. É um processo de longa duração, agnóstico de linguagem, que atua como um barramento de mensagens e orquestrador central.
- **Responsabilidades**:
    - Gerenciar o ciclo de vida dos adaptadores de ambiente.
    - Roteamento de comandos do agente de IA para o adaptador apropriado.
    - Manter o estado da sessão de desenvolvimento.
    - Carregar e fornecer diretrizes de IA.
    - Servir como o único ponto de entrada para o agente de IA.

### 2.2. Adapters (Adaptadores de Ambiente)

- **Função**: Componentes plugáveis que atuam como uma camada de tradução entre o UDK Server e um ambiente de desenvolvimento específico (por exemplo, Python/Poetry, Node.js/NPM, PHP/Composer).
- **Responsabilidades**:
    - Detectar o tipo de projeto (ex: `pyproject.toml` para Python, `package.json` for Node.js).
    - Expor as ferramentas específicas do ambiente para o UDK Server.
    - Fornecer contexto específico do ambiente (ex: versão da linguagem, dependências, frameworks).
    - Executar os comandos das ferramentas no ambiente correto (ex: dentro de um ambiente virtual Python).

### 2.3. Tools (Ferramentas)

- **Função**: Ações atômicas e discretas que podem ser executadas pelo agente de IA. As ferramentas são expostas pelos adaptadores.
- **Exemplos**:
    - **filesystem**: `read`, `write`, `list`
    - **code**: `lint`, `test`, `get_ast`
    - **runtime**: `execute_command`, `install_dependencies`
    - **project_management**: `read_issues` (uma possível integração com o OpenProject)

### 2.4. Guidelines (Diretrizes de IA)

- **Função**: Um sistema para fornecer contexto e instruções em linguagem natural para o agente de IA.
- **Responsabilidades**:
    - Carregar diretrizes de uma fonte configurável (ex: um diretório `.ai/guidelines/`).
    - Combinar diretrizes de diferentes níveis (core, framework, projeto).
    - Fornecer o conjunto completo de diretrizes para o agente no início de uma sessão.

### 2.5. Context Manager (Gerenciador de Contexto)

- **Função**: Um componente dentro do UDK Server que rastreia o estado dinâmico do ambiente de desenvolvimento.
- **Responsabilidades**:
    - Manter uma lista de arquivos abertos ou recentemente modificados.
    - Rastrear o histórico de comandos e resultados.
    - Armazenar o último erro ou saída de teste.
    - Fornecer este contexto dinâmico para o agente de IA para melhorar a relevância de suas ações.

---

## 3. Workflow de Interação

O fluxo de trabalho de uma sessão de desenvolvimento com o UDK é o seguinte:

1.  **Inicialização**: O UDK Server é iniciado no diretório raiz de um projeto.
2.  **Ativação do Adaptador**: O servidor detecta o tipo de projeto (ex: Python) e ativa o `PythonAdapter` correspondente.
3.  **Descoberta de Ferramentas**: O `PythonAdapter` descobre e registra as ferramentas disponíveis para este ambiente (ex: `filesystem`, `pytest`, `pip`).
4.  **Conexão do Agente**: Um agente de IA se conecta ao UDK Server (por exemplo, através de stdin/stdout, como no protótipo TimeKeeper Boost).
5.  **Sincronização de Contexto**: O servidor envia um pacote de contexto inicial para o agente, contendo:
    - A lista de ferramentas e suas ações disponíveis.
    - As diretrizes de IA combinadas.
    - O estado inicial do projeto (ex: estrutura de diretórios, arquivos abertos).
6.  **Loop de Comando**: O agente entra em um loop de "pensar-agir":
    - O agente envia um comando JSON para o servidor (ex: `{"tool": "filesystem", "action": "read", "args": {"path": "app/main.py"}}`).
    - O servidor roteia o comando para o adaptador, que executa a ação da ferramenta.
    - O resultado (ou erro) é retornado ao agente como uma resposta JSON.
    - O Gerenciador de Contexto atualiza o estado do ambiente.
7.  **Atualização de Contexto**: O servidor pode enviar proativamente atualizações de contexto para o agente se o estado do ambiente mudar (ex: um arquivo foi modificado).

---

## 4. Protocolo de Comunicação (JSON)

A comunicação entre o Agente de IA e o UDK Server é feita através de mensagens JSON simples.

### Mensagem do Agente para o Servidor (Comando)

```json
{
  "tool": "tool_name",
  "action": "action_name",
  "args": {
    "arg1_name": "value1",
    "arg2_name": 123
  }
}
```

### Mensagem do Servidor para o Agente (Resposta)

**Sucesso:**
```json
{
  "status": "success",
  "result": {
    "data_type": "string",
    "value": "Conteúdo do arquivo..."
  },
  "context_update": {
    "last_modified_file": "app/main.py"
  }
}
```

**Erro:**
```json
{
  "status": "error",
  "message": "Descrição detalhada do erro.",
  "error_type": "FileNotFoundError"
}
```
