# An intelligent multi agent framework for active distribution networks based on IEC 61850 and FIPA standards

## Paper Metadata

- **Filename:** An intelligent multi agent framework for active distribution networks based on IEC 61850 and FIPA standards.pdf
- **DOI:** 10.1109/isap.2015.7325527
- **Authors:** Cintuglu, Mehmet H. and Martin, Harold and Mohammed, Osama A.
- **Year:** 2015
- **Journal/Venue:** 2015 18th {International} {Conference} on {Intelligent} {System} {Application} to {Power} {Systems} ({ISAP})
- **URL:** http://dx.doi.org/10.1109/ISAP.2015.7325527
- **Extraction Date:** 2025-06-03T15:01:19.825362
- **Total Pages:** 7

## Abstract



## Keywords



---

## Full Text Content



### Page 1

See discussions, stats, and author profiles for this publication at: https://www.researchgate.net/publication/308673427
An intelligent multi agent framework for active distribution networks based on
IEC 61850 and FIPA standards
Conference Paper · September 2015
DOI: 10.1109/ISAP.2015.7325527
CITATIONS
14
READS
341
3 authors:
Mehmet Hazar Cintuglu
ABB
40 PUBLICATIONS   2,220 CITATIONS   
SEE PROFILE
Harold Martin
Florida International University
20 PUBLICATIONS   531 CITATIONS   
SEE PROFILE
Osama A Mohammed
Florida International University
721 PUBLICATIONS   15,721 CITATIONS   
SEE PROFILE
All content following this page was uploaded by Mehmet Hazar Cintuglu on 28 September 2016.
The user has requested enhancement of the downloaded file.

---


### Page 2

Abstract— The development of a resilient and intelligent smart 
grid concept with decentralized control capability requires extensive deployment of interoperable frameworks. This paper 
presents a global multi agent framework using IEC 61850 and 
the foundation for intelligent physical agents (FIPA) standards. 
The developed framework was implemented on a laboratory 
based smart grid test bed at Florida International University. 
The open connectivity unified architecture (OPC UA) interface 
was adopted to share common information between two 
platforms. The hardware/software based Smart Grid Test Bed 
involves actual IEC 61850 intelligent electronic devices (IED) and 
a complete hardware based laboratory setup. In order to present 
the capabilities of the developed framework, an autonomous 
distributed energy resource (DER) ancillary service use case was 
realistically demonstrated as a sample study. 
 
Index Terms— FIPA, IEC 61850, JADE, Multi agent, OPC UA 
I. INTRODUCTION 
N contrast to centralized control in existing grid , the emerging smart grid concept compels utilities to adopt decentralized methods as a result of the highly dynamic behavior of 
the active distribution networks. Decentralized control approaches intend to provide autonomy for different control layers by enabling an event-driven peer-to-peer communication 
structure, where central control schemes mainly rely on 
master-slave interactions. In power system applications, the 
implementation of decentralized control is established using 
multi agent frameworks, which are composed of interacting 
multiple intelligent agents to achieve a global or local 
objective function. An agent requires interaction with its 
environment through sensors and actuators. A sensor acquires 
the data from the outside world and the actuator responds 
according to the agent’s decision. Embedded decision making 
algorithms facilitate the benefit maximization of the agents’ 
autonomy. 
Multi agent based schemes are widely applied to power system controls; including self-healing, resilient grid automation 
[1]-[2] and power system protection [3]-[4]. Multi agent based 
microgrid control draws considerably more attention than any 
other 
smart 
grid 
applications 
[5-10]. 
For 
actual 
implementation of decentralized control schemes in power 
systems, it is imperative to link multi agent objects to 
distributed industrial control systems such as intelligent 
electronic devices (IED) and programmable logic controllers 
(PLC). 
 
The 
required 
interface 
is 
established 
through 
the 
combination of the information data and protocols. 
Interoperability is one of the major challenges to 
accomplish a complete smart grid infrastructure due to the 
large amount of processed data from different vendor and 
communication protocols [11]. Utilities and independent 
system operators seek the most proper way to reach the 
required information easily and securely for different 
application layers, such as metering, protection, automation 
and market segments. For this reason, The NIST Framework 
and Roadmap for Smart Grid Interoperability Standards 
Release [12] defines three major goals to establish 
interoperability standards and protocols for the smart grid. The 
IEEE Std. 2030 establishes three integrated architectural perspectives: power systems, communications technology, and 
information technology [13]. The guidelines also define the 
design criteria, and reference model applications with 
communication connections and data flows [14]. 
IEC 61850 is the new international standard of communications, which enables the integration of all substation functions, 
such as protection, control, measurement and monitoring. IEC 
61850 expands the area of influence in many parts of power 
systems due to its wide industry acceptance. Communication 
systems for hydroelectric power plants and distributed energy 
resources (DERs) have been recently applied to other domains 
as IEC 61850 extension standards [15]. However, the smart 
grid concept covers an extensive control, automation and 
protection applications such that a single standard may not 
meet all the required forms of monitoring and information 
exchange demands. 
Considering the emerging active distribution networks, new 
energy market policies are necessary such as implementation 
of real-time auction models and scheduling the dispatch of 
DERs. Hierarchical control of microgrids require interaction 
with utilities for dynamic adjustment of the primary, 
secondary and tertiary control levels. Taking into account the 
mentioned requirements of the future grid, advanced 
intelligent multi agent frameworks are necessary with a 
flexible ability to create tailor-made decentralized control 
schemes while allowing the legacy protocols. 
The foundation for intelligent physical agents (FIPA) is an 
organization which intends to evolve inter-operable agent 
communications with semantically meaningful messages, such 
as how messages are transferred and presented as objects [16]. 
 
An Intelligent Multi Agent Framework for 
Active Distribution Networks Based on 
IEC 61850 and FIPA Standards 
Mehmet H. Cintuglu, Harold Martin, Student Members, IEEE, Osama A. Mohammed, Fellow, IEEE 
I
978-1-5090-0191-0/15/$31.00 ©2015 IEEE

---


### Page 3

Java agent development framework (JADE) is a software 
framework to develop agents compliant with FIPA standards 
with flexible agent behavior methods [17]. 
Taking the specific benefits of two major frameworks, this 
work intends to provide a flexible intelligent multi agent 
framework for all power system application layers, merging 
the IEC 61850 and FIPA standards by using the open 
connectivity unified architecture (OPC UA) interface. To date, 
few researchers have contributed using multi agent systems 
with industrial devices where most of them have presented 
their work in simulation environments. This contribution is 
intended to extend existing works to a hardware-based 
laboratory environment within an actual smart grid test bed. 
The outline of the paper is as follows. Section II discusses 
the related work and contribution of this work. In section III, 
the developed cyber-physical framework is explained in detail. 
An experimental case study is demonstrated in Section IV. 
Section V concludes the paper. 
II. RELATED WORK 
The integration of IEC 61850 and OPC UA provides an opportunity to extend interoperability with different information 
domains in a standard format. In [18], a hierarchical control, 
monitoring and diagnosis applications for smart grid automation were presented. A JADE multi agent platform was linked 
to PLC and distributed control system (DCS) field devices using OPC DA (Data Access) servers for maintenance planning 
system and repairs on monitored industrial devices [19]. An 
internet-of-energy based virtual power plant (VPP) controller 
scheme was proposed using IEC 61850 and OPC UA semantic 
services [20]. The proposed model is composed of physical 
electric grid assets, a communication network, ontology layer 
and service layers. In [21], an autonomous regional network 
management system with its own multi-agent system application known as the Au RA-NMS was proposed. The platform 
was developed in partnership between several UK universities, 
distribution network operators and equipment manufacturers. 
A modular agent-based smart grid simulation platform mosaik 
was proposed [22]. This platform allows for large-scale deployment tests of smart grid concepts. In [23], the extension of 
this simulation platform utilizing the OPC UA interface was 
presented. Unfortunately, none of the listed references address 
the hardware-in-the-loop control challenges. With this motivation, this paper presents a state-of-the-art framework platform 
using IEC 61850 and FIPA standards. 
III. CYBER-PHYSICAL FRAMEWORK 
A cyber-physical framework consists of physical and cyber 
components. Actual physical components are the sensors, 
actuators, generation units, circuit breakers and distribution 
lines. Cyber components are the data informational 
representation of the actual physical models with a 
standardized protocols. This section briefly explains the 
hardware and the data information model of the proposed 
framework. 
 
IED1/XCBR$ST$Pos$st Val
Attribute: Boolean
Data: Switch Position
Functional Constraint: Status
Logical Node: Circuit Breaker
Logical Group: Switchgear
Logical Device: IED
 
Fig.1. Object name of a circuit breaker position value 
 
A. IEC 61850 Framework 
When it comes to interoperability in a smart grid, IEC 
61850 is the most promising standard for future grids. Selfdescribing devices and object-oriented peer-to-peer data 
exchange capabilities are the most significant superiorities of 
IEC 61850 over the other common standards. The use of 
names for all the data, virtualized models, standardized 
configuration language, lower cabling and transducer 
installation costs are some of the numerous key features and 
benefits [24]. Logical nodes (abstract data objects) are the 
main elements of IEC 61850 object oriented virtual model, 
which consists of standardized data and data attributes. IEC 
61850 defines the abstract communication service interface 
(ACSI), which creates objects and services independent of any 
protocols. This enables a hierarchical class model, in which all 
class information, services that operate on these classes, and 
associated parameters can be accessed from a communication 
network [25]. The abstract interface allows the data objects to 
be mapped to any other protocol, such as manufacturing 
messaging specification (MMS) protocol and sampled measured values (SMV) protocol on Ethernet data frame. 
 The virtual model aims to express a physical (logical) device 
and number of logical nodes. IEC 61850 standardized 91 logical nodes into 13 logical groups. Each logical node contains 
data elements (DATA), which are standard and related to logical node functions. Most of the data objects are composed of 
common data classes (CDC), which involves basic data 
objects, status, control, and measurement. Each data element 
consists of a number of data attributes with a data attribute 
type (DAType) which belongs to functional constraints (FC). 
Fig.1. shows a sample anatomy of an object name for a 
breaker position value. A physical device is defined by a 
network address. 
 
T(0)
T1 T1
T2
T3
T0
Time of transmission
T0
T0
retransmission in stable condition (no events for long time)
T(0)
retransmission in stable conditions may be shorter by event 
T1 shortest retransmission time after the event
T2,T3
retransmission time until achieving the stable condition time
Event

Fig.2. GOOSE messaging [26] 
 
Generic object oriented substation events (GOOSE) is a 
multicast model based on a publisher-subscriber mechanism 
within the IEC 61850 framework, which ensures fast 
messaging with a 4 ms period of time.

---


### Page 4

GOOSE messages are periodically sent from the publisher 
IEDs to subscribers with To retransmission time period. 
Should an event occur related to GOOSE control, a new 
message is generated momentarily, then the message is 
continuously retransmitted with variable time periods (T1, T2, .. 
,Tn) until it reaches the To value again as shown in Fig. 2. This 
retransmitting scheme ensures the appropriate level of reliability. The fast messaging capability of the GOOSE model is 
widely used in modern power system protection applications, 
bringing forth a new era of advanced high speed peer-to-peer 
communication. The details relating to the GOOSE model of 
messaging is out-of-scope of this work, thus further 
information can be obtained from the related standard [26]. 
 
Node
Variable1
Object1
Method1
Attributes
Display Name=…..
Node Id=…..
Event Notifier=…..
Event
Notifications
Data Change
Notifications
Write Data
Invoke 
Methods
OPC UA Server Address Space
OPC UA 
Client
Variable2
Variable3
Method2
 
Fig.3. OPC UA nodeclass [27] 
 
B. OPC UA 
OPC was originally utilized to abstract various PLC protocols 
into an interoperable interface for a secure and reliable data 
exchange. The advent of smart grid interoperability efforts led 
to the development of OPC UA, which keeps all the functionality of the original OPC Data Access (DA), but switches from 
Microsoft-COM/DCOM technology to state-of-the-art web 
services technology. OPC UA is not directly compatible with 
the classic OPC since they use different technology. OPC UA 
uses a framework based on client and server architecture, in 
which the server provides real-time data to clients. Moreover, 
it can be implemented with Java or .Net platforms eliminating 
the need to use Microsoft Windows based platforms. This 
provides a perfect opportunity to model multi-agent based 
systems on Unix/Linux systems. The OPC UA modeling is 
based on nodes and references between the nodes. A node can 
have different sets of attributes connected through references. 
A nodeclass is composed of objects, variables and methods. A 
variable contains the value which clients can read, write and 
subscribe to the changes of the value. A method is similar to a 
function called by client and returns a result. The OPC UA 
address space is structured with objects containing only the 
node attributes. Further information can be obtained from the 
reference [27]. 
( inform
 :sender agent1
 :receiver hpl-auction-server
 :content
 (price (bid good02) 150)
 :in-reply-to round-4
 :language sl
 :ontology hpl -auction
)
ACL message
Begin message 
structure
Communicative 
act type
Message 
Parameter
Message content 
expression
Parameter 
expression
Fig.4. ACL message components [28] 
 
C. FIPA Specifications and JADE Platform 
An agent is an interacting object with its own thread of control that operates autonomously. The ideal agent is also expected to have semantic interoperability based on internal 
decision making [17]. The standardization of agent-based 
technologies is an ongoing research that few standards have 
yet to realize to its fullest potential. FIPA specifications help 
to allow an easy interoperability between agent systems with 
agent communication language and transport level protocols. 
Agent 
communication 
language 
(ACL) 
represents 
a 
communicative act or messages intended to perform some 
action, with precisely defined syntax and semantics. Fig. 4 
shows the components of a sample ACL message. 
The beginning message structure of an ACL message 
expresses communicative acts such as (inform, request, refuse 
etc.). Sender and receiver parameters designate the name of 
the sender and intended recipient agents, respectively. Content 
involves the object of the action and parameters passed 
through the message. Message parameters define the 
expression of the agent responding to received messages, and 
which parameter is sent through the message. 
 The JADE (Java Agent Development Framework) platform 
is based on FIPA specifications which enables developers to 
create complex agent based systems with a high degree of interoperability using ACL messages [29]. A JADE agent, at its 
simplest, is a Java class that extends the core agent class 
which allows it to inherit behaviors for registration, 
configuration and general management of the agents. 
Send/receive messages can be implemented by calling basic 
methods using standard communication protocols and 
registering in several domains. External software can be 
integrated by the use of behavior abstraction, which enables 
the link with the OPC UA nodes along with the JADE agent 
messages [30]. 
 
D. IEDs and Hardware Components 
 The intelligent multi agent framework is implemented in a 
reconfigurable small scale power system available at Florida 
International University, Smart Grid Test Bed [31-34]. The 
platform consists of conventional and non-conventional 
generation units, transmission and load models, field sensors 
and actuators. Further information about the test bed can be 
obtained from above references. 
The IEDs are located on system buses to enable monitoring, 
control and protection. The agent platform was implemented 
on a single personal computer, however since the information 
is accessible through the network, the computation can be 
easily distributed [38]. An off-the-shelf OPC UA server [33]

---


### Page 5

was implemented to acquire IEC 61850 logical node 
measurements. An OPC UA client [35] was embedded in the 
Java platform to enable JADE to access mapped IEC 61850 
measurements. The overview of the laboratory setup is shown 
in Fig. 5. 
IV. SAMPLE USE CASE: DER ANCILLARY SERVICE 
A DER based autonomous ancillary service use case is 
demonstrated in real-time for validation of the proposed multi 
agent framework using the combination of IEC 61850 and 
FIPA standards. The IEEE guide 1547.3 defines DER 
interoperability issues by means of monitoring, information 
exchange, and control. Some use cases are demonstrated as 
business operations of the DERs and stakeholder entities with 
direct communication interactions [36]. 

Fig. 5 Agent platform and laboratory setup 
 
This case study was adopted from IEEE 1547.3 guide to 
provide a prototype demonstration of the developed 
framework. The DER units can be utilized to provide ancillary 
services such as load regulation and reactive power support in 
distribution feeders. Especially in peak hours, the excessive 
energy demand may result in overloading of the distribution 
lines by drawing excessive current. This would result in 
thermal overheating and voltage drops beyond permissible 
limits on different parts of the feeder. Scheduled operation of 
DERs would provide a solution to relieve such overloading 
problems by contributing with either active or reactive power 
support [39]. According to [37]-[40], DER operators and the 
area electric power system operator (AESPO) interact with 
each other though messages. These two entities can be 
considered as intelligent agents with the following duties and 
attributes: 
 
1) AESPO 
It is the responsible entity for safe and reliable operation of 
the distribution power system. The complete utility grid model 
is the property of AESPO. 
2) DER Operator 
It is the main responsible entity for DER generation units. 
Monitoring, protection and control of the units are handled by 
DER operators. 
 
AESPO and DER operator are the two entities that carry out 
the stated ancillary service mechanisms. The decentralized 
collaboration of AESPO and DER operators is based on an 
autonomous event-driven information exchange model, which 
requires implementation of agents featuring actuators, sensors, 
embedded intelligent decision making algorithms, and 
communication channels. 
 
Utility
DER1 Operator agent
DER1 Synchronizer agent
AESPO 
agent
Jade Platform
OPC UA Java Client
OPC UA IEC 61850 Server
DER1
DER2 Operator agent
DER2 Synchronizer agent
Governor
AVR
DER2
Governor
AVR
System 
Load
PLC (Gen1)
IED (AESPO)
PLC (Gen2)
IED 
(Gen1)
IED 
(Gen2)
Fig. 6 IED deployment and agents 
 
Fig. 6 illustrates the laboratory deployment of the multi 
agent framework, IEDs, PLCs, line models, loads, DERs, 
automatic voltage regulators (AVR) and governors. 
 
DR Operator Agent
DR Synchronizer Agent
AESPO Agent
Overloading 
occurs
Request for 
DR Ancillary 
Services
Agree to 
Supply Power
Inform for 
Synchronization
IEC 61850 RYSN 
function is enabled
Acknowledge of 
Synchronization
DR Unit 
Operation
Inform Operational 
Information 
Periodically
Overloading 
Subside
Agree to 
Shutdown
IEC 61850 RYSN 
function is disabled
CBR is Opened
Inform for 
Disconnect
Shutdown 
Occurs
Request for DR 
Ancillary Services 
Suspention
 
Fig. 7 Ancillary service use case UML flowchart 
 
The cooperation agreement of the entities is established by 
sent/received messages from each parties in a certain form and 
an understandable content. This common or shared structured 
vocabulary is referred as the system ontology. Ontologies are 
constructed with a consistent relationship within an 
application domain. Abstraction is a way to express the real

---


### Page 6

world objects with their characteristics, attributes and 
interaction with other entities. Prior to actual computer code 
implementation, unified modeling language (UML) tools are 
utilized to provide a meaningful abstract modeling of the 
emulated case. Event-driven sequencing outcome of the case 
presented in this paper is illustrated in Fig. 7. In this use case, 
AESPO agent and DER operator agents are defined in the 
JADE platform. The AESPO agent is intended to continuously 
check the critical current flow value from the beginning point 
of the feeder through the IEC 61850 current measurement 
(CMMXU) logical node. 
When the current flow from the feeder reaches its critical 
value, the high-alarm node LDO.CMMXU.Hi Alm.st Val of the 
function block becomes high. The AESPO agent is monitoring 
this value through the OPC UA client. According to embedded 
intelligent decision making algorithm an ancillary service 
support Request message is published to DER operator agents 
which are registered to the directory service (yellow pages). 
The yellow page is a service mechanism, in which an agent 
can find other agents providing the services it requires in order 
to achieve its goals. The directory facilitator (DF) is the agent 
that provides yellow page service to the agent platform. The 
AESPO agent periodically looks up available operators from 
the DF agent. A random availability function is defined for 
each DER operator to define whether to issue an Agree or 
Reject message in return. Fig. 8 shows the correspondence 
between the AESPO agent and two DERs. 

Fig. 8. Correspondence between JADE agents 
 
If the DER operator agrees to provide ancillary service, it 
autonomously enables the DER synchronizer agent. The DER 
synchronizer agent is the IEC 61850 synchronism check 
(RSYN) logical node of the IED and it is not defined in JADE 
platform. The DER synchronizer agent continuously checks 
the condition across the circuit breaker from the bus and line 
parts of the power system and gives the permission to close 
the circuit breaker when the synchronization conditions are 
satisfied. The determination of the closing signal is defined 
according to frequency and phase angle difference. The 
monitored frequency and phase angle difference value is 
continuously read by PLC in order to adjust the governor 
speed. U_BUS and U_LINE are bus voltage and line voltage 
measurements, respectively. The synchronization status can be 
obtained from the function block by SYNC_INPRO 
(synchronization in progress) or SYNC_OK (in synchronism). 
LLDB (live line, dead bus), LLLB (live line, live bus), DLLB 
(dead line, live bus), DLDB (dead line, dead bus) outputs 
designate the health of the line and bus. 
Fig.9 (a)-(b) shows the frequency and phase angle difference 
of the DER and AESPO. The figures cover 30 seconds of the 
synchronization process. From the 35th to 65th second, the 
generator output frequency decreased manually by decresing 
the applied torque to the generator shaft from the governor. At 
the 70th second, the utility and generator frequency match, thus 
the synchronizer switch is closed. At the 76th second, the 
applied torque to the generator shaft was increased to deliver 
more power to the system. Fig.9 (b) shows the phase angle 
difference between of AESPO and DER voltage. As 
synchronization occurs at the 70th second, the phase angle 
difference decreases to a value almost equal to zero. This 
clearly shows that the generator is synchronized to the utility. 

Fig. 9. (a) Frequency change (b) Phase angle difference 
V. CONCLUSION 
This paper presented a real-time implementation of a 
laboratory based intelligent multi agent framework using IEC 
61850 and FIPA standards. The IEC 61850, OPC UA, JADE 
platforms and a hardware setup were introduced as a complete 
cyber-physical structure. Merging these multi agent legacy 
protocols proposes an enhanced interoperability framework 
for future smart grid deployments. Experimental results are 
given in order to validate the effectiveness of the proposed 
framework. The proposed framework is highly recommended 
for secondary and tertiary level intelligent multi agent based 
decentralized control schemes such as voltage/frequency 
regulation and economic issues in the power systems.

---


### Page 7

REFERENCES 
[1] Cintuglu, Mehmet Hazar, and Osama Mohammed. "Simulation of 
digitalized power system using PMU and intelligent control." Industry 
Applications Society Annual Meeting, 2013 IEEE. IEEE, 2013. 
[2] Zhabelova, G.; Vyatkin, V., "Multiagent Smart Grid Automation Architecture 
Based 
on 
IEC 
61850/61499 
Intelligent 
Logical 
Nodes," Industrial Electronics, IEEE Transactions on , vol.59, no.5, 
pp.2351,2362, May 2012 
[3] Hui Wan; Li, K.K.; Wong, K.P., "An Adaptive Multiagent Approach to 
Protection Relay Coordination With Distributed Generators in Industrial 
Power Distribution System," Industry Applications, IEEE Transactions 
on , vol.46, no.5, pp.2118,2124, Sept.-Oct. 2010 
[4] Apostolov, Alexander. "Multi-agent systems and IEC 61850." Power 
Engineering Society General Meeting, 2006. IEEE. IEEE, 2006. 
[5] Chun-Xia Dou; Bin Liu, "Multi-Agent Based Hierarchical Hybrid 
Control for Smart Microgrid," Smart Grid, IEEE Transactions on , 
vol.4, no.2, pp.771,778, June 2013 
[6] Foo.Eddy, Y.S.; Gooi, H.B.; Chen, S.X., "Multi-Agent System for Distributed 
Management 
of 
Microgrids," Power 
Systems, 
IEEE 
Transactions on , vol.30, no.1, pp.24,34, Jan. 2015 
[7] Kumar Nunna, H.S.V.S.; Doolla, S., "Multiagent-Based Distributed-Energy-Resource Management for Intelligent Microgrids," Industrial Electronics, IEEE Transactions on , vol.60, no.4, pp.1678,1687, April 2013 
[8] Meiqin Mao; Peng Jin; Hatziargyriou, N.D.; Liuchen Chang, 
"Multiagent-Based 
Hybrid 
Energy 
Management 
System 
for 
Microgrids," Sustainable Energy, IEEE Transactions on , vol.5, no.3, 
pp.938,946, July 2014 
[9] Cintuglu, Mehmet Hazar, Harold Martin, and Osama Mohammed. 
"Real-Time Implementation of Multiagent-Based Game Theory Reverse 
Auction Model for Microgrid Market Operation." Smart Grid, IEEE 
Transactions on 6.2 (2015): 1064-1072. 
[10] Dimeas, A.L.; Hatziargyriou, N.D., "Operation of a Multiagent System 
for Microgrid Control," Power Systems, IEEE Transactions on , vol.20, 
no.3, pp.1447,1455, Aug. 2005 
[11] Mc Morran, A., et al. "Addressing the Challenge of Data Interoperability 
for Off-Line Analysis of Distribution Networks in the Smart Grid, IEEE 
PES Transmission and Distribution Conference and Exposition, Orlando." FL. May (2012). 
[12] Von Dollen, Don. "Report to NIST on the smart grid interoperability 
standards roadmap." Electric Power Research Institute (EPRI) and National Institute of Standards and Technology (2009). 
[13] IEEE Vision for Smart Grid Communications: 2030 and Beyond," IEEE 
Vision for Smart Grid Communications: 2030 and Beyond, pp.1,390, 
May 31 2013 
[14] Leccese, F., "An overwiev on IEEE Std 2030," Environment and 
Electrical Engineering (EEEIC), 2012 11th International Conference 
on , vol., no., pp.340,345, 18-25 May 2012 
[15] Communication Networks and Systems for Power Utility Automation 
for Distributed Energy Resources (DER) — Part 7–420, IEC61850, Int. 
Electrotech. Committee, 2011. 
[16] Odell, James, and Marian Nodine. "The foundation for intelligent 
physical agents." Retrievable at: http://www. fipa.org (2006). 
[17] Bellifemine, Fabio, Agostino Poggi, and Giovanni Rimassa. "JADE–A 
FIPA-compliant agent framework." Proceedings of PAAM. Vol. 99. No. 
97-108. 1999. 
[18] Srinivasan, S.; Kumar, R.; Vain, J., "Integration of IEC 61850 and OPC 
UA for Smart Grid automation," Innovative Smart Grid Technologies - 
Asia (ISGT Asia), 2013 IEEE , vol., no., pp.1,5, 10-13 Nov. 2013 
[19] Diaconescu, E.; Spirleanu, C., "Communication solution for industrial 
control applications with multi-agents using OPC servers," Applied and 
Theoretical Electricity (ICATE), 2012 International Conference on , 
vol., no., pp.1,6, 25-27 Oct. 2012 
[20] Sucic, S.; Rohjans, S.; Mahnke, W., "Semantic smart grid services: Enabling a standards-compliant Internet of energy platform with IEC 61850 
and OPC UA," EUROCON, 2013 IEEE , vol., no., pp.1375,1382, 1-4 
July 2013 
[21] Davidson, E.M.; Mc Arthur, S.D.J., "Exploiting Multi-agent System 
Technology within an Autonomous Regional Active Network 
Management System," Intelligent Systems Applications to Power 
Systems, 2007. ISAP 2007. International Conference on , vol., no., 
pp.1,6, 5-8 Nov. 2007 
[22] Rohjans, S.; Lehnhoff, S.; Schutte, S.; Scherfke, S.; Hussain, S., "mosaik 
- A modular platform for the evaluation of agent-based Smart Grid control," Innovative Smart Grid Technologies Europe (ISGT EUROPE), 
2013 4th IEEE/PES , vol., no., pp.1,5, 6-9 Oct. 2013 
[23] Schutte, S.; Niesse, A.; Rohjans, S.; Rohlfs, H., "OPC UA compliant 
coupling of multi-agent systems and Smart Grid simulations," Industrial 
Electronics Society, IECON 2013 - 39th Annual Conference of the 
IEEE , vol., no., pp.7576,7581, 10-13 Nov. 2013 
[24] Mackiewicz, R.E., "Overview of IEC 61850 and Benefits," Power Systems Conference and Exposition, 2006. PSCE '06. 2006 IEEE PES , vol., 
no., pp.623,630, Oct. 29 2006-Nov. 1 2006 
[25] Communication Networks and Systems in Substations — Part 7–2, 
Basic Communication Structure for Substation and Feeder EquipmentAbstract Communication Service Interface (ACSI), IEC61850, Int. 
Electrotech. Committee, 2003. 
[26] Communication Networks and Systems in Substations — Part 8–1, Specific Communication Service Mapping (SCSM)- Mappings to MMS 
(ISO 9506-1 and ISO 9506-2) and to ISO/IEC 8802-3, IEC61850, Int. 
Electrotech. Committee, 2003. 
[27] Mahnke, Wolfgang, Stefan-Helmut Leitner, and Matthias Damm. OPC 
unified architecture. Springer, 2009. 
[28] Fipa, F. I. P. A. specification part 2: Agent communication language. 
Technical report, FIPA-Foundation for Intelligent Physical Agents, 
1997. 
[29] Bellifemine, 
Fabio, 
Agostino 
Poggi, 
and 
Giovanni 
Rimassa. 
"Developing multi-agent systems with a FIPA-compliant agent 
framework." Software-Practice and Experience 31.2 (2001): 103-128. 
[30] Bellifemine, Fabio Luigi, Giovanni Caire, and Dominic Greenwood. Developing multi-agent systems with JADE. Vol. 7. John Wiley & 
Sons, 2007. 
[31] V. Salehi, A. Mohamed, A. Mazloomzadeh, and O. A. Mohammed, "Laboratory-Based Smart Power System, Part I: Design and System Development," IEEE Transactions on Smart Grid, vol.3, no.3, pp.1394-1404, 
Sept. 2012 
[32] V. Salehi, A. Mohamed, A. Mazloomzadeh, and O.A. Mohammed, "Laboratory-Based Smart Power System, Part II: Control, Monitoring, and 
Protection," IEEE Transactions on Smart Grid, vol.3, no.3, pp.14051417, Sept. 2012 
[33] Mazloomzadeh, Ali, Mehmet Hazar Cintuglu, and Osama Mohammed. 
"Islanding detection using synchronized measurement in smart 
microgrids."Innovative Smart Grid Technologies Latin America (ISGT 
LA), 2013 IEEE PES Conference On. IEEE, 2013. 
[34] Cintuglu, Mehmet Hazar, and Osama Mohammed. "Islanding detection 
in microgrids." Power and Energy Society General Meeting (PES), 2013 
IEEE. IEEE, 2013. 
[35] Kepware Technologies. [Online]. Available: http://www.kepware.com 
/Support_Center/Support Documents/OPC_UA_Connectivity_Guide.pdf 
(2015, January) 
[36] JEasy OPC. [Online]. Available: http://jeasyopc.sourceforge.net/ (2015, 
January) 
[37] IEEE Guide for Monitoring, Information Exchange, and Control of Distributed Resources Interconnected with Electric Power Systems," IEEE 
Std 1547.3-2007 , vol., no., pp.1,160, Nov. 16 2007 
[38] Mazloomzadeh, Ali, Mehmet H. Cintuglu, and Osama A. Mohammed. 
"Development and evaluation of a laboratory based phasor measurement 
devices." Innovative Smart Grid Technologies Conference (ISGT), 2015 
IEEE Power & Energy Society. IEEE, 2015. 
[39] Cintuglu, Mehmet H., Ahmed T. Elsayed, and Osama A. Mohammed. 
"Microgrid automation assisted by synchrophasors." Innovative Smart 
Grid Technologies Conference (ISGT), 2015 IEEE Power & Energy 
Society. IEEE, 2015. 
[40] Cintuglu, Mehmet H., Tarek A. Youssef, Ahmed T. Elsayed, and Osama 
A. Mohammed. "Frequency and voltage control of microgrids upon 
unintentional cascading islanding." In Southeast Con 2015, pp. 1-6. 
IEEE, 2015. 

View publication stats

---
