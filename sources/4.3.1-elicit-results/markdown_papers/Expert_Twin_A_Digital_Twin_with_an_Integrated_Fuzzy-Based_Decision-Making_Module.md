

---

Page 1

---

 
Decision Making: Applications in Management and Engineering, Volume 8, Issue 1 (2025) 1-21 
 
1 
 
 
Decision Making: Applications in 
Management and Engineering 
Journal homepage: www.dmame-journal.org 
ISSN: 2560-6018, eISSN: 2620-0104 
 
Expert Twin: A Digital Twin with an Integrated Fuzzy-Based Decision-
Making Module 
 
Gergő Dávid Monek1, Szabolcs Fischer1,* 
 
1 
Central Campus Győr, Széchenyi István University, Győr, Hungary 
 
ARTICLE INFO 
ABSTRACT 
Article history: 
Received 5 April 2024 
Received in revised form 19 May 2024 
Accepted 7 June 2024 
Available online 29 June 2024 
Digitalization and the application of modern Industry 4.0 solutions are 
becoming increasingly important to remain competitive as product ranges 
expand and global supply chains grow. This paper presents a new Digital Twin 
framework to achieve robustness in manufacturing process optimization and 
enhance the efficiency of decision support. Most digital twins in the literature 
synchronously represent the real system without any control elements 
despite the bidirectional data link. The proposed approach combines the 
advantages 
of 
traditional 
process 
simulations 
with 
a 
real-time 
communication and data acquisition method using programmable logic 
controllers designed to control automated systems. In addition, it 
complements this by utilizing human experience and expertise in modeling 
using Fuzzy Logic to create a control-enabled digital twin system. The 
resulting "Expert Twin" system reduces the reaction time of the production to 
unexpected events and increases the efficiency of decision support; it 
generates and selects alternatives, therefore creating smart manufacturing. 
The Expert Twin framework was integrated, tested, and validated on an 
automated production sample system in a laboratory environment. In the 
experimental scenarios carried out, the method production increased 
production line utility by up to 28% and the number of re-schedules can be 
halved. 
 
Keywords: 
Expert Twin (ET); Digital Twin (DT); Fuzzy 
Logic (FL); Manufacturing Simulation; 
Intelligence layer; Cyber-Physical Systems 
(CPSs), Decision-Making Support 
 
 
1. Introduction 
Manufacturing systems undergo significant transformations due to Industry 4.0 (I4.0) [1,2] and 
the increasing digitization of the sector. (These industries can be considered the automotive and 
machine manufacturing [3–5], railway industry [6–8], mining [9], etc.) This evolution is driven by 
global competitiveness, necessitating manufacturers to respond quickly and adaptively to diverse 
and rapidly changing consumer demands. These dynamics introduce higher complexity and reduce 
the available time for decision-making (DM) within the manufacturing framework, thus demanding 
the application of intelligent and innovative technologies. The various make-to-order manufacturing 
strategies, such as Just in Time (JIT) and Just in Sequence (JIS), necessitate an accurate estimation of 
lead times (LTs) to ensure efficient and optimized utilization of resources. Additionally, reliable 
 
* Corresponding author. 
E-mail address: fischersz@sze.hu 
 
https://doi.org/10.31181/dmame8120251181    


---

Page 2

---

Decision Making: Applications in Management and Engineering 
Volume 8, Issue 1 (2025) 1-21 
2 
 
 
system load and performance forecasting are crucial for pricing bids on manufacturing deadlines and 
production management decisions. Given the challenging nature of LT estimation, there is a pressing 
need for new and improved methodologies that consider a broader and more precise range of system 
parameters influencing LTs, leveraging the extensive dataset made available by digitalization. While 
Discrete Event Simulation (DES) is a well-established and long-employed method in corporate 
environments for predicting future system states, it proves particularly time-consuming and costly 
for Small and Medium Industries (SMIs) due to the essential input information and logic descriptions 
needed for model construction. Furthermore, the continual maintenance and updating of traditional 
simulation models impose significant tasks on the employing company [10]. 
A digital twin (DT) represents a digital model of a physical asset, where the complexity of the DT 
– whether real-time or predictive – depends on its specific application. DTs can model various levels 
of system behavior and complexity tailored to user needs and can be utilized throughout all stages 
of the product lifecycle, from prototyping to production. In the context of manufacturing, the 
deployment of DTs and CPS (Cyber-Physical System) [11,12] in a production environment is referred 
to as a Cyber-Physical Production System (CPPS). The digitization of the shop floor has led to more 
accurate and timely information flow, enhancing reporting times, reducing errors, and increasing 
process planning flexibility. The concept of the DT has garnered considerable applications such as 
machine fault prediction, structural optimization design, and intelligent management and control. 
The DT employs sophisticated digital techniques to construct high-fidelity representations of physical 
entities and to simulate their characteristics and behaviors within a virtual environment. This 
innovation offers a novel approach to overcoming existing challenges in job shop production and 
enhancing production management and control. Modern production processes require integration 
between factory floor automation and Enterprise Resource Planning (ERP) systems, with the 
Manufacturing Execution System (MES) serving as the intermediary to manage production lines 
aligned with business strategies. The MES enhances situational awareness of the production process, 
and a CPPS plays a critical role in real-time DM support and predictive planning, thereby reducing 
unnecessary operational costs [13,14]. 
A fundamental element of CPS is Machine to Machine (M2M) communication, which 
encompasses any interaction between machines, controllers, and actuators across wired and 
wireless networks. M2M is integrated into the Internet of Things (IoT) networks, supported by various 
commercial and open-source communication protocols designed for manufacturing. OPC-Unified 
Architecture (OPC-UA) is a flexible implementation protocol across a broader range of industrial 
automation applications. In the context of CPS, the challenge lies in utilizing available data to enhance 
productivity, predict system responses, and minimize downtime. Real-time data from programmable 
logic controllers (PLC) and RFID (Radio-frequency identification) or NFC (Near Field Communication) 
tags on production pallets are crucial sources for updating both the MES and the DT. Tags facilitate 
the automatic identification and tracking of products throughout production phases, enhancing the 
accuracy of the MES updates through M2M communications [13]. 
A robustly constructed DT facilitates the iterative enhancement of production planning and 
process control by integrating and synthesizing all constituent elements and data. Furthermore, the 
DT employs a virtual model as a dynamic benchmark for detecting disturbances and provides a 
broader array of information for scheduling decisions. This approach potentially fosters a more 
efficient scheduling paradigm compared to conventional simulation-based scheduling and 
optimization methods.  
Nevertheless, it is critical to highlight that while an increasing volume of data can be integrated 
into the DT system through automatic updates of model parameters using information transmitted 


---

Page 3

---

Decision Making: Applications in Management and Engineering 
Volume 8, Issue 1 (2025) 1-21 
3 
 
 
from Programmable Logic Controllers (PLCs) overseeing automated systems and data from 
Manufacturing Execution Systems (MES) or ERP systems, the incorporation of human expertise and 
DM logic remains crucial. This paper introduces a so-called Expert Twin (ET) framework, a type of DT 
developed from user interactions with the observed system, which is enhanced by a DM module 
employing fuzzy logic (FL). 
The paper is organized as follows. Section 2 presents the foundational concepts of DT and DES, 
examining their potential applications within industrial contexts and discussing the integration of DM 
support into a DT simulation framework, concluding by clearly articulating the research aims. Section 
3 introduces a novel DT paradigm termed the expert twin with bilateral communication capabilities 
utilizing the OPC-UA protocol. This section also describes the execution of DT via DES modeling, 
coupled with a DM module developed using MATLAB that employs FL. Section 4 presents a case study 
conducted in the Cyber-Physical Manufacturing System Laboratory at Széchenyi István University. 
The final section offers concluding remarks contextualizing the study's contributions within a broader 
scholarly framework. 
 
2. Related Works 
Recent studies collectively signal an accelerating trend in adopting DT technology, spurred by its 
ability to merge and analyze large datasets, significantly elevating operational efficiencies and 
predictive capacities across various sectors. Despite the persisting challenges in data integration and 
system complexity, the prospective advantages of DT technology for catalyzing innovative solutions 
and achieving operational excellence are considerable. 
Luo et al., [15] extensively review how Industry 4.0 technologies, including the IoT, cloud 
manufacturing, blockchain, and big data analytics, reshape production planning. Their study details 
the transition towards DT frameworks integrating these advanced technologies with production 
planning systems, facilitating real-time, data-driven DM. The paper thoroughly evaluates the benefits 
and applications of each technology within production planning, emphasizing their contributions to 
enhancing adaptability and efficiency in manufacturing operations. It also offers critical insights into 
future research trajectories, underscoring the necessity for data-driven models capable of managing 
uncertainties and responding dynamically to changes in manufacturing environments. 
Turner and Garn [16] investigate advancements in DES for human-centric manufacturing, 
emphasizing the integration of human-in-the-loop methodologies, extended reality (XR), and DTs. 
Their findings suggest significant DM and operational efficiency enhancements through dynamic, 
interactive simulation models. The study highlights the critical role of advanced DES in adapting to 
and predicting changes in manufacturing environments, aided by advanced data integration and 
machine learning. 
Liu et al., [17] provide a systematic review of DT technologies, focusing on integrating physical 
entities, virtual models, and twin data in various applications. The paper clarifies the relationship 
between DTs and cyber-physical systems, providing comprehensive insights into the functionalities 
and applications of DTs in industries such as manufacturing; it discusses the role of DTs in bridging 
the physical and virtual worlds, enhancing simulation, prediction, and operational management. 
Tao et al., [18] explore the advancements and challenges of DTs in industrial applications, 
particularly emphasizing the pitfalls and obstacles hindering their broader implementation. While 
beneficial in synchronizing physical and virtual systems for improved monitoring and DM, they note 
that DTs face significant challenges due to overly simplistic or overly complex models, inadequate 
data interactions, and underused artificial intelligence. These issues often lead to inefficiencies in 
model accuracy, data handling, and real-time system interactions, compromising the potential 


---

Page 4

---

Decision Making: Applications in Management and Engineering 
Volume 8, Issue 1 (2025) 1-21 
4 
 
 
benefits of DT technologies in industrial settings. The authors call for a balanced approach to model 
complexity and improved data integration strategies. 
Ladj et al., [19] focus on improving data and knowledge management in the machining industry 
through a knowledge-based Digital Shadow (DS) within a DT framework. This approach merges real-
time data, expert knowledge, and machine learning, showing significant operational improvements 
in the aeronautics machining industry by enabling precise predictions and effective system 
management. 
Dos Santos et al., [20] present a systematic literature review on applying simulation as DTs in 
decision support systems for productive processes, focusing on DES and Agent-Based Simulation 
(ABS). The review highlights the growing integration of simulation models with physical systems, 
enhancing their real-time operational alignment and contributing to developing advanced DTs. This 
evolution is part of a broader trend towards intelligent, automated systems, especially within 
Industry 4.0 contexts. Challenges identified include the necessity for ongoing model validation and 
integrating diverse model types to provide robust decision support. Furthermore, the review 
identifies significant research opportunities in improving the scalability and accessibility of DT 
technologies. 
 
2.1 Literature review on DES-based DTs 
This collection of studies highlights the pivotal role of DT technology in enhancing manufacturing 
processes through integrating Industry 4.0 technologies. These research efforts explore various 
applications of DTs, from improving operational efficiency in railway axle production to implementing 
dynamic scheduling in perfume manufacturing. The studies collectively demonstrate how DTs 
facilitate advanced DM, efficiency, and adaptability across diverse industrial settings, underscoring 
their significant impact on manufacturing operations. 
Ricondo et al., [21] introduce a DT framework that enhances manufacturing DM and efficiency by 
integrating simulation models and optimization engines. Highlighting the convergence of Industry 4.0 
technologies, the framework facilitates advanced, data-driven manufacturing operations. Applied to 
railway axle production, it demonstrates significant improvements in operational efficiency and 
adaptability to dynamic production demands. 
The article by Resman et al., [22] introduces a five-step methodology for developing data-driven 
DTs in manufacturing systems. The study presents a framework for aligning digital models with actual 
manufacturing processes to enhance control and optimization. It describes how DTs can adapt to 
their physical counterparts via ongoing data exchange, enabling real-time operational adjustments. 
This method was validated through a case study, illustrating its practical implementation in managing 
DTs within industrial settings. The results underscore the potential of digital systems to improve the 
efficiency and flexibility of manufacturing operations. 
Eyring et al., [23] assess the efficacy of a closed-loop DT employing DES within a smart 
manufacturing context. The study performs three principal evaluations, throughput and bottlenecks, 
supplier quality, and process alignments, to gauge the performance of the closed-loop system. 
Results indicate that integrated with live data, the DES models significantly enhance short-term 
predictive accuracy and swiftly adapt to system changes. Specifically, the throughput and bottleneck 
analysis show a 35% improvement in predictive precision and a nearly 50% reduction in error 
compared to models using historical data. The supplier quality evaluation reveals the model's quick 
adaptation to new material variances from historical distributions. The process alignment analysis 
confirms the model's effectiveness in proactively predicting and responding to potential system 
failures, minimizing downtime and waste. 


---

Page 5

---

Decision Making: Applications in Management and Engineering 
Volume 8, Issue 1 (2025) 1-21 
5 
 
 
Onaji et al., [24] conducted a detailed analysis of DT technology integration within manufacturing 
systems, illustrated through three case studies. These case studies demonstrate DTs' diverse 
applications and benefits in improving manufacturing processes. The results indicate that DTs 
substantially enhance system monitoring, control, and process optimization. Integrating real-time 
data within DTs promotes a dynamic and adaptable manufacturing environment, improving resource 
efficiency, product quality, and operational flexibility. The case studies, drawn from different sectors, 
underscore the versatility of DTs in adapting to and optimizing various manufacturing contexts, 
confirming their pivotal role in advancing Industry 4.0 initiatives. 
Tliba et al., [25] investigate implementing a DT-driven dynamic scheduling system in a hybrid flow 
shop within the perfume manufacturing industry. Their findings demonstrate that integrating DT 
technologies with optimization and simulation techniques markedly improves scheduling flexibility 
and responsiveness. This strategy effectively addresses real-time production disturbances, including 
urgent order arrivals or operational timing changes, ensuring the robustness and adaptability of the 
scheduling system to various changes. The results validate the practical utility of DTs in enhancing 
the agility and efficiency of manufacturing operations, aiding industries in navigating the complexities 
of contemporary production environments. 
Negri et al., [26] investigate the integration of DT frameworks with manufacturing execution 
systems (MES) under the umbrella of Industry 4.0, targeting improved DM and system 
responsiveness. The study introduces two frameworks designed to manage error states and facilitate 
disassembly processes related to quality issues. The MES-integrated DTs are shown to enhance 
production efficiency. Specifically, DT-driven error management significantly reduces downtime, and 
the disassembly framework proactively corrects assembly quality failures, preventing the progression 
of flawed production. These developments lead to greater operational efficiency and fewer 
interruptions, highlighting the value of DT integration in MES contexts. 
Monek and Fischer [27] proposed a solution to enhance synchronization between physical and 
digital layers in manufacturing by using discrete-event-driven simulations for more precise DT 
environments. The system updates a real-time DT by integrating cheap microcontrollers and sensors 
with standard programmable logic controllers, accurately tracking products throughout production. 
This environment offers a practical testing ground for digital-twin solutions, enabling efficient 
simulation-driven process optimization. Monek and Fischer [28] developed a modular DT framework 
for real-time monitoring and optimization of manufacturing processes with minimal components. 
Integrated with IIoT (Industrial Internet of Things), it facilitates fault detection, reduces data 
collection efforts, and supports model reusability, ultimately enhancing sustainability. 
 
2.2 Literature review on Decision support DTs 
The compilation of research studies explores the innovative applications of DT technology and FL 
methods to enhance DM processes in various manufacturing settings. By integrating real-time data, 
predictive analytics, and fuzzy systems (FSs), these studies address dynamic management of 
manufacturing processes, resource allocation optimization, and system reliability and responsiveness 
improvement. The emphasis on decision support systems employing DTs and FL showcases their 
potential to revolutionize manufacturing workflows, enhance operational flexibility, and enable real-
time adaptive responses to changing market conditions and production demands. 
The study by Yu et al., [29] investigates the application of DT technology in job shop scheduling, 
focusing on enhancing manufacturing efficiency. The technology integrates real-time data and 
predictive analytics to enable dynamic management of manufacturing processes, thereby improving 


---

Page 6

---

Decision Making: Applications in Management and Engineering 
Volume 8, Issue 1 (2025) 1-21 
6 
 
 
scheduling and resource utilization. The research highlights the potential of DTs to transform 
manufacturing workflows. 
Villalonga et al., [30] present a novel DM framework for dynamic scheduling in cyber-physical 
production systems, focusing on leveraging multiple DTs to optimize production schedules in real-
time. This framework enables decentralized, data-driven DM using FL and condition-based 
monitoring to predict equipment status and dynamically adjust production schedules. 
Mo et al., [31] devised a robust framework employing DTs and modular artificial intelligence for 
reconfiguring manufacturing systems. This innovative methodology enables dynamic adjustments to 
manufacturing systems' layout and operational parameters in response to variable market demands. 
The framework leverages knowledge graphs for DM and optimizes systems within an integrated 
simulation environment. Its efficacy was validated in a real-world application, which achieved a 10% 
improvement in process time, demonstrating significant enhancements in responsiveness and 
productivity within manufacturing contexts. 
Francalanza et al., [32] seek the challenges faced by manufacturing system designers in 
incorporating evolving product ranges. The study introduces an FL-based approach to assist designers 
in determining the changeability level of manufacturing systems. This approach employs an 
experimental intelligent ICT tool to support the creation adaptable manufacturing systems designed 
to accommodate future product developments. The experimental implementation underscores the 
importance of flexible and reconfigurable systems in effectively responding to unpredictable market 
demands and customer requirements. 
Saraeian and Shirazi [33] analyze a DT-based fault tolerance strategy to improve reliability in 
CPPS, with a specific focus on the food production industry. The study employs Fault Tree Analyzer 
(FTA), Zero-suppressed Decision Diagram (ZDD), and Support Vector Machine-Adaptive Neuro-Fuzzy 
Inference System (SVM-ANFIS) to predict and manage faults effectively. This approach proactively 
prevents failures by identifying reliable fault signatures, thus enhancing production reliability and 
reducing downtime. The findings indicate that the DT-based CPPS maintains optimal operation 
consistently, demonstrating the method's potential to boost system reliability significantly. 
Wang et al., [34] explore the use of DTs for real-time resource allocation in the shipbuilding 
industry, specifically for hull parts picking and processing. The study documents a notable 
improvement in workstation utilization rates, with an increase of 17.39% and a decrease in the 
standard deviation of utilization by 83.31%. This enhancement is attributed to the sophisticated real-
time task allocation and scheduling capabilities afforded by DT technology, which enables precise 
and efficient resource distribution and optimizes workstation operation throughout the production 
cycle. The findings corroborate the efficacy of DTs in boosting operational efficiency and resource 
management in complex manufacturing environments. 
Tulasiraman et al., [35] evaluate FL-enabled Autonomous IoT Systems (FLAIS) for proactive 
industrial maintenance. Their simulations demonstrate that FLAIS predicts equipment failures and 
advises maintenance strategies effectively, improving reliability and reducing costs. The system 
performs best under low uncertainty, with reduced effectiveness in high uncertainty environments, 
suggesting areas for improvement. This research highlights FLAIS's potential to enhance industrial 
efficiency within Industry 4.0 by leveraging real-time IoT data and FL. 
Glatt et al., [36] research implementing and validating a DT for material flow systems within a 
cyber-physical production environment, emphasizing the simulation of physical interactions in 
material handling systems. Their research demonstrates that incorporating a physics engine to 
simulate material flows markedly diminishes risks associated with handling disturbances, such as 
accidents and reduced throughput. Through scenario simulation, the DT predicts and mitigates 


---

Page 7

---

Decision Making: Applications in Management and Engineering 
Volume 8, Issue 1 (2025) 1-21 
7 
 
 
potential disruptions, enhancing safety and efficiency in material handling. The applied use case 
shows that these capabilities significantly enhance system responsiveness and cost-effectiveness by 
proactively optimizing operational parameters for safety and productivity. 
 
2.3 Research Gap 
Following the general overview, this section of the research aimed to identify research gaps by 
examining specific case studies and implementations. The outcomes of this analytical assessment are 
summarized in Table 1. Articles were collected according to two main metrics: publications between 
2020 and 2023 with a high citation count, indicating a significant impact within the field. The 
evaluation of these articles was conducted using a meticulously defined set of six criteria: 
• Detailed components: this criterion examines the extent to which the studies address the 
physical and digital complexities. 
• Communication: it evaluates the interconnectivity between physical and digital systems 
through established communication protocols. 
• DES involvement: this involves defining the extent to which DES is integrated into the DT. 
• FL implementation: this criterion examines whether FL is employed within the DT 
framework to facilitate DM processes. 
• DT utilization: it considers the objectives behind the development of the DT and its 
practical applications. 
• Validation methodology: this assesses the techniques or tools utilized for validating the 
developed DT. 
 
A comprehensive review of the studies underscores the necessity for enhanced research and 
development to augment the operational management of cyber-physical production systems. The 
analysis indicates that the full potential of the Industry 4.0 paradigm, particularly regarding DTs, could 
be more effectively realized by establishing a well-defined framework that integrates DTs within a 
DM support architecture. It is evident from the research that projects deploying DTs predominantly 
utilize DES-based systems, with OPC-UA emerging as a commonly employed M2M communication 
protocol. 
The review focused on the objectives of DTs and the application of FL in supporting DM processes. 
As delineated in Table 1, many publications incorporate these techniques concurrently, highlighting 
a significant interest in the synergistic application of these technologies. Nevertheless, two primary 
research gaps have been identified. The first concerns the scarcity of frameworks that not only 
propose theoretical models but also demonstrate their practical applications and validations. 
Furthermore, there is inadequate discussion regarding the requirements of the physical systems, the 
integration of real and virtual systems, and the options for action and control. The second identified 
gap pertains to the limited consideration given to factors influencing the performance of the 
observed systems, which are typically informed by human expertise and experience. For instance, 
the anticipation of resource reduction due to unforeseen failures or insights regarding unstocked yet 
received items remains underexplored. 
This paper aims to design and implement a DT to enhance DM in error handling and scheduling 
tasks within Cyber-Physical Production Systems. Additionally, this research includes a proof-of-
concept and validation to assess the DT framework's ability to manage industrial complexities 
dynamically. A significant innovation introduced in this paper is the ET framework—a DT variant 
enhanced by FL-based decision modules developed through user interactions with the system. This 
approach aims to integrate a higher volume of data from PLCs, MES, and ERP systems while 


---

Page 8

---

Decision Making: Applications in Management and Engineering 
Volume 8, Issue 1 (2025) 1-21 
8 
 
 
preserving the critical role of human DM expertise. This potentially creates a more efficient 
scheduling paradigm compared to traditional methods, as the DT serves as a dynamic reference 
model to detect disturbances and enrich scheduling decisions with extensive data integration. 
The proposed ET framework, enhanced by integrating expert rule sets and alternatives proposed 
by DES models, presents an adaptable and user-friendly solution. This framework is designed to 
streamline the technological requirements for DT creation by minimizing the required software tools. 
Consequently, it offers an accessible solution for small and medium-sized enterprises seeking to 
adopt DT technologies. 
 
Table 1 
Specific literature review summary table (R: real, V: virtual, TCP/IP: Transmission Control Protocol/Internet 
Protocol, SCH: scheduling, RESCH: rescheduling, OPT: optimization, MAIN: maintenance, LAB: laboratory 
testbed, SIM: simulation, THE: theoretical example, TCs: test cases, RPSD: real production system data) 
References 
Detailed 
components 
Communication 
DES 
involvement 
FL  
Digital Twin utilization 
Validation 
methodology 
[30] 
R/V 
OPC-UA 
yes 
yes 
SCH, RESCH 
LAB 
[29] 
V 
- 
yes 
no 
SCH, RESCH 
SIM 
[21] 
V 
- 
yes 
no 
OPT 
SIM 
[22] 
R/V 
OPC-UA 
yes 
no 
DT creation, 
visualization 
LAB 
[31] 
V 
OPC-UA 
yes 
yes 
reconfiguration 
SIM 
[23] 
V 
Kepware 
yes 
no 
prediction 
LAB 
[37] 
V 
- 
- 
yes 
OPT 
THE 
[32] 
V 
- 
yes 
changeability level 
determination 
THE 
[33] 
V 
- 
- 
yes 
fault-tolerant 
production 
TCs 
[25] 
V 
- 
- 
no 
SCH, RESCH 
RPSD 
[34] 
V 
OPC-UA 
- 
no 
resource allocation 
RPSD 
[35] 
V 
- 
- 
yes 
MAIN 
TCs 
[26] 
R/V 
OPC-UA 
- 
no 
reactive action 
LAB 
[36] 
R/V 
OPC-UA 
- 
no 
material handling, OPT, 
MAIN 
LAB 
[38] 
R/V 
Socket-based 
TCP/IP 
yes 
no 
OPT 
LAB 
[13] 
R/V 
OPC-UA 
yes 
no 
identification, tracking, 
monitoring 
LAB 
[28] 
R/V 
OPC-UA 
yes 
no 
synchronization, 
anomaly detection 
LAB 
 
 
 


---

Page 9

---

Decision Making: Applications in Management and Engineering 
Volume 8, Issue 1 (2025) 1-21 
9 
 
 
3. Methodology 
Based on the literature review prepared and published in Section 2 and the authors' experience 
in industrial digitization, Section 3 introduces a novel framework. It delineates the architecture, 
operational mechanisms, and the framework's suggested software and hardware specifications. 
 
3.1 Proposed Expert Twin Framework 
The framework is engineered to enhance efficiency and productivity. Figure 1 presents a 
conceptual diagram of the proposed structure. Central to this framework is an innovative decision 
support module that integrates DES's optimization and scenario exploration features with FL. This 
integration is informed by experts familiar with the system under consideration, encapsulating their 
observations and insights. The DT maintains a real-time linkage with the actual system, enabling 
dynamic interaction via OPC-UA protocols between the physical and virtual environments. This 
interaction facilitates the real-time acquisition, preprocessing, and filtration of field data, capturing 
the primary characteristics or states of the devices. 
Current literature highlights using computational technologies like FSs, which the DT employs to 
derive optimal decisions, actions, or recommendations to address uncertainties and non-linearities. 
These may include rescheduling or necessary interventions. Should an intervention be necessary, the 
decision-making module (DMM) conducts an optimization process to rearrange the production 
schedule. Utilizing the built-in genetic algorithm of the DES software and empirical analysis of 
experimental runs, this module estimates the optimal product sequence that either minimizes total 
production time or maximizes on-time deliveries. These objective functions are user-defined, and 
tailored specifically to the production system in question. 
 
 
Fig. 1. The Expert Twin framework 
 


---

Page 10

---

Decision Making: Applications in Management and Engineering 
Volume 8, Issue 1 (2025) 1-21 
10 
 
 
3.2 Digital Shadow module 
The proposed framework incorporates a DS model, essential for responding in real-time to 
alterations in the parameters and states of the physical system. The initial phase involves mapping 
the physical system within a DES environment, crafted to the requisite level of detail akin to 
conventional process simulation modeling. However, a key distinction lies in the fact that event 
triggers are derived directly from the physical system. Consequently, the PLC managing the physical 
system necessitates a direct and rapid communication link with the DES software, ideally without the 
intermediation of additional middleware or hardware. OPC-UA protocol offers a viable solution for 
M2M communication, supported by contemporary PLCs and compatible with DES software. Upon 
establishing this connection, sensor and actuator signals from the physical system are treated as 
events, enabling continuous remote monitoring and control and systematic data collection. 
Employing this methodology, the DS module alone can furnish actionable insights to facilitate 
optimization, though currently reliant on manual feedback. 
Proposed Hardware and Software 
• Siemens Tecnomatix Plant Simulation for developing the DS. 
• PLCs equipped with OPC-UA capability, such as the Siemens S7-1200 and S7-1500 product 
families. 
 
Required Competencies: Expertise in software environments and programming for both DES and 
PLC, alongside skills in OPC-UA information modeling. 
 
3.3 Decision-making module 
3.3.1 Simulation submodule 
The architecture of the Simulation submodule is intricately linked to the DS module. When 
constructing the model, elements from the DS are integrated sequentially; however, the 
programming of operational methodologies differs significantly. In the DS module, operational logic 
is controlled by signals emitted from the PLC. Conversely, in the Simulation submodule, the 
programmer is tasked with crafting the logic to mirror the system under simulation with high fidelity. 
This requires accurate input data and resource data to operationalize the model. To illustrate, within 
the DS framework, a product remains stationary at a specific station until the PLC issues an end-of-
process signal. In contrast, the Simulation model requires predefined knowledge about the duration 
of processes at each station. This essential data can be derived from the DS module, facilitating a 
more comprehensive representation within the simulation environment. 
This component is integral to converting the DS into a DT, aligning with the Kitzinger approach, 
which posits that the DT should facilitate bidirectional automatic data exchange between the physical 
and cyber systems. The employed communication protocol enables reciprocal data transmission, a 
common feature in various frameworks. Nonetheless, the mere capability for two-way 
communication is inadequate; a systematic approach to DM and intervention coordination is 
essential. 
 
3.3.2 Fuzzy logic submodule 
This block is responsible for turning the DS into a DT; following the Kritzinger approach [39], a DT 
should be a bidirectional automatic data exchange between the physical and the cyber system. It is 
necessary to incorporate decision logic into the DT to support or fully automate decision processes. 
Among the various methodologies employed in DM, Fuzzy Inference Systems (FIS) are prominently 
featured in the literature and widely adopted in industrial applications due to their simplicity, 


---

Page 11

---

Decision Making: Applications in Management and Engineering 
Volume 8, Issue 1 (2025) 1-21 
11 
 
 
efficacy, and intuitiveness [30]. FIS effectively models the non-linear relationships between inputs 
and outputs, facilitating robust and adaptable DM by applying fuzzy sets and rules. An FL module has 
been developed to recognize the challenges in the contemporary industrial digital landscape, where 
decision-critical information may not always be available with the requisite precision. The module 
should be constructed by experts with a good knowledge of the real system. The Sugeno-Fuzzy (SF) 
inference system is selected for its computational efficiency and effectiveness in handling 
optimization and adaptive challenges, making it particularly suitable for dynamic, nonlinear system 
control. In designing a Sugeno Fuzzy controller, a T-S Fuzzy model tailored to the nonlinear system is 
required. This system is characterized by blending fuzzy logic principles with systematic, 
mathematical methodologies to form a structured model capable of handling complex systems' 
inherent ambiguities and uncertainties. The formulation begins with defining the necessary fuzzy sets 
and their corresponding membership functions, categorizing the input variables into linguistic terms 
such as 'low', 'medium', and 'high'. Rules are then constructed, linking these fuzzy sets with their 
outcomes based on the logical operators AND, OR, and NOT. Constructing such a model is a 
fundamental and crucial step in this methodology. Generally, there are two prevalent strategies for 
developing fuzzy models: 
1) Identification, or fuzzy modeling, utilizing input-output data. 
2) Derivation based on the equations of the nonlinear system. 
 
The final output of the system is calculated by a weighted average of each rule's output, where 
the weights are the truth values of the rule's premises, evaluated using the membership functions of 
the inputs. This aggregation of outputs provides a single crisp output that effectively captures the 
system's behavior under various input conditions. The deployment of such a fuzzy inference system 
within operational frameworks can dramatically enhance DM capabilities by providing a robust 
mechanism for processing a range of input uncertainties and converting them into actionable 
outcomes. This capability is integral to optimizing operational efficiency and responsiveness in real-
time applications. 
Mathematical formulation of the Takagi-Sugeno Fuzzy Inference System: 
𝐼𝐹 𝑥1 𝑖𝑠 𝐴1 𝑎𝑛𝑑 𝑥2 𝑖𝑠 𝐴2 𝑇𝐻𝐸𝑁 𝑦= 𝑓(𝑥1, 𝑥2) 
𝑊ℎ𝑒𝑟𝑒 A and B are fuzzy sets and 𝑦= 𝑓(𝑥1, 𝑥2) 𝑖𝑠 𝑎 𝑐𝑟𝑠𝑖𝑝 𝑓𝑢𝑛𝑐𝑡𝑖𝑜𝑛 𝑖𝑛 𝑡ℎ𝑒 𝑐𝑜𝑛𝑠𝑒𝑞𝑢𝑒𝑛𝑡 
i-th rule can be represented as follows: 
𝑰𝑭 𝒙𝟏 𝒊𝒔 𝑨𝟏
𝒊 𝑨𝑵𝑫 𝒙𝟐 𝒊𝒔 𝑨𝟐
𝒊… 𝒙𝒏 𝒊𝒔 𝑨𝒏
𝒊 𝑻𝑯𝑬𝑵 𝒚𝒊= 𝒂𝟎
𝒊+ 𝒂𝟏
𝒊𝒙𝟏+ ⋯+ 𝒂𝒏
𝒊𝒙𝒏 
𝑾𝒉𝒆𝒓𝒆 𝒂𝟎, 𝒂𝟏, … 𝒂𝒏 𝒂𝒓𝒆 𝒕𝒉𝒆 𝒄𝒐𝒏𝒔𝒕𝒂𝒏𝒕𝒔 
weight of i-th rule can be determined as follows:  
𝒘𝟏= 𝝁𝑨𝟏
𝒊(𝒙𝟏) × 𝝁𝑨𝟐
𝒊(𝒙𝟐) × … × 𝝁𝑨𝒏
𝒊(𝒙𝒏)  
𝒙∗= 
∑
𝒘𝒊
𝒌
𝒊=𝟏
 𝒚𝒊
∑
𝒘𝒊
𝒌
𝒊=𝟏
 
Where k indicates total number of rules 
Proposed hardware and software: 
• Siemens Tecnomatix Plant Simulation to create a production process simulation. 
• Matlab Fuzzy Toolbox to create an SF system. 
 
3.4 Overview of Framework Operation 
The operational mechanism of the framework is structured as follows: The ERP system 
collaborates with the MES to compile the task list for the PLC of the manufacturing system. If 
historical data are accessible, the simulation module can be employed to formulate an optimized 


---

Page 12

---

Decision Making: Applications in Management and Engineering 
Volume 8, Issue 1 (2025) 1-21 
12 
 
 
sequence plan prior to process initiation. Upon commencement of the process, the DS system 
monitors the physical system in real-time, logging each event systematically. It continually assesses 
the alignment between the preliminary plan and the actual status. Should discrepancies surpass 
predefined thresholds or an unforeseen event occur (e.g., raw material shortages, equipment 
failures), the DS issues a trigger signal to DMM. The FL submodule evaluates whether new 
optimization is warranted based on the current data to avoid unnecessary actions. If optimization is 
deemed necessary, the simulation submodule revises its operation using the log data collected by 
the DS, and the updated model then assesses potential enhancements to the plan for the remaining 
tasks. The FL submodule, guided by established rules, determines whether intervention is required. 
If an intervention is decided upon, it prompts a modification in the task list of the PLC that controls 
the actual system. 
 
4. Results 
4.1 Test manufacturing cell 
To demonstrate and validate the efficiency of the proposed Expert Twin framework, a customized 
FESTO Modular Production System (MPS) has been utilized. This manufacturing cell, modern in terms 
of its components and reflective of contemporary industrial applications, serves as a testbed to 
exhibit the functionality and effectiveness of the newly developed system through a scaled-down 
industrial setup (Figure 2). 
 
 
Fig. 2. Real System. Customized FESTO modular cell 
 
The MPS processes cylindrical parts differentiated by three distinct colors. These parts are 
segregated into containers based on color; however, each container may contain both machined 
(hollow) and unmachined (solid) items, a distinction crucial to subsequent processing stages. Initial 
processing involves a sensor station that performs color verification and depth measurement, with 
these characteristics encoded onto an RFID tag attached to each part. Following the digital cataloging 


---

Page 13

---

Decision Making: Applications in Management and Engineering 
Volume 8, Issue 1 (2025) 1-21 
13 
 
 
of these attributes, the required machining degree is assessed at a mechanical depth detection 
station. Based on these defined product characteristics, subsequent decisions regarding the routing 
of each part are made at the next station. Machined parts may proceed directly if the conveyor belt 
elements ahead are unoccupied; otherwise, they are held until the pathway is clear. Parts requiring 
additional machining are transferred by a manipulator equipped with a vacuum head gripper to 
another conveyor leading to the machining station. Post-machining, the parts retrace their path to 
the production line's end, where they are systematically placed in a storage area by a robotic arm. 
In order to increase the complexity of the process shown, products of different colors are 
assigned varying processing times at each station. Additionally, the system can be configured to 
disable direct routes from parallel conveyors, necessitating the transfer of all products to the 
machining branch, even those not requiring further processing. In this case, products not needing to 
be machined are also placed at the machining station to continue without processing time. 
 
4.2 DS and Simulation Model implementation 
The authors' prior investigations [27,28] have already dealt in detail with the development of DS 
and DT solutions capable of replicating processes in manufacturing systems, which is summarized in 
the current article. 
The initial development phase involved establishing a DS (Figure 3). This required setting up an 
automatic data linkage between the physical system and its digital counterpart. It is crucial to ensure 
the presence of a communication channel compatible with both the hardware and software 
components involved. As discussed earlier, this connectivity is achieved through the OPC-UA 
communication protocol, a standard that satisfies real-time communication requirements and is 
broadly supported across various IoT devices. This compatibility facilitates future integrations with 
additional devices, enhancing the collection of data and thus refining the virtual model of the real 
system. On the hardware side, a Siemens S7-1516P/N PLC is employed to manage the control 
functions within the production system. This PLC gathers comprehensive data from all sensors and 
actuators in the system, making this information accessible to connected clients through a structured 
OPC-UA information model, effectively functioning as a server. The software environment utilized is 
Siemens Tecnomatix Plant Simulation, which interacts with the PLC data, responding and 
transmitting information back to the PLC. This integration of a modern PLC with a contemporary 
event-driven simulation tool allows for creating a DS module without the need for additional 
software or hardware. 
 
 
Fig. 3. Digital Shadow and Simulation model implemented in DES environment 
 
 


---

Page 14

---

Decision Making: Applications in Management and Engineering 
Volume 8, Issue 1 (2025) 1-21 
14 
 
 
4.3 Expert knowledge implementation 
This work primarily aims to enhance the efficiency of automated decision support processes by 
integrating human expert knowledge. The method is demonstrated using a simplified approach due 
to the lower computational demands and the relatively uncomplicated nature of the test system 
compared to a full-scale industrial environment, which consequently restricts the scope for process 
improvement and intervention. It is essential to acknowledge that while the proposed framework is 
universally adaptable, the individual modules must be customized to the specific manufacturing 
context by experts familiar with the system. Additionally, the framework's performance should be 
continuously monitored and adjusted as necessary. Moreover, the framework can integrate not only 
one but several different fuzzy inference systems. Two levels of DM have been distinguished. The 
first one (DMM_I) takes two input parameters (Figure 4), and the second one (DMM_II) takes three 
input parameters into account to determine whether it is necessary to modify the current production 
schedule to minimize lead time. The parameters in each case are: 
DMM_I: 
• Expected downtime: within an industrial setting, it is a critical component of production 
management for maintenance and diagnostic personnel to estimate the anticipated 
downtime in the event of a potential equipment malfunction. 
Membership functions: short, medium, long. 
• Percentage of remaining quantity: this metric denotes the proportion of the remaining 
volume to be processed on a specified resource, relative to the total batch size currently 
under production. 
Membership functions: few, moderate, many. 
 
 
Fig. 4. A Fuzzy model applicable to the specified use case (DMM_I) 
 
DMM_II: 
• f(u): outcome of the antecedent decision module (DMM_I). This parameter quantifies the 
urgency of intervention based on the primary criteria evaluated. 
Membership functions: low, medium, high. 
• Achievable efficiency: this value indicates the achievable efficiency improvement of each 
re-planning option compared to the current plan under the changed circumstances. The 
simulation module searches for an optimal solution with updated values synchronized 
from DS. 


---

Page 15

---

Decision Making: Applications in Management and Engineering 
Volume 8, Issue 1 (2025) 1-21 
15 
 
 
Membership functions: low, medium, high. 
• Level of schedule modification: in industrial contexts, maintaining schedule stability is 
paramount during revisions. This metric expresses the extent of adjustments associated 
with the rescheduling. From a DM perspective, this is significant as new optimizations may 
yield a schedule distinctly divergent from the original. 
Membership functions: low, medium, high. 
 
Figure 5 presents a schematic representation of the expert twin DM algorithm, specifically 
tailored to the use case. This flowchart delineates the systematic progression of computational steps 
and decision nodes that constitute the algorithm. The algorithm encapsulates a series of logical 
assessments and data processing tasks that facilitate real-time DM based on the dynamic data 
received from the physical system it mirrors. The structured arrangement of these tasks within the 
flowchart allows an intuitive understanding of the DM process, highlighting how data inputs are 
transformed into actionable insights or operational adjustments. 
 
4.4 Test scenario findings 
Several tests were carried out on the system presented during the case study. These evaluations 
involved the application of the proposed Expert Twin (ET) methodology, whose outcomes were 
benchmarked against those derived from a reference solution employing predefined lower and upper 
intervention thresholds. In this comparative analysis, the deviations between the actual operational 
states and the theoretically designed states were scrutinized using the limiting value methodology. 
The findings from these experiments substantiated the efficacy of utilizing a DMM equipped with 
precisely calibrated parameters. It was demonstrated that this approach significantly curtails the 
frequency of non-essential rescheduling activities, typically of low utility. Consequently, this 
reduction in unnecessary adjustments leads to decreased time spent on machine changeovers and 
the reorganization of logistical processes, thereby enhancing the overall efficiency of the production 
line and reducing lead times. 
Conversely, the method used for comparison purposes was observed to prompt re-optimization 
of the process in several instances. This frequently resulted in extended reallocation times and 
increased lead times, albeit maintaining lower idle times. This contrasts with the ET approach, where 
it was more commonly noted that the system experienced delays awaiting necessary resource 
adjustments. This comparative analysis highlights the ET methodology's distinct operational 
dynamics and potential efficiencies in streamlining production processes. 
The ET significantly enhanced the utility of the production line, achieving an increase of up to 
28%. Additionally, the frequency of rescheduling operations was effectively reduced by half. These 
findings are derived from data collected within the test environment; consequently, asserting that 
analogous substantial outcomes will be observed across all systems is not universally applicable. The 
replicability of these results is contingent upon the system's specific characteristics under 
examination, and the efficacy of the DMM and associated simulation models developed. 
Nevertheless, by leveraging a human knowledge base, there is a considerable probability that an 
effective automated decision support framework can be established that would be well-suited to 
various operational contexts. This solution also demonstrates a greater alignment with real-world 
industrial applications. Introducing a new schedule or deviations from the predefined plan can 
considerably elevate the risk of quality errors, often attributable to lapses in attention. Such 
circumstances necessitate stringent work management practices to ensure that these adjustments 
do not compromise the quality and integrity of the production process. Effective management and 


---

Page 16

---

Decision Making: Applications in Management and Engineering 
Volume 8, Issue 1 (2025) 1-21 
16 
 
 
precise coordination are essential to mitigate these risks, emphasizing the critical nature of robust 
oversight in dynamic industrial settings. 
 
 
Fig 5. Decision-making flow chart to the specified use case 
 


---

Page 17

---

Decision Making: Applications in Management and Engineering 
Volume 8, Issue 1 (2025) 1-21 
17 
 
 
5. Conclusions 
The research presented in this paper elaborates on the Expert Twin framework, an innovative DT 
system that integrates an FL-based DMM to enhance manufacturing processes. The framework is a 
significant advancement in the field of I4.0, facilitating real-time operational adjustments and 
decision support through seamless integration with CPS. 
The ET framework has demonstrated considerable improvements in production efficiency and 
DM capabilities. In controlled testing environments, implementing the ET framework led to a 28% 
increase in production line utility and a 50% reduction in the necessity for rescheduling operations. 
These enhancements underscore the framework's potential to optimize manufacturing workflows 
significantly, thus reducing operational lead times and enhancing system responsiveness to 
unforeseen production variables. It is essential to recognize the limitations of these findings as they 
are derived from controlled test scenarios. The actual applicability and effectiveness of the ET 
framework in diverse manufacturing settings may vary based on specific system characteristics and 
the intricacies of the deployment environment. Therefore, while the initial results are promising, 
further real-world applications and extended validation studies are necessary to ascertain the 
framework's universal effectiveness and adaptability fully. 
The integration of fuzzy logic within the DM processes of the ET framework highlights its 
capability to handle ambiguous and fluctuating manufacturing data effectively. This integration 
supports robust DM that accommodates the complexities and nonlinearities inherent in dynamic 
manufacturing environments. Future research should focus on enhancing the scalability of the ET 
framework to support its application across a broader range of industrial settings and complexities. 
Additionally, increasing the autonomy of the DM processes through more advanced artificial 
intelligence methodologies could further reduce the reliance on human intervention and streamline 
operations. 
Overall, the Expert Twin framework represents a significant stride towards more intelligent, 
efficient, and adaptable manufacturing systems, aligning with the goals of I4.0 to integrate digital 
and physical processes seamlessly. As industries continue to evolve towards fully automated and 
smart manufacturing systems, the principles and technologies demonstrated in the ET framework 
will likely play a pivotal role in shaping future manufacturing paradigms. 
 
List of abbreviations 
 
CPPS 
 
Cyber-Physical Production System  
CPS 
 
Cyber-Physical System 
DES 
 
Discrete Event Simulation 
DM 
 
DM 
DMM 
 
Decision-making Module 
DS  
 
Digital Shadow 
DT  
 
Digital Twin 
ERP 
 
Enterprise Resource Planning 
ET  
 
Expert Twin 
FIS  
 
Fuzzy Inference System 
FL  
 
Fuzzy Logic 
FLAIS 
 
FL-enabled Autonomous IoT Systems  
FTA 
 
Fault Tree Analyzer  
I4.0 
 
Industry 4.0 


---

Page 18

---

Decision Making: Applications in Management and Engineering 
Volume 8, Issue 1 (2025) 1-21 
18 
 
 
IoT  
 
Internet of Things  
JIS  
 
Just in Sequence 
JIT  
 
Just in Time 
LAB 
 
Laboratory testbed 
LT  
 
Lead Time 
M2M 
 
Machine to Machine 
MAIN 
 
Maintenance 
MES 
 
Manufacturing Execution System  
MPS 
 
Modular Production System  
NFC 
 
Near Field Communication 
OPC-UA 
 
OPC-Unified Architecture 
OPT 
 
Optimization 
PLC 
 
Programmable Logic Controller 
PS  
 
Tecnomatix Plant Simulation 
R  
 
Real 
RESCH 
 
Rescheduling 
RFID 
 
Radio-frequency Identification 
RPSD 
 
Real production system data 
SCH 
 
Scheduling 
SF  
 
Sugeno-Fuzzy 
SIM 
 
Simulation 
SMIs 
 
Small and Medium Industries 
SVM-ANFIS 
Support Vector Machine-Adaptive Neuro-Fuzzy Inference System 
TC  
 
Test case 
TCP/IP 
 
Transmission Control Protocol/Internet Protocol 
THE 
 
Theoretical example 
V  
 
Virtual 
ZDD 
 
Zero-suppressed Decision Diagram 
 
Author Contributions 
Conceptualization, G.D.M. and S.F.; methodology, G.D.M. and S.F.; software, G.D.M.; validation, 
G.D.M.; formal analysis, G.D.M. and S.F.; investigation, G.D.M. and S.F.; resources, G.D.M. and S.F.; 
data curation, G.D.M.; writing—original draft preparation, G.D.M. and S.F.; writing—review and 
editing, G.D.M. and S.F.; visualization, G.D.M.; supervision, S.F.; project administration, G.D.M. and 
S.F.; funding acquisition, G.D.M. and S.F. All authors have read and agreed to the published version 
of the manuscript. 
 
Funding 
This research received no external funding. 
 
Data Availability Statement 
The datasets generated or analyzed during this study are available from the corresponding author on 
reasonable request. 
 
 
 


---

Page 19

---

Decision Making: Applications in Management and Engineering 
Volume 8, Issue 1 (2025) 1-21 
19 
 
 
Conflicts of Interest 
The authors declare that they have no known competing financial interests or personal relationships 
that could have appeared to influence the work reported in this paper. 
 
Acknowledgement 
Project no. TKP2021-NVA-23 has been implemented with the support provided by the Ministry of 
Technology and Industry of Hungary from the National Research, Development and Innovation Fund, 
financed under the TKP2021-NVA funding scheme. The authors relate to the research team SZE-RAIL. 
 
References 
[1] 
Babaeimorad, S., Fattahi, P., Fazlollahtabar, H., & Shafiee, M. (2024). An integrated optimization of production and 
preventive maintenance scheduling in industry 4.0. Facta Universitatis, Series: Mechanical Engineering. 
https://doi.org/10.22190/FUME230927014B   
[2] 
Božanić, D., Epler, I., Puška, A., Biswas, S., Marinković, D., & Koprivica, S. (2024). Application of the DIBR II–rough 
MABAC decision-making model for ranking methods and techniques of lean organization systems management in 
the process of technical maintenance. Facta Universitatis, Series: Mechanical Engineering, 22(1), 101-123. 
https://doi.org/10.22190/FUME230614026B    
[3] 
Isametova, M., Nussipali, R., Karaivanov, D., Abilkhair, Z., & Isametov, A. (2022). Computational and Experimental 
Study of the Composite Material for the Centrifugal Pump Impellers Manufacturing. Journal of Applied and 
Computational Mechanics, 8(4), 1407-1421. https://doi.org/10.22055/jacm.2022.40366.3574    
[4] 
Chaubey, S. K., Gupta, K., & Madić, M. (2023). An investigation on mean roughness depth and material erosion 
speed during manufacturing of stainless-steel miniature ratchet gears by wire-EDM. Facta Universitatis, Series: 
Mechanical Engineering, 21(2), 239-258. https://doi.org/10.22190/FUME221220012C    
[5] 
Sljivic, M., Wagner, S., Pavlovic, A., & Marinkovic, D. (2022). Metal Additive Manufacturing of End-Use Components 
and Parts: A Practical Overview. In Virtual Conference on Mechanical Fatigue (pp. 149-160). Cham: Springer 
International Publishing. https://doi.org/10.1007/978-3-030-91847-7_15    
[6] 
Brautigam, A., Szalai, S., & Fischer, S. (2023). Investigation of the application of austenitic filler metals in paved 
tracks for the repair of the running surface defects of rails considering field tests. Facta Universitatis, Series: 
Mechanical Engineering. https://doi.org/10.22190/FUME230828032B     
[7] 
Fischer, S., Harangozó, D., Németh, D., Kocsis, B., Sysyn, M., Kurhan, D., & Brautigam, A. (2023). Investigation of 
heat-affected zones of thermite rail weldings. Facta Universitatis, Series: Mechanical Engineering. 
https://doi.org/10.22190/FUME221217008F    
[8] 
Tica, M., Vrcan, Ž., Troha, S., & Marinković, D. (2023). Reversible Planetary Gearsets Controlled by Two Brakes, for 
Internal Combustion Railway Vehicle Transmission Applications. Acta Polytechnica Hungarica, 20(1), 95–108. 
https://doi.org/10.12700/APH.20.1.2023.20.7    
[9] 
Ézsiás, L., Tompa, R., & Fischer, S. (2024). Investigation of the Possible Correlations between Specific Characteristics 
of Crushed Stone Aggregates. 1(1), 10-26. https://doi.org/10.31181/smeor1120242   
[10] Pfeiffer, A., Gyulai, D., Kádár, B., & Monostori, L. (2016). Manufacturing Lead Time Estimation with the Combination 
of 
Simulation 
and 
Statistical 
Learning 
Methods. 
Procedia 
Cirp, 
41, 
75–80. 
https://doi.org/10.1016/j.procir.2015.12.018  
[11] Monostori, L., Kádár, B., Bauernhansl, T., Kondoh, S., Kumara, S., Reinhart, G., Sauer, O., Schuh, G., Sihn, W., & 
Ueda, 
K. 
(2016). 
Cyber-physical 
systems 
in 
manufacturing. 
CIRP 
Annals, 
65(2), 
621–641. 
https://doi.org/10.1016/j.cirp.2016.06.005  
[12] Tilbury, D. M. (2019). Cyber-Physical Manufacturing Systems. Annual Review of Control, Robotics, and Autonomous 
Systems, 2, 427–443. https://doi.org/10.1146/annurev-control-053018-023652  
[13] Ward, R., Soulatiantork, P., Finneran, S., Hughes, R., & Tiwari, A. (2021). Real-time vision-based multiple object 
tracking of a production process: Industrial digital twin case study. Proceedings of the Institution of Mechanical 
Engineers, 
Part 
B: 
Journal 
of 
Engineering 
Manufacture, 
235(11), 
1861–1872. 
https://doi.org/10.1177/09544054211002464   
[14] Li, Y., Tao, Z., Wang, L., Du, B., Guo, J., & Pang, S. (2023). Digital twin-based job shop anomaly detection and dynamic 
scheduling. 
Robotics 
and 
Computer-Integrated 
Manufacturing, 
79, 
102443. 
https://doi.org/10.1016/j.rcim.2022.102443    
[15] Luo, D., Thevenin, S., & Dolgui, A. (2023). A state-of-the-art on production planning in Industry 4.0. International 
Journal of Production Research, 61(19), 6602–6632. https://doi.org/10.1080/00207543.2022.2122622    


---

Page 20

---

Decision Making: Applications in Management and Engineering 
Volume 8, Issue 1 (2025) 1-21 
20 
 
 
[16] Turner, C. J., & Garn, W. (2022). Next generation DES simulation: A research agenda for human centric 
manufacturing 
systems. 
Journal 
of 
Industrial 
Information 
Integration, 
28, 
100354. 
https://doi.org/10.1016/j.jii.2022.100354   
[17] Liu, X., Jiang, D., Tao, B., Xiang, F., Jiang, G., Sun, Y., Kong, J., & Li, G. (2023). A systematic review of digital twin 
about physical entities, virtual models, twin data, and applications. Advanced Engineering Informatics, 55, 101876. 
https://doi.org/10.1016/j.aei.2023.101876    
[18] Tao, F., Zhang, H., & Zhang, C. (2024). Advancements and challenges of digital twins in industry. Nature 
Computational Science, 4(3), 169–177. https://doi.org/10.1038/s43588-024-00603-w   
[19] Ladj, A., Wang, Z., Meski, O., Belkadi, F., Ritou, M., & Da Cunha, C. (2021). A knowledge-based Digital Shadow for 
machining industry in a Digital Twin perspective. Journal of Manufacturing Systems, 58, 168–179. 
https://doi.org/10.1016/j.jmsy.2020.07.018                
[20] Dos Santos, C. H., Montevechi, J. A. B., De Queiroz, J. A., De Carvalho Miranda, R., & Leal, F. (2022). Decision support 
in productive processes through DES and ABS in the Digital Twin era: A systematic literature review. International 
Journal of Production Research, 60(8), 2662–2681. https://doi.org/10.1080/00207543.2021.1898691   
[21] Ricondo, I., Porto, A., & Ugarte, M. (2021). A digital twin framework for the simulation and optimization of 
production systems. Procedia CIRP, 104, 762–767. https://doi.org/10.1016/j.procir.2021.11.128    
[22] Resman, M., Protner, J., Simic, M., & Herakovic, N. (2021). A Five-Step Approach to Planning Data-Driven Digital 
Twins for Discrete Manufacturing Systems. Applied Sciences, 11(8), 3639. https://doi.org/10.3390/app11083639   
[23] Eyring, A., Hoyt, N., Tenny, J., Domike, R., & Hovanski, Y. (2022). Analysis of a closed-loop digital twin using discrete 
event simulation. The International Journal of Advanced Manufacturing Technology, 123(1), 245–258. 
https://doi.org/10.1007/s00170-022-10176-5   
[24] Onaji, I., Tiwari, D., Soulatiantork, P., Song, B., & Tiwari, A. (2022). Digital twin in manufacturing: Conceptual 
framework and case studies. International Journal of Computer Integrated Manufacturing, 35(8), 831–858. 
https://doi.org/10.1080/0951192X.2022.2027014   
[25] Tliba, K., Diallo, T. M. L., Penas, O., Ben Khalifa, R., Ben Yahia, N., & Choley, J.-Y. (2023). Digital twin-driven dynamic 
scheduling 
of 
a 
hybrid 
flow 
shop. 
Journal 
of 
Intelligent 
Manufacturing, 
34(5), 
2281–2306. 
https://doi.org/10.1007/s10845-022-01922-3   
[26] Negri, E., Berardi, S., Fumagalli, L., & Macchi, M. (2020). MES-integrated digital twin frameworks. Journal of 
Manufacturing Systems, 56, 58–71. https://doi.org/10.1016/j.jmsy.2020.05.007   
[27] Monek, G. D., & Fischer, S. (2023). IIoT-Supported Manufacturing-Material-Flow Tracking in a DES-Based Digital-
Twin Environment. Infrastructures, 8(4), 75. https://doi.org/10.3390/infrastructures8040075   
[28] Monek, G. D., & Fischer, S. (2023). DES and IIoT fusion approach towards real-time synchronization of physical and 
digital components in manufacturing processes. Reports in Mechanical Engineering, 4(1), 161–174. 
https://doi.org/10.31181/rme040115092023m                
[29] Yu, H., Han, S., Yang, D., Wang, Z., & Feng, W. (2021). Job Shop Scheduling Based on Digital Twin Technology: A 
Survey and an Intelligent Platform. Complexity, 2021, 1–12. https://doi.org/10.1155/2021/8823273   
[30] Villalonga, A., Negri, E., Biscardo, G., Castano, F., Haber, R. E., Fumagalli, L., & Macchi, M. (2021). A decision-making 
framework for dynamic scheduling of cyber-physical production systems based on digital twins. Annual Reviews in 
Control, 51, 357–373. https://doi.org/10.1016/j.arcontrol.2021.04.008   
[31] Mo, F., Rehman, H. U., Monetti, F. M., Chaplin, J. C., Sanderson, D., Popov, A., Maffei, A., & Ratchev, S. (2023). A 
framework for manufacturing system reconfiguration and optimisation utilising digital twins and modular artificial 
intelligence. 
Robotics 
and 
Computer-Integrated 
Manufacturing, 
82, 
102524. 
https://doi.org/10.1016/j.rcim.2022.102524   
[32] Francalanza, E., Borg, J. C., & Constantinescu, C. (2016). A Fuzzy Logic Based Approach to Explore Manufacturing 
System Changeability Level Decisions. Procedia CIRP, 41, 3–8. https://doi.org/10.1016/j.procir.2015.12.011   
[33] Saraeian, S., & Shirazi, B. (2022). Digital twin-based fault tolerance approach for Cyber–Physical Production System. 
ISA Transactions, 130, 35–50. https://doi.org/10.1016/j.isatra.2022.03.007  
[34] Wang, X., Hu, X., & Wan, J. (2024). Digital-twin based real-time resource allocation for hull parts picking and 
processing. Journal of Intelligent Manufacturing, 35(2), 613–632. https://doi.org/10.1007/s10845-022-02065-1   
[35] Tulasiraman, M., Dayanandan, U., Ferrnandez, T. F., Vellaichamy, V., & Rajasekeran, D. (2024). Fuzzy Logic-enabled 
Autonomous IoT Systems for proactive maintenance in industry 4.0 digital twin scenarios. Optical and Quantum 
Electronics, 56(4), 505. https://doi.org/10.1007/s11082-023-06133-5  
[36] Glatt, M., Sinnwell, C., Yi, L., Donohoe, S., Ravani, B., & Aurich, J. C. (2021). Modeling and implementation of a 
digital twin of material flows based on physics simulation. Journal of Manufacturing Systems, 58, 231–245. 
https://doi.org/10.1016/j.jmsy.2020.04.015   


---

Page 21

---

Decision Making: Applications in Management and Engineering 
Volume 8, Issue 1 (2025) 1-21 
21 
 
 
[37] Turgay, S., Bilgin, Ö., & Akar, N. (2022). Digital Twin Based Flexible Manufacturing System Modelling with Fuzzy 
Approach. Advances in Computer, Signals and Systems, 6(7), 10-17. https://doi.org/10.23977/acss.2022.060702   
[38] Ait-Alla, A., Kreutz, M., Rippel, D., Lütjen, M., & Freitag, M. (2021). Simulated-based methodology for the interface 
configuration of cyber-physical production systems. International Journal of Production Research, 59(17), 5388–
5403. https://doi.org/10.1080/00207543.2020.1778209   
[39] Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W. (2018). Digital Twin in manufacturing: A categorical 
literature 
review 
and 
classification. 
IFAC-PapersOnLine, 
51(11), 
1016–1022. 
https://doi.org/10.1016/j.ifacol.2018.08.474   
 
 
