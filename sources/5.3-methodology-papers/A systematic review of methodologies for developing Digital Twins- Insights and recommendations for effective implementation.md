# A systematic review of methodologies for developing
Digital Twins: Insights and recommendations for
effective implementation
Emilio Carrión1,2,*, Óscar Pastor2
1Mercadona Tech, Mercadona
2PROS – VRAIN, Universitat Politècnica de València.
Abstract
Considering the diversity and complexity of the Digital Twins design and development approaches,
understanding their methodological background is a significant problem. To face it, in this paper we
present and discuss a systematic review that examines the methodologies currently employed in the
development of Digital Twins. The study analyses relevant literature focusing on modelling and proposed
methodologies for developing Digital Twins. The review identifies different approaches to Digital Twin
development as the definition of structured frameworks and the proposal of step-by-step methodologies
for building them. The review is intended to provide valuable insights for researchers, practitioners, and
decision-makers on existing methodologies for developing effective and sound Digital Twin solutions.
Keywords
Digital Twins, Methodology, Systematic Literature Review

## 1. Introduction
Digital Twin (DT) technology has gained significant popularity in recent years due to its
potential to revolutionize engineering design and maintenance practices. DTs refer to a virtual
representation of a physical system that can be used to monitor and optimize its performance in
real time [ 1]. The development of digital twins involves a combination of disciplines, including
engineering, computer science, and data analytics. To ensure the correct development of DTs, it
is essential to select and implement an appropriate development methodology to build them.
This work introduces a systematic literature review with the objective of providing an overview
of existing works on methodologies for developing DTs. By analyzing the state-of-the-art
from that point of view, this review aims to identify the different kinds of studies that describe
how to build, maintain or evolve DTs, providing future research with a grounding base about
methodologies for developing them.
To achieve its purpose, after this introduction, an analysis of related works is presented
in section 2, where how DTs are currently conceptualized and categorized is explored. Next,
the methodological dimension is faced, and how the corresponding systematic review has
Companion Proceedings of the 16th IFIP WG 8. 1 Working Conference on the Practice of Enterprise Modeling and the 13th
Enterprise Design and Engineering Working Conference, November 28 – December 1, 2023, Vienna, Austria
*Corresponding author.
/envel⌢pe-⌢penemcaryp@gmail.com (E. Carrión)
/orcid0000-0002-7026-0495 (E. Carrión); 0000-0002-1320-8471 ( Pastor)
©2023 Copyright for this paper by its authors. Use permitted under Creative Commons License Attribution 4. 0 International (CC BY 4. 0).
CEURWorkshopProceedingsceur-ws.orgISSN 1613-0073

been designed and executed is explained. Finally, the results are discussed. Conclusions and
references that have been used complete the paper.

## 2. Related works
Digital Twins are being applied to a wide range of systems, which highlights their significance
and relevance in various domains. It is crucial to establish a common understanding of what
DTs actually are because the term can be interpreted differently by different researchers and
practitioners. Without a shared definition, it becomes challenging to communicate effectively
and compare research findings in this field.
There are existing works that infer and propose a conceptualization of DTs, making a liter-
ature review of existing definitions [ 1,2]. They generalise on previous DTs implementations
making note that a big part of the existing literature on DTs does not provide clear or explicit
conceptualisations, but it develops implementations applied to some concrete field. That is a
reason why it is important to conceptualize the idea of DTs to build a shared definition to build
from. By proposing and discussing various definitions and conceptualizations, these works
contribute to clarifying the core concept of DTs: linking physical objects and digital objects in
an accurate and real-time manner. This helps establish a more precise and shared understanding
of DTs, which is fundamental for advancing research and practical applications.
A relevant set of works also make an extensive systematic review of the state-of-the-art
of DTs research. Among them, [ 3,4,5,6] categorize the use and implementations of DTs on
several levels: by themes [ 4], application fields [ 3], definitions and concepts [ 5] and several
more. These systematic reviews are important because they provide a comprehensive overview
of the current state of DTs research. By categorising the research based on themes, application
fields, definitions, and concepts -among other criteria-, such systematic reviews help researchers
and practitioners stay informed about the existing literature, identify gaps in knowledge, and
gain insights into how DTs are being applied in different contexts. They serve as a foundation
for building upon existing knowledge.
However, these works only focus on making a literature review of current definitions of DTs
and classifying their different implementations. By contrast, no relevant systematic reviews
have been conformed focusing on the research of methodologies for developing them, an area
that this work tries to cover.

## 3. Methodology
The research performed in this paper makes a systematic review [ 7] of existing literature
about methodologies for developing DTs. As it follows a methodical approach, it is performed
in a repeatable and contrastable manner. To analyse and compare existing works about the
development of DTs, Fig. 1 shows the methodology followed to gather, filter and classify the
data sample we used to perform the analysis and the following examinations.


### 3. 1. Research questions
Furthermore, to solve the objectives of this work in a structured manner, we defined the
following research questions:

- RQ1 : What kind of methodologies are being proposed? As the main contribution of this
work, we want to identify the different methods and procedures that researchers are using
or proposing for developing DTs. Therefore, a classification of existing contributions is
needed for achieving this objective.

- RQ2 : Are the related works explicitly proposing methodologies, or are they a secondary
sub-product of works with other primary objectives? We also want to evaluate explicit
solutions in order to gain insights about whether the proposal of novel methodologies for
developing DTs is a relevant field of study and is actively researched.

### 3. 2. Search strategy
We picked a corpus of 300 papers collected using Google Scholar. We used the queries “digital
twin methodology”, “digital twin method” and “digital twin model”, and gathered 300 potentially
relevant papers based on their title.
Google Scholar was used as the main source for literature articles as it has a wide coverage
of academic publications, conferences, and other academic sources. We used advanced filtering
and citation metrics that helped us assess the impact of a particular study and find studies that
were more relevant to our research. We also evaluated other well-established peer-reviewed
digital libraries like IEEE and ScienceDirect, but Google Scholar already gave us relevant studies
from those sources, so we concluded it had an acceptable coverage for the preliminary objective
of this work, as it provided a greater variety of contributions.

### 3. 3. Inclusion criteria
The inclusion criteria defined for this review is research that proposes a methodology or
structured guide for defining or developing a DT. The proposal of a methodology does not have
to be the main contribution of the research, but it should be explicitly proposed.
This means that the focus of these inclusion criteria will be a document that directly proposes
a development methodology for building the DT. Also works that propose an implementation of
a DT in a specific domain, but in this way, they propose a structured way to define and construct
a DT would also meet the criteria.
Importantly, any study that meets the inclusion criteria can be included regardless of study
design (eg, qualitative, quantitative, or mixed studies). However, research should provide
sufficient methodological detail or a structured guide on how to define or develop a DT. On the
other hand, a paper that proposes the implementation of a DT but does not detail how it is built
or defined does not meet the criteria.
It is important to note that the proposed inclusion criteria were defined before conducting
the study search to reduce the potential bias. Moreover, no further refinement of the inclusion
criteria was required to ensure reliability.

In summary, the inclusion criteria defined for this review are focused on identifying studies
that present methodologies or structured guidelines for defining or developing DTs. This ensures
a thorough and reliable review and provides valuable information on the current state of DT
methodologies and implementations in various application areas.

### 3. 4. Exclusion criteria
In this work, we only defined exclusion criteria after performing the document search for
practical reasons. This late applied exclusion criteria to exclude not compliant studies were
excluding works without available English versions and those we did lack institutional access.

### 3. 5. Inclusion criteria application
The inclusion criteria application was performed first at title level for identifying those works
that were explicitly or implicitly related with DT research. Then, a filtering was conducted
based on the abstract of the articles, excluding those that were not proposing or building DTs in
their content. And, finally, a deep analysis of the remaining articles was carried out to identify
the different contributions presented in the selected works.

### 3. 6. Quality assessment
In addition to the inclusion and exclusion criteria, we also considered an assessment of the quality
of the selected studies. This quality assessment aims to provide more detailed inclusion/exclusion
criteria and weigh the relevancy of the different individual studies to help further research on
developing DTs building methodologies.
To guide this quality assessment, we defined a checklist questionnaire that affects the study
quality relative to the research topic of this work.
The checklist has the following three quality questions:

- QQ1 : Does the paper propose a DT development methodology as a primary result? This
quality question overlaps with the RQ2, but we wanted to assess it as part of the quality
questionnaire due to the relevance implied in works which main contribution is directly
aligned with the research topic of this work.

- QQ2 : Does the paper conduct a review of existing proposed methodologies to build upon
gaps or weaknesses in the existing literature? We consider that works that make a review
of existing methodologies for developing DTs before proposing a new solution align
more with the focus of this paper, that is identifying different and well-founded ways of
building DTs.

- QQ3 : Does the paper validate the proposed methodology with a case study? A case
study is a well-established method for validating the feasibility and fitness of proposed
solutions to a real case scenario. Therefore, we consider methodologies evaluated using a
case study more relevant for the analysis of this work. Also, it indicates some degree of
maturity in the proposed solution as it is validated with an example.

This quality assessment does not consist of a weighted score, but as an indicator of the study’s
relevance to this review, more affirmative responses meaning more explicit and sustained results.
This indicator should not be used to compare the overall quality of the works, but it should be
used to assess their relevance to the objective of this study.

## 4. Results and discussion

### 4. 1. Corpus
The final corpus of this systematic review consists of a total of 46 selected papers that met the
inclusion criteria and described various methods of DT development.
It is important to emphasize that among the selected works we found numerous proposals
and approaches that faced the problem of the DT development process. For example, some
authors suggested a more structured approach, defining frameworks that described how a DT
should be structured, while others suggested a more guided approach, proposing streamlined
step-by-step procedures to develop them.
From the original 300 papers, we applied a filter to keep only those directly related to Digital
Twins and we also removed duplicates leaving us with 78 studies to work with.
Then, for practical reasons, we excluded those that lacked an English version and those we
did lack institutional access (only 4 of them), leaving us with 72 papers.
Finally, we applied the proposed inclusion criteria for only taking into account those papers
that explicitly or implicitly proposed methodologies for developing DTs, 46 papers in total. In
Table 1 we can see the final selected works.

### 4. 2. Quality assessment
The results of the quality assessment for the selected studies in the context of developing DTs
building methodologies are presented in this section. The assessment aimed to provide a more
detailed evaluation of inclusion/exclusion criteria and to weigh the relevancy of individual
studies, thereby focusing further research on the advancement of DT development methodolo-
gies. The assessment was guided by a defined checklist questionnaire, which gauged the study
quality relative to the research topic of this work.
The assessment did not employ a weighted scoring system but rather acted as an indicator of
each study’s relevance to the objetive of this work. More affirmative responses to the checklist
questions indicated more explicit and substantial results. It is important to note that this
indicator should not be used to compare the overall quality of the individual works but instead
be utilized to assess their alignment with the objectives of this study.
Based on the quality assessment, the selected studies demonstrated varying degrees of
relevance to the development of DTs building methodologies as shown in Table 1:

- 63. 04% of the studies presented comprehensive and well-defined DT development method-
ologies as their primary contributions (QQ1).

- 63. 04% of them also conducted thorough reviews of existing methodologies, identifying
gaps and weaknesses to address in their proposals (QQ2).


- 86. 96% of the studies effectively validated their proposed methodologies through case
studies, enhancing the robustness of their findings (QQ3).
We will highlight a subset of the corpus that did accomplish all three quality checks and
that can represent works fully aligned with the proposal of methodologies for developing DTs.
Those works are [9, 10, 14, 15, 17, 20, 22, 24, 26, 32, 35, 37, 39, 40, 47, 48, 49].
Overall, the quality assessment provided valuable insights into the suitability and relevance of
each study to the research objectives. This information will guide the focus of further research
in the development of DT building methodologies, ensuring that the work is built upon robust
foundations and addresses pertinent gaps in the existing literature.

### 4. 3. Research questions
In this section, we will address the proposed key research questions aimed at understanding
the current landscape of methodologies proposed for developing DTs.

4. 3. 1. RQ1: What kind of methodologies are being proposed?
The main analysis and the primary contribution of this work is the analysis and classification
of the approaches that each work proposes for developing DTs.
Analysing through the selected works we identified two general proposal trends: the definition
of frameworks or generic architectures and the definition of step-by-step methodologies for
defining and building DTs.
Framework: this kind of study proposes a framework or architecture for designing DTs. It
describes the structure that a DT should follow, often expressed as layers and the relationship
between them. They describe each layer and component, their meaning and functionality and
how they are related. They propose a structured way of defining DTs.
There is a great variety of works that base their contribution on a framework or design
architecture that describes the different parts of a DT. Some of the more representative examples
are proposals like:

- [9] a four layer architecture composed by physical layer, data extraction and consolidation
layer, cyberspace layer and interaction layer.

- [10] a seven layer architecture formed by a layer for physical entities, one for communi-
cation, one for security, another for data storage, other for modelling and optimization, a
service layer and a final one for data visualization.

- [14] a five dimension architecture made of a physical entity layer, a virtual entity one, a
services module, a data module and a connection module.

- [15] a three layer framework built by a physical layer, a data layer that populates knowl-
edge repositories and a model layer used for life cycles and logical reasoning.

- [17] a five layer architecture composed by a simulation model, a perception model, a
detection process, an entity model and a process model.

- [20] a five component architecture formed by physical entities, virtual entities a Multi-
Agent System component, semantic models and a service layer.


- [22] a reference architecture made of DT components, composition of DTs, a connectivity
topology and an external connectivity layer.
These proposals follow a similar approach: presenting a reference architecture to guide future
developments in structuring the DT solution. They try to be a generalistic solution for defining
DTs and, due to the diversity of the proposals, we can see that there have many attempts and
points of view to define the structure a DT should have. These different proposed architectures
show a lack of shared understanding of what are the basic components of a DT architecture,
what affects to have a sound and accurate understanding of what it should exactly be composed
of.
Although they propose different approaches, we have observed some similarities in most of
the presented works that can extracted to see the common points most of the solutions present.
Our research work has focused on proposing that lacking, common DT architecture by
identifying the relevant layers for conceptually characterizing the essential components a DT
architecture should be composed of.
When defining an architecture for structuring DTs, mentioned existing literature often
proposes three common layers or dimensions:

- A layer for representing the physical entities. This conveys the physical reality of the
entities we are digitising. Their conceptual modeling, the characteristics that define them
and their properties.

- A layer for the virtual entities. This represents the virtual model we create for represent
the entities in the DT. Can be expressed as 3D models, virtual simulations, state machines,
etc.

- A layer for the communications and data flows between physical and virtual contexts.
The connection between the physical and virtual layers, how they communicate, and how
their share state and synchronize to offer the real-time feedback that DTs provide.
Then, most of the works add upon these with other components like data visualization or
service layers that add functionality to the DT solution in different contexts. Nevertheless, we
can summarize these structures to those three basic ones: physical, virtual and data layers.
Open questions are raised by these insights, such as which solutions are better that the
others, if they are more suited to a specific context or field and how they perform applied to
real examples. Further research could focus in these questions to evaluate and compare the
different proposed frameworks.
Methodology: this other kind of study proposes a guide often expressed as a step-by-step
procedure for developing DTs. It guides the researcher through a procedure for designing and
building them.
In this case we also find a great variety of approaches and proposals. This kind of contribution
presents guidelines for developing DTs in a structured manner. Some representative proposed
methodology examples are:

- [24]: model physical devices creating high-level models of physical devices (e.g., sensors,
actuators), utilize the model by other systems that use these high-level models to extract
information about the physical devices, finally information consumers, such as monitoring
apps, augmented reality apps, and data providers, utilize the models.


- [26]: identify possible machine states, define variables and data source for collecting
real-time data, develop simulation models for individual equipment pieces, connect data
sources to the simulation models for real-time synchronization, analyze real-time data to
replicate system behavior, and finally create a DT by assembling all equipment models.

- [35]: collect data from physical equipment and sources, build a rational information
model based on industry standards and ontology modelling, process and organize data
for meaningful use (including long-term archiving and knowledge discovery), finally,
apply the DT to optimize processes, design, reconfiguration, and data transmission to
downstream operations.

- [39]: select and model machine components, determine modeling levels, and compose a
complete digital machine model, define data to monitor, select and create virtual sensors,
and integrate them into the machine’s physics-based model, and finally, select components
for tuning, define available data sources, and select parameters for online tuning to align
the digital model with real machine behavior.

- [43]: define the purpose and goals for creating the DT, develop a digital representation of
the physical system’s data and behavior, create a deployable software artifact based on the
DT model, collect and process data, store the DT in a repository for access and potential
customization, integrate the DT into its operational context, and finally, continuously
update the DT, ensuring it remains synchronized with the physical system for its use
cases.

- [44]: start with a system specification and creating virtual prototypes of the physical
components, ensure compatibility between physical and virtual systems’ data to maintain
consistency, identify physical components generating events and translate them into
virtual system events, filter out-of-spec data during data collection and pre-processing,
validate the DT by comparing physical and virtual system behavior, and once validated,
use the DT for various applications like anomaly detection or root-cause analysis in
day-to-day operations.

- [13]: build a virtual representation of the physical product using CAD and 3D modeling,
process data for decision-making by analyzing data from various sources, simulate product
behaviors in a virtual environment using simulation and VR technologies, command the
physical product to adjust its functions based on DT recommendations using sensors
and actuators, establish secure real-time connections between the physical and virtual
product via networking and cloud computing, finally, collect product-related data from
different sources, feeding it back into the first step for continuous improvement.
As we see, with this kind of contributions we also observe a great diversity of proposals as
each work presents its own guideline of how building a DT. Some of them make more focus
on the specific context they are presented, like defining 3D models of the physical entities or
collect real-time for running physics simulations. Nevertheless, as with the previous case, we
also identify some similarities between the proposals:

- The first step (or one of the earliest ones) most of them define is identifying and creating
a specification, ontology or model of the physical entity we are building the DT on.
This step often includes selecting the physical entities or parts to digitise and creating a
conceptual model of them.


- Then, they instantiate this conceptual models in a virtual environment where they are val-
idated as faithful representations of the entities they portray, being subject to simulations,
data flow validations and comparisons with concrete reality.

- Finally, state synchronization between physical and digital parts is validated or put to
test to ensure consistency.
Apart of these similarities, they differentiate in including steps addressed to the specific
details of the context and field they are proposed on.
These shared points between the different proposed methodologies can help guide new
developments and proposals. They give a path future research can follow to evolve and validate
current solutions.
These reflections also allow us to contribute a method proposal for developing DTs, proposal
that is based on the learnt insights, and that has three main steps:

- 1. Conceptual characterization of the DT to be developed generating a precise specification
or model, well-grounded ontologically speaking.

- 2. Instantiate the artefact built in step 1 in the selected (virtual) context of use.

- 3. Define and validate the synchronizations between the physical and the digital compo-
nents of the DT architecture.
For both frameworks and methodologies we see different approaches, further research is
needed to identify what proposals work better in different fields, development stages and con-
texts. Also, although there have been attempts to propose generic solutions for the development
of DTs, a standardized way of develop them could help practitioners to have a consistent and
reliable method for building DTs. Future research could focus in this area building upon the
insights seen in this work.

4. 3. 2. RQ2: Are the related works explicitly proposing methodologies, or are they a
secondary subproduct of works with other primary objectives?
As previously seen when discussing QQ1, the results show that 63. 04% of the analyzed works
have the proposal of a methodology for developing DTs as their primary contribution versus
the 36. 96% of them whose proposal is oriented to solve other primary problems.
These insights show an explicit interest in this field of study and validate the relevance of the
analysed papers contributions.

## 5. Conclusions
As seen through the results there is a clear and increasing interest in research about methodolo-
gies for developing DTs.
We identified two main contribution trends in the development of methodologies for building
DTs: the definition of frameworks for helping practitioners structure DTs and the definition of
step-by-step methodologies that guide the construction of DT solutions.

While the abundance of solutions highlights the progress made in this field, it also underscores
the need for standardization and comparative evaluations to identify the most effective and
efficient techniques for specific problem domains.
Researchers and practitioners seeking to develop DT-based solutions can benefit from the
selection and classification of works presented in this paper. By having a high-level view of
the different approaches, they can make informed decisions while selecting the most suitable
methods for their specific tasks.
For further works, this systematic review can be seen as a solid first step. After completing
this effort of methodological characterization of existing DT design and development methods,
we want to propose a generic method that takes the most common features and good practices
which are reported in those current approaches. Our final intention is to apply our proposal to
a practical problem from the complex logistics operations at Mercadona Tech, based on a sound
framework that takes into account the current knowledge from the DT design methodological
perspective.
In conclusion, this systematic literature review serves as a valuable resource, offering a clear
landscape of DT development methodologies, and identifying emerging trends. It is hoped that
this study will foster ongoing discussions and inspire future advancements in the field of DTs
and contribute to the broader progress of this field.
References
[1]M. Liu, S. Fang, H. Dong, C. Xu, Review of digital twin about concepts, technologies, and
industrial applications, Journal of Manufacturing Systems 58 (2021) 346–361. Publisher:
Elsevier.
[2]E. VanDerHorn, S. Mahadevan, Digital Twin: Generalization, characterization and imple-
mentation, Decision support systems 145 (2021) 113524. Publisher: Elsevier.
[3]A. Fuller, Z. Fan, C. Day, C. Barlow, Digital twin: Enabling technologies, challenges and
open research, IEEE access 8 (2020) 108952–108971. Publisher: IEEE.
[4]D. Jones, C. Snider, A. Nassehi, J. Yon, B. Hicks, Characterising the Digital Twin: A
systematic literature review, CIRP journal of manufacturing science and technology 29
(2020) 36–52. Publisher: Elsevier.
[5]C. Semeraro, M. Lezoche, H. Panetto, M. Dassisti, Digital twin paradigm: A systematic
literature review, Computers in Industry 130 (2021) 103469. Publisher: Elsevier.
[6]F. Tao, H. Zhang, A. Liu, A. Y. Nee, Digital twin in industry: State-of-the-art, IEEE
Transactions on industrial informatics 15 (2018) 2405–2415. Publisher: IEEE.
[7]B. Kitchenham, S. Charters, others, Guidelines for performing systematic literature reviews
in software engineering, 2007. [8]K. M. Alam, A. El Saddik, C2PS: A digital twin architecture reference model for the
cloud-based cyber-physical systems, IEEE access 5 (2017) 2050–2062. Publisher: IEEE.
[9]P. Zheng, A. S. Sivabalan, A generic tri-model-based approach for product-level digital twin
development in a smart manufacturing environment, Robotics and Computer-Integrated
Manufacturing 64 (2020) 101958. Publisher: Elsevier.

[10] S. Singh, M. Weeber, K.-P. Birke, Advancing digital twin implementation: A toolbox for
modelling and simulation, Procedia CIRP 99 (2021) 567–572. Publisher: Elsevier.
[11] H. Zhang, Q. Qi, W. Ji, F. Tao, An update method for digital twin multi-dimension models,
Robotics and Computer-Integrated Manufacturing 80 (2023) 102481. Publisher: Elsevier.
[12] G. White, A. Zink, L. Codecá, S. Clarke, A digital twin smart city for citizen feedback,
Cities 110 (2021) 103064. Publisher: Elsevier.
[13] F. Tao, F. Sui, A. Liu, Q. Qi, M. Zhang, B. Song, Z. Guo, S. C.-Y. Lu, A. Y. Nee, Digital
twin-driven product design framework, International Journal of Production Research 57
(2019) 3935–3953. Publisher: Taylor & Francis.
[14] C. Wu, Y. Zhou, M. V. P. Pessôa, Q. Peng, R. Tan, Conceptual digital twin modeling
based on an integrated five-dimensional framework and TRIZ function model, Journal of
manufacturing systems 58 (2021) 79–93. Publisher: Elsevier.
[15] S. Singh, E. Shehab, N. Higgins, K. Fowler, D. Reynolds, J. A. Erkoyuncu, P. Gadd, Data
management for developing digital twin ontology model, Proceedings of the Institution of
Mechanical Engineers, Part B: Journal of Engineering Manufacture 235 (2021) 2323–2337. Publisher: SAGE Publications Sage UK: London, England.
[16] M. A. N. de Andrade, H. A. Lepikson, C. A. T. Machado, A new framework and methodology
for digital twin development, in: 2021 14th IEEE International Conference on Industry
Applications (INDUSCON), IEEE, 2021, pp. 134–138. [17] P. Zhao, J. Liu, X. Jing, M. Tang, S. Sheng, H. Zhou, X. Liu, The modeling and using strategy
for the digital twin in process planning, IEEE Access 8 (2020) 41229–41245. Publisher:
IEEE.
[18] W. Jia, W. Wang, Z. Zhang, From simple digital twin to complex digital twin Part I: A novel
modeling method for multi-scale and multi-scenario digital twin, Advanced Engineering
Informatics 53 (2022) 101706. Publisher: Elsevier.
[19] W. Luo, T. Hu, W. Zhu, F. Tao, Digital twin modeling method for CNC machine tool, in:
2018 IEEE 15th International Conference on Networking, Sensing and Control (ICNSC),
IEEE, 2018, pp. 1–4. [20] X. Zheng, F. Psarommatis, P. Petrali, C. Turrin, J. Lu, D. Kiritsis, A quality-oriented digital
twin modelling method for manufacturing processes based on a multi-agent architecture,
Procedia Manufacturing 51 (2020) 309–315. Publisher: Elsevier.
[21] J. Wang, L. Ye, R. X. Gao, C. Li, L. Zhang, Digital Twin for rotating machinery fault
diagnosis in smart manufacturing, International Journal of Production Research 57 (2019)
3920–3934. Publisher: Taylor & Francis.
[22] G. N. Schroeder, C. Steinmetz, R. N. Rodrigues, R. V. B. Henriques, A. Rettberg, C. E. Pereira,
A methodology for digital twin modeling and deployment for industry 4. 0, Proceedings of
the IEEE 109 (2020) 556–567. Publisher: IEEE.
[23] Y. Gao, H. Lv, Y. Hou, J. Liu, W. Xu, Real-time modeling and simulation method of digital
twin production line, in: 2019 IEEE 8th joint international information technology and
artificial intelligence conference (ITAIC), IEEE, 2019, pp. 1639–1642. [24] G. N. Schroeder, C. Steinmetz, C. E. Pereira, D. B. Espindola, Digital twin data modeling with
automationml and a communication methodology for data exchange, IFAC-PapersOnLine
49 (2016) 12–17. Publisher: Elsevier.
[25] G. S. Martinez, S. Sierla, T. Karhela, V. Vyatkin, Automatic generation of a simulation-based

digital twin of an industrial process plant, in: IECON 2018-44th Annual Conference of the
IEEE Industrial Electronics Society, IEEE, 2018, pp. 3084–3089. [26] E. Negri, G. Assiro, L. Caioli, L. Fumagalli, others, A machine state-based digital twin
development methodology, in: Summer School F. Turco-Industrial Systems Engineering,
2019, pp. 34–40. [27] B. H. Huynh, H. Akhtar, M. K. Sett, A universal methodology to create digital twins for
serial and parallel manipulators, in: 2019 IEEE international conference on systems, man
and cybernetics (SMC), IEEE, 2019, pp. 3104–3109. [28] V. Shvedenko, V. Shvedenko, O. Shchekochikhin, A process control methodology based on
digital twins of production system objects, Automatic Documentation and Mathematical
Linguistics 55 (2021) 210–218. Publisher: Springer.
[29] P. Aivaliotis, Z. Arkouli, K. Georgoulias, S. Makris, Methodology for enabling dynamic
digital twins and virtual model evolution in industrial robotics-a predictive maintenance
application, International Journal of Computer Integrated Manufacturing (2023) 1–19. Publisher: Taylor & Francis.
[30] S. Wagner, M. Milde, F. Barhebwa-Mushamuka, G. Reinhart, Digital twin design in produc-
tion, in: Towards Sustainable Customization: Bridging Smart Products and Manufacturing
Systems: Proceedings of the 8th Changeable, Agile, Reconfigurable and Virtual Produc-
tion Conference (CARV2021) and the 10th World Mass Customization & Personalization
Conference (MCPC2021), Aalborg, Denmark, October/November 2021 8, Springer, 2022,
pp. 339–346. [31] S. Sierla, M. Azangoo, K. Rainio, N. Papakonstantinou, A. Fay, P. Honkamaa, V. Vyatkin,
Roadmap to semi-automatic generation of digital twins for brownfield process plants,
Journal of Industrial Information Integration 27 (2022) 100282. Publisher: Elsevier.
[32] F. Psarommatis, A generic methodology and a digital twin for zero defect manufacturing
(ZDM) performance mapping towards design for ZDM, Journal of Manufacturing Systems
59 (2021) 507–521. Publisher: Elsevier.
[33] L. Zhang, L. Zhou, B. K. Horn, Building a right digital twin with model engineering,
Journal of Manufacturing Systems 59 (2021) 151–164. Publisher: Elsevier.
[34] B. Tipary, G. Erd\Hos, Generic development methodology for flexible robotic pick-and-
place workcells based on Digital Twin, Robotics and Computer-Integrated Manufacturing
71 (2021) 102140. Publisher: Elsevier.
[35] S. Dai, G. Zhao, Y. Yu, P. Zheng, Q. Bao, W. Wang, Ontology-based information modeling
method for digital twin creation of as-fabricated machining parts, Robotics and Computer-
Integrated Manufacturing 72 (2021) 102173. Publisher: Elsevier.
[36] C. Constantinescu, S. Giosan, R. Matei, D. Wohlfeld, A holistic methodology for develop-
ment of Real-Time Digital Twins, Procedia CIRP 88 (2020) 163–166. Publisher: Elsevier.
[37] T. Riedelsheimer, S. Gogineni, R. Stark, Methodology to develop Digital Twins for energy
efficient customizable IoT-Products, Procedia CIRP 98 (2021) 258–263. Publisher: Elsevier.
[38] G. Barbieri, D. A. Gutierrez, A GEMMA-GRAFCET methodology to enable digital twin
based on real-time coupling, Procedia Computer Science 180 (2021) 13–23. Publisher:
Elsevier.
[39] P. Aivaliotis, K. Georgoulias, Z. Arkouli, S. Makris, Methodology for enabling digital twin
using advanced physics-based modelling in predictive maintenance, Procedia Cirp 81

(2019) 417–422. Publisher: Elsevier.
[40] Y. Qamsane, J. Moyne, M. Toothman, I. Kovalenko, E. C. Balta, J. Faris, D. M. Tilbury, K. Bar-
ton, A methodology to develop and implement digital twin solutions for manufacturing
systems, IEEE Access 9 (2021) 44247–44265. Publisher: IEEE.
[41] S. Sierla, L. Sorsamäki, M. Azangoo, A. Villberg, E. Hytönen, V. Vyatkin, Towards semi-
automatic generation of a steady state digital twin of a brownfield process plant, Applied
Sciences 10 (2020) 6959. Publisher: MDPI.
[42] H.-H. Benzon, X. Chen, L. Belcher, O. Castro, K. Branner, J. Smit, An Operational Image-
Based Digital Twin for Large-Scale Structures, Applied Sciences 12 (2022) 3216. Publisher:
MDPI.
[43] L. Stojanovic, T. Usländer, F. Volz, C. Weißenbacher, J. Müller, M. Jacoby, T. Bischoff,
Methodology and tools for digital twin management—The FA3ST approach, IoT 2 (2021)
717–740. Publisher: MDPI.
[44] J. Sleuters, Y. Li, J. Verriet, M. Velikova, R. Doornbos, A digital twin method for automated
behavior analysis of large-scale distributed IoT systems, in: 2019 14th Annual Conference
System of Systems Engineering (SoSE), IEEE, 2019, pp. 7–12. [45] Q. Liu, H. Zhang, J. Leng, X. Chen, Digital twin-driven rapid individualised designing of
automated flow-shop manufacturing system, International Journal of Production Research
57 (2019) 3903–3919. Publisher: Taylor & Francis.
[46] M. Ensafi, K. Afsari, S. M. Mehta, N. Shadab, A. Salado, S. Sagheb, M. Kretser, A modeling
methodology towards digital twin development in smart factories for the industry 4. 0
human augmentation experiments, in: Proc. of the Conference CIB W78, volume 2021,
2021, pp. 11–15. [47] S. Liu, J. Bao, Y. Lu, J. Li, S. Lu, X. Sun, Digital twin modeling method based on biomimicry
for machining aerospace components, Journal of manufacturing systems 58 (2021) 180–195. Publisher: Elsevier.
[48] L. Zhang, Y. Guo, W. Qian, W. Wang, D. Liu, S. Liu, Modelling and online training
method for digital twin workshop, International Journal of Production Research 61 (2023)
3943–3962. Publisher: Taylor & Francis.
[49] Q. Bao, G. Zhao, Y. Yu, S. Dai, W. Wang, Ontology-based modeling of part digital twin
oriented to assembly, Proceedings of the Institution of Mechanical Engineers, Part B:
Journal of Engineering Manufacture 236 (2022) 16–28. Publisher: SAGE Publications Sage
UK: London, England.
[50] A. Ebrahimi, Challenges of developing a digital twin model of renewable energy generators,
in: 2019 IEEE 28th international symposium on industrial electronics (ISIE), IEEE, 2019,
pp. 1059–1066. [51] X. Zhong, F. Babaie Sarijaloo, A. Prakash, J. Park, C. Huang, A. Barwise, V. Herasevich,
O. Gajic, B. Pickering, Y. Dong, A multidisciplinary approach to the development of
digital twin models of critical care delivery in intensive care units, International Journal
of Production Research 60 (2022) 4197–4213. Publisher: Taylor & Francis.
[52] J. C. Kirchhof, J. Michael, B. Rumpe, S. Varga, A. Wortmann, Model-driven digital twin
construction: synthesizing the integration of cyber-physical systems with their information
systems, in: Proceedings of the 23rd ACM/IEEE international conference on model driven
engineering languages and systems, 2020, pp. 90–101. Google Scholar search for... Google Scholar search for... Google Scholar search for...
300 papers
Remove duplicates andfilter those related to Digital Twins
78 papers
72 papers
46 papersRemove papers not available in english or without institut...
Remove papers that do not comply with inclusion criteria
Contribution analysis
Quality assessment Research question answersFigure 1: Publications analysis methodology.

Table 1
Publications
Publication Proposal QQ1 QQ2 QQ3
Alam, Kazi Masudul et al. 2017 [8] Framework X X
Zheng, Pai et al. 2020 [9] Framework X X X
Singh, Soumya et al. 2021 [10] Framework X X X
Zhang, He et al. 2023 [11] Framework X X
White, Gary et al. 2021 [12] Framework X
Tao, Fei et al. 2019 [13] Framework, Methodology X X
Wu, Chunlong et al. 2021 [14] Framework, Methodology X X X
Singh, Sumit et al. 2021 [15] Framework, Methodology X X X
de Andrade, Matheus. et al. 2021 [16] Framework, Methodology X
Zhao, Peng et al. 2020 [17] Framework, Methodology X X X
Jia, Wenjie et al. 2022 [18] Framework, Methodology X X
Luo, Weichao et al. 2019 [19] Framework, Methodology X
Zheng, Xiaochen et al. 2020 [20] Framework, Methodology X X X
Wang, Jinjiang et al. 2019 [21] Framework, Methodology X
Schroeder, Greyce N et al. 2020 [22] Framework, Methodology X X X
Gao, Yunpeng et al. 2019 [23] Framework, Methodology X
Schroeder, Greyce N et al. 2016 [24] Methodology X X X
Martínez, Gerardo et al. 2018 [25] Methodology X
Negri, E et al. 2019 [26] Methodology X X X
Huynh, Bao Huy et al. 2019 [27] Methodology X X
Shvedenko, VN et al. 2021 [28] Methodology X
Aivaliotis, Panagiotis et al. 2023 [29] Methodology X X
Wagner, Sarah et al. 2022 [30] Methodology X X
Sierla, Seppo et al. 2022 [31] Methodology X X
Psarommatis, Foivos et al. 2021 [32] Methodology X X X
Zhang, Lin et al. 2021 [33] Methodology X X
Tipary, Bence et al. 2021 [34] Methodology X
Dai, Sheng et al. 2021 [35] Methodology X X X
Constantinescu, Carmen et al. 2020 [36] Methodology X X
Riedelsheimer, Theresa et al. 2021 [37] Methodology X X X
Barbieri, Giacomo et al. 2021 [38] Methodology X X
Aivaliotis, Panagiotis et al. 2019 [39] Methodology X X X
Qamsane, Yassine et al. 2021 [40] Methodology X X X
Sierla, Seppo et al. 2020 [41] Methodology X
Benzon, Hans-Henrik et al. 2022 [42] Methodology X
Stojanovic, Ljiljana et al. 2021 [43] Methodology X X
Sleuters, Jack et al. 2019 [44] Methodology X X
Liu, Qiang et al. 2019 [45] Methodology X X
Ensafi, Mahnaz et al. 2021 [46] Methodology X X
Luo, Weichao et al. 2018 [19] Methodology X X
Liu, Shimin et al. 2021 [47] Methodology X X X
Zhang, Litong et al. 2022 [48] Methodology X X X
Bao, Qiangwei et al. 2022 [49] Methodology X X X
Ebrahimi, Amir et al. 2019 [50] Methodology X
Zhong, Xiang et al. 2022 [51] Methodology X X
Kirchhof, Jörg Christian et al. 2020 [52] Methodology X X