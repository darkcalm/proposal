# Hu2017 Transactive control  a framework for operating power systems characterized by high penetration of distributed energy resources

## Paper Metadata

- **Filename:** Hu2017_Transactive_control__a_framework_for_operating_power_systems_characterized_by_high_penetration_of_distributed_energy_resources_DOI_10-1007_s40565-016-0228-1.pdf
- **DOI:** 10.1007/s40565.016.0228.1
- **Authors:** Not available
- **Year:** Not available
- **Journal/Venue:** Not available
- **URL:** Not available
- **Extraction Date:** 2025-06-03T15:04:05.856013
- **Total Pages:** 14

## Abstract

Abstract not available from BibTeX metadata.

## Keywords

Keywords not available from BibTeX metadata.

---

## Full Text Content



### Page 1

Transactive control: a framework for operating power systems
characterized by high penetration of distributed energy resources
Junjie HU1
, Guangya YANG1, Koen KOK1,2, Yusheng XUE3,
Henrik W. BINDNER1
Abstract The increasing number of distributed energy
resources connected to power systems raises operational
challenges for the network operator, such as introducing
grid congestion and voltage deviations in the distribution
network level, as well as increasing balancing needs at the
whole system level. Control and coordination of a large
number of distributed energy assets requires innovative
approaches. Transactive control has received much attention due to its decentralized decision-making and transparent characteristics. This paper introduces the concept
and main features of transactive control, followed by a
literature review and demonstration projects that apply to
transactive control. Cases are then presented to illustrate
the transactive control framework. At the end, discussions
and research directions are presented, for applying transactive control to operating power systems, characterized by
a high penetration of distributed energy resources.
Keywords Distributed energy resources, Distribution
system operation, Smart grids, Transactive control
1 Introduction
An important means used by the power industry to reduce
greenhouse-gas emissions and fossil-fuel dependency is the
introduction of renewable energy generation such as wind
and solar [1–3]. As part of this transition to sustainability, the
majority of new generation units are being connected to
distribution grids [4, 5]. In addition, new loads are being
introduced, such as electric vehicles and heat pumps.
Although these new loads lead to higher overall energy
efﬁciency, their introduction leads to higher electricity use
and thus, to higher power loading of the power grid. These
new energy resources bring challenges to power system
operation, including a decline in reserve power from traditional sources [6], and grid congestion [7]. In this paper,
electric vehicles, heat pumpsetc.ﬂexible loads, storages, and
distributed generation, including renewable generation units
such as wind turbine and photovoltaic generation, are generally referred to distributed energy resources (DER). In
order to cope with the challenges described above, DER
needs to be become actively involved in grid coordination
and operation tasks; and the demand response scheme of the
DER needs to be introduced to make available additional
operational ﬂexibility [8].
The problems encountered in the power systems have
received much attention, and various efforts have been
made
to
address
the
problems.
These
range
from
Cross Check date: 16 May 2016
Received: 13 January 2016 / Accepted: 16 May 2016 / Published
online: 23 August 2016
 The Author(s) 2016. This article is published with open access at
Springerlink.com
& Junjie HU
junhu@elektro.dtu.dk
Guangya YANG
gyy@elektro.dtu.dk
Koen KOK
koenkok@elektro.dtu.dk
Yusheng XUE
xueyusheng@sgepri.sgcc.com.cn
Henrik W. BINDNER
hwbi@elektro.dtu.dk
1
Center for Electric Power and Energy, Technical University
of Denmark, Copenhagen, Denmark
2
Netherlands Organization for Applied Research, TNO,
The Hague, The Netherlands
3
State Grid Electric Power Research Institute, Nanjing, China
123
J. Mod. Power Syst. Clean Energy (2017) 5(3):451–464
DOI 10.1007/s40565-016-0228-1

---


### Page 2

developing new control methods for individual component
operation [9] to radical rethinking of system operations
[10–13]. In [11–13], the need for coordination between
transmission system operator (TSO) and distribution system operator (DSO) operation are discussed. Traditionally,
the system is kept secure by centralized control actions. For
example, the transmission system operator centrally controls few big power plants through a supervisory control
and data acquisition system. The distribution system
operator centrally manages the status of key devices, such
as breakers, reference setting points of on/off load tap
changers, capacity banks, etc. However, it is impossible to
control a large number of distributed energy resources
today [8], as the grid control systems are centralized by
design, and do not yet actively integrate distributed energy
resources into the operation on a meaningful scale.
The current development of smart grid technologies
allows DERs to adjust their operation through on-site local
monitoring and computing, and receive remote-control
signals from a market or grid operator using information
communication technology (ICT). It is likely that the
electrical power system will evolve into a hybrid system in
the next 20 years, with a set of primary generation, storage,
and transmission systems coordinated through the market,
and a set of distributed resources managed on a decentralized basis, using a mechanism that can leverage the
capabilities of DER systems [8]. The control and coordination of a large number of distributed energy resources
requires innovative distributed approaches. Transactive
control is such an approach.
Transactive control is a form of market-based control
that has been adopted by several projects and initiatives
[14, 15]. The intent of transactive control is to reach
equilibriums
by
standardizing
a
scalable,
distributed
mechanism via exchanging information about generation,
consumption,
constraints,
and
responsive assets over
dynamic, real-time forecasting periods, using economic
incentive signaling [16], and thus solving complex power
system problems. In another words, the operation is based
on the management of interactions instead of actions.
This paper reviews the recent development in transactive control application, and illustrates that as a framework
which can be applied generally to the operation of power
systems characterized by a high penetration of distributed
energy resources. By reviewing the existing demonstration
projects and literature, and presenting illustrative case
studies, the paper classiﬁes the implementing methods of
transactive control by way of information exchange
between the involved actors and the operational purpose.
Furthermore, the research challenges faced by the application of transactive control in future power systems are
discussed.
The remainder of the paper is organized as follows:
concepts and main methods of transactive control are
introduced in Section 2. Section 3 reviews the literature
that applies to the transactive control framework to manage
distributed energy resources. In Section 4, demonstration
projects are described. Section 5 presents two case studies
using the transactive control framework. Research challenges are discussed in Section 6. Finally, a discussion and
conclusion are given in Section 7.
2 Transactive control in smart grids
2.1 Basic concept
A transaction is an exchange of goods, services and/or
funds through negotiation. Accordingly, transactive control
is a framework that enables actors to interact with each
other through an economic signal, in order to optimize the
allocation of resources. In [14], transactive control is
deﬁned as an implementation of transactive energy.
Transactive Energy is ‘‘a set of economic and control
mechanisms that allows the dynamic balance of supply and
demand across the entire electrical infrastructure using
value as a key operational parameter’’ [14]. In a transactive
energy-management system, mid- to small-sized electricity-consuming or producing devices automatically negotiate their actions with each other, with devices in the
physical network, and with dispatch systems of energy
suppliers through efﬁcient and scalable electronic market algorithms [17].
In fact, transactive control is already in use in some
wholesale energy markets in the world, for instance the
Nord Pool Spot market [18]. The trading and clearing
mechanism used in the market is a typical form of transactive control. However, the application of transactive
control is still largely missing in distribution system
operation and at the retail market level.
In the transactive control framework, the utility function
applied in microeconomics is used, and describes the
degree of well-being the product provides for consumers. It
thus deﬁnes the different responses of different devices to
various prices [19]. As a framework, its application in
power systems can be classiﬁed into the following aspects,
which will be discussed further in Sections 3 and 4.
1)
Frequency regulation via tertiary control [20].
2)
Frequency control in power systems via secondary
control [19].
3)
Congestion and voltage management in distribution
network [7, 21–23].
4)
Manage the energy distribution inside an operation of
balance responsible parties (or aggregators) [24, 25].
452
Junjie HU et al.
123

---


### Page 3

5)
Distribution system operation in term of inﬂuencing
the behaviors of the decision-makers connected on the
network [26].
6)
New electricity spot market mechanism that facilitates
the participation of ﬂexible demand [27, 28].
7)
Residential optimal energy management considering
network operational constraints of utility [29–31].
2.2 Time scale
In transactive control, one of the main ideas is to integrate retail and wholesale markets, and other markets, into
a single platform, by utilizing forward and spot transactions, thereby guiding investment and operating decisions
[32]. Forward transaction is used to coordinate investment
decisions and manage risks. Spot transaction is used to
coordinate operating decisions and mitigate risk. The time
scale of these two type transactions is shown in Fig. 1.
Forward transactions are not new compared to the current
market mechanism. However, the spot could be real time,
or close to real time, e.g., 5 minutes. In the demonstration
projects described in Section 4, a 5-minute market is
widely used.
2.3 Implementing methods
In general, two types of implementing methods are
widely used in the literature, and in the demonstration
projects that will be introduced in Sections 3 and 4. The
implementing method is deﬁned as a way to ﬁnd the
equilibrium among the actors, and thus complete the
transactions. These two kinds of approaches include:
1)
A one-time information exchange-based method, such
as the merit-order-based market-clearing mechanism.
2)
An iterative information exchange-based method that,
mathematically, is normally explained by dual decomposition computing algorithms.
In the demonstration projects, the one-time information
exchange-based
method
is
widely
applied.
Each
participator generates a bid (a quantity and a price) for
every bid period (e.g., 5 minutes), and communicates with
the aggregating entity. Figure 2 shows an example of the
method to solve a grid congestion problem. Three steps are
included in the transactive control. Firstly, each device (or
device agent) bids their available ﬂexibility to the aggregating entity (system operator in this case). Then, the
system operator aggregates the bids and performs a pricediscovery mechanism; i.e., a merit-order-based marketclearing mechanism to ﬁnd the clearing price. The cleared
price is used to control the devices. We note that meritorder-based market-clearing mechanism is widely used to
ﬁnd the price, and to realize the transactions in the
demonstration projects.
Besides the one-time information exchange, an iterative
information exchange-based method is also widely proposed that normally exploits the algorithms of dual
decomposition [34, 35]. Note that in transactive control
framework, the dual variables are normally interpreted as
prices that reﬂect the equilibriums, while in many studies
they only serve as the coordinating signals [34, 35]. Figure 3 illustrates the scheme of the method. Examples are
given in the ﬁgure where the interaction between system
operator/aggregators and aggregators/DER units are presented. Note that the upper-level entity sends the price to
the lower-level entity; in correspondence, the lower level
responds with its power schedules. After certain iterations,
an agreement is reached between the upper-level entity and
the lower-level entity. In our view, the upper-level entity
decides when to stop based on its operational purpose.
Note
that
the
key
difference
between
these
two
approaches is the information exchange timing. The onetime information exchange-based method is less complex,
leading to lower communication requirements and higher
scalability.
The
iterative
information
exchange-based
method can present actors more opportunity to exchange
their operational conditions and willingness, but may need
more time to reach equilibriums. In practical applications,
the
iterative
information
exchange-based
method
is
expected to be useful in the scheduling phase, while the
one-time information exchange-based method is more
suitable of the real-time control phase.
3 Literature review regarding application
of transactive control in smart grids
This section overviews the studies that apply the transactive control framework for managing distributed energy
resources with different purposes in smart grids.
In [7], the transactive control method is applied to solve
distribution network grid congestion between the distribution system operator and the electric vehicle (EV) ﬂeet
Decade
Year
Day
Hour Minute Second
Millisecond
Carbon 
emission 
goals
Transmission 
and distribution 
planning
Day-ahead 
scheduling
Primary 
frequency 
control
Demand
response 
Automatic 
generation 
control signal 
Dynamic 
system 
response 
(stability)
Transactive energy 
Fig. 1 Transactive control’s position in electric power system
timelines when applying for system operation
Transactive control: a framework for operating power systems…
453
123

---


### Page 4

operators, who manage the charging of EVs centrally.
Firstly, the EV ﬂeet operators (FO) generate optimal
charging schedules, based on the energy spot price. However, the sum of the charging schedule of all the FOs may
bring operational challenges to the DSO, and thus it needs
to be modiﬁed. Then, a ﬂexibility cost function of FO is
formulated that reﬂects the charging power deviation from
the scheduled charging power in the form of a quadratic
function. The overall objective is to minimize the ﬂexibility cost function of EV FOs with respect to the grid
capacity constraints. The minimization is formulated as a
Lagrange problem, and solved iteratively using a decomposition algorithm. The Lagrange multipliers are interpreted as congestion price that coordinates the EV FO’s
charging proﬁles. Furthermore, the study is extended in
[21] to solve the voltage-band violations by introducing
congestion prices at the buses level.
In [22], Ipakchi pointed out that a higher penetration of
distributed energy resources will require greater attention
to distribution congestion issues, and a need for improved
distribution-automation
and
distribution-management
capabilities. A transactive control approach is proposed to
solve these problems. In the example described in the
paper, a plug-in electric vehicle requests 7.8 k Wh of
charging energy over the next two hours. This request can
be presented as a demand transaction and sent to a
demand-side management application operated by the
utility. Knowing the transaction delivery point to which
the car charger is connected, this application will check
the available capacity of the low-voltage distribution
transformer and feeders. Then it determines whether the
additional load will impact the circuit reliability and cause
any adverse phase imbalances. The demand-side management system will then schedule the charging for the
requested time period. At the same time, the management
system may receive many more charging requests that
have to be checked and coordinated with wholesale
scheduling at the substation supplying the feeders, to
ensure adequate supply. Each of these actions could be
modeled as a transaction among the consumers, the utility, and suppliers.
Besides the application of congestion and voltage
management [7, 21, 22] in the distribution system, a conceptual framework of using transactive control is proposed
in [26] that aims to optimally coordinate the operation of
self-interested individual decision-makers that emerge in
the distribution system. The optimal operation of the grid is
described according to a set of predeﬁned technical and
economic targets, and can be achieved by inﬂuencing the
behaviors of the decision-makers with appropriate market
signals. In the study, the authors argue that complex system
theory can be used to support the framework. In addition, a
Price-response device control
Customer price-flexibility curve
Load (k W)
Price ($/k Wh ) 
Price ($/k Wh )
Price ($/k Wh )
Load (k W)
Indoor 
temperature
Price
Bid
Tair
Max load
Base load 
Charge battery
Water heater
AC
Discharge battery
Price-discovery mechanism
Pclear
Pwholesale
Rated node capacity
Node supply curve
Demand curve
Tset
t
Fig. 2 Key aspects in one-time information exchange-based transactive control [33]
System operator/aggregators
Price
Power
Aggregators/DER units
Fig. 3 Scheme of iterative information exchange-based method
454
Junjie HU et al.
123

---


### Page 5

multi-agent model is built in the study to test the transactive control strategy.
Reference [36] formulated a class of ﬁnite horizon
dynamic game (or a transactive control system) to optimally control the charging proﬁle of a large number of
electric vehicles. Within the game, the control objective is
to minimize electricity-generation costs by establishing an
EV charging schedule that ﬁlls the overnight demand valley. Moreover, the paper established a sufﬁcient condition
under which the system converges to the unique Nash
equilibrium. In order to implement the transactive control
system, an iterative algorithm for computing the unique
Nash equilibrium is proposed, which includes four steps:
Step 1: The utility broadcasts the forecast of base
demand to all the EVs.
Step 2: Each of the EVs proposes an optimal charging
strategy that minimizes its charging cost, with respect to a
common aggregated EV demand broadcasted by the
utility.
Step 3: The utility collects all the optimal charging
strategies proposed by the individual EVs, and updates the
aggregated EV demand to all EVs.
Step 4: Repeat Step 2 and Step 3 until the optimal
strategies proposed by all EVs no longer change.
A similar study performed in [37] proved that a transactive
control-based
algorithm
converges
to
optimal
charging proﬁles, irrespective of the speciﬁcations of EVs,
even with asynchronous computation. Besides, the authors
also extended the algorithm to track a given load proﬁle
and to real-time implementation. Furthermore, in [38], the
study deals with more loads in a multiple residence setup.
The study ﬁnds the social-welfare maximization for energy
scheduling, between a utility company and residential
energy-users. The problem is solved by a distributed subgradient method that can be supported by an advanced
metering
infrastructure
(a
two-way
communication
network).
In addition to optimally managing the residential energy
of a utility [36–38], the study in [29] suggested a two-stage
residential energy-management method that considered
network operational constraints. In the ﬁrst stage, a dayahead pricing scheme and residential appliance scheduling
are determined through the interaction of the utility company and residential customers. In the second stage, prices
are updated based on the actual residential loads that draw
lessons from the locational marginal price (LMP) used in
the transmission system. In addition, in [30, 31], transactive control is used to coordinate the thermostatic loads
with the purpose of realizing efﬁcient energy allocation,
subject to peak energy constraint (feeder capacity constraints described in the study).
In [24], a scalable three-step approach for demand-side
management of EVs is presented. The three steps consist of
aggregation, optimization, and control. In the aggregation
step, individual EV charging constraints are aggregated
upwards. In the optimization step, the aggregated constraints are used for the scalable computation of a collective
charging
plan,
which
minimizes
costs
for
the
electricity supply. In the real-time control step, the objective to divide the optimal power generated in Step 2
between the individual EVs, is determined by a marketbased priority scheme. The work is further developed in
[25], where an event-driven dual coordination mechanism
is presented at the real-time control level. The simulation
result indicated that the number of messages exchanged
with the EVs was signiﬁcantly reduced, by at least 64%. In
[23], the transactive control framework is proposed to
manage the charging of electric vehicles, and incorporates
a distribution transformer and voltage constraints. A hierarchical multi-agent structure was used in the study, consisting of an auctioneer agent, substation agent, and EV
device agent. The substation agent summed up the bid
functions of all the underlying devices in a low-voltage
network, and in turn sent the bid function to a unique
auctioneer agent who deﬁned the equilibrium price. In
addition, the substation agent also ensured that the grid
constraints were not violated, given the possible equilibrium price.
In [19], the auction-based transactive control is applied
to control the cluster of loads with the purpose of providing
spinning reserves. Firstly, each device deﬁnes a utility
function for the utilization of the power ﬂexibility; e.g., the
corner price model developed in [24] is applied to calculate
the bid function of an EV. Then, in real-time operation, all
the device agents send their bids to a concentrator agent or
ﬂeet operator agent. The concentrator agent sums up the
bid functions of their zone, and then sends the aggregated
bid function to a unique auctioneer agent. Finally, the
auctioneer agent will deﬁne the equilibrium price as the
intersection of the aggregate bid functions and the supply
bid function. After the equilibrium price is deﬁned, it is
sent back to all of the devices agents, and the corresponding power of the device agents will be determined.
The market-clearing takes place every 15 minutes, or can
be made event-driven. Furthermore, the transactive control
method is extended to cooperate in frequency reserve
markets.
In [20], a hierarchical transactive control architecture
combines market transactions at the tertiary level with
inter-area and unit-level control at the primary and secondary level. The purpose of the hierarchical transactive
control is to ensure frequency regulating, using optimal
allocation of resources in the presence of uncertainties in
renewables and load. Models and controllers developed at
the tertiary level follow the standard market-clearing procedure that aims at social-welfare maximization. The
Transactive control: a framework for operating power systems…
455
123

---


### Page 6

problem is solved iteratively, and the global asymptotic
stability of the overall system is established.
In [27, 28], a novel day-ahead pool market mechanism is
proposed, to facilitate the participation of ﬂexible demand
in the electricity market. In the study, the market-clearing
optimization problem is, ﬁrstly, converted from a socialwelfare maximization problem to an equivalent generation
cost-minimization problem, and then solved indirectly by
its Lagrangian dual problem. The mathematical decomposition scheme is interpreted as a two-level iterative marketclearing mechanism, with the elements of lambda representing the 24-hour electricity price. The proposed market
mechanism is demonstrated with electric vehicles and heatpump systems.
In summary, a key operational parameter used in transactive control is value (i.e., cost/utility functions in
[7, 19, 21–25, 36, 37]). Thereafter the equilibrium price can
be discovered and the transaction can be executed. It is seen
that iterative information exchange is required to reach
equilibriums between the ﬂeet operator and electric vehicles
in [7, 21, 36, 37], while only one-time information exchange
is required in [19, 21–25] to reach the equilibrium. The
aforementioned studies are summarized in Table 1.
4 Demonstration projects in US and Europe
In this section, four demonstration projects are brieﬂy
introduced: the Grise Wise Olympic Peninsula project, the
Paciﬁc Northwest Demonstration project, and the GridSMART demonstration project from the USA; and the
Powermatching City project from Europe. The summary of
demonstration project using transactive control framework
is shown in Table 2.
Grid Wise Olympic Peninsula project [39]: The project
adopted transactive control to coordinate the power use of
residential
electric
water
heaters
and
thermostats,
commercial building-space conditioning, municipal water
pump loads, and several distributed generators, with the
purpose of reducing stress on local distribution networks.
The ﬁeld demonstration took place in Washington and
Oregon, and was paid for by the U.S. Department of
Energy and several northwest utilities. Real-time price at
5-minute intervals was found to be an effective control
signal for managing distribution congestion. Peak loads
were effectively reduced on the experimental feeder.
The Paciﬁc Northwest Demonstration project [40]: The
project expanded upon the experience of the previously
described Grid Wise Olympic Peninsula project. This project provided two-way communication between distributed
generation, storage, and demand assets, and the existing
gird infrastructure. The purpose was to use and test the
tranactive control signal. The signals communicated the
cost of delivering energy to a speciﬁc location. Using
automated controller, the devices such as water heaters,
electric furnaces etc. could make their own decision when
to use electricity.
Grid SMART demonstration project [41]: The project
aimed to design, build, and operate a transactive control
system, to engage residential consumers and their end-use
resources, to address the local-scale grid congestion. The
method has the advantage of providing greater efﬁciency
under normal operating conditions, and greater ﬂexibility
to react under situations of system stress. Three main
aspects were studied: the impact on system operations, and
on households, and observations about the sensitivity of
load to price changes.
Powermatching City [42]: Power Matching City is a
living lab environment based on state-of-the-art off-theshelf consumer products that have been altered to provide
ﬂexibility, and allow coordination with the smart grid [43].
The technology used in the project is Power Matcher [44]; a
‘demand response’ technology that balances all smart
devices, from low voltage to high voltage, in a virtual
Table 1 Summary of references using transactive control framework
References
Operational purpose
Implemention methods
[7, 21, 23]
Congestion and voltage management
Iterative information exchange based
[19]
Secondary frequency control
One-time information exchange based
[22]
Congestion management in distribution network
Not speciﬁed
[26]
Distribution system general operation
Iterative information exchange based
[36–38]
Residential optimal energy management of utility
Iterative information exchange based.
[29]
Residential optimal energy management of utility
considering network operational constraints
Iterative information exchange based
[30, 31]
Residential optimal energy management of utility
considering network operational constraints
One-time information exchange based
[24, 25]
Manage the power distribution of aggregator
One-time information exchange based
[20]
Tertiary frequency control
Iterative information exchange based
[27, 28]
New electricity spot market mechanism
Iterative information exchange based
456
Junjie HU et al.
123

---


### Page 7

market [15]. In the ﬁrst phase of the demonstration, Power Matching City consisted of 22 common Dutch households,
located
near
the
city
of
Groningen,
in
the
Netherlands. Later, this number was scaled up further. The
houses were ﬁtted with either a domestic combined heat
and power unit (micro-CHP) or a heat pump with a gasﬁred heater [45]. Some households also contained intelligent white-good appliances, and electric vehicles were
integrated as well. Outside the district, a 2.5 MW wind
turbine was available. The output power of the wind turbine could be scaled down digitally to match the consumption of the households. All devices were interfaced
with Power Matcher software, to operate Power Matching
City as a virtual power plant (VPP). It was concluded that
the VPP successfully followed its optimized energy proﬁle,
and provided the required regulatory power at the same
time [46].
5 Case studies
As the market adoption of DER reaches regional scale it
will create signiﬁcant issues in the management of the
distribution system related to existing planning and control.
This is likely to lead to problems for power quality and
reliability, since integrating distributed resources into
wholesale markets, without aligning distribution control
schemes, may create unacceptable consequences. Furthermore, as discussed in [10], as distributed energy resources
increase, the need to balance these resources across the
distribution system will likely give rise to the development
of a distribution system control tier, to complement the
bulk power system control tier.
Thus,inthisstudy,wepresenttworelevantcasestudiesthat
apply transactive control framework at the distribution system
level. The ﬁrst case gives a brief overview of the developed
work [7], where distribution congestions are solved by a
transactive control framework. In the second case, a transactive control is applied to manage the distribution system balance dynamically between supply and demand.
To apply the transactive control in both case studies, a
software agent (either an aggregator in Section 5.1 or a
local device agent in Section 5.2) will be present to represent the DER’s operational ﬂexibility. The agent will
form a cost function (Section 5.1) or a Walrasian demand
function (Section 5.2) to characterize the ﬂexibility. These
functions are bid into a virtual market where the equilibrium will be found among the agents. The conditions of the
equilibrium’s existence depend on the convexity of the cost
functions or the monotonicity of the demand functions.
More assumptions and conditions of applying transactive
control method are presented in Section 6.
5.1 Distribution grid congestion management
considering electric vehicle integration
In this case, we use electric vehicles as an example to be
integrated in the distribution system. Figure 4 shows that
the system consists of three actors: distribution system
operator, aggregators, and electric vehicle owners located
in a low-voltage network.
In this system, we assume aggregator manage the
charging schedule of electric vehicles centrally, with the
purpose of procuring the electricity from a spot market in a
low-price period, and fulling the energy requirements of
EV charging. However, if all the EVs are charged in the
low-price period, the aggregated power may introduce a
congestion problem into the distribution network. Thus,
transactive control will be used between the DSO and the
aggregator to coordinate the power schedules. In [7] and
[21], a ﬂexibility cost function that represents the cost of
the power preference difference of aggregators in each time
slot t is proposed as follows.
lk ¼ Ck;t ~Pk
Agg tð Þ  Pk
Agg tð Þ

2
ð1Þ
subject to
X
T
t¼1
~Pk
Agg tð Þnt ¼
X
T
t¼1
Pk
Agg tð Þnt
ð2Þ
Table 2 Summary of demonstration project using transactive control framework
Projects
Operational purpose
Implemention methods
Grid Wise Olympic Peninsula project
Congestion management
One-time information
exchange
The Paciﬁc Northwest Demonstration
project
Coordinate the operational decision of distributed energy
resources
One-time information
exchange
Grid SMART demonstration project
Congestion management
One-time information
exchange
Powermatching City
Manage the balance between supply and demand
One-time information
exchange
Transactive control: a framework for operating power systems…
457
123

---


### Page 8

where ~Pk
Agg is the control variable; Pk
Agg tð Þ is the preferred
schedule; Ck;t is the weighting factors that are associated
with the power difference; nt is the length of time slot t; k is
the index of the aggregator (Agg).
The objective is to minimize the cost of all the aggregators with respect to the power-transformer constraint
from the DSO.
min
X
NAgg
k¼1
X
T
t¼1
Ck;t ~Pk
Agg tð Þ  Pk
Agg tð Þ

2
ð3Þ
subject to
X
NAgg
k¼1
~Pk
Agg tð Þ  PMax
Tran tð Þ
ð4Þ
X
T
t¼1
~Pk
Agg tð Þnt ¼
X
T
t¼1
Pk
Agg tð Þnt
ð5Þ
where
PMax
Tran
is
the
power-transformer
capacity.
By
introducing Lagrange multipliers or shadow price kðtÞ,
and
considering
the
constraint
(5),
problem
(3)
is
transferred into a partial Lagrangian problem.
X
NAgg
k¼1
X
T
t¼1
Ck;t ~Pk
Agg tð Þ  Pk
Agg tð Þ

2
þ
X
nt
t¼1
ðtÞkðtÞ

X
NAgg
k¼1
~Pk
Agg tð Þ  PMax
Tran tð Þ
 
!
ð6Þ
Problem (6) can be broken down for each aggregator
given the kx tð Þ in each iteration. Thus each aggregator will
get a new optimal schedule denoted as Pk
Aggðt; kxðtÞÞ; and
the
Lagrange
multipliers
are
updated
according
to
kxþ1 tð Þ ¼ kx tð Þ þ ax
P
NAgg
k¼1
Pk
Agg t; kx tð Þ
ð
Þ  PMax
Tran tð Þ
 
!
until
the shadow price convergence. x is the index of the
negotiation step; ax is the stepsize and normally it is a
constant. The converged shadow price kxþ1 tð Þ is used as
the congestion price.
To illustrate the modeling method, we assume 72 households are connected to a power transformer, and the power
transformer allocates 200 k W to two EV aggregators. Each
aggregator (Agg 1 and Agg 2) has 36 EVs, which means a
100% penetration case. The scheduling period considered in
the study starts from 16:00 to 06:00 and a 15-minute interval
is used (56 time slots are deﬁned). The hourly predicted dayahead market price is assumed to be known by the aggregator. Each aggregator uses a linear programming method to
generate the aggregated power schedule. For the parameters
of the EVs used in generating charging schedule, the battery
capacity of each EV is set to 24 k Wh, the initial state of
charge of individual EV is set to 0.2 of the battery capacity,
and the maximum charging power is limited to 3.7 k W,
which ﬁts with the Danish case (16 A, 230 V connection).
With the values of these parameters, the aggregated power of
Agg 1 and Agg 2 is shown in Fig. 5.
We note that the aggregated power schedule during time
slots 45 to 48, i.e., 02:00 to 03:00, exceeds the allocated
capacity of the transformer. Therefore, the power schedule
at these four time slots needs to be modiﬁed by the method
Electricity 
spot market
Status information
Control/coordination 
relation
Physical connection
DSO operation
Interacting operation with 
spot market, DSO etc
EV charging schedule operation
EV user panel
Price reflecting 
grid constraints
Aggregator 
power schedule
Transactive
control 
Electric vehicle owner
External grid
Aggregator 
Distribution system 
operator
Fig. 4 Transactive control system for electric vehicle integration
458
Junjie HU et al.
123

---


### Page 9

described in this section. The weighting factor rates C1,t
and C2,t in (1) are set to 0.5 and 0.1. A constant stepsize
ax = 0.1 is chosen for the Lagrangian multiplier update.
With the values of the parameters, Figs. 6 and 7 show the
convergence of the price and the aggregators at time 02:00
to 03:00. As noted in Fig. 7, the sum of the power schedule
of Agg 1 and Agg 2 is 200 k W after the iterative information exchange. The simulation is performed within
MATLAB using CVX, a package for specifying and
solving convex programs [47].
5.2 System balance
In this section, the Power Matcher development is
described, to show the application of the transactive control
framework for system balance. Power Matcher has been
designed as a general-purpose coordination mechanism for
balancing demand and supply in large clusters of distributed generation, demand response, and electricity storage connected to the distribution grid, and is open-source
available. The open-source reference implementation of
Power Matcher is programmed in Java which makes it
deployable on a wide variety of processing platforms. The
local device control agent software makes use of OSGi,
which implements an open and modular Internet-of-Things
architecture for Java. This makes the Power Matcher software easily deployable and maintainable. Power Matcher
[43, 48, 49] has been shown to improve the match between
consumption and production by:  adding value to
renewable/distributed generation and demand-side ﬂexibility; ` improving the integration of renewable generation;
´
mitigating
congestion
(i.e.
local
network
overloading) in distribution networks. A comprehensive
treatment of this technology can be found in [50].
Power Matcher is based on multi-agent systems technology. Within a Power Match cluster, the agents are
organized into a logic tree. The leaves of this tree are a
number of local device agents. The root of the tree is
formed by the auctioneer agent, which handles the price
forming by searching for the equilibrium price. In order to
obtain scalability, concentrator agents can be added to the
structure as tree nodes. A local device agent is representative of a DER device. For a DER unit to be able to
participate in a Power Matcher cluster, its associated agent
must communicate its momentary bid curve or demand
function to the auctioneer agent. This function deﬁnes the
DER’s electricity demand d(p) for a given price p. An offer
to produce a certain amount of electricity against a certain
price is expressed by negative d(p) value. The core functionality of the auctioneer and the concentrator is to run the
electronic market, allocating the electrical power resource
to the local device agents. The electronic market solves this
allocation problem by ﬁnding the general equilibrium price
p* such that:
X
Na
a¼1
da p
ð
Þ ¼ 0
ð7Þ
Fig. 5 Aggregated power schedule of Agg 1 and Agg 2
Fig. 6 Convergence of shadow price
Fig. 7 Convergence of power schedule of Agg 1 and Agg 2
Transactive control: a framework for operating power systems…
459
123

---


### Page 10

where Na is the number of local device agents; da p
ð Þ is the
demand function of agent a that states the agent’s demand
or supply at a given price p.
A number of larger-scale demonstration projects have
been conducted successfully with the Power Matcher technology, to demonstrate its feasibility and potential. Here,
we zoom in on one of those, Couperus Smart Grid,
alongside the Power Matching City project described in
Section 4. The Couperus project demonstrated the ability
to perform tasks concurrently for system-wide balancing
and local distribution-level congestion management. In this
text we focus on the balancing aspect.
The Couperus Smart Grid project turned an apartment
block, with approx. Three hundred apartments and individual heat pumps for heating, into a Virtual Power Plant
using Power Matcher technology, performing both imbalance reduction and capacity management (peak shaving) in
the local LV-to-MV (low voltage to medium voltage)
substation. The operational ﬂexibility can be used to optimize the trading position of the energy supplier involved;
for example, by reducing the imbalance of a wind farm; i.e.
the difference between the day-ahead forecast and the
actual production. A more detailed description of the project’s outcomes can be found in [51], of which we give an
overview in this section.
Each of the apartments in the building is heated by a
heat pump with a nominal electrical power of 1 k W. The
systems are used for space heating and tap-water heating,
and are equipped with a heat-storage tank. The inlet water
for all heat pumps comes from a groundwater heat
exchanger (aquifer) providing a low inlet temperature,
leading to a high energy efﬁciency of the heating
process.
The balancing functionality of the VPP is performed by
the so-called Imbalance Agent. In the case of this project,
this software agent used the ﬂexibility of the heat pumps to
reduce the imbalance of the wind turbine farm. The realtime imbalance of the wind farm was used as an input for
this agent. During this part of the test, 150 heat pumps were
connected to the VPP. As each heat pump has a nominal
power of 1 k W, and a low duty cycle (i.e. the heat pumps
operate with relatively long off times), the power deviations requested from the VPP were chosen in the range of
±10 k W. From the energy supplier in the project, the
imbalance signal of a nearby wind turbine was fed into the
system, scaled to this response range. The imbalance signal
was the difference between the day-ahead forecasted wind
generation and the actual generation.
To reduce the wind power imbalance, the imbalance
agent bids the imbalance signal into the electronic market.
In case of a surplus of wind power, the price on the electronic market to go down, resulting in a number of heat
pumps to switch on to consume the surplus. Similarly, in
case of underproduction, the price will rise and electricity
demand from the heat pumps will fall.
Figure 8 shows the relation between the requested and
realized imbalance reduction, as delivered by the VPP over
two weeks in the winter. On almost all occasions, the
compensation requested can be fulﬁlled quantitatively:
both signals are highly correlated (correlation equals 0.90)
with a slope equal to 1. The response accuracy in the ﬁgure is 94.6%, indicating that the Power Matcher performs
well coordinating among the heat pumps to compensate the
unexpected under- or overproduction of the wind turbine.
Note that during the winter the heat pumps have the highest
running time, providing heat to the apartments, which
limits their response. Thus, these results can be seen as a
worse-case category performance.
6 Research challenges
Compared to conventional power systems operation, one
of the important advantages of transactive control is the
incorporation of DER users’ priorities/ needs/ utilities/ costs
into the operation of the power systems. Thus the entire
system can achieve an optimum balance necessary to meet
objectives and constraints. Therefore, it is important to
investigate the price-response behavior of DERs and to
design the optimal pricing strategy. Next to these two challenges, another issue is how to create and operate a market
where efﬁciency and transparency are guaranteed. On the
method front, how to ensure the convergence of the transactive control application, and increase the speed of the
convergences, are also important issues. In addition, the
requirements of the ICT infrastructure for communication
Fig. 8 Relation between requested and realized imbalance reduction
over two winter weeks [51]
460
Junjie HU et al.
123

---


### Page 11

among various stakeholders are another important challenge. Last but not least, the standardization of interface of
transactive energy is essential for successful implementation. Besides these general challenges, speciﬁcally, regarding application of transactive control in solving network
problems, more studies are needed on how to calculate the
base line, and how to use the ‘shadow price’ in practice.
6.1 Price-response behavior of DERs
In a transactive control framework, it is necessary for
the DER owner to be price sensitive, and able to actively
respond to the price informed by the system operator.
However, it is a challenge to model the price-response
behavior of customers properly. Both [52] and [53]
describe how, if most of the buildings in a distribution
circuit have an energy-management system that turns up
the air-conditioning or the heating when electricity prices
drop below a threshold, then the distribution circuit, and
indeed the entire grid, can be destabilized, due to the
ampliﬁed spikes. To understand the price-response behavior of customers, methods including a conditional logit
model [54] and a parametric stochastic process [55] are
presented in the literature. Nevertheless, it is noted in
[54, 55], the extent to which a properly designed price
signal could assist in maintaining that grid reliability will
remain open until the DER owner’s price responsiveness is
tested empirically through experiments.
6.2 Pricing strategy design and convergence issue
As discussed in [52], a simple price strategy may
destabilize the power system operation. In contrast to
conventional power system operation, in the near future,
more distributed energy resources integrated into operation
requires additional research on the convergence of dynamic
pricing. In real-time operation, new market mechanisms
are needed to create effective interactions that are closely
linked to the distribution control systems and DERs, to
ensure the security and efﬁciency of the system, as well as
the optimality of the DER operation. Regarding the convergence of the iterative-based method under the circumstance of transactive control, [29] and [38] discuss that, in
general, the convergence can be obtained by following
certain stepsize rules. In addition, as described in [38], the
algorithms
ﬁnd
near-optimal
schedules,
even
when
advanced metering infrastructures (AMI) messages (updated prices and residential load) are lost, which can happen in the presence of malfunctions, or noise in the
communication network. However, much research is needed to increase the convergence speed, since high iteration
numbers are seen in many studies, and these imply more
time is needed for convergence.
6.3 Market place design
To ensure enough competition and fairness in the
capacity market, one prerequisite is the number of market
participants; e.g., FOs in Section 5.1. If there are few FOs
in the distribution area, and issue such as market power
will become a major challenge from the market perspective. Thus how to deﬁne the market rules that can create
enough competition and fairness will be a big challenge in
transactive control application.
It is worth mentioning that the application of transactive
control does not call for a central market. A centralized
marketplace can potentially bring too many participants,
considering DERs’ direct participation, into one platform,
which brings challenges both for market design and for
operation. The creation of distributed marketplaces may be
a reasonable approach to involve more DERs into the
current operation. The distributed marketplaces could
possibly following the existing geographical distribution
areas.
6.4 Requirements for ICT infrastructure
In addition to conventional stakeholders, the new
stakeholders in smart grid will probably include aggregators and prosumers. Thus communication will be an
important issue, since a large population of stakeholders
needs to be connected. For example, in the case presented
in Section 5.1, FOs need to communicate well with EVs, in
order to make an optimal charging schedule, and this
information includes driving pattern, state of charge, and
some other preferences of EV owners. The time-constraint
is not an essential issue in the scheduling problem,
although FOs need real-time information exchange to
ensure the schedule is properly executed. For the interaction between FOs and the distribution grid capacity market
operator, real-time communication is a challenge, but a
reasonable time range can be established, as well as trying
to limit the market iteration with certain rules. This kind of
setup will require an advanced ICT infrastructure that is
becoming affordable.
Furthermore, as discussed in [45], an ICT delay during
market-clearing can introduce an instability issue into the
power system. It is noted in the paper that there is a
counterintuitive relationship between the market-clearing
time and the price-signal delay: when the market-clearing
time is relatively long, delaying the price signal can
improve the market’s stability, while reducing the communication delay can destabilize the market. This counterintuitive effect shows that the full impact of information
technology on power markets can be signiﬁcant and difﬁcult to anticipate. Therefore, as markets are incorporated
into transactive control applications, careful attention
Transactive control: a framework for operating power systems…
461
123

---


### Page 12

should be paid to the effects of information technology on
the market’s dynamic behavior.
6.5 Standardization of interface of transactive
energy
The envisioned standardized interfaces include two
aspects:  an interface for all the actors participating in the
transactive energy market, which will deﬁne the bid forms;
e.g., according to the market structure, market operating
mechanism; ` an interface with DERs; i.e., the information sent by the market operator should be understood by
the DERs, and thus the DERs can respond to the signal. To
build a standardized platform that accelerates the development of transactive energy, several initiatives have been
seen in the ﬁeld, including: USEF (universal smart energy
framework [56]); open ADR (open automated demand
response) alliance [57]; and EF-PI (Energy Flexibility
Platform and Interface) white paper [58].
6.6 Baseline issue
The baseline is normally deﬁned as an estimate of the
electricity that would have been consumed by a customer
in the absence of a demand-response event [59, 60]. For
example, in the ﬁrst case study, the transactive control
method enables the demand response. The aggregator that
optimally generates the energy schedule is an operation in
the absence of a demand-response event. Thus, the optimized energy schedule of the aggregators will be used as a
baseline in the transactive control method, to prevent grid
constraint violation. However, aggregators may not make
the energy schedule optimal. Instead, they can procure the
electricity based on the customer’s power usage pattern.
Under this circumstance, the customer’s normal daily
proﬁles will be used as a baseline. Nevertheless, more
research is needed to characterize the baseline, since it will
be very important in the settlement stage.
7 Conclusions
In
summary,
from
a
demand
response-enabling
approach to a power system operational principle, the
transactive control framework has shown its distinctive
capability to incorporate DER users’ priorities, needs, or
costs that accommodate the high penetration of distributed
energy resources smoothly into future power systems.
The implementation methods of transactive control
include a one-time information exchange-based approach,
and an iterative information exchange-based method.
These two methods have been used widely in the literature
and demonstration projects. Note that, for a hierarchical
transactive control system, it is possible to combine both
implementation methods, such as using the one-time
information method on lower levels, and having an iterative information exchange method in the upper levels.
Finally, there is also a need for policymakers to better
understand the relationship between pricing schemes and
control systems, as it relates to distributed energy resources
to ensure proper market structures and rules, to maintain a
highly reliable and clean energy system.
The current development trend is to integrate all the
energy networks together, to hedge against the intermittency brought about by the increasing penetration of
renewable energy. The ultimate goal of this development
would be a so-called ‘‘Energy Internet’’, where energy can
be polled and sent from anyone, anywhere, at any time.
The operation of such a system would involve more participants from different energy networks than the ones seen
today. The incentives for participation would be from some
designed market mechanisms and eventually, the system
operation would be based on handling various energy
offers and requests from all the participants. In the operation, all the participants, including the grid operators, will
come with their own objectives, as well as constraints, for
participation. The problem will become highly complex,
including concerns from both economic and technical
aspects. Such situations may be suitable for the application
of transactive control principles.
Acknowledgement The authors thank Pamela Macdougall of TNO,
The Netherlands for her valuable comments on the draft of this
article. Koen Kok’s contribution to the writing of this article was
ﬁnanced by the TNO Early Research Program on Energy Storage and
Conversion (ERP ECS) through the SOSENS project. This work is
partly supported by the Danish i Power project (http://www.ipowernet.
dk/) funded by the Danish Agency for Research and Innovation (No.
0603-00435B).
Open Access
This article is distributed under the terms of the
Creative Commons Attribution 4.0 International License (http://
creativecommons.org/licenses/by/4.0/), which permits unrestricted
use, distribution, and reproduction in any medium, provided you give
appropriate credit to the original author(s) and the source, provide a
link to the Creative Commons license, and indicate if changes were
made.
References
[1] Medium-term renewable energy market report 2015: market
analysis and forecasts to 2020. International Energy Agency
(IEA), Paris, 2015
[2] Pineda I, Wilkes J (2015) Wind in power: 2014 European
statistics. The European Wind Energy Association (EWEA),
Brussels
[3] Ge SY, Xu L, Liu H et al (2015) Low-carbon beneﬁt analysis on
DG penetration distribution system. J Mod Power Syst Clean
Energy 3(1):139–148. doi:10.1007/s40565-015-0097-z
462
Junjie HU et al.
123

---


### Page 13

[4] Coster EJ, Myrzik JMA, Kruimer B et al (2011) Integration
issues of distributed generation in distribution grids. PIEEE
99(1):28–39
[5] Pepermans G, Driesen J, Haeseldonckx D et al (2005) Distributed generation: deﬁnition, beneﬁts and issues. Energy Policy 33(6):787–798
[6] Ela E, Milligan M, Kirby B (2011) Operating reserves and
variable generation. NREL/TP-5500-51978. National Renewable Energy Laboratory (NREL), Golden
[7] Hu JJ, You S, Lind M et al (2014) Coordinated charging of
electric vehicle for congestion prevention in the distribution
grid. IEEE Trans Smart Grid 5(2):703–711
[8] De Martini P, Chandy KM, Fromer NA (2012) Grid 2020:
towards a policy of renewable and distributed energy resources. Resnick Institute, California Institute of Technology,
Pasadena
[9] Juamperez M, Yang G, Kjær SB (2014) Voltage regulation in
LV grids by coordinated volt-var control strategies. J Mod
Power Syst Clean Energy 2(4):319–328. doi:10.1007/s40565014-0072-0
[10] Hanninen S (2015) Detailed requirements and constraints for the
control of ﬂexibility. European FP 7 project ELECTRA (European Liaison on electricity committed towards long-term
research activities for smart grids), ENGIE Lab Laborelec,
Linkebeek
[11] Hansen H, Holm-Hansen HH, Samuelsson O, et al (2013)
Coordination of system needs and provision of services. In:
Proceedings of the 22nd international conference and exhibition
on electricity distribution (CIRED’13), Stockholm, 10–13 June
2013, 4 pp
[12] Ding Y, Hansen LH, Cajar PD et al (2013) Development of a
DSO-market on ﬂexibility services. i Power WP3.8. i Power
Consortium, Copenhagen
[13] Zegers AA, Brunner H (2014) TSO-DSO interaction: an overview of current interaction between transmission and distribution system operators and an assessment of their cooperation in
smart grids. International Smart Grid Action Network (ISAGN)
Discussion Paper Annex 6 Power T&D Systems, Task 5.
ISAGN, Paris
[14] Grid Wise transactive energy framework, Version 1.0. PNNL22946 Ver1.0. The Grid Wise Architecture Council, Richland,
2015
[15] Kok K, Warmer CJ, Kamphuis IG (2005) Power Matcher: multiagent control in the electricity infrastructure. In: Proceedings
of the 4th international joint conference on autonomous agents
and multiagent systems (AAMAS’05), Utrecht, 25–29 July
2005, pp 75–82
[16] Hammerstrom D, Oliver T, Melton R et al (2009) Standardization of a hierarchical transactive control system. In: Proceedings
of the grid-interop conference, Denver, 17–19 Nov 2009,
pp 35–41
[17] Kok K, Widergren S (2016) A society of devices: integrating
intelligent distributed resources with transactive energy. IEEE
Power Energy Mag 14(3):34–45
[18] Nord Pool. http://www.nordpoolspot.com/About-us/
[19] Weckx S, D’Hulst R, Driesen J (2015) Primary and secondary
frequency support by a multi-agent demand control system.
IEEE Trans Power Syst 30(3):1394–1404
[20] Bejestani AK, Annaswamy A, Samad T (2014) A hierarchical
transactive control architecture for renewables integration in
smart grids: analytical modeling and stability. IEEE Trans Smart
Grid 5(4):2054–2065
[21] Hu JJ, Yang GY, Bindner HW (2015) Network constrained
transactive control for electric vehicles integration. In: Proceedings of the 2015 IEEE Power and Energy Society general
meeting, Denver, 26–30 July 2015, 5 pp
[22] Ipakchi A (2011) Demand side and distributed resource management—a transactive solution. In: Proceedings of the 2011
IEEE Power and Energy Society general meeting, San Diego,
24–29 July 2011, 8 pp
[23] Weckx S, D’Hulst R, Claessens B et al (2014) Multiagent
charging of electric vehicles respecting distribution transformer
loading
and
voltage
limits.
IEEE
Trans
Smart
Grid
5(6):2857–2867
[24] Vandael S, Claessens B, Hommelberg M et al (2013) A scalable
three-step approach for demand side management of plug-in
hybrid vehicles. IEEE Trans Smart Grid 4(2):720–728
[25] De Craemer K, Vandael S, Claessens B et al (2014) An eventdriven dual coordination mechanism for demand side management of PHEVs. IEEE Trans Smart Grid 5(2):751–760
[26] Bompard EF, Han B (2013) Market-based control in emerging
distribution
system
operation.
IEEE
Trans
Power
Deliv
28(4):2373–2382
[27] Papadaskalopoulos D, Strbac G, Mancarella P et al (2013)
Decentralized participation of ﬂexible demand in electricity
markets—part I: market mechanism. IEEE Trans Power Syst
28(4):3658–3666
[28] Papadaskalopoulos D, Strbac G, Mancarella P et al (2013)
Decentralized participation of ﬂexible demand in electricity
markets—part II: application with electric vehicles and heat
pump systems. IEEE Trans Power Syst 28(4):3667–3674
[29] Moradzadeh B, Tomsovic K (2013) Two-stage residential
energy management considering network operational constraints. IEEE Trans Smart Grid 4(4):2339–2346
[30] Li S, Zhang W, Lian JM et al (2016) Market-based coordination
of thermostatically controlled loads—part I: a mechanism. IEEE
Trans Power Syst 31(2):1170–1178
[31] Li S, Zhang W, Lian JM et al (2016) Market-based coordination
of thermostatically controlled loads—part II: unknown parameters. IEEE Trans Power Syst 31(2):1179–1187
[32] Barrager S, Cazalet E (2014) Transactive energy: a sustainable
business and regulatory model for electricity. Baker Street
Publishing, San Francisco
[33] Hu JJ (2014) Control strategies for power distribution networks
with electric vehicle integration. Ph.D. Thesis. Technical
University of Denmark, Copenhagen
[34] Disfani VR, Fan LL, Piyasinghe L et al (2014) Multi-agent
control of community and utility using Lagrangian relaxation
based dual decomposition. Electr Power Syst Res 110:45–54
[35] Kraning M, Chu E, Lavaei J et al (2013) Dynamic network
energy management via proximal message passing. Found Trend
Optim 1(2):70–122
[36] Ma ZL, Callaway DS, Hiskens IA (2013) Decentralized charging control of large populations of plug-in electric vehicles.
IEEE Trans Control Syst Technol 21(1):67–78
[37] Gan L, Topcu U, Low SH (2013) Optimal decentralized protocol
for
electric
vehicle
charging.
IEEE
Trans
Power
Syst
28(2):940–951
[38] Gatsis N, Giannakis GB (2012) Residential load control: distributed scheduling and convergence with lost AMI messages.
IEEE Trans Smart Grid 3(2):770–786
[39] Katipamula S, Chassin DP, Hatley DD, et al (2006) Transactive
controls: market-based Grid Wise TM controls for building systems. PNNL-15921. Paciﬁc Northwest National Laboratory,
Richland
[40] Paciﬁc Northwest Smart Grid Demonstration Project. http://
www.pnwsmartgrid.org/
[41] Widergren S, Subbarao K, Fuller J et al (2014) AEP Ohio
grid SMART demonstration project real-time pricing demonstration analysis. PNNL-23192. Paciﬁc Northwest National
Laboratory, Richland
[42] Power Matching City. http://www.powermatchingcity.nl
Transactive control: a framework for operating power systems…
463
123

---


### Page 14

[43] Kok K, Roossien B, Mac Dougall P et al (2012) Dynamic pricing
by scalable energy management systems: ﬁeld experiences and
simulation results using Power Matcher. In: Proceedings of the
2012 IEEE Power and Energy Society general meeting, San
Diego, 22–26 July 2012, 8 pp
[44] The suite. Power Matching Suite. http://ﬂexiblepower.github.io/
technology/powermatcher/
[45] Roossien B, Mac Dougall PA, Van den Noort A (2010) Intelligent heating systems in households for smart grid applications.
In: Proceedings of the 2nd international conference on innovation for sustainable production (I-SUP’10), Bruges, 18–21 April
2010
[46] Roossien B, Van den Noort A, Kamphuis R, et al (2011)
Balancing wind power ﬂuctuations with a domestic virtual
power plant in Europe’s ﬁrst smart grid. In: Proceedings of the
2011 IEEE Trondheim Power Tech conference, Trondheim,
19–23 June 2011, 5 pp
[47] Grant M, Boyd SP (2013) CVX: MATLAB software for disciplined convex programming, version 2.0 beta. CVX Research
Inc
[48] Warmer CJ, Hommelberg MPF, Roossien B et al (2007) A ﬁeld
test using agents for coordination of residential micro-chp. In:
Proceedings of the 2007 international conference on intelligent
systems applications to power systems (ISAP’07), Niigata, 5–8
Nov 2007, 4 pp
[49] Roossien B (2009) Field-test upscaling of multi-agent coordination in the electricity grid. In: Proceedings of the 20th international conference and exhibition on electricity distribution
(CIRED’09), Part 1, Prague, 8–11 June 2009, 4 pp
[50] Kok K (2013) The Power Matcher: smart coordination for the
smart electricity grid. Ph.D. Thesis. Amsterdam Vrije Universiteit, Amsterdam
[51] Van Pruissen O, Kok K, Eisma A (2015) Simultaneous imbalance reduction and peak shaving using a ﬁeld operational virtual
power plant with heat pumps. In: Proceedings of the 23rd
international conference on electricity distribution, Lyon, 15–18
June 2005, 5 pp
[52] Pentland A (2015) Simple market models fail the test. Nature
525(7568):190–191
[53] Krause SM, Bo¨rries S, Bornholdt S (2013) Econophysics of
adaptive power markets: when a market does not dampen ﬂuctuations but ampliﬁes them. Phys Rev E 92(1):5
[54] Faruqui A, Hledik RM, Levy A et al (2011) Will smart prices
induce smart charging of electric vehicles? Social Science
Research Network (SSRN), 25 Aug 2011
[55] Yu RS, Yang WX, Rahardja S (2012) A statistical demand-price
model with its application in optimal real-time price. IEEE
Trans Smart Grid 3(4):1734–1742
[56] Universal Smart Energy Framework (USEF). http://www.usef.
info
[57] Open ADR. http://www.openadr.org/
[58] Energy ﬂexibility platform & interface. Power Matching Suite.
http://ﬂexiblepower.github.io/EF-Pi%20Whitepaper/
[59] Chao HP (2011) Demand response in wholesale electricity
markets: the choice of customer baseline. J Regul Econ
39(1):68–88
[60] The demand response baseline (2009) White Paper. Ener NOC
Inc, Boston
Junjie HU received the M.Sc. degree in Control Theory and Control
Engineering from Tong Ji University, China in 2010 and the Ph.D
degree in Electrical Engineering from Technical University of
Denmark, Denmark in 2014. Currently, he is a Postdoctoral
researcher with the Department of Electrical Engineering, Technical
University of Denmark. His main ﬁelds of interests are distributed
energy resources (DERs) integration with focus on electric vehicles,
application of optimal control theory on active distribution grid
operation and management, and DER’s optimal participation into the
ancillary service market.
Guangya YANG received the B.Sc., M.Sc. and Ph.D in 2002, 2005
and 2008 respectively, all in electric power system ﬁeld. Currently, he
is associate professor with the Center for Electric Power and Energy,
Department of Electrical Engineering of the Technical University of
Denmark. His ﬁelds of interest include power system operation and
control, renewable energy integration and wide-area system monitoring and protection.
Koen KOK is a scientiﬁc researcher in the interdisciplinary ﬁeld of
intelligent electricity systems, combining electrical engineering and
control engineering with computational intelligence. Currently, he is a
Senior Scientist at the Center for Electric Power and Energy,
Technical University of Denmark. Further, he is afﬁliated with TNO,
the largest applied research institute in The Netherlands, where he is a
senior scientist as well. He holds a B.Sc. in Electrical Engineering and
an M.Sc. and a Ph.D in Computer Science. He has extensive research
experience in the ﬁelds of market-based control of power systems,
smart grid ICT architectures and integration of distributed energy
resources and demand response in the electricity system. He is one of
the inventors of the Power Matcher, an award winning and opensource smart grid technology for matching demand and distributed
generation on one hand with available renewable power and network
capacity on the other.
Yusheng XUE received the M.Sc. degree in Electrical Engineering
from EPRI, China in 1981 and the Ph.D degree from the University of
Liege, Belgium in 1987. He has been an Academician of the Chinese
Academy of Engineering since 1995. He is now the Honorary
President of State Grid Electric Power Research Institute (SGEPRI or
NARI), China, Adjunct Professor in dozens of Chinese universities
and an Adjunct Professor of the University of Newcastle in Australia.
He is the Editor-in-Chief of Automation of Electric Power System (in
Chinese) and Journal of Modern Power Systems and Clean Energy (in
English), as well as Chairman of the Technical Committee of Chinese
National Committee of CIGRE since 2005.
Henrik W. BINDNER received the M.S. degree in electrical
engineering from the Technical University of Denmark, Lyngby,
Denmark, in 1988. Since 1990, he has been with the Risø National
Laboratory for Sustainable Energy, Roskilde, Denmark, in the Wind
Energy Division. Since 2008, he has been a Senior Scientist with the
Department for Electrical Engineering at the Risø Campus, Technical
University of Denmark. He has mainly been working on integration of
wind energy into power systems, as well as analysis, design, and
control of small island systems.
464
Junjie HU et al.
123

---
