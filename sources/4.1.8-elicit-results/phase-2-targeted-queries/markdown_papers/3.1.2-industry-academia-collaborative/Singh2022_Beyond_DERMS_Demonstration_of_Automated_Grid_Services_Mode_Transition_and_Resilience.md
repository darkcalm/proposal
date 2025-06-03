# Singh2022 Beyond DERMS  Demonstration of Automated Grid Services, Mode Transition, and Resilience

## Paper Metadata

- **Filename:** Singh2022_Beyond_DERMS__Demonstration_of_Automated_Grid_Services,_Mode_Transition,_and_Resilience_DOI_10-2172_1862821.pdf
- **DOI:** 10.2172/1862821
- **Authors:** Not available
- **Year:** Not available
- **Journal/Venue:** Not available
- **URL:** Not available
- **Extraction Date:** 2025-06-03T15:04:04.039325
- **Total Pages:** 36

## Abstract

Abstract not available from BibTeX metadata.

## Keywords

Keywords not available from BibTeX metadata.

---

## Full Text Content



### Page 5

iii 
CONTENTS 
ACRONYMS .................................................................................................................................. v 
ACKNOWLEDGMENTS ............................................................................................................. vi 
EXECUTIVE SUMMARY .......................................................................................................... vii 
1 
INTRODUCTION ................................................................................................................... 1 
2 
REVIEW OF BEYOND DERMS PLATFORM ARCHITECTURE 
AND UTILITY INTEGRATION............................................................................................ 3 
 
Platform Elements .......................................................................................................... 3 
 
Grid Services .................................................................................................................. 4 
 
Connecting Utility Services and DERs .......................................................................... 4 
 
Power Flow Modeling .................................................................................................... 6 
 
Time Series Simulation .................................................................................................. 6 
 
DER Modeling ............................................................................................................... 6 
 
Device Integration .......................................................................................................... 7 
3 
ADVANCED USE CASES: GRID SERVICES FOR DER OPERATIONS 
AND VALIDATION............................................................................................................... 8 
 
Ancillary Services (Frequency Regulation) ................................................................... 9 
 Frequency Regulation Concept .......................................................................... 9 
 Using the Beyond DERMS Platform for Ancillary Services ........................... 10 
 Experimental Setup and Results ....................................................................... 10 
 Consideration of Stored Energy in DERS for Ancillary Services .................... 13 
 
Automatically Transitioning among Operating Modes ................................................ 14 
 Motivating Scenarios ........................................................................................ 14 
 Process for Automated Mode Switching .......................................................... 15 
 
Black-sky-day Operation .............................................................................................. 16 
 Grid-interactive Battery Demonstration Results .............................................. 17 
 Local Resilience (Off-grid) Mode Battery Demonstration Results.................. 19 
 Other Grid Services .......................................................................................... 20 
4 
CONCLUSION AND FUTURE WORK .............................................................................. 21 
 
Conclusions .................................................................................................................. 21 
 
Gaps and Future Work ................................................................................................. 21 
 Distribution Network Simulator ....................................................................... 21 
 Large-Scale Deployment .................................................................................. 22 
 Network Constraint and Congestion Management .......................................... 22 
 Cybersecurity.................................................................................................... 23

---


### Page 6

iv 
FIGURES 
1 
The three key elements required for a fully functional DERMS, as implemented in the 
Beyond DERMS platform, that connects grid operators, DER owners, and their devices. .....4 
2 
Utility interconnection architecture. .........................................................................................5 
3 
Cloud and Io T architecture. ......................................................................................................5 
4 
An illustration of the overall control architecture for DER coordination within the 
“Beyond DERMS” platform.....................................................................................................9 
5 
An illustration of a virtual power plant (VPP) bidding its frequency regulation capacity 
into a market, and then adjusting its net power consumption to track with an AGC 
signal.......................................................................................................................................10 
6 
Results from Frequency Regulation Trial 1. The upper panel shows the target setpoint 
and the actual power. The lower two panels show elements of the PJM score and the 
number of “energy packets” delivered in each time period. ..................................................11 
7 
Results from Frequency Regulation Trial 2 in which the target setpoint was scaled 
down to an average of about 60k W, which was still significantly higher than the 
average water heater load. This trial resulted in a composite PJM performance score of 
0.78. ........................................................................................................................................12 
8 
Results from Frequency Regulation Trial 3 in which the target setpoint was scaled 
down to an average of about 50k W. This trial resulted in a composite PJM performance 
score of 0.90. ..........................................................................................................................13 
9 
Stored energy from Trial 3. The top panel shows the actual and target power timeseries 
(as in Figure 8). The lower panel shows the total amount of stored energy in the fleet of 
DERs.......................................................................................................................................14 
10 A screenshot from the Beyond DERMS platform showing the results of peak load 
probability forecasting. In the platform these probabilities were used to auto-schedule 
peak events, thus automatically transitioning from load shaping mode to peak reduction 
mode. ......................................................................................................................................16 
11 The residential-scale battery system and inverter used for this “Black Sky” 
demonstration. ........................................................................................................................18 
12 The power and current (upper panel) and state of charge (lower panel) for tests initiated 
by remote commands from the DERMS. ...............................................................................19 
13 Battery behavior during blackout scenario with EV charger. ................................................20

---


### Page 7

v 
ACRONYMS 
ACE 
Area Control Error 
AGC 
Automatic Generation Control 
ARPA-E 
Advanced Research Projects Agency — Energy 
 
BED 
Burlington Electric Department 
BTM 
behind the meter 
 
DER 
distributed energy resource 
DERMS 
distributed energy resource management systems 
DOE 
U.S. Department of Energy 
 
EV 
electric vehicle 
EVSE 
electric vehicle supply equipment 
 
FERC 
Federal Energy Regulatory Commission 
 
GIS 
geographic information systems 
 
HVAC 
heat, ventilation and air conditioning 
 
Io T 
internet of things 
ISO 
independent system operator 
 
NODES 
Network Optimized Distributed Energy Systems 
 
OE 
Office of Electricity 
 
PEM 
Packetized Energy Management 
 
Qo S 
quality of service 
 
R&D 
research and development 
RTO 
regional transmission organization 
 
So C 
state of charge 
VB 
virtual battery 
VEC 
Vermont Electric Cooperative 
VPP 
virtual power plant 
 
.

---


### Page 8

vi 
ACKNOWLEDGMENTS 
 
This report was prepared by UChicago Argonne, LLC, operator of Argonne National 
Laboratory. Argonne’s work was supported by the U.S. Department of Energy (DOE) under 
contract DE-AC02-06CH11357. 
 
The authors wish to acknowledge the sponsorship and guidance provided by Dan Ton, 
Office of Electricity, DOE. 
 
We would also like to extend our special appreciation to Matthew Sessions (Packetized 
Energy), Jeff Frolik (Packetized Energy), Mads Almassalkhi (Packetized Energy), Seth 
Maciejowski (Packetized Energy), Jason Shafer (Northview Weather), Kevin Cronin (Northview 
Weather), and Mark Ehler (Northview Weather) for their contributions.

---


### Page 9

vii 
EXECUTIVE SUMMARY 
 
This report describes the results of the Beyond DERMS project aiming to build, deploy, 
and demonstrate a holistic platform that supports the integrated operation and planning of future 
power distribution networks with bi-directional power flows, many diverse distributed energy 
resources (DERs), and inverter-based resources. The results demonstrate how emerging ‘internet 
of energy’ technologies can be leveraged to simultaneously solve the grid problems of today and 
prepare for the challenges of tomorrow in a way that goes beyond the capabilities of existing 
distributed energy resource management systems (DERMS). 
 
The Beyond DERMS platform used in this project was developed from a study of the 
performance of over 300 smart energy devices, thousands of simulated devices, and data from 
over 20,000 smart meters connected on the distribution networks of two utility partners, Vermont 
Electric Cooperative (VEC) and Burlington Electric Department (BED). These devices and data 
streams were used to test various functions on this single platform. The results clearly showed 
that the core “Beyond DERMS” concepts are feasible and motivate the need for a large-scale 
demonstration project to demonstrate how DERMS fits with other key elements of grid 
modernization that include Advanced Metering Infrastructure, DER and aggregations applying 
microgrid concepts. 
 
The project was organized in three phases: 1) conceptualization, 2) platform development 
and 3) advanced use cases. The accomplishments of each phase are summarized below. 
Phase 1 (Conceptualization) 
1. Development of the core Beyond DERMS concepts and a DERMS platform for 
integration testing with 300 behind-the-meter (BTM) DERs including water heaters, 
electric vehicles (EVs), and batteries. 
2. Initial system integration tests and simulations of the DERMS platform, in cooperation 
with utility partner(s). 
3. Demonstration of the core Beyond DERMS concepts, such as integrating planning 
functions within the DERMS, and the capability to deliver grid services for the following: 
• Peak load reduction to mitigate generation and transmission capacity costs. 
• Load shaping (i.e., energy arbitrage) to reduce the cost of wholesale energy purchases 
needed to supply time-varying loads. 
• Distribution network management services through a software system that can model 
and manage distribution network constraints in real time. 
• Ancillary services for balancing authorities, independent system operator (ISO), or 
regional transmission organization (RTO). 
• Resilience for consumers and for the grid as a whole.

---


### Page 10

viii 
Phase 2 (Platform Development) 
1. Integration of weather, load, and DER forecasting and integration of economic analysis 
tools into the Beyond DERMS platform. 
2. Demonstration of how the platform can go beyond conventional DERMS to include grid 
planning functions that allow electric utilities to plan for and manage DERs on a single 
platform. 
3. Demonstration of the capability of a wider range of DERs to provide flexible grid 
services by integrating weather, load, and DER forecasting and by integrating economic 
analysis tools that facilitate DER project planning. 
Phase 3 (Advanced Use Cases) 
Phase 3 demonstrated more advanced use cases including Ancillary Services and Black-sky-day 
operation and Mode Switching) using the Beyond DERMS platform. Phase 3 tests showed how 
groups of DERs can provide a range of grid services, such as: 
• Peak load management. 
• Load shaping for energy price (LMP) arbitrage. 
• Distribution network management (in simulation). 
• Ancillary services (in simulation). 
 
These tests demonstrated how a Beyond DERMS platform can fuse together AMI, 
SCADA, and DER data to provide a utility with deep insights into distribution network 
operations and planning, extending the value of DERMS and BTM DER resources. 
 
These grid services apply to use cases for ancillary services, black-sky-day operations, 
and Mode Switching. The advanced use cases validate the grid services provided by the Beyond 
DERMS platform, that integrates DER management with distribution network planning and 
forecasting functions.

---


### Page 11

1 
1 INTRODUCTION 
 
Distributed renewable generation, energy storage, and smart energy appliances are 
increasingly prevalent behind the meter (BTM) in residential and commercial buildings. As the 
result of years of DOE R&D, microgrid technology for locally managing DERs to provide 
building-level resilience and to reduce energy costs is well-established. Similarly, the technology 
for basic demand response (reducing load during peak periods through direct load control or by 
adjusting thermostat setpoints) is operational in utilities and markets. Demand response programs 
and time-of-use electric rates continue to drive the adoption of DERs, including home batteries. 
However, neither basic demand response nor microgrids can address emerging grid impacts, 
such as managing constraints in distribution networks with bi-directional power flow patterns 
and providing real-time grid balancing services to balancing authorities. Thus, there is a need for 
technology that can coordinate millions of DERs to solve problems both within distribution 
networks and for the bulk power system. 
 
Distributed Energy Resource Management Systems (DERMS) have the potential to 
address this need but many of the core ideas that underlie the DERMS concept―such as 
simultaneously providing grid services for the bulk grid and for the distribution network―have 
not been demonstrated with large numbers of installed diverse devices. 
 
The potential for DERs to contribute to grid balancing services is well-recognized, most 
notably in Federal Energy Regulatory Commission (FERC) Order No. 2222.1 The 
implementation of FERC 2222 has the potential to dramatically change the U.S. electricity 
industry by opening up new business models that allow distributed energy resources to compete 
with centralized grid assets in markets.2 However, for electric utilities that need to maintain 
aging transmission and distribution network infrastructure, it is not clear how they can coordinate 
the actions of thousands of DERs controlled by many different aggregators, each managing 
overlapping groups of diverse assets that connect on both low- and medium-voltage distribution 
networks. Operating distribution circuits in this new environment requires innovative 
modifications for emerging algorithms for DER coordination. These innovative approaches 
advance earlier research and development (R&D) that focused on microgrids and Distributed 
Energy Resource Management Systems (DERMS). 
 
The U.S. Department of Energy (DOE) has sponsored a wide range of research, 
development, and demonstration efforts that have moved many distribution-level smart grid 
technologies forward. The 2009 American Recovery and Reinvestment Act Smart Grid 
Investment Grant program accelerated the adoption of advanced metering and other smart grid 
infrastructure. The DOE’s Office of Electricity’s (DOE/OE) Grid Modernization Initiative and 
Microgrid Program have led to significant advances in microgrid controls (energy management 
systems), DERMS, distribution system modeling software, associated control algorithms, and 
 
1 FERC Order No. 2222, Participation of Distributed Energy Resource Aggregations in Markets Operated by 
Regional Transmission Organizations and Independent System Operators (Issued September 17, 2020). 
2 P. Hines and A. B. Wannop, “FERC Order 2222 should be a watershed moment — Grid operators can help 
ensure that,” Utility Dive. (November 2020).

---


### Page 12

2 
industry standards.3 The Advanced Research Projects Agency—Energy’s (ARPA-E) Network 
Optimized Distributed Energy Systems (NODES) program began the development of algorithms 
required for aggregated DERs to solve a range of real-time grid problems. But what is not yet 
clear is how best to integrate these various technologies to address the range of problems faced 
by the electricity industry today and to help them plan for the challenges of tomorrow. 
 
Furthermore, integrated DER management systems have not been effectively 
demonstrated at scale with thousands of devices and more than 1 MW of aggregated capacity. 

3 IEEE 2030.7™ Standard for Specification of Microgrid Controllers and IEEE 2030.11™ Guide for Distributed 
Energy Management Systems.

---


### Page 13

3 
2 REVIEW OF BEYOND DERMS PLATFORM ARCHITECTURE 
AND UTILITY INTEGRATION 
 
This section revisits the architecture and components of Beyond DERMS Platform. A 
detailed description of these components is available in the Beyond DERMS Phase 1 and 2 
report.4 
 PLATFORM ELEMENTS 
 
The developed Beyond DERMS platform implements three key functions: 
1. Utility Dashboard: Provide utilities and other grid operators with the ability to manage 
DERs. The platform described here is specifically designed to provide four types of grid 
services: peak reduction services to minimize load during event periods; load shaping 
such that DERs track with a desired daily load shape or with marginal generation costs; 
ancillary services, such as frequency regulation or spinning reserves; and automated 
distribution network management functions for both planning and operations. 
2. Customer Interface: Provide DER owners (e.g., home or business owners) with the 
ability to connect their DERs and manage how those devices interact with the grid. In this 
project, we used a custom-designed mobile app to meet this requirement. 
3. Internet of Things (Io T) Interconnections: Provide the backend Io T technology needed 
to coordinate the behavior of millions of devices. This project uses Packetized Energy 
Management (PEM) as the foundation for this Io T system. 
 
Figure 1 illustrates how these three elements come together in the platform. The 
dashboard provides grid operators with the ability to visualize and manage how DERs operate to 
provide grid services. The mobile app provides end users with the ability to change how their 
devices interact with the DERMS. Finally, the backend Io T platform allows devices to interact 
with the platform in real time, using the core PEM technology. 
 
4 https://www.osti.gov/biblio/1825329-beyond-derms-platform-development-flexibility-prediction-valuemeasurements.

---


### Page 14

4 
 
FIGURE 1 The three key elements required for a fully functional DERMS, as 
implemented in the Beyond DERMS platform, that connects grid operators, DER 
owners, and their devices. 
 GRID SERVICES 
 
The Beyond DERMS platform aims to operate across historical, operations, and planning 
time scales, while also providing the ability to coordinate DERs for five different grid services: 
1. Peak load reduction 
2. Load shaping 
3. Ancillary services 
4. Distribution network management 
5. Resilience 
 CONNECTING UTILITY SERVICES AND DERS 
 
We connected AMI, SCADA, micro PMUs, and engineering network model data into the 
platform by developing a local “data agent,” which locally communicated with the utility data 
systems and then securely transferred data to the cloud-based DERMS. This architecture is 
shown in Figure 2.

---


### Page 15

5 
 
FIGURE 2 Utility interconnection architecture. 
 
The Beyond DERMS platform uses a modern “serverless” cloud software architecture 
hosted on Amazon Web Services. Figure 3 describes the overall architecture of the software. 
This serverless architecture allows us to write code that responds to specific events (such as a 
device requesting a “packet” of energy) without needing to also manage the computer servers 
that run the code. This asynchronous design aligns well with the asynchronous nature of our core 
software algorithms, which are designed to be “device driven,” rather than a more conventional 
top-down optimization approach in which data is collected from devices, centrally optimized, 
and then centrally dispatched. Instead, our algorithms respond to requests from devices to 
consume (or produce) “packets” of energy. In the serverless approach, each message from a 
device (Io T message) triggers a set of code, which subsequently runs the appropriate 
calculations, records data in the databases, and responds to devices based on grid conditions. 
 
FIGURE 3 Cloud and Io T architecture.

---


### Page 16

6 
 
In this project, we were able to successfully implement the software architecture shown 
in figures 2 and 3, integrating with the partner utility’s (Vermont Electric Cooperative, VEC) 
meter data management system, geographic information systems (GIS), SCADA, and power 
flow data. Using this architecture, we built a software module known as Grid Solver, which 
allows the utility to visualize historical data for various assets within their network. 
 POWER FLOW MODELING 
 
In order to integrate a power flow model into the platform, we used a Docker container 
(similar to a virtual machine), which includes the actual Grid Lab-D simulation engine, following 
the method developed by Chassin et al at SLAC National Accelerator Laboratory.5 We 
subsequently built a scenario analysis tool into Grid Solver, which allows us to run quasi-steadystate power flow simulations within the platform, based on historical utility AMI data, which are 
fed into the Docker container within our cloud software. We tested this power flow modeling 
tool using both the IEEE 123 bus test case and a full set of distribution circuits provided by our 
utility partner VEC. 
 TIME SERIES SIMULATION 
 
In order to develop a time-series simulation of the IEEE 123 node test case within 
Grid Solver, we added anonymized time-series data collected from the utility-provided AMI data 
to each load (or house) in the original network model. This provides us the ability to run the base 
case, as well as time-series (quasi steady-state time-series, QSTS) simulations. 
 DER MODELING 
 
The next subtask was to model DERs within the platform, so that we could simulate the 
behavior of different types of devices as they were added to the system. In particular, we focused 
on the development of models of the following device types: 
• Level 2 electric vehicle supply equipment (EVSEs). 
• Grid interactive water heaters. 
• Grid-edge (residential scale) battery systems. 
• Rooftop PV systems. 
• HVAC systems (particularly with heat pumps). 
 
5 D. Chassin, V. Lubeck, and A. Teyber, “Stanford/SLAC development version of Grid LAB-D,” from SLAC 
National Accelerator Laboratory. https://github.com/slacgismo/gridlabd.

---


### Page 17

7 
 DEVICE INTEGRATION 
 
In order to perform integration testing for various DERs and grid services, we connected 
over 350 DERs in partnership with our two utility partners, VEC and BED. This fleet of DERs 
includes the following set of devices: 
• Electric hot water heaters using the Mello smart thermostat for water heaters (∼300 
units). 
• Level 2 EVSEs, primarily using the Turbo DX from Webasto (∼40 units). 
• Mini-split heat pumps (∼5 units). 
• BTM batteries and PV inverters (∼10 units). 
• Rooftop PV systems. 
• Heat, ventilation, and air conditioning (HVAC) systems (particularly with heat pumps).

---


### Page 18

8 
3 ADVANCED USE CASES: GRID SERVICES FOR DER OPERATIONS 
AND VALIDATION 
In this project, we focused on developing algorithms for each of five different DER use cases. 
1. Peak reduction, to mitigate costs associated with generation and capacity (i.e., resource 
adequacy). 
2. Energy arbitrage, to reduce energy costs by shifting load from high-cost periods to lowcost periods. 
3. Ancillary services, such as frequency regulation — reducing the need to use conventional 
resources, like gas turbines — to provide real-time grid balancing. 
4. Distribution network constraint management, in which DERs are coordinated to ensure 
that distribution network voltages and currents remain within limits, thus providing nonwires alternatives to conventional distribution network upgrades. 
5. Resilience, in which DERs react to local conditions to help users recover from bulk grid 
outages (e.g., with the help of solar power and batteries) or to support the resilience of the 
bulk grid by locally reacting to voltage and frequency deviations. 
 
While some of the use cases have been demonstrated in previous reports, the remainder 
of this section describes the algorithms used to implement advanced used cases related to mode 
transition, ancillary services such as frequency regulation, and black-sky-day operations. 
 
The underlying technology used in this project for coordinating distributed energy 
resources is known as Packetized Energy Management.6 In this system, devices make 
randomized requests for “packets” of energy (an amount of energy consumed over a fixed period 
of time) to a coordinator who accepts or denies requests based on the real-time energy 
consumption level, relative to a target. The target (“Optimized power reference” in Figure 4) is 
chosen via an optimization routine that can consider a wide range of different factors, including 
the price of energy, carbon emissions levels, renewable generation, or grid constraints. Feedback 
from the coordinator allows the optimization engine to adjust the optimization formulation and 
thus the target setpoint for the aggregation of DERs (the virtual battery, or VB). The result is the 
ability to coordinate a fleet of diverse DERs as if they were a conventional power grid asset, such 
as a battery or a flexible power plant. 
 
6 [ref to IEEE Spectrum Article] https://spectrum.ieee.org/packetized-power-grid.

---


### Page 19

9 
 
FIGURE 4 An illustration of the overall control architecture for DER coordination within the 
“Beyond DERMS” platform. 
 ANCILLARY SERVICES (FREQUENCY REGULATION) 
 
As variable energy resources such as wind and solar increase, an even greater need arises 
for real-time balancing resources that can rapidly respond to changes in both supply and demand. 
In most modern power systems, this real-time balancing comes largely from primary, secondary, 
and tertiary frequency reserves. When performing primary frequency regulation, a generator 
adjusts its active power in response to changes in the frequency of the locally measured AC 
voltage. For secondary frequency regulation (also known as Automatic Generation Control, or 
AGC), a generator adjusts its power output in response to a signal sent by the regional balancing 
authority every 2-6 seconds. This signal, known as Area Control Error (ACE), is based on a 
combination of the deviation between scheduled and actual power exports/inputs and the 
regionally measured voltage frequency. Finally, for tertiary reserves (also known as contingency 
reserves), a generator agrees to rapidly increase its output in response to an unexpected loss of 
some other power generation resource. 
 
FERC Order No. 2222 opens up the potential for aggregated demand-side resources that 
have an aggregate capacity of at least 100k W to provide ancillary services into wholesale 
electricity markets. The ruling makes it difficult for utilities to “block” the participation of DERs 
in ancillary service markets so long as they meet regional telemetry and other requirements. 
 Frequency Regulation Concept 
 
Motivated by both the increasing need for balancing resources and changes in market 
rules, this project leveraged the “Beyond DERMS” platform to test the potential for a group of 
aggregated devices (a virtual power plant, or VPP) to provide secondary frequency regulation 
services. Specifically, this portion of the project demonstrate that an aggregated group of DERs 
can provide secondary frequency regulation by rapidly adjusting the aggregated power

---


### Page 20

10 
consumption in response to an AGC signal. Figure 5 illustrates the overall concept of a VPP 
bidding into the market with a “frequency regulation bid,” then receiving an AGC signal from 
the ISO, and then adjusting net power consumption to match this signal. 
 
FIGURE 5 An illustration of a virtual power plant (VPP) bidding its frequency regulation capacity 
into a market, and then adjusting its net power consumption to track with an AGC signal. 
 Using the Beyond DERMS Platform for Ancillary Services 
 
In order to test the ability of the platform to perform ancillary services, we run several 
tests in which about 250 distributed energy resources (primarily water heaters) were connected to 
the platform and used for secondary frequency regulation. Specifically, we tested the ability of 
the group of devices to track with a “Reg-D” test signal from PJM.7 This signal was then scaled 
to produce a signal that the fleet of devices could track (see experiments in the next section). 
 Experimental Setup and Results 
 
This section shows the results from several trials in which we tested the ability of the 
platform to deliver secondary frequency regulation services per the PJM Reg-D test signal. Each 
trial lasted about 40 minutes and used the same test signal. Trials differed in the time of day, and 
in location of the tracking signal, relative to the baseline load. 
 
In each trial we measure performance using the three elements of the PJM frequency 
regulation performance scoring: accuracy, delay, and precision. Accuracy is a measure of 
correlation between the signals. The Delay score is based on the amount of delay between the 
 
7 https://www.pjm.com/markets-and-operations/ancillary-services.

---


### Page 21

11 
target and actual signals, and the Precision score is based on the actual amount of error between 
the target and actual. Each trial includes 208 online and connected devices. 
 
Trial 1 (Figure 6) was a test trial in which the target power level was set quite high, 
relative to the actual baseline load. As would be expected, this trial resulted in a low precision 
score (0.11). The accuracy and delay scores were 0.70 and 0.81, respectively, leading to an 
overall score of 0.54. 
 
FIGURE 6 Results from Frequency Regulation Trial 1. The upper panel shows the target setpoint 
and the actual power. The lower two panels show elements of the PJM score and the number of 
“energy packets” delivered in each time period. 
 
In Trial 2 (Figure 7) we scaled down the relative position of the setpoint, but not far 
enough to fully allow the load to track with the target signal. In this case, the Accuracy score 
increased to 0.87, Delay to 0.96, Precision to 0.50, and the overall composite score was 0.78.

---


### Page 22

12 
 
FIGURE 7 Results from Frequency Regulation Trial 2 in which the target setpoint was scaled down 
to an average of about 60k W, which was still significantly higher than the average water heater 
load. This trial resulted in a composite PJM performance score of 0.78. 
 
In the final “Trial 3” (Figure 8), we further scaled down the target setpoint to about 50k W, 
substantially increasing the overall performance scores. This case had an Accuracy score of 0.95, 
Delay of 0.99, Precision of 0.77, and Composite of 0.90. This score is on par with or exceeds the 
overall performance scores commonly achieved by natural gas power plants, which suggests that 
it is indeed possible for aggregated DERs to provide frequency regulation services to the grid.

---


### Page 23

13 
 
FIGURE 8 Results from Frequency Regulation Trial 3 in which the target setpoint was scaled down 
to an average of about 50k W. This trial resulted in a composite PJM performance score of 0.90. 
 Consideration of Stored Energy in DERS for Ancillary Services 
 
Flexible load devices typically have some ability to shift the time at which they pull 
energy from the grid and “store” energy. Water heaters, refrigeration systems, and buildings 
store energy in thermal format. EVs and BTM batteries store energy chemically and pool pumps 
have a daily minimum run time that can be shifted through the day. Understanding how much 
stored energy exists in a fleet of devices is a useful parameter in DER scheduling in order to 
provide ancillary services. 
 
In order to understand this stored energy, we used the data from Trial 3 and measured the 
aggregated amount of stored energy in the fleet but adding up the effective stored energy in each 
DER (primarily water heaters). For a water heater, devices that are 10 degrees F above their 
setpoint are considered to be at 100% “state of charge” (So C), and devices that are 10 degrees 
below their setpoint are considered to be at 0% So C. 
 
Figure 9 shows the resulting state of charge for our fleet of devices. Clearly, over the 
40 minutes of this trial the total amount of stored energy decreases due to the fact that the target 
load level is held below the average/baseline for a significant portion of the time. In the final 
15 minutes of the trial, stored energy increases again (as the overall load level is higher). This 
trial shows that it is feasible to monitor stored energy in a fleet of DERs modeled as a virtual 
battery.

---


### Page 24

14 
 
FIGURE 9 Stored energy from Trial 3. The top panel shows the actual and target power timeseries 
(as in Figure 8). The lower panel shows the total amount of stored energy in the fleet of DERs. 
 AUTOMATICALLY TRANSITIONING AMONG OPERATING MODES 
 
This use case demonstrates the ability of Beyond DERMS to automatically switch 
between operating modes based on grid and market conditions. This use case demonstrates the 
algorithms for optimally switching in and out of ancillary service markets. In this use case, we 
optimize DER scheduling among ancillary services, peak reduction, and energy arbitrage. 
Performing this optimization requires bidding into wholesale ancillary service markets, which 
are only just now beginning to open up for BTM DER participation. 
 
To enable VBs so that they automatically detect the right time to transition from one 
operating mode to another, we used relatively simple rules. Under this system, DERs are 
scheduled to perform energy arbitrage when no peak events have been scheduled and when no 
network constraints are binding. When a distribution network constraint is binding, the DERs 
“behind” that constraint automatically switch to a constraint management mode under which 
they cease to perform services for the bulk grid and focus exclusively on ensuring that voltage 
and current limits are not violated. Similarly, DERs operate in arbitrage mode until they 
approach the pre-positioning period for a peak event, at which point they transition into peak 
management mode. Once the peak event has concluded or the constraint is no longer binding, the 
DERs return to focusing on their default load shaping grid service. 
 Motivating Scenarios 
 
Under normal operating conditions when distribution network constraints are not binding, 
DERs can easily be set to provide services into wholesale electricity markets, such as load 
shifting for energy arbitrage or ancillary services. However, in the event of a need for peak

---


### Page 25

15 
reduction or constraint management, DERs must switch operating modes to satisfy system 
constraints. 
 
In all cases, it is important to manage DERs to honor customer quality of service (Qo S) 
limits. Under normal conditions DERs need to strictly adhere to these constraints. 
 
In the Beyond DERMS platform DERs typically default to an energy arbitrage mode 
under normal conditions when constraints are not binding. The question is, how can we 
automatically enable DERs to switch to one of the other modes when it is advantageous or 
necessary to do so, without requiring unnecessary complexity in the control algorithms. 
 
Here we look specifically at the case of automatically detecting “high-cost windows” and 
triggering a switch to peak reduction mode when these windows occur. For this use case, we 
define a “high-cost window” as a period of time when there is a very high probability that this 
particular hour is the peak hour of the month, which is when utilities in the region are assessed 
transmission fees based on their contribution to the peak monthly load. During these high-cost 
windows, it is optimal to transition from the relatively mild load shaping algorithm to an 
aggressive peak reduction mode. 
 
A key element of the project was enabling customers to stay informed of peak events 
through the mobile application associated with the platform. We have found that by allowing 
customers to be informed of events, the impact of peak reduction events has less negative impact 
on customers’ experienced quality of service. Thus, as an element of enabling automatic mode 
switching, we developed the ability for the DERMS platform to send peak event notifications to 
the associated phone application. 
 Process for Automated Mode Switching 
 
In order to enable mode switching between the energy arbitrage and peak reduction 
modes we employed the following process: 
1. Forecast circuit-level and regional net load over a ~72-hour horizon. 
2. Compute the probability of binding network constraints or expensive peak load events. 
3. If probability is low: 
• Continue to perform economic grid services within customer Qo S limits (ancillary 
services or load shaping for energy arbitrage). 
4. If probability is high: 
• Execute peak load management. 
a. Notify customers. 
b. Pre-position. 
c. Minimize load with (somewhat) relaxed Qo S limits. 
d. Recovery.

---


### Page 26

16 
 
The precise methods used for peak load probability estimation were described in a prior 
report. Figure 10 shows results from the peak load forecasting tool through which the automatic 
transition into peak reduction mode was enabled. 
 
FIGURE 10 A screenshot from the Beyond DERMS platform showing the results of peak load 
probability forecasting. In the platform these probabilities were used to auto-schedule peak events, 
thus automatically transitioning from load shaping mode to peak reduction mode. 
 BLACK-SKY-DAY OPERATION 
 
Distributed Energy Resources have the potential to generate a wide range of benefits 
including grid services for utilities and balancing authorities/ISOs and financial savings for 
consumers. However, many have noted that DERs also have the potential to make both the grid 
as a whole, and individual customer locations more resilient to bulk grid outages. This section 
reviews how a DERMS can facilitate both system and local resilience and presents illustrative 
testing results from a small-scale demonstration with a residential battery system. 
 
Grid-connected batteries are one of the most promising technologies for enabling 
resilience from DERs. Home battery systems like the Tesla Powerwall are becoming 
increasingly popular among consumers with rooftop PV systems. And community-scale battery 
systems, when paired (for example) with community solar, are increasingly being adopted in 
order to enable community microgrids that can enable limited resilience functionality, such as 
powering a school or a hospital for a period of time if the bulk grid fails.

---


### Page 27

17 
 
In order to deliver resilience to the grid as a whole, a system is needed in which DERs 
have “good reflexes,” such that they can respond to both local and regional grid problems. 
 
With respect to regional grid problems, the frequency regulation results described in 
Section 3.1 demonstrate that it is possible for DERs to react quickly (in seconds) to a balancing 
signal from the bulk grid. With this capability in place, it would be possible for grid operators, 
for example, to send an emergency ramping signal to a fleet of DERs in order to rapidly reduce 
load or generation when the risk of a cascading failure is high, thus mitigating blackout risk. 
 
Similarly results previously presented in this project show that it is possible for DERs to 
sense locally measured voltage and frequency and adjust their power output accordingly.8 With 
this capability, DERs can react to local conditions, enabling behaviors that can increase grid 
resilience. 
 
Finally, in particular for battery systems combined with solar PV, DERs can provide 
local resilience by enabling backup power systems that can continue for long periods of time, 
even if the build grid is unable to provide reliable power. 
 
DERMS platforms have the potential to coordinate these core behaviors, thus enabling 
both local and regional energy system resilience. 
 Grid-interactive Battery Demonstration Results 
 
In order to demonstrate that residential-scale batteries can respond quickly to signals 
from a DERMS when grid-connected, we developed a demonstration using a home battery 
system connected to a residential-scale inverter, as shown in Figure 11. This system was 
connected to the Beyond DERMS platform using a small Wi-Fi-enabled microcontroller that 
communicated with the inverter via the MODBUS protocol. 
 
8 https://www.osti.gov/biblio/1825329-beyond-derms-platform-development-flexibility-prediction-valuemeasurements.

---


### Page 28

18 

FIGURE 11 The residential-scale battery system and inverter used for this “Black Sky” 
demonstration. 
 
In order to demonstrate that batteries can participate in remotely initiated grid services 
managed by the DERMS, we performed a simple test in which the DERMS sent a message to the 
battery controller to initiate a discharge event and then a subsequent charge event. The results in 
Figure 12 show that this type of remote management is indeed feasible.

---


### Page 29

19 
 
FIGURE 12 The power and current (upper panel) and state of charge (lower panel) for 
tests initiated by remote commands from the DERMS. 
 Local Resilience (Off-grid) Mode Battery Demonstration Results 
 
In order to demonstrate the potential for off-grid operations from a residential battery 
system, we used the DERMS to initially configure the battery so that it would supply local loads 
in the case of a grid outage. In this grid-forming mode when voltage from the grid is not 
measured, the inverter sets the battery to discharge current to supply a local load (an EV 
charging station, in this case).

---


### Page 30

20 
 
Figure 13 shows results from a test of this functionality for the battery setup shown in 
Figure 12. As shown, when the grid is disconnected, the battery switches to supplying current to 
the local load. After the grid reconnects, the battery charges in order to recover its state of charge 
to the nominal level. 
 
FIGURE 13 Battery behavior during blackout scenario with EV charger. 
 Other Grid Services 
 
The existing Beyond DERMS platform can be used for other grid services and markets 
including 
• Resilience & black start, in which DERs react to local conditions to help users to recover 
from bulk grid outages (e.g., with the help of solar and batteries) or to support the 
resilience of the bulk grid by locally reacting to voltage and frequency deviations. 
• Ramping, in which DERs may be responsible for providing ramping patterns and 
parameters at regular intervals during the operating day, with Beyond DERMS platform 
determining a unified optimal ramping capability and ramp rate limits with or without 
storage. 
• Capacity Services: Instead of relying only on the nameplate capacity information of the 
distributed PVs, information about the PV generation under different sun-tracking 
capabilities can be more useful for accurately estimating the PV capacities. It is important 
for Beyond DERMS platform to determine the optimal size of combinations of different 
DERs (e.g., storage + PV, storage + flexible load, etc.) to achieve target MW capacity 
with a certain guarantee.

---


### Page 31

21 
4 CONCLUSION AND FUTURE WORK 
 CONCLUSIONS 
 
This report on the Beyond DERMS Phase 3 project demonstrates how the Beyond 
DERMS platform developed in phases 1 and 2 can be leveraged to support a portfolio of grid 
services based on findings from a small-scale demonstration. In particular, the report describes 
use cases for enhanced peak management, load shaping, and energy arbitrage along with 
automated provision of ancillary services to the ISO/RTO (i.e., frequency regulation) using PJM 
price signals. 
 
The report describes the resilient operation of the Beyond DERMS platform under 
abnormal grid conditions by dispatching existing storage assets to supply power to the local 
loads. This demonstrated the automatic mode switching capability of the platform in response to 
grid conditions (i.e., black-sky-day operation) and market conditions. In the transition mode 
scenario, DERs can transition from providing grid services to the bulk grid to a resilience mode 
to support local customer reliability and resilience. 
 
The performance of each grid service is measured in terms of flexible capacity offered 
per device and for the portfolio as a whole. This report identifies the extent to which different 
device types can provide different types of grid services; specifically, how much flexible 
capacity can be delivered for an average device, and for how long. This characterization allows 
us to build an equivalent “virtual battery” model for a fleet of devices in each category, or for a 
combination of devices. The model characterizes how flexible capacity changes with season, 
temperature, and customer quality of service limits. 
 GAPS AND FUTURE WORK 
 Distribution Network Simulator 
 
Distribution network simulation and optimization models are key elements of advanced 
DERMS software. Open-source software systems (such as Grid Lab-D, which was used in this 
project) can be valuable elements of a DERMS. However, we found a number of limitations in 
Grid Lab-D that we think could be addressed by migrating to a more advanced power flow tool 
such as the “Power Models Distribution” tool developed by Los Alamos National Laboratory.9 
Furthermore, new approaches to distribution network simulation and modeling are needed. We 
hope this need will be addressed in a future large-scale demonstration project. 
 
9 The tool incorporates modern methods of optimization-based response and controls to reduce the scalability and 
convergence challenges that are often faced by simulation, in particular those seen when combining distribution 
and transmission level modeling.

---


### Page 32

22 
 Large-Scale Deployment 
 
It is important to evaluate the ability of DER management platforms to perform grid 
services at the MW scale. While the results described in this report are promising, they represent 
a fairly limited scale and such tests are often viewed cautiously within the U.S. electricity 
industry. Larger-scale tests often reveal new challenges and opportunities for innovation. 
Further, results from large-scale demonstrations are often necessary to support tech-to-market 
transitions. The work completed in this project provides a solid foundation for a larger MW scale 
demonstration of the ability to orchestrate DERs to provide advanced grid services that go 
beyond conventional demand response. This DOE/OE from had led to the technology being 
demonstrated by Packetized Energy on a large-scale project funded by the California Energy 
Commission BRIDGE Program.10 
 Network Constraint and Congestion Management 
 
One of the key challenges in aggregation platforms is managing the network constraints 
while ensuring grid services. Aggregators have limited visibility of network operating 
conditions, particularly such constraint violations as reverse power flow, equipment overloading, 
voltage limit violations, and line congestions due to lack of network model and topology. These 
constraints are generally managed by DMS or utility DERMS. The interaction of the Beyond 
DERMS platform with DMS/Utility DERMS can play a significant role in ensuring that the 
network constraints are respected through network management functions. This concept has been 
demonstrated by Argonne National Laboratory in collaboration with PECO, Schneider Electric, 
and Schweitzer Engineering Lab on a DOE-funded project where microgrid is integrated with 
utility DMS in order to provide support services to distribution grids, particularly the voltage 
support, load relief, and monitoring of DERs and system operating states. 
 
The Beyond DERMS platform communicates mainly with behind-the-meter units and 
uses them in an aggregated fashion to coordinate DERs to ensure that system voltages and 
currents remain within limits, providing a non-wires alternative to conventional transmission and 
distribution network upgrades, whereas DMS/Utility DERMS uses this platform—among other 
resources, such as DER aggregators, utility owned and operated DERs, virtual power plants 
(VPPs), microgrids, and traditional resources such as switches, capacitors, network 
configurations etc.—to provide DSOs with complete awareness, effortless real-time and lookahead constraint management, optimal coordination and management of DERs and aggregators, 
and other system-wide operations. Therefore, if properly integrated, DER aggregators and DMS 
perfectly complement one another, and can provide a full spectrum of DER services regarding 
both customer- and grid-related operations regardless of the DERs’ sizes and locations. In this 
configuration, when a distribution or transmission limit violation is identified, either in real-time 
or forecasted, the DERMS may be in a position to provide service(s) that can help manage that 
 
10 https://www.globenewswire.com/news-release/2021/02/03/2169132/0/en/Packetized-Energy-Awarded-2-MillionContract-to-Make-Energy-Demand-Flexible-and-Help-Solve-California-Grid-Challenges.html.

---


### Page 33

23 
violation by re-dispatching its DERs to alleviate overloads or mitigate voltage or power quality 
problems [IEEE P2030.11]. 
 
While network constraint management is an important aspect of future research, it is 
important to implement and demonstrate the functionality of DERMS functions specified in 
IEEE 2033.11 in many forms of DER aggregation, in microgrids, virtual power plants, and 
resource mixes created for specific market applications. 
 Cybersecurity 
 
At the utility and system operator level, contributions made toward DER cybersecurity do 
not pay sufficient attention to inter- and intra-domain interactions and smart-inverter 
connectivity interfaces, and lack effective scrutiny of third-party vulnerabilities and external 
threats. While the advent of new technologies (such as DERMS and aggregators amid utilities 
and DERs) looks promising from an operational flexibility and resiliency standpoint, the 
cybersecurity implications of enabling communication infrastructure remains largely underresearched. Under California’s Rule 21, DERs are required to support protocol-basedsecurity 
solutions, which are insufficient. DERs span multiple security administrative domains, meaning 
that the utility may only be able to monitor the security posture of devices up to the smart meter 
while DER owners and aggregators control and manage their devices themselves. The various 
networks used to control the DER are likely to be interconnected with the utility control center, 
aggregators, manufacturer cloud networks, and other IT networks, thereby increasing the attack 
surface. 
 
While development of technical and security functionalities for DER communication and 
control networks is still underway, the adoption of smart-inverter-enabled DERs is taking place 
at a breakneck speed for utility- and customer-owned DERs. Utility-owned DERs traditionally 
suffer from security vulnerabilities stemming from the use of legacy systems (e.g., 
programmable logic controller, primitive gateway) and communication protocols (e.g., DNP3, 
Modbus) with insufficient security features. Customer-owned DERs use unsecure 
communication means (e.g., internet) and service platforms (e.g., cloud) to communicate with 
the control center directly or indirectly via DER aggregators and vendors (non-utility entities) 
with no propriety advantage. 
 
The autonomy and privileges of these vendors and aggregators over DER devices, if 
misused, can pose a cybersecurity concern.11 In particular, the security requirements for the 
interaction between customer-owned DERs and aggregators and between aggregators and 
utilities are still being discovered when it is highly expected that these aggregators will pervade 
the local DER administration space in a bid to provide the best experience to customers and 
optimal grid services to utilities. Several cyber-vulnerabilities also exist at DER devices with 
remote-control and two-way communication capabilities (IEEE 1547TM 2018 compliant), which, 
 
11 J. Pack. “Cybersecurity for distributed energy resources and SCADA systems.” (September 19, 2019). 
https://www.tdworld.com/smart-utility/grid-security/article/20973136/cybersecurity-for-distributed-energyresources-and-scada-systems

---


### Page 34

24 
if exploited, could potentially cause a local supply-demand imbalance and power cuts in worstcase scenarios. 
 
A comprehensive framework composed of layered cyber-physical solutions is required to 
prevent, detect, and mitigate cyberattacks through DER devices and associated communication 
systems. More research is currently required on (1) the involvement of aggregators in the largescale DER infrastructure, (2) the cyberthreats and operational risks introduced as a large number 
of devices and access points integrated into utility systems, and (3) the security of parameters 
governing the provision of aggregator services. Therefore, there is a need for (1) a secure 
network architecture for end-to-end solutions for grid services while acknowledging the 
possibility of attack initiation and propagation from external agents, (2) the realization of crossdomain cybersecurity interoperability, and (3) attack-resilient grid service participation strategy 
among DMS, DERMS, DER aggregators, utility-scale PV plants, and customer-owned DERs 
needed to deliver reliable grid services.

---
