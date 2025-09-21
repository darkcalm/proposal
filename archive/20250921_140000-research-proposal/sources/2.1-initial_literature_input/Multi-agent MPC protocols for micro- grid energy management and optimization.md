

---

Page 1

---

Multi-agent MPC protocols for micro-
grid energy management and optimization
Multiagentní MPC protokoly pro energetickou optimalizaci mikrosítě
Pavel Elis
Master Thesis
T.I.M.E. Double Degree
The present work was submitted to
RWTH Aachen University
Faculty of Electrical Engineering and Information Technology
Institute for Automation of Complex Power Systems
Univ.-Prof. Antonello Monti, Ph. D.
and to
CTU in Prague
Faculty of Electrical Engineering
Department of Control Engineering
Supervisor: M. Sc. Gonca Gürses-Tran (’)
Kristian Hengster-Movric, Ph.D. (*)
(’) Institute for Automation of Complex Power Systems, RWTH Aachen
(*) Department of Control Engineering, CTU in Prague, FEE
December 2019


---

Page 2

---



---

Page 3

---



---

Page 4

---



---

Page 5

---

Declaration
I declare that the presented work was developed independently and that I have listed
all sources of information used within it in accordance with the methodical instruc-
tions for observing the ethical principles in the preparation of university theses.
Place, Date
Signature
Prohlášení autora práce
Prohlašuji, že jsem předloženou práci vypracoval samostatně a že jsem uvedl veškeré
použité informační zdroje v souladu s Metodickým pokynem o dodržování etických
principů při přípravě vysokoškolských závěrečných prací.
Místo, Datum
Podpis
Acknowledgement
I would like to express my appreciation to both of my supervisors, Kristian Hengster-
Movric, Ph.D. and M.Sc. Gonca Gürses-Tran, for their guidance and valuable advice
during the whole process of my master thesis. Moreover, I would like to thank my
parents for their mental and financial support during my studies abroad.


---

Page 6

---



---

Page 7

---

Abstract
One of the challenges of microgrids under the influence of high shares of intermittent
renewable energy sources (RES) is an effective and reliable control. Model predictive
control (MPC) is a promising approach to solve this problem for a specified time
horizon since it allows integrating of a cost-minimizing objective function and system
boundaries while taking power demand and supply into account.
An agent-based MPC scheme was developed as a two-level architecture based
on multi-agent control system (MAS) consensus algorithm providing power balance
in the microgrid and centralized MPC that is aspiring to streamline the control
processes to reach the targeted objectives.
During the examination of the simulated results, the expected correlation of the
result properties and control parameters was found.
Additionally, the situations
with the highest improvement ratio in comparison with the results of the reference
control architecture were discovered and analysed.
Based on the results, a significant cost reduction can be seen in most of the
tested datasets that were measured on a real-life microgrid solution. Therefore, the
implementation of the suggested control can prove to be appropriate and beneficial
for microgrid operators and grid customers.
Keywords: Power system, Microgrid, Multi-agent control, MPC, Consensus
vii


---

Page 8

---



---

Page 9

---

Abstrakt
Navržení efektivního a spolehlivého řízení mikrosítí s vysokým podílem energie z ob-
novitelných zdrojů, je jednou z výzev při jejich nasazení. Prediktivní řízení (MPC)
systému je slibný přístup, jak vyřešit tento problém v určitém časovém horizontu.
Tento přístup umožňuje integraci řízení na základě minimalizace funkce, která dává
do souvislosti různé druhy nákladů a omezení systému, ve vazbě na výrobu a spo-
třebu energie.
Navržené multiagentní MPC řízení bylo vyvinuto jako dvoustupňová architektura,
založená na konsensuálním algoritmu více agentů, který zajišťuje výkonovou rovno-
váhu v mikrosíti a centralizovaném MPC, který zefektivňuje řízené procesy tak, aby
dosáhly vytyčených cílů.
Při zkoumání navržených simulací byla ověřena předpokládaná korelace získaných
výsledků a řídicích parametrů. Dále byla identifikována a analyzována situace s
nejvyšším zlepšením ve srovnání s výsledky referenční řídící architektury.
Na základě výsledků testů řídicího protokolu na testovaných datech, které byly
měřeny v reálné mikrosíti, je vidět možnost významného snížení nákladů na provoz
mikrosítě. Navrhované řešení tedy ukazuje vhodnost jeho implementace a přínos,
jak pro provozovatele mikrosítí, tak pro zákazníky distribuční soustavy.
Klíčová slova: Energetický systém, Mikrosíť, Multiagentní řízení, MPC, Konsen-
sus
ix


---

Page 10

---



---

Page 11

---

Contents
Acronyms
1
1
Introduction
3
2
Microgrid Control Concepts
5
2.1
The Microgrid
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
2.1.1
Microgrids components
. . . . . . . . . . . . . . . . . . . . .
8
2.1.2
Microgrids types . . . . . . . . . . . . . . . . . . . . . . . . .
11
2.1.3
Demand side management . . . . . . . . . . . . . . . . . . . .
12
2.2
Typical microgrid controllers
. . . . . . . . . . . . . . . . . . . . . .
15
2.2.1
Decentralised control architecture . . . . . . . . . . . . . . . .
16
2.2.2
Centralised control architecture . . . . . . . . . . . . . . . . .
19
2.2.3
Distributed multi-agent control architecture . . . . . . . . . .
20
2.3
The Concept of model predictive control . . . . . . . . . . . . . . . .
23
2.3.1
MPC formulation . . . . . . . . . . . . . . . . . . . . . . . . .
25
2.3.2
MPC solution . . . . . . . . . . . . . . . . . . . . . . . . . . .
26
3
Use Case
31
3.1
Demonstration site Simris . . . . . . . . . . . . . . . . . . . . . . . .
31
3.1.1
Simris components . . . . . . . . . . . . . . . . . . . . . . . .
31
3.2
Measured data
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
32
3.3
Other used data
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
34
3.4
Reference control algorithm . . . . . . . . . . . . . . . . . . . . . . .
34
4
Modelling the Controller
37
4.1
Control structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
38
4.2
Distributed MAS control . . . . . . . . . . . . . . . . . . . . . . . . .
40
4.2.1
Weighted adjacency matrix . . . . . . . . . . . . . . . . . . .
40
4.2.2
Multi-agent system control constraints . . . . . . . . . . . . .
41
4.2.3
Update rules
. . . . . . . . . . . . . . . . . . . . . . . . . . .
42
4.2.4
Algorithm implementation . . . . . . . . . . . . . . . . . . . .
43
4.3
Model predictive control . . . . . . . . . . . . . . . . . . . . . . . . .
46
4.3.1
Designed model . . . . . . . . . . . . . . . . . . . . . . . . . .
47
4.3.2
Data forecast . . . . . . . . . . . . . . . . . . . . . . . . . . .
48
4.3.3
Cost function . . . . . . . . . . . . . . . . . . . . . . . . . . .
51
4.3.4
Prediction constraints . . . . . . . . . . . . . . . . . . . . . .
51
xi


---

Page 12

---

Contents
5
Exemplary Results
53
5.1
Evaluation metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . .
53
5.1.1
Economical metrics . . . . . . . . . . . . . . . . . . . . . . . .
53
5.1.2
Power exchange metrics . . . . . . . . . . . . . . . . . . . . .
54
5.1.3
Battery energy storage system (BESS) metrics
. . . . . . . .
54
5.2
Simulation results
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
54
5.2.1
Control parameters settings . . . . . . . . . . . . . . . . . . .
55
5.2.2
Simulation of complete data . . . . . . . . . . . . . . . . . . .
60
6
Conclusion
63
Bibliography
65
List of Figures
71
List of Tables
73
A Content of the attached CD
77
xii


---

Page 13

---

Acronyms
CO2 Carbon Dioxide 5, 9, 10
A/C Air-condition 13
AC Alternating Current 7, 9, 11, 15, 17, 31
BESS Battery Energy Storage System xii, 8, 10, 11, 14, 18, 19, 31, 34, 35, 37–40,
42, 44, 46–48, 51–61, 63, 64, 71, 73
BUG Back-up Generator 9, 10, 31, 34, 38, 42–44, 48
CCHP Combined Cooling, Heating And Power System 14, 15
CCVSI Current-controlled Voltage Source Inverters 17, 18
CT Current Transformer 8
DC Direct Current 7, 9, 11, 15, 16, 31
DER Distributed Energy Resources 6, 15
DG Distributed Generation 5
DSM Demand Side Management 12
EMS Energy Management System 6, 8, 15
ESS Energy Storage System 7, 10, 15–20, 53, 54
EU European Union 6
HESS Hybrid Energy Storage System 18
HV High Voltage 11
IEEE The Institute Of Electrical And Electronics Engineers 6, 8
LC Local Controller 16
Li-ion Lithium-ion 54, 64
1


---

Page 14

---

Acronyms
LTI Linear Time-invariant 24, 25
MAS Multi-agent Control System vii, xi, 16, 20, 22, 23, 38, 40–43, 45, 63, 73
MMSE Minimized Mean Square Error 48
MPC Model Predictive Control vii, 3, 4, 23–25, 37–39, 46–49, 52, 55, 59, 63, 64
MV Medium Voltage 11
OPF Optimal Power Flow Problem 15
PCC Point of Common Coupling 8, 11, 20, 32, 48, 51, 54
PID Proportional–integral–derivative Control 24
PT Potential Transformer 8
PV Photovoltaic 9, 12, 20, 31, 33, 38
QP Quadratic Programming 28
RES Renewable Energy Sources vii, 3, 5, 10
SARIMA Seasonal Autoregressive Integrated Moving Average 48, 49, 54, 63, 71
SMES Superconducting Magnetic Energy Storage System 11
SoC State of Charge 16–19, 34, 37, 38, 42, 46, 47, 52, 56, 64
USA United States of America 5
V2G Vehicle-to-grid 14
VCVSI Voltage-controlled Voltage Source Inverters 17, 18
VPP Virtual Power Plant 15
2


---

Page 15

---

1 Introduction
As a result of the climate change incentives, governments around the world are lim-
iting the number of fossil-fuelled power plants. Similarly, large nuclear power plants
are getting less and less popular due to safety concerns and high initial costs. Shut-
ting down of these centrally located high power generators is completely changing
the power grid. The energy generation nowadays happens in an increasingly de-
centralized manner. Such change does not only affect the energy path between the
producers and the consumers but also introduces the need to develop novel control
architectures [1].
The need to adapt to these challenges motivates the implementation of renewable
energy sources (RES) into the grid. However, the operation and control of systems
with major RES contribution is more complex and volatile due to their dependence
on meteorological inputs. In this context, a major research effort is currently under-
taken concerning future reliable and resilient power system operation. Among this,
the concept of microgrids and local energy communities emerges, see [2, 3]. This
power system structure, based on the separation of a part of the power grid, is able
to significantly lower the general complexity of the whole system. Additionally, it
provides opportunities for more effective control of the installed renewable sources.
There are a number of possibilities to realize the microgrid control, as for example
[4, 5]. Existing solutions differ not only in the implementation of actual algorithms
but also in the overall structure of each microgrid. For this reason, microgrid control
is often precisely designed to fit the features of a specific system.
Generally, the control of microgrids does not have to differ from the conventional
control of power grids. In this case, the well-known three-level control architecture
with decentralized primary control and centralized secondary and tertiary control is
embedded, [5]. The microgrids, however, bring opportunities for the design of more
scalable, reliable and efficient control concepts such as the distributed control. Var-
ious distributed cooperative control approaches are presented in numerous articles,
see [6, 7, 8, 9].
Model predictive control (MPC), [10, 11, 12], is also widely used for microgrids. It
enables to incorporate the knowledge about power generation from renewables over
a specific time horizon in the decision-making process. In this way, the controller
performance can be improved, especially when the knowledge about the future power
generation is subject to low uncertainty, see [13, 14, 15].
In particular, [16, 17, 9] bring a consensus algorithm that provides optimal power
resources management based on minimization of quadratic costs of all controllable
power resources.
However, this particular algorithm, which is often used in the
3


---

Page 16

---

1 Introduction
literature fails to converge on arbitrary network topologies even if they contain a
spanning tree.
This thesis brings a modified cooperative protocol mitigating the instability issues
from [16]. Moreover, the algorithm works on arbitrary communication graph topolo-
gies containing a spanning tree. Furthermore, this consensus algorithm is combined
with a higher level MPC protocol to achieve optimal dispatch of energy resources.
The dependence of the total algorithm performance on control parameters is iden-
tified and the parameters are set so as to optimize the system behaviour according
to economical and battery utilization criteria. The developed control architecture
is successfully tested on the actual data measured at microgrid Simris, deployed
as a part of EU project InterFlex H2020. The performed tests are very promising;
the proposed algorithm outperforms conventional control in most of the tests and
brings significant cost reduction when the energy production and consumption of
the microgrid are balanced.
In Chapter 2 the concept of microgrids is introduced, followed by the architecture
of the typical control strategies for microgrids and the concept of model predictive
control. In the second part of the thesis, the implementation of the control algorithm
is shown. Chapter 3 describes the scope and objective of the pilot site. Moreover,
the underlying dataset and necessary data pre-processing steps are presented. The
design of the controller is elaborated in detail in Chapter 4.
In Chapter 5 the simulated results of the implemented control are shown, ex-
plained and compared. Conclusions have been drawn in Chapter 6, incorporating
the relevance for future work in this field.
4


---

Page 17

---

2 Microgrid Control Concepts
Due to the rapid population growth and industrialization, the electricity demand
is increasing significantly.
To cope with this development, the power generation
capacity increases accordingly.
A major part of the new generation assets (also
replacing current bulk power generation) shall be covered by distributed generation
(DG) based on RES to achieve lower carbon dioxide (CO2) emission in the energy
sector. Thus, new challenges arise in terms of predicting the grid operating state,
since RES are highly intermittent.
As a consequence of population density growth, the energy network will be ex-
panded into very rural places where only the construction of electricity lines for
interconnection with the main power grid can become very expensive. Because of
the usual low energy demand in these areas, the construction of conventional power
plants would not make much sense. Also, covering the demand with central bulk
generation is inefficient due to losses and cost of construction of long transmission
lines.
One way to solve these problems is the microgrid concept. This idea of grid infras-
tructure increases the reliability of the network by segmentation which reduces the
probability of the black-outs. Therefore, the overall security of supply is increased.
Due to the local distribution of energy resources, the cost of the grid construction
can be significantly decreased. The fact, that the energy does not have to travel far,
can have a positive influence on the electricity price. The microgrid control, which
can lead to the utilization of different energy sources to the economical optimum,
can also result in a reduction of the energy price.
In many industrially strong countries, the congestion on the main power lines
starts to be a severe problem. The density of the population does not allow the
construction of new overhead lines and the upgrade of the existing can be com-
plicated. The dense distribution of power sources and loads (in comparison with
today’s power system) in microgrids can facilitate the future grid development.
Lastly, smaller systems, such as microgrids, can result in a higher quality of energy
supply towards the end consumer, due to a less complex control scheme [18, 19].
2.1 The Microgrid
For a long time, microgrids did not have worldwide-used definition and there are
multiple reasons for it. In the different parts of the world, the concept of microgrid
was introduced regarding particular motivations.
In the United States of America (USA) the main propagators frequently saw mi-
crogrids as the way, how to get electrification to very remote locations and also
5


---

Page 18

---

2 Microgrid Control Concepts
how to replace obsolete network infrastructure. In one of the oldest definition of
microgrid [20] from 2002, the microgrid is defined as a system which besides elec-
tricity provides also heat. The emphasis is placed on the simplicity of connection
and disconnection of individual customers, local reliability and security of electricity
supply.
On the other hand, in the European Union (EU), the main purpose of microgrid
infrastructure is mostly to integrate renewable energy sources and to operate them
with maximal efficiency. Due to their intermittent character, they are often used
as a negative load in today’s network. It is crucial to apply a microgrid control to
ensure the efficient utilization of these energy sources and to provide quality, reliable
and secure energy supply.
In countries with high dependence on the import of fossil fuels, such as Japan,
the microgrid concept can be a technique to reduce their dependence on imported
primary energy carriers. This can help to protect the network from frequent energy
shortages. For such an innovative country as Japan, this is also a practical approach
to test new energy sources and technologies of energy harvesting [18, 21].
The microgrid concept was finally defined in 2017 by The Institute of Electrical and
Electronics Engineers (IEEE) Standard for the Specification of Microgrid Controllers
[22]. By standard IEEE 2030.7-2017, a microgrid is a group of interconnected loads
and distributed energy resources (DER) with clearly defined electrical boundaries
that act as a single controllable entity concerning the grid. It can be connected
and disconnected from the grid to operate in grid-connected or islanded modes
respectively.
As mentioned in the definition, there are two fundamental modes in which the
microgrid can be used.
• Islanded mode In the islanded mode the microgrid is disconnected from the
macrogrid. During this operation, the energy exchange inside the microgrid is
controlled by its central controller.
• Grid-connected mode During the operation in the grid-connected mode
the microgrid is fully connected to the main macrogrid. The control of the
voltage and the frequency level stays in the hands of the macrogrid energy
management system (EMS) authorities. The microgrid central controller only
coordinate power dispatch of the variable sources and loads to maintain the
economical optimization.
The switching between these two modes is done by the locally implemented central
controlling system and it does not depend on the macrogrid. The central controller
contains the logic that decides if the modes should be changed.
There are many potential reasons to switch between the microgrid’s modes. In
general, the switching events can be divided into two categories; preplanned and
unplanned. In case of preplanned switching event, the incident is scheduled and
expected. Therefore, the process of opening/closing of the main switch should lead
to minimal transient. Typically, this event occurs during maintenance.
6


---

Page 19

---

2.1 The Microgrid
The unplanned switching is usually induced by any type of faults. The way, in
which the microgrid controller reacts to this event highly depends on the operating
condition before the fault and also on the fault nature.
Furthermore, the fault
detection interval and microgrid topology influence the final state [23].
Beside distributed generators and distributed loads, the microgrids usually contain
energy storage systems (ESSs) that provide the ability to save energy for later use.
Energy can be saved not only as an electrical but also in the form of thermal energy
or other.
Conventionally, microgrids are designed as separated parts of the main electricity
network, thus three-phase alternating current (AC) power systems. Although the
biggest advantage of AC systems, easy voltage level change by transformers, is not
that crucial for microgrids.
On the other hand, some distributed energy sources are producing direct current
(DC) power and that must be later converted by DC/AC converter for connection
to the grid. Also, many DC loads use the opposite process to get the power from the
grid. Hence, recently fully DC microgrids, as well as hybrid microgrids (partially
AC, partially DC), are proposed [24]. Thanks to that, the large power conversion
losses can be avoided.
Figure 2.1: Typical microgrid structure [18]
7


---

Page 20

---

2 Microgrid Control Concepts
In Figure 2.1 the typical structure of a microgrid is visualized. The microgrid
is connected to the main grid through substation with main switch (point of com-
mon coupling (PCC)). The power flows inside the microgrid and also power exchange
with outside are controlled by EMS. Beside that, it consists of energy resources (con-
ventional based on fossil fuels and renewable sources), energy storage (in this case
illustrated as BESS inside of container) and final energy users. These components
will be discussed in further detail in the following section.
2.1.1 Microgrids components
Typically, microgrids are composed of the following general components. The num-
ber of different parts depends on the design of each specific one.
PCC
The main switch connects the microgrid with the macrogrid. This equipment is usu-
ally strongly standardized (IEEE 1547) and beside power switching, it also provides
power protection, metering, and communication between both sides.
The grid status is measured from both sides of the switch to find out the operating
conditions of the microgrid. As it is illustrated in Figure 2.2, the current transformer
(CT) and potential transformer (PT) are used for this purpose [25].
Figure 2.2: Schematic diagram of a circuit breaker based interconnection switch [25]
Energy generation
Distributed energy generators are usually small energy sources located near the
areas, where the created energy is stored or consumed. Principally we can distinguish
between two main types, thermal energy sources that are based on the burning of
fossil fuel and renewable energy sources.
8


---

Page 21

---

2.1 The Microgrid
The generation of electrical energy can also be combined with other processes such
as the usage of thermal energy from waste heat. This process allows us to decrease
the overall electricity demand in the microgrid and increase the energy production
efficiency significantly.
The energy generators are producing AC or DC power, in case that the microgrid
infrastructure is using the other type, the power must be converted by the appro-
priate power electronics. Many different energy sources are using various ways for
electric energy production, only the most fitting ones for microgrids will be listed
[23]:
• Combustion engines
• Wind turbines
• Fuel-cells
• Photovoltaic system (or solar-thermal systems)
Typically, the combustion engines transform chemical energy stored in fuel material
to mechanical energy by burning process. Even though some renewable fuels exist,
most combustion engines run on fossil fuels and usually produce CO2 emissions. The
fuel-burning process can be initialized at any moment and after start-up time the
output power of the engine is easy to regulate. Therefore, in microgrid concepts,
they are usually used as back-up generators and their usage in the microgrid should
be limited.
On the other hand, the energy generation from renewable sources is strongly sup-
ported. The wind turbine converts the mechanical energy of the wind to electric
energy. They can be designed in many different sizes from small household applica-
tions to large wind turbines located in off-shore wind parks with rated power up to
10 MW. The total amount of installed wind turbine capacity is growing worldwide
and for many countries and regions, it slowly becomes the most important energy
source [26].
Fuel-cell systems convert the chemical energy to electrical not using a burning pro-
cess as combustion engines but through chemical reaction of hydrogen and oxygen.
Although these two elements are energetically demanding during their production,
we can consider fuel-cell as a renewable source. Despite the fact, that the process is
not very efficient, the use of fuel-cell can be beneficial in some cases due to the low
operational cost.
Photovoltaic (PV) systems consist of PV panels that convert solar radiation into
electrical energy. PV systems are often accompanied by additional systems utilizing
the same primary energy such as solar-thermal systems for heating purposes. The
size of the system can differ from household applications (typically PV panels on
roof) to large solar parks. Compared to the wind turbine, the disadvantage of PV
panels is the necessity to convert the created power from DC to AC. Despite the
large progress in power electronics in recent years, the AC/DC conversion has at
best an efficiency of 92% [27].
9


---

Page 22

---

2 Microgrid Control Concepts
Energy consumption
Energy consumption represents all electrical energy which is converted to the other
energy types and used by end-users.
In the concept of power system networks,
energy consumption corresponds to all nodes that are taking energy from the grid.
Energy consuming objects can be categorized in multiple ways.
Typically, to
the size of the customer, we can distinguish between industrial, commercial and
residential consumers. Since the consumption of residential consumers is quite un-
predictable, it makes sense to aggregate them into bigger groups and create larger
virtual objects with large consumption and higher predictability rate for control
purposes.
In recent years, the possibility of the controllable load of microgrids has been
researched. This concept aims to take less critical consumption processes and shift
them such that, from a microgrid operators perspective, an optimal load profile
is achieved.
Thanks to the load shifting the microgrid control can decrease the
divergence between load peaks and valleys and thus follow the production curve of
RES accordingly. This topic is further discussed in Section 2.1.3.
Energy storages
Distributed energy storages are crucial components of microgrids which balance a
power mismatch between energy generation and consumption in the network.
They are improving the microgrid performance in three ways [25]. First of all, they
allow energy resources to run on maximum output when grid capacity is limited.
In case that RES generate electrical energy in times of low energy demand in the
network, distributes energy storages can charge and thus temporarily consume the
energy locally. During low energy generation times, for example at nights, the energy
can be discharged and provided to the grid customers. This significantly improves
the efficiency of renewable sources and helps to reduce CO2 emission.
As it was said before, the largest disadvantage of many renewable sources is their
intermittency. In case of fluctuation of the primary energies of these generators, the
distributed energy storages can replace them as a power source.
Lastly, the storages can help during disturbances, maintenance or unplanned out-
ages of the network. The BESSs are systems with very steep starting ramp that
makes them usable almost immediately. Therefore, in case of faults, this ESSs can
provide energy and support the most important processes before while BUGs are
slowly activated.
The different distributed energy storages can store energy in the form of electrical,
chemical, mechanical or in other type of energy [23]:
• BESS
• Capacitor/Super-capacitor storage
• Low- and high-speed flywheel
10


---

Page 23

---

2.1 The Microgrid
• Superconducting magnetic energy storage system (SMES)
BESSs store electrical energy in the form of chemical energy between two or more
chemical elements. They are DC power systems, hence the power electronics inverter
is necessary for their connection to AC microgrids network. Currently, they are the
most popular type of distributed storage and they still gain popularity.
Super-capacitors (sometimes ultra-capacitors) are storing directly electrical en-
ergy. Their biggest advantage is very high power density, the ability to tolerate
frequent charging/discharging cycles and much shorter start-up times compared to
batteries. Therefore, they can be used most efficiently in applications, where high
power charging capability is more important than energy-storing [28].
Flywheel systems are converting electrical energy to rotation energy (kinetic en-
ergy). Usually, the system consists of rotation mass, electric motor supplying energy
to it and generator coupled to the same shaft. Besides energy storage, this system
can be also used for smoothing of different power sources.
The last type of energy storage is SMES. This system usually includes a super-
conducting coil located in artificially created extremely cold surroundings. Once the
coil is charged the energy is stored in the form of magnetic energy nearly eternally.
The charging and discharging losses are very low, thus the overall efficiency is mostly
affected by the energy needed for creating the cold ambient [29].
2.1.2 Microgrids types
Depending on several parameters such as size, purpose, technical design, and stabil-
ity aspects, the microgrids can generally be divided into few categories. [30, 31]
Utility microgrid
The utility or community microgrids (sometimes milligrids) are usually quite large
microgrids that are connected to the main grid with the multiple PCC. The main
microgrid network runs on medium voltage level so the PCC is provided by a high
voltage (HV)/medium voltage (MV) power substation (primary substation). Com-
munity microgrids typically connect a few thousands of customers and bigger dis-
tributed generators such as wind power plants.
These microgrids do not deviate from the formal definition.
Utility microgrid
usually contains centrally owned distributed generators and the power balancing
and control is realized by a central control system [32].
Remote microgrid
The remote microgrid is ordinarily not connected to the main grid and their ge-
ographical remoteness makes the connection to a macrogrid very costly or totally
impossible. Hence, the microgrid system is usually controlled by decentralized con-
trol methods and stays in the islanded mode.
These microgrids can represent whole villages, small cities or grids on islands.
11


---

Page 24

---

2 Microgrid Control Concepts
Facility microgrid
Facility microgrids represent the classical microgrid structure on a small scale.
Mostly, it contains just one customer, private or industrial with small distributed
power sources, for example, rooftop PV panels on private premises.
This type is generally connected with the main utility grid and works in grid-
connected mode. Mostly just in case of faults in macrogrid, the mode would switch
to islanded.
Institutional microgrid
Institutional, campus or virtual microgrids combines a group of low voltage dis-
tributed loads and/or distributed generators in such a way, that they can be ob-
served as a single entity from the main grid point of view. From a system controllers
point of view, this is a significant advantage.
Special cases
Besides these four cases, the microgrid concept can also be deployed in very special
cases where the reliable energy supply is secured. A typical example of this problem
can be the electricity network in military bases, hospitals or similar tactical objects.
2.1.3 Demand side management
In electricity systems where one significant part of the energy is created by renew-
able sources the new challenges arise. For stability purposes, the same amount of
generated and consumed energy must be secured in the network for any moment in
time. Usually, the peak of renewable generators does not correspond to the time
of load peaks. For that reason, enough capacity of expensive back-up generators or
other power sources must be located in the network.
One of the solutions to fit generation and load curve to each other a little better
can be demand side management (DSM). Systems that apply DSM can reschedule
the energy demand towards times when it can be covered more effectively.
DSM can be classified into two categories, direct and indirect load control. While
direct load control increases or reduces the electric demand of assets, when the grid
is imbalanced, indirect load control employs price signals and motivates the end
customer to use electricity in specific hours by its price [33].
There are six load-shaping methods [34]:
1. Peak clipping - decreasing the maximum load peak value
2. Valley filling - filling the difference between peak and valley
3. Load shifting - moving peak load to the different place in time
4. Strategic conservation - reduction of general consumption because of future
reasons
12


---

Page 25

---

2.1 The Microgrid
5. Strategic load growth - promotion of general consumption because of future
reasons
6. Flexible load shape - increasing of load flexibility
In Figure 2.3 the load-shaping methods are visualized. It shows all six mentioned
methods on the smaller figures. The purple arrows on all of them indicate the wanted
change of the load curve.
Figure 2.3: Illustration of load shaping methods [35]
Controllable loads
According to research in [36], one can classify controllable loads into three categories.
Type I contains all smaller types of loads which are not critical for the end customers
and can be interrupted or rescheduled. With this controllable load type, only the
demand modification are possible, there is no energy to be stored and used later.
Therefore, they are sometimes known as passive controllable loads. Typically, air-
condition (A/C), water and central heating or washing machine processes can be
re-planned to a later point in time.
There are two ways how to process this load management. The customer can
make a deal with power utilities and then limit his power demand in preallocated
time or when it is needed. The other approach gives the end customer a higher level
of freedom. Short time-variant power prices are distributed between customers and
they can adjust their power demand accordingly.
13


---

Page 26

---

2 Microgrid Control Concepts
The second category, type II, is called active controllable loads and includes
BESSs, vehicle-to-grid (V2G) systems, and combined cooling, heating and power
systems (CCHPs). Unlike the previous category, these systems can store the gener-
ated energy for later use and supply it to the network.
The advantages of BESSs are described in Section 2.1.1. The development of V2G
systems is strongly related to the rapid expansion of electro-mobility. In this concept,
batteries of fully electric cars or of plug-in hybrid which are currently connected to
the grid might be used as distributed storages when needed. These small capacity
devices can help with power network balancing and provide support for distributed
renewable generators. V2G can also be used as a controllable load of the first type
by scheduling car charging.
Figure 2.4: Classification of controllable loads [36]
14


---

Page 27

---

2.2 Typical microgrid controllers
CCHP saves energy into different end user’s thermal processes such as space heat-
ing or cooling, water heating, refrigeration or in the case of industrial customers in
the form of residual process heat. Due to the low criticality of these processes, the
CCHPs are one of the most promising controllable loads.
In the last category, the whole microgrid or virtual power plant (VPP) (virtual
object aggregating multiple DER and ESSs) is considered as a controllable load for
the larger system.
Besides the preceding load types, these systems also contain
distributed generators. Described classification can be seen in Figure 2.4.
2.2 Typical microgrid controllers
Changing the power network infrastructure from the conventional grid structure to-
wards the microgrid concept brings new challenges in its controlling systems. During
grid-connected mode, the control might be done by the macrogrid operator and the
microgrid central controller might only support this process and attempt to increase
efficiency of the entire power generation process.
On the other hand, in the case of islanded mode, the microgrid’s EMS must be able
to provide voltage stability and general power flow quality regardless of intermittent
power generation of renewable distributed sources.
Conventionally, the three-level-hierarchical control is used in case of power systems
(including microgrids). The lowest level, primary control is in most cases designed
as decentralized droop control which reacts to rapid load changes by changing the
power output of AC generators.
However, these systems can reveal problems. The change of power output of a
generator creates a trade-off between power change and general power qualities such
as frequency or voltage. Moreover, this system is not obtainable for DC distributed
generators which are irreplaceable components of microgrids. The primary control
response is a very quick and autonomous operation. The time scale of this control is
in the range of tens to hundreds of milliseconds to keep voltage and frequency close
to nominal values.
On the contrary, the secondary control is mostly implemented in centralized or
distributed form.
This control operates in longer time-scale (seconds up to tens
of seconds) and its main aim is to compensate the voltage and/or frequency offset
introduced by the primary control.
The purpose of the highest control level, the tertiary control, is not to balance
power generation and demand. Instead of it, it optimizes the performance of the
grid according to economic and operational features.
This is also known as the
optimal power flow problem (OPF). Tertiary control can also manage all kinds of
power flows inside of control area or in between more of them.
Usually, this level of control updates the control information quite seldom, ap-
proximately once every 15 minutes. In some implementation, this control structure
is reduced to the two-layer and the features of the tertiary control are taken over by
secondary control [5, 4].
15


---

Page 28

---

2 Microgrid Control Concepts
This conventional control strategy does not take into account the distributed
energy storages which are typical for microgrids. Similarly, the distributed power
sources without mechanical rotating mass of large inertia are not possible to be
controlled in the manner described above.
Therefore, the control strategies, especially for microgrids with energy storages
and DC power generators, will be now introduced. In general, they can be classified
into three groups based on their architecture. This classification can be noticed in
Figure 2.5.
In decentralised control algorithms, there is no communication between compo-
nents of the system at all. Each containing a local controller (LC) which is providing
the decision making with only a local set of information. Due to the lack of this
bonding between grid elements, the reaction time of the control can be very fast.
Typically, the decentralized control is managed by the standard droop control or by
droop control related to state of charge (SoC) of distributed ESS.
The centralised type of grid control adds a central controller to the system. The
main goal of this central management is to adjust control levels of every single local
controller and to provide the desired power set-points. Centralised control can be
implemented in the secondary or tertiary control level.
Nevertheless, the centralized control brings up multiple challenges. In large sys-
tems where some microgrid parts are located in very remote areas, the commu-
nication distance might be enormous which is increasing controller reaction time
significantly. The fact that all the information is stored at one location also in-
troduces the problem of privacy, security, and reliability of the system. In case of
a security breach to the central controller or in case of some kind of failure, the
complete system might be shut down.
Hence, the third type of control is proposed.
Distributed multi-agent system
(MAS) control offers higher confidentiality for each microgrid component such as
communication between direct neighbours in the network which makes the system
faster and more reliable. The system might be also equipped with a plug-and-play
feature that makes the connection of new agents to the grid very easy. In addition
to that, the individual failure of one agent would lead to lower performance of the
control, but not to complete collapse.
Similar to centralized control, distributed MAS can be used in secondary and
tertiary control level. Recently, this type of control was in focus of many research
studies and numerous different algorithms of distributed control were created. This
topic is further discussed in Section 2.2.3 which is dedicated to it.
2.2.1 Decentralised control architecture
Since decentralized control can operate very fast it is usually used for the primary
control, for balancing the frequency in the grid. As it was mentioned before, although
the conventional droop control can be directly used in most of the microgrids cases,
it can be slightly adjusted to provide efficient control for microgrid’s distributed DC
energy sources.
16


---

Page 29

---

2.2 Typical microgrid controllers
Figure 2.5: Decentralised, centralised and distributed multi-agent control
architecture for microgrids (left to right) [5]
Three different adaptations of droop control are introduced in [5]. Besides clas-
sical version frequently used in macrogrid, there is droop control based on SoC of
distributed ESS and one form of droop control for microgrids with heterogeneous
storages.
Droop control
Conventional droop control is based on coupling between voltage frequency and
amplitude and active and reactive output power. Since the power lines in microgrids
are usually quite short and their impedance is mainly reactive, some elements of
droop equations can be neglected and the control relationship is then interpreted by
following equations (2.1) [9]
fMG = f∗−m · (P −P ∗),
UMG = U∗−n · (Q −Q∗),
(2.1)
where UMG and fMG are frequency and amplitude of the microgrid voltage, P and
Q are active and reactive power respectively and the variables with stars are base
values. Constants m and n are droop coefficients. All the variables are used in per
unit notation.
As it is seen from the equations 2.1, the output voltage frequency directly depends
only on active power as well as voltage amplitude on reactive power. This approxi-
mation which can be done only in small scale systems makes the droop control very
easy to implement.
For the connection of DC distributed generators to the AC grid the power in-
verters are needed. Typically, two types are used. voltage-controlled voltage source
inverters (VCVSI) can to maintain voltage frequency and amplitude control. On
the other hand, current-controlled voltage source inverters (CCVSI) provide active
and reactive power control.
17


---

Page 30

---

2 Microgrid Control Concepts
Both are ideal for different tasks. VCVSI can be used when the optimal power
quality in terms of voltage amplitude and frequency is important.
In contrast,
CCVSI can be used in cases when power balance is not provided to return the
system into a steady state [37].
SoC Droop control
Conventional droop control does not take the state of charge of distributed energy
storages into consideration.
The specific level of SoC which influences not only
remaining energy capacity but also affects energy storage system efficiency and life-
time. For some systems, such as BESS, it might be very inconvenient to discharge
stored energy completely due to the faster ageing of batteries [38].
One of the described solutions of this problem implements weighted droop coeffi-
cients into the droop equations. As a result of this, the energy storage system with
higher SoC can be prioritized and the probability of very low SoC of any of the
ESS is lowered. Therefore, the power demand could be split between ESSs more
advantageously.
This system still has some constraints. In case when one ESS has significantly
higher SoC then another, it would be preferred and rapidly discharged with high
discharging current to cover the power demand. However, the discharging current is
limited in most of the ESS applications. Secondly, it is quite obvious that in case of
low SoC of all ESSs that voltage amplitude and frequency control would be affected.
Heterogeneous storage droop control
Currently, there is no single energy storage type that would be able to secure effective
and low-cost energy for all the processes in the microgrid. Hence, the microgrid
architecture usually contains multiple various types. This brings diversity into the
grid and enables efficient govern to the control algorithm. These systems are often
referred to in literature as hybrid energy storage systems [39].
To utilize different energy storages described in Section 2.1.1, it is useful to con-
sider their specific properties. Various ESSs can differ in many parameters such as
specific power density, energy density, energy price or cycle life. Each ESS compo-
sition is designed for different operation purposes.
For example, supercapacitors are the type of energy storage with long cycle life,
high specific power density, but quite high energy price as well. Therefore, it can be
used very efficiently for power balancing in the grid, however, they are completely
inappropriate for delivering constant energy for a longer period.
There are numerous control algorithms for this type of microgrid system. Among
the most interesting: embedding the linear filtering into the grid. In this algorithm,
the power demand signal is filtered with a low pass filter and then divided into short-
term fluctuation and long-term power demand signal accordingly. Subsequently, the
fast-cycling ESSs such as supercapacitors cover the low grid power variation and i.e.
BESS secure the stable power output.
18


---

Page 31

---

2.2 Typical microgrid controllers
2.2.2 Centralised control architecture
The second type of control strategy is built-in centralised way. Centralised con-
trollers are usually implemented as a secondary or tertiary control providing power
quality control and optimal power flow supervision.
In general, these algorithms can be divided into these two hierarchical control
categories, secondary and tertiary.
Secondary control
Conventionally, the centralised controller as a secondary control is used for correction
of deviation from desired voltage amplitude and frequency created by setting the
correct power set-points.
There are several algorithms presented in [5] modified
especially for microgrid usage.
Certainly, the classic secondary control as it is known from the use in macrogrid
can be adapted to microgrids with distributed energy storages by taking BESSs of
individual storages into consideration by providing weighted droop control as it was
described in Section 2.2.1. However, it does not solve the problem of overloading of
the most charged storage in case of low SoC on others.
Another useful approach is balancing discharge rates of joined energy storages.
Always when there is generated power shortage, the missing power is split into ESSs
inequitable way such that all storages can discharge at the same speed. This algo-
rithm works reasonably fine if the initial SoC of the storages is the same. However,
it does not take into consideration different properties of ESSs and their advantages
and disadvantages.
The lifespan of battery packs in BESS depends, among other parameters, on
charge/discharge cycles and depth of each discharge process. To improve this factor
a new method is designed that starts a charging process for each ESS component
when the batteries reach a float voltage. Thus the number of charging/discharging
cycles is minimized and the lifetime of the battery packs is extended.
The last presented algorithm is the rule-based control. With this set of rules,
the microgrid is maintained and optimized as much as possible. It might include
the decision making for many possible states of the system including fault states.
Previously described algorithms can be also combined by rule-based algorithm to
use them in their most advantageous time.
Tertiary control
Tertiary control in the microgrid concept has different goals during grid-connection
mode and islanded mode. What remains unchanged, is the optimization of power
flow between individual components and the effectiveness of the whole grid.
During grid-connection, the optimal power flow between the microgrid and main
macrogrid could be optimized in such a way, that it is most economically beneficial.
The energy price in the macrogrid can be taken as it is from a local utility or it can
be predicted by an algorithm such as model predictive control. Under consideration
19


---

Page 32

---

2 Microgrid Control Concepts
of this information, the power flow through the PCC can be optimized by buying
energy and charging distributed energy storages during cheap electricity periods.
Similarly, power can be supplied to the main grid when there is a surplus in the
microgrid or when it is economically preferable.
In contrast, during islanded mode, the general aim of tertiary control is different
due to no power exchange with the main grid. In this case, the controller can focus
on forecasts of power generation of renewable sources and an optimal dispatch.
For example, in some periods of the day much larger contribution of PV power
resources can be expected. Similarly, the load curve can be estimated and charging
or discharging of ESSs can be planned accordingly.
2.2.3 Distributed multi-agent control architecture
The last group of control system architectures includes algorithms which appear
to be very promising for further research. In comparison with the previously de-
scribed hierarchical control architecture, the distributed MAS control offers many
advantages [9, 5, 8].
That is the reason why they are commonly used not only in power grid systems
but also in computer science, sensor networks or for groups of unmanned vehicles
such as flying drones or other types of ground robots [40].
As the name implies, this approach is based on splitting the microgrid into smaller
pieces, usually to model each component as an independent agent which unfold
many typical features. Firstly, the complexity of the control is quite low. Each
agent can work separately with an own set of information and security that this
approach provides. The fact that it does not depend on anyone else also increases
the reliability significantly.
However, in comparison with decentralized control methods, the communication
and data exchange between individual agents is possible.
Therefore, each agent
simply behaves according to its information about surroundings, responds directly
to the changes and can fully employ the distributed resources and storages.
This communication network is ordinarily sparse, such that there is no connection
between each agent but only in between selected ones (for example neighbouring
agents). Thanks to that, the agents face a reduced amount of communication effort.
Furthermore, communication is usually done on short distances and therefore can
be very fast [5]. There are three different communication architectures which will
be discussed later in Section 2.2.3.
In addition to it, the system is highly adaptive to the changes in communication
or power connection topology. In case that the topology is still connected after the
adjustments, the system should be able to adapt.
Similar to a centralized algorithm, distributed MAS can be deployed for secondary
and tertiary control. As secondary control, the agents are sharing their information
with their neighbourhood and organize the load sharing.
20


---

Page 33

---

2.2 Typical microgrid controllers
In the case of tertiary control, many algorithms with cooperative or competitive
approaches to agent behaviour can be found in literature. Algorithms from both of
these categories will be further discussed in Section 2.2.3.
Communication architecture
The communication between individual agents in the networks can be provided
according to three different architectures, hierarchical, topology-based and fully dis-
tributed. Exemplary diagrams for each of the architecture are given in Figure 2.6
[5].
Figure 2.6: Distributed MAS communication architectures [5]
First of all, in the hierarchical architecture, all the agents communicate with each
other through one central agent. It can be a randomly chosen one from the agent
set or a new agent added to the grid exactly for this purpose. The central agent is
aware of the grid topology and allocating the optimization problems to each agent.
Even in the presence of the central agent, each agent works with its own set of
parameters, objective function and constraints. The information distribution is the
main difference between this algorithm and centralized control algorithms, that were
introduced in the previous section.
The second architecture enables agents to exchange data directly only with neigh-
bours based on the network topology. Usually, this communication network pre-
cisely mirrors the power network connection. Therefore, it is normally the most
cost-efficient way to establish a communication connection.
Each agent is aware of its neighbours and the parameters of the power connection.
Hence, the complex problem of optimal power flow can be distributed between them.
The agents are usually iteratively updating their local variables and converging to
a consensus. This algorithm is further discussed in the following chapter.
The last communication architecture is fully distributed and it contains commu-
nication connection between all agents. It is de facto a specific modification of the
topology based architecture.
21


---

Page 34

---

2 Microgrid Control Concepts
This architecture is advantageous for its high robustness, not only due to the po-
tential failure of one of the agent but also for total independence from the power
network topology. However, it is usually the most complex and expensive to con-
struct.
Control strategies
There are several strategies of MAS control based on many different approaches.
Demonstration of synchronization of independent agents could be found often in
nature. Based on observation of schools of fish or flocks of birds, many of these
algorithms were created [7].
First, the big class of these strategies is containing consensus algorithms which are
providing synchronization of the agents. These algorithms are iteratively looking for
a common value of defined parameters by the cooperation of the agents.
The other group of control strategies contains algorithms based on game the-
ory. Game theory algorithms are creating an environment in which all agents are
considered as players of the game and they are trying to optimize their objective
depending on their and other players’ actions simultaneously. If the goal of each
agent can be expressed, game theory control algorithms can provide a large set of
interesting solutions [8].
Solely the consensus algorithm will is described in detail in the following section.
Consensus algorithms
Consensus algorithms are control strategies that are described as interaction between
neighbouring agents in one network topology to convert to the optimal value of
specific shared variable. In case that the agent can be described as single integrator
systems, the dynamic of consensus algorithms in discrete system can be expressed
by equation (2.3) [16]
xi[t + 1] =
n
X
j=1
dijxj[t],
(2.2)
where xi and xj both describe local information of agent i and j respectively, where
agent i is the examined agent and agent j is part of a set of neighbours n. The
constant dij stands for a coupling coefficient between these specific agents and t
indicates time step.
In case that the network connection graph is in the form of a spanning tree and it
is fully connected, the consensus is achieved. Although, the system dynamic highly
depends on dij coefficients. Therefore, correct settings of them is crucial [41].
Equation (2.3) can be described in matrix form to state one time-step computation
of the whole network into one
X[t + 1] = DX[t],
(2.3)
22


---

Page 35

---

2.3 The Concept of model predictive control
where D matrix is a weighted adjacency matrix (communication matrix) of the
system, it is symmetrical over the main diagonal and contains dij communication
coefficients between individual agents.
It can be designed in different ways which highly influence the final performance.
For some topologies, such as radial or ring connection of agents, it might change the
dynamics significantly [42]. The selected variants are further discussed in Chapter
4.
Since consensus algorithms can be described as an integral part of the MAS net-
works, there are many different adaptations to the specific needs of each network.
To modify the algorithm for real networks, consensus strategy with delays as well
as with changing topology and with sampled data are discussed.
Beside that, the optimal consensus, adaptive consensus algorithm is presented in
[9] to achieve better control performance. Depending on which type of system the
agents are located in, the consensus for single-integrator systems and second-order
consensus algorithm can be found. Besides, algorithms for generic linear system
agents are mentioned.
Moreover, the consensus algorithm can be modified by adding a leader to the
system to improve the control performance. Leaderless systems convert to a consen-
sus based only on their initial values. Declaring one agent as a leader changes the
dynamics a bit and the common value is then pinning to it.
This changes the problem from a cooperative regulator problem to a cooperative
tracking. On the other hand, pinning consensus algorithm is not applicable when
the right final value is unknown [7].
2.3 The Concept of model predictive control
MPC is a control strategy firstly used in the 80s in the petrochemical industry. After
that, it was thoroughly investigated and massively deployed in many other industrial
fields [43].
In literature, MPC is also known as dynamic matrix control, generalised predictive
control, model algorithmic control or predictive functional control. Therefore, the
model predictive control is the generic name which covers all these control systems
together.
There are many reasons for MPC popularity. MPC control can provide multivari-
able control solutions and take the physical limitation of the system into consider-
ation. Besides that, it allows the system to operate, considering physical limits or
very close to them which makes it usually very effective.
Lastly, the update rate of individual steps is not that fast and therefore there is
sufficient time for computation that has to be done during the control. This reason
was crucial mostly at the start of the first MPC implementation due to the lower
computation power than we have today. In these days, this is only a minor advantage
of the algorithm [10].
23


---

Page 36

---

2 Microgrid Control Concepts
Control structure is generally quite simple. Essentially, the controller has to con-
tain a dynamic model of a controlled system which is used to forecast the future
states. This allows to MPC to take into consideration the future evolution of state
variables during their optimization in the current time.
Thanks to that, MPC
can predict future events and optimally prepare for them unlike classical propor-
tional–integral–derivative control (PID) control.
For the performance of the algorithm, it does not matter how was the model
obtained. Generally, it is more convenient to use linear time-invariant (LTI) models
if possible.
When the system does not have linear dynamic or if it can not be
linearised reasonably, the version of non-linear MPC is also available. However, in
the case of LTI model, the control problem is simplified with linear algebra principles
and the complexity of the problem is reduced to the matrix equations, which can be
computed very fast and efficiently [44].
Often, the model is just an approximation of the system and has smaller or larger
differences in its dynamics.
Hence, there is always some level of uncertainty in
the prediction.
To decide how should the algorithm proceed, a cost function is
introduced. This function solves the typical trade-off between the performance of
the system and the price of the control. That can be described as the ability to
follow the right trajectory and price of the input to the system, respectively. This
function is usually designed according to what is important for the system and
control designer.
When the future strategy is completely planned, only the first step of the control
is applied. Subsequently, the whole control process is repeated in the next time step
and the prediction horizon is also moved one step forward.
In real life systems, the resources are always limited. Luckily, the algorithm is
aware of constraints in the size of the input to the system as well as in state val-
ues. These constraints can be classified into two categories, equality and inequality
constraints.
As an illustration, the first group contains any relationship between state variables
that must be precisely held at any time. The second category represents for instance
maximum possible input to the system which can not be exceeded.
In Figure 2.7 some significant signals of MPC control in the current time step k
are shown. Signal s(t) represents the set-point of the system, the value to which the
actual output y(t) should converge. Signal r(t) stands for reference trajectory in the
time step k. It shows the optimal trajectory that the system should follow.
The internal model of the system is used to create predicted outputs ^y(t|k) and
^yf(t|k) with applied input and without it respectively. As it is visible, they depend
on current time-step k. Afterwards, the ^y(t|k) can be expressed as a free system
response ^yf(t|k) and the response depending on the applied input. From this rela-
tionship, the optimal applied input can be easily computed.
As was said before, from the computed optimal input just the first step is taken
and the whole process is repeated for the next time-step. For the sake of simplicity,
the presented example is a single input single output continuous system. In the case
24


---

Page 37

---

2.3 The Concept of model predictive control
of the multi-variable control system, the reference signal r(t) is often computed as
least square permeation of single references.
For the case of MPC with constraints, the more complicated algorithms for ref-
erence computation can be used. The predicted outputs are computed for multiple
time steps and then the least square algorithm concerning the constraints is applied.
In the end, just the first step of the computed trajectory is taken, as always [10].
For this thesis, the description of the MPC algorithm in case of linear time-
invariant systems will follow.
2.3.1 MPC formulation
In general, the MPC algorithm proceeds in three steps; it measures the available
measurements, computes the optimal input accordingly and then applies it to the
system. The controller performance can be influenced by two important components
of MPC structure.
Firstly, the definition of an internal model and the fact how it reflects the reality
significantly determines the speed with which the controlled output can converge
to the reference. Secondly, the definition of the cost function solves the trade-off
between different aspects of the controller. The designer of the control can typically
decide what is the priority, the cost-saving of the input to the system or the speed
of controller convergence.
The typical implementation of MPC control can be seen in Figure 2.8. In this
case, it is enhanced by the observer which is a classical implementation of a Kalman
filter. These settings can be used when the system is not fully observable.
Internal model
For this thesis, the linear time-invariant discrete-time model will be assumed.
In the general implementation of the MPC algorithm into the real world, the
systems are usually non-linear and continuous where there are no assumptions ap-
plied. In it is the case, the system must be a priori linearized on some reasonable
surroundings (usually around equilibrium points). Moreover, it has to be sampled.
Applying state-space equations the model can be described by equations (2.4) [10]
x(k + 1) = Ax(k) + Bu(k),
y(k) = Cyx(k),
z(k) = Czx(k),
(2.4)
where x is a vector of the state variables, y is a vector of measured outputs and z
is a vector of controllable outputs. In ordinary system type, the vectors y and z are
the same.
For LTI system, it does not matter how the internal model is obtained. One of the
possible ways is the identification regarding system response. Other possibilities are
trying to approximate the real system with known system equations or to declare it
as a known system and then identify its parameters.
25


---

Page 38

---

2 Microgrid Control Concepts
Cost function
The cost function assigns scalar prices to each possible control strategies.
The
optimal one is then chosen as the control strategy with the lowest cost. Usually,
quadratic cost functions are used due to their simplicity and ensured non-negative
values. In general form, the cost function can be defined as equation (2.5) [10]
V (k) =
Hp
X
i=Hw
||^z(k + i|k) −r(k + i|k)||2
Q(i) +
Hu−1
X
i=0
||Δ^u(k + i|k)||2
R(i).
(2.5)
This equation contains two terms. The first one penalizes the distance between pre-
dicted output of the system ^z and reference r for each future time step in dependency
on current time step k. That is done by summation of all penalties in prediction
horizon Hp. The first penalized time step is set by Hw.
The second term penalizes the used input into the system for each time step in the
defined control horizon Hu, where Hu ≤Hp. Both equation terms are multiplied by
coefficients Q and R, respectively. With these factors, the weight of each term can
be defined. In the case of single controlled variable systems, these two parameters
are scalars, but in the case of general multi-variable systems, they are matrices.
They both are assumed to be non-negative and even more often diagonal.
Constraints
The inequality constraints of the system are defined in matrices E, F, and G and
taking restriction of input change Δ^u, input absolute value ^u and controlled variables
^z respectively into consideration.
The matrices have the structure so the following matrix equation would create
each constraint in each line of the final equation,
E ·

Δ^u(k|k)
...
Δ^u(k + Hu −1|k)
1

≤

0
...
0
0

.
(2.6)
The structure of the other two matrices is based on the same principle.
2.3.2 MPC solution
In this section, the differences between constrained and unconstrained solutions of
the controlled system are discussed. Although there are differences between these
two approaches, they are both based on minimization of the cost function.
Unconstrained solution
As said before, in the unconstrained case the solution of the minimization can be
reduced to the matrix operation. The cost function can be modified as follows [10]
V (k) = ||Z(k) −T(k)||2
Q + ||ΔU(k)||2
R,
(2.7)
26


---

Page 39

---

2.3 The Concept of model predictive control
where Z, T, and ΔU are column vectors of ^z, ^r, and Δ^u in each time step of the
predicted horizon.
Furthermore, Z can be written in the form that reveals the dependency on current
state, input, and change of the input from the last time step,
Z(k) = Ψx(k) + Φu(k −1) + ΘΔU(k).
(2.8)
Subsequently, tracking error ϵ can be defined as the difference between predicted free
response of the system ^yf and predicted trajectory ^r. This error shows the progress
of control if it is equal to zero the control reference is reached,
ϵ(k) = T(k) −Ψx(k) −Φu(k −1).
(2.9)
From here the cost function can be redesigned as follows
V (k) = const −ΔU(k)T G + ΔU(k)T HΔU(k),
(2.10)
where G and H are defined as
G = 2ΘT Qϵ,
(2.11)
H = ΘT QΘ + R.
(2.12)
The optimal input to the system ΔU(k)opt is then found by minimization of equation
(2.10). The gradient is computed and set to zero. The final form of the optimum
input is then defined in equation (2.13)
ΔU(k)opt = 1
2H−1G.
(2.13)
There is another way, based on the least square algorithm with which it is possible
to compute the optimal input. Since the inverse matrix of Hessian matrix H can be
quite tricky, this approach is mostly used.
Firstly, the square roots of R and Q matrix are necessary,
ST
QSQ = Q,
ST
RSR = R.
(2.14)
Based on them, the square root of the cost function can be found,

SQ(ΘΔU(k) −ϵ(k))
SRΔU(k)

2
= V (k),
(2.15)
and the least square solution of this equation

SQΘ
SR
 ΔU(k) =

SQϵ(k)
0
 .
(2.16)
27


---

Page 40

---

2 Microgrid Control Concepts
Constrained solution
All three constraint matrices can be expressed in the same fashion as matrix F
F1
F2
. . .
FHu
f
 ·

^u(k|k)
...
^u(k + Hu −1|k)
1

≤

0
...
0
0

.
(2.17)
Since the predicted input can changes to form of equation (2.18) the matrix F can
be rewritten as equation (2.19),
^u(k + i −1|k) = u(k −1) +
i−1
X
j=0
Δ^u(k + j|k),
(2.18)
FΔU(k) ≤−F1u(k −1) −f.
(2.19)
Now, the same trick can be used for the constraint matrix G. For which the de-
composition according to equation (2.8) is used. After setting G =
Γ
g
 it can be
finally expressed similarly in equation (2.19),
ΓΘΔU(k) ≤−Γ(Ψx(k) + Φu(k −1)) −g.
(2.20)
All constraints can be summed up in one equation (2.21),

F
ΓΘ
W

ΔU(k) ≤

−F1u(k −1) −f
−Γ(Ψx(k) + Φu(k −1)) −g
w

.
(2.21)
Above-mentioned, the optimum input is found as a minimization of cost function,
in this time as a subject to constraints in equation (2.21). This kind of optimization
problem is called quadratic programming (QP) and it is a standard optimization
algorithm. Here, the task is presented as the following minimization,
minimize ΔU(k)T HΔU(k) −GT ΔU(k).
(2.22)
The solution of the QP problem is shown in [10]. Due to the high complexity, it is
not further discussed in this work.
28


---

Page 41

---

2.3 The Concept of model predictive control
Figure 2.7: Basic idea of MPC shown on dependency of individual signals on time
[10]
29


---

Page 42

---

2 Microgrid Control Concepts
Figure 2.8: Structure of MPC enhanced by observer (when some of the states are
not observable from system outputs). In this case the set-point of the
system is labelled as w(.|k) [45]
30


---

Page 43

---

3 Use Case
For the rigorous validation of the created control algorithm, the testing on the
data from the real-life demonstration site is necessary. Thanks to that, the real
phenomena, which can occur in the microgrid, can be observed.
In the context of H2020 EU Projekt InterFlex, the consortium develops advanced
control solutions for the microgrid test site in Simris, developed by E.ON in Sweden.
The testing of the software in the authentic environment brings the opportunity
to test the control algorithms on the situations, that would occur very rarely in real-
life, but could be critical for the whole system. That increases the final reliability of
the analysis, proposed solution of the project and creates the ideas for the further
development and reasoning for a future deployment of these new control schemes.
3.1 Demonstration site Simris
The test site Simris is located in southern Sweden. It is a microgrid concept, capable
to run all by itself which contains distributed renewable sources, distributed storage
systems and connections to the communities nearby this village. The project started
in 2017 and since then, it was used for testing new features of microgrid and smart
grid concepts and also for testing of large variety of control algorithms.
3.1.1 Simris components
The structure of Simris can be seen in Figure 3.1. The individual components of
the microgrid are represented by their schematic symbols [15].
In the right bottom corner the renewable sources, PV park, and wind generator
are illustrated. Right above them, the BUG and BESS can be seen. All of these
components have assigned transformers for the conversion of their output voltage to
the grid level. Of course, due to the DC output voltage of the PV park and BESS,
there are additionally DC/AC inverters.
The installed rated powers of the PV park, wind generator and BUG are 500 kW,
442 kW, and 350 kW respectively. In the original implementation of the BESS, the
battery pack was constructed with Li-Ion batteries with a total capacity of 333 kWh.
In early 2019 the redox flow BESS was added parallel to the already implemented
BESS. It increased a total battery capacity of the system up to 1933 kWh.
The figure also depicts six schematic symbols of accumulated loads, which are to-
gether representing 150 objects, mostly households. Couple of them are equipped by
distributed energy storages which opens the opportunity for demand side manage-
31


---

Page 44

---

3 Use Case
ment. Currently, the water boilers, heat pumps, and distributed BESS are installed
with a total capacity of 142.55 kWh.
Figure 3.1: Schematic structure of Simris demonstration site [15]
On the top of the figure, the PCC with the macrogrid is shown. There are also ad-
ditional components of the microgrid structure such as circuit breakers. In between
individual components, there are black numbered dots that represent physically in-
stalled buses. The parameters of each power bus, such as resistance and reactance
are also listed.
3.2 Measured data
For the simulation of the designed controller, not all measurements of the highlighted
buses are needed. It is only necessary to collect the measurements of seven “passive”
nodes, power measurement from buses 3, 5, 6, 7, 10, 11 and 13. The control concept
and reasoning behind this decision will be further discussed in Chapter 4.
Unfortunately, the work with real-life data brings some problems. Firstly, not all
the data can be used. For the successful simulation of the control, the measured
data should be taken simultaneously. It is also useful when the individual measured
32


---

Page 45

---

3.2 Measured data
data vectors are sampled with the same sampling frequency. If this is not the case,
the data has to be extrapolated or re-sampled to obtain the same measuring times.
Another usual problem is missing some data. In the real-life measuring systems
the successful rate of measuring systems is nearly never 100%. The solution of this
problem might be once again the extrapolation.
In this specific case, the necessary data from bus 10 are not available. Instead of
it, there is a data vector measured on bus 8 which contains the sum of data from
bus 10 and 11. Therefore, this does not have to be considered as a problem. To get
the requested data from bus 10 we can simply subtract vector 11 from measured
vector 8.
The data selection aimed to find a period that is as long as possible with as fast
as possible sampling rate. From the given data, the period of 33 days between the
afternoons of 3.9.2017 and 4.10.2017 is chosen. Five of the measured nodes were
measured originally with sampling time 10 seconds, the other two were measured
faster, every 1 second. Therefore, they are re-sampled to the same frequency.
For this time interval, all the measured vectors should have a length equal to 268
976 samples. The description of the measured data is shown in Table 3.1:
Bus number
Name
Data length
Missing data [%]
3
SRS 131
268 669
0.11
5
SRS 204
268 908
0.03
6
N 149 464
268 976
0
7
N 115 765
268 923
0.02
8
N 149 403
237 120
11.84
11
N 140 359
267 530
0.54
12
N 106 160
265 381
1.42
Table 3.1: Table showing the amount of missing data in measured vectors
As it is clear from the rates of the missing data, there is no problem in the ex-
trapolation of the missing data for most of the measured vectors. Unfortunately,
the vector measured at bus number 8 is missing a significant amount of data, ap-
proximately 3 days.
Since it represents the summation of the data from PV farm and wind generator,
the vector is in the shape formed by PV farm data, it looks like a typical curve
highly dependent on the time of the day.
That is why in the control simulation, 3 days of data before the data gap are
multiplied once again behind it to fill the gap.
After this correction, the rest of the data is fixed applying the MATLAB function
fillmissing [46] that provides piecewise cubic spline interpolation. With this correc-
tion, the continuity of the data is preserved and measured vectors are extended to
the same length.
33


---

Page 46

---

3 Use Case
3.3 Other used data
Besides measured data on the test site, another data set is necessary for the control
algorithm. For the right settings of the cost function parameters, the price of energy
generated from individual sources during the measured period must be known.
Information about global energy prices are taken from the official database of Nord
pool energy market past data that are freely accessible through their web-page [47].
For the area of Sweden where Simris is located the day-ahead settlement energy
price is available every hour. Therefore, they have to be also extrapolated to the
desired sampling frequency.
The past price of the BUG fuel in Sweden in autumn 2017 can be also found on-line
[48]. The consumption of the BUG can be assumed to behave linearly concerning the
created power [49], hence computation of the energy price created by this method
is not complicated.
3.4 Reference control algorithm
For the comparison of the suggested control algorithm with a comparable control
structure, another control strategy that is utilizing BESS is needed. This additional
control approach is necessary to provide a reference rule-based control to manage
the BESS in the microgrid system.
Therefore, one of the simplest control approaches is created. The general idea
is to charge and discharge BESS between its limits with constant charging and
discharging power. Thus, the power from BESS would be in the form of the square
function over the time simulation, the BESS SoC would form the triangle function
and the battery pack would be utilized during all time steps.
The implementation of this control is done by simple relating of BESS cost func-
tion parameters to the global energy price. In the beginning, the cost of BESS is set
a little bit lower, given a fixed term. At the moment of reaching the BESS SoC limit,
the value is multiplied by -1 and the utilization of power from the battery pack turns
out to be more costly than from the main grid. When reaching the upper limit, the
value changes again its sign and the whole process is repeated.
In consideration of the BESS energy capacity, the described value is experimen-
tally chosen as 3 e/MWh. With these settings, one full equivalent battery cycle is
done in time duration approximately one day.
The SoC of BESS in the third week of the measured period between 18.9.2017 and
25.9.2017 is shown in Figure 3.2. It can be seen that the displayed function does
not completely follow the shape of the triangle function. This light differentiation
is caused by the influence of renewable sources and their variable production.
Nevertheless, this effect does not restrict the usability of the reference control.
Moreover, the later discharging in the case when the microgrid energy sources pro-
duce more power than needed is meaningful and simulates the real situation accord-
ingly.
34


---

Page 47

---

3.4 Reference control algorithm
Sep 19
Sep 20
Sep 21
Sep 22
Sep 23
Sep 24
Sep 25
Time
2017   
20
30
40
50
60
70
80
90
SoC [%]
BESS SoC
Figure 3.2: SoC of BESS during one week test with reference control
35


---

Page 48

---



---

Page 49

---

4 Modelling the Controller
As the main objective of the thesis, the control mechanism for the described system
in Chapter 3 is designed. The fundamental ambition of the controller is to provide
the economical optimality of the system during the power balancing of the grid.
The designed controller can be divided into two layers. In the bottom one, a dis-
tributed multi-agent system is used for the administration of the power distribution
between individual power sources. This control works at considerably high speed
and is executed every 10 seconds. Therefore, it represents a conventional secondary
control level.
This type of control is chosen due to its high process reliability, computation speed
and the ability of the system to react to eventual changes in the network topology.
Thanks to that, the system is an ideal control mechanism for finding the appropriate
power distribution ratio between power sources and it ensures the power balance.
However, this lower algorithm level aims only at providing optimal power distri-
bution from the theoretically infinite distributed sources. However, this does not
represent the real-life case and the sources are limited not only in rated power but
in the case of BESS in the power capacity as well.
This problem may lead to the exceeding of the output current from the sources,
which may prove to be very critical. Moreover, heavy discharging of the batteries
may strongly affect the process of ageing which is not desirable.
For these reasons, the upper level of control is implemented. The model predictive
controller considers all the constraints into consideration that the real-life systems
brings and additionally, it optimizes the charging and discharging processes on the
BESS.
Every 15 minutes, the future development of the battery pack state of charge is
predicted and the optimal control input is chosen accordingly. Hence, the MPC
controller represents the tertiary control in the traditional representation.
Employing this control configuration, the network operator can determine the
emphasis on the SoC of BESS or the price of the power received from the main
power grid.
Also, under consideration of forecasts for the distributed renewable
energy sources, the optimal charging and discharging in time of expensive power
price can be realized.
This brings to the system the necessary economical optimization and it enables
the grid operator to consume the locally generated green energy efficiently without
unnecessary wasting. These aspects are crucial for the usability of the microgrid
concept and its further deployment in the future.
37


---

Page 50

---

4 Modelling the Controller
4.1 Control structure
For the sake of MAS control, the physical system that is shown in Figure 3.1 has
to be divided into individual agents. This classification can be seen in Figure 4.1.
There are five agents representing energy sources. Agents 1, 7, 8, 9 and 10 stand for
connection to the main grid, BUG, BESS, wind generator and PV farm respectively.
Moreover, agents 9 and 10 represent the renewable sources and their power gener-
ation is highly requested. Therefore, it is reasonable to use all the generated energy
by them in every time step and to consider them as passive agents, that can not be
controlled.
Besides them, the system consists of five agents numbered 2 to 6 that repre-
sent power loads. Similarly to renewable sources, they are considered to be non-
controllable passive agents. Even though the agent 2 - Simris includes some ele-
ments of demand management, they will not be considered in this work due to their
low power capacity in comparison with the BESS. Nevertheless, they might prove
themselves to be very useful in other applications.
Figure 4.1: Agent representation of demonstration site situation
Hence, the created control uses only the power outputs of agent 1, 7 and 8 as the
active contribution to the system. The power outputs of the other agents are taken
as disturbances, that have to be covered by the active agents. The set of agents can
be divided into two subsets,
PA = {P1, P7, P8},
PP = {P2, P3, P4, P5, P6, P9, P10}.
For the distributed MAS control, the communication between agents is possible in
the way as it is shown in Figure 4.1. It is an example of topology communication
architecture as it was explained in Section 2.2.3, each agent can communicate only
with its direct physical neighbours.
All three active agents contain the information about the cost of the power that
they can generate and based on the ratio between these costs, the energy mismatch
of the network is distributed between active agents.
On the second control level, the MPC controller uses for the optimization of the
distributed process information of the BESS SoC and set its price to be the most
38


---

Page 51

---

4.1 Control structure
convenient for the overall system. By the set of control parameters, the emphasis
of the algorithm can be placed on the specific system features or used to solve the
trade-off between them.
This process does not aim to supplement the distributed algorithm, rather it
optimizes its operations by considering the BESS. The general design of the overall
control is shown in Figure 4.2.
Figure 4.2: General structure of control algorithm
The distributed MAS control is executed every 10 seconds. The current data of
power generation/demand of passive agents are summed up and cost function pa-
rameters are loaded to the individual active agents. Subsequently, by the distributed
consensus algorithm the power mismatch of the passive agents is taken care of by
optimal power distribution between the active agents.
For visualization in Figure 4.2, the individual cost parameters are summed up in
the vector c,
c =


a1
b1
a7
b7
a8
b8


=


c1
c2
c3
c4
c5
c6


.
Moreover, every 15 minutes the cost function parameters of the BESS are set by
the MPC controller and used for the period until the next MPC iteration.
For
the evaluation of the MPC, the cost function is built on current data and forecast
future time-steps. After that, the cost function is minimized and the optimal control
parameters are found.
39


---

Page 52

---

4 Modelling the Controller
4.2 Distributed MAS control
The consensus algorithm as a distributed MAS control solution is mentioned already
in several articles [9, 17, 16]. In general, the overall balancing problem is formulated
by equation (4.1),
X
i
PG,i +
X
m
PR,m = −
X
j
PL,j,
(4.1)
where the P
i PG,i represents all the overall generated power by conventional sources
as well as by the BESS, the P
m PR,m symbolizes the power generated by renewable
sources and finally, the P
j PL,j is the summation of the overall load demand. The
total generated power is divided into these two groups because distributed renewable
sources are considered as an uncontrollable input to the network.
The quadratic cost is assigned to each controllable source [16],
Ci(PG,i) = 1
2ai(PG,i)2 + bi(PG,i) + ci
(4.2)
with ai, bi, ci as cost parameters. By the distributed algorithm the summation of
these prices should be minimized to set the optimal ratio of the power distribution
between all active power sources,
min
X
i
Ci.
(4.3)
To find the minimum value of this problem, the first derivation of all cost functions
is needed,
ri = aiPi + bi.
(4.4)
Now, only the cooperation of all the agents on finding the common value of r is
necessary. This process can be done in a centralised manner. Since the load, as
well as the power generation from renewable sources, proved to be intermittent the
advantages of distributed control such as control speed, reliability, and the control
flexibility might be useful.
4.2.1 Weighted adjacency matrix
As was described in Section 2.2.3 the choice of the weighted adjacency matrix D of
grid communication is crucial for the speed of convergence of the algorithm. The
matrix D can not be designed completely randomly, all its elements must be non-
negative and summation of each row equal to one. Therefore, the following equations
(4.5) must hold,
D · e = e, DT · e = e, with e =


1
1
...
1


.
(4.5)
40


---

Page 53

---

4.2 Distributed MAS control
Matrix D is designed in this way is called the doubly stochastic matrix. According
to Perron-Frobenius Lemma [42], the eigenvalues of this matrix are less or equal
to 1 with one eigenvalue 1 and the limit value of the D matrix in infinity can be
computed by following equation,
J = lim
k→∞Dk = eeT
n ,
(4.6)
where n is the matrix dimension.
There are multiple approaches to how to get a weighted adjacency matrix for
the power system. Since the communication links between individual agents are
bidirectional, it makes sense to create matrix D which is symmetrical over the main
diagonal, therefore dij = dji. These elements dij of the matrix D represent the
coefficients of information exchange in the network.
The elements on the main
diagonal are then computed as a subtraction of all these elements in the row from
one. By this approach, the sum condition is ensured.
The most conventional approach to set the coefficients in the network is called
Uniform method. The elements of the D matrix are computed concerning the amount
of nodes in the overall network. The Uniform method rule is summarized in following
equation (4.7),
dij =







1
n,
j ∈Ni,
1 −P
j∈Ni
1
n,
i = j,
0,
otherwise,
(4.7)
where n is the amount of the nodes in the network. Even though the speed of the
convergence might be a little bit improved by adapting the algorithm to the specific
network, for this application it is sufficient. The simplicity of the application, as
well as stability guarantee, are also important advantages.
The final D matrix for the system that is shown in Figure 4.1 is expressed like
this
D =


















0.9
0.1
0
0
0
0
0
0
0
0
0.1
0.7
0.1
0.1
0
0
0
0
0
0
0
0.1
0.9
0
0
0
0
0
0
0
0
0.1
0
0.8
0.1
0
0
0
0
0
0
0
0
0.1
0.7
0.1
0.1
0
0
0
0
0
0
0
0.1
0.9
0
0
0
0
0
0
0
0
0.1
0
0.7
0.1
0.1
0
0
0
0
0
0
0
0.1
0.9
0
0
0
0
0
0
0
0
0.1
0
0.8
0.1
0
0
0
0
0
0
0
0
0.1
0.9


















.
(4.8)
4.2.2 Multi-agent system control constraints
The real system is limited by the set of control constraints.
Simple example of
these limitations can be the fact that the energy can not be drawn out from the
41


---

Page 54

---

4 Modelling the Controller
BESS when its SoC drops under pre-set limit or the physically impossible process
of charging the energy to the BUG.
In the consensus algorithm, all the constraints can be implemented with the same
approach. When any limit of active agent is exceeded, its initial consensus value
drops to zero and the produced power is set as a constant.
By this adjustment
the active agent is converted into the passive agent for this specific time-step, the
power mismatch in a microgrid is recalculated and the consensus algorithm iteration
process can continue.
The control constraints that are implemented into the algorithms can be seen in
Table 4.1:
Microgrid component
Constraint
Value
Li-Ion BESS
energy capacity
333 kWh
Minimal SoC
0.2
Maximal SoC
0.9
Maximal charge
1342.32 kW
Maximal discharge
839.02 kW
BUG
Maximal power
350 kW
Minimal power
0 kW
Table 4.1: Table of control constraints of MAS control
Moreover, supplying the generated energy from the microgrid to the main grid
is not allowed in the case when the BESS is not fully charged.
Thank to these
settings, the system is not selling the generated energy in situations when the energy
reserves are low. This precaution aims to prepare the microgrid for unexpected fault
situations better.
4.2.3 Update rules
The consensus algorithm for optimal power dispatch, as suggested in [16, 17, 9] is
expressed by the following three equations,
ri[k + 1] =
X
j∈Ni
dijrj[k] + ϵPD,i[k],
Pi[k + 1] = ri[k + 1] −bi
ai
,
PD,i[k + 1] =
X
j∈Ni
dij (PD,j[k] + (Pj[k + 1] −Pj[k])) ,
(4.9)
where the ri stands for optimal derivative of the cost (4.4) for agent i, ϵ is the con-
vergence step and PD,i refers to local estimate of power mismatch in the network,
see [17]. Algorithm (4.9) aims to determine consensus on variable r to which all in-
dividual ris converge. When there is no difference between ris in the entire network,
the algorithm terminates.
42


---

Page 55

---

4.2 Distributed MAS control
The rules (4.9) can be stated concisely in matrix form,
R[k + 1] = D · R[k] + ϵPD[k],
P[k + 1] = B · R[k + 1] + G,
PD[k + 1] = D · PD[k] + D · (P[k + 1] −P[k]),
(4.10)
where variables ri are arranged into a column vector R, as well as PD,i and Pi into
PD and P. The matrices B and G contain the relationship between cost parameters;
in the case of matrix B, they are located on the main diagonal in the form of 1
ai and
G is a column vector with components −bi
ai .
Furthermore, the dynamics of the whole distributed system can be examined in
the state-space representation. For that, the individual cost derivatives ri and PD,i
are taken as state variables. Therefore, the system matrix is defined by the following
equation,
"
R[k + 1]
PD[k + 1]
#
=
"
D
ϵI
DB(D −I)
D + ϵDB
#
·
"
R[k]
PD[k]
#
,
(4.11)
where I refers to the identity matrix. System (4.11) is found not to converge to a
steady-state consensus on at least some connected graph topologies [1]. This can be
elucidated by looking at the nominal system; (4.11) for ϵ = 0; having system matrix
"
D
0
DB(D −I)
D
#
.
(4.12)
The matrix (4.12) contains repeated eigenvalue set of matrix D and due to the
Perron-Frobenius Theorem the matrix D has the largest eigenvalue equal to 1 and
all other with magnitudes strictly less than that. The whole control can be seen in
the schematic diagram in Figure 4.3.
For D to have a single eigenvalue equal to 1, the graph must contain a spanning
tree. This is crucial for convergence of consensus algorithms. The ϵ−disturbance
generally does not vanish on the subspace pertaining to both 1 eigenvalues of (4.12).
This subtle fact invalidates the logic based on the robustness of the consensus algo-
rithm, as used in [16, 17, 9]. Namely, no ϵ > 0 can generally be found small enough
to ensure convergence.
4.2.4 Algorithm implementation
The necessary information for the algorithm implementation is the cost function
parameters of agents 1, 7 and 8.
Since that the costs of agent 1 and 7 depend
linearly on the created power, the a coefficients are set very low, a1 = a7 = 0.001.
For the connection to the macrogrid, the real data are taken from the historical
data of the official web-page of the Nord pool as it was introduced in the previous
chapter.
For the back-up generator, the comparison with energy price from the main grid
is used and BUG energy is assumed to be approximately 10 times more expensive.
43


---

Page 56

---

4 Modelling the Controller
Figure 4.3: Schematic diagram of the distributed MAS control [9]
Therefore, the cost parameter of BUG is set to ten times higher value for the
whole simulation, b7 = 10 · b1. This should not influence the simulation because
the BUG is meant to be used only occasionally, in moments when microgrid control
collapses. This is not the topic of this work and it will not be further examined.
Now, we have two cost function parameters of the BESS which can be used to in-
fluence the ratio of the power distribution. Unfortunately, optimizing of two param-
eters with quite tightly bounded relation can be very complex and computationally
demanding. Moreover, the a8 parameter is only setting the sensitivity of the final
ratio on the related b parameter. With the unlimited precision of parameter setting,
it can be considered constant. Therefore, the parameter a is set to the following
value, a8 = 0.1.
Convergence issues of the cooperative algorithm mentioned in the previous section
motivate the development of a modified control protocol which does not suffer from
these problems.
44


---

Page 57

---

4.2 Distributed MAS control
At first, the solution by rescaling the whole lower part of the system matrix to
shrink the Gerschgorin’s disks of the respective eigenvalues inside the unit circle was
tried. Unfortunately, this solution solved the stability problem, but also drastically
changed the whole dynamics of the system.
Other tested solution was the attempt to change the matrix D in the way that
it would solve the stability issues.
Unfortunately, the D matrix must fulfil the
requirements for the stochastic matrix and therefore it can not be changed in the
way in which D + ϵDB is not doubly stochastic as well.
The solution was found eventually [1]. By scaling the lower right block of the
system matrix (4.11) by a positive scalar factor α < 1, the system (4.15) converges
to steady-state consensus in ris. The single agent’s update rules are given as,
ri[k + 1] =
X
j∈Ni
dijrj[k] + ϵPD,i[k],
Pi[k + 1] = ri[k + 1] −bi
ai
,
PD,i[k + 1] =
X
j∈Ni
dij (αPD,j[k] + (Pj[k + 1] −Pj[k])) ,
(4.13)
for 0 < α < 1. In matrix form this reads,
R[k + 1] = D · R[k] + ϵPD[k],
P[k + 1] = B · R[k + 1] + G,
PD[k + 1] = αD · PD[k] + D · (P[k + 1] −P[k]).
(4.14)
The adjusted system can be represented by the following state-space dynamics,
"
R[k + 1]
PD[k + 1]
#
=
"
D
ϵI
DB(D −I)
αD + ϵDB
#
·
"
R[k]
PD[k]
#
.
(4.15)
Theorem 1 (Proposed algorithm). For any 0 < α < 1 the system (4.15) converges
to the span
h
1T
0
iT on arbitrary graph topologies containing a spanning tree, given
ϵ > 0 is sufficiently small.
Proof. For 0 < α < 1, the nominal system matrix
Anom =
"
D
0
DB(D −I)
αD
#
(4.16)
has a single eigenvalue 1 with eigenvector
h
1T
0
iT ; all other eigenvalues of (4.16)
have absolute value strictly less than 1. Hence, the second-largest nominal system
eigenvalue satisfies λ<1(Anom) = max(λ<1(D), α) < 1.
The ϵ−perturbation vanishes on span
h
1T
0
iT for ∀ϵ > 0
ϵAd
"
1
0
#
:= ϵ
"
0
I
0
DB
# "
1
0
#
= 0.
(4.17)
45


---

Page 58

---

4 Modelling the Controller
For convergences of the original system (4.15) to the span
h
1T
0
iT the second
largest eigenvalue of the system (4.15) needs to satisfy
|λ<1(Anom + ϵAd)| < 1.
(4.18)
As one has,
|λ<1(Anom + ϵAd)| ≤|λ<1(Anom)| + ϵ|λ(Ad)|
(4.19)
(4.18) is certainly satisfied for
ϵ < 1 −|λ<1(Anom)|
|λ(Ad)|
,
(4.20)
giving an upper bound on ϵ to fulfil the condition (4.18).
The obtained system has the same properties as a leaderless consensus algorithm,
according to [7]. The final iterated value of the consensus variable r depends only on
the initial values of ris. Since the amount of produced or used power is known, this
information can be distributed through the network to compute the power mismatch
in the grid. This is required for determining the optimum controller’s initial values
as well as the cost functions.
This is different from the protocol described in [16, 17, 9]. A few hundred iterations
are needed for finding the consensus value but the required distribution of the data
through the network is done very quickly.
That is a price to pay for having a
stabilized system with perfectly deterministic behaviour. The algorithm retains all
the advantages of distributed solutions such as lower complexity, reliability, and
security and it is guaranteed to converge on arbitrary graph topologies containing a
spanning tree.
Moreover, the distributed multi-agent system (MAS) consensus algorithm can also
be initialized with partially known data. That speeds up the initial reaction of the
controller, which might be useful in case of a rapidly changing environment typical
for RES microgrids. The iteration process of the consensus algorithm on consensus
values r can be seen in Figure 4.4.
4.3 Model predictive control
The second level of control is embedded by the centralised MPC controller to mini-
mize the costs of energy imported from the macrogrid (negative number stands for
selling energy) and optimize the BESS SoC by keeping it on a 50% level.
As it was explained in Section 2.3, this type of controller requires a model of
the system and prediction of the system disturbances, in this case in the form of
microgrid power mismatch and future global energy price.
Besides that, the cost function needs to be rightly set and weighted to find the
optimal trade-off between both observed values. It has to also take all kinds of the
restriction and limitation of the system into consideration.
46


---

Page 59

---

4.3 Model predictive control
50
100
150
200
250
300
Iterations
-50
-40
-30
-20
-10
0
10
r [-]
Agent 1
Agent 2
Agent 3
Agent 4
Agent 5
Agent 6
Agent 7
Agent 8
Agent 9
Agent 10
Figure 4.4: Consensus algorithm iteration for one time step
As was said in the introduction to this chapter, the MPC control is executed
once every 15 minutes and it sets the cost function parameters of the BESS for the
following 15 minutes. Hence, the 90 cycles of the first layer control are performed
during one step of the MPC controller.
4.3.1 Designed model
Naturally, the most relevant variable of the BESS is its SoC. Nevertheless, for the
computation reasons the energy with which is the battery pack charged will be used
as a state variable. Thanks to that the state space equation stays significantly less
complex. With the knowledge of the maximum energy capacity of the BESS, it is
simple to convert this value to needed SoC. The battery energy is held in kWh.
The state equation of the BESS energy can be expressed by equation (4.21),
x[k + 1] = x[k] −r −b8
4a8
,
(4.21)
where r is the optimum cost that was found by consensus algorithm and a8 with
b8 are cost parameters of agent 8 - BESS. Since the MPC operates only every 15
minutes the new capacity is computed as if the power distribution between individual
agents stays the same as in the time-step k for the whole time. The factor of 1
4 in
this equation is caused by the recalculation of the used energy to kWh.
The calculation of the variable r is done from the known mismatch in the network
and active agent’s cost function parameters. In our specific case, it can be written
in the following manner,
r = −s + b1
a1 + b7
a7 + b8
a8
1
a1 + 1
a7 + 1
a8
,
(4.22)
47


---

Page 60

---

4 Modelling the Controller
where s is the network power mismatch and parameters a and b refer to agent 1 -
PCC, agent 7 - BUG and agent 8 - BESS based on their identification numbers. In
case that the s is not known for the computed time step, its estimation ^s might be
used.
The probability of the real power distribution staying completely constant for 15
minutes is very low. After all, there are 90-time steps in which the distribution ratio
can be changed. This model configuration is given an estimate that is showing what
capacity would be available in the next MPC time step.
With consideration of all these model settings, the state equation (4.21) has two
uncontrollable inputs s and b1 and controllable b8 which is used for MPC control.
4.3.2 Data forecast
To obtain the necessary data forecast the regression analysis on provided data is
utilized. Both of the predicted data sequences, energy prices, and power mismatch,
show high dependency on the time of day when they were measured. Unfortunately,
that is not the only relationship among data that can be observed. From the mea-
sured datasets, it is clear that the individual days are not completely independent.
Firstly, the Gaussian process regression model is used to estimate future data.
Even though some dependencies between data are preserved, the predicted model
stayed constant for all days and the amplitudes of the data vector are very different.
Therefore, this estimated model did not correspond well with reality.
The non-stationarity between days had to been added to the model. For this
problem, the typical regression solution of econometrics is used. The seasonal au-
toregressive integrated moving average (SARIMA) model estimates the relationships
among variables by autoregressive method, it takes defined previous known data to
forecast the future ones.
The name of the algorithm is composed of three parts. Autoregression represents
the fact that the model is finding dependencies between previously known or own
lagged data.
The word integrated stands for the fact, that the individual time
series values are converted into the differences between the two following time steps.
Thanks to that, the time series becomes stationary.
Finally, the moving average refers to the relationship between regression error of
the previous data and the individual observations by computing their linear combi-
nation. The computed variable is then minimized by any minimizing algorithm. In
the following implementation, the minimized mean square error (MMSE) algorithm
is used.
Moreover, the model adaptation SARIMA can add the pattern between data that
repeats itself. In this case, the repeating pattern every 96-time steps (one day) can
be easily observed on the measured data.
After setting up the described model, the prediction results are very satisfying in
comparison with Gaussian process model. The prediction of the one full day after
learning on 7 days data can be seen in Figure 4.5 also with a 95% forecast probability
of the MMSE algorithm.
48


---

Page 61

---

4.3 Model predictive control
The SARIMA model is implemented by MATLAB build-in function arima [50]
and its parameters are chosen by Econometric Modeler App. This application is a
part of the same program and provides to a user a way to choose the right settings
for given data.
Sep 04
Sep 05
Sep 06
Sep 07
Sep 08
Sep 09
Sep 10
Sep 11
Sep 12
Time
2017   
0
10
20
30
40
50
60
70
80
Observed energy price
MMSE price forecast
95% MMSE forecast intervals
Figure 4.5: One-day prediction of global energy prices by an estimated SARIMA
model
The performance of the prediction algorithm shows quality approximation all
over predicted 96-time steps. Taking into account the fact, that the MPC predictive
horizon will not be that long in the implemented program, the behaviour of the
forecast algorithm is completely sufficient.
The graph of real data, one step prediction (15 minutes) and 24 steps prediction (6
hours) on the dataset of 5 days between 11.9.2017 and 16.9.2017 for both microgrid
mismatch and global energy prices are shown in Figures 4.6 and 4.7, respectively.
The performance of short, one step prediction is very functional and the predic-
tions are tracking the real data very tightly. It can be seen that the long prediction,
as 6 hours prediction is, reacts late to large steps in the real data curves. In the
case of power mismatch in the microgrid, the long prediction shows obvious draw-
backs and the performance of the MPC algorithm could be strongly influenced by
inaccurate prediction. On the other hand, in the case of global energy price data,
the real data curve is quite seasonal and significantly more predictable than power
mismatch. That is the reason why this long prediction also tracks the reality better
and can be used in the algorithm deployment.
49


---

Page 62

---

4 Modelling the Controller
Sep 12
Sep 13
Sep 14
Sep 15
Sep 16
Time
2017   
-400
-200
0
200
400
600
800
Power [kW]
Power mismatch
Predicted mismatch for 24 steps
Predicted mismatch for 1 step
Figure 4.6: Prediction of microgrid mismatch compared with real data on one week
dataset
Sep 12
Sep 13
Sep 14
Sep 15
Sep 16
Time
2017   
20
25
30
35
40
45
50
55
60
Real global energy price
Predicted price for 24 steps
Predicted price for 1 step
Figure 4.7: Prediction of global energy price compared with real data on one week
dataset
50


---

Page 63

---

4.3 Model predictive control
4.3.3 Cost function
As was mentioned in Section 2.3.1 the right selection of the cost function and its
parameters by network operator is crucial for providing the required control perfor-
mance.
The cost function in the controller implementation is chosen in a little bit different
style that was presented in equation (2.5).
Implemented cost function is in the
following form (4.23),
V (b8) = Q
Tp
X
k=1
h
E
2 −^x[k](b8)
i2 + R
Tp−1
X
t=0
h
^b1[t] · r[t](b8)−^b1[t]
a1
i
,
(4.23)
where E stands for maximal energy that can be stored in the BESS. In the compu-
tation of the current time-step of the second term, the real system state x[k] is used
instead of its prediction ^x[k] similarly as the real power price coefficient b1. In the
following prediction steps, the system variable prediction is computed by using data
forecast.
In the implementation, the control horizon is set to the same value as the predictive
horizon. This decision is made due to the fact, that the future evolution of this
specific system continues on a trajectory that is penalized according to future states
and control efforts necessary for moving between them.
The cost function is the subject of minimization of dependency on only one vari-
able. By this simplification, the whole process of minimization becomes computa-
tionally easier, less complex and faster.
The first part of the cost function sets the price of distance of the BESS charged
energy from 50% of battery capacity. With every deviation by which the stored
energy differs from the middle of capacity, the cost of this part of the equation
grows quadratically. This value is multiplied by its coefficient Q.
The second part of the equation expresses the price of power delivered to the
microgrid through the PCC and it is weighted by coefficient R. This equation term
is linear because of the possibility of supplying energy back to the main grid which
is expressed by its negative cost. With the right settings of two coefficients R and
Q, the importance of each phenomenon is set and the trade-off between them is
optimally balanced.
When the function reaches a steady-state, the optimal values of b8 for future Tp
steps are found. From this created control sequence the first control input is taken
and applied to the system. The rest is discarded and the whole process is repeated
in the following time step.
4.3.4 Prediction constraints
For the quality and meaningful prediction of the system’s future behaviour, it is
necessary to constrain the system state into which the model can get in the future
steps. Since the price of energy from the main grid is not limited, the second term
of cost function (4.23) can be minimized as it is.
51


---

Page 64

---

4 Modelling the Controller
On the other hand, that is not the case for its first term.
The limitations of
BESS are presented in the previous Table 4.1 and it would not make sense for
the MPC algorithm to take the future states with SoC outside of these limits into
consideration.
52


---

Page 65

---

5 Exemplary Results
In the last part of the thesis, the performance of the implemented control algorithm
is evaluated on measured data. The parameters are chosen for economical evaluation
as well as for the measurement of the BESS utilization.
The control results are simulated in several tests. First, the control algorithm
results are compared depending on the setting of the control parameters, the ratio
between MPC cost function Q and R and the length of the predictive horizon. Each
control settings is used on data from multiple days to validate its repeatability.
In the second part, the simulation results of the proposed algorithm are shown
compared with the reference control algorithm as well as with the situation of mi-
crogrid without distributed ESS.
5.1 Evaluation metrics
To provide a complex evaluation of the algorithm performance, multiple independent
evaluation metrics are used to ensure objectivity. All observed measured features
can be divided into 3 groups, metrics considering economical aspects of the simulated
results, metric regarding power exchange with the main grid and metric of the BESS
performance.
5.1.1 Economical metrics
The evaluation of the control algorithm based on the economical results can be
considered as the most important aspect for its theoretical future deployment. Al-
gorithm, that confirms its benefit by lowering of total variable costs provides to the
system authorities strong reasoning for its utilization in the microgrid as well as the
expected profitability of the project.
In the upcoming simulations, the total cost of the energy drawn from the main
grid will be computed.
Similarly, the assumption of selling energy back to the
macrogrid by the same actual price is made and total revenues from energy trades
are estimated. The earnings made by selling energy are taken as negative costs.
At the end of the test, these two values are summed up and the total flexible
cost of the control algorithm use is determined. For the sake of better comparison
between multiple tests of different lengths, the average cost of energy per day is also
added.
Due to the expected high dependency of total costs on power mismatch during the
test period, the comparison with other control algorithms is executed on the same
53


---

Page 66

---

5 Exemplary Results
data. Therefore, the simulation of the control without distributed ESSs is carried
out as well as the reference control presented in Section 3.4.
The differences between these two approaches are described by absolute cost re-
duction in Euros and relative cost reduction. Analysis of these value is the most
relevant for the assessment of the suggested algorithm functionality.
5.1.2 Power exchange metrics
The second group of used measuring metrics takes the exchange of energy with the
main grid through the PCC into consideration. The total amount of energy drawn
from the main grid in kWh, as well as the total quantity of created energy that is
supplied to the macrogrid, are measured.
5.1.3 BESS metrics
The last category of proposed measuring metrics evaluates the performance of the
algorithm regarding processes on the BESS. The battery processes can be examined
for several different reasons.
In case of including of BESS into microgrid, it is reasonable to utilize it whenever
the conditions are appropriate. Deployment of BESS represents a quite large fixed
cost of the system which has to be taken care of by revenues of the system. In the
case of intermittent usage of the BESS, the expense of integrating it into the system
might become unreasonable.
This BESS feature can be observed through multiple parameters. During the tests,
the charged and discharged energy to the batteries are measured and the equivalent
full battery cycles are computed from the individual charging and discharging se-
quences. The amount of full equivalent cycles is then averaged to find comparable
value of one-day utilization.
Another important aspect of BESS is the process of ageing. Even though the
process of ageing of lithium-ion (Li-ion) batteries is unavoidable, some processes are
more convenient for the battery pack than others. For example, the often cycling of
the batteries as well as high charging and discharging currents are strongly unwanted.
As can be seen, the required utilization of Li-ion batteries is not straight forward
and the final decision must be done by a microgrid operator.
5.2 Simulation results
All simulated tests are done on the previously described microgrid solution data
using a suggested control algorithm with different settings of control parameters.
The control performance is tested on multiple day sequences from measured data.
For the successful use of the SARIMA models introduced in Section 4.3.2, previ-
ously known measured values are required. Therefore, the first week is not used for
testing and due to that, at least seven days are always used for training of SARIMA
model.
54


---

Page 67

---

5.2 Simulation results
For the possibility of result comparison, the simulation of the system with the
reference control, as well as the simulation of the system without BESS, are executed.
The total costs of the system controlled by these algorithms are measured.
During all simulations shown in this chapter, the following conventions are used.
Energy drawn from the main grid is taken as positive and energy supplied to the
main grid as negative. The same convention also applies to powers. In the case of
energy prices, the positive values represent bought energy and negative sold one.
Lastly, the comparison done with the reference control in positive values shows that
the suggested control algorithm is more advantageous.
5.2.1 Control parameters settings
Necessary control parameters, the ratio between parameters of the MPC cost func-
tion Q and R, as well as the predictive horizon h, are set based on performed tests.
Q/R ratio
The same control algorithm settings are applied on multiple control settings with
only difference in the ratio of Q and R parameters. The test is performed twice on
two different datasets to ensure the correct settings.
Simulation 1 - 3 days between 18.9.2017 and 20.9.2017
The results of simulation
for both reference systems are the following:
• System without BESS
C1 = −32.23 e
• Reference control
C2 = −33.65 e
#
MPC settings
Power exchange results
h
Q
R
Etot,in[kWh]
Etot,out[kWh]
Ctot,in[e]
Ctot,out[e]
Ctot[e]
1
24
5
1
4391.29
-5274.90
173.02
-216.89
-43.88
2
24
1
1
4377.94
-5337.82
171.59
-219.97
-48.38
3
24
1
2
4387.00
-5347.51
171.57
-220.42
-48.85
4
24
1
3
4366.48
-5326.92
170.77
-219.44
-48.67
5
24
1
5
4379.32
-5339.85
171.44
-220.07
-48.63
Table 5.1: Table showing MPC settings and power exchange results of Simulation 1
The performance of the implemented algorithm can be seen in Tables 5.1 and
5.2. The columns of Table 5.1 refer to test number, predictive horizon h, control
parameter Q, control parameter R, total energy drawn by the microgrid Etot,in,
55


---

Page 68

---

5 Exemplary Results
#
BESS results
Comparison
Etot,char[kWh]
Etot,dis[kWh]
EFC
EFC
Cr,1[e]
Cr,1[%]
Cr,2[e]
Cr,2[%]
1
2130.41
-2159.08
9.14
3.05
11.65
36.15
10.23
30.40
2
1954.27
-2053.07
8.38
2.79
16.15
50.10
14.73
43.76
3
1932.32
-2031.72
8.29
2.76
16.62
51.56
15.20
45.16
4
1920.17
-2019.52
8.24
2.75
16.44
51.01
15.02
44.64
5
1724.44
-1823.83
7.39
2.47
16.41
50.90
15.02
44.52
Table 5.2: Table showing BESS processes results and comparison with reference
algorithms of Simulation 1
supplied to the main grid Etot,out, total cost of drawn energy Ctot,in, total cost of
supplied energy Ctot,out and summation of these two costs (left to right).
The individual tests are refereed by the same number in Table 5.2. The other
columns represent total energy deposited into the BESS Etot,char, total energy dis-
charged from BESS Etot,dis, amount of equivalent full cycles EFC, day-average of
equivalent full battery cycles, comparison with the first reference control in Euros
and in percentage Cr,1 and same comparison with second reference architecture Cr,2
(left to right).
Based on the Simulation 1 results, the control settings in test 3 turned out to be
the one with the highest relative cost comparison. This setting is used in the full test
at the end of this chapter. It can be also observed that with the growing emphasis
on the BESS SoC the utilization of BESS also increases. This fact can be seen in
the part of Table 5.2 BESS results. It is worth noting that the energy exchange with
the main grid does not depend on this feature.
To make sure that the selected parameters are providing the most advantageous
control, a similar test is done for the next 3 days.
56


---

Page 69

---

5.2 Simulation results
Simulation 2 - 3 days between 21.9.2017 and 23.9.2017
The results of simulation
of both reference systems are the following:
• System without BESS
C1 = 383.00 e
• Reference control
C2 = 377.86 e
The performance of the implemented algorithm can be seen in Tables 5.3 and 5.4.
#
MPC settings
Power exchange results
h
Q
R
Etot,in[kWh]
Etot,out[kWh]
Ctot,in[e]
Ctot,out[e]
Ctot[e]
6
24
1
1
10260.62
-206.54
379.31
-9.29
370.02
7
24
1
2
10195.22
-161.25
376.29
-6.92
369.37
8
24
1
3
10243.15
-232.69
380.17
-10.21
369.97
Table 5.3: Table showing MPC settings and power exchange results of Simulation 2
#
BESS results
Comparison
Etot,char[kWh]
Etot,dis[kWh]
EFC
EFC
Cr,1[e]
Cr,1[%]
Cr,2[e]
Cr,2[%]
6
3748.90
-3753.24
16.08
5.36
12.99
3.39
7.84
2.08
7
3943.91
-3966.76
16.91
5.64
13.64
3.56
8.49
2.25
8
3638.75
-3683.22
15.61
5.20
13.04
3.40
7.89
2.09
Table 5.4: Table showing BESS processes results and comparison with reference
algorithms of Simulation 2
Also, the results from the Simulation 2 show that the most convenient ratio be-
tween Q and R is 1:2. It would be possible to find the optimal Q/R ratio even more
precisely by executing other tests with values close to the chosen ratio. However,
the results do not differ that much from each other so the small adjustment of the
ratio would not have appreciable added value.
The dependency of the BESS utilization on Q parameter is not that obvious in
results from the Simulation 2, which can be caused by inaccuracies of individual
final values of distributed MAS system iterations.
It is also very convenient that during these 3 days the production of distributed
generators is lower than in the case of Simulation 1 and the total cost of the system is
also quite large. The fact that the best results are once again generated by simulation
with this Q/R ratio, represents very useful observation about the microgrid system.
The mentioned Q/R ratio will be used from now on.
57


---

Page 70

---

5 Exemplary Results
Predictive horizon h
The optimal predictive horizon h is found similarly.
Unfortunately, the tests of
the predictive horizon turn out to be affected by the prediction error. Therefore,
the longer simulations are chosen to distribute the error between more program
iterations and to find the optimal predictive horizon value.
Same as before, two tests are executed on two seven day-long datasets in the
second and third week of the measured data.
Simulation 3 - 7 days between 18.9.2017 and 25.9.2017
The results of simulation
for both reference systems are the following:
• System without BESS
C1 = 334.07 e
• Reference control
C2 = 329.49 e
The performance of the implemented algorithm can be seen in Tables 5.5 and 5.6.
#
MPC settings
Power exchange results
h
Q
R
Etot,in[kWh]
Etot,out[kWh]
Ctot,in[e]
Ctot,out[e]
Ctot[e]
9
3
1
2
15369.77
-6410.57
561.11
-254.91
306.20
10
4
1
2
15414.75
-6455.55
562.58
-256.80
305.78
11
5
1
2
15390.76
-6431.54
561.59
-255.75
305.84
12
8
1
2
15366.52
-6407.27
561.04
-254.63
306.40
13
12
1
2
15522.10
-6562.91
570.49
-262.47
308.02
Table 5.5: Table showing MPC settings and power exchange results of Simulation 3
#
BESS results
Comparison
Etot,char[kWh]
Etot,dis[kWh]
EFC
EFC
Cr,1[e]
Cr,1[%]
Cr,2[e]
Cr,2[%]
9
5109.52
-4976.33
21.35
3.05
27.87
8.34
23.09
7.01
10
5487.90
-5354.71
22.97
3.28
28.29
8.47
23.71
7.20
11
5351.70
-5218.50
22.39
3.20
28.23
8.45
23.65
7.18
12
5719.19
-5585.99
23.96
3.42
27.67
8.28
23.09
7.01
13
5704.23
-5571.04
23.90
3.41
26.06
7.80
21.47
6.52
Table 5.6: Table showing BESS processes results and comparison with reference
algorithms of Simulation 3
58


---

Page 71

---

5.2 Simulation results
Simulation 4 - 7 days between 25.9.2017 and 2.10.2017
The results of simulation
of both reference systems are the following:
• System without BESS
C1 = −336.72 e
• Reference control
C2 = −338.90 e
The performance of the implemented algorithm can be seen in Tables 5.7 and 5.8.
#
MPC settings
Power exchange results
h
Q
R
Etot,in[kWh]
Etot,out[kWh]
Ctot,in[e]
Ctot,out[e]
Ctot[e]
14
4
1
2
3558.68
-13686.14
112.77
-455.10
-342.34
15
5
1
2
3572.31
-13696.30
113.19
-455.61
-342.41
16
6
1
2
3969.89
-14076.84
125.76
-467.16
-341.40
17
8
1
2
3585.21
-13681.16
113.62
-455.08
-341.47
Table 5.7: Table showing MPC settings and power exchange results of Simulation 4
#
BESS results
Comparison
Etot,char[kWh]
Etot,dis[kWh]
EFC
EFC
Cr,1[e]
Cr,1[%]
Cr,2[e]
Cr,2[%]
14
2601.98
-2700.25
11.16
1.59
5.62
1.67
3.44
1.02
15
2653.97
-2749.05
11.39
1.63
5.69
1.69
3.51
1.04
16
2533.37
-2612.70
10.87
1.55
4.68
1.39
2.50
0.74
17
2673.59
-2742.90
11.47
1.64
4.75
1.41
2.57
0.76
Table 5.8: Table showing BESS processes results and comparison with reference
algorithms of Simulation 4
In comparison with previous simulation to set Q/R ratio, these two tests for
predictive horizon did not come up with the same optimal value. Unlike the ratio,
the predictive horizon has to be set as an integer.
In Simulation 3 the optimal
predictive horizon turned out to be equal to 4, in Simulation 4 h is equal to 5.
Therefore, both of them will be used in the future simulation of the whole dataset.
On the other hand, the relative cost reductions are very similar for both predictive
horizon settings so this adjustment is not expected to change the results significantly.
The found values correspond with prediction time 1 hour and 1 hour and 15 min-
utes respectively. The fact that the optimality is found in such a short predictive
horizon can be considered very convenient because with longer predictive horizon
the MPC cost function starts to be quite complex and its minimization very com-
putationally demanding.
59


---

Page 72

---

5 Exemplary Results
It should be noted that the utilization of BESS is growing with longer prediction.
Also, it is evident that the algorithm brings significant cost reduction when the
energy production of the renewable sources in the microgrid is lower than energy
demand for most of the time.
5.2.2 Simulation of complete data
Finally, the long-time period of 21 days between 11.9.2017 and 2.10.2017 is simulated
with the previously found ratio Q/R = 1 : 2 and multiple predictive horizons. Once
again, the results of simulation of both reference systems are the following:
• System without BESS
C1 = −580.60 e
• Reference control
C2 = −599.88 e
The final results can be seen in Tables 5.9 and 5.10.
#
MPC settings
Power exchange results
h
Q
R
Etot,in[kWh]
Etot,out[kWh]
Ctot,in[e]
Ctot,out[e]
Ctot[e]
17
3
1
2
25014.99
-40496.07
873.06
-1506.98
-633.92
18
4
1
2
25131.73
-40613.60
868.55
-1502.93
-634.38
19
5
1
2
25143.78
-40624.68
874.08
-1507.48
-633.40
20
6
1
2
25445.41
-40926.99
884.32
-1517.01
-632.69
Table 5.9: Table showing MPC settings and power exchange results of complete simulation
#
BESS results
Comparison
Etot,char[kWh]
Etot,dis[kWh]
EFC
EFC
Cr,1[e]
Cr,1[%]
Cr,2[e]
Cr,2[%]
17
10457.00
-10555.42
44.86
2.14
53.31
9.18
34.04
5.67
18
10050.65
-10149.81
43.12
2.05
53.77
9.26
34.5
5.75
19
10290.51
-10388.76
44.15
2.10
52.80
9.10
33.52
5.59
20
10228.71
-10327.54
43.88
2.01
52.01
8.97
32.81
5.47
Table 5.10: Table showing BESS processes results and comparison with reference
algorithms of complete simulation
From the measured data, it is evident that during this period the distributed
generators are producing significant amount of energy. Despite the unfavourable
conditions of the microgrid, the algorithm proved to be useful with relative cost
reduction of approximately 9% and 5.75% compared to the reference system without
BESS and reference control system, respectively.
60


---

Page 73

---

5.2 Simulation results
In average, the utilization of the BESS is relatively high. With two full equivalent
full cycles per day, the installation of BESS into the microgrid is justified. With
the cost reduction, roughly 60 e in only one month promises returns on initial
investment into battery technology.
The cost reduction of approximately 40 e per month compared to the reference
control architecture shows that the control algorithms of microgrid network can
provide a very interesting method of cost reduction or even revenue creation for the
deployed microgrids.
61


---

Page 74

---



---

Page 75

---

6 Conclusion
The main aim of this thesis was to design a multi-agent model predictive control
algorithm for microgrid architectures that would optimize its energy management.
The thesis fulfilled all the assigned tasks. After the general introduction to the
topic, the current state-of-the-art microgrid concept as an energy grid solution is
given in detail. Subsequently, the structure of common control strategies for micro-
grids as well as a model predictive control concept are presented.
In the second half of the thesis, the specific use case in southern Sweden is de-
scribed, completed by the description of pre-processing methods applied to the mea-
sured data.
Besides that, the reference control architecture for a representative
comparison of the designed control results is presented.
In Chapter 4 the designed control architecture was presented. The control al-
gorithm was implemented in two levels to maximize the utilization of two control
approaches distributed MAS control and MPC.
The consensus algorithm is implemented as a type of distributed MAS control.
This algorithm ensures the power balance in the microgrid based on power distribu-
tion between active nodes that represent controllable energy sources. The optimal
ratio is found, based on the minimum total cost of the generated energy that is de-
termined iteratively by communication of the consensus variable between individual
agents.
On the other hand, the MPC control is aiming to set the parameters of the BESS
cost function to provide optimal economical results valid for the simulation time
horizon. The future states are forecast using SARIMA model prediction and the
MPC cost function puts into relation the cost of future states of BESS with the cost
of future energy exchange with the main grid. After then, the resulting equation is
minimized with respect to BESS cost function parameter.
The designed control is subsequently tested on the a priori prepared datasets and
the results analysed by several evaluation metrics examining different aspects of the
control, such as BESS utilization in equivalent full battery cycles or energy exchange
with the main grid.
The evaluated results clearly show that the proposed algorithm reacts to the
changes of its control parameters. Different parameter settings were tested by sim-
ulations on independent datasets from time intervals of 3 weeks and the most con-
venient parameter set was found.
Finally, the control with the optimal parameter set is applied to the whole dataset.
Also, this finally selected test reveals relative system cost reduction of up to approx-
imately 6% compared to the reference control mechanism.
63


---

Page 76

---

6 Conclusion
From the provided simulation several dependencies are observable. Firstly, the
control parameter Q which sets the emphasis on the BESS SoC changes the uti-
lization of the battery pack significantly. The same effect is observed during the
extension of the control parameter predictive horizon. Therefore, the changes of
these parameters can be used when the BESS is not utilized adequately.
The second important conclusion of the simulation results is the dependency of
the relative cost reduction on the difference of absolute values of energy supplied and
drawn from the main grid. When the total algebraic sum of the energy exchange is
low, the algorithm proves to be more profitable.
This feature of the control algorithm can be explained by the general control idea.
The MPC controller is trying to postpone the purchase or sale of energy from the
main grid according to global price data with the utilization of the BESS. In case of
a large difference between absolute values of Etot,in and Etot,out, the algorithm has
a limited range and the algorithm’s profitability is decreasing.
There are several possibilities to improve the suggested control algorithm in future
work. The consensus algorithm suffers from the requirement to set initial conditions
for iteration. One possible approach to improve the algorithm is to iteratively search
for the optimal initial conditions depending on power deficit or surplus of individual
agents. Adjusting all agent’s initial consensus values, the optimal final consensus
value could be found and the necessary communication could be reduced.
Another suggested improvement of the algorithm is the adaptation of the BESS
ageing process into the MPC objective function to minimize system cost. Li-ion bat-
teries ageing is a very complex process depending on many factors such as charging
and discharging currents, depth of discharge, median of BESS SoC or the temper-
ature of the pack. With the careful extension of the cost function to include these
factors, an optimal process considering the batteries ageing could be reached.
In general, the results of the proposed control architecture appear to be very
promising. The designed algorithm can create a notable cost reduction which proves
to be a strong argument for its selection for any future microgrid solution.
However, the implementation would require an existing communication infras-
tructure to enable multi-agent consensus. Thus, future work could also focus on de-
termining a trade-off between communication extension to unfold advanced control
mechanisms, in comparison to a reference control scheme with no communication.
64


---

Page 77

---

Bibliography
[1]
P. Elis et al. “Multi-agent MPC protocol for microgrid energy management
and optimization”. Submitted for consideration on IFAC conference, Berlin
2020.
[2]
Nikos Hatziargyriou. Microgrids: architectures and control. John Wiley & Sons,
2014.
[3]
Magdi S Mahmoud. Microgrid: advanced control methods and renewable energy
system integration. Elsevier, 2016.
[4]
T. L. Nguyen et al. “Agent based distributed control of islanded microgrid
— Real-time cyber-physical implementation”. In: 2017 IEEE PES Innovative
Smart Grid Technologies Conference Europe (ISGT-Europe). 2017, pp. 1–6.
doi: 10.1109/ISGTEurope.2017.8260275.
[5]
T. Morstyn, B. Hredzak, and V. G. Agelidis. “Control Strategies for Micro-
grids With Distributed Energy Storage Systems: An Overview”. In: IEEE
Transactions on Smart Grid 9.4 (2018), pp. 3652–3666. issn: 1949-3053. doi:
10.1109/TSG.2016.2637958.
[6]
Reza Olfati-saber, J. Alex Fax, and Richard M. Murray. “Consensus and coop-
eration in networked multi-agent systems”. In: Proceedings of the IEEE. 2007,
p. 2007.
[7]
M. I. Abouheaf and F. L. Lewis. “Multi-agent differential graphical games:
Nash online adaptive learning solutions”. In: 52nd IEEE Conference on Deci-
sion and Control. 2013, pp. 5803–5809. doi: 10.1109/CDC.2013.6760804.
[8]
M. Reyasudin Basir Khan, Razali. Jidin, and Jagadeesh. Pasupuleti. “Multi-
agent based distributed control architecture for microgrid energy manage-
ment and optimization”. In: Energy Conversion and Management 112 (2016),
pp. 238–307.
[9]
Y. Han et al. “MAS-Based Distributed Coordinated Control and Optimization
in Microgrid and Microgrid Clusters: A Comprehensive Overview”. In: IEEE
Transactions on Power Electronics 33.8 (2018), pp. 6488–6508. issn: 0885-
8993. doi: 10.1109/TPEL.2017.2761438.
[10]
J.M. Maciejowski. Predictive Control with Constraints. England.: Prentice
Hall, 2002.
[11]
John Rossiter. Model-based Predictive Control-a Practical Approach. Jan. 2003.
doi: 10.1201/9781315272610.
65


---

Page 78

---

Bibliography
[12]
Y. Xue et al. “A comparison between two MPC algorithms for demand charge
reduction in a real-world microgrid system”. In: 2016 IEEE 43rd Photovoltaic
Specialists Conference (PVSC). 2016, pp. 1875–1880. doi: 10.1109/PVSC.
2016.7749947.
[13]
Alessandra Parisio, Evangelos Rikos, and Luigi Glielmo. “A Model Predictive
Control Approach to Microgrid Operation Optimization”. In: Control Systems
Technology, IEEE Transactions on 22 (Sept. 2014), pp. 1813–1827. doi: 10.
1109/TCST.2013.2295737.
[14]
Alessandra Parisio et al. “Use of model predictive control for experimental
microgrid optimization”. In: Applied Energy 115 (Feb. 2014), 37–46. doi: 10.
1016/j.apenergy.2013.10.027.
[15]
G. Gürses-Tran et al. “MPC based energy management optimization for a
european microgrid implementation”. In: 25th International Conference on
Electricity Distribution. Vol. Paper 1908. 2019.
[16]
Y. Xu and Z. Li. “Distributed Optimal Resource Management Based on the
Consensus Algorithm in a Microgrid”. In: IEEE Transactions on Industrial
Electronics 62.4 (2015), pp. 2584–2592. issn: 0278-0046. doi: 10.1109/TIE.
2014.2356171.
[17]
S. Luo et al. “Multi-agent systems using model predictive control for coordi-
native optimization control of microgrid”. In: 2017 20th International Con-
ference on Electrical Machines and Systems (ICEMS). 2017, pp. 1–5. doi:
10.1109/ICEMS.2017.8056293.
[18]
Z. Guoping, W. Weijun, and M. Longbo. “An Overview of Microgrid Planning
and Design Method”. In: 2018 IEEE 3rd Advanced Information Technology,
Electronic and Automation Control Conference (IAEAC). 2018, pp. 326–329.
doi: 10.1109/IAEAC.2018.8577763.
[19]
R. Venkatraman and S. K. Khaitan. “A survey of techniques for designing and
managing microgrids”. In: 2015 IEEE Power Energy Society General Meeting.
2015, pp. 1–5. doi: 10.1109/PESGM.2015.7286590.
[20]
R. Lasseter et al. “Integration of Distribution Energy Resources - The CERTs
Microgrid concept”. In: Consortium for Electric Reliability Technology Solu-
tions (2002).
[21]
L. Tao et al. “From laboratory Microgrid to real markets — Challenges and
opportunities”. In: 8th International Conference on Power Electronics - ECCE
Asia. 2011, pp. 264–271. doi: 10.1109/ICPE.2011.5944600.
[22]
“IEEE Standard for the Specification of Microgrid Controllers”. In: IEEE Std
2030.7-2017 (2018), pp. 1–43.
[23]
F. Katiraei, M. R. Iravani, and P. W. Lehn. “Micro-grid autonomous operation
during and subsequent to islanding process”. In: IEEE Transactions on Power
Delivery 20.1 (2005), pp. 248–257. issn: 0885-8977. doi: 10.1109/TPWRD.
2004.835051.
66


---

Page 79

---

[24]
Xiong Liu, Peng Wang, and Poh Chiang Loh. “A hybrid AC/DC micro-grid”.
In: 2010 Conference Proceedings IPEC. 2010, pp. 746–751. doi: 10.1109/
IPECON.2010.5697024.
[25]
B. Kroposki et al. “Microgrids: Technologies and Testing”. In: IEEE Power
and Energy Magazine (2008).
[26]
I. Erlich, M. Wilch, and C. Feltes. “Reactive power generation by DFIG
based wind farms with AC grid connection”. In: 2007 European Conference
on Power Electronics and Applications. 2007, pp. 1–10. doi: 10.1109/EPE.
2007.4417777.
[27]
S. Zhou. “Study of Control and Efficiency of AC-DC Converter”. In: 2010 In-
ternational Conference on Electrical and Control Engineering. 2010, pp. 4250–
4253. doi: 10.1109/iCECE.2010.1033.
[28]
V. V. Joshi, N. Mishra, and D. Malviya. “A Vector Control Based Superca-
pacitor Current Control Algorithm for Fuel Cell and Battery - Supercapacitor
Integrated Electric Vehicles”. In: 2018 IEEE 8th Power India International
Conference (PIICON). 2018, pp. 1–6. doi: 10.1109/POWERI.2018.8704381.
[29]
A. M. S. Yunus and M. Saini. “Overview of SMES units application on smart
grid systems”. In: 2016 International Seminar on Intelligent Technology and
Its Applications (ISITIA). 2016, pp. 465–470. doi: 10.1109/ISITIA.2016.
7828705.
[30]
R. Majumder. “Some Aspects of Stability in Microgrids”. In: IEEE Trans-
actions on Power Systems 28.3 (2013), pp. 3243–3252. issn: 0885-8950. doi:
10.1109/TPWRS.2012.2234146.
[31]
Mariya Soshinskaya et al. “Microgrids: Experiences, barriers and success fac-
tors”. In: Renewable and Sustainable Energy Reviews 40 (2014), pp. 659 –
672. issn: 1364-0321. doi: https : / / doi . org / 10 . 1016 / j . rser . 2014 .
07.198. url: http://www.sciencedirect.com/science/article/pii/
S1364032114006583.
[32]
Carmen Wouters. “Towards a regulatory framework for microgrids—The Sin-
gapore experience”. In: Sustainable Cities and Society 15 (2015), pp. 22 –
32. issn: 2210-6707. doi: https : / / doi . org / 10 . 1016 / j . scs . 2014 .
10.007. url: http://www.sciencedirect.com/science/article/pii/
S2210670714001152.
[33]
Hassan Harb. “Predictive Demand Side Management Strategies for Residential
Building Energy Systems”. PhD thesis. E.ON Energy Research Center, RWTH
Aachen University, 2017.
[34]
A. Monti et al. Dual Demand SideManagement. Tech. rep. Project No. 30.
Institute for Automation of Complex Power Systems, Institute for Energy
Efficient Buildings, and Indoor Climate, 2014, p. 150.
67


---

Page 80

---

Bibliography
[35]
Lokeshgupta Bhamidi, Arindam Sadhukhan, and S. Sivasubramani. “Multi-
objective optimization for demand side management in a smart grid environ-
ment”. In: Dec. 2017, pp. 200–205. doi: 10.1109/ICPES.2017.8387293.
[36]
Jingshuang Shen, Chuamwen Jiang, and Bosong Li. “Controllable Load Man-
agement Approaches in Smart Grids”. In: Energy Conservation in Infrastruc-
tures (2015). issn: 1996-1073.
[37]
A. Bidram, A. Davoudi, and F. L. Lewis. “A Multiobjective Distributed Con-
trol Framework for Islanded AC Microgrids”. In: IEEE Transactions on Indus-
trial Informatics 10.3 (2014), pp. 1785–1798. issn: 1551-3203. doi: 10.1109/
TII.2014.2326917.
[38]
J. Timmermans et al. “Batteries 2020 — Lithium-ion battery first and second
life ageing, validated battery models, lifetime modelling and ageing assess-
ment of thermal parameters”. In: 2016 18th European Conference on Power
Electronics and Applications (EPE’16 ECCE Europe). 2016, pp. 1–23. doi:
10.1109/EPE.2016.7695698.
[39]
A. Etxeberria et al. “Hybrid Energy Storage Systems for renewable Energy
Sources Integration in microgrids: A review”. In: 2010 Conference Proceedings
IPEC. 2010, pp. 532–537. doi: 10.1109/IPECON.2010.5697053.
[40]
Mohammed I. Abouheaf et al. “Multi-agent discrete-time graphical games and
reinforcement learning solutions”. In: Automatica 50.12 (2014), pp. 3038 –3053.
issn: 0005-1098. doi: https://doi.org/10.1016/j.automatica.2014.
10.047. url: http://www.sciencedirect.com/science/article/pii/
S0005109814004282.
[41]
Y. Cao et al. “An Overview of Recent Progress in the Study of Distributed
Multi-Agent Coordination”. In: IEEE Transactions on Industrial Informatics
9.1 (2013), pp. 427–438. issn: 1551-3203. doi: 10.1109/TII.2012.2219061.
[42]
Y. Xu and W. Liu. “Novel Multiagent Based Load Restoration Algorithm for
Microgrids”. In: IEEE Transactions on Smart Grid 2.1 (2011), pp. 152–161.
issn: 1949-3053. doi: 10.1109/TSG.2010.2099675.
[43]
J. B. Rawlings. “Tutorial overview of model predictive control”. In: IEEE
Control Systems Magazine 20.3 (2000), pp. 38–52. issn: 1066-033X. doi: 10.
1109/37.845037.
[44]
Carlos E. García, David M. Prett, and Manfred Morari. “Model predictive
control: Theory and practice—A survey”. In: Automatica 25.3 (1989), pp. 335
–348. issn: 0005-1098. doi: https://doi.org/10.1016/0005- 1098(89)
90002-2. url: http://www.sciencedirect.com/science/article/pii/
0005109889900022.
68


---

Page 81

---

[45]
S. Shariati and D. Abel. “Model Predictive Control in two days: Educating a
new way of thinking”. In: IFAC-PapersOnLine 49.6 (2016). 11th IFAC Sym-
posium on Advances in Control Education ACE 2016, pp. 40 –45. issn: 2405-
8963. doi: https://doi.org/10.1016/j.ifacol.2016.07.150. url: http:
//www.sciencedirect.com/science/article/pii/S240589631630355X.
[46]
MathWorks Matlab function fillmissing. https://de.mathworks.com/help/
matlab/ref/fillmissing.html?searchHighlight=fillmissing&s_tid=
doc_srchtitle.
[47]
Nord Pool group Day-ahead prices. http://https://www.nordpoolgroup.
com/Market-data1/Dayahead/Area-Prices/SE/Hourly/?dd=SE4&view=
table.
[48]
Statista Average prices of diesel fuel in Sweden from 2000 to 2018 (in euros).
https://www.statista.com/statistics/603731/diesel-fuel-prices-
sweden/.
[49]
Diesel generators Approximate Diesel Fuel Consumption Chart. https://www.
dieselgenerators.com/approximate-diesel-fuel-consumption-chart.
[50]
MathWorks Matlab function arima. https://de.mathworks.com/help/econ/
arima.html.
69


---

Page 82

---



---

Page 83

---

List of Figures
2.1
Typical microgrid structure [18] . . . . . . . . . . . . . . . . . . . . .
7
2.2
Schematic diagram of a circuit breaker based interconnection switch
[25] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
2.3
Illustration of load shaping methods [35] . . . . . . . . . . . . . . . .
13
2.4
Classification of controllable loads [36] . . . . . . . . . . . . . . . . .
14
2.5
Decentralised, centralised and distributed multi-agent control archi-
tecture for microgrids (left to right) [5] . . . . . . . . . . . . . . . . .
17
2.6
Distributed MAS communication architectures [5] . . . . . . . . . . .
21
2.7
Basic idea of MPC shown on dependency of individual signals on time
[10] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
29
2.8
Structure of MPC enhanced by observer (when some of the states are
not observable from system outputs). In this case the set-point of the
system is labelled as w(.|k) [45] . . . . . . . . . . . . . . . . . . . . .
30
3.1
Schematic structure of Simris demonstration site [15] . . . . . . . . .
32
3.2
SoC of BESS during one week test with reference control
. . . . . .
35
4.1
Agent representation of demonstration site situation . . . . . . . . .
38
4.2
General structure of control algorithm . . . . . . . . . . . . . . . . .
39
4.3
Schematic diagram of the distributed MAS control [9]
. . . . . . . .
44
4.4
Consensus algorithm iteration for one time step . . . . . . . . . . . .
47
4.5
One-day prediction of global energy prices by an estimated SARIMA
model
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
49
4.6
Prediction of microgrid mismatch compared with real data on one
week dataset
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
50
4.7
Prediction of global energy price compared with real data on one week
dataset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
50
71


---

Page 84

---



---

Page 85

---

List of Tables
3.1
Table showing the amount of missing data in measured vectors . . .
33
4.1
Table of control constraints of MAS control . . . . . . . . . . . . . .
42
5.1
Table showing MPC settings and power exchange results of Simula-
tion 1
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
55
5.2
Table showing BESS processes results and comparison with reference
algorithms of Simulation 1 . . . . . . . . . . . . . . . . . . . . . . . .
56
5.3
Table showing MPC settings and power exchange results of Simula-
tion 2
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
57
5.4
Table showing BESS processes results and comparison with reference
algorithms of Simulation 2 . . . . . . . . . . . . . . . . . . . . . . . .
57
5.5
Table showing MPC settings and power exchange results of Simula-
tion 3
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
58
5.6
Table showing BESS processes results and comparison with reference
algorithms of Simulation 3 . . . . . . . . . . . . . . . . . . . . . . . .
58
5.7
Table showing MPC settings and power exchange results of Simula-
tion 4
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
59
5.8
Table showing BESS processes results and comparison with reference
algorithms of Simulation 4 . . . . . . . . . . . . . . . . . . . . . . . .
59
5.9
Table showing MPC settings and power exchange results of complete
simulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
60
5.10 Table showing BESS processes results and comparison with reference
algorithms of complete simulation . . . . . . . . . . . . . . . . . . . .
60
73


---

Page 86

---



---

Page 87

---

Appendix


---

Page 88

---



---

Page 89

---

A Content of the attached CD
1. Literature - A folder containing all the utilized literature
2. Matlab - A folder containing the whole used Matlab program
3. Multi-agent MPC protocols for microgrid energy management and optimiza-
tion.pdf
77
