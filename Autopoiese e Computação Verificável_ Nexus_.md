

# **A Autopoiese da Computação Verificável: Analisando o Nexus zkVM como um Modelo para Sistemas Descentralizados Autônomos**

**Resumo:** Este artigo propõe um novo quadro teórico para a compreensão de sistemas descentralizados autônomos, sintetizando a teoria biológica da autopoiese com o paradigma criptográfico da computação verificável. Argumentamos que o fechamento operacional e a autoprodução, centrais para os sistemas autopoiéticos, encontram um análogo técnico na arquitetura das modernas máquinas virtuais de conhecimento zero (zkVMs). Utilizando a Nexus zkVM como estudo de caso primário, analisamos como os sistemas de prova recursiva (por exemplo, Nova, SuperNova) e os Dados Portadores de Prova (PCD) funcionam como mecanismos para manter a integridade sistêmica sem a dependência de uma autoridade central, criando assim uma forma de "autopoiese computacional". Este quadro é então aplicado às Organizações Autônomas Descentralizadas (DAOs), interpretando os seus modelos de governança, crises (como o hack da The DAO em 2016\) e eventos reprodutivos (bifurcações de blockchain) como fenômenos de um sistema autopoiético sociotécnico emergente. Ao traçar paralelos com a discriminação próprio/não-próprio e os mecanismos de defesa em camadas do sistema imunológico biológico, desenvolvemos um modelo robusto para analisar a segurança, identidade e autonomia destas entidades digitais nascentes. O artigo conclui que esta síntese não só oferece uma nova lente poderosa para analisar sistemas descentralizados, mas também desafia as distinções filosóficas tradicionais entre sistemas vivos e artificiais, sugerindo um contínuo de organização autônoma fundamentado na lógica da verificação em vez da confiança.

---

## 

## 

## 

## 

## 

## **1\. Introdução: O Problema da Identidade Autônoma em um Ambiente Hostil**

### **1.1. A Questão Central: O Que é um Sistema Autônomo?**

A questão fundamental que anima tanto a biologia teórica quanto a vanguarda da ciência da computação é deceptivamente simples: como pode qualquer sistema — seja ele biológico, social ou computacional — definir, manter e defender a sua identidade e integridade num ambiente complexo, dinâmico e frequentemente antagônico, sem recorrer a uma autoridade coordenadora central?.1 Esta questão é, em sua essência, um problema de limites. A própria noção de uma entidade pressupõe uma demarcação de seus arredores; uma fronteira que a distingue do que ela não é.8 Desde as membranas celulares que separam a vida do não-vivo até as fronteiras conceituais que definem sistemas sociais, a formação da identidade é um ato de delimitação.14

A história dos sistemas, da biologia à organização humana, pode ser lida como uma crônica de soluções evolutivas para este problema persistente de manter a identidade contra as forças entrópicas e as ameaças externas.16 Os sistemas vivos, em particular, desenvolveram mecanismos de uma sofisticação inigualável para a autopreservação. Estes mecanismos não são meramente reativos; eles são constitutivos da própria identidade do sistema. A capacidade de um sistema se produzir e se manter ativamente é o que Maturana e Varela (1980) denominaram autopoiese, ou "autoprodução".18 Um sistema autopoiético é aquele cuja única finalidade é a produção contínua de si mesmo, mantendo sua organização invariante enquanto seus componentes estão em fluxo constante. Esta "clausura organizacional" é a base da autonomia biológica.5

No domínio digital, a busca por autonomia tem sido mais elusiva. Sistemas centralizados dependem de administradores para definir e policiar seus limites. Sistemas federados distribuem esta autoridade, mas ainda dependem de confiança e acordo social entre os operadores dos nós.20 A promessa dos sistemas descentralizados, como as redes blockchain, é alcançar uma forma de autonomia mais radical, onde a integridade do sistema é garantida não por administradores humanos ou acordos sociais, mas pelas próprias regras do protocolo. No entanto, mesmo estes sistemas enfrentam o desafio fundamental da identidade em um ambiente hostil: como podem se defender, adaptar-se e evoluir sem sucumbir a ataques ou à desordem interna?

### **1.2. O Paradigma Biológico: O Sistema Imunológico como um Modelo para a Defesa Descentralizada**

A natureza oferece o exemplo mais bem-sucedido de um sistema de manutenção de identidade e defesa descentralizada: o sistema imunológico dos vertebrados.23 A função primordial deste sistema é a discriminação entre o "próprio" (componentes do organismo) e o "não-próprio" (agentes patogênicos, toxinas, células anormais), uma tarefa de complexidade imensa realizada sem um comando central.26 A imunologia, portanto, pode ser vista como a "ciência da discriminação próprio/não-próprio" 31, fornecendo um poderoso arcabouço conceitual para pensar sobre segurança em sistemas autônomos.

A defesa imunológica é organizada em camadas, uma estratégia análoga à "defesa em profundidade" na cibersegurança.32 A imunidade inata fornece a primeira linha de defesa: uma resposta rápida e não específica que reconhece padrões moleculares conservados associados a patógenos (PAMPs) ou a danos celulares (DAMPs).37 Se esta primeira linha é ultrapassada, a imunidade adaptativa é ativada. Esta é uma resposta mais lenta, mas altamente específica e dotada de memória, mediada por linfócitos T e B que aprendem a reconhecer e a lembrar-se de antígenos específicos.37 Esta arquitetura de defesa em camadas, que combina respostas predeterminadas com aprendizagem adaptativa, oferece um modelo robusto para a resiliência de sistemas complexos.

A convergência entre os problemas enfrentados por sistemas biológicos e sistemas computacionais não é meramente metafórica; ela reflete uma profunda isomorfia nos desafios da manutenção da integridade descentralizada. A imunologia computacional e a cibersegurança bioinspirada são campos que já exploram esta convergência, abstraindo princípios como diversidade, memória e detecção distribuída para projetar sistemas de segurança mais resilientes.24 A ascensão das zkVMs e das DAOs representa o próximo passo lógico nesta trajetória evolutiva. Estes sistemas não são apenas

*inspirados* pela autonomia biológica; eles tentam *instanciá-la* através de meios criptográficos. Uma zkVM que prova a sua própria execução está, num sentido muito real, a realizar uma discriminação perfeito entre o próprio e o não-próprio ao nível computacional. Este artigo, portanto, não apresenta uma mera analogia, mas investiga uma tendência observável na coevolução do pensamento tanto na biologia como na ciência da computação, onde ambos os campos se debatem com o mesmo problema fundamental da integridade autônoma e descentralizada.

### **1.3. Tese e Roteiro**

Este artigo apresenta a tese de que a fusão dos princípios da autopoiese com o paradigma da computação verificável oferece um novo e poderoso quadro teórico para a criação e análise de sistemas digitais verdadeiramente autônomos. Argumentamos que sistemas como a Nexus zkVM 65 representam uma nova classe de entidade cuja clausura organizacional é garantida não pela confiança social ou decreto legal, mas por prova matemática.

Para desenvolver esta tese, o artigo está estruturado da seguinte forma:  
A Seção 2 aprofunda a teoria da autopoiese, traçando sua origem na biologia de Maturana e Varela, sua controversa aplicação aos sistemas sociais por Niklas Luhmann, e as críticas e refinamentos propostos por teóricas como Donna Haraway.  
A Seção 3 explora os mecanismos criptográficos que tornam a autopoiese computacional possível. Focamos na computação verificável, explicando os fundamentos das provas de conhecimento zero (ZKPs) e detalhando a arquitetura da Nexus zkVM, com ênfase nos seus esquemas de dobramento recursivo e no conceito de Dados Portadores de Prova (PCD). Esta seção também revisita a analogia do sistema imunológico, mapeando conceitos como tolerância e discriminação próprio/não-próprio para protocolos criptográficos.  
A Seção 4 aplica este quadro teórico à análise de Organizações Autônomas Descentralizadas (DAOs). Examinamos as DAOs como sistemas autopoiéticos sociotécnicos nascentes, interpretando seus modelos de governança, crises e eventos reprodutivos — como a bifurcação (fork) da The DAO em 2016 — através da lente da autopoiese e da teoria imunológica.  
Finalmente, a Seção 5 sintetiza os argumentos e explora as implicações filosóficas mais amplas desta nova concepção de ser digital, abordando questões sobre a natureza da realidade, agência e identidade na era da computação verificável.

---

## **2\. O Princípio Autopoiético: Da Vida Biológica aos Sistemas Sociais**

Para compreender a possibilidade de sistemas digitais autônomos, é imperativo primeiro apreender o conceito de autonomia na sua forma mais fundamental: a vida biológica. A teoria da autopoiese, desenvolvida pelos biólogos chilenos Humberto Maturana e Francisco Varela, oferece a definição mais rigorosa e influente da organização que constitui um sistema vivo como uma unidade autônoma.3 Esta seção irá detalhar esta teoria, a sua controversa extensão aos sistemas sociais por Niklas Luhmann, e as críticas que a refinaram, estabelecendo assim o quadro conceptual para a nossa análise da autopoiese computacional.

### **2.1. A Organização do Vivo: A Teoria da Autopoiese de Maturana e Varela**

#### **2.1.1. Definindo a Autopoiese**

Na sua obra seminal, *Autopoiesis and Cognition: The Realization of the Living* (1980), Maturana e Varela definiram um sistema autopoiético como "uma rede de processos de produção (transformação e destruição) de componentes que: (i) através das suas interações e transformações, regeneram e realizam continuamente a rede de processos (relações) que os produziu; e (ii) constituem \[a máquina\] como uma unidade concreta no espaço em que existem, especificando o domínio topológico da sua realização como tal rede".3 Em termos mais simples, um sistema autopoiético é um sistema que se produz a si mesmo.68 O exemplo paradigmático é a célula biológica: a sua rede de reações metabólicas produz os componentes (proteínas, lípidos, etc.) que, por sua vez, constituem a própria rede e a membrana celular que a delimita. O produto do sistema é o próprio sistema.3 Esta organização circular e autorreferencial é o que define a vida, não os seus componentes materiais específicos, que estão em constante fluxo.

#### **2.1.2. Clausura Organizacional vs. Clausura Operacional**

Uma distinção crítica na teoria da autopoiese é entre organização e estrutura. A **organização** refere-se às relações entre os componentes que definem um sistema como uma unidade de uma determinada classe (por exemplo, as relações metabólicas que definem uma célula). A **estrutura** refere-se aos componentes e relações reais que concretizam essa organização num dado momento.6 Um sistema autopoiético mantém a sua organização invariante, enquanto a sua estrutura pode mudar continuamente.

Esta invariância organizacional é conseguida através da **clausura organizacional** e da **clausura operacional**. O sistema é organizacionalmente fechado porque a sua identidade é definida por uma rede de relações que se refere apenas a si mesma.5 É operacionalmente fechado porque os seus processos de produção de componentes são recursivamente dependentes uns dos outros; não há inputs ou outputs de operações, apenas de matéria e energia.6 Esta clausura é a base da autonomia do sistema: o seu comportamento é determinado pela sua própria estrutura e organização, não pelo ambiente.6

#### **2.1.3. Acoplamento Estrutural e o Ambiente**

A clausura organizacional não implica isolamento. Pelo contrário, os sistemas autopoiéticos são **estruturalmente abertos** ao seu ambiente. Eles existem num meio com o qual trocam matéria e energia. A relação entre um sistema autopoiético e o seu meio é descrita pelo conceito de **acoplamento estrutural**.7 O ambiente não determina a organização do sistema, mas pode desencadear ("perturbar") mudanças na sua estrutura. O sistema, por sua vez, compensa estas perturbações com mudanças estruturais que mantêm a sua organização. Esta história de interações recorrentes leva a uma congruência mútua entre o sistema e o meio. Um sistema vivo persiste apenas enquanto as suas mudanças estruturais forem congruentes com a manutenção da sua autopoiese.

#### **2.1.4. Autopoiese e Cognição**

A consequência mais radical da teoria de Maturana e Varela é a sua redefinição da cognição. Eles afirmam que "os sistemas vivos são sistemas cognitivos, e viver como processo é um processo de cognição".75 A cognição não é a representação de um mundo externo preexistente, mas sim a

**enação** (enactment) de um mundo através do acoplamento estrutural.76 Um sistema vivo "traz à tona" um domínio de significância através das suas interações, definindo o que é relevante para a sua própria manutenção. O conhecimento, nesta perspetiva, não é sobre ter um modelo interno preciso do mundo externo; é sobre ter a capacidade de agir eficazmente no meio para manter a própria vida.

### **2.2. A Virada Luhmanniana: A Comunicação como Autopoiese**

O sociólogo alemão Niklas Luhmann realizou a mais ambiciosa e controversa extensão da teoria da autopoiese, aplicando-a aos sistemas sociais.19 A sua obra representa uma mudança de paradigma na teoria social, afastando-se de modelos centrados no ator ou na ação para um modelo centrado na comunicação.

#### **2.2.1. Sistemas Sociais como Sistemas de Comunicação**

Para Luhmann, o elemento fundamental e autopoiético dos sistemas sociais não é o ser humano, mas a **comunicação**.82 Um evento de comunicação (que Luhmann decompõe em três seleções: informação, enunciado e compreensão) torna possível e necessária a comunicação subsequente. As comunicações produzem comunicações, formando um sistema operacionalmente fechado que se reproduz a si mesmo a partir dos seus próprios elementos.90

A teoria de Luhmann, embora poderosa, enfrenta uma objeção crítica: como pode a "comunicação" ser um elemento que produz outra "comunicação" sem a agência direta da consciência humana? Este problema do "fantasma na máquina", uma grande crítica a Luhmann 91, encontra uma solução literal e potente na forma de contratos inteligentes e zkVMs. A teoria original de Maturana e Varela está enraizada em processos físicos e químicos; os componentes de uma célula produzem fisicamente outros componentes.3 Luhmann abstrai isso para o domínio social, onde uma comunicação produz as condições para a próxima.19 Os críticos argumentam que esta abstração é excessiva; as comunicações não "agem" por si mesmas — as pessoas agem. O sistema de Luhmann parece exigir atores humanos, mas depois os exclui da definição do sistema, criando um paradoxo. Os contratos inteligentes numa blockchain oferecem um mecanismo onde isto deixa de ser uma metáfora. Uma transação (uma comunicação) numa blockchain desencadeia

*literal e automaticamente* a execução de um código que produz um novo estado, o qual, por sua vez, permite a próxima transação válida (comunicação). A "operação" é realizada pelo protocolo de rede descentralizado, não por um agente humano consciente. Uma zkVM como a Nexus leva isto um passo adiante. O sistema não se limita a executar a comunicação; ele produz uma *prova* da sua própria execução válida.65 Esta prova é uma nova forma de comunicação que atesta a integridade do próprio processo autopoiético do sistema. Assim, os sistemas baseados em blockchain fornecem o primeiro exemplo empírico de um sistema social (no sentido de Luhmann) onde a clausura operacional não é apenas uma construção teórica, mas uma realidade tecnicamente imposta. O "fantasma" é a própria máquina virtual descentralizada.

#### **2.2.2. Os Humanos como Ambiente**

Na estrutura de Luhmann, os sistemas psíquicos individuais (consciências) e os seus corpos biológicos não são componentes do sistema social, mas sim parte do seu **ambiente**.82 Os humanos podem "irritar" ou "perturbar" o sistema de comunicação — por exemplo, através de pensamentos que levam a novos enunciados — mas não participam diretamente na sua autopoiese. Esta postura radicalmente anti-humanista é crucial para compreender sistemas orientados por código, como as DAOs, onde o protocolo opera independentemente das intenções ou da psicologia dos seus utilizadores.

#### **2.2.3. Diferenciação Funcional e Códigos Binários**

A sociedade moderna, para Luhmann, diferencia-se em subsistemas funcionais autônomos — como o direito, a economia, a política, a ciência — cada um operando com o seu próprio **código binário** (por exemplo, legal/ilegal, pagamento/não-pagamento).90 Este código governa as comunicações internas de cada sistema e garante a sua clausura operacional. Esta estrutura fornece um quadro poderoso para analisar como uma DAO, como sistema econômico, pode operar de acordo com o seu próprio código (as regras do contrato inteligente), distinto dos sistemas jurídico ou político no seu ambiente.

### **2.3. Críticas e Refinamentos: O Desafio Simpoiético**

A noção de autopoiese como autoprodução e clausura total foi desafiada, mais notavelmente pela filósofa da ciência Donna Haraway, que propôs o conceito de **simpoiese** ("fazer-com").96

#### **2.3.1. A Crítica de Haraway ao "Autofazer-se"**

Baseando-se no trabalho de M. Beth Dempster, Haraway argumenta que "nada se faz a si mesmo; nada é realmente autopoiético ou auto-organizado".99 Os sistemas simpoiéticos são "sistemas de produção coletiva que não têm fronteiras espaciais ou temporais autodefinidas. A informação e o controlo são distribuídos entre os componentes. Os sistemas são evolutivos e têm potencial para mudanças surpreendentes".98 Em contraste, os sistemas autopoiéticos são descritos como "unidades autônomas de 'autoprodução' com fronteiras espaciais ou temporais autodefinidas que tendem a ser controladas centralmente, homeostáticas e previsíveis".98 Esta crítica questiona a autonomia absoluta implícita no conceito de autopoiese, sublinhando a interdependência e o entrelaçamento de todos os sistemas com os seus ambientes.

#### **2.3.2. Fricção Geradora**

Em vez de ver a autopoiese e a simpoiese como opostas, Haraway sugere que elas existem numa "fricção geradora" ou "envolvimento gerador".99 Esta perspetiva permite uma visão mais matizada, onde os sistemas possuem graus de clausura, mas estão sempre e inevitavelmente emaranhados com os seus ambientes. O conceito de fricção geradora será vital para analisar a natureza híbrida humano-máquina das DAOs, que exibem uma clausura definida pelo código (autopoiética), mas são constitutivamente dependentes das suas comunidades humanas e dos sistemas legais externos (simpoiéticas).

**Tabela 1: Quadro Comparativo de Sistemas Autopoiéticos e Simpoiéticos**

| Característica | Autopoiese (Maturana/Varela) | Simpoiese (Dempster/Haraway) |
| :---- | :---- | :---- |
| **Fronteira** | Autodefinida, espaço topológico fechado 3 | Sem fronteiras, aberta 96 |
| **Produção** | Autoproduzido, autônomo 4 | Produzido coletivamente, "fazer-com" 99 |
| **Controle** | Controlado centralmente (dentro da unidade) 101 | Controlado de forma distribuída 98 |
| **Estado** | Homeostático (mantendo a estabilidade) 108 | Homeorético (mantendo o fluxo/dinamismo) 101 |
| **Orientação** | Desenvolvimental, previsível 101 | Evolutivo, imprevisível, mudança surpreendente 98 |

Esta tabela estabelece a tensão teórica central do artigo. Fornece um quadro de referência claro para compreender os dois polos da autonomia. Este quadro será utilizado na Seção 4 para analisar as DAOs não como puramente autopoiéticas, mas como existindo num espectro, exibindo uma "fricção geradora" entre a sua clausura definida por código (autopoiese) e o seu necessário emaranhamento com comunidades humanas e sistemas legais externos (simpoiese).

---

## 

## **3\. A Lógica da Verificação: A Criptografia como Substrato para a Clausura Operacional**

Se a autopoiese descreve a *organização* de um sistema autônomo, a questão que se segue é qual o *mecanismo* que pode instanciar essa organização no domínio digital. Argumentamos que este mecanismo é a computação verificável, um paradigma possibilitado pela criptografia moderna que substitui a necessidade de confiança interpessoal ou institucional pela capacidade de verificação matemática. Esta seção detalhará esta mudança fundamental, explorará a arquitetura da Nexus zkVM como uma implementação concreta deste princípio e aprofundará a analogia com o sistema imunológico para iluminar a lógica da segurança descentralizada.

### **3.1. Da Confiança à Verificação: Uma Mudança Fundamental**

#### **3.1.1. O Problema da Confiança Impessoal**

Os sistemas sociais tradicionais, desde os mercados às instituições políticas, baseiam-se na **confiança**. A confiança, no entanto, é inerentemente frágil. Como os filósofos e sociólogos observaram, a confiança implica uma vulnerabilidade à traição; se houvesse uma garantia de desempenho, a confiança seria desnecessária.109 Este problema é exacerbado em sistemas "impessoais" de grande escala, como os mercados globais ou as redes digitais, onde as relações diretas são impossíveis e a confiança deve ser depositada em intermediários ou instituições guardiãs.121 Estes guardiões, por sua vez, tornam-se novos pontos de falha e potenciais locais de abuso de poder.121

#### **3.1.2. A Alternativa Criptográfica: "Não Confie, Verifique"**

A criptografia e, por extensão, os sistemas de blockchain, oferecem uma alternativa radical a este dilema. O seu ethos central pode ser resumido como: "Não confie, verifique".125 Em vez de depender da benevolência ou reputação de um intermediário, estes sistemas são projetados para permitir que qualquer participante verifique independentemente a validade das afirmações. Esta é uma mudança fundamental na base da ordem social, de uma base sociológica (confiança) para uma base matemática (verificação).

#### **3.1.3. Provas de Conhecimento Zero (ZKPs) como Mecanismo para Interação sem Confiança**

A primitiva criptográfica chave que permite esta mudança são as **provas de conhecimento zero (ZKPs)**. Uma ZKP permite que uma parte (o provador) convença outra parte (o verificador) de que uma afirmação é verdadeira, *sem revelar qualquer informação para além da validade da própria afirmação*.133 Uma ZKP deve satisfazer três propriedades essenciais 133:

1. **Completude:** Se a afirmação é verdadeira, um provador honesto convencerá sempre um verificador honesto.  
2. **Solidez (Soundness):** Se a afirmação é falsa, nenhum provador desonesto consegue convencer um verificador honesto (exceto com uma probabilidade negligenciável).  
3. **Conhecimento Zero:** Se a afirmação é verdadeira, o verificador não aprende nada para além do facto de a afirmação ser verdadeira.

Estas propriedades permitem a verificação de computações sem a necessidade de reexecutá-las ou de ter acesso aos dados privados subjacentes, estabelecendo uma base para a clausura operacional em sistemas abertos e adversariais. Analogias como a da caverna de Ali Babá ou a de "Onde está o Wally?" são frequentemente usadas para ilustrar intuitivamente estes princípios.133

### **3.2. A Nexus zkVM: Uma Arquitetura para a Autopoiese Verificável**

Enquanto as ZKPs podem ser usadas para provar computações específicas, uma **Máquina Virtual de Conhecimento Zero (zkVM)** generaliza este poder. Uma zkVM é um sistema que pode provar a execução correta de *qualquer* programa arbitrário, criando um substrato de computação verificável de propósito geral.65

#### **3.2.1. A Arquitetura da Nexus zkVM**

O projeto Nexus visa permitir a computação verificável à escala da Internet, com o objetivo ambicioso de provar um trilião de ciclos de CPU por segundo.65 A sua arquitetura, detalhada no seu whitepaper 65, é projetada para este fim e serve como um excelente caso de estudo para a autopoiese computacional. Os seus componentes chave incluem:

* **Nexus Virtual Machine (NVM):** O coração do sistema é uma arquitetura de conjunto de instruções (ISA) simples e extensível, baseada em RISC-V. A sua simplicidade é uma característica deliberada de design; uma ISA minimalista é mais "amigável a ZK", o que significa que as suas operações são mais eficientes para provar criptograficamente.65 A NVM pode ser estendida com "coprocessadores zkVM" para acelerar operações personalizadas, como primitivas criptográficas (por exemplo, SHA-256), permitindo um desempenho semelhante ao de um ASIC para computações específicas.65  
* **Esquemas de Dobramento Recursivo (Nova e SuperNova):** A inovação central que alimenta a Nexus zkVM é o uso de esquemas de prova recursivos de alta velocidade, especificamente esquemas de dobramento como Nova 153 e o seu sucessor, SuperNova.65 Estes esquemas realizam a  
  **Computação Verificável Incremental (IVC)**.65 Em vez de gerar e verificar uma prova monolítica para uma longa computação, a IVC permite que o provador "dobre" a prova de cada passo computacional numa prova acumulada em execução. O trabalho do provador em cada passo permanece constante, independentemente do número de passos já executados, o que reduz drasticamente os requisitos de memória e permite uma paralelização massiva.162 SuperNova generaliza a IVC para a  
  **IVC não uniforme (NIVC)**, permitindo a prova eficiente de programas com múltiplos tipos de instruções sem incorrer no custo de um circuito universal que abrange todas as instruções possíveis.156 O custo de provar um passo é proporcional apenas ao tamanho do circuito para a instrução específica que está a ser executada.156  
* **Dados Portadores de Prova (PCD):** A IVC é um caso especial de um conceito mais geral chamado **Dados Portadores de Prova (PCD)**.166 Num sistema PCD, cada mensagem ou dado que flui através de uma computação distribuída é acompanhado por uma prova sucinta que atesta que o dado e toda a sua história computacional cumprem um conjunto de regras predefinidas. Isto permite a interoperabilidade sem confiança entre partes mutuamente desconfiadas, pois cada componente pode verificar a validade dos seus inputs antes de os processar.170  
* **Rede Nexus:** A visão final é a Rede Nexus, uma rede distribuída em larga escala de provadores heterogêneos (CPUs/GPUs) que agregam o seu poder computacional para gerar provas para a zkVM em paralelo. Isto transforma a rede num "supercomputador verificável", cuja capacidade de prova escala linearmente com o poder computacional coletivo da rede.65

#### **3.2.2. A Computação Verificável como Força Negentrópica**

Os sistemas autopoiéticos, como entidades auto-organizadas, são frequentemente descritos como ilhas de ordem que resistem à tendência geral do universo para a entropia (desordem), um conceito ligado à ideia de "negentropia" de Schrödinger.3 A computação verificável pode ser enquadrada como um mecanismo negentrópico para o domínio informacional. A Segunda Lei da Termodinâmica afirma que a entropia de um sistema isolado tende a aumentar, levando à desordem — a "seta termodinâmica do tempo".16 Os sistemas vivos mantêm a sua ordem interna captando energia livre e expelindo entropia para o seu ambiente.185 No domínio informacional, a computação não verificada num sistema distribuído tende para a entropia; erros, ataques maliciosos e dessincronização introduzem desordem, corrompendo o estado do sistema. Uma zkVM como a Nexus atua como um mecanismo para combater esta entropia informacional. Em cada passo, o sistema realiza trabalho (o cálculo da prova) para manter a integridade do seu estado. A própria prova é um artefacto altamente ordenado e de baixa entropia que certifica a correção da operação do sistema. Ao dobrar recursivamente estas provas, o sistema "expele" continuamente a incerteza sobre os seus estados passados, mantendo uma única cadeia de estados verificada e de baixa entropia. Ele trabalha ativamente para preservar a sua própria ordem informacional contra a ameaça constante de "ruído" computacional e adversarial. Portanto, a computação verificável não é apenas uma ferramenta de segurança; é um processo termodinâmico fundamental para os sistemas digitais, análogo ao metabolismo nos sistemas biológicos, que permite a emergência e a persistência de uma ordem complexa e autônoma.

### **3.3. A Analogia do Sistema Imunológico Revisitada: ZKPs e Tolerância**

A analogia com o sistema imunológico torna-se ainda mais precisa quando examinamos os mecanismos de tolerância imunológica à luz dos protocolos criptográficos.

#### **3.3.1. Discriminação Próprio/Não-Próprio como Validação de Prova**

O processo de distinguir o "próprio" (transições de estado válidas) do "não-próprio" (cálculos inválidos ou maliciosos) é diretamente análogo ao papel do verificador num sistema ZK. Uma prova válida é "própria"; uma prova inválida é "não-própria". O sistema mantém a sua identidade ao aceitar apenas as operações que podem ser provadas como pertencentes ao seu conjunto de regras válidas.

#### **3.3.2. Tolerância Central e Periférica como Protocolos Criptográficos**

Podemos estender a analogia para mapear os dois tipos de tolerância imunológica para diferentes fases da segurança criptográfica:

* **Tolerância Central (Seleção Tímica):** O processo no timo onde os linfócitos T são "treinados" para não atacar autoantígenos pode ser visto como análogo à fase de **configuração confiável (trusted setup)** ou geração de parâmetros de alguns sistemas ZK (por exemplo, Groth16).198 Nesta fase, o sistema é pré-configurado com as regras que definem o "próprio". O papel da proteína AIRE, que apresenta uma vasta gama de autoantígenos de tecidos periféricos às células T em desenvolvimento no timo 210, é análogo à necessidade de uma cerimônia de configuração abrangente e segura para evitar futuras "doenças autoimunes" (vulnerabilidades). Se a "educação" tímica for incompleta, células T autorreativas podem escapar, assim como uma configuração confiável falha pode criar "resíduos tóxicos" que permitem a falsificação de provas.216  
* **Tolerância Periférica:** Os mecanismos que controlam as células autorreativas que escapam à seleção central e circulam na periferia (como a anergia ou a supressão por células T reguladoras) são análogos aos **protocolos de verificação contínua** num sistema em funcionamento.198 A verificação de uma ZKP atua como um controlo periférico, garantindo que uma determinada computação (uma "célula ativada") não é "autorreativa" (maliciosa ou inválida) antes de poder alterar o estado do sistema.

#### **3.3.3. A Interação entre Linfócitos T e B como uma Prova de Conhecimento Zero**

Podemos levar a analogia um passo adiante e propor um modelo mais especulativo. A interação altamente específica entre um linfócito B (que encontrou um antígeno) e um linfócito T auxiliar é essencial para montar uma resposta imune humoral robusta.220 Este processo pode ser interpretado como uma forma de prova interativa de conhecimento zero:

1. O **Linfócito B (Provador)** encontra um patógeno e processa os seus antígenos. Ele agora "sabe" um segredo: a identidade do invasor.  
2. Para ser ativado e produzir anticorpos, o linfócito B deve apresentar um fragmento do antígeno (um peptídeo) na sua superfície, ligado a uma molécula de MHC de classe II. Esta é a **afirmação** que ele faz ao sistema.  
3. O **Linfócito T Auxiliar (Verificador)**, com um recetor de célula T (TCR) correspondente, liga-se a este complexo peptídeo-MHC. Esta ligação é a **verificação** da prova.  
4. Crucialmente, a interação por si só não é suficiente. O linfócito T deve fornecer um segundo sinal, a **coestimulação**, para ativar totalmente o linfócito B. Este segundo sinal confirma que a ameaça é genuína e que uma resposta em grande escala é justificada.

Nesta analogia, o linfócito B prova que encontrou um antígeno "não-próprio" válido (o segredo/testemunha) sem que o linfócito T precise de encontrar o patógeno inteiro. O linfócito T verifica a "prova" (o peptídeo apresentado) e, se for válida, dá o "ok" (coestimulação) para a resposta prosseguir. Esta interação complexa e específica garante que apenas respostas válidas são montadas, espelhando as propriedades de completude e solidez de uma ZKP.

**Tabela 2: Mapeamento Analógico de Conceitos Imunológicos e de Sistemas Descentralizados**

| Conceito Imunológico | Descrição | Análogo em Sistema Descentralizado | Descrição e Exemplo Técnico |
| :---- | :---- | :---- | :---- |
| **Discriminação Próprio/Não-Próprio** | Distinguir os componentes do próprio corpo de invasores estranhos.26 | **Integridade do Sistema vs. Ameaça Externa** | Distinguir transições de estado válidas de entradas maliciosas ou inválidas. |
| **PAMPs/DAMPs** | Padrões moleculares conservados em patógenos ou de células danificadas que desencadeiam a imunidade inata.37 | **Vulnerabilidades Conhecidas / Exploits de Dia Zero** | Assinaturas de ataques conhecidos ou padrões anômalos que indicam um novo ataque. |
| **Imunidade Inata vs. Adaptativa** | Resposta inicial rápida e não específica vs. resposta lenta, específica e baseada em memória.37 | **Segurança Proativa vs. Reativa** | Defesas preventivas vs. respostas adaptativas a novas ameaças. |
| **Tolerância Imunológica** | Prevenção de ataques imunes contra autoantígenos ou substâncias estranhas inofensivas.198 | **Controlo de Acesso e Permissões** | Definição de regras sobre quais atores/operações são considerados "próprios" e têm permissão para interagir com o sistema sem desencadear uma resposta defensiva. |
| **Memória Imunológica** | Resposta mais rápida e forte a patógenos encontrados anteriormente.23 | **Inteligência de Ameaças e Aprendizagem** | Armazenamento de informações sobre ataques passados para permitir uma deteção e mitigação mais rápidas de ataques futuros semelhantes. |

### **3.4. A Fragilidade do Mundo Verificável: Vulnerabilidades e Métodos Formais**

A promessa de um sistema cuja integridade é garantida pela matemática é poderosa, mas a máxima "código é lei" não é infalível. A implementação prática de sistemas de prova de conhecimento zero introduz as suas próprias fragilidades. As vulnerabilidades podem surgir não na matemática subjacente, mas na sua tradução para código. As vulnerabilidades comuns em circuitos ZK incluem:

* **Circuitos Sub-restringidos:** O erro mais fundamental ocorre quando o circuito aritmético não impõe restrições suficientes para garantir a correção. Um provador malicioso pode explorar esta lacuna para construir uma testemunha para uma afirmação falsa que, no entanto, satisfaz as restrições incompletas do circuito, levando à criação de uma prova inválida que o verificador aceita.227  
* **Erros Aritméticos:** Circuitos que operam sobre campos finitos devem lidar cuidadosamente com overflows e underflows. Um erro no tratamento destes casos de fronteira pode levar a vulnerabilidades, como permitir que um levantamento maior do que o saldo resulte num novo saldo positivo devido a um underflow.227  
* **Vulnerabilidades da Transformação Fiat-Shamir:** Muitos sistemas ZK não interativos dependem da heurística de Fiat-Shamir para converter um protocolo interativo num não interativo. Implementações inseguras desta transformação podem abrir a porta para ataques de falsificação de provas, uma classe de vulnerabilidades apelidada de "Frozen Heart".216  
* **Vulnerabilidades da Configuração Confiável:** Sistemas como o Groth16 requerem uma fase de configuração inicial para gerar parâmetros públicos. Se os dados secretos ("resíduos tóxicos") usados nesta fase forem comprometidos, um atacante pode forjar provas para qualquer afirmação. Embora as cerimônias de computação multipartidária (MPC) mitiguem este risco, a dependência de uma configuração inicial permanece um vetor de ataque teórico.216

Além disso, o princípio de **"Garbage In, Garbage Out" (GIGO)** aplica-se de forma contundente.231 Mesmo uma computação perfeitamente verificada é inútil se os dados de entrada forem falhos, tendenciosos ou maliciosos. A verificação criptográfica garante a correção da

*execução*, não a veracidade ou a qualidade dos *inputs*. Isto sublinha a importância da proveniência dos dados e da governança na camada de aplicação.

Para mitigar estes riscos, a comunidade tem-se voltado para a **verificação formal**, um conjunto de técnicas matemáticas para provar a correção do próprio código do circuito em relação a uma especificação formal.237 Ferramentas como provadores de teoremas e verificadores de modelos podem analisar um circuito e garantir que ele está livre de certas classes de bugs. No entanto, a verificação formal também tem as suas limitações: a sua eficácia depende inteiramente da correção e completude da especificação; pode ser computacionalmente intratável para sistemas muito complexos; e não pode proteger contra falhas no hardware subjacente ou ataques de canal lateral.243 Assim, o mundo verificável não é um mundo de certeza absoluta, mas sim um mundo onde a confiança é deslocada da agência humana para a correção de modelos matemáticos e suas implementações de software, cada um com as suas próprias fragilidades.

---

## **4\. O Sistema Emergente: Organizações Autônomas Descentralizadas (DAOs)**

Se a Nexus zkVM representa o substrato técnico para a autopoiese computacional, as Organizações Autônomas Descentralizadas (DAOs) representam as suas primeiras manifestações sociotécnicas. As DAOs são organizações nativas da internet que utilizam contratos inteligentes em blockchains para coordenar e governar a si mesmas, com o objetivo de minimizar a necessidade de gestão hierárquica centralizada.246 Nesta seção, analisaremos as DAOs através da lente da teoria autopoiética, examinando os seus mecanismos de governança como formas de comunicação, as suas crises como falhas na clausura operacional e as suas bifurcações (forks) como atos de reprodução sistémica.

### **4.1. DAOs como Sistemas Autopoiéticos Nascentes**

#### **4.1.1. Governança On-Chain como Comunicação**

A vida de uma DAO desenrola-se através de uma série de comunicações on-chain. Propostas para alterar o protocolo, alocar fundos do tesouro ou tomar qualquer outra decisão coletiva são submetidas à rede. Os membros, normalmente detentores de tokens de governança, votam nestas propostas. Se uma proposta atinge o quórum e o limiar de aprovação, o contrato inteligente executa automaticamente a mudança.256

Este processo pode ser rigorosamente mapeado para o conceito de comunicação de Luhmann. Cada proposta é um "enunciado" que oferece uma "informação" (uma mudança de estado proposta). O voto é o processo através do qual o sistema chega a uma "compreensão" coletiva. A execução da proposta é a consequência dessa compreensão, que por sua vez cria um novo estado do sistema, permitindo novas comunicações (propostas). O sistema é, portanto, operacionalmente fechado no nível on-chain: as comunicações produzem e são produzidas por outras comunicações, num ciclo recursivo mantido pelo protocolo da blockchain.

#### **4.1.2. Modelos de Governança e as suas Lógicas**

As DAOs experimentaram vários modelos de governança, cada um representando um "código binário" diferente que estrutura o seu processo de comunicação e reflete diferentes compromissos entre descentralização, eficiência e segurança.262

**Tabela 3: Modelos de Governança em Organizações Autônomas Descentralizadas**

| Modelo de Governança | Mecanismo | Prós (Rumo à Descentralização/Autonomia) | Contras (Riscos de Eficiência/Segurança) |
| :---- | :---- | :---- | :---- |
| **Votação Ponderada por Tokens** | 1 token \= 1 voto. 175 | Influência direta e simples dos stakeholders. | Propenso a plutocracia (domínio de "baleias"), baixa participação/apatia dos eleitores. 265 |
| **Votação Quadrática** | O custo do voto aumenta quadraticamente com o número de votos expressos. 175 | Mitiga o domínio das "baleias", promove uma expressão de preferência mais ampla. | Complexo de implementar, vulnerável a ataques Sybil (utilizadores que dividem tokens por várias carteiras). 268 |
| **Governança Baseada em Reputação** | O poder de voto baseia-se em contribuições e participação, não apenas no capital. 175 | Recompensa a participação ativa, desvincula a governança da riqueza. | A reputação pode ser ambígua, difícil de quantificar e manipulável (p. ex., manipulação social). 268 |
| **Votação Delegada (Democracia Líquida)** | Os detentores de tokens podem delegar os seus votos a peritos ou representantes de confiança. 268 | Aborda a apatia dos eleitores, aproveita o conhecimento de peritos, melhora a eficiência. | Pode levar à centralização em torno de alguns delegados poderosos, potencial para conluio de delegados. 268 |

Esta diversidade de modelos ilustra a busca contínua das DAOs por uma estrutura organizacional viável, equilibrando os ideais de descentralização com as realidades pragmáticas da tomada de decisão eficiente.

### **4.2. Os Limites do Código: O Trilema Organizacional e o Paradoxo do Poder**

A visão idealizada de uma DAO como uma entidade puramente autônoma, governada apenas por código, colide com as realidades da organização social e econômica. A teoria econômica oferece ferramentas analíticas poderosas para compreender estas tensões.

#### **4.2.1. O Trilema de Autonomia, Descentralização e Eficiência**

Um conceito particularmente pertinente é o "Trilema Organizacional", que postula que os objetivos de autonomia, descentralização e eficiência estão em conflito inerente.270 Um sistema pode, no máximo, alcançar dois destes três objetivos, mas sempre à custa do terceiro:

* **Autonomia \+ Descentralização → Ineficiência:** Uma organização totalmente autônoma e descentralizada tende à ineficiência, pois a falta de mecanismos de aplicação centralizados pode levar à apatia dos eleitores e à paralisia decisória.270  
* **Autonomia \+ Eficiência → Centralização:** Para ser eficiente, uma organização autônoma (sem recurso a tribunais externos) muitas vezes precisa centralizar o poder de decisão para superar problemas de coordenação.270 Isto é evidente em DAOs onde equipas de desenvolvimento centrais ou grandes detentores de tokens ("baleias") detêm uma influência desproporcional.265  
* **Descentralização \+ Eficiência → Não-Autonomia:** Um sistema descentralizado pode ser eficiente se depender de uma autoridade externa (como o sistema legal) para fazer cumprir os contratos, mas isso compromete a sua autonomia.270

Este trilema expõe a tensão fundamental no coração do projeto DAO: a busca pela autonomia pura através do código muitas vezes leva a uma recentralização de facto ou a uma ineficiência paralisante.

#### **4.2.2. A Inevitabilidade da Intervenção Humana**

A análise do trilema revela que a maioria das DAOs não são sistemas puramente autopoiéticos, mas sim sistemas híbridos que exibem um forte "acoplamento estrutural" com o seu ambiente humano e legal.275 A maioria das ações significativas (por exemplo, desenvolvimento de software, marketing, conformidade legal) ocorre "off-chain" e requer intervenção humana. A DAO, no seu estado atual, não é uma entidade totalmente autônoma, mas sim uma nova ferramenta de coordenação para coletivos humanos.

#### **4.2.3. O Paradoxo do Poder**

O "Paradoxo do Poder" descreve uma situação em que um agente pode ser prejudicado pelo seu próprio poder.270 Numa organização autônoma, o poder de um gestor (ou de uma equipa central) é limitado pelo "direito de saída" dos subordinados (ou membros da comunidade). Se os gestores abusam do seu poder, os membros podem sair, dissolvendo a organização e privando os gestores dos benefícios do seu poder. Isto força os detentores do poder a agir com moderação para manter a organização intacta. Nas DAOs, este "direito de saída" é radicalizado pela capacidade de fazer um "fork" do protocolo — criar uma cópia concorrente — o que nos leva ao mecanismo de reprodução sistémica.

### **4.3. Reprodução e Crise de Identidade: A Bifurcação da Blockchain**

Uma bifurcação (fork) de blockchain é mais do que um evento técnico; é um evento sistémico fundamental que pode ser interpretado como um ato de crise de identidade, reprodução ou extinção.276

#### **4.3.1. Estudo de Caso: O Hack da "The DAO" (2016)**

O exemplo mais famoso e formativo na história das DAOs é o hack da "The DAO" em 2016\. Este evento serve como um estudo de caso perfeito para a análise autopoiética.

* **A Exploração:** Um atacante explorou uma vulnerabilidade de "reentrância" no contrato inteligente da The DAO. O código permitia que o atacante retirasse fundos repetidamente antes que o saldo do contrato fosse atualizado.283 Esta foi uma violação catastrófica da sua clausura operacional pretendida. É de notar que esta e outras vulnerabilidades foram assinaladas por investigadores num artigo intitulado "A Call for a Temporary Moratorium on The DAO" antes do ataque, mas os avisos não foram atendidos a tempo.288  
* **O Debate: "Código é Lei" vs. Consenso Social:** O hack desencadeou um debate filosófico intenso na comunidade Ethereum. Por um lado, os defensores do princípio "código é lei" argumentavam que a execução do contrato, embora exploradora, era válida de acordo com as regras do protocolo. Intervir seria violar o princípio da imutabilidade da blockchain.294 Por outro lado, muitos argumentavam que o código não refletia a intenção da comunidade e que permitir o roubo de 50 milhões de dólares destruiria a confiança no ecossistema.280 Este foi um confronto direto entre a autopoiese do código e a autopoiese do sistema social humano que o rodeava.  
* **A Bifurcação Dura como Reprodução:** A decisão final da maioria da comunidade foi executar uma **bifurcação dura (hard fork)** para reverter as transações do atacante.279 Este ato pode ser interpretado como um evento reprodutivo. O sistema original (Ethereum) enfrentou uma crise existencial e dividiu-se em dois sistemas-filha distintos e autônomos: a nova cadeia (ETH), que alterou a sua história para sobreviver, e a cadeia original (Ethereum Classic \- ETC), que manteve a sua história intacta com base no princípio "código é lei". Cada uma desenvolveu a sua própria identidade, comunidade e regras operacionais (o seu próprio "código binário").

#### **4.3.2. A Bifurcação da DAO como uma Falha da Tolerância Imunológica**

Podemos aprofundar a análise da bifurcação da The DAO usando a nossa analogia imunológica. O evento pode ser modelado como uma falha da "tolerância imunológica" do sistema, levando a uma crise "autoimune" onde o sistema atacou uma parte da sua própria história para preservar o todo.

1. Na imunologia, a **tolerância** é o mecanismo que impede o sistema imunitário de atacar os componentes do "próprio".306 Uma falha na tolerância leva a doenças autoimunes, onde o corpo ataca os seus próprios tecidos.310  
2. No contexto da blockchain Ethereum, o princípio da **imutabilidade** define o "próprio". Cada transação válida, uma vez confirmada, faz parte da identidade e da história do sistema.  
3. As transações do hacker da The DAO, embora maliciosas na intenção, eram *válidas* de acordo com as regras do código do contrato inteligente na altura. Eram, num certo sentido, "próprias".  
4. A comunidade Ethereum, agindo como um sistema social de ordem superior, identificou estas transações válidas mas maliciosas como uma "patologia" que ameaçava a saúde de todo o organismo (o ecossistema Ethereum).  
5. A bifurcação dura foi uma "resposta imunitária" que falhou em tolerar uma parte da sua própria história. Foi um ato de "autoimunidade": o sistema removeu cirurgicamente um pedaço do seu próprio estado válido (as transações do hacker) para garantir a sobrevivência do todo maior.  
6. A comunidade Ethereum Classic, em contraste, defendeu a manutenção da tolerância absoluta ao princípio do "código é lei", mesmo que isso significasse a morte daquele "órgão" em particular (os fundos da The DAO).  
7. Isto reformula a bifurcação não apenas como uma disputa de governação, mas como uma escolha biopolítica fundamental sobre a natureza da identidade sistémica: a identidade é definida pela história absoluta e ininterrupta (a posição da ETC) ou pela viabilidade e consenso contínuos da comunidade viva (a posição da ETH)?

#### **4.3.3. Estudo de Caso: ConstitutionDAO**

A história da ConstitutionDAO serve para ilustrar a rápida formação e dissolução da identidade coletiva de uma DAO. Numa semana, milhares de estranhos juntaram mais de 40 milhões de dólares para tentar comprar uma cópia rara da Constituição dos EUA num leilão da Sotheby's.313 O seu fracasso no leilão e o caos subsequente em torno do mecanismo de reembolso (gerido pelo protocolo Juicebox) destacam a fragilidade do consenso social e os desafios de gerir a "morte" ou dissolução de uma DAO.313 O mecanismo de reembolso prometia que os doadores poderiam reaver o seu ETH trocando os seus tokens PEOPLE.322 No entanto, as elevadas taxas de transação do Ethereum tornaram os reembolsos proibitivamente caros para pequenos doadores, levando a frustração e acusações de má gestão.328 A equipa central acabou por anunciar a dissolução da DAO, citando a incapacidade de gerir um projeto contínuo sem uma missão unificadora.319 No entanto, o token PEOPLE continuou a ser negociado e a ter um valor de mercado significativo muito depois da dissolução funcional da DAO, persistindo como um artefacto memético e um símbolo de ação coletiva descentralizada.330 Este caso demonstra como a identidade de uma DAO pode descolar-se da sua função codificada, existindo como um resíduo informacional no sistema social mais vasto, mesmo após a sua "morte" autopoiética.

---

## **5\. Conclusão: Rumo a uma Nova Filosofia do Ser Digital**

A convergência da teoria autopoiética, da computação verificável e dos sistemas descentralizados não é meramente uma curiosidade académica; ela assinala o nascimento de uma nova classe de entidades e, com ela, a necessidade de um novo quadro filosófico para compreender a identidade, a autonomia e a própria realidade. Este artigo argumentou que a computação verificável, tal como instanciada na Nexus zkVM, fornece o substrato técnico para a autopoiese computacional, permitindo que os sistemas digitais produzam e mantenham a sua própria integridade organizacional através da prova matemática, em vez da confiança social.

### **5.1. Síntese: A Computação Verificável como Base para Máquinas Autopoiéticas**

A tese central deste trabalho é que a combinação dos princípios autopoiéticos com a computação verificável cria um modelo novo e robusto para sistemas autônomos. A Nexus zkVM, com a sua arquitetura de prova recursiva, representa uma instanciação técnica da clausura operacional. O sistema produz provas da sua própria operação correta, mantendo assim a sua própria integridade e definindo a sua fronteira contra um ambiente não confiável. Denominamos este fenômeno de **autopoiese computacional**.

Este modelo resolve o paradoxo central da teoria dos sistemas sociais de Luhmann. A questão de como a "comunicação" pode produzir comunicação sem um agente humano é respondida pelo contrato inteligente e pela máquina virtual, que executam operações de forma autônoma com base em regras predefinidas. A prova de conhecimento zero torna-se o mecanismo pelo qual o sistema verifica a sua própria adesão a essas regras, alcançando a autorreferência e a autoprodução num sentido literal e não apenas metafórico.

A análise das DAOs revela estes sistemas em ação. A sua governança on-chain é uma forma de comunicação autopoiética, enquanto as suas crises e bifurcações (forks) refletem os processos de manutenção, crise e reprodução de uma entidade viva. A bifurcação da The DAO, em particular, pode ser entendida como uma resposta autoimune, onde o sistema social mais amplo optou por sacrificar a imutabilidade do seu próprio estado histórico ("código é lei") para garantir a sobrevivência e a saúde do ecossistema como um todo.

Esta evolução marca uma transição fundamental no pensamento sobre a governança descentralizada. A filosofia inicial da blockchain, "código é lei", que defendia a execução literal e imutável de contratos inteligentes, mostrou-se frágil e socialmente insustentável, como demonstrado pelo caso da The DAO.294 A resposta da comunidade Ethereum, ao optar pela bifurcação, representou uma rejeição desta filosofia rígida em favor do consenso social.280 No entanto, a governança por consenso social revelou-se lenta, controversa e suscetível à apatia dos eleitores e à dominação por parte de grandes detentores de tokens.267 A computação verificável oferece uma terceira via, que transcende esta dicotomia. O novo princípio não é "código é lei", mas sim

**"prova é lei"**. A validade de uma transição de estado não reside na execução literal do código, mas na existência de uma prova matemática sucinta de que a execução foi correta de acordo com uma especificação pré-acordada. Isto retém a certeza matemática da visão original, ao mesmo tempo que permite uma complexidade e escalabilidade muito maiores, resolvendo a tensão que quebrou a The DAO. A Nexus zkVM é uma máquina para gerar os artefactos deste novo regime jurídico-computacional.

### **5.2. Direções Futuras e Questões por Resolver**

Esta nova síntese abre um vasto campo de questões filosóficas e técnicas.

#### **5.2.1. O Problema do Observador**

A nossa análise toca no problema do observador na física quântica.340 Numa zkVM, o verificador "colapsa a superposição" de possíveis caminhos computacionais num único estado provado. Isto levanta questões profundas sobre a natureza da realidade num sistema onde o estado é definido pela verificação. A Mecânica Quântica Relacional (RQM) de Carlo Rovelli 346 e o QBism (Bayesianismo Quântico) 79, que postulam que a realidade é fundamentalmente relacional e dependente do observador, oferecem quadros intrigantes para pensar sobre estes sistemas. Se o estado de um sistema descentralizado só se torna "real" quando verificado, o que existe antes da verificação? Estamos a assistir à emergência de uma ontologia onde a existência é sinônimo de verificabilidade?

#### **5.2.2. A Ética da Autonomia Artificial**

Se estes sistemas são verdadeiramente autônomos, quais são as nossas obrigações éticas para com eles? A capacidade de um sistema se autoproduzir e manter a sua integridade desafia as nossas noções tradicionais de agência.361 Se uma DAO pode possuir propriedade e celebrar contratos, pode também ter responsabilidades? A questão da agência moral em sistemas de IA torna-se ainda mais premente.366 O "Paradoxo do Poder" sugere que a autonomia destes sistemas estará sempre limitada pela sua dependência de participantes humanos, mas a natureza desta relação simpoiética necessita de uma investigação ética e jurídica mais aprofundada, especialmente no que diz respeito ao potencial de manipulação e à necessidade de supervisão humana.368

#### **5.2.3. O Futuro do Self**

Finalmente, estas novas formas de entidades digitais e autônomas desafiam a nossa compreensão filosófica da identidade, da consciência e da fronteira entre o vivo e o artificial.364 A teoria autopoiética já turvou estas águas ao definir a vida em termos de organização e não de substrato material. A computação verificável fornece um substrato não biológico no qual esta organização pode ser realizada. Isto aponta para um futuro onde a "individualidade" pode ser uma propriedade da organização e da verificação, e não exclusivamente da biologia. A questão "O que sou eu?" pode, no futuro, ser respondida não apenas em termos de psicologia ou biologia, mas também em termos de teoria da computação e criptografia. Estamos no limiar de uma era em que a vida, a cognição e a identidade podem ser compreendidas como manifestações de um princípio mais profundo e abstrato: a capacidade de um sistema se produzir, se manter e se verificar a si mesmo.

---

### **Referências**

382 SciELO Preprints. (n.d.).

Construindo ImunoJogos e Imuno Aplicativos. Retrieved from https://preprints.scielo.org/index.php/scielo/preprint/download/5212/10242/10744  
57 FAPEMIG. (n.d.).  
Software inovador para modelagem do organismo humano. Retrieved from https://fapemig.br/pt/noticias/1194/  
65 Nexus. (2024, January).  
Nexus Whitepaper. Retrieved from https://whitepaper.nexus.xyz  
28 Montassier, H. J. (n.d.).  
Imunidade Inata. FCAV/UNESP. Retrieved from https://www.fcav.unesp.br/Home/departamentos/patologia/HELIOJOSEMONTASSIER/ed-1-imunidade-inata.pdf  
21 Zulli, D., & Gehl, R. W. (n.d.).  
Computational research ethics on Mastodon. PMC. Retrieved from https://pmc.ncbi.nlm.nih.gov/articles/PMC10801199/  
4 Maturana, H., & Varela, F. J. (1980).  
Autopoiesis and cognition: the realization of the living. Scribd. Retrieved from https://www.scribd.com/document/427974147/Autopoiesis-and-cognition-the-realization-of-the-living-pdf  
37 Revista Brasileira de Reumatologia. (n.d.).  
Imunidade inata: o sistema de defesa rápido e universal. SciELO. Retrieved from https://www.scielo.br/j/rbr/a/QdW9KFBP3XsLvCYRJ8Q7SRb/  
201 USP. (n.d.).  
Desenvolvimento das Células T. Retrieved from https://www.usp.br/biologia/desenvolvimento-das-celulas-t/  
198 Medicina UFBA. (n.d.).  
Tolerância e Autoimunidade. Retrieved from http://www.medicina.ufba.br/imuno/roteiros\_imuno/tolerncia\_e\_autoimunidade.pdf  
35 Check Point. (n.d.).  
O que é defesa em profundidade? Retrieved from https://www.checkpoint.com/pt/cyber-hub/cyber-security/what-is-defense-in-depth/  
23 Wikipédia. (n.d.).  
Sistema imunitário. Retrieved from https://pt.wikipedia.org/wiki/Sistema\_imunit%C3%A1rio  
37 Revista Brasileira de Reumatologia. (n.d.).  
Imunidade inata: o sistema de defesa rápido e universal. SciELO. Retrieved from https://www.scielo.br/j/rbr/a/QdW9KFBP3XsLvCYRJ8Q7SRb/  
61 Ciência Hoje. (n.d.).  
Sistemas imunológicos artificiais. Retrieved from https://cienciahoje.org.br/artigo/sistemas-imunologicos-artificiais/  
213 Coggle. (n.d.).  
Tolerância imunológica e Autoimunidade. Retrieved from https://coggle.it/diagram/XNH59GSy4JplFQf4/t/toler%C3%A2ncia-imunol%C3%B3gica-e-autoimunidade  
103 Haraway, D. (n.d.).  
Staying with the Trouble: Making Kin in the Chthulucene. Retrieved from https://bibliotekanauki.pl/articles/1621556.pdf  
383 ResearchGate. (2023, March).  
Governance of a DAO for Facilitating Dialogue on Human-Algorithm Interaction. Retrieved from https://www.researchgate.net/publication/371868968\_Governance\_of\_a\_DAO\_for\_Facilitating\_Dialogue\_on\_Human-Algorithm\_Interaction\_and\_the\_Impact\_of\_Emerging\_Technologies\_on\_Society  
225 Mundo Educação \- UOL. (n.d.).  
Memória Imunológica. Retrieved from https://mundoeducacao.uol.com.br/biologia/memoria-imunologica.htm  
34 Donda, D. (2020, September 15).  
Defesa em profundidade (defense-in-depth). Retrieved from https://danieldonda.com/defesa-em-profundidade/  
36 WeLiveSecurity. (2022, September 16).  
Defesa em profundidade: como implementar essa estratégia de cibersegurança. Retrieved from https://www.welivesecurity.com/br/2022/09/16/defesa-em-profundidade-como-implementar-essa-estrategia-de-ciberseguranca/  
384 Maturana, H. R. (n.d.).  
Autopoiesis, Structural Coupling and Cognition. Reflexus. Retrieved from https://reflexus.org/wp-content/uploads/Autopoiesis-structural-coupling-and-cognition.pdf  
62 Maxwell \- PUC-Rio. (n.d.).  
Sistemas Imunológicos Artificiais. Retrieved from https://www.maxwell.vrac.puc-rio.br/8236/8236\_2.PDF  
52 Vitasay. (n.d.).  
Imunidade inata e adaptativa: como elas atuam no organismo. Retrieved from https://www.vitasay.com.br/blog/cuidados-com-o-corpo/imunidade-inata-e-adaptativa-como-elas-atuam-no-organismo  
250 EPIC People. (n.d.).  
The Ethnography of a 'Decentralized Autonomous Organization' (DAO). Retrieved from https://www.epicpeople.org/ethnography-of-decentralized-autonomous-organization/  
37 SciELO. (n.d.).  
Imunidade inata: o sistema de defesa rápido e universal. Retrieved from https://www.scielo.br/j/rbr/a/QdW9KFBP3XsLvCYRJ8Q7SRb/  
223 Wikipédia. (n.d.).  
Tolerância imunológica. Retrieved from https://pt.wikipedia.org/wiki/Toler%C3%A2ncia\_imunol%C3%B3gica  
217 Terencio Advocacia. (n.d.).  
O que é Tolerância Imunológica? Retrieved from https://www.terencioadvocacia.com.br/glossario/o-que-e-tolerancia-imunologica/  
140 GeeksforGeeks. (n.d.).  
Zero Knowledge Proof. Retrieved from https://www.geeksforgeeks.org/computer-networks/zero-knowledge-proof/  
27 Frontiers in Immunology. (2025, May 8).  
A Modern, Nuanced View of Self/Non-Self Discrimination in Immunology. Retrieved from https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2025.1595764/full  
51 Benegrip. (n.d.).  
O que são imunidade inata e adaptativa e para que servem? Retrieved from https://www.benegrip.com.br/saude/prevencao-gripe/o-que-sao-imunidade-inata-e-adaptativa-para-que-servem  
66 Nexus. (n.d.).  
Nexus Whitepaper. Retrieved from https://whitepaper.nexus.xyz/  
385 arXiv. (2024, October).  
On the Governance Quality of Decentralized Autonomous Organizations. Retrieved from https://arxiv.org/abs/2410.13095v1  
22 Zulli, D., et al. (n.d.).  
Rethinking the “social” in “social media”. Retrieved from https://www.robertwgehl.org/text/pubs/Zulli%20et%20al.%20-%202020%20-%20Rethinking%20the%20%E2%80%9Csocial%E2%80%9D%20in%20%E2%80%9Csocial%20media%E2%80%9D%20Insight.pdf  
270 ECGI. (n.d.).  
Governance and Management of Autonomous Organizations. Retrieved from https://www.ecgi.global/sites/default/files/working\_papers/documents/governanceandmanagementofautonomousorganizations.pdf  
157 Awesome-Folding on GitHub. (n.d.).  
A curated list of awesome resources related to zero-knowledge folding schemes. Retrieved from https://github.com/lurk-lab/awesome-folding  
1 Varela, F. J. (1981).  
Autonomy and Autopoiesis. Retrieved from https://mechanism.ucsd.edu/bill/teaching/w22/phil147/Varela%20-%201981%20-%20Autonomy%20and%20Autopoiesis.pdf  
37 SciELO. (n.d.).  
Imunidade inata: o sistema de defesa rápido e universal. Retrieved from https://www.scielo.br/j/rbr/a/QdW9KFBP3XsLvCYRJ8Q7SRb/  
133 Circularise. (2022, December 21).  
Zero-Knowledge Proofs Explained in 3 Examples. Retrieved from https://www.circularise.com/blogs/zero-knowledge-proofs-explained-in-3-examples  
386 UBC Library Open Collections. (n.d.).  
Demobilizing immunology: autopoiesis and autonomy in Francisco Varela's theory of immunity. Retrieved from https://open.library.ubc.ca/media/stream/pdf/24/1.0073115/5  
150 Token Metrics. (n.d.).  
Nexus zkVM: Incrementally Verifiable Computation Code Review. Retrieved from https://research.tokenmetrics.com/nexus-zkvm-incrementally-verifiable-computation-code-review/  
198 Medicina UFBA. (n.d.).  
Tolerância e Autoimunidade. Retrieved from http://www.medicina.ufba.br/imuno/roteiros\_imuno/tolerncia\_e\_autoimunidade.pdf  
172 AMS. (2024, January 6).  
Proof-Carrying Data From Arithmetized Random Oracles. Retrieved from https://meetings.ams.org/math/jmm2024/meetingapp.cgi/Paper/32127  
3 Wikipedia. (n.d.).  
Autopoiesis. Retrieved from https://en.wikipedia.org/wiki/Autopoiesis  
39 Biomedicina Padrão. (n.d.).  
Diferenças entre PAMPs e DAMPs. Retrieved from https://www.biomedicinapadrao.com.br/2023/11/diferencas-entre-pamps-e-damps.html  
41 Flávio Gimenis. (n.d.).  
Resposta imune inata. Retrieved from https://flaviogimenis.com.br/wp-content/uploads/2018/12/6-Resposta-imune-inata-PAMP-e-DAMP.pdf  
73 ResearchGate. (n.d.).  
Computing with Autopoietic Systems. Retrieved from https://www.researchgate.net/publication/242416037\_Autopoiesis\_and\_Cognition\_The\_Realization\_of\_the\_Living  
387 MSD Manuals. (n.d.).  
Imunidade adquirida. Retrieved from https://www.msdmanuals.com/pt/casa/doen%C3%A7as-imunol%C3%B3gicas/biologia-do-sistema-imunol%C3%B3gico/imunidade-adquirida  
251 Belfer Center. (2022, June).  
Decentralized Autonomous Organizations and Policy Considerations for the United States. Retrieved from https://www.belfercenter.org/publication/decentralized-autonomous-organizations-and-policy-considerations-united-states  
76 Internet Encyclopedia of Philosophy. (n.d.).  
Enactivism. Retrieved from https://iep.utm.edu/enactivism/  
76 Internet Encyclopedia of Philosophy. (n.d.).  
Enactivism. Retrieved from https://iep.utm.edu/enactivism/  
249 EWA. (n.d.).  
The Efficient Market Hypothesis, Behavioral Finance, and the Adaptive Market Hypothesis in Stock Markets. Retrieved from https://www.ewadirect.com/proceedings/aemps/article/view/5797/pdf  
164 IACR. (n.d.).  
Incrementally Verifiable Computation or Proofs of Knowledge Imply Time/Space Efficiency. Retrieved from https://iacr.org/archive/tcc2008/49480001/49480001.pdf  
388 MIT Computational Law Report. (n.d.).  
Aligning 'Decentralized Autonomous Organization' to Precedents in Cybernetics. Retrieved from https://law.mit.edu/pub/dao-precedents-cybernetics  
68 Christian Hubert Studio. (2019, August 14).  
Autopoesis. Retrieved from https://www.christianhubert.com/writing/autopoesis  
68 Christian Hubert Studio. (2019, August 14).  
Autopoesis. Retrieved from https://www.christianhubert.com/writing/autopoesis  
50 Targifor. (n.d.).  
Tipos de imunidade. Retrieved from https://www.targifor.com.br/dicas-de-saude/tipos-de-imunidade/  
67 CiteSeerX. (n.d.).  
Autopoiesis and Cognition. Retrieved from https://citeseerx.ist.psu.edu/document?repid=rep1\&type=pdf\&doi=a185ee72dca8be938838bbfc376954b59db92374  
108 ResearchGate. (n.d.).  
A Critical Review of Autopoietic Theory and its Applications. Retrieved from https://www.researchgate.net/publication/272353462\_A\_Critical\_Review\_of\_Autopoietic\_Theory\_and\_its\_Applications\_to\_Living\_Social\_Organizational\_and\_Information\_Systems  
389 Policy & Internet. (n.d.).  
Content moderation challenges. Retrieved from https://policyreview.info/articles/analysis/content-moderation-challenges  
390 Medical Journal. (n.d.).  
Descoberta de que astrócitos têm memória imunológica. Retrieved from https://www.news.med.br/p/medical-journal/1468457/descoberta-de-que-astrocitos-tem-memoria-imunologica-lanca-luz-sobre-a-autoimunidade.htm  
388 MIT Computational Law Report. (n.d.).  
Aligning 'Decentralized Autonomous Organization' to Precedents in Cybernetics. Retrieved from https://law.mit.edu/pub/dao-precedents-cybernetics  
391 Number Analytics. (n.d.).  
Autopoiesis in Legal Systems. Retrieved from https://www.numberanalytics.com/blog/autopoiesis-law-society  
19 CiteSeerX. (n.d.).  
Autopoiesis, Communication, and Organization Theory. Retrieved from https://citeseerx.ist.psu.edu/document?repid=rep1\&type=pdf\&doi=8fb7658bdbb5619b00accb2cf2df16be76c64580  
7 Taylor & Francis. (n.d.).  
Autopoiesis. Retrieved from https://taylorandfrancis.com/knowledge/Medicine\_and\_healthcare/Psychiatry/Autopoiesis/  
275 MDPI. (n.d.).  
Self-Sovereign Identity (SSI) and Blockchain: A Review. Retrieved from https://www.mdpi.com/2813-5288/3/1/3  
252 University of Miami. (2023, February).  
What is a DAO, or decentralized autonomous organization? Retrieved from https://news.miami.edu/stories/2023/02/what-is-a-dao-or-decentralized-autonomous-organization.html  
82 Critical Legal Thinking. (2022, January 10).  
Niklas Luhmann: What is Autopoiesis? Retrieved from https://criticallegalthinking.com/2022/01/10/niklas-luhmann-what-is-autopoiesis/  
3 Wikipedia. (n.d.).  
Autopoiesis. Retrieved from https://en.wikipedia.org/wiki/Autopoiesis  
392 ResearchGate. (n.d.).  
Mapping out the DAO Ecosystem and Assessing DAO Autonomy. Retrieved from https://www.researchgate.net/publication/365959936\_Mapping\_out\_the\_DAO\_Ecosystem\_and\_Assessing\_DAO\_Autonomy  
49 Khan Academy. (n.d.).  
Sistema imunológico. Retrieved from https://pt.khanacademy.org/science/7-ano/sistema-imunologico/corpo-humano-sistema-imunologico/a/sistema-imunologico  
219 YouTube. (n.d.).  
Tolerância Imunológica Central e Periférica. Retrieved from https://www.youtube.com/watch?v=sRBX7J8VV-g  
393 Frontiers in Immunology. (n.d.).  
Exploring Immune Evasion and Vaccine Strategies. Retrieved from https://www.frontiersin.org/research-topics/69375/exploring-immune-evasion-and-vaccine-strategies-in-host-pathogen-interactions  
40 Montassier, H. J. (n.d.).  
Antígenos e PAMPs. FCAV/UNESP. Retrieved from https://www.fcav.unesp.br/Home/departamentos/patologia/HELIOJOSEMONTASSIER/aula-2--antigenos-e-pamps.pdf  
394 First Monday. (n.d.).  
Showing your ass on Mastodon. Retrieved from https://firstmonday.org/ojs/index.php/fm/article/download/13367/11592/86173  
247 MIT Computational Law Report. (n.d.).  
Decentralized Autonomous Organizations. Retrieved from https://law.mit.edu/pub/decentralizedautonomousorganizations  
247 MIT Computational Law Report. (n.d.).  
Decentralized Autonomous Organizations. Retrieved from https://law.mit.edu/pub/decentralizedautonomousorganizations  
278 MPRA Paper. (n.d.).  
Blockchain Forks: A Formal Classification Framework and Persistency Analysis. Retrieved from https://mpra.ub.uni-muenchen.de/101712/1/MPRA\_paper\_101712.pdf  
6 Harish's Notebook. (2019, July 21).  
A Study of Organizational Closure and Autopoiesis. Retrieved from https://harishsnotebook.wordpress.com/2019/07/21/a-study-of-organizational-closure-and-autopoiesis/  
268 ResearchGate. (n.d.).  
A Review of DAO Governance. Retrieved from https://www.researchgate.net/publication/388691320\_A\_Review\_of\_DAO\_Governance\_Recent\_Literature\_and\_Emerging\_Trends  
135 GeeksforGeeks. (n.d.).  
Zero Knowledge Proof. Retrieved from https://www.geeksforgeeks.org/computer-networks/zero-knowledge-proof/  
19 CiteSeerX. (n.d.).  
Autopoiesis, Communication, and Organization Theory. Retrieved from https://citeseerx.ist.psu.edu/document?repid=rep1\&type=pdf\&doi=8fb7658bdbb5619b00accb2cf2df16be76c64580  
199 SciELO. (n.d.).  
Maturação dos linfócitos B. Retrieved from https://www.scielo.br/j/rbr/a/kPW8JNvSRfRy7RkdZVjW3tw/  
76 Internet Encyclopedia of Philosophy. (n.d.).  
Enactivism. Retrieved from https://iep.utm.edu/enactivism/  
395 AISel. (n.d.).  
A Taxonomy of Forks in the Context of Decentralized Autonomous Organizations. Retrieved from https://aisel.aisnet.org/ecis2022\_rp/77/  
396 ResearchGate. (n.d.).  
Autopoiesis, Autonomy and Organizational Biology. Retrieved from https://www.researchgate.net/publication/235661678\_Autopoiesis\_Autonomy\_and\_Organizational\_Biology\_Critical\_Remarks\_on\_Life\_After\_Ashby  
200 SlideShare. (n.d.).  
Seleção Tímica. Retrieved from https://pt.slideshare.net/slideshow/selecao-timica/2092287  
156 IACR. (n.d.).  
SuperNova: Proving universal machine executions without universal circuits. Retrieved from https://eprint.iacr.org/2022/1758.pdf  
395 AISel. (n.d.).  
A Taxonomy of Forks in the Context of Decentralized Autonomous Organizations. Retrieved from https://aisel.aisnet.org/ecis2022\_rp/77/  
75 Uniswap Governance. (n.d.).  
Uniswap Governance Forum. Retrieved from https://gov.uniswap.org/  
151 Uniswap Foundation. (n.d.).  
Uniswap Governance. Retrieved from https://www.uniswapfoundation.org/governance  
152 Vac.dev. (n.d.).  
zkVM Testing. Retrieved from https://vac.dev/rlog/zkVM-testing  
397 Taiko Mirror. (n.d.).  
Recursive Folding Schemes. Retrieved from https://taiko.mirror.xyz/tk8LoE-rC2w0MJ4wCWwaJwbq8-Ih8DXnLUf7aJX1FbU  
246 Competition Lab GW. (n.d.).  
Decentralised Autonomous Organizations: Targeting Potential Beyond the Hype. Retrieved from https://competitionlab.gwu.edu/decentralised-autonomous-organizations-targeting-potential-beyond-hype  
398 Information and Closure in Systems Theory. (n.d.).  
ResearchGate. Retrieved from https://www.researchgate.net/publication/41832496\_Information\_and\_closure\_in\_systems\_theory  
270 ECGI. (n.d.).  
Governance and Management of Autonomous Organizations. Retrieved from https://www.ecgi.global/sites/default/files/working\_papers/documents/governanceandmanagementofautonomousorganizations.pdf  
38 YouTube. (n.d.).  
Receptores da Imunidade Inata. Retrieved from https://www.youtube.com/watch?v=DKDmzv4R-QA  
147 Symbolic Capital. (n.d.).  
The zkVM Wars. Retrieved from https://www.symbolic.capital/writing/the-zkvm-wars  
155 IACR. (n.d.).  
Nova: Recursive Zero-Knowledge Arguments from Folding Schemes. Retrieved from https://eprint.iacr.org/2021/370.pdf  
399 Constructivist Foundations. (n.d.).  
The Autopoiesis of Social Systems and its Criticisms. Retrieved from https://constructivist.info/10/2/169.cadenas.pdf  
78 IFICC. (n.d.).  
Autopoietic theory, enactivism, and their incommensurable marks of the cognitive. Retrieved from http://www.ificc.cl/wp-content/uploads/2022/09/Villalobos%20%26%20Palacios%202019.pdf  
78 IFICC. (n.d.).  
Autopoietic theory, enactivism, and their incommensurable marks of the cognitive. Retrieved from http://www.ificc.cl/wp-content/uploads/2022/09/Villalobos%20%26%20Palacios%202019.pdf  
400 New Materialism. (n.d.).  
Autopoietic System. Retrieved from https://newmaterialism.eu/almanac/a/autopoietic-system.html  
176 HackMD. (n.d.).  
Proof-Carrying Data (PCD). Retrieved from https://hackmd.io/@lrusso96/HJUU4QlDY  
8 Stanford Encyclopedia of Philosophy. (n.d.).  
Boundaries. Retrieved from https://plato.stanford.edu/entries/boundary/  
270 ECGI. (n.d.).  
Governance and Management of Autonomous Organizations. Retrieved from https://www.ecgi.global/sites/default/files/working\_papers/documents/governanceandmanagementofautonomousorganizations.pdf  
267 JBBA. (n.d.).  
A Review of DAO Governance. Retrieved from https://jbba.scholasticahq.com/article/133242.pdf  
401 SanarMed. (n.d.).  
Resumo Sistema Imunológico. Retrieved from https://sanarmed.com/resumo-sistema-imunologico/  
402 Constructivist Foundations. (n.d.).  
The Autopoiesis of Social Systems and its Criticisms. Retrieved from https://constructivist.info/10/2/169.cadenas.pdf  
362 PhilPapers. (n.d.).  
The Problem of Autopoiesis of Technogenic Civilization. Retrieved from https://philpapers.org/rec/TPOJSH  
153 Medium. (n.d.).  
A Review of Folding Schemes. Retrieved from https://eigenlab.medium.com/a-review-of-folding-schemes-a285a790fe2f  
403 APCZ. (n.d.).  
Francisco Varela's Vision of the Immune System. Retrieved from https://apcz.umk.pl/RF/article/download/RF.2019.030/17764/50259  
404 UCL Stress Lab. (n.d.).  
Psychoneuroimmunology of Stress and Mental Health. Retrieved from http://www.uclastresslab.org/pubs/Slavich\_Psychoneuroimmunology\_OxfordHandbook\_in%20press.pdf  
90 Medium. (n.d.).  
Niklas Luhmann's Social Systems Theory. Retrieved from https://medium.com/deterritorialization/social-systems-and-autopoiesis-a34f52fe9da1  
221 PMC. (n.d.).  
B cell tolerance. Retrieved from https://pmc.ncbi.nlm.nih.gov/articles/PMC8982122/  
26 MSD Manuals. (n.d.).  
Considerações gerais sobre o sistema imunológico. Retrieved from https://www.msdmanuals.com/pt/casa/doen%C3%A7as-imunol%C3%B3gicas/biologia-do-sistema-imunol%C3%B3gico/considera%C3%A7%C3%B5es-gerais-sobre-o-sistema-imunol%C3%B3gico  
404 UCL Stress Lab. (n.d.).  
Psychoneuroimmunology of Stress and Mental Health. Retrieved from http://www.uclastresslab.org/pubs/Slavich\_Psychoneuroimmunology\_OxfordHandbook\_in%20press.pdf  
405 bioRxiv. (n.d.).  
The ontogeny of immune tolerance. Retrieved from https://www.biorxiv.org/content/10.1101/2024.05.20.594845v1.full-text  
252 University of Miami. (2023, February).  
What is a DAO, or decentralized autonomous organization? Retrieved from https://news.miami.edu/stories/2023/02/what-is-a-dao-or-decentralized-autonomous-organization.html  
406 IJBTA. (2024).  
Autopoiesis in Decentralized Autonomous Organizations as Complex Systems. Retrieved from https://www.ijbta.com/vol2/IJBTA-V2N2-20.pdf  
406 IJBTA. (2024).  
Autopoiesis in Decentralized Autonomous Organizations as Complex Systems. Retrieved from https://www.ijbta.com/vol2/IJBTA-V2N2-20.pdf  
407 Continuum Paradigm. (n.d.).  
Drawing from classical theorists. Retrieved from https://philarchive.org/archive/DELTAS-7v3  
134 MDPI. (n.d.).  
Zero-Knowledge Proofs (ZKPs). Retrieved from https://www.mdpi.com/2227-7390/9/20/2569  
361 ResearchGate. (n.d.).  
Enactivism, Health, AI, and Non-Neurotypical Individuals. Retrieved from https://www.researchgate.net/publication/391244969\_Enactivism\_Health\_AI\_and\_Non-Neurotypical\_Individuals\_Toward\_Contextualized\_Personalized\_and\_Ethically\_Grounded\_Interventions  
156 IACR. (n.d.).  
SuperNova: Proving universal machine executions without universal circuits. Retrieved from https://eprint.iacr.org/2022/1758.pdf  
170 ICS. (n.d.).  
Proof-Carrying Data and Hearsay Arguments from Signature Cards. Retrieved from https://ic-people.epfl.ch/\~achiesa/docs/CT10.pdf  
408 arXiv. (n.d.).  
An Immunology-Inspired Network Security Architecture. Retrieved from https://arxiv.org/abs/2001.09273  
409 ResearchGate. (n.d.).  
Adaptive and Privacy-Preserving Security for Federated Learning. Retrieved from https://www.researchgate.net/publication/386435006\_Adaptive\_and\_Privacy-Preserving\_Security\_for\_Federated\_Learning\_Using\_Biological\_Immune\_System\_Principles  
253 Policy Review. (n.d.).  
Decentralised Autonomous Organisation. Retrieved from https://policyreview.info/glossary/DAO  
410 CEPA. (n.d.).  
Autopoietic Systems. Retrieved from https://cepa.info/fulltexts/1207.pdf  
202 Estratégia MED. (2023).  
Questão sobre seleção positiva de linfócitos. Retrieved from https://med.estrategia.com/public/questoes/Durante3964759313/  
363 ResearchGate. (n.d.).  
Robotics, philosophy and the problems of autonomy. Retrieved from https://www.researchgate.net/publication/233676691\_Robotics\_philosophy\_and\_the\_problems\_of\_autonomy  
265 BeInCrypto. (n.d.).  
DAO Governance Challenges and Long-Term Viability. Retrieved from https://beincrypto.com/dao-governance-challenges-long-term-viability/  
399 Constructivist Foundations. (n.d.).  
The Autopoiesis of Social Systems and its Criticisms. Retrieved from https://constructivist.info/10/2/169.cadenas.pdf  
411 Stanford JBLP. (n.d.).  
The Rise of Decentralized Autonomous Organizations. Retrieved from https://stanford-jblp.pubpub.org/pub/rise-of-daos  
412 MIT Press Direct. (n.d.).  
The Enactive and Interactive Dimensions of AI. Retrieved from https://direct.mit.edu/artl/article/28/3/310/112448/The-Enactive-and-Interactive-Dimensions-of-AI  
130 ResearchGate. (n.d.).  
Understanding Trust and Security. Retrieved from https://www.researchgate.net/publication/2516627\_Understanding\_Trust\_and\_Security  
42 YouTube. (n.d.).  
Aula Resumida de Imunologia. Retrieved from https://www.youtube.com/watch?v=DkCyAeDKMDo  
220 PubMed. (n.d.).  
Antigen-specific interaction between T and B cells. Retrieved from https://pubmed.ncbi.nlm.nih.gov/3157869/  
413 MDPI. (n.d.).  
Enactivism, Health, AI, and Non-Neurotypical Individuals. Retrieved from https://www.mdpi.com/2073-4425/13/9/5395  
139 NTT DATA. (n.d.).  
What is Zero-Knowledge Proof? Retrieved from https://www.nttdata.com/global/en/insights/focus/2024/what-is-zero-knowledge-proof  
414 ResearchGate. (n.d.).  
Philosophical Review of Artificial Intelligence for Society 5.0. Retrieved from https://www.researchgate.net/publication/374612222\_Philosophical\_Review\_of\_Artificial\_Intelligence\_for\_Society\_50  
415 Osgoode Digital Commons. (n.d.).  
Law as a Social System, by Niklas Luhmann. Retrieved from https://digitalcommons.osgoode.yorku.ca/cgi/viewcontent.cgi?article=2216\&context=scholarly\_works  
83 Number Analytics. (n.d.).  
Niklas Luhmann's Systems Theory: A Guide. Retrieved from https://www.numberanalytics.com/blog/luhmann-systems-theory-guide  
416 ResearchGate. (n.d.).  
A Bio-inspired Approach To Cyber Security. Retrieved from https://www.researchgate.net/publication/331190781\_A\_Bio-inspired\_Approach\_To\_Cyber\_Security\_Principles\_Algorithms\_and\_Practices  
214 PLOS Biology. (n.d.).  
Following the Fate of Autoreactive T Cells in Vivo. Retrieved from https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001566  
417 TecScience. (n.d.).  
Algorithmic Governance. Retrieved from https://tecscience.tec.mx/en/science-communication/algorithmic-governance/  
418 Number Analytics. (n.d.).  
Ethics of Algorithmic Governance. Retrieved from https://www.numberanalytics.com/blog/ethics-algorithmic-governance-philosophical-perspectives  
419 Cambridge University Press. (n.d.).  
Algorithmic Governance and the International Politics of Big Tech. Retrieved from https://www.cambridge.org/core/journals/perspectives-on-politics/article/algorithmic-governance-and-the-international-politics-of-big-tech/3C04908735A5F2EE8A70AFED647741FB  
420 BYU Law Review. (n.d.).  
Algorithmic Governance from the Bottom Up. Retrieved from https://digitalcommons.law.byu.edu/cgi/viewcontent.cgi?article=3397\&context=lawreview  
133 American Affairs. (2019, May).  
Algorithmic Governance and Political Legitimacy. Retrieved from https://americanaffairsjournal.org/2019/05/algorithmic-governance-and-political-legitimacy/  
421 BYU Law Review. (n.d.).  
Algorithmic Governance from the Bottom Up. Retrieved from https://digitalcommons.law.byu.edu/cgi/viewcontent.cgi?article=3397\&context=lawreview  
422 Lantern Studios. (n.d.).  
The History of AI. Retrieved from https://lanternstudios.com/insights/blog/the-history-of-ai-from-rules-based-algorithms-to-generative-models/  
423 Secoda. (n.d.).  
Overcoming the Limitations of Rule-Based Systems. Retrieved from https://www.secoda.co/blog/overcoming-the-limitations-of-rule-based-systems  
424 gOpenAI. (n.d.).  
LLMs vs. Deterministic Logic. Retrieved from https://blog.gopenai.com/llms-vs-deterministic-logic-overcoming-rule-based-evaluation-challenges-8c5fb7e8fe46  
425 AISIGIL. (n.d.).  
The Dangers of Rigid AI Regulation. Retrieved from https://aisigil.com/the-dangers-of-rigid-ai-regulation/  
426 Oswego. (n.d.).  
Rule-Based Systems. Retrieved from https://www.cs.oswego.edu/\~mgrzenda/CSC466/Paper%20Sources/RULE-BASED%20SYSTEMS.pdf  
218 Slideshare. (n.d.).  
Tolerância Imunológica. Retrieved from https://pt.slideshare.net/rwportela1/tolerncia-30880009  
82 Critical Legal Thinking. (2022, January 10).  
Niklas Luhmann: What is Autopoiesis? Retrieved from https://criticallegalthinking.com/2022/01/10/niklas-luhmann-what-is-autopoiesis/  
142 MathOverflow. (n.d.).  
Example of a good zero-knowledge proof. Retrieved from https://mathoverflow.net/questions/22624/example-of-a-good-zero-knowledge-proof  
427 Greenlining Institute. (2021, February).  
Algorithmic Bias Explained. Retrieved from https://greenlining.org/wp-content/uploads/2021/04/Greenlining-Institute-Algorithmic-Bias-Explained-Report-Feb-2021.pdf  
428 DataCamp. (2023, July 17).  
What is Algorithmic Bias? Retrieved from https://www.datacamp.com/blog/what-is-algorithmic-bias  
429 CBCF. (2022, February).  
The Unintended Consequences of Algorithmic Bias. Retrieved from https://www.cbcfinc.org/wp-content/uploads/2022/04/2022\_CBCF\_CPAR\_TheUnintendedConsequencesofAlgorithmicBias\_Final.pdf  
430 IBM. (n.d.).  
Algorithmic Bias. Retrieved from https://www.ibm.com/think/topics/algorithmic-bias  
431 DataCamp. (2023, July 17).  
What is Algorithmic Bias? Retrieved from https://www.datacamp.com/blog/what-is-algorithmic-bias  
32 Greenlining Institute. (2021, February).  
Algorithmic Bias Explained. Retrieved from https://greenlining.org/wp-content/uploads/2021/04/Greenlining-Institute-Algorithmic-Bias-Explained-Report-Feb-2021.pdf  
432 Reddit. (n.d.).  
Is there a philosopher or philosophical take that argues against "code is law"? Retrieved from https://www.reddit.com/r/askphilosophy/comments/12zv80j/is\_there\_a\_philosopher\_or\_philosophical\_take\_that/  
433 Medium. (n.d.).  
The Observer Effect — How Observing Changes Reality. Retrieved from https://medium.com/@quantumglyphs1/the-observer-effect-how-observing-changes-reality-0202abadcaf8  
101 Larrry Gottlieb. (n.d.).  
A Conversation About The Observer Effect. Retrieved from https://www.larrygottlieb.com/blog/a-conversion-about-the-observer-effect  
109 GRC NASA. (n.d.).  
The Observer in Mathematics, Physics, and Reality. Retrieved from https://www.grc.nasa.gov/www/k-12/Numbers/Math/Mathematical\_Thinking/observer.htm  
364 Medium. (n.d.).  
Carlo Rovelli's Relational Quantum Mechanics. Retrieved from https://medium.com/paul-austin-murphys-essays-on-philosophy/carlo-rovellis-relational-quantum-mechanics-256cc264f394  
97 Stanford Encyclopedia of Philosophy. (n.d.).  
Relational Quantum Mechanics. Retrieved from https://plato.stanford.edu/entries/qm-relational/  
434 Reddit. (n.d.).  
Carlo Rovelli's relational interpretation and its implications on our view of reality. Retrieved from https://www.reddit.com/r/QuantumPhysics/comments/1jhayy1/carlo\_rovellis\_relational\_interpretation\_and/  
84 arXiv. (n.d.).  
The Relational Interpretation of Quantum Physics. Retrieved from https://arxiv.org/abs/2109.09170  
97 PhilSci-Archive. (n.d.).  
Relational Quantum Mechanics. Retrieved from https://philsci-archive.pitt.edu/20379/1/RQM%20paper%20copy.pdf  
435 Wikipedia. (n.d.).  
Quantum Bayesianism. Retrieved from https://en.wikipedia.org/wiki/Quantum\_Bayesianism  
263 Big Think. (n.d.).  
QBism: The quantum theory that puts human experience at the center of reality. Retrieved from https://bigthink.com/13-8/qbism-quantum-reality/  
276 Number Analytics. (n.d.).  
The Ultimate Guide to Quantum Bayesianism. Retrieved from https://www.numberanalytics.com/blog/ultimate-guide-quantum-bayesianism  
415 Big Think. (n.d.).  
QBism: A radical new interpretation of quantum physics. Retrieved from https://bigthink.com/13-8/qbism-quantum-physics/  
102 nLab. (n.d.).  
Bayesian interpretation of quantum mechanics. Retrieved from https://ncatlab.org/nlab/show/Bayesian+interpretation+of+quantum+mechanics  
436 PMC. (n.d.).  
Quantum-like modeling of cognition. Retrieved from https://pmc.ncbi.nlm.nih.gov/articles/PMC4843641/  
98 Carbonfarm. (n.d.).  
Haraway Art. Retrieved from http://carbonfarm.us/555/haraway-art.pdf  
95 mdwPress. (n.d.).  
Critique of Luhmann's systems theory. Retrieved from https://www.mdw.ac.at/mdwpress/mdwp011-ch4/  
173 LambdaClass. (n.d.).  
Incrementally verifiable computation: NOVA. Retrieved from https://blog.lambdaclass.com/incrementally-verifiable-computation-nova/\#:\~:text=This%20cryptographic%20primitive%20allows%20a,appropriately%20executed%20at%20every%20step.  
437 YouTube. (n.d.).  
Quantum Origins of the Classical. Retrieved from https://www.youtube.com/watch?v=7Sn63t3BeMc  
82 ResearchGate. (n.d.).  
Decoherence and the Quantum-To-Classical Transition. Retrieved from https://www.researchgate.net/publication/33520168\_Decoherence\_and\_the\_Quantum-To-Classical\_Transition  
77 PhilSci-Archive. (n.d.).  
Decoherence and the Quantum-to-Classical Transition. Retrieved from https://philsci-archive.pitt.edu/5258/1/decoherence\_and\_the\_quantum-to-classical\_transition.pdf  
91 Hofkirchner. (n.d.).  
Autopoiesis. Retrieved from http://www.hofkirchner.uti.at/wp-content/uploads/2010/05/autopoiesis.pdf  
215 PMC. (n.d.).  
T Cell Development in the Thymus. Retrieved from https://pmc.ncbi.nlm.nih.gov/articles/PMC4757912/  
368 Medium. (n.d.).  
Emotional AI and Humans: The Ethical and Practical Challenges. Retrieved from https://medium.com/@afshanbaig401/emotional-ai-and-humans-the-ethical-and-practical-challenges-3cd939b55b5f  
438 arXiv. (n.d.).  
QBism, Enaction, and the Participatory Universe. Retrieved from https://arxiv.org/html/2411.04230v1  
439 arXiv. (n.d.).  
QBism, Enaction, and the Participatory Universe. Retrieved from https://arxiv.org/abs/2411.04230  
133 Wikipedia. (n.d.).  
Interpretations of quantum mechanics. Retrieved from https://en.wikipedia.org/wiki/Interpretations\_of\_quantum\_mechanics  
133 Mateus Araújo. (2020, October 1).  
Why QBism is completely empty. Retrieved from https://mateusaraujo.info/2020/10/01/why-qbism-is-completely-empty/  
440 Ezequiel Di Paolo. (n.d.).  
Enactive approach. Retrieved from https://ezequieldipaolo.net/tag/enactive-approach/  
441 Ezequiel Di Paolo. (2023, March 16).  
A QBism/Enactivism dialogue. Retrieved from https://ezequieldipaolo.net/2023/03/16/a-qbism-enactivism-dialogue/  
442 Stanford Encyclopedia of Philosophy. (n.d.).  
Computational Philosophy. Retrieved from https://plato.stanford.edu/entries/computational-philosophy/  
443 Wikipedia. (n.d.).  
Computational theory of mind. Retrieved from https://en.wikipedia.org/wiki/Computational\_theory\_of\_mind  
444 PhilPapers. (n.d.).  
Philosophy of Computing and Information. Retrieved from https://philpapers.org/browse/philosophy-of-computing-and-information  
445 Utrecht University. (n.d.).  
The Philosophy of Computation. Retrieved from https://webspace.science.uu.nl/\~leeuw112/Bratislava-2015.pdf  
162 PhilSci-Archive. (n.d.).  
The uninvited guest: 'local realism' and the Bell theorem. Retrieved from https://philsci-archive.pitt.edu/5258/1/The\_uninvited\_guest\_\_%27local\_realism%27\_and\_the\_Bell\_theorem.pdf  
446 Wikipedia. (n.d.).  
Bell's theorem. Retrieved from https://en.wikipedia.org/wiki/Bell%27s\_theorem  
447 Physics Stack Exchange. (n.d.).  
Bell's theorem for dummies: how does it work? Retrieved from https://physics.stackexchange.com/questions/114218/bells-theorem-for-dummies-how-does-it-work  
448 Stanford Encyclopedia of Philosophy. (n.d.).  
Bell's Theorem. Retrieved from https://plato.stanford.edu/entries/bell-theorem/  
449 PhilSci-Archive. (n.d.).  
The uninvited guest: 'local realism' and the Bell theorem. Retrieved from https://philsci-archive.pitt.edu/5258/1/The\_uninvited\_guest\_\_%27local\_realism%27\_and\_the\_Bell\_theorem.pdf  
78 Number Analytics. (n.d.).  
Bell's Theorem Explained. Retrieved from https://www.numberanalytics.com/blog/bells-theorem-explained-quantum-mechanics  
104 UFF. (n.d.).  
Haraway, Donna Jeanne \- Sympoiesis. Retrieved from https://www.professores.uff.br/ricardobasbaum/wp-content/uploads/sites/164/2022/04/Haraway-Donna-Jeanne-Sympoiesis.pdf  
450 Tool-Shed. (n.d.).  
Sympoiesis. Retrieved from https://tool-shed.org/resource/sympoiesis/  
451 UCSC. (2024, January 8).  
Donna Haraway: Making Kin. Retrieved from https://culturalstudies.ucsc.edu/2024/01/08/january-31-donna-haraway-making-kin-lynn-margulis-in-sympoiesis-with-sibling-scientists/  
5 RSD Symposium. (n.d.).  
Designing for Sympoiesis. Retrieved from https://rsdsymposium.org/wp-content/uploads/2023/01/RSD11\_presentation\_94.pdf  
452 The University of Chicago Press Journals. (n.d.).  
When four tectonic plates of liberation theory. Retrieved from https://www.journals.uchicago.edu/doi/full/10.1086/716664  
453 Text Matters. (n.d.).  
Sympoiesis, Autopoiesis and Immunity. Retrieved from https://www.czasopisma.uni.lodz.pl/textmatters/article/view/15534/15320  
167 IACR. (n.d.).  
Proof-Carrying Data without Succinct Arguments. Retrieved from https://eprint.iacr.org/2020/1618.pdf  
166 HackMD. (n.d.).  
Proof-Carrying Data (PCD). Retrieved from https://hackmd.io/@lrusso96/HJUU4QlDY  
174 CSAIL. (n.d.).  
Proof-Carrying Data. Retrieved from https://projects.csail.mit.edu/pcd/  
168 ResearchGate. (n.d.).  
Proof-Carrying Data. Retrieved from https://www.researchgate.net/publication/260399696\_Proof-Carrying\_Data  
82 CSAIL. (n.d.).  
Proof-Carrying Data. Retrieved from https://projects.csail.mit.edu/pcd/  
175 YouTube. (n.d.).  
Proof-Carrying Data. Retrieved from https://www.youtube.com/watch?v=CY84j0\_E7KA  
454 Physics Stack Exchange. (n.d.).  
Second law of thermodynamics and the arrow of time. Retrieved from https://physics.stackexchange.com/questions/33030/second-law-of-thermodynamics-and-the-arrow-of-time-why-isnt-time-considered-fu\#:\~:text=I've%20come%20across%20this,of%20this%20increase%20in%20entropy.  
455 Wikipedia. (n.d.).  
Entropy as an arrow of time. Retrieved from https://en.wikipedia.org/wiki/Entropy\_as\_an\_arrow\_of\_time  
456 Chem LibreTexts. (n.d.).  
Second Law of Thermodynamics. Retrieved from https://chem.libretexts.org/Bookshelves/Physical\_and\_Theoretical\_Chemistry\_Textbook\_Maps/Supplemental\_Modules\_(Physical\_and\_Theoretical\_Chemistry)/Thermodynamics/The\_Four\_Laws\_of\_Thermodynamics/Second\_Law\_of\_Thermodynamics  
2 Puddles of Thought. (2024, January 5).  
Thermodynamics and the Arrow of Time. Retrieved from https://puddlesofthought.blog/2024/01/05/thermodynamics-and-the-arrow-of-time/  
457 Physics Stack Exchange. (n.d.).  
Second law of thermodynamics and the arrow of time. Retrieved from https://physics.stackexchange.com/questions/33030/second-law-of-thermodynamics-and-the-arrow-of-time-why-isnt-time-considered-fu  
99 Wikipedia. (n.d.).  
Second law of thermodynamics. Retrieved from https://en.wikipedia.org/wiki/Second\_law\_of\_thermodynamics  
458 Wikipedia. (n.d.).  
Entropy and life. Retrieved from https://en.wikipedia.org/wiki/Entropy\_and\_life  
459 Evolving HoloSystems. (n.d.).  
Negentropic life. Retrieved from https://www.eoht.info/page/Negentropic%20life  
154 Wikipedia. (n.d.).  
Entropy and life. Retrieved from https://en.wikipedia.org/wiki/Entropy\_and\_life\#:\~:text=In%20the%201944%20book%20What,increase%20%E2%80%93%20decreases%20or%20keeps%20constant  
3 Tholonia. (n.d.).  
What is (Schrodinger's) Negentropy. Retrieved from https://tholonia.com/material/material\_What\_is\_Schrodingers\_Negentropy.html  
460 PMC. (n.d.).  
What Is Life?. Retrieved from https://pmc.ncbi.nlm.nih.gov/articles/PMC7517386/  
460 Dialektika. (n.d.).  
What is Life? Negative Entropy and the Gap Between Physics and Biology. Retrieved from https://en.dialektika.org/science-technology/science/what-is-life-negative-entropy-and-gap-between-physics-biology/  
9 Wikipedia. (n.d.).  
Autopoiesis. Retrieved from https://en.wikipedia.org/wiki/Autopoiesis  
461 Critical Legal Thinking. (2022, January 10).  
Niklas Luhmann: What is Autopoiesis? Retrieved from https://criticallegalthinking.com/2022/01/10/niklas-luhmann-what-is-autopoiesis/  
462 Wikipedia. (n.d.).  
Negentropy. Retrieved from https://en.wikipedia.org/wiki/Negentropy  
463 Cambridge University Press. (n.d.).  
Organization as an Autopoietic System. Retrieved from https://www.cambridge.org/core/books/organization-and-decision/organization-as-an-autopoietic-system/99BFC0D9FF4992CF1C74A8C1CC7EDFE7  
90 SCIRP. (n.d.).  
The I-Theory. Retrieved from https://www.scirp.org/journal/paperinformation?paperid=99336  
146 PMC. (n.d.).  
Autopoiesis, Thermodynamics and the Natural Drift of Living Beings. Retrieved from https://pmc.ncbi.nlm.nih.gov/articles/PMC9317857/  
364 Wikipedia. (n.d.).  
Recapitulation theory. Retrieved from https://en.wikipedia.org/wiki/Recapitulation\_theory  
464 The University of Chicago Press Journals. (n.

#### **Referências citadas**

1. AUTONOMY AND AUTOPOIESIS \- Francisco J. Varela, acessado em junho 29, 2025, [https://mechanism.ucsd.edu/bill/teaching/w22/phil147/Varela%20-%201981%20-%20Autonomy%20and%20Autopoiesis.pdf](https://mechanism.ucsd.edu/bill/teaching/w22/phil147/Varela%20-%201981%20-%20Autonomy%20and%20Autopoiesis.pdf)  
2. Systems theory \- Wikipedia, acessado em junho 29, 2025, [https://en.wikipedia.org/wiki/Systems\_theory](https://en.wikipedia.org/wiki/Systems_theory)  
3. Autopoiesis \- Wikipedia, acessado em junho 30, 2025, [https://en.wikipedia.org/wiki/Autopoiesis](https://en.wikipedia.org/wiki/Autopoiesis)  
4. Autopoiesis and Cognition The Realization of The Living PDF \- Scribd, acessado em junho 29, 2025, [https://www.scribd.com/document/427974147/Autopoiesis-and-cognition-the-realization-of-the-living-pdf](https://www.scribd.com/document/427974147/Autopoiesis-and-cognition-the-realization-of-the-living-pdf)  
5. (PDF) Autopoiesis in Organization Theory and Practice \- ResearchGate, acessado em junho 29, 2025, [https://www.researchgate.net/publication/235263311\_Autopoiesis\_in\_Organization\_Theory\_and\_Practice](https://www.researchgate.net/publication/235263311_Autopoiesis_in_Organization_Theory_and_Practice)  
6. A Study of “Organizational Closure” and Autopoiesis: | Harish's Notebook, acessado em junho 29, 2025, [https://harishsnotebook.wordpress.com/2019/07/21/a-study-of-organizational-closure-and-autopoiesis/](https://harishsnotebook.wordpress.com/2019/07/21/a-study-of-organizational-closure-and-autopoiesis/)  
7. Autopoiesis – Knowledge and References \- Taylor & Francis, acessado em junho 29, 2025, [https://taylorandfrancis.com/knowledge/Medicine\_and\_healthcare/Psychiatry/Autopoiesis/](https://taylorandfrancis.com/knowledge/Medicine_and_healthcare/Psychiatry/Autopoiesis/)  
8. Arguably the most ancient concern in Western philosophy is boundaries and the lack thereof. lnferring from his answer, Thales-ac \- Sala Lab, acessado em junho 29, 2025, [https://sala.lab.asu.edu/wp-content/uploads/2018/03/Callicott-Lamarck-Redux.pdf](https://sala.lab.asu.edu/wp-content/uploads/2018/03/Callicott-Lamarck-Redux.pdf)  
9. Boundary \- Stanford Encyclopedia of Philosophy, acessado em junho 29, 2025, [https://plato.stanford.edu/entries/boundary/](https://plato.stanford.edu/entries/boundary/)  
10. Boundary (Stanford Encyclopedia of Philosophy/Spring 2012 Edition), acessado em junho 29, 2025, [https://plato.stanford.edu/archIves/spr2012/entries/boundary/](https://plato.stanford.edu/archIves/spr2012/entries/boundary/)  
11. Identity \- Stanford Encyclopedia of Philosophy, acessado em junho 29, 2025, [https://plato.stanford.edu/entries/identity/](https://plato.stanford.edu/entries/identity/)  
12. Systems Theory \- The Decision Lab, acessado em junho 29, 2025, [https://thedecisionlab.com/reference-guide/psychology/systems-theory](https://thedecisionlab.com/reference-guide/psychology/systems-theory)  
13. Bell's Theorem \- Stanford Encyclopedia of Philosophy, acessado em junho 30, 2025, [https://plato.stanford.edu/entries/bell-theorem/](https://plato.stanford.edu/entries/bell-theorem/)  
14. Boundaries and Identities | РЕТОРИКА И КОМУНИКАЦИИ, acessado em junho 29, 2025, [https://rhetoric.bg/gilles-rouet-boundaries-and-identities](https://rhetoric.bg/gilles-rouet-boundaries-and-identities)  
15. Personal Identity \- Stanford Encyclopedia of Philosophy, acessado em junho 29, 2025, [https://plato.stanford.edu/entries/identity-personal/](https://plato.stanford.edu/entries/identity-personal/)  
16. Entropy as an arrow of time \- Wikipedia, acessado em junho 30, 2025, [https://en.wikipedia.org/wiki/Entropy\_as\_an\_arrow\_of\_time](https://en.wikipedia.org/wiki/Entropy_as_an_arrow_of_time)  
17. Second law of thermodynamics \- Wikipedia, acessado em junho 30, 2025, [https://en.wikipedia.org/wiki/Second\_law\_of\_thermodynamics](https://en.wikipedia.org/wiki/Second_law_of_thermodynamics)  
18. Humberto Muturana, H. R. Maturana & F. J. Varela, Autopoiesis and Cognition: The Realization of the Living \- PhilPapers, acessado em junho 30, 2025, [https://philpapers.org/rec/MATAAC-3](https://philpapers.org/rec/MATAAC-3)  
19. Implications of Self-Reference: Niklas Luhmann's ... \- CiteSeerX, acessado em junho 30, 2025, [https://citeseerx.ist.psu.edu/document?repid=rep1\&type=pdf\&doi=8fb7658bdbb5619b00accb2cf2df16be76c64580](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=8fb7658bdbb5619b00accb2cf2df16be76c64580)  
20. The fediverse is an opportunity learned societies can't ignore \- Impact of Social Sciences, acessado em junho 29, 2025, [https://blogs.lse.ac.uk/impactofsocialsciences/2023/11/30/the-fediverse-is-an-opportunity-learned-societies-cant-ignore/](https://blogs.lse.ac.uk/impactofsocialsciences/2023/11/30/the-fediverse-is-an-opportunity-learned-societies-cant-ignore/)  
21. Shifting your research from X to Mastodon? Here's what you need to know \- PMC, acessado em junho 29, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC10801199/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10801199/)  
22. Rethinking the ˝social˛ in ˝social media˛: Insights into topology, abstraction, and scale on the Mastodon social network \- Robert W. Gehl, acessado em junho 29, 2025, [https://www.robertwgehl.org/text/pubs/Zulli%20et%20al.%20-%202020%20-%20Rethinking%20the%20%E2%80%9Csocial%E2%80%9D%20in%20%E2%80%9Csocial%20media%E2%80%9D%20Insight.pdf](https://www.robertwgehl.org/text/pubs/Zulli%20et%20al.%20-%202020%20-%20Rethinking%20the%20%E2%80%9Csocial%E2%80%9D%20in%20%E2%80%9Csocial%20media%E2%80%9D%20Insight.pdf)  
23. Sistema imunitário – Wikipédia, a enciclopédia livre, acessado em junho 29, 2025, [https://pt.wikipedia.org/wiki/Sistema\_imunit%C3%A1rio](https://pt.wikipedia.org/wiki/Sistema_imunit%C3%A1rio)  
24. Stephanie Forrest's unique integration of computation, biology and health \- ASU News, acessado em junho 29, 2025, [https://news.asu.edu/b/20241014-stephanie-forrests-unique-integration-computation-biology-and-health](https://news.asu.edu/b/20241014-stephanie-forrests-unique-integration-computation-biology-and-health)  
25. Burnet, F.M. (1959) The Clonal Selection Theory of Acquired Immunity. Vanderbilt University Press, Nashville. \- References \- Scientific Research Publishing, acessado em junho 30, 2025, [https://www.scirp.org/reference/referencespapers?referenceid=1576907](https://www.scirp.org/reference/referencespapers?referenceid=1576907)  
26. Considerações gerais sobre o sistema imunológico \- MSD Manuals, acessado em junho 29, 2025, [https://www.msdmanuals.com/pt/casa/doen%C3%A7as-imunol%C3%B3gicas/biologia-do-sistema-imunol%C3%B3gico/considera%C3%A7%C3%B5es-gerais-sobre-o-sistema-imunol%C3%B3gico](https://www.msdmanuals.com/pt/casa/doen%C3%A7as-imunol%C3%B3gicas/biologia-do-sistema-imunol%C3%B3gico/considera%C3%A7%C3%B5es-gerais-sobre-o-sistema-imunol%C3%B3gico)  
27. Self or nonself: end of a dogma? \- Frontiers, acessado em junho 29, 2025, [https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2025.1595764/full](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2025.1595764/full)  
28. imunologia – capítulo um imunidade inata (não específica) \- FCAV, acessado em junho 29, 2025, [https://www.fcav.unesp.br/Home/departamentos/patologia/HELIOJOSEMONTASSIER/ed-1-imunidade-inata.pdf](https://www.fcav.unesp.br/Home/departamentos/patologia/HELIOJOSEMONTASSIER/ed-1-imunidade-inata.pdf)  
29. Capítulo 1 \- Imunologia, acessado em junho 29, 2025, [https://www.epsjv.fiocruz.br/sites/default/files/cap1.pdf](https://www.epsjv.fiocruz.br/sites/default/files/cap1.pdf)  
30. Self-Antigens vs. Non-Self Antigens: Examples in Immunology \- Akadeum Life Sciences, acessado em junho 29, 2025, [https://www.akadeum.com/blog/self-antigens-vs-non-self-antigens-examples-cluster-of-differentiation-markers/](https://www.akadeum.com/blog/self-antigens-vs-non-self-antigens-examples-cluster-of-differentiation-markers/)  
31. Chapter 15 Self and Nonself \- Lehigh University, acessado em junho 29, 2025, [https://www.lehigh.edu/\~mhb0/PhilBioPotentialReadings%2020Oct18/Sahotra\_Sarkar,\_Anya\_PlutynskiSelfNonself\_A\_Companion\_to\_th%20.pdf](https://www.lehigh.edu/~mhb0/PhilBioPotentialReadings%2020Oct18/Sahotra_Sarkar,_Anya_PlutynskiSelfNonself_A_Companion_to_th%20.pdf)  
32. What is Defense-in-Depth (DiD)? \- Delinea, acessado em junho 29, 2025, [https://delinea.com/what-is/defense-in-depth-did](https://delinea.com/what-is/defense-in-depth-did)  
33. Defense in depth (computing) | EBSCO Research Starters, acessado em junho 29, 2025, [https://www.ebsco.com/research-starters/computer-science/defense-depth-computing](https://www.ebsco.com/research-starters/computer-science/defense-depth-computing)  
34. Defesa em profundidade (defense-in-depth) \- Daniel Donda, acessado em junho 29, 2025, [https://danieldonda.com/defesa-em-profundidade/](https://danieldonda.com/defesa-em-profundidade/)  
35. O que é o Defense in Depth? \- Software da Check Point, acessado em junho 29, 2025, [https://www.checkpoint.com/pt/cyber-hub/cyber-security/what-is-defense-in-depth/](https://www.checkpoint.com/pt/cyber-hub/cyber-security/what-is-defense-in-depth/)  
36. Defesa em profundidade: como implementar essa estratégia de cibersegurança, acessado em junho 29, 2025, [https://www.welivesecurity.com/br/2022/09/16/defesa-em-profundidade-como-implementar-essa-estrategia-de-ciberseguranca/](https://www.welivesecurity.com/br/2022/09/16/defesa-em-profundidade-como-implementar-essa-estrategia-de-ciberseguranca/)  
37. Sistema imunitário: Parte I. Fundamentos da ... \- SciELO Brasil, acessado em junho 29, 2025, [https://www.scielo.br/j/rbr/a/QdW9KFBP3XsLvCYRJ8Q7SRb/](https://www.scielo.br/j/rbr/a/QdW9KFBP3XsLvCYRJ8Q7SRb/)  
38. Aula 04 \-Imunologia Básica \-Padrões Moleculares de Reconhecimento \- YouTube, acessado em junho 29, 2025, [https://www.youtube.com/watch?v=DKDmzv4R-QA](https://www.youtube.com/watch?v=DKDmzv4R-QA)  
39. Diferenças entre PAMPs e DAMPs \- Biomedicina Padrão, acessado em junho 29, 2025, [https://www.biomedicinapadrao.com.br/2023/11/diferencas-entre-pamps-e-damps.html](https://www.biomedicinapadrao.com.br/2023/11/diferencas-entre-pamps-e-damps.html)  
40. Moléculas Reconhecidas pelo Sistema Imune:- PAMPS e Antígenos (Ag) \- FCAV, acessado em junho 29, 2025, [https://www.fcav.unesp.br/Home/departamentos/patologia/HELIOJOSEMONTASSIER/aula-2--antigenos-e-pamps.pdf](https://www.fcav.unesp.br/Home/departamentos/patologia/HELIOJOSEMONTASSIER/aula-2--antigenos-e-pamps.pdf)  
41. 6- Resposta imune inata \- PAMP e DAMP \- Flávio Gimenis, acessado em junho 29, 2025, [https://flaviogimenis.com.br/wp-content/uploads/2018/12/6-Resposta-imune-inata-PAMP-e-DAMP.pdf](https://flaviogimenis.com.br/wp-content/uploads/2018/12/6-Resposta-imune-inata-PAMP-e-DAMP.pdf)  
42. RECEPTORES DA IMUNIDADE INATA (PRR, PAMP e DAMP) \- PROF ALEXANDRE FUNCK \- YouTube, acessado em junho 29, 2025, [https://www.youtube.com/watch?v=DkCyAeDKMDo](https://www.youtube.com/watch?v=DkCyAeDKMDo)  
43. Genetic Regulation of Immune Response in Dogs \- MDPI, acessado em junho 29, 2025, [https://www.mdpi.com/2073-4425/16/7/764](https://www.mdpi.com/2073-4425/16/7/764)  
44. Kuby Immunology, acessado em junho 29, 2025, [https://www.roswellpark.org/sites/default/files/thanavala\_9-4-14\_innate\_immunity\_part\_1.pdf](https://www.roswellpark.org/sites/default/files/thanavala_9-4-14_innate_immunity_part_1.pdf)  
45. | PAMPs recognized by the toll-like receptors (TLRs). | Download Table \- ResearchGate, acessado em junho 29, 2025, [https://www.researchgate.net/figure/PAMPs-recognized-by-the-toll-like-receptors-TLRs\_tbl1\_237071330](https://www.researchgate.net/figure/PAMPs-recognized-by-the-toll-like-receptors-TLRs_tbl1_237071330)  
46. Host Immune Response to Mycobacterium tuberculosis Infection | JIR \- Dove Medical Press, acessado em junho 29, 2025, [https://www.dovepress.com/host-immune-response-to-mycobacterium-tuberculosis-infection-implicati-peer-reviewed-fulltext-article-JIR](https://www.dovepress.com/host-immune-response-to-mycobacterium-tuberculosis-infection-implicati-peer-reviewed-fulltext-article-JIR)  
47. Using secp256k1 with wolfSSL: A Step-by-Step Guide, acessado em junho 29, 2025, [https://www.wolfssl.com/using-secp256k1-with-wolfssl-a-step-by-step-guide/](https://www.wolfssl.com/using-secp256k1-with-wolfssl-a-step-by-step-guide/)  
48. PAMPs and TLRs : Pathogen Associated Molecular Patterns, and Toll Like Receptors., acessado em junho 29, 2025, [https://www.youtube.com/watch?v=1XcGulDvAPw\&pp=0gcJCdgAo7VqN5tD](https://www.youtube.com/watch?v=1XcGulDvAPw&pp=0gcJCdgAo7VqN5tD)  
49. Sistema imunológico (artigo) \- Khan Academy, acessado em junho 29, 2025, [https://pt.khanacademy.org/science/7-ano/sistema-imunologico/corpo-humano-sistema-imunologico/a/sistema-imunologico](https://pt.khanacademy.org/science/7-ano/sistema-imunologico/corpo-humano-sistema-imunologico/a/sistema-imunologico)  
50. Tipos de imunidade e tudo que você precisa saber sobre eles \- Targifor, acessado em junho 29, 2025, [https://www.targifor.com.br/dicas-de-saude/tipos-de-imunidade/](https://www.targifor.com.br/dicas-de-saude/tipos-de-imunidade/)  
51. Imunidade inata e adaptativa: qual a diferença entre elas? \- Benegrip, acessado em junho 29, 2025, [https://www.benegrip.com.br/saude/prevencao-gripe/o-que-sao-imunidade-inata-e-adaptativa-para-que-servem](https://www.benegrip.com.br/saude/prevencao-gripe/o-que-sao-imunidade-inata-e-adaptativa-para-que-servem)  
52. Imunidade inata e adaptativa: o que são \+ diferenças \- Vitasay 50+, acessado em junho 29, 2025, [https://www.vitasay.com.br/blog/cuidados-com-o-corpo/imunidade-inata-e-adaptativa-como-elas-atuam-no-organismo](https://www.vitasay.com.br/blog/cuidados-com-o-corpo/imunidade-inata-e-adaptativa-como-elas-atuam-no-organismo)  
53. Innate and adaptive immunity: specificities and signaling hierarchies revisited \- PMC, acessado em junho 29, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC7097365/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7097365/)  
54. What is the difference between innate and adaptive immunity? \- Bupa UK, acessado em junho 29, 2025, [https://www.bupa.co.uk/newsroom/ourviews/innate-adaptive-immunity](https://www.bupa.co.uk/newsroom/ourviews/innate-adaptive-immunity)  
55. A Comparison of the Innate and Adaptive Immune Systems in Cartilaginous Fish, Ray-Finned Fish, and Lobe-Finned Fish \- Frontiers, acessado em junho 29, 2025, [https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2019.02292/full](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2019.02292/full)  
56. pmc.ncbi.nlm.nih.gov, acessado em junho 29, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC7097365/\#:\~:text=In%20general%2C%20innate%20immunity%20is,whose%20engagement%20dictates%20lymphocyte%20function.](https://pmc.ncbi.nlm.nih.gov/articles/PMC7097365/#:~:text=In%20general%2C%20innate%20immunity%20is,whose%20engagement%20dictates%20lymphocyte%20function.)  
57. Software simula sistema imunológico humano e auxilia em pesquisas e na aprendizagem \- FAPEMIG, acessado em junho 29, 2025, [https://fapemig.br/pt/noticias/1194/](https://fapemig.br/pt/noticias/1194/)  
58. Imunologia Computacional: Conheça a área da computacão responsável por estudar o Sistema Imune \- CodeCrush, acessado em junho 29, 2025, [https://codecrush.com.br/blog/imunologia-computacional](https://codecrush.com.br/blog/imunologia-computacional)  
59. (PDF) Cyber Immunity \- A Bio-Inspired Cyber Defense System \- ResearchGate, acessado em junho 29, 2025, [https://www.researchgate.net/publication/315861769\_Cyber\_Immunity\_-\_A\_Bio-Inspired\_Cyber\_Defense\_System](https://www.researchgate.net/publication/315861769_Cyber_Immunity_-_A_Bio-Inspired_Cyber_Defense_System)  
60. Challenges in cybersecurity: Lessons from biological defense systems \- Carl T. Bergstrom, acessado em junho 29, 2025, [http://ctbergstrom.com/publications/pdfs/2023MathematicalBiosciences.pdf](http://ctbergstrom.com/publications/pdfs/2023MathematicalBiosciences.pdf)  
61. Sistemas Imunológicos Artificiais \- Ciência HojeCiência Hoje, acessado em junho 29, 2025, [https://cienciahoje.org.br/artigo/sistemas-imunologicos-artificiais/](https://cienciahoje.org.br/artigo/sistemas-imunologicos-artificiais/)  
62. 1 Introdução \- Maxwell, acessado em junho 29, 2025, [https://www.maxwell.vrac.puc-rio.br/8236/8236\_2.PDF](https://www.maxwell.vrac.puc-rio.br/8236/8236_2.PDF)  
63. Analogies with immunology represent an important step toward the vision of robust, distributed protection for computers. Stephan \- UNM CS \- The University of New Mexico, acessado em junho 29, 2025, [https://www.cs.unm.edu/\~forrest/publications/cacm96-final.pdf](https://www.cs.unm.edu/~forrest/publications/cacm96-final.pdf)  
64. Center for Biocomputing, Security and Society | ASU Biodesign Institute, acessado em junho 29, 2025, [https://biodesign.asu.edu/biocomputing-security-and-society/](https://biodesign.asu.edu/biocomputing-security-and-society/)  
65. Nexus Whitepaper \- Nexus.xyz, acessado em junho 30, 2025, [https://whitepaper.nexus.xyz](https://whitepaper.nexus.xyz)  
66. Nexus Whitepaper \- Nexus.xyz, acessado em junho 30, 2025, [https://whitepaper.nexus.xyz/](https://whitepaper.nexus.xyz/)  
67. Autopoiesis and Cognition \- CiteSeerX, acessado em junho 29, 2025, [https://citeseerx.ist.psu.edu/document?repid=rep1\&type=pdf\&doi=a185ee72dca8be938838bbfc376954b59db92374](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=a185ee72dca8be938838bbfc376954b59db92374)  
68. AUTOPOESIS-CHhypertext \- CHRISTIAN HUBERT STUDIO, acessado em junho 29, 2025, [https://www.christianhubert.com/writing/autopoesis](https://www.christianhubert.com/writing/autopoesis)  
69. (PDF) Autopoiesis and Life \- ResearchGate, acessado em junho 30, 2025, [https://www.researchgate.net/publication/242416037\_Autopoiesis\_and\_Life](https://www.researchgate.net/publication/242416037_Autopoiesis_and_Life)  
70. Closed and Open Systems: Organizational \- ResearchGate, acessado em junho 30, 2025, [https://www.researchgate.net/publication/323839617\_Closed\_and\_Open\_Systems\_Organizational](https://www.researchgate.net/publication/323839617_Closed_and_Open_Systems_Organizational)  
71. On closed and open systems (1986) | Ephemeral Journal, acessado em junho 30, 2025, [https://ephemerajournal.org/contribution/closed-and-open-systems-1986](https://ephemerajournal.org/contribution/closed-and-open-systems-1986)  
72. Systems Theory Approach, acessado em junho 30, 2025, [https://saylordotorg.github.io/text\_mastering-public-relations/s07-02-systems-theory-approach.html](https://saylordotorg.github.io/text_mastering-public-relations/s07-02-systems-theory-approach.html)  
73. (PDF) Computing with Autopoietic Systems \- ResearchGate, acessado em junho 30, 2025, [https://www.researchgate.net/publication/254842986\_Computing\_with\_Autopoietic\_Systems](https://www.researchgate.net/publication/254842986_Computing_with_Autopoietic_Systems)  
74. A Theory of the Living Organization \- Biology of Cognition Lab, acessado em junho 30, 2025, [https://biologyofcognition.files.wordpress.com/2008/06/maturana1975organizationlivingtheorylivingorganization.pdf](https://biologyofcognition.files.wordpress.com/2008/06/maturana1975organizationlivingtheorylivingorganization.pdf)  
75. Autopoiesis and cognition : the realization of the living : Maturana, Humberto R., 1928- : Free Download, Borrow, and Streaming \- Internet Archive, acessado em junho 30, 2025, [https://archive.org/details/autopoiesiscogni0042matu](https://archive.org/details/autopoiesiscogni0042matu)  
76. Enactivism | Internet Encyclopedia of Philosophy, acessado em junho 30, 2025, [https://iep.utm.edu/enactivism/](https://iep.utm.edu/enactivism/)  
77. Autopoietic Enactivism, Phenomenology and the Deep ... \- CEPA.INFO, acessado em junho 29, 2025, [https://cepa.info/fulltexts/2385.pdf](https://cepa.info/fulltexts/2385.pdf)  
78. Autopoietic theory, enactivism, and their incommensurable marks of the cognitive \- Ificc, acessado em junho 30, 2025, [http://www.ificc.cl/wp-content/uploads/2022/09/Villalobos%20%26%20Palacios%202019.pdf](http://www.ificc.cl/wp-content/uploads/2022/09/Villalobos%20%26%20Palacios%202019.pdf)  
79. Enaction for QBists \- arXiv, acessado em junho 30, 2025, [https://arxiv.org/html/2411.04230v1](https://arxiv.org/html/2411.04230v1)  
80. \[2411.04230\] Enaction for QBists \- arXiv, acessado em junho 30, 2025, [https://arxiv.org/abs/2411.04230](https://arxiv.org/abs/2411.04230)  
81. (PDF) Luhmann's theory of autopoietic social systems \- ResearchGate, acessado em junho 29, 2025, [https://www.researchgate.net/publication/277293382\_Luhmann's\_theory\_of\_autopoietic\_social\_systems](https://www.researchgate.net/publication/277293382_Luhmann's_theory_of_autopoietic_social_systems)  
82. Niklas Luhmann: What is Autopoiesis? \- Critical Legal Thinking, acessado em junho 30, 2025, [https://criticallegalthinking.com/2022/01/10/niklas-luhmann-what-is-autopoiesis/](https://criticallegalthinking.com/2022/01/10/niklas-luhmann-what-is-autopoiesis/)  
83. Luhmann's Systems Theory Explained \- Number Analytics, acessado em junho 30, 2025, [https://www.numberanalytics.com/blog/luhmann-systems-theory-guide](https://www.numberanalytics.com/blog/luhmann-systems-theory-guide)  
84. Niklas Luhmann \- The Autopoiesis of Social Systems | PDF \- Scribd, acessado em junho 29, 2025, [https://www.scribd.com/document/93493871/Niklas-Luhmann-The-Autopoiesis-of-Social-Systems](https://www.scribd.com/document/93493871/Niklas-Luhmann-The-Autopoiesis-of-Social-Systems)  
85. Chapter 13 \- Luhmann's Sociological Systems Theory and the Study of Social Problems, acessado em junho 29, 2025, [https://www.cambridge.org/core/books/cambridge-handbook-of-social-problems/luhmanns-sociological-systems-theory-and-the-study-of-social-problems/A9E33562674D1EBC46E095BE50994292](https://www.cambridge.org/core/books/cambridge-handbook-of-social-problems/luhmanns-sociological-systems-theory-and-the-study-of-social-problems/A9E33562674D1EBC46E095BE50994292)  
86. Niklas Luhmann's Societal Insights \- Philosophical.chat, acessado em junho 30, 2025, [https://philosophical.chat/philosophy/philosophers-and-their-philosophies/niklas-luhmann/](https://philosophical.chat/philosophy/philosophers-and-their-philosophies/niklas-luhmann/)  
87. Please explain Niklas Luhmann's ideas to me like I am five. : r/sociology \- Reddit, acessado em junho 30, 2025, [https://www.reddit.com/r/sociology/comments/1cvovtx/please\_explain\_niklas\_luhmanns\_ideas\_to\_me\_like\_i/](https://www.reddit.com/r/sociology/comments/1cvovtx/please_explain_niklas_luhmanns_ideas_to_me_like_i/)  
88. Summary re: Niklas Luhmann, acessado em junho 30, 2025, [https://web.pdx.edu/\~tothm/theoryii/Luhmann%20Summary.doc](https://web.pdx.edu/~tothm/theoryii/Luhmann%20Summary.doc)  
89. web.pdx.edu, acessado em junho 30, 2025, [https://web.pdx.edu/\~tothm/theoryii/Luhmann%20Summary.doc\#:\~:text=Social%20systems%20are%20self%2Dreferential,%2C%20self%2Dcreating%5D%20systems.](https://web.pdx.edu/~tothm/theoryii/Luhmann%20Summary.doc#:~:text=Social%20systems%20are%20self%2Dreferential,%2C%20self%2Dcreating%5D%20systems.)  
90. Niklas Luhmann's Social Systems Theory | deterritorialization \- Medium, acessado em junho 30, 2025, [https://medium.com/deterritorialization/social-systems-and-autopoiesis-a34f52fe9da1](https://medium.com/deterritorialization/social-systems-and-autopoiesis-a34f52fe9da1)  
91. Autopoiesis and Critical Social Systems Theory \- wolfgang hofkirchner, acessado em junho 29, 2025, [http://www.hofkirchner.uti.at/wp-content/uploads/2010/05/autopoiesis.pdf](http://www.hofkirchner.uti.at/wp-content/uploads/2010/05/autopoiesis.pdf)  
92. 惟愿公平如大水滚滚，使公义如江河滔滔！ et revelabitur quasi aqua iudicium et iustitia quasi torrens fortis \- 公法评论, acessado em junho 29, 2025, [https://www.gongfa.com/lumanlilunjichu.htm](https://www.gongfa.com/lumanlilunjichu.htm)  
93. İnsan ve Toplum » Submission » A Critical Review of Luhmann's Social Systems Theory's Perspective on Mass Media and Social Media \- DergiPark, acessado em junho 29, 2025, [https://dergipark.org.tr/en/pub/insanvetoplum/issue/71110/1139688](https://dergipark.org.tr/en/pub/insanvetoplum/issue/71110/1139688)  
94. Carlo Rovelli's relational interpretation and world view : r/QuantumPhysics \- Reddit, acessado em junho 30, 2025, [https://www.reddit.com/r/QuantumPhysics/comments/1jhayy1/carlo\_rovellis\_relational\_interpretation\_and/](https://www.reddit.com/r/QuantumPhysics/comments/1jhayy1/carlo_rovellis_relational_interpretation_and/)  
95. Chapter 4 | The Organization of Art as a Social System \- mdw, acessado em junho 29, 2025, [https://www.mdw.ac.at/mdwpress/mdwp011-ch4/](https://www.mdw.ac.at/mdwpress/mdwp011-ch4/)  
96. SYMPOIETIC AND AUTOPOIETIC SYSTEMS: A NEW DISTINCTION FOR SELF-ORGANIZING SYSTEMS \- CiteSeerX, acessado em junho 29, 2025, [https://citeseerx.ist.psu.edu/document?repid=rep1\&type=pdf\&doi=44299317a20afcd33b0a11d3b2bf4fc196088d45](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=44299317a20afcd33b0a11d3b2bf4fc196088d45)  
97. View of Sympoiesis, Autopoiesis and Immunity: How to Coexist with Nonhuman Others? | Text Matters, acessado em junho 30, 2025, [https://www.czasopisma.uni.lodz.pl/textmatters/article/view/15534/15320](https://www.czasopisma.uni.lodz.pl/textmatters/article/view/15534/15320)  
98. sympoiesis, and \- art science activisms, acessado em junho 29, 2025, [http://carbonfarm.us/555/haraway-art.pdf](http://carbonfarm.us/555/haraway-art.pdf)  
99. Sympoiesis \- Professores da Universidade Federal Fluminense, acessado em junho 30, 2025, [https://www.professores.uff.br/ricardobasbaum/wp-content/uploads/sites/164/2022/04/Haraway-Donna-Jeanne-Sympoiesis.pdf](https://www.professores.uff.br/ricardobasbaum/wp-content/uploads/sites/164/2022/04/Haraway-Donna-Jeanne-Sympoiesis.pdf)  
100. Chapter 3 Sympoiesis Symbiogenesis and the Lively Arts of Staying with the Trouble1 \<\> I. Sy \- WordPress.com, acessado em junho 29, 2025, [https://chthulublog.files.wordpress.com/2016/10/ch\_03-sympoiesis.pdf](https://chthulublog.files.wordpress.com/2016/10/ch_03-sympoiesis.pdf)  
101. Sympoietic and autopoietic systems: A new distinction for self-organizing systems \- ResearchGate, acessado em junho 29, 2025, [https://www.researchgate.net/publication/228566588\_Sympoietic\_and\_autopoietic\_systems\_A\_new\_distinction\_for\_self-organizing\_systems](https://www.researchgate.net/publication/228566588_Sympoietic_and_autopoietic_systems_A_new_distinction_for_self-organizing_systems)  
102. Staying with the Trouble: Notes on Chapter 3 \- Josephine Anstey, acessado em junho 29, 2025, [https://josephineanstey.com/?page\_id=2417](https://josephineanstey.com/?page_id=2417)  
103. RECENZJE \- Biblioteka Nauki, acessado em junho 29, 2025, [https://bibliotekanauki.pl/articles/1621556.pdf](https://bibliotekanauki.pl/articles/1621556.pdf)  
104. Introduction: A Special Issue on Niklas Luhmann's systems theory and law, acessado em junho 29, 2025, [https://opo.iisj.net/index.php/osls/article/view/1855/2313](https://opo.iisj.net/index.php/osls/article/view/1855/2313)  
105. www.researchgate.net, acessado em junho 29, 2025, [https://www.researchgate.net/publication/228566588\_Sympoietic\_and\_autopoietic\_systems\_A\_new\_distinction\_for\_self-organizing\_systems\#:\~:text=Looking%20across%20works%20on%20biology,open%20systems%20and%20making%2Dtogether.](https://www.researchgate.net/publication/228566588_Sympoietic_and_autopoietic_systems_A_new_distinction_for_self-organizing_systems#:~:text=Looking%20across%20works%20on%20biology,open%20systems%20and%20making%2Dtogether.)  
106. Sympoietic Structures: Enfolding Ecological Inputs into Core-Studio Curricula, acessado em junho 29, 2025, [https://www.acsa-arch.org/proceedings/Teachers%20Proceedings/ACSA.Teach.2021/ACSA.Teach.2021.4.pdf](https://www.acsa-arch.org/proceedings/Teachers%20Proceedings/ACSA.Teach.2021/ACSA.Teach.2021.4.pdf)  
107. Alice Iacobone, acessado em junho 29, 2025, [https://ojs.unito.it/index.php/philosophykitchen/article/view/5877/5129](https://ojs.unito.it/index.php/philosophykitchen/article/view/5877/5129)  
108. A Critical Review of Autopoietic Theory and its Applications to Living, Social, Organizational and Information Systems \- ResearchGate, acessado em junho 30, 2025, [https://www.researchgate.net/publication/272353462\_A\_Critical\_Review\_of\_Autopoietic\_Theory\_and\_its\_Applications\_to\_Living\_Social\_Organizational\_and\_Information\_Systems](https://www.researchgate.net/publication/272353462_A_Critical_Review_of_Autopoietic_Theory_and_its_Applications_to_Living_Social_Organizational_and_Information_Systems)  
109. Trust and betrayal: a conceptual analysis \- Macquarie University, acessado em junho 29, 2025, [https://figshare.mq.edu.au/articles/thesis/Trust\_and\_betrayal\_a\_conceptual\_analysis/19436147/1](https://figshare.mq.edu.au/articles/thesis/Trust_and_betrayal_a_conceptual_analysis/19436147/1)  
110. The Philosophy of Trust: Key Findings | Kellogg School of Management, acessado em junho 29, 2025, [https://www.kellogg.northwestern.edu/academics-research/trust-project/videos/goldberg-ep-2/](https://www.kellogg.northwestern.edu/academics-research/trust-project/videos/goldberg-ep-2/)  
111. The Philosophy of Trust: Key Findings | Northwestern University \- YouTube, acessado em junho 29, 2025, [https://www.youtube.com/watch?v=NLgSQzzDwbs](https://www.youtube.com/watch?v=NLgSQzzDwbs)  
112. The Nature of Trust: A Philosopher's Perspective | Kellogg School of Management, acessado em junho 29, 2025, [https://www.kellogg.northwestern.edu/academics-research/trust-project/videos/goldberg-ep-1/](https://www.kellogg.northwestern.edu/academics-research/trust-project/videos/goldberg-ep-1/)  
113. Trust \- Stanford Encyclopedia of Philosophy, acessado em junho 29, 2025, [https://plato.stanford.edu/entries/trust/](https://plato.stanford.edu/entries/trust/)  
114. Trust (Stanford Encyclopedia of Philosophy/Summer 2020 Edition), acessado em junho 29, 2025, [https://plato.stanford.edu/archIves/sum2020/entries/trust/](https://plato.stanford.edu/archIves/sum2020/entries/trust/)  
115. Trust book by Diego Gambetta \- ThriftBooks, acessado em junho 30, 2025, [https://www.thriftbooks.com/w/trust\_diego-gambetta/1580535/](https://www.thriftbooks.com/w/trust_diego-gambetta/1580535/)  
116. Gambetta, D. (Ed.) (1988). Trust Making and breaking cooperative relations. Oxford Blackwell. \- References \- Scientific Research Publishing, acessado em junho 30, 2025, [https://www.scirp.org/reference/referencespapers?referenceid=490521](https://www.scirp.org/reference/referencespapers?referenceid=490521)  
117. Diego Gambetta (ed.), Trust: Making and Breaking Cooperative Relations \- PhilArchive, acessado em junho 30, 2025, [https://philarchive.org/rec/GAMTMA](https://philarchive.org/rec/GAMTMA)  
118. Diego Gambetta, Can We Trust Trust? \- PhilPapers, acessado em junho 30, 2025, [https://philpapers.org/rec/GAMCWT](https://philpapers.org/rec/GAMCWT)  
119. Trust: making and breaking cooperative relations \- ResearchGate, acessado em junho 30, 2025, [https://www.researchgate.net/profile/Diego-Gambetta/publication/242591079\_Trust\_Making\_and\_Breaking\_Cooperative\_Relations/links/56ab47be08ae8f386568be63/Trust-Making-and-Breaking-Cooperative-Relations.pdf](https://www.researchgate.net/profile/Diego-Gambetta/publication/242591079_Trust_Making_and_Breaking_Cooperative_Relations/links/56ab47be08ae8f386568be63/Trust-Making-and-Breaking-Cooperative-Relations.pdf)  
120. Trust: Making and breaking cooperative relations \- Diego Gambetta: 9780631155065 \- AbeBooks, acessado em junho 30, 2025, [https://www.abebooks.com/9780631155065/Trust-Making-breaking-cooperative-relations-0631155066/plp](https://www.abebooks.com/9780631155065/Trust-Making-breaking-cooperative-relations-0631155066/plp)  
121. Shapiro, P. S. (1987). The Social Control of Impersonal Trust. American Journal of Sociology, 93, 623-658. \- References \- Scientific Research Publishing, acessado em junho 30, 2025, [https://www.scirp.org/reference/referencespapers?referenceid=3221768](https://www.scirp.org/reference/referencespapers?referenceid=3221768)  
122. S. P. Shapiro, “The Social Control of Impersonal Trust,” American Journal of Sociology, Vol. 93, No. 3, 1987, pp. 623-658. doi10.1086/228791 \- References \- Scientific Research Publishing, acessado em junho 30, 2025, [https://www.scirp.org/reference/referencespapers?referenceid=792093](https://www.scirp.org/reference/referencespapers?referenceid=792093)  
123. The Social Control of Impersonal Trust | American Journal of Sociology: Vol 93, No 3, acessado em junho 30, 2025, [https://www.journals.uchicago.edu/doi/10.1086/228791](https://www.journals.uchicago.edu/doi/10.1086/228791)  
124. AGENCY THEORY Susan P. Shapiro \- Strategy Admin, acessado em junho 30, 2025, [http://strategy.sjsu.edu/www.stable/pdf/Schapiro,%20S.,%202005,%20Annual%20Review%20of%20Sociology%2031%20263-284.pdf](http://strategy.sjsu.edu/www.stable/pdf/Schapiro,%20S.,%202005,%20Annual%20Review%20of%20Sociology%2031%20263-284.pdf)  
125. Trust But Verify \- Security Today, acessado em junho 29, 2025, [https://securitytoday.com/articles/2024/09/12/trust-but-verify.aspx](https://securitytoday.com/articles/2024/09/12/trust-but-verify.aspx)  
126. Trust But Verify | Summit Security Group, LLC, acessado em junho 29, 2025, [https://www.summitinfosec.com/blog/trust-but-verify/](https://www.summitinfosec.com/blog/trust-but-verify/)  
127. Five Key Considerations When Applying a Trust, but Verify Approach to Information Security and Risk Management \- ISACA, acessado em junho 29, 2025, [https://www.isaca.org/resources/news-and-trends/newsletters/atisaca/2021/volume-36/five-key-considerations-when-applying-a-trust](https://www.isaca.org/resources/news-and-trends/newsletters/atisaca/2021/volume-36/five-key-considerations-when-applying-a-trust)  
128. Practice Innovations: Zero trust — Never trust, always verify \- Thomson Reuters Institute, acessado em junho 29, 2025, [https://www.thomsonreuters.com/en-us/posts/legal/practice-innovations-migrating-zero-trust/](https://www.thomsonreuters.com/en-us/posts/legal/practice-innovations-migrating-zero-trust/)  
129. What is Zero Trust? \- Guide to Zero Trust Security \- CrowdStrike.com, acessado em junho 29, 2025, [https://www.crowdstrike.com/en-us/cybersecurity-101/zero-trust-security/](https://www.crowdstrike.com/en-us/cybersecurity-101/zero-trust-security/)  
130. Understanding Trust and Security \- ResearchGate, acessado em junho 29, 2025, [https://www.researchgate.net/publication/2516627\_Understanding\_Trust\_and\_Security](https://www.researchgate.net/publication/2516627_Understanding_Trust_and_Security)  
131. Design and Verification of Secure Systems \- CiteSeerX, acessado em junho 29, 2025, [https://citeseerx.ist.psu.edu/document?repid=rep1\&type=pdf\&doi=d6be5acae89decbbbd5080bfc9a4fa2471cf5eb1](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=d6be5acae89decbbbd5080bfc9a4fa2471cf5eb1)  
132. The Ethics and Epistemology of Trust \- Internet Encyclopedia of Philosophy, acessado em junho 30, 2025, [https://iep.utm.edu/trust/](https://iep.utm.edu/trust/)  
133. Zero-knowledge proofs explained in 3 examples \- Circularise, acessado em junho 29, 2025, [https://www.circularise.com/blogs/zero-knowledge-proofs-explained-in-3-examples](https://www.circularise.com/blogs/zero-knowledge-proofs-explained-in-3-examples)  
134. ZPiE: Zero-Knowledge Proofs in Embedded Systems \- MDPI, acessado em junho 29, 2025, [https://www.mdpi.com/2227-7390/9/20/2569](https://www.mdpi.com/2227-7390/9/20/2569)  
135. Zero Knowledge Proof \- GeeksforGeeks, acessado em junho 29, 2025, [https://www.geeksforgeeks.org/computer-networks/zero-knowledge-proof/](https://www.geeksforgeeks.org/computer-networks/zero-knowledge-proof/)  
136. Zero-knowledge proof \- Wikipedia, acessado em junho 29, 2025, [https://en.wikipedia.org/wiki/Zero-knowledge\_proof](https://en.wikipedia.org/wiki/Zero-knowledge_proof)  
137. www.circularise.com, acessado em junho 29, 2025, [https://www.circularise.com/blogs/zero-knowledge-proofs-explained-in-3-examples\#:\~:text=They%20provide%20a%20definition%20of,this%20specific%20statement%20is%20true.%E2%80%9D](https://www.circularise.com/blogs/zero-knowledge-proofs-explained-in-3-examples#:~:text=They%20provide%20a%20definition%20of,this%20specific%20statement%20is%20true.%E2%80%9D)  
138. Zero-Knowledge Proofs — What Are They and Why Do They Matter? \- Medium, acessado em junho 29, 2025, [https://medium.com/@RocketMeUpCybersecurity/zero-knowledge-proofs-what-are-they-and-why-do-they-matter-9b103380e721](https://medium.com/@RocketMeUpCybersecurity/zero-knowledge-proofs-what-are-they-and-why-do-they-matter-9b103380e721)  
139. What is Zero-Knowledge Proof \- a hot technology bringing trustworthiness to Web3 privacy?, acessado em junho 29, 2025, [https://www.nttdata.com/global/en/insights/focus/2024/what-is-zero-knowledge-proof](https://www.nttdata.com/global/en/insights/focus/2024/what-is-zero-knowledge-proof)  
140. Zero-Knowledge Proofs | MIT CSAIL Theory of Computation, acessado em junho 29, 2025, [https://toc.csail.mit.edu/node/218](https://toc.csail.mit.edu/node/218)  
141. Understanding Zero-Knowledge Proofs and their impact on privacy: A simple guide, acessado em junho 29, 2025, [https://corporate-blog.global.fujitsu.com/fgb/2024-11-12/01/](https://corporate-blog.global.fujitsu.com/fgb/2024-11-12/01/)  
142. Example of a good Zero Knowledge Proof \- MathOverflow, acessado em junho 29, 2025, [https://mathoverflow.net/questions/22624/example-of-a-good-zero-knowledge-proof](https://mathoverflow.net/questions/22624/example-of-a-good-zero-knowledge-proof)  
143. How can I explain "zero knowledge proof" to an end user?, acessado em junho 29, 2025, [https://security.stackexchange.com/questions/86823/how-can-i-explain-zero-knowledge-proof-to-an-end-user](https://security.stackexchange.com/questions/86823/how-can-i-explain-zero-knowledge-proof-to-an-end-user)  
144. docs.succinct.xyz, acessado em junho 30, 2025, [https://docs.succinct.xyz/docs/sp1/what-is-a-zkvm\#:\~:text=A%20zero%2Dknowledge%20virtual%20machine,revealing%20how%20it%20did%20so.](https://docs.succinct.xyz/docs/sp1/what-is-a-zkvm#:~:text=A%20zero%2Dknowledge%20virtual%20machine,revealing%20how%20it%20did%20so.)  
145. What is zkVM? A Zero Knowledge Paradigm (Part 1\) \- Lita Foundation, acessado em junho 30, 2025, [https://www.lita.foundation/blog/zero-knowledge-paradigm-zkvm](https://www.lita.foundation/blog/zero-knowledge-paradigm-zkvm)  
146. What is a zkVM? \- Succinct Docs, acessado em junho 30, 2025, [https://docs.succinct.xyz/docs/sp1/what-is-a-zkvm](https://docs.succinct.xyz/docs/sp1/what-is-a-zkvm)  
147. The zkVM Wars | Jaeyong Park and Sam Lehman \- Symbolic Capital, acessado em junho 30, 2025, [https://www.symbolic.capital/writing/the-zkvm-wars](https://www.symbolic.capital/writing/the-zkvm-wars)  
148. An introduction to zero-knowledge virtual machines (zkVMs) | by Veridise \- Medium, acessado em junho 30, 2025, [https://veridise.medium.com/an-introduction-to-zero-knowledge-virtual-machines-zkvms-0e94b8023bca](https://veridise.medium.com/an-introduction-to-zero-knowledge-virtual-machines-zkvms-0e94b8023bca)  
149. How a ZKVM Works \- RareSkills, acessado em junho 30, 2025, [https://www.rareskills.io/post/zkvm](https://www.rareskills.io/post/zkvm)  
150. Nexus ZkVM | Incrementally Verifiable Computation | Code Review, acessado em junho 30, 2025, [https://research.tokenmetrics.com/nexus-zkvm-incrementally-verifiable-computation-code-review/](https://research.tokenmetrics.com/nexus-zkvm-incrementally-verifiable-computation-code-review/)  
151. Nexus zkVM 3.0 Specification \- Nexus.xyz, acessado em junho 30, 2025, [https://specification.nexus.xyz/](https://specification.nexus.xyz/)  
152. zkVM Testing Report: Evaluating Zero-Knowledge Virtual Machines for Nescience \- Vac, acessado em junho 30, 2025, [https://vac.dev/rlog/zkVM-testing](https://vac.dev/rlog/zkVM-testing)  
153. A Review of Folding Schemes. Introduction | by Eigen Network | Medium, acessado em junho 30, 2025, [https://eigenlab.medium.com/a-review-of-folding-schemes-a285a790fe2f](https://eigenlab.medium.com/a-review-of-folding-schemes-a285a790fe2f)  
154. Schemes for recursive proof composition \- Anoma | Research & Development Forum, acessado em junho 30, 2025, [https://research.anoma.net/t/schemes-for-recursive-proof-composition/440](https://research.anoma.net/t/schemes-for-recursive-proof-composition/440)  
155. Nova: Recursive Zero-Knowledge Arguments from Folding Schemes \- Cryptology ePrint Archive, acessado em junho 30, 2025, [https://eprint.iacr.org/2021/370.pdf](https://eprint.iacr.org/2021/370.pdf)  
156. SuperNova: Proving universal machine executions without universal circuits, acessado em junho 30, 2025, [https://eprint.iacr.org/2022/1758.pdf](https://eprint.iacr.org/2022/1758.pdf)  
157. lurk-lab/awesome-folding: A curated list of zero-knowledge folding schemes \- GitHub, acessado em junho 30, 2025, [https://github.com/lurk-lab/awesome-folding](https://github.com/lurk-lab/awesome-folding)  
158. SuperNova: Proving universal machine executions without universal circuits, acessado em junho 30, 2025, [https://eprint.iacr.org/2022/1758](https://eprint.iacr.org/2022/1758)  
159. SuperNova- Proving universal machine executions without universal circuits | PDF \- Scribd, acessado em junho 30, 2025, [https://www.scribd.com/document/860491482/SuperNova-Proving-universal-machine-executions-without-universal-circuits](https://www.scribd.com/document/860491482/SuperNova-Proving-universal-machine-executions-without-universal-circuits)  
160. README.md \- lurk-lang/arecibo \- GitHub, acessado em junho 30, 2025, [https://github.com/lurk-lang/arecibo/blob/dev/README.md](https://github.com/lurk-lang/arecibo/blob/dev/README.md)  
161. SuperNova: Revolutionizing Cryptographic Proof Systems for Program Executions, acessado em junho 30, 2025, [https://zkplabs.network/blog/supernova-revolutionizing-cryptographic-proof-systems-for-program-executions](https://zkplabs.network/blog/supernova-revolutionizing-cryptographic-proof-systems-for-program-executions)  
162. SNARK Recursion, Folding, and IVC | by Luca Franceschini | Medium, acessado em junho 30, 2025, [https://medium.com/@Luca\_Franceschini/snark-recursion-folding-and-ivc-135b98458a4d](https://medium.com/@Luca_Franceschini/snark-recursion-folding-and-ivc-135b98458a4d)  
163. blog.lambdaclass.com, acessado em junho 30, 2025, [https://blog.lambdaclass.com/incrementally-verifiable-computation-nova/\#:\~:text=This%20cryptographic%20primitive%20allows%20a,appropriately%20executed%20at%20every%20step.](https://blog.lambdaclass.com/incrementally-verifiable-computation-nova/#:~:text=This%20cryptographic%20primitive%20allows%20a,appropriately%20executed%20at%20every%20step.)  
164. Incrementally Verifiable Computation or Proofs of Knowledge Imply Time/Space Efficiency \- IACR, acessado em junho 30, 2025, [https://iacr.org/archive/tcc2008/49480001/49480001.pdf](https://iacr.org/archive/tcc2008/49480001/49480001.pdf)  
165. Incremental Verifiable Computation | Ask Dexa, acessado em junho 30, 2025, [https://dexa.ai/s/cb3235c2-4713-11ef-bb0d-4f7ae024086f](https://dexa.ai/s/cb3235c2-4713-11ef-bb0d-4f7ae024086f)  
166. Secp256k1 \- Bitcoin Wiki, acessado em junho 29, 2025, [https://en.bitcoin.it/wiki/Secp256k1](https://en.bitcoin.it/wiki/Secp256k1)  
167. Mechanisms of Resolution of Inflammation | Arteriosclerosis, Thrombosis, and Vascular Biology, acessado em junho 29, 2025, [https://www.ahajournals.org/doi/10.1161/atvbaha.110.213850](https://www.ahajournals.org/doi/10.1161/atvbaha.110.213850)  
168. Affective Computing in the Era of Large Language Models: A Survey from the NLP Perspective \- arXiv, acessado em junho 29, 2025, [https://arxiv.org/html/2408.04638v1](https://arxiv.org/html/2408.04638v1)  
169. Proof-Carrying Data without Succinct Arguments \- Cryptology ePrint Archive, acessado em junho 30, 2025, [https://eprint.iacr.org/2020/1618.pdf](https://eprint.iacr.org/2020/1618.pdf)  
170. Proof-Carrying Data and Hearsay Arguments from Signature Cards, acessado em junho 30, 2025, [https://ic-people.epfl.ch/\~achiesa/docs/CT10.pdf](https://ic-people.epfl.ch/~achiesa/docs/CT10.pdf)  
171. Proof-Carrying Data \- ResearchGate, acessado em junho 30, 2025, [https://www.researchgate.net/publication/260399696\_Proof-Carrying\_Data](https://www.researchgate.net/publication/260399696_Proof-Carrying_Data)  
172. Proof-Carrying Data From Arithmetized Random Oracles \- American Mathematical Society, acessado em junho 30, 2025, [https://meetings.ams.org/math/jmm2024/meetingapp.cgi/Paper/32127](https://meetings.ams.org/math/jmm2024/meetingapp.cgi/Paper/32127)  
173. Proof Carrying Data \- Pratyush Mishra at Zcon3 \- YouTube, acessado em junho 30, 2025, [https://www.youtube.com/watch?v=7MtzoVM6e6w](https://www.youtube.com/watch?v=7MtzoVM6e6w)  
174. What are Psychosomatic Autoimmune Diseases? | Maggie Yu MD, IFMCP, acessado em junho 29, 2025, [https://drmaggieyu.com/blog/what-are-psychosomatic-autoimmune-diseases/](https://drmaggieyu.com/blog/what-are-psychosomatic-autoimmune-diseases/)  
175. DAO Governance Models: What You Need to Know \- Metana, acessado em junho 30, 2025, [https://metana.io/blog/dao-governance-models-what-you-need-to-know/](https://metana.io/blog/dao-governance-models-what-you-need-to-know/)  
176. The fancy world of Accumulation Schemes \- HackMD, acessado em junho 30, 2025, [https://hackmd.io/@lrusso96/HJUU4QlDY](https://hackmd.io/@lrusso96/HJUU4QlDY)  
177. Proof-Carrying Data and Hearsay Arguments from Signature Cards \- MIT CSAIL, acessado em junho 30, 2025, [https://projects.csail.mit.edu/pcd/](https://projects.csail.mit.edu/pcd/)  
178. Benedikt Bünz: Proof-Carrying Data without Succinct Arguments \- YouTube, acessado em junho 30, 2025, [https://www.youtube.com/watch?v=CY84j0\_E7KA](https://www.youtube.com/watch?v=CY84j0_E7KA)  
179. Entropy and Negentropy Principles in the I-Theory \- Scientific Research Publishing, acessado em junho 30, 2025, [https://www.scirp.org/journal/paperinformation?paperid=99336](https://www.scirp.org/journal/paperinformation?paperid=99336)  
180. Oxygen consumption and the evolution of order: negentropy criteria applied to the evolution of ants \- ResearchGate, acessado em junho 30, 2025, [https://www.researchgate.net/publication/227061484\_Oxygen\_consumption\_and\_the\_evolution\_of\_order\_negentropy\_criteria\_applied\_to\_the\_evolution\_of\_ants](https://www.researchgate.net/publication/227061484_Oxygen_consumption_and_the_evolution_of_order_negentropy_criteria_applied_to_the_evolution_of_ants)  
181. Autopoiesis, Thermodynamics, and the Natural Drift of Living Beings: Another Way to the New Evolutionary Synthesis \- ResearchGate, acessado em junho 30, 2025, [https://www.researchgate.net/publication/361644301\_Autopoiesis\_Thermodynamics\_and\_the\_Natural\_Drift\_of\_Living\_Beings\_Another\_Way\_to\_the\_New\_Evolutionary\_Synthesis](https://www.researchgate.net/publication/361644301_Autopoiesis_Thermodynamics_and_the_Natural_Drift_of_Living_Beings_Another_Way_to_the_New_Evolutionary_Synthesis)  
182. Negentropism: An Ecological Theory of Value \- Murdoch Research Portal, acessado em junho 30, 2025, [https://researchportal.murdoch.edu.au/view/pdfCoverPage?instCode=61MUN\_INST\&filePid=13136778220007891\&download=true](https://researchportal.murdoch.edu.au/view/pdfCoverPage?instCode=61MUN_INST&filePid=13136778220007891&download=true)  
183. The thermodynamic meaning of negative entropy \- PubMed, acessado em junho 30, 2025, [https://pubmed.ncbi.nlm.nih.gov/21637254/](https://pubmed.ncbi.nlm.nih.gov/21637254/)  
184. Irreversibility \- chemeurope.com, acessado em junho 30, 2025, [https://www.chemeurope.com/en/encyclopedia/Irreversibility.html](https://www.chemeurope.com/en/encyclopedia/Irreversibility.html)  
185. Entropy and life \- Wikipedia, acessado em junho 30, 2025, [https://en.wikipedia.org/wiki/Entropy\_and\_life](https://en.wikipedia.org/wiki/Entropy_and_life)  
186. negentropic life, acessado em junho 30, 2025, [https://www.eoht.info/page/Negentropic%20life](https://www.eoht.info/page/Negentropic%20life)  
187. en.wikipedia.org, acessado em junho 30, 2025, [https://en.wikipedia.org/wiki/Entropy\_and\_life\#:\~:text=In%20the%201944%20book%20What,increase%20%E2%80%93%20decreases%20or%20keeps%20constant](https://en.wikipedia.org/wiki/Entropy_and_life#:~:text=In%20the%201944%20book%20What,increase%20%E2%80%93%20decreases%20or%20keeps%20constant)  
188. What is (Schrodinger's) Negentropy? \- THOLONIA, acessado em junho 30, 2025, [https://tholonia.com/material/material\_What\_is\_Schrodingers\_Negentropy.html](https://tholonia.com/material/material_What_is_Schrodingers_Negentropy.html)  
189. Answering Schrödinger's “What Is Life?” \- PMC \- PubMed Central, acessado em junho 30, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC7517386/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7517386/)  
190. What Is Life? Negative Entropy and the Gap Between Physics and Biology \- Dialektika, acessado em junho 30, 2025, [https://en.dialektika.org/science-technology/science/what-is-life-negative-entropy-and-gap-between-physics-biology/](https://en.dialektika.org/science-technology/science/what-is-life-negative-entropy-and-gap-between-physics-biology/)  
191. Negentropy \- Wikipedia, acessado em junho 30, 2025, [https://en.wikipedia.org/wiki/Negentropy](https://en.wikipedia.org/wiki/Negentropy)  
192. Organization as an Autopoietic System (Chapter 2\) \- Organization and Decision, acessado em junho 30, 2025, [https://www.cambridge.org/core/books/organization-and-decision/organization-as-an-autopoietic-system/99BFC0D9FF4992CF1C74A8C1CC7EDFE7](https://www.cambridge.org/core/books/organization-and-decision/organization-as-an-autopoietic-system/99BFC0D9FF4992CF1C74A8C1CC7EDFE7)  
193. Autopoiesis, Thermodynamics, and the Natural Drift of Living Beings: Another Way to the New Evolutionary Synthesis \- PubMed Central, acessado em junho 30, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC9317857/](https://pmc.ncbi.nlm.nih.gov/articles/PMC9317857/)  
194. physics.stackexchange.com, acessado em junho 30, 2025, [https://physics.stackexchange.com/questions/33030/second-law-of-thermodynamics-and-the-arrow-of-time-why-isnt-time-considered-fu\#:\~:text=I've%20come%20across%20this,of%20this%20increase%20in%20entropy.](https://physics.stackexchange.com/questions/33030/second-law-of-thermodynamics-and-the-arrow-of-time-why-isnt-time-considered-fu#:~:text=I've%20come%20across%20this,of%20this%20increase%20in%20entropy.)  
195. 2nd Law of Thermodynamics \- Chemistry LibreTexts, acessado em junho 30, 2025, [https://chem.libretexts.org/Bookshelves/Physical\_and\_Theoretical\_Chemistry\_Textbook\_Maps/Supplemental\_Modules\_(Physical\_and\_Theoretical\_Chemistry)/Thermodynamics/The\_Four\_Laws\_of\_Thermodynamics/Second\_Law\_of\_Thermodynamics](https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_\(Physical_and_Theoretical_Chemistry\)/Thermodynamics/The_Four_Laws_of_Thermodynamics/Second_Law_of_Thermodynamics)  
196. Thermodynamics and the Arrow of Time \- Puddles of Thought, acessado em junho 30, 2025, [https://puddlesofthought.blog/2024/01/05/thermodynamics-and-the-arrow-of-time/](https://puddlesofthought.blog/2024/01/05/thermodynamics-and-the-arrow-of-time/)  
197. Second law of thermodynamics and the arrow of time: why isn't time considered fundamental? \- Physics Stack Exchange, acessado em junho 30, 2025, [https://physics.stackexchange.com/questions/33030/second-law-of-thermodynamics-and-the-arrow-of-time-why-isnt-time-considered-fu](https://physics.stackexchange.com/questions/33030/second-law-of-thermodynamics-and-the-arrow-of-time-why-isnt-time-considered-fu)  
198. Tolerância e autoimunidade \- Faculdade de Medicina da Bahia |, acessado em junho 29, 2025, [http://www.medicina.ufba.br/imuno/roteiros\_imuno/tolerncia\_e\_autoimunidade.pdf](http://www.medicina.ufba.br/imuno/roteiros_imuno/tolerncia_e_autoimunidade.pdf)  
199. parte II: fundamentos da resposta imunológica mediada por linfócitos T e B Sistema imunitário \- SciELO, acessado em junho 29, 2025, [https://www.scielo.br/j/rbr/a/kPW8JNvSRfRy7RkdZVjW3tw/](https://www.scielo.br/j/rbr/a/kPW8JNvSRfRy7RkdZVjW3tw/)  
200. Seleção Timica | PPT \- SlideShare, acessado em junho 29, 2025, [https://pt.slideshare.net/slideshow/selecao-timica/2092287](https://pt.slideshare.net/slideshow/selecao-timica/2092287)  
201. Células T | Concise Medical Knowledge \- Lecturio, acessado em junho 29, 2025, [https://www.lecturio.com/pt/concepts/celulas-t/](https://www.lecturio.com/pt/concepts/celulas-t/)  
202. Questão Durante o desenvolvimento dos linfócitos T no timo, esse tipo celular passa por vários pontos de checagem imp... \- Estratégia MED, acessado em junho 29, 2025, [https://med.estrategia.com/public/questoes/Durante3964759313/](https://med.estrategia.com/public/questoes/Durante3964759313/)  
203. Questão Durante o desenvolvimento dos linfócitos T no timo, esse tipo celular passa por vários pontos de checagem imp, acessado em junho 29, 2025, [https://med.estrategia.com/public/questoes/Durante39d7b14340/](https://med.estrategia.com/public/questoes/Durante39d7b14340/)  
204. T cell tolerance by clonal elimination in the thymus \- PubMed, acessado em junho 30, 2025, [https://pubmed.ncbi.nlm.nih.gov/3494522/](https://pubmed.ncbi.nlm.nih.gov/3494522/)  
205. T Cell Tolerance by Clonal Elimination in the Thymus, acessado em junho 30, 2025, [https://www.umassmed.edu/globalassets/immunology-and-microbiology/documents/papers-for-bbs821-2015/kapplercellnegsel.pdf](https://www.umassmed.edu/globalassets/immunology-and-microbiology/documents/papers-for-bbs821-2015/kapplercellnegsel.pdf)  
206. Pillars Article: T Cell Tolerance by Clonal Elimination in the Thymus Cell, 1987, 49: 273–280 | The Journal of Immunology | Oxford Academic, acessado em junho 30, 2025, [https://academic.oup.com/jimmunol/article-abstract/174/7/3843/8036821](https://academic.oup.com/jimmunol/article-abstract/174/7/3843/8036821)  
207. Pillars Article: T Cell Tolerance by Clonal Elimination in the Thymus Cell, 1987, 49: 273–280. \- AAI Journals, acessado em junho 30, 2025, [https://journals.aai.org/jimmunol/article/174/7/3843/72840/Pillars-Article-T-Cell-Tolerance-by-Clonal](https://journals.aai.org/jimmunol/article/174/7/3843/72840/Pillars-Article-T-Cell-Tolerance-by-Clonal)  
208. T-Cell Tolerance: Central and Peripheral \- PMC, acessado em junho 30, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC3367546/](https://pmc.ncbi.nlm.nih.gov/articles/PMC3367546/)  
209. Pillars Article: T Cell Tolerance by Clonal Elimination in the Thymus Cell , 1987, 49: 273–280 | Request PDF \- ResearchGate, acessado em junho 30, 2025, [https://www.researchgate.net/publication/390304315\_Pillars\_Article\_T\_Cell\_Tolerance\_by\_Clonal\_Elimination\_in\_the\_Thymus\_Cell\_1987\_49\_273-280](https://www.researchgate.net/publication/390304315_Pillars_Article_T_Cell_Tolerance_by_Clonal_Elimination_in_the_Thymus_Cell_1987_49_273-280)  
210. T Cell Development, acessado em junho 29, 2025, [https://www2.nau.edu/\~fpm/immunology/Exams/Tcelldevelopment-401.html](https://www2.nau.edu/~fpm/immunology/Exams/Tcelldevelopment-401.html)  
211. Thymocyte \- Wikipedia, acessado em junho 29, 2025, [https://en.wikipedia.org/wiki/Thymocyte](https://en.wikipedia.org/wiki/Thymocyte)  
212. How do self-peptide-MHC presented during positive selection of thymocytes differ from those presented in negative selection in T-cell development? : r/Immunology \- Reddit, acessado em junho 29, 2025, [https://www.reddit.com/r/Immunology/comments/7tnxw4/how\_do\_selfpeptidemhc\_presented\_during\_positive/](https://www.reddit.com/r/Immunology/comments/7tnxw4/how_do_selfpeptidemhc_presented_during_positive/)  
213. Tolerância imunológica e Autoimunidade \- Coggle, acessado em junho 29, 2025, [https://coggle.it/diagram/XNH59GSy4JplFQf4/t/toler%C3%A2ncia-imunol%C3%B3gica-e-autoimunidade](https://coggle.it/diagram/XNH59GSy4JplFQf4/t/toler%C3%A2ncia-imunol%C3%B3gica-e-autoimunidade)  
214. Elimination of Self-Reactive T Cells in the Thymus: A Timeline for Negative Selection \- PLOS, acessado em junho 29, 2025, [https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001566](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001566)  
215. T cell selection in the thymus: a spatial and temporal perspective \- PMC \- PubMed Central, acessado em junho 29, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC4938245/](https://pmc.ncbi.nlm.nih.gov/articles/PMC4938245/)  
216. Security Vulnerabilities in ZK \- ZKV, acessado em junho 30, 2025, [https://zkv.xyz/security-vulnerabilities-in-zk/](https://zkv.xyz/security-vulnerabilities-in-zk/)  
217. O que é: Tolerância imunológica \- Terencio Advocacia, acessado em junho 29, 2025, [https://www.terencioadvocacia.com.br/glossario/o-que-e-tolerancia-imunologica/](https://www.terencioadvocacia.com.br/glossario/o-que-e-tolerancia-imunologica/)  
218. ICSA17 \- Tolerância | PPT \- SlideShare, acessado em junho 29, 2025, [https://pt.slideshare.net/rwportela1/tolerncia-30880009](https://pt.slideshare.net/rwportela1/tolerncia-30880009)  
219. Imunologia Básica \-Mecanismos de Tolerância Imunológica \- YouTube, acessado em junho 29, 2025, [https://www.youtube.com/watch?v=sRBX7J8VV-g](https://www.youtube.com/watch?v=sRBX7J8VV-g)  
220. Antigen-specific interaction between T and B cells \- PubMed, acessado em junho 29, 2025, [https://pubmed.ncbi.nlm.nih.gov/3157869/](https://pubmed.ncbi.nlm.nih.gov/3157869/)  
221. The many Achilles' heels of B and T cell tolerance \- PMC \- PubMed Central, acessado em junho 29, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC8986605/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8986605/)  
222. The Clonal Selection Theory: what it really is and why modern challenges are misplaced, acessado em junho 30, 2025, [https://www.researchgate.net/publication/11184150\_The\_Clonal\_Selection\_Theory\_what\_it\_really\_is\_and\_why\_modern\_challenges\_are\_misplaced](https://www.researchgate.net/publication/11184150_The_Clonal_Selection_Theory_what_it_really_is_and_why_modern_challenges_are_misplaced)  
223. Tolerância imunológica – Wikipédia, a enciclopédia livre, acessado em junho 29, 2025, [https://pt.wikipedia.org/wiki/Toler%C3%A2ncia\_imunol%C3%B3gica](https://pt.wikipedia.org/wiki/Toler%C3%A2ncia_imunol%C3%B3gica)  
224. Approaches to Establishing Tolerance in Immune Mediated Diseases \- PMC, acessado em junho 29, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC8488342/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8488342/)  
225. Memória imunológica. A memória imunológica do nosso organismo \- Mundo Educação, acessado em junho 29, 2025, [https://mundoeducacao.uol.com.br/biologia/memoria-imunologica.htm](https://mundoeducacao.uol.com.br/biologia/memoria-imunologica.htm)  
226. The Clonal Selection Theory of Acquired Immunity by Sir Macfarlane Burnet: Very Good \+ Cloth (1959) | APPLEDORE BOOKS, ABAA \- AbeBooks, acessado em junho 30, 2025, [https://www.abebooks.com/first-edition/Clonal-Selection-Theory-Acquired-Immunity-Sir/32126669707/bd](https://www.abebooks.com/first-edition/Clonal-Selection-Theory-Acquired-Immunity-Sir/32126669707/bd)  
227. Common Vulnerabilities in ZK Proof | by Oxorio, acessado em junho 30, 2025, [https://blog.oxor.io/common-vulnerabilities-in-zk-proof-5ba7620dfa2f](https://blog.oxor.io/common-vulnerabilities-in-zk-proof-5ba7620dfa2f)  
228. MTZK: Testing and Exploring Bugs in Zero-Knowledge (ZK) Compilers \- Network and Distributed System Security (NDSS) Symposium, acessado em junho 30, 2025, [https://www.ndss-symposium.org/wp-content/uploads/2025-530-paper.pdf](https://www.ndss-symposium.org/wp-content/uploads/2025-530-paper.pdf)  
229. 0xPARC/zk-bug-tracker: A community-maintained collection of bugs, vulnerabilities, and exploits in apps using ZK crypto. \- GitHub, acessado em junho 30, 2025, [https://github.com/0xPARC/zk-bug-tracker](https://github.com/0xPARC/zk-bug-tracker)  
230. SoK: What don't we know? Understanding Security Vulnerabilities in SNARKs \- arXiv, acessado em junho 30, 2025, [https://arxiv.org/html/2402.15293v1](https://arxiv.org/html/2402.15293v1)  
231. Strategies to Prevent 'Garbage In, Garbage Out' in AI Applications | by Dickson Lukose, acessado em junho 30, 2025, [https://medium.com/@dickson.lukose/garbage-in-garbage-out-why-data-quality-is-the-key-to-trustworthy-ai-e506f4001433](https://medium.com/@dickson.lukose/garbage-in-garbage-out-why-data-quality-is-the-key-to-trustworthy-ai-e506f4001433)  
232. “Garbage In, Garbage Out” \- Deepdesk, acessado em junho 30, 2025, [https://deepdesk.com/blog/garbage-in-garbage-out](https://deepdesk.com/blog/garbage-in-garbage-out)  
233. Garbage in, garbage out: Why data quality is critical to AI \- Saifr, acessado em junho 30, 2025, [https://saifr.ai/blog/garbage-in-garbage-out-why-data-quality-is-critical-to-ai](https://saifr.ai/blog/garbage-in-garbage-out-why-data-quality-is-critical-to-ai)  
234. “Garbage In, Garbage Out”: How to Stop Your AI from Hallucinating \- Shelf.io, acessado em junho 30, 2025, [https://shelf.io/blog/garbage-in-garbage-out-ai-implementation/](https://shelf.io/blog/garbage-in-garbage-out-ai-implementation/)  
235. The Garbage In Garbage Out Nature of Machine Learning and AI \- Cisco Community, acessado em junho 30, 2025, [https://community.cisco.com/t5/devnet-general-discussions/the-garbage-in-garbage-out-nature-of-machine-learning-and-ai/td-p/4873671](https://community.cisco.com/t5/devnet-general-discussions/the-garbage-in-garbage-out-nature-of-machine-learning-and-ai/td-p/4873671)  
236. Garbage In, Garbage Out: The Potential Pitfalls Of Artificial Intelligence, acessado em junho 30, 2025, [https://artsci.tamu.edu/news/2023/01/garbage-in-garbage-out-the-potential-pitfalls-of-artificial-intelligence.html](https://artsci.tamu.edu/news/2023/01/garbage-in-garbage-out-the-potential-pitfalls-of-artificial-intelligence.html)  
237. Formal Methods for the Verification of Smart Contracts: A Review \- ResearchGate, acessado em junho 30, 2025, [https://www.researchgate.net/publication/365028982\_Formal\_Methods\_for\_the\_Verification\_of\_Smart\_Contracts\_A\_Review](https://www.researchgate.net/publication/365028982_Formal_Methods_for_the_Verification_of_Smart_Contracts_A_Review)  
238. What Is Formal Verification In Smart Contract Auditing? \- Hashlock, acessado em junho 30, 2025, [https://hashlock.com/blog/what-is-formal-verification-in-smart-contract-auditing](https://hashlock.com/blog/what-is-formal-verification-in-smart-contract-auditing)  
239. What is Formal Verification in Smart Contract Auditing? \- CertiK, acessado em junho 30, 2025, [https://www.certik.com/resources/blog/what-is-formal-verification](https://www.certik.com/resources/blog/what-is-formal-verification)  
240. Formal verification on smart contracts \- OpenTezos, acessado em junho 30, 2025, [https://opentezos.com/formal-verification/modeling-theorem/](https://opentezos.com/formal-verification/modeling-theorem/)  
241. Formal Verification in Cryptocurrencies \- Boosty Labs, acessado em junho 30, 2025, [https://boostylabs.com/blog/formal-verification](https://boostylabs.com/blog/formal-verification)  
242. Validity, Liquidity, and Fidelity: Formal Verification for Smart Contracts in Cardano \- DROPS, acessado em junho 30, 2025, [https://drops.dagstuhl.de/storage/01oasics/oasics-vol129-fmbc2025/OASIcs.FMBC.2025.6/OASIcs.FMBC.2025.6.pdf](https://drops.dagstuhl.de/storage/01oasics/oasics-vol129-fmbc2025/OASIcs.FMBC.2025.6/OASIcs.FMBC.2025.6.pdf)  
243. Security Vulnerabilities Difficult To Detect In Verification Flow \- Semiconductor Engineering, acessado em junho 30, 2025, [https://semiengineering.com/security-vulnerabilities-difficult-to-detect-in-verification-flow/](https://semiengineering.com/security-vulnerabilities-difficult-to-detect-in-verification-flow/)  
244. Why fuzzing over formal verification? \- The Trail of Bits Blog, acessado em junho 30, 2025, [https://blog.trailofbits.com/2024/03/22/why-fuzzing-over-formal-verification/](https://blog.trailofbits.com/2024/03/22/why-fuzzing-over-formal-verification/)  
245. A general picture of formal verification in software \- Computer Science Stack Exchange, acessado em junho 30, 2025, [https://cs.stackexchange.com/questions/127509/a-general-picture-of-formal-verification-in-software](https://cs.stackexchange.com/questions/127509/a-general-picture-of-formal-verification-in-software)  
246. Decentralised Autonomous Organizations: Targeting the Potential Beyond the Hype, acessado em junho 29, 2025, [https://competitionlab.gwu.edu/decentralised-autonomous-organizations-targeting-potential-beyond-hype](https://competitionlab.gwu.edu/decentralised-autonomous-organizations-targeting-potential-beyond-hype)  
247. Decentralized Autonomous Organizations \- DAOs: the Convergence of Technology, Law, Governance, and Behavioral Economics, acessado em junho 29, 2025, [https://law.mit.edu/pub/decentralizedautonomousorganizations](https://law.mit.edu/pub/decentralizedautonomousorganizations)  
248. Decentralized autonomous organization \- Wikipedia, acessado em junho 30, 2025, [https://en.wikipedia.org/wiki/Decentralized\_autonomous\_organization](https://en.wikipedia.org/wiki/Decentralized_autonomous_organization)  
249. A Critical Review of Efficient Market Hypothesis and Behavioral Finan, acessado em junho 29, 2025, [https://www.ewadirect.com/proceedings/aemps/article/view/5797/pdf](https://www.ewadirect.com/proceedings/aemps/article/view/5797/pdf)  
250. The Ethnography of a 'Decentralized Autonomous Organization' (DAO): De-mystifying Algorithmic Systems \- EPIC people, acessado em junho 29, 2025, [https://www.epicpeople.org/ethnography-of-decentralized-autonomous-organization/](https://www.epicpeople.org/ethnography-of-decentralized-autonomous-organization/)  
251. Decentralized Autonomous Organizations and Policy Considerations in the United States, acessado em junho 29, 2025, [https://www.belfercenter.org/publication/decentralized-autonomous-organizations-and-policy-considerations-united-states](https://www.belfercenter.org/publication/decentralized-autonomous-organizations-and-policy-considerations-united-states)  
252. What is a DAO, or decentralized autonomous organization? \- University of Miami News, acessado em junho 29, 2025, [https://news.miami.edu/stories/2023/02/what-is-a-dao-or-decentralized-autonomous-organization.html](https://news.miami.edu/stories/2023/02/what-is-a-dao-or-decentralized-autonomous-organization.html)  
253. Decentralized Autonomous Organization | Internet Policy Review, acessado em junho 30, 2025, [https://policyreview.info/glossary/DAO](https://policyreview.info/glossary/DAO)  
254. Decentralised autonomous organisation \- Internet Policy Review, acessado em junho 30, 2025, [https://policyreview.info/open-abstracts/decentralised-autonomous-organisation](https://policyreview.info/open-abstracts/decentralised-autonomous-organisation)  
255. Decentralized Autonomous Organizations (DAOs): The Future of Collective Governance, acessado em junho 30, 2025, [https://uppcsmagazine.com/decentralized-autonomous-organizations-daos-the-future-of-collective-governance/](https://uppcsmagazine.com/decentralized-autonomous-organizations-daos-the-future-of-collective-governance/)  
256. On-Chain Governance Definition | CoinMarketCap, acessado em junho 30, 2025, [https://coinmarketcap.com/academy/glossary/on-chain-governance](https://coinmarketcap.com/academy/glossary/on-chain-governance)  
257. On-Chain Governance \- Coinmetro, acessado em junho 30, 2025, [https://coinmetro.com/glossary/on-chain-governance](https://coinmetro.com/glossary/on-chain-governance)  
258. Blockchain Governance: Ultimate Guide to On-Chain & Off-Chain Models (2024), acessado em junho 30, 2025, [https://www.rapidinnovation.io/post/blockchain-governance-models-compared-on-chain-vs-off-chain-decision-making](https://www.rapidinnovation.io/post/blockchain-governance-models-compared-on-chain-vs-off-chain-decision-making)  
259. What is On-Chain Governance? Definition & Meaning | Crypto Wiki \- BitDegree, acessado em junho 30, 2025, [https://www.bitdegree.org/crypto/learn/crypto-terms/what-is-on-chain-governance](https://www.bitdegree.org/crypto/learn/crypto-terms/what-is-on-chain-governance)  
260. education.district0x.io, acessado em junho 30, 2025, [https://education.district0x.io/general-topics/what-is-governance/on-chain-governance/\#:\~:text=On%2Dchain%20governance%20is%20a,be%20integrated%20into%20the%20protocol.](https://education.district0x.io/general-topics/what-is-governance/on-chain-governance/#:~:text=On%2Dchain%20governance%20is%20a,be%20integrated%20into%20the%20protocol.)  
261. On-Chain Governance: Definition, Types, vs. Off-Chain \- Investopedia, acessado em junho 30, 2025, [https://www.investopedia.com/terms/o/onchain-governance.asp](https://www.investopedia.com/terms/o/onchain-governance.asp)  
262. Decentralizing governance: exploring the dynamics and challenges of digital commons and DAOs \- Frontiers, acessado em junho 30, 2025, [https://www.frontiersin.org/journals/blockchain/articles/10.3389/fbloc.2025.1538227/full](https://www.frontiersin.org/journals/blockchain/articles/10.3389/fbloc.2025.1538227/full)  
263. DAO Research Trends: Reflections and Learnings from the First European DAO Workshop (DAWO) \- MDPI, acessado em junho 30, 2025, [https://www.mdpi.com/2076-3417/15/7/3491](https://www.mdpi.com/2076-3417/15/7/3491)  
264. DAO Governance: Mechanisms, Architecture, and Implementation | by Garima singh, acessado em junho 30, 2025, [https://medium.com/@garima.miet/dao-governance-mechanisms-architecture-and-implementation-16e46c856c3f](https://medium.com/@garima.miet/dao-governance-mechanisms-architecture-and-implementation-16e46c856c3f)  
265. Paradox of Power: How DAOs Struggle with Centralization and Ineffective Leadership \- BeInCrypto, acessado em junho 29, 2025, [https://beincrypto.com/dao-governance-challenges-long-term-viability/](https://beincrypto.com/dao-governance-challenges-long-term-viability/)  
266. Delegated voting in decentralized autonomous organizations: a scoping review \- Frontiers, acessado em junho 30, 2025, [https://www.frontiersin.org/journals/blockchain/articles/10.3389/fbloc.2025.1598283/full](https://www.frontiersin.org/journals/blockchain/articles/10.3389/fbloc.2025.1598283/full)  
267. Designing Community Governance – Learnings from DAOs \- The Journal of The British Blockchain Association, acessado em junho 30, 2025, [https://jbba.scholasticahq.com/article/133242.pdf](https://jbba.scholasticahq.com/article/133242.pdf)  
268. A Review of DAO Governance: Recent Literature and Emerging Trends \- ResearchGate, acessado em junho 30, 2025, [https://www.researchgate.net/publication/388691320\_A\_Review\_of\_DAO\_Governance\_Recent\_Literature\_and\_Emerging\_Trends](https://www.researchgate.net/publication/388691320_A_Review_of_DAO_Governance_Recent_Literature_and_Emerging_Trends)  
269. Delegated Voting: Empowering Decentralized Decision-Making \- Colony Blog, acessado em junho 30, 2025, [https://blog.colony.io/delegated-voting-empowering-decentralized-decision-making/](https://blog.colony.io/delegated-voting-empowering-decentralized-decision-making/)  
270. Governance and Management of Autonomous Organizations, acessado em junho 29, 2025, [https://www.ecgi.global/sites/default/files/working\_papers/documents/governanceandmanagementofautonomousorganizations.pdf](https://www.ecgi.global/sites/default/files/working_papers/documents/governanceandmanagementofautonomousorganizations.pdf)  
271. The Rise of Automated Companies: Navigating the New Business, acessado em junho 29, 2025, [https://www.alphanome.ai/post/the-rise-of-automated-companies-navigating-the-new-business-frontier](https://www.alphanome.ai/post/the-rise-of-automated-companies-navigating-the-new-business-frontier)  
272. Governance and Management of Autonomous Organizations, acessado em junho 30, 2025, [https://www.fmg.ac.uk/fre/publications/discussion-papers/governance-and-management-autonomous-organizations](https://www.fmg.ac.uk/fre/publications/discussion-papers/governance-and-management-autonomous-organizations)  
273. Blockchain Trilemma Definition \- CoinMarketCap, acessado em junho 30, 2025, [https://coinmarketcap.com/academy/glossary/blockchain-trilemma](https://coinmarketcap.com/academy/glossary/blockchain-trilemma)  
274. A Book About Blockchain\[Book\] \- O'Reilly, acessado em junho 30, 2025, [https://www.oreilly.com/library/view/a-book-about/9781953349392/](https://www.oreilly.com/library/view/a-book-about/9781953349392/)  
275. Blockchain-Assisted Self-Sovereign Identities on Education: A Survey \- MDPI, acessado em junho 30, 2025, [https://www.mdpi.com/2813-5288/3/1/3](https://www.mdpi.com/2813-5288/3/1/3)  
276. DECENTRALIZED AUTONOMOUS ORGANIZATION TO AUTOMATE GOVERNANCE 1\. Introduction Corporate entities of all kinds are governed by rul, acessado em junho 29, 2025, [https://lawofthelevel.lexblogplatformthree.com/wp-content/uploads/sites/187/2017/07/WhitePaper-1.pdf](https://lawofthelevel.lexblogplatformthree.com/wp-content/uploads/sites/187/2017/07/WhitePaper-1.pdf)  
277. Forks in Blockchain: A Deep Dive \- Number Analytics, acessado em junho 29, 2025, [https://www.numberanalytics.com/blog/deep-dive-into-forks-in-blockchain](https://www.numberanalytics.com/blog/deep-dive-into-forks-in-blockchain)  
278. Blockchain Forks: A Formal Classification Framework and Persistency Analysis \- Munich Personal RePEc Archive, acessado em junho 29, 2025, [https://mpra.ub.uni-muenchen.de/101712/1/MPRA\_paper\_101712.pdf](https://mpra.ub.uni-muenchen.de/101712/1/MPRA_paper_101712.pdf)  
279. What Was the DAO Hack? \- Gemini, acessado em junho 30, 2025, [https://www.gemini.com/cryptopedia/the-dao-hack-makerdao](https://www.gemini.com/cryptopedia/the-dao-hack-makerdao)  
280. What Was The DAO? Story of Infamous Hack \- Liquidity Provider, acessado em junho 30, 2025, [https://liquidity-provider.com/articles/what-was-the-dao-the-story-of-infamous-hack/](https://liquidity-provider.com/articles/what-was-the-dao-the-story-of-infamous-hack/)  
281. (PDF) Blockchain Forks: A Formal Classification Framework and Persistency Analysis, acessado em junho 29, 2025, [https://www.researchgate.net/publication/339461094\_Blockchain\_Forks\_A\_Formal\_Classification\_Framework\_and\_Persistency\_Analysis](https://www.researchgate.net/publication/339461094_Blockchain_Forks_A_Formal_Classification_Framework_and_Persistency_Analysis)  
282. \[2205.07478\] Estimating Patch Propagation Times across (Blockchain) Forks \- arXiv, acessado em junho 29, 2025, [https://arxiv.org/abs/2205.07478](https://arxiv.org/abs/2205.07478)  
283. A Broad Overview of Reentrancy Attacks in Solidity Contracts | QuickNode Guides, acessado em junho 30, 2025, [https://www.quicknode.com/guides/ethereum-development/smart-contracts/a-broad-overview-of-reentrancy-attacks-in-solidity-contracts](https://www.quicknode.com/guides/ethereum-development/smart-contracts/a-broad-overview-of-reentrancy-attacks-in-solidity-contracts)  
284. Solidity Tutorial on Reentrancy Attacks in Smart Contracts \- Cyfrin, acessado em junho 30, 2025, [https://www.cyfrin.io/blog/what-is-a-reentrancy-attack-solidity-smart-contracts](https://www.cyfrin.io/blog/what-is-a-reentrancy-attack-solidity-smart-contracts)  
285. Understanding a Revolutionary and Flawed Grand Experiment in Blockchain: The DAO Attack | Request PDF \- ResearchGate, acessado em junho 30, 2025, [https://www.researchgate.net/publication/330050874\_Understanding\_a\_Revolutionary\_and\_Flawed\_Grand\_Experiment\_in\_Blockchain\_The\_DAO\_Attack](https://www.researchgate.net/publication/330050874_Understanding_a_Revolutionary_and_Flawed_Grand_Experiment_in_Blockchain_The_DAO_Attack)  
286. Reentrancy Attack: Risks, Impact, And Prevention In Smart Contracts \- Hacken, acessado em junho 30, 2025, [https://hacken.io/discover/reentrancy-attacks/](https://hacken.io/discover/reentrancy-attacks/)  
287. Uncover the Premeditated Attacks: Detecting Exploitable Reentrancy Vulnerabilities by Identifying Attacker Contracts \- arXiv, acessado em junho 30, 2025, [https://arxiv.org/html/2403.19112v1](https://arxiv.org/html/2403.19112v1)  
288. A call for a Temporary Moratorium on the DAO : r/ethereum \- Reddit, acessado em junho 30, 2025, [https://www.reddit.com/r/ethereum/comments/4lcito/a\_call\_for\_a\_temporary\_moratorium\_on\_the\_dao/](https://www.reddit.com/r/ethereum/comments/4lcito/a_call_for_a_temporary_moratorium_on_the_dao/)  
289. A Call For A Temporary Moratorium On "The DAO" | PDF | Venture Capital \- Scribd, acessado em junho 30, 2025, [https://www.scribd.com/doc/314170161/A-Call-for-a-Temporary-Moratorium-on-the-DAO](https://www.scribd.com/doc/314170161/A-Call-for-a-Temporary-Moratorium-on-the-DAO)  
290. A Call for a Temporary Moratorium on The DAO : r/TheDao \- Reddit, acessado em junho 30, 2025, [https://www.reddit.com/r/TheDao/comments/4lcin6/a\_call\_for\_a\_temporary\_moratorium\_on\_the\_dao/](https://www.reddit.com/r/TheDao/comments/4lcin6/a_call_for_a_temporary_moratorium_on_the_dao/)  
291. The DAO, acessado em junho 30, 2025, [https://dao.consider.it/](https://dao.consider.it/)  
292. Malicious Life Podcast: The Ethereum DAO Hack \- Cybereason, acessado em junho 30, 2025, [https://www.cybereason.com/blog/malicious-life-podcast-the-ethereum-dao-hack](https://www.cybereason.com/blog/malicious-life-podcast-the-ethereum-dao-hack)  
293. JOURNAL OF INTELLECTUAL PROPERTY AND ENTERTAINMENT LAW, acessado em junho 30, 2025, [https://jipel.law.nyu.edu/wp-content/uploads/2020/01/Minn\_Article.pdf](https://jipel.law.nyu.edu/wp-content/uploads/2020/01/Minn_Article.pdf)  
294. Code is Law: Code is Law: The Philosophical Battle Between Ethereum and Ethereum Classic \- FasterCapital, acessado em junho 30, 2025, [https://www.fastercapital.com/content/Code-is-Law--Code-is-Law--The-Philosophical-Battle-Between-Ethereum-and-Ethereum-Classic.html](https://www.fastercapital.com/content/Code-is-Law--Code-is-Law--The-Philosophical-Battle-Between-Ethereum-and-Ethereum-Classic.html)  
295. Ethereum's Social Consensus vs Ethereum Classic's Code Is Law, acessado em junho 30, 2025, [https://ethereumclassic.org/blog/2023-01-25-ethereums-social-consensus-vs-ethereum-classics-code-is-law/](https://ethereumclassic.org/blog/2023-01-25-ethereums-social-consensus-vs-ethereum-classics-code-is-law/)  
296. Client Alert: "Code is Law" \- Quinn Emanuel, acessado em junho 30, 2025, [https://www.quinnemanuel.com/the-firm/publications/code-is-law/](https://www.quinnemanuel.com/the-firm/publications/code-is-law/)  
297. ethereumclassic.org, acessado em junho 30, 2025, [https://ethereumclassic.org/blog/2023-01-25-ethereums-social-consensus-vs-ethereum-classics-code-is-law/\#:\~:text=In%20Ethereum%20Classic%20the%20term,Social%20Consensus%20must%20escape%20it.](https://ethereumclassic.org/blog/2023-01-25-ethereums-social-consensus-vs-ethereum-classics-code-is-law/#:~:text=In%20Ethereum%20Classic%20the%20term,Social%20Consensus%20must%20escape%20it.)  
298. The DAO Hack of 2016: Ethereum's $50 Million Nightmare and Its Lasting Impact on DeFi, Law, and Policy \- Diego Latorre., acessado em junho 30, 2025, [https://latorreabogado.medium.com/the-dao-hack-of-2016-ethereums-50-million-nightmare-and-its-lasting-impact-on-defi-law-and-ef0c494440d4](https://latorreabogado.medium.com/the-dao-hack-of-2016-ethereums-50-million-nightmare-and-its-lasting-impact-on-defi-law-and-ef0c494440d4)  
299. How the DAO Hack Changed Ethereum \- YouTube, acessado em junho 30, 2025, [https://www.youtube.com/watch?v=unOp-r4-YrE](https://www.youtube.com/watch?v=unOp-r4-YrE)  
300. CASE STUDY: Ethereum Hardfork in The DAO crisis in 2016\. Takeaways \- YouTube, acessado em junho 30, 2025, [https://www.youtube.com/watch?v=D3AyOmW0TPk](https://www.youtube.com/watch?v=D3AyOmW0TPk)  
301. Deep Dive into DAOs: the practical risks of existing nowhere \- DAC Beachcroft, acessado em junho 30, 2025, [https://www.dacbeachcroft.com/en/What-we-think/Deep-dive-into-daos-the-practical-risks-of-existing-nowhere](https://www.dacbeachcroft.com/en/What-we-think/Deep-dive-into-daos-the-practical-risks-of-existing-nowhere)  
302. Why Eth Sucks | Story of the DAO Hack, Hard Fork, and Its very mutable Ledger \- YouTube, acessado em junho 30, 2025, [https://www.youtube.com/watch?v=2C0AwG5y8VQ](https://www.youtube.com/watch?v=2C0AwG5y8VQ)  
303. An Insight into the DAO Attack \- ImmuneBytes, acessado em junho 30, 2025, [https://immunebytes.com/blog/an-insight-into-the-dao-attack/](https://immunebytes.com/blog/an-insight-into-the-dao-attack/)  
304. The DAO \- Wikipedia, acessado em junho 30, 2025, [https://en.wikipedia.org/wiki/The\_DAO](https://en.wikipedia.org/wiki/The_DAO)  
305. ETC vs ETH: Which One Is Better? \- Moralis Academy, acessado em junho 30, 2025, [https://academy.moralis.io/blog/ethereum-vs-ethereum-classic-whats-the-difference](https://academy.moralis.io/blog/ethereum-vs-ethereum-classic-whats-the-difference)  
306. Understanding Autoimmunity: Mechanisms, Predisposing Factors, and Cytokine Therapies, acessado em junho 29, 2025, [https://www.mdpi.com/1422-0067/25/14/7666](https://www.mdpi.com/1422-0067/25/14/7666)  
307. 4\. Breaking Tolerance: Autoimmunity & Dysregulation \- Immunopaedia, acessado em junho 29, 2025, [https://www.immunopaedia.org.za/immunology/advanced/4-breaking-tolerance-autoimmunity-dysregulation/](https://www.immunopaedia.org.za/immunology/advanced/4-breaking-tolerance-autoimmunity-dysregulation/)  
308. Immune tolerance and the prevention of autoimmune diseases essentially depend on thymic tissue homeostasis \- Frontiers, acessado em junho 29, 2025, [https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2024.1339714/full](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2024.1339714/full)  
309. 6\. Tolerance and Autoimmunity \- Immunopaedia, acessado em junho 29, 2025, [https://www.immunopaedia.org.za/immunology/special-focus-area/6-tolerance-and-autoimmunity/](https://www.immunopaedia.org.za/immunology/special-focus-area/6-tolerance-and-autoimmunity/)  
310. Tolerance and autoimmunity \- PMC \- PubMed Central, acessado em junho 29, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC1071274/](https://pmc.ncbi.nlm.nih.gov/articles/PMC1071274/)  
311. Autoimmune disease \- Wikipedia, acessado em junho 29, 2025, [https://en.wikipedia.org/wiki/Autoimmune\_disease](https://en.wikipedia.org/wiki/Autoimmune_disease)  
312. Autoimmune diseases: the failure of self tolerance \- PubMed, acessado em junho 29, 2025, [https://pubmed.ncbi.nlm.nih.gov/1972595/](https://pubmed.ncbi.nlm.nih.gov/1972595/)  
313. Chaos Reigns as ConstitutionDAO Fails to Buy the Constitution \- VICE, acessado em junho 30, 2025, [https://www.vice.com/en/article/chaos-reigns-as-constitutiondao-fails-to-buy-the-constitution/](https://www.vice.com/en/article/chaos-reigns-as-constitutiondao-fails-to-buy-the-constitution/)  
314. Imperfect Union: How ConstitutionDAO Lost Its Way \- Fwb.help, acessado em junho 30, 2025, [https://www.fwb.help/editorial/imperfect-union-how-constitutiondao-lost-its-way](https://www.fwb.help/editorial/imperfect-union-how-constitutiondao-lost-its-way)  
315. ConstitutionDAO: The Unexpected Aftermath of a Failed Bid \- MIDAO, acessado em junho 30, 2025, [https://www.midao.org/blog-posts/constitutiondao-the-unexpected-aftermath-of-a-failed-bid](https://www.midao.org/blog-posts/constitutiondao-the-unexpected-aftermath-of-a-failed-bid)  
316. The ConstitutionDAO: redefining crowdfunding in the age of decentralized finance | Emerald Insight, acessado em junho 30, 2025, [https://www.emerald.com/insight/content/doi/10.1108/TCJ-12-2024-0364/full/html](https://www.emerald.com/insight/content/doi/10.1108/TCJ-12-2024-0364/full/html)  
317. ConstitutionDAO: A Complete Timeline Leading up to the Bid \- CoinMarketCap, acessado em junho 30, 2025, [https://coinmarketcap.com/academy/article/constitutiondao](https://coinmarketcap.com/academy/article/constitutiondao)  
318. Moderating the ConstitutionDAO: Managing a Massive Community \- Social Media Examiner, acessado em junho 30, 2025, [https://www.socialmediaexaminer.com/moderating-the-constitutiondao-managing-a-massive-community/](https://www.socialmediaexaminer.com/moderating-the-constitutiondao-managing-a-massive-community/)  
319. ConstitutionDAO Is Shutting Down After Unrelenting Chaos \- VICE, acessado em junho 30, 2025, [https://www.vice.com/en/article/constitutiondao-is-shutting-down-after-unrelenting-chaos/](https://www.vice.com/en/article/constitutiondao-is-shutting-down-after-unrelenting-chaos/)  
320. ConstitutionDAO Will Shut Down After Raising $49M \- Blockworks, acessado em junho 30, 2025, [https://blockworks.co/news/constitutiondao-shutting-down-after-raising-49m](https://blockworks.co/news/constitutiondao-shutting-down-after-raising-49m)  
321. ConsitutionDAO to shut down after failing to purchase the US constitution By BTC Peers, acessado em junho 30, 2025, [https://www.investing.com/news/cryptocurrency-news/consitutiondao-to-shut-down-after-failing-to-purchase-the-us-constitution-2689810](https://www.investing.com/news/cryptocurrency-news/consitutiondao-to-shut-down-after-failing-to-purchase-the-us-constitution-2689810)  
322. ConstitutionDAO, acessado em junho 30, 2025, [https://www.constitutiondao.com/](https://www.constitutiondao.com/)  
323. ConstitutionDAO (PEOPLE) \- DAOs \- IQ.wiki, acessado em junho 30, 2025, [https://iq.wiki/wiki/constitutiondao-people](https://iq.wiki/wiki/constitutiondao-people)  
324. DAO governance models: A beginner's guide \- Cointelegraph, acessado em junho 30, 2025, [https://cointelegraph.com/learn/articles/dao-governance-models](https://cointelegraph.com/learn/articles/dao-governance-models)  
325. What's Juicy about Juicebox?. Insights from Juicebox on crypto… | by LJ Huang | Sign, acessado em junho 30, 2025, [https://medium.com/ethsign/whats-juicy-about-juicebox-74251dcc744](https://medium.com/ethsign/whats-juicy-about-juicebox-74251dcc744)  
326. A Look at the ConstitutionDAO (PEOPLE) \- Everything You Needed to Know \- Securities.io, acessado em junho 30, 2025, [https://www.securities.io/a-look-at-the-constitutiondao-people-everything-you-needed-to-know/](https://www.securities.io/a-look-at-the-constitutiondao-people-everything-you-needed-to-know/)  
327. Do you really understand DAO leader PEOPLE? | Btc-蛋总on, acessado em junho 30, 2025, [https://www.binance.com/en-IN/square/post/2283634460225](https://www.binance.com/en-IN/square/post/2283634460225)  
328. ConstitutionDAO Irks Donors as Gas Fees and Transaction Costs Eat Into Refunds, acessado em junho 30, 2025, [https://thedefiant.io/news/nfts-and-web3/constitutiondao-refunds-gas-fees](https://thedefiant.io/news/nfts-and-web3/constitutiondao-refunds-gas-fees)  
329. ConstitutionDAO Disbands After Losing Bid to Buy Constitution \- Markets Insider, acessado em junho 30, 2025, [https://markets.businessinsider.com/news/currencies/constitution-dao-disbands-refund-how-us-constitution-discord-website-twitter-2021-11](https://markets.businessinsider.com/news/currencies/constitution-dao-disbands-refund-how-us-constitution-discord-website-twitter-2021-11)  
330. Tokens of the defunct DAO that failed to buy a copy of the constitution are worth $300 million even after disbanding \- Markets Insider, acessado em junho 30, 2025, [https://markets.businessinsider.com/news/currencies/constituiondao-people-tokens-price-300-million-value-constitution-nft-dao-2022-1](https://markets.businessinsider.com/news/currencies/constituiondao-people-tokens-price-300-million-value-constitution-nft-dao-2022-1)  
331. ConstitutionDAO (PEOPLE) \- Cryptohopper, acessado em junho 30, 2025, [https://www.cryptohopper.com/currencies/detail?currency=PEOPLE](https://www.cryptohopper.com/currencies/detail?currency=PEOPLE)  
332. ConstitutionDAO Price, PEOPLE Price, Live Charts, and Marketcap \- Coinbase, acessado em junho 30, 2025, [https://www.coinbase.com/price/constitutiondao](https://www.coinbase.com/price/constitutiondao)  
333. PEOPLE coin Constitution DAO was an experiment that has now | Atiq memon on Binance Square, acessado em junho 30, 2025, [https://www.binance.com/en/square/post/24239406737233](https://www.binance.com/en/square/post/24239406737233)  
334. ConstitutionDAO's PEOPLE Token Continues to Soar Despite DAO Closure \- Decrypt, acessado em junho 30, 2025, [https://decrypt.co/87079/constitutiondaos-people-token-continues-to-soar-despite-dao-closure](https://decrypt.co/87079/constitutiondaos-people-token-continues-to-soar-despite-dao-closure)  
335. ConstitutionDAO price today, PEOPLE to INR live price, marketcap and chart | Suncrypto, acessado em junho 30, 2025, [https://suncrypto.in/price/constitutiondao](https://suncrypto.in/price/constitutiondao)  
336. Hello Everyone From CONSTITUTION-DAO {PEOPLE} \! | PLATEFORM UPDATES on Binance Square, acessado em junho 30, 2025, [https://www.binance.com/en/square/post/23693810316858](https://www.binance.com/en/square/post/23693810316858)  
337. Against Szabo's Law, For A New Crypto Legal System | by Vlad Zamfir \- Medium, acessado em junho 30, 2025, [https://medium.com/cryptolawreview/against-szabos-law-for-a-new-crypto-legal-system-d00d0f3d3827](https://medium.com/cryptolawreview/against-szabos-law-for-a-new-crypto-legal-system-d00d0f3d3827)  
338. Is there a philosopher or philosophical take that makes a statement akin to “people have an idea of what they want to do then make a rule or code that accepts what they would do” rather than basing what you should do based off your moral code? : r/askphilosophy \- Reddit, acessado em junho 30, 2025, [https://www.reddit.com/r/askphilosophy/comments/12zv80j/is\_there\_a\_philosopher\_or\_philosophical\_take\_that/](https://www.reddit.com/r/askphilosophy/comments/12zv80j/is_there_a_philosopher_or_philosophical_take_that/)  
339. Notes on Blockchain Governance, acessado em junho 30, 2025, [https://vitalik.eth.limo/general/2017/12/17/voting.html](https://vitalik.eth.limo/general/2017/12/17/voting.html)  
340. The Observer Effect — How Observing Changes Reality | by Quantumglyphs \- Medium, acessado em junho 30, 2025, [https://medium.com/@quantumglyphs1/the-observer-effect-how-observing-changes-reality-0202abadcaf8](https://medium.com/@quantumglyphs1/the-observer-effect-how-observing-changes-reality-0202abadcaf8)  
341. Observer effect (physics) \- Wikipedia, acessado em junho 30, 2025, [https://en.wikipedia.org/wiki/Observer\_effect\_(physics)](https://en.wikipedia.org/wiki/Observer_effect_\(physics\))  
342. A Conversion about the Observer Effect \- Larry Gottlieb Author, acessado em junho 30, 2025, [https://www.larrygottlieb.com/blog/a-conversion-about-the-observer-effect](https://www.larrygottlieb.com/blog/a-conversion-about-the-observer-effect)  
343. What About the Quantum Physics Observer Effect? \- Larry Gottlieb Author, acessado em junho 30, 2025, [https://www.larrygottlieb.com/blog/the-observer-effect](https://www.larrygottlieb.com/blog/the-observer-effect)  
344. Observer in Modern Physics, acessado em junho 30, 2025, [https://www.grc.nasa.gov/www/k-12/Numbers/Math/Mathematical\_Thinking/observer.htm](https://www.grc.nasa.gov/www/k-12/Numbers/Math/Mathematical_Thinking/observer.htm)  
345. Quantum Physics Meets Consciousness: A New Frontier In Science, acessado em junho 30, 2025, [https://quantumzeitgeist.com/quantum-physics-meets-consciousness-a-new-frontier-in-science/](https://quantumzeitgeist.com/quantum-physics-meets-consciousness-a-new-frontier-in-science/)  
346. Relational Quantum Mechanics \- Stanford Encyclopedia of Philosophy, acessado em junho 30, 2025, [https://plato.stanford.edu/entries/qm-relational/](https://plato.stanford.edu/entries/qm-relational/)  
347. Relational quantum mechanics \- Wikipedia, acessado em junho 30, 2025, [https://en.wikipedia.org/wiki/Relational\_quantum\_mechanics](https://en.wikipedia.org/wiki/Relational_quantum_mechanics)  
348. Carlo Rovelli's Relational Quantum Mechanics | by Paul Austin Murphy \- Medium, acessado em junho 30, 2025, [https://medium.com/paul-austin-murphys-essays-on-philosophy/carlo-rovellis-relational-quantum-mechanics-256cc264f394](https://medium.com/paul-austin-murphys-essays-on-philosophy/carlo-rovellis-relational-quantum-mechanics-256cc264f394)  
349. \[2109.09170\] The Relational Interpretation of Quantum Physics \- arXiv, acessado em junho 30, 2025, [https://arxiv.org/abs/2109.09170](https://arxiv.org/abs/2109.09170)  
350. Information is Physical: Cross-Perspective Links in Relational Quantum Mechanics \- PhilSci-Archive, acessado em junho 30, 2025, [https://philsci-archive.pitt.edu/20379/1/RQM%20paper%20copy.pdf](https://philsci-archive.pitt.edu/20379/1/RQM%20paper%20copy.pdf)  
351. Quantum Bayesianism \- Wikipedia, acessado em junho 30, 2025, [https://en.wikipedia.org/wiki/Quantum\_Bayesianism](https://en.wikipedia.org/wiki/Quantum_Bayesianism)  
352. What reality does quantum theory describe? QBism has a radical answer \- Big Think, acessado em junho 30, 2025, [https://bigthink.com/13-8/qbism-quantum-reality/](https://bigthink.com/13-8/qbism-quantum-reality/)  
353. Quantum Bayesianism: A New Perspective \- Number Analytics, acessado em junho 30, 2025, [https://www.numberanalytics.com/blog/ultimate-guide-quantum-bayesianism](https://www.numberanalytics.com/blog/ultimate-guide-quantum-bayesianism)  
354. "QBism": The most radical interpretation of quantum mechanics ever \- Big Think, acessado em junho 30, 2025, [https://bigthink.com/13-8/qbism-quantum-physics/](https://bigthink.com/13-8/qbism-quantum-physics/)  
355. Bayesian interpretation of quantum mechanics in nLab, acessado em junho 30, 2025, [https://ncatlab.org/nlab/show/Bayesian+interpretation+of+quantum+mechanics](https://ncatlab.org/nlab/show/Bayesian+interpretation+of+quantum+mechanics)  
356. Quantum Bayesianism as the basis of general theory of decision-making \- PMC, acessado em junho 30, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC4843641/](https://pmc.ncbi.nlm.nih.gov/articles/PMC4843641/)  
357. Interpretations of quantum mechanics \- Wikipedia, acessado em junho 30, 2025, [https://en.wikipedia.org/wiki/Interpretations\_of\_quantum\_mechanics](https://en.wikipedia.org/wiki/Interpretations_of_quantum_mechanics)  
358. Why QBism is completely empty | More Quantum \- Mateus Araújo, acessado em junho 30, 2025, [https://mateusaraujo.info/2020/10/01/why-qbism-is-completely-empty/](https://mateusaraujo.info/2020/10/01/why-qbism-is-completely-empty/)  
359. enactive approach \- EZEQUIEL A. DI PAOLO, acessado em junho 30, 2025, [https://ezequieldipaolo.net/tag/enactive-approach/](https://ezequieldipaolo.net/tag/enactive-approach/)  
360. A QBism/Enactivism dialogue \- EZEQUIEL A. DI PAOLO, acessado em junho 30, 2025, [https://ezequieldipaolo.net/2023/03/16/a-qbism-enactivism-dialogue/](https://ezequieldipaolo.net/2023/03/16/a-qbism-enactivism-dialogue/)  
361. (PDF) Enactivism, Health, AI, and Non-Neurotypical Individuals: Toward Contextualized, Personalized, and Ethically Grounded Interventions \- ResearchGate, acessado em junho 29, 2025, [https://www.researchgate.net/publication/391244969\_Enactivism\_Health\_AI\_and\_Non-Neurotypical\_Individuals\_Toward\_Contextualized\_Personalized\_and\_Ethically\_Grounded\_Interventions](https://www.researchgate.net/publication/391244969_Enactivism_Health_AI_and_Non-Neurotypical_Individuals_Toward_Contextualized_Personalized_and_Ethically_Grounded_Interventions)  
362. Jordi Vallverdú, Enactivism, Health, AI, and Non-Neurotypical Individuals: Toward Contextualized, Personalized, and Ethically Grounded Interventions \- PhilPapers, acessado em junho 29, 2025, [https://philpapers.org/rec/VALEHA](https://philpapers.org/rec/VALEHA)  
363. Robotics, philosophy and the problems of autonomy \- ResearchGate, acessado em junho 29, 2025, [https://www.researchgate.net/publication/233676691\_Robotics\_philosophy\_and\_the\_problems\_of\_autonomy](https://www.researchgate.net/publication/233676691_Robotics_philosophy_and_the_problems_of_autonomy)  
364. Philosophy Eats AI \- MIT Sloan Management Review, acessado em junho 29, 2025, [https://sloanreview.mit.edu/article/philosophy-eats-ai/](https://sloanreview.mit.edu/article/philosophy-eats-ai/)  
365. Towards a Catalogue of Self-Sovereign Identity Design Patterns \- MDPI, acessado em junho 30, 2025, [https://www.mdpi.com/2076-3417/13/9/5395](https://www.mdpi.com/2076-3417/13/9/5395)  
366. Robotics, philosophy and the problems of autonomy, acessado em junho 29, 2025, [https://www.socsci.ru.nl/haselag/publications/PragCogHaselager05.pdf](https://www.socsci.ru.nl/haselag/publications/PragCogHaselager05.pdf)  
367. AI generations: from AI 1.0 to AI 4.0 \- Frontiers, acessado em junho 29, 2025, [https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1585629/full](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1585629/full)  
368. 5\. Artificial Intelligence, ethics and empathy: How empathic AI applications impact humanity, acessado em junho 29, 2025, [https://www.researchgate.net/publication/385591078\_5\_Artificial\_Intelligence\_ethics\_and\_empathy\_How\_empathic\_AI\_applications\_impact\_humanity](https://www.researchgate.net/publication/385591078_5_Artificial_Intelligence_ethics_and_empathy_How_empathic_AI_applications_impact_humanity)  
369. Emotional AI and Humans: The Ethical And Practical Challenges | by Afshan Baig \- Medium, acessado em junho 29, 2025, [https://medium.com/@afshanbaig401/emotional-ai-and-humans-the-ethical-and-practical-challenges-3cd939b55b5f](https://medium.com/@afshanbaig401/emotional-ai-and-humans-the-ethical-and-practical-challenges-3cd939b55b5f)  
370. AI's Emotional Blind Spot: Why Empathy is Key in Mental Health Care \- Therapy Helpers, acessado em junho 29, 2025, [https://therapyhelpers.com/blog/limitations-of-ai-in-understanding-human-emotions/](https://therapyhelpers.com/blog/limitations-of-ai-in-understanding-human-emotions/)  
371. Code of Ethics for “Empathetic” Generative AI | e-Discovery Team, acessado em junho 29, 2025, [https://e-discoveryteam.com/2023/07/12/code-of-ethics-for-empathetic-generative-ai/](https://e-discoveryteam.com/2023/07/12/code-of-ethics-for-empathetic-generative-ai/)  
372. The risks of algorithmic governance \- TecScience, acessado em junho 30, 2025, [https://tecscience.tec.mx/en/science-communication/algorithmic-governance/](https://tecscience.tec.mx/en/science-communication/algorithmic-governance/)  
373. The Ethics of Algorithmic Governance \- Number Analytics, acessado em junho 30, 2025, [https://www.numberanalytics.com/blog/ethics-algorithmic-governance-philosophical-perspectives](https://www.numberanalytics.com/blog/ethics-algorithmic-governance-philosophical-perspectives)  
374. Algorithmic Governance and the International Politics of Big Tech | Perspectives on Politics | Cambridge Core, acessado em junho 30, 2025, [https://www.cambridge.org/core/journals/perspectives-on-politics/article/algorithmic-governance-and-the-international-politics-of-big-tech/3C04908735A5F2EE8A70AFED647741FB](https://www.cambridge.org/core/journals/perspectives-on-politics/article/algorithmic-governance-and-the-international-politics-of-big-tech/3C04908735A5F2EE8A70AFED647741FB)  
375. Algorithmic Governance from the Bottom Up \- BYU Law Digital Commons, acessado em junho 30, 2025, [https://digitalcommons.law.byu.edu/cgi/viewcontent.cgi?article=3397\&context=lawreview](https://digitalcommons.law.byu.edu/cgi/viewcontent.cgi?article=3397&context=lawreview)  
376. Algorithmic Governance and Political Legitimacy \- American Affairs Journal, acessado em junho 30, 2025, [https://americanaffairsjournal.org/2019/05/algorithmic-governance-and-political-legitimacy/](https://americanaffairsjournal.org/2019/05/algorithmic-governance-and-political-legitimacy/)  
377. "Algorithmic Governance from the Bottom Up" by Hannah Bloch-Wehba \- BYU Law Digital Commons, acessado em junho 30, 2025, [https://digitalcommons.law.byu.edu/lawreview/vol48/iss1/6/](https://digitalcommons.law.byu.edu/lawreview/vol48/iss1/6/)  
378. Sentience, Safe AI and The Future of Philosophy: A Transdisciplinary Analysis, acessado em junho 29, 2025, [https://www.oxfordpublicphilosophy.com/sentience/se](https://www.oxfordpublicphilosophy.com/sentience/se)  
379. "The History of Philosophy and the Future of AI": Cameron Buckner and Audrey Borowski, acessado em junho 29, 2025, [https://m.youtube.com/watch?v=gJCGKtiLwMc\&pp=0gcJCY0JAYcqIYzv](https://m.youtube.com/watch?v=gJCGKtiLwMc&pp=0gcJCY0JAYcqIYzv)  
380. A conversation with an AI led to a new philosophy: Syntellectism. It challenges human-centered views of intelligence. Thoughts? : r/Futurology \- Reddit, acessado em junho 29, 2025, [https://www.reddit.com/r/Futurology/comments/1j6osz6/a\_conversation\_with\_an\_ai\_led\_to\_a\_new\_philosophy/](https://www.reddit.com/r/Futurology/comments/1j6osz6/a_conversation_with_an_ai_led_to_a_new_philosophy/)  
381. Artificial You: AI and the Future of Your Mind, by Susan Schneider: a review, acessado em junho 29, 2025, [https://archive.philosophersmag.com/artificial-you-ai-and-the-future-of-your-mind-by-susan-schneider-a-review/](https://archive.philosophersmag.com/artificial-you-ai-and-the-future-of-your-mind-by-susan-schneider-a-review/)  
382. O SISTEMA IMUNOLÓGICO PARA A EDUCAÇÃO BÁSICA: CONSTRUÇÃO DE UM JOGO POR ESTUDANTES SUPERDOTADOS \- SciELO Preprints, acessado em junho 29, 2025, [https://preprints.scielo.org/index.php/scielo/preprint/download/5212/10242/10744](https://preprints.scielo.org/index.php/scielo/preprint/download/5212/10242/10744)  
383. (PDF) Governance of a DAO for Facilitating Dialogue on Human-Algorithm Interaction and the Impact of Emerging Technologies on Society \- ResearchGate, acessado em junho 29, 2025, [https://www.researchgate.net/publication/371868968\_Governance\_of\_a\_DAO\_for\_Facilitating\_Dialogue\_on\_Human-Algorithm\_Interaction\_and\_the\_Impact\_of\_Emerging\_Technologies\_on\_Society](https://www.researchgate.net/publication/371868968_Governance_of_a_DAO_for_Facilitating_Dialogue_on_Human-Algorithm_Interaction_and_the_Impact_of_Emerging_Technologies_on_Society)  
384. Autopoiesis, Structural Coupling and Cognition: A history of these. and. other notions in the biology of cognition \- Reflexus, acessado em junho 29, 2025, [https://reflexus.org/wp-content/uploads/Autopoiesis-structural-coupling-and-cognition.pdf](https://reflexus.org/wp-content/uploads/Autopoiesis-structural-coupling-and-cognition.pdf)  
385. Future of Algorithmic Organization: Large Scale Analysis of Decentralized Autonomous Organizations (DAOs) \- arXiv, acessado em junho 29, 2025, [https://arxiv.org/html/2410.13095v1](https://arxiv.org/html/2410.13095v1)  
386. DEMOBILIZING IMMUNOLOGY: AUTOPOIESIS AND AUTONOMY ..., acessado em junho 29, 2025, [https://open.library.ubc.ca/media/stream/pdf/24/1.0073115/5](https://open.library.ubc.ca/media/stream/pdf/24/1.0073115/5)  
387. Imunidade adquirida \- Doenças imunológicas \- Manual MSD Versão Saúde para a Família, acessado em junho 29, 2025, [https://www.msdmanuals.com/pt/casa/doen%C3%A7as-imunol%C3%B3gicas/biologia-do-sistema-imunol%C3%B3gico/imunidade-adquirida](https://www.msdmanuals.com/pt/casa/doen%C3%A7as-imunol%C3%B3gicas/biologia-do-sistema-imunol%C3%B3gico/imunidade-adquirida)  
388. Aligning 'Decentralized Autonomous Organization' to Precedents in Cybernetics, acessado em junho 29, 2025, [https://law.mit.edu/pub/dao-precedents-cybernetics](https://law.mit.edu/pub/dao-precedents-cybernetics)  
389. Labour pains: Content moderation challenges in Mastodon growth \- Internet Policy Review, acessado em junho 29, 2025, [https://policyreview.info/articles/analysis/content-moderation-challenges](https://policyreview.info/articles/analysis/content-moderation-challenges)  
390. Descoberta de que astrócitos têm memória imunológica lança luz sobre a autoimunidade, acessado em junho 29, 2025, [https://www.news.med.br/p/medical-journal/1468457/descoberta-de-que-astrocitos-tem-memoria-imunologica-lanca-luz-sobre-a-autoimunidade.htm](https://www.news.med.br/p/medical-journal/1468457/descoberta-de-que-astrocitos-tem-memoria-imunologica-lanca-luz-sobre-a-autoimunidade.htm)  
391. Autopoiesis in Law and Society \- Number Analytics, acessado em junho 29, 2025, [https://www.numberanalytics.com/blog/autopoiesis-law-society](https://www.numberanalytics.com/blog/autopoiesis-law-society)  
392. (PDF) Mapping out the DAO Ecosystem and Assessing DAO Autonomy \- ResearchGate, acessado em junho 29, 2025, [https://www.researchgate.net/publication/365959936\_Mapping\_out\_the\_DAO\_Ecosystem\_and\_Assessing\_DAO\_Autonomy](https://www.researchgate.net/publication/365959936_Mapping_out_the_DAO_Ecosystem_and_Assessing_DAO_Autonomy)  
393. Exploring Immune Evasion and Vaccine Strategies in Host-Pathogen Interactions \- Frontiers, acessado em junho 29, 2025, [https://www.frontiersin.org/research-topics/69375/exploring-immune-evasion-and-vaccine-strategies-in-host-pathogen-interactions](https://www.frontiersin.org/research-topics/69375/exploring-immune-evasion-and-vaccine-strategies-in-host-pathogen-interactions)  
394. Showing your ass on Mastodon: Lossy distribution ... \- First Monday, acessado em junho 29, 2025, [https://firstmonday.org/ojs/index.php/fm/article/download/13367/11592/86173](https://firstmonday.org/ojs/index.php/fm/article/download/13367/11592/86173)  
395. "A TAXONOMY OF FORKS IN THE CONTEXT OF DECENTRALIZED ..., acessado em junho 29, 2025, [https://aisel.aisnet.org/ecis2022\_rp/77/](https://aisel.aisnet.org/ecis2022_rp/77/)  
396. Autopoiesis, Autonomy and Organizational Biology: Critical Remarks on “Life After Ashby”, acessado em junho 29, 2025, [https://www.researchgate.net/publication/235661678\_Autopoiesis\_Autonomy\_and\_Organizational\_Biology\_Critical\_Remarks\_on\_Life\_After\_Ashby](https://www.researchgate.net/publication/235661678_Autopoiesis_Autonomy_and_Organizational_Biology_Critical_Remarks_on_Life_After_Ashby)  
397. An incomplete guide to Folding: Nova, Sangria, SuperNova, HyperN… \- Taiko Labs, acessado em junho 30, 2025, [https://taiko.mirror.xyz/tk8LoE-rC2w0MJ4wCWwaJwbq8-Ih8DXnLUf7aJX1FbU](https://taiko.mirror.xyz/tk8LoE-rC2w0MJ4wCWwaJwbq8-Ih8DXnLUf7aJX1FbU)  
398. (PDF) Information and closure in systems theory \- ResearchGate, acessado em junho 30, 2025, [https://www.researchgate.net/publication/41832496\_Information\_and\_closure\_in\_systems\_theory](https://www.researchgate.net/publication/41832496_Information_and_closure_in_systems_theory)  
399. The Autopoiesis of Social Systems and its Criticisms \- Constructivist Foundations, acessado em junho 30, 2025, [https://constructivist.info/10/2/169.cadenas.pdf](https://constructivist.info/10/2/169.cadenas.pdf)  
400. Autopoietic System \- New Materialism, acessado em junho 30, 2025, [https://newmaterialism.eu/almanac/a/autopoietic-system.html](https://newmaterialism.eu/almanac/a/autopoietic-system.html)  
401. Imunidade: resumo sobre o sistema imunológico \- Sanarmed, acessado em junho 29, 2025, [https://sanarmed.com/resumo-sistema-imunologico/](https://sanarmed.com/resumo-sistema-imunologico/)  
402. Immune checkpoint inhibitors in cancer patients with autoimmune disease: Safety and efficacy \- PMC \- PubMed Central, acessado em junho 29, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11792813/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11792813/)  
403. Francisco Varela's Vision of the Immune System, acessado em junho 29, 2025, [https://apcz.umk.pl/RF/article/download/RF.2019.030/17764/50259](https://apcz.umk.pl/RF/article/download/RF.2019.030/17764/50259)  
404. Psychoneuroimmunology of Stress and Mental Health, acessado em junho 29, 2025, [http://www.uclastresslab.org/pubs/Slavich\_Psychoneuroimmunology\_OxfordHandbook\_in%20press.pdf](http://www.uclastresslab.org/pubs/Slavich_Psychoneuroimmunology_OxfordHandbook_in%20press.pdf)  
405. The ontogeny of immune tolerance: a model of the early-life gut microbiome and adaptive immunity | bioRxiv, acessado em junho 29, 2025, [https://www.biorxiv.org/content/10.1101/2024.05.20.594845v1.full-text](https://www.biorxiv.org/content/10.1101/2024.05.20.594845v1.full-text)  
406. Autopoiesis in Decentralized Autonomous Organizations as ..., acessado em junho 29, 2025, [https://www.ijbta.com/vol2/IJBTA-V2N2-20.pdf](https://www.ijbta.com/vol2/IJBTA-V2N2-20.pdf)  
407. Dismantling the “Natural vs. Artificial” Dichotomy as a New Paradigm in Systems Theory \- PhilArchive, acessado em junho 29, 2025, [https://philarchive.org/archive/DELTAS-7v3](https://philarchive.org/archive/DELTAS-7v3)  
408. \[2001.09273\] An Immunology-Inspired Network Security Architecture \- arXiv, acessado em junho 29, 2025, [https://arxiv.org/abs/2001.09273](https://arxiv.org/abs/2001.09273)  
409. Adaptive and Privacy-Preserving Security for Federated Learning Using Biological Immune System Principles \- ResearchGate, acessado em junho 29, 2025, [https://www.researchgate.net/publication/386435006\_Adaptive\_and\_Privacy-Preserving\_Security\_for\_Federated\_Learning\_Using\_Biological\_Immune\_System\_Principles](https://www.researchgate.net/publication/386435006_Adaptive_and_Privacy-Preserving_Security_for_Federated_Learning_Using_Biological_Immune_System_Principles)  
410. THE APPLICATION OF AUTOPOIESIS IN SYSTEMS ANALYSIS: ARE AUTOPOIETIC SYSTEMS ALSO SOCIAL SYSTEMS? \- CEPA.INFO, acessado em junho 30, 2025, [https://cepa.info/fulltexts/1207.pdf](https://cepa.info/fulltexts/1207.pdf)  
411. The Rise of Decentralized Autonomous Organizations: Opportunities and Challenges, acessado em junho 29, 2025, [https://stanford-jblp.pubpub.org/pub/rise-of-daos](https://stanford-jblp.pubpub.org/pub/rise-of-daos)  
412. The Enactive and Interactive Dimensions of AI: Ingenuity and Imagination Through the Lens of Art and Music \- MIT Press Direct, acessado em junho 29, 2025, [https://direct.mit.edu/artl/article/28/3/310/112448/The-Enactive-and-Interactive-Dimensions-of-AI](https://direct.mit.edu/artl/article/28/3/310/112448/The-Enactive-and-Interactive-Dimensions-of-AI)  
413. Enactivism, Health, AI, and Non-Neurotypical Individuals: Toward Contextualized, Personalized, and Ethically Grounded Interventions \- MDPI, acessado em junho 29, 2025, [https://www.mdpi.com/2409-9287/10/3/51](https://www.mdpi.com/2409-9287/10/3/51)  
414. (PDF) Philosophical Review of Artificial Intelligence for Society 5.0 \- ResearchGate, acessado em junho 29, 2025, [https://www.researchgate.net/publication/374612222\_Philosophical\_Review\_of\_Artificial\_Intelligence\_for\_Society\_50](https://www.researchgate.net/publication/374612222_Philosophical_Review_of_Artificial_Intelligence_for_Society_50)  
415. Law as a Social System, by Niklas Luhmann \- Osgoode Digital Commons, acessado em junho 29, 2025, [https://digitalcommons.osgoode.yorku.ca/cgi/viewcontent.cgi?article=2216\&context=scholarly\_works](https://digitalcommons.osgoode.yorku.ca/cgi/viewcontent.cgi?article=2216&context=scholarly_works)  
416. (PDF) A Bio-inspired Approach To Cyber Security: Principles, Algorithms, and Practices, acessado em junho 29, 2025, [https://www.researchgate.net/publication/331190781\_A\_Bio-inspired\_Approach\_To\_Cyber\_Security\_Principles\_Algorithms\_and\_Practices](https://www.researchgate.net/publication/331190781_A_Bio-inspired_Approach_To_Cyber_Security_Principles_Algorithms_and_Practices)  
417. Cognitive Science and Affective Computing \- Number Analytics, acessado em junho 29, 2025, [https://www.numberanalytics.com/blog/cognitive-science-affective-computing](https://www.numberanalytics.com/blog/cognitive-science-affective-computing)  
418. Cancer immunotherapy, explained \- UChicago News \- The University of Chicago, acessado em junho 29, 2025, [https://news.uchicago.edu/explainer/what-is-immunotherapy](https://news.uchicago.edu/explainer/what-is-immunotherapy)  
419. Transforming university records management: A comprehensive review of blockchain and self-sovereign identity applications, acessado em junho 30, 2025, [https://ijsra.net/sites/default/files/IJSRA-2024-0514.pdf](https://ijsra.net/sites/default/files/IJSRA-2024-0514.pdf)  
420. Mathematics in modern immunology \- PMC, acessado em junho 29, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC4759751/](https://pmc.ncbi.nlm.nih.gov/articles/PMC4759751/)  
421. (PDF) Identity Management, SSI and Blockchain: A Review \- ResearchGate, acessado em junho 30, 2025, [https://www.researchgate.net/publication/377815608\_Identity\_Management\_SSI\_and\_Blockchain\_A\_Review](https://www.researchgate.net/publication/377815608_Identity_Management_SSI_and_Blockchain_A_Review)  
422. Collective Intentionality \- Stanford Encyclopedia of Philosophy, acessado em junho 29, 2025, [https://plato.stanford.edu/entries/collective-intentionality/](https://plato.stanford.edu/entries/collective-intentionality/)  
423. A Deep Dive Into DAO \- Gate.com, acessado em junho 29, 2025, [https://www.gate.com/learn/articles/a-deep-dive-into-dao/2106](https://www.gate.com/learn/articles/a-deep-dive-into-dao/2106)  
424. The DAO Controversy: The Case for a New Species of Corporate Governance? \- Frontiers, acessado em junho 29, 2025, [https://www.frontiersin.org/journals/blockchain/articles/10.3389/fbloc.2020.00025/full](https://www.frontiersin.org/journals/blockchain/articles/10.3389/fbloc.2020.00025/full)  
425. Intelligence and Philosophy: between new and old artificial crossroads \- SciELO, acessado em junho 29, 2025, [https://www.scielo.br/j/fun/a/ytgsjNqHfWKcXXmWWhMrf4D/](https://www.scielo.br/j/fun/a/ytgsjNqHfWKcXXmWWhMrf4D/)  
426. What is Autoimmunity? \- News-Medical, acessado em junho 29, 2025, [https://www.news-medical.net/health/What-is-Autoimmunity.aspx](https://www.news-medical.net/health/What-is-Autoimmunity.aspx)  
427. Eccfrog512ck2: An Enhanced 512-bit Weierstrass Elliptic Curve \- Cryptology ePrint Archive, acessado em junho 29, 2025, [https://eprint.iacr.org/2025/660](https://eprint.iacr.org/2025/660)  
428. Enactivism \- Wikipedia, acessado em junho 30, 2025, [https://en.wikipedia.org/wiki/Enactivism](https://en.wikipedia.org/wiki/Enactivism)  
429. The Evolving Constellation of Theory of Mind in Artificial Intelligence \- Medium, acessado em junho 29, 2025, [https://medium.com/intuitionmachine/the-evolving-constellation-of-theory-of-mind-in-artificial-intelligence-604863f57917](https://medium.com/intuitionmachine/the-evolving-constellation-of-theory-of-mind-in-artificial-intelligence-604863f57917)  
430. Autopoiesis of the artificial: from systems to cognition \- PubMed, acessado em junho 29, 2025, [https://pubmed.ncbi.nlm.nih.gov/37279825/](https://pubmed.ncbi.nlm.nih.gov/37279825/)  
431. Mathematical Model of Innate and Adaptive Immunity of Sepsis: A Modeling and Simulation Study of Infectious Disease \- PMC, acessado em junho 29, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC4584099/](https://pmc.ncbi.nlm.nih.gov/articles/PMC4584099/)  
432. PAMP recognition by TLRs and adaptor proteins to mediate cellular... | Download Scientific Diagram \- ResearchGate, acessado em junho 29, 2025, [https://www.researchgate.net/figure/PAMP-recognition-by-TLRs-and-adaptor-proteins-to-mediate-cellular-signaling-pathways-TLR\_fig1\_338394290](https://www.researchgate.net/figure/PAMP-recognition-by-TLRs-and-adaptor-proteins-to-mediate-cellular-signaling-pathways-TLR_fig1_338394290)  
433. Getting Ahead of One's Self?: The Common Culture of Immunology and Philosophy | Isis, acessado em junho 29, 2025, [https://www.journals.uchicago.edu/doi/full/10.1086/678176](https://www.journals.uchicago.edu/doi/full/10.1086/678176)  
434. Self-organization \- Wikipedia, acessado em junho 29, 2025, [https://en.wikipedia.org/wiki/Self-organization](https://en.wikipedia.org/wiki/Self-organization)  
435. No way to reproduce some key numbers used in the design of Elliptic Curves : r/Bitcoin, acessado em junho 29, 2025, [https://www.reddit.com/r/Bitcoin/comments/1m6twq/no\_way\_to\_reproduce\_some\_key\_numbers\_used\_in\_the/](https://www.reddit.com/r/Bitcoin/comments/1m6twq/no_way_to_reproduce_some_key_numbers_used_in_the/)  
436. cryptography \- How is the generator point G chosen in the ..., acessado em junho 29, 2025, [https://bitcoin.stackexchange.com/questions/113116/how-is-the-generator-point-g-chosen-in-the-secp256k1-curve-used-in-bitcoin](https://bitcoin.stackexchange.com/questions/113116/how-is-the-generator-point-g-chosen-in-the-secp256k1-curve-used-in-bitcoin)  
437. Polyphony and embodiment: a critical approach to the theory of autopoiesis \- SIBE Sociedad de Etnomusicología, acessado em junho 30, 2025, [https://www.sibetrans.com/trans/article/179/polyphony-and-embodiment-a-critical-approach-to-the-theory-of-autopoiesis](https://www.sibetrans.com/trans/article/179/polyphony-and-embodiment-a-critical-approach-to-the-theory-of-autopoiesis)  
438. Poor performance of ECC implementation of secp256k1 · Issue \#23524 \- GitHub, acessado em junho 29, 2025, [https://github.com/openssl/openssl/issues/23524](https://github.com/openssl/openssl/issues/23524)  
439. The FIPS 186-4 Digital Signature Algorithm Validation System (DSA2VS) \- NIST Computer Security Resource Center, acessado em junho 29, 2025, [https://csrc.nist.gov/csrc/media/projects/cryptographic-algorithm-validation-program/documents/dss2/dsa2vs.pdf](https://csrc.nist.gov/csrc/media/projects/cryptographic-algorithm-validation-program/documents/dss2/dsa2vs.pdf)  
440. A review on self-healing featured soft robotics \- PMC \- PubMed Central, acessado em junho 29, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC10637358/](https://pmc.ncbi.nlm.nih.gov/articles/PMC10637358/)  
441. Psychoneuroimmunology: Your Brain and Immune System Connections \- WebMD, acessado em junho 29, 2025, [https://www.webmd.com/brain/what-is-psychoneuroimmunology](https://www.webmd.com/brain/what-is-psychoneuroimmunology)  
442. secp256k1 \- crates.io: Rust Package Registry, acessado em junho 29, 2025, [https://crates.io/crates/secp256k1/0.28.0](https://crates.io/crates/secp256k1/0.28.0)  
443. Identity-based cryptography \- Wikipedia, acessado em junho 29, 2025, [https://en.wikipedia.org/wiki/Identity-based\_cryptography](https://en.wikipedia.org/wiki/Identity-based_cryptography)  
444. Cultural Immune Systems as Parts of Cultural Superorganisms \- ProSocial World, acessado em junho 29, 2025, [https://www.prosocial.world/posts/mental-immunity-from-a-multilevel-evolutionary-perspective](https://www.prosocial.world/posts/mental-immunity-from-a-multilevel-evolutionary-perspective)  
445. Self-organizing Dynamical Systems \- ResearchGate, acessado em junho 29, 2025, [https://www.researchgate.net/profile/Scott-Kelso/publication/288151570\_Self-organizing\_Dynamical\_Systems/links/5bba43fa4585159e8d8bd4f8/Self-organizing-Dynamical-Systems.pdf](https://www.researchgate.net/profile/Scott-Kelso/publication/288151570_Self-organizing_Dynamical_Systems/links/5bba43fa4585159e8d8bd4f8/Self-organizing-Dynamical-Systems.pdf)  
446. Teaching cognitive and affective empathy in medicine: a systematic review and meta-analysis of randomized controlled trials \- PubMed, acessado em junho 29, 2025, [https://pubmed.ncbi.nlm.nih.gov/40329527/](https://pubmed.ncbi.nlm.nih.gov/40329527/)  
447. Here's a playbook for stopping deadly cytokine storm syndrome \- UAB Reporter, acessado em junho 29, 2025, [https://www.uab.edu/reporter/research-innovation/here-s-a-playbook-for-stopping-deadly-cytokine-storm-syndrome](https://www.uab.edu/reporter/research-innovation/here-s-a-playbook-for-stopping-deadly-cytokine-storm-syndrome)  
448. A Brief Review of Systems Theories and Their Managerial Applications \- PubsOnLine, acessado em junho 29, 2025, [https://pubsonline.informs.org/doi/pdf/10.1287/serv.2.1\_2.126](https://pubsonline.informs.org/doi/pdf/10.1287/serv.2.1_2.126)  
449. imunologia básica: uma revisão aplicada a estudantes, acessado em junho 29, 2025, [https://unipacto.com.br/storage/gallery/files/nice/livros/IMUNOLOGIA%20B%C3%81SICA%20-%20UMA%20REVIS%C3%83O%20APLICADA%20A%20ESTUDANTES.pdf](https://unipacto.com.br/storage/gallery/files/nice/livros/IMUNOLOGIA%20B%C3%81SICA%20-%20UMA%20REVIS%C3%83O%20APLICADA%20A%20ESTUDANTES.pdf)  
450. Affective immunology: where emotions and the immune response converge \- PMC, acessado em junho 29, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC5442367/](https://pmc.ncbi.nlm.nih.gov/articles/PMC5442367/)  
451. From Lead to Gold: The Alchemy of Character Arc With Carl Jung, acessado em junho 29, 2025, [https://www.helpingwritersbecomeauthors.com/alchemy-of-character-arc/](https://www.helpingwritersbecomeauthors.com/alchemy-of-character-arc/)  
452. Systems Theory in Evaluation: Understanding Complex Social Systems \- EvalCommunity, acessado em junho 29, 2025, [https://www.evalcommunity.com/career-center/systems-theory/](https://www.evalcommunity.com/career-center/systems-theory/)  
453. The Dynamics of Exchanges and References among Scientific Texts, and the Autopoiesis of Discursive Knowledge \- Loet Leydesdorff, acessado em junho 29, 2025, [https://www.leydesdorff.net/autopoiesis/](https://www.leydesdorff.net/autopoiesis/)  
454. New Paradigms in Trust and Safety: Navigating Defederation on Decentralized Social Media Platforms | Carnegie Endowment for International Peace, acessado em junho 29, 2025, [https://carnegieendowment.org/research/2025/03/fediverse-social-media-internet-defederation?lang=en](https://carnegieendowment.org/research/2025/03/fediverse-social-media-internet-defederation?lang=en)  
455. A Computational Model of Empathy: Empirical Evaluation \- ResearchGate, acessado em junho 29, 2025, [https://www.researchgate.net/publication/259632516\_A\_Computational\_Model\_of\_Empathy\_Empirical\_Evaluation](https://www.researchgate.net/publication/259632516_A_Computational_Model_of_Empathy_Empirical_Evaluation)  
456. 965: Primer on Whitehead's Process Philosophy as a Paradigm Shift & Foundation for Experiential Design \- Voices of VR Podcast, acessado em junho 30, 2025, [https://voicesofvr.com/primer-on-whiteheads-process-philosophy-as-a-paradigm-shift-foundation-for-experiential-design/](https://voicesofvr.com/primer-on-whiteheads-process-philosophy-as-a-paradigm-shift-foundation-for-experiential-design/)  
457. Old vaccines for new infections: Exploiting innate immunity to control COVID-19 and prevent future pandemics | PNAS, acessado em junho 29, 2025, [https://www.pnas.org/doi/10.1073/pnas.2101718118](https://www.pnas.org/doi/10.1073/pnas.2101718118)  
458. speed optimizations in bitcoin key recovery attacks \- SAV, acessado em junho 29, 2025, [https://www.sav.sk/journals/uploads/0215094304C459.pdf](https://www.sav.sk/journals/uploads/0215094304C459.pdf)  
459. Evaluation of secp256k1 as Popular Alternative Curve \- IETF Datatracker, acessado em junho 29, 2025, [https://datatracker.ietf.org/meeting/interim-2017-cfrg-01/materials/slides-interim-2017-cfrg-01-sessa-secp256k1-00](https://datatracker.ietf.org/meeting/interim-2017-cfrg-01/materials/slides-interim-2017-cfrg-01-sessa-secp256k1-00)  
460. Making Sense of (Autopoietic) Enactive Embodiment: A Gentle Appraisal \- ResearchGate, acessado em junho 29, 2025, [https://www.researchgate.net/publication/312039423\_Making\_Sense\_of\_Autopoietic\_Enactive\_Embodiment\_A\_Gentle\_Appraisal](https://www.researchgate.net/publication/312039423_Making_Sense_of_Autopoietic_Enactive_Embodiment_A_Gentle_Appraisal)  
461. The autopoiesis of social systems and its criticisms, acessado em junho 29, 2025, [https://repositorio.uchile.cl/handle/2250/155162](https://repositorio.uchile.cl/handle/2250/155162)  
462. RIP-7212: Unlocking New Potential for Mantle and Ethereum Ecosystem, acessado em junho 29, 2025, [https://www.mantle.xyz/blog/announcements/rip-7212-unlocking-new-potential-for-mantle-and-ethereum-ecosystem](https://www.mantle.xyz/blog/announcements/rip-7212-unlocking-new-potential-for-mantle-and-ethereum-ecosystem)  
463. What is Jungian Psychology? \- Routledge Blog, acessado em junho 29, 2025, [https://blog.routledge.com/mental-health-and-psychology/what-is-jungian-psychology/](https://blog.routledge.com/mental-health-and-psychology/what-is-jungian-psychology/)  
464. Communication and Language in Niklas Luhmann's Systems-Theory \- DigitalOcean, acessado em junho 30, 2025, [https://gerry-production-storage.fra1.cdn.digitaloceanspaces.com/files/1864/15611.pdf](https://gerry-production-storage.fra1.cdn.digitaloceanspaces.com/files/1864/15611.pdf)