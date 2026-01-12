## ***Blockchain***
Blockchain is a distributive, immutable, ledger technology which is transparent and one of the disruptive technologies which added another defination of trust on internet.

### ***Applications***
- **Financial Services**: Blockchain streamlines operations in banking and finance by enabling faster, cheaper cross-border payments, more efficient trade finance, and secure asset tokenization. It also supports the development of Central Bank Digital Currencies (CBDCs) and Decentralized Finance (DeFi) platforms, which operate without traditional intermediaries.
- **Supply Chain Management**: Companies use blockchain to track products from origin to consumer, which helps verify authenticity, ensure ethical sourcing (e.g., "Fair Trade" or "Organic" labels), and quickly identify issues during food safety concerns.
- **Healthcare**: It is used to securely manage and share patient medical records, track pharmaceuticals through the supply chain to prevent counterfeit drugs, and ensure data integrity in clinical trials.
- **Real Estate**: Blockchain simplifies the process of recording property deeds and managing titles by creating a permanent, tamper-proof record of ownership, which can reduce costs and processing times associated with manual paperwork.
- **Smart Contracts**: These self-executing contracts, with terms directly written into code, automatically trigger actions when conditions are met. They have applications in insurance claim processing, real estate agreements, and various automated business processes.
- **Digital Identity and Voting**: The technology can provide secure, verifiable digital identities, giving individuals more control over their personal data. In elections, it has the potential to facilitate secure, tamper-proof digital voting systems, making fraud more difficult and results nearly instant.
- **Intellectual Property Protection**: Artists and content creators can use blockchain to register their original work and track royalty payments, ensuring they receive due credit and compensation for their creations.
---


## ***Hashing***
Making blocks encrypted. Each block contains timestamp of creation, data, hash of the prev block and hash of that block.

### ***5 requirements of hash algos***
- Deterministic (one hash for one data)
- One way (data ---> hash -x-> data)
- Fast computation
- Avalanche effect (complete change in hash for a minimal change in data)
- Withstand collision (tough to hack)
---

## ***Immutable Ledger***
Change in one block creates notable chnage in successor blocks in the chain helps to identify any hacker corruption and rewash the block.
---

## ***P2P Network***
A decentralized system where individual computers (nodes) connect and transact directly, without a central server, forming a shared, distributed digital ledger
---

## ***Byzantine Grnaral Problem***
A classic thought experiment in distributed computing about achieving consensus (agreement) among unreliable participants (generals/nodes) who might be traitors.
It's proven that making true dicision becomes impossible when 1/3 of the genarals are traitors
---

## ***Consensus Protocols***
Mechanisms used in blockchain networks to achieve agreement among distributed nodes on the state of the ledger, ensuring data integrity and security without a central authority.
- **Proof of Work (PoW)**: Miners solve complex mathematical puzzles to validate transactions and create new blocks, requiring significant computational power and energy.
- **Proof of Stake (PoS)**: Validators are chosen to create new blocks based on the amount of cryptocurrency they hold and are willing to "stake" as collateral, reducing energy consumption compared to PoW.
- **Delegated Proof of Stake (DPoS)**: Token holders vote for a small number of delegates who are responsible for validating transactions and creating new blocks, enhancing scalability and efficiency.
- **Practical Byzantine Fault Tolerance (PBFT)**: A consensus algorithm designed to function efficiently in environments where nodes may act maliciously, ensuring agreement as long as less than one-third of the nodes are faulty.
- **Competative chain acceptance**: The longest chain in the network is accepted as the valid one.

After block mining (POW), the block is added to the chain of all the nodes in the network through some acceptance criteria, which prevents malicious attacks