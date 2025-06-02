

---

Page 1

---

Fair Coordination of Distributed Energy Resources with Volt-Var Control and PV
Curtailment
Daniel Gebbrana,∗, Sleiman Mhannab, Yiju Maa, Archie C. Chapmanc, Gregor Verbiˇca
aSchool of Electrical and Information Engineering, The University of Sydney, Sydney, Australia
bDepartment of Electrical and Electronic Engineering, The University of Melbourne, Melbourne, Australia
cSchool of Information Technology and Electrical Engineering, The University of Queensland, Brisbane, Australia
Abstract
This paper presents a novel distributed optimal power ﬂow (DOPF) method for fair distributed energy resource (DER) coordination
in the context of mandated rooftop PV inverter control modes. In practice, inverter reactive power control is increasingly required
by grid connection codes, which often unfairly curtail PV generation of prosumers towards the end of low-voltage feeders. Simi-
larly, optimization-based DER coordination methods that aim solely for technically-eﬃcient DER coordination do not consider the
distribution of PV curtailment across customers. To address these concerns, we develop a tractable multi-objective DOPF method
for optimal DER coordination that (i) curtails PV generation fairly across prosumers, and (ii) incorporates a standard piecewise-
linear volt-var control reactive power control function without using integer variables. Three equity principles representing diﬀerent
interpretations of fairness are implemented in our coordination method; namely, egalitarian, proportional and uniform dynamic PV
curtailment redistribution. The performance of our approach is demonstrated on low-voltage distribution feeders of diﬀerent sizes
(5, 10, 25, 50 and 100 prosumers) using two network topologies: line topology without lateral spurs and tree topology with lateral
spurs. Each network considers three levels of PV penetration, giving 30 test systems in total. The results demonstrate the eﬀective-
ness of the proposed DOPF method for fair DER coordination: PV curtailment is equitably distributed among prosumers with a
computational burden on par with conventional DOPF approaches. Moreover, diﬀerent fairness methods result in diﬀerent patterns
of curtailment, which a regulator may choose between.
Keywords: distributed optimal power ﬂow (DOPF), distributed energy resources (DER), ADMM, prosumers, demand response,
Volt-Var Control, fair PV curtailment.
1. Introduction
The centralized power system operation paradigm is rapidly
shifting towards a more distributed one, driven by an increasing
uptake of prosumer-owned distributed energy resources (DER),
which necessitates new tools for DER management [1]. In this
context, distributed AC optimal power ﬂow (DOPF) approaches
[2–5] have emerged as an eﬀective tool for DER coordina-
tion, for three main reasons: (i) they explicitly consider net-
work constraints, (ii) they permit a prosumer-based decompo-
sition, which preserves prosumer prerogative and privacy, and
(iii) they are computationally scalable. However, the current
DOPF approaches fail to consider reactive power compensa-
tion, which is increasingly required by grid connection codes,
and tend to curtail more PV generation from prosumers at the
end of low-voltage feeders.
1.1. Background
The AC optimal power ﬂow problem is typically solved us-
ing interior-point methods (IPM). Although they only guarantee
∗Corresponding author
Email addresses: daniel.gebbran@sydney.edu.au (Daniel Gebbran),
sleiman.mhanna@unimelb.edu.au (Sleiman Mhanna),
yiju.ma@sydney.edu.au (Yiju Ma), archie.chapman@uq.edu.au
(Archie C. Chapman), gregor.verbic@sydney.edu.au (Gregor Verbiˇc)
local optimality, IPM are desirable as they can converge to fea-
sible solutions. In contrast, convex relaxations often converge
to infeasible solutions [6], but are also desirable as they provide
a lower bound on the optimal solution, which can be used to
assess the quality of the solution obtained from IPM. However,
the AC OPF problem quickly becomes intractable when consid-
ering a large number of DER and the longer optimization hori-
zons required to accommodate inter-temporal couplings (e.g.
battery storage). This therefore encouraged distributed solution
approaches.
Conceptually, distributed approaches decompose the opti-
mization problem into several smaller subproblems, where each
subproblem can be solved by an individual agent.
The so-
lution is reached by iteratively exchanging messages between
the agents until the problem converges. Distributed optimiza-
tion approaches can be hierarchical or fully distributed. The
former include a higher level central coordinator, whereas the
latter have no central entity.
Distributed optimization tech-
niques can be broadly categorized into: (i) methods based on
Lagrangian decomposition, and (ii) techniques for solving the
Karush-Kuhn-Tucker conditions in a distributed manner. We
provide a brief overview of each category next, but interested
readers are referred to [6] for a comprehensive survey of dis-
tributed optimization and control algorithms applied to power
Preprint submitted to Elsevier
March 10, 2022
arXiv:2203.04842v1  [cs.CE]  9 Mar 2022


---

Page 2

---

Nomenclature
Sets
x
Set of network variables for OPF.
ˆx
Set of network variables for DOPF.
zh
Set of prosumer variables for OPF.
ˆzh
Set of prosumer variables for DOPF.
B
Set of buses in the power network.
H
Set of prosumers in the power network.
T
Time horizon of the problem.
X
Feasible set of network variables for OPF.
ˆX
Feasible set of network variables for DOPF.
Zh
Feasible set of variables for prosumer h for OPF.
ˆZh
Feasible set of variables for prosumer h for DOPF.
Variables
qg,0,t
Active power (kW) from reference bus at time t.
qg,0,t
Reactive power (kVAr) from reference bus at t.
vi,t
Voltage (p.u.) at bus i at t.
θi j,t
Voltage phase angle between buses i and j at t.
ph,t/qh,t Active/reactive power demand (kW/kVAr) of pro-
sumer h at t.
vh,t
Voltage (p.u.) at prosumer h at t.
pbat
h,t
Battery active power (kW) of prosumer h at t.
pPV
h,t
PV active power generation (kW) of prosumer h at t.
yh,t
PV curtailment (kW) of prosumer h at t.
pch
h,t/pch
h,t Charging/discharging of prosumer’s h battery at t.
S oCh,t
State-of-charge (kW h) of prosumer’s h battery, at t.
yt
Maximum amount of PVC (kW) across all pro-
sumers, at t.
yt
Minimum amount of exported power (kW) across all
participating prosumers, at t.
λ•
h,t
Dual variable of prosumer h at t, associated with
given • (voltage, active or reactive power).
Parameters
bi j
Susceptance (p.u.) of branch ij.
gi j
Conductance (p.u.) of branch ij.
c0/c1/c2 Constant ($), linear ($/kW) and quadratic ($/kW2)
coeﬃcient terms of the network cost function.
vr,t/θr,t Reference voltage (magnitude and angle), in p.u.
cToU
t
Time-of-use tariﬀ($/kW) at time interval t of pro-
sumer cost functions.
cFiT
Feed-in-tariﬀ($/kW) of prosumer cost functions.
sh
Apparent power rating (kVA) of prosumer’s h in-
verter.
qh
Reactive power set rating (kVAr) of prosumer’s h in-
verter.
V•
Voltage setting (V) of Volt-Var Control equation.
pd
h,t
Active power demand (kW) of prosumer h at t.
˜pPV
h,t
PV power generation (kW) of prosumer h at t.
η•
h
Battery charging/discharging eﬃciency of prosumer
h.
∆t
Time interval (h) within T .
k
Iteration number.
ρ•
ADMM penalty parameter.
α
Weighting coeﬃcient for PVC penalty function.
β
Weighting coeﬃcient for reactive power VVC relax-
ation.
γ
Positive small number to avoid division by 0.
ϵabs/ϵrel Absolute and relative feasibility tolerances for
ADMM termination criteria.
µ/τ
ADMM residual balancing parameters.
•/•
Minimum/maximum magnitude operator.
•+/•−
Non-negative terms of given • = •+ −•−.
∥•∥2
2-norm (Euclidean distance) of a set.
•k
Previous variables values, used in current ADMM it-
eration k.
•k+1
Calculated variables values obtained in current
ADMM iteration k.
Abbreviations
AC
Alternating current.
ADMM Alternating direction method of multipliers.
DER
Distributed energy resources.
DNSP Distribution network service provider.
DOPF Distributed optimal power ﬂow.
KKT
Karush-Kuhn-Tucker.
MINLP Mixed-integer nonlinear programming.
OPF
Optimal power ﬂow.
PV
Photovoltaic.
PVC
Photovoltaic curtailment.
PWL
Piecewise-linear.
SOC
Second-order cone.
VVC
Volt-Var Control.
2


---

Page 3

---

systems, including mathematical formulations and convergence
properties.
1.1.1. Lagrangian-based methods
Lagrangian-based methods use the Lagrangian function of an
optimization problem with a separable structure. A decompo-
sition is obtained by duplicating (consensus) variables shared
between subproblems, e.g., voltages and/or power ﬂows. Con-
sistency between the copies is enforced by additional equality
constraints.
The simplest Lagrangian-based method is dual decomposi-
tion [7]. The basic idea is to relax the coupling constraints by
multiplying them by Lagrange multipliers (dual variables) and
adding them to the objective. The solution procedure then it-
erates between minimization of the Lagrangian over the primal
variables and maximization over the dual variables in a proce-
dure called dual ascent. Because of the decomposable struc-
ture, the minimization of the Lagrangian can be parallelized;
however the dual update needs to be computed centrally. Con-
vergence of dual ascent is often poor because the dual can be
non-smooth.
The poor convergence of the dual decomposition can be im-
proved by augmenting the Lagrangian with a quadratic penalty
on the consensus constraints, which smooths the Lagrangian
but destroys the separability of the problem. The most popular
Augmented Lagrangian-based method is the alternating direc-
tion method of multipliers (ADMM) [8], which uses alternate
minimizations over the duplicated variables, which restores the
separability.
More recently, the Augmented Lagrangian alternating direc-
tion inexact Newton (ALADIN) method was proposed to solve
distributed optimization problems [9]. Similar to ADMM, AL-
ADIN combines a coordination step between agents after solv-
ing local optimization problems based on the Augmented La-
grangian. The coordination step, however, entails solving an
equality-constrained quadratic program, obtained from sensi-
tivity evaluations of all the subproblems (gradients of local
objective functions, Hessian approximations of local objective
functions and constraints, and Jacobians of constraints). In part
due to this improved coordination step, ALADIN oﬀers locally
quadratic convergence properties and may converge faster than
ADMM, even for non-convex OPF [9].
In a diﬀerent approach, the analytical target cascading
(ATC) method [10] makes use of a hierarchical separation in
a tree structure, where parent and child subproblems share cou-
pling variables.
The coupling constraints are enforced by a
quadratic penalty relaxed function. Furthermore, it is possi-
ble to use the Augmented Lagrangian modeled within the ATC
to be solved at each subproblem, eﬀectively solving the ATC
hierarchical subproblems using ADMM.
The auxiliary problem principle (APP) [11] technique also
decomposes an optimization problem into smaller parts, solv-
ing the subproblems based on the Augmented Lagrangian and
sharing the common variables, and eventually ensuring consen-
sus between them. However, the APP uses linearized cross-
terms when modeling the Augmented Lagrangian, which sim-
pliﬁes it and decouples the subproblems in a way that does not
require a central coordinator.
1.1.2. KKT conditions-based methods
An alternative approach to Lagrangian relaxation is the dis-
tributed solution of the Karush-Kuhn-Tucker (KKT) optimality
conditions. In the optimality condition decomposition (OCD)
[12], each agent performs one Newton step to the KKT condi-
tions for its subproblem in each iteration and shares the result-
ing primal and dual variables with the neighboring agents. Each
primal and dual variable is assigned to a speciﬁc subproblem,
where all other variables are ﬁxed at their last update. The cou-
pling for these ﬁxed variables is modeled using linear penalties,
added to the objective function, which does not require a central
coordinator [6].
The consensus+innovation (C+I) algorithm [13] also solves
the KKT conditions in a distributed manner without a central
coordinator, but allows all variables in each subproblem to vary.
Each update takes into account the coupling between the neigh-
boring Lagrange multipliers, in tandem with a local innovation
term, enforcing the demand and supply power balance. The
limit point of the algorithm satisﬁes the KKT conditions.
1.2. Decomposition of the Optimal Power Flow
Diﬀerent decomposition approaches to solve the distributed
OPF problem have been studied for more than 20 years [14].
They range from region-wise decompositions [15, 16] to more
recent component-wise decomposition [17–19].
Approaches
for DER coordination typically use prosumer-based decompo-
sition, decomposing the problem at the connection point be-
tween prosumers and the network [2–5].
In prosumer-based decomposition, the home energy manage-
ment problem [20] used to schedule prosumer-owned DER is
solved in one piece. Because the only information that is ex-
changed with the aggregator is the grid demand, but not the in-
dividual device schedules, this preserves prosumer prerogative
and privacy.
Furthermore, because the prosumer subproblems can be
solved on single-board computers at prosumer premises [21],
this approach can be easily implemented in practice, as demon-
strated in a recent Australian trial [2].
Existing approaches
that use prosumer-based decomposition also solve the network
problem in one piece; this results in a signiﬁcantly lower num-
ber of iterations compared to component-based decomposition
used, for example, in [17–19]. The total solution time is well
below the DER dispatch intervals, which are typically ﬁve min-
utes or more [2, 5]. Finally, solving the network problem in one
piece by the aggregator aligns well with the hierarchical struc-
ture of DER aggregation where the aggregator assumes the role
of a central coordinator.
1.3. Literature gap
Theoretically, ALADIN allows for a prosumer-based decom-
position. However, the computation of the sensitivities for the
consensus step makes ALADIN impractical for formulations
containing nonsmooth functions, such as piecewise-linear func-
tions and problems with integer variables in general. As shown
3


---

Page 4

---

Table 1: Comparison of the existing approaches for DER coordination and voltage control with the proposed method.
[2–5]
[22]
[23–27]
[28]
[29]
[9, 17, 30–32]
This paper
DOPF with Volt-Var control and fair PV curtailment
×
DOPF with prosumer-based decomposition
×
×
Active or reactive inverter dispatch
×
×
Active and reactive inverter dispatch
×
×
×
×
×
Local voltage control with Volt-Var Control
×
×
Fair PV Curtailment
×
×
×
next, these are required in our problem formulation. APP, OCD
and C+I, on the other hand, do not require a central coordina-
tor, which does not align with the hierarchical prosumer aggre-
gation structure. Further, they require each agent to estimate
voltages and power ﬂows in each iteration. This is redundant
for prosumer-based approaches, where the aggregator computes
the network OPF, obtaining these variables’ optima at each it-
eration, and not just estimates. Hence, there are no gains from
using OCD or C+I methods in prosumer-based DOPF formu-
lations. Moreover, C+I algorithms have not been applied to
non-convex AC OPF [6]. Similarly, ATC oﬀers no beneﬁts be-
cause the prosumer-based decomposition has only two layers
of subproblems, and does not beneﬁt from further partition-
ing.
In case the prosumer-based DOPF was combined with
a higher layer OPF (e.g., a medium- and low-voltage coordi-
nation problem partitioned in three levels: MV, LV and pro-
sumers), it is possible that ATC could oﬀer beneﬁts, especially
if using ADMM to solve parent-child subproblems.
Given the drawbacks of the existing approaches mentioned
above, all the existing prosumer-based DOPF formulations for
DER coordination [2–5] use ADMM. Nevertheless, in the con-
text of Volt-Var Control (VVC) and PV curtailment, ADMM-
based approaches suﬀer from two main pitfalls.
First, they
do not consider standard inverter reactive power compensa-
tion, which is crucial for voltage regulation in medium- and
low-voltage networks [33], and is increasingly required by grid
connection codes [34–36]. The standardized VVC curves de-
ﬁned in [34–36] are piecewise-linear functions, which adds to
the complexity of the already hard, non-convex optimization
problem. Therefore, most works that consider reactive power
dispatch (in prosumer-based decomposition as well as in other
methods) do not account for these standardized functions [2–
5, 17, 29–32]. The only exception is [28], which uses a control
strategy to account for the piecewise-linear VVC in local volt-
age control instead of using OPF.
Second, a high PV penetration can result in infeasibility of
the OPF problem unless PV generation is curtailed. Still, sim-
ply allowing the OPF to curtail PV power, as in [4, 21], puts
prosumers at the end of the feeder at a disadvantage [27]. In
countries like Australia, PV penetration has reached levels that
require active network management [1, 27], which calls for a
solution that distributes curtailment in an equitable manner. A
fair redistribution of PV curtailment has been addressed both
from a control perspective [23–25] and from an optimization
perspective [27, 29]. However, both approaches [27, 29] dis-
regard DER coordination. Moreover, the existing methods use
proportional PV curtailment only. We propose two additional
PV curtailment methods, using diﬀerent notions of fairness.
1.4. Contributions
Table 1 summarizes the existing approaches for voltage con-
trol in low-voltage networks in the context of DER coordina-
tion. They treat diﬀerent aspects of the problem in isolation,
but a uniﬁed method is still missing. Against this background,
the major contribution of this paper is a novel OPF formulation
for coordination of prosumer-owned DER with a standardized
(piecewise-linear) VVC function and a fair PVC, and its im-
plementation in a computationally eﬃcient DOPF. To the best
of our knowledge, our formulation is the ﬁrst to include both
a standardized VVC function within an OPF problem, and a
fair PV curtailment within a DOPF. In a nutshell, this work is
a uniﬁed distributed framework that incorporates advantages of
previous works and further pushes the state-of-the-art for DER
coordination algorithms, while avoiding known disadvantages,
as shown in Table I.
In more detail, the proposed method features:
• Standard inverter Volt-Var control (VVC) piecewise-linear
function for reactive power compensation embedded in the
prosumer subproblem;
• Fair PV curtailment (PVC) using three diﬀerent notions of
fairness resulting in diﬀerent curtailment patterns, imple-
mented in the DOPF problem;
• Tractable1 computational performance that scales well ow-
ing to its distributed nature despite the mixed-integer non-
linear nature of the problem.2
1.5. Paper structure
This paper is structured as follows: Section 2 discusses in-
verter operation modes for voltage control in distribution net-
works, including the VVC formulation used in the proposed
DOPF approach. Section 3 formulates the DER coordination
problem.
Section 4 discusses fair PVC strategies using the
1By “tractable” we mean solvable in practice, not polynomial-time com-
putable as in computational complexity theory.
2In more detail, the problem belongs to the class of mixed-integer nonlin-
ear programming (MINLP) problems that have a non-convex continuous relax-
ation, which, when compared to MINLP problems with a convex continuous
relaxation, are more challenging to solve using current state-of-the-art MINLP
technology.
4


---

Page 5

---

three proposed equity principles. Section 5 details the prob-
lem decomposition with PVC redistribution and the resulting
formulation of the ADMM-inspired DOPF problem. Section 6
discusses the algorithm and implementation details. Section 7
presents detailed results for the 50-bus test system with tree
topology, gives a comparison across all 50 simulation cases fo-
cusing on the algorithmic performance, and discusses practical
implementation considerations. Finally, Section 8 gives con-
cluding remarks.
2. PV inverters for voltage control
In traditional distribution networks, voltage regulation only
catered for diurnal energy demand ﬂuctuations, which was done
at the substation using transformer tap-changers and capaci-
tor banks [33]. With the emergence of distributed PV gener-
ation, the slowly responding utility equipment is no longer ﬁt
for purpose. Not only does PV generation signiﬁcantly reshape
net demand patterns, it also causes power ﬂuctuations due to
rapid changes in solar insolation, which requires voltage con-
trol along the feeder.
PV inverters can address these challenges, and are increas-
ingly being used for feeder voltage control. Various standards
[34–36] oﬀer diﬀerent modes of operation:
• Fixed Power Factor mode (no voltage regulation);
• Volt-Var Control (VVC) regulates inverter reactive power
based on the voltage at the point of network coupling;
• Volt-Watt Control regulates the active power using P-V
droop control above a certain voltage;
• Power Rate Limit mode limits the rate of change of in-
verter active power output;
• Voltage Balance mode balances voltages between phases
by injecting unbalanced three-phase current.
With the increasing PV penetration, curtailment is required
to keep voltages within limits. A network company can impose
a limit on the amount of active power that can be injected into
the grid, but this is clearly suboptimal. A better solution is to
use dynamic curtailment using P-V droop control. This can be
unfair because the over-voltage at which prosumers are required
to curtail PV is not evenly distributed across the grid [27]. To
achieve a fair PV curtailment, diﬀerent approaches have been
proposed, including using voltage sensitivity information com-
puted centrally [23] or in a decentralized fashion [26] to set
adaptive droop control for inverters, and using a consensus al-
gorithm [25] to coordinate the curtailment control across pro-
sumers. More recently, the authors in [27, 29] used a central-
ized DC OPF formulation to compute fair PV curtailment. In
[29], they analyzed the dispatch of optimal active and reactive
inverter power considering a fairer curtailment, but without ac-
tually distributing all curtailment equally and fairly. This is ad-
dressed in [27], which also presents a thorough analysis of pro-
portional and economically fair PVC using diﬀerent metrics.
V1
V2
V3
V4
−q
q
V [V]
Q [VAr]
Figure 1: Generic Volt-Var Control (VVC) function.
An alternative approach is to cast the voltage control prob-
lem as an OPF problem with inverter reactive power compen-
sation and active power curtailment (APC) as decision vari-
ables [22, 30–32]. Authors in [22] and [37] formulate a re-
laxed second-order cone (SOC) OPF, where [22] calculates op-
timal inverter reactive power compensation to minimize line
losses, whereas [37] includes inverter VVC within the OPF
to account for reactive compensation when formulating an in-
vestment game to assess network PV hosting capacity. Other
approaches control both reactive power compensation and ac-
tive power curtailment: [31] formulates a SOC OPF for an
unbalanced four-wire distribution network; a Jacobi-Proximal
ADMM is employed by [32] on a decentralized peer-to-peer
network, based on voltage sensitivity coeﬃcients instead of
solving the actual OPF problem; and [30] formulates an AC
OPF, solving the resulting problem using ADMM to minimize
power losses and voltage deviations.
Yet another approach is proposed in [28], where the authors
study voltage control in distribution networks as a distributed
control problem. They show that careful design of local Volt-
Var controller is required to ensure convergence. They also
demonstrate that the power system dynamics with existing con-
trols can be interpreted as distributed algorithms for solving the
optimization problems for reactive power dispatch. The paper,
however, does not consider prosumer-owned DER, nor APC.
Our work is based upon VVC and APC. Unlike [22, 30, 31]
and similar to [28, 37], our formulation uses a standard VVC
function, using a local voltage-based response included in var-
ious international standards [34–36] and adopted by all manu-
facturers in Australia [38]. VVC is typically represented as a
deadband graph, with a region close to the nominal voltage un-
der which no response is enacted. The amount of VAr injection
or absorption based on voltage and maximum available reactive
power at each connection is given by:
qt = φ (vt) =















q,
if
vt ≤V1
q V2−vt
V2−V1 ,
if
V1 < vt < V2
0,
if
V2 ≤vt ≤V3
−q vt−V3
V4−V3 ,
if
V3 < vt < V4
−q,
if
vt ≥V4,
(1)
where q is the maximum reactive power output (normally de-
ﬁned as a percentage of the inverter’s maximum capacity s), vt
is the voltage amplitude at the point of common coupling, and
qt is the reactive power output, at any given time t. A graphical
representation of (1) is shown in Fig. 1.
Diﬀerent standards suggest or enforce diﬀerent values for V1
5


---

Page 6

---

to V4, and implementation follows the requirements of the local
distribution network service provider (DNSP) [38].
3. Distributed energy resources coordination
We formulate our proposed approach for DER coordination
as a multiperiod OPF problem. Conceptually, it consists of two
sources of costs. On the one hand, prosumers schedule their
DER to minimize energy expenditure3. On the other hand, the
distribution system operator coordinates prosumer actions to
minimize energy-based operating costs while meeting network
and operational constraints. In our formulation, the network
cost component is modeled as the cost of power generation, but
it could also be modeled as the marginal cost of losses, or the
cost of drawing power from the grid.
This is conceptually diﬀerent from bi-level optimization,
where the prosumer problem is modeled explicitly, and its so-
lution is included as a constraint in the aggregator’s problem.
Solving bi-level optimization problems requires reformulating
the lower-level problem (the prosumer problem in our case)
with its optimality KKT conditions, which are then included in
the upper level (aggregator) problem, resulting in a MILP prob-
lem; however, this can only be done for convex problems [39].
Our problem is inherently non-convex due to the AC network
constraints and also requires the use of binary variables for the
VVC functions, resulting in an MINLP with a non-convex re-
laxation. Moreover, existing bi-level models (e.g. [40, 41]) do
not consider network constraints. Solving bi-level models with
non-convex mixed-integer problems is an open research prob-
lem [39].
The objective function of our problem formulation is
minimize
x, z
F (x, z) B f
 x

+
X
h∈H
gh (zh)
=
X
t∈T
 
c2
 p+
g,0,t
2 + c1p+
g,0,t + c0 +
X
h∈H
 cToU
t
p+
h,t −cFiTp−
h,t

!
,
(2)
where f (x) represents the network OPF objective function,
gh (zh) are prosumer objective functions for each household h;
H is the set of prosumers, x is the set of network variables (ac-
tive and reactive power ﬂows, and voltages, for each t ∈T ),
zh is the set of internal variables of prosumer h for each t ∈T
(e.g., battery charging and discharging), and z B {zh}h∈H. The
network objective f (x) can include, for example, loss mini-
mization, peak load reduction, or minimizing the use of backup
diesel as in [2]. The prosumer objective gh (zh) accounts for
a ﬁxed time-of-use (ToU) tariﬀfor purchasing energy, and a
feed-in-tariﬀ(FiT) for selling excess PV generation to the grid.
For the sake of simplicity, we assume a balanced three-phase
network, which can be modeled by its single-phase equivalent.
The model can be readily extended to include unbalanced net-
works with a combination of single- and three-phase connec-
tions as in [2]. The network constraints for the OPF are given
3When cToU > cFiT, as is the case in Australia, this corresponds to PV self-
consumption.
for each bus i ∈B, and for each time interval t ∈T (index 0
denotes the reference bus):
pg,i,t −ph,t = vi,t
X
j ∈B
vj,t
 gi j cos θi j,t + bi j sin θi j,t

,
(3a)
qg,i,t −qh,t = vi,t
X
j ∈B
v j,t
 gi j sin θi j,t −bi j cos θi j,t

,
(3b)
v0,t = 1,
θ0,t = 0,
(3c)
vi ≤vi,t ≤vi,
(3d)
pg,0,t ≤pg,0,t ≤pg,0,t,
qg,0,t ≤qg,0,t ≤qg,0,t,
(3e)
where pg,i,t, qg,i,t = 0 ∀i ∈B \ 0, ph,t, qh,t are the total net
active and reactive power of prosumer h connected to bus i,4
and θi j,t = θi,t −θ j,t is the angle diﬀerence between i and its
neighboring bus j. Constraints (3a) and (3b) model the power
ﬂow equations, (3c) models the reference bus, and (3d) and (3e)
capture voltage and generator limit constraints.
On the other hand, constraints of prosumers consist of the
power balance equation
ph,t = pbat
h,t + pd
h,t −pPV
h,t ,
∀t ∈T , h ∈H,
(4)
where ph,t is the total power of household h exchanged with the
grid, with ph,t ≤ph,t ≤ph,t, pbat
h,t is the scheduled battery charg-
ing power such that pbat
h,t ≤pbat
h,t ≤pbat
h,t , pd
h,t is the household
ﬁxed demand (non-controllable), and pPV
h,t is the PV generation
power output. Additionally, let ph,t = p+
h,t −p−
h,t, where p+
h,t
and p−
h,t are non-negative terms that represent the imported and
exported active power.5
Now, we enable a reduction in PV generation by introducing
a schedulable curtailment variable yh,t. The inverter’s capacity
is also considered, which may require additional active power
curtailment according to the reactive power response. The fol-
lowing equations are introduced ∀t ∈T , h ∈H:
0 ≤pPV
h,t ≤˜pPV
h,t ,
(5a)
yh,t = ˜pPV
h,t −pPV
h,t ,
(5b)
s2
h ≥
 pPV
h,t
2 + q2
h,t,
(5c)
where ˜pPV
h,t is a parameter denoting the maximum PV generation
for prosumer h at t, and yh,t ≥0 denotes the amount of curtailed
PV power.6 For batteries, the constraints are, ∀t ∈T , h ∈H:
pbat
h,t = pch
h,t −pdis
h,t,
(6a)
S oCh,0 ≤S oCh,T,
(6b)
S oCh,t = S oCh,t−∆t +
 ηch
h pch
h,t −pdis
h,t/ηdis
h

∆t,
(6c)
4Note that prosumers have their own dedicated buses. In other words, at
most one prosumer is connected to at a certain bus i, hence H ⊂B.
5Note that because the second term in (2) is a convex piecewise linear func-
tion, at least one of the variables p+
h,t and p−
h,t can be zero at time slot t. This
therefore obviates the need to use binary variables.
6In our model, we assume batteries and PV have independent inverters. A
hybrid inverter would require slight modiﬁcations in (5c).
6


---

Page 7

---

where pch
h,t, pdis
h,t ≥0 are the battery charging and discharging
powers respectively, S oCh,t is the scheduled battery state of
charge, with S oCh,t ≤S oCh,t ≤S oCh,t,7 ηh is the battery charge
or discharge eﬃciency, and ∆t is the time interval.
Let OPF constraints (3) deﬁne a feasible set X for network
variables x. Likewise, let prosumer constraints (4), (5), and (6)
deﬁne a feasible set Zh for the variables zh (prosumer’s active
and reactive power demand, battery charging, state of charge,
and PV curtailment). Henceforth, x ∈X and zh ∈Zh, and Z is
the feasible set for all prosumer variables z.
We can rewrite the above problem in its compact form, ac-
counting for the VVC coupling between prosumers and the net-
work, which yield the following mixed-integer nonlinear pro-
gramming (MINLP) problem:8
minimize
x∈X, z∈Z
F (x, z)
(7a)
subject to qh,t = φ
 vh,t

,
∀h ∈H, t ∈T .
(7b)
This DER coordination problem is an all-encompassing
model that can be used to compute a DER-based OPF with
VVC, either centrally or in a distributed fashion.
Previous
works have utilized similar problems, but [4] and [21] do not
consider the VVC given by (7b), whereas [2] and [3] do not
account for the VVC nor the PVC given by (5b), and [37]
accounts for the VVC in a SOC OPF but does not consider
schedulable DER. However, this problem still lacks considera-
tion of the fair distribution of PV curtailment across prosumers,
which we discuss next.
4. Fair PV curtailment redistribution
To control the amount of power curtailed at prosumer PV
generation, a penalty function is added to (7a):
minimize
x∈X, z∈Z
F (x, z) + αΨ(.),
(8a)
subject to qh,t = φ
 vh,t

,
∀h ∈H, t ∈T ,
(8b)
where α > 0 is a numerical weight that determines how much a
reduction in Ψ(.) is favored over the cost minimization F (x, z)
or vice versa. For α = 0 we recover (7).
Next, constraints are introduced to problem (8) to model the
type of curtailment, encoding diﬀerent equity principles: egali-
tarian, proportional, and uniform dynamic.
4.1. Egalitarian PVC redistribution
In this case, PVC is redistributed equally among all pro-
sumers. An example of this case is shown in Fig. 2b). It can be
mathematically translated into an egalitarian objective, where
7The inclusion of (6b) avoids the full depletion of the battery, without con-
sidering the subsequent time horizon. Replacing this constraint would be rec-
ommended when implementing the algorithm in a rolling horizon basis.
8As no two prosumers share the same bus and H ⊂B, as discussed previ-
ously, we have vh,t = vi,t for prosumer h connected at bus i.
the end-goal is to achieve the lowest PVC across all prosumers.
The constraint to be included in (8) is:
yt ≥yh,t,
∀h ∈H, t ∈T ,
(9)
where yt is the highest amount of curtailed PV yh,t at any given
house, at time period t. Correspondingly, we use Ψ
Ä
y
ä
= P
t yt
as the penalty function.
4.2. Proportional PVC redistribution
In this case, each prosumer is curtailed proportionally to how
much they would be able to export on an uncongested operation
(which is diﬀerent from their actual PV generation).9 This is
shown in Fig. 2c). Once again, we use Ψ
Ä
y
ä
= P
t yt, but for the
proportional PVC redistribution, the corresponding constraint
to be considered in (8) is:
yt ≥
yh,t
p−
h,t + yh,t
,
∀h ∈H, t ∈T ,
(10)
where p−
h,t is the exported power of house h during period t. A
proportional factor now divides yh,t, corresponding to the max-
imum available export power of each prosumer.
4.3. Uniform dynamic PVC redistribution
This case employs a uniform dynamic PVC redistribution
that reduces the highest power-exporting prosumers ﬁrst. Ob-
serve in Fig. 2d) that the optimisation algorithms enforces a
smallest possible uniform export limit. The limit is determined
based on the current operating condition, hence the name dy-
namic. This stands in contrast to the current industry practice
of imposing a ﬁxed export limit irrespective of the operating
condition. We use Ψ
Ä
y
ä
= P
t
Ä
−yt
ä
. Its associated constraint
is:
yt ≤p−
h,t,
∀
¶
h ∈H |
 p−
h,t + yh,t

> yt
©
, t ∈T ,
(11)
where yt is the lowest amount of exported power p−
h,t at any
given house subject to curtailment, at time period t. In other
words, prosumers exporting less than yt are not curtailed.
5. Distributed coordination problem
The resulting DER coordination problem (8) and the corre-
sponding PVC constraint (9)-(11), account for a fair PVC shar-
ing among prosumers on top of the reactive power compensa-
tion from the VVC.
Three main complications arise when solving this problem
centrally. First, the privacy of all prosumers is violated be-
cause prosumers have to share their energy consumption details
with the central coordinator. Second, this problem is diﬃcult to
9Note that it is also possible to determine a proportional PVC based on
installed PV capacities [27]. However, the self-interested allocation of PV has
been shown to be ineﬃcient [37].
7


---

Page 8

---

p−
h,t
yh,t
0
Power
Prosumer index h
h
h
a)
b)
c)
d)
h
h
Whit
Figure 2: Examples of PVC redistribution for ﬁve households where black in-
dicates power exported and red power curtailed: a) shows the unfair base case
(i.e., curtailed as in [4, 21]) where three prosumers only export energy (black),
and two prosumers are completely curtailed (red), b) shows an egalitarian re-
distribution, c) depicts the proportional redistribution, and d) demonstrates the
uniform dynamic PVC redistribution. The gray bars show the base case. Note
the solid colors retain the same total length in all cases.
solve, consisting of a large mixed-integer problem with a non-
convex continuous relaxation that is computationally challeng-
ing in itself [42]. Third, the function introduced by the VVC
function (1) is piecewise linear (PWL) and non-convex. By in-
cluding it in the OPF formulation (8b), the problem becomes an
MINLP with a number of binary variables proportional to HT.
The problem in its central form (8) cannot be solved in a dis-
tributed fashion because it is not directly decomposable. Two
steps are necessary to decouple common variables between the
aggregator and prosumers in order to bestow a decomposable
structure, which gives rise to 1 + H subproblems.
5.1. Problem decomposition
First, constraints associated with VVC (8b) and PVC (9)-(11)
need to be included in either the network feasible set X or the
prosumer feasible sets Z. As the PVC constraint is associated
with the PVC penalty function, it is included in the network set
X. Now, the new feasible set for the network is ˆX. Similarly, as
the VVC-related constraint is related to the inverter’s reactive
power output, we include this equation in the prosumer sets Z,
which then becomes ˆZ. Another reason for this attribution of
the VVC equation to prosumer sets is to avoid further compli-
cating the already NP-hard network subproblem by adding the
mixed-integer variables associated with the PWL function.
Second, since some variables appear in both ˆX and ˆZ, the
general approach in ADMM-based solutions is to duplicate
these variables by assigning one copy for the network and one
copy for the respective prosumer.
Next, consensus between
these copies is captured by, ∀h ∈H, t ∈T ,
ˆph,t = ph,t,
(12a)
ˆyh,t = yh,t,
(12b)
ˆqh,t = qh,t,
(12c)
vi,t = vh,t,
¶
i ∈B | ∃h connected to i
©
,
(12d)
where the left-hand terms are copies for the network problem,

ˆph,t, ˆyh,t, ˆqh,t, vi,t
	
⊂ˆx ∈ˆX, and the right-hand terms are copies
for the prosumer problem,

ph,t, yh,t, qh,t, vh,t
	
⊂ˆz ∈
ˆZ. This
confers a decomposable structure on the problem.
In more
detail, duplicating the common variables allows us to rewrite
problem (8) as
minimize
ˆx ∈ˆX, ˆz ∈ˆZ
F (ˆx, ˆz) + αΨ(.),
(13a)
subject to
(12),
(13b)
where ˆx ∈ˆX is the new set of network variables, and ˆz ∈ˆZ is
the new set of prosumer variables. In this form, the sets of vari-
ables ˆX and ˆZ are decoupled, and (13a) is separable if (13b) is
relaxed (shown next). We will exploit this decomposable struc-
ture to solve the resulting problem in a distributed fashion.
The ADMM [8] capitalises on the decomposable structure
in (13) and performs alternating minimizations over sets ˆX and
ˆZh. At each iteration k, each subproblem calculates the next
set of variables denoted by k + 1. The prosumer subproblems
utilize the next set of variables k + 1 calculated by the network
OPF subproblem.
To begin with, we write the Augmented (partial) Lagrange
function of the problem:
L B F (ˆx, ˆz) + αΨ(.) +
X
t∈T
X
h∈H
Äρp
2
 ˆph,t −ph,t
2
+ λp
h,t
 ˆph,t −ph,t

+ ρy
2
 ˆyh,t −yh,t
2 + λy
h,t
 ˆyh,t −yh,t

+ ρq
2
 ˆqh,t −qh,t
2 + λq
h,t
 ˆqh,t −qh,t
 ä
= F (ˆx, ˆz) + αΨ(.) +
X
h∈H
 Lp
h + Ly
h + Lq
h

= F (ˆx, ˆz) + αΨ(.) +
X
h∈H
Lh,
(14)
where ρ > 0 is a penalty parameter associated with each type
of variable, and λ is the dual variable (Lagrangian multiplier)
associated with each coupling constraint.10
Before we reach the ﬁnal ADMM-inspired formulation, we
need to discuss three additional steps due to the nature of the
problem.
5.2. VVC relaxation
The voltage at prosumer vh,t is not determined in any way
by the household, but calculated in the network subproblem.
Therefore, instead of taking the Augmented Lagrangian of the
voltage, we instead (i) treat vk+1
h,t as an input to the prosumer sub-
problems, which yields qk+1
h,t with (1), and (ii) include a modi-
ﬁed penalty term to the network Lagrangian.
From the ﬁrst point, the PWL function for the VVC (1) is no
longer part of the prosumer optimization subproblem. Instead,
it is calculated externally, as is shown in Fig. 3. As a result, qk+1
h,t
becomes a parameter in the prosumer subproblem. We deﬁne
for each household ˜Lh = Lp
h + Ly
h.
10The dual variables for active power are used as locational marginal prices
(LMP) in other approaches to the DER coordination problem. See [43] for a
discussion on LMP.
8


---

Page 9

---

Prosumer
optimization:
calculates ˆzk+1
h
ˆpk+1
h
, ˆyk+1
h
, λk
h
vk+1
h
pk+1
h
, yk+1
h
, qk+1
h
qk+1
h
Prosumer algorithm
Aggregator
optimization:
calculates ˆxk+1
Figure 3: Algorithm ﬂowchart for DOPF with prosumer-based VVC.
From the second point, we introduce a new penalty parameter
that damps oscillations of vi,t in subsequent iterations:
Φ ( ˆq) = β
X
t∈T
X
h∈H
 ˆqh,t −ˆqk
h,t
2,
(15)
where β is a weighting factor. This equation penalizes oscil-
lations of reactive power ˆqk+1
h,t , which occur in ill-conditioned
problems. This can lead to a violation of constraint (12d) that
does not appear in the Lagrangian, because it is not a variable
in the prosumer subproblems.
This procedure greatly simpliﬁes the network problem by
removing the binary variables associated with the non-convex
piece-wise linear VVC function.
5.3. PVC constraints
Since (5b) is not accounted for in the network subproblem,
we need to limit the amount of curtailed power. We do so by
adding the following constraint to ˆX:
p−
h,t + ˆyh,t ≤p−,k
h,t + yk
h,t,
∀h ∈H, t ∈T ,
(16)
which guarantees the sum of exported and curtailed power on
the aggregator problem is never larger than the present sum of
the exported and curtailed power.
Therefore, if a prosumer
is generating power but also consuming the same amount of
power within its household, it will not be curtailed.
Moreover, a modiﬁcation is required for the proportional
PVC redistribution constraint; the prosumer constraints that
model the power and curtailed power are no longer within the
OPF (network) subproblem. Therefore, (10) is rewritten using
prosumer values from the previous iteration as parameters. We
have ∀h ∈H, t ∈T :
yt ≥
P
h∈H
yk
h,t
Ä
p−,k
h,t + yk
h,t + γ
ä P
h∈H
Ä
p−,k
h,t + yk
h,t
ä ˆyh,t,
(17)
where γ > 0 is a very small value to prevent an undeﬁned oper-
ation if no power is exported or curtailed.
5.4. Power ﬂow equations
The curtailed power value is changed within the network sub-
problem, so a small modiﬁcation of the power ﬂow equation is
needed to capture the resulting diﬀerence in each prosumer’s
power demand. Hence, we update the left-hand side of the OPF
constraint (3a), where ∀i ∈B:
pg,i,t −
 ˆph,t +
 ˆyh,t −yk
h,t

= vi,t
X
j ∈B
vj,t
 gi j cos θi j,t + bi j sin θi j,t

,
(18)
which reﬂects the new power demand from each household;
that is, considering the changes within the PVC variable in ad-
dition to the updated variable for prosumer’s demand ˆph,t.
5.5. Resulting ADMM-inspired algorithm
Finally, at a given iteration k, the next iterate k+1 is computed
by solving the following subproblems for primal variables:
ˆxk+1 B argmin
ˆx ∈ˆX

F (ˆx, ˆz) + Φ ( ˆq) + αΨ(.) +
X
h∈H
Lh

,
(19a)
qk+1
h,t B φ
 vk+1
h,t

,
∀h ∈H, t ∈T ,
(19b)
ˆzk+1
h
B argmin
ˆzh ∈ˆZh

g (ˆzh) + ˜Lh

∀h ∈H,
(19c)
and update dual variables ∀h ∈H, t ∈T :
λp,k+1
h,t
B λp,k
h,t + ρp  ˆpk+1
h,t −pk+1
h,t

,
(19d)
λy,k+1
h,t
B λy,k
h,t + ρy  ˆyk+1
h,t −yk+1
h,t

,
(19e)
λq,k+1
h,t
B λq,k
h,t + ρq  ˆqk+1
h,t −qk+1
h,t

,
(19f)
where (19a) is the subproblem solved by the aggregator (hold-
ing p, y, q constant at k), (19b) is the VVC update, (19c) is
the subproblem of each prosumer (holding ˆp, ˆy, ˆq constant at
k + 1, results of the network subproblem and VVC update), and
(19d)-(19f) are, respectively, the dual updates for λp, λy and λq.
Because problems (19b) and (19c) are decoupled, they can be
solved in parallel, for example, by individual prosumers.
6. Implementation
The proposed coordination method is described in Algorithm
1. The problem (19) is solved on a 32 GB RAM, Intel i7-7700,
3.60 GHz PC. All subproblems were implemented in Python
using Pyomo [44] as a modeling interface, and solved using
IPOPT v3.12.11 [45], with linear solver MA27 [46]. All sub-
problems were solved sequentially.
6.1. ADMM algorithmic details
We use primal and dual residuals to deﬁne the stopping cri-
teria [8]. They are, respectively:
rk B

ˆpk+1
1,0 −pk+1
1,0 , ..., ˆpk+1
H,T −pk+1
H,T, ˆyk+1
1,0 −yk+1
1,0 , ...,
ˆyk+1
H,T −yk+1
H,T, ˆpk+1
1,0 −pk+1
1,0 , ..., ˆqk+1
H,T −qk+1
H,T

=rk
p + rk
y + rk
q,
(20a)
9


---

Page 10

---

Algorithm 1 DOPF with VVC and PVC Redistribution
1: Initialization: k = 1, λ1 = 0, ρ1 = 1, vh,t = vi,t = 1 p.u., all
other variables set to zero.
2: while ∥rk∥2 > ϵpri or ∥sk∥2 > ϵdual do
3:
Compute ˆxk+1 using (19a) at aggregator.
4:
Communicate ˆpk+1
h
, ˆyk+1
h
, vk+1
h
, λk
h to all prosumers.
5:
Calculate (19b), in parallel at each prosumer
6:
Compute ˆzk+1 using (19c), in parallel at each prosumer
7:
Communicate all pk+1
h
, yk+1
h
, qk+1
h
to aggregator
8:
Update λk+1 using (19d)-(19f)
9:
Update ρk+1 using (23)
10:
k = k + 1
11: end while
sk B

ρp
 pk+1
1,0 −pk
1,0

, ..., ρp
 pk+1
H,T −pk
H,T

,
ρy
 yk+1
1,0 −yk
1,0

, ..., ρy
 yk+1
H,T −yk
H,T

,
ρq
 qk+1
1,0 −qk
1,0

, ..., ρq
 qk+1
H,T −qk
H,T
 
=sk
p + sk
y + sk
q,
(20b)
where (20a) represent the violations of the coupling equa-
tions (12a–12c) associated with the Augmented Lagrangian
(14) at the current iteration, and (20b) represents the violation
of the Karush-Kuhn-Tucker (KKT) stationarity constraints.
The termination criteria are then given by:
∥rk∥2 ≤ϵpri
and
∥sk∥2 ≤ϵdual,
(21)
where ϵpri and ϵdual are feasibility tolerances determined by the
following equations [8]:
ϵpri =
√
3HTϵabs
+ ϵrelmax

∥ˆpk + ˆyk + ˆqk∥2, ∥pk + yk + qk∥2
	
,
(22a)
ϵdual =
√
3HTϵabs + ϵrel∥λk
p + λk
y + λk
q∥2.
(22b)
In real-world applications, the standard ADMM may exhibit
poor performance due to poor conditioning of the problem. Ac-
celerated methods and adaptive penalty methods have been pro-
posed to speed up the convergence of ADMM, but accelerated
methods have been found to show no consistent or substantial
improvement on non-convex AC OPF problems. Therefore, we
adopt a residual balancing adaptive method [18], based on up-
dating diﬀerent ρ independently, according to the relative mag-
nitude of the primal and dual residuals [8]:
ρk+1
p
B







ρk
p
 1 + τincr
if
∥rk+1
p ∥2 > µincr∥sk+1
p ∥2,
ρk
p
 1 + τdecr−1
if
∥sk+1
p ∥2 > µdecr∥rk+1
p ∥2,
ρk
p
otherwise,
(23)
where τincr, τdecr > 0, µincr, µdecr > 1 are parameters that tune
how the diﬀerences between primal and dual residuals aﬀect
ρk+1
p . The same formula applies for ρy and ρq, accordingly.
For our simulations, ϵabs = 0.001, ϵrel = 0.01, τincr =
1.15, τdecr = 0.9, µincr =
1
1.15, µdecr = 1.15 for proportional and
uniform dynamic redistribution, µincr =
1
0.8, µdecr = 0.8 for egal-
itarian redistribution.
Implementations without any form of adaptive methods have
shown a very poor performance for any of the coordinated
cases, where the number iterations can be orders of magnitude
above the adaptive method. This is common among poorly con-
ditioned non-convex problems [18]. Furthermore, using sepa-
rate weights ρp, ρy and ρq has also shown signiﬁcant improve-
ment over using a single weight, which is also a known charac-
teristic of ADMM [8].
The appropriate selection of the multi-objective weights α
and β may require close attention, and are proportional to the
numerical conditioning of the problem. However, this is a gen-
eral characteristic of multi-objective problems [8]. For β, values
outside the optimal range may lead to an infeasible or slowly
converging problem. The optimal range for β was found to be
from 1 to 10.
Exceedingly high values of α can lead to slower convergence,
and values too small fail to distribute the PVC across all pro-
sumers. However, as noted in our results and mentioned in
[27], there is a trade-oﬀbetween fairly distributing PVC and
maximizing energy export, which can be seen as a cost of fair-
ness. Small values for α can be used to obtain diﬀerent fairness
trade-oﬀs. The optimal range of α was found to be from 50
to 100. Lower values of α fail to properly distributed the PVC
across all prosumers, while higher values increase the number
of iterations k.
6.2. Test networks
The proposed method was tested on low-voltage distribution
feeders of diﬀerent sizes (6, 11, 26, 51 and 101 buses) using
two network topologies: tree topology with lateral spurs and
line topology without lateral spurs. The tree topology with lat-
eral spurs is shown in Fig. 4. The network is split into subareas
of diﬀerent sizes with, respectively, 5, 10, 25, 50 and 100 pro-
sumers shown as black dots (the red dot is the connection to the
upstream medium voltage network modeled as an equivalent
generator). The line topology is simply a straight line feeder,
as in [17]. Unlike in [17], we did not use the fat-tree topology
because PV curtailment of a single prosumer does not aﬀect
other prosumers due to the connection to the medium voltage
network in between.
5
15
25
50
100
Figure 4: 6-, 16-, 26-, 51- and 101-bus networks showing buses, lines, and
the generator in red. The cyan, magenta, blue, black and red areas encompass,
respectively, 5, 15, 25, 50 and 100 prosumers.
10


---

Page 11

---

A limit for the reactive power limit of 10 % was used in the
simulations (qh = 0.1sh). The inverter capacity sh was set equal
to the PV generation capacity, which required active power cur-
tailment according to (5c) when the inverter provided reactive
power.
The voltage reference is vr = 230 V, and the volt-
age limits vi = 216 V and vi = 253 V according to the Aus-
tralian standard (230 V ± 6 %/10 %). Voltages for VVC are
V1 = 216 V, V2 = 225 V, V3 = 244 V and V4 = 253 V.
We used electricity demand and PV data with half-hourly res-
olution (∆t = 0.5) on a spring day (2011/11/07) from a recent
Australian smart grid trial [47]. All prosumers have batteries
with maximum capacity of 7.5 kW h, charging and discharging
eﬃciency η = 0.92, and maximum charging or discharging rate
of 3.75 kW. The time-of-use tariﬀcToU
t
was 0.12 $/kWh oﬀ-
peak (23:00 - 7:00), 0.22 $/kWh shoulder (7:30 - 14:00, 20:00
- 22:30), and 0.52 $/kWh peak (14:00 - 19:30), and the feed-in-
tariﬀcFiT was 0.10 $/kWh. The battery state of charge ate the
beginning of the horizon was set to S oCh,0 = 3 kW h. The APC
of scenario B limits exporting up to 2 kW for each prosumer.
The connection to the medium-voltage network is modeled as a
generator with a quadratic cost function with c2 = 0.025 $/kW2
for the three smaller networks and c2 = 0.015 $/kW2 for the
two bigger networks, and c1 = c0 = 0 for all networks.
6.3. Test cases
We applied the three fair PVC methods on each network with
three levels of PV penetration: low, medium, and high. The low
and medium cases do not require curtailment, so the choice of
the PVC method is not important. This gives 50 test cases in
total, as summarized in Table 3. In summary, we considered
the following seven scenarios:
(A) Uncoordinated: prosumers act in a selﬁsh manner, seeking
the best cost according to connection tariﬀs.
(B) Uncoordinated, VVC, ﬁxed APC: inverters have VVC en-
abled. The active power export limit is set to 2 kW for each
prosumer.
(C) Coordinated: the standard DER coordination problem [4,
21] is utilized.
(D) Coordinated, VVC: (7) implemented in a distributed man-
ner.
(E) Coordinated, VVC, PVC #1: implementation of (19) using
an egalitarian PVC redistribution.
(F) Coordinated, VVC, PVC #2: implementation of (19), us-
ing a proportional PVC redistribution.
(G) Coordinated, VVC, PVC #3: implementation of (19), us-
ing an uniform dynamic PVC redistribution.
7. Simulation results
We present the results in two parts: we ﬁrst discuss in detail
the results for the 51-bus network with tree topology and 50
prosumers (Fig. 4 black), followed by a comparison across all
50 cases focusing on the algorithmic performance only.
7.1. 50-prosumer network with tree topology
Fig. 5 shows a comparison of all seven scenarios detailed in
Section 6.3, focusing on the occurrence of voltage violations
(top graphs) and the curtailed PV generation (bottom).
Scenarios A and B: As expected in networks with a high
PV penetration, the voltage stress is very high. When uncoor-
dinated, prosumers exceed the voltage limits: over 1.3 p.u., and
under 0.93 p.u. as seen in Fig. 5a. In scenario B, shown in
Fig. 5b, we still have over-voltage because there is no coordi-
nation between agents. Due to the APC, no prosumer exceeds
25 kW h in a day of exported energy, as seen in Fig. 5l.
Scenarios C and D: When coordinating prosumers, and cur-
tailing PV generation, we can ensure proper operation within
network limits. This is shown in Fig. 5c, where voltages lie
within the required limits 0.96 - 1.1 p.u. Note, however, that
the PVC depends on the electrical distance; that is, prosumers
at the end of the feeder are curtailed more. Fig. 5j shows that
over half of the prosumers are curtailed for the most part of the
day. If we enable the VVC for all inverters, we have less volt-
age stress on the network, as shown in Fig. 5d, but we still have
an unfair (albeit smaller) PVC, shown in Fig. 5k.
Scenario E: The curtailment is spread across all prosumers
roughly equally (Fig. 5l). There are minimal ﬂuctuations of
prosumers curtailment, since some prosumers may not export
at any given time interval t. As proposed, prosumers who are
not exporting energy at t are not curtailed. Observe in Fig. 5e
how the voltage stress in the network is reduced.
Scenario F: The proportional redistribution spreads the PVC
across all prosumers in proportion to the exported power at each
interval t (Fig. 5m). Once again, there are small variations for
prosumers curtailment, because the contributions of individu-
als are diﬀerent at each t. Nevertheless, the proportion of en-
ergy curtailed versus the sum of curtailed and exported energy
ranges between 15% and 30%, which can be attributed to dif-
ferent rooftop PV orientations and demand proﬁles.
Scenario G: The uniform dynamic redistribution curtails
more aggressively prosumers who export more. Prosumers who
export less are curtailed very little or not at all, as shown in
Fig. 5n. The reduction in voltage stress on the network (Fig. 5g)
is comparable to Scenarios E and F.
7.1.1. General observations
Observe in Table 2 that the total amount of curtailed energy
P yh,t is higher among cases with a fair PVC (E, F, and G) when
compared to a similar case without a fair PVC (D). The fairness
penalty drives the pattern of curtailment away from the most ef-
ﬁcient conﬁguration of Scenario D. However, the results show
a smaller total curtailed energy when compared to the coordi-
nated case without VVC (C). This is, in turn, proportional to
the maximum reactive power qh.11
The impact of fair curtailment and the reactive power com-
pensation using VVC in the original cost function (2) is shown
11Our selected value qh = 0.1sh is below all Australian DNSP’s requirements
(which range from 0.3 to 0.6) [38], and is already enough to demonstrate the
impact of VVC in networks with a high DER penetration.
11


---

Page 12

---

1.0
1.2
Voltage [p.u.]
0
200
400
600
Occurrences
a)
UC
1.0
1.1
1.2
Voltage [p.u.]
b)
UC_VVC_fAPC
1.0
1.1
1.2
Voltage [p.u.]
c)
C
1.0
1.1
1.2
Voltage [p.u.]
d)
C_VVC
1.0
1.1
1.2
Voltage [p.u.]
e)
C_VVC_PVC#1
1.0
1.1
1.2
Voltage [p.u.]
f)
C_VVC_PVC#2
1.0
1.1
1.2
Voltage [p.u.]
g)
C_VVC_PVC#3
20
40
Prosumer index
20
0
20
40
Energy per day [kWh]
h)
Exported
Curtailed
20
40
Prosumer index
i)
20
40
Prosumer index
j)
20
40
Prosumer index
k)
20
40
Prosumer index
l)
20
40
Prosumer index
m)
20
40
Prosumer index
n)
Figure 5: Results for the 50-prosumer network with tree topology under the seven proposed scenarios. Figures a-g show the distribution of voltages vh,t over a day,
and ﬁgures h-n show the amount of energy exported P
t p−
h , in black, and curtailed P
t yh, in red, for each prosumer over a day.
Table 2: Number of iterations, parallel computation time, sum of PVC, de-
viation from the optimal cost of the solution without VVC (scenario C) and
with VVC (scenario D), and average coeﬃcient of variation of PVC, for all
distributed scenarios (C-G).
Scen.
k
tPar[s]
P yh,t [kW h]
F%C
F%D
CVyh,t
C
27
157.8
311.9
N/A
23.8
1.48
D
25
149.0
145.2
-31.2
N/A
1.87
E
19
156.4
201.3
-15.4
12.0
0.19
F
24
171.3
194.9
-18.5
9.7
0.92
G
19
165.6
227.0
-11.1
15.3
1.85
in Table 2 (columns F%C and F%D).
F%C shows the diﬀer-
ence of F(x, z) between any given scenario and the coordination
without neither VVC nor fair PVC (C), while F%D shows the
same diﬀerence with respect to Scenario D (with VVC but with-
out fair PVC). The worst case scenario is Scenario G, where
the increase in the cost function is 15.3 % compared to the op-
timal result of the DOPF without considering fair PVC (D). As
discussed previously, all scenarios outperform the original case
without VVC (C).
The diﬀerence of total curtailed energy P yh,t between sce-
narios E and F is negligible, but Scenario G has a larger
amount of curtailment. This shows that the uniform dynamic
PVC redistribution reduces the total exported energy the most.
However, the uniform dynamic PVC redistribution aﬀects the
lowest-exporting prosumers the least. Conversely, the egalitar-
ian redistribution spreads the PVC roughly equally among all
energy-exporting prosumers, curtailing lowest-exporting pro-
sumers the most. The proportional redistribution strikes a mid-
dle ground between these two.
The last column of Table 2 shows the average coeﬃcient of
variation of the curtailment CVyh,t during the daylight hours of
a day. The variation in scenarios C, D and G are very high,
which indicates the curtailment is spread unevenly. This is be-
cause prosumers are curtailed according to electrical distances
for scenarios C and D, and higher exporting prosumers are cur-
tailed more aggressively in scenario G. Scenario E shows a very
low variation (evenly spread curtailment), while Scenario F lies
somewhere between these two extremes.
0
5
10
15
20
Time [h]
100
75
50
25
0
25
50
Power [kW]
pg
X
h
(yh, t)
Scen. A
Scen. B
Scen. C
Scen. D
Scen. E
Scen. F
Scen. G
Figure 6: Cumulative PV curtailments yh,t (red) and cumulative power ﬂows
through the distribution transformer pg,t (black) for the 50-prosumer network
with tree topology for all scenarios.
7.1.2. Computational performance
The four distributed scenarios were also simulated in their
centralized form (8). Bonmin [48] is used to solve Problem (8).
However, these simulations became intractable. The simulation
did not converge for any of the VVC scenarios for the ﬁrst part
of the results (D, E, F, and G, 50-prosumer network) in more
than 72 hours. The number of binary variables resulting from
the VVC constraint was over a thousand for this network.
The number of iterations k for the algorithm to converge was
actually smaller for scenarios E, F and G, which is shown in
Table 2. The total parallel computation time tPar (the sum of
the slowest parts when solving (19)) is slightly larger, resulting
from a longer computation time per iteration due to the larger
number of variables. The number of iterations is comparable to
other approaches that use prosumer-based decomposition [2–
4].
12


---

Page 13

---

7.1.3. Network and prosumer power ﬂows
Fig. 6 shows cumulative PV curtailments yh,t and cumula-
tive power ﬂows through the distribution transformer pg,t. Ob-
serve that the power ﬂow through the distribution transformer
varies little across scenarios, with slightly more PV curtailment
in cases with PVC redistribution, as discussed in Section 7.1.1.
Fig. 7 shows power ﬂows for scenarios D, E, F and G for four
selected prosumers: two at the feeder head and two at the end of
the feeder, and two with a bigger and two with a smaller PV sys-
tem. Prosumers close to the feeder head (Figs. 7a and 7c) show
no PVC in scenario D; that is, they are only curtailed when a
fair PVC scheme is in eﬀect. Meanwhile, prosumers located
at the end of the feeder (Figs. 7b and 7d) are curtailed more
in scenario D (no PVC redistribution) when compared to sce-
narios E, F and G. Prosumers with bigger PV systems (Fig. 7c
and 7d) are curtailed more in scenarios F (proportional) and G
(uniform dynamic) when compared to scenario E (egalitarian).
Conversely, prosumers with smaller PV systems (Figs. 7a and
7b) are curtailed more in scenario E than in scenario F, and are
not curtailed at all in scenario G. These results agree with the
results in [27], both in terms of the location of the prosumers
and the size of their respective PV systems.
Table 3: Number of iterations for ﬁfty simulations with diﬀerent PV penetra-
tion, curtailment redistribution method, network size and topology.
PV Penetration
& Method
Network
Size
k
(Line topology)
k
(Tree topology with
radial spurs)
Low
5
13
15
15
12
13
25
26
17
50
27
16
100
26
18
Medium
5
23
8
15
7
6
25
29
7
50
30
8
100
28
12
High –
Egalitarian
5
28
32
15
31
22
25
35
19
50
36
19
100
45
25
High –
Proportional
5
22
18
15
33
18
25
29
16
50
27
24
100
27
19
High –
Uniform
Dynamic
5
17
12
15
16
15
25
20
20
50
23
19
100
22
22
7.2. Comparison of algorithmic performance of all cases
The number of iterations k for each of the 50 test cases is
shown in Table 3. Observe that the the number of iterations
is not directly related to the size or the type of the network,
which is also shown in [5]. In general, the line topology re-
quired a slightly larger number of iterations when compared to
the tree topology with radial spurs, which agrees with the re-
sults in [17]. Note, however, that [17] uses a component-based
decomposition so the total number of iterations is signiﬁcantly
higher. By contrast, we solve the network subproblem in one
piece, which reduces the number of iterations signiﬁcantly at
the expense of the increase in the computational burden in each
iteration.
The primal residuals (rp, ry, rq) across all ﬁfty simulations
were on average less than 0.0015 kW, and their maximum val-
ues were 0.050 kW, 0.048 kW and 0.068 kW for rp, ry, rq, re-
spectively. These values are within the same range as in [2],
which has been successfully deployed in a real-life trial. Note
that a rolling-horizon implementation used in [2] would likely
result in a faster convergence due to the warm start of each sub-
sequent horizon.
7.3. Practical implementation considerations
7.3.1. Convergence
It is known that distributed optimization approaches for the
non-convex AC OPF problem do not theoretically guarantee a
globally optimal solution [6]. However, as discussed in [6] and
demonstrated extensively in [18, 19], ADMM has been numer-
ically shown to converge on a wide range of OPF cases. Our
simulations featuring ten diﬀerent network conﬁgurations un-
der three diﬀerent levels of PV penetration, for a total of ﬁfty
diﬀerent simulation scenarios, all exhibit good convergence, as
evidenced by the vanishing primal and dual residuals. In other
words, the KKT conditions are satisﬁed since the primal and
dual residuals converge within the established tolerance [8]. It
is noteworthy that the KKT conditions are necessary to ascer-
tain a (locally) optimal point in a non-convex problem, and suf-
ﬁcient to ascertain a globally optimal point in a convex prob-
lem. The robustness shown by the results of our ADMM-based
algorithm for diﬀerent test cases agree with previous results us-
ing ADMM for non-convex DOPF problems, whether in large
systems decomposed by areas [16], in element-wise decompo-
sition [19] or in prosumer-based decomposition [2–5].
7.3.2. Parameter Settings
Furthermore, parameters need to be reset between diﬀerent
network sizes/topologies and curtailment redistribution meth-
ods (beyond the discussion in subsection 6.1). This is a known
requirement for non-convex distributed optimization problems
in general, in particular for ADMM [8, 18, 19]. However, once
the parameter settings are established for a given system and
redistribution method, any scenario can be simulated under the
same algorithmic parameter settings. This means that for im-
plementation purposes on a single network, the distribution sys-
tem operator would only need to tune the parameters once for
each desired curtailment redistribution method (or only once,
if using a single curtailment method), and proceed to operating
the algorithm with that set of parameters for all scenarios.
13


---

Page 14

---

3
2
1
0
1
2
3
Power [kW]
a)
Head of feeder
ph, t
pd
h, t
pPV
h, t
yh, t
pbat
h, t
b)
Smaller PV system
End of feeder
0
5
10
15
20
Time [h]
6
4
2
0
2
4
Power [kW]
c)
Head of feeder
Scen. D
Scen. E
Scen. F
Scen. G
0
5
10
15
20
Time [h]
d)
Larger PV system
End of feeder
Figure 7: Power ﬂows for four selected prosumers for the 50-prosumer network with tree topology for scenarios D, E, F and G. Prosumers are selected based on
the size of their PV system (small in cases a and b, big in cases c and d) and their location on the feeder (close to the feeder head in cases a and c, at the end of the
feeder in cases b and d).
7.3.3. Hardware implementation
It has been shown that edge computing devices with low pro-
cessing power are able to compute the prosumer subproblem
quickly (in less than a second), which does not impede the
deployment of this algorithm in actual distributed settings [5].
Alternatively, diﬀerent distributed computation archetypes may
be employed, such as grouping a small number of prosumers
within an area and assigning one local computing agent to han-
dle their subproblems, as has been implemented in a real-world
trial in Australia [2].
7.3.4. Communication Requirements
The proposed algorithm requires communication between
the aggregator and the prosumers. The size of the messages ex-
changed between the agents is smaller than 2 KB, which can be
accommodated using the existing last-mile network technolo-
gies, such as 4G, or networks tailored for the Internet of Things
[49] such as LTE-M, NB-IoT and EC-GSM-IoT. These tech-
nologies oﬀer suﬃciently small latencies relative to the compu-
tation time of the DOPF network subproblem so that the com-
munication delay accounts for less than 5% of the total compu-
tation time [5]. Economical aspects and limiting factors such as
low area coverage and poor internet connection would probably
play a bigger tole in choosing the appropriate network technol-
ogy.
8. Conclusion
This paper has proposed a novel approach for distributed en-
ergy resources (DER) coordination via an AC distributed op-
timal power ﬂow inspired by the alternating direction method
of multipliers (ADMM). Compared to existing methods, the
proposed solution includes a standard inverter Volt-Var Con-
trol (VVC) function for reactive power compensation and a fair
PV curtailment (PVC) distribution among prosumers, which
have previously been only addressed in isolation. The resulting
problem is a mixed-integer nonlinear problem due to the piece-
wise linear VVC function and the non-convex network prob-
lem, and is shown to be intractable if solved centrally. The
proposed distributed approach, on the other hand, is tractable
because it avoids using integer variables. Moreover, including
fair PVC and inverter VVC in the DER coordination problem
retains its privacy-preserving characteristic and the computa-
tional eﬃciency, both in terms of the computation time and the
number of iterations.
We have demonstrated the eﬀectiveness of the proposed
method on 50 diﬀerent test cases using low-voltage distribution
networks of diﬀerent sizes and topologies, and with diﬀerent
PV penetration levels. The simulation results on a large number
of diverse cases demonstrate the robustness of the proposed ap-
proach, even though ADMM does not oﬀer convergence guar-
antees for non-convex problems.
We have proposed three diﬀerent approaches for PVC redis-
tribution, each adopting diﬀerent notions of fairness. The re-
14


---

Page 15

---

sults demonstrate that the combination of inverter VVC and
PVC eﬀectively reduces voltage stress on the network with-
out penalizing prosumers at the end of the feeder. This stands
in contrast to conventional DER coordination approaches that
curtail electrically-distant prosumers the most. The overall in-
crease in the cost compared to an optimal solution with unfair
allocation PVC (with VVC) is 15.3 % in the worst-case sce-
nario.
The proposed method requires frequent message exchange
between prosumers and the central coordinator, which requires
a communication network with suﬃciently low latency and
high enough bandwidth. Current network technologies have a
suﬃciently small latency, but the impact on the communication
network traﬃc for a very large number of agents needs further
research.
References
[1] AEMO, Energy Networks Australia, . Open Energy Networks. Tech.
Rep.; 2018.
[2] Scott, P., Gordon, D., Franklin, E., Jones, L., Thi´ebaux, S.. Network-
aware coordination of residential distributed energy resources.
IEEE
Transactions on Smart Grid 2019;10(6):6528–6537.
[3] Andrianesis, P., Caramanis, M.C.. Optimal grid-distributed energy re-
source coordination. In: 57th Annual Allerton Conference on Communi-
cation, Control, and Computing (Allerton). 2019, p. 318–325.
[4] Attarha, A., Scott, P., Thi´ebaux, S.. Aﬃnely adjustable robust ADMM
for residential DER coordination in distribution networks. IEEE Transac-
tions on Smart Grid 2020;11(2):1620–1629.
[5] Gebbran, D., Mhanna, S., Chapman, A.C., Hardjawana, W., Vucetic,
B., Verbiˇc, G.. Practical considerations of DER coordination with dis-
tributed optimal power ﬂow. In: Proceedings of the 2020 International
Conference on Smart Grids and Energy Systems (SGES 2020). 2020, p.
1–6.
[6] Molzahn,
D.K., D¨orﬂer,
F., Sandberg,
H., Low,
S.H., Chakrabarti,
S., Baldick, R., et al. A survey of distributed optimization and control
algorithms for electric power systems. IEEE Transactions on Smart Grid
2017;8(6):2941–2962.
[7] Everett,
H..
Generalized lagrange multiplier method for solving
problems of optimum allocation of resources.
Operations Research
1963;11(3):399–417.
[8] Boyd, S., Parikh, N., Chu, E., Peleato, B., Eckstein, J.. Distributed
optimization and statistical learning via the alternating direction method
of multipliers. Foundations and Trends in Machine Learning 2011;3:1–
122.
[9] Engelmann, A., Jiang, Y., M¨uhlpfordt, T., Houska, B., Faulwasser, T..
Toward distributed OPF using ALADIN. IEEE Transactions on Power
Systems 2019;34(1):584–594.
[10] Tosserams, S., Papalambros, P., Etman, L., Rooda, J.. An augmented
Lagrangian relaxation for analytical target cascading using the alternating
direction method multipliers. Structural and Multidisciplinary Optimiza-
tion 2006;31:176–189.
[11] Cohen,
G..
Auxiliary problem principle and decomposition of opti-
mization problems.
Journal of Optimization Theory and Applications
1980;32:277–305.
[12] Conejo, A.J., Nogales, F.J., Prieto, F.J.. A decomposition procedure
based on approximate newton directions.
Mathematical Programming
2002;93(3):495–515. doi:10.1007/s10107-002-0304-3.
[13] Kar, S., Hug, G., Mohammadi, J., Moura, J.M.F.. Distributed state
estimation and energy management in smart grids: A consensus+ inno-
vations approach. IEEE Journal of Selected Topics in Signal Processing
2014;8(6):1022–1038. doi:10.1109/JSTSP.2014.2364545.
[14] Kim, B., Baldick, R.. Coarse-grained distributed optimal power ﬂow.
IEEE Transactions on Power Systems 1997;12(2):932–939.
[15] Erseghe, T.. Distributed optimal power ﬂow using ADMM. IEEE Trans-
actions on Power Systems 2014;29(5):2370–2380.
[16] Guo,
J., Hug,
G., Tonguz,
O.K.. A case for nonconvex distributed
optimization in large-scale power systems. IEEE Transactions on Power
Systems 2017;32(5):3842–3851.
[17] Peng, Q., Low, S.H.. Distributed optimal power ﬂow algorithm for radial
networks, I: Balanced single phase cas. IEEE Transactions on Smart Grid
2018;9(1):111–121.
[18] Mhanna, S., Verbiˇc, G., Chapman, A.C.. Adaptive ADMM for dis-
tributed AC optimal power ﬂow. IEEE Transactions on Power Systems
2019;34(3):2025–2035.
[19] Mhanna, S., Chapman, A.C., Verbiˇc, G.. Component-based dual de-
composition methods for the OPF problem. Sustainable Energy, Grids
and Networks 2018;16:91–109.
[20] Azuatalam, D., Paridari, K., Ma, Y., F¨orstl, M., Chapman, A.C., Verbiˇc,
G.. Energy management of small-scale PV-battery systems. Renewable
and Sustainable Energy Reviews 2019;112:555–570.
[21] Gebbran, D., Verbiˇc, G., Chapman, A.C., Mhanna, S.. Coordination of
prosumer agents via distributed optimal power ﬂow. In: Proceedings of
the 19th International Conference on Autonomous Agents and Multiagent
Systems (AAMAS 2020). 2020, p. 1–3.
[22] Farivar,
M., Neal,
R., Clarke,
C., Low,
S.. Optimal inverter VAR
control in distribution systems with high PV penetration. In: 2012 IEEE
Power and Energy Society General Meeting. 2012, p. 1–7.
[23] Tonkoski, R., Lopes, L.A.C., El-Fouly, T.H.M.. Coordinated active
power curtailment of grid connected PV inverters for overvoltage preven-
tion. IEEE Transactions on Sustainable Energy 2011;2(2):139–147.
[24] Dom´ınguez-Garc´ıa, A.D., Cady, S.T., Hadjicostis, C.N.. Decentralized
optimal dispatch of distributed energy resources. In: 2012 IEEE 51st
IEEE Conference on Decision and Control (CDC). 2012, p. 3688–3693.
[25] Haque, A.N.M.M., Xiong, M., Nguyen, P.H.. Consensus algorithm for
fair power curtailment of PV systems in LV networks. In: 2019 IEEE PES
GTD Grand International Conference and Exposition Asia (GTD Asia).
2019, p. 813–818.
[26] Alyami, S., Wang, Y., Wang, C., Zhao, J., Zhao, B.. Adaptive real
power capping method for fair overvoltage regulation of distribution net-
works with high penetration of PV systems. IEEE Transactions on Smart
Grid 2014;5(6):2729–2738.
[27] Liu, M., Procopiou, A., Petrou, K., Ochoa, L., Langstaﬀ, T., Hard-
ing, J., et al. On the fairness of PV curtailment schemes in residential
distribution networks. IEEE Transactions on Smart Grid 2020;.
[28] Zhou, X., Farivar, M., Liu, Z., Chen, L., Low, S.. Reverse and for-
ward engineering of local voltage control in distribution networks. IEEE
Transactions on Automatic Control 2020;:1–1Early access.
[29] Lusis, P., Andrew, L.L.H., Chakraborty, S., Liebman, A., Tack, G..
Reducing the unfairness of coordinated inverter dispatch in PV-rich dis-
tribution networks. In: 2019 IEEE Milan PowerTech. 2019, p. 1–6.
[30] Dall’Anese, E., Dhople, S.V., Johnson, B.B., Giannakis, G.B.. Decen-
tralized optimal dispatch of photovoltaic inverters in residential distribu-
tion systems. IEEE Transactions on Energy Conversion 2014;29(4):957–
967.
[31] Su, X., Masoum, M.A., Wolfs, P.J.. Optimal PV inverter reactive power
control and real power curtailment to improve performance of unbalanced
four-wire LV distribution networks. IEEE Transactions on Sustainable
Energy 2014;5(3):967–977.
[32] Almasalma, H., Claeys, S., Deconinck, G.. Peer-to-peer-based inte-
grated grid voltage support function for smart photovoltaic inverters. Ap-
plied Energy 2019;239:1037 – 1048.
[33] Turitsyn, K., ˇSulc, P., Backhaus, S., Chertkov, M.. Options for control
of reactive power by distributed photovoltaic generators. In: Proceedings
of the IEEE; vol. 99. 2011, p. 1063–1073.
[34] IEEE Standard for Interconnection and Interoperability of Distributed En-
ergy Resources with Associated Electric Power Systems Interfaces. IEEE,
Std. IEEE 1547-2018.
[35] Australia and New Zealand Standard for Grid connection of energy sys-
tems via inverters. Standards Australia and Standards New Zealand, Std.
AS/NZS 4777.2:2015.
[36] VDE Application Rule for Generators connected to the low-voltage dis-
tribution network. Verband Deutscher Elektrotechniker, Std. VDE-AR-N
4105:2018-11.
[37] Ma, Y., Gebbran, D., Chapman, A.C., Verbiˇc, G.. A photovoltaic system
investment game for assessing network hosting capacity allocations. In:
The Eleventh ACM International Conference on Future Energy Systems
15


---

Page 16

---

(e-Energy’20). 2020, p. 1–9.
[38] Australia’s Clean Energy Council, . Clean Energy Council submission to
the AS/NZS 4777.2:2015 Proposed Changes. Tech. Rep.; 2020.
[39] Conejo, A.J., Ruiz, C.. Complementarity, not Optimization, is the Lan-
guage of Markets.
IEEE Open Access Journal of Power and Energy
2020;7:344–353.
[40] Riaz, S., Marzooghi, H., Verbiˇc, G., Chapman, A.C., Hill, D.J.. Generic
demand model considering the impact of prosumers for future grid sce-
nario analysis. IEEE Transactions on Smart Grid 2019;10(1):819–829.
doi:10.1109/TSG.2017.2752712.
[41] Zugno, M., Morales, J.M., Pinson, P., Madsen, H.. A bilevel model for
electricity retailers’ participation in a demand response market environ-
ment. Energy Economics 2013;36:182 – 197.
[42] Bienstock, D., Verma, A.. Strong NP-hardness of AC power ﬂows fea-
sibility. Operations Research Letters 2019;47(6):494–501.
[43] Papavasiliou,
A..
Analysis of distribution locational marginal prices.
IEEE Transactions on Smart Grid 2018;9(5):4872–4882.
[44] Hart, W.E., Watson, J.P., Woodruﬀ, D.L.. Pyomo: modeling and solving
mathematical programs in python. Mathematical Programming Compu-
tation 2011;3(3):219–260.
[45] W¨achter,
A., Biegler,
L.T.. On the implementation of a primal-dual
interior point ﬁlter line search algorithm for large-scale nonlinear pro-
gramming. Mathematical Programming 2006;106(1):25–57.
[46] Smith, J.. HSL archive: A collection of Fortran codes for large scale
scientiﬁc computation. URL: http://www.hsl.rl.ac.uk/.
[47] Ratnam, E.L., Weller, S.R., Kellett, C.M., Murray, A.T.. Residen-
tial load and rooftop PV generation: an Australian distribution network
dataset. International Journal of Sustainable Energy 2015;:1–20.
[48] Bonami, P., Biegler, L., Conn, A., Cornu´ejols, G., Grossmann, I.,
Laird, C., et al. An algorithmic framework for convex mixed integer
nonlinear programs. Discrete Optimization 2008;5(2):186–204.
[49] Gebbran, D., Chapman, A.C., Verbiˇc, G.. The Internet of Things as a
facilitator of smart building services. In: 2018 Australasian Universities
Power Engineering Conference (AUPEC). 2018, p. 1–6.
16
