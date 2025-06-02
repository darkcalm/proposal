

---

Page 1

---

Scalable multi-agent reinforcement learning for distributed control of
residential energy ﬂexibility
Flora Charbonniera,∗, Thomas Morstynb, Malcolm D. McCullocha
aDepartment of Engineering Science, University of Oxford, UK
bSchool of Engineering, University of Edinburgh, UK
Abstract
This paper proposes a novel scalable type of multi-agent reinforcement learning-based coordination for distributed
residential energy. Cooperating agents learn to control the ﬂexibility oﬀered by electric vehicles, space heating and
ﬂexible loads in a partially observable stochastic environment. In the standard independent Q-learning approach,
the coordination performance of agents under partial observability drops at scale in stochastic environments.
Here, the novel combination of learning from oﬀ-line convex optimisations on historical data and isolating marginal
contributions to total rewards in reward signals increases stability and performance at scale. Using ﬁxed-size
Q-tables, prosumers are able to assess their marginal impact on total system objectives without sharing personal
data either with each other or with a central coordinator. Case studies are used to assess the ﬁtness of diﬀerent
combinations of exploration sources, reward deﬁnitions, and multi-agent learning frameworks. It is demonstrated
that the proposed strategies create value at individual and system levels thanks to reductions in the costs of
energy imports, losses, distribution network congestion, battery depreciation and greenhouse gas emissions.
Keywords:
Energy management system, multi-agent reinforcement learning, demand-side response,
peer-to-peer, prosumer, smart grid.
Highlights
• Privacy-preserving multi-agent reinforcement learning is used to coordinate residential energy
• Learning from optimisations improves coordination scalability in stochastic environments
• Marginal reward signals further enhance cooperation relative to previous approaches
• The curse of dimensionality is mitigated by the use of ﬁxed-size Q-tables
• Case studies with large real-life datasets yield 33.7% local and global cost reductions
1. Introduction
This paper addresses the scalability issue of dis-
tributed domestic energy ﬂexibility coordination in a
cost-eﬃcient and privacy-preserving manner. A novel
class of coordination strategies using optimisation-
based multi-agent reinforcement learning (MARL1)
with ﬁxed Q-table size is proposed for household-level
decision-making, tackling the challenge of scalability for
simultaneously learning independent agents under par-
tial observability in a stochastic environment [1]. Mul-
tiple versions of the novel strategy are assessed to max-
imise the statistical expectation of system-wide bene-
ﬁts, including local battery costs, grid costs and green-
house gas emissions.
Widespread electriﬁcation of primary energy pro-
vision and decarbonisation of the power sector are
two vital prerequisites for limiting anthropogenic global
warming to 1.5oC above pre-industrial levels. To reduce
risks of climate-related impacts on health, livelihood,
security and economic growth, intermittent renewable
power supplies could be required to supply 70% to 85%
of electricity by 2050 [2]. However, this poses the chal-
lenges of the intermittency and limited controllability of
resources [3]. Therefore, a robust, decarbonised power
system will rely on two structural features: decentral-
isation and demand response (DR) [4]. The coordina-
tion of distributed ﬂexible energy resources can help
reduce costs for transmission, storage, peaking plants
and capacity reserves, improve grid stability, align de-
mand with decarbonised energy provision, promote en-
ergy independence and security, and lower household
energy bills [5, 6].
Residential sites constitute a signiﬁcant share of po-
tential DR, representing for example 38.5% of the 2019
UK electricity demand, and 56.4% of energy consump-
tion if including transport and heat, which are both
∗Corresponding author
Email address: flora.charbonnier@eng.ox.ac.uk (Flora Charbonnier)
1A full nomenclature is available in Appendix A
Preprint submitted to Applied Energy
March 29, 2022
arXiv:2203.03417v2  [eess.SY]  27 Mar 2022


---

Page 2

---

undergoing electriﬁcation [7]. Increasing ownership of
EVs and PV panels has been facilitated by regulatory
changes, with many countries committing to internal
combustion car phase-outs in the near future, and by
plummeting costs, with an 82% and 87% levelised cost
drop between 2010 and 2019 for EVs and PV panels
[8, 9]. This potential is so far underexploited, as DR pri-
marily focuses on larger well-known industrial and com-
mercial actors that require less coordination and data
management [10], with most customers still limited to
trade with utility companies [11]. The primary hurdles
to unlocking residential ﬂexibility are the high capital
cost of communication and control infrastructure as the
domestic potential is highly fragmented [4], concerns
about privacy and hindrance of activities [12, 6], and
computational challenges for real-time control at scale
[13].
Traditionally, convex optimisation would be used to
maximise global coordination objectives in convex prob-
lems with variables known ahead of time. Techniques
such as least-squares and linear programming have been
well-studied for over a century [14]. However, residen-
tial energy coordination presents challenges to its appli-
cation. Firstly, optimisations that are centralised are
hindered by privacy, acceptance, and communication
constraints, and present exponential time complexity
at the scale of millions of homes [15]. Secondly, stan-
dard optimisation methods cannot be used without full
knowledge of the system’s inputs and dynamics [16].
In residential energy, agents only have partial observ-
ability of the system due to both the stochasticity and
uncertainty of environment variables such as individual
residential consumption and generation proﬁles, and to
the privacy and infrastructure cost constraints that hin-
der communication between agents during implemen-
tation [17].
Not relying on shared information may
also improve the robustness of the solutions to failure
of other agents, communication delays, and unreliable
information, and improve adaptability to changing en-
vironments [18]. Finally, the real-life complex electric-
ity grid environment may not be amenable to a con-
vex model representation. Due to the heterogeneity of
users and behaviours needing diﬀerent parameters and
models, the large-scale use of model-based controllers
is cumbersome [19].
A model-free approach instead
avoids modelling non-trivial interactions of parameters,
including private information [15].
Given these challenges to residential energy ﬂexi-
bility coordination, and the speciﬁc constraints of the
problem at play which renders traditional approaches
unsuitable, we seek to develop a novel coordination
mechanism which satisﬁes the following criteria, as
tested in real-life scenarios:
• Computational scalability: minimal and constant
computation burden during implementation as
the system size increases;
• Performance scalability: no drop in coordination
performance as the system size increases, mea-
sured in savings obtained per hour and per agent;
• Acceptability: local control of appliances, no com-
munication of personal data, thermal discomfort,
or hindrance/delay of activities.
The rest of this paper is organised as follows. In
Section 2 we motivate the novel MARL approach with
a literature review and a gap analysis. In Section 3, a
system model is presented that includes household-level
modelling of EVs, space heating, ﬂexible loads and PV
generation. Section 4 lays out the MARL methodol-
ogy, with various methodological options for indepen-
dent agents to learn to cooperate.
In Section 5, the
input data used to populate the model is presented. In
Section 6, the performance of diﬀerent MARL strategies
is compared to lower and upper bounds in case studies.
Finally, we conclude in Section 7.
2. MARL-based energy coordination: literature
review and gap analysis
Reinforcement learning (RL) can overcome the con-
straints faced by centralised convex optimisation for
residential energy coordination, by allowing for decen-
tralised and model-free decision-making based on par-
tial knowledge.
RL is an artiﬁcial intelligence (AI)
framework for goal-oriented agents2 to learn sequen-
tial decision-making by interacting with an uncertain
environment [22]. As an increasing wealth of data is
collected in local electricity systems, RL is of growing
interest for the real-time coordination of distributed en-
ergy resources (DERs) [23, 5].
Instead of optimising
based on inherently uncertain data, RL more realisti-
cally searches for statistically optimal sequential deci-
sions given partial observation and uncertainty, with no
a priori knowledge [16]. Approximate learning methods
may be more computationally scalable, more eﬃcient
in exploring high-dimensional state spaces and there-
fore more scalable than exact global optimisation with
exponential time complexity [24, 15].
As classiﬁed in [25], numerous RL-based coordina-
tion methods have been proposed in the literature for
residential energy coordination, though with remain-
ing limitations in terms of scalability and privacy pro-
tection. On the one hand, in RL-based direct control
strategies, a central controller directly controls individ-
ual units, and households directly forfeit their data and
control to a central RL-based scheduler [26].
While
most existing AI-based DR research thus assumes fully
observable tasks [23], direct controllability of resources
from diﬀerent owners with diﬀerent objectives and re-
sources and subject to privacy, comfort and security
concerns is challenging [27]. Moreover, centralised poli-
cies do not scale due to the curse of dimensionality as
the state and action spaces grow exponentially with the
system size [28]. On the other hand, RL-based indi-
rect control strategies consider decision-making at the
2Here agents are independent computer systems acting on behalf of prosumers [20]. Prosumers are proactive consumers with
distributed energy resources actively managing their consumption, production and storage of energy [21].
2


---

Page 3

---

prosumer level, entering the realm of MARL. This can
be achieved using diﬀerent communication structures,
with either centralised, bilateral, or no sharing of per-
sonal information, as presented below.
Firstly, agents may share information with a cen-
tral entity, which in turn broadcasts signals based on a
complete picture of the coordination problem. For ex-
ample, the central entity may send unidirectional price
signals to customers based on information such as pro-
sumers’ costs, constraints and day-ahead forecasts. RL
can inform both the dynamic price signal [29, 30], and
the prosumer response to price signals [30, 31].
The
central entity may also collect competitive bids and set
trades and match prosumers centrally, where RL algo-
rithms are used to reﬁne individual bidding strategies
[32, 33, 34, 35, 36] or to dictate the auction market
clearing [11, 37].
Units may also use RL to cooper-
ate towards common objectives with the mediation of
a central entity that redistributes centralised personal
information [38, 39, 40, 41]. However, information cen-
tralisation also raises costs, security, privacy and scal-
ability of computation issues. Biased information may
lead to ineﬃcient or even infeasible decisions [42].
Secondly, RL-based coordination has been proposed
where prosumers only communicate information bilat-
erally without a central authority. For example, in [43]
agents use transfer learning with distributed W-learning
to achieve local and system objectives. Bilateral peer-
to-peer communication oﬀers autonomy and expression
of individual preferences, though with remaining risks
around privacy and bounded rationality [44]. There is
greater robustness to communication failures compared
situations with a single point of failure. However, as
the system size increases, the number of communica-
tion iterations until algorithmic convergence increases,
requiring adequate computational resources and limited
communication network latency for feasibility [45]. The
safe way of implementing distributed transactions to en-
sure data protection is an ongoing subject of research
[25].
Finally, in RL-based implicit coordination strate-
gies, prosumers rely solely on local information to make
decisions. For example, in [46, 47], competitive agents
in isolation maximise their proﬁts in RL-based energy
arbitrage, though they do not consider the impacts of
individual actions on the rest of the system, with po-
tential negative impacts for the grid. For example, a
concern is that all loads receive the same incentive,
the natural diversity on which the grid relies may be
diminished [48], and the peak potentially merely dis-
placed, with overloads on upstream transformers. Im-
plicit cooperation, which keeps personal information at
the local level while encouraging cooperation towards
global objectives, has been thus far under-researched
beyond frequency control.
In [49], agents learn the
optimal way of acting and interacting with the envi-
ronment to restore frequency using local information
only.
This is a promising approach for decentralised
control.
However, the applicability in more complex
scenarios with residential electric vehicles and smart
heating load scheduling problems has not been consid-
ered.
Moreover, the convergence slows down for in-
creasing number of agents, and scalability beyond 8
agents has not been investigated. Indeed, fundamental
challenges to the coordination of simultaneously learn-
ing independent agents at scale under partial observ-
ability in a stochastic environment have been identi-
ﬁed when using traditional RL algorithms [1]: indepen-
dent learners may reach individual policy equilibriums
that are incompatible with a global Pareto optimal, the
non-stationarity of the environment due to other con-
currently learning agents aﬀects convergence, and the
stochasticity of the environment prevents agents from
discriminating between their own contribution to global
rewards and noise from other agents or the environ-
ment. Novel methods are therefore needed to develop
this approach.
We seek to bridge this gap, using implicit coordina-
tion to unlock the so-far largely untapped value from
residential energy ﬂexibility to provide both individual
and system beneﬁts. We propose a new class of MARL-
based implicit cooperation strategies for residential DR,
to make the best use of the ﬂexibility oﬀered by in-
creasingly accessible assets such as photovoltaic (PV)
panels, electric vehicle (EV) batteries, smart heating
and ﬂexible loads.
Agents learn RL policies using a
data-based, model-free statistical approach by explor-
ing a shared environment and interacting with decen-
tralised partially observable Markov decision processes
(Dec-POMDPs), either through random exploration or
learning from convex optimisation results. In the ﬁrst
rehearsal phase [50] with full understanding of the sys-
tem, they learn to cooperate to reach system-wide ben-
eﬁts by assessing the global impact of their individual
actions, searching for trade-oﬀs between local, grid and
social objectives. The pre-learned policies are then used
to make decisions under uncertainty given limited local
information only.
This approach satiﬁes the computational scalability,
coordination scalability and acceptance criteria set out
in this paper.
Firstly, the real-time control method is computa-
tionally scalable thanks to ﬁxed-size Q-tables which
avoid the curse of dimensionality, and there is only
minimal, constant local computation required to imple-
ment the pre-learned policies during implementation.
No further communication is required for implementa-
tion. This increases robustness to communication is-
sues and data inaccuracy relative to when relying on
centralised and bilateral communication, and cuts the
costs of household computation and two-way communi-
cation infrastructure.
Secondly, we address the outstanding MARL coor-
dination performance scalability issue for agents with
partial observability in a stochastic environment seek-
ing to maximise rewards which also depend on other
concurrently learning agents [51, 1]. The case studies in
this paper show that allowing agents to learn from om-
niscient, stable, and consistent optimisation solutions
can successfully act as an equilibrium-selection mecha-
nism, while the use of marginal rewards improves learn-
3


---

Page 4

---

ability3 by isolating individual contributions to global
rewards.
This novel methodological combination of-
fers signiﬁcant improvements on MARL scalability and
convergence issues, with high coordination performance
maintained as the number of agents increases, where
that of standard MARL drops at scale.
Finally, this method tackles acceptability issues,
with no interference in personal comfort nor commu-
nication of personal data.
The speciﬁc novel contributions of this paper are
(a) a novel class of decentralised ﬂexibility coordina-
tion strategies, MARL-based implicit cooperation, with
no communication and ﬁxed-size Q-tables to mitigate
the curse of dimensionality; (b) a novel MARL explo-
ration strategy for agents under partial observability
to learn from omniscient, convex optimisations prior to
implementation for convergence to robust cooperation
at scale; and (c) the design and testing with large banks
of real-world data of combinations of reward deﬁnitions,
exploration strategies and multi-agent learning frame-
works for assessing individual impacts on global energy,
grid and storage costs.
Methodologies are identiﬁed
which outperform a baseline with increasing numbers
of agents despite uncertainty.
3. Local system description
In this section, the variables, objective function and
constraints of the problem are described. This sets the
frame for the application of the RL algorithms pre-
sented in Section 4.
3.1. Variables
We consider a set of time steps t ∈T = {t0, ..., tend}
and a set of prosumers i ∈P = {1, ..., n}.
Decision
variables are italicised and input data are written in
roman. Energy units are used unless speciﬁed other-
wise.
Participants have an EV, a PV panel, electric
space heating and generic ﬂexible loads.
The EV at-home availability µt
i (1 if available, 0 oth-
erwise), EV demand for required trips dt
EV,i, household
electric demand dt
i, PV production pt
PV,i, external tem-
perature Tt
e and solar heat ﬂow rate φt are speciﬁed as
inputs for t ∈T and i ∈P.
The local decisions by prosumers are the energy
ﬂows in and out of the battery bt
in,i and bt
out,i, the
electric heating consumption ht
i and the prosumer con-
sumption ct
i. These have both local and system impacts
(Figure 1). Local impacts include battery energy levels
Et
i, losses ϵt
ch,i and ϵt
dis,i, prosumer import pt
i, build-
ing mass temperature T t
m,i and indoor air temperature
T t
air,i. System impacts arise through the costs of total
grid import gt and distribution network trading. Dis-
tribution network losses and reactive power ﬂows are
not included.
3.2. Objective function
Prosumers cooperate to minimise system costs con-
sisting of grid (ct
g), distribution (ct
d) and storage (ct
s)
costs. This objective function will be maximised both
in convex optimisations oﬀ-line – to provide an up-
per bound for the achievable objective function, and in
some cases to provide information to the learners dur-
ing the simulated learning phase – and in the learning
of MARL policies for decentralised online implementa-
tion.
max F =
X
∀t∈T
ˆFt =
X
∀t∈T
−(ct
g + ct
d + ct
s)
(1)
ct
g = Ct
g
 gt + ϵg

(2)
Where losses incurred by imports and exports from and
to the main grid are approximated as
ϵg = R
V2
 gt2
(3)
The grid cost coeﬃcient Ct
g is the sum of the grid
electricity price and the product of the carbon inten-
sity of the generation mix at time t and the Social
Cost of Carbon which reﬂects the long-term societal
cost of emitting greenhouse gases [52].
The impacts
of local decisions on upstream energy prices are ne-
glected. Grid losses are approximated using the nom-
inal root mean square grid voltage V and the average
resistance between the main grid and the distribution
network R [53], based on the assumption of small net-
work voltage drops and relatively low reactive power
ﬂows [54]. The second-order dependency disincentivises
large power imports and exports, which helps ensure in-
teractions of transmission and distribution networks do
not reduce system stability.
ct
d = Cd
X
i∈P
max
 −pt
i, 0

(4)
Distribution costs ct
d are proportional to the distribu-
tion charge Cd on exports. The resulting price spread
between individual imports and exports decreases risks
of network constraints violation by incentivising the use
of local ﬂexibility ﬁrst [55]. Distribution network losses
due to power ﬂows between prosumers are neglected so
there is no second-order dependency.
ct
s = Cs
X
i∈P
 bt
in,i + bt
out,i

(5)
Storage battery depreciation costs ct
s are assumed to
be proportional to throughput using the depreciation
coeﬃcient Cs, assuming a uniform energy throughput
degradation rate [56].
3“the sensitivity of an agent’s utility to its own actions as opposed to actions of others, which is often low in fully cooperative
Markov games” [1]
4


---

Page 5

---

𝑔! grid import
𝑝"
! prosumer import
𝑝#!
Σ = 0
𝑐"
!
consumption
Σ = 0
Prosumer 𝑛
Prosumer 1
d$%,"
!
 EV demand
Σ = 𝐸!'" −𝐸!
PV production 
p(),"
*
Houseshold 
demand d"
!
EV Battery
Substation
𝑏+#,"
!
𝜖,-.,"
!
loss
Temperature 
T"
*
ℎ"
!
heating
𝑏/0!,"
!
charge & discharge
𝜖1! grid loss
𝜖23,"
!
Figure 1: Local system model. Red dotted lines denote energy balances.
3.3. Constraints
Let E0, E and E be the initial, minimum and maxi-
mum battery energy levels, ηch and ηdis the charge and
discharge eﬃciencies, and bin the maximum charge per
time step. Demand dtD
i,k is met by the sum of loads con-
sumed ˆci,k,tC,tD at time tC by prosumer i for load of
type k (ﬁxed or ﬂexible) demanded at tD. The ﬂexi-
bility boolean fi,k,tC,tD indicates if time tC lies within
the acceptable range to meet dtD
i,k. A Crank-Nicholson
scheme [57] is employed to model heating, with κ a 2x5
matrix of temperature coeﬃcients, and Tt
i and T
t
i lower
and upper temperature bounds. System constraints for
steps ∀t ∈T and prosumers ∀i ∈P are:
• Prosumer and substation energy balance (see Fig-
ure 1)
pt
i = ct
i + ht
i + bt
in,i
ηch
−ηdisbt
out,i −pt
PV,i
(6)
X
i∈P
pt
i = gt
(7)
• Battery energy balance
Et+1
i
= Et
i + bt
in,i −bt
out,i −dt
EV,i
(8)
• Battery charge and discharge constraints
E0 = Et0
i = Etend
i
+ btend
in,i −btend
out,i −dtend
EV,i
(9)
µt
iEi ≤Et
i ≤Ei
(10)
bt
in,i ≤µt
ibin
(11)
bt
out,i ≤µt
iEi
(12)
• Consumption ﬂexibility — the demand of type k
at time tD by prosumer i must be met by the
sum of partial consumptions ˆci,k,tC,tD at times
tC...tC + nﬂex within the time frame nﬂex speci-
ﬁed by the ﬂexibility of each type of demand in
matrix fi,k,tC,tD
X
tC∈T
ˆci,k,tC,tDfi,k,tC,tD = dtD
i,k
(13)
• Consumption — the total consumption at time
tC is the sum of all partial consumptions ˆci,k,tC,tD
meeting parts of demands from current and pre-
vious time steps tD:
X
tD∈N
ˆci,k,tC,tD = ctC
i,k
(14)
• Heating — the workings to obtain this equation
are included in Appendix C:
T t+1
m,i
T t+1
air,i

= κ
1, T t
m,i, Tt
e, φt, ht
i
⊺
(15)
Tt
i ≤T t
air,i ≤T
t
i
(16)
• Non-negativity constraints
ct
i, ht
i, Et
i, bt
in,i, bt
out,i, ˆci,l,tC,tD ≥0
(17)
While the proposed framework could accommodate
the use of idiosyncratic satisfaction functions to perform
trade-oﬀs between ﬂexibility use and users’ comfort,
no such trade-oﬀs are considered in this paper, with
comfort requirements for temperature and EV usage
always being met. Field evaluations have shown that
programmes that do not maintain thermal comfort are
consistently overridden, increasing overall energy use
and costs [58], while interference in consumption pat-
terns and temperature set-points cause dissatisfaction
[5].
Meeting ﬁxed domestic loads, ensuring suﬃcient
charge for EV trips, and maintaining comfortable tem-
peratures are therefore set constraints.
4. Reinforcement learning methodology
The MARL approach is now presented in which in-
dependent prosumers learn to make individual decisions
which together maximise the statistical expectation of
the objective function in Section 3.
At time step t ∈T , each agent is in a state st
i ∈S
corresponding to accessible observations (here the time-
varying grid cost), and selects an action at
i ∈A as de-
ﬁned in Section 4.3. This action dictates the decision
5


---

Page 6

---

variables in Section 3.1 bt
in,i, bt
out,i, ht
i and ct
i. The en-
vironment then produces a reward rt ∈R which cor-
responds to the share ˆFt of the system objective func-
tion presented in Section 3.2 and agents transition to
a state st+1
i
. Agents learn individual policies πi by in-
teracting with the environment using individual, decen-
tralised ﬁxed-size Q-tables.
We ﬁrst introduce the Q-learning methodology.
Then, the mapping between the RL agent action and
the decision variables in Section 3.1 is presented. Fi-
nally, we propose variations on the learning method,
with diﬀerent experience sources, multi-agent struc-
tures and reward deﬁnitions.
4.1. Q-Learning
While
any
reinforcement
learning
methodology
could be used with the framework proposed in this pa-
per, here we focus on Q-learning, a model-free, oﬀ-
policy RL methodology.
Its simplicity and proof of
convergence make it suited to developing novel learning
methodologies in newly deﬁned environments [5]. State-
actions values Q(s, a) represent the expected value of all
future rewards rt ∀t ∈T when taking action a in state
s according to policy π:
Q(s, a) ≜Eπ[rt + γrt+1 + γ2rt+2...|st = s, at = a]
(18)
where γ is the discount factor setting the relative im-
portance of future rewards. Estimates are reﬁned in-
crementally as
ˆQ(s, a) ←ˆQ(s, a) + αδ
(19)
where δ is the temporal-diﬀerence error,
δ =

rt + γ ˆV (snext) −ˆQ(s, a)

(20)
ˆV is the state-value function estimate,
ˆV (s) =
max
a∗∈A(s)
ˆQ(s, a∗)
(21)
and α is the learning rate. In this work we use hys-
teretic learners, i.e. chieﬂy optimistic learners that use
an increase rate superior to the decrease rate in order to
reduce oscillations in the learned policy due to actions
chosen by other agents [1, 59]. For β < 1:
α =
(
α0
if δ > 0
α0β
otherwise
(22)
Agents follow an ϵ-greedy policy to balance explo-
ration of diﬀerent state-action pairs and knowledge ex-
ploitation. The greedy action with highest estimated
rewards is selected with probability 1 −ϵ and random
actions otherwise.
a∗=
(
arg max a∗∈A ˆQ(s, a∗)
if x ∼U(0, 1) > ϵ
a ∼p(a) =
1
|A| ∀a ∈A
otherwise
(23)
Henceforth, we refer to the estimates ˆQ and ˆV as Q
and V to reduce the amount of notation.
4.2. Agent state
The agent state is deﬁned by the time-dependent
grid cost coeﬃcient Ct
g, i.e. the sum of the grid elec-
tricity price and the product of the carbon intensity
of the generation mix at time t and the social cost of
carbon.
To convert the RL policy action into local decisions,
the agent also requires information on their current PV
generation, battery level, ﬂexible loads and indoor air
temperature, as described below in Section 4.3.
4.3. Agent action
Large action spaces compound the curse of dimen-
sionality in Q-learning and waste exploration resources
[28]. At each time step, the decision variables in Sec-
tion 3 controlling the ﬂows in and out of the batterybt
in,i
and bt
out,i, the electric heating consumption ht
i and the
prosumer consumption ct
i for household i are therefore
synthesised into a single variable ψ ∈[0, 1] controlling
the use of available local ﬂexibility. Figure 2 shows how
consumption (for domestic loads and heat), imports and
storage change with ψ.
At each step, the ﬁxed requirements for loads, heat
and upcoming EV trips are ﬁrst met. The ψ decision
then applies to the remaining ﬂexibility. In conditions
deemed optimal for energy exports ψ = 0, all initial
storage and residual PV generation is exported and ﬂex-
ible loads are delayed. On the other end, a passive agent
does not utilise its ﬂexibility and uses the default ac-
tion ψ = 1, maximising imports with EVs charged when
plugged in and no ﬂexible loads delayed. Intermediate
imports trade-oﬀs are mapped on Figure 2:
1. From exporting all to none of the initial storage
Et
i
2. From meeting ﬁxed loads dt
i,ﬁxed with the energy
stored to importing the required amount
3. From no to maximum ﬂexible consumption dt
i,tot
4. From exporting to storing PV energy pt
PV,i re-
maining after meeting loads
5. From importing no additional energy to ﬁlling up
the battery to capacity Ei
Costlier
actions
incurring
battery
depreciation,
losses and export costs are towards either ψ extreme,
only used in highly beneﬁcial situations (convex local
costs function in the lower plot of Figure 2).
Rank-
ing actions consistently ensures agents do not waste re-
sources trialling sub-optimal combinations of decisions.
For example, it is more cost-eﬃcient to ﬁrst absorb en-
ergy imports by consuming ﬂexible loads, and only use
the battery (incurring costs) if imports are large.
Note that although this action space is continuous,
it can be discretised into intervals for implementation
in Q-learning.
4.4. Variations of the learning method
Diﬀerent experience sources, reward deﬁnitions and
MARL structures are proposed within the MARL ap-
proach.
The performance of these combinations of
algorithmic possibilities will be assessed in Section 6 to
inform eﬀective model design.
6


---

Page 7

---

Cost
pPV<dfixed
dfixed<pPV<dtot
dtot<pPV
Energy
Δp Import
Δs Storage
c Consumption
ϵ Losses
Battery, loss & 
export costs
Ψ
Ψ
1 2
3 5
1
3
5
1
3 4 5
Ψ
Figure 2: Decision variable ψ. Sections 1-5 denote the trade-oﬀregimes described in Section 4.3. At each step, the ﬁxed requirements
for loads, heat and upcoming EV trips are ﬁrst met. The ψ decision then applies to the remaining ﬂexibility, from maximal energy
exports (full use of ﬂexibility) at ψ = 0, to maximal energy imports (no use of ﬂexibility) at ψ = 1. dtot and dﬁxed are the sum of
household and heating loads with and without their ﬂexible component. If ﬁxed loads cannot be fully met by PV energy, the residual
is met by storage and imports (2). If there is additional PV energy after meeting all loads, it can be stored or exported (4).
4.4.1. Experience sources
In data-driven strategies, the learning is determined
by the collected experience.
• Environment
exploration.
Traditionally,
agents collect experience by interacting with an
environment [22].
• Optimisations. A novel approach collects expe-
rience from optimisations. Learning from entities
with more knowledge or using knowledge more ef-
fectively than randomly exploring agents has pre-
viously been proposed, as with agents “mimick-
ing” humans playing video games [60]. Similarly,
agents learn from convex “omniscient” optimisa-
tions on historical data with perfect knowledge
of current and future variables. This experience
is then used under partial observability and con-
trol for stable coordination between prosumers
at scale.
Note in this case that, although the
MARL learning and implementation are model-
free, a model of the system is used to run the
convex optimisation and produce experience to
learn from. A standard convex optimiser uses the
same data that would be used to populate the en-
vironment explorations but solves over the whole
day-horizon with perfect knowledge of all vari-
ables using the problem description in Section 3.
Then, at each time step, the system variables
are translated into equivalent RL {st, at, rt, st+1}
tuples for each agent, which are used to update
the policies in the same way as for standard Q-
learning as presented below.
4.4.2. MARL structures
Both the centralised and decentralised structures
proposed use ﬁxed-size |S| × |A| Q-tables correspond-
ing to individual state-action pairs. The size of a global
Q-table referencing all possible combinations of states
and actions would grow exponentially with the number
of agents. This would limit scalability due to memory
limitations and exploration time requirements. More-
over, as strategies proposed in this paper are privacy-
preserving, only local state-action pairs are used for in-
dividual action selection, wasting the level of detail of
a global Q-table.
• Distributed learning. Each agent i learns its
Qi table with its own experience. No information
is shared between agents.
• Centralised learning. A single table Qc uses
experience from all agents during pre-learning.
All agents use the centrally learned policy for de-
centralised implementation.
4.4.3. Reward deﬁnitions
The reward deﬁnition is central to learning as its
maximisation forms the basis for incrementally alter-
ing the policy [22]. Assessing the impact of individual
actions on global rewards accurately is key to the ef-
fective coordination of a large number of prosumers. In
the following, the Q-tables Q0, Qdiﬀ,QA and Qcount may
be either agent-speciﬁc Qi or centralised Qc based on
the MARL structure. We proposed four variations of
the Q-table update rule for each experience step tuple
collected (st
i, at
i, rt, st+1
i
).
Q(st
i, at
i) ←Q(st
i, at
i) + αδ
(24)
• Total reward. The instantaneous total system
reward rt = ˆFt is used to update the Q-table Q0.
δ = rt + γV 0(st+1
i
) −Q0(st
i, at
i)
(25)
• Marginal reward.
The diﬀerence in total in-
stant rewards rt between that if agent i selects
the greedy action and that if it selects the default
action is used to update Qdiﬀ[61]. The default
action adefault corresponds to ψ = 1, where no
ﬂexibility is used. The default reward rt
ai=adefault,
where all agents perform their greedy action apart
from agent i which performs the default action, is
7


---

Page 8

---

obtained by an additional simulation.
δ =
 rt −rt
ai=adefault

+γV diﬀ(st+1
i
)−Qdiﬀ(st
i, at
i)
(26)
• Advantage reward.
The post diﬀerence be-
tween Q0 values when i performs the greedy and
the default action is used. This corresponds to
the estimated increase in rewards not just instan-
taneously but over all future states, analogously
to in [62]. No additional simulations are required
as the Q-table values are reﬁned over the normal
course of explorations.
δ =
 Q0(st
i, at
i) −Q0(st
i, aai=adefault)

−QA(st
i, at
i)
(27)
• Count. The Q-table stores the number of times
each state-action pair is selected by the optimiser.
αδ = 1
(28)
5. Input Data
This section presents the data that is fed into the
model presented in Section 3. Interaction with this data
will shape the policies learned through RL [22] and
should reﬂect resource intermittency and uncertainty
to maximise the expectation of rewards in a robust way
without over-ﬁtting. EV demand dt
EV,i and availability
µt
i, PV production pt
PV,i and electricity consumption dt
i
are drawn from large representative datasets.
5.1. Data selection and pre-processing
Load and PV generation proﬁles are obtained from
the Customer Led Network Revolution (CLNR), a UK-
based smart grid demonstration project [63, 64], and
mobility data from the English National Travel Sur-
vey (NTS) [65]. The NTS does not focus on EVs only
and oﬀers a less biased view into the general popula-
tion’s travel pattern than small-scale EV trials data,
both due to the smaller volume of data available com-
pared to for generic cars and because the self-selected
EV early trial participants may not be representative of
patterns once EVs become widely adopted. It is implic-
itly assumed that electriﬁcation will not aﬀect transport
patterns [66].
NTS data from 82,455 households from 2002 to 2017
results in 1,272,834 full days of travel proﬁles.
Load
and PV data from 11,907 customers between 2011 and
2014 yields 620,702 and 22,670 full days of data, respec-
tively. Proﬁles are converted to hourly resolution and
single missing points replaced with the ﬁgure from the
same time the day or week before or after which has the
lowest sum of squares of diﬀerences between the previ-
ous and subsequent point. Tested with available data,
this yields absolute errors with mean 0.13 and 0.08 kWh
and 99th percentile 1.09 and 0.81 kWh for PV and load
data. PV sources have nominal capacities between 1.35
and 2.02 kWp.
The at home-availability of the vehicles is inferred
from the recorded journeys’ origin and destination. EV
energy consumption proﬁles are obtained using rep-
resentative consumption factors from a tank-to-wheel
model proposed in [66], dependent on travel speed and
type (rural, urban, motorway).
5.2. Markov chain
During learning, agents continuously receive experi-
ence to learn from. However, numerous subsequent days
of data are not available for single agents. We design a
Markov chain mechanism to feed consistent proﬁles for
successive days, using both consistent scaling factors
and behaviour clusters.
Daily proﬁles for load and travel are normalised such
that P
t=0..24 xt = 1, and clustered using K-means,
minimising the within-cluster sum-of-squares [67] in
four clusters for both weekday and weekend data (with
one for no travel). The features used for load proﬁles
clustering are normalised peak magnitude and time and
normalised values over critical time windows, and those
for travel are normalised values between 6 am and 10
pm. PV proﬁles were grouped per month.
Probabilistic Markov chain transition rules are
shown in Table 1. Transition probabilities for clusters k
and scaling factors λ are obtained from available transi-
tions between subsequent days in the datasets for each
week day type w (week day or weekend day). Figure 3
shows that subsequent PV and load scaling factors fol-
low strong linear correlation, with the residuals of the
perfect correlation following gamma distributions with
zero mean, whereas EV load scaling factors follow more
complex patterns, so transitions probabilities are com-
puted between 50 discrete intervals.
6. Case study results and discussion
This section compares the performance of the res-
idential ﬂexibility coordination strategies presented in
Section 4 to baseline and upper bound scenarios for
increasing numbers of prosumers.
The performance
of traditionally used MARL strategies drops at scale,
while that of the novel optimisation-based methodol-
ogy using marginal rewards is maintained.
6.1. Set-up
The MARL algorithm is trained in oﬀ-line simula-
tions using historical data prior to online implemen-
tation.
This means agents do not trial unsuccessful
actions with real-life impacts during learning.
More-
over, the computation burden is taken prior to im-
plementation, while prosumers only apply pre-learned
policies, avoiding the computational challenges of large-
scale real-time control.
The learning occurs over 50 epochs consisting of an
exploration, an update and an evaluation phase. First,
the environment is explored over two training episodes
of duration |T | = 24 hours. Learning in batches of mul-
tiple episodes helps stabilise learning in the stochastic
environment. Then, Q-tables are updated based on the
rules presented in Section 4.4. Finally, an evaluation is
performed using a deterministic greedy policy on new
evaluation data.
Ten repetitions are performed such
8


---

Page 9

---

Normalised proﬁle
Scaling factor
PV
Randomly selected from current
month bank bt+1 = (m)
Computed as λt+1 = λt + x,
where
x ∼Γ (α(bt, bt+1), β(bt, bt+1))
Load
Cluster selected based on
transition probability
p(kt+1|kt, wt, wt+1)
Normalised proﬁle randomly
selected from bank
bt+1 = (kt+1, wt+1)
EV
Random variable from discrete
distribution p(λt+1|λt, bt, bt+1)
Table 1: Markov chain mechanism for selecting behaviour clusters, proﬁles and scaling factors for input data in subsequent days
that the learning may be assessed over diﬀerent trajec-
tories.
The Social Cost of Carbon is set at 70 £/tCO2, con-
sistent with the UK 2030 target [68]. Weather [69], elec-
tricity time-of-use prices [70] and grid carbon intensity
[71] are from January 2020, where relevant speciﬁed for
London, UK. The low solar heat gains in January are
neglected [72]. Other relevant parameters for the case
studies are listed in Appendix B.
As performed on a Intel(R) Core(TM) i7-9800X
CPU @ 3.80GHz, computation time for a learning tra-
jectory is 2′45′′ for one agent and 97′5′′ for 30 agents,
including evaluation points. The policy can then be di-
rectly applied at the household level during operation.
Case
study
results
using
diﬀerent
experience
sources, reward deﬁnitions and MARL structures are
presented in Figure 4. Acronyms for each strategy are
tabulated in the legend. Positive values denote savings
relative to a baseline scenario where all agents are pas-
sive, i.e. not using their ﬂexibility with EVs charged
immediately and no ﬂexible loads delayed. As the Q-
learning policies are ﬁrst initialised with zero values,
in the ﬁrst epoch of learning completely random action
values are chosen, which provides rewards far below the
baseline. As agents collect experience and update their
policies at each epoch, improved policies are learned,
some of which are able to outperform the baseline. An
upper bound is provided by results from “omniscient”
convex optimisations, which are however not achiev-
able in practice for three main reasons. Firstly, they
use perfect knowledge of all the environment variables
in the present and future, despite uncertainty in re-
newable generation, mix of the grid, and customer be-
haviour. Optimisation with inaccurate data would lead
to suboptimal results.
Secondly, prosumers may not
be willing to yield their data and direct control to an
external entity. Finally, central optimisations become
computationally expensive for real-time control of large
numbers of prosumers.
6.2. Results
Results presented in Figure 4 show that only the
algorithms learning from optimisations maintained sta-
ble coordination performance at scale, while the perfor-
mance of traditionally used MARL algorithms would
drop in this context of stochasticity and partial obser-
vation. The optimisation-based algorithm which uses
marginal rewards (MO) performed best.
We further
elaborate on the results in the subsections below.
6.2.1. Environment exploration-based learning
The centralised MARL structure is favoured for en-
vironment exploration-based learning (continuous lines
in Figure 4). A single policy uses experience collected
by all agents, rather than each agent learning from their
own experience only.
Figure 4 shows that environment exploration-based
MARL using total rewards (TE, orange), the baseline
0
10
20
30
0
20
40
60
80
0
10
20
30
0
20
40
60
80
Load, ρ = 0.87
EV consumption, ρ = 0.19  
ft [-]
ft [-]
ft+1 [-]
Figure 3: Scaling factors for normalised proﬁles (i.e. total daily loads in kWh) in subsequent days. Linear correlation can be observed
for the load proﬁles, while more complex patterns are exhibited for EV consumption. ρ is the Pearson correlation coeﬃcient.
9


---

Page 10

---

0
10
20
30
40
50
0.25
0.20
0.15
0.10
0.05
0.00
0.05
0.10
0.15
100
101
0.25
0.20
0.15
0.10
0.05
0.00
0.05
0.10
0.15
Number of prosumers
Baseline
Optimal
Centralised
Decentralised
Reference
MARL structure
1 prosumer
End savings vs. number of prosumers
Epoch
Savings relative to baseline [£/h/prosumer]
Explorer Optimiser
Total rewards
Marginal
Advantage
Count
TE
ME
AE
TO
MO
AO
CO
Figure 4: The left-hand side plot shows the ﬁve-epoch moving average of evaluation rewards relative to baseline rewards for a single
prosumer. The right-hand side plot shows the mean of the ﬁnal 10 evaluations against the number of prosumers. Lines show median
values and shaded areas the 25th and 75th percentiles over the 10 repetitions. The best-performing MARL structure is displayed
for each exploration source and reward deﬁnition pair. The performance of the baseline MARL algorithm (TE, orange) drops as the
number of concurrently learning agents in the stochastic environment increases; the best-performing alternative algorithm proposed
(MO, purple) maintains high performance at scale.
MARL framework, exhibits a high performance for a
single agent. However, savings drop as the number of
cooperating agents increases, down to around zero from
ten agents. Coordination challenges arise for indepen-
dent learners to isolate the contribution of their actions
to total rewards from the stochasticity of the environ-
ment, compounded by other simultaneously learning
agents’ random explorations, and the non-stationarity
of their on-policy behaviour [1].
Using advantage rewards (AE, grey), based on esti-
mates of the long-term value of actions relative to that
of the baseline action, yields superior results beyond
two agents. However, as AE uses the total reward Q0-
table as an intermediary step, results similarly drops
for increasing numbers of agents.
Using marginal rewards (ME, dark green), the value
of each agent’s action relative to the baseline action
is singled out immediately by an additional simulation
and used as a reward at each time step. This improves
the performance relative to TE and AE for ﬁve agents
and more, though still with declining performance as
the number of agents increases.
6.2.2. Optimisation-based learning
Optimisation-based learning generally favours the
distributed MARL structure, with agents able to con-
verge to distinct compatible policies (dashed lines in
Figure 4).
Comparing trajectories in Figure 4, learning from
the total rewards obtained by an optimiser (TO, light
blue) yields lower savings than when using environment
explorations (TE). The learned policies yield negative
savings, i.e.
would provide worse outcomes than in-
ﬂexible agents. The omniscient optimiser takes precise,
extreme decisions thanks to its perfect knowledge of all
current and future system variables, importing at very
high ψ values when it is optimal to do so. RL algorithms
on the other hand are used under partial observability,
aiming for actions that statistically perform well under
uncertainty.
Agents independently picking TO-based
decisive actions in a stochastic environment do not yield
optimal outcomes. Assessing the long-term advantage
of actions from optimisations (AO, dark blue) follows a
similar trend, whilst providing marginally superior sav-
ings relative to TO.
Optimisation-based learning using marginal rewards
(MO, purple) oﬀers the highest savings as the additional
baseline simulations are best able to isolate the con-
tribution of individual actions from variations caused
by both the environment and other agents. When in-
creasing the number of agents, the strategy is able
to learn from optimal, stable, consistently behaving
agents. Savings of 6.18p per agent per hour, or £45.11
per agent per month are obtained on average for 30
agents, corresponding to a 33.7% reduction from base-
line costs. 65.9% of savings stem from reduced battery
depreciation, 20.32% from distribution grid congestion,
11.1% from grid energy, and 2.7% from greenhouse gas
emissions.
The count-based strategy learning from optimisa-
tions (CO, light green) seeks to reproduce the state-
action patterns of the omniscient optimiser with per-
fect knowledge of system variables and perfect control
of agents for local decision-making under partial ob-
servability. It provides results lower than the high per-
formances of MO, though with a stable performance at
scale. Savings of £21.09 per agent per month on aver-
age for 30 agents are obtained. The battery and dis-
10


---

Page 11

---

tribution grid costs increase by an equivalent of 6.0%
and 7.7% of total savings respectively, while grid energy
and greenhouse gas emissions costs reductions represent
59.7% and 54.0% of total savings.
Both the MO and CO strategies exhibit stable per-
formance at scale, though converging to diﬀerent types
of policy. The MO policy saves more by smoothing out
the charging and distribution grid utilisation proﬁles
despite smaller savings in imports and emissions costs,
while CO derives a larger advantage from the grid price
diﬀerentials in grid imports, though with higher battery
and distribution grid costs. The weight applied to each
of those competing objectives in the objective function
directly impacts the policies that are learned. Examples
of how the individual home energy management sys-
tem decision variables (heating, energy consumption,
battery charging) vary based on the controller are illus-
trated in Appendix D.
Overall, the new class of optimisation-based learn-
ing performs signiﬁcantly better across diﬀerent num-
bers of prosumers, with higher savings and lower
inter-quartile range than environment-based learning
at scale.
This superior performance requires compu-
tations to run optimisations on historical data, and to
perform baseline simulations to compute marginal re-
wards, though computational time for pre-learning is
not strictly a limiting factor as it is performed oﬀ-line
ahead of implementation.
A fundamental challenge in MARL has been the
trade-oﬀbetween fully centralised value functions,
which are impractical for more than a handful of agents,
or, in a more straightforward approach, independent
learning of individual action-value functions by each
agent in independent Q-learning (IQL) [73]. However,
an ongoing issue with this approach has been that of
convergence at scale, as agents do not have explicit rep-
resentations of interactions between agents, and each
agent’s learning is confounded by the learning and ex-
ploration of others [74].
As shown in Figure 4, the
Pareto selection, non-stationarity and stochasticity is-
sues presented in Section 2 have prevented environ-
ment exploration-based learners from achieving success-
ful MARL cooperation at scale for agents under par-
tial observability in a stochastic environment.
This
case study of coordinated residential energy manage-
ment shows that the novel combination of marginal re-
wards, which help agents isolate their marginal contri-
bution to total rewards, and the learning from results
of convex optimisations, where agents learn successful
policy equilibriums from omniscient, stable, and consis-
tent solutions, oﬀer signiﬁcant improvements on these
scalability and convergence issues.
7. Conclusion
In this paper, a novel class of strategies has ad-
dressed the scalability issue of residential energy ﬂex-
ibility coordination in a cost-eﬃcient and privacy-
preserving manner. The combination of oﬀ-line opti-
misations with multi-agent reinforcement learning pro-
vides high, stable coordination performance at scale.
We identiﬁed in the literature that the concept of
RL-based implicit energy coordination, where energy
prosumers cooperate towards global objectives based
on local information only, had been under-researched
beyond frequency droop control with limited number
of agents. The scalability of such methods was identi-
ﬁed as a key gap that we have sought to bridge. The
novel coordination mechanism proposed in this paper
thus satisﬁes the criteria for successful residential en-
ergy coordination set out in the introduction, as tested
with large banks of real data in the case studies:
• Computational scalability: The scalability of tra-
ditional learning algorithms is signiﬁcantly im-
proved thanks to ﬁxed-size Q-tables to avoid the
curse of dimensionality, so that policies can be
learned for larger number of agents. The proposed
method does not require expensive communica-
tion and control appliances at the prosumer level,
as pre-learned policies are directly applied with no
further communication and no exponential time
real-time optimisations needed. This is a crucial
beneﬁt for applications with physical limitations
in hardware availability and processing time.
• Performance scalability:
The coordination per-
formance remains high for increasing numbers of
prosumers despite the challenges of partial ob-
servability, environment stochasticity and concur-
rently learning of agents, thanks to learning from
the results of global omniscient optimisations on
historical data, and to rewards signals that isolate
individual contributions to global rewards. Sig-
niﬁcant value of £45.11 per agent per month was
obtained in the presented case study for 30 agents,
thanks to savings in energy, prosumer storage and
societal greenhouse gas emissions-related costs.
Those savings do not drop with increasing num-
ber of agents, as opposed to with standard MARL
approaches.
• Acceptability:
The approach does not rely on
sharing of personal data, thermal discomfort,
or hindrance/delay of activities, and the appli-
ances are controlled locally.
This cost-eﬃcient
and privacy-preserving implicit coordination ap-
proach could help integrate distributed energy re-
sources such as residential energy, otherwise ex-
cluded from energy systems’ ﬂexibility manage-
ment.
Important future work is a more detailed assessment
of the impacts of the coordination strategies on power
ﬂows, as well as an evaluation of the generalisation and
adaptability potential of policies when used by other
households or if household characteristics change over
time. Moreover, while all agents readily reduce indi-
vidual costs through participation in the framework,
further game-theoretic tools could be used to design a
post-operation reward scheme.
11


---

Page 12

---

Acknowledgement
This work was supported by the Saven Euro-
pean Scholarship and by the UK Research and In-
novation and the Engineering and Physical Sciences
Research Council (award references EP/S000887/1,
EP/S031901/1, and EP/T028564/1).
References
[1] L. Matignon, G. Laurent, N. Le Fort-Piat, In-
dependent reinforcement learners in cooperative
Markov games: A survey regarding coordination
problems, Knowledge Engineering Review 27 (1)
(2012) 1–31. doi:10.1017/S0269888912000057.
[2] Masson-Delmotte, V., Global Warming of 1.5C.
An IPCC Special Report on the impacts of global
warming of 1.5C above pre-industrial levels and re-
lated global greenhouse gas emission pathways, in
the context of strengthening the global response to
the threat of climate change (2018).
[3] S. Bose, S. Low, Some Emerging Challenges in
Electricity Markets, in: Smart Grid Control, power
elec Edition, 2019, pp. 29–45.
doi:10.1007/
978-3-319-98310-3_2.
[4] T.-O. L´eautier, Imperfect Markets and Imperfect
Regulation:
An Introduction to the Microeco-
nomics and Political Economy of Power Markets,
MIT Press, 2019.
[5] J. V´azquez-Canteli, Z. Nagy, Reinforcement learn-
ing for demand response:
A review of algo-
rithms and modeling techniques, Applied Energy
235 (Oct 2018) (2019) 1072–1089. doi:10.1016/
j.apenergy.2018.11.002.
[6] K. Pumphrey, S. Walker, M. Andoni, V. Robu,
Green hope or red herring? Examining consumer
perceptions of peer-to-peer energy trading in the
United Kingdom, Energy Research and Social Sci-
ence 68 (September 2019) (2020) 101603.
doi:
10.1016/j.erss.2020.101603.
[7] Department for Business Energy and Industrial
Strategy, Energy consumption in the UK (2021).
[8] I. R. E. Agency, Renewable Power Generation
Costs in 2018, 2018. arXiv:arXiv:1011.1669v3,
doi:10.1007/SpringerReference_7300.
[9] BloomberNEF, 2019 Battery Price Survey (2019).
[10] Charles River Associates, An assessment of the
economic value of demand-side participation in the
Balancing Mechanism and an evaluation of options
to improve access (2017).
[11] T. Chen, W. Su, Indirect Customer-to-Customer
Energy Trading with Reinforcement Learning,
IEEE Transactions on Smart Grid 10 (4) (2019)
4338–4348. doi:10.1109/TSG.2018.2857449.
[12] D. Bugden, R. Stedman, A synthetic view of ac-
ceptance and engagement with smart meters in
the United States, Energy Research and Social
Science 47 (January 2018) (2019) 137–145. doi:
10.1016/j.erss.2018.08.025.
[13] F. Moret, P. Pinson, Energy Collectives: A Com-
munity and Fairness Based Approach to Future
Electricity Markets, IEEE Transactions on Power
Systems 34 (5) (2019) 3994–4004. doi:10.1109/
TPWRS.2018.2808961.
[14] S. Boyd, Convex optimization theory, Vol. 25,
2009.
URL http://citeseerx.ist.psu.edu/viewdoc/
download?rep=rep1&type=pdf&doi=10.1.1.
214.7707
[15] S. Dasgupta, Computer Science: A Very Short In-
troduction, Oxford University Press, 2016. doi:
10.1093/actrade/9780198733461.001.0001.
[16] B.
Recht,
A
tour
of
reinforcement
learn-
ing:
The
view
from
continuous
control,
arXiv
(2018).
arXiv:1806.09460,
doi:
10.1146/annurev-control-053018-023825.
[17] V. Fran¸cois Lavet, Contributions to deep reinforce-
ment learning and its applications in smartgrids
(2017).
[18] S. Sen, M. Sekaran, J. Hale, Learning to coordi-
nate without sharing information, Proceedings of
the National Conference on Artiﬁcial Intelligence
1 (1994) 426–431.
[19] F. Ruelens, Residential Demand Response of Ther-
mostatically Controlled Loads Using Batch Rein-
forcement Learning, IEEE Transactions on Smart
Grid 8 (5) (2017) 2149–2159. doi:10.1109/TSG.
2016.2517211.
[20] M. Wooldridge, Intelligent Agents: The Key Con-
cepts, Springer Berlin Heidelberg, Berlin, Heidel-
berg, 2002.
[21] T. Morstyn, N. Farrell, S. Darby, M. McCul-
loch, Using peer-to-peer energy-trading platforms
to incentivize prosumers to form federated power
plants, Nat Energy 3 (2) (2018) 94–101.
[22] R. S. Sutton, A. G. Barto, Reinforcement learning
: an introduction [electronic resource], Adaptive
computation and machine learning, MIT Press,
Cambridge, Mass., 1998.
[23] I. Antonopoulos, Artiﬁcial intelligence and ma-
chine learning approaches to energy demand-side
response:
A systematic review, Renewable and
Sustainable Energy Reviews 130 (April) (2020)
109899. doi:10.1016/j.rser.2020.109899.
[24] C. Schellenberg, J. Lohan, L. Dimache, Compari-
son of metaheuristic optimisation methods for grid-
edge technology that leverages heat pumps and
12


---

Page 13

---

thermal energy storage, Renewable and Sustain-
able Energy Reviews 131 (June) (2020) 109966.
doi:10.1016/j.rser.2020.109966.
URL
https://doi.org/10.1016/j.rser.2020.
109966
[25] F. Charbonnier, T. Morstyn, M. McCulloch, Co-
ordination of resources at the edge of the electric-
ity grid: systematic review and taxonomy (2022).
arXiv:2202.03786.
[26] D. O’Neill, M. Levorato, A. Goldsmith, U. Mi-
tra, Residential Demand Response Using Rein-
forcement Learning, 2010 First IEEE International
Conference on Smart Grid Communications (2010)
409–414doi:10.1109/smartgrid.2010.5622078.
[27] S. J. Darby, Demand response and smart tech-
nology in theory and practice: Customer experi-
ences and system actors, Energy Policy 143 (April)
(2020)
111573.
doi:10.1016/j.enpol.2020.
111573.
URL https://doi.org/10.1016/j.enpol.2020.
111573
[28] W. Powell, Approximate dynamic programming:
solving the curses of dimensionality, 2nd Edition,
Wiley series in probability and statistics, J. Wiley
& Sons, Hoboken, N.J., 2011.
[29] R. Lu, S. H. Hong, Incentive-based demand re-
sponse for smart grid with reinforcement learning
and deep neural network, Applied Energy 236 (De-
cember 2018) (2019) 937–949.
doi:10.1016/j.
apenergy.2018.12.061.
[30] B. Kim, Y. Zhang, M. Van Der Schaar, J. Lee, Dy-
namic Pricing and Energy Consumption Schedul-
ing With Reinforcement Learning, IEEE Transac-
tions on Smart Grid 7 (5) (2016) 2187–2198.
[31] M. Babar, P. H. Nguyen, V. Cuk, I. G. Kamphuis,
M. Bongaerts, Z. Hanzelka, The evaluation of agile
demand response: An applied methodology, IEEE
Transactions on Smart Grid 9 (6) (2018) 6118–
6127. doi:10.1109/TSG.2017.2703643.
[32] M. G. Vay´a, L. B. Rosell´o, G. Andersson, Opti-
mal bidding of plug-in electric vehicles in a market-
based control setup, Proceedings - 2014 Power Sys-
tems Computation Conference, PSCC 2014 (2014).
doi:10.1109/PSCC.2014.7038108.
[33] Y. Ye, D. Qiu, M. Sun, D. Papadaskalopou-
los, G. Strbac, Deep Reinforcement Learning for
Strategic Bidding in Electricity Markets, IEEE
Transactions on Smart Grid 11 (2) (2020) 1343–
1355. doi:10.1109/TSG.2019.2936142.
[34] D. Dauer, C. M. Flath, P. Str¨ohle, C. Weinhardt,
Market-based EV charging coordination, Proceed-
ings - 2013 IEEE/WIC/ACM International Con-
ference on Intelligent Agent Technology, IAT 2013
2 (2013) 102–107. doi:10.1109/WI-IAT.2013.97.
[35] Y. Sun, A. Somani, T. Carroll, Learning based bid-
ding strategy for HVAC systems in double auction
retail energy markets, Proceedings of the American
Control Conference 2015-July (2015) 2912–2917.
doi:10.1109/ACC.2015.7171177.
[36] J. G. Kim, B. Lee, Automatic P2P energy trad-
ing model based on reinforcement learning using
long short-term delayed reward, Energies 13 (20)
(2020). doi:10.3390/en13205359.
[37] B. J. Claessens, S. Vandael, F. Ruelens, K. De
Craemer, B. Beusen, Peak shaving of a heteroge-
neous cluster of residential ﬂexibility carriers using
reinforcement learning, 2013 4th IEEE/PES Inno-
vative Smart Grid Technologies Europe, ISGT Eu-
rope 2013 (2013) 1–5doi:10.1109/ISGTEurope.
2013.6695254.
[38] X. Zhang, T. Bao, T. Yu, B. Yang, C. Han, Deep
transfer Q-learning with virtual leader-follower for
supply-demand Stackelberg game of smart grid,
Energy 133 (2017) 348–365.
doi:10.1016/j.
energy.2017.05.114.
[39] I. Dusparic, Maximizing renewable energy use
with decentralized residential demand response,
2015 IEEE 1st International Smart Cities Confer-
ence, ISC2 2015 (2015). doi:10.1109/ISC2.2015.
7366212.
[40] I. Dusparic, Multi-agent residential demand re-
sponse
based
on
load
forecasting,
2013
1st
IEEE Conference on Technologies for Sustain-
ability, SusTech 2013 (2013) 90–96doi:10.1109/
SusTech.2013.6617303.
[41] L.
A.
Hurtado,
E.
Mocanu,
P.
H.
Nguyen,
M. Gibescu, R. I. Kamphuis, Enabling Cooperative
Behavior for Building Demand Response Based on
Extended Joint Action Learning, IEEE Transac-
tions on Industrial Informatics 14 (1) (2018) 127–
136. doi:10.1109/TII.2017.2753408.
[42] T. Morstyn,
M. Mcculloch,
Peer-to-Peer En-
ergy Trading, Analytics for the Sharing Econ-
omy:
Mathematics, Engineering and Business
Perspectives
(March)
(2020).
doi:10.1007/
978-3-030-35032-1.
[43] A.
Taylor,
Accelerating
Learning
in
multi-
objective systems through Transfer Learning, Pro-
ceedings of the International Joint Conference on
Neural Networks (2014) 2298–2305doi:10.1109/
IJCNN.2014.6889438.
[44] S. Herbert, Models of bounded rationality, MIT
Press, Cambridge, Mass. ; London, 1982.
[45] J. Guerrero, D. Gebbran, S. Mhanna, A. C. Chap-
man, G. Verbiˇc, Towards a transactive energy sys-
tem for integration of distributed energy resources:
Home energy management, distributed optimal
power ﬂow, and peer-to-peer energy trading, Re-
newable & sustainable energy reviews 132 (2020).
13


---

Page 14

---

[46] J. Cao, Deep Reinforcement Learning Based En-
ergy Storage Arbitrage With Accurate Lithium-ion
Battery Degradation Model, IEEE Transactions on
Smart Grid 14 (8) (2019) 1–9.
[47] Y. Yang, J. Hao, Y. Zheng, C. Yu, Large-Scale
Home Energy Management Using Entropy-Based
Collective Multiagent Deep Reinforcement Learn-
ing Framework (2019) 630–636.
[48] C. Crozier, D. Apostolopoulou, M. McCulloch,
Mitigating the impact of personal vehicle electri-
ﬁcation: A power generation perspective, Energy
Policy 118 (2013) (2018) 474–481. doi:10.1016/
j.enpol.2018.03.056.
[49] S. Rozada, D. Apostolopoulou, E. Alonso, Load
frequency control: A deep multi-agent reinforce-
ment learning approach, IEEE Power and Energy
Society General Meeting 2020-August (2020) 0–4.
doi:10.1109/PESGM41954.2020.9281614.
[50] L. Kraemer, B. Banerjee, Multi-agent reinforce-
ment learning as a rehearsal for decentralized plan-
ning, Neurocomputing 190 (2016) 82–94.
doi:
10.1016/j.neucom.2016.01.031.
[51] L. Bu¸soniu,
R. Babuˇska,
B. De Schutter,
A
comprehensive survey of multiagent reinforcement
learning, IEEE Transactions on Systems, Man and
Cybernetics Part C: Applications and Reviews
38 (2) (2008) 156–172. doi:10.1109/TSMCC.2007.
913919.
[52] M. Parry, Climate change 2007: impacts, adap-
tation and vulnerability, Published for the Inter-
governmental Panel on Climate Change [by] Cam-
bridge University Press, Cambridge, 2007.
[53] T. Morstyn, M. McCulloch, Multiclass Energy
Management for Peer-to-Peer Energy Trading
Driven by Prosumer Preferences, IEEE Transac-
tions on Power Systems 34 (5) (2019) 4005–4014.
doi:10.1109/TPWRS.2018.2834472.
[54] C. Coﬀrin, P. Van Hentenryck, R. Bent, Approxi-
mating line losses and apparent power in AC power
ﬂow linearizations, IEEE Power and Energy So-
ciety General Meeting (2012) 1–8doi:10.1109/
PESGM.2012.6345342.
[55] T. Morstyn, A. Teytelboym, C. Hepburn, M. Mc-
Culloch, Integrating P2P Energy Trading with
Probabilistic
Distribution
Locational
Marginal
Pricing,
IEEE
Transactions
on
Smart
Grid
11 (4) (2020) 3095–3106. doi:10.1109/TSG.2019.
2963238.
[56] R. Dufo-L´opez, J. M. Lujano-Rojas, J. L. Bernal-
Agust´ın, Comparison of diﬀerent lead–acid battery
lifetime prediction models for use in simulation of
stand-alone photovoltaic systems, Applied energy
115 (2014) 242–253.
[57] ISO, Calculation of Energy Use for Space Heating
and Cooling ISO/FDIS 13790:2007(E) (2007).
[58] O. Sachs, Field Evaluation of Programmable Ther-
mostats (2012).
[59] L. Matignon, G. J. Laurent, N. Le Fort-piat,
Hysteretic Q-Learning : an algorithm for Decen-
tralized Reinforcement Learning in Cooperative
Multi-Agent Teams ., in: Proceedings of the 2007
IEEE/RSJ International Conference on Intelligent
Robots and Systems, IEEE, 2007, pp. 64–69.
[60] O. Vinyals, Grandmaster level in StarCraft II
using multi-agent reinforcement learning,
Na-
ture 575 (November) (2019).
doi:10.1038/
s41586-019-1724-z.
[61] D. Wolpert,
K. Tumer,
Optimal payoﬀfunc-
tions for members of collectives, Advances in
Complex Systems 04 (03 2002).
doi:10.1142/
S0219525901000188.
[62] J.
N.
Foerster,
G.
Farquhar,
T.
Afouras,
N. Nardelli, S. Whiteson, Counterfactual multi-
agent policy gradients, 32nd AAAI Conference on
Artiﬁcial Intelligence, AAAI 2018 (2018) 2974–
2982arXiv:1705.08926.
[63] R. Wardle, Dataset (TC1a): Basic Proﬁling of Do-
mestic Smart Meter Customers (2014).
[64] R. Wardle, Dataset (TC5):
Enhanced Proﬁling
of Domestic Customers with Solar Photovoltaics
(PV) (2014).
[65] Department for Transport, National Travel Sur-
vey 2002-2017 (2019). doi:http://doi.org/10.
5255/UKDA-SN-5340-10.
[66] C. Crozier, D. Apostolopoulou, M. McCulloch,
Numerical analysis of national travel data to
assess the impact of UK ﬂeet electriﬁcation,
20th Power Systems Computation Conference,
PSCC 2018 (2018) 1–7arXiv:1711.01440, doi:
10.23919/PSCC.2018.8450584.
[67] S.
Lloyd,
Least
squares
quantization
in
PCM,
IEEE
Transactions
on
Infor-
mation
Theory
28
(2)
(1982)
129–137.
doi:10.1109/TIT.1982.1056489.
[68] D. Hirst, Commons Brieﬁng Paper SNO5927: Car-
bon Price Floor (CPF) and the price support
mechanism (2018).
[69] Weather Wunderground,
London City Airport
weather history (2020).
[70] Octopus Energy, Octopus Energy API (2019).
[71] National Grid ESO, Environmental Defense Fund
Europe,
University of Oxford Department of
Computer Science, WWF, Carbon Intensity API
(2020).
[72] J. Brown, J. Chambers, A. Rogers, SMITE : Us-
ing Smart Meters to Infer the Thermal Eﬃciency of
Residential Homes, in: The 7th ACM International
14


---

Page 15

---

Conference on Systems for Energy- Eﬃcient Build-
ings, Cities, and Transportation (BuildSys ’20),
2020.
[73] M. Tan, Multi-Agent Reinforcement Learning : In-
dependent vs . Cooperative Agents (1993).
[74] T. Rashid, G. Farquhar, B. Peng, S. White-
son, Weighted QMIX: Expanding monotonic value
function factorisation for deep multi-agent rein-
forcement learning, Advances in Neural Informa-
tion Processing Systems 2020-December (2020).
arXiv:2006.10800.
[75] HOMER Energy, HOMER Pro 3.14 User Manual
(2020).
[76] W. Schram, Empirical evaluation of V2G round-
trip eﬃciency, SEST 2020 - 3rd International Con-
ference on Smart Energy Systems and Technolo-
gies (October) (2020). doi:10.1109/SEST48500.
2020.9203459.
[77] V.
Becker,
W.
Kleiminger,
V.
Coroam˘a,
F.
Mattern,
Estimating
the
savings
po-
tential
of
occupancy-based
heating
strate-
gies,
Energy
Informatics
1
(S1)
(2018).
doi:10.1186/s42162-018-0022-6.
[78] BRE, SAP 2012 9.92 The Government’s Stan-
dard Assessment Procedure for Energy Rating of
Dwellings (2014). arXiv:9809069v1.
[79] British Standards, Heating systems in buildings.
Method for calculation of the design heat load, Ics
91.140.10 (January) (2009) 1–89.
15


---

Page 16

---

Appendix A
Nomenclature
Acronyms
AE
MARL with advantage rewards and exploration-based learning
AO
MARL using advantage rewards and optimisation-based learning
AI
artiﬁcial intelligence
CLNR
customer-led network revolution
CO
MARL using count rewards and optimisation-based learning
ME
MARL using marginal rewards and exploration-based learning
MO
MARL using marginal rewards and optimisation-based learning
Dec-POMDP
decentralised partially observable Markov decision process
DER
distributed energy resource
DR
demand response
EV
electric vehicle
MARL
multi-agent reinforcement learning
NTS
national travel survey
PV
photovoltaic
RL
reinforcement learning
TE
MARL using total rewards and exploration-based learning
TO
MARL using total rewards and optimisation-based learning
UK
United Kingdom
Variables
bin
charge into the battery [kWh]
bin
maximum charge into the battery [kWh]
bout
discharge out of the battery [kWh]
c
household consumption [kWh]
ˆc
partial consumption for load type and time demanded [kWh]
cd
distribution cost [£]
Cd
distribution charge [£/kWh]
cg
grid cost [£]
Cg
grid cost coeﬃcient [£/kWh]
cs
storage cost [£]
Cs
battery depreciation coeﬃcient [£/kWh]
d
household demand [kWh]
dEV
electric vehicle demand [kWh]
dﬁxed
sum of non-ﬂexible household and heating loads [kWh]
dtot
sum of household all heating loads [kWh]
E
battery energy level [kWh]
E0
initial battery energy level [kWh]
E
minimum battery energy level [kWh]
E
maximum battery energy level [kWh]
f
ﬂexibility boolean
F
objective function [£]
ˆF
share of objective function for given time step
g
total grid import to the group of prosumers [kWh]
h
heating energy consumption [kWh]
k
behaviour cluster for transport or household consumption proﬁle
p
prosumer import [kWh]
pPV
PV generation [kWh]
Q
Q value [£]
ˆQ
Q value estimate [£]
r
global reward [£]
R
average resistance between the main grid and the prosumers [Ω]
Te
external temperature [oC]
Tm
building mass temperature [oC]
Tair
indoor air temperature [oC]
T
minimum indoor air temperature [oC]
T
maximum indoor air temperature [oC]
U
uniform distribution function
16


---

Page 17

---

V
nominal root mean square grid voltage [V]
ˆV
state-value estimate [£]
Greek letters
α0
base learning rate [-]
α
learning rate [-]
β
hysteretic learning rate reduction factor [-]
γ
discount factor [-]
δ
loss [£]
ϵch
battery charging losses [kWh]
ϵdis
battery discharging losses [kWh]
ϵ
share of random action selection during exploration [-]
ηch
battery charging eﬃciency [-]
ηdis
battery discharging eﬃciency [-]
κ
matrix of heating model coeﬃcients
λ
scaling factor for transport or household consumption proﬁle [kWh]
µ
electric vehicle availability boolean
π
policy
φ
solar heat ﬂow rate [J.s−1]
ψ
local ﬂexibility use decision variable [-]
Indexes
a
action
i
prosumer
s
state
t
time step
tC
consumption time step
tD
demand time step
w
day type (week day or weekend day)
Sets
A
set of actions
T
set of time steps
P
set of prosumers
S
set of states
Table 2: Nomenclature
17


---

Page 18

---

Appendix B
Case study input data
• Learning parameters: The depreciation, learning and exploration rates are γ = 0.99, α0 = 0.01 and ϵ =
0.5. The hysteretic learning rate reduction parameter for negative errors is β = 0.5. The states are deﬁned
by three uniform grid cost intervals for each day. The action space is discretised in 10 equal ψ intervals.
• Battery: ηch = ηdis = √ηround trip [75], where ηround trip = 0.87 [76], capacity E = 75 kWh, max. charging
rate bin = 22 kW, depreciation Cs = 20 USD/MWh-throughput [53], initial and min. charge E0 = 0.5E
and E = 0.1E.
• Grid: nominal voltage V = 415 [V], average resistance to prosumers R = 0.084 [Ω] [53].
• Flexible loads: 10% deferrable for up to nﬂex = 5 hours.
• Heating: housing of 76 m2, 2.4m height. Comfort temperature 20oC between 7-10am and 5-10pm, setback
16oC. Variations of 3oC acceptable. U-values from [77], other heating inputs from [57, 78, 79]. Pre-heating
up to ﬁve hours in advance. Coeﬃcients after re-arranging:
κ =
6.84e−2, 9.08e−1, 9.15e−2, 2.62e−4, 2.52e−1
2.40e−1, 8.80e−1, 1.20e−1, 3.46e−4, 1.46

(29)
• EV consumption factors [kWh/10km]: 2.25 for motorway, 1.62 for urban and 1.36 for rural travel [66].
• Distribution network export charge: 0.01 £/kWh
18


---

Page 19

---

Appendix C
Heating model
We use the simple hourly method heating model laid out in [57].
The input data used in the heating model in this paper is tabulated below. Note that these heating model
and input data are meant as a generic building example that can be used to test the relative performances of
the MARL coordination algorithms in the case study in Section 6. Models and parameters used for the detailed
study of a speciﬁc building should be validated with experimental data.
Symbol
Deﬁnition
Value
Unit
Reference
Ad
door area
1.4 × 2
m2
Af
ﬂoor area
76
m2
Awd
window area
1.4×1.4
m2
e
shielding coeﬃcient
0.03
-
[79]
h
height of rooms
2.4
m
his
heat transfer coeﬃcient between the
air node θair and the surface node θs
3.45
W.m−2.K−1
[57]
hms
heat
transfer
coeﬃcient
between
nodes m and s
9.1
W.m−2.K−1
[57]
kparty
fraction of ﬂoor space that is party
ﬂoor rather than on ground, for one-
storey building
0.5
[-]
nmin
minimum external air exchange rate
per hour for a habitable room
0.5
h−1
[79]
n50
Air exchange rate resulting from a
pressure diﬀerence of 50 Pa between
the inside and the outside of the
building, including the eﬀects of air
inlets, medium construction family
dwelling
6
h−1
[79]
Ug
U-value for ground (old build)
1.0
W.m−2.K−1
[77]
Ur
U-value for roof (old build)
1.0
W.m−2.K−1
[77]
Uw
U-value for walls, ceiling against
outside (old build)
1.5
W.m−2.K−1
[77]
Uwd
U-value for windows (old build)
4.3
W.m−2.K−1
[77]
ϵ
height correction factor
1
-
[79]
Λat
dimensionless ratio between the in-
ternal surfaces area and the ﬂoor
area
4.5
[-]
[57]
τ
time step
3600
s
Table 3: Input parameters to the heating model
We obtain the following intermediate parameter values:
• Eﬀective mass area Am [m2] for a medium-class building [57]:
Am = 2.5Af
(30)
• Internal heat capacity of the building zone for medium-class building J.K−1 [57]:
Cm = 165, 000Af
(31)
• Area of all surfaces facing the building zone Atot [m2] [57]:
Atot = ΛatAf
(32)
• The coupling conductance [W.K−1] [57]:
Htr,is = hisAtot
(33)
• The coupling conductance between nodes m and s [W.K−1] [57]:
Htr,ms = hmsAm
(34)
19


---

Page 20

---

• Wall area (excluding windows and doors)
Aw = 4
p
Afh −8Awd −Ad
(35)
• The thermal transmission coeﬃcient of walls [W.K−1] [57]:
Htr,w = AwUw
(36)
• The thermal transmission coeﬃcienf of the roof [W.K−1] [57]:
Htr,r = AfUr
(37)
• The thermal transmission coeﬃcient of the ﬂoor [W.K−1] [57]:
Htr,f = Af(1 −kparty)Ug
(38)
• The heat transfer coeﬃcient for opaque elements Htr,op [W.K−1] [57]:
Htr,op = Htr,w + Htr,r + Htr,f
(39)
• The opaque heat transfer coeﬃcient is split between conductance transfer and Htr,em [57]:
Htr,em =
1
1
Htr,op −
1
Htr,ms
(40)
• The thermal transmission coeﬃcienf of windows [W.K−1] [57]:
Htr,wd = (Awd + Ad)Uwd,eﬀ
(41)
• The conditioned air volume [m3]
Vr = Afh
(42)
• The hygiene minimuim air ﬂow rate of a heated space Vmin [m3.h−1] [79]:
Vmin = nminVr
(43)
• The inﬁltration through building envelope Vinf [m3.h−1] [79]:
Vinf = 2Vrn50eϵ
(44)
• The air ﬂow rate of heated space [m3.h−1] [79]:
V = max(Vmin, Vinf)
(45)
• The heat transfer by ventilation Hve [W.K−1] [79]:
Hve = 0, 34V
(46)
• The eﬀective window U-value, corrected for the assumed use of curtains [W.m−2.K−1] [57]:
Uwd,eﬀ=
1
1
Uwd + 0.04
(47)
• Three helper transmission coeﬃcients [57]:
Htr,1 =
1
1
Hve +
1
Htr,is
(48)
Htr,2 = Htr,1 + Htr,w
(49)
Htr,3 =
1
1
Htr,2 +
1
Htr,ms
(50)
20


---

Page 21

---

• The heat ﬂow rate from internal heat sources Φint [W] is taken as the sum of the average heat ﬂow rate
from appliances Φint,A and occupants Φint,OC [57]:
Φint = Φint,A + Φint,OC = 2Af + 1.5Af = 3.5Af
(51)
• the part of the heat ﬂow rate from internal heat sources going to the air node θint Φia [W] [57]
Φia = 1
2Φint
(52)
Given these input parameters, the Crank-Nicholson scheme is deﬁned in [57] is applied. We seek to ﬁnd the
temperature of the internal air node θair [oC] and of the building mass θm,t at each time step given the heating
or cooling power ΦHC (positive for heating and negative for cooling), the external air temperature θe [oC] and
the heat ﬂow rates from solar heat sources Φsol.
The air node temperature θair is given as
θair = Htr,isθs + Hveθsup + Φia + ΦHC
Htr,is + Hve
(53)
Where the surface node temperature θs is deﬁned as:
θs =
Htr,msθm + Φst + Htr,wθe + Htr,1

θsup + Φia+ΦHC
Hve

Htr,ms + Htr,w + Htr,1
(54)
The average temperature over the hour of the building mass θm:
θm = 1
2(θm,t-1 + θm,t)
(55)
θm,t = θm,t-1
  Cm
τ + 1
2(H3 + Htr,em)

+ Φmtot
Cm
τ + 1
2(Htr,3 + Htr,em)
(56)
Φmtot = Φm + Htr,emθe + Htr,3
Φst + Htr,wθe + Htr,1

Φia+ΦHC
Hve
+ θsup

Htr,2
(57)
The part of heat ﬂow rates from internal and solar heat sources going to the internal nodes θs
Φst =

1 −Am
At
−Htr,w
9.1At
 1
2Φint + Φsol

(58)
The part of heat ﬂow rates from internal and solar heat sources going to the internal nodes θm
Φm = Am
At
1
2Φint + Φsol

(59)
θsup = θe
(60)
We rearrange the equations of this model in order to obtain a linear recursive formulation. We ﬁrst deﬁne
some helper variables:
A = Cm
τ
+ 1
2(Htr,3 + Htr,em)
(61)
B = 1 −Am
At
−Htr,w
9.1At
(62)
C = BΦint
2
(63)
D = AmΦint
2At
+ Htr,3
Htr,2

C + Htr,1Φia
Hve

(64)
E = Htr,em + Htr,3
Htr,2
(Htr,w + Htr,1)
(65)
Htr,ms + Htr,w + Htr,1
(66)
21


---

Page 22

---

G = 1
F
Htr,msaT
2
+ C + Htr,1Φia
Hve

(67)
H = Htr,ms
2F
(1 + bT)
(68)
I = 1
F
Htr,mscT
2
+ Htr,w + Htr,1

(69)
J = 1
F
Htr,msdT
2
+ B

(70)
K = 1
F
Htr,mseT
2
+ Htr,1
Hve

(71)
aT = D
A
(72)
bT =
  Cm
τ + 0.5(H3 + Htr,em)

A
(73)
cT = E
A
(74)
dT =
Am
At + Htr,3B
Htr,2
A
(75)
eT = Htr,3Htr,1
Htr,2HveA
(76)
aair = Htr,isG + Φia
Htr,is + Hve
(77)
bair =
Htr,isH
Htr,is + Hve
(78)
cair = Htr,isI + Hve
Htr,is + Hve
(79)
dair =
Htr,isJ
Htr,is + Hve
(80)
eair = Htr,isK + 1
Htr,is + Hve
(81)
κ =
 aT
bT
cT
dT
eT
aair
bair
cair
dair
eair

(82)
Rearranging eqs. (58), (62) and (63):
Φst = C + BΦsol
(83)
Rearranging eqs. (57), (59), (60) and (83):
Φmtot =
 Am
2At
Φint + Am
At
Φsol

+ Htr,emθe + Htr,3
Htr,2
(C + BΦsol) +
Htr,3
Htr,2
Htr,wθe + Htr,3
Htr,2
Htr,1
Φia + ΦHC
Hve
+ (θe)

(84)
Φmtot = AmΦint
2At
+ Am
At
Φsol + Htr,emθe + Htr,3C
Htr,2
+ Htr,3B
Htr,2
Φsol + Htr,3Htr,w
Htr,2
θe+
Htr,3Htr,1Φia
Htr,2Hve
+ Htr,3Htr,1
Htr,2Hve
ΦHC + Htr,3Htr,1
Htr,2
θe
(85)
22


---

Page 23

---

Φmtot =
AmΦint
2At
+ Htr,3
Htr,2

C + Htr,1Φia
Hve

+
Am
At
+ Htr,3B
Htr,2

Φsol
+

Htr,em + Htr,3
Htr,2
(Htr,w + Htr,1)

θe + Htr,3Htr,1
Htr,2Hve
ΦHC
(86)
Rearranging eqs. (64), (65) and (86):
Φmtot = D +
Am
At
+ Htr,3B
Htr,2

Φsol + Eθe + Htr,3Htr,1
Htr,2Hve
ΦHC
(87)
From eqs. (56) and (61)
θm,t =
  Cm
τ + 0.5(H3 + Htr,em)

A
θm,t-1 + Φmtot
A
(88)
From eqs. (87) and (88)
θm,t = D
A +
Cm
τ + 0.5(H3 + Htr,em)
A
θm,t-1 + E
Aθe +
Am
At + Htr,3B
Htr,2
A
Φsol+
Htr,3Htr,1
Htr,2HveAΦHC
(89)
From eqs. (72) to (76) and (89):
θm,t = aT + bTθm,t-1 + cTθe + dTΦsol + eTΦHC
(90)
From eqs. (55) and (90):
θm = 1
2 (θm,t-1 + aT + bTθm,t-1 + cTθe + dTΦsol + eTΦHC)
(91)
θm = aT
2 + 1 + bT
2
θm,t-1 + cT
2 θe + dT
2 Φsol + eT
2 ΦHC
(92)
From eqs. (54), (60), (66), (83) and (92)
θs = Htr,msaT
2F
+ Htr,ms
F
1 + bT
2
θm,t-1 + Htr,mscT
2F
θe + Htr,msdT
2F
Φsol+
Htr,mseT
2F
ΦHC + C
F + B
F Φsol + Htr,w
F
θe + Htr,1
F
θe + Htr,1Φia
FHve
+ Htr,1
FHve
ΦHC
(93)
θs = 1
F
Htr,msaT
2
+ C + Htr,1Φia
Hve

+ Htr,ms
2F
(1 + bT)θm,t-1+
1
F
Htr,mscT
2
+ Htr,w + Htr,1

θe+
1
F
Htr,msdT
2
+ B

Φsol + 1
F
Htr,mseT
2
+ Htr,1
Hve

ΦHC
(94)
From eqs. (67) to (71) and (94):
θs = G + Hθm,t-1 + Iθe + JΦsol + KΦHC
(95)
From eqs. (53), (60) and (95):
θair =
Htr,isG
Htr,is + Hve
+
Htr,isH
Htr,is + Hve
θm,t-1 +
Htr,isI
Htr,is + Hve
θe +
Htr,isJ
Htr,is + Hve
Φsol+
Htr,isK
Htr,is + Hve
ΦHC +
Hve
Htr,is + Hve
θe +
Φia
Htr,is + Hve
+
1
Htr,is + Hve
ΦHC
(96)
θair = Htr,isG + Φia
Htr,is + Hve
+
Htr,isH
Htr,is + Hve
θm,t-1 + Htr,isI + Hve
Htr,is + Hve
θe +
Htr,isJ
Htr,is + Hve
Φsol+
Htr,isK + 1
Htr,is + Hve
ΦHC
(97)
23


---

Page 24

---

From eqs. (77) to (81) and (97):
θair = aair + bairθm,t-1 + cairθe + dairΦsol + eairΦHC
(98)
Note that the notation from [57] was used in this appendix.
In this paper, T t+1
air,i ←θair, T t+1
m,i
←θm,t,
T t
m,i ←θm,t-1, T t
e ←θe, Φt ←Φsol, ht
i ←ΦHC, such that from eqs. (82), (90) and (98):
T t+1
m,i
T t+1
air,i

= κ
1, T t
m,i, Tt
e, φt, ht
i
⊺
(99)
This is equivalent to eq. (15).
24


---

Page 25

---

Appendix D
Residential energy management: commented illustrative day
Here we look in detail at the actions selected by an agent which learned to coordinate using diﬀerent MARL
strategies. This is meant to illustrate how example RL ψ actions translate into local energy management system
behaviour. Note however that the MARL algorithms aim to generate statistically favourable outcomes when
averaged over longer durations and over larger number of agents.
As such, while the average outcomes are
predictable, as described in Section 6, this individual case is not meant to be generally representative but rather
simply an example day in a stochastic environment.
Figure 5 shows an example of an evaluation day during which the ﬁnal policies learned is used deterministically
on a day-long batch of data. Four diﬀerent policies are compared:
• Baseline: no ﬂexibility used
• Optimal: the actions selected by a central optimiser with perfect knowledge and control of all current and
future variables
• CO: a policy seeking to replicate action patterns by the optimiser by counting the number of actions taken
for each grid coeﬃcient level (state) during pre-learning (see Section 4)
• MO: learning from optimisations and using marginal rewards (see Section 4)
The baseline and optimal act as reference points while the two latter policies have been identiﬁed in Section 6
as scalable policies when the number of agents increases. While both policies reduce costs relative to the baseline
on average at scale, MO was shown to be the best-performing policy at scale.
Subplot A shows the wholesale prices and the grid carbon intensity for the example day, as well as the resulting
grid cost coeﬃcient Cg given a social cost of carbon of 70 £/tCO2. This coeﬃcient informs the choice of action
ψ.
Subplot B shows the action ψ selected by each policy over time. The CO policy seeks to imitate patterns by
the optimiser – though with more limited information than is available to the optimiser – and takes more extreme
actions, for example with maximum delaying of consumption (ψ = 0) at time intervals with high network cost
coeﬃcient Ct
g, whereas the MO policy selects intermediate ψ values.
Subplot C shows the total energy consumption over time. This includes both household loads and heating
consumption. MO takes intermediate ψ actions and so follows more closely the baseline, non-ﬂexible consump-
tion proﬁle than CO which delays more loads when taking lower ψ values. Both strategies are seen to shave
consumption peaks and/or displace them to lower-price time intervals. As the total household electric demand
is ﬁxed, displacing consumption does not increase total consumption. However, variation in heating loads within
the acceptable temperature bounds may increase overall consumption. Thus, in this example day the MO strat-
egy consumes more 26.1% more energy than the baseline, though overall incurring lower costs and greenhouse
gas emissions.
Subplot D shows cumulative rewards over time each of the policies. While the CO strategy was seen to
take advantage more closely of grid price diﬀerentials, overall the costs incurred are higher than with the MO
strategy. With the MO strategy, savings of £1.20 are obtained compared to the baseline over the example day,
corresponding to a 57.5% reduction from baseline costs. 86.3% of savings stem from reduced battery depreciation,
22.3% from reduced distribution grid congestion, while grid energy costs increased by 8.6%. In this example day
the CO strategy achieved savings of £0.76, with 66.1% stemming from reduced grid energy costs, 30.0% from
reduced battery costs, and 3.9% from reduced grid congestion.
An interplay is thus illustrated by the two policies between the costs of battery depreciation and distribution
network congestion on the one hand, and the opportunity for energy arbitrage to save on grid energy and emissions
costs on the other. Both the MO and CO strategies exhibit stable performance at scale, though converging to
diﬀerent types of policy. The MO policy saves more by smoothing out the charging and distribution grid utilisation
proﬁles despite smaller savings in imports and emissions costs, while CO derives a larger advantage from the grid
price diﬀerentials in grid imports, though with higher battery and distribution grid costs. The weight applied
on each of those competing objectives in the objective function will have a direct impact on the policies that are
learned.
Subplot E shows the heating energy proﬁle, resulting in the temperatures in subplot F. The baseline proﬁle
maintains the median desired temperature, whereas the ﬂexible policies can go above or below that median,
within the desired temperature bounds. Both policies are more likely to absorb energy imports through heating
(no marginal costs) rather than storage (battery depreciation costs) relative to the baseline policy. Consumption
peaks are shaved or displaced to lower-cost time intervals with both policies.
Subplot G shows the EV at-home availability and consumption. In this example day, the electric vehicle (EV)
leaves home at 9 am, consumes 2.2 kWh on an outbound trip, remains parked at its destination for 1 hour, and
consumes 2.2 kWh on the inbound trip back to the home at 12 pm. The car can therefore not be charged during
this time interval, and enough charge has to be available beforehand for these travelling loads.
25


---

Page 26

---

0
5
10
15
20
0.02
0.04
0.06
0.08
Grid price [£/kWh]
A
Wholesale
Cg
0
5
10
15
20
0
2
4
Heating [kWh]
E
0
5
10
15
20
0.00
0.25
0.50
0.75
1.00
Action variable  [-]
B
0
5
10
15
20
14
16
18
20
22
Indoor air temperature [oC]
F
0
5
10
15
20
0
2
4
6
Total consumption [kWh]
C
0
5
10
15
20
0.0
0.5
1.0
1.5
2.0
EV load [kWh]
G
EV unavailable
0
5
10
15
20
Time [h]
4
2
0
2
4
Cumulative rewards [£]
D
baseline
optimal
CO
MO
0
5
10
15
20
Time [h]
0
20
40
60
Battery level [kWh]
H
0.4
0.5
0.6
0.7
Carbon intensity [kgCO2/kWh]
Figure 5: Example of local home energy system variables for one agent using diﬀerent policies learned ahead of implementation
(optimisation-based learning using marginal rewards (MO) and optimiser state-action pairs selection counts (CO), compared with
the inﬂexible baseline and omniscient centralised optimiser control actions
Subplot H shows the battery level proﬁles. In the baseline, the EV is charged as soon as it is plugged in,
given battery capacity and charging rate constraints. The CO policy sells energy from the battery when prices
increase to take advantage of the price diﬀerentials, whereas the MO policy ﬂattens out the charging proﬁle.
26
