# TimeFarm Bot

This repository contains a Python-based bot for automating tasks in the TimeFarm Telegram game. It can automatically handle farming, claiming rewards, upgrading, and managing authentication tokens for multiple accounts.

This bot was analyzed and prepared as part of a larger exploration into time-based systems and decentralized applications. The core logic resides in `main.py`.

## Configuration

All configuration is handled via environment variables, which can be placed in a `.env` file in the root of the project.

For a detailed explanation of all configuration options, how to tune them for your specific needs, and best practices for deployment, please see the comprehensive guide:

**[>> Guia de Configuração (Portuguese Configuration Guide)](./GUIA_CONFIGURACAO.md)**

## Setup

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Create your account file:**
    *   Create a file named `query.txt` in the root directory.
    *   Add your account `query_id`(s) to this file, one per line.
3.  **Create your configuration file:**
    *   Create a file named `.env`.
    *   Add the necessary configuration variables (see the guide above for details).
4.  **Run the bot:**
    ```bash
    python main.py
    ```
