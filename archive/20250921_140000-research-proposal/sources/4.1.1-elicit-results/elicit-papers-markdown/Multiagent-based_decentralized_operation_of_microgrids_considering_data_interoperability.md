# Multiagent-based decentralized operation of microgrids considering data interoperability

## Paper Metadata

- **Filename:** Multiagent-based decentralized operation of microgrids considering data interoperability.pdf
- **DOI:** 10.1109/smartgridcomm.2015.7436334
- **Authors:** Cintuglu, Mehmet H. and Mohammed, Osama A.
- **Year:** 2015
- **Journal/Venue:** 2015 {IEEE} {International} {Conference} on {Smart} {Grid} {Communications} ({SmartGridComm})
- **URL:** http://dx.doi.org/10.1109/SmartGridComm.2015.7436334
- **Extraction Date:** 2025-06-03T15:01:22.232321
- **Total Pages:** 7

## Abstract



## Keywords



---

## Full Text Content



### Page 1

See discussions, stats, and author profiles for this publication at: https://www.researchgate.net/publication/304416620
Multiagent-based decentralized operation of microgrids considering data
interoperability
Conference Paper · November 2015
DOI: 10.1109/Smart Grid Comm.2015.7436334
CITATIONS
25
READS
168
2 authors:
Mehmet Hazar Cintuglu
ABB
40 PUBLICATIONS   2,220 CITATIONS   
SEE PROFILE
Osama A Mohammed
Florida International University
721 PUBLICATIONS   15,721 CITATIONS   
SEE PROFILE
All content following this page was uploaded by Mehmet Hazar Cintuglu on 11 July 2016.
The user has requested enhancement of the downloaded file.

---


### Page 2





























































Abstract—Transition from conventional power distribution to 
active distribution networks requires extensive integration of 
decentralized microgrid control capabilities with on-demand 
industrial data interoperability. This paper presents a decentralized hierarchical microgrid operation scheme with a multiagent 
framework using IEC 61850 and the foundation for intelligent 
physical agents (FIPA) standards. The conducted studies are 
mainly focused on secondary and tertiary control levels. Secondary control deals with the operational reliability of the microgrid 
with a decentralized remote interaction between distributed energy resources (DER) and microgrid operator. Tertiary level 
presents the aggregated operation of multiple microgrids aiming 
to enhance the reliability of the host grid with ancillary services. 
Experimental results are presented in a laboratory based test bed 
involving actual intelligent electronic devices (IED) and multiple 
microgrids. 
 
Index Terms—Microgrid, FIPA, smart grid, cloud, multiagent, 
IEC 61850, Jade, hierarchical control, OPC UA, decentralized 
control, interoperability 
I. INTRODUCTION 
ENTRALIZED methods of operation are more susceptible to single point failures, where managing the vast 
number of data generated from the extensive deployment of 
smart devices becomes infeasible. Due to their inherent resilience, decentralized methods have drawn considerably more 
attention than centralized methods. Decentralized control approaches intend to provide autonomy for hierarchical control 
layers by enabling a bidirectional event-driven peer-to-peer 
communication structure, where central control schemes mainly rely on one way master-slave messaging interactions [1]. 
 In power system applications, the implementation of decentralized control is established using multi-agent frameworks, 
which are composed of interacting multiple intelligent agents 
to achieve a global or a local objective function. Multi-agent 
based schemes are widely applied to power system controls in 
literature; including self-healing, resilient grid automation [2]-
[3] and power system protection [4]-[5]. Multiagent-based 
microgrid control draws considerably more attention than any 
other smart grid applications as one of the main assets of 
emerging active distribution network concept [6]. Multi-agent 
based hierarchical hybrid control for microgrid is proposed to 
maintain voltage and maximize economic benefit [7]. In [8] 
 
This work was partially supported by grants for the Office of Naval Research. The authors are with the Energy Systems Research Laboratory, Department of Electrical and Computer Engineering, Florida International University, Miami, FL 33174 (e-mail: mohammed@fiu.edu). 
and [9], multi-agent based distributed energy resource (DER) 
management of microgrids are presented. Microgrid market 
operations are implemented in a simulation [10], in a real-time 
digital simulator [11] and in a laboratory-based hardware platform [12] using multi-agent based controls. 
 Although many multiagent-based microgrid studies have 
been reported, none of the previous works address the industrial data interoperability, which is crucial for actual field deployment. Most of the works have been validated in simulation environments where data interoperability of the cyberphysical components have never been an issue. In reality, an 
agent requires to interact with its environment through sensors 
and actuators. A sensor acquires the data from the outside 
world and the actuator responds according to the agent’s decision. For actual implementation of decentralized control 
schemes in power systems, it is imperative to link multi-agent 
objects to distributed industrial control systems such as smart 
meters, phasor measurement units (PMU) [13], intelligent 
electronic devices (IED) and programmable logic controllers 
(PLC) [14]. The required interface is established through a 
combination of interoperable data and protocols. 
 Interoperability of the field devices with an agent based 
communication capability is one of the challenges to accomplish decentralized control of smart grid infrastructure. Attempts to extend IEC 61850 protocol with IEC 61850-7-420 
for distributed energy resource (DER) control are promising, 
however, the smart grid concept covers extensive control, automation and protection applications such that a single standard cannot meet all the required forms of monitoring and information exchange [15]. Hierarchical control of the microgrids require interaction with utilities for dynamic management of the primary, secondary and tertiary control levels 
[16]. To achieve future microgrid decentralized control goals, 
advanced intelligent multiagent frameworks are required with 
the flexible ability to create tailor-made decentralized control 
schemes while following the power system legacy protocols. 
The foundation for intelligent physical agents (FIPA) is an 
organization which intends to evolve inter-operable agent 
communications with semantically meaningful messages, such 
as how messages are transferred and presented as objects [17]. 
Java agent development framework (JADE) is a software 
framework to develop agents compliant with FIPA standards 
with flexible agent behavior methods [18]. The flexibility of 
the java environment facilitates tailor-made agent implementation. Taking the specific benefits of two major frameworks, 
this work intends to provide a flexible multi-agent framework 
for decentralized hierarchical control of microgrids merging 
Multiagent-Based Decentralized Operation of 
Microgrids Considering Data Interoperability 
Mehmet H. Cintuglu, Student Member, and Osama A. Mohammed, Fellow, IEEE 
C
IEEE Smart Grid Comm'15 Symposium - Architecture and Control 1570139501
1
2015 IEEE International Conference on Smart Grid Communications (Smart Grid Comm): Architectures, Control and Operation for
Smart Grids and Microgrids
978-1-4673-8289-2/15/$31.00 ©2015 IEEE
404

---


### Page 3

the IEC 61850 and FIPA standards. The open connectivity 
unified architecture (OPC UA) is adopted as a middleware and 
a cloud data service is integrated to provide real-time information exchange though the internet to enhance the data availability for remote access points [19-23]. 
Briefly, the major contributions of this paper presents are: 
1) a tailor-made flexible hybrid multi-agent framework for 
secondary and tertiary levels for hierarchical microgrid operation considering legacy power system data protocols explicitly 
IEC 61850 and FIPA standards; 2) the integration of the proposed framework with a cloud real-time data service to provide ubiquitous data interoperability and remote location data 
access; and 3) a unique laboratory-based cyber-physical infrastructure to validate the proposed framework. 
The remainder of the paper is as follows. Section II gives an 
overview of the hierarchical control of microgrids. In Section 
III, the developed cyber-physical multiagent framework is 
explained in detail. Section IV demonstrates the hardware 
setup and the real-time experimental results of the secondary 
and tertiary level microgrid control experiments. The conclusion and discussion are stated in Section VI. 
II. HIERARCHICAL MICROGRID CONTROL 
Hierarchical control of microgrids is a compromise between 
fully centralized and fully decentralized control schemes [24]. 
In literature, three distinct control levels are introduced according to control response speed and communication infrastructure requirements. Primary control level deals with output 
power control of each individual DER unit, which is based on 
local measurements and in general depending on the control 
method (e.g droop control), does not require remote decentralized communication. Hence, this control level is not one of the 
primary concerns of this paper. 
Secondary control deals with the economical and operational reliability of the microgrids. Two distinct approaches can be 
implemented in this level: (i) centralized; and (ii) decentralized. Centralized methods are extensively covered in literature. Although this control method provides an opportunity to 
use advanced optimization tools, the major drawback of the 
centralized methods are the requirement of high communication capability with a powerful central controller thus being 
susceptible to single point, failure, which can easily compromise the system with a complete collapse. Agent based communication approaches are well-suited for decentralized controls in secondary level for cooperation inside the microgrid 
especially for stand-alone systems. Secondary control is 
achieved by DER units which are generally located in same 
microgrid, and are not widely dispersed, so long distance 
communication is not a major concern. 
Tertiary control can be assumed as the interaction of multiple microgrids with a host grid. Aggregated cooperation of 
multiple microgrids enhances the reliability of the host grid 
with ancillary services such as voltage and frequency regulation. Since a vast amount of information is required for this 
highly complex system, decentralized methods are more favorable for this geographically dispersed system. Since controllers are located at remote location, advanced communication infrastructures are required such as cloud-based services. 
 
^WKKƉĞƌĂƚŽƌ
dĞƌƚŝĂƌǇ>ĞǀĞůŽŶƚƌŽů
,ŽƐƚ'ƌŝĚŽŶƚƌŽů
hƉĚĂƚĞƌĂƚĞ͗ŵŝŶƵƚĞƐ
;Ğ͘ŐĂŶĐŝůůĂƌǇƐĞƌǀŝĐĞ͕ĂƵĐƚŝŽŶͿ
DŝĐƌŽŐƌŝĚKƉĞƌĂƚŽƌ
^ĞĐŽŶĚĂƌǇ>ĞǀĞůŽŶƚƌŽů
ZKƉĞƌĂƚŽƌ
WƌŝŵĂƌǇ>ĞǀĞůŽŶƚƌŽů
Z>ŽĐĂůŽŶƚƌŽů
/ŵŵĞĚŝĂƚĞƌĞƐƉŽŶƐĞ
;Ğ͘ŐƉŽǁĞƌƐŚĂƌŝŶŐ͕ƉƌŽƚĞĐƚŝŽŶͿ
DŝĐƌŽŐƌŝĚŽŶƚƌŽů
hƉĚĂƚĞƌĂƚĞ͗ƐĞĐŽŶĚƐ
;Ğ͘ŐŽƉƚŝŵŝǌĂƚŝŽŶ͕'Ϳ
 
Fig.1. Hierarchical control of a microgrid 
 
The IEEE guide 1547.3 defines DER interoperability issues 
by means of monitoring, information exchange, and control. 
Some use cases are demonstrated as business operations of the 
DERs and stakeholder entities with direct communication interactions [25]. In this study, we adopted a model in which 
three control levels are defined hierarchically and linked to 
appropriate agents as shown in Fig.1: (i) area electric power 
system operator (AESPO); (ii) Microgrid operators; (iii) DER 
operators. 
• AESPO: is the responsible entity for safe and reliable operation of the host grid. The complete utility grid model is the 
property of AESPO. Tertiary level controls are handled by 
interaction of AESPO and Microgrid Operators such as economic dispatch of the units and the auction process. 
• Microgrid Operator: is the main responsible entity for monitoring, dispatch and control of the units inside the microgrid. 
Secondary controls are handled with interaction of Microgrid 
Operators and DER Operators such as optimization and automatic generation control (AGC). 
• DER Operator: is the main responsible entity for individual 
DER generation units. Monitoring, protection and primary 
control of the units are handled by DER operators such as 
power sharing and protection. 
III. PROPOSED MULTI-AGENT FRAMEWORK 
This section briefly explains the hardware and data information model of the proposed framework. 
A. IEC 61860 Framework 
Self-describing devices and object-oriented peer-to-peer data exchange capabilities are the most significant superiorities 
of IEC 61850 over the other common standards. Logical nodes 
(abstract data objects) are the main elements of the IEC 61850 
object oriented virtual model, which consists of standardized 
data and data attributes. The virtual model aims to express a 
physical (logical) device and number of logical nodes. IEC 
61850 standardized 91 logical nodes into 13 logical groups. 
 
/ϭͬyZΨ^dΨWŽƐΨƐƚsĂů
ƚƚƌŝďƵƚĞ͗ŽŽůĞĂŶ
ĂƚĂ͗^ǁŝƚĐŚWŽƐŝƚŝŽŶ
&ƵŶĐƚŝŽŶĂůŽŶƐƚƌĂŝŶƚ ͗^ƚĂƚƵƐ
>ŽŐŝĐĂůEŽĚĞ ͗ŝƌĐƵŝƚƌĞĂŬĞƌ
>ŽŐŝĐĂů'ƌŽƵƉ͗^ǁŝƚĐŚŐĞĂƌ
>ŽŐŝĐĂůĞǀŝĐĞ͗/
 
Fig.2. Object name of a circuit breaker position value 
 
2
2015 IEEE International Conference on Smart Grid Communications (Smart Grid Comm): Architectures, Control and Operation for
Smart Grids and Microgrids
405

---


### Page 4

Each logical node contains data elements (DATA), which 
are standard and related to logical node functions. Most of the 
data objects are composed of common data classes (CDC), 
involving basic data objects, status, control, and measurement. 
Each data element consists of a number of data attributes with 
a data attribute type (DAType) which belongs to functional 
constraints (FC). Fig.2. shows a sample anatomy of an object 
name for a breaker position value. 
B. FIPA Specifications and JADE Platform 
Agent communication language (ACL) represents a communicative act or messages intended to perform some action, 
with precisely defined syntax and semantics. An agent is an 
interacting object with its own thread of control that operates 
autonomously. Fig.3. shows a representation of a message 
exchanged between interacting agents. The beginning message 
structure of an ACL message expresses communicative acts 
such as (inform, request, refuse etc.). Sender and receiver parameters designate the name of the sender and intended recipient agents, respectively. Content involves the object of the 
action and parameters passed through the message. 
Message parameters define the expression of the agent responding to received messages, and which parameter is sent 
through the message. The JADE (Java Agent Development 
Framework) platform is based on FIPA specifications which 
enables developers to create complex agent based systems 
with a high degree of interoperability using ACL messages 
[26]. JADE agent, at its simplest, is a Java class that extends 
the core agent class which allows it to inherit behaviors for 
registration, configuration and general management of the 
agents. Send/receive messages can be implemented by calling 
basic methods using standard communication protocols and 
registering in several domains. External software can be integrated by the use of behavior abstraction, which enables a link 
with OPC UA nodes along with JADE agent messages [27]. 
C. OPC UA 
OPC UA uses a framework based on client and server architecture, in which the server provides real-time data to clients. 
The OPC UA modeling is based on nodes and references between the nodes [28]. A node can have different sets of attributes connected through references. A nodeclass is composed 
of objects, variables and methods. A variable contains the 
value which clients can read, write and subscribe to the changes of the value. A method is similar to a function called by a 
client and returns a result. The OPC UA address space is 
structured with objects containing only the node attributes. 
 
;ƌĞƋƵĞƐƚ
͗ƐĞŶĚĞƌ^WKŐĞŶƚ
͗ƌĞĐĞŝǀĞƌDŝĐƌŽŐƌŝĚŐĞŶƚƐϭ͕Ϯ͕͘͘E
͗ĐŽŶƚĞŶƚ
;ŶĐŝůůĂƌǇ;^ǇŶĐϮŚŽƵƌƐͿϮϬŬtͿ
͗ŝŶͲƌĞƉůǇͲƚŽĂǀĂŝůĂďŝůŝƚǇ
͗ůĂŶŐƵĂŐĞƐů
͗ŽŶƚŽůŽŐǇŚƉůͲŶĐŝůůĂƌǇ^ĞƌǀŝĐĞ
Ϳ
>ŵĞƐƐĂŐĞ
ĞŐŝŶŵĞƐƐĂŐĞ
ƐƚƌƵĐƚƵƌĞ
ŽŵŵƵŶŝĐĂƚŝǀĞ
ĂĐƚƚǇƉĞ
DĞƐƐĂŐĞ
WĂƌĂŵĞƚĞƌ
DĞƐƐĂŐĞĐŽŶƚĞŶƚ
ĞǆƉƌĞƐƐŝŽŶ
WĂƌĂŵĞƚĞƌ
ĞǆƉƌĞƐƐŝŽŶ

Fig.3. ACL message components 

Fig. 4 Agent platform and laboratory setup 
D. Physical Hardware-Based Microgrid 
The proposed multi agent framework is implemented in a 
reconfigurable small scale power system available at Florida 
International University, Smart Grid Test Bed as shown in 
Fig.4 [29-30]. The IEDs are located on system buses to enable 
monitoring, control and protection. The agent platform is implemented on a single personal computer, yet the information 
is accessible through the network, the computation can be easily distributed. An off-the-shelf OPC UA server is implemented to acquire IEC 61850 logical node measurements. An OPC 
UA client is embedded in the Java platform to enable JADE to 
access mapped IEC 61850 measurements. The OPC UA data 
is published to the cloud-service, which can be utilized with 
remote OPC clients on the network. 
IV. EXPERIMENTAL RESULTS AND VALIDATION 
This section introduces the real-time experiments to validate 
the proposed multiagent framework. A tertiary level control is 
demonstrated with an ancillary service for load regulation in 
the host grid feeder. Islanding detection [31-32] and automatic 
generation control (AGC) cases are demonstrated as secondary 
level control examples. The cooperation and agreement of the 
entities is established by sent/received messages from each 
parties in a certain form and an understandable content. The 
related event-driven sequence outcome of the proposed control 
is illustrated in Fig. 5. The case study starts with an overloading situation in the feeder, which results in the AESPO agent 
requesting for ancillary service as tertiary level control case. 
 
KǀĞƌůŽĂĚŝŶŐ
KĐĐƵƌƐ
KǀĞƌůŽĂĚŝŶŐ
^ƵďƐŝĚĞ
ZĞƋƵĞƐƚĨŽƌ
DŝĐƌŽŐƌŝĚŶĐŝůůĂƌǇ
^ĞƌǀŝĐĞƐ
ZĞƋƵĞƐƚĨŽƌ
ŶĐŝůůĂƌǇ^ĞƌǀŝĐĞƐ
^ƵƐƉĞŶƚŝŽŶ
/ƐůĂŶĚŝŶŐKĐĐƵƌƐ
ZĞƋƵĞƐƚĨŽƌ
ƵƚŽŵĂƚŝĐ
'ĞŶĞƌĂƚŝŽŶŽŶƚƌŽů
ŐƌĞĞƚŽZĞŐƵůĂƚĞ
&ƌĞƋƵĞŶĐǇ
ŶĂďůĞ^ĞĐŽŶĚĂƌǇ
ŽŶƚƌŽů
/ŶĨŽƌŵKƉĞƌĂƚŝŽŶĂů
/ŶĨŽƌŵĂƚŝŽŶ
WĞƌŝŽĚŝĐĂůůǇ
/ŶĨŽƌŵKƉĞƌĂƚŝŽŶĂů
/ŶĨŽƌŵĂƚŝŽŶ
WĞƌŝŽĚŝĐĂůůǇ
/ϲϭϴϱϬZz^E
&ƵŶĐƚŝŽŶŝƐŶĂďůĞĚ
ŐƌĞĞƚŽ
^ǇŶĐŚƌŽŶŝǌĞ
^WKŐĞŶƚ
DŝĐƌŽŐƌŝĚŐĞŶƚƐ
ZŐĞŶƚƐ
 
Fig. 5 Event-driven sequence of hierarchical microgrid operation 
3
2015 IEEE International Conference on Smart Grid Communications (Smart Grid Comm): Architectures, Control and Operation for
Smart Grids and Microgrids
406

---


### Page 5

ŝƐƉĞƌƐĞĚ
&ĞĞĚĞƌ>ŽĂĚ
DŝĐƌŽŐƌŝĚͲϭͲ
DŝĐƌŽŐƌŝĚͲϮͲ
/;^WKͿ
/;D'ϭͿ
/;D'ϮͿ
KW
:
/ϲϭϴϱϬ
KW
:
/ϲϭϴϱϬ
KW
:
/ϲϭϴϱϬ
ůŽƵĚZĞĂůͲdŝŵĞĂƚĂ
dĞƌƚŝĂƌǇ>ĞǀĞůŽŶƚƌŽůŐĞŶƚƐ
• 
^WKĂŐĞŶƚ
• 
DŝĐƌŽŐƌŝĚŽƉĞƌĂƚŽƌĂŐĞŶƚ
• 
^ǇŶĐŚƌŽŶŝǌĂƚŝŽŶĂŐĞŶƚ
 
Fig. 6 Tertiary level control (ancillary service) cyber-physical setup 
 
When overloading subsides, the AESPO agent requests suspension of ancillary service, which leads to microgrid islanding and accordingly frequency regulation with secondary control by AGC 
A. Tertiary Control (Ancillary Service) 
Microgrids can be utilized to provide ancillary services such 
as load regulation and reactive power support in distribution 
feeders. Especially during peak hours, the excessive energy 
demand may result in overloading of the distribution lines by 
drawing excessive current. This would result in thermal overheating and voltage drops beyond permissible limits on different parts of the feeder. Scheduled operation of microgrids 
would provide a solution to relieve such overloading problems 
by contributing with either active or reactive power support. 
Fig.6. shows the laboratory deployment of the multi agent 
framework with IEC 61850 IEDs, the OPC server, a Jade platform and a cloud interface for the tertiary control level. In this 
use case, the AESPO agent and microgrid operator agents are 
defined in the JADE platform. 
The AESPO agent is intended to continuously check the 
critical current flow value from the beginning point of the 
feeder through the IEC 61850 three-phase current measurement CMMXU function block, which is a logical node inherited from MMXU for metering and measurements [16]. When 
the current flow from the feeder reaches its critical value, the 
high-alarm node LDO.CMMXU.Hi Alm.st Val of the function 
block becomes high. The AESPO agent monitors this value 
through the OPC UA client. According to the embedded decision making algorithm, an ancillary service support Request 
message is published to the microgrid operator agents registered to the directory service (yellow pages). Yellow page is a 
service mechanism in Jade platform, in which an agent can 
find other agents providing the services it requires in order to 
achieve its goals. The directory facilitator (DF) is the agent 
that provides yellow page service to the agent platform. The 
AESPO agent periodically looks up available operators from 
the DF agent. A random availability function is defined for 
each microgrid operator to define whether to issue an Agree or 
Refuse message in return. Fig. 7 shows the correspondence 
between the AESPO agent and two microgrid operator agents. 
If any of the microgrid operators agree to provide ancillary 
service, it enables the synchronizer agent. 

Fig. 7. Correspondence between AESPO agent and microgrid agents 
 
The synchronizer agent is the IEC 61850 synchronism 
check (RSYN) logical node of the IED and it is not defined in 
JADE platform. The synchronizer agent continuously checks 
the condition across the circuit breaker from bus and line regions of the power system and gives the permission to close 
the circuit breaker when the synchronization conditions are 
satisfied, where f is the frequency, φ is phase angle difference, and T is the time duration (1). Synchronization permission and circuit breaker closing signal is subject to frequency, 
phase angle difference and voltage values from both sides of 
the circuit breaker. The monitored frequency and phase angle 
difference value is continuously read by a PLC in order to 
adjust the governor speed. 

(
)
(
)
host
microgrid
threshold
threshold
host
microgrid
threshold
threshold
T
f
f
f
T
T
T
φ
φ
φ
−
≥
≥
−
≥
≥
 
(1) 
Fig.8 (a)-(b) shows frequency and phase angle difference of 
AESPO and microgrid. The figures cover 30 seconds of the 
synchronization process. Initially, the microgrid is operating at 
61 Hz. From the 35th to 65th second, the generator output 
frequency decreased manually by decresing the applied torque 
to the generator shaft from the governor. At the 70th second, 
the AESPO and microgrid frequency match, thus the 
synchronizer switch is closed. 

Fig. 8. (a) Frequency change (b) Phase angle difference 
^ǇŶĐŚƌŽŶŝǌĞĚ
KƉĞƌĂƚŝŽŶ 
^ǇŶĐŚƌŽŶŝǌĂƚŝŽŶ 
ŝŶƉƌŽĐĞƐƐ 
^ǇŶĐŚƌŽŶŝǌĞĚ
KƉĞƌĂƚŝŽŶ 
4
2015 IEEE International Conference on Smart Grid Communications (Smart Grid Comm): Architectures, Control and Operation for
Smart Grids and Microgrids
407

---


### Page 6

/ŶǀĞƌƚĞƌ
ĂƐĞĚZ
,ŽƐƚ'ƌŝĚ
/Ϯ
/ϯ
/ϰ
/ϱ
DŝĐƌŽŐƌŝĚ
DĂŝŶƵƐĂƌ
/ϭ
>ŽĐĂů>ŽĂĚ
'ŽǀĞƌŶŽƌ
s Z
W>
^ǇŶĐŚƌŽŶŽƵƐ
'ĞŶĞƌĂƚŽƌ

DŝĐƌŽŐƌŝĚ
ŵďĞĚĚĞĚ
ŽŶƚƌŽůůĞƌ
KWh^ĞƌǀĞƌ
KWhůŝĞŶƚ
:ĂĚĞ
DƵůƚŝŐĞŶƚ
WůĂƚĨŽƌŵ
ůŽƵĚ
ZĞĂůͲdŝŵĞ
ĂƚĂ
/ϲϭϴϱϬ
DŽĚďƵƐ
ZĂǁĚĂƚĂ
ͬ
ŽŶǀĞƌƚĞƌ
ͬ
ŽŶǀĞƌƚĞƌ >ŽĂĚ
ĂƚƚĞƌǇ
^ŽƵƌĐĞ
Ws
WĂŶĞů
^ĞĐŽŶĚĂƌǇŽŶƚƌŽůŐĞŶƚƐ
• 
DŝĐƌŽŐƌŝĚŽƉĞƌĂƚŽƌĂŐĞŶƚ
• 
ZŽƉĞƌĂƚŽƌĂŐĞŶƚ
• 
/ƐůĂŶĚŝŶŐĚĞƚĞĐƚŝŽŶĂŐĞŶƚ
 
Fig. 9. Secondary level control (AGC) cyber-physical setup 
 
At the 76th second, the applied torque to generator shaft is 
increased to deliver more power to the system. Fig.8 (b) shows 
the phase angle difference between AESPO and microgrid bus 
voltages. As synchronization occurs at the 70th second, the 
phase angle difference decreases to a value almost equal to 
zero. This clearly shows that the microgrid is synchronized to 
the utility. 
B. Secondary Control (Islanding Detection and AGC) 
Fig. 9 shows the implemented microgrid structure which 
involves conventional and renewable DERs. A microgrid can 
operate in grid-connected and islanded mode. In gridconnected operation mode, DER units operate in grid-feeding 
mode which exports constant active and reactive power. 
Frequency and voltage regulation is handled by host grid. 
However, in islanded operation, a microgrid must be able to 
regulate internal frequency and voltage with a proper control. 
Droop control is the commonly accepted operation for power 
sharing among DERs in a microgrid. In the droop control 
scheme, the frequency can deviate from the nominal value 
based on loading conditions. Selecting one of the DER units to 
enable secondary control to restore the frequency to nominal 
value is a common practice in islanded operation. 
In this case, when overloading subsides and the microgrid 
starts to draw power from the host grid, AESPO sends ancillary service suspension request to utility connected microgrids. Upon receiving request, microgrid gets disconnected 
from the host grid. Since prior to separation, the microgrid 
was importing power from the host grid, during the islanding 
situation, an immediate microgrid frequency dip is detected 
due to the power imbalance. The active power imbalance introduces frequency deviation in islanded microgrid (2), where 
Htot is the total inertia, fn is the nominal frequency, and fs is the 
system frequency. 
 
dt
df
f
H
t
P
t
P
t
P
s
n
tot
load
gen
2
))
(
)
(
(
)
(
=
−
=
Δ
 (2) 
Microgrid operator and DER operator agents are defined in 
Jade platform and islanding detection agents are the FRPFRQ 
function block which inherits from PTOF logical node [16]. A 
consecutive islanding detection algorithm is used to enable 
islanding detection which senses under/over frequency setting 
initially, then the frequency gradient is compared to set value. 
When islanding is detected, the microgrid operator Requests 
DER operators to switch operation to droop control to enable 
accurate power sharing. Droop based primary control deviates 
the frequency from the nominal value according to the system 
loading conditions. 

Fig. 10. Correspondence between microgrid and DER agents 
 
AGC based secondary control is used to restore system frequency to nominal value. A common way to implement AGC 
in power systems is to implement a proportional-integral (PI) 
controller. An Area control error (ACE) in a power system is 
given as (3), where B is the frequency bias factor, ѐPT is the 
deviation of active power balance in area, and ѐW' is the 
control command to be sent to the governor. ȕ1 and ȕ2 are the 
PI control coefficients. 
 
1
2
T
AGC
ACE
P
B f
P
ACE
ACEdt
β
β
= Δ
+
Δ
Δ
= −
−
³
 
(3) 

Fig. 11. (a) Frequency change (b) Phase angle difference 
/ƐůĂŶĚŝŶŐ/ŶƐƚĂŶƚ 
^ĞĐŽŶĚĂƌǇ
ŽŶƚƌŽůŶĂďůĞĚ 
ƌŽŽƉZĞƐƉŽŶƐĞ 
5
2015 IEEE International Conference on Smart Grid Communications (Smart Grid Comm): Architectures, Control and Operation for
Smart Grids and Microgrids
408

---


### Page 7

Microgrid operator agent requests DER operator agents to 
serve as frequency regulator unit to restore the system frequency to nominal level. Fig. 10 shows the correspondence 
microgrid operator agent and DER operator agents. In this 
case, inverter-based DER Agrees to enable AGC to restore the 
system frequency. Fig. 11 (a)-(b) shows frequency and phase 
angle difference of AESPO and microgrid during the secondary control process. From 100th to 130th second, the microgrid 
is operating in grid connected mode. When islanding detected 
at 130th second, the droop controller of the DERs are enabled. 
This results settling of the operation frequency to 58.5 Hz for 
the remainder of the operation in this loading level. At 170th 
secondary control is enabled by inverter-based DER to restore 
system frequency to nominal value of 60 Hz. The phase angle 
difference clearly shows the AESPO and microgrid are operating separately. 
V. CONCLUSION 
This study presents an industrial adaptation of agent technology to microgrids considering data interoperability. This 
work proposed an agent framework based on IEC 61850 and 
FIPA standards. The proposed framework is validated by realtime experiments with secondary and tertiary microgrid operations in a state-of-the-art smart grid laboratory setup. 
REFERENCES 
[1] Cintuglu, Mehmet Hazar, and Osama Mohammed. "Simulation of digitalized power system using PMU and intelligent control." Industry Applications Society Annual Meeting, 2013 IEEE. IEEE, 2013. 
[2] Fenghui Ren; Minjie Zhang; Soetanto, D.; Xiao Dong Su, "Conceptual 
Design of A Multi-Agent System for Interconnected Power Systems 
Restoration," Power Systems, IEEE Transactions on , vol.27, no.2, 
pp.732,740, May 2012 
[3] Zhabelova, G.; Vyatkin, V., "Multiagent Smart Grid Automation Architecture 
Based 
on 
IEC 
61850/61499 
Intelligent 
Logical 
Nodes," Industrial Electronics, IEEE Transactions on , vol.59, no.5, 
pp.2351,2362, May 2012 
[4] Hui Wan; Li, K.K.; Wong, K.P., "An Adaptive Multiagent Approach to 
Protection Relay Coordination With Distributed Generators in Industrial 
Power Distribution System," Industry Applications, IEEE Transactions 
on , vol.46, no.5, pp.2118,2124, Sept.-Oct. 2010 
[5] Apostolov, Alexander. "Multi-agent systems and IEC 61850." Power 
Engineering Society General Meeting, 2006. IEEE. IEEE, 2006. 
[6] Dimeas, A.L.; Hatziargyriou, N.D., "Operation of a Multiagent System 
for Microgrid Control," Power Systems, IEEE Transactions on , vol.20, 
no.3, pp.1447,1455, Aug. 2005 
[7] Chun-Xia Dou; Bin Liu, "Multi-Agent Based Hierarchical Hybrid Control for Smart Microgrid," Smart Grid, IEEE Transactions on , vol.4, 
no.2, pp.771,778, June 2013 
[8] Kumar Nunna, H.S.V.S.; Doolla, S., "Multiagent-Based Distributed-Energy-Resource Management for Intelligent Microgrids," Industrial Electronics, IEEE Transactions on , vol.60, no.4, pp.1678,1687, April 2013 
[9] Meiqin Mao; Peng Jin; Hatziargyriou, N.D.; Liuchen Chang, "Multiagent-Based 
Hybrid 
Energy 
Management 
System 
for 
Microgrids," Sustainable Energy, IEEE Transactions on , vol.5, no.3, 
pp.938,946, July 2014 
[10] Foo.Eddy, Y.S.; Gooi, H.B.; Chen, S.X., "Multi-Agent System for Distributed Management of Microgrids," Power Systems, IEEE Transactions on , vol.30, no.1, pp.24,34, Jan. 2015 
[11] Logenthiran, T.; Srinivasan, D.; Khambadkone, A.M.; Htay Nwe Aung, 
"Multiagent System for Real-Time Operation of a Microgrid in RealTime Digital Simulator," Smart Grid, IEEE Transactions on , vol.3, 
no.2, pp.925,933, June 2012 
[12] Cintuglu, M.H.; Martin, H.; Mohammed, O.A., "Real-Time Implementation of Multiagent-Based Game Theory Reverse Auction Model for Microgrid Market Operation," Smart Grid, IEEE Transactions on , vol.PP, 
no.99, pp.1,1 
[13] Mazloomzadeh, Ali, Mehmet H. Cintuglu, and Osama A. Mohammed. 
"Development and evaluation of a laboratory based phasor measurement 
devices." Innovative Smart Grid Technologies Conference (ISGT), 2015 
IEEE Power & Energy Society. IEEE, 2015. 
[14] Cintuglu, Mehmet H., Ahmed T. Elsayed, and Osama A. Mohammed. 
"Microgrid automation assisted by synchrophasors." Innovative Smart 
Grid Technologies Conference (ISGT), 2015 IEEE Power & Energy Society. IEEE, 2015. 
[15] Communication Networks and Systems for Power Utility Automation 
for Distributed Energy Resources (DER) — Part 7–420, IEC61850, Int. 
Electrotech. Committee, 2011. 
[16] Cintuglu, Mehmet H., Tarek A. Youssef, Ahmed T. Elsayed, and Osama 
A. Mohammed. "Frequency and voltage control of microgrids upon unintentional cascading islanding." In Southeast Con 2015, pp. 1-6. IEEE, 
2015. 
[17] Odell, James, and Marian Nodine. "The foundation for intelligent physical agents." Retrievable at: http://www. fipa.org (2006). 
[18] Bellifemine, Fabio, Agostino Poggi, and Giovanni Rimassa. "JADE–A 
FIPA-compliant agent framework." Proceedings of PAAM. Vol. 99. No. 
97-108. 1999. 
[19] Bera, S.; Misra, S.; Rodrigues, J.J.P.C., "Cloud Computing Applications 
for Smart Grid: A Survey," Parallel and Distributed Systems, IEEE 
Transactions on , vol.PP, no.99, pp.1,1 
[20] Genge, B.; Beres, A.; Haller, P., "A survey on cloud-based software 
platforms to implement secure smart grids," Power Engineering Conference (UPEC), 2014 49th International Universities , vol., no., pp.1,6, 25 Sept. 2014 
[21] Rajeev, T.; Ashok, S., "A cloud computing approach for power management of microgrids," Innovative Smart Grid Technologies - India 
(ISGT India), 2011 IEEE PES , vol., no., pp.49,52, 1-3 Dec. 2011 
[22] L. Ji,W. Lifang, and Y. Li, “Cloud Service based intelligent power 
monitoring and early-warning system,” in Proc. of IEEE Conf. on ISGT 
Asia, 2012, pp. 1–4. 
[23] Simmhan, Y.; Aman, S.; Kumbhare, A.; Rongyang Liu; Stevens, S.; 
Qunzhi Zhou; Prasanna, V., "Cloud-Based Software Platform for Big 
Data Analytics in Smart Grids," Computing in Science & Engineering , 
vol.15, no.4, pp.38,47, July-Aug. 2013 
[24] Olivares, D.E.; Mehrizi-Sani, A.; Etemadi, A.H.; Canizares, C.A.; Iravani, R.; Kazerani, M.; Hajimiragha, A.H.; Gomis-Bellmunt, O.; Saeedifard, M.; Palma-Behnke, R.; Jimenez-Estevez, G.A.; Hatziargyriou, 
N.D., "Trends in Microgrid Control," Smart Grid, IEEE Transactions 
on , vol.5, no.4, pp.1905,1919, July 2014 
[25] IEEE Guide for Monitoring, Information Exchange, and Control of Distributed Resources Interconnected with Electric Power Systems," IEEE 
Std 1547.3-2007 , vol., no., pp.1,160, Nov. 16 2007 
[26] Bellifemine, Fabio, Agostino Poggi, and Giovanni Rimassa. "Developing multi-agent systems with a FIPA-compliant agent framework." Software-Practice and Experience 31.2 (2001): 103-128. 
[27] Bellifemine, Fabio Luigi, Giovanni Caire, and Dominic Greenwood. Developing multi-agent systems with JADE. Vol. 7. John Wiley & 
Sons, 2007. 
[28] Mahnke, Wolfgang, Stefan-Helmut Leitner, and Matthias Damm. OPC 
unified architecture. Springer, 2009. 
[29] V. Salehi, A. Mohamed, A. Mazloomzadeh, and O. A. Mohammed, 
"Laboratory-Based Smart Power System, Part I: Design and System Development," IEEE Transactions on Smart Grid, vol.3, no.3, pp.13941404, Sept. 2012 
[30] V. Salehi, A. Mohamed, A. Mazloomzadeh, and O.A. Mohammed, 
"Laboratory-Based Smart Power System, Part II: Control, Monitoring, 
and Protection," IEEE Transactions on Smart Grid, vol.3, no.3, pp.14051417, Sept. 2012 
[31] Mazloomzadeh, Ali, Mehmet Hazar Cintuglu, and Osama Mohammed. 
"Islanding detection using synchronized measurement in smart microgrids."Innovative Smart Grid Technologies Latin America (ISGT LA), 
2013 IEEE PES Conference On. IEEE, 2013. 
[32] Cintuglu, Mehmet Hazar, and Osama Mohammed. "Islanding detection 
in microgrids." Power and Energy Society General Meeting (PES), 2013 
IEEE. IEEE, 2013. 
 
6
2015 IEEE International Conference on Smart Grid Communications (Smart Grid Comm): Architectures, Control and Operation for
Smart Grids and Microgrids
409
View publication stats

---
