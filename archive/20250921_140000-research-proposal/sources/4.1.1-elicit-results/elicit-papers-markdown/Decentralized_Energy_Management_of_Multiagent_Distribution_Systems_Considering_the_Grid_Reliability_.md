# Decentralized Energy Management of Multiagent Distribution Systems Considering the Grid Reliability and Agent Misbehavior

## Paper Metadata

- **Filename:** Decentralized Energy Management of Multiagent Distribution Systems Considering the Grid Reliability and Agent Misbehavior.pdf
- **DOI:** 10.1109/jsyst.2024.3369871
- **Authors:** Aghamohammadi, Farshid and Abbaspour, Ali and Saber, Hossein and Fattaheian-Dehkordi, Sajjad and Lehtonen, Matti
- **Year:** 2024
- **Journal/Venue:** IEEE Systems Journal
- **URL:** http://dx.doi.org/10.1109/JSYST.2024.3369871
- **Extraction Date:** 2025-06-03T15:01:22.383153
- **Total Pages:** 12

## Abstract



## Keywords



---

## Full Text Content



### Page 1

IEEE SYSTEMS JOURNAL
1
Decentralized Energy Management of Multiagent
Distribution Systems Considering the Grid
Reliability and Agent Misbehavior
Farshid Aghamohammadi
, Ali Abbaspour
, Hossein Saber
, Sajjad Fattaheian-Dehkordi
,
and Matti Lehtonen
Abstract—In recent years, the high expansion of independent
energy sources and development of multiagent structures have
resulted in new challenges in the efﬁcient power management of
distribution networks. In this regard, decentralized management
along considering operational concerns of the system will be a
key factor in running the future multiagent systems. Therefore,
this article proposes a decentralized framework based on the alternating direction method of multipliers for managing the peerto-peer (P2P) energy trading in a multiagent distribution system
while considering the technical constraints and reliability of the
network. This strategy facilitates considering the effects of the
network reliability while running the agents’ optimization in a
decentralized manner. Respectively, each agent would tend to exchange energy with more reliable agents, which would result in
the resilient operation of the network. Moreover, the uncertainty
of renewable energy sources is addressed using distributionally
robust optimization. Additionally, with the aim of increasing the
security of the P2P energy market against communication errors
and agents’ misbehavior, an algorithm is developed to identify the
existence of a problem in the market convergence as well as how it
could be mitigated. Finally, this scheme is investigated on 37 and
69 bus test systems to study its capability in running sustainable
energy systems.
Index Terms—Agent misbehavior, decentralized optimization,
distributionally
robust
optimization
(DRO),
energy
system
optimization, ﬂexible resources, multiagent, peer-to-peer (P2P)
trading, reliability, renewable energies, transactive energy (TE),
uncertainty.
A. Sets
Gm
Set of distributed generation (DG) of
agent m.
Bm
Set of battery energy storage (BES) of
agent m.
Km
Set of renewable generation of agent m.
M
Set of all agents.
Nline /Nnode
Set of lines/nodes in the distribution network.
Manuscript received 19 March 2023; revised 19 August 2023 and 19 January
2024; accepted 14 February 2024. (Corresponding author: Sajjad FattaheianDehkordi.)
Farshid Aghamohammadi, Ali Abbaspour, and Hossein Saber are with the
Department of Electrical Engineering, Sharif University of Technology, Tehran
14588-89694,Iran(e-mail:farshid.aq@gmail.com;abbaspour@sharif.edu;hossein.saber@ee.sharif.edu).
Sajjad Fattaheian-Dehkordi and Matti Lehtonen are with the Department of
Electrical Engineering and Automation, Aalto University, 02150 Espoo, Finland
(e-mail: sajjad.fattaheiandehkordi@aalto.ﬁ; matti.lehtonen@aalto.ﬁ).
Digital Object Identiﬁer 10.1109/JSYST.2024.3369871
Ai/Ci
Set of parent node/child nodes of node i
in the distribution network.
B. Parameters
α2,m, α1,m, α0,m
Cost parameters of DG m.
p DG
g
/p DG
g
Upper/lower bound of active power output of DG.
q DG
g
/q DG
g
Upper/lower bound of reactive power output of DG.
pch
b /pdch
b
Maximum charging/discharging rate of
BES.
So Cb /So Cb
Upper/lower bound of So C of BES.
ri/xi
Resistance/reactance of line i.
vi/vi
Upper/lower bound of squared voltage
magnitude of node i.
F i
Maximum capacity of line i.
ηch
b /ηdch
b
Charging/discharging efﬁciency of BES.
Eb
Energy capacity of BES.
λb
t/λs
t
Price of buying from / selling to the upperlevel grid.
Um
n
Normalized
unavailability
between
agents m and n.
υm
Weighting factor of agent m in reliability
cost.
Cm
sh,t
Load shedding price of agent m at time t.
p L
i,t/q L
i,t
Active/reactive load at node i.
ak
Smoothing factor.
C. Variables
p DG
g,t /q DG
g,t
Active/reactive power output of DG.
pch
b,t / pdch
b,t
Charging/discharging rate of BES.
So Cb,t
State of charge of BES.
P m
b,t/ P m
s,t
Active power bought/sold to the upperlevel grid.
pm
n,t
Active power transferred from agent m to
n.
pm
sh,t
Load shedding of agent m at time t.
p RG
k,t
Active power output of renewable generation.
Pi,t/Qi,t
Active/reactive power ﬂow in line i.
λm
n,t
P2P energy trading price between agents
m and n.
χm,t
Sign function for keeping reliability cost
positive.
vi,t
Squared nodal voltage magnitude at node
i.
© 2024 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see
https://creativecommons.org/licenses/by/4.0/
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination.

---


### Page 2

2
IEEE SYSTEMS JOURNAL
li,t
Squared line current magnitude of line i.
ˆpm
n,t
Auxiliary variable duplicating the value
of pm
n,t.
f m,k
n
MSD between agent m and n in the kth
iteration.
˜f m,k
n
Weighted moving average of the MSD.
π(k)
Stationary distribution in the kth iteration.
I. INTRODUCTION
R
ESTRUCTURING in energy systems, the increase in fossil fuel prices, and environmental concerns in recent years
have led to the widespread proliferation of renewable energy
sources in local systems. In this regard, the emergence of renewable energy sources in the distribution networks has changed
them into active distribution networks with potential reliability,
and ﬂexibility problems [1]. Therefore, optimal management of
renewable energy sources while considering economic issues
and maintaining the resiliency of the distribution network is of
great importance.
The concept of multiagent structures in local systems can be
used as an optimal method to manage renewable energy sources.
An agent could manage its local systems by receiving the required information and processing it [2]. Moreover, agents can
exchange information with other agents due to the development
of communication infrastructures to optimize their objectives.
As a result, the expansion of multiagent systems can lead to the
creationofanenergymarketwithdecentralizedoperation,which
has major advantages over the traditional centralized methods,
i.e., reducing the need for huge communication requirements
and heavy computational burdens, increasing the scalability, and
preserving autonomy and privacy of local systems [3].
In recent years, numerous studies have been done on the
development of operational management models for multiagent systems; hence, new decentralized schemes have been
presented. Respectively, one of the major concepts in this ﬁeld
is peer-to-peer (P2P) energy trading, which allows prosumers
and local systems to participate in local energy markets. A
distributed market framework is proposed in [4] which allows
the prosumers to trade based on the characteristics of the energy
such as location and generation technology. Still, this article has
not considered the uncertainties of the network operation. In
[5], a two-stage P2P energy sharing strategy is presented and a
distributed approach is used to implement it. In the ﬁrst stage,
buildings determine their optimal amount of energy exchange
with each other as well as the retailer; while in the second
stage, reciprocal prices are obtained using a noncooperative
game model. In [6], game-theoretic frameworks are proposed, in
which pricing between sellers is modeled with a noncooperative
game, and the dynamics of buyers to select sellers are modeled
as an evolutionary game. Purage et al. [7] proposed a scalable
robustoptimalschedulingmodelformultimicrogrid(multi-MG)
systems. Nevertheless, it is noteworthy that, in these works,
the operational and technical limitations of the network have
not been considered and merely the economic factors of the
P2P energy trading markets have been studied. Accordingly,
the obtained results may not address the operational constraints
of the network; therefore, technical issues such as power ﬂow
equations seem to be necessary to be considered in the developed
P2P energy markets.
A uniﬁed energy market framework for P2P energy trading
is proposed in [8] to enable the decentralized operation of
distribution systems considering network constraints. In [9],
the distribution network is divided into several energy-sharing
regions (ESRs) with different network fees; each of these ESRs
has an energy-sharing provider. While this scheme enables the
ﬂexible operation of the system, the developed Stackelberg game
model to manage the market does not enable the fully decentralized operation of the system. Li et al. [10] used Nash bargaining
to operate the transactive energy (TE) trading structure with
high penetration of solar energy resources. In [11] a distributed
energy management system is developed to operate community
MGs. In this work, a microgrid central controller is considered
to manage the related distributed energy resources and energy
storage systems along with home energy management system
in local houses. Wang et al. [12] presented an iterative bilevel
programming structure for the coordination of multi-MGs in the
TE market and the operation of the distribution network. At each
iteration, MGs take their decisions at the lower level and send
their equivalent loads to DSO. Then DSO modiﬁes the distribution system and calculates the TE path for the MGs. Although
the authors in [8], [9], [10], [11], and [12] have respected the operational limitations of the grid, they have not considered uncertainties as well as the reliability of the grid in their investigations.
By the increasing share of renewable energies, the uncertainties associated with their power generation must be taken
into account in the operation of the grid to increase the system reliability. For this purpose, various approaches including
stochastic programming (SP), robust optimization (RO), and
distributionally robust optimization (DRO) have been employed
in recent works to address the uncertainties of renewable energy
sources. In this regard, the authors in [13] have used SP to model
the uncertainty of power output of photovoltaic (PV) units as
well as uncertainties of energy prices, and load demand. In [14],
a method for scheduling of multi-MG systems by using the SP
is presented. In this approach, MGs schedule their resources
for the normal and resilient operation of the network when
they are disconnected from the main grid. Intera-day markets
are presented in [15] to enable prosumers to exchange energy
with their neighbors or the grid considering their generation
uncertainties via different scenarios. A bilevel risk-constrained
SP for managing a TE market has been used in [16]. The
uncertainties of the day-ahead market prices are handled in
the ﬁrst stage. In the second stage, a noncooperative game is
utilized to model a market for MGs to maximize their proﬁts.
Nonetheless, the authors in [15] and [16] have not considered
reliability. Fattaheian-Dehkordi et al. [17] proposed a distributed
transactive framework to efﬁciently manage multi-MG systems.
In this work, each agent optimizes its local resources by receiving TE signals and the SP is employed to model the uncertain
parameters. Still, the work in [17] did not study reliability and
agents’ probable misbehaviors.
In the RO method, unlike SP, there is no need for probability
density function (PDF) for uncertain parameters, leading to a
reduction in computational burden; hence, only an uncertainty
set of the uncertain parameter is required to apply the RO
model [18]. In [3], RO is used to handle the uncertainties of
local resources. Wei et al. [19] employed the RO with the aim
of modeling the uncertainty of wind power output as well as
minimizing the cost of each MG. Nevertheless, the RO approach
could result in too conservative outputs. This method considers
the worst-case scenario and therefore it may not be very costeffective.
Recently, the DRO approach has attracted remarkable attention in modeling the uncertainty in optimization models. However, the DRO approach stands out as it does not require the exact
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination.

---


### Page 3

AGHAMOHAMMADI et al.: DECENTRALIZED ENERGY MANAGEMENT OF MULTIAGENT DISTRIBUTION SYSTEMS
3
PDF for modeling uncertain parameters, which is a limitation of
SP. In addition, unlike RO, DRO takes advantage of historical
data for optimization modeling, making it more data-efﬁcient
andlessconservativeinitsdecision-makingprocess.Thisunique
combination allows DRO to inherit the beneﬁcial aspects of
both SP and RO while overcoming their limitations. As a result,
DRO provides a promising solution for handling uncertainty
in optimization problems. In [20], a co-optimization model for
energy trading is presented. In this work, the Wasserstein metric
(WM)-based DRO is employed to handle uncertainties. Duan
et al. [21] used Wasserstein-metric-based afﬁnely adjustable
distributionally robust to manage the uncertainty of wind power
and analyzed the effect of sample size on the results obtained
from DRO. Note that the authors in [3], [18], [19], [20], [21],
and [22] have not taken into account the grid reliability as well as
the data manipulation or common data failures that could lead to
convergence problems during the decentralized operation of the
system. In recent works, only authors in [23] have considered
the misbehavior of MGs in their distributed TE management
scheme for multi-MG systems. However, their approach lacked
consideration of uncertainties and network constraints, while
also being limited to a small sample size of only 4 MGs. As a
result, their model may not fully capture the complexities and
challenges that arise in real-world scenarios involving a larger
number of MGs and diverse network conditions.
Based on the above-mentioned discussions, the authors believe that the decentralized optimization of multiagent distribution systems based on the P2P concept while considering the
grid reliability as well as agents misbehavior and uncertainties of
renewable energy sources has not been investigated in previous
research works. Respectively, a new scheme based on the TE
concept is developed to enable the P2P transaction of system
agents, while considering the grid reliability. In other words,
the network reliability could act as an important criteria for
agents while participating in the P2P energy management. In this
regard, the developed scheme enables the agents to consider the
grid reliability while optimizing their energy transactions with
other entities. Moreover, most of the existing papers in this ﬁeld
have used SP and RO methods to handle the uncertainties in
P2P energy trading. In this work, the DRO approach is used
to overcome the deﬁciencies in the SP as well as RO methods
in modeling the uncertainties of power output by renewable
energy sources. Finally, the agents misbehavior could affect
the convergence of the P2P energy management; therefore, a
new algorithm is proposed to determine the agents misbehavior
and resolve the convergence issue in the system. The taxonomy
table of research works in the context of P2P energy trading is
presented in Table I.
In this study, we have proposed a P2P energy trading framework for interconnected agents considering the operating constraintsofthenetwork.Inaddition,the P2Pmarketpricingmechanism is developed in a decentralized manner. Furthermore, a
novel method is presented to model the reliability of the grid
as a cost term in the optimization objective of agents. Finally,
to increase the security of the P2P energy market, an algorithm
is presented to identify and mitigate communication errors and
convergence problems. The contributions of this article are as
follows.
1) A P2P energy trading framework is proposed for operating
multiagent distribution systems. As a result, this decentralized framework preserves the privacy and autonomy
of agents. Also, unlike previous works in this context,
this article strives to model the effect of the reliability
TABLE I
TAXONOMY OF RESEARCH WORKS ON P2P ENERGY TRADING
of the grid on the operation optimization of agents. This
method reduces the impacts of the contingency (i.e., fault)
in the network on the results of the TE market. As a result,
the resiliency-based energy management of the system is
conducted in a decentralized manner.
2) The optimization problem of agents is modeled using
data-driven DRO to handle the uncertainties of solar energy resources, in which the WM is used to construct the
uncertainty set. Finally, equivalent linear programming
reformulation of the DRO model is derived to reduce the
computational complexity.
3) In this article, an algorithm for increasing the security
of the P2P energy trading market is presented. In this
algorithm, at the ﬁrst step, any error in the communication
between agents is examined for the presence of noise,
misperception, or cyber-attacks. In the second step, if
the transmitted information is correct, the communicated
information in the market is examined for any potential
problem in the convergence of the P2P market. Unlike
other existing works, this algorithm strives to provide a
method for identifying the existence of a convergence
problem in the P2P market and then determining badbehaving agents. As a result, it can realize and diminish
the convergence problem in a distributed manner or by
considering a control entity.
In this article, the presented P2P market framework is discussed in Section II-A. Moreover, the problem formulation for
each agent is described in Section II-B. In Section II-C, the WM
is used for constructing an ambiguity set of uncertain parameter
and linear programming reformulation for the DRO model are illustrated. Decentralized P2P energy trading and pricing strategy
are explained in Section II-D. Different convergence problems
of the P2P market are proposed in Section II-E. Section II-F
presents an algorithm for identifying and mitigating the convergence problems of the P2P market. The results of implementing
the proposed framework and misbehavior detection algorithm
on the modiﬁed IEEE 37-bus test system and its usefulness are
demonstrated in Section III. Finally, the conclusion is presented
in Section IV.
II. METHODOLOGY
Based on the current trend, distribution networks will be
structured of multiagents/MGs, which would also facilitate the
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination.

---


### Page 4

4
IEEE SYSTEMS JOURNAL
Fig. 1.
System agent modeling.
integration growth of renewable energy sources. These selfstanding entities, which are connected by the distribution grid,
will have their independently operated local resources. A simple
model of an independently operated agent is presented in Fig. 1.
Respectively, system agents could independently optimize the
operation of their local resources. System agents will be able to
exchange energy with each other and the main grid; therefore,
a market framework would be required to facilitate the energy
exchange between the agents. This market could increase public
welfare and reduce network losses. For this purpose, in this
article, the concept of multiagent systems is used to create a P2P
energy trading structure to facilitate the distributed management
of the multiagent energy system. As mentioned, the modeled
agents aim to maximize their proﬁts in the market. Each agent
is in charge of optimizing its local resources by calculating its
operational variables and estimated price signals. This process
would be done by considering the operational constraints of
local resources and the uncertainty associated with the power
generation of renewable energy sources. In addition, the distribution network is subject to grid faults (e.g., line failure), and
these faults may severely affect the determined optimized power
exchanges in the energy market. Respectively, in this article, it
is assumed that agents could model the reliability of the grid as a
costtermandconsiderthistermintheirobjectivefunctionswhile
optimizing their local resources. As a result, energy trading with
other agents would be optimized considering the failure risk of
the connecting lines and the reliability of the grid. On the other
hand, due to the requirements for a lot of information exchange
in this structure, this market can be affected by communication errors, cyber-attacks, or misbehaving agents; which can
cause problems in running the proposed distributed algorithm.
Therefore, it is important to consider an approach to identify
information authenticity while running the market.
A. Distributed Transactive-Based Management Framework
for Multiagent Systems
In this study, a distributed framework based on the TE concept
is proposed to enable the operation of the distribution networks
with multiagent structures. In this article, system agents would
be responsible for optimizing their local resources and satisfying
technical constraints. These agents can be divided into two
subsets of sellers and buyers of energy, which could negotiate
directly with each other in the developed TE market. Note
that the alternating direction method of multipliers (ADMM)
is employed to run the operation of the distribution network,
while agents independently optimize their objective functions.
Therefore, in every iteration, information exchange would be
done among the agents and then every agent calculates global
variables and energy prices with the received information. It
should be noted that this framework is not dependent on a
central coordinator which is required in a central market model
for gathering, analyzing, and optimizing the operation of local
resources. Therefore, the market is managed in a completely
decentralized manner.
B. Agent Scheduling
As mentioned, each agent is responsible for minimizing the
operational costs of its resources according to received price
signals and uncertainties of power generation by renewable
energy sources. These costs would depend on the available local
resources and could include the cost of purchasing and selling
energy with the main grid or the P2P energy trading market, the
cost of storage units, as well as the cost of fuel-based distributed
generation (DG) units.
1) DG Cost: The fuel-based generation units, such as distributed diesel or microturbines, have a nonlinear cost function
that could be modeled with a quadrative cost function as follows:
Cm,DG
t

p DG
g,t

=

g∈Gm

α2,m.p DG
g,t
2+α1,m.p DG
g,t +α0,m

(1)
where the positive coefﬁcients of α2,m, α1,m, and α0,m are
relevant to DG characteristics. The output power boundary of
the DG unit is shown based on its minimum/maximum active
and reactive generation capacities as follows:
p DG
g
≤p DG
g,t ≤p DG
g
(2a)
q DG
g
≤q DG
g,t ≤q DG
g
.
(2b)
2) Battery Energy Storage (BES) Cost: Frequent charging
and discharging of BESs reduce their lifespan. For this reason, the degradation cost function (3) is considered as a linear
function using the charge and discharge rate and the lifetime
degradation coefﬁcient of the BES (i.e., θb) [32].
Cm,BES
t

pch
b,t, pdch
b,t

=

b∈Bm
θb.

ηch
b .pch
b,t + pdch
b,t /ηdch
b

.
(3)
Constraints imposed on the operation of BES are as follows:
0 ≤pch
b,t ≤pch
b
b ∈Bm , t ∈T
(4a)
0 ≤pdch
b,t ≤pdch
b
b ∈Bm , t ∈T
(4b)
So Cb ≤So Cb,t ≤So Cb
b ∈Bm , t ∈T
(4c)
So Cb,t = So Cb,t−1 + 1
Eb

ηch
b pch
b,t −
1
ηdch
b
.pdch
b,t

b ∈Bm, t ∈T
(4d)
So Cb,T = So Cb,0.
(4e)
Constraints (4a) and (4b) indicate the charging rate, and
discharging rate of the BES. The state of charge (So C) limit
is enforced in (4c) to protect batteries against overcharging and
undercharging. Moreover, the So C balance equation is shown
in (4d). Finally, (4e) imposes that the So C at the end of the day
should be equal to the So C at the beginning of the day.
3) Cost (Proﬁt) of Energy Trading: Each agent can exchange
energy with the main grid; therefore, the cost (proﬁt) of agent
m for buying and selling energy can be presented in (5). In (5),
P m
b,t (P m
s,t) shows the amount of purchasing (selling) energy by
agent m from (to) the main grid at time t. Moreover, λb
t (λs
t)
represents the price of purchasing (selling) energy from (to) the
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination.

---


### Page 5

AGHAMOHAMMADI et al.: DECENTRALIZED ENERGY MANAGEMENT OF MULTIAGENT DISTRIBUTION SYSTEMS
5
main grid. It should be noted that λb
t is always bigger than λs
t.
Cm,grid
t

P m
b,t, P m
s,t

=λb
t ·

1⊤P m
b,tΔt

−λs
t ·

1⊤P m
s,tΔt

.
(5)
Also, the cost (proﬁt) of agent m for the P2P energy trading at
time t is displayed in the following:
Cm,P 2P
t

pm
n,t

=

n∈M\m

λm
n,t
⊤pm
n,tΔt.
(6)
4) Proposed Reliability Cost: The distribution network is
exposed to various faults such as wire breaks due to storms, ﬁre,
falling trees on power lines, etc. [33], [34]. These faults and line
failures would prevent the P2P power transactions determined
in the energy market, which could result in load shedding and
ﬁnancial loss. As a result, these conditions will reduce the
reliability of the P2P market. Therefore, in this article, a novel
method for modeling reliability as a cost term has been proposed
to increase the reliability of the P2P market by reducing the
effect of the potential network faults on the P2P market. In this
method, each agent considers a penalty coefﬁcient for each of
market participants while optimizing its P2P power transactions.
Agents calculate these coefﬁcients based on the unavailability
time of other peers during a year. The calculated coefﬁcients
should be considered in the objective function of the agents in
order to affect their traded energy with other participants in the
P2P market.
For this purpose, it is possible to calculate the unavailability of
different lines based on the mean failure rates and repair times.
In other words, according to the network topology, the unavailability time of different agents per year could be estimated. For
normalization, these numbers will be divided by 8760 h and the
cost of reliability will be entered into the modeling of each agent
as represented in the following:
Cm,Re
t
(pm
n ) =

n∈M\m
υm.γm
n .χm,t.Um
n .pm
n,t
(7a)
0 ≤υm ≤10.
(7b)
As a result, with the addition of the reliability cost term in
the objective function of each agent, more energy exchange will
be done among agents with higher reliable connections because
their unavailability time is lower than the others and this will lead
to smaller reliability costs, respectively. In (7a), Um
n stands for
the calculated normalized unavailability. Moreover, υmis used
for weighting in order to determine desirable reliability for each
agent. In addition, the value of pm
n,t will be negative when agent
m is an energy seller. Therefore, χm,tis a coefﬁcient to ensure
that the value of the reliability cost will always be positive. It
means that, when the value of pm
n,t is positive and the agent m is
a buyer of energy, the value of χm,t is +1 and when the agent
is a seller, its value is −1.
5) Load Shedding Cost: The cost of load shedding should be
taken into account in the operational optimization of agents. The
load shedding may be the result of line loading in the distribution
grid [17], [28]. In this regard, the cost of load shedding is
modeled in (8), where the load shedding price is presented by
Cm
sh,t.
Cm,sh
t

pm
sh,t

= Cm
sh,t. pm
sh,t
(8a)
pm
sh,t ≥0
∀t ∈T , ∀m ∈M.
(8b)
6) Uncertainties Costs: Each agent can have solar power
generation units. Respectively, due to the unpredictable nature
of renewable energy sources, their uncertainties should be considered in the agent’s optimization model. In this regard, an
ambiguity set can be created using the forecasted generation
data, which is represented by ˜ζ in this article. Also, the cost
associated with the uncertainties of agent m at time t can be
represented by the Φm
t (xm
t , ˜ζm
t ). The predicted data, ˜ζ, have
a probability distribution (PD) of P. Moreover, ˆPN represents
the ambiguity set including all the possible PD of the forecasted
variable, and xm
t
represents the decision variables of agent m at
time t. Therefore, the total cost of each agent can be split into two
parts. The ﬁrst part which is not dependent on the uncertainty
of the power generation by renewable energy sources includes
the cost of buying and selling energy, the cost of distributed
production, battery degradation cost, load shedding cost, and
reliability cost. The second part is related to decisions affected
by uncertainties. Hence, the objective function should minimize
operating costs and the expectation of the function Φm
t (xm
t , ˜ζm
t )
under the worst-case distribution called Pworst in the ambiguity
set ˆPN. Thus, the objective for the uncertainties can be shown
as follows:
min sup
P∈ˆPN
EP
	
Φ

x, ˜ζt

.
(9)
7) System Model: The operational modeling of the grid is
presented in (10) considering the linearized Dist Flow model
[17].
j∈Ci
[Pj,t + rjlj,t] −Pi,t −

g∈Gm
p DG
g,t −

k∈Km
p RG
k,t
−

n∈M\m
pn
m,t +

b∈Bm

pch
b,t −pdch
b,t

+ p L
i,t −pm
sh,t = 0
i ∈Nline ,
t ∈T ∀m ∈M
(10a)

j∈Ci
[Qj,t + xjlj,t] −Qi,t −

g∈Gm
q DG
g,t + q L
i,t = 0
i ∈Nline ,
t ∈T ∀m ∈M
(10b)
P i,t
2 + Qi,t
2 ≤vi,tli,t i ∈Nline ,
t ∈T ∀m ∈M
(10c)
v Ai,t = vi,t + 2 (ri Pi,t + xi Qi,t) + li,t

r2
i + x2
i

i ∈Nline ,
t ∈T ∀m ∈M
(10d)
vi ≤vi,t ≤vi
i ∈Nnode ,
t ∈T ∀m ∈M
(10e)
P i,t
2 + Qi,t
2 ≤F
2
i
i ∈Nnode ,
t ∈T ∀m ∈M.
(10f)
Constraints (10a) and (10b) demonstrate the active and reactive power balance at each bus of the grid. Equations (10c) and
(10d) are employed to calculate the voltage and current [35]. It
is noteworthy that the child and parent nodes are denoted by Ci
and Ai in this article. Furthermore, (10e) and (10f) demonstrate
voltage and line capacity limits.
C. DRO Model
1) WM-Based Ambiguity Set: The creation of the ambiguity
set has an excellent outcome in evaluating the expectation of
the random variable ˜ζ. Therefore, the true PD of the random
variable is required. However, in practical applications, the true
PD is always ambiguous and only a limited number of historical
data ˆζ := {ˆζ1, ˆζ2, . . . , ˆζN} is available. Hence, the exact PD of
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination.

---


### Page 6

6
IEEE SYSTEMS JOURNAL
the random variable cannot be obtained and only the empirical
distribution ˆPN = 1/N
N
k=1 δˆζkcan be calculated, where δˆζk
denotes the Dirac measure of the random variable ζk.
In this article, we have used the WM to create the ambiguity
set, because it has an out-of-sample performance guarantee. This
asymptotic guarantee indicates that as N tends to inﬁnity, the
ambiguity set converges to the true distribution, and a tractable
reformulation [36].
The WM which is a method for measuring the distance between two PDs can be formulated as (11) in our problem. Where
Ξ is compact supporting space and the two PDs ˆPN, P ∈ℜ(Ξ),
and ℜ(Ξ) denote the collection of all PDs with compact support
Ξ. In this regard, the empirical distribution ˆPN is used as an
estimate of the true PD in (11) to construct the ambiguity set.
W

ˆPN, P

= inf
Π

Ξ2
ˆζN −˜ζ
 Π

dˆζN, d˜ζ

.
(11)
In (11), Π is a joint distribution of ˜ζ and ˆζN with marginals
ˆPN and P. Therefore, the ambiguity set can be created as (12),
which shows a Wasserstein ball with a center of ˆPN and a radius
of ε(N).
ˆP :=

P ∈ℜ

Ξ

|W
ˆPN, P

≤ε(N)

.
(12)
Note that ε(N) has a great effect on the performance of the
WM-based method. ε(N) is a function of the conﬁdence level
β and the sample number N. In addition, ε(N) must converge
to zero as N goes to inﬁnite and can be shown as follows [37]:
ε (N) = D

1
N ln

1
1 −β

.
(13)
In (13), D is the diameter of the support of the random variable. From [38], D can be computed by solving the optimization
problem displayed in the following:
D ≃min

1
λ + ln
 1
N
N
k=1 eλ∥ˆζN−ˆμ∥
2
s.t. λ > 0
(14)
where ˆμ is the mean of the sample.
2) Problem Reformulation: For solving the DRO, we require to evaluate the worst-case expected costs in (9), which
is a multiple-dimensional optimization problem over PDs. This
problem seems to be intractable. On the other hand, the cost
function Φm
t is deﬁned in such a way that any shortage or excess
in the power production by solar units that cause load shedding
or nontraded power is penalized. Accordingly, the general form
of Φm
t would be as follows:
Φ

x, ˜ζ

= γ2˜ζ2 −γ1˜ζ + γ0.
(15)
Since γ2 > 0; thus, Φ(x, ˜ζt) is a convex quadratic function.
Considering the sample set {ˆζ1, ˆζ2, . . . , ˆζN} of the random
variable ˜ζ by the boundary [ζ, ¯ζ], the worst-case costs in (9)
could be evaluated according to Lemma 1 in [38] as follows:
sup
P∈ˆP
EP
	
Φ

x, ˜ζt

(16a)
=
⎧
⎪
⎨
⎪
⎩
inf
λ≥0
λ · ε (N) + 1
N
N
k=1 sk
s.t. sup
ζ≤ζ≤¯ζ

Φ (x, ζ) −λ
ζ −ˆζk


≤sk, ∀k ≤N
(16b)
⎧
⎪
⎪
⎪
⎪
⎪
⎪
⎨
⎪
⎪
⎪
⎪
⎪
⎪
⎩
inf
λ≥0
λ · ε (N) + 1
N
N
k=1 sk
s.t.Φ

x, ζ

−λ

ζ −ˆζk

≤sk, ∀k ≤N
Φ

x, ¯ζ

−λ

¯ζ −ˆζk

≤sk, ∀k ≤N
Φ

x, ˆζk

≤sk, ∀k ≤N
(16c)
where sk is an auxiliary variable. However, with the increase of
the historical sample set, the number of the quadratic constraints
and auxiliary variables in (16c) will increase. This would result
in a heavy computational burden. To overcome this drawback,
the value of λ is taken as follows:
λ = max

Φ′ 
x, ¯ζ

, −Φ′ 
x, ζ

(17)
where Φ′(x, ˜ζ) is the derivative of Φ(x, ˜ζ) with respect to ˜ζ.
Therefore, we would have
inf
λ≥0
λ · ε (N) + 1
N
N

k=1
sk
≤
⎧
⎪
⎪
⎨
⎪
⎪
⎩
inf
λ≥0
λ · ε (N) + 1
N
N
k=1 Φ

x, ˆζk

s.t.
 Φ′ 
x, ¯ζ

≤λ
−Φ′ 
x, ζ

≤λ
.
(18)
Note that the number of constraints and decision variables in
(18) remains similar while using larger sample sets, however,
in this case, the computational burden signiﬁcantly alleviates. It
is noteworthy that the results of (16c) and (18) have very small
differences which could be ignored [38].
D. Decentralized P2P Energy Trading Approach Among
Multiagents
Distributed methods are suitable for maintaining the privacy
and autonomy of agents. Consequently, in this study, the ADMM
algorithm is utilized to develop a P2P energy trading scheme
in a distributed fashion. The purpose of this optimization is to
minimize the operating costs of individual agents. Therefore,
the overall objective function is represented in (19a). Note
that the P2P energy trading payments are excluded from the
presented formulation due to (19c) and (19d). Note that (19c)
is the reciprocity coupled constraint, that prohibits the energy
trading between two seller or buyer agents.
min
x

m∈M

t∈T

Cm
t (xm
t ) + sup
Pt∈ˆPt
EPt

Φm
t

xm
t , ˜ζm
t

(19a)
s.t. (2), (4), (7b)–(7c), (8b), (10) ∀t ∈T , m ∈M
(19b)
pn
m,t + pm
n,t = 0
∀t ∈T , m/n ∈M, m ̸= n
(19c)
λn
m,t = λm
n,t
∀t ∈T , m/n ∈M, m ̸= n
(19d)
where
Cm
t (xm
t )=Cm,DG
t
+Cm,BES
t
+Cm,grid
t
+Cm,Re
t
+
Cm,sh
t
.
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination.

---


### Page 7

AGHAMOHAMMADI et al.: DECENTRALIZED ENERGY MANAGEMENT OF MULTIAGENT DISTRIBUTION SYSTEMS
7
To apply the ADMM algorithm and therefore the pricing algorithm of the energy trading among agents, (19) is reformulated.
In this regard, (19c) is reformulated considering an auxiliary
variable (i.e.,ˆpm
n,t). The augmented Lagrangian function associated with the P2P energy trading is shown in (20c), where zm
t
denotes the set of auxiliary variables, i.e., zm
t := {ˆpm
n,t} n ∈
M\m. Note that λm
n,t is the Lagrangian multiplier related to
(20b).
ˆpm
n,t + ˆpn
m,t = 0
∀t ∈T , m/n ∈M, m ̸= n
(20a)
pm
n,t = ˆpn
m,t
∀t ∈T , m/n ∈M, m ̸= n
(20b)
Lm
t (xm
t , zm
t , λm
t ) = Cm
t (xm
t )
+ sup
Pt∈ˆPt
EPt

Φm
t

xm
t , ˜ζm
t

+

n∈M\m

λm
n,t
⊤(pm
n,t
−ˆpm
n,t) + ρ
2
pm
n,t −ˆpm
n,t
2
2

(20c)
and λm
t := {λm
n,t} n ∈M\m.
1) xm
t - Update: Due to the decomposability of the augmented Lagrangian and the constraints (19b), xm
t can be updated
in a decentralized way. Therefore, each agent m computes the
problem (21) iteratively for updating the local variable xm
t with
considering the auxiliary variables zm,τ
t
and the Lagrangian
multiplier λm,τ
t
as constants. Note that τ shows the iteration
index.
xm,τ+1
t
:= arg min
xm
t ∈X m
t

t∈T
Lm
t (xm
t , zm,τ
t
, λm,τ
t
).
(21)
After computing (21) in every iteration, each agent m sends
pm,τ+1
n,t
to the agent n.
2) zm
t - Update: The auxiliary variable zm
t is updated locally
with solving (22) by agent m.
min
z
Lm
t (xm
t , zm,τ
t
, λm,τ
t
) .
(22)
Problem (22) can be simpliﬁed as follows by considering the
facts that every ˆpm
n,t is just coupled with ˆpn
m,t and the objective
function is also decomposable.
min
ˆpm
n,t
−

λm
n,t
⊤ˆpm
n,t −

λn
m,t
⊤ˆpn
m,t + ρ
2
ˆpm
n,t−pm
n,t
2
2
+ ρ
2
ˆpn
m,t −pn
m,t
2
2 .
(23)
3) λm
t – Update:
λm,τ+1
n,t
= λm,τ
n,t + ρ

pm,τ+1
n,t
−ˆpm,τ+1
n,t

.
(24)
Each agent locally updates Lagrangian multipliers and sends
λm,τ+1
n,t
to agent n.
Regarding the presented decentralized algorithm, x and z are
interpreted as local and global variables, respectively. Additionally, the stopping criteria could be deﬁned as follows:
rτ :=
ˆpm,τ
n,t −pm,τ
n,t

(25a)
sτ := ρ

ˆpm,τ
n,t −ˆpm,τ−1
n,t

 .
(25b)
The distributed algorithm for optimizing the P2P market is
illustrated in Fig. 2.
Note that, the convergence of the multiblock ADMM algorithm shown in (19) cannot be guaranteed in general. However,
by introducing an auxiliary variable (ˆpm
n,t), this optimization
problem can be transformed into a corresponding two-block
ADMM model (20c). This structure consists of the blocks
related to the energy management terms and auxiliary variables,
respectively.
Fig. 2.
Distributed algorithm for optimizing the P2P energy trading and agents
schedules.
In conclusion, the research conducted in [39] reinforces the
notion that the dual-block ADMM algorithm exhibits global
convergence when employed to tackle convex optimization
problems.
E. P2P Market Convergence Problems
Despite the major advantages of decentralized methods over
centralized ones; due to the lack of a central observer, decentralized management is prone to malicious attacks and misbehaving.
In other words, a malicious agent can easily manipulate information to prevent the ADMM algorithm from convergence or an
attacker can cause communication errors or disruption with the
scheduling model of agents. Hence, identifying the misleading
agent and problems that prevent the P2P trading algorithm to
converge to the optimal solution is another aspect of increasing
the reliability of the P2P energy market. This section should
be done in parallel with the ADMM algorithm and must be
implemented on the output data of the ADMM algorithm to
ensure the correctness of the data in each iteration. The proposed
algorithm can be implemented in a distributed manner or by a
control entity.
The P2P energy market is faced with different convergence
problems. One of the possible problems is the noise in the
data received by each agent, which can be a communication
error or due to an attack on the P2P market. In this case, the
data can be modeled as ˆA(k) = A(k) + δ(k) where A(k) is
actual communicated information, ˆA(k) is the decision vector
calculated by the ADMM, and δ(k) is a random vector that can
be different in each iteration.
Another problem is the existence of a fraudulent agent.
This misbehaving agent manipulates its output information in
a way that maximizes its proﬁts and reduces the proﬁts of other
market participants while following the ADMM algorithm. An
attacker can also hack an agent’s software and cause problems
in the market convergence. Therefore, providing a process to
identify and resolve these threats to the market seems to be
necessary.
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination.

---


### Page 8

8
IEEE SYSTEMS JOURNAL
F. Identify and Mitigate Convergence Problems
ADMM properties have been taken into account to develop
an algorithm to identify the convergence problems in the P2P
marketduetoagents’misbehavior.Inthisregard,Boydetal.[39]
show that in case Cm
t would have a closed, proper, and convex
form; therefore, the augmented Lagrangian (20c) has a saddle
point. Thus, we have
pm,k
n,t −ˆpm,k
n,t

2
→0
as k →∞.
(26)
Therefore, if the mentioned conditions for Cm
t
are met, the
amount of disagreement ∥pm,k
n,t −ˆpm,k
n,t ∥2
2 might not decline
monotonically. However, for large k, when there is no convergence problem, we would have
pm,k+1
n,t
−ˆpm,k+1
n,t

2
2 <
pm,k
n,t −ˆpm,k
n,t

2
2 .
(27)
This condition is true for all variables [40]. Using the convergence property shown in (27), we could calculate the mean
squared disagreement (MSD) between the agents m and n in
the kth iteration as follows:
f m,k
n
=
T
t=1
pm,k
n,t + pn,k
m,t

2
2
T
.
(28)
In (28), for large k, in case the value of f m,k
n
decreases uniformly; there will be no problem in the convergence. However,
the convergence problem will occur if for a large k, we have
sup
	
f m,k′
n
: k′ > k

> sup
	
f m,k′
n
: k′ > k + t

.
(29)
Our proposed algorithm for detecting convergence problem
in the P2P market has two stages. In the ﬁrst stage, each agent
considers a square matrix D for MSD. Therefore, agent m calculates the MSD values according to the received and calculated
data in the mth row of matrix D. Moreover, the agent m sends
calculated values to other agents, so that all agents have access
to the data. It should be noted that this does not mean the privacy
of agents is not protected because the D matrix does not contain
any information about the amount of energy exchanged between
the agents. Furthermore, in this matrix, we should have f m,k
n
=
f n,k
m ; therefore, any inconsistencies indicate a mistake in the
exchanged data. Based on the above-mentioned discussions, the
communication error will be detected and should be addressed
in the P2P market. Therefore, if the agent m detects such an
error for each of its customers or vendors (i.e., the calculated
value does not correspond to the received value), it can log a
communication error. In addition, since these kinds of structures
are vulnerable to communication failures such as data loss and
it would affect the algorithm of this stage, a special moving
list must be considered to record the misbehaving agents’ ID;
consequently, if these failures continue more than a predeﬁned
limit, the energy exchange between the problematic agents will
be cut off.
Then, in the second stage of the proposed process, the
weighted moving average of the MSD is deﬁned as follows:
˜f m,k
n
= ak f m,k
n
+

1 −ak ˜f m,k−1
n
(30)
where ak ∈(0, 1) is the smoothing factor that meets ∞
k=0 ak =
∞. As a result, each agent can calculate the conﬁdence level of
other participants as follows:
Bm (k) =
˜f m,k
n
36
n=0 ˜f m,k
n
∀n ∈M.
(31)
Algorithm 1: Identiﬁcation and Mitigation of Misbehaving
Agents.
1.
If τ = 1:
2.
Initialize two lists for suspicious agents;
3. Each agent calculates its MSDs values;
4. Agents exchange MSDs with each other and the central
entity;
5. If Agents verify :
6.
Central entity constructs state transition matrix;
7.
Central entity computes in a distributional manner;
8.
Central entity computes the standard deviation (i.e.,)
correspond to;
9.
If :
10.
Central entity ﬁnds the misbehaving agents;
11.
Central entity updates the list of suspicious agents;
12. Else:
13.
The central entity receives misbehaving agents’ ID;
14.
The central entity updates the list of agents with
communication failures;
15. Central entity makes decisions;
Based on the above-mentioned discussions, each agent can
calculate the square matrix B using the calculated and received
information. As it turns out, B is a row stochastic matrix and irreducible [41]; therefore, B has an eigenvalue 1 corresponding to
a stationary distribution π(k) that can satisfy π(k)B(k) = π(k).
Asaresult,B canbeperceivedasastatetransitioncorresponding
to a Marco chain in which each agent tends to interact more
frequently with the suspicious agents, and vice versa. Every
agent can compute stationary distribution π(k) in a distributed
manner. Therefore, rmis(k) = arg max π(k) can be identiﬁed
as the most suspicious agent in every iteration.
To prevent convergence problems in the P2P market, a supervisor entity can be introduced, which calculates the π(k)
matrix in each iteration by receiving the information from all
agents. Despite other works such as [23] that their algorithms
are always suspect to an agent in each iteration; in this article, a
novel index based on the standard deviation (STD) of the calculated stationary matrix is considered to detect the existence of
convergence error in the main algorithm. Therefore, the central
entity calculates the STD of the π(k) in each iteration, then
when the value of the STD rises higher than a certain threshold,
the entity becomes suspicious and tries to ﬁnd misbehaving
agents. Accordingly, the agents whose corresponding value in
π(k) is higher than the average value between the maximum
and minimum data of will be identiﬁed as misbehaving agents.
If these agents are detected continuously at a certain number of
iterations, the central entity sends alarm signals to these agents
and stops them from exchanging energy with each other. It
should be noted that this method can also be implemented entity
in a distributed manner by eliminating the market supervisor.
III. RESULTS
To evaluate the effectiveness of the proposed P2P trading
framework, two case studies were carried out. The ﬁrst test
system is considered to be a 37-bus multiagent distribution test
system shown in Fig. 3, while another one is a 69-bus system
demonstrated in Fig. 4 [42]. Purposely, each network bus is
considered as an agent that has a combination of local resources,
i.e., PV units, load demands, BESs, and microturbine units.
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination.

---


### Page 9

AGHAMOHAMMADI et al.: DECENTRALIZED ENERGY MANAGEMENT OF MULTIAGENT DISTRIBUTION SYSTEMS
9
Fig. 3.
Modiﬁed IEEE-37 bus distribution network.
Fig. 4.
Modiﬁed IEEE-69 bus distribution network.
Fig. 5.
Total energy sold by agent 8 to other agents in the P2P market at 10th
hour with/without considering the grid reliability.
Fig. 6.
Total energy purchased by agent 20 from other agents in the P2P market
at 10th hour with/without considering the grid reliability cost.
The proposed P2P trading framework is applied to schedule the
energy exchange among the agents and the main grid for 24 h
while taking into account the operating constraints of the grid.
Moreover, a sample set considered with 40 samples is used to
construct an ambiguity set of DRO with 95% conﬁdence level.
The ﬁrst part discusses the results obtained from the P2P
energy market within the IEEE 37 and 69-bus test systems,
while the second part addresses the developed algorithm for
identifying convergence problems in the market in case of agent
misbehavior for a test system.
A. P2P Energy Market Analysis in Multiagent Systems
1) Case Study I. IEEE 37-Bus System: In this part, the results
related to the P2P market on the IEEE 37-bus system are given.
Furthermore, one of the main purposes of this article is to model
the reliability in terms of cost. Consequently, Figs. 5 and 6 show
Fig. 7.
Total energy purchased by agent 20 from other agents in the P2P
market at 10th hour when the failure rate of line 16 (between agents 2 and 16)
is increased with considering the grid reliability cost.
Fig. 8.
Charging/discharging amounts of agent 20’s BES in 24 h.
Fig. 9.
Power generation by PV and microturbine units in agent 8 in 24 h.
the amount of energy exchange between agents with and without
modeling the cost of the grid reliability while considering the
technical limitations of the grid. In this regard, Fig. 5 shows
the amount of energy exchange of agent 8 with other agents at
the 10th hour. Moreover, Fig. 6 shows the amount of energy
purchased by agent 20 from other agents at 10th hour. Here, the
negative values in the presented results indicate that the energy is
sold to other entities. To emphasize the impact of reliability cost,
an alternative scenario is explored in Fig. 7, where the failure
rate of line-connected agents 2 and 16 is deliberately heightened.
This scenario vividly demonstrates the inﬂuence of reliability
cost on energy transactions. It is evident from Fig. 7 that, in
response to increased failure rates, agent 20 opts to exclusively
obtain energy from agents 17 and 19, who beneﬁt from more
robust and reliable connections. It can be seen that agents, which
have a set of reliable lines connected them together, tend to
exchange more energy with each other. Fig. 8 depicts the amount
of BES power charging/discharging in agent 20 at every hour of
the day.
Fig. 9 demonstrates the amount of power generation by different types of DG units operated by agent 8 during the operational horizon. Fig. 10 illustrates the total energy that the main
grid exchanged with the system agents during the operational
horizon. On the other hand, the total energy produced by all
agents in 24 h is shown in Fig. 11. The P2P price between
agents 8 and 20 at the 10th hour is shown in Fig. 12. The
resultsshowtheconvergenceof P2Ppriceduringoperationofthe
developed trading market. Note that the P2P price is converged
to 17.84 $/k W which is between the selling/purchasing price
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination.

---


### Page 10

10
IEEE SYSTEMS JOURNAL
Fig. 10.
Total energy the main grid traded with agents in 24 h.
Fig. 11.
Total power generation by PV and DG units of all the agents in 24 h.
Fig. 12.
P2P market price convergence between agents 8 and 20 at 10th hour.
Fig. 13.
Total energy bought by agent 27 from other agents in the P2P market
at 10th hour with/without considering the grid reliability cost.
announced by the upper-level network to agents (i.e., 29/62
$/k W and 17/77 $/k W). As expected for a time period like hour
10 when the agents’ energy production is higher than the entire
demand needed by them, the total energy required by the agents
is provided within the P2P market and the surplus energy is sold
to the main network. Therefore, it is anticipated that the P2P
market price will be near the purchase price of the main grid.
2) Case Study II. IEEE 69-Bus System: To validate the effectiveness of the proposed method, the IEEE 69-bus system
is employed for the second case study, characterized by an
increased number of buses and a more sophisticated topology.
This selection aims to enhance the comprehensiveness of the
evaluation.
In Fig. 13, the presented data at the 10th hour illustrates the
quantity of power transactions speciﬁcally carried out by agent
27 within the P2P trading market. The comparison contrasts
Fig. 14.
Total solar genration and its effect on P2P market price.
Fig. 15.
P2P market price convergence between agents 2 and 17 at 13th hour.
scenarios with and without the inclusion of reliability costs,
shedding light on the amount of power acquired by agent 27
from other agents under these different conditions. Notably,
the ﬁgures reveal a discernible trend wherein agents exhibit a
preference for procuring energy from counterparts with lower
associated reliability costs, as observed in Figs. 5 and 6.
Moving to Fig. 14, the visualization captures the impact of
total solar generation on the P2P market price. Notably, when
solar generation reaches its zenith, there is a corresponding
decrease in the P2P market price. This phenomenon contributes
to optimizing the total welfare of the market, as evidenced by
the market experiencing its highest levels of overall well-being
during periods of peak solar generation. Fig. 15 displays the P2P
price dynamics between agents 2 and 17 at the 13th hour. The
outcomes reveal a notable convergence in P2P prices, illustrating
the stabilization and efﬁciency achieved within the developed
trading market during its operational phase.
B. Results of Implementing the Convergence Problem
Detection Algorithm for Agent Misbehavior
In this part, the behavior of the stationary matrix π(k) and the
standard deviation diagram related to it, in P2P markets on the
37-bus test system with/without a convergence problem will be
investigated. Furthermore, the introduced convergence problem
detection algorithm has been implemented in the developed P2P
market to mitigate the problem.
In the ﬁrst case, the P2P market is operated without any
convergence problem. In this case, the results related to the
matrix π(k) and the standard deviation associated with each
iteration are shown in Fig. 16. Based on the presented results
in Fig. 16, both diagrams reach a permanent state after several
iterations.
In the second case, agent 4 sends the random information to
agent 8, leading to a convergence problem in the P2P market.
Therefore, as shown in Fig. 17(a) and (b), the corresponding
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination.

---


### Page 11

AGHAMOHAMMADI et al.: DECENTRALIZED ENERGY MANAGEMENT OF MULTIAGENT DISTRIBUTION SYSTEMS
11
Fig. 16.
Simulation results when there is no convergence problem. (a) Evolution of the stationary distribution matrix. (b) Evolution of the standard deviation
value during the running iterations.
Fig. 17.
Simulation results when agent 4 sends fraudulent data to agent 8, without considering a central entity to supervise convergence problems. (a) Evolution
of the stationary distribution matrix. (b) Evolution of the standard deviation value during the iterations.
Fig. 18.
Simulation results when agent 4 sends fraudulent data to agent 8, with a central entity to supervise convergence problems. (a) Evolution of the stationary
distribution matrix. (b) Evolution of the standard deviation value during the iterations.
numbers are increasing in both matrix π(k) and the corresponding standard deviation diagram. In this case, the process of
“identifying and mitigating the convergence problems” by the
supervisor entity is not deployed in the market; therefore, the
market diverges and the convergence problem will not be solved.
In the third case, agent 4 sends the incorrect information
to agent 8 again; but in this case, the control entity becomes
suspicioustothe P2Pmarketwhenthestandarddeviationofπ(k)
in Fig. 18(b) exceeds a certain threshold value. Therefore, the
supervisor entity has proceeded to identify problematic agents.
Then as it ensures that the agents have a problem and the
problem is not transient; the supervisor entity prohibits their
energy exchange. As a result, their power exchange reaches zero.
Finally, the effect of this action can be seen in Fig. 18(a), where
the P2P market has converged.
IV. CONCLUSION
In this article, a decentralized framework is presented for
operating the P2P energy market in the distribution network
considering multiagent systems and network constraints. In
addition, the uncertainties associated with the power generation
of renewable energy units are modeled using a data-driven DRO
model. As a result, each agent can exchange energy with other
agents as well as the upper-level network in the developed P2P
energy market. This would enable the agent to minimize its
costs while maintaining its privacy and autonomy. In addition,
a novel method for modeling the grid reliability as a cost term
while running the P2P market is proposed. The obtained results
present the importance of considering the reliability of the grid
while optimizing the scheduling of local resources. Finally,
an algorithm is presented to identify and reduce the effect of
convergence problems due to the misbehavior of agents while
running the P2P market. This algorithm would enable to check
the correctness of the communicated information as well as
prevent misbehavior by agents. The proposed scheme is implemented on the modiﬁed IEEE-37 and IEEE-69 bus test system
to illustrate the effectiveness of the proposed P2P management
structure considering the operating constraints of the grid.
REFERENCES
[1] M. Ourahou, W. Ayrir, B. E. Hassouni, and A. Haddi, “Review on smart
grid control and reliability in presence of renewable energies: Challenges
and prospects,” Math. Comput. Simul., vol. 167, pp. 19–31, 2020.
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination.

---


### Page 12

12
IEEE SYSTEMS JOURNAL
[2] T. Logenthiran, D. Srinivasan, and D. Wong, “Multi-agent coordination
for DER in Micro Grid,” in Proc. IEEE Int. Conf. Sustain. Energy Technol.,
2008, pp. 77–82.
[3] A. Rajaei, S. Fattaheian-Dehkordi, M. Fotuhi-Firuzabad, and M. MoeiniAghtaie, “Decentralized transactive energy management of multimicrogrid distribution systems based on ADMM,” Int. J. Elect. Power
Energy Syst., vol. 132, 2021, Art. no. 107126.
[4] S. Talari, M. Khorasany, R. Razzaghi, W. Ketter, and A. S. Gazafroudi,
“Mechanism design for decentralized peer-to-peer energy trading considering heterogeneous preferences,” Sustain. Cities Soc., vol. 87, 2022,
Art. no. 104182.
[5] S. Cui, Y.-W. Wang, and J.-W. Xiao, “Peer-to-peer energy sharing among
smart energy buildings by distributed transaction,” IEEE Trans. Smart
Grid, vol. 10, no. 6, pp. 6491–6501, Nov. 2019.
[6] A. Paudel, K. Chaudhari, C. Long, and H. B. Gooi, “Peer-to-peer energy
trading in a prosumer-based community microgrid: A game-theoretic
model,” IEEE Trans. Ind. Electron., vol. 66, no. 8, pp. 6087–6097,
Aug. 2018.
[7] M. I. S. L. Purage, A. Krishnan, E. Y. Foo, and H. B. Gooi, “Cooperative
bidding-based robust optimal energy management of multimicrogrids,”
IEEE Trans. Ind. Inform., vol. 16, no. 9, pp. 5757–5768, Sep. 2019.
[8] L. P. M. I. Sampath, A. Paudel, H. D. Nguyen, E. Y. Foo, and H. B.
Gooi, “Peer-to-peer energy trading enabled optimal decentralized operation of smart distribution grids,” IEEE Trans. Smart Grid, vol. 13, no. 1,
pp. 654–666, Jan. 2021.
[9] L. Chen, N. Liu, and J. Wang, “Peer-to-peer energy sharing in distribution
networks with multiple sharing regions,” IEEE Trans. Ind. Inform., vol. 16,
no. 11, pp. 6760–6771, Nov. 2020.
[10] J. Li, C. Zhang, Z. Xu, J. Wang, J. Zhao, and Y.-J. A. Zhang, “Distributed
transactive energy trading framework in distribution networks,” IEEE
Trans. Power Syst., vol. 33, no. 6, pp. 7215–7227, Jun. 2018.
[11] G. Liu, T. Jiang, T. B. Ollis, X. Zhang, and K. Tomsovic, “Distributed
energy management for community microgrids considering network operational constraints and building thermal dynamics,” Appl. Energy, vol. 239,
pp. 83–95, 2019.
[12] Y. Wang, Z. Huang, M. Shahidehpour, L. L. Lai, Z. Wang, and Q. Zhu,
“Reconﬁgurable distribution network for managing transactive energy
in a multi-microgrid system,” IEEE Trans. Smart Grid, vol. 11, no. 2,
pp. 1286–1295, Feb. 2019.
[13] N. Liu, M. Cheng, X. Yu, J. Zhong, and J. Lei, “Energy-sharing provider
for PV prosumer clusters: A hybrid approach using stochastic programming and Stackelberg game,” IEEE Trans. Ind. Electron., vol. 65, no. 8,
pp. 6740–6750, Aug. 2018.
[14] P. Salyani, R. Nourollahi, K. Zare, and R. Razzaghi, “A cooperative game
approachforoptimalresiliency-orientedschedulingoftransactivemultiple
microgrids,” Sustain. Cities Soc., vol. 89, 2023, Art. no. 104358.
[15] M. Khorasany, A. Najaﬁ-Ghalelou, and R. Razzaghi, “A framework for
joint scheduling and power trading of prosumers in transactive markets,”
IEEE Trans. Sustain. Energy, vol. 12, no. 2, pp. 955–965, Apr. 2020.
[16] H. Nezamabadi and V. Vahidinasab, “Arbitrage strategy of renewablebased microgrids via peer-to-peer energy-trading,” IEEE Trans. Sustain.
Energy, vol. 12, no. 2, pp. 1372–1382, Apr. 2020.
[17] S. Fattaheian-Dehkordi, A. Rajaei, A. Abbaspour, M. Fotuhi-Firuzabad,
and M. Lehtonen, “Distributed transactive framework for congestion management of multiple-microgrid distribution systems,” IEEE Trans. Smart
Grid, vol. 13, no. 2, pp. 1335–1346, Mar. 2021.
[18] A. Rajaei, S. Fattaheian-Dehkordi, M. Fotuhi-Firuzabad, M. MoeiniAghtaie, and M. Lehtonen, “Developing a distributed robust energy management framework for active distribution systems,” IEEE Trans. Sustain.
Energy, vol. 12, no. 4, pp. 1891–1902, Oct. 2021.
[19] C. Wei, Z. Shen, D. Xiao, L. Wang, X. Bai, and H. Chen, “An optimal
scheduling strategy for peer-to-peer trading in interconnected microgrids based on RO and Nash bargaining,” Appl. Energy, vol. 295, 2021,
Art. no. 117024.
[20] J. Li, M. E. Khodayar, J. Wang, and B. Zhou, “Data-driven distributionally
robust co-optimization of P2P energy trading and network operation for
interconnected microgrids,” IEEE Trans. Smart Grid, vol. 12, no. 6,
pp. 5172–5184, Nov. 2021.
[21] C. Duan, L. Jiang, W. Fang, and J. Liu, “Data-driven afﬁnely adjustable
distributionallyrobustunitcommitment,”IEEETrans.Power Syst.,vol.33,
no. 2, pp. 1385–1398, Apr. 2017.
[22] N. Liu, X. Yu, C. Wang, C. Li, L. Ma, and J. Lei, “Energy-sharing
model with price-based demand response for microgrids of peer-to-peer
prosumers,” IEEE Trans. Power Syst., vol. 32, no. 5, pp. 3569–3583,
Sep. 2017.
[23] Y. Liu, H. B. Gooi, Y. Li, H. Xin, and J. Ye, “A secure distributed
transactive energy management scheme for multiple interconnected microgrids considering misbehaviors,” IEEE Trans. Smart Grid, vol. 10, no. 6,
pp. 5975–5986, Nov. 2019.
[24] D.Gregorattiand J.Matamoros,“Distributedenergytrading:Themultiplemicrogrid case,” IEEE Trans. Ind. Electron., vol. 62, no. 4, pp. 2551–2559,
Apr. 2014.
[25] G. Tsaousoglou, P. Pinson, and N. G. Paterakis, “Transactive energy for
ﬂexible prosumers using algorithmic game theory,” IEEE Trans. Sustain.
Energy, vol. 12, no. 3, pp. 1571–1581, Mar. 2021.
[26] M. Elkazaz, M. Sumner, and D. Thomas, “A hierarchical and decentralized
energymanagementsystemforpeer-to-peerenergytrading,”Appl.Energy,
vol. 291, 2021, Art. no. 116766.
[27] M. Toﬁghi-Milani, S. Fattaheian-Dehkordi, M. Gholami, M. FotuhiFiruzabad, and M. Lehtonen, “A novel distributed paradigm for energy
scheduling of islanded multiagent microgrids,” IEEE Access, vol. 10,
pp. 83636–83649, 2022.
[28] M. Toﬁghi-Milani, S. Fattaheian-Dehkordi, M. Fotuhi-Firuzabad, and
M. Lehtonen, “Decentralized active power management in multi-agent
distribution systems considering congestion issue,” IEEE Trans. Smart
Grid, vol. 13, no. 5, pp. 3582–3593, Sep. 2022.
[29] H. Saberi, C. Zhang, and Z. Y. Dong, “Data-driven distributionally robust
hierarchical coordination for home energy management,” IEEE Trans.
Smart Grid, vol. 12, no. 5, pp. 4090–4101, May 2021.
[30] S. Fattaheian-Dehkordi, A. Abbaspour, M. Fotuhi-Firuzabad, and M.
Lehtonen, “A distributed framework for intense ramping management
in distribution networks,” IEEE Trans. Smart Grid, vol. 14, no. 1,
pp. 315–327, Jan. 2022.
[31] S. Fattaheian-Dehkordi, A. Abbaspour, M. Fotuhi-Firuzabad, and M.
Lehtonen, “Incentive-based ﬂexible-ramp-up management in multimicrogrid distribution systems,”
IEEE Syst. J., vol. 16, no. 3,
pp. 5011–5022, Sep. 2022, doi: 10.1109/JSYST.2022.3161730.
[32] M. A. Ortega-Vazquez, “Optimal scheduling of electric vehicle charging
and vehicle-to-grid services at household level including battery degradation and price uncertainty,” IET Gener., Transmiss., Distrib., vol. 8, no. 6,
pp. 1007–1016, 2014.
[33] J. W. Mitchell, “Power line failures and catastrophic wildﬁres under
extreme weather conditions,” Eng. Failure Anal., vol. 35, pp. 726–735,
2013.
[34] P. J. Maliszewski, E. K. Larson, and C. Perrings, “Environmental determinantsofunscheduledresidentialoutagesintheelectricalpowerdistribution
of Phoenix, Arizona,” Rel. Eng. Syst. Saf., vol. 99, pp. 161–171, 2012.
[35] M. Farivar and S. H. Low, “Branch ﬂow model: Relaxations and
convexiﬁcation—Part I,” IEEE Trans. Power Syst., vol. 28, no. 3,
pp. 2554–2564, Sep. 2013.
[36] P. Mohajerin Esfahani and D. Kuhn, “Data-driven distributionally robust
optimization using the Wasserstein metric: Performance guarantees and
tractable reformulations,” Math. Program., vol. 171, no. 1, pp. 115–166,
2018.
[37] C. Zhao and Y. Guan, “Data-driven risk-averse stochastic optimization with Wasserstein metric,” Operations Res. Lett., vol. 46, no. 2,
pp. 262–267, 2018.
[38] C. Duan, W. Fang, L. Jiang, L. Yao, and J. Liu, Distributionally Robust
Chance-Constrained Voltage-Concerned DC-OPF with Wasserstein Metric, 2017.
[39] S. Boyd, N. Parikh, E. Chu, B. Peleato, and J. Eckstein, “Distributed optimization and statistical learning via the alternating direction method of multipliers,” Found. Trends Mach. Learn., vol. 3, no. 1,
pp. 1–122, 2011.
[40] O. Vukovi´c and G. Dán, “Security of fully distributed power system state
estimation: Detection and mitigation of data integrity attacks,” IEEE J.
Sel. Areas Commun., vol. 32, no. 7, pp. 1500–1508, Jul. 2014.
[41] Z. Qu, Cooperative Control of Dynamical Systems: Applications to Autonomous Vehicles. Berlin, Germany: Springer Science & Business Media,
2009.
[42] [Online].
Available:
https://drive.google.com/ﬁle/d/1Gz PC1
Ieq IV9LTKPIgic MSZq5n6ZRi T2Y/view?usp=sharing
This article has been accepted for inclusion in a future issue of this journal. Content is final as presented, with the exception of pagination.

---
