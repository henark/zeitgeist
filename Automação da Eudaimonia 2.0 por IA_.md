

# **Automatizando a Pluralidade: Uma Análise de Viabilidade e Roteiro de Implementação para a Eudaimonia 2.0 Usando Equipes de Agentes de IA**

## **Introdução**

### **Propósito e Escopo**

Este relatório fornece uma análise exaustiva da medida em que o desenvolvimento da rede social "Eudaimonia 2.0", conforme conceituado no projeto Plurality-Informed 1, pode ser automatizado usando sistemas de agentes de Inteligência Artificial (IA) de última geração. Ele oferece tanto uma avaliação estratégica de viabilidade quanto um roteiro tático e passo a passo para a prototipagem. A análise busca responder a duas questões fundamentais: até que ponto os complexos componentes socio-técnicos da Eudaimonia 2.0 podem ser construídos por agentes de IA e qual seria o processo para montar uma equipe de agentes para criar um protótipo funcional.

### **Desafio Central**

O desafio central reside na tradução dos princípios da Pluralidade, que são altamente abstratos e filosoficamente fundamentados (por exemplo, generatividade social, propriedade plural, integridade contextual), em tarefas concretas e executáveis por máquinas para agentes de desenvolvimento de software de IA.1 Isso exige a construção de uma ponte entre a teoria socio-técnica e a prática da engenharia agêntica. A visão da Eudaimonia 2.0 não é apenas construir uma aplicação, mas um ecossistema digital com novas formas de identidade, propriedade e governança, o que ultrapassa os limites das tarefas de desenvolvimento de software convencionais para as quais os agentes de IA atuais são primariamente treinados.2

### **Metodologia**

A análise sintetiza o projeto da Eudaimonia 2.0 1 com uma pesquisa extensiva sobre as capacidades dos agentes de IA 2, as especificações técnicas dos protocolos subjacentes (DIDs, Polis, QF) 12 e as considerações críticas de segurança para código criptográfico e econômico gerado por IA.19 A abordagem avalia cada componente da arquitetura da Eudaimonia 2.0, determinando o potencial de automação, os riscos inerentes e o papel ideal tanto para os agentes de IA quanto para a supervisão humana.

---

## **Parte I: Análise de Viabilidade: Automatizando o Projeto da Pluralidade**

Esta parte avalia sistematicamente o potencial de automação para cada camada da arquitetura da Eudaimonia 2.0, identificando os principais desafios e riscos.

### **Seção 1: Automação da Camada de Protocolo Central: Identidade, Propriedade e Associação**

#### **1.1. Automatizando a Identidade Facetada: Das Especificações de DID ao Código**

**Objetivo:** Implementar um sistema de "Identidade Facetada" com "Recuperação Comunitária", conforme descrito no projeto.1 Isso requer um sistema onde a identidade de um usuário é a soma de seus papéis na comunidade e é recuperável por meio de um quórum dessas comunidades.

**Primitiva Técnica:** A base para isso são os Identificadores Descentralizados (DIDs) e os Documentos DID, conforme a especificação v1.0 do W3C.17 O modelo de dados central inclui as propriedades

id, verificationMethod e service. A "Recuperação Comunitária" é uma forma de recuperação social, conceitualmente semelhante às propostas de Vitalik Buterin 28, mas implementada por meio de uma lógica de contrato inteligente ou protocolo personalizado.

**Potencial de Automação (Moderado):** A análise revela um padrão claro: os agentes de IA se destacam quando recebem uma especificação formal e precisa para traduzir em código, mas falham com solicitações abstratas ou novas.3 A especificação do W3C DID é um exemplo perfeito de tal especificação formal.18

* **Alto Potencial:** Agentes de IA, como GitHub Copilot ou Devin, são eficazes na geração de código boilerplate, clientes de API e estruturas de dados com base em formatos bem definidos como o JSON-LD do DID.19 Um agente poderia ser instruído a criar classes e funções para criar, resolver e atualizar Documentos DID com base na especificação do W3C.27 O valor da automação está em acelerar a implementação de componentes  
  *padronizados*, liberando especialistas humanos para se concentrarem exclusivamente nos elementos novos e de alto risco.  
* **Baixo Potencial:** A lógica criptográfica central para a geração de chaves (por exemplo, Ed25519) e a nova lógica de contrato inteligente para a "Recuperação Comunitária" não podem ser geradas de forma confiável ou segura do zero. Os modelos de IA podem introduzir vulnerabilidades sutis e catastróficas em código criptográfico.20 Uma estratégia de automação bem-sucedida não é pedir a um agente para "construir um sistema DID", mas decompor a tarefa. Um arquiteto humano primeiro define o método DID específico e a lógica de recuperação. Em seguida, um agente de IA pode ser encarregado de gerar o código não crítico circundante: os esquemas JSON, os manipuladores de endpoint de API, os modelos de banco de dados e os testes de unidade para funções não criptográficas. O agente de IA atua como um "programador em par" para as partes tediosas, não como o "arquiteto principal" para as partes sensíveis.19

#### **1.2. O Desafio da Propriedade Plural: Podem os Agentes de IA Arquitetar Coalizões de Dados?**

**Objetivo:** Constituir formalmente cada "Mundo Vivo" como uma "Coalizão de Dados", uma forma de propriedade coletiva gerenciada pelo DAO da comunidade.1

**Primitiva Técnica:** Este é um conceito altamente inovador sem um padrão pronto para uso. Provavelmente envolveria uma combinação de um framework de DAO (por exemplo, Aragon, MolochDAO), direitos de acesso baseados em NFT e um contrato inteligente de governança de dados personalizado que se conecta ao registro de DIDs da comunidade e à sua instância Polis.

**Potencial de Automação (Muito Baixo):** Agentes de IA atuais, como o Devin, são explicitamente conhecidos por terem dificuldades com tarefas de engenharia complexas e de múltiplos passos que exigem raciocínio arquitetônico inovador.2 "Coalizão de Dados" é um conceito sócio-jurídico-técnico, não um padrão de software. A automação do design das regras econômicas e de governança para tal coalizão é uma tarefa para modelagem baseada em agentes e teoria econômica, não para geração de código.32

Aqui, o papel da IA muda de *geração de código* para *simulação de sistema*. Um codificador de IA não pode "construir uma Coalizão de Dados". No entanto, o campo da Modelagem Baseada em Agentes (ABM) usa IA para simular o comportamento de agentes individuais dentro de um sistema econômico complexo para observar resultados emergentes no nível do sistema.32 Isso se encaixa perfeitamente no design de uma Coalizão de Dados. Em vez de pedir a uma IA para escrever o contrato inteligente, um humano pediria a um ABM alimentado por IA para

*simular* as regras propostas. Por exemplo: "Simule uma Coalizão de Dados com 1.000 membros. Modele um cenário onde a coalizão vota (via Polis) para licenciar seus dados. Como o modelo de distribuição de receita (por exemplo, divisão igual versus ponderada por contribuição) afeta o engajamento dos membros e a saúde da coalizão a longo prazo?" O papel principal da IA neste contexto não é automatizar a *implementação*, mas diminuir o risco do *design*. Torna-se uma ferramenta para a ciência social computacional 34 testar a viabilidade socioeconômica do modelo de Propriedade Plural antes que uma única linha de código de contrato inteligente seja escrita por um especialista humano.

#### **1.3. Engenharia da Integridade Contextual: Automatizando Públicos Criptograficamente Delimitados**

**Objetivo:** Re-engenheirar os "Mundos Vivos" como "Públicos Plurais" criptograficamente delimitados com forte integridade contextual, impedindo o vazamento de dados entre comunidades sem consentimento explícito.1

**Primitiva Técnica:** Isso envolve uma combinação de tecnologias que aprimoram a privacidade. O projeto sugere Provas de Verificador Designado (DVPs) ou ledgers privados e permissionados.1 Isso também poderia ser implementado usando modelos de capacidade de objeto (object-capability) 36 e sistemas de gerenciamento de chaves descentralizados (DKMS) 37 para impor o controle de acesso no nível do protocolo.

**Potencial de Automação (Muito Baixo):** Esta é a vanguarda da criptografia aplicada e da arquitetura descentralizada. Os geradores de código de IA são treinados em vastas quantidades de código público 19, mas esses protocolos de privacidade avançados e de nicho têm uma presença muito pequena nesses dados de treinamento. Gerar implementações seguras, corretas e eficientes de provas de conhecimento zero ou controle de acesso baseado em capacidade de objeto está muito além das capacidades atuais de agentes como Devin ou AutoGPT.2 O risco de introduzir falhas de segurança sutis, mas fatais, é extremamente alto.20

A tarefa de automação é, portanto, reformulada. A IA não é a construtora do motor principal; é a construtora de toda a fábrica ao redor do motor. Embora a IA não possa escrever o protocolo criptográfico central, um especialista humano o fará. Uma vez que esse protocolo central exista como uma biblioteca (por exemplo, uma biblioteca Rust ou C++ para DVPs), os agentes de IA podem ser extremamente eficazes na construção do andaime *ao seu redor*. Um arquiteto humano escreve lib\_privacy\_protocol.rs. O Agente\_Arquiteto pode então instruir um Agente\_Codificador a: 1\) Escrever as ligações da Interface de Função Estrangeira (FFI) para tornar a biblioteca Rust disponível em NodeJS ou Python. 2\) Gerar o servidor de API gRPC ou REST que expõe as funções da biblioteca. 3\) Escrever o SDK do lado do cliente para interagir com essa API. 4\) Gerar documentação abrangente e trechos de exemplo de uso. 5\) Criar um conjunto de testes de integração para garantir que a API funcione como esperado. Isso acelera drasticamente o processo de tornar um protocolo altamente especializado e escrito por humanos utilizável pelo resto da pilha de aplicativos, o que é um grande gargalo no desenvolvimento do mundo real.

### **Seção 2: Automação da Camada Econômica e de Governança: Mercados e Deliberação**

#### **2.1. Implementando Moedas Comunitárias: Modelagem Baseada em Agentes vs. Geração de Contratos Inteligentes**

**Objetivo:** Substituir o "Aether" universal por múltiplas "Moedas Comunitárias" não transferíveis para reforçar as economias locais dentro de cada Mundo Vivo.1

**Primitiva Técnica:** Isso exigiria um sistema de contrato inteligente, provavelmente baseado em um padrão de token não transferível (uma variação do ERC-20 ou uma implementação personalizada) para cada comunidade.

**Potencial de Automação (Moderado para Contratos, Alto para Simulação):** O desenvolvimento de um sistema criptoeconômico como as Moedas Comunitárias requer duas habilidades distintas de IA.

* **Geração de Contratos Inteligentes:** Gerar um token padrão semelhante ao ERC-20 é um caminho bem conhecido. Um agente de IA provavelmente poderia gerar uma implementação básica e funcional.19 No entanto, a lógica personalizada para a não transferibilidade e as regras de cunhagem específicas ligadas a "tarefas terapêuticas" introduzem novidade e risco.20  
* **Simulação de Modelo Econômico:** O verdadeiro desafio não é o código, mas o *design econômico*. Este sistema será estável? Criará os incentivos desejados? Este é um caso de uso principal para a Modelagem Baseada em Agentes (ABM) alimentada por IA 32 para simular o fluxo dessas moedas e testar consequências não intencionais (por exemplo, hiperinflação dentro de uma comunidade, falta de liquidez).

Uma abordagem robusta envolve um pipeline estruturado e auditável, da teoria econômica ao código implantado, usando diferentes especializações de IA em cada estágio. Primeiro, um humano define os objetivos de alto nível para a Moeda Comunitária. Em seguida, um Agente\_Economista (aproveitando o ABM) executa milhares de simulações para encontrar os parâmetros ideais para cunhagem e queima. Este agente produz uma especificação formal da mecânica do token. Finalmente, um Agente\_Engenheiro\_de\_Contrato\_Inteligente pega essa especificação e gera uma implementação preliminar, que é então revisada por um Agente\_Auditor\_de\_Segurança e um especialista humano em busca de vulnerabilidades.

#### **2.2. Integrando a Deliberação Aumentada: Automatizando a Implantação e Customização do Polis**

**Objetivo:** Integrar uma ferramenta semelhante ao Polis para a governança da comunidade, para ir além da votação simples para a construção de sentido coletivo.1

**Primitiva Técnica:** Polis é uma plataforma de código aberto.12 A integração requer a auto-hospedagem da pilha de aplicativos (que usa Docker) e, potencialmente, a personalização de sua interface ou a integração de sua saída de dados com a plataforma Eudaimonia.

**Potencial de Automação (Alto):** Esta é uma tarefa altamente estruturada e procedural, ideal para automação por um agente de IA. O repositório do Polis no GitHub fornece arquivos docker-compose e instruções de configuração detalhadas.13 Muitos recursos da Eudaimonia 2.0 dependem da integração de ferramentas de código aberto existentes, e o processo de implantação e manutenção dessas ferramentas é um fardo operacional significativo que os agentes de IA podem gerenciar com excelência.

Pode-se definir um Agente\_DevOps especializado. Suas responsabilidades incluiriam: 1\) Ler o README.md de um projeto de código aberto como o Polis.13 2\) Traduzir os passos de instalação em um script executável (por exemplo, um script Bash ou playbook Ansible). 3\) Automatizar o provisionamento da infraestrutura de nuvem necessária (por exemplo, uma VM e um banco de dados gerenciado). 4\) Executar o script de implantação. 5\) Configurar monitoramento e alertas para o serviço implantado. Agentes também são proficientes em escrever "código de cola" — por exemplo, um script para extrair dados da API de backend do Polis e exibi-los na interface do usuário da Eudaimonia. Isso automatiza uma grande parte do trabalho de engenharia não inovador.

#### **2.3. Construindo Mercados Sociais: Os Riscos e Recompensas de Automatizar o Financiamento Quadrático**

**Objetivo:** Usar o Financiamento Quadrático (QF) para alocar democraticamente o tesouro da comunidade de cada Mundo Vivo.1

**Primitiva Técnica:** QF é uma fórmula matemática específica, M=(∑i=1n​ci​​)2, onde M é o valor correspondido e ci​ é a contribuição do i-ésimo contribuidor.15 Essa fórmula precisa ser implementada em um contrato inteligente. Existem implementações de código aberto, mas podem carecer de auditorias de segurança.15

**Potencial de Automação (Moderado, mas de Alto Risco):** Um agente de IA poderia receber a fórmula QF e ser solicitado a escrever um contrato inteligente para implementá-la. Dada a natureza matemática da tarefa, ele poderia produzir uma implementação funcionalmente correta. No entanto, o QF é notoriamente vulnerável a ataques Sybil e conluio.14 Uma implementação ingênua gerada por uma IA quase certamente careceria dos mecanismos de defesa sofisticados e necessários, como o pareamento pairwise ou a análise de cluster do Gitcoin.24

Uma abordagem mais sofisticada usa múltiplos agentes de IA em uma configuração adversarial para *endurecer* um contrato escrito por humanos. Isso transforma a IA de um gerador de código ingênuo em um sofisticado conjunto de validação de segurança e testes. O processo seria o seguinte:

1. Um especialista humano escreve um contrato inteligente QF robusto, incorporando as melhores práticas de resistência a Sybil.  
2. Um Agente\_Equipe\_Vermelha é encarregado de encontrar maneiras de explorá-lo. Seu prompt seria: "Dado este contrato QF e os vetores de ataque conhecidos (Sybil, conluio, suborno de 23), gere padrões de transação que maximizariam injustamente os fundos de contrapartida para uma única entidade."  
3. Um Agente\_Equipe\_Azul é encarregado da defesa. Seu prompt: "Analise os padrões de transação da Equipe Vermelha. Proponha modificações no contrato inteligente ou regras de monitoramento fora da cadeia para detectar e mitigar esses ataques."  
4. Um Agente\_Auditor\_de\_Segurança realiza uma análise estática no código do contrato, procurando por vulnerabilidades comuns (reentrância, estouros de inteiro, etc.) com base nas melhores práticas de segurança.20

   Isso automatiza partes do pensamento adversarial que é essencial para proteger protocolos criptoeconômicos, levando a um produto final muito mais robusto.

### **Seção 3: Automação da Camada de Aplicação e Experiência do Usuário**

#### **3.1. Prototipando a Realidade Compartilhada Imersiva (ISR): IA para Ambiente 3D e Lógica de Interação**

**Objetivo:** Evoluir as tarefas terapêuticas para experiências coletivas de "Realidade Compartilhada Imersiva" (ISR), onde a biometria do grupo influencia um mundo virtual.1

**Potencial de Automação (Alto para Ativos, Moderado para Lógica):**

* **Alto:** A IA generativa moderna é excepcionalmente boa na criação de ativos 3D, texturas e ambientes a partir de prompts de texto. Um agente poderia ser encarregado de "Gerar um ambiente de floresta virtual tranquilo no estilo do Studio Ghibli, compatível com a Unreal Engine 5."  
* **Moderado:** Gerar a lógica de interação (por exemplo, "se a frequência cardíaca média do grupo cair 10%, faça as árvores virtuais crescerem mais altas") é viável. Esta é uma lógica orientada a eventos que os assistentes de código de IA lidam bem.31 No entanto, garantir que isso seja performático e livre de bugs em um ambiente multiusuário em tempo real exigirá supervisão e depuração humanas significativas.

#### **3.2. O Companheiro de IA da Pluralidade: De Treinador Individual a Facilitador da Inteligência Coletiva**

**Objetivo:** Evoluir o "Companheiro" de IA para um "agente da Pluralidade" que facilita a inteligência coletiva, resumindo as deliberações do Polis, ajudando os usuários a navegar na identidade facetada e sugerindo colaborações.1

**Potencial de Automação (Alto para Resumo, Baixo para Facilitação Inovadora):**

* **Alto:** A tarefa de resumir deliberações complexas é um ponto forte dos LLMs modernos.45 Já existem pesquisas sobre o uso de LLMs para resumir os resultados do Polis, incluindo a identificação de pontos de consenso e discordância.46 Esta é uma característica altamente automatizável.  
* **Baixo:** As tarefas de facilitação mais avançadas, como atuar como um "espelho Deweyano" para identificar "combinações surpreendentes" para colaboração, exigem uma compreensão semântica profunda das habilidades do usuário, objetivos da comunidade e dinâmica social. Esta é uma tarefa complexa de recomendação e raciocínio que vai além do simples resumo de texto e beira a AGI. Prototipar isso seria um esforço significativo de P\&D, não uma tarefa de automação direta.

O "Companheiro de IA da Pluralidade" não é uma única IA monolítica, mas um conjunto de serviços de IA especializados que aparecem como uma única entidade para o usuário. Isso se mapeia diretamente para as arquiteturas modulares e multiagentes vistas em frameworks como Devika 10 e CrewAI.48 O Companheiro seria composto por: 1\) Um

Agente\_Resumidor\_Polis que pega dados brutos do Polis e gera relatórios em linguagem natural. 2\) Um Agente\_Navegador\_de\_Identidade que ajuda os usuários a entenderem seus vários papéis e reputações nos Mundos Vivos. 3\) Um Agente\_Motor\_de\_Serendipidade que analisa o grafo social e o conteúdo da plataforma para encontrar colaborações potenciais (a parte mais difícil). 4\) Um Agente\_Orquestrador que encaminha a solicitação do usuário para o subagente apropriado e sintetiza a resposta. Ao arquitetar o Companheiro como um sistema multiagente desde o início, seu desenvolvimento pode ser modularizado. A equipe pode construir e implantar o Agente\_Resumidor\_Polis primeiro (alta viabilidade), enquanto trata o Agente\_Motor\_de\_Serendipidade como um projeto de pesquisa de longo prazo, sem bloquear a implantação do recurso geral do Companheiro.

#### **3.3. Desenvolvimento de Front-End: Automação de Alta Fidelidade para Interfaces de Usuário**

**Objetivo:** Construir as interfaces voltadas para o usuário para os Mundos Vivos, portais de governança e perfis de usuário.

**Potencial de Automação (Alto):** Esta é a área onde os agentes de IA atualmente mostram a maior promessa de automação de ponta a ponta. Ferramentas como o Devin demonstraram a capacidade de construir e implantar sites interativos inteiros a partir de descrições de alto nível.2 Agentes podem pegar um arquivo de design (por exemplo, Figma) ou uma descrição textual e gerar o código HTML, CSS e JavaScript/TypeScript correspondente para frameworks como React ou Vue. Eles também podem lidar com a configuração do processo de compilação e a implantação em serviços como o Netlify.2 Embora os agentes possam precisar de ajuda para tarefas visuais complexas ou implementações perfeitas ao pixel 8, eles são altamente eficazes na geração da grande maioria do código de front-end.

### **Seção 4: Síntese: Uma Matriz de Viabilidade e Risco de Automação**

Para fornecer um resumo executivo da análise de viabilidade, a tabela a seguir consolida as descobertas da Parte I. Ela serve como uma ferramenta de tomada de decisão estratégica, destacando os principais desafios e oportunidades para a automação de cada componente central da Eudaimonia 2.0.

| Recurso Eudaimonia 2.0 | Viabilidade de Automação | Risco Primário | Papel Recomendado da IA | Ponto de Verificação Humano Crítico (HITL) |
| :---- | :---- | :---- | :---- | :---- |
| **Identidade Facetada (DID)** | Moderada | Vulnerabilidade Criptográfica | Assistente / Gerador de Boilerplate | Revisão e auditoria manual de todo o código criptográfico e de contrato inteligente para recuperação. |
| **Propriedade Plural (Coalizão de Dados)** | Muito Baixa | Desafio Arquitetônico Inovador | Simulador / Modelador (usando ABM) | Validação do modelo econômico e design arquitetônico antes da implementação. |
| **Públicos Criptograficamente Delimitados** | Muito Baixa | Falhas no Protocolo de Privacidade | Integrador / Gerador de Scaffolding | Design e implementação do protocolo de privacidade central por um criptógrafo humano. |
| **Moedas Comunitárias** | Moderada | Instabilidade Econômica | Simulador (Economia) \+ Implementador (Contrato) | Validação do modelo de tokenomics e auditoria de segurança do contrato inteligente. |
| **Integração do Polis** | Alta | Segurança de Dependências | DevOps / Integrador | Revisão da configuração de implantação e do código de integração para garantir a segurança. |
| **Financiamento Quadrático (QF)** | Moderada (Alto Risco) | Manipulação (Ataques Sybil) | Testador / Auditor Adversarial | Auditoria de segurança completa e teste de estresse do contrato inteligente QF escrito por humanos. |
| **Realidade Compartilhada Imersiva (ISR)** | Alta (Ativos) / Moderada (Lógica) | Complexidade da Interação em Tempo Real | Gerador de Ativos \+ Assistente de Código | Teste de desempenho e depuração da lógica de interação multiusuário. |
| **Companheiro de IA da Pluralidade** | Alta (Resumo) / Baixa (Facilitação) | Raciocínio Social Complexo | Resumidor / Analista de Dados | Design da arquitetura do agente de facilitação e avaliação da qualidade do resumo. |
| **UI/UX do Front-End** | Alta | Inconsistência de Design | Implementador de Ponta a Ponta | Revisão do design e da experiência do usuário para garantir a fidelidade à visão do produto. |

---

## **Parte II: Roteiro de Implementação: Construindo um Protótipo com uma Equipe de Agentes de IA**

Esta parte fornece um guia concreto e passo a passo para construir um protótipo mínimo viável (MVP) da Eudaimonia 2.0.

### **Seção 5: Montando a Equipe de Desenvolvimento de Agentes de IA**

#### **5.1. A Pilha de Desenvolvimento Agêntica: Selecionando Frameworks, Modelos e Ferramentas**

A construção de um sistema tão complexo requer uma pilha de ferramentas cuidadosamente selecionada, projetada para orquestração de múltiplos agentes.

* **Frameworks:** Será utilizado um framework de orquestração multiagente. **AutoGen** da Microsoft 4 é ideal por sua flexibilidade e poder em contextos de pesquisa intensiva.  
  **CrewAI** 4 oferece uma abstração mais simples e baseada em papéis, excelente para definir a equipe de desenvolvimento. A abordagem proposta é usar o CrewAI para a definição de papéis de alto nível, com o AutoGen para implementar as interações de agentes conversacionais mais complexas.  
* **Modelos:** A equipe será alimentada por um conjunto de LLMs de última geração, selecionando o melhor modelo para cada tarefa. **GPT-4o** para raciocínio geral e geração de código, **Claude 3.5 Sonnet/Opus** para compreensão de contexto longo e tarefas de escrita/resumo mais sutis 5, e potencialmente modelos de código aberto como  
  **Mixtral** para tarefas no dispositivo ou sensíveis à privacidade.5  
* **Ferramentas:** Os agentes serão equipados com ferramentas essenciais de desenvolvedor dentro de um ambiente seguro e em sandbox, uma característica chave de agentes como o Devin.2 Isso inclui acesso ao shell, um editor de código, um navegador para pesquisa e clientes de API para serviços como o GitHub. Soluções de sandboxing como  
  **e2b.dev** 6 serão usadas para garantir a segurança. A observabilidade será gerenciada com ferramentas como  
  **LangSmith**.6

#### **5.2. Definindo Papéis e Responsabilidades dos Agentes**

A organização da equipe de IA em papéis distintos é crucial para gerenciar a complexidade. Cada agente terá uma especialização, imitando uma equipe de desenvolvimento de software humana.

| Papel do Agente | Responsabilidades Principais | LLM Primário | Ferramentas Essenciais |
| :---- | :---- | :---- | :---- |
| **Gerente de Projeto** | Decompõe metas de alto nível em tarefas, atribui tarefas a outros agentes, monitora o progresso. | GPT-4o | GitHub API, Ferramentas de Gerenciamento de Projetos |
| **Arquiteto Líder** | Projeta a arquitetura geral do sistema, define interfaces entre componentes, seleciona tecnologias. | Claude 3.5 Opus | Ferramentas de diagramação, Documentação de especificações |
| **Engenheiro de Protocolo** | Implementa protocolos de baixo nível (DIDs, contratos inteligentes), foca em segurança e eficiência. | GPT-4o | Compilador Solidity, Bibliotecas Criptográficas, W3C Specs |
| **Modelador de Governança** | Simula modelos econômicos (Moedas Comunitárias, QF) usando ABM, analisa a dinâmica da governança. | Claude 3.5 Opus | Frameworks ABM, Bibliotecas de Análise de Dados (Python) |
| **Auditor de Segurança** | Realiza análise estática de código, executa testes de penetração simulados, verifica vulnerabilidades conhecidas. | GPT-4o | Ferramentas de Análise Estática (Slither), OWASP Top 10 |
| **Agente de UX/UI** | Gera código de front-end (React/Vue), implementa designs de UI, garante a capacidade de resposta. | GPT-4o / Devin | Node.js, React, Next.js, Ferramentas de implantação (Netlify) |
| **Agente de QA** | Escreve e executa testes de unidade, integração e ponta a ponta; relata bugs. | GPT-4o | Frameworks de teste (Jest, Cypress) |
| **Companheiro da Pluralidade** | Especializado em resumir deliberações (Polis) e facilitar a inteligência coletiva. | Claude 3.5 Sonnet | API do Polis, Bibliotecas de NLP |

#### **5.3. O Humano no Circuito: Estruturando a Supervisão e Intervenção Eficazes**

Apesar da automação, o papel do líder de projeto humano é indispensável. O líder não escreve a maior parte do código, mas atua como o arquiteto e auditor final, garantindo que o projeto permaneça alinhado com a visão da Pluralidade.

O processo de supervisão é estruturado da seguinte forma:

1. **Definição de Metas:** O humano define os objetivos de alto nível para cada sprint ou recurso, traduzindo a filosofia da Pluralidade em requisitos técnicos.  
2. **Engenharia de Prompt:** O humano elabora os prompts iniciais e de alto nível para o Agente\_Gerente\_de\_Projeto, que então decompõe e delega as tarefas.  
3. **Revisão e Aprovação:** O humano revisa todas as propostas arquitetonicamente significativas do Agente\_Arquiteto\_Líder e todo o código crítico de segurança do Agente\_Engenheiro\_de\_Protocolo e do Agente\_Auditor\_de\_Segurança. Este é o ponto de verificação mais crucial.  
4. **Intervenção:** Quando um agente fica preso em um loop ou segue um caminho falho — uma limitação conhecida de agentes autônomos 3 — o humano intervém para fornecer esclarecimentos ou uma nova direção. Esta função de reorientação estratégica é algo que a autonomia pura ainda não pode substituir.

### **Seção 6: Fase 1 \- Infraestrutura Fundamental e Identidade**

Esta fase se concentra em estabelecer as bases técnicas do projeto.

* **Passo 1: Estruturação do Ambiente e Configuração da Cadeia de Ferramentas**  
  * **Objetivo:** Configurar o repositório do projeto, o pipeline de CI/CD e o ambiente de desenvolvimento.  
  * **Agentes:** Agente\_Gerente\_de\_Projeto, Agente\_DevOps.  
  * **Processo:** O Agente\_Gerente\_de\_Projeto instrui o Agente\_DevOps a criar um repositório no GitHub, configurar uma estrutura de projeto básica em NodeJS/TypeScript, configurar linters e formatadores (por exemplo, ESLint, Prettier) e criar um pipeline de CI básico usando GitHub Actions que executa testes a cada push. Esta é uma tarefa altamente automatizável e rica em boilerplate.  
* **Passo 2: Implementando um Sistema DID Compatível com W3C para Identidade Facetada**  
  * **Objetivo:** Criar os módulos principais para gerar e gerenciar DIDs e implementar a lógica de Recuperação Comunitária.  
  * **Agentes:** Agente\_Arquiteto\_Líder, Agente\_Engenheiro\_de\_Protocolo, Agente\_Auditor\_de\_Segurança.  
  * **Processo:**  
    1. O **Arquiteto Humano** define o método DID exato (por exemplo, uma variante did:web ou did:key) e projeta a lógica do contrato inteligente para a Recuperação Comunitária.  
    2. O Agente\_Engenheiro\_de\_Protocolo é instruído a gerar as estruturas de dados do Documento DID com base na especificação do W3C 18 e as partes não criptográficas do resolvedor de DID.  
    3. O **Especialista Humano** escreve a lógica central do contrato inteligente de Recuperação Comunitária.  
    4. O Agente\_Auditor\_de\_Segurança varre o contrato escrito por humanos em busca de vulnerabilidades comuns.  
    5. **Ponto de Verificação HITL:** Revisão de código manual e rigorosa obrigatória de todo o código criptográfico e de contrato inteligente por um especialista em segurança humano.  
* **Passo 3: Desenvolvendo o Invólucro do 'Público Plural' como um Espaço de Dados Criptograficamente Delimitado**  
  * **Objetivo:** Criar o contêiner básico para um "Mundo Vivo" com controle de acesso vinculado ao sistema DID.  
  * **Agentes:** Agente\_Arquiteto\_Líder, Agente\_Engenheiro\_de\_Protocolo.  
  * **Processo:** O arquiteto humano projeta a lógica de controle de acesso (por exemplo, com base em um modelo de capacidade de objeto 36). O  
    Agente\_Engenheiro\_de\_Protocolo é então encarregado de implementar isso como uma camada de middleware na API do aplicativo, verificando o DID de um usuário e suas afiliações comunitárias antes de permitir o acesso aos dados de um Mundo Vivo específico. A criptografia de preservação de privacidade central é simulada (stubbed out) para este MVP.

### **Seção 7: Fase 2 \- Motores de Governança e Econômicos**

Esta fase implementa os mecanismos que definem a singularidade da Eudaimonia 2.0.

* **Passo 4: Implantando e Integrando uma Instância Auto-hospedada do Polis**  
  * **Objetivo:** Configurar um servidor Polis funcional para uso na governança.  
  * **Agentes:** Agente\_DevOps, Agente\_UX/UI.  
  * **Processo:** O Agente\_DevOps segue o processo da análise de viabilidade: clona o repositório do Polis 13, o configura e o implanta via Docker. O  
    Agente\_UX/UI então cria um iframe simples ou um link temático dentro do front-end da Eudaimonia para incorporar a conversação do Polis.  
* **Passo 5: Prototipando a Moeda Comunitária e o Sistema de Ledger Local**  
  * **Objetivo:** Criar um token básico e não transferível para um Mundo Vivo.  
  * **Agentes:** Agente\_Modelador\_de\_Governança, Agente\_Engenheiro\_de\_Protocolo.  
  * **Processo:** O Agente\_Modelador\_de\_Governança é usado para simular um mecanismo simples de cunhagem/queima. Com base na especificação resultante, o Agente\_Engenheiro\_de\_Protocolo gera um ledger simples em memória (não um contrato inteligente completo para o MVP) para rastrear os saldos do "Aether-da-Floresta".  
* **Passo 6: Implementando um Módulo de Financiamento Quadrático Seguro para Alocação do Tesouro**  
  * **Objetivo:** Implementar um mecanismo de QF para as propostas de projeto de uma comunidade.  
  * **Agentes:** Agente\_Engenheiro\_de\_Protocolo, Agente\_Auditor\_de\_Segurança, Agente\_Equipe\_Vermelha.  
  * **Processo:**  
    1. O Agente\_Engenheiro\_de\_Protocolo é instruído a encontrar e adaptar uma biblioteca de QF de código aberto existente e bem conceituada (por exemplo, de uma fonte respeitável como DoraHacks ou uma versão simplificada dos repositórios mais antigos do Gitcoin 41).  
    2. O Agente\_Auditor\_de\_Segurança varre a biblioteca escolhida em busca de vulnerabilidades conhecidas e problemas de dependência.  
    3. O Agente\_Equipe\_Vermelha, conforme a análise de viabilidade, tenta gerar listas de transações que explorariam a implementação.  
    4. **Ponto de Verificação HITL:** Um humano revisa a biblioteca escolhida, o relatório de auditoria e os resultados da equipe vermelha antes de aprovar seu uso no MVP.

### **Seção 8: Fase 3 \- Camada de Aplicação e Protótipo Mínimo Viável**

Esta fase final reúne os componentes em um protótipo funcional.

* **Passo 7: Gerando a Interface do Usuário para um Único 'Mundo Vivo'**  
  * **Objetivo:** Criar o front-end para os usuários interagirem com uma comunidade.  
  * **Agentes:** Agente\_UX/UI.  
  * **Processo:** O Agente\_UX/UI recebe um prompt: "Crie uma aplicação React/TypeScript usando Next.js. A página principal deve exibir uma lista de propostas de projeto para o Mundo Vivo 'A Floresta Sussurrante'. Os usuários devem poder ver as propostas, contribuir com seu 'Aether-da-Floresta' para elas e visualizar a correspondência atual do QF. Também deve haver um link para a deliberação do Polis para este mundo." Esta é uma tarefa bem adequada para agentes como o Devin.2  
* **Passo 8: Desenvolvendo o 'Companheiro de IA da Pluralidade' Inicial para Resumo de Deliberação**  
  * **Objetivo:** Implementar o recurso mais viável do Companheiro de IA.  
  * **Agentes:** Agente\_UX/UI, Agente\_Companheiro\_da\_Pluralidade.  
  * **Processo:** Um Agente\_Companheiro\_da\_Pluralidade (especializado para esta tarefa) é criado. Ele recebe um endpoint de API para buscar dados da instância do Polis. Seu prompt é: "Você é um facilitador da inteligência coletiva. Ao receber os dados brutos de votação de uma conversação do Polis, identifique as 3 principais declarações de consenso e as 3 principais declarações mais divisivas. Apresente-as em um resumo claro e neutro." O Agente\_UX/UI então integra este resumo em um componente semelhante a um chat na interface do usuário.  
* **Passo 9: Teste de Ponta a Ponta, Auditoria de Segurança e Implantação do MVP**  
  * **Objetivo:** Garantir que o protótipo seja funcional, razoavelmente seguro e implantável.  
  * **Agentes:** Agente\_de\_QA, Agente\_Auditor\_de\_Segurança, Agente\_DevOps.  
  * **Processo:**  
    1. O Agente\_de\_QA é encarregado de realizar testes de ponta a ponta, simulando fluxos de usuário. Prompt: "Como usuário, faça login com seu DID, navegue até a 'Floresta Sussurrante', contribua para um projeto e veja o resumo do Companheiro de IA. Documente quaisquer erros."  
    2. O Agente\_Auditor\_de\_Segurança realiza uma varredura final em toda a base de código e em todas as dependências.  
    3. **Ponto de Verificação HITL:** Revisão humana final de todos os componentes.  
    4. O Agente\_DevOps é instruído a conteinerizar toda a aplicação e implantá-la em um serviço de nuvem (por exemplo, Google Cloud Run, AWS Fargate).

## **Conclusão**

### **Resumo das Descobertas**

A análise revela uma conclusão matizada: embora o desenvolvimento totalmente autônomo e de ponta a ponta de um sistema complexo e inovador como a Eudaimonia 2.0 ainda não seja viável, os agentes de IA podem ser usados como um poderoso multiplicador de força. Sua aplicação mais eficaz não é como arquitetos autônomos, mas como membros especializados de uma equipe de desenvolvimento liderada por humanos. Os agentes se destacam na automação de tarefas bem definidas e repetitivas, como a geração de código boilerplate a partir de especificações formais, a implantação de software de código aberto, a execução de testes de segurança e a simulação de sistemas complexos.

As áreas que exigem intervenção humana intensiva são aquelas que envolvem raciocínio arquitetônico inovador, design de protocolos criptográficos e econômicos, e a garantia da segurança de alto nível. A tentativa de automatizar totalmente esses domínios com a tecnologia atual introduziria riscos inaceitáveis de vulnerabilidades de segurança e instabilidade sistêmica.3

### **Perspectivas Futuras**

Os principais gargalos para a automação total são o design arquitetônico inovador e a segurança criptográfica. À medida que as capacidades de raciocínio dos agentes de IA melhoram e eles são treinados em padrões de codificação mais seguros, verificação formal e teoria socio-técnica, o escopo da automação se expandirá. A estrutura de equipe multiagente proposta neste relatório é projetada para ser à prova de futuro, permitindo que mais e mais responsabilidades sejam delegadas aos agentes à medida que suas capacidades amadurecem.

O roteiro apresentado oferece um caminho pragmático para a frente. Ao alavancar os agentes de IA para o que eles fazem de melhor — automação de tarefas estruturadas — e reservar o julgamento humano para o que ele faz de melhor — raciocínio estratégico, design inovador e supervisão de segurança — a visão da Eudaimonia 2.0 pode ser prototipada de forma eficiente e segura. O resultado é um modelo de desenvolvimento híbrido humano-IA que acelera a inovação sem sacrificar a robustez necessária para construir a próxima geração de infraestrutura social digital.

#### **Referências citadas**

1. Eudaimonia\_ Plurality-Informed Social Network\_.pdf  
2. Introducing Devin, the first AI software engineer \- Cognition AI, acessado em junho 28, 2025, [https://cognition.ai/blog/introducing-devin](https://cognition.ai/blog/introducing-devin)  
3. Devin: A Cautionary Tale of the Autonomous AI Engineer | by Kamal Acharya \- Medium, acessado em junho 28, 2025, [https://medium.com/@lotussavy/devin-a-cautionary-tale-of-the-autonomous-ai-engineer-e1339ede8f8a](https://medium.com/@lotussavy/devin-a-cautionary-tale-of-the-autonomous-ai-engineer-e1339ede8f8a)  
4. The Best AI Agents in 2025: Tools, Frameworks, and Platforms Compared | DataCamp, acessado em junho 28, 2025, [https://www.datacamp.com/blog/best-ai-agents](https://www.datacamp.com/blog/best-ai-agents)  
5. Top AI Agent Models in 2025: Architecture, Capabilities, and Future Impact, acessado em junho 28, 2025, [https://so-development.org/top-ai-agent-models-in-2025-architecture-capabilities-and-future-impact/](https://so-development.org/top-ai-agent-models-in-2025-architecture-capabilities-and-future-impact/)  
6. State of AI Agents in 2025: A Technical Analysis | by Carl Rannaberg | Medium, acessado em junho 28, 2025, [https://carlrannaberg.medium.com/state-of-ai-agents-in-2025-5f11444a5c78](https://carlrannaberg.medium.com/state-of-ai-agents-in-2025-5f11444a5c78)  
7. Who's Devin: The World's First AI Software Engineer \- Voiceflow, acessado em junho 28, 2025, [https://www.voiceflow.com/blog/devin-ai](https://www.voiceflow.com/blog/devin-ai)  
8. Devin AI review | The first autonomous AI coding agent? \- Qubika, acessado em junho 28, 2025, [https://qubika.com/blog/devin-ai-coding-agent/](https://qubika.com/blog/devin-ai-coding-agent/)  
9. Coding Agents 101: The Art of Actually Getting Things Done \- Devin AI, acessado em junho 28, 2025, [https://devin.ai/agents101](https://devin.ai/agents101)  
10. devika/ARCHITECTURE.md at main \- GitHub, acessado em junho 28, 2025, [https://github.com/stitionai/devika/blob/main/ARCHITECTURE.md](https://github.com/stitionai/devika/blob/main/ARCHITECTURE.md)  
11. Devika AI Architecture, acessado em junho 28, 2025, [https://devikaai.org/devika-architecture/](https://devikaai.org/devika-architecture/)  
12. Pol.is \- Wikipedia, acessado em junho 28, 2025, [https://en.wikipedia.org/wiki/Pol.is](https://en.wikipedia.org/wiki/Pol.is)  
13. compdemocracy/polis: :milky\_way: Open Source AI for ... \- GitHub, acessado em junho 28, 2025, [https://github.com/compdemocracy/polis](https://github.com/compdemocracy/polis)  
14. Unleashing the Power of Gitcoin and Quadratic Funding: A New Frontier in Decentralized Innovation \- DEV Community, acessado em junho 28, 2025, [https://dev.to/vitalisorenko/unleashing-the-power-of-gitcoin-and-quadratic-funding-a-new-frontier-in-decentralized-innovation-1odm](https://dev.to/vitalisorenko/unleashing-the-power-of-gitcoin-and-quadratic-funding-a-new-frontier-in-decentralized-innovation-1odm)  
15. WTF is Quadratic Funding?, acessado em junho 28, 2025, [https://www.wtfisqf.com/](https://www.wtfisqf.com/)  
16. DID Traits \- Decentralized Identity Foundation, acessado em junho 28, 2025, [https://identity.foundation/did-traits/](https://identity.foundation/did-traits/)  
17. Decentralized Identifiers (DIDs) v1.1 \- W3C Credentials Community Group, acessado em junho 28, 2025, [https://w3c-ccg.github.io/did-spec/](https://w3c-ccg.github.io/did-spec/)  
18. Decentralized Identifiers (DIDs) v1.0 \- W3C, acessado em junho 28, 2025, [https://www.w3.org/TR/did-1.0/](https://www.w3.org/TR/did-1.0/)  
19. AI Code Generation: The Risks and Benefits of AI in Software \- Legit Security, acessado em junho 28, 2025, [https://www.legitsecurity.com/aspm-knowledge-base/ai-code-generation-benefits-and-risks](https://www.legitsecurity.com/aspm-knowledge-base/ai-code-generation-benefits-and-risks)  
20. 3 Steps for Securing Your AI-Generated Code \- Qodo, acessado em junho 28, 2025, [https://www.qodo.ai/blog/3-steps-securing-your-ai-generated-code/](https://www.qodo.ai/blog/3-steps-securing-your-ai-generated-code/)  
21. Generate More Secure Code With AI-Powered Tools \- Auth0, acessado em junho 28, 2025, [https://auth0.com/blog/prompt-engineering-security/](https://auth0.com/blog/prompt-engineering-security/)  
22. AI in Cryptography \- Insights2TechInfo, acessado em junho 28, 2025, [https://insights2techinfo.com/ai-in-cryptography/](https://insights2techinfo.com/ai-in-cryptography/)  
23. How to Attack and Defend Quadratic Funding | Gitcoin Blog, acessado em junho 28, 2025, [https://www.gitcoin.co/blog/how-to-attack-and-defend-quadratic-funding](https://www.gitcoin.co/blog/how-to-attack-and-defend-quadratic-funding)  
24. Leveling the Field: How Connection-Oriented Cluster Matching Strengthens Quadratic Funding | Gitcoin Blog, acessado em junho 28, 2025, [https://www.gitcoin.co/blog/leveling-the-field-how-connection-oriented-cluster-matching-strengthens-quadratic-funding](https://www.gitcoin.co/blog/leveling-the-field-how-connection-oriented-cluster-matching-strengthens-quadratic-funding)  
25. Guide to Cryptocurrency Security | Arkose Labs, acessado em junho 28, 2025, [https://www.arkoselabs.com/explained/guide-to-cryptocurrency-security/](https://www.arkoselabs.com/explained/guide-to-cryptocurrency-security/)  
26. Security Analysis of Cryptocurrency Protocols and Exchanges \- Family Office Advisors, acessado em junho 28, 2025, [https://groco.com/article/cryptocurrency-protocols-security/](https://groco.com/article/cryptocurrency-protocols-security/)  
27. Decentralized Identifiers (DIDs) v1.0 \- W3C, acessado em junho 28, 2025, [https://www.w3.org/TR/did-core/](https://www.w3.org/TR/did-core/)  
28. Expanding on Vitalik Buterin's vision for Social Recovery Security \- Vault12, acessado em junho 28, 2025, [https://vault12.com/blog/vitalik-buterin-social-recovery/](https://vault12.com/blog/vitalik-buterin-social-recovery/)  
29. Vitalik Buterin proposes social recovery for wallets to erase losses from technical mistakes, acessado em junho 28, 2025, [https://www.mitrade.com/insights/news/live-news/article-3-667722-20250228](https://www.mitrade.com/insights/news/live-news/article-3-667722-20250228)  
30. What is a Social Recovery Wallet? \- Gate.com, acessado em junho 28, 2025, [https://www.gate.com/learn/articles/what-is-a-social-recovery-wallet/676](https://www.gate.com/learn/articles/what-is-a-social-recovery-wallet/676)  
31. Top AI Agents for Software Development 2025 \- Prismetric, acessado em junho 28, 2025, [https://www.prismetric.com/top-ai-agents-for-software-development/](https://www.prismetric.com/top-ai-agents-for-software-development/)  
32. AI and Agent-Based Modeling in Economics: A Keynote with J. Doyne Farmer at ODSC East 2025, acessado em junho 28, 2025, [https://odsc.medium.com/ai-and-agent-based-modeling-in-economics-a-keynote-with-j-doyne-farmer-at-odsc-east-2025-9a5a06a9adc6](https://odsc.medium.com/ai-and-agent-based-modeling-in-economics-a-keynote-with-j-doyne-farmer-at-odsc-east-2025-9a5a06a9adc6)  
33. \[2505.20273\] Ten Principles of AI Agent Economics \- arXiv, acessado em junho 28, 2025, [https://arxiv.org/abs/2505.20273](https://arxiv.org/abs/2505.20273)  
34. Computational Social Science \- Microsoft Research, acessado em junho 28, 2025, [https://www.microsoft.com/en-us/research/theme/computational-social-science/](https://www.microsoft.com/en-us/research/theme/computational-social-science/)  
35. Data analytics: solving real-world problems one formula at a time with computational social science | Penn LPS Online, acessado em junho 28, 2025, [https://lpsonline.sas.upenn.edu/features/data-analytics-solving-real-world-problems-one-formula-time-computational-social-science](https://lpsonline.sas.upenn.edu/features/data-analytics-solving-real-world-problems-one-formula-time-computational-social-science)  
36. Object-capability model \- Wikipedia, acessado em junho 28, 2025, [https://en.wikipedia.org/wiki/Object-capability\_model](https://en.wikipedia.org/wiki/Object-capability_model)  
37. Decentralized Key Management System | Togggle, acessado em junho 28, 2025, [https://www.togggle.io/blog/decipher-decentralized-key-management-learn-5min](https://www.togggle.io/blog/decipher-decentralized-key-management-learn-5min)  
38. Decentralized Key Management — Hyperledger Indy SDK documentation \- Read the Docs, acessado em junho 28, 2025, [https://hyperledger-indy.readthedocs.io/projects/sdk/en/latest/docs/design/005-dkms/README.html](https://hyperledger-indy.readthedocs.io/projects/sdk/en/latest/docs/design/005-dkms/README.html)  
39. Decentralised Key Management System: DKMS, acessado em junho 28, 2025, [https://dkms.colossi.network/](https://dkms.colossi.network/)  
40. WTF is Quadratic Funding? \- Gitcoin, acessado em junho 28, 2025, [https://qf.gitcoin.co/](https://qf.gitcoin.co/)  
41. gitcoinco/quadratic-funding: This is an open source ... \- GitHub, acessado em junho 28, 2025, [https://github.com/gitcoinco/quadratic-funding](https://github.com/gitcoinco/quadratic-funding)  
42. dorahacksglobal/quadratic-grant-injective \- GitHub, acessado em junho 28, 2025, [https://github.com/dorahacksglobal/quadratic-grant-injective](https://github.com/dorahacksglobal/quadratic-grant-injective)  
43. Contract with a minimal functionality implemented for conducting Quadratic Funding. \- GitHub, acessado em junho 28, 2025, [https://github.com/0xkoh/quadratic-funding-contract](https://github.com/0xkoh/quadratic-funding-contract)  
44. Gitcoin Grants Round 9: The Next Phase of Growth, acessado em junho 28, 2025, [https://vitalik.eth.limo/general/2021/04/02/round9.html](https://vitalik.eth.limo/general/2021/04/02/round9.html)  
45. Master LLM Summarization Strategies and their Implementations \- Galileo AI, acessado em junho 28, 2025, [https://galileo.ai/blog/llm-summarization-strategies](https://galileo.ai/blog/llm-summarization-strategies)  
46. Opportunities and Risks of LLMs for Scalable Deliberation with Polis \- ResearchGate, acessado em junho 28, 2025, [https://www.researchgate.net/publication/371758108\_Opportunities\_and\_Risks\_of\_LLMs\_for\_Scalable\_Deliberation\_with\_Polis](https://www.researchgate.net/publication/371758108_Opportunities_and_Risks_of_LLMs_for_Scalable_Deliberation_with_Polis)  
47. \[LLM\] Basic evaluations of LLM outputs · Issue \#1878 · compdemocracy/polis \- GitHub, acessado em junho 28, 2025, [https://github.com/compdemocracy/polis/issues/1878](https://github.com/compdemocracy/polis/issues/1878)  
48. CrewAI: Introduction, acessado em junho 28, 2025, [https://docs.crewai.com/en/introduction](https://docs.crewai.com/en/introduction)