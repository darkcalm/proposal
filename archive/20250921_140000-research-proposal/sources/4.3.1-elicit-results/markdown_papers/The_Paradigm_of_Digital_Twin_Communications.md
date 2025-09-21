

---

Page 1

---

1
The Paradigm of Digital Twin Communications
Tom H. Luan, Ruhan Liu, Longxiang Gao, Rui Li, Haibo Zhou
Abstract—With the fast evolving of cloud computing and
artiﬁcial intelligence (AI), the concept of digital twin (DT) has
recently been proposed and ﬁnds broad applications in industrial
Internet, IoT, smart city, etc. The DT builds a mirror integrated
multi-physics of the physical system in the digital space. By
doing so, the DT can utilize the rich computing power and
AI at the cloud to operate on the mirror physical system, and
accordingly provides feedbacks to help the real-world physical
system in their practical task completion. The existing literature
mainly consider DT as a simulation/emulation approach, whereas
the communication framework for DT has not been clearly
deﬁned and discussed. In this article, we describe the basic DT
communication models and present the open research issues. By
combining wireless communications, artiﬁcial intelligence (AI)
and cloud computing, we show that the DT communication
provides a novel framework for futuristic mobile agent systems.
Index Terms—Digital twin; Mobile agent system; Communi-
cation; Wire less network
I. INTRODUCTION
Over the past decades, the networking technology has
evolved along two lines, as illustrated in Fig. 1.
The ﬁrst line is the development of the wired network
technology from the Internet to cloud computing, big data
analysis and AI. Notably, with the continuous evolution of
Internet and wired access technologies starting from 1990s,
as of April 2021, the population of Internet users reaches
4.72 billion, which is 57 percent of the world population.
The intensive computing demands of Internet users drive the
development of the centralized cloud computing and data cen-
ter networks. As reported, by 2021, 94 percent of workloads
and compute instances are processed by cloud data centers,
making the cloud as the centre of data and computing in the
worldwide. Finally, the global connectivity, giant data resource
and rich computing power, coupled with the advances of
artiﬁcial intelligence (AI), make the cloud a supreme platform
nowadays for the global intelligence.
Another line is the surge development of the wireless
network technologies from the smart electronics to Internet
of Things (IoT), ﬁfth-generation (5G) cellular network and
mobile agent systems. The wide adoption of smart electronics,
e.g., iPhone, represents the ﬁrst step to put the computing
power on the palm of people. As a result, the way that people
live has been revolutionized with various mobile applications
and the IoT technology, such as smart home and smart commu-
nity [1]. With the explosive usage of wireless electronics, 5G
networks have emerged to provide the larger network capacity,
smaller communication latency and higher spectrum efﬁciency
to support the massive ubiquitous mobile devices. The fast and
ubiquitous wireless connectivity, powerful onboard computing
facility and AI have paved the way for mobile agent systems,
e.g., UAVs, autonomous vehicles, which open the potentials
for a high-degree community-wide automation.
It is foreseeable that the broad applications of mobile
agent systems would result in another revolution in our lives
towards the full automation and signiﬁcant enhancement on
the life quality, efﬁciency and convenience. However, the
mobile agents are constantly limited by their battery, onboard
processing power and sensing range. To alleviate the physical
limitations of mobile devices, the line of wireless networking
technologies needs to seek for the rich AI and resources from
the cloud, which drives the two lines converge at the DT
technology. Speciﬁcally, a DT system maintains a mirroring
digital representative (DR) at the virtual space, e.g., the cloud
for a mobile agent (referred to as the physical entity (PE)).
In this framework, the PE works in the real-world environ-
ment for practical task executions. The DR keeps real-time
communications with their PE to learn PE’s status. With such
information, the DR works on the cloud as a collaborating
peer to the PE to exploit the cloud resource to help the PE on
ﬁnishing its tasks.
The concept of DT has been developed for decades. Nowa-
days, DT has found rich applications in industry with the
smart grid system, Industry 4.0, smart city and healthcare.
However, in contrast to most existing works which consider
DT as a simulation platform, a thorough investigation on DT
as a promising communication framework to facilitate the
mobile agent systems is rare in the literature. In this article,
we introduce the basic concepts and characteristics of DT
communication, discuss the possibility of different application
scenarios. For further study, we explore the three ways of DR
deployment and analyze how it differs from other technologies.
II. STRUCTURE OF DT AND ITS COMMUNICATION MODEL
A typical DT concept model contains four parts: a PE in
real space, a DR in virtual space, the connections of current
data and information that ties the PE and DR together, namely
intra-twin communications, and the connections to connect the
DR with the outside world. The functions and characteristics
of each part is described as follow.
a) Physical Entity (PE): In the real space of a DT
system, various of infrastructures such as sensors and cameras
are responsible for collecting data of current physical measure-
ments of PE. Taking the autonomous vehicles as an example,
as in Fig. 1, the PE is a real-world vehicle containing different
sensors, e.g., the cameras which are installed at every angle
and ensures the 360 degree view of the external environment,
and radar and LiDAR on the four sides of the vehicles can be
used to detect the objects around and measure its distance and
speed in real time.
arXiv:2105.07182v1  [cs.NI]  15 May 2021


---

Page 2

---

2
Internet
Cloud 
Computing
Big Data
Artificial 
Intelligence
Smart 
Electronics
Internet 
of Things
5G 
Network
Wireless 
Agent System
Wired Network System
Wireless Network System
Physical world
information
Computation 
results
Physical Space
Virtual Space
Digital Twin System
Physical Entity (PE)
Digital Representative (DR)
Fig. 1: Technology lines of networking
b) Digital Representative (DR): In the virtual space of
a DT system, a DR can be treated as a software application
maintaining a real-time model of its PE. It receives the real-
time data collected by PE via a synchronized private link.
After processing the data, the DR can not only visualize and
represent the instant status of its PE, but also can calculate
anticipatory operations to help its PE to make decisions in
the real-world. For example, as in Fig. 1, according to the
information received from a vehicle, e.g., the trafﬁc environ-
ment, weather conditions, passenger’s preferences, and the
information learned from the cloud such as regional trafﬁc
information, a DR of a vehicle can calculate the best driving
strategy on the velocity, lane to stay and feedback to the
vehicle. The information from the DR help the vehicle to make
the most accurate path planning and optimal driving strategy.
c) Intra-twin Communications: The connection between
PE and DR, i.e., the intra-twin communication, contains two
components: the raw data transmission and the processed in-
formation transmission. Speciﬁcally, the raw data refers to the
data collected by different sensors that ﬂow from PE to the DR,
whereas the processed information refers to the analysis result
that generated and sent from DR to the PE. What is noteworthy
is that the connection link between PE and its DR has to
be private and completely protected to share the information
and knowledge (or AI models) within the twin. The three
components, i.e., PE, DR and intra-twin communication, make
up a complete inner loop of the DT system that can help
implement effective simulation, prediction and feedback loops
within the twin.
d) Communications to Outside World: The connection
of DRs to the outside world include two types.
The ﬁrst type is the communications among DRs, i.e.,
inter-twin communications. Note that with each DR keeping
the synchronized communications with its PE, the commu-
nications among PEs can be relayed through their DRs. For
Autonomous Vehicle 1 
(PE 1)
DR 1
Autonomous Vehicle 2 
(PE 2)
DR 2
Inter-twin 
Communication
Intra-twin 
Communication
Intra-twin 
Communication
Out-of-Field 
Communications 
over DT
Fig. 2: DT system for autonomous vehicles
example, as in Fig. 2, assuming that PE 1 intends to learn
the road information from PE 2 in its driving path. The direct
vehicle-to-vehicle communications between PE 1 and PE 2
may be unavailable due to the out-of-ﬁeld. To achieve this
goal, DR1 can communicate with DR 2 to retrieve PE 2’s
sensed information using the inter-twin communication, and
transmit to PE 1 using its intra-twin communication.
The second type is the communications of DR with the
cloud. By living on the cloud, the DR can retrieve information
from cloud and synchronize with its PE. In the meantime, the
cloud can also communicate with DRs to retrieve their PE’s
information for census.


---

Page 3

---

3
III. CHARACTERISTIC OF DR
As a key component of DT, the DR is a new digital approach
that communicate, compute, simulate and control the whole
life cycle of PEs by using PE’s historical data, real-time data,
cloud data and algorithmic AI models [2]. According to this
concept, the typical characteristics of a DR can be described
as follows:
• Always-on Application: A DR can utilize the computing
and storage resources at the cloud to assist its PE. A PE
can be off-line due to limitations on wireless connectivity.
In this case, a DR can work on behave of its PE in the
cloud.
• Synchronization: In contrast to simply a cloud computing
scheme, a DR keeps the real-time bidirectional infor-
mation synchronization with its PE. On one hand, the
PE updates the real-time local information collected at
the physical end. At the same time, the DR may also
collect useful information from other DRs or the cloud,
and synchronize with the PE to help PE on its task
accomplishment.
• Private: The goal of a DR is to assist its PE, and
therefore, DR works as a collaborating peer to its PE.
Therefore, as a synchronized pair, a DR is private to the
PE and cannot release any sensitive information of its PE.
• Autonomous: With sufﬁcient data and computing power,
a DR can work autonomously. For example, in the inter-
twin communications in Fig. 2, DR 1 can communicate
with DR 2 without notifying PE 1, and only synchro-
nize the retrieved information to PE 1. The autonomous
behavior of DRs should acquire the permissions of their
PEs.
IV. STATE-OF-THE-ART
With the development of networking and AI technologies,
the state-of-the-art research frames DT as a modern imperative
for digital transformation initiatives. Three typical application
scenarios of DT system in literature is introduced as follows.
A. Model of Communications
As a new paradigm that mainly used in the cyber-physical
environment, how to ensure high quality communication ca-
pability is the basic topic of a DT system. As illustrated in
Fig. 3, the DT systems focusing on the digital operations in
the virtual space and the existing network technologies in the
real-world, such as 5G and ﬁber grid, can be complementary to
each other. Speciﬁcally, the impact between the two is mutual,
by establishing DR of target network, the performance of the
network in terms of security, data communication rate, and
bandwidth can be greatly improved. Meanwhile, with the aid
of high-performance network, DR can meet the requirements
for synchronization and privacy in simulation and computing
scenarios.
At present, there are several studies exploring how the
characteristics of DT can be used to improve the commu-
nication quality of network. In order to solve the mismatch
between the conventional network management scheme and
the real physical situation, Wang et al. [3] propose a DT based
optical communication system to narrow the gap between the
physical layer and network layer, so as to achieve a high-
reliable and high-efﬁciency optical communication system.
To accommodate the development of smart vehicles, a DT
based social-aware vehicular edge network is introduced by
[4] to conduct massive content delivery. By constructing a
social model in DR, a cache cloud is generated to merge
corresponding stored content from multiple vehicles, which
shows great advantages in optimizing caching performance. In
industrial IoT environment, Jia et al. [5] propose an intelligent
clock synchronization method. With the predictable clock
behaviors, the synchronization-related timestamp exchange
is signiﬁcantly reduced, and a high quality data exchange
network with high clock accuracy and low communication
resource consumption can be derived.
B. Simulation and Prediction
With high-quality communication as the basis to transmit
data and knowledge, the DT system can be used to perform
simulation tasks in a variety of scenarios, such as anomaly
detection and autonomous vehicles testing. This is particularly
useful for areas that involve a mass of labor or resource
consumption. As shown in Fig. 3, from a holistic perspective, a
simulation can be seen as a bridge in the whole DT ecosystem,
that is, it is directly related to the underlying application
scenario of DT, i.e., communication, to ensure accurate and
real-time data transmission. At the same time, simulation
also maintains massive information exchange with the upper
application scenario, i.e., computing and analysis, in order
to fulﬁll the real-time task requirements in the real-world
environment.
Beneﬁt from the fewer constraints, simulation is the closest
scenario to industrial-grade applications and has received a lot
of attention from enterprises and research institutes. Danilczyk
et al. [6] develop a DT based security framework named
ANGEL to intelligently guard the physical system of the smart
grid. By utilizing real-time sensed data, ANGEL is capable to
assess the system behavior and simulate complex attacks. As a
result, defense and optimization strategies are retrieved for the
physical system to form a self-healing grid. By combining with
edge computing technology, Maheswaran et al. [7] introduce
a distributed DT network deployed at the edge machine where
multiple AI models are hosted to solve different application
problems, which enables the autonomous vehicle assistance
system with low-latency and multiple applications. In the ﬁeld
of medical health, as a future development direction, [8] also
mentions that as a further development of current medical
simulation such as monitoring of macro-physical indicators
and the prevention of dominant diseases, a complete DT based
human body can be realized to simulate medication and to
monitor the body reaction, which is a powerful tool to promote
drug research, epidemic treatment and disease prediction, etc.
C. Computing and Analysis
As a light-weight application scenario, computing and anal-
ysis of DT mainly focus on speciﬁc task implementation.


---

Page 4

---

4
Computing Module
High Fidelity Modeling
Simulation and 
Prediction
Computing and 
Analysis
AI/Algorithm Module
Data Module
Digital 
Reprensetative
Network
Physical 
Entity
Cloud
Vehicle
UAV
Robot
Body Network
Vehicle
UAV
Robot
Body Network
5G/6G
Satellite
WLAN
Wireline
Edge computing
5G/6G
Satellite
WLAN
Wireline
Edge computing
Cloud 
computing
Blockchain
Datacenter 
network
Twin Network
(peer-to-peer)
Cloud 
computing
Blockchain
Datacenter 
network
Twin Network
(peer-to-peer)
Data
Result
Demand
Model
Inter-twin Communication
Intra-twin Communication
High-efficiency Networking
Fig. 3: Application scenarios of DT communication system
It is more ﬂexible and is often used in conjunction with
simulation scenarios by designing corresponding AI models
using techniques such as deep learning and transfer learning
to simulate real-world target tasks. For example, by deploying
a retrained YOLO model, a DT system can be used to
detect speciﬁed targets, such as pedestrian, cars, indicators
and special equipment. Typically, to maintain the privacy of
DT system, computing and analysis applications are required
to only contain a bidirectional intra-twin communication link
to transmit data and information with simulation platform,
while the simulation platform has the permission to determine
whether to exchange data with external devices according to
the task requirements.
With the proliferation of AI technologies, multiple AI based
methods are proposed to improve the performance of DT
system. By utilizing deep learning and computer aided engi-
neering simulation, [9] develops an equipment parts assembly
model hosted in DT system, which effectively improves the
accuracy of equipment welding. In the remote health monitor-
ing area, [10] introduces multiple machine learning models
to predict and evaluate individual stress level according to
washable sensors; in this way, the stress information can be
learned and analyzed without exposing humans to negative
environment. To ﬁll the gap in the integration of DT based
models with the observed cyber-physical system, [11] proposes
a model-driven method that can fully analyze and describe the
whole ecosystem of cyber-physical system and its DT, which
helps eliminate repetitive programs and foster the systematic
engineering of DT.
V. JUSTIFICATION OF CONCEPTS
This section compares DT with existing networking tech-
nologies.
A. Comparison to Cloud Computing and Edge Computing
The cloud computing is an integrated and open platform to
host the data and computing in the worldwide. Built upon a
cluster of powerful computing servers using the virtualization
technology, the cloud computing provides a global container
over the world for users to deploy their applications and
services.
The edge computing is an extension of cloud computing
which deploys lightweight cloud-like devices at the user’s
premises so as to avoid the remote long-thin connections
from mobile users to the cloud, and provide the fast-rate
real-time responses to local service requests. Similar to cloud
computing, the edge computing provides an open container
facility but to local wireless devices only, where the wireless
devices can ofﬂoad their applications and computing tasks.
In contrast to a hardware computing facility featured by
the caching and computing resource, the DT is a computing
framework where the virtual part, i.e., DR, is a software
application installed and operated on the cloud or edge serve.
Different from the cloud and edge computing which are
open to different users, the DR corresponds one-to-one to its
physical part. As such, the DR should have private data and
protected storage and computing space in the virtual space. To
obtain a clearer understanding, we summarize the comparisons
in Table I.


---

Page 5

---

5
TABLE I: Comparison of cloud, edge and DR
Cloud
Edge
DR
Hardware / Software
hardware
hardware
software
Amount of Users
n
n
1
Personalization
low
median
high
Privacy
median
median
high
Deployment
global
local
global/local/PE
Data Carrying Capacity
high
median
low
The DT system provides a secured framework for com-
munications. In a complete DT communication system, each
PE has its own exclusive DR, and the data communication
between them follows the private principle, which can be used
to ensure sufﬁcient security and privacy. Speciﬁcally, in intra-
twin communication, DR and PE ﬁrst establishes a private link
in the process of data transmission and sharing, and all data
only can be transmitted through this speciﬁc link. During the
inter-twin communication, all data ﬁrst request for the PE’s
permission. In this process, all private information in PE will
be retained, and only data marked as approved information can
be exchanged between DRs via inter-twin communications.
B. Comparison to Mobile Cloud Computing
The mobile cloud computing is the most similar framework
to DT. Mobile cloud computing also maintains a private
application on the cloud dedicated to mobile users, e.g., Apple
iCloud. The design goal of mobile cloud computing is to
alleviate the computing and storage burden of mobile devices
with the always-on cloud resources.
The existing literature on mobile cloud computing mainly
considers the applications of data ofﬂoading by uploading and
storing data from mobile users to cloud to reduce the local
load and cost [12]. DT system can be seen as an evolu-
tionary version of mobile cloud. In addition to transmitting
and storing data, the DT system maintains an autonomous
software application on cloud in which DR can perform full
AI applications, such as data cleaning, data fusion, as well as
data processing and analysis, so as to analyze and predict the
real scenarios faced by PE, and assist PE towards the optimal
decision making. In addition, compared with mobile cloud
computing, which works in a reactive manner, the DR can
work in a proactive manner in communications. For example,
depending on the needs of different tasks and deployment
environments, DR can predict the communication bandwidth
of the intra-twin communications and actively schedule the
data synchronizations towards the optimal communication
performance.
C. Comparison to Artiﬁcial Intelligence
Artiﬁcial intelligence refers to the technology that simulates
human intelligence through computer programs. By leveraging
the mathematical optimization and logical reasoning, AI can
learn external data and adaptively generate solutions to achieve
speciﬁc goals, such as planning, perceiving and manipulating
machinery. Different algorithmic models can be integrated to
suit the needs of tasks in complex scenarios. In a nutshell, AI
is a task-driven technique. It treats models as the basic unit
for achieving functions and only solves one problem at a time.
DT is an integrated multiphysics that looks at the big picture
and provides a holistic solution for large-scale tasks. A DR can
contain multiple AI models. According to the answers of sub-
problems given by different models, the DR can eventually
provide a comprehensive output to optimize the solution [13].
For example, in the process of moving goods by a large
robotic arm, an RNN based speech recognition model can
recognize the voice commands issued by the user, and then,
through semantic analysis, the target product, action command,
and movement destination information can be recognized and
transmitted as input to the corresponding target detection
model, action planning model, and path planning model.
Finally, through the analysis and calculation in DR, a strategy
plan with the least time and material cost consumption can be
transmitted to the PE to achieve the target task.
VI. DEPLOYMENT OF DR
As a light-weight software solution, DT communication
system is actually quite ﬂexible; it can be deployed in multiple
environment and through different networks, as shown in
Fig. 4. The descriptions and examples are detailed as follows.
A. Deployment on the Cloud
As the primary way of the DT system deployment, in most
cases, DRs are deployed in a cloud-based environment. This is
suitable for the physical entities that need to constantly move
or that need to be called by multiple devices. For example,
in the application of healthcare, most of the medical monitor
devices is required to be moved to different area based on the
demand. In addition, the wearable devices also should move
at will with the wearer. In this case, to ensure the stability of
data transmission and reduce jitter, DR can be deployed in the
cloud to cope with the movement of devices on the PE side
and to ensure the interaction of data between various different
monitoring devices [14].
B. Deployment on the Edge
Other than deploying the DR system on the cloud, the DT
system can also be built on edge environment, which is more
suitable for large equipment that does not require frequent
location changes. Take remote surgery robot as example, as a
large equipment with high requirements for device precision
and sterile environment, the surgical robot is usually ﬁxed in
a speciﬁc location in the operating room and does not need to
be moved frequently. More importantly, during the procedure,
the robot and the surgeon uses a private link for data and
command communication so as to ensure that the commands
from surgeon and the feedback from robot movements are
real-time and uninterrupted. By deploying the DT system at
the edge, not only can we take advantage of the localized
edge environment to improve the data processing and analysis
performance of AI models, but also combine the advantages
of fast-rate low-cost edge connections to ensure the privacy
and synchronization of data transmission [15].


---

Page 6

---

6
(a) DR Deployed on the Cloud
Intra-twin 
Communications
Edge Server
Edge Server
Cloud
Intra-twin 
Communications
PE
PE
DR
DR
DR
(in a Trust Zone)
PE
(Execution unit)
Physical Entity
Inter-twin 
Communications
Intra-twin 
Communications
(b) DR Deployed on the Edge
(c) DR Deployed on the Physical Entity
Fig. 4: Deployment of DR
C. Deployment on the Physical Entity
Other than the deployment approach introduced above, the
DT system also can be deployed directly on the reserved trust
area at the physical entity. Speciﬁcally, in the real-world appli-
cations, especially industrial systems, the hardware of physical
entity needs to be protected from malicious communications.
In this case, a DR can be deployed at the trust zone of the phys-
ical entity. Any outside communications need to go through
the DR using the inter-twin communications, and the veriﬁed
and secured data are forwarded from DR to the execution
unit of PE through the private intra-twin communications. In
this scenario, a DR may perform the functions such as data
cleaning, security veriﬁcation, honeypot, etc.
VII. OPEN RESEARCH ISSUES
Although the concept of DT communication system is
increasingly pervasive in recent years, it is still in its infancy.
From the perspective of intra-twin and inter-twin communica-
tions, some open issues are discussed as follows.
A. Intra-twin Communications
Communication Efﬁciency: The intra-twin communications
are featured by the private, synchronized and wireless nature.
As the PE would be moving constantly and dynamically con-
nect to the network with unreliable and heterogenous wireless
access technologies, to guarantee the reliable and timely data
synchronization within the DT is challenging. Note that the
intra-twin communications are long-lasting connections, it is
possible for DR to learn and predict the access bandwidth of
PE and adapt the data synchronization accordingly.
Security: For the challenges of security requirements, the
intra-twin communication mainly focuses on the privacy pro-
tection and attack defense due to the private data involved.
These challenges can be solved through multiple technologies
such as blockchain, cryptography and AI. By collecting and
training attack data and abnormal behaviors, the system can be
trained to identify and even predict attack before it happens.
B. Inter-twin Communications
Communication Efﬁciency: The inter-twin communications
are typically through the Internet, or even shared memory
when the DRs are in the same cloud. The communication
bandwidth is therefore not the bottlecheck issue. Instead, how
to enable DRs the locate the useful information source for
data fetching is challenging for inter-twin communications.
The named data networking is a plausible approach for DRs
to locate the needed information.
Security: In contrast to the security challenges of intra-
twin communications, inter-twin communication should be
more concerned with the boundaries and integrity of data
transmission. That is, before transmitting information to an-
other DR, the DT system should ﬁrst justify if the target
data has sufﬁcient permissions to be disclosed. In addition,
to ensure the integrity of the data, when historical data is lost
or incomplete, the blockchain can be used on the DR of a
security-related DT system to provide important input.
VIII. CONCLUSION
As a virtual digital equivalent of a physical system, DT com-
munication system presents many possibilities for innovation,
such as give real-time prediction and provide decision support
for live operations. More importantly, as an integrated AI so-
lution, the application of DT system shows better performance
in mobile agent system.
In this paper, we describe the basic structure and advantages
of the DT system. By comparing it with cloud computing,
mobile cloud computing and edge computing, we explore the
application scope of DT and discuss the deployment approach
in detail. Despite the research of DT is still in its initial stage,
we provide a new perspective for understanding DT and lay the
theoretical foundation for its in-depth use in mobile devices.
REFERENCES
[1] X. Li, R. Lu, X. Liang, X. Shen, J. Chen, and X. Lin, “Smart community:
an internet of things application,” IEEE Communications magazine,
vol. 49, no. 11, pp. 68–75, 2011.
[2] F. Tao, W. Liu, J. Liu, and X. Liu, “Digital twin and its potential
application exploration,” Computer Integrated Manufacturing Systems,
vol. 24, no. 01, pp. 4–21, 2018.


---

Page 7

---

7
[3] D. Wang, Z. Zhang, M. Zhang, M. Fu, J. Li, S. Cai, C. Zhang,
and X. Chen, “The role of digital twin in optical communication:
fault management, hardware conﬁguration, and transmission simulation,”
IEEE Communications Magazine, vol. 59, no. 1, pp. 133–139, 2021.
[4] K. Zhang, J. Cao, S. Maharjan, and Y. Zhang, “Digital twin empow-
ered content caching in social-aware vehicular edge networks,” IEEE
Transactions on Computational Social Systems, pp. 1–13, 2021.
[5] P. Jia, X. Wang, and X. Shen, “Digital-twin-enabled intelligent dis-
tributed clock synchronization in industrial iot systems,” IEEE Internet
of Things Journal, vol. 8, no. 6, pp. 4548–4559, 2021.
[6] W. Danilczyk, Y. Sun, and H. He, “Angel: An intelligent digital twin
framework for microgrid security,” in 2019 North American Power
Symposium (NAPS), 2019.
[7] M. Maheswaran, T. Yang, and S. Memon, “A fog computing frame-
work for autonomous driving assist: Architecture, experiments, and
challenges,” arXiv preprint arXiv:1907.09454, 2019.
[8] X. You, C. X. Wang, J. Huang, and Z. Z. e. a. X. Gao, “Towards 6g
wireless communication networks: vision, enabling technologies, and
new paradigm shifts,” SCIENCE CHINA Information Sciences, vol. 64,
no. 1, 2021.
[9] “Deep learning enhanced digital twin for closed-loop in-process quality
improvement,” CIRP Annals, vol. 69, no. 1, pp. 369 – 372, 2020.
[10] C. Scheuermann, T. Binderberger, N. von Frankenberg, and A. Werner,
“Digital twin: A machine learning approach to predict individual stress
levels in extreme environments.” New York, NY, USA: Association for
Computing Machinery, 2020.
[11] J. C. Kirchhof, J. Michael, B. Rumpe, S. Varga, and A. Wortmann,
“Model-driven digital twin construction: Synthesizing the integration of
cyber-physical systems with their information systems.”
New York,
NY, USA: Association for Computing Machinery, 2020.
[12] M. Shiraz, A. Gani, R. H. Khokhar, and R. Buyya, “A review on
distributed application processing frameworks in smart mobile devices
for mobile cloud computing,” IEEE Communications Surveys Tutorials,
vol. 15, no. 3, pp. 1294–1313, 2013.
[13] Z. Peijie and Y. Chao, “Intelligent logistics management system for
complex precision equipment assembly workshop driven by digital
twins,” 2018.
[14] Z. Lin, L. Ying, Y. Yuan, and R. Lei, “The construction method of cloud
medical simulation platform and a cloud medical system based on digital
twins,” 2018.
[15] A. Rasheed, O. San, and T. Kvamsdal, “Digital twin: Values, challenges
and enablers,” arXiv preprint arXiv:1910.01719, 2019.
