# Multi-Agent Framework for Service Restoration in Distribution Systems With Distributed Generators and Static Mobile Energy Storage Systems

## Paper Metadata

- **Filename:** Multi-Agent Framework for Service Restoration in Distribution Systems With Distributed Generators and Static_Mobile Energy Storage Systems.pdf
- **DOI:** None
- **Authors:** Not available
- **Year:** Not available
- **Journal/Venue:** Not available
- **URL:** Not available
- **Extraction Date:** 2025-06-03T15:01:20.532414
- **Total Pages:** 17

## Abstract

Abstract not available from BibTeX metadata.

## Keywords

Keywords not available from BibTeX metadata.

---

## Full Text Content



### Page 1

Received March 1, 2020, accepted March 8, 2020, date of publication March 13, 2020, date of current version March 24, 2020.
Digital Object Identifier 10.1109/ACCESS.2020.2980544
Multi-Agent Framework for Service Restoration in
Distribution Systems With Distributed Generators
and Static/Mobile Energy Storage Systems
PANGGAH PRABAWA, (Student Member, IEEE), AND DAE-HYUN CHOI
, (Member, IEEE)
School of Electrical and Electronics Engineering, Chung-Ang University, Seoul 156-756, South Korea
Corresponding author: Dae-Hyun Choi (dhchoi@ cau.ac.kr)
This work was supported in part by the National Research Foundation of Korea (NRF) through the Korea Government (MSIP) under
Grant 2018R1C1B6000965, and in part by the Chung-Ang University Research Grants in 2019.
ABSTRACT This paper presents a multi-agent system (MAS)-based approach for service restoration in a
distribution system with distributed generators (DGs), static energy storage systems (SESSs), and mobile
energy storage systems (MESSs). In comparison with existing MAS-based service restoration approaches
in a two-layer cyber-physical architecture, excluding the dispatch of MESSs, we propose a three-layer
framework that consists of cyber, physical, and transportation layers corresponding to the communication
scheme for the MAS, electric distribution system, and transportation network for MESSs, respectively.
In the proposed MAS framework, agents communicate and cooperate with each other for service restoration
without violating system operation constraints by conducting the following actions: i) Kruskal-algorithmbased island reconﬁguration (switch agent), ii) generation of switching sequence and dispatches of DGs and
SESSs (DG and static battery agents) under monitored loading condition (load agent), and iii) dispatch of
MESSs based on optimal road routing using the Dijkstra algorithm (mobile battery agent). Case studies were
carried out in an IEEE 33-bus distribution system, and the results validated the performance of the proposed
approach in terms of number of restored loads and restoration time steps, voltage level, and state of charge
of the SESSs and MESSs with different numbers of fault lines and SESSs/MESS, and different extents of
damaged roads.
INDEX TERMS
Service restoration, multi-agent system, mobile energy storage system, distributed
generator, restoration sequence, active distribution network.
NOMENCLATURE
The
main
notations
used
throughout
this
paper
are
summarized here. Other undeﬁned symbols are explained
within the text.
A. SETS
L
Set of loads in distribution network.
T
Set of restoration scheduling horizon.
GDG
Set of DGs.
GESS
Set of ESSs.
GMESS
Set of mobile ESSs.
The associate editor coordinating the review of this manuscript and
approving it for publication was Weiguo Xia
.
B. VARIABLES
It,ij
Current magnitude from node i to j at time
step t.
Vt,i
Voltage magnitude for node i at time step t.
Pt,l
Real power consumption of load l at time step t.
P(Q)t,g
Real(reactive) power generation output of DG g
at time step t.
PC(D)
t,g
Charging(discharging) real power of ESS g ∈
GESS and mobile ESS g
∈
GMESS at time
step t.
P(Q)t,ij
Real(reactive) power from node i to j at time
step t.
SOCt,g
State of charge of ESS g at time step t.
b DG
t,g
Binary variable for specifying real power generation status of DG g at time step t.
51736
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/
VOLUME 8, 2020

---


### Page 2

P. Prabawa, D.-H. Choi: Multi-Agent Framework for Service Restoration in Distribution Systems With DGs and Static/MESSs
b ESS
t,g
Binary variable for specifying charging and discharging status of ESS g at time step t.
b BR
t,ij
Binary variable for specifying real power ﬂow
status from node i to j at time step t.
b L
t,l
Binary variable for specifying load consumption
status at node l at time step t.
C. PARAMETERS
Rij
Resistance of the line from node i to j.
Xij
Reactance of the line from node i to j.
Rg
Ramping rate of the real power output
for DG g.
ωl
Load priority for load l.
ηC(D)
g
Charging(discharging) efﬁciency of ESS g.
Qcap
g
Energy capacity of ESS g.
V min(max)
Minimum(maximum) limit of the allowed
voltage range for any node.
Pmin(max)
g
Minimum(maximum) real power capacity
of DG g.
Qmin(max)
g
Minimum(maximum) reactive power capacity of DG g.
PC,min(max)
g
Minimum(maximum) charging real power
capacity of ESS g.
PD,min(max)
g
Minimum(maximum)
discharging
real
power capacity of ESS g.
Pmin(max)
ij
Minimum(maximum)
real
power
ﬂow
capacity of line from node i to j.
Qmin(max)
ij
Minimum(maximum) reactive power ﬂow
capacity of line from node i to j.
ABBREVIATIONS
The main abbreviations used throughout this paper are summarized here.
MAS
Multi-Agent System.
DSSR
Distribution System Service Restoration.
DER
Distributed Energy Resource.
DG
Distributed Generator.
PV
Photovoltaic.
SESS
Static Energy Storage System.
MESS
Mobile Energy Storage System.
SOC
State of Charge.
LA
Load Agent.
SA
Switch Agent.
HSA
Head Switch Agent.
DA
DG Agent.
BSDA
Black Start DA.
NBSDA
Non-Black Start DA.
I. INTRODUCTION
For reliable and resilient operation of electric distribution
systems under extreme weather conditions and potential
cyber attacks, power systems have attracted much attention
from both academia and industry in the context of developing self-healing smart distribution systems [1]. Self-healing
functions are typically used by system operators from a centralized distribution system control center with the aim of
rapidly identifying and isolating faulty areas, and efﬁciently
restoring the customer service. To this end, maximum load
is provided to the faulty areas through network reconﬁguration using remotely controllable switches (e.g., sectionalizing
switches and tie switches).
Recently, electric distribution systems are being integrated
with emerging smart grid technologies, including distributed
energy resources (DERs) (e.g., solar photovoltaic (PV), static
energy storage systems (SESSs), and mobile energy storage
systems (MESSs)) and demand side management. Thus, service restoration of distribution systems through self-healing
operation can be more efﬁciently conducted through the
coordination of dispatchable DERs, controllable switches,
and load shedding and shifting [2]. However, a centralized
service restoration approach could be vulnerable to a single
point of failure and have a signiﬁcantly increasing computational complexity due to the control of a large number
of heterogeneous DERs and switches along with various
demand response programs. These challenges require further
distributed service restoration through operations of smart
distribution systems.
The procedure of a self-healing distribution system mainly
consists of (1) fault identiﬁcation and isolation and (2) service
restoration. In the ﬁrst step, measurements from protective
relays and fault indicators are employed to identify faulty
locations. The faulty areas are isolated by opening the adequate switches along the distribution feeder. In the second
step, DERs locally support the load demand in the faulty
areas, and switches automatically connect the faulty areas to
non-faulty areas, thereby achieving service restoration. In this
study, we assumed that fault identiﬁcation and isolation operate well. Under this assumption, we addressed the aforementioned challenges for centralized service restoration.
We propose a distributed multi-agent service restoration for
active distribution systems with distributed generators (DGs),
SESSs, and MESSs. A more detailed review of the literature related to distribution system service restoration (DSSR)
allows categorization into the following three parts:
1) Centralized approach: To restore unserved loads quickly
and efﬁciently, service restoration approaches were traditionally designed for centralized operation, that is,
a central entity coordinates the operations of controllable switches and DERs using overall system
information in an optimization framework. Service
restoration algorithms were formulated in terms of a
mixed-integer nonlinear programming (MINLP) problem based on the bus injection formulation [3], relaxed
mixed-integer semideﬁnite programming (MISDP) [4]
in unbalanced three-phase distribution systems, and
relaxed mixed integer second-order cone programming
(MISOCP) [5], [6] in balanced three-phase distribution
systems. To address the increasing computational complexity of the MINLP problem, mixed-integer linear
programming (MILP) was used for service restoration.
VOLUME 8, 2020
51737

---


### Page 3

P. Prabawa, D.-H. Choi: Multi-Agent Framework for Service Restoration in Distribution Systems With DGs and Static/MESSs
Some examples are a two-stage service restoration strategy consisting of MILP and NLP models [7], multi-time
step service restoration in balanced three-phase distribution systems under cold load pickup conditions [8] and
unbalanced three-phase distribution systems [9], critical
load restoration using a look-ahead optimization formulation with DGs in a secondary distribution system [10],
and the analysis of the stability of microgrids in terms of
frequency deviation [11]. To consider the uncertainty in
the load and output of DGs, robust optimization-based
service restoration algorithms were developed on the
basis of the information gap decision theory [12] and
on a two-stage model using the column-and-constraint
generation method [13].
2) Hierarchical distributed approach: Hierarchical distributed models and methods were developed in a
multi-agent system (MAS) where all local agents communicated and cooperated with each other to complete
the service restoration process in a hierarchical manner.
In [14], a MAS-based approach for service restoration
was initially developed in a two-level hierarchical architecture where a bus agent at the lower level communicated only with the neighboring bus agents to restore
the local load, while a feeder agent at the upper level
facilitated the negotiation process of all load agents
globally. A two-layer framework was also presented
in [15], [16]. It consisted of a zone (or region) agent and a
feeder agent corresponding to the ﬁrst and second layers,
respectively. In this scheme, the zone agent monitors its
own zone status, communicates with the corresponding
feeder agent, and conducts the restoration action. The
feeder agent manages the actions of the zone agents
by communicating with its neighboring feeder agents.
A hybrid centralized–decentralized framework integrated with DGs was presented in [17]. In this framework, load agents and feeder agents communicated and
coordinated their actions for the desired service restoration. In [18], a three-layer service restoration framework
was presented, which consisted of a data layer for monitoring and collecting data, an agent layer for scheduling
the service restoration, and an output layer for performing the switching sequence. A new MAS-based
framework based on a reinforcement learning method,
namely the Q-learning algorithm, was proposed in [19].
In this case, historical restoration experience was used
for better future restoration process.
3) Fully distributed approach: Compared with centralized
and hierarchical distributed approaches, a fully distributed approach requires no central coordinator or
distribution network model to conduct service restoration. In [20], a MAS-based framework consisting of
a switch agent, a load agent, and a generator agent was
proposed. The performance of this framework was quantiﬁed under three different cases including full restoration, partial restoration, and alternative path restoration.
In [21], four agents, including a fault zone agent,
a zone-tie agent, a down-zone agent, and a healthy-zone
agent, were deﬁned. Each agent followed expert system rules to conduct their own restoration process
autonomously. A new fully distributed algorithm was
developed in [22]. It considers distributed ESS support in which a switch agent restores the load after
detecting, locating, and isolating a fault while a distributed ESS agent supports the distribution system in
both grid-connected and islanded modes. Two fully
distributed MAS-based approaches for service restoration were presented in [23] and [24]; they considered
controlled DG islanding and the uncertainty of load
demand together with DGs, respectively. A distributed
MAS-based communication scheme using the average
consensus algorithm was developed in [25] via local
communications between agents for global information
discovery as inputs of the optimization-based service
restoration module, which would thus become robust to
a disastrous event.
A broader range of service restoration methods and future
directions for electric distribution systems are summarized
in [26] and [27]. More recently, truck-mounted mobile emergency resources such as mobile generators and MESSs are
being increasingly used for more efﬁcient service restoration of distribution systems owing to their mobility. The
literature on service restoration with mobile emergency
resources includes critical load restoration by pre-positioning
and/or real-time allocation of mobile emergency generators
in microgrids [28], [29], development of a co-optimization
service restoration framework including the dispatch of repair
crews and MESSs [30], a joint service restoration framework using DGs and MESSs with both transportation and
distribution networks [31], and MESS scheduling for voltage
regulation via reactive power support from MESSs [32].
Extensive research has been carried out on the DSSR
problem in hierarchical and fully distributed MAS-based
approaches. However, to the best of our knowledge, previous
studies have neither presented a MAS-based approach integrated with MESSs nor investigated the impact of MESSs
on the performance of the DSSR. The novelty of this study
is that it provides a hierarchical MAS-based framework that
schedules the on/off operations of switches and dispatches
of DGs, SESSs, and MESSs to restore the unserved load efﬁciently. The main contributions of this study are summarized
as follows:
1) Compared to existing MAS-based service restoration methods in a two-layer cyber-physical architecture, excluding the dispatch of MESSs, we present a
three-layer framework that consists of cyber, physical,
and transportation layers corresponding to i) the communication scheme for the MAS, ii) electric distribution
system with switches and DERs including DGs, SESSs,
and MESSs, and iii) transportation network for MESSs,
respectively.
2) Considering the emergency situation that requires the
dispatch of MESSs, we design a communication scheme
51738
VOLUME 8, 2020

---


### Page 4

P. Prabawa, D.-H. Choi: Multi-Agent Framework for Service Restoration in Distribution Systems With DGs and Static/MESSs
where MESS agents cooperate with load agent (LA),
switch agent (SA), DG agent (DA), and SESS agent to
restore the unserved loads effectively. We adopt Dijkstra
algorithm to MESS agents for determining optimal road
routing paths for the MESSs. In addition, we investigate
the impact of MESSs under damaged road condition
on the proposed algorithm and verify that more damaged roads can change the target node of a MESS with
unserved loads with a slower service restoration time.
The simulation results conﬁrmed, under various simulation
environments, that the proposed agents can be successfully
coordinated to energize as much load as possible with different number of faulty lines and SESSs/MESSs while satisfying system operation constraints for nodal voltage in terms
of a number of restored loads and restoration time steps,
the amount of dispatch of DGs, and the state of charge of
SESSs and MESSs.
The rest of this paper is organized as follows. Section II
introduces the proposed MAS-based architecture along with
various types of agents, and addresses the problem formulation. Section III presents the proposed MAS-based service
restoration strategy. The simulation results for the proposed
service restoration approach are reported in Section IV, and
the conclusions are given in Section V.
II. SYSTEM MODEL AND PROBLEM FORMULATION
A. TYPE OF AGENT
The proposed distributed service restoration strategy is built
upon a multi-agent system where the following four types of
agents play a role in the restoration process.
1) LOAD AGENT (LA)
Each LA is associated with its load node. The LA has the
knowledge of the load ID and the amount of load demand.
This agent monitors the voltage and current at its node.
2) SWITCH AGENT (SA)
The SA detects the fault location and controls the switching of two adjacent switches at every node. This agent
has the knowledge of the switch ID, on/off status of the
switch, and the node in which the switch is deployed. Each
SA communicates with the head switch agent (HSA) at the
upper level, which conducts island reconﬁguration for maintaining a radial topology of the distribution system.
3) DG AGENT (DA)
The DA represents the generator ID, the generation capacity,
and the ramping rate of the DG. The primary goal of this agent
is to perform distribution power ﬂow analysis and calculate
the amount of available power generation at each time step.
There are two types of DAs: (1) black start DA (BSDA) and
(2) non-black start DA (NBSDA). A BSDA controls the black
start generator that is capable of providing a local power
support without depending on an external power source from
the grid. A non-black start generator can only restart with
FIGURE 1. A three-layer framework illustrating the proposed MAS-based
service restoration approach.
an external power support, and its operation is managed by
the NBSDA.
4) BATTERY AGENT (BA)
BAs are classiﬁed into two categories, namely static battery
agent (SBA) and mobile battery agent (MBA), corresponding
to ESS and MESS, respectively. The BA contains information
one the ESS/MESS ID, location of the node to which the
ESS/MESS is connected, charging and discharging power
capacities, state of energy, maximum charging and discharging capabilities, the statuses of charging and discharging, and
the number of MESSs in transit.
B. ARCHITECTURE FOR MULTI-AGENT SYSTEM
A MAS provides an effective framework and mechanism for achieving a distributed and autonomous control.
A MAS consists of different types of agents that are given
speciﬁc roles for achieving particular tasks. In this study,
we propose a MAS-based scheme where heterogeneous
agents deﬁned in the previous subsection monitor, process,
and exchange service restoration-related data with each other,
thereby leading to efﬁcient and reliable service restoration.
Fig. 1 illustrates a three-layer framework that consists of
a power system, and cyber and transportation layers, corresponding to: i) an electric distribution system with DGs,
ESSs/MESSs, switches, and loads ii) a communication network for agents and iii) a road network for MESSs. As shown
in this ﬁgure, agents interact each other in the cyber layer
through information exchange to restore the unserved load in
the power system layer efﬁciently by operating the switches
VOLUME 8, 2020
51739

---


### Page 5

P. Prabawa, D.-H. Choi: Multi-Agent Framework for Service Restoration in Distribution Systems With DGs and Static/MESSs
and DGs along with quick dispatch of MESSs in the transportation layer. A simple description for the communication procedure of the agents is as follows. The SA detects
fault locations and informs its corresponding LA about them.
Simultaneously, the SA sends the information on the fault
locations to the HSA, which in turn conducts island reconﬁguration based on this information to maintain a radial structure of post-fault distribution systems. Then, the LA shares
the information concerning the amount of unserved load with
its neighboring LAs and sends it to the corresponding DA
and BA. According to the reconﬁgured islands with the
switching status updated by the HSA, the DA communicates
each other to determine the maximum generation capacity
that can cover the unserved load in its own island at each
time step. Similarly, through the communications among BAs
(i.e., SBA and MBA), the SBA and MBA identify the capability of ESSs and MESSs for service restoration, respectively.
Furthermore, the MBA calculates the optimal road routing
path for a MESS and dispatches it to a destination for quick
service restoration.
C. PROBLEM FORMULATION
A general algorithm for the DSSR problem that produces the
optimal operation schedule of switches and DERs is formulated as a constrained optimization problem with the following objective function and equality/inequality constraints.
1) OBJECTIVE FUNCTION
The objective function for the DSSR problem is to maximize
the total restored load Pt,l in the speciﬁed time horizon T
with time interval 1t considering load priority ωl.
max
X
t∈T
X
l∈L
ωl Pt,l1t.
(1)
2) CONSTRAINTS
The current in any distribution line from node i to j and
the voltage at any node i at time step t should be maintained within their allowable limits, i.e., Imax
ij
and V min(max),
respectively,
It,ij ≤Imax
ij
(2)
V min ≤Vt,i ≤V max
(3)
where V min and V max are set to 0.95 p.u and 1.05 p.u.,
respectively.
The total power consumption of the restored load at each
time step should be less than the power provided by DGs,
ESSs and MESSs.
X
l∈L
Pt,l ≤
X
g∈GDG
Pt,g +
X
g∈GESS
(PD
t,g −PC
t,g)
(4)
+
X
g∈GMESS
(PD
t,g −PC
t,g).
(5)
where GDG, GESS, and GMESS are the sets for DG, ESS, and
ESS, respectively. PC
t,g and PD
t,g represent the charging and
discharging power of ESS (g ∈GESS) and MESS (g ∈
GMESS), respectively.
The capacity constraints of real (Pt,g) and reactive power
outputs (Qt,g) of any DG along with the constraint for the
ramping rate (Rg) of the real power output are expressed as:
b DG
t,g Pmin
g
≤Pt,g ≤b DG
t,g Pmax
g
,
g ∈GDG, t ∈T
(6)
b DG
t,g Qmin
g
≤Qt,g ≤b DG
t,g Qmax
g
,
g ∈GDG, t ∈T
(7)
−Rg1t ≤Pt,g −Pt−1,g ≤Rg1t,
g ∈GDG, t ∈T
(8)
where a binary decision variable b DG
t,g determines the energization status of DG (b DG
t,g
= 1: energized, b DG
t,g
= 0:
de-energized).
Equation (9) deﬁnes the operational dynamics of the state
of charge (SOC) for ESS g ∈GESS at current time t ∈T
in terms of the SOC at previous time t −1, charging and
discharging efﬁciency, i.e., ηC
g and ηD
g , and charging and discharging power, i.e., PC
t,g and PD
t,g, respectively. Equation (10)
expresses the capacity constraint of the SOC for the ESS.
Equations (11) and (12) present the constraint on charging
(PC
t,g) and discharging power (PD
t,g) of the ESS, respectively,
where b ESS
t,g represents the binary decision variable that determines the on/off status of the ESS.
SOCt,g = SOCt−1,g + ηC
g PC
t,g1t −1
ηDg
PD
t,g1t
(9)
SOCmin
g
≤SOCt,g ≤SOCmax
g
(10)
PC,min
g
b ESS
t,g
≤PC
t,g ≤PC,max
g
b ESS
t,g
(11)
PD,min
g
(1 −b ESS
t,g ) ≤PD
t,g ≤PD,max
g
(1 −b ESS
t,g ).
(12)
Note that the constraints (9)–(12) also hold true for MESS
g ∈GMESS along with the road routing algorithm.
Equations (13) and (14) guarantee that the real and reactive
power ﬂows from node i to j become zero if the corresponding
line is not energized (b BR
t,ij
= 0). Otherwise, they should
be maintained within their allowable range when the line is
energized (b BR
t,ij = 1).
b BR
t,ij Pmin
ij
≤Pt,ij ≤b BR
t,ij Pmax
ij
,
(i, j) ∈B, t ∈T
(13)
b BR
t,ij Qmin
ij
≤Qt,ij ≤b BR
t,ij Qmax
ij
,
(i, j) ∈B, t ∈T .
(14)
Equation (15) limits the sudden load pickup of DGs and
ESSs/MESSs at each time step to prevent a sudden drop of
the system frequency [8]. In (15), the sudden incremental
amount of restored loads at each step must be smaller or
equal to the maximum allowable pickup power in terms of 5%
(ξDG = 0.05) and 100% (ξESS(MESS) = 1) of the total capacity of all energized DGs and ESSs/MESSs in discharging
state, respectively.
X
l∈L
Pl(b L
t,l −b L
t−1,l)
≤ξDG X
g∈GDG
b DG
t,g Pmax
g
+ξESS(MESS)
X
g∈GESS S GMESS
b DG
t,g PD,max
g
(15)
51740
VOLUME 8, 2020

---


### Page 6

P. Prabawa, D.-H. Choi: Multi-Agent Framework for Service Restoration in Distribution Systems With DGs and Static/MESSs
Algorithm
1
Kruskal
Algorithm-Based
Island
Reconﬁguration
1 function Kruskal(edges)
2 Initialize a priority queue Q to contain all edges in G
using the weights as keys
3 Deﬁne a forest T empty
4 while T has fewer than n −1 edges do
5
▷Remove the minimum weighted edge (i,j) from Q
6
//Prevent cycles in T. Add edge (i,j) only if T does
not contain a path between i and j yet
7
▷Let C(j) be the cluster containing j, and let C(i) be
the cluster containing i
8
if C(j)=C(i) then
9
▷Add edge(i,j) to T
10
▷Merge C(j) and C(i) into one cluster, that is,
union C(j) and C(i)
11
end
12 end
13 return tree T
where the energized load is considered only when the status
of the load is switched from off at time step t −1 (b L
t−1,l = 0)
to on at time step t (b L
t−1,l = 1).
III. PROPOSED SERVICE RESTORATION STRATEGY
A. ISLAND RECONFIGURATION
Given that multiple islands are created owing to multiple line
faults, the network reconﬁguration initiates with the operation of tie-switches. However, when some islands are merged
into a single one through a closing tie-switch, the reconﬁgured network may not be radially structured because additional lines associated with tie-switches can make the merged
island looped. To eliminate this loop, island reconﬁguration
is executed by the HSA.
The island reconﬁguration process is carried out using a
greedy Kruskal algorithm [33] based on graph theory. This
algorithm is formulated as a minimum spanning tree problem
that minimizes a weight inside a graph. In the graph theory
literature, an undirected graph G = (V, E) is expressed in
terms of V, which is the set of nodes or vertices, and E, which
is the set of edges. An unordered pair (i, j) belongs to the
set E if nodes i and j are connected to each other through
an edge. The weight ωij of each edge (i, j) used for island
reconﬁguration can be updated using (16), which represents
the inverse of an absolute value of the real power ﬂow Pij at
line (i, j).
ωij =
1
|Pij| =
1
R

|Vi|2

1−Vi V ∗
j
Rij−j Xij

(16)
where Rij and Xij are the values of the resistance and reactance
of line (i, j). We can observe from (16) that a higher real power
ﬂow yields a lower line loss, thus lowering the corresponding
weight. As shown in Algorithm 1, the Kruskal algorithm
Algorithm 2 Dijkstra Algorithm-Based Road Routing
of MESS
1 function Dijkstra(network, source)
2 for each road node j in network do
3
▷dist[j]:=inﬁnity
4
▷previous[j]:=undeﬁned
5 end
6 dist[source]:=0
7 Q:= the set of all nodes in graph
8 while Q is not empty do
9
▷i:= node in Q with smallest dist[ ]
10
▷Remove i from Q
11
for each neighbor j of i do
12
▷alt:=dist[i]+dist-between(i,j)
13
if alt < dist[j] then
14
▷dist[j]:=alt
15
▷previous[j]:=i
16
end
17
end
18
▷return previous[]
19 end
constructs a tree network T without loop by sequentially
deleting the line with the minimum weight. The procedure
followed by Algorithm 1 is summarized as follows.
An initial weight is calculated using (16). All the available
edges with their corresponding weights are initialized and
listed (line 2). After initializing a set T that contains the result
of the algorithm (line 3), the algorithm iteratively obtains the
desired radial network (line 4∼12). The weighted edges are
marked, spanning from node i to j (line 5). The parameter T
can not be allowed to contain cycles (line 7∼11). Nodes i and j
are separated into its own cluster (line 7). If the edge spans
from node i to j, the edge is added to T and the cluster C
is updated (line 8∼11). Finally, the algorithm provides the
desired radial distribution network T (line 13).
B. ROAD ROUTING FOR MOBILE ESS
A road routing process is required for a MESS so that its
optimal charing and discharging schedules can be efﬁciently
determined. In general, the Dijkstra algorithm is used as a
road routing method to ﬁnd the shortest path such that the
travel time of the MESS is minimized, thereby leading to
more rapid restoration of the non-energized load through
faster MESS dispatching.
The Dijkstra algorithm solves the problem of ﬁnding the
shortest path from a source node to a destination node in a
graph [34]. Given a node j inside a graph G, the algorithm
calculates the fastest route between an initial source node and
the target node j. In this study, the node and edge deﬁned in
the Dijkstra algorithm represents the road node and the road,
respectively, and the weight corresponds to the road length
between two adjacent road nodes. The pseudocode of the
Dijkstra algorithm is shown in Algorithm 2.
VOLUME 8, 2020
51741

---


### Page 7

P. Prabawa, D.-H. Choi: Multi-Agent Framework for Service Restoration in Distribution Systems With DGs and Static/MESSs
The Dijkstra algorithm starts with two input data, namely
the road network topology, including each road length, and
a source road node. The initial distance between the source
node and other node j is set (line 2∼4). Any node j other than
the source node is assumed to have inﬁnite distance. This
inﬁnite distance guarantees that the other nodes in the next
iteration can be selected according to their minimum distance.
After setting the distance from the source node to itself as zero
(line 6) and storing all the nodes from the graph to the set Q
(line 7), the iterative algorithm proceeds until all the nodes
are eliminated from the set Q in the subsequent procedure
(line 8∼19). The node i with the smallest distance from the
source node is deleted from Q (lines 9 and 10). For each
unvisited neighboring node j to node i (line 11), the temporary
distance from i to j, namely alt, is calculated (line 12). If alt
is less than the known distance for node j, the distance for
node j is updated (line 13∼16). The visited node j is updated
if all the neighboring nodes of node i are already calculated
(line 15). The iteration goes back to line 8 with the updated
node i.
Note that some roads can be severely damaged owing to
extreme weather conditions. In this situation, the damaged
roads are excluded prior to the execution of the Dijkstra
algorithm.
C. GENERATION OF ENERGIZATION SEQUENCE
In the reconﬁgured islands resulting from Algorithm 1,
a feasible energization sequence for the optimal switching
operations can be calculated and generated by the DA. The
generated switching sequence is then sent to the SA that
controls the on/off status of the switches to energize the
corresponding switchable lines. The proposed algorithm for
energization sequence generation is shown in Algorithm 3.
This algorithm initiates by constructing the branching table
(line 1), which includes multiple paths from one source node
to different destination nodes. These multiple paths can be
constructed to restore the unserved multiple loads based on
their load priorities. A simple numerical example to show
how to construct the branching table is provided in the next
section. ‘‘Time step’’ denotes the cumulated iteration time
slot whenever the energization sequence is generated. ‘‘Load
in time step’’ and ‘‘Load demand in time step’’ represent
the total restored load and the sum of load demand at each
time step, respectively. After setting the initial value for
the aforementioned three variables (line 2∼4), the algorithm
proceeds provided that the total generation is larger than the
total load demand (line 5∼34). Here, the total generation is
given by the sum of all the generation outputs from DGs and
ESSs and the total load demand is deﬁned as the sum of the
load demand at the considered time step for each consecutive
time step. At each time step, the restorable load is iteratively
selected provided that Gen pickup is larger than the load
demand at that time step (line 8). Through distribution power
ﬂow analysis, which makes use of the load demand including
the load with the highest load priority, potential violations
of the operation constraints of the distribution system are
Algorithm 3 Energization of Switchable Lines
1 Construct the branching table
2 Time step = 1
3 Load in time step = 1
4 Load demand in time step = 0
5 while Total generation > Total load demand do
6
▷Gen pickup=0.05×Generation+Battery discharge
7
▷Search for loads with high priority in each row of
the branching table
8
while Generation pickup > load demand in time step
do
9
▷Select the load with the highest load priority
from the branching window
10
▷Calculate the load demand
11
▷Conduct distribution power ﬂow analysis
12
if Constraint is violated then
13
▷Exclude the load from the branching
window in the branching table
14
▷Continue
15
else
16
▷Choose the load with higher priority
17
if Battery status is not set then
18
if Maximum ramping rate < Generation
pickup then
19
▷Battery status=charge
20
▷Continue
21
else
22
▷Battery status=discharge
23
▷Continue
24
end
25
end
26
▷Energize the load by DG and/or ESS
27
▷Load demand in time step += load demand
28
▷Load in time step += 1
29
▷Battery status = not set
30
end
31
end
32
▷Load demand in time step = 0
33
▷Timestep+=1
34 end
tested (line 9∼11). If no violation is identiﬁed, the DGs and
ESSs restore the load at each iteration (line 17∼29). The
ESSs charge power when there is a surplus generation pickup
of DGs compared to the maximum ramping rate of DGs.
Otherwise, the ESSs discharge power. After restoring the load
by DGs and/or ESSs, the load demand at each time step is
updated and the load count at the time step increases by one
(line 26∼28). Finally, the amount of load demand at each time
step is reset and the time step is increased by one.
D. SUMMARY OF THE PROPOSED STRATEGY
When single or multiple faults occur in the distribution system, the agents deﬁned in Section II-A communicate with
51742
VOLUME 8, 2020

---


### Page 8

P. Prabawa, D.-H. Choi: Multi-Agent Framework for Service Restoration in Distribution Systems With DGs and Static/MESSs
FIGURE 2. Flowchart of the procedure of the proposed service restoration.
each other to restore the load in the islands efﬁciently and
reliably. The agents make a decision based on the island
that is formed by the fault location. The decision includes
the scheduling of the switching sequence and the dispatch
of DGs, ESSs, and MESSs. The procedure followed by the
proposed multi-agent service restoration strategy is illustrated
in Fig. 2. This procedure involves the following ﬁfteen steps:
Step 1): Single or multiple islands are formed as a result
of a faulty location. The SA informs the LA about
the faulty location and performs the corresponding
island reconﬁguration.
Step 2): In this step, the existence of the primary (black
start distributed generator (BSDG) and ESS) and
secondary (non-black start distributed generator (NBSDG)) power sources in each island is
checked. Note that the secondary power source
requires the power support from the primary
source to start its power generation.
Step 2.1): If the island consists of the primary and secondary power sources,
the NBSDA requests power from the
primary source.
Step 2.2): If the island contains only the NBSDG,
the NBSDA requests the MBA to
supply
power
to
the
NBSDG
by
dispatching MESSs. If no primary and
secondary power sources are located in
the island, the load restoration can be
done only by MESSs, whose dispatch
is performed by the MBA.
Step 3): In each island, the power sources for load restoration and the corresponding agents (i.e., DA and
BA) are identiﬁed and prepared.
Step 4): The LA sends information on the amount of load
demand to the DA and BA deﬁned in Step 3).
Step 5): The DA calculates the available generation capacity of the DG, and the BA informs the DA about
the initial SOC of the ESSs.
Step 6): By
comparing
the
available
power
of
the
DGs/ESSs with the load demand, the DA and BA
in the island conﬁrm that they supply their power
to the load.
Step 7): Algorithm 3 described in Section III-C initiates
with a time step=1 and proceeds through multiple
iterations while the generation capacity is sufﬁcient to support the loads in the island.
Step 8): According to the communication with the DA
and the BA, the total generation capacity is calculated by adding up the capacity of the DGs
and ESSs.
VOLUME 8, 2020
51743

---


### Page 9

P. Prabawa, D.-H. Choi: Multi-Agent Framework for Service Restoration in Distribution Systems With DGs and Static/MESSs
Step 9): If the total generation capacity is larger than the
total load demand, the DA and BA determine
the power sources for load restoration. Then, the
DA conducts power ﬂow analysis of the distribution system at each time step and determines
the restored loads without violating the operation constraints of the distribution system. Finally,
the DA calculates the switching sequence using the
results from power ﬂow analysis.
Step 10): If more loads need to be restored, the DA updates
the generation of the DG for the next time step
according to the following equation:
Pt+1,g = Pt,g + Rg1t.
(17)
In addition, the BA updates its SOC after energizing the loads at time step t.
SOCt+1 = SOCt −1t
Qcap
X
t∈T
PC(D)
t,g
(18)
where Qcap is the energy capacity (Wh) of the ESS,
and PC(D)
t,g
is the charging (discharging) power at
time step t. If there is no more load that can be
restored, then it goes to Step 14).
Step 11): If there is no power source or the energization
sequence calculated from Step 9) is insufﬁcient
for complete load restoration, the LA requests the
MBA to supply power.
Step 12): Using Algorithm 2 introduced in Section III-B,
the MBA identiﬁes the damaged roads and, after
excluding them, calculates the shortest path from
the source node to the destination node with the
unserved loads.
Step 13): If the aforementioned energization procedure
including MESS dispatch can not restore the load
completely, load shedding is performed.
Step 14): According to the switching sequence calculated
from Step 9), the SA turns the switches on or off.
Step 15): According to the road path calculated from
Step 12), the MBA dispatches MESSs to the destination node.
Finally, Fig. 3 shows the communication scheme among
agents for service restoration. The SA initiates the restoration process by sending the fault information to the LA
and DA, which acknowledge it. Simultaneously, the fault
information is delivered by the SA to the HSA, which performs the island reconﬁguration to maintain a radial topology
of the distribution system. The LAs request the amount of
unserved load to the DA and BA. The DA requests the load
demand and network topology after island reconﬁguration
to the LA and HSA, respectively. The DA then requests the
power support for a black-start capability if the DA controls
only the NBSDG. If the DA manages the BSDG, then it
will request the power from the BA as the supplementary
power for restoration. The DA then calculates the energization switching sequence based on the available data at every
FIGURE 3. Illustration of the communication scheme among agents.
FIGURE 4. Modified IEEE 33-bus test system.
time step while satisfying all the system operation constraints.
The switching sequence calculated by the DA is sent to the
SAs via the HSA, which controls the status of the switches.
Finally, based on the results from the previous energization
process, the DA requests the MBA to dispatch its MESS.
IV. SIMULATION RESULTS
A. SIMULATION SETUP
In this section, we analyze the performance of the proposed
MAS-based approach for service restoration in the modiﬁed
IEEE 33-bus distribution test system, as shown in Fig. 4.
The IEEE 33-bus system is modiﬁed with the following
additional equipment: one BSDG at the substation, one SESS
at node 2, four NBSDGs at nodes 18, 22, 25, and 33, and
ﬁve tie-switches between pairs of nodes (8, 21), (9, 15),
(12, 22), (18, 33), and (25, 29). Initially, one MESS is
assumed to be connected to the substation. This MESS is
in turn assumed to have an average speed of 30 km/h and
require ﬁve minutes for transit time. Tables 1 and 2 show
the operation characteristics of the ﬁve BSDGs/NBSDGs and
three SESSs/MESSs, respectively. In Table 2, a road node is
an intersection between the corresponding two road branches.
In this simulation, the road nodes include all the electrical
51744
VOLUME 8, 2020

---


### Page 10

P. Prabawa, D.-H. Choi: Multi-Agent Framework for Service Restoration in Distribution Systems With DGs and Static/MESSs
TABLE 1. Profiles of BSDG and NBSDG in the IEEE 33-bus system.
TABLE 2. Profiles of SESS and MESS in the IEEE 33-bus system.
FIGURE 5. Road topology.
buses with additional fourteen road nodes as shown in Fig. 5
where the charging stations for MESSs are marked with green
dots, corresponding to road nodes 25 and 31.
The generation capability of the NBSDGs at road nodes
10, 14, 25, and 43 corresponding to bus 22, 18, 33, and
25 can be supported by the MESSs. The weight ωl for the
l-th load priority is randomly generated from 1 to 10 based on
a uniform distribution. For simplicity, the weight is classiﬁed
into three levels, from 1 to 3, where the largest number
represents the highest priority. The energization sequence is
generated at every time step with a one-minute time interval.
In our simulation study, three cases were tested in the IEEE
33-bus system according to the number of islands after island
reconﬁguration with different number of fault lines:
• Case 1: one island with three fault lines
• Case 2: two islands with one fault line
• Case 3: four islands with seven fault lines
To investigate the impact of the SESSs and MESSs on
the performance of the proposed approach, each case above
FIGURE 6. Four islands after three fault lines in Case 1.
FIGURE 7. One island with two loops before reconfiguration in Case 1.
includes the following four scenarios with different numbers
of SESSs and MESSs:
• Scenario 1 (S1): no SESS and no MESS
• Scenario 2 (S2): one SESS
• Scenario 3 (S3): one SESS and one MESS
• Scenario 4 (S4): one SESS and two MESSs
We assume that all the switches become open when the
faults occur and the proposed restoration strategy initiates.
The proposed service restoration approach is implemented
in a computer (AMD Ryzen 7 2700X, 8 cores clocked at
3.7 GHz with 32-GB RAM in 64-bit operating system) using
MATLAB R2019b along with MATPOWER 7.0 to conduct
distribution power ﬂow analysis.
B. CASE 1
Case 1 considers the situation in which there are three fault
lines (line 2-3, line 3-4, and line 12-13). These faults give
rise to four islands, as shown in Fig. 6. This fault information
is delivered by the SAs to the two types of agents: i) LAs
for the calculation of the amount of restorable load, and
ii) the HSA for island reconﬁguration. During the island
reconﬁguration process, the HSA conducts the following two
steps: i) formation of the loops using the four tie-switches
in Fig. 7, and ii) reconﬁguration of the network with the loops
to achieve a radial network by disconnecting the lines 6-7 and
9-10 using the Kruskal algorithm (Algorithm 1) in Fig. 8.
The topology information of the radial network after island
reconﬁguration is then sent to the DA, which in turn generates
the energization sequence.
To generate the energization sequence, the HSA ﬁrst constructs the branching table. This branching table includes
the load restoration paths that are constructed by energizing
VOLUME 8, 2020
51745

---


### Page 11

P. Prabawa, D.-H. Choi: Multi-Agent Framework for Service Restoration in Distribution Systems With DGs and Static/MESSs
FIGURE 8. One island after reconfiguration in Case 1.
FIGURE 9. Updated branching table.
the switchable lines based on load priorities. The branching
table has m rows, where m is the total number of paths
from one source node (node 1) to multiple end nodes. Fig. 9
shows an example of how the branching table is updated in
Case 1 with S1. In this example, the source node is node 1,
and the end nodes are nodes 7, 10, 13, 3, and 4. Thus, a total
of ﬁve paths (m = 5) are considered. As shown in Fig. 8,
no branch split is identiﬁed in the path from node 1 to
node 21. Therefore, the elements from the second column to
the sixth column in each row of the branching table are identical. However, a branch split occurs at node 21, leading to
line 21-8 and line 21-22. Consequently, the seventh column
(with orange color) of the branching table is updated with the
end node numbers (8 and 22) of these two lines, as shown in
the initial branching table in Fig. 9.
This column, highlighted with orange color, is deﬁned
as the branching window. Let us assume that the load at
node 9 has a high load priority. Given that node 8 is in
the same row as node 9, the load restoration for node 8 is
initiated by Algorithm 3. If no constraint violation occurs in
Algorithm 3, the branching window is shifted to the right
with the updated window [9, 9, 7, 22, 9] as shown in the
updated branching table in Fig. 9. Note that the branching
window for row 4 does not shift to the right. This is because
the path associated with row 4 excludes node 9. The aforementioned process for branching table updating continues
FIGURE 10. Real power of one SESS and five DGs in S2 for Case 1.
FIGURE 11. Reactive power of one SESS and five DGs in S2 for Case 1.
until the branching window reaches the end node, as long
as the calculated energization sequence is feasible. Once the
ﬁnal energization sequence is calculated, the DA sends the
result of the calculated switching sequence to the HSA, which
in turn delivers it to the SAs. If the available power of the
DGs is insufﬁcient, the BA commands to discharge the power
of the SESSs and MESSs. If the DGs and SESSs/MESSs
do not restore the load with the energization sequence, load
shedding must be ﬁnally conducted according to the result of
the energization sequence.
We observe from Table 3 that the number and amount of
restored loads are identical for the four scenarios in Case 1.
However, note that the total number of restoration time steps
in each scenario is listed in decreasing order, namely: S1 >
S2 > S3 > S4. We can conclude from this observation that
an increasing number of ESSs and MESSs results in a faster
restoration. Table 4 compares the result of the restoration
sequence between S1 and S2 in Case 1. We can see from
this table that loads with a high priority such as L19, L9,
and L29 are restored earlier in S2 than in S1. This is because
the ESS at t
= 1 enables the NBSDGs to start earlier,
which in turn increases the total capacity of the generation
sources and the maximum load pickup associated with the
frequency response rate, thereby leading to a reduction of
the total restoration time steps. Note from Table 4 that no
load restoration is conducted at time step 8 in S2, where the
violation of the voltage constraint occurs.
Figs. 10 and 11 show the dispatch schedules of the real and
reactive power from ﬁve DGs and an ESS in S2. The negative
and positive powers of the ESS correspond to the charging
and discharging states, respectively. Note in this ﬁgure that
51746
VOLUME 8, 2020

---


### Page 12

P. Prabawa, D.-H. Choi: Multi-Agent Framework for Service Restoration in Distribution Systems With DGs and Static/MESSs
TABLE 3. Summary of test cases and scenarios.
TABLE 4. Restoration sequence for Case 1 (S1 and S2).
the dispatched real power does not violate the DG ramp rate
constraint and that the ESS can support the restoration by
injecting reactive power as well as by stabilizing the system
by absorbing reactive power.
C. CASE 2
In Case 2, we assume that a single line fault (line 1-2)
generates two islands. As shown in Fig. 12, these two islands
can be maintained with a radial topology structure through
island reconﬁguration by disconnecting lines 4-5, 6-7,
9-10, 12-13, and 25-29. In Fig. 12, it is observed that DG1
(BSDG) is located in one island including only the substation
and DG2∼DG5 (NBSDGs) is located in the other island.
The results of S1 in Case 2 reported in Table 3 show that
the proposed approach calculates an infeasible solution for
load restoration. This is expected because all the DGs in
the island separated from the substation are NBSDGs without black-start capability. By contrast, it can be observed in
S2∼S4 that the proposed approach successfully restores the
FIGURE 12. Topology of Case 2.
load where the ESS and/or MESS can supply power for the
NBSDGs to turn on for the load restoration. Note that the
amount of restored load in S2 is less than in S3 and S4. This
is because load shedding occurs at some time step where
the total load demand is larger than the total generation in
the island. Finally, similar to the observation from Case 1,
in Case 2 it is also observed that the total number of restoration time steps decreases as the ESS and/or MESS further
contribute to the load restoration.
D. CASE 3
In Case 3, the distribution system is assumed to have
seven fault lines (lines 2-3, 3-4, 6-7, 12-13, 15-16, 20-21,
and 25-29), which leads to seven islands. After island reconﬁguration, the seven islands are merged into four, as shown
in Fig. 13. We ﬁrst observe from Table 3 that the total number
of restored loads in both S1 and S2 are four, corresponding
to L1, L2, L19, and L20 in one island. This observation
VOLUME 8, 2020
51747

---


### Page 13

P. Prabawa, D.-H. Choi: Multi-Agent Framework for Service Restoration in Distribution Systems With DGs and Static/MESSs
FIGURE 13. Topology of Case 3.
FIGURE 14. SOC of SESS, MESS1, and MESS2 in S4 for Case 1.
is because the other islands have only NBSDAs without
black-start capability. Another observation is that the total
number of restoration time steps in S3 is the highest one
among the four scenarios. This is because only one MESS
is dispatched to supply power to the loads in all the islands.
By contrast, two MESSs are coordinated in S4 to restore the
load in all the islands, thereby yielding shorter restoration
time steps than in S3.
In addition, the total computation time for the proposed
approach in all cases and scenarios is provided from Table 3.
Here, the total computation time implies the sum of the
execution times for: i) Algorithms 1 and 3 under S1 and S2,
and ii) Algorithms 1, 2, and 3 under S3 and S4. We observe
from Table 3 that the proposed approach requires a small
computation time less than two seconds. This observation justiﬁes that the proposed approach is computationally efﬁcient
and practical for real-time service restoration.
E. SOC OF ESS AND VOLTAGE MAGNITUDE RESULTS
UNDER DIFFERENT CASES AND SCENARIOS
Figs. 14, 15, and 16 show the scheduled SOC of the
SESS, MESS1, and MESS2 in S4 for Cases 1, 2, and 3,
FIGURE 15. SOC of SESS, MESS1, and MESS2 in S4 for Case 2.
FIGURE 16. SOC of SESS, MESS1, and MESS2 in S4 for Case 3.
respectively. We observe from Fig. 14 that in Case 1 three
ESSs conduct the charging or discharging processes at each
time step, thus increasing or decreasing the SOC level.
During the discharging process at a certain time step, all
ESSs contribute to the restoration of loads. In particular,
it is observed from this ﬁgure that, after some time steps,
the ESS charges more power than MESS1 and MESS2.
This implies that the ESS charges power from the grid after
restoring the loads. This charging process can be conducted
because the substation is connected to the unserved load area.
We observe from Fig. 15 that in Case 2 the SOC of the
SESS decreases as the restoration time step increases and the
SESS continuously restores the loads. By contrast, as shown
in Fig. 14, the contribution of MESS1 and MESS2 to the
restoration of the load is less than that of SESS. Due to the
longer time for load restoration, MESS1 is not dispatched
to the unserved load area so that the SOC of MESS1 keeps
unaltered. MESS2 enables through the charging process that
DG5 turns on; and then, DG5 and MESS2 start to restore the
island together. We observe from Fig. 16 that in Case 3 the
SOC of the SESS does not change. Thus, the ESS does
not contribute to load restoration. This is because the island
including the ESS has a small amount of restorable loads,
which can be fully restored by DG1 in the same island.
We also observe from Fig. 16 that the SOCs of MESS1 and
MESS2 keep unchanged in the time-step periods [1, 13] and
[5, 20], respectively. These periods represent the travel time
of MESS1 and MESS2 from one island to another. Another
observation is that the two MESSs only discharge power
during the restoration time steps. This is because there is no
redundant power to use for their charging in the island.
51748
VOLUME 8, 2020

---


### Page 14

P. Prabawa, D.-H. Choi: Multi-Agent Framework for Service Restoration in Distribution Systems With DGs and Static/MESSs
FIGURE 17. Voltage magnitudes in S3 for three cases.
FIGURE 18. Voltage magnitudes in S4 for three cases.
Figs. 17 and 18 show the voltage magnitude results for
three cases under S3 and S4, respectively. It is conﬁrmed
from these ﬁgures that the voltage magnitude at any node is
maintained within its allowable limit [0.95 p.u., 1.05 p.u.].
By comparing Fig. 17 with 18, we have the following three
observations. First, for Case 1, the voltage magnitude in S4 is
slightly higher than in S3. This phenomenon derives from
the fact that an additional MESS in S4 further increases
the voltage magnitude by supplying real power to the loads.
Second, for Case 2, the voltage magnitude in both S3 and
S4 is identical. This is natural because MESS1 in S4 for
Case 2 performs neither charging nor discharging, as shown
in Fig 15, thereby leading to no impact on the voltage proﬁle.
Third, for Case 3, the voltages at buses 9, 10, and 11 are higher
in S3 than in S4. This is because load shedding occurs at these
three buses and the corresponding voltages increase.
F. IMPACT OF MESS IN DAMAGED TRANSPORTATION
NETWORK ON THE PROPOSED APPROACH
In this subsection, we investigate the impact of a MESS in
a damaged transportation network on the performance of the
proposed service restoration method. To conduct this impact
analysis in a proper way, we selected Case 3 in S4, which
includes two MESSs in four islands. As shown in Fig. 19,
we conducted the performance analysis of the proposed
method under three different scenarios: i) scenario I: no damage, ii) scenario II: two damaged roads (19-21 and 24-28),
and iii) scenario III: six damaged roads (11-18, 18-19,
19-20, 19-21, 23-24, 24-28, and 28-38). No damage scenario
was selected as a base case where the depots for the MESSs
are located at road nodes 25 and 31, and the target nodes
FIGURE 19. Illustration of three road topologies with no damage, two
damaged roads, and six damaged roads, respectively.
FIGURE 20. SOC of the SESS, MESS1, and MESS2 in S4 for Case 3 under
road damage.
for service restoration are at road nodes 43 and 10. Table 5
compares the results of the Dijkstra algorithm among three
different scenarios without and with damaged roads. We ﬁrst
observe from this table that as more roads are damaged,
the travel distance and time for the MESSs further increase.
This is because the Dijkstra algorithm selects the suboptimal
routing path excluding the damaged roads. Another observation from Table 5 and Fig. 19 is that compared to scenarios 1
and 2, in scenario 3 the initial target road nodes 43 and 10
for the source road nodes 25 and 31 are changed to road
nodes 10 and 43, respectively. We can conclude from this
observation that, under situation of damaged road, the Dijkstra algorithm changes the target road node associated with
the unserved load as well as calculates an alternative routing
path for the MESS to conduct the service restoration through
a quick MESS dispatch.
Fig. 20 shows the scheduled SOC of the SESS, MESS1,
and MESS2 in S4 for Case 3 under scenario III. Compared
to the results in Fig 16 without road damage, we observe
from Fig. 20 that MESS1 and MESS2 require one and three
more restoration time steps, respectively, thus leading to a
VOLUME 8, 2020
51749

---


### Page 15

P. Prabawa, D.-H. Choi: Multi-Agent Framework for Service Restoration in Distribution Systems With DGs and Static/MESSs
TABLE 5. Results of MESSs using the Dijkstra algorithm in Case 3 (S4) under different road conditions.
FIGURE 21. Topology of the IEEE 69-bus system after island
reconfiguration.
total of 29 restoration time steps. After MESS1 supplies the
unserved load in the island under a damaged road situation,
the SOC of the MESS1 does not decrease signiﬁcantly to
maintain the rest of the loads, differing from the result shown
in Fig 16. This is because the amount of unserved load without road damage is larger than with road damage. By contrast,
after MESS2 restores the unserved load in a different island,
the SOC of MESS2 further decreases to support the amount
of unserved load that is larger than without road damage.
Finally, we evaluate the scalability of the proposed
approach in the modiﬁed IEEE 69-bus distribution test system [35]. The IEEE 69-bus system is modiﬁed with the following additional equipments: one BSDG at the substation,
four NBSDGs at nodes 11, 18, 49, and 61 with the generation
capacities of a pair of the active and reactive power with
(5 MW, 5 MVAr), (0.8 MW, 0.6 MVAr), (1 MW, 0.9 MVAr),
(1 MW, 0.9 MVAr), and (2 MW, 1.8 MVAr), respectively.
The ﬁve tie-switches are located between pairs of nodes
(11, 43), (13, 21), (15, 46), (27, 65), and (50, 59). One SESS
is connected to node 2, and two MESSs are connected to
nodes 1 and 61. The proﬁles of SESS and MESSs are the same
as ones in the IEEE 33-bus system. The distribution system
is assumed to have seven fault lines (lines 3-4, 6-7, 12-13,
21-22, 42-43, 50-59, and 57-58). Island reconﬁguration generates four island as shown in Fig. 21. The test environment
in the IEEE 69-bus system is similar to Scenario 4 under
Case 3 in the IEEE 33-bus system.
The simulation result shows that the total computation time
for the proposed approach is 1.34 seconds, and we verify
that the proposed approach is still computationally efﬁcient in
larger distribution system. Fig. 22 shows the scheduled SOC
of the SESS, MESS1, and MESS2 in the IEEE 69-bus system. We observe from this ﬁgure that the proposed approach
requires a total of 26 restoration time steps to restore the
unserved loads completely. In this ﬁgure, the SESS does
not participate in the service restoration process because the
FIGURE 22. SOC of the SESS, MESS1, and MESS2 in the IEEE 69-bus
system.
island including the SESS has a small amount of restorable
loads, which can be completely restored by DG in the same
island. Different from the result in Fig. 16, it is observed from
Fig. 22 that the MESS1 and MESS2 stop discharging their
power to the loads in the islands at time steps 18 and 25,
respectively. This is because the capacities of DGs in the
islands are large enough to supply their power to all the loads.
To the best of the authors knowledge, this work is the
ﬁrst MAS framework for service restoration considering the
dispatch of the MESSs in active distribution systems with
DGs and SESSs. The advantage and meaningful observations
of the proposed approach can be summarized as follows:
• The proposed service restoration method through the
coordination of heterogenous agents for loads, switches,
DGs, SESSs, and MESSs can successfully increase the
total amount of restored loads and save the total number of restoration time steps while maintaining voltage
quality along the distribution feeder.
• The dispatch of the MESSs signiﬁcantly increases the
total amount of restored loads from 280 k W (with only a
single SESS) to 3,715 k W (with additional two MESSs),
which is veriﬁed from Case 3 in Table 3.
• Furthermore, the total number of restoration time steps
is reduced as more MESSs are dispatched to restore
the unserved loads. This is veriﬁed from Case 2 in
Table 3, which shows that the total number of restoration
time steps under S2 (without the MESS), S3 (with a
single MESS), and S4 (with two MESSs) are 26, 20, 18,
respectively.
• Under situation of damaged road, the Dijkstra algorithm
successfully calculates an alternative routing path for the
MESS to conduct the service restoration at the expense
of a slower service restoration time. This is veriﬁed
from Table 5.
51750
VOLUME 8, 2020

---


### Page 16

P. Prabawa, D.-H. Choi: Multi-Agent Framework for Service Restoration in Distribution Systems With DGs and Static/MESSs
• The proposed approach is computationally efﬁcient and
practical for real-time service restoration. The maximum
computation times in the IEEE 33-bus and 69-bus systems are 1.31 and 1.34 seconds, respectively.
V. CONCLUSION
In this paper, we propose a hierarchical multi-agent system
approach for service restoration in active distribution system with switches, distributed generators, and static/mobile
energy storage systems. In the proposed approach, agents for
load, switch, distributed generator, and static/mobile energy
storage system communicate and cooperate with each other
to restore the unserved loads due to extreme weather events
and potential cyber-attacks efﬁciently and quickly. Various
simulation results demonstrate that the proposed MAS-based
approach can perform a successful service restoration under
a scenario of single or multiple faults with different number
of static and mobile energy storage systems while satisfying
the system operation constraints.
In the future, we will extend the proposed MAS-based
model to a more practical service restoration framework in
a realistic unbalanced three-phase distribution system with a
voltage-dependent load model. Another interesting direction
for future research is to develop a robust MAS-based service
restoration method considering the uncertainty of renewable distributed generators and load demands under various
demand side management programs.
REFERENCES
[1] Z. Wang, B. Chen, J. Wang, and C. Chen, ‘‘Networked microgrids for
self-healing power systems,’’ IEEE Trans. Smart Grid, vol. 7, no. 1,
pp. 310–319, Jan. 2016.
[2] B. Chen, Z. Ye, C. Chen, and J. Wang, ‘‘Toward a MILP modeling framework for distribution system restoration,’’ IEEE Trans. Power Syst., vol. 34,
no. 3, pp. 1749–1760, May 2019.
[3] S. Khushalani, J. M. Solanki, and N. N. Schulz, ‘‘Optimized restoration of
unbalanced distribution systems,’’ IEEE Trans. Power Syst., vol. 22, no. 2,
pp. 624–630, May 2007.
[4] Y. Wang, Y. Xu, J. He, C.-C. Liu, K. P. Schneider, M. Hong, and
D. T. Ton, ‘‘Coordinating multiple sources for service restoration to
enhance resilience of distribution systems,’’ IEEE Trans. Smart Grid,
vol. 10, no. 5, pp. 5781–5793, Sep. 2019.
[5] R. Romero, J. F. Franco, F. B. Leao, M. J. Rider, and E. S. de Souza, ‘‘A new
mathematical model for the restoration problem in balanced radial distribution systems,’’ IEEE Trans. Power Syst., vol. 31, no. 2, pp. 1259–1268,
Mar. 2016.
[6] T. Ding, Y. Lin, Z. Bie, and C. Chen, ‘‘A resilient microgrid formation
strategy for load restoration considering master-slave distributed generators and topology reconﬁguration,’’ Appl. Energy, vol. 199, pp. 205–216,
Aug. 2017.
[7] P. L. Cavalcante, J. C. Lopez, J. F. Franco, M. J. Rider, A. V. Garcia,
M. R. R. Malveira, L. L. Martins, and L. C. M. Direito, ‘‘Centralized selfhealing scheme for electrical distribution systems,’’ IEEE Trans. Smart
Grid, vol. 7, no. 1, pp. 145–155, Jan. 2016.
[8] B. Chen, C. Chen, J. Wang, and K. L. Butler-Purry, ‘‘Multi-time step
service restoration for advanced distribution systems and microgrids,’’
IEEE Trans. Smart Grid, vol. 9, no. 6, pp. 6793–6805, Nov. 2018.
[9] B. Chen, C. Chen, J. Wang, and K. L. Butler-Purry, ‘‘Sequential service
restoration for unbalanced distribution systems and microgrids,’’ IEEE
Trans. Power Syst., vol. 33, no. 2, pp. 1507–1520, Mar. 2018.
[10] Y. Xu, C.-C. Liu, Z. Wang, K. Mo, K. P. Schneider, F. K. Tuffner, and
D. T. Ton, ‘‘DGs for service restoration to critical loads in a secondary
network,’’ IEEE Trans. Smart Grid, vol. 10, no. 1, pp. 435–447, Jan. 2019.
[11] Y. Xu, C.-C. Liu, K. P. Schneider, F. K. Tuffner, and D. T. Ton, ‘‘Microgrids
for service restoration to critical load in a resilient distribution system,’’
IEEE Trans. Smart Grid, vol. 9, no. 1, pp. 426–437, Jan. 2018.
[12] K. Chen, W. Wu, B. Zhang, and H. Sun, ‘‘Robust restoration decisionmaking model for distribution networks based on information gap decision
theory,’’ IEEE Trans. Smart Grid, vol. 6, no. 2, pp. 587–597, Mar. 2015.
[13] X. Chen, W. Wu, and B. Zhang, ‘‘Robust restoration method for
active distribution networks,’’ IEEE Trans. Power Syst., vol. 31, no. 5,
pp. 4005–4015, Sep. 2016.
[14] T. Nagata, Y. Tao, and H. Sasaki, ‘‘A multi-agent approach to power
system restoration,’’ IEEE Trans. Power Syst., vol. 17, no. 2, pp. 457–462,
May 2002.
[15] A. Zidan and E. F. El-Saadany, ‘‘A cooperative multiagent framework
for self-healing mechanisms in distribution systems,’’ IEEE Trans. Smart
Grid, vol. 3, no. 3, pp. 1525–1539, Sep. 2012.
[16] Z. Dong, L. Lin, L. Guan, H. Chen, and Q. Liang, ‘‘A service restoration
strategy for active distribution network based on multiagent system,’’ in
Proc. IEEE Innov. Smart Grid Technol. Asia (ISGT Asia), Singapore,
May 2018, pp. 384–389.
[17] A. Elmitwally, M. Elsaid, M. Elgamal, and Z. Chen, ‘‘A fuzzy-multiagent
service restoration scheme for distribution system with distributed generation,’’ IEEE Trans. Sustain. Energy, vol. 6, no. 3, pp. 810–821, Jul. 2015.
[18] E. Shirazi and S. Jadid, ‘‘Autonomous self-healing in smart distribution
grids using agent systems,’’ IEEE Trans Ind. Informat., vol. 15, no. 12,
pp. 6291–6301, Dec. 2019.
[19] M. J. Ghorbani, M. A. Choudhry, and A. Feliachi, ‘‘A multiagent design for
power distribution systems automation,’’ IEEE Trans. Smart Grid, vol. 7,
no. 1, pp. 329–339, Jan. 2016.
[20] J. M. Solanki, S. Khushalani, and N. N. Schulz, ‘‘A multi-agent solution to
distribution systems restoration,’’ IEEE Trans. Power Syst., vol. 22, no. 3,
pp. 1026–1034, Aug. 2007.
[21] A. Abel Hafez, W. A. Omran, and Y. G. Hegazy, ‘‘A decentralized technique for autonomous service restoration in active radial distribution networks,’’ IEEE Trans. Smart Grid, vol. 9, no. 3, pp. 1911–1919, May 2018.
[22] C. P. Nguyen and A. J. Flueck, ‘‘Agent based restoration with distributed
energy storage support in smart grids,’’ IEEE Trans. Smart Grid, vol. 3,
no. 2, pp. 1029–1038, Jun. 2012.
[23] A. Sharma, D. Srinivasan, and A. Trivedi, ‘‘A decentralized multiagent
system approach for service restoration using DG islanding,’’ IEEE Trans.
Smart Grid, vol. 6, no. 6, pp. 2784–2793, Nov. 2015.
[24] A. Sharma, D. Srinivasan, and A. Trivedi, ‘‘A decentralized multi-agent
approach for service restoration in uncertain environment,’’ IEEE Trans.
Smart Grid, vol. 9, no. 4, pp. 3394–3405, Jul. 2018.
[25] C. Chen, J. Wang, F. Qiu, and D. Zhao, ‘‘Resilient distribution system
by microgrids formation after natural disasters,’’ IEEE Trans. Smart Grid,
vol. 7, no. 2, pp. 958–966, Mar. 2016.
[26] A. Zidan, M. Khairalla, A. M. Abdrabou, T. Khalifa, K. Shaban,
A. Abdrabou, R. El Shatshat, and A. M. Gaouda, ‘‘Fault detection, isolation, and service restoration in distribution systems: State-of-the-art and
future trends,’’ IEEE Trans. Smart Grid, vol. 8, no. 5, pp. 2170–2185,
Sep. 2017.
[27] F. Shen, Q. Wu, S. Huang, J. C. Lopez, C. Li, and B. Zhou, ‘‘Review
of service restoration methods in distribution networks,’’ in Proc. IEEE
PES Innov. Smart Grid Technol. Conf. Eur. (ISGT-Eur.), Sarajevo, BosniaHerzegovina, Oct. 2018, pp. 1–6.
[28] S. Lei, J. Wang, C. Chen, and Y. Hou, ‘‘Mobile emergency generator prepositioning and real-time allocation for resilient response to natural disasters,’’ IEEE Trans. Smart Grid, vol. 9, no. 3, pp. 2030–2041, May 2018.
[29] L. Che and M. Shahidehpour, ‘‘Adaptive formation of microgrids with
mobile emergency resources for critical service restoration in extreme conditions,’’ IEEE Trans. Power Syst., vol. 34, no. 1, pp. 742–753, Jan. 2019.
[30] S. Lei, C. Chen, Y. Li, and Y. Hou, ‘‘Resilient disaster recovery logistics of
distribution systems: Co-optimize service restoration with repair crew and
mobile power source dispatch,’’ IEEE Trans. Smart Grid, vol. 10, no. 6,
pp. 6187–6202, Nov. 2019.
[31] S. Yao, P. Wang, and T. Zhao, ‘‘Transportable energy storage for more
resilient distribution systems with multiple microgrids,’’ IEEE Trans.
Smart Grid, vol. 10, no. 3, pp. 3331–3341, May 2019.
[32] H. H. Abdeltawab and Y. A.-R.-I. Mohamed, ‘‘Mobile energy storage
scheduling and operation in active distribution systems,’’ IEEE Trans. Ind.
Electron., vol. 64, no. 9, pp. 6828–6840, Sep. 2017.
[33] D. P. Montoya and J. M. Ramirez, ‘‘A minimal spanning tree algorithm for
distribution networks conﬁguration,’’ in Proc. IEEE Power Energy Soc.
Gen. Meeting, San Diego, CA, USA, Jul. 2012, pp. 1–7.
VOLUME 8, 2020
51751

---


### Page 17

P. Prabawa, D.-H. Choi: Multi-Agent Framework for Service Restoration in Distribution Systems With DGs and Static/MESSs
[34] A. Javaid, ‘‘Understanding Dijkstra’s algorithm,’’ SSRN Elect. J.,
Jan. 2013, doi: 10.2139/ssrn.2340905.
[35] J. S. Savier and D. Das, ‘‘Impact of network reconﬁguration on loss
allocation of radial distribution systems,’’ IEEE Trans. Power Del., vol. 22,
no. 4, pp. 2473–2480, Oct. 2007.
PANGGAH PRABAWA (Student Member, IEEE)
received the B.E. degree in electrical engineering
from the Institute of Technology Sepuluh Nopember, Surabaya, Indonesia, in 2018. He is currently
pursuing the M.S. degree in electrical and electronics engineering with Chung-Ang University,
Seoul, South Korea. His current research interest
includes power system service restoration.
DAE-HYUN CHOI (Member, IEEE) received the
B.S. degree in electrical engineering from Korea
University, Seoul, South Korea, in 2002, and the
M.Sc. and Ph.D. degrees in electrical and computer engineering from Texas A&M University,
College Station, TX, USA, in 2008 and 2014,
respectively. He is currently an Assistant Professor with the School of Electrical and Electronics
Engineering, Chung-Ang University, Seoul. From
2002 to 2006, he was a Researcher with Korea
Telecom (KT), Seoul, where he worked on designing and implementing
home network systems. From 2014 to 2015, he was a Senior Researcher
with LG Electronics, Seoul, where he developed home energy management
systems. His research interests include power system state estimation, electricity markets, the cyber-physical security of smart grids, and the theory and
applications of cyber-physical energy systems. He received the Best Paper
Award from the 2012 Third IEEE International Conference on Smart Grid
Communications (Smart Grid Comm), Tainan City, Taiwan.
51752
VOLUME 8, 2020

---
