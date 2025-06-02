

---

Page 1

---

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021
1
Centralised rehearsal of decentralised cooperation:
Multi-agent reinforcement learning for the scalable
coordination of residential energy flexibility
Flora Charbonnier* Bei Peng† Thomas Morstyn* Malcolm McCulloch*
Abstract—This paper investigates how deep multi-agent re-
inforcement learning can enable the scalable and privacy-
preserving coordination of residential energy flexibility. The
coordination of distributed resources such as electric vehicles
and heating will be critical to the successful integration of large
shares of renewable energy in our electricity grid and, thus,
to help mitigate climate change. The pre-learning of individual
reinforcement learning policies can enable distributed control
with no sharing of personal data required during execution.
However, previous approaches for multi-agent reinforcement
learning-based distributed energy resources coordination impose
an ever greater training computational burden as the size of
the system increases. We therefore adopt a deep multi-agent
actor-critic method which uses a centralised but factored critic
to rehearse coordination ahead of execution. Results show that
coordination is achieved at scale, with minimal information
and communication infrastructure requirements, no interference
with daily activities, and privacy protection. Significant savings
are obtained for energy users, the distribution network and
greenhouse gas emissions. Moreover, training times are nearly 40
times shorter than with a previous state-of-the-art reinforcement
learning approach without the factored critic for 30 homes.
Index
Terms—Cooperative
systems,
Distributed
control,
Demand-side response, Electric vehicles, Energy management
system, Multi-agent reinforcement learning.
I. INTRODUCTION
T
HIS paper tackles the problem of computational scala-
bility in coordinating residential energy flexibility while
maintaining privacy. To achieve this, we propose the use of
cooperative multi-agent reinforcement learning (MARL) with
a centralised but factored critic.
The decarbonisation of power supply, concurrent with the
electrification of heat and transport, is urgently required to
mitigate the climate crisis. To this end, large shares of non-
dispatchable renewable energy must supply the power grid,
just as the loads to be managed increase, thus heightening
the need for demand-side flexibility coordination. Residential
energy has substantial such flexibility potential, particularly
as private transport and heat provision are electrified. For
example, in the UK, the residential sector already represents
about one third of overall electricity demand and up to 60%
of peak demand, when the value of flexibility is highest [1].
The cost of two-way information and distributed computa-
tion infrastructure is a hurdle in the way of this coordination,
as the large overall residential potential is split into millions
*Department of Engineering Science, University of Oxford
†Department of Computer Science, University of Liverpool
of homes with limited individual value [2]. Moreover, users
may distrust interference with their daily activities and privacy
[3, 4]. The question of computational scalability of real-time
control of millions of homes is also unresolved [5].
The use of reinforcement learning (RL) has therefore been
proposed to coordinate distributed energy resources (DERs).
The decentralised execution of pre-learned policies can over-
come these challenges whilst improving robustness and re-
moving the need for a convex representation of complex
systems [5]. However, most existing works have relied on
the centralised [6–21] or bilateral [22] sharing of personal
information. This may raise issues around communication in-
frastructure costs, security, privacy, computational scalability,
and vulnerability to biased information [5, 23, 24].
In implicit coordination strategies, on the other hand, DERs
are coordinated without sharing personal data [5]. Advantages
include reduced complexity and costs of the ICT infrastructure,
enhanced privacy, self-control and acceptability for users,
robustness against failures, and reliability [23, 25]. In RL-
based implementations, the data access and computational
burden needs are shifted to a pre-training phase, when agents
learn individual policies in a shared environment. A fully
decentralised execution at the home level then only depends
on local information. This multi-agent task can be modelled as
a decentralised partially observable Markov decision process
(Dec-POMDP) [26]. Yet, a competitive approach [27, 28],
where each agent only seeks to maximise their own utility,
may lead to sub-optimal outcomes, negatively impacting the
grid and individuals. The peak may be merely displaced,
with overloads on upstream transformers [29]. The addition
of a network management term to the individual competitive
rewards functions was therefore suggested [30]. In [31], full
cooperation is achieved as independent learners concurrently
learn to maximise a shared multi-objective function.
The computational scalability of the training phase for co-
operative DER coordination remains a challenge. To improve
learning efficiency, we seek to adopt a MARL algorithm that
fully exploits the benefits of the centralised training with
decentralised execution (CTDE) [32] paradigm. In CTDE, due
to partial observability or communication constraints, each
agent must learn a decentralised policy conditioned only on
local observations. However, the training itself can be cen-
tralised in a simulated environment, with access to additional
information about the environment (e.g., global state) and
other agents. Table I summarises three common classes of
cooperative MARL approaches used to solve a Dec-POMDP.
arXiv:2305.18875v2  [eess.SY]  5 Jun 2023


---

Page 2

---

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021
2
The simplest type is independent learning, where each agent
treats other agents as part of the environment and learns
independently. For instance, in independent Q-learning (IQL)
[33], each agent i learns a decentralised action-value function
Qi based only on individual observations and actions. This
method is limited as it cannot explicitly represent interactions
between agents. It is also prone to instability as each agent’s
learning is confounded by the learning and exploration of
others and the non-stationarity of the environment [34, 35].
In contrast, one category of CTDE algorithms is the cen-
tralised multi-agent policy gradient method [36–39], in which
each agent learns a centralised critic with a decentralised actor.
The centralised and monolithic critic utilises the global state
and the actions of all agents, which are only available during
centralised training, to estimate the centralised action-value
function Qtot. Compared to Qi, Qtot improves coordination
by capturing the interdependent effects of all agents’ actions
and guiding the optimisation of decentralised policies. Yet,
learning a satisfactory estimate of Qtot can be impractical
since it directly conditions on the global state and joint action,
which can grow exponentially with the number of agents.
Value function factorisation methods [34, 40–43] constitute
another category of CTDE algorithms. The centralised action-
value function Qtot is represented as a mixing function of
individual action-value functions Qi to enable easy decentral-
isation and enhance scalability. Value decomposition has been
shown to be an effective approach in most environments and
shares the major advantages of centralised training, especially
in environments with dense rewards [44], such as in DER
coordination. However, how to best represent and learn Qtot
is still an open question.
Here, to solve the residential energy flexibility coordina-
tion problem, we propose the use of the factored multi-
agent centralised policy gradient (FACMAC) approach [48].
FACMAC is a multi-agent actor-critic method that learns a
single centralised but factored critic1, which factors the cen-
tralised action-value function Qtot as a non-linear monotonic
function of individual action-value functions Qi. It therefore
combines the advantages of both centralised multi-agent policy
gradient and value function factorisation methods. Whilst this
could allow home energy management systems to learn more
coordinated behaviour when privately operating their electric
vehicles (EVs), heating, and other flexible loads, this potential
has thus far not been investigated.
The contribution of this paper is thus to build a bridge
between the fields of DER coordination and MARL to reduce
the computational burden associated with residential energy
flexibility coordination. Using a multi-agent actor-critic frame-
work that learns decentralised policies with a centralised but
factored critic addresses the pitfalls of both the poor coordina-
tion performance of independent learners and the intractability
at scale of optimisations or centralised critic estimation. To
enhance the performance of DER coordination, we further
improve the centralised but factored critic methodology by
incorporating two techniques: convolutional neural networks
1For the remainder of this paper, we will use “FACMAC” and “centralised
but factored critic approach” interchangeably.
MARL Approach
Schematic illustration
Independent learning [31,
33, 45–47]
𝑄!
𝑄"
𝑄#
Centralised
multi-agent
policy gradient [36–39]
𝑄!"#$%"
Value function factorisa-
tion [34, 40–43, 48]
𝑄!
𝑄"
𝑄#
𝑄$%&'(%
TABLE I
THREE COMMON CLASSES OF MULTI-AGENT REINFORCEMENT
LEARNING (MARL) APPROACHES TO SOLVE A DECENTRALISED
PARTIALLY OBSERVABLE MARKOV DECISION PROCESS (DEC-POMDP)2.
[49] and hysteretic learning [50]. Furthermore, we extend the
supervised loss approach from single-agent RL [51] to the
MARL case, to combine computationally “expensive” training
data obtained from system optimisations results and “cheap”
environment exploration to guide the learning of multi-agent
cooperation.
This work freely provides a local energy environment and
MARL testing and benchmarking framework on GitHub3.
MARL research is generally conducted on virtual benchmark
game environments designed explicitly for evaluating and
developing MARL algorithms. If MARL is to leave the
laboratory setting, benchmark environments must tackle real-
world problems such as DER coordination.
The rest of this paper is organised as follows. In Section II,
the testing environment is presented that includes household-
level modelling of EVs, space heating, flexible loads and
photovoltaic (PV) generation. We then describe the MARL
methodologies used to coordinate home energy consumption
in this system in Section III. Their performance is assessed
in experiments conducted using real-life data in Section IV.
Finally, we conclude in Section V.
II. PROBLEM DESCRIPTION
In this section, the variables, objective function and con-
straints of the problem are described. This sets the frame
2Note that the action-value functions are represented as tables (as would
be the case in a tabular Q-learning implementation) for illustration purposes,
though these can be estimated using function approximators such as neural
networks.
3https://github.com/floracharbo/MARL local electricity


---

Page 3

---

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021
3
𝑔! grid import
𝑝"
! home import
𝑝!"
𝑐"
! consumption
Home 1
Household 
demand d"
!
Substation
Temperature 
T"
#
ℎ"
! heating
𝜖$! grid loss
PV production 
p%&,"
#
EV Battery
d(),"
!
 EV demand
charge & discharge 𝑏*+,"
!
𝑏,-!,"
!
loss 𝜖./,"
!
𝜖012,"
!
Home 𝑛
Fig. 1.
Local energy system model. Homes have vehicle-to-grid (V2G)-enabled electric vehicles, flexible household demand, electric heating, and PV
generation. Energy balances apply at the asset-, home- and substation levels.
for the application of the MARL algorithms presented in
Section III. This model is modular, and as such energy
resources in each home could readily be removed, modified
(e.g., using other car models) and added (e.g., modelling smart
hot water tanks) without reducing its compatibility with the
MARL methods. This work uses the model presented in [31].
A. Local energy system model variables
The local system model is illustrated in Figure 1. Partici-
pants under a secondary substation have a V2G-enabled EV,
a PV panel, electric space heating and generic flexible loads.
We consider a set of time steps t ∈T = {t0, ..., tend} and a set
of homes i ∈P = {1, ..., n}. Decision variables are italicised
and input data are written in roman. Energy units are used
unless specified otherwise.
The EV at-home availability µt
i (1 if available, 0 otherwise),
EV demand for required trips dt
EV,i, household electric demand
dt
i, PV production pt
PV,i, external temperature Tt
e and solar heat
flow rate ϕt are specified as inputs for t ∈T and i ∈P.
The local decisions are the battery charge bt
in,i and discharge
bt
out,i, the electric heating consumption ht
i and the household
consumption ct
i. These have local and system impacts. Local
impacts include battery energy levels Et
i, losses ϵt
ch,i and
ϵt
dis,i, home imports pt
i, building mass temperatures T t
m,i and
indoor air temperatures T t
air,i. System impacts arise through
the costs of total grid import gt and distribution network use.
Distribution network losses and reactive power flows are not
included in this work.
B. Objective function
All homes cooperate to minimise the sum of grid (ct
g),
distribution (ct
d) and storage (ct
s) costs.
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
The grid cost coefficient Ct
g is the sum of the grid electricity
price and the product of the carbon intensity at time t and the
social cost of carbon, which reflects the long-term societal
cost of emitting greenhouse gases [52]. The impacts of local
decisions on upstream energy prices are neglected.
ct
d = Cd
X
i∈P
max
 −pt
i, 0

(3)
Distribution costs ct
d are proportional to the distribution charge
Cd on exports. The resulting price spread between individual
imports and exports decreases network constraint violation
risks by incentivising the use of local flexibility first [53].
ct
s = Cs
X
i∈P
 bt
in,i + bt
out,i

(4)
Storage battery depreciation costs ct
s assume a uniform energy
throughput degradation rate Cs [54].
C. Constraints
The constraints for steps ∀t ∈T and homes ∀i ∈P are:
• Substation-, home- and EV battery-level energy balances
– for ηch and ηdis the charge and discharge efficiencies:
X
i∈P
pt
i = gt
(5)
pt
i = ct
i + ht
i +
bt
in,i
ηch
−ηdisbt
out,i −pt
PV,i
(6)
Et+1
i
= Et
i + bt
in,i −bt
out,i −dt
EV,i
(7)
• Battery charge and discharge constraints – Let E0, E
and E be the initial, minimum and maximum battery
energy levels, and bin and bout the maximum charge and
discharge per time step:
E0 = Et0
i = Etend
i
+ btend
in,i −btend
out,i −dtend
EV,i
(8)
µt
iEi ≤Et
i ≤Ei
(9)
bt
in,i ≤µt
ibin
(10)


---

Page 4

---

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021
4
bt
out,i ≤bout
(11)
• Consumption flexibility – Demand dtD
i,k is met by the sum
of partial consumptions ˆci,k,tC,tD at time tC by prosumer
i for load of type k (fixed or flexible) demanded at tD.
The flexibility boolean fi,k,tC,tD indicates if time tC lies
within the acceptable range {tD, ..., tD+nflex} to meet dtD
i,k.
X
tC∈T
ˆci,k,tC,tDfi,k,tC,tD = dtD
i,k
(12)
• Consumption – the total consumption at time tC is the
sum of all partial consumptions ˆci,k,tC,tD:
X
tD∈N
ˆci,k,tC,tD = ctC
i,k
(13)
• Heating – A Crank-Nicholson scheme [55] was refor-
mulated as a linear recursive expression, with κ a 2x5
matrix of temperature coefficients, and Tt
i and T
t
i lower-
and upper-temperature bounds:
T t+1
m,i
T t+1
air,i

= κ
1, T t
m,i, Tt
e, ϕt, ht
i
⊺
(14)
Tt
i ≤T t
air,i ≤T
t
i
(15)
• Non-negativity constraints:
ct
i, ht
i, Et
i, bt
in,i, bt
out,i, ˆci,l,tC,tD ≥0
(16)
III. REINFORCEMENT LEARNING STRATEGY
FORMULATION
We now present the MARL methodologies which allow
independent agents (i.e., homes) to learn to make individual
decisions to maximise the total discounted reward, which is
equivalent to maximising the statistical expectation of the
objective function for the energy system described in Sec-
tion II-B.
The MARL policies are trained in offline simulations prior
to potential online executions in the electricity grid, so agents
do not trial unsuccessful actions with real-life impacts during
learning. Moreover, this means that the computation burden
is taken prior to implementation, and homes would merely
need to apply pre-learned policies, avoiding the computational
challenges of large-scale real-time control in power system
applications.
A. Reinforcement learning
RL is a machine learning paradigm where an agent aims
to solve a sequential decision-making problem by directly
interacting with an uncertain environment [56]. The goal of
the RL agent is to learn a policy (i.e., a sequence of actions)
that maximises its long-term expected total reward.
We consider a fully cooperative multi-agent task in which
a team of agents interacts with the same environment to
achieve some common goal, which can be modelled as a
Dec-POMDP [26]. The Dec-POMDP consists of a tuple
G = ⟨N, S, A, P, r, O, γ⟩. Here N ≡{1, ..., n} denotes the
finite set of agents and s ∈S describes the true state of the
environment. At each time step, each agent i ∈N selects a
discrete or continuous action ai ∈A, forming a joint action
a ∈A ≡An. The environment then produces a transition
to the next state s′ according to the state transition function
P(s′|s, a) : S × A × S →[0, 1] and a team reward r(s, a).
γ ∈[0, 1) is a discount factor. Due to the partial observability,
each agent i ∈N draws an individual partial observation oi ∈
Ωfrom the observation kernel O(s, i). Each agent learns a
policy µi(τi), conditioned only on its local action-observation
history τi ∈T ≡(Ω× A)∗, which may be stochastic or
deterministic. The joint policy µ induces a joint action-value
function: Qµ(st, at)
=
Est+1:∞,at+1:∞[Rt|st, at], where
Rt = P∞
i=0 γirt+i is the discounted return.
RL methods were initially developed for single agents,
rather than for large numbers of agents under partial ob-
servability in stochastic environments. Further methodological
innovation was therefore needed for multiple such agents to
learn to cooperate [31].
B. Optimisation-informed independent learning
Some
of
these
challenges
have
been
mitigated
in
optimisation-informed independent learning [31] by generat-
ing training data using “omniscient” convex optimisations.
Agents thus concurrently learn by interacting with a shared en-
vironment using individual, decentralised fixed-size Q-tables,
guided by the action choice of the agents in the convex
optimisation solutions. These stable, consistent solutions align
with the global optima Pareto and can successfully act as a
coordination mechanism [31].
Additional baselining simulations, which compare total re-
wards to that if each agent took a baseline, inflexible action,
can further improve learnability4. Each agent thus learns
from their marginal reward, i.e., the difference in total instant
rewards rt between that if agent i selects the greedy action
and that if it selects the default action is used to update Qdiff.
The default reward rt
ai=adefault, where all agents perform their
greedy action apart from agent i, which performs the default
action, is obtained by an additional simulation.
Q(st
i, at
i) ←Q(st
i, at
i) + αδ
(17)
where
δ =
 rt −rt
ai=adefault

+ γV diff(st+1
i
) −Qdiff(st
i, at
i)
(18)
However, although this allows for stable coordination per-
formance as the number of agents increases, these coordination
mechanisms come at a computational cost at scale.
C. Centralised but factored critic
Figure 2 schematically illustrates the structure of the mod-
ified factored multi-agent centralised policy gradients (FAC-
MAC) algorithm [48]. Like multi-agent deep deterministic
gradients (MADDPG) [38], a popular multi-agent actor-critic
method, FACMAC uses deep deterministic policy gradients
to learn policies. However, FACMAC learns a centralised but
4“the sensitivity of an agent’s utility to its own actions as opposed to
actions of others, which is often low in fully cooperative Markov games”
[35]


---

Page 5

---

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021
5
Environment
Critic 1
Critic n
Mixing function
𝑄!"! 𝒐!, 𝒂!
Actor 1
Actor n
Forward pass
Backpropagation
𝑎#
!
𝑎$!
𝑜#
!
𝑜$!
𝑠#
!%#
𝑟!
𝑜#
!, 𝑎#
!
𝑜$!, 𝑎$!
𝑄# 𝑜#
!, 𝑎#
!
𝑄$ 𝑜$!, 𝑎$!
  .
𝑄& 𝑜&
!, 𝑎&
!
&'#..$
𝑠!
𝑊#
𝑊)
  .
𝑏#
𝑏)
MLP
MLP
MLP
MLP
𝑄!"! 𝒐!, 𝒂!
𝑐!,
𝑐!
𝑎*+,-
!
1
0
𝑐!
ℎ!
ℎ!
𝑎./01
!
1
0
ℎ!
∆𝑠!
∆𝑠!
𝑎201
!
1
−1
∆𝑠!
Fig. 2. The overall FACMAC architecture. For each agent i, there is one actor network that selects individual action at
i based on local observation ot
i. This
action is inputted into the local energy environment to obtain the next state st+1
i
and reward rt. For each agent i, there is one critic network that estimates
the individual action-value function Qi, which is then combined into the centralised action-value function Qtot via a non-linear monotonic mixing function
approximated by a mixing network with non-negative weights. The actor network includes a convolutional layer followed by two hidden layers. The critic
network is a linear network with one hidden layer.
factored critic, which combines per-agent utilities into the
centralised action-value function via a non-linear monotonic
function, as in QMIX [34]. This enables more scalable learning
of the centralised critic. Moreover, FACMAC uses a new
centralised policy gradient estimator that optimises over the
entire joint action space to allow for more coordinated policy
changes and fully reap the benefits of a centralised critic.
In FACMAC, all agents share a centralised critic Qµ
tot that
is factored as:
Qµ
tot(τ, a, s; ϕ, ψ) = gψ(s, {Qµi
i (τi, ai; ψi)}n
i=1)
(19)
where ϕ and ψ are parameters of the centralised action-
value function Qµ
tot and agent-wise utilities Qµi
i , respectively,
and gψ is a non-linear monotonic function parameterised as
a mixing network with parameters ψ, as in QMIX [34]. To
evaluate the policy, the centralised but factored critic is trained
by minimising the following loss:
L(ϕ, ψ) = ED[(ytot −Qµ
tot(τ, a, s; ϕ, ψ)2]
(20)
where ytot = r + γQµ
tot(τ ′, µ(τ ′; θ−), s′; ϕ−, ψ−), D is the
replay buffer, and θ−, ϕ−and ψ−are the parameters of the
target actors, critic, and mixing network, respectively.
To update the decentralised policy of each agent, a cen-
tralised policy gradient estimator is used to optimise over the
entire joint action space:
∇θJ(µ) = ED[∇θµ∇µQµ
tot(τ, µ1(τ1), ..., µn(τn), s)]
(21)
where µ = {µ1(τ1; θ1), ..., µn(τn; θn)} is the set of all
agents’ current policies, and all agents share the same actor
network parameterised by θ.
We build on this work by making three additional method-
ological contributions:
1) Convolutional networks: A convolutional layer with
kernel size 3 allows for improved feature extraction on both
the actor networks when learning action time series selection
for the day ahead.
2) Hysteretic learning: Hysteretic learners are optimistic
learners that use a higher learning rate for increasing Q-
values than for decreasing Q-values, which helps to reduce
oscillations in the learned policy due to actions chosen by
other agents [50]. For a temporal-difference error δ, the base
learning rate α, and β < α:
( ˆQ(s, a) ←ˆQ(s, a) + αδ
if δ > 0
ˆQ(s, a) ←ˆQ(s, a) + βδ
otherwise
(22)
3) Supervised loss: Inspired by [51], we propose a mixed
optimisation-informed centralised but factored critic approach
that incorporates a supervised loss, so agents can learn from
both demonstrator and exploration data. The supervised loss
enables the agent to learn to mimic the expert demonstrations
(the convex optimisation results in our problem), while the
temporal difference loss enables the agent to learn from its
own experience generated through directly interacting with


---

Page 6

---

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021
6
the environment. This mechanism thus combines “expensive”
demonstration data from convex optimisations and “cheap”
exploration data from simulation environment to guide the
learning of multi-agent cooperation. A weighted penalty is
added to the loss for actions that deviate from the demonstrator
data:
δsupervised loss = C
X
t
 at
i,demonstrator −at
i,exploration
2
(23)
We investigate whether this could guide the agents’ learning
and reduce the number of exploration steps required, especially
as the exploration space and coordination challenges are
particularly potent in MARL.
D. RL formulation
Here, we present how the decision variables in Section II
translate into RL experience tuples (ot
i, at
i, rt).
1) Observation: The IQL methodology performed best
with a small observation space, which we therefore limit to the
current grid cost coefficient. In the factored critic methodology,
the observation space consists of the grid cost coefficients for
24 hours ahead
2) Actions: The RL agent selects three different actions.
The constraints are then enforced in the environment thanks
to a physics-informed approach to translate these agent actions
into feasible EV, heating and flexible consumption variables.
• Battery action at
bat,i ∈[−1, 1]: for negative values scales
the maximum amount of feasible discharge (bt
out,i), and
for positive values of feasible charge (bt
in,i), as illustrated
in Figure 3. Given Equations (7) to (11):
(∆st
i, ∆st
i) =
f(Et
i, dt
EV,i, ..., dtend
EV,i, µt
i, ..., µtend
i
, E0, E, E, bout, bin)
(24)
abattery [-]
s [kWh]
0
0
Fig. 3. Translating the battery action into the change in battery energy level.
• Heating action at
heat,i ∈[0, 1]: linearly scales between the
minimum and maximum amount of feasible heating (ht
i)
given local temperature constraints. Given Equations (14)
and (15):
(ht
i, ht
i) = f(T t
m,i, Tt
e, ϕt, T t
i,air, T t
i,air)
(25)
ht
i = (1 −at
i,heat)ht
i + at
i,heatht
i
(26)
• Household consumption action at
cons,i ∈[0, 1]: scales fea-
sible flexible household consumption (ct
i). Given Equa-
tions (12) and (13):
(ct
i, ct
i) = f(dt−nflex
i
, ..., dt
i, ct−nflex
i
, ..., ct−1
i
)
(27)
ct
i = (1 −at
i,cons)ct
i + at
i,consct
i
(28)
3) Reward: The global reward rt ∈R the RL agents
receive at each timestep corresponds to the share ˆFt of the
system objective function presented in Section II-B.
IV. RESULTS
We conduct a series of experiments to assess the per-
formance and computational scalability of the MARL ap-
proaches presented in Section III, when applied to solve
the residential flexibility coordination problem in Section II.
Both the optimisation-informed independent learning and the
centralised but factored critic approach achieve coordination at
scale for the homes controlling their DERs. However, the fac-
tored critic achieves this with a nearly 40-fold computational
cost reduction for 30 homes.
A. Set-up
The input data generation is presented in [31]. It draws on
large-scale real-life data [57–59] to generate realistic training
and testing samples in a consistent manner. The social cost of
carbon is set at 70 £/tCO2, consistent with the UK 2030 target
[60]. Weather [61], electricity time-of-use prices [62] and grid
carbon intensity [63] are from January 2021, where relevant
specified for Oxford, UK. The low solar heat gains in January
are neglected [64]. EVs are assumed to have a capacity of 39
kWh and 6.6 kW maximum charging rate [65]. All code and
other parameters are freely available on GitHub5.
B. Results and discussion
Figure 4 shows that the methodological additions of hys-
teretic learning and convolutional layers in the actor networks
significantly improved the performance of the FACMAC ap-
proach when applied to the problem of DER coordination and
planning for day-long time series. The increase in average
savings is seen to be primarily driven by an improvement of
lower percentile “worst-case” performances.
Adopting these two additions, Figure 5(a) then shows the
total system savings achieved per home and month as the
number of agents trained increases. These savings are com-
puted relative to a baseline where all agents are inflexible,
with EVs charged immediately and no flexible loads delayed.
An example day is illustrated in Figure 6, showing local
control variables for a home in the inflexible and coordinated
scenarios.
We can see that the coordination performance of IQL (grey
line) drops as the number of homes increases, even if learning
from optimisation data (grey dotted line). This is due to the
learnability issues mentioned above for independent learn-
ers. Without a coordination mechanism, independent learners
under partial observability in a stochastic environment face
challenges such as the incompatibility of individual policy
equilibriums with a global Pareto optimal, the non-stationarity
of the environment due to other concurrently learning agents
affects convergence, and the stochasticity of the environment
5https://github.com/floracharbo/MARL local electricity


---

Page 7

---

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021
7
1
2
3
- 20
0
20
40
Savings [£/home/month]
hysteretic 
learning 
convolutional
neural
network 
mean 
median 
interquartile range 
1: linear neural network, no hysteretic learning
2: linear neural network, hysteretic learning
3: convolutional neural network, hysteretic learning
Fig. 4. Improvements in savings per home and month achieved when adding
the use of hysteretic learning and of convolutional neural networks for 10
homes using the adapted FACMAC approach.
prevents agents from discriminating between their own con-
tribution to global rewards and noise from other agents or the
environment [35].
Only when combining optimisation-informed learning with
individual marginal rewards can coordination be achieved
at scale (blue dotted line). However, even in cases where
optimisation models are available (which is often not the
case in complex real-life problems), optimisations are com-
putationally expensive. Indeed, in the interior point method,
which is used to solve non-linear continuous problems in
convex optimisation solvers, the inverse of the Jacobian of the
Karush–Kuhn–Tucker (KKT) conditions must be computed in
each Newton-Raphson update step. As this includes derivatives
with respect to all decision variables of the problem for all
constraints and the objective function [67], the Jacobian grows
with O(n2). This step therefore bears a high computational
burden which can be prohibitive as the system size grows [68],
particularly in machine learning applications where numerous
optimisations must be performed to generate training data.
The centralised but factored critic methodology (green
lines) achieves equivalent coordination performance to the
optimisation-informed marginal reward Q-learning approach,
whilst overcoming its dependency on optimisations and addi-
tional marginal rewards computations. The objective function
in Section II could be reduced by £49.84 per home and
month on average for 30 homes, or a 7.4% reduction. £46.51
was saved through reduced consumer energy bills and £3.56
through greenhouse gas emissions reduction. At the same time,
battery depreciation costs increased by £0.17 and distribution
network use increased the total costs by £0.05 per month and
home relative to the inflexible baseline.
The centralised but factored critic can capture a global
understanding of the impact of individual policies on the
system via the centralised action-value function, using extra
information (e.g., global state and joint action) available only
during training. In the residential DER coordination problem,
100
80
60
40
20
0
20
40
60
Savings [£/home/month]
Independent Q-learning
Marginal reward Q-learning
Centralised but factored critic
0
5
10
15
20
25
30
Number of homes
102
103
104
Time [s]
y = 14.94x2 + 444.58x + 312.92
y = 22.9x + 53.4
+ 53.4
a
b
Fig. 5.
(a) 50th percentile savings per home and month relative to the
baseline scenario as the number of agents increases over ten repeats. Full
lines correspond to training using random environment explorations only.
Dotted lines use experience from convex optimisations for training. The
shaded areas show the spread between the 25th and 75th percentile values
over the ten repeats. (b) Corresponding required computation time for the
10 repeats for the two methodologies which achieve coordination at scale,
namely optimisation-informed independent Q-learning and the centralised but
factored critic approach. Functions are fitted using SciPy’s optimize.curve fit
non-linear least squares function [66]6.
there is particularly high value in cooperation signals that take
a global view of the system, as the global rewards are highly
dependent on the cumulative impact of multiple agents taking
actions simultaneously. The backward propagation of gradients
from the centralised but factored critic to the individual actor
networks can then guide the optimisation of individual policies
in the absence of full state information at the scale of indi-
vidual agents [44]. FACMAC can also enable more scalable
learning as the centralised action-value function is represented
as a combination of individual action-value functions, which
condition on much smaller local observations and actions. The
factored critic uses information more efficiently as network
weight updates use state space information that has the most
impact on the global value of actions taken by agents. The
updates structurally take into account the partial observability
of agents taking actions, and aim to update only the knowledge
necessary to know which actions agents should take and when.
6Fitting a second-order polynomial function into the computational time
of the centralised but factored critic approach yields a second-order term
coefficient of -0.175 and a first-order coefficient of 28.272. This confirms
the hypothesis that a first-order complexity representation is a better fit, as
illustrated in Figure 5(b).


---

Page 8

---

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021
8
0
5
10
15
20
0.15
0.20
0.25
0.30
0.35
Grid price [£/kWh]
a
Wholesale
Cg
0
5
10
15
20
0
5
10
15
Home consumption [kWh]
b
baseline
MARL policy
0
5
10
15
20
Time [h]
28
30
32
34
36
38
EV battery level [kWh]
c
EV on a trip
0.26
0.28
0.30
0.32
0.34
Carbon intensity 
[kgCO2/kWh]
Fig. 6.
Example day: (a) Wholesale prices, grid carbon intensity, and
resulting grid cost coefficient Cg given a social cost of carbon of 70 £/tCO2.
(b) Total energy consumption, including both household loads and heating
consumption. (c) EV battery energy profile.
The back-propagation from the centralised but factored
critic thus mirrors the global optimisation, given the partial ob-
servability of the agents taking actions: each back-propagation
includes a Jacobian-gradient product of the value error with
respect to the weights of the networks for each operation in the
graph. Figure 5 thus shows that optimisation-informed FAC-
MAC (incorporating the supervised loss, green dotted line)
does not achieve superior performance relative to FACMAC.
This demonstrates that the centralised but factored critic alone
already provides an equivalent coordination mechanism for
the cooperation of the agents in the system, and the use of
optimisation data adds no additional value.
The optimisation-informed independent learning and the
centralised but factored critic approaches thus mirror each
other in their provision of a global coordination mechanism
and achieve very similar performance, while having structural
differences which lead to varying computational efficiencies.
In both cases, the Jacobian plays a role, and both marginal
rewards and the backward propagation from the centralised
but factored critic aim to improve learnability, sending per-
sonalised rewards to each agent that best represent their
contribution to the global reward. One advantage of IQL is
that it does not require neural networks and, as such, is more
robust to hyper-parameter tuning and more easily interpretable,
provided it can learn from model optimisation results. It also
provides superior coordination performance below 10 agents,
as FACMAC was designed for scale, when more invidual critic
networks can yield better centralised critic factorisation. Nev-
ertheless, the factored critic uses information more efficiently
and achieves superior computational scalability as the number
of value networks only grows linearly with the number of
homes O(n). Figure 5(b) shows the optimisation-informed ap-
proach required second-order polynomial computational time
as the number of agents increases, whereas the centralised but
factored critic methodology required approximately first-order
polynomial time. For 30 homes, the factored critic approach
thus required 38.9 times less computational time.
V. CONCLUSION
This paper has proposed the use of a cooperative multi-
agent reinforcement learning approach that learns a centralised
but factored critic to enable privacy-preserving and scalable
coordination of residential energy flexibility.
Compared with a previous state-of-the-art independent
learning approach which learned from global optimisation
results, the centralised but factored critic yielded similar
coordination at scale, as each coordinated home provided
an average reduction of £46.82 in global system costs per
month for 30 homes. Moreover, the centralised but factored
critic approach required computational time nearly 40 times
lower for 30 homes, and growing only at first-order rather
than second-order polynomial time. This improved scalability
opens the way for coordinating flexible energy resources such
as electric vehicles and heating in a fully distributed manner.
The impact of such coordination on the distribution net-
work and the potential cooperative management of network
constraints by agents could be further investigated.
REFERENCES
[1] J. Torriti.
Household electricity demand, the intrinsic
flexibility index and UK wholesale electricity market
prices.
Environmental Economics and Policy Studies,
24(1):7–27, 2022.
[2] T-O. L´eautier.
Imperfect Markets and Imperfect Reg-
ulation: An Introduction to the Microeconomics and
Political Economy of Power Markets. MIT Press, 2019.
[3] K. Pumphrey, S. Walker, M. Andoni, and V. Robu.
Green hope or red herring? Examining consumer percep-
tions of peer-to-peer energy trading in the United King-
dom. Energy Research and Social Science, 68(September
2019):101603, 2020.
[4] D. Bugden and R. Stedman.
A synthetic view of
acceptance and engagement with smart meters in the
United States.
Energy Research and Social Science,
47(January 2018):137–145, 2019.
[5] F. Charbonnier, T. Morstyn, and M. Mcculloch. Coordi-
nation of resources at the edge of the electricity grid


---

Page 9

---

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021
9
: Systematic review and taxonomy.
Applied Energy,
318(April):119188, 2022.
[6] D. O’Neill, M. Levorato, A. Goldsmith, and U. Mi-
tra. Residential Demand Response Using Reinforcement
Learning. 2010 First IEEE International Conference on
Smart Grid Communications, pages 409–414, 2010.
[7] I. Antonopoulos et al. Artificial intelligence and machine
learning approaches to energy demand-side response: A
systematic review. Renewable and Sustainable Energy
Reviews, 130(April):109899, 2020.
[8] S. Darby.
Demand response and smart technology in
theory and practice: Customer experiences and system
actors. Energy Policy, 143(April):111573, 2020.
[9] T. Chen and W. Su.
Indirect Customer-to-Customer
Energy Trading with Reinforcement Learning.
IEEE
Transactions on Smart Grid, 10(4):4338–4348, 2019.
[10] R. Lu and S. Hong. Incentive-based demand response for
smart grid with reinforcement learning and deep neural
network. Applied Energy, 236(December 2018):937–949,
2019.
[11] B. Kim, Y. Zhang, M. Van Der Schaar, and J. Lee.
Dynamic Pricing and Energy Consumption Scheduling
With Reinforcement Learning.
IEEE Transactions on
Smart Grid, 7(5):2187–2198, 2016.
[12] P. H. Babar, M. Zbigniew Hanzelka. The evaluation of
agile demand response: An applied methodology. IEEE
Transactions on Smart Grid, 9(6):6118–6127, 2018.
[13] M. G. Vay´a, L. B. Rosell´o, and G. Andersson. Optimal
bidding of plug-in electric vehicles in a market-based
control setup. Proceedings - 2014 Power Systems Com-
putation Conference, PSCC 2014, 2014.
[14] Y. Ye, D. Qiu, M. Sun, D. Papadaskalopoulos, and
G. Strbac. Deep Reinforcement Learning for Strategic
Bidding in Electricity Markets. IEEE Transactions on
Smart Grid, 11(2):1343–1355, 2020.
[15] D. Dauer, C. Flath, P. Str¨ohle, and C. Weinhardt. Market-
based EV charging coordination.
Proceedings - 2013
IEEE/WIC/ACM International Conference on Intelligent
Agent Technology, IAT 2013, 2:102–107, 2013.
[16] Y. Sun, A. Somani, and T. Carroll.
Learning based
bidding strategy for HVAC systems in double auction
retail energy markets.
Proceedings of the American
Control Conference, 2015-July:2912–2917, 2015.
[17] J. Kim and B. Lee. Automatic P2P energy trading model
based on reinforcement learning using long short-term
delayed reward. Energies, 13(20), 2020.
[18] B. Claessens, S. Vandael, F. Ruelens, K. De Craemer,
and B. Beusen. Peak shaving of a heterogeneous clus-
ter of residential flexibility carriers using reinforcement
learning.
2013 4th IEEE/PES Innovative Smart Grid
Technologies Europe, ISGT Europe 2013, pages 1–5,
2013.
[19] X. Zhang, T. Bao, T. Yu, B. Yang, and C. Han.
Deep transfer Q-learning with virtual leader-follower for
supply-demand Stackelberg game of smart grid. Energy,
133:348–365, 2017.
[20] I. Dusparic, A. Taylor, A. Marinescu, V. Cahill, and
S. Clarke.
Maximizing renewable energy use with
decentralized residential demand response. 2015 IEEE
1st International Smart Cities Conference, ISC2 2015,
2015.
[21] L. Hurtado, E. Mocanu, P. Nguyen, M. Gibescu, and
R. Kamphuis. Enabling Cooperative Behavior for Build-
ing Demand Response Based on Extended Joint Action
Learning. IEEE Transactions on Industrial Informatics,
14(1):127–136, 2018.
[22] A. Taylor, I. Dusparic, E. Galvan-Lopez, S. Clarke,
and V. Cahill. Accelerating Learning in multi-objective
systems through Transfer Learning.
Proceedings of
the International Joint Conference on Neural Networks,
pages 2298–2305, 2014.
[23] J. Guerrero, D. Gebbran, S. Mhanna, A. Chapman, and
G. Verbiˇc.
Towards a transactive energy system for
integration of distributed energy resources: Home energy
management, distributed optimal power flow, and peer-
to-peer energy trading. Renewable & sustainable energy
reviews, 132, 2020.
[24] T. Morstyn and M. Mcculloch. Peer-to-Peer Energy Trad-
ing. Analytics for the Sharing Economy: Mathematics,
Engineering and Business Perspectives, (March), 2020.
[25] T. Mai et al.
An overview of grid-edge control
with the digital transformation. Electrical Engineering,
103(4):1989–2007, 2021.
[26] Frans A Oliehoek and Christopher Amato.
A concise
introduction to decentralized POMDPs. Springer, 2016.
[27] J. Cao.
Deep Reinforcement Learning Based Energy
Storage Arbitrage With Accurate Lithium-ion Battery
Degradation Model. IEEE Transactions on Smart Grid,
14(8):1–9, 2019.
[28] Y. Yang, J. Hao, Y. Zheng, and C. Yu.
[29] C. Crozier, D. Apostolopoulou, and M. McCulloch.
Mitigating the impact of personal vehicle electrifica-
tion: A power generation perspective.
Energy Policy,
118(2013):474–481, 2018.
[30] A. Pigott, C. Crozier, K. Baker, and Z. Nagy.
Gri-
dLearn: Multiagent reinforcement learning for grid-aware
building energy management.
Electric Power Systems
Research, 213(October 2021):108521, 2022.
[31] F. Charbonnier, T. Morstyn, and M. McCulloch. Scal-
able multi-agent reinforcement learning for distributed
control of residential energy flexibility. Applied Energy,
314:118825, 2022.
[32] F. A Oliehoek, M. Spaan, and N. Vlassis. Optimal and
approximate q-value functions for decentralized pomdps.
Journal of Artificial Intelligence Research, 32:289–353,
2008.
[33] M. Tan. Multi-Agent Reinforcement Learning : Indepen-
dent vs. Cooperative Agents. 1993.
[34] T. Rashid, M. Samvelyan, C. Schroeder de Witt, G. Far-
quhar, J. Foerster, and S. Whiteson. QMIX: Monotonic
Value Function Factorisation for Deep Multi-Agent Re-
inforcement Learning Tabish. Proceedings of the 35th
International Conference on Machine Learning, 2018.
[35] L. Matignon, G. Laurent, and N. Le Fort-Piat.
Inde-
pendent reinforcement learners in cooperative Markov
games:
A
survey
regarding
coordination
problems.


---

Page 10

---

JOURNAL OF LATEX CLASS FILES, VOL. 14, NO. 8, AUGUST 2021
10
Knowledge Engineering Review, 27(1):1–31, 2012.
[36] J. Gupta, M. Egorov, and M. Kochenderfer.
Coop-
erative Multi-agent Control Using Deep Reinforcement
Learning. Lecture Notes in Computer Science (including
subseries Lecture Notes in Artificial Intelligence and
Lecture Notes in Bioinformatics), 10642 LNAI:66–83,
2017.
[37] J. Foerster, G. Farquhar, T. Afouras, N. Nardelli, and
S. Whiteson. Counterfactual multi-agent policy gradients.
32nd AAAI Conference on Artificial Intelligence, AAAI
2018, pages 2974–2982, 2018.
[38] R. Lowe, Y. Wu, A. Tamar, J. Harb, A. Pieter, and I. Mor-
datch.
Multi-agent actor-critic for mixed cooperative-
competitive environments. In I. Guyon, U. Von Luxburg,
S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan,
and R. Garnett, editors, Advances in Neural Information
Processing Systems, volume 30. Curran Associates, Inc.,
2017.
[39] R.
Lowe.
Multi-Agent
Actor-Critic
for
Mixed
Cooperative-Competitive Environments. 2020.
[40] T. Rashid, G. Farquhar, B. Peng, and S. Whiteson.
Weighted QMIX: Expanding monotonic value function
factorisation for deep multi-agent reinforcement learning.
In Advances in Neural Information Processing Systems,
volume 33, pages 10199–10210, 2020.
[41] J. Wang, Z. Ren, T. Liu, Y. Yu, and C. Zhang. QPLEX:
Duplex dueling multi-agent Q-learning. In International
Conference on Learning Representations, 2021.
[42] Jian H., Seth A. H., Haibin W., and Shih-wei L. QR-
MIX: distributional value function factorisation for co-
operative multi-agent reinforcement learning.
CoRR,
abs/2009.04197, 2020.
[43] W. Qiu, et al. Rmix: Learning risk-sensitive policies for
cooperative reinforcement learning agents. 2021.
[44] G. Papoudakis, F. Christianos, L. Sch¨afer, and S. V.
Albrecht. Benchmarking multi-agent deep reinforcement
learning algorithms in cooperative tasks, 2020.
[45] V. Mnih et al.
Playing atari with deep reinforcement
learning. CoRR, abs/1312.5602, 2013.
[46] S. Omidshafiei, J. Pazis, C. Amato, J. P. How, and J. Vian.
Deep decentralized multi-task multi-agent reinforcement
learning under partial observability. 34th International
Conference on Machine Learning, ICML 2017, 6:4108–
4122, 2017.
[47] J. Foerster et al. Stabilising experience replay for deep
multi-agent reinforcement learning.
34th International
Conference on Machine Learning, ICML 2017, 3:1879–
1888, 2017.
[48] B. Peng et al. Facmac: Factored multi-agent centralised
policy gradients. 34:12208–12221, 2021.
[49] Y. Lecun, L. Bottou, Y. Bengio, and P. Haffner. Gradient-
based learning applied to document recognition.
Pro-
ceedings of the IEEE, 86(11):2278–2324, 1998.
[50] L. Matignon, G. Laurent, and N. Le Fort-piat. Hysteretic
Q-Learning : an algorithm for Decentralized Reinforce-
ment Learning in Cooperative Multi-Agent Teams.
In
Proceedings of the 2007 IEEE/RSJ International Con-
ference on Intelligent Robots and Systems, pages 64–69.
IEEE, 2007.
[51] T. Hester et al. Deep q-learning from demonstrations.
32nd AAAI Conference on Artificial Intelligence, AAAI
2018, pages 3223–3230, 2018.
[52] M. Parry. Climate change 2007: impacts, adaptation and
vulnerability. Published for the Intergovernmental Panel
on Climate Change [by] Cambridge University Press,
Cambridge, 2007.
[53] T. Morstyn, A. Teytelboym, C. Hepburn, and M. McCul-
loch. Integrating P2P Energy Trading with Probabilistic
Distribution Locational Marginal Pricing. IEEE Trans-
actions on Smart Grid, 11(4):3095–3106, 2020.
[54] R. Dufo-L´opez, J. M Lujano-Rojas, and J. Bernal-
Agust´ın.
Comparison of different lead–acid battery
lifetime prediction models for use in simulation of stand-
alone photovoltaic systems.
Applied energy, 115:242–
253, 2014.
[55] ISO. Calculation of Energy Use for Space Heating and
Cooling ISO/FDIS 13790:2007(E), 2007.
[56] R. Sutton and A. Barto.
Reinforcement learning : an
introduction [electronic resource]. Adaptive computation
and machine learning. MIT Press, Cambridge, Mass.,
1998.
[57] R. Wardle. Dataset (TC1a): Basic Profiling of Domestic
Smart Meter Customers, 2014.
[58] R. Wardle. Dataset (TC5): Enhanced Profiling of Do-
mestic Customers with Solar Photovoltaics (PV), 2014.
[59] Department for Transport. National Travel Survey 2002-
2017, 2019.
[60] D. Hirst. Commons Briefing Paper SNO5927: Carbon
Price Floor (CPF) and the price support mechanism,
2018.
[61] Global Modeling and Assimilation Office (GMAO).
Merra-2 inst1 2d asm Nx: 2d,1-hourly, instantaneous,
single-level,
assimilation,
single-level
diagnostics
v5.12.4, 2015.
[62] Octopus Energy. Octopus Energy API, 2019.
[63] National Grid ESO, Environmental Defense Fund Eu-
rope, University of Oxford Department of Computer
Science, and WWF. Carbon Intensity API, 2020.
[64] J. Brown, J. Chambers, and A. Rogers.
SMITE :
Using Smart Meters to Infer the Thermal Efficiency
of Residential Homes.
In The 7th ACM International
Conference on Systems for Energy- Efficient Buildings,
Cities, and Transportation (BuildSys ’20), 2020.
[65] Nissan Intelligent Mobility. Nissan leaf, 2022.
[66] P. Virtanen. SciPy 1.0: Fundamental Algorithms for Sci-
entific Computing in Python. Nature Methods, 17:261–
272, 2020.
[67] S. Wright. Primal-Dual Interior-Point Methods. Society
for Industrial and Applied Mathematics, 1997.
[68] K. Baker. A learning-boosted quasi-newton method for
ac optimal power flow. arXiv preprint arXiv:2007.06074,
2020.
