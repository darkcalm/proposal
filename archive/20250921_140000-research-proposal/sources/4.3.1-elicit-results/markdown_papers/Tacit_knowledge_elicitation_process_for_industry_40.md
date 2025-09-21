

---

Page 1

---

Vol.:(0123456789)
Discover Artificial Intelligence             (2022) 2:6  
| https://doi.org/10.1007/s44163-022-00020-w
1 3
Discover Artificial Intelligence
Research
Tacit knowledge elicitation process for industry 4.0
Enzo Fenoglio1,3 · Emre Kazim1,2 · Hugo Latapie3 · Adriano Koshiyama1,2
Received: 6 December 2021 / Accepted: 21 February 2022
© The Author(s) 2022 
 
OPEN
Abstract
Manufacturers migrate their processes to Industry 4.0, which includes new technologies for improving productivity and 
efficiency of operations. One of the issues is capturing, recreating, and documenting the tacit knowledge of the aging 
workers. However, there are no systematic procedures to incorporate this knowledge into Enterprise Resource Planning 
systems and maintain a competitive advantage. This paper describes a solution proposal for a tacit knowledge elicita-
tion process for capturing operational best practices of experienced workers in industrial domains based on a mix of 
algorithmic techniques and a cooperative game. We use domain ontologies for Industry 4.0 and reasoning techniques 
to discover and integrate new facts from textual sources into an Operational Knowledge Graph. We describe a concepts 
formation iterative process in a role game played by human and virtual agents through socialization and externalization 
for knowledge graph refinement. Ethical and societal concerns are discussed as well.
Keywords  Concept maps · Knowledge graph · Ontology · Tacit knowledge · Knowledge management · AI ethics
1  Introduction
Manufacturers migrate their processes to Industry 4.0 innovative practices, which include the adoption of recent tech-
nologies for improving productivity and efficiency of operations through visibility and analytics [1]. One of the major 
critical issues they face is capturing, recreating, and documenting the experience of the aging workers, the so-called 
tribal knowledge before they change their role or leave the company—This paper uses indifferently the terms of tribal 
knowledge, tacit knowledge, and implicit knowledge, although a subtle difference between tacit and implicit knowledge 
and the term tribal knowledge is jargon.
Tribal knowledge is a term widely employed in the industry to denote critical knowledge obtained by some senior staff 
subject matter experts (SME) who have gained deep expertise on types of equipment, a device, or a method. It is associ-
ated with action since it reflects understanding how more than knowing what [2]. The Six Sigma Business Dictionary 
describes tribal knowledge as “any unwritten information that is not commonly known by others within a company. This 
term is used most when referencing information that may need to be known by others to produce a quality product or service”. 
The tribal knowledge represents how people act unconsciously and intuitively. It is always tacit and never expressed [3] 
or not easily expressible since  we can know more than we can tell, as stated by Polanyi [4]. Tribal knowledge is a subset of 
the institutional knowledge, which comprises all documented and undocumented knowledge in an organization [5]. It 
brings decades of hands-on experience acquired without direct instruction, self-study, or help from others. In this sense, 
 *  Enzo Fenoglio, e.fenoglio@ucl.ac.uk; Emre Kazim, emre.kazim@holisticai.com; Hugo Latapie, hlatapie@cisco.com; Adriano Koshiyama, 
adriano.koshiyama@holisticai.com | 1Department of Computer Science, University College London, Glower St, London WC1E 6BT, 
UK. 2Holistic AI, 18 Soho Square, London W1D 3QL, UK. 3Emerging Technologies & Incubation, Cisco Systems Inc, 170 West Tasman Dr., 
San Jose 95134, CA, USA.


---

Page 2

---

Vol:.(1234567890)
Research	
Discover Artificial Intelligence             (2022) 2:6  
| https://doi.org/10.1007/s44163-022-00020-w
1 3
it belongs to the company, but it is stored within the heads of the experienced workforce never transformed into the 
company knowledge base, and quantifiable only indirectly as a loss when senior workers leave and cannot get replaced 
by apprentices with comparable performance skills.
The process of extracting information out of the head of an expert is not new. It was part of the development process 
for expert systems. The method consisted of two phases: (i) knowledge elicitation, where the knowledge was extracted 
by the expert, and (ii) knowledge representation, where the knowledge was stored in a database. The techniques utilized 
in the past were somehow inefficient and based on direct interviews to develop rule-based systems without the support 
of contemporary cognitive psychology [6] or knowledge management principles [5].
Our contribution follows the same bi-partition, but to the best of our knowledge, this is the first work describing a 
framework for capturing tacit operational best practices of experienced workers in industrial domains based on a cogni-
tive reasoning system and a role-playing game. We use domain ontologies for Industry 4.0 and reasoning techniques to 
discover and integrate new facts from textual sources for automatic Knowledge Graph (KG) generation. We describe a 
concepts-formation iterative process as a role game played by SMEs, knowledge engineers, and virtual agents to capture 
tacit knowledge through socialization and externalization for KG refinement. We defend the thesis that it is not possible 
to fully capture tacit knowledge (usually nonverbal and unexpressed) with a purely algorithmic approach. On the con-
trary, explicit and implicit knowledge transfer is made possible in a cooperative game where human experts and virtual 
agents play together according to the elicitation process described in Sect. 4. The synergy between SMEs and knowledge 
engineers from one side and the cognitive system from the other will lead to knowledge creation through constructive 
learning, reflective ability, active interaction, and collaboration of human and virtual participants. The conversion of 
tacit knowledge into organizational knowledge will be promoted by (i) the application of Concept Maps (CM) mining for 
concepts visualization [7], (ii) the application of domain ontology on a KG for knowledge representation and automatic 
knowledge generation [8, 9], and (iii) the application of logical and semantic reasoning to infer new knowledge in a 
continuous learning process for KG alignment and refinement [10] supervised by SMEs. The resulting KG capitalizes the 
full corporate business knowledge (implicit and explicit) into enterprise assets and can be the base for a conversational 
AI application for industrial domains such as maintenance operations, troubleshooting, reparations, on-site training, etc., 
or can be used as a unified base of expertise in an organization or as a unified enterprise semantic search for intelligent 
information retrieval.
Industry 4.0 is interdisciplinary and at the convergence of different capabilities that foster industrial innovations and 
social advances. In this respect, we follow the approach proposed in [11] for a convergence framework where people, 
objects, and organizations are connected to collect data from specific systems and processes and communicate with 
each other. In our work, we create value through the convergence of engineering methodologies (the cognitive system) 
and the convergence of the humanities and sociology (the cooperative game). In this way, our work can contribute to 
the transformation of the existing and complex relationships in the production process for Industry 4.0 with a better 
understanding of the technology-driven social mechanisms underneath.
The rest of the paper is organized as follows: In Sect. 2, we present some of the methods proposed for capturing tacit 
knowledge. In Sect. 3, we provide a functional description of our cognitive framework for capturing tacit knowledge 
into a KG. In Sect. 4, we describe the knowledge elicitation process using our game role approach for KG alignment and 
refinement. In Sect. 5, we discuss the societal and ethical concerns for the system proposed. In Sect. 6, we draw some 
conclusions. Future works are discussed in Sect. 7.
2  Related work
Tacit knowledge is the work-related practical knowledge learned informally on the job by workers. However, the impor-
tance of tacit knowledge is not systematically recognized by most companies, probably because the workforce age 
segmentation has never impacted companies as faced nowadays. According to the US Bureau of Labor Statistics1, by 
2029, around 25% of the workforce in the industry will be aged above 55 years and retire in the following years. As many 
qualified people retire, a wealth of information related to best practices and efficient operations is being inevitably lost. It 
will become increasingly difficult to find experts with 25 or more years in the workforce who know how to fix a critical 
1  www.bls.gov.


---

Page 3

---

Vol.:(0123456789)
Discover Artificial Intelligence             (2022) 2:6  
| https://doi.org/10.1007/s44163-022-00020-w	
Research
1 3
problem—assuming that it is non-trivial to transfer experience across jobs. Eventually, the better an organization can 
elicit tacit knowledge from its employees and share it across the organization, the more innovative it can be [12].
Many companies do not have any systematic approach to collect and incorporate the field experience of experienced 
workers and assess the role of tacit knowledge management on the success of Enterprise Resource Planning (ERP) 
systems implementation [13]. At best, the loss of tacit knowledge is mitigated by informal procedures [6]. The main 
approaches proposed are the following: 
1.	 Internal reports: For most companies, the standard best practice for recording tacit knowledge is via internal reports 
and any other tribal exchanges such as conversations, forum postings, chats, emails, wikis, software repository issues. 
However, if not enforced, this procedure is ineffective and difficult to replicate. A critical aspect of this approach is 
related to workers’ communication skills. SMEs who have previous experience expressing their expertise are far more 
able to share their knowledge than others. On the contrary, workers who lack minimal communication skills with 
similar domain expertise cannot externalize their knowledge correctly to others. A better approach is described in 
[14] without considering tacit knowledge.
2.	 One-on-one mentoring: Most companies prefer to organize a worker development program in the form of one-
on-one mentoring [15], where a new apprentice shadows some veteran engineer, technician, or senior worker in the 
first 6 or 12 months on the job. The tacit knowledge is usually passed on during on-site training. However, due to the 
urgency of the assigned tasks, senior engineers typically do not have the time, energy, and motivation to carry out 
maintenance inspection and fault diagnosis and thoroughly explain how they function while working [6] to supervi-
sors.
3.	 On-site training: Some companies prefer to provide on-site training to young engineers in the belief that they may 
better absorb and grasp domain knowledge from veteran engineers after they have a mental picture of the overall 
system or problem they are working to. However, most of the time, mentoring focuses on resolving an individual 
issue but fails to help trace the root cause of the problem in similar systems. It may often cause the inexperienced 
workers to jump directly to problem-solving using inefficient (sometimes dangerous) shortcuts for trial and error or 
opting for unwarranted large-scale parts or components replacement when charged with similar jobs.
4.	 Rules collector system: This method enables a process to capture an individual’s expertise in a formalized manner 
updating hand-crafted rules and knowledge databases with information retrieved from the interaction with workers. 
It is the old approach from the time of expert systems. Unfortunately, rule-based systems are brittle and difficult to 
maintain. The rules captured can be contradictory and non-sufficient to ensure the consistency of the knowledge 
base. In our approach, we avoid the limitations of the rules collector system by reasoning in domain ontology to 
discover new knowledge.
KG construction is undoubtedly new for the tacit knowledge elicitation process that we describe for generating an opera-
tional knowledge graph in industrial domains. However, it is common practice for explicit knowledge transfer in other 
domains. For example, for the biomedical domain, in [16] the authors construct a PubMed KG to create connections 
among bio-entities, authors, articles, affiliations, and funding; in [17], the authors describe KGen, a KG generator from 
biomedical scientific literature using NLP techniques and ontology linking. For the financial domain, in [18] the authors 
present Enterprise Knowledge Graphs to illustrate a set of AI-driven applications strongly based on KGs for FinTechs; in 
[19] the authors introduce the KnowEdu system for the education domain that supports personalized teaching services 
and adaptive learning solutions using pedagogical data in a textual format for a neural network pipeline to generate a KG.
3  The cognitive framework functional architecture
In this section, we describe the cognitive pipeline for converting tacit knowledge into explicit knowledge. The mix of 
explicit and tacit knowledge allows organizations to make sense of their environment [20]. The continuous social inter-
action of tacit and explicit knowledge through dialogue and debate creates the institutional knowledge maintained 
on the internal technical documentation of the company. The implicit knowledge represents the industrial culture, the 
occupational traditions, and the cultural values of the workforce that uses, develops, administers, and operates the 
technology in the working environment [21]. In this sense, it is very reductive to think that the overall knowledge in a 
company belongs exclusively to one particular group of experts or a single individual as competence, skills, or know-how. 
It is far better to consider this knowledge as the result of social accomplishments of constructing and reconstructing 


---

Page 4

---

Vol:.(1234567890)
Research	
Discover Artificial Intelligence             (2022) 2:6  
| https://doi.org/10.1007/s44163-022-00020-w
1 3
new knowledge as the ongoing product of practices that engage employees, promote collaboration, and expand the 
knowledge transformation towards a stronger company culture where background knowledge and implicit cognitive 
rules have a fundamental relevance. Tacit knowledge is a social and not an individual attribute [22], and the different 
forms of tacit knowledge [23] go beyond the reductive form of tacit knowledge as know-how. If we want to efficiently 
translate tacit knowledge into explicit knowledge, we shall also emulate the social working environment in which the 
workforce is acting. Insofar we assume the applicability of the Nonaka-Takeuki model [24] that postulates how knowledge 
in an organization is created through continuous social interaction of tacit and explicit knowledge, coupled with the four 
sequential modes of knowledge conversion of the SECI model: Socialization (from tacit to tacit), Externalisation (from 
tacit to explicit), Combination (from explicit to explicit), and Internalization (from explicit to tacit). It is outside the scope 
of this paper to discuss the limitations and the criticism raised by the SECI knowledge creation process. More detailed 
information on these aspects can be found in [25–28].
For the objectives of this paper, the SECI spiral model of knowledge creation perfectly justifies the role game we 
propose to convert tacit knowledge into explicit knowledge with human and virtual agents interacting in the process 
of knowledge transformation. It is worthwhile noting how the inability to formalize directly tacit knowledge does not 
exclude the possibility that a virtual agent (a computer system) might perform the same tasks using alternative repre-
sentations or that tacit knowledge cannot be transferred to a machine [29, 30]. Nevertheless, no automatic cognitive 
system can capture the tacit knowledge or any other genuine human activity with a purely algorithmic approach—from 
workers’ heads to corporate databases—without considering the social, cultural, legal, sociological contexts of the data 
collection and representation. The supervision of a human agent in the cooperative game described in Sect. 4  will ensure 
that non-algorithmic qualitative factors that require human appreciation may be considered during the knowledge 
transformation process, complementing the neuro-symbolic pipeline used to capture the quantitative algorithmic fac-
tors into an operational KG.
3.1  The neurosymbolic architecture
The architecture of the cognitive framework for tacit knowledge elicitation can be described as a hybrid neurosymbolic 
system where a neural network focused on sub-symbolic tasks interacts with a symbolic system— it can be classified as 
Neuro;Symbolic (Type 3) [31].
The functional architecture of the cognitive framework is presented in Fig. 1. It includes three main layers: (i) sub-
symbolic layer, (ii) conceptual layer, (iii) symbolic layer. The main difference with other neurosymbolic architectures is 
Fig. 1   Cognitive framework Functional Architecture for tacit knowledge elicitation


---

Page 5

---

Vol.:(0123456789)
Discover Artificial Intelligence             (2022) 2:6  
| https://doi.org/10.1007/s44163-022-00020-w	
Research
1 3
that the symbolic and the sub-symbolic layers are not coupled directly but interact through an intermediate layer (the 
conceptual layer).
3.1.1  Sub‑symbolic layer
The sub-symbolic layer processes heterogeneous input data collected from the internal technical documentation, opera-
tion and maintenance (O&M) manuals, troubleshooting manuals, technical documentation, and reports from different 
structured or unstructured sources. Other input data types, such as video and audio, have not been scoped in this study 
but can be recorded for archival purposes and documentation.
NLP Data Processing One of the advantages of using input in textual format is the great availability of mature Natural 
Language Processing (NLP) methods. The raw input textual data is stored in files and processed using standard data 
mining tools for automatic knowledge extraction from text.
It is outside the scope of this paper to provide detailed information for KG construction from text using NLP tools and 
techniques. The reader can look at the specialized literature [9, 17, 32–34]. Nevertheless, we provide some basic NLP 
concepts practical for KG generation to extract information for KG construction, such as named entity recognition (NER), 
relation extraction (RE), and entity resolution (ER). A KG is a direct acyclic graph (DAG) defined as KG = (V, E) containing 
a set of nodes or vertices V and a set of edges E ⊆V × V . Named entity recognition or entity extraction is about identify-
ing entities of interest from textual sources to represent the nodes, while relation extraction is about extracting relations 
between two entities of interests identified in the text, i.e., how concepts and entities relate to each other to represent 
edges. Entity resolution identifies whether multiple mentions in a text refer to the same entity. Some preprocessing steps 
(tokenization, stemming, lemmatization, etc.) are performed using standard NLP tools such as Stanford NLP software [35], 
Apache OpenNLP [36], NTLK [37] to prepare the data sources for information extraction, . The modern way to perform 
NER is to take advantage of a pre-trained language model based on transformers (BERT [38]) because it can be adapted 
for the purposes of the specific domain even when few pre-training examples are available [39]. The classical approach to 
extract relations relies on Lexico-Syntactic Patterns and Hearst Patterns [40] as syntactic features, but many other methods 
are available [41]. Eventually, we can represent all the information extracted with a triple subject →predicate →object to 
represent the relationships existing between subjects and objects where relations are the predicates, whereas entities 
are the subjects and the objects. This format can be stored as an RDF statement in a triplestore database.
3.1.2  Conceptual layer
The conceptual layer bridges the gap between symbolic and sub-symbolic representation with an intermediate layer 
that shares knowledge structures using a geometrical representation of knowledge [42]. The principal motivation for 
introducing this layer (Fig. 1) is the different abstraction levels between sub-symbolic and symbolic layers and the need 
to have an enterprise ontology for alignment and refinement of the heterogeneous KGs (triplestore databases) generated 
from texts in the sub-symbolic layer. The conceptual layer is an adaptation layer that facilitates the transformation of the 
information extracted from text (RDF triples) into symbolic objects (operational concepts) for composing new concepts 
and discovering similarities (concepts formation). We exploit this characteristic to fuse similar operational concepts and 
construct the operational KG. Actually, the raw KG composed of entities and relations in the RDF form generated in the 
sub-symbolic layer, is by its nature incomplete and based only on explicit knowledge found in the textual sources used 
during the generation process. Its associated ontological schema has to be alignment with an enterprise ontology and/
or foundational domain ontologies for industrial domains [43] that are more general in supporting domain-specific 
applications. The entity alignment is part of the concept formation phase and can be achieved via joint KG embedding 
methods such as OntoEA [44] for higher quality and usability.
Concepts formation Concept formation is the construction of the ontology (the data graph schema) in a bottom-up 
approach that extracts knowledge instances from input textual data (ontology learning) and uses other knowledge 
resources coming from the CMs [45]. The operational KG is then created by ingesting data to the fused ontologies [46–48]. 
The interplay between CMs and the raw KGs leads to concepts formation by merging the knowledge representation for 
CMs and the knowledge representation for KGs (the ontologies). For the sake of completeness, we provide some back-
ground information for CM, KG, and ontology:


---

Page 6

---

Vol:.(1234567890)
Research	
Discover Artificial Intelligence             (2022) 2:6  
| https://doi.org/10.1007/s44163-022-00020-w
1 3
•	 Concept maps or conceptual diagram is well-recognized approach [7] that uses both content knowledge and pro-
cess knowledge to prompt users to create visual maps of a diagnostic strategy for identifying technical problems in 
complex environments [6]. A CM is a special type of propositional semantic network that is flexible, improves learning 
achievements, prompts constructive learning and active interactions [49, 50]. It is designed in the form of a directed 
graph where nodes represent concepts and edges represent relationships [51]. Despite being an old tool (1984), a CM 
visualizes the level of understanding and the level of thinking to assess the learning progress among human experts, 
displaying the structural nature and extent of knowledge, including misunderstandings of knowledge [49]. This aspect 
is quite important in our process because it facilitates human interactions and group synergies (Sect. 4). The CM [7, 
52] is an alternative step for the automatic generation of concepts from texts to operational knowledge graph where 
we follow the CM mining frameworks described in [51, 53]. As an example, in Fig. 2 we present a fictitious example 
of a CM to illustrate the simple case of troubleshooting a not-lighting lamp.
•	 Knowledge graphs are more recent and adapted for automatic processing and machine reasoning than CMs. A KG 
acquires and integrates information into an ontology and applies a reasoner to derive new knowledge [8]. KGs can 
Fig. 2   Concept Map for the 
not-lighting lamp trouble-
shooting (ContextMinds)
Fig. 3   Knowledge graph schema for the not-lighting lamp troubleshooting (TypeDB from Vaticle Labs)


---

Page 7

---

Vol.:(0123456789)
Discover Artificial Intelligence             (2022) 2:6  
| https://doi.org/10.1007/s44163-022-00020-w	
Research
1 3
efficiently express N-ary relationships between heterogeneous data in multiple domains using a hypergraph structure 
and clear denotation of entities, relations, and attributes. For example, in Fig. 3, we present the KG schema for the use 
case of troubleshooting the not-lighting lamp. The main difference with the equivalent CM in Fig. 2 is the new entity 
named SME and the nested relationships for the abstract roles played (safety and operational) introduced to capture 
the need for expert supervision.
	
  A complete introduction to KG applications for different domains is in [9] with applications ranging from open 
KGs published on the Web, such as DBpedia, YAGO, Freebase, Wikidata, to proprietary enterprise KGs for a variety of 
different goals such as empowering business analytics, facilitating research and discovery, semantic search features 
and recommendations, detecting emerging events for FinTech, etc.
•	 Ontology promotes knowledge sharing [54] and offer a common communication mode for the knowledge elicitation 
process. The ontology describes and captures the domain knowledge [55], establishing the definitions of the techni-
cal concepts used by SMEs and providing the meaning of the relationships between technical terms and operational 
concepts. As such, ontologies aim to make domain knowledge explicit, remove contradictions and ambiguities, sepa-
rate domain knowledge from operational knowledge, enable machines to reason and learn, and facilitate knowledge 
sharing between machines and humans [56]. Foundational domain ontologies have been developed for industrial 
domains such as aviation, aerospace, construction, steel production, chemical engineering, product development, 
and many others. A detailed presentation of the current state of ontologies for Industry 4.0 and reviews for existing 
ontological frameworks and ontological standardization efforts can be found in [43]. However, the typical condition 
is that a full ontology for a particular industrial domain does not exist or is available only partially. In this case, the 
enterprise domain ontology can be developed from the CMs [45], with the foundational ontologies used as baselines 
for the collaborative process described in Sect. 4.
	
  Many methods for ontology learning from text or automatic ontology-population with NLP techniques have been 
investigated in the literature. For example, in [57], the author provides a knowledge repository of ontology learn-
ing tools; in [58], is presented how to populate an ontology with deep learning-based NLP methods from biological 
documents, and in [59] NLP techniques for ontology population using a combination of rule-based approaches and 
machine learning are discussed as well. However, only for specific and well-defined domains a fully automatic ontol-
ogy construction using textual data is feasible [60]. Tacit knowledge is non-verbal and unexpressed; this makes the 
process of fully automating ontology learning an open research challenge, requiring human cognitive processing 
mandatory. We satisfy this requirement with a cognitive reasoning system and the role-playing game.
3.1.3  Symbolic layer
Once concepts have been formed in the conceptual layer, the SMEs and the knowledge engineers improve the knowledge 
models generated, adding new concepts and relationships in a collaborative knowledge construction process that takes 
into account the tacit knowledge. The symbolic layer is where the concepts initially formed in the conceptual layer (and 
sometimes ill-formed) are validated to create a consistent operational KG. Here we mainly refer to ontology alignment 
[61, 62] expressed for making integration into a data graph schema possible. The implicit knowledge is also converted 
into explicit knowledge and encoded in an ontological structure during the collaborative knowledge process (Sect. 4). 
We follow an iterative process of learning cycles for learning how to build an enhanced KG by improving the capabilities 
to integrate new fragments of knowledge extracted from the conceptual layer.
Logical reasoner Partial information is naturally stored in a graph where the relationships between operational con-
cepts are integrated with an enterprise domain ontology, while the logical reasoner infers implicit knowledge. This paper, 
follows the KG life cycle described in [63] with three distinct reasoning phases. In particular, in the learning phase (see 
Fig. 5), we reason for knowledge integration and knowledge discovery (Sect. 4: Phase III), and we use the logical reasoner 
to derive new knowledge, add missing knowledge to identify conflicting information generated in the conceptual layer 
. We note how some aspects of tacit knowledge can be encoded in the KG model as logical rules. For example, in the 
non-lighting lamp problem (see Figs. 2 and 3), there is no direct relationship between incandescent lamp and filament 
condition (broken or intact), but it can be added to the data schema with a rule stating that when the filament for an 
incandescent lamp is broken, then the lamp does not light-up. Finally, reasoning for application service is related to 
the operational phase (Sect. 4: Phase IV), when knowledge is retrieved for knowledge base question answering (KBQA) 


---

Page 8

---

Vol:.(1234567890)
Research	
Discover Artificial Intelligence             (2022) 2:6  
| https://doi.org/10.1007/s44163-022-00020-w
1 3
services or for search services to provide on-site training to new hires. A detailed discussion of reasoning in KGs can be 
found in [63, 64].
3.1.4  Development software
We have used an exploratory programming approach to support the solution proposal described in this paper. We 
use the ContextMinds2 tool to merge CM and KG. We use Text2Onto [65] for OWL ontology learning from text because 
knowledge is modeled at a meta-level and can be easily translated into different target languages. This tool also features 
algorithms for generating terms, synonyms, concepts, taxonomic and non-taxonomic relations. For the graph database, 
we use TypeDB3 that provides a strongly typed knowledge representation system based on hypergraphs and enables 
modeling any type of complex network with an ontological schema. TypeDB ontologies do not work with RDF triples 
but with a concept level entity-relationship model, representing data with entities, relations, roles, and attributes. An 
embedded reasoning engine can interpret the resulting knowledge representation system with TypeQL query language. 
For KG reasoning, we have also explored RNNLogic [66] for its capability to train a reasoning predictor with logic rules. 
For NLP analysis, we also use Stanza [67], a Python NLP library for syntactic analysis.
4  Knowledge elicitation process
The knowledge elicitation process consists of a set of methods to elicit the tacit knowledge of a domain expert [68] with a 
mix of algorithmic techniques and a cooperative game. In particular, we focus on problem-solving knowledge [69], which 
is about capturing the domain knowledge of workers in a specific industrial structure during the accomplishment of tasks, 
such as maintenance operations, troubleshooting, and reparations. In management contexts, many different techniques 
have been proposed [12]. Our proposal goes beyond these techniques and describes a two-stages elicitation process 
based on (I) a cognitive framework that automatically transforms heterogeneous textual inputs and domain ontologies 
into a raw KG using explicit knowledge, and (II) a role game paradigm, in which human (H) and virtual (V) participants with 
different skill levels, from experts (E) to apprentices (A), play together to refine the KG using human cognitive process-
ing for implicit knowledge integration (see Fig. 4). The primary motivation for our proposal is the incompleteness and 
inconsistency of KGs generated using only explicit data due to the heterogeneity and uncertainty of the textual sources 
and the evolution and acquisition costs of data and knowledge [70]. In order to infer and add missing knowledge to the 
KG or identify erroneous information, the KG refinement stage is needed. Several methods have been proposed [10] for 
the expansion and the enrichment of KGs, but we will be more interested in enriching the ontology of the KG since we 
use reasoning techniques as the main semantic operation during the KG refinement.
Moreover, in the case of tacit knowledge, a richer ontology is conditioned by human experts’ supervision and human 
cognitive processing operated in the role-playing game (see also Sect. 3.1.2). Our configuration echoes the renowned 
Turing’s imitation game but is significantly different. We implement a role-playing game where the objective is not to 
Fig. 4   Knowledge Elicitation 
Process functional diagram
2  www.contextminds.com.
3  vaticle.com.


---

Page 9

---

Vol.:(0123456789)
Discover Artificial Intelligence             (2022) 2:6  
| https://doi.org/10.1007/s44163-022-00020-w	
Research
1 3
assess if the virtual assistant has acquired some human characteristics, but rather to assess the correctness and reliability 
of the knowledge transferred between human and virtual agents and facilitate as much as possible the translation of 
SMEs tacit knowledge into valuable explicit knowledge through socialization and externalization (Sect. 3). The knowledge 
creation framework allows the transfer of insightful knowledge from SMEs to virtual agents in an iterative learning process 
under the supervision of human experts. This point is particularly critical because only human agents can diagnose why 
and how the virtual assistant may or may not be successful at specific tasks.
For completeness, this type of translation based on the SECI model is not new and has been described by other 
researchers [71]. The role game as a simulation of the professional activity with the participation of several experts 
has been described in [12] but without the involvement of the virtual agents. The participation of human experts in 
the knowledge elicitation process will also safeguard against possible collateral effects. In some instances, the tacit 
knowledge employed by SMEs is incorrect or dangerous and shall not be exposed to the virtual assistant during the 
learning phase. Incorrectly used equipment, incorrectly interpreted results, or procedural shortcuts can impose risks 
on the product and service quality and negatively impact employees’ and consumers’ safety. This aspect goes beyond 
the logical reasoning capability of the virtual assistant and a purely algorithmic approach. Therefore, the knowledge 
engineers—the game’s referee, will double-check the practices used by the SMEs and determine which knowledgeable 
facts can be kept and stored in the KG and which others must be questioned and avoided because they are dangerous, 
unsafe, or illegal. In this way, we ensure that the human apprentices can eventually interact with the cognitive system 
in the operational phase without the risk of learning uncontrolled facts that may compromise their learning experience 
and future productivity in the organization.
4.1  Knowledge elicitation work‑breakdown
The overall process for capturing tacit knowledge can be broken down into four phases (see Fig. 5). The objective of the 
first three phases is to capture tacit knowledge into a KG in a role-playing game similar to a video conference. The last 
phase is not scoped in this paper but is briefly described.
•	 Phase I—Dry Run: In this phase, two human experts (HE) generate reference CMs that are compared against 
the expert’s CM generated on similar use cases. We will assess whether the experts can sustain a rich technical 
Fig. 5   Phases for the Knowl-
edge Elicitation Process: HE 
is the Human Expert, HA the 
Human Apprentice, KE the 
Knowledge Engineer, VE the 
Virtual Expert, and VA Virtual 
Apprentice. KEq and VAq are 
the Knowledge Engineer and 
the Virtual Apprentice asking 
questions, while HEa and VEa 
are the Human Expert and the 
Virtual Expert giving answers, 
respectively. Phases I, II, and 
III capture tacit knowledge 
into a KG, while Phase IV is the 
operational setup-up when 
the human apprentice inter-
acts with the virtual expert 
(the cognitive assistant)


---

Page 10

---

Vol:.(1234567890)
Research	
Discover Artificial Intelligence             (2022) 2:6  
| https://doi.org/10.1007/s44163-022-00020-w
1 3
exchange in a simulated working environment that may look unfamiliar. The rationale is to select the most knowl-
edgeable experts on their subject of expertise and ensure optimal collaboration with the other team members 
(the apprentice and the knowledge engineer).
•	 Phase II—Init: We start by replacing the less performing HE with a knowledge engineer (KE) to coordinate the 
elicitation process. The KE will also impersonate the apprentice. Selecting the HE and the KE that fit better is criti-
cal for the rest of the process. There may be experts who know how to do but cannot explain the process they do. 
To mitigate this possibility, we introduce the role of the game master played by the KE, who facilitates the com-
munication exchange with SMEs. The KE should be technically knowledgeable and possess a positive command 
attitude and directional authority to create a friendly environment and make knowledge transfer possible. The 
natural choice is to select the knowledge engineer from the pool of the best-performing SMEs, but other options 
that strongly depend on the corporate culture and personnel availability are possible. The HE and the KE will also 
create gold standards for quality assessment made of CMs extracted by human annotators from a set of tests [53].
•	 Phase III—Learning: In the learning phase, the virtual expert learns concepts and relationships from the role game 
technical session played by SMEs and knowledge engineers. We use CMs mining techniques [53] and ontology 
learning methods to generate an operational KG. The human expert (HE) is challenged by the KE impersonating 
the apprentice. The initial KGs are enhanced via an iterative Q&A session when the participants exchange techni-
cal information until the HE and the KE agree that a successful knowledge transfer has been completed. Typical 
examples are machine service, industrial troubleshooting, production processes control, etc. The decision process 
between the HE and the KE can be easily automated in case of conflicts introducing a majority vote mechanism.
	
  The human/machine interaction is done on two channels: channel 1 between the virtual apprentice (VA) and 
the HE, and channel 2 between the virtual expert (VE) and the KE (Fig.  6). The rationale is to isolate direct interac-
tions of the human agents, which are gradually replaced by their virtual counterparts impersonated by avatars 
depending on the level of quality reached in the sessions. The quality of the concepts produced in this phase will 
be scored by measuring the semantic similarity between concepts generated by the apprentice and the expert 
[72]. In particular, channel 1 isolates the interactions of the human expert giving answers ( HEa ) and the knowl-
edge engineer asking questions ( KEq ) through the virtual apprentice (avatar) asking questions ( VAq ), and channel 
2 isolates the interactions of the KEq and the HEa through the virtual expert (avatar) giving answers ( VEa ). This 
arrangement in which humans are represented as avatars in a virtual environment and where each human sees 
the other as an avatar on their screen has been described in [73] in the context of an autonomous system for 
achieving artificial general intelligence. However, our arrangement aims to activate the experts’ minds and reveal 
their tacit and implicit creative thinking procedures in a role-playing game [12] for KG refinement. Accordingly, 
the cognitive system learns to virtualize human agents for knowledge transfer. We also note that in the process 
described, some of the implicit cultural values of the organization—the tacit knowledge, are implicitly captured 
and encoded in the knowledge base schema.
Fig. 6   Phase III—Learning. On channel 1, HEa is the Human Expert giving answers, VAq the virtual apprentice asking questions imperson-
ated by its avatar on the screen masking the Knowledge Engineer asking questions KEq . On channel 2, VEa is the Virtual expert giving 
answers impersonated by its avatar on the screen masking the human expert HEa accordingly. The rectangle with dashed border captures 
the configuration used in Phase IV (operations) where we eventually replace KEq with the apprentice HA 


---

Page 11

---

Vol.:(0123456789)
Discover Artificial Intelligence             (2022) 2:6  
| https://doi.org/10.1007/s44163-022-00020-w	
Research
1 3
•	 Phase IV—Operations: In the operational phase, the VE replaces the HE, and the HA replaces the KE. In this phase, the 
final KG is integrated into a cognitive system to allow new hires to formulate a technical problem as a collaborative 
task to the virtual expert, elicit mental models, and analyze the results [6] for knowledge retrieval and knowledge 
visualization [74]. Research done on regular classrooms has shown that learning with KGs resulted in better perfor-
mance by students [49]. We expect the same improvements for workers in the industry interacting with this cognitive 
system for on-site training services.
5  Ethical and societal implications
Ethical and societal concerns are inevitable for the cognitive system we have described. Organizations should be vigi-
lant about the knowledge management procedures for transferring tacit knowledge to be fair and equitable for human 
participants in the process. Once successfully trained, the cognitive system will operate in an industrial environment to 
allow new hires for on-site training. All the aspects of knowledge management shall be considered: from knowledge 
creation to knowledge transfer, from knowledge sharing to knowledge governance [75]. Should the system operate with 
a conversational AI user interface, impact assessment for the creation and use of the interface [76] shall be conducted 
by an independent organization before deploying the system. More specifically, from a societal and ethical standpoint, 
we can demarcate three points of interest that broadly track, data, model, and impact: 
1.	 Data relates to concerns around what data is used and how the data is collected. Regarding what data is used, we 
note above that we propose using technical documentation and internal reports rather than video and audio assess-
ment. Notwithstanding this, our approach lends itself to others using this kind of data. This is problematic because 
the collection of emotive data (such as verbal and facial expressions) requires surveillance of staff over long periods. 
The ethical concern here is one of consent and the appropriateness of the potential use of emotive data.
2.	 Model relates to the conceptual and symbolic layer we have discussed above. Here ground assumptions are made, 
which may be deemed contentious given that behavior analysis is occurring. Concerns with bias can be raised 
regarding the exclusion of various types of unconscious behavior such as routed in variations in customs, language 
use—here, the danger of excluding certain sources of tacit knowledge is what is of concern.
3.	 Impact relates to how tacit knowledge is used and the readiness with which the techniques of assessing non-
algorithmic factors such as unconscious, unexplained knowledge can be abused. In essence, the rendering explicit 
of that which is implicit can be used to monitor subliminally and possibly thereby manipulate staff, a concern the EU 
AI Regulation draft (2021) raises as a critical concern [77]. In sum, these ethical and societal considerations can be 
addressed through accountability, transparency, and good governance mechanisms, such as those proposed in [78].
Allying with this board demarcation is the vibrant policy and regulatory debates and proposals relating to the ethical 
and societal implications and management of such systems. For example, at the state and federal levels of the United 
States, there are both existing and proposed regulations [79]; in the UK, worker and talent management is a case stud-
ied extensively as a critical area of legislative concern (moving beyond surveillance to include mental autonomy and 
well-being) [80]. Finally, the most advanced regulatory intervention is the proposed EU AI Act [77], which categorizes 
any algorithmic system used in the context of human resources as high-risk and thereby requiring the highest level of 
governance and assurance. The significance of these developments can be thought of as going beyond engineering 
validation and efficacy to one of societal impact.
We conclude with a real case about ethical and privacy implications concerning intellectual properties (IP) for tribal 
knowledge. We have discussed in Sect. 2 that one traditional method for capturing tribal knowledge is based on internal 
reports. The USPTO has granted recently (2019) a patent to IBM [81] about maintaining tribal knowledge for accelerated 
compliance control deployment building a tribal knowledge graph or knowledge base comprising a semantic level and 
an operational level, focusing on knowledge that does not exist or is not kept up-to-date in a traditionally structured, 
well-defined, coherent set of documents. We observe that the general idea to capture tribal knowledge into a KG is 
similar to ours, standing the different definition for tribal knowledge (Sect. 1). Moreover, it is a contrived trick to define 
tribal knowledge as knowledge that does not exist because even if unstructured, it is already explicit and can be easily 
captured by a process, machine, or computer system as it is claimed.


---

Page 12

---

Vol:.(1234567890)
Research	
Discover Artificial Intelligence             (2022) 2:6  
| https://doi.org/10.1007/s44163-022-00020-w
1 3
Nevertheless, this particular definition of tribal knowledge ensures the patent’s claims eligibility since they are not 
directed towards managing personal behavior, relationships, or interactions between people. It removes all the com-
plexity of the process described in Sect. 4. On the contrary, the ideas described in this paper are not patentable in the 
US because methods which can be performed mentally, or which are the equivalent of human mental work, are unpatentable 
abstract ideas [82]. Similar restrictions apply in other countries. In the UK, it is not patentable a scheme, rule or method 
for performing a mental act, playing a game or doing business, or a program for a computer; [83]. The rationale is to avoid 
patenting a system that will result in certain harmful adverse effects on technology related to concepts performed in 
the human mind, which can create unintended ethical and privacy challenges despite solving critical social issues [84]. 
Once again, these ethical considerations can be addressed through accountability, transparency, and good governance 
mechanisms but pose serious problems to those organizations that want to apply tacit knowledge management prin-
ciples for their business.
6  Conclusions
We have described a solution proposal for capturing operational best practices of experienced workers (a.k.a. the tacit or 
tribal knowledge) in industrial domains for knowledge transfer. We use domain ontologies for Industry 4.0 and reason-
ing techniques to discover and integrate new facts into an operational KG. We describe a concepts formation iterative 
process to integrate explicit and tacit knowledge in a role game played by subject matter experts and knowledge engi-
neers interacting indirectly with a virtual agent represented by an avatar. At the end of the learning phase, the expert is 
replaced by the virtual agent, and the knowledge engineer is impersonated by new hires or workers that need on-site 
training. Societal and ethical concerns have also been discussed.
7  Future directions
We plan to consolidate the investigations performed and develop the complete cognitive architecture to validate the 
method proposed in this paper. We also plan to extend the sensory input modalities to video stream sources for using 
T-Patterns analysis [85], adopting the approach described in [73] that may be used to improve the completeness of 
the operational KGs for troubleshooting tasks during the learning session with a better identification of temporal and 
sequential patterns—typical of manufacturing industrial processes.
Acknowledgements  The authors would like to thank the editor and two anonymous referees who kindly reviewed the earlier version of this 
manuscript and provided valuable suggestions and comments.
Authors’ contributions  EF conceived the initial cognitive framework and Sect. 4. HL contributed to Sect. 3. EK and AK are the authors of Sect. 5. 
The first draft of the manuscript and the following amendments were written by EF. All authors read and approved the final manuscript.
Funding  No external funding was provided for the specific research described in this article.  
 Availability of data and materials  Data sharing not applicable to this article as no datasets were generated or analysed during the current study.
Code availability  Not applicable.
Declarations 
Ethics approval and consent to participate  Not Applicable
Consent for publication  Not Applicable
Competing interests  The authors declare that there are no conflicts of interest or competing interests associated with this article or with the 
research it describes.
Open Access  This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adapta-
tion, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, 
provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article 
are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in 


---

Page 13

---

Vol.:(0123456789)
Discover Artificial Intelligence             (2022) 2:6  
| https://doi.org/10.1007/s44163-022-00020-w	
Research
1 3
the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will 
need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://​creat​iveco​mmons.​org/​licen​ses/​by/4.​0/.
References
	 1.	 Santos C, Mehrsai A, Barros AC, Araújo M, Ares E. Towards industry 4.0: an overview of European strategic roadmaps. Procedia Manuf. 
2017;13:972–9 (Manufacturing engineering society international conference 2017).
	 2.	 Brockmann EN, Anthony WP. Tacit knowledge and strategic decision making. Group Organ Manag. 2002;27(4):436–55.
	 3.	 Hadjimichael D, Tsoukas H. Toward a better understanding of tacit knowledge in organizations: Taking stock and moving forward. Acad 
Manag Ann. 2019;13(2):672–703.
	 4.	 Polanyi M, Sen A. The tacit dimension. Chicago, IL: University of Chicago Press; 2009.
	 5.	 Nonaka I. A dynamic theory of organizational knowledge creation. Organ Sci. 1994;5(1):14–37.
	 6.	 Yuetong Lin, Shahhosseini AM, Badar MA, Foster T, Dean J. A concept map-based cognitive framework for acquiring expert knowledge 
in industrial environment. In: 2016 IEEE frontiers in education conference (FIE). 2016. p. 1–5.
	 7.	 Novak JD, Gowin DB, Kahle JB. Learning about learning. Cambridge: Cambridge University Press; 1984. p. 1–14.
	 8.	 Ehrlinger L, Wöß W. Towards a definition of knowledge graphs. In: Martin, M., Cuquet, M., Folmer, E. (eds.) SEMANTiCS 2016, Leipzig, 
Germany, September 12-15, 2016. CEUR Workshop Proceedings, vol. 1695, 2016.
	 9.	 Hogan A, Blomqvist E, Cochez M, D’amato C, Melo GD, Gutierrez C, Kirrane S, Gayo JEL, Navigli R, Neumaier S, Ngomo A-CN, Polleres A, 
Rashid SM, Rula A, Schmelzeisen L, Sequeda J, Staab S, Zimmermann A. Knowledge graphs. ACM Comput Surv. 2021. https://​doi.​org/​10.​
1145/​34477​72.
	10.	 Paulheim H. Knowledge graph refinement: a survey of approaches and evaluation methods. Semantic Web. 2017;8:489–508.
	11.	 Lee C, Lim C. From technological development to social advance: a review of industry 4.0 through machine learning. Technol Forecast 
Soc Change. 2021;167:120653. https://​doi.​org/​10.​1016/j.​techf​ore.​2021.​120653.
	12.	 Gavrilova T, Andreeva T. Knowledge elicitation techniques in a knowledge management context. J Knowl Manag. 2012;16(4):523–37.
	13.	 Dorobǎţ I. The role of tacit knowledge management in ERP systems implementation. IO: Productivity; 2008.
	14.	 Barthelmey A, Störkle D, Kuhlenkötter B, Deuse J. Cyber physical systems for life cycle continuous technical documentation of manufac-
turing facilities. Procedia CIRP. 2014;17:207–11.
	15.	 Sanyal C, Rigby C. E-mentoring as a HRD intervention: an exploratory action research study within an international professional mentor-
ing scheme. Hum Resour Dev Int. 2017;20(1):18–36.
	16.	 Xu J, Kim S, Song M, et al. Building a pubmed knowledge graph. Sci Data. 2020;7:205. https://​doi.​org/​10.​1038/​s41597-​020-​0543-2.
	17.	 Rossanez A, dos Reis JC, Torres RdS, de Ribaupierre H. KGen: a knowledge graph generator from biomedical scientific literature. BMC Med 
Inform Decis Mak. 2020;20:314. https://​doi.​org/​10.​1186/​s12911-​020-​01341-5.
	18.	 Bellomarini L, Fakhoury D, Gottlob G, Sallinger E (2019) Knowledge graphs and enterprise ai: The promise of an enabling technology. In: 
2019 IEEE 35th international conference on data engineering (ICDE). p. 26–37. https://​doi.​org/​10.​1109/​ICDE.​2019.​00011
	19.	 Chen P, Lu Y, Zheng VW, Chen X, Yang B. KnowEdu: a system to construct knowledge graph for education. IEEE Access. 2018;6:31553–63. 
https://​doi.​org/​10.​1109/​ACCESS.​2018.​28396​07.
	20.	 Baumard P. Tacit knowledge in professional firms: the teachings of firms in very puzzling situations. J Knowl Manag. 2002;6(2):135–51.
	21.	 Gherardi S, Nicolini D. To transfer is to transform: The circulation of safety knowledge. Organization. 2000;7(2):329–48.
	22.	 Pozzali A. Tacit knowledge, implicit learning and scientific reasoning. Mind Soc. 2007;7(2):227–37.
	23.	 Viale R (2013) Tacit Knowledges, pp. 305–323. Springer, Berlin, Heidelberg. https://​doi.​org/​10.​1007/​978-3-​642-​40216-6_​12
	24.	 Nonaka I, Takeuchi H. The knowledge-creating company: how Japanese companies create the dynamics of innovation. New York: Oxford 
University Press; 1995. p. 284.
	25.	 Nonaka I, von Krogh G. Tacit knowledge and knowledge conversion: controversy and advancement in organizational knowledge creation 
theory. Organ Sci. 2009;20(3):635–52.
	26.	 Zárraga C, García-Falcón JM. Factors favoring knowledge management in work teams. J Knowl Manag. 2003;7(2):81–96.
	27.	 Sakiroglu M, Riedel J, Pawar KS (2005) The knowledge creation process and model within NPD teams. In: 2005 IEEE international technol-
ogy management conference (ICE). p. 1–10
	28.	 Gourlay S. Conceptualizing knowledge creation: a critique of Nonaka’s theory. J Manag Stud. 2006;43(7):1415–36.
	29.	 Fenstermacher KD. The tyranny of tacit knowledge: What artificial intelligence tells us about knowledge representation. In: Proceedings 
of the 38th annual Hawaii international conference on system sciences. 2005. p. 243. https://​doi.​org/​10.​1109/​HICSS.​2005.​620.
	30.	 Susskind D. Re-thinking the capabilities of machines in economics. Department of Economics Discussion Paper Series: University of 
Oxford; 2017.
	31.	 d’Avila Garcez AS, Besold TR, Raedt LD, Földiák P, Hitzler P, Icard T, Kühnberger K, Lamb LC, Miikkulainen R, Silver DL. Neural-symbolic 
learning and reasoning: contributions and challenges. In: 2015 AAAI spring symposia, Stanford University, Palo Alto, California,USA, March 
22-25, 2015.
	32.	 Dessì D, Osborne F, Reforgiato Recupero D, Buscaldi D, Motta E. Generating knowledge graphs by employing natural language processing 
and machine learning techniques within the scholarly domain. Futur Gener Comput Syst. 2021;116:253–64. https://​doi.​org/​10.​1016/j.​
future.​2020.​10.​026.
	33.	 Martínez-Rodríguez J-L, López-Arévalo I, Ríos-Alvarado AB. OpenIE-based approach for knowledge graph construction from text. Expert 
Syst Appl. 2018;113:339–55.
	34.	 Kertkeidkachorn N, Ichise R. T2KG: an end-to-end system for creating knowledge graph from unstructured text. In: AAAI workshops. 2017.
	35.	 Manning CD, Surdeanu M, Bauer J, Finkel JR, Bethard S, McClosky D. The Stanford CoreNLP natural language processing toolkit. In: ACL 
(system demonstrations). The Association for Computer Linguistics, US; 2014. p. 55–60. https://​nlp.​stanf​ord.​edu/​softw​are/.


---

Page 14

---

Vol:.(1234567890)
Research	
Discover Artificial Intelligence             (2022) 2:6  
| https://doi.org/10.1007/s44163-022-00020-w
1 3
	36.	 Apache Software Foundation: openNLP Natural Language Processing Library. 2014. http://​openn​lp.​apache.​org/.
	37.	 Bird S, Klein E, Loper E. Natural language processing with Python: analyzing text with the natural language toolkit. Newton: O’Reilly Media 
Inc; 2009.
	38.	 Devlin J, Chang M-W, Lee K, Toutanova K. BERT: pre-training of deep bidirectional transformers for language understanding. 2019. arXiv:​
abs/​1810.​04805.
	39.	 Liu Z, Jiang F, Hu Y, Shi C, Fung P. NER-BERT: a pre-trained model for low-resource entity tagging. 2021. arXiv:​2112.​00405 [cs.CL].
	40.	 Hearst MA. Automatic acquisition of hyponyms from large text corpora. In: COLING 1992 volume 2: the 14th international conference on 
computational linguistics. 1992. https://​aclan​tholo​gy.​org/​C92-​2082
	41.	 Singh S. Natural language processing for information extraction. CoRR, 2018. arXiv:​1807.​02383 [cs.CL].
	42.	 Gardenfors P. Conceptual spaces as a framework for knowledge representation. Mind Matter. 2004;2(2):9–27.
	43.	 Sampath Kumar VR, Khamis A, Fiorini S, Carbonera JL, Olivares Alarcos A, Habib M, Goncalves P, Li H, Olszewska JI. Ontologies for industry 
4.0. Knowl Eng Rev. 2019;34:17.
	44.	 Xiang Y, Zhang Z, Chen J, Chen X, Lin Z, Zheng Y. OntoEA: ontology-guided entity alignment via joint knowledge graph embedding. In: 
Findings of the association for computational linguistics: ACL-IJCNLP 2021. Association for Computational Linguistics, Online; 2021. p. 
1117–1128. https://​doi.​org/​10.​18653/​v1/​2021.​findi​ngs-​acl.​96.
	45.	 Soares A, Sousa C. Using concept maps for ontology development: a case in the work organization domain. In: Azevedo A, editor. Innov 
Manuf Netw. Boston, MA: Springer; 2008. p. 177–86.
	46.	 Buchgeher G, Gabauer D, Gil JM, Ehrlinger L. Knowledge graphs in manufacturing and production: a systematic literature review. IEEE 
Access. 2021;9:55537–54. https://​doi.​org/​10.​1109/​ACCESS.​2021.​30703​95.
	47.	 Zhao Z, Han S-K, So I-M. Architecture of knowledge graph construction techniques. Int J Pure Appl Math. 2018;118(19):1869–83.
	48.	 Zhao M, Wang H-Q, Guo J, Liu D, Xie C, Liu Q, Cheng Z. Construction of an industrial knowledge graph for unstructured chinese text 
learning. Appl Sci. 2019;9(13):2720.
	49.	 Cui J, Yu S. Fostering deeper learning in a flipped classroom: effects of knowledge graphs versus concept maps. Br J Educ Technol. 
2019;50(5):2308–28.
	50.	 Daley BJ. Concept maps: practice applications in adult education and human resource development. New Horiz Adult Educ Hum Resour 
Dev. 2010;24(2–4):31–7.
	51.	 Zubrinic K, Kalpic D, Milicevic M. The automatic creation of concept maps from documents written using morphologically rich languages. 
Expert Syst Appl. 2012;39(16):12709–18.
	52.	 Novak JD, Cañas AJ. The origins of the concept mapping tool and the continuing evolution of the tool. Inf Vis. 2006;5(3):175–84.
	53.	 Villalon JJ, Calvo RA. Concept map mining: A definition and a framework for its evaluation. In: 2008 IEEE/WIC/ACM international confer-
ence on web intelligence and intelligent agent technology, vol. 3. 2008. p. 357–360
	54.	 Hoppe T, Eisenmann H, Viehl A, Bringmann O. Shifting from data handling to knowledge engineering in aerospace industry. In: 2017 IEEE 
international systems engineering symposium (ISSE). 2017. p. 1–6. https://​doi.​org/​10.​1109/​SysEng.​2017.​80883​12.
	55.	 Lian-dong Z, Qifeng W. Knowledge discovery and modeling approach for manufacturing enterprises. In: 2009 third international sym-
posium on intelligent information technology application, vol 1. 2009. p. 291–4.
	56.	 Persson C, Wallin EO. Engineering and business implications of ontologies - a proposal for a minimum viable ontology. In: 2017 13th IEEE 
conference on automation science and engineering (CASE). 2017. p. 864–869. https://​doi.​org/​10.​1109/​COASE.​2017.​82562​12.
	57.	 Konys A. Knowledge repository of ontology learning tools from text. Procedia Comput Sci. 2019;159:1614–28. https://​doi.​org/​10.​1016/j.​
procs.​2019.​09.​332 (Knowledge-based and intelligent information & engineering systems: proceedings of the 23rd international confer-
ence KES2019).
	58.	 Ayadi A, Samet A, de Bertrand de Beuvron F, Zanni-Merk C. Ontology population with deep learning-based nlp: a case study on the bio-
molecular network ontology. Procedia Computer Science 159, 572–581, 2019. https://​doi.​org/​10.​1016/j.​procs.​2019.​09.​212. Knowledge-
based and intelligent information & engineering systems: proceedings of the 23rd international conference KES2019.
	59.	 Maynard D, Li Y, Peters W. Nlp techniques for term extraction and ontology population. IOS Press, NLD; 2008. p. 107–127
	60.	 Wong W, Liu W, Bennamoun M. Ontology learning from text: a look back and into the future. ACM Comput Surv. 2012;44:20–12036.
	61.	 Husáková M, Bureš V. Formal ontologies in information systems development: a systematic review. Information. 2020. https://​doi.​org/​
10.​3390/​info1​10200​66.
	62.	 Ngo D, Bellahsene Z. Efficient semantic verification of ontology alignment. In: 2015 IEEE/WIC/ACM international conference on web 
intelligence and intelligent agent technology (WI-IAT), vol 1. 2015. p. 141–148. https://​doi.​org/​10.​1109/​WI-​IAT.​2015.​92.
	63.	 Bellomarini L, Sallinger E, Vahdati S. Chapter 6 reasoning in knowledge graphs: an embeddings spotlight. Cham: Springer; 2020. p. 87–101.
	64.	 Chen W, Xiong W, Yan X, Wang WY. Variational knowledge graph reasoning. In: Proceedings of the 2018 conference of the North American 
chapter of the association for computational linguistics: human language technologies, vol 1. 2018. p. 1823–1832.
	65.	 Cimiano P, Völker J. Text2onto. In: Montoyo A, Muńoz R, Métais E, editors. Natural language processing and information systems. Berlin, 
Heidelberg: Springer; 2005. p. 227–38.
	66.	 Qu M, Chen J, Xhonneux L-., Bengio Y, Tang J. Rnnlogic: learning logic rules for reasoning on knowledge graphs. In: International confer-
ence on learning representations. 2021.
	67.	 Qi P, Zhang Y, Zhang Y, Bolton J, Manning CD. Stanza: a Python natural language processing toolkit for many human languages. In: Pro-
ceedings of the 58th annual meeting of the association for computational linguistics: system demonstrations. 2020.
	68.	 Shadbolt N, Smart PR. In: Wilson JR, Sharples S, editors. Knowledge elicitation: methods, tools and techniques. CRC Press; 2015. p. 163–200
	69.	 Sureephong P, Ouzrout Y, Buzon L, Bouras A. Knowledge management system enabling collaboration in industry cluster. Int J Manuf Res. 
2010;5(4):478–97.
	70.	 Saïs F. Knowledge graph refinement: link detection, link invalidation, key discovery and data enrichment. 2019. https://​tel.​archi​ves-​ouver​
tes.​fr/​tel-​02441​156.
	71.	 Kimmerle J, Cress U, Held C. The interplay between individual and collective knowledge: technologies for organisational learning and 
knowledge building. Knowl Manag Res Pract. 2010;8(1):33–44.
	72.	 Zhu G, Iglesias C. Computing semantic similarity of concepts in knowledge graphs. IEEE Trans Knowl Data Eng. 2017;29:72–85.


---

Page 15

---

Vol.:(0123456789)
Discover Artificial Intelligence             (2022) 2:6  
| https://doi.org/10.1007/s44163-022-00020-w	
Research
1 3
	73.	 Nivel E, Thórisson KR, Steunebrink BR, Dindo H, Pezzulo G, Rodríguez M, Hernández C, Ognibene D, Schmidhuber J, Sanz R, Helgason HP, 
Chella A, Jonsson GK. Bounded recursive self-improvement. CoRR. 2013. arXiv:​1312.​6764.
	74.	 Sun K, Liu Y, Guo Z, Wang C. Visualization for knowledge graph based on education data. Int J Softw Inform. 2016;10(3).
	75.	 Rhem AJ. AI ethics and its impact on knowledge management. AI Ethics. 2021;1(4):33–7.
	76.	 Ruane E, Birhane A, Ventresque A. Conversational AI: social and ethical considerations. AICS; 2019.
	77.	 European Commission: Proposal for a regulation on a European approach for artificial intelligence. 2021. https://​digit​al-​strat​egy.​ec.​europa.​
eu/​en/​libra​ry/​propo​sal-​regul​ation-​europ​ean-​appro​ach-​artif​icial-​intel​ligen​ce.
	78.	 Koshiyama AS, Kazim E, Treleaven PC, Rai P, Szpruch L, Pavey G, Ahamat G, Leutner F, Goebel R, Knight A, Adams J, Hitrova C, Barnett J, 
Nachev P, Barber D, Chamorro-Premuzic T, Klemmer K, Gregorovic M, Khan SA, Lomas E. Towards algorithm auditing: a survey on manag-
ing legal, ethical and technological risks of AI. Software Engineering eJournal: ML and associated algorithms; 2021.
	79.	 US Congress gov: H.R.6580 - 117th Congress (2021-2022): algorithmic accountability act of 2022, 2022. https://​www.​congr​ess.​gov/​bill/​
117th-​congr​ess/​house-​bill/​6580.
	80.	 UK Government. The roadmap to an effective AI assurance ecosystem—extended version. 2021. https://​www.​gov.​uk/​gover​nment/​publi​
catio​ns/​the-​roadm​ap-​to-​an-​effec​tive-​ai-​assur​ance-​ecosy​stem/​the-​roadm​ap-​to-​an-​effec​tive-​ai-​assur​ance-​ecosy​stem-​exten​ded-​versi​on.
	81.	 IBM. Maintaining tribal knowledge for accelerated compliance control deployment (U.S. Patent No. 10,511,554. USPTO, Dec 2019). https://​
paten​ts.​justia.​com/​patent/​10511​554.
	82.	 UPSPTO. Manual of patent examining procedure (MPEP) (Ninth Edition, Revision 10.2019, Last Revised June 2020, Chapter 2100, Sec-
tion 2106). https://​www.​uspto.​gov/​web/​offic​es/​pac/​mpep/​s2106.​htm.
	83.	 GOV.UK Intellectual Property Office. Manual of patent practice 2022. https://​www.​gov.​uk/​guida​nce/​manual-​of-​patent-​pract​ice-​mopp/​
secti​on-1-​paten​tabil​ity.
	84.	 World Economic Forum. Artificial intelligence collides with patent law. 2018. https://​www3.​wefor​um.​org/​docs/​WEF_​48540_​WP_​End_​
of_​Innov​ation_​Prote​cting_​Patent_​Law.​pdf.
	85.	 Magnusson MS. T-Pattern detection and analysis (TPA) with THEMETM : a mixed methods approach. Front Psychol. 2020;10:2663. https://​
doi.​org/​10.​3389/​fpsyg.​2019.​02663.
Publisher’s Note  Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
