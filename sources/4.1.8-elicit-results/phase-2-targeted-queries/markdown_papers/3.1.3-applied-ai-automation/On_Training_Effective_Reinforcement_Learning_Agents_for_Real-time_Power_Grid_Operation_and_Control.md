# On Training Effective Reinforcement Learning Agents for Real-time Power Grid Operation and Control

## Paper Metadata

- **Filename:** On Training Effective Reinforcement Learning Agents for Real-time Power Grid Operation and Control.pdf
- **DOI:** None
- **Authors:** Not available
- **Year:** Not available
- **Journal/Venue:** Not available
- **URL:** Not available
- **Extraction Date:** 2025-06-03T15:04:11.256781
- **Total Pages:** 8

## Abstract

Abstract not available from BibTeX metadata.

## Keywords

Keywords not available from BibTeX metadata.

---

## Full Text Content



### Page 1

On Training Effective Reinforcement Learning
Agents for Real-time Power Grid Operation and
Control
Ruisheng Diao∗
AI & System Analytics
GEIRI North America
San Jose, CA 95134
ruisheng.diao@geirina.net
Di Shi
AI & System Analytics
GEIRI North America
San Jose, CA
di.shi@geirina.net
Bei Zhang
AI & System Analytics
GEIRI North America
San Jose, CA
beizhangzl@gmail.com
Siqi Wang
AI & System Analytics
GEIRI North America
San Jose, CA
siqi.wang@gmail.com
Haifeng Li
System Operations
Jiangsu Electric Power Company
Nanjing, China
lhfcloud@163.com
Chunlei Xu
Power System Automation
Jiangsu Electric Power Company
Nanjing, China
chunleixu@js.sgcc.com.cn
Tu Lan
AI & System Analytics
GEIRI North America
San Jose, CA
lantusky2017@gmail.com
Desong Bian
AI & System Analytics
GEIRI North America
San Jose, CA
desong.bian@geirina.net
Jiajun Duan
AI & System Analytics
GEIRI North America
San Jose, CA
jiajun.duan@geirina.net
Abstract
Deriving fast and effectively coordinated control actions remains a grand challenge affecting the secure and economic operation of today’s large-scale power
grid. This paper presents a novel artiﬁcial intelligence (AI) based methodology to
achieve multi-objective real-time power grid control for real-world implementation.
State-of-the-art off-policy reinforcement learning (RL) algorithm, soft actor-critic
(SAC) is adopted to train AI agents with multi-thread ofﬂine training and periodic
online training for regulating voltages and transmission losses without violating
thermal constraints of lines. A software prototype was developed and deployed in
the control center of SGCC Jiangsu Electric Power Company that interacts with
their Energy Management System (EMS) every 5 minutes. Massive numerical
studies using actual power grid snapshots in the real-time environment verify the
effectiveness of the proposed approach. Well-trained SAC agents can learn to
∗Dr. Ruisheng Diao is with GEIRI North America as Deputy Department Head, AI & System Analytics,
leading the development of a number of AI-based applications in power systems (autonomous voltage control,
line ﬂow control, intelligent maintenance scheduling for power utilities and control centers). Cell phone:
(480)-414-7095, website: https://www.linkedin.com/in/ruisheng-diao-ph-d-pe-789a9655/
Workshop on machine learning for engineering modeling, simulation and design @ Neur IPS 2020
ar Xiv:2012.06458v1 [math.OC] 11 Dec 2020

---


### Page 2

provide effective and subsecond (<20 ms) control actions in regulating voltage
proﬁles and reducing transmission losses.
1
Introduction
Over recent years, the electricity sector has undergone signiﬁcant changes, with ever-increasing
penetration of intermittent energy resources, storage devices, and power electronics equipment
integrated into decades-old grid infrastructure, causing more stochastic and dynamic behavior that
affects the secure and economic operation of the grid. Various control measures exist to restore
the imbalance of active and reactive power to ensure voltage, frequency and line ﬂows operating
within their normal ranges. Compared to mature controllers that function well at local levels, deriving
system-wide optimal controls by coordinating many controllers for real-time operating conditions
while complying with all security constraints remains a grand challenge.
Such a control problem is known as security constrained AC optimal power ﬂow (AC OPF), where
control objectives can be minimization of total generation costs, total network losses, amount of
control actions or a combination of all while respecting physics and security constraints. Many prior
research efforts were proposed to solve the large-scale non-convex AC OPF problem considering
various constraints with mixed-integer variables, including nonlinear programming, quadratic programming, Lagrangian relaxation, interior point method and mixed-integer linear programming. A
comprehensive survey is conducted in [1] that summarizes the main challenges and state-of-the-art
techniques. In [2]-[3], semideﬁnite programming (SDP) relaxation-based methods are proposed
for solving the multi-objective OPF problem. In [4], the authors proposed a quasi-Newton method
using second-order information for solving real-time OPF problem. However, due to the non-convex
and complex nature of the problem (NP-Hard) and the need for accurate system-wide models in
real-time environment, deriving solutions for the AC OPF problem with all security constraints is very
challenging. Thus, relaxation of constraints and simpliﬁcations of system models, e.g., DC based
OPF, are typically used to obtain feasible and suboptimal solutions. In fact, nearly all today’s vendors’
tools adopt DC-based models for obtaining fast OPF solutions in power industry. To effectively deal
with the new challenges and derive fast OPF solutions, new approaches are much-needed [5].
Recent success of applying RL technologies in various control problems including game of GO,
self-driving cars and robotics provides a promising way of deriving instant control actions for
reaching feasible and suboptimal AC OPF solutions. Recently, RL-based algorithms were reported
for regulating voltage proﬁles [6] and transmission line ﬂows [7], load-frequency control [8], and
emergency control for enhancing transient voltage behavior [9]. In this paper, a novel method is
presented to perform multi-objective power grid control in real time, by adopting the state-of-the-art
off-policy RL algorithm, soft actor-critic, with superior performance in convergence and robustness
over other RL algorithms [10]. The novelty of this method includes: (1) the AC OPF control problem
is formulated as Markov Decision Process (MDP) where RL-based algorithms can be applied to
derive suboptimal solutions; (2) it provides a general and ﬂexible framework to include various types
of control objectives and constraints of a power grid when training AI agents; (3) once properly
trained, RL agents can provide subsecond control actions to regulate bus voltages and transmission
losses when sensing abnormal power system states, in case of abrupt changes in voltages and line
ﬂows; and (4) multi-threading-based training process of SAC agents with periodical model update is
developed to ensure long-term control effectiveness and mitigate the over-ﬁtting issue. The remainder
of this paper is organized as follows. Section 2 provides the proposed RL-based methodology for
deriving real-time control actions including architecture design, deﬁnition of RL components, and
implementation details in a control center. In Section 3, case studies are conducted on a city-level
power network for demonstrating the effectiveness of the proposed approach. Finally, conclusions
are drawn in Section 4 with future work identiﬁed.
2
Proposed Solution for Real-time Multi-objective Power Grid Control
Using Soft Actor-Critic
2.1
Problem Formulation
Without losing generality, this work mainly targets at deriving real-time corrective operational control
decisions for power grid operating conditions at an interval of 5 minutes in a control center. The
2

---


### Page 3

control objectives include regulating bus voltages within secure zones and minimizing transmission
losses while respecting power ﬂow equations and physical constraints, e.g., line ratings and limits of
generators. The mathematical formulation of the control problem is given below:
Objective function
:
minimize
X
i,j
Ploss(i, j), (i, j) ∈ΩL
(1)
Subject to
:
X
n∈Gi
P g
n −
X
n∈Di
P d
m −gi V 2
i =
X
j∈Bi
Pij(y)
(2)
X
n∈Gi
Qg
n −
X
n∈Di
Qd
m −bi V 2
i =
X
j∈Bi
Qij(y)
(3)
Pij(y) = gij V 2
i −Vi Vj(gij cos(θi −θj) + bij sin(θi −θj)), (i, j) ∈ΩL
(4)
Qij(y) = −V 2
i (bij0 + bij) −Vi Vj(gij sin(θi −θj) −bij cos(θi −θj)), (i, j) ∈ΩL
(5)
P min
n
≤Pn ≤P max
n
, n ∈G;
(6)
Qmin
n
≤Qn ≤Qmax
n
, n ∈G
(7)
V min
i
≤Vi ≤V max
i
, i ∈B
(8)
q
P 2
ij + Q2
ij ≤Smax
ij
, (i, j) ∈ΩL
(9)
where Ploss is power losses on transmission line connecting bus (or node) i and bus j; P g
n is active
power injection into bus n; P d
m is active power consumption at bus m; θi and Vi are voltage phage
angle and magnitude at bus i, in polar form, respectively. bij and gij are conductance and susceptance
of transmission line. Pij and Qij stand for active and reactive power on a transmission line. Eq. 2
through Eq. 5 represent power ﬂow equations, representing quasi-steady-state conditions of a power
grid, which need to be met all the time. Eq. 6 and Eq. 7 are active and reactive power output limits of
each generator, respectively. Eq. 8 and Eq. 9 specify bus voltage secure zones and line ﬂow limits to
be controlled, respectively.
2.2
Overall Flowchart of the Proposed Methodology
Deriving multi-objective real-time control actions respecting both equality and inequality constraints
shown in Eq. 1 through Eq. 9 can be formulated as a discrete-time stochastic control process, a.k.a.,
MDP. Among various RL techniques, the off-policy, SAC method is adopted because of its superior
performance in fast convergence and robustness, which maximizes the expected reward by exploring
as many control actions as possible, leading to a better chance of ﬁnding optimum. The detailed
algorithm description of SAC can be found in [10]. The main ﬂowchart of the proposed methodology
is depicted in Fig 1, including three key modules:
Module (a): Fig 1(a) provides the interaction process between the power grid simulation environment
(an AC power ﬂow solver satisfying Eq. 2 through Eq. 7) and the SAC agent. The environment
receives control actions, outputs the corresponding next system states and calculates the reward;
while the SAC agent receives states and reward before outputting control actions, in order to satisfy
Eq. 8, Eq. 9 and minimize the objective function, Eq. 1.
Module (b): Fig 1(b) shows the ofﬂine training process of an SAC agent. Representative power grid
operating snapshots are collected from EMS for preprocessing. System state variables are extracted
from those converged snapshots and fed into SAC agent training module, where neural networks are
used to establish direct mappings between system states and control actions. The controls are then
3

---


### Page 4

Figure 1: Main ﬂowchart and key function modules of the proposed methodology
veriﬁed by another AC power ﬂow solution to calculate reward values before updating SAC agent
weights for maximizing long-term expected reward and entropy.
Module (c): To ensure long-term effectiveness and robustness of SAC agent, multiple training
processes with different sets of hyperparameters are launched simultaneously, including several
ofﬂine training processes and one online training process (initialized by the best ofﬂine-trained
model), shown in Fig 1(c). The best-performing model selected from these processes is then used for
application in real-time environment.
2.3
Training Effective SAC Agents
Several key elements in training effective RL agents for multi-objective real-time power ﬂow control
are given below:
4

---


### Page 5

2.3.1
Episode, Terminating Conditions, Simulation Environment
Each episode is deﬁned as a quasi-steady-state operating snapshot, obtained from the EMS system at
an interval of 5 minutes. Termination condition of training episodes includes: i) no more voltage or
thermal violations with reduction of transmission losses reaching a threshold, e.g., 0.5%; ii) power
ﬂow calculation diverges; or iii) the maximum number of control iteration is reached. The power
grid simulation environment used in this work is the AC power ﬂow calculation program used by
system operators in a control center, which typically uses the Newton-Raphson method for obtaining
converged solution of system snapshots [11].
2.3.2
State Space
The state space is formed by including bus voltage magnitudes (V ), phase angles (θ), active and
reactive power on transmission lines (Pij and Qij), collected from real-time power grid snapshots in
the areas to be monitored and controlled. The batch normalization technique is applied to different
types of variables for maintaining consistency and improving agent training efﬁciency.
2.3.3
Reward Deﬁnition
The reward value at each control iteration when training SAC agent consider adopts the following
logic:
reward =







−(∆Poverflow)/10 −(∆Vviolation)/100,
if voltage or ﬂow violation
50 −∆Ploss ∗1000,
if ∆Ploss < 0
−100,
if ∆Ploss ≥2%
−1 −∆Ploss ∗50,
otherwise
(10)
∆Ploss = Ploss −Ploss_pre
(11)
∆Poverflow =
N
X
i,j
((Sij −Smax
ij
)2
(12)
∆Vviolation =
M
X
i
((Vi −V max
i
) ∗(Vi −V min
i
))
(13)
where N is the total number of lines with thermal violation; M is the total number of buses with
voltage violation; Ploss is the present transmission loss value and Ploss_pre is the line loss at the base
case.
2.3.4
Action Space
In this work, conventional generators are used to regulate voltage proﬁles and transmission losses.
A control vector is then created to include voltage set points (Vset) at each selected power plant as
continuous values, e.g., [0.9,1.1] p.u. The same control command is applied to all available generators
inside the same power plant. The details of training SAC agents are given in Algorithm 1, where the
gradients of different networks are calculated using equations provided in [10],[12].
3
Control Performance of SAC Agents
The presented SAC-based methodology for multi-objective power ﬂow control was developed in
Python 3.6 using Tensorﬂow 1.14, which was deployed in the control center of SGCC Jiangsu Electric
Power Company in Nov., 2019. The city-level power grid (220 k V and above) is used to demonstrate
the SAC agents’ performance, which consists of 45 substations, 5 power plants (with 12 generators)
and around 100 transmission lines, serving electricity to the city of Zhangjiagang, China. Massive
historical operating snapshots (full topology node/breaker models for Jiangsu province with 1500
nodes and 420 generators, at an interval of 5 minutes) were obtained from their EMS system. The
control objectives are to minimize transmission losses (at least 0.5% reduction) without violating bus
voltages ([0.97-1.07] pu) and line ﬂow limits (100% of MVA rating), namely, Eqs. 1, 8 and 9. Voltage
5

---


### Page 6

Algorithm 1 SAC Training Algorithm for Multi-objective Real-time Power Grid Control
Initialize: policy network φ ←random weights; Q networks θ1, θ2 ←random weights; target
networks ψ1 ←θ1, ψ2 ←θ2; replay buffer D ←{}
Set up power grid simulation environment env
for episode in range (n_episodes) do
reset environment and get initial conditions, state, reward, Ploss_ini, Vset_ini, done ←
env.reset()
for step t in itertools.count() do
if replay buffer D not full then
random action at ←random(A)
else
action at ←sample from policy π(at
st)
SAC agent interacts with environment, st+1, rt, done ←env.step(at,st)
Store transition (st, st+1, r, at, done) to D
if done == True or t == maxlen then
break
if episode ≥batch_size then
{(st, at, r, st+1)} ←sample from D
θi ←θi - λQ∇θJQ(θi), i ∈(1,2)
φ ←φ - λπ∇φJπ(φ)
α ←α - λ∇αJ(α)
ψi ←τθi + (1 - τ)ψi, i ∈(1,2)
Save agent model and write logs
Figure 2: Performance of SAC agent (blue dots: training phase; red circle: testing phase)
setpoints of the 12 generators in 5 power plants are adjusted by the SAC agent every 5 minutes. The
performance of training and testing SAC agents using a time series of actual system snapshots is
illustrated in Fig 2 and Fig ??, where positive rewards indicate successfully resolving voltage and
thermal violation issues, deﬁned in Eq. 8, Eq. 9. From 12/3/2019 to 1/13/2020, 7,249 operating
snapshots were collected. Two additional epochs of the original data sets were created and randomly
shufﬂed to create a training set (80%) and a test set (20%). For the ﬁrst 150 snapshots, the SAC
agent struggles to ﬁnd effective policies (with negative reward values); however, achieves satisfactory
performance thereafter. Three training processes are simultaneously launched and updated twice
a week to ensure control performance. For real-time application during this period, the developed
method provides valid controls for 99.41% of these cases. The average line loss reduction is 3.6412%
(compared to the line loss value before control actions). There are 1,019 snapshots with voltage
violations, in which SAC agent solves 1,014 snapshots completely and effectively mitigates the
remaining 5 snapshots.
6

---


### Page 7

Figure 3: Reduction in transmission losses, City of Zhangjiagang
4
Conclusions and Future Work
In this work, a novel methodology of training effective SAC agents with periodic updating is presented
for multi-objective power ﬂow control. The detailed design and ﬂowchart of the proposed methodology are provided for reducing transmission losses without violating voltage and line constraints.
Massive numerical simulations conducted on a real power grid in real-time operational environment
demonstrates the effectiveness and robustness of this approach. In future work, a multi-agent RLbased approach will be investigated for coordinating more types of corrective and preventive controls
for use in larger power networks.
Broader Impact
Power grid operation and control are facing new challenges caused by the increased penetration of
intermittent energy and dynamic electricity demands. Many traditional planning and operational
practices used by human operators may become ineffective under certain circumstances, because it is
not possible to precisely predict and study all possible power grid operating conditions thoroughly
for deriving corresponding controls, especially under severe disturbances that are never studied. In
addition, the models across different time horizons used for grid planning and operational purposes
are never perfect, resulting over-investment of grid infrastructure (if models are pessimistic) or
security risks (if models are optimistic).
The fast development and evolvement of AI technologies over the past few years and their successful
stories reported in various control problems, provide a promising way to ﬁll the above technology
gaps facing today’s power industry. In this work, we adopt state-of-the-art reinforcement learning
algorithms to tackle multi-objective real-time power ﬂow control problem and achieved preliminary
success. During the development phase, several difﬁculties were encountered by the team, which may
be typical for other industrial control problems, including (1) ensuring raw data and model quality to
be used for training RL agents, (2) collecting a sufﬁcient number of meaningful samples, (3) improving
performance of RL agents via hyperparameter tuning with limited computing resources, (4) design
of interfaces interacting with existing environment in a control center without interrupting existing
system operation, (5) ensuring long-term control effectiveness and robustness, (6) coordination of
AI-based controls with human operators. Besides the results presented in this paper, we are expanding
the capability of the developed method toward larger areas in the provincial power network, with
similar control performance observed. Moreover, a pilot project is underway in order to apply
AI-based voltage controls in a closed-loop form, by switching capacitors and reactors for regulating
voltage levels in a small zone using control commands derived from RL agents.
We hope the ﬁndings of this work can beneﬁt researchers and engineers in the area of promoting and
applying AI techniques in the power community.
7

---


### Page 8

Acknowledgments and Disclosure of Funding
This work is funded by State Grid Corporation of China (SGCC) Jiangsu Electric Power Company
through its Science and Technology Program.
References
[1] E. Mohagheghi, M. Alramlawi, A. Gabash and P. Li, “A Survey of Real-Time Optimal Power Flow,” Energies,
vol. 11, no. 11, 2018.
[2] D. K. Molzahn, J. T. Holzer, B. C. Lesieutre, et al., “Implementation of a large-scale optimal power ﬂow
solver based on semideﬁnite programming,” IEEE Trans. Power Systems, vol. 28, no. 4, pp. 3987-3998, Nov.
2013.
[3] R. Madani, M. Ashraphijuo, and J. Lavaei, “Promises of conic relaxation for contingency-constrained optimal
power ﬂow problem,” IEEE Trans. Power System, vol. 31, no. 2, pp. 199-211, Jan. 2015.
[4] Y. Tang, K. Dvijotham, and S. Low, “Real time optimal power ﬂow,” IEEE Trans. Smart Grid, vol. 8, no. 6,
pp. 2963–2973, Nov. 2017.
[5] DOE ARPA-E, “Grid Optimization Competition.” [Online]. Available: https://gocompetition.energy.gov/
[6] R. Diao, Z. Wang, D. Shi, etc., “Autonomous voltage control for grid operation using deep reinforcement
learning,” IEEE PES General Meeting, Atlanta, GA, USA, 2019.
[7] B. Zhang, X. Lu, R. Diao, et. al. “Real-time Autonomous Line Flow Control Using Proximal Policy
Optimization,” paper accepted for the IEEE PES General Meeting, Montreal, Canada, 2020.
[8] Z. Yan and Y. Xu, “Data-driven load frequency control for stochastic power systems: A deep reinforcement
learning method with continuous action search,” IEEE Trans. Power Syst., pp. 1–1, 2019.
[9] Q. Huang, R. Huang, W. Hao, etc., “Adaptive power system emergency control using deep reinforcement
learning,” IEEE Trans. Smart Grid, early access, 2019.
[10] T. Haarnoja et al., “Soft actor-critic: off policy maximum entropy deep reinforcement learning with a
stochastic actor,” in ICML, vol. 80, Stockholm Sweden, Jul. 2018, pp. 1861–187.
[11] P. Kundur, Power System Stability and Control, Mc Graw-Hill, Inc, New York (1994)
[12] T. Haarnoia, et al., “Soft actor-critic algorithms and applications,” ar Xiv preprint ar Xiv:1812.05905, 2018.
Appendix:
Table 1: Typical hyperparameters used for training SAC agents
Name
Description
Value
batch_size
batch size
32-200
maxlen
max number of iterations per episode
10-40
Decay_rate
decay rate
0.15
replay_size
replay buffer size
100,000-1,000,000
gamma
discount factor
0.99
epochs
number of epochs
1-5
polyak
polyak
0.995
lr
learning rate
0.0001-0.001
alpha
initial value of alpha
0.001-0.2
entropy_max
max value of entropy
0.001
random_seed
random seed value
10-30
n_hidden
number of hidden layers
2-5
n_neuros
number of neuros in hidden layers
64
n_inputlayer
dimension of input layer
300-500
n_outputlayer
dimension of output layer
5
8

---
