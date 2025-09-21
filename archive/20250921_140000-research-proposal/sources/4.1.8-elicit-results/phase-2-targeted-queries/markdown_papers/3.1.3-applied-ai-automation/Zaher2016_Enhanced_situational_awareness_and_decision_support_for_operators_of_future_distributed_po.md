# Zaher2016 Enhanced situational awareness and decision support for operators of future distributed power network architectures

## Paper Metadata

- **Filename:** Zaher2016_Enhanced_situational_awareness_and_decision_support_for_operators_of_future_distributed_power_network_architectures_DOI_10-1109_ISGTEurope-2016-7856198.pdf
- **DOI:** 10.1109/ISGTEurope.2016.7856198
- **Authors:** Not available
- **Year:** Not available
- **Journal/Venue:** Not available
- **URL:** Not available
- **Extraction Date:** 2025-06-03T15:04:10.233178
- **Total Pages:** 7

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

Downloaded from orbit.dtu.dk on: Jun 03, 2025
Enhanced Situational Awareness and Decision Support for Operators of Future
Distributed Power Network Architectures
Zaher, Ammar S. A. E.; Catterson, V. M.; Syed, M. H.; Mc Arthur, S.D.J ; Burt, Graeme M.; Marinelli, Mattia;
Prostejovsky, Alexander
Published in:
Proceedings of 2016 6th IEEE PES International Conference and Exhibition
Link to article, DOI:
10.1109/ISGTEurope.2016.7856198
Publication date:
2016
Document Version
Peer reviewed version
Link back to DTU Orbit
Citation (APA):
Zaher, A. S. A. E., Catterson, V. M., Syed, M. H., Mc Arthur, S. D. J., Burt, G. M., Marinelli, M., & Prostejovsky, A.
(2016). Enhanced Situational Awareness and Decision Support for Operators of Future Distributed Power
Network Architectures. In Proceedings of 2016 6th IEEE PES International Conference and Exhibition IEEE.
https://doi.org/10.1109/ISGTEurope.2016.7856198

---


### Page 2

Enhanced Situational Awareness and Decision Support 
for Operators of Future Distributed Power Network 
Architectures 
A. S. Zaher, V. M. Catterson, M. H. Syed, S.D.J Mc Arthur and G. M. Burt 
Institute for Energy and Environment, University of Strathclyde, Glasgow, Scotland 
 
M. Marinelli, A. Prostejovsky 
Centre for Electric Power and Energy, Technical University of Denmark, Roskilde, Denmark 

Abstract—This paper describes scenarios proposed for a control 
room decision support system aimed at future power network 
operators. The purpose is to consider the requirements of the 
future control room from the perspective of the operator under 
the conditions of a significant frequency excursion incident. The 
control room visualisation and decision support functionality for 
aiding the operator in restoring the frequency to its target value 
will be considered. The analysis takes place within the Web-ofCells framework, adopted to deal with power system control 
through a web of subsystems, called cells, which are highly 
automated, and operated by Cell Operators. 
I. 
INTRODUCTION 
With the rapidly increasing levels of automation and 
intelligence within today's power systems, the control room 
of the future may look significantly different to the traditional 
concept of visualising the network diagram and real time 
alarms. On the one hand, there is ever more data being 
generated and collected by wide area measurement systems, 
phasor measurement units, and online condition monitoring, 
and control room operators will need additional support in 
order to sift and prioritise key information. On the other hand, 
automation systems to achieve active network management, 
auto-reclosing capability, and dynamic plant ratings lead to a 
network that is more self-managing and self-healing than ever 
before, reducing the burden on operators to take action. 
This means that the role of the control room operator will 
inevitably change. The control room as a physical location 
may not exist, with typical operator functions being the 
responsibility of individuals who may either be co-located or 
distributed remotely. Systems to assist operators must 
likewise adapt and evolve to meet the needs of future 
engineers, while still ensuring emergency situations can be 
recovered when smart systems reach their limits of operation. 
This paper considers one particular view of future 
networks, as posited by the EU project ELECTRA (European 
Liaison on Electricity Committed Towards Long-term 
Research Activity), called the Web of Cells [1,2]. In this 
vision, transnational grids are formed by network sections 
operating as peers, without hierarchical control. The operator 
is tasked with control of one or more cells, and incidents can 
be resolved by actions taken within the cell, or by requesting 
support from neighbouring cells. 
This paper considers the particular scenario of managing a 
significant frequency excursion within the Web of Cells 
architecture, from the point of view of the control room 
operator managing one cell. Within this paper, “control room 
operator” is intended to mean the engineer with responsibility 
for online management of the network, and does not reflect 
their physical location. With reference to the literature on 
future control rooms, a set of requirements from the operator 
in this scenario is identified. The role of decision support is 
discussed, and the functionality in terms of prioritising 
appropriate actions is presented. 
II. 
POWER SYSTEM CONTROL ROOM DECISION SUPPORT 
The operation of power systems is an extremely 
challenging task mainly due to the size and complexity of 
networks and the large number of contingencies that can 
occur. Because of the large size and complicated nature of 
networks, forming a complete and accurate picture of the 
state of a particular area for which an operator might be 
responsible, can be quite difficult. These difficulties have the 
potential to prohibit operators from achieving the required 
level of situational awareness (SA) to make informed 
decisions and respond effectively to any particular incident. 
It has been shown recently that the lack of SA has been 
recognised as a significant contributing factor to several large 
electrical disturbances worldwide, with numerous incidents 
including the Italian blackout in 2003 to the more recent 
black out in Arizona and South Carolina in 2011 [3]. It is 
thought that one of the main reasons for the escalation of 
incidents is due to poor information sharing between 
operators, and or failure in the information systems, leading 
to delayed and inadequate responses being taken [3]. 
Decision Support Systems (DSS) have been incorporated 
in power system control rooms in order to help operators

---


### Page 3

avoid such situations. The concept of DSS was derived from 
the combination of theoretical studies of organizational 
decision making at the Carnegie Institute of Technology and 
technical computing advances from the 1950s onwards [4]. It 
was from this point that DSS grew to a distinct research topic. 
A DSS can be generically defined as an information 
system that is designed to support business or organisational 
decision making activities [4]. Such a system typically serves 
the management and operation or planning levels in an 
organisation with the aim of supporting users to make 
decisions by providing the right information at the right time. 
DSSs have been applied to a variety of applications within 
the power systems domain. Vale et al [5] detail a DSS to help 
operators with demand response and contracts adoption. This 
system uses machine-learning techniques to create a rule 
base, which describes the actions of different actors in 
demand response programs. A number of works exist in the 
area of intelligent alarm processing from different authors 
looking at prioritising, suppressing, and fault diagnosis of 
generated alarms [6-9]. The main objective of these systems 
is to filter the amount of data presented to the operator so that 
the highest priority information is passed to them. 
Research in this area of DSS has more recently fallen 
under the wider topic of situational awareness (SA), which 
encompasses a more holistic view of how to improve operator 
awareness through a more complete assessment of the 
network and its ICT systems. One definition of SA has been 
expressed as: the perception of the elements in the 
environment within a volume of time and space, the 
comprehension of their meaning and a projection of their 
status in the near future [3]. Aspects such as optimised PMU 
placement [10] and improved GUI visualisations [11-13] as 
well as the alarm processing research mentioned previously 
all fall under situational awareness. 
III. 
FUTURE DISTRIBUTED POWER NETWORK 
ARCHITECTURES 
One vision of the power system in 2030 and beyond is for 
the network architecture to correspond to a Web of Cells. The 
Web of Cells was conceived as a means of achieving 
distributed control among autonomous regions of the 
network, termed cells [1]. A cell is defined as "a group of 
interconnected loads, distributed energy resources and storage 
units within well-defined grid boundaries corresponding to a 
physical portion of the grid and to a confined geographical 
area" [1]. The key feature is that each cell is a peer of other 
cells, with no overall system operator able to exercise 
hierarchical control over cells. It is expected that peer cells 
will collaborate to efficiently allocate resources, including 
power and ancillary services, via tie lines between cells [2]. 
Trends within power systems are such that distribution 
networks are becoming more like traditional transmission 
systems, with bidirectional power flows, more active control, 
and greater observability than in the past. This trend is 
expected to continue, so that by 2030 there may not be a split 
between Transmission System Operators and Distribution 
System Operators, but simply Cell Operators [2]. A cell is not 
confined to a particular voltage level, and some cells may 
span voltage levels. Therefore, it is expected that current 
utilities will transition to operating one or more cells, which 
will generally correspond to their current geographical 
network regions. 
 
Fig. 1. Web of Cells architecture example 
With this in mind, an operator will have certain 
responsibilities for managing their cell, such as maintaining 
voltage and thermal constraints, responding to frequency 
deviations, and so on. Periodically (such as on a 15-minute 
basis), each cell will commit to a plan of service delivery 
with neighbouring cells, to ensure contingencies can be 
handled. The operator is able to take unilateral action within 
their cell, as long as they continue to meet their commitments 
to neighbours. 
This change in operator responsibilities places new 
requirements on the data and information systems the 
operator needs to access. As some examples: 
 The operator needs to be able to visualise the current state 
of commitments to neighbours, and any constraints on 
satisfying them such as tie line capacity. It is expected 
that network automation will achieve these commitments 
without breaching constraints in the general case, so no 
operator action is required. But awareness of which 
constraints are reaching their limits is beneficial, as an 
internal cell reconfiguration instigated by the operator 
may alleviate congestion. 
 The operator must be able to see a forecast of events 
within the committed time period, in order to identify 
looming threats to service delivery. It may be that a tie 
line is within capacity limits now, but a generator is 
scheduled to go offline with a significant impact on intercell power flows. It is easier to resolve such situations 
with foresight of their occurrence, rather than responding 
in a reactive manner as they occur. A forecast of 
headroom on each constrained asset and flexibility within 
dispatchable loads is needed to assist with this. 
 The operator needs to be able to find out which automatic 
control systems are operating, but at the same time not be 
overwhelmed by notifications of every automated action 
within the cell. There may be times when automated 
systems such as active network management schemes are 
disabled, due to outages for maintenance or other events. 
The operator needs to be able to predict the outcome of 
manual control actions, including the response (or nonresponse) of controllers. But the high level of automation 
expected within a cell would be mentally taxing if events 
were presented like SCADA alarms. Therefore, there

---


### Page 4

must be a way for the operator to "drill down" to the 
status information for automated systems. 
 The operator must be able to take action if and when the 
automated control systems fail to resolve a contingency 
event. Automated systems will be designed to handle 
particular contingencies, such as a certain loss of 
generation. If the size of the event exceeds the designed 
capabilities of the controller, the network may not be 
automatically recoverable. It is expected that in extreme 
circumstances, automatic load shedding will be initiated 
as a final preservation strategy. However, the human 
operator may know of alternative strategies to maintain 
network operation, or may wish to alter the priority of 
loads for shedding given specific knowledge. It should be 
possible for the operator to override the automated 
systems in such a case. 
These requirements highlight two broad functions for the 
information system: it must support visualisation of current 
and future state (Situational Awareness); and it must allow 
control actions to be taken. Since the latter is expected to 
occur only in unusual circumstances (such as extreme 
network events), it would be beneficial for the information 
system to also provide decision support at such times, guiding 
the operator as to what actions are available, and their 
expected outcomes. 
The next section considers a particular case study of 
managing a frequency excursion within a Web of Cells. The 
role of the operator, and the functionality of the information 
system to support that role, are proposed and discussed. 
IV. 
DECISION SUPPORT DURING FREQUENCY DEVIATIONS 
A critical incident which any network must be prepared to 
handle is that of a significant frequency deviation event. This 
section explores how such a scenario might be handled within 
the Web of Cells framework. Any event that causes a 
significant deviation in frequency beyond the operational 
limits is managed by the following three services: 
1. Frequency Containment Control (FCC): As the 
name suggests, the main responsibility of this 
service is to stop the rise or fall of frequency and to 
contain it to a pre-defined value. 
2. Balance Restoration Control (BRC): Once the 
frequency deviation has been contained, it is the 
responsibility of BRC to restore the frequency back 
within the operational limits and the power exchange 
with other cells to the scheduled values. 
3. Balance Steering Control (BSC): Although the 
frequency has been restored by BRC, the reserves 
that are utilized by BRC are fast acting and therefore 
may be expensive. These reserves would need to be 
replaced for the remainder of the scheduled period. 
Therefore, it is the responsibility of the BSC to 
replace the restoration reserves with the most 
economically feasible resources. 
As shown in Fig. 2. there are two phases of frequency 
management within the Web of Cells architecture: a 
procurement phase and real-time operation phase. Although 
the services described earlier seem very similar to the 
services that are available to the operators today, it is the 
distributed procurement and real-time delivery of these 
services necessary within the Web of Cells paradigm that sets 
them apart. It is intended that the procurement of services is 
achieved by an algorithm distributed amongst the cells within 
the network (hereafter referred to as the “inter-cell 
algorithm”), which will fairly allocate resources to meet 
contingencies anticipated by each cell. The implementation of 
this algorithm is out of the scope of this paper, which focuses 
instead on the requirements and functionality of each actor 
within the cell. 
 
Fig. 2. Frequency management in Web of Cells 
V. 
FUTURE CONTROL ROOM DECISION SUPPORT 
EXAMPLES 
Two main scenarios are considered here, which fall within 
the category of a significant frequency excursion incident 
(such as the loss of two generators) within the Web of Cells. 
The scenarios detail how the visualisations and decision 
support might be provided to a cell operator under these 
circumstances. The two scenarios are as follows: 
1. A single frequency deviation event within a cell 
2. Two frequency deviation events occurring within the 
same cell as follows: 
a. Two simultaneous or near simultaneous events 
b. The second event occurs after the initial event 
frequency restoration phase. 
For the first scenario, the automatic frequency control 
scheme described in the previous section is envisaged to 
automatically handle a single frequency disturbance event 
within a cell. In line with the “guidelines” detailed in [3] the 
authors agree that even while the system is automatically 
resolving the single event, key information must still be 
relayed to the operator so that they are kept well informed of 
what is happening within the network and how any particular 
incident is being dealt with. That is, there is no operator 
decision to be made, but visualisation of the situation is 
required. It is for this reason that the single event scenario is 
considered to be of interest. 
The second scenario has been further split into two cases 
as the timing of the second event differentiates the options 
available to an operator when attempting to resolve the 
incident. Sequence diagrams have been created in order to 
describe the various interactions taking place between the 
different 
system 
actors. 
These 
actors 
are:

---


### Page 5

Fig. 3. Scenario 1) Single frequency event sequence diagram.
 
Aggregators/devices: This refers to the controllable 
demand/generation that is available within the cell. 
In general, the aggregator is responsible for all 
devices that are present within their portfolio. There 
can be more than one aggregator within a cell. 
 
Cell Monitoring and Control: This is the entity 
within the cell that is responsible for monitoring the 
observables available within the network and taking 
control 
decisions. 
Monitoring 
involves 
the 
processing of all the observables and making it 
available to any entity as and when required. Control 
involves all the automated control algorithms that 
are present within the cell. 
 
Inter-cell Algorithm: This refers to the control 
algorithm that in a distributed manner communicates 
and negotiates with other cells to coordinate network 
restoration plans. 
 
Decision Support: Refers to the software system 
responsible for processing any available information 
to portray to the operator what is happening within 
the network. It must decide how best to show this, 
while aiding the operator through any processes they 
may need help with. 
 
Human Operator: is the person responsible for the 
secure and stable operation of the cell. Although 
most of the functionalities within the cell are 
envisioned to be automated, manual control can be 
given to the operator and their authority supersedes 
all other entities within the cell. 
The aim is to explain the sequence of events as the 
frequency excursion incidents progress from the initial point 
of occurrence to finally the frequency being restored.

---


### Page 6

Figure 4: Scenario 2a) Two frequency events within the same cell 
1) Single Frequency Deviation Event 
The sequence diagrams are concerned with the real-time 
operation phase as shown in Figure 2. Therefore, it is 
assumed that at the start of each diagram, there is an agreed 
plan for containment reserves and restoration reserves for the 
current scheduled period, which has been communicated to 
devices as appropriate. Figure 3 details the operation phase 
for the single frequency event. 
The process starts with the frequency deviation incident 
being detected locally at the cell level by the Aggregator, 
where the frequency is monitored. The containment reserve 
plans are automatically activated to contain the frequency. 
FCC is fast acting (within milliseconds) and so there is no 
time for these events to be relayed to the operator, or for the 
operator to alter the plan. However, the basis for the 
containment reserve plan is that its activation will contain a 
single frequency deviation event. 
Following this, the cell control mechanisms attempt to 
identify the location of the incident to prepare for the 
frequency restoration phase and BSC. Measurements are 
taken from within the cell, and appropriate information 
shared with neighbouring cells. 
Once this process is complete, the problem cell is 
identified to the operator. The information passed to the 
operator will differ depending on whether they operate the 
problem cell or not. If the problem is within a distant cell, 
only an indication that there is a problem in the network 
currently being resolved is needed, as no action from within 
this cell is necessary. A cell neighbouring the problem cell 
will display a visualisation of how their reserves are 
contributing to the restoration of the frequency. At this point 
the neighbouring cell can automatically calculate its available 
flexibility over and above its current commitment so that it is 
already preparing for a subsequent incident should that occur. 
In the scenario shown in Figure 3, the problem originated 
within the cell of this operator. Therefore, the DSS presents 
updated visualisations detailing this and the activated plans 
for resolving the excursion to the human operator. It is 
envisaged that a timeline visualisation indicating the current 
frequency of the network and a forecast of the result of the 
restoration plans is displayed. This ensures that the operator 
is kept informed with what is happening in the network, 
especially if it falls within their responsibility area. Finally, 
for the BSC phase, a list of back-up resources available to the 
cell is provided to the DSS. The DSS then processes this 
information to prioritise the resources for the operator in 
terms of suitability and price. Cell control and monitoring 
also provides an automated frequency replacement plan,

---


### Page 7

giving the operator the choice of implementing this or 
utilising a plan based on their manual selection from the 
prioritised list. The time-line visualisations would also be 
updated accordingly based on the operator selection, to reflect 
the new replacement reserves. The operator has a certain 
window of time in which to make their decision, after which 
if no response has been received, the decision support 
automatically signals the cell control to implement its plan. 
It is worth mentioning here that for the single frequency 
event scenario, it can be seen that no actions are really 
necessary from an operator’s point of view as everything is 
dealt with automatically. Nevertheless, actions can still be 
taken if needed to manually override the executed plans. 
2) a) Two simultaneous frequency events 
This second scenario starts with the same frequency 
containment process as before, however a second frequency 
event occurs almost instantly within the same cell. As there 
are insufficient containment reserves to deal with this 
excursion, automatic load shedding takes place to contain the 
frequency. This information is passed to the operator. The 
same disturbance location and magnitude identification 
process takes place as before, with the total combined 
disturbance from both events now being calculated. This 
allows for the deficit in the restoration plans obtained during 
the procurement phase to be determined and highlighted to 
the operator using the time-line visualisation. 
As the load shed process has taken place by this point, the 
operator now has some time to take action and authorise a 
reserve request to the neighbouring cells. This can be either in 
the form of asking for an automated plan to be formulated by 
the cell control mechanisms or by manually formulating a 
plan by requesting reserves from the desired neighbouring 
cells. Once the extra reserves are procured, the full frequency 
restoration process can be completed and the visualisations 
showing the time-line of how and when the plan will restore 
the frequency of the network can be updated accordingly. 
2) b) Second event occurs after initial event restoration 
In this scenario, a second frequency event occurs after the 
initial restoration plans have been executed and when the 
frequency of the network is being restored. However, due to 
the second event, the frequency will not restore to its target 
level. No load shed takes place at this point of time as the 
restoration reserves have the effect of containing the 
frequency. From the point that the frequency is contained, the 
process is similar to that described for 2a, with the operator 
being given the option of altering the restoration plan. 
CONCLUSION 
This paper has explored the requirements of a control room of 
2030, from the point of view of a cell operator within the 
Web of Cells architecture. With the anticipated levels of 
automated control within future power networks, there are 
many situations where no operator action will be required. 
However, there are ever increasing volumes of data being 
gathered from power networks, and operators will require 
tools for prioritising information, particularly during network 
events such as frequency deviations. This work proposes the 
functionality of the control room visualisation and decision 
support system, which can restore the frequency to its target 
value after such an event. 
ACKNOWLEDGMENT 
The work in this paper has been in part supported by the 
European Commission, under the FP7 project ELECTRA 
(grant no: 609687). 
REFERENCES 
[1] L. Martini, L. Radaelli, H. Brunner, C. Caerts, A. Morch, S. Hanninen, 
C. Tornelli, “ELECTRA IRP Approach to Voltage and Frequency 
Control for Future Power Systems with High DER Penetration”, 23rd 
International Conference on Electricity Distribution (CIRED), June 
2015. 
[2] M. H. Syed, G. M. Burt, J. K. Kok, R. D’Hulst, “Demand Side 
Participation for Frequency Containment in the Web of Cells 
Architecture”, International Symposium on Smart Electric Distribution 
Systems and Technologies (EDST), September 2015. 
[3] Mathaios Panteli, Daniel S. Kirschen, “Situation awareness in power 
systems: Theory, challenges and applications”, Electric Power Systems 
Research, Volume 122, May 2015, Pages 140-151. 
[4] Keen, P. G. W. (1978). “Decision support systems: an organizational 
perspective.” Reading, Mass., Addison-Wesley Pub. Co. 
[5] Faria, Pedro, and Zita Vale. "Decision Support Concerning Demand 
Response Programs Design and Use-A Conceptual Framework and 
Simulation Tool." Applied Mathematics & Information Sciences 8.1 
(2014): 161. 
[6] G. M. Burt, J. R. Mc Donald, A. G. King, J. Spiller, D. Brooke and R. 
Samwell, "A real-time decision support system for the operation of a 
132 k V power network," Control, International Conference on, 
Coventry, UK, 1994, pp. 153-158 vol.1. 
[7] R. W. Bijoch, S. H. Harris, T. L. Volkmann, J. J. Bann and B. F. 
Wollenberg, "Development and implementation of the NSP intelligent 
alarm processor for power systems," in IEEE Transactions on Power 
Systems, vol. 6, no. 2, pp. 806-812, May 1991. 
[8] Alvin H. Shoop, Steven Silverman, “A real-time alarm processor”, 
International Journal of Electrical Power & Energy Systems, Volume 
14, Issue 2, 1992, Pages 108-113. 
[9] E. Kyriakides, J.W. Stahlhut, G.T. Heydt, “A next generation alarm 
processing algorithm incorporating recommendations and decisions on 
wide area control”, In: Proc. of the IEEE Power Engineering Society 
General Meeting, 2007. 
[10] R. Emami and A. Abur, "Robust Measurement Design by Placing 
Synchronized Phasor Measurements on Network Branches," in IEEE 
Transactions on Power Systems, vol. 25, no. 1, pp. 38-43, Feb. 2010. 
[11] T.J. Overbye, D.A. Wiegmann, A.M. Rich, Y. Sun, “Human factors 
aspects of power system voltage contour visualizations”, in: Proc. of 
the IEEE Power Engineering Society General Meeting, 2003. 
[12] R.P. Klump, J.D. Weber, “Real-time data retrieval and new 
visualization techniques for the energy industry”, in: Proc. of the 35th 
Annual Hawaii International Conference on System Sciences (HICSS), 
2002. 
[13] T.J. Overbye, J.D. Weber, “Visualization of power system data”, in: 
Proc. of the 33rd Annual Hawaii International Conference on System 
Sciences (HICSS), 2000.

---
