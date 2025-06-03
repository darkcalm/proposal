

---

Page 1

---

 
Operation Orchestration of Local Energy Communities through
Digital Twin
Citation for published version (APA):
Nguyen, A., Tran, T., Tran, M.-Q., Nguyen, P. H., & Slootweg, J. G. (2022). Operation Orchestration of Local
Energy Communities through Digital Twin: A Review on suitable Modeling and Simulation Approaches. In
ENERGYCON 2022 - 2022 IEEE 7th International Energy Conference, Proceedings Article 9830264 Institute of
Electrical and Electronics Engineers. https://doi.org/10.1109/ENERGYCON53164.2022.9830264
DOI:
10.1109/ENERGYCON53164.2022.9830264
Document status and date:
Published: 21/07/2022
Document Version:
Accepted manuscript including changes made at the peer-review stage
Please check the document version of this publication:
• A submitted manuscript is the version of the article upon submission and before peer-review. There can be
important differences between the submitted version and the official published version of record. People
interested in the research are advised to contact the author for the final version of the publication, or visit the
DOI to the publisher's website.
• The final author version and the galley proof are versions of the publication after peer review.
• The final published version features the final layout of the paper including the volume, issue and page
numbers.
Link to publication
General rights
Copyright and moral rights for the publications made accessible in the public portal are retained by the authors and/or other copyright owners
and it is a condition of accessing publications that users recognise and abide by the legal requirements associated with these rights.
            • Users may download and print one copy of any publication from the public portal for the purpose of private study or research.
            • You may not further distribute the material or use it for any profit-making activity or commercial gain
            • You may freely distribute the URL identifying the publication in the public portal.
If the publication is distributed under the terms of Article 25fa of the Dutch Copyright Act, indicated by the “Taverne” license above, please
follow below link for the End User Agreement:
www.tue.nl/taverne
Take down policy
If you believe that this document breaches copyright please contact us at:
openaccess@tue.nl
providing details and we will investigate your claim.
Download date: 03. Jun. 2025


---

Page 2

---

Operation Orchestration of Local Energy
Communities through Digital Twin: A Review on
suitable Modeling and Simulation Approaches
Thien-An Nguyen-Huu1, Trung Thai Tran1, Minh-Quan Tran1, Phuong H. Nguyen1, JG Slootweg1,2
1 Department of Electrical Engineering, Eindhoven University of Technology, Eindhoven, The Netherlands
2 Enexis Netbeheer, ’s-Hertogenbosch, The Netherlands
{an.nguyen.huu.thien, t.t.tran, m.q.tran, p.nguyen.hong, j.g.slootweg}@tue.nl
Abstract—Increasing the integration of distributed energy
resources (DERs) requires an orchestration of the existing cen-
tralized management system used for the electricity grid and the
emerging distributed ones for local energy communities (LEC).
To support this orchestration, design and operation strategies of
LECs needs to be analysed, based on a so-called Digital Twin
(DT) platform with suitable modeling and simulation techniques.
This paper presents a set of requirements needed to develop DT,
thus enabling operation orchestration of LECs. Based on these
specific requirements, a comprehensive review on the relevant
physics-based and data-driven models will be discussed, especially
focusing on the flexibility profile of LEC based on data-driven
model to support the balancing reserves to the electricity grid.
Index Terms—Digital twin, Local Energy Community, physics-
based model, data-driven model, flexibility profile.
I. INTRODUCTION
Electrical energy systems worldwide are under a rapid
transformation as a result of technological changes, and am-
bition to achieve the target of climate neutrality. The increase
of small-scale, environmental-friendly distributed energy re-
sources (DERs), e.g., solar photovoltaic (PV), wind turbine,
battery systems (BESS), electric vehicles (EVs), or heat pumps
(HPs) requires the change of the centralized paradigm to man-
age the electrical energy systems to evolve toward distributed
ones which are adopted for local energy communities (LEC).
In Fig. 1, each LEC represents a locally and collectively
organized energy system that consists of a number of houses
and/or buildings, and have a variety of local generations of heat
and electricity, flexible storage systems and demands. LEC is
not only capable of self-provision of energy, but also sharing
resources with other LECs to make efficient use of most energy
available, and contribute to ancillary services such as balancing
reserves, reactive power supporting.
Due to the diversity of sub-systems included (integrated
buildings with on-site DERs within the LEC), an orchestration
between LECs and the electricity grid is crucial to harmonise
various management and operational objectives. To enable
such the orchestration, Digital twin (DT) has emerged as a
promising approach to reflect the best models with real-time
The authors would like to acknowledge the financial support for this
work from RVO funded TROEF project (no. MOOI32025), https://www.troef-
energy.nl/, and the FlexiGrid project that is funded by the European Com-
munity’s Horizon 2020 Framework Programme under grant agreement (no.
864048), https://flexigrid.org/.
Fig. 1. LEC and electricity grid through Digital Twin.
updated information to emulate the complete characteristics,
actions, operations, as well as life cycle of actual systems with
potential services [1]. It is based on selecting proper modeling
and simulation tools to capture fully steady-state and dynamic
behaviours of each component and the overall integrated
systems. The existing modeling approaches and simulation
tools have focused either electricity networks or local energy
systems, while interaction between these two systems (e.g.,
utility grid vs. LEC) is not comprehensively addressed. There
are some works done to fill in this gap, e.g., NEPLAN [2],
DEMKit [3], which provides tools to analyze, plan, optimize
and simulate large-scale electrical networks. However, these
tools are only for case specific while the generic approach is
missing to replicate in large system areas, with the possibility
for various services, such as demand respond programs, or
market structures.
In this paper, we specify on requirements needed to de-
velop a DT platform to enable the orchestration of LECs
and the electricity networks. A comprehensive review on the
current state of the art (SotA) in modeling and simulations
for integrated energy systems (electricity grids and LECs)
will be conducted to find a suitable approach so that the
local control strategies available for sub-systems (building,
building neighborhood) will be listed and reflected on available
modeling approaches.
Firstly, a possible DT framework for a LEC is presented in
Section II. Then, the current SotA modeling and simulation
tools is shown in Section III. Section IV shows the mapping
of the DT requirements to available modeling approaches.


---

Page 3

---

Fig. 2. Digital twin framework for Local Energy Community.
II. DIGITAL TWIN FRAMEWORK FOR LEC
In this paper, we present a possible framework for DT plat-
form, focusing on a virtual testing environment for a specific
LEC located in the Bunnik, the Netherlands, as shown in
Fig. 2. This environment represents (almost) identical charac-
teristics as the real system; and includes model library, twining
services, and the integrated energy analysis. The developed
platform is essential for assessing the value and profitability of
energy communities, and optimisation of the (system) design.
Being considered as a living lab, the LEC in Bunnik has 8
office buildings including PV rooftop systems, EV charging
stations, BESS connected in a ring network topology through
some medium voltage (MV)/low voltage (LV) transformers.
Through a bi-directional exchange of information between the
virtual testing and physical environment, the efficiency of both
systems is continuously enhanced.
A. Model library
The developed library contains various (physics-based
and/or data-driven) component models to build and examine
exactly the behaviors of both components and complete LECs.
The developed library enables four modeling levels, including
components level (PV, FERs, base load), building level (resi-
dential building, office building), multiple building/LEC level,
and electricity grids level. Depending on the applications,
the physics-based models are formulated mathematically in
detailed or simplified approaches. Thanks to the cutting-edge
Artificial Intelligence (AI) technologies, behaviors which are
difficult to model by physics-based model can be captured by
data-driven models or a combination of these methods, using
machine learning techniques taking into account historical
data. In the model library, the LEC profiles (PV, base-load,
flexibility) are generated by leveraging some existing applica-
tion programming interfaces (APIs) such as Artificial Load
Profile Generator (ALPG) [4], Load Profile Generator [5],
Residential load profile based on gaussian mixture model [6]
or multivariate elliptical copulas model [7]. The model library
is developed in Python open source to facilitate replication
both in academia and industry.
B. Twining Services
The twining services provide different functionalities to
develop control strategies for included sub-systems (e.g.,
buildings or building neighbourhoods) to analyse and opti-
mize their coordination, e.g., automatic frequency restoration
reserve (aFRR). The twining services are developed based on
Fig. 3. Twining services considering in Time scale dimension.
Fig. 4. Load and PV profile of a LEC.
several objectives, such as minimize costs, maximize the pen-
etration of renewable energy resources and minimize energy
consumption. In this part, market integration is one of the
important factors that should be considered in this platform to
develop the control strategies. For instance, the market price
information from the electricity market is used in aFRR service
to maximize profit of LEC and optimize the performance of
BESS.
C. Integrated energy analysis
The outputs of the twining services are the profiles of
LEC, buildings, or components. Based on these outputs, the
integrated energy analysis is developed for different stake-
holder purposes. The energy analysis can be done by various
developed power flow calculation depending on the purpose of
the analysis and the complexity of the systems. Another option
is considering open sources such as OpenDSS, Pandapower,
Pypsa, Pypower. Hardware-in-the-loop testing environment is
used to implement validation of the developed models and
control strategies in a real-time digital simulator named OPAL-
RT platforms connecting with the Matlab software. Lastly,
the visualization module will be developed in our platform
to deliver the results to end-users.
D. Modeling and Simulation Requirements
To employ the DT platform for orchestrating operation of
LEC and the electricity grid, there is a variety of requirements
that need to be taken into account. The hypothetical LEC
consists of 10 to 100 houses and/or buildings, with aggregated
PV systems in a range of 100 kW - 300 kW, and flexible
energy resources (FERs) such as BESS, EVs, and EV charging
stations, heat pump systems. The LEC is normally connected
to the electricity grid through a transformer 22/0.4 kV, as
depicted in Fig. 1.
Besides the aspects of system and profile data requirements,
the time scale dimension (see Fig. 3) is also one of the
important factors that needs to be considered for setting up a
DT platform. Depending on the analytical needs of the stake-
holders, the DT platform can be developed to model different


---

Page 4

---

levels, ranging from component [8], household/building [7],
[9], and complete LEC level [10], to distribution [11], [12],
and grid/market interaction level [13]. Each modeling level
corresponds to a specific time-scale frame (from microsecond
to years or longer). In the future work, we will focus on the
highlighted area (the quasi-dynamics time scale) to investigate
scenarios and optimal algorithm for DER control and coordi-
nation, building(s) and LEC energy management to show the
flexibility value, peak reduction, optimal energy consumption
within LEC based on DT platform.
In Fig. 4, PV and load profiles for an individual household
and the aggregated community are presented that a residential
area will generate a lot of energy during the day and especially
consume energy in the evening. The individual household
profile or the aggregated profile of the LEC are modeled using
a day data with 15-minute resolution. The blue and yellow
lines represent the total power consumption and PV generation
of 55 households in a LEC assuming the households have
the same consumption and PV generation data, respectively.
However, in practice, if there is enough data from the smart
meter, the red and purple lines illustrate accurately the total
power consumed and PV generation from these households,
respectively. There is a relative difference between the actual
measured data and the assumption of lack of data. In fact, PVs
in each house are installed in the same geographical area where
are the same weather conditions (irradiance, temperature).
However, because each installed PV capacity is different in
each house, so the PV generation is not equal. This shows
the importance of the data-driven model in implementing DT
platforms. In addition, the load and PV profiles of LEC also
show a surplus generated from PV that has not been fully
utilized in households. This enables the twining services of
the LEC to be able to make the most of this surplus energy,
such as providing balancing reserves [13]–[16] or exchanging
energy [17]–[19] to other LECs.
III. REVIEW ON MODELING APPROACHES
Due to the diversity of network configurations and involved
components, it is hard to find a unique, general representation
of LECs. There are various modeling approaches in the
literature that can be applied to model LECs. The following
section aims to review different aspects of available model-
ing and simulation techniques, tools that are useful for the
development of LEC Digital Twin models.
A. Physics-based Model
The classical approach uses mathematical representations of
physical systems to derive the components and the whole LEC
model. Herewith, it is classified as physics-based model. In
this approach, usually, each component of LEC is modelled by
component-based approach, then aggregated to obtain a com-
plete LEC model. The mathematical model of each component
is obtained based on detailed knowledge of actual devices.
Then, a high order state space model, which can be represented
for most engineering systems, is used to simulate a complete
LEC in a standard form as follows:
˙x(t) = Ax(t) + Bu(t)
y(t) = Cx(t) + Du(t)
(1)
where x(t), y(t), u(t) are the vectors of system state, output,
and input; A, B, C, D are the matrices of state, input and
output, and feed-forward.
The complexity of aggregated models can be reduced by
applying simplification techniques, such as order reduction
methods, or neglecting several dynamics of the system that
are not necessary for certain research purposes. Several ap-
plications of this type of model for DERs can be found in
[8], [10], [11], [20], [21]. In [11], [20], one-year time-series
power flow is executed using OpenDSS platform to calculate
state variables such as voltage magnitude, currents and powers
in LEC based on physics-based model. Authors in [8], [10],
[22] proposed coupled sequence components based models of
DER, load devices to conduct the transient stability analysis
of LEC. The proposed component-based models of DERs can
reflect the behavior of actual systems with a high level of detail
which reduce computational time while maintaining accurate
dynamics.
In most power system studies, static load models such as
constant impedance/current/power, ZIP or exponential models
which provide adequate accuracy for steady-state or semi
steady-state studies. However, the static models have a disad-
vantages of less accuracy in capturing the transient dynamics
of the power electronic load devices.
FERs, including BESS, plug-in EVs, thermal (TESS) and
hydrogen (HESS) energy storage systems, are essential com-
ponents for flexible and reliable operations of LECs. Typically,
BESS [23], [24] and storage system of EVs [25] can be
modeled as (nonlinear or linear) equivalent circuit model [26],
or electrochemical model in term of their state of charge [27].
Similar to BESS, TESS and HESS can be modeled in term
of thermal balance [28] and level of stored hydrogen [29],
respectively.
The electricity grid can be modeled in various ways,
depending on the purposes of system analyses. Electrical
networks can be modeled as equivalent (multi-) port networks
using network and port theory [30], or equivalent models
using the Thevenin theorem [31]. In [32], [33], the state-
space model of a multi-bus electrical network is developed
through linearization of equations describing components in
the system, including power electronics-based converters, con-
trollers, electrical topology of the system described by nodal
admittance matrix, and impedance-equivalent load models.
These models can be used to evaluate system stability and
performance, as well as component-, system-level controller
designs.
B. Data-driven Model
It is known that a formulation of mathematical models
requires detailed knowledge of the actual system (including
steady-state, dynamics behavior and uncertainties), hence not
being applicable for LEC with a complex structure. The inte-
gration of information and communication technologies, and


---

Page 5

---

advanced measurement infrastructure enables the development
of data-driven approaches that can satisfy the growing demand
for accurate, scalable LEC modeling.
Accurate data-driven modeling approaches for DERs (PV,
Wind turbine) are discussed in [34], [35], in which the models
are design based on only representative sub-datasets from
large DER input data, selected by a crucial pre-processing
step. By doing this way, extreme large amount of unnecessary
computation is reduced while the completeness and accuracy
of the developed models is still guaranteed. Furthermore, the
direct forecasting model for PV power generation is developed
directly using PV power output historical data samples is
discussed in [36].
The EV charging stations can be represented by stochastic
models, as proposed in [37]–[39]. These models also include
uncertainties, such as charging classes, charging load profiles,
and location of the EVs. The high accuracy of these models
allows various studies for grid supporting services of these
flexible resources.
To enhance the static load models, proper stochastic mod-
eling of load consumption is required in different types of
studies such as modern grid planning, quantification of impact
of low carbon technologies, finding secure levels of penetration
of PV generation, and LV state estimation as in [7], [40]–
[42]. The main purpose of these approaches is to capture the
statistical properties of the smart meter measurement dataset
to generate the load profiles.
For electrical networks, dynamic equivalent models using
measurement data are powerful modeling approaches that can
be used for various applications [43]. The Prony analysis
[44], and System identification technique [45] use the input
and output measurement data to generate a black-, grey-
box models of the system structure without requiring full
knowledge of system structure and parameters.
As an example, a general architecture of Deep Reinforce-
ment Learning (DRL) to optimize the electricity consump-
tion of devices in residential buildings and aggregations of
buildings is shown in [9]. The combination of Reinforcement
Learning and Deep Neural Network enables powerful models
for the online cost minimization problem in a large systems
with high uncertainties of electrical patterns.
In [7], the authors proposed a top-down data-driven model-
ing approach named conditional multivariate elliptical copulas
for generating the resident load profiles in quasi-dynamic
time frame. The proposed approach unifies the consumption
modeling for MV and LV networks, simulating active power
consumption scenarios in flexible time horizons for a whole
year. Based on a one-year smart meter data, the power flow
analysis generates training data sets for a data-driven state
estimation for LEC requiring more accurate and lower com-
putational burden in [46]. The state estimation was designed
based on the physical connections of the distribution network
and the position of the phasor measurement unit (PMU). The
authors in [47] presented a probabilistic approach for grid
supportive demand side management based on Monte Carlo as
well as Neural Network method to reduce the probability of
Distribution
DERs
Customer Promise
Bussiness
Layer
Function 
Layer
Information 
Layer
Congestion & 
voltage management
Digital Twin (DT)
Network models
DT
DERs 
model
Building(s) energy 
managments 
optimization
Simulated use-cases
AI - based grid-egde
control coordination
DT
Building 
model
Fig. 5. Digital Twin architecture built in SGAM model.
geographical dependent operation limit violations considering
in quasi-dynamic time domain. In [48], a stochastic optimiza-
tion model is used for the optimal operation for an LEC. The
mixed-integer linear programming (MILP) model minimizes
both the operation cost and CO2 emission of LEC which is
run with a one-hour time resolution for one day. The MILP
model was implemented and solved in AMPL and CPLEX.
An online state of charge and state of health estimation of
BESS [49] is explored by DT platform with equivalent circuit
models and all battery relevant data measured and transmitted
to the cloud thank to the Internet of Energy.
IV. MAPPING THE REQUIREMENTS OF DIGITAL TWIN TO
AVAILABLE MODELING
Most of the related articles using the DT platform focus on
individual applications, the operation orchestration between
the LEC and the grid has not been taken into account
[50]–[54]. In order to orchestrate the operation of LEC and
the electricity grid through DT, the mapping of a variety
of requirements discussed in Section II with current SotA
model and simulation tools is essential. Table I illustrates a
classification of SotA studies on LEC and DERs through DT
and conventional approach.
The peak load shaving use case [55] includes three main
strategies which are demand-side management, BESS and EV
integration between LEC and the electricity grid. The opti-
mization and control models for peak load shaving strategies
are implemented both in the data-driven model [56] and the
physics-based model [57]. In order to perform peak load
shaving strategies, various requirements of system character-
istics are detailed in table I, including the number of houses,
the total of PV generation, FER parameters, network topol-
ogy, as well as measurement data in 15 minutes resolution.
The remaining use cases, including building load forecasting,
self-sufficiency scheduling, balancing reserve, congestion and
voltage management, and smart mobility charging station,
take into account additional requirements, depending on the
coupling features of the use-cases, e.g., occupancy levels or
thermal conversions. The profile requirements, besides data
from smart meter, important data such as weather condition,
cost rate, and assigned data from transmission/distribution
system operators (TSO, DSOs) are also considered in DT
platform for LEC.


---

Page 6

---

TABLE I
MAPPING REQUIREMENTS FOR EACH DT USE-CASES TO RELEVANT
MODELING AND SIMULATIONS METHODS
Use cases
of DT
Requirements
Modeling/ Simulation tools
System
Profile
Data-driven
models
Physics-based
models
Peak load
shaving
• 10 - 100 households
• 100 - 300 kWp PV
• FERs: BESS, EV, HP
• 22/0.4kV grid topologies
• Smart meter data
• EV pattern profiles
• Radiance profiles
• Temp. profiles
[56]
[57]
Building load
and
production
forecasting
• Building features
• 10 - 100 kWp PV
• FERs: BESS, EV, HP
• Thermal conversions
• Smart meter data
• EV pattern profiles
• Occupancy profiles
[1], [7],
[17], [19],
[36], [40]
[1], [17],
[19]
Building/LEC
self-
sufficiency
• Building features
• 10 - 100 kWp PV
• FERs: BESS, EV, HP
• Thermal conversions
• Forecasted building load
data
• EV pattern profiles
• Forecasted PV profiles
[41], [45],
[48]
[48]
Balancing
reserve
• Building features
• 10 - 300 kW/kWh BESS
• Building thermal inertia
• Assigned data from TSO
• Scheduled energy profiles
[13]–[15],
[21]
[13]–[15],
[21]
Congestions
and Voltage
management
• 10 - 100 households
• 100 - 300 kWp PV
• FERs: BESS, EV, HP
• 22/0.4kV grid topologies
• Assigned data from DSO
• Weather data
[11]
[20]
Smart
charging
same as above
• Market price data
• Network residual capacity
data
• EV pattern profile data
[25], [37],
[39], [52]
[26], [27],
[38]
In TROEF project, the architecture of DT platform is
designed in the smart grid architecture model (SGAM) [58],
including three layers as shown in Fig. 5. The Information
layer consists of network models (quasi-dynamic models of
network assets, e.g., transformers, cable lines, network topolo-
gies), DER models (on-site PV, wind, batteries, EV charging
and associated parameters), and building models (e.g., thermal-
electric models of buildings with potential flexibility gained
from thermal mass). The functional layer has various different
use–cases for residential building, building-related generation
systems, controllable building installations, utility building,
electric mobility impact, analyzing potential problem of con-
gestion and voltage management in distribution system, AI-
based DER coordination, and building(s) energy management
optimization. The business layer aims to develop DT platform
with the involvement of business actors such as solution
or algorithm developers, building owner or operators, local
authorities (e.g., municipalities), distribution system operator.
Based on system and data requirements for the development
of DT platform, it is possible to apply and improve the
current SotA model and simulation tools to fulfill the technical
requirements proposed in the SGAM model of TROEF project.
V. CONCLUSION
This papers aims to present an overview about possible
modeling and simulation methods needed while considering
the integration between Local energy community (LEC) and
the electricity grid through Digital Twin (DT) platform. The
analysis specifies on the requirements needed for developing a
Digital Twin platform which enables the operation orchestra-
tion between the LEC and the electricity grid. Based on this
development of DT, generating individual household/building
profiles as well as the aggregated ones for LECs play a crucial
role which can be realized via either physics-based or data-
driven models. In the future work, this topic will be addressed
comprehensively along with potential flexibility from the LEC
which can provide balancing reserves to the electricity grid.
REFERENCES
[1] E. O’Dwyer, I. Pan, R. Charlesworth, S. Butler, and N. Shah, “Integra-
tion of an energy management tool and digital twin for coordination and
control of multi-vector smart energy systems,” Sustainable Cities and
Society, vol. 62, nov 2020.
[2] [Online]. Available: https://www.neplan.ch/
[3] G. Hoogsteen, J. L. Hurink, and G. J. Smit, “DEMKit: A Decentralized
Energy Management Simulation and Demonstration Toolkit,” Proceed-
ings of 2019 IEEE PES Innovative Smart Grid Technologies Europe,
ISGT-Europe 2019, pp. 13–17, 2019.
[4] G. Hoogsteen, A. Molderink, J. L. Hurink, and G. J. Smit, “Generation
of flexible domestic load profiles to evaluate demand side management
approaches,” in 2016 IEEE International Energy Conference (ENERGY-
CON).
IEEE, 2016, pp. 1–6.
[5] N. Pflugradt, J. Teuscher, B. Platzer, and W. Schufft, “Analysing low-
voltage grids using a behaviour based load profile generator,” in Inter-
national conference on renewable energies and power quality, vol. 11,
2013, p. 5.
[6] G. J. McLachlan, S. X. Lee, and S. I. Rathnayake, “Finite mixture
models,” Annual review of statistics and its application, vol. 6, pp. 355–
378, 2019.
[7] E. M. S. Duque, P. P. Vergara, P. H. Nguyen, A. Van Der Molen, and
J. G. Slootweg, “Conditional Multivariate Elliptical Copulas to Model
Residential Load Profiles from Smart Meter Data,” IEEE Transactions
on Smart Grid, vol. 12, no. 5, pp. 4280–4294, sep 2021.
[8] M. H. Roos, P. H. Nguyen, J. Morren, and J. G. Slootweg, “Modeling
and Experimental Validation of Power Electronic Loads and DERs for
Microgrid Islanding Simulations,” IEEE Transactions on Power Systems,
vol. 35, no. 3, pp. 2279–2288, may 2020.
[9] E. Mocanu, D. C. Mocanu, P. H. Nguyen, A. Liotta, M. E. Webber,
M. Gibescu, and J. G. Slootweg, “On-line building energy optimization
using deep reinforcement learning,” IEEE transactions on smart grid,
vol. 10, no. 4, pp. 3698–3708, 2018.
[10] M. Roos, P. Nguyen, J. Morren, and J. G. Slootweg, “Direct-Quadrature
Sequence Models for Energy-Function Based Transient Stability Anal-
ysis of Unbalanced Inverter-Based Microgrids,” IEEE Transactions on
Smart Grid, vol. 12, no. 5, pp. 3692–3704, sep 2021.
[11] T. T. Mai, A. N. M. Haque, P. P. Vergara, P. H. Nguyen, and G. Pemen,
“Adaptive coordination of sequential droop control for pv inverters to
mitigate voltage rise in pv-rich lv distribution networks,” Electric Power
Systems Research, vol. 192, p. 106931, 2021.
[12] P. P. Vergara, T. T. Mai, A. Burstein, and P. H. Nguyen, “Feasibility and
Performance Assessment of Commercial PV Inverters Operating with
Droop Control for Providing Voltage Support Services,” in Proceedings
of 2019 IEEE PES Innovative Smart Grid Technologies Europe, ISGT-
Europe 2019. Institute of Electrical and Electronics Engineers Inc., sep
2019.
[13] S. F. Contreras, C. A. Cortes, and J. M. Myrzik, “Optimal microgrid
planning for enhancing ancillary service provision,” Journal of Modern
Power Systems and Clean Energy, vol. 7, no. 4, pp. 862–875, 2019.
[14] Y. Zhou, Z. Wei, G. Sun, K. W. Cheung, H. Zang, and S. Chen, “A
robust optimization approach for integrated community energy system
in energy and ancillary service markets,” Energy, vol. 148, pp. 1–15,
2018.
[15] H. Firoozi, H. Khajeh, and H. Laaksonen, “Optimized operation of
local energy community providing frequency restoration reserve,” IEEE
Access, vol. 8, pp. 180 558–180 575, 2020.
[16] R. Rana, K. Berg, M. R. Brubæk, and O. B. Fosso, “Ancillary services
from a residential community-a norwegian case study,” in 2021 Interna-
tional Conference on Smart Energy Systems and Technologies (SEST).
IEEE, 2021, pp. 1–6.
[17] R. Faia, J. Soares, T. Pinto, F. Lezama, Z. Vale, and J. M. Corchado,
“Optimal model for local energy community scheduling considering peer
to peer electricity transactions,” IEEE Access, vol. 9, pp. 12 420–12 430,
2021.
[18] E. Kremers, “Intelligent local energy management through market
mechanisms: Driving the german energy transition from the bottom-up,”
Energy Reports, vol. 6, pp. 108–116, 2020.


---

Page 7

---

[19] M. Stephant, D. Abbes, K. Hassam-Ouari, A. Labrunie, and B. Robyns,
“Distributed optimization of energy profiles to improve photovoltaic
self-consumption on a local energy community,” Simulation Modelling
Practice and Theory, vol. 108, p. 102242, 2021.
[20] P. P. Vergara, T. T. Mai, A. Burstein, and P. H. Nguyen, “Feasibility and
Performance Assessment of Commercial PV Inverters Operating with
Droop Control for Providing Voltage Support Services,” in Proceedings
of 2019 IEEE PES Innovative Smart Grid Technologies Europe, ISGT-
Europe 2019. Institute of Electrical and Electronics Engineers Inc., sep
2019.
[21] M. Roos, D. Geldtmeijer, H. Nguyen, J. Morren, and J. Slootweg,
“Optimizing the technical and economic value of energy storage systems
in lv networks for dno applications,” Sustainable Energy, Grids and
Networks, vol. 16, pp. 207–216, 2018.
[22] M. H. Roos, P. H. Nguyen, J. Morren, and J. Slootweg, “Aggregation
of component-based grid-feeding der and load models for simulation of
microgrid islanding transients,” Electric Power Systems Research, vol.
189, p. 106759, 2020.
[23] C. Parthasarathy, H. Hafezi, and H. Laaksonen, “Lithium-ion bess
integration for smart grid applications-ecm modelling approach,” in 2020
IEEE Power & Energy Society Innovative Smart Grid Technologies
Conference (ISGT).
IEEE, 2020, pp. 1–5.
[24] T.-A. Nguyen-Huu, V. T. Nguyen, K. Hur, J. W. Shim et al., “Coor-
dinated control of a hybrid energy storage system for improving the
capability of frequency regulation and state-of-charge management,”
Energies, vol. 13, no. 23, p. 6304, 2020.
[25] G. Piazza, S. Bracco, F. Delfino, and S. Siri, “Optimal design of electric
mobility services for a local energy community,” Sustainable Energy,
Grids and Networks, vol. 26, p. 100440, 2021.
[26] A. Farmann and D. U. Sauer, “Comparative study of reduced order
equivalent circuit models for on-board state-of-available-power predic-
tion of lithium-ion batteries in electric vehicles,” Applied Energy, vol.
225, pp. 1102–1122, sep 2018.
[27] J. Schmalstieg, C. Rahe, M. Ecker, and D. U. Sauer, “Full Cell Parame-
terization of a High-Power Lithium-Ion Battery for a Physico-Chemical
Model: Part I. Physical and Electrochemical Parameters,” Journal of The
Electrochemical Society, vol. 165, no. 16, pp. A3799–A3810, 2018.
[28] G. Alva, Y. Lin, and G. Fang, “An overview of thermal energy storage
systems,” Energy, vol. 144, pp. 341–378, 2018.
[29] M. Becherif, H. Ramadan, K. Cabaret, F. Picard, N. Simoncini, and
O. B´ethoux, “Hydrogen energy storage: new techno-economic emer-
gence solution analysis,” Energy Procedia, vol. 74, pp. 371–380, 2015.
[30] M. Ili´c, R. Jaddivada, and X. Miao, “Modeling and analysis methods for
assessing stability of microgrids,” IFAC-PapersOnLine, vol. 50, no. 1,
pp. 5448–5455, 2017.
[31] M. Naderi, Y. Khayat, Q. Shafiee, and H. Bevrani, “Modeling of voltage
source converters in microgrids using equivalent thevenin circuit,” in
2018 9th Annual Power Electronics, Drives Systems and Technologies
Conference (PEDSTC).
IEEE, 2018, pp. 510–515.
[32] I. Sowa, T. T. Tran, T. Heins, D. Raisz, and A. Monti, “An average
consensus algorithm for seamless synchronization of andronov-hopf
oscillator based multi-bus microgrids,” IEEE Access, vol. 9, pp. 90 441–
90 454, 2021.
[33] T. T. Tran, I. Sowa, D. Raisz, and A. Monti, “An average consensus-
based power-sharing among voc-based distributed generations in multi-
bus islanded microgrids,” IET Generation, Transmission & Distribution,
vol. 15, no. 4, pp. 792–807, 2021.
[34] M. S. Thomas and A. Nisar, “Data-driven modeling and simulation
of pv array,” in 2015 2nd International Conference on Computing for
Sustainable Global Development (INDIACom).
IEEE, 2015, pp. 308–
313.
[35] M. Tan and Z. Zhang, “Wind turbine modeling with data-driven methods
and radially uniform designs,” IEEE Transactions on Industrial Infor-
matics, vol. 12, no. 3, pp. 1261–1269, 2016.
[36] U. K. Das, K. S. Tey, M. Seyedmahmoudian, S. Mekhilef, M. Y. I.
Idris, W. Van Deventer, B. Horan, and A. Stojcevski, “Forecasting of
photovoltaic power generation and model optimization: A review,” pp.
912–928, jan 2018.
[37] Y. Wang and D. Infield, “Markov Chain Monte Carlo simulation
of electric vehicle use for network integration studies,” International
Journal of Electrical Power and Energy Systems, vol. 99, pp. 85–94, jul
2018.
[38] R. C. Leou, J. H. Teng, H. J. Lu, B. R. Lan, H. T. Chen, T. Y. Hsieh, and
C. L. Su, “Stochastic analysis of electric transportation charging impacts
on power quality of distribution systems,” IET Generation, Transmission
and Distribution, vol. 12, no. 11, pp. 2725–2734, jun 2018.
[39] R. C. Leou, C. L. Su, and C. N. Lu, “Stochastic analyses of electric
vehicle charging impacts on distribution network,” IEEE Transactions
on Power Systems, vol. 29, no. 3, pp. 1055–1063, 2014.
[40] E. Ghiani, A. Giordano, A. Nieddu, L. Rosetti, and F. Pilo, “Planning
of a smart local energy community: The case of berchidda municipality
(italy),” Energies, vol. 12, no. 24, p. 4629, 2019.
[41] B. Yan, M. Di Somma, G. Graditi, and P. B. Luh, “Markovian-based
stochastic operation optimization of multiple distributed energy systems
with renewables in a local energy community,” Electric Power Systems
Research, vol. 186, p. 106364, 2020.
[42] C. Orozco, S. Lilla, A. Borghetti, F. Napolitano, and F. Tossani, “An
admm approach for day-ahead scheduling of a local energy community,”
in 2019 IEEE Milan PowerTech.
IEEE, 2019, pp. 1–6.
[43] S. Sen and V. Kumar, “Microgrid modelling: A comprehensive survey,”
Annual Reviews in Control, vol. 46, pp. 216–250, 2018.
[44] S. M. Zali and J. Milanovic, “Dynamic equivalent model of distribution
network cell using prony analysis and nonlinear least square optimiza-
tion,” in 2009 IEEE Bucharest PowerTech.
IEEE, 2009, pp. 1–6.
[45] P. N. Papadopoulos, T. A. Papadopoulos, P. Crolla, A. J. Roscoe,
G. K. Papagiannis, and G. M. Burt, “Measurement-based analysis of
the dynamic performance of microgrids using system identification
techniques,” IET Generation, Transmission & Distribution, vol. 9, no. 1,
pp. 90–103, 2015.
[46] M. Q. Tran, A. S. Zamzam, P. H. Nguyen, and G. Pemen, “Multi-area
distribution system state estimation using decentralized physics-aware
neural networks,” Energies, vol. 14, no. 11, jun 2021.
[47] F. Ni, P. H. Nguyen, J. F. Cobben, H. E. Van den Brom, and D. Zhao,
“Three-phase state estimation in the medium-voltage network with
aggregated smart meter data,” International Journal of Electrical Power
and Energy Systems, vol. 98, pp. 463–473, jun 2018.
[48] D. S. Shafiullah, P. P. Vergara, A. N. Haque, P. H. Nguyen, and A. J.
Pemen, “Gaussian Mixture Based Uncertainty Modeling to Optimize
Energy Management of Heterogeneous Building Neighborhoods: A Case
Study of a Dutch University Medical Campus,” Energy and Buildings,
vol. 224, oct 2020.
[49] W. Li, M. Rentemeister, J. Badeda, D. J¨ost, D. Schulte, and D. U. Sauer,
“Digital twin for battery systems: Cloud battery management system
with online state-of-charge and state-of-health estimation,” Journal of
Energy Storage, vol. 30, aug 2020.
[50] S. Kaewunruen, P. Rungskunroch, and J. Welsh, “A digital-twin evalu-
ation of net zero energy building for existing buildings,” Sustainability,
vol. 11, no. 1, p. 159, 2019.
[51] Q. T. Tran, Y. Besanger, M. Jung, T. L. Nguyen et al., “Digital twin
integrated power-hardware-in-the-loop for the assessment of distributed
renewable energy resources,” Electrical Engineering, pp. 1–12, 2021.
[52] W. Li, M. Rentemeister, J. Badeda, D. J¨ost, D. Schulte, and D. U. Sauer,
“Digital twin for battery systems: Cloud battery management system
with online state-of-charge and state-of-health estimation,” Journal of
energy storage, vol. 30, p. 101557, 2020.
[53] H.-A. Park, G. Byeon, W. Son, H.-C. Jo, J. Kim, and S. Kim, “Digital
twin for operation of microgrid: Optimal scheduling in virtual space of
digital twin,” Energies, vol. 13, no. 20, p. 5504, 2020.
[54] M. You, Q. Wang, H. Sun, I. Castro, and J. Jiang, “Digital twins
based day-ahead integrated energy system scheduling under load and
renewable energy uncertainties,” Applied Energy, vol. 305, p. 117899,
2022.
[55] M. Uddin, M. F. Romlie, M. F. Abdullah, S. Abd Halim, T. C. Kwang
et al., “A review on peak load shaving strategies,” Renewable and
Sustainable Energy Reviews, vol. 82, pp. 3323–3332, 2018.
[56] H. Jiang, Y. Zhang, Y. Chen, C. Zhao, and J. Tan, “Power-traffic
coordinated operation for bi-peak shaving and bi-ramp smoothing–a
hierarchical data-driven approach,” Applied energy, vol. 229, pp. 756–
766, 2018.
[57] Y. Yang, H. Li, A. Aichhorn, J. Zheng, and M. Greenleaf, “Sizing
strategy of distributed battery storage system with high penetration
of photovoltaic for voltage regulation and peak load shaving,” IEEE
Transactions on smart grid, vol. 5, no. 2, pp. 982–991, 2013.
[58] M. Gottschalk, M. Uslar, and C. Delfs, “The smart grid architecture
model–sgam,” in The Use Case and Smart Grid Architecture Model
Approach.
Springer, 2017, pp. 41–61.
