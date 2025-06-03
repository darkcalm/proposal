# Connecting Distributed Pockets of Energy Flexibility through Federated Computations  Limitations and Possibilities

## Paper Metadata

- **Filename:** Connecting_Distributed_Pockets_of_Energy_Flexibility_through_Federated_Computations__Limitations_and_Possibilities_DOI_10-1109_icmla51294-2020-00186.pdf
- **DOI:** 10.1109/icmla51294.2020.00186
- **Authors:** Not available
- **Year:** Not available
- **Journal/Venue:** Not available
- **URL:** Not available
- **Extraction Date:** 2025-06-03T15:01:23.097004
- **Total Pages:** 6

## Abstract

Abstract not available from BibTeX metadata.

## Keywords

Keywords not available from BibTeX metadata.

---

## Full Text Content



### Page 1

Connecting Distributed Pockets of Energy
Flexibility through Federated Computations:
Limitations and Possibilities
Javad Mohammadi
Carnegie Mellon University
Pittsburgh, PA, USA
jmohamma@andrew.cmu.edu
Jesse Thornburg
Grid Fruit
Pittsburgh, PA, USA
jesse@gridfruit.com
Abstract—Electric grids are traditionally operated as multientity systems with each entity managing a geographical region.
Interest and demand for decarbonization and energy democratization is resulting in growing penetration of controllable energy
resources. In turn, this process is increasing the number of grid
entities. The paradigm shift is also fueled by increased adoption of
intelligent sensors and actuators equipped with advanced processing and computing capabilities. While collaboration among power
grid entities (agents) reduces energy cost and increases overall
reliability, achieving effective collaboration is challenging. The
main challenges stem from the heterogeneity of system agents and
their collected information. Furthermore, the scale of data collection is constantly increasing and many grid entities have strict
privacy requirements. Another challenge is the energy industry’s
common practice of keeping data in silos. Federated computation
is an approach well suited to addressing these issues that are
increasingly important for multi-agent energy systems. Through
federated computation, agents collaboratively solve learning and
optimization problems while respecting each agent’s privacy and
overcoming barriers of cross-device and cross-organization data
isolation. In this paper, we ﬁrst establish the need for federated
computations to achieve energy optimization goals of the future
power grid. We discuss practical challenges of performing multiagent data processing in general. Then we address challenges
that arise speciﬁcally for orchestrating operation of connected
distributed energy resources (DERs) in the Internet of Things
(Io T). We conclude this paper by presenting a novel federated
computation framework that addresses some of these issues, and
we share examples of two initial ﬁeld test setups in research
demonstrations and commercial building applications with Grid
Fruit LLC.
Index Terms—Federated Computations, Energy Efﬁciency,
Distributed Energy Resources, Distributed Optimization, Smart
Grid, Internet of Things, Multi-Agent Systems, Electric Grid
I. INTRODUCTION
The future electric delivery infrastructure is expected to
differ from the existing system by increased penetration of
Distributed Energy Resources (DERs) for example solar photovoltaic (PV) systems, electric vehicles (EVs) and energy
storage systems. DERs are multiplying across the Americas,
Europe, and Africa [1], [2]. The rollout is accompanied by
widespread adoption of advanced sensing, actuation, computation and communication technologies. While the physical infrastructure and energy exchanges will continue to be
administrated and overseen by the grid operator, a central
entity, the architecture of the future grid is being designed to
accommodate increasing demand for energy democratization
and end-use engagement [3]. Electrical utilities and regulators
are updating many long-standing practices to meet these
demands and interests. For example, the architecture of nascent
Transactive Energy (TE) systems [4] allows a wide range of
power grid entities (from homeowners with solar PV to grid
operators) to collaborate and compete to provide cost-effective
electricity with high reliability [5].
Flexibility in production and consumption (also known as
prosumption) will play a critical role in preserving reliability
and resilience of the future power grids that are characterized
by high penetration of intermittent energy sources (e.g., solar
PV) [6], [7]. Here, ﬂexibility refers to the ability of a DER to
adjust prosumption levels in a desired amount of time.
In parallel, resilience challenges face the future grid as
cybersecurity and environmental threats are growing [8], [9].
Power system resilience is typically deﬁned as the capability
of a system to maintain its functionality and characteristics
after a disturbance [10]. In a power grid context, a disturbance
often manifests as a brownout (drop in voltage) or blackout
(power outage) [11]. Identifying and aggregating ﬂexibilities
offered by power grid entities is commonly viewed as the
viable solution for avoiding these disturbances and operating
a reliable, resilient and climate friendly grid [12].
Federated computation is an approach key to both optimal
DER dispatch and energy resilience in the future grid. Federated analytics and collaborative, distributed decision-making
will act as the glue to connect different pieces of the future grid
together, especially those connected in the Internet of Things
(Io T). In other words, federated computations enable leverage Io T-connected DERs and entities (with near-ubiquitous
communication and computation capabilities) to aggregate
spatiotemporal ﬂexibility of geographically-dispersed DERs.
This aggregation allows control at a scale to provide this future
grid with much-needed energy resilience [7].
Federated computations in multi-agents systems are studied
in different contexts. In this regard, distributed optimization
and decentralized learning are established directions. The
interest in these methodologies is driven by the need to
ar Xiv:2009.10182v1 [cs.DC] 21 Sep 2020

---


### Page 2

develop scalable optimization and learning solutions to deal
with large datasets [13], address privacy and security concerns
[14], and manage multi-agent systems [15]. The architecture
of existing distributed optimization methods falls into two
categories based whether the methods depend on a central
agent to oversee computations and optimization. In the case
where a central agent is responsible for regulating updates and
computation among agents, all other agents are required to
directly share updates with that central entity. As an example,
Alternating Direction Method of Multipliers (ADMM) is a
commonly used method that decomposes the original problem
into sub-problems and a master problem. The ADMM setup
requires each agent to solve an optimization sub-problem and
share updates with the central agent. The central agent then
updates the update functions of the master problem [16].
Distributed optimization and distributed learning are closely
related. Distributed learning methods orchestrate cross-agent
computations
that
enable
collaboration
in
mining
large
datasets. These models often map the multi-agent setups to
graph environments where nodes represents learning agents.
Data may reside on nodes or edges of the representative graph
[17]. Recent works in this regards have investigated using
proximal gradient methodologies [18], ADMM-based methods
[19], or stochastic gradient decent (SGD) approaches [20],
Federated analytics has received tremendous attention recently. Federated learning is a multi-agent setup thorough
which multiple entities collaborate to solve a machine learning
problem. A central coordinator often regulates this process
and communicates with the system’s agents. Each entity
keeps its raw data in conﬁdence, performs local updates, and
shares model updates only with the central entity. This iterative process allows cross-device and cross-institution model
training [21], [22]. Edge computation has been studied and
implemented in limited capacities (e.g., with fog computing
and query processing [23]–[25]). However, increasing computational and data storage capabilities of the edge devices
allow inference and training tasks to be conducted locally [22].
Using federated analytics across agents with heterogeneous
hardware and statistical data is an active research area [26].
Organizations are often reluctant to share their data, even
though sharing the knowledge and resulting insights beneﬁts
all involved parties. For example, anti-money-laundering initiatives will greatly beneﬁt from mining the data of different
ﬁnancial institutions. However, requesting access to sensitive
client information is an ever-present obstacle. Federated learning can enable joint ﬁnancial analysis among these institutions
without sharing any customer data. Another example is the
collaborative efforts to reduce carbon emissions. Large building portfolios are major contributors to greenhouse gas (GHG)
emissions, however management ﬁrms are not willing to share
their energy and environmental data. They fear that doing
so will advantage their competitors by revealing information
about their building occupancies.
Federated analytics is an effective tool for breaking
these cross-device and cross-institutional silos. The approach
promises to be extremely useful in the context of future energy
systems with numerous Io T-connected DERs connecting and
disconnecting from the grid at any given time, especially with
the DERs in different locations and under different supervision
and organization.
In this paper, we ﬁrst discuss how the electric power grid
is evolving towards a multi-agent system with heterogeneous
agents. From literature, including prior research works, we
establish the need for federated computation across everincreasing energy resources in section II. We begin section
III by highlighting the challenges of implementing federated
computation framework in Io T setups, speciﬁcally in Io Tconnected DERs. We then build on [12], [17] and presents
a novel federated computation method that is well suited to
address the needs of future multi-agent grid. The proposed
method enables agents to collaboratively perform a personalized and agent-speciﬁc computation while maintaining data
privacy. In section IV, we describe implementations possibilities of the above-described methods in research (through
the Carnegie PLUG testbed) and commercialization (partnering
with grid services company Grid Fruit LLC).
II. THE FUTURE PLUG-AND-PLAY GRID
The electric power grid is one of the most complex manmade systems in the world [27]. This system spans multiple
states, countries, and entire continents. Control responsibilities
for this network are shared among different entities. The
decision-making process occurs at different scales and across
multiple spatiotemporal dimensions. The energy management
paradigms of the electric grid are traditionally designed to
regulate and manage a limited number of decision-making
entities. Entities often control assets in a speciﬁc geographical
area [28]. Interactions between these entities depend on the
policies and rules governing power grid operation in these
areas as well as prearranged bilateral agreements. The lack
of coordination to optimize cross-entity energy resources inevitably results in suboptimal system dispatch.
The future electric power grid infrastructure is emerging
with a complexity that requires it be composed of many
interacting elements. As the grid evolves, its new architecture
should accommodate and manage an ensemble of constituent
parts while ensuring interoperability and resilience. The future
grid should enable plug-and-play engagement and manage
heterogeneous energy resources under stress and uncertainty
[29]. The main trends behind this transition include evolving
consumer expectations and technological progress. Economies
of distributed electric networks are emerging at the same time,
as well as growing needs for resilience given cybersecurity and
environmental threats [6].
Customers expect increased access to information and a
high level of service from the twenty-ﬁrst century power
infrastructure. These expectations are elevated partly because
outside the power sector, third party providers are offering
increased choice and ease of use. For example, Uber and Lyft
have disrupted the transportation system while improving it in
certain respects (e.g., market-driven availability and responsiveness). On the energy side, customers demand improvements in information access as well as energy choice, equity,

---


### Page 3

and reliability from their electric infrastructure. Electric grids
are now expected to accommodate these rising expectations.
Technological advancements have led to ubiquitous computation and communications. This enables local information
processing and decision-making and empowers customers to
manage their on-site energy resources (e.g., solar PV and
storage) and decide how and when to share their excess
energy. Technology improvements have also unlocked new
avenues for energy efﬁciency. For example, real-time access
and coordination of building heating and cooling systems reduces their energy use and improves occupant comfort. On the
other hand, the sensing and communication capabilities being
added to these devices (across the spectrum of generation and
consumption) creates a large attack surface for cyber intruders
and can jeopardize the operations of the grid.
The energy democratization exceptions (i.e., resisting the
dominant energy agenda while reclaiming and democratically
restructuring energy regimes [30]) have gained steam in recent
years due to access to a wider range of energy choices,
widespread adoption of distributed energy resources, increased
affordability of electric energy storage, and climate change
considerations [31]. These exceptions combined with innovative business models are encouraging local and peer-to-peer
energy transactions. This shift is changing the economics of
electricity generation and use.
The reliability and resilience of the aging power infrastructure is increasingly challenged by climate change, natural
disasters, and cyber threats. The electric grid is key for
operating other critical infrastructures. More speciﬁcally, any
power disruption is harmful to national security, economic
prosperity, and communications networks as well as the basic
standard of living. The number of extreme natural weather
events like wildﬁres, ﬂoods, storms, and heatwaves is on
the rise [8], [9]. These environmental strains highlight the
need for energy resiliency. For example, recent wildﬁres in
California have pushed the state’s largest utility, Paciﬁc Gas
and Electric, close to bankruptcy [32]. A resilient grid is
prepared to handle disruptions in the supply side caused
by natural hazards, deal with cyber-physical incidents, and
manage human interventions. Grid operators used to dispatch
designated generation resources to preserve reliability at the
time of needs. The ongoing grid transformation have enabled
grid operators to access a ﬂeet of small scale energy resources
on the supply and demand sides that if orchestrated effectively
can signiﬁcantly boost grid resilience. These systemic changes
amplify the need for multi-entity coordination. This relies on
local communication and computation capabilities. Effective
coordination preserves privacy and scale across multi-modal
data sources and heterogeneous devices.
III. SCALABLE COORDINATION OF UNDERUTILIZED
ENERGY FLEXIBILITY POCKETS
Energy ﬂexibility is the ability of energy producers or consumers to adjust their output power (generation by producers)
or their energy consumption level (demand of consumers, e.g.
shifting or reducing loads) [33]. Energy ﬂexibility comes in
many forms and presents itself in bulk power grids as well
as microgrids and urban electric systems [34]. One example
is homeowner willingness to adjust the temperature setpoint(s)
of a building’s cooling systems in response to a load reduction
request from the grid manager. Certain strained electrical
utilities send out these requests in peak energy use hours.
Unless the grid takes direct control of the load in question,
the energy ﬂexibility is dependent on end-user cooperation.
Another example of energy ﬂexibility is regulating power
output of a solar farm to help the grid operator stabilize the
bulk power grid during extreme weather events.
Utilizing energy ﬂexibility offered by small scale DERs is
more challenging than leveraging ﬂexibility of large consumers
or producers. This is because DERs are constantly growing in
number, in geographical spread, and in heterogeneity. If used
effectively, distributed pockets of energy ﬂexibility offered by
DERs can be a reliable resource for grid management given
their closer proximity to end-use facilities when compared to
the grid manager (central) node. Furthermore, the distributed
nature of DERs adds to the grid’s ﬂexibility for control across
the network [35], [36]. Scalable aggregation is the key in
unlocking the massive potential of DERs.
A. Challenges
Io T-connected DER controllers have a wide-range of communication and computation capabilities. This heterogeneity
poses a challenge for utilizing federated computations to
orchestrate DER functionalities. Put differently, data storage
limitations, communication overhead, and computational constraints can degrade the performance of the analytics performed on local devices [37]. Moreover, the heterogeneity and
multi-modality of the data collected by Io T-connected DERs
pose additional difﬁculties in performing computations across
these devices. Architectural design and computation process
on edge Io T devices are extensively studied in the literature
[38]–[40]. In what follows, we elaborate on key issues and
discuss how they apply to the multi-agent DER context.
Agent hardware limitations, including constrained data storage and restricted computational and communication capabilities, can negatively affect cross-agent collaboration in multiagent settings. These limitations slow down local computational process by increasing communication overhead and
hindering intra-agent coordination. Hence, hardware speciﬁcations must be taken into account when implementing federated
computations. For example, authors in [41] study hardware
requirements for implementing next word prediction for a
user typing. These hardware issues are even more visible in
the context of nascent Io T-connected DERs. The standards
and requirements for the DER hardware setups are not yet
well-deﬁned. Manufactures and vendors are pursuing different
communication protocols (e.g. Open ADR [42]) while experimenting with computational possibilities. A gap also persists
between access to device monitoring and measurement information in the same class of assets (e.g., solar PV inverters).
Quality and frequency of information exchange among
agents of a multi-agent network directly impact overall performance of the network. In multi-agent information processing

---


### Page 4

setups, agents with limited communication resources can hinder convergence across the network. In addition, the tradeoff between communication cost and frequency should be
accounted for in designing federated computations [43]. To
address this issue, researchers have proposed a wide-range of
solutions such as reducing the number of inter-agent information exchanges and reduce the size of exchanged message [44].
Accounting for communication limitations is more critical
in the DERs energy management context since maintaining
supply and demand balance is the key in preserving power
grid’s reliability. Wide-spread communication disruption can
unbalance equity of generation and consumption and lead to
power outages. Hence, developing robust federated computation methodologies for achieving energy management goals is
critically important.
The aforementioned issues (i.e., computation and communication constraints) leads to emergence of straggling agents.
Stragglers fail to share or compute updates in time. Selective engagement of resourceful agents (computationally and
communication-wise) could be a possible solution to address
this issue [40]. Asynchronous implementation of updates [45]
also alleviates this issue. Finally, depending on their location
Io T-connected DERs might be governed by different policies.
For example, some utilities allow DERs to provide a widerange services for the grid while others may restrict participation to a speciﬁc aggregation arrangements. This heterogeneity
of policies is an obstacle that limits coordination between DER
agents located in different utility territories.
B. Energy Management in DER networks
This section intends to present a generic form for optimizing
operation of a DER ﬂeet that can be solved in a centralized
fashion. The following equations formulate this problem as:
minimize
xk
X
k∈Ωagents
fk(xk)
(1a)
s.t.
gj(x) ≤0; (: µj)
j ∈Ωineq
(1b)
hj(x) = 0; (: λj)
j ∈Ωeq
(1c)
In this setup the objective function (fk(·)) can capture
a wide-range of goals including energy cost or emission
minimization that k agents (i.e., Io T-connected DERs) are
collectively aiming to achieve. Also, sets of all agents, inequality constraints, and equality constraint are represented by
Ωagents, Ωineq, and Ωeq , respectively. Moreover, xk denotes
the variables associated with agent k. Inequality and equality
constraints associated with each agent are denoted by gj(·)
and hj(·). Variables µj and λj are Lagrangian multipliers associated with inequality and equality constraints, respectively.
Numerous solution approaches exist that are based on ﬁnding a solution that satisﬁes the ﬁrst-order optimality conditions
of this problem. These conditions can be derived from the
Lagrangian function of original optimization problem (1).
Henceforth these conditions will be denoted by O.
C. Agent-Based Analytics
This section presents a novel federated computation framework which directly solves the ﬁrst order optimality conditions
of the underlying optimization problem (i.e., (1)). Thus, technically reduces the optimization problem to ﬁnding a solution
for a coupled system of equations with geometric constraints.
This system of equations can be solved in a fully distributed
manner through an iterative process. This is due to the fact
each equation only contains local variables (i.e., related an
agent or its neighboring agents)
This iterative process relies on the agents to conduct local
updates and information exchange. In the case that a problem formulation includes constraints of the physical power
network, physical-connections needs to be reﬂected in the
communication graph. Each agent i is only required to update
variables associated with itself (namely Vi) and share updates
with a limited number of other agents. Collectively, agents of
this multi-agent system solve the optimality conditions of the
underlying optimization problem. In order to solve the discussed set of equation, the federated computation framework
creates local copies of shared variables and assign each copy to
a corresponding agent [46]. The iterative process ensures that
all the local copies converge to the same value. The formula
for local updates of each agent is presented below, where the
consensus term enforces agreement between local copies of
agents. The ﬁnal term uses the updated copies to solve the
optimality conditions.
Vi(k + 1)
=
P[Vi(k) + ρC
i (k)
neighborhood consensus
z
}|
{
X
j∈Ωi
(Vi(k) −Vj(k))
(2)
+ρI
i (k)
Oi(Vi(k))
|
{z
}
optimality conditions
]F, j ∈Ωi
In (2), Vi is the collection of variables associate with
agent i including xi, µj, λj. Also, k denotes the iteration
number whereas Ωi represents the neighboring set of agent
i. Furthermore, Oi(·) represents the ﬁrst order optimality
constraints associated with agent i while ρC
i and ρI
i denote the
tuning parameter vectors. Finally, P is the projection operator
that projects Vi onto its determined feasible space, denoted by
F. The feasible space is deﬁned as the intersection of equality
and inequality constraints of (1).
Updating variables in (2) only involve algebraic functions.
The lightweight linear structure of these federated updates is
well-suited to work on resource-constrained DER controllers.
This update scheme can also be implemented in a fully
distributed peer-to-peer fashion or distributed with centralized
oversight (i.e., where a central agent receives information
update from all agents). The updates for variables of all agents
follows the following compact form:
V(k + 1) = e V(k) −Ae V(k) + C
e V(k + 1) = P [V(k + 1)]F
(3)
V contains stacked variables for all agents, where A and C
represent system parameters and tuning weights. Moreover, P
is the projection operator that enforces variables to stay in the
feasible space (i.e., F). Also, e V is the vector of the stacked
projected variables. Convergence analysis is presented in [12].

---


### Page 5

Fig. 1. (a) Synchronous update and (b) Asynchronous update
On a separate note, the federated computation framework
being presented accommodates both synchronous and asynchronous update architectures. The difference between the two
schemes is the frequency of information exchange between
agents. In the synchronous update structure, every agent exchanges information with all neighboring agents after each
iteration. Agents wait for each neighboring agens to send
them updated information before performing the next update
of their local variables. Under the asynchronous update regime,
some agents only exchange information after intervals of a few
iterations. In this setup, agents are grouped into clusters where
the exchange between agents within a cluster may take place
every iteration while communication with agents in another
cluster typically occurs every few iterations. These two update
schemes are shown in Fig. 1. Asynchronous architectures can
substantially reduce the communication overhead [45] as interand intra-cluster updates follow two different clocks.
IV. BENCHMARK AND IMPLEMENTATION
The majority of existing federated analytics methods proposed in the literature will face difﬁculties in real-world setups
since researchers do not have access to large scale testing
setups [21]. This motivates developing test-bed for evaluating
federated computation methods. In what follow, we discuss
two test setup for testing federated computations in the context
of future electric grids; Carnegie PLUG and Grid Fruit, LLC.
The Carnegie PLUG testbed at Carnegie Mellon University
(CMU) is a campuswide hardware-in-the-loop (HIL) setup.
Carnegie PLUG (short for ”prosumer-in-the-loop simulation
grid”) enables large-scale sensing, computation and actuation
over a network of heterogeneous Io T-connected energy producers and consumers (prosuming) assets [47]. This system
is build on a multi-agent architecture that facilitates plugand-play integration of virtual (simulated) and on-campus
DERs. Carnegie PLUG has three layers; agent integration,
communication and data acquisition. Most CMU buildings
are equipped with sensors to collect ﬁne-grained energy and
environmental data (e.g., electricity consumption and temperature of campus ofﬁces and labs). Carnegie PLUG utilizes this
data in real-time and enables connecting this data to related
agents in the simulation environment. In Carnegie PLUG setup
each building or room can be modeled as an agent. The
communication between agents will take place in the opensource, DOE-funded VOLTTRONTM platform [48].
Grid Fruit is a startup company that puts unused energy
and operational data to work for the grid and its commercial
buildings. Speciﬁcally, in collaboration with us Grid Fruit
has developed machine learning software to provide energy
efﬁciency and grid incentives to their commercial consumers.
Using machine learning with enhanced monitoring and dynamic control, Grid Fruit optimizes load operations across
each building to minimize wasted energy and emergency
maintenance procedures on key building loads. In their food
store projects speciﬁcally, Grid Fruit is enabling lower energy
bills, operational costs, and food waste while transforming
commercial refrigeration systems into thermal batteries for
the grid. This, in turn, allows food stores to access demand
response rebates from the grid and reduce the stores peak demand charges, which constitute the majority of their electricity
bills in many regions.
Grid Fruit is optimizing the schedule of time-shiftable
load events (e.g., defrost cycles in refrigeration systems) in
multiple load types for commercial buildings. The approach
described in section III can be tailored to allow Grid Fruit
to optimally balance DERs including rooftop PV and multiple
load types (e.g., HVAC, lighting, refrigeration). In Grid Fruit’s
recent project with utility customer Southern California Edison
(SCE), Grid Fruit is optimizing load scheduling in convenience
stores across the utility (around 5,345 stores) and across the
state of California (11,990 stores) [49]. Federated computation
aggregates load ﬂexibility and smooths the aggregate demand
of these convenience stores. The proposed project is generating and modeling load scheduling commands over year-long
simulations with SCE grid conditions (e.g., SCE time-of-use
pricing and demand charges). Furthermore, the federated computation approach enables optimization of stores aggregated
across all of California’s sixteen distinct climate zones. A
key metric of interest to SCE is reduction in max demand
as compared with the pre-intervention baseline. In initial tests,
Grid Fruit has demonstrated reduction in maximum demand of
up to 58.2% in evening peak hours for a single store (36.6%
reduction over the entire day). Grid Fruit intends to apply
the above-described federated learning approach to optimize
operation of the convenience store loads (real-world DERs)
across the entire SCE service territory and across the state
of California. Aggregating the ﬂexibility potential of food
stores across these areas will turn the untapped resource of
commercial building demand into a grid asset that enables
peak shaving on the order of 100 MW at peak-demand hours.
V. CONCLUSION
In this paper, we have highlighted the impact and role
of Io T-connected DERs in the future of the electric power
grid. The number of affordable energy resources (e.g., solar
PV) is on the rise. These systems come in a wide range
of sizes with different monitoring and control technologies
and capabilities. This inherent heterogeneity makes decisionmaking and coordination across these various systems challenging. Federated computation enables large-scale machine
learning and optimization across heterogeneous agents. This

---


### Page 6

approach is well suited to orchestrating operation of Io Tconnected DERs across many locations. We have detailed
the hurdles for achieving effective coordination across Io T
networks, such as complications of DER controllers. We presented a novel, lightweight, coordination method and discussed
implementation and benchmarking directions in both research
and commercial contexts.
REFERENCES
[1] F. C. Dos Santos, J. Thornburg, and T. S. Ustun, “Automated planning
of rooftop PV systems by aerial image processing,” in 2018 IEEE PES
Asia-Paciﬁc Power and Energy Engineering Conference, Oct. 2018.
[2] M. Babcock, R. E. Ciez, A. Loew, B. Sergi, J. Thornburg, and N. J.
Williams, “Institutional inﬂuence on power sector investments: A case
study of distributed and centralized energy in Kenya and Tanzania,”
Energy Research and Social Science, vol. 41, 4 2018.
[3] J. Thornburg and B. Krogh, “Simulating energy management strategies
for microgrids with smart meter demand management,” in 2017 IEEE
PES Power Africa Conference, Accra, Ghana, Jun. 2017.
[4] K. Kok, S. Widergren, G. Yang, and J. Hu, “Guest editorial introduction
to the special section on transactive approaches to integration of ﬂexible demand and distributed generation,” IEEE Transactions on Power
Systems, vol. 34, no. 5, pp. 3991–3993, 2019.
[5] W. Tushar, T. K. Saha, C. Yuen, D. Smith, and H. V. Poor, “Peer-topeer trading in electricity networks: an overview,” IEEE Transactions
on Smart Grid, 2020.
[6] A. Imteaj, M. H. Amini, and J. Mohammadi, “Leveraging decentralized
artiﬁcial intelligence to enhance resilience of energy networks,” ar Xiv
preprint ar Xiv:1911.07690, 2019.
[7] J. Thornburg, “A tool for probabilistic evaluation of microgrid operating
strategies with demand side management,” Ph.D. dissertation, Carnegie
Mellon University, Dec. 2018.
[8] Q. Schiermeier, “Increased ﬂood risk linked to global warming: likelihood of extreme rainfall may have been doubled by rising greenhousegas levels,” Nature, vol. 470, no. 7334, Feb. 2011.
[9] J. Robbins, “Climate whiplash: Wild swings in extreme weather are on
the rise,” Yale Environment 360, Nov. 2019.
[10] C. S. Holling, “Resilience and stability of ecological systems,” Annual
review of ecology and systematics, vol. 4, no. 1, pp. 1–23, 1973.
[11] J. Thornburg, G. Hug, T. Ustun, A. Rowe, and B. Krogh, “Incorporating
smart-grid operating strategies into off-grid electriﬁcation planning,” in
SIAM Conference on Control and Its Applications, Jul. 2015.
[12] J. Mohammadi, “Distributed computational methods for energy management in smart grids,” Ph.D. dissertation, Carnegie Mellon University,
2016.
[13] V. Cevher et al., “Convex optimization for big data: Scalable, randomized, and parallel algorithms for big data analytics,” IEEE Signal
Processing Magazine, vol. 31, no. 5, pp. 32–43, 2014.
[14] F. Yan, S. Sundaram, S. Vishwanathan, and Y. Qi, “Distributed autonomous online learning: Regrets and intrinsic privacy-preserving properties,” IEEE Transactions on Knowledge and Data Engineering, vol. 25,
no. 11, pp. 2483–2493, 2012.
[15] J. Chen and A. H. Sayed, “Diffusion adaptation strategies for distributed
optimization and learning over networks,” IEEE Transactions on Signal
Processing, vol. 60, no. 8, pp. 4289–4305, 2012.
[16] S. Boyd et al., Distributed optimization and statistical learning via the
alternating direction method of multipliers.
Now Publishers Inc, 2011.
[17] J. Mohammadi and S. Kolouri, “Collaborative learning through shared
collective knowledge and local expertise,” in 29th International
Workshop on Machine Learning for Signal Processing.
IEEE, 2019.
[Online]. Available: https://doi.org/10.1109/MLSP.2019.8918888
[18] M. Li, D. G. Andersen, A. J. Smola, and K. Yu, “Communication
efﬁcient distributed machine learning with the parameter server,” in
Advances in Neural Information Processing Systems, 2014, pp. 19–27.
[19] Z. Huang, R. Hu, Y. Guo, E. Chan-Tin et al., “Dp-admm: Admmbased distributed learning with differential privacy,” IEEE Transactions
on Information Forensics and Security, vol. 15, pp. 1002–1012, 2019.
[20] E. P. Xing, Q. Ho, W. Dai, J. K. Kim, J. Wei, S. Lee, X. Zheng, P. Xie
et al., “Petuum: A new platform for distributed machine learning on big
data,” IEEE Transactions on Big Data, vol. 1, no. 2, pp. 49–67, 2015.
[21] P. Kairouz, H. B. Mc Mahan, B. Avent et al., “Advances and open
problems in federated learning,” ar Xiv preprint ar Xiv:1912.04977, 2019.
[22] T. Li, A. K. Sahu, A. Talwalkar, and V. Smith, “Federated learning:
Challenges, methods, and future directions,” IEEE Signal Processing
Magazine, vol. 37, no. 3, pp. 50–60, 2020.
[23] F. Bonomi, R. Milito, J. Zhu, and S. Addepalli, “Fog computing and its
role in the internet of things,” in Proceedings of the ﬁrst edition of the
MCC workshop on Mobile cloud computing, 2012, pp. 13–16.
[24] A. Deshpande, C. Guestrin, S. R. Madden, J. M. Hellerstein, and
W. Hong, “Model-based approximate querying in sensor networks,” The
VLDB journal, vol. 14, no. 4, pp. 417–443, 2005.
[25] P. Garcia Lopez, A. Montresor, D. Epema, A. Datta, T. Higashino,
A. Iamnitchi, M. Barcellos, P. Felber, and E. Riviere, “Edge-centric
computing: Vision and challenges,” 2015.
[26] T. Li, M. Sanjabi, A. Beirami, and V. Smith, “Fair resource allocation
in federated learning,” ar Xiv preprint ar Xiv:1905.10497, 2019.
[27] Z. Bao, Y. Cao, G. Wang, and L. Ding, “Analysis of cascading failure
in electric grid based on power ﬂow entropy,” Physics Letters A, vol.
373, no. 34, pp. 3032–3040, 2009.
[28] A. J. Wood, B. F. Wollenberg, and G. B. Shebl´e, Power generation,
operation, and control.
John Wiley & Sons, 2013.
[29] S. Widergren and J. D. Taft, “Grid architecture: The decisions that
will shape our energy future [guest editorial],” IEEE Power and Energy
Magazine, vol. 17, no. 5, pp. 14–16, 2019.
[30] J. C. Stephens, M. J. Burke, B. Gibian, E. Jordi et al., “Operationalizing
energy democracy: Challenges and opportunities in vermont’s renewable
energy transformation,” Frontiers in Communication, vol. 3, p. 43, 2018.
[31] H. Keshan, J. Thornburg, and T. S. Ustun, “Comparison of lead-acid and
lithium ion batteries for stationary storage in off-grid energy systems,”
in IET Int’l Conference on Clean Energy and Technology, Nov. 2016.
[32] K. Blunt et al., “PG&E starts to cut power for nearly 800,000 California
customers on wildﬁre risk.” Wall Street Journal, Oct. 2019.
[33] R. G. Junker, A. G. Azar, R. A. Lopes, K. B. Lindberg, G. Reynders,
R. Relan, and H. Madsen, “Characterizing the energy ﬂexibility of
buildings and districts,” Applied Energy, vol. 225, pp. 175–182, 2018.
[34] J. Thornburg, B. Krogh, and T. S. Ustun, “Stochastic simulator for smart
microgrid planning,” in ACM DEV 2016, Nairobi, Kenya, Nov. 2016.
[35] J. Thornburg, T. S. Ustun, and B. Krogh, “Smart microgrid operation
simulator for management and electriﬁcation planning,” in 2016 IEEE
PES Power Africa Conference, Livingstone, Zambia, Jun. 2016.
[36] T. S. Ustun, J. Thornburg, and B. Krogh, “Smart pricing implementation/simulator with ICT infrastructure,” in Africa-EU Symposium on
Renewable Energy Research and Innovation, Mar. 2016.
[37] A. Imteaj, U. Thakker, S. Wang, J. Li, and M. H. Amini, “Federated
learning for resource-constrained iot devices: Panoramas and state-ofthe-art,” ar Xiv preprint ar Xiv:2002.10610, 2020.
[38] M. Chen, Z. Yang, W. Saad, C. Yin, H. V. Poor, and S. Cui, “A joint
learning and communications framework for federated learning over
wireless networks,” ar Xiv preprint ar Xiv:1909.07972, 2019.
[39] F. Chen, M. Luo et al., “Federated meta-learning with fast convergence
and efﬁcient communication,” ar Xiv preprint ar Xiv:1802.07876, 2018.
[40] A. Das and T. Brunschwiler, “Privacy is what we care about: Experimental investigation of federated learning on edge devices,” in Proceedings
of the First International Workshop on Challenges in AI and ML for
Internet of Things, 2019, pp. 39–42.
[41] A. Hard, K. Rao, R. Mathews, S. Ramaswamy et al., “Federated learning
for mobile keyboard prediction,” ar Xiv preprint ar Xiv:1811.03604, 2018.
[42] C. Mc Parland, “Open ADR open source toolkit: Developing open source
software for the Smart Grid,” in 2011 IEEE Power and Energy Society
General Meeting.
IEEE, 2011, pp. 1–7.
[43] C. Ma, J. Koneˇcn`y, M. Jaggi, V. Smith, M. I. Jordan, P. Richt´arik,
and M. Tak´aˇc, “Distributed optimization with arbitrary local solvers,”
Optimization Methods and Software, vol. 32, no. 4, pp. 813–848, 2017.
[44] J. Koneˇcn`y et al., “Federated learning: Strategies for improving communication efﬁciency,” ar Xiv preprint ar Xiv:1610.05492, 2016.
[45] J. Mohammadi, G. Hug, and S. Kar, “Asynchronous distributed approach
for dc optimal power ﬂow,” in 2015 IEEE Eindhoven Power Tech. IEEE,
2015, pp. 1–6.
[46] R. Olfati-Saber, J. A. Fax, and R. M. Murray, “Consensus and cooperation in networked multi-agent systems,” Proceedings of the IEEE,
vol. 95, no. 1, pp. 215–233, 2007.
[47] J. Kim, C. Goodman, and J. Mohammadi, “Carnegie PLUG: prosumerin-the-loop simulation grid,” ar Xiv preprint ar Xiv:2005.06597, 2020.
[48] “Volttron documentation,” Available at: https://volttron.org/, 2019.
[49] J. Lenard, “U.S. convenience store count,” The Association For Convenience and Fuel Retailing (NACS), 2020.

---
