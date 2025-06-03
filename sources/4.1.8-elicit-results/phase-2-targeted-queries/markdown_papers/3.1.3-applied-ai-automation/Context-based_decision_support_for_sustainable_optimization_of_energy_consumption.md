# Context-based decision support for sustainable optimization of energy consumption

## Paper Metadata

- **Filename:** Context-based decision support for sustainable optimization of energy consumption.pdf
- **DOI:** None
- **Authors:** Not available
- **Year:** Not available
- **Journal/Venue:** Not available
- **URL:** Not available
- **Extraction Date:** 2025-06-03T15:04:09.731047
- **Total Pages:** 15

## Abstract

Abstract not available from BibTeX metadata.

## Keywords

Keywords not available from BibTeX metadata.

---

## Full Text Content



### Page 1

energies
Article
Decision Support System for a Low Voltage
Renewable Energy System
Iulia Stamatescu *, Nicoleta Arghira *, Ioana F˘ag˘ar˘a¸san, Grigore Stamatescu,
Sergiu Stelian Iliescu and Vasile Caloﬁr
Department of Industrial Automation and Informatics, Faculty of Automatic Control and Computers,
University “Politehnica” of Bucharest, 313 Splaiul Independentei, 06004 Bucharest, Romania;
ioana@shiva.pub.ro (I.F.); grigore.stamatescu@upb.ro (G.S.); iliescu@shiva.pub.ro (S.S.I.);
vasile@shiva.pub.ro (V.C.)
* Correspondence: iulia.stamatescu@aii.pub.ro (I.S.); nicoleta.arghira@aii.pub.ro (N.A.);
Tel.: +40-21-402-9147 (I.S.)
Academic Editor: Wenxin Liu
Received: 6 November 2016; Accepted: 9 January 2017; Published: 18 January 2017
Abstract: This paper presents the development of a decision support system (DSS) for a low-voltage
grid with renewable energy sources (photovoltaic panels and wind turbine) which aims at achieving
energy balance in a pilot microgrid with less energy consumed from the network. The DSS is based
on a procedural decision algorithm that is applied on a pilot microgrid, with energy produced from
renewable energy sources, but it can be easily generalized for any microgrid. To underline the beneﬁts
of the developed DSS two case scenarios (a household and an ofﬁce building with different energy
consumptions) were analyzed. The results and throw added value of the paper is the description
of an implemented microgrid, the development and testing of the decision support system on real
measured data. Experimental results have demonstrated the validity of the approach in rule-based
decision switching.
Keywords: power systems; microgrid; decision support system; distributed energy resources;
renewable energy sources; low voltage renewable energy system
1. Introduction
A microgrid is deﬁned as “a group of interconnected loads and distributed energy resources
(DER) with clearly deﬁned electrical boundaries that act as a single controllable entity with respect to
the grid and it can connect and disconnect from the grid to enable it to operate in both grid-connected
or island mode” [1]. The beneﬁts of this concept lie in the advanced functions that are available, such
as setting the operation mode: on-grid or islanding when energy cannot be supplied from the national
grid (during peak times of the day).
Microgrids could be described as upgraded electrical networks which possess two-way digital
communication between the supplier and consumer, intelligent metering, and monitoring systems [2].
Microgrid technology incorporates traditional elements, as well as new generation elements: a set of
control systems and grid management, sensors, communications, and information systems. It combines
software and hardware designed to signiﬁcantly improve the way the current energy system is
operated, while providing the possibility of further modernization.
The beneﬁts of a microgrid can be widely acknowledged. Microgrids can manage direct
communication and interaction among energy distribution companies, households, or consumers.
The implementation of the microgrid opens several possibilities to consumers to directly control and
manage their individual consumption patterns [3]. Among the undisputed beneﬁts, a slight disadvantage
lies in the variability of electricity prices, which directly impacts energy usage prediction [4].
Energies 2017, 10, 118; doi:10.3390/en10010118
www.mdpi.com/journal/energies

---


### Page 2

Energies 2017, 10, 118
2 of 15
Microgrids will be the foundation stone of future decentralized power systems. This will open the
window of opportunity for the usage of on-shore and off-shore renewable energy and electric vehicles,
while maintaining availability for conventional power generation and power system adequacy [5].
Using the microgrid technology the consumers have access to real-time information about their energy
consumption, having the possibility to make smart choices about the energy usage. Thus, consumers
will be able to reduce consumption during times of peak consumption, adjusting the amount taken
from the grid [6].
The agenda of the European Union for 2020 comes with a clear message regarding the energy
ﬁeld. The future energy infrastructure should develop the efﬁcient and sustainable use of natural
resources. The existing grid must be upgraded, otherwise the generation of renewable energy will be
put on hold, the internal energy market will develop slower, and energy efﬁciency and savings will be
missed [7].
The distributed power generation in the low voltage electrical networks (supplied at 230/400 V)
has a very important role in the international research due to its effects and its technical
implementation [8]. More precisely, the local power generation losses of distributed power can be
compensated, but an excess of power can generate overloads of the electric line, providing instability of
the network [9]. Hence, the rational management of the electrical energy must be ensured to maintain
the balance of power/energy on each line of the network (generated power equal to consumed
power) [10]. The differences from this ideal case led to over- and under-production of energy and the
stability of the distributed power system will be perturbed [11,12].
Additionally, energy ﬂow optimization should be tackled. In the context of RES, the optimization
function should consider uncertainties. Another important challenge is the minimization of the energy
costs, [13]. Solutions for centralized control and optimization for integrated energy systems were
developed to minimize the energy waste in the generation process as well, [14]. Information systems
that support themselves on artiﬁcial intelligence techniques and consider knowledge and reasoning
(rules) can be a solution for power ﬂow computation, optimization, and planning. Bayesian networks,
fuzzy systems, decision trees, and decision tables were used for power system control and optimization
in the later literature [15,16].
European concern for distributed generation from renewable energy systems (DG-RES) were
materialized by setting up a giant cluster of projects called the Integration of Renewable Energy
Sources and Distributed Generation into the European Electricity Grid—Integration of Renewable
Energy Sources and Distributed Generation into the European Electricity Grid (IRED) cluster [17].
The consortium highlighted the need of an energy management system at a macro and micro level
considering that the existing control strategies were not always giving the optimal results.
In this context, the paper presents the implementation of a decision support system for a
low-voltage grid with renewable energy sources (photovoltaic panels and wind turbine). The goal
of the decision-based control system is to achieve energy balance in the microgrid with less energy
consumed from the grid.
2. Decision Support Solutions for Power Systems
Decision support systems (DSS) are information systems that integrate dedicated informatics
objects for decision assistance and general instruments as a constituent part of the global system [14].
In power systems (PS), DSSs are more and more studied in the last years when variable energy
renewable sources generate in power grids. The main goal of the studied decision support systems
is to maintain the load-generation balance always (to assure the adequacy of the power system).
The solutions concern:
A.
PS planning [18,19]
B.
PS operation [20,21]
Authors in [19] propose a methodology for jointly tackling the problem of determining the
number, location, type, and size of distributed generators (DGs), while also considering the availability

---


### Page 3

Energies 2017, 10, 118
3 of 15
of the (renewable) sources that DGs harvest. This approach is applied in the planning phase of the
power system when the meta-heuristic algorithm (e.g., particle swarm optimization) result sets the
amount of renewable energy that can be connected to a speciﬁc electrical line/bus.
Power system planning is very challenging and a framework for a decision-making aid was
proposed in [20]. A complex consumption model was developed considering heating, electricity, and
transportation as well as cost and environmental aspects. The paper computes distinctly the energy
consumption and generation, but the decision is left for the system operators.
The DSS described in [21] is part of B type DSSs and it describes a simulation-based decision
support tool that considers prediction of the performance of photovoltaic panel (PV), wind, and battery
technologies to achieve load–generation balance. The matching of supply options to demand proﬁles
is quantitative measured through an inequality coefﬁcient. Still, the computation formula is not clear,
nor is the used algorithm, and the results of the case study are not provided.
A complex smart decision support system for the smart city of Florence in Italy that handles
different areas (transport and mobility, commercial, environment, energy) was proposed in [22].
The decision-making process was based on hierarchical decision trees and each node has three options:
positive, negative, and uncertain. The outcome of the decision tree is based on a bottom-up strategy [23],
but in this paper the main importance is given to user’s option. An adapted smart DSS architecture for
a microgrid is proposed in Figure 1.
Decision
Maker Client
Registered
User Client
Guest
User Client
Server
Client Server
Interface
User Management
Interface
DSS Module
Micro Grid
Relational
Database
Admin
Relational
Database
 
Figure 1. Smart DSS architecture for a microgrid, adapted from [22].
A decision tree approach for controlled islanding of a microgrid is presented in [24], as are decision
rules concerning the situations when incidents occur with continuous monitoring of the system
parameters (voltage, frequency, harmonics, current, etc.). This DSS based on an event classiﬁcation
model (different types of faults) can be used for initiation of controlled islanding of the microgrid.
The literature survey shows different strategies used for decision support systems, but the
outcome of these studies does not offer speciﬁc power generation–consumption balance solutions.
The need for proposed scenarios involving different types of distributed generation in microgrids for
the users to be adopted is called for.
3. The Microgrid Hardware Architecture
The proposed microgrid (Figure 2) is implemented at the CIST Multidisciplinary Scientiﬁc and
Technologic Research Institute (ICSTM) of “Valahia” University of Targoviste (UVT) [25]. The research
institute is spread over an area of 7250 m2 and has 2240 m2 built area, which includes 35 research
laboratories, ﬁve technical laboratories, six functional annexes, seven administrative spaces, and four
dissemination spaces. The studied microgrid is composed of three subsystems:
•
Subsystem 1: 10 photovoltaic panels (10 PVs) with a maximum power of P10 PV max = 50 W.
•
Subsystem 2: a photovoltaic panel (1 PVBat) with a maximum power of PPVBat max = 220 W and a
bank of batteries.
•
Subsystem 3: a wind system (EOL400) with a maximum power of PEOL max = 400 W.

---


### Page 4

Energies 2017, 10, 118
4 of 15
B attery B ank
Eos G 200 24V
10PVs
PW X500
(P=50W ; V=17.2V; I=2.9A)
EO L400
P n=400W
Inverter
Sunny Island
SI 3324
Inverter
Sunny B oy
P D C _m ax =2200W
Inverter
W indy B oy
W B 1100LV
1PVB at
P m ax = 220W
Subsystem 1
Subsystem 2
Subsystem 3
Pow er G rid
U = 220V
f=50H z
Voltage R egulator
C onsum er
Figure 2. The developed hardware infrastructure—pilot microgrid.
Subsystem 1 (Figure 3) is composed of: 10 photovoltaic panels (10 PVs) (Figure 4a) and an
inverter (Figure 4b). The 10 PVs were oriented east–west, with an area of southern exposure and
their inclination is about 30 degrees. The PVs are PWX500 type (power = 50 W, voltage = 17.2 V and
current intensity = 2.9 A) and they were produced by Photo Watt International Co (Bourgoin-Jallieu,
France) [26]. The 10 PVs photovoltaic system mounted on the terrace is connected to a Sunny Boy
SB2100TL inverter (maximum power = 2200 W, maximum voltage = 600 V, minimum voltage = 125 V)
from SMA (Niestetal, Germany) which is connected to the local power network.
Figure 3. Block diagram of the 10 photovoltaic panels connected to the local power network.

(a) 
(b) 
Figure 4. The components of the subsystem 1: (a) 10 photovoltaic panels; and (b) the Sunny Boy
SB2100TL inverter.

---


### Page 5

Energies 2017, 10, 118
5 of 15
Subsystem 2 (Figure 5) is composed of a photovoltaic panel (1 PVBat) (Figure 6a), an inverter
(Figure 6b), a voltage regulator (Figure 6c) and a battery bank (Figure 6c). The photovoltaic panel
was oriented east–west, with an area of southern exposure and an inclination of about 30 degrees.
The photovoltaic system used in this application are produced by Sunshine Solar Technology Co
(Huaxi Industrial Zone, Wuxi, China) and the technical characteristics of the ST220 type PV are as
follow: maximum power = 220 W, maximum current intensity = 36.6 V, maximum power point
voltage = 30 V, maximum power point current intensity = 7.345 A [27]. The 1 PVBat is mounted
on the terrace and it is connected to a bank of batteries via a 24 V voltage regulator (Steca Tarom
245-24V-45A type (Memmingen, Germany)). Subsystem 2 is connected to the local power network
with a Sunny Island SI3324 inverter (maximum voltage = 32 V, minimum voltage = 21 V) from SMA
(Niestetal, Germany). The battery bank consists of 12 lead-gel batteries (type Polymer Gel Battery
Standby Eos G200 2V200Ah from Narada (Hangzhou, China)), with the individual voltage of 2 V,
connected in series. Following this conﬁguration, the bank’s terminals have 24 V.
Voltage 
regulator
Steak Tarom
24V
Figure 5. Block diagram of Subsystem 2 connected to the grid.
 
(a) 
(b) 
(c) 
Figure 6. The components of the subsystem 2: (a) a photovoltaic panel; (b) the Sunny Island SI3324
inverter from SMA; and (c) the battery’s bank and the voltage regulator.
Subsystem 3 (Figure 7) is composed of one wind system (Figure 8a) and one inverter
(Figure 8b). The wind system (EOL400) is situated about 6 m above the terrace and it has the
following characteristics:
•
Rated power = 400 W
•
Starting wind speed = 5 m/s
•
Maximum wind speed = 50 m/s
•
Output voltage 20–60 V DC

---


### Page 6

Energies 2017, 10, 118
6 of 15
Figure 7. Block diagram of Subsystem 3 connected to the grid.
(a) 
(b) 
Figure 8.
The components of Subsystem 3:
(a) the wind system; and (b) the Windy Boy
WB1100LV inverter.
The used inverter in this system is a Windy Boy WB1100LV inverter from SMA (Niestetal,
Germany) with the following features: maximum power = 200 W, maximum voltage = 60 V, minimum
voltage = 21.3 V. The windy Boy inverter is connected to the local power network.
4. The Developed Microgrid Controller Software
The microgrid controller software is used to manage the electrical energy in a low-voltage local
grid, connected to the national grid. A block diagram of the microgrid controller software is presented
below (Figure 9). The software has four major functions:
•
The monitoring function/module
•
The diagnosis function/module
•
The prediction function/module
•
The decision support system module
 
Figure 9. Block diagram of the microgrid software.

---


### Page 7

Energies 2017, 10, 118
7 of 15
The monitoring function gathers data regarding signiﬁcant parameters that characterize the
energy production and consumption (current, voltage, energy, etc.) and the environment factors (wind
speed, irradiance, etc.). The generation parameters can be achieved either by speciﬁc sensors or directly
from the inverters through the Sunny Web Box device. The monitored data is processed to ﬁnd the
daily energy proﬁle [28].
The diagnosis function is used to evaluate the state of the network, the state of each component,
and to identify the causes of damage or an alarm in the network. Fault diagnosis is used to determine
the type, size, and location of the fault and the time of its occurrence, based on the analytics observed
or heuristic symptoms [29]. The design of the diagnosis function was carried out using methods based
on the signal model such as “Fault detection with trend checking and ﬁxed threshold”, as well as
statistical tests for detecting changes (“Wald Tests”).
The method “Fault detection with trend checking and ﬁxed threshold” (Figure 10) is based on
calculating the ﬁrst-order derivative of the signal and monitoring its evolution. If the thresholds are
ﬁxed properly this method can detect a fault faster than other methods:
•
Y = d Y(t)
dt
;
•
Ymin <
•
Y(t) <
•
Ymax
(1)
upper 
threshold 
exceeding 
alarm
lower 
threshold 
exceeding 
alarm
 
Figure 10. The fault detection method with trend checking and ﬁxed threshold.
The prediction function aims to achieve short and medium-term forecasts of electricity generation
from renewable sources in the developed microgrid, as well as the prediction of energy consumption
for the used equipment (e.g., lighting, ventilation and heating system, computers, etc.).
Power generation prediction can be achieved using artiﬁcial intelligence algorithms.
The implementation with an adaptive neuro-fuzzy inference system for RES production prediction
was described in [2]. The training set of the test consists of objects with the following attributes: time
of day (0–23), season (summer, winter, etc.), month of the year (January, February, etc.), solar radiation,
wind speed, active power from photovoltaic panels, active power produced by the wind turbine.
The authors in [30] are exploring ways of performing accurate forecasts of generating power from
renewable energy sources so that independent system operators can, consequently, act.
The prediction, for the energy consumption of each equipment can be done using a
knowledge-based expert system. The historical consumption is used to generate knowledge through a
decision table classiﬁcation method. The result of the classiﬁcation will show if the equipment will
consume (pr(h) = 1) or not (pr(h) = 0) at a certain hour. The electricity consumption will be computed
considering the following equation:
P(h) = pr(h) × P
(2)

---


### Page 8

Energies 2017, 10, 118
8 of 15
where P is the mean value of positive power from historical consumption.
The decision function is the one that used information/knowledge from the other three modules
and computes decisions (regarding the RES to be used or grid connection) as a support for the users [31].
The application and results of this paper consider the decision support system and it will be detailed
in the next chapter of this article.
5. The Decision Support System and Experiment Results
5.1. Decision Support System Principle
Decision support systems (DSS) are primarily concerned with the representation and processing
of explicit knowledge. The DSS’s knowledge attribute types are three basic categories: descriptive,
procedural and reasoning knowledge [32]. Procedural knowledge consists of a set of procedures for
handling various tasks. Examples of procedural knowledge include algorithms, strategies, action plans,
programs, and methods [33]. Instances of these three types of knowledge (descriptive, procedural and
reasoning) can be applied in the generation of new knowledge and has long been recognized in the
building of decision support systems [34].
The developed DSS is based on a procedural decision algorithm that is applied on the pilot
microgrid, but it can be easily generalized for any microgrid. The developed decision support
system module aims at achieving a set of rules that lead to satisfying the electricity consumed in the
studied microgrid.
We deﬁne the following:
•
PCONS is the consumed power (e.g., the institute as consumer) in the developed microgrid.
•
PPV is the power produced by photovoltaic panels.
•
PEOL is the power produced by the wind turbine.
•
PBAT is the power stored in batteries.
•
PGRID is the output power from the public electricity supply.
The condition that should be satisﬁed at any time by the microgrid electric network is:
PPV + PEOL + PBAT = PGRID + PCONS
(3)
PPV = P10PVs + P1PVBat
(4)
where:
•
P10 PVs represents the power produced by the ﬁrst subsystem (10 photovoltaic panels (10 PVs)
with a maximum power of P10 PV max = 50 W).
•
P1 PVBat represents the power produced by the second subsystem (a photovoltaic panel (1 PVBat)
with a maximum power of P1 PVBat max = 220 W connected to a bank of batteries).
The PGRID power is positive when it receives energy from RES generation and it is negative when
the consumer is supplied from the national grid.
The geographic region where the microgrid is installed is favorable to produce energy from
renewable sources (wind and photovoltaics). For the system protection, the consumer (ICSTM institute)
is linked at the national grid all the time. For the given microgrid, a set of speciﬁc rules were designed.
The rules tackle the possibilities of energy connection of the speciﬁc proposed microgrid.
A set of decision rules are listed in the decision table below (Table 1). Rule 1 state that when the
consumed power is greater than the power available from the PV, wind, and batteries, then the system
should be connected to the public grid. Rule 2 depicts the situation in which the loaded battery is used
when the consumption is higher than the microgrid production. Rule 3 states that if the produced
power is greater than the consumed power, the battery will be connected for loading. Rule 4 considers

---


### Page 9

Energies 2017, 10, 118
9 of 15
the photovoltaic generations lower than the consumption and, if the weather conditions are favorable,
the wind turbine must be connected. Rule 5 considers the wind turbine generation lower than the load
and, if the weather conditions are favorable, the photovoltaic system needs to be connected. The two
available renewable power sources (photovoltaic panels and wind) are connected continuously to the
microgrid. Rules 4 and 5 present the situation in which the consumer is active and the battery cannot
supply energy. These two account for the commonly-occurring scenarios where increased production
of wind energy is mutually exclusive with increased production of photovoltaic energy.
Table 1. The DSS decision rules.
No.
Condition
Decision
Rule 1.
PCONS > PPV + PEOL + PBAT
Public Network (Grid) Connection
Rule 2.
PCONS > PPV + PEOL
Connection to the battery supply
Rule 3.
PCONS < PPV + PEOL
Battery connection for loading
Rule 4.
PCONS > PPV and favorable weather conditions
Wind generator connection
Rule 5.
PCONS > PEOL and favorable irradiance
Photovoltaic panels connection
5.2. DSS Experiment
The developed DSS based on the above set of rules was implemented in two case studies. The
ﬁrst case study is implemented on the ICSTM microgrid system for the day of 5 May 2016. Since the
consumption of the ICSTM institute is far larger than the generated power, another case study is also
considered. In this case study, the developed DSS uses the consumption of a residence. This shows the
DSS system operating in a simulation case where the generation and load are approximately equal.
With the help of the simulation case, different applied rules can be used and observed.
Further, the energy production of each subsystem described in paragraph 3 is shown.
In Figure 11 the monitored production from Subsystem 1 (10 PV panels, max 500 W) is presented.
As expected, maximum power is obtained during the time interval 10 h–13 h and energy generation
was achieved between 7 a.m. and 7 p.m. since 5 May was a sunny day.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
Time [h]
0
50
100
150
200
250
300
350
400
450
500
Power [W]
P hotovoltaic panel pow er production
S ubsystem 1 (10P V s) pow er production
Figure 11. Subsystem 1: 10 PVs generation.
Figure 12 shows the energy production for the PV of Subsystem 2 (max 220 W) on 5 May 2016.
Peak production is realized between 10 a.m. and 4 p.m.

---


### Page 10

Energies 2017, 10, 118
10 of 15
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
Time [h]
0
50
100
150
200
250
Power [W]
P hotovoltaic panel pow er production
S ubsystem 2 (1P V B at) pow er production
Figure 12. Subsystem 2: 1 PV generation connected to a battery bank.
The wind turbine was not installed in May 2016 but measured data using an online database [35]
was used when conducting the experiment. This data is presented in Figure 13.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
Time [h]
0
50
100
150
200
250
300
350
400
Power [W]
W ind pow er production
S ubsystem 3 (E ol400) pow er production
Figure 13. Subsystem 3: wind generation.
The energy consumption was monitored in the building and the DSS rules were implemented
overall the microgrid.
5.3. Results and Discussion
5.3.1. Case Study 1—Simulation
This case study analyzes the power generated by the three subsystems described above
(Subsystem 1: 10 PVs generation; Subsystem 2: 1 PV generation connected to a battery bank; and

---


### Page 11

Energies 2017, 10, 118
11 of 15
Subsystem 3: wind generation) and the consumed power of a residence. The residence consumption
is determined by the following appliances: a fridge (180l), a halogen lamp (0.5 k W) and the power
supply from a wood boiler. The DSS output actuates to use the energy supply of one or more of the
following: power grid, PV panels, wind turbine, or battery. Both energy production and consumption
are represented in Figure 14.
Figure 14. Load–generation curves: case study 1.
An application of the developed decision tree algorithm can be observed in Figure 14 and an
hourly detail of the applied rules can be seen in Table 2. The ﬁgure shows ﬁrst that the battery will be
used (per its storage capacity) during the day when the consumption is greater than the production
(e.g., 1 a.m.–2:15 a.m.). Between 2:15 a.m. and 8:45 a.m. the consumption is greater than the production
generated by the wind subsystem, rule 1 will be applied: the command for the connection to the
national grid. From 8:45 a.m. to 9:45 a.m. the battery will be connected for loading and the stored
energy will be used from 9:45 a.m. to 10:30 a.m. During the day (10:30 a.m. to 17:15 p.m.) the consumer
is not active and the bank of batteries will be connected for loading. The accumulated energy will be
used ﬁrst between 17:15 p.m. and 19:30 p.m. when the consumption is greater than the production
(wind plus photovoltaic). At night (19:30 p.m. to 23 p.m.) the residence consumption is around 1416 W
so it cannot be covered by the RES generation and the DSS rule involves the connection to the national
grid. During the night (23 p.m. to 24 p.m.) the consumer is not active, so it does not use any electricity
and the generated power is greater than the consumed power. Though, the battery will be connected
for loading and the wind energy production can be stored for later use.
Table 2. Application of DSS decision rules on the simulation case study.
Time Interval
Applied Rule
Condition
Action
1 a.m.–2:15 a.m.
Rule 2.
PCONS > PPV + PEOL
Connection to the battery supply
2:15 a.m.–8:45 a.m.
Rule 1:
PCONS > PPV + PEOL + PBAT
Public Network (Grid) Connection
8:45 a.m.–9:45 a.m.
Rule 3.
PCONS < PPV + PEOL
Battery connection for loading
9:45 a.m.–10:30 a.m.
Rule 2.
PCONS > PPV + PEOL
Connection to the battery supply
10:30 a.m.–17:15 p.m.
Rule 3.
PCONS < PPV + PEOL
Battery connection for loading
17:15 p.m.–19:30 p.m.
Rule 2.
PCONS > PPV + PEOL
Connection to the battery supply
19:30 p.m.–23 p.m.
Rule 1.
PCONS > PPV + PEOL + PBAT
Public Network (Grid) Connection
23 p.m.–24 p.m.
Rule 3.
PCONS < PPV + PEOL
Battery connection for loading

---


### Page 12

Energies 2017, 10, 118
12 of 15
5.3.2. Case Study 2
The DSS output actuate such as to use for energy supply one or more of the following: power
grid, PV panels, wind turbine, or battery. Both energy production and consumption of the ICSTM
institute are represented in Figure 15.
 
Figure 15. Load–generation curves for the day of 5 May: case study 2.
An application of the developed decision tree can be observed on Figure 15 and an hourly detail
of the applied rules can be seen in Table 3. The ﬁgure shows that during the night (1 a.m. to 6 a.m.;
9 p.m. to 12 p.m.) the consumer is not active, so it does not use any electricity. Since the wind turbine
had favorable weather conditions, it generated and the DSS system commands the link with the battery
bank so that this outcome can be accumulated for later use. During daytime (7 a.m. to 9 p.m.) the
ICSTM consumption is around 25 k W, so it cannot be covered by the RES generation in the pilot
microgrid, so the DSS rule involves the connection to the national grid.
Table 3. Application of DSS decision rules on the pilot microgrid.
Time Interval
Applied Rule
Condition
Action
1 a.m.–6 a.m.
Rule 3.
PCONS < PPV + PEOL
Battery connection for loading
7 a.m.–9 p.m.
Rule 1:
PCONS > PPV + PEOL + PBAT
Public Network (Grid) Connection
9 p.m.–12 p.m.
Rule 3.
PCONS < PPV + PEOL
Battery connection for loading
The beneﬁts of using such a system are multiple in terms of energy consumption costs (since the
load is not always connected to the grid and it operates in “island mode”), as well as CO2 emission
reduction (using the renewable power sources). For a residential household, during spring to autumn
months when the radiance is high, half of the consumed energy can be supplied from the microgrid, so
the energy bill will decrease accordingly. However, this would not be possible without the DSS system
because during peak production and lower load periods, the energy would be spilled and not saved
for later in batteries, as it happens with the DSS control.

---


### Page 13

Energies 2017, 10, 118
13 of 15
6. Conclusions
We have presented the design, development, and implementation of a decision support system
for a low-voltage microgrid. The model revolves around a real operational microgrid system that
includes solar and wind energy generation, and energy storage batteries as well. Considering the
software implementation, the approach is ﬂexible as to accommodate different microgrid structures
and patterns.
The proposed decision support system is based on a decision table with ﬁve rules that are
explained in detail in respect to the implemented microgrid. Two case studies were presented: a
household with lower energy consumption and an ofﬁce building (the ICSTM institute) with high
energy consumption during work hours. The experimental results showed the application of the
proposed rules and it have demonstrated the validity of the approach in terms of energy cost reduction,
as well as an efﬁcient use of the produced renewable energy with the battery deployment.
The provided tool is relevant to several stakeholders (energy providers, consumers, etc.) which
can deploy it for more reliable, safer, and economic operation of their electrical (micro-)grid.
Future work aims at implementing ﬁner-grained rules within the decision support framework
and associated software, as well as improves and account for load and weather predictions to improve
the decision mechanisms for the microgrid operator. Additionally, a success metric can be computed
since, for now, just a qualitative gain in terms of energy provided by the microgrid subsystems was
considered (and not supplied from the national grid).
Acknowledgments: This work was mainly supported by the Romanian National Authority for Scientiﬁc Research,
CNDI-UEFISCDI, project code PN-II-PT-PCCA-2011-3.2-1616, “Intelligent Decision Support and Control System
for Low Voltage Grids with Distributed Power Generation from Renewable Energy Sources” (INDESEN), Contract
nr. 42/2012.
Author Contributions: Iulia Stamatescu and Nicoleta Arghira wrote major paragraphs of the paper and integrate
the contributions written by the other authors. Ioana F˘ag˘ar˘a¸san provided algorithms and principles used for fault
detection and diagnosis modules, and offered guidance and supervised the development of these modules. All the
paragraphs regarding these aspects are written by this author. Sergiu-Stelian Iliescu conceived the idea of research
and provided guidance. Grigore Stamatescu and Vasile Caloﬁr performed the analysis for the relevant study
case and provided the results used for demonstration in this article. All authors have contributed signiﬁcantly to
this work.
Conﬂicts of Interest: The authors declare no conﬂict of interest.
References
1.
Tristan Glenwright, Introduction to Microgrids, U.S. Department of Energy, Ofﬁce of Electricity Delivery
and Energy Reliaility. 2012. Available online: www.oe.energy.gov (accessed on 6 October 2016).
2.
Elena Dragomir, O.; Dragomir, F.; Stefan, V.; Minca, E. Adaptive Neuro-Fuzzy Inference Systems as a Strategy
for Predicting and Controling the Energy Produced from Renewable Sources. Energies 2015, 8, 13047–13061.
[Cross Ref]
3.
Rasheed, M.B.; Javaid, N.; Awais, M.; Khan, Z.A.; Qasim, U.; Alrajeh, N.; Iqbal, Z.; Javaid, Q. Real Time
Information Based Energy Management Using Customer Preferences and Dynamic Pricing in Smart Homes.
Energies 2016, 9, 542. [Cross Ref]
4.
Liang, H.; Zhuang, W. Stochastic Modeling and Optimization in a Microgrid: A Survey. Energies 2014, 7,
2027–2050. [Cross Ref]
5.
Beykverdi, M.; Jalilvand, A.; Ehsan, M. Cooperative Energy Management of Hybrid DC Renewable Grid
Using Decentralized Control Strategies. Energies 2016, 9, 859. [Cross Ref]
6.
Arghira, N.; Hawarah, L.; Ploix, S.; Jacomino, M. Prediction of appliances energy use in smart homes. Energy
2012, 48, 128–134. [Cross Ref]
7.
Europeean Stategie for 2020. Available online: http://ec.europa.eu/europe2020/europe-2020-in-a-nutshell/
priorities/index_ro.htm (accessed on 6 October 2016).
8.
Cha, H.-J.; Won, D.-J.; Kim, S.-H.; Chung, I.-Y.; Han, B.-M. Multi-Agent System-Based Microgrid Operation
Strategy for Demand Response. Energies 2015, 8, 14272–14286. [Cross Ref]

---


### Page 14

Energies 2017, 10, 118
14 of 15
9.
Oh, S.-J.; Yoo, C.-H.; Chung, I.-Y.; Won, D.-J. Hardware-in-the-Loop Simulation of Distributed Intelligent
Energy Management System for Microgrids. Energies 2013, 6, 3263–3283. [Cross Ref]
10.
Kuo, M.-T.; Lu, S.-D. Design and Implementation of Real-Time Intelligent Control and Structure Based on
Multi-Agent Systems in Microgrids. Energies 2013, 6, 6045–6059. [Cross Ref]
11.
Giordano, V.; Meletiou, A.; Covrig, C.F.; Mengolini, A.; Ardelean, M.; Fulli, G.; Jimenez, M.S.; Filiou, C.
Smart Grid projects in Europe: Lessons learned and current developments. Jt. Res. Cent. Inst. Energy Transp.
2013. [Cross Ref]
12.
Package of Implementation Measures for the EU’s Objectives on Climate Change and Renewable Energy for
2020, Directive of the European Parliament and of the Council on the Promotion of Use of Renewable Energy
Sources, {COM (2008) 19}. Available online: http://ec.europa.eu/energy/climate_actions/doc/2008_res_ia_
en.pdf (accessed on 6 October 2016).
13.
Jain, N.; Alleyn, A.G. A framework for the optimization of integrated energy systems. Appl. Therm. Eng.
2012, 48, 495–505. [Cross Ref]
14.
Robescu, L.D.; Lazaroiu, G.C.; Dumbrava, V.; Manea, E.; Presura, A. Optimizing electricity costs of
wastewater treatment plant in presence of RES and power market. In Proceedings of the 9th International
Symposium on Advanced Topics in Electrical Engineering (ATEE), Bucharest, Romania, 7–9 May 2015;
pp. 808–811.
15.
Jain, A.; Duin, R.P.W.; Mao, J. Statistical pattern recognition: A review. IEEE Trans. Pattern Anal. Mach. Intell.
2000, 22, 4–37. [Cross Ref]
16.
Mayne, D.; Falugi, P.J. Generalized Stabilizing Conditions for Model Predictive Control. J. Optim. Theory Appl.
2016, 169, 719. [Cross Ref]
17.
Integration of Renewable Energy Sources and Distributed Generation into the European Electricity Grid
Cluster. Available online: http://www.ired-cluster.org/ (accessed on 6 October 2016).
18.
Filip, F.G. Decision Support Systems (Sisteme Support Pentru Decizii); Technical Publishers: Bucharest,
Roamania, 2004.
19.
Torrent-Fontbona, F.; Lopez, B. Decision support for grid-connected renewable energy generators planning.
Energy 2016, 115, 577–590. [Cross Ref]
20.
Girones, V.C.; Moret, S.; Marechal, F.; Favrat, D. Strategic energy planning for large-scale energy systems: A
modelling framework to aid decision-making. Energy 2015, 90, 173–186. [Cross Ref]
21.
Born, F.J.; Clarke, J.A.; Johnstone, C.M. Development and demonstration of a renewable energy based energy
demand/supply decision support tool for the building design profession. In Proceedings of the 7th IBPSA
Conference, Rio de Janeiro, Brazil, 13–15 August 2001; pp. 1–8.
22.
Bartolozzi, M.; Bellini, P.; Nesi, P.; Pantaleo, G.; Santi, L. A Smart Decision Support System for Smart
City. In Proceedings of the 2015 IEEE International Conference on Smart City, Guadalajara, Mexico,
25–28 October 2015; pp. 117–122.
23.
Pupaza, D. Industrial Informatics System Analysis (Analiza de Sistem in Informatica Industriala); Agir Publisher:
Bucharest, Romania, 2006.
24.
Azim, R.; Li, F. A Decision Tree Based Approach for Controlled Islanding of Microgrids. In Proceedings of the
2016 IEEE/PES Transmission and Distribution Conference and Exposition, Dallas, TX, USA, 3–5 May 2016;
pp. 1–5.
25.
ICSTM Multidisciplinary Scientiﬁc and Technologic Research Institute (ICSTM) of “Valahia” University of
Targoviste (UVT) Homepage. Available online: http://916.icstm.ro (accessed on 6 October 2016).
26.
PWX500,
Photo Watt
International.
Available
online:
http://pdf.archiexpo.com/pdf/photowatttechnologies/photowatt-pwx500--12v/62614--84848.html (accessed on 6 October 2016).
27.
PV ST220, Sunshine Solar Technology. Available online: http://www.sunshinesolar.com.cn/product_show.
asp?id=904 (accessed on 6 October 2016).
28.
Dragomir, O.E.; Dragomir, F.; Radulescu, M. Matlab Application of Kohonen Self-Organising Map to Classify
Consumers’ Load Proﬁles. Procedia Comput. Sci. 2014, 31, 474–479. [Cross Ref]
29.
Fagarasan, I.; Ploix, S.; Gentil, S. Causal fault detection and isolation based on a set-membership approach.
J. Autom. 2004, 40, 2099–2110.
30.
Dragomir, F.; Dragomir, O.E. Forecasting of photovoltaic power generation by RBF neural networks.
Adv. Mater. Res. 2014, 918, 200–205. [Cross Ref]

---


### Page 15

Energies 2017, 10, 118
15 of 15
31.
Stamatescu, I.; Stamatescu, G.; Arghira, N.; F˘ag˘ar˘asan, I.; Iliescu, S.S. Fuzzy decision support system for solar
tracking optimization. In Proceedings of the 2014 International Conference on Development and Application
Systems (DAS), Suceava, Romania, 15–17 May 2014.
32.
Bonczek, R.H.; Holsapple, C.W.; Whinston, A.B. Future directions in developing decision support systems.
Decis. Sci. 1980, 11, 616–631. [Cross Ref]
33.
Bonczek, R.H.; Holsapple, C.W.; Whinston, A.B. Foundation of Decision Support Systems; Academic Press:
New York, NY, USA, 1981.
34.
Burstein, F.; Holsapple, C. Handbook on Decision Support Systems 1. In International Handbooks on Information
Systems; Springer: Berlin/Heidelberg, Germany, 2008.
35.
Online Database for Wind Production. Available online: http://www.energinet.dk/en/el/engrosmarked/
udtraek-af-markedsdata/Sider/default.aspx (accessed on 6 October 2016).
© 2017 by the authors; licensee MDPI, Basel, Switzerland. This article is an open access
article distributed under the terms and conditions of the Creative Commons Attribution
(CC-BY) license (http://creativecommons.org/licenses/by/4.0/).

---
