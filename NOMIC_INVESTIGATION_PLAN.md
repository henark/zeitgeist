# Nomic and nBTC: Investigation Plan

This document outlines the initial research plan for the `nomic-io/nomic` repository and the `nBTC` token. This investigation will serve as a practical case study to inform the design of the "Bitcoin Reimagined" hybrid governance system.

## Research Targets

The first phase of the investigation will be a detailed study of the repository. The primary targets for this research are:

1.  **`README.md`:** To get a high-level overview of the Nomic project, its mission, and its core value proposition.

2.  **`nBTC` Documentation:** A deep dive into any dedicated documentation (e.g., in a `docs/` folder or a specific `nbtc.md` file) to answer the following key questions:
    *   **Technical Specification:** What is the nature of the `nBTC` token (e.g., IBC token, wrapped ERC-20)?
    *   **Bridge Architecture:** How does the bridge connecting Bitcoin to the Nomic chain function?
    *   **Security Model:** What are the trust assumptions and security guarantees of the bridge?

3.  **Source Code:** An analysis of the source code for the `nBTC` bridge and token contracts to understand their low-level implementation.

4.  **Governance Documentation:** A review of any documents explaining the governance model of the Nomic chain, which will provide crucial context for the subsequent analysis of the project's community issues.

This research will provide the foundational knowledge required to analyze Nomic's governance challenges and apply those lessons to our own design.
