# Federated Architecture for Secure and Transactive Distributed Energy Resource Management Solutions (FAST-DERMS)

## Paper Metadata

- **Filename:** Federated_Architecture_for_Secure_and_Transactive_Distributed_Energy_Resource_Management_Solutions_(FAST-DERMS)_DOI_10-2172_1839591.pdf
- **DOI:** 10.2172/1839591
- **Authors:** Ding, Fei and Liu, Weijia and MacDonald, Jason and Ogle, James and Pratt, Annabelle and Saha, Avijit and Hagerman, Joe and Baggu, Murali
- **Year:** 2022
- **Journal/Venue:** 
- **URL:** http://dx.doi.org/10.2172/1839591
- **Extraction Date:** 2025-06-03T15:01:19.023181
- **Total Pages:** 65

## Abstract



## Keywords



---

## Full Text Content



### Page 1

Federated Architecture for 
Secure and Transactive 
Distributed Energy 
Resource Management 
Solutions (FAST-DERMS) 
System Architecture and Reference 
Implementation 
January 2022 
Fei Ding 
Weijia Liu 
Jason Mac Donald 
James Ogle 
Annabelle Pratt 
Avijit Saha 
Joe Hagerman 
Murali Baggu 
NREL/TP-5D00-81566

---


### Page 2

ii 
Disclaimer 
This work was authored in part by the National Renewable Energy Laboratory, operated by Alliance for 
Sustainable Energy, LLC, for the U.S. Department of Energy (DOE) under Contract No. DE-AC3608GO28308. Funding provided by the U.S. Department of Energy Office of Energy Efficiency and 
Renewable Energy Building Technologies Office and the U.S. Department of Energy Office of 
Electricity’s Advanced Grid Research Program through the Grid Modernization Initiative. 
This work was authored in part by the Pacific Northwest National Laboratory, operated by Battelle for the 
U.S. Department of Energy under Contract DE-AC05-76RL01830. 
This work was authored in part by the Lawrence Berkeley National Laboratory operated under Contract 
Grant No. DE-AC02-05CH11231. 
This work was authored in part by Oak Ridge National Laboratory, managed by UT-Battelle LLC for the 
US Department of Energy under contract DE-AC05-00OR22725.

---


### Page 3

iii 
 
Federated Architecture for Secure and 
Transactive Distributed Energy Resource 
Management Solutions (FAST-DERMS) 
System Architecture and Reference Implementation 
Fei Ding1 
Weijia Liu1 
Jason Mac Donald2 
James Ogle3 
Annabelle Pratt1 
Avijit Saha1 
Joe Hagerman4 
Murali Baggu1 
January 2022 

1 National Renewable Energy Laboratory 
2 Lawrence Berkeley National Laboratory 
3 Pacific Northwest National Laboratory 
4 Oak Ridge National Laboratory

---


### Page 4

iv 
Summary 
This document provides system-level specifications for a federated architecture for secure and transactive 
distributed energy resource management solutions (FAST-DERMS), presents a solution, and describes 
operational concepts for the proposed solution. FAST-DERMS enables the provision of reliable, resilient, 
and secure transmission and distribution (T&D) grid services through the scalable aggregation and nearreal-time management of utility-scale and small-scale distributed energy resources (DERs). 
We first present the principles and objectives of FAST-DERMS. Then, after discussing important system 
concepts, we present the specifications for FAST-DERMS and a solution that employs a distributed and 
federated control methodology in which the DERs connected to a single point of common coupling with 
the rest of the system, such as individual substations, are optimized coordinately to provide system-level 
grid services. 
FAST-DERMS aims to aggregate and coordinate the operations of DERs to support T&D grid operations. 
The key optimization and control component of this FAST-DERMS reference implementation is a 
flexible resource scheduler (FRS) that aggregates the DERs within a substation service area. These FRSs 
operate at the substation level and perform constrained economic dispatch of DERs, either directly or 
through a transactive market or aggregator, as shown in Figure ES-1. An FRS Coordinator at the 
distribution system operator (DSO) level aggregates distribution substations operated by FRSs and 
interfaces with the transmission system operator (TSO) to provide transmission services. FAST-DERMS 
also allows for the integration of the FRS Coordinator with an existing distribution utility management 
system that could be employed by the DSO to enhance distribution grid operations. 

Figure ES-1. Conceptual diagram of FAST-DERMS 
This FAST-DERMS reference implementation relies on several key components, including:

---


### Page 5

v 
• DERs: A broad range of DERs—including solar photovoltaics, battery energy storage systems, 
electric vehicles, building loads, and other distributed generators—is considered in the FASTDERMS design. These DERs and the local aggregations of these DERs can offer flexible and 
dispatchable active power and/or reactive power that can be used to support grid services. 
• FRS: The FRS is the key optimization and control component of FAST-DERMS. Its main function is 
to generate firm offers to the wholesale market operated by the TSO through performing reliabilityconstrained commitment in coordination with distribution network management and dispatch of 
DERs connected to a substation. These FRSs operate at the substation level. DERs can subscribe, 
either directly or through an aggregator or transactive market, to the FRS and be treated as 
schedulable resources via different incentive options and at different aggregation levels. 
• FRS Coordinator: The FRS Coordinator maps and aggregates distribution substations operated by 
individual FRSs to the appropriate pricing nodes in transmission markets. 
• Aggregators: Third-party or utility-owned aggregators that already aggregate and control a subset of 
the DERs in the distribution network can also subscribe to the FRS and become controllable assets. 
The aggregator directly interacts with the FRS by providing an aggregated flexibility of its DERs. 
The operations of individual DERs are still managed by the aggregator. 
• Transactive market: FAST-DERMS also recognizes a transactive energy market as one method to 
aggregate and implement DER controls. A transactive market manager is an important FASTDERMS reference implementation component. It manages transactive DERs through a subscription 
to the FRS. 
Also, the successful implementation of DER management requires close collaboration with existing 
utility monitoring and management systems, such as distribution supervisory control and data acquisition 
systems, outage management systems, distribution management systems, and advanced distribution 
management systems. To maintain safe, reliable, and secure operations, utilities must provide an 
overarching authority to DER operations. 
FAST-DERMS follows a “total DSO” approach to enable the interactions between DERs at distribution 
networks and TSOs. This approach requires all resources sited in a distribution network to be aggregated 
through the distribution utility or their surrogate, ensuring that the DSO maintains control of its network 
and enabling the DSO to manage any competing objectives between the needs of the T&D systems. 
Specifically, FAST-DERMS provides a scalable and interoperable approach for distribution utilities to 
aggregate and control a variety of DERs to participate in wholesale electricity markets and provide 
transmission grid services. With the network-level stochastic optimization solved by the FRSs, FASTDERMS can manage the uncertainty in the flexibility offers from DERs within the distribution network, 
and thus they can provide a firm aggregate service to the transmission system. 
Standard-based communications protocols will be used in FAST-DERMS to support reliable and 
interoperable data exchange. This document provides guidance for the communications architecture to 
manage complexity and to encourage interoperability in the context of the FAST-DERMS reference 
implementation. A separate communications system design document will specify the specific standards 
and profiles for implementation. This document provides a high-level overview of the standards 
appropriate for the interfaces among different FAST-DERMS components. 
Given the increasing numbers and sophistication of cyber and physical threats, FAST-DERMS also 
incorporates approaches to detect anomalies and to provide a fail-safe to secure grid operations in the 
presence of cyber-physical attacks. This document provides a brief overview of these approaches.

---


### Page 6

vi 
Acknowledgments 
The authors thank Jason Autrey, Tom Bialek, Tom Eyford, Jesse Gantz, Andrew Ingram, Rahul Kadavil, 
Dino Lelic, Greg Smith, George Stefopoulos and Brad Williams for feedback on the draft of this 
document. We also thank Ryan Fedie, Erika Gupta and Chris Irwin of the U.S. DOE for their guidance. 
The views expressed in the article do not necessarily represent the views of the DOE or the U.S. 
Government. The U.S. Government retains and the publisher, by accepting the article for publication, 
acknowledges that the U.S. Government retains a nonexclusive, paid-up, irrevocable, worldwide license 
to publish or reproduce the published form of this work, or allow others to do so, for U.S. Government 
purposes.

---


### Page 7

vii 
Acronyms and Abbreviations 
ADMS 
advanced distribution management system 
AMI 
advanced metering infrastructure 
BESS 
battery energy storage system 
BMS 
building management system 
BTM 
behind the meter 
CAISO 
California Independent System Operator 
DER 
distributed energy resource(s) 
DERMS 
distributed energy resource management system 
DMS 
distribution management system 
DNP3 
Distributed Network Protocol 3 
DSO 
distribution system operator 
DSSE 
distribution system state estimation 
EMS 
energy management system 
EV 
electric vehicle 
FAST-DERMS 
Federated Architecture for Secure and Transactive Distributed Energy Resource 
Management Solutions 
Fo M 
front of the meter 
FRS 
flexible resource scheduler 
GIS 
geographic information system 
GMLC 
Grid Modernization Laboratory Consortium 
HEMS 
home energy management system 
HVAC 
heating, ventilating, and air conditioning 
IEC 
International Electrotechnical Commission 
IEEE 
Institute of Electrical and Electronics Engineers 
ISO 
independent system operator 
MGC 
microgrid controller 
MPC 
model-predictive controller 
NERC 
North American Electric Reliability Corporation 
OMS 
outage management system 
PV 
photovoltaic 
RTO 
regional transmission organization 
T&D 
transmission and distribution 
TMM 
transactive market manager 
TSO 
transmission system operator 
SCADA 
supervisory control and data acquisition 
VAR 
volt ampere reactive 
VPP 
virtual power plant

---


### Page 8

viii 
Contents 
Disclaimer ..................................................................................................................................................... ii 
Summary ...................................................................................................................................................... iv 
Acknowledgments ........................................................................................................................................ vi 
Acronyms and Abbreviations ..................................................................................................................... vii 
1.0 Introduction .......................................................................................................................................... 1 
2.0 Objectives ............................................................................................................................................. 4 
2.1 Grid Architecture Guidance ......................................................................................................... 4 
2.2 System Architecture Objectives ................................................................................................... 4 
2.3 System Architecture Principles .................................................................................................... 5 
3.0 System Concepts................................................................................................................................... 7 
3.1 Distributed Energy Resource Qualities ........................................................................................ 7 
3.2 System Flexibility ........................................................................................................................ 7 
3.3 Grid Services ................................................................................................................................ 8 
3.4 Distributed, Centralized, and Decentralized Systems .................................................................. 8 
3.5 Federated Architecture ................................................................................................................. 9 
3.6 Laminar Coordination .................................................................................................................. 9 
3.7 Total Distribution System Operator Model ................................................................................ 10 
3.8 Transactive Market Concepts ..................................................................................................... 11 
3.9 Secure Distributed Energy Resource Management for Grid Operations ................................... 12 
3.10 Communications and Interoperability Concepts ........................................................................ 13 
4.0 System Specifications ......................................................................................................................... 14 
4.1 Distributed Energy Resource Flexibility Management in Total Distribution System Operator 
Model ......................................................................................................................................... 14 
4.2 Federated Structure for Heterogeneous Distributed Energy Resource Types and Aggregation 
Methods ...................................................................................................................................... 14 
4.3 Distributed Energy Resource Management with the Laminar Coordination Framework .......... 15 
4.4 Secure Distributed Energy Resource Management for Grid Operations ................................... 15 
4.5 Communications and Interoperability ........................................................................................ 15 
5.0 Federated Architecture for Secure and Transactive Distributed Energy Resource Management 
Solution Reference Implementation ................................................................................................... 18 
5.1 FAST-DERMS Reference Implementation Structure ................................................................ 18 
5.2 Reference Implementation Components .................................................................................... 20 
5.2.1 Distributed Energy Resources ......................................................................................... 20 
5.2.2 Flexible Resource Scheduler ........................................................................................... 22 
5.2.3 Flexible Resource Scheduler Coordinator ....................................................................... 22 
5.2.4 Local Distributed Energy Resource Controls .................................................................. 22 
5.2.5 Aggregators ..................................................................................................................... 23

---


### Page 9

ix 
5.2.6 Transactive Market Manager........................................................................................... 24 
5.2.7 Communications .............................................................................................................. 24 
5.3 Operational Concepts ................................................................................................................. 25 
5.3.1 Flexible Resource Scheduler ........................................................................................... 25 
5.3.2 Registration and Subscription Methods .......................................................................... 27 
5.3.3 Transactive Market .......................................................................................................... 30 
5.3.4 Secure Grid Operations ................................................................................................... 32 
5.4 Interaction Patterns ..................................................................................................................... 33 
5.4.1 Interaction with Transmission System Operator ............................................................. 33 
5.4.2 Interactions with Existing Distribution Utility Systems .................................................. 34 
5.4.3 Interactions with a Wholesale Market Operated by a Transmission System Operator ... 36 
5.4.4 Interactions within a Traditionally Regulated Market Environment ............................... 39 
Appendix A ................................................................................................................................................. 46 
Appendix B ................................................................................................................................................. 48 
Appendix C ................................................................................................................................................. 49 
Appendix D ................................................................................................................................................. 53

---


### Page 10

x 
Figures 
Figure 1. FAST-DERMS manages a wide variety of DERs to provide grid flexibility ......................... 3 
Figure 2. Example laminar network. ...................................................................................................... 10 
Figure 3. Grid Wise interoperability stack. ............................................................................................. 13 
Figure 4. High-level FAST-DERMS reference implementation structure .......................................... 18 
Figure 5. Structure of the FAST-DERMS reference implementation .................................................. 19 
Figure 6. FAST-DERMS reference implementation communications interfaces ............................... 25 
Figure 7. Transactive energy market based on one-way communication ............................................ 31 
Figure 8. Transactive energy market based on two-way communications .......................................... 32 
Figure 9. A two-step process adopted in the FAST-DERMS reference implementation to secure grid 
operations .......................................................................................................................................... 33 
Figure 10. Responsibilities of the FRS and scheduling coordinator based on the market timeline .. 34 
Figure 11. FRS process flow to participate in wholesale markets ........................................................ 37 
Figure 12. Conceptual diagram of FAST-DERMS applied to a vertically integrated utility in a 
traditionally regulated market environment .................................................................................. 40

---


### Page 11

1 
1.0 Introduction 
Traditionally, transmission grid services have been provided by power generating plants, and distribution 
grid management is achieved by legacy voltage regulating devices, such as transformer on-load tap 
changers, capacitor banks, and voltage regulators. As the capacity of distributed energy resources (DERs) 
increases rapidly in modern distribution grids, DERs have become significant contributors to reshaping 
the generation mix and the energy consumption profiles; therefore, using DERs to provide energy and 
grid services at both the transmission and distribution (T&D) levels has started to be investigated by 
utilities and related stakeholders and has been identified as a promising area for research, development, 
and demonstration (Sun and Frew 2021). 
There are various definitions of DERs—some limit the DERs to distributed generation sources (NERC 
2017), and some consider only behind-the-meter (BTM) DERs (DNV GL 2014). In this project, we 
employ a general and extended definition: a DER can be a local generation unit, such as rooftop solar 
photovoltaic (PV) and fuel cells; a storage unit, such as a battery; a flexible and controllable load with 
demand response capability, such as an electric vehicle (EV); or a schedulable building load located at 
low- to medium-voltage distribution systems (International Renewable Energy Agency 2019b) (California 
Public Utilities Commission 2020a). The following key features of DERs can be identified based on the 
adopted definition: 
• A DER can act as a power producer, a power consumer, or even a prosumer that can switch its role at 
will. For some DERs (e.g., inverter-based PV and batteries), active power and reactive power can be 
controlled separately. 
• DERs can be very different from each other in terms of rated power and capacity, consumption 
pattern, generation profile, control method, operational constraints, etc. 
• DERs can provide flexibility because they are controllable within certain physical limitations, such as 
power and capacity limits. Some DERs—e.g., BTM building loads that directly influence the comfort 
of end users—are subject to additional constraints to meet customers’ preference. 
The growth in DERs has brought both challenges and opportunities to utilities (Ardani, O'Shaughnessy, 
and Schwade 2018). Proper cost-effective management of DERs can provide valuable services to meet 
the demands of electric grids and customers. At the same time, utilities must deal with challenges, 
including conductor or equipment overload, protection device malfunction caused by reverse power flow, 
voltage violations, limited real-time communications, retail rate limitations, and cross subsidies. So far, 
utilities have investigated different DER integration and coordination schemes to tackle these challenges. 
Several examples include: 
• Xcel Energy introduced demand response programs for customers with controllable loads, such as 
heating, ventilating, and air-conditioning (HVAC) devices and industrial freezers (Xcel Energy 
2016). Economic rewards are provided to incent customers to reduce electricity consumption during 
peak demand hours. 
• Hawaiian Electric offered a fast demand response scheme that employs DERs to help maintain the 
stability of the grid (Hawaiian Electric 2014). The responses of DERs can be either completely 
automated (where control signals will be directly sent from the utility operator) or semiautomated 
(where customers will manually respond to demand response requests). Owners of DERs 
participating in the demand response scheme receive financial incentives. 
• Pacific Gas and Electric Company implemented a field demonstration of a distributed energy resource 
management system (DERMS) in managing DERs (Ardani, O'Shaughnessy, and Schwade 2018). The

---


### Page 12

2 
demonstrated DERMS use cases include DER data visualization, overload mitigation, voltage 
regulation, DER price response, and operational flexibility improvement. 
Numerous optimization and control strategies have been developed for different types of DERs over the 
years; however, DER management and control are still siloed and at times conflicting between various 
DER technologies and the distribution management systems. Centralized control methods are widely 
adopted to manage large-scale DERs, but a centralized control structure is not scalable to manage a vast 
number of DERs. On the other hand, BTM DERs are generally managed according to local control 
objectives, and they are poorly integrated with the rest of the grid assets. To summarize, the existing DER 
control and management methods have the following limitations: 
• Utilities generally do not have real-time or near-real-time visibility of DERs, especially BTM DERs; 
hence, the observability of the distribution grid is reduced. 
• Existing DERs are typically managed by either a centralized controller or according to local control 
objectives. A large number/capacity of DERs acting only in response to local objectives could lead to 
operational issues in distribution grids, such as voltage sags and feeder overloads. 
• Most DERs are associated with uncertainty factors, including weather conditions and customer 
behavior; however, DER uncertainty has not been well addressed in existing studies. Also, more 
accurate DER modeling techniques are required to accommodate DER integrations with various types 
and characteristics. 
• Existing DER controls typically interact with the local distribution grid for services such as peak 
demand management and volt/volt ampere reactive (VAR) optimization. On the other hand, some 
commercial aggregators have managed to collect and control DERs to directly participate in bulk grid 
services while bypassing the distribution-level control. This can lead to conflict between 
transmission-level market and distribution operational considerations. New mechanisms are needed to 
integrate dispersed DERs and interact with both the distribution system and the transmission system 
to provide holistic grid services. 
To address these limitations, this document specifies a federated architecture for secure and transactive 
DER management solutions (FAST-DERMS). FAST-DERMS enables the provision of reliable, resilient, 
and secure T&D energy and grid services through the scalable aggregation and near-real-time 
management of utility-scale and small-scale DERs. FAST-DERMS addresses the recent FERC Order 
2222 (Department of Energy Federal Energy Regulatory Commission 2020) by providing an architectural 
solution to enable DERs at the distribution system to participate in wholesale markets. It encompasses the 
management of a broad range of DERs, including PVs, battery energy storage systems (BESSs), EVs, 
flexible building loads, combined heat and power, and other distributed generators, as shown in Figure 1. 
These DERs can be dispatched directly if they act individually; as part of a fleet consisting of a single 
technology, such as an EV fleet; or as part of a local aggregation of different types of DERs in buildings, 
managed by a home energy management system (HEMS) or building management system (BMS), or 
among buildings, managed by a microgrid controller (MGC).

---


### Page 13

3 

Figure 1. FAST-DERMS manages a wide variety of DERs to provide grid flexibility 
Increased DER penetration has also driven the power industry to reconsider the role of distribution 
utilities, and the concept of a distribution system operator (DSO) is gaining ground (Rahimi and Mokhtari 
2014). Although not many utilities in the United States today are considered DSOs, we envision that 
DSOs will become common in the future, and therefore we present the proposed FAST-DERMS with 
reference to DSOs. There is a spectrum of organizational models for DSOs. Instead of covering all 
features or possible definitions, we assume only the following key functions for a DSO: (1) responsible 
for real-time operations of the distribution system, (2) operates an open and transparent distribution 
market; (3) manages DERs; and (4) performs long-and short-term planning (Black & Veatch 
Management Consulting 2020).

---


### Page 14

4 
2.0 Objectives 
2.1 Grid Architecture Guidance 
The FAST-DERMS system architecture is using the guiding principles from the Grid Modernization 
Laboratory Consortium (GMLC) Grid Architecture project (GMLC 1.2.1)1. This body of work examined 
the limitations of the existing grid relative to the desired qualities of a modernized grid and specified new 
grid structures to enable the realization of those desired qualities. 
Architecture specifications relevant to the objective of enabling the grid to accommodate and use DERs 
were consolidated into a summary document, referred as the “reference grid architecture document” (Taft 
and Ogle 2021). This document identified several architectural objectives: 
• Provide industry structure models that relieve constraints on the use of DERs, facilitate the increasing 
penetration of DERs, and enable their use for customer and system benefit. 
• Accommodate DERs that might exist in dynamic heterogeneous mixtures that vary across a system 
with multiple models of DER use, ownership, and operation. 
• Enable improved electric system reliability and resilience by automating grid operations and 
responses. 
• Enable creative uses of and access to DER assets, and enable new business models for the grid. 
• Expand bulk power system and distribution system relationships to improve system operation and 
resilience. 
• To the extent that the grid structural changes can enable, support, or provide potential to improve 
recovery after some failure, they should do so. 
The reference grid architecture document also provides specifications for a grid with high penetrations of 
DERs. FAST-DERMS is specifically aligned with a subset of these specifications as outlined in Appendix 
D. See the reference grid architecture document (Taft and Ogle 2021) for more detailed discussions of 
these specifications. The reference grid architecture document contains additional specifications that are 
not required for FAST-DERMS but with which FAST-DERMS is compatible. 
The grid architecture specifications provide structures at a grid level. It informs the system and 
components architecture to ensure that the complex set of components and relationships form a cohesive 
whole at the grid level. 
In the following sections, this document provides system architecture principles and objectives, followed 
by important system concepts. Then we present system-level specifications. Finally, we present a 
description of a FAST-DERMS reference implementation, including operational concepts. 
2.2 System Architecture Objectives 
The fundamental goal of FAST-DERMS is to enable the provision of reliable, resilient, and secure T&D 
energy and grid services through the scalable aggregation and near-real-time management of utility-scale 
and small-scale DERs. To achieve this goal, the system architecture has been developed to support the 
following objectives: 
 
1 https://gmlc.doe.gov/projects/1.2.1.

---


### Page 15

5 
• Enable the provision of energy and grid services at the T&D level from utility-scale and small-scale 
DERs. 
• Coordinate reliability-constrained economic dispatch of DERs connected to a distribution system to 
balance customer and system benefits. Resulting efficiencies enable reduced cost of service for all 
customers. 
• Provide a mechanism, such as stochastic optimization, to manage the uncertainty in the flexibility that 
can be provided by DERs within the distribution network, and thus to provide a firm aggregate 
service to the transmission system. 
• Transparently integrate with existing distribution utility management systems and allow for flexible 
system deployment. 
• Transparently integrate with a broad range of DER types, including solar PVs, BESSs, EVs, building 
loads, and other distributed generators. 
• Enable the coordination of DERs under utility or nonutility ownership/operation and coexistence of 
different control schemes for DERs. 
• Encompass different aggregation levels, including single entities and different kinds of aggregations, 
including fleet operators that aggregate the same types of DERs (e.g., EVs or batteries) and 
aggregators that aggregate different types of DERs (e.g., commercial and industrial curtailment 
service providers). 
• Enable transactive markets to manage the aggregated performance of a group of DERs. Market-based 
signals such as electricity price may be employed to coordinate the DER energy transactions in the 
distribution grid. Both passive responses (such as DERs responding to locational marginal pricing or 
dynamic pricing signals) and active flexibility provisions (such as DERs submitting bid prices for 
energy transactions) need to be considered. 
• Detect and protect against increasing numbers and sophistication of cyber and physical threats. 
Incorporate approaches to detect anomalies and provide a fail-safe to secure grid operations in the 
presence of cyber-physical attacks. 
• Consider the impact of DERs that do not participate in the coordination/control solutions provided by 
the DSO, such as treating them as inflexible net load on the system. For example, some nonutilityowned resources could be operated or managed by themselves and not participate in DSO services. 
Because they do not directly interact with the DSO, these resources are both uncontrollable and 
present high uncertainty to the DSO. 
2.3 System Architecture Principles 
The following principles were core considerations in the development of the FAST-DERMS system 
architecture. 
• Follow a total DSO model, as described in Section 3.7, where all resources connected to the 
distribution level that participate in transmission markets are orchestrated through the DSO to enable 
interactions between DERs at distribution networks and TSOs. This approach requires all 
participating resources sited in a distribution network to be aggregated through the distribution utility 
or their surrogate, ensuring that the DSO maintains control of its network and enabling the DSO to 
manage any competing objectives among the needs of the T&D systems. 
• The coordination of DERs must respect grid operational constraints. To maintain safe, reliable, and 
secure operations, utilities must provide an overarching authority to DER operations; therefore, DER

---


### Page 16

6 
aggregation and control should be achieved through close interactions between the DER aggregation 
mechanisms and existing distribution utility management and communications systems. 
• Apply Laminar Coordination Framework principles (See Section 3.6) to manage the complexity of 
the coordination of increasing numbers of DERs and varying forms of aggregation while enabling 
customer and system benefits. Distribute the control of DER flexibility optimization to substation and 
lower layers to manage at scale. 
• Apply standards-based communications interfaces between system components in a layered 
communications architecture separating functionality from data integration to avoid dependencies 
with specific deployments.

---


### Page 17

7 
3.0 System Concepts 
This section provides general descriptions of concepts that are key for FAST-DERMS, including DER 
qualities, system flexibility, grid services, distributed control, federated control, laminar coordination, the 
total DSO model transactive markets, secure DER management and communications and interoperability. 
Entity definitions are provided in Appendix A. 
3.1 Distributed Energy Resource Qualities 
There are various definitions of DERs—some limit the DERs to distributed generation sources (NERC 
2017), and some consider only BTM DERs (GL 2014). In this project, we employ a general and extended 
definition: a DER can be a local generation unit, such as rooftop solar PV and fuel cells; a storage unit, 
such as a battery; a flexible and controllable load with demand response capability, such as an EV; or a 
schedulable building load located at low- to medium-voltage distribution systems (International 
Renewable Energy Agency 2019b) (California Public Utilities Commission 2020a). The following key 
features of DERs can be identified based on the adopted definition: 
• A DER can act as a power producer, a power consumer, or even a prosumer that can switch its role at 
will. For some DERs (e.g., inverter-based PVs and batteries), active power and reactive power can be 
controlled separately. 
• DERs can be very different from each other in terms of rated power and capacity, consumption 
pattern, generation profile, control method, operational constraints, etc. 
• DERs can provide flexibility because they are controllable within certain physical limitations, such as 
power and capacity limits. Some DERs—e.g., BTM building loads that directly influence the comfort 
of end users—are subject to additional constraints to meet customers’ preference. 
DERs can be clustered according to their basic characteristics as a load, generator, or storage (New York 
ISO 2017). Loads can only withdraw energy from the grid and can provide services such as demand 
response and demand shifting. Typical loads include building loads and EVs without vehicle-to-grid 
capability. Generators can only inject energy into the grid and can participate in energy markets and 
potentially provide ancillary services, such as regulation and reserve. The most common generation-only 
resource in distribution systems is solar PV. A BESS is an ideal example of a storage resource because it 
can both withdraw energy from and inject energy into the grid. Storage resources can provide many grid 
services, including those mentioned and others, such as peak demand management, congestion 
management, and frequency regulation. 
3.2 System Flexibility 
The increasing integration of variable renewable energy resources in T&D grids has brought significant 
uncertainty and intermittence to power systems in terms of planning and operation. As indicated by the 
famous “duck curve” (Loutan 2015), more resources are required to provide services (e.g., ramping and 
reserve) to maintain system reliability to cope with the sharp changes in the system net load curve (U.S. 
Department of Energy 2020a); hence, flexibility becomes an important and desired attribute of modern 
power systems. 
The GMLC Foundational Metrics Analysis project (U.S. Department of Energy 2020a) defines flexibility 
as “the ability to respond to future uncertainties that might stress the system in the short term and require 
the system to adapt over the long term.” In this report, we focus on short-term flexibility in the

---


### Page 18

8 
operational domain. FAST-DERMS aims to enable DERs to improve power system flexibility through 
various aggregation and control methods. 
In general, power system flexibility can be evaluated in the following three dimensions (U.S. Department 
of Energy 2020a): 
• Overgeneration/curtailment: Excess generation from renewable energy sources could result in 
curtailment because of power system reliability requirements. The ability to reduce overgeneration 
(i.e., curtail generation) is a key indicator of flexibility. 
• Ramping: Larger ramping capacity, reduced ramping cost, and faster ramping speed can more 
effectively handle the fluctuations caused by intermittent renewable energy generation and load 
variation, resulting in a more flexible power system. 
• Uncertainty: Generation and load variations will result in oscillations and deviations of system 
parameters such as frequency and voltage that could affect power system reliability. Systems with 
higher flexibility can withstand a higher volume of fluctuations caused by uncertainties associated 
with both generation and demand. 
3.3 Grid Services 
The key functionality of a power system is to deliver consistent and reliable power to customers. Because 
the nature of electricity demands that power generation and consumption must be balanced in real time, 
meeting customer expectations is challenged by various factors, such as supply-demand variation, device 
malfunction, component failure, and cyber threats; therefore, different types of grid services have been 
promoted to tackle these issues from different perspectives and to help maintain electricity service 
quality. 
Grid services can be clustered into two categories: transmission grid services and distribution grid 
services. In general, transmission grids and distribution grids are very different in terms of scale, capacity, 
voltage level, and control method. More information on these services is summarized in Appendix C. 
In addition to transmission grid services, FAST-DERMS enables DERs to enhance local distribution grid 
performances in terms of reliability and power quality. The improved distribution grid performances will 
benefit DER owners in return. 
3.4 Distributed, Centralized, and Decentralized Systems 
To be consistent with the grid architecture reference specification (Taft and Ogle 2021), we use the 
following definitions: 
• A decentralized system is one in which the elements are separate (usually geographically dispersed 
but not always) and act independently, with perhaps some small amount of supervision to provide set 
points, etc. 
• A distributed system is a decentralized system in which the elements cooperate to solve a common 
problem. This implies some form of communication among the decentralized elements. 
• A centralized system is one in which all the computing, logic, control, data analysis, etc., is 
performed at a single element.

---


### Page 19

9 
Distributed systems might have a central element that participates in the overall processes, which is 
sometimes characterized as a hybrid of central and distributed architectures. 
The modern electric grid comprises centralized, distributed, and decentralized elements both in the 
physical grid structure as well in the control structure. 
3.5 Federated Architecture 
A federated architecture is a pattern that allows for interoperability and information sharing between 
semiautonomous, decentralized control systems and applications. In this context, a federate is a collection 
of DERs that are aggregated and managed by some control paradigm—for example, a transactive market 
or a building management system that manages DERs as well as loads. 
Federated systems typically have some form of consolidation and services layer on top of decentralized 
elements (e.g., a federated data warehouse or federated network). A federated network lets multiple 
networks (which could be geographically distributed) work together by employing shared services and a 
central management framework for consistent configuration and policies. 
3.6 Laminar Coordination 
The basic structural elements that are used to compose laminar networks are discussed in (Taft and Ogle 
2021). Typically, a master problem is decomposed into secondary problems, and an inter-domain 
communications bus facilitates bidirectional information flow between coordinator nodes. Multiple 
decompositions are possible for complex problems, with multiple coordination domains. These elements 
provide building blocks for assembling laminar networks for a specific grid or a portion of a grid. Each 
laminar node requires intelligence, i.e., computing capacity. 
An example of a laminar network is shown in Figure 2. The coordination root node could be extended to 
the independent system operator (ISO)/regional transmission operator (RTO), but it does not need to be 
because of the roles and responsibilities defined for the total DSO model, discussed in Section 3.7.

---


### Page 20

10 
 
Figure 2. Example laminar network. Image from Interop Strategic Vision Whitepaper (March 2018) 
3.7 Total Distribution System Operator Model 
Traditionally, distribution systems are modeled as lumped substation nodes in a transmission system, and 
the distribution system is treated as a pricing node in the locational marginal pricing markets. With the 
increasing proliferation of DERs, however, more and more DERs are aggregated and participating in 
wholesale markets. This brings new requirements for defining the roles of TSOs and DSOs. The 
California Independent System Operator (CAISO) has identified a spectrum of possible designs that can 
be envisioned in terms of the complementary roles of DSOs and TSOs (Kristov 2014). 
FAST-DERMS is following the total DSO approach—i.e., the DER aggregators operating resources in a 
distribution system should go through the DSO to participate in the wholesale market. A TSO only 
optimizes the transmission system with the distribution network modeled as an aggregated P-node,1 and 
the DSO is responsible for dispatching all resources in the distribution network and ensuring distribution 
system reliability, efficiency, resilience, and security. There should be no information passing from the 
distribution network to the transmission network or vice versa, other than the data exchange between the 
TSO and DSO, resulting in a more scalable and secure TSO-DSO interaction paradigm. It is structurally 
sound and simpler to implement (Kristov 2014), and it can provide a clean interface and separation of 
roles and responsibilities for DSOs and TSOs (Taft and Ogle 2021). The total DSO model enables the 
 
1 In organized markets using the locational marginal pricing market paradigm, the transmission-distribution interface substation is 
a pricing point, often called a “pricing node” or “P-node.”

---


### Page 21

11 
TSO to use distribution-connected assets for grid resilience and operational flexibility purposes without 
interfacing with distribution operations or impacting distribution system reliability. 
3.8 Transactive Market Concepts 
The transactive energy approach is widely considered as a promising solution to coordinate a large 
number of dispersed, decentralized DERs through an incentive-based mechanism. The most significant 
feature in this approach is that the DER control and coordination is achieved through the exchange of 
value-based information with explicit meaning to negotiate and, ultimately, settle on a price that best 
satisfies each party’s needs and/or constraints. 
Transactive energy has been implemented and tested in numerous pilot projects in the United States, most 
of which focus on: 
• Developing control methodologies (e.g., how controls change verse price) 
• Managing the system through pricing, including: 
– 
Price formation: determining the first price or “seed” price 
– 
Price discovery: determining the capacity or response from an offered price 
– 
Price negotiation: determining the increase or decrease in price and response in an orderly way to 
encourage settlement. 
• Evaluating the response from the approach (e.g., observing what happened or 
measurement/verification of what happened). 
For example, the AEP grid SMART project introduced a real-time market to control DERs that were 
located BTM, such as HVAC systems (Widergren, et al. 2014) (Prinsloo, Mammoli and Dobson 2017). 
The Pacific Northwest Smart Grid Demonstration Grid project implemented and evaluated transactive 
energy concepts for a future smart grid (Lian, et al. 2017) (Agalgaonkar and Hammerstrom 2017). In 
most of these prior works, the DSO “scheduled” DERs based on local data through a price signal to 
implement transactive energy control (Abrishambaf, et al. 2019). A transactive energy system provides 
benefits to multiple parties of an energy system: 
1. Distribution utilities want specific DER responses at a specific time (e.g., temporarily) and in a 
specific location (i.e., spatially) in the distribution system because they require services to correct for 
excursions and constraints or to avoid maintenance, defer capital upgrades, or manage other financial 
considerations of the utilities. 
2. Consumers want DER and BTM assets to reduce their cost and to improve their services when (i.e., 
temporarily) and where (i.e., spatially) they can benefit—otherwise, the customer would do nothing 
and hold the utility to their (regulated) responsibilities. 
3. Implementers, such as demand-side management providers or third-party energy service providers 
(e.g., energy contractors such as those that reduce demand charges or optimize for tariffs), want a 
structure where they can benefit or share in the value of the avoided costs. 
In all these cases, price formation, price discovery, and price negotiation are critical to elicit responses in 
flexibility and energy use from disparate, decentralized devices to satisfy the utility constraints or needs 
and provide customer benefits.

---


### Page 22

12 
In any structure of transactions among multiple parties, buyers and sellers must manage their objectives, 
goals, and decision criteria; their financial or energy constraints; and their willingness or ability to 
exchange services compared to other options. 
For any transaction, the market maker serves as the party responsible for ensuring that there is fairness in 
the exchange between the parties (or, more simply, a structure to transact openly and fairly). They do not, 
however, define the objectives and goals, the value perception for each party, or the economic utility of 
the transaction; rather, they help form the processes and settlement of the exchange. For example, the 
objective or primary goal of each participant or stakeholder is, notionally, described as follows: 
• Because distribution utilities are responsible for reliability by managing and balancing a system with 
two-way power flows, distribution utilities might want new options to minimize price from their 
generation and transmission provider, to adhere to voltage constraints (e.g., ±5% from the ANSI 
voltage tolerance boundary (ANSI C84.1)), to recruit voltage support, or to recruit supplemental 
reactive power. 
• Consumers or implementers (such as demand-side management providers or third-party energy 
service providers) might want new options to minimize price or differentials in price between present 
contracts and future contracts, to improve comfort (e.g., reduce set point excursions), or to better 
manage other needs or expectations. 
3.9 Secure Distributed Energy Resource Management for Grid 
Operations 
FAST-DERMS relies on advanced operational technology and information technology to achieve 
enhanced DER monitoring and control capabilities; however, both cyber and physical threats are 
increasing in frequency and sophistication. FAST-DERMS is facing two major vulnerabilities to cyberphysical threats: misfunction of controls and communications interruption between the controls and 
DERs/DER aggregations. To address these vulnerabilities and achieve resilience against such attacks, 
effective approaches to detect anomalies and provide a fail-safe to secure grid operations in the presence 
of cyber-physical attacks are needed. 
Many anomaly detection methods exist, and they can be divided into model knowledge-based and datadriven methods (Tan, et al. 2020). A critical function of distribution system state estimation (DSSE) is to 
detect, identify, and eliminate bad measurement data. The analysis is essentially based on the properties 
of residuals, and this is the most common model knowledge-based anomaly detection method. The 
weighted least squares estimation assumes that the measurement errors follow a Gaussian distribution. 
Using the linear relation between the residuals and errors, the mean and covariance of the measurement 
residuals can be derived after the DSSE process, and then the properties of the residuals (e.g., normalized 
distribution) can be used to formulate a test to identify the bad measurement data. In traditional weighted 
least squares DSSE, the detection of bad data is done only after the estimation by processing the 
measurement residuals. Based on the properties of residuals, only one suspicious measurement can be 
identified and then removed (or corrected) in each iteration. Then the DSSE must be processed repeatedly 
to get a correct estimation. On the other hand, data-driven methods typically use machine learning 
algorithms to build a model or map a relation of the studied system. If system data do not conform to the 
expected relations, then an attack can be identified.

---


### Page 23

13 
3.10 Communications and Interoperability Concepts 
Given the scope of the FAST-DERMS problem domain, spanning from the TSO to the DSO interface 
through group-level aggregation, and individual DER connections, there is a complex industry-standard 
landscape. Various standards have been used in this space, including Distributed Network Protocol 3 
(DNP3) (IEEE 1815) and the Institute of Electrical and Electronics Engineers (IEEE) Standard 2030.5. 
The latter has been selected as the choice for California implementation in Rule 21 (California Public 
Utilities Commission 2020b). Both communications standards can support different information models, 
and the Rule 21 DER information model is based on International Electrotechnical Commission (IEC) 
Standard 61850 and Sun Spec Modbus. 
The communications landscape gets even more complex if considering the various types of 
communications network technologies and associated protocols that could be used in a specific 
deployment. For the purposes of the FAST-DERMS communications architecture, the primary 
interoperability focus is at the information level, as defined by the Grid Wise Architecture Council’s 
interoperability framework, depicted in Figure 3 (Grid Wise Architecture Council 2008). This layer 
provides a consistent semantic understanding or the domain definition of the information exchanged. In 
addition, it includes the business context to define how the information is applied to specific business 
process interactions. Category 6, the Business Procedures layer, is also relevant to ensure that the rules of 
the interactions are commonly understood. The IEC Common Information Model collection of standards 
(IEC-61970 and IEC-61968) contains examples of industry standards in these layers. 
 
Figure 3. Grid Wise interoperability stack. Image from (Grid Wise Architecture Council 2008)

---


### Page 24

14 
4.0 System Specifications 
This section provides the system specifications for FAST-DERMS. 
4.1 Distributed Energy Resource Flexibility Management in Total 
Distribution System Operator Model 
The reference grid architecture document (Taft and Ogle 2021) specifies several requirements for grid 
entities to support the preferred total DSO model presented in Section 3.7. In this structure, the DSO is 
responsible for traditional distribution system reliability management and for managing distribution assets 
to meet power and energy flows at the T&D interface, to optionally participate in wholesale markets, and 
to provide grid services to the TSO. In addition, DER aggregators and other third-party energy service 
providers do not bypass the DSO to directly participate with the TSO. 
Although this grid structure addresses challenges associated with potential tier bypassing, it creates 
additional responsibilities for traditional grid operators and scalability concerns because the number and 
variety of DERs within a distribution area can be large, as can the different aggregations methods. FASTDERMS provides a means by which the DSO can help manage that complexity while leveraging the 
benefits of DERs and maintaining traditional grid reliability management. 
1. Specification 1: 
1.1. The FAST-DERMS reference implementation shall conform to the TSO and DSO 
responsibilities as defined in the total DSO model. 
1.2. A distributed flexibility management approach is responsible for coordinating the operation of 
the DERs across the entire distribution network to achieve the maximum operational flexibility 
for enhancing grid operations. 
1.3. The distribution utility management system(s) responsible for managing the distribution system 
shall provide reliability constraints to the flexibility management function coordinating DER 
operations. 
4.2 Federated Structure for Heterogeneous Distributed Energy 
Resource Types and Aggregation Methods 
The distribution system might be subject to a broad range of DERs, including PV, BESS, EVs, flexible 
building loads, combined heat and power, and other distributed generators. These DERs might be 
managed individually or as part of a fleet consisting of a single technology, such as an EV fleet; as part of 
a local aggregation of different types of DERs in buildings managed by a BMS or by a HEMS; or among 
buildings managed by an MGC. DERs that are geographically dispersed and of varying types might be 
aggregated and managed via an aggregator. Such a condition presents a complex management front to the 
DSO responsible for the operation of the distribution system with these diverse DER interconnections and 
management paradigms. 
To address this complexity, FAST-DERMS applies the federated architecture concept, described in 
Section 3.5, recognizes the coexistence of different aggregation methods of DERs, and enables the cooptimization and coordination of these different DER aggregations. In this regard, a federate is a 
collection of DERs that are aggregated and managed by some control paradigm—for example, a 
transactive market or a BMS that manages multiple DERs. A FAST-DERMS reference implementation

---


### Page 25

15 
must provide a framework for interoperability and information sharing by which each federate can 
participate with the DSO to provide flexibility in the form of energy and grid services. From the DSO 
perspective, the different forms of DER types, aggregations, and optimization objectives in the federates 
do not need to be exposed; they only need to see an interface by which to leverage potential flexibility 
services. By the same token, the federate does not need to know the details of the grid constraints that can 
drive service requests. 
2. Specification 2: 
2.1 Apply the federated architecture concept and incorporate different methods of aggregating DERs 
to enable co-optimization and coordination. 
2.2 Include price-based controls as an aggregation method. 
4.3 Distributed Energy Resource Management with the Laminar 
Coordination Framework 
A FAST-DERMS reference implementation should follow a Laminar Coordination Framework, as 
described in Section 3.6. 
3. Specification 3: 
3.1 Assemble the coordination and control structure to support grid-constrained DER flexibility 
management from layered control domains. 
3.2 Support distributed DER coordination minimally to the substation level. 
3.3 Ensure extensibility to further distributed decomposition. 
3.4 The types of resources within a control domain should be transparent to other layers. 
4.4 Secure Distributed Energy Resource Management for Grid 
Operations 
A FAST-DERMS reference implementation should address vulnerabilities to cyber-physical threats. In 
particular, the malfunction of controls and communications interruptions are the two major threats that a 
FAST-DERMS reference implementation should prepare for and have the capability to mitigate. 
4. Specification 4: 
4.1 Be aware of threats—for example, incorporate effective approaches to detect anomalies. 
4.2 Have a fail-safe to secure grid operations in the presence of cyber-physical attacks. 
4.5 Communications and Interoperability 
The use of industry-standard communication protocols and profiles for FAST-DERMS is critical to 
achieving the desired interoperability objectives. FAST-DERMS does not dictate a particular standard 
provided it meets the necessary requirements for the information and behavior of the FAST-DERMS 
control architecture. 
Similarly, the FAST-DERMS communications architecture does not specify any specific physical 
network technologies and should be compatible with network topologies and technologies that can 
provide the appropriate communications connections and quality of service necessary for FAST-DERMS 
operations. This is likely to be a mix of utility private communications networks and leased commercial 
service provider networks. In general, distribution supervisory control and data acquisition (SCADA) 
systems, where they exist, have a hub-and-spoke structure, generally using communications networks 
owned by the utility itself. This hub-and-spoke arrangement is augmented in a laminar coordination-based

---


### Page 26

16 
architecture, with communications networks and message buses at the feeder level aggregated at the 
substation level for local distributed controls. With increasing levels of nonutility-owned DER 
connections and potential energy service providers, there might be increasing use of the Internet and 
cloud services (Taft, De Martini and Kristov, 2015). 
The communications architecture is guided by the grid architecture and FAST-DERMS principles, 
objectives, and specifications. The decision to follow a total DSO model in FAST-DERMS defines 
specific roles for the TSO and DSO that establish expectations and requirements for interactions between 
the two. In this model, the DSO is responsible for managing distribution assets. The DSO might provide 
services to the TSO based on DER flexibility in their area over the TSO-DSO interface. DER telemetry 
flows and dispatch instruction flow through the DSO layer, and the devices’ specific details and control 
are not exposed to the TSO. This structure is summarized in the recommendations for DER telemetry in 
Taft (2017). Additionally, the TSO does not bypass the DSO to interact directly with DER devices, 
aggregators, or other energy service organizations. 
FAST-DERMS coordinates DERs to provide energy and grid services but must be guided by the 
operational constraints of the distribution system to ensure that system reliability is maintained. To 
accomplish this, there must be information sharing between the DER management solution components 
and other utility management systems, such as an advanced distribution management system (ADMS), as 
well as a common representation of the distribution network model. A communications architecture that 
uses standards-based information models and separates data integration from application functionality 
within the DSO level will facilitate interoperability and allow flexibility and extensibility (Melton, et al. 
2018). 
A FAST-DERMS reference implementation must support the coordination of DERs connected to various 
feeders across the distribution system, owned or managed by different parties, and organized into a 
variety of different groupings or aggregations. At the same time, it must be aware of the structure and 
operational constraints of the distribution system network to ensure reliability is maintained. The 
communications architecture is guided by the grid architecture Laminar Coordination Framework 
concepts described in Section 3.6. The communications architecture must support multiple layers of 
laminar coordination. These can exist at the DSO, substation, aggregator, building/microgrid, and 
ultimately the DER device levels and the interface between the DSO and TSO. The primary 
communications interfaces occur between these layers (interlayer), but communications between elements 
within a given layer (intra-layer) are compatible with the architecture. This allows FAST-DERMS to be 
extensible with the future evolution of distributed controls for distribution system operation. 
5. Specification 5: 
5.1 Standards-based communications should be employed at all interfaces. 
5.2 The information exchanged between the TSO and DSO for DER management should be limited 
to that needed for energy or grid services at the relevant T&D interface point. 
5.3 Information exchange approaches that separate data integration from application functionality 
should be used to facilitate interoperability and allow flexibility and extensibility. 
5.4 Communications between multiple control domains is required. These can exist at the DSO, 
substation, aggregator, building/microgrid, and the DER device levels and the interface between the 
DSO and TSO. 
5.5 The communications system should be compatible with distributed control approaches that 
require peer-to-peer communications within a layer.

---


### Page 27

17 
5.6 The FAST-DERMS reference implementation should not be dependent on fixed network 
topologies or technologies. It should be able to adapt to dynamic DER grouping and changes in 
network topology.

---


### Page 28

18 
5.0 Federated Architecture for Secure and Transactive 
Distributed Energy Resource Management Solution 
Reference Implementation 
This section describes a specific FAST-DERMS reference implementation, including its overall structure, 
key components, and operational concepts. 
5.1 FAST-DERMS Reference Implementation Structure 
FAST-DERMS aims to aggregate and coordinate the operations of DERs to support T&D grid operations. 
The FAST-DERMS reference implementation follows Specification 1, which requires a total DSO 
approach—i.e., the DER aggregators operating resources in a distribution system should go through the 
DSO to participate in the wholesale market. As described in Figure 4, the FAST-DERMS reference 
implementation leverages DERs—both individual DERs and local aggregations of DERs such as within a 
building (Bldg) or microgrid (ugrid)—to provide energy and grid services and to reduce the cost of 
service for all customers. 
 
Figure 4. High-level FAST-DERMS reference implementation structure 
The core functional component of the FAST-DERMS reference implementation is a flexible resource 
scheduler (FRS) that operates at the substation service area level to perform reliability-constrained 
economic dispatch of a heterogeneous set of DERs that might be aggregated by different means. These 
include local aggregations in buildings or microgrids, a DER aggregator, or a transactive market manager 
(TMM), thereby adhering to Specification 2. The FAST-DERMS reference implementation employs a 
distributed control methodology in which the resources downstream of a given substation are optimized 
independently with limited oversight from central distribution utility management system(s) that manage

---


### Page 29

19 
system reliability. This distributed approach can be further decomposed into various layers in the grid 
structure to form a self-similar hierarchical pattern consistent with the grid architecture Laminar 
Coordination Framework of Specification 3. The distributed approach also helps manage the scalability 
for the DSO. Multiple FRSs exist for a typical distribution system with multiple substations, and therefore 
an FRS Coordinator is needed to represent the overall distribution system at the DSO level. 
The distribution utility management systems might offer constraints to the FRSs through the FRS 
Coordinator as well as request distribution grid services from the FRSs to support reliable distribution 
operations. The FRSs will coordinate the flexibility of DERs based on these constraints and distribution 
reliability. Bounded by constraints from the distribution operations, the FRS Coordinator can also 
facilitate DERs participating in the TSO wholesale market; thus, the FRSs and FRS Coordinator become 
core components of a DSO’s operational systems, complementing existing reliability management 
responsibilities to help manage the complexity of coordinating high levels of DERs. 
Finally, the FRS Coordinator interfaces—either directly or through an existing distribution utility 
management system or scheduling coordinator—with the TSO to negotiate the provision of energy and 
transmission grid services. 
Figure 5 shows a more detailed view of the solution structure with many different kinds of DERs, 
including both front-of-the-meter (Fo M) DERs (such as utility-scale PV power plants, utility-scale BESS, 
and public EV charging stations operated by utilities) and BTM DERs (such as rooftop PVs, small BESS, 
light-duty EVs, and controllable loads that are located at commercial and residential buildings). 
 
Figure 5. Structure of the FAST-DERMS reference implementation 
Each FRS manages the DERs located downstream of a substation (Sub-1 through Sub-M). The FRSs and 
FRS Coordinator can be either stand-alone systems or integrated with existing distribution utility 
management systems. In either case, the FRSs will provide a way for the DSO to manage DERs in the 
entire distribution network to acquire the maximum operational flexibility for enhancing grid operations. 
If a utility management system exists—such as a DMS, an outage management system (OMS), or an

---


### Page 30

20 
ADMS—it is still monitoring and controlling legacy devices (such as voltage regulators) and some DERs 
(such as utility-owned BESS). 
DERs can subscribe directly to the FRS and participate as individuals or as part of an aggregation 
managed by an entity such as a BMS, MGC, aggregator, or a TMM. Entities such as a BMS or MGC that 
manage local aggregations of DERs can subscribe directly to the FRS or through an aggregator or 
transactive market, allowing for multiple levels of aggregation. Any subscriber to the FRS—either an 
individual DER or an aggregating entity—chooses the type of incentive they receive and indicates the 
degree of aggregation they belong to. This allows for resources that can respond to real-time changes in 
price signals as well as those that prefer a capacity payment and opt for direct control. 
FAST-DERMS provides a scalable approach to integrating DSO-managed DERs into wholesale 
electricity markets and transmission system operations following the total DSO model. This model 
requires that all resources sited in a distribution network are aggregated through the distribution utility or 
their surrogate, ensuring that the DSO maintains control of its network and enabling the DSO to manage 
any competing objectives between the needs of the T&D systems (Kristov 2014). We recognize, however, 
that some resources in the DSO’s service territory could be operated by a third-party DERMS and 
interface directly with the TSO. Although this introduces the risks that are addressed by the total DSO 
model, the FAST-DERMS reference implementation can offer some mitigation of these risks. This 
special case is discussed in Section 5.3.2.3. In brief, the impact of DERs that do not subscribe to the FRS 
or are not managed by a DMS/ADMS that interacts with the FRS will be incorporated into the uncertainty 
modeling in the FRS. 
Communication is an important element in FAST-DERMS to support reliable information exchange 
among different components. The FRS requires information from its subscribers to solve its optimal 
scheduling problem. The details and specifics of the information depend on the subscription method. For 
instance, under direct control, it is expected that the FRS could have access to all types of DER 
information, including both static information (such as DER locations and capacities) and time-varying 
DER information (such as real-time DER flexibility and availability). But if a DER is participating via an 
aggregator or a TMM, the FRS might only have knowledge of the DER location and capacity and will 
likely not have access to real-time DER dispatch information that is determined by the internal control 
decisions made by the aggregator or TMM. The FRS also needs to send its scheduling decisions to the 
subscribed resources, and the scheduling decision will be further disaggregated and communicated to 
individual DERs. Data exchanges among the DERs, aggregators, FRSs, TSO, and other distribution 
utility management systems are also necessary to realize the features and functions of FAST-DERMS. All 
the information flow will be realized via standards-based communications protocols, with appropriate 
augmentation to support the advanced probabilistic features of the architecture. 
5.2 Reference Implementation Components 
This section provides a description of the key components of the FAST-DERMS reference 
implementation. Entity definitions are provided in Appendix A. 
5.2.1 
Distributed Energy Resources 
In this project, we consider a general case where many DERs with distinct characteristics and different 
control approaches exist in the distribution system. Examples of the DERs we consider are shown in 
Figure 8, including Fo M DERs and BTM DERs. Generally, a BTM DER is privately owned and operated 
by customers, and it provides power that can be used on-site without passing through a meter. BTM 
DERs are typically small in capacity (e.g., <100 k W). On the other hand, an Fo M DER provides power to

---


### Page 31

21 
off-site locations and passes through an electric meter before reaching end users. They typically have 
large capacities (e.g., >100 k W) and are owned or operated by distribution utilities. Various Fo M DERs 
and BTM DERs can be found in existing distribution systems, and the following DERs are considered in 
the FAST-DERMS architecture: 
1. Fo M DERs: 
– 
PV power plant: A PV power plant refers to a group of solar panels with a common point of 
connection. A PV power plant is connected to the distribution feeder through power inverters that 
can be controlled by the DSO. 
– 
Utility-scale BESS: A utility-scale BESS consists of one or a group of battery energy storage 
unit(s). A utility BESS is connected to the distribution feeder through power inverters that can be 
controlled by the DSO. 
– 
Public EV charging station operated by utilities: Public EV charging stations are typically located 
at commercial areas such as shopping centers and can host multiple EVs. Here, we consider 
public EV charging stations operated by utilities. 
2. BTM DERs: 
– 
Building BESS: A building BESS is a battery-based energy storage system installed at a 
residential or commercial building, and it typically serves as an emergency power supply. A 
BESS is connected to a building load supply system through its power inverter. 
– 
Rooftop PV: Rooftop PV generally refers to solar panels installed on the rooftop of residential 
and commercial buildings. PV panels are connected to the building load supply system through 
power inverters. 
– 
Building load: Building loads can consist of a variety of demands, such as lighting demand, air 
conditioning, and water heating. 
– 
Light-duty EV: Light-duty EVs such as personal vehicles plugged into EV supply equipment 
available at residential buildings and commercial charging stations. 
In addition, local aggregations of different DERs, such as at buildings or in microgrids, are also 
considered. 
Both Fo M and BTM DERs vary in their capabilities to provide grid services; thus, different DERs are 
suited to provide specific grid services according to the service requirements summarized in Appendix C. 
One aspect of capability is the frequency and speed at which the DER can react. As reviewed in Appendix 
C, different grid services require different response speeds. Most DERs can respond to a limited number 
of grid service calls within a certain period. This is common in existing demand response (load-shedding) 
schemes. Some DERs can respond to service calls on an hourly basis. Energy service provision in dayahead and hour-ahead markets are good examples in which DERs respond to market dispatches by 
shifting their generation/consumption at these timescales. Finally, some DERs can be frequently called 
upon and are capable of promptly responding to grid service requests. The representative grid service that 
requires DERs to be very responsive is frequency regulation. Typical DERs that can provide frequency 
regulation services include inverter-based DERs, such as PV and BESS. Most building loads and other 
non-inverter-based DERs have much larger time constants and thus are not well suited to provide 
frequency regulation. 
Further, grid services include active power-based services (such as frequency regulation) and reactive 
power-based services (such as voltage regulation). Transmission grid operations are generally more 
focused on active power, including on energy markets and ancillary services, such as demand response, 
frequency regulation, and congestion management. In distribution grids, peak load management mainly

---


### Page 32

22 
relies on active power management. Both Fo M and BTM DERs can provide active power-related 
services. Inverter-based DERs, such as BESS and PV, can adjust both their active and reactive power 
generation/consumption; therefore, they are widely used to provide both active power-based grid services 
and reactive power-based grid services. Some building loads also produce reactive power, but their 
reactive power is typically not controllable or schedulable, so building loads are generally not used to 
provide reactive power-based grid services. 
5.2.2 
Flexible Resource Scheduler 
The FRS determines the level of wholesale market interaction in FAST-DERMS. The focus of FASTDERMS is on wholesale market contexts run by an ISO or RTO that delivers electricity through 
competitive market mechanisms, though Section 5.4.4 includes discussion of FAST-DERMS within the 
context of traditionally regulated markets.1 Each FRS aggregates all DER types located downstream of a 
substation in a physical distribution network and computes an aggregated bid or schedule for the 
substation service area’s net load (and in rare instances, net generation) for wholesale electricity markets 
as well as bids or schedules for any capacity-based ancillary services and other nonmarket services. The 
bids computed reflect any physical constraints on the distribution system such that all bids will result in 
voltages and equipment loading that is safely within operating limits. These bids are provided to the FRS 
coordinator to be combined and sent to the wholesale markets. Each FRS also disaggregates grid control 
signals in real time to the various resources subscribed to the FRS to meet the service objectives for the 
network. These transmission-level service offers/responses are accomplished while respecting the voltage 
and thermal constraints of the distribution system that the resources are connected to. The interactions 
among the FRSs, FRS coordinator, and the TSO are further explained in sections 5.4.1, 5.4.3, and 5.4.4. 
The geographic scope of an FRS is the feeders connected to one substation. If computationally feasible, 
the FRS will co-optimize all feeders connected to a substation so that the substation tap changers and 
transformer thermal constraints can be considered. If it is not feasible, the feeders will be assumed to be 
independent of one another, and the FRS will treat each feeder as a separate resource connected to the 
substation bus. The FRS will also coordinate with an existing utility DMS, ADMS, or DERMS through 
the FRS coordinator to collect real-time measurements, topology, and utility equipment set points; to 
ensure that the outcomes behind the managed substation are not causing challenges elsewhere in the 
distribution system; and to collect DER schedules if some resources within the scope of the FRS are 
controlled by such systems, as described in Section 5.4.2. 
5.2.3 
Flexible Resource Scheduler Coordinator 
The FRS Coordinator maps and aggregates distribution substations operated by individual FRSs to the 
appropriate pricing nodes in transmission markets. 
It functions as an aggregator of independently optimized substations so that they can be bid into 
wholesale markets, and it directs the appropriate TSO dispatch and control signals to each FRS. It can 
represent each FRS as an independent market resource or as an aggregated resource. 
5.2.4 
Local Distributed Energy Resource Controls 
DERs have local controllers with different control strategies, such as deadband control and droop control, 
depending on the characteristics of DERs and the nature of the control variables. FAST-DERMS does not 
 
1As defined in the Federal Energy Regulatory Commission’s Energy Primer: A Handbook of Energy Market Basics, June 2020, 
available at https://www.ferc.gov/sites/default/files/2020-05/energy-primer.pdf.

---


### Page 33

23 
require specific implementations of local DER controls; however, local DER controllers (such as for 
individual battery and PV inverters) and controllers for local DER aggregations (such as HEMS, BMS, 
and MGC) can choose to subscribe to the FRS. These local DER aggregations are generally too small to 
have the option to directly participate in a wholesale market. Even if they are of adequate size and can 
provide grid services on their own, their revenue might be trivial because of the limited capacity and 
flexibility. By subscribing to the FRS, either directly or through an aggregator or transactive market, the 
increased flexibility provided by all resources is expected to increase the revenue of the local DER 
aggregations from providing scalable transmission grid services. 
For DERs subscribing directly to the FRS, their local DER controllers are required to follow the optimal 
DER dispatch signals provided by the FRS. They must also provide the information that is required by the 
FRS, as outlined in Section 5.3.1.2. In addition, resource flexibility is required information by the FRS 
from all subscribed resources. The flexibility defines the feasible operation bounds of a resource, and its 
format depends on the subscription option of the resource. Currently, not all local DER controllers have 
the capability to quantify such flexibility; therefore, examples of solutions to providing the required 
flexibility information will be developed in this project. 
5.2.5 
Aggregators 
An aggregator is as an entity or agent that aggregates a group of assets or customers to act as a single 
participant in power system and/or power markets (Burger, et al. 2016) (Ikaheimo, Evens and Karkkainen 
2010). Different DER aggregation projects have been proposed, launched, or implemented (Cook, et al. 
2018). Compared with individual DERs that might be too small to participate in electricity markets, DER 
aggregation assembles a portfolio of DERs to meet the capacity requirement and thus can expand the 
economic gains for both the power system and the DER customers (Migden-Ostrander, et al. 2018). Some 
aggregators provide virtual power plant (VPP) services. Also, some aggregators use DERMS as their 
software platforms, where a DERMS is a software-based solution that provides, at a minimum, visibility 
of DERs through asset monitoring and DER scheduling and dispatch; and may also provide power and 
voltage control, resource valuation (U.S. Department of Energy 2015b), the ability to monitor and control 
DER aggregations and forecast DER capabilities (EPRI 2016a). 
DERs can either be aggregated and controlled using a utility-DERMS, as discussed in Section 5.4.2.3, or 
through a third-party management system that is not under the DSO’s control. We refer to such thirdparty management systems as “third-party DERMS.” Multiple third-party DERMS providers exist, such 
as Siemens, Enbala, Auto Grid, and Energy Hub (Guidehouse insights 2020). Such DERMS typically 
manage smart inverters, combined heat and power units, and other distributed generation resources. 
In addition to third-party DERMS, we consider that a variety of third-party aggregators possibly exist to 
manage multiple DERs, such as a fleet of EVs or a group of buildings. These third-party aggregators can 
either subscribe to the FRS and participate in activities to provide transmission grid services or directly 
bid in electricity markets on their own. If the third-party aggregator subscribes to the FRS, it is expected 
to submit the aggregated DER data, uncertainties, and forecasts to the FRS and follow the optimal 
schedules and control signals solved by the FRS. The operations of individual DERs are directly managed 
by the aggregator. If the third-party aggregator directly participates in the wholesale market, it will 
provide self-scheduled consumption/generation of resources under its direct control consistent with 
market gate closure in the day-ahead market. In this scenario, the third-party aggregator will be 
considered a “self-schedulable resource,” as mentioned in Section 5.3.2.3. It should share its intended real 
and reactive operational schedules with the FRS prior to the day-ahead optimization.

---


### Page 34

24 
5.2.6 
Transactive Market Manager 
For FAST-DERMS, a key party in implementing DER controls in the transactive energy market is the 
TMM. The TMM is the “market maker,” and its purpose is to form the market by which the parties can 
engage in price negotiation. The TMM will therefore serve as the pricing node that helps facilitate: 
1. From the perspective of a consumer with DERs, recruit and reward load flexibility through 
transactive resources from both energy efficiency (e.g., reducing energy consumption in k Wh) and 
demand management (e.g., managing power in k W) 
2. From the perspective of the DSO, meet the goal(s) of the utility, such as dispatching DERs to: 
– 
Ensure, improve, or enhance the reliable delivery of power by the utility 
– 
Manage, flatten, or control the variability of renewable generation or changing customer demand 
– 
Better manage customer adoption and dispatch of rapidly changing technologies in connected 
homes and buildings (as a result of the increase of Internet of Things devices in buildings and 
building equipment) 
– 
Help meet obligations to reduce fossil fuel usage through non-wires solutions (e.g., using the load 
side to realize change). 
In an independent third-party configuration, for example, price could be directly seeded from feeder 
information by calculating the distribution locational marginal price to best serve the customer and 
distribution needs. 
In this project, we are exploring two different TMM schemes defined by the direction in which price 
information is shared: 
1. One-way communication: DERs receive and act given a price signal. The price formation will be 
influenced or modified by observation of the responses of DERs. In one-way communications 
approaches, DERs do not submit bids/offers; rather, their response is inferred from observation over 
time. Given the one-way communications mechanism, there are limitations on how quick and how 
“firm” the responses can be considered; therefore, it is expected that a combination of simulations, 
models, and historical data will be leveraged to characterize the uncertainty of responses 
2. Two-way communications: DERs communicate their bids or offers (e.g., quantity of response or 
capacity at a given price) with the TMM. The bids/offers will directly influence the (next) price 
formation until settlement. The price formation will be influenced by the responses of DERs because 
DERs directly submit bids/offers. 
5.2.7 
Communications 
Specific communications standards for different communications interfaces required by the FASTDERMS reference implementation, shown in Figure 6, are defined in the FAST-DERMS Communication 
System Design specification (Anandar 2021). These interfaces include device-level interfaces (1, 2, and 
3), group-level control interfaces (5, 6, and 7), group-level transactive interfaces (4, 8, and 9) and 
transmission service interfaces (10).

---


### Page 35

25 
 
Figure 6. FAST-DERMS reference implementation communications interfaces 
5.3 Operational Concepts 
5.3.1 
Flexible Resource Scheduler 
The FRS determines the aggregate service quantities available for wholesale market bidding from all 
DERs connected behind a distribution substation. It operates on timescales consistent with both dayahead and real-time markets and provides control signals to the managed DERs, while ensuring 
distribution network constraints are respected. Using a stochastic optimization framework, the FRS is 
capable of managing individual DERs, aggregators of DERs, and DERs that participate based on realtime energy prices. The FRS coordinates with other distribution utility management systems, through the 
FRS Coordinator, to ensure it has updated distribution measurements and states, as well as constraints so 
that the aggregate TSO bids are solved based on distribution utility feedback. 
5.3.1.1 
Control Method/Models 
A key function of the FRS will be to manage the uncertainty in the flexibility offers from distributed 
resources and thus provide a firm aggregate service to the TSO. This will be done by formulating an 
optimal power flow-based stochastic optimization using resources through a variety of subscription 
methods. The stochastic optimization will operate at two timescales: 
• Ranging from 24–48 hours ahead for integration into day-ahead electricity markets

---


### Page 36

26 
• On a rolling basis every 5–30 minutes,1 with a time horizon of 2–4 hours. This instance operates as a 
model-predictive controller (MPC) that manages time-coupled resource states and integration into 
hour-ahead/real-time markets. 
A separate dispatch algorithm will disaggregate TSO signals and provide real-time control signals to the 
various resources that have offered flexibility using the results of the MPC. 
5.3.1.2 
Resource Models 
The model used in the optimization for the FRS will incorporate resource-specific and distribution 
network power flow constraints. In general, the FRS expects the following information from the 
resources2: 
• Response model: This describes how the resources, or aggregations of resources, respond to the 
signal sent by the FRS. For transactive resources, this could be price-quantity curves; for aggregators 
or directly controlled resources, this could be simply following a reference signal. If a coupling exists 
between the resource’s real and reactive power output, the coupling information would also be 
provided. If the resource is an aggregation, a model for how the aggregator will dispatch their 
resources could be included as well (e.g., proportional dispatch based on nameplate). This 
information is provided as part of the resource subscription. 
• Feasible region (flexibility): Resources have constraints on both the time-dependent models of 
resource states (such as state of charge) and on the feasible operating regions of the resources 
(maximum power, reactive power, energy storage capacity, etc.). Feasible operating regions could be 
time dependent as well, such as in cases of demand response and EV aggregations. Providing the 
feasible region in which a resource’s states can be operated represents the flexibility of the resource 
and can be provided on a continuous basis because it could evolve with time. 
• Uncertainty: Each resource will have uncertainty associated with forecasted flexibility that will also 
be used by the FRS. A probability density function for each point estimate is ideal, though the exact 
model of uncertainty to be provided is open for discussion. 
• Locational information: Resources will need to provide locational information, ideally which bus and 
phase(s) in the network model they connect to. If they belong to an aggregation that is within an area 
of the network, they can provide the aggregation information instead of a specific bus. This 
information will be used by the FRS to ensure that network constraints are satisfied. We can assume 
that the DSO can supply the network location based on the resource’s service address and its 
subscription method. 
• Cost information (if transactive): Although the resource will specify during subscription that it will be 
responsive based on price, the shape of that response might change over time. A transactive resource 
must provide its cost of generation/price response as a time series of monotonic price-quantity curves. 
It is anticipated that price-responsive resources will have varying abilities to provide such types of 
information. The TMM, another component in the FAST-DERMS architecture, will be capable of 
developing/refining price response models where resources are unfit to provide them. 
It is expected that this information will be in different forms for different resource types. Also, if a 
resource is involved in multiple services or services at multiple timescales, it might need to provide 
 
1 This time is still under investigation and will be finalized in the next version of the document. In general, it could be 5, 15, 30, 
or 60 minutes, depending on the complexity of the model and the needs of the architectural design. 
2 Note that to the FRS, a resource could be a single resource or an aggregation. The information presented applies to both unless 
explicitly stated.

---


### Page 37

27 
information for each service. As of now, we intend to model up to three different types of flexible 
resources: load, generation, and storage. Another option could be to create a single generalized DER 
model that can be used to represent all three types in the FRS. Aggregations of resources will be modeled 
as a single resource, which might make the generalized model the best option. 
5.3.1.3 
Addressing Computational Tractability 
We anticipate that making the stochastic optimization problems tractable will require network-reduction 
techniques to reduce computational complexity. This is an opportunity for other DERMS/ADMS 
functions to supply meaningful information to the FRS. ADMS and third-party DERMS applications 
could identify critical infrastructure locations (buses or lines) or provide live network parameter updates 
to ensure that specific buses are maintained in the reduced-form optimization that would improve the 
performance of the FRS. Other approaches to reduce the computational burden will be examined as well, 
such as careful choice and weighting of scenarios if scenario-based optimization is a selected solution 
methodology. Further, the day-ahead problem might require a different solution methodology and/or 
formulation than the near-real-time MPC. 
5.3.1.4 
Forecasted Input Requirements 
Creating day-ahead offers for the distribution network as a whole requires the use of forecasts for the 
remainder of the load in the network in addition to what controllable resources are providing the system. 
Probabilistic nodal load forecasts will be created on timescales consistent with the day-ahead and hourahead controllers. Similarly, there will also be probabilistic forecasts of insolation and/or PV production 
for the DERs directly managed by the FRS. 
5.3.2 
Registration and Subscription Methods 
During the registration process, DERs in the distribution network that have opted to participate in grid 
service provision will need to effectively “subscribe” to an agreement with the DSO. Agreements for 
resource integration specify the type of incentive that a resource will receive and respond to and the level 
of aggregation of the resource. Appendix B lists some existing settlement plans used by utilities to recruit 
DERs to participate in demand response programs and/or to provide grid services. 
Based on the incentive choice, sources are categorized into two main groups: (1) transactive resources 
whose consumption is dependent on the electricity price and (2) contractually obligated resources that are 
under a prior contract to offer flexibility and are under direct control of the FRS. The aggregation level 
specifies whether a resource is an individual DER or an aggregation of multiple resources and whether 
those resources are co-located—and if not, how much information the FRS has about the location of 
resources. The combination of incentive choices and aggregation level defines the way in which a 
resource is modeled and controlled in the FRS. 
FAST-DERMS does not limit the number of grid services that DERs can participate in. DERs can choose 
the same or different subscription packages for different services at will—e.g., DERs can subscribe as a 
transactive resource for energy market participation and subscribe as a contractually obligated resource 
that is under the direct control of the FRS for ancillary services in the transmission grid; therefore, DERs 
can receive benefits from different programs for providing different services. But DERs are not allowed 
to subscribe through different subscription methods for the same service to avoid “double counting.” 
Under current regulations, double counting—i.e., receiving benefits from different programs for the same 
service—is prohibited; thus, by limiting DERs to one subscription method per service, FAST-DERMS 
can eliminate the possibility of double counting when scheduling the DERs.

---


### Page 38

28 
Resources in the distribution network can also opt out of participation in the FRS by declaring themselves 
to be self-scheduled. These resources could opt for direct participation in wholesale markets or other outof-market activities that require distribution access. But these resources must interact with the FRS to 
provide operation schedules because their production/consumption impacts the substation meter where 
TSO services are measured. 
5.3.2.1 
Incentive Options 
Incentive options govern the method of control by which a resource participates in the FRS—based either 
on price or on direct power set point. The two main categories of incentive structures for resources 
subscribing to the FRS are transactive and capacity obligated. Transactive resources receive remuneration 
primarily based on a savings they can achieve by aligning their consumption with a real-time electricity 
price signal. Contractually obligated resources receive remuneration from participation primarily from an 
existing capacity contract with their DSO. The flexible portion of their capacity will be under direct 
control of the FRS, responding to real and/or reactive power set point commands. 
From the perspective of the FRS, all transactive resources will interact with the FRS in the same manner. 
They will provide hourly price-quantity curves or “bids” for energy that are aligned with decision-making 
for day-ahead market interaction. They will have a recourse opportunity to update that information before 
gate closure for real-time markets. They will provide a measure of uncertainty on the output of those 
curves. Additionally, they will receive hourly pricing that results from TSO day-ahead market clearing 
(for planning purposes) and 5-minute energy dispatch prices that will be settled in real time. We 
anticipate that most resources cannot provide the full suite of data needed for the probabilistic 
optimization of transactive resources, so FAST-DERMS includes a TMM that will provide aggregation 
and integration solutions for these resources. The TMM will act as an aggregator for most transactive 
services, maintaining the single communications and data structure required by the FRS. The ways in 
which a resource might interact with the TMM are described in Section 5.3.3. 
Contractually obligated resources are those that the DSO has previously contracted to provide flexibility. 
These resources are dispatched directly with a real and/or reactive power command from the FRS realtime control. They provide the feasible real and reactive power bounds around which they might be 
controlled as well as schedules of any baseline power being consumed or produced under the absence of a 
service request. Where a form of energy storage exists, they might provide their initial state of charge and 
any off-of-meter changes in energy storage throughout the day (e.g., EVs disconnecting from charging 
infrastructure in a parking garage). We further categorize contractually obligated resources as: 
1. Resources that are under a capacity obligation with a predefined contract to provide flexibility. If 
valuable, day-ahead and MPC optimizations can provide these resources with their expectation of 
power set points based on the optimization runs, though the ability to respond to the real-time 
dispatch controller would be more valuable. It is anticipated that these resources would communicate 
their flexibility and associated uncertainty to the FRS for integration into both the day-ahead and realtime optimizations. Contractually obligated resources could also include energy storage limits in their 
resource definition. 
2. Resources that are under a capacity obligation with a predefined contract to provide flexibility with 
dispatch limitations. These resources are very similar to those described above, but they face dispatch 
limitation seasonally or over another horizon greater than that of the FRS. This is meant to be similar 
to legacy demand response programs in which a limited number of calls is allowed by the program 
per season. The FRS would include an explicit risk of running out of these resources in the objective 
value, though the approach would be based largely on engineering intuition because explicitly 
quantifying this risk is out of the project’s scope.

---


### Page 39

29 
We acknowledge that under certain circumstances (e.g., in advance of public safety power shutoff 
events), the capacity obligation constraints and restrictions might be revised to follow the regulations of 
governing authorities. From the perspective of the FRS, the resource models will be general enough to 
accommodate such scenarios. 
5.3.2.2 
Aggregation Options 
There are five possible levels of aggregation: 
1. Individual metered resources. This is a single resource located at a specific bus on the network 
model, and its interaction is measured at that meter. From the perspective of the FRS, there is not a 
difference between communicating directly with the resource and communicating with a third-party 
aggregator that represents them and relays the dispatch signal. 
2. Aggregations of co-located resources behind a single meter. This resource could comprise multiple 
resource types and exists at a known network location. The expectation is that a local resource 
manager, such as a BMS, would be responsible for disaggregating commands/price response. Some 
examples of these resource types include prosumer commercial buildings with multiple DERs, a 
commercial EV fleet parking lot, or a microgrid. 
3. Aggregations behind multiple meters—resources known. In the process of registering their 
aggregation, the aggregator indicates the locations and capacities of all their resources in the network; 
however, the resource the FRS uses is the whole aggregation, and it integrates only with the 
aggregator; thus, when the FRS sends a dispatch command to the aggregator, the locations that the 
aggregator uses to respond to that dispatch are unknown. The FRS must represent this dispatch with 
some model of the spatial uncertainty of the dispatch. 
4. Aggregations behind multiple meters—resources partially known. The aggregator indicates to the 
FRS the total capacities of its aggregation (and associated uncertainties) in accordance with its 
bidding process timeline. The FRS has a general knowledge of where and what resources are in the 
network (such as that they are inside a particular “zone” of the distribution network). Integration is 
purely with the aggregator. 
5. Aggregations behind multiple meters—resources unknown. The aggregator indicates to the FRS the 
total capacities of its aggregation (and associated uncertainties) in accordance with its bidding process 
timeline. The FRS has no knowledge of where or what resources are in the network (though perhaps 
there could be boundaries such as a group of laterals). Integration is purely with the aggregator. This 
carries the most uncertainty of any aggregation model and would be the least valuable, though likely 
much easier to assemble. 
5.3.2.3 
Non-Subscribing Resources 
These are also resources that will not subscribe to and provide their flexibility to the FRS. Some resources 
could participate directly in the wholesale market. We assume that these resources will have a wholesale 
distribution access tariff1 in place, and thus these resources will require interaction with the DSO to gain 
access. From the perspective of the FRS, these resources become self-scheduled resources, and they are 
treated as inflexible net load on the system. Although these resources are not providing their flexibility to 
the FRS, they are located inside the distribution network that is managed by the FRS; therefore, these 
self-schedulable resources will be required to provide their intended power/energy operational schedules 
prior to the day-ahead optimization. If they provide economic bid curves to the wholesale market, these 
 
1 Today, a distribution-connected resource needs a contract with the utility to access wholesale markets. This is called a 
Wholesale Distribution Access Tariff.

---


### Page 40

30 
could be provided in lieu of scheduled operation. We also assume that the wholesale distribution access 
tariff would have provisions to revoke access or to penalize the resource if it significantly deviates from 
its schedule. This scheme will ensure that the FRS can assume that the information is relatively accurate 
and perform its network optimization. 
Some nonutility-owned resources could be operated or managed by themselves and do not participate in 
the wholesale market. Because they do not directly interact with the FRS/DSO, we assume that the FRS 
has no knowledge of these DERs other than their locations and capacities if they are registered with the 
distribution utility. These resources are both uncontrollable and introduce high uncertainty into the FRS 
optimization models. 
In practice, these non-subscribing resources need to go through an interconnection procedure before being 
connected to the distribution grid; thus, their capacities and other basic parameters are registered, and they 
are considered to be available to the FRS. Although the FRS does not have the authority to directly 
dispatch these resources, the registration information will be used by the FRS for uncertainty modeling 
and optimization. 
5.3.3 
Transactive Market 
In this project, we are exploring two different TMM schemes defined by the direction in which price 
information is shared: 
1. One-way communication: DERs receive and act given a price signal. The price formation will be 
influenced or modified by observation of the responses of DERs. In one-way communication 
approaches, DERs do not submit bids/offers; rather, their response is inferred from observation over 
time. Given the one-way communication mechanism, there are limitations on how quick and how 
“firm” the responses can be considered; therefore, it is expected that a combination of simulations, 
models, and historical data will be leveraged to characterize the uncertainty of responses. 
2. Two-way communication: DERs communicate their bids or offers (e.g., quantity of response or 
capacity at a given price) with the TMM. The bids/offers will directly influence the (next) price 
formation until settlement. The price formation will be influenced by the responses of DERs because 
DERs directly submit bids/offers. 
5.3.3.1 
One-Way Communication Scheme 
The one-way communication scheme results from a consideration of how to best organize technology in 
buildings and considering the building/grid relationship. It is also significantly inspired by appropriate 
lessons from the success of information technology by considering that the amount of diverse legacy DER 
technologies we have today will be dwarfed by what we will have in 10 years. The one-way 
communication scheme helps address “backward compatibility” as grid technologies evolve. 
Energy and grid services could be separated into three buckets: (1) those concerned primarily with the 
overall balance of the supply and demand of energy to minimize costs, (2) those concerned with power 
quality and related energy topics, and (3) those that address system capacity constraints that are primarily 
local. Further, the use of direct load control, event-based demand response, and aggregators began at a 
time when DER control was a priori. Through their existence, however, these schemes have slowly 
worked on pricing, response, and “firmness” a posteriori. For these reasons, one-way communication 
schemes are important to revisit.

---


### Page 41

31 
In the one-way communication diagram shown in Figure 7, a price signal is passed from the FRS to the 
transactive resources, where the DERs operate themselves and “consume” energy. A response evaluator is 
introduced in the TMM to observe the “consumed” energy (e.g., the observed feeder-level energy) or 
response to the provided price. The response evaluator will send the estimated response as a function of 
the price change that was observed to the FRS. As explained, the responses of the DERs can be estimated 
by the response evaluator based on historical data, demand elasticity, etc. 
 
Figure 7. Transactive energy market based on one-way communication 
5.3.3.2 
Two-Way Communications Scheme 
In the two-way communications scheme, shown in Figure 8, the price and response can be communicated 
bidirectionally between the parties. The TMM serves as the intermediary between the transactive 
resources and the FRS. The two-way communications scheme consists of the following steps: 
• The FRS sends a forecast as a high-/low-price band derived from its needs to the TMM. 
• The TMM calculates a flexibility band (as a bid price) and sends the forecast to the transactive 
resources. 
• The transactive resources optimize their energy schedules with respect to the received price forecast 
and generate the corresponding quantity of responses that are sent back to the TMM. 
• The TMM evaluates the received quantity offers at the bid prices from the transactive resources and 
settles the local market according to the pricing scheme with respect to distribution system 
constraints, or it engages in price discovery/negotiation again (repeating steps 2 and 3) to arrive at a 
settled price and quantity. 
The settled DER responses will then be sent to the FRS. The TMM can augment the data to include an 
estimation of uncertainty to characterize the anticipated firmness of the DERs.

---


### Page 42

32 
 
Figure 8. Transactive energy market based on two-way communications 
5.3.4 
Secure Grid Operations 
To secure grid operations with the adoption of FAST-DERMS, this solution incorporates a two-step 
process to enhance the security of FAST-DERMS. As depicted in Figure 9, the first step is to detect 
anomalies using a hybrid method incorporating both DSSE and a machine learning algorithm. The hybrid 
anomaly detection method can effectively defend against false data injection attacks targeted at both 
system model and real-time DER measurements. Once an anomaly is detected, the FRS will be informed 
for re-optimization, and local volt/VAR responses of inverter-based DERs will adaptively stabilize the 
network voltage and frequency (xx). Through such a two-step procedure, FAST-DERMS can help secure 
grid operations in the presence of unexpected events to some extent. We recognize that passive anomaly 
detection has limited capability in handling sudden, large-scale failures, and a holistic approach that can 
prepare for, detect, mitigate and endure attacks is needed to comprehensively secure grid operations.

---


### Page 43

33 
 
Figure 9. A two-step process adopted in the FAST-DERMS reference implementation to secure grid 
operations 
5.4 Interaction Patterns 
5.4.1 
Interaction with Transmission System Operator 
In this section, we assume that the TSO is an ISO or an RTO that operates wholesale markets through 
competitive market mechanisms. In Section 5.4.4, we discuss the operation of the FRS in traditionally 
regulated markets. 
FAST-DERMS is following the total DSO approach, as introduced in Section 3.7—i.e., the DER 
aggregators operating resources in a distribution system should go through the DSO to participate into the 
wholesale market. 
According to market regulations, the FRS Coordinator might not be eligible to directly bid in the ISO 
market. For example, the California Independent System Operator (CAISO) requires all businesses except 
for the acquisition and holding of congestion revenue rights to be conducted through approved and 
registered entities called “scheduling coordinators.” For simplicity, hereafter we use the term FRS to refer 
jointly to the individual FRSs and to the FRS Coordinator. 
The primary responsibilities of scheduling coordinators are to: 
• Represent generators, load-serving entities, proxy demand resources, reliability demand response 
resources, importers, and exporters 
• Provide North American Electric Reliability Corporation (NERC) tagging data 
• Submit bids and inter-scheduling coordinator trades 
• Settle all services and inter-scheduling coordinator trades related to the CAISO markets 
• Ensure compliance with CAISO tariff 
• Submit annual, weekly, and daily forecasts of demand. 
Note: The FRS is not a scheduling coordinator, and it does not necessarily make the DSO become a 
scheduling coordinator. Two scenarios could exist:

---


### Page 44

34 
1. The DSO is not a certified scheduling coordinator. In this scenario, the FRS generates energy bids 
and submits bidding information to its corresponding scheduling coordinator for market clearing. 
2. The DSO is a certified scheduling coordinator. In certain cases where the DSO can act as a 
scheduling coordinator, the FRS can be configured to directly submit its bids to the wholesale market 
on the DSO’s behalf. 
In this project, we consider the scenario where the DSO is not a scheduling coordinator. Figure 10 
illustrates the responsibilities of the FRS and the scheduling coordinator along the market operation 
timeline. As shown in Figure 10, there is a clear boundary between the responsibilities of the FRS and the 
scheduling coordinator. The FRS manages the market participation strategies of DERs and submits bids 
to the scheduling coordinator on behalf of the DSO. The scheduling coordinator aggregates bid 
information and directly interacts with the market operator. When the market is cleared, the scheduling 
coordinator allocates the market settlement to the corresponding FRS. The FRS then takes the 
responsibility to disaggregate the settlements and notify its subscribers about their final energy schedules. 
 
Figure 10. Responsibilities of the FRS and scheduling coordinator based on the market timeline 
5.4.2 
Interactions with Existing Distribution Utility Systems 
FAST-DERMS focuses on the control integration of DERs through the FRS. Legacy devices—such as 
load tap changers, voltage regulators, capacitor banks, and line switches—are still managed and 
monitored by existing utility management systems. 
As described in Section 5.2.2, the FRS provides two major functions: 
1. Provide a bid or schedule to a wholesale market on behalf of the DSO as well as bids or schedules of 
any capacity-based ancillary services and other nonmarket services. 
2. Disaggregate grid control signals in real time to the various resources subscribed to the FRS (as 
described in Section 5.3.2) to meet the objectives for the entire network.

---


### Page 45

35 
In addition, the FRS needs to coordinate with existing distribution utility management systems to satisfy 
both distribution voltage and thermal constraints and to maintain distribution system reliability. 
The FRS requires a certain amount of system information that can be acquired directly from SCADA and 
geographic information system (GIS) if utilities do not have a DMS or an ADMS. For utilities that do 
have a DMS or an ADMS, the FRS can be embedded in the existing DMS or ADMS platforms, or it can 
acquire system information from the DMS/ADMS to perform its task. This section provides an overview 
of the relationship between the FRS and existing utility systems 
5.4.2.1 
Supervisory Control and Data Acquisition 
For DSOs that do not have a DMS or an ADMS, the FRS requests system topology information, DER 
locational information, and real-time feeder head measurements (e.g., active and reactive powers, 
voltages, currents) from the SCADA system. In such systems, the legacy devices are typically operating 
under local control. In addition, it is important for the FRS to consider the local capacitor operations and 
regulator tap position changes when solving its optimization problems. 
5.4.2.2 
Distribution Management System and Advanced Distribution Management 
System 
For DSOs that have a DMS or an ADMS, the FRS can be embedded in the existing DMS or ADMS 
platform, or the FRS can acquire system information from the DMS/ADMS. In either configuration, the 
FRS performs best when operating in a total DSO model, where all resources located in the network are 
either responsive to the control and/or price signals or provide self-schedules on time to limit exposure to 
poor market and control performance measured at the substation meter. There are a few opportunities to 
leverage the capabilities of a DMS/ADMS in FAST-DERMS: 
1. The DMS/ADMS updates topology as switching decisions are made and provides set point schedules 
for legacy devices (e.g., capacitor banks and voltage regulators). Ideally, this is done prior to gate 
closure in day-ahead wholesale markets because significant topology changes can have large impacts 
on resource availability for the distribution feeder aggregation. 
2. Network reduction will be used in the FRS to reduce optimization computational complexity. There 
could be some critical buses that should not be merged or simplified in the network reduction, and 
these bus locations should be provided by the DMS/ADMS to the FRS. 
3. The DMS/ADMS checks the feasibility of the power flow resulting from the FRS to satisfy local 
distribution system operational requirements with the potential control actions on legacy devices and 
flags any buses that could result in a constraint violation, prompting an update of constraints and 
rerunning the FRS to achieve feasibility. This feasibility check will be useful as a safety check, and it 
will be valuable to ensure reliable system operation given the simplifications and assumptions made 
to perform multiperiod optimal power flow in the FRS. 
If a distribution utility does not have a DMS or an ADMS, the FRS will operate as a stand-alone system, 
and it can run full-system power flow to perform a feasibility check. 
5.4.2.3 
Distributed Energy Resource Management System 
As a complement to a DMS that controls only legacy grid assets, some DSOs also have a DERMS or an 
ADMS providing DERMS functions to control utility-owned DERs, such as solar power plants and 
utility-scale BESSs. DERMS applies to software that can integrate the needs of utility grid operations

---


### Page 46

36 
with the capabilities of flexible demand-side energy resources at the edges of the grid (Greentech Media 
2017) and manage diverse and dispersed DERs, both individually and in aggregate, to support multiple 
objectives related to distribution grid operations, end-customer value, or market participation. We call 
such systems “utility-DERMS.” For such utilities, the FRS is a complement to the existing utilityDERMS, and it will add extensive energy scheduling capability for both privately owned and BTM 
DERs. The coordination between the FRS and utility-DERMS varies significantly depending on whether 
the FRS can schedule the DERs operated by the utility-DERMS or not. 
If the FRS can schedule these DERs, the FRS will acquire DER data from utility-DERMS and treat them 
as a group of flexible resources managed by a utility-owned aggregator. The utility-DERMS will control 
its DERs to follow the schedules optimized by the FRS. 
If the FRS cannot schedule these DERs, the utility-DERMS will schedule its DERs in accordance with its 
original rules, and the FRS might receive the schedules of utility-owned DERs and treat them as known, 
non-dispatchable loads. 
5.4.3 
Interactions with a Wholesale Market Operated by a Transmission System 
Operator 
This section provides an example of an FRS interacting—through a scheduling coordinator—with a 
wholesale market operated by a TSO for a distribution utility that has an ADMS deployed. As before, we 
use the term FRS to refer jointly to individual FRSs and to the FRS Coordinator. A sequence diagram in 
Figure 11 shows the process flow of the FRS participating in the wholesale market and the interactions 
between the FRS and the other relevant entities.

---


### Page 47

37 
 
Figure 11. FRS process flow to participate in wholesale markets 
The interactions are divided into two stages: the scheduling stage and the operation stage. An explanation 
of these two stages is provided in the following. 
(1) Scheduling Stage 
In the scheduling stage, the FRS has three major roles: 
• Optimizing DER schedules 
• Coordinating with the ADMS to avoid distribution operation constraint violations 
• Bidding into electricity markets. 
To optimize DER schedules, the FRS needs to retrieve the following data before scheduling DERs: 
• Network topology and parameters as well as the settings of legacy devices from the ADMS

---


### Page 48

38 
• Resource model information, as discussed in Section 2.2.1.1, from the resources that have subscribed 
to the FRS 
• Intended power/energy operational schedules from the self-scheduled, nonparticipating resources 
• Locations and capacities of other nonparticipating DERs (not self-scheduled), if known, from the 
DSO 
• Historical operating data (market price, etc.) from the FRS’s own database. 
To coordinate with the ADMS: 
• The FRS sends its DER schedules to the ADMS. 
• The ADMS runs full-network power flow and performs a feasibility check based on the DER 
schedules submitted by the FRS, load forecast, and legacy device status. If distribution network 
constraints are violated, the ADMS will notify the FRS, and the FRS will need to revise the DER 
schedules to avoid the violations. 
To participate in electricity markets: 
• The FRS generates bidding blocks (quantity and price) based on the aggregated resources’ flexibility 
for different grid services and submits the net load bidding blocks to the scheduling coordinator for 
market clearing. 
• The FRS receives cleared market settlements from the scheduling coordinator. 
• The FRS allocates disaggregated awards and settled prices to its subscribed resources for day-ahead 
and intra-hour planning. 
(2) Operating Stage 
In the operating stage, the major role of the FRS is managing the responses of subscribed resources to the 
grid service requests. The FRS might receive grid service requests throughout the operation period. Based 
on the service request and the scheduling solution determined during the scheduling stage, the FRS will 
determine the disaggregated real-time control signals and send them to its subscribed resources. The 
actual responses of the subscribed resources will be collected and monitored by the FRS. If a grid service 
request cannot be fulfilled by some resources that have subscribed to those services, the FRS will perform 
a real-time redispatch to meet the grid service target through the control of other available resources. 
Because of the fast response requirement of real-time operation, unlike the scheduling stage, we assume 
that there is no interaction for a feasibility check and decision revision between the ADMS and the FRS. 
Instead, it is expected that the ADMS can provide the FRS with the operation/control laws of its 
controlled legacy devices or the acceptable range of the power injection at the bus locations of the FRS 
resources so that the real-time control signals generated by the FRS will not violate distribution network 
operation constraints (such as voltage or thermal limits). But it is possible that some ADMS platforms 
cannot provide such information; in that case, alternative solutions will need to be found to address the 
constraint violation issues.

---


### Page 49

39 
5.4.4 
Interactions within a Traditionally Regulated Market Environment 
Utilities in traditionally regulated markets1 are frequently vertically integrated, owning generation, 
transmission, and distribution (Coley Girouard 2015). In a vertically integrated utility, the FRS still 
aggregates and optimizes the operations of all DERs located downstream of a substation in a physical 
distribution network and provides a schedule for the network’s net load (and in rare instances, net 
generation) to the utility’s transmission operator on behalf of the distribution operator as well as bids or 
schedules for any capacity-based ancillary services while maintaining voltage and thermal constraints in 
the distribution system. 
So far, we have considered the FRS scheduling DER flexibility in competitive markets operated by an 
ISO or RTO. Although competitive markets are absent in a traditionally regulated market, this does not 
introduce unique technical difficulties for deploying flexible DERs to support transmission-level 
operations. The FRS can still be relied on for aggregating and optimizing DERs; thus, this subsection 
briefly reviews the interaction between the FRS and other entities within a traditionally regulated market 
environment. 
A general conceptual diagram of FAST-DERMS when adopted by utilities in a traditionally regulated 
market environment is shown in Figure 12. The key difference between Figure 12 and Figure 5 lies in the 
interaction of the FRS with the transmission system. Because vertically integrated utilities in a 
traditionally regulated market environment do not rely on a competitive electricity market to schedule 
generating resources, the FRS will not communicate with a scheduling coordinator or market operator. 
Instead, the FRS still needs to solve its optimization problem but directly submits the schedule for the 
network’s net load (and in rare instances, net generation) to the transmission operator in the utility 
company for its scheduling and dispatch purposes. The FRS subscription methods described in Section 
5.3.2 are still applicable for DERs in a traditionally regulated market environment. 
 
1 As defined in the Federal Energy Regulatory Commission’s Energy Primer: A Handbook of Energy Market Basics, June 2020, 
available at https://www.ferc.gov/sites/default/files/2020-05/energy-primer.pdf.

---


### Page 50

40 
 
Figure 12. Conceptual diagram of FAST-DERMS applied to a vertically integrated utility in a traditionally 
regulated market environment 
At present, although a utility company is vertically integrated, the operations of the transmission system 
and the distribution system might still be completely isolated. Also, there exist some vertically integrated 
utilities in which DERs are owned and operated by the generation side, which oversees the operations of 
generators, but the generation operators do not have connections with distribution operators. To reflect 
such scenarios, we use dashed lines in Figure 12 to denote the connections between the generation 
operations and the distribution operations. With the increasing integration of DERs, to fully exploit the 
value of DERs, we envision that both communications and coordination will exist among generation, 
transmission, and distribution operations within vertically integrated utilities in a traditionally regulated 
market environment in the near future.

---


### Page 51

41 
References 
ABB. 2019. "DERMS looking ahead." 
https://library.e.abb.com/public/8c470712bab44130b06b3d3da74c7bcf/DERMSLooking-Ahead_9AKK107492A2126-US.pdf. 
Abrishambaf, Omid, Fernando Lezama, Pedro Faria, and Zita Vale. 2019. "Towards transactive 
energy systems: an analysis on current trends." Energy Strategy Reviews 100418. 
Agalgaonkar, Yashodhan P., and Donald J. Hammerstrom. 2017. "Evaluation of smart grid 
technologies employed for system reliability improvement: Pacific Northwest smart grid 
demonstration experience." IEEE Power and Energy Technology Systems Journal 24-31. 
American Electric Power. 2011. "Direct load control event." 
https://smartgrid.epri.com/Use Cases/Direct%20Load%20Control%20Event_ph2add.pdf. 
Anandar, Jithendar. 2021. "FAST-DERMS Communication System Design Specification". 
Electric Power Research Institute. 
Ardani, Kristen, Eric O'Shaughnessy, and Paul Schwade. 2018. "Coordinating distributed energy 
resources for grid services: a case study of Pacific Gas and Electric". Golden, CO: NREL. 
Argonne National Laboratory. 2017. "Foundational report series: advanced distribution 
management systems for grid modernization." 
Black & Veatch Management Consulting, LLC. 2020. "Distribution System Operator (DSO) 
Models for Utility Stakeholders: Organizational Models for a Digital, Distributed Modern 
Grid." https://www.bv.com/sites/default/files/202001/20%20Distribution%20System%20Operator%20Models%20for%20Utility%20Stakeh
olders%20WEB%20%281%29.pdf. 
Burger, Scott, Jose Pablo Chaves-Avila, Carlos Batlle, and Ignacio J. Perez-Arriaga. 2016. "The 
value of aggregators in electricity systems." http://energy.mit.edu/wpcontent/uploads/2016/01/CEEPR_WP_2016-001.pdf. 
California Energy Commission & California Public Utilities Commission. 2015. 
"Recommendations for utility communications with distributed energy resources (DER) 
systems with smart inverters, Smart Inverter Working Group Phase 2 Recommendations, 
Draft v9." https://www.energy.ca.gov/sites/default/files/201905/SIWG_Phase_2_Communications_Recommendations_for_CPUC.pdf. 
California ISO. 2020a. "Business practice manual for market operations." Mar. 
https://bpmcm.caiso.com/Pages/BPMDetails.aspx?BPM=Market%20Operations. 
—. 2015a. "Energy storage and distributed energy resources (ESDER) stakeholder initiative." 
Jul. 
http://www.caiso.com/Initiative Documents/Energy Storageand Distributed Energy Resourc
es-Issue Paper Straw Proposal.pdf. 
—. 2015b. "Flexible ramping product: revised draft final proposal." Dec. 
http://www.caiso.com/Documents/Revised Draft Final Proposal-Flexible Ramping Product2015.pdf. 
—. 2016. "Frequency response phase 2." Dec. 
https://www.caiso.com/Documents/Issue Paper_Frequency Response Phase2.pdf. 
—. 2020b. "PDR-DERP-NGR summary comparison matrix." 
http://www.caiso.com/Documents/Participation Comparison-Proxy DemandDistributed Energy-Storage.pdf. 
California Public Utilities Commission. 2020a. Distributed energy resources. 
https://www.publicadvocates.cpuc.ca.gov/der.aspx.

---


### Page 52

42 
—. 2020b. Rule 21 Interconnection. https://www.cpuc.ca.gov/Rule21/. 
Cleveland, Frances, and Annabelle Lee. 2013. "Cyber security for DER systems." EPRI. Jul. 
https://smartgrid.epri.com/doc/der%20rpt%2007-30-13.pdf. 
Coley Girouard, and Danny Waggoner. 2015. How much do you know about your electric utility. 
Feburary 17. https://blog.aee.net/how-much-do-you-know-about-your-electric-utility. 
Cook, Jeffrey J., Kristen Ardani, Eric O'Shaughnessy, Brittany Smith, and Robert Margolis. 
2018. Expanding PV value: lessons learned from utility-led distributed energy resources 
aggregation in the United States. Golden, CO: NREL. 
Department of Energy Federal Energy Regulatory Commission. 2020. "Participation of 
Distributed Energy Resource Aggregations in Markets Operated by Regional 
Transmission Organizations and Independent System Operators." 
ENTSO-E. 2020. Transmission system operator. http://www.entsoeevent.eu/transmission_system_operator.html. 
EPRI. 2016b. "Abstract: electricity utility guidebook for geographic information systems data 
quality: metadata." Sep. https://www.epri.com/research/products/000000003002007921. 
—. 2016a. "Common functions for DER group management, third edition." Nov. 
https://www.epri.com/research/products/000000003002008215. 
FERC. 2020. Regional transmission organizations (RTO)/independent system operator (ISO). 
https://www.ferc.gov/industries/electric/indus-act/rto.asp. 
GL, DNV. 2014. "A review of distributed energy resources." Sep. 
http://documents.dps.ny.gov/public/Common/View Doc.aspx?Doc Ref Id=%7B52BC75E8
-BBDD-4E2C-9D7D-34C160E0753A%7D. 
Greentech Media. 2017. The Distributed Energy Resource Management System Comes of Age. 
https://www.greentechmedia.com/articles/read/the-distributed-energy-resourcemanagement-system-comes-of-age. 
Grid Wise Architecture Council. 2008. "Grid Wise Interoperability Context-Setting Framework." 
—. 2015. "Grid Wise transactive energy framework, version 1.0." Jan. 
https://www.gridwiseac.org/pdfs/te_framework_report_pnnl-22946.pdf. 
Gridworks. 2018. "The role of distributed energy resources in today's grid transition." Aug. 
https://gridworks.org/wp-content/uploads/2018/09/Grid Lab_Role Of DER_online-1.pdf. 
Guidehouse insights. 2020. Guidehouse Insights Leaderboard: DERMS Vendors. 
https://guidehouseinsights.com/reports/guidehouse-insights-leaderboard-derms-vendors. 
Hawaiian Electric. 2014. "Fast demand response: be a clean, lean, green company." 
https://www.hawaiianelectric.com/documents/products_and_services/demand_response/
HECO_Fast_DR_SALES_Presentation_2014.pdf. 
Holy Cross Energy. 2019. "Electric rate tariff adjustments distribution flexibility program - 
optional." https://www.holycross.com/wp-content/uploads/2019/06/Electric-ServiceTariffs-Rules-and-Regulations-amended-14May2019-CLEAN_a.pdf#page=38. 
IEEE. 2007. "IEEE Guide for Monitoring, Information Exchange, and Control of Distributed 
Resources Interconnected with Electric Power Systems." IEEE Std 1547.3-2007 1-160. 
Ikaheimo, Jussi, Corentin Evens, and Seppo Karkkainen. 2010. "DER Aggregator Business: the 
Finnish case." http://www.ece.hut.fi/enete/DER_Aggregator_Business_Finnish_Case.pdf. 
International Renewable Energy Agency. 2019a. "Aggregators: innovation landscape brief." 
https://www.irena.org/-
/media/Files/IRENA/Agency/Publication/2019/Feb/IRENA_Innovation_Aggregators_20

---


### Page 53

43 
19.PDF?la=en&hash=EB86C1C86A7649B25050F57799F2C0F609894A012016/01/CEE
PR_WP_2016-001.pdf. 
—. 2019b. "Innovation landscape for a renewable power future: solution VI aggregating 
distributed energy resources for grid services." https://irena.org/-
/media/Files/IRENA/Agency/Topics/Innovation-andTechnology/IRENA_Landscape_Solution_06.pdf?la=en&hash=509F4C4D7C052104D8
97063EC6578901FA514184. 
ISO New England. 2020. Administering the wholesale electricity markets. https://www.isone.com/about/what-we-do/three-roles/administering-markets. 
Kristov, Lorenzo. 2014. "DSO and TSO roles and responsibilities in the decentralized energy 
future." Sep. 
https://www.gridwiseac.org/pdfs/workshop_091014/kristov_091114_pres.pdf. 
Li, D, W.-Y. Chiu, and H Sun. 2017. "Chapter 7-demand side management in microgrid control 
systems." Microgrid 203-230. 
Lian, Jianming, H. Ren, Yannan Sun, K. Kalsi, Di Wu, and S. Widergren. 2017. Transactive 
system part II: analysis of two pilot transactive systems using foundational theory and 
metrics. PNNL. 
Loutan, Clyde. 2015. "Briefing on the duck curve and current system conditions." Jul. 
http://www.caiso.com/Documents/Briefing_Duck Curve_Current System ConditionsISOPresentation-July2015.pdf. 
Melton, Ronald B., Kevin P. Schneider, Eric Lightner, Thomas E. Mc Dermott, Poorva Sharma, 
Yingchen Zhang, Fei Ding, et al. 2018. "Leveraging Standards to Create an Open 
Platform for the Development of Advanced Distribution Applications." IEEE Access 
(IEEE) 6: 37361-37370. 
Migden-Ostrander, Janine, John Shenot, Camille Kadoch, Max Dupuy, and Carl Linvill. 2018. 
"Enabling third-party aggregation of distributed energy resources." Feb. 
https://www.raponline.org/wpcontent/uploads/2018/04/enabling_third_party_aggregation_distributed_energy_resource
s2.pdf. 
NERC. 2017. "Distribution energy resources: connection modeling and reliability 
considerations." Feb. 
https://www.nerc.com/comm/Other/essntlrlbltysrvcstskfrc DL/Distributed_Energy_Resou
rces_Report.pdf. 
New York ISO. 2017. "Distributed Energy Resources Market Design Concept Proposal." Dec. 
https://www.nyiso.com/documents/20142/1391862/Distributed-Energy-Resources-2017Market-Design-Concept-Proposal.pdf/122a815f-b767-e67f-0a8f-323e5489c2b1. 
—. 2020. "Manual 2: ancillary service manual." May. 
https://www.nyiso.com/documents/20142/2923301/ancserv.pdf/df83ac75-c616-8c89c664-99dfea06fe2f. 
Open EI. 2020. Definition: distribution management system. 
https://openei.org/wiki/Definition:Distribution_Management_System. 
PJM. 2019. "PJM manual 11: energy & ancillary services market operations." Dec. 
https://www.pjm.com/-/media/documents/manuals/m11.ashx?la=en. 
—. 2020b. "PJM manual 18: PJM capacity market." May. https://www.pjm.com/-
/media/documents/manuals/m18.ashx?la=en.

---


### Page 54

44 
—. 2020a. "PJM manual 36: system restoration." Jun. 
https://pjm.com/~/media/documents/manuals/m36.ashx. 
PJM State & Member Training Dept. 2015. "Reactive reserves and generator D-curves." Jan. 
https://www.pjm.com/-/media/training/nerc-certifications/gen-exammaterials/gof/20160104-reactive-reserves-and-d-curve.ashx?la=en. 
Prinsloo, Gerro, Andrea Mammoli, and Robert Dobson. 2017. "Customer domain supply and 
load coordination: a case for smart villages and transactive control in rural off-grid 
microgrids." Energy 430-441. 
Rahimi, Farrokh., and Sasan Mokhtari. 2014. "A New Distribution System Operator Construct." 
Open Access Technology International, Inc., 
https://www.gridwiseac.org/pdfs/workshop_091014/a_new_dist_sys_optr_construct_pap
er.pdf. 
Schneider Electric. 2019. "Eco Struxure DERMS: providing grid flexibility for all grid edge 
devices." Nov. https://download.schneiderelectric.com/files?p_Doc_Ref=DERMS_SS_11719. 
Science Direct. 2020. Energy management system. 
https://www.sciencedirect.com/topics/engineering/energy-management-system. 
Singaravelan, A., and M. Kowsalya. 2017. "A practical investigation on conservation voltage 
reduction for its efficiency with electric home appliances." Energy Procedia 117: 724730. 
Sun, Y, and B Frew. 2021. Challenges and Research Priorities in United States Wholesale 
Electricity Markets. DOE GMLC. 
Taft, Jeffrey D. 2017. DER telemetry communication architecture for ESOs, DSOs, and system 
operators. Nov. 
https://gridarchitecture.pnnl.gov/media/advanced/DER_Communication_Structure_final_
GMLC.pdf. 
Taft, Jeffrey D., and Angela Becker-Dippmann. 2015. "Grid architecture." Jan. 
https://gridarchitecture.pnnl.gov/media/white-papers/Grid%20Architecture%20%20-
%20DOE%20QER.pdf. 
Taft, Jeffrey D., and Jim Ogle. 2021. "Grid Architecture Guidance Specification for FASTDERMS." 
Taft, Jeffrey D., Kristov, Lorenzo, and Paul De Martini. 2015. "A reference model for 
distribution grid control in the 21st century." Jul. 
https://www.pnnl.gov/main/publications/external/technical_reports/PNNL-24463.pdf. 
Taft, Jeffrey D. 2016. "Architectural Basis for Highly Distributed Transactive Power Grids: 
Frameworks, Networks, and Grid Codes." 
Taft, Jeffrey D, Paul De Martini, and Lorenzo Kristov. 2015. "A Reference Model for 
Distribution Grid Control in the 21st Century." 
Taft, Jeffrey D. 2016. Architectural Basis for Highly Distributed Transactive Power Grids: 
Frameworks, Networks, and Grid Codes. Pacific Northwest National Laboratory. 
Taft, Jeffrey D. 2019. "Grid architecture." IEEE Power & Energy Magazine 18-28. 
Tan, Sen, Josep M. Guerrero, Peilin Xie, Renke Han, and Juan C. Vasquez. 2020. "Brief survey 
on attack detection methods for cyber-physical systems." IEEE System Journal 1-11. 
Thomas, Sharon. 2018. Evolution of the distribution system & the potential for distribution-level 
markets: a primer for state utility regulators. The National Association of Regulatory 
Utility Commissioners.

---


### Page 55

45 
U.S. Department of Energy. 2006. "Benefits of demand response in electricity markets and 
recommendations for achieving them." Feb. 
https://www.energy.gov/sites/prod/files/oeprod/Documentsand Media/DOE_Benefits_of_
Demand_Response_in_Electricity_Markets_and_Recommendations_for_Achieving_The
m_Report_to_Congress.pdf. 
—. 2016. "Distribution automation: results from the smart grid investment grant program." Sep. 
https://www.energy.gov/sites/prod/files/2016/11/f34/Distribution%20Automation%20Su
mmary%20Report_09-29-16.pdf. 
—. 2020b. Grid Architecture. https://gmlc.doe.gov/projects/1.2.1. 
—. 2020a. "Grid modernization: metrics analysis (GMLC 1.1) - Flexibility." Apr. 
https://gmlc.doe.gov/resources/grid-modernization-metrics-analysis-gmlc1.1-flexibility. 
—. 2017b. "Modern distribution grid, vol. II: advanced technology maturity assessment." Mar. 
https://gridarchitecture.pnnl.gov/media/Modern-Distribution-Grid_Volume-II_v1_1.pdf. 
—. 2017a. "Quadrennial energy review: transforming the nation's electricity system: the second 
installment of the QER." Jan. 
https://www.energy.gov/sites/prod/files/2017/02/f34/Quadrennial%20Energy%20Review
--Second%20Installment%20%28Full%20Report%29.pdf. 
—. 2015b. "Quadrennial technology review 2015, chapter 3: enabling modernization of the 
electric power system – technology assessment, flexible and distributed energy 
resources." http://energy.gov/sites/prod/files/2015/09/f26/QTR2015-3D-Flexible-andDistributed-Energy_0.pdf. 
—. 2015a. "Voices of experience: insights into advanced distribution management systems." 
Feb. 
https://www.energy.gov/sites/prod/files/2015/02/f19/Voices%20of%20Experience%20-
%20Advanced%20Distribution%20Management%20Systems%20February%202015.pdf. 
Widergren, Steven E., Jason Fuller, Cristina Marinovici, and Abhishek Somani. 2014. 
"Residential transactive control demonstration." ISGT. Washington, DC, USA: IEEE. 15. 
Xcel Energy. 2019. "Demand-side management Annual status report." Apr. 
https://www.xcelenergy.com/staticfiles/xeresponsive/Company/Rates%20&%20Regulations/Public%20Service%20Company%202
018%20DSM%20Annual%20Status%20Report_FINAL.pdf. 
—. 2016. "Peak partner rewards program." https://www.xcelenergy.com/staticfiles/xeresponsive/Programs%20and%20Rebates/Business/CO-Peak-Partner-Rewards-infosheet.pdf. 
—. 2020. Renewable Energy Options - Residential. 
https://www.xcelenergy.com/programs_and_rebates/residential_programs_and_rebates/re
newable_energy_options_residential.

---


### Page 56

46 
Appendix A 
Entity Definition 
The common entities in distribution grids are briefly introduced and defined. 
Advanced distribution management system (ADMS): an integrated software platform that provides a 
variety of comprehensive distribution grid management functions, such as distribution voltage 
management via volt/volt ampere reactive optimization, conservation voltage reduction, fault and outage 
management, peak demand management, and advanced functions and optimizations considering 
distributed energy resources (U.S. Department of Energy 2015a). 
Aggregator: an entity or agent that aggregates a group of assets or customers to act as a single participant 
in power system and/or power markets (Burger, et al. 2016). Through aggregation, small-scale distributed 
energy resources (DERs) can behave like a sizeable resource from the point of view of the electric grid. 
An aggregator might present the assets under its control as a virtual power plant, where an aggregation of 
dispersed DERs operates like a traditional power plant (International Renewable Energy Agency 2019a). 
Advanced metering infrastructure (AMI): typically refers to the measurement and collection system 
that consists of smart meters, communications networks, and information management systems. Smart 
meter reading data can be remotely accessed and delivered to utilities and customers every 15 minutes or 
even faster (U.S. Department of Energy 2017a). 
Distributed energy resource management system (DERMS): a software-based solution that enhances 
the utility’s network awareness and visibility into distributed energy resources (DERs) and offers a 
number of control functionalities, such as asset monitoring and control, scheduling and dispatch, power 
and voltage control, and resource valuation (U.S. Department of Energy 2015b). A DERMS can also be 
used to monitor and control DER aggregations, forecast DER capabilities, and communicate with other 
enterprise systems and into DER aggregators (EPRI 2016a). In some cases, this functionality is provided 
by an advanced distribution management system. 
Distribution management system (DMS): an operational system that is capable of collecting data from 
sensors and measurement devices; monitoring and analyzing grid conditions; and controlling the 
distribution grid to increase efficiency, mitigate overloads, and optimize power flows (Open EI 2020) 
(U.S. Department of Energy 2017b). 
Distribution operator (DO): an entity that manages and operates the distribution grid. Generally, power 
delivery service quality is maintained by the distribution operator through control systems, such as 
distribution management systems and outage management systems. 
Distribution System Operator (DSO): an entity responsible for balancing supply and demand variations 
at the distribution level and linking the wholesale and retail market agents while maintaining the 
traditional role of the operator as a custodian for distribution system reliability (Rahimi and Mokhtari 
2014). This is an evolving concept, and there is a wide spectrum of organizational models for DSOs 
(Black & Veatch Management Consulting 2020). 
Energy management system (EMS): an automated system that collects measurement data, monitors the 
performance of the transmission system and in some cases primary distribution substations, and controls 
and optimizes system operation through optimizations and contingency analysis (Science Direct 2020).

---


### Page 57

47 
The energy management system is the transmission system’s analog to the distribution management 
system (U.S. Department of Energy 2017b). 
Flexible resource scheduler: an entity proposed in this project that aggregates and manages all 
distributed energy resources in a distribution network to provide firm services in wholesale electricity 
markets and transmission system operations. The geographic scope of an instance of the flexible resource 
scheduler will be the feeders connected to one substation. 
Geographic information system (GIS): a computer system for storing the geographic data of 
transmission and distribution grid equipment, maintaining the grid asset database, and displaying data on 
a map (EPRI 2016b). 
Market operator: an independent organization to administer and organize wholesale electricity markets. 
In the United States, independent system operators typically administer electricity markets and power 
system planning and operation (ISO New England 2020). In this report, the term market operator denotes 
the department that manages electricity markets. Power system planning and operation is beyond the 
responsibility of a market operator. 
Outage management system (OMS): a computer-aided system for power outage identification, outage 
alerts, and service restoration assistance. 
Supervisory control and data acquisition (SCADA): for power distribution application, a system 
capable of collecting data from remote sensors and measurement devices, monitoring distribution system 
status, and performing control actions. 
Scheduling coordinator: an entity that represents market participants such as generators and load-serving 
entities and settles all services and trades related to wholesale electricity markets (California ISO 2020a). 
In this project, the scheduling coordinator is defined as the upstream market coordinator of the applicable 
distribution system, meaning that all market bids of the flexible resource scheduler will be processed by 
the scheduling coordinator before entering wholesale electricity markets. 
Transactive market: a scalable energy market/platform designed for coordinating local energy 
transactions among dispersed distributed energy resources (Grid Wise Architecture Council 2015). Similar 
to the concept of a conventional electricity market, a transactive market also uses the price as the core 
“value signal” for control. 
Transmission system operator (TSO): an entity that coordinates, controls, and monitors the power 
transmission grid (FERC 2020). In the United States, the definition is similar to those of an independent 
system operator (ISO) and regional transmission operator (RTO). The core function of the TSO in a 
wholesale electricity market is to maintain the security and reliability of power system operation. In this 
regard, the TSO service is normally specified in guidelines as part of the electricity market (ENTSO-E 
2020). In this report, we do not further distinguish a TSO from an ISO or an RTO.

---


### Page 58

48 
Appendix B 
Settlement Plans 
Some existing settlement plans used by utilities to recruit distributed energy resources (DERs) for 
participating in demand response programs and/or providing grid services are listed here (U.S. 
Department of Energy 2006). 
1. Traditional price/rate program. In addition to existing rate plans—such as a fixed rate, time-of-use 
rate, or real-time pricing rate (if applicable)—DERs might require a rate reduction for agreeing to 
provide grid services such as demand response. Depending on the capacity and flexibility of DERs, 
customers could choose from a selection of rate programs to fit their needs. If the DERs successfully 
respond to utility dispatch orders, the subscribed rate programs should reduce the energy bills for 
these DER owners. 
2. Net energy metering program. Customers with a sufficient capacity of DERs could feed power back 
to the grid when the generation capability is abundant (e.g., rooftop solar panels producing more 
power than the demand of the customer). The amount of energy that is fed back to the grid will 
reduce the net energy usage, resulting in a reduced energy procurement cost for the customer. 
3. Energy credit/reward program. If DERs can be separately metered, DERs could subscribe to an 
energy credit/reward program for the amount of power generation. The credit can be applied to 
reduce the customers’ energy bills, similar to the net energy metering program, or it can be saved for 
later use or trade to other customers. If the DER generation is renewable—e.g., generated by rooftop 
solar panels—an additional carbon emission credit could apply to reward the customers for generating 
clean energy. 
4. Buyback program. Instead of negotiating with DERs, utilities could post a price/reward for certain 
desired services. DERs that find the posted price acceptable can sign contracts with the utilities and 
agree to provide the specified service when requested to obtain the posted reward/compensation (U.S. 
Department of Energy 2006). 
5. Customized bilateral contract. A customized bilateral contract offers flexible rate plans for DER 
owners to participate in a variety of grid services. The customized contract will specify the technical 
details of DERs, involved grid services, rate plans, and operating protocols. 
As discussed in Section 5.3.2, the flexible resource scheduler offers two DER incentive subscription 
options: contractually obligated and transactive resources. We expect that the DER settlement plans will 
be narrowed to two options in the Federated Architecture for Secure and Transactive Distributed Energy 
Resource Management Solutions (FAST-DERMS): One is a bilateral contract that is widely used for 
DER aggregation, and the other is a real-time pricing scheme that will be implemented for transactive 
resources. The detailed settlement plan design will not be elaborated upon because it is not the focus of 
this FAST-DERMS architecture document.

---


### Page 59

49 
Appendix C 
Grid Services 
This section briefly reviews common transmission and distribution grid services and identifies several 
representative services that could be implemented through the Federated Architecture for Secure and 
Transactive Distributed Energy Resource Management Solutions (FAST-DERMS). More comprehensive 
studies of grid services, which include testing1 and valuation2 of grid services, were undertaken under 
GMLC Projects 1.2.4 and 1.4.2. 
Transmission Grid Services 
A transmission grid connects power generation plants with load centers through long-distance 
transmission infrastructure. Balancing power generation from power plants with the system power 
demand is the major factor that influences the operation and control of transmission grids; thus, most 
transmission grid services are designed to manage power generation and demand variation at different 
timescales. 
Figure C.1 shows the most common transmission grid services and the event speeds of these services 
(U.S. Department of Energy 2017a). Here, energy market participation is included as a grid service.3 At 
different timescales, different tools will be employed to resolve the demand-supply variation. Automatic 
control strategies such as inertial response will kick in at the subsecond level, whereas grid investment 
and expansion through capacity markets and transmission and distribution planning will ensure long-term 
balance between power supply and demand. 
 
Figure C.1 Common bulk grid services and event speeds. Image from (U.S. Department of Energy 
2017a) 
Table C.1 distills the potential transmission grid services shown in Figure C.1 to those that FASTDERMS aims to provide, and it provides a brief review of these services. For each service, we summarize 
the technical requirements that are typically requested by transmission system operators and market 
operators from wholesale electricity market participants. The qualifying distributed energy resources 
(DERs) are identified as the controllable resources that can contribute such services. 
 
1 https://gmlc.doe.gov/projects/1.4.02. 
2 L.C. Markel, S.W. Hadley, P.W. O'connor and A.K. Wolfe, “Valuation Framework for Informing Grid Modernization 
Decisions: Summary, A summary of the principles and process for valuing grid services and technologies,” ORNL/SPR2019/1106, March 2019. 
3 The Federal Energy Regulatory Commission separates energy market operations and ancillary services. See the Energy Primer: 
A Handbook of Energy Market Basics, June 2020, available at https://www.ferc.gov/sites/default/files/2020-05/energyprimer.pdf.

---


### Page 60

50 
Table C.1 Review of Potential Bulk Grid Services for FAST-DERMS 
Service 
Description 
Typical Requirements 
Qualifying 
DERs 
Frequency 
regulation 
Balances power generation with loads and 
maintains system frequency at 60 Hz 
(California ISO 2016) (New York ISO 
2020). The typical frequency regulation 
signal, automatic generation control, is 
updated every 4 seconds. 
Minimum aggregated 
capacity = 0.5 MW 
Minimum regulation capacity 
= 0.1 MW 
Service deployment 
<= 4 seconds 
PV, BESS, EV 
Voltage 
regulation 
Maintains transmission voltages within 
acceptable limits (New York ISO 2020) 
(PJM State & Member Training Dept. 
2015) 
Minimum sustained period = 
15 minutes 
Required to submit P-Q 
curve 
PV, BESS, EV 
Real-time 
scheduling 
(real-time 
energy market) 
Based on actual real-time operations and 
enables participants to alter their dayahead bids (PJM 2019) (California ISO 
2020b). The typical real-time settlement 
interval is 5 minutes. 
Minimum aggregated 
capacity = 0.5 MW 
 
PV, BESS, EV 
Reserve 
(spinning/nonspinning) 
Provides backup generation capacity to 
help maintain power balance and system 
frequency (New York ISO 2020) 
Minimum aggregated 
capacity = 0.5 MW 
Service deployment 
<= 10 minutes 
Minimum run time = 30 
minutes 
PV, BESS 
Flexible 
ramping 
Addresses the uncertainties of renewable 
generation forecast (California ISO 2015a) 
(California ISO 2015b). The typical 
ramping service interval is 5 minutes. 
Minimum aggregated 
capacity = 0.5 MW 
Dispatch interval <= 5 
minutes 
PV, BESS 
Day-ahead 
scheduling 
(day-ahead 
energy market) 
Enables the participant to buy and sell 
energy for the next operating day (PJM 
2019) (California ISO 2020b). The typical 
day-ahead settlement interval is 1 hour. 
Minimum aggregated 
capacity = 0.5 MW 
Dispatch interval <= 1 hour 
PV, BESS, EV, 
building loads 
Demand 
response 
Employs demand curtailment to help 
maintain system balance and reliability; 
also known as emergency demand 
response (GL 2014) (PJM 2019) 
Minimum aggregated 
capacity = 0.5 MW 
Minimum curtailment 
capacity = 0.5 MW 
Service deployment 
<= 30 minutes 
PV, BESS, EV, 
building loads

---


### Page 61

51 
Service 
restoration 
(black start) 
Generating units start up without relying 
on external power and help crank other 
generators and supply loads after a 
blackout (PJM 2020a). 
Capability to self-start 
without outside power 
Capability to maintain 
stability 
Minimum run time = 16 
hours 
PV, BESS 
Capacity 
market 
Long-term product designed to ensure that 
transmission systems have adequate 
resources and capacity to meet reliability 
requirements (PJM 2020b) 
Minimum aggregated 
capacity >= 0.5 MW 
PV, BESS, EV, 
building loads 
Distribution Grid Services 
The distribution grid is responsible for delivering electricity from local substations to dispersed end users 
in a relatively small area compared to a transmission grid service area. Because the power supply-demand 
balance is primarily managed by generators and the transmission grid, distribution grids generally focus 
more on maintaining power delivery service quality. In this section, we emphasize distribution grid 
services in the operation and control stage because the long-term investment planning issues are similar to 
those in transmission grid services. 
Traditional distribution grid control is based on three functions: power flow management, volt/volt 
ampere reactive (VAR) regulation, and demand response. 
• Power flow management: 
– 
The most significant feature of a distribution grid is its unbalanced three-phase power flow. 
Unbalanced power flows have negative impacts on power quality and equipment life span, and 
thus they should be closely monitored throughout the distribution grid. Power flow management 
has traditionally been accomplished through network reconfiguration, an approach that modifies 
distribution grid topology by operating switching devices (e.g., switches, circuit breakers, 
reclosers, and relays), most of which has been done manually. Network reconfiguration can be 
used to balance loads and regulate distribution voltages, and it is also an important solution to 
improving distribution grid reliability by reconnecting outage areas to other normal branches or 
feeders when faults happen. Load balancing service can also be provided by power electronic 
devices and reactive power controllers. 
– 
An emerging, related topic is reverse power flow management. The fast-growing integration of 
DERs introduces reverse power flows in distribution grids, which could cause malfunctions of 
traditional protection relays. Reverse power flow management service can also be provided by 
switching devices. 
• Voltage regulation: 
– 
The voltage profile plays a key role in maintaining power delivery service quality. The service 
voltage magnitude must be kept within an acceptable range for all end users. Traditionally, 
voltage has been controlled through regulators and serial line drop compensators, some of which 
are automatic and some of which are manually adjusted. Reactive power has been mainly 
controlled by switching capacitors in and out of the circuit. More recently, integrated volt/VAR 
controls and optimizations have been used so that voltage regulators, on-load tap changers, 
capacitors, and other volt/VAR control devices (such as inverters) can be coordinated to

---


### Page 62

52 
maximize the improvement in distribution voltages while minimizing the switching operations of 
these devices (U.S. Department of Energy 2016) (Argonne National Laboratory 2017). 
• Peak load management: 
– 
Load management allows distribution utilities to reduce demand for electricity during peak usage 
time, which can in turn reduce costs by purchasing wholesale electricity at a lower price and 
improve distribution system reliability. Conservation voltage reduction is another important 
distribution voltage management application that reduces feeder voltage levels through on-load 
tap changers or through voltage regulators to reduce the total power consumption of the 
distribution grid. Conservation voltage reduction can also be regarded as a distribution grid peak 
load management service or a demand response service (Singaravelan and Kowsalya 2017). 
Currently, distribution grid services are generally managed by distribution system operators (DSOs) using 
utility-owned or contracted devices, such as voltage regulators and large battery energy storage systems; 
thus, market-based financial rewards are typically not applicable to distribution grid services. Although 
providing distribution grid services might not bring revenue to DER owners, improving distribution grid 
operational flexibility and reliability will in turn benefit DER owners. In addition, some distribution 
utilities provide incentives in order to recruit DER customers to contribute to voltage and power 
management (Holy Cross Energy 2019). Also, distribution-level energy markets are an emerging topic 
that has already attracted attention from utilities (Thomas 2018); therefore, in this project, the DERs are 
expected to use their flexibility through FAST-DERMS to provide distribution grid services and to meet 
the control objectives of DSOs.

---


### Page 63

53 
Appendix D 
Specifications Listed in Reference Grid Architecture 
FAST-DERMS aligns with the following specifications that are listed in the reference grid architecture 
document (Taft and Ogle 2021): 
“ 1.1 Distribution providers have a total Distribution System Operator role. 
1.2 The DSO is responsible for managing distribution assets to meet an agreement with 
the TSO as to power and energy flows at the transmission/distribution interface 
substations. 
1.3 The DSO is responsible for managing DER and power flows to/from and inside its 
distribution service area to maintain distribution reliability and meets its 
responsibilities to the TSO at the T/D interface, including power and energy flows 
across that interface, and management of volatility arising from distribution 
connected elements. 
1.4 The TSO limits its grid observability to the Bulk Power System up to the T/D 
interface; it does not obtain grid state or operational data from DER devices or 
aggregators. 
1.5 The TSO does not bypass the DSO to dispatch DER directly. 
1.6 DER aggregators and other third-party energy services providers do not bypass the 
DSO to deal directly with the TSO. 
2.3 Coordinate DER inverters with grid control to avoid conflicts at the distribution 
secondary level and to provide regulation service. 
4.1 Use the Laminar Coordination Framework to develop specific Laminar Networks 
that correspond to the actual physical system being coordinated. 
4.2 Follow the Framework to define logical information flows for the coordination 
process. 
4.3 Maintain Laminar structure, even when DER are being coordinated via aggregators 
or other third parties. 
4.4 Third parties can host Laminar nodes on behalf of the DER they aggregate. 
4.5 Connect aggregators to the appropriate DSO to participate in the coordination data 
flows for the DER they manage in the service area of the DSO. Aggregators and 
other third parties may connect to more than one DSO if they have DER in more 
than one DSO service area (refer to Specification 1). 
4.7 Use Laminar structure to define building-to-grid and microgrid-to-grid interfaces. 
5.1 Use Laminar coordination structure to coordinate BTM and secondary-connected 
storage with other grid resources and devices. This applies to third party-operated 
storage as well as owner-operated storage. 
5.2 BTM/secondary-connected storage coordination elements or functions must fit into a 
larger Laminar coordination framework so that storage coordination does not 
conflict with other distribution grid control devices and systems.

---


### Page 64

54 
5.3. If BTM/secondary-connected storage is to be used as a bulk power system resource, 
the coordination mechanism must not introduce coordination framework gapping or 
tier bypassing and must not enable hidden coupling, including via markets. 
7.3 DER management must include access to real time circuit topology state, including 
grid fragment topology. 
8.3 Provide communication connectivity that supports both device-to-control center 
communication and peer-to-peer communications, including Laminar Network 
coordination communications. 
9.3 Consider the use of resilience as a cyber defense, instead of relying only on IT-type 
defenses. 
10.2.2 Use structure for coordination and control that is consistent with Laminar 
Coordination Framework and logical energy networks (LENs). 
10.2.3 Plan for faster action near the edge, i.e., at the segment level, with time frame of 
action slowing as one moves upward the structure. 
10.2.4 Accommodate DER at any level in the structure. 
10.3.1 Use Laminar structure for organizing EV charging. 
10.3.2 Recognize the effect of transportation infrastructure networks (roadways) as 
related to the topology of the electric distribution system. 
10.4.1 Sensing for distribution grid protection and control uses the observability platform 
structure and either the distributed intelligence platform structure or the Laminar 
coordination domain structure. 
10.4.2 Sensors may be shared across multiple protection and control applications. 
10.4.3 Direct sensor-to-local application data flows are permitted to provide low latency. 
Sensor data does not have to flow to a remote data store or broker first.”

---


### Page 65

National Renewable Energy Laboratory 
15103 Denver West Parkway 
Golden, CO 80401 
303-275-3000 • www.nrel.gov 
https://gmlc.doe.gov

---
