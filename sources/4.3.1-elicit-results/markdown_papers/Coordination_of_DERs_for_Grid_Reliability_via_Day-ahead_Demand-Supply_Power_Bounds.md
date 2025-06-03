

---

Page 1

---

1
Coordination of DERs for Grid Reliability via
Day-ahead Demand-Supply Power Bounds
Thomas Navidi, Abbas El Gamal, Life Fellow, IEEE, and Ram Rajagopal, Member, IEEE
Abstract—A previous study has shown that coordinating DERs
to protect the distribution grid can significantly reduce the in-
frastructure upgrades needed to address future increases in DER
and electrification penetrations. Implementing such coordination
in the real world, however, is challenging due the temporal and
spatial uncertainties about the loads and renewable generation,
smart meter and network delays, incomplete information about
the grid, different consumer objectives and privacy constraints,
and scalability of the coordination scheme. This paper describes
a day-ahead 2-layer DER coordination scheme that addresses
these challenges. A global controller uses historical load data
to compute day-ahead hourly demand upper and lower bounds
for each consumer node. It then solves a largest volume axis-
aligned box optimization problem to determine corresponding
supply power bounds which if followed, ensures grid reliability.
A local controller at each consumer node then determines the
DER power injections which satisfy the consumer’s objectives
while obeying its supply bounds. Simulation results demonstrate,
for example, that this scheme can capture 62% of the reduction
in transformer violations achievable by the perfect-foresight
centralized controller used in the aforementioned previous study.
Index Terms—Distributed energy resources, DERMS, distribu-
tion grids.
I. INTRODUCTION
Coordination of the power injections from distributed en-
ergy resources (DER), such as EV chargers, battery storage
units, and flexible thermal loads, across a distribution net-
work can provide several benefits, including reducing peak
network load during extreme weather conditions, providing
grid services, and safeguarding grid infrastructure, such as
transformers and voltage regulators. Existing programs for
DER coordination, such as virtual power plants (VPPs) and
demand response, aim to provide grid services but do not
consider distribution grid reliability. In a recent study [1],
the authors showed that coordinating DERs for grid reliability
has the potential to significantly reduce the grid infrastructure
upgrades needed to support future increases in DER and
electrification penetrations, while also reducing peak network
load. The perfect foresight centralized controller used in [1]
to demonstrate these benefits, however, is not implementable
and it has remained unclear how much of these benefits can be
attained by practical coordination schemes which must operate
under challenging requirements, including: (i) temporal and
spatial uncertainties about the loads and renewable generation,
(ii) smart meter and communication delays that can be up to
several hours [2] as well as communication network delays,
(iii) incomplete information about the physical characteristics
T. Navidi and A. El Gamal are with the Department of Electrical Engineer-
ing at Stanford University. R. Rajagopal is with the Departments of Civil and
Environmental Engineering and Electrical Engineering at Stanford University.
of the network, (iv) different objectives and privacy constraints
of the consumers who own the DERs, and (v) scalability to
large numbers of consumers.
In this paper, we present a day-ahead DER coordination
scheme whose main objective is to minimize transformer and
voltage violations across the distribution network under the
aforementioned real-world constraints. We demonstrate that
this scheme can reap a significant fraction of the benefits
of the perfect foresight controller with a moderate increase
in consumer electricity cost. To address the above first two
requirements of an implementable scheme, we use the 2-layer
control architecture first reported in [3] which comprises a
global controller (GC) that could be operated by the DSO
or via an aggregator cooperating with the DSO, and local
controllers (LC) located at consumers’ sites. Communication
takes place only between the GC and the LCs and the GC
sends updates to the LCs once per a day. Each day, the GC
uses past power injection data obtained from the smart meters
to compute hourly power demand upper and lower bounds over
the following day for every consumer or group of consumers
in the network. The GC then computes corresponding hourly
power supply upper and lower bounds by solving a maximum
volume axis aligned box optimization problem [4] whose
objective is to maximize the volume of the box defined by the
supply bounds subject to power flow constraints and fairness
across consumers while staying within the given upper and
lower power demand bounds. This formulation guarantees that
any set of power injections that satisfies the supply bounds
does not violate the reliability constraints. The supply power
bounds for each consumer node is then sent to its LC to
determine the power injections over the span of the following
day by minimizing a combination of its own objective and de-
viation from the supply bounds subject to its DER constraints.
The scheme satisfies the third requirement above by using
a data-driven linear model of the network learned through
smart meter data. It further satisfies the fourth requirement
by not requiring knowledge of any consumer constraints,
objectives or DER data, such as SOC of storage, flexible
load, or EV charging rate. The scheme is scalable, satisfying
the last requirement for implementable coordination, since the
maximum volume axis aligned box problem is convex and the
constraint space is independent of the number of DERs in the
network.
This paper provides several significant enhancements and
improvements over our earlier conference paper [5]. While
in [5] the supply bounds were computed using a heuristic,
the new GC algorithm provides guarantees on grid reliability
when the bounds are satisfied and the linear power flow model
is accurate. This paper also considers flexible thermal load
as another controllable DER in addition to the EV charging
arXiv:2307.00188v1  [eess.SY]  1 Jul 2023


---

Page 2

---

2
and storage considered in [5] While [5] included very limited
simulation results, this paper provides extensive results for 11
3-phase distribution networks representing varying climates,
sizes, and mixtures of commercial and residential consumers
over a 3-decade horizon with recent projections of DER
penetrations from [6], [7], [8], [9]. We further benchmark the
performance of our scheme relative to the bookend local and
perfect foresight centralized controllers in [1].
In addition to [3], [5], there has been other DER co-
ordination schemes, sometimes referred to as management
systems (DERMS), that aim to protect the grid. For exam-
ple [10] describes a hierarchical control scheme in which a
centralized controller uses power flow to calculate distribution
grid locational marginal prices (DLMPs) for each DER. Each
local DER controller then attempts to minimize its assigned
DLMP. This scheme, however, assumes that the objective of
all consumers is to minimize the DLMP rather than allowing
each of them to define its own objective. The strategy in [11]
uses a centralized controller to determine Lipschitz constraints
that guarantee the safe operation of a local reinforcement
learning algorithm for voltage stability. Their control strategy,
however, is only applied to voltage stability and not to other
objectives such as transformer overloading or individual DER
objectives and is only applicable to a neural network based
local controller. In [12] the authors present a method to
calculate flexibility bounds at a single point in the distribution
grid based on voltage limits. They do not consider transformer
limits and do not fully explore the extension of their method
to calculating bounds for multiple points in the grid simulta-
neously. Finally, the authors in [13] determine bounds for each
node by solving a similar maximum volume box problem. In
contrast to the work presented in this paper, however, their
paper (i) only considers voltage constraints, (ii) the bounds
are determined based only on the network model with no
consideration of consumer loads (e.g., demand bounds), which
can lead to unfairly allocating too much flexibility to nodes
with smaller loads at the expense of nodes with larger loads,
(iii) does not include any local controllers, (iv) has very limited
simulation results, and (v) does not provide any performance
evaluation relative to other DER coordination schemes.
In the following section we introduce the grid and DER
models and the various assumptions we make in formulating
the bounds coordination problem. In Section III, we describe
the bounds scheme. In Section IV, we present the simulation
setup used in evaluating our scheme. Since this setup is the
same as that in [1], we provide only a brief summary and
refer the readers to that paper for more details. In Section V,
we compare the performance of our scheme to the local and
the perfect-foresight controllers used in [1] to bookend the
performance of any implementable DER coordination scheme.
II. MODELS AND ASSUMPTIONS
We consider control of distributed energy resources within
a 3-phase distribution network modeled by a graph with a
set of nodes [1 : N] and a set of edges (lines) L. Node
i = 1 corresponds to the substation which is connected to
the transmission system and supplies power to the rest of the
nodes. We denote the set of consumer nodes by C ⊂[1 : N],
where |C| = NC. The set of transformers in the network
is specified by a set of node pairs (i, j) ∈T , where and
|T | = NT. Each consumer node comprises a collection of
uncontrollable loads, solar PV, energy storage, EV chargers,
and flexible thermal loads located under a single secondary
transformer or a single smart meter. This collection can
represent one or several residential consumers or a larger
commercial building. We consider the steady state operation
of the network over time steps t ∈{1, 2, . . .} each of length
δ, which we assume to be 15min in our simulations. The total
complex net power consumption at each node i ∈[1 : N] in
the network in timestep t is denoted by si(t). The steady state
power flows in the network determine the voltage magnitude
vi(t) for each node i at time t.
In the following we provide the models and assumptions
on the loads and controllable DERs we assume throughout
the paper.
Uncontrollable load. This includes a stochastic uncontrollable
load, with constant power factor, and solar PV generation,
which is assumed to be real and independent of the power fac-
tor. The combined uncontrollable load at node i and timestep
t is denoted by pi(t).
Energy storage. We assume the battery storage k at node i
has maximum capacity (energy) Qmax
ik
At time t, the storage
unit at node i has a charging power rate of cik(t) ≥0,
discharging rate of dik(t) ≥0, and a state of charge (energy)
of Qik(t). We assume that each storage unit only charges
and discharges real power, and that storage charges and
discharges with efficiency 0 ≤γc
ik ≤1 and 0 ≤γd
ik ≤1,
respectively. Hence, the storage energy at time t is modeled by
Qik(t) = Qik(t−1)+γc
ikδ cik(t)−γd
ikδ dik(t). The maximum
charging and discharging energy rates are denoted by cmax
ik
and
dmax
ik
, respectively.
Electric vehicle charging. The model we use for EV charging
is similar to that for energy storage with maximum discharge
power dmax
ik
= 0 (we do not consider vehicle to grid in this
paper) and cik(t) is bounded above by the EV charger rated
power. Each EV k ∈Ei, where Ei is the set of EVs at node
i, is to be charged within non-overlapping time windows Wik
over the simulation time horizon. The end time of window
w ∈Wik is denoted by tend
w . An additional constraint on EV
charging comes from the requirement that it must be charged
to a desired level Qfinal
ikw by the end of each window, i.e.,
Qik(tend
w ) = Qfinal
ikw , w ∈Wik and k ∈Ei.
Flexible thermal load. These include loads for air condition-
ing, ventilation, electric space and water heating and cooking.
We denote the total thermal load (power consumption) at
node i and timestep t by ui(t) and its maximum over the
simulation horizon by umax
i
, and assume that it has a constant
power factor of 0.92. We further denote the fraction of flexible
thermal energy that can be shifted to another time within
the same day by ϕ, which depends on the network and
whether the node is commercial or residential. We express
the thermal energy at time step t ∈[1 : Td] as Qik(t) =
Qik(t −1) + δ cik(t), where Qik(0) = 0. In practice, the
thermal energy consumed by the flexible load is determined
by the consumers desired temperature band for each thermal


---

Page 3

---

3
load. As the appliance consumes energy, the temperature either
increases or decreases. To provide grid services, the controller
adjusts the thermal load energy consumption while keeping the
temperature within the band. Accurately relating the thermal
energy consumption to temperature can be very complex,
requiring detailed data about the appliances, thermal models
of the buildings, climate conditions, and consumer behavior.
Since this paper is focused on the bounds coordination scheme
and on comparing its performance to the bookend controllers
in [1] rather than on thermal load modeling, operation, and
consumer behavior, we will use the simplified temperature to
thermal load energy consumption model in Section III-B.
In summary, the dynamics for the battery storage, EV
charging, and flexible load can all be expressed as Qik(t) =
Qik(t −1) + γc
ikδ cik(t) −γd
ikδ dik(t), where dik(t) = 0 for
EV charging and γc
ik = 1 and dik(t) = 0 for flexible thermal
load with the additional constraints for each DER as described
above.
A. Linearized inverse power flow
To maintain reliable operation, the network operator needs
to manage both the voltage magnitudes at each node and the
complex power flowing through each transformer to keep them
within their respective safe ranges. The relationship between
the net load and the voltage at each node i ∈[1 : N] is
governed by the AC power flow equations and accompanying
constraints [14]. We denote the maximum rated apparent
power squared of transformer (i, j) by τ max
ij
, and the upper
and lower limits on The voltage magnitude vi at node i by
vmin
i
and vmax
i
. We say that a set of power injections si for
i ∈[1 : N] is feasible if it satisfies these transformer and
voltage limits.
In general, the power flow equations are non-convex which
can lead to computationally intractable optimization problems.
Under some conditions, this can be addressed through convex
relaxation; however, the commonly used SDP and SOCP re-
laxations do not provide a correct solution when the objective
function is a decreasing function of the real power injection as
is the case for the maximum volume box problem discussed
later in this paper [14]. This may be alleviated through the
use of sequential convexification and modifications to the
relaxation via the method described in [15]. However, this
method still requires knowledge of the physical parameters of
the network, which are often not available even to the DSO.
Moreover, since we are only interested in scheduling, as in
other settings such as day ahead markets, we use the following
linearized the power flow equations [16], [17]
v(t) = As(t) + a,
(1a)
τ(t) = (Fs(t) + f)2 + (Gs(t) + g)2,
(1b)
where the bold symbols refer to the vector versions of the
variables defined earlier, A, a, F, f, G, g are the linear model
coefficients learned from the data, and the square of a vector
refers to an element-wise square operation.
In addition to significantly reducing the computational com-
plexity of computing the supply bounds, this model can in
fact be more accurate than physics based approximations [16]
because the parameter values of such models, such power line
admittances, configurations and parameters of capacitor banks,
voltage regulators, and switches, are often not completely
known to the GC whose function is to characterize the set of
feasible power injections via the supply bounds. In contrast,
the power and voltage measurement data needed to train
the above model are readily available through existing smart
metering infrastructure. Furthermore, this data driven model
can readily adapt to changes in the states of the network assets,
such as voltage regulators and switches, without needing to
know the specifics of such changes.
B. Reactive power modeling
Since the voltages, hence, the feasible set of real power
injections, depend on the reactive power injections, to establish
the real power injection supply bounds we need to know the
relationship between the reactive power at each consumer node
and its real power. Since the GC does not have information
about the composition of the load at each node, we estimate
this relationship using the historical net load data from the
smart meters and the transformer monitoring equipment. Since
the supply bounds need to guarantee that the complex power
is within a certain feasible region, we use this relationship to
establish an upper and lower percentile estimate of the reactive
power as a function of the real power. The specific percentile
can be adjusted to tune how conservative of an estimate to
use for the range of possible reactive power injections. In
this study, we use a linear least squares estimator trained
on the 90th percentile of reactive power injections for the
upper bound and the 10th percentile for the lower bound. The
resulting upper and lower bounds on the reactive power (as a
function of the real power) are
qu(t) = Hu(t)pu(t) + hu(t),
(2a)
ql(t) = Hl(t)pl(t) + hl(t),
(2b)
where qu(t) and ql(t) are the upper and lower bounds on
reactive power, and Hu, hu, Hl, hl are the linear model coef-
ficients. The model coefficients are a function of t since there
are different coefficients for each hour in the day.
III. DAY-AHEAD DER COORDINATION SCHEME
A block diagram of the day ahead 2-layer DER coordination
scheme is given Figure 1. In the following subsections we
describe the GC and the LC in detail.
A. Global controller
The AC power flow equations provide a mapping from the
nodes real and reactive power injections to their voltages,
hence the set of feasible node voltages, i.e., voltages within
tolerable limits, can be represented by a set of feasible power
injections. Similarly, the transformer constraints represent an-
other set of feasible power injections. The intersection of these
two sets represents the feasible set of power injections in
the network, that is, the power injections that can be reliably
supported by the distribution network. Since each consumer’s
LC has access only to its own power injections and does


---

Page 4

---

4
...
  Learn linearized power flow models
  Learn reactive power models
Solve problem (7) for hourly supply
bounds
Node i DER states
and objectives
net load
  Solve problem (11) each
  time step for DER power
  injections
pui, pli
Historical load data
  Hourly demand bounds
Global Controller
    Node i DER power 
    injection profiles
Local Controller i
...
Fig. 1: Block diagram of the day ahead two-layer coordination
scheme. Input data are described in the parallelograms and
operations in the rectangles.
not have any information about the power injections at other
nodes, the LCs cannot jointly operate at any arbitrary point in
this feasible set of power injections. Hence in our scheme, the
GC provides each LC with day-ahead hourly “supply” upper
and lower bounds denoted by the 24-dimensional vectors pl
i
and pu
i on its net power injections for each node i ∈C such
that if every LC operates within its given supply bounds, the
resulting set of power injections in the network is feasible.
Such bounds define a “supply box” in the NC-dimensional
space of consumer node power injections for each hour of the
next day.
Determining the supply bounds by finding the axis-aligned
supply box with the maximum volume that fits within the set
of feasible power injections, however, can lead to situations in
which consumers in favorable locations in the network receive
significantly more power injection flexibility relative to their
actual demands, resulting in much higher inevitable supply
bound violations at other nodes. To address this problem,
node demands must be taken into consideration in finding the
supply bounds. This is achieved by first finding upper and
lower hourly “demand” bounds pld
i , pud
i
on the net power
injections for each node i ∈C and for each hour of the
next day as follows. To find the hourly demand bounds for
a consumer node, the GC uses the node’s historical load data
corresponding to the next day, for example, if the next day is
a weekday, the load data would be from the past weekdays in
the past 5 weeks, similarly for weekends. The GC then sets
the lower demand bound for each hour to be the lowest of
either 0 or the power injection value of the selected historical
data for that hour, and the upper demand bound for each hour
is the highest of either 1kW or the power injection value of
the selected historical data for that hour. The derived demand
bounds define a demand box in the NC-dimensional space of
consumer node power injections for each hour of the following
day; see Figure 2.
Demand bound box
Supply bound box
Feasible power 
injection region
{𝑝!
"}
{𝑝!
#}
{𝑝!
"$}
{𝑝!
#$}
Fig. 2: Illustration of the maximum volume axis aligned box
problem.
From the above discussion, to ensure maximum flexibility
the GC aims to find the largest volume axis-aligned supply box
(defined by the supply bounds) which is in the intersection of
the axis-aligned demand box and the set of feasible power in-
jections. Further to prevent unfairly allocating more flexibility
to nodes with lower demands at the expense of other nodes,
we normalize the difference between the supply and demand
bounds for each node by the difference between the upper and
lower demand bounds for that node (for each hour) as follows
∆u
i = pud
i
−pu
i
pud
i
−pld
i
, ∆l
i = pl
i −pld
i
pud
i
−pld
i
, i ∈C,
(3)
where 0 ≤∆u
i , ∆l
i < 1 and ∆u
i +∆l
i < 1. The reason this nor-
malization ensures fairness in flexibility across all consumer
nodes is that the maximum box volume solution tries to make
the supply box as close as possible to a hypercube within
the demand box, such that shorter demand box dimensions
have their corresponding supply box side lengths prioritized
over the longer dimensions. This leads to the following supply
bounds optimization problem formulation for each hour of the
following day (we do not introduce an index for hour).
maximize:
X
i∈C
log(1 −∆u
i −∆l
i)
(4a)
subject to: ∆u
i ≥0, ∆l
i ≥0, ∆u
i + ∆l
i < 1, i ∈C
(4b)
pu
i = pud
i
−(pud
i
−pld
i )∆u
i ,
pl
i = pld
i + (pud
i
−pld
i )∆l
i, i ∈C
(4c)
qu = Hupu + hu, ql = Hlpl + hl,
(4d)
v = As + a, s ∈[sl, su]
(4e)
vmin
i
≤vi ≤vmax
i
, i ∈[1 : N]
(4f)
τ = (Fs + f)2 + (Gs + g)2, s ∈[sl, su] (4g)
τij ≤τ max
ij
, (i, j) ∈T .
(4h)


---

Page 5

---

5
The objective function (4a) is the sum of the log of the
normalized width for each node’s supply bounds. Maximizing
this objective is equivalent to maximizing the normalized
volume of the axis aligned supply box. The constraints (4b)-
(4c) define the relationship between the demand and the supply
bounds. The constraints (4d) are the mappings from real power
supply bounds to the reactive power injection bounds for each
node. The constraints (4e)-(4h) are the data-driven mappings
of real and reactive power to the voltage magnitude and
limits at each node and the apparent power and limits at each
transformer, respectively.
Solving this problem requires ensuring that every com-
plex power injection s ∈

sl, su
satisfies the voltage and
transformer constraints, hence the problem appears intractable.
However, since both the set of power injections arising from
the voltage constraints and from power injections correspond-
ing to the transformer constraints are convex, their intersection
with the demand box is also convex. Thus, we can take
advantage of the convexity to simplify the problem as in [18]
and its expanded version in [4] in which the constraints reduce
to those needed to define the convex feasible set. To do so,
we split the power flow mapping matrices and coefficients
into positive and negative components A+, A−, a+ and a−
such that A+ + A−= A, a+ + a−= a, and similarly
for F+, F−f +, f −and G+, G−, g+, g−. The transformer
mapping will be referred to as B+, B−, b+, b−to simplify the
notation. Then we can verify that every power injection within
the supply bounds satisfies the constraints by only checking
the upper and lower vertices of the box as follows
vu = A+su + a+ + A−sl + a−
(5a)
vl = A+sl + a+ + A−su + a−
(5b)
vmin
i
≤vu
i ≤vmax
i
, vmin
i
≤vl
i ≤vmax
i
, i ∈[1 : N]
(5c)
τ u = B+su + b+ + B−sl + b−
(5d)
τ l = B+sl + b+ + B−su + b−
(5e)
τ u
ij ≤τ max
ij
, τ l
ij ≤τ max
ij
, (i, j) ∈T .
(5f)
Replacing the constraints (4e)-(4h) with the above con-
straints, yields a computationally efficient and scalable op-
timization problem which the GC solves for each hour of
the next day. The resulting supply upper and lower bounds
for each consumer node are then sent to its local controller.
As long as each local controller is able to restrict the power
injections to within its supply bounds, the network constraints
are satisfied provided the linear mappings from the power
injection to node voltages and transformer powers are accurate.
Relationship to maximum loadability. The maximum vol-
ume axis aligned box problem is related to the problem of find-
ing the maximum loadability of a transmission system [15],
[19] for voltage stability analysis. The maximum loadability
problem aims to maximize the power injection at a single
node in the transmission grid constrained by the power flow
equations and voltage limits. Key differences between this
previous work and our box problem are: (i) we find both
a maximum and minimum range of power injections for all
nodes in the network rather than a single injection for all the
nodes, (ii) we consider the variability of load over time to
limit the power injection of nodes in the distribution network
depending on their demands ahead of time, and (iii) we include
transformer power limits in the constraint set.
B. Local controller
The local controller determines the power injections for
the stationary storage, EV chargers, and flexible thermal
load within each consumer’s node. It aims to satisfy the
consumer’s objectives and preferences, such as minimizing the
total electricity cost, charging EVs on time, and maintaining
comfortable climate while minimizing the deviation of the
net power injection from its supply bounds. Why would
consumers consider the supply bounds at the expense of less
flexibility in satisfying their objectives, however?
To address this key question, we propose incentivizing
consumers via a tiered rate plan similar to ones currently
offered by some utilities such as PG&E [20]. Under our
proposed incentive, consumers would pay a reduced Time of
Use (TOU) rate when their net power injection is within the
supply bounds and regular TOU rate when they violate the
bounds. The exact discounted rate, however, only needs to
be sufficient for consumers to prioritize following the bounds
over other cost saving strategies, such as energy arbitrage.
Although our scheme allows for consumers to have different
objectives, to evaluate the performance of the scheme, in
Section V we assume that all local controllers have the same
objectives. In particular, to determine the power injections
for the DERs at each node, the local controller solves the
following optimization problem for every time step t, i.e.,
every δ = 15 minutes of each day.
minimize: λbLb
i(t) +
Ki
X
k=1
λikLf
ik(t)
(6a)
subject to: 0 ≤ci(t) ≤cmax
i
(t), 0 ≤di(t) ≤dmax
i
(t) (6b)
Qmin
i
(t) ≤Qi(t) ≤Qmax
i
(t)
(6c)
Qik(t) = Qik(t −1) + γc
ikδcik(t)
−γd
ikδdik(t), k ∈[1 : Ki]
(6d)
Qik(tend
w ) = Qfinal
ikw , w ∈Wik, k ∈Ei.
(6e)
The first term in the above objective function corresponds to
the deviation from the supply bounds:
Lb
i(t) =
h
pi(t) +
Ki
X
k=1
(cik(t) −dik(t)) −pu
i (t) −ϵu
i (t)
i
+
+
h
pl
i(t) + ϵl
i(t) −pi(t) −
Ki
X
k=1
(cik(t) + dik(t))
i
+,
(7)
where pu
i (t) and pl
i(t) are the supply bounds during the hour in
which t lies, ϵu
i (t) and ϵl
i(t) are the sum of the past deviations
of the net power injection from the upper and lower bounds
during the hour, respectively, which allows the controller to
ensure that the average power across the hour can satisfy the
bounds. The second term in the objective function for each
DER k is
Lf
ik(t) = |Qik(t) −Qtarget
ik
(t)|,
(8)


---

Page 6

---

6
where Qtarget
ik
(t) is the desired state of DER k at time t, which
depends on the specific objective of the consumer. We assume
that the objective is to minimize the cost of electricity based on
the given or reduced time-of-use (TOU) rate. Thus, the desired
state for each DER is Qtarget
ik
(t) = Qmax
ik
(t) for t in the 12
hour period before the start of the peak price period (from
early morning to late afternoon), and Qtarget
ik
(t) = Qmin
ik (t) for
t during the peak price period (between late afternoon to late
evening). In all other times t (night time) in which the TOU
rate is lowest and there is no solar generation, the objective
Lf
ik(t) = 0.
To determine the limits on the thermal load energy con-
sumption profiles Qmin
ik (t) and Qmax
ik
(t) that correspond to the
ends of the desired temperature band, we use the following
simple model. We assume that the given baseline thermal load
energy consumption profile Qbase
ik
(t) (see Section IV for how
it is determined for the simulations) corresponds to the mid
point of the desired temperature band and express the limits
on the thermal load energy as
Qmax
ik
(t) = min

Qbase
ik
(t) + ϕ Qbase
ik
(Td), Qbase
ik
(Td)
	
,
Qmin
ik (t) = max

0, Qbase
ik
(t) −ϕ Qbase
ik
(Td),
Qbase
ik
(Td) −(Td −t) δ umax
i
	
.
These limits ensure that the total shifted energy consumption
does not exceed a fraction ϕ of the total thermal energy
consumption during the day and is equal to the baseline
consumption by the end of the day.
IV. SIMULATION SETUP
We simulate and evaluate our DER coordination scheme
using the same methodology, data and assumptions detailed
in [1]. To make the presentation of our results somewhat self-
contained, in the following we provide a summary of the
simulation setup and the DER bookend controllers.
We use the power flow-optimization system in [1] in which
the input data includes the linearized network models, load
profiles, DER operating parameters, DER penetrations, and
prescribed electricity tariffs. Using this data, a network sce-
nario is generated by randomly choosing the EV charging
windows and assigning rooftop PV, stationary storage, and
flexible loads to the consumer nodes in the network. The
operation of the chosen DER control scheme is then simulated
to determine the DER power injection profiles for all DERs,
which allows us to run quasi-static power flow simulation
using OpenDSS [21] to determine the voltage at each node
and apparent power flow through each transformer. This in-
formation is then used to compute the transformer and voltage
reliability metrics and determine the cost of electricity for
each node. This process is repeated for several scenarios and
reliability statistics are computed.
As in [22], [1], the metric we use for steady-state voltage
declares a violation at a node if its voltage magnitude exceeds
the specifications in the ANSI C84.1 standard, which represent
a deviation of ±5% from the nominal voltage magnitude on
average across any 1-hour window. The metric for transformer
thermal overloading declares a violation at a transformer if
its average apparent power is greater than 120% of its rated
capacity over one or more 2-hour windows.
Table I summarizes the main characteristics of the eleven 3-
phase distribution networks we used to evaluate our scheme.
The columns are the assigned name indicating location and
source of network data, type of network data, the number of
nodes, transformers, and consumer nodes for each network.
The asterisk by the network name indicates a network that
aggregates consumers under the secondary transformer. The
networks without asterisk have models for individual con-
sumers under each secondary transformer.
TABLE I: Main characteristics of the networks used in the
simulations.
Name
Type
N
NT
NC
Sacramento* [23]
Synthetic
278
99
91
Iowa* [24]
Real
915
268
193
Central SF [25]
Synthetic
2115
232
425
Commercial SF [25]
Synthetic
172
17
18
Tracy [25]
Synthetic
775
108
161
Rural San Benito [25]
Synthetic
243
15
22
Los Banos [25]
Synthetic
2010
251
426
Vermont [26]
Real
4245
828
1384
Arizona* [23]
Real
138
46
38
Marin [25]
Synthetic
3689
231
811
Oakland [25]
Synthetic
10073
658
2426
To construct the load profiles, we first use the 2018 resi-
dential and commercial consumer load profiles dataset in [27]
to construct 1-year baseline profiles for each node in each
network based on its geographical census code. We then scale
these profiles for each node so that its average daily peak load
matches that of the network. The reactive power component
of the load for each node is chosen such that the power factor
is randomly distributed between 0.9 and 0.95 as is commonly
assumed, e.g., see [24].
To determine the electrification increases, we use the pro-
jections up to 2050 in [6], which is categorized by space
heating, water heating, and other loads. We uniformly scale
the electrification due to loads other than thermal by their
electrification projection percentage. We then randomly choose
a consumer that does not already have electric space heating
or water heating, and assign to it a load profile of either
space or water heating that is converted from the thermal
energy in [27] to electric energy using the median published
efficiency for the corresponding electric appliance in [28]. This
process is repeated until the total added electric energy in a
network equals its electrification projection. The sum of air
conditioning, space heating, and water heating load profiles at
each node represents its baseline thermal load profile referred
to in Section III-B. We declare a percentage of the thermal load
profile as flexible load using the projections in [29], which
specifically considers electric furnaces, air conditioners, and
water heaters.
EV penetration is defined as the EV charging energy as a
percentage of the total energy in the network with no solar
included, and assuming penetrations from the high electrifica-
tion projections in [6]. We assume the Workplace and home


---

Page 7

---

7
L2 EV chargers to have a rated charging power of 6.3kW [7]
and that charging power can be varied between any value less
than this rated power. To determine the EV charging windows,
we use the synthetic data generator in [30] to produce sample
charging schedules each consisting of a starting time, ending
time, charging energy demand, and whether charging is done
at home or at work over the 1-year simulation horizon. We
continue to add new EVs to the network at random until the
total energy consumed by EVs as determined by the data
generator is equal to the total projected EV electrification
penetration energy.
PV penetration is defined as the energy generated by solar
PV as a percentage of the total energy consumed by the
network, including for EV charging. We set the PV penetration
in 2050 for each network to 23% of the total potential rooftop
solar PV generation of its nearest city [8], which corresponds
to approximately the same amount of solar PV capacity as
the high penetration scenario for nationwide distributed PV
projected in [9]. To determine the PV penetration for the years
prior to 2050, we scale the penetrations in proportion to the
nationwide PV capacity provided in [9]. The PV generation
profiles for each network are obtained from the solar data
of the closest geographic region to the network provided
in [31]. Nodes are assigned a PV generation profile at random
until reaching the PV penetration. The profile is scaled such
that the ratio of solar PV energy generation to the total
energy consumed by the node is randomly distributed between
40 −90%, which roughly corresponds to the upper quartile
estimate of residential PV system sizes given in [9].
We assume that only nodes with solar PV can have sta-
tionary storage and define storage penetration as a percentage
of the nodes with PV. The storage penetrations we assume
correspond to the highest adoption rates given in [9], which
range between 30% and 70% depending on the year. Each
storage unit is randomly assigned a capacity which is between
40 −80% of the average daily PV energy generation, which
corresponds to the upper quartile estimate of residential battery
system sizes in [9], a maximum c-rate of 0.5 [9] and a round-
trip efficiency of 0.86 [32].
The TOU tariffs [33] used in the simulations include
peak, part-peak, and off peak rates for both residential and
commercial consumers. The hours during which these rates
apply are chosen such that the middle of the peak price hour
corresponds to the most frequent total network peak demand
hour. In addition, EV TOU rates [34] are included (see [1]
for details). We assume that the reduced rate used when the
consumers obey their respective supply bounds is 80% of the
regular TOU rates.
Bookend controllers.
To evaluate our bounds scheme, we compare its perfor-
mance in terms of transformer and voltage violations to two
bookend control schemes. The first is a centralized perfect
foresight controller that has perfect knowledge of all future
loads and DER states 2-days in advance and has full control
over all DERs. This centralized controller determines the
power injections for all DERs by minimizing a weighted
sum of the electricity cost, voltage violations and transformer
overloading metrics, and storage operation cost with the grid
reliability objectives having the highest weight. The constraints
are the linearized inverse power flow mapping and the storage,
EV charging, and flexible load dynamics.
The second bookend control scheme is a local controller that
runs fully autonomously at each node and operates its DERs
with the goal of minimizing the consumer’s total electricity
cost. It is a simple heuristic that does not presume knowledge
or forecasts of any variable values, except for the end of the
current EV charging window and the percentage of thermal
load that is flexible, which may be specified by the consumer.
At each time step, the controller checks its electricity tariff
to find the lowest cost time period and reserves operation to
within those time periods as much as possible.
Software implementation. All data used in the simulations
are publicly available and referenced in this paper and in [1].
The code for the simulations will be available on Github after
publication of this paper.
V. SIMULATION RESULTS
We simulated our DER coordination scheme using the setup
outlined in the previous section for the years 2020 to 2050
using the same scenarios as in [1] to provide a fair comparison
of our scheme to the two bookend controllers.
Figure 3 plots the means and standard errors across the 11
networks for the transformer overloading and voltage violation
metrics between 2020 and 2050 using our bounds scheme as
well as the means with the bookend controllers. Note that
from 2020 to 2030, the transformer overloading and voltage
violations steadily increase for all three control schemes. From
2035 to 2045, the bounds scheme and centralized controller
see a slower increase in violations as the amount of flexi-
bility and stationary storage begin to offset the downsides
of increased electrification. Finally, after 2045, the amount
of load flexibility becomes high enough to actually decrease
the violations for both the bounds scheme and the centralized
controller. In 2050, the means of the transformer and voltage
violations for the bounds scheme are 49% and 20%, respec-
tively, compared to 29% and 18% for the centralized controller
and 81% and 28% for the local controller. Hence the bounds
scheme captures 62% and 75% of the violation reductions of
the centralized controller versus the local controller.
Figure 4 shows the means and standard errors of the
violation percentages for each individual network averaged
across all 16 scenarios in 2050. The bounds scheme is able
to reduce the number of overloaded transformers significantly
across all networks with the exception of the commercial SF
network, which has much less flexible load due to having only
commercial consumers as opposed to primarily residential
consumers as for all other networks. Note that all networks ex-
hibit noticeable reduction in voltage violations with the bounds
scheme. However, there are significant variations across net-
works because some are naturally more prone to voltage
violations than others due to their specific configuration of
power lines and consumers.
As pointed out in [1], DER coordination provides benefits
to reliability beyond reducing the transformer and voltage
violations according to the binary-valued metrics. Figure 5


---

Page 8

---

8
0
5
10
15
20
25
30
2020
2025
2030
2035
2040
2045
2050
nodes with voltage violations (%)
bounds
centralized
local
0
10
20
30
40
50
60
70
80
90
2020
2025
2030
2035
2040
2045
2050
overloaded transformers (%)
Fig. 3: Aggregated means and standard errors of the violation
percentages with the bounds scheme compared to the means
of the bookend control schemes for each simulation year.
plots the empirical probability that the percentage magnitude
of transformer apparent powers across all networks and sce-
narios in 2050 being greater than value on the x-axis. Note that
shifting the distribution of the magnitudes of all transformer
apparent powers towards the y-axis represents less violations.
The bounds controller has an average magnitude of 192% for
transformer overloading events as opposed to 243% to 159%
for the fully local and fully centralized controllers. The results
for voltage violations are similar with the bounds controller
having an average magnitude of 5.47% as opposed to 5.93%
to 5.32% for the local and centralized controllers.
A. Impact on peak load
In addition to reducing the number of transformers that
experience overloading and nodes with voltage violations,
the bounds scheme reduces the peak network load over the
simulation horizon relative to the local controller. As shown
in Figure 6, the peak load with the bounds scheme is reduced
by 12% on average in 2050 compared to the bookend local
controller versus an 18% decrease from the centralized control
scheme.
0
10
20
30
40
50
60
70
tracy
vermont
arizona
central SF
commercial SF
oakland
los banos
marin
rural san benito
sacramento
iowa
nodes with voltage violations (%)
local
bounds
centralized
0
10
20
30
40
50
60
70
80
90
overloaded transformers (%)
Fig. 4: Means and standard errors of the violation percentages
for individual networks in 2050.
Fig. 5: The empirical probability of the percentage magnitude
of transformer apparent powers being greater than value on
the x-axis across all networks and scenarios in 2050.


---

Page 9

---

9
75
80
85
90
95
100
2020
2025
2030
2035
2040
2045
2050
Peak load with bounds control (% of LC)
bounds
centralized
Fig. 6: Plot of the means and standard errors of the peak load
over the simulation horizon as a percentage of the bookend
local controller peak load.
B. Impact on electricity cost
In [1], we showed the centralized controller increases elec-
tricity cost by 5.1% in 2050 over the local controller, which
focuses only on minimizing electricity cost. With the bounds
controller, we find that when calculating the cost with no
incentive to follow the bounds, the increase is between 9.8%
and 11.1% relative to the local controller. When factoring in
the 80% incentive we assumed in our simulations, the cost of
electricity is reduced to between 93.4% and 95.0% of the cost
under the local bookend controller.
C. Impact of load flexibility
The projections of load flexibility from [29] include a
base case and an enhanced case with the enhanced one,
which we assumed in the above results, projecting significantly
more load flexibility. In order to determine the impact of the
amount of load flexibility on the performance of the bounds
scheme, Figure 7 shows the mean and standard errors of
the percentage of overloaded transformers averaged across all
networks and scenarios in 2050 with the three control schemes
for the base and enhanced flexibility cases. The means of the
percentage of overloaded transformers for the bounds scheme
and the base load flexibility are 69% and 25%, respectively,
compared to 49% and 20% with enhanced load flexibility.
Thus, load flexibility represents a significant contribution to
the performance of the bounds scheme.
VI. CONCLUSION
We presented a DER coordination scheme which aims to
protect distribution grids with high penetrations of DER and
electrification. We demonstrated that this scheme can capture
a significant fraction of the reliability benefits of a perfect
foresight centralized controller relative to current autonomous
DER control [1]. Another important benefit of our scheme
relative to autonomous DER control is that it reduces peak
network power even though this objective is not explicitly
20
30
40
50
60
70
80
90
base
enhanced
overloaded transformers (%)
bounds
bounds
centralized
Fig. 7: Means and standard errors of the percentge of over-
loaded transformers across all networks in 2050 with base and
enhanced load flexibility.
included in the bounds problem formulation. We showed our
scheme addresses all the requirements of an implementable
DER coordination.
Our bounds scheme can be readily deployed using existing
computing and communication infrastructure and does not
require the development or deployment of any new hardware
(the GC and LC operations can both be handled using existing
cloud infrastructure and DER embedded controllers) or grid
infrastructure, making it very cost effective especially when
considering the significant savings it provides to grid infras-
tructure upgrades. Deploying our scheme, however, requires
the involvement of distribution grid operators (DSO) not
only to provide the necessary information about the grid,
e.g., the linearized grid models used in this paper, but also
to ensure broad consumer adoption of the scheme through
various incentives, such as our proposed reduced TOU rate.
Our scheme can also operate seamlessly with existing demand
response and virtual power plants (VPP) programs which aim
to reduce electricity cost during extreme climate conditions.
In such cases, the LCs would adjust their control objectives
to satisfy the requests for grid services from the DSO, DER
vendors or third party DER aggregators while still aiming to
keep power injections within the supply bounds.
To evaluate the bounds scheme, we assumed that the de-
mand bounds are determined by the GC using historical smart
meter data. Other ways to determine these bounds include
incentivizing consumers to submit their own demand bound
forecasts. Having more accurate demand bounds would allow
the GC to better allocate supply bounds to other nodes who
may need the additional capacity. We also assumed that all
LCs use the same control objective. The scheme, however,
allows consumers to have different objectives provided they
include staying within the given supply bounds.
The 80% of TOU incentive assumed in this paper is only
meant to illustrate the potential for our scheme to provide
savings to both the consumers who use their DER flexibility


---

Page 10

---

10
for grid reliability and the DSO who saves on distribution asset
upgrade costs. The exact values of the incentive will have to
be calculated on an individual network basis by considering
the cost savings of deferring transformer and voltage upgrades
and differences in cost of electricity over time. These costs
can vary widely depending on the DSO network equipment,
location, and electricity generation portfolio.
ACKNOWLEDGMENT
The authors would like to thank Anthony Degleris for
bringing to their attention the maximum volume axis aligned
box problem in [18]. The work presented in this paper was
supported under ARPA-E award DE-AR0000697 and US DOE
award DE-OE0000919.
REFERENCES
[1] T. Navidi, A. E. Gamal, and R. Rajagopal, “Coordinating distributed
energy
resources
for
reliability
can
significantly
reduce
future
distribution grid upgrades and peak load,” 2023. [Online]. Available:
https://doi.org/10.48550/arXiv.2306.08717
[2] “Smart meters and smart meter systems: A metering industry. eei-aeic-
utc. a joint project of the eei and aeic meter committees perspective.
march 2011.”
[3] K. Anderson, R. Rajagopal, and A. El Gamal, “Coordination of dis-
tributed storage under temporal and spatial data asymmetry,” IEEE
Trans. on Smart Grid, vol. PP, no. 99, 2017.
[4] M. Behroozi, “Largest inscribed rectangles in geometric convex sets,”
2022. [Online]. Available: https://doi.org/10.48550/arXiv.1905.13246
[5] T. Navidi, C. Leblanc, A. El Gamal, and R. Rajagopal, “Der information
unaware coordination via day-ahead dynamic power bounds,” IEEE
International Conference on Communications, Control, and Computing
Technologies for Smart Grids (SmartGridComm), pp. 1–6, 2020.
[6] M. Trieu, P. Jadun, J. Logan, C. McMillan, M. Muratori, D. Steinberg,
L. Vimmerstedt, R. Jones, B. Haley, and B. Nelson, “Electrification
futures study: Scenarios of electric technology adoption and power
consumption for the united states,” NREL, Golden, CO, USA,
Tech. Rep. NREL/TP-6A20-71500, 2018. [Online]. Available: https:
//www.nrel.gov/docs/fy18osti/71500.pdf
[7] M. Muratori, C. L. Rames, S. Srinivasa Raghavan, M. W. Melaina, and
E. W. Wood, “National plug-in electric vehicle infrastructure analysis,”
2 2018. [Online]. Available: https://www.osti.gov/biblio/1420371
[8] P. Gagnon, R. Margolis, J. Melius, C. Phillips, and R. Elmore, “Rooftop
solar photovoltaic technical potential in the united states: A detailed
assessment,” NREL, Golden, CO, USA, Tech. Rep. NREL/TP-6A20-
65298, 2016. [Online]. Available: https://www.nrel.gov/docs/fy16osti/
65298.pdf
[9] A. Prasanna, K. McCabe, B. Sigrin, and N. Blair, “Storage futures study:
Distributed solar and storage outlook: Methodology and scenarios.”
NREL, Golden, CO, USA, Tech. Rep. NREL/TP-7A40-79790, 2021.
[Online]. Available: https://www.nrel.gov/docs/fy21osti/79790.pdf
[10] P. Andrianesis and M. Caramanis, “Distribution network marginal costs:
Enhanced ac opf including transformer degradation,” IEEE Transactions
on Smart Grid, vol. 11, no. 5, pp. 3910–3920, 2020.
[11] W. Cui, J. Li, and B. Zhang, “Decentralized safe reinforcement
learning for inverter-based voltage control,” Electric Power Systems
Research, vol. 211, p. 108609, 2022. [Online]. Available: https:
//www.sciencedirect.com/science/article/pii/S037877962200685X
[12] M. Bolfek and T. Capuder, “A practical approach to flexibility provision
assessment in an unobservable distribution network,” Electric Power
Systems Research, vol. 212, p. 108262, 2022. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S0378779622004631
[13] J. Comden, A. S. Zamzam, and A. Bernstein, “Secure control regions
for distributed stochastic systems with application to distributed energy
resource dispatch,” in 2022 American Control Conference (ACC), 2022,
pp. 2208–2213.
[14] L. Gan, N. Li, U. Topcu, and S. H. Low, “Exact convex relaxation of
optimal power flow in radial networks,” IEEE Transactions on Automatic
Control, vol. 60, no. 1, pp. 72–87, 2015.
[15] W. Wei, J. Wang, N. Li, and S. Mei, “Optimal power flow of radial
networks and its variations: A sequential convex optimization approach,”
IEEE Transactions on Smart Grid, vol. 8, no. 6, pp. 2974–2987, 2017.
[16] Y. Liu, N. Zhang, Y. Wang, J. Yang, and C. Kang, “Data-driven power
flow linearization: A regression approach,” IEEE Transactions on Smart
Grid, vol. 10, pp. 2569–2580, 2019.
[17] J. Yu, Y. Weng, and R. Rajagopal. (2017) Mapping rule estimation
for power flow analysis in distribution grids. [Online]. Available:
https://arxiv.org/pdf/1702.07948.pdf
[18] S. Boyd and L. Vandenberghe, Convex Optimization.
Cambridge
University Press, 2004.
[19] I. Dobson, T. Van Cutsem, C. Vournas, C. Demarco, M. Venkatasub-
ramanian, T. Overbye, and C. Canizares, “Voltage stability assessment:
Concepts, practices and tools,” IEEE Power Engineering Society, Power
System Stability Subcommittee Special Publication, vol. 11, pp. 21–22,
01 2002.
[20] “Tiered
Rate
Plan
(E-1).”
[Online].
Available:
https://www.pge.com/en US/residential/rate-plans/rate-plan-options/
tiered-base-plan/tiered-base-plan.page
[21] D. Montenegro, M. Hernandez, and G. Ramos, “Real time opendss
framework for distribution systems simulation and analysis,” Sixth
IEEE/PES Transmission and Distribution: Latin America Conference
and Exposition (T&D-LA), pp. 1–5, 2012.
[22] A. K. Jain, K. Horowitz, F. Ding, N. Gensollen, B. Mather, and
B. Palmintier, “Quasi-static time-series pv hosting capacity methodology
and metrics,” 2019 IEEE Power & Energy Society Innovative Smart Grid
Technologies Conference (ISGT), pp. 1–5, 2019.
[23] K. P. Schneider et al., “Analytic considerations and design basis for
the ieee distribution test feeders,” IEEE Transactions on Power Systems,
vol. PP, no. 99, pp. 1–1, 2017.
[24] F. Bu, Y. Yuan, Z. Wang, K. Dehghanpour, and A. Kimber, “A time-
series distribution test system based on real utility data,” 2019 North
American Power Symposium (NAPS), pp. 1–6, 2019.
[25] B.
Palmintier,
T.
Elgindy,
C.
Mateo,
F.
Postigo,
T.
G´omez,
F. de Cuadra, and P. D. Martinez, “Experiences developing large-
scale synthetic u.s.-style distribution test systems,” Electric Power
Systems Research, vol. 190, p. 106665, 2021. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S0378779620304685
[26] “Electric
power
research
institute
(epri)
feeder
j1,”
2022.
[Online].
Available:
https://sourceforge.net/p/electricdss/code/HEAD/
tree/trunk/Distrib/EPRITestCircuits/epri dpv/J1
[27] E. J. H. Wilson, A. Parker, A. Fontanini, E. Present, J. L. Reyna, and et.
al, “End-use load profiles for the u.s. building stock: Methodology and
results of model calibration, validation, and uncertainty quantification,”
3 2022. [Online]. Available: https://www.osti.gov/biblio/1854582
[28] CEC, “Modernized appliance efficiency database system (maedbs),”
https://cacertappliances.energy.ca.gov/Pages/ApplianceSearch.aspx,
ac-
cessed: 2023.
[29] P. Jadun, T. Mai, C. Murphy, Y. Sun, M. Muratori, B. Nelson, R. Jones,
and J. Logan, “Electrification futures study flexible load profiles,”
National Renewable Energy Laboratory, Golden, CO, Tech. Rep., 2020.
[Online]. Available: https://data.nrel.gov/submissions/127
[30] S. Powell, G. V. Cezar, and R. Rajagopal, “Speech original model,”
Mendeley Data, vol. V1, 2021.
[31] NREL, “Solar power data for integration studies,” https://www.nrel.gov/
grid/solar-power-data.html, Golden, CO, USA, accessed: 2023.
[32] K. Mongird, V. Viswanathan, J. Alam, C. Vartanian, V. Sprenkle, and
R. Baxter, “2020 grid energy storage technology cost and performance
assessment,” USDOE, Tech. Rep., December 2020. [Online]. Available:
https://www.energy.gov/energy-storage-grand-challenge/downloads/
2020-grid-energy-storage-technology-cost-/and-performance
[33] “Pacific gas and electric: Tariffs,” 2022, https://www.pge.com/tariffs/
index.page.
[34] D. Chakraborty, D. S. Bunch, J. H. Lee, and G. Tal, “Demand
drivers for charging infrastructure-charging behavior of plug-in electric
vehicle
commuters,”
Transportation
Research
Part
D:
Transport
and Environment, vol. 76, pp. 255–272, 2019. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S1361920919301919
