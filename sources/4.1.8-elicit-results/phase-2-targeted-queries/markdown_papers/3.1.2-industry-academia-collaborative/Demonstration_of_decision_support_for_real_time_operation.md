# Demonstration of decision support for real time operation

## Paper Metadata

- **Filename:** Demonstration of decision support for real time operation.pdf
- **DOI:** None
- **Authors:** Not available
- **Year:** Not available
- **Journal/Venue:** Not available
- **URL:** Not available
- **Extraction Date:** 2025-06-03T15:04:05.328323
- **Total Pages:** 44

## Abstract

Abstract not available from BibTeX metadata.

## Keywords

Keywords not available from BibTeX metadata.

---

## Full Text Content



### Page 1

General rights 
Copyright and moral rights for the publications made accessible in the public portal are retained by the authors and/or other copyright 
owners and it is a condition of accessing publications that users recognise and abide by the legal requirements associated with these rights. 
 
 Users may download and print one copy of any publication from the public portal for the purpose of private study or research. 
 You may not further distribute the material or use it for any profit-making activity or commercial gain 
 You may freely distribute the URL identifying the publication in the public portal 
 
If you believe that this document breaches copyright please contact us providing details, and we will remove access to the work immediately 
and investigate your claim. 

Downloaded from orbit.dtu.dk on: 6 03, 2025
Demonstration of decision support for real time operation
Catterson, Victoria ; MCarthur, Stephen; Chen, Minjiang; Pertl, Michael; Reigstad, Tor Inge ; Ciavarella,
Roberto; Di Somma, Marialaura; Riaño, Sandra; Marinelli, Mattia; Zuelli, Roberto
Publication date:
2018
Document Version
Publisher's PDF, also known as Version of record
Link back to DTU Orbit
Citation (APA):
Catterson, V., MCarthur, S., Chen, M., Pertl, M., Reigstad, T. I., Ciavarella, R., Di Somma, M., Riaño, S.,
Marinelli, M., & Zuelli, R. (2018). Demonstration of decision support for real time operation. ELECTRA
Consortium.

---


### Page 2

Project No. 609687 
FP7-ENERGY-2013-IRP 

WP 8 
Future Control Room Functionality 

Deliverable 8.2 
Demonstration of decision support for real time 
operation 

02/02/2018 

ELECTRA 
European Liaison on Electricity Committed 
Towards long-term Research Activities for Smart 
Grids

---


### Page 3

Project ID: 609687 
 
02/02/2018 Page 2 of 43 
ID&Title 
D8.2 
Demonstration of decision support for real 
time operation 
Number of pages: 
43 
Short description (Max. 50 words): 
ELECTRA Deliverable 8.2 reports on the demonstration of decision support within the future 
control room in light of voltage and frequency control in the 2030+ power system. The 
decision support must identify key threats and vulnerabilities, and propose and prioritise 
appropriate interventions. 
Version 
Date 
Modification’s nature 
V0.1 
28/07/2017 
First Draft 
V0.02 
02/08/2017 
Revised Draft 
V0.03 
07/08/2017 
Final Draft 
V1.00 
27/09/2017 
Under review 
V2.00 
02/02/2018 
Released 
Accessibility 
 PU, Public 
 PP, Restricted to other program participants (including the Commission Services) 
 RE, Restricted to other a group specified by the consortium (including the Commission 
Services) 
 CO, Confidential, only for members of the consortium (including the Commission 
Services) 
If restricted, please specify here 
the group: 
 
Owner / Main responsible: 
Task T8.3 Leader: 
Stephen Mc Arthur 
(USTRATH) 
 
Reviewed by: 
Technical Project Coordinator: 
 
Helfried Brunner (AIT) 
Carlo Tornelli (RSE) 
01/02/2018 
Final Approval by: 
ELECTRA Technical Committee 
TOQA appointed Reviewer: 
Luciano Martini 
02/02/2018

---


### Page 4

Project ID: 609687 
 
02/02/2018 Page 3 of 43 
Authors 
Name 
Last Name 
Organization 
Country 
Victoria 
Catterson 
USTRATH 
UK 
Stephen 
Mc Arthur 
USTRATH 
UK 
Minjiang 
Chen 
USTRATH 
UK 
Michael 
Pertl 
DTU 
DK 
Tor Inge 
Reigstad 
SINTEF 
NO 
Roberto 
Ciavarella 
ENEA 
IT 
Marialaura 
Di Somma 
ENEA 
IT 
Sandra 
Riaño 
TECNALIA 
SPAIN 
Mattia 
Marinelli 
DTU 
DK 
Roberto 
Zuelli 
RSE 
IT

---


### Page 5

Project ID: 609687 
 
02/02/2018 Page 4 of 43 
Copyright 
© Copyright 2013-2018 The ELECTRA Consortium 
Consisting of: 
Coordinator 
 
Ricerca Sul Sistema Energetico – (RSE) 
Italy 
Participants 
 
Austrian Institute of Technology Gmb H - (AIT) 
Austria 
Vlaamse Instelling Voor Technologisch Onderzoek N.V. - (VITO) 
Belgium 
Belgisch Laboratorium Van De Elektriciteitsindustrie - (LABORELEC) 
Belgium 
Danmarks Tekniske Universitet - (DTU) 
Denmark 
Teknologian Tutkimuskeskus - (VTT) 
Finland 
Commissariat A L’Energie Atomique Et Aux Energies Alternatives - (CEA) 
France 
Fraunhofer-Gesellschaft Zur Förderung Der Angewandten Forschung E.V – (IWES) 
Germany 
Centre For Renewable Energy Sources And Saving - (CRES) 
Greece 
Agenzia Nazionale per Le Nuove Tecnologie, L´Energia E Lo Sviluppo Economico 
Sostenibile - (ENEA) 
Italy 
Fizikalas Energetikas Instituts - (IPE) 
Latvia 
SINTEF Energi AS - (SINTEF) 
Norway 
Instytut Energetyki - (IEN) 
Poland 
Instituto De Engenharia De Sistemas E Computadores Do Porto - (INESC_P) 
Portugal 
Fundacion Tecnalia Research & Innovation - (TECNALIA) 
Spain 
Joint Research Centre European Commission - (JRC) 
Belgium 
Nederlandse Organisatie Voor Toegepast Natuurwetenschappelijk Onderzoek – (TNO) Netherlands 
Turkiiye Bilimsel Ve Teknolojik Arastirma Kurumu - (TUBITAK) 
Turkey 
University Of Strathclyde - (USTRATH) 
UK 
European Distributed Energy Resources Laboratories (DERlab) 
Germany 
Institute for Information Technology at University of Oldenburg (OFFIS) 
Germany 

This document may not be copied, reproduced, or modified in whole or in part for any 
purpose without written permission from the ELECTRA Consortium. In addition to such 
written permission to copy, reproduce, or modify this document in whole or part, an 
acknowledgment of the authors of the document and all applicable portions of the 
copyright notice must be clearly referenced. 
 
All rights reserved. 
This document may change without notice.

---


### Page 6

Project ID: 609687 
 
02/02/2018 Page 5 of 43 
Executive summary 
The present report considers the need for decision support systems (DSS) within the future control 
room of 2030+, in the context of the ELECTRA [1] Web of Cells (Wo C) network architecture. The 
main aim is to identify critical decisions that must be made during the operation of a cell within the 
Wo C, and to propose and demonstrate methods of supporting these decisions. The presented 
work is heavily based on the visualisation scenarios reported in ELECTRA D8.1 [2]. While D8.1 
considers particular scenarios from initiating incident through to scenario resolution, and proposes 
new analytics and visualisations to assist the operator in resolving the situation, D8.2 focuses in 
detail on one or more decision points within these scenarios. 
By building on the scenarios in D8.1, the research reported in this Deliverable provides novel 
solutions to a range of problems tackled from a Web of Cells functionality viewpoint. This extends 
to the consideration of autonomy and interaction with neighbouring cells absent in other research 
projects. The drive is to assess a range of solutions that can be combined within the Wo C control, 
automation and decision support platform. The assessment of transient stability margins and 
critical clearing time, imbalance in tie line flow, loss of mains, over voltage curtailment and 
procurement of reserves (following single and double frequency deviations) are the scenarios. 
Within these, the learning arising includes: 
● The casting of the problem for a Wo C implementation, drawing out the unique opportunities 
to solve the issues within this context; 
● Enhanced use of Optimal Power Flow within a Wo C context; 
● Effective use of storage to support Wo C operation; 
● Knowledge based and constraint satisfaction techniques; and, 
● Interaction between the operator and automated systems within the Wo C. 
 
All of the above are linked and consider from a decision support perspective i.e. how would the 
system inform operators and take control as necessary. 
Chapter 1 introduces some context and definitions to explain the need for decision support within 
the future control scenarios. Chapter 2 describes in detail the decision points where a DSS can be 
applicable, what the key actions are that could be taken, and which metrics are important for 
prioritisation of the actions. Chapter 3 presents the techniques and methods used for 
implementation of the decision support demonstrators, along with results of testing. Chapter 4 
concludes with the learning and new knowledge derived from the design and specification of these 
demonstrators.

---


### Page 7

Project ID: 609687 
 
02/02/2018 Page 6 of 43 
Terminologies 
Abbreviations 
BESS 
Battery Energy Storage Systems 
BRC 
Balance Restoration Control 
BSC 
Balance Steering Control 
CBS 
Critical Bus Screening 
CCGT 
Combined Cycle Gas Turbines 
CCT 
Critical Clearing Time 
CSP 
Constraint Satisfaction Problem 
DER 
Distributed Energy Resource 
DG 
Distributed Generation 
DMS 
Distribution Management System 
DSS 
Decision Support System 
ELECTRA IRP 
European Liaison On Electricity Committed Towards Long-Term 
Research Activity Integrated Research Programme 
ESB 
Energy Safety Band 
FCC 
Frequency Containment Control 
KB 
Knowledge Base 
MOC 
Merit Order Collection 
MOD 
Merit Order Decision 
MS 
Milestone 
OPF 
Optimal Power Flow 
PMU 
Phasor Measurement Unit 
PPVC 
Post-Primary Voltage Control 
RES 
Renewable Energy Sources 
RDSS 
RSE Decision Support System 
SCADA 
Supervisory Control and Data Acquisition 
SG 
Synchronous Generator 
SLD 
Single Line Diagram 
SOC 
State Of Charge 
SOR 
Speed Of Response 
TD 
Time Domain 
UDSS 
USTRATH Decision Support System 
Wo C 
Web-of-Cells

---


### Page 8

Project ID: 609687 
 
02/02/2018 Page 7 of 43 
Table of contents 
1. Introduction and methodology ................................................................................................... 10 
1.1 
Decision support for human operators within a Web of Cells .......................................... 10 
1.2 
ELECTRA Control Room Scenarios ................................................................................ 11 
1.3 
Decision support design methodology ............................................................................ 11 
2 
Requirements and specification of decision support functions ............................................... 12 
2.1 
Decision support during a single frequency deviation event (USTRATH_1) .................... 12 
2.1.1 
Functional requirements for the procurement of new BRC reserves after a frequency 
event (USTRATH_DSS_1) ....................................................................................... 12 
2.1.2 
Functional requirements for the BSC replacement of BRC deployed reserves 
(USTRATH_DSS_4) ................................................................................................. 13 
2.1.3 
Functional requirements for the BESS energy restoration after a frequency deviation 
event (ENEA_DSS_1) .............................................................................................. 13 
2.2 
Decision support during two simultaneous frequency events (USTRATH_2) .................. 14 
2.2.1 
Functional requirements to the response to a frequency event larger than the BRC 
reserves can handle (USTRATH_DSS_2) ................................................................ 14 
2.2.2 
Functional requirements for the response to an emergency request from a 
neighbouring cell for BRC support (USTRATH_DSS_3) ........................................... 14 
2.2.3 
Functional requirements for the response to a frequency event due to the loss of a tieline (RSE_DSS_1) .................................................................................................... 15 
2.3 
Decision support for transient stability preventive control (DTU_2) ................................. 15 
2.3.1 
Functional requirements for transient stability preventive control (DTU_DSS_1) ...... 15 
2.4 
Decision support for management of inter-cell loop flows (DTU_4) ................................. 16 
2.4.1 
Requirements 
and 
functionality 
for 
management 
of 
inter-cell 
loop 
flows 
(SINTEF_DSS_1) ..................................................................................................... 16 
2.5 
Decision support for over/under voltage (TEC_2) ........................................................... 17 
2.5.1 
Functional requirements for the response to an over/under voltage event 
(INESC_P_DSS_1) .................................................................................................. 17 
3 
Decision support system design and implementation ............................................................. 18 
3.1 
Decision support during a single frequency deviation event (USTRATH_1) .................... 18 
3.1.1 
Decision support system design overview for frequency control ............................... 18 
3.1.2 
Decision support for the procurement of new BRC reserves after a frequency event 
(USTRATH_DSS_1) ................................................................................................. 18 
3.1.3 
Decision 
support 
for 
the 
BSC 
replacement 
of 
BRC 
deployed 
reserves 
(USTRATH_DSS_4) ................................................................................................. 20 
3.1.4 
Decision support for BESS energy restoration after a frequency deviation event 
(ENEA_DSS_1) ........................................................................................................ 21 
3.2 
Decision support during a two frequency deviations event (USTRATH_2) ...................... 25

---


### Page 9

Project ID: 609687 
 
02/02/2018 Page 8 of 43 
3.2.1 
Decision support for the response to a frequency event larger than BRC reserves can 
handle (USTRATH_DSS_2) ..................................................................................... 25 
3.2.2 
Decision support for the response to an emergency request from a neighbouring cell 
for BRC support (USTRATH_DSS_3)....................................................................... 26 
3.2.3 
Decision support for the response to a frequency event due to the loss of a tie-line 
(RSE_DSS_1) .......................................................................................................... 26 
3.3 
Decision support system for transient stability preventive control (DTU_2) ..................... 30 
3.3.1 
Decision support for transient stability preventive control (DTU_DSS_1) .................. 30 
3.4 
Decision support system for management of inter-cell loop flows (DTU_4) ..................... 33 
3.4.1. Decision support for management of inter-cell loop flows (SINTEF_DSS_1) ................ 33 
3.5 
Decision support system for over/under voltage (TEC_2) ............................................... 37 
3.5.1 
Decision support for the response to an over/under voltage event NESC_P_DSS_1 37 
4 
Conclusions ........................................................................................................................... 41 
5 
References ............................................................................................................................ 42 
6 
Disclaimer .............................................................................................................................. 43

---


### Page 10

Project ID: 609687 
 
02/02/2018 Page 9 of 43 
List of figures and tables 
 
Figure 3-1: UDSS architecture ...................................................................................................... 18 
Figure 3-2: Cell diagram of USTRATH_DSS_1 case study ........................................................... 20 
Figure 3-3: Flow-chart of the decisional logic for ENEA_DSS_1 ................................................... 22 
Figure 3-4: Cell diagram of ENEA_DSS_1 case study .................................................................. 23 
Figure 3-5: Example of network with the loss of a tie-line .............................................................. 27 
Figure 3-6: RDSS architecture ...................................................................................................... 28 
Figure 3-7: Wo C in N conditions ................................................................................................... 28 
Figure 3-8: Wo C in N-1 conditions and no violations ..................................................................... 28 
Figure 3-9: Wo C in N-1 conditions and violations .......................................................................... 29 
Figure 3-10: Wo C in N-1 conditions and change of set-points ....................................................... 29 
Figure 3-11: Network conditions after the fault clearing ................................................................. 30 
Figure 3-12: Flowchart of the transient stability preventive control approach. ................................ 31 
Figure 3-13: New England test system with indication of associated cost functions ...................... 32 
Figure 3-14: CCTs and active power set-points for initial condition and after successful dispatch . 33 
Figure 3-15: Topology of the Pan-European Single Reference Power System. ............................. 35 
Figure 3-16: Initial load flow (a), load flow after power reduction in SG1.10 (b) and unscheduled 
power flow after power reduction in SG1.1 (c) ............................................................................... 36 
Figure 3-17: Result of updated OPF in Cell 1 and 2 (a), actual load flow after updated OPF (b) and 
unscheduled power flow after updated OPF (c) ............................................................................ 37 
Figure 3-18: Voltage Control Algorithm ......................................................................................... 39 
Figure 3-19: - Portuguese MV Network ......................................................................................... 39 
Figure 3-20: Voltage values in some nodes of the considered Portuguese network ...................... 40 
Figure 3-21: Total losses of the considered Portuguese distribution system ................................. 40 

Table 1-1: Subset of the scenarios defined in ELECTRA D8.1 and adopted in D8.2 ..................... 11 
Table 3-1: USTRATH_DSS_1 case study result ........................................................................... 20 
Table 3-2: USTRATH_DSS_4 case study result ........................................................................... 21 
Table 3-3: BESS MOC in ENEA_DSS_1 ...................................................................................... 23 
Table 3-4: BESS MOD in ENEA_DSS_1 ...................................................................................... 24 
Table 3-5: Information provided to the Cell Operators in ENEA_DSS_1 ....................................... 24 
Table 3-6: USTRATH_DSS_2 case study result ........................................................................... 26 
Table 3-7: Comparison of measured values and results from power flow on nodes nearby SG1.10
 ..................................................................................................................................................... 36

---


### Page 11

Project ID: 609687 
 
02/02/2018 Page 10 of 43 
1. Introduction and methodology 
1.1 Decision support for human operators within a Web of Cells 
This report discusses the need for Decision Support Systems (DSS) for operators of a network cell 
within the future Web of Cells (Wo C) architecture developed within the ELECTRA IRP [1]. The aim 
is to demonstrate specific scenarios where DSS are particularly useful, due to the complexity of the 
control options available to such an operator. The main questions addressed in this report are: 
● Which decisions are particularly critical for the cell operator? 
● What are some of the available control actions that could be taken? 
● How can such actions be prioritised and compared against each other? 
● How can alternative plans be presented to the operator, and how can they reprioritise the 
control actions? 
The work is heavily based on the visualisation scenarios developed in in previous activities and 
reported in D8.1 [2]. The present document considers specific critical scenarios in detail, from 
initiating incident through to scenario resolution, and proposes new analytics and visualisations to 
assist the operator in resolving the situation. The aim is to focus in detail on one or more decision 
points within these scenarios, and explore the questions above. 
As outlined in D8.1, “the roles and activities in the future control centres will evolve with respect to 
the manual switching, dispatching and restoration functions currently active. The control centre 
operators will supervise on the power system and intervene - when necessary - thanks to the 
maturation and wide scale deployment of flexible controls.” Part of the decision support research is 
to help characterise what the role of an “operator” will be in the future. In the first instance, we 
consider someone with responsibility for the cell. However, the solutions could be applied to 
provide decision support for those overseeing the full Web of Cells, where additional high level 
supervisory support could be added to the visualisations and automation provide per cell. 
A decision point is characterised as being a situation where there are various actions that could be 
taken, and it is not a trivial task to prioritise which is better or worse than others. One example 
would be where there is a need to procure balancing support from a neighbouring cell, but multiple 
neighbours can provide sufficient spare resources. The operator must decide whether to take 
support from a single neighbour, some support from each neighbour, or whether to manage local 
load, and how much in each case. There are various metrics which can help to prioritise the 
choices, such as speed of response of the resource, and tie-line constraints. In this context, the 
DSS can construct a plan to restore cell balance, which comprises a sequence of actions (such as 
requests to neighbours and local signals) to achieve the plan. 
The focus is on an environment where the operator will fully delegate decisions to the DSS, and be 
informed of the status and stability of the network. It is envisaged that there will be a mode 
whereby the operator can take manual decisions at any point, without necessarily having to follow 
the plan(s) proposed by the DSS. However, for time-critical decisions where an action must be 
taken within a certain window the fully automated mode of the DSS will be able to independently 
implement the highest priority plan. A key aspect of the research is determining the decision 
support to drive the appropriate balance of interaction between an operator and the automated 
control system. 
The DSS is conceived to be a powerful advance on typical control approaches through its abilities 
for gathering data from neighbouring cells, its intelligent reasoning, and its proactive operation.

---


### Page 12

Project ID: 609687 
 
02/02/2018 Page 11 of 43 
1.2 ELECTRA Control Room Scenarios 
A number of control room scenarios have been developed in which operators must have visibility of 
and take action to mitigate critical issues. A subset of these scenarios were taken forward to 
detailed study, and those selected allowed the best combination of novel decision making and 
reasoning functionality linked to complex issues that would need to be handled by the control 
room. These covered transient stability, inter-cell loop flows, frequency management and voltage 
control. The table below briefly summarises these detailed scenarios, as the starting point for 
examining decision support requirements. 
Table 1-1: Subset of the scenarios defined in ELECTRA D8.1 and adopted in D8.2 
Scenario name 
Brief description 
Transient stability preventive control 
(DTU_2) 
Initiating incident: Insufficient transient stability margin Critical 
Clearing Time (CCT) 
Potential actions: Dispatch of local generators; request for 
neighbouring cell support 
Inter-cell loop flows (DTU_4) 
Initiating incident: Power over a tie-line exceeds/undershoots 
its contracted value 
Potential actions: Control loads/generators to manage power 
flow; troubleshoot the cause; take action to resolve the cause 
Proactive operation of Post-Primary 
Voltage Control (PPVC) (TEC_2) 
Initiating incident: Timed repeated trigger 
Potential actions: Detect voltage deviations from forecast, 
activate PPVC reserves 
Single frequency deviation event 
(USTRATH_1) 
Initiating incident: Loss of generation/increase in load 
Potential actions: Procurement of replacement reserves 
Two frequency deviation events 
(USTRATH_2) 
Initiating incident: Two losses of generation/increases in load 
happening almost simultaneously. Loss of a tie-line. 
Potential actions: Procurement of sufficient reserves 
 
1.3 Decision support design methodology 
The methodology for developing decision support demonstrators was as follows: 
1. Develop the requirements and functional specification for decision support. 
a. Select one of the scenarios defined in D8.1 (as above) for close study. 
b. Identify one or more decision points within the scenario sequence diagrams. For 
each decision point, identify: 
i. What decision does the operator have to make? 
ii. What are some of the alternative actions that could be taken? 
iii. What is the intended/successful outcome? 
c. For each decision point identified above, determine what metrics are important for 
selecting between alternative actions to resolve the decision (i.e. what makes one 
plan “better” than another?). Consider how to select the most suitable metrics.

---


### Page 13

Project ID: 609687 
 
02/02/2018 Page 12 of 43 
2. Based on the functional specification, design the decision support system. 
a. Select an appropriate tool or approach for implementing the DSS (e.g. constraint 
satisfaction, optimization methods, case based reasoning). 
b. Implement and test “off-line”, i.e. with historical, simulated, or synthetic data. 
2 Requirements 
and 
specification 
of 
decision 
support 
functions 
The primary difference between the DSS functions in this work, compared to other research, is the 
Wo C context. The decision support needs to accommodate the automation and interactions 
required for the operation of a web of cells. 
This section presents the outcomes of step 1 of the methodology presented in section 1.3. For 
each of the control room scenarios selected for detailed study, one or more decision points have 
been identified. These are given codes for ease of reference (such as USTRATH_DSS_1). Each 
decision point is analysed for its required functionalities, which provide a specification of the 
decision support systems implemented in Chapter 3. 
2.1 Decision support during a single frequency deviation event 
(USTRATH_1) 
The scenario USTRATH_1 involves a sudden change in system balance, which causes the 
frequency to deviate outside of operational limits. It is assumed that the deviation can be mitigated 
by the Balance Restoration Control (BRC) reserves previously procured during the planning phase 
of operation, and therefore the Wo C control systems will automatically return the frequency within 
operational limits. 
This scenario has three key decision points where the operator can be involved: 
● Procurement of new BRC reserves after a frequency event; 
● Balance Steering Control (BSC) replacement of BRC deployed reserves; 
● Battery Energy Storage Systems (BESS) energy restoration after a frequency deviation 
event. 
2.1.1 Functional requirements for the procurement of new BRC reserves after a 
frequency event (USTRATH_DSS_1) 
After Frequency Containment Control (FCC) has operated to contain the frequency deviation and 
BRC has operated to restore the frequency, the cell may need to replenish the BRC reserves in 
case of a future event. The Wo C concept includes a periodic planning phase, where neighbouring 
cells can negotiate to provide each other support in case of events during real time operation. If the 
USTRATH_1 scenario occurs very shortly after the previous planning phase, the cell operator may 
wish to procure new reserves to mitigate against a further loss of generation. However, if there is a 
very short period before the next scheduled planning phase, the operator may prefer to take the 
risk of operating with depleted reserves, instead of procuring further (potentially costly) reserves. 
In this case, the decision support system aims to address the question: what reserve should be 
procured for BRC? Some alternative actions that could be taken include procuring no reserves, 
slow acting reserves (e.g. combined cycle gas turbines - CCGT), fast acting reserves (e.g. Hydro), 
or demand response. The cost will be a factor in the prioritisation of resources, but not the primary 
driver (for example, CCGT may be cheaper than Hydro, but a fast response is needed to restore

---


### Page 14

Project ID: 609687 
 
02/02/2018 Page 13 of 43 
frequency). A successful outcome would be when the operator is satisfied that sufficient reserves 
have been procured for BRC for the remainder of the real time operation period. 
The metrics that are taken into account when prioritising these actions are: time remaining until 
next planning phase, available reserves within its own cell and neighbouring cells with capacity, 
speed of response, cost of reserves and location of reserves (own and neighbour resources may 
be preferable to neighbour-of-neighbour resources), and tie-line operation margin. 
2.1.2 Functional requirements for the BSC replacement of BRC deployed reserves 
(USTRATH_DSS_4) 
When BRC has completed its operation to restore frequency within limits, BSC takes over to 
optimise the mix of generation and demand management. As the reserves used at the BRC stage 
are fast acting and therefore expensive, the target of BSC is to replace these reserves with more 
economical choices. But the most economical solution is not necessarily the best solution. 
In this case, the decision support system aims to address the question: how to replace the 
deployed reserves with “better” sources? Some alternative actions that could be taken include 
making no changes to the generation/load profile, or substituting fast-acting generation with slower 
start up generation. A successful outcome would be any expensive BRC deployed reserves being 
replaced with less expensive options. 
The metrics that are taken into account when prioritising these actions are: available reserves from 
own cell and neighbouring cells with capacity, speed of response, cost and location of resources 
and tie-line operation margin. 
2.1.3 Functional requirements for the BESS energy restoration after a frequency 
deviation event (ENEA_DSS_1) 
When a sudden system imbalance occurs with a divergence of the frequency from the nominal 
value, BESS within the cell (one or more) can be used to provide the energy required for the 
restoring process. A “safety energy band” is defined for each BESS system within the cell in order 
to ensure the necessary power for the stability control. 
After reaching the stability, the BRC brings the State of Charge (SOC) of the BESS into their safety 
energy range by slow charging or discharging operations. In particular, the cell operator must 
conveniently set the charging/discharging currents to bring SOC more quickly again within their 
safety energy range. However, the cell operator has to ensure currents are not too high in order to 
preserve the stability of the whole system, through an automated control system. Therefore, the 
cell operator requires DSS support to decide on the following issues: 
● How much "energy restoration time" is necessary for each BESS to return within the safety 
energy range? 
● To evaluate the energy restoration time, the DSS must know the SOC for each BESS. 
Then, the cell operator can decide to modify the charging/discharging current, by choosing 
the appropriate value. 
● Which are the alternative actions that could be taken to bring the SOC of the BESS back in 
their safety energy range? 
If the cell does not have spare capacity, the DSS can consider using the support of the 
neighbouring cells. The metrics which could take into account when prioritizing these actions are 
the cost of the reserves and the location of resources.

---


### Page 15

Project ID: 609687 
 
02/02/2018 Page 14 of 43 
2.2 Decision support during two simultaneous frequency events 
(USTRATH_2) 
The scenario USTRATH_2 involves two almost simultaneous events which disturb the system 
balance. It is assumed that the combined effect of the events is more significant than the BRC 
reserves can mitigate. An alternative abnormal event that may imply the loss of the system stability 
is the loss of a tie-line. Therefore, further actions must be taken to procure emergency support and 
return the frequency within the operational margin. 
This scenario has three key decision points where the operator can be involved: 
● Response to a frequency event larger than the BRC reserves can handle; 
● Response to an emergency request from a neighbouring cell for BRC support; 
● Response to a frequency event due to the loss of a tie-line. 
2.2.1 Functional requirements to the response to a frequency event larger than the 
BRC reserves can handle (USTRATH_DSS_2) 
During scenario USTRATH_2, a combination of FCC and load shedding contains the frequency, 
then BRC reserves are deployed, but the frequency does not return within operational limits. At this 
point, the problem cell must contact its local devices and neighbouring cells to ask for how much 
support can be offered to mitigate this emergency situation. 
The decision support system aims to address the question: how can frequency be restored within 
operational limits? Once the neighbouring cells respond with their available capacity, some 
alternative actions that could be taken include requesting that some or all of this support is 
deployed. A successful outcome is a balance being restored to the system. 
The metrics that are taken into account when prioritising the use of resources are: available 
reserves from own cell and neighbouring cells with speed of response, capacity and costs and tieline operation limits. 
2.2.2 Functional requirements for the response to an emergency request from a 
neighbouring cell for BRC support (USTRATH_DSS_3) 
This decision point is complementary to USTRATH_DSS_2, in that the neighbouring cell to the 
problem cell must also make a decision about how much support can be committed to their 
neighbour. 
The decision support system aims to address the question: how much capacity should be offered 
to the neighbour in this emergency situation? If the cell has a spare capacity which is uncommitted 
as reserves, it should generally be offered. However, if this cell (cell A) has committed to offer BRC 
support to a third party cell (cell C), should it offer those reserves to its neighbour in immediate 
need (cell B: the cell with the problem)? Does it depend on how soon the next planning phase 
begins? That is, the chances of cell A needing to supply BRC support to cell C will be lower if this 
real time operation phase finishes in 10 minutes, compared to it finishing in 5 hours. The amount of 
BRC reserves offered to cell B will vary based on factors such as this. A successful outcome would 
be where sufficient reserves are offered to the neighbours without compromising this cell’s 
commitments. 
The metrics that are taken into account when prioritizing the options are: time remaining before the 
next planning phase, the capacity of uncommitted reserves, the capacity of committed reserves 
and the tie-line operation margins.

---


### Page 16

Project ID: 609687 
 
02/02/2018 Page 15 of 43 
2.2.3 Functional requirements for the response to a frequency event due to the loss 
of a tie-line (RSE_DSS_1) 
A situation that may cause relevant frequency deviations is the loss of a tie-line transferring power. 
In fact, the loss of a tie-line implies an unbalance between load and generation, which causes a 
frequency oscillation. 
Even if the FCC intervenes to stop the frequency deviation, at the end of the intervention the 
frequency is not at its rated value. Hence, the “Balance Restoration Reserve” is activated through 
the BRC to restore the rated frequency1. 
In this case, the decision support process should identify what flexibilities involve to maintain the 
system balance and the rated frequency. In this frame, the control room operator has different 
levers to act on, such as: 
● network reconfiguration; 
● change the load and/or generation profiles; 
● change the power exchanged with neighbouring cells. 
In order to support the control room operator in the choice of the best solution, the following 
metrics should be taken into account: 
● available reserve from flexibilities (e.g. storage, distributed generation, controllable loads 
etc.); 
● support available from the neighbouring cells; 
● power flows on the tie-lines and the related information (e.g. maximum transfer capacity); 
● actual network situation (i.e. bus voltages, line currents etc.). 
As in the previous situation, the intended outcome is to restore frequency to its rated value. Finally, 
if the perturbation can be managed at the local level, the decision support process acts only on 
local information otherwise, the influence will also be on neighbouring cells ones. 
2.3 Decision support for transient stability preventive control (DTU_2) 
It is important to operate the power system with sufficient transient stability margins in terms of 
Critical Clearing Time (CCT). Therefore, the CCT for severe contingencies, e.g. three-phase fault, 
has to be assessed online. Preventive actions to re-establish a predefined stability level need to be 
taken if insufficient transient stability margins are detected. Several preventive actions could be 
taken, but the most effective one is to re-dispatch generators. The predefined stability margin is 
expressed as the minimum CCT which is allowed for a specific contingency. 
2.3.1 Functional 
requirements 
for 
transient 
stability 
preventive 
control 
(DTU_DSS_1) 
The decision support system aims to answer the question: How can the generators be dispatched 
economically to re-establish pre-defined stability margins? Technical constraints, such as 
active/reactive power capabilities, maximum line flows and voltage levels must be satisfied. As the 
control is from a preventive nature, the dispatch of the generators must be done in the most 
economical way in order to minimize the additional costs. The metrics used in the approach are the 
CCT and costs of the re-dispatch. 
The decision support system needs information about the current system state, e.g. generation 
schedule, breaker status and operation of capacitor banks. Global information is needed to an 
extent so that it is possible to represent the external power system as an equivalent. 
 
1 It has to be noted that when the BRC is activated, only the resources of the considered cell(s) are 
involved.

---


### Page 17

Project ID: 609687 
 
02/02/2018 Page 16 of 43 
The decision support system provides the control room operator a dispatch suggestion and the 
associated additional costs of the proposed action. The control room operator has to evaluate and 
approve the suggested dispatch. If necessary, the control room operator can interact with the 
decision support system by imposing additional constraints, e.g. that the active power set-point of 
certain generators is fixed and, thus, these generators cannot be re-dispatched. That means the 
re-dispatch assessment is re-run taking into account the additional introduced constraints and a 
new re-dispatch proposal are calculated. 
2.4 Decision support for management of inter-cell loop flows (DTU_4) 
Loop flows are a normal occurrence in the power system. In a meshed grid, an Optimal Power 
Flow (OPF) will give results that cause some power to flow to neighbouring cells both through the 
direct connection, but also through multiple other cells that provide an alternative path. However, 
when a loop flow occurs outside specified power flows, this is an indication that the system does 
not behave as suggested by the OPF. There could be several reasons for this deviation, such as 
sudden changes in network configuration (e.g. loss of a transmission line), but also more subtle 
causes perhaps will not always be detected, which include: 
● A generator or other sources of active and reactive power are unable to deliver the 
contracted power due to limitations in the source (e.g. apparent power limitation in 
converters and stability limits in synchronous generators). The entire source could also be 
malfunctioning, or is unable to accept new set points due to faults in the communication 
system. 
● Faulty measurement data: The measured power through a line or from a source differs from 
the actual power flow, causing regulating units to behave suboptimally. 
● Uncoordinated voltage set points between cells: If set points within a cell are not 
communicated to the neighbouring cell, this will cause an unscheduled reactive power flow 
across tie-lines with varying voltage set points on each side. 
2.4.1 Requirements and functionality for management of inter-cell loop flows 
(SINTEF_DSS_1) 
The purpose of this decision support system is threefold: to analyse the cause of the unscheduled 
loop flow; to mitigate the cause of the unscheduled loop flow; and, if necessary, to perform 
mitigation measures on possible negative consequences from the loop flow (i.e. load shedding or 
activation of additional generators). 
To analyse the cause of the unscheduled loop flow, a useful tool could be a heat mapping of 
contracted vs real power flow in the two cells bordering the tie-line with the unscheduled loop 
flows. Green colours indicate small or no deviation (+/- 10 % of rated capacity), and red large 
deviations (>10% of rated capacity). As more tie-lines have deviating values, further cells should 
be included. An important aspect of such tool is that it should be easy and intuitive to use when 
analysing the root cause. If some areas show high variation between contracted and real values, 
the sources in this area can be analysed to determine if they: 
- 
Provide contracted values: If not, a check can be performed to see that they are able to 
receive a new set point. If not, new limitations on the generator should be provided to the 
OPF, which as soon as possible should perform a recalculation to update all set points in 
the cell. Some part of this functionality could be integrated into the OPF as an automated 
check.

---


### Page 18

Project ID: 609687 
 
02/02/2018 Page 17 of 43 
- 
Measure the correct values: This can be controlled by analysing nearby measurements to 
look for inconsistencies. This should result in a work order to inspect measurement 
equipment on relevant locations. 
- 
Have large changes in voltage set-points in each end of a tie line: These should be 
changed to match, and a new OPF carried out and implemented. 
If no causes for the loop flow is found, or could be mitigated, and the loop flow is causing constraint 
violations etc, alternatives such as load shedding or starting of additional generators should be 
performed. 
2.5 Decision support for over/under voltage (TEC_2) 
The voltage control developed will be a centralized control. This centralized control will be placed 
at a Cell Operator control room and will send set-points to different kinds of distributed energy 
resources (DER), like controllable loads, microgeneration, generation or storage devices. One of 
the main objectives of this voltage control is to proactively mitigate over/under voltages, restoring 
the voltage levels to nominal values. 
2.5.1 Functional requirements for the response to an over/under voltage event 
(INESC_P_DSS_1) 
One of the assumptions of ELECTRA is the large-scale integration of DER, which may bring 
challenges to the operation of cells. One of the main challenges of this integration is related to 
voltage problems because resources like PV or wind generation may cause sudden voltage 
variations. 
When a violation of the voltage limits is detected, flexible resources can be mobilized to mitigate 
the problem. A centralized cell controller will periodically run an OPF algorithm and send set points 
to the resources that are available to contribute to the voltage problem mitigation. The cell operator 
will be able to accept or reject the first solution provided by the OPF. In case the solution is 
rejected, a new OPF will be run but now only considering the flexible resources selected by the cell 
operator to solve the voltage problem. 
The decision support platform that will be developed for voltage control will include two modes of 
operation: proactive and corrective mode. The proactive mode will calculate set points to be used 
by the resources in the next time frame of 15 minutes, if a voltage problem is envisaged. The 
corrective scenario will be used when an unexpected voltage problem occurs.

---


### Page 19

Project ID: 609687 
 
02/02/2018 Page 18 of 43 
3 Decision support system design and implementation 
3.1 Decision support during a single frequency deviation event 
(USTRATH_1) 
3.1.1 Decision support system design overview for frequency control 
The main focus of the USTRATH Decision Support System (UDSS) is to develop an intelligent 
system that gathers cell information and provides the knowledge and optimisation tools to support 
proactive decision making. The proposed UDSS has knowledge about decision points and what 
data is required for each decision point. Then, the UDSS can provide decision option(s) based on 
its knowledge or optimised solutions by interacting with its optimisation tool. The selected 
optimisation method is constraint programming, which is applied to a Constraint Satisfaction 
Problem (CSP) [3]. A CSP needs a value selected from a given finite domain to be assigned to 
each variable in the problem so that all constraints are met. The UDSS architecture is illustrated in 
Figure 3.1. The details of the UDSS architecture are described below. 
The UDSS is composed of a Knowledge Base (KB) and a CSP solver. The KB contains the 
knowledge that determines when it needs to trigger the decision making. This is based on the cell 
information received. If the network conditions mean a decision is required, it will request the 
required data from the Supervisory Control and Data Acquisition (SCADA) for this decision point 
such as the available reserves from its own and neighbouring cells along with their speed of 
response, cost and capacity. After that, if the KB needs the CSP solver to provide the ranked 
solutions it will add the relevant constraints, variables and domains into the CSP solver and trigger 
it to search potential solutions for this decision point. For some cases, the KB has the knowledge to 
directly provide the decision plan based on its knowledge without using the CSP solver, such as 
USTRATH_DSS_3 (see 3.2.2 for details). The CSP solver searches for solutions by finding 
complete assignments of domain values to variables that meet all the constraints. For many 
problems, there may be more than one set of variable assignments that satisfy all declared 
constraints. In such cases, the CSP solver can be configured to return either a user-defined 
number of solutions in a best-first manner or to search for all possible solutions. 
The following sections explain how different decision points in two frequency scenarios can be 
modelled as a CSP. 
 
Figure 3-1: UDSS architecture 
3.1.2 Decision support for the procurement of new BRC reserves after a frequency 
event (USTRATH_DSS_1) 
In this case, the decision support function aims to procure new reserves to mitigate against a 
further loss of generation after the frequency returns to the operational limits. Therefore, the

---


### Page 20

Project ID: 609687 
 
02/02/2018 Page 19 of 43 
decision support system needs to determine which reserve should be procured for BRC and a fast 
response is required to restore the frequency. The metrics that are taken into account when 
prioritising the actions are: available reserves from own cell and neighbouring cells with speed of 
response, cost, the capacity of each reserve and tie-line operation limits between cells. 
To model this decision point as a CSP, it must be expressed as a set of variables with finite 
discrete domains and a set of constraints. The variables of the CSP are the reserves of each cell, 
 . Associated with each variable is a domain of discrete values, which are the 
control signals that can be sent to the reserves, e.g. . Each 
reserve is given a number of control bandings, e.g. 80% of rated output, 70% of rated output, 60% 
of rated output etc. The control bandings become the reserve variable’s domain, e.g. {1, 0.8, 0.6, 
0.4, 0.2, 0}, where 1 represents reserve operation with rated output and 0 represents the 0 output 
state of the reserve. In addition to variables and their domains, the constraints on the solution must 
be modelled. For this decision point, it needs to procure the new BRC reserves as quickly as 
possible in case a further frequency deviation happens before the next scheduled planning phase. 
Following constraints have been defined: 
Reserve constraints: any potential solution in the form of control signals sent to reserves 
must fulfil the required BRC reserves. 
Time constraints: the total time to procure new BRC reserves must be complete before 
the next planning phase for any possible solution. 
Tie-line operation constraints: the reserve operation between cells must be within tie-line 
operation limits for any given solution, i.e. a determined solution will not result in a thermal 
overload of tie-line operation limits between cells. 
Solution prioritisation constraints: for a given situation, there may be many sets of 
options, which meet the constraints above. As a result, it needs to sort the solutions to find 
the solution that is determined to be better than the others. As this decision point needs to 
procure reserves as quickly as possible, the quicker solution will be best. If some solutions 
have the same operation time, it will compare total cost and determine which one is 
cheapest. 
3.1.2.1 USTRATH_DSS_1 case study 
The case study for this decision point comprises three cells, which are portrayed in Figure 3.2. It is 
assumed that each cell has one generator and one reserve. The amount of each reserve is: 
 . The Speed Of Response (SOR) for each 
reserve is: . The cost function 
for each reserve uses the polynomial function, i.e. 
 . In addition, the status of 
reserve takes into consideration the calculation of the cost for the required reserve. This is 
because it is less expensive to generate power from a warm generator than a cold generator. The 
tie-line operation limits between Cell1 and Cell2, and Cell2 and Cell3 is 50 MW and 150 MW 
respectively. From the perspective of CSP, each reserve variable has the following domain (control 
bandings), {1, 0.9, 0.8, 0.7, 06, 0.5, 0.4, 0.3, 0.2, 0.1, 0}. For this case study, we assume the 
frequency event occurred within Cell2 (red colour), which needs to procure 100 MW BRC reserves. 
The time remaining until the next planning phase in this case study is 30 minutes. The result of 
this case study is shown in Table 3.2 which lists the top 3 decision options and noted that reserve 
initial status in each cell is presented at the bottom of the table.

---


### Page 21

Project ID: 609687 
 
02/02/2018 Page 20 of 43 
 
Figure 3-2: Cell diagram of USTRATH_DSS_1 case study 
 
Table 3-1: USTRATH_DSS_1 case study result 
 
As the purpose of this decision point is to procure the new BRC reserves as quickly as possible to 
mitigate further loss of generation, the first option is to procure all 100MW reserves from Cell3. 
This is the quickest option (less than a minute). The reason to take all reserves from Cell3 is that it 
is the fastest acting between these three reserves. However, the fast acting solution is more 
expensive by comparing with other options. 
3.1.3 Decision support for the BSC replacement of BRC deployed reserves 
(USTRATH_DSS_4) 
This case is the replacement of the deployed BRC reserves with more economical choices. As a 
result, the decision support system needs to replace the deployed BRC reserves with less 
expensive options. The metrics that are taken into account for this decision point are: available 
reserves from own cell and neighbouring cells with speed of response, the cost of reserves, the 
capacity of each reserve and tie-line operation limits between cells. 
To model this decision point as a CSP, it utilises the same variables and domains as 
USTRATH_DSS_1. Hence, the variables of the CSP are the reserves of the cells, 
 . 
The 
domain 
of 
each 
variable 
is 
the 
control 
banding, 
e.g. 
 as described in the USTRATH_DSS_1 CSP model. The 
constraints of the CSP are the same as applied for USTRATH_DSS_1: reserve constraints, time 
constraints, tie-line operation constraints and solution prioritization constraints. However, 
the approach to sort the potential solutions is different within the solution prioritization 
constraints. As the target of this decision point is to provide more economical solutions to replace 
the deployed BRC reserves, the cheaper solution will be better. If some solutions have the same 
total cost, the quicker solution will be selected as the best. 
3.1.3.1 USTRATH_DSS_4 case study 
The USTRATH_DSS_4 case study utilises the same cell network (the three-cell network as shown 
in Figure 3.2) as the USTRATH_DSS_1 case study. Each cell has one reserve and capacity 
amount, cost, and speed of response and these are the same as in the USTRATH_DSS_1 case 
study. Moreover, the domain for the reserve variable is the same, {1, 0.9, 0.8, 0.7, 06, 0.5, 0.4, 0.3, 
0.2, 0.1, 0}. As discussed above, the constraints for this CSP are the same as the 
USTRATH_DSS_1 CSP model. It assumes the Cell2 needs to replace 100 MW reserves within 30

---


### Page 22

Project ID: 609687 
 
02/02/2018 Page 21 of 43 
minutes before the next planning phase in this case study. The tie-line operation limits between 
the cells are the same as the USTRATH_DSS_1 case study. The result of USTRATH_DSS_4 is 
presented in Table 3.3 which shows the top 3 options reserve initial status in each cell is presented 
at the bottom of the table. 
Table 3-2: USTRATH_DSS_4 case study result 
 
From the case study result, the first option is the cheapest option (total cost: 2525.5) that takes 
35MW from Cell1, 45MW from Cell2 and 20MW from Cell3. However, the first option will take more 
time to complete the operation by comparison with the other options. 
3.1.4 Decision support for BESS energy restoration after a frequency deviation 
event (ENEA_DSS_1) 
In a Wo C architecture, the role of the dynamic elements within the cell will increase even more to 
guarantee the cell stability and thus the whole network stability. From this point of view, it is crucial 
that the BESS involved in the cell stability process are in a state of charge within the safety energy 
band in order to ensure the necessary power for the stability control. 
In the USTRATH_1 scenario (single frequency deviation event), the cell stability is obtained after a 
single frequency deviation by means of BRC, where the SOC state of all the BESS involved in the 
stability control will be verified within the cell, and the safety energy range will be restored as well. 
The cell operator is in charge of the decision to select the BESS within the cell for the energy 
storage restoration, if necessary. To support the cell operator's decision, several information is 
needed: 
● Safety energy band recovery time; 
● Cost of the reserves; 
● BESS position; 
● Information about the BESS (the type of BESS, capacity, SOC). 
By following this approach, the cell operator will be able to decide which BESS to control for the 
energy band restoration or whether it should make no decision.

---


### Page 23

Project ID: 609687 
 
02/02/2018 Page 22 of 43 
The logical scheme of the decision logic system is shown in Figure 3.3 below. 
 
Figure 3-3: Flow-chart of the decisional logic for ENEA_DSS_1 
To avoid the interference with BRC control, the safety energy range restoration is carried out only 
after a BRC control caused by, for example, a single frequency deviation event. 
Once the stable state of the cell is verified, a BESS Merit Order Collection (MOC) is created. The 
BESS MOC is a matrix of information related to BESS devices within the cell, such as BESS 
device type, SOC state, safety energy band specifics. Moreover, some other information could be 
added about the BESS location within the cell and energy band restoration costs. 
Starting from BESS MOC information, a BESS Merit Order Decision (MOD) matrix is created. The 
BESS MOD is a sub set of BESS MOC containing only the energy storage systems actually 
involved in the stability process and a SOC outside of the safety energy band. 
A restoration current is set (id_res). This current will be the charge/discharge current for the safety 
energy band restoration and could be changed by the cell operator between a maximum and 
minimum value, always ensuring the cell stability. 
Exploiting the above information, the DSS estimates the charge/discharge times required for the 
safety energy range restoration for all the energy storage system listed in BESS MOD and, 
optionally, evaluates costs as well. 
Thus, cell operator could be able to choose which BESS to control within the cell in order to restore 
its safety energy band or just do nothing if he foresees that the next single frequency deviation 
event will not occur in the future.

---


### Page 24

Project ID: 609687 
 
02/02/2018 Page 23 of 43 
3.1.4.1 ENEA_DSS_1 case study 
The ENEA_DSS_1 case study is based on a generic Wo C architecture shown in Figure 3.4. 
 
Figure 3-4: Cell diagram of ENEA_DSS_1 case study 
In each cell, there can be one or more energy storage systems to support the frequency restoration 
during an imbalance event. For simplicity, it is assumed that there is one energy storage system for 
each cell. Moreover, a (SOCmax - SOCmin) band named Energy Safety Band (ESB) is defined for 
each energy storage system. The ESB definition is important to guarantee the necessary spare 
power for the cell frequency restoration. 
In a stable grid condition, we assume that each SOC is always within its own ESB. In case of an 
imbalance event, it is possible that the SOC value can escape the ESB to support the frequency 
restoration. After the frequency restoration, the ENEA_DSS_1 supports the cell operator for the 
ESB restoration. ENEA_DSS_1 makes available to the cell operator two tables, which are the 
BESS MOC and the BESS MOD. Moreover, the ENEA_DSS_1 sets a low electrical current within 
a idmax and idmin, for the safety energy band restoration. The BESS MOC table is a list of all energy 
storage system within the grid divided by cell as shown in Table 3-3. 
Table 3-3: BESS MOC in ENEA_DSS_1 
BESS 
 
CELL 
Type 
Energy 
safety band 
[Min-Max] 
SOCmax 
 
SOCmin 
SOC real time 
value 
Location and 
cost (in case) 
CELL1 
- 
 [20% - 80%] 
 90% 
 10% 
 18% 
 - 
CELL2 
 - 
 [20% - 80%] 
 90% 
 10% 
 30% 
 - 
CELL3 
 - 
 [20% - 80%] 
 90% 
 10% 
 15% 
 - 
 
The BESS MOD table is a subset of BESS MOC and represents, for each cell, the energy storage 
system with the SOC value escaped its own safety energy band. In our case study, this is 
assumed to be true for CELL1 and CELL3 as shown in Table 3.5.

---


### Page 25

Project ID: 609687 
 
02/02/2018 Page 24 of 43 
Table 3-4: BESS MOD in ENEA_DSS_1 
BESS CELL 
ESB escape 
CELL1 
YES 
CELL2 
NO 
CELL3 
YES 
 
At the end, the cell operator can modify the electrical current value for the ESB restoration between 
idmax and idmin, thereby guaranteeing the frequency stability. 
Starting from this premise, the ENEA_DSS_1 evaluates the necessary time for the ESB restoration 
related to the energy storage system in CELL1 and CELL3, and makes available to the operator 
the information shown in Table 3-5. 
Table 3-5: Information provided to the Cell Operators in ENEA_DSS_1 
ESB Time 
restoration 
CELL 
Time(min) 
Necessary Action 
(Charge/discharge) 
ESS state 
(Charge/discharge) 
CELL1 
f(Type, SOC _real time 
value)2 
Charge 
Charge 
CELL3 
f(Type, SOC _real time value) 
Charge 
Discharge 
 
During the restoration phase, the current has to be low in order to guarantee the system stability. 
This means that the ESB restoration process could require a long time (depending on the SOC 
value), and during this phase, the BESS will be busy due to its involvement in the restoration 
process. 
Thus, it is important to know what type of action (charging/discharging) is necessary for the ESB 
restoration, as well as the actual state of the BESS in each cell. 
In this case study, for example, to restore the ESB in CELL1, a charge action of the BESS is 
necessary, but this cell is already in charge mode, thus the operator will not undertake any action. 
On the other hand, as shown in Table 3.6, in CELL3 a charge action for ESB restoration is 
necessary, while the BESS state is in discharge mode. In this case, cell operator can decide to put 
the BESS in CELL3 in charge mode in order to restore the ESB and chose the electrical current, 
 
2 The energy restoration time for charging/discharging process is linked to the battery type, the battery capacity and 
actual SOC value. For a fully charged battery, the discharging time can be defined based on Peukert's law [4]. 
Conversely, for a fully discharged battery, the charging time can be defined through practical formulas experimentally 
validated. Starting from the actual SOC value, it is possible to determine the time energy restoration for the charging and 
discharging process, based on references above.

---


### Page 26

Project ID: 609687 
 
02/02/2018 Page 25 of 43 
between idmax and idmin, to minimize the restoration time (Time2) or just do nothing if he foresees 
the next single frequency deviation event will not occur in the future. 
3.2 Decision support during a two frequency deviations event 
(USTRATH_2) 
The scenario USTRATH_2 considers the extreme situation when two frequency events happen 
within one cell. Three key decision points occur where the operator may be involved and requires 
emergency support in order to return the frequency back to operational limits. The details of the 
design of these three decision support points are described below. 
3.2.1 Decision support for the response to a frequency event larger than BRC 
reserves can handle (USTRATH_DSS_2) 
The USTRATH_DSS_2 design, based around the proposed UDSS architecture mentioned above 
in section 3.1.1, are detailed below. 
After the second frequency event occurs, the combined effect of the event is more significant than 
the BRC reserves can mitigate. The problem cell needs to contact the own cell and neighbouring 
cells about how much support can be provided to return the frequency to within operational limits. 
The metrics that are taken into account for prioritising the options are: available reserves from own 
cell and neighbouring cells with speed of response, cost, the capacity of each reserve and tie-line 
operation limits between cells. 
To model this decision point as a CSP, we select available reserves from each cell as variables, 
 . 
The 
domain 
of 
each 
variable 
is 
the 
control 
bandings, 
 . The constraints considered for this decision point are the same 
as the USTRATH_DSS_1, which are reserve constraints, time constraints, tie-line operation 
constraints and solution prioritization constraints. Since this decision point is to deal with an 
emergency situation, the decision support needs the support from the local cell and neighbouring 
cells as quickly as possible. The solution prioritization constraints utilized in this case search for 
the quicker solutions from the potential solutions. 
3.2.1.1 USTRATH_DSS_2 case study 
The case study applies the same scenario as the USTRATH_DSS_1 case study. Therefore, the 
capacity amount, speed of response and cost of reserves are the same as discussed in the 
USTRATH_DSS_1 case study. Moreover, the variable, domain, and constraints are the same for 
the CSP in this case study. It assumes the two frequency event happened within Cell2, which 
needs 150MW reserves to return the frequency back to operational limits before the next planning 
phase in 30 minutes. Furthermore, the tie-line operation limits between the cells are the same as 
the USTRATH_DSS_1 case study. The USTRATH_DSS_4 case study result is depicted in Table 
3-6 with the top 3 options presented reserve initial status in each cell is presented at the bottom of 
the table.

---


### Page 27

Project ID: 609687 
 
02/02/2018 Page 26 of 43 
Table 3-6: USTRATH_DSS_2 case study result 
 
As this decision point is to deal with an emergency situation, it needs to receive the support as 
quickly as possible. Hence, the first option from the result is the quickest operation that takes 2.4 
minutes. However, the cost for the first option is not the most expensive one from the results. This 
is because the status of the reserve in Cell1 is OFF for a certain time, and it will cost more to allow 
it to generate from this cold status. 
3.2.2 Decision support for the response to an emergency request from a 
neighbouring cell for BRC support (USTRATH_DSS_3) 
The USTRATH_DSS_3 design, is also based on the UDSS architecture mentioned above in 
section 3.1.1.This decision point is when the requirement is from a neighbouring cell’s point of 
view, and the decision is about how much support can be offered to the neighbouring cell 
(frequency event cell). Therefore, the decision support system needs to address how much of its 
reserves can be provided in this emergency situation. The metrics considered in this case are: time 
remaining before the next planning phase, the capacity of uncommitted reserves, the capacity of 
committed reserves and tie-line operation limits between the cells 
To achieve this decision point, the KB of the UDSS needs to take these metrics (detailed above) 
into account to provide a potential plan. Hence, if this cell has a spare capacity which is 
uncommitted, the KB of UDSS should decide if this can be offered to the problem cell. However, if 
this cell has committed reserves, the KB of UDSS may decide to offer these reserves to support 
the other cell, depending on how soon the next planning phase begins. If this real-time operation 
phase finishes in 10 minutes, compared to it finishing in 2 hours, the KB of UDSS may consider it 
very low risk to offer committed reserves. As a result, the KB of UDSS does not need to interact 
with the CSP solver to provide the decision plan within this case. 
3.2.3 Decision support for the response to a frequency event due to the loss of a 
tie-line (RSE_DSS_1) 
The primary goal of the RSE Decision Support System (RDSS) is to support the control centre 
operator in the operation of the power system under control. In the following, a special focus is on 
those conditions that may endanger the stability of the power system, such as the loss of a tie-line 
connecting different cells (Figure 3.5).

---


### Page 28

Project ID: 609687 
 
02/02/2018 Page 27 of 43 
 
Figure 3-5: Example of network with the loss of a tie-line 
When a tie-line is lost an imbalance between load and generation occurs and the system 
experiences a frequency deviation. The RDSS provides a set of solutions to operate the power 
system in secure and stable conditions through the identification of those levers that support the 
system. The levers available to the control room operator are: grid reconfiguration; storage; power 
plant support; Distributed Generation (DG) contribution; and load modulation. 
Grid reconfiguration is an operation performed by the control centre operator to change the 
topology of the network that can be optimized considering the load and generation profiles to 
limit/avoid congestions and constraint violations. Hence, grid reconfiguration can be exploited to 
manage network events and to improve the quality of supply through the adoption of opportune 
network configurations. 
Battery energy storage allows the storage of excess energy in periods of high DERs production 
and low demand which can be released later, for instance when there is no DERs production and 
the load is high or during network events. Finally, a further contribution in the management of the 
power system may come from DG, either in terms of curtailment and injection, and load 
modulation. 
The levers that will be used for the resolution of the network event are ranked by means of a merit 
order considering the following aspects: activation time; duration of guaranteed behaviour; 
availability (yes/no); and cost. 
The reaction time is the time lever needs to be activated and to begin to provide its support; the 
duration indicates the time interval when the lever is available to provide a defined support while 
the availability of a lever indicates if the lever is available. 
The cost related to storage, DG and loads are expressed in €/MW injected/absorbed, depending 
on the operating conditions while the costs associated to the reconfiguration of the grid is equal to 
the cost of switching operations (related to the consumed lifetime of breakers). 
In Figure 3.6 the architecture of the RDSS is presented: the web of cells is observed from the 
control centre where the operator supervises the dynamic of the whole system. When a network 
event is identified, the RDSS identifies the levers that may be used for the resolution of the event 
and enables the activation of the best solution.

---


### Page 29

Project ID: 609687 
 
02/02/2018 Page 28 of 43 

Figure 3-6: RDSS architecture 
3.2.3.1 RSE_DSS_1 case study 
The case study considers the power system organized with Wo C architecture, as shown in Figure 
3.7: the four cells (C1 – C4) are connected with each other through tie-lines, exchanging power. 
For each cell there is a set-point expressed in MVA that is positive if injected in the network. It is 
negative if absorbed from the network. 
 
Figure 3-7: Wo C in N conditions 
In N conditions all the lines are connected, all the constraints are fulfilled and no alarms are sent to 
the network operator. When the tie-line L1 is lost the automatic circuit breakers open and there is 
no exchange of power on that line anymore (Figure 3-8). Also in N-1 conditions the cells keep their 
set-points to the value before the network event and constraint violations do not occur since the tielines can transfer all the power. 
 
Figure 3-8: Wo C in N-1 conditions and no violations 
Power System 
Network event 
identification 
Decision support 
system 
+ 
Control centre 
operator 
Identification of the 
levers 
Network data

---


### Page 30

Project ID: 609687 
 
02/02/2018 Page 29 of 43 
When the loss of L1 implies the violation of a network constraint the new network situation is 
reported in Figure 3-9: the cell C4 cannot keep its set-point since a constraint violation occurs on 
line L3. Hence, the new network situation is not acceptable since there is an imbalance between 
load and generation and constraints are violated. 
 
Figure 3-9: Wo C in N-1 conditions and violations 
The intervention of the RDSS is required and the new network situation is represented in Figure 
3-10: in order to fulfil all the network constraints and keep the balance between load and 
generation the set-points of the cells change. 
With respect to the situation before the fault, cells C1 and C2 do not vary their set-points while the 
set-points of cells C3 and C4 is updated. Consequently, the power flows on the tie-lines connected 
to C3 and C4 are the only ones to change. 
In this situation, the RDSS supports the network operator, highlighting the cells with a different setpoint (C3 and C4) and updating the power flows on the tie-lines by means of an OPF. The levers 
used for reaching the new equilibrium are selected based on a merit order approach, taking into 
account the above mentioned aspects (i.e. activation time, duration of guaranteed behaviour, 
availability, cost). 
 
Figure 3-10: Wo C in N-1 conditions and change of set-points 
After the intervention of the RDSS, the new network situation is reported in Figure 3-11: the fault is 
isolated and the cells directly involved in the fault have a new set-point. The new network situation 
(Figure 3-11) fulfils all the network constraints, guaranteeing the balance between load and 
generation.

---


### Page 31

Project ID: 609687 
 
02/02/2018 Page 30 of 43 
 
Figure 3-11: Network conditions after the fault clearing 
 
3.3 Decision support system for transient stability preventive control 
(DTU_2) 
It is crucial to assess the transient stability of power systems online on a grid-wide basis and take 
preventive actions if issues are identified [5, 6]. The proposed decision support tool assesses the 
CCT of the power system for three-phase faults and calculates the needed re-dispatch of 
generator if violations of a pre-defined limit are identified i.e. if the CCT for certain contingencies is 
below the pre-defined limit. The results of the assessment in terms of needed re-dispatch and 
associated costs are presented to the control room operator who has to decide whether the 
proposed re-dispatch is applied or not. The operator may also introduce additional constraints, e.g. 
the unavailability of generators to take over the dispatched power. The decision support tool 
facilitates experience of previous tools. 
3.3.1 Decision support for transient stability preventive control (DTU_DSS_1) 
3.3.1.1 Transient stability preventive control approach 
Figure 3-12 shows the flow chart of the proposed transient stability preventive control. It comprises 
the elements which are needed to establish a transient stability control and visualizes how they 
interact. In the following section, all elements are comprehensively described. 
Physical Grid 
This block represents the real physical grid, for which the transient stability control is applied. The 
feedback from the decision support block represents the interaction of the control room operator 
with the physical grid. The control room operator has to decide and approve whether the proposed 
dispatch is applied to the system or additional constraints are to be considered in the assessment 
leading to a new dispatch recommendation.

---


### Page 32

Project ID: 609687 
 
02/02/2018 Page 31 of 43 
 
Figure 3-12: Flowchart of the transient stability preventive control approach. 
System Snapshot 
A system snapshot is needed to update the Time Domain (TD) simulation model with the current 
system state. Two variants are proposed to obtain a system snapshot. In the first variant, the 
needed data is extracted from the SCADA system. The needed data includes: breaker status, 
generation output, activation of capacitor banks, RES generation, line flows and further relevant 
data. Phasor Measurement Units (PMUs) are another option to obtain a system snapshot, but that 
assumes full observability of the power system by PMUs. In case, the needed data is not fully 
available from either of these sources, a hybrid approach could be used by combining SCADA and 
PMU data to obtain a full system snapshot [7]. 
Critical Bus Screening 
Based on the current system snapshot, a Critical Bus Screening (CBS), which aims at determining 
the most critical fault locations, is carried out prior to the update of the simulation model. Only 
busbar faults are considered. Therefore, in the following the term critical buses are used, instead of 
the more generic term critical fault location. The CBS analyzes the pre-disturbance conditions and 
filters out the potentially critical buses. The CBS method is based on the work in [8-10]. A heuristic 
approach is used to identify the buses which are regarded as most critical. Buses are scanned for 
three criteria indicating their criticality. Only buses which satisfy all three criteria are regarded as 
critical and qualify for the analysis in the TD simulation. The CBS evaluates three criteria: 1) Bus 
properties in terms of voltage level and connectivity, 2) Active power injected into the bus versus 
generator active power and 3) Active power leaving the bus. 
Update of Simulation Model 
The simulation model, which represents the real power system, has to be updated with data from 
the current system snapshot. The data includes generator schedule, breaker status, dispatch of 
capacitor banks and Renewable Energy Sources (RES) generation. The updated simulation model

---


### Page 33

Project ID: 609687 
 
02/02/2018 Page 32 of 43 
is then ready to be used in the TD simulation. Additionally, the results of the CBS are saved in a list 
which contains the identified critical buses. Only these buses are considered in the assessment. 
Transient Stability Assessment and Dispatch Scheme 
The potentially critical buses are analyzed in the transient stability assessment and dispatch 
scheme, which is based on a hybrid approach using an estimation of dispatch, combined with TD 
simulations. The goal of the transient stability assessment and dispatch scheme is to determine the 
re-dispatch which is needed to achieve the desired critical clearing time while respecting all 
technical constraints and minimizing costs. The dispatch procedure starts with the Synchronous 
Generator (SG) which is associated with the bus with the lowest CCT and continues consecutively 
with CCTs in ascending order. This will deliver a near-optimal solution for the re-dispatch. 
3.3.1.2 Case study for visualization and decision support for the control room operator 
The capabilities of the approach are demonstrated on the well known New England system with 39 
buses [11] and 10 SGs shown in Figure 3.13. The results of the transient stability assessment and 
the proposed dispatch are presented in comprehensive but condensed form to the control room 
operator as shown in Figure 3.14. The situation awareness of the control room operator is 
increased as the stability margin is displayed graphically and the buses, at which the CCT is below 
the limit, are shown in a table format. Additionally, the generators and their respective dispatch to 
achieve the desired stability margin are shown numerically. Furthermore, the associated costs of 
the proposed dispatch are stated. 
 
Figure 3-13: New England test system with indication of associated cost functions 
It can be seen that all CCTs meet the specified limit after the successful dispatch. The CCTs at bus 
23 and 29 are exactly at the limit, whereas bus 22 is even more elevated than it was actually 
determined. Due to the close proximity of G7 to G6, the dispatch of G7 also affected the CCT at bus 
22. Due to the influence of the generators in close proximity, only a near optimal solution is found

---


### Page 34

Project ID: 609687 
 
02/02/2018 Page 33 of 43 
which illustrates one of the drawbacks of the sequential approach but the assessment is carried 
out in a transparent and traceable way. 
The amount of information presented to the control room operator is kept low in order not to 
overload it and to facilitate fast understanding of the condition. Moreover, warning signals could be 
generated when the CCT is below a specified limit, e.g. 200 ms. Different levels of severity can 
then be added depending on the size of the critical unit. If there is a need for in-depth information, 
the control room operator should be given the possibility to access the underlying data, e.g. 
reactive power set points. 
 
Figure 3-14: CCTs and active power set-points for initial condition and after successful dispatch 
 
3.4 Decision support system for management of inter-cell loop flows 
(DTU_4) 
The loop flow management tool is to be implemented in an inter cell SCADA-system or Distribution 
Management System (DMS). The main overview is given as a layer in the single line diagram 
overview. 
If inter cell loop flows above planned power flows occur, a warning will be given when the deviation 
is larger than a given threshold, and it will be possible to activate the loop flow layer to analyse and 
mitigate the cause of the unscheduled loop flow. 
3.4.1. Decision support for management of inter-cell loop flows (SINTEF_DSS_1) 
When the loop flow layer is selected, it shows a heat mapping / colour coding of real vs computed 
power flows in the intercell system (e.g. with green or no colour as no deviation, red for positive 
deviation, and blue for negative deviation). The purpose of this layer is to give an intuitive overview 
of cells that are causing the unscheduled loop flows. The cells connecting the tie-lines that show 
the largest deviations, or cells which show the largest differences in the sum of deviations (i.e. the 
sum of deviation of all tie-lines to the cell are not zero) are marked with an exclamation mark. 
These cells can be selected for further inspection, and a similar colour coded Single Line Diagram 
(SLD) -overview is given within the cell. 
For the SLD in the cell, generators with deviating contracted and measured values above a given 
threshold are marked with exclamation marks. For these generators, three automated tasks can be 
carried out (in addition to inspecting them manually):

---


### Page 35

Project ID: 609687 
 
02/02/2018 Page 34 of 43 
● Generators with exclamation marks are automatically pinged with a new set-point, to see 
that communications are working. If communication to the generator is down, this is shown 
with a separate signal in the SLD next to the exclamation mark. 
● To check for measurement errors, a subnetwork with a distance of one node in every 
direction from the generator is created, and a power flow is run with measured power flow 
values in all nodes. If measured and computed voltages from this simulation do not match, 
all of these nodes are flagged as "may have malfunctioning measurement equipment", and 
an automated work order to inspect the instruments is created. The set-points for these 
generators are then not considered further. 
● If the generator is not producing power, and it is shown that both measurement and 
communication equipment is working, the generator is marked as offline. If the generator is 
online and is able to receive set points, but does not have enough available power or 
reactive power, then the generators active and reactive power limits are estimated. 
When these three automated subtasks are completed for all marked generators, then the cell-OPF 
runs a new calculation with the new limits for the affected generators. This task (with subtasks) can 
be selected for one cell or for all marked cells. 
A case study shows an example of how the system may work. The case study is based on Case 5 
in a four-cell Pan-European reference power system described in D5.4 "Functional description of 
the monitoring and observability detailed concepts for the Pan-European Control Schemes" [12]. 
The synchronous generator SG1.10, placed near Cell 2 and Cell 3 in Cell 1 as seen in Figure 3.15, 
have deviation between contracted and measured power production and the three automated task 
mentioned above is tested on this generator.

---


### Page 36

Project ID: 609687 
 
02/02/2018 Page 35 of 43 
 
Figure 3-15: Topology of the Pan-European Single Reference Power System. 
Firstly, the generator SG1.10 is pinged with a new power set-point. Figure 3.16 (a) shows the 
measured power flow between the cells before the production of SG1.10 is reduced by 100MW. 
Both the active and reactive power flow in the tie-lines equals the scheduled power flow and the 
arrows are therefore coloured green. Figure 3.16 (b) shows the measured power flow between the 
cells after the production of SG1.10 is reduced by 100MW. In this case, increases in tie-line power 
flow is marked with red color and decreases are marked with blue colour. In addition, a red 
exclamation mark shows the tie-line with the largest deviation in active power and another red 
exclamation mark shows the cells which show the largest differences in the sum of deviations. The 
unscheduled power flows in Figure 3.16 (c) clearly show that the communication is working.

---


### Page 37

Project ID: 609687 
 
02/02/2018 Page 36 of 43 
 
Figure 3-16: Initial load flow (a), load flow after power reduction in SG1.10 (b) and unscheduled power 
flow after power reduction in SG1.1 (c) 
The next step is to check for measurement errors. The measured voltages one node away from 
SG1.10 are compared to the solution of a load flow based on the measured power flow values in 
these nodes. The results are shown in Table 3-7and indicate that there is an error in the voltage 
measurement on Bus 1.2, since the voltage measurement error is relatively large (2.17%) 
Table 3-7: Comparison of measured values and results from power flow on nodes nearby SG1.10 
 
Bus 1.2 
Bus 1.10 
LV_DFIG-1.10 
 
Voltage 
[k V] 
Angle 
[degrees] 
Voltage 
[k V] 
Angle 
[degrees] 
Voltage 
[k V] 
Angle 
[degrees] 
Measured 
220.30 
-3.80 
20.19 
0.00 
0.70 
-148.40 
LF results 
225.18 
-3.76 
20.19 
0.00 
0.70 
-148.34 
Error % 
2.17 
 
0.00 
 
0.00 
 
Error degrees 
 
-0.04 
 
0.00 
 
-0.06 
 
The third step is to run a new OPF with the new limitations of SG1.10. The production of SG 1.10 
is now reduced from 325 MW to 225 MW and the production gap is covered by SG2.11 in Cell 2. 
Figure 3.16 compares the load flow before and after a new OPF is run. Figure 3.16 (a) presents 
the load flow with the initial power production and Figure 3.16 (b) shows the actual load flow with 
100 MW production reduction in SG1.10. This production will be covered by SG2.11 in Cell 2 and 
this causes the need for a new OPF in Cell 1 and Cell 2. Figure 3.17 (a) shows the results of the 
OPF and the actual power flow (load flow) is shown in Figure 3.17 (b). The unscheduled power 
flow is shown in Figure 3.17 (c). When comparing Figure 3.16 (c) and Figure 3.17 (c), it is clear 
that running new OPFs in Cell 1 and Cell 2 will not reduce the unscheduled power flow through 
Cell 3 and Cell 4. This is caused by a coordination error of voltage set-points between the cells. A 
new OPF considering all cells is therefore needed.

---


### Page 38

Project ID: 609687 
 
02/02/2018 Page 37 of 43 

Figure 3-17: Result of updated OPF in Cell 1 and 2 (a), actual load flow after updated OPF (b) and 
unscheduled power flow after updated OPF (c) 
In the inter cell loop flow layer overview, an exclamation mark is also shown in the middle between 
cells that have differing voltage set-points between the cells. There are valid reasons for having 
different set-points, but when there is a difference in set-points and an unscheduled power flow 
after the generator’s limits have been adjusted with the previously mentioned task, this would 
indicate that a coordination error of voltage set-points between cells have occurred. In this case, 
the user will have a possibility to select the "voltage set-point coordination" task, that runs an 
algorithm (for instance OPF) to create new voltage set-points. 
It is also possible to run a "network configuration check", that sends a query to all line breakers to 
see if the network configuration shown in SCADA / DMS matches reality. If not, the overview is 
updated, and the errors marked for further troubleshooting. 
If neither of these methods solves the issues, there will be a need for more systematic analysis to 
determine the root causes for the unscheduled loop flows. The user can still inspect elements 
manually to see if possible errors are detected, and then have an overview over working and 
malfunctioning equipment. 
In addition to these troubleshooting measures, there is also a safety feature that prevents line 
overloading. If the loop flow causes a tie-line to exceed its rating, an algorithm (for instance OPF) 
is run to disconnect non-prioritized load supplied by the loop flow, or generation supplying it. A 
report is given describing violated constraints, and disconnected units. 
3.5 Decision support system for over/under voltage (TEC_2) 
The increasing integration of distributed generation in distribution networks may create voltage rise 
problems due to a growing number of dispersed power injections. These problems may be 
mitigated by acting on the distributed resources downstream, but the control strategy must be fast 
and well co-ordinated. If the voltage problems detected are created by the excess generation from 
RES, it may be necessary to reduce some of those resources power output or even curtail some of 
them. 
To overcome these issues, a voltage control strategy that co-ordinate the operation of the available 
DER was created in this subtask. This control strategy is based on an OPF tool that manages all 
available resources to solve voltage problems and minimize power losses. 
3.5.1 Decision support for the response to an over/under voltage event 
NESC_P_DSS_1 
The OPF that will be developed has the objective of minimizing losses and will use flexible 
resources that are considered to be available and managed by cell operators. Some of those 
resources are the following: storage devices owned by the cell operators; transformers with onload tap changer; micro-generation resources; and flexible loads.

---


### Page 39

Project ID: 609687 
 
02/02/2018 Page 38 of 43 
Two modes of operation are envisaged: corrective and proactive mode. The corrective Post 
Primary Voltage Control (PPVC) mode is triggered if the voltage in any node is outside the 
predefined limits. The proactive PPVC mode is always active and is based on an OPF algorithm 
that is run using short-term load and generation forecasting for the next 15 min interval. The 
solution of this OPF provides the optimal operation regime of the available controllable resources. 
The OPF uses generation/load data and tie-lines power flows as main inputs. Besides, power flow 
limits of lines, power generation, limits of generators, voltage limits of busbars/terminals (specified 
by the Regulation), and the amount of available PPVC reserves will be the constraints of the 
algorithm. The outputs of the algorithm are voltage set-points for PVC nodes (with automatic 
voltage regulation - AVR - capability), and set-points for capacitor banks, controllable loads, and 
on-load tap changers (PPVC node controllers). 
The voltage control algorithm is assumed to be installed in cell operator control room, which is the 
entity responsible to manage all assets in a cell. 
3.5.1.1 Voltage control algorithm 
The innovative part of this voltage control algorithm is the proactive voltage control. Each time 
period of 15 minutes (CTS-3), the proactive voltage control system will gather information of the 
tie-lines reactive flows, forecasting data and reserve information, in order to perform an OPF. 
Then, the set-points provided by OPF will be sent to the respective resources and used for the next 
time frame of 15 minutes or until a voltage problem occurs. 
Beyond the proactive voltage control, it is also necessary a corrective voltage control in case any 
unexpected voltage problem occurs. A proactive voltage control system will gather the current 
nodes’ voltage values observed from each cell continuously, and will check if they are in a safe 
band or not every minute. If the voltage values do not exceed the safe band limits, it will move to 
the next time frame. Otherwise, if the safe band is exceeded, the OPF algorithm will be triggered. 
The first step of the corrective algorithm is to gather data from the network, like load and 
generation values, and perform a power flow to calculate the voltage in the nodes. If any node 
voltage value exceeds the safe-band limits, an OPF will be run in order to calculate the new setpoint that will be sent to the respective resources, using the following data: resources status 
information, tie-lines active/reactive power set-points and forecast load and generation values. 
Again, the set-points calculated by the OPF will be used in the next time frame (15 min) or until a 
new voltage problem occurs. 
When a voltage problem occurs and the OPF is triggered, the solution found is presented to the 
cell operator. The cell operator will have a certain amount of time (e.g. 1 minute) to decide if that 
solution is to be implemented or not. If no decision is taken in the predefined amount of time, the 
algorithm will implement the solution found. Otherwise, if cell operator decides that some resource 
should not be activated, a new solution is calculated considering this information. The diagram of 
the voltage control algorithm developed is presented in the Figure 3.18. T=15 indicates that the 
time interval is 15 minutes, which can be generalised for any time period.

---


### Page 40

Project ID: 609687 
 
02/02/2018 Page 39 of 43 
 
Figure 3-18: Voltage Control Algorithm 
3.5.1.2 Case study for visualization and decision support for the control room operator 
The network chosen is a Portuguese medium voltage network and it is shown in Figure 3.19. It has 
309 buses, that are being supplied by an high voltage network (bus 301 – which is the reference 
bus), 336 active loads placed in 112 buses and some of those loads have photovoltaic 
generations. This network is divided into four cells. 
 
Figure 3-19: - Portuguese MV Network

---


### Page 41

Project ID: 609687 
 
02/02/2018 Page 40 of 43 
Cell operator will have access to various information in the control room, such as the bus voltages 
(highlighting the buses whose voltage is reaching the safe-band limits or those where the voltage 
limits were violated), the solution of the OPF when a problem occurs, the set points sent to the 
available resources, etc. Other information like the cost of the solution implemented will also be 
provided. 
The main decision that the cell operator has to take is to accept or reject the solution provided by 
the OPF in the proactive scenario or the corrective scenario. For example, when the proactive 
scenario is activated, an OPF will be run and set points will be calculated for the next 15 minutes. 
However, if cell operator does not want to activate a specific resource, a new OPF will be run not 
considering that resource. Obviously, this solution is not optimal and costs or energy losses may 
increase. An example is provided in the following Figure 3.20 and Figure 3.21, where it is shown 
that the exclusion of a certain resource (flexible loads 26 and 28 of Cell 4) induces changes in the 
voltages and energy losses. 
 
Figure 3-20: Voltage values in some nodes of the considered Portuguese network 
 
Figure 3-21: Total losses of the considered Portuguese distribution system 
As we can observe from Figure 3.20, the voltages in some of the nodes decreased, although none 
of them surpassed the limits. Figure 3.21 shows that the total losses in the cell increased with the 
exclusion of flexible load 26 and 28.

---


### Page 42

Project ID: 609687 
 
02/02/2018 Page 41 of 43 
4 Conclusions 
This report, and Deliverable, details the development and demonstration of decision support for 
operators of the future Wo C framework. It builds on the scenarios presented in ELECTRA 
Deliverable 8.2, which specified requirements for visualisations and analytics to assist the operator. 
The aim is to identity critical decisions within these scenarios, define available control actions for 
these decisions and prioritise actions for the operator. As a result, a methodology for developing 
decision support demonstrators is proposed. 
Based on the Wo C architecture, the DSS should have specific requirements that differ from current 
network management. Therefore, for the scenarios selected, one or more decision points within 
these scenarios have been identified and various actions that the operator (or automated control 
system) could take are specified. Moreover, metrics for selecting between alternative actions to 
resolve the decision have been determined with the intended outcome for each decision point. 
According to the functional specification of decision points within the selected scenarios, decision 
support systems have been designed to operate under the Wo C framework. Appropriate tools, 
methods and control algorithms have been selected. In order to implement the DSS, case studies 
have been developed to test the proposed decision points. 
This Deliverable provides novel solutions to a range of problems tackled from a Web of Cells 
functionality viewpoint, which means that it considers a level of automation and interaction with 
neighbouring cells which is absent in other research projects. The solutions specified will now be 
prototyped and assessed, with a particular emphasis on how they can be combined within the 
Wo C control, automation and decision support platform. A range of control issues are covered i.e 
the assessment of transient stability margins and critical clearing time, imbalance in tie line flow, 
loss of mains, over voltage curtailment and procurement of reserves (following single and double 
frequency deviations) are the scenarios. Enhancements in the use of OPF, and novel knowledge 
based and constraint satisfaction approaches to automatically identifying control decisions have 
been investigated. These will now be built and their performance assessed, along with their 
suitability for combination within Wo C control. This will also allow the assessment of the future role 
of an operator within the Wo C. 
The DSS needs to operate with visualisations that allow the operator to observe the system state 
at a glance and enable intuitive situational awareness. As a result, some of these decision support 
systems will combine reasoning algorithms with visualisations, which are designed in Task 8.2, to 
relay key information to the operator and to assist them in making accurate decisions and taking 
action quickly.

---


### Page 43

Project ID: 609687 
 
02/02/2018 Page 42 of 43 
5 References 
[1] 
http://www.electrairp.eu (ELECTRA IRP web site). 
[2] 
ELECTRA IRP, “D8.1: Demonstration of Visualization Techniques for the Control Room 
Engineer in 2030,” 2016. 
[3] 
K. R. Apt. Principles of Constraint Programming, Cambridge University Press, 2003. 
[4] 
Omar, N., Bossche, P. V. D., Coosemans, T., & Mierlo, J. V. (2013). Peukert revisited—
critical appraisal and need for modification for lithium-ion batteries. Energies, 6(11), 56255641. 
[5] 
T. Weckesser, H. Johannsson, S. Sommer, and J. Østergaard, “Investigation of the 
Adaptability of Transient Stability Assessment Methods to Real- Time Operation,” in 3rd 
IEEE PES International Conference and Exhibition on Innovative Smart Grid Technologies 
(ISGT Europe), 2012, pp. 1–9. 
[6] 
M. Pertl, M. Rezkalla, and M. Marinelli, “A Novel Grid-Wide Transient Stability Assessment 
and Visualization Method for Increasing Situation Awareness of Control Room Operators,” in 
IEEE PES Innovative Smart Grid Technologies Conference Asia (ISGT), 2016, pp. 1–6. 
[7] 
M. Glavic and T. Van Cutsem, “Reconstructing and tracking network state from a limited 
number of synchrophasor measurements,” IEEE Trans. Power Syst., vol. 28, no. 2, pp. 
1921–1929, 2013. 
[8] 
V. Kolluri, S. Mandal, M. Y. Vaiman, M. M. Vaiman, S. Lee, and P. Hirsch, “Fast Fault 
Screening Approach to Assessing Transient Stability in Entergy’s Power System,” in IEEE 
Power Engineering Society General Meeting, 2007, pp. 1–6. 
[9] 
S. Lee, L. Min, and M. Vaiman, “Fast Fault Screening for Real-Time Transient Stability 
Assessment,” 2010. 
[10] M. Y. Vaiman, M. M. Vaiman, and A. Gaikwad, “Fast Fault Screening Methodology for 
Transient Stability Analysis of Bulk Power Systems,” in IEEE Power and Energy Society 
General Meeting, 2013, pp. 1–5. 
[11] T. Athay, R. Podmore, and S. Virmani, “A Practical Method for the Direct Analysis of 
Transient Stability,” IEEE Transactions on Power Apparatus and Systems, vol. PAS-98, no. 
2, March/April 1979, pp. 573-584. 
[12] Marinelli, Mattia, et al. "Functional description of the monitoring and observability detailed 
concepts for the Pan-European Control Schemes: ELECTRA Deliverable D5. 4. WP5: 
Increased Observability." (2017).

---


### Page 44

Project ID: 609687 
 
02/02/2018 Page 43 of 43 
6 Disclaimer 
The ELECTRA project is co-funded by the European Commission under the 7th Framework 
Programme 2013. 
The sole responsibility for the content of this publication lies with the authors. It does not 
necessarily reflect the opinion of the European Commission. 
The European Commission is not responsible for any use that may be made of the information 
contained therein.

---
