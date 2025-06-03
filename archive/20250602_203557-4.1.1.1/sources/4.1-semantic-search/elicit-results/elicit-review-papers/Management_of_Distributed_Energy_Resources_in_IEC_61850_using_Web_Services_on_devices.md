

---

Page 1

---

Managing IEC 61850 Message Exchange for
SDN-Controlled Cognitive Communication Resource
Allocation in the Smart Grid
Yanny Moscovits1∗, Eliseu Torres1†, and Joberto S. B. Martins1‡
Salvador University, Salvador, Brazil
yannymoscovits@gmail.com, eliseutorres.gx@gmail.com, joberto.martins@gmail.com
Abstract
The IEC 61850 standard is being largely used in the Smart Grid (SG) context mainly
due to its ability to address communication, interoperability and migration issues. IEC
61850 currently aims at internal substation communication. Nevertheless, there is a de-
mand to generalize its use for distributed SG systems like Home Energy Management
Systems (HEMS) and Advanced Monitoring Infrastructure (AMI) Communication which
potentially involves distributed substations or distributed SG components. IEC 61850-
based systems require constrained timing requirements for communication and the common
approach is to allocate static link bandwidth resources leading in some cases to over di-
mensioning. This paper presents the Substation Cognitive Communication Resource Man-
agement (IC2RM), that aims the management of bandwidth allocation for IEC messages
using a cognitive approach for its provisioning and the SDN/OpenFlow for its deployment.
By dynamically deploying bandwidth for IEC messages, IC2RM optimizes links between
SG substations and systems and potentially reduces the operational costs (OPEX).
Keywords: IEC 61850, Smart Grid, Substation Communication, IEC Communication Man-
agement, SDN/ OpenFlow, Cognitive Resource Allocation, IEC Messages, GOOSE, SV.
1
Introduction
The IEC 61850 standard is being largely used in the Smart Grid (SG) context. It addresses
and standardizes important aspects of the grid operation and management such as the com-
munication messages required, topologies and services. The IEC 61850 also proposes complete
models, describing everything from physical devices to data and attributes [1] [2].
In the Smart Grid a robust and largely distributed network communication capability is
essential to guarantee the grid operation and management [3]. The grid structure and operation
can be segmented in various ways. This fundamentally depends on the problem perspective
being focused. The most basic and generic structured segmentation consists of 3 general grid
components that must communicate: i) generation; ii) transmission; and iii) distribution [2].
In regards to network communication supporting the main SG components, there are grid
elements that have a functionality and communicate as part of their operation and management
processes. Considering this perspective, the main functional elements communicating within
the SG are: i) the Home Energy Management Systems (HEMS); ii) the Substation Automation
Systems (SAS); iii) the Grid Energy Management System (GEMS); and iv) the Advanced
Monitoring Infrastructure (AMI) Communication [4].
∗Moscovits, Y. is with UNIFACS IPQoS research group
†Torres, E. is with FIBRE UNIFACS IPQoS research group
‡Prof. Dr. Martins, J. is with UNIFACS IPQoS and NUPERC research groups
arXiv:2001.08160v1  [cs.NI]  1 Jan 2020


---

Page 2

---

8th International Workshop on ADVANCEs in ICT, January 2020
Moscovits and Martins
The Home Energy Management Systems (HEMS) is part of the Smart Grid on the consump-
tion side where home appliances (e.g., air conditioner, dishwasher, dryer, refrigerator, kitchen
stove, and washing machine) data are collected using smart meters. This data will be used to
optimize power source and distribution. HEMS allows the end user to track consumption and
optimize it, reducing energy costs [5].
The Substation Automation Systems (SAS) enables control through physical elements with-
out the need for human interference, increasing reliability and reducing the duration of distur-
bances or failures. For this, communication protocols between the IEDs (Intelligent Electronic
Device) are used.
There are approximately 150 diﬀerent communication protocols for data
transmission and 20 diﬀerent communication protocols in speciﬁc equipment used in utility
companies. This makes it diﬃcult to interconnect equipment from diﬀerent manufacturers and
gateways introduce delays in messaging can lead to improper operation. In this speciﬁc SG
functional component, IEC 61850 plays a fundamental role and is relevant.
The Grid Energy Management System aims the overall management of the entities involved
in the SG such as distributed energy sources, microgrids, energy storage, smart buildings, smart
homes and electric vehicles, among others.
The Advanced Monitoring Infrastructure (AMI) is a bi-directional communication network
integrated with sensors, intelligent meters and monitoring systems that enable the collection
and distribution of information between meters and utilities [6].
Although the IEC 61850 was initially developed aiming to support internal substation com-
munications addressing its problems and issues (SAS), the standard is being applied and ex-
tended for other SG communication scenarios like HEMS, GEMS and AIM [7] [8].
The main advantages of using IEC 61850 in substations are its lower installation cost and
its capability to support new features and advanced services such as the ones required in the
Smart Grid. IEC 61850 deﬁnes external visible aspects of the devices beyond data encoding
on the wire and consequently enables interoperability, eases programming and lower equipment
migration cost [2].
A problem concerning the adoption of IEC 61850 for communication either inside a sub-
station or between substations is the need to have dedicated high speed capacity to support
the timing requirement of priority messages. Inside a substation, dedicated switch ports are
often allocated for IEC 61850 exchange of priority messages. For exchange of priority messages
between substations, a dedicated overdimensioned link capacity is often used and this results
in a relevant operational cost for the majority of the deployments. That being said, this paper
proposes the cognitive allocation of communication resources, like link bandwidth and port
capacity, in such a way that they can be optimized and shared among IEC 61850 messages.
This paper presents the Substation Cognitive Communication Resource Management
(IC2RM). IC2RM objective is to allow the cognitive control of communication resources al-
located for groups of IEC 61850 messages inside substation’s network or between substations
and functional elements of the Smart Grid. IC2RM addresses the issue of optimizing network
resources deployed for communication among Smart Grid functional elements.
In the next part of this article, Section 2 discusses IEC 61850 message types, their scope
and related requirements.
Section 3 indicates the relevant work being done related to SG
components communication with IEC 61850. Section 5 describes the IC2RM architecture and
61850 data modeling approach used to control and manage the IEC messages. Section 6 presents
the implementation and section 7 presents the ﬁnal considerations.
2


---

Page 3

---

8th International Workshop on ADVANCEs in ICT, January 2020
Moscovits and Martins
2
IEC Messages Types, Scope and Requirements
The Substation Cognitive Communication Resource Management (IC2RM) objective is to allow
the cognitive control of communication resources allocated for groups of IEC 61850 messages
and, in this perspective, its necessary to identify the messages types and scope alongside with
their format and requirements.
There are 4 basic IEC 61850 messages types: i) Sampled Values (SV) messages; ii) PTP/S-
NTP (Precision Time Protocol/ Synchronous Network Time Protocol) messages; iii) GOOSE
(Generic Object Oriented Substation Event) messages; and iv) MMS (Manufacturing Message
Speciﬁcation) messages.
SV, PTP/SNTP and GOOSE IEC 61850 messages are transported over the SG network
using either UDP/IP (User Datagram Protocol/ Internet Protocol) or straight in the Ethernet
frame payload. SV messages are intended to support eﬃcient monitoring and control of substa-
tion and SG equipment. PTP/SNTP messages are intended to support time synchronization
among IEDs (Intelligent Electronic Device) or IEC-based equipment. GOOSE messages are
mainly intended to support hard real-time control applications. The Manufacturing Message
Speciﬁcation (MMS) is a client-server based communication protocol. The client is a network
application or device that requests data and actions from a server. The server contains a Virtual
Manufacturing Device (VMD) in which it allocates objects and contents [9].
The Smart Grid (SG) requires communication resources between components at various
levels and uses various network and communication technologies [2]. A relevant question con-
cerning IEC 61850 in the SG is: What is the IEC 61850 main utilization scope and what are
its deployment communication issues?
The scope of the IEC 61850 in the Smart Grid has been primarily deﬁned on support-
ing message exchanges internally and between substations. In transmission and distribution
substations, the IEC 61850 supports two group of messages that provide communication with
diﬀerent functionality and timing requirements: i) Horizontal communication; and ii) Vertical
communication (Figure 1) [2]
Figure 1: IEC 61850 Horizontal and Vertical Communication Messages and Timings [2]
Horizontal communication uses typically GOOSE messages and are intended to support
critical protection and control applications with real-time transmission delay requirements.
Vertical communication uses typically MMS messages that are intended to support non-critical
supervision applications. An example of typical timing requirements for the utilization of IEC
61850 message exchanges is illustrated in Table 1 (Figure 1) [10].
It is a fact that the main IEC 61850 communication approach to support the exchange of
3


---

Page 4

---

8th International Workshop on ADVANCEs in ICT, January 2020
Moscovits and Martins
messages in substations is to over dimension network links in such a way that IEC messages
always get all bandwidth they need and pass through with the required delay. The basic IC2RM
motivation is then to propose a new approach for link resource allocation looking for answers
to the following research question: Is it possible to deploy IEC 61850 messages communication
using links with shareable and limited resources?
The relevance of this approach is based on the following aspects: i) an IEC 61850 network
with shareable resources do represent a more economical and eﬃcient use of network technolo-
gies and resources in substations and among substations. In eﬀect, the over dimensioning of
substation’s communication resources does represent an investment (CAPEX). On the other
hand, the over dimensioning of communication resources among substations (typically wide
area telecommunication links) does represent an operational cost (OPEX) and, as such, its
reduction is relevant; and ii) SG uses multiple systems at substation level that require commu-
nication with heterogeneous requirements and the deployment of shareable resources lead to a
potentially more eﬃcient solution.
The next rationale involving IEC 61850 message exchanges in the Smart Grid is: Can ma-
chine learning (ML) be used to support eﬃcient and adequate communication resource alloca-
tion for IEC messages and other application and systems in substations and among substations?
The IC2RM is a cognitive communication approach based on SDN/OpenFlow for IEC
61850’s communication resources allocation in the Smart Grid considering message exchanges
inside substation and between substations and SG systems. IC2RM architecture is illustrated in
Figure 2 and, in summary, it aims to allow the utilization of shareable communication resources
by critical and non-critical IEC messages for functional components of the Smart Grid.
Figure 2: IC2RM Architecture and Operation Scope
3
Related Work
Ustun (2019) in [8], presents recent application of the IEC 61850 to support communication in
various Smart Grid application scenarios like substation communication, microgrid communi-
cation and home network communication, among others. Ustun (2011) in [11] applies extensive
4


---

Page 5

---

8th International Workshop on ADVANCEs in ICT, January 2020
Moscovits and Martins
communication capabilities of the IEC 61850 in microgrid distributed energy resource (DER)
deployments with fault current limiters IEC modeling. Solar Home System (SHS) and Smart
Meter(SM) are modeled in [12] with IEC 61850 communication performance evaluation for
diﬀerent network technologies.
IEC 61850 communication-based coordinated operation of distributed energy resources
(DER) and locally controlled distribution static compensators (DSTATCOM) is presented in
[7] where MMS type IEC 61850 messages are mapped onto the XMPP (eXtensible Message
Presence Protocol) web protocol to provide microgrid communication.
In all the above references, no resource allocation scheme is presented for optimize IEC
message communication and guarantee its time constraints. To the extent of our knowledge,
IEC 61850 message time guarantees deployed using SDN and machine learning support for
managing real time message constraints have not yet been proposed.
4
IC2RM Architecture and Link Management
The IC2RM architecture is illustrated in Figure 2.
IC2RM is composed by 3 modules: i)
The IEC 61850 communication broker; ii) a cognitive engine; and iii) a SDN-based network
monitoring and communication resource deployment module.
The IEC 61850 communication broker manages the constrained and shareable communica-
tion resources either inside or between substations and systems. It decides how much bandwidth
is allocated for each speciﬁc set of messages exchange.
The cognitive module processes all new message exchanges and, dynamically, suggests to
the broker what resource allocation action should be executed upon the set of switches used in
the substation or between substations. The main purpose of the cognitive engine is to provide
feedback to the broker in terms of what is the best resource allocation action to be be executed
based on the learning process involved in the system operation.
The SDN-based network monitoring and communication resources deployment module is
basically an SDN interface between the broker and the set of OpenFlow-based switches. It
monitors new incoming IEC 61850 message traﬃc by the use of OpenFlow Packet-In messages
and sets-up the ﬂow-tables in the switches of the target communication grid system.
The IC2RM’s operation (dataﬂow) is modeled using the following principles: i) all IEC 61850
message exchanges are, at least during the ﬁrst message exchange between control or supervisory
equipment, inspected by the IC2RM; ii) there is a message priority scheme deﬁned by the
manager that basically deﬁnes messages that do have stringent bandwidth reservation allocation
and messages that do not need it; and iii) there is a message communication identiﬁcation model
in a way that messages can be identiﬁed and detected for on-the-ﬂy processing.
5
Message Identiﬁcation Modeling for SDN-based Link
Management supporting IEC 61850-based Systems
IEC 61850-based systems are modeled using typically the following steps: i) An information
model is proposed with the modules that communicate in the IEC 61850-based system; ii) A set
of messages is created supporting the expected service or functionality for the system; and iii)
These messages are mapped onto the basic set of IEC messages. As an example, Kikusato in [8]
deﬁnes an IEC-based information module with a set of messages for an EV (Electric Vehicle)
charging system.
5


---

Page 6

---

8th International Workshop on ADVANCEs in ICT, January 2020
Moscovits and Martins
IC2RM focuses on managing basic IEC 61850 messages and, as such, IC2RM message iden-
tiﬁcation modeling has to do with identifying and allocating link bandwidth for these messages.
This approach guarantees that IC2RM Message would work with any IEC 61850-based system
development.
In terms of the IC2RM implementation, the following priority message modeling is deﬁned: i)
GOOSE and SV messages have an assigned minimum private bandwidth allocated; ii) MMS and
PTP/SNTP share a maximum limited amount of link bandwidth; and iii) MMS and PTP/SNTP
maximum conﬁgured bandwidth can be, dynamically, re-allocated to GOOSE/ SV messages to
guarantee its timing requirements. This priority modeling approach reﬂects the main objective
of the IC2RM which is to provide enough bandwidth to priority messages (GOOSE/ SV) while
keeping some room to allow less priority messages (MMS and PTP/SNTP) over a restrained
link with limited bandwidth resources.
From the operational point of view, IEC 61850 message resource allocation requires the
following actions to be executed by the IC2RM: i) GOOSE and SV messages exchanged by
IEC-based equipment are processed by the broker when communication starts (1st message)
to allocate bandwidth resource; ii) IC2RM implements soft-state control of critical and non-
critical message exchanges among all IEC-based equipment; and iii) Messages are identiﬁed
using SDN/OpenFlow PacketIn message and other OpenFlow protocol resources.
IC2RM message identiﬁcation modeling uses the following OpenFlow ﬂowtable parameters:
• GOOSE messages (Figure 3) [13]: i) Source/ Destination MAC addresses (equipment
identiﬁcation); ii) EtherType (GOOSE message); and iii) APPID (Application ID).
• SV messages: i) Source/ Destination MAC addresses (equipment identiﬁcation); ii) Ether-
Type (SV message); and iii) APPID (Application ID).
Figure 3: IEC 61850 GOOSE Message Structure [13]
6
IC2RM Prototype Implementation
The IC2RM prototype implementation focuses initially on managing inter-substation IEC 61850
message exchanges as illustrated in Figure 4.
In this experimental setup 2 substations are interconnected using a link (100 Mbps) and there
is one ethernet OpenFlow-capable switch connecting IEC-capable and non-capable equipment
per substation. The IC2RM runs on a server (controller) located in one of the substations.
6


---

Page 7

---

8th International Workshop on ADVANCEs in ICT, January 2020
Moscovits and Martins
Figure 4: Inter-Substation Communication Experimental Setup
Its location in either substation 1 or 2 does not aﬀect the overall operation because OpenFlow
PacketIn messages generated when new IEC 61850 message traﬃc is generated are forwarded
to the controller independently of its position and both switches use the same controller.
This IEC 61850 application scenario is relevant to control and supervision applications
that must operate beyond substations limits.
This is, for instance, the case of microgird’s
communication in wide area for functionalities like the ones required by distributed energy
resources (DER) which are highly dynamic in nature. Current IEC 61850 standard does not
fully support this kind of setup and is oriented for internal substation communication.
The IC2RM prototype uses the following software components: i) Ubuntu Server 14.04.4 as
the operating system; iii) Mininet Version 2.2.2 to deploy the inter-substation communication
setup of hosts and switches indicated in Figure 4 iii) Oracle VM VirtualBox Version 4.1.18
r78361 as the virtualization software and iv) Pox controller; and v) OpenVSwich (OVS) as the
SDN/Openﬂow basic components.
In terms of the IC2RM’s architecture module deployment, the IEC 61850 communication
resource broker and the reinforcement learning (RL) cognitive engine are user applications
running as a SDN-OpenFlow controller module in one of the hosts conﬁgured with the Mininet.
Link bandwidth allocation per prioritized (GOOSE and SV) and non-prioritized IEC mes-
sage exchanges is realized by using the Queue Manager 1 [14]. The QueueManager is a module
developed to allow the OpenFlow controller to manage dynamically the bandwidth allocation
directly on OpenVSwitch. With this module, when the controller is setting a new ﬂow, it can
specify the maximum rate of bandwidth in a output port of OVS, and split the bandwidth
between priority queues. Each queue receives then a speciﬁc tag that indicates the bandwidth
rate. This solution solves a typical problem in controllers that can set queues, but the conﬁgu-
rations of bandwidth allocation is intended to be done externally to the controller, preventing
in some case the deployment of a dynamically conﬁgured switch.
7
Final Considerations
IC2RM proposes a new scheme to allow priority and non-priority IEC 61850 messages to be
exchanged in substations and between substations and SG functional components keeping their
time constraint requirements. The IC2RM uses a SDN-based broker that dynamically manages
the bandwidth allocation for all messages ﬂows.
This allows link optimization and, conse-
quently, the utilization of links that do not need anymore to be over dimensioned, leading to
the utilization of IEC 61850 standard in a larger set of distributed applications and systems in
the Smart Grid context.
1https://github.com/EliseuTorres/QueueManager
7


---

Page 8

---

8th International Workshop on ADVANCEs in ICT, January 2020
Moscovits and Martins
IC2RM current prototype implementation runs on a Mininet emulated experimental setup
with a POX SDN controller. The deployed prototype is able to detect new incoming IEC 61850
message ﬂows that require bandwidth allocation using the OpenFlow PacketIn resource. The
broker allocates then the required bandwidth per message type to comply with its standard
timing requirements. In current version of the IC2RM prototype, a straightforward resource
allocation method is used with the continuous and static allocation of bandwidth per message
ﬂow. At this prototype stage, the cognitive allocation approach based on the RL is not yet
implemented since the current objective is to have a proof of concept of the prototype basic
operation.
The next steps in the prototype implementation will include the use of reinforcement learning
to learn about message traﬃc patterns that allow the dynamic management of under dimen-
sioned links either inside or between substations.
References
[1] N. Honeth, Wu Yiming, , and L. Nordstr¨om. Application of the IEC 61850-7-420 Data Model on
a Hybrid Renewable Energy System. In IEEE Trondh PowerTech, pages 1–6, June 2011.
[2] Yona Lopes, Fraz˜ao Franco Ricardo Henrique, Acosta Molano David, Apostolo dos Santos Mar-
gareth, Galv˜ao Calhau Fl´avio, Malcher Bastos Carlos Alberto, S. B. Martins Joberto, and Cas-
tro Fernandes Nat´alia. Smart Grid e IEC 61850: Novos Desaﬁos em Redes e Telecomunica¸c˜oes
para o Sistema El´etrico. In XXX Simp´osio Brasileiro de Telecomunica¸c˜oes - SBrT’12, pages 1–44.
SBRT - Sociedade Brasileira de Telecomunica¸c˜oes, Brasilia, Brazil, September 2012.
[3] Romildo Bezerra, F. Calhau, F. Nascimento, and Joberto Martins. A Framework to Support Smart
Grid Solutions with Ubiquitous, Autonomic and Real-Time Features Targeting the Sustainable Use
of Renewable Power. Journal of Selected Areas in Renewable Energy, 3(10):1–6, October 2013.
[4] N. Dorsch, H. Georg, and C. Wietfeld. Analysing the Real-Time-Capability of Wide Area Com-
munication in Smart Grids. In 2014 INFOCOM WKSHPS, pages 682–687, April 2014.
[5] Dusit Niyato, Lu Xiao, and Ping Wang. Machine-to-machine communications for home energy
management system in smart grid. IEEE Communications Magazine, 49(4):53–59, April 2011.
[6] F. Bouhafs, M. Mackay, and M. Merabti. Links to the Future: Communication Requirements and
Challenges in the Smart Grid. IEEE Power and Energy Magazine, 10(1):24–32, January 2012.
[7] S. Hussain and I. Ali.
IEC 61850 Modeling of DSTATCOM and XMPP Communication for
Reactive Power Management in Microgrids. IEEE Syst Jour, 12(4):3215–3225, December 2018.
[8] T. Ustun, S. Hussain, and H. Kikusato. IEC 61850-Based Communication Modeling of EV Charge-
Discharge Management for Maximum PV Generation. IEEE Access, 7:4219–4231, 2019.
[9] C. Ozansoy, A. Zayegh, and A. Kalam. Time Synchronisation in a IEC 61850 Based Substation
Automation System. In Proc. of the Australasian University Power Engin. Conf, pages 1–7, 2008.
[10] H. Le´on, C. Montez, O. Valle, and F. Vasques. Real-Time Analysis of Time-Critical Messages in
IEC 61850 Electrical Substation Communication Systems. Energies, 12(12):2272, January 2019.
[11] T. Ustun, C. Ozansoy, and A. Zayegh. Extending Iec 61850-7-420 for Distributed Generators with
Fault Current Limiters. In 2011 IEEE PES, pages 1–8, November 2011.
[12] S. Hussain, A. Tak, T. Ustun, and I. Ali. Communication Modeling of Solar Home System and
Smart Meter in Smart Grids. IEEE Access, 6:16985–16996, 2018.
[13] Petr Matousek.
Description of IEC 61850 Communication.
Techical Report FIT-TR-2018-01,
Brno University of Technology, February 2019.
[14] E Torres, R Reale, L. Sampaio, and J. Martins. BAMSDN: Uma Ferramenta para a Explora¸c˜ao
Dinˆamica e Flex´ıvel de Recursos Baseada em Modelo de Aloca¸c˜ao de Banda e SDN/OpenFlow.
In Simp´osio Brasileiro de Redes de Computadores, pages 1–8, May 2018.
8


---

Page 9

---

8th International Workshop on ADVANCEs in ICT, January 2020
Moscovits and Martins
9
