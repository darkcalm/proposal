

---

Page 1

---

Predictive digital twin for wind energy 
systems: a literature review
Ege Kandemir1*, Agus Hasan1, Trond Kvamsdal2 and Saleh Abdel‑Afou Alaliyat1 
Introduction
As the world shifts towards renewable and sustainable energy sources, wind turbines 
play a crucial role in this global change. Wind energy offers a promising new frontier in 
meeting the growing need for sustainable energy by utilizing the vast potential of wind 
resources in diverse environments. On the other hand, the installation and operation of 
wind farms pose challenges that demand innovative solutions to improve overall perfor-
mance, reliability, and efficiency. In this context, predictive digital twins have attracted 
attention as an innovative technology with the potential to fundamentally alter the wind 
energy market. Digital twins, which are virtual replicas of physical assets or systems, 
Abstract 
In recent years, there has been growing interest in digital twin technology 
in both industry and academia. This versatile technology has found applications 
across various industries. Wind energy systems are particularly suitable for digital twin 
platforms due to the integration of multiple subsystems. This study aims to explore 
the current state of predictive digital twin platforms for wind energy systems by sur‑
veying literature from the past five years, identifying challenges and limitations, 
and addressing future research opportunities. This review is structured around four 
main research questions. It examines commonly employed methodologies, includ‑
ing physics-based modeling, data-driven approaches, and hybrid modeling. Addition‑
ally, it explores the integration of data from various sources such as IoT sensors, histori‑
cal databases, and external application programming interfaces. The review also delves 
into key features and technologies behind real-time systems, including communica‑
tion networks, edge computing, and cloud computing. Finally, it addresses current 
challenges in predictive digital twin platforms. Addressing these research questions 
enables the development of hybrid modeling strategies with data fusion algorithms, 
which allow for interpretable predictive digital twin platforms in real time. Filter meth‑
ods with dimensionality reduction algorithms minimize the computational resource 
demand in real-time operating algorithms. Moreover, advancements in high-band‑
width communication networks facilitate efficient data transmission between physical 
assets and digital twins with reduced latency.
Keywords:  Wind energy systems, Predictive digital twin, Digital twin enabling 
technologies, Digital twin literature review, Wind energy literature review, Trends in 
predictive digital twin
Open Access
© The Author(s) 2024. Open Access  This article is licensed under a Creative Commons Attribution 4.0 International License, which permits 
use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original 
author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third 
party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the mate‑
rial. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or 
exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://​
creat​iveco​mmons.​org/​licen​ses/​by/4.​0/.
REVIEW
Kandemir et al. Energy Informatics            (2024) 7:68  
https://doi.org/10.1186/s42162-024-00373-9
Energy Informatics
*Correspondence:   
ege.kandemir@ntnu.no
1 Department of ICT and Natural 
Sciences, Norwegian University 
of Science and Technology, 
Ålesund, Norway
2 Department of Mathematical 
Sciences, Norwegian University 
of Science and Technology, 
Trondheim, Norway


---

Page 2

---

Page 2 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
allow real time monitoring, simulation, and predictive analysis. The application of pre-
dictive digital twins, especially in wind farms, offers valuable insights into the behavior 
and performance of systems, enhancing proactive decision-making, energy forecasting, 
and competence in the energy market.
Motivation and objective
The motivation behind of this literature review lies in the fact that, while there are sev-
eral reviews on digital twins, this study specifically focuses on predictive digital twins 
within the context of wind energy systems-a perspective that has not been previously 
explored. Conducting a review of predictive digital twins for wind farms is essential due 
to the critical necessity of addressing the inherent challenges in this dynamic and volatile 
environment. Some main challenges with wind farms are diverse and severe conditions, 
including variable wind patterns, complex environment interaction, and difficulties in 
data collection. These factors can impact the structural integrity, energy yield, and over-
all operational efficiency of wind turbines. Predictive digital twins have the potential to 
transform the way wind farms are monitored and managed. By integrating advanced 
data analytics, machine learning algorithms, statistical and probabilistic methods, and 
real time sensor data, these digital assets can predict potential issues before they esca-
late. This approach helps optimize performance and contributes to the reliability and 
cost-effectiveness of wind energy projects.
This review aims to comprehensively explore the current state of predictive digital 
twins for wind farms. The key objectives include:
•	 Surveying existing literature Providing a thorough overview of existing studies, 
research, and implementations related to predictive digital twins in the context of 
wind energy.
•	 Assessing current methods Evaluating the advancements in predictive modeling, data 
analytics, and machine learning techniques applied to wind farm operations. Inves-
tigating how predictive digital twins contribute to enhancing the performance, reli-
ability, and energy yield of wind farms.
•	 Identifying challenges and limitations Identifying and critically analyzing the chal-
lenges, limitations, and gaps in current research and applications of predictive digital 
twins in the wind industry.
•	 Proposing future directions Proposing potential directions for future research, 
emphasizing areas that necessitate exploration to enhance the capabilities of predic-
tive digital twins in the realm of wind energy.
This review aims to consolidate and synthesize the existing knowledge, providing valua-
ble insights for researchers and stakeholders who are involved in advancing wind energy 
through the application of predictive digital twin technologies.
Problem definition and contribution
Predictive digital twins within the realm of wind energy systems have attracted sig-
nificant attention in recent decades. The creation of predictive digital twin platforms 
has been made possible by real time data, simulation models, and advanced analytical 


---

Page 3

---

Page 3 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
	
methods. This technology not only allows stakeholders to forecast potential issues but 
also enhances informed decision-making and performance optimization. Despite the 
growing investment in this field, there remains a need for a comprehensive understand-
ing of the current state of research and development in predictive digital twin appli-
cations specific to wind energy systems. The main challenge lies in the lack of solid 
knowledge regarding key challenges and advancements, along with a gap in the literature 
related to predictive digital twins in wind energy systems. As the field is rapidly evolving, 
there is a risk of inconsistency and limited transferability of findings across different sys-
tems and industries. Additionally, the effectiveness of predictive digital twins in enhanc-
ing the overall performance and reliability of wind energy systems remains unclear, given 
the data provided by several independent sources. The integration and analysis of vari-
ous data still pose prominent issues. To address these challenges, a literature review is 
necessary to comprehend existing knowledge, identify trends, and provide a foundation 
for future research.
This paper contributes to the understanding and development of digital twin tech-
nology within wind energy systems through a comprehensive literature review. A sys-
tematic approach is used in the review, beginning with the formulation of the research 
question and establishment of the review protocol. Relevant studies are then searched in 
the selected databases using the defined query strings. By conducting a literature survey 
from the past five years, this study presents key trends and advancements in predictive 
digital twin platforms. The analysis identifies current challenges and limitations, while 
also discussing commonly employed methodologies, with a focus on enhancing digital 
twin systems. Furthermore, future research opportunities are outlined to lay a founda-
tion for ongoing advancements in this field. This review seeks to offer valuable insights 
and practical guidance for academics, industry professionals, or technology developers 
working on digital twin technology in the wind energy sector.
Background information
A digital twin is a representation of a physical system created through digital informa-
tion. This digital counterpart serves as a duplicate of the information embedded in the 
physical system and remains interconnected with it throughout the lifecycle. The origins 
of the Digital Twin concept can be traced back to a 2002 University of Michigan presen-
tation aimed at establishing a Product Lifecycle Management. Figure 1 provides a visual 
depiction of the digital twin, highlighting its primary components: real space, virtual 
space, the link for data and information flow from real space to virtual space (Grieves 
2016).
The digital twin concept operates on three main fronts: first, it stores essential 
component data. In this capacity, the digital twin systematically collects, organizes, 
and stores critical information pertaining to the physical system’s components. This 
encompasses a detailed inventory of the structure, dynamics, and configuration of the 
various elements of the system. This repository is not only used for the current state 
but also lays the groundwork for several processes. The stored data becomes the foun-
dational building block upon which the digital twin can further analyze, simulate, and 
visualize the behavior of the physical system. In the realm of wind energy, the digital 
twin may capture detailed information about the turbine’s components, such as the 


---

Page 4

---

Page 4 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
specifications of the rotor blades, turbine output, the configuration of the generator 
or gearbox, also parameters related to environment like wind speed and wind direc-
tion. More specifically, the digital twin might store data on the aerodynamic profiles 
of the rotor blades, including their material composition and dimensions (Jureczko 
et al. 2005). It would document the specifications of the gearbox, detailing gear ratios 
and load-bearing capacities (Moghadam et  al. 2021). Wind sensor data, historical 
wind patterns, and turbine performance metrics, such as power output and efficiency, 
would also be systematically recorded. This detailed component data can be used as 
the foundation for subsequent analyses and simulations. This information can then 
be used to simulate the wind turbine’s behavior under various conditions, to optimize 
the turbine’s performance. Second, it analyzes and simulates the asset based on that 
data, where computational models and algorithms are utilized to examine the stored 
data within the digital twin. The digital twin employs advanced analytical tools and 
machine learning algorithms to simulate the behavior of the physical system under 
various conditions. These models are intended to replicate the dynamic interactions 
between components and the environment. The simulations and models enable us to 
gain insights into how the asset responds to different inputs, environmental factors, 
or operational scenarios. These virtual tests can identify potential issues or efficiency 
losses, enabling us to comprehensively assess the system. A digital twin for a wind 
turbine leverages stored data to conduct detailed performance analyses and simula-
tions. For instance, the digital twin may employ computational models that consider 
parameters such as wind speed, blade geometry, and turbine specifications. Analyz-
ing the data could involve simulations to predict power generation output at varying 
wind speeds. The digital twin can be used to assess the wind direction impact on the 
turbine’s yaw mechanism, optimizing its alignment for maximum energy capture (Wu 
and Wang 2012). Structural simulations may also be employed to evaluate the integ-
rity of turbine components, helping identify potential stress points or areas requiring 
Fig. 1  Conceptual framework of digital twin for a wind turbine. The physical asset consists of sensors and IoT 
devices. The digital twin platform consists of three main fronts: big data and analytics, simulation & property 
modeling, and visualization. Data is provided from the physical assets to the digital twin platform, where 
information and processes are sent to the physical asset from the digital twin platform


---

Page 5

---

Page 5 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
	
maintenance (Bazilevs et al. 2015). Forecasting algorithms can also be implemented 
to estimate the power output in different time horizons (Hanifi et al. 2020). Imple-
menting all these models enhances efficiency by providing a deep understanding of 
performance, minimizing downtime under diverse conditions. Third, it visualizes rel-
evant data and results according to predefined objectives. These presentations pro-
vide insights through the digital twin’s simulation processes. In this phase, the digital 
twin transforms complex data and simulation results into comprehensible visual rep-
resentations. These visualizations align with predefined objectives, to ensure that the 
information presented is relevant and serves specific needs. Visualization of a digital 
twin involves creating graphical representations, a dashboard, 3D visualizations, and 
other illustrative formats that convey key findings (Kandemir et al. 2023). These visual 
outputs may include performance metrics, trends, and critical insights derived from 
the analytical simulations. The primary goal is to present the information in a clear 
and accessible way, facilitating effective communication and decision-making among 
various stakeholders. In this way, stakeholders can intuitively grasp the complexities 
of the physical system. In the context of wind turbines, a predefined objective is to 
optimize energy production; the digital twin could generate visualizations that display 
real time power output, efficiency trends, and the impact of different wind conditions 
on energy generation. These tools could include graphical representations of power 
curves, efficiency maps, and performance trends of subsystems (Rafiee et al. 2018). 
These visualizations can be used to quickly assess the impact of wind speed, direction, 
or turbine settings on energy production. Additionally, the digital twin might gener-
ate visual alerts or dashboards highlighting areas of the turbine that require attention 
or maintenance.
Digital twin applications rely on four key technologies: “Internet of Things”, “Data 
and Analytic”, “Cloud Computing” and “Accessibility and Interaction” (Wang and Liu 
2022). The Internet of Things (IoT) functions as a system where physical devices are 
embedded with software, utilizing Internet connectivity. Various techniques, such 
as Bluetooth, Wi-Fi, RFID, and GPRS, can establish connections in IoT, facilitating 
communication between physical and virtual entities for data transfer. Many compa-
nies are actively investing in IoT to foster machine-to-machine communications. The 
framework is structured into three primary layers: perception, network, and appli-
cation. In the perception layer, interaction with the environment occurs through 
sensors and actuators. The network layer manages connections between diverse enti-
ties, including “things,” network devices, and servers, processing data in the process. 
The final layer provides services to users (Shah et al. 2018; Mouha 2021). Data and 
Analytics encompass the utilization of various corporate tools like Standard Query 
Language (SQL) for tasks such as data storage, manipulation, and retrieval. In this 
process, it’s crucial to evaluate data through advanced methods that align with spe-
cific objectives. These analytics involve a range of methods, including physics based 
models, statistical and predictive analysis, machine learning, and artificial intelligence 
(Fowdur et  al. 2018). Cloud Computing enables people to reach, share, and store 
information via the Internet. This innovative computing technology utilizes a network 
of data centers with interconnected computers, allowing the execution of software 
functions. Users have access to powerful platforms, and services over the Internet, 


---

Page 6

---

Page 6 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
making it a versatile collection of network-enabled services. Cloud Computing pro-
vides on-demand, flexible, and tailored computing infrastructures to a wide range of 
stakeholders (Kalapatapu and Sarkar 2012). Accessibility and Interaction with Digital 
Twin involve examining physical systems from a distance. The digital twin stands out 
by being reachable remotely, facilitating global data transfer with fewer limitations. 
In scenarios where local access is limited, the need for remote monitoring and con-
trol of assets becomes apparent. Moreover, within complex systems, understanding 
subsystems poses a challenge, but the digital twin simplifies understanding both sub-
systems and the interaction between systems (Singh et al. 2021). Human interaction 
emphasizes communication and interaction between humans and machines. Emerg-
ing technologies in this area include virtual and augmented reality, 3D visualizations, 
and recognition algorithms (Ma et al. 2019).
Outline
In "Methodology" Section, the methodology is outlined, detailing the establishment of 
a review protocol that plays a pivotal role in the investigation of predictive digital twin 
technology. Specifically, inclusion criteria are outlined, the search strategy is executed, 
and a systematic approach is employed to explore relevant literature. In "Results" Sec-
tion, the results of the literature review are provided, aligning with the research ques-
tions and presenting key findings on predictive digital twin technology, including current 
applications, methods, and emerging trends. Section "Discussion" engages in a discus-
sion, analyzing the implications, trends, and methods identified in the literature. This 
section aims to gain a deeper understanding of the context of predictive digital twins. In 
"Conclusions and future work" Section, conclusions are drawn, summarizing the state of 
predictive digital twins based on insights obtained from the literature review.
Methodology
The methodology is inspired by the guidelines proposed by Kitchenham and Charters 
(2007) for a systematic literature review. Well-formulated research questions are essen-
tial as they guide the search, selection, and analysis of relevant studies which provides a 
comprehensive overview of existing research on a specific topic. The predefined search 
strategy and inclusion/exclusion criteria enhance reliability. Reviews significantly con-
tribute to scientific knowledge by summarizing findings, identifying gaps, and establish-
ing a reliable foundation for future research. The format also promotes transparency and 
credibility, owing to the well-established protocol. This paper is conducted in three main 
steps, as shown in Fig. 2, which include planning, execution, and reporting.
The planning phase is dedicated to the formulation of an effective search strat-
egy and establishing criteria to evaluate the quality of the gathered studies. Dur-
ing the execution stage, the focus lies on the identification of pertinent studies and 
the extraction of the employed methodologies for the corresponding studies. The 
reporting phase synthesizes all the acquired findings and methodologies, facilitating 
a comprehensive and critical discussion of the outcomes. In essence, this three-step 
methodology provides a structured framework for conducting literature review.


---

Page 7

---

Page 7 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
	
Research questions
The research question in a literature review is crucial as it shapes the entire study. Its sig-
nificant role lies in establishing an unbiased framework essential for maintaining objec-
tivity, reliability, and credibility. A well-formulated research question ensures a thorough 
analysis of existing literature, contributing to the academic integrity of the review. In 
this context, four research questions have been formulated: (1) targeting methodologies, 
(2) addressing the integration of data from various sources, (3) focusing on real time 
decision-making, and (4) delving into challenges.
•	 RQ1: What methodologies are commonly employed in developing predictive digital 
twin models for wind energy systems?
•	 RQ2: How do predictive digital twin applications integrate and analyze data from 
diverse sources to enhance their predictive capabilities?
•	 RQ3: What are the key features and technologies that facilitate real time wind energy 
systems through predictive digital twin?
•	 RQ4: What are the challenges commonly encountered in wind energy systems when 
implementing predictive digital twin solutions?
Search strategy
For the literature review on predictive digital twin in wind energy systems, a com-
prehensive search strategy was developed. This strategy involved the utilization of 
academic databases and search engines such as IEEE Xplore, Scopus, ACM Digital 
Fig. 2  Framework for a literature review. Plan: Develop the research question, establish the review protocol, 
and create query strings for database searches. Execution: Identify relevant research, filter results based on 
established quality criteria, and identify proposed methods. Report: Analyze multiple methods found in the 
literature and document the findings


---

Page 8

---

Page 8 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
Library, SpringerLink, Wiley Online Library, and Taylor & Francis Online. The search 
string was structured using a combination of keywords and Boolean operators (AND, 
OR) to refine the search results effectively. The keywords and logical operators are 
explicitly detailed in Table 1 with the corresponding research questions. The search 
was conducted across the selected databases between the years 2019 and 2024, aim-
ing to identify relevant studies published within the last 5 years.
Quality criteria and study selection
To ensure transparency and minimize potential bias in the literature review on pre-
dictive digital twins for wind energy systems, quality and inclusion criteria were 
established. These criteria were applied to the selection of studies in accordance with 
PRISMA guidelines (Page et al. 2021). The selection process involved evaluating stud-
ies based on predefined criteria, as outlined in Table 2. The criteria emphasize studies 
employing research methodologies such as experimental studies, case studies, simu-
lations, and theoretical frameworks relevant to predictive digital twin applications in 
wind energy. Only peer-reviewed articles published in academic journals, conference 
proceedings, and scholarly books from recognized publishers are included, with Eng-
lish as the publication language. The review captures the most current advancements 
and developments in the field over the last 5 years. The qualified study went through 
the process of multiple stages, including title, abstract, and keyword screening fol-
lowed by full-text assessment. Figure 3 explicitly outlines each step of the study selec-
tion procedure.
Table 1  Search strings used in the digital libraries and databases
Boolean logical operators (“AND”, “OR”) used in the search. “AND” searches find all the search strings, while “OR” searches find 
one term or the other. The first part of the “AND” search is common for all four research questions, targeting studies focused 
on digital twin or wind energy related studies. The second part of the “AND” term is specified for each research question
No
Keywords
RQ-1 (“DT” OR “Predictive Digital Twin” OR “Wind Energy” OR “Wind Turbine” OR “Wind Farm”) AND (“Physics Based 
Modelling” OR “Data Driven Models” OR “Hybrid Models”)
RQ-2 (“DT” OR “Predictive Digital Twin” OR “Wind Energy” OR “Wind Turbine” OR “Wind Farm”) AND (“Data” OR 
“Feature Selection” OR “Dimensionality Reduction” OR “Real Time”)
RQ-3 (“DT” OR “Predictive Digital Twin” OR “Wind Energy” OR “Wind Turbine” OR “Wind Farm”) AND (“Key Features” 
OR “Enabling Technologies” OR “IoT” OR “Communication” OR “Computing” OR “Human Machine Interface”)
RQ-4 (“DT” OR “Predictive Digital Twin” OR “Wind Energy” OR “Wind Turbine” OR “Wind Farm”) AND (“Challenges” 
OR “Quality” OR “Complex Models” OR “Model Order Reduction” OR “Validation” OR “Calibration”)
Table 2  Systematic literature review inclusion and quality criteria
No
Criteria
1
The study is written in English
2
The study is available as a full-text
3
The study is published in a scientific peer-reviewed journal, conference, book or book chapter
4
The study is related to Digital Twin “OR” Wind Energy Systems “OR” Digital Twin Enabling Technologies
5
The study is published within last five years
6
The study is implements Experimental Study “OR” Simulation “OR” State of Art Framework


---

Page 9

---

Page 9 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
	
Methodology extraction and synthesis
This section outlines the methodology extraction and synthesis process utilized in the 
literature review on predictive digital twin technology in wind energy systems. The 
objective was to gather and integrate information on the methods, models, and tech-
nologies employed in the selected studies. Each study was examined for the methods 
and frameworks implemented or conceptualized in predictive digital twin models for 
wind energy systems, including validation models. Another important aspects were the 
sources of data, modeling techniques, simulation tools, validation methods, and reason-
ing approaches applied. By identifying the methodologies, and technologies employed in 
these studies, the review provides a comprehensive overview of the diverse approaches 
in predictive digital twin technology for wind energy. The synthesis of methodologies 
given in the discussion ("Discussion" Section ), directly aligned with the research ques-
tions posed at the outset of the review, allowing insights into specific aspects of pre-
dictive digital twin technology. The initial number of studies from the database search 
and the selected studies with complete citations are provided at the end of each research 
question in the results section as Tables 3, 5, 6 and 7.
Results
RQ1: What methodologies are commonly employed in developing predictive digital twin 
models for wind energy systems?
Developing predictive digital twin models for wind energy systems involves leverag-
ing advanced methodologies to accurately simulate and forecast the performance and 
behavior of wind turbines. In this context, three main categories of methodologies are 
identified: physics-based modeling, data-driven approaches, and hybrid models. These 
categories were selected based on current research and applications within the field of 
wind energy systems (Vargas et al. 2019; Liu and Chen 2019).
Physics based modeling
Physics based modeling constitutes one of the core elements for wind energy systems, 
crucial for optimizing performance and ensuring reliability. This section elaborates on 
the key submodels involved: structure, aerodynamics, electric model, and control. These 
four submodels in wind energy system modeling are essential for design, analysis, and 
optimization.
The structural model covers the mechanical behavior of wind turbine compo-
nents. Structural dynamics enable the investigation of wind turbines under various 
Fig. 3  Study selection diagram. Step 1: Study search in selected databases, Step 2: Removal of duplicate 
studies, Step 3: Filtering the studies according to quality criteria, Step 4: Screening the studies based on 
abstract and keywords, Step 5: Screening the studies based on full text, Step 6: Inclusion of relevant studies


---

Page 10

---

Page 10 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
loads. Techniques such as finite element analysis enable the prediction of wind tur-
bine responses. These dynamics involve modeling bending and torsion moments, 
along with tension, compression, and shear forces  (Hernandez-Estrada et  al. 2021; 
Jahani et al. 2022; Rajamohan et al. 2022). Studies also consider periodic loads that 
may cause fatigue effects (Fu et al. 2020; Njiri et al. 2019). Additionally, due to the 
high aspect ratio of wind turbines, aeroelastic effects such as flutter are accounted 
for (Chen et al. 2021; Li et al. 2020; Ma et al. 2019). By assessing all these factors, 
structural integrity and longer lifespan can be achieved. Material properties play a 
pivotal role in the structural model. Incorporating characteristics such as elastic-
ity, damping, or strength is crucial for accurately representing the behavior of tur-
bine components (Pradeep et al. 2019; Igwemezie et al. 2019; O’Leary et al. 2019). 
Table 3  Primary studies related to research question 1
Model type
Number of studies 
from initial database 
search
Selected studies
Physics based modelling 182
Hernandez-Estrada et al. (2021), Jahani et al. (2022), 
Rajamohan et al. (2022), Fu et al. (2020), Njiri et al. (2019), 
Chen et al. (2021), Li et al. (2020), Ma et al. (2019), Pradeep 
et al. (2019), Igwemezie et al. (2019), O’Leary et al. (2019), 
Ren et al. (2021), Zhao et al. (2019), Mu et al. (2023), Zilong 
and Xiao Wei (2022), Porchetta et al. (2021) Qian et al. 
(2020), Vogel and Willden (2020), Hornshøj-Møller et al. 
(2021), Ledoux et al. (2021), Zhang and Qu (2021), Tahir 
et al. (2019), Branlard et al. (2022), Papi et al. (2024), Ferreira 
et al. (2022), Kaviani and Nejat (2021), Sedaghatizadeh et al. 
(2019), Tian et al. (2019) Xiaoyu and Chao (2019), Huang 
et al. (2019), Ravanji et al. (2020), Basit et al. (2020), Li et al. 
(2020), Navarrete et al. (2019), Sierra-García and Santos 
(2021), Gambier (2021), Yang et al. (2021), Saenz-Aguirre 
et al. (2019), Liu et al. (2021), Bashetty et al. (2020), Akbari 
et al. (2019), Merizalde et al. (2019), Udo and Muhammad 
(2021), Hsu et al. (2020)
Data-driven approaches
134
Fahrmeir et al. (2021), Liu and Chen (2019), Gualtieri (2019), 
Barhmi et al. (2020), Dupré et al. (2020), López and Arboleya 
(2022), Wang et al. (2021), Niu et al. (2022), Liu et al. (2021), 
Naik et al. (2019), Zheng et al. (2023), Carneiro et al. (2022), 
Elyasichamazkoti and Khajehpoor (2021), Li et al. (2020), 
Tuerxun et al. (2021), Lu et al. (2020), Barhmi and Fatni 
(2019), Nielson et al. (2020), Sun et al. (2020), Huang et al. 
(2021), Kisvari et al. (2021), Banik et al. (2020), Shahid et al. 
(2021), Shivani et al. (2019), Elsaraiti and Merabet (2021), 
Sheoran and Pasari (2022), Liu et al. (2021), Tyass et al. 
(2022), Keyantuo et al. (2021), Messner and Pinson (2019), Li 
and Wu (2020), Qian et al. (2019), Simon et al. (2024), Mbuli 
et al. (2020), Yan et al. (2022)
Hybrid modelling
141
Kosovic et al. (2020), Zhang et al. (2020), Du et al. (2019), 
Zhang et al. (2019), Wang et al. (2022), Korprasertsak and 
Leephakpreeda (2019), Aly (2020), Hur (2021), Alhussein 
et al. (2020), Aly (2020), Lv et al. (2022), Mamun et al. (2020), 
Kaya (2019), Morita et al. (2022), Dong et al. (2021), Dong 
et al. (2022), Liang et al. (2020), Liu and Liang (2021), Choi 
et al. (2022), Cai et al. (2021), Zhilyaev et al. (2022), Li et al. 
(2024), Cheng and Yao (2022), Kareem (2020), Miyanawala 
and Jaiman (2019a), Reddy et al. (2019b), Wu and Ma 
(2022), Selvaraj and Selvaraj (2022), Buabeng et al. (2021), 
Heydari et al. (2021), Beretta et al. (2021), Pandit et al. 
(2023), Maldonado-Correa et al. (2024), Zhang et al. (2022), 
Liu et al. (2021), Guo and Wang (2021)


---

Page 11

---

Page 11 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
	
Given the diverse operating conditions and environmental effects, assessing the life-
long performance also relies on correctly represented material properties. In terms 
of structural modeling, tower and foundation design are additional aspects that need 
to be considered. The analysis of interactions with the ground, such as soil properties 
or seismic loads, is essential for onshore wind farm infrastructures (Ren et al. 2021; 
Zhao et  al. 2019). Moreover, in offshore wind farms, the hydrodynamic effects on 
the wind turbines have a significant impact, requiring materials that can withstand 
harsher conditions such as high salinity causing oxidation (Mu et al. 2023). The influ-
ence of high-amplitude waves on freestream affects the dynamic pressure. Especially 
for floating offshore wind turbines, precise models are required to investigate com-
plex dynamics involving surface waves and subsurface ocean currents  (Zilong and 
Xiao Wei 2022; Porchetta et al. 2021).
The aerodynamics model predicts the interaction between the wind, turbine blades, 
and the influence of the wind turbines on one another. Computational fluid dynamics 
uses numerical methods to analyze and solve fluid flow problems. Several techniques, 
such as finite volume or finite differences, are employed in the solution method. The dif-
ferential equations, such as the Navier–Stokes equations, enable the description of the 
relation between pressure, temperature, velocity, and density of a moving fluid (Qian 
et al. 2020; Vogel and Willden 2020; Hornshøj-Møller et al. 2021). Additionally, the Blade 
Element Momentum Theory combines two phenomena, the blade element theory and 
momentum theory, to calculate aerodynamic forces and moments, considering airfoil 
characteristics and aerodynamic losses (Ledoux et al. 2021; Zhang and Qu 2021; Tahir 
et al. 2019). Dynamic inflow affects the wind energy system as wind turbines reach a 
steady state after a change in the existing state, such as sudden pitch angle variation or 
tower shadow. Accounting for this effect would enhance the capability to capture the 
time-varying behavior of aerodynamic performance  (Branlard et  al. 2022; Papi et  al. 
2024; Ferreira et al. 2022). Although aeroelastic effects are mentioned in the previous 
paragraph, it should be noted that elastic deformations lead to changes in the aerody-
namic characteristics of the wind turbine, causing unpredictable behavior (Kaviani and 
Nejat 2021). Boundary layer models, both in laminar and turbulent flow on the blade 
surface, should be another consideration due to their effect on aerodynamic perfor-
mance and noise generation (Sedaghatizadeh et al. 2019; Tian et al. 2019).
The electric model simulates the electrical aspects of wind energy systems, focusing 
on power conversion and integration with the grid. It involves simulating the electrical 
properties a generator, such as synchronous/asynchronous operation (Xiaoyu and Chao 
2019), excitation control, and voltage regulation (Huang et al. 2019; Ravanji et al. 2020), 
to enhance power generation and grid stability. Additionally, the electric model includes 
models of power electronics such as rectifiers, inverters, and converters to link variable-
speed turbines with the grid, ensuring efficient energy conversion. Moreover, the electric 
model examines grid connection dynamics, ensuring compliance with grid codes, and 
managing reactive power, thereby facilitating the smooth integration of wind turbines 
into the electrical grid. Basit et al. (2020); Li et al. (2020)
The control model governs the operation of the wind turbine for optimum per-
formance, safety, and reliability. Pitch control algorithms are one of the most popular 
methods for adjusting the blade pitch angle to optimize energy capture and respond to 


---

Page 12

---

Page 12 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
different wind conditions. By implementing pitch control algorithms, stable operations 
can be conducted across a wide range of environmental conditions  (Navarrete et  al. 
2019; Sierra-García and Santos 2021; Gambier 2021). Similarly, yaw control is a method 
used to increase efficiency. With this control strategy, the turbine aligns with the incom-
ing wind direction, capturing maximum energy with minimum structural load  (Yang 
et al. 2021; Saenz-Aguirre et al. 2019; Liu et al. 2021). Another algorithm in the con-
trol model is the rotor speed regulation algorithm, which determines the optimum rota-
tional speed through pitch control or generator torque control. This helps minimize 
mechanical stress while maximizing efficiency (Bashetty et al. 2020; Akbari et al. 2019). 
Additionally, fault detection and diagnostics algorithms enhance wind energy system 
operations. Monitoring system health and detecting anomalies can prevent catastrophic 
consequences. Fault detection and predictive maintenance enable cost-effective opera-
tion (Merizalde et al. 2019; Udo and Muhammad 2021; Hsu et al. 2020).
Data‑driven approaches
In data-driven approaches for wind energy systems, several techniques can be applied 
depending on the characteristics of a dataset and the required prediction task. These 
methods are investigated in three main categories: regression models, machine learning 
algorithms, and statistical methods.
A regression model is a statistical method used to analyze the relationship between 
a dependent variable and one or multiple independent variables. The aim is to pre-
dict the value of the dependent variable based on the values of the independent vari-
ables  (Fahrmeir et  al. 2021). Regression models are commonly used for prediction, 
forecasting, and understanding the influence of different variables on an outcome (Liu 
and Chen 2019; Gualtieri 2019). Although there are several types of regression models 
in wind energy systems, three model types are commonly used: linear regression, poly-
nomial regression, and ridge regression. Linear regression is mainly used to predict the 
linear relation of turbine power output based on variables such as wind speed, wind 
direction, or environmental effects (Barhmi et al. 2020; Dupré et al. 2020; López and 
Arboleya 2022). On the other hand, polynomial regression captures the nonlinear corre-
lation of input variables with turbine performance parameters. This method enables the 
comprehension of complex nonlinear interactions among independent variables (Wang 
et al. 2021; Niu et al. 2022; Liu et al. 2021). Ridge regression ensures more stable pre-
dictions between input variables and output performance by including a regularization 
term to prevent overfitting. It is particularly useful when the correlation between inde-
pendent variables is high, and it finds application in design, optimization, and forecast-
ing (Naik et al. 2019; Zheng et al. 2023; Carneiro et al. 2022).
Machine learning algorithms are popular methods used in wind energy systems. By 
analyzing various datasets, including weather patterns, turbine operations, and mainte-
nance records, machine learning algorithms can identify patterns to improve the over-
all efficiency of wind energy production (Elyasichamazkoti and Khajehpoor 2021). The 
most common algorithms used for this purpose include support vector machines (SVN), 
artificial neural networks (ANN), recurrent neural networks (RNN), and long short-term 
memory (LSTM) networks. A support vector machine is a supervised machine learn-
ing algorithm used for data classification and regression analysis. It can classify different 


---

Page 13

---

Page 13 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
	
wind conditions, enabling optimal wind settings (Li et al. 2020; Tuerxun et al. 2021; Lu 
et al. 2020). Artificial neural networks learn complex patterns such as wind speed or 
direction to predict turbine power output accurately with optimum parameters (Barhmi 
and Fatni 2019; Nielson et al. 2020; Sun et al. 2020). Recurrent neural networks are pow-
erful tools, especially for learning sequential data and predicting sequential outputs. 
They can capture temporal dependencies and nonlinear dynamics in time-series data, 
allowing for accurate forecasts (Huang et al. 2021; Kisvari et al. 2021). Long short-term 
memory networks are specialized versions of recurrent neural networks that enable 
forecasts over extended time horizons (Banik et al. 2020; Shahid et al. 2021).
Statistical models are another popular method due to their interpretability and abil-
ity to capture temporal patterns. Some of the commonly used methods, specifically for 
wind energy systems, are autoregressive integrated moving average (ARIMA), vector 
autoregression, and seasonal decomposition. Autoregressive integrated moving aver-
age models consist of three main components: autoregression, differencing, and moving 
average (Shivani et al. 2019; Elsaraiti and Merabet 2021; Sheoran and Pasari 2022). This 
model can also be extended for non-stationary time series by accounting for seasonality. 
The method facilitates short term planning for turbine operation (Liu et al. 2021; Tyass 
et al. 2022). Unlike the previous method, vector autoregression is useful for dealing with 
multiple time series variables as they interact with each other. For instance, the influ-
ence of wind speed, temperature, and pressure on wind power generation, along with 
their dependencies with each other, can be investigated with this model (Keyantuo et al. 
2021; Messner and Pinson 2019; Li and Wu 2020). Although seasonal decomposition is 
not a forecasting technique, it is an important technique for understanding the underly-
ing components of time series. The main classical decomposition components are trend, 
seasonal, and residual components. This technique is widely used in wind energy sys-
tems (Qian et al. 2019; Simon et al. 2024; Mbuli et al. 2020; Yan et al. 2022).
Hybrid modelling
In the evolving field of wind energy, hybrid modeling techniques have attracted signifi-
cant attention as robust solutions by integrating physics knowledge with data-driven 
approaches. This section focuses on the main five advanced hybrid methodologies in 
forecasting, grid integration, fluid dynamics, structure, and predictive maintenance. As 
they rely on both physical laws and machine learning, accurate and reliable models for 
predictive digital twin platforms for wind energy systems can be achieved.
Hybrid forecasting models integrate machine learning algorithms with numeri-
cal weather prediction models for accurate wind speed predictions, which later yield 
power output forecasts for the wind turbines. Time series analysis employs methods like 
ARIMA, LSTM, or fuzzy logic with the numerical weather prediction models to forecast 
wind conditions (Kosovic et al. 2020; Zhang et al. 2020; Du et al. 2019). Ensemble meth-
ods are particularly useful for merging different models to quantify uncertainties (Zhang 
et al. 2019; Wang et al. 2022; Korprasertsak and Leephakpreeda 2019). Also, data assimi-
lation methods like the Kalman filter or its variations are important for combining real-
time sensor data with forecast models implemented in digital twin platforms (Aly 2020; 
Hur 2021). As wind energy production forecasting models enhance the supply side of 
grid integration, hybrid models for electricity load estimation can be utilized to estimate 


---

Page 14

---

Page 14 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
the demand side. Some commonly deployed hybrid algorithms include artificial neural 
networks, wavelet neural networks, Kalman filtering, convolutional neural networks 
(CNN), and LSTM models with physics-based models (Alhussein et al. 2020; Aly 2020; 
Lv et al. 2022; Mamun et al. 2020).
Hybrid aerodynamic models combine high-fidelity computational fluid dynamics 
(CFD) simulations with machine learning models for optimum aerodynamic perfor-
mance. Computational fluid dynamics simulations are used to generate data for machine 
learning models, such as Gaussian process regression or support vector regression, to 
reduce computational costs  (Kaya 2019; Morita et  al. 2022). Similarly, reinforcement 
learning algorithms based on real-time data and computational fluid dynamics data 
are applied for control strategies  (Dong et  al. 2021, 2022). Additionally, data derived 
from computational fluid dynamics simulations are corrected with real-time data using 
Kalman filtering to improve accuracy (Liang et al. 2020; Liu and Liang 2021). A phys-
ics-informed neural network incorporates partial differential equations governing fluid 
dynamics, such as the Navier–Stokes equations, into the neural network architecture, 
allowing for interpretability (Choi et al. 2022; Cai et al. 2021).
Similar to hybrid aerodynamic models, hybrid structural models integrate finite ele-
ment analysis with machine learning algorithms such as SVM, ANN, and CNN (Zhily-
aev et al. 2022; Li et al. 2024; Cheng and Yao 2022). These analyses are used to optimize 
design parameters. Moreover, the multiphysics interaction of fluid flow with structures 
(fluid–structure interaction), integrating mechanical and fluid dynamics and enhanced 
with machine learning algorithms, enables the prediction of complex interactions in the 
environment (Kareem 2020; Miyanawala and Jaiman 2019a; Reddy et al. 2019b).
Hybrid predictive maintenance models combine various anomaly detection techniques 
with data-driven approaches to identify potential failures or estimate the remaining life 
of wind turbines. These hybrid models can be used to diagnose several components of 
the wind turbine using different sensor data and in-built predictive models (Wu and Ma 
2022; Selvaraj and Selvaraj 2022; Buabeng et al. 2021). In wind turbines, the gearbox, 
bearings, and other rotating components are the main points of interest. In study (Hey-
dari et al. 2021), hybrid modelling for gearboxes, which are often prone to failure, is the 
focus. The proposed framework consists of several different methods: clustering filters, 
ant bee colony optimization algorithm, variational mode decomposition, multi-verse 
optimization algorithm, and wavelet transform. Combining these methods enables the 
detection of anomalies before a failure occurs. Primarily, supervisory control and data 
acquisition system data are utilized for this purpose (Heydari et al. 2021; Beretta et al. 
2021; Pandit et al. 2023; Maldonado-Correa et al. 2024). Another important predictive 
analysis is the estimation of the remaining useful life of the components for proactive 
maintenance scheduling (Zhang et al. 2022; Liu et al. 2021; Guo and Wang 2021).
RQ2: How do predictive digital twin applications integrate and analyze data from diverse 
sources to enhance their predictive capabilities?
From the reviewed studies, the integration and analysis of data from diverse sources for 
predictive digital twin platforms primarily focuses on three main challenges: integration, 
execution, and monitoring. As depicted in Table 5, research on data integration emerged 
most prominently during the initial database search, highlighting the critical need for 


---

Page 15

---

Page 15 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
	
effective methods due to the heavy reliance of digital twin platforms on data from multi-
ple sources to build accurate and comprehensive models. The integration of heterogene-
ous data is essential for enabling a functional platform (Correia et al. 2023). Regarding 
execution, advancements in computational power have facilitated efficient model analy-
sis. However, the majority of reviewed studies concentrate on methods such as feature 
selection and dimensionality reduction to manage large datasets (Qi et al. 2021). Real-
time monitoring of digital twin platforms enables proactive decision-making and accu-
rate forecasting, which are crucial for real-world applications. As indicated in Table 5, 
Table 4  Summary of different methodologies for Integrating and analyzing data from diverse 
sources
Management of data from multiple sources
Commonly employed techniques
Data integration
Data Collection: IoT devices, Databases, API Data Cleaning: 
Missing Values and Duplicate Removal, Outlier Detection Data 
Transformation: Normalization, Discretization Data Alignment: 
Time Series Alignment, Event Synchronization, Georeferencing, 
Data Fusion: Kalman Filter, Ensemble Methods
Feature selection and dimensionality reduction
Feature Selection: Filters, Wrappers Dimensionality Reduction: 
PCA, T-distributed Stochastic Neighbor Embedding
Real time monitoring
SCADA, Anomaly Detection, Predictive Maintenance, Environ‑
ment Variable Monitoring, Reactive Control, Continuous 
Learning
Table 5  Primary studies related to research question 2
Management of data from multiple 
sources
Number of studies 
from initial database 
search
Selected studies
Data integration
82
Zhang and Qu (2021), Minerva et al. 
(2020), Jacoby and Usländer (2020), Kaur 
et al. (2020), Platenius-Mohr et al. (2020), 
Bonney et al. (2022), Xu et al. (2019), Ben‑
zon et al. (2022), Alasadi and Bhaya (2017), 
García et al. (2016), Lv et al. (2020), Liu 
et al. (2023), Nguyen et al. (2013), Mei et al. 
(2020), Mohamed et al. (2023), Booshehri 
et al. (2021), Sharma and Balachandra 
(2019), Yue et al. (2024), Majidi Nezhad 
et al. (2019), Ma et al. (2024), Lio et al. 
(2021), da Silva et al. (2021)
Feature selection and dimensionality 
reduction
41
Marti-Puig et al. (2019), Qadir et al. (2021), 
Liu and Chen (2019), de Sá et al. (2020), Mir 
et al. (2020), Deng et al. (2021), Wang et al. 
(2020), Gu et al. (2019), Kong et al. (2015), 
Shen et al. (2019), Khan et al. (2019), 
Kouadri et al. (2020)
Real time monitoring
57
He et al. (2022), Chakraborty et al. (2023), 
Maldonado-Correa et al. (2020), Gonzalez 
et al. (2019), Xiang et al. (2022), Morrison 
et al. (2022), Hsu et al. (2020), Wang et al. 
(2020), Shin et al. (2021), van Dinter et al. 
(2022), Falekas and Karlis (2021), Zhong 
et al. (2023), Lio et al. (2021), Chen et al. 
(2019), Moness and Moustafa (2020), Tu 
et al. (2022), Fernandez-Gauna et al. (2022), 
Yang et al. (2019), Zhao et al. (2020), He 
et al. (2021)


---

Page 16

---

Page 16 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
monitoring represents the second most studied aspect in the literature (Correia et al. 
2023). The commonly employed techniques and methods are summarized in Table 4.
Data integration
Data is one of the key elements for predictive digital twin platforms. Integrating data 
from diverse sources into the digital twin platform requires several processes (Zhang 
and Qu 2021). The first step is identifying relevant data sources, which can include IoT 
devices, sensors, databases, external application programming interfaces, or historical 
trends (Minerva et al. 2020; Jacoby and Usländer 2020; Kaur et al. 2020; Platenius-Mohr 
et al. 2020). Each data source may have its own structure, including structured data from 
SQL databases, unstructured text files and images, or semi-structured data from various 
application programming interfaces (Bonney et al. 2022; Xu et al. 2019; Benzon et al. 
2022).
These collected data need to go through cleaning and transformation methods to 
be useful and meaningful for further analysis. Data cleaning techniques address miss-
ing values, duplicates, outlier detection, and inconsistencies within the dataset (Alasadi 
and Bhaya 2017). Transformation methods may include normalization, discretization, 
and dimensionality reduction (García et al. 2016).1 After preprocessing the data with 
cleaning and transformation methods, the data from different schemas and structures 
need to be aligned to have a unified format (Lv et al. 2020; Liu et al. 2023; Nguyen et al. 
2013). Schema matching algorithms and ontology alignment enable the reconciliation 
of data schemas and types from diverse sources (Mei et al. 2020; Mohamed et al. 2023; 
Booshehri et al. 2021).
The different sources may provide temporal and spatial data. The alignment of these 
data is essential for reliable operation. Temporal alignment methods, such as time 
series alignment or event synchronization, ensure consistency across time-stamped 
data streams (Sharma and Balachandra 2019; Yue et al. 2024). On the other hand, spa-
tial alignment techniques may include georeferencing or coordinate transformation for 
integrating geospatial data (Majidi Nezhad et al. 2019; Ma et al. 2024). As the data are 
aligned and synchronized, data fusion algorithms, such as Kalman filters or ensemble 
methods, can fuse information from diverse sources while considering uncertainties (Lio 
et al. 2021; da Silva et al. 2021).
Feature selection and dimensionality reduction
Enhancing the predictive capabilities of digital twin platforms, dimensionality reduc-
tion and feature selection are two important aspects to focus on the most relevant and 
informative features with the minimum data complexity. In digital twin applications, 
large amounts of data are necessary for reliable operation. These data include several 
input features, causing overfitting, an increase in model complexity, more computational 
resources, and decreased interpretability (Marti-Puig et al. 2019). Feature selection tar-
gets finding the most relevant subset of features to predict the target variables (Qadir 
et al. 2021). Filter and wrapper approaches are some commonly used frameworks. Filter 
1  The study published before 2019.


---

Page 17

---

Page 17 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
	
methods assess the relevance of the features independently of the predictive model, 
whereas wrapper methods evaluate different combinations of features, yielding slower 
but more precise results (Liu and Chen 2019; de Sá et al. 2020). In wind forecasting algo-
rithms, feature selection methods are deployed for comprehensive results with mini-
mum computational resource demand (Mir et al. 2020).
Similarly, dimensionality reduction aims to reduce the number of input dimensions 
while retaining essential information. Principal component analysis (PCA) is a technique 
that projects high-dimensional data onto a lower-dimensional subspace defined by prin-
cipal components. These components are then used in data-driven algorithms in wind 
energy systems (Deng et al. 2021; Wang et al. 2020; Gu et al. 2019; Kong et al. 2015). 
T-distributed stochastic neighbor embedding is a nonlinear dimensionality reduction 
technique that preserves the local structure of the data in a lower-dimensional space. 
In wind energy systems, T-distributed stochastic neighbor embedding is used to reduce 
the dimensionality of data clusters to identify patterns (Shen et al. 2019; Khan et al. 2019; 
Kouadri et al. 2020).
Real time monitoring
Efficient utilization of wind power depends on the real-time monitoring and optimiza-
tion of turbine performance. Critical parameters like rotor speed, power output, and 
component temperature must be continuously monitored (He et al. 2022; Chakraborty 
et al. 2023). Supervisory control and data acquisition (SCADA) systems are commonly 
used technologies that interface with the turbines. The knowledge gained from such 
tools in real-time monitoring can be further implemented into the digital twin platform 
to increase predictive capabilities (Maldonado-Correa et al. 2020; Gonzalez et al. 2019). 
Another important aspect of real-time data analysis techniques is to detect anomalies 
in turbine performance, which can address potential component failures (Xiang et al. 
2022; Morrison et al. 2022). Advancements in these techniques can evolve into predic-
tive maintenance to predict the needs of individual components. By integrating subsys-
tem models and real-time environment and turbine parameters, potential issues can be 
addressed, allowing proactive maintenance planning (Hsu et al. 2020; Wang et al. 2020; 
Shin et al. 2021). Several ongoing studies specifically focus on these areas, where meth-
ods and enabling technologies can be transferred to wind energy systems (van Dinter 
et al. 2022; Falekas and Karlis 2021; Zhong et al. 2023).
Real-time monitoring also plays a vital role in assessing wind resources. Continuous 
monitoring of wind speed, direction, and other meteorological data enables the assessment 
of available wind resources in real-time (Lio et al. 2021). With the methods mentioned in 
"Data integration" Section, integrating various types of data with the meteorological models 
built into the digital twin enables more precise wind forecasts. These forecast data can then 
be used to adjust turbine settings, such as yaw angles or pitch angles, to maximize energy 
production (Chen et al. 2019; Moness and Moustafa 2020; Tu et al. 2022). In study (Chen 
et al. 2019), a real-time feedback blade pitch control system is proposed for vertical axis 
wind turbines. To optimize the pitch angle of the blade, the suggested equation relies on 
real-time flow velocity, azimuth angle of the blade, and tip speed ratio. This real-time feed-
back pitch angle control system increases overall performance. Predictive digital twin appli-
cations can create a feedback loop, comparing predictions with actual outcomes to refine 


---

Page 18

---

Page 18 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
models iteratively. This continuous learning process enhances the predictive capabilities 
of the digital twin over time, enabling more accurate and reliable predictions (Fernandez-
Gauna et al. 2022; Yang et al. 2019). The technologies explained in "RQ3: What are the key 
features and technologies that facilitate real time wind energysystems through predictive 
digital twin?" Section enable the remote diagnosis of issues and implementation of control 
strategies in real-time from a centralized digital twin platform (Zhao et al. 2020; He et al. 
2021).
Fig. 4  Real-time operation facilitating features and technologies
Table 6  Primary studies related to research question 3
Key features and technologies
Number of studies 
from initial database 
search
Selected studies
IoT Sensors and Data Acquisition
49
Li et al. (2023), Wang et al. (2023), Liew et al. 
(2020), Karad and Thakur (2021), Guo et al. 
(2022), Dimitrov et al. (2019), Yang et al. 
(2020), Silva et al. (2023)
Communication Networks
64
Zheng et al. (2019), Haghshenas et al. 
(2023), Sasikala et al. (2021), Fahim et al. 
(2022), Isto et al. (2020), Nguyen et al. 
(2021), Farkas et al. (2018), Wu et al. (2021), 
Mashaly (2021), Mccarty et al. (2023), Liu 
et al. (2020)
Edge Computing and Cloud Computing 32
Saad et al. (2020), Hungud and Arunacha‑
lam (2020), Li et al. (2021), Fahim et al. 
(2022), Olatunji et al. (2021), Zhang et al. 
(2022)
Human Machine Interface
55
Kumar and Lee (2022), Qin et al. (2020), 
Evergreen (2020), Kandemir et al. (2023), 
Haghshenas et al. (2023), Stadtmann et al. 
(2023), Lalik and Watorek (2021), Kilimann 
et al. (2019), Erdei et al. (2022), Kaarlela et al. 
(2020), Bucchiarone (2022)


---

Page 19

---

Page 19 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
	
RQ3: What are the key features and technologies that facilitate real time wind energy 
systems through predictive digital twin?
Real-time wind energy systems are important for optimizing wind farm performance. 
By integrating advanced technologies, real-time operating platforms facilitate decision-
making processes. To identify the key features and technologies that enhance real-time 
wind energy systems through predictive digital twins, a comprehensive literature review 
was conducted, primarily focusing on academic journals and conference papers on digi-
tal twins and wind energy systems. The technologies were evaluated based on their rel-
evance, impact on real-time monitoring and prediction, as well as overall contribution 
to system efficiency (Stadtmann et al. 2023; Qi et al. 2021). Figure 4 summarizes the key 
features and technologies enabling real-time operations.
IoT sensors for data acquisition
In the complex landscape of the wind energy systems, Internet of Things sensors are one 
of the important components, facilitating the collection of essential data for optimum 
performance and informed operation. These sensors are positioned across wind turbines 
and the operating environment to monitor several vital parameters, providing operators 
insights into operational conditions (Li et al. 2023; Wang et al. 2023; Liew et al. 2020).
Advanced multi-sensor platforms are employed in wind energy systems to capture a 
diverse range of data. These sensors encompass various technologies, such as anemom-
eters for wind speed and direction, thermocouples for temperature monitoring, humid-
ity sensors for atmospheric moisture levels, accelerometers for vibration analysis, and 
power meters for electrical output measurement (Karad and Thakur 2021). Additionally, 
Table 7  Primary studies related to research question 4
Common challenges
Number of studies 
from initial database 
search
Selected studies
Data Quality Assurance
31
Avanzini and Eriksson (2021), Eriksson and Markussen 
(2023), Ward et al. (2021), Koo and Yoon (2024), Mogh‑
adam and Nejad (2022), Chen et al. (2021), Adedipe et al. 
(2020), Hirvoas et al. (2021), Hung et al. (2022)
Model Complexity and 
Model Order Reduction
73
Taira et al. (2020), Siddiqui et al. (2019), Andersen and 
Murcia Leon (2022), Liang et al. (2023), Zhao et al. (2023), 
Gözcü and Dou (2020), Sayed et al. (2019), Grinderslev 
et al. (2021), Liu et al. (2019), Michalakes (2020), Veers et al. 
(2023), Kumar and Ezhilarasi (2023), Siddiqui et al. (2020), 
Premaratne et al. (2022), Zhao et al. (2021), Lin et al. (2020), 
Bui (2023), Morovati et al. (2021), Al-Iedani and Gajic 
(2020), Wu et al. (2021), Zhang et al. (2022), Ali and Cal 
(2020), Siddiqui et al. (2020), Tabib et al. (2022)
Validation and Calibration 45
Pimenta et al. (2020), Jonscher et al. (2022), Lee and Fields 
(2021), Bergua et al. (2023), Vahidi and Porté-Agel (2022), 
Wang et al. (2022), Valikhani et al. (2024), Hirvoas et al. 
(2022), Sousa and Gorlé (2019), Poterjoy (2022), Han et al. 
(2020), Schwegmann et al. (2023), Habibi et al. (2019), Liu 
et al. (2021), Rajpoot et al. (2021), Hur (2019), Cho et al. 
(2021), Petrović et al. (2021), Collet et al. (2021), Mahmoud 
and Oyedeji (2019), Ghareveran and Yazdizadeh (2019), 
Wang et al. (2022), Barhate et al. (2024), Saenz-Aguirre 
et al. (2020), Xie et al. (2023), Saenz-Aguirre et al. (2019)


---

Page 20

---

Page 20 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
emerging technologies like Light Detection and Ranging and Sonic Detection and Rang-
ing support precise wind profiling and turbulence detection. Light Detection and Rang-
ing allows for the detection of turbulent wind before it negatively influences turbine 
performance, thus optimizing energy production (Guo et al. 2022; Dimitrov et al. 2019). 
On the other hand, Sodar provides advantages in measuring the wind profile at different 
altitudes and supporting the anemometers mounted on wind turbines (Yang et al. 2020; 
Silva et al. 2023).
Communication networks
Communication networks in wind energy systems should be designed to ensure reliable 
transfer so that the collected sensor data can be used for comprehensive analysis (Zheng 
et  al. 2019). Advanced standardized communication protocols such as MQTT and 
OPC UA allow sensor data to be transmitted efficiently and securely. Depending on 
the requirements, centralized control systems or cloud-based platforms are possible 
solutions(Haghshenas et al. 2023; Sasikala et al. 2021). These protocols enable reliable 
data transmission over various network infrastructures, facilitating access to critical 
operational insights.
Low-latency communication networks are essential for data transmission between 
operating subsystems and the central control system. Technologies like 5 G (fifth-gener-
ation cellular network technology) or the standards like time-sensitive networking prior-
itize the reduction of latency problems (Fahim et al. 2022; Isto et al. 2020; Nguyen et al. 
2021; Farkas et al. 2018). In study (Isto et al. 2020), the focus is on 5 G networks for digi-
tal twin applications in remote machinery control systems. Two application scenarios 
are demonstrated: video feedback and haptic feedback. Compared to LTE (Long-Term 
Evolution), lower delay and jitter are observed in both cases. Wind turbines generate 
large volumes of data, including sensor readings, environmental parameters, and perfor-
mance metrics. High-bandwidth communication networks, such as fiber-optic cables or 
high-speed wireless links, are essential for efficiently transmitting this data to predictive 
digital twin systems for analysis (Wu et al. 2021; Mashaly 2021). Security is another criti-
cal aspect of communication networks. Encryption protocols are employed to safeguard 
data integrity and protect against cyber threats, ensuring the confidentiality and security 
of sensitive information (Mccarty et al. 2023; Liu et al. 2020).
Edge computing and cloud computing
Edge computing enables data acquisition through sensors and IoT devices, as discussed 
in "IoT sensors for data acquisition" Section. Although edge devices often have limited 
computational power, they can still be useful for local processing. These computational 
sources can be programmed to support the predictive models implemented in the digital 
twin platform. Through edge computing platforms like NVIDIA Jetson or Intel Movid-
ius, rapid adjustments can be made based on insights from analytics, thereby achiev-
ing optimum performance parameters more quickly  (Saad et  al. 2020; Hungud and 
Arunachalam 2020; Li et al. 2021).
On the other hand, cloud computing provides scalability through platforms capable of 
processing large amounts of data and performance parameters. These powerful frame-
works support big data analytics for in depth trend analysis, enhancing the performance 


---

Page 21

---

Page 21 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
	
of predictive models dynamically. The dynamic update of predictive models supports 
long-term optimization. Integrating edge devices allows centralized management and 
condition monitoring of wind energy platforms, providing comprehensive insights for 
stakeholders (Fahim et al. 2022; Olatunji et al. 2021; Zhang et al. 2022).
Human machine interface
The human–machine interface (HMI) is one of the essential features enabling seamless 
real time operation. This technology focuses on the interaction between human opera-
tors and complex systems (Kumar and Lee 2022). The interface should provide intui-
tive visualization of real time data along with trends and future predictions. These data 
enable predictive analytics and provide a comprehensive view of system status. Visual 
elements may vary from simple charts to 3D models (Qin et al. 2020; Evergreen 2020). 
Some commonly used libraries and applications include WebGL, Plotly, and Unity (Kan-
demir et al. 2023; Haghshenas et al. 2023). These programs may incorporate interactive 
control panels where operators can adjust turbine settings or monitor performance. The 
selection of the required interaction should be planned according to operational condi-
tions. Touchscreens, augmented reality, or other virtual controls allow for intuitive inter-
action with quick adaptability to a changing environment (Stadtmann et al. 2023; Lalik 
and Watorek 2021; Kilimann et al. 2019).
The human–machine interface, combined with decision support systems based on 
predictive insights, provides operators with contextual information and recommenda-
tions for decision-making. Another important role of the human–machine interface is 
to enable operational training as a support tool for new operators. Interactive tutorials, 
help menus, and troubleshooting guides assist operators in adapting to optimum operat-
ing conditions (Erdei et al. 2022; Kaarlela et al. 2020; Bucchiarone 2022).
RQ4: What are the challenges commonly encountered in wind energy systems 
when implementing predictive digital twin solutions?
The integration of predictive digital twin solutions in wind energy systems enhances 
efficiency and reliability through advanced analytics. However, implementing these 
solutions comes with significant challenges that need to be addressed to realize their 
potential. Several review papers identify the most common key challenges in this 
domain, including data quality assurance, model complexity, model order reduction, val-
idation, and calibration. These challenges are categorized based on their impact on the 
development, deployment, and execution of predictive digital twin solutions (Rodríguez 
et al. 2023; Hartmann et al. 2018; Liu et al. 2021).
Data quality assurance
Data quality assurance is a critical aspect of predictive digital twin platforms. High-
quality data enables improved predictive accuracy, effective condition monitoring, and 
higher economic viability (Avanzini and Eriksson 2021; Eriksson and Markussen 2023). 
However, maintaining high-quality data presents several challenges, including manag-
ing complex data from diverse sources, addressing sensor reliability issues, quantifying 
uncertainty, and resolving data completeness problems.


---

Page 22

---

Page 22 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
The acquisition of reliable data from heterogeneous sensors and IoT devices requires 
continuous sensor calibration. In digital twin platforms, implementing periodic calibra-
tion algorithms is necessary to prevent inaccurate data (Ward et al. 2021; Koo and Yoon 
2024). The uncertainties in a digital twin platform may originate from various sources, 
including measurement errors, variations in wind properties, and operational param-
eters such as rotor speed within the models. Techniques like Monte Carlo simulation 
and Bayesian inference are commonly used to quantify the magnitude and distribution 
of these uncertainties (Moghadam and Nejad 2022; Chen et al. 2021; Adedipe et al. 2020; 
Hirvoas et  al. 2021). In the event of network failures or sensor malfunctions, imple-
mented failover mechanisms ensure continuous data availability (Hung et al. 2022).
Model complexity and model order reduction
In predictive digital twin platforms for wind energy systems, sophisticated models 
introduce significant computational challenges. High-fidelity models can capture com-
plex interactions and nonlinear behavior within and between wind turbines, but they 
demand substantial computational resources for large scale simulations. To address this 
issue, model order reduction techniques can achieve reliable predictive capabilities while 
reducing the need for extensive computational resources. However, these techniques 
also require validation with high-fidelity models (Taira et al. 2020).
Modelling types are discussed in "IoT sensors for data acquisition" Section. In physics-
based modelling, computational fluid models are used to simulate the airflow around 
turbine blades, aiming to capture several effects such as fluid flow or wake forma-
tion (Siddiqui et al. 2019; Andersen and Murcia Leon 2022). For detailed analysis, these 
high-resolution models are required with intensive processing power. Similarly, in the 
structural dynamics of the components, finite element analysis is used to comprehend 
deformation or failure points under different loading conditions (Liang et al. 2023; Zhao 
et al. 2023; Gözcü and Dou 2020). Moreover, these two models may require coupled 
simulation to understand the interaction between aerodynamic forces and structural 
responses (fluid structure interaction), which becomes more computationally inten-
sive (Sayed et al. 2019; Grinderslev et al. 2021; Liu et al. 2019). On the other hand, sto-
chastic elements are necessary to achieve a realistic environmental simulation. Methods 
mentioned in "Data quality assurance" Section  may address this issue with an additional 
computational cost. To address these temporal and spatial resolution challenges, some 
possible solutions are utilizing high-performance computing resources, using efficient 
data handling systems, or adapting model order reduction techniques (Michalakes 2020; 
Veers et al. 2023).
There are several model order reduction techniques that can be adapted depending 
on the application (Kumar and Ezhilarasi 2023). Proper orthogonal decomposition is a 
technique, which identifies significant modes by decomposing the system into orthogo-
nal modes. This method can be utilized for analyzing wake dynamics, velocity fields or 
structure dynamics (Siddiqui et al. 2020; Premaratne et al. 2022; Zhao et al. 2021). Simi-
larly, the balanced truncation approach, used in linear time-invariant systems, seeks to 
achieve a balance between controllability and observability while reducing the states (Lin 
et al. 2020). This method is useful in the modeling and control design of systems (Bui 
2023; Morovati et al. 2021; Al-Iedani and Gajic 2020). Data-driven reduced order models 


---

Page 23

---

Page 23 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
	
include techniques inherited from deep learning algorithms, which can model nonlinear 
turbine aerodynamics, wind turbine interactions, and unsteady fluid–structure interac-
tions with reliable predictive capability and less demanding computational resources. 
Some commonly used algorithms in these models are CNN, LSTM, and ANN. These 
data-driven reduced order models can be combined with different methods, enabling 
hybrid models for enhanced performance and accuracy (Wu et al. 2021; Zhang et al. 
2022; Ali and Cal 2020; Siddiqui et al. 2020; Tabib et al. 2022).
Validation and calibration
Continuous calibration and validation of models and sensors on a predictive digital twin 
platform are crucial to ensure accurate and reliable platforms under real environmental 
conditions (Pimenta et al. 2020; Jonscher et al. 2022; Lee and Fields 2021; Bergua et al. 
2023). However, several challenges need to be considered in this context. Addressing 
limited historical data, ensuring sensor reliability, and dynamically adapting to varying 
conditions pose significant challenges.
In newly deployed digital twin platforms, historical data might be scarce, limiting the 
ability to validate model performance. Collecting data from the system and operating 
environment takes time. However, to overcome such challenges, physics-based models 
explained in "Physics based modeling" Section  can be useful for simulating the dynam-
ics in question (Vahidi and Porté-Agel 2022; Wang et al. 2022). The generated synthetic 
data can then be used for calibration in the initial phase. Bayesian inference techniques 
can be coupled with data assimilation methods to integrate synthetic data generated 
from physics-based models. This approach enhances the predictive capabilities of the 
model with new, unforeseen data (Valikhani et al. 2024; Hirvoas et al. 2022; Sousa and 
Gorlé 2019; Poterjoy 2022).
The data collected from sensors plays a key role in the predictive capabilities of digi-
tal twin platforms. However, these sensors may experience calibration drift over time 
due to environmental factors and mechanical wear. Therefore, it is necessary to employ 
advanced calibration techniques, such as periodic sensor recalibration, to ensure data 
accuracy  (Han et  al. 2020; Schwegmann et  al. 2023). Additionally, model-based fault 
detection and isolation algorithms, such as observer-based approaches, can be utilized 
to detect sensor anomalies and correct measurements (Habibi et al. 2019; Liu et al. 2021; 
Rajpoot et al. 2021). Kalman filters with different variations or deep learning algorithms 
can further enhance data reliability based on the system dynamics (Hur 2019; Cho et al. 
2021).
Dynamic system adaptation methods can be integrated into digital twin platforms 
to address validation and calibration issues. Implementing advanced control-oriented 
techniques such as model predictive control or adaptive robust control can calibrate the 
platform to replicate the dynamic behavior of adaptive control systems (Petrović et al. 
2021; Collet et al. 2021; Mahmoud and Oyedeji 2019). Additionally, parameter estima-
tion techniques such as least squares, extended Kalman filter, or sparse identification of 
nonlinear dynamics (SINDy) can be used to update the model parameters based on real-
time sensor feedback under dynamic operating conditions (Ghareveran and Yazdizadeh 
2019; Wang et al. 2022; Barhate et al. 2024). In this regard, data-driven approaches like 


---

Page 24

---

Page 24 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
reinforcement learning or neural networks can adaptively calibrate the system based on 
observed behaviors (Saenz-Aguirre et al. 2020; Xie et al. 2023; Saenz-Aguirre et al. 2019).
Discussion
This section provides a deeper analysis of the most recent trends, methods, and chal-
lenges in predictive digital twin platforms for wind energy systems. The current state of 
this field is examined through four main discussion points, which target common meth-
odologies, integration and analysis of various data sources, key features and technolo-
gies, and encountered challenges.
Commonly employed methodologies are handled in three main groups: physics-based 
modeling, data-driven approaches, and hybrid models. In physics-based modeling, the 
primary research areas include the mechanical behavior of turbine components, aer-
oelastic effects, and material properties. This research can extend to offshore wind tur-
bine structures, investigating materials under such conditions and the effects of surface 
waves and ocean currents on structural dynamics. In aerodynamic models, numerical 
analysis in fluid flow problems has a solid foundation. Similarly, the aeroelastic effect on 
aerodynamic characteristics and dynamic inflow can be investigated further for better 
energy efficiency in wind farms. In terms of electrical models, grid integration is attract-
ing attention due to the implementation of new renewable resources. Control models 
mainly focus on three aspects: pitch control, yaw control, and predictive maintenance. 
Predictive maintenance with fault detection algorithms is popular in different fields, and 
there is potential to adapt these technologies for wind energy systems.
In data-driven approaches, regression models, machine learning algorithms, and 
statistical methods are implemented in studies. Regression models are used to relate 
dependent variables with independent variables. Among data-driven approaches, 
machine learning algorithms represent the most popular research area, offering a vari-
ety of algorithm types. These models can capture nonlinear temporal and spatial fea-
tures quite well; however, many of them lack interpretability. To enhance the capabilities 
of machine learning algorithms, statistical models are incorporated to obtain reliable 
patterns.
Hybrid models are among the most popular algorithms in predictive digital twin plat-
forms for wind energy systems. For hybrid forecasting models, most research focuses 
on varying time intervals for wind speed forecasting, essential for operational planning, 
grid stability, and maintenance scheduling. In terms of fluid dynamics, hybrid models 
find popular applications in optimizing blade shapes using high-fidelity models, inves-
tigating, and mitigating real-time wake effects, as well as adapting control for pitch 
and yaw angles. Regarding structural models, common research areas include predic-
tive maintenance based on structural health monitoring data, in cooperation with early 
warning systems for structural failures. Additionally, fatigue and load-bearing capac-
ity during the design phase are two popular areas for structural optimization. One of 
the most significant developments in both structural and aerodynamics hybrid mod-
els is physics-informed neural networks, enabling the embedding of partial differential 
equations governing the physics laws into neural networks. This enables the investiga-
tion of complex flow patterns or structural responses with different material properties 
and conservation laws. Hybrid predictive maintenance models are another common 


---

Page 25

---

Page 25 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
	
implementation in predictive digital twin platforms. Estimating the remaining useful 
life with hybrid models is popular in various fields, with ongoing research, especially in 
wind turbines, through vibration and thermal analysis. With the increasing popularity 
of renewable energy systems, grid integration becomes an important field of research 
to enhance grid stability by aligning wind power generation with real-time demand 
forecasts.
Integrating data from diverse sources for analysis and improving predictive capabili-
ties requires significant attention. Current studies show that integrating data from differ-
ent sources and structuring these data in a comprehensible way is a trending area. Data 
preprocessing techniques are well established; however, there is still a need for research 
in unsupervised algorithms for processing data. Due to the intensity of multiple sensors, 
reliable frameworks and protocols with alignment methods are necessary. Continuous 
real-time monitoring is crucial for reliable predictive models, as it enables continuous 
learning to iteratively increase model accuracy. However, real-time monitoring requires 
models that maintain essential information. Therefore, feature selection methods are 
used to capture the necessary input, while dimensionality reduction can reduce the 
number of input dimensions.
Communication protocols such as MQTT and OPC UA are commonly employed for 
efficient and secure data transmission. Many studies focus on reducing latency in com-
munication networks due to the need for time-sensitive networking in predictive digital 
twin platforms. These technologies enable cloud computing with large amounts of data. 
Transferring confidential data through these technologies requires secure encryption 
protocols to ensure secure operation. Relying on these data, human–machine interface 
modules can be developed. As part of a digital twin platform, interaction with systems 
through different means is essential for awareness and adapting to optimal conditions.
Data quality assurance is one of the challenges in digital twin platforms due to sev-
eral heterogeneous data from different sensors and databases, which are associated with 
uncertainties. There is attention on continuous sensor calibration to eliminate errors. 
Also, with probabilistic simulations and ensemble methods, the inherited uncertainties 
within the models can be quantified. Another challenge is model complexity due to high-
fidelity modeling, which is in disfavor in real-time operation. In recent studies, the focus 
is on model order reduction techniques to overcome the model complexity problems. 
Utilizing hybrid models in reduced-order models is a trending approach. Another chal-
lenge is model validation and calibration. To overcome this issue, a combination of his-
torical data and the collected sensor data is mainly used with different type algorithms.
Despite the analysis provided in this study, several limitations need to be addressed 
to ensure an objective approach to predictive digital twin platforms for wind energy 
systems.
Physics-based, data-driven, and hybrid models introduce inherent biases associated 
with each methodology. For instance, physics-based models may provide robust and 
repeatable results in simulating mechanical behaviors and aerodynamic characteris-
tics; however, they often rely on idealized assumptions, lacking real-world complexities. 
Data-driven approaches, particularly deep learning algorithms, can identify complex 
patterns, but as mentioned earlier in the text, they suffer from a lack of interpretabil-
ity. Moreover, data-driven approaches are highly sensitive to the quality of training data. 


---

Page 26

---

Page 26 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
Hybrid models attempt to combine the strengths of these two methods, but they often 
inherit the limitations of both methodologies, leading to potential overfitting and com-
putational inefficiencies.
The integration of heterogeneous data sources is a critical challenge that impacts 
the reliability of predictive models. Despite advances in data processing and alignment 
methods, the quality of data from diverse sources remains a significant concern. Sen-
sor calibration errors, data transmission latency, and inconsistencies in data formats can 
introduce significant issues such as noise or biases. Furthermore, this study emphasizes 
the need for real-time monitoring and continuous learning, which necessitates robust 
data quality assurance mechanisms. However, the implementation of such mechanisms 
brings several challenges, such as handling missing or corrupted data points. High-fidel-
ity models often result in high computational demands, making real-time application 
challenging. Model order reduction techniques may lead to the loss of critical details 
necessary for precise predictions. In the context of offshore wind turbines, these limita-
tions introduce additional layers of complexity.
Quantifying uncertainties within predictive models remains a critical challenge. 
Probabilistic simulations and ensemble methods offer potential solutions, but they also 
introduce computational complexity and demand high-quality data. The scalability of 
the different models in wind energy systems and varying geographic locations is another 
limitation. Most studies focus on specific case studies under controlled environments, 
which may not be generalizable to other settings. For example, the performance of pre-
dictive maintenance algorithms developed for onshore turbines may differ when applied 
to offshore turbines due to different operational conditions. This study falls short of pro-
viding comprehensive strategies for managing uncertainties and dealing with the scal-
ability of the methods.
In this study’s meta-analysis, it is observed that the current trend in predictive digi-
tal twin platforms for wind energy systems involves the attempt to overcome inherited 
challenges with hybrid models. Additionally, the trend in model development primar-
ily consists of combining various models, incorporating both physics-based models and 
machine learning algorithms for better accuracy and interpretability.
Conclusions and future work
In conclusion, the literature review on predictive digital twins for wind energy systems 
highlights the significant potential in the renewable energy sector. Key findings from 
the literature indicate that predictive digital twins can be leveraged by various modeling 
types, including inherited methods from physics and machine learning algorithms. This 
capability allows for identification of potential failures, enhanced predictive capabilities, 
and informed decision-making processes. However, the successful implementation of 
predictive digital twins in wind energy systems requires overcoming several challenges. 
These include the need for:
•	 High-fidelity data acquisition to ensure that data are collected precisely and accu-
rately for comprehensive analysis. These data enable the training of models to sup-
port reliable decision making.


---

Page 27

---

Page 27 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
	
•	 Standardized, reliable communication networks to align with industry standards, facili-
tating secure data exchange and interoperability.
•	 Integration of diverse data sources, such as sensors, IoTs, historical databases, and exter-
nal APIs, into a unified system to create a comprehensive view. This process requires 
methods such as data normalization and synchronization.
•	 Addressing cybersecurity concerns to protect the integrity and confidentiality of the 
data involved.
•	 Improving human–machine interface issues to ensure that the insights generated by 
predictive digital twins are effectively perceived by operators and decision-makers.
Future research should focus on enhancing the precision and reliability of predictive mod-
els by exploring hybrid approaches that combine physical and data-driven techniques. For 
instance, integrating finite element analysis with deep learning neural networks could sig-
nificantly strengthen model capabilities. Developing methodologies to quantify and reduce 
uncertainties is essential for reliable operations. Leveraging techniques such as Bayesian 
inference and Monte Carlo simulations can facilitate robust predictive analysis. Incorpo-
rating diverse data sources, including historical trends and real-time environmental inputs, 
alongside pure sensor data, will improve model capabilities. Additionally, scalability and 
adaptability of predictive digital twin models across various systems and industries are 
crucial. This involves reviewing data compatibility, modularity, and interoperability. Com-
mon Data Models (CDM) and data lakes can help address compatibility and integration 
challenges. Moreover, focusing on APIs and middleware software will enable better data 
exchange.
Overall, predictive digital twins stand as a promising technology in the wind energy sec-
tor, which facilitates a shift towards greater sustainability. Continued innovation in this area 
will support the goal of achieving global renewable energy targets aligned with the United 
Nations Sustainable Development Goals.
Author contributions
E.K. Prepared the document, including research, writing, and drafts. A.H. Revised the document and suggested additional 
references T.K. Revised the document and suggested additional references S.A. Revised the document and suggested 
additional references.
Funding
Open access funding provided by NTNU Norwegian University of Science and Technology (incl St. Olavs Hospital - Trond‑
heim University Hospital). No external funding.
Availability of data and materials
No datasets were generated or analysed during the current study.
Declarations
Ethics approval and consent to participate
Not applicable
Consent for publication
Not applicable
Competing interests
The authors declare that they have no competing interests.
Received: 8 June 2024   Accepted: 31 July 2024


---

Page 28

---

Page 28 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
References
Adedipe T, Shafiee M, Zio E (2020) Bayesian network modelling for the wind energy industry: an overview. Reliab Eng 
Syst Safety 202:107053
Akbari R, Izadian A, Weissbach R (2019) An approach in torque control of hydraulic wind turbine powertrains. In: 2019 
IEEE Energy Conversion Congress and Exposition (ECCE). 979–982
Al-Iedani I, Gajic Z (2020) Order reduction of a wind turbine energy system via the methods of system balancing and 
singular perturbations. Int J Electr Power Energy Syst 117:105642
Alasadi SA, Bhaya WS (2017) Review of data preprocessing techniques in data mining. J Eng Appl Sci 12(16):4102–4107
Alhussein M, Aurangzeb K, Haider SI (2020) Hybrid CNN-LSTM model for short-term individual household load forecast‑
ing. IEEE Access 8:180544–180557
Ali N, Cal RB (2020) Data-driven modeling of the wake behind a wind turbine array. J Renew Sustain Energy 12(3):033304
Aly HHH (2020) An intelligent hybrid model of neuro wavelet, time series and recurrent Kalman filter for wind speed 
forecasting. Sustain Energy Technol Assess 41:100802
Aly HHH (2020) A proposed intelligent short-term load forecasting hybrid models of ANN, WNN and KF based on cluster‑
ing techniques for smart grid. Electric Power Syst Res 182:106191
Andersen SJ, Murcia Leon JP (2022) Predictive and stochastic reduced-order modeling of wind turbine wake dynamics. 
Wind Energy Sci 7(5):2117–2133
Avanzini GB, Eriksson KE (2021) Quality Assurance Framework of Digital Twins for the Oil and Gas Industry. Offshore 
Mediterranean Conf Exhibit. 2021–157
Banik A, Behera C, Sarathkumar TV, Goswami AK (2020) Uncertain wind power forecasting using LSTM-based prediction 
interval. IET Renew Power Generat 14(14):2657–2667
Barhate SC, Siram O, Sahoo N (2024) Wake modelling of horizontal-axis wind turbines using sparse identification of non-
linear dynamics (SINDY). In: Ray RK, Bora SN, Maiti DK (eds) Adv Theoret Appl Mech. Springer, Singapore, pp 69–82
Barhmi S, Elfatni O, Belhaj I (2020) Forecasting of wind speed using multiple linear regression and artificial neural net‑
works. Energy Syst 11(4):935–946
Barhmi S, Fatni OE (2019) Hourly wind speed forecasting based on support vector machine and artificial neural networks. 
IAES Int J Artif Intell 8(3):286–291
Bashetty S, Guillamon JI, Mutnuri SS, Ozcelik S (2020) Design of a robust adaptive controller for the pitch and torque 
control of wind turbines. Energies 13(5):1195
Basit MA, Dilshad S, Badar R, Rehman SM (2020) Limitations, challenges, and solution approaches in grid-connected 
renewable energy systems. Int J Energy Res 44(6):4132–4162
Bazilevs Y, Korobenko A, Deng X, Yan J (2015) Novel structural modeling and mesh moving techniques for advanced 
fluid-structure interaction simulation of wind turbines. Int J Numerical Methods Eng 102(3–4):766–783
Benzon H-H, Chen X, Belcher L, Castro O, Branner K, Smit J (2022) An operational image-based digital twin for large-scale 
structures. Appl Sci 12(7):3216
Beretta M, Julian A, Sepulveda J, Cusidó J, Porro O (2021) An ensemble learning solution for predictive maintenance of 
wind turbines main bearing. Sensors 21(4):1512
Bergua R, Robertson A, Jonkman J, Branlard E, Fontanella A, Belloli M, Schito P, Zasso A, Persico G, Sanvito A, Amet E, Brun 
C, Campaña-Alonso G, Martín-San-Román R, Cai R, Cai J, Qian Q, Maoshi W, Beardsell A, Pirrung G, Ramos-García N, 
Shi W, Fu J, Corniglion R, Lovera A, Galván J, Nygaard TA, Santos CR, Gilbert P, Joulin P-A, Blondel F, Frickel E, Chen P, 
Hu Z, Boisard R, Yilmazlar K, Croce A, Harnois V, Zhang L, Li Y, Aristondo A, Mendikoa Alonso I, Mancini S, Boorsma 
K, Savenije F, Marten D, Soto-Valle R, Schulz CW, Netzband S, Bianchini A, Papi F, Cioni S, Trubat P, Alarcon D, Molins 
C, Cormier M, Brüker K, Lutz T, Xiao Q, Deng Z, Haudin F, Goveas A (2023) Oc6 project phase iii: validation of the 
aerodynamic loading on a wind turbine rotor undergoing large motion caused by a floating support structure. 
Wind Energy Sci 8(4):465–485
Bonney MS, Angelis M, Dal Borgo M, Andrade L, Beregi S, Jamia N, Wagg DJ (2022) Development of a digital twin opera‑
tional platform using python flask. Data-Centric Eng 3:1
Booshehri M, Emele L, Flügel S, Förster H, Frey J, Frey U, Glauer M, Hastings J, Hofmann C, Hoyer-Klick C, Hülk L, Kleinau 
A, Knosala K, Kotzur L, Kuckertz P, Mossakowski T, Muschner C, Neuhaus F, Pehl M, Robinius M, Sehn V, Stappel M 
(2021) Introducing the open energy ontology: enhancing data interpretation and interfacing in energy systems 
analysis. Energy AI 5:100074
Branlard E, Jonkman B, Pirrung GR, Dixon K, Jonkman J (2022) Dynamic inflow and unsteady aerodynamics models for 
modal and stability analyses in openfast. J Phys Conf Series 2265(3):032044
Buabeng A, Simons A, Frempong NK, Ziggah YY (2021) A novel hybrid predictive maintenance model based on cluster‑
ing, smote and multi-layer perceptron neural network optimised with grey wolf algorithm. SN Appl Sci 3(5):593
Bucchiarone A (2022) Gamification and virtual reality for digital twin learning and training: architecture and challenges. 
Virtual Real Intell Hardware 4(6):471–486
Bui HH (2023) Control design for the ward-Leonard system in wind turbines. Eng Technol Appl Sci Res 13(1):9968–9972
Cai S, Mao Z, Wang Z, Yin M, Karniadakis GE (2021) Physics-informed neural networks (PINNs) for fluid mechanics: a 
review. Acta Mechanica Sinica 37(12):1727–1738
Carneiro TC, Rocha PAC, Carvalho PCM, Fernández-Ramírez LM (2022) Ridge regression ensemble of machine learning 
models applied to solar and wind forecasting in Brazil and Spain. Appl Energy 314:118936
Chakraborty A, Dey D, Das P, Ray S (2023) Real-time monitoring of wind turbine performance using IoT technology to 
prevent potential disruptions. In: 2023 14th International Conference on Computing Communication and Net‑
working Technologies (ICCCNT). 1–6
Chen B, Hua X, Zhang Z, Nielsen SRK, Chen Z (2021) Active flutter control of the wind turbines using double-pitched 
blades. Renew Energy 163:2081–2097
Chen D, Wang D, Zhu Y, Han Z (2021) Digital twin for federated analytics using a Bayesian approach. IEEE Internet Things 
J 8(22):16301–16312
Chen L, Yang Y, Gao Y, Gao Z, Guo Y, Sun L (2019) A novel real-time feedback pitch angle control system for vertical-axis 
wind turbines. J Wind Eng Indust Aerodynam 195:104023


---

Page 29

---

Page 29 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
	
Cheng B, Yao Y (2022) Design and optimization of a novel u-type vertical axis wind turbine with response surface and 
machine learning methodology. Energy Convers Manag 273:116409
Cho S, Choi M, Gao Z, Moan T (2021) Fault detection and diagnosis of a blade pitch system in a floating wind turbine 
based on Kalman filters and artificial neural networks. Renew Energy 169:1–13
Choi S, Jung I, Kim H, Na J, Lee JM (2022) Physics-informed deep learning for data-driven solutions of computational fluid 
dynamics. Korean J Chem Eng 39(3):515–528
Collet D, Alamir M, Di Domenico D, Sabiron G (2021) Data-driven fatigue-oriented MPC applied to wind turbines indi‑
vidual pitch control. Renew Energy 170:1008–1019
Correia JB, Abel M, Becker K (2023) Data management in digital twins: a systematic literature review. Knowl Inform Syst 
65(8):3165–3196
da Silva RG, Ribeiro MHDM, Moreno SR, Mariani VC, Santos Coelho L (2021) A novel decomposition-ensemble learning 
framework for multi-step ahead wind energy forecasting. Energy 216:119174
Deng Y-C, Tang X-H, Zhou Z-Y, Yang Y, Niu F. Application of machine learning algorithms in wind power: a review. Energy 
Sour Part A Recovery Utilizat Environ Eff. 1–22
Dimitrov N, Borraccino A, Peña A, Natarajan A, Mann J (2019) Wind turbine load validation using lidar-based wind retriev‑
als. Wind Energy 22(11):1512–1533
Dong H, Xie J, Zhao X (2022) Wind farm control technologies: from classical control to reinforcement learning. Progress 
Energy 4(3):032006
Dong H, Zhang J, Zhao X (2021) Intelligent wind farm control via deep reinforcement learning and high-fidelity simula‑
tions. Appl Energy 292:116928
Du P, Wang J, Yang W, Niu T (2019) A novel hybrid model for short-term wind power forecasting. Appl Soft Comput 
80:93–106
Dupré A, Drobinski P, Alonzo B, Badosa J, Briard C, Plougonven R (2020) Sub-hourly forecasting of wind speed and wind 
energy. Renew Energy 145:2373–2379
Elsaraiti M, Merabet A (2021) A comparative analysis of the ARIMA and LSTM predictive models and their effectiveness for 
predicting wind speed. Energies 14(20):6782
Elyasichamazkoti F, Khajehpoor A (2021) Application of machine learning for wind energy from design to energy-water 
nexus: a survey. Energy Nexus 2:100011
Erdei TI, Krakó R, Husi G (2022) Design of a digital twin training centre for an industrial robot arm. Appl Sci 12(17):8862
Eriksson K, Markussen C (2023) Quality assurance of digital twins. Int Conf Offshore Mech Arctic Eng 86830:1
Evergreen SDH (2020) Effective data visualization: the right chart for the right data. SAGE, Los Angeles
Fahim M, Sharma V, Cao T-V, Canberk B, Duong TQ (2022) Machine learning-based digital twin for predictive modeling in 
wind turbines. IEEE Access 10:14184–14194
Fahrmeir L, Kneib T, Lang S, Marx BD (2021) Regression Models. Springer, Berlin, Heidelberg, pp 23–84
Falekas G, Karlis A (2021) Digital twin in electrical machine control and predictive maintenance: State-of-the-art and 
future prospects. Energies 14(18):5933
Farkas J, Bello LL, Gunther C (2018) Time-sensitive networking standards. IEEE Commun Standards Mag 2(2):20–21
Fernandez-Gauna B, Graña M, Osa-Amilibia J-L, Larrucea X (2022) Actor-critic continuous state reinforcement learning for 
wind-turbine control robust optimization. Inform Sci 591:365–380
Ferreira C, Yu W, Sala A, Viré A (2022) Dynamic inflow model for a floating horizontal axis wind turbine in surge motion. 
Wind Energy Sci 7(2):469–485
Fowdur TP, Beeharry Y, Hurbungs V, Bassoo V, Ramnarain-Seetohul V (2018) Big data analytics with machine learning tools. 
Springer, Cham, pp 49–97
Fu B, Zhao J, Li B, Yao J, Mouafo Teifouet AR, Sun L, Wang Z (2020) Fatigue reliability analysis of wind turbine tower under 
random wind load. Struct Safety 87:101982
Gambier A (2021) Pitch control of three bladed large wind energy converters-a review. Energies 14(23):8083
García S, Ramírez-Gallego S, Luengo J, Benítez JM, Herrera F (2016) Big data preprocessing: methods and prospects. Big 
Data Anal 1(1):9
Ghareveran MH, Yazdizadeh A (2019) Estimation of v47/660kw wind turbine state and fault detection with extended 
kalman filter. In: 2019 6th International Conference on Control, Instrumentation and Automation (ICCIA). 1–7
Gonzalez E, Stephen B, Infield D, Melero JJ (2019) Using high-frequency SCADA data for wind turbine performance moni‑
toring: a sensitivity study. Renew Energy 131:841–853
Grieves M (2016) Origins of the digital twin concept
Grinderslev C, Sørensen NN, Horcas SG, Troldborg N, Zahle F (2021) Wind turbines in atmospheric flow: fluid-structure 
interaction simulations with hybrid turbulence modeling. Wind Energy Sci 6(3):627–643
Gu J, Wang Y, Xie D, Zhang Y (2019) Wind farm NWP data preprocessing method based on t-SNE. Energies 12(19):3622
Gualtieri G (2019) A comprehensive review on wind resource extrapolation models applied in wind energy. Renew 
Sustain Energy Rev 102:215–233
Guo F, Mann J, Peña A, Schlipf D, Cheng PW (2022) The space-time structure of turbulence for lidar-assisted wind turbine 
control. Renew Energy 195:293–310
Guo R, Wang Y (2021) Remaining useful life prognostics for the rolling bearing based on a hybrid data-driven method. 
Proc Instit Mech Eng Part I J Syst Control Eng 235(4):517–531
Gözcü O, Dou S (2020) Reduced order models for wind turbine blades with large deflections. J Phys Conf Series 
1618(5):052046
Habibi H, Howard I, Simani S (2019) Reliability improvement of wind turbine power generation using model-based fault 
detection and fault tolerant control: A review. Renew Energy 135:877–896
Haghshenas A, Hasan A, Osen O, Mikalsen ET (2023) Predictive digital twin for offshore wind farms. Energy Inform 6(1):1
Han X, Jiang J, Xu A, Bari A, Pei C, Sun Y (2020) Sensor drift detection based on discrete wavelet transform and grey 
models. IEEE Access 8:204389–204399
Hanifi S, Liu X, Lin Z, Lotfian S (2020) A critical review of wind power forecasting methods-past, present and future. Ener‑
gies 13(15):3764


---

Page 30

---

Page 30 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
Hartmann D, Herz M, Wever U (2018). In: Keiper W, Milde A, Volkwein S (eds) Model Order Reduct Key Technol Digital 
Twins. Springer, Cham, pp 167–179
He L, Hao L, Qiao W (2021) Remote monitoring and diagnostics of pitch-bearing defects in an mw-scale wind turbine 
using pitch symmetrical-component analysis. IEEE Trans Indust Appl 57(4):3252–3261
He L, Zhang C, Zhang B, Yang O, Yuan W, Zhou L, Zhao Z, Wu Z, Wang J, Wang ZL (2022) A dual-mode triboelectric nano‑
generator for wind energy harvesting and self-powered wind speed monitoring. ACS Nano 16(4):6244–6254
Hernandez-Estrada E, Lastres-Danguillecourt O, Robles-Ocampo JB, Lopez-Lopez A, Sevilla-Camacho PY, Perez-Sariñana 
BY, Dorrego-Portela JR (2021) Considerations for the structural analysis and design of wind turbine towers: a 
review. Renew Sustain Energy Rev 137:110447
Heydari A, Garcia DA, Fekih A, Keynia F, Tjernberg LB, De Santoli L (2021) A hybrid intelligent model for the condition 
monitoring and diagnostics of wind turbines gearbox. IEEE Access 9:89878–89890
Hirvoas A, Prieur C, Arnaud E, Caleyron F, Munoz Zuniga M (2021) Quantification and reduction of uncertainties in a wind 
turbine numerical model based on a global sensitivity analysis and a recursive Bayesian inference approach. Int J 
Numer Method Eng 122(10):2528–2544
Hirvoas A, Prieur C, Arnaud E, Caleyron F, Zuniga MM (2022) Wind turbine quantification and reduction of uncertainties 
based on a data-driven data assimilation approach. J Renew Sustain Energy 14(5):053303
Hornshøj-Møller SD, Nielsen PD, Forooghi P, Abkar M (2021) Quantifying structural uncertainties in Reynolds-averaged 
Navier-stokes simulations of wind turbine wakes. Renew Energy 164:1550–1558
Hsu J-Y, Wang Y-F, Lin K-C, Chen M-Y, Hsu JH-Y (2020) Wind turbine fault diagnosis and predictive maintenance through 
statistical process control and machine learning. IEEE Access 8:23427–23439
Huang B, Liang Y, Qiu X (2021) Wind power forecasting using attention-based recurrent neural networks: a comparative 
study. IEEE Access 9:40432–40444
Huang Y, Zhang Z, Huang W, Chen S (2019) Dc-link voltage regulation for wind power system by complementary sliding 
mode control. IEEE Access 7:22773–22780
Hung M-H, Lin Y-C, Hsiao H-C, Chen C-C, Lai K-C, Hsieh Y-M, Tieng H, Tsai T-H, Huang H-C, Yang H-C, Cheng F-T (2022) A 
novel implementation framework of digital twins for intelligent manufacturing based on container technology 
and cloud manufacturing services. IEEE Trans Autom Sci Eng 19(3):1614–1630
Hungud V, Arunachalam SK (2020) Chapter five—digital twin: empowering edge devices to be intelligent. In: Raj P, 
Evangeline P (eds) The digital twin paradigm for smarter systems and environments: the industry use cases, vol 
117. Elsevier, United States, pp 107–127
Hur S-H (2019) Estimation of useful variables in wind turbines and farms using neural networks and extended kalman 
filter. IEEE Access 7:24017–24028
Hur S-h (2021) Short-term wind speed prediction using extended Kalman filter and machine learning. Energy Reports 
7:1046–1054
Igwemezie V, Mehmanparast A, Kolios A (2019) Current trend in offshore wind energy sector and material requirements 
for fatigue resistance improvement in large wind turbine support structures—a review. Renew Sustain Energy Rev 
101:181–196
Ilham Tyass, Abdelouahad Bellat, Abdelhadi Raihani, Khalifa Mansouri, Tajeddine Khalili (2022) Wind speed prediction 
based on seasonal ARIMA model. E3S Web Conf 336:00034
Isto P, Heikkilä T, Mämmelä A, Uitto M, Seppälä T, Ahola JM (2020) 5G based machine remote operation development 
utilizing digital twin. Open Eng 10(1):265–272
Jacoby M, Usländer T (2020) Digital twin and internet of things-current standards landscape. Appl Sci 10(18):6519
Jahani K, Langlois RG, Afagh FF (2022) Structural dynamics of offshore wind turbines: a review. Ocean Eng 251:111136
Jonscher C, Hofmeister B, Grießmann T, Rolfes R (2022) Very low frequency IEPE accelerometer calibration and application 
to a wind energy structure. Wind Energy Sci 7(3):1053–1067
Jureczko M, Pawlak M, Mezyk A (2005) Optimisation of wind turbine blades. J Mater Proc Technol 167(2):463–471
Kaarlela T, Pieskä S, Pitkäaho T (2020) Digital twin and virtual reality for safety training. In: 2020 11th IEEE International 
Conference on Cognitive Infocommunications (CogInfoCom), pp. 000115–000120
Kalapatapu A, Sarkar M (2012) Cloud computing: an overview. CRC Press, Florida, pp 3–29
Kandemir E, Liu J, Hasan A (2023) Digital twin-driven dynamic repositioning of floating offshore wind farms. Energy 
Reports 9:208–214
Karad S, Thakur R (2021) Efficient monitoring and control of wind energy conversion systems using internet of things 
(IoT): a comprehensive review. Environ Dev Sustain 23(10):14197–14214
Kareem A (2020) Emerging frontiers in wind engineering: Computing, stochastics, machine learning and beyond. J Wind 
Eng Indust Aerodynam 206:104320
Kaur MJ, Mishra VP, Maheshwari P (2020). In: Farsi M, Daneshkhah A, Hosseinian-Far A, Jahankhani H (eds) The conver‑
gence of digital twin, IoT, and machine learning: transforming data into action. Springer, Cham, pp 3–17
Kaviani HR, Nejat A (2021) Investigating the aeroelasticity effects on aeroacoustics and aerodynamics of a mw-class 
HAWT. J Wind Eng Indust Aerodynam 213:104617
Kaya M (2019) A CFD based application of support vector regression to determine the optimum smooth twist for wind 
turbine blades. Sustainability 11(16):4502
Keyantuo P, Dunn LN, Haydon B, Vermillion C, Chow FK, Moura SJ (2021) A vector auto-regression based forecast of wind 
speeds in airborne wind energy systems. IEEE Conference on Control Technology and Applications (CCTA). 69–75
Khan M, Liu T, Ullah F (2019) A new hybrid approach to forecast wind power for large scale wind turbine data using deep 
learning with TensorFlow framework and principal component analysis. Energies 12(12):2229
Kilimann J-E, Heitkamp D, Lensing P (2019) An augmented reality application for mobile visualization of gis-referenced 
landscape planning projects. In: Proceedings of the 17th International Conference on Virtual-Reality Continuum 
and Its Applications in Industry. Association for Computing Machinery, New York
Kisvari A, Lin Z, Liu X (2021) Wind power forecasting—a data-driven method along with gated recurrent neural network. 
RenewEnergy 163:1895–1909


---

Page 31

---

Page 31 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
	
Kitchenham BA, Charters S (2007) Guidelines for performing systematic literature reviews in software engineering. Tech‑
nical Report EBSE-2007-01, School of Computer Science and Mathematics, Keele University
Kong X, Liu X, Shi R, Lee KY (2015) Wind speed prediction using reduced support vector machines with feature selection. 
Neurocomputing 169:449–456
Koo J, Yoon S (2024) Simultaneous in-situ calibration for physical and virtual sensors towards digital twin-enabled build‑
ing operations. Adv Eng Inform 59:102239
Korprasertsak N, Leephakpreeda T (2019) Robust short-term prediction of wind power generation under uncertainty via 
statistical interpretation of multiple forecasting models. Energy 180:387–397
Kosovic B, Haupt SE, Adriaansen D, Alessandrini S, Wiener G, Delle Monache L, Liu Y, Linden S, Jensen T, Cheng W, 
Politovich M, Prestopnik P (2020) A comprehensive wind power forecasting system integrating artificial intel‑
ligence and numerical weather prediction. Energies 13(6):1372
Kouadri A, Hajji M, Harkat M-F, Abodayeh K, Mansouri M, Nounou H, Nounou M (2020) Hidden Markov model based 
principal component analysis for intelligent fault diagnosis of wind energy converter systems. Renew Energy 
150:598–606
Kumar R, Ezhilarasi D (2023) A state-of-the-art survey of model order reduction techniques for large-scale coupled 
dynamical systems. Int J Dynam Control 11(2):900–916
Kumar N, Lee SC (2022) Human-machine interface in smart factory: a systematic literature review. Technol Forecast Soc 
Change 174:121284
Lalik K, Watorek F (2021) Predictive maintenance neural control algorithm for defect detection of the power plants rotat‑
ing machines using augmented reality goggles. Energies 14(22):7632
Ledoux J, Riffo S, Salomon J (2021) Analysis of the blade element momentum theory. SIAM J Appl Math 81(6):2596–2621
Lee JCY, Fields MJ (2021) An overview of wind-energy-production prediction bias, losses, and uncertainties. Wind Energy 
Sci 6(2):311–365
Li Y, Fan L, Miao Z (2020) Wind in weak grids: low-frequency oscillations, subsynchronous oscillations, and torsional inter‑
actions. IEEE Trans Power Syst 35(1):109–118
Li F, Li L, Peng Y (2021) Research on digital twin and collaborative cloud and edge computing applied in operations and 
maintenance in wind turbines of wind power farm. Environ Sustain Dev (GEESD2021) 17:80–92
Li S, Patnaik S, Li J (2023) IoT-based technologies for wind energy microgrids management and control. Electronics 
12(7):1540
Li Z, Wen B, Dong X, Peng Z, Qu Y, Zhang W (2020) Aerodynamic and aeroelastic characteristics of flexible wind turbine 
blades under periodic unsteady inflows. J Wind Eng Indust Aerodynam 197:104057
Li Y, Wu Z (2020) A condition monitoring approach of multi-turbine based on var model at farm level. Renew Energy 
166:66–80
Li L-L, Zhao X, Tseng M-L, Tan RR (2020) Short-term wind power forecasting based on support vector machine with 
improved dragonfly algorithm. Journal of Cleaner Production 242:118447
Li W, Ren J, Shi K, Lu Y, Zhou J, Zheng H (2024) Flexibility prediction of thin-walled parts based on finite element method 
and k-k-cnn hybrid model. Int J Adv Manufact Technol
Liang J, Kato B, Wang Y (2023) Constructing simplified models for dynamic analysis of monopile-supported offshore wind 
turbines. Ocean Eng 271:113785
Liang Y, Liu L, Huang J (2020) Modeling of wind power service with CFD and Kalman filtering. Springer, Singapore, pp 
61–81
Liew HF, Rosemizi AR, Aihsan MZ, Muzamir I, Baharuddin I (2020) Wind characterization by three blade savonius wind 
turbine using IoT. IOP Conf Series Mater Sci Eng 932(1):012080
Lin Z, Cevasco D, Collu M (2020) A methodology to develop reduced-order models to support the operation and main‑
tenance of offshore wind turbines. Appl Energy 259:114228
Lio WH, Li A, Meng F (2021) Real-time rotor effective wind speed estimation using gaussian process regression and 
Kalman filtering. Renew Energy 169:670–686
Liu H, Chen C (2019) Data processing strategies in wind energy forecasting models and applications: a comprehensive 
review. Appl Energy 249:392–408
Liu M, Fang S, Dong H, Xu C (2021) Review of digital twin about concepts, technologies, and industrial applications. J 
Manufact Syst 58:346–361
Liu Y, Ferrari R, Wu P, Jiang X, Li S, Wingerden J-W (2021) Fault diagnosis of the 10mw floating offshore wind turbine 
benchmark: a mixed model and signal-based approach. Renew Energy 164:391–406
Liu L, Liang Y (2021) Wind power forecast optimization by integration of CFD and Kalman filtering. Energy Sour Part A 
Recovery Utilizat Environ Effect 43(15):1880–1896
Liu X, Lin Z, Feng Z (2021) Short-term offshore wind speed forecast by seasonal ARIMA—a comparison against GRU and 
LSTM. Energy 227:120492
Liu Y, Liu S, Zhang L, Cao F, Wang L (2021) Optimization of the yaw control error of wind turbine. Front Energy Res 
9:626681
Liu X, Ospina J, Konstantinou C (2020) Deep reinforcement learning for cybersecurity assessment of wind integrated 
power systems. IEEE Access 8:208378–208394
Liu H, Song W, Niu Y, Zio E (2021) A generalized Cauchy method for remaining useful life prediction of wind turbine 
gearboxes. Mech Syst Signal Proc 153:107471
Liu K, Yu M, Zhu W (2019) Enhancing wind energy harvesting performance of vertical axis wind turbines with a new 
hybrid design: a fluid-structure interaction study. Renew Energy 140:912–927
Liu X, Zhang L, Wang J, Zhou Y, Gan W (2023) A unified multi-step wind speed forecasting framework based on numerical 
weather prediction grids and wind farm monitoring data. Renew Energy 211:948–963
Liu P, Zhao L, Fang G, Ge Y (2021) Explicit polynomial regression models of wind characteristics and structural effects on a 
long-span bridge utilizing onsite monitoring data. Struct Control Health Monitor 28(5):2705
Lu P, Ye L, Zhong W, Qu Y, Zhai B, Tang Y, Zhao Y (2020) A novel spatio-temporal wind power forecasting framework based 
on multi-output support vector machine and optimization strategy. J Cleaner Product 254:119993


---

Page 32

---

Page 32 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
Lv L, Wu Z, Zhang J, Zhang L, Tan Z, Tian Z (2022) A VMD and LSTM based hybrid model of load forecasting for power grid 
security. IEEE Trans Indust Inform 18(9):6474–6482
Lv M, Duan B, Jiang H, Dong D (2020) Application of knowledge graph technology in unified management platform 
for wind power data. In: IECON 2020 The 46th Annual Conference of the IEEE Industrial Electronics Society. 
1762–1766
López G, Arboleya P (2022) Short-term wind speed forecasting over complex terrain using linear regression models and 
multivariable LSTM and NARX networks in the ANDES mountains, ECUADOR. Renew Energy 183:351–368
Ma P, Macdonald M, Rouse S, Ren J (2024) Automatic geolocation and measuring of offshore energy infrastructure with 
multimodal satellite data. IEEE J Oceanic Eng 49(1):66–79
Ma X, Tao F, Zhang M, Wang T, Zuo Y (2019) Digital twin enhanced human-machine interaction in product lifecycle. 
Procedia CIRP 83:789–793
Ma Z, Zeng P, Lei L (2019) Analysis of the coupled aeroelastic wake behavior of wind turbine. J Fluids Struct 84:466–484
Mahmoud MS, Oyedeji MO (2019) Adaptive and predictive control strategies for wind turbine systems: a survey. IEEE/
CAA J Automat Sinica 6(2):364–378
Majidi Nezhad M, Groppi D, Marzialetti P, Fusilli L, Laneve G, Cumo F, Garcia DA (2019) Wind energy potential analy‑
sis using sentinel-1 satellite: a review and a case study on Mediterranean islands. Renew Sustain Energy Rev 
109:499–513
Maldonado-Correa J, Martín-Martínez S, Artigao E, Gómez-Lázaro E (2020) Using SCADA data for wind turbine condition 
monitoring: a systematic literature review. Energies 13(12):3132
Maldonado-Correa J, Torres-Cabrera J, Martín-Martínez S, Artigao E, Gómez-Lázaro E (2024) Wind turbine fault detection 
based on the transformer model using SCADA data. Eng Fail Anal 162:108354
Mamun AA, Sohel M, Mohammad N, Haque Sunny MS, Dipta DR, Hossain E (2020) A comprehensive review of the load 
forecasting techniques using single and hybrid predictive models. IEEE Access 8:134911–134939
Marti-Puig P, Blanco-M A, Cárdenas JJ, Cusidó J, Solé-Casals J (2019) Feature selection algorithms for wind turbine failure 
prediction. Energies 12(3):453
Mashaly M (2021) Connecting the twins: a review on digital twin technology and its networking requirements. Procedia 
Comput Sci 184:299–305
Mbuli N, Mathonsi M, Seitshiro M, Pretorius J-HC (2020) Decomposition forecasting methods: a review of applications in 
power systems. Energy Reports 6:298–306
Mccarty M, Johnson J, Richardson B, Rieger C, Cooley R, Gentle J, Rothwell B, Phillips T, Novak B, Culler M, Wright B 
(2023) Cybersecurity resilience demonstration for wind energy sites in co-simulation environment. IEEE Access 
11:15297–15313
Mei Y, Song S, Lee Y, Park J, Kim S-H, Yi S (2020) Representing temporal attributes for schema matching. In: Proceedings of 
the 26th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining. KDD ’20. Association for 
Computing Machinery, New York. 709–719
Merizalde Y, Hernández-Callejo L, Duque-Perez O, Alonso-Gómez V (2019) Maintenance models applied to wind turbines. 
A comprehensive overview. Energies 12(2):225
Messner JW, Pinson P (2019) Online adaptive lasso estimation in vector autoregressive models for high dimensional wind 
power forecasting. Int J Forecast 35(4):1485–1498
Michalakes J (2020) HPC for weather forecasting. Springer, Cham, pp 297–323
Minerva R, Lee GM, Crespi N (2020) Digital twin in the IoT context: a survey on technical features, scenarios, and architec‑
tural models. Proc IEEE 108(10):1785–1824
Mir M, Shafieezadeh M, Heidari MA, Ghadimi N (2020) Application of hybrid forecast engine based intelligent algorithm 
and feature selection for wind signal prediction. Evolv Syst 11(4):559–573
Miyanawala TP, Jaiman RK (2019) A hybrid data-driven deep learning technique for fluid-structure interaction. Int Conf 
Offshore Mech Arctic Eng 2:002–08004
Moghadam FK, Nejad AR (2022) Online condition monitoring of floating wind turbines drivetrain by means of digital 
twin. Mech Syst Signal Proc 162:108087
Moghadam FK, Rebouças GFdS, Nejad AR (2021) Digital twin modeling for predictive maintenance of gearboxes in float‑
ing offshore wind turbine drivetrains. Forschung Im Ingenieurwesen 85(2):273–286
Mohamed E, Gerami Seresht N, AbouRizk S (2023) Context-driven ontology-based risk identification for onshore wind 
farm projects: a domain-specific approach. Adv Eng Inform 56:101962
Moness M, Moustafa AM (2020) Real-time switched model predictive control for a cyber-physical wind turbine emulator. 
IEEE Trans Indust Inform 16(6):3807–3817
Morita Y, Rezaeiravesh S, Tabatabaei N, Vinuesa R, Fukagata K, Schlatter P (2022) Applying Bayesian optimization with 
gaussian process regression to computational fluid dynamics problems. J Comput Phys 449:110788
Morovati S, Zhang Y, Djouadi SM, Tomsovic K, Wintenberg A, Olama M (2021) Robust output feedback control design for 
inertia emulation by wind turbine generators. IEEE Trans Power Syst 36(6):5056–5067
Morrison R, Liu X, Lin Z (2022) Anomaly detection in wind turbine SCADA data for power curve cleaning. Renew Energy 
184:473–486
Mouha RA (2021) Internet of things (Iot). J Data Anal Inform Proc 9(2):77
Mu Z, Guo W, Li Y, Tagawa K (2023) Wind tunnel test of ice accretion on blade airfoil for wind turbine under offshore 
atmospheric condition. Renew Energy 209:42–52
Naik J, Dash PK, Dhar S (2019) A multi-objective wind speed and wind power prediction interval forecasting using vari‑
ational modes decomposition based multi-kernel robust ridge regression. Renew Energy 136:701–731
Navarrete EC, Trejo Perea M, Jáuregui Correa JC, Carrillo Serrano RV, Moreno GJR (2019) Expert control systems imple‑
mented in a pitch control of wind turbine: a review. IEEE Access 7:13241–13259
Nguyen TH, Prinz A, Friisø T, Nossum R, Tyapin I (2013) A framework for data integration of offshore wind farms. Renew 
Energy 60:150–161
Nguyen HX, Trestian R, To D, Tatipamula M (2021) Digital twin for 5g and beyond. IEEE Commun Maga 59(2):10–15


---

Page 33

---

Page 33 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
	
Nielson J, Bhaganagar K, Meka R, Alaeddini A (2020) Using atmospheric inputs for artificial neural networks to improve 
wind turbine power prediction. Energy 190:116273
Niu W, Huang J, Yang H, Wang X (2022) Wind turbine power prediction based on wind energy utilization coefficient and 
multivariate polynomial regression. J Renew Sustain Energy 14(1):013306
Njiri JG, Beganovic N, Do MH, Söffker D (2019) Consideration of lifetime and fatigue load in wind turbine control. Renew 
Energy 131:818–828
Olatunji OO, Adedeji PA, Madushele N, Jen T-C (2021) Overview of digital twin technology in wind turbine fault diagnosis 
and condition monitoring. In: 2021 IEEE 12th International Conference on Mechanical and Intelligent Manufactur‑
ing Technologies (ICMIMT). 201–207
O’Leary K, Pakrashi V, Kelliher D (2019) Optimization of composite material tower for offshore wind turbine structures. 
Renew Energy 140:928–942
Page MJ, Moher D, Bossuyt PM, Boutron I, Hoffmann TC, Mulrow CD, Shamseer L, Tetzlaff JM, Akl EA, Brennan SE, Chou R, 
Glanville J, Grimshaw JM, Hróbjartsson A, Lalu MM, Li T, Loder EW, Mayo-Wilson E, McDonald S, McGuinness LA, 
Stewart LA, Thomas J, Tricco AC, Welch VA, Whiting P, McKenzie JE (2021) PRISMA 2020 explanation and elabora‑
tion: updated guidance and exemplars for reporting systematic reviews. BMJ. https://​doi.​org/​10.​1136/​bmj.​n160
Pandit R, Astolfi D, Hong J, Infield D, Santos M (2023) Scada data for wind turbine data-driven condition/performance 
monitoring: a review on state-of-art, challenges and future trends. Wind Eng 47(2):422–441
Papi F, Jonkman J, Robertson A, Bianchini A (2024) Going beyond BEM with BEM: an insight into dynamic inflow effects 
on floating wind turbines. Wind Energy Sci 9(5):1069–1088
Petrović V, Jelavić M, Baotić M (2021) MPC framework for constrained wind turbine individual pitch control. Wind Energy 
24(1):54–68
Pimenta F, Pacheco J, Branco CM, Teixeira CM, Magalhães F (2020) Development of a digital twin of an onshore wind 
turbine using monitoring data. J Phys Conf Series 1618(2):022065
Platenius-Mohr M, Malakuti S, Grüner S, Schmitt J, Goldschmidt T (2020) File- and API-based interoperability of digital 
twins by model transformation: An IIoT case study using asset administration shell. Future Generat Comput Syst 
113:94–105
Porchetta S, Muñoz-Esparza D, Munters W, van Beeck J, van Lipzig N (2021) Impact of ocean waves on offshore wind farm 
power production. Renew Energy 180:1179–1193
Poterjoy J (2022) Implications of multivariate non-gaussian data assimilation for multiscale weather prediction. Monthly 
Weather Rev 150(6):1475–1493
Pradeep AV, Prasad SVS, Suryam LV, Kumari PP (2019) A comprehensive review on contemporary materials used for 
blades of wind turbine. Mater Today Proc 19:556–559
Premaratne P, Tian W, Hu H (2022) A proper-orthogonal-decomposition (pod) study of the wake characteristics behind a 
wind turbine model. Energies 15(10):3596
Qadir Z, Khan SI, Khalaji E, Munawar HS, Al-Turjman F, Mahmud MAP, Kouzani AZ, Le K (2021) Predicting the energy out‑
put of hybrid PV-wind renewable energy system using feature selection technique for smart grids. Energy Reports 
7:8465–8475
Qi Q, Tao F, Hu T, Anwer N, Liu A, Wei Y, Wang L, Nee AYC (2021) Enabling technologies and tools for digital twin. J Manu‑
fact Syst 58:3–21
Qian Z, Pei Y, Zareipour H, Chen N (2019) A review and discussion of decomposition-based hybrid models for wind 
energy forecasting applications. Appl Energy 235:939–953
Qian Y, Wang T, Yuan Y, Zhang Y (2020) Comparative study on wind turbine wakes using a modified partially-averaged 
Navier-stokes method and large eddy simulation. Energy 206:118147
Qin X, Luo Y, Tang N, Li G (2020) Making data visualization more efficient and effective: a survey. VLDB J 29(1):93–117
Rafiee A, Van der Male P, Dias E, Scholten H (2018) Interactive 3d geodesign tool for multidisciplinary wind turbine plan‑
ning. J Environ Manag 205:107–124
Rajamohan S, Vinod A, Aditya Pragada Venkata Sesha, M, Gopalakrishnan Vadivudaiyanayaki H, Nhanh Nguyen V, Arıcı M, 
Nižetić S, Thai Le T, Hidayat R, Tuyen Nguyen D, (2022) Approaches in performance and structural analysis of wind 
turbines—a review. Sustain Energy Technol Assess 53:102570
Rajpoot SC, Pandey C, Rajpoot PS, Singhai SK, Sethy PK (2021) A dynamic-SUGPDS model for faults detection and isola‑
tion of underground power cable based on detection and isolation algorithm and smart sensors. J Electr Eng 
Technol 16(4):1799–1819
Ravanji MH, Cañizares CA, Parniani M (2020) Modeling and control of variable speed wind turbine generators for fre‑
quency regulation. IEEE Trans Sustain Energy 11(2):916–927
Reddy SB, Magee AR, Jaiman RK, Liu J, Xu W, Choudhary A, Hussain AA (2019) Reduced order model for unsteady fluid 
flows via recurrent neural networks. Int Conf Offshore Mech Arctic Eng 2:002–08007
Ren Q, Xu Y, Zhang H, Lin X, Huang W, Yu J (2021) Shaking table test on seismic responses of a wind turbine tower sub‑
jected to pulse-type near-field ground motions. Soil Dynam Earthquake Eng 142:106557
Rodríguez F, Chicaiza WD, Sánchez A, Escaño JM (2023) Updating digital twins: Methodology for data accuracy quality 
control using machine learning techniques. Comput Indust 151:103958
Saad A, Faddel S, Mohammed O (2020) IoT-based digital twin for energy cyber-physical systems: design and implementa‑
tion. Energies 13(18):4762
Saenz-Aguirre A, Zulueta E, Fernandez-Gamiz U, Lozano J, Lopez-Guede JM (2019) Artificial neural network based rein‑
forcement learning for wind turbine yaw control. Energies 12(3):436
Saenz-Aguirre A, Zulueta E, Fernandez-Gamiz U, Ulazia A, Teso-Fz-Betono D (2020) Performance enhancement of the 
artificial neural network-based reinforcement learning for wind turbine yaw control. Wind Energy 23(3):676–690
Sasikala G, Chandra YPS, Siva N, Vinesh AS (2021) Wind turbine fault monitoring system using MQTT. J Phys Conf Series 
2040(1):012002
Sayed M, Lutz T, Krämer E, Shayegan S, Wüchner R (2019) Aeroelastic analysis of 10 mw wind turbine using CFD-CSD 
explicit FSI-coupling approach. J Fluids Struct 87:354–377


---

Page 34

---

Page 34 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
Schwegmann S, Faulhaber J, Pfaffel S, Yu Z, Dörenkämper M, Kersting K, Gottschall J (2023) Enabling virtual met masts for 
wind energy applications through machine learning-methods. Energy AI 11:100209
Sedaghatizadeh N, Arjomandi M, Kelso R, Cazzolato B, Ghayesh MH (2019) The effect of the boundary layer on the wake 
of a horizontal axis wind turbine. Energy 182:1202–1221
Selvaraj Y, Selvaraj C (2022) Proactive maintenance of small wind turbines using IoT and machine learning models. Int J 
Green Energy 19(5):463–475
Shah N, Bhatt C, Patel D (2018) IoT gateway for smart devices. Springer, Cham, pp 179–198
Shahid F, Zameer A, Muneeb M (2021) A novel genetic LSTM model for wind power forecast. Energy 223:120069
Sharma T, Balachandra P (2019) Model based approach for planning dynamic integration of renewable energy in a transi‑
tioning electricity system. Int J Electr Power Energy Syst 105:642–659
Shen Y, Abubakar M, Liu H, Hussain F (2019) Power quality disturbance monitoring and classification based on improved 
PCA and convolution neural network for wind-grid distribution systems. Energies 12(7):1280
Sheoran S, Pasari S (2022) Efficacy and application of the window-sliding ARIMA for daily and weekly wind speed fore‑
casting. J Renew Sustain Energy 14(5):053305
Shin W, Han J, Rhee W (2021) AI-assistance for predictive maintenance of renewable energy systems. Energy 221:119775
Shivani Sandhu KS, Ramachandran Nair A (2019) A comparative study of arima and rnn for short term wind speed 
forecasting. In: 2019 10th International Conference on Computing, Communication and Networking Technologies 
(ICCCNT). 1–7
Siddiqui MS, Fonn E, Kvamsdal T, Rasheed A (2019) Finite-volume high-fidelity simulation combined with finite-element-
based reduced-order modeling of incompressible flow problems. Energies 12(7):1271
Siddiqui MS, Latif STM, Saeed M, Rahman M, Badar AW, Hasan SM (2020) Reduced order model of offshore wind turbine 
wake by proper orthogonal decomposition. Int J Heat Fluid Flow 82:108554
Siddiqui MS, Rasheed A, Kvamsdal T (2020) Numerical assessment of rans turbulence models for the development of 
data driven reduced order models. Ocean Eng 196:106799
Sierra-García JE, Santos M (2021) Improving wind turbine pitch control by effective wind neuro-estimators. IEEE Access 
9:10413–10425
Silva RN, Fantini DG, Mendes RC, Guimarães M, Oliveira T, Junior AB (2023) Assessment of wind resource considering local 
turbulence based on data acquisition with sodar. Wind Eng 47(4):747–765
Simon J, Moll J, Krozer V (2024) Trend decomposition for temperature compensation in a radar-based structural health 
monitoring system of wind turbine blades. Sensors 24(3):800
Singh M, Fuenmayor E, Hinchy EP, Qiao Y, Murray N, Devine D (2021) Digital twin: origin to future. Appl Syst Innovat 
4(2):36
Sousa J, Gorlé C (2019) Computational urban flow predictions with Bayesian inference: validation with field data. Build 
Environ 154:13–22
Stadtmann F, Rasheed A, Kvamsdal T, Johannessen KA, San O, Kölle K, Tande JO, Barstad I, Benhamou A, Brathaug T, Chris‑
tiansen T, Firle A-L, Fjeldly A, Frøyd L, Gleim A, Høiberget A, Meissner C, Nygård G, Olsen J, Paulshus H, Rasmussen 
T, Rishoff E, Scibilia F, Skogås JO (2023) Digital twins in wind energy: emerging technologies and industry-
informed future directions. IEEE Access 11:110762–110795
Sun H, Qiu C, Lu L, Gao X, Chen J, Yang H (2020) Wind turbine power modelling and optimization using artificial neural 
network with wind field experimental data. Appl Energy 280:115880
Sá FPG, Brandão DN, Ogasawara E, Coutinho RdC, Toso RF (2020) Wind turbine fault detection: A semi-supervised learn‑
ing approach with automatic evolutionary feature selection. In: 2020 International Conference on Systems, Signals 
and Image Processing (IWSSIP). 323–328
Tabib MV, Tsiolakis V, Pawar S, Ahmed SE, Rasheed A, Kvamsdal T, San O (2022) Hybrid deep-learning pod-based paramet‑
ric reduced order model for flow around wind-turbine blade. J Phys Conf Series 2362(1):012039
Tahir A, Elgabaili M, Rajab Z, Buaossa N, Khalil A, Mohamed F (2019) Optimization of small wind turbine blades using 
improved blade element momentum theory. Wind Eng 43(3):299–310
Taira K, Hemati MS, Brunton SL, Sun Y, Duraisamy K, Bagheri S, Dawson STM, Yeh C-A (2020) Modal analysis of fluid flows: 
applications and outlook. AIAA Journal 58(3):998–1022
Tian W, Ozbay A, Hu H (2019) A wind tunnel study of wind loads on a model wind turbine in atmospheric boundary layer 
winds. J Fluids Struct 85:17–26
Tu G, Li Y, Xiang J (2022) Coordinated rotor speed and pitch angle control of wind turbines for accurate and efficient 
frequency response. IEEE Trans Power Syst 37(5):3566–3576
Tuerxun W, Chang X, Hongyu G, Zhijie J, Huajian Z (2021) Fault diagnosis of wind turbines based on a support vector 
machine optimized by the sparrow search algorithm. IEEE Access 9:69307–69315
Udo W, Muhammad Y (2021) Data-driven predictive maintenance of wind turbine based on SCADA data. IEEE Access 
9:162370–162388
Vahidi D, Porté-Agel F (2022) A physics-based model for wind turbine wake expansion in the atmospheric boundary 
layer. J Fluid Mech 943:49
Valikhani M, Jahangiri V, Ebrahimian H, Liberatore S, Moaveni B, Hines E (2024) Aerodynamic load estimation in wind 
turbine drivetrains using a Bayesian data assimilation approach. In: Platz R, Flynn G, Neal K, Ouellette S (eds) Model 
Validat Uncertainty Quantificat, vol 3. Springer, Cham, pp 67–71
Vargas SA, Esteves GRT, Maçaira PM, Bastos BQ, Cyrino Oliveira FL, Souza RC (2019) Wind power generation: a review and 
a research agenda. J Cleaner Product 218:850–870
van Dinter R, Tekinerdogan B, Catal C (2022) Predictive maintenance using digital twins: a systematic literature review. 
Inform Software Technol 151:107008
Veers P, Bottasso CL, Manuel L, Naughton J, Pao L, Paquette J, Robertson A, Robinson M, Ananthan S, Barlas T, Bianchini A, 
Bredmose H, Horcas SG, Keller J, Madsen HA, Manwell J, Moriarty P, Nolet S, Rinker J (2023) Grand challenges in the 
design, manufacture, and operation of future wind turbine systems. Wind Energy Sci 8(7):1071–1131
Vogel CR, Willden RHJ (2020) Investigation of wind turbine wake superposition models using Reynolds-averaged Navier-
stokes simulations. Wind Energy 23(3):593–607


---

Page 35

---

Page 35 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
	
Wang N, Chen Q, Zhu L, Sun H (2022) Integration of data-driven and physics-based modeling of wind waves in a shallow 
estuary. Ocean Modell 172:101978
Wang J, Liang Y, Zheng Y, Gao RX, Zhang F (2020) An integrated fault diagnosis and prognosis approach for predictive 
maintenance of wind turbine bearing with limited samples. Renewe Energy 145:642–650
Wang T, Liu Z (2022) Digital Twin and Its Application for the Maintenance of Aircraft. Springer, Cham, pp 1035–1052
Wang L, Liu J, Qian F (2021) Wind speed frequency distribution modeling and wind energy resource assessment based 
on polynomial regression model. Int J Electrical Power Energy Syst 130:106964
Wang A, Qian Z, Pei Y, Jing B (2022) A de-ambiguous condition monitoring scheme for wind turbines using least squares 
generative adversarial networks. Renew Energy 185:267–279
Wang J, Wang S, Zeng B, Lu H (2022) A novel ensemble probabilistic forecasting system for uncertainty in wind speed. 
Appl Energy 313:118796
Wang H, Xiong B, Zhang Z, Zhang H, Azam A (2023) Small wind turbines and their potential for internet of things applica‑
tions. iScience 26(9):107674
Wang Z, Yao L, Ding J, Zhang J (2020) Wind turbine rolling bearing fault diagnosis using t-sne and gwo-svm. In: 2020 7th 
International Conference on Information Science and Control Engineering (ICISCE). 2274–2279
Ward R, Choudhary R, Gregory A, Jans-Singh M, Girolami M (2021) Continuous calibration of a digital twin: comparison of 
particle filter and Bayesian calibration approaches. Data-Centric Eng 2:15
Wu P, Gong S, Pan K, Qiu F, Feng W, Pain C (2021) Reduced order model using convolutional auto-encoder with self-
attention. Phys Fluids 33(7):077107
Wu Y, Ma X (2022) A hybrid LSTM-KLD approach to condition monitoring of operational wind turbines. Renew Energy 
181:554–566
Wu Z, Wang H (2012) Research on active yaw mechanism of small wind turbines. Energy Procedia 16:53–57
Wu Y, Zhang K, Zhang Y (2021) Digital twin networks: a survey. IEEE Internet Things J 8(18):13789–13804
Xiang L, Yang X, Hu A, Su H, Wang P (2022) Condition monitoring and anomaly detection of wind turbine based on 
cascaded and bidirectional deep learning networks. Appl Energy 305:117925
Xiaoyu Z, Chao L (2019) Accommodation capability assessment of high-voltage direct current with a large-scale wind 
power integration system based on risk constraints of sub-synchronous oscillation. J Eng 2019(16):2131–2136
Xie J, Dong H, Zhao X (2023) Data-driven torque and pitch control of wind turbines via reinforcement learning. Renew 
Energy 215:118893
Xu Y, Sun Y, Liu X, Zheng Y (2019) A digital-twin-assisted fault diagnosis using deep transfer learning. IEEE Access 
7:19990–19999
Yan Y, Wang X, Ren F, Shao Z, Tian C (2022) Wind speed prediction using a hybrid model of EEMD and LSTM considering 
seasonal features. Energy Reports 8:8965–8980
Yang J, Fang L, Song D, Su M, Yang X, Huang L, Joo YH (2021) Review of control strategy of large horizontal-axis wind 
turbines yaw system. Wind Energy 24(2):97–115
Yang C, Liu J, Zeng Y, Xie G (2019) Real-time condition monitoring and fault detection of components based on 
machine-learning reconstruction model. Renew Energy 133:433–441
Yang G, Xinlei S, Baoliang L, Wenzhong S, Mingjiang Z, Ziyan Z (2020) Research on wind power prediction based on dop‑
pler sodar. Chinese Automation Congress, Shanghai, pp 1345–1348
Yue R, Jiang G, Jin X, He Q, Xie P (2024) Spatio-temporal feature alignment transfer learning for cross-turbine blade icing 
detection of wind turbines. IEEE Trans Instrument Measure 73:1–17
Zhang M, Amaitik N, Wang Z, Xu Y, Maisuradze A, Peschl M, Tzovaras D (2022) Predictive maintenance for remanufactur‑
ing based on hybrid-driven remaining useful life prediction. Appl Sci 12(7):3218
Zhang X, Ji T, Xie F, Zheng C, Zheng Y (2022) Data-driven nonlinear reduced-order modeling of unsteady fluid-structure 
interactions. Phys Fluids 34(5):053608
Zhang L, Qu J (2021) Study on aerodynamic performance of a combined vertical axis wind turbine based on blade ele‑
ment momentum theorem. J Renew Sustain Energy 13(3):033304
Zhang J, Wei Y, Tan Z (2020) An adaptive hybrid model for short term wind speed forecasting. Energy 190:115615
Zhang J, Yan J, Infield D, Liu Y, Lien F-s (2019) Short-term forecasting and uncertainty analysis of wind turbine power 
based on long short-term memory network and gaussian mixture model. Appl Energy 241:229–244
Zhang K, Yu X, Liu S, Dong X, Li D, Zang H, Xu R (2022) Wind power interval prediction based on hybrid semi-cloud 
model and nonparametric kernel density estimation. Energy Reports 8:1068–1078
Zhao Z, Dai K, Camara A, Bitsuamlak G, Sheng C (2019) Wind turbine tower failure modes under seismic and wind loads. J 
Perform Constr Facilit 33(2):04019015
Zhao X, Dao MH, Le QT (2023) Digital twining of an offshore wind turbine on a monopile using reduced-order modelling 
approach. Renew Energy 206:531–551
Zhao N, Jiang Y, Peng L, Chen X (2021) Fast simulation of nonstationary wind velocity fields by proper orthogonal 
decomposition interpolation. J Wind Eng Indust Aerodynam 219:104798
Zhao L, Zhou Y, Matsuo IBM, Korkua SK, Lee W-J (2020) The design of a remote online holistic monitoring system for a 
wind turbine. IEEE Trans Indust Appl 56(1):14–21
Zheng Y, Ge Y, Muhsen S, Wang S, Elkamchouchi DH, Ali E, Ali HE (2023) New ridge regression, artificial neural networks 
and support vector machine for wind speed prediction. Adv Eng Software 179:103426
Zheng Y, Yang S, Cheng H (2019) An application framework of digital twin and its case study. J Ambient Intell Humaniz 
Comput 10(3):1141–1153
Zhilyaev I, Krushinsky D, Ranjbar M, Krushynska AO (2022) Hybrid machine-learning and finite-element design for flexible 
metamaterial wings. Mater Design 218:110709
Zhong D, Xia Z, Zhu Y, Duan J (2023) Overview of predictive maintenance based on digital twin technology. Heliyon 
9(4):14534
Zilong T, Xiao Wei D (2022) Layout optimization of offshore wind farm considering spatially inhomogeneous wave loads. 
Appl Energy 306:117947


---

Page 36

---

Page 36 of 36
Kandemir et al. Energy Informatics            (2024) 7:68 
Publisher’s Note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
