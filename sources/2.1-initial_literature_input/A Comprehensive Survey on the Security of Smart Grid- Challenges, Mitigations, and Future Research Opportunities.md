

---

Page 1

---

1
A Comprehensive Survey on the Security of Smart
Grid: Challenges, Mitigations, and Future
Research Opportunities
Arastoo Zibaeirad
, Farnoosh Koleini
, Shengping Bi
, Tao Hou
, Member, IEEE,
Tao Wang∗
, Member, IEEE
Abstract—In this study, we conduct a comprehensive review
of smart grid security, exploring system architectures, attack
methodologies, defense strategies, and future research opportu-
nities. We provide an in-depth analysis of various attack vectors,
focusing on new attack surfaces introduced by advanced com-
ponents in smart grids. The review particularly includes an ex-
tensive analysis of coordinated attacks that incorporate multiple
attack strategies and exploit vulnerabilities across various smart
grid components to increase their adverse impact, demonstrating
the complexity and potential severity of these threats. Following
this, we examine innovative detection and mitigation strategies,
including game theory, graph theory, blockchain, and machine
learning, discussing their advancements in counteracting evolving
threats and associated research challenges. In particular, our
review covers a thorough examination of widely used machine
learning-based mitigation strategies, analyzing their applications
and research challenges spanning across supervised, unsuper-
vised, semi-supervised, ensemble, and reinforcement learning.
Further, we outline future research directions and explore new
techniques and concerns. We first discuss the research opportu-
nities for existing and emerging strategies, and then explore the
potential role of new techniques, such as large language models
(LLMs), and the emerging threat of adversarial machine learning
in the future of smart grid security.
Index Terms—Smart Grid, Cybersecurity, Smart Grid Archi-
tecture, Adversarial Machine Learning, Large Language Models,
Cyber-Physical Systems.
I. INTRODUCTION
C
ONVENTIONAL power grids have been integral to
electricity distribution for decades, serving as the core
infrastructure for energy transmission from power plants to
end-users [1]. However, the growing electricity demand and
increasing integration of renewable energy resources have
urged a more advanced and enhanced power grid system. As a
result, the smart grid, a sophisticated electrical grid system that
incorporates advanced information and communication tech-
nologies (ICT), has been introduced to enhance the efficiency,
sustainability, and reliability of electricity distribution [2].
The ICT integration in smart grids enables bidirectional
flows of both electricity and information, positioning smart
∗Corresponding Author
Arastoo Zibaeirad and Farnoosh Koleini are with the Department of
Computer Science, University of North Carolina at Charlotte, Charlotte, NC
28223 USA (e-mail: azibaeir@uncc.edu; fkoleini@uncc.edu)
Shengping Bi, Tao Hou, and Tao Wang are with the Department of Com-
puter Science and Engineering, University of North Texas, Denton, TX 76205
USA (e-mail: shengpingbi@my.unt.edu; tao.hou@unt.edu; tao@unt.edu)
grids as the modern backbone of energy infrastructure [8]. By
leveraging ICTs, smart grids facilitate dynamic pricing, effec-
tive load management, and improved grid operations, thereby
mitigating power outages and enhancing system stability [9]
[10]. In addition, intelligent entities such as smart meters
and advanced distribution management systems (ADMS) en-
able demand-side management and substantially reduce the
operational and management costs by employing advanced
fault detection and automation techniques [2], [11], [12].
Smart grids also facilitate the integration of a diverse range
of energy resources. Particularly, the decentralized power
generation via distributed energy resources (DERs), reduces
transmission losses and improves the energy efficiency [13].
The integration of renewable energy systems like solar panels
and wind turbines delivers a more sustainable and eco-friendly
energy production [14], [15]. The adoption of vehicle-to-grid
technology as well as the development of microgrids offers
a reliable energy supply in the event of outages or disasters,
further enhancing the grid resilience [16], [17].
Although smart grids offer numerous advantages, the in-
creased connectivity and complexity of smart grids also ex-
pose them to various security threats. Smart grids have been
identified as potential targets for various attacks, which can
exploit vulnerabilities in the ICT infrastructure to disrupt
power supply, compromise sensitive data, or inflict physical
damage to grid components. For example, the Stuxnet attack,
uncovered in 2010, aimed at compromising the industrial
control systems to damage the Iranian nuclear facilities [18]. In
2015, attackers penetrated the information systems of energy
distribution companies in Ukraine, leading to significant power
outages. The Dragonfly 2.0 campaign, identified in 2017
has demonstrated its capability to compromise the security
of energy sector network in the United States and Europe
[19]. These examples highlight the critical need for adequate
security measures to protect the smart grid infrastructure.
Towards this, multiple strategies have been proposed in
smart girds to improve their security. Specifically, smart grids
incorporate advanced monitoring and detection techniques to
provide real-time alerts and responses to potential attacks [20].
The self-healing mechanisms facilitate quick recovery from
attacks and minimize adverse impacts [21]. Data exchange has
been protected by encrypted and authenticated communication
protocols [11]. Smart grids also foster collaboration among
stakeholders through shared threat intelligence and best secu-
arXiv:2407.07966v1  [cs.CR]  10 Jul 2024


---

Page 2

---

2
TABLE I
COMPARISONS OF OUR SURVEY PAPER WITH THE EXISTING SURVEYS
Key Criteria
Our Survey
[3]
(2023)
[4]
(2023)
[5]
(2022)
[6]
(2021)
[7]
(2020)
Comprehensive Review of Smart Grid Layers
✓
✓
✓
✓
✓
▲
Holistic Integration of Cyber, Cyber-Physical, and Physical Layers
✓
▲
▲
✓
▲
✗
Architecture of Smart Grid
✓
✓
✓
✓
✓
▲
Classification of Attacks
✓
✓
✓
✓
✓
✗
Emerging Detection and Mitigation Solutions
✓
✓
▲
▲
▲
✗
Include Game Theory Approaches
✓
✗
✗
✗
✗
✗
Include Graph Theory Approaches
✓
✗
✗
✗
✗
✓
Include Blockchain Approaches
✓
✓
✗
✗
✗
✗
Include ML Approaches
✓
▲
✓
✓
▲
✗
Role of Adversarial Machine Learning
✓
✗
✗
✗
✗
✗
Role of Large Language Models (LLMs)
✓
✗
✗
✗
✗
✗
Discuss Challenges of Each Detection/Mitigation Technique
✓
✓
▲
▲
▲
✗
Discuss Future Research Directions
✓
✓
✓
✓
▲
▲
✓: Fully addressed; ▲: Partially addressed; ✗: Not addressed at all.
rity practices, enhancing the security of the entire grid infras-
tructure [22]. While conventional security strategies such as
cryptography, authentication, and intrusion detection systems
(IDS) are essential to preserve the security of smart grids,
they might not be sufficient to defend against the continuously
evolving and increasingly sophisticated cyber attacks. The
complicated structure and heterogeneous components of smart
grids impose a significant challenge in combating advanced
cyber attacks, necessitating innovative and efficient solutions.
To defend against evolving attack threats, emerging tech-
niques such as machine learning, blockchain, graph theory,
and game theory have been extensively investigated and have
proven their capability in understanding and mitigating smart
grid security threats. However, these techniques also face
substantial challenges. Adversarial machine learning attacks,
in particular, pose a considerable threat to machine learning-
based strategies, necessitating ongoing research and develop-
ment to enhance the resilience of smart grid systems. Recently,
large language models (LLMs) have also demonstrated great
potential in cybersecurity and attack detection, offering in-
sights into their offensive security capabilities [23].
In this study, we aim to conduct a comprehensive literature
review to examine different network attacks targeting smart
grids and investigate emerging mitigation strategies that show
potential in better preventing and detecting advanced threats.
We carry out a detailed examination of various attack vectors,
detection and mitigation strategies, and emerging threats of
adversarial machine learning attacks and LLMs, providing a
holistic overview of potential security challenges and solutions
within the smart grids.
A. Key Contributions
The main contributions of this paper can be summarized as
follows:
• We provide a systematic study of smart grid architecture,
by defining and categorizing them to three interconnected
layers including the physical, cyber-physical, and cyber
layers. This holistic view offers a multidimensional un-
derstanding of smart grid attacks and defenses.
• We conduct a review of the literature on various attacks in
smart grids, covering cyber, cyber-physical, and coordi-
nated attacks. Our work includes a detailed classification
of these attacks, providing a structured understanding of
the threats in smart grids.
• We critically review and compare emerging detection
and mitigation solutions, including game theory, graph
theory, blockchain, and machine learning techniques,
highlighting their potential effectiveness and possible
shortcomings.
• We explore LLMs and adversarial machine learning,
emphasizing their significance and potential impacts on
the future of smart grid security.
B. Related Works
Multiple surveys have been conducted, each examining
different security perspectives of smart grids.
Ghiasi et al. [3] delve into the analysis of different cyber
attack models, highlighting their characteristics and applica-
bility to understand the vulnerabilities and threats facing these
systems. It also explores cutting-edge security approaches
like blockchain and quantum computing, positioning these
technologies as innovative solutions for enhancing security
and resilience in smart grids. Hasan et al. [4] delve into
the cyber-physical aspects of smart grids. Additionally, it
compiles relevant security standards and protocols, serving
as a useful resource for implementing or updating security
measures. Otuoze et. al. [24] shows a detailed classification
of smart grid security threats into technical and non-technical
sources. Furthermore, the paper differentiates between tech-


---

Page 3

---

3
nical sources, which include infrastructural, operational, and
data management security, and non-technical sources like
environmental factors and regulatory policies. Peng et al. [25]
and Faquir et al. [6] review various attack scenarios including
denial of service, false data injection, and others, providing
insights into how these attacks affect smart grid operations
and suggesting defense strategies to mitigate their impact.
Liu et al. [26] offer detailed recommendations for policy and
operational changes to enhance the security and privacy of
smart grid systems, emphasizing the importance of developing
standards and protocols that address the unique requirements
of these systems. Krishnan et al. [27] identify and discuss the
benefits and challenges of applying blockchain and machine
learning (ML) techniques within smart grid applications. Jokar
et al. [28] cover the application of cryptography in smart
grids, addressing key management challenges and suggesting
cryptographic measures to secure communications and protect
data.
Unlike previous works that focus predominantly on specific
aspects of smart grid security such as cyber attacks or the
integration of certain technologies like blockchain and ML,
our review paper comprehensively explores all three intercon-
nected layers of the smart grid. This approach allows for a
better understanding of how vulnerabilities at one layer can
affect others, providing a more integrated perspective on smart
grid security. By doing so, we address a critical and rapidly
evolving area that poses significant risks to smart grid security.
While previous surveys have discussed various traditional and
modern security techniques, our paper highlights advanced
detection and mitigation strategies that employ cutting-edge
technologies such as game theory, graph theory, blockchain,
and a comprehensive use of ML techniques. This not only
covers a wide range of potential solutions but also discusses
their practical implications and effectiveness in real-world
scenarios. Also, we explore the potential role of LLMs and
adversarial machine learning models in smart grids, a topic that
is relatively unexplored in existing literature. This provides
readers with practical insights into choosing potential security
measures based on specific needs and threat landscapes in the
future. In Table I, we summarized our survey paper’s key
contributions and compared it to five recent survey papers
based on several key criteria.
C. Structure of the Paper
Our survey provides a comprehensive examination of smart
grid security, focusing on its structure, emerging attack vec-
tors, detection and mitigation strategies, and future research
directions. Figure 1 visually summarizes the organization and
structure of our study.
Section II lays the foundation by detailing the structure,
components, and communication protocols of the smart grid.
We partition the system into three interconnected layers: the
physical layer, the cyber-physical layer, and the cyber layer.
The physical layer includes components related to the gener-
ation, transmission, distribution, and consumption of electric
power. The cyber-physical layer integrates the physical layer
with sensing, measurement, and control systems, bridging the
I. Introduction
II. Overview of Smart Grid
A. Structure of Smart Grid
B. Components in Smart Grid
C. Communication Protocols in Smart Grid
III. Emerging Attacks in Smart Grid
A. Cyber Layer Attacks
B. Cyber-Physical Layer Attacks
C. Coordinated (hybrid) Attacks
IV. Detection and Mitigation
A. Game Theory-based Techniques
B. Graph-based Techniques
C. Blockchain
D. Machine Learning
V. Future Research Directions
VI. Conclusion
Fig. 1. Structure of This Study.
gap between physical infrastructure and the digital control
system. The cyber layer forms the communication and data
exchange backbone, encompassing data communication, net-
working, supervisory, and management.
Section III explores emerging attacks in smart grids. We
particularly examine the vulnerabilities associated with new
components of smart grids, i.e., cyber and cyber-physical
layers. We also investigate coordinated attacks that can affect
multiple layers simultaneously, demonstrating the complexity
and potential severity of these threats.
Section IV focuses on detection and mitigation techniques.
As conventional security measures like cryptography, authen-
tication, and network protocols have been intensively inves-
tigated, our study shifts towards exploring innovative detec-
tion and mitigation approaches including game theory, graph
theory, blockchain, and machine learning. These advanced
techniques are crucial for future smart grid security, helping
to identify and mitigate threats more effectively.
Section V outlines future research directions to further
enhance the smart grid security. We present potential research
directions for emerging detection and mitigation techniques,
and explore new methods and concerns, particularly LLM
applications and adversarial machine learning attacks. LLMs
have the potential to understand complex attack patterns and
detect sophisticated zero-day attacks, which are crucial to
improve smart grid security. Adversarial ML attacks pose sig-
nificant threats by misleading existing models and bypassing


---

Page 4

---

4
detectors. Therefore, a thorough examination of LLMs and
adversarial attacks adds a critical dimension to our study.
Section VI concludes the paper by summarizing the key
findings and emphasizing the importance of continued research
and development in smart grid security.
II. OVERVIEW OF SMART GRID
In this section, we provide a brief overview of smart grids
from perspectives of its structures, components, and protocols.
A. Structure of Smart Grid
Smart grids can be built on different architectures given
their specific operational concentrations, including manage-
ment, distribution, communication, security, and scalability.
For example, microgrid and peer-to-peer architectures focus
on electricity generation and distribution, facilitating local en-
ergy production and direct energy trading among participants.
Meanwhile, hierarchical and cloud-based architectures concen-
trate on the scalable and centralized energy management, en-
hancing control and data analytic capabilities across the smart
grid cyber infrastructure. On the other hand, zero trust and end-
to-end communication architectures aim at preserving security
and ensuring secure, efficient data exchange. While each archi-
tectural model focuses on specific aspects, a cohesive, layered
framework is essential for the design and functionality of smart
grids. Santacana et al. [29] propose a four-layer model com-
prising power conversion/transport/storage/consumption layer,
sensor/actuator layer, communication layer, and decision in-
telligence layer. Another study [30] presents a six-layered
framework, namely the physical layer, control layer, data
communication layer, network layer, supervisory layer, and
management layer. Although various layered frameworks have
been proposed, they often cater to specific architectural needs.
In this study, we introduce a more generalized framework
with three primary layers, each with its own specific sub-
layers. Figure 2 shows the three primary layers of the proposed
framework.
1) Physical Layer
We define the physical layer as the foundation of the smart
grid, covering the generation, transmission, distribution, and
consumption of electrical power. The physical layer ensures
that electricity is generated and transported efficiently and
reliably across the grid to meet the demands of diverse
consumers. In our definition, the physical layer includes the
following sub-layers:
• Generation Layer involves the production of electrical
energy from various sources, such as fossil fuels, nuclear
power, and renewable energy sources like solar, wind, and
hydroelectric power.
• Transmission Layer is responsible for the high-voltage
transportation of electrical power from the generation
sources to distribution substations.
• Distribution Layer manages the lower voltage distribution
of electricity from substations to consumers, ensuring that
electricity reaches the end-users safely and reliably.
Generation Layer
Transmission Layer
Distribution Layer
Consumers Layer
Physical Layer
Cyber-Physical Layer
Cyber Layer
SCADA
Control Layer
Measurement and Sensor Layer
PLC
Smart Meter
PMU
Synchro phasor
Network Layer
Management Layer
Application Layer
SIEM
EMS
Demand Response
Fig. 2. Layers in Smart Grid
• Consumption Layer focuses on the end-users of electric-
ity, including households, industries, and commercial es-
tablishments. It encompasses the devices and appliances
that utilize electrical energy.
2) Cyber-Physical Layer
We define the cyber-physical layer as the intermediary
between the physical and cyber layers, connecting the physical
components of the smart grid with their digital counterparts.
This layer is essential for monitoring, control, and optimization
of the smart grid performance. In our definition, the sub-layers
within the cyber-physical layer include:
• Control Layer facilitates real-time control of the smart
grid components. It employs control algorithms in au-
tomation devices and deploys communication protocols
directed through routers, switches, and gateways. This
layer ensures that the grid functions optimally and adapts
to changes in demand, effectively regulating the perfor-
mance of the smart grid.
• Measurement and Sensor Layer is integral to the col-
lection and processing of data from various sensors and
meters installed across the grid. These sensors provide
crucial information on the performance and status of
the grid components, enabling the control layer to make
informed decisions and adjustments.
3) Cyber Layer
We define the cyber layer as the digital backbone of the
smart grid, responsible for the communication, data pro-
cessing, and management of the grid operations. This layer
facilitates the seamless exchange of information and control
signals between various grid components, enabling efficient
and coordinated operations. In our definition, the sub-layers
within the cyber layer include:
• Network Layer forms the essential communication in-
frastructure, ensuring seamless data transmission and
exchange among various components of the smart grid.


---

Page 5

---

5
This layer is integral to data flow management and plays
a key role in maintaining data integrity and security. It
harnesses a variety of modern wireless and wired com-
munication technologies, integrating them to establish a
robust and resilient network that forms the backbone of
the smart grid communication system.
• Management Layer focuses on the supervision and man-
agement of smart grid operations to ensure effective
and efficient functioning. The management layer is in-
tegral for data processing, monitoring, diagnostics, and
decision-making processes to ensure the secure, efficient,
and reliable operation of smart grids.
• Application Layer is concerned with the specific ap-
plications and services built on top of the smart grid
infrastructure. It involves various software applications
and user interfaces that are designed to enhance the
overall efficiency, reliability, and sustainability of the
energy sector.
B. Components in Smart Grid
In smart grids, various components work together to en-
sure efficient functioning and management of modern power
systems. These components can be broadly categorized into
three classes: 1) communication, data management and con-
trol components; 2) energy generation, storage and efficiency
components; 3) security components.
1) Communication, Data Management and Control Com-
ponents
These components form the communication backbone and
control mechanisms of the smart grid.
• Advanced Metering Infrastructure (AMI) is a pivotal com-
ponent of smart grids, enabling two-way communication
between utilities and customers [31]. AMI facilitates the
collection and analysis of energy usage data, supporting
demand response and energy management.
• Distribution Management Systems (DMS) streamline the
management of distribution networks, enhancing effi-
ciency and reliability [32]. DMS integrates various func-
tions such as fault location, isolation, and service restora-
tion, improving overall operational performance.
• Distribution Automation (DA) systems optimize the op-
eration of distribution networks using advanced sensors,
communication technologies, and control devices [33].
DA systems enable real-time monitoring and control of
the distribution network.
• Phasor Measurement Units (PMUs) provide real-time
monitoring of power systems, measuring voltage, current,
and frequency at high resolutions [34]. PMUs enhance
the ability to detect and respond to grid disturbances,
improving system stability and reliability.
• Remote Terminal Units (RTUs) collect data from field
sensors, convert it to digital form, and transmit it to the
central system [35]. They also receive and execute control
commands, enabling remote monitoring and control of
grid components.
• Supervisory Control and Data Acquisition (SCADA) sys-
tems monitor and control critical infrastructure in the
power grid, providing real-time data on system states
[36]. SCADA systems enable operators to make informed
decisions and take timely actions to maintain grid stability
and security.
• Wide Area Monitoring Systems (WAMS) monitor power
systems over large geographical areas, offering real-time
data on stability and performance [37]. WAMS helps in
the early detection of potential grid issues, allowing for
proactive measures to prevent large-scale outages.
2) Energy Generation, Storage, and Efficiency Components
These components are integral to energy production, stor-
age, and management of energy demand.
• Microgrids are small-scale power grids that can operate
independently or in conjunction with the main grid,
improving resilience and energy efficiency [38].
• Distributed Energy Resources (DERs) include renewable
energy sources like solar panels and wind turbines, which
contribute to a sustainable and diverse energy mix [39].
• Energy Storage Systems (ESS) help balance supply and
demand by storing excess energy and releasing it during
peak demand periods [40].
• Demand Response (DR) programs allow utilities to ad-
just energy consumption during peak demand periods to
alleviate grid stress [41].
3) Security Components
These components establish critical defenses to secure the
grid from cyber threats and unauthorized access.
• Intrusion Detection Systems (IDS) actively monitor and
identify suspicious activities, protecting the grid from
potential cyber attacks.
• Firewalls establish a barrier between the trusted internal
network of the smart grid and potential threats from
outside networks.
While the integration of new components such as AMI,
PMU, and SCADA indeed enhances the efficiency and reli-
ability of smart grids, it also brings new security challenges.
This is because these components rely on ICT infrastructure,
making them vulnerable to potential cyber attacks.
C. Communication Protocols in Samrt Grids
In smart grids, communication protocols are essential to
facilitate efficient data exchange and ensure seamless interac-
tion between various components and devices. DNP3, Modbus,
and MQTT are the most prominent communication protocols
adopted in smart grids.
• Distributed Network Protocol 3 (DNP3) is widely used
in SCADA systems [42]. It supports features such as
authentication, encryption, and data integrity to ensure
the confidentiality, integrity, and availability of sensitive
information and control commands.
• Modbus is a common communication protocol in in-
dustrial control systems and smart grid operations, used
for monitoring and controlling devices like intelligent
electronic devices (IEDs), programmable logic controllers
(PLCs) and RTUs [43]. Due to its age and simplicity,


---

Page 6

---

6
Modbus lacks robust security features such as authentica-
tion, encryption, and data integrity mechanisms, leaving
the smart grid vulnerable to cyber attacks.
• Message Queuing Telemetry Transport (MQTT) is a
lightweight, publish-subscribe messaging protocol de-
signed for low-bandwidth and high-latency networks [44].
MQTT offers inherent security features such as transport
layer security (TLS) and secure sockets layer (SSL)
encryption, which provide secure channels for data trans-
mission. However, its lightweight nature may expose it
to potential vulnerabilities such as weak authentication,
insecure default settings, and susceptibility to denial of
service (DoS) attacks.
In the subsequent sections, we will explore various network
attacks targeting different layers of smart grids and examine
emerging mitigation strategies to defend against these threats.
III. EMERGING ATTACKS IN SMART GRID
In this section, we focus on understanding various types
of attacks that undermine the security of smart grids. While
attacks on power grids have been extensively investigated, our
interest is primarily in the attacks associated with the newly
incorporated smart grid components. Specifically, we catego-
rize these attacks into three main groups: cyber layer attacks,
which aim at the cyber infrastructure of smart grids to dis-
rupt operations and compromise data privacy; cyber-physical
layer attacks, which target the control and sensor systems
in smart grids, potentially causing operational failures and
physical consequences; coordinated attacks, which combine
cyber and physical tactics to simultaneously attack various
grid components, undermining the core security principles of
confidentiality, integrity, and availability.
For each category, we will discuss different attacks from
three security perspectives:
• Confidentiality,
which
involves
safeguarding
against
unauthorized access, use, or disclosure of sensitive in-
formation.
• Integrity, which ensures the accuracy, completeness, and
uncorrupted state of data and system components.
• Availability, which pertains to the system capability to
provide timely access to resources and services when
needed.
A. Cyber Layer Attacks
Cyber layer attacks in smart grids can be defined as unau-
thorized or malicious activities targeting various components
within the cyber layer of smart grids (including network,
management, and application sub-layers). These attacks uti-
lize various tactics like malware, phishing, ransomware, and
DoS attacks, each with distinct objectives such as breaching
sensitive data, exploiting financial gain, or disrupting network
functioning. Table II categorizes cyber layer attacks based
on malicious objectives that impact the security aspects of
confidentiality, integrity, or availability.
TABLE II
TAXONOMY OF ATTACKS IN THE CYBER LAYER
Security Impact
Cyber Attack
Reference
Confidentiality
Eavesdropping
[45]–[47]
Man-in-the-middle
[48]–[50]
Unauthorized Access
[51]–[54]
Reconnaissance
[55]–[57]
Message Replay
[45], [58]–[60]
Integrity
Supply Chain Attacks
[61]–[64]
Command Manipulation
[65], [66]
Code Manipulation
[65], [67]
Malware Injection
[68]
Rogue Node
[69]–[71]
Broadcast Message Spoofing
[58]
Topology Attacks
[72], [73]
Sybil
[74]–[76]
Byzantine
[77], [78]
Availability
DOS/DDOS
[79]–[83]
Response Delay
[58], [59], [84]
1) Confidentiality
Eavesdropping: The attack (also known as traffic analysis
or packet sniffing) refers to the interception and analysis of
network traffic to gain sensitive information [45]. In smart
grids, eavesdropping may expose critical data to attackers
including energy consumption patterns, pricing information,
control messages, etc. Encryption and secure communication
protocols can help mitigate the risk of eavesdropping in smart
grids [46], [47].
Man-in-the-middle (MITM): These attacks occur when an
adversary intercepts communication between two parties, po-
tentially intercepting, modifying, or injecting packets without
the original participants’ knowledge [48]. In smart grids, a
successful MITM attack could lead to unauthorized access
to sensitive data, FDI , or the manipulation of control mes-
sages [49]. Defense strategies against MITM attacks include
cryptographic-based prevention (e.g., TLS), anomaly mitiga-
tion, and anomaly detection [50].
Unauthorized Access: Such attack aims to grant illegiti-
mate access to critical systems (e.g., control centers, energy
management platforms), resulting in the tampering of energy
usage data, disruption of grid operations, or breach of cus-
tomer information in smart grids [51]. One prevalent form of
unauthorized access is password pilfering, which steals users’
passwords to gain unauthorized access to sensitive information
or systems [52]. Preventing unauthorized access in smart grids
requires a combination of strong authentication, access control
policies, firewalls, and regular security audits [53], [54].
Reconnaissance Attacks: These attacks can either actively
scan the network to identify critical infrastructures or passively
monitor the network traffic to identify potential vulnerabilities
of grid’s operations, which serve as preliminary steps for
more advanced cyber aggression [57]. A specific instance of
reconnaissance, known as Modbus Network Scanning, scans


---

Page 7

---

7
the network to identify devices operating with the Modbus
protocol, and further launches attacks on the target devices
[56].
Message Replay: Such attack, also known as a replay attack,
is a type of cyber-attack where an attacker intercepts and
retransmits a valid data transmission, often with malicious
intent. One such example in smart grids is the baseline
response replay attack, where the attacker captures legitimate
responses from a Modbus device, and then replays these
responses at a later time to either mislead the system or
conceal malicious activities [58]–[60]. Such attacks can lead
to incorrect system states being reported, potentially leading to
misguided operational decisions or hidden malicious activities.
Replay attacks can be mitigated by using various security
measures such as time-stamping, sequence numbering, or
cryptographic techniques like nonce or digital signatures [45].
2) Integrity
Supply Chain Attacks: These attacks aim to compromise
a smart grid by targeting various stages of a product life
cycle (e.g., manufacturing, distribution, and maintenance) [61].
Particularly, hardware supply chain attacks aim to tamper with
or manipulate hardware components during the production or
distribution, potentially introducing backdoors or vulnerabili-
ties into smart grid equipments [62]. Also, in 2018, Bloomberg
reported that malicious microchips were inserted during the
manufacturing process, compromising many companies [63].
On the software side, supply chain attacks focus on compro-
mising the development, distribution, or update processes of
software, potentially leading to the installation of malicious
code within smart grids. A notable example is the SolarWinds
attack in 2020, where attackers embedded a malicious script
into the software updates, resulting in breaches of multiple
U.S. government agencies and companies [64].
Command Manipulation: Such attack aims to alter the con-
trol commands in smart grids, potentially leading to inappro-
priate operations, equipment damage, or service disruptions
[65]. A real-world example is Industroyer, a highly sophis-
ticated piece of malware, which was specifically designed
to target Ukraine’s power grid. In 2016, it successfully ma-
nipulated control commands, resulting in a significant power
outage [66].
Code Manipulation: This attack targets the software running
on smart grid systems, altering its behavior to introduce
vulnerabilities or facilitate unauthorized access [65]. A notable
example of code manipulation is the malware Flame (sKy-
WIper), which was discovered in 2012. It primarily targeted
computer systems in the Middle East, and was intricately
designed to manipulate code in order to steal sensitive infor-
mation and monitor user activities [67].
Malware Injection: The attack aims to insert malicious soft-
ware into systems, potentially disrupting their functionality,
stealing sensitive information, or facilitating further attacks. A
real-world instance of such an attack is the malware known
as BlackEnergy, which evolved from a simple DDoS platform
to a highly sophisticated, plug-in based malware capable of
targeting critical infrastructures. By exploiting vulnerabilities
in widely-used communication standards, BlackEnergy allows
attackers to gain unauthorized access, steal sensitive informa-
tion, and disrupt essential operations, posing a significant risks
to critical systems and infrastructure [68].
Rogue Node: Such attack aims to intercept, modify, or inject
false data, commands, or messages, directly causing security
breaches and system instability of smart grids [69]. Such
attacks can be mitigated by incorporating robust authentication
mechanisms that prevent unauthorized users from accessing
system assets [70], [71].
Broadcast Message Spoofing: The attack specifically targets
smart grids using the Modbus protocol, where an attacker
forges a broadcast message that appears to originate from a
legitimate source, potentially distributing incorrect commands
across the grid [58]. The objective of the attack is to deceive
the system into acting on fraudulent commands, emphasizing
the critical importance of secure and verifiable communication
within the smart grid infrastructure.
Topology Attacks: These attacks target the structure and
configuration of a network to disrupt the information flow
between its components and nodes [72], [73]. Such attacks
provide false or misleading data of the grid topology (e.g.,
fake routing tables or configuration files) to control systems,
potentially disrupting the communication in smart grids.
Sybil: The attack occurs when a malicious node in a
network illegitimately claims multiple identities [74], [75]. By
controlling a large number of identities, a Sybil attack can
disproportionately impact the network operations, manipulate
data aggregation, disrupt communication, or undermine trust-
based schemes [76]. Such attack is particularly threatening
to distributed systems (e.g., wireless sensor networks in smart
grids), where nodes often rely on information from other nodes
to make decisions or perform tasks.
Byzantine: This attack occurs in distributed systems when
one or more nodes behave maliciously or unpredictably, un-
dermining the system reliability [77]. As smart grids rely on
distributed control systems, malicious nodes can disseminate
conflicting information to various parts of the system, leading
to inaccurate data aggregation, communication disruption, or
incorrect system decisions [78].
3) Availability
DoS/DDoS Attacks: These attacks have different opera-
tional tactics but share a common objective - to overwhelm
a target system or network, rendering it unavailable or inac-
cessible. A DoS attack leverages one device to flood a target
with excessive traffic or requests, whereas a DDoS attack
coordinates multiple devices (e.g., botnets) to generate the
deluge of requests. In smart grids, such attacks may target key
components such as control systems or communication net-
works, potentially leading to significant disruptions in power
distribution and management [80]. Mirai botnet is a real-world
example of botnet-driven DDoS attacks, where the attacker
exploits vulnerable IoT devices to launch large-scale attacks
against various internet services [79]. To mitigate these attacks,
it is essential to implement robust network security protocols,
such as deploying IDSs, or adopting traffic filtering techniques.
Response Delay Attack: Such attack directly affects ser-
vice availability by intentionally increasing the latency in
the response of a Modbus device [59]. The resultant delays
can disrupt the real-time operation of the system, leading to


---

Page 8

---

8
synchronization issues, incorrect system states, and even un-
availability of control responses. For example, if the command
to boot power production in response to demand surge is
significantly delayed, it could result in power shortages and
outages.
Research challenges against cyber-layer attacks: Though
cryptography based authentication, encryption and IDSs can
help mitigate many cyber-layer attacks, defending against
them presents various challenges due to the complexity and
critical nature of the smart grid infrastructure. The diverse
range of attack vectors requires the defense strategies to be
both comprehensive and highly flexible. As smart grids are
interconnected, a cyber-layer attack may not only compromise
the integrity of the network, management, and application sub-
layers, but also cascade to other layers, resulting in more
extensive damage. It is necessary to deploy a suite of security
strategies that can work cohesively to provide robust protection
across all layers of the smart grids. Also, the continually
evolving attacks necessitate ongoing updates and adaptation
of security protocols and systems. Further, implementing ef-
fective security strategies should consider the potential false
positives and the imperative for immediate and rapid response
to threats, all while maintaining the grid’s operational integrity.
These challenges underscore the importance of developing
dynamic, resilient, and intelligent security solutions that can
mitigate the ever-changing threats to the cyber layer of smart
grids.
B. Cyber-physical Layer Attacks
Cyber-physical layer attacks exploit vulnerabilities in the
cyber-physical layers (including control, measurement and
sensor sub-layers), directly or indirectly impacting the smart
grid’s functionality. For example, an attack could disrupt con-
trol algorithms leading to equipment dysfunction or electricity
misrouting. Alternatively, an attacker could compromise the
integrity of sensor data, undermining the grid reliability and
resulting in power outages. Table III outlines the classification
of cyber-physical attacks based on their malicious objectives.
1) Confidentiality
Side Channel attacks: These attacks exploit inadvertent in-
formation leaks from physical systems to compromise sen-
sitive data. Such attacks usually target devices using crypto-
graphic techniques (e.g., smart meters, PMUs) [85]. Power
analysis attacks, for example, infer secret keys by analyzing
the power consumption patterns of a device during cryp-
tographic operations [86]. Electromagnetic analysis attacks
extract sensitive information, such as cryptographic keys, from
electromagnetic emissions of a device [87]. Timing attacks
exploit variations in operation times to gain sensitive data [88].
Mitigation strategies such as the adoption of secure hardware
designs, and randomization of timing or power consumption
patterns can be deployed to defend against such attacks. [89],
[90].
Insider Attacks: Such attacks are perpetrated by insiders
who have authorized access to the network and systems within
the smart grid. An insider could be an employee, contractor,
or even a business partner for their personal gains or malicious
TABLE III
TAXONOMY OF ATTACKS IN THE CYBER-PHYSICAL LAYER
Security Impact
Cyber-Physical Attack
Reference
Confidentiality
Side Channel Attack
[85]–[90]
Insider Attacks
[91]
Integrity
GPS Spoofing and Time Synchro-
nization Attacks
[92]–[95]
False Data Injection (FDI)
[96]–[102]
Attacks on Automatic Generation
Control (AGC)
[103], [104]
Attacks on Voltage Control
[105]–[110]
Demand Side Management Attacks
[111], [112]
Switching Attacks
[113]–[118]
Load Redistribution
[119]–[122]
Attacks in Vehicle-to-grid (V2G)
[123]–[125]
Aurora
[126]–[129]
Advanced
Persistent
Threats
(APTs)
[130]–[142]
Source ID Mix Attacks
[143]–[145]
Rogue Interloper
[146], [147]
Availability
Puppet Attacks
[148], [149]
intents. They have the sufficient knowledge of the system to
bypass the security enforcement, potentially resulting in data
theft, system damage, or operational disruption. IDS can be
deployed to identify suspicious activities of insider attacks
[91].
2) Integrity
Switching Manipulation Attacks: In switching manipulation
attacks, an adversary aims to manipulate the state of switches
(e.g., circuit breakers, transfer switches) to disrupt normal
grid operation and cause physical damage [113]–[117]. By
modifying the state of switches, the attacker can alter power
flows, cause overloads, or even isolate parts of the grid, leading
to significant operational challenges and risks [118].
Load Redistribution Attacks: In such attacks, an adversary
aims to manipulate the control system to alter the distribu-
tion of electrical loads across the network [119], [120]. The
attacks can be accomplished by falsifying data or dispatching
malicious commands to control systems [121]. By redistribut-
ing the load inappropriately, the attacker can cause physical
equipment to overload and potentially fail, leading to blackouts
or other disruptions of service [122].
Attacks in Vehicle-to-grid (V2G): V2G technologies allow
two-way energy exchange between electric vehicles (EVs) and
the power grid, enabling EVs to act as distributed energy
resources [123]. In the attack scenario, a malicious actor might
hack into the control systems of autonomous vehicles or the
V2G communication interface to manipulate power flow, spoof
charging/discharging commands, or disrupt grid balance by
injecting false data [124]. Such attacks could lead to local
and wider grid instabilities, causing power quality issues or
even blackouts. Moreover, the vehicle’s functionality could be
compromised, posing safety risks [125].
Aurora: The attack targets the electrical generators of a


---

Page 9

---

9
power grid and aims to de-synchronize the phase of a gen-
erator from the power grid (e.g., opening and closing circuit
breakers to alter the physical process of the power system). It
dynamically accelerates or decelerates the generator, imposing
mechanical stress and eventually damaging or destroying the
generator. Aurora attack is first discovered by the Idaho
National Laboratory in the United States in 2007. It is par-
ticularly concerning because it can cause physical damage
to critical infrastructure, and potentially lead to widespread
power outages [126]–[129].
Advanced Persistent Threats (APTs): APTs are a category
of prolonged and targeted cyber-attacks designed to gain
unauthorized access to a network and remain undetected for
an extended period. The primary goal of most APT attacks
is to achieve and maintain ongoing access to the targeted
network for monitoring activities and breaching sensitive data.
STUXNET, uncovered in 2010, is a specific example of
APTs capable of causing physical damages to cyber-physical
systems. The malicious worm targets the programmable logic
controllers (PLCs) within the supervisory control and data
acquisition (SCADA) system of Iran nuclear infrastructure
[130]. It exploited vulnerabilities to alter the frequency of
the electrical current powering the centrifuges, resulting in
physical damage [131]. Havex is another examples of APTs.
Developed by the Dragonfly cyber espionage group, Havex is
a Remote Access Trojan (RAT) that exploits vulnerabilities in
the energy sector, particularly in the United States and Europe.
It has been deployed in attacks on Industrial Control Systems
(ICS), with a focus on compromising critical infrastructures
[136]–[138]. CrashOverride, also known as Industroyer, is
malware employed on attack on the Ukrainian power grid in
2016 [139], [140]. It is the first malware designed specifically
to attack electric grids, which can directly control electricity
substation switches and circuit breakers [141]. All these at-
tacks highlight the potentially severe consequences that APTs
can have on the interconnected smart grid systems [132]–
[134].
Source ID Mix: Source ID mix is a type of data spoofing
attack that targets wide-area measurement systems in smart
grids. Instead of altering the actual measurements, source
ID mix tampers with the data from PMUs by confusing
their source identification tags. Such attacks can compromise
the operational reliability of the network, potentially leading
to incorrect actions based on faulty data interpretations. To
defend against such attacks, a more robust authentication
scheme is required to enforce data authenticity and integrity
in power systems [144], [145].
Location and Time Synchronization Attacks: These attacks
are significant threats to smart grid systems, exploiting their
reliance on precise timing for crucial operations [92], [93]. For
example, GPS Spoofing transmits counterfeit GPS signals to
mislead receivers, potentially causing system instability or in-
correct operational decisions, especially in the synchronization
of PMUs [94]. Similarly, Time Stamp Attacks (TSAs) interfere
with precise GPS timing, disrupting functionalities such as
transmission line fault detection and event location estimation
[95]. To protect against these timing-dependent threats, multi-
antenna-based algorithms have been proposed for quick GPS
spoofing detection.
False Data Injection (FDI):
These
attacks,
which
rank
among the most prevalent attacks in the smart grid, aim
to disrupt system operations by injecting false data [96].
Such attacks can mislead automated systems and operators by
introducing erroneous data into PMUs, leading to incorrect
operational decisions. State estimators and converters are
particularly vulnerable to FDI attacks, which can result in
inaccurate grid state estimates, inappropriate power distri-
bution decisions, and potential disruptions or inefficiencies
[97]–[99], [150]. FDI attacks can also compromise protection
systems designed to detect and isolate grid faults. If such
systems are compromised, their ability to accurately detect
faults may be impaired, potentially leading to prolonged
outages or equipment damage [100]. Additionally, during load
balancing, attackers may introduce false data about the load
on different grid parts, causing flawed power distribution
decisions and possibly resulting in overloads or underloads
in certain areas [101]. A variation of the FDI attack is the
blind FDI attack, where the adversary injects false data without
comprehensive system knowledge. Blind FDI attackers can
still cause significant disruption despite their limited system
understanding [102].
Attacks on Automatic Generation Control (AGC): Attacks
on AGC pose significant risks to the stability and reliability of
smart grids. The AGC system maintains a real-time balance
between generation and load by continually adjusting power
output from various generators. If an attacker manages to
manipulate the AGC, they can induce frequency instability,
overloading or underloading of generators, or even cause
blackouts. This could be achieved by injecting false data,
tampering with command signals, or exploiting vulnerabilities
in the communication network [103], [104].
Attacks on Voltage Control: In such attacks, adversaries
manipulate control systems to alter voltage levels within the
grid. They can be achieved by providing false data or sending
malicious commands to voltage control devices. Such attacks
are particularly concerning because it can lead to physical
damage and cascading failures in the power system due to
voltage instability [105].
Demand Side Management Attacks: Demand Side Manage-
ment Attacks, such as Pricing Attacks, aim to manipulate the
pricing signals for customers in a demand response system. In
pricing attacks, an attacker could falsify price signals to make
electricity seem more expensive or cheaper than it actually
is. This could lead customers to adjust their energy usage
based on false information, leading to instability of grid,
financial losses, or even physical damage due to unexpected
load changes [111], [112].
Rogue Interloper Attacks: A Rogue Interloper attack on
smart grids occurs when an unauthorized device or entity
infiltrates the network. The rogue device, through identity
spoofing or other forms of deception, presents itself as a
legitimate component within the smart grid network. Once
accepted as part of the system, it can engage in various
malicious activities, such as sending false data or commands,
disrupting network communication, or even assuming control
over certain operations. The potential consequences of such


---

Page 10

---

10
an attack are significant, leading to operational disruptions
or even physical damage to equipment. This highlights the
necessity of robust device authentication and stringent access
control measures within smart grid networks [146], [147].
3) Availability
Puppet Attacks: In puppet attacks, an attacker gains control
of a legitimate node within a network and uses it to carry
out malicious activities. The attacker can manipulate the
device to send false data, execute unauthorized commands,
or disrupt normal operations. Such attacks can indirectly
affect the functionality of the smart grid, for instance, by
exhausting the bandwidth needed for the control algorithms
to function correctly, leading to equipment malfunction or
electricity misrouting. Additionally, they can compromise the
network operation, potentially resulting in power outages or
damage to physical infrastructure [148].
Research challenges against cyber-physical layer at-
tacks: Defending against cyber-physical layer attacks in smart
grids presents unique challenges due to their direct impacts
on physical infrastructure. Unlike cyber-layer attacks, which
primarily target network and application, cyber-physical at-
tacks can cause actual physical damage to grid components.
These attacks exploit the control and sensor layers, leading to
malfunctions in equipment and mismanagement of electricity
flow. Maintaining integrity in grids is particularly challeng-
ing because many attacks in this layer specifically aim to
compromise this security aspect. The primary goal against
such attacks is to maintain grid stability and prevent physical
damage, even in the face of sophisticated attacks that aim
to disrupt the balance between supply and demand in smart
grids. The defense requires not only securing the network
from unauthorized access but also ensuring the integrity of
control commands and the authenticity of sensor data. This
necessitates implementing secure communication protocols,
real-time anomaly detection systems, and resilient control
strategies that can adapt to and compensate for malicious
activities.
C. Coordinated (hybrid) Attacks
Coordinated attacks utilize a mix of cyber and cyber-
physical attack methods to conduct simultaneous or sequen-
tial strikes on multiple components within the smart grid
[151]. These attacks can involve complex strategies, such as
launching a cyber attack to disrupt communication systems
followed by a physical attack on critical infrastructure, or
vice versa. Despite their complexity, coordinated attacks are
highly effective and difficult to detect because they leverage
covert masking tactics to compromise multiple security ob-
jectives simultaneously. These tactics can include blending
malicious actions with legitimate operations to avoid detection
and exploiting timing and sequencing to maximize impact.
Coordinated attacks typically compromise multiple aspects of
security. Table IV outlines various types of coordinated at-
tacks, classifying them based on directly compromised security
aspects.
Coordinated Topology Attacks: These attacks compromise
smart grid operations by manipulating both the physical and
TABLE IV
TAXONOMY OF COORDINATED ATTACKS IN SMART GRID
Security Impact
Coordinated Attacks
Reference
Integrity
Coordinated Data
Injection Attacks
[152]
Availability
Coordinated Load
Changing Attacks
[153], [154]
Confidentiality, Integrity
Coordinated Replay
Attacks
[155]
Integrity, Availability
Coordinated Topology
Attacks
[156]–[159]
Line Outage Masking
Attacks
[158],
[160]–[164]
Coordinated DoS Attacks
[151]
Confidentiality, Integrity,
Availability
Line Outage Masking
Attacks
[165], [166]
cyber components of the system simultaneously. They manip-
ulate state and topology data to mislead control center about
line outages and can result in cascading failures within the
grid. The attack strategy includes several steps: First, attackers
gather detailed topology information and system state data.
Next, they physically trip a transmission line to create a real
outage and use false data injection to hide the outage of
the tripped line. Finally, the attackers generate a fake outage
signal for another line, misleading the control center into
rerouting power improperly, which can potentially overload
critical lines. By carefully coordinating these actions, attackers
make it difficult for operators to distinguish between real and
fake outages, leading to incorrect operational decisions and
increased grid vulnerability [156].
Coordinated Data Injection Attacks: The primary goal of
these attacks is to mislead the energy management system by
injecting data that resembles normal grid operations, resulting
in incorrect control decisions and potential large-scale power
outages. These cooperative attackers exploit their knowledge
of the power network topology and collaborate to inject false
data that appears normal to avoid traditional detection mech-
anisms in smart girds. Quickest Detection has been proposed
to promptly detect and mitigate such coordinated false data
injections before they can cause significant damage to the
power grid infrastructure [152].
Coordinated Load Changing Attacks: Such attacks aim to
coordinate botnets (i.e., a large number of infected IoT de-
vices) to create sudden spikes or drops in energy usage,
disrupting the balance between power supply and demand in
a smart grid [153]. Typically, the attackers can manipulate
the infected IoT devices to simultaneously turn high-wattage
appliances on or off, creating the spikes or drops. The rapid
changes can destabilize the power grid, leading to automatic
load shedding and potentially causing widespread power out-
ages [154].
Coordinated Replay Attacks: These attacks aim to mask the
effects of physical attacks on the power grid by replaying
recorded normal meter measurements to control centers. To
be effective, coordinated replay attacks generally require com-
promising a large number of branch meters, ensuring the false


---

Page 11

---

11
data appears consistent and avoids detection. An optimized
approach to such attacks can evade bad data detection systems
by strategically altering only four meter measurements, mak-
ing them more stealthy and efficient [155]. Recent strategies to
defend against such attacks focuses on developing multilevel
programming models to enhance the interaction representation
between the control center and adversaries, thereby improving
the detection of overloaded transmission lines [164].
Line Outage Masking attacks: The objective of these at-
tacks is to mislead the control center into believing that the
grid is operating normally, despite one or more transmission
lines being out of service [160], [162]. These attacks pose a
significant threat to the stability and security of smart grids,
leading to severe operational risks and widespread power
outages [161]. To hide the line disruptions, attackers can
exploit RTUs and PMUs through malicious circuit breaker
manipulation and DDoS attacks, erasing the master boot record
and overwhelming call centers [158], [163], [164]. Continuous
monitoring and quick detection are critical to mitigate the risks
posed by Line Outage Masking attacks and to maintain the
integrity and reliability of the power grid [165]–[167].
Coordinated DoS Attacks: These attacks target both phys-
ical infrastructure and SCADA systems, resulting in severe
consequences. The strategy generally begins with an initial
physical disruption, such as tampering with power flow meters,
followed by DoS attacks to disrupt communication channels
between SCADA systems and their sensors or control devices.
Such coordination masks the disruption by making critical
measurement data unavailable, preventing system operators
from detecting the initial damage. Consequently, it leads to
incorrect operational decisions and a cascade of failures,
significantly impeding the grid’s ability to respond effectively
[151].
Research challenges against coordinated attacks: It is
crucial to develop sophisticated detection mechanisms to de-
fend against coordinated attacks in smart grids. One strategy is
the use of Collaborative Intrusion Detection Systems (CIDS),
which integrate IDS across different nodes to provide compre-
hensive monitoring and a unified response strategy [168]. Sim-
ilarly, the Coordinated Attack Response and Detection System
(CARDS) employs a signature-based model for efficient data
collection, analysis, and multi-source information correlation
[169]. Additionally, [152] improves detection solutions by un-
derstanding attacker-defender dynamics, designing distributed
detection algorithms, and evaluating the trade-offs between
detection speed and reliability. Coordinated attacks can also be
identified by analyzing cross-domain attack information [170].
[171] proposes a tri-level optimization model to defend against
coordinated attacks by strategically distributing defensive re-
sources on both the physical and cyber components of the
smart grid.
Despite advanced defense mechanisms, addressing coordi-
nated attacks on smart grids remains a significant challenge.
First, the complex nature of these attacks, targeting physical,
cyber, and cyber-physical layers simultaneously, complicates
the development of comprehensive defense strategies. Detect-
ing and mitigating such attacks requires advanced monitor-
ing systems capable of identifying and correlating anomalies
across different layers of the grid infrastructure. Second, it is
important to ensure scalability of defense strategies for large-
scale smart grids, demanding real-time data processing and
efficient algorithms. Furthermore, continuous improvement in
threat intelligence and information sharing among smart grid
operators is essential to defend against emerging coordinated
attack strategies. Finally, integrating advanced technologies,
such as machine learning, into security frameworks presents
both opportunities and challenges. While these technologies
can improve detection and response capabilities, they also
introduce new vulnerabilities that need to be addressed to
ensure robust defense mechanisms.
IV. DETECTION AND MITIGATION
In this section, we explore innovative approaches to detect
and mitigate different network attacks in smart grids. Specifi-
cally, we examine the application of four advanced techniques:
game theory, graph theory, blockchain, and machine learning.
These techniques have demonstrated effectiveness and preva-
lence in contemporary research. Each technique offers unique
advantages — game theory models the adversarial dynamics,
graph-based techniques leverage the networked nature of grids,
blockchain provides an immutable audit trail, and machine
learning enables adaptable and predictive defenses.
A. Game Theory-based Techniques
Game theory studies how participants make decisions in
strategic situations where the outcome for each depends on
the actions of others. It can be used to develop strong security
measures in smart grids by modeling the complex interactions
between different entities, such as utility providers, customers,
and potential attackers, and analyzing the various threats and
vulnerabilities involved [186]. This enables the development of
robust security strategies that account for the various players’
incentives and potential actions.
Game theory has multiple applications in network intrusion
detection for smart grids [187]. [177] proposes a 2-player zero-
sum stochastic security game to model interactions between
malicious attackers and an IDS. The authors in [172] develop
a decision-making and control algorithms via a game-theoretic
framework. They proposed a distributed IDS model and two
game-theoretic schemes: a security warning system for real-
time network security overviews and a finite game between
the attacker and IDS, with analytical solutions for Nash
equilibrium in the security game.
Nash equilibrium is a key concept in game theory, where
each participant’s strategy is optimal given the strategies of
all others. This principle ensures defense strategies are stable
and resilient. Nash equilibrium can also introduce mixed
strategies, where players randomly choose among multiple
actions with certain probabilities, introducing unpredictability
that complicates attack strategy of adversaries [188].
Game theory also offers adaptive defensive approaches
against dynamic smart grid threats (e.g., APTs) [189], [190].
One typical example is defensive deception, which misleads
attackers by manipulating their perceptions and beliefs to
protect systems and data [191]. Further, differential game


---

Page 12

---

12
TABLE V
TAXONOMY OF GAME THEORY DETECTION AND MITIGATION METHODS
Method
Attack
Detection
Mitigation
Strength
Weakness
Reference
(Non-)cooperative, Non-zero-sum
Intrusions
✓
✗
Flexibility, Scalability
Complexity
[172]
Sequential Game Model
Cyber
✗
✓
Interdependent Analysis
Simplified Assumptions, Static
[173]
Nash Equilibrium
Cyber
✓
✗
Robust
Complexity
[174]
Two-person Zero-Sum
FDI
✓
✗
Practical Scenarios
Complexity
[175]
Perfect Bayesian Equilibrium
FDI
✓
✗
Optimization
Not Realistic Assumption
[176]
Zero-sum Stochastic & Q-learning
Cyber
✓
✗
Stochastic Modeling
Scalability
[177]
Zero-sum Non-cooperative
Coordinated CP
✓
✗
Moving Target Defense
Convergence Time
[178]
Attack-Detection Evolutionary
FDI
✓
✓
Adaptability
Reliance on Simulations
[179]
Non-cooperative, Nash Equilibrium
DDoS
✓
✓
High Accuracy-Dynamic
Complexity
[180]
Bayesian Nash Equilibrium
DDoS
✓
✓
Computational Efficiency
Approximation Errors
[181]
Zero-sum Matrix
APT
✗
✓
Optimization
Not Convergent
[182]
Zero-sum
DoS/DDoS
✗
✓
Dynamic
Not Generalized
[183]
Stochastic Game with Q-Learning
APT
✗
✓
Adaptability
Performance Limitations
[184]
Nash-Cumulative Prospect Theory
APT
✓
✗
Performance
Scalability
[185]
models can be applied to dynamic defense processes and
trust frameworks for identifying vulnerabilities. The approach
significantly enhances APT attack detection’s accuracy, speed,
and efficiency.
Additionally, game theory is useful in modeling attacks
and defenses within smart grids, addressing challenges like
data injection attacks [173], energy theft in AMI [174], [192],
and cyber threats in the electricity market [175]. Moreover,
game theory is important in maintaining global network opti-
mization, especially in FDI attacks on networked microgrids
[176]. Another study presents new game-theoretic approaches
for corrupted sensor data detection [193]. It formulates the
problem as a zero-sum game with partial information, where
the detector aims to minimize the estimation error and the
attacker maximizes it, with the goal to develop efficient
solutions for optimal detectors.
Table V summarizes the game theory methods used, the
types of attacks detected or mitigated, and the strengths and
weaknesses of each method.
Research challenge of game theory applications in smart
grid security: Ensuring the practical implementation and
scalability of game-theoretic solutions in real-world smart
grids poses several challenges. One major challenge is ac-
curately modeling the complex interactions between various
entities, such as utility providers, customers, and attackers,
while considering their diverse objectives and strategies. Ad-
ditionally, developing realistic threat models that account for
the dynamic and evolving nature of cyber threats is difficult.
Game theory relies heavily on the assumption of rational
behavior, often not reflecting real-world events, resulting in
a gap between theory and practice. Another challenge is
the computational complexity of finding Nash equilibria and
optimal strategies within the resource constraints of smart
grid devices [188]. Scalability issues also increase as smart
grids expand, challenging the application of game theory in
large-scale smart grid networks [194]. Moreover, designing
robust game-theoretic models that can effectively manage
errors and adapt to unpredictable player behaviors is essential
for practical and reliable implementation in smart grid systems
[186].
B. Graph-based Techniques
Graph theory is the study of mathematical structures that
model pairwise interactions between objects, with vertices
(nodes) connected by edges (lines) [206]. Multiple graph-
based methods have been developed to defend against network
threats in smart grids [195], [207]–[210]. Recent studies
further extend beyond traditional graph theory, incorporating
graph neural networks to enhance attack detection and miti-
gation strategies. These techniques leverage the principles of
graph theory to uncover hidden structures and irregularities
within data, facilitating efficient attack detection across various
domains such as network security, power systems, and fraud
prevention [195], [197], [198], [207]–[215].
Graph-based algorithms have shown their potential for
intrusion detection in smart grids. For example, the GrIDS
network transforms network activities into event graphs for
suspicious activity detection. Similarly, the Local Deviation
Coefficient Graph-Based (LDCGB) algorithm improves data
labeling and clustering, enhancing discrimination between
normal and anomalous data [195]. Graph-based algorithms
can also be applied to fraud prevention [215], analyzing
connectivity patterns in communication networks to detect
potential fraudulent activities, including energy theft, billing
fraud, and FDI attacks. Additionally, graph-based methods
have been explored for network hardening, helping to extract
efficient flow paths and identify potential vulnerabilities that
attackers might exploit [196]. Case studies also demonstrate
the effectiveness of graph-based methods in addressing false
data injection in smart grids by utilizing Laplacian matrices
and Graph Fourier Transforms (GFT) [197], [198]. Further,
graph theory-based methods have been used to test the network


---

Page 13

---

13
TABLE VI
TAXONOMY OF GRAPH THEORY DETECTION AND MITIGATION METHODS
Method
Attack
Detection
Mitigation
Strength
Weakness
Reference
Graph-based Clustering
DDoS
✓
✗
Robustness
Manual Initialization
[195]
Attack Graphs
Multi-step Intrusion
✗
✓
Practical
Graph Simplifications
[196]
Graph Signal Processing
FDI
✓
✗
Measurement Compatibility
Complexity
[197]
Graph-based Outlier Detection
FDI
✓
✗
Adaptability
Data Dependency
[198]
Graph Analytic Metric
Pass-the-Hash
✗
✓
Quantitative
Complexity
[199]
Structural Temporal GNN
Anomalous Edges
✓
✗
Temporal & Structural
Potential Overfitting
[200]
Graph-based Classification
FDI
✓
✓
Observability Maintenance
Complexity
[201]
Attack Graphs
Multi-stage
✗
✓
Scalability
Complexity
[202]
Spatial-Temporal GNN
DDoS
✓
✓
High Accuracy
Not Generalized
[203]
Dynamic Reachability Graph
Path-the-Hash
✗
✓
Dynamic
Computational Resources
[204]
GNN
Infiltration
✓
✓
Scalability
Complexity
[205]
vulnerability of lateral movements and privilege escalation
attacks, preventing potential APTs [199]. Table VI summarizes
the graph theory methods against different attacks in smart
grids.
Research challenges of graph-based techniques in smart
grid security: Graph-based techniques in smart grid security
face several research challenges. One major challenge is the
scalability of these methods. As the size of smart grids
increases, the amount of data grows exponentially, making it
difficult to design a big data-driven, meaningful, and valid
graph for real-time data processing and analysis [216], [217].
Another challenge is the accuracy of anomaly detection. The
detection accuracy of graph-based methods may significantly
decrease due to noisy and sparse datasets [218], [219]. These
methods must effectively distinguish between normal oper-
ational variations and actual security threats to minimize
false positives and false negatives. Additionally, it also poses
technical and compatibility issues when incorporating graph-
based techniques with existing smart grid infrastructure and
communication protocols. Moreover, the dynamic nature of
smart grids, with constantly changing topologies and new
devices being added, requires adaptive and robust graph-based
models that can evolve with the system [200], [217]. Finally,
it is critical to protect the privacy and security of the data used
in graph-based methods, as these techniques rely on extensive
data collection and analysis, raising concerns about potential
data breaches and misuse.
C. BlockChain
Blockchain technology is a database system that allows for
transparent information sharing over a network by organiz-
ing data into sequentially linked blocks. Initially designed
for Bitcoin transactions [220], blockchain has been actively
applied in broad applications, especially toward the increased
operation efficiency and security of smart grids [221]. It uses
consensus algorithms, immutable ledgers, and decentralization
to provide a secure platform for data sharing across sectors
[222]. Blockchain technology enhances security by detecting
bad data, increasing resilience against network attacks, and
preventing data manipulation and tampering [3], [223]–[225].
A node/user requests 
for a transaction
A block is created
The transaction is check 
with predefined rules set 
in smart contract
Consensus mechanisms, 
such as PoW and PoS, 
allow all nodes to validate 
transactions
A distributed ledger
makes transactions
immutable across the 
blockchain network
The block is added 
to the network
Generation
Transmission
Distribution
Consumer
Ledger
Ledger
Ledger
Ledger
Ledger
Fig. 3. A workflow illustrating how blockchain technology improves smart
grid security.
To understand the role of blockchain in improving smart
grid security, it is important to emphasize the reliability it
brings through its consensus mechanisms. Particularly, devices
involved in power generation, transmission, distribution, or
consumption initiate transactions by creating blocks. These
blocks are validated by smart contracts, ensuring transactions
adhere to a predefined set of rules. Consensus mechanisms
like Proof of Work (PoW) and Proof of Stake (PoS) ensure
all nodes accept the transaction [231]. Once consensus is
achieved, the block is added to the blockchain, and the
transaction is permanently recorded in the distributed ledger.
This guarantees the immutability, security, and transparency of


---

Page 14

---

14
TABLE VII
TAXONOMY OF BLOCKCHAIN THEORY DETECTION AND MITIGATION METHODS
Method
Attack
Detection
Mitigation
Strengths
Weakness
Reference
PoW Consensus
DDoS
✗
✓
Decentralization
Complexity
[223]
Keyless Signature Infrastructure
Cyber
✓
✓
Real-Time Transactions
Interoperability, Latency
[224]
Blockchain-based Secure Distributed
Dynamic State Estimation
FDI
✓
✓
Controllable False Alarms
Detection Delays
[225]
PoW Consensus
Data Tampering
Unauthorized Access
✗
✓
Transparency
Complexity
[226]
Blockchain Signaling System
DDoS
✗
✓
Scalability
Complexity
[227]
PoW-PoS (trust-chain)
Insider (Sybil)
✗
✓
Resilient
Scalability
[228]
Data Driven Trust Mechanism
Greyhole-Blackhole
✓
✓
Decentralization
Scalability
[229]
Permissioned Consortium (Ethereum)
FDI
✓
✗
High Accuracy
Complexity
[230]
transactions. Figure 3 illustrate the information flow between
blockchain and smart grid operations, demonstrating the use
of smart contracts for transaction validation, consensus mech-
anisms for network-wide agreement, and a distributed ledger
to maintain the integrity and transparency of transaction data.
Blockchain technology provides a robust foundation for
improving security in smart grids, particularly through the
implementation of microgrids [232], [233]. These smaller,
autonomous grids facilitate the integration and management of
blockchain, which efficiently handles localized data and peer-
to-peer energy trading. The decentralized nature of blockchain
aligns well with microgrids’ structure, improving their se-
curity, transparency, and resilience. It ensures that energy
production and consumption data are securely recorded and
easily accessible. Additionally, decentralization mitigates sin-
gle points of failure and reduces vulnerability to cyber threats,
significantly enhancing the resilience and robustness of the
microgrid [234]. Practical examples include the Brooklyn
Microgrid project and the Power Ledger initiative in Aus-
tralia, both of which demonstrate how local energy trading
can be facilitated, making transactions easy and creating a
more democratic energy market [235]. The TransActive Grid
project further shows blockchain’s potential to transparently
log energy transactions, highlighting its applicability to smart
grid technology [236]. Table VII provides a comprehensive
overview of blockchain theory, including detection and miti-
gation methods for various attacks, as well as their strengths
and weaknesses.
Research challenges of blockchain techniques in smart
grid security: Although blockchain in smart grids brings
numerous security benefits, it also present several research
challenges [237]. One major challenge is scalability. Current
blockchain processing capabilities may not be sufficient to
handle the high volume of transactions in a large-scale smart
grid. The time required for increased transactions to be con-
firmed on the blockchain can introduce significant delays,
reducing transaction speed, increasing costs, and inhibiting
real-time energy trading [226], [238]–[240]. Additionally,
energy-intensive consensus mechanisms like Proof of Work
are not sustainable for resource-constrained devices in smart
grids [233], [241]. Research is needed to ensure low-latency
and energy-efficient transaction validation and confirmation
for real-time applications in smart grids. Interoperability is
another critical issue. It is challenging to seamlessly integrate
blockchain with current smart grid infrastructure and proto-
cols [233], [242]. The lack of standardization in blockchain
technology can lead to compatibility issues between different
systems and technologies. Ensuring interoperability is cru-
cial for creating comprehensive solutions that enhance the
security and efficiency of the grid ecosystem. Data privacy
is also a significant concern. Ensuring data privacy while
maintaining transparency on the blockchain is a complex
problem, especially with sensitive data involved in smart grids.
Disclosing transactional details can compromise user integrity
and confidentiality, violating privacy preferences [233]. Re-
search is needed to develop methods that ensure data privacy
without compromising the transparency and security benefits
of blockchain technology.
D. Machine Learning
Machine learning (ML) focuses on developing algorithms
and statistical models to identify patterns and make data-
driven decisions. These patterns include correlations, trends,
and anomalies within the data. By recognizing these patterns,
ML algorithms can predict outcomes and detect irregularities.
Through iterative processes, these algorithms improve their
accuracy and performance over time [317]. ML finds applica-
tion in many fields, including network security [318], natural
language processing [319], computer vision [320], agriculture
[321], and medicine [322].
Machine Learning 
Trained Model
PMU
RTU
Sensors
Attack happened or 
not? 
SCADA
Unknown data
Normal
Attack
Training Dataset
Training
Fig. 4.
Overview of Machine Learning-Based Attack Detection in Smart
Grids.
ML has also been extensively applied into smart grids
to improve its security. It assists smart grids in monitoring


---

Page 15

---

15
TABLE VIII
SUMMARY OF MACHINE LEARNING APPROACHES FOR ATTACK DETECTION IN SMART GRIDS
Learning Type
Specific Methods
Challenges
References
Supervised Learning
Classification, Regression, Neural Network
Methods
- Scarcity of high-quality labeled data
- Class imbalance and limited generalization to new attacks
- High computational intensity and black box nature of neural
network models
[22], [65],
[243]–[260]
Unsupervised Learning
Neural Network Methods, Clustering and
Outlier Detection Methods, Other Detection
Schemes
- High false positives/negatives and difficulty distinguishing
between normal behaviors and attacks without ground truth
- Complexity due to dynamic nature of smart grids and high
dimensionality of data
[261]–[274]
Semi-supervised Learning
Clustering-based Models, S3VM, Adver-
sarial Autoencoders (AAEs), Generative-
Adversarial-Based Semi-Supervised learn-
ing (GBSS), SS-Deep-ID, AE-GRU, GAN-
RNN, Semi-WTC, ESFCM
- Curse of dimensionality and noise in the dataset
- Challenges in handling complex attack patterns, overfitting,
and computational costs
- Data variability and integrity issues, such as incompleteness
or inconsistencies due to sensor or network failures
[243],
[275]–[285]
Ensemble Learning
Bagging, Boosting, Stacking, Extremely
Randomized Trees
- Computational complexity, especially in real-time systems
- Ensuring diversity among learners to prevent overfitting
while maintaining accuracy
[286]–[303]
Reinforcement Learning
SARSA,
Q-Learning,
DQN,
Attention-
aware DRL, Actor-Critic Methods, Deep
Deterministic Policy Gradient (DDPG)
- Sparse and delayed rewards due to the infrequency of attacks
- Computational complexity vs. real-time decision-making
- Difficulty in creating flexible models for evolving grid
dynamics and new attacks
[156],
[304]–[316]
grid operations and detecting unusual activities that indicate
security breaches. By analyzing vast amounts of data from
different sources, such as PMUs, RTUs, and other sensors
within the SCADA system, ML models can identify normal
and suspicious activities. These models employ advanced algo-
rithms and are trained on both regular and attack-pattern data,
including power consumption, operational logs, and sensor
readings, which allows them to effectively distinguish between
normal and abnormal behaviors. Upon detecting a potential
threat, an automated alert system immediately notifies grid
operators, enabling them to take appropriate action to mitigate
the risk. Figure 4 provides a representation of this process.
ML can be deployed in either centralized or distributed
configurations, depending on the specific infrastructure of the
smart grid [323]–[326]. In the centralized approach, data is
aggregated and processed in a single location. This method
simplifies data management and processing but can present
scalability issues as data volumes increase. On the other
hand, distributed ML processes data across multiple edge
locations, which can improve model scalability and efficiency.
However, it raises confidentiality concerns due to the need
to transfer, store, and process data in various locations. To
ensure data security in distributed settings, federated learning
algorithms have been developed, allowing models to be trained
across multiple decentralized devices without sharing raw data
[327]–[332]. This approach helps mitigate the risks associated
with data breaches and ensures that sensitive information
remains protected while still benefiting from the advantages
of distributed ML.
In this section, we examine various ML techniques that
show promise in the field of smart grid security. We classify
them into five categories: supervised, unsupervised, semi-
supervised, ensemble, and reinforcement learning. Each cat-
egory is discussed in detail, presenting its characteristics and
limitations. We also provide recent examples to demonstrate
their potential in enhancing smart grid security. Our studies
are summarized in Table VIII.
1) Supervised Learning Algorithms
Supervised learning algorithms leverage labeled training
data to develop models for attack detection and mitigation.
They can be classified into three groups: classification, regres-
sion, and neural network methods. Each group has a distinct
set of algorithms with specific application methods.
Classification Methods: In supervised learning, a variety of
algorithms have been applied to binary classification problems
in the context of attack detection.
The Perceptron operates as a fundamental learning algo-
rithm using a weight vector and input samples to predict
the occurrence of an attack. It iteratively adjusts the weights
until a specific criterion is met. However, it only ensures
convergence when the samples are linearly separable, making
it most suitable for attack scenarios where measurements can
be separated by a hyperplane [243].
The K-Nearest Neighbor (KNN) algorithm is used to clas-
sify instances by identifying the most prevalent class among
its k closest neighbors within the feature space. It has proven
effective in detecting FDI attacks, particularly in smaller-
scale smart grid systems [244] [245]. However, when the
feature vector size greatly exceeds the instance size, a situation
known as the curse of dimensionality arises. We can adopt
strategies such as feature selection algorithms, kernel methods
like Support Vector Machines (SVMs), or reducing instance
sizes to help mitigate the issue.
SVMs are designed to separate benign and corrupted mea-
surements by computing a hyperplane in a transformed feature
space. They introduce slack variables for flexibility when the
samples are not linearly separable and prove their efficacy in
high-dimensional spaces [22], [246]–[248].
Sparse Logistic Regression employs the Alternating Di-
rection Method of Multipliers (ADMM) to solve classifica-


---

Page 16

---

16
tion problems, effectively reducing computational complexity
while maintaining accuracy in large-scale or high-dimensional
datasets. Additionally, methods such as Decision Trees (DT)
and the Naive Bayes Classifier (NBC) have proven successful
in the development of Intrusion Detection Systems (IDS) for
smart grids. Decision Trees are adept at distinguishing between
normal and malicious activities, providing high accuracy and
true positive rates. Naive Bayes Classifiers, on the other hand,
are particularly effective in detecting Denial of Service (DoS)
attacks, including blackhole attacks, ensuring robust security
for smart grid systems [249], [250].
A recent study by He et al. [333] demonstrates the use
of classification techniques in smart grids for detecting FDI
attacks. They improve their model performance by using a
cross-entropy loss function and adjusting the learning rate with
Adam and cosine annealing algorithms.
Regression Methods: Regression techniques, such as lin-
ear regression, offer an alternative approach to classifica-
tion methods for detecting smart grid attacks. For instance,
Yip et al. presented two linear regression-based algorithms
to identify defective and compromised smart meters in a
neighborhood area network. These algorithms analyze reported
energy consumption data to detect anomalies, enabling the
successful identification of fraudulent consumers and faulty
smart meters, and providing an accurate estimation of energy
theft/loss [251]. However, it is important to note that while
linear regression can handle large datasets and establish a
quantitative relationship between variables, it requires a linear
relationship between variables and is sensitive to outliers.
Neural Network Methods: Neural Networks (NN) are pow-
erful machine learning models capable of identifying complex
patterns within large datasets. In smart grids, NNs have shown
great promise in detecting malicious activities, fraudulent
behaviors, and anomalies.
Deep Neural Networks (DNN), a subset of NNs with
multiple hidden layers, are particularly effective in learning in-
tricate patterns. Their ability to learn complex representations
makes them highly suitable for identifying various types of
attacks, such as energy fraud in consumer energy consumption
[256]. For example, autoencoders are effective in identifying
anomalies within the high-dimensional and noisy data of smart
grids. Huang et al. introduced a Stacked Sparse Denoising
Autoencoder (SSDAE) for electricity theft detection [252].
This model leverages sparsity, noise reduction, and the particle
swarm optimization algorithm to extract robust features and
set optimal error thresholds using a receiver operating char-
acteristic curve. Additionally, the Extreme Learning Machine
(ELM), a feed-forward NN, has been successfully employed
to detect False Data Injection (FDI) attacks [253]–[255].
Recurrent Neural Networks (RNN) are designed to recog-
nize patterns in sequences of data by utilizing their internal
state (memory) to process variable-length sequences. They
have been used to detect False Data Injection (FDI) attacks
targeting the smart grid [257]. Additionally, deep learning
frameworks that incorporate both Convolutional Neural Net-
works (CNN) and Long Short-Term Memory (LSTM) net-
works have been proposed to detect anomalies caused by FDI
attacks [258]. Another approach is the Temporal Graph Neural
Network (TGNN) proposed by Haghshenas et al. [259], which
detects and localizes FDI attacks in smart grids by leveraging
GNN to capture system topological information and state
measurements. Furthermore, Takiddin et al. [260] proposed
a strategy using a Generalized Graph Neural Network and a
graph autoencoder (GAE) to detect FDI attacks. This method
captures spatio-temporal features to improve generalization
and effectiveness against unseen attacks.
Research challenges of supervised learning in smart
grid security: Despite their effectiveness, supervised learning
methods in smart grid security face several challenges, includ-
ing the need for extensive labeled data, handling data imbal-
ance due to the rarity of attack events, and ensuring scalability
to process vast amounts of real-time data. The scarcity of high-
quality labeled data limits model training effectiveness and im-
pedes generalization to new attacks. This is further exacerbated
by class imbalance, where normal data far outnumbers attack
samples [65]. Additionally, these methods often suffer from
high computational intensity, significant data requirements for
training, and a lack of interpretability. Further, models must be
adaptable to evolving cyber threats, protect privacy while using
sensitive data, and manage substantial computational resource
demands.
2) Unsupervised Learning Algorithms
Unlike supervised learning that relies on labels, unsu-
pervised learning leverages ML algorithms to analyze and
cluster unlabeled datasets. These algorithms discover hidden
patterns without the need for human intervention. Given the
computational challenges and high false alarm rates of super-
vised learning in large-scale anomaly detection, unsupervised
learning emerges as a more effective alternative for identifying
anomalies without the need for labeled data [334].
Neural Network Methods: In unsupervised learning, Deep
Belief Networks (DBN) and autoencoders have been par-
ticularly effective to detect anomalies and attacks in smart
grids. In [261], [262], DBNs are utilized, leveraging unsu-
pervised learning for initial weight allocation and subsequent
model parameter fine-tuning, thereby outperforming SVM-
based detection methods. Autoencoder, another powerful tool
in unsupervised anomaly detection, have been employed in
ensemble methods with varying structures and connection
densities to enhance efficiency, diversity, and training time
[263]. Further, [264] incorporated autoencoders into six one-
class algorithms for anomaly detection. Autoencoder-based
classifiers have demonstrated notable effectiveness in real-
time detection of various DDoS attacks by utilizing the pre-
dictability of TCP traffic, outperforming supervised methods
in detecting new attacks [265]. Additionally, [266] intro-
duces Donut, an innovative unsupervised anomaly detection
algorithm based on Variational Autoencoder (VAE) for Key
Performance Indicators (KPIs), which are measurable values
that demonstrate how effectively an organization is achieving
key objectives. Although originally designed for web appli-
cations, this algorithm can be adapted to smart grid security
by monitoring the grid’s operational data in terms of power
quality, load forecasts, outage durations, energy production
levels, distribution efficiency, incident response times, and
cybersecurity incidents.


---

Page 17

---

17
Clustering and Outlier Detection Methods: Clustering and
outlier detection techniques in unsupervised learning also
hold significant potential for robust anomaly detection. For
example, [267] introduces UNIDS, a system that employs
Sub-Space Clustering for outlier detection, demonstrating the
power of clustering-based approaches in unsupervised learn-
ing. [268] further explores this field by utilizing the K-
Means clustering algorithm to identify suspicious activities
within networks. Several hybrid clustering techniques have
been proposed, including the method presented by [269],
which combines Sub-Space Clustering (SSC) and One Class
SVM (OCSVM) for unsupervised anomaly detection. This
approach, tested on the NSL-KDD dataset, detects attacks
without prior knowledge. Furthermore, Jiang et al. [270]
introduced a novel method to determine the outlier factor
of clusters, measuring the deviation degree of a cluster and
computing the cluster radius threshold. Their improved nearest
neighbor (INN) method and clustering-based unsupervised
intrusion detection show higher accuracy in detecting unknown
intrusions. Syarif et al. [271] evaluated the performance of
various clustering algorithms in network anomaly detection.
They found that while traditional misuse detection techniques
struggled with high unknown intrusion rates, clustering-based
anomaly detection showed promising accuracy. Finally, [272]
provides a comprehensive overview of various clustering and
outlier detection schemes, illustrating their integral role for
effective intrusion detection in smart grids.
Other Detection Schemes: Isolation forest, adaptive reso-
nance theory, and self-organizing maps have also emerged as
powerful unsupervised learning tools for anomaly detection. In
[273], the isolation forest technique is used to detect Covert
Data Integrity Assaults (CDIA) in smart grid networks. It
isolates anomalies using a binary tree structure, based on the
premise that anomalies are fewer and require fewer splits
to isolate. [274] introduces a machine learning-based IDS
for smart grids, using Adaptive Resonance Theory and Self-
Organizing Maps to identify cyber attacks, assess their impact
on physical measurements, and differentiate between normal,
faulty, and malicious states.
Research challenges of unsupervised learning in smart
grid security: Unsupervised learning for smart grid attack
detection faces several key challenges. First, it is inherently
difficult to distinguish between normal behavior and cyber-
attacks without labeled data. Additionally, it is challenging to
measure the performance and ensure the reliability of unsu-
pervised models in the absence of a ground truth. Collecting
high-quality data is essential to develop effective unsupervised
learning models that can accurately detect anomalies and cyber
attacks. Furthermore, smart grids produce vast amounts of
data continuously, and unsupervised learning models must be
capable of handling this volume in real-time to provide timely
detection and response to potential threats. The evolving nature
of cyber threats also require the models to be regularly updated
to recognize new attack patterns and strategies. Moreover,
unsupervised models often operate as black boxes, providing
little insight into how they reach their conclusions. This lack
of interpretability in detection decisions hampers trust and
deployment, as stakeholders need to understand and trust the
system’s decisions.
3) Semi-supervised Learning Algorithms
Semi-supervised learning models effectively utilize both
labeled and unlabeled data, offering robust solutions for var-
ious cybersecurity challenges in smart grids. [275] demon-
strates that the clustering-based semi-supervised models are
particularly effective for DDoS attack detection. Meanwhile,
the semi-supervised SVM model, presented in [276] and
[243], handles network intrusion detection and smart grid
attack detection with an impressive accuracy of up to 90
percent. Leveraging the strengths of autoencoders and GANs,
Adversarial Autoencoders (AAEs) proposed by [277] provide
an effective solution for detecting unobservable FDI attacks
in smart grids. Similarly, the Generative-Adversarial-Based
Semi-Supervised learning (GBSS) framework, discussed in
[278], utilizes conditional GANs for diagnosing cyber attacks
and faults in power grids, outperforming other semi-supervised
models under challenging learning conditions.
The SS-Deep-ID model, proposed by [279], incorporates
a multiscale residual temporal convolutional module and a
traffic attention mechanism. It proves superior in various
metrics and demonstrates computational effectiveness in real-
time intrusion detection for smart grids. Dairi et al. present
two innovative methods for anomaly detection: AE-GRU,
which combines a GRU-based stacked autoencoder, and GAN-
RNN, which integrates a GAN with an RNN for enhanced
cyber attack detection in smart grids [280]. The Semi-WTC
framework introduces an innovative semi-supervised method
that enhances attack detection in cybersecurity by combining
weight-task consistency and a recurrent prototype module
[281].
Rathore et al. introduce a semi-supervised learning-based
distributed attack detection framework for smart grids, utiliz-
ing a fog-based approach to enhance security and efficiency
through the novel ESFCM method [282]. Another study uti-
lizes semi-supervised learning combined with deep feature
extraction techniques to detect cyber-attacks by leveraging
normal operation data from PMUs, enabling the identification
of anomalies without requiring extensive examples of attack
patterns [283].
Research challenges of semi-supervised learning in
smart grid security: Semi-supervised learning models face
challenges in handling complex attack patterns, overfitting,
and the computational costs associated with large, high-
dimensional smart grid data. Reducing data complexity while
retaining critical features is challenging because standard
ML methods are not designed to effectively handle both
labeled and unlabeled data simultaneously. This necessitates
the development of new strategies to manage this combination
effectively [284]. The variability, incompleteness, and incon-
sistency of smart grid data, caused by sensor malfunctions
or network issues, further complicate the learning process.
Moreover, the dynamic evolution of attack vectors necessitates
continuous adaptation of semi-supervised learning models.
This adaptation is constrained by the scarcity of labeled data
for new threats, making it challenging for these models to
effectively detect emerging attacks. Finally, the computational
costs associated with processing large volumes of smart grid


---

Page 18

---

18
data and the need for real-time anomaly detection increase
the complexity, necessitating robust, efficient, and scalable
solutions.
4) Ensemble Learning
Ensemble learning combines multiple classifiers into a
meta-classifier to enhance detection accuracy and robustness
[286]. It has proven their effectiveness across various applica-
tions in smart grid security. For example, [290] demonstrates
the efficacy of ensemble learning for stealthy FDI attack
detection in smart grids by combining both supervised and
unsupervised classifiers. Elgarhy et al. develop a strategy to
secure electricity theft detectors against evasion attacks by
clustering smart grid consumers based on their consumption
patterns. They assign specific detectors to each cluster and
reinforce them with an ensemble of models [299].
Ensemble ML techniques, including bagging [335], boost-
ing [336], stacking [337], and extremely randomized trees, can
significantly improve the effectiveness of attack detection in
IDS for smart grids [287]–[289].
Bagging, or bootstrap aggregating, trains multiple base
learners on different subsets of the original dataset, providing
diversity among the learners and reducing model variance.
When implemented using REPTree as the base class, it ex-
hibits superior performance in terms of classification accuracy,
lower false positives, and reduced model-building time in IDSs
[291]. Moreover, [292] demonstrates that both bagging and
adaptive boosting can improve the reliability of cyber attack
detection in power systems.
Boosting constructs a robust classifier from multiple weak
ones by iteratively training on subsets of the total dataset
and assigning increased weight to misclassified examples, thus
concentrating the model on challenging cases. The CKS-FCS-
FLGB method has utilized boosting to effectively detect varied
FDI attacks even in small-sample datasets, enhancing the
stability and resistance of smart grid systems [293]. Hazman
et al. propose IDS-SIoEL, a sophisticated IDS for cyber-
physical systems that employs AdaBoost and feature selection
to enhance security performance [298].
Stacking combines the predictions of various base learning
models via a meta-learner to improve detection probability,
reduce false alarm rates, minimize miss detection rates, and
enhance overall accuracy [294]. [295] demonstrated the effi-
cacy of a tree-based stacking ensemble technique for IDSs,
while [296] underscored the value of stacking for effective
network intrusion detection using heterogeneous datasets.
The Extremely Randomized Trees method introduces a level
of randomness and robustness by randomizing the selection of
features and thresholds for each split in the tree. When coupled
with Kernel Principal Component Analysis for dimensionality
reduction, it displayed superior efficiency and accuracy in
detecting stealthy cyber attacks in smart grid networks [297].
Research challenges of ensemble Learning in smart grid
security: Detecting attacks in smart grids using ensemble
learning faces several significant challenges. One major issue
is handling heterogeneous and multi-sourced data, including
both cyber and cyber-physical systems, which increases the
complexity of identifying attacks [300], [301]. Another chal-
lenge is the computational complexity of combining multiple
machine learning models, especially in real-time systems
where rapid decision-making is crucial [302]. Additionally, en-
suring diversity among individual learners is critical; too much
similarity can lead to overfitting, while too much variation
may reduce accuracy [303]. These challenges complicate the
development and deployment of effective ensemble learning
models for smart grid security.
5) Reinforcement Learning
Reinforcement Learning (RL) trains algorithms to learn
from their environments. In a smart grid, RL works through
an iterative interaction process between an agent (e.g., a
detection system) and the environment (e.g., the smart grid
infrastructure). The agent observes the current state of the en-
vironment, such as network traffic patterns indicating potential
unauthorized access, power consumption readings revealing
unusual spikes suggestive of electrical theft or equipment
failure, and the operational status of grid components show-
ing signs of malfunction or tampering. The agent performs
actions within the environment to achieve specific goals, such
as detecting anomalies or security breaches. Following each
action, the agent receives feedback in the form of rewards
to learn and improve its strategy. The agent policy, which
maps observed environmental states to actions, evolves to
maximize cumulative rewards, enabling more accurate and
quick detection of attacks [304]. Figure 5 illustrates the RL
framework, depicting the agent as a detector, the environment
as the smart grid infrastructure, and the crucial interaction
driven by the state of the system.
sdsdsa
IDS
Smart Grid
Generation
Transmission
Distribution
Consumption
Smart Grid Environment
Actions
State
Reward
RL Agent (Attack Detectors)
Fig. 5.
A representation of the Reinforcement Learning process in Smart
Grids for attack detection.
RL methods such as State Action Rewarded State Action
(SARSA), Q-Learning, Deep Q-Network (DQN), Attention-
aware deep reinforcement learning (Attention-aware DRL),
Actor-Critic Methods, and Deep Deterministic Policy Gradient
(DDPG) have been extensively applied to address various
security challenges in smart grids.


---

Page 19

---

19
State Action Rewarded State Action (SARSA) is a model-
free RL method that learns the Q-value for state-action pairs to
guide the policy [338]. It enables robust, proactive attack de-
tection without requiring specific attack models and responds
sensitively to minor deviations from normal operations, thus
limiting the attacker’s action space. This approach has been
successfully implemented for online cyber attack detection in
smart grids [306].
Q-Learning is another model-free algorithm that learns the
value of an action in a particular state [339]. In smart grids, it
has been applied to analyze vulnerabilities against sequential
topology attacks [156], successfully identifying critical attack
sequences. However, it struggles with large and continuous
state-action spaces, and can hardly identify the best actions
when faced with delayed rewards.
Deep Q-Networks (DQNs) were introduced to overcome the
limitations of Q-Learning by combining Q-Learning with deep
neural networks [307]. DQNs have been employed to detect
data integrity attacks in AC power systems, offering improved
efficiency by avoiding the curse of dimensionality [308]. Li
et al. further enhanced this approach with a DQN-based DRL
algorithm that achieves both high accuracy and low latency
in detecting cyber attacks in smart grids [309]. This method
incorporates a dynamic AC system model, a continuous state-
space DQN within a Markov Decision Process (MDP) frame-
work, and a unique reward function to balance detection delay
and accuracy. El-Toukhy et al. introduce a method to detect
electricity theft attacks in smart power grids using DQN and
Double DQN (DDQN). These techniques adapt to dynamic
theft behaviors by learning optimal actions through exploration
and exploitation mechanisms [305]. Other researchers further
enhanced the DQN methodology by integrating it with LSTM
networks, effectively addressing the continuously changing
nature of grid states and the rare occurrence of attack states
[310]. Despite these improvements, DQNs still face challenges
with overestimating Q-values and maintaining stability during
the learning process.
Attention-aware DRL integrates an attention mechanism
into the DRL framework, allowing it to selectively focus on
critical parts of the state for feature extraction while avoiding
distractions from irrelevant details. This approach improves
the representation and distinguishability of states and has
demonstrated effectiveness in detecting FDI attacks in smart
grids [311].
There are also some DRL-based methods called Actor-Critic
methods balance the benefits of value-based and policy-based
methods by having two separate components, an actor that
decides the policy and a critic that evaluates it [312]. An
application of these methods in a real-world context can be
seen in the work by Feng and Xu [313], which presents an
optimal online defense strategy for CPS under unknown cyber-
attacks, employing a novel cyber-state dynamics model and a
game-theoretical actor-critic NN structure, further enhanced by
a DRL algorithm, leading to real-time, accurate, and timely
learning and implementation of optimal defense and worst
attack policies.
Actor-Critic methods balance the benefits of value-based
and policy-based methods by utilizing two separate compo-
nents: an actor that decides the policy and a critic that evaluates
it [312]. Feng and Xu present an optimal online defense
strategy that employs a novel cyber-state dynamics model and
an actor-critic neural network for unknown attacks mitigation
in cyber-physical systems [313]. This approach enables real-
time, accurate, and timely learning and implementation of
optimal defense and worst attack policies.
Deep Deterministic Policy Gradient (DDPG) is an algo-
rithm that combines DQN and actor-critic approaches, specif-
ically designed to handle environments with continuous ac-
tion spaces [314]. It has been successfully applied to detect
FDI cyber-attacks and identify vulnerabilities in conventional
index-based cyber-attack detection systems for DC microgrids
[315].
Research challenges of reinforcement Learning in smart
grid security: Although RL methods offer many opportunities
to enhance smart grid security, several challenges remain to be
addressed [340], [341]. First, high-quality data is essential for
training effective RL models, but obtaining sufficient labeled
data, especially for rare cyber-attack events, is difficult. The
infrequency of attacks leads to sparse and delayed rewards,
complicating the development of effective response policies.
Additionally, RL models need to balance the exploration of
new strategies with the exploitation of known ones; excessive
exploration can lead to suboptimal performance and compro-
mise grid security. Real-time processing capabilities are also
required for prompt decision-making, but this is challenging
due to the computational demands of many RL algorithms.
Furthermore, the dynamic nature of cyber threats requires
RL algorithms to continually and rapidly adapt to new and
evolving attack patterns. However, the complexity of smart
grid systems and the variability of attacks make it difficult to
create precise RL models that can accommodate evolving grid
dynamics and new threats.
V. FUTURE RESEARCH DIRECTIONS
We have conducted a comprehensive overview of various
emerging detection and mitigation strategies in smart grids,
discussing their advantages and research challenges. Despite
notable advancements, these challenges highlight the critical
need for continued research and development to enhance the
effectiveness and reliability of these techniques and ensure the
resilience and integrity of future smart grid infrastructures.
In this section, we present potential research directions that
are crucial for advancing these detection and mitigation tech-
niques.
A. Research Directions for Emerging Techniques
Research directions for game theory methods: Game the-
ory has shown great potential for developing decision-making,
analysis, and control algorithms in smart grid security. Future
research is needed to refine the proposed models, develop
practical algorithms, and decentralize decision-making process
[172]. Research could focus on developing game-theoretic
models that consider partial network failures instead of com-
plete blackouts, and incorporating varying levels of defense
success to create more realistic and adaptable security models.


---

Page 20

---

20
Additionally, it is crucial to account for the criticality of
different nodes in the network, concentrating defense efforts
on the most important nodes to optimize resource allocation.
Research could further expand the scale of existing models
to include nonlinear relationships, which will better represent
grid dynamics and account for performance drops due to
faulty nodes [173]. Also, probabilities of natural failures and
cyber attacks should be independently considered to make
models more comprehensive and realistic. Furthermore, future
research should aim to decentralize the decision-making pro-
cesses to improve the resilience and efficiency of smart grid
operations.
Research directions for graph-based methods: Graph-based
methods have shown promise in enhancing smart grid security
by modeling and analyzing complex relationships and interac-
tions within the grid. Future research could focus on several
key areas to further advance these techniques. First, It is crucial
to address scalability issues and optimize computational effi-
ciency to deploy graph-based methods in large-scale smart grid
systems. One promising direction is to reduce the complexity
of the attack graph by abstracting multiple vulnerabilities on
a host with similar effects into a generic vulnerability [208].
Another direction is to refine algorithms for traversing attack
graphs to identify the most cost-effective network configu-
ration changes, thereby protecting critical resources [196].
Additionally, research could expand graph-based models to
handle dynamic changes in the smart grid, such as fluctuating
power demands and varying network configurations, to im-
prove real-time analysis and response capabilities. It is also
essential to develop more sophisticated algorithms to detect
and mitigate cyber attacks by leveraging graph theory ability
to represent network topologies and dependencies. Graph-
based approaches could further incorporate machine learning
and artificial intelligence to enhance predictive capabilities,
enabling the early identification of potential threats.
Research directions for blockchain methods:
Blockchain
methods hold significant potential to enhance smart grid
security by providing decentralized, transparent, and tamper-
proof transaction records. Future research could focus on
several areas to advance these techniques. Firstly, it is
essential to develop scalable blockchain architectures tailored
to the high transaction volumes and real-time requirements of
smart grids. Improving consensus algorithms is also critical
to enhance transaction speed and reduce energy consumption.
Additionally, research should explore the interoperability of
blockchain systems with existing smart grid infrastructure
to ensure seamless integration and operation. Further, it
is important to investigate the economic implications and
cost-effectiveness of implementing blockchain for widespread
adoption
in
smart
grids.
Specifically,
a
technological
evaluation of blockchains should be conducted to assess
their scalability, robustness, resource usage, and transaction
costs, determining the practical feasibility and efficiency of
blockchain implementations in microgrid energy markets
[235]. Addressing these research directions will help realize
the full potential of blockchain methods in securing smart
grid operations.
Research directions for machine learning methods:
Machine learning methods offer promising advancements
for smart grid security, yet several key areas require further
research to fully realize their potential. Current applications in
smart grids face limitations such as scalability, data scarcity
and quality, model interpretability, computational complexity,
and adaptability, privacy concerns. Future research should
focus on developing more efficient and scalable machine
learning algorithms capable of handling the vast amounts of
data generated by smart grids. Advanced data preprocessing
and augmentation techniques should be developed to enhance
the quality of training data, addressing challenges of sparse
and incomplete data. Collaborative data sharing frameworks
among different smart grid operators could further enhance
data availability, providing a more comprehensive dataset for
model training and validation. Additionally, research could
aim to develop models that provide clear explanations for their
predictions and decisions, facilitating their integration into
existing smart grid infrastructures. It is also crucial to reduce
the computational complexity of machine learning algorithms
to ensure they can be deployed on resource-constrained
devices in smart grids. Real-time processing capabilities will
be essential for machine learning to continuously learn from
new data and adapt their strategies accordingly. Furthermore,
research should address privacy concerns by incorporating
advanced privacy-preserving techniques, such as federated
learning and differential privacy, to protect sensitive data
while enabling effective machine learning model training.
We will also explore new and emerging ML techniques
and concerns to enhance smart grid security. One promising
direction is the application of large language models (LLMs).
LLMs have the potential to understand complex attack patterns
and detect sophisticated zero-day attacks. Incorporating LLMs
into smart grid systems may significantly improve anomaly
detection. Another critical area is addressing the increasing
concern of adversarial machine learning attacks. As ML al-
gorithms become more prevalent in smart grids, adversarial
attacks pose a significant threat by misleading existing models
and bypassing detectors. Addressing these threats is crucial to
maintain the integrity of smart grid security systems.
In what follows, we will explore the potential and challenges
of using LLMs in smart grids and examine adversarial ML
attacks, their mechanisms, and mitigation strategies.
B. Large Language Models
LLMs like OpenAI’s GPT [342] and Google’s Gemini [343]
hold significant promise in the field of cybersecurity. They
offer substantial potential for improving the cybersecurity
of smart grids, particularly in digital substations [344]. For
instance, LLMs are effective for detecting DDOS attacks
when used with few-shot learning or fine-tuning [345]. Unlike
traditional ML models, which require frequent re-training to
accommodate new attack patterns, LLMs can interpret context
and respond to novel threats without explicit re-training. By
leveraging LLMs, we can analyze vast datasets and system
logs to identify patterns and detect irregularities that indi-
cate potential cyber-attacks [346]. For example, LLMs can
dynamically understand and adapt to new threats, offering


---

Page 21

---

21
a robust solution for anomaly detection in IEC 61850-based
communications, such as generic object-oriented system events
and sampled values messages [347].
However, deploying LLMs in smart grid security comes
with several limitations that need to be addressed. One major
concern is their tendency to memorize specific sequences
from their training data, which can raise privacy and security
issues [348]. This memorization can inadvertently lead to the
reproduction of personal information, highlighting the need for
meticulous data handling and privacy measures. Furthermore,
while LLMs show promise in understanding complex attack
patterns and data, their deployment for automatic vulnerabil-
ity detection remains challenging due to their limitations in
action-oriented capabilities. The ReAct, short for Reasoning
and Acting, aims to bridge this gap by enabling LLMs to
dynamically reason about their actions, update plans based on
environmental feedback, and improve task performance. Inte-
grating reasoning and acting makes LLMs more adaptive and
capable of handling dynamic and evolving scenarios, which
is crucial for tasks (e.g., automatic vulnerability detection in
smart grids) that require both understanding and proactive
interventions [349]. Additionally, LLMs are susceptible to tar-
geted attacks such as bad data injection and domain knowledge
extraction, emphasizing the need for robust threat models and
validation mechanisms [350]. Moreover, pre-trained LLMs are
not ready for deployment as-is; they need to be fine-tuned
or used with few-shot learning to provide context-specific
solutions [351].
These challenges highlight the need for comprehensive
strategies to ensure the secure deployment of LLMs in smart
grids. By carefully addressing these concerns, LLMs could
become a promising solution, potentially replacing traditional
machine learning methods and aiding in the development of
advanced IDSs, thereby enhancing overall system resilience.
C. Adversarial Machine Learning
Adversarial machine learning attacks exploit vulnerabilities
in ML models, leading to incorrect predictions and com-
promising the reliability and accuracy of decision-making
processes [352]. They aim to create malicious inputs, known
as adversarial examples, to manipulate ML models, posing a
significant risk to the reliability of ML based detection and
mitigation techniques. In particular, the adversarial examples
can blur the line between grid vulnerabilities and normal
grid performance, creating an attack surface for adversaries
to exploit breaches in smart grids without being detected.
Adversarial machine learning attacks can be launched in
two main ways: data poisoning attacks and evasion attacks.
Poisoning attacks inject adversarial data into the training set
to deceive the model during the training stage [353], [354].
These attacks can alter the learning process of the model,
leading to incorrect predictions even on clean data. Evasion
attacks, on the other hand, occur during the inference stage.
They make subtle changes to the test data, leading the model
to misclassify inputs it has learned to recognize [355]–[357].
Evasion attacks are more prevalent as they are easier to execute
and do not require access to the training phase. Attackers can
carry out evasion attacks with just query access to the model,
making them a more practical and immediate threat. Figure 6
illustrates the process of an adversarial attack on ML models
in smart grids.
Sensors
Smart 
Meters
IEDs
RTUs
PMUs
Voltage and 
Current sensors
Attacker
Add Noise
Adversarial Perturbation
False Prediction
Right Prediction
Machine Learning Models
Perturbed data
Input Data
Fig. 6. Illustration of an adversarial attack in a smart grid.
Adversarial attacks can be categorized into three main
types: white-box, gray-box, and black-box attacks. In white-
box attacks, the attacker has complete knowledge of the target
model, including its architecture, parameters, and training data.
It allows the attacker to generate highly effective adversarial
examples by exploiting specific vulnerabilities in the model
[358]–[360]. In gray-box attacks, the adversary has partial
knowledge of the target model, such as knowing the model ar-
chitecture but not having access to internal weights or specific
training data. Adversarial examples are often generated using
a surrogate model that has a similar architecture to the target
model, allowing the attacker to approximate the behavior of
the target model and identify vulnerabilities [361]–[363]. In
black-box attacks, the attacker has no direct knowledge about
the internals of the target model. Instead, they rely on querying
the model and observing its outputs to infer ways to generate
adversarial examples [364]–[371].
These attacks can severely disrupt smart grid operation by
causing misclassifications in attack detection, leading to incor-
rect energy predictions and faulty grid management decisions,
potentially resulting in power disruptions [352], [372]–[375].
Therefore, it is crucial to develop techniques to enhance the
resilience of ML models and make them robust against these
attacks.
Defending against adversarial ML attacks requires a com-
prehensive approach. One effective strategy is adversarial
training, where models are intentionally trained on adversarial
examples to improve their robustness and resilience [376].
Defensive distillation, which trains a secondary model using
the soft probabilities derived from a primary model, reduces
the model sensitivity to small input changes [377]. Regu-
larization methods, such as dropout and weight decay, can
also enhance model robustness. Another strategy uses input
transformations to move potential adversarial examples far
from the decision boundary of the model, combined with
detectors that identify inputs deviating from expected patterns
[378]. Thermometer encoding offers a new way to encode
categorical data. Instead of using a one-hot representation, it
employs a cumulative representation where each binary bit
corresponds to a temperature threshold, making it much harder
for attackers to manipulate inputs without being detected


---

Page 22

---

22
[379]. Further, game theory presents a promising approach
to enhance robustness against adversarial attacks. Equilibrium
strategies can create adaptive defenses that evolve in response
to the adversary’s tactics, making machine learning models
more resilient in dynamic environments [380], [381]. Finally,
continuous model evaluation and updating are essential to
adapt to new attack strategies and maintain security.
It remains a challenging task to address adversarial machine
learning attacks, as no single solution fits all purposes [382],
[383]. Heuristic-based defense mechanisms cannot protect
against all types of attacks. The transferability of adversarial
examples is another major challenge; if an attack works on one
model, it is likely to work on another model with a different
architecture or training data, allowing attackers to refine their
strategies on less secure models. In addition, while the ability
to predict and prevent adversarial attacks is desirable, it usually
requires high computational cost and may reduce the model
accuracy on legitimate inputs. Further, defenses that harden
a model against adversarial inputs often come with trade-
offs, such as decreased accuracy on clean inputs or increased
model complexity [384].These challenges against adversarial
machine learning attacks underscore the need for ongoing
research to develop new and flexible defense strategies, which
will mitigate risks and enhance the resilience of machine
learning models in smart grids [384]–[386].
VI. CONCLUSION
In this study, we have explored the intricate nature of
cyber, cyber-physical, and coordinated attacks on smart grids,
offering a comprehensive analysis of various attack types
and their implications for smart grid security. We critically
examine and compare a range of detection and mitigation
strategies, highlighting their potential benefits and limitations.
Additionally, we discuss potential future research directions
for emerging detection techniques, including the deployment
of LLMs in smart grid security and the emerging threat of
adversarial machine learning. Our study not only enhances
the understanding of current threats but also identifies key
areas for future research, emphasizing the urgent need for
advanced, robust detection algorithms to keep pace with the
rapidly evolving threats to smart grids.
REFERENCES
[1] S. M. Amin and B. F. Wollenberg, “Toward a smart grid: power delivery
for the 21st century,” IEEE power and energy magazine, vol. 3, no. 5,
pp. 34–41, 2005.
[2] X. Fang, S. Misra, G. Xue, and D. Yang, “Smart grid—the new and
improved power grid: A survey,” IEEE communications surveys &
tutorials, vol. 14, no. 4, pp. 944–980, 2011.
[3] M. Ghiasi, T. Niknam, Z. Wang, M. Mehrandezh, M. Dehghani, and
N. Ghadimi, “A comprehensive review of cyber-attacks and defense
mechanisms for improving security in smart grid energy systems: Past,
present and future,” Electric Power Systems Research, vol. 215, p.
108975, 2023.
[4] M. K. Hasan, A. A. Habib, Z. Shukur, F. Ibrahim, S. Islam, and M. A.
Razzaque, “Review on cyber-physical and cyber-security system in
smart grid: Standards, protocols, constraints, and recommendations,”
Journal of Network and Computer Applications, vol. 209, p. 103540,
2023.
[5] H. Kayan, M. Nunes, O. Rana, P. Burnap, and C. Perera, “Cybersecurity
of industrial cyber-physical systems: A review,” ACM Computing
Surveys (CSUR), vol. 54, no. 11s, pp. 1–35, 2022.
[6] D. Faquir, N. Chouliaras, V. Sofia, K. Olga, and L. Maglaras, “Cy-
bersecurity in smart grids, challenges and solutions,” AIMS Electronics
and Electrical Engineering, vol. 5, no. 1, pp. 24–37, 2021.
[7] T. N. Nguyen, B.-H. Liu, N. P. Nguyen, and J.-T. Chou, “Cyber
security of smart grid: attacks and defenses,” in ICC 2020-2020 IEEE
International Conference on Communications (ICC).
IEEE, 2020, pp.
1–6.
[8] V. C. Gungor, D. Sahin, T. Kocak, S. Ergut, C. Buccella, C. Cecati, and
G. P. Hancke, “Smart grid technologies: Communication technologies
and standards,” IEEE transactions on Industrial informatics, vol. 7,
no. 4, pp. 529–539, 2011.
[9] H. Farhangi, “The path of the smart grid,” IEEE power and energy
magazine, vol. 8, no. 1, pp. 18–28, 2009.
[10] W. Wang, Y. Xu, and M. Khanna, “A survey on the communication
architectures in smart grid,” Computer networks, vol. 55, no. 15, pp.
3604–3629, 2011.
[11] Y. Yan, Y. Qian, H. Sharif, and D. Tipper, “A survey on smart grid com-
munication infrastructures: Motivations, requirements and challenges,”
IEEE communications surveys & tutorials, vol. 15, no. 1, pp. 5–20,
2012.
[12] G. Dileep, “A survey on smart grid technologies and applications,”
Renewable energy, vol. 146, pp. 2589–2625, 2020.
[13] F. Rahimi and A. Ipakchi, “Demand response as a market resource
under the smart grid paradigm,” IEEE Transactions on smart grid,
vol. 1, no. 1, pp. 82–88, 2010.
[14] T. Ahmad, R. Madonski, D. Zhang, C. Huang, and A. Mujeeb, “Data-
driven probabilistic machine learning in sustainable smart energy/smart
energy systems: Key developments, challenges, and future research
opportunities in the context of smart grid paradigm,” Renewable and
Sustainable Energy Reviews, vol. 160, p. 112128, 2022.
[15] A. Mahmood, N. Javaid, M. A. Khan, and S. Razzaq, “An overview
of load management techniques in smart grid,” International Journal
of Energy Research, vol. 39, no. 11, pp. 1437–1450, 2015.
[16] K. M. Tan, V. K. Ramachandaramurthy, and J. Y. Yong, “Integration of
electric vehicles in smart grid: A review on vehicle to grid technolo-
gies and optimization techniques,” Renewable and Sustainable Energy
Reviews, vol. 53, pp. 720–732, 2016.
[17] Y. Yoldas¸, A. ¨Onen, S. Muyeen, A. V. Vasilakos, and I. Alan, “En-
hancing smart grid with microgrids: Challenges and opportunities,”
Renewable and Sustainable Energy Reviews, vol. 72, pp. 205–214,
2017.
[18] R. Langner, “Stuxnet: Dissecting a cyberwarfare weapon,” IEEE Secu-
rity & Privacy, vol. 9, no. 3, pp. 49–51, 2011.
[19] O. Symantec, “Dragonfly: Western energy sector targeted by sophisti-
cated attack group,” 2017.
[20] C.-W. Ten, G. Manimaran, and C.-C. Liu, “Cybersecurity for critical
infrastructures: Attack and defense modeling,” IEEE Transactions on
Systems, Man, and Cybernetics-Part A: Systems and Humans, vol. 40,
no. 4, pp. 853–865, 2010.
[21] M. Amin, “Security challenges for the electricity infrastructure,” Com-
puter, vol. 35, no. 4, pp. supl8–supl10, 2002.
[22] Y. Zhang, L. Wang, W. Sun, R. C. Green II, and M. Alam, “Distributed
intrusion detection system in a multi-layer network architecture of
smart grids,” IEEE Transactions on Smart Grid, vol. 2, no. 4, pp. 796–
808, 2011.
[23] M. Shao, B. Chen, S. Jancheska, B. Dolan-Gavitt, S. Garg, R. Karri,
and M. Shafique, “An empirical evaluation of llms for solving offensive
security challenges,” arXiv preprint arXiv:2402.11814, 2024.
[24] A. O. Otuoze, M. W. Mustafa, and R. M. Larik, “Smart grids security
challenges: Classification by sources of threats,” Journal of Electrical
Systems and Information Technology, vol. 5, no. 3, pp. 468–483, 2018.
[25] C. Peng, H. Sun, M. Yang, and Y.-L. Wang, “A survey on security
communication and control for smart grids under malicious cyber at-
tacks,” IEEE Transactions on Systems, Man, and Cybernetics: Systems,
vol. 49, no. 8, pp. 1554–1569, 2019.
[26] J. Liu, Y. Xiao, S. Li, W. Liang, and C. P. Chen, “Cyber security
and privacy issues in smart grids,” IEEE Communications surveys &
tutorials, vol. 14, no. 4, pp. 981–997, 2012.
[27] V. K. Mololoth, S. Saguna, and C. ˚Ahlund, “Blockchain and machine
learning for future smart grids: A review,” Energies, vol. 16, no. 1, p.
528, 2023.
[28] P. Jokar, N. Arianpoo, and V. C. Leung, “A survey on security issues
in smart grids,” Security and Communication Networks, vol. 9, no. 3,
pp. 262–273, 2016.
[29] E. Santacana, G. Rackliffe, L. Tang, and X. Feng, “Getting smart,”
IEEE power and energy magazine, vol. 8, no. 2, pp. 41–48, 2010.


---

Page 23

---

23
[30] J. Stoustrup, A. Annaswamy, A. Chakrabortty, and Z. Qu, “Smart grid
control,” Springer International Publishing. doi, vol. 10, pp. 978–3,
2019.
[31] N. M. G. Strategy, “Advanced metering infrastructure,” US Department
of Energy Office of Electricity and Energy Reliability, 2008.
[32] W. R. Cassel, “Distribution management systems: Functions and pay-
back,” IEEE Transactions on Power Systems, vol. 8, no. 3, pp. 796–801,
1993.
[33] D. Shirmohammadi, W. E. Liu, K. C. Lau, and H. W. Hong, “Distribu-
tion automation system with real-time analysis tools,” IEEE Computer
Applications in Power, vol. 9, no. 2, pp. 31–35, 1996.
[34] R. E. Wilson, “Pmus [phasor measurement unit],” IEEE Potentials,
vol. 13, no. 2, pp. 26–28, 1994.
[35] C. J. Tavora, “The remote link unit—an advanced remote terminal
concept,” IEEE Transactions on Industrial Electronics and Control
Instrumentation, no. 3, pp. 151–155, 1979.
[36] D. J. Gaushell and H. T. Darlington, “Supervisory control and data
acquisition,” Proceedings of the IEEE, vol. 75, no. 12, pp. 1645–1658,
1987.
[37] W. Mittelstadt, P. Krause, R. Wilson, P. Overholt, D. Sobajic, J. Hauer,
and D. Rizy, “The doe wide area measurement system (wams) project:
Demonstration of dynamic information technology for the future power
system,” USDOE Bonneville Power Administration, Portland, OR
(United States), Tech. Rep., 1996.
[38] R. H. Lasseter and P. Paigi, “Microgrid: A conceptual solution,” in 2004
IEEE 35th annual power electronics specialists conference (IEEE Cat.
No. 04CH37551), vol. 6.
IEEE, 2004, pp. 4285–4290.
[39] M. F. Akorede, H. Hizam, and E. Pouresmaeil, “Distributed energy
resources and benefits to the environment,” Renewable and sustainable
energy reviews, vol. 14, no. 2, pp. 724–734, 2010.
[40] P. F. Ribeiro, B. K. Johnson, M. L. Crow, A. Arsoy, and Y. Liu, “Energy
storage systems for advanced power applications,” Proceedings of the
IEEE, vol. 89, no. 12, pp. 1744–1756, 2001.
[41] Q. Zhang and J. Li, “Demand response in electricity markets: A
review,” in 2012 9th international conference on the European Energy
market.
IEEE, 2012, pp. 1–8.
[42] M. Majdalawieh, F. Parisi-Presicce, and D. Wijesekera, “Dnpsec:
Distributed network protocol version 3 (dnp3) security framework,”
Advances in Computer, Information, and Systems Sciences, and Engi-
neering, vol. 1, pp. 227–234, 2006.
[43] A. Swales et al., “Open modbus/tcp specification,” Schneider Electric,
vol. 29, no. 3, p. 19, 1999.
[44] O. Standard, “Mqtt version 3.1. 1,” URL http://docs. oasis-open.
org/mqtt/mqtt/v3, vol. 1, p. 29, 2014.
[45] Z. A. Baig and A.-R. Amoudi, “An analysis of smart grid attacks and
countermeasures.” J. Commun., vol. 8, no. 8, pp. 473–479, 2013.
[46] C. Valli, A. Woodward, C. Carpene, P. Hannay, M. Brand, R. Karvinen,
and C. Holme, “Eavesdropping on the smart grid,” 2012.
[47] J. Tyav, S. Tufail, S. Roy, I. Parvez, A. Debnath, and A. Sarwat, “A
comprehensive review on smart grid data security,” SoutheastCon 2022,
pp. 8–15, 2022.
[48] M. Z. Gunduz and R. Das, “Analysis of cyber-attacks on smart grid ap-
plications,” in 2018 International Conference on Artificial Intelligence
and Data Processing (IDAP).
IEEE, 2018, pp. 1–5.
[49] P. Wlazlo, A. Sahu, Z. Mao, H. Huang, A. Goulart, K. Davis,
and S. Zonouz, “Man-in-the-middle attacks and defence in a power
system cyber-physical testbed,” IET Cyber-Physical Systems: Theory
& Applications, vol. 6, no. 3, pp. 164–177, 2021.
[50] M. Conti, N. Dragoni, and V. Lesyk, “A survey of man in the middle
attacks,” IEEE communications surveys & tutorials, vol. 18, no. 3, pp.
2027–2051, 2016.
[51] N. Komninos, E. Philippou, and A. Pitsillides, “Survey in smart grid
and smart home security: Issues, challenges and countermeasures,”
IEEE Communications Surveys & Tutorials, vol. 16, no. 4, pp. 1933–
1954, 2014.
[52] Y. Yang, T. Littler, S. Sezer, K. McLaughlin, and H. Wang, “Impact
of cyber-security issues on smart grid,” in 2011 2nd IEEE PES
International Conference and Exhibition on Innovative Smart Grid
Technologies.
IEEE, 2011, pp. 1–7.
[53] D. B. Rawat and C. Bajracharya, “Cyber security for smart grid
systems: Status, challenges and perspectives,” SoutheastCon 2015, pp.
1–6, 2015.
[54] C.-C. Sun, A. Hahn, and C.-C. Liu, “Cyber security of a power grid:
State-of-the-art,” International Journal of Electrical Power & Energy
Systems, vol. 99, pp. 45–56, 2018.
[55] Z. El Mrabet, N. Kaabouch, H. El Ghazi, and H. El Ghazi, “Cyber-
security in smart grid: Survey and challenges,” Computers & Electrical
Engineering, vol. 67, pp. 469–482, 2018.
[56] M. Bristow, “Modscan: a scada modbus network scanner,” in DefCon-
16 Conf., Las Vegas, NV, 2008.
[57] J. Gonzalez and M. Papa, “Passive scanning in modbus networks,” in
Critical Infrastructure Protection 1.
Springer, 2008, pp. 175–187.
[58] P. Huitsing, R. Chandia, M. Papa, and S. Shenoi, “Attack taxonomies
for the modbus protocols,” International Journal of Critical Infrastruc-
ture Protection, vol. 1, pp. 37–44, 2008.
[59] P. Radoglou-Grammatikis, I. Siniosoglou, T. Liatifis, A. Kourouniadis,
K. Rompolos, and P. Sarigiannidis, “Implementation and detection of
modbus cyberattacks,” in 2020 9th International Conference on Modern
Circuits and Systems Technologies (MOCAST).
IEEE, 2020, pp. 1–4.
[60] F. Aloul, A. Al-Ali, R. Al-Dalky, M. Al-Mardini, and W. El-Hajj,
“Smart grid security: Threats, vulnerabilities and solutions,” Interna-
tional Journal of Smart Grid and Clean Energy, vol. 1, no. 1, pp. 1–6,
2012.
[61] O. Duman, M. Ghafouri, M. Kassouf, R. Atallah, L. Wang, and M. Deb-
babi, “Modeling supply chain attacks in iec 61850 substations,” in
2019 IEEE International Conference on Communications, Control, and
Computing Technologies for Smart Grids (SmartGridComm).
IEEE,
2019, pp. 1–6.
[62] V. V. Rao, R. Marshal, and K. Gobinath, “The iot supply chain
attack trends-vulnerabilities and preventive measures,” in 2021 4th
International Conference on Security and Privacy (ISEA-ISAP). IEEE,
2021, pp. 1–4.
[63] B. Businessweek, “The big hack: How china used a tiny chip to
infiltrate us companies,” Bloomberg, New York, NY, USA, Tech. Rep,
vol. 4, 2018.
[64] E. D. Wolff, K. Growley, M. Gruden et al., “Navigating the solarwinds
supply chain attack,” The Procurement Lawyer, vol. 56, no. 2, 2021.
[65] A. S. Musleh, G. Chen, and Z. Y. Dong, “A survey on the detection
algorithms for false data injection attacks in smart grids,” IEEE
Transactions on Smart Grid, vol. 11, no. 3, pp. 2218–2234, 2019.
[66] A. Cherepanov and R. Lipovsky, “Industroyer: Biggest threat to in-
dustrial control systems since stuxnet,” WeLiveSecurity, ESET, vol. 12,
2017.
[67] B. Bencs´ath, G. P´ek, L. Butty´an, and M. Felegyhazi, “The cousins of
stuxnet: Duqu, flame, and gauss,” Future Internet, vol. 4, no. 4, pp.
971–1003, 2012.
[68] R. Khan, P. Maynard, K. McLaughlin, D. Laverty, and S. Sezer, “Threat
analysis of blackenergy malware for synchrophasor based real-time
control and monitoring in smart grid,” in 4th International Symposium
for ICS & SCADA Cyber Security Research 2016 4, 2016, pp. 53–63.
[69] A. Alrawais, A. Alhothaily, C. Hu, and X. Cheng, “Fog computing
for the internet of things: Security and privacy issues,” IEEE Internet
Computing, vol. 21, no. 2, pp. 34–42, 2017.
[70] K. Zaidi, M. B. Milojevic, V. Rakocevic, A. Nallanathan, and M. Ra-
jarajan, “Host-based intrusion detection for vanets: A statistical ap-
proach to rogue node detection,” IEEE transactions on vehicular
technology, vol. 65, no. 8, pp. 6703–6714, 2015.
[71] A. Sahu, H. K. Tippanaboyana, L. Hefton, and A. Goulart, “Detection
of rogue nodes in ami networks,” in 2017 19th International Conference
on Intelligent System Application to Power Systems (ISAP).
IEEE,
2017, pp. 1–6.
[72] J. Kim and L. Tong, “On topology attack of a smart grid: Undetectable
attacks and countermeasures,” IEEE Journal on Selected Areas in
Communications, vol. 31, no. 7, pp. 1294–1305, 2013.
[73] X. Liu and Z. Li, “Local topology attacks in smart grids,” IEEE
Transactions on Smart Grid, vol. 8, no. 6, pp. 2617–2626, 2016.
[74] B. N. Levine, C. Shields, and N. B. Margolin, “A survey of solutions to
the sybil attack,” University of Massachusetts Amherst, Amherst, MA,
vol. 7, p. 224, 2006.
[75] J. Newsome, E. Shi, D. Song, and A. Perrig, “The sybil attack in sensor
networks: analysis & defenses,” in Proceedings of the 3rd international
symposium on Information processing in sensor networks, 2004, pp.
259–268.
[76] P. Sarigiannidis, E. Karapistoli, and A. A. Economides, “Detecting
sybil attacks in wireless sensor networks using uwb ranging-based
information,” Expert Systems with Applications, vol. 42, no. 21, pp.
7560–7572, 2015.
[77] K. J. Ross, K. M. Hopkinson, and M. Pachter, “Using a distributed
agent-based communication enabled special protection system to en-
hance smart grid security,” IEEE Transactions on Smart Grid, vol. 4,
no. 2, pp. 1216–1224, 2013.


---

Page 24

---

24
[78] L. Lamport, R. Shostak, and M. Pease, “The byzantine generals
problem,” in Concurrency: the works of leslie lamport, 2019, pp. 203–
226.
[79] M. Antonakakis, T. April, M. Bailey, M. Bernhard, E. Bursztein,
J. Cochran, Z. Durumeric, J. A. Halderman, L. Invernizzi, M. Kallitsis
et al., “Understanding the mirai botnet,” in 26th {USENIX} security
symposium ({USENIX} Security 17), 2017, pp. 1093–1110.
[80] A. Huseinovi´c, S. Mrdovi´c, K. Bicakci, and S. Uludag, “A survey of
denial-of-service attacks and solutions in the smart grid,” IEEE Access,
vol. 8, pp. 177 447–177 470, 2020.
[81] I. Ortega-Fernandez and F. Liberati, “A review of denial of service
attack and mitigation in the smart grid using reinforcement learning,”
Energies, vol. 16, no. 2, p. 635, 2023.
[82] S. Y. Diaba and M. Elmusrati, “Proposed algorithm for smart grid
ddos detection based on deep learning,” Neural Networks, vol. 159,
pp. 175–184, 2023.
[83] G. Torres, S. Shrestha, and S. Misra, “icad: Information-centric network
architecture for ddos protection in the smart grid,” in 2022 IEEE
International Conference on Communications, Control, and Computing
Technologies for Smart Grids (SmartGridComm).
IEEE, 2022, pp.
154–159.
[84] B. Moussa, M. Debbabi, and C. Assi, “A detection and mitigation
model for ptp delay attack in a smart grid substation,” in 2015 IEEE
International Conference on Smart Grid Communications (SmartGrid-
Comm).
IEEE, 2015, pp. 497–502.
[85] F.-X. Standaert, “Introduction to side-channel attacks,” Secure inte-
grated circuits and systems, pp. 27–42, 2010.
[86] T.-H. Le, C. Canovas, and J. Cl´ediere, “An overview of side channel
analysis attacks,” in Proceedings of the 2008 ACM symposium on
Information, computer and communications security, 2008, pp. 33–43.
[87] K. Gandolfi, C. Mourtel, and F. Olivier, “Electromagnetic analysis:
Concrete results,” in Cryptographic Hardware and Embedded Sys-
tems—CHES 2001: Third International Workshop Paris, France, May
14–16, 2001 Proceedings 3.
Springer, 2001, pp. 251–261.
[88] Z. H. Jiang, Y. Fei, and D. Kaeli, “A novel side-channel timing attack
on gpus,” in Proceedings of the on Great Lakes Symposium on VLSI
2017, 2017, pp. 167–172.
[89] H. Wang, H. Sayadi, T. Mohsenin, L. Zhao, A. Sasan, S. Rafatirad, and
H. Homayoun, “Mitigating cache-based side-channel attacks through
randomization: A comprehensive system and architecture level anal-
ysis,” in 2020 Design, Automation & Test in Europe Conference &
Exhibition (DATE).
IEEE, 2020, pp. 1414–1419.
[90] W. Cilio, M. Linder, C. Porter, J. Di, D. R. Thompson, and S. C. Smith,
“Mitigating power-and timing-based side-channel attacks using dual-
spacer dual-rail delay-insensitive asynchronous logic,” Microelectronics
Journal, vol. 44, no. 3, pp. 258–269, 2013.
[91] H. Bao, R. Lu, B. Li, and R. Deng, “Blithe: Behavior rule-based insider
threat detection for smart grid,” IEEE Internet of Things Journal, vol. 3,
no. 2, pp. 190–205, 2015.
[92] X. Fan, L. Du, and D. Duan, “Synchrophasor data correction under gps
spoofing attack: A state estimation-based approach,” IEEE Transactions
on Smart Grid, vol. 9, no. 5, pp. 4538–4546, 2017.
[93] Z. Zhang, S. Gong, A. D. Dimitrovski, and H. Li, “Time synchroniza-
tion attack in smart grid: Impact and analysis,” IEEE Transactions on
Smart Grid, vol. 4, no. 1, pp. 87–98, 2013.
[94] A. Jafarnia-Jahromi, A. Broumandan, J. Nielsen, and G. Lachapelle,
“Gps vulnerability to spoofing threats and a review of antispoofing
techniques,” International Journal of Navigation and Observation, vol.
2012, 2012.
[95] S. Gong, Z. Zhang, M. Trinkle, A. D. Dimitrovski, and H. Li, “Gps
spoofing based time stamp attack on real time wide area monitoring
in smart grid,” in 2012 IEEE Third International Conference on Smart
Grid Communications (SmartGridComm).
IEEE, 2012, pp. 300–305.
[96] G. Liang, J. Zhao, F. Luo, S. R. Weller, and Z. Y. Dong, “A review
of false data injection attacks against modern power systems,” IEEE
Transactions on Smart Grid, vol. 8, no. 4, pp. 1630–1638, 2016.
[97] Y. Liu, P. Ning, and M. K. Reiter, “False data injection attacks
against state estimation in electric power grids,” ACM Transactions on
Information and System Security (TISSEC), vol. 14, no. 1, pp. 1–33,
2011.
[98] R. B. Bobba, K. M. Rogers, Q. Wang, H. Khurana, K. Nahrstedt,
and T. J. Overbye, “Detecting false data injection attacks on dc
state estimation,” in Preprints of the first workshop on secure control
systems, CPSWEEK, vol. 2010.
Stockholm, Sweden, 2010.
[99] L. Xie, Y. Mo, and B. Sinopoli, “False data injection attacks in
electricity markets,” in 2010 First IEEE International Conference on
Smart Grid Communications.
IEEE, 2010, pp. 226–231.
[100] A. Teixeira, S. Amin, H. Sandberg, K. H. Johansson, and S. S. Sastry,
“Cyber security analysis of state estimators in electric power systems,”
in 49th IEEE conference on decision and control (CDC). IEEE, 2010,
pp. 5991–5998.
[101] H. Zhang, W. Meng, J. Qi, X. Wang, and W. X. Zheng, “Distributed
load sharing under false data injection attack in an inverter-based
microgrid,” IEEE Transactions on Industrial Electronics, vol. 66, no. 2,
pp. 1543–1551, 2018.
[102] Z.-H. Yu and W.-L. Chin, “Blind false data injection attack using pca
approximation method in smart grid,” IEEE Transactions on Smart
Grid, vol. 6, no. 3, pp. 1219–1226, 2015.
[103] S. Sridhar and M. Govindarasu, “Model-based attack detection and
mitigation for automatic generation control,” IEEE Transactions on
Smart Grid, vol. 5, no. 2, pp. 580–591, 2014.
[104] A. Ameli, A. Hooshyar, E. F. El-Saadany, and A. M. Youssef, “Attack
detection and identification for automatic generation control systems,”
IEEE Transactions on Power Systems, vol. 33, no. 5, pp. 4760–4774,
2018.
[105] Y. Isozaki, S. Yoshizawa, Y. Fujimoto, H. Ishii, I. Ono, T. Onoda,
and Y. Hayashi, “Detection of cyber attacks against voltage control in
distribution power grids with pvs,” IEEE Transactions on Smart Grid,
vol. 7, no. 4, pp. 1824–1835, 2015.
[106] X. Chen, J. Zhou, M. Shi, Y. Chen, and J. Wen, “Distributed resilient
control against denial of service attacks in dc microgrids with constant
power load,” Renewable and Sustainable Energy Reviews, vol. 153, p.
111792, 2022.
[107] N. Bhusal, M. Gautam, and M. Benidris, “Detection of cyber attacks
on voltage regulation in distribution systems using machine learning,”
IEEE Access, vol. 9, pp. 40 402–40 416, 2021.
[108] A. Teixeira, K. Paridari, H. Sandberg, and K. H. Johansson, “Voltage
control for interconnected microgrids under adversarial actions,” in
2015 IEEE 20th Conference on Emerging Technologies & Factory
Automation (ETFA).
IEEE, 2015, pp. 1–8.
[109] P. Ju and X. Lin, “Adversarial attacks to distributed voltage control in
power distribution networks with ders,” in Proceedings of the Ninth
International Conference on Future Energy Systems, 2018, pp. 291–
302.
[110] L. Langer, P. Smith, M. Hutle, and A. Schaeffer-Filho, “Analysing
cyber-physical attacks to a smart grid: A voltage control use case,” in
2016 Power Systems Computation Conference (PSCC).
IEEE, 2016,
pp. 1–7.
[111] J. Giraldo, A. C´ardenas, and N. Quijano, “Integrity attacks on real-time
pricing in smart grids: impact and countermeasures,” IEEE Transac-
tions on Smart Grid, vol. 8, no. 5, pp. 2249–2257, 2016.
[112] R. Tan, V. Badrinath Krishna, D. K. Yau, and Z. Kalbarczyk, “Impact
of integrity attacks on real-time pricing in smart grids,” in Proceedings
of the 2013 ACM SIGSAC conference on Computer & communications
security, 2013, pp. 439–450.
[113] S. Liu, S. Mashayekh, D. Kundur, T. Zourntos, and K. Butler-Purry,
“A framework for modeling cyber-physical switching attacks in smart
grid,” IEEE Transactions on Emerging Topics in Computing, vol. 1,
no. 2, pp. 273–285, 2013.
[114] S. Liu, X. Feng, D. Kundur, T. Zourntos, and K. L. Butler-Purry,
“Switched system models for coordinated cyber-physical attack con-
struction and simulation,” in 2011 IEEE First International Workshop
on Smart Grid Modeling and Simulation (SGMS).
IEEE, 2011, pp.
49–54.
[115] S. Liu, X. Feng, D. Kundur, T. Zourntos, and K. Butler-Purry, “A class
of cyber-physical switching attacks for power system disruption,” in
Proceedings of the Seventh Annual Workshop on Cyber Security and
Information Intelligence Research, 2011, pp. 1–1.
[116] S. Liu, S. Mashayekh, D. Kundur, T. Zourntos, and K. L. Butler-Purry,
“A smart grid vulnerability analysis framework for coordinated variable
structure switching attacks,” in 2012 IEEE Power and Energy Society
General Meeting.
IEEE, 2012, pp. 1–6.
[117] S. Liu, D. Kundur, T. Zourntos, and K. L. Butler-Purry, “Coordinated
variable structure switching attack in the presence of model error and
state estimation,” in 2012 IEEE Third International Conference on
Smart Grid Communications (SmartGridComm).
IEEE, 2012, pp.
318–323.
[118] G. Wu, G. Wang, J. Sun, and L. Xiong, “Optimal switching attacks
and countermeasures in cyber-physical systems,” IEEE Transactions on
Systems, Man, and Cybernetics: Systems, vol. 51, no. 8, pp. 4825–4835,
2019.
[119] L. Lee and P. Hu, “Vulnerability analysis of cascading dynamics in
smart grids under load redistribution attacks,” International Journal of
Electrical Power & Energy Systems, vol. 111, pp. 182–190, 2019.


---

Page 25

---

25
[120] Y. Xiang, Z. Ding, Y. Zhang, and L. Wang, “Power system reliability
evaluation considering load redistribution attacks,” IEEE Transactions
on Smart Grid, vol. 8, no. 2, pp. 889–901, 2016.
[121] Y. Yuan, Z. Li, and K. Ren, “Quantitative analysis of load redistri-
bution attacks in power systems,” IEEE Transactions on Parallel and
Distributed Systems, vol. 23, no. 9, pp. 1731–1738, 2012.
[122] ——, “Modeling load redistribution attacks in power systems,” IEEE
Transactions on Smart Grid, vol. 2, no. 2, pp. 382–390, 2011.
[123] N. Saxena, S. Grijalva, V. Chukwuka, and A. V. Vasilakos, “Network
security and privacy challenges in smart vehicle-to-grid,” IEEE Wireless
Communications, vol. 24, no. 4, pp. 88–98, 2017.
[124] Y. Zhang, S. Gjessing, H. Liu, H. Ning, L. T. Yang, and M. Guizani,
“Securing vehicle-to-grid communications in the smart grid,” IEEE
Wireless Communications, vol. 20, no. 6, pp. 66–73, 2013.
[125] W. Han and Y. Xiao, “Privacy preservation for v2g networks in smart
grid: A survey,” Computer Communications, vol. 91, pp. 17–28, 2016.
[126] M. Zeller, “Myth or reality—does the aurora vulnerability pose a risk
to my generator?” in 2011 64th Annual Conference for Protective Relay
Engineers.
IEEE, 2011, pp. 130–136.
[127] A. Srivastava, T. Morris, T. Ernster, C. Vellaithurai, S. Pan, and
U. Adhikari, “Modeling cyber-physical vulnerability of the smart grid
with incomplete information,” IEEE Transactions on Smart Grid,
vol. 4, no. 1, pp. 235–244, 2013.
[128] M. Zeller, “Common questions and answers addressing the aurora
vulnerability,” in DistribuTECH Conference, 2011.
[129] H. He and J. Yan, “Cyber-physical attacks and defences in the smart
grid: a survey,” IET Cyber-Physical Systems: Theory & Applications,
vol. 1, no. 1, pp. 13–27, 2016.
[130] P. Shakarian, “Stuxnet: Cyberwar revolution in military affairs,” 2011.
[131] J. P. Farwell and R. Rohozinski, “Stuxnet and the future of cyber war,”
Survival, vol. 53, no. 1, pp. 23–40, 2011.
[132] K. Zetter, Countdown to zero day: Stuxnet and the launch of the world’s
first digital weapon.
Crown, 2015.
[133] T. M. Chen, “Stuxnet, the real start of cyber warfare?[editor’s note],”
IEEE network, vol. 24, no. 6, pp. 2–3, 2010.
[134] N. Falliere, L. O. Murchu, and E. Chien, “W32. stuxnet dossier,” White
paper, symantec corp., security response, vol. 5, no. 6, p. 29, 2011.
[135] K. Hemsley and R. Fisher, “A history of cyber incidents and threats
involving industrial control systems,” in Critical Infrastructure Protec-
tion XII: 12th IFIP WG 11.10 International Conference, ICCIP 2018,
Arlington, VA, USA, March 12-14, 2018, Revised Selected Papers 12.
Springer, 2018, pp. 215–242.
[136] S. I. Response, “Dragonfly: Cyberespionage attacks against energy
suppliers,” Rapp. tecn, vol. 7, 2014.
[137] G. Wangen, “The role of malware in reported cyber espionage: a review
of the impact and mechanism,” Information, vol. 6, no. 2, pp. 183–211,
2015.
[138] D. Hentunen and A. Tikkanen, “Havex hunts for ics/scada systems,”
in F-Secure, 2014.
[139] R. M. Lee, M. Assante, and T. Conway, “Crashoverride: Analysis of
the threat to electric grid operations,” Dragos Inc., March, p. 7, 2017.
[140] J. Slowik, “Crashoverride: Reassessing the 2016 ukraine electric power
event as a protection-focused attack,” Dragos, Inc, 2019.
[141] A. Bindra, “Securing the power grid: Protecting smart grids and
connected power systems from cyberattacks,” IEEE Power Electronics
Magazine, vol. 4, no. 3, pp. 20–27, 2017.
[142] A. Greenberg, “’crash override’: The malware that took down a power
grid,” URL http://bit. ly/2raojOf, Wired Magazine, retrieved, pp. 09–20,
2017.
[143] H. Zhang, B. Liu, and H. Wu, “Smart grid cyber-physical attack and
defense: A review,” IEEE Access, vol. 9, pp. 29 641–29 659, 2021.
[144] Y. Cui, F. Bai, Y. Liu, P. L. Fuhr, and M. E. Morales-Rodriguez,
“Spatio-temporal characterization of synchrophasor data against spoof-
ing attacks in smart grids,” IEEE Transactions on Smart Grid, vol. 10,
no. 5, pp. 5807–5818, 2019.
[145] S. Liu, S. You, H. Yin, Z. Lin, Y. Liu, W. Yao, and L. Sundaresh,
“Model-free data authentication for cyber security in power systems,”
IEEE Transactions on Smart Grid, vol. 11, no. 5, pp. 4565–4568, 2020.
[146] S. East, J. Butts, M. Papa, and S. Shenoi, “A taxonomy of attacks
on the dnp3 protocol,” in Critical Infrastructure Protection III: Third
Annual IFIP WG 11.10 International Conference on Critical Infrastruc-
ture Protection, Hanover, New Hampshire, USA, March 23-25, 2009,
Revised Selected Papers 3.
Springer, 2009, pp. 67–81.
[147] I. A. Siddavatam and F. Kazi, “Security assessment framework for
cyber physical systems: A case-study of dnp3 protocol,” in 2015 IEEE
Bombay Section Symposium (IBSS).
IEEE, 2015, pp. 1–6.
[148] P. Yi, T. Zhu, Q. Zhang, Y. Wu, and L. Pan, “Puppet attack: A denial
of service attack in advanced metering infrastructure network,” Journal
of Network and Computer Applications, vol. 59, pp. 325–332, 2016.
[149] G. L. B. Jacoba and G. P. C. Genove, “Cybersecurity of smart grids:
Attacks and defenses of the smart meters in an advanced metering in-
frastructure (ami),” Southeast Asian Journal of Science and Technology,
vol. 8, no. 1, pp. 74–83, 2023.
[150] S. Besati, S. Essakiappan, and M. Manjrekar, “A new flexible modified
impedance network converter,” in 2023 IEEE Transportation Electrifi-
cation Conference & Expo (ITEC).
IEEE, 2023, pp. 1–5.
[151] J. Tian, B. Wang, T. Li, F. Shang, and K. Cao, “Coordinated cyber-
physical attacks considering dos attacks in power systems,” Interna-
tional Journal of Robust and Nonlinear Control, vol. 30, no. 11, pp.
4345–4358, 2020.
[152] S. Cui, Z. Han, S. Kar, T. T. Kim, H. V. Poor, and A. Tajer,
“Coordinated data-injection attack and detection in the smart grid: A
detailed look at enriching detection solutions,” IEEE Signal Processing
Magazine, vol. 29, no. 5, pp. 106–115, 2012.
[153] L. Arnaboldi, R. M. Czekster, C. Morisset, and R. Metere, “Modelling
load-changing attacks in cyber-physical systems,” Electronic Notes in
Theoretical Computer Science, vol. 353, pp. 39–60, 2020.
[154] A. Dabrowski, J. Ullrich, and E. R. Weippl, “Grid shock: Coordinated
load-changing attacks on power grids: The non-smart power grid is
vulnerable to cyber attacks as well,” in Proceedings of the 33rd Annual
Computer Security Applications Conference, 2017, pp. 303–314.
[155] R. Deng, P. Zhuang, and H. Liang, “Ccpa: Coordinated cyber-physical
attacks and countermeasures in smart grid,” IEEE Transactions on
Smart Grid, vol. 8, no. 5, pp. 2420–2430, 2017.
[156] J. Yan, H. He, X. Zhong, and Y. Tang, “Q-learning-based vulnerability
analysis of smart grid against sequential topology attacks,” IEEE
Transactions on Information Forensics and Security, vol. 12, no. 1,
pp. 200–210, 2016.
[157] J. Zhang and L. Sankar, “Physical system consequences of unobserv-
able state-and-topology cyber-physical attacks,” IEEE Transactions on
Smart Grid, vol. 7, no. 4, 2016.
[158] Z. Li, M. Shahidehpour, A. Alabdulwahab, and A. Abusorrah, “Bilevel
model for analyzing coordinated cyber-physical attacks on power
systems,” IEEE Transactions on Smart Grid, vol. 7, no. 5, pp. 2260–
2272, 2015.
[159] Z. Wang, H. He, Z. Wan, and Y. Sun, “Coordinated topology attacks
in smart grid using deep reinforcement learning,” IEEE Transactions
on Industrial Informatics, vol. 17, no. 2, pp. 1407–1415, 2020.
[160] Z. Li, M. Shahidehpour, A. Alabdulwahab, and A. Abusorrah, “Ana-
lyzing locally coordinated cyber-physical attacks for undetectable line
outages,” IEEE Transactions on Smart Grid, vol. 9, no. 1, pp. 35–47,
2016.
[161] D. U. Case, “Analysis of the cyber attack on the ukrainian power grid,”
Electricity Information Sharing and Analysis Center (E-ISAC), vol.
388, no. 1-29, p. 3, 2016.
[162] H.-M. Chung, W.-T. Li, C. Yuen, W.-H. Chung, Y. Zhang, and C.-
K. Wen, “Local cyber-physical attack for masking line outage and
topology attack in smart grid,” IEEE Transactions on Smart Grid,
vol. 10, no. 4, pp. 4577–4588, 2018.
[163] X. Liu, Z. Li, X. Liu, and Z. Li, “Masking transmission line outages
via false data injection attacks,” IEEE Transactions on Information
Forensics and Security, vol. 11, no. 7, pp. 1592–1602, 2016.
[164] M. Tian, M. Cui, Z. Dong, X. Wang, S. Yin, and L. Zhao, “Multilevel
programming-based coordinated cyber physical attacks and counter-
measures in smart grid,” IEEE Access, vol. 7, pp. 9836–9847, 2019.
[165] S. Soltan, M. Yannakakis, and G. Zussman, “React to cyber attacks on
power grids,” IEEE Transactions on Network Science and Engineering,
vol. 6, no. 3, pp. 459–473, 2018.
[166] S. Soltan and G. Zussman, “Expose the line failures following a cyber-
physical attack on the power grid,” IEEE Transactions on Control of
Network Systems, vol. 6, no. 1, pp. 451–461, 2018.
[167] S. Soltan, P. Mittal, and H. V. Poor, “Line failure detection after a
cyber-physical attack on the grid using bayesian regression,” IEEE
Transactions on Power Systems, vol. 34, no. 5, pp. 3758–3768, 2019.
[168] C. V. Zhou, C. Leckie, and S. Karunasekera, “A survey of coordinated
attacks and collaborative intrusion detection,” computers & security,
vol. 29, no. 1, pp. 124–140, 2010.
[169] J. Yang, P. Ning, X. S. Wang, and S. Jajodia, “Cards: A distributed
system for detecting coordinated attacks,” in Information Security
for Global Information Infrastructures: IFIP TC11 Sixteenth Annual
Working Conference on Information Security August 22–24, 2000,
Beijing, China 15.
Springer, 2000, pp. 171–180.


---

Page 26

---

26
[170]
¨O. Sen, D. van der Velde, K. A. Wehrmeister, I. Hacker, M. Henze,
and M. Andres, “Towards an approach to contextual detection of multi-
stage cyber attacks in smart grids,” in 2021 International Conference
on Smart Energy Systems and Technologies (SEST).
IEEE, 2021, pp.
1–6.
[171] K. Lai, M. Illindala, and K. Subramaniam, “A tri-level optimization
model to mitigate coordinated attacks on electric power systems in a
cyber-physical environment,” Applied energy, vol. 235, pp. 204–218,
2019.
[172] T. Alpcan and T. Basar, “A game theoretic approach to decision and
analysis in network intrusion detection,” in 42nd IEEE International
Conference on Decision and Control (IEEE Cat. No. 03CH37475),
vol. 3.
IEEE, 2003, pp. 2595–2600.
[173] X. G. Shan and J. Zhuang, “A game-theoretic approach to modeling
attacks and defenses of smart grids at three levels,” Reliability Engi-
neering & System Safety, vol. 195, p. 106683, 2020.
[174] A. A. C´ardenas, S. Amin, G. Schwartz, R. Dong, and S. Sastry, “A
game theory model for electricity theft detection and privacy-aware
control in ami systems,” in 2012 50th Annual Allerton Conference on
Communication, Control, and Computing (Allerton).
IEEE, 2012, pp.
1830–1837.
[175] M. Esmalifalak, G. Shi, Z. Han, and L. Song, “Bad data injection
attack and defense in electricity market using game theory study,” IEEE
Transactions on Smart Grid, vol. 4, no. 1, pp. 160–169, 2013.
[176] N. Nikmehr and S. Moradi Moghadam, “Game-theoretic cybersecurity
analysis for false data injection attack on networked microgrids,” IET
Cyber-Physical Systems: Theory & Applications, vol. 4, no. 4, pp. 365–
373, 2019.
[177] T. Alpcan and T. Basar, “An intrusion detection game with limited
observations,” in 12th Int. Symp. on Dynamic Games and Applications,
Sophia Antipolis, France, vol. 26, 2006.
[178] S. Lakshminarayana, E. V. Belmega, and H. V. Poor, “Moving-target
defense against cyber-physical attacks in power grids via game theory,”
IEEE Transactions on Smart Grid, vol. 12, no. 6, pp. 5244–5257, 2021.
[179] Z. Zhang, J. Hu, J. Lu, J. Cao, and F. E. Alsaadi, “Preventing false
data injection attacks in lfc system via the attack-detection evolutionary
game model and kf algorithm,” IEEE Transactions on Network Science
and Engineering, vol. 9, no. 6, pp. 4349–4362, 2022.
[180] Z. Abou El Houda, B. Brik, A. Ksentini, L. Khoukhi, and M. Guizani,
“When federated learning meets game theory: A cooperative framework
to secure iiot applications on edge computing,” IEEE Transactions on
Industrial Informatics, vol. 18, no. 11, pp. 7988–7997, 2022.
[181] H. Wu, W. Wang, C. Wen, and Z. Li, “Game theoretical security
detection strategy for networked systems,” Information Sciences, vol.
453, pp. 346–363, 2018.
[182] S. Rass, S. K¨onig, and S. Schauer, “Defending against advanced
persistent threats using game-theory,” PloS one, vol. 12, no. 1, p.
e0168675, 2017.
[183] M. V. De Assis, A. H. Hamamoto, T. Abr˜ao, and M. L. Proenc¸a, “A
game theoretical based system using holt-winters and genetic algorithm
with fuzzy logic for dos/ddos mitigation on sdn networks,” IEEE
Access, vol. 5, pp. 9485–9496, 2017.
[184] K. Chung, C. A. Kamhoua, K. A. Kwiat, Z. T. Kalbarczyk, and R. K.
Iyer, “Game theory with learning for cyber security monitoring,” in
2016 IEEE 17th International Symposium on High Assurance Systems
Engineering (HASE).
IEEE, 2016, pp. 1–8.
[185] L. Xiao, D. Xu, N. B. Mandayam, and H. V. Poor, “Attacker-centric
view of a detection game against advanced persistent threats,” IEEE
transactions on mobile computing, vol. 17, no. 11, pp. 2512–2523,
2018.
[186] W. Saad, Z. Han, H. V. Poor, and T. Basar, “Game-theoretic methods
for the smart grid: An overview of microgrid systems, demand-side
management, and smart grid communications,” IEEE Signal Processing
Magazine, vol. 29, no. 5, pp. 86–105, 2012.
[187] S. Roy, C. Ellis, S. Shiva, D. Dasgupta, V. Shandilya, and Q. Wu, “A
survey of game theory as applied to network security,” in 2010 43rd
Hawaii International Conference on System Sciences.
IEEE, 2010,
pp. 1–10.
[188] Z. M. Fadlullah, Y. Nozaki, A. Takeuchi, and N. Kato, “A survey of
game theoretic approaches in smart grid,” in 2011 International Con-
ference on Wireless Communications and Signal Processing (WCSP).
IEEE, 2011, pp. 1–4.
[189] Y. Park and S. Kim, “Game theory-based bi-level pricing scheme for
smart grid scheduling control algorithm,” Journal of Communications
and Networks, vol. 18, no. 3, pp. 484–492, 2016.
[190] M. N. A. Khalid, A. A. Al-Kadhimi, and M. M. Singh, “Recent
developments in game-theory approaches for the detection and defense
against advanced persistent threats (apts): A systematic review,” Math-
ematics, vol. 11, no. 6, p. 1353, 2023.
[191] M. Zhu, A. H. Anwar, Z. Wan, J.-H. Cho, C. A. Kamhoua, and
M. P. Singh, “A survey of defensive deception: Approaches using
game theory and machine learning,” IEEE Communications Surveys
& Tutorials, vol. 23, no. 4, pp. 2460–2493, 2021.
[192] R. Jiang, R. Lu, Y. Wang, J. Luo, C. Shen, and X. Shen, “Energy-theft
detection issues for advanced metering infrastructure in smart grid,”
Tsinghua Science and Technology, vol. 19, no. 2, pp. 105–120, 2014.
[193] K. G. Vamvoudakis, J. P. Hespanha, B. Sinopoli, and Y. Mo, “Detection
in adversarial environments,” IEEE Transactions on Automatic Control,
vol. 59, no. 12, pp. 3209–3223, 2014.
[194] C. Y. Ma, D. K. Yau, and N. S. Rao, “Scalable solutions of markov
games for smart-grid infrastructure protection,” IEEE Transactions on
Smart Grid, vol. 4, no. 1, pp. 47–55, 2013.
[195] Z. Mingqiang, H. Hui, and W. Qian, “A graph-based clustering al-
gorithm for anomaly intrusion detection,” in 2012 7th International
Conference on Computer Science & Education (ICCSE).
IEEE, 2012,
pp. 1311–1314.
[196] L. Wang, S. Noel, and S. Jajodia, “Minimum-cost network hardening
using attack graphs,” Computer Communications, vol. 29, no. 18, pp.
3812–3824, 2006.
[197] E. Drayer and T. Routtenberg, “Detection of false data injection
attacks in smart grids based on graph signal processing,” IEEE Systems
Journal, vol. 14, no. 2, pp. 1886–1896, 2019.
[198] M. Jorjani, H. Seifi, and A. Y. Varjani, “A graph theory-based approach
to detect false data injection attacks in power system ac state estima-
tion,” IEEE Transactions on Industrial Informatics, vol. 17, no. 4, pp.
2465–2475, 2020.
[199] J. R. Johnson and E. A. Hogan, “A graph analytic metric for mitigating
advanced persistent threat,” in 2013 IEEE International Conference on
Intelligence and Security Informatics.
IEEE, 2013, pp. 129–133.
[200] L. Cai, Z. Chen, C. Luo, J. Gui, J. Ni, D. Li, and H. Chen, “Structural
temporal graph neural networks for anomaly detection in dynamic
graphs,” in Proceedings of the 30th ACM international conference on
Information & Knowledge Management, 2021, pp. 3747–3756.
[201] M. Doostmohammadian, H. Zarrabi, H. R. Rabiee, U. A. Khan, and
T. Charalambous, “Distributed detection and mitigation of biasing
attacks over multi-agent networks,” IEEE Transactions on Network
Science and Engineering, vol. 8, no. 4, pp. 3465–3477, 2021.
[202] K. Durkota, V. Lis`y, B. Boˇsansk`y, C. Kiekintveld, and M. Pˇechouˇcek,
“Hardening networks against strategic attackers using attack graph
games,” Computers & Security, vol. 87, p. 101578, 2019.
[203] Y. Cao, H. Jiang, Y. Deng, J. Wu, P. Zhou, and W. Luo, “Detect-
ing and mitigating ddos attacks in sdn using spatial-temporal graph
convolutional network,” IEEE Transactions on Dependable and Secure
Computing, vol. 19, no. 6, pp. 3855–3872, 2021.
[204] E. Purvine, J. R. Johnson, and C. Lo, “A graph-based impact metric
for mitigating lateral movement cyber attacks,” in Proceedings of the
2016 ACM Workshop on Automated Decision Making for Active Cyber
Defense, 2016, pp. 45–52.
[205] E. Gelenbe, P. Fr¨ohlich, M. Nowak, S. Papadopoulos, A. Protogerou,
A. Drosou, and D. Tzovaras, “Iot network attack detection and mitiga-
tion,” in 2020 9th Mediterranean Conference on Embedded Computing
(MECO).
IEEE, 2020, pp. 1–6.
[206] R. Diestel, A. Schrijver, and P. Seymour, “Graph theory,” Oberwolfach
Reports, vol. 7, no. 1, pp. 521–580, 2010.
[207] S. Staniford-Chen, S. Cheung, R. Crawford, M. Dilger, J. Frank,
J. Hoagland, K. Levitt, C. Wee, R. Yip, and D. Zerkle, “Grids-a graph
based intrusion detection system for large networks,” in Proceedings
of the 19th national information systems security conference, vol. 1.
Citeseer, 1996, pp. 361–370.
[208] P. Ammann, D. Wijesekera, and S. Kaushik, “Scalable, graph-based
network vulnerability analysis,” in Proceedings of the 9th ACM Confer-
ence on Computer and Communications Security, 2002, pp. 217–224.
[209] S. Jha, O. Sheyner, and J. Wing, “Two formal analyses of attack
graphs,” in Proceedings 15th IEEE Computer Security Foundations
Workshop. CSFW-15.
IEEE, 2002, pp. 49–63.
[210] C. Phillips and L. P. Swiler, “A graph-based system for network-
vulnerability analysis,” in Proceedings of the 1998 workshop on New
security paradigms, 1998, pp. 71–79.
[211] L. P. Swiler, C. Phillips, D. Ellis, and S. Chakerian, “Computer-
attack graph generation tool,” in Proceedings DARPA Information
Survivability Conference and Exposition II. DISCEX’01, vol. 2. IEEE,
2001, pp. 307–321.


---

Page 27

---

27
[212] S. Noel, S. Jajodia, B. O’Berry, and M. Jacobs, “Efficient minimum-
cost network hardening via exploit dependency graphs,” in 19th An-
nual Computer Security Applications Conference, 2003. Proceedings.
IEEE, 2003, pp. 86–95.
[213] O. Kosut, L. Jia, R. J. Thomas, and L. Tong, “Malicious data attacks
on the smart grid,” IEEE Transactions on Smart Grid, vol. 2, no. 4,
pp. 645–658, 2011.
[214] D. Kundur, X. Feng, S. Liu, T. Zourntos, and K. L. Butler-Purry,
“Towards a framework for cyber attack impact analysis of the electric
smart grid,” in 2010 First IEEE international conference on smart grid
communications.
IEEE, 2010, pp. 244–249.
[215] T. Pourhabibi, K.-L. Ong, B. H. Kam, and Y. L. Boo, “Fraud detec-
tion: A systematic literature review of graph-based anomaly detection
approaches,” Decision Support Systems, vol. 133, p. 113303, 2020.
[216] W. Wang and Z. Lu, “Cyber security in the smart grid: Survey and
challenges,” Computer networks, vol. 57, no. 5, pp. 1344–1371, 2013.
[217] L. Akoglu, H. Tong, and D. Koutra, “Graph based anomaly detection
and description: a survey,” Data mining and knowledge discovery,
vol. 29, pp. 626–688, 2015.
[218] S. Ranshous, S. Shen, D. Koutra, S. Harenberg, C. Faloutsos, and N. F.
Samatova, “Anomaly detection in dynamic networks: a survey,” Wiley
Interdisciplinary Reviews: Computational Statistics, vol. 7, no. 3, pp.
223–247, 2015.
[219] J. Yanmei, L. Mingsheng, L. Yangyang, L. Yaping, Z. Jingyun,
L. Yifeng, and L. Chunyang, “Enhanced neighborhood node graph
neural networks for load forecasting in smart grid,” International
Journal of Machine Learning and Cybernetics, vol. 15, no. 1, pp. 129–
148, 2024.
[220] S. Nakamoto, “Bitcoin: A peer-to-peer electronic cash system,” Decen-
tralized business review, p. 21260, 2008.
[221] P. Zhuang, T. Zamir, and H. Liang, “Blockchain for cybersecurity in
smart grid: A comprehensive survey,” IEEE Transactions on Industrial
Informatics, vol. 17, no. 1, pp. 3–19, 2020.
[222] T. Winter, “The advantages and challenges of the blockchain for smart
grids,” 2018.
[223] L. Yue, H. Junqin, Q. Shengzhi, and W. Ruijin, “Big data model
of security sharing based on blockchain,” in 2017 3rd International
Conference on Big Data Computing and Communications (BIGCOM).
IEEE, 2017, pp. 117–121.
[224] M. Mylrea and S. N. G. Gourisetti, “Blockchain for smart grid
resilience: Exchanging distributed energy at speed, scale and security,”
in 2017 Resilience Week (RWS).
IEEE, 2017, pp. 18–23.
[225] M. N. Kurt, Y. Yılmaz, and X. Wang, “Secure distributed dynamic state
estimation in wide-area smart grids,” IEEE Transactions on Information
Forensics and Security, vol. 15, pp. 800–815, 2019.
[226] E. Mengelkamp, B. Notheisen, C. Beer, D. Dauer, and C. Weinhardt,
“A blockchain-based smart grid: towards sustainable local energy
markets,” Computer Science-Research and Development, vol. 33, pp.
207–214, 2018.
[227] B. Rodrigues, L. Eisenring, E. Scheid, T. Bocek, and B. Stiller, “Eval-
uating a blockchain-based cooperative defense,” in 2019 IFIP/IEEE
Symposium on Integrated Network and Service Management (IM).
IEEE, 2019, pp. 533–538.
[228] N. Kolokotronis, S. Brotsis, G. Germanos, C. Vassilakis, and S. Shiae-
les, “On blockchain architectures for trust-based collaborative intrusion
detection,” in 2019 IEEE world congress on services (SERVICES), vol.
2642.
IEEE, 2019, pp. 21–28.
[229] D. Sivaganesan, “A data driven trust mechanism based on blockchain
in iot sensor networks for detection and mitigation of attacks,” Journal
of trends in Computer Science and Smart technology (TCSST), vol. 3,
no. 01, pp. 59–69, 2021.
[230] M. Ghiasi, M. Dehghani, T. Niknam, A. Kavousi-Fard, P. Siano, and
H. H. Alhelou, “Cyber-attack detection and cyber-security enhancement
in smart dc-microgrid based on blockchain technology and hilbert
huang transform,” Ieee Access, vol. 9, pp. 29 429–29 440, 2021.
[231] P. Zhang, D. C. Schmidt, J. White, and A. Dubey, “Consensus mecha-
nisms and information security technologies,” Advances in Computers,
vol. 115, pp. 181–209, 2019.
[232] A. S. Musleh, G. Yao, and S. Muyeen, “Blockchain applications in
smart grid–review and frameworks,” Ieee Access, vol. 7, pp. 86 746–
86 757, 2019.
[233] M. B. Mollah, J. Zhao, D. Niyato, K.-Y. Lam, X. Zhang, A. M.
Ghias, L. H. Koh, and L. Yang, “Blockchain for future smart grid:
A comprehensive survey,” IEEE Internet of Things Journal, vol. 8,
no. 1, pp. 18–43, 2020.
[234] A. Bani-Ahmed, M. Rashidi, A. Nasiri, and H. Hosseini, “Reliabil-
ity analysis of a decentralized microgrid control architecture,” IEEE
Transactions on Smart Grid, vol. 10, no. 4, pp. 3910–3918, 2018.
[235] E. Mengelkamp, J. G¨arttner, K. Rock, S. Kessler, L. Orsini, and
C. Weinhardt, “Designing microgrid energy markets: A case study: The
brooklyn microgrid,” Applied energy, vol. 210, pp. 870–880, 2018.
[236] L. Orsini, S. Kessler, J. Wei, and H. Field, “How the brooklyn microgrid
and transactive grid are paving the way to next-gen energy markets,”
in The energy internet.
Elsevier, 2019, pp. 223–239.
[237] P. Koukaras, K. D. Afentoulis, P. A. Gkaidatzis, A. Mystakidis,
D. Ioannidis, S. I. Vagropoulos, and C. Tjortjis, “Integrating blockchain
in smart grids for enhanced demand response: Challenges, strategies,
and future directions,” Energies, vol. 17, no. 5, p. 1007, 2024.
[238] K. Croman, C. Decker, I. Eyal, A. E. Gencer, A. Juels, A. Kosba,
A. Miller, P. Saxena, E. Shi, E. G¨un Sirer et al., “On scaling decentral-
ized blockchains: (a position paper),” in Financial Cryptography and
Data Security: FC 2016 International Workshops, BITCOIN, VOTING,
and WAHC, Christ Church, Barbados, February 26, 2016, Revised
Selected Papers 20.
Springer, 2016, pp. 106–125.
[239] A. A. Monrat, O. Schel´en, and K. Andersson, “A survey of blockchain
from the perspectives of applications, challenges, and opportunities,”
IEEE Access, vol. 7, pp. 117 134–117 151, 2019.
[240] A. A. G. Agung and R. Handayani, “Blockchain for smart grid,”
Journal of King Saud University-Computer and Information Sciences,
vol. 34, no. 3, pp. 666–675, 2022.
[241] H. Vranken, “Sustainability of bitcoin and blockchains,” Current opin-
ion in environmental sustainability, vol. 28, pp. 1–9, 2017.
[242] A. Reyna, C. Mart´ın, J. Chen, E. Soler, and M. D´ıaz, “On blockchain
and its integration with iot. challenges and opportunities,” Future
generation computer systems, vol. 88, pp. 173–190, 2018.
[243] M. Ozay, I. Esnaola, F. T. Y. Vural, S. R. Kulkarni, and H. V. Poor,
“Machine learning methods for attack detection in the smart grid,”
IEEE transactions on neural networks and learning systems, vol. 27,
no. 8, pp. 1773–1786, 2015.
[244] S. Azad, F. Sabrina, and S. Wasimi, “Transformation of smart grid
using machine learning,” in 2019 29th Australasian Universities Power
Engineering Conference (AUPEC).
IEEE, 2019, pp. 1–6.
[245] J. Yan, B. Tang, and H. He, “Detection of false data attacks in smart
grid with supervised learning,” in 2016 International Joint Conference
on Neural Networks (IJCNN).
IEEE, 2016, pp. 1395–1402.
[246] M. Esmalifalak, L. Liu, N. Nguyen, R. Zheng, and Z. Han, “Detecting
stealthy false data injection using machine learning in smart grid,” IEEE
Systems Journal, vol. 11, no. 3, pp. 1644–1652, 2014.
[247] J. Sakhnini, H. Karimipour, and A. Dehghantanha, “Smart grid cyber
attacks detection using supervised learning and heuristic feature selec-
tion,” in 2019 IEEE 7th international conference on smart energy grid
engineering (SEGE).
IEEE, 2019, pp. 108–112.
[248] S. Ahmed, Y. Lee, S.-H. Hyun, and I. Koo, “Feature selection–based
detection of covert cyber deception assaults in smart grid communi-
cations networks using machine learning,” IEEE Access, vol. 6, pp.
27 518–27 529, 2018.
[249] P. I. Radoglou-Grammatikis and P. G. Sarigiannidis, “An anomaly-
based intrusion detection system for the smart grid based on cart de-
cision tree,” in 2018 global information infrastructure and networking
symposium (GIIS).
IEEE, 2018, pp. 1–5.
[250] N. Boumkheld, M. Ghogho, and M. El Koutbi, “Intrusion detection
system for the detection of blackhole attacks in a smart grid,” in
2016 4th International Symposium on Computational and Business
Intelligence (ISCBI).
IEEE, 2016, pp. 108–111.
[251] S.-C. Yip, K. Wong, W.-P. Hew, M.-T. Gan, R. C.-W. Phan, and S.-
W. Tan, “Detection of energy theft and defective smart meters in smart
grids using linear regression,” International Journal of Electrical Power
& Energy Systems, vol. 91, pp. 230–240, 2017.
[252] Y. Huang and Q. Xu, “Electricity theft detection based on stacked
sparse denoising autoencoder,” International Journal of Electrical
Power & Energy Systems, vol. 125, p. 106448, 2021.
[253] D. Xue, X. Jing, and H. Liu, “Detection of false data injection attacks in
smart grid utilizing elm-based ocon framework,” IEEE Access, vol. 7,
pp. 31 762–31 773, 2019.
[254] Y. Li, R. Qiu, and S. Jing, “Intrusion detection system using online
sequence extreme learning machine (os-elm) in advanced metering
infrastructure of smart grid,” PloS one, vol. 13, no. 2, p. e0192216,
2018.
[255] L. Yang, Y. Li, and Z. Li, “Improved-elm method for detecting false
data attack in smart grid,” International Journal of Electrical Power &
Energy Systems, vol. 91, pp. 183–191, 2017.


---

Page 28

---

28
[256] V. Ford, A. Siraj, and W. Eberle, “Smart grid energy fraud detection
using artificial neural networks,” in 2014 IEEE symposium on compu-
tational intelligence applications in smart grid (CIASG).
IEEE, 2014,
pp. 1–6.
[257] A. Ayad, H. E. Farag, A. Youssef, and E. F. El-Saadany, “Detection
of false data injection attacks in smart grids using recurrent neural
networks,” in 2018 IEEE power & energy society innovative smart
grid technologies conference (ISGT).
IEEE, 2018, pp. 1–5.
[258] X. Niu, J. Li, J. Sun, and K. Tomsovic, “Dynamic detection of false data
injection attack in smart grid using deep learning,” in 2019 IEEE Power
& Energy Society Innovative Smart Grid Technologies Conference
(ISGT).
IEEE, 2019, pp. 1–6.
[259] S. H. Haghshenas, M. A. Hasnat, and M. Naeini, “A temporal graph
neural network for cyber attack detection and localization in smart
grids,” in 2023 IEEE Power & Energy Society Innovative Smart Grid
Technologies Conference (ISGT).
IEEE, 2023, pp. 1–5.
[260] A. Takiddin, R. Atat, M. Ismail, O. Boyaci, K. R. Davis, and E. Ser-
pedin, “Generalized graph neural network-based detection of false
data injection attacks in smart grids,” IEEE Transactions on Emerging
Topics in Computational Intelligence, 2023.
[261] H. Karimipour, A. Dehghantanha, R. M. Parizi, K.-K. R. Choo, and
H. Leung, “A deep and scalable unsupervised machine learning system
for cyber-attack detection in large-scale smart grids,” IEEE Access,
vol. 7, pp. 80 778–80 788, 2019.
[262] L. Wei, D. Gao, and C. Luo, “False data injection attacks detection
with deep belief networks in smart grid,” in 2018 Chinese Automation
Congress (CAC).
IEEE, 2018, pp. 2621–2625.
[263] J. Chen, S. Sathe, C. Aggarwal, and D. Turaga, “Outlier detection
with autoencoder ensembles,” in Proceedings of the 2017 SIAM inter-
national conference on data mining.
SIAM, 2017, pp. 90–98.
[264] J. Meira, R. Andrade, I. Prac¸a, J. Carneiro, V. Bol´on-Canedo,
A. Alonso-Betanzos, and G. Marreiros, “Performance evaluation of
unsupervised techniques in cyber-attack anomaly detection,” Journal
of Ambient Intelligence and Humanized Computing, vol. 11, pp. 4477–
4489, 2020.
[265] R. Bhatia, S. Benno, J. Esteban, T. Lakshman, and J. Grogan, “Unsuper-
vised machine learning for network-centric anomaly detection in iot,”
in Proceedings of the 3rd acm conext workshop on big data, machine
learning and artificial intelligence for data communication networks,
2019, pp. 42–48.
[266] H. Xu, W. Chen, N. Zhao, Z. Li, J. Bu, Z. Li, Y. Liu, Y. Zhao, D. Pei,
Y. Feng et al., “Unsupervised anomaly detection via variational auto-
encoder for seasonal kpis in web applications,” in Proceedings of the
2018 world wide web conference, 2018, pp. 187–196.
[267] P. Casas, J. Mazel, and P. Owezarski, “Unsupervised network intru-
sion detection systems: Detecting the unknown without knowledge,”
Computer Communications, vol. 35, no. 7, pp. 772–783, 2012.
[268] R. Bhaumik, B. Mobasher, and R. Burke, “A clustering approach to
unsupervised attack detection in collaborative recommender systems,”
in Proceedings of the International Conference on Data Science
(ICDATA).
Citeseer, 2011, p. 1.
[269] G. Pu, L. Wang, J. Shen, and F. Dong, “A hybrid unsupervised
clustering-based anomaly detection method,” Tsinghua Science and
Technology, vol. 26, no. 2, pp. 146–153, 2020.
[270] S. Jiang, X. Song, H. Wang, J.-J. Han, and Q.-H. Li, “A clustering-
based method for unsupervised intrusion detections,” Pattern Recogni-
tion Letters, vol. 27, no. 7, pp. 802–810, 2006.
[271] I. Syarif, A. Prugel-Bennett, and G. Wills, “Unsupervised clustering
approach for network anomaly detection,” in Networked Digital Tech-
nologies: 4th International Conference, NDT 2012, Dubai, UAE, April
24-26, 2012. Proceedings, Part I 4.
Springer, 2012, pp. 135–145.
[272] A. Patcha and J.-M. Park, “An overview of anomaly detection tech-
niques: Existing solutions and latest technological trends,” Computer
networks, vol. 51, no. 12, pp. 3448–3470, 2007.
[273] S. Ahmed, Y. Lee, S.-H. Hyun, and I. Koo, “Unsupervised machine
learning-based detection of covert data integrity assault in smart grid
networks utilizing isolation forest,” IEEE Transactions on Information
Forensics and Security, vol. 14, no. 10, pp. 2765–2777, 2019.
[274] A. Valdes, R. Macwan, and M. Backes, “Anomaly detection in electrical
substation circuits via unsupervised machine learning,” in 2016 IEEE
17th international conference on information reuse and integration
(IRI).
IEEE, 2016, pp. 500–505.
[275] M. Aamir and S. M. A. Zaidi, “Clustering based semi-supervised
machine learning for ddos attack classification,” Journal of King Saud
University-Computer and Information Sciences, vol. 33, no. 4, pp. 436–
446, 2021.
[276] J. Haweliya and B. Nigam, “Network intrusion detection using semi
supervised support vector machine,” International Journal of Computer
Applications, vol. 85, no. 9, 2014.
[277] Y. Zhang, J. Wang, and B. Chen, “Detecting false data injection attacks
in smart grids: A semi-supervised deep learning approach,” IEEE
Transactions on Smart Grid, vol. 12, no. 1, pp. 623–634, 2020.
[278] M. Farajzadeh-Zanjani, E. Hallaji, R. Razavi-Far, M. Saif, and M. Par-
vania, “Adversarial semi-supervised learning for diagnosing faults and
attacks in power grids,” IEEE Transactions on Smart Grid, vol. 12,
no. 4, pp. 3468–3478, 2021.
[279] M. Abdel-Basset, H. Hawash, R. K. Chakrabortty, and M. J. Ryan,
“Semi-supervised spatiotemporal deep learning for intrusions detection
in iot networks,” IEEE Internet of Things Journal, vol. 8, no. 15, pp.
12 251–12 265, 2021.
[280] A. Dairi, F. Harrou, B. Bouyeddou, S.-M. Senouci, and Y. Sun, “Semi-
supervised deep learning-driven anomaly detection schemes for cyber-
attack detection in smart grids,” in Power Systems Cybersecurity:
Methods, Concepts, and Best Practices.
Springer, 2023, pp. 265–295.
[281] Z. Li, W. Chen, Z. Wei, X. Luo, and B. Su, “Semi-wtc: A practical
semi-supervised framework for attack categorization through weight-
task consistency,” arXiv preprint arXiv:2205.09669, 2022.
[282] S. Rathore and J. H. Park, “Semi-supervised learning based distributed
attack detection framework for iot,” Applied Soft Computing, vol. 72,
pp. 79–89, 2018.
[283] R. Qi, C. Rasband, J. Zheng, and R. Longoria, “Semi-supervised outlier
detection and deep feature extraction for detecting cyber-attacks in
smart grids using pmu data,” in 17th International Conference on
Information Technology–New Generations (ITNG 2020).
Sprdies-
tel2010graphinger, 2020, pp. 509–515.
[284] I. Triguero, S. Garc´ıa, and F. Herrera, “Self-labeled techniques for
semi-supervised learning: taxonomy, software and empirical study,”
Knowledge and Information systems, vol. 42, pp. 245–284, 2015.
[285] Y. Zhang and J. Yan, “Semi-supervised domain-adversarial training
for intrusion detection against false data injection in the smart grid,”
in 2020 international joint conference on neural networks (IJCNN).
IEEE, 2020, pp. 1–7.
[286] R. Polikar, “Ensemble learning,” Ensemble machine learning: Methods
and applications, pp. 1–34, 2012.
[287] B. A. Tama and S. Lim, “Ensemble learning for intrusion detection
systems: A systematic mapping study and cross-benchmark evaluation,”
Computer Science Review, vol. 39, p. 100357, 2021.
[288] A. A. Aburomman and M. B. I. Reaz, “A survey of intrusion detection
systems based on ensemble and hybrid classifiers,” Computers &
security, vol. 65, pp. 135–152, 2017.
[289] I. Syarif, E. Zaluska, A. Prugel-Bennett, and G. Wills, “Application
of bagging, boosting and stacking to intrusion detection,” in Machine
Learning and Data Mining in Pattern Recognition: 8th International
Conference, MLDM 2012, Berlin, Germany, July 13-20, 2012. Pro-
ceedings 8.
Springer, 2012, pp. 593–602.
[290] M. Ashrafuzzaman, S. Das, Y. Chakhchoukh, S. Shiva, and F. T.
Sheldon, “Detecting stealthy false data injection attacks in the smart
grid using ensemble-based machine learning,” Computers & Security,
vol. 97, p. 101994, 2020.
[291] D. Gaikwad and R. C. Thool, “Intrusion detection system using bagging
ensemble method of machine learning,” in 2015 international confer-
ence on computing communication control and automation.
IEEE,
2015, pp. 291–295.
[292] X. Chen, L. Zhang, Y. Liu, and C. Tang, “Ensemble learning methods
for power system cyber-attack detection,” in 2018 IEEE 3rd Inter-
national Conference on Cloud Computing and Big Data Analysis
(ICCCBDA).
IEEE, 2018, pp. 613–616.
[293] J. Cao, D. Wang, Z. Qu, M. Cui, P. Xu, K. Xue, and K. Hu, “A novel
false data injection attack detection model of the cyber-physical power
system,” IEEE Access, vol. 8, pp. 95 109–95 125, 2020.
[294] T. T. Khoei, G. Aissou, W. C. Hu, and N. Kaabouch, “Ensemble
learning methods for anomaly intrusion detection system in smart
grid,” in 2021 IEEE international conference on electro information
technology (EIT).
IEEE, 2021, pp. 129–135.
[295] M. Rashid, J. Kamruzzaman, T. Imam, S. Wibowo, and S. Gordon,
“A tree-based stacking ensemble technique with feature selection for
network intrusion detection,” Applied Intelligence, vol. 52, no. 9, pp.
9768–9781, 2022.
[296] S. Rajagopal, P. P. Kundapur, and K. S. Hareesha, “A stacking ensemble
for network intrusion detection using heterogeneous datasets,” Security
and Communication Networks, vol. 2020, pp. 1–9, 2020.


---

Page 29

---

29
[297] M. R. C. Acosta, S. Ahmed, C. E. Garcia, and I. Koo, “Extremely
randomized trees-based scheme for stealthy cyber-attack detection in
smart grid networks,” IEEE access, vol. 8, pp. 19 921–19 933, 2020.
[298] C. Hazman, A. Guezzaz, S. Benkirane, and M. Azrour, “lids-sioel:
intrusion detection framework for iot-based smart environments secu-
rity using ensemble learning,” Cluster Computing, vol. 26, no. 6, pp.
4069–4083, 2023.
[299] I. Elgarhy, M. M. Badr, M. Mahmoud, M. M. Fouda, M. Alsabaan, and
H. A. Kholidy, “Clustering and ensemble based approach for securing
electricity theft detectors against evasion attacks,” IEEE Access, 2023.
[300] A. Starke, K. Nagaraj, C. Ruben, N. Aljohani, S. Zou, A. Bretas, J. Mc-
Nair, and A. Zare, “Cross-layered distributed data-driven framework for
enhanced smart grid cyber-physical security,” IET Smart Grid, vol. 5,
no. 6, pp. 398–416, 2022.
[301] C. Hu, J. Yan, and X. Liu, “Adaptive feature boosting of multi-sourced
deep autoencoders for smart grid intrusion detection,” in 2020 IEEE
Power & Energy Society General Meeting (PESGM).
IEEE, 2020,
pp. 1–5.
[302] O. Sagi and L. Rokach, “Ensemble learning: A survey,” Wiley Inter-
disciplinary Reviews: Data Mining and Knowledge Discovery, vol. 8,
no. 4, p. e1249, 2018.
[303] L. I. Kuncheva, Combining pattern classifiers: methods and algorithms.
John Wiley & Sons, 2014.
[304] R. S. Sutton and A. G. Barto, Reinforcement learning: An introduction.
MIT press, 2018.
[305] A. T. El-Toukhy, M. M. Badr, M. Mahmoud, G. Srivastava, M. M.
Fouda, and M. Alsabaan, “Electricity theft detection using deep rein-
forcement learning in smart power grids,” IEEE Access, 2023.
[306] M. N. Kurt, O. Ogundijo, C. Li, and X. Wang, “Online cyber-attack
detection in smart grid: A reinforcement learning approach,” IEEE
Transactions on Smart Grid, vol. 10, no. 5, pp. 5174–5185, 2018.
[307] V. Mnih, K. Kavukcuoglu, D. Silver, A. A. Rusu, J. Veness, M. G.
Bellemare, A. Graves, M. Riedmiller, A. K. Fidjeland, G. Ostrovski
et al., “Human-level control through deep reinforcement learning,”
nature, vol. 518, no. 7540, pp. 529–533, 2015.
[308] D. An, Q. Yang, W. Liu, and Y. Zhang, “Defending against data
integrity attacks in smart grid: A deep reinforcement learning-based
approach,” IEEE Access, vol. 7, pp. 110 835–110 845, 2019.
[309] Y. Li and J. Wu, “Low latency cyberattack detection in smart grids
with deep reinforcement learning,” International Journal of Electrical
Power & Energy Systems, vol. 142, p. 108265, 2022.
[310] D. An, F. Zhang, Q. Yang, and C. Zhang, “Data integrity attack in
dynamic state estimation of smart grid: Attack model and countermea-
sures,” IEEE Transactions on Automation Science and Engineering,
vol. 19, no. 3, pp. 1631–1644, 2022.
[311] R. Huang, Y. Li, and X. Wang, “Attention-aware deep reinforcement
learning for detecting false data injection attacks in smart grids,”
International Journal of Electrical Power & Energy Systems, vol. 147,
p. 108815, 2023.
[312] V. Konda and J. Tsitsiklis, “Actor-critic algorithms,” Advances in neural
information processing systems, vol. 12, 1999.
[313] M. Feng and H. Xu, “Deep reinforecement learning based optimal
defense for cyber-physical system in presence of unknown cyber-
attack,” in 2017 IEEE Symposium Series on Computational Intelligence
(SSCI).
IEEE, 2017, pp. 1–8.
[314] T. P. Lillicrap, J. J. Hunt, A. Pritzel, N. Heess, T. Erez, Y. Tassa,
D. Silver, and D. Wierstra, “Continuous control with deep reinforce-
ment learning,” arXiv preprint arXiv:1509.02971, 2015.
[315] A. J. Abianeh, Y. Wan, F. Ferdowsi, N. Mijatovic, and T. Dragiˇcevi´c,
“Vulnerability identification and remediation of fdi attacks in islanded
dc microgrids using multiagent reinforcement learning,” IEEE Trans-
actions on Power Electronics, vol. 37, no. 6, pp. 6359–6370, 2021.
[316] S. Yu, “Fast detection of advanced persistent threats for smart grids:
A deep reinforcement learning approach,” in ICC 2022-IEEE Interna-
tional Conference on Communications.
IEEE, 2022, pp. 2676–2681.
[317] M. I. Jordan and T. M. Mitchell, “Machine learning: Trends, perspec-
tives, and prospects,” Science, vol. 349, no. 6245, pp. 255–260, 2015.
[318] M. Khan and L. Ghafoor, “Adversarial machine learning in the context
of network security: Challenges and solutions,” Journal of Computa-
tional Intelligence and Robotics, vol. 4, no. 1, pp. 51–63, 2024.
[319] J. Wireman, F. Koleini, and N. Tabrizi, “A comparison of public
sentiment on covid-19 vaccines on twitter and reddit: An analysis using
vader,” in 2023 Congress in Computer Science, Computer Engineering,
& Applied Computing (CSCE).
IEEE, 2023, pp. 1242–1246.
[320] H. R. Kappali, K. Sadyojatha, and S. Prashanthi, “Computer vision and
machine learning in paddy diseases identification and classification: A
review.” Indian Journal Of Agricultural Research, vol. 58, no. 2, 2024.
[321] K. G. Liakos, P. Busato, D. Moshou, S. Pearson, and D. Bochtis,
“Machine learning in agriculture: A review,” Sensors, vol. 18, no. 8,
p. 2674, 2018.
[322] E. A. Movahed, F. Koleini, and N. Tabrizi, “Tensor decompositions in
cancer study; a comprehensive,” in Proceedings of 36th International
Conference on, vol. 97, 2024, pp. 101–113.
[323] H. B. McMahan, E. Moore, D. Ramage, S. Hampson, and B. A.
y Arcas, “Communication-efficient learning of deep networks from de-
centralized data,” in International Conference on Artificial Intelligence
and Statistics, 2016.
[324] X. Lian, W. Zhang, C. Zhang, and J. Liu, “Asynchronous decentralized
parallel stochastic gradient descent,” ArXiv, vol. abs/1710.06952, 2017.
[325] N. Rashvand, K. Witham, G. Maldonado, V. Katariya, A. Sultan,
G. Schirner, and H. Tabkhi, “Distributed learning for automatic modula-
tion recognition in bandwidth-limited networks,” in Signal Processing,
Sensor/Information Fusion, and Target Recognition XXXIII, vol. 13057.
SPIE, 2024, pp. 345–357.
[326] P. Gholami and H. Seferoglu, “Digest: Fast and communication effi-
cient decentralized learning with local updates,” IEEE Transactions on
Machine Learning in Communications and Networking, 2024.
[327] E. Bagdasaryan, A. Veit, Y. Hua, D. Estrin, and V. Shmatikov, “How
to backdoor federated learning,” in Proceedings of the Twenty Third
International Conference on Artificial Intelligence and Statistics, ser.
Proceedings of Machine Learning Research, S. Chiappa and R. Calan-
dra, Eds., vol. 108.
PMLR, 26–28 Aug 2020, pp. 2938–2948.
[328] V. Mothukuri, R. M. Parizi, S. Pouriyeh, Y. ping Huang, A. Dehghan-
tanha, and G. Srivastava, “A survey on security and privacy of federated
learning,” Future Gener. Comput. Syst., vol. 115, pp. 619–640, 2021.
[329] P. Gholami and H. Seferoglu, “Fast and communication efficient
decentralized learning with local updates,” in Federated Learning
and Analytics in Practice: Algorithms, Systems, Applications, and
Opportunities, 2023.
[330] ——, “Improved generalization bounds for communication efficient
federated learning,” arXiv preprint arXiv:2404.11754, 2024.
[331] S. Gholami, J. I. Lim, T. Leng, S. S. Y. Ong, A. C. Thompson, and
M. N. Alam, “Federated learning for diagnosis of age-related macular
degeneration,” Frontiers in Medicine, vol. 10, 2023.
[332] V. Tolpegin, S. Truex, M. E. Gursoy, and L. Liu, “Data poisoning
attacks against federated learning systems,” in European Symposium
on Research in Computer Security, 2020.
[333] W. He, W. Liu, C. Wen, and Q. Yang, “Detection of false data injection
attacks on smart grids based on a-bitg approach,” Electronics, vol. 13,
no. 10, p. 1938, 2024.
[334] V. Chandola, A. Banerjee, and V. Kumar, “Anomaly detection: A
survey,” ACM computing surveys (CSUR), vol. 41, no. 3, pp. 1–58,
2009.
[335] L. Breiman, “Bagging predictors,” Machine learning, vol. 24, pp. 123–
140, 1996.
[336] P. Bartlett, Y. Freund, W. S. Lee, and R. E. Schapire, “Boosting the
margin: A new explanation for the effectiveness of voting methods,”
The annals of statistics, vol. 26, no. 5, pp. 1651–1686, 1998.
[337] D. H. Wolpert, “Stacked generalization,” Neural networks, vol. 5, no. 2,
pp. 241–259, 1992.
[338] R. S. Sutton, A. G. Barto et al., Introduction to reinforcement learning.
MIT press Cambridge, 1998, vol. 135.
[339] C. J. Watkins and P. Dayan, “Q-learning,” Machine learning, vol. 8,
pp. 279–292, 1992.
[340] J. Wang, Y. Gao, and R. Li, “Reinforcement learning based bilevel real-
time pricing strategy for a smart grid with distributed energy resources,”
Applied Soft Computing, vol. 155, p. 111474, 2024.
[341] M. Sharif and H. Seker, “Smart ev charging with context-awareness:
Enhancing resource utilization via deep reinforcement learning,” IEEE
Access, 2024.
[342] J. Achiam, S. Adler, S. Agarwal, L. Ahmad, I. Akkaya, F. L. Aleman,
D. Almeida, J. Altenschmidt, S. Altman, S. Anadkat et al., “Gpt-4
technical report,” arXiv preprint arXiv:2303.08774, 2023.
[343] M. Reid, N. Savinov, D. Teplyashin, D. Lepikhin, T. Lillicrap, J.-b.
Alayrac, R. Soricut, A. Lazaridou, O. Firat, J. Schrittwieser et al.,
“Gemini 1.5: Unlocking multimodal understanding across millions of
tokens of context,” arXiv preprint arXiv:2403.05530, 2024.
[344] A. Zaboli, S. L. Choi, T.-J. Song, and J. Hong, “Chatgpt and other
large language models for cybersecurity of smart grid applications,”
arXiv preprint arXiv:2311.05462, 2023.
[345] M. Guastalla, Y. Li, A. Hekmati, and B. Krishnamachari, “Application
of large language models to ddos attack detection,” in International
Conference on Security and Privacy in Cyber-Physical Systems and
Smart Vehicles.
Springer, 2023, pp. 83–99.


---

Page 30

---

30
[346] M. Gupta, C. Akiri, K. Aryal, E. Parker, and L. Praharaj, “From chatgpt
to threatgpt: Impact of generative ai in cybersecurity and privacy,” IEEE
Access, 2023.
[347] S. Hussain, A. Iqbal, S. S. Hussain, S. Zanero, A. Shikfa, E. Ragaini,
I. Khan, and R. Alammari, “A novel hybrid methodology to secure
goose messages against cyberattacks in smart grids,” Scientific reports,
vol. 13, no. 1, p. 1857, 2023.
[348] S. Biderman, U. PRASHANTH, L. Sutawika, H. Schoelkopf, Q. An-
thony, S. Purohit, and E. Raff, “Emergent and predictable memorization
in large language models,” Advances in Neural Information Processing
Systems, vol. 36, 2024.
[349] S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y. Cao,
“React: Synergizing reasoning and acting in language models,” arXiv
preprint arXiv:2210.03629, 2022.
[350] J. Li, Y. Yang, and J. Sun, “Risks of practicing large language
models in smart grid: Threat modeling and validation,” arXiv preprint
arXiv:2405.06237, 2024.
[351] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal,
A. Neelakantan, P. Shyam, G. Sastry, A. Askell et al., “Language mod-
els are few-shot learners,” Advances in neural information processing
systems, vol. 33, pp. 1877–1901, 2020.
[352] I. J. Goodfellow, J. Shlens, and C. Szegedy, “Explaining and harnessing
adversarial examples,” arXiv preprint arXiv:1412.6572, 2014.
[353] L. Mu˜noz-Gonz´alez, B. Biggio, A. Demontis, A. Paudice, V. Wongras-
samee, E. C. Lupu, and F. Roli, “Towards poisoning of deep learning
algorithms with back-gradient optimization,” in Proceedings of the 10th
ACM workshop on artificial intelligence and security, 2017, pp. 27–38.
[354] A. Shafahi, W. R. Huang, M. Najibi, O. Suciu, C. Studer, T. Dumitras,
and T. Goldstein, “Poison frogs! targeted clean-label poisoning attacks
on neural networks,” Advances in neural information processing sys-
tems, vol. 31, 2018.
[355] B. Flowers, R. M. Buehrer, and W. C. Headley, “Evaluating adversarial
evasion attacks in the context of wireless communications,” IEEE
Transactions on Information Forensics and Security, vol. 15, pp. 1102–
1113, 2019.
[356] F. Zhang, P. P. Chan, B. Biggio, D. S. Yeung, and F. Roli, “Adver-
sarial feature selection against evasion attacks,” IEEE transactions on
cybernetics, vol. 46, no. 3, pp. 766–777, 2015.
[357] B. Biggio, I. Corona, D. Maiorca, B. Nelson, N. ˇSrndi´c, P. Laskov,
G. Giacinto, and F. Roli, “Evasion attacks against machine learning
at test time,” in Machine Learning and Knowledge Discovery in
Databases: European Conference, ECML PKDD 2013, Prague, Czech
Republic, September 23-27, 2013, Proceedings, Part III 13.
Springer,
2013, pp. 387–402.
[358] M. Zhou, X. Gao, J. Wu, K. Liu, H. Sun, and L. Li, “Investigat-
ing white-box attacks for on-device models,” in Proceedings of the
IEEE/ACM 46th International Conference on Software Engineering,
2024, pp. 1–12.
[359] K. Roshan, A. Zafar, and S. B. U. Haque, “Untargeted white-box adver-
sarial attack with heuristic defence methods in real-time deep learning
based network intrusion detection system,” Computer Communications,
vol. 218, pp. 97–113, 2024.
[360] N. I. Mahbub, M. D. Hossain, S. Akhter, M. I. Hossain, K. Jeong,
and E.-N. Huh, “Robustness of workload forecasting models in cloud
data centers: A white-box adversarial attack perspective,” IEEE Access,
2024.
[361] J. Jo, J. Kim, and Y.-J. Suh, “Exploring public data vulnerabilities in
semi-supervised learning models through gray-box adversarial attack,”
Electronics, vol. 13, no. 5, p. 940, 2024.
[362] G. Apruzzese and V. Subrahmanian, “Mitigating adversarial gray-box
attacks against phishing detectors,” IEEE Transactions on Dependable
and Secure Computing, 2022.
[363] Z. Wang, M. Gao, J. Li, J. Zhang, and J. Zhong, “Gray-box shilling
attack: an adversarial learning approach,” ACM Transactions on Intel-
ligent Systems and Technology (TIST), vol. 13, no. 5, pp. 1–21, 2022.
[364] N. Papernot, P. McDaniel, I. Goodfellow, S. Jha, Z. B. Celik, and
A. Swami, “Practical black-box attacks against machine learning,” in
Proceedings of the 2017 ACM on Asia conference on computer and
communications security, 2017, pp. 506–519.
[365] F. Suya, A. Suri, T. Zhang, J. Hong, Y. Tian, and D. Evans, “Sok:
Pitfalls in evaluating black-box attacks,” in 2024 IEEE Conference on
Secure and Trustworthy Machine Learning (SaTML). IEEE, 2024, pp.
387–407.
[366] R. Liu, W. Zhou, T. Zhang, K. Chen, J. Zhao, and K.-Y. Lam, “Boosting
black-box attack to deep neural networks with conditional diffusion
models,” IEEE Transactions on Information Forensics and Security,
2024.
[367] P.-Y. Chen, H. Zhang, Y. Sharma, J. Yi, and C.-J. Hsieh, “Zoo: Zeroth
order optimization based black-box attacks to deep neural networks
without training substitute models,” in Proceedings of the 10th ACM
workshop on artificial intelligence and security, 2017, pp. 15–26.
[368] W. Zhou, X. Hou, Y. Chen, M. Tang, X. Huang, X. Gan, and
Y. Yang, “Transferable adversarial perturbations,” in Proceedings of the
European Conference on Computer Vision (ECCV), 2018, pp. 452–467.
[369] Y. Dong, F. Liao, T. Pang, H. Su, J. Zhu, X. Hu, and J. Li, “Boosting
adversarial attacks with momentum,” in Proceedings of the IEEE
conference on computer vision and pattern recognition, 2018, pp.
9185–9193.
[370] S. Thomas, F. Koleini, and N. Tabrizi, “Dynamic defenses and the
transferability of adversarial examples,” in 2022 IEEE 4th International
Conference on Trust, Privacy and Security in Intelligent Systems, and
Applications (TPS-ISA).
IEEE, 2022, pp. 276–284.
[371] A. Ilyas, L. Engstrom, A. Athalye, and J. Lin, “Black-box adversarial
attacks with limited queries and information,” in International confer-
ence on machine learning.
PMLR, 2018, pp. 2137–2146.
[372] W. He, J. Wei, X. Chen, N. Carlini, and D. Song, “Adversarial example
defense: Ensembles of weak defenses are not strong,” in 11th USENIX
workshop on offensive technologies (WOOT 17), 2017.
[373] B. Hitaj, G. Ateniese, and F. Perez-Cruz, “Deep models under the gan:
information leakage from collaborative deep learning,” in Proceedings
of the 2017 ACM SIGSAC conference on computer and communications
security, 2017, pp. 603–618.
[374] N. Papernot, P. McDaniel, S. Jha, M. Fredrikson, Z. B. Celik, and
A. Swami, “The limitations of deep learning in adversarial settings,” in
2016 IEEE European symposium on security and privacy (EuroS&P).
IEEE, 2016, pp. 372–387.
[375] N. Carlini and D. Wagner, “Towards evaluating the robustness of neural
networks,” in 2017 ieee symposium on security and privacy (sp). Ieee,
2017, pp. 39–57.
[376] A. Madry, A. Makelov, L. Schmidt, D. Tsipras, and A. Vladu, “Towards
deep learning models resistant to adversarial attacks,” arXiv preprint
arXiv:1706.06083, 2017.
[377] N. Papernot, P. McDaniel, X. Wu, S. Jha, and A. Swami, “Distillation
as a defense to adversarial perturbations against deep neural networks,”
in 2016 IEEE symposium on security and privacy (SP).
IEEE, 2016,
pp. 582–597.
[378] N. Carlini and D. Wagner, “Magnet and” efficient defenses against
adversarial attacks” are not robust to adversarial examples,” arXiv
preprint arXiv:1711.08478, 2017.
[379] J. Buckman, A. Roy, C. Raffel, and I. Goodfellow, “Thermometer
encoding: One hot way to resist adversarial examples,” in International
conference on learning representations, 2018.
[380] Y. Zhou, M. Kantarcioglu, and B. Xi, “A survey of game theoretic
approach for adversarial machine learning,” Wiley Interdisciplinary
Reviews: Data Mining and Knowledge Discovery, vol. 9, no. 3, p.
e1259, 2019.
[381] P. Dasgupta and J. Collins, “A survey of game theoretic approaches
for adversarial machine learning in cybersecurity tasks,” AI Magazine,
vol. 40, no. 2, pp. 31–43, 2019.
[382] M.-M. Z¨uhlke and D. Kudenko, “Adversarial robustness of neural
networks from the perspective of lipschitz calculus: A survey,” ACM
Computing Surveys, 2024.
[383] Y. Zhao, T. Pang, C. Du, X. Yang, C. Li, N.-M. M. Cheung, and
M. Lin, “On evaluating adversarial robustness of large vision-language
models,” Advances in Neural Information Processing Systems, vol. 36,
2024.
[384] X. Yuan, P. He, Q. Zhu, and X. Li, “Adversarial examples: Attacks and
defenses for deep learning,” IEEE transactions on neural networks and
learning systems, vol. 30, no. 9, pp. 2805–2824, 2019.
[385] R. R. Wiyatno, A. Xu, O. Dia, and A. De Berker, “Adversarial
examples in modern machine learning: A review,” arXiv preprint
arXiv:1911.05268, 2019.
[386] I. Ilahi, M. Usama, J. Qadir, M. U. Janjua, A. Al-Fuqaha, D. T. Hoang,
and D. Niyato, “Challenges and countermeasures for adversarial attacks
on deep reinforcement learning,” IEEE Transactions on Artificial
Intelligence, vol. 3, no. 2, pp. 90–109, 2021.
