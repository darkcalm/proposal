

---

Page 1

---

Exploring Blockchain for The Coordination of
Distributed Energy Resources
Qing Yang
College of Electronics and Information Engineering
and Blockchain Technology Research Center
Shenzhen University
Shenzhen, China
yang.qing@szu.edu.cn
Hao Wang*
Department of Data Science and Artiﬁcial Intelligence
Faculty of Information Technology
Monash University
Melbourne, VIC 3800, Australia
hao.wang2@monash.edu
Abstract—The fast growth of distributed energy resources
(DERs), such as distributed renewables (e.g., rooftop PV panels),
energy storage systems, electric vehicles, and controllable ap-
pliances, drives the power system toward a decentralized system
with bidirectional power ﬂow. The coordination of DERs through
an aggregator, such as a utility, system operator, or a third-party
coordinator, emerges as a promising paradigm. However, it is not
well understood how to enable trust between the aggregator and
DERs to integrate DERs efﬁciently. In this paper, we develop
a trustable and distributed coordination system for DERs using
blockchain technology. We model various DERs and formulate
a cost minimization problem for DERs to optimize their energy
trading, scheduling, and demand response. We use the alternating
direction method of multipliers (ADMM) to solve the problem in
a distributed fashion. To implement the distributed algorithm in
a trustable way, we design a smart contract to update multipliers
and communicate with DERs in a blockchain network. We
validate our design by experiments using real-world data, and the
simulation results demonstrate the effectiveness of our algorithm.
Index Terms—Smart grid, distributed energy resource (DER),
energy management, distributed optimization, blockchain
I. INTRODUCTION
Various factors, such as concerns about climate change, have
driven the fast growth of distributed energy resources (DERs)
in the power system. These DERs often include distributed
renewables (e.g., rooftop PV panels), energy storage systems,
electric vehicles, and controllable appliances, such as heating,
ventilation, and air conditioning (HVAC), water heaters, and
washers. Due to the stochastic and non-dispatchable nature of
DERs, it is challenging to manage DERs by the centralized
approach used in the operation of today’s power system. A
paradigm shift toward a decentralized power system with
bidirectional power ﬂow is gaining attention to enable the
integration of DERs. The widely accepted roadmap is inte-
grating hundreds of thousands of DERs through an aggregator,
such as a utility, system operator, or a third-party coordinator.
However, it is not well understood how to build trust between
DERs and the aggregator to coordinate DERs. This paper aims
to explore blockchain, known as a decentralized ledger, to
facilitate a trustable system for the decentralized coordination
of DERs.
*Corresponding author: Hao Wang.
A. Related works
A large body of literature studied how to coordinate DERs
for various applications. For example, the aggregation of
controllable loads, distributed generators, and energy storage
was studied in [1] for mitigating the impact of the variable
renewable generations. The integration of distributed renew-
ables as a virtual power plant was studied in [2]. Other
research considered coordinating DERs to provide demand
response (DR) in addition to feeding electricity back to the
grid. Customer-owned DERs, such as HVAC, water heaters,
and cloth washers, can be switched on or off to absorb or
shed power. For example, using electric space heating loads in
a building to defer power consumption was studied in [3]. How
to coordinate ﬂexible loads to build demand response capacity
was illustrated in [4]. Recent studies also explored other
transactive energy applications for DERs, such as ancillary
services [5]–[7] and peer-to-peer energy trading [8]. However,
the above studies adopted centralized solution methods, which
causes privacy concerns and operational problems, as DERs
are often owned by independent prosumers.
Great efforts have also been made to develop distributed
solutions to the coordination of DERs. For example, Wang
and Huang in [9] designed an incentive mechanism and a
distributed algorithm for energy trading among interconnected
microgrids. Yang and Wang in [10] developed a distributed
transactive energy management scheme for smart homes to
energy trading and manage their HVAC systems. You et al. in
[11] developed distributed solutions to the scheduling problem
of battery swapping for electric vehicles. A fully distributed
algorithm was proposed in [12] for a virtual power plant
considering the transmission limits and constraints of DERs.
Most of the developed distributed algorithms shared similar
underlying methodologies, such as primal-dual decomposition
and alternating direction method of multipliers (ADMM).
However, such algorithms often need to be executed by DERs
and a central computing node that updates the dual variables.
Such a design has a risk of single-point failure and also
requires a veriﬁable and trustable computing environment.
This paper is motivated to address the above problem and
facilitate a trustable system for the coordination of DERs.
arXiv:2103.06046v1  [cs.DC]  10 Mar 2021


---

Page 2

---

B. Our Work and Contributions
Blockchain [13] is a decentralized ledger that can provide
trust and transparency to the transactions. Blockchain can also
execute smart contracts to run generic programs to enable
various functions. Recently, the energy sector has been keen to
explore blockchain technology to enable transactional digital
platforms and improve the efﬁciencies of the system. For
example, LO3 Energy [14] deployed a blockchain system to
allow online payments for energy trading in a microgrid.
In this work, we take a further step to design a blockchain
system for DERs to enable distributed optimization and build
a trustable and efﬁcient future energy system. Specially, we
formulate an optimization problem for DERs to interact with
each other and with the grid by feeding back energy and
performing demand response. Given the popularity of ADMM
in the distributed energy system, we also decompose our DER
optimization problem and solve it using ADMM to coordinate
DERs in a distributed manner. We design a trustable DER
coordination system based on the blockchain technology by
implementing the updating rules for the dual variables in a
smart contract on the blockchain system. Our design provides
a generic approach to the implementation of distributed opti-
mization algorithms on blockchain and thus enable a trustable
and efﬁcient system for the coordination of DERs in the future
power grid.
The remainder of this paper is organized as follows. Sec-
tion II introduces the system model and formulates the DERs
cost minimization problem. Section III presents the design
of the distributed algorithm and blockchain system for the
coordination of DERs. Section IV presents the simulation
results of DER coordination. Section V concludes our work.
II. SYSTEM MODEL AND FORMULATION
We
consider
a
group
of
prosumers
denoted
as
N={1, 2, . . . , N},
and
each
prosumer
i∈N
has
a
set
of DERs, including ﬂexible loads (such as air conditioners
and shiftable loads), distributed renewables, and behind-
the-meter energy storage, as shown in Fig. 1. The DERs
are coordinated by a blockchain-based coordination system
to optimize their energy schedule over a time horizon
T ={1, 2, . . . , T}, which is evenly divided into T time slots.
For example, in a daily schedule, each day can be divided
into T = 24 time slots.
A. prosumers and Distributed Energy Resources
Before modeling DERs, we present the prosumers’ grid
power purchase, as prosumers are interconnected in a dis-
tributed network. We denote the power purchase of prosumer
i in time slot t ∈T as pG
i [t], and its grid is written as
CG
i = πE
X
t∈T pG
i [t] + πD max
t∈T pG
i [t],
which consists of two charges to the prosumers. The ﬁrst
term πE
P
t∈T pG
i [t] is called the energy charge, which is
based on the accumulative energy consumed. The second term
πD maxt∈T pG
i [t] is called the demand charge, which is based
Grid
Virtual power plant
Prosumer i’s
smart house
Renewable
Air Conditioner
Shiftable
Battery
Powerline
Fig. 1. The system model and the operational principle for the coordination
of DERs.
on the peak demand over the horizon T. Such a demand charge
drives prosumers to reduce their peak load and thus alleviate
the system peak. Given the physical capacity, the electricity
purchased from the grid satisﬁes the following constraints:
0 ≤pG
i [t] ≤P G
i , ∀i ∈N, t ∈T ,
(1)
in which pG
i [t] is non-negative and bounded by the capacity
of the grid power supply P G
i .
In the following, we model DERs, including ﬂexible loads,
renewables, and energy storage.
1) Flexible Loads: We take the HVAC as a typical example
of an adjustable appliance. The indoor temperature of pro-
sumer i in time slot t is denoted as τ In
i [t], and τ Ref
i
is the
preferred indoor temperature. The indoor temperature evolves
with the HVAC load pAC
i [t] and the outdoor temperature
τ Out[t]. Based on the model of HVAC [15], [16], the dynamics
of the indoor temperature is
τ In
i [t] = τ Out[t] −
 τ Out[t] −τ In
i [t −1]

e1/RC
+γipAC
i [t−1], ∀i ∈N, ∀t ∈T ,
(2)
in which the coefﬁcients R and C are the equivalent heat
capacity and thermal resistance of the HVAC, respectively,
and γi indicates the operating mode of heating or cooling.
We model prosumer i’s experience of using HVAC as a
discomfort cost, which measures the deviation of the indoor
temperature τ In
i [t] to the preferred temperature τ Ref
i
. Specif-
ically, the discomfort cost is a quadratic function shown as
CAC
i
= ωAC
X
t∈T
 τ In
i [t] −τ Ref
i
2 , ∀i ∈N,
in which the coefﬁcient ωAC is the prosumer’s sensitivity to
the discomfort. Also, the indoor temperature should be kept
within an accepted range, shown as
T AC ≤τ In
i [t] ≤T
AC, ∀i ∈N, ∀t ∈T ,
(3)
where T AC and T
AC are the upper-bound and lower-bound for
the indoor temperature at all times.
Another type of load called shiftable load pS
i [t] represents
the appliances with their usage shifted over a time window


---

Page 3

---

T S
i . Typical shiftable appliances include washers that can be
shifted to any available time slots. But prosumers often have
a routine schedule to use these appliances, and we denote the
preferred schedule for the shiftable load as P S
i [t]. Prosumers
can schedule shiftable loads within T S
i as long as the task is
completed. Therefore, we have the following constraints for
shiftable loads:
X
t
pS
i [t] =
X
t
P S
i [t], t ∈T S
i , i ∈N.
(4)
Rescheduling shiftable appliances change prosumers’ rou-
tine behaviors and cause discomfort as well. Similarly, we
model the discomfort cost as a quadratic function as
CS
i = ωS
X
t∈T S
i
 pS
i [t] −P S
i [t]
2 ,
in which the coefﬁcient ωS is prosumers’ sensitivity to load
shifting. For both discomfort costs CAC
i
and CS
i , we use
quadratic functions, which are widely used in energy eco-
nomics literature to capture marginal increase in costs.
2) Distributed Renewables: In addition to purchasing elec-
tricity from the grid, prosumers have distributed renewable
generations to use. We denote prosumer i’s renewable gener-
ation in time slot t as P RE
i
[t]. Prosumers can choose to use
renewable supply to meet their loads and also feed renewable
back to the grid. The local renewable energy usage pRE
i [t] of
prosumer i should satisfy the following constraints:
0 ≤pRE
i [t] ≤P RE
i
[t], ∀i ∈N, t ∈T .
(5)
Note that we assume that prosumer i’s renewable generation
can be predicted day-ahead. For the feed-in renewable, we will
discuss it with feed-in tariff in Section II-B.
3) Energy Storage: We assume that prosumer i has an
energy storage unit with a capacity of EB
i . We let eB
i [t], pCH
i [t],
and pDIS
i
[t] denote the energy storage level, the amount of
charging power and discharging power, respectively. The en-
ergy storage operation should satisfy the following constraints:
eB
i [t]=eB
i [t−1]+ηCH
i pCH
i [t]−1
ηDIS
i
pDIS
i
[t], ∀i∈N, t∈T ,
(6)
αB
i EB
i ≤eB
i [t] ≤αB
i EB
i , ∀i ∈N, t ∈T ,
(7)
0 ≤pCH
i [t] ≤P CH
i
, ∀i ∈N, t ∈T ,
(8)
0 ≤pDIS
i
[t] ≤P DIS
i
, ∀i ∈N, t ∈T ,
(9)
in which ηCH
i
∈[0, 1] and ηDIS
i
∈(0, 1] are the efﬁciencies
of charging and discharging. Constraints (7)-(9) specify the
box constraints for the energy storage level, the amount of
charging power and discharging power. For example, αB
i and
αB
i denote the minimum and maximum fraction of the energy
storage capacity for the feasible range of the energy storage
level. Similarly, P CH
i
and P DIS
i
denote the maximum amount
of charging power and discharging power, respectively.
The energy storage operation incurs degradation, and we
model its cost as
CB
i = βB
i
X
t∈T
 pCH
i [t] + pDIS
i
[t]

,
which is a function of charging and discharging power. Note
that βB
i is the cost coefﬁcient.
B. Interaction of Distributed Energy Resources
Prosumers can interact with each other to trade energy using
their renewable and energy storage. Also, prosumers can feed
renewable back to the grid and perform demand response using
ﬂexible loads.
We ﬁrst model the energy trading among prosumers. For
a pair of prosumers i and j, where j ∈N\i, they can trade
energy denoted as pET
i,j[t]. Note that pET
i,j[t] > 0 indicates that
prosumer i sells energy to j; otherwise, pET
i,j[t] < 0 indicates
that prosumer i purchases energy from j. We assume that the
power loss during the energy trade is negligible. Thus, the
energy trading for any pair i and j satisﬁes the following
clearing constraints:
pET
i,j[t] + pET
i,j[t] = 0, ∀t ∈T , ∀i ∈N, ∀j ∈N\i.
(10)
A feed-in tariff (FIT) provides rewards to FIT-eligible
renewable generators to feed electricity back to the grid and
thus serves as a policy instrument to promote the adoption of
renewable energy. We denote the FIT rate as πFIT[t] for all
the prosumers. Each prosumer i decides how much renewable
to sell to the grid, which is denoted as pFIT
i
[t]. Therefore, we
have the following constraints for feed-in energy:
0 ≤pFIT
i
[t] ≤P RE
i
[t] −pRE
i [t], ∀i ∈N, ∀t ∈T ,
(11)
in which the feed-in renewable energy pFIT
i
[t] is non-negative
and no greater than the available renewable energy excluding
the self-consumed renewable, i.e., P RE
i
[t] −pRE
i [t].
For the feed-in renewable energy, prosumer i can earn a FIT
revenue RFIT
i
as
RFIT
i
=
X
t∈T πFIT[t]pFIT
i
[t].
The demand response program is another service that pro-
sumers can provide and earn extra revenue. The grid operator
usually sends DR requests during peak hours to ask prosumers
to reduce their load. Prosumers can decide whether or not
and how much load they can reduce, denoted as pDR
i [t]. Once
prosumers respond to the DR requests and perform load
reduction, they can receive rewards at a unit rate of πDR[t]
from the grid. The revenue from DR RDR
i
is written as
RDR
i
=
X
t∈T
πDR[t]pDR
i [t].
The prosumers’ load reduction only counts their grid pur-
chase and thus is bounded by its scheduled grid power
purchase pG
i [t]. Thus, we have the following constraints for
the load reduction pDR
i [t]:
0 ≤pDR
i [t] ≤pG
i [t], ∀i ∈N, t ∈T .
(12)


---

Page 4

---

C. Problem Formulation
All the prosumers need to balance their supply and demand
and aim to minimize the total costs. Speciﬁcally, prosumer i
needs to satisfy the the following balance constraints:
pAC
i [t] + pS
i [t] + pCH
i [t] +
X
j∈N\i pET
i,j[t]
= pRE
i [t] + pG
i [t] −pDR
i [t] + pDIS
i
[t], ∀t ∈T ,
(13)
in which the left-hand side is the total demand of prosumer i,
and the right-hand side is the total realized supply of i, all in
time slot t.
For the simplicity of the notations, we deﬁne pG
i
=
{pG
i [t], ∀t}, pAC
i
= {pAC
i [t], ∀t}, τ IN
i
= {τ IN
i [t], ∀t}, pS
i =
{pS
i [t], ∀t}, pCH
i
= {pCH
i [t], ∀t}, pDIS
i
= {pDIS
i
[t], ∀t}, pET
i
=
{pET
i,j[t], ∀t, ∀j}, pFIT
i
= {pFIT
i
[t], ∀t}, and pDR
i
= {pDR
i [t], ∀t}.
We consider optimally coordinating DERs and aim to min-
imize the total cost of DERs. Therefore, we formulate the
following DERs Cost Minimization problem.
DCM: DERs Cost Minimization
minimize
X
i∈N
CH
i (pG
i , pAC
i , τ IN
i , pS
i , pCH
i , pDIS
i
)
−
X
i∈N
 RET
i (pET
i ) + RFIT
i
(pFIT
i
) + RDR
i (pDR
i )

subject to
(1) −(13)
variables:
{pG
i , pAC
i , τ IN
i , pS
i , pCH
i , pDIS
i
, pET
i , pFIT
i
, pDR
i }.
Note that the centralized method is not available for solving
Problem DCM, as the centralized solution requires prosumers
to reveal private information and thus causes serious privacy
concerns. Therefore, we will develop a privacy-persevering
distributed optimization algorithm to solve Problem DCM and
discuss how to implement the algorithm as a smart contract
working on a blockchain system in Section III.
III. DISTRIBUTED ALGORITHM ON BLOCKCHAIN
This section will present the design of a distributed algo-
rithm to coordinate DERs, which can be implemented as a
smart contract working on the blockchain.
A. Distributed Algorithm
To preserve the prosumers’ privacy and solve the optimal
solution to Problem DCM, we design a distributed optimiza-
tion algorithm that can be implemented as a smart contract on
a blockchain system.
The ADMM method [17] provides a distributed solu-
tion method, which has been used in energy trading [9]
for its good convergence and scalability. We ﬁrst introduce
ˆpET
i ={ˆpET
i,j[t], ∀t, ∀j} as the auxiliary variables for the energy
trading decisions pET
i . To replace (10), we introduce equivalent
constraints as
ˆpET
i,j[t] = pET
i,j[t], ∀j∈N\i, ∀i∈N, ∀t∈T ,
(14)
ˆpET
i,j[t]+ˆpET
j,i[t] = 0, ∀j∈N\i, ∀i∈N, ∀t ∈T .
(15)
We deﬁne the dual variables λi={λi,j[t], ∀j∈N\i, t∈T }
for constraints (14) and decompose Problem DCM into the
following two tasks executed by prosumers and a smart
contract on the blokchain.
PLTi: Prosumer i’s Local Task
minimize
X
i∈N
CH
i (pG
i , pAC
i , τ IN
i , pS
i , pCH
i , pDIS
i
)
−
X
i∈N
 RET
i (pET
i ) + RFIT
i
(pFIT
i
) + RDR
i (pDR
i )

+
X
t∈T
X
j∈N \i
hρ
2
 ˆpET
i,j[t]−pET
i,j[t]
2 −λi,j[t]pET
i,j[t]
i
subject to
(1) −(9), (11) −(13), (15)
variables:
pG
i , pAC
i , τ IN
i , pS
i , pCH
i , pDIS
i
, pET
i , pFIT
i
, pDR
i .
Prosumer i determines the optimal energy schedule and
trading for DERs in Task PLTi. Then the prosumers call
the smart contract in Task SCT to get the updated dual
variables λi and auxiliary variables ˆpET
i
to solve Problem
DCM iteratively.
After receiving prosumers’ energy trading decisions pET
i ,
the smart contract solves the following optimization task.
SCT: Smart Contract Task
minimize
X
t∈T
X
i∈N
X
j∈N \i
nρ
2
 ˆpET
i,j[t] −pET
i,j[t]
2
+ λi,j[t]ˆpET
i,j[t]
o
subject to
(15)
variables:
{ˆpET
i , ∀i ∈N},
in which, the smart contract updates the dual variables λi
and auxiliary variables ˆpET
i
and broadcasts to prosumers.
Speciﬁcally, Task SCT solves the optimal auxiliary variables
as
ˆpET
i,j[t]=ρ
 pET
i,j[t] −pET
j,i[t]

−(λi,j[t] −λj,i[t])
2ρ
,
(16)
and updates the dual variables as
λi,j[t] ←λi,j[t] + ρ
 ˆpET
i,j[t] −pET
i,j[t]

.
(17)
B. Blockchain for the Coordination of DERs
In our work, we employ blockchain technology to facilitate
the coordination of DERs for three purposes. First, we adopt
the blockchain to implement an open and veriﬁable DER
energy coordination platform. Unlike the conventional central-
ized energy coordination, the blockchain provides a trustable
computing machine that can execute the DER coordination
algorithm written in a smart contract. Therefore, the use of
the blockchain removes the need for a centralized coordinator
and guarantees the correctness of the coordination algorithm.
Second, the blockchain network can be used as a secure and
robust data communication network to exchange information
among prosumers. Third, the blockchain also provides an
efﬁcient payment tool for energy trading and service rewards.
For the underlying blockchain system, we let the users’
smart meters be the blockchain nodes to form the blockchain


---

Page 5

---

Blockchain network
Smart contract
Prosumer i’s
smart meter
Other prosumers
Block node
Execute the PLTi
①Read the auxiliary variable
and dual
variable
from the smart contract
②Compute the locally optimal DER schedule
③Update
to the smart contract
④Repeat ①to ③until algorithm converges
Execute the SCT
①Receive the users’ energy trading decisions
②Calculate the auxiliary variable
and dual variable
Read 
and 
Update 
Fig. 2.
The process of the distributed DER coordination algorithm on
blockchain.
network, as shown in Fig. 2. Modern smart meters are
equipped with embedded systems that support embedded op-
erating systems (e.g., Ubuntu Core) and application software,
including the blockchain software. The prosumers’ smart me-
ters can connect to the blockchain network via the wireless
communication link such as LoRa and 5G Narrowband IoT.
The connected smart meters form a peer-to-peer network
that supports data communication and the operation of the
blockchain.
We choose the Ethereum blockchain with proof-of-authority
(PoA) consensus protocol (Clique) based on the following
considerations in this work. First, Ethereum is an open and
mature blockchain project supported by most of the operating
systems and hardware. Second, the consensus protocol, which
is used to synchronized the states of all the blockchain nodes,
has a critical impact on the performance of the blockchain.
We select the PoA consensus rather than proof-of-work (PoW)
because the computational complexity of PoW is prohibitively
high for smart meters’ hardware resources. Third, Ethereum
supports the smart contract for the users to implement their
function in the Solidity programming language.
The blockchain nodes in Fig. 2 can be divided into two
categories: PoA nodes and normal nodes. The normal nodes
are the normal prosumers that can send transactions and
interact with the smart contract. The normal nodes can also
access the data on the blockchain and verify the execution of
the transactions. Among the normal nodes, some are selected
as the PoA nodes that participate in the consensus process
of the blockchain. Speciﬁcally, a group of PoA nodes forms a
committee to receive the transactions, execute smart contracts,
and package them to generate a new block in a round-robin
manner. The PoA nodes can also vote to add a node into or
remove a node out of the committee.
As discussed in Section III-A, we implement the SCT
part of the distributed algorithm in the smart contract on
the blockchain. Since the execution of the smart contract is
transparent and veriﬁable, the result of the SCT is guaranteed
to be correct and trustable. Speciﬁcally, the smart contract
in Fig. 2 implements three functions. The ﬁrst function is
to let the prosumers update their energy trading decisions
pET
i . The second function is to solve the problem of SCT
as in Eq. (16) and Eq. (17). The third function is to let
the prosumers read the latest value of dual variables λi and
auxiliary variables ˆpET
i . In each iteration of the distributed
algorithm, the prosumer i ﬁrst read the value of λi and ˆpET
i
from the smart contract, then solve the problem of PLTi
to compute pET
i , and ﬁnally update this value to the smart
contract. The smart contract automatically executes the second
function when all the trading decisions are updated. This
algorithm iterates until the results converge to the optimal
coordination schedule.
IV. NUMERICAL RESULTS
To evaluate the performance of our design, we simulate the
blockchain-based DER coordination system with a distributed
algorithm using real-world data [18], [19]. Due to the page
limit, we do not include the implementation detail.
First, we evaluate the convergence of the distributed opti-
mization algorithm in Section III with 10 prosumers. We see
in Fig. 3 that the algorithm converges within 10 iterations to
keep the error below the preset error threshold.
Second, we show the optimal energy schedule of 10 pro-
sumers over one week in Fig. 4. Prosumers’ grid supply and
renewable proﬁles in 4(a)-(b) are complementary to each other,
as prosumers ﬁrst use their local renewables and then use grid
Fig. 3. The convergence of the proposed distributed optimization algorithm.
(a)
(b)
(c)
(d)
Fig. 4. The optimal energy schedule of DERs including (a) grid supply, (b)
renewable energy supply, (c) shiftable load, and (d) HVAC load.


---

Page 6

---

(a)
(b)
Fig. 5. The service schedule of (a) the feed-in energy and (b) the demand
response.
(a)
(b)
Fig. 6. The energy trading records of two typical users: (a) user 1 and (b)
user 6.
power if there is a deﬁcit in renewable generation. The optimal
scheduling of shiftable and HVAC loads in 4(c)-(d) exhibits a
similar trend because they have similar shiftable appliances
and face the same outdoor temperature. But the shiftable
and HVAC loads still show some diversity as prosumers’
operational preferences of their DERs are different.
Third, Fig. 5 illustrates the optimized feed-in energy and
demand response. We see from Fig. 5(a) that prosumers sell
extra renewable generations to the grid when the system has
a low demand. In Fig. 5(b), prosumers perform differently in
demand response as they have different local generation and
load proﬁles, and some of them do not have the capacity to
respond to demand response signals in the peak hours.
Fourth, Fig. 6 shows the optimal energy trading of two typi-
cal prosumers. We see that prosumers 1 and 6 are two different
types, as prosumer 1 has higher renewable generations and
sells a lot to others, while prosumer 6 lacks local renewables
and needs to buy energy from other prosumers most of the
time. The blockchain-based DER coordination system helps
the prosumers to trade energy with each other and interact
with the grid to sell energy or perform demand response, which
signiﬁcantly improves the efﬁciency of the system.
V. CONCLUSION
This paper developed a blockchain system for the coordina-
tion of distributed energy resources. We modeled energy trad-
ing, feed-in energy, and demand response for various DERs.
Given prosumers’ independence, we designed a distributed
optimization algorithm to coordinate DERs to minimize their
costs. More importantly, we developed a blockchain system
with a smart contract to execute the distributed optimization
algorithm for DERs to facilitate the trustable and efﬁcient
integration of DERs. We validated our design by numerical
simulations using real-world data.
For our future work, we will 1) model more services that
DERs can provide, 2) consider network constraints for DERs,
and 3) implement the blockchain system on the Internet of
things devices.
REFERENCES
[1] M. J. Kasaei, M. Gandomkar, and J. Nikoukar, “Optimal management
of renewable energy sources by virtual power plant,” Renewable energy,
vol. 114, pp. 1180–1188, 2017.
[2] N. Naval, R. S´anchez, and J. M. Yusta, “A virtual power plant optimal
dispatch model with large and small-scale distributed renewable gener-
ation,” Renewable Energy, vol. 151, pp. 57–69, 2020.
[3] A. Thavlov and H. W. Bindner, “Utilization of ﬂexible demand in a
virtual power plant set-up,” IEEE Transactions on Smart Grid, vol. 6,
no. 2, pp. 640–647, 2014.
[4] M. Royapoor, M. Pazhoohesh, P. J. Davison, C. Patsios, and S. Walker,
“Building as a virtual power plant, magnitude and persistence of de-
ferrable loads and human comfort implications,” Energy and Buildings,
vol. 213, p. 109794, 2020.
[5] E. Mashhour and S. M. Moghaddas-Tafreshi, “Bidding strategy of virtual
power plant for participating in energy and spinning reserve markets-part
i: Problem formulation,” IEEE Transactions on Power Systems, vol. 26,
no. 2, pp. 949–956, 2010.
[6] C. Ji, P. You, E. J. Pivo, Y. Shen, D. F. Gayme, and E. Mallada, “Optimal
coordination of distribution system resources under uncertainty for joint
energy and ancillary service market participation,” Preprint, pp. 1–5,
2019.
[7] O. Borne, M. Petit, and Y. Perez, “Provision of frequency-regulation
reserves by distributed energy resources: Best practices and barriers to
entry,” in 2016 13th International Conference on the European Energy
Market (EEM).
IEEE, 2016, pp. 1–7.
[8] M. R. Alam, M. St-Hilaire, and T. Kunz, “Peer-to-peer energy trading
among smart homes,” Applied energy, vol. 238, pp. 1434–1443, 2019.
[9] H. Wang and J. Huang, “Incentivizing energy trading for interconnected
microgrids,” IEEE Transactions on Smart Grid, vol. 9, no. 4, pp. 2647–
2657, 2018.
[10] Q. Yang and H. Wang, “Cooperative energy management of hvac via
transactive energy,” in 2020 IEEE 16th International Conference on
Control & Automation (ICCA).
IEEE, 2020, pp. 1271–1277.
[11] P. You, S. H. Low, L. Zhang, R. Deng, G. B. Giannakis, Y. Sun,
and Z. Yang, “Scheduling of ev battery swapping-part ii: Distributed
solutions,” IEEE Transactions on Control of Network Systems, vol. 5,
no. 4, pp. 1920–1930, 2017.
[12] G. Chen and J. Li, “A fully distributed admm-based dispatch approach
for virtual power plant problems,” Applied Mathematical Modelling,
vol. 58, pp. 300–312, 2018.
[13] I. Bashir, Mastering Blockchain: Distributed ledger technology, decen-
tralization, and smart contracts explained. Packt Publishing Ltd, 2018.
[14] “Building a robust value mechanism to facilitate transactive energy,”
Technical Whitepaper, LO3 Energy, 2017. [Online]. Available: https:
//exergy.energy/wp-content/uploads/2017/12/Exergy-Whitepaper-v8.pdf
[15] S. Cui, Y.-W. Wang, and J.-W. Xiao, “Peer-to-peer energy sharing among
smart energy buildings by distributed transaction,” IEEE Trans. Smart
Grid, vol. 10, no. 6, pp. 6491–6501, 2019.
[16] N. Lu, “An evaluation of the hvac load potential for providing load
balancing service,” IEEE Transactions on Smart Grid, vol. 3, no. 3, pp.
1263–1270, 2012.
[17] S. Boyd, N. Parikh, E. Chu, B. Peleato, and J. Eckstein, “Distributed
optimization and statistical learning via the alternating direction method
of multipliers,” Found. Trends Mach. Learn., vol. 3, no. 1, pp. 1–122,
2011.
[18] H. Wang and J. Huang, “Joint investment and operation of microgrid,”
IEEE Transactions on Smart Grid, vol. 8, no. 2, pp. 833–845, 2017.
[19] Energy Research, Website, Pecan Street Inc., accessed Oct. 1, 2019.
[Online]. Available: https://www.pecanstreet.org/dataport/
