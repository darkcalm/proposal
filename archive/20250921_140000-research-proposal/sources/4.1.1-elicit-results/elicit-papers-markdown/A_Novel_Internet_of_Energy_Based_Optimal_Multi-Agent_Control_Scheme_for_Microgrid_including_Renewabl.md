# A Novel Internet of Energy Based Optimal Multi-Agent Control Scheme for Microgrid including Renewable Energy Resources

## Paper Metadata

- **Filename:** A Novel Internet of Energy Based Optimal Multi-Agent Control Scheme for Microgrid including Renewable Energy Resources.pdf
- **DOI:** 10.3390/ijerph18158146
- **Authors:** Alhasnawi, Bilal Naji and Jasim, Basil H. and Rahman, Zain-Aldeen S. A. and Guerrero, Josep M. and Esteban, M. Dolores
- **Year:** 2021
- **Journal/Venue:** International Journal of Environmental Research and Public Health
- **URL:** http://dx.doi.org/10.3390/ijerph18158146
- **Extraction Date:** 2025-06-03T15:01:19.968450
- **Total Pages:** 24

## Abstract



## Keywords



---

## Full Text Content



### Page 1

International Journal of
Environmental Research
and Public Health
Article
A Novel Internet of Energy Based Optimal Multi-Agent Control
Scheme for Microgrid including Renewable Energy Resources
Bilal Naji Alhasnawi 1,*
, Basil H. Jasim 1
, Zain-Aldeen S. A. Rahman 1,2
, Josep M. Guerrero 3
and M. Dolores Esteban 4,*


Citation: Alhasnawi, B.N.; Jasim,
B.H.; Rahman, Z.-A.S.A.; Guerrero,
J.M.; Esteban, M.D. A Novel Internet
of Energy Based Optimal
Multi-Agent Control Scheme for
Microgrid including Renewable
Energy Resources. Int. J. Environ. Res.
Public Health 2021, 18, 8146. https://
doi.org/10.3390/ijerph18158146
Academic Editors: Shu-Yuan Pan,
Li-Chi Chiang, Yu-Pin Lin and Paul
B. Tchounwou
Received: 9 June 2021
Accepted: 26 July 2021
Published: 31 July 2021
Publisher’s Note: MDPI stays neutral
with regard to jurisdictional claims in
published maps and institutional afﬁliations.
Copyright: © 2021 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed
under
the
terms
and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).
1
Electrical Engineering Department, University of Basrah, Basrah 61001, Iraq; hanbas632@gmail.com (B.H.J.);
as.zain9391@stu.edu.iq (Z.-A.S.A.R.)
2
Department of Electrical Techniques, Qurna Technique Institute, Southern Technical University,
Basra 61016, Iraq
3
Center for Research on Microgrids (CROM), Department of Energy Technology, Aalborg University,
9220 Aalborg, Denmark; joz@energy.aau.dk
4
Civil Engineering Department, Hydraulics, Energy and Environment/Profesor Aranguren 3,
Universidad Politécnica de Madrid (UPM), 28040 Madrid, Spain
*
Correspondence: bilalnaji11@yahoo.com (B.N.A.); mariadolores.esteban@upm.es (M.D.E.);
Tel.: +964-7809-0985 (B.N.A.)
Abstract: The increasing integration of Renewable Energy Resources (RERs) in distribution networks
forms the Networked Renewable Energy Resources (NRERs). The cooperative Peer-to-Peer (P2P)
control architecture is able to fully exploit the resilience and ﬂexibility of NRERs. This study proposes
a multi-agent system to achieve P2P control of NRERs based Internet of Things (Io T). The control
system is fully distributed and contains two control layers operated in the agent of each RER. For
primary control, a droop control is adopted by each RER-agent for localized power sharing. For
secondary control, a distributed diffusion algorithm is proposed for arbitrary power sharing among
RERs. The proposed levels communication system is implemented to explain the data exchange
between the distribution network system and the cloud server. The local communication level utilizes
the Internet Protocol (IP)/Transmission Control Protocol (TCP), and Message Queuing Telemetry
Transport (MQTT) is used as the protocol for the global communication level. The effectiveness of the
proposed system is validated by numerical simulation with the modiﬁed IEEE 9 node test feeder. The
controller proposed in this paper achieved savings of 20.65% for the system, 25.99% for photovoltaic,
35.52 for diesel generator, 24.59 for batteries, and 52.34% for power loss.
Keywords: renewable energy resources; diffusion algorithm; Io T; IEEE microgrid; cooperative
control; cloud platform
1. Introduction
Renewable energy is going to be an important source for power generation in the
near future because we can use these resources again and again to produce useful energy.
The energy resources are normally classiﬁed as fossil resources, renewable, and nuclear
energy resources. Different renewable energy resources, such as hydropower, wind, solar,
biomass, ocean energy, biofuel, geothermal, etc., provide 15–20% of the total world’s energy.
The world is going to turn into a global village due to more requirement of energy due to
fast-growing population, which leads to the use the fossil fuels such as coal, gas, and oil to
fulﬁl the energy requirement, which creates unsustainable situations and many problems
such as depletion of fossil fuels, environmental and geographical conﬂicts, greenhouse
effect, global warming, and ﬂuctuation in fuel prices. Due to environment-friendly and
less emission of gases from renewable energy, it is considered as sustainable energy; also
supported for the society from each dimension: economic, social, and environmental [1].
Int. J. Environ. Res. Public Health 2021, 18, 8146. https://doi.org/10.3390/ijerph18158146
https://www.mdpi.com/journal/ijerph

---


### Page 2

Int. J. Environ. Res. Public Health 2021, 18, 8146
2 of 24
Microgrids may be a prospective power system that addresses the renewable energy
technologies (RET) accompanying the necessary growing deployment of distributed energy
resources (DER) [2].
The micro-grid has a hierarchical control system consisting of internal/primary, secondary, and tertiary control levels [2,3]. The micro grid is connected to the main grid
during normal operation. But, in the event of a disturbance, it will change to autonomous
mode. Therefore, it is crucial for a stable and economically effective micro grid operation
to have an appropriate control scheme, which can keep the voltage/frequency stable and
maintain active/active power-sharing. Both voltage and frequency of a micro grid are
dictated by a main grid in a grid connected mode, however, in an islanded mode, primary
control takes the responsibility of the voltage and frequency control [4]. Operation of a
micro grid with a primary control alone, in an islanded mode, causes the steady-state
load-dependent voltage and frequency deviations, giving rise to power quality problems
and deteriorating the healthy operation of MG. Thus it must compensate for such variations
with the use of a second additional control to revert voltage and frequency to the nominal
values (i.e., standard or reference) of each distributed generator unit [5–8].
The secondary control approaches include centralised control [9], decentralised control [10], and distributed control [11]. Inspired by the cooperative Multi Agent Systems
(MAS) control concept the distributed control concept. It depends on the communication
between local authorities who can exchange information via a local communication network with neighbouring agents [12]. The distributed generator unit in the micro grid is
regarded as the agent capable of communicating with its neighbouring agents through a
sparse communication network. Thus, a micro grid behaves as a MAS.
The traditional secondary microwave control structure uses a centralized system in
which each unit is connected to all the rest of the unit bi-directionally. This controller
problem is gathering comprehensive information in a system that requires costly and
complex network communications, lacks ﬂexibility, and is prone to single point failure.
This means that the centralized control process stops working regardless of whether or not
a single unit breaks down or loses connections to the remaining network due to failure of
communication links [13]. On the other hand, the main advantage of the distributed check
method is that the unit is not required for communications in the communication network
with all other units, thereby enhancing the reliability of the entire micro network operation
and reducing bandwidth and communication network cost requirements. Because of this
attribute, distributed cooperative control systems are popular for promising micro grid
application solutions [1].
Therefore, in this paper, the researchers developed a new decentralized cooperative
peer-to-peer approach for coordinating the multi Renewable Energy Resources (RERs)
operation in distribution networks.
The Internet of Energy (Io E) refers to a paradigm that connects different digital, real,
and virtual devices to intelligent environments via network information. It applies in
many ﬁelds, including transport, energy, and urban areas. Energy Internet is considered a
smart microgrid revolutionary network. In the energy and power sectors, it is regarded
as an overall Io T application. The Energy Internet consists of different techniques and
components, which are summarised into three groups, i.e., (i) system of power, (ii) system
of communication, and (iii) control systems. In one study, the researchers stated that
the Energy Internet’s cross-disciplinary nature had presented several opportunities and
challenges, which have to be investigated further and validated [14].
It was noted that the MGs act as primary building blocks in an Energy Internet since
they can be operated in grid-connected and islanded modes [15]. The droop based primary control can be used for autonomous power sharing among all connected distributed
generations. An islanded MGs’ secondary control feature allows voltage/frequency restoration while maintaining precise power sharing among the connected distributed generations [16]. Furthermore, the tertiary control helps in the optimal operation of the microgrids
(MGs) [17]. In the hierarchy, tertiary control helps determine optimal dispatch values, which

---


### Page 3

Int. J. Environ. Res. Public Health 2021, 18, 8146
3 of 24
are dependent on renewable and load forecasting. Regarding the dispatch intervals, both
the primary and the secondary controls are operated for sharing the actual power deviation
taking place from the dispatch values. A consensus algorithm-based secondary control
and the distributed optimisation algorithm-dependent tertiary controls have garnered a
lot of research attention owing to their increased ﬂexibility and resilience compared to the
centralised control [18,19]. Furthermore, the implementation of a distributed algorithm is
dependent on Multi-Agent System (MAS), wherein multiple subsystems/agents interact
with one another with the help of sparse communication networks [20].
To the best of the authors’ knowledge, achieving reactive power/active power sharing
and voltage and frequency regulation, with preserved local information privacy, is still the
open question. To this end, this paper presents a distributed consensus-based method to
achieve reactive power, active power sharing and voltage and frequency regulation in MG.
First, the original control problem is transformed into an equivalent active power reference
generation problem, which can be solved by obtaining the global active power utilization
level. Further, a distributed diffusion algorithm is proposed to acquire this global variable.
In addition, this study objectives to offer potential solutions for following situations: (i) distributed controllers may neither be located at the same location as distributed generations
nor have a proprietary communication network. A remote control of microgrids by the
Internet, taking communication latency into consideration, is required. (ii) For microgrids
governed via multi agent systems, each agent or sub-multi agent systems can be practically owned via different stakeholders who could cooperate or work independently. (iii)
With the features in Internet of Things and renewable system, the number of controllable
units in microgrid is dramatically increasing. Any distributed control system scalability to
withstand increasing numbers of distributed generations is an issue worthy of exploration.
1.1. Related Works
Active power-sharing traditionally takes place through primary control. The centralised controller is then used to offset drop control deviations in frequency [21,22]. There
is no ﬂexibility in the centralised control structure, and there can be a single failure. The
literature therefore reports distributed control algorithms [23]. The information shared by
the distributed controllers over a sparse communication network can be used to achieve
active power sharing and frequency control [24]. However, the distributed generations are
transmitted directly to their neighbours without protection of their privacy or sensitive
local data such as power outputs, usage levels, power capacity, etc.
In [25], coordinated controls were proposed, including for different distributed energy
storage systems, to equalize charge status. A secure cloud-based multi-agent platform is
not, however, investigated. In [26], the Combination of Communication Technology and
Hierarchical Control Method proposed a coordinated method for the assessment of the
state-of-the-art balance in Alternating Current (AC) MG. However, the proposed control
structure will inevitably invalidate intact high level control functions. In [27], the authors
proposed an efﬁcient distributed control method for the synchronisation in the Island micro
grid of several Renewable Energy Resources (RERs). The secondary control technique
is developed to remove deviations in frequency and to ensure a certain time-efﬁcient
power sharing. Within a limited time frame, the proposed end time controller allows the
unconnected design for the voltage control and an alternate time frame for reactive power
sharing. However, the authors do not consider the graph network for data and information
transfer between the MG connect agents.
In [28], the authors suggested a distributed iterative learning environment to address
Direct Current (DC) microgrid’s current/voltage sharing problem. The optimal control
method, which is further determined by using the iterative value algorithm, was derived
in game theory. An adaptive dynamic programming architecture and algorithm were
developed to share current while simultaneously changing the DC bus’s voltage to its
rated value. However, active and reactive power sharing is not investigated. In [29], an
MG isolated composed by parallel connected inverters from multiple voltage sources was

---


### Page 4

Int. J. Environ. Res. Public Health 2021, 18, 8146
4 of 24
analysed by the researchers. The primary control was integrated into every inverter by
internal voltage and current systems with PR trimmings, Virtual Impedance, external
voltage, and frequency drops controllers. A secondary frequency restoration function has
been implemented by the investigators. This contributes to the implementation of the
diffusion algorithm including a frequency control and a single communication network
delay. However, a secure cloud-based platform for multi-agents is not investigated. In [30],
the authors proposed a split multi-agent ﬁnite time control approach with a balance of
load delay and voltage restoration in the battery’s DC MG. Theoretically, for each device,
delays can be different and endless. The linearization feedback approach is used with the
input time delays in dual integrated and single integration systems in order to transform
charging and voltage recovery problem. However, the distributed control for multi agent
system governed microgrids in Internet of Energy is not investigated.
In order to meet load demand and protection demand, the authors in [31] created a
Hybrid control system, based on a multiagent system event, which utilizes online supplies
of renewable energy. However, there is no study of the active and reactive power sharing. In [32], the authors suggested a new control method for voltage/frequency restore
approach based on the consensus algorithm and proposed method implemented in island
microgrid systems (MGs). However, a secure cloud-based platform for multi-agents is not
investigated. The authors proposed a diffused method for coordination control of hybrid
microgrids in [33]. The method proposed regulates accurate dc current and reactive power
shares between distributed microgrid generators, maintains power-sharing between the
two microgrids and restores a DC voltage, and the AC frequency, to their rated values.
However, the authors do not consider the graph network for data and information transfer
between the MG connect agents. In [34], researchers suggested a collapsing distributed and
hierarchical cooperative control method for microgrid cluster, including distributed layer
generation, micro grid layer, and cluster layer controls for MG. The distributed generation
layer control regulates each distributed unit’s current/tension locally. The control of the
microgrid layers for each microgrid is performed to positively manage distributed generating units via several small communication networks. The control of the Cluster-Layer
co-ordinates micro grids on the basis of a more advanced peer-to-peer communication
interface between micro-grid-agents. However, the distributed control for multi agent system governed microgrids in Internet of Energy not investigated. In [35], a new distributed
multi-agent framework based on the cloud layer computing architecture is developed for
real-time microgrid economic dispatch and monitoring. In [36], the Time of Use (To U)
model is proposed to deﬁne the rates for shoulder-peak and on-peak hours. A two-level
communication system connects the microgrid system, implemented in MATLAB, to the
cloud server. In [37], the researchers proposed a multi-agent and multi-layer architecture
for acquiring the P2 P control of the MGs. Here, the control framework was distributed entirely and it contained three control layers that were operated in every MG. For the primary
control, the researchers adopted a droop control for every MG-agent to carry out a localized
power-sharing. The researchers proposed a distributed diffusion for each secondary control
that helped in voltage/frequency restoration and arbitrary power-sharing amongst the
microgrid. However, a cloud-based platform for multi-agents is not investigated.
The existing technical studies do not address the following limitations.
•
The critical bus voltage, subject to distributed secondary voltage regulation, must
be restored to ensure continuous operation of sensitive loads. Literature [38] provides critical bus voltage restoration, but it doesn’t simultaneously maintain accurate
reactive-power sharing among units of Renewable Energy Resources (RERs) [39].
•
To the best of our knowledge, a behaviour and analysis of distributed secondary
control, when the AC side voltage of a distributed generator unit reaches to its limit,
has not been reported.
•
Literature [40–42] assume purely inductive networks for small signal dynamic analyses of the distributed secondary frequency controller [42] and the distributed sec-

---


### Page 5

Int. J. Environ. Res. Public Health 2021, 18, 8146
5 of 24
ondary voltage controller [40,41]. For a practical micro grid system, especially the low
voltage (LV) micro grid system
•
The active power, reactive power-sharing simultaneous regulation are not investigated.
Second, the distributed diffusion control method for multi agent governed microgrids
in the Internet of Energy has not been studied. This motivates us to provide a novel
approach that enables the group play and plug feature, such that microgrids with
multiple multi agent, owned by different stakeholders, can be ﬂexibly controlled.
1.2. Paper Contribution
The present developments and limitations of the literature have led the researcher to
propose a fully distributed diffusion based control system for the achievement of several
objectives. The chief contributions of this paper are summarised as:
1.
The peer-to-peer control architecture considering multi-agent and multi-layers interaction is introduced for a distribution networks in the Energy Internet, which has not
been reported in the past.
2.
This paper summarises the ﬁndings of researchers in distributed control design of
RERs devices in microgrid to provide ancillary services, including equal reactive
power sharing, equal active power-sharing between RES units, and controlling the
load in both islanded mode and grid-connected mode.
3.
An Io T-based communication protocol including speciﬁcations such as MQTT is
proposed. This improves system ﬂexibility. The proposed system offered analytics and business intelligence (BI), which allowed the researchers to gain insights
on data collected by visualizing dashboards and reports. Additionally, the use of
large data-based data storage technologies enabled the system’s scalability at the
national level. This provided energy-efﬁciency strategies for the home owners and
the utility companies.
2. Proposed System Description
Here, the researchers considered that the RESs consisted of the communication and
control agents on the Internet of Energy realm, as described in Figure 1. The physical
components of a general microgrid included the inverter-interfaced Renewable Energy
Resources [Such as photovoltaic, wind turbine, and energy storage systems], dynamic and
static loads, and the diesel generators. It was noted that a framework controlled the RESs in
a microgrid, wherein one MAS agent managed every RESs. The MAS agents communicate
by Local Area Network (LAN) and can access the Internet for remotely controlling the microgrid via the cloud servers. In the Energy Internet, every distributed generator/microgrid
was managed by various stakeholders and their controllers on the MAS/agents differed
from MG components. It was expected that number of the distributed generator and MG
agents could be changed online. Hence, a remote, ﬂexible, and distributed control and
implementation framework were necessary. Figure 1 presents a proposed system.
A smart grid would need an effective measuring and communication system to
continuously track the power and cost proﬁle and regularly quantify power losses. There
are several stages of data processing.
This work contains measurement units (MU) for every distribution network bus. MU
is MATLAB modelling. Power and cost information is sent to the control centre regularly
at a ﬁxed time. The control centre is designed as a virtual data management and analysis
platform. One approach to communication, relating to the device topology proposed, is
considered. The case takes a Cloud approach, which sends its measured data directly to
the cloud by any MU connected to the corresponding feeder bus, as illustrated in Figure 1.
The data transfer among the MATLAB software package and the open-source Io T
framework Thing Speak are used to model proposed communication architectures. Thing Speak was chosen for the simulation of real-time cloud communication due to its following
beneﬁts [43]:

---


### Page 6

Int. J. Environ. Res. Public Health 2021, 18, 8146
6 of 24
1.
Thing Speak Cloud Io T platform data aggregation, tracking and analysis. In the smart
grid model, the power proﬁle is monitored on multiple Thing Speak channels in
real-time and depicted graphically.
2.
Security: The Username and password allow user authentication while each channel
is equipped with its ID and accessible (see by other users). There are two keys in
each channel for the application programming interface. A randomly generated read
key and write key of the API. These keys can save or retrieve information from each
channel over the Internet or LAN.
3.
It facilitates the double-way ﬂow of data between the user and virtual device and
allows data and remote control to be exchanged in real-time. The MATLAB Desktop Toolbox offers communication between the simulated feeding model and the
Thing Speak Io T platform.
4.
Communication network enabling for the data transmission over the Internet between
MATLAB and Thing Speak.
5.
Allows importing, exporting, analysing, and viewing data on multiple platforms and
their ﬁelds simultaneously,
 
Communication 
network
Control layer
Physical layer
Cyber layer
2
1
4
3
Primary 
controller
Secondary 
controller
Home 1
Home 2
Home 3
Home 4
Home 5
Battery
Photovoltaic
Utility 
Grid
Diesel 
Generator 
Transformer
Transformer
Transformer
Converter
Inverter
BUS 2
BUS 
7
BUS 8
BUS 9
BUS 3
BUS 6
BUS 4
BUS 5
6
9
8
7
5
Figure 1. IEEE 9 bus system, with renewable energy sources and communication system.
3. Renewable Energy Resources (RERs)
3.1. Photovoltaic Cell Modeling
Figure 2 shows a single photovoltaic cell diode system based upon which current
source, diode, resistance series, and parallel resistance are represented. In the Figure 3
Illustration, the photovoltaic cell current-voltage characteristics are described in the mathematical equation standard [44]:
I = Iph;cell −I0;cell

exp
q(V + IRs;cell
ak T

−1

−V + IRs;cell
Rp;cell
,
(1)
where: Iph;cell, is a current (A) of photovoltaic; I0;cell, is a saturation current of a photovoltaic;
T is a temperature of a diode; k is a constant of Boltzmann (1.38 × 10−23 J/K); Rp, is a
parallel resistance of PV (Ω); Rs, is a series resistance of PV (Ω), V is a thermal voltage.

---


### Page 7

Int. J. Environ. Res. Public Health 2021, 18, 8146
7 of 24
Ideal Solar Cell
Practical Solar Cell
Iph,cell
ID,cell
IP
Rp,cell
Rs,cell
I
V
 
Figure 2. Equivalent circuit of photovoltaic.
IPH,cell
Id,cell
V
V
V
I
-
=
Figure 3. Voltage and current of photovoltaic.
3.2. Photovoltaic Modeling
The photovoltaic module consisting of PV cells joined in a parallel and series shapes
is mentioned above. Therefore, Equation (1) derives from the mathematical standard and
the PV module description of its I-V characteristic [44]:
I = IPH −IO

exp
V + IRS
a Vt

−1

−V + IRS
Rp
,
(2)
where: Vt is a thermal voltage, IPH is a photocurrent (A), RS is a series resistance, IO is a
reverse leakage current, Rp is a parallel resistance. The Equation (2) produces voltage and
current curve as indicated in Figure 4.
The PV module’s photocurrent (IPH) is determined by the amount of solar radiation
falling on modulus and photovoltaic cell temperature that ﬁts the equation below [44]:
Iph = G
Gn

Iph;n + Ki∆T

(3)
where: IPH.n is a photocurrent; Gn is a irradiance
Voc = Voc;n + Kv∆T
(4)

---


### Page 8

Int. J. Environ. Res. Public Health 2021, 18, 8146
8 of 24
where: Kv is a temperature coefﬁcient, Voc;n is open circuit voltage.
Io =
Isc;n + Ki∆T
exp
 Voc;n+Kv∆T
a Vt

−1
,
(5)
where Isc;n is a short-circuit current.
Figure 4. Current-voltage, photovoltaic module curves at different temperatures and permanent
insolation levels.
System of Energy Storage
The system of battery storage stores excess energy generated by generation of renewables. In the event of energy shortages from the renewable energy systems batteries will
be discharged so as to meet demand for load. Simple dynamics of batteries are modelled,
such as [44,45]:
SOCbat = 100

1 −

1
Qbat
·
Z t
0 ibat(t)dt

,
(6)
BAH =
1
3600
Z t
0 ibat(t)dt,
(7)
where Qbat is a maximum batteries capacity (A h), SOCbat is a batteries state of charge (%),
BAH is a battery ampere-hour and ibat is the battery current.
3.3. Diesel Generator of Disterbuted Network
In the micro grid, this diesel generator balances power and charge. A diesel engine, a
control system, an exciting system, and a simulated machine are included in the models.
Diesel engine and the model system governor are combined with speed inputs into one
unit (in p.u.). The mechanical capacity of the diesel motor is the block output. The control
function is modelled as follows [46]:
Hc =
k(1 + T3S)
1 + T1S + T1T2S,
(8)
where T1, T2 and T3 are regulator time constants, k is a proportional gain and. The actuator
transfer function is as:
Ha =
1 + T4S
[s(1 + T5S)(1 + T6S)],
(9)
where T4, T5 and T6 are actuator time constants. An excitement system is represented by
the following transfer function for the synchronous machine.
Vf d
Vro
=
1
Ks + STe
,
(10)

---


### Page 9

Int. J. Environ. Res. Public Health 2021, 18, 8146
9 of 24
where Vro is a regulator’s output, Vf d is a exciter voltage, Te is time constant (seconds), Ks
is the gain.
3.4. Problem Formulation
This paper considered an MG with N controllable distributed generator (indexed as
I = 1, 2, . . . , N.). The MGs electrical network is presented using an elaborate weighted
graph, T = (VT, ET), wherein the nodes VT = {v1, v2, . . . v N} represented the buses (RES)
and edges, ET ⊆VT × VT, represented line connections [47].
3.5. Primary Control of Inverter
The basic graph for Renewable Energy Resources (RERs) connected via AC/DC
converters and LCL ﬁlters is shown in Figure 5. The proposed primary control is shown in
Figure 5 [48].
ωni = ωi + m Pi Pi
(11)
Vni = Voi + m Qi Qi
(12)
where ωni and Vni are the nominal set points for frequency and voltage, ωi and Voi are
the frequency and voltage of DG i, m Pi and m Qi are the frequency and voltage magnitude
droop coefﬁcients of DG i, respectively.
 
i

li
i
bi
v
fi
C
oi
v
fi
j X
d
R
d
j X
Power 
calculation
Power 
Controller
i
P
i
Q
Voltage 
Controller
Current 
Controller
PWM
ni
V
Figure 5. Schematic of control.
3.6. MASs Communication
The communication networks of microgrid having N agents was represented using
a graph: G = (VG, EG) having a deﬁned set of nodes VG = {v1, v2, . . . , v N} and edges
EG ⊆VG × VG. All nodes presented in the graph G(agents) showed a one-to-one correspondence to the units in the graph T (renewable energy resources). Furthermore, edges
in G, which represented the communication links for the data exchange, differed from
electrical connection seen in T . In addition, set of neighbors described in the ith node
of G was represented by Ni =

vj ∈VG :
 vi, vj
 ∈EG
	
. The researchers represented the
adjacency matrix as

aij
 ⊆Rn×n [11]. Here, the term aij represented the information that
was exchanged between the units i and j, wherein aij = 1 when units i and j were connected
with the edge (vi, vj) ∈EG, else aij = 0. The researchers represented the Laplacian matrix
as L =

lij
 ⊆Rn×n where each element lij = ∑n
i=1 aij −aji. They described the pinning
matrix as G = diag[gi] ⊆Rn×n and gi = 1 when the RER/agent could access the references
ωre f and Vre f , else gi = 0. Figure 6 presents the data exchange between the controllers.

---


### Page 10

Int. J. Environ. Res. Public Health 2021, 18, 8146
10 of 24
2
1
4
3
6
9
8
7
5
Figure 6. The information exchange graph among the connected agents.
3.7. Proposed Secondary Distributed Controller
The chief objective of this section is to add to droop controller of renewable energy
resources a secondary controller. In order to control the frequency and voltage of the system
in a common connecting point, the controller receives information from neighbouring RES
and sharing power between appliances. Moreover, a virtual leader can be assigned to one
RES or a couple of storage devices on the system. The leader has the tension and frequency
setpoints of the system and shares the information with his neighbouring storage units. The
RES model needs to be developed in order to develop such a control design. A simpliﬁed
RES model has been developed in our recent work. The model reﬂects the dynamics of the
DC and the RES active power. The RES dynamics of devices in smart grids can be precisely
incorporated into this model. The RER device dynamics can be displayed [49]:
ωi = ωnom
i
−DP
i Pi
(13)
|Vi| = |Vnom
i
| −DQ
i Qi
(14)
.
Ei = −DP
i
3600 Pi
(15)
.
Pi = u P
i
(16)
For the development of such a simpliﬁed model, voltage controller and current
controller dynamics are supposed to be much faster than a droop controller, so its dynamics
may be ignored. u P
i for distributed active power-sharing is input in the above-mentioned
model, and DP
i reﬂects RESs heterogeneity. To ensure the equality of power sharing, DP
i Pi
should be controlled by batteries in order to increase power sharing in a RES with higher
capacity (lower drop-in gain, DP
i ). This study regulates nominal voltage and the frequency
of adjacent RES units in order to minimize communications between RERs. The control
design will require only nominal frequencies ωnom
i
and the nominal tension |Vnom
i
| of its
adjacent devices, and thus, only the frequency and voltage signals from neighbouring RESs.
These inputs include

.
V
nom
i
 = u V
i ,
.
Qi& = u Q
i and
.ωnom
i
= uω
i . The overall dynamics of
the ith is formulated as [49]:
.
Ei = −DP
i
3600 Pi
(17)
.
Pi = u P
i
(18)

---


### Page 11

Int. J. Environ. Res. Public Health 2021, 18, 8146
11 of 24

.
V
nom
i
 = u V
i
(19)
.
Qi = u Q
i
(20)
.ωnom
i
= uω
i
(21)
Let ωre f and Vre f be a reference voltage and frequency of RES. These references are
used as external commands, which force RES to precisely converge voltage and frequency
to their desired values. The respect, design of diffusion is proposed as:
u P
i = −C2
DP
i
∑
j∈Ni

DP
i Pi −DP
j Pj

(22)
u V
i = −C3 ∑
j∈Ni

|Vnom
i
| −
Vnom
j


−CV
0 a0i

|Vnom
i
| −DQ
i Qi −
Vre f 

(23)
u Q
i = −C3
DQ
i
∑
j∈Ni

DQ
i Qi −DQ
j Qj

(24)
uω
i
= −C2 ∑
j∈Ni

ωnom
i
−ωnom
j

−Cω
0 a0i

ωnom
i
−DP
i Pi −ωre f 
(25)
Let
.
e Pi ≜DP
i Pi and
.
e Qi ≜DQ
i Qi, then a closed-loop model of renewable energy resources with a diffusion design Equations (22)–(25) are [49]:
.
Ei = −1
3600
e Pi
(26)
.
e Pi = −C2 ∑
j∈Ni

e Pi −e Pj

(27)

.
V
nom
i
 = −C3 ∑
j∈Ni

|Vnom
i
| −
Vnom
j


−CV
0 a0i

|Vnom
i
| −e Qi −
Vref 

(28)
.
e Qi = −C3 ∑
j∈Ni

e Qi −e Qj

(29)
.ωnom
i
= −C2 ∑
j∈Ni

ωnom
i
−ωnom
j

−Cω
0 a0i

ωnom
i
−e Pi −ωref 
(30)
e P(t) = e−C2Lte P(0)
(31)
where L is symmetric matrix, e P(0) is vector of initial proportional active power. e−C2Lt is a
symmetric matrix.
e−C2Lt = Ulim
t→∞diag
n
1, e−C2λ2t, . . . , e−C2λNto
UT = Udiag{1, 0, . . . , 0}UT
(32)
where λ2, . . . , λN are positive eigenvalues of L once G is connected. On the other hand,
Udiag{1, 0, . . . , 0}UT =
h
1N/
√
N, 0N, . . . , 0N
i
UT = 1N1T
N/N where the eigenvector associated with zero eigenvalue of L is 1N.
e−C2Lte P(0) = 1T
Ne P(0)
N
1N
(33)
ˆωi ≜ωi −ωref , i = 1, . . . , N; ˆω ≜[ ˆω1, . . . , ˆωN]T
(34)

---


### Page 12

Int. J. Environ. Res. Public Health 2021, 18, 8146
12 of 24
.
ˆωi
=
.ωi =
.ωnom
i
−
.
e Pi
= −C2 ∑
j∈Ni

ωnom
i
−ωnom
j

−C2 ∑
j∈Ni

e Pi −e Pj

−Cω
0 a0i ˆωi
= −C2 ∑
j∈Ni
  ˆωi −ˆωj
 −Cω
0 a0i ˆωi
(35)
Denote D0 ≜diag {a0i}i=1,...,N. Consequently, we obtain from (35) that
.
ˆω
nom = −[C2L + Cω
0 D0] ˆω
(36)
If at least one of the folder is connected with a leader, e.g., D0 is not a zero matrix,
the communications graph G between the followers was shown in [49] that all the values
on C2L + Cω
0 D0 of the matrix were positive in real parts for all C2 > 0 and Cω
0
> 0.
lim
t→∞ˆω(t) = 0. This corresponds to the battery frequency diffusion of the reference frequency
ωre f . Figure 7 shows the proposed method ﬂowchart.
 
Start
Initialization and 
configuration
Update the number of 
renewable energy sources 
Exchange information 
with neighboring
Adjust Active power, and 
Reactive power, 
comunication 
algorithm converges ?
End
Sent the results to primary 
control
Y
Y
NO
Are parameters 
changes?
Y
No
Correct active power, and 
reactive power,
Is time =24 h?
No
Is an incoming command 
from the web page?
Receive command from 
Web page by TCP/MQTT 
protocol
Switch on and switch off 
the appliances
Y
NO
Send data to web page by 
TCP/MQTT protocol
Figure 7. The proposed method ﬂowchart.

---


### Page 13

Int. J. Environ. Res. Public Health 2021, 18, 8146
13 of 24
4. Proposed Internet of Energy Communication Platform
The decentralised controller of a smart MG helps in managing the system operating
conditions if there is some disturbance. Furthermore, the Io T technology can be used
for communicating between the appliances present in smart homes, central controller, or
power management centres. The researchers proposed the Io T platform for collecting the
data, monitoring, managing, and controlling a smart microgrid. All appliances and energy
resources were integrated and connected in this platform. The major Io T platform layers
included energy supply layer, network layer, energy management layer, energy appliance
layer, control system layer, and the Internet of Things service layer, as presented in Figure 8.
Agents layer
Io T platform layer
Network layer
Data processing layer
Cloud platform layer
Figure 8. Proposed Internet of Energy platform architecture.
It is a demanding job to develop an energy management distributed Energy Internet
(Io E) base. The role of the platform is to (1) incorporate the micro-grid tools into the
communications system and (2) link to the Io E cloud in order to track and manage the
devices. The Io E communications network proposed is composed of four different layers,
as deﬁned in Figure 8. Following is a summary of each layer.
(a)
Agent Layer
The device or perception layer was referred to as the layer of different components [50].
Various Io T users are included in the device layer, which comprises of smart electric vehicles,
smart homes, and transportation systems, along with RERs such as FCs, MTs, and the WTs.
Additionally, this layer supported different kinds of sensors for measuring the real-time
environmental and physical state of the components and the actuators needed for adjusting
them. Hence, WSNs and WSANs were seen to be an inseparable component of this layer.
(b)
Io T platform layer
The Io T platform layer is the sensors layer. Moreover, this layer supports different
types of sensors to monitor the environmental or physical condition of connected agents
and to adjust them in real-time. Wireless sensor and actor network (WSANs) and wireless
sensor network (WSNs) are the two pieces of the sheet that are inseparable. WSNs can be
described as a number of sensors that are used to sense the environmental conditions and
transmit them through a wireless network to other devices or upper layers.

---


### Page 14

Int. J. Environ. Res. Public Health 2021, 18, 8146
14 of 24
(c)
Network layer
Network layers can assemble the data from cloud and perception layers and then
transfer it to upper layers for extra processing and storage. It can transmit the data to other
smart devices for distributed functions present on component edges. A few communication
topologies that are used in changed areas include WIFI, Bluetooth, Z-Wave, Zigbee, 3G/4G,
Lo Ra, UMB, and cellular networks. These devices provide a wireless communication
facility and can be used in various applications.
(d)
Layer of data processing
Layer of data processing is deﬁned as the layer which allows processing and storing a
huge volume of data, which was assembled from lower layers with the help of powerful
processors [50].
(e)
Layer of cloud
The cloud layer stores a historical data from distributed energy resources (DERs)
for the purpose of global tracking. One of the features required for Io T applications and
services is to store historical data [51]. The Io E cloud layer includes virtualized servers.
In addition, an application interface has been introduced with preserved historical data for
each DER. A vast volume of data can be saved and maintained in the historical archive,
which is supported by the application interface to the cloud infrastructure [52].
4.1. MQTT Knowledge
Message Queuing Telemetry Transport (MQTT) is a lightweight protocol that makes
effective use of the network bandwidth with a ﬁxed header of two bytes. The MQTT is
operational on TCP and ensures that all messages are sent from agent to server.
Three main players, MQTT broker, MQTT publisher, and a MQTT subscriber, are
included in a protocol [53]. The MQTT subscriber and publisher are indirectly linked and
do not use one IP address simultaneously. MQTT Broker refers to the network gate way that
ﬁlters, obtains, and distributes the publishers’ messages to the thousands of simultaneouslyconnected MQTT subscribers. An MQTT broker takes care of the customer authorization
and initialization process necessary for communication. To publish the information, the
MQTT publishers utilize custom themes for catering to their clients. The MQTT protocol
did not use Metadata marking. After that, the MQTT topic management presents the
metadata for a message load, which is considerable, and it can attach meaningful attributes
to topic. MQTT is seen to be a string having a multi-attribute and multi-level layer. All
subjects could be updated for deriving the routing data. Figure 9a presents the connection’s
initialization after exchanging the control packets between the clients and brokers. It was
noted that the check packets for the CONNAC, Link, PUBACK, PUBLISH, SUBSCRIBE,
SUBACK, etc., comprise speciﬁc instructions regarding the theme, transmission, and the
payload Quality of Service (Qo S). Figure 9b presents all components of the MQTT contact.
4.2. Architecture of Proposed System
Figure 10 presents an overview of smart homes’ hierarchical platform with a cyber
layer, physical layer, and control layer. Two communication layers were included in the
hybrid platform. It was seen that in Layer one (local layer), the appliances in the smart
building transmitted the MQTT messages to a Building MQTT Client (BMC), reported
the events/measurement, and subscribed to the MQTT messages that BMC published for
protection/control purpose. Layer two (global layer) represented the interaction between
the cloud and BMC with the HTTP GET/POST requests’ help. In this architecture, every
appliance was equipped with a Wi-Fi module connected to the local gate way. Thus, it
could periodically publish the values of a dedicated and pre-deﬁned topic. After that,
BMC subscribes to different issues and posts received values to the cloud channel. Cloud
data can be accessed by the cloud MATLAB interface, which implements the designed
appliance resource allocation algorithm. The researchers found that if communication
failure occurs in any layer, the architecture proposed is resilient (either local or global).

---


### Page 15

Int. J. Environ. Res. Public Health 2021, 18, 8146
15 of 24
BMC was therefore developed to operate as a local controller for all devices in the building
during any communication link failure or high network latency noted. The results section
highlighted this function of the BMC [11].
(a) 
 
(b) 
MQTT 
Broker
(Server)
MQTT 
Client
(Publish/
Subscribe)
Cloud
Request 
(Connect)
Confirmation 
(Connect)
Request 
(Publish/Subscribe)
Confirmation 
(Publish/Subscribe)
Indication
Response
Indication
Response
Response
Subscribers 
to topic: Data 1
Publisher 1
Subscribers 
to topic: Data n
Publisher n
MQTT Broker
Topic: Data1
Topic: Data n
Figure 9. (a) MQTT Procedure, (b) MQTT Topic and Component.

---


### Page 16

Int. J. Environ. Res. Public Health 2021, 18, 8146
16 of 24
 
MQTT
Publish/ 
Subscribe
MQTT
Publish/ 
Subscribe
MQTT
Publish/ 
Subscribe
MQTT
Publish/ 
Subscribe
MQTT
Client
Cloud-Based Service
Storages
Processor
Client Interface
API Functions
HTTP 
Manager
Security
Manager
Channel Feed
Manager
Event
Manager
Command
Provider
Client Interface
Data 
Acquisation
Data Analytics
Network Data 
Aggregation
Decision Manager
Appliance 
Consumption Data
Appliance Status
Appliance Priority
Source Analyzer
Distribution Grid 
Model
Communication 
Engine
Channel Read/ 
Write Manager
Thingspeak Platform
Control 
layer
Cyber layer
Physical layer
Figure 10. Proposed communication architecture of microgrid.
5. Result Analysis and Discussion Proposed Method
The proposed controller is tested with the micro grid, as shown in Figure 1. Here,
researchers have described the simulated implementation of the distributed secondary
controller, on a multi-agent system platform, in addition to their correlation with the cloud
server and LAN. The multi-agent system was implemented in the MATLAB cluster connected to LAN via the network switch and connected to the cloud server via the Internet.
Local communication was carried out by the TCP/IP protocol, whereas the TCP protocol
conducted the communication between the cloud server and MAS. Communication between the agents was in the form of a client/server format with the help of Thing Speak
and could be conﬁgured for any network topology. In the Thing Speak-based communication system, every agent acted as the server, which waits for the incoming messages. It
can dispatch the messages to a corresponding technique since it was the neighbouring
server’s client.
6. Access to Internet Web Page
In this study, the researchers carried out a simulation test, where they described and
discussed the results of a decentralised power-management and control approach for micro

---


### Page 17

Int. J. Environ. Res. Public Health 2021, 18, 8146
17 of 24
grid in Energy Internet paradigm, which was implemented using the proposed algorithm
over the cloud platform for regulating the appliances in a smart home. As noted in software
communication and architecture interface, a MATLAB program was present for the Main
Command and Control Unit (MCCU), which helped organize all Thing Speak platforms.
The MQTT (Mosquitto) functions as a broker and bridges the home appliance subscription
and MCCU publishers’ gap. For regulating the home appliances through the MQTT
gateway, the researchers used a custom code derived from the proposed MATLAB-based
algorithm for its deployment. Here, the researchers designed a Thing Speak dashboard
interface, using a simple and effective user interface (UI), which allowed the homeowners
to access and interact with the home energy management service over the cloud system.
Figure 11 presents an internet web page that can be accessed in any internet browser after
entering and providing their username and password.
 
Figure 11. Thing-Speak platform.
This section discusses the effect of the microgrid communication system. The microgrid will exchange information in the presence of the communications device, such as
load consumption and power generation. To ensure power-sharing of microgrid operating
costs, the microgrid gets required power from a neighbouring microgrid. That means a
communication system provides the data needed to transfer power between the microgrids,
utilizing the IEEE 9 bus system in reference [54].
The experimental results noted in MATLAB for the power, voltage, and actual power
of every RERs have been presented in Figures 12 and 13. All renewable energy sources
in the microgrid autonomously alters their power output for fulﬁlling load demands.
Results for Scenarios indicated that a cloud server’s distributed MAS control for the remote
microgrid was an effective technique. This study extracts and simulates SPR-305E-WHT-D
solar. Table 1 lists these factors. Table 2. BUS generation and load parameters of IEEE 9 test
system [55].
PRi and DRi are the nominal active power generation and the reciprocal of frequency
droop gain of the inverter-based generator at bus i, respectively. PLi and DLi are the nominal
load and the frequency coefﬁcient of the load at bus I, respectively. PRi = 0 and DRi = 0
(PLi = 0 and DLi = 0) if no inverter-based generator (load) is connected to bus i.

---


### Page 18

Int. J. Environ. Res. Public Health 2021, 18, 8146
18 of 24
Figure 12. The graphical user interface of active power proﬁle.
Figure 13. The graphical user interface of the reactive-power proﬁle.
Table 1. Parameters of Photovoltaic.
Parameters
Values
Short-circuit current (Isc)
5.96 (A)
Parallel string
1
Maximum current Imp
5.58 (A)
Maximum voltage
 Vmp

54.7 (V)
Temperature coefﬁcient of (Voc)
−0.27269 (%/◦C)
Temperature coefﬁcient of (Isc)
0.061745 (%/◦C)
Shunt resistance (Rsh)
269.5934 Ω
Series resistance (Rs)
0.37152 Ω
Diode saturation curent Io
6.3 × 10−1 (A)
Series connected modules
7
Short-circuit current (Voc)
6.42 (V)
Number of cells
96

---


### Page 19

Int. J. Environ. Res. Public Health 2021, 18, 8146
19 of 24
Table 2. BUS generation and load parameters of IEEE 9 test system.
Bus
PRi (p.u.)
PLi (p.u.)
Vi (p.u.)
DRi (s)
DLi (s)
1
0.67
0
1
5
0
2
1.63
0
1
5
0
3
0.85
0
1
5
0
4
0
0
1
0
10−2
5
0
0.9
1
0
2
6
0
0
1
0
10−2
7
0
1
1
0
2
8
0
0
1
0
10−2
9
0
1.25
1
0
2
Figure 12 illustrates the graphical user interface of power proﬁle at demand scenario.
Figure 13 illustrates the graphical user interface of reactive power proﬁle at demand
scenario. The proposed system’s effectiveness of proposed scheme for remote microgrid
via cloud server is validated.
7. Results Discussion
The results are illustrated in Figures 12 and 13 Measurement of power sharing for all
renewable energy resources. It is noted from the results that:
1.
In both scenarios, as Figure 12 illustrates, the aims of active power sharing can be
accurately achieved.
2.
From Figure 13, the suggested system can realise accurate sharing of reactive power.
As the control objective of power sharing is to make sure both reactive and active
power sharing among generators follows renewable energy resources,
In the system’s case, the efﬁciency and effectiveness before applying the proposed
algorithm is 0.639. After implementing the suggested MAS method, efﬁciency of the
system is found to be 0.771. By comparing proposed algorithms with traditional method,
the proposed algorithm in our work saved 20.65%.
In the photovoltaic case, the efﬁciency and effectiveness before applying the proposed
algorithm is 0.677. Whereas after implementing the suggested MAS method, efﬁciency of
system is found to be 0.853. By comparing proposed algorithms with traditional methods,
the proposed algorithm in our work saved 25.99%.
In the diesel generator case, the efﬁciency and effectiveness before applying the
proposed algorithm is 0.653. Whereas after implementing the suggested MAS method,
efﬁciency of the system is found to be 0.883. By comparing proposed algorithms with
traditional methods, the proposed algorithm in our work saved 35.52%.
In the battery case, the efﬁciency and effectiveness before applying the proposed
algorithm is 0.687. Whereas after implementing the suggested MAS method, efﬁciency of
system is found to be 0.856. By comparing proposed algorithms with traditional methods,
the proposed algorithm in our work saved 24.59%.
In the power loss case, the efﬁciency and effectiveness before applying the proposed
algorithm is 2.541. Whereas after implementing the suggested MAS method, efﬁciency of
system is found to be 1.211. By comparing proposed algorithms with traditional methods,
the proposed algorithm in our work saved 52.34%.
The comparison between with and without corrective method is illustrated in Table 2.
Figure 14 shows the efﬁciency and effectiveness without the proposed MAS. Figure 15
shows the efﬁciency and effectiveness by using the proposed method. Figure 16 shows
the comparison between power loss without the proposed method and with the proposed
method. Figure 17 shows the improvement (%) by using the proposed method. Table 3
shows the difference between with and without the corrective method.

---


### Page 20

Int. J. Environ. Res. Public Health 2021, 18, 8146
20 of 24
Figure 14. The efﬁciency and effectiveness without proposed method.
Figure 15. The efﬁciency and effectiveness by using proposed method.
Figure 16. Comparison between power loss without proposed method and with proposed method.

---


### Page 21

Int. J. Environ. Res. Public Health 2021, 18, 8146
21 of 24
Figure 17. Improvement (%) by using proposed method.
Table 3. Difference between with and without corrective method.
Efﬁciency and
Effectiveness
Proposed
Method
Centralized
Percentage Improvement with
Proposed System (%)
ηsys
0.771
0.639
20.65%
ηPV
0.853
0.677
25.99
ηDG
0.885
0.653
35.52
ηBATT
0.856
0.687
24.59
Ploss
1.211
2.541
52.34%
8. Conclusions
This paper is intended to serve as a preliminary basis for quantifying the environmental and social beneﬁts resulting from microgrid implementation. This paper presents a new
cooperative controller for coordinating the multi renewable energy resources operation
using the IEEE 9 test feeder as the basis and with major modiﬁcations. The suggested
control scheme deﬁnes the data exchange within, and among, a multi agent system to
enable MG’s ﬂexible control in Internet of Energy. The proposed control objectives are
achieved with the evaluation of the stability considering network latency. The proposed
controller depends on the information transferring between the connected agents in the
MG system. In addition, the reactive/active power is optimally shared among the RERs.
The proposed controller improves the performance of the primary droop control method
that can’t adjust the MG-VF to their nominal values, and also, it does not enhance the
power-sharing among the RERs in MG. A hypothetical multi-agent MG system is designed
to prove the proposed controller’s effectiveness using the MATLAB/Simulink environment in the presence of the different scenarios in MG. In addition, this study presents a
hierarchical communication platform with a two-level structure, which is suitable for the
microgrid management system. The proposed platform uses TCP/IP for local microgrid
data exchange and as a backup communication method among microgrids in case of a
failure in the cloud level communication. Finally, for accessing the data related to the power
consumption of the individual loads, the researchers developed a reliable web portal associated with the Io T environment. The authors also provided a GUI after plotting a graph of
power consumption for determining the power usage of every appliance. The results presented the effectiveness of proposed methods in equally sharing the active/reactive power
of loads, during constant power load, and load change events. The controller proposed in
this paper achieved savings of 20.65% for the system, 25.99% for photovoltaic, 35.52 for
diesel generator, 24.59 for batteries, and 52.34% for power loss.

---


### Page 22

Int. J. Environ. Res. Public Health 2021, 18, 8146
22 of 24
Future extension of this work may include the integration of the Lo Ra WAN network,
with the proposed Io T architecture, because the use of the Lo Ra WAN technology could lead
to a very promising solution, due to its good coverage capabilities (both in outdoor and in
hybrid environments), whereas its most critical aspect is represented by the relatively low
data throughput and duty cycle limitation.
Author Contributions: B.N.A.: writing—original draft, methodology, software, and validation;
B.H.J.: supervisor, formal analysis, resources, investigation, editing, and writing—review; Z.-
A.S.A.R.: writing, and review; J.M.G.: supervision, writing—review, and editing; M.D.E.: supervision,
writing—review, funding, and editing. All authors have read and agreed to the published version of
the manuscript.
Funding: This research received no external funding.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Data sharing not applicable.
Conﬂicts of Interest: The authors declare no conﬂict of interest.
Nomenclature
Abbreviations & Acronyms
Renewable Energy Resources
RERs
Networked Renewable Energy Resources
NRERs
Peer-To-Peer
P2P
Internet of Things
Io T
Internet Protocol
IP
Transmission Control Protocol
TCP
Message Queuing Telemetry Transport
MQTT
Renewable Energy Technologies
RET
Distributed Energy Resources
DER
Multi Agent Systems
MAS
Internet Of Energy
Io E
Alternating Current
AC
Microgrid
MG
Direct Current
DC
Low Voltage
LV
Business Intelligence
BI
Local Area Network
LAN
Measurement Units
MU
Identity Document
ID
Application Programming Interface
API
Photovoltaic
PV
References
1.
Kumar, M. Social, Economic, and Environmental Impacts of Renewable Energy Resources. In Wind Solar Hybrid Renewable Energy
System; Okedu, K.E., Tahour, A., Aissaou, A.G., Eds.; Intech Open: London, UK, 2020. [Cross Ref]
2.
Liu, X.; Su, B. Microgrids—An integration of renewable energy technologies. In Proceedings of the 2008 China International
Conference on Electricity Distribution, Guangzhou, China, 10–13 December 2018. [Cross Ref]
3.
Alhasnawi, B.N.; Jasim, B.H. A New Coordinated Control of Hybrid Microgrids with Renewable Energy Resources under Variable
Loads and Generation Conditions. Iraqi J. Electr. Electron. Eng. 2020, 16, 1–20. [Cross Ref]
4.
Perez-Ibacache, R.; Silva, C.A.; Yazdani, A. Linear state-feedback primary control for enhanced dynamic response of AC
microgrids. IEEE Trans. Smart Grid 2019, 10, 3149–3161. [Cross Ref]
5.
Alhasnawi, B.N.; Jasim, B.H.; Anvari-Moghaddam, A.; Blaabjerg, F. A New Robust Control Strategy for Parallel Operated
Inverters in Green Energy Applications. Energies 2020, 13, 3480. [Cross Ref]
6.
Cucuzzella, M.; Incremona, G.P.; Ferrara, A. Decentralized sliding mode control of islanded AC microgrids with arbitrary
topology. IEEE Trans. Ind. Electron. 2017, 64, 6706–6713. [Cross Ref]

---


### Page 23

Int. J. Environ. Res. Public Health 2021, 18, 8146
23 of 24
7.
Hu, J.; Bhowmick, P. A consensus-based robust secondary voltage and frequency control scheme for islanded microgrids. Int. J.
Electr. Power Energy Syst. 2020, 116, 105575. [Cross Ref]
8.
Alhasnawi, B.N.; Jasim, B.H.; Esteban, M.D. A New Robust Energy Management and Control Strategy for a Hybrid Microgrid
System Based on Green Energy. Sustain. J. Rec. 2020, 12, 5724. [Cross Ref]
9.
Seyedi, Y.; Karimi, H.; Guerrero, J.M. Centralized disturbance detection in smart microgrids with noisy and intermittent
synchrophasor data. IEEE Trans. Smart Grid 2017, 8, 2775–2783. [Cross Ref]
10.
Garcia-Trivino, P.; Torreglosa, J.P.; Fernandez-Ramirez, L.M.; Jurado, F. Decentralized fuzzy logic control of microgrid for electric
vehicle charging station. IEEE J. Emerg. Sel. Power Electron. 2018, 6, 726–737. [Cross Ref]
11.
Alhasnawi, B.N.; Jasim, B.H.; Sedhom, B.E.; Hossain, E.; Guerrero, J.M. A New Decentralized Control Strategy of Microgrids in
the Internet of Energy Paradigm. Energies 2021, 14, 2183. [Cross Ref]
12.
Lu, X.; Chen, S.; Lü, J. Finite-time tracking for double integrator multiagent systems with bounded control input. IET Control
Theory Appl. 2013, 7, 1562–1573. [Cross Ref]
13.
Bidram, A.; Lewis, F.L.; Davoudi, A. Distributed control systems for small-scale power networks: Using multiagent cooperative
control theory. IEEE Control Syst. Mag. 2014, 34, 5677.
14.
Wang, Y.; Nguyen, T.L.; Syed, M.H.; Xu, Y.; Guillo-Sansano, E.; Nguyen, V.-H.; Burt, G.M.; Tran, Q.-T.; Caire, R. A Distrib-uted
Control Scheme of Microgrids in Energy Internet Paradigm and Its Multisite Implementation. IEEE Trans. Ind. Inform. 2021, 17,
1141–1153. [Cross Ref]
15.
Hou, X.; Sun, Y.; Lu, J.; Zhang, X.; Koh, L.H.; Su, M.; Guerrero, J.M. Distributed Hierarchical Control of AC Microgrid Oper-ating
in Grid-Connected, Islanded and Their Transition Modes. IEEE Access 2018, 6, 77388–77401. [Cross Ref]
16.
Shaﬁee, Q.; Guerrero, J.M.; Vasquez, J.C. Distributed Secondary Control for Islanded Microgrids—A Novel Approach. IEEE Trans.
Power Electron. 2014, 29, 1018–1031. [Cross Ref]
17.
Zhang, C.; Xu, Y.; Dong, Z.Y.; Yang, L.F. Multitimescale Coordinated Adaptive Robust Operation for Industrial Multienergy
Microgrids with Load Allocation. IEEE Trans. Ind. Inform. 2019, 16, 3051–3063. [Cross Ref]
18.
Molzahn, D.K.; Dorﬂer, F.; Sandberg, H.; Low, S.H.; Chakrabarti, S.; Baldick, R.; Lavaei, J. A Survey of Distributed Optimi-zation
and Control Algorithms for Electric Power Systems. IEEE Trans. Smart Grid 2017, 8, 2941–2962. [Cross Ref]
19.
Wang, Y.; Xu, Y.; Tang, Y.; Syed, M.H.; Guillo-Sansano, E.; Burt, G.M. Decentralised-distributed hybrid voltage regulation of
power distribution networks based on power inverters. IET Gener. Transm. Distrib. 2019, 13, 444–451. [Cross Ref]
20.
Ge, X.; Yang, F.; Han, Q.-L. Distributed networked control systems: A brief overview. Inf. Sci. 2017, 380, 117–131. [Cross Ref]
21.
Eskandari, M.; Li, L.; Moradi, M.H.; Siano, P.; Blaabjerg, F. Active Power Sharing and Frequency Restoration in an Autonomous
Networked Microgrid. IEEE Trans. Power Syst. 2019, 34, 4706–4717. [Cross Ref]
22.
Awal, M.A.; Yu, H.; Tu, H.; Lukic, S.M.; Husain, I. Hierarchical Control for Virtual Oscillator Based Grid-Connected and Islanded
Microgrids. IEEE Trans. Power Electron. 2020, 35, 988–1001. [Cross Ref]
23.
Weng, S.; Yue, D.; Dou, C.; Shi, J.; Huang, C. Distributed Event-Triggered Cooperative Control for Frequency and Voltage Stability
and Power Sharing in Isolated Inverter-Based Microgrid. IEEE Trans. Cybern. 2019, 49, 1427–1439. [Cross Ref] [Pub Med]
24.
Ding, L.; Han, Q.-L.; Zhang, X.-M. Distributed Secondary Control for Active Power Sharing and Frequency Regulation in Islanded
Microgrids Using an Event-Triggered Communication Mechanism. IEEE Trans. Ind. Inform. 2019, 15, 3910–3922. [Cross Ref]
25.
Mortezaei, A.; Simoes, M.G.; Savaghebi, M.; Guerrero, J.M.; Al-Durra, A. Cooperative Control of Multi-Master–Slave Islanded
Microgrid With Power Quality Enhancement Based on Conservative Power Theory. IEEE Trans. Smart Grid 2016, 9, 2964–2975.
[Cross Ref]
26.
Diaz, N.L.; Luna, A.C.; Vasquez, J.C.; Guerrero, J.M. Centralized Control Architecture for Coordination of Distributed Renewable
Generation and Energy Storage in Islanded AC Microgrids. IEEE Trans. Power Electron. 2017, 32, 5202–5213. [Cross Ref]
27.
Alhasnawi, B.N.; Jasim, B.H. A Novel Hierarchical Energy Management System Based on Optimization for Multi-Microgrid.
Int. J. Electr. Eng. Inform. 2020, 12, 586–606.
28.
Liu, X.-K.; Jiang, H.; Wang, Y.-W.; He, H. A Distributed Iterative Learning Framework for DC Microgrids: Current Sharing and
Voltage Regulation. IEEE Trans. Emerg. Top. Comput. Intell. 2018, 4, 119–129. [Cross Ref]
29.
Coelho, E.A.A.; Wu, D.; Guerrero, J.M.; Vasquez, J.C.; Dragicevic, T.; Stefanovic, C.; Popovski, P. Small-Signal Analysis of
the Microgrid Secondary Control Considering a Communication Time Delay. IEEE Trans. Ind. Electron. 2016, 63, 6257–6269.
[Cross Ref]
30.
Zhang, R.; Hredzak, B. Distributed Finite-Time Multiagent Control for DC Microgrids with Time Delays. IEEE Trans. Smart Grid
2019, 10, 2692–2701. [Cross Ref]
31.
Alhasnawi, B.N.; Jasim, B.H. A New Energy Management System Of On-Grid / Off-Grid Using Adaptive Neuro-Fuzzy Inference
System. J. Eng. Sci. Technol. 2020, 15, 3903–3919.
32.
Shahab, M.A.; Mozafari, B.; Soleymani, S.; Dehkordi, N.M.; Shourkaei, H.M.; Guerrero, J.M. Distributed Consensus-Based Fault
Tolerant Control of Islanded Microgrids. IEEE Trans. Smart Grid 2020, 11, 37–47. [Cross Ref]
33.
Yoo, H.-J.; Nguyen, T.-T.; Kim, H.-M. Consensus-Based Distributed Coordination Control of Hybrid AC/DC Microgrids.
IEEE Trans. Sustain. Energy 2020, 11, 629–639. [Cross Ref]
34.
Wu, X.; Xu, Y.; He, J.; Wang, X.; Vasquez, J.C.; Guerrero, J.M. Pinning-Based Hierarchical and Distributed Cooperative Control for
AC Microgrid Clusters. IEEE Trans. Power Electron. 2020, 35, 9865–9885. [Cross Ref]

---


### Page 24

Int. J. Environ. Res. Public Health 2021, 18, 8146
24 of 24
35.
Alhasnawi, B.N.; Jasim, B.H.; Rahman ZA, S.; Siano, P. A Novel Robust Smart Energy Management and Demand Reduction for
Smart Homes Based on Internet of Energy. Sensors 2021, 21, 4756. [Cross Ref]
36.
Alhasnawi, B.N.; Jasim, B.H.; Siano, P.; Guerrero, J.M. A Novel Real-Time Electricity Scheduling for Home Energy Management
System Using the Internet of Energy. Energies 2021, 14, 3191. [Cross Ref]
37.
Wang, Y.; Nguyen, T.-L.; Xu, Y.; Tran, Q.-T.; Caire, R. Peer-to-Peer Control for Networked Microgrids: Multi-Layer and MultiAgent Architecture Design. IEEE Trans. Smart Grid 2020, 11, 4688–4699. [Cross Ref]
38.
Bidram, A.; Davoudi, A.; Lewis, F.L. A multiobjective distributed control framework for islanded AC microgrids. IEEE Trans.
Ind. Informat. 2014, 10, 1785–1798. [Cross Ref]
39.
Simpson-Porco, J.W.; Shaﬁee, Q.; Dörﬂer, F.; Vasquez, J.C.; Guerrero, J.M.; Bullo, F. Secondary frequency and voltage control of
islanded microgrids via distributed averaging. IEEE Trans. Ind. Electron. 2015, 62, 7025–7038. [Cross Ref]
40.
Wu, X.; Shen, C.; Iravani, R. A Distributed, Cooperative Frequency and Voltage Control for Microgrids. IEEE Trans. Smart Grid
2018, 9, 2764–2776. [Cross Ref]
41.
Schiffer, J.; Seel, T.; Raisch, J.; Sezi, T. Voltage stability and reactive power sharing in inverter-based microgrids with consensusbased distributed voltage control. IEEE Trans. Control Syst. Technol. 2016, 24, 96–109. [Cross Ref]
42.
Simpson-Porco, J.W.; Dörﬂer, F.; Bullo, F. Synchronization and power sharing for droop-controlled inverters in islanded microgrids.
Automatica 2013, 49, 2603–2611. [Cross Ref]
43.
Forcan, M.; Maksimovi´c, M. Cloud-Fog-based approach for Smart Grid monitoring. Simul. Model. Pract. Theory 2020, 101, 101988.
[Cross Ref]
44.
Ortiz, L.; Orizondo, R.; Águila, A.; González, J.W.; López, G.J.; Isaac, I. Hybrid AC/DC microgrid test system simulation:
Grid-connected mode. Heliyon 2019, 5, 12. [Cross Ref] [Pub Med]
45.
Alhasnawi, B.N.; Jasim, B.H. Adaptive Energy Management System for Smart Hybrid Microgrids. In Proceedings of the 3rd
Scientiﬁc Conference of Electrical and Electronic Engineering Researches (SCEEER), Basrah, Iraq, 15–16 June 2020. [Cross Ref]
46.
Alhasnawi, B.N.; Jasim, B.H.; Issa, W.; Esteban, M.D. A Novel Cooperative Controller for Inverters of Smart Hybrid AC/DC
Microgrids. Appl. Sci. 2020, 10, 6120. [Cross Ref]
47.
Qiu, H.; Zhao, B.; Gu, W.; Bo, R. Bi-Level Two-Stage Robust Optimal Scheduling for AC/DC Hybrid Multi-Microgrids. IEEE Trans.
Smart Grid 2018, 9, 5455–5466. [Cross Ref]
48.
Xu, Y.; Sun, H.; Gu, W.; Xu, Y.; Li, Z. Optimal Distributed Control for Secondary Frequency and Voltage Regulation in an Islanded
Microgrid. IEEE Trans. Ind. Inform. 2019, 15, 225–235. [Cross Ref]
49.
Kyprianidis, K.; Dahlquist, E. (Eds.) Consensus Control of Distributed Battery Energy Storage Devices in Smart Grids. In AI and
Learning Systems—Industrial Applications and Future Directions, Konstantinos Kyprianidis and Erik Dahlquist; Intech Open: London,
UK, 2021. [Cross Ref]
50.
Tajalli, S.Z.; Mardaneh, M.; Taherian-Fard, E.; Izadian, A.; Kavousi-Fard, A.; Dabbaghjamanesh, M.; Niknam, T. Do S-Resilient
Distributed Optimal Sched-uling in a Fog Supporting IIo T-Based Smart Microgrid. IEEE Trans. Ind. Appl. 2020, 56, 2968–2977.
[Cross Ref]
51.
Alhasnawi, B.N.; Jasim, B.H. A new internet of things enabled trust distributed demand side management system. Sustain. Energy
Technol. Assess. 2021, 46, 101272.
52.
Marzal, S.; González-Medina, R.; Salas-Puente, R.; Garcerá, G.; Figueres, E. An Embedded Internet of Energy Communication
Platform for the Future Smart Microgrids Man-age-ment. IEEE Internet Things J. 2019, 6, 7241–7252. [Cross Ref]
53.
Alhasnawi, B.N.; Jasim, B.H.; Esteban, M.D.; Guerrero, J.M. A Novel Smart Energy Management as a Service over a Cloud
Computing Platform for Nanogrid Appliances. Sustain. J. Rec. 2020, 12, 9686. [Cross Ref]
54.
Guo, Z.; Pinson, P.; Chen, S.; Yang, Q.; Yang, Z. Chance-Constrained Peer-to-Peer Joint Energy and Reserve Market Considering
Renewable Generation Uncertainty. IEEE Trans. Smart Grid 2021, 12, 798–809. [Cross Ref]
55.
Song, Y.; Hill, D.J.; Liu, T. Small-Disturbance Angle Stability Analysis of Microgrids: A Graph Theory Viewpoint. IEEE Conf.
Control. Appl. 2015. [Cross Ref]

---
