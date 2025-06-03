# Wang2021 Understanding the implications of artificial intelligence on field service operations  a case study of BT

## Paper Metadata

- **Filename:** Wang2021_Understanding_the_implications_of_artificial_intelligence_on_field_service_operations__a_case_study_of_BT_DOI_10-1080_09537287-2021-1882694.pdf
- **DOI:** 10.1080/09537287.2021.1882694
- **Authors:** Not available
- **Year:** Not available
- **Journal/Venue:** Not available
- **URL:** Not available
- **Extraction Date:** 2025-06-03T15:04:11.460768
- **Total Pages:** 41

## Abstract

Abstract not available from BibTeX metadata.

## Keywords

Keywords not available from BibTeX metadata.

---

## Full Text Content



### Page 1

ORCA – Online Research @
Cardiff
This is an Open Access document downloaded from ORCA, Cardiff University's institutional
repository:https://orca.cardiff.ac.uk/id/eprint/130971/
This is the author’s version of a work that was submitted to / accepted for publication.
Citation for final published version:
Wang, Yingli , Skeete, Jean-Paul and Owusu, Gilbert 2022. Understanding the implications of artificial
intelligence on field service operations: a case study of BT. Production Planning and Control 33 (16) , pp.
1591-1607. 10.1080/09537287.2021.1882694 
Publishers page: https://doi.org/10.1080/09537287.2021.1882694 
Please note: 
Changes made as a result of publishing processes such as copy-editing, formatting and page numbers may
not be reflected in this version. For the definitive version of this publication, please refer to the published
source. You are advised to consult the publisher’s version if you wish to cite this paper.
This version is being made available in accordance with publisher policies. See 
http://orca.cf.ac.uk/policies.html for usage policies. Copyright and moral rights for publications made
available in ORCA are retained by the copyright holders.

---


### Page 2

Understanding the implications of Artificial Intelligence on Field Service Operations: A 
Case Study of BT 
 Authors: Yingli Wang*1, Jean-Paul Skeete1, Gilbert Owusu2 
 *Corresponding author 
 1Dr. Yingli Wang 
 Cardiff Business School, Cardiff University 
Aberconway Building, Colum Drive, 
Cardiff, UK 
CF10 3EU 
 
1Dr. Jean-Paul Skeete 
Cardiff Business School, Cardiff University 
Aberconway Building, Colum Drive, 
Cardiff, UK 
CF10 3EU 
 
2Dr. Gilbert Owusu 
Head of Service and Operational Transformation Research, 
BT plc., Adastral Park, Ipswich, UK

---


### Page 3

Understanding the implications of artificial intelligence on field service 
operations: a case study of BT 
Abstract 
Driven by insufficient empirical research and understanding about AI deployment in 
operations management, we set out to explore the implications of AI on field service 
operations. Via an in-depth case study of four AI initiatives across a time span of 20 
years at BT telecommunications, we explored the answers to the following two research 
questions (RQs): RQ1: How has the deployment of artificial agents affected the 
operational efficiency of the organization? And RQ2: What are the critical success 
factors (CSFs) of AI deployment? Our study found that having a standard TRL protocol, 
a people-centric approach, as well as establishing a portfolio of AI initiatives are 
instrumental to BT’s success. We also identified a range of other CSFs that were essential 
to the successful deployment of AI in BT’s field service operations. This paper therefore 
contributes to the timely and emerging sociotechnical debates around the real-world 
implications of AI deployment within organizations. 
Keywords: Artificial intelligence; Case study; Critical success factors; Service operations; Machine 
learning 
1. Introduction 
The age of data science is upon us (Fosso and Akter 2019). After six decades of development 
and fuelled by increasing computing power and storage, Artificial Intelligence (AI) is now 
mature enough to be deployed by operations management professionals, where organizations 
that collect the right kinds of data and invest in their analytic and predictive capacity will be 
best positioned to competitively navigate the next decade. A recent Mc Kinsey global survey 
of over 2000 senior executives suggests that the majority of companies that have adopted AI 
reported an uptick in revenue in business areas such as sales and marketing, and 44 percent of 
companies surveyed say AI has reduced their costs (often in manufacturing) (Cam, Chui, and 
Hall 2019). 
Although classic AI techniques have been well established and applied in the research 
discipline of operations research and operations management (Bullers, Nof, and Whinston 
1980; Shaw and Whinston 1989), AI has received relatively low interest in general. Much of 
the recent progress in AI rely on data-driven techniques such as deep learning and artificial

---


### Page 4

neural networks. Given sufficiently large labelled training datasets and computation power, 
these approaches are achieving unprecedented results, as evidenced by recent successes such 
as IBM’s Watson beating Jeopardy! champions Brad Rutter and Ken Jennings in 2011 and 
Google’s Deep Mind Alpha Go defeating Chinese Go champion Ke Jie in 2017. So-called 
‘narrow AI’ (which consists of highly scoped machine-learning solutions that target a specific 
task and the algorithms chosen are optimised for that specific task), has also seen rapid 
developments in computer vision and speech recognition, robotics, autonomous vehicles and 
virtual agents. 
As a result, AI has drawn renewed academic attention lately. We witness a number of review 
efforts trying to consolidate the applications of AI in industrial marketing (Martínez-López and 
Casillas 2013), supply chain management (Min 2010) risk management (Baryannis et al. 2019), 
logistics (Klumpp 2018) and manufacturing (Wuest et al. 2016). Yet those reviews point out 
that our academic understanding of the implications of AI on operations management (OM) is 
still rather limited. This view is firmly endorsed by Duan et al. (2019, 64): “It appears that 
there are very limited academic research papers focusing on understanding the use and impact 
of the new generation of AI from the technology application perspective with rigorous 
academic investigation and theorisation”. This gap is also highlighted by studies in 
management that there exists a mismatch between extant literature and the organizational 
implementation of newer technologies like AI (Benner and Tushman 2015; Phan, Wright, and 
Lee 2017). Subsequently, there have been calls for a return to phenomena-driven, problemoriented research that might help generate new and more precise concepts associated with 
exploration and exploitation of new innovation (Benner and Tushman 2015). 
As most claims of AI impact in the public domain, typically in white papers published by large 
tech and consulting companies and AI developers, are not substantiated by measurable 
empirical evidence and rigorous academic research, it is thus difficult to know how, why and 
to what extent AI systems are being used, and how they impact on individual and organisational 
decision making and transform organisations. Equally, there has been a lack of research on 
identifying the critical success factors affecting the current use of AI and its impact on 
operations (Duan, Edwards, and Dwivedi 2019). In practice, executives see the potential of 
using AI to achieve competitive advantages but are often uncertain about how to deploy AI, 
usually resulting in the adoption of an ad hoc approach(Fountaine, Mc Carthy, and Saleh 2019).

---


### Page 5

Therefore, our main aim in this paper is to explore the implications of AI on operations 
management. Subsequently our research questions (RQs) are; 
▪ RQ1. How has the deployment of an artificial agent affected the operational efficiency 
of the organization? 
▪ RQ2. What are the critical success factors of AI deployment? 
We attempt to answer the two RQs via an in-depth case study of multiple AI initiatives 
originated at BT, one of the world’s leading communication services companies. Our research 
offers valuable lessons and insights for both academia and practitioners of operations 
management by exploring the implications of AI adoption in various areas of operations - we 
substantiated and showcased where AI was deployed, how value was created and why certain 
challenges exist. While most studies in the OM literature tend to propose and validate specific 
AI techniques, our study focuses more on the implementation and implications of AI 
techniques. Thus, compared to extant literature that leans more on classic AI techniques, our 
study embraces both classic and emerging (e.g. machine learning) AI. The CSFs framework 
we developed can be used as a guide to aid the successful design and deployment of AI in 
practice and lays a firm foundation for future research. This paper therefore contributes to the 
timely and emerging sociotechnical debates about the real-world implications of AI 
deployment. 
This paper proceeds in the following manner: Section 2 offers a literature review of some basic 
concepts around AI, its application in operations as well the theoretical underpinning of CSFs. 
Section 3 describes our methodological approach, the four use cases and lays out the methods 
of analysis used to interpret collected data. Section 4 presents the main findings and Section 5 
discusses their significance and concludes with a summary of the major findings, study 
limitations and future research directions. 
2. Literature review 
2.1. What is Artificial Intelligence? 
For simplicity’s sake, we define intelligence in this paper as the ability to accomplish complex 
goals (Tegmark 2017). In humans, this manifests as biological intelligence, but when it is 
engineered (non-biological), it is referred to as Artificial Intelligence or ‘AI’. As an academic 
discipline, AI dates back to the mid-1950s, and was coined by John Mc Carthy (who invented 
LISP, the computer language used for the vast majority of AI programme) for the Dartmouth

---


### Page 6

Conference in 1956 to discuss the simulation of intelligent behaviour by machines (Copeland 
2012). Mc Culloch and Pitts are widely recognised as the ones who laid the foundation of AI - 
in 1943 they described mathematical models of neurons in the brain and showed how such 
neurons could learn and hence change their action along the time. Another notable pioneer is 
the British scientist Alan Turning who wrote the famous seminal paper attempting to answer 
the question ‘Can a machine think?’(Turing et al. 2004). 
AI is still quite a “broad” definition, and can be vague, causing some misrepresentation of the 
types of AI that are currently in existence. “Weak” or “narrow” AI is the only form of machine 
intelligence that exists in our world today. This is AI that can be programmed to perform a 
single task such as recommending music via personalised playlists, playing chess, or 
controlling robotic manipulators. While narrow AI can execute tasks in real-time, they are fed 
from a specific dataset, and thus these systems cannot perform outside of the specified tasks 
for which they have been designed. Unlike General or “Strong” AI, (which does not yet exist), 
narrow AI is not conscious, sentient, or driven by emotion (Jajal 2018). 
AI in our paper is defined as the ability of a machine to perform cognitive functions that 
associate with human minds, such as perceiving, reasoning, learning and problem solving 
(Duan, Edwards, and Dwivedi 2019). According to Min (2010), AI can be further classified 
into a number of sub-fields: (1) artificial neural networks (ANN) and rough set theory 
(“thinking humanly”); (2) machine learning, expert systems, and Generic Algorithms (GAs) 
(“acting humanly”); (3) fuzzy logic (“thinking rationally”); and (4) agent-based systems 
(“acting rationally”). There are a broad range of AI techniques (old and new) and some of the 
main ones have been summarised in Figure 1. 
[Figure 1 near here] 
All AI applications require data training sets. Depending on the technique used, an algorithm 
can improve itself by adding a feedback loop that tells it in which cases it made mistakes. The 
main difference between traditional analytic models and AI analytics is that the former uses 
fixed rules to arrive at a conclusion, whilst the latter uses dynamic data and heuristic solutions 
to arrive at conclusions that might elude traditional methods (Danielsson, Macrae, and 
Uthemann 2017). 
The AI problem scope can be categorised with respect to the three-level decision making 
hierarchy of operations management: 1) strategic decisions that deal with long term, executive 
level issues such as facility location and capital investment. 2) tactical decisions that deal with

---


### Page 7

intermediate term, mid manager level issues such as joint demand planning, supplier selection 
and inventory planning and 3) operational decisions that deal with short-term, routine issues 
such as vehicle routing, order picking (Min 2010). 
 2.1.1 Machine learning 
AI does not represent a single technology, rather it is a multidimensional field encompassing a 
range of different technologies and methods such as computer vision, robotics & motion, 
natural language processing, voice recognition and machine learning (Jordan and Mitchell 
2015). Among those, machine learning (a subset of AI that can learn patterns from data without 
the need to define them a priori) is regarded as one of the most prominent developments today 
(Lee and Shin 2019; Murphy and Bach 2012). Powered by recent advances in cloud computing 
and computational processing capacity via powerful GPU cards, and with the abundance of 
‘big data’, machine learning (ML) has been applied in a broad range of areas (Cam, Chui, and 
Hall 2019). For example, companies can train an algorithm to analyse time series data from 
Internet of Things (Io Ts) in order to detect anomalies or make forecasts on the remaining life 
of a component of a machinery, thus supporting predictive maintenance (Susto et al. 2015). 
Conceptually, ML algorithms can be viewed as “searching through a large space of candidate 
programmes, guided by training experience, to find a program that optimises the performance 
metric” (Jordan and Mitchell 2015, 255). ML algorithms can be further categorised by the 
available feedback into supervised, unsupervised, and reinforcement learning (Jordan and 
Mitchell 2015; Wuest et al. 2016). It is worth noting that current research often blends across 
these categories, for instance, semi-supervised learning makes use of unlabelled data to 
augment labelled data in a supervised learning context (Lee and Shin 2019). 
• Supervised learning: is the most widely used ML method and is used to discover the 
mapping function with a dataset that consists of input and output pairs for classification 
and prediction purpose. It takes what it has learned in the past and applies that to new 
data using labelled examples to predict future patterns and events. It learns by explicit 
example. 
• Unsupervised learning: is used to capture the relationship or correlation among input 
data for theme analysis or grouping purposes when no information about desired 
outputs is available. Datasets will not be pre-labelled, and the goal is to find some 
patterns of structure from the data.

---


### Page 8

• Reinforcement learning: is a type of dynamic programming that trains algorithms using 
a system of reward and punishment. It tests different actions to determine which ones 
provide maximum cumulative reward in an environment, as opposed to simply being 
told which action to take. It tends to be used for gaming, robotics and navigation. 
• Semi-supervised learning: The AI model learns from the labelled data to then make a 
judgement on the unlabelled data and find patterns, relationships and structures. 
2.1.2. Deep Learning 
Deep Learning is a subset of ML. In its current state of development, it is a metaphorical and 
literal “black box” that takes one or multiple inputs, such as the data from the sensors in 
driverless vehicles, and processes those inputs into outputs, which are the controls of the 
vehicle (See Figure 2.). In other words, Deep Learning uses Artificial Neural Networks (ANNs) 
to perform a function that takes in data inputs, and ‘spits out solutions’ as data outputs. 
Learning can be supervised, semi-supervised, reinforced or unsupervised. 
As deep learning is deployed more widely, ANNs have already begun solving many of 
society’s problems such as facial recognition along the EU border, language translation, 
spotting deadly tumours, making multi-million-dollar financial trades on the stock market, etc. 
The reality is, however, that: 
‘No one really knows how the most advanced algorithms do what they do [and] that 
could be a problem’ (Knight 2017b). 
AI precision is bundled with opaqueness and a certain interpretive cost that makes these 
technologies be commonly referred to as "black-box" systems. Code is often kept undisclosed 
and is fundamentally difficult (even impossible) to understand. The type of data that is gathered, 
the associations that are targeted, and the concerns that are factored into the algorithmic 
predictions are not at all obvious. These layers of opacity can disguise biased, discriminatory 
or otherwise undesirable results from supervision until negative results become obvious 
(Packin 2017). The problem is that while “black box” ANNs can approximate any function, 
studying the structure of the black box won't reveal any insight into the structure of the function 
that is being approximated. Also, from a traditional statistics viewpoint, ANNs are nonidentifiable models, i.e. given a dataset and network topology, there can be two ANNs with 
different variables that produce the same result. This makes analysis quite difficult. 
[Figure 2 near here]

---


### Page 9

2.2. AI deployment in operations and critical success factors 
Business innovation researchers have long argued that some firms either reconfigure assets and 
existing capabilities to maintain long-term competitive advantages, or that their ambidextrous 
organizational design allows for simultaneous exploration and exploitation of technology, and 
ultimately adaptation over time (O’Reilly and Tushman 2008). In the context of this paper, we 
argue that AI represents an opportunity to significantly contribute to their firms’ 
competitiveness by beginning to invest in their analytic and predictive capacities (Tushman et 
al. 2017). 
2.2.1 AI deployment 
Academic research exploring how AI is deployed in operations and supply chains is still an 
emerging area of interest, given the technology’s rapid rate of development. In the operational 
research field, there are continued efforts in utilising classic AI techniques, for example, for 
demand forecasting (Carbonneau, Laframboise, and Vahidov 2008), job shop scheduling 
(Mesghouni et al. 1999), production line balancing and sequencing (Kim, Kim, and Kim 2000; 
Kucukkoc and Zhang 2015), traffic engineering (Bielli and Reverberi 1996) and inventory 
management (Altay Guvenir and Erel 1998; Jiang and Sheng 2009). Nevertheless, there has 
been a resurgence of interest in recent years. For instance, the work of Fethi and Pasiouras 
(2010) has explored the use of AI techniques in the banking sector via a literature review. Their 
study identifies data envelopment analysis as the most widely applied O.R. technique in the 
field, coupled with AI techniques such as neural networks, support vector machines, and 
multicriteria decision aid that has emerged in recent years. The main areas of application lie in 
bank failure prediction, the assessment of bank creditworthiness and underperformance. In a 
similar vein, Wuest et al. (2016) concentrate on exploring the adoption of ML in manufacturing. 
They argue that supervised ML is a good fit for most manufacturing applications due to the 
fact that the majority of manufacturing applications can provide labelled data. They have 
subsequently discussed a few application cases in areas such as tool/machine condition 
monitoring, image recognition of faulty/damaged products and time series forecasting. 
In practice we see the active exploration of AI in a variety of sectors. A recent global survey 
conducted by Mc Kinsey global institute (Chui et al. 2018) has identified that robotic process 
automation, computer vision, and machine learning are the most commonly deployed AI 
techniques. For each of these, at least 20 percent of respondents say their companies have 
already embedded these technologies into their business processes. Physical robotics and

---


### Page 10

autonomous vehicles are the least commonly deployed, largely because they are relevant only 
to companies in industries such as automotive and transport. Among different sectors, Telecom 
is seen as one of the leading industries (along with financial services, media and high tech) that 
has established significant experience in deploying AI in several areas. Hence, it was chosen 
as the sector for our study. Among respondents in this sector, 75% agree that AI has been 
actively adopted in service operations, product and service development (45%), marketing and 
sales (38%), supply chain management (26%), risk (23%), human resources (17%) and strategy 
and corporate finance (15%). Given that service operations is the most established segment 
for AI, our study focuses predominantly on this area. 
2.2.2 Critical success factors for AI deployment 
The theory of critical success factors (CSFs) has its foundation within strategy research 
(Grimm, Hofstetter, and Sarkis 2014), and is well established in the operations, general 
management and technology management disciplines. CSFs are “those few things that must go 
well to ensure success for an organisation, and therefore must be given special and continual 
attention in order to bring about high performance” (Boynton and Zmud 1984). CSFs have 
been explored in a variety of areas, e.g. ERP implementation (Holland and Light 1999), lean 
implementation (Netland 2015), TQM (Wali, Deshmukh, and Gupta 2003), new product 
development (Cooper and Kleinschmidt 1995), emergency relief logistics (Pettit and Beresford 
2009) sustainability (Luthra et al. 2018) and business process management (Bai and Sarkis 
2013). 
Despite the heightened acceptance and expectations from AI in recent years, there has been a 
lack of systematic efforts in understanding what factors organisations should pay critical 
attention to when it comes to making sense of - and subsequently deploying - AI. Various 
issues, challenges (social, economic, technological, ethical, legal and organisational) and 
opportunities (in various application domains) have been discussed (Duan, Edwards, and 
Dwivedi 2019; Wilson and Daugherty 2018), but most are speculative or based on the review 
of literature. It is therefore hoped that by identifying CSFs in AI deployment via empirical 
research, we can contribute to filling this void in the literature. 
3. Research method 
Our research adopts a case study approach in order to explore the implications of AI adoption 
on operations management. As suggested by Eisenhardt (1989), the case study approach is

---


### Page 11

especially appropriate in new or emerging topic areas. Anchored in real practice, a case study 
can result in a rich and holistic account of a complex phenomenon where the boundaries 
between phenomenon and context are not clearly evident, and provides answers to “how?” and 
“why?” questions (Rowley 2002; Yin 2018). 
As discussed earlier, the telecommunications sector (commonly known as telecom) has been 
one of the leading industries in the use of AI in their operations. Our study focuses on the BT 
organization, the largest provider of consumer fixed-line voice and broadband services and the 
largest mobile network operator in the UK. BT is also a global organisation that provides 
products and services to approximately 180 countries. It was also the first European telecom 
to use AI techniques in workforce scheduling in the 1990s. Since then they have extended the 
use of AI across workforce and resource management and have received numerous industrial 
awards for their innovative work. They have also used AI in other areas such as automated 
network design, process optimisation, cyber-security threat detection and ‘nuisance call’ 
detection. Unlike many organisations which are still experimenting with AI, BT has established 
practices in deploying and subsequently scaling its adoption within its organisation. Being able 
to gain access to such a large organisation with rich experience in AI provides us with 
invaluable insights. 
In this research, we have examined in depth four different AI use cases across a time span of 
over 20 years (See Table 1). These four initiatives were chosen because they present both 
classic and newly established AI techniques, and were deployed at different levels (strategic, 
tactical and operational), offering us a comprehensive understanding about BT’s AI 
deployment journey and the impact it has had on operational performance. 
 
[Table 1 near here] 
3.1 Case study background and BT’s AI initiatives 
Field service operations (FSOs) at BT are characterised by front and back office staff as well 
as non-human resources such as service equipment, network assets, etc. and AI underpins many 
of the core FSO processes. A common FSO scenario for example could involve a customer 
requesting a service/reporting a fault which cannot be configured/resolved automatically, and 
requires one or more engineering or other activities to take place either at the office, the

---


### Page 12

customer’s premise and/or other facilities (e.g. telephone exchange building, a store to collect 
spares, etc.) 
Use case 1: BT has over 20,000 field engineers (with diverse skillsets) serving geographically 
dispersed and diverse customers including internet service providers and end users. Its AIpowered scheduling systems (i.e. resource planning, scheduling and allocation system) are the 
backbone of FSO optimization and allows the company to effectively send the right engineer 
with the right skills to the right location to deliver the right service. Given the importance and 
scale of this AI scheduling system, we chose to examine it as our first use case, where BT was 
able to deploy various AI methods such as constraint programming, heuristic and machine 
learning in combination with artificial neural networks. 
This use case is also interesting because a substantial part of this AI model’s integration into 
the organizations FSOs involves cooperation and co-development with end-users (service 
engineers), and this ‘stakeholder management’ was key to the success of the overall project. 
This use case, therefore, was an ideal opportunity to explore how AI technology was used to 
realise a flexible and efficient scheduling system capable of managing a large organization’s 
field-force. 
Use case 2: The second case study investigates an algorithm developed by researchers at BT, 
that was eventually handed over to – and implemented by the company’s operations division. 
This division maintains the telephone cables, ducts, cabinets and exchanges that connect a 
significant share of homes and businesses to the national broadband and telephone network. 
The ML algorithm implemented by the operations division uses historical data to predict 
whether a landline is healthy enough for reconnection for new customers. If the line is 
determined to be unhealthy, then customers (not end users, but retail operators) are informed 
that an engineer must be deployed on site to carry out the necessary works. If the line is 
determined to be healthy, then an automatic reconnection is established. This algorithm took 
4-6 months from development to implementation and was introduced about 10 years ago and 
remains in use today. 
Use case 3: Field engineers travel to warehouses each morning to source the spare parts that 
they require to perform tasks assigned to them for that day. BT has 90 Fixed warehouses in the 
country they operate. For some engineers this may involve a long travel time between their 
home location and the warehouse, as well as between the warehouse and the service site. The 
company decided to increase the number of operational warehouses to over 700 in order to

---


### Page 13

minimise travel and improve efficiency. These additional warehouses are mobile and need to 
be quickly deployed and redeployed as needed. Warehouses deployed must fulfil multiple 
objectives (e.g. minimise the cumulative travel time for all taskforce, minimise travel distances 
and differences in the number of engineers each warehouse serves). Manually finding 700 sites 
would be too time consuming and hence the company adopted the use of genetic algorithm 
(GA), a heuristic based search technique in AI to optimise the warehouse allocation problem. 
Use case 4: While AI in use case 3 was used at strategic level, focusing on the deployment of 
warehouses to ensure the organisation is set up for optimal performance, use case 4 focuses on 
the use of AI at operational level, to manage its spare parts inventory replenishment in order to 
achieve the agreed customer service level agreement with customers. A hybrid AI-simulation 
approach using meta-heuristics was used to support the decision of which product and which 
spare volume should be replenished at which warehouse. The output of the AI model is a plan 
of spare parts transfer between warehouses over a given number of days against different asset 
replenishment policies and demand profiles. Asset tracking data collected from Io T devices are 
fed back to the algorithm in a dynamic and closed loop. 
3.2. Data collection and analysis method 
This study adopts a longitudinal and participative qualitative research approach, for the 
purposes of capturing relevant themes from the perspectives of AI developers and other 
company stakeholders based on their experiences. It then becomes possible to establish 
linkages between collections of different sets of knowledge within the organization (King and 
Brooks 2017). 
Given the time span of the AI use cases discussed in Section 3.1, our main data collection 
strength lies in that one of the researchers embedded in the case organisation’s R&D division. 
He was a core member of the R&D team and has oversight of the development and 
implementation of the four AI initiatives. He participated regularly in the AI transformative 
programme meetings and kept an AI deployment logbook to record the milestone events and 
reflections. This longitudinal participative approach helps to break the data access barriers in 
otherwise ‘hard to reach’ areas within the organisation. Another strength of this approach is 
that it provides us far more detailed information about BT’s AI deployments in the context 
which they occur than could be collected through a one-off snapshot type of study. 
Longitudinal data collection allows researchers to build up a more accurate and reliably ordered

---


### Page 14

account of the key events and paint a rich and accurate picture of when, how and why critical 
events took place. 
A weakness of participative research is the potential lack of objectivity as the researcher may 
lose his independence through heavy involvement with the company. Through multiple data 
collection methods and triangulation of research findings, this negative effect can be largely 
reduced. Therefore, our further data collection methods include both interviews and intensive 
analysis of a range of secondary data resources e.g. company archival documents and records. 
Four semi-structured interviews were conducted with the programme leads of the initiatives 
which allow us to critically evaluate whether our interpretation of how the initiatives have been 
implemented is valid. We include our interview protocol in Appendix 1. Our respondents were 
based in the UK and France and were selectively targeted for their opinions on the role of AI 
in operations management within the BT organization. This non-probability sampling method 
allowed for the inclusion of key institutional actors in the data gathering process (Penrod et al. 
2003; Tansey 2007). Interviews were recorded, written up, cross checked between researchers 
and later verified by participants. 
Multiple secondary data resources were used in order to further improve research validity, 
including system demonstrations, archival records, BT’s own research publications on AI, the 
company’s press documents, media reports and information available from the company 
website. This secondary source of data was invaluable in providing context for what 
respondents were saying, and also added to the triangulation of information effect (Cresswell 
2010). Finally, investigator triangulation also enhances the robustness of our research findings. 
Two external researchers were involved in the data collection process which improves data 
accuracy and richness through cross check and consolidation. The external researchers have 
had a long-term working relationship with the internal researcher for over a decade. This 
integrative ‘insider’ and ‘outsider’ investigation of the subject cases helped to capture a greater 
richness of data and largely reduces the subjectivities and bias in qualitative research. 
Our data analysis began simultaneously with the gathering of data, and continued throughout 
the data collection process and beyond. We make use of interpretative analysis, which 
combines theoretical awareness with empirical expert assessments, often seen in other 
contemporary industrial case studies (Bergek et al. 2013; Berggren, Magnusson, and 
Sushandoyo 2015; Geels, Dudley, and Kemp 2012). Our data analysis process was based on 
the principles of abductive reasoning whereby the researchers engaged in a to-and-from method

---


### Page 15

between the empirical and the conceptual, in order to make sense of the phenomena under 
study (Ketokivi and Choi, 2014). 
Our first level analysis consists of a detailed description (collated and finalised between 
researchers) of each initiative, based on the data collected from the programme documents, 
logbooks, interview transcripts and a range of secondary data resources. Analysis within use 
case was then conducted. We adopted an open coding process to build concepts and categories. 
Those individual codes were then grouped into categories. For instance, when we explore CSFs, 
there were different issues concerning ‘input data quality’, we would group those codes 
together into the category of data quality. We further assign them to either ‘design’, 
‘deployment’ or ‘post-deployment’ stages. Having undertaken detailed within-use case 
analysis, cross-use case analyses were conducted. Cross-case patterns were then sought by 
looking for similarities and differences among the use cases. Logical connections for any 
differences/similarities were explored through various data sources in order to obtain external 
validity. 
4. Research findings 
4.1 AI deployments in BT 
As evidenced by Table 2, all four AI use cases we examined have delivered significant impact 
on field service operations. We were able to capture and quantify those benefits thanks to our 
longitudinal observation and involvement of those initiatives. Beyond the economic gains those 
use cases have demonstrated, AI methods have also played a critical role in empowering local 
engineers to take more control and influence of their jobs. A notable initiative (as part of use 
case 1) was the development of a work/task recommendation system. Rather than centralised 
task allocation being ‘pushed’ to local engineers, this AI-powered task recommendation system 
with a mobile app allows local engineers to ‘pull’ their own work, for non-priority tasks. Local 
engineers can plan their own routes, bundle work together and swap jobs among team members. 
The ML approach was used to extract knowledge from past jobs, their service outcomes and 
associated text notes to provide engineers with an ordered list of jobs tailored for that specific 
individual, overlaying information with current business priorities while leaving the ultimate 
choice with him/her. This award-winning initiative has demonstrated a noticeable impact on 
the wellbeing of local engineers, with mental health absence down by 36% whilst productivity 
improved by 10%.

---


### Page 16

We found that one of the major roles AI has played within BT is to help planners and engineers 
make better decisions at the strategic, tactical and operational level. As FSO begins to transition 
from experience-based, leader-driven decision making to data-driven decision making, we 
began to observe that employees augment their judgment and intuition with algorithms’ 
recommendations to arrive at better answers than either humans or machines could reach on 
their own. As summarised in Table 2, this resulted in a rise in forecast accuracy, productivity 
and reduction in travel times and operational expenditure. When those decisions are 
decentralised, they drive further behavioural changes and employee empowerment. 
[Table 2 near here] 
Our data shows that the followings are strategically important for the successful deployment 
of AI at scale within BT; 
First, BT used a standard Technology Readiness Level (TRL) framework to initiate, develop 
and implement its AI initiatives. Typically, either its R&D or its operations function will raise 
a business problem or challenge that can be tackled by AI. Then its R&D team will work with 
operations to formulate and define the problem. The analytical studies will inform the 
development of a proof of concept (Po C) and models. Models will be refined taking 
consideration of the contextual constraints and company policies. Simulation tends to be used 
to articulate or visualise a ‘to-be’ future state. The Po C will then be used to gain senior 
management’s support and buy-in. A small-scale pilot/trial will be set up to test how the 
proposed AI method works in practice. If the results are overall positive, a large-scale 
deployment will be rolled out within the organisation. 
Second, the senior executives emphasised that it is very important that AI is not treated as a 
technology being plugged into practice, rather it has always been considered as a business 
transformative programme within BT. It means that the success of those AI initiatives depends 
on how well the technical, political, structural and social aspects of transformation have been 
managed. For instance, gaining stakeholders’ support and engaging with end users at the Po C 
stage is considered as critical. Involving multiple stakeholders and end users at the early stages 
helped to validate requirements and getting the system deployed correctly the first time. It also 
helps to detect any concerns or barriers for the later deployment. For example, if the AI 
initiative would lead to changes in engineers’ work location or task pattern, it is necessary to 
engage with the union at the trial stage. This user/people-centric approach is at the core of the

---


### Page 17

AI transformation process, as pointed out by a service director, ‘We can easily integrate new 
work on the system. The key thing is taking people with us’. 
Another important observation across the four use cases is that while for each individual AI 
initiative, there will be a leader from operations that takes the whole ownership of the 
programme, there is a need for business, IT, and analytics leaders to share accountability for 
the AI transformation. This requires a step change from siloed functional work to crossfunctional team-based work. 
Third, creating a portfolio of AI programmes, rather just having a list of ad hoc initiatives, is 
critical. A systematically planned and organised portfolio helped building the momentum, 
demonstrating the potential and thus sustained the impact. The demonstrable benefits from the 
portfolio projects have helped to remove some of the barriers and challenges faced during the 
deployment such as planners’ fear of becoming obsolete and engagement with local engineers. 
In the four use cases examined, there is a tight connection between AI initiatives at different 
levels, and strong rationales given to the staging and the rollout and the sequencing of these 
over time. For example, when it comes to asset optimisation, use case 3 is concerned with the 
strategic deployment of mobile warehouses in the UK, which then lays the foundation for use 
case 4, which deploys another AI technique to schedule the automated replenishment between 
those mobile warehouses. For workforce schedule and resource management in use case 1, 
strategic forecasting was deployed first, which then informs the tactical capacity planning. 
Capacity planning in turn drives the task scheduling at the daily operational level. 
Despite the standard TRL protocol, people-centric design and deployment, and the systematic 
portfolio approach, the implementation of AI within BT is not without challenges. In the 
following subsections, we zoom in further and offer further details about how AI use cases 
have been implemented at BT and some of the challenges encountered. Constrained by the 
space, we will focus primarily on use cases 1 and 2 where new AI techniques (ML) were used 
and major obstacles for implementation signified. 
4.1.1. Use case 1 
The business problem 
BT has a significant ‘field force’ of more than 20,000 engineers in the field daily, with 
engineers conducting visits to customers and exchanges. For each engineering visit, a particular 
set of skills is required, so both tasks and engineers are multi-skilled, and this requires some

---


### Page 18

consideration, as well as the availability of engineers to carry out these visits. The question for 
BT became; How does the organization orchestrate this operation given the variables at play? 
This was described by an AI specialist respondent as a ‘combinatorial problem’. 
About 20 years ago, BT’s AI research team decided to build an AI framework to model and 
optimise these activities. After several framework designs, a constraint-based model was born, 
which allowed for the easy inclusion of different requirements. On the optimisation side, BT’s 
AI developers used meta-heuristic techniques that are able to produce good solutions in a short 
period of time as the optimisation task was described as a ‘NP-hard problem’ or more simply, 
a problem that cannot be solved in polynomial time. 
During the interviews, respondents stated that while the nature of the problem does not allow 
them to find an optimal solution, (the problem being combinatorial and NP-hard), they could 
get an approximation of the best result. This is largely due to the AI solution being an 
operational system, meaning it is in use and not generated offline. Thus, several optimisations 
are done throughout the day, and for example optimisations that are done earlier in the day – 
before engineers start work – the algorithm has more time to generate a schedule and dispatch 
it to the engineers, so there is somewhat of constraint or trade-off between algorithm speed and 
solution quality. 
Implementation challenges 
When discussing the organizational implementation of this AI solution, one respondent 
described it the following manner: 
What is always difficult in any company, is to make sure the company is actually using 
your [developers’] technology. – Senior AI specialist 
Respondents went on to explain that while it is good to build prototypes, it was ‘very tricky’ to 
make sure that the company was using the technology and extracting the most benefits from it. 
Today, the latest version of the AI scheduling program is currently deployed across BT, and 
the system currently orchestrates around 3000 engineers (and ~150k tasks) daily. The AI model 
is applied to different lines of business, and in different modes of operation. Some lines of 
business will prioritize all an engineer’s given tasks, while others may prioritize only the first 
task of the day and make recommendations throughout the rest of the day, from which the 
engineers may ‘self-select’. While engineers can reject certain tasks prescribed by the 
algorithm, they are not given complete freedom, as productivity would suffer. This is the reason 
why the algorithm’s task rules are based on a recommendation system that filters out certain

---


### Page 19

inefficiencies in order to retain a certain level of productivity. The recommendation system is 
seen as a good balance as it still gives the engineers some latitude over task selection, especially 
unforeseen events like customer issues or engineer overlap etc. Respondents stressed that 
flexibility was key as there is no absolute ‘right or wrong’ in this type of FSO AI application. 
On the management side of the technology’s implementation, respondents revealed that BT’s 
top management was always involved in the development of this AI solution. They also 
explained that the model was purposely designed to be generic from the beginning, because 
the AI development team understood that that there was a trade-off and that the model had to 
be robust enough to cover the organization’s immediate and future needs; aware that the 
business expects results. Respondents reiterated that projects within BT must present robust 
business cases by being able to provide evidence of the benefits to the organization before any 
significant investment is made. The benefits in this case usually fall in one of two categories: 
(1) cost reduction from the optimisation itself and (2) automatization, where less people are 
needed to manage the service. Most of these AI business cases are predicated on cost savings, 
and respondents conceded that this can lead to job displacement and reskilling. It is estimated 
that all AI products deployed within BT to date has ‘helped the business save around £400 
million over a ten-year period’. 
Apart from the business case for their AI application, respondents identified three additional 
levels ‘stakeholder management’. First, it was revealed that top management ‘took a lot of 
convincing’, because the developers had to demonstrate that they could deliver better solutions 
than 3rd party optimisation vendors who were ‘keen to get their wares into the company’. 
Second, operational users (engineers) also needed to be convinced as they were accustomed to 
their own bespoke tools, spreadsheets etc., in addition to feeling some level of job insecurity. 
Lastly, developers had to convince BT’s IT team who had to take onboard this new capability, 
as they were already incentivised to keep things ‘running as they are’ (new capabilities require 
learning and staff training). 
Regarding the decision to develop the AI solution ‘in-house’ over purchasing a solution from 
a 3rd party, the following was expressed by a Service and Management Research decision 
maker: 
The challenge is not the AI models, the challenge is how you model the business 
problem, and to be able to do that, you need domain knowledge, and this is what

---


### Page 20

distinguishes us [inhouse development] from external vendors. Because we are close to 
the business, we are best placed to model those problems. 
Also, with external 3rd party solutions, there are licensing costs (if the tools are not open source), 
so in the short term while this might be a good solution, you lose control of the intellectual 
property (IP) in the long run. It was expressed that there is not a right or a wrong answer here, 
and it depends on what the business needs and what would be the most appropriate solution. 
So total ‘cost of ownership’ or TCO over the lifetime of the project was a significant 
consideration for BT. 
Regarding the challenges of implementing such a system, it was revealed that integrating with 
the operational system is especially challenging because many events must be managed 
simultaneously, and unforeseen events must be addressed while making sure the system 
remains reliable. This contrasts with offline development, which is somewhat easier, where the 
AI application can be run, and results generated without immediately impacting on the day’s 
operations. Also, in the event of an operational system failure, the entirety of the organization’s 
operations may come to a halt. Another challenge is that when business models are engaged 
with AI applications, timescales are short, and if developers are not well prepared, the 
organization may request new functionalities that the team cannot deliver in a timely manner. 
4.1.2. Use case 2 
The business problem 
The business problem driving the AI solution in this second case was described as follows: In 
the UK there are about 25 million premises, and at any given time, BT serves a significant 
share of those premises. Hence, for the remaining premises, in a lot of the cases, BT would 
have served theses premises previously, meaning that there is still ‘network’ going to those 
premises. When a customer, for whatever reason, no longer retains BT’s services, the network 
is left in place, and it becomes what is called a ‘stopped line’. 
Now if that customer decides to come back, or someone at that premise comes back a couple 
of years later and would like service with BT, what happens then? Does BT send an engineer 
out in a week or two to do all the necessary work to make the line good again? Or does BT take 
a gamble by just switching on the line and hoping that it’s going to work? Hence, this decision 
must be made at the time the customer makes the order.

---


### Page 21

About 10 years ago when the operation unit was created, they did not have any intelligence 
about how to make such a decision, and it was basically just a gamble. In a lot of cases, if the 
line has been there for a couple of years, and nobody has been using it, it could have gone 
faulty and wouldn’t work. This would then lead the customers to phone back and complain 
about the line not working, and this resulted in what is called an ‘early-life failure’. 
Thus, over the past decade, these stopped lines would be tested regularly, as all copper lines 
were being electrically tested once or twice a week, and these tests would give BT some idea 
about the health of their lines. However, this information was never used, and these metrics 
were just stored, and nothing further was done. Hence, the opportunity arose to develop an 
algorithm that would predict – based on these electrical measurements – (and a few other things) 
whether a line would work or not, whether it would generate an early-life failure. This 
algorithm was developed in collaboration with a senior manager in the operations unit 
throughout the entire process, and this manager – who was the director for service at the time 
– was the one who originally identified the problem of early-life failures being unacceptably 
high. 
The AI solution that emerged is described as a classification tree / regression model 
combination. Most of the development time of the algorithm was the formulation of the 
problem: What were developers were trying to achieve specifically? What data did they need? 
What data would be available in the system to make these decisions (run the algorithm)? The 
research team developed the algorithm in MATLAB and handed it over to the operations unit, 
who implemented it into their Oracle systems (SQL), and it has since become part of the 
standard order process. In essence, the algorithm runs in the background and decides what 
information should be displayed to the call centre agents when they are dealing with endcustomers. The algorithm decides whether to tell the agent that there is an existing line at the 
premises. If the line is marked as unhealthy, then the customer is not told there is a line there, 
and subsequently, they won’t be able to raise the start order or automatic reactivation on the 
line. They will be forced to go down the engineering activity route or the ‘new line provide’ as 
it is called. The algorithm is invisible to the end customer and call centre agents, and it 
effectively steers how the order will be handled ‘in the dark’. 
Implementation challenges 
The result of this AI solution was that the fraction of early-life failures was reduced by more 
than half, where before it was approximately 15% (thousands per week) and the algorithm

---


### Page 22

brought it down to about 7% or 8%. It was noted by respondents that it was only when these 
results started coming in once the algorithm was deployed, that people in the organization 
began to take notice. The system was designed in such a way that the algorithm can be tuned, 
and this tuneability is to accommodate the trade-off between the number of early life-failures 
and the number of engineering visits, or the costs incurred vs revenues generated, because 
different types of orders will have different cost and revenue impacts. Thus, if the operations 
unit is prepared to tolerate more failures, then there will be fewer engineering visits. Whereas 
if the operations unit wants to reduce the number of early-life failures, then the company will 
have to incur more engineering visits or engineering activity. Revenues are slightly higher 
when an engineer visit is scheduled compared to an automatic restart of a line. 
One key issue highlighted in this case was the ‘explanability’ and transparency of the AI 
algorithm. Project Lead pointed out that when this AI solution was handed over to the 
operations unit, they initially didn’t ‘take ownership’ of the algorithm and considered it as some 
obscure technology that ‘just sat there’ doing its thing in the background. Most of the people 
looking after these processes did not really understand the AI algorithm, as it was a black box 
to them, and this had some adverse effects as time went on. Sometimes the agent (AI 
application) would produce wrong results, but the operations unit managers didn’t have the 
capability to detect the abnormalities and the original BT developers were brought back to sort 
things out. 
Another thing that tended to happen was if the operations unit wanted to change their 
organizational priorities, instead of working with the algorithm, or trying to relearn new rules 
from data, they would manually tinker with the parameters instead. Therefore, there were 
several cases where the operations unit wanted to make a change, but instead of changing the 
algorithm, they put additional processes around the algorithm. For example, they would add an 
additional process step further down the line that would override what the algorithm was 
prescribing, and subsequently just add a lot of complexity to the process. 
Therefore this ‘black box’ effect as we discussed earlier in section 2, if not managed well, could 
lead to detrimental impacts on operations. ALL of the users of AI (not just the core members) 
should be trained to have a proper understanding of its functionality and take the ownership of 
the algorithm in order to mitigate the potential risks of AI producing wrong outputs and driving 
wrong decisions or behaviours.

---


### Page 23

On the other hand, if a user really understands how the algorithm works, there could be a 
potential adverse effect on the opposite end of the spectrum. An interesting example was 
speculated by a senior AI developer at BT regarding people within the operations unit, involved 
in planning or business improvement, who could twist the algorithmic process itself: 
There were people [at the operations unit] who knew how it [certain algorithmic 
parameters] worked, and they could kind of game the system, so you got what you 
might call ‘partisan decision making’. [For example] if there was one guy who 
understood how it worked, and he was part of the organization that looked after revenue, 
he could then game the system, so that he got more revenue, he could tweak one of the 
parameters because we gave [the operations unit] control of a threshold they could set. 
And the fact that it then led to more engineering visits, but he didn’t tell anybody, and 
because it was a black box, the people looking after the cost and engineering workforce 
they didn’t know why they got more engineering activities they had to do. So, when 
you’ve got an organization where the different KPIs are looked after by different teams, 
you’ve got some people that understand how to tweak these algorithms and others who 
don’t, then you can get those kinds of games being played. 
This phenomenon resembles ‘adversarial perturbations’ (Eykholt et al. 2017) or ‘white-box 
scenarios’ (Sharif et al. 2016) created by adversarial human agents who know about the internal 
architecture or parameters of the AI system in question. Competent and responsible ownership 
or ‘control’ over the algorithm or AI system was key in this case in order to facilitate proper 
system functionality. 
4.1.3 Summary 
As Use cases 3 and 4 utilise classic AI optimisation techniques, the issue discussed in Use case 
2 about AI explanability and transparency was not significant. As with Use case 1, both Use 
cases 3 and 4 stress the importance of buy-in from senior management and early stakeholder 
engagement. Across the four cases, our respondents’ emphasis was that AI is not deployed to 
replace but empower the existing human capital within the organization by improving their 
decision making. 
Some of the best practice takeaways from our observations for individual AI design and 
implementation were that the utilisation of business process (re)engineering concept (BPR) 
(Grover et al. 1995; Towill 1997): the AI transformative team need to clearly map out “as-is”

---


### Page 24

processes (current state) and articulate the “to-be” processes (future state). As-is process review 
forces the team to define its current processes accurately. If they are not clearly stated, the tobe processes may allow developers to shortcut some processes post-deployment. It was 
perceived that although some of the AI techniques may be new, the principles of business 
system engineering still apply in the company’s digital transformative programmes. BPR 
affords proper planning by outlining a clear roadmap and vision from the start – which was 
critical to ensuring the success of the AI initiatives. 
Another best practice suggestion reflected by the transformation programme leads was the clear 
formation of the problem (problem definition). All programme leads concur that this probably 
was the hardest yet most important part of the AI application development cycle. A clearly 
defined problem specifies the boundary of the transformation programme and related 
stakeholders, pinpoints key critical issues to address as well as appreciates the social/cultural 
factors that shape the problem. 
Once the problem is clearly formulated, the next is to embed the right AI logic into the AI 
programme in order to produce desirable outputs. To do this, we need competent AI developers 
who not only have expertise knowledge in AI but also understand how the business works. The 
management team acknowledges that talent with both set of skills are rare but throughout two 
decades of development, the company has successfully developed a pool of in-house talents 
that reside in its R&D team. This, however, may still be a significant barrier for smaller 
companies. 
Finally, our observation suggests that having this central capability, though important, may not 
be sufficient on its own. As indicated by use case 2, there is a need to bridge the AI world with 
business operations – the transformation programme needs someone as a ‘translator’ who really 
understands how things work in the business domain and takes an active role in developing the 
use case with the data scientists and data engineers. We feel that the translators will have to 
understand how AI algorithms work, the value of AI analytics in his or her business domain, 
and act as catalyst to convince his/her peers to use the outputs generated by AI for operations 
management. 
4.2 Critical success factors for AI deployment 
We took the good practices, challenges and lessons learnt in Section 4.1, combined them with 
further examination of evidences and our own reflections, to propose a list of critical success

---


### Page 25

factors (CSFs) for the successful implementation of AI in FSO. These factors are summarised 
in Table 3. We arrange those factors based on pre-, during and post-deployment stages. We 
corroborated those factors within the R&D team as well as with project leads and received no 
objections. 
[Table 3 near here] 
Development stage 
At the development phase, strategy formulation, not only among AI developers, but in 
collaboration with business executives was key. This is the starting point of an AI initiative, 
i.e. to identify areas where there are pertinent problems that AI technology would help address. 
Within BT, a robust business rationale (‘business case’) is the main prerequisite for making 
resources available to special projects like AI development. Hence the AI strategy has been 
clearly formulated to set the vision, articulate the business value that is expected out of the AI 
initiative(s) and the specific objectives to capture the value. 
Without the support of top management, it is unlikely that any AI initiative will achieve the 
target impact, or even go into production at a later stage. The AI developers in these cases had 
to have the sponsorship of senior management in order to drive these projects to fruition. 
Previous research suggests that when top management share their vision on digital 
transformation, they tend to bring the majority of employees on board (Fitzgerald et al. 2013). 
Stakeholder buy-in is an equally important factor. Effective stakeholder engagement would 
result in a common vision which is a prerequisite for success in projects like these. In all four 
use cases, the AI development team adopted a people-centric design philosophy, and actively 
worked with the IT department, external clients, business domain managers, human resources 
and end-users across all stages, particularly at the development stage. Buy-in from end users 
at the proof-of-concept or ‘beta testing’ phase is of particular importance, where their input not 
only improves the accuracy of the model but also empowers these users by giving them a sense 
of security and control. From a more operational perspective, as articulated in section 4.1.3, 
proper problem formulation and a competent in-house development team across different 
functions were all CSFs in BT’s AI deployment. 
We want to emphasise the importance of data availability and quality at the deployment stage. 
All AI algorithms require data training sets. The outputs an AI algorithm generates are only as 
good as the quality of input data. This leads to a much-debated issue on AI introduced bias in 
decision making – AI models can embed bias and deploy them at scale (Knight 2017a; Manyika,

---


### Page 26

Silberg, and Presten 2019). Underlying data are often the source of bias therefore it is 
extremely important the AI models get fed the right data. It is essential that organisations are 
aware of the contexts in which there may be high risk for AI to exacerbate bias. Minimising 
bias would help an AI programme to gain trust and reach its potential. The data availability is 
another critical issue. In many organisations, not just within our case company, data exist in 
different legacy systems and in different formats which can be a challenge. This disparity may 
demand a great deal of effort in preparing the data set before feeding them into the AI model. 
Deployment stage 
During BT’s AI deployment phase, stakeholder management continued with the top-down 
training of ‘gold’ or master trainers who would then train staff below them. All users of an AI 
algorithm should understand how it works, at least, in principle. As evidenced in use case 2, 
there was asymmetric understanding of how the algorithm works among those charged with its 
care. Lack of understanding may result in workaround rather than work with AI, resulting in 
unnecessary processes and efforts put in place, or risk of being exploited by others who 
understand and are able to manipulate the algorithm. So, the CSF here would be adequate / 
appropriate training for not just some staff, but all staff that engage with the algorithm. This 
large-scale training could potentially accelerate the penetration of AI applications within 
businesses, leading to more initiatives being proposed, piloted and rolled out. Communication 
and training go hand in hand. It helps to raise AI awareness and could also facilitate cross 
learning between different functions. At the strategic level, effective communication conveys 
the vision of the AI transformative programmes and helps to gain buy-in and continuous use 
of AI – hence being considered as a critical factor. 
A concession made by BT was the concern about how ‘visible’ and ‘explainable’ these AI 
systems and their decision-making processes were to the end-users that were being guided by 
the system. In both use cases 1 and 2, the developers acknowledged that aspects of these models 
were indeed ‘black boxes’(Danielsson, Macrae, and Uthemann 2017). The concept of AI 
transparency also emerged where in the second use case, the algorithm was invisible to most 
stakeholders, yet it assessed, decided and steered the direction of important processes that these 
stakeholders were involved in. The explanablility and transparency challenge is not unique to 
BT, but is a problem facing many organisations (Burt 2018). There is no easy solution to it. 
High tech companies such as Google have begun to develop tools and frameworks to deploy 
interpretable and inclusive machine learning models but there is still a long way to go. For our

---


### Page 27

case company BT, it continues to work with universities and other research partners to address 
this challenge. 
Equally challenging is the issue of AI governance – another critical factor that must be taken 
seriously. There is an increasing concern regarding the risk of harm associated with the use of 
AI technologies if they are not deployed in a responsible manner, and the data within these 
models is not managed properly. AI governance deals with a number of complex ethical issues 
such as data protection and privacy, security, safety, bodily and mental integrity, justice, 
equality and solidarity (World Economic Forum 2019). Ideally, organisations should have an 
AI governance framework utilising self- and co-regulatory approaches informed by current 
laws and perspectives from companies, academia, and associated technical bodies to curb 
inopportune AI use. However, like many organisations, BT is still trying to find the best way 
to manage those issues. 
Codifying or integrating the right AI logic into existing IT applications is important in order to 
automate the scheduling and optimisation processes. Those IT applications operationalise the 
AI logic and translate them into expected outputs. Without this process, AI algorithms will not 
function properly. In practice, we see many IT systems such as enterprise resource planning, 
production planning, transport scheduling and task scheduling to facilitate the planning and 
scheduling of certain operation activities. To utilise the increasingly available data from those 
systems, AI needs to integrate with those operational systems in order to generate the outputs. 
That implies that AI developers need to work closely with IT departments in order to embed 
the right AI algorithms into practice. 
Post-deployment 
Post-deployment CSFs are equally important. Having a set of Key Performance Indicators 
(KPIs) in place to monitor operational performance helps to evaluate whether AI has delivered 
positive impacts on operation performance. The right KPIs will motivate and incentivise the 
right behaviours (Kaplan and Norton 1992). It is worth noting that performance measurement 
systems need to continue to reflect their environment and strategies and need to be revised 
along with the business change (Kennerley and Neely 2003). While the exact KPIs need to be 
determined based on individual AI programmes, those KPIs for AI transformation programmes 
should in principle enable companies to examine how well the changes associated with the AI 
model occurs and whether it is working as intended.

---


### Page 28

The same logic holds for the AI algorithms themselves. As was evidenced in our use cases, the 
AI models should be reviewed and audited for fitness post-deployment, and just as importantly, 
the in-house expertise must be in place to detect and correct any problems that may arise. 
Another post-deployment measure would be the built-in option to correctly adjust the 
algorithm’s parameters in a user-friendly manner that would allow for better optimisation as 
the business environment and logic changes. User-friendliness is key, as this would circumvent 
the need for long and expensive developer update cycles. 
Finally, proper ownership of the AI model or algorithm is arguably at the root of all postdeployment CSFs. If there is no one person or team ultimately responsible for the AI system 
after ‘handover’, then it runs the risk of being ignored, underused, and can malfunction or even 
be exploited. Deciding where responsibility should lie within the organisation, as suggested by 
Fountaine et al., (2019), should be influenced by the maturity of AI capability, business model 
complexity and the pace and level of technical innovation required. 
5. Discussion and Conclusion 
Driven by the emerging demand for contemporary empirical research and understanding 
around AI deployment in operations management, we set out to explore the implications of AI 
in field service operations. Via an in-depth case study of four large AI initiatives across a time 
span of 20 years at BT, one of the world’s leading communication services companies, we 
explored the answers to the following two RQs. 
▪ RQ1. How has the deployment of an artificial agent affected the operational efficiency 
of the organization? 
The four use cases of AI applications examined in this paper, while being different in context, 
raised some common points of interest as it relates to the implementation of AI in service 
operations management. All four AI use cases have delivered significant impact on field 
service operations in terms cost saving, time reduction and productivity improvement. They 
have augmented better decision making and played a critical role in empowering local 
engineers to take more control and exert more influence over their jobs. Our study found that 
having a standard TRL protocol, people-centric approach, as well as the establishment of a 
portfolio in AI initiatives were instrumental to BT’s success in the design and deployment of 
AI at scale in its field operations. We also observed that when it comes to individual AI 
initiatives, the use of BPR affords BT a structured way for digital transformation. The problem

---


### Page 29

formulation is perceived as most critical as it draws the boundary and lays the foundation for 
AI model development. Our study also identified several challenges, ranging from stakeholder 
management to AI explanability. 
▪ RQ2. What are the critical success factors of AI deployment? 
Through a detailed examination of the use cases, we were able to draw out a total of seventeen 
CSFs for AI deployment in field service operations. Those are arranged at development, 
deployment and post-deployment stages and are discussed in depth in Section 4.2. An 
important argument we make here is that the AI deployment process is iterative and continual, 
and organisations need to monitor and track the value AI generates and regularly review the 
fitness of AI models. This last lag of activities tends to be forgotten in practice yet is of critical 
importance. 
We make two important theoretical contributions. First, the findings from our study provide 
valuable new insights into how the deployment of AI has affected the efficiency of field service 
operations in practice. Although research on AI dates back to 1950s, most research in the OM 
literature tends to propose and develop classic AI techniques, and studies that are able to 
empirically evidence the impact of AI on operations are very rare (Duan, Edwards, and 
Dwivedi 2019; Min 2010). Being able to gain access to a large organisation such as BT where 
both classic and emerging AI applications such as machine learning have been deployed at 
scale offered us a rare opportunity to examine multiple AI initiatives in practice and extract 
key learning points for both practitioners and scholars. Our study explored the implications of 
AI adoption in various areas of operations, and substantiated and showcased where AI was 
deployed, how value was created and why certain challenges exist. 
Our second contribution is the identification of a range of CSFs that are essential to the 
successful deployment of AI in operations, filling an important void in the literature. To our 
knowledge, this is the first study that attempts to establish a framework that encapsulates 
critical factors for AI deployment in our discipline. Studies in operations and technology 
management have long been using well established theories such as Diffusion of Innovation 
(Do I) (Rogers 2003), Technology-organisation-environment (TOE) framework (Tornatzky, 
Fleischer, and Chakrabarti 1990), and technology acceptance model (TAM) (Venkatesh and 
Davis 2000; Venkatesh et al. 2003; Davis 1989) to investigate factors that influence the 
decision to adopt or reject a particular technological innovation. For example, Fosso Wamba 
et al (2016), via a survey of over 400 SME managers found that intention to adopt RFID

---


### Page 30

technology is mainly related to RFID’s relative advantage and compatibility, the firm’s size 
and the country where the adopting organisation is located. However this stream of research 
tends to focus on factors affecting the intention of adoption, not the actual adoption; whereas 
our study explores the factors that determine the success of the entire lifecycle (i.e. 
development, deployment and post-deployment) of AI adoption in organisations. 
With studies that do investigate the factors influencing actual implementation, such as the work 
of Soja (2010) and Zhang and Dhaliwal (2009), our findings resonate with some of the key 
factors identified. For instance the ‘sufficient in-house expertise’ CSF corresponds to the factor 
of ‘managerial IT knowledge’ suggested by Zhang and Dhaliwal (2009), and the ‘problem 
formulation’ CSF bears some similarities with ‘clear project definition’ proposed by Soja 
(2010). Yet it is important to point out that while some factors (such as the ones discussed 
above) we identified are generic and observable from other technological innovation adoptions, 
the majority of the factors derived from our studies are unique to AI deployment. Therefore, 
our study serves as a foundation for future research to further validate and/or expand the factors 
we have identified in other operation settings. 
For practitioners, our study presents how a systematic approach should be established in 
capturing the best value out of AI initiatives. BT’s case demonstrates that TRL is an effective 
guiding framework for organisations to initiate, develop and implement its AI initiatives. We 
stress the need to treat AI not as technology-push exercise but as a strategic digital 
transformation programme. We also highlight that if done well, the people-centric and multiple 
stakeholder management would ensure organisational buy-in and employee empowerment. We 
emphasise the need to create a portfolio of AI initiatives in order to deploy AI at scale. For 
individual AI design and implementation, we found utilising the concept of BPR helped 
executives to develop a clear roadmap and vision for improvement, and ensure that AI 
initiatives delivered the expected impact. Our CSF framework offers a useful guide to 
organisations that wish to embark on the journey of AI and about the factors that will determine 
success or failure of an AI programme. 
As this research is based on a single case study of BT and given the explorative nature of this 
study, future research should explore whether our findings could be applicable to the wider 
telecom industry. As a major European and global player, BT largely resembles the 
characteristics of a typical telecom provider in industry and lessons learnt could potentially be 
transferable to other providers. Given the insights set out in this paper, it may be possible for

---


### Page 31

other scholars to apply some of our findings to better understand the role of AI in other highly 
regulated, service-based industries. Future research should examine more cases in the same 
sector or across sectors to add further insights to this under researched area. The use of Delphi 
studies to elucidate the factors we identified or new factors will add further academic rigor to 
the identification of CSFs. A large-scale survey to test the causal relation between those factors 
and organisational performance is equally interesting. These will continue to contribute and 
extend our understanding of the impact of AI in operations. 
Future studies that examine the implications of more ‘disruptive’ types of AI initiatives would 
also be worthwhile. While significantly impactful, these applications of AI we have studied are 
exploitative, and did not fundamentally change the organization’s business models or create 
new value networks (Christensen et al. 2018; HBR 2015; Kapoor and Klueter 2014). Rather, 
these models took control over some key decision-making processes within BT’s field service 
operation. This paper, however, was able to capture FSO rate of improvement – thanks to 
artificial intelligence – within the organization, which was reflected in the metrics that were 
reported by BT. 
Acknowledgement: 
We would like to extend our sincere thanks to Dr. Kjeld Jensen and Dr. Raphael Dornet at BT 
for their valuable support and insights to our research.

---


### Page 32

Appendix 1 
Interview protocol 
I. Introduction 
a. Research motivation and objectives 
b. Confidentiality, research consent and permission for recording 
II. General background information 
a. Interviewee’s role and responsibility within the organisation, years of 
experience and areas of expertise 
III. Detailed interview questions 
The following interview questions will act as the principal topics of discussion, although we 
will use follow-up questions if necessary, depending on the direction of the interview. 
1. Can you please give us a brief introduction about the AI deployment within your 
organisation? 
2. How was the [XXX] project initiated? And why? What are the primary goals and 
expected outcomes? 
3. Who led (is leading) the AI transformation process? What are the key managerial 
decisions behind the deployment of this artificial intelligence model? 
4. How did (or will) the AI project change the existing practices? (business model/value 
chain/knowledge transfer) 
5. In your opinion, what are the main challenges and risks along the AI deployment? 
How those risks are mitigated? 
6. Who are (or will be) affected by this AI deployment? 
o Employees 
o Customers 
o Suppliers 
o Other stakeholders 
7. What are the benefits of AI deployment on organisation performance? E.g. on certain 
KPIs. 
8. Are there any lessons learnt and best practices you’d like to highlight? 
9. Which criticisms or drawbacks do you think might drive supply chain practitioners 
away from the technology? 
10. Do you have anything else to add?

---


### Page 33

References 
Altay Guvenir, H., and Erdal Erel. 1998. ‘Multicriteria Inventory Classification Using a 
Genetic Algorithm’. European Journal of Operational Research 105 (1): 29–37. 
https://doi.org/10.1016/S0377-2217(97)00039-8. 
Bai, Chunguang, and Joseph Sarkis. 2013. ‘A Grey-Based DEMATEL Model for Evaluating 
Business Process Management Critical Success Factors’. International Journal of 
Production Economics 146 (1): 281–92. https://doi.org/10.1016/j.ijpe.2013.07.011. 
Baryannis, George, Sahar Validi, Samir Dani, and Grigoris Antoniou. 2019. ‘Supply Chain 
Risk Management and Artificial Intelligence: State of the Art and Future Research 
Directions’. International Journal of Production Research 57 (7): 2179–2202. 
https://doi.org/10.1080/00207543.2018.1530476. 
Benner, Mary J., and Michael L. Tushman. 2015. ‘Reflections on the 2013 Decade Award—
“Exploitation, Exploration, and Process Management: The Productivity Dilemma 
Revisited” Ten Years Later’. Academy of Management Review 40 (4): 497–514. 
https://doi.org/10.5465/amr.2015.0042. 
Bergek, Anna, Christian Berggren, Thomas Magnusson, and Michael Hobday. 2013. 
‘Technological Discontinuities and the Challenge for Incumbent Firms: Destruction, 
Disruption or Creative Accumulation?’ Research Policy 42 (6): 1210–1224. 
Berggren, Christian, Thomas Magnusson, and Dedy Sushandoyo. 2015. ‘Transition Pathways 
Revisited: Established Firms as Multi-Level Actors in the Heavy Vehicle Industry’. 
Research Policy 44 (5): 1017–28. https://doi.org/10.1016/j.respol.2014.11.009. 
Bielli, Maurizio, and Pierfrancesco Reverberi. 1996. ‘New Operations Research and Artificial 
Intelligence Approaches to Traffic Engineering Problems’. European Journal of 
Operational Research 92 (3): 550–72. https://doi.org/10.1016/0377-2217(96)00010-0. 
Boynton, Andrew C., and Robert W. Zmud. 1984. ‘An Assessment of Critical Success Factors’. 
Sloan Management Review 25 (4): 17–27. 
Bullers, William I., Shimon Y. Nof, and Andrew B. Whinston. 1980. ‘Artificial Intelligence in 
Manufacturing Planning and Control’. A I I E Transactions 12 (4): 351–63. 
https://doi.org/10.1080/05695558008974527. 
Burt, Andrew. 2018. Regulating Artificial Intelligence: How to Control the Unexplainable. 
The 
University 
of 
Chicago. 
https://www.youtube.com/watch?v=jc E5JPImxfc&t=1433s. 
Cam, Arif, Michael Chui, and Bryce Hall. 2019. ‘Survey: AI Adoption Proves Its Worth, but 
Few 
Scale 
Impact 
| 
Mc Kinsey’. 
Industry. 
Mc Kinsey. 
https://www.mckinsey.com/featured-insights/artificial-intelligence/global-ai-surveyai-proves-its-worth-but-few-scale-impact. 
Carbonneau, Real, Kevin Laframboise, and Rustam Vahidov. 2008. ‘Application of Machine 
Learning Techniques for Supply Chain Demand Forecasting’. European Journal of 
Operational Research 184 (3): 1140–54. https://doi.org/10.1016/j.ejor.2006.12.004. 
Christensen, Clayton M., Rory Mc Donald, Elizabeth J. Altman, and Jonathan E. Palmer. 2018. 
‘Disruptive Innovation: An Intellectual History and Directions for Future Research’. 
Journal of Management Studies 55 (7): 1043–78. https://doi.org/10.1111/joms.12349. 
Chui, Michael, James Manyika, Mehdi Miremadi, Nicolaus Henke, Rita Chung, Pieter Nel, 
and Sankalp Malhotra. 2018. ‘Sizing the Potential Value of AI and Advanced Analytics 
| 
Mc Kinsey’. 
Mc Kinsey. 
https://www.mckinsey.com/featured-insights/artificialintelligence/notes-from-the-ai-frontier-applications-and-value-of-deep-learning. 
Cooper, Robert G., and Elko J. Kleinschmidt. 1995. ‘Benchmarking the Firm’s Critical Success 
Factors in New Product Development’. Journal of Product Innovation Management 12 
(5): 374–91. https://doi.org/10.1111/1540-5885.1250374.

---


### Page 34

Copeland, Jack. 2012. Artificial Intelligence: A Philosophical Introduction. Oxford, UK ; 
Cambridge, Mass: W.B. 
Cresswell, Tim. 2010. ‘Towards a Politics of Mobility’. Environment and Planning D: Society 
and Space 28 (1): 17–31. 
Danielsson, Jon, Robert Macrae, and Andreas Uthemann. 2017. ‘Artificial Intelligence, 
Financial Risk Management and Systemic Risk’. LSE Systemic Risk Centre. 
http://www.systemicrisk.ac.uk/publications/SP13. 
Davis, Fred D. 1989. ‘Perceived Usefulness, Perceived Ease of Use, and User Acceptance of 
Information 
Technology’. 
MIS 
Quarterly 
13 
(3): 
319–40. 
https://doi.org/10.2307/249008. 
Duan, Yanqing, John S. Edwards, and Yogesh K Dwivedi. 2019. ‘Artificial Intelligence for 
Decision Making in the Era of Big Data – Evolution, Challenges and Research 
Agenda’. International Journal of Information Management 48 (October): 63–71. 
https://doi.org/10.1016/j.ijinfomgt.2019.01.021. 
Eisenhardt, Kathleen M. 1989. ‘Building Theories from Case Study Research’. The Academy 
of Management Review 14 (4): 532–50. https://doi.org/10.2307/258557. 
Eykholt, Kevin, Ivan Evtimov, Earlence Fernandes, Bo Li, Amir Rahmati, Chaowei Xiao, Atul 
Prakash, Tadayoshi Kohno, and Dawn Song. 2017. ‘Robust Physical-World Attacks on 
Deep 
Learning 
Models’. 
Ar Xiv:1707.08945 
[Cs], 
July. 
http://arxiv.org/abs/1707.08945. 
Fethi, Meryem Duygun, and Fotios Pasiouras. 2010. ‘Assessing Bank Efficiency and 
Performance with Operational Research and Artificial Intelligence Techniques: A 
Survey’. 
European 
Journal 
of 
Operational 
Research 
204 
(2): 
189–98. 
https://doi.org/10.1016/j.ejor.2009.08.003. 
Fitzgerald, Michael, Nina Kruschwitz, Didier Bonnet, and Michael Welch. 2013. ‘Embracing 
Digital 
Technology’. 
MIT 
Sloan 
Management 
Review. 
2013. 
https://sloanreview.mit.edu/projects/embracing-digital-technology/. 
Fosso, Wamba Samuel, and Shahriar Akter. 2019. ‘Understanding Supply Chain Analytics 
Capabilities and Agility for Data-Rich Environments’. International Journal of 
Operations 
& 
Production 
Management 
39 
(6/7/8): 
887–912. 
https://doi.org/10.1108/IJOPM-01-2019-0025. 
Fountaine, Tim, Brian Mc Carthy, and Tamim Saleh. 2019. ‘Building the AI-Powered 
Organization’. 
Harvard 
Business 
Review, 
1 
July 
2019. 
https://hbr.org/2019/07/building-the-ai-powered-organization. 
Geels, Frank W., Geoff Dudley, and René Kemp. 2012. Findings, Conclusions and 
Assessments of Sustainability Transitions in Automobility. Routledge, New York, NY, 
USA and Oxon, United Kingdom. 
Grimm, Jörg H., Joerg S. Hofstetter, and Joseph Sarkis. 2014. ‘Critical Factors for SubSupplier Management: A Sustainable Food Supply Chains Perspective’. International 
Journal of Production Economics, Sustainable Food Supply Chain Management, 152 
(June): 159–73. https://doi.org/10.1016/j.ijpe.2013.12.011. 
Grover, Varun, Seung Ryul Jeong, William J. Kettinger, and James T. C. Teng. 1995. ‘The 
Implementation of Business Process Reengineering’. Journal of Management 
Information 
Systems 
12 
(1): 
109–44. 
https://doi.org/10.1080/07421222.1995.11518072. 
HBR. 2015. ‘Tesla’s Not as Disruptive as You Might Think’. Harvard Business Review, 1 May 
2015. https://hbr.org/2015/05/teslas-not-as-disruptive-as-you-might-think. 
Holland, C.R., and B. Light. 1999. ‘A Critical Success Factors Model for ERP 
Implementation’. IEEE Software 16 (3): 30–36. https://doi.org/10.1109/52.765784.

---


### Page 35

Jajal, Tannya D. 2018. ‘Distinguishing between Narrow AI, General AI and Super AI’. 
Medium. 21 May 2018. https://medium.com/@tjajal/distinguishing-between-narrowai-general-ai-and-super-ai-a4bc44172e22. 
Jiang, Chengzhi, and Zhaohan Sheng. 2009. ‘Case-Based Reinforcement Learning for 
Dynamic Inventory Control in a Multi-Agent Supply-Chain System’. Expert Systems 
with Applications 36 (3, Part 2): 6520–26. https://doi.org/10.1016/j.eswa.2008.07.036. 
Jordan, M. I., and T. M. Mitchell. 2015. ‘Machine Learning: Trends, Perspectives, and 
Prospects’. Science 349 (6245): 255–60. https://doi.org/10.1126/science.aaa8415. 
Kaplan, Robert S., and David P. Norton. 1992. ‘The Balanced Scorecard—Measures That 
Drive 
Performance’. 
Harvard 
Business 
Review, 
1 
January 
1992. 
https://hbr.org/1992/01/the-balanced-scorecard-measures-that-drive-performance-2. 
Kapoor, Rahul, and Thomas Klueter. 2014. ‘Decoding the Adaptability–Rigidity Puzzle: 
Evidence from Pharmaceutical Incumbents’ Pursuit of Gene Therapy and Monoclonal 
Antibodies’. 
Academy 
of 
Management 
Journal 
58 
(4): 
1180–1207. 
https://doi.org/10.5465/amj.2013.0430. 
Kennerley, Mike, and Andy Neely. 2003. ‘Measuring Performancein a Changing Business 
Environment’. International Journal of Operations & Production Management 23 (2): 
213–29. https://doi.org/10.1108/01443570310458465. 
Kim, Yeo Keun, Sun Jin Kim, and Jae Yun Kim. 2000. ‘Balancing and Sequencing MixedModel U-Lines with a Co-Evolutionary Algorithm’. Production Planning & Control 
11 (8): 754–64. https://doi.org/10.1080/095372800750038355. 
King, Nigel, and Joanna Brooks. 2017. Template Analysis for Business and Management 
Students. London, UK: Sage. https://uk.sagepub.com/en-gb/eur/template-analysis-forbusiness-and-management-students/book244282#description. 
Klumpp, Matthias. 2018. ‘Automation and Artificial Intelligence in Business Logistics 
Systems: Human Reactions and Collaboration Requirements’. International Journal of 
Logistics 
Research 
and 
Applications 
21 
(3): 
224–42. 
https://doi.org/10.1080/13675567.2017.1384451. 
Knight, Will. 2017a. ‘How to Root Out Hidden Biases in AI’. MIT Technology Review. 2017. 
https://www.technologyreview.com/s/609130/how-to-root-out-hidden-biases-in-ai/. 
———. 2017b. ‘There’s a Big Problem with AI: Even Its Creators Can’t Explain How It 
Works’. 
MIT 
Technology 
Review. 
2017. 
https://www.technologyreview.com/s/604087/the-dark-secret-at-the-heart-of-ai/. 
Kucukkoc, Ibrahim, and David Z. Zhang. 2015. ‘A Mathematical Model and Genetic 
Algorithm-Based Approach for Parallel Two-Sided Assembly Line Balancing 
Problem’. 
Production 
Planning 
& 
Control 
26 
(11): 
874–94. 
https://doi.org/10.1080/09537287.2014.994685. 
Lee, In, and Yong Jae Shin. 2019. ‘Machine Learning for Enterprises: Applications, Algorithm 
Selection, 
and 
Challenges’. 
Business 
Horizons, 
November. 
https://doi.org/10.1016/j.bushor.2019.10.005. 
Luthra, Sunil, Sachin Kumar Mangla, Ravi Shankar, Chandra Prakash Garg, and Suresh Jakhar. 
2018. ‘Modelling Critical Success Factors for Sustainability Initiatives in Supply 
Chains in Indian Context Using Grey-DEMA℡’. Production Planning & Control 29 
(9): 705–28. https://doi.org/10.1080/09537287.2018.1448126. 
Manyika, James, Jake Silberg, and Brittany Presten. 2019. ‘What Do We Do About the Biases 
in AI?’ Harvard Business Review, 25 October 2019. https://hbr.org/2019/10/what-dowe-do-about-the-biases-in-ai. 
Martínez-López, Francisco J., and Jorge Casillas. 2013. ‘Artificial Intelligence-Based Systems 
Applied in Industrial Marketing: An Historical Overview, Current and Future Insights’. 
Industrial Marketing Management, Special Issue on Applied Intelligent Systems in

---


### Page 36

Business-to-Business 
Marketing, 
42 
(4): 
489–95. 
https://doi.org/10.1016/j.indmarman.2013.03.001. 
Mesghouni, K., P. Pesin, D. Trentesaux, S. Hammadi, C. Tahon, and P. Borne. 1999. ‘Hybrid 
Approach to Decision-Making for Job-Shop Scheduling’. Production Planning & 
Control 10 (7): 690–706. https://doi.org/10.1080/095372899232768. 
Min, Hokey. 2010. ‘Artificial Intelligence in Supply Chain Management: Theory and 
Applications’. International Journal of Logistics Research and Applications 13 (1): 13–
39. https://doi.org/10.1080/13675560902736537. 
Murphy, Kevin P., and Francis Bach. 2012. Machine Learning: A Probabilistic Perspective. 
Cambridge, MA: MIT Press. 
Netland, Torbjørn. 2015. ‘Critical Success Factors for Implementing Lean Production: The 
Effect of Contingencies’. SSRN Scholarly Paper ID 2716939. Rochester, NY: Social 
Science Research Network. https://papers.ssrn.com/abstract=2716939. 
O’Reilly, Charles A., and Michael L. Tushman. 2008. ‘Ambidexterity as a Dynamic 
Capability: Resolving the Innovator’s Dilemma’. Research in Organizational Behavior 
28 (January): 185–206. https://doi.org/10.1016/j.riob.2008.06.002. 
Packin, Nizan Geslevich. 2017. ‘Regtech, Compliance and Technology Judgment Rule’. SSRN 
Scholarly Paper ID 3043021. Rochester, NY: Social Science Research Network. 
https://papers.ssrn.com/abstract=3043021. 
Penrod, Janice, Deborah Bray Preston, Richard E. Cain, and Michael T. Starks. 2003. ‘A 
Discussion of Chain Referral As a Method of Sampling Hard-to-Reach Populations’. 
Journal 
of 
Transcultural 
Nursing 
14 
(2): 
100–107. 
https://doi.org/10.1177/1043659602250614. 
Pettit, Stephen, and Anthony Beresford. 2009. ‘Critical Success Factors in the Context of 
Humanitarian Aid Supply Chains’. International Journal of Physical Distribution & 
Logistics Management 39 (6): 450–468. 
Phan, Phillip, Michael Wright, and Soo-Hoon Lee. 2017. ‘Of Robots, Artificial Intelligence, 
and 
Work’. 
Academy 
of 
Management 
Perspectives 
31 
(4): 
253–55. 
https://doi.org/10.5465/amp.2017.0199. 
Rogers, Everett M. 2003. Diffusion of Innovations, 5th Edition. 5th edition. New York: Free 
Press. 
Rowley, Jennifer. 2002. ‘Using Case Studies in Research’. Management Research News 25 
(1): 16–27. https://doi.org/10.1108/01409170210782990. 
Sharif, Mahmood, Sruti Bhagavatula, Lujo Bauer, and Michael K. Reiter. 2016. ‘Accessorize 
to a Crime: Real and Stealthy Attacks on State-of-the-Art Face Recognition’. In 
Proceedings of the 2016 ACM SIGSAC Conference on Computer and Communications 
Security, 
1528–1540. 
CCS 
’16. 
New 
York, 
NY, 
USA: 
ACM. 
https://doi.org/10.1145/2976749.2978392. 
Shaw, Michael J., and Andrew B. Whinston. 1989. ‘An Artificial Intelligence Approach to the 
Scheduling of Flexible Manufacturing Systems’. IIE Transactions 21 (2): 170–83. 
https://doi.org/10.1080/07408178908966221. 
Soja, Piotr. 2010. ‘Understanding Determinants of Enterprise System Adoption Success: 
Lessons Learned from Full-Scope Projects in Manufacturing Companies’. Production 
Planning & Control 21 (8): 736–50. https://doi.org/10.1080/09537281003601597. 
Susto, Gian Antonio, Andrea Schirru, Simone Pampuri, Seán Mc Loone, and Alessandro Beghi. 
2015. ‘Machine Learning for Predictive Maintenance: A Multiple Classifier Approach’. 
IEEE 
Transactions 
on 
Industrial 
Informatics 
11 
(3): 
812–20. 
https://doi.org/10.1109/TII.2014.2349359. 
Tansey, Oisín. 2007. ‘Process Tracing and Elite Interviewing: A Case for Non-Probability 
Sampling’. PS: Political Science & Politics 40 (04): 765–772.

---


### Page 37

Tegmark, Max. 2017. Life 3.0: Being Human in the Age of Artificial Intelligence. 01 edition. 
Penguin. 
Tornatzky, Louis G, Mitchell Fleischer, and Alok K Chakrabarti. 1990. The Processes of 
Technological Innovation. Lexington, Mass.: Lexington Books. 
Towill, D.R. 1997. ‘Successful Business Systems Engineering. I. The Systems Approach to 
Business 
Processes’. 
Engineering 
Management 
Journal 
7 
(1): 
55–64. 
https://doi.org/10.1049/em:19970109. 
Turing, Alan, Richard Braithwaite, Geoffrey Jefferson, and Max Newman. 2004. ‘Can 
Automatic Calculating Machines Be Said to Think?(1952)’. B. Jack Copeland, 487. 
Tushman, Michael L., Anna Kahn, Mary Elizabeth Porray, and Andy Binns. 2017. ‘Change 
Management Is Becoming Increasingly Data-Driven. Companies Aren’t Ready’. 
Harvard Business Review, 23 October 2017. https://hbr.org/2017/10/changemanagement-is-becoming-increasingly-data-driven-companies-arent-ready. 
Venkatesh, Viswanath, and Fred D. Davis. 2000. ‘A Theoretical Extension of the Technology 
Acceptance Model: Four Longitudinal Field Studies’. Management Science 46 (2): 
186–204. https://doi.org/10.1287/mnsc.46.2.186.11926. 
Venkatesh, Viswanath, Michael G. Morris, Gordon B. Davis, and Fred D. Davis. 2003. ‘User 
Acceptance of Information Technology: Toward a Unified View’. MIS Quarterly 27 
(3): 425–78. https://doi.org/10.2307/30036540. 
Wali, Ayoob A., S. G. Deshmukh, and A. D. Gupta. 2003. ‘Critical Success Factors of TQM: 
A Select Study of Indian Organizations’. Production Planning & Control 14 (1): 3–14. 
https://doi.org/10.1080/0953728021000034781. 
Wamba, Samuel Fosso, Angappa Gunasekaran, Mithu Bhattacharya, and Rameshwar Dubey. 
2016. ‘Determinants of RFID Adoption Intention by SMEs: An Empirical 
Investigation’. 
Production 
Planning 
& 
Control 
27 
(12): 
979–90. 
https://doi.org/10.1080/09537287.2016.1167981. 
Wilson, H. James, and Paul R. Daugherty. 2018. ‘Collaborative Intelligence: Humans and AI 
Are 
Joining 
Forces’. 
Harvard 
Business 
Review, 
1 
July 
2018. 
https://hbr.org/2018/07/collaborative-intelligence-humans-and-ai-are-joining-forces. 
World Economic Forum. 2019. ‘AI Governance: A Holistic Approach to Implement Ethics 
into AI’. World Economic Forum. https://www.weforum.org/whitepapers/aigovernance-a-holistic-approach-to-implement-ethics-into-ai/. 
Wuest, Thorsten, Daniel Weimer, Christopher Irgens, and Klaus-Dieter Thoben. 2016. 
‘Machine Learning in Manufacturing: Advantages, Challenges, and Applications’. 
Production 
& 
Manufacturing 
Research 
4 
(1): 
23–45. 
https://doi.org/10.1080/21693277.2016.1192517. 
Yin, Robert K. 2018. Case Study Research and Applications. Sixth edition. Los Angeles: 
SAGE Publications, Inc. 
Zhang, Cheng, and Jasbir Dhaliwal. 2009. ‘An Investigation of Resource-Based and 
Institutional Theoretic Factors in Technology Adoption for Operations and Supply 
Chain Management’. International Journal of Production Economics, Special Issue on 
Operations Strategy and Supply Chains Management, 120 (1): 252–69. 
https://doi.org/10.1016/j.ijpe.2008.07.023.

---


### Page 38

Figures 
 
Figure 1. Main AI techniques underpin operations 

Figure 2. Simple illustration of the black box decision making process

---


### Page 39

Tables 
Table 1: A summary of the four AI use cases at BT 
 
AI Use 
cases 
Use case 1: 
AI for field service 
operation 
optimisation 
Use case 2: 
AI for 
predictive 
detection of 
‘unhealthy’ line 
connections 
Use case 3: 
AI for 
peripatetic 
warehouse 
deployment 
Use case 4: 
AI for 
automated 
inventory 
replenishment 
supported by 
Io T 
Background Multiple AI 
techniques were 
deployed to optimise 
and automate field 
service operations at 
the national level 
Algorithm uses 
historical data to 
predict whether a 
landline for 
reconnection is 
healthy or not. 
Strategic mobile 
warehouse 
deployment in 
response to reduce 
travel time and 
improve Service 
level agreements 
(SLA) 
Operational level 
inventory 
replenishment 
(spares) using an 
AI based 
automated supply 
chain decision 
AI 
techniques 
Multi-objective 
genetic algorithms; 
Heuristic search 
algorithms; 
Machine 
learning/neural 
networks; 
Heuristic search & 
evolutionary 
algorithms 
A classification 
tree/ regression 
model 
combination 
predictive 
algorithm 
Heuristic based 
search technique 
named Genetic 
Algorithm (GA) 
A hybrid AIsimulation 
approach using 
Meta-heuristics 
AI category ML and optimization ML 
Optimization 
Optimization 
Level 
Strategic 
(forecasting), tactical 
(capacity planning) 
and operational level 
optimization (task 
scheduling) 
Operational 
Strategic 
Operational 
Objectives 
To optimise and 
automatedemand 
forecasting, network 
capacity planning 
and workforce 
scheduling 
 
To reduce 
customer 
complaints about 
faulty connections 
and automate 
decision making 
about incoming 
orders (either 
automatic 
connection or 
engineering visit). 
To select the best 
700 sites (i.e. 
exchanges) out of 
5000 possible 
exchanges as 
mobile 
warehouses 
supplying spare 
parts to field 
engineers 
To find the 
optimal solution 
to support the 
decision of which 
product and which 
spare volume 
should be 
replenished at 
which warehouse 
How 
long 
the 
AI 
application 
has 
been 
deployed 
about 20 years 
10 years 
5 years 
2 years

---


### Page 40

Table 2: Impact summary of the four AI use cases at BT 
 
AI Use cases 
Use case 1: 
AI for field service 
operation 
optimisation 
Use case 2: 
AI for 
predictive 
detection of 
‘unhealthy’ line 
connections 
Use case 3: 
AI for 
peripatetic 
warehouse 
deployment 
Use case 4: 
AI for 
automated 
inventory 
replenishment 
supported by 
Io T 
Tangible 
Impact on 
operational 
performance 
• Accuracy of 
planned task 
completions 
improved from 
80.3% (manual) to 
90.5%. 
• 3% increase in 
demand forecast 
accuracy, 
• 10% increase in 
resource 
productivity; 
• 17% in travel time 
reduction in some 
parts of the 
business, 
• Customer 
complaints 
reduced 50%, 
from 15% now 
to 7-8% 
• 3-5% travel 
time reduction 
• Significant 
Cost savings in 
terms of 
reduced 
deployment 
time, reduced 
travel time for 
engineers and 
increased SLAs 
• Reduction by 
43% of the 
penalty cost 
• 60% reduction 
in volume of 
misplaced 
items 
Intangible 
impact 
• Allowing planners to focus on bigger picture; 
• Supporting data-driven decision making; 
• Improving field engineers’ wellbeing.

---


### Page 41

Table 3: CSFs for AI deployment in operations 
Stages 
Development 
Deployment 
Post-deployment 
CSFs 
• Strategy 
formulation 
• Top management 
support 
• Stakeholder buyin 
• Sufficient inhouse expertise 
• Collaborative 
work between 
business, IT and 
analytics, and 
‘translators’ to 
bridge AI with 
business 
• Problem 
formulation 
• Data 
quality/integrity 
and availability 
• Stakeholder 
engagement 
• Training 
everyone who 
engages with the 
algorithms 
• Effective 
communications 
• ‘Explainable’ AI: 
transparency and 
fairness 
• AI Governance 
• Codifying the 
right AI logic into 
operations’ 
information 
system 
applications 
• Set of KPIs in 
place to monitor 
AI’s impact on 
operations 
performance 
• Regular review of 
the fitness of AI 
algorithms 
• Revising and 
modifying AI 
algorithms (if 
possible, with 
built-in options) 
when business 
changes 
• AI Ownership

---
