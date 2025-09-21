

---

Page 1

---

Digitalization of urban multi-energy systems – Advances in digital twin 
applications across life-cycle phases
B. Koirala a,*, H. Cai a, F. Khayatian a,b, E. Munoz a, J.G. An a,c, R. Mutschler a, M. Sulzer a,  
C. De Wolf a,d, K. Orehounig a,e
a Urban Energy Systems Lab, Swiss Federal Laboratories for Materials Science and Technology (Empa), Überlandstrasse 129, 8600 Dübendorf, Switzerland
b Klesse College of Engineering and Integrated Design, The University of Texas at San Antonio, 1 UTSA Circle, San Antonio, TX 78249, USA
c Electronics and Telecommunication Research Institute, 218 Gajeong-ro, Yuseong-gu, Daejeon 34129, South Korea
d Circular Engineering for Architecture, Swiss Federal Institute of Technology (ETH), Stefano-Franscini-Platz, 5, Zürich 8093, Switzerland
e Faculty of Architecture and Spatial Planning, TU Wien, Karlsplatz 13 1040 Vienna, Austria
A R T I C L E  I N F O
Keywords:
Digital twin
Urban energy systems
Digitalization
Modeling
Data
Ontologies
Life-cycle phases
A B S T R A C T
Urban multi-energy systems (UMES) incorporating distributed energy resources are vital to future low-carbon 
energy systems. These systems demand complex solutions, including increased integration of renewables, 
improved efficiency through electrification, and exploitation of synergies via sector coupling across multiple 
sectors and infrastructures. Digitalization and the Internet of Things bring new opportunities for the design- 
build-operate workflow of the cyber-physical urban multi-energy systems. In this context, digital twins are ex­
pected to play a crucial role in managing the intricate integration of assets, systems, and actors within urban 
multi-energy systems. This review explores digital twin opportunities for urban multi-energy systems by first 
considering the challenges of urban multi energy systems. It then reviews recent advancements in digital twin 
architectures, energy system data categories, semantic ontologies, and data management solutions, addressing 
the growing data demands and modelling complexities. Digital twins provide an objective and comprehensive 
information base covering the entire design, operation, decommissioning, and reuse lifecycle phases, enhancing 
collaborative decision-making among stakeholders. This review also highlights that future research should focus 
on scaling digital twins to manage the complexities of urban environments. A key challenge remains in identi­
fying standardized ontologies for seamless data exchange and interoperability between energy systems and 
sectors. As the technology matures, future research is required to explore the socio-economic and regulatory 
implications of digital twins, ensuring that the transition to smart energy systems is both technologically sound 
and socially equitable. The paper concludes by making a series of recommendations on how digital twins could 
be implemented for urban multi energy systems.
1. Introduction
The current energy system is transforming, driven by technological 
advances, climate and energy policy shifts, and evolving societal ex­
pectations [1,2]. The rapid advancement of decarbonization, decen­
tralization, and digitalization has revolutionized the energy sectors 
[3–7]. In this context, UMES are emerging in the energy landscape due 
to their ability to optimally manage increasing shares of distributed 
energy resources (DERs) in terms of type, location, and time [8–10]. As 
urban areas become the epicenters of global energy consumption, the 
integration of multiple energy sectors such as electricity, heat, and gas is 
critical for demand management, increased integration of renewables, 
and reduction of environmental impacts. As illustrated in Fig. 1, with the 
increasing number of energy carriers, technologies, and actors, the 
complexities of socio-technical energy systems are also increasing 
rapidly. Due to increasing sector coupling, energy systems are becoming 
a decentralized interconnected system of systems, further increasing the 
complexity of system architecture and operation [11–13]. Such 
increasing complexity requires advanced digital tools to navigate it 
[14].
Digitalization is playing a crucial role in the changing energy land­
scape. Energy systems are going through rapid evolution towards 
* Corresponding author.
E-mail address: binod.koirala@empa.ch (B. Koirala). 
Contents lists available at ScienceDirect
Advances in Applied Energy
journal homepage: www.elsevier.com/locate/adapen
https://doi.org/10.1016/j.adapen.2024.100196
Received 17 May 2024; Received in revised form 22 October 2024; Accepted 23 October 2024  
Advances in Applied Energy 16 (2024) 100196 
Available online 28 October 2024 
2666-7924/© 2024 The Author(s). Published by Elsevier Ltd. This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/ ). 


---

Page 2

---

digitalization thanks to emerging technologies such as the internet of 
things (IoT), artificial intelligence (AI), blockchain technology (BT), and 
digital twins (DTs) [15]. The increased application of information, 
communication, and automation technologies, as well as software, is 
transforming the energy system into a cyber-physical system [16–20]. 
These technologies facilitate more efficient energy distribution, pre­
dictive maintenance of energy assets, and better integration of distrib­
uted renewable energy sources. The emergence of digitalization and the 
Internet of Things (IoT) brings new opportunities and challenges for the 
planning and operation of the cyber-physical energy system [21].
Among these digital technologies, digital twins (DTs) have emerged 
as a transformative tool. A digital twin is an innovative concept that 
describes the management of a virtual replica of a physical object or 
system. Examples of digital twins are increasingly common in industrial 
sectors such as manufacturing, automotive, and logistics; however, the 
adoption of digital twins has been relatively slow in the energy sector. 
DTs offer virtual representations of physical energy assets, enabling real- 
time monitoring, simulation, and optimization across different life-cycle 
phases [1,22]. By integrating data from multiple sources, DTs create a 
comprehensive digital counterpart that represents the state and 
behavior 
of 
its 
physical 
counterpart, 
enabling 
improved 
decision-making and operational efficiency [23,24]. DTs can also opti­
mize operations and contribute to predictive maintenance, increasing 
the reliability of energy systems [25]. These virtual representations in 
DTs include models enabling stakeholders to foresee the impact of 
different scenarios and strategies [26]. Data-driven modeling, optimi­
zation, and model learning processes are functionalities enabled by 
digital replicas [27]. At the same time, digital twins (DT) and 
cyber-physical systems are considered closely related concepts that can 
complement each other. DTs use data from cyber-physical systems to 
enhance predictive analytics and optimization, improving the efficiency 
and resiliency of energy systems. Through better insight based on 
real-time data from cyber-physical systems, DTs can facilitate the energy 
system integration of renewables [28], improve system reliability [29], 
and provide much-needed flexibility services [22,30] – hence allowing 
the transformation of the current fossil fuel-based energy system into a 
low-carbon one.
DTs offer a real-time connection to data, enhancing information 
modeling processes such as Building Information Modelling (BIM), In­
ternational Foundation Class (IFC), Geographic Information System 
(GIS), and supporting simulation models like Functional Mock-up 
Interface (FMI). However, the full potential of data-driven modeling is 
often hindered by siloed data, a common challenge in digital trans­
formation. The integration of semantic data as a feature of DTs can help 
address this issue. DTs frequently incorporate an internal knowledge 
graph, which, when based on semantic web standards such as Web 
Ontology Language (OWL), can improve interoperability and scalability 
[31].
In the changing energy and digital landscape, several cities and 
communities around the world are increasingly using or planning to 
adopt DTs. Below and in Section 5, we offer an overview of the potential 
of these initiatives. For example, Cityzenith is developing the urban DT 
of several cities such as Las Vegas, Phoenix, Aberdeen, etc. [32]. These 
DTs combine available data in a standard, easy-to-understand 3D visual 
model to help decision-making. Stockholm virtual city, a 3D city DT 
model, performs real-time fleet, traffic flows, and pedestrian mapping 
using different software from Bentley [33]. It provides digital contexts 
for designing complex scenarios for urban planning projects. Similarly, 
Zürich 4D is a DT for visualizing structural development in space and 
time, including future scenarios, which is not yet coupled with the en­
ergy system [34]. Yet, it is an effective source for the historical and 
future data of the urban built environment of Zürich. A digital urban 
climate twin, which also considers the energy system and its anthro­
pogenic heat emissions, has been developed for Singapore [35]. It can 
demonstrate how measures like electric vehicles and tree cover can 
reduce urban heat in Singapore. For more details on some of these UMES 
DT applications, refer to Section 5.
In the context of UMES, DTs have attracted considerable interest for 
their potential to improve the entire supply chain from generation, 
transport, distribution, and consumption as well as to manage increasing 
Fig. 1. Schematic diagram of lateral multi-energy carrier interactions in urban multi-energy systems (UMESs). The diagram illustrates a complex system architecture 
of UMESs covering the entire value chain from local generation, conversion, storage, transport, and demand. Different colored arrows represent multi-energy carriers 
flow (green: electricity, blue: Hydrogen, grey: (synthetic/bio) methane, red: heating, and orange: cooling). CHP: combined heat and power, PV: photovoltaics, PVT: 
photovoltaics and thermal collector, MSW: municipal solid waste, SMR: steam methane reforming, ATR: auto-thermal reforming, H2: hydrogen, and CH4: methane.
B. Koirala et al.                                                                                                                                                                                                                                 
Advances in Applied Energy 16 (2024) 100196 
2 


---

Page 3

---

complexity. From optimizing energy generation units and grid operation 
to improving energy efficiency in buildings, DTs offer opportunities to 
improve the economic and environmental performance of UMES [36]. 
Such latest digital applications also help exploit synergies and in­
terdependencies between different energy systems and sectors [37]. Yet, 
it should be highlighted here that these applications of DTs so far are 
mainly limited to data collection, communication, and visualization, but 
fully functional UMES DTs do not fully exist yet in practice. The existing 
applications also suffer from fragmented approaches and are not ready 
to act as a holistic ecosystem of DTs to make sound decisions. Ideally, the 
DTs from the planning stage should accompany and enhance the UMES’s 
commissioning, operation, performance monitoring, and decom­
missioning. The integration of DTs in UMES represents a significant leap 
forward, offering unprecedented insights into system performance and 
facilitating more effective decision-making across the entire life cycle of 
UMESs. Despite these potential for scalability, the application of DTs for 
UMES has not been reviewed in detail. By delving into the current state 
of UMESs and the potential application of DTs, this review aims to un­
derstand how DTs can drive the future of UMESs comprehensively. Since 
UMES DTs are admittedly a new topic, this paper takes a clear stance and 
proposes what a UMES DT should look like. Readers are encouraged to 
approach this review paper with this consideration in mind.
1.1. Materials, methods, and research objectives
The methodological approach involves a comprehensive literature 
search on scholarly articles, technical reports, and industry publications. 
This detailed review synthesized advancements in DT architectures, 
energy system data categories, semantic ontologies, and data manage­
ment solutions, focusing on their application across different life-cycle 
phases pertinent to UMES.
As UMES continue to evolve, DTs have emerged as a transformative 
tool, enabling data-driven decision-making and optimization of urban 
infrastructure. Recent advancements in UMES and DTs have paved the 
way for innovative approaches to urban planning, monitoring and 
infrastructure management. To fully leverage the potential of DTs, it is 
crucial to explore several key areas like the latest technological de­
velopments, the methods for data collection from physical twins, and the 
techniques for data management and analytics, and their application 
across different lifecycle stages of UMES. This review addresses these 
essential aspects by investigating the following main research questions: 
- What are the recent advances in UMES and DTs?
- How is data collected from existing physical twins, including 
network infrastructures, technologies, sensors, and actuators? What 
are the data management and semantic ontologies techniques used to 
collect and store the data, and how can data be made accessible in 
the DT, ensuring interoperability across different data sources?
- How does DT process the data to generate insights into and infor­
mation about the physical twin, and how do its various components 
interconnect and communicate?
- How are DTs applied across different life cycle phases of UMES? 
How is information accessed through user interfaces, enabling 
informed decision-making by the relevant stakeholders?
To systematically address these questions, this review involved the 
following steps:
Systematic literature review: A comprehensive literature review is 
conducted using electronic databases such as Scopus, Web of Science, 
and Google Scholar, with key words like "urban multi-energy systems", 
"digital twins," "data models," and "data management". A total of 227 
sources including journal articles, conference papers, book chapters, 
technical reports, and relevant case studies, were reviewed to analyze 
advancements in UMES DT applications.
Identification of data and knowledge management in DTs: 
Various data sources for DTs, as proposed in the literature, including 
different twin phases, are identified and elaborated upon in Section 3. 
This includes the exploration of data management strategies across 
different twin phases.
Evaluation of semantic ontologies and data categories: The re­
view assessed the use of semantic ontologies and knowledge represen­
tation techniques to enhance the interoperability and semantic 
integration of heterogeneous data sources within UMES. Commonly 
adopted ontologies for energy, buildings, and urban infrastructure are 
reviewed in Section 3.
Application of DTs in UMES lifecycle phases: Case-studies were 
reviewed to investigate how DTs can be applied during the planning, 
operation, and reuse phases of UMES. The role of DTs in facilitating 
collaborating energy planning, improving system operations, and 
managing decommissioning processes are analyzed in Section 5.
Identification of research gaps and future directions: Based on 
the findings of the review, critical research gaps and future research 
directions are identified and discussed in Section 7, with particular 
attention to scalability, data integration, and interoperability issues, the 
integration of emerging technologies, and the socio-economic implica­
tions of UMES DTs.
The methodology ensures a comprehensive exploration of the cur­
rent state-of-the-art DT applications for UMES, providing a robust 
foundation for understanding and advancing this rapidly evolving field. 
The rest of the review paper is organized as follows to systematically 
examine the creation and application of UMES DT, addressing the key 
research gaps in this field. Section 2 introduces and defines the funda­
mental UMES and DT concepts, providing the necessary context for 
understanding how digital twins can address the complexity of UMES. 
Section 3 discusses the data management process within UMES DTs, 
focusing on data organization and promising initiatives for efficient data 
handling. This section highlights the need to address data integration 
challenges, a crucial research gap in the development of scalable and 
reliable UMES DTs. Section 4 reviews common methods for modelling 
and representing UMES DTs, highlighting which models and architec­
tures are most suitable and how frequently DTs should be updated – 
areas where the lack of a standardized approach remains a significant 
challenge. Section 5 covers various DT applications across planning, 
operation, and decommissioning phases, emphasizing their intercon­
nectedness and the need for holistic lifecycle management, a gap in 
current DT applications. Section 6 discusses the key findings and out­
lines the remaining challenges in scaling and applying digital twins to 
real-world UMES. Finally, Sections 7 and 8 present this review’s future 
outlook and the key conclusions, identifying research directions that can 
further advance the field.
2. Urban multi-energy systems (UMES) and digital twins (DT)
This section establishes the important context for understanding the 
role of DTs within UMES, highlighting their significance in the broader 
scope of urban energy systems. While the primary focus of the paper is 
on specific applications of DTs in UMES, the literature review has been 
expanded to highlight recent advancement in UMESs and to explore how 
digital twins can help improve the transition of these systems. A clear 
working definition of UMES, DTs, and UMES DTs are provided to clarify 
their scope in this paper. The sections conclude with a discussion on the 
key opportunities and challenges associated with implementing UMES 
DTs.
2.1. Urban multi-energy systems (UMES)
Given the advantages of distributed energy resources, UMESs are 
rapidly emerging in the energy landscape [4,11]. Inspired by the JPI 
Urban Europe’s definition of positive energy districts [38], the following 
definition is adopted to define the scope of this review: Urban 
multi-energy systems (UMES) are efficient and flexible decentralized energy 
systems composed of multiple interconnected consumers and producers that 
B. Koirala et al.                                                                                                                                                                                                                                 
Advances in Applied Energy 16 (2024) 100196 
3 


---

Page 4

---

emit low or net-zero greenhouse gases and actively manage local production 
and consumption of renewable energy. Geographically, they can span 
groups of buildings, neighborhoods, districts, and cities. UMES holisti­
cally integrates different energy carriers, technologies, and in­
frastructures in interaction with the buildings, the users, and the 
adjacent energy systems, mobility, and ICT while securing the energy 
supply in line with social, economic, and environmental sustainability.
Figs. 1 and 2 illustrate that UMESs are complex infrastructural net­
works integrating different generation, conversion, storage, and 
network technologies. UMES integrates various energy sources and 
technologies to meet the diverse energy needs of urban areas efficiently 
and sustainably. Fig. 2 shows that UMESs are a complex socio-technical 
[39,40], interconnected system of systems [41] consisting of multiple 
actors, various decision-makers, and technological artifacts governed by 
energy policy in a multi-level institutional space [42,43]. UMES actors 
include households, building-owners, local communities, housing cor­
porations, local municipalities, national government, energy suppliers, 
intermediaries or aggregators, system operators, energy service and 
technology providers, regulators, and (local) energy market operators 
[4,14]. By integrating multiple energy carriers, UMES goes beyond the 
concept of smart and microgrids, incorporating decentralized produc­
tion and utilizing local synergies [44]. The integration of different en­
ergy carriers such as electricity, (renewable) gas, heating, and cooling, 
as well as various sectors such as buildings and transport sectors 
together with community engagement, is expected to contribute to more 
flexible, sustainable, cost-effective, and efficient energy systems [4,45]. 
UMESs are emerging as an essential building block for the effective 
decarbonization of the built environment and for dealing with the se­
curity of supply challenges.
Previous research efforts have demonstrated techno-economic 
modeling approaches to the planning and operation of UMES [4,
46–50]. These studies utilize optimization techniques such as linear and 
non-linear programming [48,51–58]. Keirstead, Jennings, and Sivaku­
mar (2012) identified challenges of energy system modelling like model 
complexity, data quality, uncertainty, and model integration [59] . Nik, 
Prerea, and Chen (2021) highlight the need for improving the models 
capturing future climate variations to design resilient energy transition 
pathways [60]. Zheng et al. (2024) identified physical, cyber, and social 
energy processes layer in urban energy systems to further optimize their 
design and implementation [61]. The authors also highlight the need for 
data sharing and analytics for urban-scale energy modelling as well as 
policies for safety, privacy, cyber-security, and interoperability issues.
Moreover, current urban energy planning practices face significant 
challenges due to the vast array of modeling tools and continuously 
evolving data sets that are often not interlinked, compatible, or consis­
tent. This results in a constrained, static, and isolated view of UMES, 
particularly in multi-actor contexts. Future energy system models will 
benefit from access to sensors and contextual data [21]. For instance, a 
digital twin composed of connected metered PV readings could lead to 
better forecasts of energy supply and its intermittency. With the emer­
gence of cyber-physical systems, how data is collected, stored, analyzed, 
and presented is also changing. However, processing the dynamic and 
steadily increasing volume of data using traditional models is chal­
lenging. Sectoral integration, with increasing synergies and in­
terdependencies, adds further complexities to the planning and 
operation of UMES. As a result, significant challenges and opportunities 
exist for improving the modeling of UMES planning and operations, 
driven by the need to manage growing data quantities and extract 
actionable insights. Non-conventional approaches will be required for 
the effective planning and operation of UMES [62,63], and the appli­
cation of DTs is expected to help overcome these limitations.
Fig. 2. Schematic diagram of multi-level interactions of UMES as complex multi-layer socio-techno-economic systems of systems. The UMES is decomposed into 
technical, infrastructure, sector, and social scales. The four physical scales are represented in the Urban digital Twin, defining the UMES DT. The latest digitalization 
trends, such as cyber-physical systems, the Internet of Things, and digital twins, have the potential to provide a solid information basis for decision-making and 
performance monitoring. The classes categorize the typical components in UMES and are discussed further in Section 3 and Table 2.
B. Koirala et al.                                                                                                                                                                                                                                 
Advances in Applied Energy 16 (2024) 100196 
4 


---

Page 5

---

2.2. Digital twins (DT)
Several definitions regarding DTs are available in the literature [21,
24,64–69]. For the scope of this review, the following is adopted as a 
working definition: A digital twin (DT) is a virtual representation of an 
object or system that spans its lifecycle, is updated using real-time data, 
and uses models and machine-learning techniques as information bases 
to support decision-making [70]. The digital twin is an emerging 
concept in research and industry [65,67]. The idea of the digital twin 
was first introduced by Greives in 2003 concerning product life-cycle 
management as a virtual and digital equivalent to a physical product 
consisting of three main parts: a) physical products in real space, b) 
virtual products in virtual space, and c) the data and information 
interconnection between virtual and physical products [24,65]. How­
ever, some even believe that DTs were practiced many decades earlier, e. 
g., in NASA’s Apollo mission [71].
Moreover, there are several initiatives to make DTs of smart cities 
[72], whole countries such as the UK [73] and Singapore [74], and even 
the entire earth [75]. Rasheed et al. (2020) define the digital twin as “the 
virtual representation of a physical asset enabled through data and 
simulators for real-time prediction, optimization, monitoring, control­
ling and improved decision making” [76]. Hoffbauer et al. (2019) 
introduce several types of DTs: the digital twin prototype, the digital 
twin instance, and the digital twin aggregate [77]. Pileggi et al. (2019) 
argue that a digital twin is a simulation tool used in a specialized way, 
which is meant to be employed not only at the development stage but 
also during the operational phase of the physical system [21]. Woods 
and Freas (2019) emphasize that DTs are essential for understanding 
and managing the complex integration of multiple assets and systems, 
such as those found in zero-carbon communities [66]. Zhang et al. 
(2021) review various simulation tools, highlighting the potential of DT 
applications in accelerating sustainability efforts [78].
Similarly, Schooling et al. (2020) argue that DTs enhance the ability 
to monitor, interpret, and make more informed decisions across 
different infrastructure networks and sectors [79]. With the capabilities 
of multi-physics simulation, data analytics, machine learning, and arti­
ficial intelligence [80,81], DTs can effectively demonstrate the impact of 
design changes, operation scenarios, and environmental variations, thus 
facilitating the planning and operation processes. Multi-physics models 
offer interpretability, while machine-learning models contribute to the 
speed and efficiency of DTs [82]. The digital twins, with its ability to 
create dynamic, real-time representations of physical systems, serve as 
the foundational framework for their application within UMES, where 
the complexity and integration of diverse energy sources require 
specialized approaches..
2.3. UMES digital twins’ definition
From the definitions and discussion of DTs above, we can consider all 
UMES DTs to contain or at least strive for the following elements: 
1. A digital representation of a real-world physical UMES, including the 
data requirements and data processing module
2. A real-time data connection to the physical twin, which is updated at 
desired intervals
3. A mathematical model to predict specific behavior/future conditions 
of the physical twin, e.g., machine-learning-based, simulation, and 
optimization models.
Optionally, connections and mapping between digital twins of 
different UMES life-cycle phases and connections to other databases 
outside the scope of the urban energy system are needed.
Building on the foundational understanding of UMES DTs, it is 
essential to explore the current advancements, challenges, and ongoing 
initiatives in this field as identified by recent literature and projects. 
Ferr´e-Bigorra et al. (2022) reviews existing approaches on urban digital 
twin highlighting open issues, key challenges and requirements for 
future development [83]. Bettencourt (2024) highlights recent 
achievements and conceptual challenges for urban digital twins 
emphasizing size, heterogeneity and open-ended character of cities. 
Weil et al. (2023) indicates interoperability and semantics, computa­
tional infrastructures, data acquisition and quality, modeling and 
simulation, human resources as well as governance, organizational and 
social issues as main challenges for widespread adoption of urban digital 
twins [84]. Using systematic literature review and expert survey, Lei 
et al. (2023) also identifies interoperability and practical value as main 
challenges for urban digital twins [85]. Onile et al. (2021) explore DTs 
in energy services [22], and the +CityXchange project develops digital 
twin models for buildings in positive energy blocks, integrating a 
physics-driven simulation with operational data [86]. Peldon et al. 
(2024) highlights transformative role of digital twin in shaping urban 
futures [87]. JPI Urban Europe funded PED-ID project highlights po­
tential uses of DTs in various aspects of UMES, such as planning, visu­
alization, communication/stakeholder engagement, and simulation of 
scenarios [88]. Horizon Europe is also funding several new research 
projects on further developing and demonstrating DT applications in 
energy systems [89]. In addition, several commercial initiatives are also 
emerging for the development of UMES DTs [32,66]. Having reviewed 
the current developments and key research in UMES DTs, the next 
sub-section will delve into the specific advantages these systems offer, as 
well as the challenges that must be addressed for their effective imple­
mentation and widespread adoption.
2.4. Advantages and challenges of UMES DTs
The complex and multi-dimensional UMESs present significant 
challenges related to data integration, system optimization, and real- 
time operation. DTs provide innovative solutions to these challenges 
by offering a real-time, data-driven virtual replica of physical systems 
capable of simulating, monitoring and optimizing UMESs. DTs are ex­
pected to provide a robust information basis through continuous vali­
dation, integrating heterogeneous data sources, and investigating 
different what-if scenarios in UMESs. These capabilities will facilitate 
UMES’s continuous integrated planning, operation, and collaborative 
decision-making. UMES DTs facilitate improved resource management 
and optimization by monitoring and analyzing asset usage, perfor­
mance, and condition, including fault-detection. This allows for more 
efficient utilization of resources, such as energy, water, and materials. 
The data-driven approach enables better decision-making regarding 
resource 
allocation, 
maintenance 
scheduling, 
and 
retrofitting 
opportunities.
Additionally, DTs can assist in assessing environmental impacts and 
identifying sustainability improvements. By integrating data on energy 
consumption, material usage, and waste generation, DTs can provide 
insights into the ecological footprint of built assets. This information 
supports informed decision-making regarding design modifications, 
energy efficiency enhancements, and adopting circular practices, lead­
ing to a more sustainable built environment. The advantages of UMES 
DTs can be measured using the key performance metrics listed in 
Table 1.
Despite the above benefits, as illustrated in Table 1 below, today’s 
UMES DTs are not without shortcomings: The technical and financial 
complexity of establishing a DT represents a significant barrier, neces­
sitating a substantial commitment of resources and expertise [90]. The 
depth and breadth of data required to feed a DT for accurate reflection 
and forecasting can also cause data overload, where managing such 
information becomes an additional complex layer to navigate [91]. DTs 
simultaneously expand the potential attack surface for cyber threats 
[25]. Moreover, the development of DTs is bound by the quality of 
available data, which can be hindered by both technical data collection 
limitations and privacy regulations, thus impacting the veracity and 
utility of the DT model [92].
B. Koirala et al.                                                                                                                                                                                                                                 
Advances in Applied Energy 16 (2024) 100196 
5 


---

Page 6

---

As UMES evolve, so must the DTs that represent them, yet scaling 
these solutions to model larger, more complex systems accurately re­
mains a formidable task [62]. Additionally, discrepancies in communi­
cation standards and protocols across different UMES components pose 
interoperability challenges, further complicating the DTs’ ability to 
provide a seamless and unified system model [93]. Many challenges in 
operating DTs, such as lack of interoperability and practical value, 
hinder their design and implementation [85]. Additional challenges of 
the existing DT for UMES are rooted in the complexity of transforming 
energy systems into cyber-physical systems [62,94]. As UMESs evolve to 
integrate more DERs and adopt advanced digital and automation tech­
nologies, there is a pressing need for robust data management and so­
phisticated tools to harness the potential synergies and manage the 
reliability and flexibility of these interconnected systems [62].
Moreover, regulatory considerations are pivotal, as existing energy 
regulations may not have accounted for DTs’ rapid advancement and 
unique capabilities [95]. While DTs present an innovative tool for 
advancing UMES, the road to their full-scale implementation and 
seamless integration is marked by various technical, security, and reg­
ulatory hurdles due to data protection and privacy issues. Addressing 
these will require a concerted inter- and cross- disciplinary effort from 
researchers, industry practitioners, and policymakers to ensure that DTs 
can deliver on their promise to foster sustainable and resilient urban 
energy landscapes [2,96,97].
Having established the foundational context for UMES digital twins 
and explored their roles in advancing urban energy systems, the next 
section will delve deeper into the important aspect of data and knowl­
edge management, which underpins the development and operation of 
DT models. Effective data management is key to ensure that DTs can 
accurately represent and optimize UMES in real-time. The following 
section explores the processes and frameworks required to manage the 
vast amount of data generated and utilized by UMES DTs, examining 
how data flows through the various phases of UMES DTs’ lifecycle. The 
next section will also highlight the role of existing techniques like 
Building information modelling.
3. Data and knowledge management for UMES DTs
Data is essential for the development and operation of DT models. 
During its separate phases, namely pre-twin, active-twin, and post-twin, 
DTs often ingest and integrate data from multiple sources and require a 
data connection to the physical twin during its operation. Management 
of data is critical for the effective operation of a DT. This section explores 
the processes necessary to manage data required and generated by a DT. 
The review considers general requirements of DTs in the Architecture, 
Engineering, and Construction (AEC) sector and identifies specific fea­
tures or requirements necessary for UMES DTs. This section highlights 
the difference and complementarity between DTs and building infor­
mation modeling (BIM), as the latter is widely used in practice, espe­
cially in the AEC sector, and serves as an essential data source for DTs. 
Then, different data sources for UMES DTs in pre-twin, active, and post- 
twin phases are highlighted, corresponding to UMES’s design, opera­
tion, and decommissioning/material re-utilization phases, respectively. 
This follows a comprehensive elaboration on semantic ontologies and 
data-schemas for UMES DTs. Finally, data transaction protocols sup­
porting UMES DTs communications with physical twin and simulation 
models are highlighted.
3.1. The difference between DTs and BIM
Building information modeling (BIM) is a standardized process of 
managing digital information about a construction project and 
throughout the lifetime of an asset or facility. The BIM process applies to 
buildings and supports the construction and operation phases. Examples 
of applications of BIM relevant to UMES include urban energy planning 
[98], planning of district energy systems [99], community energy sys­
tem design [100], and site selection for a solar PV power plant [101]. 
BIM is typically applied in a project’s planning, design, construction, 
operational, and decommissioning phases [102,103],. The BIM process 
facilitates collaborative management and decision-making throughout a 
construction asset or facility’s lifetime.
On the other hand, DTs provide a real-time data connection and 
model how the physical asset will behave under different scenarios. 
Therefore, it can be argued that a BIM strategy is a prerequisite for a 
digital twin, as it provides the initial information required to build a 
UMES DT. The line separating BIM and DT is increasingly blurred. 
Dimensional extensions are used to describe the application and func­
tionality of BIM. 3D BIM describes the modeling of the geometry in 3 
dimensions. This is then extended to 4D (time), 5D (cost), 6D (safety/ 
sustainability), and 7D (facility management); however, there is limited 
agreement across the industry on what these categories refer to beyond 
the 5th dimension [104]. Some have also proposed an 8th dimension for 
the sustainability and circularity of the asset during the design process 
[105]. Others have gone beyond this, defining the 8th, 9th, and 10th 
dimensions as safety, lean requirements, and industrial automation 
[106]. The connection of the BIM model to real-time DTs has been 
proposed to close the performance gap between simulated and actual 
energy usage; however, closing this loop is far from maturity [107].
Table 1 
Overview of key issues and key performance indicators of urban multi-energy system digital twins (UMES DTs).
B. Koirala et al.                                                                                                                                                                                                                                 
Advances in Applied Energy 16 (2024) 100196 
6 


---

Page 7

---

DTs can be considered an extension or evolution of the BIM process, 
enabling ongoing operational decisions due to the real-time data 
connection. It could be argued that they represent or extend a dimension 
of the BIM process; however, it will take time until a consensus is 
established on this definition. BIM models have been considered insuf­
ficient for lifecycle asset management, and a shift to DTs that incorpo­
rate artificial intelligence, machine learning, and dynamic digital 
models has been proposed to address this shortfall [108]. DTs extend 
static BIM models to enable real-time analysis, visualization, and control 
of the built environment [109]. There are proprietary and nonpropri­
etary data formats to exchange BIM information. In addition to 
modeling construction assets, several opportunities from BIM-GIS inte­
gration have been hypothesized to expand the range of applications 
[110]. The use of BIM as a data source in GIS is particularly relevant for 
multi-energy systems as the spatial context of an energy system is vital in 
determining infrastructure synergies, resource availability, and demand 
flexibility. Conventional BIM models, however, are considered chal­
lenging for energy analysis of buildings due to the inability to extract 
space boundaries of buildings for energy analysis [100]. A review of the 
use of BIM in energy simulation has also been carried out by [111]. One 
of the main non-proprietary data formats for exchanging BIM informa­
tion is the Industry Foundation Classes (IFC) format. The IFC format is a 
reference format designed to share information between project stake­
holders. The focus is on interoperability, and the model has been criti­
cized for not containing sufficient semantic information for DTs; the 
authors propose a "no model architecture" to connect BIM and DT [112].
In this work, we define and align the UMES DT Lifecycle Phases with 
the established BIM project phases, see Fig. 3. The pre-twin phase cor­
responds to a BIM project’s Design, Planning, and Construction phases 
and UMES’s planning phase. During this phase, schematics and de­
scriptions of the system are created through an iterative process with 
engineers and other stakeholders. These data types can later be used to 
develop DTs that only become active once updated by the physical twin/ 
real-world facility; therefore, DTs are only active during the operational 
phase of a project. During the post-twin, the information collected by the 
active digital twin can assist in decommissioning and material and asset 
reuse.
3.2. Data sources for UMES DTs
A conceptual framework for UMES DTs for the urban area shows the 
necessity of integrating domain knowledge from infrastructure systems 
such as water, energy, and transportation [113]. In addition, other data, 
such as occupancy and economic activities, might also be relevant. This 
sub-section explores the different data types required by and produced 
by UMES DTs.
3.2.1. Pre-twin data sources
The pre-twin phase corresponds to the design-build phase of the 
physical object and refers to a period where there is no real-world 
physical counterpart to establish a data connection. Data is subject to 
frequent updates and refinements as designers build the DT during this 
period. Designers are focused on optimizing the system’s design, 
modeling performance, and procuring the equipment and expertise 
required to construct the real-world physical counterpart.
Fig. 4 shows the data types used during the pre-twin phase. The pre- 
twin phase corresponds to a BIM model’s design, planning construction 
phases, and UMES’s planning phase. In these phases, 3D BIM models are 
created containing architectural, structural, and system data, city scale 
geometry models, and geo-coded sensor data. This is then often 
extended to 4D (time) and 5D (cost) to perform what-if scenario analysis 
during the design phase. The data sources used in DTs are strongly tied 
to the scale of the physical entity they represent. For example, DTs of 
buildings rely on detailed information about the construction and ge­
ometry of the building, which is often contained in a BIM model; city- 
scale DTs, on the other hand, are usually built using open geospatial 
data, network topologies, and statistical data. DTs of UMES need to 
integrate data from multiple sources that cover the different physical 
entities that influence the model. As discussed earlier, the information in 
a BIM model could be a starting point for building digital twin models. 
Some approaches aim to convert all the data stored in an IFC into a 
knowledge graph [114]. Others believe that the IFC schema is complex 
and unable to cover the operational phase of the building lifecycle suf­
ficiently; as a result, a modular data integration framework is proposed 
that relies on several ontologies for data integration [115]. In the 
literature, it is accepted that knowledge graphs are inefficient for storing 
time series, and it is recommended that they be stored in a dedicated 
time series database [116].
Fig. 3. The diagram outlines the phases of a digital twin (DT) concerning the lifecycle phases of the real-world urban multi-energy system (UMES) asset and BIM 
processes, providing examples of applications and data sources that change throughout the UMES and DT asset’s lifecycle. The lifecycle is divided into pre-twin 
models, active-twin, and post-twin phases, highlighting design, operation, and decommissioning/material re-utilization, respectively. While pre-twin and post- 
twin phases rely heavily on static historical data, active twin relies on real-time sensor data.
B. Koirala et al.                                                                                                                                                                                                                                 
Advances in Applied Energy 16 (2024) 100196 
7 


---

Page 8

---

As illustrated in Fig. 2, UMES DT sources data across multiple scales 
of the physical system, encompassing technological components, infra­
structure networks, and sectorial interactions. In the use cases reviewed 
in this work, DTs can be created to represent assets and systems span­
ning different spatial and temporal scales. The complexity of handling 
multiple scales in a single twin establishes the need for a network of 
interconnected DTs instead of a single monolithic digital twin [117]. 
This means the digital twin developers must know the data models 
available to represent the domains and scales relevant to their DT. An 
in-depth discussion of DTs for the built environment, their requirements, 
abilities, and spatial scales is provided in [113].
3.2.2. Active-twin data sources
Real-time data connection often provides updates about a system’s 
state. The update cycle between a UMES DT and its physical counterpart 
is illustrated in Fig. 4. The UMES DT must be able to handle data with 
different modalities and contexts, which are collected at heterogeneous 
temporal and spatial scale resolutions. Furthermore, UMES DT should 
match and refine data along different modalities to provide compre­
hensive and reliable information to the corresponding decision-makers. 
It must then understand how this data influences long-term forecasting.
3.2.3. The post-twin as a data source
Supposing that a DT is maintained throughout the life cycle of UMES, 
asset managers can use the available information on assets and materials 
to connect to other applications and databases for reuse and second-life 
applications. Furthermore, the comprehensive data repository encom­
passing the entire lifespan of a DT can serve statistical purposes or be 
employed to train future DT models. This utilization facilitates 
leveraging historical and operational data to enhance predictive ana­
lytics and refine other DT frameworks, ensuring continual improvement 
and knowledge transfer across models. The post-twin as the data source 
for the decommissioning and re-use phase of UMES is further elaborated 
in Section 5.3.
3.3. Data handling and interface integration
Aheleroff et al. (2021) describes a DT Reference Architecture Model 
for Industry 4.0 [118]. This reference architecture sets DTs apart from 
standard models due to a time data connection. The reference standard 
defines the level of integration based on how this real-time connection is 
implemented. The levels of integration defined in the reference archi­
tecture include: Digital Model (no real-time), Digital Shadow (one way), 
Digital Twin (bi-directional), and Digital Predictive (bi-directional 
powered by distributed computing technologies). When considering the 
importance of real-time connection of UMES DTs, live data connection 
will mostly be obtained from meters and sensors installed across the 
UMES system.
Data is at the heart of the functionality of DTs. Effective handling of 
diverse data types—such as real-time sensor data, historical datasets, 
and forecast data—is essential to the operational success of DTs. Digital 
twins utilize advanced data fusion techniques to integrate these het­
erogeneous data sources into a coherent model, allowing for real-time 
monitoring and predictive analytics [119,120]. Data preprocessing 
steps, such as normalization, missing data imputation, and filtering 
[121], are employed to ensure data quality before use in the digital twin. 
The ability to process and manage these data efficiently ensures that the 
virtual twin remains an accurate and up-to-date representation of the 
physical energy system.
The integration of various modules within the digital twin is facili­
tated by a middleware layer using standardized communication pro­
tocols such as OPC-UA [122] and MQTT [123,124]. This layer ensures 
seamless interoperability between different system components and 
external data sources. These interfaces play an important role in 
achieving a modular and scalable architecture in UMES DTs. In addition, 
different methods are needed to address and overcome data gaps, which 
can arise due to sensor faults, communication failures, or data sparsity. 
Techniques such as interpolation, machine learning-based data recon­
struction, and data augmentation from historical datasets are applied to 
minimize the impact of missing data [125]. Additionally, real-time 
redundancy checks and fallback mechanisms can be implemented to 
maintain the continuous operation of the digital twin.
3.4. Ontologies and data schemas for UMES DTs
The contextual understanding of the integration layers of a digital 
twin can be augmented through the use of ontologies and established 
data models. DTs can be implemented to work in communication with a 
data architecture built on schemas that comply or make reference to 
such data models. The challenge data architects face when building a 
comprehensive DT framework, is enabling the twin to access the 
required data access without compromising performance. Domain 
models provide a basis for the physical representation of the system, 
allowing advanced querying and analytics, and meta-models can pro­
vide functional processes such as scenario and provenance tracking. This 
section gives an overview of data models that could be implemented to 
represent the key processes necessary for an UMES DT.
Over the past few years, ontologies have been seen as a critical 
Fig. 4. A digital twin of urban multi-energy system (UMES). Each image is a snapshot of the physical twin at a specific time. The snapshots represent the update cycle 
of the digital twin during distinct phases of its life. Snapshots are less frequent during the planning and decommissioning phases and more intensive during the 
operation phase. The performance of a UMES improves throughout its life as additional data is gathered and processed from the physical counterpart.
B. Koirala et al.                                                                                                                                                                                                                                 
Advances in Applied Energy 16 (2024) 100196 
8 


---

Page 9

---

technology for addressing heterogeneities and mitigating mis­
understandings and isolation, which can lead to a lack of clarity about 
activities, data, and information in a particular domain. Moreover, on­
tologies enable semantics-driven knowledge processing, which converts 
knowledge into tangible assets. Thus, ontologies are formal structures 
enabling acquiring, maintaining, accessing, sharing, and reusing data, 
information, and knowledge.
Knowledge management systems benefit from ontologies that 
semantically enrich information and precisely define the meaning of 
various information artifacts. Ontologies have been developed to facil­
itate knowledge sharing and reuse among different disciplines and 
research communities, such as advances in medicine, knowledge 
engineering, natural language processing, cooperative information sys­
tems, information integration, and software agents. We can conclude 
that ontologies provide the following: 
• A common and shared understanding of a specific domain and 
context.
• A 
human 
and 
machine-readable 
approach 
to 
knowledge 
management.
• An explicit conceptualization describing data meaning.
Adherence to standardized ontologies and data schemas enables 
interoperability and scalability of UMES DTs. Ontologies define the 
Table 2 
An overview of ontologies and their capability to represent the necessary elements of an urban multi-energy system digital twin (UMES DT). Green/tick: the majority of 
concepts are covered by the ontology. Yellow/dash: partial coverage. Red/cross: Limited coverage, in combination with an additional ontology, is necessary. *Includes 
extensions and submodules. Note that a limited or absent capability does not mean the ontology is inferior; it is just specialized in other areas.
B. Koirala et al.                                                                                                                                                                                                                                 
Advances in Applied Energy 16 (2024) 100196 
9 


---

Page 10

---

classes and properties that make up a domain, enable contextual un­
derstanding of data ingested by the twin, and can handle assumptions 
when simulating future scenarios. Ontologies can be used to organize 
the ingestion and querying of real-time and historical measurements of 
the physical twin. They handle the spatial hierarchies of the equipment, 
e.g., sub-meters and temporal aggregations, e.g., daily, hourly, 
minutely, etc. The individual domain ontologies and their relation to the 
components of UMES systems are discussed below.
3.4.1. Ontologies and data models relevant to UMES DTs
In the context of UMES, integrating ontologies and data models is 
pivotal to creating effective Digital Twins (DTs). No single ontology or 
data model can fully represent all the elements and functions of UMES 
DTs. The choice will depend on the specific functionality and re­
quirements of the twin. Therefore, a comprehensive and integrated 
approach is necessary to effectively select and utilize ontologies and 
data models that represent the relevant features of the UMES DTs. This 
section reviews the ontologies and data models relevant to domains 
containing the UMES classes shown in Fig. 2. Table 2 provides an 
overview of different semantic ontologies and their capabilities to 
represent the necessary elements of a UMES DT.
The Open Energy Ontology (OEO) is an example of domain 
ontology that supports energy system modeling by categorizing entities 
as either continuants or occurrents [126]. This classification allows for 
capturing dynamic processes and the impact on systems components 
integral to UMES’s function and operation. Similarly, the Smart Ap­
pliances Reference Ontology (SAREF) provides a framework for 
interoperability between smart appliances [127], focusing on 
device-centric approaches and extending to energy (SAREF4ENER), 
smart grids (SAREF4GRID) and smart city (SAREF4CITY) applications 
relevant to UMESs.
Another important ontology is the Semantic Sensor Network 
(SSN), which describes sensors and actuators regarding capabilities, 
measurement processes, observations, and deployments [128]. This 
ontology helps integrate sensor data from multiple sectors into UMES 
DTs [129]. The Common Information Model (CIM), a Unified 
Modelling Language (UML)-based standard developed by the Interna­
tional Electrotechnical Commission (IEC), offers a standardized 
approach for network modeling [130], aligning data structures used in 
UMES DTs with industry standards and facilitating integration across 
different operators. UML is a standardized modelling language used to 
specify, visualize, construct and document the artifacts of software and 
non-software systems.
CityGML, an open-data model from the Open Geospatial Consortium 
(OGC), represents urban infrastructures in 3D models, making it a 
valuable resource for detailed simulation of UMES [131]. CityGML 3.0 
contains a more extensive set of classes for semantic models to enable 
more accessible connections to different ontologies [132]. It has been 
used to support energy simulation of urban data models and store 
simulation configurations, highlighting its potential applications within 
UMES DTs [133]. Similarly, the SEMANCO ontology facilitates the 
creation of models of UMES [134,135], although its adoption beyond 
the initial project remains unclear.
The RealEstateCore (REC) and Brick ontologies focus on building 
systems and assets, providing uniform metadata representation within 
UMES [136,137]. Both ontologies are modular and interoperable, 
aligning with standards like Shapes Constraint Language (SHACL) and 
the Digital Twin Definition Language (DTDL) to ensure consistent 
modeling. Domain Analysis-Based Global Energy Ontology (DAB­
GEO) addresses the heterogeneity in energy ontologies, offering a 
comprehensive and modular framework for various energy domains 
[138].
Azure Industry Ontologies (AIO), part of Microsoft’s digital twin 
platform, incorporates domain-specific ontologies into their Digital 
Twin Definition Language (DTDL). At the time of writing, four ontol­
ogies are developed in open-source repositories: intelligent buildings, 
smart cities, energy grids, and manufacturing [139]. Despite some up­
date frequency and format complexity limitations, AIO aligns well with 
established ontologies like Brick and CIM, demonstrating its relevance 
for UMES DTs. Lastly, FIWARE Data Models provide open-source com­
ponents and data models for developing applications across smart cities 
and other domains, proving their suitability for UMES DT implementa­
tions [140].
Next, as a summary of the above-mentioned ontologies, Table 2
presents different semantic ontologies, their capabilities, and consider­
ations for integrating them into UMES DTs, considering different classes 
presented in Fig. 2. It highlights each model’s scope, features, licensing, 
and development status, offering insights into their relevance and 
applicability within the UMES context. This integrated approach un­
derscores the necessity of combining multiple ontologies and data 
models to create robust and effective UMES DTs.
3.5. Data transaction protocols supporting UMES DTs communication
UMES DT requires a hosting platform that manages the data 
communication between various data sources and data processing 
modules. Executing a DT is often managed by a primary solver that 
handles the communication between various secondary modules based 
on a standardized protocol. DT encompasses the concept of the IoT in 
connecting virtual and physical spaces [36,141–143]. IoT refers to 
interacting with objects without human intervention, providing intelli­
gent services [144–147]. ISO 23,247 can be considered when consid­
ering protocols for network communication in UMES DT [148–150].
3.5.1. DT and real-world communication
UMES utilizes multiple sensors to manage effective energy balance 
[88,89],. These sensors monitor the system’s status and performance 
and collect the necessary data to control energy production, storage, and 
usage. UMES sensors are bound to lightweight IoT network protocols (e. 
g., Zigbee [151–153], LoRaWAN [154–156], Bluetooth, etc.) in the 
physical twin representing the real-world layers. UMES DTs can consider 
the IoT platforms (e.g., oneM2 M [157,158], NGSI-LD [159,160], etc.) 
for collecting vast and diverse data. In addition, network communica­
tion protocols such as low-power, lightweight MQTT [123,124], HTTP, 
and CoAP [161] can also be considered.
3.5.2. DT and simulation model communication
Given that seamless communication between the simulation modules 
is an integral part of UMES DTs, the Functional Mockup Interface (FMI) 
[162] has also been the popular choice for standardizing communication 
within the DTs. FMI is a tool-independent standard for the exchange of 
dynamic models and co-simulation. These standards resolve communi­
cation issues by allowing various simulation modules to interact and 
exchange information efficiently, ensuring interoperability and cohesive 
operation within the UMES DTs. Resorting to FMI for co-simulation or 
model-exchange allows FMUs (functional mockup units) to communi­
cate promptly based on a standardized protocol. Such a setup facilitates 
interoperability between different simulation platforms. FMUs can be 
imported into a variety of simulation environments, which can be 
divided into two categories: 
(1) commercial toolboxes such as Dymola [163], Simulink [164], 
COMSOL Multi-physics, Ansys Twin Builder, and SimulationX 
[165];
(2) non-commercial toolboxes such as openmodelica [166], and 
Mosaik [167]
3.6. Summary of data management for UMES DTs
This review of data management shows that DTs can be built from 
various data sources. The data requirements will depend on the twin’s 
purpose and the physical counterpart’s condition. The approach also 
B. Koirala et al.                                                                                                                                                                                                                                 
Advances in Applied Energy 16 (2024) 100196 
10 


---

Page 11

---

depends on whether the physical counterpart exists or whether the 
UMES is in the planning phase. It is argued that a digital model of a 
conceptual future system cannot be twinned until the physical coun­
terpart is built. Nevertheless, existing processes, such as BIM, can be 
utilized to collect the information to create the Digital Twin during the 
planning phase.
Once the objectives and the case for a UMES have been established, 
several ontologies will be used to represent the functionality and 
knowledge generated by the DT. Adherence to standardized ontologies 
will facilitate interoperability and scalability; however, care must be 
taken to select and reuse the relevant ontologies wherever possible. The 
limited adoption of published ontologies implies that this is a chal­
lenging endeavor. The same message is valid for communication pro­
tocols; a mandatory feature of DTs is synchronization between the 
digital model and the physical counterpart. Without this, it is not a twin. 
Using documented communication protocols enables effective, secure, 
and efficient operation of DTs. Moreover, further development in data- 
sharing protocols is needed to ensure interoperability across diverse 
systems, data security and privacy, scalability, real-time processing and 
synchronization, and standardization of data formats. Ontologies and 
communication protocols were not created solely to serve the data needs 
of DTs; however, DTs could demonstrate the value, building upon a 
semantically robust foundation using established ontologies and data 
models.
Having established the importance of data and knowledge manage­
ment in UMES DTs, the next important aspect involves understanding 
the architectural frameworks that underpin these systems. The archi­
tecture of UMES DTs is central to their functionality, as it defines how 
data is processed, interpreted and utilized to support collaborative 
decision-making. The following section explores the various data pro­
cessing modules that form the foundation of UMES DT architectures, 
ranging from highly interpretable open-box models to more opaque 
closed-box models, along with hybrid approaches. Next section will 
provide insight into the different modeling techniques and their roles in 
achieving accurate and efficient UMES DTs.
4. UMES DT architectures
In the core of UMES DT architecture sit several data processing 
modules, forming an ecosystem of various digital services that address 
the purpose of the DT. The architecture of these data processing modules 
can be divided into four categories, i.e., (1) open-box (white-box) 
models, (2) semi-open-box (grey-box) models, (3) closed-box (black- 
box) models, and (4) a combination of the models (hybrid) [168]. At one 
end of the model interpretability spectrum sit the open-box models. 
Open-box models (also referred frequently as equation-based or 
physics-based models, e.g., TRNSYS, EnergyPlus) are developed based 
on clear and explainable theoretical structures that represent physical 
phenomena (e.g., laws of heat and mass transfer) and can be deployed 
without observations of a system’s performance. Around the center of 
the model interpretability spectrum lie semi-open-box models (e.g., 
CityEnergyAnalyst [169]). Semi-open-box models rely on a partial 
theoretical structure and require data for completion; hence, 
resistance-capacitance 
(RC) 
models 
are 
frequently 
used 
for 
semi-open-box 
modeling 
[170]. 
The 
theoretical 
structure 
of 
semi-open-box models is coupled with observations (data) to identify 
and enhance prior knowledge about the model parameters. Modelica is 
one of the leading platforms for creating semi-open box energy models 
[171]. Closed-box models (e.g., Buildingenergy.ninja [172]) sit at the 
far end of the model interpretability spectrum, with limited trans­
parency. Closed-box models solely rely on observations of a system’s 
performance and do not necessarily provide explainable knowledge 
about their internal workings.
The distinction between open, semi-open, and closed-box models can 
be attributed to the abstraction level employed in each method. In the 
context of UMESs, this translates to the desired level of interpretability. 
However, high-level abstraction is conditioned on the availability of 
measurements during the systems’ operation. 
- Open-box models are based on equations and are more detailed and 
transparent. They aim to provide a deep and complete understanding 
of the system. Each component or equation of an open-box model can 
be viewed, modified, updated, and extended. On the contrary, 
closed-box models are abstract and obscure, often based on simple 
and modular transfer functions that collectively mimic the behavior 
of a complex system.
- Closed-box models are beneficial when the inner-workings of the 
system are not well-understood or when the focus is on prediction 
rather than understanding the underlying mechanism of the system.
- Semi-open-box models share qualities of open-box and closed-box 
models, providing a tradeoff between the interpretability of open- 
box models and the computational efficiency of closed-box models. 
Users of semi-open-box models can access some internal details of 
the system, but not all.
Despite the general descriptions above, the distinction between the 
three modeling approaches has diminished in recent years. Open-box 
models can be fine-tuned with measurements when there is a lack of 
confidence in the prior knowledge. On the other hand, semi-open-box 
models can host various levels of abstraction, from fully detailed 
models to encapsulated equations. Similarly, it has long been believed 
that closed-box models often provide a high-level of abstraction and 
mask the system’s internal working, which they mimic. However, with 
the advancements in physics-constrained closed-box models, the 
distinction between semi-open and closed-box models has faded [173].
No single model is the perfect solution for all UMES DT applications, 
as each model architecture has certain purposes with advantages and 
drawbacks. For instance, open-box models provide insights into every 
part of a system, even where physical data loggers are not installed. 
Meanwhile, closed-box models can only provide predictions if mea­
surements are already available and representative. Open-box models 
can be executed at different temporal resolutions, including those 
different from the measurements [174]. Semi-open-box models provide 
more accurate predictions than open-box models while being more 
robust to unforeseen events than closed-box models. Closed-box models 
can offer higher accuracy in forecasts when compared to open and 
semi-open-box models [175].
Regardless of the chosen architecture, it is imperative that the model 
performs well in real-world setups and is capable of generalizing to 
unforeseen events. This capability is often called high-fidelity perfor­
mance and is crucial for evaluating system performance (e.g., robust­
ness, flexibility, and resiliency) in extreme scenarios [176]. It is 
important to note that high-fidelity performance is an imprecise 
description of a model’s function. Thus, case-specific quantitative met­
rics are vital in choosing the proper model architecture for each use case. 
Such criteria are often chosen based on the application of the digital 
twin [174]. For instance, models with high-levels of uncertainty can be 
unsuitable for implementing and benchmarking MPC (model predictive 
controllers). Thus, rule-based controllers (RBC) will inevitably become 
the preferred choice for such scenarios [177]. This issue affects explicitly 
pure open-box models that are not calibrated to measurements and, 
thus, suffer from the “performance gap” phenomenon. In such cases, 
semi-open-box and closed-box models – developed and fine-tuned based 
on measurements – can mimic the physical counterpart accurately and, 
therefore, appear to be the preferred solutions for digital twin model 
architectures [178]. A comparison of different architectures and their 
features is provided in Table 3.
Although many articles discuss the high-fidelity feature of the digital 
twin, the execution time of the underlying modeling process is rarely 
mentioned. Occasionally, there are incompatible needs for the fidelity of 
the virtual representation, and therefore, multiple DTs of different 
abstraction levels are recommended [179]. Other means to reduce 
B. Koirala et al.                                                                                                                                                                                                                                 
Advances in Applied Energy 16 (2024) 100196 
11 


---

Page 12

---

computation complexity include using machine learning techniques to 
build a surrogate model [180]. However, interpretability and extrapo­
lation with machine learning techniques are often considered insuffi­
cient. Incorporating known physical equations into the black-box neural 
network can provide a favorable balance between both sides and ensure 
trust when managing critical infrastructure [181].
Two aspects differentiate UMES DTs from classical UMES simulation 
platforms: (1) the capability of data communication between different 
DT modules and the physical counterpart and (2) the capability to 
actively override the input variables to the DT modules during data 
processing [182]. UMES DTs can be developed from open to closed-box 
models, often consisting of different engines (solvers) that may run at 
dissimilar temporal resolutions.
The literature is rich with studies that adopt various configurations 
of the abovementioned model architectures. DTs of energy systems have 
been devised and trialed at building to urban scales by integrating data 
streams with open, semi-open, and closed-box models or a combination.
4.1. Open-box models
Open-box models require validation against measurements to assess 
their reliability. The validation is often followed by a calibration process 
to reduce the performance gap as much as possible. While calibration 
can be applied to both the model and the inputs, fine-tuning the latter is 
more common. Studies have coupled real-time (as well as future) 
weather data with EnergyPlus through co-simulation to visualize energy 
demand, water consumption, and the global warming potential [183]. In 
another case study, fine-tuned open-box models were developed in 
MATLAB and then coupled with TRNSYS and CONTAM software to 
create a digital twin of a complex pipe-integrated shell roof system. 
Another great platform is the spawn of EnergyPlus (SOEP), which cou­
ples Modelica with EnergyPlus tools [184,185]. This coupled modeling 
allows data communication between different software, where each 
software is tailored for simulating one module of the overall integrated 
system [186].
4.2. Semi-open-box models
Semi-open-box models are often sought when the excessive compu­
tational load of pure open-box models must be avoided, yet model 
interpretability is highly desired. Vering et al. (2019) opted for semi- 
open-box models [163] in the Modelica simulation environment for 
developing and simulating dynamic systems, given the modularity of 
Modelica Libraries [187]. The model was executed in a Docker virtual 
environment to ensure interoperability with different operating systems 
[188]. Similarly, Clausen et al. (2021) used the Modelica environment to 
create semi-open-box modules for building systems and executing sim­
ulations [189].
4.3. Closed-box models
In cases where the physical environment is too complex to model and 
interpretability is less important, studies opt for pure closed-box models. 
The application of closed-box models with online updates based on real- 
time data streams has proven suitable for replicating the performance of 
HVAC systems and evaluating alternative operation scenarios [190]. 
Given that closed-box models benefit from a generic architecture, 
transferability to different energy sectors is facilitated when opting for 
end-to-end data-driven architectures [172].
Given that the DTs may consist of various modules with dissimilar 
levels of complexity, hybrid models are becoming more prevalent [191,
192]. For instance, a combination of semi-open and closed-box models 
has been utilized to benchmark the load-shifting potential of MPCs 
through storage systems [190]. It has been argued that a combination of 
open and closed-box models yields more robust DTs and, therefore, is a 
more suitable solution for benchmarking the operation and control of 
energy systems [193]. On an urban scale, Srinivasan et al. (2020) 
resorted to an open-box model for seamless data transfer for real-time 
demand response. In this study, open-box modules have also been fed 
with future weather data as a surrogate simulation engine to support 
decision-making through closed-box models [194].
As a subcategory of closed-box models, Artificial Intelligence (AI) has 
displayed exciting potential for designing and operating digital twins for 
UMES. The utilization of AI in developing digital twins for urban energy 
systems spans from the microscale of individual buildings to the 
macroscale of districts and entire cities. At the building level, digital 
twins utilize AI to enhance energy efficiency, predict maintenance 
needs, and facilitate the integration of renewable energy sources, as 
demonstrated by Testasecca and Lazzaro (2023) in their exploration of 
smart energy networks [195]. Expanding to the district and city scales, 
AI-enriched digital twins offer sophisticated management of energy 
networks, promoting sustainability through predictive analytics and 
boosting resilience against environmental challenges [15]. Furthermore, 
the incorporation of AI with digital twins for the development of hybrid 
and sustainable energy systems is explored by Khan et al. (2022), 
illustrating the potential for optimization and sustainability in energy 
systems [196].
The utilization of AI in the development and management of digital 
twins for urban energy systems also presents several limitations. One of 
the primary concerns is data privacy and security, as the integration of 
AI with digital twin technology requires handling sensitive data, 
potentially exposing it to cybersecurity risks [197]. The complexity of 
accurately modeling and simulating the intricacies of urban energy 
systems poses another significant challenge, demanding advanced 
computational resources and sophisticated algorithms [198]. Moreover, 
these digital twins require continuous data collection and processing to 
reflect real-world changes accurately, which can be resource-intensive 
[199]. The quality and availability of data become crucial factors in 
the effectiveness of these systems, particularly in complex urban envi­
ronments with layered infrastructure networks [200]. Lastly, the po­
tential for algorithmic biases in AI models can lead to skewed outcomes, 
necessitating careful calibration and oversight. The accuracy of AI 
models is often called "impressively high," with accuracies over 95 %. 
However, AI systems would render unreliable compared to 
safety-critical systems that are certified out to 5–6 decimal points (i.e., 
99.99999 %) [201]. Most of the limitations specified here for the 
AI-driven DTs also apply to DTs in general, particularly data privacy and 
security, computational expenses, sophisticated algorithms, and 
resource intensity.
Table 3 
A comparison of distinctive features and characteristics of urban multi-energy 
system (UMES) digital twin (DT) architectures, open-box, semi-open-box, and 
closed-box models.
Open-box
Semi open-box
Closed-box
Inputs
System 
characteristics, 
time-series data
System 
characteristics, 
Time-series data
Time-series 
data
Outputs
Time-series data
Time-series data
Time-series 
data
Transparency and 
abstraction
Transparent
Customizable
Abstract
Spatio-temporal 
Resolution
Limited by the 
simulation tool
Limited by the 
simulation tool
Limited by the 
measurements
Manual labor
Medium-High
Low-Medium
Low-Medium
Simulation time
Medium-High
Low-Medium
Low-Medium
Computing 
resources
Low-Medium
Low-Medium
Medium-High
Accuracy of 
model
Low-Medium
Medium-High
Medium-High
Performance 
fidelity
Medium-High
Medium-High
Low-Medium
Generalization 
capabilities
Medium-High
Medium-High
Low-Medium
B. Koirala et al.                                                                                                                                                                                                                                 
Advances in Applied Energy 16 (2024) 100196 
12 


---

Page 13

---

To summarize, the UMES DTs architecture consists of several data 
processing modules categorized into open-box, semi-open-box, closed- 
box, and hybrid models. Open-box models are transparent, based on 
theoretical structures, and require no system performance observations. 
Semi-open-box models combine theoretical structures with observa­
tional data for enhanced parameter identification. Closed-box models 
rely solely on system performance data with limited transparency. Each 
model type has strengths and limitations regarding interpretability, 
computational efficiency, and accuracy. The distinction between these 
models diminishes with technological advancements, allowing for more 
robust and flexible digital twin implementations. Regardless of the 
chosen model, ensuring high-fidelity performance in real-world sce­
narios remains crucial. The integration of AI further enhances the ca­
pabilities of digital twins, although it introduces challenges related to 
data privacy, computational resources, and potential algorithmic biases.
With a solid understanding of UMES DT architectures, the next sec­
tion focuses on how digital twins can be applied to different life-cycle 
phases of urban energy systems. From initial planning and design to 
ongoing operation and eventual decommissioning, digital twins offer a 
wide range of applications to optimize each phase of UMES. However, it 
is essential to recognize that the integration of DTs across lifecycle 
phases is still evolving, and greater interoperability between these 
phases can unlock further potential. Next section explores how DTs 
contribute to improved energy planning, operation and decommission­
ing, providing insight into both the opportunities and challenges that 
arise with it.
5. UMES DT application to lifecycle phases
By leveraging DTs, UMES can improve strategic energy planning, 
dynamically manage energy supply and demand, enhance energy effi­
ciency, and increase the resilience of urban infrastructure. Applications 
of DTs in different lifecycle phases of UMES, from planning and design to 
operation and decommissioning, can exploit distinct opportunities and 
challenges, as discussed in the sub-section below. They are also expected 
to offer higher flexibility, scale, and interoperability beyond existing 
solutions such as Building Information Modelling (BIM), Computer- 
Aided Design (CAD), Geographic Information System (GIS), Energy 
management systems (EMS), and Building Management Systems (BMS) 
[32]. UMES DTs build on these existing solutions by integrating and 
enhancing data exchange and decision-making capabilities across these 
platforms. It should be noted that today DT applications for design, 
operation, and decommissioning phases are not interoperable silos. Data 
science and analytics development are needed to connect between 
different life cycle phases, further maximizing the benefits of DT ap­
plications. By applying DTs in different UMES lifecycle phases, energy 
system actors, such as urban planners, policymakers, engineers, citizens, 
and energy communities, can better understand the complexities and 
opportunities of such systems.
5.1. Planning phase
During UMES planning, DTs can help consider energy system ar­
chitecture, technology selection, and stakeholder engagement. With the 
widening applications, UMES DTs can act as a “base truth” and “visual 
basis” to enhance the collaborative planning process, addressing the 
inputs of various energy system actors such as city, utilities, energy 
planners, and project developers as well as facilitating their evaluations 
and decision-making process in UMES design. The UMES DTs will act as 
an unbiased basis to test the alignment of proposed socio-techno- 
economic and institutional design choices in different transition trajec­
tories and scenarios with the energy and emission performance 
objectives.
However, the DT application in UMES planning is new [64,65]. 
Table 4 summarizes some examples of applications of DTs in the plan­
ning phase of UMES. The table lists digital twin projects from diverse 
locations, including the Orkney Islands, Anzio port, Docklands, Zürich, 
and Singapore, each serving distinct purposes like reducing carbon 
footprint, achieving zero energy districts, urban planning, and collabo­
rative decision support. The projects utilize various platforms such as 
IES, Green building studio, Unity3D, GIS, and Virtual Singapore to 
effectively implement and visualize the UMES DTs.
Orkney Islands DT represents a complex environment of buildings, 
energy systems, and other infrastructures, including their in­
terrelationships and the impact of changes on system performance. 
Using scenario analysis, the UMES DT helps to understand how a com­
bination of energy efficiency measures and local renewable energy re­
sources could create conditions for a zero-carbon community [66]. The 
challenges associated with the Orkney Island DT were installing new 
heat meters, oil meters, electricity meters, and weather sensors to pro­
vide a clearer picture across the island portfolio. The main limitation of 
the Orkney Islands DT is that it is not built in an open-source 
environment.
Anzio port DT supports the transformation of port areas to zero- 
energy districts in the Lazio region of Italy. The focus is on energy- 
saving procedures and strategies as well as renewable energy integra­
tion for sustainable mobility [202]. The DT supports decision-making 
among port stakeholders using integrated multi-scale digital data sour­
ces from BIM and GIS to simulate strategies for energy performance 
improvement at the port area. Anzio port DT’s limitation is the inte­
gration of multi-scale digital simulations into real-time data. Further 
expansion of DT extending the harbor representation can improve its 
environmental and economic management.
Docklands DT is an open-source platform that can be used to gather 
citizens’ feedback on urban planning and policy decisions [203]. It has 
six layers: terrain, buildings, infrastructures, mobility, digital layer 
Table 4 
Examples of digital twins (DTs) application to the planning phase of urban multi- 
energy system (UMES). It covers various digital twin projects across multiple 
locations, highlighting their geographical scale, purpose, and platform/mid­
dleware used.
Location
Geographical 
scale
Purpose
Platform/ 
middleware
Reference
Orkney 
Islands
District
Reduce carbon 
footprint and 
energy 
consumption and 
maximize 
renewables
Integrated 
Environmental 
Solutions (IES)
[66]
Anzio port
District
Zero energy 
district, energy 
savings, 
renewables 
integration, 
sustainable 
mobility
Green building 
studio, In-sight, 
Revit, Archi 
CAD, 
Infraworks, 
CFD
[202]
Docklands
District
Urban planning, 
energy usage
Unity3D, 
WebGL
[203]
Zürich
City
Geodata 
repository for 
urban planning, 
platform for 
visualization and 
collaboration
GIS, geoportal, 
Virtual Zürich
[34,204,
205]
Singapore
City
Collaborative 
decision support 
system, Urban 
planning, 
analysis of the 
potential for solar 
energy 
production, 
communication, 
and visualization
Virtual 
Singapore
[206,207]
Helsinki
City
Urban planning
CityGML, 
Virtual Helsinki
[207–209]
B. Koirala et al.                                                                                                                                                                                                                                 
Advances in Applied Energy 16 (2024) 100196 
13 


---

Page 14

---

(smart city), and virtual layer (digital twin). The Docklands DT offers an 
online interaction platform for citizens, researchers, and city councils. It 
helps citizen engagement as citizens can easily tag problem areas in the 
city and request changes, providing valuable feedback for urban plan­
ning. Some datasets are interpolated due to the availability of only 
aggregated data at Dublinked open data source [210], leading to less 
accurate simulations. Further limitations of current DT include poor 
representation of older buildings, open spaces, and some infrastructures 
and the exclusion of some urban mobility.
Zürich 4D is a DT for visualizing structural development in space and 
time, including future scenarios, and acts as a source for historical and 
future data [34]. The City of Zürich uses its DT in the areas of envi­
ronment (noise, air pollution), energy (solar potential analysis), and 
urban planning [204]. It is also used explicitly to develop the municipal 
development plan of Zürich. It can be used for location-based collabo­
ration with internal (city departments) and external partners. The data 
sets of Zürich 4D are also available at Open Government Data. The 
Zürich DT also enables digital participatory processes in Urban plan­
ning, e.g., Minecraft computer games and web-based 3D interactive 
tools. It offers new possibilities for collaborative discussion and 
decision-making in urban planning. The limitation of Zürich 4D is that it 
is not yet integrated to the energy system. Nevertheless, it demonstrates 
the key components of a digital twin relevant to UMES, specifically the 
visualization of structural development over space and time, which 
could potentially evolve to incorporate energy systems.
Singapore’s digital urban climate twin, which also considers the 
energy system and its anthropogenic heat emissions, has been developed 
to demonstrate how measures like electric vehicles and tree cover can 
reduce urban heat [35]. It integrates computational models such as 
environmental, land surface, building energy, etc.) as well as regional 
and micro-scale climate models. Exploring what-if scenarios, it can be 
exploited by urban planners and policymakers in their decision-making 
processes. Challenges include validating the DT through environmental 
monitoring to develop reliable model simulations in an urban context.
The digital twin of Helsinki is a virtual replica of the city’s envi­
ronment, operation, and changing circumstances. It combines informa­
tion technology services, open data, and continuous updates of 
information. Helsinki DT contains information about renewable energy 
potentials, possibilities for energy renovations, water consumption, 
district heating and electricity throughout the region. City planners, 
housing companies, residents, and energy service providers can benefit 
from its energy data on buildings, simulated building heating demand, 
solar energy, and geothermal potential. It is being used to illustrate 
upcoming plans and to co-create new city functions in collaboration 
with citizens [207]. Despite the potential of DT for urban planning, 
organizational, technical, and data integration issues hinder its exten­
sive deployment [208].
The DTs reviewed here offer insights into both the capabilities and 
limitations of current platforms in supporting UMES planning. For DT to 
fully support UMES, it must integrate not only urban infrastructure data 
but also energy system data. DTs of Orkney Islands, Docklands, and 
Singapore demonstrate the importance of this integration, enabling 
decision-making that accounts for energy consumption, emissions, and 
system performance. Singapore DT illustrates the importance of scal­
ability and the ability to integrate a wide range of data sources. A UMES 
digital twin must be flexible enough to evolve with changing urban 
energy needs and technological advancements. In summary, while 
existing digital twins have made substantial progress in supporting 
UMES planning, there are still gaps regarding full UMES integration. 
Future development should focus on enhancing energy system data 
integration, improving scalability, and fostering collaboration to realize 
the full potential of digital twins for urban energy system 
transformation.
5.2. Operation phase
UMES DT application in the operation phase emphasizes real-time 
monitoring, management, and optimization to maintain system perfor­
mance according to design targets. UMES increasingly integrates 
distributed generation, sensing, and actuation at technology and infra­
structure levels. The efficient operation of these systems necessitates 
significant flexibility, which can be sourced from sector coupling [12] 
and active engagement of energy usage. The latter requires incorpo­
rating the interaction between humans and technical systems in UMES 
DTs. Extreme events, such as geopolitical tensions, can significantly 
change human perceptions and behaviors regarding energy systems, 
leading to sudden changes in energy consumption patterns. This needs 
to be considered holistically in the UMES DT. In addition, future UMES 
will feature high automation levels and complexity, which raises the 
question of how humans, at the heart of UMES, interact with such sys­
tems efficiently and transparently. In both cases, the human dimension 
should be holistically incorporated into DTs to ensure that human re­
sponses and decision-making processes are accurately represented, 
allowing for more resilient and adaptable UMES.
To this end, we provide a detailed comparison of various applications 
of DTs in terms of system boundaries, the purpose of the application, the 
inclusion of humans, the update frequency of information, and the 
estimated technology readiness level (TRL) [211], as shown in Table 5. 
These use cases focus on the operation phase of UMES across multiple 
locations and geographical scales, including projects in Salamanca, 
Montreal, Dübendorf, Grafton, Florida, and Gelderland.
Table 5 shows that many of the envisioned values of DTs are closely 
linked to the operation of cyber-physical UMESs and the extent to which 
human interaction is incorporated. These applications include, but are 
not limited to, predictive maintenance or control, testing of new oper­
ational strategy [213], reliability, fault detection and diagnostics (FDD) 
and cyber-security assessment [214], education and training, and 
disaster management [22]. Although the term "digital twin" is not al­
ways explicitly mentioned in those use cases, core concepts of DTs are 
captured. A UMES DT prototype has been developed in [213], aiming at 
state estimation for power system operations, addressing the bottleneck 
caused by the need for extensive real-time data collection. The prototype 
was used to generate pseudo-measurements, which can be used to 
optimize DER operations for distribution voltage regulation. A digital 
twin has been developed [214] to detect coordinated cyber attacks on 
increasingly digitalized networked microgrids. When combined with a 
resilient control algorithm, this approach helps mitigate the impacts of 
such attacks on the system. Beyond sensing and actuation of the physical 
system, the integration of humans is addressed in [215], which in­
troduces a game-based approach to facilitate human-machine interac­
tion and promote behavioral changes that enhance energy efficiency. 
The digital twin in [216] focuses on thermal comfort study by leveraging 
real-time sensing and virtual reality to engage humans in an immersed 
environment. Moreover, the digital twin developed in [217] focuses on 
benchmarking advanced control algorithms and enables the evaluation 
of performance gaps under realistic conditions. Reference [218] in­
vestigates demand response mechanisms for distribution network 
management, utilizing a hardware-in-the-loop test platform based on 
real infrastructure to evaluate the effectiveness of control algorithms 
and their practical implications. Lastly, a disaster city digital twin has 
been envisioned in [219], representing a unifying framework to inte­
grate data collection, analysis, and decision-making for disaster man­
agement. The proposed framework not only considers data collection on 
the physical infrastructure but also integrates humans via social sensing.
Despite their varied use across scales and regions, DTs often show 
low TRLs, ranging from conceptual proposal [219] to prototyping at the 
district level [213]. A notable gap in many cases is the lack of consid­
eration for human factors, although emerging interaction mechanisms, 
such as social sensing, are proposed in [219]. Information from such 
mechanisms can be asynchronous and does not necessarily need to be 
B. Koirala et al.                                                                                                                                                                                                                                 
Advances in Applied Energy 16 (2024) 100196 
14 


---

Page 15

---

communicated simultaneously, as is required in physical system use 
cases [214,218].
Moreover, the geographical boundary of existing applications of 
UMES DTs in the operation phase is mainly at the building and district 
levels, indicating potential scalability challenge. These challenges are 
likely related to the difficulty in collecting system-related information 
and efficient modeling pipelines. For example, the open-box modeling 
approach in [167] requires construction details and year-long time se­
ries data. Such observations suggest that future research must provide 
tools to streamline information collection and scalable and computa­
tionally tractable modeling procedures. Additionally, there is often a 
siloed approach within disciplines, where one field may oversimplify 
another. This discipline-specific approach may hinder a holistic inte­
gration of DTs at different levels and a full representation of the oper­
ational stage. For example, real-time simulators with high-fidelity 
models have been used to mirror the operational environment, 
providing a virtual testbed for advanced control and system manage­
ment strategy [212]. However, the infrastructure-level simulators sur­
veyed in [212] tend to abstract buildings and districts as nodes, which 
creates a barrier to incorporating human interactions. Further research 
is needed to bridge the gaps between disciplines and their traditional 
representations of each other, ensuring a more comprehensive integra­
tion of DTs that includes both the technical and human dimensions.
The applications of DT in UMES differ notably between the planning 
and operation stages. DTs can be used for long-term forecasting and 
infrastructure design in the planning stage. In contrast, they are more 
commonly utilized for real-time system monitoring and management in 
the operational stage. Also, the availability and data types used to up­
date the DTs differ in both cases. In the planning stage, there is often a 
reliance on hypothetical or projected data, leading to a greater need for 
approximation and extrapolation. By contrast, the operation stage 
typically involves real-time or near-real-time data, allowing for more 
precise and accurate updates to the DT.
Furthermore, the response to the latest information in the planning 
stage has a significantly larger time lag, whereas DT in the operation 
stage responds on a much smaller time scale. It is necessary to point out 
that current DT development in the planning and operational stages are 
typically treated separately. However, this approach can lead to in­
efficiencies and missed opportunities for insights that could be gained 
from a more integrated approach. Future research should strive to 
connect the flow of data collection and decision-making in both stages to 
achieve higher synergies. For example, data and insights gathered dur­
ing the operational phase could inform adjustments in long-term 
planning.
5.3. Decommissioning, reuse, and circular economy
The focus of UMES design so far has been on planning and operating 
new infrastructures. However, to enhance resource recovery and inte­
grate circular engineering principles, the decommissioning of UMES 
should already be considered in the design phase [218–222]. In reuse 
and decommissioning, various data sources are commonly used, 
including water networks, sewage plants, telecommunication systems, 
power networks, BIM models containing architectural, structural, and 
system data, city-scale geometry models, and geo-coded sensor data. 
The application of DT during the operational stage significantly facili­
tates the end-of-life phase. DT applications for reuse and decom­
missioning play a crucial role due to the following reasons: 
- For end-of-life management, information on how the assets were 
used and to what capacity is needed [219]. DT can be used in pre­
dictive maintenance, which is state-dependent and implies that at 
the designated end-of-life, it is possible to predict the asset’s state. 
For example, companies in several countries, including Switzerland, 
offer PVs for leasing and buy-back programs. It is vital to know the 
state of the product-service models for reuse.
- The challenge concerning UMES is that the DT is federated or 
aggregated of multiple assets and asset classes. So, it is essential to tie 
in operations and end-of-life or decommissioning. For example, 
suppose you are modeling local grid energy and know that 20 % of 
your PVs must be decommissioned or replaced. In that case, you need 
the model to adjust and reallocate energy demands.
- DT can contribute to tracking, recycling, and management of con­
struction waste [221].
There are no concrete instances where DTs have been employed for 
reuse. There are two significant obstacles in this regard. Firstly, DTs are 
still relatively new, and the existing examples primarily concentrate on 
energy rather than materials. Since reuse is a developing practice, it will 
likely take some time before real-life DT implementation occurs, as reuse 
and DTs must evolve independently. Nevertheless, DT implies high- 
fidelity/volume of data. If a DT is maintained at the end-of-life, asset 
managers can use the information to connect to other applications and 
databases (like a reused material marketplace).
DTs also contribute to the circular economy by promoting the reuse 
and repurposing of assets. By capturing detailed information about a 
building or infrastructure, including its design, materials, and compo­
nents, DTs can facilitate the identification of potential reuse opportu­
nities. This includes assessing the feasibility of deconstructing and 
repurposing components or entire structures, promoting a more sus­
tainable construction approach, and reducing waste generation.
Moreover, DTs enable improved collaboration and communication 
among stakeholders in the built environment. With a shared digital 
representation, designers, architects, engineers, facility managers, and 
other professionals can collaborate more effectively, exchange infor­
mation, and simulate different scenarios. This enhanced collaboration 
streamlines processes, optimizes resource allocation, and supports 
implementing circular principles at various stages, from design to 
operation and maintenance. Moreover, the life-cycle data set of DTs can 
be used to train future DT applications.
Table 5 
Overview of digital twin (DT) applications in the urban multi-energy system (UMES) operation phase. Different UMES DTs are contrasted based on geographical scale, 
purpose, human interaction, models, and TRL level.
Location
Geographical 
scale
Purpose
Human in the 
loop
Communication
Model
TRL
Ref.
Salamanca, ES
Building
Behavioral change for energy saving
Yes
Both synchronous and 
asynchronous
Closed box
3-4
[211]
Montr´eal, CA
Building
Thermal comfort assessment
Yes
Synchronous
Semi-open 
box
3-4
[212]
nestli, Dübendorf, CH
Building
Controller benchmarking and flexibility 
quantification
No
Synchronous
Open box
3-4
[167,
213]
ProDROMOS, Grafton, 
USA
District
Monitoring and testing
No
Synchronous
Open box
4 – 6
[214]
Florida, USA
District
Cyber security testing
No
Synchronous
Open box
2-4
[215]
GECN, Gelderland, NL
District
Primary voltage control
No
Synchronous
Open box
3-4
[216]
-
City
Disaster management
Yes
Asynchronous
Closed box
1
[217]
B. Koirala et al.                                                                                                                                                                                                                                 
Advances in Applied Energy 16 (2024) 100196 
15 


---

Page 16

---

After examining the various lifecycle applications of UMES DTs, it is 
important to reflect on the broader implications and the challenges that 
arise from their deployment. The discussion in the next section will 
delve into the complexities associated with advancing UMES DTs, 
considering socio-technical dynamics, interoperability, cybersecurity, 
and scalability. It will also explore how data management across life­
cycle phases plays a critical role in ensuring seamless real-world inte­
gration, and how digital twins can facilitate the transition toward 
decarbonized and resilient urban energy systems. The following section 
will provide a critical assessment of the current state of UMES DTs, 
outlining the advancements and identifying gaps that need to be 
addressed for future developments.
6. Discussion
The advancement of DTs for UMES requires a comprehensive 
approach that considers the multi-faceted nature of such systems, 
including socio-technical complexities, interoperability, cybersecurity, 
and scalability challenges. As UMES DTs evolve, the need for system-of- 
systems approaches becomes imperative, demanding coordinated and 
collaborative efforts across sectors and disciplines. DTs must align with 
real-world data connection requirements, ensuring the accuracy of vir­
tual representation and facilitating seamless information exchange 
among subsystems.
Data collection and management are pivotal across UMES lifecycle 
phases and corresponding pre-twin, active, and post-twin phases of its 
DTs. While operational phases require real-time data connections, 
planning and decommissioning phases benefit from static and historical 
data sets. This review highlights advancements in integrating and pro­
cessing data in UMES DTs, encompassing data gathering, modeling, 
simulation, optimization, and visualization. DTs provide information for 
UMES through continuous validation and integration of heterogeneous 
data sources. Different DT components capture, analyze, and interpret 
data to enable collaborative and informed decision-making. The UMES 
DT should also be able to notify when the physical twin must be 
decommissioned. Yet, continuing updates throughout the decom­
missioning process might not be feasible. Even if possible, what data 
should be updated and how this connection should be maintained must 
be further explored. DTs also should develop the inherent ability to 
complement poor and low-quality data.
The interoperability of DTs across UMES lifecycle phases is crucial 
for future development. No single model fits all applications; choosing 
between open-box, closed-box, or semi-open-box models should align 
with specific operational needs. Closed-box models are favored for their 
efficiency and predictive accuracy. UMES DTs also play a pivotal role in 
steering energy systems toward decarbonization goals, offering oppor­
tunities for enhanced efficiency, sustainability, and resilience through 
improved planning and optimized operations. DTs-enabled co-simula­
tion frameworks can also facilitate the reuse of sophisticated tools across 
multiple sectors.
However, the digitalization of UMES introduces cybersecurity chal­
lenges, necessitating robust assessments of cyber threats as systems 
become increasingly interconnected. Addressing these concerns requires 
standardized and secured interfaces. Furthermore, as the scale of the 
physical system extends, the computational demands necessitate a 
distributed cloud computing approach to manage the growth effectively. 
Fully digitalized energy systems can be costly, and they often must go 
through the resistance of utilities and customers.
Furthermore, integrating social dimensions into UMES DTs is crucial 
for understanding user behavior, ensuring public acceptance, and 
aligning with societal expectations. This holistic approach aligns tech­
nical potential with community engagement and societal expectations.
While recent advancements in platforms and tools show promise, 
particularly in operational and planning phases, there remains a need to 
explore reuse and decommissioning phases comprehensively. Estab­
lishing clear standards and definitions for UMES DTs is essential for 
maximizing their potential across diverse urban energy scenarios. In 
conclusion, continuous refinement and development of UMES DTs are 
necessary to effectively accommodate the evolving landscape of urban 
energy systems and their management complexities.
After discussing the range of critical issues on development and 
integration of UMES DTs in this section, it is important to consider the 
future direction of UMES DTs and its broader implications. As UMES DTs 
continue to mature, the challenge will be in maintaining alignment 
between digital and physical system growth, especially as these systems 
become more complex and interconnected. The following outlook sec­
tion delves into the key trends, challenges, and opportunities that will 
shape the future development of UMES DTs, emphasizing the need for 
interdisciplinary collaboration, standardized communication protocols, 
and system-of-systems approaches to ensure the seamless integration of 
digital twins across diverse sectors.
7. Outlook
Digital twins (DTs) offer a comprehensive framework for analyzing 
Urban Multi-Energy Systems (UMES). As UMES DTs evolve, maintaining 
pace with physical system expansion necessitates a system-of-systems 
approach involving novel technologies, multiple sectors, actors, and 
collaborative decision-making. Achieving consensus and standardiza­
tion of interfaces between technical and social systems requires inter­
disciplinary collaboration. Effective communication between DTs and 
standardized approaches to their development is essential for seamless 
data exchange with other digital twins.
This review has highlighted a range of critical research questions on 
development and integration of UMES DTs that are pivotal to the future 
of intelligent energy systems. Addressing these questions is essential not 
only to push the technological boundaries but also to ensure the seam­
less integration of UMES DTs into complex urban environments. The 
following research outlook delves into key challenges surrounding data 
management, interoperability, modeling, economic and regulatory im­
pacts, socio-technical dynamics, lifecycle management, cybersecurity, 
and scalability. These questions aim to inspire new innovations and 
collaborative efforts across disciplines, driving the evolution of UMES 
DTs and their role in transforming urban energy landscapes: 
1. Data Management: What data management techniques can handle 
the volume, velocity, and variety of UMES data without over­
whelming DT capabilities or end-users? What are the optimal 
methods for integrating real-time sensor and meter data into UMES 
DTs? How frequently should these data be updated to balance system 
accuracy with computational efficiency?
2. Interoperability and Standardization: How can we develop uni­
versal protocols and standards to facilitate the seamless integration 
of DTs across different energy systems and sectors? What standards 
and protocols are necessary for seamless interaction between various 
digital twin platforms and UMES components?
3. Modeling Approaches: What strategies are the most effective for 
creating open and semi-open box models for UMES that balance 
transparency, adaptability, user interaction, system performance, 
and security? How can artificial intelligence and machine learning 
(closed-box models) enhance the predictive and operational capa­
bilities of UMES DTs?
4. Economic and Regulatory Impacts: What economic models and 
regulatory frameworks are required to support the adoption and 
scaling of DTs in UMES, encouraging innovation while protecting 
stakeholder interests? How can DTs improve the reliability and 
resilience of UMES, particularly in response to environmental and 
human-caused challenges? How can DTs shape regulatory and policy 
frameworks to promote equitable, cost-effective, and sustainable 
development of UMES?
5. Socio-technical Dynamics: How do social dynamics and stake­
holder engagement influence the design and acceptance of DTs in 
B. Koirala et al.                                                                                                                                                                                                                                 
Advances in Applied Energy 16 (2024) 100196 
16 


---

Page 17

---

different life-cycle phases of UMES? What methods can effectively 
integrate socio-technical aspects in UMES DTs? How can DTs 
improve human-machine interfaces and stakeholder engagement in 
UMES management?
6. Lifespan Availability, Decommissioning, and Reuse: What are 
the best practices for using DTs to manage UMES assets’ decom­
missioning and reuse phases, ensuring environmental compliance 
and cost efficiency? What strategies and technological innovations 
are needed to ensure the accessibility and functional relevance of 
UMES DTs throughout their lifecycle?
7. Cybersecurity Measures: How can DTs be fortified against 
emerging cyber threats associated with UMES’s increased connec­
tivity and complexity? Which best practices and security measures 
are critical for protecting UMES DTs?
8. Scalability Challenges: As UMES grows in scale and complexity, 
what computational architectures will ensure that DTs remain 
effective and responsive to real-time data and simulation needs? 
How can DTs be designed to scale from individual system compo­
nents to the full extent of UMES without compromising 
functionality?
Addressing these pivotal questions demands an interdisciplinary 
approach integrating technological innovation with policy, human fac­
tors, and economic considerations. Insights gathered from these future 
research will critically influence the emergence of UMES, making them 
more adaptive, secure, and integrated into society. This comprehensive 
exploration will enhance the deployment and utility of UMES DTs, 
driving the transition toward smarter, more sustainable urban energy 
systems.
8. Conclusion
As cities increasingly adopt distributed energy resources and inte­
grate renewables into their energy infrastructure, the complexity of 
these systems demands sophisticated solutions for real-time monitoring, 
optimization, and data management. This review has underscored the 
vital role of digital twins as virtual replicas of urban multi-energy sys­
tems, enhancing system design and operation. Yet, the success of UMES 
DTs hinges on effective data handling and system integration. Advanced 
data fusion techniques and middleware enable seamless interoperability 
between various system components and external data sources. Digital 
twins exemplify the innovative approach for closing the gap between 
transactional data systems and system analysis, significantly contrib­
uting to the entire urban multi-energy systems lifecycle phases of 
planning, operation, decommissioning, and reuse by aligning contin­
uous validation and integration of heterogeneous data sources with 
model and optimization-based analysis digital twin support collabora­
tive and well-informed decision-making processes for urban multi- 
energy system stakeholders. The application of urban multi-energy 
system digital twins has shown potential for enhancing performance, 
sustainability, and resilience, improving energy efficiency, optimizing 
operations, and reducing emissions and costs.
The strategic value of digital twins extends beyond operational an­
alytics to encompass long-term planning, making them critical tools for 
achieving decarbonization objectives. The predictive accuracy of digital 
twins is vital. Yet, the preference for closed-box models underscores the 
need for context-specific data management strategies to optimize digital 
twin applications throughout the urban multi-energy system lifecycle. 
There is growing recognition of the advantages of open and semi-open 
box models, which provide transparency in system operations and the 
flexibility for ongoing modification. These models are advantageous in 
scenarios that require user intervention and iterative learning, facili­
tating greater adaptability and system evolution.
Despite the promising potential of DTs, achieving mature imple­
mentation is challenging, especially regarding scalability and data up­
date methodologies in later lifecycle stages. Scaling digital twins to 
handle the complexity and heterogeneity of urban energy systems, 
ensuring data interoperability through standardized ontologies, and 
addressing socio-economic and regulatory implications are all areas 
requiring further attention. At the same time, ensuring the feasibility of 
continuous data updates requires robust data governance frameworks 
and scalable computing solutions. Future research should focus on 
developing standardized ontologies and protocols to enhance data 
interoperability across different urban systems. Additionally, exploring 
the integration of emerging technologies, such as blockchain for secure 
data sharing and edge computing for real-time analytics, can further 
enhance the functionality and resilience of UMES DTs. Addressing these 
areas will ensure that digital twin technology continues to support 
sustainable and inclusive urban energy transitions.
Glossary
Below is the summary of the definition of key terms used in this 
review article.
Term
Definition
Ref.
Urban multi-energy 
systems (UMES)
Urban multi-energy systems (UMES) are energy- 
efficient and energy-flexible urban areas or 
groups of connected buildings that emit low or 
net-zero greenhouse gas and actively manage 
local production and consumption of renewable 
energy
[38]
Digital twin (DT)
A virtual representation of an object or system 
that spans its lifecycle is updated using real-time 
data and uses simulation, machine learning, and 
reasoning to help decision-making. 
Or 
Digital representation of assets, processes, and 
systems within a built environment with the 
two-way connection between the physical and 
digital world.
[70] 
[223]
Distributed energy 
resources (DERs)
“Energy resources composed of generation, 
storage and controllable load which is 
connected at the low or medium voltage 
distribution level “ (IEC 61,850)
[224]
Cyber-physical system
“Interacting digital, analog, physical and human 
components engineered to provide functionality 
through integrated physics and logic.”
[67]
Internet of Things (IoT)
“An infrastructure of interconnected entities, 
people, systems and information resources 
together with services which process and react 
to information from the physical world and the 
virtual world” ISO/IEC 20,924:2021
[225]
Building information 
modeling (BIM)
“A collaborative way for multi-disciplinary 
information storing, sharing, exchanging, and 
managing throughout the entire project 
lifecycle including planning, design, 
construction, operation, maintenance, and 
demolition phase
[226]
Semantic ontologies
A common language that enables mapping 
between functional and architectural 
components.
–
Physical Twin
The physical, real-world entity that the digital 
twin represents.
–
Technology readiness 
level (TRL)
The most widely used scale for a maturity 
assessment allows a consistent comparison of 
maturity between diverse types of technologies.
[227]
Declaration
During the preparation of this work, the authors used language 
editing tools such as Grammarly, DeepL and ChatGPT to improve lan­
guage and readability. After using these tools, the author reviewed and 
edited the content as needed and take full responsibility for the content 
of the publication.
B. Koirala et al.                                                                                                                                                                                                                                 
Advances in Applied Energy 16 (2024) 100196 
17 


---

Page 18

---

CRediT authorship contribution statement
B. Koirala: Writing – review & editing, Writing – original draft, 
Visualization, Validation, Project administration, Methodology, Inves­
tigation, Funding acquisition, Formal analysis, Conceptualization. H. 
Cai: Writing – review & editing, Writing – original draft, Investigation, 
Conceptualization. F. Khayatian: Writing – review & editing, Writing – 
original draft, Investigation. E. Munoz: Writing – review & editing. J.G. 
An: Writing – original draft, Investigation. R. Mutschler: Writing – 
review & editing. M. Sulzer: Writing – review & editing, Writing – 
original draft, Visualization, Methodology, Funding acquisition, 
Conceptualization. C. De Wolf: Writing – original draft, Investigation. 
K. Orehounig: Writing – review & editing, Investigation, Funding 
acquisition, Conceptualization.
Declaration of competing interest
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper.
Acknowledgments
This research has been conducted within the SWEET PATHFNDR and 
SWEET DecarbCH projects (SWEET Call 1–2020), as well as the SWEET 
SWICE project (SWEET Call 1–2021), funded by the Swiss Federal Office 
of Energy (SFOE). Section 3: Data and Knowledge Management was co- 
funded by the SFOE P+D program as part of the DIGICITIES project 
under the framework of the joint programming initiative ERA-Net Smart 
Energy Systems’ focus initiative Digital Transformation for the Energy 
Transition under grant agreement No 883973. Special thanks to Dr. 
James Allan for contributing to Section 3: Data and Knowledge Man­
agement and revising several versions of this paper.
Data availability
No data was used for the research described in the article. 
References
[1] Do Amaral JVS, Dos Santos CH, Montevechi JAB, De Queiroz AR. Energy digital 
twin applications: a review. Renew Sustain Energy Rev 2023;188:113891. 
https://doi.org/10.1016/j.rser.2023.113891.
[2] Mancarella P. MES (multi-energy systems): an overview of concepts and 
evaluation models. Energy 2014;65:1–17. https://doi.org/10.1016/j. 
energy.2013.10.041.
[3] Vargas M, Davis G. World energy scenarios 2016. London, UK: World Energy 
Council; 2016.
[4] Koirala BP, Koliou E, Friege J, Hakvoort RA, Herder PM. Energetic communities 
for community energy: a review of key issues and trends shaping integrated 
community energy systems. Renew Sustain Energy Rev 2016;56:722–44. https:// 
doi.org/10.1016/j.rser.2015.11.080.
[5] Devine-Wright P. Community versus local energy in a context of climate 
emergency. Nat Energy 2019;4:894–6. https://doi.org/10.1038/s41560-019- 
0459-2.
[6] IRENA. Transforming the energy system and holding the line on rising global 
temperatures. Abu Dhabi /Bonn/ New York: International Renewable Energy 
Agency (IRENA); 2019.
[7] Bogdanov D, Farfan J, Sadovskaia K, Aghahosseini A, Child M, Gulagi A, et al. 
Radical transformation pathway towards sustainable electricity via evolutionary 
steps. Nat Commun 2019;10:1077. https://doi.org/10.1038/s41467-019-08855- 
1.
[8] D´oci G, Vasileiadou E, Petersen AC. Exploring the transition potential of 
renewable energy communities. Futures 2015;66:85–95. https://doi.org/ 
10.1016/j.futures.2015.01.002.
[9] Hoppe T, de Vries G. Social Innovation and the Energy Transition. Sustainability 
2018;11:141. https://doi.org/10.3390/su11010141.
[10] van der Schoor T, van Lente H, Scholtens B, Peine A. Challenging obduracy: how 
local communities transform the energy system. Energy Res Soc Sci 2016;13: 
94–105. https://doi.org/10.1016/j.erss.2015.12.009.
[11] Koirala B, Hers S, Morales-Espa˜na G, ¨Ozdemir ¨O, Sijm J, Weeda M. Integrated 
electricity, hydrogen and methane system modelling framework: application to 
the Dutch Infrastructure Outlook 2050. Appl Energy 2021;289:116713. https:// 
doi.org/10.1016/j.apenergy.2021.116713.
[12] Bardow A, Fiorentini M, Heer P, K¨amper A, Koirala B, Knoeri C, et al. Flexibility 
and sector coupling in energy systems: definitions and metrics: synthesis report. 
ETH Zurich 2023. https://doi.org/10.3929/ETHZ-B-000641177.
[13] Koirala BP, Cai H, De Koning J, Heer P, Orehounig K. Flexibility assessment of 
power-hydrogen-power (P2H2P) system in multi-energy districts. J Phys: Conf 
Ser 2023;2600:072007. https://doi.org/10.1088/1742-6596/2600/7/072007.
[14] Koirala BP, van Oost E, van der Windt H. Community energy storage: a 
responsible innovation towards a sustainable energy system? Appl Energy 2018; 
231:570–85. https://doi.org/10.1016/j.apenergy.2018.09.163.
[15] Cali U, Dimd BD, Hajialigol P, Moazami A, Gourisetti SNG, Lobaccaro G, et al. 
Digital Twins: shaping the future of energy systems and smart cities through 
cybersecurity, efficiency, and sustainability. In: 2023 International Conference on 
Future Energy Solutions (FES). Vaasa, Finland: IEEE; 2023. p. 1–6. https://doi. 
org/10.1109/FES57669.2023.10182868.
[16] Macana CA, Quijano N, Mojica-Nava E. A survey on cyber physical energy 
systems and their applications on smart grids. In: 2011 IEEE PES CONFERENCE 
ON INNOVATIVE SMART GRID TECHNOLOGIES LATIN AMERICA (ISGT LA). 
Medellin, Colombia: IEEE; 2011. p. 1–7. https://doi.org/10.1109/ISGT- 
LA.2011.6083194.
[17] Inderwildi O, Zhang C, Wang X, Kraft M. The impact of intelligent cyber-physical 
systems on the decarbonization of energy. Energy Environ Sci 2020;13:744–71. 
https://doi.org/10.1039/C9EE01919G.
[18] Orumwense EF, Abo-Al-Ez K. A systematic review to aligning research paths: 
energy cyber-physical systems. Cogent Eng 2019;6:1700738. https://doi.org/ 
10.1080/23311916.2019.1700738.
[19] Hoogsteen G. A cyber-physical systems perspective on decentralized energy 
management. PhD. University of Twente; 2017. https://doi.org/10.3990/ 
1.9789036544320.
[20] Bartock M, Cichonski J, Souppaya M, Smith M, Witte G, Scarfone K. Guide for 
cybersecurity event recovery. Gaithersburg, MD: National Institute of Standards 
and Technology; 2016. https://doi.org/10.6028/NIST.SP.800-184.
[21] Pileggi P, Verriet J, Broekhuijsen J, van Leeuwen C, Wijbrandi W, Konsman M. 
A digital twin for cyber-physical energy systems. In: 2019 7th Workshop on 
Modeling and Simulation of Cyber-Physical Energy Systems (MSCPES). Montreal, 
QC, Canada: IEEE; 2019. p. 1–6. https://doi.org/10.1109/ 
MSCPES.2019.8738792.
[22] Onile AE, Machlev R, Petlenkov E, Levron Y, Belikov J. Uses of the digital twins 
concept for energy services, intelligent recommendation systems, and demand 
side management: a review. Energy Rep 2021;7:997–1015. https://doi.org/ 
10.1016/j.egyr.2021.01.090.
[23] Tao F, Zhang H, Liu A, Nee AYC. Digital twin in industry: state-of-the-Art. IEEE 
Trans Ind Inf 2019;15:2405–15. https://doi.org/10.1109/TII.2018.2873186.
[24] Grieves M. Digital twin: manufacturing excellence through virtual factory 
replication. Florida institute of technology; 2014.
[25] DUET. Building secure and trusted digital urban twins 2022. https://www.digit 
alurbantwins.com/post/building-secure-and-trusted-digital-urban-twins
(accessed November 29, 2023).
[26] FacilitiesNet. How digital twins technology enables smart buildings, smart cities. 
Facilitiesnet 2022. https://www.facilitiesnet.com/buildingautomation/article/ 
How-Digital-Twins-Technology-Enables-Smart-Buildings-Smart-Cities-19488
(accessed November 29, 2023).
[27] Mont´ans FJ, Chinesta F, G´omez-Bombarelli R, Kutz JN. Data-driven modeling and 
learning in science and engineering. Comptes Rendus M´ecanique 2019;347: 
845–55. https://doi.org/10.1016/j.crme.2019.11.009.
[28] Li H, Zhang T, Huang Y. Digital twin technology for integrated energy system and 
its application. In: 2021 IEEE 1st International Conference on Digital Twins and 
Parallel Intelligence (DTPI); 2021. p. 422–5. https://doi.org/10.1109/ 
DTPI52967.2021.9540160.
[29] Lamagna M, Groppi D, Nezhad MM, Piras G. A comprehensive review on digital 
twins for smart energy management system. Int J EQ 2021;6:323–34. https://doi. 
org/10.2495/EQ-V6-N4-323-334.
[30] Zhou Y, Su P, Wu J, Sun W, Xu X, Abeysekera M. Digital twins for flexibility 
service provision from industrial energy systems. In: 2021 IEEE 1st International 
Conference on Digital Twins and Parallel Intelligence (DTPI). Beijing, China: 
IEEE; 2021. p. 274–7. https://doi.org/10.1109/DTPI52967.2021.9540158.
[31] W3C. OWL 2 web ontology language conformance (Second Edition) 2012. 
https://www.w3.org/TR/owl2-conformance/(accessed November 29, 2023).
[32] Cityzenith. Cityzenith - world leading urban digital twin technology 2023. http 
s://cityzenith.com/(accessed March 10, 2023).
[33] Stockholm Virtual City. Stockholm virtual city | drive Sweden 2021. http 
s://www.drivesweden.net/en/project/stockholm-virtual-city (accessed March 
10, 2023).
[34] Zürich 4D - Stadt Zürich n.d. https://www.stadt-zuerich.ch/hbd/de/index/staedt 
ebau/zuerich-4dhtml (accessed March 10, 2023).
[35] SEC-DUCT. cooling Singapore 2023. https://sec.ethz.ch/research/cs.html
(accessed June 20, 2023).
[36] Fuller A, Fan Z, Day C, Barlow C. Digital twin: enabling technologies, challenges 
and open research. IEEE Access 2020;8:108952–71. https://doi.org/10.1109/ 
ACCESS.2020.2998358.
[37] IPA-UK. Transforming infrastructure performance: roadmap to 2030. 
infrastructures and projects authority, government of UK; 2021.
[38] Urban Europe. Positive energy districts (PED). JPI Urban Europe 2021. https://jp 
i-urbaneurope.eu/ped/(accessed October 15, 2021).
[39] Houwing M, Heijnen P, Bouwmans I. Socio-Technical complexity in energy 
infrastrucutres: conceptual framework to study the impact of domestic level 
energy generation, storage and exchange. IEEE; 2006. p. 906–11.
B. Koirala et al.                                                                                                                                                                                                                                 
Advances in Applied Energy 16 (2024) 100196 
18 


---

Page 19

---

[40] Cherp A, Vinichenko V, Jewell J, Brutschin E, Sovacool B. Integrating techno- 
economic, socio-technical and political perspectives on national energy 
transitions: a meta-theoretical framework. Energy Res Soc Sci 2018;37:175–90. 
https://doi.org/10.1016/j.erss.2017.09.015.
[41] Mobasheri S, Dorahaki S, Rashidinejad M, MollahassaniPour M. Overview of 
multi-energy interconnected systems in different energy grids. IoT Enabled Multi- 
Energy Syst 2023:9–30. https://doi.org/10.1016/B978-0-323-95421-1.00002-1.
[42] Kunneke R. Critical infrastructures: aligning institutions and technology 2013.
[43] Scholten D, Künneke R, Groenewegen J, Correlj´e A. Towards the comprehensive 
institutional design of energy infrastructures. editor. In: van den Hoven J, editor. 
Handbook of ethics, values, and technological design: sources, theory, values and 
application domains. Dordrecht: Springer; 2015.
[44] Koirala B, Mutschler R, Bartolini A, Bollinger A, Orehounig K. Flexibility 
assessment of e-mobilty in multi-energy districts. CIRED Porto Workshop 2022: e- 
mobility and power distribution systems. In: Hybrid Conference. Porto, Portugal: 
Institution of Engineering and Technology; 2022. p. 824–8. https://doi.org/ 
10.1049/icp.2022.0827.
[45] Lund H, Muenster E. Integrated energy systems and local energy markets. Energy 
Pol 2006;34:1152–60. https://doi.org/10.1016/j.enpol.2004.10.004.
[46] Koirala B, Chaves ´Avila J, G´omez T, Hakvoort R, Herder P. Local alternative for 
energy supply: performance assessment of integrated community energy systems. 
Energies 2016;9:981. https://doi.org/10.3390/en9120981.
[47] Abeysekera M, Wu J, Nick J. Integrated energy systems: an overview of benefits, 
analysis methods, research gaps and opportunites. Hubnet 2016.
[48] Mendes G, Ioakimidis C, Ferr˜ao P. On the planning and analysis of integrated 
community energy systems: a review and survey of available tools. Renew Sustain 
Energy Rev 2011;15:4836–54.
[49] Xu X, Jin X, Jia H, Yu X, Li K. Hierarchical management for integrated community 
energy systems. Appl Energy 2015;160:231–43. https://doi.org/10.1016/j. 
apenergy.2015.08.134.
[50] Acosta C, Ortega M, Bunsen T, Koirala B, Ghorbani A. Facilitating energy 
transition through energy commons: an application of socio-ecological systems 
framework for integrated community energy systems. Sustainability 2018;10: 
366. https://doi.org/10.3390/su10020366.
[51] Cardoso G, Stadler M, Bozchalui MC, Sharma R, Marnay C, Barbosa-P´ovoa A, 
et al. Optimal investment and scheduling of distributed energy resources with 
uncertainty in electric vehicle driving schedules. Energy 2014;64:17–30. https:// 
doi.org/10.1016/j.energy.2013.10.092.
[52] Weber C, Shah N. Optimisation based design of a district energy system for an 
eco-town in the United Kingdom. Energy 2011;36:1292–308. https://doi.org/ 
10.1016/j.energy.2010.11.014.
[53] Best RE, Flager F, Lepech MD. Modeling and optimization of building mix and 
energy supply technology for urban districts. Appl Energy 2015;159:161–77. 
https://doi.org/10.1016/j.apenergy.2015.08.076.
[54] Huang Z, Yu H, Peng Z, Zhao M. Methods and tools for community energy 
planning: a review. Renew Sustain Energy Rev 2015;42:1335–48. https://doi. 
org/10.1016/j.rser.2014.11.042.
[55] Karunathilake H, Hewage K, Prabatha T, Ruparathna R, Sadiq R. Project 
deployment strategies for community renewable energy: a dynamic multi-period 
planning approach. Renew Energy 2020;152:237–58. https://doi.org/10.1016/j. 
renene.2020.01.045.
[56] Yu H, Huang Z, Pan Y, Long W. Analysis of Urban Energy Planning Policies. 
Guidelines for community energy planning. Singapore: Springer Singapore; 2020. 
p. 455–95. https://doi.org/10.1007/978-981-13-9600-7_13.
[57] Krog L, Sperling K. A comprehensive framework for strategic energy planning 
based on Danish and international insights. Energy Strategy Reviews 2019;24: 
83–93. https://doi.org/10.1016/j.esr.2019.02.005.
[58] van Beuzekom I, Gibescu M, Slootweg JG. A review of multi-energy system 
planning and optimization tools for sustainable urban development. In: 2015 
IEEE Eindhoven PowerTech. Eindhoven, Netherlands: IEEE; 2015. p. 1–7. https:// 
doi.org/10.1109/PTC.2015.7232360.
[59] Keirstead J, Jennings M, Sivakumar A. A review of urban energy system models: 
approaches, challenges and opportunities. Renew Sustain Energy Rev 2012;16: 
3847–66. https://doi.org/10.1016/j.rser.2012.02.047.
[60] Nik VM, Perera ATD, Chen D. Towards climate resilient urban energy systems: a 
review. Natl Sci Rev 2021;8:nwaa134. https://doi.org/10.1093/nsr/nwaa134.
[61] Zheng Z, Shafique M, Luo X, Wang S. A systematic review towards integrative 
energy management of smart grids and urban energy systems. Renew Sustain 
Energy Rev 2024;189:114023. https://doi.org/10.1016/j.rser.2023.114023.
[62] Sulzer M, Wetter M, Mutschler R, Sangiovanni-Vincentelli A. Platform-based 
design for energy systems. Appl Energy 2023;352:121955. https://doi.org/ 
10.1016/j.apenergy.2023.121955.
[63] Zhivov AM, Michael C, Liesen R, Kimman J, Broers W. Energy master 
planningtowards net-zero energy communities/campuses. ASHRAE 2014;120: 
114–29.
[64] Tao F, Qi Q. Make more digital twins. Nature 2019;573:490–1. https://doi.org/ 
10.1038/d41586-019-02849-1.
[65] Jones D, Snider C, Nassehi A, Yon J, Hicks B. Characterising the digital twin: a 
systematic literature review. CIRP J Manufac Sci Technol 2020;29:36–52. 
https://doi.org/10.1016/j.cirpj.2020.02.002.
[66] Woods E., Freas B. Creating zero carbon communities: the role of digital twins 
2019.
[67] Farsi M., Daneshkhah A., Hosseinian-Far A., Jahankhani H. Digital twin 
technologies and smart cities. 2020.
[68] Lim KYH, Zheng P, Chen C-H. A state-of-the-art survey of digital twin: techniques, 
engineering product lifecycle management and business innovation perspectives. 
J Intell Manuf 2020;31:1313–37. https://doi.org/10.1007/s10845-019-01512-w.
[69] Wright L, Davidson S. How to tell the difference between a model and a digital 
twin. Adv Model and Simul in Eng Sci 2020;7:13. https://doi.org/10.1186/ 
s40323-020-00147-4.
[70] IBM. What is a digital twin? 2021. https://www.ibm.com/topics/what-is-a-digita 
l-twin (accessed October 20, 2021).
[71] Miskinis C. The mysterious history of digital twin technology and who created it. 
Challenge Advisory 2019. https://www.challenge.org/insights/digital-twin-hi 
story/(accessed September 6, 2022).
[72] Deren L, Wenbo Y, Zhenfeng S. Smart city based on digital twins. ComputUrban 
Sci 2021;1:4. https://doi.org/10.1007/s43762-021-00005-y.
[73] Walters A. National digital twin programme 2019. https://www.cdbb.cam.ac. 
uk/what-we-do/national-digital-twin-programme (accessed February 23, 2022).
[74] Reiser A. Singapore’s digital twin of entire country. tomorrow’s world today® 
2022. https://www.tomorrowsworldtoday.com/2022/09/12/singapores-digita 
l-twin-of-entire-country/(accessed November 9, 2022).
[75] Bauer P, Stevens B, Hazeleger W. A digital twin of Earth for the green transition. 
Nat Clim Chang 2021;11:80–3. https://doi.org/10.1038/s41558-021-00986-y.
[76] Rasheed A, San O, Kvamsdal T. Digital twin: values, challenges and enablers from 
a modeling perspective. IEEE Access 2020;8:21980–2012. https://doi.org/ 
10.1109/ACCESS.2020.2970143.
[77] Hofbauer G, Sangl A, Engelhardt S. The digital transformation of the product 
management process: conception of digital twin impacts for the different stages. 
IJIED 2019;5:74–86. https://doi.org/10.18775/ijied.1849-7551- 
7020.2015.52.2006.
[78] Zhang X, Shen J, Saini PK, Lovati M, Han M, Huang P, et al. Digital twin for 
accelerating sustainability in positive energy district: a review of simulation tools 
and applications. Front Sustain Cities 2021;3:663269. https://doi.org/10.3389/ 
frsc.2021.663269.
[79] Schooling J., Burgess G., Enzer M. Flourishing systems: re-envisioning 
infrastructure as a platform for human flourishing. Apollo - university of 
Cambridge Repository; 2020. https://doi.org/10.17863/CAM.52270.
[80] Fahim M, Sharma V, Cao T-V, Canberk B, Duong TQ. Machine learning-based 
digital twin for predictive modeling in wind turbines. IEEE Access 2022;10: 
14184–94. https://doi.org/10.1109/ACCESS.2022.3147602.
[81] Arsiwala A, Elghaish F, Zoher M. Digital twin with machine learning for 
predictive monitoring of CO2 equivalent from existing buildings. Energy Build 
2023;284:112851. https://doi.org/10.1016/j.enbuild.2023.112851.
[82] Ritto TG, Rochinha FA. Digital twin, physics-based model, and machine learning 
applied to damage detection in structures. Mech Syst Signal Process 2021;155: 
107614. https://doi.org/10.1016/j.ymssp.2021.107614.
[83] Ferr´e-Bigorra J, Casals M, Gangolells M. The adoption of urban digital twins. 
Cities 2022;131:103905. https://doi.org/10.1016/j.cities.2022.103905.
[84] Weil C, Bibri SE, Longchamp R, Golay F, Alahi A. Urban digital twin challenges: a 
systematic review and perspectives for sustainable smart cities. Sustain Cities Soc 
2023;99:104862. https://doi.org/10.1016/j.scs.2023.104862.
[85] Lei B, Janssen P, Stoter J, Biljecki F. Challenges of urban digital twins: a 
systematic review and a Delphi expert survey. Autom Const 2023;147:104716. 
https://doi.org/10.1016/j.autcon.2022.104716.
[86] +CityxChange. positive city exchange 2020. https://cityxchange.eu/(accessed 
March 10, 2020).
[87] Peldon D, Banihashemi S, LeNguyen K, Derrible S. Navigating urban complexity: 
the transformative role of digital twins in smart city development. Sustain Cities 
Soc 2024;111:105583. https://doi.org/10.1016/j.scs.2024.105583.
[88] Kalles S., Ankaras E., Nilsson T., Thuvander L. Identifying the potential role of 
digital twins in supporting PEDs. Sweden: JPI Urban Europe; 2022.
[89] EU. EU programmes to support the digital and green transformation of the energy 
system | Shaping Europe’s digital future 2023. https://digital-strategy.ec.europa. 
eu/en/policies/eu-programmes-digitalisation-energy (accessed June 13, 2023).
[90] Tzachor A, Sabri S, Richards CE, Rajabifard A, Acuto M. Potential and limitations 
of digital twins to achieve the sustainable development goals. Nat Sustain 2022. 
https://doi.org/10.1038/s41893-022-00923-7.
[91] Boyes H, Watson T. Digital twins: an analysis framework and open issues. Comput 
Ind 2022;143:103763. https://doi.org/10.1016/j.compind.2022.103763.
[92] Zwitter A, Gstrein OJ. Handbook on the politics and governance of big data and 
artificial intelligence. editors. Northampton: Edward Elgar Publishing; 2023.
[93] Pritoni M, Paine D, Fierro G, Mosiman C, Poplawski M, Saha A, et al. Metadata 
schemas and ontologies for building energy applications: a critical review and use 
case analysis. Energies 2021;14:2024. https://doi.org/10.3390/en14072024.
[94] Pileggi P, Verriet J, Broekhuijsen J, Van Leeuwen C, Wijbrandi W, Konsman M. 
A digital twin for cyber-physical energy systems. In: 2019 7th Workshop on 
Modeling and Simulation of Cyber-Physical Energy Systems (MSCPES). Montreal, 
QC, Canada: IEEE; 2019. p. 1–6. https://doi.org/10.1109/ 
MSCPES.2019.8738792.
[95] Wang J, Gao F, Zhou Y, Guo Q, Tan C-W, Song J, et al. Data sharing in energy 
systems. Adv Appl Energy 2023;10:100132. https://doi.org/10.1016/j. 
adapen.2023.100132.
[96] Alanne K, Saari A. Distributed energy generation and sustainable development. 
Renew Sustain Energy Rev 2006;10:539–58. https://doi.org/10.1016/j. 
rser.2004.11.004.
[97] Mavromatidis G, Orehounig K, Carmeliet J. A review of uncertainty 
characterisation approaches for the optimal design of distributed energy systems. 
Renew Sustain Energy Rev 2018;88:258–77. https://doi.org/10.1016/j. 
rser.2018.02.021.
B. Koirala et al.                                                                                                                                                                                                                                 
Advances in Applied Energy 16 (2024) 100196 
19 


---

Page 20

---

[98] Yamamura S, Fan L, Suzuki Y. Assessment of urban energy performance through 
integration of BIM and GIS for smart city planning. Procedia Eng 2017;180: 
1462–72.
[99] Wehkamp S, Schmeling L, Vorspel L, Roelcke F, Windmeier K-L. District energy 
systems: challenges and new tools for planning and evaluation. Energies 2020;13: 
2967.
[100] Wetter M, van Treeck C, Helsen L, Maccarini A, Saelens D, Robinson D, et al. 
IBPSA Project 1: BIM/GIS and Modelica framework for building and community 
energy system design and operation – ongoing developments, lessons learned and 
challenges. IOP Conf Ser: Earth Environ Sci 2019;323:012114. https://doi.org/ 
10.1088/1755-1315/323/1/012114.
[101] Heo J, Moon H, Chang S, Han S, Lee D-E. Case study of solar photovoltaic power- 
plant site selection for infrastructure planning using a BIM-GIS-based approach. 
Appl. Sci. 2021;11:8785.
[102] Azhar S. Building information modeling (BIM): trends, benefits, risks, and 
challenges for the AEC industry. Leadership Manag Engin 2011;11:241–52.
[103] Kivits RA, Furneaux C. BIM: enabling sustainability and asset management 
through knowledge management. Scien World J 2013. 2013.
[104] Charef R, Alaka H, Emmitt S. Beyond the third dimension of BIM: a systematic 
review of literature and assessment of professional views. J Build Eng 2018;19: 
242–57.
[105] Charef R. The use of building information modelling in the circular economy 
context: several models and a new dimension of BIM (8D). Cleaner Eng Technol 
2022;7:100414.
[106] Ershadi M, Jefferies M, Davis P, Mojtahedi M. Implementation of Building 
Information Modelling in infrastructure construction projects: a study of 
dimensions and strategies. Int. J. Inform. Syst. Project Manag. 2021;9:43–59.
[107] Xu X, Mumford T, Zou PX. Life-cycle building information modelling (BIM) 
engaged framework for improving building energy performance. Energy Build 
2021;231:110496.
[108] Lu Q, Xie X, Heaton J, Parlikad AK, Schooling J. From BIM towards digital twin: 
strategy and future development for smart asset management. In: Borangiu T, 
Trentesaux D, Leit˜ao P, Giret Boggino A, Botti V, editors. Service oriented, holonic 
and multi-agent manufacturing systems for industry of the future. Cham: Springer 
International Publishing; 2020. p. 392–404. https://doi.org/10.1007/978-3-030- 
27477-1_30.
[109] Deng M, Menassa CC, Kamat VR. From BIM to digital twins: a systematic review 
of the evolution of intelligent building representations in the AEC-FM industry. 
J Infor Technol Const (ITcon) 2021;26:58–83. https://doi.org/10.36680/j. 
itcon.2021.005.
[110] Song Y, Wang X, Tan Y, Wu P, Sutrisna M, Cheng JCP, et al. Trends and 
opportunities of BIM-GIS integration in the architecture, engineering and 
construction industry: a review from a spatio-temporal statistical perspective. 
ISPRS Int J Geoinf 2017;6:397. https://doi.org/10.3390/ijgi6120397.
[111] Kamel E, Memari AM. Review of BIM’s application in energy simulation: tools, 
issues, and solutions. Autom Const 2019;97:164–80. https://doi.org/10.1016/j. 
autcon.2018.11.008.
[112] El-Diraby T, Sobhkhiz S. The building as a platform: predictive digital twinning. 
buildings and semantics. CRC Press; 2022. p. 201–21.
[113] Boje C, Kubicki S, Guerriero A, Rezgui Y, Zarli A. Digital twins for the built 
environment. Build Semantics 2022:179–99. https://doi.org/10.1201/ 
9781003204381-10.
[114] Chevallier Z, Finance B, Boulakia BC. A reference architecture for smart building 
digital twin. editor. In: 2020 International Workshop on Semantic Digital Twins. 
2615. Unknow, France: SeDiT; 2020. p. 2020.
[115] Mavrokapnidis D, Katsigarakis K, Pauwels P, Petrova E, Korolija I, Rovas D. 
A linked-data paradigm for the integration of static and dynamic building data in 
digital twins. In: Proceedings of the 8th ACM International Conference on Systems 
for Energy-Efficient Buildings, Cities, and Transportation. Coimbra Portugal: 
ACM; 2021. p. 369–72. https://doi.org/10.1145/3486611.3491125.
[116] Pauwels P, Costin A, Rasmussen MH. Knowledge graphs and linked data for the 
built environment. In: Bolpagni M, Gavina R, Ribeiro D, editors. Industry 4.0 for 
the built environment: methodologies, technologies and skills. Cham: Springer 
International Publishing; 2022. p. 157–83. https://doi.org/10.1007/978-3-030- 
82430-3_7.
[117] Bolton A., Butler L., Dabson I., Enzer M., Evans M., Fenemore T., et al. Gemini 
principles. apollo - university of Cambridge repository; 2018. https://doi.org/ 
10.17863/CAM.32260.
[118] Aheleroff S, Xu X, Zhong RY, Lu Y. Digital twin as a service (DTaaS) in industry 
4.0: an architecture reference model. Adv Eng Inf 2021;47:101225. https://doi. 
org/10.1016/j.aei.2020.101225.
[119] Liu Z., Meyendorf N., Mrad N. The role of data fusion in predictive maintenance 
using digital twin, Provo, Utah, USA: 2018, p. 020023. https://doi.org/10.1063/ 
1.5031520.
[120] Hakimi O, Liu H, Abudayyeh O, Houshyar A, Almatared M, Alhawiti A. Data 
fusion for smart civil infrastructure management: a conceptual digital twin 
framework. Buildings 2023;13:2725. https://doi.org/10.3390/ 
buildings13112725.
[121] García S, Ramírez-Gallego S, Luengo J, Benítez JM, Herrera F. Big data 
preprocessing: methods and prospects. Big Data Anal 2016;1:9. https://doi.org/ 
10.1186/s41044-016-0014-0.
[122] OPC-UA. OPC UA online reference - released specifications 2024. https://refere 
nce.opcfoundation.org/(accessed September 8, 2024).
[123] Mishra B, Kertesz A. The use of MQTT in M2M and IoT systems: a survey. IEEE 
Access 2020;8:201071–86. https://doi.org/10.1109/ACCESS.2020.3035849.
[124] Quincozes S, Emilio T, Kazienko J. MQTT Protocol: fundamentals, tools and 
future directions. IEEE Latin Am Trans 2019;17:1439–48. https://doi.org/ 
10.1109/TLA.2019.8931137.
[125] Rodríguez F, Chicaiza WD, S´anchez A, Esca˜no JM. Updating digital twins: 
methodology for data accuracy quality control using machine learning 
techniques. Comp Ind 2023;151:103958. https://doi.org/10.1016/j. 
compind.2023.103958.
[126] Booshehri M, Emele L, Flügel S, F¨orster H, Frey J, Frey U, et al. Introducing the 
open energy ontology: enhancing data interpretation and interfacing in energy 
systems analysis. Energy and AI 2021;5:100074. https://doi.org/10.1016/j. 
egyai.2021.100074.
[127] Daniele L, den Hartog F, Roes J. Created in close interaction with the industry: the 
smart appliances REFerence (SAREF) ontology. editors. In: Cuel R, Young R, 
editors. Formal ontologies meet industry. Cham: Springer International 
Publishing; 2015. p. 100–12. https://doi.org/10.1007/978-3-319-21545-7_9.
[128] Compton M, Barnaghi P, Bermudez L, García-Castro R, Corcho O, Cox S, et al. The 
SSN ontology of the W3C semantic sensor network incubator group. J Web 
Semantics 2012;17:25–32. https://doi.org/10.1016/j.websem.2012.05.003.
[129] Janowicz K, Haller A, Cox SJD, Phuoc DL, Lefrancois M. SOSA: a lightweight 
ontology for sensors, observations, samples, and actuators. J Web Semantics 
2019;56:1–10. https://doi.org/10.1016/j.websem.2018.06.003.
[130] Lambert, Eric, Boultadakis, George, Kukk, Kalle, Kotsalos, Konstantinos, Bilidis, 
Nikos. European energy data exchange reference architecture: data management 
working group. 2021.
[131] Biljecki F, Kumar K, Nagel C. CityGML Application domain extension (ADE): 
overview of developments. Open Geospatial Data, Softw Stand 2018;3:13. 
https://doi.org/10.1186/s40965-018-0055-6.
[132] Kutzner T, Chaturvedi K, Kolbe TH. CityGML 3.0: new functions open up new 
applications. PFG 2020;88:43–61. https://doi.org/10.1007/s41064-020-00095-z.
[133] Widl E, Agugiaro G, Peters-Anders J. Linking semantic 3D city models with 
domain-specific simulation tools for the planning and validation of energy 
applications at district level. Sustainability 2021;13:8782. https://doi.org/ 
10.3390/su13168782.
[134] Corrado V, Ballarini I, Madrazo L, Nemirovskij G. Data structuring for the 
ontological modelling of urban energy systems: the experience of the SEMANCO 
project. Sustain Cities Soc 2015;14:223–35. https://doi.org/10.1016/j. 
scs.2014.09.006.
[135] Corrado V., Ballarini I. SEMANCO Deliverable 3.2: guidelines for structuring 
energy data. Accessed July 2013;31.
[136] Balaji B, Bhattacharya A, Fierro G, Gao J, Gluck J, Hong D, et al. Brick: towards a 
unified metadata schema for buildings. In: Proceedings of the 3rd ACM 
International Conference on Systems for Energy-Efficient Built Environments. 
New York, NY, USA: Association for Computing Machinery; 2016. p. 41–50. 
https://doi.org/10.1145/2993422.2993577.
[137] Hammar K., Wallin E.O., Karlberg P., H¨alleberg D. The RealEstateCore ontology. 
In: Ghidini C, Hartig O, Maleshkova M, Sv´atek V, Cruz I, Hogan A, et al., editors. 
The semantic web – ISWC 2019, vol. 11779, Cham: Springer International 
Publishing; 2019, p. 130–45. https://doi.org/10.1007/978-3-030-30796-7_9.
[138] Cuenca J, Larrinaga F, Curry E. DABGEO: a reusable and usable global energy 
ontology for the energy domain. J Web Semantics 2020;61–62:100550. https:// 
doi.org/10.1016/j.websem.2020.100550.
[139] Anderson B., Barnstedt E., Weinstock G. Adopting DTDL-based industry 
ontologies - azure digital twins 2023. https://learn.microsoft.com/en-us/azure/ 
digital-twins/concepts-ontologies-adopt (accessed December 15, 2023).
[140] Conde J, Munoz-Arcentales A, Alonso ´A, L´opez-Pernas S, Salvachúa J. Modeling 
digital twin data and architecture: a building guide with FIWARE as enabling 
technology. IEEE Internet Comput 2022;26:7–14. https://doi.org/10.1109/ 
MIC.2021.3056923.
[141] Jiang Z, Guo Y, Wang Z. Digital twin to improve the virtual-real integration of 
industrial IoT. J Ind Infor Int 2021;22:100196. https://doi.org/10.1016/j. 
jii.2020.100196.
[142] Minerva R, Lee GM, Crespi N. Digital twin in the IoT context: a survey on 
technical features, scenarios, and architectural models. Proc IEEE 2020;108: 
1785–824. https://doi.org/10.1109/JPROC.2020.2998530.
[143] Jacoby M, Usl¨ander T. Digital twin and internet of things—current standards 
landscape. Appl Sci 2020;10:6519. https://doi.org/10.3390/app10186519.
[144] Laghari AA, Wu K, Laghari RA, Ali M, Khan AA. A review and state of art of 
internet of things (IoT). Arch Computat Methods Eng 2022;29:1395–413. https:// 
doi.org/10.1007/s11831-021-09622-6.
[145] Li X, Xu LD. A review of internet of things—resource allocation. IEEE Int Things J 
2021;8:8657–66. https://doi.org/10.1109/JIOT.2020.3035542.
[146] Hossein Motlagh N, Mohammadrezaei M, Hunt J, Zakeri B. Internet of things 
(IoT) and the energy sector. Energies 2020;13:494. https://doi.org/10.3390/ 
en13020494.
[147] Singh RP, Javaid M, Haleem A, Suman R. Internet of things (IoT) applications to 
fight against COVID-19 pandemic. Diab Metab Syndr 2020;14:521–4. https://doi. 
org/10.1016/j.dsx.2020.04.041.
[148] Aheleroff S, Xu X, Zhong RY, Lu Y. Digital twin as a service (DTaaS) in industry 
4.0: an architecture reference model. Adv Eng Infor 2021;47:101225. https://doi. 
org/10.1016/j.aei.2020.101225.
[149] Bong Kim D, Shao G, Jo G. A digital twin implementation architecture for wire +
arc additive manufacturing based on ISO 23247. Manufac Lett 2022;34:1–5. 
https://doi.org/10.1016/j.mfglet.2022.08.008.
[150] Cabral JVA, Gasca EAR, Alvares AJ. Digital twin implementation for machining 
center based on ISO 23247 standard. IEEE Latin Am Trans 2023;21:628–35. 
https://doi.org/10.1109/TLA.2023.10130834.
B. Koirala et al.                                                                                                                                                                                                                                 
Advances in Applied Energy 16 (2024) 100196 
20 


---

Page 21

---

[151] Safaric S, Malaric K. ZigBee wireless standard. In: Proceedings ELMAR 2006; 
2006. p. 259–62. https://doi.org/10.1109/ELMAR.2006.329562.
[152] Ramya CM, Shanmugaraj M, Prabakaran R. Study on ZigBee technology. In: 2011 
3rd International Conference on Electronics Computer Technology. 6; 2011. 
p. 297–301. https://doi.org/10.1109/ICECTECH.2011.5942102.
[153] Adi PDP, Sihombing V, Siregar VMM, Yanris GJ, Sianturi FA, Purba W, et al. 
A performance evaluation of ZigBee mesh communication on the internet of 
things (IoT). In: 2021 3rd East Indonesia Conference on Computer and 
Information Technology (EIConCIT); 2021. p. 7–13. https://doi.org/10.1109/ 
EIConCIT50028.2021.9431875.
[154] Almuhaya MAM, Jabbar WA, Sulaiman N, Abdulmalek S. A survey on LoRaWAN 
technology: recent trends, opportunities, simulation tools and future directions. 
Electronics (Basel) 2022;11:164. https://doi.org/10.3390/electronics11010164.
[155] Haxhibeqiri J, De Poorter E, Moerman I, Hoebeke J. A survey of LoRaWAN for 
IoT: from technology to application. Sensors 2018;18:3995. https://doi.org/ 
10.3390/s18113995.
[156] Jouhari M, Saeed N, Alouini M-S, Amhoud EM. A survey on scalable LoRaWAN 
for massive IoT: recent advances, potentials, and challenges. IEEE Commun Surv 
Tutor 2023:1. https://doi.org/10.1109/COMST.2023.3274934. –11.
[157] Swetina J, Lu G, Jacobs P, Ennesser F, Song J. Toward a standardized common 
M2M service layer platform: introduction to oneM2M. IEEE Wireless Commun 
2014;21:20–6. https://doi.org/10.1109/MWC.2014.6845045.
[158] An J, Le Gall F, Kim J, Yun J, Hwang J, Bauer M, et al. Toward global IoT-enabled 
smart cities interworking using adaptive semantic adapter. IEEE Int Things J 
2019;6:5753–65. https://doi.org/10.1109/JIOT.2019.2905275.
[159] Privat G. Guidelines for modelling with NGSI-LD (ETSI White Paper). 2021.
[160] Abid A, Lee J, Le Gall F, Song J. Toward mapping an NGSI-LD context model on 
RDF graph approaches: a comparison study. Sensors 2022;22:4798. https://doi. 
org/10.3390/s22134798.
[161] Arvind S, Narayanan VA. An overview of security in CoAP: attack and analysis. In: 
2019 5th International Conference on Advanced Computing & Communication 
Systems (ICACCS); 2019. p. 655–60. https://doi.org/10.1109/ 
ICACCS.2019.8728533.
[162] Blockwitz T., Otter M., Akesson J., Arnold M., Clauß C., Elmqvist H., et al. 
Functional mockup interface 2.0: the standard for tool independent exchange of 
simulation models. Proceedings, München: 2012.
[163] Vering C, Mehrfeld P, Nürenberg M, Coakley D, Lauster M, Müller D. Unlocking 
potentials of building energy systems’ operational efficiency: application of 
digital twin design for HVAC systems. Italy: Rome; 2019. p. 1304–10. https://doi. 
org/10.26868/25222708.2019.210257.
[164] Murashov I, Zverev S, Smorodinov V, Grachev S. Development of digital twin of 
high frequency generator with self-excitation in Simulink. IOP Conf Ser: Mater Sci 
Eng 2019;643:012078. https://doi.org/10.1088/1757-899X/643/1/012078.
[165] Rodemann T, Unger R. Smart company digital twin 2018:9.
[166] Fritzson P. The openmodelica environment for building digital twins of 
sustainable cyber-physical systems. In: 2021 Winter Simulation Conference 
(WSC). Phoenix, AZ, USA: IEEE; 2021. p. 1–12. https://doi.org/10.1109/ 
WSC52266.2021.9715443.
[167] Khayatian F., Cai H., Bojarski A., Heer P., Bollinger A. Benchmarking HVAC 
controller performance with a digital twin, Ningbo, China: 2022.
[168] Harish VSKV, Kumar A. A review on modeling and simulation of building energy 
systems. Renew Sustain Energy Rev 2016;56:1272–92. https://doi.org/10.1016/ 
j.rser.2015.12.040.
[169] Fonseca JA, Nguyen T-A, Schlueter A, Marechal F. City energy analyst (CEA): 
integrated framework for analysis and optimization of building energy systems in 
neighborhoods and city districts. Energy Build 2016;113:202–26. https://doi.org/ 
10.1016/j.enbuild.2015.11.055.
[170] Li Y, O’Neill Z, Zhang L, Chen J, Im P, DeGraw J. Grey-box modeling and 
application for building energy simulations - a critical review. Renew Sustain 
Energy Rev 2021;146:111174. https://doi.org/10.1016/j.rser.2021.111174.
[171] Fritzson P., Engelson V. Modelica — a unified object-oriented language for system 
modeling and simulation. In: Jul E, editor. ECOOP’98 — object-oriented 
programming, vol. 1445, Berlin, Heidelberg: Springer Berlin Heidelberg; 1998, p. 
67–90. https://doi.org/10.1007/BFb0054087.
[172] Westermann P, Rousseau G, Evins R. Buildingenergy.ninja: a web-based surrogate 
model for instant building energy time series for any climate. J Phys: Conf Ser 
2021;2042:012012. https://doi.org/10.1088/1742-6596/2042/1/012012.
[173] Drgoˇna J, Tuor AR, Chandan V, Vrabie DL. Physics-constrained deep learning of 
multi-zone building thermal dynamics. Energy Build 2021;243:110992. https:// 
doi.org/10.1016/j.enbuild.2021.110992.
[174] Khayatian F., Bollinger A., Heer P. Temporal resolution of measurements and the 
effects on calibrating building energy models. arXiv:201108974 [Eess] 2020.
[175] Arendt K, Jradi M, Shaker H, Veje C. COMPARATIVE analysis of WHITE-, gray- 
and black-box models for thermal simulation of indoor ENVIRONMENT: teaching 
building case study, 8. ASHRAE/IBPSA-USA; 2018. p. 173–80.
[176] Marzullo T, Dey S, Long N, Leiva Vilaplana J, Henze G. A high-fidelity building 
performance simulation test bed for the development and evaluation of advanced 
controls. J Build Perfor Simul 2022;15:379–97. https://doi.org/10.1080/ 
19401493.2022.2058091.
[177] Maasoumy M, Razmara M, Shahbakhti M, Vincentelli AS. Handling model 
uncertainty in model predictive control for energy efficient buildings. Energy 
Build 2014;77:377–92. https://doi.org/10.1016/j.enbuild.2014.03.057.
[178] Coakley D, Raftery P, Keane M. A review of methods to match building energy 
simulation models to measured data. Renew Sustain Energy Rev 2014;37:123–41. 
https://doi.org/10.1016/j.rser.2014.05.007.
[179] VanDerHorn E, Mahadevan S. Digital Twin: generalization, characterization and 
implementation. Decis Support Syst 2021;145:113524. https://doi.org/10.1016/ 
j.dss.2021.113524.
[180] Huang ZF, Soh KY, Islam MR, Chua KJ. Digital twin driven life-cycle operation 
optimization for combined cooling heating and power-cold energy recovery 
(CCHP-CER) system. Appl Energy 2022;324:119774. https://doi.org/10.1016/j. 
apenergy.2022.119774.
[181] Chatzivasileiadis S, Venzke A, Stiasny J, Misyris G. Machine learning in power 
systems: is it time to trust it? IEEE Power Energy Mag 2022;20:32–41. https://doi. 
org/10.1109/MPE.2022.3150810.
[182] Singh S, Weeber M, Birke K-P. Advancing digital twin implementation: a toolbox 
for modelling and simulation. Procedia CIRP 2021;99:567–72. https://doi.org/ 
10.1016/j.procir.2021.03.078.
[183] Issermann M, Chang F-J, Kow P-Y. Interactive urban building energy modelling 
with functional mockup interface of a local residential building stock. J Clean 
Prod 2021;289:125683. https://doi.org/10.1016/j.jclepro.2020.125683.
[184] Wetter M., Benne K., Gautier A., Nouidui T.S., Ramle A., Roth A., et al. Lifting the 
garage door on spawn, an open-source bem- controls engine 2020:8.
[185] SOEP. Spawn of EnergyPlus 2020. https://lbl-srg.github.io/soep/(accessed June 
13, 2023).
[186] Lydon GP, Caranovic S, Hischier I, Schlueter A. Coupled simulation of thermally 
active building systems to support a digital twin. Energy Build 2019;202:109298. 
https://doi.org/10.1016/j.enbuild.2019.07.015.
[187] Wetter M, Zuo W, Nouidui TS, Pang X. Modelica buildings library. J Build Perfor 
Simul 2014;7:253–70. https://doi.org/10.1080/19401493.2013.765506.
[188] Merkel D. Docker: lightweight linux containers for consistent development and 
deployment 2014. https://dl.acm.org/doi/fullHtml/10.5555/2600239.2600241
(accessed October 11, 2022).
[189] Clausen A, Arendt K, Johansen A, Sangogboye FC, Kjærgaard MB, Veje CT, et al. 
A digital twin framework for improving energy efficiency and occupant comfort 
in public and commercial buildings. Energy Inform 2021;4:40. https://doi.org/ 
10.1186/s42162-021-00153-9.
[190] Chen K, Zhu X, Anduv B, Jin X, Du Z. Digital twins model and its updating method 
for heating, ventilation and air conditioning system using broad learning system 
algorithm. Energy 2022;251:124040. https://doi.org/10.1016/j. 
energy.2022.124040.
[191] Nutkiewicz A, Choi B, Jain RK. Exploring the influence of urban context on 
building energy retrofit performance: a hybrid simulation and data-driven 
approach. Adv Appl Energy 2021;3:100038. https://doi.org/10.1016/j. 
adapen.2021.100038.
[192] Jain RK, Qin J, Rajagopal R. Data-driven planning of distributed energy resources 
amidst socio-technical complexities. Nat Energy 2017;2:17112. https://doi.org/ 
10.1038/nenergy.2017.112.
[193] Jafari MA, Zaidan E, Ghofrani A, Mahani K, Farzan F. Improving building energy 
footprint and asset performance using digital twin technology. IFAC- 
PapersOnLine 2020;53:386–91. https://doi.org/10.1016/j.ifacol.2020.11.062.
[194] Srinivasan RS, Manohar B, Issa RRA. Urban building energy CPS (UBE-CPS): real- 
time demand response using digital twin. In: Anumba CJ, Roofigari-Esfahan N, 
editors. Cyber-Physical systems in the built environment. Cham: Springer 
International Publishing; 2020. p. 309–22. https://doi.org/10.1007/978-3-030- 
41560-0_17.
[195] Testasecca T, Lazzaro M, Sirchia A. Towards Digital Twins of buildings and smart 
energy networks: current and future trends. In: 2023 IEEE International 
Workshop on Metrology for Living Environment (MetroLivEnv). Milano, Italy: 
IEEE; 2023. p. 96–101. https://doi.org/10.1109/ 
MetroLivEnv56897.2023.10164035.
[196] Khan AH, Omar S, Mushtary N, Verma R, Kumar D, Alam S. Digital twin and 
artificial intelligence incorporated with surrogate modeling for hybrid and 
sustainable energy systems. In: Fathi M, Zio E, Pardalos PM, editors. Handbook of 
smart energy systems. Cham: Springer International Publishing; 2022. p. 1–23. 
https://doi.org/10.1007/978-3-030-72322-4_147-1.
[197] Shen Z, Arra˜no-Vargas F, Konstantinou G. Artificial intelligence and digital twins 
in power systems: trends, synergies and opportunities. Digitaltwin 2023;2:11. 
https://doi.org/10.12688/digitaltwin.17632.2.
[198] Ssin S, Cho H, Woo W. A-UDT: augmented urban digital twin for visualization of 
virtual and real IoT data. editors. In: Tom Dieck MC, Jung TH, Loureiro SMC, 
editors. Augmented reality and virtual reality. Cham: Springer International 
Publishing; 2021. p. 221–36. https://doi.org/10.1007/978-3-030-68086-2_17.
[199] Lu Q, Jiang H, Chen S, Gu Y, Gao T, Zhang J. Applications of digital twin system 
in a smart city system with multi-energy. In: 2021 IEEE 1st International 
Conference on Digital Twins and Parallel Intelligence (DTPI). Beijing, China: 
IEEE; 2021. p. 58–61. https://doi.org/10.1109/DTPI52967.2021.9540135.
[200] Gai K, Xiao Q, Qiu M, Zhang G, Chen J, Wei Y, et al. Digital twin-enabled AI 
enhancement in smart critical infrastructures for 5G. ACM Trans Sen Netw 2022; 
18:1–20. https://doi.org/10.1145/3526195.
[201] Tegler E. The vulnerability of AI systems may explain why Russia isn’t using them 
extensively in Ukraine. Forbes n.d. https://www.forbes.com/sites/erictegler/20 
22/03/16/the-vulnerability-of-artificial-intelligence-systems-may-explain-why-th 
ey-havent-been-used-extensively-in-ukraine/(accessed April 9, 2024).
[202] Agostinelli S, Cumo F, Nezhad MM, Orsini G, Piras G. Renewable Energy system 
controlled by open-source tools and digital twin model: zero energy port area in 
Italy. Energies 2022;15:1817. https://doi.org/10.3390/en15051817.
[203] White G, Zink A, Codec´a L, Clarke S. A digital twin smart city for citizen feedback. 
Cities 2021;110:103064. https://doi.org/10.1016/j.cities.2020.103064.
[204] Schrotter G, Hürzeler C. The digital twin of the City of Zurich for urban planning. 
PFG 2020;88:99–112. https://doi.org/10.1007/s41064-020-00092-2.
B. Koirala et al.                                                                                                                                                                                                                                 
Advances in Applied Energy 16 (2024) 100196 
21 


---

Page 22

---

[205] Stadt Zürich. Digital Twin - Stadt Zürich 2023. https://www.stadt-zuerich.ch/po 
rtal/de/index/politik_u_recht/stadtrat/weitere-politikfelder/smartcity/english 
/projects/zwilling.html (accessed April 12, 2023).
[206] Virtual Singapore. Virtual Singapore 2023. https://www.nrf.gov.sg/programme 
s/virtual-singapore (accessed April 12, 2023).
[207] Caprari G, Castelli G, Montuori M, Camardelli M, Malvezzi R. Digital twin for 
urban planning in the green deal era: a state of the art and future perspectives. 
Sustainability 2022;14:6263. https://doi.org/10.3390/su14106263.
[208] H¨am¨al¨ainen M. Urban development with dynamic digital twins in Helsinki city. 
IET Smart Cit 2021;3:201–10. https://doi.org/10.1049/smc2.12015.
[209] Ruohomaki T, Airaksinen E, Huuska P, Kesaniemi O, Martikka M, Suomisto J. 
Smart city platform enabling digital twin. In: 2018 International Conference on 
Intelligent Systems (IS). Funchal - Madeira, Portugal: IEEE; 2018. p. 155–61. 
https://doi.org/10.1109/IS.2018.8710517.
[210] Dublinked. Dublin’s open data portal 2024. https://data.smartdublin. 
ie/(accessed October 21, 2024).
[211] García ´O, Alonso RS, Prieto J, Corchado JM. Energy efficiency in public buildings 
through context-aware social computing. Sensors 2017;17:826. https://doi.org/ 
10.3390/s17040826.
[212] Shahinmoghadam M, Natephra W, Motamedi A. BIM- and IoT-based virtual 
reality tool for real-time thermal comfort assessment in building enclosures. Build 
Environ 2021;199:107905. https://doi.org/10.1016/j.buildenv.2021.107905.
[213] Bojarski A., Khayatian F., Cai H. nestli: Neighborhood energy system testing 
towards large-scale integration 2023.
[214] Darbali-Zamora R, Johnson J, Summers A, Jones CB, Hansen C, Showalter C. State 
estimation-based distributed energy resource optimization for distribution 
voltage regulation in telemetry-sparse environments using a real-time digital 
twin. Energies 2021;14:774. https://doi.org/10.3390/en14030774.
[215] Saad A, Faddel S, Youssef T, Mohammed OA. On the implementation of iot-based 
digital twin for networked microgrids resiliency against cyber attacks. IEEE Trans 
Smart Grid 2020;11:5138–50. https://doi.org/10.1109/TSG.2020.3000958.
[216] Christakou K, Pignati M, Rudnik R, Sarri S, Le Boudec J-Y, Paolone M. Hardware- 
in-the-loop validation of the grid explicit congestion notification mechanism for 
primary voltage control in active distribution networks. In: 2016 Power Systems 
Computation Conference (PSCC). Genoa, Italy: IEEE; 2016. p. 1–7. https://doi. 
org/10.1109/PSCC.2016.7540876.
[217] Fan C, Zhang C, Yahja A, Mostafavi A. Disaster City Digital Twin: a vision for 
integrating artificial and human intelligence for disaster management. Int J Inf 
Manage 2021;56:102049. https://doi.org/10.1016/j.ijinfomgt.2019.102049.
[218] Invernizzi DC, Locatelli G, Velenturf A, Love PED, Purnell P, Brookes NJ. 
Developing policies for the end-of-life of energy infrastructure: coming to terms 
with the challenges of decommissioning. Energy Pol 2020;144:111677. https:// 
doi.org/10.1016/j.enpol.2020.111677.
[219] Mˆeda P, Calvetti D, Hjelseth E, Sousa H. Incremental digital twin 
conceptualisations targeting data-driven circular construction. Buildings 2021;11: 
554. https://doi.org/10.3390/buildings11110554.
[220] Preut A, Kopka J-P, Clausen U. Digital twins for the circular economy. 
Sustainability 2021;13:10467. https://doi.org/10.3390/su131810467.
[221] Chen Z, Huang L. Digital twin in circular economy: remanufacturing in 
construction. IOP Conf Ser: Earth Environ Sci 2020;588:032014. https://doi.org/ 
10.1088/1755-1315/588/3/032014.
[222] Rocca R, Rosa P, Sassanelli C, Fumagalli L, Terzi S. Integrating virtual reality and 
digital twin in circular economy practices: a laboratory application case. 
Sustainability 2020;12:2286. https://doi.org/10.3390/su12062286.
[223] Enzer M. Guest post: mark Enzer on the ‘national digital twin’ – The ODI 2020. htt 
ps://theodi.org/article/guest-blog-mark-enzer-on-the-national-digital-twin/
(accessed February 28, 2022).
[224] IEC 61850. Distributed energy resources – IEC 61850 2023. https://iec61850.dvl. 
iec.ch/what-is-61850/targeted-markets/distrib_resources/(accessed May 26, 
2023).
[225] ISO/IEC. ISO/IEC 20924:2021. ISO n.d. https://www.iso.org/standard/82771. 
html (accessed May 26, 2023).
[226] Sacks R, Eastman C, Lee G, Teicholz P. BIM handbook: a guide to building 
information modeling for owners, designers, engineers, contractors, and facility 
managers. Hoboken, New Jersey: John Wiley & Sons, Inc.; 2018. https://doi.org/ 
10.1002/9781119287568.
[227] European Commission. Directorate general for research and innovation. 
Technology readiness level: guidance principles for renewable energy 
technologies : final report. LU: Publications Office; 2017.
B. Koirala et al.                                                                                                                                                                                                                                 
Advances in Applied Energy 16 (2024) 100196 
22 
