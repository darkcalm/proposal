

---

Page 1

---

Open Access
© The Author(s) 2024. Open Access  This article is licensed under a Creative Commons Attribution 4.0 International License, which permits 
use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original 
author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third 
party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the mate‑
rial. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or 
exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://​
creat​iveco​mmons.​org/​licen​ses/​by/4.​0/.
REVIEW
Cespedes‑Cubides and Jradi ﻿
Energy Informatics            (2024) 7:11  
https://doi.org/10.1186/s42162-024-00313-7
Energy Informatics
A review of building digital twins to improve 
energy efficiency in the building operational 
stage
Andres Sebastian Cespedes‑Cubides1* and Muhyiddine Jradi1 
Abstract 
The majority of Europe’s building stock consists of facilities built before 2001, pre‑
senting a substantial opportunity for energy efficiency improvements during their 
operation and maintenance phase. Digitalizing these buildings with digital twin 
technology can significantly enhance their energy efficiency. Reviewing the applica‑
tions and trends of digital twins in this context is beneficial to understand the cur‑
rent state of the art and the specific challenges encountered when applying this 
technology to older buildings. This study focuses on the application of digital twins 
in building operations and maintenance (O & M), emphasizing energy efficiency 
throughout the building lifetime. A systematic process to select 21 pertinent use-case 
studies was performed, complemented by an analysis of six enterprise-level digital 
twin solutions. This was followed by an overview of general characteristics, thematic 
classification, detailed individual study analyses, and a comparison of digital twin 
solutions with commercial tools. Five main applications of digital twins were identified 
and examined: component monitoring, anomaly detection, operational optimization, 
predictive maintenance and simulation of alternative scenarios. The paper highlights 
challenges like the reliance on Building Information Modeling (BIM) and the need 
for robust data acquisition systems. These limitations hinder the implementation 
of digital twins, in particular in existing buildings with no digital information available. 
It concludes with future research directions emphasizing the development of methods 
not solely reliant on BIM data, integration challenges, and potential enhancements 
through AI and machine learning applications.
Keywords:  Digital twin, Energy efficiency, Operation, Maintenance, Building 
Information Modeling (BIM), Energy Modeling, IoT system
Introduction
Buildings within the European Union consume nearly 40% of the total energy consump-
tion (European commission 2018). According to the International Energy Agency (IEA), 
the buildings and construction sector is responsible for approximately 36% of total emis-
sions (European Parliament 2023), with 22% coming from residential buildings, 8% from 
non-residential buildings, and 6% from construction projects and industries (IEA 2019). 
Because of this, the buildings sector holds great potential for achieving cost-effective 
*Correspondence:   
acub@mmmi.sdu.dk
1 Mærsk McKinley Møller 
Institute, University of Southern 
Denmark, Campusvej 55, 
5230 Odense, Denmark


---

Page 2

---

Page 2 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
improvements in efficiency and substantial proportional reductions in greenhouse gas 
emissions (European commission 2020).
To meet the ambitious energy and environmental targets set for 2030 and 2050, the 
EU has placed a strong emphasis on the construction and buildings sector through the 
energy performance of buildings directive (European Parliament 2010). The revised 
directive aims to increase the rate of building renovation, specially for the worst-per-
forming buildings and supports better air quality, the digitalisation of energy systems for 
buildings and the roll-out of infrastructure for sustainable mobility.
However, the global implementation of energy efficiency measures in existing build-
ings is lacking and falls far short of the necessary actions to achieve net-zero carbon 
dioxide emissions by 2050. This is evident from the fact that existing buildings still make 
up the majority, accounting for over 97% of the building stock (Arup 2023b). The EU’s 
building stock, for instance, consists of more than 220 million units, with 85% of them 
constructed before 2001. It is projected that around 85–95% of these buildings will still 
be in existence by 2050 (Fufa et al. 2021). The majority of these buildings are energy inef-
ficient, relying on fossil fuels for heating and cooling and employing outdated technolo-
gies and wasteful appliances.
In general, the majority of buildings are in the operational stage of their life cycle. 
This also means that, depending on the age of the building, the available information 
and level of digitalisation can vary greatly. A considerable opportunity arises for incor-
porating digital technologies to contribute to reduce energy demand as well as enhance 
comfort. This transformation aligns with the continuous progress in communication 
and information technologies, together with the advancement and establishment of 
interconnected and intelligent grids. These buildings should adapt their operations to 
changes in the energy grid and occupant behaviour, as well as enable strategic mainte-
nance. By reducing energy consumption in buildings, it is possible to reduce greenhouse 
gas emissions and mitigate the impact of climate change. Additionally, improving energy 
and maintenance efficiency in buildings can also result in cost savings for building own-
ers and occupants, as well as potential better indoor comfort levels (Volk et al. 2013). 
The digitization of building data is a key catalyst in this context, expanding rapidly across 
various sectors within the building industry and construction sector.
The increasing interest to de-carbonize the building stock, the public directives aimed 
towards improving energy efficiency and the increasing capabilities of digital and sta-
tistical methods are major incentives to describe the current state of the digital twins 
for buildings technologies. This research aims to systematically evaluate strategies for 
boosting energy efficiency in buildings with diverse digital integrations. Emphasizing the 
role of digital twins in operational energy optimization, the research will examine their 
usage in building operations, identifying prevalent implementation patterns. Further-
more, it will scrutinize case studies to evaluate the advantages and outline the current 
and potential capabilities offered by digital twin technologies in buildings.
Recent developments on digitalisation for the construction sector have been con-
nected with Building Information Modeling (BIM) (ISO 2021) models providing a 
source of truth during the design and construction phases of a building. It facilitates 
the collaboration between Architecture, Engineering and construction (AEC) profes-
sionals, making it widespread over the last decades (Lu et al. 2020a). Furthermore, 


---

Page 3

---

Page 3 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
	
BIM models have also been used for running simulations to provide insights about 
the expected performance of the building or to assist the construction process (Pent-
tilä et al. 2022).
However, traditional BIM techniques provide only static analysis with no data-
exchange between sensors and the digital model. This is a problem addressed by the 
concept of digital twins.
Digital twining techniques, initially utilized within Aerospace and Manufactur-
ing, have now extended to applications throughout a building’s life cycle as shown in 
Fig. 1. A digital twin is a digital and/or mathematical model of a physical asset which 
integrates sensor readings and a form of data exchange between the digital model and 
the physical asset. The trend of utilizing digital twins and modeling for buildings has 
been gaining popularity (Bortolini et al. 2022). With the help of an Internet of Things 
(IoT) system comprised of sensors, a data pipeline and a data processing and analysis 
system, the BIM models can be extended into Digital Twins which reflect in a more 
precise way the behavior and properties of the modeled building, during any phase of 
its life-cycle (Lu et al. 2020b; Bortolini et al. 2022; Hou et al. 2023)  (Fig. 2).
The potential of connecting BIM and IoT-based data sources is a relatively new 
development. As a generalization, BIM and IoT data offer complementary views of 
the project that together supplement the limitations of each. BIM models offer high 
fidelity representations of the project at the component level. IoT data can bring to 
the table near-real-time operation data and performance statistics (Lu et al. 2020b).
An obstacle impeding the broad adoption of digital building twins is that a sig-
nificant number of the constructions present in the usual city were designed and 
built before the digital era. At the same time, implementation and completeness 
of BIM models in recent buildings is also scarce (Volk et al. 2013). As a result, the 
Fig. 1  Diagram of a building digital twin (Jradi and Bjørnskov 2023)


---

Page 4

---

Page 4 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
incorporation of IoT technologies and software might not be easily supported by an 
existing and accessible BIM model.
Given the potential benefits from implementing digital twins in the built environment, 
the trends to use BIM models for achieving digital twins and while also acknowledging 
the limitations of this method due to the older age of much of the building stock. The 
aim in this paper is also to provide a comprehensive overview of various digital twin use 
cases, both with and without the use of BIM. This includes an analysis of their architec-
ture, implementation, and the benefits reported. Additionally, the study describes what a 
typical digital twin solution looks like for existing buildings and discusses both the ben-
efits and challenges of implementing these technologies in the building stock.
The primary aim of this research is to systematically explore and evaluate a range of 
scholarly works focused on the application of digital twins in the domain of building 
operations and maintenance (O & M). To this end, a methodical review system will be 
employed.
Subsequent sections of this study detail the methodology adopted for selecting the 
case studies that form the basis of this analysis. The paper then proceeds to present an 
overview of the key findings from these studies, offering a thematic classification of the 
topics covered. This is followed by a comprehensive description of each selected case 
study. Later sections provide in-depth insights and discuss emerging trends observed in 
the research. This includes a critical analysis and comparison of digital twin solutions 
with existing commercial tools. The paper concludes by identifying the challenges faced 
in this field and outlining potential future directions for the technology.
Research methodology
“Search for previous studies” section and Fig. 3 provide an outline of the methodology 
used for this review. The process begins with a search of previous studies using plat-
forms like Google Scholar and review papers. Cross-referencing and AI tools such as 
Elicit and ResearchRabbit are then used to compile scholarly articles. Studies pertinent 
to digital twins for building O & M that have a use case implementation are selected. 
Metadata from these studies is extracted for individual analyses and to classify them by 
topic. The analysis includes evaluating the level of data integration and the technology 
used. Studies that do not meet the criteria are discarded.
Fig. 2  Benefits of digital twins for O & M in buildings (Pressac 2018). A Digital twin for buildings can enable 
services that enhance the building operation stage


---

Page 5

---

Page 5 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
	
Search for previous studies
The initial screening for studies related to digital twins for building started by using a 
term search with Google Scholar, the search terms were:
•	 Digital twins for buildings.
•	 Digital twins for building energy efficiency.
The results where then prioritized based on the default google page rankings and the 
number of citations. The initial google scholar results revealed a large proportion of 
the papers related to the search terms to be reviewing papers. The initial selection of 
papers was made using the following heuristic: 
1.	 Search of terms with google scholar.
2.	 Discard reviewing papers.
3.	 Choose papers with at least 5 citations provided by the default google scholar rank-
ing.
4.	 Add papers with less citations but deemed relevant for the purpose of this study by 
using the AI cross-referencing tools.
5.	 Take into account two of the most recent review papers and 2 of the most cited 
review papers.
Fig. 3  Methodology for selecting and analyzing studies on digital twins for building operations and 
maintenance (O & M)


---

Page 6

---

Page 6 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
A filtering process followed using the scientific AI tool Elicit (2023) which uses language 
models and cross-referencing to provide summaries and an overview of the public feed-
back given to each paper. Additionally a cross-citation search was made with the help of 
the tool ResearchRabbit (2023) by generating a cross-citation graph as shown in Fig. 4 
which provides an extended view of the relation between studies and unveils relevant 
studies in the field. This process yielded an initial group of 150 studies from the literature 
and 4 review papers was selected.
Adhering to the criteria of seeking digital twins for buildings in their operational 
phase, a list of studies using the Mendeley Reference Manager was compiled. This pro-
cess yielded 21 use-case studies that were identified as pertinent to this review.
This study aims to provide a detailed overview of current digital twin solutions for 
modern buildings. To achieve this, a qualitative analysis of prominent market-available 
digital twin technologies was conducted. The focus was on solutions applicable during 
the operational phase of buildings, aligning with the digital twin definition presented in 
Fig. 4  Network graph from ResearchRabbit illustrating connections between research works. Use cases are 
marked in green, while related works are shown in blue. This interactive tool aids in discovering relevant 
papers that might otherwise be overlooked. However, its scope is confined to the range of public databases 
it utilizes


---

Page 7

---

Page 7 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
	
the previous “Introduction” section and Fig. 1. This analysis is conducted with the inten-
tion of shedding light on the fundamental distinctions between enterprise-level digital 
twin solutions and custom, in-house digital twin implementations. A process for col-
lecting and scrutinizing six enterprise-level digital twin solutions, details of which are 
elaborated in the subsequent sections of this document.
Analysis process
In order to extract the most relevant characteristics from the list of articles, the follow-
ing steps were taken:
Metadata extraction from the selected studies
From the resulting studies a data extraction was made, listing year, place of the study, 
number of citations and a brief description of the study. This description served as the 
starting point for the classification by topic.
Classification by topic
An attempt to provide a classification for the reviewed studies based on the main benefit 
of the use case implementation was made. All related to enhancements achieved during 
the operation stage.
Individual analyses
A more detailed analysis was carried out, reviewing the overall structure of the imple-
mented digital twin solution, the reported results and the reported challenges.
Expected similarities & differences
Given the experimental nature of the use-cases in these studies, it is expected to find 
variations in the scope and magnitude of each digital twin implementation. Similarly, the 
specific advantages and applications of each will differ. The focus here is on identifying 
diverse modeling methods, as well as contrasting hardware and software architectures. 
There is a particular interest in studies that either incorporate Building Information 
Modeling (BIM) or proceed without it.
Despite these differences, some commonalities among the studies are also expected, 
particularly concerning the fundamental structure of the digital twins and the flow of 
information between the physical asset and its digital counterpart. Moreover, given the 
increasing prevalence of machine learning, its application is foreseen in many use cases. 
Lastly, it is anticipated that these digital twins will yield insights leading to enhanced effi-
ciency, potentially even achieving this efficiency autonomously.
Results
General characteristics from metadata
These papers span from 2016 to 2023, showing a noticeable upward trend in the number 
of publications each year Fig. 5.
The use cases that draw the most attention are summarized in Table 1. However, the 
papers that gather the most attention are the review papers which compile a number of 
previous studies and analyze them (Boje et al. 2020; Yitmen et al. 2021).


---

Page 8

---

Page 8 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
Topics of the studies
Focusing mainly on the application and specific benefit obtained from the digital twin 
implementation, the identified recurrent topics were:
•	 Component monitoring
•	 Anomaly detection
•	 Operational optimization
•	 Predictive maintenance
•	 Simulation of Scenarios
Table 2 lists the category of each analyzed article.
Fig. 5  Number of publications per year (As of September 2023)
Table 1  First five studies organized by number of citations
Name
Main author
Year
Country
Citations
Digital Twin: Vision, benefits,
boundaries, and creation for buildings (Khajavi et al. 2019)
Khajavi, S. H.
2019
Finland
212
Developing a Digital Twin at
Building and City Levels: Case
Study of West Cambridge Campus (Lu et al. 2020c)
Lu, Q.
2020
UK
145
Digital twin aided sustainability-based
lifecycle management for railway
turnout systems (Kaewunruen and Lian 2019)
Kaewunruen, S.
2019
UK
122
Digital Twin Hospital Buildings:
An Exemplary Case Study
through Continuous Lifecycle Integration (Peng et al. 2020)
Peng, Y.
2020
China
62
Digital twin-enabled anomaly
detection for built asset monitoring
in operation and maintenance (Lu et al. 2020d)
Lu, Q.
2020
UK
56


---

Page 9

---

Page 9 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
	
Individual analyses
In order to provide a structured overview of the energy efficiency aspect of each digital 
twin use-case a general description of each case is provided, followed by a summarizing 
list highlighting the aspects that are more relevant to this review, these aspects are:
•	 Reported energy efficiency improvement: Qualitative overview of the claimed ben-
efits of the study’s implementation relative to energy efficiency only.
•	 Reported benefits: Qualitative overview of the claimed potential benefits of the DT, 
not only constrained to energy efficiency.
•	 Reported quantitative improvements from DT: Quantitative improvements reported 
from implementing the digital twin, for example, percentages of cost reduction and 
energy efficiency gains.
•	 Technology highlights: Key technologies utilized in the implementation/design of 
the DT, specially in the data acquisition and data processing aspect.
Component monitoring
Khajavi et al. (2019) described a research project involving four rounds of experimen-
tation, resulting in the collection and analysis of over 25,000 sensor readings. These 
readings were used to create and test a limited digital twin of an office building facade 
element. The research introduces a method to establish a real-time digital twin using a 
sensor network. It entails gathering and analyzing specific environmental factors from 
the building’s surroundings. While the study used a modest sensor network to monitor 
light, temperature, and humidity, the outlined framework could be adapted for a more 
comprehensive digital twin of the building’s facade and interior. The paper also addresses 
technical challenges in digital twin creation and offers potential solutions. It proposes 
a sensor arrangement framework for enabling digital twin functionality on a building 
facade and discusses advantages like cost savings and tenant comfort improvement. The 
research primarily focuses on the building facade, but it suggests future exploration into 
applying digital twins to building interiors. The idea of expanding the sensor network 
for enhanced applications, including security and movement monitoring, is also raised. 
Lastly, the study emphasizes the importance of evaluating the system’s cost-effectiveness 
relative to its benefits.
Table 2  Themes identified and the respective papers addressing them
Theme
Publications
1. Component monitoring
 Khajavi et al. (2019), Li et al. (2022)
2. Anomaly detection
 Bjørnskov et al. (2022), Lu et al. (2020d, 2020)
3. Operational Optimization
 Bjørnskov and Jradi (2023), Chiara Tagliabue et al. 
(2021), Clausen et al. (2021), Jradi and Bjørnskov (2023), 
Lee et al. (2016), Moretti et al. (2020), Peng et al. (2020), 
Wang et al. (2022), Zaballos et al. (2020), Zhao et al. 
(2022), Agostinelli et al. (2022)
4. Predictive maintenance
 Hosamo et al. (2022), Ni et al. (2021, 2022)
5. Simulation of alternative
scenarios
 Agostinelli et al. (2021), Kaewunruen and Lian (2019)


---

Page 10

---

Page 10 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
•	 Reported energy efficiency improvements: Possibility for finer temperature and light-
ing control.
•	 Reported benefits: Lowering maintenance cost, lower management and operational 
cost.
•	 Reported quantitative improvements from DT: None
•	 Technology highlights: Bluetooth, WiFi, Python, CSV format.
 Li et al. (2022) introduced a new solution to connect Digital Twins (DTs) with intelligent 
buildings by creating a foundational model for Building Digital Twins (BDTs). This model 
includes static information, a physical representation, and interaction mapping for vir-
tual representation of physical buildings. The paper discusses sub-model characteristics, 
collaboration between models, real-time sensing, and feedback control. The proposed 
approach offers a platform-independent method for describing BDTs and ensures the 
foundation model’s validity. A case study demonstrates real-time operation and mainte-
nance using a chiller DT, validating the effectiveness of the model. However, the paper 
lacks in-depth technology implementation discussions and doesn’t fully explore dynamic 
evolution. The presented case study is relatively simple, suggesting future work should 
focus on more complex systems to validate the model further.
•	 Reported energy efficiency improvements: Improve chiller’s coefficient of perfor-
mance (COP) by manipulating the chiller setpoints more intelligently.
•	 Reported benefits: Lower management and operational cost, less energy consump-
tion.
•	 Reported quantitative improvements from DT: An increase in the chiller’s COP of 
around 40% when optimization active.
•	 Technology highlights: IFC, WebGL, Python, Modbus.
Anomaly detection
Bjørnskov et al. (2022) introduced a systematic method for retro-commissioning, which 
emphasizes rectifying issues and irregularities in retrofitted facilities. The study uses a 
hospital in Odense, Denmark as a case example, showcasing a dynamic model-based 
solution to retro-commissioning various building components. This technique involves 
identifying faults by applying predetermined thresholds, revealing problems like improp-
erly functioning cooling coils. Despite the increasing interest in retrofitting buildings, 
many countries still have gaps in retro-commissioning procedures. The approach rec-
ommended in the paper is adaptable and scalable, suitable for diverse building types and 
locations, necessitating minor adjustments to suit specific systems. The utilization of 
clamp-on sensors for data collection and calibration is a practical and widely applicable 
solution. Developing and fine-tuning a dynamic energy model marks the initial stages 
of implementing continuous commissioning within the BuildCOM (Jradi et  al. 2021) 
research project.
•	 Reported energy efficiency improvements: Better energy models, provide a better 
baseline for measuring energy efficiency.


---

Page 11

---

Page 11 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
	
•	 Reported benefits: More realistic monitoring and forecasting of energy usage, more 
accurate detection of improper operation.
•	 Reported quantitative improvements from DT: None
•	 Technology highlights: EnergyPlus, Clamp-on sensors, WiFi & cellular internet.
 Lu et al. (2020d) created a Digital Twin (DT)-enabled anomaly detection system to com-
prehensively monitor building assets during the operations and maintenance (O & M) 
phase. It introduces a novel DT-based anomaly detection process flow that integrates 
data, enhances decision-making, and automates the detection process. The study also 
designed a data integration structure based on IFC (ISO 2018) extension for diverse 
operational data management. The framework’s efficacy was demonstrated through a 
case study involving HVAC system pumps, highlighting its ability to continuously moni-
tor building assets and streamline daily O & M management.
•	 Reported energy efficiency improvements: None
•	 Reported benefits: More accurate and faster detection of improper operation.
•	 Reported quantitative improvements from DT: None.
•	 Technology highlights: IFC, BMS
 Lu et al. (2020c) presented the development of a DT system architecture and presents 
a DT demonstrator for the West Cambridge site, focusing on a building-level DT. The 
challenges of DT development, particularly related to data management, are thoroughly 
analyzed, and lessons learned are discussed. The study offers a novel system architecture 
for future research, showcasing one of the early exploratory pilot projects for building 
and city-level DTs. It provides a road-map for future research while acknowledging the 
need for organized guidance to tackle data management challenges. The paper doesn’t 
extensively cover the value of integrating city-level information, which is suggested as 
a topic for future research. The authors plan to collect occupant feedback, collaborate 
with the University of Cambridge’s Estate Management Department, validate the system 
architecture on a broader city scale, and explore practical applications of DTs in diverse 
management activities and services.
•	 Reported energy efficiency improvements: None
•	 Reported benefits: Anomaly detection, maintenance optimization, support for deci-
sion-making
•	 Reported quantitative improvements from DT: None
•	 Technology highlights: IFC, cellular internet, radio frequency, cloud databases.
Operational optimization
Bjørnskov and Jradi (2023) introduced an energy modeling framework rooted in the 
SAREF (2023) ontology, emphasizing modular data-driven models. Using SAREF4BLDG 
(2020) and SAREF4SYST (Kukkonen et al. 2022) extensions, the framework links model 
inputs and outputs systematically. This foundation will be extended to real buildings, 
incorporating devices, sensors, and diverse services. Utilizing SAREF ontology enhances 
interoperability, integration with physical systems, and scalability of DTs, facilitating 


---

Page 12

---

Page 12 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
broader adoption across domains like industry, energy, and smart cities, potentially 
expanding to streets, districts, and cities. The study presents a use case focused on a room 
equipped with temperature and ventilation sensors and controls. It highlights how the 
python framework is applied in a service designed to detect anomalies in components.
•	 Reported energy efficiency improvements: None
•	 Reported benefits: Semantic modeling, anomaly detection, easily integrable and 
extensible.
•	 Reported quantitative improvements from DT: None.
•	 Technology highlights: Ontologies, Python, BMS and IFC.
Tagliabue et al. (2021) discussed the application of a digital twin for assessing sus-
tainability using rating systems like LEED (Green Building Council 2023). The digital 
twin is utilized throughout an asset’s lifecycle, including design and use phases. This 
solution improves building management and real-time sustainability evaluation com-
pared to traditional checklist-based protocols. The eLUX building (Uni Brescia build-
ing 2016), a prototype in the University of Brescia, serves as a case study. Equipped 
with sensors, it collects and displays indoor environmental quality and occupancy 
data. The digital twin supports user behavior by showing a sustainability scoreboard, 
promoting sustainable actions. The text highlights limitations in using a Digital Twin 
(DT) for sustainability purposes, particularly in the creation of a Sustainable Digital 
Twin (SDT). The DT was originally designed with a focus on predictive maintenance, 
indoor air quality, space organization, and energy efficiency. Sustainability assessment 
was added later, causing challenges. The suggestion is to create an SDT specifically for 
sustainability, which could address these issues.
•	 Reported energy efficiency improvements: None
•	 Reported benefits: Near real-time assessment of building sustainability index.
•	 Reported quantitative improvements from DT: None
•	 Technology highlights: NoSQL database, ethernet local area network, BIM.
 Clausen et al. (2021) introduced a Digital Twin Framework for implementing Model 
Predictive Control (MPC) in both physical and simulated buildings. The framework 
encompasses an architecture for building control, occupancy prediction, and data 
format using sMAP. It includes a parameterized Zone Model that can be adjusted for 
controllable zones and a Zone Control Application enabling temperature and CO2 
target configuration. An instance of this framework was applied to control a univer-
sity classroom (room U182) in SDU Odense, Denmark. The experiments showed that 
the system can keep comfort levels comparable to those of commercial control strate-
gies while also allowing for energy-saving approaches. This involves a multi-objective 
optimization problem that balances comfort and energy conservation, such as adjust-
ing variable air volume (VAV) damper positions based on occupancy predictions. 
This improved upon default rule-based strategies. However, due to complex factors 
like the building’s ventilation system and weather fluctuations, quantifying energy 
savings precisely remains challenging.


---

Page 13

---

Page 13 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
	
•	 Reported energy efficiency improvements: Planning energy consumption based on 
grid behavior without compromising occupant comfort.
•	 Reported benefits: Potential for an increase in energy efficiency.
•	 Reported quantitative improvements from DT: None
•	 Technology highlights: Generic data layer, model predictive control, sMAP bus 
(Dawson-Haggerty et al. 2010).
 Jradi and Bjørnskov (2023) presented a complementary paper of their earlier work 
(Bjørnskov and Jradi 2023), it introduces a comprehensive digital twin platform 
designed to enhance the energy efficiency and intelligence of buildings. The plat-
form integrates dynamic data-driven energy models with real-time data from various 
sensors and meters within the building. It replaces traditional Building Information 
Models (BIMs) with dynamic energy models combined with real-time data. The plat-
form provides several key services:
The platform gathers and manages data from various sources within the building, 
creating a user-friendly open-standard context information model. It offers real-time 
tracking, continuous commissioning, and fault detection for effective energy manage-
ment and rapid issue identification. Additionally, it supports optimal decision-making 
through simulations, enabling informed choices and alternate control strategies for 
the building’s lifecycle.
•	 Reported energy efficiency improvements: None
•	 Reported benefits: More accurate, easier to create an maintain models for DTs.
•	 Reported quantitative improvements from DT: None
•	 Technology highlights: Python, building management systems.
 Lee et al. (2016) discussed the use of Building Information Modeling (BIM) and vari-
ous technologies to enhance building energy efficiency. The focus is on using devices 
like sensors, digital meters, and integrated platforms to automate energy-saving 
actions. The paper proposes employing a manager with basic knowledge to oversee 
these systems in a centralized Energy Operation Center (EOC) to reduce manage-
ment costs. BIM is highlighted as a tool for visualizing building equipment data, aid-
ing monitoring, and facilitating smart city management. A case study is presented, 
showing how this approach improves energy efficiency by managing the EOC and 
integrating various technologies. It is estimated that using BIM-based energy effi-
ciency methods could lead to significant energy savings in Sejong City’s (South Korea) 
buildings. The paper concludes that this solution can optimize building energy per-
formance, reduce costs, and minimize environmental impact. The ultimate aim is to 
develop a control unit for a smart city’s energy grid system using the building energy 
integrated operation center.
•	 Reported energy efficiency improvements: Finer and automated control of lighting, 
HVAC and electronic equipment results in a better resource management.
•	 Reported benefits: Energy consumption reduced, constant monitoring and anom-
aly detection a centralized control interface for the building’s systems


---

Page 14

---

Page 14 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
•	 Reported quantitative improvements from DT: 17% energy reduction.
•	 Technology highlights: BACnet, BIM, wireless sensor networks (WSN).
 Moretti et al. (2020) introduced an openBIM methodology aimed at aiding dynamic 
Asset Management (AM) applications even when there is limited available as-built 
information. The approach utilizes the IfcSharedFacilitiesElements schema for process-
ing both existing and newly created Industry Foundation Classes (IFC) objects, allowing 
real-time integration of data. The methodology is tested using data from the West Cam-
bridge DT Research Facility, demonstrating its potential for supporting asset anomaly 
detection. By integrating BIM and IoT tools, this solution enhances the automation of 
digital AM processes within the context of building development. The method proves 
effective for existing buildings, addressing issues related to data scarcity. It enables easier 
access to data across domains, supporting the creation of AM applications for intelligent 
buildings. This approach facilitates both the integration of static AM data and real-time 
IoT data, reducing uncertainty and automating operations. The study showcases the 
openBIM solution’s potential in built Asset Management and suggests testing its robust-
ness through additional application case studies in future research.
•	 Reported energy efficiency improvements: None
•	 Reported benefits: A standard approach to implement DTs for buildings with a 
scarcity of data. Effective utilization of BIM data and sensor data in a unified IFC-
based system.
•	 Reported quantitative improvements from DT: None
•	 Technology highlights: WSN, BIM, BMS, language-agnostic UML specification.
 Peng et al. (2020) discussed an exemplary Digital Twin (DT) project conducted at 
East Hospital for over a year. The project aimed to achieve improved performance and 
energy efficiency through continuous lifecycle integration. The results showed a 10% 
increase in management satisfaction, approximately 1% energy savings annually, and 
over 10% avoidance of facility faults and repairs through DT diagnosis. While the case 
was specific to Shanghai, China, the solution has wider applicability to modern hospi-
tals globally due to shared management needs and electrical systems.
The paper emphasizes three key points: Continuous Life-cycle Integration, Real-
time Visual Management and Intelligent DT Diagnosis. However, the implementa-
tion revealed certain shortcomings and challenges: Professional System Integration, 
Financial Risks and Data Security and Ownership.
•	 Reported energy efficiency improvements: An automated pattern recognition algo-
rithm finds what is the normal usage of electric equipment and notifies workers 
when abnormal behaviour is found, asking them to intervene to reduce energy waste.
•	 Reported benefits: A unified visualization and control digital system for the build-
ing increased the operation and management satisfaction. Fault prediction and 
validation allowed for less maintenance costs.
•	 Reported quantitative improvements from DT: Around 1% increase in energy effi-
ciency.


---

Page 15

---

Page 15 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
	
•	 Technology highlights: BacNet, OPC and HTTP API requests. Apache kafka and pri-
vate cloud storage.
 Wang et al. (2022) introduced the concept of using digital twin technology in build-
ing operation and maintenance processes, along with the integration of machine learn-
ing algorithms for intelligent prediction. The process involves establishing a digital twin 
model for building operation and maintenance, integrating and visually displaying rel-
evant data. The machine learning algorithm is then applied for data-driven predictions 
and diagnoses.
The paper highlights 3 main key points: A framework is proposed for digital twin 
tech in building operation and maintenance combined with machine learning for intel-
ligent predictions and diagnoses. The digital twin tech aids in visualizing and retrieving 
diverse operational data. 3D model-based data retrieval is more intuitive than traditional 
methods. The potential for achieving intelligent building operation and maintenance is 
emphasized.
•	 Reported energy efficiency improvements: None
•	 Reported benefits: A framework and DT development process that allows for fast 
integration with artificial neural networks (ANN).
•	 Reported quantitative improvements from DT: None
•	 Technology highlights: BIM, ANN.
 Zaballos et al. (2020) suggested a Smart Campus (SC) concept involving the integra-
tion of Building Information Modeling (BIM) and IoT-based wireless sensor networks 
(WSN) for environmental monitoring and emotion detection. This aims to gauge occu-
pants’ comfort levels, which significantly impact productivity. The research is conducted 
within the software environment of Autodesk Revit (2023b) 2020, combining BIM and 
IoT to provide real-time access to information and automation.
SC supports intelligent decision-making processes, energy efficiency, and comfort. The 
model encompasses three intelligence domains: Green campus (energy consumption), 
Healthy campus (comfort monitoring), and real-time facility management. The ongo-
ing research project aims to develop a multi-disciplinary Smart Campus with distinctive 
characteristics to enhance sustainability beyond traditional campuses.
•	 Reported energy efficiency improvements: None
•	 Reported benefits: Enhanced comfort enabled through real-time environment moni-
toring and emotion-detection.
•	 Reported quantitative improvements from DT: None
•	 Technology highlights: BIM, WSN, bluetooth, arduino, ethernet, WiFi.
 Zhao et al. (2022) employed illustrative case studies to explore how DTs are used in 
FM, leading to improved building performance and enhanced efficiency of Mechanical, 
Electrical, and Plumbing (MEP) systems. The study highlights real-time data collection, 
predictive maintenance, and cost reduction as key benefits of DT implementation. A 
conceptual framework is developed to address challenges in integrating Building Infor-
mation Modeling (BIM) and FM models, providing guidance for implementing DT with 


---

Page 16

---

Page 16 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
considerations for data acquisition, processing, modeling, and application. The use of 
Machine Learning (ML) and Artificial Intelligence (AI) in DT is proposed to enhance 
FM systems’ intelligence and communication. The research’s findings contribute to 
practitioners’ understanding of DT’s impact on FM and suggest a content-dependent 
approach to knowledge development. Overall, the study underscores DT’s potential to 
transform FM practices in the digital construction era, proposing solutions to imple-
mentation challenges.
•	 Reported energy efficiency improvements: None
•	 Reported benefits: A standard abstraction of a digital twin for buildings.
•	 Reported quantitative improvements from DT: None
•	 Technology highlights: BIM
 Agostinelli et al. (2022) focused on a policy for digitizing port infrastructure to enhance 
maintenance processes and energy efficiency, ultimately transitioning port areas into 
Zero Energy Districts (ZED). The Lazio Region initiated this process in 2020, with the 
Anzio port serving as a representative pilot project due to its relevance in the Medi-
terranean context. The study’s objective was to establish energy-saving strategies and 
incorporate Renewable Energy Systems (RESs) to promote sustainable mobility. The 
paper elaborates on these strategies, conducts an energy analysis starting from the cur-
rent state, and showcases the potential for the infrastructure to achieve energy self-suffi-
ciency. The concept of utilizing a Digital Twin (DT) for the area’s analysis is highlighted. 
Moreover, the text discusses the synergistic benefits of integrating Building Information 
Modeling (BIM) and Geographic Information System (GIS) techniques to maximize the 
impact of energy efficiency measures.
•	 Reported energy efficiency improvements: A detailed energy model provided insights 
into the major consumers of energy in the port, replacing the lighting to LED tech-
nology reduced drastically the total energy consumption.
•	 Reported benefits: Reduced energy consumption, a decision-making tool in the form 
of a digital model with aggregated BIM and GIS data, providing insights into solar 
and wind potential.
•	 Reported quantitative improvements from DT: Around 15% of total energy con-
sumption reduction after the structural changes.
•	 Technology highlights: BIM, GIS, Autodesk Revit.
Predictive maintenance
Hosamo et al. (2022) discussed the application of Digital Twin technology in facili-
tating predictive maintenance and dynamic maintenance strategies in the Facility 
Management and Maintenance (FMM) process. The proposed framework involves 
integrating data from Building Information Models (BIM), Internet of Things (IoT) 
sensor networks, and Facility Management (FM) systems. The framework includes 
three modules for predictive maintenance: operational fault detection, condition 


---

Page 17

---

Page 17 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
	
prediction, and maintenance planning. Various machine learning techniques like 
Artificial Neural Networks (ANN), Support Vector Machines (SVM), and decision 
trees are used to predict the state of components and enhance the lifetime of Air 
Handling Unit (AHU) components.
The research proves that automated fault detection in Air Handling Units (AHUs) is 
highly effective, performing well with different AHU types and problems. The paper 
covers data sources, semantic data definitions, and techniques for identifying and fix-
ing faults.
Nevertheless, the paper recognizes certain drawbacks. The accuracy of predic-
tions is influenced by developers’ algorithm choices, tied to their expertise. The study 
emphasizes the importance of exploring alternative prediction methods. Future 
directions include adopting an ontology-based solution for consistent integration of 
data from diverse sensors and systems. The paper suggests using incremental learning 
techniques to regularly enhance the prediction models with new input data.
•	 Reported energy efficiency improvements: None.
•	 Reported benefits: Cost reduction through predictive maintenance of ventilation 
systems.
•	 Reported quantitative improvements from DT: None.
•	 Technology highlights: IFC, Ontologies, Web API, Autodesk Revit. RS 485 sen-
sors, TCP/IP enabled.
 Ni et al. (2021) introduced a cloud-based framework for digitizing historic buildings 
through digital twins and AI development. The framework has been applied to three 
chosen historic buildings, demonstrating successful collection, transmission, and 
storage of data in the cloud. This allows the creation of digital twins updated with 
real-time sensor data. Future plans involve installing sensor boxes in these buildings 
to extract valuable insights from the collected data. This will enable the creation of AI 
models for tasks like anomaly detection, occupancy prediction, and energy-efficient 
control, contributing to building preservation and energy optimization.
In another study, Ni et al. (2022) extended their work to enhance (Ni et al. 2021). 
This study aimed to enhance the preservation of historic buildings by utilizing digi-
talisation methods to create digital twins. By combining Internet of Things (IoT) 
technology and ontology, the study proposed a solution to consistently represent 
data from historic buildings, showcase their current operational state, and enable fur-
ther data analysis. The study developed an IoT system using hardware, open-source 
software libraries, RealEstateCore ontology, and Microsoft Azure to implement this 
solution. A practical case study conducted in a historic building demonstrated that 
a digital twin reflecting the building’s real-time status can be generated using sensor 
data. Insights from the digital twin were used to improve the indoor environment of 
the building for both heritage preservation and human comfort. Future work could 
involve using monitored indoor conditions to estimate occupancy levels and incor-
porating additional data, such as energy consumption, to model energy behavior and 
reduce operational costs of historic buildings.


---

Page 18

---

Page 18 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
•	 Reported energy efficiency improvements: None
•	 Reported benefits: Real-time monitoring, an unified knowledge-base of the build-
ing, possibility to do data analytics.
•	 Reported quantitative improvements from DT: None, however presented an esti-
mated cost for cloud services of 3000 Swedish crowns for 100 data entry points.
•	 Technology highlights: Arduino, cellular internet, Azure cloud, ontologies.
Simulation of alternative scenarios
Agostinelli et al. (2021) discussed the implementation of Digital Twin (DT) method-
ology in buildings, enabling them to enhance their knowledge using sensor data and 
integrate with AI systems for self-learning and prediction. The research’s main goal is 
to use machine learning to manage self-production and supply systems in an energy 
smart grid, addressing thermal and electrical loads. Real-time monitoring through 
DT improves building energy performance, identifying user behaviors and refining 
energy strategies. Load forecasting allows to simulate and predict daily thermal loads 
using historical sensor data and smart metering, while optimizing energy balance and 
production systems. The DT also optimizes indoor comfort by adjusting system oper-
ations based on environmental data. Extending the research to urban contexts, the 
integration of BIM-GIS systems aids in connecting urban energy cells to the national 
grid, focusing on electric mobility and storage.
•	 Reported energy efficiency improvements: Using solar and geothermal power 
sources, orchestrated by a digital twin platform, the energy demand from the grid 
was significantly reduced.
•	 Reported benefits: Cost reduction from energy optimizations.
•	 Reported quantitative improvements from DT: Around 38% cost reduction from 
energy consumption.
•	 Technology highlights: Bluetooth, WiFi, BIM, GIS, Autodesk Revit
 Kaewunruen and Lian (2019) introduced a 6D Building Information Model (BIM) for 
a railway turnout system. This BIM system covers all stages from planning to dem-
olition, providing comprehensive project information. A life-cycle assessment was 
also conducted using shared information. The BIM acts as a data-sharing platform, 
improving planning efficiency, collaboration, and sustainability. It enhances mainte-
nance visualization, stakeholder collaboration, and cost estimation. The digital twin 
aspect aids stakeholders in policy and sustainability solutions. The study demon-
strates BIM’s role in promoting cleaner production and maintenance policies. With 
evolving technology like ’Internet plus’, BIM is expected to integrate with GIS for 
various applications in urban planning, triggering a digital revolution in engineering 
construction towards innovation. It is worth nothing that this is the only author in 
this review who does not differentiate between BIM and Digital Twin concepts.


---

Page 19

---

Page 19 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
	
•	 Reported energy efficiency improvements: None
•	 Reported benefits: BIM implementation can reduce capital cost and carbon emis-
sions by allowing prioritisation of maintenance and operational works.
•	 Reported quantitative improvements from DT: None.
•	 Technology highlights: BIM, GIS, no data collection in site.
Table  3 presents a non-exhaustive summary of the reported benefits of the digital 
twin use cases, with special attention to the reported achievements related to energy 
efficiency. As it can be appreciated, only 5 out of 20 analyzed use-cases reported 
any sort of quantitative benefits. The majority of the studies restrain from reporting 
the total cost reduction or improvement of energy efficiency resulting from the DT 
implementation.
Table 3  Summary of the reported benefits of DT, with special emphasis in energy efficiency
Study
Energy efficiency 
benefits
Other benefits
Reported quantitative 
benefits
 Khajavi et al. (2019)
Finer temperature and 
lighting control
Lower costs
None
 Li et al. (2022)
Improve chiller’s COP
Lower costs
Lower energy consump‑
tion
40% COP increase
 Bjørnskov et al. (2022)
Better baseline energy 
models
More realistic monitoring 
and detection
None
 Lu et al. (2020d)
None
Detection of improper 
operation
None
 Lu et al. (2020c)
None
Detection of improper 
operation
None
 Bjørnskov and Jradi (2023)
None
Semantic modeling
None
 Chiara Tagliabue et al. 
(2021)
None
Sustainability assessment
None
 Clausen et al. (2021)
Planned energy consump‑
tion
Potential increase in 
energy efficiency
None
 Jradi and Bjørnskov (2023)
None
More accurate, easier to 
maintain models
None
 Lee et al. (2016)
Finer temperature and 
lighting control
Lower costs
Constant monitoring
17% Energy consumption
reduction
 Moretti et al. (2020)
None
Unified IFC-based system
None
 Peng et al. (2020)
Optimization recommen‑
dations
Unified visualization and 
control
1% Energy consumption
reduction
 Wang et al. (2022)
None
DT framework for using 
ANNs
None
 Zaballos et al. (2020)
None
Enhanced comfort
None
 Zhao et al. (2022)
None
Standard conceptual 
model for DTs
None
 Agostinelli et al. (2022)
Energy model to support 
decision-making
Integrate BIM and GIS for 
better decisions
15% energy reduction
after retrofitting
 Hosamo et al. (2022)
None
Lower costs
Predictive maintenance
None
 Ni et al. (2021)
None
Real-time monitoring
None
 Agostinelli et al. (2021)
Renewable sources 
orchestration through DT
Lower costs
38% cost reduction
from retrofitting+DT
 Kaewunruen and Lian 
(2019)
None
Lower costs
None


---

Page 20

---

Page 20 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
Commercial tools for digital twins for buildings
A thorough review of existing literature has been conducted to highlight the substan-
tial potential of digital twin technology across a range of applications in building opera-
tion. In addition to the theoretical and experimental investigations reviewed above, this 
section will present the commercial tools presented and developed in recent years to 
deliver various services of digital twins in buildings. These tools come predominantly 
from firms specializing in energy, engineering, and construction. A detailed review of 
these recent instruments is presented:
•	 Arup has created ’Neuron’ (Arup 2023a), an intelligent digital twin system for build-
ings, aimed at aiding property owners in attaining notable energy conservation via 
sophisticated machine learning and anticipatory upkeep. This system employs 5 G 
and the Internet of Things (IoT) to collect up-to-the-minute sensory data from vari-
ous equipment and systems. Furthermore, it utilizes Building Information Modelling 
(BIM) to exhibit these intricate datasets via a cloud-centric, unified administrative 
interface. Additionally, Arup harnesses artificial intelligence and machine learning to 
assess, enhance, and mechanize operations.
•	 Granlund introduced a platform showcasing the Granlund Manager’s Digital Twin 
(Grandlund 2023), which conveniently displays data in real-time, superimposed on 
the building’s three-dimensional layout. This enables the tracking of conditions on a 
building-wide, floor-specific, and individual unit level. The Digital Twin amalgamates 
information from Building Information Models (BIMs) utilized during the planning 
stage, along with data from Internet of Things (IoT) and automation systems, as well 
as insights from property occupants, among other origins.
•	 Autodesk has introduced ’Autodesk Tandem’ (Autodesk 2023a), a cloud-based digital 
twin platform designed for building and facility applications. This technology allows 
projects to remain digital from inception to completion by utilizing Building Infor-
mation Modeling (BIM) data. With Autodesk Tandem, construction and engineering 
companies can create and deliver a digital twin to building owners, providing them 
with accessible, contextual, and insightful data for seamless operations. The Tandem 
platform empowers architectural, engineering, and construction (AEC) firms to uti-
lize BIM data throughout the project lifecycle, facilitating the creation and delivery of 
a digital twin. Moreover, it assists owners in integrating operational systems with the 
digital twin to convert fragmented data into actionable business intelligence.
•	 Siemens presented the ’Building Twin’ (Siemens 2023), a digital twin solution that 
offers real-time insights into a building’s performance, allowing instant modifications 
to enhance efficiency and furnish data for refining the design of upcoming build-
ings. The suggested digital twin contributes to more economical, uncomplicated, and 
environmentally conscious smart buildings. These advantages are realized through 
improved comprehension of building performance, swift detection and resolution of 
issues in real-time, and enhanced utilization of available space.
•	 Bosch has recently introduced its “Connecting Building Services” (Bosch 2023) pack-
age, employing Azure Digital Twins to develop solutions that are sensitive to the 
building’s context. This involves crafting digital depictions of assets, surroundings, 
and business systems within buildings and facilities. This capability empowers clients 


---

Page 21

---

Page 21 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
	
to utilize predictions and anticipatory insights, leading to quicker, more knowledge-
able choices in enhancing building efficiency and minimizing carbon emissions.
•	 Catenda has developed a digital platform solution, named ’Bimsync Arena’ (Catenda 
2023b) as part of their newly developed Catenda Hub, designed to enhance the crea-
tion of building digital twins. This platform facilitates improved design collabora-
tion, error reduction, time savings, and elevated deliverable quality, all powered by an 
open BIM collaboration environment. Bimsync (Catenda 2023a) seamlessly connects 
information and data to the virtual asset through an intuitive interface, ultimately 
culminating in the creation of a comprehensive building digital twin.
Classification based on the data integration level
Table 4 presents a consolidated analysis of the case studies examined. This analysis spe-
cifically focuses on the integration of data within the digital twin implementations, as 
per the classification framework proposed by Kritzinger et al. (2018), as shown in Fig. 6. 
Notably, several articles describe a comprehensive digital twin framework or develop-
ment process that includes extensive data integration. However, in order to analyse the 
experience obtained from each real-life system, only the implemented use cases from 
each study are considered.
Table 4  Data integration level for the analyzed use cases
Study
Domain
Level of integration
BIM
ML
Models’ type
 Khajavi et al. (2019)
Component monitoring
Digital shadow
✓
Sensor data only
 Li et al. (2022)
Component monitoring
Digital twin
✓
Gray-box
 Bjørnskov et al. (2022)
Fault detection and com‑
missioning
Digital model
White-box
 Lu et al. (2020d)
Fault detection and com‑
missioning
Digital shadow
✓
Gray-box
 Lu et al. (2020c)
Fault detection and com‑
missioning
Digital shadow
✓
✓
Gray-box
 Bjørnskov and Jradi (2023)
Operational optimization
Digital shadow
✓
Gray-box
 Chiara Tagliabue et al. 
(2021)
Operational optimization
Digital twin
✓
✓
Gray-box
 Clausen et al. (2021)
Operational optimization
Digital twin
Gray-box
 Jradi and Bjørnskov (2023)
Operational optimization
Digital shadow
✓
Gray-box
 Lee et al. (2016)
Operational optimization
Digital shadow
✓
Sensor data only
 Moretti et al. (2020)
Operational optimization
Digital shadow
✓
Sensor data only
 Peng et al. (2020)
Operational optimization
Digital shadow
✓
✓
Gray-box
 Wang et al. (2022)
Operational optimization
Digital shadow
✓
✓
Gray-box
 Zaballos et al. (2020)
Operational optimization
Digital shadow
✓
Gray-box
 Zhao et al. (2022)
Operational optimization
Digital model
✓
Sensor data only
 Agostinelli et al. (2022)
Operational optimization
Digital model
✓
White-box
 Hosamo et al. (2022)
Predictive maintenance
Digital shadow
✓
✓
Gray-box
 Ni et al. (2022)
Predictive maintenance
Digital shadow
✓
Gray-box
 Ni et al. (2021)
Predictive maintenance
Digital shadow
Sensor data only
 Agostinelli et al. (2021)
Scenario simulation
Digital shadow
✓
✓
Gray-box
 Kaewunruen and Lian 
(2019)
Scenario simulation
Digital model
✓
White-box


---

Page 22

---

Page 22 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
In the ‘Models Type’ column, an endeavor is made to classify the mathematical and 
physical models employed for simulation, estimation, and forecasting within each 
case study. In instances where no specific models for these purposes are identified, 
and the digital twin services rely solely on sensor inputs, such scenarios are catego-
rized as ‘Sensor Data Only’. The classification further delineates whether the models 
used are exclusively physical (termed ‘White-Box’), solely statistical (‘Black-Box’), or a 
hybrid of physical and statistical approaches (‘Gray-Box’). For instance, a system lev-
eraging sensor data to calibrate parameters within a physics-based model would be 
categorized as a ‘Gray-Box’ model.
Following the guidelines described in “Classification based on the data integration 
level” section, Table 4 compiles the classification of the use cases analyzed. As appre-
ciated in the table, the vast majority of digital twin for building solutions use BIM as 
part of the creation process of the DT. There is only one study where the BIM model 
is created as part of the DT creation process (Peng et al. 2020) while all the other BIM 
uses attempt to utilize a previously existing model.
This analysis reveals a trend in the modeling approaches for simulation and fore-
casting in digital twin services. Selected studies (Khajavi et al. 2019; Lee et al. 2016; 
Moretti et al. 2020; Zhao et al. 2022) integrate only sensor data with preprocessing 
techniques to inform building management, without mathematical processing of this 
data. Conversely, the predominant modeling solution for estimating key digital twin 
metrics relies on Gray-Box methods. These methods synergize physical laws and sta-
tistical techniques, offering a range of digital twin services based in forecasting and 
simulation.
In the case of the enterprise solutions, a classification of each one of the presented 
solutions is depicted in Table 5:
Fig. 6  Levels of data integration for digital twins (Kritzinger et al. 2018)
Table 5  Data integration level for the analyzed commercial tools
Tool
Level of integration
BIM
ML
 Arup (2023a) Arup Neuron
Digital shadow
✓
✓
 Grandlund (2023) Grandlund Manager’s
Digital Twin
Digital shadow
✓
 Autodesk (2023a) Autodesk Tandem
Digital shadow
✓
 Siemens (2023) Siemens Building Twin
Digital shadow
✓
 Bosch (2023) Bosch Connecting Building Services
Digital shadow
 Catenda (2023a) Catenda Hub
Digital shadow
✓


---

Page 23

---

Page 23 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
	
Given that enterprise solutions typically provide a centralized source of truth with real 
time data ingestion from the building they are classified as digital shadows following the 
previously mentioned classification, this is further discussed in “Commercial tools vs 
custom implementations” section.
Discussion
Consensus on digital twin definition
The analysis evidences the lack of consensus on the definition of Digital Twins. For 
instance, some studies using an isolated digital simulation refer to their solution as digi-
tal twin. A more granular segmentation can be useful to understand the different levels 
of maturity of the digital twin implementations. Utilizing the levels of data integration of 
Kritzinger et al. (2018) for digital twins in manufacturing, as shown in Fig. 6, enables a 
more detailed description of the level of data integration among the analyzed use cases, 
as is evident in Table 4. The number of case studies with complete feedback loops, sen-
sor data and some sort of automated action occurring in the building is relatively small, 
all the documents use the term digital twin to refer to their implementation.
In addition, the term “digital twin” is interpreted in various ways, particularly in its 
simulation and predictive functions. Many academic studies define digital twins as mod-
els of physical assets with the ability to simulate scenarios, a considerable number of 
the reviewed academic studies agree on the simulation function of digital twins. On the 
contrary, commercial tools commonly define a digital twin as a centralized platform for 
visualizing sensor data and operational information. These commercial definitions do 
not always include simulation abilities or models based on physical laws. This distinction 
highlights the different emphasis placed on digital twins by academic research versus 
commercial applications.
Digital twins’ relation to energy information systems (EIS)
Building Energy Information Systems (EIS) are specialized platforms designed to moni-
tor, analyze, and control the energy use of buildings (Granderson et  al. 2011). They 
collect data from various sources, such as HVAC systems, lighting, and other energy-
consuming devices, to provide insights into the building’s energy performance. EIS tools 
help in identifying inefficiencies, optimizing energy use, and reducing operational costs. 
They can also support decision-making processes for energy conservation measures.
On the other hand, a digital twin for buildings is a virtual model of a physical build-
ing. It integrates data from various sources, including sensors, systems, and external 
data feeds, to create a real-time, dynamic representation of the building. This model can 
simulate, predict, and analyze the building’s performance under various conditions. The 
points below address the relationship and integration potential between EIS and digital 
twins:
Enhanced Data Integration and Analysis: Digital twins can enhance the capabilities 
of EIS by providing a more detailed and comprehensive model of the building. Digi-
tal twins can simulate the impact of different energy conservation measures, helping 
stakeholders make more informed decisions.


---

Page 24

---

Page 24 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
Real-time Performance Optimization: By integrating EIS with digital twins, buildings 
can achieve real-time energy performance optimization. The digital twin can sim-
ulate various scenarios in real-time, allowing the EIS to adjust systems to improve 
energy efficiency dynamically.
Sustainability and Compliance: Digital twins, through their detailed simulation capa-
bilities, can help buildings comply with energy regulations and standards by accu-
rately predicting and demonstrating energy performance. When combined with EIS, 
buildings can not only monitor compliance but also find innovative ways to improve 
sustainability metrics.
In conclusion, digital twins for buildings and Building Energy Information Systems 
(EIS) are intricately linked technologies. When combined, they can greatly improve 
how we manage, operate, and optimize energy use within buildings. While digital twins 
offer a broader perspective that might not always concentrate on energy systems, their 
integration with the data-driven and energy-focused approach of EIS holds significant 
promise. This combination brings together the detailed modeling and predictive capa-
bilities of digital twins with the monitoring and operational strengths of EIS.
Commercial tools vs custom implementations
Commercial tools’ strength relies mainly in the ease of use, solution’s like Arup’s “Neu-
ron” (Arup 2023a), Siemens’ “Building Twin” (Siemens 2023) and Autodesk Tandem 
(Autodesk 2023a) offer a comprehensive suite of visualization tools and provide the 
users with the possibility of implementing dashboards. They also integrate with the 
most popular digital systems and protocols, such as BMS systems, BACNet and Modbus 
protocols.
Table 6 presents a different angle for the analysis of the commercial tools, providing a 
direct comparison of the potential services offered by these tools and the custom-made 
studies analysed. The services provided by commercial tools are usually an extension 
of BIM technology to incorporate sensor measurements (Arup 2023a; Siemens 2023; 
Autodesk 2023a; Catenda 2023b). This system architecture allows typically for monitor-
ing, anomaly assessment and enhanced operation, based on the same monitoring capa-
bilities and manual action-taking. However, they lack any sort of physical model which 
simulates the building systems and therefore any forecasting or predictive maintenance 
capability is generally not available.
Table 6  Supported topics from each commercial tool, based on publicly available descriptions of 
the tools
Theme
Tools
1. Component monitoring
Neuron, Granlund, Autodesk Tandem,
Building Twin, Bosch DT service, Bimsync Arena
2. Anomaly detection
Neuron, Autodesk Tandem,
Building Twin, Bosch DT service, Bimsync Arena
3. Operational Optimization
Neuron, Granlund, Autodesk Tandem,
Bosch DT service
4. Predictive maintenance
(None)
5. Simulation of alternative scenarios
(None)


---

Page 25

---

Page 25 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
	
It is worth noting that the commercial solutions focus on providing data services 
and dashboards for building operators which then can take actions based on the uni-
fied source of information. If an automatic controlling action is desired, custom integra-
tion or expansions of the solution would be necessary. Enabling a full duplex digital twin 
solution would require extra steps tailor made for each specific scenario.
Enterprise solutions still enable many of the benefits of having digital twins in the built 
environment, such as real-time monitoring and diagnosis. Decision-making support 
and the possibility of forecasting and enhancing the energy efficiency throughout the 
building.
In contrast, custom digital twin solutions are tailored to address the specific opera-
tional needs of each building. These systems offer detailed insights and possess the flex-
ibility required for the implementation and iterative development of the digital twin, 
facilitating its continuous evolution. Over time, these solutions can be fine-tuned to 
emphasize operational benefits that yield the most significant impact, and can integrate 
advanced features like automation and control loops for building systems. However, the 
development and maintenance of custom solutions necessitates a dedicated team of 
engineers and specialists, often resulting in higher costs compared to standard off-the-
shelf products. Additionally, while custom digital twins are designed for expert users, 
this focus can limit their accessibility and usability for external stakeholders who may 
not have in-depth knowledge of the system.
Digital twins for energy efficiency
Table 3 suggests that digital twins can enhance energy efficiency during the operation 
and maintenance phases of buildings. However, there is a lack of direct studies quantify-
ing this impact, with only a few reported instances of measurable improvements. Nota-
ble among these are increases of up to 40% in the Coefficient of Performance (COP) for 
chillers, energy consumption reductions of 17%, and 15% reductions post-retrofitting. 
Retrofitting emerges as a key factor for improving energy efficiency, which may neces-
sitate additional investment in the building’s physical systems overhaul.
Additional potential advantages include:
•	 Cost Reduction: While several studies point to cost savings as a major benefit of digi-
tal twins, quantitative evidence backing these claims is sporadic.
•	 Operational Improvements: Digital twins offer more than just direct energy savings. 
They support enhanced operations through ongoing monitoring, identifying incor-
rect operations, and real-time surveillance, all of which may indirectly contribute to 
energy conservation.
Digital twins can contribute to energy savings in buildings through a variety of mecha-
nisms. By creating a virtual replica of a building, digital twins enable the fine-tuning of 
temperature and lighting according to the patterns and behaviors of occupants, ensur-
ing that energy is used optimally and only when necessary. They also empower build-
ing operators with data-driven recommendations on how to best manage and adjust 
the building’s energy systems for maximum efficiency. Additionally, digital twins facili-
tate the simulation of various retrofitting scenarios, allowing stakeholders to assess the 


---

Page 26

---

Page 26 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
potential impacts and benefits before physical changes are made. This predictive capa-
bility not only aids in identifying the most effective retrofitting strategies but also mini-
mizes the risks and costs associated with the trial-and-error of physical modifications.
In summary, digital twins hold potential for increasing energy efficiency and cutting 
costs in the building industry. Yet, the extent of these benefits is not consistently docu-
mented and varies greatly. The capacity to customize building operations and the provi-
sion of actionable insights demonstrate the strategic value of digital twins in optimizing 
energy use and enhancing overall building performance.
Challenges
A critical aspect shared by both custom and off-the-shelf digital twin solutions is their 
dependency on a robust data acquisition system. This system typically comprises a com-
munications network and an array of sensors strategically distributed throughout the 
building. The efficacy of these solutions is contingent on the availability and quality of 
data gathered from these systems. A notable challenge arises when these systems need 
to be integrated with a Building Management System (BMS) present in the building. 
This integration often presents complexities that demand specialized engineering exper-
tise to address effectively.
Additionally, most current digital twin solutions primarily depend on the use of Build-
ing Information Modeling (BIM), which, are not widely available for the majority of 
existing building stock (Volk et al. 2013). This gap signifies that digital twin solutions 
capable of integrating BIM data, yet not solely dependent on these models, are of signifi-
cant interest. Such solutions would offer greater applicability and flexibility, especially in 
scenarios where comprehensive BIM data is unavailable or incomplete.
There is an emphasized need to compare different digital twin methods and define 
clear criteria for them. A consensus on the definition and scope of digital twins in con-
struction and energy efficiency is missing. Therefore, further research is required to 
specify the optimal characteristics and proper boundaries of digital twins for building 
applications.
Proposed digital twin for building operation framework
Unlike in manufacturing, where digital twins often include a 3D model of the physical 
asset, digital twins for buildings may not always need this type of visualization. The setup 
of these digital twins can differ greatly, customized to meet the particular goals of the 
services they support. This means the intended use of the digital twin dictates its design, 
development, and implementation. For example, a digital twin designed for ongoing 
commissioning services would have a different configuration than one used for opti-
mizing performance or analyzing retrofit options. Another example is the digital twin 
solution highlighted by (Lu et al. 2020c) which offers an interactive 3D visualization that 
can display indoor comfort metrics on demand. This functionality necessitates the use 
of 3D engines, robust systems for data transmission and integration, and sophisticated 
visualization dashboards. In contrast, Hosamo et al. (2022) describe a digital twin devel-
oped to facilitate predictive maintenance for Air Handling Units. This system merges 
building information with sensor data to run simulations and leverages machine learn-
ing to suggest maintenance schedules, indicating that digital twin solutions for buildings 


---

Page 27

---

Page 27 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
	
can significantly differ. Despite this variety, the fundamental architecture of digital twin 
models remains consistent, incorporating three essential layers common to all examined 
solutions. The abstraction of this layered model is depicted in Fig. 7.
These service-oriented digital twin solutions integrate one or many components in 
each layer. With an up-to-down design phase and an down to up implementation. The 
shape of the solution will be defined by the service is expected to provide. On this basis, 
the digital twins can be divided into three layers, Data, Model and Service layers.
•	 The Data Layer presents significant technical complexities within the digital twin 
framework. It involves the collection, integration, and transmission of data across 
various subsystems. The primary challenges at this level include ensuring high-qual-
ity data-particularly from Building Information Modeling (BIM) and sensors-and the 
integration of existing systems such as Building Management Systems (BMS), Geo-
graphic Information Systems (GIS), and online weather services.
•	 The Model Layer leverages the collected data together with user-defined models to 
produce specific outcomes. These may include simulation results, predictive fore-
casts, or optimization strategies derived from reasoning systems. Enhancing this lay-
er’s effectiveness often involves incorporating domain-specific knowledge and expert 
input to guide the modeling process.
Fig. 7  Proposed Digital twin layer model with its different components as a basis for building operation and 
management support


---

Page 28

---

Page 28 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
•	 The service layer, deals with the implementation of the interface that will provide 
the end user with all the relevant information that will allow them to benefit from 
the digital twin. This layer can manifest as a user interface for data interaction or as 
part of an automated feedback loop where modeling outcomes directly influence the 
building’s operation through actuators.
In line with the proposed digital model, the University of Southern Denmark together 
with public and private sector partners have launched the DanRETWin (Jradi et  al. 
2023) project, which aims to provide digital twin-based solutions for supporting and 
enhancing the retrofitting process of the danish building stock. Within the context of 
this project some of the mentioned challenges and future research efforts are going to be 
addressed. Integration and generalization of models in relation with old buildings, where 
digital information is very low or non-existing is one of the main research objectives.
Conclusions
This study evaluated the application of digital twins during the operational phase of 
building management. Integrating real-time data with digital models of buildings and 
their components enables services that include anomaly detection, continuous system 
monitoring, and energy use optimization. These services contribute to cost savings and 
improved building performance.
Digital twins have the potential to enhance energy efficiency and reduce operational 
costs in the building industry. They enable customization of building operations and 
provide operators with actionable insights, highlighting the strategic role of digital twins 
in optimizing energy consumption and bolstering overall building efficacy. However, the 
extent of these advantages is not consistently documented and exhibits considerable var-
iability. Moreover, there is a notable lack of discussion on the costs involved in develop-
ing and maintaining digital twins relative to their quantifiable advantages.
The digital twin use cases reviewed predominantly rely on Building Information Mod-
eling (BIM) for establishing the digital representation. Some studies detail the creation 
of a BIM model, which is subsequently integrated into a digital twin framework during 
the development phase of the digital twin.
A prominent obstacle in the rapid and effective development of building digital twins 
is the generally substandard quality of existing models and data. This challenge is exacer-
bated by the substantial effort required to synthesize various building systems and data 
processing technologies.
Digital twins in the construction sector are more inclined to offer service-oriented 
applications rather than exhaustive simulations of entire buildings and their subsystems. 
The specific purpose of a digital twin influences its design, development, and deploy-
ment. Consequently, there is no standardized architecture or set list of services for digi-
tal twins in building operations, leading to significant variations in the features of each 
digital twin based on its initial design and intended function.
Future work
Future research should aim to devise methods that do not exclusively depend on BIM 
data, and when BIM is utilized, to automate the extraction of model data. Further 


---

Page 29

---

Page 29 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
	
exploration into artificial intelligence and machine learning is warranted to refine 
digital twin applications, address integration complexities, and reduce the cost and 
time associated with their deployment. Concurrently, new studies on digital twins 
for buildings should pay special attention to the measurable benefits obtained from 
the digital twin, providing a reliable assessment of their value. This would involve a 
detailed analysis of the costs and savings over the lifecycle of the digital twin, ensur-
ing that the economic and environmental implications are clearly understood and 
effectively communicated. These research areas are crucial for overcoming existing 
barriers and enhancing the practical deployment and effectiveness of digital twins in 
the industry.
Abbreviations
O&M	
Operation and Maintenance
IoT	
Internet of Things
BIM	
Building Information Modeling
EU	
European Union
DT	
Digital Twin
IEA	
International Energy Agency
AI	
Artificial intelligence
AEC	
Architecture, Engineering, Construction
ML	
Machine Learning
BDT	
Building digital twin
HVAC	
Heating, Ventilation and Air conditioning
LEED	
Leadership in energy and environmental design
MPC	
Model predictive control
SDT	
Sustainable digital twin
VAV	
Variable Air Volume
EOC	
Energy operation center
IFC	
Industry foundation classes
AM	
Asset management
SC	
Smart campus
WSN	
Wireless sensor network
MEP	
Mechanical, electrical and plumbing
ZED	
Zero energy districts
RES	
Renewable energy system
GIS	
Geographical information system
FMM	
Facility management and maintenance
ANN	
Artificial neural networks
SVM	
Support vector machines
AHU	
Air handling unit
BMS	
Building management system
Acknowledgements
Not applicable.
Author contributions
ASCC contributed with the research methodology, analysis of previous studies and proposed DT framework, discussion 
and conclusions. MJ contributed with the general layout of the document, analysis of commercial tools, discussion and 
conclusions.
Funding
Open access funding provided by University of Southern Denmark This research was carried out under the ‘DanRETwin: 
A Digital Twin solution for optimal energy retrofit decision-making and decarbonization of the Danish building stock’ pro‑
ject, funded by the Danish Energy Agency (Energistyrelsen) under the Energy Technology Development and Demonstra‑
tion Program (EUDP), ID number: 640222-496754.
Availability of data and materials
All data generated or analysed during this study are included in this published article and its supplementary references 
list.
Declarations
Ethics approval and consent to participate
Not applicable.


---

Page 30

---

Page 30 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
Competing interests
The authors declare that they have no competing interests.
Received: 28 December 2023   Accepted: 12 February 2024
References
Agostinelli S, Cumo F, Guidi G, Tomazzoli C (2021) Cyber-physical systems improving building energy management: 
digital twin and artificial intelligence. Energies 14(8):2338. https://​doi.​org/​10.​3390/​EN140​82338
Agostinelli S, Cumo F, Nezhad MM, Orsini G, Piras G (2022) Renewable energy system controlled by open-source tools 
and digital twin model: zero energy port area in Italy. Energies 15(5):1817. https://​doi.​org/​10.​3390/​EN150​51817
Arup (2023a) Digital twin—arup. https://​www.​arup.​com/​servi​ces/​digit​al/​digit​al-​twin. Accessed 31 Aug 2023
Arup (2023b) The EU Green Deal and building retrofits: making it work for everyone. Accessed 31 Aug 2023
Autodesk (2023a) Autodesk Tandem. https://​intan​dem.​autod​esk.​com/. Accessed 31 Aug 2023
Autodesk (2023b) Revit for Architecture & Building Design | Autodesk. https://​www.​autod​esk.​com/​produ​cts/​revit/​archi​
tectu​re. Accessed 31 Aug 2023
Bjørnskov J, Jradi M (2023) An ontology-based innovative energy modeling framework for scalable and adaptable build‑
ing Digital Twins. Energy Build 292:113146. https://​doi.​org/​10.​2139/​SSRN.​43419​36
Bjørnskov J, Jradi M, Veje C (2022) Component-level re-commissioning of a newly retrofitted Danish healthcare building. 
J Build Eng 51:104277. https://​doi.​org/​10.​1016/J.​JOBE.​2022.​104277
Boje C, Guerriero A, Kubicki S, Rezgui Y (2020) Towards a semantic construction Digital Twin: directions for future research. 
Automation in Construction 114:103179. https://​doi.​org/​10.​1016/J.​AUTCON.​2020.​103179
Bortolini R, Rodrigues R, Alavi H, Vecchia LFD, Forcada N (2022) Digital twins’ applications for building energy efficiency: a 
review. Energies 15(19):7002. https://​doi.​org/​10.​3390/​EN151​97002
Bosch (2023) Digital Twins | bosch energy and building solutions Singapore. https://​www.​bosch​build​ingso​lutio​ns.​com/​
sg/​en/​news-​and-​stori​es/​digit​aliza​tion/. Accessed 31 Aug 2023
Catenda (2023a) Catenda hub. https://​bimsy​nc.​com/. Accessed 31 Aug 2023
Catenda (2023b) Catenda hub—the common data environment—Catenda. https://​caten​da.​com/​bim-​solut​ions-​open-​
stand​ards/​caten​da-​hub-​common-​data-​envir​onment/. Accessed 31 Aug 2023
Chiara Tagliabue L, Re Cecconi F, Maltese S, Rinaldi S, Luigi A, Ciribini C, Flammini A (2021) Leveraging Digital Twin for 
sustainability assessment of an educational. Building. https://​doi.​org/​10.​3390/​su130​20480
Clausen A, Arendt K, Johansen A, Sangogboye FC, Kjærgaard MB, Veje CT, Jørgensen BN (2021) A digital twin framework 
for improving energy efficiency and occupant comfort in public and commercial buildings. Energy Inf 4(2):1–19. 
https://​doi.​org/​10.​1186/​S42162-​021-​00153-9/​FIGUR​ES/​11
Dawson-Haggerty S, Jiang X, Tolle G, Ortiz J, Culler D (2010) sMAP. In: Proceedings of the 8th ACM conference on embed‑
ded networked sensor systems, pp. 197–210. ACM, New York, NY, USA. https://​doi.​org/​10.​1145/​18699​83.​18700​03
Elicit (2023) Elicit: the AI research assistant. https://​elicit.​org/. Accessed 31 Aug 2023
European commission (2018) Energy performance of buildings directive. https://​energy.​ec.​europa.​eu/​topics/​energy-​effic​
iency/​energy-​effic​ient-​build​ings/​energy-​perfo​rmance-​build​ings-​direc​tive_​en. Accessed 31 Aug 2023
European commission (2020) State of the Union: Commission raises climate ambition. https://​ec.​europa.​eu/​commi​ssion/​
press​corner/​detail/​en/​ip_​20_​1599. Accessed 31 Aug 2023
European Parliament (2010) Directive 2010/31/EU of the European Parliament and of the Council of 19 May 2010 on the 
energy performance of buildings. Accessed 31 Jan 2024
European Parliament (2023) energy performance of buildings: climate neutrality by 2050 | News | European Parliament. 
https://​www.​europ​arl.​europa.​eu/​news/​en/​press-​room/​20230​206IP​R72112/​energy-​perfo​rmance-​of-​build​ings-​clima​
te-​neutr​ality-​by-​2050. Accessed 31 Aug 2023
Fufa SM, Flyen C, Flyen A-C (2021) How can existing buildings with historic values contribute to achieving emission 
reduction ambitions? Appl Sci 11(13):5978. https://​doi.​org/​10.​3390/​app11​135978
Granderson J, Piette MA, Ghatikar G (2011) Building energy information systems: user case studies. Energy Eff 4(1):17–30. 
https://​doi.​org/​10.​1007/​s12053-​010-​9084-4
Grandlund (2023) Digital Twin presents property data visually and understandably—Granlund. https://​www.​granl​undgr​
oup.​com/​servi​ces/​digit​al-​twin/. Accessed 31 Aug 2023
Green building council (2023) LEED rating system | U.S. Green Building Council. https://​www.​usgbc.​org/​leed. Accessed 
31 Aug 2023
Hosamo HH, Svennevig PR, Svidt K, Han D, Nielsen HK (2022) A Digital Twin predictive maintenance framework of air 
handling units based on automatic fault detection and diagnostics. Energy Build 261:111988. https://​doi.​org/​10.​
1016/J.​ENBUI​LD.​2022.​111988
Hou H, Lai JH, Wu H, Wang T (2023) Digital twin application in heritage facilities management: systematic literature 
review and future development directions. https://​doi.​org/​10.​1108/​ECAM-​06-​2022-​0596
IEA (2019) Global status report for buildings and construction 2019—analysis—IEA. https://​www.​iea.​org/​repor​ts/​global-​
status-​report-​for-​build​ings-​and-​const​ructi​on-​2019. Accessed 31 Aug 2023
ISO (2018) ISO 16739-1:2018 - Industry Foundation Classes (IFC) for data sharing in the construction and facility manage‑
ment industries—Part 1: data schema. https://​www.​iso.​org/​stand​ard/​70303.​html. Accessed 31 Aug 2023
ISO: ISO 29481-1:2016 (2021) Building information models—Information delivery manual – Part 1: Methodology and 
format. https://​www.​iso.​org/​stand​ard/​60553.​html. Accessed 31 Aug 2023
Jradi M, Boel N, Madsen BE, Jacobsen J, Hooge JS, Kildelund L (2021) BuildCOM: automated auditing and continuous 
commissioning of next generation building management systems. Energy Inf 4(1):1–18. https://​doi.​org/​10.​1186/​
S42162-​020-​00136-2/​FIGUR​ES/7


---

Page 31

---

Page 31 of 31
Cespedes‑Cubides and Jradi ﻿Energy Informatics            (2024) 7:11 
	
Jradi M, Bjørnskov J (2023) A Digital Twin platform for energy efficient and smart buildings applications. In: 2023 fifth 
international conference on advances in computational tools for engineering applications (ACTEA) pp 1–6 https://​
doi.​org/​10.​1109/​ACTEA​58025.​2023.​10194​071
Jradi M, Madsen BE, Kaiser JH (2023) DanRETwin: a digital twin solution for optimal energy retrofit decision-making and 
decarbonization of the Danish building stock. Appl Sci 13(17):9778. https://​doi.​org/​10.​3390/​app13​179778
Kaewunruen S, Lian Q (2019) Digital twin aided sustainability-based lifecycle management for railway turnout systems. J 
Clean Prod 228:1537–1551. https://​doi.​org/​10.​1016/J.​JCLEP​RO.​2019.​04.​156
Khajavi SH, Motlagh NH, Jaribion A, Werner LC (2019) Digital Twin: vision, benefits, boundaries, and creation for buildings. 
IEEE Access 7:147406–147419. https://​doi.​org/​10.​1109/​ACCESS.​2019.​29465​15
Kritzinger W, Karner M, Traar G, Henjes J, Sihn W (2018) Digital Twin in manufacturing: a categorical literature review and 
classification. IFAC-PapersOnLine 51(11):1016–1022. https://​doi.​org/​10.​1016/J.​IFACOL.​2018.​08.​474
Kukkonen V, Kücükavci A, Seidenschnur M, Rasmussen MH, Smith KM, Hviid CA (2022) An ontology to support flow 
system descriptions from design to operation of buildings. Automation in Construction 134:104067. https://​doi.​org/​
10.​1016/J.​AUTCON.​2021.​104067
Lee D, Cha G, Park S (2016) A study on data visualization of embedded sensors for building energy monitoring using BIM. 
Int J Precisi Eng Manuf 17(6):807–814. https://​doi.​org/​10.​1007/​S12541-​016-​0099-4/​METRI​CS
Li S, Yang Q, Xing J, Chen W, Zou R (2022) A foundation model for building Digital Twins: a case study of a chiller. Build‑
ings 12(8):1079. https://​doi.​org/​10.​3390/​BUILD​INGS1​20810​79
Lu Q, Xie X, Heaton J, Parlikad AK, Schooling J (2020a) From BIM towards digital twin: strategy and future development 
for smart asset management. Stud Comput Intell 853:392–404. https://​doi.​org/​10.​1007/​978-3-​030-​27477-1_​30/​
FIGURE
Lu Q, Xie X, Parlikad AK, Schooling JM, Konstantinou E (2020b) Moving from building information models to digital twins 
for operation and maintenance. Proc Inst Civil Eng Smart Infrastruct Constr 174(2):46–56. https://​doi.​org/​10.​1680/​
JSMIC.​19.​00011
Lu Q, Parlikad AK, Woodall P, Don Ranasinghe G, Xie X, Liang Z, Konstantinou E, Heaton J, Schooling J (2020c) Developing 
a Digital Twin at building and city levels: case study of west Cambridge campus. J Manag Eng. https://​doi.​org/​10.​
1061/​(ASCE)​ME.​1943-​5479.​00007​63
Lu Q, Xie X, Kumar Parlikad A, Schooling JM (2020d) Digital twin-enabled anomaly detection for built asset monitoring in 
operation and maintenance. https://​doi.​org/​10.​1016/j.​autcon.​2020.​103277
Moretti N, Xie X, Merino J, Brazauskas J, Parlikad AK (2020) An openBIM approach to IoT integration with incomplete as-
built data. Appl Sci 10(22):8287. https://​doi.​org/​10.​3390/​APP10​228287
Ni Z, Eriksson P, Liu Y, Karlsson M, Gong S (2021) Improving energy efficiency while preserving historic buildings with digi‑
tal twins and artificial intelligence. IOP Conf Ser Earth Environ Sci. https://​doi.​org/​10.​1088/​1755-​1315/​863/1/​012041
Ni Z, Liu Y, Karlsson M, Gong S (2022) Enabling preventive conservation of historic buildings through cloud-based digital 
twins: a case study in the city theatre. Norrköping IEEE Access. https://​doi.​org/​10.​1109/​ACCESS.​2022.​32021​81
Peng Y, Zhang M, Yu F, Xu J, Gao S (2020) Digital Twin hospital buildings: an exemplary case study through continuous 
lifecycle. Integration. https://​doi.​org/​10.​1155/​2020/​88466​67
Penttilä H, Rajala M, Freese S (2022) Building information modelling of modern historic buildings. In: Proceedings of 
the 25th international conference on education and research in computer aided architectural design in Europe 
(eCAADe). pp 607–613 https://​doi.​org/​10.​52842/​CONF.​ECAADE.​2007.​607
Pressac (2018) What is a Digital Twin & How is It Used for Smart Facilities Management?. https://​www.​press​ac.​com/​insig​
hts/​what-​is-a-​digit​al-​twin-​and/. Accessed 31 Aug 2023
ResearchRabbit (2023) ResearchRabbit. https://​www.​resea​rchra​bbit.​ai/. Accessed 31 Aug 2023
SAREF (2020) SAREF extension for building. https://​saref.​etsi.​org/​saref​4bldg/​v1.1.​2/. Accessed 31 Aug 2023
SAREF (2023) SAREF Portal. https://​saref.​etsi.​org/. Accessed 31 Aug 2023
Siemens (2023) Building twin-digital building lifecycle—global. https://​www.​sieme​ns.​com/​global/​en/​produ​cts/​build​
ings/​digit​al-​build​ing-​lifec​ycle/​build​ing-​twin.​html. Accessed 31 Aug 2023
Uni Brescia building: eLUX (2016) https://​elux.​unibs.​it/. Accessed 31 Aug 2023
Volk R, Stengel J, Schultmann F (2013) Building Information Modeling (BIM) for existing buildings-Literature review and 
future needs https://​doi.​org/​10.​1016/j.​autcon.​2013.​10.​023
Wang C, Lee B, Shirowzhan S, Zhao Y, Wang N, Liu Z, Mu E (2022) Construction theory for a building intelligent operation 
and maintenance system based on digital twins and machine learning. Buildings 12(2):87. https://​doi.​org/​10.​3390/​
BUILD​INGS1​20200​87
Yitmen I, Alizadehsalehi S, Akiner I, Akiner ME (2021) An adapted model of cognitive digital twins for building lifecycle 
management. Appl Sci 11(9):4276. https://​doi.​org/​10.​3390/​APP11​094276
Zaballos A, Briones A, Massa A, Centelles P, Caballero V (2020) A smart campus’ digital twin for sustainable comfort moni‑
toring. Sustainability 12(21):9196. https://​doi.​org/​10.​3390/​SU122​19196
Zhao J, Feng H, Chen Q, Soto B (2022) Developing a conceptual framework for the application of digital twin technolo‑
gies to revamp building operation and maintenance processes. J Build Eng 49:104028. https://​doi.​org/​10.​1016/J.​
JOBE.​2022.​104028
Publisher’s Note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
