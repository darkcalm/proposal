

---

Page 1

---

1
Distributed Energy Management and Demand Response in
Smart Grids: A Multi-Agent Deep Reinforcement Learning
Framework
AMIN SHOJAEIGHADIKOLAEI, University of Kansas
ARMAN GHASEMI, University of Kansas
KAILANI JONES, University of Kansas
YOUSIF DAFALLA, University of Kansas
ALEXANDRU G. BARDAS, University of Kansas
REZA AHMADI, Amazon Web Services, Kirkland
MORTEZA HASHEMI, University of Kansas
This paper presents a multi-agent Deep Reinforcement Learning (DRL) framework for autonomous control
and integration of renewable energy resources into smart power grid systems. In particular, the proposed
framework jointly considers demand response (DR) and distributed energy management (DEM) for residential
end-users. DR has a widely recognized potential for improving power grid stability and reliability, while at
the same time reducing end-users’ energy bills. However, the conventional DR techniques come with several
shortcomings, such as the inability to handle operational uncertainties while incurring end-user disutility,
which prevents widespread adoption in real-world applications. The proposed framework addresses these
shortcomings by implementing DR and DEM based on real-time pricing strategy that is achieved using deep
reinforcement learning. Furthermore, this framework enables the power grid service provider to leverage
distributed energy resources (i.e., PV rooftop panels and battery storage) as dispatchable assets to support the
smart grid during peak hours, thus achieving management of distributed energy resources. Simulation results
based on the Deep Q-Network (DQN) demonstrate significant improvements of the 24-hour accumulative
profit for both prosumers and the power grid service provider, as well as major reductions in the utilization of
the power grid reserve generators.
CCS Concepts: • Theory of computation →Multi-agent reinforcement learning; • Information sys-
tems →Mobile information processing systems;
Additional Key Words and Phrases: Demand Response, Distributed Energy Management, Reinforcement
Learning, Deep Q-Network (DQN)
1
INTRODUCTION
Recent proliferation in renewable energy sources (RESs) and distributed energy resources (DERs)
along with the advances in information and communication technologies (ICT) has facilitated a
paradigm shift from the traditional power consumers to the more resourceful energy prosumers. A
prosumer is an active end-user with the ability to consume and produce energy [1]. The number of
prosumers is increasing as more households are proceeding to install solar photovoltaic (PV) rooftop
panels and energy storage system (ESS) [2]. The premise of such a distributed network of energy
resources is to provide economic and ancillary benefits to both prosumers and power grid service
provider (SP) [3]. The interaction between the prosumers and SP has been investigated in several
prior studies. Many works utilize model-based control paradigms, such as model predictive control
(MPC) [4], mixed-integer linear programming (MILP) [5], dynamic and stochastic programming [6],
and alternating direction method of multiplier (ADMM) [7]. One key step for applying these
techniques is to establish an accurate model that captures the dynamics of the microgrid and the
interactions between various components with all the operational constraints.
arXiv:2211.15858v1  [cs.MA]  29 Nov 2022


---

Page 2

---

The massive deployment of DERs and RESs dramatically increases the complexity and uncertainty
of the system due to the more complex cross-area power balancing between SP and prosumers. This
makes the accurate system model hard to obtain. The model-based nature of the aforementioned
methods also exhibits limited generalization capabilities [8]. Difficulties in handling nonlinear
behavior, volatile renewable generations, and heterogeneity of the end-users represent other major
shortcomings of these methods. To overcome these challenges, model-free Reinforcement Learning
(RL) techniques are proven beneficial for demand-side energy management since they do not require
an explicit model of the environment. In general, RL frameworks are emerging as the pre-eminent
tool for sequential decision-making problems within unknown environments. Similar to many
other scientific and engineering domains, the RL-based solutions are receiving more attention from
the power system society. For instance, voltage and frequency control [9], market bidding [10],
microgrid energy management [11], and demand response (DR) [12] are just a few examples of
power-related problems that can be solved using RL.
In this paper, and to bridge the gap between the power system and RL communities, we investigate
the mutual interplay between participants and the different tasks in a residential microgrid. We
propose a framework based on Deep Reinforcement Learning (DRL) for both SP and prosumers
to enable dynamic decision-making. A service provider agent (SPA) is deployed for solving the
distributed energy management (DEM) problem in the microgrid by dynamically determining the
electricity buy price as a control parameter for optimization of the energy management across
distributed prosumers. For instance, a higher electricity buy price during peak hours (e.g., evening
hours) incentivizes the prosumers with surplus energy to discharge their battery. As a result, the
prosumer receives economic benefit in terms of electricity bill reduction. This process is called
Demand Response (DR). The purpose of DR is to encourage the prosumers to actively participate in a
program and contribute to the optimal energy distribution in the electricity retail market. Moreover,
buying electricity from distributed prosumers would enable the power grid service provider to
support higher demands during peak hours. In our envisioned system model, the prosumer agent
(PA) solves the prosumer energy management problem by determining the charge/discharge of the
battery installation. Thus, each prosumer independently maximizes its own profit.
In summary, our main contributions are as follows:
• We formally define the interaction between SP and the prosumers as a Markov Decision
Process (MDP), and develop a multi-agent DRL framework that interweaves the real-
time energy management over the microgrid with the prosumer side real-time DR, using
demand-dependent dynamic pricing for incentivizing prosumers’ participation in DR.
• We show that the proposed DRL framework enables the service provider to leverage energy
storage as dispatchable assets, while incentivizing the prosumers to actively participate in
the program to support the grid activities.
• Our numerical results based on Deep Q-Network (DQN) demonstrate that the proposed
framework reduces the average daily bill for prosumers, while at the same time it provides
higher profits for the grid service provider (SP) by leveraging distributed energy resources
instead of tapping into traditional reserve generation facilities with higher costs.
The remainder of this paper is organized as follows. Section 2 covers related work, followed by the
system model and problem formulation in Section 3. Next, Section 4 formulates the DRL framework
and Section 5 presents numerical results. Finally, Section 6 concludes the paper.
2


---

Page 3

---

2
RELATED WORK
The interaction between service provider and end-users have been investigated in many prior
works. Recently, there has been growing interests in adopting RL to address the concerns of this
interaction. These attempts can be categorized as follows:
Prior Works Focused on Service Provider: A multitude of prior works use RL in the context of
power systems, mainly to address service provider concerns. For example, a hierarchical electricity
market with bidding and pricing over wholesale and retailer using DRL was proposed in [13].
In [14], a Deep Deterministic Policy Gradient (DDPG) algorithm was used to solve the bidding
problem of several generation companies. Moreover, RL has been widely employed for energy
management optimization [15, 16]. In [15], the authors proposed a multi-agent distributed energy
management using Q-learning framework with time-of-use pricing for a microgrid energy market
with a centralized battery pack and renewable generation. The authors in [16] designed a novel
RL method that uses classical recurrent neural networks instead of SAR (State-Action-Reward)
method to solve the microgrid energy management in the Industrial Internet of Things (IIoT). In
contrast to these works, we propose a dynamic pricing scheme with DQN at the service provider
side, combined with distributed battery and PV installations at the demand side.
Prior Works Focused on End-users: The authors in [17] developed a DDQN-based load
scheduling algorithm with a time-of-use scheme to reduce the peak load demand and the operation
cost for the distribution system, however without considering prosumers. In [18], the interaction
between households and the service provider was modeled to jointly solve the energy scheduling
consumption and preserving privacy for the households by using policy gradient RL method.
Furthermore, [19] developed a home energy management system (HEMS) using Actor-Critic
technique based on adaptive dynamic programming. Likewise, in [20], an energy management
DR using Q-learning adjusts the consumption plan for thermostatically controlled loads. Along
the same lines, [21] proposed a framework for home energy management based on multi-agent
Q-learning to minimize the electricity bill as well as DR-induced dissatisfaction costs for end-users.
Their method considered proliferation of rooftop PV systems, but did not consider home energy
storage systems. Moreover, the works in [22, 23], focused on reducing the high peak load in large-
scale HEM using Entropy-based multi-agent deep reinforcement learning, and the work in [24]
applied prioritized DDPG in multi-carrier energy system to solve the real-time energy management
problem. It is also worth noting that these works [17–23] do not consider the grid side and only
propose optimization algorithms for end-users.
Prior Works Focused on Both Service Provider and End-users: Other research works have
addressed the interactions between retailer/SP and end-users. For example, [25] investigated a
gradient-based method to minimize the aggregate load demand by assuming the presence of
consumption scheduling devices on the users side. Furthermore, works such as [26–28] leveraged
the Stackelberg game to model and maximize the retailer profit and minimize the payment bill of its
customers. The authors included renewable energy generation on the retailer side, which is different
from our model with distributed PV installations across prosumers. The studies in [29] and [30]
proposed a hierarchical agent-based framework to maximize both retailer and customers profits. A
Q-learning DR is proposed in [31] for the energy consumption scheduling problem that can work
without prior information and leads to reduced system costs. Also, in [32] both service provider
profit and consumers’ cost are considered to find the optimal retail price. However, unlike our effort,
the works presented in [29–32] only consider regular electricity consumers, rather than prosumers
with generation and storage capabilities. In contrast to these efforts, we model a microgrid that
consists of both consumers and prosumers that are equipped with battery storage. As a result, the
proposed multi-agent DRL framework achieves DR with dynamic pricing and distributed energy
3


---

Page 4

---

Table 1. Taxonomy of Related Work on Management of Distributed Energy Resources. (!: Considered, —:
Not Considered )
Reference
Energy management
Retailer/end-user
Renewable penetration
Energy storage
RL
DR
profit optimization
consideration
consideration
algorithm
[29],[31],[32]
!
!
—
—
!
[27],[28],[18],[30]
!
!
—
—
—
[21]
—
!
!
—
!
[22], [23]
—
!
—
—
!
[26]
!
—
—
!
!
Our proposed framework
!
!
!
!
!
AI agent
Service Provider
Prosuemer with 
PV & ESS system
Consumer
Information Flow
Electrical Connection
g
N
Electricity Flow
1,2,...,
1,2,...,
1,2,...,
g
p
c
i
N
j
N
c
N
=
=
=
p
N
1
2
1
2
2
1
c
N
Generation Facilities
Prosumers
Consumers
1
G
P
2
G
P
1
H
P
2
H
P
j
H
P
i
G
P
cnP
1nP
2
nP
,
b
s

Fig. 1. Proposed microgrid system architecture that consists of generation facilities, traditional consumers,
and prosumers that are equipped with solar rooftop panels and energy storage and deep reinforcement
learning agents. Grid and prosumers are equipped with deep reinforcement learning agents to dynamically
adjust their policies in terms of buy/sell prices and power injection.
management for a microgrid with large-scale rooftop PV panels and energy storage system. Table 1
compares our work with the previous related works.
3
MICROGRID MODEL AND PROBLEM FORMULATION
The envisioned microgrid model is shown in Figure 1. On the end-user side, the microgrid consists of
regular consumers as well as prosumers that are equipped with PV panels, battery, and an intelligent
agent. The presence of consumers ensure that the microgrid always has energy deficiency. The
conventional generation units are connected to the microgrid to meet the deficiency. The base
generation units have low cost for the service provider but if their capacity is not enough, the
reserve and the more expensive generation facilities will be dispatched to meet the real-time
microgrid demand [33]. Without loss of generality, this paper forgoes the ramp rate constraints of
the generation facilities. The agent decides on whether to consume the excess energy generated by
the PV system, store it in the battery, or sell it to the grid. On the other side, the SP is responsible
4


---

Page 5

---

for dispatching power to the loads from various generation facilities, including distributed energy
resources of prosumers.
In this paper, distributed energy management and demand response optimization problems
are defined for the SP and prosumers, respectively. On the grid side, the SP is engaged in energy
management with the objective of improving its own profit. On the household side, prosumers
engage in DR with the goal of reducing their daily electricity bill. The complex interactions between
the two sides denote the joint DEM-DR approach proposed in this paper.
Service Provider Energy Distribution Model: In the presence of prosumers, the DEM problem
of the microgrid evolves into a much more complex problem since the prosumers also appear as
generation facilities in certain time periods due to injection of power into the grid. Hence, in this
paper, the DEM formulation is defined as follows ,
max
𝜌𝑏
Ψ𝐺(𝑇) = R𝐺(𝑇) −


𝑁𝑔
∑︁
𝑖=1
F𝐺𝑖(𝑇) +
𝑁𝑝
∑︁
𝑗=1
F𝐻𝑗(𝑇)


(1)
Subject to:
𝑁𝑔
∑︁
𝑖=1
F𝐺𝑖(𝑇) =
𝑁𝑖
∑︁
𝑖=1
F𝐵𝑖(𝑇) +
𝑁𝑟
∑︁
𝑖=1
F𝑅𝑖(𝑇),
(2)
R𝐺(𝑇) =
𝑇
∫
0
𝑃𝐷(𝑡).𝜌𝑠(𝑡)𝑑𝑡,
(3)
F𝐻𝑗(𝑇) =
𝑇
∫
0
𝑃𝐻𝑗(𝑡).𝜌𝑏(𝑡)𝑑𝑡
for PHj (t) ≥0,
(4)
𝑃𝐷(𝑡) =
𝑁𝑔
∑︁
𝑖=1
(𝑃𝐺𝑖(𝑡) −𝑃𝑙𝑜𝑠𝑠𝑖(𝑡)) +
𝑁𝑝
∑︁
𝑗=1
𝑃𝐻𝑗(𝑡),
(5)
𝑃𝑙𝑜𝑠𝑠𝑖= 𝛽𝑖× 𝑃2
𝐺𝑖(𝑡),
(6)
𝑃min
𝐺𝑖
≤𝑃𝐺𝑖(𝑡) ≤𝑃max
𝐺𝑖
for 𝑖= 1, 2, ..., 𝑁𝑔,
(7)
where Ψ𝐺(𝑇) denotes the SP profit over a time horizon of 𝑇, and R𝐺(𝑇) is SP revenue as a result
of selling electricity to the loads, which is calculated by Equation (3) where 𝑃𝐷(𝑡) and 𝜌𝑠(𝑡)
denote the total system demand and electricity sell price at any given time, respectively. F𝐺𝑖(𝑇)
is the cost of generation unit 𝑖defined as the quadratic function of 𝑃𝐺𝑖, which means F𝐺𝑖(𝑃𝐺𝑖) =
𝑎𝑖𝑃2
𝐺𝑖+ 𝑏𝑖𝑃𝐺𝑖+ 𝑐𝑖where 𝑎𝑖, 𝑏𝑖, and 𝑐𝑖are fitting parameters and 𝑃𝐺𝑖is the amount of power
purchased from generation unit 𝑖[34]. This cost consists of the cost of base generation units F𝐵𝑖(𝑇)
and cost of reserve generation units F𝑅𝑖(𝑇) in Equation (2) where 𝑁𝑖and 𝑁𝑟are the number of base
and reserve generation facilities, respectively. 𝑁𝑔is the number of all generation facilities. If the
power demand exceeds the amount of base generation, the overall cost will be significantly higher
because procuring reserve power is more costly. F𝐻𝑗(𝑇) is the cost of buying electricity from the
𝑗𝑡ℎprosumer and calculated by Equation (4) where 𝑃𝐻𝑗(𝑡) and 𝜌𝑏(𝑡) denote the power injected by
the 𝑗𝑡ℎprosumer and electricity buy price, respectively. Equation (5) illustrates the total generation
and total demand power balance requirement, which needs to be maintained at any given time slot
𝑡. 𝑁𝑝and 𝑁𝑐denote the number of prosumers and consumers, respectively. 𝑃𝑙𝑜𝑠𝑠𝑖denotes the losses
induced by generation unit 𝑖, where 𝛽𝑖is the loss coefficient [35]. In addition, the power output of
each generation unit must not exceed its operation limits, which are described in Equation (7).
5


---

Page 6

---

The SP’s goal is to maximize its profit. To do so, the SP dynamically changes the buy price to
incentivize the prosumers to sell their excess energy to the grid, especially during the peak demand
hours. Hence, the control variable in DEM problem is the buy price 𝜌𝑏(𝑡).
Prosumer Side Demand Response Model: The objective of the prosumers is to minimize
their daily electricity bill by engaging in DR as a response to the dynamic buy price controlled by
the SP. Therefore, the prosumer side profit maximization is formulated as follows,
max
𝑃𝑏𝑗
Ψ𝐻𝑗(𝑇) = F𝐻𝑗(𝑇) + 1{𝑃𝐻𝑗(𝑡)<0} × C𝐻𝑗(𝑇)
(8)
Subject to:
C𝐻𝑗(𝑇) =
𝑇
∫
0
𝑃𝐻𝑗(𝑡).𝜌𝑠(𝑡)𝑑𝑡
for PHj (t) < 0,
(9)
F𝐻𝑗(𝑇) =
𝑇
∫
0
𝑃𝐻𝑗(𝑡).𝜌𝑏(𝑡)𝑑𝑡
for PHj(t) ≥0,
𝑃𝐻𝑗(𝑡) = 𝑃𝑃𝑉𝑗(𝑡) −𝑃𝑏𝑗(𝑡) −𝑃𝐶𝑗(𝑡),
(10)
𝑆𝑜𝐶min
𝑏𝑗
≤
1
𝐶𝑏𝑗
𝑡
∫
0
𝑃𝑏𝑗(𝜏)𝑑𝜏+ 𝑆𝑜𝐶𝑏𝑗(0) ≤𝑆𝑜𝐶max
𝑏𝑗,
(11)
𝑃max, dis
𝑏𝑗
≤𝑃𝑏𝑗(𝑡) ≤𝑃max, charge
𝑏𝑗
,
(12)
0 ≤𝑃𝑃𝑉𝑗(𝑡) ≤𝑃max
𝑃𝑉𝑗,
(13)
𝑃𝐻𝑗(𝑡)
 ≤𝑃max
𝐻𝑗,
(14)
𝑆𝑜𝐶𝑏𝑗(0),
𝑆𝑜𝐶min
𝑏𝑗,
𝑃max
𝐻𝑗
≥0,
where Ψ𝐻𝑗(𝑇) is the profit of the 𝑗𝑡ℎprosumer and 𝐶𝐻𝑗(𝑇) is the cost of buying electricity from the
grid over the time horizon 𝑇, which is described by Equation (9). F𝐻𝑗(𝑇) describes the prosumer 𝑗
revenue as a result of selling power to the grid and is calculated by Equation (4). Each prosumer has
an internal household-scale power system with a power balance equation of its own that needs to
be satisfied at all times. This is formulated by Equation (10) where 𝑃𝑃𝑉𝑗, 𝑃𝑏𝑗and 𝑃𝐶𝑗are the amount
of PV generation, battery charging/discharging power, and power consumption of the 𝑗𝑡ℎprosumer,
respectively. According to Equation (10), 𝑃𝐻𝑗can take a positive or negative value depending
on the amount of PV generation and battery charge or discharge action. A positive (negative)
value means the prosumer 𝑗injects (purchases) power to (from) the grid. Hence, 1{𝑃𝐻𝑗(𝑡)<0} is
one/zero when the injected power from prosumer 𝑗is negative/positive. The state of charge of each
prosumer battery should be maintained within a safe operational range as illustrated in Equation
(11) where 𝐶𝑏𝑗is the nominal battery capacity and 𝑆𝑜𝐶𝑏𝑗(0) represents the initial state of charge of
the battery. 𝑆𝑜𝐶min
𝑏𝑗
and 𝑆𝑜𝐶max
𝑏𝑗
are the lowest and highest allowable state of charge for the battery,
respectively. Furthermore, the charging and discharging power of the battery is limited as Equation
(12), where 𝑃max, charge
𝑏𝑗
and 𝑃max, dis
𝑏𝑗
are the maximum charge/discharge power ratings of the battery.
The constraint in Equation (13) is imposed by the physical limitations of the size of the PV system
and shows that the amount of PV generation is limited by the 𝑃max
𝑃𝑉𝑗. Dynamic power injection into
the grid might cause instability in some cases. Thus, the maximum allowable power injection is
limited by Equation (14).
6


---

Page 7

---

Fig. 2. Implemented Reinforcement Learning framework
In this paper, the formulated DR method is different from the conventional time-based DR, such
as Real-Time Pricing (RTP) methods [25]. Conventionally, RTP approaches rely on dynamically
changing the electricity sell price to motivate the customers to alter their energy use profile, while
the proposed DEM-DR algorithm relies on dynamically changing the buy price instead of the sell
price. This potentially incentivizes prosumers to participate in the program without any customer
dissatisfaction. At any given time slot 𝑡, both aforementioned optimization problems must be solved
at the same time. Dynamic SP pricing scheme in DEM-DR problem reinforces the need to implement
the optimization problems in short intervals (e.g., 15 minutes).
4
REINFORCEMENT LEARNING FOR DEM AND DR
Reinforcement Learning (RL) is a model-free machine learning technique that trains an agent to
take optimal actions through repeated interactions with an environment. The general RL framework
consists of a set of states S, a set of actions A, a reward function 𝑅, and probability of transition
between the states. The policy 𝜋is a mapping from the states of the environment (𝑠𝑡) to the actions
(𝑎𝑡), i.e., 𝜋: S →A. The agent’s ultimate goal is to learn which action 𝑎𝑡∈A to take at each time
instance 𝑡to maximize its cumulative reward over time. The action 𝑎𝑡results in reward 𝑟𝑡, and the
environment transitions from the state 𝑠𝑡to 𝑠𝑡+1 ∈S.
In this section, we use 𝑡as superscript to denote discrete time slots. It should be noted that there
is no interaction between the prosumers, such that their goals are to maximize their local profit
regardless of other prosumers’ performance.
4.1
Decision-Making Problem Formulation
In order to tackle the optimization problems in Section 3, we leverage a multi-agent DRL approach
such that we define agent for the grid side SP and agents for the prosumer side with PV and battery
storage capabilities. The SPA is representative of the service provider agent, while PA𝑗denotes
the 𝑗𝑡ℎprosumer agent. Each agent observes the environment and subsequently takes an action,
receiving a reward commensurate with the merit of the action. The agents will receive a reward
through their action selection, which is profit maximization for SPA and electricity bill reduction
for PA. Figure 2 graphically demonstrates the interaction between the SPA and PA agent with the
environment, their observation, and the action for each agent.
4.1.1
Service Provider Agent. The SPA observes the cost of buying electricity (base and reserve
generation) from 𝑁𝑔generation facilities at time slot 𝑡, which is denoted by F𝑡
𝐺= [F𝑡
𝐺1, F𝑡
𝐺1, ..., F𝑡
𝐺𝑁𝑔].
In addition, the SPA observes the cost of buying electricity from 𝑁𝑝prosumers denoted by
F𝑡
𝐻= [F𝑡
𝐻1, F𝑡
𝐻1, ..., F𝑡
𝐻𝑁𝑝], and the total power demand of the loads 𝑃𝑡
𝐷at the time slot 𝑡. Hence,
environment states 𝑠𝑡
𝑆𝑃𝐴= {F𝑡
𝐺, F𝑡
𝐻, 𝑃𝑡
𝐷} ∈S𝑆𝑃𝐴are observable by the SPA. Subsequently, the SPA
7


---

Page 8

---

Fig. 3. Timeline of interaction between the SPA and PA. At each time slot 𝑡, the SPA dynamically determines
the buy price in Step 2 (based on collected information in Step 1), and the PA decides on injected power and
changing the battery state of charge in Step 3.
takes an action by adjusting the electricity buy price denoted by 𝑎𝑡
𝑆𝑃𝐴= 𝜌𝑡
𝑏∈A𝑆𝑃𝐴, where A𝑆𝑃𝐴
is the finite set of available actions for SPA, i.e., all the possible buy prices.
The SPA reward function is defined based on the grid profit,
𝑟𝑡
𝑆𝑃𝐴= 𝑃𝑡
𝐷× 𝜌𝑡
𝑠−
𝑁𝑔
∑︁
𝑖=1
F𝑡
𝐺𝑖−
𝑁𝑝
∑︁
𝑗=1
1{𝑃𝐻𝑗(𝑡) ≥0} × 𝑃𝑡
𝐻𝑗× 𝜌𝑡
𝑏,
(15)
where 𝑟𝑡
𝑃𝑆𝐴is the SPA reward at time slot t. The value of F𝑡
𝐺𝑖is obtained using the incremental
cost curve of the 𝑖𝑡ℎgeneration facility. Given the definition of the immediate reward, the ultimate
goal for the SPA is to maximize the cumulative reward 𝑅𝑡
𝑆𝑃𝐴= Í∞
𝑘=0 𝛾𝑘𝑟𝑡+𝑘+1
SPA
over an infinite time
horizon known as expected return, where 0 ≤𝛾≤1 is the discount factor.
4.1.2
Prosumer Agent. 𝑃𝐴𝑗observes its own local parameters at each time slot 𝑡including power
consumption 𝑃𝑡
𝐶𝑗, state of charge of the battery 𝑆𝑜𝐶𝑡
𝑗, and the PV generation 𝑃𝑡
𝑃𝑉𝑗, as well as the
electricity buy price 𝜌𝑡
𝑏which is the result of SPA action. Hence 𝑠𝑡
𝑃𝐴𝑗= {𝑃𝑡
𝐶𝑗,𝑆𝑜𝐶𝑡
𝑗, 𝑃𝑡
𝑃𝑉𝑗, 𝜌𝑡
𝑏} ∈S𝑃𝐴𝑗.
Subsequently, the charge/discharge command to the energy storage in prosumer 𝑗is the action
determined by 𝑃𝐴𝑗, which is shown by 𝑎𝑡
𝑃𝐴𝑗= 𝑃𝑡
𝑏𝑗∈A𝑃𝐴𝑗. In this case, A𝑃𝐴𝑗is the finite set of
available actions to 𝑃𝐴𝑗. The reward function for the prosumer agents is defined as,
𝑟𝑡
𝑃𝐴𝑗= 1{𝑃𝐻𝑗(𝑡) ≥0} × 𝑃𝑡
𝐻𝑗× 𝜌𝑡
𝑏+ 1{𝑃𝐻𝑗(𝑡)<0} × 𝑃𝑡
𝐻𝑗× 𝜌𝑡
𝑠.
(16)
Similar to the SPA, the 𝑃𝐴𝑗tries to maximize its infinite-horizon accumulative reward 𝑅𝑡
𝑃𝐴𝑗=
Í∞
𝑘=0 ˜𝛾𝑘
𝑗𝑟𝑡+𝑘+1
𝑃𝐴𝑗, where 0 ≤˜𝛾𝑗≤1 is the discount rate for 𝑃𝐴𝑗.
The timeline of interactions between the SPA and PA agents is illustrated in Figure 3. At a given
time slot 𝑡, the SPA makes a decision first by determining the market electricity buy price (𝑎𝑡
𝑆𝑃𝐴)
based on the complete information of the prices of electricity generation facilities and the electricity
demand from the prosumers’ agents. The SPA then receives a reward (𝑟𝑡
𝑆𝑃𝐴) for taking the action.
Next, the PAs observe the sell and buy price, and make the decision (𝑎𝑡
𝑃𝐴𝑗) in terms of changing the
battery state of charge and receive a reward (𝑟𝑡
𝑃𝐴𝑗) for that decision. Finally, the PAs inform the
SPA about the demand and the injected power.
8


---

Page 9

---

Fig. 4. Retail prices for the last two days of the simulation.
4.2
Deep Q-Network Learning
A systematic review of Deep Learning (DL) methods applied to the smart grid is provided in [36].
Deep Reinforcement Learning is the combination of Deep Neural Networks (DNNs) and RL. In
general, RL solutions can be divided into value- and policy-based algorithms. The value-based
solutions are straight-forward to implement. The main value-based method is Q-learning. Due to
the high dimensionality nature of the problem Deep Q-Network (DQN) agents, which can handle
a large state space, are used to solve their respective Markov Decision Processes (MDPs) and
maximize their accumulative rewards. In addition, since the action spaces of SPA and PAs are
discrete, the DQN can be used for solving this problem. The transition formula of Q-learning is,
𝑄(𝑠𝑡,𝑎𝑡) ←𝑄(𝑠𝑡,𝑎𝑡) + 𝛼[𝑟𝑡+1 + 𝛾max
𝑎𝑡+1 𝑄(𝑠𝑡+1,𝑎𝑡+1) −𝑄(𝑠𝑡,𝑎𝑡)] ,
(17)
where 𝛼is the learning rate. Additionally,𝛾is the discount factor, with a range of 0 to 1. If𝛾is closer
to zero, the agent prioritizes the immediate reward over long-term rewards. On the other hand,
if 𝛾is closer to one, the agent places greater weights over the future rewards compared with the
immediate reward. The estimated Q-values are used to find the optimal policy that maximizes the
accumulative rewards. An𝜖-greedy strategy is used to balance between exploration and exploitation,
i.e.,
𝑎𝑡=
(
arg max
𝑎𝑡
𝐸

𝑄 𝑠𝑡,𝑎𝑡
with probability 1 −𝜖,
random action
with probability 𝜖,
where the probability of random action is 𝜖that decays from 1 to 0.01 over the training episodes in
our simulations.
5
NUMERICAL RESULTS
In this study, we leverage the grid and prosumers’ agents to implement the proposed DEM-DR
scheme referred to as Agent-Based scheme. To demonstrate the efficacy of the proposed approach,
we compare it with the Conventional approach, which simply injects the excess power to the grid
when the battery is fully charged. The simulation parameters for DQN agents are tabulated in
Table 2. As previously mentioned, the set of buy prices is defined as A𝑆𝑃𝐴, representing the action
space of the service provider agent. We designate the action space for prosumers as follows,
𝑃𝑡
𝑏𝑗=


𝑃max,charge
𝑏𝑗
Charge action,
0
No charge or discharge action,
𝑃max,dis
𝑏𝑗
Discharge action.
(18)
We compare the Agent-Based with the Conventional scheme through two scenarios: (1) A small-
scale setting with 5 prosumers in which we demonstrate the agents’ effectiveness in interacting
9


---

Page 10

---

Table 2. DQN Hyperparameters and Simulation Parameters.
Hyperparameters
Value for 𝑆𝑃𝐴
Value for 𝑃𝐴𝑗
Batch size
64
64
Discount factor
𝛾=[0.95-0.99]
˜𝛾𝑗=[0.95-0.99]
Learning rate
𝛼=1e-3
˜𝛼𝑗=1e-3
Soft update interpolation
1e-5
1e-5
Hidden Layer-nodes
1-[1000]
2-[1000,1000]
Activation
Tanh
Tanh
Optimizer
Adam
Adam
Simulation Parameter
Description
Value
𝑃max
𝑃𝑉𝑗
Max. PV Generation
[2-6] kW
𝑃max,charge
𝑏𝑗
/𝑃max,dis
𝑏𝑗
Max. allowable charge/discharge
2/-2.5 kW
𝑃max
𝐻𝑗
Max. allowable power injection
10 kW
𝑆𝑜𝐶max
𝑏𝑗
Max. state of charge
0.9 × 𝐶𝑏𝑗
𝑆𝑜𝐶min
𝑏𝑗
Min. state of charge
0.1 × 𝐶𝑏𝑗
𝐶𝑏𝑗
Energy storage capacity
[8-15] kWh
𝜙𝑗(0)
Initial state of charge
[1-4] kWh
𝜌𝑠
Sell price [before 11am, after 11am]
[0.05, 0.095] $/kWh
A𝑆𝑃𝐴
Buy price set for Agent-Based scenario
{0.05, 0.06, 0.07,
0.08, 0.09, 0.1}$/kWh
𝜌𝑡
𝑏
Buy price for Conventional scenario
0.06 $/kWh
h
𝑃min
𝐺1 , 𝑃max
𝐺1
i
Limitation of base generation
[5, 45] kW
h
𝑃min
𝐺2 , 𝑃max
𝐺2
i
Limitation of reserve generation
[0, 100] kW
[𝛽1, 𝛽2]
Transmission loss coefficient of two generators
[0.0002, 0.0002]
Fig. 5. (a) Average daily bill comparison of the Conventional vs. Agent-Based schemes in a small-scale
microgrid with 5 prosumers. (b) Performance comparison of the Conventional vs. Agent-Based scenarios in
terms of grid profit and reserve unit utilization.
with the energy marketplace environment, and improvements made to both SP and prosumers’
economic benefits. (2) A medium-scale setting with 50 prosumers wherein we investigate the
system’s reliability and scalability by simulating a larger-scale microgrid. We implemented our
DQN agents using Python3 with PyTorch 1.5.0. All simulations were performed via episodic
updating across 10,000 episodes, each of which represents a 24-h cycle. A cycle consists of 96
iterations (sampling time is 15 minutes).
5.1
Scenario I: Small-Scale Simulation with 5 Prosumers
The first scenario studies the microgrid in Figure 1 consisting of two generation facilities (a base
plant and a spinning reserve) managed by one distribution SP, five prosumers, and one non-
generational consumer. The DQN agents are implemented for the SP and the prosumers. The
operational parameters of the five prosumers and the single consumer are tabulated in Table 2. The
10


---

Page 11

---

utilized consumption and generation profiles for the prosumers mimic real-world trends reported
by California ISO [37] to exemplify real-world operation.
5.1.1
Macroscopic Evaluation of Prosumers and Grid Benefits. As reported in Table 2, the
sell price for both Conventional and Agent-Based scenarios takes two values depending on the time
of a day. On the other hand, the buy price is constant during a day for the Conventional scenario,
while in the Agent-Based scenario the buy price is dynamically determined by the SPA. Figure 4
compares the dynamic pricing achieved by the Agent-Based approach vs. the fixed-pricing of the
Conventional scheme. The results shown in Figure 5 (a) compares the average daily bill of prosumers
when utilizing the two approaches. As pictured, the average daily bills have decreased by 22.1%,
8.2%, 10.9%, 48.8%, and 15.9% for prosumer 1 to prosumer 5, respectively. Figure 5 (b) on the other
hand, illustrates the moving average of SP profit and reserve generation consumption. According to
these results, the Agent-Based approach is offering an 25.7% increase in the SP profit, made possible
by a 16% reduction in reserve power consumption, compared to the conventional approach. This
further demonstrates that the proposed Agent-Based approach is capable of providing a higher
profit for the SP while offering greater economic benefit for the prosumers, warranting a win-win
scenario for the grid and prosumers.
5.1.2
Microscopic Evaluation of Prosumers’ Behavior. Figure 6 illustrates the temporal
profiles of several internal states of all five prosumers over the course of the last two simulated days
for the Agent-Based and Conventional approaches. These graphs provide an intuitive interpretation
of how each demand-side participators respond to the DR scheme in real-time. As pictured, using
the Conventional method, the households’ PV systems can charge their batteries only when their
generation is more than consumption, while only being able to sell their excess generation when
their batteries are fully charged.
Observations on prosumers 1 and 2: As demonstrated in Figure 6 (a) and (b), the generated
power by prosumers 1 and 2 is less than their consumption (except for a very short period of time
for prosumer 2). Therefore, throughout simulation of the Conventional approach, their batteries
are never charging, denying them potential economic benefits otherwise possible by incorporating
the energy storage system, and prohibiting them from participating in grid support during peak
demand hours. On the other hand, using the Agent-Based approach, the prosumer batteries are
charging during off-peak-low-price hours (i.e., beginning of the day), and prosumers are engaging
in grid support during peak demand hours. Although charging the battery at the beginning of
the day incurs some cost for prosumers, it eventually provides higher economic benefits to them
through selling the energy back to the grid at a higher price, while assisting with grid power
balance during peak demand hours. In other words, the stored energy in prosumer 1 and 2 batteries
is dispatched to the grid by properly incentivizing them to participate in DR.
Observations on prosumer 3: According to consumption and generation profiles for prosumer
3 illustrated in Figure 6 (c), only a small amount of excess PV generation during a few hours is
discernible. In this case, the results demonstrate that deploying the Agent-Based algorithm yields a
higher SoC compared with the Conventional method. This is because the RL agent learns to charge
the battery at the beginning of the day when the selling price by the grid is low, and to support the
grid in the afternoon when the buy price is high.
Observations on prosumers 4 and 5: According to Figure 6 (d) and (e), these prosumers have
excess PV generation during peak sun hours (e.g., around noon). The Conventional scheme fully
charges the batteries of these prosumers during the peak sun hours, while the Agent-Based scheme
charges the batteries starting from the beginning of the day when the sell price is low. As a result,
11


---

Page 12

---

Fig. 6. Generation and consumption profiles along with the State-of-Charge (SoC) for 5 prosumers.
these prosumers can sell their excess power during sun hours, rather than storing it, at even a
higher price rate than the Conventional scheme could, after fully charging the batteries.
5.1.3
Effect of Battery Size. Figure 7 demonstrates the prosumers’ daily bill reduction and
grid daily profit achieved by increasing the size of prosumer batteries from 2kWh to 25kWh. As
pictured, the daily bill for all five prosumers decreases as the battery capacities are increased.
Similarly, the grid daily profit also increases by increasing the battery capacities. Nevertheless, the
improvements start to level down as the battery capacities approach to around 15kWh. Based on
this observation, we use batteries with capacities in the range of 8kWh to 15kWh for all prosumers
in the simulations.
Figure 8 demonstrates the impact of transmission losses on the total grid profit. In particular, the
results show that as the value of transmission loss 𝛽increases, the service provider profit decreases
since it has to purchase more power to meet the total demand at any given time.
5.2
Scenario II: Medium Scale Simulation with 50 Prosumers
The second scenario studies a medium scale microgrid with 50 prosumers and 𝑁𝑐= 40 non-
generational consumers. In this scenario, the proposed method’s scalability is the main criteria
under investigation. The average daily electricity bills for 50 prosumers each with a distinct
consumption profile, while using Conventional and Agent-Based approaches are illustrated in
12


---

Page 13

---

(a)
(b)
Fig. 7. (a) Effect of increasing battery capacity on the prosumers’ average daily bill reduction in small-scale
simulation. (b) Effect of increasing battery capacity on the grid profit improvement in small-scale simulation.
Fig. 8. Impact of transmission losses on total grid profit.
Figure 9(a). According to this figure, the average daily bill is reduced for all 50 prosumers in the
Agent-Based scenario. Figure 9(b) represents the probability distribution function of the average
daily bill for 50 prosumer data points. This figure illustrates an average bill of $1.96 for Conventional
method, vs. $1.74 for Agent-Based method, amounting to around 12% bill reduction for a 24 hour
billing cycle.
Figure 9 (c) compares the accumulative grid profit and reserve power utilization of the Conven-
tional and Agent-Based scenarios in our medium scale microgrid. As pictured, the Agent-Based
method provides around 4.3% higher profit over a 24-hour period. This improvement is due to the
fact that the SPA and PAs learn how to dispatch the batteries’ power to rely on the prosumers’
PV generation, rather than using the costly reserve power. Moreover, properly incentivizing the
prosumers to dispatch their stored energy has a positive impact on shaving the peak load demand
of the grid, as compared in Figure 10 over a 24-hour period. As pictured, the Agent-Based approach
shifts the demand at the peak hours between 18pm to 24pm to early morning hours before 6am.
6
CONCLUSION
In this paper, we propose a Deep Reinforcement Learning (DRL) framework for energy manage-
ment and demand response in prosumer dominated microgrids. The service provider DRL agent
dynamically changes the electricity buy price and determines the direction and amount of power
flow according to the household’s load demand. Further, the prosumers DRL agent controls the
13


---

Page 14

---

Datapoint for 
prosumer number 30.
(b)
(a)
(c)
Fig. 9. Performance of the Conventional vs. Agent-Based scenarios in the medium scale microgrid with 50
prosumers. (a) Average daily bills of prosumers; (b) Distribution of average daily bills; (c) Performance com-
parison of the Conventional vs. Agent-Based scenarios in terms of grid profit and reserve power consumption
with 50 prosumers.
Fig. 10. Average net power comparison for the Conventional vs. Agent-Based scenarios during a 24-hour
period.
battery charge and discharge rate and amount of power injection into the grid. These DRL agents
collectively provide a dynamic decision-making framework. Our simulation results demonstrate
that the proposed framework provides higher economic benefits for both power grid and prosumers.
Specifically, properly incentivizing prosumers through dynamic pricing and leveraging the capacity
of distributed battery resources result in: (i) reduced average daily bills for prosumers, (ii) enhanced
profits for the grid by decreasing the reserve generation power demand, and (iii) reduced net power
demands during peak hours. The proposed framework can be extended by including other external
observations such as weather conditions, or investigating the performance of DRL agents under
peer-to-peer energy sharing across prosumers.
REFERENCES
[1] S. Grijalva and M. U. Tariq. Prosumer-based smart grid architecture enables a flat, sustainable electricity industry. In
ISGT 2011, 2011. doi: 10.1109/ISGT.2011.5759167.
[2] Nian Liu, Xinghuo Yu, Cheng Wang, and Jinjian Wang. Energy sharing management for microgrids with pv prosumers:
A stackelberg game approach. IEEE Trans. on Industrial Informatics, 13(3):1088–1098, 2017. doi: 10.1109/TII.2017.2654302.
[3] M Khoshjahan, R Baembitov, and M Kezunovic. Impacts of weather-related outages on der participation in the
wholesale market energy and ancillary services. In 2021 CIGRE Grid of the Future Symposium, Providence, Rhode Island,
14


---

Page 15

---

USA, 2021.
[4] Leong Kit Gan, PengFei Zhang, Jaehwa Lee, Michael A Osborne, and David A Howey. Data-driven energy management
system with gaussian process forecasting and mpc for interconnected microgrids. IEEE Trans. on Sustainable Energy,
12(1):695–704, 2020.
[5] Nikolaos G. Paterakis, Ozan Erdinç, Anastasios G. Bakirtzis, and João P. S. Catalão. Optimal household appliances
scheduling under day-ahead pricing and load-shaping demand response strategies. IEEE Transactions on Industrial
Informatics, 11(6):1509–1519, 2015. doi: 10.1109/TII.2015.2438534.
[6] Hesam Farzaneh, Mohammad Shokri, Hamed Kebriaei, and Farrokh Aminifar. Robust energy management of residential
nanogrids via decentralized mean field control. IEEE Trans. on Sustainable Energy, 11(3):1995–2002, 2019.
[7] Wann-Jiun Ma, Jianhui Wang, Vijay Gupta, and Chen Chen. Distributed energy management for networked microgrids
using online admm with regret. IEEE Transactions on Smart Grid, 9(2):847–856, 2018. doi: 10.1109/TSG.2016.2569604.
[8] Marina Dorokhova, Yann Martinson, Christophe Ballif, and Nicolas Wyrsch. Deep reinforcement learning control of
electric vehicle charging in the presence of photovoltaic generation. Applied Energy, 301:117504, 2021.
[9] Jianhong Wang, Wangkun Xu, Yunjie Gu, Wenbin Song, and Tim Green. Multi-agent reinforcement learning for active
voltage control on power distribution networks. Advances in Neural Information Processing Systems, 34, 2021.
[10] Bala Suraj Pedasingu, Easwar Subramanian, Yogesh Bichpuriya, Venkatesh Sarangan, and Nidhisha Mahilong. Bidding
strategy for two-sided electricity markets: A reinforcement learning based framework. In Proceedings of the 7th ACM
International Conference on Systems for Energy-Efficient Buildings, Cities, and Transportation, pages 110–119, 2020.
[11] Esmat Samadi, Ali Badri, and Reza Ebrahimpour. Decentralized multi-agent based energy management of microgrid
using reinforcement learning. International Journal of Electrical Power & Energy Systems, 122:106211, 2020.
[12] José R Vázquez-Canteli and Zoltán Nagy. Reinforcement learning for demand response: A review of algorithms and
modeling techniques. Applied energy, 235:1072–1089, 2019.
[13] Hanchen Xu, Hongbo Sun, Daniel Nikovski, Shoichi Kitamura, Kazuyuki Mori, and Hiroyuki Hashimoto. Deep
reinforcement learning for joint bidding and pricing of load serving entity. IEEE Trans. on Smart Grid, 10(6), 2019.
[14] Yanchang Liang, Chunlin Guo, Zhaohao Ding, and Huichun Hua. Agent-based modeling in electricity market using
deep deterministic policy gradient algorithm. IEEE Trans. on Power Systems, 35(6):4180–4192, 2020.
[15] Elham Foruzan, Leen-Kiat Soh, and Sohrab Asgarpoor. Reinforcement learning approach for optimal distributed
energy management in a microgrid. IEEE Trans. on Power Systems, 33(5):5749–5758, 2018.
[16] Aicha Dridi, Hossam Afifi, Hassine Moungla, and Jordi Badosa. A novel deep reinforcement approach for iiot microgrid
energy management systems. IEEE Transactions on Green Communications and Networking, 2021.
[17] Biao Wang, Yan Li, Weiyu Ming, and Shaorong Wang. Deep reinforcement learning method for demand response
management of interruptible load. IEEE Trans. on Smart Grid, 2020.
[18] Hwei-Ming Chung, Sabita Maharjan, Yan Zhang, and Frank Eliassen. Distributed deep reinforcement learning for
intelligent load scheduling in residential smart grid. IEEE Trans. on Industrial Informatics, 2020.
[19] Qinglai Wei, Zehua Liao, and Guang Shi. Generalized actor-critic learning optimal control in smart home energy
management. IEEE Trans. on Industrial Informatics, 17(10):6614–6623, 2021. doi: 10.1109/TII.2020.3042631.
[20] F. Ruelens, B. J. Claessens, S. Vandael, B. De Schutter, R. Babuška, and R. Belmans. Residential demand response of
thermostatically controlled loads using batch reinforcement learning. IEEE Trans. on Smart Grid, 8(5):2149–2159, 2017.
doi: 10.1109/TSG.2016.2517211.
[21] Xu Xu, Youwei Jia, Yan Xu, Zhao Xu, Songjian Chai, and Chun Sing Lai. A multi-agent reinforcement learning based
data-driven method for home energy management. IEEE Trans. on Smart Grid, 2020.
[22] Jianwen Sun, Yan Zheng, Jianye Hao, Zhaopeng Meng, and Yang Liu. Continuous multiagent control using collective
behavior entropy for large-scale home energy management. In Proceedings of the AAAI Conference on Artificial
Intelligence, volume 34, pages 922–929, 2020.
[23] Yaodong Yang, Jianye Hao, Yan Zheng, and Chao Yu. Large-scale home energy management using entropy-based
collective multiagent deep reinforcement learning framework. In IJCAI, pages 630–636, 2019.
[24] Yujian Ye, Dawei Qiu, Jonathan Ward, Marcin Abram, and C Bessiere. Model-free real-time autonomous energy
management for a residential multi-carrier energy system: A deep reinforcement learning approach. In IJCAI, pages
339–346, 2020.
[25] Pedram Samadi, Hamed Mohsenian-Rad, Vincent WS Wong, and Robert Schober. Real-time pricing for demand
response based on stochastic approximation. IEEE Trans. on Smart Grid, 5(2):789–798, 2014.
[26] Liyan Jia and Lang Tong. Dynamic pricing and distributed energy management for demand response. IEEE Trans. on
Smart Grid, 7(2):1128–1136, 2016.
[27] Mengmeng Yu, Seung Ho Hong, Yuemin Ding, and Xun Ye. An incentive-based demand response (dr) model considering
composited dr resources. IEEE Trans. on Industrial Electronics, 66(2):1488–1498, 2018.
15


---

Page 16

---

[28] Amrit Paudel, Kalpesh Chaudhari, Chao Long, and Hoay Beng Gooi. Peer-to-peer energy trading in a prosumer-based
community microgrid: A game-theoretic model. IEEE Trans. on Industrial Electronics, 66(8), 2019. doi: 10.1109/TIE.
2018.2874578.
[29] Kaveh Dehghanpour, M Hashem Nehrir, John W Sheppard, and Nathan C Kelly. Agent-based modeling of retail
electrical energy markets with demand response. IEEE Trans. on Smart Grid, 9(4), 2016.
[30] Renzhi Lu and Seung Ho Hong. Incentive-based demand response for smart grid with reinforcement learning and
deep neural network. Applied energy, 236:937–949, 2019.
[31] B. Kim, Y. Zhang, M. van der Schaar, and J. Lee. Dynamic pricing and energy consumption scheduling with reinforce-
ment learning. IEEE Trans. on Smart Grid, 7(5):2187–2198, 2016.
[32] Renzhi Lu, Seung Ho Hong, and Xiongfeng Zhang. A dynamic pricing demand response algorithm for smart grid:
Reinforcement learning approach. Applied Energy, 220:220–230, 2018.
[33] Mostafa Goodarzi and Qifeng Li. Evaluate the capacity of electricity-driven water facilities in small communities as
virtual energy storage. Applied Energy, 309:118349, 2022.
[34] Weerakorn Ongsakul and Vo Ngoc Dieu. Artificial intelligence in power system optimization. Crc Press, 2019.
[35] Chengcheng Zhao, Jianping He, Peng Cheng, and Jiming Chen. Consensus-based energy management in smart grid with
transmission losses and directed communication. IEEE Trans. on Smart Grid, 8(5), 2017. doi: 10.1109/TSG.2015.2513772.
[36] Mohamed Massaoudi, Haitham Abu-Rub, Shady S Refaat, Ines Chihi, and Fakhreddine S Oueslati. Deep learning in
smart grid technology: A review of recent advancements and future prospects. IEEE Access, 9, 2021.
[37] California ISO. Current and forecasted demand. URL http://www.caiso.com/TodaysOutlook/Pages/default.aspx.
16
