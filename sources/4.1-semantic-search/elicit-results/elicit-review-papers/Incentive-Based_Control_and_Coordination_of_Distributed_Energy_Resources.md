

---

Page 1

---

1
Hierarchical Control Framework for Integrated
Coordination between DERs and Demand Response
Di Wu, Jianming Lian, Yannan Sun, Tao Yang, and Jacob Hansen
Abstract—Demand response represents a signiﬁcant but largely
untapped resource that can greatly enhance the ﬂexibility and
reliability of power systems. This paper proposes a hierarchical
control framework to facilitate the integrated coordination be-
tween distributed energy resources and demand response. The
proposed framework consists of coordination and device layers.
In the coordination layer, various resource aggregations are
optimally coordinated in a distributed manner to achieve the
system-level objectives. In the device layer, individual resources
are controlled in real time to follow the optimal power dispatch
signals received from the coordination layer. For practical appli-
cations, a method is presented to determine the utility functions of
controllable loads by accounting for the real-time load dynamics
and the preferences of individual customers. The effectiveness
of the proposed framework is validated by detailed simulation
studies.
Index Terms—Distributed control, distributed energy resource,
demand response, hierarchical control, resource allocation.
I. INTRODUCTION
With growing emphasis on system efﬁciency and reliability,
a great effort has been made in developing distributed energy
resources (DERs) such as distributed generator (DG) and
energy storage. These resources are small and highly ﬂexible
compared with conventional generators, and are playing an
increasingly important role in the future smart grid [1], [2].
On the other hand, demand-side control has presented a
novel and viable way to supplement conventional supply-side
control [3]–[5]. In fact, demand response (DR) represents a
signiﬁcant but largely untapped resource in the power grid.
According to National Energy Technology Laboratory, with
only 10% customer participation, the potential nationwide
value of demand dispatch could be several billion dollars per
year in reduced energy costs [6]. The deployment of DERs
and DR will not only defer infrastructure investments in the
power grid, but also meet additional reserve requirements
from renewable generation. Although the deployment of DR
and DERs can lead to more economic and reliable system
operation, it requires proper coordination between DERs and
DR to harvest their potential beneﬁts.
The coordination problem can be solved in a completely
centralized manner, where a single control center accesses
This work was supported by the Laboratory Directed Research and Devel-
opment program at Paciﬁc Northwest National Laboratory. Paciﬁc Northwest
National Laboratory is operated for the U.S. Department of Energy by Battelle
Memorial Institute under Contract DE-AC05-76RL01830.
D. Wu, J. Lian, Y. Sun, and J. Hansen are with the Paciﬁc Northwest Na-
tional Laboratory, Richland, WA 99354 USA (e-mail: {di.wu, jianming.lian,
yannan.sun, jacob.hansen}@pnnl.gov).
T. Yang is the Department of Electrical Engineering, University of North
Texas, Denton, TX 76203 USA (e-mail: Tao.Yang@unt.edu).
states of potentially thousands of devices and broadcasts
control signals to them. Such a centralized control strategy
is often subject to several disadvantages, such as high require-
ment and cost in communication, substantial computational
burden, limited ﬂexibility and scalability, and disrespect of
privacy [7]. As an alternative, a distributed control strategy
has been proposed, where each control agent maintains a set
of variables and updates them through information exchange
with a few neighboring agents. During the past few years,
many studies have been dedicated to distributed approaches
for DER coordination. In [8], the authors developed a dis-
tributed algorithm that is resilient against potential packet
drops and applied the algorithm to DER coordination. In [9],
a strategy based on the local replicator equation was pre-
sented for economic dispatch of DGs. Other algorithms that
can be applied to the DER coordination include the leader-
follower consensus algorithm [10], two-level incremental cost
consensus algorithm [11], distributed algorithm based on the
consensus and bisection method [12], and minimum-time
consensus algorithm [13], just to name a few. There are also
studies that incorporated power losses into the distributed
algorithm design [14], [15]. Recently, coordination between
DERs and DR has been reported in [16] and [17]. Although
useful insights regarding DER and DR coordination have been
reported in these studies, the existing results cannot be directly
extended and applied to practical applications. This is because
the controllable loads were simply modeled as a “generator”
with negative generation, where the load characteristics and
dynamics were totally ignored. Furthermore, the studies did
not address the issue of designing real-time load control
strategies to achieve optimal power consumption. This paper
proposes a hierarchical control framework with two layers to
achieve integrated coordination of DERs and DR. The under-
lying control strategy accounts for the detailed characteristics
and dynamics of controllable loads, and addresses the issue of
designing real-time control strategies.
The rest of this paper is organized as follows. In Section II,
the major challenges of integrated coordination between DERs
and DR are ﬁrst discussed in detail, and then the proposed
hierarchical control framework is brieﬂy introduced with main
contributions highlighted. The top layer of the proposed frame-
work is described in Section III, where a general coordi-
nation problem between DERs and DR is formulated and
solved using a distributed approach. The bottom layer of the
proposed framework is described in Section IV, where the
device aggregation and real-time control are presented and
illustrated using air conditioners (ACs). In Section V, various
case studies along with detailed simulation results are provided
arXiv:1701.01913v1  [math.OC]  8 Jan 2017


---

Page 2

---

2
Fig. 1.
Illustration of the proposed hierarchical control framework for integrated coordination between DERs and DR.
to demonstrate the effectiveness of the proposed framework.
Finally, concluding remarks are given in Section VI.
II. PROBLEM STATEMENT AND PROPOSED FRAMEWORK
Power system operation requires instantaneous power bal-
ance between generation and demand that is constantly vary-
ing. Most balancing is achieved through energy scheduling.
In this paper, the short-term scheduling and operation prob-
lems are considered for DGs and controllable loads. At the
scheduling stage, the optimal resource allocation problem is
formulated and solved between DGs and DR, where the real-
time dynamics of controllable loads must be captured. At the
operation stage, real-time control is carried out so that DGs
and controllable loads follow optimal power generation and
consumption, respectively.
A. Technical Challenges
Although many results regarding DER and DR coordination
have been presented in the literature, there are still several
technical gaps that are signiﬁcant enough to prohibit practical
application of these existing results.
First, the cost functions of DGs and the utility functions
of controllable loads are required to formulate and solve the
optimal coordination problem. Existing studies such as [16]
and [17] assume that those functions are available and can be
directly used in the proposed distributed approaches. However,
it is not straightforward to construct the utility functions of
power for controllable loads as the cost functions of power for
DGs. For instance, the utility of using an AC is directly related
to the comfort an individual customer perceives at different
indoor air temperatures rather than the power consumption.
Therefore, it is required in practice to extract the utility
functions and capture the underlying economics based on the
preferences of individual customers.
Second, it is required for practical applications to consider
the operation stage as well. After the coordination problem
is solved at the scheduling stage, individual resources are
expected to follow optimal generation or consumption through
real-time control. It is straightforward for DGs to meet this
expectation because their generation level can be continuously
adjusted with existing generator controllers. However, this is
often not the case for controllable loads. Some controllable
loads such as thermostatically controllable loads have not been
designed with the capability to continuously adjust their power
consumption. Furthermore, their power consumption cannot
be directly controlled and is usually indirectly affected by
other control variables. For example, the thermostat of an AC
receives the temperature setpoint as the control input and then
automatically switches the compressor on and off to maintain
the indoor air temperature around the setpoint. Therefore, a
real-time load controller has to be designed for individual
controllable loads using the locally acceptable control input
while capturing the underlying economics.
Effectively coordinating and controlling DERs and DR for
short-term scheduling and real-time control cannot be realized
by simply adding one coordination algorithm to another load
control approach. A systematic method is needed to capture
the underlying economics and dynamics of controllable load
synthetically in both scheduling and real-time control. The
proposed framework herein exactly meets such a need. The
main contributions of this paper are summarized as follows:
• We discuss the gap between short-term scheduling and real-
time control from existing coordination algorithms and load
control approaches, and identify challenges to bridging the
gap.
• We design a holistic hierarchical control framework, which
is capable of directly adopting existing coordination algo-
rithms and load modeling/control approaches.
• We deﬁne the functionality and formulate mathematic
problems in each layer, and specify the information to
be exchanged between layers/sublayers in both short-term
scheduling and real-time control.
• We identify candidate coordination algorithms and load
control approaches that can ﬁt in the proposed framework,
and use example algorithm and approach to illustrate the
proposed framework.
B. Proposed Framework
To overcome the technical challenges described above, this
paper proposes a hierarchical control framework as shown in
Fig. 1 to facilitate integrated coordination between DERs and
DR. The proposed framework consists of two layers including


---

Page 3

---

3
coordination (top) and device layers (bottom). In Fig. 1, dash
lines represent information ﬂow between layers/sublayers,
where the information exchange frequency is the same as
short-term scheduling. Solid lines represent information ﬂow
within a layer/sublayer, where the information exchange fre-
quency is typically much higher than short-term scheduling.
An overview of each layer is provided herein and more details
are provided in the following sections.
• The coordination layer is only involved in short-term
scheduling stage. Prior to each scheduling period, each
coordinator receives aggregated utility or cost functions
from aggregators or device controllers, as indicated by the
green dash lines with up arrows. Then, the aggregation
of various resources including DGs and controllable loads
are optimally coordinated to achieve power balance. To
overcome the disadvantages associated with centralized
coordination algorithms, a distributed coordination method
can be employed, where local variables are exchanged
iteratively following algorithms as explained in Section III.
Once the coordination problem is solved, the regulation
signals are sent back to aggregators or device controllers
for real-time control, as indicated by the green dash lines
with down arrows.
• The device layer includes two sublayers: device aggregation
and device control.
– In the aggregation sublayer, DERs are divided into groups
as appropriate. Prior to each scheduling period, each ag-
gregator received utility or cost functions from its under-
lying device controllers (as indicated by the red dash lines
with up arrows), determines the aggregated functions,
and then sends these information to the corresponding
coordinator in the top layer (as indicated by the green
dash lines with up arrows). After coordination problem
is solved, each aggregator receives the regulation signals
from top layer (as indicated by the green dash lines with
down arrows) and then broadcasts these signals to its
underlying devices (as indicated by the red dash lines
with down arrows) to collectively provide the desired
power generation or consumption.
– The device control sublayer is involved in both schedul-
ing and real-time operation stages. At the scheduling
stage, the controller at each device reports to its comman-
der (either an aggregator or a coordinator) the required
information (as indicated by the green/red dash lines with
up arrows), which is then used for coordination. After
coordination problem is solved, it receives the regulation
signals from its commander (as indicated by the green/red
dash lines with down arrows). During real-time operation,
it regulates devices to fulﬁll their functionality (e.g.,
control the indoor air temperature within the comfort
zone) while following the scheduled energy generation
or consumption.
III. OPTIMAL RESOURCE COORDINATION
A. General Description
In the coordination layer, the optimal coordination problem
is solved for each coordination period to determine the most
economic schedule of power generation and consumption for
DERs and DR, respectively. The objective is to maximize the
social welfare, i.e., the difference between the utility of power
consumption and the cost of power generation, while meeting
the desired total power output without violating operating
constraints of individual resources.
The mathematical formulation of the scheduling problem
for each coordination period is presented as follows, where
power generation or consumption should be understood as the
average value during each coordination period,
min
pGi, pLj
NG
X
i=1
CGi(pGi) −
NL
X
j=1
ULj(pLj)
(1a)
subject to
NG
X
i=1
pGi −
NL
X
j=1
pLj = D
(1b)
0 ≤P min
Gi
≤pGi ≤P max
Gi
(1c)
0 ≤P min
Lj
≤pLj ≤P max
Lj
(1d)
where different notations are deﬁned as follows:
– NG (or NL) is the number of generator (or load) aggregation
in the network;
– CGi(pGi) is the cost of the i-th generator aggregation as a
function of the power generation pGi;
– ULj(pLj) is the utility of the j-th load aggregation as a
function of the power consumption pLj;
– D is the desired total power output;
– [P min
Gi , P max
Gi ] is the range of power generation for the i-th
generator aggregation;
– [P min
Lj , P max
Lj
] is the range of power consumption for the
j-th load aggregation.
Note that [P min
Lj , P max
Lj
] for each load aggregation can be
obtained by aggregating the power range of individual con-
trollable loads. For example, the average power consumption
of an AC for the next 5 minutes depends on the temperature
setpoint selected by the homeowner, the current indoor air
temperature and the outside air temperature, etc.
B. Proposed Approach
Without loss of generality, all the DGs can be enumerated as
the ﬁrst NG agents. The optimization problem deﬁned in (1a)–
(1d) can then be generalized as
min
pi
N
X
i=1
Ci(pi)
(2a)
subject to
N
X
i=1
pi = D
(2b)
P min
i
≤pi ≤P max
i
,
i = 1, . . . , N
(2c)
where N = NG + NL,
pi =
 pGi,
i = 1, . . . , NG
−pLi−NG ,
i = NG + 1, . . . , NG + NL
(3)
Ci(·) =
(
CGi(·),
i = 1, . . . , NG
−ULi−NG (·),
i = NG + 1, . . . , NG + NL.
(4)


---

Page 4

---

4
The optimal solution can be obtained through various dis-
tributed coordination algorithms reviewed in Section I. Most
of these algorithms are consensus-based with marginal cost
modeled as consensus variables. They solve the problem
essentially through price-directive decomposition, which is
actually the gradient method applied to the dual problem.
Different methods have been proposed to update the dual
variable using partial or total mismatch between demand and
supply (the gradient of the dual problem) [8], [10]–[12], [16].
In this paper, we use the distributed coordination algorithm
proposed in [18].
Prior to each scheduling period, each coordinator receives
the aggregated utility or cost functions as well as the power
operating ranges from aggregators or device controllers, as
indicated by the green dash lines with up arrows in Fig. 1.
Next, each coordinator converts the received cost/utility func-
tions and power output to Ci(·) and pi, respectively, according
to (2). Then, the coordinator starts to run the coordination
algorithm as shown in (5).
λi(k + 1)=λi(k) −βk
X
j∈Ni
(λi(k) −λj(k))
−αk(pi(k) −Di) ,
(5a)
pi(k + 1)=∇C−1
i
(λi(k + 1)) ,
(5b)
where Ni = {j ∈V|(j, i) ∈E} is the neighboring set of the
i-th agent, ∇Ci(·) is the derivative of cost function and ∇C−1
denotes its inverse function, αk and βk are the gain parameters
at step k for innovation term and consensus term , respectively,
and Di is chosen such that PN
i=1 Di = D. The determination
of Di can be arbitrary. In practice, one option to determine
Di is that the system operator forecasts the total demand D,
and then arbitrarily distributes this demand to a small set of
agents or even a single agent (Di is zero for the remaining
agents). Alternatively, each agent can also determine its own
Di. This strategy is used in this paper. Please refer to Section
V.A for more details.
With this algorithm, each coordinator i only maintains a
local variable λi that is the estimate of the optimal incremental
cost, and updates it through information exchange with its
neighboring coordinators (as indicated by the black lines in
the coordinator layer in Fig. 1.) By executing (5), λi(k) and
pi(k) at each coordinating agent will converge to the optimal
dual variable (clearing prices) and power output, which are
sent back to aggregators or device controllers for real-time
control, as indicated by the green dash lines with down arrows
in Fig. 1.
IV. DEVICE AGGREGATION AND CONTROL
A. General Description
Although it is necessary to have CGi(pGi) and ULj(pLj) to
formulate the optimal coordination problem as shown in (1a)–
(1d), the distributed algorithms only require their derivatives,
C′
Gi(pGi) and U ′
Lj(pLj), to solve this coordination problem.
The derivative of CGi(pGi) (or ULj(pLj)) is often referred
to as the supply (or demand) curve, which characterizes the
relationship between marginal cost (or utility) and power
generation (or consumption). Hence, the device layer has to
determine the supply and demand curves of various resources
and send them to the coordination layer at the beginning
of each coordination period. To maintain the scalability of
the proposed framework in dealing with a large number
of resources, the device layer is further divided into two
sublayers: device aggregation and device control. In the device
aggregation sublayer, resources of similar type are grouped
together when their individual sizes are small. In practice,
the resource aggregation is usually employed to either fa-
cilitate coordination processes or represent business models.
Each aggregator serves as the message channel between the
coordination layer and the device control sublayer. It collects
the individual supply or demand curves from resources within
its aggregation (as indicated by the red dash lines with up
arrows in Fig. 1), and then sends the aggregated curve to the
coordination layer (as indicated by the green dash lines with
up arrows in Fig. 1). Then it sends the optimal dispatch signals
received from the coordination layer to the device control
sublayer (as indicated by the red dash lines with down arrows
in Fig. 1). In the device control sublayer, real-time control
translates the optimal dispatch signals into local control inputs
so that individual resources can follow the optimal generation
or consumption.
The supply curves of DGs can be easily determined based
on generator operational cost, fuel efﬁciency, and fuel cost.
It is also straightforward for them to follow the optimal
generation in real time because their generation level can
be continuously adjusted with well established controllers.
However, for controllable load, technical challenges exist in
i) determining the demand curves of controllable loads based
on individual customer preference, and ii) designing real-time
control that can translate optimal power demand into locally
acceptable control input. As pointed out in Section II, one
essential step is to obtain the relationship between marginal
utility and local control input.
B. Proposed Approach
The demand curve dynamically represents how individual
customers value convenience or comfort and the corresponding
energy usage. It is essential to capture the opportunity cost of
DR. To extract the demand curve, it is necessary to quanti-
tatively relate the marginal utility of individual customers for
power demand to the local control input based on customer
preference. Herein, a practical method is presented for ACs
to extract such a relationship. This method was originally
proposed in the GridWise R
⃝demonstration project [19], and
then rigorously analyzed in [20]. Although it has been speciﬁ-
cally presented for ACs, the underlying control philosophy can
be easily extended and applied to other types of controllable
loads.
This method represents the relationship between marginal
utility and local control input by a response curve as illus-
trated in Fig. 2, which is determined by several parameters.
The parameters λavg and σ are the average and variance,
respectively, of the electricity prices over a period of time
in the past, which can be calculated by a local controller or
load aggregator. The parameters Tdesired, Tmin, and Tmax are


---

Page 5

---

5
Fig. 2.
Illustration of the response curves for air conditioners.
Fig. 3.
User interface in the GridWise R
⃝demonstration project
directly speciﬁed by users, where Tdesired is the desired indoor
air temperature setpoint, and Tmin and Tmax are the lower and
upper bounds of the acceptable indoor air temperature setpoint.
The parameter k is a positive number completely abstracted
from the owner’s preference of indoor air temperature setpoint
over the electricity price. For example, when k is very large,
the response curve becomes an almost vertical line at Tdesired.
This implies that the homeowner is very sensitive to the indoor
air temperature, and would like to maintain the indoor air
temperature setpoint at Tdesired regardless of the electricity
price. When k is close to zero, the response curve becomes
an almost horizontal line at λavg. This implies that the house
owner is very sensitive to the electricity price, and would
like to sacriﬁce comfort for cost saving. In the GridWise R
⃝
demonstration project, the abstraction of k is done by letting
individual homeowners specify their preferences of comfort
over cost through a user interface as shown in Fig. 3.
In the proposed framework, prior to each coordination
period, each load controller at the device layer determines
its DR curve (which is equivalent to the utility/cost function)
considering the load dynamics. These curves are sent to
aggregators (as indicated by the red dash lines with up arrows
in Fig. 1), and then aggregated at aggregators and later used
by coordinators to run the distributed coordination algorithms
for determining the optimal power consumption and real-time
price signal. The price signal is then broadcasted to each
device every 5 minutes, as indicated by the red dash lines with
down arrows in Fig. 1. Within each 5-minute operating period,
this response curve will be used by a real-time controller to
translate the optimal power demand represented by clearing
price λclear into the indoor air temperature setpoint Tset for
this operating period. Recall that the demand curve is the
mapping from marginal utility to power demand. Since the
response curve is the mapping from marginal utility to the
indoor air temperature setpoint, it is only left to determine the
relationship between indoor air temperature setpoint and power
demand. The dynamics of each AC i can be described by the
Fig. 4.
Illustration of the demand response curves of air conditioners.
Equivalent Thermal Parameter model. The detailed model can
be found in [21], [22], and can be represented in a simpliﬁed
form as
˙xi(t) =
 Aixi(t) + Bi
on
if qi(t) = 1
Aixi(t) + Bi
off
if qi(t) = 0,
(6)
where xi(t) is the continuous state vector consisting of indoor
air temperature T i
a(t) and mass temperature T i
m(t), and qi(t)
denotes the operating mode of the AC with qi(t) = 1 when
it is ON and qi(t) = 0 when it is OFF. The operating mode
of the AC for cooling is usually controlled by a hysteretic
controller,
qi(t+) =



1
if T i
a(t) ≥Tset + δ/2
0
if T i
a(t) ≤Tset −δ/2
qi(t)
otherwise,
(7)
where δ is the hysteresis band centered around the indoor
air temperature setpoint Tset. When the model parameters
(Ai, Bi
on, Bi
off) are known to local controllers, the relationship
between indoor air temperature setpoint and power consump-
tion can be derived, which ﬁnally leads to the demand curve
as shown in Fig. 4 by taking into account the corresponding
response curve. The determination of Ei
max, Ei
min, λi
min, and
λi
max is provided in the Appendix. If the model parameters
are unknown, they can be estimated based on the measured
indoor air temperature as proposed in [23]. The individual
demand curves will be sent to the load aggregator, where they
are aggregated together, and sent to the coordination layer to
solve the optimal coordination problem.
With this method, the load utility/cost functions depend
on the market clearing price during previous periods, the
outside air temperature, and customer preference for comfort.
Therefore, these functions in (4) are time-varying from one
scheduling period to another. The DR curve illustrated in Fig. 4
is the derivative of utility function (1a). Since the DR curve is
monotonically non-increasing, the utility function is concave.
The negative utility function in (1a) becomes a cost function
in (2a), which is convex.
V. CASE STUDIES
This section demonstrates the proposed hierarchical control
framework by case studies on the IEEE 123-node system
that was prepared by IEEE PES Distribution System Analysis
Subcommittee’s Distribution Test Feeder Working Group [24].
The simulation studies are implemented in GridLAB-D [25],


---

Page 6

---

6
Fig. 5.
IEEE 123-node test system.
TABLE I
GENERATOR PARAMETERS
DG No.
ai (kW2h)
bi ($/kWh)
ci ($/h)
Range (kW)
1
0.00015
0.0267
0.38
[50,500]
2
0.00052
0.0152
0.65
[20,100]
3
0.00042
0.0185
0.4
[40,200]
4
0.00031
0.0297
0.3
[20,250]
5
0.00025
0.0156
0.33
[30,300]
which is an advanced open-source power systems modeling
and simulation environment developed at Paciﬁc Northwest
National Laboratory.
A. Test System Description
The IEEE 123-node test system shown in Fig. 5 consists
of 123 nodes and 118 lines. It has been modiﬁed to include
houses with ACs and other residential loads. The number of
houses has been adjusted to match the peak load provided
in the test system dataset, which results in 1,222 houses.
The following studies assume that 988 ACs participate in the
DR program, and the remaining 234 ACs are uncontrollable
as other residential loads. The controllable ACs are grouped
into three load aggregations, where the number of houses
under each aggregation are 98, 254, and 632, respectively.
There are ﬁve DGs connected to the system, whose generation
cost parameters are adopted from [26] and [27] and listed in
Table I. Although it is typical to represent generation cost
by quadratic functions, the distributed algorithms reviewed in
the Introduction section are able to handle convex functions
that are more general than quadratic functions. In fact, the
cost functions of DR in this paper are convex, as explained
in Section IV-B. The distributed algorithm for solving the
optimal coordination problem is selected to be the leaderless
algorithm deﬁned in (5a) and (5b), which requires undirect
communication networks.
Prior to each coordination period, which is selected to
be 5 minutes, controllable loads are aggregated and then
coordinated with DGs so that they can meet
contr. load + uncontr. load −DG gen. = ref.
(8)
In (8), ref. represents the desired power consumption of
the distribution system and can be commanded by system
operators. For example, in island microgrid operation, the
command will be set to zero, i.e., DGs and controllable loads
are scheduled to balance the uncontrollable load within the
microgrid for each 5-minute period. For a grid-connected
distribution system, DGs and DR can be controlled to follow a
given signal for either reducing energy cost or providing grid
services. For example, they can actively participate in the load
following service by setting the reference signal as
ref. = feeder hourly schedule −load following signal.
In the coordination problem (2), the desired total output from
DGs and DR is
D = ref. −uncontr. load .
(9)
In order to apply the distributed algorithm in (5), we need
to determine Di such that P
i Di = D. In this paper, we
choose to distribute D only among three load aggregators and
set Di to zero for DGs. The distribution of D is realized by
distribution of ref. signal and local uncontr. load. First, ref.
signal can be arbitrarily distributed among load aggregators
ofﬂine, prior to scheduling period. In this paper, we evenly
distribute this signal among three aggregators. On the other
hand, the uncontrollable load at each aggregator is unknown
and needs to be forecasted. While there are different load fore-
casting methodologies, e.g., artiﬁcial neural networks [28], au-
toregressive moving average models [29], and semi-parametric
additive models [30], this work simply assumes that the
forecast of local uncontrollable load in the next 5-minute
period is equal to the measured local uncontrollable load in the
current period. Please note that renewable generation as one
kind of important distributed generation could also be modeled
as negative uncontrollable load as it is typically controlled for
maximum power tracking. It is forecasted and adjusted every
5 minutes, and becomes a component of ‘uncontr. load’. In
such a way, controllable load and DGs can be optimally used
to help address the uncertainty and variability from renewable
generation.
When performing DGs and DR coordination for the time
period t using (5a) and (5b), the initial values of power pi
and marginal costs λi are set to be converged values in the
time period t−1. This can help to greatly reduce the required
number of iterations.
B. Simulation Results
1) Base case (Case 1): The test system is ﬁrst simulated
without any DGs and controllable loads for a typical summer
day with a minimum time step of 30 seconds. The 5-minute
average feeder power consumption is plotted in Fig. 6, together
with the outside air temperature. Since AC load accounts for
more than 80% of the total load in this system, the system
load increases as the outside air temperature rises.


---

Page 7

---

7
0 1
2
3 4
5
6 7
8
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
0
2
4
6
Feeder load (MW)
Hour of day
 
 
0 1
2
3 4
5
6 7
8
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
70
80
90
100
Outside air temperature (°F)
Feeder load
Temperature
Fig. 6.
Base case feeder load (5-minute average) and outside air temperature.
0 1
2
3 4
5
6 7
8
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
0
0.5
1
1.5
2
2.5
3
3.5
4
Hour of day
Power [MW]
 
 
Desired
Actual
Fig. 7.
Desired vs. resulted feeder load (both are 5-minute average).
2) Active DER and DR Coordination (Case 2): The test
system is then simulated with DGs and controllable loads
under the proposed hierarchical control framework for the
same summer day. In general, the reference signal can be
any time series within the capability of the active distribution
system. To verify the effectiveness of the proposed framework,
the desired feeder load consumption is set to be 0.7 of the
feeder load in base case, as shown by the blue dashed line
in Fig. 7. Such a reference signal is simple to construct yet
useful for testing the proposed method because
• The 30% reduction of load at the feeder requires the
participation of DG and DR during scheduling, which is
exactly what we need to study.
• The reduction is proportional to the load feeder in the
base case and therefore varies with time. Such varying load
reduction requires DG and DR to vary their generation or
consumption in a coordinative manner.
• Such a desired signal requires DG and DR to support the
local system more during peak hours than off-peak hours,
which seems plausible. The test case enables us to compare
DER participation in peak hours with off-peak hours, as
well as the difference in energy price of the distribution
system.
The obtained 5-minute average power consumption is plot-
ted by the red curve in Fig. 7. As can be seen, the actual feeder
load follows the desired value with reasonable accuracy. The
small mismatch is due to a few factors such as approximation
of demand curve, errors in uncontrollable load forecast, and
0 1
2
3 4
5
6 7
8
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
0
0.05
0.1
0.15
0.2
0.25
0.3
0.35
0.4
Hour of day
Power [MW]
 
 
DG1
DG2
DG3
DG4
DG5
Fig. 8.
Generation output from DGs in Case 2.
0 1
2
3 4
5
6 7
8
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
0
0.5
1
Agg. 1
Hour of day
Power [MW]
 
 
Scheduled
Actual
Max
Min
0 1
2
3 4
5
6 7
8
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
0
0.5
1
1.5
Agg. 2
Power [MW]
Hour of day
0
1
2
3 4
5
6 7
8
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
0
1
2
3
Agg. 3
Power [MW]
Hour of day
Fig. 9.
Load under each aggregator in Case 2.
approximation of optimal solution in coordination layers.
The output of DGs is shown in Fig. 8. DG2 is the cheapest
generator and is at its maximum output almost all the time.
Other DGs generate more during peak hours, because the
reference signal essentially requires more reduction from the
base case during peak hours. It can be easily veriﬁed that
the marginal cost of all DGs that are not at their generation
limits is the same, using the cost parameters in Table I. The
scheduled and actual load from aggregators together with
their dynamic capability (max and min) are plotted in Fig. 9.
The feasible load range for each AC in each time period
depends on the current indoor air temperature, temperature
setpoint and acceptable range, price information etc., and
therefore varies signiﬁcantly from one time period to another.
Nevertheless, the feasible load range from aggregating a large
number of ACs does not vary much. The actual average power
consumption closely follows the desired value, which veriﬁes
the effectiveness of the proposed coordination and control.
The acceptable temperature settings and the simulated in-
door air temperature are plotted in Fig. 10 for a house under
Aggregator 1. Based on how customers value their com-


---

Page 8

---

8
0 1
2
3 4
5
6 7
8
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
60
65
70
75
80
Hour of day
Temperature (°F)
 
 
Inside air temperature
Tmax
Tmin
Fig. 10.
Indoor air temperature of House 1 under Aggregator 1 in Case 2.
0
1
2
3
4
5
6
7
8
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
0
1
2
3
Agg. 3 load
Hour of day
Power (MW)
 
 
w/o constraints
w/ constraints
Thermal capacity
0
1
2
3
4
5
6
7
8
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
10
15
20
25
Agg. 3 price
Hour of day
Price (cents/kWh)
 
 
w/o constraints
w/ constraints
Fig. 11. Power consumption and clearing price under Aggregator 3 in Case 3.
fort, temperature setpoint varies with the system energy cost
throughout a day. During off-peak hours when the energy price
is low, the temperature setpoint and indoor air temperature are
closer to the desired value, which is 72.3 ◦F in this case.
3) Active DER and DR Coordination with Line Capacity
Constraints (Case 3): It follows from Fig. 9 that the load
from Aggregator 3 exceeds 2 MW during peak hours. Now
suppose that the thermal capacity is at 2 MW for the branch
that connects Aggregator 3 to the distribution system. Since
the branch connects only Aggregator 3 to the distribution
system, the power consumption by Aggregator 3 is equal to
the power ﬂow in the branch (ignoring losses for simplicity).
Therefore, the capacity limit of such a branch can be taken
care of by imposing the limit to Aggregator 3’s power range,
i.e., modifying the maximum power consumption pmax
i
of
Aggregator 3 in (2c). In this case, the maximum power limit
of Aggregator 3 in (2c) becomes active for some time. The
simulation results are shown in Fig. 11. It can be seen that the
proposed framework can account for local thermal constraints
as well when coordinating DERs and DR. When congestion
occurs, the active local constraint signiﬁcantly raises the en-
ergy price for the load under Aggregator 3. It should be noted
that the load and price are obtained using the same optimal
coordination algorithm, rather than being manually modiﬁed to
meet the local constraint. Compared with the case where there
is not line capacity constraints, these load and price are just
some different solutions of the optimal coordination problem
(2) with some updated parameters.
VI. CONCLUSIONS
This paper presents a hierarchical control framework to
integrate DR into DER coordination. The proposed framework
takes the advantage of existing coordination algorithms and
device controllers, and bridges the gap between short-term
scheduling and real-time control of controllable loads. This
is done by synthetically capturing the underlying economics
from DR as well as detailed dynamics for device-level control.
Simulation results showed that the proposed method is capable
to optimally coordinate DR with DGs and control DR in real-
time to realize the desired allocation of power consumption.
The future work is to expand this framework to include
distributed energy storage into this coordination between DGs
and controllable loads.
APPENDIX A
DEMAND CURVE DETERMINATION
The demand curve of each AC as shown in Fig. 4 is charac-
terized by the maximum and minimum energy consumptions
(Ei
max and Ei
min), and the corresponding energy prices (λi
min
and λi
max), which can be calculated as follows:
• Ei
max and λi
min: For the i-th unit, the theoretical upper bound
of average power consumption corresponds to the operation
when the device is ON for the entire period. In this case, the
average power consumption is simply equal to pc, which
is the instantaneous power when the device is ON and
is constant through the 5-minute operating period. With
qi(t) = 1, the closed-form analytical expression of indoor
air temperature T i
a(t) can be obtained by solving (6). The
setpoint Tset must be low enough to satisfy (10) to maintain
the ON status for the entire period assuming the device is
operated in cooling mode,
Tset ≤T on
set ,
(10)
where T on
set = mint{T i
a(t)}−δ/2 when the device is initially
OFF, and T on
set = mint{T i
a(t)} + δ/2 when the device is
initially ON.
– If T on
set ≥Tmin, where Tmin is the lowest acceptable
temperature setpoint speciﬁed by the user, ﬁnd the energy
price λi
min which corresponds to T on
set on the curve in Fig 2.
For any price that is less than λi
min, AC i will be ON for
the entire operating period and the maximum average
power consumption Ei
max is pc.
– If T on
set < Tmin, the device can only be ON for part of
the period, because Tset (≥Tmin > T on
set) will trigger the
device to be OFF for at least some time during the period.
In this case, the energy price λi
min simply corresponds
to Tmin on the curve in Fig 2. The corresponding upper
bound of feasible average power consumption Ei
max can
be found by solving (6) and (7) by letting Tset = Tmin.


---

Page 9

---

9
• Ei
min and λi
max: The theoretical lower bound of average
power consumption is zero and it corresponds to the op-
eration when the device is OFF for the entire period. The
setpoint Tset must satisfy (11) to maintain the OFF status
for the entire period when the device is operated in cooling
mode,
Tset ≥T off
set ,
(11)
where T off
set = maxt{T i
a(t)}−δ/2 when the device is initially
OFF, and T off
set = maxt{T i
a(t)} + δ/2 when the device is
initially ON.
– If T off
set ≤Tmax, where Tmax is the highest acceptable
temperature setpoint speciﬁed by the user, ﬁnd the energy
price λi
max which corresponds to T off
set on the curve in
Fig 2. For any price that is higher than λi
max, AC i will
be OFF for the entire operating period and there is no
energy consumption.
– If T off
set > Tmax, the device can only be OFF for part of
the period, because Tset (≤Tmax < T off
set ) will trigger the
device to be ON for at least some time during the period.
In this case, the energy price λi
max simply corresponds to
Tmax on the curve in Fig 2. The corresponding lower
bound of feasible average power consumption Ei
min can
be found by solving (6) and (7) by letting Tset = Tmax.
• For any point between λi
min and λi
max, the device will only
be ON for part of the period. The closed-form analytical
expression does not exist, but the numerical method can be
used to ﬁnd the corresponding average power consumption.
This process needs to be repeated for a large number of
points to accurately characterize the demand curve. On
the other hand, submitting the entire demand curve to
aggregators requires sending all the points, which also
burdens the communication network. In fact, many practical
applications do not require the entire demand curve, and its
approximation should good enough for engineering purpose.
For example, the demand curve shown in Fig. 4 can be ap-
proximated by a step curve as long as the difference between
λi
min and λi
max is small. In this case, only three quantities
including Ei
min, Ei
max and (λi
min + λi
max)/2 are required to
characterize the approximated step curve, thereby reducing
communication requirement and computational cost.
REFERENCES
[1] J. Driesen and F. Katiraei, “Design for distributed energy resources,”
IEEE Power Energy Mag., vol. 6, no. 3, pp. 30–40, May 2008.
[2] J. Huang, C. Jiang, and R. Xu, “A review on distributed energy resources
and Microgrid,” Renew. Sust. Energy Rev., vol. 12, no. 9, pp. 2472–2483,
2008.
[3] A. Ipakchi and F. Albuyeh, “Grid of the future,” IEEE Power Energy
Mag., vol. 7, no. 2, pp. 52–62, Mar./Apr. 2009.
[4] P. Palensky and D. Dietrich, “Demand side management: Demand
response, intelligent energy systems, and smart loads,” IEEE Trans. Ind.
Informat., vol. 7, no. 3, pp. 381–388, Aug. 2011.
[5] D. S. Callaway and I. A. Hiskens, “Achieving controllability of electric
loads,” Proc. IEEE, vol. 99, no. 1, pp. 184–199, Jan. 2011.
[6] J. Goellner, M. Prica, J. Miller, S. Pullins, J. Westerman, J. Harmon,
T. Grabowski, H. Weller, B. Renz, S. Knudsen, and D. Coen, “Demand
dispatch—intelligent demand for a more efﬁcient grid,” National Energy
Technology Laboratory, Tech. Rep. DOE/NETL-DE-FE0004001, 2011.
[7] H. Farhangi, “The path of the smart grid,” IEEE Power Energy Mag.,
vol. 8, no. 1, pp. 18–28, Jan. 2010.
[8] A. D. Domínguez-García, C. N. Hadjicostis, and N. F. Vaidya, “Resilient
networked control of distributed energy resources,” IEEE J. Sel. Areas
Commun., vol. 30, no. 6, pp. 1137–1148, Jul. 2012.
[9] A. Pantoja, N. Quijano, and K. M. Passino, “Dispatch of distributed
generators under local-information constraints,” in Proc. IEEE American
Control Conf., Jun. 2014, pp. 2682–2687.
[10] Z. Zhang, X. Ying, and M.-Y. Chow, “Decentralizing the economic
dispatch problem using a two-level incremental cost consensus algorithm
in a smart grid environment,” in Proc. North Amer. Power Symp. (NAPS),
2011, pp. 1–7.
[11] Z. Zhang and M.-Y. Chow, “Convergence analysis of the incremen-
tal cost consensus algorithm under different communication network
topologies in a smart grid,” IEEE Trans. Power Syst., vol. 27, no. 4, pp.
1761–1768, 2012.
[12] H. Xing, Y. Mou, M. Fu, and Z. Lin, “Distributed bisection method
for economic power dispatch in smart grid,” IEEE Trans. Power Syst.,
vol. 30, no. 6, pp. 3024–3035, Nov. 2015.
[13] T. Yang, D. Wu, Y. Sun, and J. Lian, “Minimum-time consensus based
approach for power system applications,” IEEE Trans. Ind. Electron.,
vol. 63, no. 2, pp. 1318–1328, Feb. 2016.
[14] G. Binetti, A. Davoudi, F. L. Lewis, D. Naso, and B. Turchiano, “Dis-
tributed consensus-based economic dispatch with transmission losses,”
IEEE Trans. Power Syst., vol. 29, no. 4, pp. 1711–1720, Jul. 2014.
[15] W. T. Elsayed and E. F. El-Saadany, “A fully decentralized approach
for solving the economic dispatch problem,” IEEE Trans. Power Syst.,
vol. 30, no. 4, pp. 2179–2189, Jul. 2015.
[16] G. Hug, S. Kar, and C. Wu, “Consensus + innovations approach for
distributed multiagent coordination in a microgrid,” IEEE Trans. Smart
Grid, vol. 6, no. 4, pp. 1893–1903, Jul. 2015.
[17] Y. Xu, Z. Yang, W. Gu, M. Li, and Z. Deng, “Robust real-time distributed
optimal control based energy management in a smart grid,” IEEE Trans.
Smart Grid, pp. 1–12, 2015, to appear.
[18] S. Kar and G. Hug, “Distributed robust economic dispatch in power
systems: A consensus + innovations approach,” in Proc. IEEE Power
Energy Soc. Gene. Meet., Jul. 2012.
[19] J. C. Fuller, K. P. Schneider, and D. Chassin, “Analysis of residential
demand response and double-auction markets,” in Proc. IEEE Power
and Energy Soc. Gene. Meet., Jul. 2011, pp. 1–7.
[20] S. Li, W. Zhang, J. Lian, and K. Kalsi, “Market-based coordination of
thermostatically controlled loads—Part I: A mechanism design formu-
lation,” IEEE Trans. Power Syst., vol. 31, no. 2, pp. 1170–1178, Mar.
2016.
[21] “Residential module user’s guide.” [Online]. Available: http://gridlab-d.
sourceforge.net/wiki/index.php/Residential_module_user’s_guide
[22] A. Thomas, P. Jahangiri, D. Wu, C. Cai, H. Zhao, D. C. Aliprantis,
and L. Tesfatsion, “Intelligent residential air-conditioning system with
smart-grid functionality,” IEEE Trans. Smart Grid, vol. 3, no. 4, pp.
2240–2251, Dec. 2012.
[23] S. Li, W. Zhang, J. Lian, and K. Kalsi, “Market-based coordination
of thermostatically controlled loads—Part II: Unknown parameters and
case studies,” IEEE Trans. Power Syst., vol. 31, no. 2, pp. 1179–1187,
Mar. 2016.
[24] Distribution test feeders. Distribution Test Feeder Working Group, IEEE
PES Distribution System Analysis Subcommittee. [Online]. Available:
http://ewh.ieee.org/soc/pes/dsacom/testfeeders/index.html
[25] GridLAB-D. [Online]. Available: http://www.gridlabd.org/
[26] T. Logenthiran, D. Srinivasan, A. M. Khambadkone, and H. N. Aung,
“Multiagent system for real-time operation of a microgrid in real-time
digital simulator,” IEEE Trans. Smart Grid, vol. 3, no. 2, pp. 925–933,
Jun. 2012.
[27] M. Modiri-Delshad, S. Koohi-Kamali, E. Taslimi, S. H. Aghay Kaboli,
and N. A. Rahim, “Economic dispatch in a microgrid through an
iterated-based algorithm,” in Proc. IEEE Clean Energy Tech., Nov. 2013,
pp. 82–87.
[28] H. S. Hippert, C. E. Pedreira, and R. C. Souza, “Neural networks for
short-term load forecasting: a review and evaluation,” IEEE Trans. Power
Syst., vol. 16, no. 1, pp. 44–55, Feb. 2001.
[29] S.-J. Huang and K.-R. Shih, “Short-term load forecasting via ARMA
model identiﬁcation including non-Gaussian process considerations,”
IEEE Trans. Power Syst., vol. 18, no. 2, pp. 673–679, May 2003.
[30] S. Fan and R. Hyndman, “Short-term load forecasting based on a semi-
parametric additive model,” IEEE Trans. Power Syst., vol. 27, no. 1, pp.
134–141, Feb. 2012.
