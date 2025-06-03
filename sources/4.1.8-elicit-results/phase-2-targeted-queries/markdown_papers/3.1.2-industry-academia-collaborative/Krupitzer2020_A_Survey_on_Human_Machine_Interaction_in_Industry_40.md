# Krupitzer2020 A Survey on Human Machine Interaction in Industry 4.0

## Paper Metadata

- **Filename:** Krupitzer2020_A_Survey_on_Human_Machine_Interaction_in_Industry_4.0_DOI_-.pdf
- **DOI:** .
- **Authors:** Not available
- **Year:** Not available
- **Journal/Venue:** Not available
- **URL:** Not available
- **Extraction Date:** 2025-06-03T15:04:03.074765
- **Total Pages:** 45

## Abstract

Abstract not available from BibTeX metadata.

## Keywords

Keywords not available from BibTeX metadata.

---

## Full Text Content



### Page 1

A Survey on Human Machine Interaction in Industry 4.0
CHRISTIAN KRUPITZER, VERONIKA LESCH, MARWIN ZÜFLE, and SAMUEL KOUNEV, University of Würzburg, Germany
SEBASTIAN MÜLLER, JANICK EDINGER, and CHRISTIAN BECKER, University of Mannheim,
Germany
ALEXANDER LEMKEN, ioxp Gmb H, Germany
DOMINIK SCHÄFER, Syntax Systems Gmb H, Germany
Industry 4.0 or Industrial Io T both describe new paradigms for seamless interaction between human and
machines. Both concepts rely on intelligent, inter-connected cyber-physical production systems that are able
to control the process flow of the industrial production. As those machines take many decisions autonomously
and further interact with production and manufacturing planning systems, the integration of human users
require new paradigms. In this paper, we provide an analysis of the current state-of-the-art in human machine
interaction in the Industry 4.0 domain. We focus on new paradigms that integrate the application of augmented
and virtual reality technology. Based on our analysis, we further provide a discussion of research challenges.
CCS Concepts: • Human-centered computing →Human computer interaction (HCI); • Applied computing →Industry and manufacturing; • Software and its engineering →Designing software.
Additional Key Words and Phrases: human machine interaction, augmented / virtual reality, Industry 4.0,
Industrial Io T
ACM Reference Format:
Christian Krupitzer, Veronika Lesch, Marwin Züfle, Samuel Kounev, Sebastian Müller, Janick Edinger, Christian
Becker, Alexander Lemken, and Dominik Schäfer. 2020. A Survey on Human Machine Interaction in Industry
4.0. 1, 1 (February 2020), 45 pages. https://doi.org/10.1145/1122445.1122456
1
INTRODUCTION
The world has witnessed three industrial revolutions since the late eighteenth century which all
brought major leaps forward in the efficiency and productivity of industrial activities and are
largely acknowledged as historical facts, at least in Europe.
While the first and second industrial revolution were characterized by mechanization based on
the invention of the steam engine and electrification of production processes, respectively, the third
industrial revolution was induced by the introduction of computerized, thus automated, processes
into manufacturing [28].
Authors’ addresses: Christian Krupitzer, christian.krupitzer@uni-wuerzburg.de; Veronika Lesch, veronika.lesch@
uni-wuerzburg.de; Marwin Züfle, marwin.zuefle@uni-wuerzburg.de; Samuel Kounev, samuel.kounev@uni-wuerzburg.de,
University of Würzburg, Am Hubland, Würzburg, Germany, 97074; Sebastian Müller, mueller.sebastian12@gmx.de; Janick
Edinger, janick.edinger@uni-mannheim.de; Christian Becker, chrstian.becker@uni-wuerzburg.de, University of Mannheim,
Schloss, Mannheim, Germany, 68161; Alexander Lemken, lemken@ioxp.de, ioxp Gmb H, Julius-Hatry-Straße 1, Mannheim,
Germany, 68163; Dominik Schäfer, Dominik.Schaefer@syntax.com, Syntax Systems Gmb H, Höhnerweg 2-4, Weinheim,
Germany, 69469.
Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee
provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and
the full citation on the first page. Copyrights for components of this work owned by others than ACM must be honored.
Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires
prior specific permission and/or a fee. Request permissions from permissions@acm.org.
© 2020 Association for Computing Machinery.
XXXX-XXXX/2020/2-ART $15.00
https://doi.org/10.1145/1122445.1122456
, Vol. 1, No. 1, Article . Publication date: February 2020.
ar Xiv:2002.01025v1 [cs.HC] 3 Feb 2020

---


### Page 2

2
Krupitzer et al.
What had been less agreed upon in the scientific community and among practitioners until
recently is the question whether manufacturing is currently subject to another disruptive revolution,
for the first time not only identified ex post. A distinctive feature of this alleged fourth industrial
revolution, commonly referred to as Industry 4.0 (I4.0), is the integration of two formerly opposing
paradigms of industrial activities, the so-called economies of scale and economies of scope, by
means of mass production of individually customized products [66, 83].
Opponents of the notion of another actual revolution advocate the view that I4.0 can be seen as
a step-wise evolution based upon characteristic technologies of the third industrial revolution’s
computer-integrated manufacturing rather than representing a stand-alone revolution following a
specific scientific break-through [59]. Besides, the true magnitude and implications of I4.0, accused
of being subject to predictive and exaggerating marketing efforts, will only be verifiable in retrospect
[9].
However, despite existing skepticism towards the revolutionary character and degree of maturity
of I4.0 activities and enabling technologies, in the most recent years I4.0 has largely been established
and accepted as a synonym for a fourth industrial revolution, either ongoing or on the verge of
inception. This observation bases on a substantial amount of publications from information and
communications technology and manufacturing science. The main reason for acknowledging I4.0 as
an actual revolution in the industrial sector is the magnitude of economic effects and process-related
implications it is expected to exert on the manufacturing industry, comparable to those of the
preceding industrial revolutions [28, 48].
1.1
Problem Statement and Motivation
Problem Statement. Accepting the predominant classification of I4.0 as a revolutionizing development for the industrial sector, its relevance and significance for advanced economies is obvious.
This holds true for Germany in particular, considering the fact that the German industrial sector is
still comparably large and a crucial pillar of German economic power, having contributed 26.1% of
the country’s overall gross value added in 2017 [67, p.61].
At the same time, in light of modern globalized business and value chains, any corporate entity
or even industry branch is at risk of losing market share and ultimately its raison d’être if it
fails to successfully manage its cost structure and stay competitive. While the German economy,
supported by its broad network of small and medium-sized enterprises, certainly represents a
particular case regarding the significance of the industrial sector for the overall economy, advanced
economies with a strong production industry, in general, face this challenge. Taking as given their
disadvantage as opposed to competing emerging economies with respect to the general level of
labor cost, competitiveness based on industrial activities of similar structure and nature seems out
of reach.
Instead, a promising resort might be found in the implementation of advanced automation
solutions for manufacturing. The rationale behind said strategy lies in the hope for increased
productivity induced by the application of superior technology, compensating for the disadvantage
regarding the costs per piece. On top of that, the disadvantage in the cost structure might be reduced
by the opportunity to implement less human labor-intensive operations provided by the increased
degree of process automation.
Despite the apparent economic appeal of such an approach, there is another crucial sphere to be
considered in an evaluation of the overall problem and potential methods of resolution. In modern
informed societies, both from a political and economic or managerial point of view, it is imperative
to secure social sustainability when promoting such a far-reaching agenda.
Returning to the particularities of the German economic structure, a phenomenon closely linked
to the size of its industrial sector is the large share of the active labor force employed in this sector.
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 3

A Survey on Human Machine Interaction in Industry 4.0
3
According to the German Federal Statistical Office (2018), the industrial sector employed 19.9% of all
employees in Germany in 2017 [67, p.70]. Obviously, a large cut in jobs in the manufacturing industry
due to increasing automation of formerly human tasks would have wide-ranging implications for
the German economy and particularly the labor market and the affected individuals.
On the other hand, securing competitiveness of domestic industrial activities, as indicated above,
seems indispensable as well if a substantial share of jobs in the sector is supposed to be preserved.
Hence, at first sight, decision-makers in businesses and government authorities seem to be running
into the problem and dilemma of equipping manufacturers with appropriate tools, in particular
technologies, for fierce competition while, at the same time, determining a tolerable amount and
degree of process automation in order to preserve jobs in one of the most significant employment
sectors.
Motivation. Fortunately, the manufacturing industry is currently evolving away from the
notion that productivity enhancements through technological progress and sustainable human
employment are mutually exclusive, instead moving towards the integration of both under the
fourth industrial revolution.
In particular, a central characteristic of I4.0 activities is supposed to be the integration of human
operators into modern and advanced production processes, captured under the paradigm of humancentered automation in manufacturing [44]. This means that future competitiveness is not supposed
to be secured only via superiority in automation-based productivity but rather through offering
enhanced value to customers by providing individual product customization. For that purpose,
meaningful integration of the strengths of both human and machine entity is supposed to enable
an increase in manufacturing flexibility [5].
Thus, successful collaboration and interaction of humans with diverse and potentially innovative technological hardware and software components, i.e. machines, with the aim of achieving
human-machine symbiosis [58] will gain enormously in importance in various facets of industrial
production. Nonetheless, so far, and to the best of the author’s knowledge, no comprehensive
survey on human-machine interaction (HMI) in I4.0 and an attempt at a structural description
and capture of the topic exists in research. The lack of said type of study, in combination with the
topic’s relevance for successful implementation of I4.0 activities and, in turn, for ensuring future
competitiveness and employment in the industrial sector, provides the motivation for this paper.
1.2
Research Questions
In order to fill the mentioned gap in research regarding a comprehensive study of the state of the
art in HMI related to I4.0 operations, this paper attempts to provide a wide-ranging overview and,
in particular, a structural ordering of the different facets of HMI in I4.0. This kind of structured
description of the overall topic, taking into account different perspectives and sub-components,
can help distinguishing and integrating diverse research streams as well as foci and opinions of
scientists. Such integration provides a sound basis for a comprehensive understanding of the topic’s
different facets and, consequently, potential orientation concerning open research issues to be
addressed in the future.
Therefore, this paper aims to analyze and find answers to three consecutive high-level research
questions guiding the procedure and remaining structure of the paper. While the first research
question, Research Question 1 (RQ1), features a more qualitative character, the second and third
research question, Research Question 2 (RQ2) and Research Question 3 (RQ3), aim to motivate a
more quantitative analysis based upon potential insights gained from answering RQ1.
In particular, RQ1 raises the question what the current state of the art in HMI research in the
area of I4.0 is. In the course of answering RQ1, a comprehensive taxonomy of the topic is supposed
to be developed, capturing and systematically structuring the most important facets of the topic.
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 4

4
Krupitzer et al.
Relating to different elements of this taxonomy, RQ2 and RQ3 ask what the main foci and
identifiable patterns in research related to HMI in the I4.0 area are, respectively. On a more detailed
level, RQ2 and RQ3 are split into several sub-questions specifying the respective focus in the
identification of potential focal points and patterns in related research. The three sub-questions of
RQ2 ask what the focal points in research related to the human, machine, or interaction aspect
in I4.0-related HMI are, respectively. The sub-questions of RQ3, on the other hand, focus on
the identification of underlying patterns in research related to the topic and ask what kinds of
associations can be identified in the data on related research and how related research articles can
be classified with regard to individual aspects of the topic, respectively. A detailed listing of the
three main research questions and their sub-questions, if applicable, is provided in Table 1.
Main Research Questions
RQ1
What is the current state of the art in human-machine interaction research in the area of Industry
4.0?
RQ2
What are the main foci in research related to human-machine interaction in the area of Industry
4.0?
RQ3
What are the patterns which can be identified in research related to human-machine interaction
in the area of Industry 4.0?
Sub-Questions
RQ2.1
What are the focal points in research related to the human aspect in Industry 4.0-related humanmachine interaction?
RQ2.2
What are the focal points in research related to the machine aspect in Industry 4.0-related
human-machine interaction?
RQ2.3
What are the focal points in research related to the interaction aspect in Industry 4.0-related
human-machine interaction?
RQ3.1
What kinds of associations can be identified in the data on research related to human-machine
interaction in Industry 4.0?
RQ3.2
How can research articles related to human-machine interaction in Industry 4.0 be classified with
regard to individual aspects of the topic?
Table 1. Research Questions
1.3
Structure
Having presented a short introduction to the topic of HMI in I4.0 including an emphasis on the
relevance of research and progress in both I4.0 overall and its sub-aspect of HMI, the paper continues
in Section 2 with a definition and description of the relevant foundations for the overall paper. This
includes a description of the fundamentals of HMI and of two fundamental technologies for I4.0
activities (Cyber-Physical Systems (CPSs) and the Internet of Things (Io T)), followed by a detailed
clarification of the meaning and scope of I4.0 as well as a description of a data mining approach
applied in the course of this paper.
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 5

A Survey on Human Machine Interaction in Industry 4.0
5
Before Section 4 covers and describes the methodological approach of a structured literature
review implemented in this paper, Section 3 presents an overview over studies related to the type
and topic of this paper.
As the central parts and answers to the research questions of this paper, Section 5 and Section 6
present the results of the applied methodology and implemented analyses, starting with a description
of the developed taxonomy in Section 5 and followed by a quantitative analysis of the prevalence
of different taxonomy elements in the literature sample and of patterns in the collected data in
Section 6.
Finally, in Section 7, a summary of the central propositions of the study, combined with concluding
remarks, follows which leads to an outlook on opportunities for future research derived from the
insights of this paper.
2
BACKGROUND
Before presenting and describing the study’s methodology and results in depth beginning in
Section 4, the following section aims to lay the groundwork for a general and common understanding
of HMI and I4.0, especially for readers not yet broadly familiar with the topic of this paper.
After a brief introduction to the concept of HMI and related technologies, the concepts of CPSs
and the Io T are addressed in order to lay the foundations for a following detailed description of the
umbrella term I4.0.
2.1
Human-Machine Interaction and Related Technologies
While early scientific efforts on HMI or human-computer interaction had concentrated on fully
controllable systems, research quickly turned the focus towards adaptive mechanisms due to the
development of dynamic, highly complex human-machine systems [24]. Exceeding the role of
mere information processing, automated systems have evolved into partly independent actors in
dynamic situations and uncertain environments which has led to the requirement of introducing
elements of human-to-human relationships into HMI and human-machine collaboration [24]. This
implies that, in complex human-machine systems, the human and machine agent can no longer be
considered in isolation and should instead be regarded as a dynamic unit or team collaborating
towards an overall task and aim including dynamic task allocation among participants [24].
Enabling adaptability and dynamism of the human-machine system has required the abandonment of full system-side determinism in order to leave degrees of freedom for the automated
system to react to situations which could not have been perfectly foreseen and modeled by system
designers [24]. Thus, the human operator’s responsibility evolves from full control to partial control
and supervision in the interaction with machines [24].
In order to secure that the human operator maintains an overview and understanding of the
processes and dynamics in this complex human-machine system, the types and characteristics of
implemented interfaces remain a central aspect in the examination of HMI processes, especially
regarding ergonomic properties like usability and transparency [24]. As modern and advanced
instances of user interfaces (UIs), Augmented Reality (AR) and Virtual Reality (VR) will play an
important role in the discussion of UIs for HMI purposes in I4.0 in the course of this paper. Therefore,
brief definitions of those technologies are provided.
According to Paelke, AR applications are characterized by enhancing a real-world environment
through its integration with computer-generated information [46]. Mainly, this implies adding
digital objects and information to a human user’s real-world view, enabling direct interaction
with information which has a direct spatial relation to the real environment and is more readily
interpretable in its environmental context [46].
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 6

6
Krupitzer et al.
In contrast, users of VR applications do not necessarily maintain a view of a real-world scenery
but are instead immersed in an entirely computer-generated and digital world offering interaction
possibilities with components of the artificial environment [42]. Thus, both AR and VR enable the
mediation of information in a spatial relation to the environmental context [46], but AR relies on a
basis of data from a real-world scenery to be enhanced digitally while VR applications are entirely
based on computer-generated content [10].
2.2
Cyber-Physical Systems and the Internet of Things
Representing main enablers leading to the development of I4.0 [90], the concepts of CPSs in
manufacturing and the Io T are briefly introduced in this section.
The concept of a CPS has been known for more than a decade now, characterized primarily
by its feature of integrating computational processes with the corresponding physical processes,
i.e. synchronizing physical and cyber world. This means that physical processes are constantly
monitored and controlled in the cyber space so that computation has a direct manipulating impact on real-world operations while, at the same time, feedback from physical processes affects
computational procedures [34].
While conceivable application scenarios for CPSs are numerous and diverse, the technology
has received enormous attention in manufacturing research recently, especially regarding I4.0
applications. Therefore, CPSs deployed in a manufacturing context, mainly machines and production modules, are often referred to as Cyber-Physical Production Systems (CPPSs). CPPSs are
characterized by their capabilities to collect and exchange data and information autonomously, to
activate actual physical processes, and to perform independent mutual control via their embedded
local intelligence [1, 85].
Obviously, self-organization and mutual control among various instances of CPPSs requires
context-awareness and communication channels connecting all involved entities which is provided
by the ability to sense the environment in real time and the installation in a networked infrastructure
[85, 93].
Said interconnection among CPPSs represents an important instance of another fundamental
pillar of I4.0 activities [28, 90], namely the Io T. The Io T can be considered as representing an
extension to the well-known Internet by adding a huge amount of ending nodes to the network.
What is special about those nodes added under the Io T is that they are regularly small-scale
computers regarding both the functionality and computing power they provide as well as the
amount of energy they consume [13]. This coincides with the above description of CPPSs added
to the Io T network which feature small-scale embedded sensors and processing units capable of
serving a specific purpose, e.g. capturing and communicating operational and environmental data
[25].
Consequently, the Io T represents a network infrastructure where any conceivable physical item,
i.e. thing, can be embedded with computational intelligence featuring a connection to the Internet
[13]. With respect to HMI processes in industrial operations, this implies that machinery and
products of a CPS-type offer a new quality of information transparency and availability by being
able to provide data to an authorized entity at any time via the Internet.
2.3
Industry 4.0
Having introduced important technological foundations for a successful implementation of I4.0
activities, the question arises what the term Industry 4.0 actually comprises. Therefore, the
following subsections define the meaning and scope of I4.0 by first explaining the origin of the
term and its evolution towards a synonym for a fourth industrial revolution and then introducing
paradigms used in literature to illustrate the scope and concept of I4.0 operations.
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 7

A Survey on Human Machine Interaction in Industry 4.0
7
2.3.1
Origin and Evolution of the Term. Interestingly, Industry 4.0, or rather the German equivalent Industrie 4.0, is not a term established by scholars in scientific publications. Instead, towards
the end of 2011, the German federal government adopted the Industrie 4.0 project initiated a short
while before by the German Industry-Science Research Alliance and made it an integral part of
their high-tech strategy 2020 [29]. In 2011, the term Industrie 4.0 was also first introduced to
the general public and the scientific community in the course of the Hannover Fair [61, 76].
Soon after, the concept and ideas of Industrie 4.0 found their way into scientific research and a
growing number of studies were published dedicated towards different aspects of the topic. Indeed,
some of the early contributions towards I4.0 actually even used the German instead of the English
version of the term (cf. [53, 63, 64, 78, 81]). As indicated in the Introduction, only over time, I4.0
evolved into a stand-alone term representing a synonym for future smart manufacturing and a
fourth industrial revolution.
Nonetheless, the label I4.0 for innovative concepts of CPS- and Io T-integrated smart manufacturing is not unique in research activities from different areas. Particularly in the U.S., scientific
publications frequently address either the so-called Industrial Internet, Industrial Internet of Things
[80], or simply smart manufacturing [72]. Besides, there are numerous national and regional initiatives similar to the German strategic initiative of Industrie 4.0, e.g. in the U.S. [26, 53], China [39],
Japan [79], South Korea [69], France, and the Basque Country in Spain [53].
2.3.2
Paradigms. After the clarification of the origin and evolution of the term itself, the following
subsections are supposed to define and illustrate the fundamental pillars and constituents of the
I4.0 concept. For that purpose, they present central paradigms of I4.0, as identified and elaborated
on in related scientific literature, in order to give the reader an overview over main features of I4.0
operations.
Actors in Future Manufacturing. As indicated in Section 1.1, a central characteristic of manufacturing activities adhering to I4.0 is the integration of human factors into operations despite
an advanced degree of process automation. This kind of human-centered perspective on smart
manufacturing activities is reflected in the work of Weyer et al. who define three different types of
actors in manufacturing as a central paradigm of future I4.0 activities. These actors are represented,
on the one hand, by products and machinery turning into smart products and smart machines
reflecting increased autonomy and automation under I4.0, as well as, on the other hand, by augmented operators highlighting the significance of human involvement to ensure smooth running
of operations [85].
Smart Products. According to the authors of [85], products under I4.0 evolve from passive
objects, upon which actions are performed, into active subjects crucial to the implementation of
decentralized process control. In that sense, every product is embedded with individual memory
early on in the production process enabling products to self-orchestrate their assembly process.
This means that unfinished products carry information about the remaining required process steps
so that they can, e.g., order the specific service or part needed for their next step of assembly from
production resources with open capacity [85].
Smart Machines. The second type of central agents in I4.0 is represented by smart machines
implying that modern machinery turns into CPPSs, thus featuring characteristics described in
Section 2.2, like context-awareness, self-organization, as well as mutual control and communication.
Furthermore, in order to increase flexibility and adaptability of the overall production system, smart
machines allow for a fast and convenient integration of a new CPPS into an existing production
cell, enabling a plug-and-play solution instead of a lengthy ramp-up phase for newly integrated
manufacturing equipment [85].
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 8

8
Krupitzer et al.
Despite those advanced capabilities and opportunities offered by smart products and especially
machines, the complexity of modern, highly automated production processes implies that the human
factor in production cannot be eliminated without restraining the overall system’s operability and
functionality [91].
Augmented Operators. This is why Weyer et al. define a third type of central actor in I4.0
activities which is the augmented operator. The distinct feature of this vivid human agent compared
to its counterparts is the inherent adaptability of the human entity, making it the most flexible
part of the entire operations. Assuming this role, the human is supposed to take responsibility of
various crucial tasks to complement the overall, still highly automated system [85].
Yet, human operators in I4.0 are not supposed to rely solely on their inherent capabilities. Instead,
in performing their tasks, they receive support by appropriate technologies in order to exploit their
own full potential [85]. The coherent consequence of this interplay of human and machine actors
in the course of manufacturing activities is the necessity for purposeful and successful HMI in
order to guarantee corporate success in I4.0, leading to the topic of this paper.
Design Principles for Industry 4.0 Activities. Representing a suitable conclusion and integration
of the technological and process-related characteristics of I4.0 introduced so far, this subsection
provides an overview over design principles for I4.0 operations, as identified and defined in scientific
literature on the anticipated fourth industrial revolution.
Based on a survey on the German Industrie 4.0 combined with a nominal group workshop
with corporate experts, Hermann et al. develop a framework of four major design principles
for I4.0 activities. These are technical assistance, interconnection, information transparency, and
decentralized decisions [22].
Practically, the first one of these design principles directly refers to the human role of an
augmented operator in I4.0 activities, as introduced in the preceding section. To be more precise,
technical assistance as a guideline for designing I4.0 operations suggests to provide both virtual
and physical support for human workers in smart manufacturing environments. Virtual assistance
implies support for the human operator in maintaining an overview and understanding of ongoing
activities and processes via appropriate data and information visualization. Physical assistance,
on the other hand, can be provided, for instance, by co-working robots performing physically
demanding tasks [22].
Interconnection hints towards the necessity to comprehensively connect production factors
and stakeholders like manufacturing equipment and people via the Internet in order to enable
seamless collaboration and information sharing. This, in turn, requires the establishment of common
standards for communication and an appropriate level of cyber security when designing such a
system [22].
This type of interconnected design of I4.0 activities directly leads to the remaining two design
principles of information transparency and decentralized decisions. The ubiquitous connectivity of
manufacturing equipment and employees enables the aggregation of raw data from the physical
world to higher-value context information in the cyber space where it is made available transparently
and comprehensibly to the appropriate and authorized entities. Finally, providing CPPSs and
employees with such aggregated and context-related information tailored to their specific situation
enables decentralized autonomy for those actors in decision-making and process control [22].
3
RELATED WORK
After laying the foundations for the description of the actual in-depth analysis in the course of
this paper, which will follow in the upcoming sections, an overview over related work and a
differentiation of related studies from this paper are provided in order to justify the relevance of
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 9

A Survey on Human Machine Interaction in Industry 4.0
9
this study and to give the reader an idea of ongoing research activities in the field of I4.0. Taking
into account the type of study this paper represents, surveys on I4.0-related topics are considered
as relevant related scientific work.
On the most general level, existing published surveys on I4.0 can be divided into two main
clusters. The first group of papers includes surveys on aspects and subtopics of I4.0 other than HMI
while the second cluster comprises studies which do have a focus on HMI in an I4.0 environment.
However, with regard to a differentiation from this paper, those surveys investigate some specific
partial aspect instead of aiming for a comprehensive description and classification of HMI in I4.0.
For a more detailed description of the two clusters of related work, the following sections provide
an overview over I4.0-related surveys with and without a focus on HMI aspects.
3.1
Surveys on Industry 4.0 without a Focus on Human-Machine Interaction
Considering the fact that I4.0 has been an extensively covered topic in industrial research for the
last couple of years, it is of little surprise that numerous surveys on some of its elements can be
found. Among the related surveys identified, those examining different aspects compared to this
paper often have a fairly technological focus.
In their general study on I4.0 research, Saucedo-Martínez et al. identify nine central baseline
technologies for I4.0 activities and cluster scientific publications included in their sample according
to those technological categories [62]. Those baseline technologies are Big Data and analytics,
autonomous robots, simulation, horizontal and vertical system integration, the industrial Io T, cyber
security, additive manufacturing, AR, and the cloud. In order to determine more detailed insights on
each of these technologies, the articles assigned to the respective category, representing research
specialized on this type of technology, are analyzed in more depth (cf. [62]).
In a similar approach, Kang et al. investigate the national initiatives for future manufacturing in
Germany, the U.S., and South Korea with regard to the respective central technological components,
cluster existing publications according to those technologies, and analyze the technologies based
on the identified relevant literature [30]. For Germany, those are CPSs, the Io T, Big Data, cloud
computing, and sensors, while for the U.S., smart energy and additive manufacturing, and for South
Korea, smart energy, three-dimensional (3D) printing, and holograms are added [30].
Brettel et al. conduct an extensive literature review based on an immense sample of 5911 articles
from practice-oriented journals targeted at industrial executives, combined with expert interviews
from the industrial and consulting sector [5]. In their structured literature review, they map
research on I4.0 according to the topics of individualization of production, horizontal integration in
collaborative networks, and end-to-end digital integration, as well as the respective sub-aspects. In
order to evaluate the practical relevance of their findings, they conduct the mentioned structured
interviews with experts from practice [5].
Lu provides another general survey on I4.0, clustering related literature according to the five
categories of concept and perspectives of I4.0, CPSs, key technologies, interoperability, and applications of I4.0 [39]. In the analysis of each of the five categories, Lu applies a particular focus on
interoperability aspects of I4.0, developing a broad conceptual framework of the topic [39].
Preuveneers & Ilie-Zudor, in turn, survey the general developments and trends in I4.0, identifying remaining challenges to the implementation of such activities which offer opportunities
for future research [55]. The challenges identified and to be further researched are ways of guaranteeing predictable system behavior, quality assurance for context-aware behavior, risks with
shifting intelligence from operators to automated systems, and compliance regulations and legal
implications.
Finally, Pfohl et al. analyze the determinants for the diffusion of technological innovations under
an I4.0 scenario in their structured literature review [51] while Hermann et al. survey the topic of
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 10

10
Krupitzer et al.
design principles for I4.0 activities covered in corresponding research [22]1. The diffusion factors
for technological innovations in I4.0 identified in the former study are the degree of maturity of
the communication system, know-how of staff, industry-wide investment efficiency, and industry
membership [51].
3.2
Surveys on Industry 4.0 with a Focus on Human-Machine Interaction
A similar number of surveys covering specific facets of HMI or human factors in I4.0 has been
identified in the course of collecting relevant literature for this paper. The vast majority of these
studies is specifically oriented towards either VR or AR applications, or both, within I4.0 operations
and, thus, covers only a subset of this paper’s scope.
Büttner et al. conduct a survey on AR and VR applications in I4.0 manufacturing activities,
more precisely on the available platform technologies and application areas, creating a smallscale design space for such Mixed Reality applications in manufacturing [6]. This design space
differentiates among four general application scenarios and four types of Mixed Reality technology
platforms available for application, respectively. The application scenarios are manufacturing,
logistics, maintenance, or training while the available platforms comprise mobile devices (AR),
projection (AR), and head-mounted displays (HMDs) (AR or VR).
Dini & Dalle Mura and Wang et al. both present surveys on AR applications, however not
restricted to I4.0-related application scenarios [8, 82]. Dini & Dalle Mura investigate general commercial AR applications including besides industrial scenarios also, among others, civil engineering.
The specific AR application scenarios which they examine based on related scientific literature
are maintenance and repairing, inspection and diagnostics, training, safety, and machine setup [8].
Wang et al., in turn, examine scientific research on AR applications for assembly purposes from a
time span of 26 years starting as early as 1990 and concentrating mainly on the period from 2005
until 2015. Thus, they extend the scope to many years before the advent of I4.0-related initiatives
and ideas. The major application purposes of AR in assembly tasks which they investigate are
assembly guidance, assembly design and planning, and assembly training [82].
Lukosch et al. provide a literature review on AR applications with an even less specific focus on
industrial deployment by examining the state of the art at the time in research on collaboration in
AR considering a wide range of possible application fields, the industrial sector being only one of
those [40]. As a result, they identify remaining research challenges relating to collaboration in AR
which are the identification of suitable application scenarios and interaction paradigms as well as
an enhancement of the perceived presence and situational awareness of remote users [40].
Palmarini et al., in turn, conduct a structured literature review on different software development
platforms and types of data visualization and hardware available for AR applications in various
maintenance scenarios [47]. The aim and purpose of their study is to derive a generic guideline
facilitating a firm’s selection process of the appropriate type and design of AR application, tailored
to the specific type of maintenance activity at hand which the firm is planning to enhance utilizing
AR technology [47].
Lastly, Choi et al. and Turner et al. provide surveys on VR technology in an industrial environment,
the latter group of authors concentrating on a potential combination of VR technology with discrete
event simulation for scenario testing in I4.0 activities [7, 74]. Choi et al., on the other hand, present
a survey on VR applications in manufacturing, concentrating on potential contributions of VR
deployment in the development process for new products and deriving a mapping of different
types of VR technology towards the different steps of the product development process. Therefore,
1Recall Section 2.3.2 for more details on the insights on I4.0 design principles gained from the study of Hermann et al. [22].
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 11

A Survey on Human Machine Interaction in Industry 4.0
11
they consider applicability of various VR technologies for the phases of concept development,
system-level design, design of details, testing and refinement, and launch of production [7].
Besides those surveys on AR and VR applications, a literature review by Hecklau et al. exists
on the major challenges as well as skills and competencies needed for future employees under
an I4.0 scenario [21]. The authors utilize the insights from the literature analysis to structure the
required skills according to different categories, based on which a competence model is created
analyzing employees’ levels of skills and competencies which will be particularly important in
an I4.0 working environment. Those main categories for the competence model are technical,
methodological, social, and personal competencies [21].
Finally, it is important to highlight that this outline of related work does not claim to be exhaustive.
Instead, it is rather supposed to provide an overview and an idea of other existing scientific literature
regarding the topic and thereby underline that, to the best of the author’s knowledge, a study
highly similar to this paper does not exist. This observation serves for justifying the conduct of
this study and, at the same time, implicates the necessary importance and relevance of the paper.
4
METHODOLOGICAL APPROACH FOR DEFINING AND ANALYZING A
TAXONOMY
Having laid the foundations for an in-depth analysis of HMI in I4.0, the following section serves
the purpose of explaining the methodological approach taken in this paper in order to define and
analyze a comprehensive taxonomy of the topic.
Considering the abundance of scientific contributions towards HMI in I4.0 and the lack of a
comprehensive study attempting to capture and structure the entirety of the topic’s facets, the
development of a taxonomy has been chosen as an appropriate tool to illustrate an integration of
the topic’s various sub-aspects.
For this purpose, the methodological approach of a structured literature review in the form of
a survey has been applied in order to identify all of the most relevant aspects of the topic and
to ground the derivation of a taxonomy on a broad basis of profound scientific publications. The
overall approach, illustrated in Figure 1, comprises four major methodological steps which are the
initial collection of a literature sample, the subsequent filtering of this collection, the derivation of
a taxonomy based on the filtered final sample, and the analysis of this taxonomy. The latter step, in
turn, comprises the analysis of focal points in research on the topic of this paper and of potential
patterns in the corresponding literature.
Sample Collection 
Filtering of 
the Sample 
Derivation 
of a 
Taxonomy 
Analysis 
of the 
Taxonomy 
Analysis of 
Focal Points 
Analysis of 
Patterns 
Fig. 1. The Overall Approach Applied in the Course of this Survey
The aim is to develop a taxonomy reflecting past and current scientific efforts in the field which
can, consequently, serve as an orientation for related researchers concerning available contributions
and opportunities for further research. In particular, the taxonomy aims to grant inspiration for
novel perspectives on unexplored combinations and interactions of two or more different facets
of HMI in I4.0. Therefore, based on a large-scale survey, the taxonomy is supposed to integrate
various, possibly heterogeneous perspectives of different authors.
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 12

12
Krupitzer et al.
4.1
Literature Search for Initial Sample Collection
In a first step towards developing a taxonomy, potential scientific literature representing candidates
for the final sample of relevant publications had to be collected.
For this purpose, an approach comparable to the search procedure in a survey by Lu [39] was
chosen which is based on Webster & Watson [84]. However, the steps of going forward and
backward, i.e. of including both the articles citing the publications identified in the keyword search
and the articles cited by the identified publications, have been omitted.
Instead, the approach applied for sample collection includes the development of a rich set of
keywords for literature search as well as the choice of keyword combinations to be used for search
and of search platforms for implementation of the search. The subsequent steps comprise the actual
conduct of several search rounds using different keyword combinations and search platforms and
the corresponding decision which of the search results to include in the initial sample.
Development of a 
Set of Keywords 
for Search 
Choice of 
Keyword 
Combinations 
Choice of 
Search 
Platforms 
Conduct of 
Several 
Search Rounds 
Choice Which 
Results to Use 
11 Different 
Keywords 
15 Different 
Combinations 
Google Scholar 
IEEE Xplore 
20 Search 
Rounds 
504 Results 
Used 
Fig. 2. The Approach Applied for Collection of the Initial Sample
The intention in relying on this approach, illustrated in Figure 2, instead of following Webster &
Watson [84] in going backward and forward has been to minimize the risk of remaining within
a specific scope of research determined by the direction of the starting articles, i.e. the starting
points for going forward and backward. Instead, the aim has been to achieve a comprehensive
sample of publications representing different research streams and scientific perspectives on the
topic. Besides, as described further below, the applied approach has resulted in a final sample of
substantial size, making a procedure of going backward and forward for every article in the sample
impractical under the scope of this paper.
Regarding the identification of a set of keywords, considering the explicit focus of the paper
on HMI in an I4.0 environment, the rationale was to combine a diverse collection of keywords
aiming at HMI aspects with either Industry 4.0 or the German Industrie 4.0 occasionally
used in scientific publications (see Section 2.3.1). This means that, for every search round, a specific
keyword aiming at the HMI aspect was combined with either Industry 4.0 or Industrie 4.0.
The overall set of keywords covering the HMI aspect comprises Human-Machine Interaction,
HMI, Virtual Reality, VR, Augmented Reality, AR, Human Role, Human-Centered Design, and
Human-Machine Collaboration and is presented in Table 2 together with the I4.0 keywords.
Regarding the choice of a platform or digital library for implementation of the search, Google
Scholar was chosen as the initial search medium. The reason for deploying Scholar was to increase
the chances of identifying literature from diverse research streams, publishing entities, and possibly
even scientific disciplines for a sample covering multiple perspectives on HMI in I4.0.
However, the opening search round using the string Human-Machine Interaction Industry
4.0 revealed the general observation that coverage in Google Scholar exceeds the aspired broadness
of range by returning tremendous amounts of search results. Judging by titles, those results became
ever less focused on topics related to HMI in I4.0 the lower down the paper in the order of results
returned.
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 13

A Survey on Human Machine Interaction in Industry 4.0
13
Keywords Covering the HMI Aspect
Keywords for the I4.0 Aspect
Human-Machine Interaction
HMI
Industry 4.0
Virtual Reality
VR
Industrie 4.0
Augmented Reality
AR
Human-Centered Design
Human Role
Human-Machine Collaboration
Table 2. Keywords for Literature Search
Besides, those results revealed that a significant amount of articles with more suitable titles
stemmed from Institute of Electrical and Electronics Engineers (IEEE) sources which is why, for
the fifteen subsequent search rounds, IEEE’s digital library IEEE Xplore was used instead of Google
Scholar. Thereby, the thematic focusing of search results was supposed to be enhanced.
As a matter of fact, search rounds on IEEE Xplore returned significantly less results than provided
by Google Scholar. While the initial round on the latter platform had returned more than 9,000
results, the highest number of articles returned in a single round on Xplore was 24. Therefore, all
results returned by Xplore have been included in the initial sample whereas Scholar results have
only been taken into consideration up to a maximum of 200 results per search round.
Overall, a total of twenty search rounds has delivered an initial sample of 504 search results. As
described above, the first round was conducted using Google Scholar while the following fifteen
search rounds were implemented on IEEE Xplore. In order to further expand the sample of 323 search
results after these first sixteen rounds and to avoid an overly narrow focus on IEEE publications,
the final four search rounds delivering the last 181 results for the initial sample were conducted on
Google Scholar again.
4.2
Filtering of the Sample
Having collected a total of 504 search results as an initial sample for this survey, a crucial step in
advance of developing a taxonomy of HMI in I4.0 has been to sort out those instances of the sample
which were either redundant, not available for access, represented non-scientific publications, or
proved to be focused on topics irrelevant to the development of the taxonomy. By eliminating
the first three types of results from the initial sample, an intermediate sample of 330 articles was
generated before a detailed analysis and evaluation of content-related match of those articles
with the research focus of this paper has led to an eventual elimination of another 141 articles, as
illustrated in Figure 3. Thus, the final sample comprises 189 publications representing the basis for
the development of a taxonomy of the topic.
In the following, this section describes the process of filtering the initial sample, as illustrated in
total in Figure 3, stepwise and in more detail.
4.2.1
Elimination of Redundant and Unsuitable Literature. A first step in filtering the initial collection of literature has been to identify all instances of the same publication occurring multiple
times in this sample. In case of such duplications, only the article collected in the earliest respective
search round has been retained for the intermediate sample. In rare cases, duplicated articles from
later search rounds have been retained instead of an earlier collected instance if the publication type
of the article collected later was of higher priority, in the order of journal article over conference
proceeding over working paper.
Overall, among the 504 search results included in the initial sample, 353 distinct publications
have been identified whereas each of the remaining and discarded 151 instances represented a
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 14

14
Krupitzer et al.
189 
330 
504 
Keyword Search: 
Initial Sample: 504 Publications 
– Duplications: 
– Inaccessible: 
– Non-Scientific: 
– 151 Instances 
– 11 Instances 
– 12 Instances 
Intermediate Sample: 330 Articles 
– Unsuitable 
– Thematic Focus: – 141 Articles 
Final Sample: I 189 Articles 
Fig. 3. Process of Filtering the Initial Literature Sample
duplication, either in the form of a direct copy, as the same work published via a different channel,
or e.g. as the published German version of an English publication among the 353 distinct instances.
In a next, straightforward step, the retained 353 publications have been filtered for those not
available for a detailed analysis due to the publishing entity denying access to the full text of the
article. In total, eleven publications and their full texts have been inaccessible and, thus, have been
removed from the sample.
Finally, another twelve publications have been removed from the sample of distinct search results
because they did not represent a type of article conforming to standards and requirements of
scientific publications. Among those, five articles represented white papers published by corporate
entities, mostly consulting firms, and another five were publicly available patents. Lastly, one search
result in the form of a collection of presentation slides instead of an actual article and one published
Master thesis were discarded.
Altogether, removing 151 duplicated, eleven inaccessible, and twelve non-scientific publications
from the initial sample of 504 search results led to an intermediate sample of 330 articles representing
the basis for the in-depth analysis of literature contents towards the development of the taxonomy.
In the course of reading and analyzing the contents of the articles included in the intermediate
sample, 141 papers have been identified as focusing on topics irrelevant to the scope of this paper.
Therefore, in a final step in filtering the sample of search results, they have been removed from the
intermediate sample.
In some cases, examining the title and abstract has sufficed to unequivocally determine that
the respective article concentrated on topics irrelevant to this paper. In contrast, papers actually
dedicated towards I4.0 have been read thoroughly before potentially deciding that they did not
sufficiently cover aspects relevant to a taxonomy of HMI in I4.0 in order to be included in the final
sample.
The following section describes the properties of the resulting final sample of 189 scientific
publications which constitutes the basis for all of the following analyses conducted and presented
in the course of this paper.
4.2.2
Description of the Final Sample. The composition of the final sample can be analyzed with
respect to different characteristics of the articles included. In particular, the final sample has been
examined regarding the distribution of publication years and types as well as regions of origin
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 15

A Survey on Human Machine Interaction in Industry 4.0
15
among the total of 189 articles. In addition, the distribution of publication types has been scrutinized
for conferences, (volumes of) specific journals, or books and book series more strongly represented
within the sample.
The first notable fact when examining the articles’ publication years is that there are three
instances from a period before the actual establishment of the term and the concept of I4.0. The
reason for including those articles into the final sample despite their age is the relevance and
affiliation of their contents towards the focus of this paper, contributing insights concerning
the cooperation of workers and robots in assembly lines in order to enhance flexibility [33], a
methodology for the analysis of quality in HMI [45], and a very early and visionary concept of a
human-machine interface implementing VR aspects [65].
Apart from this triple of articles, only scientific publications from after 2012 are included in the
final sample, with the largest share of 72 articles (38.1%) stemming from 2016. In general, the vast
majority of publications stems from the period between 2015 and 2017, with another 22.2% and
21.7% of articles published in 2015 and 2017, respectively.
Figure 4 presents an overview of the overall distribution of years of publication in the final sample
including information on the respective types of publication as well as the corresponding overview
for the distribution of types of publication. Noticeable in this regard is the fact that, relating to the
main period from 2015 to 2017, the proportion of journal articles among the sample instances is by
far the highest while, for the year before and after that period, conference proceedings represent
the highest share.
0
10
20
30
40
50
60
70
80
1999
2002
2009
2013
2014
2015
2016
2017
2018
No. of Publications 
Other/Reports
Working Papers
Books
Conference
Proceedings
Journal Articles
0
20
40
60
80
100
Journal Articles
Conference
Proceedings
Books
Working Papers
Other/Reports
No. of Publications 
2018
2017
2016
2015
2014
2013
2009
2002
1999
Fig. 4. Distributions of Years and Types of Publication in the Final Sample
The predominant role of journal articles also applies to the overall sample, as can be inferred
from Figure 4 as well. More than half of the sample papers were published in a scientific journal,
the vast majority of which in the period from 2015 until 2017 and particularly in 2016, whereas
conference proceedings make up a little more than a third of the sample and 8.5% of the articles
were published in the form or as part of a book. The years of publication concerning conference
proceedings and books are a little more evenly distributed among the five-year period from 2014 to
2018 compared to journal articles.
Besides, the final sample comprises two published working papers focusing on topics relevant to
the scope of this paper and another couple of articles or reports published by the German political
foundation Friedrich-Ebert-Stiftung also covering aspects relevant to this paper and authored by
renowned German scientists.
On a more detailed level, it is worth examining the list of actual journals, conference proceedings,
and books included in the sample. In total, the final literature sample comprises articles from 44
different scientific journals, conference proceedings from 54 series of scientific conferences, and
thirteen distinct published books, nine of which are instances of one of eight different book series.
Table 3 presents an overview of all journals and conferences represented at least threefold and of
books and book series represented at least twice within the final sample of this paper. This includes
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 16

16
Krupitzer et al.
Scientific Journals
Journal
No. of Occurrences
Vol.(No.) [No. of Occurrences]
Procedia CIRP
28x
17 [2x] 29 [1x] 30 [1x] 32 [1x] 40 [1x] 41 [4x]
44 [2x] 46 [1x] 53 [1x] 54 [5x] 55 [1x] 56 [2x]
57 [2x] 59 [1x] 63 [3x]
IEEE Access
6x
5 [1x]
6 [5x]
Procedia Manufacturing
5x
1 [1x]
9 [1x]
11 [2x]
13 [1x]
CIRP Annals
3x
58(2) [1x]
65(2) [2x]
Computers in Industry
3x
65(2) [1x]
83 [1x]
89 [1x]
IEEE Computer Graphics and Appl.
3x
35(2) [3x]
IFAC-Papers On Line
3x
48(3) [2x]
49(19) [1x]
Procedia Engineering
3x
69 [1x]
100 [1x]
182 [1x]
Conference Proceedings
Conference
No. of Occurrences
Conference Edition [No. of Occurrences]
IEEE Conference on Emerging Technologies & Factory Automation
4x
2014 19th [1x] 2015 20th [3x]
IEEE Int’l Conference on Industrial Informatics
4x
2014 12th [1x] 2016 14th [2x] 2017 15th [1x]
Hawaii Int’l Conference on System Sciences
3x
2016 49th [3x]
IEEE Int’l Conference on Industrial Technology
3x
2016 [2x] 2017 [1x]
Books
Book
No. of Occurrences
Advances in Production Technology
3x
Service Orientation in Holonic and Multi-agent Manufacturing
2x
Book Series
Book Series
No. of Occurrences
Volume [No. of Occurrences]
Lecture Notes in Production Engineering
3x
n.a.
IFIP Advances in Inform. and Comm. Techn.
2x
488 [1x]
513 [1x]
Studies in Computational Intelligence
2x
594 [1x]
640 [1x]
Table 3. Frequently Occurring Publication Mediums Among the Final Sample
detailed information on the respective volume and number, if applicable, of the journal, edition of
the conference, or volume of the book series as well as the exact number of distinct occurrences of
these published instances within the final sample.
Finally, the countries of origin of the articles have been analyzed. More precisely, for every
publication in the sample, the country where the affiliated organization of the author(s) is domiciled
has been determined. For that purpose, in case of various authors with differing geographic
provenience, the country of origin of the article has been decided based on majority votes. In case
of a tie, the country of the corresponding author’s affiliated organization has been chosen, whereas
in case of a lack of information concerning the corresponding author, origin has been based on the
leading author.
Overall, publications from 32 different countries are included in the final sample. Ten of those
countries appear exactly once, the same number of countries is represented twice among the
sample. Another six countries, all from Europe, appear four times within the sample. Finally, five
publications stem from Australia and Sweden, respectively, seven articles originated in China, ten
in Spain, eleven in Italy, and 97 in Germany, which seems less striking when considering the overall
origination of the I4.0 concept.
Summarizing on a broader level, 1.1% of publications included in the final sample stem from
South America, 1.6% from Africa, 2.7% from North America, 3.7% from Australia and Oceania, 6.9%
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 17

A Survey on Human Machine Interaction in Industry 4.0
17
Fig. 5. Countries of Origin of Sample Articles
from Asia, and the vast majority of 84.1% from a European country. The distributions of countries
and continents of origin are illustrated in the form of corresponding heatmaps in Figure 5.
4.3
Analysis and Structuring of Literature Contents in the Final Sample
Based on the collected and filtered final sample of relevant scientific literature, fundamental data
on the articles’ contents has been collected and documented for the development of a taxonomy of
HMI in I4.0 as well as for all subsequent analyses in this paper. For this purpose, every paper of the
final sample has been read and analyzed thoroughly in order to identify the entirety of aspects of
HMI in I4.0 addressed by the respective article.
To be more precise, a Microsoft Excel spreadsheet has been created serving as a tool for detailed
documentation. A row has been dedicated for every article while each column, besides the one
for the respective year of publication, represents a specific attribute identified as relevant to the
development of a taxonomy of HMI in I4.0 during perusal of sample papers. In the course of
analyzing an increasing number of papers, this collection of attributes had grown to reach an
interim number of 154. Accordingly, the contents of all 189 sample articles have been analyzed,
documenting for every article and attribute, in the respective cell of the spreadsheet, whether the
attribute is addressed in the respective paper.
In order to derive a meaningful taxonomy of HMI in I4.0 from this massive and largely unstructured collection of data, the identified attributes have been clustered according to superordinate
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 18

18
Krupitzer et al.
categories of the topic which they represent instances of. These categories, again, have been clustered according to the topic’s focal points they address and then organized by arranging them in a
hierarchy.
In doing this, the overall concept of HMI in I4.0 has been structured and systematically mapped
in a taxonomy classifying the topic according to categories arranged in a three-level hierarchy. The
structure of the hierarchy implies a detailing and further partitioning of elements from first-level
categories down to third-level categories. Below the third level, the initial attributes are grouped
according to the respective category which they represent a specification of.
For the final taxonomy and the following analyses of the paper, similar attributes have been
merged and dispensable categories and attributes not essential to a comprehensive but, at the same
time, focused description of the topic have been removed. Therefore, the final taxonomy and its
three-level hierarchy of thematic categories are based on a foundation of 113 attributes for which
coverage in each of the 189 sample articles has been documented thoroughly in the spreadsheet.
4.4
Analysis of the Data Collected for Content Documentation
Besides the initial development and derivation of the actual taxonomy, the detailed documentation
of the article contents has served another purpose. In particular, the collected data set enables a
quantitative analysis of the distribution and patterns of research interest among different thematic
aspects complementing the qualitative structuring of the topic into a taxonomy of HMI in I4.0. The
following subsections outline the methodology and steps implemented for this purpose which are
an analysis of the relative frequencies of different taxonomy elements among the final sample as
well as the application of machine learning algorithms for the purpose of data mining.
4.4.1
Analysis of the Relative Frequencies of Individual Taxonomy Elements. In order to reveal
potential disparities in the coverage of individual taxonomy elements among the entirety of sample
articles, the total number of papers addressing each respective attribute of the taxonomy has been
determined. Dividing this number by the overall size of the sample (189) has yielded the relative
frequency of an attribute, stating the percentage share of articles discussing the concerned element.
Knowing the relative frequencies allows for a detection of those instances representing a focal
point of research on the topic of HMI in I4.0.
However, general research streams might not concentrate only on specific bottom-level attributes
but, instead, focus on larger subsections of the taxonomy, represented by higher-level categories. In
particular, if different authors consider varying attributes or manifestations of the same category,
they still address the same higher-level aspect of the overall topic. Therefore, the Microsoft Excel
documentation of attribute coverage has been extended to reflect also the prevalence and relative
frequencies of higher-level categories among the final sample. For this purpose, a specific category
has been marked as addressed by a respective article if the same applies to at least one of the
attributes belonging to this category.
4.4.2
Data Mining on the Documented Literature Contents. As a final step in the analysis of the
taxonomy, data mining techniques have been applied to the underlying data reflecting the contents
of the sample articles. The aim of mining the documented article contents is to uncover underlying patterns of research streams and related sub-aspects of the topic as potentially indicated by
associations and interrelations present among the content-related sample data. For this purpose,
a two-fold approach has been applied in order to scrutinize the collected data for both implicit
association rules and classification rules to be derived from the data.
Regarding implementation, a set of machine learning algorithms has performed the data mining
process. For that purpose, the open-source Waikato Environment for Knowledge Analysis (Weka)
workbench developed at University of Waikato, New Zealand has been deployed which provides a
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 19

A Survey on Human Machine Interaction in Industry 4.0
19
rich set of readily available machine learning algorithms [86]. For the analyses in the course of this
paper, three of those algorithms have been deployed. Those are the Apriori algorithm searching for
the best association rules according to specifiable parameters as well as the classifiers Zero R and
JRip.
Initially, following the CRoss Industry Standard Process for Data Mining (CRISP-DM) process
model, the aims targeted at in applying data mining techniques have been determined by formulating
the research questions RQ3.1 and RQ3.2 (business understanding).
Based on the collected set of data available and the research questions pursued, the decision
has been made to reduce the data set reflecting sample literature contents to a level of specifying
prevalence of only the third-level categories of the taxonomy. Thus, individual attributes and
categories of the first and second level as well as data on their coverage in sample articles have
been removed from the data set (data preparation).
Determined in the data understanding phase, the reason for studying data on third-level categories
instead of attributes of the taxonomy is the lower number of categories compared to attributes.
Thus, chances are higher for the algorithms to identify meaningful associations and relations in
the data due to a lower ratio of attributes2 to sample instances in the data set [88]. First- and
second-level categories, on the other hand, are discarded in order to avoid auto-correlation among
sample data, given that coverage of a lower-level category implies coverage of its superordinate
categories.
The first algorithm applied on the reduced data set in the modeling phase is the Apriori algorithm
to find association rules within the data [89]. This means that item sets, i.e. attribute values or
combinations of values of different attributes, are searched which, when observed within a sample
instance, appear together with a specific value of another attribute [89].
Finally, the Weka workbench has also been applied in order to identify models classifying
instances regarding the value of a specific attribute in the data set, called the class [86]. The aim
for the algorithm deployed is to determine a set of e.g. rules or a function which enables predicting
the value of the class if the set of values of the other attributes is known for a specific instance
[86]. For this purpose, the algorithm requires a data set as input, called the training set, used for
learning and identifying the classification model. The aim is to determine a model classifying any
conceivable instance from the real world, i.e. of the overall population, as accurately as possible.
The accuracy of the model derived from the training set, i.e. from an assumed random sample of
the population, should be evaluated on another independent sample, the test set [87].
Weka offers stratified cross-validation as a testing option for classification models which is used
with ten folds in this study as part of the evaluation phase of CRISP-DM. In ten-fold stratified
cross-validation, the group of instances in the overall data set is split into ten equal parts where,
in each fold, the values of the class attribute are distributed according to their distribution in the
overall data set [87]. Then the algorithm performs ten rounds of building a classification model
based on a training set comprising nine of the ten folds and each time tests the model’s classification
accuracy on the tenth fold whereby each fold serves as the test set once. In an eleventh round, the
algorithm uses the entire data set as training set to develop the final classification model whose
accuracy is estimated to be the mean of the tested accuracies of the previous ten rounds [87].
For the purpose of this study, the used classification algorithm has been run ten times for
every class attribute using a different seed value for the randomization procedure inherent to
the algorithm in each round. The mean of the ten accuracies, each one estimated using ten-fold
2Attributes in the context of Weka applications refer to the properties of the data set used as input for the machine
learning algorithms, not to the bottom-level elements of the taxonomy.
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 20

20
Krupitzer et al.
stratified cross-validation respectively, is supposed to represent a more reliable estimate of the true
accuracy of classification models produced by the algorithm for the respective class [87].
From the multitude of available classification algorithms in the Weka workbench, JRip has been
chosen to identify a model for each attribute. However, the classification model produced by JRip
has not been accepted in case its estimated accuracy turned out lower than the baseline accuracy
of the classification model delivered by the Zero R algorithm (evaluation phase). The Zero R model
neglects any attribute value in predicting an instance’s class value because Zero R only delivers one
simple unconditional classification rule stating that the class value of any instance is predicted to
be the specific class value appearing most frequently among all instances of the training set [87].
As another means of verifying the meaningfulness of the models accepted based on a comparison
to the baseline accuracy, Receiver Operating Characteristics (ROC) area values of those models have
been examined which should be greater than 0.5 (cf. [54]). A more detailed rationale for applying
JRip and considering Zero R and ROC area values for evaluation purposes is provided in Section
6.2.2.
5
RESULTS RQ1: A TAXONOMY OF HUMAN-MACHINE INTERACTION IN
INDUSTRY 4.0
After the detailed description of the methodology applied in this study, the following section
presents the initial principal outcome and result of the implemented analyses. In particular, this
means that the first main research question motivating this paper, i.e. RQ1, is supposed to be
answered by providing a structuring of the overall topic of HMI in I4.0 in terms of a comprehensive
taxonomy.
As stated in subsection 1.2, RQ1 asks what the current state of the art in HMI research in the
area of I4.0 is. In order to holistically capture the concept of HMI in I4.0 as discussed in scientific
literature, its various facets and sub-aspects have been captured, systematically structured, and
described in terms of a comprehensive taxonomy. This model, illustrated in Figure 6, reflects the
focal points and analytic approaches towards the topic deployed in related research.
As can be deduced from Figure 6, the taxonomy is subdivided into three top-level categories
corresponding to the main features of the topic represented by Human, Machine, and Interaction.
The rationale behind this classification is to highlight the distinction between the two major types of
intrinsically different agents in I4.0 scenarios, i.e. the human operator and the machine entity. Still,
in the course of HMI processes, these two types of actors are supposed to interact and collaborate
purposefully and successfully as an integral part of I4.0 activities. This potentially complex and
sophisticated interaction implicates a variety of different facets to analyze and take into account if
HMI in an I4.0 environment is supposed to function appropriately which is why the third category
besides the human and machine entity is dedicated towards their interaction.
Shifting the focus to a broader perspective of examining the overall taxonomy, Figure 6 reveals
that, on the second level of hierarchy, both the human and interaction category comprise four subcategories, respectively, while the machine part is detailed into three spheres on the intermediate
level. Finally, on the lowest level of categories constituting the taxonomy, the human sector
comprises eleven distinct elements, the interaction part entails ten subcategories, and the machine
subsection adds another eight detailed categories to the taxonomy.
In the following, this section describes each of the three top-level categories and their respective
lower-level elements in more detail, including overviews over the detailed attributes representing
the bottom level of the hierarchy.
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 21

A Survey on Human Machine Interaction in Industry 4.0
21
Human
Machine
Interaction
Visualization of
Data and Information
Fig. 6. A Taxonomy of HMI in I4.0
5.1
The Human Dimension
Starting with the Human subsection, the structure of the taxonomy shall be described down to the
lowest level of elements, i.e. the attributes. For that reason, Figure 7 displays the corresponding
subsection of the overall taxonomy, complemented by a table specifying the respective attributes
of the bottom-level categories.
Considering the human entity in processes of HMI in I4.0, four major aspects can be identified
and distinguished, namely the tasks to be performed by human operators in future manufacturing
activities, the role humans are supposed to assume in complex I4.0 production systems, the demands
placed on staff in order to be able to fulfill those designated tasks and roles, and the requirements
regarding the available educational and qualifying measures to be provided by governmental and
corporate entities in order to provide for the future I4.0 workforce.
Tasks. The tasks of human operators in I4.0 operations, in turn, can be described in terms of
their characteristics and the actual types of activities they encompass. According to insights from
relevant scientific literature included in the final sample, human tasks in I4.0 will be diverse and
novel and continue to evolve quickly (e.g. [11, 28]). While some authors expect human tasks to
be highly process-oriented (e.g. [77]), human operators will also be expected to perform those
spontaneous activities that are difficult to foresee and plan in advance (e.g. [68]).
Accordingly, an important type of human tasks in I4.0 operations will be the intervention in case
of failure (e.g. [56]). Besides, an important scope of human activities will be the mental work of
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 22

22
Krupitzer et al.
Human
chine
Fig. 7. A Taxonomy of HMI in I4.0 - Human subsection
planning and engineering, thus specifying processes and production plans whose implementation
and consequential output human operators then monitor and verify, respectively (e.g. [18]). On the
other hand, I4.0 activities might still imply more hands-on tasks for human operators, in particular
manual assembly and machine operating (e.g. [20]). What combines most of those activities in I4.0
is that the vast majority might, to some degree, entail the interpretation of data and information
provided for the execution of a specific task (e.g. [90]).
Roles. In performing the tasks described, human operators will assume specific roles within
I4.0 processes, especially with regard to a differentiation from the role of machine entities in HMI
procedures. With a more strategic outlook, employees are supposed to act as decision-makers
and coordinators concerning the alignment of value creation processes (e.g. [68]). Besides, human
agents are seen as a source and potential producers of knowledge in the organization (e.g. [53]).
From a more operative perspective, human operators are expected to assume the role of a flexible
problem-solver and of a controlling instance and supervisor of ongoing activities. Altogether,
this implies an increase in the degree of responsibility employees throughout the organizational
structure, down to shop floor operators, are supposed and entitled to assume (e.g [18]).
Finally, a couple of authors also shift the focus on the human role away from solely considering
employees and towards the role as a customer in an I4.0 environment where innovative digital and
online solutions enable the customer to actively participate in product design or configuration (e.g.
[83]).
Demands on Staff. Coming back to the intra-firm perspective on employees, the demands
placed on staff in comparison to industrial activities prior to I4.0 inception are considered to be
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 23

A Survey on Human Machine Interaction in Industry 4.0
23
3rd-Level Category
Attributes
Characteristics
{new;
manifold/diverse;
fast-changing;
short-term/
hard-to-plan;
process- instead of technology-oriented}
Activities
{planning/specification/engineering; monitoring; verification; interpretation of prepared data & information; machine operating; manual
assembly; troubleshooting/intervention in case of failure}
in More Strategic
Activities
{decision-maker; coordinator of value creation; producer/source of
knowledge}
in More Operative
Activities
{flexible problem-solver; more responsibility; controlling instance and
supervisor of ongoing activities}
as Customer
{participation in product design}
Compared to preIndustry 4.0
{new demands; extended demands; further training required}
Personality Traits
{flexibility; responsibility}
Skill Set
{abstraction/comprehensive process thinking; inter-disciplinary skills;
social skills; media skills; quantitative/IT skills; technological skills}
Training Methods /
Qualifying Strategies
{lifelong
learning/continuous
professional
development;
interemployee knowledge transfer; training on the job/work-integrated
learning}
Means of Skill and
Knowledge Mediation
{new training forms/educational system; learning factories; personalized training; round-based training concept; virtual training}
Educational Subject /
Content
{training on new technologies; MINT education}
Table 4. Dimensions of the Human subsection
partly new and extended which, as a consequence, requires employees to undergo further training
(e.g. [60]).
With regard to the expected personality traits of employees, working in an I4.0 environment will
require both a certain degree of personal flexibility and a necessary sense of responsibility (e.g. [3]).
Looking more precisely at the actual skills employees are expected to provide, these can be both
more generalist or more specialized. This means that the required skill set might comprise the
capability for abstraction and comprehensive process thinking, social skills, and inter-disciplinary
skills (e.g. [23]), as well as quantitative and IT, media, and technological skills (e.g. [3]).
Considering the extent and broadness of demands on staff, employees will need to be willing to
undergo qualifying measures, likely in the form of lifelong learning during the entire professional
career (e.g. [93]). Besides, learning on the job and from colleagues in the course of inter-employee
knowledge transfer represent vital opportunities for staff to acquire crucial skills and knowledge
(e.g. [50]).
Demands on Qualifying Measures. The last interim-level category picks up on the aspect of
qualifying the future I4.0 workforce, specifying demands placed on governments and firms concerning educational and training opportunities to be offered. Regarding the actual educational content
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 24

24
Krupitzer et al.
offered, sample literature mainly concentrates on training on new technologies and education in
MINT subjects (e.g. [28]).
Besides, the taxonomy differentiates among specific means of knowledge and skill mediation
addressed among the sample articles. While, in general, new training forms and an adjustment of
the educational system are requested (e.g. [71]), learning factories and personalized training are
the most often-cited specific means of effectively imparting necessary knowledge to trainees (e.g.
[19]). In addition, forms of computer-aided virtual training and a round-based training concept, e.g.
incorporating gamification elements, are considered to be potentially appropriate and useful (e.g.
[17]).
5.2
The Machine Dimension
As indicated above, the Machine subsection of the taxonomy is split into only three interim-level
categories, which describe and define the role and functionality machine entities assume and
provide in HMI processes as opposed to the role and the tasks of human actors, the type and
means of visualization of data and information, and the hardware components deployed for those
purposes. Again, the corresponding part of the overall taxonomy, complemented by a table listing
the respective attributes of the third-level categories, is illustrated in Figure 8.
Machine
Visualization of
Data and Information
Fig. 8. A Taxonomy of HMI in I4.0 - Machine subsection
Role/Functionality. As can be inferred from Figure 8, the machine entity can assume both
a passive and an active role in HMI procedures under I4.0, providing functionality either rather
passively or rather proactively, while an exact definition of the boundaries depends on the individual
case.
Assuming a passive role, the machine entity can provide a functionality of monitoring manual
workflows (e.g. [85]) or diagnosing roots of emerging problems, both machine-internal and external
(e.g. [58, 90]). A particularly crucial passive functionality is the continuous collection, aggregation,
preparation, and visualization of data and information (e.g. [18]), e.g. in order to facilitate human
operators’ fulfillment of the role of a strategic decision-maker.
Providing more active functionality, the automated system actively supports and assists the
human actor, also comprising active physical support as a means of compensating e.g. for decreasing
human capabilities with rising age of employees (e.g. [60]). Besides acting as a mere assistant for
human operators, machine entities can assume the role of an active and equal collaborator of
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 25

A Survey on Human Machine Interaction in Industry 4.0
25
3rd-Level Category
Attributes
Passive
{collection, aggregation, preparation, and visualization of data & information; monitoring of manual workflow; (self-
)diagnostics}
Active
{implementation; support and assistance for the human; collaboration with humans on joint tasks}
Augmentation Technique for the
Visual Field
{adding realistic virtual objects; modifying the user’s view; adding graphics from traditional illustration (distinct from
reality)}
Technology for Information Display
{video see-through; optical see-through; (in-situ) projection}
Context-Awareness
{sensors; positioning systems; RFID chips}
Hybrid Input-Output Platforms
{hand-held (e.g. tablet, smartphone)}
Output Platforms
{stationary screen/monitor; HMD (stereoscopic); HMD (monoscopic); HMD (no further details)}
Input Platforms
{manual controllers; other mechanical control devices (e.g. keyboard, foot pedal); camera (image capturing); wearable
sensors (motion capturing)}
Table 5. Dimensions of the Machine subsection
humans on joint activities, sharing and dividing tasks according to the respective strengths (e.g.
[79]). As another active functionality complementary to the tasks of the human operator specified
in subsection 5.1, the machine entity can implement the production strategies and plans specified
by a human (e.g. [18]).
Information Visualization. Concerning visualization of data and information, scientific literature differentiates among various techniques to augment the perceived view of the recipient
of information while there are different technologies available to display this information to the
human eye.
For the former, literature differentiates among three techniques to modify and enhance the visual
perception of a human user which are examined and deployed in various combinations in different
articles. The visual field can be enhanced by adding realistic 3D virtual objects to the real-world
view or by adding common graphical elements from traditional illustration, e.g. arrows, which are
clearly distinct from the underlying view of reality. Besides, the general view of the environment
can be modified by changing contrast or color saturation (e.g. [46]).
As a means of implementing those visual augmentations, different technologies are available
to display information to the human eye. An intuitive solution is the use of video see-through
technology displaying digitally enhanced camera footage of the real world on a screen (e.g. [52]).
As an alternative technology, optical see-through is available, allowing the user to retain a view of
the actual environment through a transparent medium like glass and displaying only the added
virtual objects digitally (e.g. [14]). Hence, in contrast to video see-through solutions, the user’s
view of the real world will remain intact in case of a shutdown of the digital display [70]. This
advantage also applies to the third information display technology covered in sample articles which
is in-situ projection deploying physical objects from the environment as a screen surface upon
which a projector projects digital information and images (e.g. [16]).
Hardware Components. In order to complement the description of the machine entity in HMI
processes under I4.0, the taxonomy includes a specification of the hardware components employed
in order to implement the machine’s functionality and information visualization. In this context,
articles included in the final sample discuss different ways of achieving context-awareness of the
automated system and different hardware platforms for user input and visual output as well as
hybrid input-output platforms.
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 26

26
Krupitzer et al.
As a means of achieving context-awareness of CPSs, a multitude of sensors like power meters,
accelerometers, thermometers, or others [36] as well as radio-frequency identification (RFID) chips
and positioning systems like Global Positioning System (GPS) and indoor solutions (e.g. [18]) are
available.
Besides, an important aspect of HMI process design in I4.0 is the choice of respective input and
output platforms. In this regard, common hand-held devices from the consumer market, i.e. mainly
tablets and smartphones, represent a hybrid solution potentially suitable for industrial applications
as well (e.g. [41]).
Regarding dedicated output platforms used for visualization purposes, different studies address
either stationary screens and monitors (e.g. [37]) or different types of HMDs like smart glasses
although authors only rarely define whether the respective study focuses on stereoscopic or
monoscopic HMDs (e.g. [27]).
Finally, designated input platforms serving as a means for human user input can be represented
by mechanical devices like manual controllers (e.g. [35]) or other control devices like keyboards
and foot pedals (e.g. [15]). Besides, user input can be registered by cameras in the form of image
capturing of the user and by wearable sensors directly capturing user motion (e.g. [31]).
5.3
The Interaction Dimension
The subsection of the taxonomy describing the character of interaction between human and machine
entity in I4.0 is split into four categories defining the location and the means of interaction, the
UIs employed, and the goals of interaction. Figure 9 provides a comprehensive overview over this
Interaction part including a detailed enumeration of the attributes specifying the third-level
categories.
Mach
Interaction
Fig. 9. A Taxonomy of HMI in I4.0 - Interaction subsection
Location of Interaction. The Interaction part of the taxonomy analyzes the intra-firm location of HMI with respect to the organizational structure, i.e. functional units, and the physical
location of interaction. The latter can be either fixed to a specific workplace where HMI occurs,
or modern technologies featuring ubiquitous connectivity and information availability enable
arbitrary interaction possibilities for the human operator (e.g. [18]).
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 27

A Survey on Human Machine Interaction in Industry 4.0
27
3rd-Level Category
Attributes
Employee Physical
Location
{fixed/workplace-bound; arbitrary}
Functional Units
{production/manufacturing; (intra-)logistics}
Machine-to-Human
{messages to human’s device; haptics}
Human-to-Machine
{multi-touch/touch screen; voice control; gesture recognition/mimics; eye gaze}
Application
{planning, design, and simulation; training; process visualization/production monitoring & quality control; maintenance; (remote) robot control; instructions for the
human; navigation; value-added services for providers & clients}
Functionality
{context-/problem-specific reduction of complexity; tracking of component positions; tracking of human position/motion; adding of knowledge components; providing individual feedback; 3D interactive customer tool}
Types
{VR; AR; traditional GUI (WIMP); NUI (post-WIMP)}
Characteristics
{intelligent; web-based; mobile; context- & user group-sensitive}
Interaction Goals
{augmentation of human capabilities; boost of human productivity & quality of
work; reduction of human errors; improvement of human decision quality; improvement in human intervention into automated processes; increase of manufacturing flexibility; customization; improvement of working conditions; reduction of
professional exclusion; increase of training efficiency; increase of human engagement}
Goals for the User Interface
{usability; transparency of system behavior; optimal & dynamic task allocation between human & machine; adaptivity & self-learning; adaption to current situation
at run-time; identification & evaluation of current work procedure}
Table 6. Dimensions of the Interaction subsection
Apart from that, considering the topic, it seems little surprising that a majority of sample articles
analyzes HMI in a production or manufacturing environment. However, the implications of I4.0
for HMI processes are also scrutinized regarding logistics operations, both internal and beyond
company borders (e.g. [2]).
Means of Interaction. A decisive aspect when designing HMI modules for modern I4.0 production systems is obviously the actual means of interaction or, more precisely, of communicating
bidirectionally. In this context, the taxonomy distinguishes between human-to-machine (H2M) and
machine-to-human (M2H) communication. A way for the system to communicate to the user, in
that sense, is to convey messages to operators via their end devices (e.g. [32]) or to control their
attention physically via haptic impulses and feedback (e.g. [53]).
More intuitive ways of communication and interaction have also been established for industrial
H2M communication in the form of touch interfaces ([12]), natural language interfaces, i.e. voice
control, gesture control including machines mimicking human motion, or even interaction via
human gaze, implemented by the machine tracking and interpreting the user’s line of sight (e.g.
[52]).
User Interfaces. A lot of attention in research related to HMI in I4.0 is spent on UIs which the
taxonomy describes in terms of their characteristics, types, functionality, and application scenarios,
the latter being wide and diverse. UIs are deployed for HMI processes in planning, design, and
scenario simulation during product development, in training, monitoring and quality control, as
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 28

28
Krupitzer et al.
well as in maintenance activities (e.g. [58]). More precisely, UIs are applied to convey instructions
to operators, to provide navigation services, i.e. guidance (e.g. [4]), or to enable operators to control
industrial robots, even remotely (e.g. [79]). Besides, advanced UIs can be used to provide valueadded services to providers and especially clients, e.g. by supplying digital manuals for installation
and/or maintenance of delivered products (e.g. [53]).
In order to be suitable for these application scenarios, UIs provide various functionalities. As a
means to avoid overwhelming the user with an abundance of information and selection options, UIs
should implement context- and problem-specific reduction of complexity and information provision
(e.g. [18]). In order to enable navigation and accurate instructions, tracking of relevant components
in the environment and tracking of the actual user are required (e.g. [52]). Considering the size of
regular industrial organizations and the number of human operators, a UI should allow for adding
of knowledge components by the user in order to make them available and accessible for other
users via the UI (e.g. [12]). At the same time, providing worker-individual feedback is important
in many applications like accurate assembly instructions (e.g. [16]). Finally, in reference to the
human role of a customer involved in product design, a potential UI offered online to customers is
supposed to implement a 3D interactive tool for individual product configuration (e.g. [92]).
Regarding possible types of UIs, a typical UI still occasionally employed or studied for I4.0
purposes is the traditional GUI implementing WIMP properties (e.g. [71]). However, more innovative
and intuitive forms of UIs are on the rise and intensely studied in various sample articles. In general,
UIs of a post-WIMP type, so-called NUIs, are addressed in order to facilitate and foster HMI
processes in I4.0 (e.g. [46]). In particular, UIs implementing VR or especially AR have received
significant attention among I4.0-related research (e.g. [49]).
Irrespective of the specific type implemented, UIs in an I4.0 context are mainly characterized
by one or several of the following properties: While generally being described as intelligent in a
number of articles, UIs might, in particular, provide context- and user group-sensitivity, implying
a capability to adapt features like layout, options, and information offered to the current usage
situation at hand (e.g. [18]). Furthermore, depending on the application scenario, various studies
discuss the use of mobile and potentially web-based UIs (e.g. [43]).
Goals. In conclusion of both the description of the Interaction part and of the structure of the
overall taxonomy, the Goals subsection consists of goals for the UI and goals to be achieved by
implementing successful HMI in general.
Concerning the latter, on an individual employee level, human capabilities are supposed to be
enhanced through the interplay with machines in their assistive role described in subsection 5.2
which shall, in turn, lead to an enhancement of human productivity and quality of work and a
reduction in the number of operators’ errors (e.g. [57]). Besides, context-specific provision of data
and information in HMI aims at improving human decision quality (e.g. [75]).
From an overall organizational perspective, HMI aims for a general increase in productivity
by means of improved human intervention into automated processes (e.g. [53]). In addition, combining the strengths of humans and machines in meaningful HMI processes targets at increasing
manufacturing flexibility in order to reach unprecedented degrees of product customization (e.g.
[93]).
Regarding the benefits for the users themselves, HMI processes in I4.0 aim for an improvement
of human working conditions and a reduction of professional and, thereby, social exclusion by
e.g. compensating for declining cognitive and physical capabilities of older employees, securing
employability across different generations of the workforce (e.g. [60]). Working conditions, in
that respect, comprise various factors like occupational health, ergonomics, and safety level at the
workplace. Furthermore, regarding employee development and attitude, relying on appropriate
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 29

A Survey on Human Machine Interaction in Industry 4.0
29
and effective means of HMI is supposed to foster training efficiency and operators’ motivation and
engagement at work (e.g. [68]).
Narrowing the focus to goals for the UIs, the most important aim for any purposeful UI, especially
in industrial contexts, is its usability, comprising e.g. the ease of use, intuitiveness in handling,
and the resulting user experience and acceptance (e.g. [17]). Besides, UIs are supposed to deliver
transparency of system behavior to the user and shall orchestrate an optimal dynamic task allocation
among human and machine entities (e.g. [73]). Therefore, UI development aims at interfaces
featuring adaptivity and learning capabilities so that, ultimately, UIs accurately adapt to the current
situational context at run-time (e.g. [18]). Finally, regarding application for purposes of monitoring
or providing instructions to operators, an aspired UI shall be capable to identify the current process
steps performed by workers in order to evaluate their accuracy and intervene in case of deviations
from the ideal or planned procedure (e.g. [38]).
6
ANALYSIS OF THE TAXONOMY
Having answered RQ1 by defining and describing a comprehensive taxonomy of HMI in I4.0,
the consequential question arises whether there are notable differences in the extent to which
the individual elements of the taxonomy are discussed in the articles of the final sample. This
question is of particular interest regarding RQ2 and the identification of focal points and potential
research streams in the field. Thereby, such concentrations, if identified, can provide orientation for
both researchers and practitioners concerning the state of the art in development and knowledge
regarding different aspects and technologies of HMI in I4.0.
Besides, when analyzing potential research streams on specific sub-aspects of the overall topic
reflected in the final sample of this paper, an important question to answer is RQ3 asking for
identifiable patterns in the data collected on sample literature contents. Therefore, the following
section provides answers to both RQ2 and RQ3 and the respective sub-questions.
6.1
Results RQ2: Main Foci in Related Research
Based on the insights gained from analyzing literature contents in the final sample, the above-raised
question has to be confirmed since there are notable differences in the extent to which different
elements of the taxonomy from the same level of hierarchy are covered and discussed among the
sample articles. In order to substantiate this result, the following section analyzes the prevalence of
top-level to third-level categories of the taxonomy in the final sample.
In the form of a heatmap, Figure 10 presents an overview over the frequencies with which the
individual categories are addressed in the final sample. To be precise, the color coding of a category
indicates the share of articles discussing the respective category by addressing one or more of its
lowest-level attributes.
The top-level categories are subject to a special color coding, given that each one is covered in
the vast majority of sample articles. Still, it is noteworthy that only the Interaction section is
addressed in every paper while 188 of 189 articles discuss the machine entity. Five sample instance,
however, cover the topic of HMI in I4.0 without explicitly considering aspects of the taxonomy’s
Human section.
Regarding the interim- and bottom-level categories, a five-sector scale has been chosen to
visualize differences in the prevalence of individual elements. The lowest three sectors correspond
to the first three quartiles while the top quartile is split into a sector covering the top 10% and the
lower 15% of the highest quartile.
What is noticeable at first glance is that there are remarkable differences in the prevalence
of individual categories and of larger sections of the taxonomy. In particular, the Interaction
section is not just the only top-level category addressed in every sample paper, but it also comprises
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 30

30
Krupitzer et al.
Human
Machine
Interaction
Visualization of
Data and Information
Inner Circle: 
 xi = 100% 
 xi ∈ [ 99% ; 100% [ 
 xi ∈ [ 97% ; 99% [ 
Outer Circles: 
 xi ∈ [ 90% ; 100% [ 
 xi ∈ [ 75% ; 90% [ 
 xi ∈ [ 50% ; 75% [ 
 xi ∈ [ 25% ; 50% [ 
 xi ∈ [ 0% ; 25% [ 
xi: Share of Articles 
 in the Final Sample 
 Addressing Category i 
Fig. 10. Prevalence of the Individual Categories among the Final Sample
the majority of the most frequently examined categories. To be precise, seven of overall twelve
categories discussed in at least 75% of sample articles represent a sub-aspect of the interaction part
in I4.0-related HMI.
On the other hand, there are sub-aspects of the taxonomy which seemingly have been studied
less frequently and intensively in related scientific literature, meaning that less than half of the
sample articles have taken into account attributes of these categories. Regarding the Interaction
part, this only concerns the section defining the different means of interaction and communication
as well as the separate bottom-level categories of UI functionalities and the physical location of
interaction. Similarly, in the analysis of the machine entity, the section describing the visualization
of data and information and the different types of hardware components except for those ensuring
context-awareness have been considered less frequently. In contrast, large parts of the Human
section have been studied less often. Those are the demands placed on the qualification measures
for employees and those placed on staff members themselves as well as the categories of the human
role as a customer and the characteristics of operators’ tasks.
More detailed insights regarding the taxonomy elements which have been studied and considered
relatively intensively, in contrast, are provided and interpreted in the following subsubsections.
Thereby, the results on foci in research related to HMI in I4.0 are supposed to be substantiated in
order to answer RQ2 comprehensively by analyzing and answering each of its three sub-questions.
6.1.1
RQ2.1: Focal Points in Research Regarding the Human Aspect. RQ2.1 raises the question which
elements of the Human section of the taxonomy are the most prevalent among the scientific articles
included in the final sample and thus represent focal points in related research.
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 31

A Survey on Human Machine Interaction in Industry 4.0
31
Regarding interim-level categories, it can be inferred from Figure 10 that only the tasks and the
role to be assumed by the human operator are discussed in at least half of the sample papers which
is why bottom-level categories of such prevalence only exist in these two subsubsections. Those
categories are the actual activities and the role of employees in mainly strategic as well as operative
activities.
However, it is worth examining the actual shares of articles addressing the individual categories
in more detail. In particular, it seems noteworthy that the demands on staff, with 48.7%, missed the
chosen critical value of 50% only marginally. Thus, despite the classification on the heatmap, they
seem to be regarded as a significant aspect in research when analyzing future HMI processes in
I4.0.
Nevertheless, the dominance of the human tasks and roles is confirmed as 87.8% and 71.4% of
sample papers discuss those categories of the Human section, respectively. Especially instances of
activities to be performed by humans are quoted regularly (86.2% of articles) while the strategic and
operative roles of humans are discussed in approximately half of the articles, with rather strategic
roles being considered slightly more often (53.4% as opposed to 50.2%).
0,00%
5,00%
10,00%
15,00%
20,00%
25,00%
30,00%
35,00%
40,00%
45,00%
planning /
specification /
engineering
monitoring
manual
assembly
machine
operating
intervention in
case of failure
decisionmaker
flexible
problem-solver
controlling
instance
further training
required
Relative 
Frequencies 
Activities 
Compared to 
pre-Industry 4.0 
Strategic 
Activities 
Operative 
Activities 
Role 
Tasks 
Demands on Staff 
Overall Number of Attributes in this Section: 40 
Number of Prevalent Attributes (Relative Frequency ≥ 20%): 9 
Fig. 11. The Most Frequent Attributes of the Human Section
Raising the level of detail in the analysis of prevalent taxonomy elements from the Human section,
the bottom-level attributes addressed in at least one fifth of sample articles have been identified.
The chosen critical value for attributes to be considered as relatively prevalent has been lowered
to 20% to reflect the circumstances of the large number of different attributes and the fact that
different authors might address a similar issue by considering different instances from a collection
of related attributes. Furthermore, out of a total of 113 attributes of the overall taxonomy, exactly
39 surpass the value of 20% which means that around one third of attributes are considered as
prevalent. This approximately coincides with the evaluation of interim- and bottom-level categories
in Section 6.1 where twelve out of 40 categories are addressed in at least 75% of articles.
As can be inferred from Figure 11, there are, on the one hand, comparatively few attributes
from the Human section surpassing the chosen critical value of 20% while, on the other hand, those
attributes which do surpass the 20% are addressed particularly often. This implies a relatively
skewed distribution of prevalence concerning the total of attributes from the Human section. More
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 32

32
Krupitzer et al.
precisely, while slightly more than a third of all attributes of the taxonomy surpass the value of 20%,
less than a quarter of the attributes from the Human section are discussed so frequently. However,
of the nine prevalent attributes from this part of the taxonomy, none is addressed in less than 25%
of the sample papers.
In general, the impression is reinforced that, regarding a consideration of the human entity,
research on HMI in I4.0 is strongly focused on different tasks to be performed by operators.
The activity most often quoted is the intervention in case of failures in the production process,
corresponding to a large number of studies assigning the role of a flexible problem-solver to human
operators. The most prevalent view of the human’s role in I4.0 activities, and at the same time
the most frequent attribute of the Human section, however, is that of a strategic decision-maker.
Thus, researchers expect employees from various levels of hierarchy to be faced with the challenge
and the opportunity to make critical decisions regarding relevant process parameters. Finally, as
indicated above, the significance of the demands on staff should not be underrated, considering that
28.6% of all sample articles expect that transition to I4.0 will require further training of employees.
Besides, more than 19% of studies mention flexibility as a required personality trait for operators,
failing the 20% value only marginally.
6.1.2
RQ2.2: Focal Points in Research Regarding the Machine Aspect. In order to identify the focal
points in research regarding the Machine section, i.e. to answer RQ2.2, first the relative frequencies
of the corresponding interim- and bottom-level categories are examined.
While only marginally less than nine in ten sample articles (89.9%) discuss the role and functionality provided by the machine and 84.7% and 58.7% of papers address the Active and Passive
sub-categories, respectively, the subsubsection of the hardware components represents a very
interesting special case. Although 93.1% of the articles in the final sample elaborate on the aspect of
implemented hardware components, none of their lower-level sub-categories is addressed in at least
75% of the papers. Hence, the vast majority of articles considers hardware components, however
with varying foci. In fact, in total, 80 sample papers (42.3%) address output and hybrid input-output
platforms, respectively, while only 47 papers address both simultaneously. Furthermore, 138 papers
(73.0%) discuss different components ensuring context-awareness of automated systems.
Examining the prevalence of specific attributes of the Machine section confirms the focal points
being output and hybrid input-output platforms, hardware components for context-awareness,
as well as active and passive functionalities provided by the machine entity (see Figure 12). In
particular, the machine’s role as an active support and assistance system for human operators
represents not only the most frequently quoted machine attribute but also the second-most frequent
attribute of the overall taxonomy. Besides, the crucial contribution of sensors in achieving contextaware systems and the fundamental role of automated systems of passively collecting, aggregating,
and visualizing data and information for human users are also reflected in the data. Finally, the
advanced output platform of a not further specified HMD is studied intensively in exactly one
third of sample publications, partially of an explorative and experimental character, while the
use of well-established input-output platforms from the consumer market, i.e. devices like tablet
computers and smartphones, for industrial applications has been examined in 42.3% of all sample
articles.
6.1.3
RQ2.3: Focal Points in Research Regarding the Interaction Aspect. As an answer to the third
sub-question of RQ2, the most prevalent elements of the Interaction section among the sample
articles shall be examined.
Considering the interim- and bottom-level categories of the taxonomy, it can be stated that more
than 90% of sample articles dedicate their analysis of HMI processes in I4.0 to one or more specific
functional units of a manufacturing organization. Still, the sub-aspects of the interaction part most
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 33

A Survey on Human Machine Interaction in Industry 4.0
33
0,00%
10,00%
20,00%
30,00%
40,00%
50,00%
60,00%
70,00%
80,00%
HMD
(no further details)
hand-held
sensors
RFID chips
support and
assistance for
humans
collaboration with
humans
data collection,
aggregation, and
visualization
Relative 
Frequencies 
Output 
Platforms 
Active 
Passive 
Hardware Components 
Hybrid 
Input-Output 
Platforms 
ContextAwareness 
Role / Functionality 
Overall Number of Attributes in this Section: 24 
Number of Prevalent Attributes (Relative Frequency ≥ 20%): 7 
Fig. 12. The Most Frequent Attributes of the Machine Section
intensively studied are the UIs deployed and the goals to be achieved, covered by 93.1% and 95.2% of
articles, respectively. Particularly the interaction goals are addressed in almost 90% of publications
while both the specific goals for the UIs implemented and their application scenarios are discussed
in slightly more than 75% of sample articles. Besides application, also the other sub-categories
of UIs represent aspects attracting substantial attention in related research. To be precise, the
characteristics and types of UIs implemented are specified in 62.4% and 65.1% of sample papers,
respectively, while different kinds of functionality provided by those UIs are discussed in only
marginally less than half (49.7%) of the sample instances.
Considering the fact that, overall, approximately one third of all attributes surpass the chosen
critial value of 20% while only 22.5% of the attributes from the Human section (cf. Figure 11) and
29.2% of the attributes describing the machine entity (cf. Figure 12) surpass that value, the share of
comparatively prevalent instances among the Interaction section will consequently be higher
than a third. This inference is confirmed by Figure 13, stating that 46.9% of attributes from the
Interaction section are discussed in more than 20% of sample papers.
Regarding the much-discussed subsubsection of goals pursued, the instances most often addressed
are usability of the UI and improved working conditions as well as high degrees of product
customization by means of successful HMI. Besides, mostly goals concerning the enhancement of
human capabilities and performances are frequently addressed, altogether suggesting that a large
stream of research on the topic primarily regards HMI as a means of efficiently supporting and
enhancing the human entity. Concerning UI types, it seems striking how many studies are dedicated
towards AR which represents one of the most often-quoted attributes of the overall taxonomy,
reflecting the large number of articles explicitly studying a specific type of AR application for
industrial purposes. Mainly, those are applications for maintenance purposes or generally visualizing
instructions to human operators, explaining their prevalence as separate attributes (36.0% and
42.9%, respectively). Apart from UI types and applications, their characteristic and functionality
of exerting sensitivity and adaptivity towards the situational context seems to be regarded as
significant by various authors. Finally, various modern interaction technologies as a means of H2M
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 34

34
Krupitzer et al.
0,00%
10,00%
20,00%
30,00%
40,00%
50,00%
60,00%
70,00%
80,00%
90,00%
Goals for 
the UI 
Characteristics 
Application 
User Interfaces 
Goals 
Interaction Goals 
Types 
Functionality 
Means of 
Interaction 
H2M 
Location of 
Interaction 
Func. 
Units Physical 
Relative 
Frequencies 
Overall Number of Attributes in this Section: 49 
Number of Prevalent Attributes (Relative Frequency ≥ 20%): 23 
Fig. 13. The Most Frequent Attributes of the Interaction Section
communication are addressed regularly, comprising touch interfaces, natural language interfaces,
and gesture recognition, while the vast majority of publications in the final sample studies HMI
processes occurring within the manufacturing unit of industrial firms.
6.2
Results RQ3: Identifiable Patterns in Related Research
After the description of relative frequencies of individual taxonomy elements as an answer to RQ2
and its sub-questions, the following section presents the results on underlying patterns in the
collected data on the coverage of third-level categories in the final sample. Therefore, research
questions RQ3.1 and RQ3.2 are analyzed in order to derive association and classification rules from
the available set of data, respectively.
6.2.1
RQ3.1: Derivation of Association Rules from the Content-Related Data. Relating to RQ3.1,
data mining techniques are deployed in order to uncover associations among the prevalence of
different third-level categories. Thereby, categories can be identified for which the decision of
authors on whether or not to address this category in a specific scientific work on HMI in I4.0
exerts a strong association with the authors’ respective decision concerning one or more other
elements of the taxonomy. Thus, the identification of such relationships, in case they are positive,
can be interpreted as a hint that authors from the considered research field regard the associated
categories as related contentwise.
For the purpose of determining association rules with a specified minimum confidence and
the highest possible support [89], Weka’s Apriori algorithm has been applied to the set of data
describing the coverage of third-level categories in the sample articles. This means that item sets,
i.e. values of specific attributes of the data set or combinations of values of different attributes, are
searched which, when observed within a sample instance, appear together with a specific value of
another attribute. Minimum confidence has been set to 0.9 which means that for at least 90% of the
sample instances with the specified item set, the value of the associated attribute must equal the
specific value in order for this relation to qualify for an association rule. Of all association rules
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 35

A Survey on Human Machine Interaction in Industry 4.0
35
identified, Apriori has been instructed to output the five rules with the highest support, i.e. with
the largest number of sample articles for which the identified rule actually holds [89].
Unfortunately, applying Apriori to the data set comprising the total of 29 third-level categories
as well as the publication year of the respective article as data attributes yields barely meaningful
results. Four of the best five association rules identified specify a category whose status (addressed
or not addressed) in an article is highly related to the aspect of the human role as a customer not
being addressed in the respective article. These associations mainly lack an intuitive rationale and
largely follow from the fact that, generally, 93.7% of sample articles neglect the category of the
human role as a customer.
In order to identify a more diverse set of association rules with a more meaningful interpretation,
the attribute as Customer has been removed from the data set and the Apriori algorithm has been
run a second time in another iteration of the data preparation and modeling phases of CRISP-DM.
However, the consecutive output based on the reduced data set exerts similar features, mainly
naming elements associated with the category Functional Units being addressed in an article.
Accordingly, Functional Units has been removed as well before running Apriori again, just like
Educational Subject/Content after this third trial.
After removing as Customer, Functional Units, and Educational Subject/ Content, the
following five rules have been determined:
(1) Goals for the UI (Addressed) =⇒Interaction Goals (Addressed)
(2) Required Skill Set (Not Addressed) =⇒Required Personality Traits
(Not Addressed)
(3) Required Skill Set (Not Addressed) =⇒Means of Skill Mediation (Not
Addressed)
(4) Augmentation Technique Visual Field (Not Addressed) =⇒Technology
Information Display (Not Addressed)
(5) Human Activities/Tasks (Addressed) =⇒Interaction Goals (Addressed)
All of those association rules have an intuitive interpretation for the final deployment phase of the
CRISP-DM process model. It seems that authors discussing the goals for applied UIs mostly regard
them in a broader perspective, considering how they contribute to the achievement of general
goals for HMI in I4.0. These interaction goals also seem to be of high relevance when discussing
future human tasks, consistent with the notion that augmented operators will be supported by
technology in performing their tasks (cf. [85]). On the other hand, not considering the required
human skill set obviously makes a discussion of means of mediating skills to employees redundant
while it also seems to imply that the respective authors forego a discussion of required human
characteristics in general, both regarding skill set and personality traits. Finally, a publication
not discussing augmentation techniques for the visual field seems to indicate that the authors
generally concentrate on sub-aspects other than the visualization of data and information to human
operators.
6.2.2
RQ3.2: Derivation of Classification Rules from the Content-Related Data. As a final step
in analyzing the data collected on the sample literature, Weka’s JRip classifier is supposed to
identify potential classification rules regarding different third-level categories of the taxonomy.
Such classifications can help researchers determine whether related research would generally be
likely to consider a specific aspect of the topic given the remaining aspects supposed to be addressed
in the study. Based on this information, unintended disregarding of important sub-aspects in the
paper can be avoided or authors can deliberately concatenate different aspects of the overall topic
not widely studied in combination yet.
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 36

36
Krupitzer et al.
Compared to other variants of classification, JRip regularly delivers a very lean and less complex
model in the form of a manageable set of consecutive rules classifying an instance based on the
values of a specific set of its attributes [89]. Particularly with regard to the number of third-level
categories of the taxonomy (29), models requiring the values of all attributes except for the class
as input to predict an instance’s class value as well as tree classifiers with too many branches are
impractical and impede an intuitive interpretation of the classification model.
Overall, for thirteen out of 30 attributes in the data set, the classification model produced by
the JRip algorithm is discarded because a simplistic and unconditional classification based on the
rule delivered by Zero R implies a higher estimated accuracy. More precisely, the model of rules
produced by JRip is not considered meaningful or as adding valuable information if its accuracy is
estimated to be lower than that of an unconditional classification rule relying solely on the most
prevalent class value in the training set [87].
Furthermore, the identified classification rules for another six class attributes are not considered
for further analysis (i.e. deployment) because their estimated classification accuracy does not exceed
that of the corresponding rule determined by Zero R by more than 3.6 percentage points while for
the remaining eleven classification models, this difference is larger than five percentage points.
Thus, for those eleven class attributes, the chances are higher that JRip provides a significantly
higher mean classification accuracy than Zero R.
As stated in Section 4.4.2, ROC area values of the accepted and considered models are examined as
another means of verifying their meaningfulness. For a random and thus uninformed or worthless
classifier, ROC area would be expected to be close to 0.5 while a perfect classifier would exhibit a
ROC area of 1 given that it would always predict articles actually addressing a specific category
to address the category (true positive rate of 1) and would never predict articles not discussing a
specific category to address this element (false positive rate of 0) [54].
Considering that the unconditional classification models delivered by Zero R predict all instances
to have the same class value, true and false positive rate for a specific class value are equal (either 0
or 1) which is also expected for a random classifier (rates are expected to be equal, not necessarily
0 or 1) [54]. Thus, these uninformed models are expected to exhibit a ROC area value similar to
a random classifier. A classification model based on JRip, on the other hand, if meaningful and
informed, should be closer to the perfect classifier’s true and false positive rates and exhibit a ROC
area greater than 0.5 (cf. [54]).
Indeed, examination of ROC area values for the eleven sets of rules considered for analysis
reveals that those classification models exhibit a respective value of at least 0.61, considerably
larger than the expected baseline case of approximately 0.5 for a random classifier [54]. Thus, those
identified classification models are considered to add value by providing some informed knowledge
about the classification of research articles related to the topic of HMI in I4.0.
The five most intuitive and meaningful sets of classification rules among the eleven considered
models, regarding interpretability of the rules, classify research articles regarding one of the
following third-level categories, respectively: the characteristics of human tasks, the demands
on staff compared to pre-I4.0, hardware output platforms, UI functionality, or means of H2M
communication. Table 7 presents the list of classification rules for these class attributes, also
including the sets of rules for the other six accepted and considered classification models.
Characteristics of Human Tasks. The model for characteristics of human tasks (cf. Table 7)
is interesting as it suggests that authors regard the changes in demands on staff brought by I4.0 for
employees with a more operative role in the operations to be linked to the characteristics of their
actual tasks under I4.0.
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 37

A Survey on Human Machine Interaction in Industry 4.0
37
Class
Accuracy
ROC Area
Rules (JRip)
Zero R
JRip
Zero R
JRip
(A. = Addressed; N.A. = Not Addressed)
Task
69.8%
75.4%
0.48
0.69
Demands Compared to pre-I4.0 (A.) & Operative Role (A.) =⇒Task Character. (A.)
Characteristics
=⇒Task Characteristics (N.A.)
Strategic Role
53.4%
61.5%
0.49
0.62
Technology Information Display (A.) & Operative Role (N.A.) =⇒Strategic Role (N.A.)
Input Platforms (A.) & UI Characteristics (N.A.) =⇒Strategic Role (N.A.)
Operative Role (N.A.) & Context-Awareness (N.A.) & Human Activities/Tasks (A.) & M2H Communication (N.A.) =⇒Strategic
Role (N.A.)
M2H Communication (A.) & Demands Compared to pre-I4.0 (N.A.) & Hybrid Platforms (N.A.) & Active (A.) =⇒Strategic Role
(N.A.)
=⇒Strategic Role (A.)
Operative Role
50.3%
65.4%
0.47
0.66
Task Characteristics (N.A.) & Required Personality Traits (N.A.) =⇒Operative Role (N.A.)
Required Skill Set (N.A.) & UI Types (A.) & Output Platforms (N.A.) =⇒Operative Role (N.A.)
as Customer (A.) & year = 2016 =⇒Operative Role (N.A.)
Augm. Techn. Vis. Field (A.) & Active (A.) & Req. Person. Traits (A.) =⇒Oper. Role (N.A.)
=⇒Operative Role (A.)
Demands
64.0%
81.5%
0.49
0.80
Required Skill Set (A.) =⇒Demands Compared to pre-I4.0 (A.)
Compared
Educational Subject/Content (A.) =⇒Demands Compared to pre-I4.0 (A.)
to pre-I4.0
=⇒Demands Compared to pre-I4.0 (N.A.)
Output
57.7%
76.9%
0.50
0.79
UI Types (A.) & Augmentation Technique Visual Field (A.) =⇒Output Platforms (A.)
Platforms
UI Types (A.) & Operative Role (A.) =⇒Output Platforms (A.)
=⇒Output Platforms (N.A.)
Hybrid
57.7%
69.0%
0.50
0.70
UI Characteristics (A.) & Output Platforms (A.) =⇒Hybrid Platforms (A.)
Platforms
UI Characteristics (A.) & Functional Units (A.) & Input Platforms (N.A.) & Required Personality Traits (N.A.) =⇒Hybrid Platforms
(A.)
=⇒Hybrid Platforms (N.A.)
UI
62.4%
67.8%
0.49
0.69
Hybrid Platforms (N.A.) & Passive Functionality (N.A.) =⇒UI Characteristics (N.A.)
Characteristics
Hybrid Platforms (N.A.) & as Customer (A.) =⇒UI Characteristics (N.A.)
=⇒UI Characteristics (A.)
UI Types
65.1%
84.2%
0.47
0.83
Output Platforms (N.A.) & UI Application (N.A.) =⇒UI Types (N.A.)
Output Platforms (N.A.) & Operative Role (A.) & Physical Location (N.A.) =⇒UI Types (N.A.)
Goals for the UI (N.A.) & Physical Location (A.) =⇒UI Types (N.A.)
=⇒UI Types (A.)
UI
47.6%
62.5%
0.47
0.61
H2M Communication (A.) & M2H Communication (A.) =⇒UI Functionality (A.)
Functionality
Hybrid Platforms (A.) =⇒UI Functionality (A.)
=⇒UI Functionality (N.A.)
H2M
61.4%
69.2%
0.48
0.65
Hybrid Platforms (A.) & Operative Role (A.) =⇒H2M Communication (A.)
Communication
Input Platforms (A.) & Output Platforms (N.A.) =⇒H2M Communication (A.)
UI Types (A.) & UI Functionality (A.) & M2H Comm. (A.) =⇒H2M Comm. (A.)
=⇒H2M Communication (N.A.)
Physical
69.8%
76.1%
0.48
0.63
Input Platforms (A.) & Passive Functionality (N.A.) =⇒Physical Location (A.)
Location
=⇒Physical Location (N.A.)
Table 7. Accepted and Considered Classification Models Produced by JRip
Demands on Staff Compared to pre-I4.0. In relation to those changes in demands on staff,
in turn, when discussing required skills of employees, authors seem to imply a change compared to
pre-I4.0, causing them to compare demands before and after inception of I4.0 (cf. Table 7).
Output Platforms. The classification rules for coverage of output platforms (cf. Table 7) seem
intuitively sensible as different types of UIs can be seen as commonly related to differing output
platforms, e.g. when regarding VR as rather linked to HMDs than to stationary screens while the
opposite applies to traditional GUIs. Therefore, a discussion of output platforms due to the consideration of specific UIs appears plausible. The additional condition of addressing the augmentation
technique for the visual field is suitable in the sense that it hints towards the fact that the study
reflects on the technological aspects of visualizing information in its analysis of UI types, making
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 38

38
Krupitzer et al.
the consideration of output platforms consequent. Varying human operative roles, on the other
hand, might require the consideration of different suitable types of output platforms.
UI Functionality. The model for UI functionality has the lowest ROC area value and degree of
estimated accuracy (62.5%) among the five models discussed (cf. Table 7). Still, a discussion of the
functionalities provided by the implemented UIs seems consequent if possible means of HMI in
both directions are examined or when hybrid platforms are considered which typically provide a
broad range of UI functionalities.
Means of H2M Communication. The first rule of the model for H2M communication (cf. Table
7) is plausible given that hybrid platforms regularly offer multiple means of H2M communication
while depending on the specific operative role, different forms of interaction from the operator to
the automated system might be more appropriate. The second rule is perfectly plausible as well,
considering that a discussion of input platforms while neglecting corresponding output platforms
suggests a focus on H2M communication. Finally, regarding the third rule, a concurrent analysis of
types and functionalities of UIs as well as M2H communication reflects a broad examination of HMI
means and tools, potentially requiring also a consideration of H2M communication for completion.
7
CONCLUSION
Having presented the applied methodology, the findings which resulted from said procedure, as
well as the implications and limitations of these results, the last chapter of this thesis is supposed
to provide a summarizing overview of the most important insights, together with concluding
remarks. Building upon that, consequent and open research issues are identified which represent
opportunities for further research on the topic of HMI in I4.0.
7.1
Summary
The aim of this thesis has been to analyze a comprehensive set of scientific literature relevant to
the topic of HMI in I4.0 and to develop, based upon this foundation, a taxonomy representing the
current state of the art regarding research in the area of the topic. Furthermore, the insights on the
taxonomy and data collected on its coverage in related literature should serve as a basis to identify
focal points and patterns in research on HMI in I4.0.
The taxonomy developed as an answer to RQ1 structures the topic in a four-layer hierarchy
consisting of three levels of categories and a bottom-level collection of attributes representing
instances or specifications of the third-level categories. On the highest rank, the topic is clustered
into three sections representing the human actor, the machine entity, and aspects defining the
process of interaction between both. On the second and third level, those three main categories are
defined in more detail in terms of their constituting aspects.
In order to capture the human aspect in I4.0-related HMI, operators’ tasks as well as the human
role in I4.0 operations are defined. Moreover, the taxonomy determines demands on employees and
the qualifying measures to be offered by firms and government in order to prepare an appropriate
I4.0 workforce as the final sections of the Human part.
In describing the machine entity, the taxonomy considers passive and active roles and functionalities assumed or offered by the automated system as well as the available techniques and
technologies representing the machine’s means of visualizing data and information to human users.
Apart from that, the taxonomy includes an analysis of the available hardware components needed
to provide such functionality and visualization services.
The third main section of the taxonomy defines the interaction processes among human and
machine agents under I4.0 in terms of different types of goals to be achieved in the interaction, the
UIs deployed, the means of interaction and communication, as well as the location of interaction.
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 39

A Survey on Human Machine Interaction in Industry 4.0
39
The analysis of the sample literature’s coverage of individual taxonomy elements in order to
answer RQ2 has revealed that the interim-level categories of UIs and goals in the interaction as
well as the implemented hardware components represent focal points in HMI-related research in
the I4.0 area. Only slightly less prevalent, discussions of the human tasks and the functionality
provided by the machine entity also seem to be regarded as highly significant in studying HMI
in I4.0 by the majority of authors in the final sample. Thus, a main stream in related research
seems to approach the topic by distinguishing tasks to be performed by humans from the role and
functionality provided by automated systems and enabled by various hardware components. Based
on that, the integration of those two types of entities in an interaction process is supposed to serve
specific purposes and goals, facilitated by the implementation of appropriate UIs. In general, the
vast majority of sample articles conducts such analyses and discussions of HMI in I4.0 with respect
to a context of manufacturing activities, revealing a focus of researchers on the industrial core
activity of production.
In the course of answering RQ3, application of data mining techniques on the data reflecting
the sample papers’ coverage of third-level categories reveals a set of association rules represented
in the data. These rules describe pairs or sets of third-level categories exhibiting interrelations in
the fact whether or not they are addressed in individual sample articles. Finally, using Weka’s JRip
algorithm, seventeen sets of classification rules have been identified serving as a potential support
for researchers in deciding whether they should include a discussion of a specific aspect in a study
dedicated towards HMI in I4.0. The most intuitive sets of rules classify research articles with regard
to the characteristics of human tasks, the demands on staff compared to pre-I4.0, output platforms,
UI functionality, and means of H2M communication.
The potential implications of these results extend to future employees and firms in the industrial
sector, facing changes in the working environment in general and challenges regarding measures
and investments to be taken in preparing for the fourth industrial revolution, respectively, as well
as to governments and customers of industrial firms. However, the implications derived from the
study’s results need to be interpreted with care by taking into account the restricted scope of the
study with respect to the number of publications related to the topic which could be included in
the initial sample and the limitations of the applied methodology.
Altogether, the findings in the course of this thesis reflect the complexity of the overall topic
of HMI in I4.0 by organizing it in a four-level taxonomy of categories and attributes. Still, the
taxonomy, and thus the topic, exhibits a clear structure on different levels of detail whose individual
elements and related sections are reflected in related research to varying extents. Examining the
sub-aspects of the taxonomy studied less frequently, judging based on the final sample of relevant
literature, reveals open research issues representing opportunities for future research which the
following final section briefly outlines.
7.2
Opportunities for Future Research
When examining the machine section of the taxonomy more closely, it is noticeable that a substantial
amount of sample articles, exactly one third to be precise, incorporates the application of HMDs of
a not further specified type as the most prevalent attribute of the output platforms category. At the
same time, none of the attributes or even the third-level categories themselves of input platforms,
technology for information display, and augmentation technique for the visual field is addressed in
more than 22.3% of articles. Considered in combination, this suggests that there might be room left
for analyzing the most appropriate input platforms to be employed in conjunction with HMDs as
the corresponding output platform for I4.0-related HMI processes. Likewise, an examination of the
most adequate techniques and technologies for information visualization implemented on an HMD
output platform might yield interesting and useful insights.
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 40

40
Krupitzer et al.
Regarding the much-discussed aspect of UIs, an apparent phenomenon among this thesis’ final
sample is the large number of articles studying a specific industrial AR application, respectively.
Nonetheless, the insights on longer-term effects and applicability of AR for such scenarios are rare.
Therefore, in light of the apparent significance of AR applications in related research, conducting
a long-term experimental study on an industrial AR application might represent an important
opportunity for future research.
Besides, despite the central role of human operators in I4.0 activities and 28.6% of sample articles
stressing the need for further training of employees to enable successful implementation of the
related processes, none of the third-level categories concerned with aspects of staff training and
qualification is addressed in at least 25% sample papers. Therefore, further studies on appropriate
measures of education and qualification of future and current members of the industrial workforce
might be of significant value to public and corporate decision-makers.
Finally, the analyses and findings in the course of this thesis might be further advanced by using
technical methods like machine learning algorithms to cluster the bottom-level attributes based on
observed sample data. This way, categories and a structure for a potential alternative design of a
taxonomy even better reflected in related scientific contributions might be identified. Furthermore,
the implemented analyses of the collected data might be intensified by conducting more iterations
of the CRISP-DM process model, searching for classification models better suited for the available
set of data.
REFERENCES
[1] Cammardella Assunta, Guizzi Guido, Vespoli Silvestro, and Visone Giusy. 2017. Man-CPS interaction: An experimental
assessment of the human behavior evolution. In 2017 IEEE 3rd International Forum on Research and Technologies for
Society and Industry (RTSI). IEEE, 1–6. https://doi.org/10.1109/RTSI.2017.8065973
[2] L. Barreto, A. Amaral, and T. Pereira. 2017. Industry 4.0 implications in logistics: an overview. Procedia Manufacturing
13 (jan 2017), 1245–1252. https://doi.org/10.1016/J.PROMFG.2017.09.045
[3] Andrea Benešová and JiÅŹí Tupa. 2017. Requirements for Education and Qualification of People in Industry 4.0.
Procedia Manufacturing 11 (jan 2017), 2195–2202. https://doi.org/10.1016/J.PROMFG.2017.07.366
[4] Oscar Blanco-Novoa, Tiago M. Fernandez-Carames, Paula Fraga-Lamas, and Miguel A. Vilar-Montesinos. 2018. A
Practical Evaluation of Commercial Industrial Augmented Reality Systems in an Industry 4.0 Shipyard. IEEE Access 6
(2018), 8201–8218. https://doi.org/10.1109/ACCESS.2018.2802699
[5] Malte Brettel, Niklas Friederichsen, Michael Keller, and Marius Rosenberg. 2014. How Virtualization, Decentralization
and Network Building Change the Manufacturing Landscape: An Industry 4.0 Perspective. International Journal of
Information and Communication Engineering 8, 1 (2014), 37–44. https://www.waset.org/publications/9997144
[6] Sebastian Büttner, Henrik Mucha, Markus Funk, Thomas Kosch, Mario Aehnelt, Sebastian Robert, and Carsten Röcker.
2017. The Design Space of Augmented and Virtual Reality Applications for Assistive Environments in Manufacturing:
A Visual Approach. In Proceedings of the 10th International Conference on PErvasive Technologies Related to Assistive
Environments - PETRA ’17. ACM Press, Island of Rhodes, Greece, 433–440. https://doi.org/10.1145/3056540.3076193
[7] Sang Su Choi, Kiwook Jung, and Sang Do Noh. 2015. Virtual reality applications in manufacturing industries: Past
research, present findings, and future directions. Concurrent Engineering: Research and Applications 23, 1 (2015), 40–63.
https://doi.org/10.1177/1063293X14568814
[8] G. Dini and M. Dalle Mura. 2015. Application of Augmented Reality Techniques in Through-life Engineering Services.
Procedia CIRP 38 (jan 2015), 14–23. https://doi.org/10.1016/J.PROCIR.2015.07.044
[9] Rainer Drath and Alexander Horch. 2014. Industrie 4.0: Hit or Hype? [Industry Forum]. IEEE Industrial Electronics
Magazine 8, 2 (2014), 56–58. https://doi.org/10.1109/mie.2014.2312079
[10] Daniel Ehmann and Carsten Wittenberg. 2018. The idea of Virtual Teach-In in the field of industrial robotics. In 2018
IEEE 14th International Conference on Control and Automation (ICCA). IEEE, 680–685. https://doi.org/10.1109/ICCA.
2018.8444250
[11] P. Fantini, G. Tavola, M. Taisch, J. Barbosa, P. Leitao, Y. Liu, M. S. Sayed, and N. Lohse. 2016. Exploring the integration
of the human as a flexibility factor in CPS enabled manufacturing environments: Methodology and results. In IECON
2016 - 42nd Annual Conference of the IEEE Industrial Electronics Society. IEEE, 5711–5716.
https://doi.org/10.1109/
IECON.2016.7793579
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 41

A Survey on Human Machine Interaction in Industry 4.0
41
[12] Holger Flatt, Nils Koch, Carsten Rocker, Andrei Gunter, and Jurgen Jasperneite. 2015. A Context-Aware Assistance
System for Maintenance Applications in Smart Factories based on Augmented Reality and Indoor Localization. In 2015
IEEE 20th Conference on Emerging Technologies & Factory Automation (ETFA). IEEE, 1–4. https://doi.org/10.1109/ETFA.
2015.7301586
[13] Elgar Fleisch. 2010. WHAT IS THE INTERNET OF THINGS? AN ECONOMIC PERSPECTIVE. Economics, Management,
and Financial Markets 5, 2 (2010), 125–157. https://search.proquest.com/docview/748829740/3C000481F22D42F4PQ/7?
accountid=14570
[14] Paula Fraga-Lamas, Tiago M. Fernandez-Carames, Oscar Blanco-Novoa, and Miguel A. Vilar-Montesinos. 2018. A
Review on Industrial Augmented Reality Systems for the Industry 4.0 Shipyard. IEEE Access 6 (2018), 13358–13375.
https://doi.org/10.1109/ACCESS.2018.2808326
[15] Markus Funk, Andreas Bächler, Liane Bächler, Thomas Kosch, Thomas Heidenreich, and Albrecht Schmidt. 2017.
Working with Augmented Reality? A Long-Term Analysis of In-Situ Instructions at the Assembly Workplace. In
Proceedings of the 10th International Conference on PErvasive Technologies Related to Assistive Environments - PETRA ’17.
ACM Press, Island of Rhodes, Greece, 222–229. https://doi.org/10.1145/3056540.3056548
[16] Markus Funk, Thomas Kosch, Romina Kettner, Oliver Korn, and Albrecht Schmidt. 2016. motion EAP: An Overview
of 4 Years of Combining Industrial Assembly with Augmented Reality for Industry 4.0. In Proceedings of the 16th
international conference on knowledge technologies and data-driven business. New York, USA. http://thomaskosch.com/
wp-content/plugins/papercite/pdf/funk2016motioneap.pdf
[17] Dominic Gorecky, Mohamed Khamis, and Katharina Mura. 2015. Introduction and establishment of virtual training
in the factory of the future. International Journal of Computer Integrated Manufacturing 30, 1 (jul 2015), 182–190.
https://doi.org/10.1080/0951192X.2015.1067918
[18] Dominic Gorecky, Mathias Schmitt, Matthias Loskyll, and Detlef Zühlke. 2014. Human-Machine-Interaction in the
Industry 4.0 Era. In Proceedings - 2014 12th IEEE International Conference on Industrial Informatics, INDIN 2014. IEEE,
289–294. https://doi.org/10.1109/INDIN.2014.6945523 ar Xiv:ar Xiv:1011.1669v3
[19] Norbert Gronau, André Ullrich, and Malte Teichmann. 2017. Development of the Industrial Io T Competences in the
Areas of Organization, Process, and Interaction Based on the Learning Factory Concept. Procedia Manufacturing 9 (jan
2017), 254–261. https://doi.org/10.1016/J.PROMFG.2017.04.029
[20] Yuqiuge Hao and Petri Helo. 2017. The role of wearable devices in meeting the needs of cloud manufacturing: A case
study. Robotics and Computer-Integrated Manufacturing 45 (jun 2017), 168–179. https://doi.org/10.1016/J.RCIM.2015.
10.001
[21] Fabian Hecklau, Mila Galeitzke, Sebastian Flachs, and Holger Kohl. 2016. Holistic approach for human resource
management in Industry 4.0. Procedia CIRP 54 (jan 2016), 1–6. https://doi.org/10.1016/J.PROCIR.2016.05.102
[22] Mario Hermann, Tobias Pentek, and Boris Otto. 2016. Design Principles for Industrie 4.0 Scenarios. In 2016 49th Hawaii
International Conference on System Sciences (HICSS). IEEE, 3928–3937. https://doi.org/10.1109/HICSS.2016.488
[23] Hartmut Hirsch-Kreinsen. 2014. Smart production systems. A new type of industrial process innovation. In DRUID
Society Conference 2014. Copenhagen.
[24] Jean-Michel Hoc. 2000. From human - machine interaction to human - machine cooperation. Ergonomics 43, 7 (jul
2000), 833–843. https://doi.org/10.1080/001401300409044
[25] Erik Hofmann and Marco Rüsch. 2017. Industry 4.0 and the current status as well as future prospects on logistics.
Computers in Industry 89 (aug 2017), 23–34. https://doi.org/10.1016/J.COMPIND.2017.04.002
[26] Sabina Jeschke, Christian Brecher, Tobias Meisen, Denis Özdemir, and Tim Eschert. 2017. Industrial Internet of Things
and Cyber Manufacturing Systems. In Industrial Internet of Things, Sabina Jeschke, Houbing Song, Christian Brecher,
and Danda B. Rawat (Eds.). Springer International Publishing, Cham, Switzerland, 3–19.
https://doi.org/10.1007/
978-3-319-42559-7_1
[27] Jana Jost, Thomas Kirks, and Benedikt Mattig. 2017. Multi-agent systems for decentralized control and adaptive
interaction between humans and machines for industrial environments. In 2017 7th IEEE International Conference on
System Engineering and Technology (ICSET). IEEE, 95–100. https://doi.org/10.1109/ICSEng T.2017.8123427
[28] Henning Kagermann. 2015. Change Through Digitization-Value Creation in the Age of Industry 4.0. In Management of
Permanent Change. Springer Fachmedien Wiesbaden, Wiesbaden, 23–45. https://doi.org/10.1007/978-3-658-05014-6_2
[29] Henning Kagermann, Wolfgang Wahlster, and Johannes Helbig. 2013.
Recommendations for implementing the strategic initiative INDUSTRIE 4.0.
Technical Report. acatech - National Academy of Science and
Engineering.
https://en.acatech.de/fileadmin/user{_}upload/Baumstruktur{_}nach{_}Website/Acatech/root/de/
Material{_}fuer{_}Sonderseiten/Industrie{_}4.0/Final{_}report{_}{_}Industrie{_}4.0{_}accessible.pdf
[30] Hyoung Seok Kang, Ju Yeon Lee, Sang Su Choi, Hyun Kim, Jun Hee Park, Ji Yeon Son, Bo Hyun Kim, and Sang Do Noh.
2016. Smart manufacturing: Past research, present findings, and future directions. International Journal of Precision
Engineering and Manufacturing-Green Technology 3, 1 (jan 2016), 111–128. https://doi.org/10.1007/s40684-016-0015-5
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 42

42
Krupitzer et al.
[31] Azfar Khalid, Pierre Kirisci, Zied Ghrairi, Klaus-Dieter Thoben, and Jürgen Pannek. 2016. A methodology to develop
collaborative robotic cyber physical systems for production environments. Logistics Research 9, 1 (dec 2016), 23.
https://doi.org/10.1007/s12159-016-0151-x
[32] Dennis Kolberg and Detlef Zühlke. 2015. Lean Automation enabled by Industry 4.0 Technologies. IFAC-Papers On Line
48, 3 (2015), 1870–1875. http://isidl.com/wp-content/uploads/2017/12/8262-English-ISIDL.pdf
[33] J. Krüger, T.K. Lien, and A. Verl. 2009. Cooperation of human and machines in assembly lines. CIRP Annals 58, 2 (jan
2009), 628–646. https://doi.org/10.1016/J.CIRP.2009.09.009
[34] Edward A. Lee. 2008. Cyber Physical Systems: Design Challenges. In 2008 11th IEEE International Symposium on
Object and Component-Oriented Real-Time Distributed Computing (ISORC). IEEE, Orlando, FL, USA, 363–369. https:
//doi.org/10.1109/ISORC.2008.25
[35] Christian Linn, Simon Bender, Joshua Prosser, Kevin Schmitt, and Dirk Werth. 2017. Virtual remote inspection - A new
concept for virtual reality enhanced real-time maintenance. In 2017 23rd International Conference on Virtual System &
Multimedia (VSMM). IEEE, 1–6. https://doi.org/10.1109/VSMM.2017.8346304
[36] Chao Liu and Xun Xu. 2017. Cyber-physical Machine Tool - The Era of Machine Tool 4.0. Procedia CIRP 63 (jan 2017),
70–75. https://doi.org/10.1016/J.PROCIR.2017.03.078
[37] Frieder Loch, Fabian Quint, and Iuliia Brishtel. 2016. Comparing Video and Augmented Reality Assistance in Manual
Assembly. In 2016 12th International Conference on Intelligent Environments (IE). IEEE, 147–150. https://doi.org/10.
1109/IE.2016.31
[38] Francesco Longo, Letizia Nicoletti, and Antonio Padovano. 2017. Smart operators in industry 4.0: A human-centered
approach to enhance operators’ capabilities and competencies within the new smart factory context. Computers &
Industrial Engineering 113 (nov 2017), 144–159. https://doi.org/10.1016/J.CIE.2017.09.016
[39] Yang Lu. 2017. Industry 4.0: A survey on technologies, applications and open research issues. Journal of Industrial
Information Integration 6 (2017), 1–10. https://doi.org/10.1016/J.JII.2017.04.005
[40] Stephan Lukosch, Mark Billinghurst, Leila Alem, and Kiyoshi Kiyokawa. 2015. Collaboration in Augmented Reality.
Computer Supported Cooperative Work (CSCW) 24, 6 (2015), 515–525. https://doi.org/10.1007/s10606-015-9239-0
[41] Riccardo Masoni, Francesco Ferrise, Monica Bordegoni, Michele Gattullo, Antonio E. Uva, Michele Fiorentino, Ernesto
Carrabba, and Michele Di Donato. 2017. Supporting Remote Maintenance in Industry 4.0 through Augmented Reality.
Procedia Manufacturing 11 (jan 2017), 1296–1302. https://doi.org/10.1016/J.PROMFG.2017.07.257
[42] George Michalos, Panagiotis Karagiannis, Sotiris Makris, Önder Tokçalar, and George Chryssolouris. 2016. Augmented
Reality (AR) Applications for Supporting Human-robot Interactive Cooperation. Procedia CIRP 41 (jan 2016), 370–375.
https://doi.org/10.1016/J.PROCIR.2015.12.005
[43] Aitor Moreno, Gorka Velez, Aitor Ardanza, Iñigo Barandiaran, Álvaro Ruíz de Infante, and Raúl Chopitea. 2017.
Virtualisation process of a sheet metal punching machine within the Industry 4.0 vision. International Journal on
Interactive Design and Manufacturing (IJIDe M) 11, 2 (may 2017), 365–373. https://doi.org/10.1007/s12008-016-0319-2
[44] Jochen Nelles, Sinem Kuz, Alexander Mertens, and Christopher M. Schlick. 2016. Human-centered design of assistance
systems for production planning and control: The role of the human in Industry 4.0. In 2016 IEEE International
Conference on Industrial Technology (ICIT). IEEE, 2099–2104. https://doi.org/10.1109/ICIT.2016.7475093
[45] K. Nolimo Solman. 2002. Analysis of interaction quality in human-machine systems: applications for forklifts. Applied
Ergonomics 33, 2 (mar 2002), 155–166. https://doi.org/10.1016/S0003-6870(01)00052-7
[46] Volker Paelke. 2014. Augmented Reality in the Smart Factory: Supporting Workers in an Industry 4.0. Environment.
In Proceedings of the 2014 IEEE 19th Conference on Emerging Technologies & Factory Automation (ETFA). IEEE, 1–4.
https://doi.org/10.1109/ETFA.2014.7005252
[47] Riccardo Palmarini, John Ahmet Erkoyuncu, and Rajkumar Roy. 2017. An Innovative Process to Select Augmented
Reality (AR) Technology for Maintenance. Procedia CIRP 59 (jan 2017), 23–28. https://doi.org/10.1016/J.PROCIR.2016.
10.001
[48] T. Pereira, L. Barreto, and A. Amaral. 2017. Network and information security challenges within Industry 4.0 paradigm.
Procedia Manufacturing 13 (2017), 1253–1260. https://www.sciencedirect.com/science/article/pii/S2351978917306820
[49] Johannes Pfeffer, Markus Graube, Patrick Reipschlaeger, Stephan Arndt, Leon Urbas, Raimund Dachselt, and Ralph
Stelzer. 2015. Towards collaborative plant control using a distributed information and interaction space. In 2015 IEEE
20th Conference on Emerging Technologies & Factory Automation (ETFA). IEEE, 1–4. https://doi.org/10.1109/ETFA.2015.
7301587
[50] Sabine Pfeiffer. 2016. Robots, Industry 4.0 and Humans, or Why Assembly Work Is More than Routine Work. Societies
6, 2 (may 2016), 16. https://doi.org/10.3390/soc6020016
[51] Hans-Christian Pfohl, Burak Yahsi, and Tamer Kurnaz. 2017. Concept and Diffusion-Factors of Industry 4.0 in the
Supply Chain. In Proceedings of the 5th International Conference LDIC, 2016, Michael Freitag, Herbert Kotzab, and
Jürgen Pannek (Eds.). Springer, Cham, Bremen, Germany, 381–390. https://doi.org/10.1007/978-3-319-45117-6_33
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 43

A Survey on Human Machine Interaction in Industry 4.0
43
[52] Bogdan-Constantin Pirvu, Constantin-Bala Zamfirescu, and Dominic Gorecky. 2016. Engineering insights from an
anthropocentric cyber-physical system: A case study for an assembly station. Mechatronics 34 (mar 2016), 147–159.
https://doi.org/10.1016/J.MECHATRONICS.2015.08.010
[53] Jorge Posada, Carlos Toro, Inigo Barandiaran, David Oyarzun, Didier Stricker, Raffaele de Amicis, Eduardo B. Pinto,
Peter Eisert, Jurgen Dollner, and Ivan Vallarino. 2015. Visual Computing as a Key Enabling Technology for Industrie
4.0 and Industrial Internet. IEEE Computer Graphics and Applications 35, 2 (mar 2015), 26–40. https://doi.org/10.1109/
MCG.2015.45
[54] David Martin Ward Powers. 2011. Evaluation: from precision, recall and F-measure to ROC, informedness, markedness
and correlation. Journal of Machine Learning Technologies 2, 1 (2011), 37–63. https://dspace2.flinders.edu.au/xmlui/
handle/2328/27165
[55] Davy Preuveneers and Elisabeth Ilie-Zudor. 2017. The intelligent industry of the future: A survey on emerging trends,
research challenges and opportunities in Industry 4.0. Journal of Ambient Intelligence and Smart Environments 9, 3 (apr
2017), 287–298. https://doi.org/10.3233/AIS-170432
[56] Christopher Prinz, Friedrich Morlock, Sebastian Freith, Niklas Kreggenfeld, Dieter Kreimeier, and Bernd Kuhlenkötter.
2016. Learning Factory Modules for Smart Factories in Industrie 4.0. Procedia CIRP 54 (jan 2016), 113–118. https:
//doi.org/10.1016/J.PROCIR.2016.05.105
[57] David Romero, Peter Bernus, Ovidiu Noran, Johan Stahre, and Åsa Fast-Berglund. 2016. The Operator 4.0: Human
Cyber-Physical Systems & Adaptive Automation towards Human-Automation Symbiosis Work Systems. In Advances
in Production Management Systems. Initiatives for a Sustainable World, Irenilza Nääs, Oduvaldo Vendrametto, João
Mendes Reis, Rodrigo Franco Gonçalves, Márcia Terra Silva, Gregor von Cieminski, and Dimitris Kiritsis (Eds.). IFIP
Advances in Information and Communication Technology (IFIPAICT), Vol. 488. Springer, Cham, 677–686.
https:
//doi.org/10.1007/978-3-319-51133-7_80
[58] David Romero, Johan Stahre, Thorsten Wuest, Ovidiu Noran, Peter Bernus, Åsa Fast-Berglund, and Dominic Gorecky.
2016. Towards an operator 4.0 typology: a human-centric perspective on the fourth industrial revolution technologies.
In CIE46 Proceedings. 1–11.
[59] Bruno G. Rüttimann and Martin T. Stöckli. 2016. Lean and Industry 4.0-Twins, Partners, or Contenders? A Due
Clarification Regarding the Supposed Clash of Two Production Systems. Journal of Service Science and Management 9
(nov 2016), 485–500. https://doi.org/10.4236/jssm.2016.96051
[60] Marco Saggiomo, Mario Loehrer, Daniel Kerpen, Jacqueline Lemm, and Yves-Simon Gloy. 2016. Human-and TaskCentered Assistance Systems in Production Processes of the Textile Industry: Determination of Operator-Critical
Weaving Machine Components for AR-Prototype Development. In 2016 49th Hawaii International Conference on System
Sciences (HICSS). IEEE, 560–568. https://doi.org/10.1109/HICSS.2016.76
[61] Adam Sanders, Chola Elangeswaran, and Jens Wulfsberg. 2016. Industry 4.0 Implies Lean Manufacturing: Research Activities in Industry 4.0 Function as Enablers for Lean Manufacturing. Journal of Industrial Engineering and Management
9, 3 (sep 2016), 811–833. https://doi.org/10.3926/jiem.1940
[62] Jania Astrid Saucedo-Martínez, Magdiel Pérez-Lara, José Antonio Marmolejo-Saucedo, Tomás Eloy Salais-Fierro, and
Pandian Vasant. 2018. Industry 4.0 framework for management and operations: a review. Journal of Ambient Intelligence
and Humanized Computing 9 (2018), 789–801. https://link.springer.com/content/pdf/10.1007/s12652-017-0533-1.pdf
[63] Günther Schuh, Till Potente, Cathrin Wesch-Potente, Anja Ruth Weber, and Jan-Philipp Prote. 2014. Collaboration
Mechanisms to Increase Productivity in the Context of Industrie 4.0. Procedia CIRP 19 (jan 2014), 51–56.
https:
//doi.org/10.1016/J.PROCIR.2014.05.016
[64] Syed Imran Shafiq, Cesar Sanin, Edward Szczerbicki, and Carlos Toro. 2015. Virtual Engineering Object / Virtual
Engineering Process: A specialized form of Cyber Physical System for Industrie 4.0. Procedia Computer Science 60
(2015), 1146–1155.
[65] H. Shimoda, H. Ishii, W. Wu, D. Li, T. Nakagawa, and H. Yoshikawa. 1999. A Basic Study on Virtual Collaborator as an
Innovative Human-Machine Interface in Distributed Virtual Environment: The Prototype System and Its Implication
for Industrial Application. In IEEE SMC’99 Conference Proceedings. 1999 IEEE International Conference on Systems, Man,
and Cybernetics (Cat. No.99CH37028), Vol. 5. IEEE, 697–702. https://doi.org/10.1109/ICSMC.1999.815636
[66] F. Shrouf, J. Ordieres, and G. Miragliotta. 2014. Smart Factories in Industry 4.0: A Review of the Concept and of
Energy Management Approached in Production Based on the Internet of Things Paradigm. In Proceedings of the
2014 IEEE International Conference on Industrial Engineering and Engineering Management. IEEE, 697–701.
https:
//doi.org/10.1109/IEEM.2014.7058728
[67] Statistisches Bundesamt (Destatis). 2018. Volkswirtschaftliche Gesamtrechnungen. Inlandsproduktberechnung Detaillierte
Jahresergebnisse. Technical Report. Statistisches Bundesamt (Destatis). https://doi.org/10.1007/s10529-009-0123-1
[68] T. Stock and G. Seliger. 2016. Opportunities of Sustainable Manufacturing in Industry 4.0. Procedia CIRP 40 (jan 2016),
536–541. https://doi.org/10.1016/J.PROCIR.2016.01.129
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 44

44
Krupitzer et al.
[69] Tae Kyung Sung. 2018. Industry 4.0: A Korea perspective. Technological Forecasting and Social Change 132 (jul 2018),
40–45. https://doi.org/10.1016/J.TECHFORE.2017.11.005
[70] Anna Syberfeldt, Oscar Danielsson, and Magnus Holm. 2015. Visual Assembling Guidance Using Augmented Reality.
Procedia Manufacturing 1 (jan 2015), 98–109. https://doi.org/10.1016/J.PROMFG.2015.09.068
[71] Sebastian Thiede, Max Juraschek, and Christoph Herrmann. 2016. Implementing Cyber-physical Production Systems
in Learning Factories. Procedia CIRP 54 (jan 2016), 7–12. https://doi.org/10.1016/J.PROCIR.2016.04.098
[72] Klaus-Dieter Thoben, Stefan Wiesner, and Thorsten Wuest. 2017. "Industrie 4.0" and Smart Manufacturing - A Review
of Research Issues and Application Examples. International Journal of Automation Technology 11, 1 (2017).
[73] Damien Trentesaux and Patrick Millot. 2016. A Human-Centred Design to Break the Myth of the "Magic Human"
in Intelligent Manufacturing Systems. In Service Orientation in Holonic and Multi-Agent Manufacturing, Theodor
Borangiu, Damien Trentesaux, André Thomas, and Duncan Mc Farlane (Eds.). Studies in Computational Intelligence
(SCI), Vol. 640. Springer, Cham, 103–113. https://doi.org/10.1007/978-3-319-30337-6_10
[74] Christopher J. Turner, Windo Hutabarat, John Oyekan, and Ashutosh Tiwari. 2016. Discrete Event Simulation and
Virtual Reality Use in Industry: New Opportunities and Future Trends. IEEE Transactions on Human-Machine Systems
46, 6 (2016), 882–894. https://doi.org/10.1109/THMS.2016.2596099
[75] Aswin Karthik Ramachandran Venkatapathy, Haci Bayhan, Felix Zeidler, and Michael ten Hompel. 2017. Human
Machine Synergies in Intra-Logistics: Creating a Hybrid Network for Research and Technologies. In 2017 Federated
Conference on Computer Science and Information Systems (Fed CSIS). 1065–1068. https://doi.org/10.15439/2017F253
[76] Birgit Vogel-Heuser and Dieter Hess. 2016. Guest Editorial Industry 4.0-Prerequisites and Visions. IEEE Transactions
on Automation Science and Engineering 13, 2 (apr 2016), 411–413. https://doi.org/10.1109/TASE.2016.2523639
[77] Tobias Wagner, Christoph Herrmann, and Sebastian Thiede. 2017. Industry 4.0 Impacts on Lean Production Systems.
Procedia CIRP 63 (jan 2017), 125–131. https://doi.org/10.1016/J.PROCIR.2017.02.041
[78] Jiafu Wan, Hu Cai, and Keliang Zhou. 2015. Industrie 4.0: Enabling Technologies. In Proceedings of 2015 International
Conference on Intelligent Computing and Internet of Things. IEEE, Harbin, China, 135–140. https://doi.org/10.1109/
ICAIOT.2015.7111555
[79] Lihui Wang, Martin Törngren, and Mauro Onori. 2015. Current status and advancement of cyber-physical systems in
manufacturing. Journal of Manufacturing Systems 37, 2 (oct 2015), 517–527. https://doi.org/10.1016/J.JMSY.2015.04.008
[80] Lidong Wang and Guanghui Wang. 2016. Big Data in Cyber-Physical Systems, Digital Manufacturing and Industry
4.0. International Journal of Engineering and Manufacturing (IJEM) 6, 4 (2016), 1–8. http://www.mecs-press.net/ijem/
ijem-v6-n4/IJEM-V6-N4-1.pdf
[81] Shiyong Wang, Jiafu Wan, Di Li, and Chunhua Zhang. 2016. Implementing Smart Factory of Industrie 4.0: An Outlook.
International Journal of Distributed Sensor Networks 12, 1 (jan 2016), 1–10. https://doi.org/10.1155/2016/3159805
[82] X. Wang, S. K. Ong, and A. Y. C. Nee. 2016. A comprehensive survey of augmented reality assembly research. Advances
in Manufacturing 4, 1 (mar 2016), 1–22. https://doi.org/10.1007/s40436-015-0131-4
[83] Yi Wang, Hai-Shu Ma, Jing-Hui Yang, and Ke-Sheng Wang. 2017. Industry 4.0: a way from mass customization
to mass personalization production. Advances in Manufacturing 5, 4 (dec 2017), 311–320. https://doi.org/10.1007/
s40436-017-0204-7
[84] Jane Webster and Richard T. Watson. 2002. Analyzing the Past to Prepare for the Future: Writing a Literature Review.
MIS Quarterly 26, 2 (2002), xiii–xxiii.
[85] Stephan Weyer, Mathias Schmitt, Moritz Ohmer, and Dominic Gorecky. 2015. Towards Industry 4.0 - Standardization
as the crucial challenge for highly modular, multi-vendor production systems. IFAC-Papers On Line 48, 3 (jan 2015),
579–584. https://doi.org/10.1016/J.IFACOL.2015.06.143
[86] Ian H. Witten. 2013. Data Mining with Weka. Class 1. Technical Report. University of Waikato. 1–47 pages. https:
//docs.google.com/file/d/0B-f7Zbfs S9-x WVp PWWRFd W1n S1E/edit
[87] Ian H. Witten. 2013. Data Mining with Weka. Class 2. Technical Report. University of Waikato. https://docs.google.
com/file/d/0B-f7Zbfs S9-xd Xp OUmgya Dd DR0U/edit
[88] Ian H. Witten. 2013. Data Mining with Weka. Class 5. Technical Report. University of Waikato. https://docs.google.
com/file/d/0B-f7Zbfs S9-x Ujh La URQb Wsxbjg/edit
[89] Ian H. Witten. 2014. More Data Mining with Weka. Class 3. Technical Report. University of Waikato.
https:
//drive.google.com/file/d/0B-f7Zbfs S9-x Yzlk WXYw QWFMX28/edit
[90] Carsten Wittenberg. 2016. Human-CPS Interaction - requirements and human-machine interaction methods for the
Industry 4.0. IFAC-Papers On Line 49, 19 (jan 2016), 420–425. https://doi.org/10.1016/J.IFACOL.2016.10.602
[91] Constantin B. Zamfirescu, Bogdan-Constantin Pirvu, Matthias Loskyll, and Detlef Zuehlke. 2014. Do Not Cancel My
Race with Cyber-Physical Systems. In Preprints of the 19th IFAC World Congress. Cape Town, South Africa, 4346–4351.
https://doi.org/10.3182/20140824-6-ZA-1003.01600
, Vol. 1, No. 1, Article . Publication date: February 2020.

---


### Page 45

A Survey on Human Machine Interaction in Industry 4.0
45
[92] Przemysław Zawadzki and Krzysztof Żywicki. 2016. Smart product design and production control for effective mass
customization in the Industry 4.0 concept. Management and Production Engineering Review 7, 3 (2016), 105–112.
https://www.degruyter.com/view/j/mper.2016.7.issue-3/mper-2016-0030/mper-2016-0030.xml
[93] Keliang Zhou, Taigang Liu, and Lifeng Zhou. 2015. Industry 4.0: Towards future industrial opportunities and challenges.
In 2015 12th International Conference on Fuzzy Systems and Knowledge Discovery (FSKD). IEEE, 2147–2152.
https:
//doi.org/10.1109/FSKD.2015.7382284
, Vol. 1, No. 1, Article . Publication date: February 2020.

---
