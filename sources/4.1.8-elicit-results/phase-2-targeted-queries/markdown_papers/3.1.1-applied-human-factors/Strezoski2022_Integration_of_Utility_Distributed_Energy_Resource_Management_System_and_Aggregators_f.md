# Strezoski2022 Integration of Utility Distributed Energy Resource Management System and Aggregators for Evolving Distribution System Operators

## Paper Metadata

- **Filename:** Strezoski2022_Integration_of_Utility_Distributed_Energy_Resource_Management_System_and_Aggregators_for_Evolving_Distribution_System_Operators_DOI_10-35833_mpce-2021-000667.pdf
- **DOI:** 10.35833/mpce.2021.000667
- **Authors:** Not available
- **Year:** Not available
- **Journal/Venue:** Not available
- **URL:** Not available
- **Extraction Date:** 2025-06-03T15:04:09.645694
- **Total Pages:** 9

## Abstract

Abstract not available from BibTeX metadata.

## Keywords

Keywords not available from BibTeX metadata.

---

## Full Text Content



### Page 1

JOURNAL OF MODERN POWER SYSTEMS AND CLEAN ENERGY, VOL. 10, NO. 2, March 2022
Integration of Utility Distributed Energy Resource
Management System and Aggregators for
Evolving Distribution System Operators
Luka Strezoski, Member, IEEE, Harsha Padullaparti, Senior Member, IEEE, Fei Ding, Senior
Member, IEEE, and Murali Baggu, Senior Member, IEEE
Abstract—With the rapid integration of distributed energy re‐
sources (DERs), distribution utilities are faced with new and un‐
precedented issues. New challenges introduced by high penetra‐
tion of DERs range from poor observability to overload and re‐
verse power flow problems, under-/over-voltages, maloperation
of legacy protection systems, and requirements for new plan‐
ning procedures. Distribution utility personnel are not adequate‐
ly trained, and legacy control centers are not properly equipped
to cope with these issues. Fortunately, distribution energy re‐
source management systems (DERMSs) are emerging software
technologies aimed to provide distribution system operators
(DSOs) with a specialized set of tools to enable them to over‐
come the issues caused by DERs and to maximize the benefits
of the presence of high penetration of these novel resources.
However, as DERMS technology is still emerging, its definition
is vague and can refer to very different levels of software hier‐
archies, spanning from decentralized virtual power plants to
DER
aggregators
and
fully
centralized
enterprise
systems
(called utility DERMS). Although they are all frequently simply
called DERMS, these software technologies have different sets
of tools and aim to provide different services to different stake‐
holders. This paper explores how these different software tech‐
nologies can complement each other, and how they can provide
significant benefits to DSOs in enabling them to successfully
manage evolving distribution networks with high penetration of
DERs when they are integrated together into the control cen‐
ters of distribution utilities.
Index Terms—Distributed generation, distributed energy re‐
source (DER), aggregator, distributed energy resource manage‐
ment system (DERMS), non-wire alternatives.
I. INTRODUCTION
W
ITH the rapidly increasing penetration of distributed
energy resources (DERs) worldwide, distribution net‐
works are evolving towards complex and dynamically chang‐
ing systems [1]-[3]. The term DER itself relates to active re‐
sources connected to distribution networks and can include
distributed generators (DGs) such as solar photovoltaic (PV)
and wind generators, various types of energy storage sys‐
tems such as electric batteries or flywheels, as well as elec‐
tric vehicles (EVs) and their charging stations [4], [5]. Mas‐
sive integration of DERs is introducing a high level of com‐
plexity in traditionally passive distribution networks, includ‐
ing their observability, management, control, and protection
[6], [7].
Poorly planned and stochastic integration of DERs have
been introducing challenges that are felt all over the distribu‐
tion network. First, distribution network operators (DNOs)
are facing increasing amounts of overloads on their feeders,
over-/under-voltages at the DER buses, and protection coor‐
dination and sensitivity issues due to the dynamic and often
unpredictable behavior of DERs [7] - [11]. Second, end-cus‐
tomers, including behind-the-meter DERs, now having an
ability to produce more energy than they need, are becoming
eager to trade with their excess energy and enter the electric‐
ity markets, but are often too small and do not possess eco‐
nomic leverage to gain significant attention and benefits
from their services.
These changes are accompanied with the restructuring of
the traditional players in the electric power system area. Two
of the most important changes are as follows. First, the tradi‐
tional DNOs are required to rapidly evolve into much more
active
operators,
termed
distribution
system
operators
(DSOs), that would be able to manage, protect, and control
emerging distribution networks in near real time. Second, tra‐
ditionally passive loads are rapidly evolving into much more
dynamic “prosumers”, that can both consume and produce
electric power, and even trade with the excess energy. Final‐
ly, groups of prosumers and other behind-the-meter DERs
Manuscript received: September 29, 2021; revised: February 3, 2022; accept‐
ed: March 7, 2022. Date of Cross Check: March 7, 2022. Date of online publica‐
tion: March 30, 2022.
This work was supported by the U.S. Department of Energy under Contract
No. DE-AC36-08GO28308 with the Alliance for Sustainable Energy, LLC, the
U. S. DOE Office of Electricity, Advanced Grid Research Program, the U. S.
DOE Office of Energy Efficiency and Renewable Energy Solar Energy Technol‐
ogies Office. This work was also supported by the Faculty of Technical Scienc‐
es in Novi Sad, Department of Power, Electronics and Telecommunication Engi‐
neering, within the project entitled “Development and Application of Modern
Methods in Teaching and Research Activities at the Department of Power, Elec‐
tronics and Telecommunication Engineering”. The authors also thank Schneider
Electric DMS Company, for allowing authors to use ADMS and DERMS soft‐
ware for research purposes. The authors thank Annabelle Pratt and Santosh Veda
for their inputs.
This article is distributed under the terms of the Creative Commons Attribu‐
tion 4.0 International License (http://creativecommons.org/licenses/by/4.0/).
L. Strezoski (corresponding author) is with the Department for Power, Elec‐
tronics, and Telecommunications, Faculty of Technical Sciences, University of
Novi Sad, Novi Sad, Serbia, and he is also with Schneider Electric DMS Com‐
pany, Novi Sad, Serbia (e-mail: lukastrezoski@uns.ac.rs).
H. Padullaparti, F. Ding, and M. Baggu are with Energy System Integration,
National Renewable Energy Laboratory, Golden, USA (e-mail: Harsha Vardhana.
Padullaparti@nrel.gov; Fei.Ding@nrel.gov; murali.m.baggu@ieee.org).
DOI: 10.35833/MPCE.2021.000667
277

---


### Page 2

JOURNAL OF MODERN POWER SYSTEMS AND CLEAN ENERGY, VOL. 10, NO. 2, March 2022
are increasingly starting to aggregate into DER groups, virtu‐
al power plants (VPPs), and DER communities, and conse‐
quently offer their services at the aggregated level, where
they can present a considerable asset for balancing authori‐
ties and other market participants [7], [10]-[15].
Nonetheless, such a core transition of traditionally passive
distribution networks cannot be successfully performed with‐
out the accompanying modernization of control centers and
the development of highly intelligent software systems to en‐
able real-time observability, control, aggregation, and protec‐
tion of increasingly complex distribution networks with huge
numbers of DERs dispersed throughout the distribution net‐
work. Thus, emerging software solutions that are aimed to
enable proper management and control of distribution net‐
works with high penetration of DERs, called distributed ener‐
gy resource management systems (DERMSs), come into
play [7], [10], [11], [15].
Ideally, a DERMS solution should provide a wide range
of tools, which would benefit both DSOs and end-customers.
Nonetheless, because these technologies are still very novel,
the definition of a DERMS is vague and can often refer to
very different DER management solutions, spanning from
VPPs to demand response (DR) providers and DER aggrega‐
tors, and to centralized enterprise systems, called utility
DERMS or grid DERMS. Further, DERMS should be con‐
sidered as a logical entity rather than as a physical platform.
DERMS functionalities can reside in other enterprise plat‐
forms such as the advanced distribution management system
(ADMS). This paper uses the term utility DERMS for sim‐
plicity, but it might refer to having the functionality of con‐
trolling DER in the applications such as volt/var optimiza‐
tion (VVO) and peak load management in ADMS or DMS
solutions used by utilities in North America. The confusion
among the key stakeholders arises because even though all
these solutions and grouped functionalities are frequently
simply called DERMS, they have different sets of tools and
aim to provide different services to different stakeholders.
Two examples–both often called DERMS–are DER aggre‐
gators and utility DERMS. Although the aim of both might
seem similar–to manage and control DERs, these two solu‐
tions differ widely in their nature and responsibilities [11],
[15]. This poor understanding of the available technologies
and their functionalities often leads to distribution utilities
being reluctant in implementing DERMS, which consequent‐
ly defers DER integration, or even worse, leads to serious is‐
sues caused by high penetration of DERs, but without a
proper tool for controlling and managing such an evolving
environment.
Thus, the main motivation of this paper is to fill this gap
and clarify the confusion when using the term DERMS,
through clearly distinguishing between the structure and au‐
thority of different DER management software solutions and
explaining their different roles and responsibilities. Further,
it is our aim to present how the two solutions on the oppo‐
site ends of this spectrum, i.e., a DER aggregator and a utili‐
ty DERMS, can complement each other when deployed to‐
gether and offer a comprehensive set of tools for optimally
managing all DERs, from small-scale, behind-the-meter, to
large-scale DERs connected to the middle-voltage network.
Finally, we will present our vision how this integration en‐
ables both the DSOs and end-customers to overcome the
challenges imposed by high penetration of DERs, and fur‐
ther, how this can enable them to reap the highest possible
benefits from DERs and their services.
For DSOs, addition of DERMS to their control centers be‐
comes inevitable with the ever-increasing penetration of
DERs to properly observe, manage, control, and protect their
corresponding grids; while for the end-customers, it enables
them to properly offer their services to DSOs and balancing
parties, and help in dynamically managing the emerging
grids. To further validate our points and to showcase where
the power system community and industry currently stands
with DERMS, at the end of the paper, we present several re‐
al-life use cases from ongoing projects from Schneider Elec‐
tric and the National Renewable Energy Laboratory (NREL),
where the integration of various DER management software
solutions has already been tested in the real-life environment.
Thus, the contributions of this paper are as follows.
1) The logical concept of DERMS, including all levels of
hierarchy, is clearly introduced in this paper.
2) The inevitable need for the emerging distribution net‐
work control centers to implement DERMS is elaborated in
detail and the benefits of integrated centralized DER manage‐
ment solutions, i.e., utility DERMS, and decentralized ones,
i.e., DER aggregators, are comprehensively presented.
3) The proposed claims are validated on the most recent,
real-life projects, where these benefits have been already
proven.
Taken together, we hope that this effort will lead to better
understanding of DERMS concept within academia and in‐
dustry, and that it will contribute to faster implementation of
DERMS into distribution network control centers globally.
The rest of this paper is organized as follows. Section II
presents the challenges imposed by high penetration of
DERs to distribution networks. Section III introduces and
discusses the utility DERMS and DER aggregator concepts
and reveals the authors’ view of their complementary na‐
tures. Section IV presents several use cases from ongoing
projects that describes the progression of different DERMS
solutions all the way up to the integration of utility DERMS
and DER aggregators to provide optimal benefits to DSOs
and end-customers. Section V concludes the paper.
II. CHALLENGES IMPOSED BY HIGH PENETRATION OF DERS
TO DISTRIBUTION NETWORKS
DERs introduce several different categories of challenges
to the traditionally passive distribution networks. First, the
addition of high penetration of DERs into the existing distri‐
bution networks, if poorly planned, can infer instability, con‐
gestion, and other technical issues. Moreover, the addition of
DERs can require huge investments by the utilities to build
new or strengthen the existing distribution network assets.
Furthermore, DGs and energy storage technologies, when
managed improperly, can cause over-voltages on the existing
feeders, and can considerably increase the voltages at their
points of interconnection (POIs) as well as at the neighbor‐
ing locations. Moreover, because of the intermittent nature
278

---


### Page 3

STREZOSKI et al.: INTEGRATION OF UTILITY DISTRIBUTED ENERGY RESOURCE MANAGEMENT SYSTEM AND AGGREGATORS FOR EVOLVING...
of the renewable DERs, in periods of low demand but high
production of these resources (e.g., high solar irradiation or
wind power), a new phenomenon of reverse power flow can
occur. Consequently, this issue could inaccurately trigger the
reaction of protective devices, as well as cause voltage prob‐
lems and unpredicted variations along the feeders [11], [15].
Finally, it is very hard to accurately predict the behavior of
renewable DGs using the traditional forecasting methods;
thus, if left unmanaged in real time, this added uncertainty
could cause issues in the operation planning and manage‐
ment of emerging distribution networks.
On the other hand, at the low-voltage side, where most of
the end-customers are located, ever-increasing penetration of
rooftop PVs, energy storages for households, as well as the
massive integration of EVs are significantly transforming the
state of traditionally passive, low-voltage parts of distribu‐
tion networks, and driving the need for systematic and intel‐
ligent management.
Thus, distribution utilities and especially operators and
grid engineers, must adapt to the emerging conditions by
learning and adopting new technologies for planning and
managing evolving distribution networks with high penetra‐
tion of DERs. Traditional practices and procedures that are
used for managing passive distribution networks, are already
outdated and inapplicable to these emerging conditions. How‐
ever, DERMS can successfully cope with DER-imposed chal‐
lenges and secure the systematic and intelligent management
of a wide range of different DERs. Further, DERMS technol‐
ogies strive to turn the potentially dangerous behavior of
DERs into operational and monetary benefits for utilities, as
well as end-customers [15]-[18]. But there are different lev‐
els to the DERMS hierarchy, which aim to provide different
services regarding DER management, while targeting differ‐
ent DERs relative to their sizes and connection point loca‐
tions (on a medium- or low-voltage distribution network).
Our goal is to show how the integration of two of these
solutions, located on the opposite ends of the hierarchical
spectrum, namely utility DERMS and DER aggregators, can
work in coherence. By complementing each other, they can
provide a required set of tools for the integration and active
management of all types of DERs, regardless of their tech‐
nology, size, or connection point location.
III. DIFFERENT DER MANAGEMENT SOLUTIONS AND THEIR
COMPLEMENTARY NATURES
This section introduces a DERMS concept and presents
the nature and characteristics of utility DERMS and DER ag‐
gregators and the benefits of their integration to DSOs.
A. DERMS and Its Usage
As the DERMS concept is novel and still emerging, the
term DERMS itself is still vague and may refer to different
solutions. Generally speaking, the term DERMS corresponds
to a software solution for managing high penetration of
DERs. However, because of its novelty, DERMS is often
used to describe various different levels of software solu‐
tions aimed for managing DERs.
On the one hand, there are decentralized software packag‐
es that aim to aggregate behind-the-meter DERs such as airconditioning or heating devices, rooftop PVs, small-scale bat‐
teries, or EVs, with the main goal to provide a better aware‐
ness of these small-scale but very dispersed assets and to
provide their services in an aggregated and much more use‐
ful manner, e.g., by entering the electricity market or by pro‐
viding DR and energy-efficiency programs, among others
[15]-[19]. On the other hand, there are fully centralized en‐
terprise systems that aim to provide services to the DSOs, to
enable them to swiftly overcome the challenges that DERs
impose on the distribution networks and their assets. These
services range from providing situational awareness to manu‐
al/automatic DER control, constraint resolution, and ad‐
vanced optimization applications for the efficient manage‐
ment of medium- to large-scale DERs and DER groups con‐
sisting of numerous small-scale units, with the objectives to
provide operational and monetary benefits to the grid opera‐
tors and engineers in the control room and to grid planners
that are responsible for the network upgrades and the addi‐
tion of new resources [11], [15].
Both utility DERMS and DER aggregators are frequently
called DERMS, but these two solutions differ widely in their
nature and responsibilities considering the existing realworld solutions applied in North America and worldwide.
One is a centralized enterprise system, which is completely
grid-aware, whereas the other is usually implemented as a
decentralized solution that is unaware or partially aware of
the grid conditions and limitations and is concerned only
with DERs and their internal conditions and responsibilities.
But these two solutions also complement each other in se‐
curing a full spectrum of services essential for today’s
DSOs, who are responsible for ensuring the safe, reliable,
and optimal management of an ever-increasing penetration
of DERs [15].
B. Roles and Responsibilities of DER Management Solutions
The main role of DER aggregators is to provide the aggre‐
gation of small-scale DERs into DER groups, and conse‐
quently to enable their services using the aggregated DER
power. The added value provided by DER aggregators in‐
cludes enabling the participation of small-scale DERs in the
electricity markets, the engagement of DERs and prosumers
in energy-saving and energy-efficiency programs, the provi‐
sion of DR and load shedding services, as well as other
mostly customer-related services. However, because of their
structure that is generally adopted nowadays, DER aggrega‐
tors are either not aware or only partially aware of the grid
model and its conditions and technical boundaries, so they
cannot guarantee not causing technical constraint violations
such as congestions, voltage violations, or protection issues.
Thus, to enable the safe use of the services offered by DER
aggregators, DSOs must have observability of the real-time
conditions in the grid, as well as the ability to validate–and
modify, if necessary–the schedules of DER aggregators to
avoid constraint violations on the grid assets.
This is where a utility DERMS comes into play. Utility
DERMS solutions are intelligent, grid-aware software pack‐
ages that enable the full awareness, control, and optimal
management of medium- to large-scale DERs and DER
groups (consisting of behind-the-meter DERs), with the goal
279

---


### Page 4

JOURNAL OF MODERN POWER SYSTEMS AND CLEAN ENERGY, VOL. 10, NO. 2, March 2022
of using all these resources to achieve system-wide benefits
without violating grid constraints. Further, utility DERMS so‐
lutions use all available resources to solve existing violations
or predicted constraint violations and keep the system in a
stable and optimal state in real time. Therefore, for largeand medium-scale DERs, whose impact on the grid condi‐
tions can be significant, a grid-aware utility DERMS is a nat‐
ural solution for their management and control [11], [15].
Even though both solutions are concerned with DER man‐
agement, utility DERMS and DER aggregators are vastly dif‐
ferent software packages, and thus they should not be re‐
ferred to by the same term. Referring to both solutions as
DERMS leads to confusion, even among parties interested in
deploying DERMS (i.e., electric utilities), and thus it should
be abandoned. From the standpoint of DSO, utility DERMS
and DER aggregators should be understood as different lev‐
els in a hierarchy: DER aggregators mainly communicate
with behind-the-meter units and use them in an aggregated
fashion to provide various services regarding customer en‐
gagement and operations. Besides, utility DERMS uses DER
aggregators, among other resources such as individual medi‐
um- to large-scale DERs, various types of DER groups,
VPPs, microgrids, and traditional resources such as switches
and capacitors, to provide DSOs with a complete awareness
as well as effortless, real-time, look-ahead constraint manage‐
ment and the optimal coordination and management of
DERs,
DER
groups,
and
other
system-wide
operations.
Therefore, if properly integrated, a DER aggregator and utili‐
ty DERMS can complement each other and provide a full
spectrum of DER services regarding both customer-related
and grid-related operations, which is regardless of the sizes
and locations of DERs.
C. Integration of Utility DERMS and DER Aggregators: an
Ideal Case
Even though both a DER aggregator and a utility DERMS
can be used as a stand-alone solution and can successfully
provide numerous benefits, their values are tremendously in‐
creased when they are integrated and used together. When
they are properly integrated and set to work coherently,
these two solutions can cover a full spectrum of DER man‐
agement services and can open a new world of possibilities
for DSOs to use DERs as valuable resources in performing a
broad set of required operations, both grid-related and cus‐
tomer-related [15], [19].
Through (near) real-time communications and data ex‐
change with a utility DERMS, DER aggregators highly en‐
hance DSOs’ awareness of and ability to manage behind-themeter DERs, especially in customer-related operations such
as participation in electricity market and DR or energy-effi‐
ciency schemes. Nonetheless, through its advanced applica‐
tions such as hosting capacity, real-time and look-ahead con‐
straint management, volt/var/watt optimization, demand flexi‐
bility, load and DER forecast, and through sophisticated inte‐
gration with DER aggregators, utility DERMS enables DSOs
with an ability to successfully manage and optimize their
emerging distribution systems with high penetration of differ‐
ent DERs, which are dispersed throughout the grid (from be‐
hind-the-meter to large-scale DERs connected to the medi‐
um-voltage distribution network) [19].
Further, DER aggregators, if integrated with a utility
DERMS, would be able to provide a much better quality of
their services because all their scheduled programs could be
validated by a utility DERMS, therefore ensuring that none
of the technical constraints are ever violated. Hence, this in‐
tegration would ultimately lead DSOs to a much-needed
transformation into a new era of future distribution systems
with high penetration of DERs.
Near real-time communication in this context is envi‐
sioned through supervisory control and data acquisition
(SCADA) and internet protocols, but can also be performed
through
custom-made
application
programing
interfaces
(APIs). Using custom-made APIs is a current practice, as in
many cases, a utility DERMS of the specific vendor on one
side, and a DER aggregator on the other side, do not support
the
same
protocols.
Hopefully,
this
practice
will
soon
change, as the standardization of the communication proto‐
cols is currently taking place, and for example, the IEEE
2030.5 protocol is a very promising solution that could be
useful on both ends.
The information exchanged through this communication
often consists of advanced metering infrastructure (AMI)
measurements that an aggregator collects for behind-the-me‐
ter resources, as well as forecasted production of small-scale
DERs controlled by DER aggregators and their operation
schedules. These data are then used in near real-time applica‐
tions of the utility DERMS, i.e., state estimation, to improve
situation awareness, as well as in constraint management
and grid optimization for near real-time and forecasted peri‐
ods. Thus, not only the observability of the grid conditions
in near real-time is significantly improved, but also the pre‐
dictions of the constraint violations can be performed with
more accuracy and consequently they can be managed proac‐
tively.
IV. REAL-LIFE USE CASES FOR UTILITY DERMS AND DER
AGGREGATORS
This section presents several real-life use cases that dem‐
onstrate the progression of different DERMS solutions all
the way up to the integration of utility DERMS and DER ag‐
gregators to provide benefits to DSOs and end-customers.
The following examples have already been tested or are cur‐
rently being tested in industrial and academic projects, using
commercially available or prototype utility DERMS and
DER aggregator solutions.
A. Distribution Voltage Management and Peak Load Reduc‐
tion Through Utility DERMS
This use case demonstrates a utility DERMS that directly
controls residential DERs that are owned by the utility.
These DERs are aggregated and controlled as a VPP to pro‐
vide peak demand reduction while enforcing the voltage reg‐
ulation. This utility DERMS is a software prototype devel‐
oped by NREL [20] (originally referred as real-time optimal
power flow) by using a feedback-based real-time optimiza‐
tion algorithm [21], [22].
A distribution feeder, located in Colorado within the ser‐
vice territory of an electric utility in North America, is used
280

---


### Page 5

STREZOSKI et al.: INTEGRATION OF UTILITY DISTRIBUTED ENERGY RESOURCE MANAGEMENT SYSTEM AND AGGREGATORS FOR EVOLVING...
as the simulation test system in this study. There are 1137
residential loads modeled, of which 163 loads represent allelectric homes. These all-electric homes are assumed to have
residential rooftop PV and battery energy storage system
(BESS) installed on their premises that participate in the
VPP and voltage regulation controls through the utility
DERMS. The experiments are conducted in the ADMS test‐
bed [14], [23], [24]. The testbed was developed by NREL
and the U. S. Department of Energy’s (DOE’s) Office of
Electricity for vendor-neutral evaluation of distribution man‐
agement strategies and through that, to help accelerate AD‐
MS deployments among DSOs. The testbed uses multi-times‐
cale simulation platforms of distribution system models, in‐
terfaced with physical hardware to represent real-world and
hypothetical future system conditions. The testbed also has a
communication interface that allows ADMS and other utility
management systems such as DERMS to interface with the
testbed using industry-standard protocols. NREL works with
utility, industry, and other research groups, to identify and
evaluate ADMS applications that are important for grid mod‐
ernization. The simulations for this use case are conducted
on the ADMS testbed using the data from a representative
peak load day on January 27, 2018.
Figure 1 shows the results from utility DERMS use case,
including substation power, total BESS power output, and
average BESS state of charge (SOC).
High load consumptions are observed during 07:00-08:00
and 17:00-23:00 for the baseline (no control) scenario. With
BESSs controlled by the utility DERMS, they discharge pow‐
er to offset the high load consumptions during these periods
and recoup the energy by charging in other periods. Voltage
regulation is implemented simultaneously by controlling the
reactive power output of PV inverters.
Figure 2 shows the results of the system voltages and the
active and reactive power outputs of PV inverters when PVs
are controlled by the utility DERMS.
Reactive power support provided by PV inverters is used
to mitigate over-voltage without causing PV curtailment.
The negative PV reactive power indicates reactive power ab‐
0.95
0.90
1.00
1.05
1.10
Voltage (p.u.)
0.95
0.90
1.00
1.05
1.10
Voltage (p.u.)
Maximum;
Minimum
Median;
70th percentile
Maximum;
Minimum
Median;
70th percentile
00:00 03:00 06:00 09:00 12:00 15:00 18:00 21:00 24:00
Time
(a)
00:00 03:00 06:00 09:00 12:00 15:00 18:00 21:00 24:00
Time
(b)
4
0
8
12
2
6
10
Active power output
(k W)
00:00 03:00 06:00 09:00 12:00 15:00 18:00 21:00 24:00
Time
(c)
-5
-10
5
0
10
Reactive power output
(kvar)
00:00 03:00 06:00 09:00 12:00 15:00 18:00 21:00 24:00
Time
(d)
Fig. 2.
Results of system voltages and active and reactive power outputs
of PV inverters. (a) System voltages for no control scenario. (b) System
voltages when PVs are controlled by utility DERMS. (c) Active power out‐
puts of PV inverters. (d) Reactive power outputs of PV inverters.
-2
-4
0
2
4
6
10
12
14
8
Power output (MW)
No control
PV and BESS are controlled by utility DERMS
00:00 03:00 06:00 09:00 12:00 15:00 18:00 21:00 24:00
Time
(a)
-3
-2
-1
-4
0
1
2
3
Power output (MW)
00:00 03:00 06:00 09:00 12:00 15:00 18:00 21:00 24:00
Time
(b)
40
20
60
80
Average BESS SOC (%)
00:00 03:00 06:00 09:00 12:00 15:00 18:00 21:00 24:00
Time
(c)
Fig. 1.
Results from utility DERMS use case. (a) Substation power output.
(b) Total BESS power output when BESSs are controlled by utility DERMS.
(c) Average BESS SOC when BESSs are controlled by utility DERMS.
281

---


### Page 6

JOURNAL OF MODERN POWER SYSTEMS AND CLEAN ENERGY, VOL. 10, NO. 2, March 2022
sorption.
B. Improved Monitoring and Control in Emerging Distribu‐
tion Networks with Large Amounts of Dispersed DERs
Utility DERMS provides accurate situation awareness of
real-time conditions in the grid to the operator, including
voltages, current and power flows, and congestions, through
SCADA and AMI systems [13]. Moreover, through sophisti‐
cated load and DER forecast algorithms, accurate predictions
of future grid conditions are estimated by utility DERMS
systems; however, with the emergence of high penetration of
behind-the-meter DERs and flexible loads, which are fre‐
quently not connected to SCADA or AMI systems, their con‐
ditions have traditionally been estimated using state estima‐
tion or other advanced applications [13], [15]. Besides, DER
aggregators enable near real-time measurements of smallscale DERs that are not connected to SCADA or AMI as
well as accurate forecasted behavior of DER groups compris‐
ing these small DERs. With these data being constantly im‐
ported from DER aggregators, a utility DERMS increases
the accuracy of the real-time situational awareness and ex‐
pands it to the grid-edge devices [13], [15].
This use case describes a study of the ability of DER ag‐
gregator and ADMS (with utility DERMS functionalities) co‐
ordination to achieve situation awareness and voltage regula‐
tion in the presence of very high penetration of DERs, using
the NREL ADMS testbed [14], [24], [25].
When high PV generation is present, the voltage regula‐
tion is a major issue. This use case also demonstrates the
ability of the real-time optimal power flow [20] introduced
in Section IV-A to coordinate with an ADMS to enforce the
voltage regulation in the distribution feeders. Specifically,
the ADMS reduces the bus voltages to mitigate the voltage
rise and the DER aggregator dispatches the PV smart invert‐
ers to further resolve the voltage issues.
This study models a set of four distribution feeders sup‐
plied by a 30 MVA, 110 k V/13.2 k V substation transformer
in Open DSS. The model is developed based on the data
from a North American electric utility. The topology of this
model is shown in Fig. 3. The feeders, located in Colorado,
serve nearly 6000 customers and have more than 13000 bus‐
es. The substation transformer is equipped with a load tap
changer (LTC). Additionally, there are 13 switched capacitor
banks with a total rating of 15.6 Mvar available for voltage
regulation and reactive power management. More than 3000
distributed PV systems are added to the model with a total
rating of 24 MW (about 200% relative to the minimum
load) to simulate a scenario with high PV penetration.
The experiments for two scenarios are carried out, as de‐
scribed in [25], for 4 hours of simulation time to study the
coordinated operation of the ADMS and DER aggregator in
accomplishing the voltage regulation. In the first scenario, re‐
ferred to as the baseline, the controls of the ADMS and
DER aggregator are turned off. The legacy devices (LTC
and capacitor banks) follow their local controller responses
and the PV smart inverters inject power at unity power fac‐
tor. The bus voltages from this scenario are shown in Fig. 4(a).
It is evident that many buses experience over-voltage issues,
i.e., voltages above the upper voltage limit of American Na‐
tional Standards Institute (ANSI) (1.05 p.u.) during the simu‐
lated period.
In the second scenario, referred to as the virtual reality
(VR)-enabled scenario, the VVO of ADMS is enabled with
the voltage regulation (customer voltage improvement) as
the control objective. This study uses the ADMS developed
by Schneider Electric [26]. The ADMS runs advanced modelbased optimization using the VVO application to issue opti‐
mal set-points to the legacy devices, i.e., the LTC and capac‐
itor banks. Since the scenario with high PV penetration in
this use case considers residential rooftop PV systems only,
they (PVs) are all assumed to be controlled by the DER ag‐
gregator and not by the ADMS. The VVO of ADMS is config‐
ured to run every 5 min to issue the set-points to the legacy de‐
vices on the slow timescale. Further, the real-time optimal
power flow algorithm [27] is used to implement the DER ag‐
gregator. The DER aggregator commands are configured to
run every 5 s to enforce the bus voltages to be within the limits
using the reactive power compensation from the small-scale
PV smart inverters and the active power curtailment, if needed.
The results from the second scenario are shown in Fig. 4(b)-
(e). As observed in Fig. 4(b), the ADMS reduces the LTC
voltage regulation set-point to 119 V from the default LTC
local controller set-point of 124 V during the initial few min‐
utes of the simulation. As a result, the LTC tap position is
lowered to -5. Consequently, the bus voltages are reduced and
reasonably confined to the ANSI voltage band from 0.95 p.u.
to 1.05 p.u, as shown in Fig. 4(d). Thus, the voltage regulation
is ensured despite the presence of high PV generation. The to‐
tal PV power outputs in both the scenarios are compared in
Fig. 4(e). As the PV inverters are not oversized, the DER ag‐
gregator curtails the PV active power to allow reactive power
absorption to regulate the voltage within operating limits. It is
observed that approximately 9 kvar reactive power is absorbed
by the PV smart inverters at around 10:00.
C. Utilizing DERs to Mitigate Real-time Constraint Viola‐
tions After Restoration of a De-energized Island
Another related use case currently being tested by using
the utility DERMS of Schneider Electric investigates how to
optimally use DERs to mitigate constraint violations after
the restoration of a de-energized island [15].
Feeder 1
Feeder 3
Feeder 2
Feeder 4
Substation
Switched capacitor
Primary network
Secondary network
Fig. 3.
Topology of studied model.
282

---


### Page 7

STREZOSKI et al.: INTEGRATION OF UTILITY DISTRIBUTED ENERGY RESOURCE MANAGEMENT SYSTEM AND AGGREGATORS FOR EVOLVING...
In a simulated environment, during the restoration of a deenergized island after a fault isolation, an overload is detect‐
ed at the beginning of the feeder, and an overload alarm ap‐
pears in the utility DERMS. It triggers a real-time constraint
management application; and the application, among its re‐
sources for constraint resolution, detects a DER group man‐
aged by a DER aggregator consisting of batteries and solar
PVs. The application computes the result that this DER
group can provide enough flexibility to mitigate the overload
condition. The command is consequently sent to the DER ag‐
gregator to increase the production of the resources in one
of the DER groups managed by it. Finally, the DER aggrega‐
tor dispatches the commands among its individual DER as‐
sets to increase production and alleviate congestion. Through
the real-time measurements, the utility DERMS confirms
that the overload issue is successfully mitigated, and the
alarm disappears, informing the operator that the violation is
successfully solved.
D. Participation of DERs in Electricity Markets Without Vio‐
lating Technical Constraints
In accordance with their integration with a day-ahead elec‐
tricity market, DER aggregators determine schedules for
their DER groups. We propose that, to validate these sched‐
ules against technical constraints, DER aggregators send
these schedules to the utility DERMS. These schedules are
considered within the look-ahead constraint management ap‐
plication of DERMS, which determines if some of the sched‐
ules would violate the technical constraints. Therefore, for
these DER groups, modified schedules as well as the maxi‐
mum export and import limits are calculated within the
DERMS and sent back to the DER aggregators, along with
the positive validations for the rest of the schedules that do
not violate any constraint. The DER aggregators accordingly
modify the schedules for critical DER groups, and it is final‐
ly ensured that all the new schedules are valid and safe to
be implemented when the time comes. The integration of the
utility DERMS and DER aggregators is essential to effective‐
ly aggregate DERs to provide bulk grid services [28].
A variation of this approach is a new grid control architec‐
ture, referred to as the federated architecture for secure and
transactive distributed energy resource management solutions
(FAST-DERMS) [29], which is shown in Fig. 5. It is current‐
ly under development and proposes a distribution utility
DERMS, which consists of flexible resource schedulers
(FRSs) and an FRS coordinator. Each FRS schedules DERs
within a substation service area. The FRS can control some
DERs, which may include a building (B) or microgrid (MG)
directly and others through a DER aggregator. Yet others may
be managed through a transactive market manager (TMM).
The FAST-DERMS project focuses on enabling scalable
aggregation and near real-time management of utility-scale
and small-scale DERs through grid-aware, reliability-con‐
strained economic dispatch by the FRS. It aims to support re‐
liable, resilient, and secure distribution and transmission net‐
work services. Further, the advancements on multiple fronts,
including communication standards, controls that effectively
handle load and DER uncertainties, transactive market struc‐
tures that ensure the protection of customer autonomy, DER
anomaly detection methods, and fail-safe DER operating
Fig. 4.
Results from voltage regulation use case. (a) Bus voltages in base‐
line scenario. (b) LTC voltage regulation set-points. (c) LTC tap positions.
(d) Bus voltages in VR-enabled scenario. (e) Total PV power outputs.
283

---


### Page 8

JOURNAL OF MODERN POWER SYSTEMS AND CLEAN ENERGY, VOL. 10, NO. 2, March 2022
modes, are being developed for the successful provision of
transmission services by distribution-connected DERs. These
controls will be demonstrated at NREL using the ADMS test‐
bed.
E. Discussion of Presented Use Cases
The presented use cases showcase the importance of DER
management solutions to the emerging DSOs. First, the criti‐
cally important awareness of the near real-time state of the
highly dynamic conditions in emerging distribution networks
is provided using DERMS and maximized by the integration
of a utility DERMS and DER aggregators. Second, utility
DERMS and DER aggregators provide DSOs with an ability
to assist TSOs in their balancing needs and other important
services, e.g., peak reduction, by intelligently using the flexi‐
bility of the available DERs and optimizing their output per
the requests for aggregated power received from TSOs. Fi‐
nally, to enable DERs to participate in the electricity mar‐
kets, distribution utilities need to be sure that the technical
constraints would not be violated by the (aggregated) DER
schedules. As presented, this is also enabled through the inte‐
gration of utility DERMS and DER aggregators, where the
utility DERMS validates the schedules of DER groups
against the technical limitations of distribution networks.
The aim of this paper with presenting these use cases has
been to showcase the current state of the art in the develop‐
ment of DERMS industry. These are some of the latest ex‐
amples from the real-life industrial use cases, and thus
where the power system community and industry are current‐
ly standing with DERMS development is shown, especially
with the integration of utility DERMS and DER aggregators.
As presented, a lot has already been done, but to reach an
ideal case that would provide effortless integration and man‐
agement of the emerging distribution systems with high pen‐
etration of DERs, a much better understanding of different
levels of DERMS solutions is needed, to use their full poten‐
tial. We hope that this paper will contribute to this area and
that it will help in better understanding how different hierar‐
chical levels of DERMS solutions can work in coherence and
contribute to an effortless DNO to DSO transformation and ap‐
plication in the emerging distribution network control centers.
V. CONCLUSION
With an ever-increasing penetration of DERs, driven by
crucially important carbon reduction initiatives around the
globe, traditionally passive distribution networks are rapidly
evolving towards highly complex and dynamically changing
systems. Such complex systems cannot be managed, con‐
trolled, or protected using legacy software solutions de‐
signed for traditional control centers; thus, control centers,
along with the personnel of electric utilities, must evolve ac‐
cordingly.
To enable such an evolvement, DERMS software solu‐
tions are emerging. DERMS software solutions are software
packages aiming to provide DSOs, end-customers, and other
stakeholders, with a set of tools that will enable them to
cope with the challenges imposed by DERs. But the term
DERMS is very broad and includes vastly different DER
management solutions, aimed for different stakeholders and
with different goals. On the one hand, mainly customer- and
single-DER-related solutions, are decentralized software solu‐
tions called DER aggregators. On the other end, the fully
grid-aware and centralized solutions, are so-called utility
DERMS solutions.
In this paper, we explore the roles and responsibilities of
these different DER management solutions and offer the
view on how the optimal integration of a utility DERMS
and DER aggregators leads to an ideal case for the future
DSO, enabling a smooth shift towards emerging distribution
networks with high penetration of DERs.
REFERENCES
[1] A. Sajadi, L. Strezoski, V. Strezoski et al., “Integration of renewable
energy systems and challenges for dynamics, control, and automation
of electrical power systems,” WIREs Energy and Environment, vol. 8,
no. 4, pp. 1-12, Aug. 2018.
[2] J. R. Aguero, E. Takayesu, D. Novosel et al., “Modernizing the grid:
challenges and opportunities for a sustainable future,” IEEE Power
and Energy Magazine, vol. 15, no. 3, pp. 74-83, May 2017.
[3] R. Das, V. Madani, F. Aminifar et al., “Distribution automation strate‐
gies: evolution of technologies and the business case,” IEEE Transac‐
tions on Smart Grid, vol. 6, no. 4, pp. 2166-2175, Jul. 2015
[4] J. M. Guerrero, F. Blaabjerg, T. Zhelev et al., “Distributed generation:
toward a new energy paradigm,” IEEE Industrial Electronics Maga‐
zine, vol. 4, no. 1, pp. 52-64, Mar. 2010.
[5] V. Smil, “Distributed generation and megacities: are renewables the an‐
swer?” IEEE Power and Energy Magazine, vol. 17, no. 2, pp. 37-41,
DSO
TSO
FRS coordinator
Distribution utility DERMS
FRS
Aggergator
TMM
DER
B/MG
DER
B/MG
DER
B/MG
FRS
Aggergator
TMM
DER
B/MG
DER
B/MG
DER
B/MG
Substation service area
Substation service area
…
Fig. 5.
Schematic of FAST-DERMS.
284

---


### Page 9

STREZOSKI et al.: INTEGRATION OF UTILITY DISTRIBUTED ENERGY RESOURCE MANAGEMENT SYSTEM AND AGGREGATORS FOR EVOLVING...
Mar. 2019.
[6] C. J. Mozina, “Impact of green power distributed generation,” IEEE
Industry Applications Magazine, vol. 16, no. 4, pp. 55-62, Jul. 2010.
[7] L. Strezoski, I. Stefani, and B. Brbaklic, “Active management of distri‐
bution systems with high penetration of distributed energy resources,”
in Proceedings of 18th International Conference on Smart Technolo‐
gies, Novi Sad, Serbia, Jul. 2019, pp. 1-5.
[8] J. Driesen and R. Belmans, “Distributed generation: challenges and
possible solutions,” in Proceedings of IEEE PES General Meeting,
Montreal, Canada, Jun. 2006, pp. 1-8.
[9] L. Strezoski, N. Vojnovic, V. Strezoski et al., “Modeling challenges
and potential solutions for integration of emerging DERs in DMS ap‐
plications: power flow and short-circuit analysis,” Journal of Modern
Power Systems and Clean Energy, vol. 7, no. 1, pp. 1365-1384, Jan.
2019.
[10] M. D. Ilic, R. Jaddivada, and M. Korpas, “Interactive protocols for dis‐
tributed energy resource management systems (DERMS),” IET Gener‐
ation, Transmission & Distribution, vol. 14, no. 11, pp. 2065-2081,
Feb. 2020.
[11] J. Wang, H. Padullaparti, F. Ding et al., “Voltage regulation perfor‐
mance evaluation of distributed energy resource management via ad‐
vanced hardware-in-the-loop simulation,” Energies, vol. 14, no. 20,
pp. 1-24, Oct. 2021.
[12] IEEE Draft Guide for Distributed Energy Resources Management Sys‐
tems (DERMS) Functional Specification, IEEE Standard P2030.11/
D11.1, 2021.
[13] N. Sadan and B. Renz, “New DER communications platform enables
derms and conforms with IEEE 1547–2018 requirements,” in Proceed‐
ings of IEEE/PES Transmission and Distribution Conference and Ex‐
position (T&D), Chicago, USA, Oct. 2020, pp. 1-5.
[14] A. Pratt, M. Baggu, S. Veda et al., “Testbed to evaluate advanced dis‐
tribution management systems for modern power systems,” in Proceed‐
ings of 18th International Conference on Smart Technologies, Novi
Sad, Serbia, Jul. 2019, pp. 5-10.
[15] L. Strezoski and I. Stefani, “Utility DERMS for active management of
emerging distribution grids with high penetration of renewable DERs,”
Electronics, vol. 10, no. 16, Aug. 2021, pp. 1-16.
[16] L. Rozentale, A. Kalnbalkite, and D. Blumberga, “Aggregator as a
new electricity market player (case study of Latvia),” in Proceedings
of IEEE 61th International Scientific Conference on Power and Elec‐
trical Engineering of Riga Technical University (RTUCON), Riga, Lat‐
via, Jul. 2020, pp. 1-6.
[17] P. Faria, J. Spínola, and Z. Vale, “Distributed energy resources sched‐
uling and aggregation in the context of demand response programs,”
Energies, vol. 11, no. 8, pp. 1-17, Jul. 2018.
[18] H. M. Rouzbahani, H. Karimipour, and L. Lei, “A review on virtual
power plant for energy management, sustainable energy technologies
and assessments,” Sustainable Energy Technologies and Assessments,
vol. 47, pp. 2213-1388, Oct. 2021.
[19] L. Strezoski, “Integration of a utility DERMS and DER aggregators:
an ideal case for tomorrow’s DSO”, submitted to IEEE ISGT Europe
2022, Novi Sad, Serbia, Oct. 2022.
[20] F. Ding, Distributed Energy Resource Management Solution Using Re‐
al-time Optimization. Golden: NREL Software Record, 2019.
[21] E. Dall’Anese, S. S. Guggilam, A. Simonetto et al., “Optimal regula‐
tion of virtual power plants,” IEEE Transactions on Power Systems,
vol. 33, no. 2, pp. 1868-1881, Mar. 2018.
[22] E. Dall’Anese and A. Simonetto, “Optimal power flow pursuit,” IEEE
Transactions on Smart Grid, vol. 9, no. 2, pp. 942-952, Mar. 2018.
[23] NREL. (2021, Sept.). Advanced distribution management systems. [On‐
line]. Available: https://www. nrel. gov/grid/advanced-distribution-man‐
agement.html
[24] H. Padullaparti, A. Pratt, I. Mendoza et al., “Peak load management in
distribution systems using legacy utility equipment and distributed en‐
ergy resources,” in Proceedings of IEEE Green Technologies Confer‐
ence, Denver, USA, Apr. 2021, pp. 435-441.
[25] J. Wang, H. Padullaparti, S. Veda et al., “Performance evaluation of
data-enhanced hierarchical control for grid operations,” in Proceedings
of IEEE PES General Meeting, Montreal, Canada, Aug. 2020, pp. 1-5.
[26] Schneider Electric. (2021, Aug.). Advanced distribution management
system. [Online]. Available: https://www. se. com/us/en/work/solutions/
for-business/electric-utilities/advanced-distribution-management-systemadms/
[27] F. Ding, H. Padullaparti, M. Baggu et al., “Data-enhanced hierarchical
control to improve distribution voltage with extremely high PV pene‐
tration,” in Proceedings of IEEE PES General Meeting, Atlanta, USA,
Jul. 2019, pp. 1-5.
[28] Australian Renewable Energy Agency. (2020, May). On the calcula‐
tion and use of dynamic operating envelopes. [Online]. Available:
https://arena. gov. au/knowledge-bank/on-thecalculation-and-use-of-dy‐
namic-operating-envelopes/
[29] U. S. Department of Energy. (2021, Aug.). Federated architecture for
secure and transactive distributed energy resource management solu‐
tions (FAST-DERMS). [Online]. Available: https://gmlc. doe. gov/proj‐
ects/2.1.1
Luka Strezoski received the B.S., M.Sc., and Ph.D. degrees in power engi‐
neering from the University of Novi Sad, Novi Sad, Serbia, in 2013, 2014,
and 2017, respectively. His Ph.D. research was conducted in a joint supervi‐
sion between University of Novi Sad and Case Western Reserve University,
Cleveland, USA. He is with the Faculty of Technical Sciences, University
of Novi Sad since 2013, and currently serves as an Assistant Professor,
Head of the Power Engineering and Applied Software Department and Di‐
rector of the Smart Grid Laboratory. He is also with Schneider Electric, No‐
vi Sad, Serbia, as a Principal Consultant to Solutions Engineering (DMS
and DERMS) and a Member of the Technology Board. He is also with Case
Western Reserve University as an Academic Affiliate. His research interests
include distribution system modeling and protection, renewable generation
modeling, integration and active management of high penetration of renew‐
able distributed energy resources, and power applications of distribution
management system and distributed energy resource management system, as
well as microgrid modeling and protection.
Harsha Padullaparti received the B.Tech. degree in electrical and electron‐
ics engineering from Jawaharlal Nehru Technological University, Hyder‐
abad, India, in 2007, the M.S. degree in electrical engineering from Indian
Institute of Technology, Madras, India, in 2010, and the Ph. D. degree in
electrical and computer engineering from the University of Texas at Austin,
Austin, USA, in 2018. He was a Senior Engineer at Power Grid Corpora‐
tion of India Limited (PGCIL), Kolkata, India, where he worked from 2009
to 2014. He is currently a Researcher in the Power Systems Engineering
Center at the National Renewable Energy Laboratory (NREL), Golden,
USA. His research interests include data analytics for distribution network
operations, advanced distribution management system, distributed energy re‐
source management system, distribution system modeling, and renewable en‐
ergy integration.
Fei Ding received the B.S. and M.S. degrees from Tianjin University, Tian‐
jin, China, and the Ph. D. degree from Case Western Reserve University,
Cleveland, USA. She is currently a Senior Research Engineer with the Na‐
tional Renewable Energy Laboratory (NREL), Golden, USA. She is leading
multiple projects with NREL on developing advanced models and controls
for managing grid-edge resources to enhance grid flexibility, reliability and
resilience, and developing new advanced distribution management system
and distributed energy resource management system applications to modern‐
ize emerging distribution networks. Her research interests include renewable
energy grid integration, distributed energy resource aggregation and control,
grid resilience, and security.
Murali Baggu received the B.Tech. degree in electrical and electronics engi‐
neering from Kakatiya University, Warangal, India, the M.S. degree in elec‐
trical engineering from the University of Idaho, Moscow, USA, and the Ph.
D. degree in electrical engineering from the Missouri University of Science
and Technology, Rolla, USA, in 2009. Currently, He is Laboratory Program
Manager for Grid Integration at the National Renewable Energy Laboratory
(NREL), Golden, USA. In this role, he leads the U.S. Department of Energy
Office of Electricity and Grid Modernization’s Initiative programs at
NREL. He currently directs and leads the NREL’s Advanced Distribution
Management Systems and Puerto Rico Grid Recovery and Resilience ef‐
forts. He has extensive experience in advanced grid control and evaluation
for future power systems with high penetration of distributed energy resourc‐
es. Before joining NREL he worked as a Lead Power Systems Engineer at
GE Global Research, Niskayuna, USA, where he developed advanced volt/
var control and distributed energy resource management algorithms. At GE
Global Research, he also led the technology development and deployment
of large-scale energy storage integration with photovoltaic systems for U.S.
Department of Defense Marine Corps installations. He has four issued pat‐
ents and more than 50 publications in these areas. He is presently Chair of
the IEEE Distribution System Operation & Planning Sub-committee. His re‐
search interests include grid integration of renewables systems (wind and
PV), energy storage system integration, distribution automation, and grid op‐
erations and control.
285

---
