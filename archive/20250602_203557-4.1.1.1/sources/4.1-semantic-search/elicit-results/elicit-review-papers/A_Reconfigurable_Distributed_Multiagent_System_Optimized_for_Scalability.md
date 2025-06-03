

---

Page 1

---

1
Hierarchical Multi-Agent DRL Based Dynamic
Cluster Reconfiguration for UAV Mobility
Management
Irshad A. Meer, Student Member, IEEE, Karl-Ludwig Besser, Member, IEEE, Mustafa Ozger, Member, IEEE,
Dominic Schupke, Member, IEEE, H. Vincent Poor, Life Fellow, IEEE, and Cicek Cavdar, Member, IEEE
Abstract—Multi-connectivity involves dynamic cluster forma-
tion among distributed access points (APs) and coordinated
resource allocation from these APs, highlighting the need
for efficient mobility management strategies for users with
multi-connectivity. In this paper, we propose a novel mobility
management scheme for unmanned aerial vehicles (UAVs) that
uses dynamic cluster reconfiguration with energy-efficient power
allocation in a wireless interference network. Our objective
encompasses meeting stringent reliability demands, minimizing
joint power consumption, and reducing the frequency of cluster
reconfiguration. To achieve these objectives, we propose a
hierarchical multi-agent deep reinforcement learning (H-MADRL)
framework, specifically tailored for dynamic clustering and power
allocation. The edge cloud connected with a set of APs through
low latency optical back-haul links hosts the high-level agent
responsible for the optimal clustering policy, while low-level agents
reside in the APs and are responsible for the power allocation
policy. To further improve the learning efficiency, we propose
a novel action-observation transition-driven learning algorithm
that allows the low-level agents to use the action space from
the high-level agent as part of the local observation space. This
allows the lower-level agents to share partial information about
the clustering policy and allocate the power more efficiently. The
simulation results demonstrate that our proposed distributed
algorithm achieves comparable performance to the centralized
algorithm. Additionally, it offers better scalability, as the decision
time for clustering and power allocation increases by only 10%
when doubling the number of APs, compared to a 90% increase
observed with the centralized approach.
Index Terms—Reinforcement learning, Energy-efficiency maxi-
mization, Ultra-reliable communications, UAV communications.
I. INTRODUCTION
In cell-less wireless network, users are no longer con-
nected to just one access point (AP) but are instead served
Parts of this work were presented at the 2024 IEEE International Conference
on Machine Learning for Communication and Networking (ICMLCN) [1].
I. A. Meer, M. Ozger, and C. Cavdar are with the School of Electrical Engi-
neering and Computer Science, KTH Royal Institute of Technology, Stockholm,
Sweden (e-mail: {iameer, ozger, cavdar}@kth.se). K.-L. Besser, and H. V. Poor
are with the Department of Electrical and Computer Engineering, Princeton
University, USA (e-mail: {karl.besser, poor}@princeton.edu). D. Schupke is
with Airbus, Central Research and Technology, Taufkirchen, 82024 Germany
(e-mail: dominic.schupke@airbus.com). M. Ozger is also with the Department
of Electronic Systems, Aalborg University, Copenhagen, 2450 Denmark (e-mail:
mozger@es.aau.dk).
This work was supported in part by the CELTIC-NEXT Project, 6G for
Connected Sky (6G-SKY), with funding received from Vinnova, Swedish
Innovation Agency. The work of K.-L. Besser is supported by the German
Research Foundation (DFG) under grant BE 8098/1-1. The work of H. V. Poor
is supported by the U.S. National Science Foundation under Grants CNS-
2128448 and ECCS-2335876.
simultaneously in non-orthogonal multiple access schemes by
numerous distributed APs [2]. This shift dramatically alters the
traditional approach to mobility management, moving away
from standard handover management to a more dynamic cluster
reconfiguration model [1], [3]. As a result, the traditional
concept of coverage is transformed from being cell-centric to
being user-centric.
In this model, users are now seamlessly supported by a
group of multiple distributed APs using the same frequency-
time resources. The cooperation of APs to form clusters and
serve users can be implemented using various techniques, such
as coordinated multi-point (CoMP) [4], cloud-radio access
network (C-RAN) [5], and cell-free networks [6]. However,
determining the optimal cluster of the APs, i.e., the cluster
configuration, to satisfy stringent quality of service (QoS)
requirements, such as reliability, in dynamic environments,
where the user’s location continuously changes is a major chal-
lenge. Moreover, the cluster configuration must simultaneously
meet multiple, often conflicting objectives. While providing
communication through multiple APs can enhance QoS, it
may also result in excessive power consumption due to the
simultaneous transmission from different APs within the cluster.
Thus, a critical factor is minimizing total transmission power
while maintaining the high reliability demands by modern
applications. The high mobility of unmanned aerial vehicles
(UAVs) can also cause frequent cluster reconfigurations, which
correspond to the change in the cluster set as well as power
levels of the associated APs. Hence, it may lead to increased
control overhead and latency to reconfigure the clusters due to
the mobility of UAVs.
In addition, developing an efficient power allocation scheme
for dynamic clusters in a multi-connectivity wireless interfer-
ence network presents a significant challenge. This requires
continuously adapting to changing network conditions and
cluster configurations while managing interference, all under
stringent QoS constraints [7]. Different approaches, including
optimization theory [8], matching theory [9], [10], and game
theory [11] have been explored to address the challenges
of dynamic clustering and resource allocation in different
networks. However, these conventional techniques are often
hindered by several issues. For example, they depend on having
complete and real-time information about network dynamics,
which is unrealistic in a wireless scenario where channel
conditions fluctuate rapidly, especially for UAV communication
having a probabilistic line of sight conditions with ground APs.
arXiv:2412.16167v1  [cs.NI]  5 Dec 2024


---

Page 2

---

2
Additionally, These methods are computationally intensive and
struggle to scale, with complexity increasing exponentially as
network size grows [2].
Machine learning (ML), especially deep reinforcement
learning (DRL), has been recognized as a more adaptable and
resilient method for managing cluster reconfiguration and re-
source allocation, by interacting with an unpredictable wireless
environment [1], [3], [12], [13]. Through environmental learn-
ing, DRL leverages unique characteristics of communication
networks to learn the desired policies. While a centralized DRL
approach can efficiently solve the cluster reconfiguration and
resource allocation problem [1], it faces scalability issues as
the network size increases. On the other hand, multi-agent
deep reinforment learning (MADRL) addresses scalability
by enabling distributed decision-making. However, despite
its scalability advantages, MADRL encounters performance
limitations due to the lack of global information, which can
affect coordination and overall efficiency [14]. As a result,
both approaches present distinct advantages and challenges
that must be balanced. This motivates the use of hierarchical
MADRL, which combines local decision-making with a higher-
level coordination structure, offering a potential solution to
both scalability and performance trade-offs.
In this paper, we provide a scalable mobility management
framework for the multi-connectivity scenario, which meets
stringent reliability requirements while minimizing transmit
power and the number of cluster reconfigurations, even when
the network size increases. Given the uncertainties in UAVs
mobility and the variability of channel conditions over time,
we model the joint problem of cluster reconfiguration and
power allocation as a Markov decision process (MDP) and
propose a hierarchical MADRL framework to solve it. A
high-level agent operates within the edge cloud and makes
the clustering decision, while multiple low-level agents each
associated with individual AP perform power allocation to
the assigned users, as shown in Figure 1. The core concept
involves decentralizing the decision-making process, assigning
responsibilities to different levels of the network rather than
relying on a single decision-making agent. To improve the
performance of hierarchical MADRL and provide the low level
agents with global environmental information for better decision
making, we propose a novel action-observation transition
mechanism. This mechanism allows the action from the higher
agent to be used as a part of the observation space of the low
level agents.
The main contributions are summarized below.
• We formulate an optimization problem focused on dy-
namic clustering of APs and their power allocation
for UAVs within a wireless interference network. The
objective is to satisfy the stringent reliability requirements,
specifically considering error probabilities in finite block-
length regimes, reduce power consumption, and minimize
the frequency of cluster reconfigurations.
• We propose a hierarchical MADRL approach to enhance
communication reliability, lower power consumption, and
minimize cluster reconfiguration frequency in a dynamic
environment while improving the scalability and reducing
complexity and overhead. The high-level agent in the edge
cloud, connected to the APs, optimizes the AP clustering
strategy, while the low-level AP agents optimize the
power allocation. Additionally, the APs’ power allocation
strategies influence the edge cloud’s clustering strategy,
further improving system performance.
• We further propose an action-observation transition-driven
hierarchical framework, where the observation space of
the low-level agents includes the actions of the higher-
level agent. This integration ensures that the decisions
made by the higher-level agent directly influence and
guide the behavior of the low-level agents, creating a
more cohesive and adaptive system for multi-connectivity
mobility management.
• Finally, we validate the feasibility of our proposed
hierarchical MADRL through numerical simulations. The
results show that our proposed algorithm can achieve better
performance in comparison with other existing works,
including the central clustering approach in [1] and the
opportunistic clustering algorithm in [15].
II. RELATED WORK
Recently, mobility management for aerial users in mobile
networks has emerged as a key research focus. In conven-
tional single-connectivity mobile networks, several studies
[16]–[20] have approached the handover problem by modeling
it as an optimization task and leveraging DRL algorithms
to make handover decisions. For example, [16] compares
model-based and deep Q-network (DQN)-based strategies for
managing handovers in single-connectivity cellular-connected
UAVs. Similarly, [17] implements a DQN-based policy to
optimize handover rates and user throughput. The authors
in [18] use Q-learning to reduce the number of handovers
and enhance signal quality by introducing an reinforcement
learning (RL)-based framework that balances handovers and
received signal strength for connected UAVs. In [19], an RL-
based handover management scheme is proposed to jointly
optimize communication delay, interference, and handover
frequency, focusing on reducing uplink interference from UAVs.
Lastly, [20] jointly optimizes handover decisions, interference,
communication delay, and UAV path using a DRL-based
framework.
While the aforementioned studies address mobility manage-
ment for single-connectivity aerial users, mobility management
for aerial users served via multi-connectivity in mobile networks
is considerably more complex. In multi-connectivity scenarios,
each user has multiple candidate APs forming a cluster to
serve. However, this leads to an exponentially larger action
space, which makes convergence difficult. In [15], a dynamic
clustering approach is employed in an open-radio access
network (O-RAN) architecture based on channel gains between
the user and the APs. Although this method does not involve
learning, it increases signal overhead and requires cluster
reconfiguration whenever a user is added or removed. In
[21], beamforming vectors for dynamic AP clustering are
designed using RL for terrestrial users. However, the proposed
method does not address aerial users with stringent reliability
requirements. The work in [22] focuses on varying reliability


---

Page 3

---

3
Table I
TABLE OF NOTATION
Notation
Definition
K, k, K
The set, the index and the number of APs
N, i, N
The set, the index and the number of AUs
hik(t)
Channel gain from AP k to AU i at time t
Γ
Clustering strategy at the edge cloud
Nk
Set of assigned users to AP k, Nk ⊆N
Mi
Serving cluster for AU i
PT,ik(t)
Transmitted power from AP k to AU i
Pi(t)
Received power at user i
Pmax
Maximum allowed transmit power
N0
Noise spectral density
G0
Antenna array gain
θi,k(t)
Elevation angle between AP k and AU i
ϕi,k(t)
Azimuth angle between AP k and AU i
γMi
i
Receive SINR at AU i served by cluster Mi
bi
Number of transmitted information bits to user i
n
Finite block-length
εi
Decoding error probability at AU i
εmax
Maximum acceptable error probability
γth
SINR threshold
Oi(t)
SINR outage probability of AU i
for aerial users served by cluster of terrestrial APs but limits
its analysis to non-interfering environments with a single user.
Matching theory has also been applied to achieve optimal
clustering in multi-connectivity mobility scenarios [9], [10];
however, this approach is based on a static snapshot model,
which does not account for the dynamic challenges inherent
in the problem.
Hierarchical deep reinforcement learning (HDRL) has
emerged as a promising solution for addressing complex
optimization problems by breaking them down into smaller,
more manageable subproblems [23], [24]. In [23], HDRL
was applied to a drone cell trajectory planning and resource
allocation problem by decomposing it into two subproblems:
higher-level global trajectory planning and lower-level local
resource allocation. Likewise, [24] tackled the joint problem
of radio access technologies (RATs) assignment and power
allocation by leveraging the HDRL framework to divide the
problem into two stages: RATs-user assignment and power
allocation. More recently, [25] extended HDRL to handle
handover management and power allocation for terrestrial users.
However, they do not consider stringent reliability requirements
in the finite block-length regime.
To the best of our knowledge, there is limited research fo-
cusing on energy-efficient mobility management solutions that
meet stringent reliability requirements in the finite block-length
regime for aerial users with multi-connectivity configuration
in mobile networks.
III. SYSTEM MODEL AND PROBLEM FORMULATION
We consider an O-RAN architecture with a downlink com-
munication scenario, where the communication is established
from a cluster of APs to the UAVs. In a given area, we have
K O-RAN radio units (O-RUs) (hereafter referred to as APs)
deployed at fixed locations. All the APs are connected to the
edge cloud with virtualization and processing resource-sharing
capabilities [26]. A total of N UAVs, also referred to as AUs,
are moving within the coverage area following a 3D stochastic
mobility model from [27]. All the AUs are equipped with a
single omnidirectional antenna while each APs is equipped
with L uniform planar array antennas. The notation used in the
paper are given in the Table I. When AU i enters the coverage
area of the edge cloud, a cluster of APs under the clustering
strategy Γ form the cluster to serve AU i. A general clustering
strategy is defined as follows.
Definition 1. A clustering strategy Γ defines a collection
{MΓ
1, MΓ
2, . . . , MΓ
N} of subsets of K, where MiΓ ⊆K is
referred to as the serving cluster for AU i, with |MΓ
i | ≥1 and
|SN
i=1 MΓ
i | ≤K.
Note that the clusters MΓ
i may overlap, and their union may
not necessarily cover all elements of K. Therefore, the total
received power Pi at AU i at time t is given as
Pi(t) =
|MΓ
i (t)|
X
k=1
hik(t) PT,ik(t) G
 θi,k(t), ϕi,k(t)

,
(1)
where PT,ik denotes the transmit power of AP k to user i,
and hik is the power attenuation between APs k and user i,
i.e., the combined path loss and fading effects. These effects
are modeled according to [28]. With known location of the
user, we incorporate the 3D beamforming and beamtracking
by leveraging the antenna radiation pattern and the steering
vectors [29]. For this, G(θi,k(t), ϕi,k(t)) represents the antenna
array gain from AP k to user i, which is located at an elevation
angle of θi,k(t) and azimuth angle of ϕi,k(t) with respect to
the APs. The antenna array gain is given by
G(θi,k(t), ϕi,k(t)) = G0 · a(θi,k(t)) · b(ϕi,k(t)) ,
where G0 represents the constant array gain, while a(θi,k(t))
and b(ϕi,k(t)) represent the steering vectors in the elevation
and azimuth directions, respectively. The vectors a(θi,k(t)) and
b(ϕi,k(t)) are given according to [29] as
a (θi) =
M
X
m=1
Imej(m−1)(kdz cos(θi)),
(2)
b (ϕi) =
N
X
n=1
IT
nej(n−1)(kdy sin(θi) sin(ϕi)) ,
(3)
where, Im and In denote column vectors of ones of sizes m and
n, respectively. The number of antennas in z- and y-directions
of the antenna array are M and N, respectively. The dz and
dy represent the antenna spacing in the z- and y-directions,
respectively, and k represents the wave number. For ease of
reading, we omit the time index t and the superscript Γ, unless
it is necessary to explicitly specify it.
Definition 2. For a given clustering strategy Γ, a power allo-
cation policy PT,ik defines power allocation in each cluster i,
{PT,i1, PT,i2, . . . , PT,iK}, where PT,ik is the allocated power
from AP k to AU i.


---

Page 4

---

4
Environment
High-level 
observation ( ̅𝑠!), reward ( ̅𝑟!"#)
Low-level 
observations (𝑆!
"), rewards (𝑟!#$
"
)
High-level action (&𝑎!)
Low-level actions (𝑎!
$) 
High-level Policy
Low-level Policy
Agent-1
Agent-2
Agent-3
Agent-K
Step 1: Clustering Decision 
Step 2: Power Allocation 
Edge Cloud
Figure 1.
Network architecture of the proposed H-MAPPO. The system consists of K multi-agents at the APs, connected to a high-level agent in the edge
cloud. These agents collaboratively serve N AUs. The H-MAPPO framework operates in two steps: (1) the high-level agent makes a clustering decision and
communicates it to the low-level agents; (2) the low-level agents allocate power to the assigned AUs based on the clustering information and local observations.
With the above definition, the receive signal-to-interference-
plus-noise ratio (SINR) at the target AU i served by cluster Mi
is:
γMi
i
=
P|Mi|
k=1 hikPT,ikG(θi,k, ϕi,k)
σ2 + PK
k=1
PN
n=1
n̸=i hkiPT,nkG(θn,k, ϕn,k)
,
(4)
where σ2 is the noise power, and the interference power is the
sum of all received power from all APs serving on the same
resource to other AUs.
A. Finite Block-length Case
UAV applications such as real-time surveillance, emergency
response, and industrial inspection require not only seamless
service continuity for payload traffic but also ultra-reliable low
latency communication (URLLC) for command and control
operations. Such communication relies on finite block-length
codes, where the decoding error probability is non-zero, thus
affecting the reliability. Multi-connectivity has been shown to
improve URLLC in such finite block-length regimes [30]–[32].
Therefore, our goal is to investigate the impact of cluster
reconfiguration and power allocation in this finite block-length
regime.
Assuming white Gaussian noise, the channel capacity as a
function of the SINR at the AU i is given by:
C(γMi
i
) = log2(1 + γMi
i
) .
(5)
In the finite block-length regime, there is an approximation
for the maximum achievable rate, accounting for the finite
sample size, error probability, and coding. The date rate for
AU i with block-length n and error probability ε is given
by [33, Eq. (296)]:
R∗
i (n, ε) ≈E
(
C(γMi
i
) −
s
V (γMi
i
)
n
Q−1(εi)+
log2 n
2n
+ O(1)
)
(6)
where Q−1 is the inverse Q-function, which is defined as
Q(x) =
1
√
2π
Z ∞
x
exp
t2
2

dt .
The channel dispersion V (γMi
i
) in (6) is given by
V (γMi
i
) =
 
1 −
1
(1 + γMi
i
)2
!
(log2 e)2 .
(7)
According to (6), using a finite block length results in a
maximum achievable rate that is less than the channel capacity
(with an infinite block length). This reduction is caused by
the channel dispersion V (γ). However, as the block length n
becomes very large and the error probability εi approaches
zero, the achievable rate can reach the channel capacity.
The minimum decoding error probability (DEP) incurred in
the transmission of bi bits to AU i using a finite block-length
of n can be accurately approximated by substituting Ri = bi
n
in (6) and is given by [34]
εi(n, bi) ≈E


Q

nC(γMi
i
) + 1
2 log2 n −bi
q
nV (γMi
i
)




.
(8)
The expectation in (8) is over γMi
i
since the SINR changes
with different channel realizations. In order to have reliable


---

Page 5

---

5
communications, the error probability should be less than a
maximum threshold, i.e., εi(n, bi) ≤εmax. The maximum DEP
constraint can also be written as a SINR constraint as
γMi
i
≥γth ≈exp
Q−1(εmax)
√n
+ bi ln 2
n
−ln n
2n

−1.
(9)
While we assume that the positions of the AUs and the
fading statistics are known, the exact channel state is assumed
to be unknown. Hence, the user will be in an outage with a
non-zero probability when the SINR at the AU is below a
predefined threshold γth, i.e., the outage probability for user i
at time t is given as
Oi(t) = Pr

γMi
i
(t) < γth

.
(10)
Depending on the specific use case, there exists an outage
probability requirement, denoted as Omax, that is deemed
acceptable. However, it is essential to acknowledge that this
tolerance level is influenced by various factors and may change
over time, e.g., when the user moves into a different area.
B. SINR Outage
In the sequel, we derive an expression for calculating the
outage probability from (10) for a single time slot t, i.e., for a
fixed power allocation and fixed positions of all users. In this
case, we can rewrite the outage probability as the probability of
a new random variable that comprises of a sum of exponentially
distributed random variables with different expected values,
Oi(t) = Pr

γMi
i
(t) < γth

= Pr


|Mi|
X
k=1
hikPT,ikG(θi,k, ϕi,k) < si


= Pr


|Mi|
X
k=1
Yik < si


= Pr (Ti < si)
= 1 −¯FTi(si)
(11)
where si = γthβi is the product of the SINR threshold γth and
the interference power βi at user i. Based on the Rayleigh
fading model, the random variable Ti is given as the sum
of exponentially distributed variables Yik ∼Exp(αik) with
different expected values αik. The expected values are given
by the product of transmit power, antenna gain, and path loss.
The survival function ¯FTi of Ti is given by [35]
¯FTi(s) =
K
X
k=1
Aik · exp (−αik · s),
(12)
Aik =
K
Y
j=1
j̸=k
αik
αij + αik
,
for k = 1, . . . , K.
(13)
For this expression to hold, we need to assume that all αik
are distinct. However, since they are the product of transmit
power, antenna gain, and path loss, this assumption will hold
almost surely in practice.
C. Problem Formulation
The joint dynamic clustering and power allocation for APs
is of utmost importance to ensure both reliable and energy-
efficient communication. To accomplish this objective, we
present an optimization problem aimed at finding the optimal
serving cluster that satisfy the QoS requirements for each user
and the corresponding power allocation vector.
Let M = {Mi, ∀i ∈N} denote the variable for AP
clustering. Let P = {PT,ik, ∀i ∈N, ∀k ∈K} denote the
transmit power variable for the multi-connectivity users. Based
on this, we use a scalarization to formulate the general multi-
objective optimization problem of APs clustering and power
allocation as
max
P,M
1
N
N
X
i=1
1 (Mi(t) = Mi(t −1)) +
PN
i=1 bi
nPtotal/(1 −εmax)
(14a)
s.t.
C1 : εi ≤εmax,
∀i
(14b)
C2 : PT,ik ≤Pmax,
∀i, k, t
(14c)
C3 : |Mi(t)| ≥1,
∀i, t
(14d)
C4 : γMi
i
(t) ≥γth,
∀i, t
(14e)
where εmax is the maximum error threshold tolerable for
the reliable communication, bi is the number of information
bits transmitted to AU i, n is the block-length, and Ptotal =
PK
k=1
PN
i=1 PT,ik is total transmitted power. The first term
in (14a) aims to maintain the stability of the serving clusters
for the AUs moving within the area, while the second term
seeks to maximize the number of bits successfully transmitted
using the minimum total transmit power. It can be observed that
given εmax, n, and bi are constant, maximizing the successfully
transmitted bits is equivalent to minimizing the total power
consumption from all APs.
D. Mobility Model
In this work, we employ a realistic and tractable mobility
model to capture the mobility of UAVs. In particular, we use
the model provided in [27] using coupled stochastic differential
equations. By utilizing estimated positions instead of actual
ones, the model incorporates more realistic device trajectories
and considers imperfect navigation. The advantage of this
approach lies in its ability to generate smoother and realistic
trajectories. Additionally, it provides better control over velocity
through correlation parameters, which influence stability and
mobility based on distance-velocity relationships. Additional
variance parameters scale Brownian perturbations, offering
flexibility in introducing stochastic variations. For detailed
explanations of the model, please refer to the original work [27].
E. User Handling
In a multi-connectivity wireless interference network, the
dynamic clustering of APs depends on the number of users
being served by the network. The arrival and departure of users
within the network’s coverage area influence the clustering
decisions. Therefore, for a more realistic and dynamic scenario,
our system needs to efficiently manage users entering and


---

Page 6

---

6
leaving the coverage area without disrupting the already
established clusters.
1) Users Entering the Coverage Area: When a completely
new mobile user enters the coverage area of the system, they
were not previously associated with the system. As a result, they
become part of the active user group and are served by a new
AP cluster. The formation of a new serving clusters without
affecting the other clusters ensures that new users seamlessly
receive services within the existing system framework.
2) User Leaves the Coverage Area: On the other hand,
active users can become inactive, e.g., by moving out of the
service area or switching off their device. As a result, they
transition from an active to a non-active state and are no longer
served by the AP cluster they were previously associated with.
The freed APs can then be used to become part of the serving
clusters of the active users. This allows to efficient management
of resources and ensure optimal service distribution to active
users.
IV. HMARDL FOR DYNAMIC CLUSTERING AND POWER
ALLOCATION
In this section, we present a hierarchical learning framework
to decompose the joint cluster reconfiguration and power
allocation problem in (14a) by exploiting the dependency
between them. In this framework, the edge cloud having global
observations learns the optimal clustering policy, also referred
as the high-level policy, for the connected APs serving the AUs
within the edge cloud coverage area. While each AP acting
as a single agent uses local observations to learn the optimal
power allocation policy, also referred as the low-level policy,
for the allocated AUs. Both the clustering and power allocation
policies are governed by their respective observation spaces,
action spaces and the reward functions.
A. Problem Decomposition
As shown in [1], the original problem remains scalable when
the number of APs in the service area is limited. However, as the
number of APs increases, the action space grows significantly,
making it challenging to find a solution for the joint objective
function within a finite time. To address this challenge,
we decompose the optimization problem in (14a) into two
subproblems, separating the tasks of cluster reconfiguration
and power allocation.
1) Subproblem 1: Optimal Cluster Reconfiguration: The
first subproblem aims to maintain the stability of the serving
clusters, which is formulated as:
Γ :
max
M
1
N
N
X
i=1
1

Mi(t) = Mi(t −1)

(15a)
s.t.
C1 −C4.
(15b)
The problem poses a combinatorial challenge and is difficult
to solve due to the non-convex nature of its objective function.
Typically, there is no computationally efficient or systematic
method for achieving an optimal solution to this type of
problem. However, it is well-suited for an iterative RL approach.
To ensure this subproblem remains bounded and converges
in time, we modify the problem by incorporating constraint
C4 into the objective function. Further details are given in
Section IV-C.
2) Subproblem 2: Optimal Power Allocation: Consider a
given fixed clustering policy π, the optimal power allocation
policy P⋆
i,k can be obtained as a solution to the following
optimization problem for every t:
P⋆
i,k :
max
P
PN
i=1 bi
nPtotal/(1 −εmax)
(16a)
s.t.
C1 −C4
(16b)
The objective in (16a) is to maximize the number of bits
transmitted while satisfying reliability constraints, with the
least possible total transmitted power. The optimal power
allocation P⋆
i,k minimizes the transmitted power in the link
between user i and the serving AP cluster for all user-AP
links at each time t. Thus, P⋆
i,k provides the optimal power
allocation for any given clustering Γ.
B. Hierarchical MAPPO Framework
The H-MAPPO framework addresses the mobility manage-
ment problem for multi-connectivity users by employing a
hierarchical decision making structure, as shown in Figure 1.
In this framework, the edge cloud first determines the high-level
action, specifically the clustering strategy Γ for each user i ∈N,
utilizing the conventional proximal policy optimization (PPO)
algorithm. Subsequently, each low-level AP k ∈K updates its
power allocation policy PT,ik for each assigned user using the
multi-agent proximal policy optimization (MAPPO) algorithm.
This update is based on the assigned users Nk, their locations,
and channel conditions. The interactions among the low-level
agents collectively determine the system state for the high-
level agent, prompting the edge cloud to revise its clustering
strategy in the subsequent decision epoch. This hierarchical
design effectively reduces the search space for each agent and
enhances learning efficiency. In the following, we define the
high-level and low-level RL components for the edge cloud
and the APs, respectively.
C. High-Level: Dynamic Cluster Reconfiguration
First, we discuss the high-level agent in detail, in particular
its observation space, action space, and reward function.
1) High-Level Observation Space: The observation space
of the high-level agent, located at the edge cloud, must include
network-level information about the connected APs and AUs for
optimal clustering. The high-level observation space includes
the location information of the AUs x, y, z = {xi, yi, zi
∀i},
user load of the APs N = {Nk, ∀k}, the channel condition
between connected APs and the AUs h = {hi,k, ∀i, k}, and
the current clustering M = {Mi,k, ∀i, k}. Consequently, the
observation space of the high-level agent is expressed as:
¯St ≜{x(t), y(t), z(t), l(t), h(t), M(t −1)}
(17)
2) High-Level Action Space: At each time step, the main
role of the high-level agent is to take an action ¯at
≜
[M1, M2, . . . , MN] which gives the serving cluster Mi for
each AU i ∈N.


---

Page 7

---

7
3) High-Level Reward Function: The reward function for
the high-level agent guides its policy πθ parameterized by θ by
rewarding stability in cluster configurations, i.e., by minimizing
the number of cluster reconfigurations, as described in (15a).
To connect the high-level policy with the low-level actions of
the APs, the reward is structured around two key objectives:
maintaining stable serving clusters for the AUs and reducing
the number of AUs experiencing SINR outages. Thus, the agent
is rewarded when clusters remain stable, provided that users
are not in outage. The instantaneous reward r that the agent
receives for a given action in a particular state is defined as:
¯r = ω1
N
N
X
i=1
1

Mi(t) = Mi(t −1)

−ω2
N
N
X
i=1
1(Oi > Oth) ,
(18)
where the non-negative weights ωi, i ∈{1, 2}, are used to
balance between the individual objectives. The reward ¯r in (18)
increases when the number of stable clusters or non-outage
users increases. The Oi is obtained from (10) and depends on
the SINR threshold.
D. Low-Level: Multi-Agent Optimal Power Allocation
Through the action ¯at of the learned policy πθ, the edge
cloud assigns a serving cluster Mi for each AU i ∈N.
Consequently, an AP k ∈K is allocated a set of users Nk ⊆N
to be served by this AP. The APs, using a multi-agent learned
policy, optimize the power allocation for their assigned users.
To facilitate this, we outline the basic RL components for the
low-level multi-agents in the following.
1) Low-Level Observation Space: The low-level observation
space sk
t is designed to encompass both local information
pertinent to the agent and shared data from the higher
level sk
t = {¯sk
t , ¯ak
t }. Specifically, the observation space for
the k-th agent includes the assigned users Nk ⊆N, their
location information x, y, z = {xj, yj, zj : j ∈Nk}, the line-
of-sight (LoS) conditions for assigned users LoSk,j, j ∈Nk,
and a set detailing the assigned clusters from the higher
level Mk = {Mj, ∀j ∈Nk}. Consequently, the observation
space of the low-level k-th agent is expressed as:
Sk
t ≜{x(t), y(t), z(t), LoSj,k, Mk(t)}
(19)
2) Low-Level Action Space: The low-level agents at APs
operate independently, utilizing a learned policy. At each time
epoch t, the higher-level agent performs clustering actions
for each user within the service area, and each low-level
agent k takes the action ak
t , which determines the optimal power
allocation P ⋆
j,k, ∀j ∈Nk. An agent k develops a policy πθk
parameterized by θk that exploits the dynamic characteristics of
the channel and the clustering from the higher level to optimize
power allocations from various APs in the cluster. The policy’s
primary objective is to maximize the objective function (16a)
while adhering to constraints. The action space of low-level
agent k is expressed as:
ak
t ≜[P ⋆
1,k, P ⋆
2,k, . . . , P ⋆
Nk,k]
(20)
𝑆= { ̅𝑆!, ̅𝑠!", ̅𝑠!#, . . ̅𝑠!$}
𝜋( ̅𝑆!)
𝜋!(𝑠"
!)
𝜋#(𝑠"
#)
𝜋$(𝑠"
$)
̅𝑆!
̅𝑠!"
𝑎!
"
𝑎!#
𝑎!
$
,𝑎!"
,𝑎!#
,𝑎!
$
̅𝑠!
#
̅𝑠!$
⊕
⊕
⊕
Environment
State Extraction
,𝑎!
% = {,𝑎!", ,𝑎!#, .. ,𝑎!$}
𝐴= {,𝑎!
%, 𝑎!", 𝑎!#, . . 𝑎!$}
Figure 2. Proposed action-observation transition-driven H-MAPPO Framework.
3) Low-Level Reward Function: The reward for the low-
level agent aims to increase the fraction of users associated to it,
while using minimum power and satisfying the constraints. In
particular, the instantaneous reward is expressed as a continuous
function that seeks to minimize the total transmitted power
while penalizing the violation of constraints. The low-level
reward function rk
t for agent k at time t is given as:
rk
t =
 
1 −ω1
PNk
j
P ⋆
j,k
NkPT max
!
−ω2
Nk
Nk
X
i=1
1(εi > εmax)
(21)
where the non-negative weights ωi, i ∈{1, 2}, are used
to balance between the individual objectives. The reward r
in (21) increases when the used transmit power is reduced, and
decreases when the number of assigned users violating the DEP
threshold εmax increases. Towards this goal, we implement the
MAPPO algorithm to derive the power allocation policy P ⋆
j,k.
E. The Proposed Hierarchical MAPPO Algorithm
An overview of the complete RL framework for the proposed
H-MAPPO is presented in Figure 2. An algorithmic description
of the proposed H-MAPPO framework is given in Algorithm 1.
In the first episode, the high-level edge cloud agent selects the
clustering of the APs. This clustering decision then updates
the observation space for the low-level APs agents, allowing
each AP to determine the power allocation based on the local
observations, as detailed in lines 7 through 9 of Algorithm 1.
After the edge cloud and APs perform their respective actions,
the rewards are computed, and both the high-level and low-level
policies are updated accordingly.


---

Page 8

---

8
F. MAPPO Policy Training
In the MAPPO algorithm, each policy πθk parameterized
by θk, is a function that maps states to actions. The policy
is typically represented by a neural network, which takes the
state as input and outputs a probability distribution over the
possible actions. Each policy is trained independently, meaning
that the data collected from one policy is not used to train
the other policies. However, the policies can share the same
architecture and weights, and can be trained in parallel.
MAPPO uses the same core principles as single-agent
PPO, with modifications to handle multiple agents and their
interactions. Derived from the Trust Region Policy Optimization
algorithm [36], [37], PPO introduces a clipped surrogate
objective to enhance stability in policy updates. Each agent
updates its policy to maximize the expected reward, using the
following clipped surrogate objective [38]:
LCLIP
k
(θk) = Et

min
n
ρt(θk) ˆAk
t ,
clip (ρt(θk), 1 −η, 1 + η) ˆAk
t
o
(22)
where ρt(θk) is the probability ratio between the new and old
policies for the action ak
t :
ρt(θk) = πθk(ak
t |sk
t )
πθold
k (ak
t |sk
t )
(23)
and ˆAk
t is the advantage function estimate for agent k. The
clipping parameter η controls the extent of policy updates to
ensure stability.
Advantage estimation quantifies how much better an action is
compared to the expected value. MAPPO employs Generalized
Advantage Estimation (GAE) to reduce variance and improve
stability:
ˆAk
t =
∞
X
l=0
(γλ)lδk
t+l,
(24)
where δk
t is the temporal difference error for agent k:
δk
t = rk
t + γV (sk
t+1) −V (sk
t ).
(25)
Here, γ is the discount factor, λ is the GAE parameter, and
V (sk) is the state value function for agent k. In MAPPO, each
agent learns its policy independently, optimizing its objective
based on individual experiences:
θk ←θk + α∇θiLCLIP
k
(θk),
(26)
where α is the learning rate. Agents interact within the
environment, which provides feedback in the form of rewards
that guide the policy updates.
G. Deployment Scenario
We formulate our problem as an MDP within OpenAI’s
Gym environment. Our hierarchical multi-agent framework
is implemented using Ray’s RLlib library [39]. RLlib offers
a scalable, flexible, and efficient solution for training RL
models across multiple nodes and GPUs. By harnessing Ray’s
Algorithm 1 H-MAPPO based Dynamic Clustering and Power
Allocation
Input: K, N, εmax, Pmax, and γth
i
Output: Clustering strategy Γ, Optimal power allocation P ⋆
i,k
1: for each episode ←1 to end do
2:
Initialize: High level observation space ¯St and low-level
observation space for each agent Si
t
3:
while not done do
4:
if first episode then
5:
Only high-level agent accepts observation space
and returns the action space
6:
end if
7:
¯
At = {¯a1
t, ¯a2
t, ..., ¯aK
t }: Action space from trained
high level agent
8:
Si
t = {¯ai
t, xi(t), li(t), LoSi}: Updated observation
space of a low-level agent i
9:
At = {a1
t, a2
t, ..., aK
t }: Action space from trained
low-level agents
10:
Calculate the error probability from (8) using
{ ¯At, At}
11:
Obtain the high level reward using (18) and low-level
reward using (21)
12:
Update the status of the users
13:
end while
14: end for
Table II
HYPERPARAMETERS EMPLOYED FOR TUNING OUR MODEL
Parameters
Value
Learning rate
10−5
Batch size
4000
Entropy coefficient
auto
Iterations
2 · 106
Discount factor (γ)
0.99
GAE parameter (λ)
1.0
PPO Clip parameter (η)
0.3
distributed computing capabilities, RLlib parallelizes simula-
tions, experience collection, and model updates, significantly
accelerating training processes and enabling the handling of
large-scale RL tasks.
Given the discrete-time nature of our problem, after each
iteration, the higher-level agent’s policy generates values for the
cluster reconfiguration indicator, while the lower-level agents’
policies generate the outage and transmit power indicators.
Using these values, the high-level reward (18) and the low-
level reward (21) for each agent are calculated and fed back
to the respective agents.
The initial agent hyperparameters are summarized in Table II,
having been empirically determined through multiple iterations.
The source code of our implementation for reproducing all
of the shown results will be made publicly available with the
final version of the paper.


---

Page 9

---

9
V. NUMERICAL EVALUATION
In this section, we showcase the effectiveness of our proposed
H-MAPPO implementation for solving (14a). Additionally, we
benchmark our H-MAPPO algorithm against the following
baseline methods:
• MSAC: A centralized approach called masked soft actor-
critic (MSAC) based clustering and power allocation
from [1].
• MAPPO: A completely distributed approach without any
hierarchical policy division based clustering and power
allocation, where each agent decides to join the serving
cluster for a user and allocated power.
• Opportunistic: An opportunistic clustering approach
from [15], where a central entity opportunistically decide
to include an O-RU (AP) in a cluster for user service
based on channel gains.
• Closest: A simple approach in which only the nearest
O-RU (AP) serves a user with maximum power.
For the numerical evaluation, there are N = 6 users in a
square area of 3 km × 3 km. They are served by K = 19 APs,
which are placed randomly within this area at a height of 25 m.
Each AP is equipped with L = 16 antennas. The model of the
path-loss follows [28], where we set the carrier frequency to
2.0 GHz to accommodate a broader range for command and
control traffic for the UAVs. The noise power at the receiver is
given as σ2 = N0B, where B = 10 MHz is the communication
bandwidth, and N0 = −174 dBm/Hz is the noise spectral
density. The UAVs move randomly following the mobility
model described in Section III-D across the area. For a fair
comparison, we keep all parameters of the communication
system the same for all algorithms.
A. Learning Efficiency of H-MAPPO
We begin by evaluating the convergence and learning
performance of the proposed action-observation transition-
driven H-MAPPO algorithm, comparing it to the distributed
MAPPO algorithm, which uses the conventional MAPPO
method to the APs agents. In H-MAPPO, the clustering
decision is centralized while power allocation is distributed,
whereas in MAPPO, both clustering and power allocation
decisions are distributed. As illustrated in Figure 3, agents
utilizing the action-observation transition-driven H-MAPPO
exhibit significantly faster convergence and higher overall
reward accumulation than those relying on the distributed
MAPPO approach. Specifically, the reward performance of
the H-MAPPO algorithm experiences a steep rise in the early
stages of training, stabilizing at a higher value in a shorter time
compared to the slower and less consistent learning trajectory
of MAPPO.
Although both algorithms show some fluctuations in reward
values, the action-observation transition-driven H-MAPPO
achieves an estimated 15 % improvement in overall rewards.
This enhanced performance can be attributed to the algorithm’s
distinct ability to decouple the tasks of clustering and power
allocation between the various APs. By allowing the high-
level edge cloud to control clustering decisions, each AP
acts independently as a PPO agent, iteratively adjusting its
0
2
4
6
8
0
50k
100k
150k
200k
250k
Time steps
Agent reward
H-MAPPO
MAPPO
Figure 3. Numerical results comparing the rewards obtained during training
iterations for both H-MAPPO and MAPPO.
power allocation strategy based on local observations of its
environment. This hierarchical structure ensures that clustering
and resource management decisions are more efficient and
tailored to the specific conditions at each AP.
Moreover, the parallel training of all low-level APs agents
further reduces training time and computational costs, as the
system can learn more efficiently by distributing tasks across
agents. The coordination between the high-level clustering
decisions and the low-level power allocation adjustments
enables the action-observation transition-driven H-MAPPO to
optimize resource utilization and achieve superior performance.
This hierarchical approach represents a notable improvement
over the traditional MAPPO algorithm, where agents face
greater difficulty balancing both clustering and power allocation
simultaneously without a clear separation of responsibilities.
B. Reliability Performance
In Figure 4, we demonstrate the reliability performance of
our proposed action-observation transition-driven H-MAPPO
algorithm. One of the primary objectives of our problem is to
ensure reliable data transmission with a DEP below a given
threshold, i.e., εi ≤εmax.
The results for DEP threshold violations are presented
in Figure 4(a) and the distribution of the SINR outage
probability O in Figure 4(b). Although these two objectives are
interdependent, in our proposed action-observation transition-
driven H-MAPPO algorithm, the DEP threshold constraint
governs the low-level policy, while the SINR outage constraint
influences the high-level policy.
In Figure 4(a), we observe the results of the average
DEP threshold violations experiences by the users under
different schemes. It can be seen that the proposed H-
MAPPO algorithm achieves comparable performance to the
centralized MSAC for medium to high thresholds, whereas
the fully distributed MAPPO suffers from a higher rate of
outages. Since the Opportunistic and Closest schemes do
not optimize for the reliability, the violations are very high


---

Page 10

---

10
10−7
10−6
10−5
10−4
10−3
0
0.002
0.004
0.006
0.008
DEP Threshold εmax
DEP Threshold Violations
H-MAPPO
MSAC
MAPPO
(a) DEP threshold violations experienced by the UAVs for different DEP
thresholds εmax.
−14 −12 −10
−8
−6
−4
−2
0
0
0.2
0.4
0.6
0.8
1
SINR Outage Proability log10 O
CDF
H-MAPPO
MSAC
MAPPO
Opportunistic
Closest
(b) CDF of the outage probability O experienced by the UAVs in service
area.
Figure 4.
Numerical results of the DEP threshold violation and the SINR outage probability O. (Section V-B)
compared to the learning-based algorithms (in the range of
0.890 to 0.989) and are therefore not shown in Figure 4(a).
Furthermore, as the DEP threshold decreases, the number
of outages increases. This is expected, as maintaining a
low error probability in a dynamic environment becomes
challenging due to fluctuating channel conditions. However,
for small thresholds εmax, our proposed H-MAPPO algorithm
significantly outperforms the other schemes.
Next, in Figure 4(b), we present the SINR outage proba-
bility results. The CDF illustrates the distribution of outage
probabilities O experienced by users as they move through
the service area. As can be seen from the figure, the proposed
H-MAPPO algorithm outperforms all comparison strategies.
In particular, for the proposed H-MAPPO algorithm, the CDF
is close to one when the outage probability is around 10−8, i.e.,
the SINR outage probability experienced by a user almost never
exceeds this value. For the centralized MSAC scheme, this
value is closer to 10−5, i.e., three orders of magnitude greater
than for our proposed algorithm. However, both algorithms
perform significantly better than the baselines MAPPO,
Opportunistic, and Closest. The superior performance of
H-MAPPO stems from its ability to adapt to strict reliability
constraints through dynamic power control by low-level agents,
guided by the maximum error threshold. By considering user
positions, LoS conditions, and spatial relationships between
neighboring APs, the algorithm minimizes interference and
ensures reliability.
Although the Opportunistic strategy performs better than
the Closest approach, the latter reduces interference by limiting
the number of serving APs per user. However, this reduction in
interference comes at the cost of reduced received power, which
increases the likelihood of outages. Both strategies fall short
of optimizing for the stricter reliability demands of the system.
These results highlight the effectiveness of our hierarchical
framework, which combines the reliability of a centralized
approach with the scalability and efficiency of a distributed
approach.
C. Transmit Power Performance
The second objective of our problem is to minimize the total
transmitted power from the serving clusters while ensuring the
system meets its reliability performance targets. Achieving this
with minimal power is crucial for system energy efficiency.
The comparison of the total transmitted power across different
algorithms is shown in Figure 5. Since the transmit power in
the Closest scheme is constant, it has been omitted from the
graph.
As depicted in Figure 5(a), the proposed H-MAPPO
algorithm achieves the DEP threshold with the lowest transmit
power, followed by the fully distributed MAPPO. In contrast,
the centralized MSAC requires the highest power. This is
because MSAC, while consuming more power, provides better
reliability compared to MAPPO, which experiences more
outages, as shown in Figure 4. The proposed H-MAPPO
outperforms both in terms of reliability and power efficiency.
The high-level clustering policy in H-MAPPO allows the edge
cloud to select the most favorable APs for the serving clusters,
whereas the fully distributed approach may involve suboptimal
APs, leading to more power consumption. Additionally, it is
observed that as the DEP requirement becomes stricter, the
total transmitted power increases to boost the SINR and reduce
transmission errors.
The Closest scheme operates with a single AP at maximum
power, resulting in a constant graph at 1/K, i.e., 1/19 ≈0.05
for this particular example. Meanwhile, the Opportunistic
scheme, which is not optimized for meeting reliability con-
straints, uses on an average over 90 % of the available power
and is unaffected by the DEP thresholds. Therefore, these
schemes are not shown in Figure 5(a). However, the transmit
power distribution for Opportunistic is presented alongside
other schemes in Figure 5(b).
The observations from Figure 5(b) reveal that the learning-
based cluster and power allocation schemes use less than
60 % of the maximum available transmit power 90 % of
the time. While non-learning based algorithms use less than


---

Page 11

---

11
10−7
10−6
10−5
10−4
10−3
0.4
0.5
0.6
0.7
DEP Threshold
Fraction of Maximum Power
H-MAPPO
MSAC
MAPPO
(a) Fraction of total transmitted power for different DEP thresholds εmax.
0
0.2
0.4
0.6
0.8
1
0
0.2
0.4
0.6
0.8
1
Fraction of the maximum transmit power
CDF
H-MAPPO
MSAC
MAPPO
Opportunistic
(b) CDF of the total transmit power.
Figure 5.
Numerical results of fraction of maximum power utilized and the distribution of the total transmit power of the system normalized by the maximum
available power. (Section V-C)
60 % of the maximum available transmit power only 30 % of
the time. This highlights that these learning-based methods
not only excel at mitigating outages and meeting stringent
reliability requirements, but they also achieve these goals with
significantly reduced total transmitted power.
D. Clustering Size and Scalability Performance
The third objective in our problem is the formation of clusters.
The distribution of the average cluster size for serving mobile
UAVs is depicted in Figure 6. Notably, the distribution for H-
MAPPO is centered around smaller cluster sizes, indicating
that the high-level clustering decision typically involves half
or fewer APs per serving cluster. Having a smaller number
of APs serving a user simplifies the coordination and is
therefore beneficial. Through training, the high-level agent
in H-MAPPO effectively balances SINR outage requirements
and the number of APs in each cluster. In particular, almost
no clusters with more than 11 APs have been formed by
the H-MAPPO algorithm. The cluster size distribution of
the H-MAPPO reflects that the scheme uses less than half
of the APs for forming clusters. While the distribution from
MAPPO reflects that it uses more than 11 APs with similar
probability. The H-MAPPO shows the highest probability for
a cluster size of 7, whereas for MSAC and MAPPO, the
peak occurs at 8. The variation in cluster sizes is due to the
separation of clustering and power allocation in H-MAPPO,
where power is optimized for a fixed cluster size. In contrast,
while MSAC centralizes the power allocation and clustering
decisions, directly influencing cluster sizes, MAPPO fully
decentralizes these decisions, resulting in a wider distribution
of cluster sizes.
Meanwhile, the Opportunistic scheme, driven by favorable
channel conditions and full power transmission, often involves
more than 50 % of APs in clusters, leading to excessive
power usage. The Closest algorithm uses only single AP
for connectivity, its results are thus not shown in Figure 6.
Additionally, it is noteworthy that both H-MAPPO and
2
4
6
8
10
12
14
16
0
0.05
0.1
0.15
0.2
0.25
Number of APs per cluster
PDF
H-MAPPO
MSAC
MAPPO
Opportunistic
Figure 6. Numerical results of the average cluster size for serving mobile
UAVs.
MSAC exhibit near-zero probability for cluster sizes greater
than or equal to 13, whereas the Opportunistic scheme peaks
at a cluster size of 16, essentially involving all APs in the
cluster.
To underscore the need for the hierarchical approach over
the centralized method for joint clustering and power allocation,
we assess the scalability of our proposed H-MAPPO algorithm
in comparison to the centralized MSAC approach. The results
in Figure 7 show the time required to complete an episode in
both H-MAPPO and MSAC, relative to the maximum episode
time, as the number of APs in the network increases. The
findings highlight the superior scalability of the H-MAPPO
algorithm, where the decision-making for clustering and power
allocation is distributed across two levels: the high-level edge
cloud for clustering and the low-level APs for power control. In
contrast, MSAC relies on a single centralized agent to manage
all decisions, making it less scalable as the network grows.


---

Page 12

---

12
5
10
15
20
25
30
0
0.2
0.4
0.6
0.8
1
Number of APs
Fraction of the Time
H-MAPPO
MSAC
Figure 7. Numerical results of the relative time needed to complete an episode
during policy training.
A key observation from the results is that when the number of
APs doubles from 16 to 32, the training time for H-MAPPO
increases by only about 10 % per episode, while the same
increase in MSAC leads to a 90 % rise in training time. This
stark difference underscores the efficiency of H-MAPPO,
as it distributes the decision-making process across agents,
reducing the computational load on a single entity. Moreover,
this improvement in scalability does not come at the cost of
performance. The distributed nature of H-MAPPO allows it to
maintain or even improve system performance while scaling
more efficiently than the centralized MSAC approach.
VI. CONCLUSION
In this paper, we have investigated the mobility management
for multi-connectivity users in an wireless interference network
under stringent reliability requirements. The mobility manage-
ment problem involves joint dynamic cluster reconfiguration
and energy-efficient power allocation with stringent QoS
requirements. To solve it, we first divided the joint problem
into two subproblems and propose a hierarchical two-layer
H-MAPPO-based mobility management scheme. For the first
layer of H-MAPPO, we have transformed the original multi-
connectivity subproblem into a cluster reconfiguration updating
problem, and leveraged the single agent PPO algorithm to
output an optimized clustering action. For the second layer, each
AP acts as an independent agent responsible for efficient power
allocation to their assigned users using the MAPPO algorithm.
The learning efficiency is improved through a novel action-
observation transition mechanism that makes the convergence
of the two layers possible.
Extensive simulation results verify the effectiveness of
the proposed H-MAPPO scheme in reducing both outage
probability and total transmit power. H-MAPPO achieves
an outage probability near 10−6 and operates below 60% of
maximum transmit power in 90% of instances, compared to
only 30% for opportunistic clustering methods. These results
underscore its advantage in enhancing reliability and power
efficiency for serving mobile UAVs.
In this work, we focused on user mobility within a single
cloud’s service area, with a single agent responsible for intra-
cloud cluster reconfiguration. A natural extension of this work
involves investigating scenarios where user mobility spans
multiple clouds, necessitating inter-cloud cluster reconfiguration
involving multiple agents.
REFERENCES
[1]
I. A. Meer, K.-L. Besser, M. Ozger, D. Schupke, H. V. Poor,
and C. Cavdar, “Learning based dynamic cluster reconfigura-
tion for UAV mobility management with 3D beamforming,”
in Proceedings of the 2024 IEEE International Conference
on Machine Learning for Communication and Networking
(ICMLCN), IEEE, May 2024, pp. 486–491. DOI: 10.1109/
ICMLCN59089.2024.10625071.
[2]
S. Bassoy, H. Farooq, M. A. Imran, and A. Imran, “Coordinated
multi-point clustering schemes: A survey,” IEEE Communica-
tions Surveys & Tutorials, vol. 19, no. 2, pp. 743–764, 2017.
DOI: 10.1109/COMST.2017.2662212.
[3]
F. Hu, Y. Deng, and A. H. Aghvami, “Scalable multi-agent
reinforcement learning for dynamic coordinated multipoint
clustering,” IEEE Transactions on Communications, vol. 71,
no. 1, pp. 101–114, Jan. 2023. DOI: 10.1109/TCOMM.2022.
3220870.
[4]
W. Mei, Q. Wu, and R. Zhang, “Cellular-connected UAV: Up-
link association, power control and interference coordination,”
IEEE Transactions on Wireless Communications, vol. 18, no. 11,
pp. 5380–5393, Nov. 2019. DOI: 10.1109/TWC.2019.2936021.
[5]
A. Checko, H. L. Christiansen, Y. Yan, et al., “Cloud RAN for
mobile networks — a technology overview,” IEEE Communi-
cations Surveys & Tutorials, vol. 17, no. 1, pp. 405–426, 2015.
DOI: 10.1109/COMST.2014.2355255.
[6]
E. Björnson and L. Sanguinetti, “Making cell-free massive
MIMO competitive with MMSE processing and centralized
implementation,” IEEE Transactions on Wireless Communica-
tions, pp. 77–90, Jan. 2020. DOI: 10.1109/TWC.2019.2941478.
[7]
B. Matthiesen, A. Zappone, K.-L. Besser, E. A. Jorswieck, and
M. Debbah, “A globally optimal energy-efficient power control
framework and its efficient implementation in wireless inter-
ference networks,” IEEE Transactions on Signal Processing,
vol. 68, pp. 3887–3902, 2020. DOI: 10.1109/TSP.2020.3000328.
[8]
Y. Dai, J. Liu, M. Sheng, N. Cheng, and X. Shen, “Joint
optimization of BS clustering and power control for NOMA-
enabled CoMP transmission in dense cellular networks,” IEEE
Transactions on Vehicular Technology, vol. 70, no. 2, pp. 1924–
1937, Feb. 2021. DOI: 10.1109/TVT.2021.3055769.
[9]
M. Simsek, T. Hobler, E. Jorswieck, H. Klessig, and G. Fet-
tweis, “Multiconnectivity in multicellular, multiuser systems: A
matching-based approach,” Proceedings of the IEEE, vol. 107,
no. 2, pp. 394–413, Feb. 2019. DOI: 10.1109/JPROC.2018.
2887265.
[10]
K. Yu, Q. Yu, Z. Tang, et al., “Fully-decoupled radio access
networks: A flexible downlink multi-connectivity and dynamic
resource cooperation framework,” IEEE Transactions on Wire-
less Communications, vol. 22, no. 6, pp. 4202–4214, Jun. 2023.
DOI: 10.1109/TWC.2022.3224010.
[11]
C. Wei, K. Xu, X. Xia, et al., “User-centric access point
selection in cell-free massive MIMO systems: A game-theoretic
approach,” IEEE Communications Letters, vol. 26, no. 9,
pp. 2225–2229, Sep. 2022. DOI: 10.1109/LCOMM.2022.
3186350.
[12]
Z. Liu, J. Zhang, Z. Liu, D. W. K. Ng, and B. Ai, “Joint
cooperative clustering and power control for energy-efficient
cell-free XL-MIMO with multi-agent reinforcement learning,”
IEEE Transactions on Communications, 2024. DOI: 10.1109/
TCOMM.2024.3415596, Early Access.


---

Page 13

---

13
[13]
B. Banerjee, R. C. Elliott, W. A. Krzymieñ, and M. Medra,
“Access point clustering in cell-free massive MIMO using
conventional and federated multi-agent reinforcement learning,”
IEEE Transactions on Machine Learning in Communications
and Networking, vol. 1, pp. 107–123, 2023. DOI: 10.1109/
TMLCN.2023.3283228.
[14]
T. T. Nguyen, N. D. Nguyen, and S. Nahavandi, “Deep
reinforcement learning for multiagent systems: A review of
challenges, solutions, and applications,” IEEE Transactions on
Cybernetics, vol. 50, no. 9, pp. 3826–3839, Sep. 2020. DOI:
10.1109/TCYB.2020.2977374.
[15]
R. Beerten, V. Ranjbar, A. P. Guevara, and S. Pollin, Cell-
free massive MIMO in the O-RAN architecture: Cluster and
handover strategies, Jan. 2023. arXiv: 2301.07618v1 [eess.SP].
[16]
I. A. Meer, M. Ozger, D. A. Schupke, and C. Cavdar,
“Mobility management for cellular-connected UAVs: Model-
based versus learning-based approaches for service availability,”
IEEE Transactions on Network and Service Management,
vol. 21, no. 2, pp. 2125–2139, Apr. 2024. DOI: 10.1109/
TNSM.2024.3353677.
[17]
B. Galkin, E. Fonseca, R. Amer, L. A. DaSilva, and I. Dusparic,
“REQIBA: Regression and deep Q-learning for intelligent UAV
cellular user to base station association,” IEEE Transactions
on Vehicular Technology, vol. 71, no. 1, pp. 5–20, Jan. 2022.
DOI: 10.1109/TVT.2021.3126536.
[18]
Y. Chen, X. Lin, T. Khan, and M. Mozaffari, “Efficient
drone mobility support using reinforcement learning,” in
Proceedings of the 2020 IEEE Wireless Communications and
Networking Conference (WCNC), IEEE, May 2020. DOI: 10.
1109/WCNC45663.2020.9120595.
[19]
A. Azari, F. Ghavimi, M. Ozger, R. Jantti, and C. Cavdar,
“Machine learning assisted handover and resource management
for cellular connected drones,” in Proceedings of the 2020
IEEE 91st Vehicular Technology Conference (VTC2020-Spring),
IEEE, May 2020. DOI: 10.1109/VTC2020-Spring48590.2020.
9129453.
[20]
Y. Deng, I. A. Meer, S. Zhang, M. Ozger, and C. Cavdar,
“D3QN-based trajectory and handover management for UAVs
co-existing with terrestrial users,” in Proceedings of the 21st
International Symposium on Modeling and Optimization in
Mobile, Ad Hoc, and Wireless Networks (WiOpt), IEEE, Aug.
2023, pp. 103–110. DOI: 10 . 23919 / WiOpt58741 . 2023 .
10349832.
[21]
Y. Al-Eryani, M. Akrout, and E. Hossain, “Multiple access in
cell-free networks: Outage performance, dynamic clustering,
and deep reinforcement learning-based design,” IEEE Journal
on Selected Areas in Communications, vol. 39, no. 4, pp. 1028–
1042, Apr. 2021. DOI: 10.1109/JSAC.2020.3018825.
[22]
I. A. Meer, K.-L. Besser, M. Ozger, H. V. Poor, and C. Cavdar,
“Reinforcement learning based dynamic power control for UAV
mobility management,” in Proceedings of the 57th Asilomar
Conference on Signals, Systems, and Computers, IEEE, Oct.
2023, pp. 724–728. DOI: 10.1109/IEEECONF59524.2023.
10477032.
[23]
W. Shi, J. Li, H. Wu, C. Zhou, N. Cheng, and X. Shen,
“Drone-cell trajectory planning and resource allocation for
highly mobile networks: A hierarchical DRL approach,” IEEE
Internet of Things Journal, vol. 8, no. 12, pp. 9800–9813, Jun.
2021. DOI: 10.1109/JIOT.2020.3020067.
[24]
A. Alwarafy, B. S. Ciftler, M. Abdallah, M. Hamdi, and N. Al-
Dhahir, “Hierarchical multi-agent DRL-based framework for
joint multi-RAT assignment and dynamic resource allocation
in next-generation hetnets,” IEEE Transactions on Network
Science and Engineering, vol. 9, no. 4, pp. 2481–2494, Jul.
2022. DOI: 10.1109/TNSE.2022.3164648.
[25]
T. Zhang, J. Xue, Y. Xu, et al., “Handover-free multi-
connectivity mobility management for downlink FD-RAN:
A hierarchical DRL based approach,” IEEE Transactions on
Cognitive Communications and Networking, 2024. DOI: 10.
1109/TCCN.2024.3452639, Early Access.
[26]
Ö. T. Demir, M. Masoudi, E. Björnson, and C. Cavdar,
“Cell-free massive MIMO in O-RAN: Energy-aware joint
orchestration of cloud, fronthaul, and radio resources,” IEEE
Journal on Selected Areas in Communications, vol. 42, no. 2,
pp. 356–372, Feb. 2024. DOI: 10.1109/jsac.2023.3336187.
[27]
P. J. Smith, I. Singh, P. A. Dmochowski, J. P. Coon, and
R. Green, “Flexible mobility models using stochastic differen-
tial equations,” IEEE Transactions on Vehicular Technology,
vol. 71, no. 4, pp. 4312–4321, Apr. 2022. DOI: 10.1109/TVT.
2022.3146407.
[28]
Enhanced LTE support for aerial vehicles, 3GPP TR 36.777,
version 15.0.0, 3GPP, Dec. 2017.
[29]
A. Colpaert, E. Vinogradov, and S. Pollin, “3D beamforming
and handover analysis for UAV networks,” in Proceedings of
the 2020 IEEE Globecom Workshops (GC Wkshps), IEEE, Dec.
2020. DOI: 10.1109/GCWkshps50303.2020.9367570.
[30]
A. Lancho, G. Durisi, and L. Sanguinetti, “Cell-free massive
MIMO for URLLC: A finite-blocklength analysis,” IEEE
Transactions on Wireless Communications, vol. 22, no. 12,
pp. 8723–8735, Dec. 2023. DOI: 10.1109/TWC.2023.3265303.
[31]
H. Ren, C. Pan, Y. Deng, M. Elkashlan, and A. Nallanathan,
“Joint pilot and payload power allocation for massive-MIMO-
enabled URLLC IIoT networks,” IEEE Journal on Selected
Areas in Communications, vol. 38, no. 5, pp. 816–830, May
2020. DOI: 10.1109/JSAC.2020.2980910.
[32]
A. A. Nasir, H. D. Tuan, H. Q. Ngo, T. Q. Duong, and H. V.
Poor, “Cell-free massive MIMO in the short blocklength regime
for URLLC,” IEEE Transactions on Wireless Communications,
vol. 20, no. 9, pp. 5861–5871, Sep. 2021. DOI: 10.1109/TWC.
2021.3070836.
[33]
Y. Polyanskiy, H. V. Poor, and S. Verdu, “Channel coding
rate in the finite blocklength regime,” IEEE Transactions on
Information Theory, vol. 56, no. 5, pp. 2307–2359, May 2010.
DOI: 10.1109/TIT.2010.2043769.
[34]
R. Devassy, G. Durisi, P. Popovski, and E. G. Strom, “Finite-
blocklength analysis of the ARQ-protocol throughput over the
Gaussian collision channel,” in Proceedings of the 2014 6th
International Symposium on Communications, Control and
Signal Processing (ISCCSP), IEEE, May 2014, pp. 172–177.
DOI: 10.1109/ISCCSP.2014.6877843.
[35]
S. Amari and R. Misra, “Closed-form expressions for dis-
tribution of sum of exponential random variables,” IEEE
Transactions on Reliability, vol. 46, no. 4, pp. 519–522, Dec.
1997. DOI: 10.1109/24.693785.
[36]
S. Roostaie and M. M. Ebadzadeh, EnTRPO: Trust region
policy optimization method with entropy regularization, Oct.
2021. arXiv: 2110.13373 [cs.LG].
[37]
N. Peng, Y. Lin, Y. Zhang, and J. Li, “AoI-aware joint spectrum
and power allocation for internet of vehicles: A trust region
policy optimization-based approach,” IEEE Internet of Things
Journal, vol. 9, no. 20, pp. 19 916–19 927, Oct. 2022. DOI:
10.1109/JIOT.2022.3172472.
[38]
J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O.
Klimov, Proximal policy optimization algorithms, Aug. 2017.
arXiv: 1707.06347 [cs.LG].
[39]
E. Liang, R. Liaw, P. Moritz, et al., RLlib: Abstractions for
distributed reinforcement learning, Jun. 2018. arXiv: 1712.
09381v4 [cs.AI].
