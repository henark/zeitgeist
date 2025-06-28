# **Tutorial: Building a Eudaimonia 2.0 MVP with an AI Agent Team**

**Objective:** To create a functional prototype that demonstrates the core concepts of Eudaimonia 2.0, including a "Living World," deliberation via Polis, a community currency, and a faceted identity.

**Required Tools:**

* Python 3.7+  
* An agent automation framework (this tutorial will use **CrewAI**'s syntax 1 for its clarity in defining roles).  
* API keys for an LLM (e.g., OpenAI, Anthropic) and, optionally, for search services.  
* Docker and Docker Compose to deploy Polis.

---

### **Phase 0: Preparation and Environment Setup**

This initial phase establishes the project's structure. It is an ideal task for a DevOps agent, as it involves creating standardized files and directories.

#### **Responsible Agent: DevOps\_Agent**

**Step 1: Structure the Project**

The human supervisor starts the process with a prompt for the DevOps\_Agent.

**Prompt for DevOps\_Agent:**

**Persona:** You are an expert DevOps Engineer specializing in infrastructure automation and project setup.

**Objective:** Prepare the initial directory and file structure for the "Eudaimonia MVP" project.

**Task:**

1. Create a root directory named eudaimonia\_mvp.  
2. Inside eudaimonia\_mvp, create the following subdirectories: agents, config, modules.  
3. Create the following empty files:  
   * eudaimonia\_mvp/main.py (main entry point to orchestrate the AI team).  
   * eudaimonia\_mvp/agents/agents.py (to define agent roles).  
   * eudaimonia\_mvp/agents/tasks.py (to define agent tasks).  
   * eudaimonia\_mvp/modules/identity.py (for the identity module prototype).  
   * eudaimonia\_mvp/modules/currency.py (for the currency module prototype).  
   * eudaimonia\_mvp/modules/interface.py (for the user interface).  
   * eudaimonia\_mvp/.env (to store API keys).  
   * eudaimonia\_mvp/requirements.txt with the following content:  
     crewai  
     python-dotenv  
     streamlit  
     requests  
4. Confirm the creation of the entire file and directory structure.

---

### **Phase 1: Implementing Augmented Deliberation**

The heart of Eudaimonia 2.0 is the capacity for collective deliberation.2 This phase focuses on deploying Polis and creating an agent capable of interacting with it.

#### **Responsible Agent: DevOps\_Agent**

**Step 2: Deploy a Local Polis Instance**

Polis is distributed via Docker, making its deployment a highly automatable task.3

**Prompt for DevOps\_Agent:**

**Persona:** You are a DevOps Engineer with experience deploying open-source applications via Docker.

**Objective:** Deploy a local, functional instance of the Polis deliberation platform.

**Task:**

1. Clone the official Polis repository: git clone https://github.com/compdemocracy/polis.git.  
2. Navigate to the cloned directory.  
3. Follow the instructions in the README.md for a local development deployment:  
   * Copy example.env to .env.  
   * Run the make start or docker-compose up command to start all necessary containers (server, client, math, and database).  
4. Verify that the instance is accessible at http://localhost. Confirm that the user creation page (/createuser) loads correctly.

#### **Responsible Agent: Plurality\_Companion\_Agent**

**Step 3: Create a Deliberation Summarizer**

This agent will specialize in analyzing the results of a Polis conversation and extracting insights, a key capability of the "AI Companion".2 Research shows that LLMs are effective for this task.4

**Prompt for Plurality\_Companion\_Agent:**

**Persona:** You are a collective intelligence facilitator, specializing in analyzing deliberation data from the Polis platform. Your goal is to provide clear, neutral, and actionable summaries.

**Objective:** Create a Python function that takes raw data from a Polis conversation and returns a structured summary.

**Task:**

1. Write a Python function named summarize\_polis\_data(polis\_data).  
2. The function should analyze the Polis data structure (which includes comments, votes, and participant groupings).  
3. The function must identify and extract:  
   * The top 3 statements that achieved the highest consensus among all participants.  
   * The top 3 statements that were the most divisive, i.e., that created the largest opposing opinion clusters.  
   * A brief narrative description of the main opinion groups that emerged.  
4. Return a Python dictionary with the keys: consensus\_statements, divisive\_statements, and group\_narrative.  
5. Add detailed comments to the code explaining each step of the analysis.

---

### **Phase 2: Prototyping Economic and Identity Primitives**

For the MVP, we will implement simplified, in-memory versions of the Community Currency and Faceted Identity concepts, avoiding the complexity of smart contracts for now.

#### **Responsible Agent: Protocol\_Engineer\_Agent**

**Step 4: Prototype the Community Currency**

**Prompt for Protocol\_Engineer\_Agent:**

**Persona:** You are a senior software engineer specializing in economic and ledger systems.

**Objective:** Create an in-memory ledger prototype for a non-transferable "Community Currency," as specified in the Eudaimonia 2.0 project.2

**Task:**

1. In the modules/currency.py file, create a Python class named CommunityCurrencyLedger.  
2. The class should manage the balances of a single currency (e.g., "Forest-Aether") for different users (identified by their wallet addresses).  
3. Implement the following methods:  
   * \_\_init\_\_(self, currency\_name): Initializes the ledger with a currency name and an empty dictionary for balances.  
   * mint(self, user\_address, amount): Adds an amount of currency to a user's balance.  
   * get\_balance(self, user\_address): Returns a user's balance.  
   * record\_contribution(self, from\_user, to\_project, amount): Deducts the amount from the from\_user's balance and records the contribution (simply print a message for the MVP). Return True if the transaction is successful, False if the balance is insufficient.  
4. Ensure the currency is non-transferable between users (i.e., do not implement a direct transfer method).

#### **Responsible Agent: Protocol\_Engineer\_Agent**

**Step 5: Prototype the Faceted Identity**

**Prompt for Protocol\_Engineer\_Agent:**

**Persona:** You are a senior software engineer specializing in decentralized identity systems.

**Objective:** Create an in-memory prototype for a "Faceted Identity" system, as specified in the Eudaimonia 2.0 project.2

**Task:**

1. In the modules/identity.py file, create a Python class named FacetedIdentityManager.  
2. The class should manage a mapping of user identities (wallet addresses) to their roles and reputations in different "Living Worlds."  
3. Implement the following methods:  
   * \_\_init\_\_(self): Initializes an empty dictionary to store identity profiles.  
   * create\_profile(self, user\_address): Creates an empty profile for a new user.  
   * add\_role(self, user\_address, world\_name, role): Adds a role to a user within a specific "Living World."  
   * get\_identity\_facets(self, user\_address): Returns all roles and worlds associated with a user.

---

### **Phase 3: User Interface and Integration**

In this final phase, a UI agent will create a simple interface to visualize the constructed components, and the human supervisor will orchestrate the team to integrate everything.

#### **Responsible Agent: UX\_UI\_Agent**

**Step 6: Build the Prototype Interface**

**Prompt for UX\_UI\_Agent:**

**Persona:** You are a front-end developer proficient in creating fast and functional user interfaces with Streamlit.

**Objective:** Create a simple web interface to display the data from the Eudaimonia MVP.

**Task:**

1. In the modules/interface.py file, write a function called render\_mvp\_interface(identity\_manager, currency\_ledger, polis\_summary).  
2. Use the Streamlit library to create the interface.  
3. The interface should have the following sections:  
   * A title: "Eudaimonia 2.0 Prototype".  
   * A "Deliberation Summary (Polis)" section that clearly displays the content of the polis\_summary dictionary.  
   * A "Community Balances" section that iterates over the users in the currency\_ledger and displays each one's balance.  
   * A "Community Identities" section that allows selecting a user and displays their faceted identities obtained from the identity\_manager.  
4. Use st.title, st.header, st.write, st.selectbox, and st.json to format the output in a readable way.

#### **Human Supervisor**

**Step 7: Orchestrate the Team and Run the MVP**

In this final step, the human supervisor edits the main.py file to import the modules, instantiate the agents, and execute the tasks in sequence.

1. **Configure main.py:**  
   * Import the classes and functions from the modules/\*.py and agents/\*.py files.  
   * Load the API keys from the .env file.  
   * Instantiate the CrewAI team agents, assigning each the roles and objectives defined in the prompts above.1  
2. **Execute the Flow:**  
   * First, run the DevOps\_Agent's task to deploy Polis.  
   * Next, simulate fetching data from a Polis conversation (a sample JSON can be used for now) and pass it to the Plurality\_Companion\_Agent's task.  
   * Run the Protocol\_Engineer\_Agent's tasks to create the ledger and identity objects.  
   * Populate the objects with some sample data (e.g., create a few users, give them currency and roles).  
   * Finally, run the UX\_UI\_Agent's task, passing the objects and the Polis summary to the rendering function.  
3. **Launch the Application:**  
   * Run the command streamlit run modulos/interface.py in the terminal.

By the end of this tutorial, you will have successfully tested the ability of an AI agent team to follow complex, multi-faceted instructions to build the fundamental components of a software prototype, from infrastructure to the user interface.