

---

Page 1

---

International Journal of Information Security (2024) 23:1171–1195
https://doi.org/10.1007/s10207-023-00784-x
REGULAR CONTRIBUTION
A review on digital twins for power generation and distribution
Jessica B. Heluany1 · Vasileios Gkioulos1
Published online: 1 December 2023
© The Author(s) 2023
Abstract
This paper presents a systematic literature review on the application of digital twins in the energy sector. Initially, we
generated an overview through a survey of prior reviews, independent of market vertical, then followed by a more detailed
review concentrating on the power production and distribution domains, as per the NIST (National Institute of Standards
and Technology) smart grid standard. We implemented a rigorous method, which included seven stages, beginning with the
collection of 2238 articles. We observed that the energy sector range was too broad and ﬁltered by generation and distribution
during the practical screening, resulting in 275 for further screening. This amount was then condensed to 81 papers that
matched the quality screening criteria for synthesis and examination. In summary, digital twin architectures and frameworks
include ﬁve components: the physical entity, bidirectional communication, the virtual entity (with modeling and simulation),
data management, and services. Our study contributed by determining that distribution management is the most pertinent
application of digital twins in the distribution domain and fault diagnosis in the generation domain. Furthermore, we found
that digital twins involve multiple stakeholders whose role is rarely discussed in studies, and we identiﬁed a similar absence
of emphasis for security. Research on security often presents the digital twin as an additional layer of protection, yet rarely
investigates the security of the digital twin by itself. The potential limitations of our study to answer some of the technical
research questions may be because of the criteria for the selection of papers. However, as the emphasis of this study is on the
energy sector, it enabled domain-speciﬁc ﬁndings for generation and distribution.
Keywords Digital twin · Smart grid · Generation · Distribution
1 Introduction
Critical infrastructures are the main sectors that provide
means for us to keep our way of life. Their malfunction
can debilitate a country’s safety and/or security in different
forms, reason for which CISA (Cybersecurity Infrastructure
and Security Agency) states that from all critical sectors,
the energy sector is of unique criticality. Their argument for
such uniqueness is that “it provides an ‘enabling function’
across all critical infrastructure sectors” [1]. Given this con-
text, it is clear the importance of improving the resilience
and reliability of the power grid to keep this critical infras-
B Jessica B. Heluany
jessica.b.heluany@ntnu.no
Vasileios Gkioulos
vasileios.gkioulos@ntnu.no
1
Department of Information Security and Communication
Technology (IIK), Faculty of Information Technology and
Electrical Engineering (IE), NTNU – Norwegian University
of Science and Technology, Gjøvik, Norway
tructure functional in adverse situations that may include
a wide range of actors, equipment, systems, markets, ser-
vices, and stakeholders. Moreover, according to the NIST
framework for smart grids, investments on this study ﬁeld
are estimated to generate economic beneﬁts that can achieve
billions of dollars [2]. Thus, possible technologies that may
be suitable to address the energy sector challenges, such as
digital twins, are worth exploring. Between the advantages
of a digital twin implementation, we can mention real-time
simulation to improve decision making, performance, diag-
nosis, among others. This makes them suitable for addressing
common problems of the energy sector, help in the energy
transition, and upmost, provide more resilience to the grid.
This illustrates the value of exploring current literature to
identify the advancements and applications of digital twin
technologies within the energy sector.
In light of this, our study seeks to cover the following
topics:
123


---

Page 2

---

1172
J. B. Heluany, V. Gkioulos
– To identify and classify research papers approaching dig-
ital twin concepts and applications in the energy sector;
– To identify design architectures, operational paradigms,
current tools, and modeling techniques for the develop-
ment of digital twins;
– To identify how the digital twin security has been
addressed;
– To investigate existing applications and identify use cases
that can contribute to foster digital twin application in the
energy sector;
By researching these topics, this work will generate fresh
insights into some challenges of the power systems, since
the identiﬁed use cases reﬂect relevant problems faced by
this sector, and the topics that cover digital twin technical
aspects are helpful for future implementations. Interest-
ingly, as stated by [3], several governments are planning to
incorporate DERs (Distributed Energy Resources) as part
of the energy transition strategy, specially from renewable
generation, which can be weather dependent resulting in
intermittent production. This fact raises even more a chal-
lenge that is widely discussed by the scientiﬁc community:
the growing management complexity of the grid. In a lit-
erature review of power systems challenges, besides the
distribution management, [4] also pointed climate changes
and environmental conditions (that are related to the dis-
cussion of DERs incorporation by [3]), disturbances or
unexpected events from faults sources, and cyber-attacks.
Considering the possible cascading effects of such risks, [5]
argued that smart grids naturally leads to decision making by
stakeholders that can be assisted by data-driven algorithms,
resulting in yet another challenge of “data-driven decision
support models.” Therefore, we can see that digital twins
can be an enabling technology to address the power sector
challenges, considering that they would be a virtual replica of
an entity of interest, allowing real-time simulations that can
guide stakeholders decisions and provide solutions to some
of these challenges.
1.1 Background
The reason for naming grids as smart relies on the fact that
more and more digital components and services are being
applied in the electricity network. The US Department of
Energy’s Advanced Grid Research [6], states that what makes
a grid smart is the “digital technology that allows for two-way
communication between the utilities and its customers, and
the sensing along the transmission lines.” However, the term
smart grids is very broad, approaching all domains of the
energy sector. The NIST conceptual model of smart grids [2]
deﬁnes seven main domains: system transmission operators
(TSOs); system distribution operators (DSOs); generation
(including DERs); customer; markets; operations and ser-
Fig. 1 NIST smart grid conceptual model
vice providers. The participants within each domain are
named Actors. Therefore, a given power plant, for example,
is an actor of the generation domain. Figure1 summarizes
the domains and the communication and electricity ﬂows
between them.
Another aspect that this standards highlights is the inter-
operability, deﬁned as “the capability of two or more net-
works,systems,devices,applications,orcomponentstowork
together, and to exchange and readily use information—
securely, effectively, and with little or no inconvenience to
the user.”
Once a smart grid is constituted of an increasing array of
interoperable systems, the ability to share information plays
a vital role in the continuous digitalization, and the need
for the energy transition, requires a consistent understanding
of the grid language to improve the communication across
stakeholders, including solutions of hardware, software, and
services.
From the digitalization perspective, digital twin appeared
in many technology trends reports in the last years. A brief
way of describing digital twins is that they constitute a virtual
replica of a real entity. By doing so, this technology would
enableaseriesofapplicationsthatmightbehelpfulforfurther
developments of smart grids. Digital twin has been listed by
Gartner as a technology trend for three consecutive years,
from 2017 to 2019 [7–9], and is still part of the trends within
Hyperautomation in 2020 Gartner report [10]. Digital twins
have also been a popular topic with increasing publications
in academic journals [11].
In a larger context, European initiatives such as the Euro-
pean Technology & Innovation Platforms (ETIPs) for Smart
Networks for Energy Transition (SNET), argue that digital
technologies are enablers to achieve a better system and put
digital twin and energy transition at the core of a low-carbon
economy [12].
123


---

Page 3

---

A review on digital twins for power generation and distribution
1173
1.2 Motivation
The topics covered in the previous sections highlight the
importance of the energy sector digitalization and its con-
nection with digital twins as one of the leading technology
trends of digitalization. However, as explained in the Back-
ground, the energy sector is composed of seven domains,
each with several possible actors. Regarding digital twins,
the possible applications are equally broad, making it hard
to see what advantages of digital twins are unique for smart
grids. Our main motivation is to better understand how digital
twins can contribute to speciﬁc smart grid domains, map-
ping what applications are more relevant according to the
selecteddomains.Giventheauthor’sknowledgebackground,
distribution and generation were selected for further investi-
gation.Weaimtocontributeinthisresearchtopicbymapping
the most common digital twins applications for these two
domains, and also evaluating the most common actors for
each domain because it provides information on what are the
real entities and how this can impact the way the digital twin
is implemented for each use case.
1.3 Structure of the paper
This paper is organized in seven sections, starting from the
introduction in Sect. 1, digital twin conceptualization in Sect.
2,andrelatedworkinSect.3toprovideanoverview,followed
by an explanation of the method applied for this systematic
literature review in Sect. 4. The ﬁndings are discussed in
Sect. 5, organized according to the research questions. Sec-
tion7 outlines some possibilities for future work, and Sect. 8
is dedicated to discussion, concluding our analysis.
2 Main aspects of digital twins
To gain an in-depth comprehension of digital twins’ con-
ceptualization and applications, this research started with an
analysis of previous reviews regardless of the market verti-
cal. The studies were analyzed aiming to map the application
domains, architectures and frameworks, tools, and security.
Deﬁnition evaluation was not initially included in the
objectives, but was quickly identiﬁed as a key factor in ensur-
ing that understanding and expectations are in sync for those
involved in the study of digital twins. Following this dis-
cussion, further study was conducted into the application
domains and use cases of digital twins.
A review of the primary tools and techniques employed
for modeling and simulation, as well as common architec-
tures and frameworks, was conducted to assess the feasibility
of creating digital twins. Furthermore, it was determined if
security was being addressed or not.
Theliteraturesearchwasconductedontwoapplicablebib-
liographic databases: ScienceDirect and IEEEXplore, using
the title query (“digital twin” AND (“review” OR “survey”
OR “state of the art”)). Only scientiﬁc/technical articles were
examined, leading to 139 studies that were reduced to 41
after applying format and content criteria during practical
screening, where Speciﬁc use cases and indirect studies were
excluded. These studies were ﬁltered by rigorous systematic
review methodologies remaining 21 for further analysis.
2.1 Definition considerations
The term digital twin has been around for approximately 20
years, since Grieves ﬁrst proposed it in 2002 [13]. However,
no common deﬁnition has been accepted by both academic
and industrial communities. To demonstrate and discuss the
lack of consensus and standardization, some authors com-
piled multiple deﬁnitions into tables to evaluate similarities
and differences [14–19], but this effort did not change the
most accepted deﬁnition, which was formalized by NASA
in 2012, and is cited in 15 from the 29 papers analyzed [11,
14–27]. According to NASA’s deﬁnition, a digital twin is
“an integrated multi-physics, multi-scale, probabilistic sim-
ulation of a vehicle or system that uses the best available
physical models, sensor updates, ﬂeet history, etc., to mirror
the life of its ﬂying twin. The digital twin is ultra-realistic
and may consider one or more important and interdependent
vehicle systems” [28].
It is out of the scope of this study to ﬁnd the com-
mon ground between deﬁnitions, but some scholars have
attempted to do so. As established by the meta-analysis in
[29], the authors inferred that the common elements among
the numerous deﬁnitions are i) virtual representation, ii) bidi-
rectional connection between the real and virtual entities, iii)
simulation, and iv) connection across all life cycle stages.
Upon analyzing these elements in correlation to NASA’s
deﬁnition, and contrasting them with published use cases,
it becomes apparent that not all digital twin applications
employ all these elements, thus indicating a misuse of the
term. As an example, some studies focus solely on modeling
and/or simulating a system of interest without considering
the bidirectional communication, while explicitly referring
to developing a digital twin instance.
In an effort to address this issue, a classiﬁcation based on
the level of data integration was proposed in [30], with the
data ﬂow exchange between the digital and physical objects
serving as the principal criterion. This work gave rise to
the terms Digital Model, Digital Shadow, and Digital Twin,
which have been cited in multiple other researches. Nev-
ertheless, there are other components that are not present
in this approach (such as the ﬁdelity of the virtual repre-
sentation), hindering the differentiation between traditional
solutions (i.e., simulation) and digital twins, and, in turn,
123


---

Page 4

---

1174
J. B. Heluany, V. Gkioulos
Fig. 2 System design hierarchy
and its knowledge domains [31]
prolonging the market time for more complex real-world
applications.
It is our opinion that the misconception about the deﬁni-
tion of digital twins has its roots in the obscure meanings
of the words “ultra-realistic,” “mirror,” and “system,” and its
relationship to complex systems organization. When refer-
ring to complex engineering systems, if no model is clearly
deﬁned at a particular abstraction layer, there is an inher-
ently ambiguity associated with the term “system” and its
constituent parts that would be “mirrored.”
In Fig.2, extracted from [31], the author deﬁnes a sys-
tem design hierarchy as composed of: parts, subcomponents,
components, subsystems, and systems. Along with this struc-
ture, several knowledge domains must be taken into consider-
ation,evidencinghowcomplexadigitaltwincanbeassuming
a high-ﬁdelity virtual replica that considers all these lev-
els and knowledge domains. In this way, thinking about a
“mirror” does not necessarily relate to “ultra-realistic” in
all levels, which, in turn, conveys the idea of modeling a
given piece of the hierarchy for all knowledge domains that
could go down to atomic levels. Thus, it is understandable
why scholars simplify the use cases, misusing the term,
and approaching real systems of interest at the component
level and only for speciﬁc knowledge domains. At the same
time, it reinforces the need for a more clear deﬁnition that
leads this technology to a higher maturity level, instead of
calling digital twin many traditional solutions that are in
place for years, such as modeling, simulation, and monitor-
ing.
2.2 Application domains
With the advancement of research on digital twins, it has
become possible to ascertain patterns and the most recurrent
ﬁelds of study. Some authors list the papers analyzed in their
reviewaccordingtomarketverticals[15,20,23],whileothers
categorize per lifecycle phase [18, 32]. Additionally, some
reviews are already based on a speciﬁc market vertical and
they list use cases without referring to the lifecycle phase
[14, 17, 22, 33, 34].
The outcomes of such studies vary depending on the sector
and the phase of the lifecycle that the digital twin addressed.
The investigation conducted in [35] (2022), which analyzed
42 papers, revealed that manufacturing and energy were the
verticals with the most publications, followed by aerospace
and automotive. From a lifecycle perspective, [18] mapped
240 papers published from 2010 to 2019, against each life-
cycle phase concluding that the amount of publications is
increasing especially for the production and service phases.
It is worth noting this reported increase for the services
phase, given that [33] analyzed applications in this area with
a cutoff date of December 2018, explicitly highlighting a
need for digital twins for services, since in several indus-
tries the proﬁt margin from services frequently surpasses the
margin from product sale. Nonetheless, over the years, [18]
shows that there has been a meaningful increase in produc-
tion/manufacturing, and service phase, approaching the gap
indicated by [33].
Taking the work [18] as a basis and compiling results from
other papers, it is possible to summarize common use cases
that might be applicable for more than one lifecycle phase:
123


---

Page 5

---

A review on digital twins for power generation and distribution
1175
Fig. 3 Example of digital twin architecture extracted from [38]
– Veriﬁcation; optimization; validation; production control
and planning; what-if analysis; predictive maintenance;
new business and business models; reduce of capital
investment; improvement of ﬂexibility to adapt to spe-
ciﬁc consumer needs; improve brand loyalty; real-time
state monitoring; asset management; traceability; data
management; man–machine interaction; costs reduc-
tion; improvement of vertical and horizontal integration;
health monitoring and analysis; support after sales recon-
ﬁguration; fault detection and diagnosis; reduction of
operational downtime; improvement of change manage-
ment of documents and assets; increase of customer
interaction and support.
2.3 Architectures and frameworks
We have noticed that some papers apply the terms architec-
ture and framework interchangeably, yet they have distinct
meanings. According to TOGAF standard deﬁnition [36],
a framework “provides the methods and tools for assisting
in the acceptance, production, use, and maintenance of an
Enterprise Architecture.” In our case, we are not dealing
with an enterprise architecture, but with one of the possible
abstraction levels. In this sense, we can assume the logi-
cal abstraction level for a digital twin system, referring to
the design, i.e., the structure, data ﬂows, functions, rules,
and methods that guide the implementation. The TOGAF
architecture framework deﬁnes three categories with types
of architectural work:
– Deliverable: a work deﬁned contractually by stakehold-
ers,
– Artifact: a work that describes an aspect of the architec-
ture and may or may not be considered a deliverable,
– Building blocks: potentially reusable component that can
be combined with other building blocks to deliver archi-
tectures and solutions.
Given that TOGAF conceptualization is broader than our
architectural scope, we also based this discussion on authors
who deﬁne architecture and framework from a computer
science view. If taken from programming perspective, a
framework is related to implementation of an architecture,
providing multiple classes that abstract particular concepts,
deﬁnes how these abstraction layers work together, provides
reusable components for application-speciﬁc features, and
organizes patterns at higher levels [37].
It can be argued that with no consensus on the deﬁni-
tion of digital twins, the way the architecture and framework
terms are used varies across the studies, although these could
be two distinct cases of term misuse. However, there is a
basis of agreement that a typical architecture has the pres-
ence of a physical and a virtual entity, in addition to the
relationship that connects them. An example of an archi-
tecture that contains these dimensions is shown in Fig.3
extracted from [38]. Regarding the framework and assum-
ing a combination of the TOGAF deﬁnition and as described
by [37] in the previous paragraph, we assume that a digital
twin framework approaches the architecture implementa-
tion and would be composed by building blocks that are
potentially reusable. This premise is aligned with the frame-
work taken as reference in Fig.4, where we observe multiple
building blocks for the physical entity platform, virtual
entity platform, data management platform, and services
platform. Each of the sub constituents of these building
blocks may be reusable in the same project, or even dif-
ferent projects depending on how they adhere to each
context.
123


---

Page 6

---

1176
J. B. Heluany, V. Gkioulos
Fig. 4 Example of digital twin framework extracted from [38]
Nonetheless, these terms are not observed in a uniﬁed
manner across the studies. Actually, attempting to detail
digital twin layers, a wide range of terms have been used,
including “properties,” “characteristics,” “enabling technolo-
gies,” among others. Table 1 from our previous work [39]
is an extraction of different authors summarizing how they
refer to the layers of further characterization. Upon evalu-
ating the description provided by the authors, it is possible
to identify overlapping terms even if they are categorized
differently. For example, [19] labels the update frequency
as a dimension of the digital twin, while in [15, 20] they
label as characteristics and utilize the term “twinning rate”
instead. Similarly, some authors seek to detail digital twins by
enumerating enabling technologies. In [23], they classiﬁed
the technologies according to domains (application, middle-
ware, network, and object), but in [17], the enablers were
listed without association do domains or building blocks.
The aim of this table is not to suggest a new terminology or
categorize digital twins features in groups, but to highlight
how the lack of consensus on digital twin concept impacts
the way it is described and detailed across the studies. Along
this table, higher group labels are separated with semicolons,
and terms used for these groups are separated with colons,
giving an idea of the proposed hierarchy in the studies.
This may be a consequence of the researchers’ varied back-
grounds, but it makes harder for the scientiﬁc community to
have an intuitive understanding of a digital architecture and
framework, and it demonstrates the need for future research
on standardizing all terms relevant for digital twin detail-
ing.
2.4 Tools
This section maps tools based on categories that were found
during the development of this study. Recalling the archi-
tectural functional blocks, similar blocks are applied for the
tools, ranging from the integration between the physical and
virtual entities, data-related services, modeling, and simula-
tion.
It is important to keep in mind that some solutions, such
as cloud services from Microsoft and Amazon, can ﬁt more
than one category. This is because some businesses provide
a variety of solutions. The identiﬁcation of all tools and their
associated categories, though, is outside the purpose of this
study. Additionally, the tool set changes depending on the
market vertical, and small ﬁxes could be included in a longer
list. Based on the research of [26] and the additional attribu-
tion of tools listed in other studies to the suggested categories,
Table 2 [39] offers an overview, where the solution suppliers
are identiﬁed in brackets.
2.5 Security
Security was mentioned as a possible solution provided by
digital twins [16, 20, 41], but there is no discussion whether
this would be related to the security of the digital twin itself.
Although some authors have stated that digital twins require
an additional security strategy due to the introduction of new
vulnerabilities [18, 22], most reviews have only mentioned
it as a challenge [15, 23, 29, 32, 42]. Section5.5 provides
further discussion on this topic for the energy sector papers.
123


---

Page 7

---

A review on digital twins for power generation and distribution
1177
Table 1 Compilation of terms used to detail digital twins in several studies highlighting the lack of uniformity related to the technology conceptu-
alization and implementation
References
DT details label
Terms used to describe DT features
[15, 20]
Characteristics
Integrated system, clone, counterpart, ties, links, description, construct, information,
simulation, test, prediction; virtual mirror, replica, physical entity, physical twin; virtual
entity, virtual twin, physical environment, virtual environment, state, realization,
metrology, twinning, twinning rate, physical-to-virtual connection/twinning,
virtual-to-physical connection/twinning, physical processes, virtual processes)
[20]
Parameters
Form, functionality, health, location, process, time, state, performance, environment
[16]
Components
radio-frequency identiﬁcation, wireless sensor networks, radio-frequency identiﬁcation
sensor networks, unit level, system level, system of systems level, middleware
(service-oriented architecture), communication protocol, communication protocol
interface (AutomationML), wireless communication, programming interface through
application programming interface, data-driven methods, geometry model, physical
model, behavior model, collaborative information model, decision making model,
scalability, model interoperability, ﬁdelity, dynamicity, modularity, application interface
layer
[23]
Domains, Enabling technologies
Application Domain: model architecture and visualization, software and Application
Programming Interfaces, data collection and pre-processing; Middleware Domain: storage
technology, data processing; Network Domain: communication technology, wireless
communication; Object Domain: hardware platform, sensor technology
[11]
Category, Dimensions
Context: reference object, tangible product life cycle phase, beneﬁts, application domain;
Data: data storage, data scope, data quality, data sources, data interpretation; Computing
capabilities: trigger types, model look-ahead perspective, computing timing capabilities,
update frequency of inputs, update frequency of outputs; Model: digital twin creation
approach, modeled characteristics, digital model types, model authenticity, model
maintenance, modularity; Integration: digital twin interaction, hierarchy, connection
mode, user focus, inter-organizational integration, collaboration; Control: level of
cognition, level of autonomy, learning capabilities; human–machine interaction: types of
interaction devices, human interaction capabilities
[17]
Enablers
Artiﬁcial intelligence, Internet of things, industrial internet of things, virtual reality,
augmented reality, hardware, communication technologies, knowledge building, design
process, development technologies
[40]
Building blocks, Properties
Physical Entity Platform: physical object (is observed), physical node (observes), human;
Virtual Entity Platform: semantic model with geometric model, physical model,
behavioral model, rule model, process model; Data Management Platform: data models,
data management methods; Service Platform: service models (physical/virtual), service
management layers
[19]
Dimension, Level
Update frequency: immediate real-time, event driven, every day, every week; Connectivity
modes: automatic, bidirectional, unidirectional; Integration breadth: world (full object
interaction), ﬁeld environment, near ﬁeld production system, product, machine; Product
lifecycle: begin of life, mid of life, end of life; Human-interaction: smart devices, virtual
reality, augmented reality, smart hybrid; Digital model richness: geometry, kinematics,
control behavior, multi-physical behavior; Simulation capabilities: look-ahead
perspective, Ad-Hoc, dynamic, static; Cyber Physical System intelligence: autonomous,
partial autonomous, automated, human triggered
[18]
Key technologies
Data-related technologies, high-ﬁdelity modeling technologies, model based simulation
technologies
[26]
Supporting tools types
Integration and simulation, digital twin modeling, bridging and twin control, big data
processing, big data storage, artiﬁcial intelligence–machine learning and application
programming interfaces
123


---

Page 8

---

1178
J. B. Heluany, V. Gkioulos
3 Related work of digital twins in the energy
market
While the previous section served as the conceptual basis
on digital twins, this section objective is to analyze previous
works of energy-related digital twins reviews and highlight
the differences between them and our work.
As a starting discussion, it is worth noticing that many
studies refer to power systems without detailing the domain.
As an example of general application in smart grids, [4]
mention use cases in distribution utilities, distributed energy
management systems, operation centers, fault diagnosis, bat-
teries systems, and renewable energy generators. Besides
these use cases are speciﬁc to the energy market, there is
no quantitative analysis to provide the most relevant ones.
Following a similar broad view of smart grids, in [44] the
authors map digital twin applications in power industry into
four groups: grid, plant, equipment, and other levels. Some
of the mentioned use cases include power grid structure and
design, control centers emulation, network security, trans-
formers, turbines, converters, relays, and fault diagnosis,
which are alike to the examples given in [4]. Research in
[45] also investigated potential uses of the technology, the
most common being anomaly detection, smart grid man-
agement, dynamic monitoring, and demand forecast. These
studies have revealed the signiﬁcance of the digital twin con-
cept across all aspects of smart grids, suggesting a number
of useful applications. However, they did not provide quan-
titative analysis to identify the most relevant use cases per
domain, which is one of the reasons we narrowed our review
to two domains, being able to contribute speciﬁcally with
generation and distribution.
For studies focused on speciﬁc domains, it has not been
demonstrated the most relevant use case either. In their dis-
cussion of Local Energy Communities (LEC) orchestration
[43], the authors goal is to develop digital twins that support
the balancing reserves of the electricity grid (distribution
domain). They contributed with modeling and simulation
methods providing relevant references for physics-based
models, and data-driven models. Their framework (Fig.5)
highlights prediction, optimization, and control strategies as
services provided by the digital twin.
Some scholars have conducted research on enabling stan-
dards and technologies for information models suitable for
digital twins. Taking into account the wide range of existing
solutions, [46] put forward the idea of utilizing the common
information model (CIM), a vendor neutral open standard
for power systems. They argue that CIM is already used
for developing interoperable applications (hardware or soft-
ware), and, given that interoperability is also a requirement
for digital twins, it may provide a framework that enables
information sharing. Also approaching standards, in [47] the
authors propose the use of communication protocols such as
IEC 61850 and IEEE C37.118 because of their ﬂexibility.
Moreover, when it comes to the energy sector, some bench-
marks are useful for developing study cases on a common
researchground.ByapplyingbenchmarkIEEE118-BusSys-
tem, [48] explored the adaptability of conventional models
for developing a power system digital twin (PSDT), what
includes enabling technologies that were discussed by [49]
such as IoT platforms, and advanced data analytics including
artiﬁcial intelligence and machine learning.
Such studies reinforce that the perceived beneﬁts are com-
mon sense among scholars. However, given that most of them
are not domain-speciﬁc, there is a gap of knowledge on what
can be the ﬁnal actors of each domain and most common
use cases, and that is the signiﬁcance of our work. We aim
at contributing with the energy sector community by doing
a quantitative analysis of use cases in generation and dis-
tribution domains, specifying the ﬁnal actors of these two
domains, such as detailing services provided by digital twins
which for these actors.
4 SLR method
This literature review differs from the one performed for the
related work section due to its rigorous and systematic steps.
It is based on the methodologies described by [50] and [51]
consisting of seven steps: (1) Identify the purpose, (2) Draft
Searching Protocol, (3) Apply practical screen, (4) Apply
quality screen, (5) Extract Data, (6) Synthesize studies, and
(7) Write the review.
Besides the databases, other tools utilized during this
research were EndNote 20 for references management (prac-
tical and quality screening), NVIVO and Excel to extract data
and synthesize information.
4.1 Purpose of the literature review
This literature review sought to identify the current state of
knowledge of digital twins in the energy sector. In order to
ﬁnd information for technical aspects of the purpose, the
following research questions were elaborated and grouped
according to speciﬁc categories. Group 1 (NIST domains
and use cases) aims to provide information for quantitative
analysis of use cases. Groups 2 and 3 (reference architec-
tures, frameworks, and tools) allow a comparison between
the conceptual aspects studied in Sect. 2 to evaluate if the
architectures and frameworks applied in the energy sector
differ from general market. Group 4 (network and binding)
focuses on the communication between the real and virtual
entities to assess if the studies detail the bidirectional com-
munication, while group 5 is focused on security, which was
expected to be present in energy-related studies, given that
it is a critical infrastructure sector. Lastly, Group 6 has the
123


---

Page 9

---

A review on digital twins for power generation and distribution
1179
Fig. 5 Digital twin framework for local energy communities digital twins extracted from [43]
Table 2 Compilation of some tools and techniques according to categories
Category
Tool/technique
Bridging/integration
Azure (Microsoft), AWS (Amazon), MindSphere (Siemens), Predix (GE), ThingWorx
(PTC), IBM Maximo Asset Health Insights (IBM), RFID, MTConnect, OPC UA,
MQTT, ZigBee, XML, IndraMotion MTX (Rexroth), Beacon (Fii-Foxconn),
TwinCAT (Beckhoff), SAP (SAP), Codesys (Codesys Group), edge/foggy computing
Data processing
Data fusion algorithms, BigQuery (Google),
Spark/Storm/S4/Hive/Mahout/Flink/Pig/Impala (Apache), edge/foggy computing,
VoltDB (VoltDB), Azure (Microsoft), AWS (Amazon)
Data storage
MongoDB (MongoDB), MySQL(Oracle/Others), Hadoop/Hbase/Kafka (Apache),
Oracle, Azure (Microsoft), AWS (Amazon), BigQuery (Google)
Data analytics
AI algorithms (e.g., feature selection, feature extraction, pattern recognition, stochastic
optimization, evolutionary, etc.), ML algorithms (neural networks, fuzzy logic, etc.),
TensorFlow (Google), Azure (Microsoft), AWS (Amazon), BigQuery (Google)
Modeling
Meta-information and semantics, ontologies, AutomationML, ﬁnite element, ﬁnite
element alternating method, AnyBody Modeling System (AnyBody Technology),
service-oriented architecture (SOA), representational state transfer (REST), Matlab
(MathWorks), Matpower (Matpower), InterPSS (InterPSS), OOPS, PowerFactory
(DIgSILENT), Modelica (Modelica), Markov chain, ANSYS Twin Builder (ANSYS),
NX (Siemens), SolidWorks (Dessault Systèmes), AutoCAD (Autodesk), 3D Max
(Autodesk), FreeCAD (Freecadweb), Azure (Microsoft), AWS (Amazon)
Simulation
FEM simulation, Montecarlo simulation, CFD simulation, DDSIM (Damage and
Durability Simulator), S2S DFS, Simulink (MathWorks), CAE-based simulation,
(CATIA) Dassault Systemes, CIROS Studio (VEROSIM), Simcenter 3D (Siemens),
ANSYS Twin Builder (ANSYS), PSS R NETOMAC (Siemens), MWorks (Tongyuan),
SUMO (Eclipse), Open Simulation Platform (DNV-GL), Azure (Microsoft), AWS
(Amazon)
123


---

Page 10

---

1180
J. B. Heluany, V. Gkioulos
objective to identify current challenges and directions for
future work.
Group 1: NIST domains and use cases
– RQ1: What is the domain and actor addressed?
– RQ2: What is the reported use case?
– RQ3: Is the study practical or theoretical?
– RQ4: What is the method applied?
– RQ5: Who are the stakeholders involved?
Group 2: Reference Architecture
– RQ1: What is the architecture adopted?
– RQ2: What are the operational requirements of each layer
of the framework?
Group 3: Framework and its tools and techniques
– RQ1: What are the modeling techniques and tools used?
– RQ2: What are the simulation techniques and tools used?
– RQ3: What are the data-related (processing, storage and
analysis) tools used?
Group 4: Network and binding
– RQ1: How is the data ﬂow between the physical and
virtual entities (manual, unidirectional or bidirectional?
– RQ2: How is the communication implemented in terms
of architecture, components and services?
Group 5: Security
– RQ1: How is the security of the digital twin itself
addressed?
– RQ2: How is the security of the communication between
the digital twin entity and the physical entity addressed?
– RQ3: How is the security of the communication within
digital twins addressed?
– RQ4: Does the study address any other layer of security?
Which one?
Group 6: Challenges and Future Work
– RQ1: What are the limitations of this study?
– RQ2: What are the challenges?
– RQ3: What is recommended as future work?
4.2 Searching protocol
The protocol was designed to allow the searching evalua-
tion and replication by deﬁning the databases and keywords
expression. The sources used to identify articles were: IEEE
Xplore, ACM Digital Library, ResearchGate, ScienceDirect,
Scopus, ProQuest, and Semantic Scholar.
The databases search was conducted with the following
query: ((“Document Title” OR “Abstract”: “digital twin*”)
AND (“Document Title” OR “Abstract”: “energy” OR “elec-
tric*” OR “power” OR “smart grid*”)). This set of keywords
intends to perform the initial ﬁlter of papers relating digital
twin technology with the energy sector, considering differ-
ent vocabulary that were retrieved from a previous broad
analysis. The collection retrieved 3675 papers including
duplicates. After eliminating duplicates, 2238 were consid-
ered for the practical screening.
4.3 Practical screening
The practical screening phase consists of identifying articles
that may contain relevant research to answer the questions
stated in the literature review purpose. The inclusion and
exclusion criteria adopted in this work are given in Table 3.
The papers assessment was conducted by the main author
(70%) and a laboratory assistant* at IIK, NTNU (30%). In
order to make the selection uniform, after each one had con-
cluded the selection, both assessed 10% of the selected by
each other and 5% of excluded. After aligning differences
and applying the inclusion/exclusion criteria explained here,
the initial 2238 papers were reduced to 275.
4.3.1 Inclusion criteria
1. Language: papers written in English.
2. Content: the content analyzed through title/abstract must
be related to the research questions.
3. Format: scientiﬁc/scholarly articles published in confer-
ences, workshops and journals.
4. Date: no restrictions were made regarding the year of pub-
lication because digital twin is an emerging technology.
5. Market vertical: papers must be related to digital twins
in the energy sector. It is worth commenting though, that
when it comes to consumers, papers that approach digital
twins focusing on energy consumption efﬁciency in other
ﬁelds, were not considered, otherwise the results would
be very broad and out of the scope of this study;
6. Smart grid domain: papers should be about generation
and distribution domains from NIST conceptual model of
smart grids
4.3.2 Exclusion criteria
1. Format: Letters, editorials, reports, posters, magazines,
trade journals, presentations, front and back matter pages
such as title pages, abstract pages, index pages, table of
contents, and stand-alone images.
123


---

Page 11

---

A review on digital twins for power generation and distribution
1181
Table 3 Inclusion and exclusion
criteria
Inclusion criteria
Type
1. Written in English
Language
2. Title eligible
Content
3. Scientiﬁc articles published in conferences, workshops and journals
Format
4. Publication year
Date
5. Energy sector
M. Vertical
6. Generation or distribution
Domain
Exclusion criteria
Type
1. Letters, editorials, reports, posters, magazines, trade journals, and presentations
Format
2. Secondary studies
Content
3. Articles that do not approach energy sector
M. Vertical
4. Articles of the energy sector, but outside the generation and distribution domains
Domain
5. Articles not found for full text download
Availability
2. Content: secondary studies in the form of reviews, sur-
veys, systematic literature reviews, and generic digital
twin frameworks.
3. Market vertical: articles outside the energy sector that do
not meet inclusion criteria ﬁve explanations.
4. Smart grid domain: papers about transmission, opera-
tions, service providers, markets, and customer domains
from NIST conceptual model of smart grids are out of the
scope.
4.4 Quality screening
The 275 studies selected during the practical screening were
rated according to a quality assessment deﬁned in a standard
form used for each paper. Again, the papers assessment was
conducted by the main author (70%) and a laboratory assis-
tant* at NTNU, IIK (30%). The papers that did not meet the
criteria were excluded, remaining 81 for the following steps.
4.4.1 Exclusion criteria
1. Research Questions: papers that do not answer at least two
questionsfromgroups2,orgroup3,orgroup5,andneces-
sarily one from group 4. The intention of this combination
is to cover at least some aspects related to architec-
ture, framework, security, and, necessarily approach the
network, once the bidirectional communication was iden-
tiﬁed as a key possible differential between a digital twin
and traditional solutions.
2. Component level: papers in which the use case is at com-
ponent level are too speciﬁc for the aim of this study.
3. Physical Model: papers that focus on the physical mod-
eling or structural properties instead of network/data.
Fig. 6 Summary of papers ﬁltering applied in this SLR
4.5 Data extraction
This step consists of systematically extracting data from each
paper selected during the quality screening. The extraction
form was prepared to store data that contributes to answering
the research questions in a consistent and uniform way, and
was performed by the coding tool available at NVIVO.
4.6 Synthesis of studies
Given the qualitative nature of most papers on digital twins,
the procedure adopted to analyze them and obtain a concept-
centric focus was based on synthesis by interpretation and
explanation.
4.7 Writing the review
The ﬁndings of this literature review are described follow-
ing standard writing principles aiming to make a theoretical
contribution by being critical and using evidence to support
the claims.
123


---

Page 12

---

1182
J. B. Heluany, V. Gkioulos
5 SLR analysis
The following subsections address the topics as organized in
the research questions.
5.1 NIST domains and use cases
As explained in the Background section 1.1, the terminology
of this paper is based on NIST Smart Grid Interoperability
Framework [2].
This work started addressing previous reviews regardless
of the market vertical, to map the main scientiﬁc ﬁndings on
digital twins, and then narrowing down to an overview of the
energy sector reviews that approached all NIST smart grid
domains. This step showed a gap in domain-based studies.
Attempting to cover this gap, we focused this paper on two
domains: generation and distribution.
After completing the practical screening and start classi-
fying the papers, we noticed that only the NIST domains
classiﬁcation would not be enough because many studies
approach more than one domain at the same time; thus,
some assumptions were made to enable the categorization
and provide an overview on what combination of domains
was more present before the quality screening. We catego-
rized the papers into four groups: generation, distribution,
multiple domains, and all domains. Nonetheless, for cases
where more than one domain is approached, for example,
transmission and distribution, the amount of papers were not
enough to enable analyzing a trend for this combination. For
this reason, the most relevant domain was taken into account
for the categorization, with the following considerations:
– Smart grid papers that are generic were considered
addressing all NIST domains and labeled in the category
“All”;
– Microgrid papers or synonyms as “Local Energy Com-
munity” usually embrace generation, distribution, and
sometimes transmission. In this work, we labeled them
as “Distribution” because this is the main domain
approached, similar to power ﬂow papers;
– Papers on electrical power systems or equipment that can
be utilized in more than one domain, such as transform-
ers, relays, batteries, high voltage cables, coolers, and so
on, were labeled as “Multiple”;
– Power plant papers, regardless of the energy source, were
labeled as “Generation”;
Following the same approach, considerations were made
to the actors found for the generation and distribution
domains:
– Generation actors: deﬁned power plant types includ-
ing wind, solar, nuclear, hydro, and thermal, added to
a generic category labeled as power plant;
– Distribution actors: substation, microgrid, distributed
energy resources (DERs), distribution centers;
For the use cases categorization, the following assump-
tions were made:
– Distribution management: papers related to multiple
energy sources to be integrated into the grid consider-
ing the uncertainty factor.
– Fault diagnosis: papers that approach monitoring, health
state, operational reliability, anomalies detection, percep-
tion, among others.
– Generation forecast: it is applicable for any energy
source, but the trend was more noticed for renewable
sources, being wind and solar, the most common targets
offorecastduetoitsintermittentpowergenerationnature.
– Performance optimization: besides the term performance
itself, other approaches of state estimation related to per-
formance were also included in this group.
– Predictivemaintenance:inadditiontoexplicitprediction-
related studies, papers approaching variables estimation,
fault prediction, and continuous monitoring were also
considered in this category.
– Reliability forecast: this category approaches both dis-
tribution management and generation forecast, however
the focus is on system resilience.
– Security enforcement: papers that approach multiple
security use cases, such as online network monitor-
ing, security testing, zero trust architectures, and secure
embedded solutions.
– Staff management: related to human aspects, behavioral,
emergence awareness, compliance with regulations, and
decision making.
Although one of the practical screening exclusion crite-
ria was to be from the generation/distribution domain, as
explained previously, some papers are not speciﬁc and a
single attribution is not possible. When papers approaching
multiple or all domains were attending the criteria (answer
at least two questions form groups 2, or 3, or 5, and neces-
sarily one from group 4), they were considered relevant for
this research and followed for further analysis.
In Fig.7, graph (a) shows the amount of papers ﬁtting into
each established category before the practical screening and
graph (b) shows the same, but after the quality screening,
where the previously explained quality criteria had to be full
ﬁlled, resulting in a higher quantity of papers on the distri-
bution domain.
The digital twin use cases categorization enabled a quanti-
tative analysis similar to the one performed at [52], contribut-
123


---

Page 13

---

A review on digital twins for power generation and distribution
1183
Fig. 7 Statistics on NIST smart domains after the practical screening
and after the quality screening
Fig. 8 Use cases statics for the distribution domain
Fig. 9 Use cases statics for the generation domain
ing to identify the most relevant use case for two scenarios.
The ﬁrst scenario in Fig.8 groups the categories of “distri-
bution,” “multiple,” and “all” NIST domains, resulting in
“distribution management” as the most relevant use case, fol-
lowed by “fault diagnosis.” But in Fig.9, only use cases from
“generation” domain papers were categorized, changing the
most relevant use case to “fault diagnosis” followed by “per-
formance optimization” and “predictive maintenance.”
5.1.1 Studies design overview and stakeholders
We observed that most selected studies present similar meth-
ods for developing their research work, following a path that
establishes the background on previous works, conceptual-
izing a use case relevant for the paper, and performing a
practical study case as a proof of concept. Although the qual-
ity criteria were developed to collect more technical studies,
implementation details are not always explained, limiting the
understanding of the tools and techniques that may leverage
the application of digital twins.
Regarding stakeholders, only 8 (9,8%) of the studies
approached them and their roles. Some just mention them
brieﬂy [53, 54] as sources for data gathering and sharing,
while when considering larger-scale digital twins, as can be
the case for the distribution domain involving several actors,
we share the opinion of [20] and [55], who support includ-
ing both stakeholders and end-user during the designing and
implementation of digital twins.
Corroborating this rationale, the papers that broadly
approached stakeholders were mainly about the distribution
domain, emphasizing how important it is to enable analy-
sis based on different perspectives and priorities that each
involved stakeholder may have [56]. Similarly, [57] argue
that the digital twin environment must enable these test sce-
narios from different viewpoints, such as induration and
carbon emission. The study [58] was performed by an electri-
cal distribution company in Brazil aiming to develop a power
system digital twin prototype to enable services of anomaly
detection, predictive maintenance, and automated network-
ing modeling. As part of the solution, they built a third-party
platform to share information with stakeholders. An example
of stakeholders was discussed in [59], a use case of beyond
ﬁfth generation (B5G) enabled smart grid, for which stake-
holders range from microgrid owners, resident operators,
utility administrators, prosumers, governments, utilities, and
regulators.
Regarding the generation domain, where most studies
focus on the component level and do not involve many actors,
from an internal perspective stakeholders may be from differ-
ent departments of the same entity [60], such as engineering,
maintenance, management, system architects, and process
engineers.
5.2 Reference architecture
The ﬁndings of reference digital twin architectures from the
energy sector review and the generic architectures discussed
in the related work Sect. 2.3 are very similar, relying on the
common ground of the three basic dimensions: virtual entity,
physical entity, and the link between them. There may be
discrepancies in the designations given to the dimensions,
with some seeing data and services as individual dimensions,
while others view them as subsections of the virtual entity.
For [61], we can express it as a ﬁve-dimension equation with
the physical entity, the virtual entity, services, data, and the
connection. An extra dimension is also considered by [62],
named as the display layer.
To avoid repetitiveness with the previous section on this
topic, only the differences will be discussed, and the most rel-
evant one is that some studies associate the term digital twin
123


---

Page 14

---

1184
J. B. Heluany, V. Gkioulos
Fig. 10 Digital twin architecture that differentiates from the deﬁnition by considering the “digital twin” block mainly as modeling and simulation,
including AI algorithms [34]
only with the layer of modeling and simulation, not with
the physical entity. Interestingly, NASA’s deﬁnition does not
clearly mention it as well, pointing to an additional ﬁnd-
ing of our work about the boundaries of the digital twin,
and whether the physical entity should or not be one of the
architecture blocks. In Figs.10 and 11, it is possible to see
examples of architectures where the block “digital twin” is
associated with modeling and simulation, including AI algo-
rithms.
Many studies depict the architecture and start deﬁning the
functional blocks within the dimensions still considering as
part of the architecture description. In this paper, however,
the tools and building blocks detailing is considered as part
of the framework, which, as deﬁned in a previous section,
is composed of reusable components for application-speciﬁc
features that enable the implementation of an architecture.
The reason for this decision (building blocks within the
framework, not architecture) is based on how the ISA-95
standard and its corresponding Purdue Reference Model
are translated to industrial automation architectures. This
standard deﬁnes a conceptual model for industrial control
systems (ICS) with ﬁve layers, as recalled in Fig.12. The
levels range from ﬁeld equipment (sensors and signals) to
business related level (Enterprise Resource Management).
Based on this standard, most industrial automation archi-
tectures present these same ﬁve layers, showing the main
components of each level without detailing the hardware,
software, and services, but showing how the components are
connected and labeling their role. As an example, a refer-
ence automation architecture was extracted from the PCS7
Siemens catalog [65], where we can see in Fig.13, the corre-
spondence between the levels of the Purdue Reference Model
and this reference automation architecture from PCS7:
– “Field Level” corresponds to Purdue Level 0, showing
the sensors and actuators at production process.
– “Control Level” corresponds to Purdue Levels 1 and 2,
showing the Programmable Logic Controllers for each
system, the switches, computers, gateways, among oth-
ers.
– “Enterprise Level” for Purdue Levels 3 and 4, where the
computers are labeled according to their role in the busi-
nessplanning,logistics,andmanufacturingmanagement.
We believe that the data ﬂow model of the Purdue Refer-
ence Model, which has been available since the 1990s, is still
relevant and enough to detail the main blocks and their cor-
responding components and roles in each level. It is possible
to map this model also to modern IIoT (Industrial Internet
of Things) environments, even considering technical features
such as time constraints, latency and availability, as explained
by AWS [66]. They argue that the use of external resources
should be placed on Purdue Level 2 systems or higher, not for
Level 0–1 systems. This is possible as the response time in
Level 2 is within minutes, compared to seconds in Level 1 and
milli/micro seconds in Level 0. Summarizing, we believe that
an architecture as exempliﬁed in Fig.13 is in accordance with
the deﬁnition considered in this paper, giving room to detail
the building blocks, software, and services in the framework
description.
5.3 Framework and its tools and techniques
The architecture is a hierarchical system that relies on the
coordination of requirements between its layers. As stated
by [67], a digital twin depends on requirements that range
from computational and communication platforms, both with
123


---

Page 15

---

A review on digital twins for power generation and distribution
1185
Fig. 11 Digital twin architectures that differentiate from the deﬁnition
in the following senses: (a) the block “digital twin grid” receives fore-
cast information and returns the states, being possible to infer that it is
basically a static model/simulation tool for the “actual grid” and other
simulations are made outside of this block, in the “data learning center,”
thus not included in the digital twin [63]. Contrasting with (b), different
models, simulation and optimization are included in the “digital twin”
block [64]
Fig. 12 ANSI/ISA-95 hierarchy pyramid of Purdue Reference Model
hardware and software components. We can then see the dig-
ital twin as the set of all its components and their respective
conﬁgurations within and across the layers, which here are
assumed as part of the framework.
Going back to the framework of Fig.4, we will further
explore the four main functional blocks in this section, focus-
ing on similarities and differences found during the relevant
analysis for the energy sector.
5.3.1 Physical entity
This section’s goal is to provide information for the types
of physical entities from the energy sector that have been
addressedintheNISTdomainsselectedforthisstudy.Table4
summarizes the physical entities for the Generation domain
and Table 5 for the set labeled as Distribution, Multiple, and
All.
Attempting to establish a link between the physical enti-
ties for each evaluated domain and the engineering systems
hierarchy, it is possible to infer from Table 4 that, for the
generation domain, most entities are component or subsys-
tem/system level, usually the main generation unity. For
nuclear power the reactor, for solar the photovoltaic con-
version unit, for thermal the steam turbine, for wind power
the wind turbine, and for hydro the generating unity com-
posed of turbine and generator. These entities are aligned
with the most relevant use case identiﬁed as fault diagnosis
for equipment.
For the distribution domain, the physical entities observed
in Table 5 hierarchy are system level, or, as would be called
in other literatures, system of systems, once the distribution
includes all energy sources. Here, the ability to accurately
estimate power demand and generation to balance the grid
is the main feature of the digital twin, also aligning with the
main use case, which is distribution management. Another
interesting ﬁnding speciﬁc to the energy sector is the use of
benchmarks for case studies. Some of the identiﬁed bench-
marks are:
– IEEE 39-bus [95, 96].
– IEEE 9-bus [96].
123


---

Page 16

---

1186
J. B. Heluany, V. Gkioulos
Fig. 13 Automation architecture example extracted from Siemens PCS7 catalog
Table 4 Physical entities modeled in typical actors from generation-related domain
Actor
Physical entities
Hydro
Pressure chamber [68]; generating unity [69]
Nuclear
Reactor core [70]; functional modules of netronic calculations, temperature dynamics, process subsystems, steam generators,
pumps, secondary circuits, and auxiliary systems [71]; microreactor [72];
Solar
Photovoltaic energy conversion unit (PVECU) composed of panel, power converter, and electrical sensors [73]; set of PV
inverters [63]; single-diode model of a single battery [61]; inverter system and weather data [74]; photovoltaic power station
with several panels [75]; photovoltaic solar farm [76]; PV power plant [77]
Thermal
Boiler island, steam turbine island and emission control equipment [78];coal mill and feedwater pump and other key equipment
[79]; key equipment from main subsystems (mechanical, lubrication, water cooling, fuel, exhaust, air intake) [80]; gas turbine
system [81]; high-temperature thermal energy storage device [82]; steam turbine system [60]; gas turbine system [83];
combustion process, air and ﬂue gas system [84]
Wind
Wind turbine power converter [40]; WT with gearbox failure [85]; turbine’s physical system, and weather sensors [86];
direct-drive wind turbine [87]; onshore wind turbines [53]; wind turbine mechanical components [88]; generators, main
shafts, gearboxes, yaw systems, pitch systems, hydraulic systems, racks, and wind turbine control systems [89]
Power plant
Large electrical generators [90]; battery energy storage [91]; auxiliary systems, thermodynamic properties, unit models (heat
exchanger, pump, compressor, boiler, etc.) [92]; boiler system [57]; four generators connected with the grid (Cigré
benchmark) [93]; CEP engine (complex event processing) [94]
– IEEE 33-bus [97].
– Cigré benchmark [93].
5.3.2 Virtual entity modeling
The intention of this section is to enrich the assessment sum-
marized in Table 2. In the reference framework of Fig.4, there
is a functional block for modeling the virtual entity, but not
for simulation. However, we can assume that the simulation
is implicitly included in the service platform. An important
aspect to highlight about the virtual entity is that modeling
and simulation, despite being different functionalities when
represented in a reference architecture/framework, are very
often developed and implemented by the same tools, and
that is the reason why the new tools and techniques iden-
tiﬁed during the systematic literature review are grouped
together:
123


---

Page 17

---

A review on digital twins for power generation and distribution
1187
– Modeling and Simulation tools and techniques: Ter-
moﬂowTM [78], semiautomatic modeling from formal
speciﬁcation [73], OpenFAST (for wind turbine) [40],
DSL (Domain-Speciﬁc Language) [69], gradient boost-
ing regressor and random forest [80], modeling based on
state machine [98], METHONTOLOGY approach [82],
convolution neural network [99], Scikit-learn toolbox
and EnergyPlus [56], Cigré benchmark [93], OpenDSS
[100], KNIME analytics platform [68], AnyLogic [101],
IEEE 39-bus benchmark [95];
Additionally, the engineering hierarchy and the require-
ment for updates during all lifecycle phases interfere with
how the actual entity is modeled and why modeling and sim-
ulating are increasingly intertwined, which might be one of
the essential differences between a digital twin and conven-
tional solutions. Modeling and simulation have been in the
market for a lengthy period, but before, the simulations were
just static models over time. But the need of the market for
predictionstoforeseescenariosandimprovedecisionmaking
has created a space for dynamic models. This way, the previ-
ous physical, mathematical, or logical models are becoming
hybrid and increasingly include data-driven algorithms that
can be regularly updated. Existing component level models
based on equations are still applied. However, when it comes
to system level and its intrinsic high complexity to link all
knowledge domains among its components, hybrid models
gain strength. In this paper, it was noticed that the dynamic
models usually rely on AI and ML for their implementation.
5.3.3 Data management
The examination of the related work showed a greater
focus on data management than the systematic literature
reviews that typically center around single use cases. From
Table 2, where the tools were categorized, three groups were
about data, comprising processing, storage, and analysis. The
framework taken as a reference from Fig.4 shows two sub-
functional blocks within the Data Management Platform,
which are Data Model and Data Management Method. Other
categories found in a nonstructured way throughout the ana-
lyzed papers were related to data acquisition, pre-processing,
storage, and processing.
5.3.4 Services
Services make up another relevant block, also identiﬁed as
one of the architecture’s layers and framework’s functional
block.
Services can be performed online or ofﬂine, depending on
the real-time need for the outcome. Some examples of online
services are visualization, monitoring, alarming, state esti-
mation, protection, and control. Ofﬂine services may include
analysis and assessment, system planning, model validation,
and disturbance analysis.
– Energy sector common services: the services coincide
with what was called previously as use cases. Here, some
are repeated to highlight energy-related services such as
load balancing [56, 63, 64], demand forecasting [56, 59,
118, 126], power ﬂow analysis [55, 55, 63, 97, 101, 103,
113, 116, 119, 129], three-phase short-circuit diagnosis
[129], among others that may be more generic to different
market verticals, such as fault diagnosis, state estimation,
operational planning, and so on.
5.3.5 AI and ML as enabling technologies
A search for terms related to AI and ML on all papers pro-
vided results in 76 studies out of 81, which corresponds to
93,8%. 16 of these (19,7%) approach the topic directly as a
key part of the study.
According to [122], a digital twin is a dynamic virtual
model and, for this reason, they propose a solution that
is updated periodically by inputting new data to a neural
network model used for security assessment purposes. An
important aspect of their work is that there is a bidirectional
communication between the virtual and the real entities and
one parameter of the solution is the time resolution. In this
case, a sub-second delay. Google Tensor Flow was used for
the ofﬂine training, what was also observed in other studies
[56, 59, 68, 80, 91, 96, 117].
Similar to [122] system level approach, but with a different
objective, [56] proposed a management tool for multi-vector
energy systems which evaluates demands, supplies, and stor-
age from different sources, using machine learning to predict
the energy demand when there is a pattern, and artiﬁcial neu-
ral networks in cases where no patterns are found. This was
demonstratedbyanexampleofagovernmentbuilding,show-
ing that it is feasible to optimize energy consumption by
calculating the cost for different scenarios and selecting the
option that best suits the user-deﬁned parameters.
Generic and more theoretical approaches, such as those
proposed by [82] and [114] highlight the trend for utiliz-
ing neural networks and machine learning for the simulation
functionality of digital twins. While [82] proposed a gray
box, deﬁning as partially theoretical with data to complete
the model, and modeled in MATLAB, [114] designed a pure
theoretical modeling engine based on several algebraic equa-
tions. Both proposed the comparison between the simulated
results and the real entity measurements, so that the system
is continuously updated to be as realistic as possible.
When dealing with forecasting situations, many scholars
study a broad range of AI/ML techniques applied to dif-
ferent actors of the power generation domain. A solution
123


---

Page 18

---

1188
J. B. Heluany, V. Gkioulos
Table 5 Physical entities modeled in typical actors from distribution-related domain
Actor
Physical entities
DERs
5 DERs response power [102]; prosumers facility [103]; Battery Energy Storage Systems (BESS) [104]; DER and ESS
(Energy Storage Systems) resources [101]; PV inverters [100]
Electrical Power
Systems
Distribution transformers [105]; 2 level inverters [106]; Gas-insulated Switchgear (GIS) [107]; converter station [99];
communication network [108]
Energy Management
System (EMS)
Power line communication [109]; heating system electriﬁcation in part of the social housing stock and interventions in
the transport sector through increased EV charger installation [56]
Microgrid
IEEE 39-bus benchmark [95]; generic generators from several sources [110]; energy units (solar, wind or conventional
generator) [111]; distribution controllers [112]
Power Flow
Carbon neutrality-focused systems [113]; control room EMS (Energy Management System) [114]; general power
system components of single or multiple loads and their sensors [115]; multi-energy ﬂow including electricity, heat,
gas, and hydrogen [116]; control center system [55]; IEEE 9-bus and IEEE 39-bus benchmark power systems [96]
Pricing
Transformers, wind turbines, solar panels, CHP systems, TESs, boilers and Evs [117]
Smart Grid
Smart meter devices, controller units, storage units, and analytics applications for network management and monitoring
[64]; distribution transformer, smart meters [118]; transmission line, transformer, controllers, circuit breakers [119];
medium voltage feeder, transformer, measuring devices [120]; energy providers [121]; dispatching control center
SCADA [122]; energy providers and stakeholders [59];generic power equipment [123]; DERs and DSOs [124];
synthetic NEM (S-NEM2300) composed of power stations, substations, wind farms, and transmission lines [54];
end-users platform of consumption monitoring [52]; control center system [67]
Substation
Substation module, equipment supervision module, and personnel positioning module [125]; medium and low voltage
distribution network [126]; converter system [127]; regional multi-energy system integrating hydroelectric, wind
power, photovoltaic, combined cooling, heating and power, energy storage, and electric vehicle charging facilities
[128]; substation components [129]; MV/LV transformers, and grid cables [58]; primary equipment and sensors of the
substation [98]; transfer switches, PMUs, power transformers, energy meters and sensors [130]; IEDs, RTUs, control
room [131]; IEEE 33 node distribution power system with photovoltaic arrays, wind generators, and circuit breakers
[97]; terminal equipment of distribution network [62]; PV loads, transformers, cables [132]
with Microsoft Azure platform based on deep learning was
developed by [53], using temporal convolution and k-nearest
approaches to predict the generated power given the wind
speed estimation for a wind turbine. Following a similar con-
text, [61] developed a digital twin to support decision making
for power grid dispatching of wind power farms, using data
mining and artiﬁcial intelligence technology to achieve out-
put forecast of new energy ﬁeld groups. In the case of hydro
source, [68] predicted the pressure of the oscillating water
column using machine learning.
Other applications may include anomalies detection of
different natures. [76], for example, studied solar farms and
proposed a digital twin based approach to detect anoma-
lies of the physical system. The technique used for the time
series simulation was deep learning, more speciﬁcally auto-
encoders.
5.4 Network and binding
The aim of the research questions focusing on network is
to better understand the bidirectional communication that is
described in most deﬁnitions. Given that one of the quality
screening inclusion criteria was that the paper should nec-
essarily mention the communication, all studies analyzed
approach the networking to some degree. The need to state
the communication as bidirectional may be to differentiate
from other traditional unidirectional solutions that are man-
ually or automatically connected from the physical entity
to the virtual one. From [64] “a bidirectional communica-
tion platform for real-time continuous data management with
high availability is essential,” but the authors gave no details
explaining what exactly is shared, what are the operational
requirements, and how this channel affects the solution. In
[107], the authors afﬁrm that the process is bidirectional and
that the real-time communication allows the synchronization
between the virtual and real entities.
According to computer science terminology, this intercon-
nection that couples data sources and synchronizes them is
called binding, a term that is not common in the literature
(used only in 4 out of 81 papers), but the term “synchroniza-
tion” and stemmed words is present in many studies, 41 out
of 81. This data sharing for synchronization relies on the goal
of updating the digital twin throughout the lifecycle of the
real system, allowing the services to be more reliable, thus
improving decision making.
Attempting to comprehend the necessary features of this
communication, some of the use cases were assessed to iden-
tifythenatureofthedataexchange.For[56],themodelstates,
set-points and forecasts are updated. Similarly, in [78] the
operating performance of a thermal power plant is extracted
and shared with the virtual platform, and in [111], the live
states are updated when a change happens. An example
123


---

Page 19

---

A review on digital twins for power generation and distribution
1189
refers to solar power plants transmitting irradiance, voltage,
frequency, and settings back to the real system at every sim-
ulation cycle [100].
For the physical implementation of the communication
channel, a wide range of technologies can be applied, as
shown previously in Table 2. The technologies explored here
are complimentary and may guide to more energy-related
implementations:
– FPGA (Field Programmable Gate Array): in [73] they
justify the use of an Artix-7 FPGA due to higher speed
and resources performance for the digital twin estimator
of a PV cell. We found other applications in [106], where
an FPGA was utilized to emulate the physical hardware
ﬁrmware, and to program the behavioral model of wind
turbines in [87].
– Raspberry Pi: similarly to FPGA, some studies applied
Raspberry Pi to implement the RTUs (Remote Terminal
Unity)betweenthephysicalandvirtualentities[111,112,
132];
– SCADA: Interestingly, 31 studies mention some sort of
connection with records from the Supervisory Control
and Data Acquisition (SCADA) system. SCADA sys-
tems can provide multivariate time series data that allows
the modeling of the system, and continuous parameters
update [119]. According to [80], any industrial sector
can adapt SCADA supervisors to establish data exchange
between the physical and virtual entities.
– Industrial Fieldbus: getting data from the ﬁeld usually
requires compatibility features where communication
protocols play an important role. Examples given by
[107] include Modbus, Industrial Ethernet, optical ﬁber
networks, among others for the collection, and MQTT,
HTTPS, RPC for transmission. Adding to the collection
protocols, besides Modbus, [100] communicates with
DERs using also DNP3 and proprietary protocols, [81]
established a communication interface with Proﬁbus to
integrate a gas turbine DCS with a PC based digital twin
platform. In the context of the distribution domain, other
common protocols are IEC 61850 [54, 55, 95, 107, 114,
130].
5.5 Security
From the research questions in the group entitled Security, it
is possible to see that the initial goal was to understand this
topic in different layers of the digital twin, starting from the
security of the digital twin itself, then of the communication
intra and inter systems, and any other layer and/or applica-
tion that could be approaching security. During the papers
analysis of the systematic literature review, the ﬁnding from
the ﬁrst review discussed in Sect. 2.5 was reinforced, that
security is not a main topic in the use cases and, even when it
is mentioned, it is not possible to answer the four questions.
Naturally, if the query for the papers collection focused on
security, many other studies would have appeared for evalua-
tion, but the energy restriction on our query limits the results
to provide a feasible reading work and restrict the market
vertical. For this reason, the ﬁndings about security were
grouped regardless of the research questions to provide an
overview of how it is being approached and what are the
gaps, being the ﬁrst identiﬁed gap the lack of focus on secu-
rity.
Using the words from [64], although “a digital twin can
both provide and undermine security based on its deploy-
ment,”fromthe81papersunderanalysis,onlythreeapproach
security directly [64, 95, 106], while others discuss brieﬂy or
just mention. From an application perspective, when secu-
rity is the main topic, it is deployed as a security layer not
focusing on the security of the digital twin itself, as can be
seen in the following studies description.
Approaching smart grid security with digital twins, [64]
argue that this sector lacks of security standardization and
propose a digital twin structure with a framework consisting
of a virtual entity, cyber-threat intelligence database for grid-
speciﬁc attacks, simulation of attacks, and data analysis to
perform vulnerability and risk assessment. All these layers
would be continuously updated, including the latest attack
vectors, to provide better security evaluation.
In a smaller scale, [95] focused on microgrids in a project
entitled ANGEL (Automatic Network Guardian for ELectri-
cal systems) where the digital twin framework sophistication
is stated as level III, with physics-based simulation, phys-
ical system, and adaptive GUI, but not machine learning,
which would characterize it as level IV. For their proof of
concept, the IEEE 39-bus benchmark was modeled in MAT-
LAB/Simulink and tested with a three-phase fault in the
physical system that is alarmed in the digital twin when a
divergence is noticed. Based on this result, the authors defend
that the solution could also be applied for security cases such
as false data injection, denial-of-service, topology attack, and
vulnerabilities in general.
A more speciﬁc application still focused on grid devices
was developed by [106] with embedded security in the con-
trol and hardware layers. The aim was to emulate and verify
hardware patchings in the digital twin before applying them
to the real devices. An FPGA was utilized together with
LabVIEW to allow the interface during the Hot-Patching
operation, adding a protection layer before the real imple-
mentation.
6 Discussion and contributions
This section will address the contributions provided by this
work by discussing them according to the groups of the
123


---

Page 20

---

1190
J. B. Heluany, V. Gkioulos
research questions (use cases, architectures, frameworks and
tools, network and binding, and security). By ﬁrst approach-
ing the digital twin conceptualization regardless of the
market, we could compare it with energy-related studies
showing how it is progressing in this critical infrastructure
sector.
Domain-speciﬁc use cases: one of the gaps identiﬁed in
the related studies and also from our review studies selec-
tion was the lack of smart grid domain-speciﬁc use cases.
Even though the application domains are common sense,
few studies address it in a quantitative way. For this rea-
son, we categorized the use cases for the generation and
distribution domains for all the 81 papers and quantiﬁed the
amount resulting in the most relevant ones. The criteria used
to categorize the actors was explained in the “SLR Analy-
sis,” 5.1, being easily reproducible in case other researches
want to perform this statistics. By doing the statistical analy-
sis, we were able to indicate that the progress of digital twins
in the energy sector regarding distribution and generation
domains are, respectively, fault diagnosis, and distribution
management. Moreover, we further investigated what were
the physical entities of each actor, providing a comprehensive
list in Tables 5 and 4.
Architectures, Frameworks, and Tools: from the com-
parison with the broad conceptualization, we identiﬁed a
difference between the most accepted deﬁnition and how
the energy-related studies establish the digital twin bound-
aries represented in architectures: while NASA’s deﬁnition
includes the real entity, services, data management, and vir-
tual entity, most analyzed studies label as digital twin only
the virtual entity, which is translated most of the times as the
modeling and simulation block. Therefore, it shows the need
for consensus regarding the digital twin boundaries when
representing it in an architecture or a framework.
We noticed that the issue presented in the related studies
about the interchangeable use of the terms “architecture” and
“framework” repeated itself in our data set. Thus, we con-
tributed with a new perspective based on the well-established
Purdue model applied to reference automation architectures
showing how it relates major suppliers, e.g., Siemens, high-
lighting how a framework is expected to differ from an
architecture by detailing tools and reusable blocks.
Turning now to the tools, it was performed a compre-
hensive compilation divided into categories: bridging, data
processing, data storage, data analytics, modeling, and simu-
lation. Naturally there are overlaps of tools that are applicable
to more than one category, but the idea is to provide an
overview and serve as consulting material for the choice
of market solutions. It is also worth noticing that the set of
tools might change according to the use or the researchers
approach. For example, a use case of wind turbines can
make use of OpenFAST, or utilize MATLAB or Labview for
the modeling and simulation. One of the limitations of this
discussionisthatthepapersevaluatedlackeddetailsofimple-
mentation, decreasing the understanding of the technical
challenges for tools selection and utilization. Interestingly,
AI and ML are mentioned by 90% of the papers, which may
be related to the dynamic nature of modeling in digital twins
when compared to traditional static models.
Network and Binding: the evaluation of the questions
related to the network and bidirectional communication,
resultedinshowingthattheterm“synchronization”isapplied
than “binding,” appearing in approximately 50% of the
studies. This was an unexpected ﬁnding given that the bidi-
rectional communication is part of the digital twin deﬁnition
and yet not well explored. Even when mentioning synchro-
nization it is not often discussed in terms of shared values,
latency issues, security issues, and so on. Thus, our con-
tribution was limited, but it was possible to identify some
variables speciﬁc to the energy sector such as states, set-
points, weather forecasts, performance indicators, voltage,
frequency, current, among others.
Security: no signiﬁcant information was found about the
security of the digital twin itself or its application as a security
layer, showing a gap in this ﬁeld for energy-related studies.
Evenbeingawareofourresearchlimitationduetothemarked
ﬁlter that could exclude papers only about the cybersecurity
of digital twins, taking into consideration that smart grids are
critical infrastructures that might require security measures
by law, it was expected to ﬁnd more information on how it is
being addressed.
7 Challenges and future work
Before stating challenges and future work, it is important
to highlight some of the limitations that may inﬂuence how
the research questions were answered. For our systematic lit-
erature review, we considered only studies from the energy
sector that followed a combination of the research questions.
This decision may have limited or even excluded papers that
detail digital twins in regard to the technical topics covered
(architecture, framework, stakeholders, network, and secu-
rity). During the analysis, we noticed that many layers of the
digital twin still lack more consistency in deﬁnitions, tools,
and applications to allow more real-world applications. This
starts with the lack of consensus for the term deﬁnition itself,
which may lead to a misuse of terminology and impacting
how other layers are deﬁned and implemented. Moving to the
implementation, the gaps found about the lack of focus on
detailed architecture and framework, security, stakeholders,
andnetworkintegrationwouldbeanaturalprogressionofthis
work. The next step of this research will focus on proposing
an architecture and framework that takes into consideration
the speciﬁc needs of the energy sector.
123


---

Page 21

---

A review on digital twins for power generation and distribution
1191
8 Conclusion
On the question of the digital twin deﬁnition, this study rein-
forced that there is a misconception. We discussed some
reasons like the utilization of broad terms such as “ultra-
realistic,” “mirror,” and “system” and proposed using the
concept of systems engineering design hierarchy to better
translate what is the real entity and what knowledge domains
will be addressed in the virtual entity.
When evaluating use cases according to smart grid
domains as deﬁned by NIST, the collaboration comes from
ﬁnding the most relevant use case for the two domains chosen
as scope, being distribution management for the distribu-
tion domain studies, and fault diagnosis for the generation
domain. Still, for the generation domain, another ﬁnding that
stands out from the results is that few studies address hydro
power plants. Given the energy transition and considering
that this energy source is renewable and composes a great
percentage of power generation, it was expected to be the
main focus in more papers. According to the World Eco-
nomic Forum [133], countries such as China, Brazil, Canada,
USA, Russia, and Norway are among the ones who produce
most hydroelectric power.
Taking into consideration the recent cyber-attack cases in
critical infrastructures, one unanticipated result was that no
focus is given to the security of the digital twin itself. Few
papers address security, and when they do, the digital twin
role is an additional security layer, without further discus-
sions on the vulnerabilities that it may add to the system.
There are additional aspects that could possibly be advan-
tageous in discovering any deﬁciencies for digital twin
execution, pertaining to both technical and human elements.
The bidirectional communication was stated to be present in
all selected papers, but requires deeper exploration of what
is shared and how the outcomes of the digital twin go back
to the real system. From the studies, the data exchange from
the real entity to the virtual one is clear, and usually used
to create and update the models that are further used for the
simulations. In turn, the simulations result provide informa-
tion that guide better decision making, regardless of the use
case. However, the human–machine interface that displays
the results is not necessarily the same as in the real system, so
the communication could be unidirectional only. None of the
studies stated an autonomous feedback that impacted the sys-
tem automatically. Moreover, given that the use cases allow
better decision making, it was expected that also the stake-
holders would be more present in the discussions, but who
are the stakeholders, what are their roles, and how each of
them have access to the information is commonly discussed.
The present results show interesting ﬁndings not only for
the energy sector, where use cases and gaps were identiﬁed,
but also for gaps related to the architecture, framework, net-
work, and human aspects involving decision making.
Acknowledgements *We would like to express our gratitude to Lama
Amro, the laboratory assistant at IIK, NTNU, who assisted on the steps
of practical and quality screening.
Author Contributions JBH and VG were involved in writing. VG was
involved in supervision. All authors have read and agreed to the pub-
lished version of the manuscript.
Funding Open access funding provided by NTNU Norwegian Univer-
sity of Science and Technology (incl St. Olavs Hospital - Trondheim
University Hospital). This work has received funding from the Research
Council of Norway through the SFI Norwegian Centre for Cybersecu-
rity in Critical Sectors (NORCICS) project no. 310105.
Open Access This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing, adap-
tation, distribution and reproduction in any medium or format, as
long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons licence, and indi-
cate if changes were made. The images or other third party material
in this article are included in the article’s Creative Commons licence,
unless indicated otherwise in a credit line to the material. If material
is not included in the article’s Creative Commons licence and your
intended use is not permitted by statutory regulation or exceeds the
permitteduse,youwillneedtoobtainpermissiondirectlyfromthecopy-
right holder. To view a copy of this licence, visit http://creativecomm
ons.org/licenses/by/4.0/.
References
1. CISA,
Energy
sector.
https://www.cisa.gov/topics/critical-
infrastructure-security-and-resilience/critical-infrastructure-
sectors/energy-sector
2. Gopstein, A., Nguyen, C., O’Fallon, C., Hastings, N., Wollman,
D.A.: Nist framework and roadmap for smart grid interoperability
standards, release 4.0 (2021-02-18 00:02:00 2021). https://doi.
org/10.6028/NIST.SP.1108r4
3. Ketter, W., Collins, J., Saar-Tsechansky, M., Marom, O.: Infor-
mation systems for a smart electricity grid: emerging challenges
and opportunities. ACM Trans. Manage. Inf. Syst. (TMIS) 9(3),
1–22 (2018)
4. Nguyen, S., Abdelhakim, M., Kerestes, R.: Survey paper of digital
twins and their integration into electric power systems, In: 2021
IEEE Power and Energy Society General Meeting (PESGM), pp.
01–05. https://doi.org/10.1109/PESGM46819.2021.9638011
5. Ardeshiri, A., Lotﬁ, A., Behkam, R., Moradzadeh, A., Barzkar,
A.: Introduction and literature review of power system challenges
and issues, Application of machine learning and deep learning
methods to power system problems, 19–43 (2021)
6. SmartGrid.gov, Ethe smart grid. https://www.smartgrid.gov/the_
smart_grid/smart_grid.html
7. GT17, Technology trends 2017 (2017). https://www.gartner.com/
smarterwithgartner/gartners-top-10-technology-trends-2017
8. GT18, Technology trends2018 (2018) https://www.gartner.com/
smarterwithgartner/gartner-top-10-strategic-technology-trends-
for-2018
9. GT19, Technology trends 2019 (2019) https://www.gartner.com/
smarterwithgartner/gartner-top-10-strategic-technology-trends-
for-2019
10. GT20,
Gartner20
(2020)
https://www.gartner.com/
smarterwithgartner/gartner-top-10-strategic-technology-trends-
for-2020
11. Uhlenkamp, J.F., Hauge, J.B., Broda, E., Lütjen, M., Freitag, M.,
Thoben, K.D.: Digital twins: a maturity model for their classi-
123


---

Page 22

---

1192
J. B. Heluany, V. Gkioulos
ﬁcation and evaluation. IEEE Access 10, 69605–69635 (2022).
https://doi.org/10.1109/ACCESS.2022.3186353
12. Vasiljevska, J., Gangale, F., Covrig, L., Mengolini, A.: Smart
grids and beyond ? An EU research and innovation perspective,
Scientiﬁc analysis or review KJ-NA-30786-EN-N (online), Lux-
embourg (Luxembourg) (2021). https://doi.org/10.2760/705655
(online)
13. Grieves, M., Vickers, J.: Digital twin: mitigating unpredictable,
undesirable emergent behavior in complex systems. In: Transdis-
ciplinary perspectives on complex systems, pp. 85–113. Springer,
Berlin (2017)
14. Negri, E., Fumagalli, L., Macchi, M.: A review of the roles of
digital twin in cps-based production systems. Proc. Manuf. 11,
939–948 (2017). https://doi.org/10.1016/j.promfg.2017.07.198
15. Barricelli, B.R., Casiraghi, E., Fogli, D.: A survey on digital twin:
deﬁnitions, characteristics, applications, and design implications.
IEEE Access 7, 167653–167671 (2019). https://doi.org/10.1109/
ACCESS.2019.2953499
16. Semeraro, C., Lezoche, M., Panetto, H., Dassisti, M.: Digital
twin paradigm: a systematic literature review. Comput. Ind. 130,
103469 (2021). https://doi.org/10.1016/j.compind.2021.103469
17. Perno, M., Hvam, L., Haug, A.: Implementation of digital twins
in the process industry: a systematic literature review of enablers
and barriers. Comput. Ind. 134, 103558 (2022). https://doi.org/
10.1016/j.compind.2021.103558
18. Liu, M., Fang, S., Dong, H., Xu, C.: Review of digital twin about
concepts, technologies, and industrial applications. J. Manuf.
Syst. 58, 346–361 (2021). https://doi.org/10.1016/j.jmsy.2020.
06.017
19. Sjarov, M., Lechler, T., Fuchs, J., Brossog, M., Selmaier, A.,
Faltus, F., Donhauser, T., Franke, J.: The digital twin concept
in industry - a review and systematization, In 2020 25th IEEE
International Conference on Emerging Technologies and Factory
Automation (ETFA), Vol. 1, pp. 1789–1796 (2020). https://doi.
org/10.1109/ETFA46521.2020.9212089
20. Jones, D., Snider, C., Nassehi, A., Yon, J., Hicks, B.: Charac-
terising the digital twin: a systematic literature review. CIRP J.
Manuf. Sci. Technol. 29, 36–52 (2020). https://doi.org/10.1016/
j.cirpj.2020.02.002
21. Ardebili, A.A., Longo, A., Ficarella, A.: Digital twin (dt) in smart
energy systems-systematic literature review of dt as a growing
solution for energy internet of the things (eiot), In E3S Web of
Conferences, Vol. 312, EDP Sciences, p. 09002 (2021)
22. Tao, F., Zhang, H., Liu, A., Nee, A.Y.C.: Digital twin in industry:
state-of-the-art. IEEE Trans. Ind. Inf. 15(4), 2405–2415 (2019).
https://doi.org/10.1109/TII.2018.2873186
23. Fuller, A., Fan, Z., Day, C., Barlow, C.: Digital twin: enabling
technologies, challenges and open research. IEEE Access 8,
108952–108971 (2020). https://doi.org/10.1109/ACCESS.2020.
2998358
24. Mylonas, G., Kalogeras, A., Kalogeras, G., Anagnostopoulos, C.,
Alexakos, C., Muñoz, L.: Digital twins from smart manufacturing
to smart cities: A survey. IEEE Access 9, 143222–143249 (2021).
https://doi.org/10.1109/ACCESS.2021.3120843
25. Balijepalli, V.M., Sielker, F., Karmakar, G.: Evolution of power
system cim to digital twins-a comprehensive review and analysis.
In 2021 IEEE PES Innovative Smart Grid Technologies Europe
(ISGT Europe), pp. 1–6 (2021)
26. Rathore, M.M., Shah, S.A., Shukla, D., Bentafat, E., Bakiras, S.:
The role of AI, machine learning, and big data in digital twin-
ning: a systematic literature review, challenges, and opportunities.
IEEE Access 9, 32030–32052 (2021). https://doi.org/10.1109/
ACCESS.2021.3060863
27. Pronost, G., Mayer, F., Marche, B., Camargo, M., Dupont, L.:
Towards a framework for the classiﬁcation of digital twins and
their applications, In 2021 IEEE International Conference on
Engineering, Technology and Innovation (ICE/ITMC), pp. 1–7
(2021). https://doi.org/10.1109/ICE/ITMC52061.2021.9570114
28. Glaessgen,
E.,
Stargel,
D.:
The
digital
twin
paradigm
for
future
nasa
and
us
air
force
vehicles,
In
53rd
AIAA/ASME/ASCE/AHS/ASC Structures, Structural Dynamics
and Materials Conference 20th AIAA/ASME/AHS Adaptive
Structures Conference 14th AIAA, p. 1818 (2012)
29. Kuehner, K.J., Scheer, R., Strassburger, S.: Digital twin: ﬁnding
common ground—a meta-review. Proc. CIRP 104, 1227–1232
(2021). https://doi.org/10.1016/j.procir.2021.11.206
30. Kritzinger, W., Karner, M., Traar, G., Henjes, J., Sihn, W.: Digital
twin in manufacturing: a categorical literature review and classi-
ﬁcation. IFAC-PapersOnLine 51(11), 1016–1022 (2018)
31. Kossiakoff, A., Biemer, S.M., Seymour, S.J., Flanigan, D.A.: Sys-
tems Engineering Principles and Practice. John Wiley & Sons,
New Jersey (2020)
32. Melesse, T.Y., Pasquale, V.D., Riemma, S.: Digital twin models in
industrial operations: a systematic literature review. Proc. Manuf.
42, 267–272 (2020). https://doi.org/10.1016/j.promfg.2020.02.
084
33. Zhang, H., Ma, L., Sun, J., Lin, H., Thürer, M.: Digital twin in
services and industrial product service systems: review and analy-
sis.Proc.CIRP 83,57–60(2019).https://doi.org/10.1016/j.procir.
2019.02.131
34. Aghazadeh Ardebili, A., Longo, A., Ficarella, A.: Digital
twins bonds society with cyber-physical energy systems: a lit-
erature review, In 2021 IEEE International Conferences on
Internet of Things (iThings) and IEEE Green Computing and
Communications (GreenCom) and IEEE Cyber, Physical and
Social Computing (CPSCom) and IEEE Smart Data (Smart-
Data) and IEEE Congress on Cybermatics (Cybermatics), pp.
284–289
(2021).
https://doi.org/10.1109/iThings-GreenCom-
CPSCom-SmartData-Cybermatics53846.2021.00054
35. van Dinter, R., Tekinerdogan, B., Catal, C.: Predictive main-
tenance using digital twins: a systematic literature review. Inf.
Softw. Technol. 151, 107008 (2022). https://doi.org/10.1016/j.
infsof.2022.107008
36. Core
concepts
(2023).
https://pubs.opengroup.org/togaf-
standard/introduction/chap03.html
37. Cavaness, C., Keeton, B.: Jakarta Struts pocket reference,
“O’Reilly Media, Inc.” (2003)
38. Josifovska, K., Yigitbas, E., Engels, G.: Reference framework for
digital twins within cyber-physical systems, In 2019 IEEE/ACM
5th International Workshop on Software Engineering for Smart
Cyber-Physical Systems (SEsCPS), pp. 25–31 (2019). https://doi.
org/10.1109/SEsCPS.2019.00012
39. Heluany, J.B., Galvão, R.: IEC 62443 standard for hydro power
plants. Energies 16(3), 1452 (2023)
40. Sivalingam, K., Sepulveda, M., Spring, M., Davies, P.: A review
and methodology development for remaining useful life pre-
diction of offshore ﬁxed and ﬂoating wind turbine power con-
verter with digital twin technology perspective, In 2018 2nd
International Conference on Green Energy and Applications
(ICGEA), pp. 197–204 (2018). https://doi.org/10.1109/ICGEA.
2018.8356292
41. Löcklin, A., Müller, M., Jung, T., Jazdi, N., White, D., Weyrich,
M.: Digital twin for veriﬁcation and validation of industrial
automation systems—a survey, In 2020 25th IEEE International
Conference on Emerging Technologies and Factory Automation
(ETFA), Vol. 1, pp. 851–858 (2020). https://doi.org/10.1109/
ETFA46521.2020.9212051
42. Perno, M., Hvam, L., Haug, A.: Enablers and barriers to the imple-
mentation of digital twins in the process industry: A systematic
literature review, In IEEE International Conference on Industrial
Engineering and Engineering Management (IEEM), pp. 959–964
(2020). https://doi.org/10.1109/IEEM45057.2020.9309745
123


---

Page 23

---

A review on digital twins for power generation and distribution
1193
43. Nguyen-Huu, T.A., Tran, T.T., Tran, M.Q., Nguyen, P.H.,
Slootweg, J.: Operation orchestration of local energy commu-
nities through digital twin: a review on suitable modeling and
simulation approaches, In: 2022 IEEE 7th International Energy
Conference (ENERGYCON), pp. 1–6. https://doi.org/10.1109/
ENERGYCON53164.2022.9830264
44. Fu, Y., Huang, Y., Hou, F., Li, K.: A brief review of digital twin in
electric power industry, In 2022 IEEE 5th International Electrical
and Energy Conference (CIEEC), pp. 2314–2318. https://doi.org/
10.1109/CIEEC54735.2022.9846081
45. Digital twin (dt) in smart energy systems - systematic literature
review of dt as a growing solution for energy internet of the things
(eiot) (2021) https://doi.org/10.1051/e3sconf/202131209002
46. Balijepalli, V. M., Sielker, F., Karmakar, G.: Evolution of power
system cim to digital twins - a comprehensive review and
analysis, In 2021 IEEE PES Innovative Smart Grid Technolo-
gies Europe (ISGT Europe), pp. 1–6. https://doi.org/10.1109/
ISGTEurope52324.2021.9640174
47. Brosinsky, C., Kummerow, A., Richter, M., Naumann, A., Wiest,
P., Nicolai, S., Westermann, D.: The role of digital twins in power
system automation and control: necessity, requirements, and ben-
eﬁts. In ETG Congress, pp. 1–6 (2021)
48. Cui, Y., Xiao, F., Wang, W., He, X., Zhang, C., Zhang, Y.: Digital
twin for power system steady-state modelling, simulation, and
analysis, In 2020 IEEE 4th Conference on Energy Internet and
Energy System Integration (EI2), pp. 1233–1238. https://doi.org/
10.1109/EI250167.2020.9346850
49. Onile, A.E., Machlev, R., Petlenkov, E., Levron, Y., Belikov, J.:
Uses of the digital twins concept for energy services, intelli-
gent recommendation systems, and demand side management:
A review. Energy Rep. 7, 997–1015 (2021). https://doi.org/10.
1016/j.egyr.2021.01.090
50. Fink, A.: Conducting Research Literature Reviews: From the
Internet to Paper. Sage publications, Thousand Oaks (2014)
51. Okoli, C.: A guide to conducting a standalone systematic literature
review. Commun. Assoc. Inf. Syst. 37(1), 43 (2015)
52. Martin Lopo, M.M., Boal, J., Sanchez Miralles, A.: Transitioning
from a meta-simulator to electrical applications: an architecture.
Simul. Model. Pract. Theory 94, 177–198 (2019). https://doi.org/
10.1016/j.simpat.2019.02.007
53. Fahim, M., Sharma, V., Cao, T.V., Canberk, B., Duong, T.Q.:
Machine learning-based digital twin for predictive modeling in
wind turbines. IEEE Access 10, 14184–14194 (2022). https://doi.
org/10.1109/ACCESS.2022.3147602
54. Arrano-Vargas, F., Konstantinou, G.: Modular design and real-
time simulators toward power system digital twins implementa-
tion. IEEE Trans. Ind. Inf. (2022). https://doi.org/10.1109/TII.
2022.3178713
55. Marot, A., Kelly, A., Naglic, M., Barbesant, V., Cremer, J.,
Stefanov, A., Viebahn, J.: Perspectives on future power system
control centers for energy transition. J. Modern Power Syst. Clean
Energy 10(2), 328–344 (2022). https://doi.org/10.35833/MPCE.
2021.000673
56. O’Dwyer, E., Pan, I., Charlesworth, R., Butler, S., Shah, N.:
Integration of an energy management tool and digital twin for
coordination and control of multi-vector smart energy systems.
Sustain. Cities Soc. 62, 102412 (2020). https://doi.org/10.1016/j.
scs.2020.102412
57. Amar, B., Subhrojyoti, R.C., Barnali, B., Dhakshinamoorthy,
R., Seenivasan, A., Naveenkumar, S.: Knowledge driven rapid
development of white box digital twins for industrial plant sys-
tems, In IECON 2021 - 47th Annual Conference of the IEEE
Industrial Electronics Society, pp. 1–6. https://doi.org/10.1109/
IECON48115.2021.9589912
58. Fernandes, S.V., João, D.V., Cardoso, B.B., Martins, M.A.I.,
Carvalho, E.G.: Digital twin concept developing on an electri-
cal distribution system-an application case. Energies 15(8), 2836
(2022). https://doi.org/10.3390/en15082836
59. Lopez, J., Rubio, J.E., Alcaraz, C.: Digital twins for intelligent
authorization in the b5g-enabled smart grid. IEEE Wirel. Com-
mun. 28(2), 48–55 (2021). https://doi.org/10.1109/MWC.001.
2000336
60. Ghita, M., Benhadou, S., Hicham, M., Mounaam, A.: Ht-tpp: a
hybrid twin architecture for thermal power plant collaborative
condition monitoring. Energies 15, 5383 (2022). https://doi.org/
10.3390/en15155383
61. Shen, R., Wang, Y., Ma, M., Zhou, Q., Lyu, Q., Zhang, J.: Appli-
cation of digital twin technology in auxiliary decision-making
system for grid-connected dispatching of new energy. J. Phys.
Conf. Ser. 2202(1), 012045 (2022). https://doi.org/10.1088/1742-
6596/2202/1/012045
62. Zijian, Z., Jiaxin, L., Tie, G., Guanyu, W., Defu, W., Shiqing,
W.: Fault prediction of distribution terminal equipment based
on entropy weight vague matter-element under the digital twin
framework, In 2021 6th International Conference on Robotics
and Automation Engineering (ICRAE), pp. 195–199. https://doi.
org/10.1109/ICRAE53653.2021.9657779
63. Jung, Y., Han, C., Lee, D., Song, S., Jang, G.: Adaptive volt-var
control in smart pv inverter for mitigating voltage unbalance at pcc
using multiagent deep reinforcement learning. Appl. Sci. 11(19),
8979 (2021). https://doi.org/10.3390/app11198979
64. Atalay, M., Angin, P.: A digital twins approach to smart grid
security testing and standardization. In 2020 IEEE International
Workshop on Metrology for Industry 4.0 and IoT, pp. 435–440.
https://doi.org/10.1109/MetroInd4.0IoT48571.2020.9138264
65. Simatic pcs7 (2018) https://cache.industry.siemens.com/dl/ﬁles/
406/109766406/att_981146/v1/br_simatic_pcs7_en_2017_Web.
pdf
66. Mapping to the ISA-95 model (2023) https://docs.aws.amazon.
com/whitepapers/latest/industrial-iot-architecture-patterns/
mapping-to-the-isa-95-model.html
67. Semenkov, K., Promyslov, V., Poletykin, A., Mengazetdinov, N.:
Validation of complex control systems with heterogeneous digital
models in industry 4.0 framework †. Machines (2021). https://doi.
org/10.3390/machines9030062
68. Seo, D., Huh, T., Kim, M., Oh, J.W., Cho, S.G., Jeong, S.C.: A pre-
dictive model for oscillating water column wave energy converters
based on machine learning. ICIC Express Lett. Part B Appl. 12(8),
733–740 (2021). https://doi.org/10.24507/icicelb.12.08.733
69. Zhao, Z., Li, D., She, J., Zhang, H., Zhou, Y., Zhao, L.: Construc-
tion and application of digital twin model of hydropower plant
based on data-driven, In 2021 3rd International Workshop on Arti-
ﬁcial Intelligence and Education (WAIE), pp. 60–64. https://doi.
org/10.1109/WAIE54146.2021.00020
70. Jharko, E.: Digital twin of npps: Simulation systems and
veriﬁcation. In 2021 International Russian Automation Con-
ference (RusAutoCon), pp. 852–857. https://doi.org/10.1109/
RusAutoCon52004.2021.9537546
71. Jharko, E.: Digital twin of the technological process of the npp
power unit. In 2021 14th International Conference Management
of large-scale system development (MLSD), pp. 1–5. https://doi.
org/10.1109/MLSD52249.2021.9600212
72. Garcia, H.E., Aumeier, S.E., Al-Rashdan, A.Y., Rolston, B.L.:
Secure embedded intelligence in nuclear systems: framework and
methods. Ann. Nucl. Energy 140, 107261 (2020). https://doi.org/
10.1016/j.anucene.2019.107261
73. Jain, P., Poon, J., Singh, J.P., Spanos, C., Sanders, S.R., Panda,
S.K.: A digital twin approach for fault diagnosis in distributed
photovoltaic systems. IEEE Trans. Power Electron. 35(1), 940–
956 (2020). https://doi.org/10.1109/TPEL.2019.2911594
74. Tuomiranta,A.,Horvath,I.,Schils,A.,Brabandere,K.,Voroshazi,
E., Bertrand, E., Aldalali, B., Gordon, I., Wabbes, A., Scheerlinck,
123


---

Page 24

---

1194
J. B. Heluany, V. Gkioulos
S.: Auto-Parametrizing the Digital Twin of Photovoltaic Power
Systems (2021). https://doi.org/10.4229/EUPVSEC20212021-
5DO.1.4
75. Liu, J., Lu, X., Zhou, Y., Cui, J., Wang, S., Zhao, Z.: Design of
photovoltaic power station intelligent operation and maintenance
system based on digital twin. In 2021 6th International Conference
on Robotics and Automation Engineering (ICRAE), pp. 206–211.
https://doi.org/10.1109/ICRAE53653.2021.9657759
76. Berlanga, R.: Digital twins in solar farms: an approach through
time series and deep learning. Algorithms 14(5), 156 (2021).
https://doi.org/10.3390/a14050156
77. Livera, A., Paphitis, G., Pikolos, L., Papadopoulos, I., Montes-
Romero, J., Lopez Lorente, J., Makrides, G., Sutterlueti, J.,
Georghiou, G.: Intelligent Cloud-Based Monitoring and Control
Digital Twin for Photovoltaic Power Plants (2022)
78. Xu, B., Wang, J., Wang, X., Liang, Z., Cui, L., Liu, X., Ku, A.Y.:
A case study of digital-twin-modelling analysis on power-plant-
performance optimizations. Clean Energy 3(3), 227–234 (2019).
https://doi.org/10.1093/ce/zkz025
79. Yan, X.: Construction of digital twin ecosystem for coal-ﬁred
generating units. J. Phys. Conf. Ser. (2021). https://doi.org/10.
1088/1742-6596/1748/5/052037
80. Deon, B., Cotta, K.P., Silva, R.F.V., Batista, C.B., Justino, G.T.,
Freitas, G.C., Cordeiro, A.M., Barbosa, A.S., Loução, F.L.,
Simioni, T., Morais, A.M., Medeiros, I.E.A., Almeida, R.J.S.,
Araújo, C.A.A., Soares, C., Padoin, N.: Digital twin and machine
learning for decision support in thermal power plant with com-
bustion engines. Knowl. Based Syst. (2022). https://doi.org/10.
1016/j.knosys.2022.109578
81. Panov, V., Cruz-Manzo, S.: Gas turbine performance digital twin
for real-time embedded systems. In Proceedings of the ASME
Turbo Expo, Vol. 5. https://doi.org/10.1115/GT2020-14664
82. Steindl, G., Stagl, M., Kasper, L., Kastner, W., Hofmann, R.:
Generic digital twin architecture for industrial energy sys-
tems. Appl. Sci. 10(24), 8903 (2020). https://doi.org/10.3390/
app10248903
83. Tsoutsanis, E., Hamadache, M., Dixon, R.: Real time diagnostic
method of gas turbines operating under transient conditions in
hybrid power plants. In Proceedings of the ASME Turbo Expo,
Vol. 5. https://doi.org/10.1115/GT2020-14748
84. Lei, Z., Zhou, H., Hu, W., Guo-Ping, L., Guan, S., Feng, X.:
Towardaweb-baseddigitaltwinthermalpowerplant.IEEETrans.
Ind. Inf. 18(3), 1716–1725 (2022). https://doi.org/10.1109/TII.
2021.3086149
85. Xiangjun, Z., Ming, Y., Xianglong, Y., Yifan, B., Chen, F., Yu,
Z.: Anomaly detection of wind turbine gearbox based on digital
twin drive, In 2020 IEEE 3rd Student Conference on Electrical
Machines and Systems (SCEMS), pp. 184–188. https://doi.org/
10.1109/SCEMS48876.2020.9352321
86. Sahal, R., Alsamhi, S.H., Breslin, J.G., Brown, K.N., Ali, M.I.:
Digital twins collaboration for automatic erratic operational data
detection in industry 4.0. Appl. Sci. 11(7), 3186 (2021). https://
doi.org/10.3390/app11073186
87. Jeroen, D.M.D.K., Stockman, K., De Maeyer, J., Jarquin-Laguna,
A., Vandevelde, L.: Digital twins for wind energy conversion sys-
tems:aliteraturereviewofpotentialmodellingtechniquesfocused
on model ﬁdelity and computational load. Processes 9(12), 2224
(2021). https://doi.org/10.3390/pr9122224
88. Olatunji, O.O., Adedeji, P.A., Madushele, N., Jen, T.C.: Overview
of digital twin technology in wind turbine fault diagno-
sis and condition monitoring, In 2021 IEEE 12th Interna-
tional Conference on Mechanical and Intelligent Manufacturing
Technologies (ICMIMT), pp. 201–207. https://doi.org/10.1109/
ICMIMT52186.2021.9476186
89. Li, F., Li, L., Peng, Y.: Research on digital twin and collaborative
cloud and edge computing applied in operations and maintenance
in wind turbines of wind power farm, In Advances in Transdisci-
plinary Engineering, Vol. 17, pp. 80–92. https://doi.org/10.3233/
ATDE210263
90. Ebrahimi, A.: Challenges of developing a digital twin model of
renewable energy generators. In 2019 IEEE 28th International
Symposium on Industrial Electronics (ISIE), pp. 1059–1066.
https://doi.org/10.1109/ISIE.2019.8781529
91. Tang, X., Sun, Y., Zhao, Y., Pei, W., Li, N., Kong, L.: Digital twin
based bess state estimation and operating opimization. In 2021
IEEE 5th Conference on Energy Internet and Energy System Inte-
gration (EI2), pp. 3402–3405. https://doi.org/10.1109/EI252483.
2021.9713587
92. Sleiti, A., Kapat, J., Vesely, L.: Digital twin in energy industry:
proposed robust digital twin for power plant and other complex
capital-intensive large engineering systems. Energy Rep. 8, 3704–
3726 (2022). https://doi.org/10.1016/j.egyr.2022.02.305
93. Song, X., Cai, H., Jiang, T., Schlegel, S., Westermann, D.: Parame-
ter tuning for dynamic digital twin of generation unit in power grid
01–06 https://doi.org/10.1109/ISGTEurope52324.2021.9640105
94. Huang, J., Zhao, L., Wei, F., Cao, B.: The application of digital
twin on power industry. IOP Conf. Ser. Earth Environ. Sci. (2021).
https://doi.org/10.1088/1755-1315/647/1/012015
95. Danilczyk, W., Sun, Y., He, H.: Angel: An intelligent digital
twin framework for microgrid security. In 2019 North Ameri-
can Power Symposium (NAPS), pp. 1–6. https://doi.org/10.1109/
NAPS46351.2019.9000371
96. Danilczyk, W., Sun, Y. L., He, H.: Smart grid anomaly detection
using a deep learning digital twin. In 2020 52nd North Ameri-
can Power Symposium (NAPS), pp. 1–6. https://doi.org/10.1109/
NAPS50074.2021.9449682
97. Zhao, Y., Zhou, Y., Li, S., Zhao, M., Zheng, Y., Fu, C.: Distri-
bution network reconﬁguration digital twin model based on bi-
level dynamical time division. In 2021 International Conference
on Power System Technology (POWERCON), pp. 2178–2187.
https://doi.org/10.1109/POWERCON53785.2021.9697854
98. Huang, L., Liang, Y., Huang, H., Zhou, J.: Digital twin mod-
eling and operating state assessment of substation equipment.
In 2021 4th International Conference on Energy, Electrical and
Power Engineering (CEEPE), pp. 159–163. https://doi.org/10.
1109/CEEPE51765.2021.9475674
99. Zhou, J., Chen, Y., Ran, L., Fang, H., Zhang, Y., Zhu, X., Jaidaa,
A.: Hybrid data-driven modeling for an ac/dc power system con-
sidering renewable energy uncertainty. Front. Energy Res. (2022).
https://doi.org/10.3389/fenrg.2022.830833
100. Darbali-Zamora, R., Johnson, J., Summers, A., Jones, C.B.,
Hansen, C., Showalter, C.: State estimation-based distributed
energy resource optimization for distribution voltage regulation
in telemetry-sparse environments using a real-time digital twin.
Energies 14(3), 774 (2021). https://doi.org/10.3390/en14030774
101. Feng, Z., Wu, Y., Gao, H., Zhu, S.: Digital twin framework for adn
ﬂexible resources assessment. In 2020 IEEE Eurasia Conference
on IOT, Communication and Engineering (ECICE), pp. 209–212.
https://doi.org/10.1109/ECICE50847.2020.9302004
102. Han, J., Hong, Q., Syed, M.H., Khan, M.A.U., Yang, G., Burt, G.,
Booth, C.: Cloud-edge hosted digital twins for coordinated con-
trol of distributed energy resources. IEEE Trans. Cloud Comput.
(2022). https://doi.org/10.1109/TCC.2022.3191837
103. Kovalyov, S.P.: Design and development of a power system digital
twin: a model-based approach. In 2021 3rd International Confer-
ence on Control Systems, Mathematical Modeling, Automation
and Energy Efﬁciency (SUMMA), pp. 843–848. https://doi.org/
10.1109/SUMMA53307.2021.9632191
104. Han, J., Hong, Q., Feng, Z., Syed, M., Burt, G., Booth, C.:
Design and implementation of a real-time hardware-in-the-loop
platform for prototyping and testing digital twins of distributed
123


---

Page 25

---

A review on digital twins for power generation and distribution
1195
energy resources. Energies 15, 6629 (2022). https://doi.org/10.
3390/en15186629
105. Tiago Rabelo, C., Marcos Aurélio Izumida, M., Kennedy Alves,
M., Amadeu Fernandes de, M., de Francisci, S.: Application study
in the ﬁeld of solutions for the monitoring distribution transform-
ers of the overhead power grid. Energies 14(19), 6072 (2021).
https://doi.org/10.3390/en14196072
106. Farnell, C., Soria, E., Jackson, J., Mantooth, H.A.: Cyber protec-
tion of grid-connected devices through embedded online security.
In 2021 IEEE Design Methodologies Conference (DMC), pp. 1–
6. https://doi.org/10.1109/DMC51747.2021.9529935
107. Jiang, Z., Guo, Y., Wang, Z.: Digital twin to improve the virtual-
real integration of industrial IoT. J. Ind. Inf. Integr. (2021). https://
doi.org/10.1016/j.jii.2020.100196
108. Chen, J., Deng, R., Guo, Y., Lin, W., Cao, W., Guan, K.: Research
on network management technology of power line carrier commu-
nication in low-voltage distribution network based on digital twin.
In 2021 7th International Conference on Computer and Com-
munications (ICCC), pp. 2112–2116. https://doi.org/10.1109/
ICCC54389.2021.9674420
109. Chen, Y., Chen, Q., Gao, J., Chen, X.: Hardware-in-loop based
digital twin technology for integrated energy system: a case study
of guangyang island in chongqing, copyright - Copyright The
Institute of Electrical and Electronics Engineers, Inc. (IEEE) 2022
Last updated - 2022-08-18 (2022 2022). https://doi.org/10.1109/
CIEEC54735.2022.9846475
110. Li, C., Yang, D.: Construction of power grid digital twin model
based on gan. In 2021 China Automation Congress (CAC), pp.
7767–7771. https://doi.org/10.1109/CAC53003.2021.9728190
111. Saad, A., Faddel, S., Mohammed, O.: IoT-based digital twin for
energy cyber-physical systems: design and implementation. Ener-
gies 13(18), 4762 (2020). https://doi.org/10.3390/en13184762
112. Saad, A., Faddel, S., Youssef, T., Mohammed, O.A.: On the imple-
mentation of IoT-based digital twin for networked microgrids
resiliency against cyber attacks. IEEE Trans. Smart Grid 11(6),
5138–5150 (2020). https://doi.org/10.1109/TSG.2020.3000958
113. Xie, J., Guo, J., Sun, M., Su, D., Li, W., Chen, S., Wang, S.:
A digital twin ﬁve-dimensional structural model construction
method suitable for active distribution network. In 2022 2nd
International Conference on Electrical Engineering and Mecha-
tronics Technology (ICEEMT), pp. 418–426. https://doi.org/10.
1109/ICEEMT56362.2022.9862649
114. Brosinsky, C., Song, X., Westermann, D.: Digital twin - concept
of a continuously adaptive power system mirror. In International
ETG-Congress 2019; ETG Symposium, pp. 1–6
115. Huxoll, N., Aldebs, M., Baboli, P.T., Lehnhoff, S., Babazadeh,
D.: Model identiﬁcation and parameter tuning of dynamic loads
in power distribution grid: digital twin approach. In 2021 Inter-
national Conference on Smart Energy Systems and Technolo-
gies (SEST), pp. 1–6. https://doi.org/10.1109/SEST50973.2021.
9543095
116. Xing, J., Sun, S., Yu, P., Li, Y., Cheng, Y., Wang, Y., Li, S.,
Zhu, J.: Multi-energy simulation and optimal scheduling strat-
egy based on digital twin. In 2022 Power System and Green
Energy Conference (PSGEC), pp. 96–100. https://doi.org/10.
1109/PSGEC54663.2022.9881079
117. You, M., Wang, Q., Sun, H., Castro, I., Jiang, J.: Digital twins
based day-ahead integrated energy system scheduling under load
and renewable energy uncertainties. Appl. Energy 305, 117899
(2022). https://doi.org/10.1016/j.apenergy.2021.117899
118. Tzanis, N., Andriopoulos, N., Magklaras, A., Mylonas, E., Birbas,
M., Birbas, A.: A hybrid cyber physical digital twin approach for
smart grid fault prediction. In 2020 IEEE Conference on Industrial
Cyberphysical Systems (ICPS), Vol. 1, pp. 393–397. https://doi.
org/10.1109/ICPS48405.2020.9274723
119. Zhang, Y., Luo, J., Zhu, W., Wu, Y., Zhang, X.: Application
of digital twins in smart grids (2022). https://doi.org/10.1109/
ICPICS55264.2022.9873758
120. Wagner, T., Mehlmann, G., Richter, M.: Application of the dig-
ital twin concept for a distribution network. In IEEE Power and
Energy Student Summit, pp. 1–5 (2020)
121. Mourtzis, D., Angelopoulos, J., Panopoulos, N.: Development of
a pss for smart grid energy distribution optimization based on
digital twin. Proc. CIRP 107, 1138–1143 (2022). https://doi.org/
10.1016/j.procir.2022.05.121
122. Zhou, M., Yan, J., Feng, D.: Digital twin framework and its appli-
cation to power grid online analysis. CSEE J. Power Energy
Syst. 5(3), 391–398 (2019). https://doi.org/10.17775/CSEEJPES.
2018.01460
123. Darian, L., Kontorovych, L.: Electrical power equipment digital
twins. Basic principles and technical requirements (2021). https://
doi.org/10.1051/e3sconf/202128801029
124. Sellitto, G.P., Aranha, H., Masi, M., Pavleska, T.: Enabling a zero
trust architecture in smart grids through a digital twin. In Com-
munications in Computer and Information Science, Vol. 1462, pp.
73–81. https://doi.org/10.1007/978-3-030-86507-8_7
125. Hu, C., Shi, W., Jiang, L.: Application case of digital twin tech-
nology in electric power system. IOP Conf. Ser. Mater. Sci. Eng.
(2020). https://doi.org/10.1088/1757-899X/788/1/012083
126. Ma, Q.: Application of digital twin and hologram technology to
achieve distribution network reliability forecast (2022). https://
doi.org/10.1109/ACPEE53904.2022.9784043
127. Ruhe, S., Nicolai, S., Jiang, T., Cai, H., Sayed, N. E., Geithner,
T., Frueh, N., Ulbig, A., Schoenfeld, B., Prinz, S.: Approach of a
dt based automatic grid operation for distribution grids, In ETG
Congress, pp. 1–6 (2021)
128. Bai, H., Yuan, Z., Tang, X., Liu, J., Yang, W., Pan, S., Xue, Y.,
Liu, W.: Automatic modeling and optimization for the digital twin
of a regional multi-energy system. In 2022 Power System and
GreenEnergyConference(PSGEC),pp.214–219.https://doi.org/
10.1109/PSGEC54663.2022.9881075
129. Pan, H., Dou, Z., Cai, Y., Li, W., Lei, X., Han, D.: Digital twin
and its application in power system. In 2020 5th International
Conference on Power and Renewable Energy (ICPRE), pp. 21–
26. https://doi.org/10.1109/ICPRE51194.2020.9233278
130. Jose, F.V., Norma, G.M., Ivan, R.F., Sebastian, R.D., Arnaldo,
G.O., Cesar, A.C.: Digital twin of the medium voltage grid of
university city at unam. In 2021 IEEE PES Innovative Smart Grid
Technologies Europe (ISGT Europe), pp. 1–6. https://doi.org/10.
1109/ISGTEurope52324.2021.9640160
131. Kummerow, A., Nicolai, S., Brosinsky, C., Westermann, D., Nau-
mann, A., Richter, M.: Digital-twin based services for advanced
monitoring and control of future power systems. In 2020 IEEE
Power and Energy Society General Meeting (PESGM), pp. 1–5.
https://doi.org/10.1109/PESGM41954.2020.9354468
132. Schäler, C., Strasser, K., Damböck, R., Schwefel, H.P.: Increased
renewable hosting capacity of a real low-voltage grid based on
continuous measurements—results from an actual pv connection
request, In: Communications in Computer and Information Sci-
ence, Vol. 1462, pp. 90–98. https://doi.org/10.1007/978-3-030-
86507-8_9
133. Which countries produce the most hydroelectric power? (2023).
https://www.weforum.org/agenda/2015/10/which-countries-
produce-the-most-hydroelectric-power/
Publisher’s Note Springer Nature remains neutral with regard to juris-
dictional claims in published maps and institutional afﬁliations.
123
