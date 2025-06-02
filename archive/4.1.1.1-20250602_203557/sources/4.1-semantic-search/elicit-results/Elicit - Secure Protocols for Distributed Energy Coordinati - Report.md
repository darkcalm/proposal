

---

Page 1

---

How are agent communication protocols adapted and implemented
for secure, scalable coordination in distributed energy resource
maintenance?
Agent protocols achieve secure and scalable coordination through reinforcement learning, consensus-based
techniques, and negotiation methods, while implementing encryption and hierarchical control structures.
Abstract
Agent communication protocols for distributed energy resource maintenance appear in 25 studies that de-
scribe secure, scalable coordination through distinct design choices. Fourteen studies employ distributed or
decentralized multi-agent architectures—13 with distributed protocols and 8 with decentralized methods—to
support tasks such as fault detection and restoration, self-healing, and economic dispatch. Sixteen studies
validate approaches via simulation, while 5 report field or reference implementations.
Adaptation methods include reinforcement learning (reported in 4 studies), consensus- and leader election–
based techniques (3 studies), and negotiation or rule-based approaches (2 studies each). Security features such
as SSL, VPN, and TLS encryption are integrated in 13 studies, with some emphasizing resilience against
cyber-attacks and communication failures.
Scalability is achieved by clustering, reduced communication
overhead, hierarchical or layered control, and minimal data sharing. Collectively, the papers indicate that
agent protocols adapted through these techniques can support secure, scalable maintenance of distributed
energy resources.
Paper search
Using your research question ”How are agent communication protocols adapted and implemented for secure,
scalable coordination in distributed energy resource maintenance?”, we searched across over 126 million
academic papers from the Semantic Scholar corpus. We retrieved the 499 papers most relevant to the query.
Screening
We screened in papers that met these criteria:
• DER System Focus: Does the study focus on distributed energy resource (DER) systems AND
include aspects of maintenance or system upkeep?
• Multi-Agent Protocol: Does the research investigate communication protocols involving multiple
agents or systems (more than a single agent)?
• Security and Scalability: Does the study address either security mechanisms OR scalability aspects
(or both) in its coordination protocol design?
• Maintenance Coordination: Does the study include specific details about maintenance coordination
or scheduling processes?
• Validation Method: Does the study include empirical data, simulation results, OR validated theo-
retical frameworks?
• Implementation Details: Does the research provide technical implementation details of the proposed
protocols or coordination mechanisms?
• Practical Application: Does the study demonstrate or discuss practical application of the coordina-
tion mechanisms in a DER context?
1


---

Page 2

---

We considered all screening questions together and made a holistic judgement about whether to screen in
each paper.
Data extraction
We asked a large language model to extract each data column below from each paper. We gave the model
the extraction instructions shown below for each column.
• Agent Communication Protocol Type:
Identify and describe the specific type of agent communication protocol used in the study. Look in the
methods or technical approach sections for details about:
• Communication architecture (centralized, decentralized, distributed)
• Communication mechanism (direct neighbor communication, multi-hop communication, etc.)
• Key communication characteristics (autonomy, local view, scalability)
If multiple communication protocols are described, list all. If the protocol is not explicitly named, provide
a detailed description of its key features. If no clear protocol is identified, write ”Not specified”.
• Agent Characteristics and Capabilities:
Extract detailed information about the agents' characteristics from the methods section:
• Types of agents used (e.g., switch agents, energy storage agents, prosumer agents)
• Specific capabilities of each agent type
• Decision-making mechanisms (e.g., reinforcement learning, rule-based)
• Autonomy level and decision-making scope
List each agent type separately with its specific characteristics. If agent details are not clearly defined, note
”Agent characteristics not fully specified”.
• Coordination Mechanism:
Identify how agents coordinate and interact to achieve system objectives:
• Coordination strategy (e.g., distributed optimization, reinforcement learning)
• Information sharing mechanisms
• Coordination constraints or rules
• Performance metrics for coordination
If multiple coordination approaches are described, list all. If coordination is not clearly explained, write
”Coordination mechanism not specified”.
• Scalability and Resilience Characteristics:
Extract information about the protocol's scalability and resilience:
• Maximum number of agents tested
• Performance under different scale conditions
• Resilience to communication failures
• Adaptability to changing system conditions
2


---

Page 3

---

Look in results, discussion, or limitations sections. If scalability is not directly addressed, note ”Scalability
not explicitly evaluated”.
• Energy System Context:
Describe the specific energy system context:
• Type of energy system (smart grid, residential energy, distribution network)
• Specific energy resources involved (distributed energy storage, electric vehicles, flexible loads)
• Operational modes (grid-connected, islanded)
Provide as much detail as possible from the methods and context sections. If system context is unclear, write
”System context not fully specified”.
• Performance Outcomes:
Identify key performance outcomes of the agent communication protocol:
• Quantitative performance metrics (cost reductions, eﬀiciency improvements)
• System-level benefits (reduced congestion, emissions, energy losses)
• Individual agent/prosumer level benefits
Extract numerical values if provided. If no clear outcomes are specified, note ”Performance outcomes not
quantified”.
Results
Characteristics of Included Studies
Study
Study Focus
Protocol Type
Implementation
Scale
Maintenance
Context
Mohammed, 2017
Cyber-physical
systems, communi-
cation/control for
operational
security
Data-centric
middleware,
protocol
translation,
scalable
multi-agent system
Conceptual,
hardware
prototype
Grid/microgrid
protection, electric
vehicle integration,
adaptive
protection
Asgeirsson et al.,
2007
Aggregation/market
integration of
distributed energy
resources
Inter-Control
Center
Communications
Protocol (ICCP),
Secure Sockets
Layer/Virtual
Private Network
(SSL/VPN),
Extensible Markup
Language (XML)
Web Services
Field
demonstration,
more than 20
distributed energy
resources
Distributed energy
resource
aggregation,
economic dispatch,
market
participation
3


---

Page 4

---

Study
Study Focus
Protocol Type
Implementation
Scale
Maintenance
Context
Chouhan, 2017
Multi-agent system
for distribution
automation with
distributed genera-
tion/microgrids
Foundation for
Intelligent Physical
Agents (FIPA),
decentralized
peer-to-peer
Simulation,
real-world test
system
Fault location,
isolation,
restoration (FLIR)
Abdelhamid et al.,
2022
Decentralized
multi-agent system
for self-healing
Decentralized
multi-agent system
(Java Agent
DEvelopment
Framework,
JADE)
Simulation, 22 kV
radial system
Fault detection,
isolation, service
restoration
Jane et al., 2020
Adaptive leader
election for tactical
microgrids
Decentralized,
distributed,
multi-hop
Simulation
Leader election,
optimal power
flow, grid stability
Zhang, No date
found
Multi-agent opti-
mization/learning
for smart/resilient
grids
Distributed,
neighbor
communication,
reinforcement
learning
Conceptual,
simulation
Volt/var control,
power
management,
resilience
Wei, 2019
Multi-agent
system-based
coordination of
microgrids
Decentralized,
consensus, hybrid
Simulation,
multiple
microgrids
Coordination,
economic dispatch,
reliability
Sharma et al., 2017
Distributed control
for energy storage
under cyber-attack
Distributed,
leader-follower,
consensus
Simulation,
medium-voltage
system
Peak shaving,
cyber-attack
resilience
Nguyen and
Flueck, 2012
Agent-based
restoration with
energy storage
Distributed,
autonomous agents
Simulation, IEEE
34-node feeder
Fault detection,
restoration,
islanding
Nazari et al., 2020
Resilient
distributed
frequency control
Distributed,
neighbor/multi-
hop
Simulation,
large-scale grids
Frequency
regulation,
communication
failure resilience
Charbonnier et al.,
2023
Deep multi-agent
reinforcement
learning for
residential
flexibility
Centralized
factored critic,
minimal data
sharing
Simulation, more
than 30 homes
Residential
flexibility, electric
vehicle/heating
coordination
Peskar et al., 2024
Adaptive
agent-based
control for naval
microgrids
Decentralized,
direct neighbor
Simulation, 3
batteries plus
generator
Battery
management,
adaptive strategy
4


---

Page 5

---

Study
Study Focus
Protocol Type
Implementation
Scale
Maintenance
Context
Sharma et al., 2024
Distributed
application
architecture/API
for grid operations
Distributed
layered, Common
Information Model
(CIM)-based API
Conceptual,
reference
implementation
Modular grid
operations,
distributed energy
resource
management
system/advanced
distribution
management
system integration
Das et al., 2024
Adaptive dynamic
programming for
distributed energy
resource
coordination
Reinforcement
learning (adaptive
dynamic
programming,
deterministic
policy gradient),
actor-critic
Simulation, IEEE
123-node
Distributed energy
resource dispatch,
battery energy
storage system life
optimization
Moheuddin et al.,
2009
Scalable,
reconfigurable
distributed
multi-agent system
Decentralized,
FIPA/JADE,
clustering
Simulation, large
power system
Fault identification,
reconfiguration
García et al., 2010
Agent-based
distributed
smart-grid
management
Distributed,
event-driven,
middleware
Field-tested, large
deployments
Network
management,
device
configuration,
monitoring
Charbonnier et al.,
2022
Scalable
multi-agent
reinforcement
learning for
residential energy
Decentralized,
Q-learning, fixed
Q-tables
Simulation
Residential
flexibility, electric
vehi-
cle/heating/loads
Schmutzler et al.,
2011
Web services for
distributed energy
resources in IEC
61850
Distributed,
Devices Profile for
Web Services
(DPWS), Web
Services (WS-*)
Proof-of-concept,
electric vehicle use
case
Distributed energy
resource
integration,
plug-and-play,
asset management
Sun and Ye, 2011
Scalable
multi-agent system
communications
for islanded
microgrids
Distributed,
token-ring,
multi-hop
Simulation
Microgrid
communications,
failure detection
5


---

Page 6

---

Study
Study Focus
Protocol Type
Implementation
Scale
Maintenance
Context
Sampaio et al.,
2020
Multi-agent
system-based self-
healing/adaptive
protection
Distributed,
negotiation
Test bench, digital
relays
Self-healing,
adaptive
protection,
distributed
generation
Yang et al., 2021
Multi-agent
system-based
optimal load
restoration
Distributed,
peer-to-peer,
consensus
Simulation
Critical load
restoration,
distributed energy
resources
Al-Hinai and
Alhelou, 2021
Multi-agent system
for restoration in
smart grids
Decentralized
(JADE), binary
integer linear
programming
Simulation,
14/70-bus
Fault location,
isolation,
restoration
Ding et al., 2022
Federated
architecture for
distributed energy
resource
management
systems
Distributed/federated,
hierarchical
Conceptual,
system-level
specifications
Distributed energy
resource
aggregation,
economic dispatch,
transmission and
distribution
services
Bhattacharya et
al., 2019
Incentive-based
distributed energy
resource
coordination
Hierarchical,
ZeroMQ (ZMQ)
publish/subscribe,
VPN
Simulation, more
than 10,000
devices
Frequency
response,
regulation,
ramping
Mihailescu et al.,
2011
Dynamic coalition
for virtual power
stations
Distributed,
coalition formation
Conceptual,
algorithmic
Virtual power
station creation,
adaptation,
stability
Across 25 studies of multi-agent system protocols for grid and distributed energy resource management, the
following patterns were observed:
• Protocol Type:
– Distributed multi-agent system approaches were most common (13 studies).
– Decentralized multi-agent system protocols were used in 8 studies.
– Middleware, web services, or API-based protocols (including FIPA, JADE, ICCP, DPWS, CIM,
and others) were found in 10 studies.
– Centralized or hierarchical architectures were used in 3 studies.
– Reinforcement learning or other optimization-based protocols were found in 4 studies.
– Hybrid or other approaches (such as consensus or coalition formation) were found in 4 studies.
• Implementation Scale:
– 16 studies used simulation only.
6


---

Page 7

---

– 2 studies combined simulation with real-world test systems or hardware prototypes.
– 5 studies were field-tested, bench-tested, or included a reference implementation.
– 2 studies were conceptual or algorithmic only.
• Maintenance Context (Application Domain):
– Fault detection, restoration, self-healing, or adaptive protection was addressed in 8 studies.
– Distributed energy resource or market aggregation, dispatch, or coordination was addressed in 8
studies.
– Grid or microgrid stability, operation, or optimization was addressed in 6 studies.
– Residential flexibility, electric vehicle, heating, or load management was addressed in 2 studies.
– Battery or energy storage management was addressed in 3 studies.
– Communication, cybersecurity, or resilience was addressed in 2 studies.
– Network or device management or asset management was addressed in 2 studies.
We did not find mention of implementation scale information for studies outside these categories, and some
studies addressed multiple protocol types or application domains.
Thematic Analysis
Protocol Adaptation Mechanisms
Study
Protocol Type
Adaptation
Method
Security Features
Scalability
Approach
Mohammed, 2017
Data-centric
middleware,
protocol
translation
Adaptive
protection,
protocol gateway
Cybersecurity
testbeds, resilience
to attacks
Scalable
cloud-based
multi-agent system,
multi-lingual
system
Asgeirsson et al.,
2007
ICCP, SSL/VPN,
XML Web Services
Standard protocol
integration, market
procedures
SSL, VPN, secure
communications
Standards-based
technology,
aggregation,
process historian
Chouhan, 2017
FIPA,
decentralized
peer-to-peer
Q-learning, hybrid
control
No mention found
Hierarchical
multi-agent system,
reduced
communication
overhead
Abdelhamid et al.,
2022
Decentralized
multi-agent system
(JADE)
Expert rules, agent
specialization
No mention found
Fully decentralized,
agent types (zone,
feeder, microgrid)
Jane et al., 2020
Decentralized,
distributed,
multi-hop
Adaptive leader
election,
desirability index
No mention found
Communication
complexity
reduction (2N)
7


---

Page 8

---

Study
Protocol Type
Adaptation
Method
Security Features
Scalability
Approach
Zhang, No date
found
Distributed,
neighbor
communications,
reinforcement
learning
Model-free
reinforcement
learning, bi-level,
consensus
Privacy-preserving,
safe reinforcement
learning
Distributed
optimization, local
data only
Wei, 2019
Decentralized,
consensus, hybrid
Evolutionary/genetic
algorithms,
consensus
No mention found
Coordination area
selection, scalable
multi-agent system
Sharma et al., 2017
Distributed,
leader-follower,
consensus
Fuzzy logic
deviation detection
Cyber-attack
resilience
Arbitrary topology,
consensus-based
control
Nguyen and
Flueck, 2012
Distributed,
autonomous agents
Local view,
autonomy
No mention found
Fully distributed,
scalable
Nazari et al., 2020
Distributed,
neighbor/multi-
hop
Dynamic
communication
hops, resilient
distributed
frequency
regulation
Resilience to
communication
failures
Scalable to large
grids, local
communications
Charbonnier et al.,
2023
Centralized
factored critic,
minimal data
Deep reinforcement
learning, factored
critic
Privacy (no data
sharing)
Minimal
communications,
scalable
reinforcement
learning
Peskar et al., 2024
Decentralized,
direct neighbor
Adaptive strategy
mapping
No mention found
Priority-based run
order, small-scale
Sharma et al., 2024
Distributed
layered,
CIM-based API
Laminar
coordination,
modular
applications
Securability,
standards-based
Layered,
extensible, scalable
APIs
Das et al., 2024
Reinforcement
learning (adaptive
dynamic
programming,
deterministic
policy gradient),
actor-critic
Off-policy
deterministic
policy gradient,
policy-based
exploration
No mention found
IEEE 123-node,
scalable
reinforcement
learning
Moheuddin et al.,
2009
Decentralized,
FIPA/JADE,
clustering
Spectral clustering,
cost function
No mention found
Cluster agents,
reduced
communication
overhead
García et al., 2010
Distributed,
event-driven,
middleware
Rule-engines, data
ontologies
Secure
measurement
retrieval
Event-bus, agent
specialization
8


---

Page 9

---

Study
Protocol Type
Adaptation
Method
Security Features
Scalability
Approach
Charbonnier et al.,
2022
Decentralized,
Q-learning, fixed
Q-tables
Off-line convex
optimization,
reward isolation
No data sharing
Fixed Q-tables,
scalable
reinforcement
learning
Schmutzler et al.,
2011
Distributed,
DPWS, WS-*
Plug-and-play,
protocol mapping
WS-* compliance
Dynamic
distributed energy
resource discovery,
scalable
Sun and Ye, 2011
Distributed,
token-ring,
multi-hop
Token-ring, failure
detection
Failure detection
Parallelized
message
propagation
Sampaio et al.,
2020
Distributed,
negotiation
Negotiation,
adaptive
protection
No mention found
Multi-agent
system,
negotiation,
adaptive settings
Yang et al., 2021
Distributed,
peer-to-peer,
consensus
Min/max-
consensus, bias
min-consensus
No mention found
Peer-to-peer,
adaptive to
topology
Al-Hinai and
Alhelou, 2021
Decentralized
(JADE), binary
integer linear
programming
Pre-calculation,
binary integer
linear
programming
No mention found
Decentralized,
scalable to 70-bus
Ding et al., 2022
Distributed/federated,
hierarchical
Federated resource
scheduling,
constrained
dispatch
Secure, federated
Substation-level
aggregation
Bhattacharya et
al., 2019
Hierarchical, ZMQ
publish/subscribe,
VPN
Multi-objective
optimization,
aggregator
hierarchy
VPN, Transport
Layer Security
(TLS) encryption
More than 10,000
devices,
co-simulation
Mihailescu et al.,
2011
Distributed,
coalition formation
Dynamic coalition,
negotiation
No mention found
Open-ended
adaptation,
coalitional games
Protocol Type:
• Distributed protocol types were the most common, found in 13 studies.
• Decentralized approaches were used in 8 studies.
• Reinforcement learning-based protocols were found in 4 studies.
• Hierarchical, peer-to-peer, and multi-hop protocols were each found in 2–3 studies.
• Middleware, federated, layered, FIPA, JADE, clustering, event-driven, centralized, hybrid, ZMQ,
DPWS/WS-*, token-ring, binary integer linear programming, and coalition formation were each found
in 1–3 studies.
9


---

Page 10

---

• We found protocol type information for all studies.
Adaptation Method:
• Reinforcement learning-based adaptation (including Q-learning, deep reinforcement learning, model-
free reinforcement learning, actor-critic, off-policy) was used in 4 studies.
• Consensus-based adaptation (including min/max-consensus, leader election) was found in 3 studies.
• Negotiation and rule-based/expert rules were each found in 2 studies.
• Other adaptation methods (clustering, evolutionary/genetic, fuzzy logic, protocol mapping/integration,
adaptive
protection/strategy,
modular/laminar,
multi-objective
optimization,
coalition,
pre-
calculation/binary integer linear programming, plug-and-play, failure detection, market procedures,
data ontologies, cost function, aggregator hierarchy, dynamic communications, reward isolation,
convex optimization, factored critic, local view/autonomy, federated resource scheduling, constrained
dispatch) were each found in 1 study.
• We found adaptation method information for all studies.
Security Features:
• Security features were specified in 13 studies.
– Of these, resilience to attacks or communication failures was mentioned in 3 studies.
– Privacy or no data sharing was mentioned in 3 studies.
– Encryption (SSL, VPN, TLS) was mentioned in 2 studies.
– Secure or federated approaches were found in 2 studies.
– Secure measurement retrieval, WS-* compliance, securability/standards-based, and failure detec-
tion were each found in 1 study.
• We did not find mention of security features in 12 studies.
Scalability Approach:
• Distributed or decentralized scalability approaches were found in 7 studies.
• Scalable reinforcement learning approaches were found in 3 studies.
• Reduced communication overhead was found in 3 studies.
• Aggregation and local communication/data approaches were each found in 2 studies.
• Hierarchical, cloud-based, layered/extensible, large-scale (more than 10,000 devices), event-bus,
priority-based, small-scale, peer-to-peer, adaptive topology/settings, fixed Q-tables, dynamic discov-
ery, parallelized, multi-agent system, substation-level, co-simulation, open-ended/coalitional games,
IEEE 123-node, and agent specialization/types were each found in 1 study.
• We found scalability approach information for all studies.
Coordination Architectures
Study
Architecture Type
Communication
Model
Resource
Management
Performance
Metrics
Mohammed, 2017
Centralized/decentralized
hybrid
Data-centric bus,
protocol
translation
Microgrid/electric
vehicle control,
adaptive
protection
No mention found
10


---

Page 11

---

Study
Architecture Type
Communication
Model
Resource
Management
Performance
Metrics
Asgeirsson et al.,
2007
Centralized with
distributed
elements
ICCP, web services
Distributed energy
resource
aggregation,
economic dispatch
Market
participation,
operational control
Chouhan, 2017
Hybrid (central-
ized/decentralized)
FIPA, peer-to-peer
Fault location,
isolation,
restoration, switch
optimization
Agent
communications,
restoration speed
Abdelhamid et al.,
2022
Decentralized
multi-agent system
JADE, agent
communications
Self-healing,
distributed
generation
management
No mention found
Jane et al., 2020
Decentralized
Distributed,
multi-hop
Leader election,
power flow
Communication
complexity (2N)
Zhang, No date
found
Distributed,
hierarchical
Neighbor
communications,
leader-follower
Volt/var, power
management,
resilience
No mention found
Wei, 2019
Decentralized/hybrid Consensus, market
Microgrid
coordination,
economic dispatch
Reliability,
scalability
Sharma et al., 2017
Distributed
Leader-follower,
consensus
Distributed energy
storage system
peak shaving
No mention found
Nguyen and
Flueck, 2012
Distributed
Local agent
communications
Restoration,
islanding
No mention found
Nazari et al., 2020
Distributed
Neighbor/multi-
hop
Frequency
regulation
Stability, fair
power sharing
Charbonnier et al.,
2023
Centralized critic,
distributed agents
Minimal
communications
Residential
flexibility
Training time, user
savings
Peskar et al., 2024
Decentralized
Direct neighbor
Battery/generator
management
Battery/generator
remaining useful
life, temperature
Sharma et al., 2024
Distributed layered
CIM-based API
Modular grid
operations
No mention found
Das et al., 2024
Distributed
reinforcement
learning
Actor-critic
Distributed energy
resource/battery
energy storage
system dispatch
Optimization gap,
cost savings
Moheuddin et al.,
2009
Decentralized,
clustered
FIPA/JADE,
cluster
communications
Fault
reconfiguration
Communication
overhead, decision
time
García et al., 2010
Distributed
Event-bus,
rule-engines
Network
management,
configuration
No mention found
11


---

Page 12

---

Study
Architecture Type
Communication
Model
Resource
Management
Performance
Metrics
Charbonnier et al.,
2022
Decentralized
Q-learning, fixed
Q-tables
Residential
flexibility
Cost, congestion,
emissions
Schmutzler et al.,
2011
Distributed
DPWS, WS-*
Distributed energy
resource
plug-and-play
Latency, scalability
(qualitative)
Sun and Ye, 2011
Distributed
Token-ring,
multi-hop
Microgrid
communications
No mention found
Sampaio et al.,
2020
Distributed
Negotiation
Self-healing,
adaptive
protection
No mention found
Yang et al., 2021
Distributed
Peer-to-peer,
consensus
Load restoration
No mention found
Al-Hinai and
Alhelou, 2021
Decentralized
JADE, binary
integer linear
programming
Restoration
Computational
eﬀiciency
Ding et al., 2022
Distributed/federatedHierarchical,
federated resource
scheduling
Distributed energy
resource
aggregation,
dispatch
No mention found
Bhattacharya et
al., 2019
Hierarchical
ZMQ
publish/subscribe,
VPN
Frequency,
regulation,
ramping
Response time,
reserve targets
Mihailescu et al.,
2011
Distributed
Coalition
formation
Virtual power
station creation,
adaptation
Stability
(qualitative)
Architecture Type:
• Distributed architectures were found in 13 studies.
• Decentralized architectures were found in 7 studies.
• Hybrid, hierarchical, layered, federated, or clustered architectures were found in 10 studies.
• Many studies described more than one architecture type (such as hybrid or layered).
Communication Model:
• Peer-to-peer, neighbor, or local agent communication was found in 7 studies.
• Consensus, leader-follower, negotiation, or coalition-based communication was found in 8 studies.
• Bus, event-bus, or protocol translation models were found in 2 studies.
• Web services, APIs, publish-subscribe, or token-ring models were found in 5 studies.
• JADE, FIPA, or agent-based communication frameworks were found in 4 studies.
• Market-based communication was found in 1 study.
• Minimal communication was found in 1 study.
• We found 2 studies using other models such as Q-learning or actor-critic.
Resource Management Approaches:
12


---

Page 13

---

• Distributed energy resource management, aggregation, dispatch, or plug-and-play was found in 5 stud-
ies.
• Microgrid, islanding, restoration, or self-healing was found in 5 studies.
• Flexibility management (residential or load) was found in 2 studies.
• Battery or generator management was found in 1 study.
• Frequency or voltage regulation was found in 2 studies.
• Peak shaving, economic dispatch, or market participation was found in 2 studies.
• Fault reconfiguration was found in 1 study.
• Other resource management approaches (such as network management, leader election, modular oper-
ations, etc.) were found in 7 studies.
Performance Metrics:
• We found quantified performance metrics in 14 studies (including measures such as cost, latency, re-
sponse time, scalability, user savings, and others).
• We did not find mention of quantified performance metrics in 11 studies.
Security and Scalability Integration
• Security and scalability are often addressed together in protocol adaptation, with a focus on:
– Resilience to cyber-attacks and communication failures (e.g., through protocol-level security such
as Secure Sockets Layer, Virtual Private Network, Web Services compliance).
– Middleware for secure data exchange.
– Design choices that minimize communication, such as fixed Q-tables or local-only data.
• Scalability is achieved through:
– Clustering.
– Hierarchical control.
– Distributed optimization.
– Minimal data sharing.
• Empirical validation is limited :
– Explicit evaluation of security outcomes is rare.
– Quantitative scalability metrics are inconsistently reported.
• Included studies support the feasibility of secure, scalable agent communication, but the available
evidence base is limited in empirical validation.
Maintenance-Specific Implementations
• Maintenance contexts addressed in the included studies:
– Fault detection, isolation, restoration, self-healing, and adaptive protection.
– Economic dispatch and resource allocation.
• Protocol adaptation for maintenance :
– Rapid restoration is supported by agent-based protocols (e.g., Chouhan, Yang, Al-Hinai).
– Resilience to faults and cyber-attacks is a focus in several studies (e.g., Sharma et al., Nazari,
Mohammed).
13


---

Page 14

---

– Eﬀicient resource allocation is addressed in studies on aggregation and dispatch (e.g., Asgeirsson,
Bhattacharya, Das).
• Agent-based approaches enable :
– Local autonomy.
– Rapid response.
– Adaptability to changing system conditions.
• Comparability and evaluation :
– The diversity of maintenance tasks and system contexts in the included studies complicates direct
comparison.
– Few studies provide comprehensive, quantitative evaluation of maintenance outcomes.
References
A. Al-Hinai, and Hassan Haes Alhelou. “A Multi-Agent System for Distribution Network Restoration in
Future Smart Grids.” Energy Reports, 2021.
A. Bhattacharya, Jacob Hansen, K. Kalsi, Jianming Lian, S. Nandanoori, M ReeveHayden, Adetola Veronica,
et al. “Incentive-Based Control and Coordination of Distributed Energy Resources,” 2019.
A. García, Juan Oliver, and D. Gosch. “An Intelligent Agent-Based Distributed Architecture for Smart-Grid
Integrated Network Management.” IEEE Local Computer Network Conference, 2010.
Ahmed Maged Abdelhamid, N. Zakzouk, and S. E. El Safty. “A Multi-Agent Approach for Self-Healing and
RES-Penetration in Smart Distribution Networks.” Mathematics, 2022.
Avijit Das, Di Wu, Bilal Ahmad Bhatti, and Mohamed Kamaludeen. “Approximate Dynamic Programming
With Enhanced Off-Policy Learning for Coordinating Distributed Energy Resources.” IEEE Transactions
on Sustainable Energy, 2024.
C. Nguyen, and A. Flueck. “Agent Based Restoration With Distributed Energy Storage Support in Smart
Grids.” IEEE Transactions on Smart Grid, 2012.
D. Sharma, S. Singh, Jeremy Lin, and Elham Foruzan.
“Agent-Based Distributed Control Schemes for
Distributed Energy Storage Systems Under Cyber Attacks.” IEEE Journal on Emerging and Selected
Topics in Circuits and Systems, 2017.
F. C. Sampaio, R. Leão, R. F. Sampaio, L. S. Melo, and G. Barroso. “A Multi-Agent-Based Integrated Self-
Healing and Adaptive Protection System for Power Distribution Systems with Distributed Generation,”
2020.
F. Charbonnier, Bei Peng, Thomas Morstyn, and M. Mcculloch. “Centralised Rehearsal of Decentralised
Cooperation: Multi-Agent Reinforcement Learning for the Scalable Coordination of Residential Energy
Flexibility.” Applied Energy, 2023.
F. Charbonnier, Thomas Morstyn, and M. Mcculloch. “Scalable Multi-Agent Reinforcement Learning for
Distributed Control of Residential Energy Flexibility.” Applied Energy, 2022.
Fei Ding, Weijia Liu, Jason S. MacDonald, James Ogle, Annabelle Pratt, and M. Baggu.
“Federated
Architecture for Secure and Transactive Distributed Energy Resource Management Solutions (FAST-
DERMS),” 2022.
H. Asgeirsson, R. Seguin, Cameron Sherding, Andre G. de Bruet, R. Broadwater, and M. Dilek. “Advanced
Communication and Control Solutions of Distributed Energy Resources (DER),” 2007.
Hongbin Sun, and Xue Ye. “A Micro-Grid Communication Mechanism in Distributed Power System.” In-
ternational Conference on Applied Informatics and Communication, 2011.
J. Schmutzler, Sven Gröning, and C. Wietfeld. “Management of Distributed Energy Resources in IEC 61850
Using Web Services on Devices.” IEEE International Conference on Smart Grid Communications, 2011.
14


---

Page 15

---

Jarrett Peskar, Braden Priddy, Kerry Sado, Austin R. J. Downey, Kristen Booth, and Jamil Khan. “Adaptive
Agent-Based Control for Lithium-Ion Batteries in Naval Microgrids.” Design Automation Conference,
2024.
Jinshou Wei.
“Modeling and Coordination of Interconnected Microgrids Using Distributed Artificial In-
telligence Approaches.
(Modélisation Et Coordination de Micro-Réseau Interconnectées En Utilisant
l'intelligence Artificielle Distribuée),” 2019.
Lun Yang, Yinliang Xu, Hongbin Sun, M. Chow, and Jianguo Zhou. “A Multiagent System Based Optimal
Load Restoration Strategy in Distribution Systems,” 2021.
M. Nazari, L. Wang, S. Grijalva, and M. Egerstedt.
“Communication-Failure-Resilient Distributed Fre-
quency Control in Smart Grids: Part II: Algorithmic Implementation and System Simulations.” IEEE
Transactions on Power Systems, 2020.
O. Mohammed.
“Keynote Lecture III: Energy Cyber Physical Systems and Their Communication and
Control Challenges for Operational Security in Power Systems.” International Middle East Power Systems
Conference, 2017.
Poorva Sharma, A. Reiman, Alexander A. Anderson, Shiva Poudel, C. Allwardt, Andrew Fisher, Tylor E.
Slay, et al. “GridAPPS-D Distributed App Architecture and API for Modular and Distributed Grid
Operations.” IEEE Access, 2024.
Qianzhi Zhang. “Multi-Agent Optimization and Learning Methods for Sustainable, Smart and Resilient
Power Distribution Systems and Microgrids,” n.d.
R. Mihailescu, Matteo Vasirani, and Sascha Ossowski. “Dynamic Coalition Formation and Adaptation for
Virtual Power Stations in Smart Grids,” 2011.
Robert S Jane, S. Goldsmith, G. Parker, W. Weaver, and Denise M. Rizzo. “Adaptive Leader Election
for Control of Tactical Microgrids.” The Journal of Defence Modeling and Simulation: Applications,
Methodology, Technology, 2020.
S. Chouhan. “A Multi-Agent Design for Smart Distribution Automation System with Distributed Energy
Resources and Microgrids,” 2017.
Summiya Moheuddin, A. Noore, and M. Choudhry.
“A Reconfigurable Distributed Multiagent System
Optimized for Scalability,” 2009.
15
