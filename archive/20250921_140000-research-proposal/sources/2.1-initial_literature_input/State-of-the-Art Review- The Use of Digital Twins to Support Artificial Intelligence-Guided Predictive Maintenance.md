

---

Page 1

---

State-of-the-Art Review: The Use of Digital
Twins to Support Artificial Intelligence-Guided
Predictive Maintenance⋆⋆⋆
Sizhe Ma1[0000−0002−2532−5915], Katherine A. Flanigan1[0000−0002−2454−5713],
and Mario Berg´es1[0000−0003−2948−9236] ⋆⋆⋆
1Civil and Environmental Engineering, Carnegie Mellon University, 5000 Forbes Ave,
PA 15213, USA
{sizhem,kflaniga,mberges}@andrew.cmu.edu
Abstract. In recent years, predictive maintenance (PMx) has risen to
prominence, capturing significant attention for its potential to enhance
efficiency, automation, accuracy, cost-effectiveness, and the reduction of
human involvement in the maintenance process. Importantly, PMx has
evolved in tandem with digital advancements, such as Big Data and
the Internet of Things (IOT). These technological strides have enabled
Artificial Intelligence (AI) to revolutionize PMx processes, with increas-
ing capacities for real-time automation of monitoring, analysis, and pre-
diction tasks. However, despite these leaps, PMx continues to grapple
with challenges——ranging from poor explainability and sample ineffi-
ciency in data-driven methods to high complexity in physics-based mod-
els——that stymie its broader adoption. In this context, this paper posits
that Digital Twins (DTs) hold the transformative potential to be seam-
lessly integrated into the PMx process as a means to surmount these lim-
itations, thereby laying the groundwork for more extensive and context-
sensitive automated PMx applications across varied stakeholders. Never-
theless, we contend that, at present, state-of-the-art DTs have not fully
matured to the extent required to bridge these existing gaps. Our paper
unfolds as a comprehensive roadmap for the evolution of DTs, geared
towards redressing current limitations and fostering the large-scale pro-
gression of automated PMx. We structure our approach in three dis-
tinct stages: initially, we reference our prior work where we methodically
identified and distinctly defined the Information Requirements (IRs) and
Functional Requirements (FRs) for PMx, which serve as the fundamental
blueprint for any ensuing unified framework. Subsequently, we embark
⋆This work has been submitted to Springer for possible publication. Copyright may
be transferred without notice, after which this version may no longer be accessible.
⋆⋆This material is based upon work supported by the U.S. Army Research Office and
the U.S. Army Futures Command under Contract No. W911NF-20-D-0002. The
content of the information does not necessarily reflect the position or the policy of
the government and no official endorsement should be inferred.
⋆⋆⋆Mario Berg´es holds concurrent appointments at Carnegie Mellon University (CMU)
and as an Amazon Scholar. This manuscript describes work at CMU and is not
associated with Amazon.
arXiv:2406.13117v1  [cs.AI]  19 Jun 2024


---

Page 2

---

2
S. Ma et al.
on an exhaustive literature review across various disciplines to ascertain
how DTs are presently being employed to integrate these previously iden-
tified IRs and FRs, and we also unveil extant standardized DT models
and tools that stand to fortify automated PMx initiatives. Lastly, we
spotlight the discernible gaps——in particular, those IRs and FRs that
current DT implementations have yet to fully support—and meticulously
delineate the components necessary for the realization of a comprehen-
sive, automated PMx system. The paper culminates with a synthesis of
our research directions, aimed at the seamless integration of DTs into
the PMx paradigm to actualize this ambitious vision.
1
Introduction
Effective maintenance is vital for the efficiency, safety, and longevity of systems
and their assets. Numerous strategies have been developed to enhance mainte-
nance processes, including Predictive Maintenance (PMx), Corrective Mainte-
nance (CM), Preventative Maintenance (PvM), and Total Productive Mainte-
nance [66]. Among these, PMx stands out as the most appropriate for scenar-
ios where avoiding run-to-failure is crucial, typical of many complex real-world
systems. PMx is a forward-looking maintenance strategy that leverages data
analysis, artificial intelligence (AI), and other advanced technologies to foresee
potential system failures and implement preventative measures. This approach
integrates real-time monitoring, data analytics, and historical data to anticipate
equipment failures before they occur, enabling maintenance teams to plan re-
pairs or replacements proactively. Previously, four primary levels of PMx have
been identified [32], each defined by distinct methodologies: Level 1: visual in-
spection, Level 2: instrument inspection, Level 3: real-time condition monitoring,
and Level 4: continuous monitoring coupled with predictive techniques.
In recent years, PMx has experienced significant advancements, presenting
new possibilities for improving system performance [89]. These developments
have been driven by the adoption and integration of advanced technologies such
as the Internet of Things (IoT), large-scale datasets, and increased computing
power [84]. The IoT, a network of interconnected devices equipped with sensors,
software, and internet connectivity, plays a pivotal role in this transformation. It
facilitates seamless data collection and exchange between systems and the inter-
net, reflecting the broader trend of technology integration in industrial processes
and engineered systems. The expanded availability of data has created new op-
portunities for PMx, as more information can now inform maintenance decisions.
Furthermore, PMx increasingly depends on complex algorithms and models ca-
pable of handling the vast amounts of data generated by IoT systems [89, 91].
With the advantage of growing computing resources, these algorithms support
near real-time monitoring, analysis, and prediction of system behavior. Together,
these technological advancements have led to more accurate predictions and have
enhanced the standard of maintenance decision-making capabilities.
Despite the significant progress in PMx, various challenges remain that hin-
der its full development and broader adoption. These challenges arise from the


---

Page 3

---

SOTA: AI-Guided PMx DT
3
complexities inherent in both data-driven and physics-based modeling techniques
crucial to PMx. Data-driven PMx encounters difficulties such as the scarcity of
failure data, as systems rarely operate until failure, complicating accurate failure
prediction [4, 113]. Moreover, current models often lack explainability, leading to
skepticism about the accuracy of algorithms and diminishing trust in the mod-
els’ decisions and recommendations [93]. Additionally, many PMx algorithms
are not sample-efficient, requiring extensive datasets to produce reliable results,
which is problematic given the infrequency of machine failures [113]. Conversely,
physics-based modeling techniques are characterized by their intractable com-
plexity, making them resource-intensive and demanding considerable expertise
to develop [2]. These models also tend to have limited generalizability, as they are
typically tailored to specific types of equipment [13]. To address these limitations,
hybrid approaches such as Physics-Informed Machine Learning (PIML), Scien-
tific Machine Learning (Sci-ML), and integrated hybrid models have emerged as
promising solutions [73, 90]. However, these methods, while effectively leverag-
ing sensor data, often incorporate only a portion of available physical knowledge
into the modeling process. For instance, PIML embeds physical rules as implicit
constraints within ANN models without comprehensive integration, underscor-
ing the evolving nature of these approaches and the necessity for further research
and development.
The current manuscript takes this discussion further. It seeks to build upon
the foundations established by our previous research [60], contextualizing each
requirement with tangible examples, exploring state-of-the-art literature indi-
vidually, and gleaning insights from industry standards and expert perspectives.
In this context, the present paper builds upon that foundation without redun-
dantly restating the selection procedure of manuscripts; instead, it focuses on
the identification of critical elements that constitute a computational framework
of DT. We delve into standardized DT models and environments that can facili-
tate the integration and implementation of PMx strategies. While we argue that
DTs have this transformative potential within the PMx space, state-of-the-art
DTs have not yet achieved a level of maturity and robustness that is requisite
for widespread industrial adoption. So, we further assess the current status of
individual manuscripts in terms of their fulfillment of the identified IRs and FRs,
thereby providing a more detailed and granular understanding of existing gaps.
This paper serves as a roadmap for DT developments that will address existing
shortcomings and support the advancement of automated PMx at scale.
A systematic approach comprising three primary stages, which is designed to
underscore the interaction between PMx and DT. We begin in Section 2 with a
presentation of the identified IRs and FRs from our previous work. These IRs and
FRs form the foundation for any unified PMx DT. We then move to Section 3,
where a comprehensive literature review is conducted to explore the current uti-
lization of DTs in incorporating these IRs and FRs. This section also details the
supporting DT models and environments, highlighting the existing standardized
DT tools that facilitate automated PMx tasks. The subsequent section, Sec-
tion 4, serves to connect the concepts discussed in the previous sections. Here,


---

Page 4

---

4
S. Ma et al.
we identify and scope the gaps, particularly those IRs and FRs not currently
supported by DTs. This critical analysis helps to pinpoint the missing elements
necessary for fully automated PMx. Finally, the chapter concludes in Section 5,
where we summarize the research agenda for expanding and integrating DTs
into the PMx process. This concluding section aims to chart a path forward for
realizing the vision of seamlessly blending PMx with DT technologies, thereby
enhancing the efficiency and efficacy of maintenance strategies.
2
Predictive Maintenance, Informational Requirements
and Functional Requirements
2.1
Predictive Maintenance and Related Strategies
Maintenance practices play a pivotal role in ensuring the safe, prolonged, and
economically viable use of equipment across diverse sectors. Over the past two
decades, the field has witnessed remarkable advancements, refining and enhanc-
ing the way industries approach equipment upkeep. At the core of these advance-
ments lie three predominant maintenance strategies: CM, PvM, and PMx.
Delving deeper, as depicted in Figure 1a:
– CM is reactive in nature, instigating maintenance actions only after a com-
ponent or system exhibits a fault. While it addresses immediate issues, this
approach can lead to unforeseen breakdowns.
– PvM operates on a calendar-based system, scheduling routine maintenance
checks and repairs. This proactive approach aims to preemptively mitigate
potential failures, but it may also inadvertently result in redundant checks
and wastage of resources.
– PMx is the most advanced among the three, predicting equipment failure by
estimating its forthcoming states. It recommends specific maintenance tasks
from a broad spectrum of choices, considering both resource accessibility and
economic implications.
Further elucidation on the economic implications of these strategies is pro-
vided in Figure 1b. The visualization highlights the comparison of the cost-
effectiveness of reactive repairs against preventive measures. Observably, while
CM might grapple with soaring replacement expenditures and secondary dam-
ages, PvM could inadvertently lead to superfluous repairs and resource depletion.
PMx masterfully bridges the gap, determining the most opportune moments for
maintenance interventions. Any divergence from this meticulously crafted sched-
ule could tip the balance, either causing resource wastage or amplifying the risk
of collateral damage [71].
2.2
Informational Requirements and Functional Requirements of
Predictive Maintenance
Traditionally, PMx harnesses granular insights about the system, such as real-
time operational parameters and configurations, to finetune its maintenance


---

Page 5

---

SOTA: AI-Guided PMx DT
5
(a)
(b)
Fig. 1: Comparison between different maintenance techniques with respect to
(a) the underlying mechanisms and (b) the economy [84].
agenda. This optimization predominantly relies on prognostic techniques to iden-
tify future usage profiles and the RUL of the equipment. With the contemporary
surge in computational prowess, ML algorithms have led to significant advance-
ments in AI-guided optimization for PMx. Their evolution has paved the way for
groundbreaking strides in AI-driven optimization techniques tailored for PMx.
Building on this foundation, it is pivotal to revisit the IRs and FRs we de-
lineated in our prior research [60]. Following the step of system and software
industry [53, 97], these systematically identified IRs and FRs provide a struc-
tured framework and critical blueprint, enabling the effective implementation
and optimization of PMx strategies within the evolving landscape of AI and
digital technology, as shown in Figure 2.
IRs:
1. Physical Properties: The spatial information and characteristics of an asset
or its components.
2. Reference Values: The benchmark for an asset or its components to fail.
3. Contextual Information: The data used to determine the current or future
states of a component or to make decisions and recommendations without
being directly derived from the physical entity being maintained.
4. Performance Metrics: The metrics that quantify the performance of opera-
tions of an asset or its components.
5. Historical Data: The maintenance records and usage profiles of an asset or
its components.
6. Faults: The anomalies, malfunctions, or failures of an asset or its components.
FRs:
1. Theory Awareness: The ability of the system to maintain efficient and con-
sistent representations of the physical phenomena involved in the assets’
operation [53].


---

Page 6

---

6
S. Ma et al.
2. Context Awareness: The ability of the system to perceive and adapt to var-
ious operational and environmental factors [28].
3. Interpretability: The ability of the system to generate human-interpretable
outputs [107].
4. Robustness: The ability of the system to maintain acceptable performance
under potential disturbances in both physical and digital domains [53].
5. Adaptivity: The ability of the system to modify its internal process or be-
haviors based on the deterioration or evolution of an asset [53].
6. Scalability: The ability of the system to maintain performance across a di-
verse range of workloads or to be extended to varying scales.
7. Transferability: The system’s capability to uphold its performance when de-
ployed on assets or conditions distinct from those on which it was initially
trained [53].
8. Uncertainty Awareness: The system’s ability to recognize and quantify un-
certainty inherent in its input, process modeled, and/or outputs.
Fig. 2: Overview of the identified IRs and FRs.


---

Page 7

---

SOTA: AI-Guided PMx DT
7
3
Digital Twins and Threads
3.1
Digital Twins
The concept of Digital Twins (DTs) initially emerged without a widely agreed-
upon definition, as various fields adapted the term to fit their unique applica-
tions. The term gained a more defined structure when Grieves offered a com-
prehensive description, defining DTs as “a set of virtual information constructs
that fully describes a potential or actual physical manufactured product from the
micro atomic level to the macro geometrical level” [31]. Figure 3 shows how these
elements operate with each other visually in the context of PMx.
Grieves’ seminal work further introduces two critical applications of DTs,
labeled as ‘Possibilities.’ The first concept focuses on integrating usage data
into the design phase, and the second, known as “front-running” a simulation
in real-time, aims to prevent unpredictable and undesirable outcomes. These
concepts have evolved into key elements of DT technology, commonly referred
to in academia and industry as ‘design-in-use’ and ‘what-if simulation.’
The evolution of these concepts highlights not just the increasing relevance
of DT technology but also the diverse ways in which DTs have been developed
and applied across various sectors. In the last five years, different industries
have adopted these visions to suit their needs. The aerospace and automotive
industries, for instance, have largely leveraged the ‘what-if simulation’ aspect
to meet their complex systems and safety requirements [24]. The manufacturing
sector, conversely, has leaned towards the ‘design-in-use’ model, using real-time
operational data to enhance manufacturing processes and product designs [37].
The Medical and Healthcare sectors have shown a balanced application of both
models, employing ‘what-if simulations’ for medical procedures and ‘design-in-
use’ for optimizing medical equipment and systems [33].
These two primary characteristics of DTs exemplify how their definitions and
functionalities are shaped by the varied expectations of stakeholders in different
fields. As new technologies emerge, the scope and potential of DTs have contin-
ued to grow, incorporating features like advanced visualization, interoperability,
and Human-System Interaction (HSI). This expansion leads to an even greater
divergence in the understanding and application of DTs.
3.2
Digital Threads
The term Digital Thread (DThread), in a PMx context, refers to the intercon-
nected flow (wired or wireless) and systematic integration of data across the
lifecycle of an asset or a system [52], as shown in Figure 3. This encompasses
the data generated from the design phase, operation phase, and maintenance
phase, facilitating a comprehensive understanding of the asset’s health and per-
formance. Conceptualizing DThreads can be aided by envisioning them as links
or threads, which weave together information such as sensor data, operational
data, maintenance records, inspection data, etc. Analogous to sewing threads,


---

Page 8

---

8
S. Ma et al.
Fig. 3: Digital Twin and Digital Thread used for Aviation-related PMx.
the continuity of DThreads is essential, as any break in these connections ob-
structs the seamless flow of data.
It is vital to distinguish between DThread and DT to avoid any miscon-
ception that may occur from mixing the two terms. DTs focus on creating the
virtual replica of a product that can mimic the behavior of the physical asset with
the help of high-fidelity simulations or data-driven methods, whereas DThreads
provide actionable information flow between physical and virtual assets bidirec-
tionally. Thus, DThread can be interpreted as the link including all the required
information to generate and supply updates to a DT [95]. It is worth highlighting
that DThread is neither DT nor part of DT, but rather an essential element of
DTF to realize DT. DT heavily relies on DThread to access and integrate data
from various sources and stages along the physical entities’ lifecycle. Without
a continuous flow of information, DT could not be kept up-to-date accurately,
thus merely a simulation model. While DThread is a prerequisite for DT, the
opposite does not hold, indicating that DThread can be operationalized inde-
pendently of a DTF [35]. DThread is used synonymously with connected supply
chain [52] and simplified information-relay frameworks [63]. However, it is un-
deniable that, in the absence of a virtual counterpart to the physical entity, the
information flow provided by DThread could not be effectively integrated for
high-level downstream tasks [94], such as optimization, and decision-making.
3.3
Digital Twin Frameworks
There have been multiple attempts at proposing a DTF as the solution for PMx
tasks [14, 76]. Depending on the assets they are considering for maintenance and
the PMx tasks applied, as well as the algorithms used to model the physical twin,
the DTF implemented varies significantly. In order not to mislead or confuse the
reader, we first present minimal viable components that a DTF should have so
as to pave a roadmap for further investigating the mapping between PMx and
DT on both general and individual levels. This list of components is inspired by
[52] and expanded by selected literature after the three-step process [60]. In the
meantime, an accompanying contextual example (italics) is provided in parallel.


---

Page 9

---

SOTA: AI-Guided PMx DT
9
The example considers creating a DT for the helicopter to aid the PMx process
aimed at maintaining the health of a helicopter’s tail rotor drive shaft (TRDS)
towards alignment and imbalance. DTFs from selected literature only have a
subset of components listed below, which has the potential to realize IRs and
FRs:
– Physical Twin (PT) - PTs are practical artifacts that could potentially cover
a wide range of applications (e.g., system, product, equipment). Without PT,
the DT is a conventional simulation model. Example: The TRDS itself.
– Physical Twin Environment (PTE) - Depending on the PT, PTE exists as
a set of measurable variables in which the PT lives. It provides contextual
information. Without PTE, the DT is an incomplete representation of the
PT. Example: The surrounding conditions that the helicopter operates in,
including the atmospheric pressure, humidity, and temperature.
– Digital Twin (DT) - A digital representation of the physical asset generated
by computers. From a functionality point of view, it could be viewed as an
integrated model that combines information models (e.g., geometry, material
configurations) and simulation engines (e.g., static models, dynamic models),
etc. From a solution point of view, it could utilize physics-based models, data-
driven models, or even expert-based models. Without DT, the PT lacks
an integrated information source to exchange data and perform analysis.
Example: The integration of information models like the geometry, operating
conditions, and health conditions (e.g., alignment, imbalance) of TRDS, and
dynamics model like finite element model based on vibration analysis.
– Digital Twin Environment (DTE) - The ‘virtual world’ in which the DT
exists. The practical use could be replicating PTE for different simulation
scenarios. Without DTE, what-if analyses are narrow, if not absent. Exam-
ple: The Digital representation (a matrix in its simplest form) of atmospheric
pressure, humidity, and temperature.
– Digital Environment (DE) - The platforms that sustain the functionality of
DTs. The actual selection depends on the exact rule and behavior to be mod-
eled. Without DE, the DT is merely a concept that remains unimplemented.
Example: Ansys Fluent1, due to its interoperability and scriptability.
– Instrumentation - The sensors, detectors, and other measurement tools, in-
cluding digitized manual inspection notes, periodically collect data from the
physical world. They are segments independent from PT or PTE that pro-
vides DT with information/knowledge of the two. Without instrumentation,
there is no data from PT to transmit to DT. Example: Accelerometers on
each drive shaft segment and meteorological sensors on the helicopter.
– Realization - The actuators or human resources, depending on the PT, peri-
odically realize actions/decisions generated from the digital world. They are
segments independent from PT or PTE that receives and actualize infor-
mation/knowledge generalized by the Analysis component. Without realiza-
tion, there is no action/decision from DT to be actualized on PT. Example:
1 Ansys
Mechanical
[website],
www.ansys.com/products/structures/ansys-
mechanical, (last accessed October 2022).


---

Page 10

---

10
S. Ma et al.
Human resources that realize the action generated by the system, such as
inspection or repair.
– Digital Thread (DThread) - The digital connection between PT and DT
allows bi-directional information flow between two twins. Without DThread,
there is no data exchange between different components in the DTF, and
the DT is no better than an analog model. Example: Data acquisition and
management software like LabVIEW2 plus IoT platforms or middleware like
Microsoft Azure IoT Suite3.
– Historical Repository (HR) - The storage system for the past usage patterns
and maintenance records of the PT. Unlike other components that form part
of the DT, HR exists as a separate entity. It captures and retains extensive
historical data that are not immediately discernible from examining the PT.
A pointer within the DT is created to indicate the location of the HR per-
tinent to a specific PT instance, allowing the HR to maintain an intimate
connection with the DT while retaining its distinct identity. Without HR,
there is no longitudinal analysis, and therefore, hinders the effective pre-
diction of future performance and potential issues. Example: Time-series
database like InfluxDB4 stores in a hard drive or cloud-based solution.
– Analysis Module - The module that analyses information from DT and gen-
erates alarms, recommendations, decisions, or actions in the PMx context.
In practical implementation, observe–orient–decide–act (OODA) could be
viewed as a representation of the analysis module. Without the analysis
module, the DT simply mimics the PT and is capable of simulation without
generating actionable information. Example: The OODA process for this ex-
ample would unfold as follows. First, the current state of the system, with
regard to its health and operation, is observed through a user interface. Next,
the observed states are oriented in relation to reference standards. A decision
is then made as to whether an inspection or repair is needed based on the
orientation stage. Finally, appropriate actions are taken in response to the
prior decision.
– Accountability Module - This component furnishes justifications for the
alerts, recommendations, decisions, or actions delivered by the Analysis mod-
ule. Periodic human review is required to ensure the validity of these out-
puts and to assess whether the Digital Twin or Analysis module necessitates
updates or retraining. Without the explanation module, attributing respon-
sibility (accountability) for unfavorable or even damaging results from the
system’s output becomes ambiguous. This lack of clarity can significantly un-
dermine user trust in the framework, thereby hindering its successful deploy-
ment. Example: SHAP method that elucidates the significance of vibrations
at various locations in the prediction of misalignment and imbalance.
2 LabVIEW [website], www.ni.com/en-us/shop/labview.html, (last accessed October
2022).
3 Microsoft Azure IoT Suite [website], azure.microsoft.com/en-us/products/iot-hub,
(last accessed November 2022).
4 InfluxDB [website], www.influxdata.com, (last accessed November 2022).


---

Page 11

---

SOTA: AI-Guided PMx DT
11
– Query & Response (QR) - QR accordingly accesses and gathers information
from the digital twin side. Without the functionality of QR, DT is merely
an integration of unorganized information without efficient ways to interact
with users. Example: Ansys Mechanical’s API that allows user to acquire
information or modify the settings of DT.
3.4
Standardized Models in Digital Twin and Standardized Digital
Environments
Following the list of critical components within DTF, the ensuing section con-
solidates and discusses the standard models and environments observed in the
literature, providing valuable insight into the foundational elements of the DT
concept. When certain models or environments are identified, examples from
unselected literature are also mentioned to offer readers more insights when im-
plementing their own DT while understanding the mapping between PMx and
DT. These discussions focus primarily on two key questions: what kind of models
can serve as a part of the DT, and which DE can effectively support these models.
The significance of discussing models in DT lies in their ability to capture and
simulate the complexities of physical systems. The choice of the model directly
impacts the accuracy and performance of the DTs and PMx tasks. Different sce-
narios and systems may require different kinds of models, be they physics-based,
data-driven, or even expert-based models. By examining and categorizing the
models, we offer a comprehensive view of the current landscape, informing future
design and development of DT in various PMx-related domains. The importance
of examining DE is underscored by their integral role in enabling the operation
and interaction of DTs. DEs are the computational platforms or ecosystems that
underpin the functionality of DTs. They can range from general-purpose com-
puting platforms, such as Amazon Web Services (AWS)5, to dedicated software
solutions, such as Ansys Twin Builder6, designed specifically to support com-
plex simulations, data analysis, and real-time interactions between the PTs and
DTs. While general-purpose computing platforms provide flexibility and broad
capabilities, dedicated software solutions can offer more immediate, out-of-the-
box value, and efficiency for the development and deployment of DTs. Given the
scale of PMx DT, only dedicated software solutions are discussed in the following
section.
Models in Digital Twin The models in DT are the models operating within
the virtual space to represent certain characteristics or properties of their PT.
Depending on the motivation and purpose of the task, the models being used
can be significantly different. However, thanks to the increase in computing
resources, one thing in common for most DTs in literature is the integration
5 Amazon Web Services [website], https://aws.amazon.com/, (last accessed November
2022).
6 Ansys Twin Builder [website], www.ansys.com/products/digital-twin/ansys-twin-
builder, (last accessed November 2022).


---

Page 12

---

12
S. Ma et al.
of multiple models focusing on different aspects of the physical twins. There
were multiple attempts to categorize these sub-models or elements that could
potentially be part of the DT [55, 82]. Before discussing actual models, we first
present a non-exhaustive classification of these elements and their projections
to IRs and FRs in Table 1. This act is crucial, because a non-exhaustive list,
while it may not capture every conceivable element, provides a valuable reference
and framework for understanding the breadth and complexity of the models
that may be included within a DT. This list serves as a foundational layer
to start the exploration of DT’s architecture and the various ways it can be
adapted to suit different tasks or objectives. Moreover, the classification of these
elements and their corresponding IRs and FRs enables a systematic analysis of
how different elements can contribute to the overall functionality of PMx DTs.
It provides a roadmap for understanding the interaction between these elements
and their influence on the system’s performance. In the meantime, accompanying
contextual examples (italics) are provided in parallel under the same example
mentioned in Section 3.3:
– Information Model: This model defines the geometric, topological and opera-
tional information of the physical entity (e.g., dimension, configuration). Ex-
ample: The computer-aided design (CAD) file of the helicopter or its TRDS.
– Static Rule Model: This type of model defines the physical rules/properties
that define the static (not time-dependent) input-output behavior of the as-
set or component. These models only consider the static rule of the physical
entity instead of the dynamic evolution/deterioration. Example: The finite
element model, representing the TRDS, ingests data from the load sensor
and consequently generates strain outputs.
– Dynamic Behavior Model: Like the preceding type, this model also defines
input-output behavior but as it relates to time. These models could include in
scope the evolution/deterioration under ideal circumstances or disturbances.
Behavior models are an essential factor for the simulation ability of DTs.
Example: The Hidden Markov model that models the change in the health
state of the TRDS over time.
– Tools for Integration: It describes the process that determines the inter-
actions between the aforementioned models, which plays a pivotal role in
the DTs, as it guarantees the functionality of the overall system. Example:
Snippets of code that define, based on the different operating status of the
helicopter and system (train or validation), how the outputs from the finite
element model are transferred to the Hidden Markov model.
The remaining section explores DT models, their strengths, and their limita-
tions individually. Examples are incorporated with each model to offer readers
more channels for extensive reading, as all examples lie within the intersection
of DT and PMx.
Point Cloud Modeling - Information Model: Point clouds are discrete
data sets representing 3D shapes or objects in space. They typically encompass
Cartesian coordinates, electrical responses, and asset textures. It is typically


---

Page 13

---

SOTA: AI-Guided PMx DT
13
Table 1: Mapping between different types of models and requirements.
Requirement
Identifier
information
Model
Static Rule
Model
Dynamic
Behavior
Model
Tools for
integration
IR1
x
x
x
IR2
x
x
x
IR3
x
IR4
x
x
x
IR5
x
x
IR6
x
FR1
x
x
FR2
x
x
FR3
x
x
FR4
x
x
x
FR5
x
x
x
FR6
x
x
x
FR7
x
x
x
FR8
x
x
used to capture larger, complex, and spatially distributed assets in PMx, such
as industrial equipment and facilities [96, 98] and transportation assets [118].
This typically involves the output of 3D scanners [121] or photogrammetry soft-
ware [68] during the inspection or monitoring phase, which often takes the form
of point clouds. The point cloud data and the derived 3D model are used in var-
ious level of PMx tasks, including anormaly detection and diagnosis [108, 115].
As critical components for capturing information about physical entities, point
clouds serve as a foundational modeling technique used for information modeling.
Point cloud modeling techniques can be classified based on various standards,
including the learning mechanism. For example, according to the learning mech-
anism, point cloud modeling techniques could be grouped into categories such
as non-learning, supervised learning, unsupervised learning, and reinforcement
learning [118]. One of the key strengths of point cloud modeling lies in its high
resolution. Furthermore, the raw data necessary for point cloud modeling is gen-
erally easy to collect. However, working with 3D point clouds also poses certain
challenges. For instance, raw point clouds demand data mining techniques to
transform them into an efficient and useful format suitable for point cloud mod-
eling [61]. Moreover, the practicality of the point cloud modeling process is a
critical concern. It must not only be less time-consuming but also offer higher
accuracy than manual processes [96]. Thus, while point cloud modeling is a pow-
erful tool for capturing and representing physical entities, it is not without its
challenges, especially when applied in the context of PMx DT.


---

Page 14

---

14
S. Ma et al.
Building Information Modeling (BIM) - Information Model: Re-
garded as a platform for generating precise and interoperable information mod-
els, BIM effectively represents the physical properties of a given structure. It is
typically used in the context of PMx for built environments or structures, like
buildings, infrastructures, and even cities [50, 58]. BIM models are typically cre-
ated during the design phase and further updated throughout construction phase
of a building or infrastructure project, making the models created via BIM typi-
cally exhibit richer semantics and a more organized structure. As BIM supports
a lifecycle perspective, enabling users to monitor and maintain an asset from
its inception through to its decommissioning, it could assist on a wider range of
PMx tasks than point clouds, such as decision-making and prognosis [36, 43].
However, the role BIM plays within DTF is relatively limited, primarily due to
its lack of data manipulation or predictive capabilities [77]. Another challenge
associated with BIM is related to entities that lack pre-existing BIM documenta-
tion. In such cases, the effort required to create and update a BIM model is often
disproportionate to the resultant output. This imbalance can present significant
obstacles to the practical implementation of BIM in these contexts [7, 50]. As a
result, the potential of BIM in the field of PMx DT may be hindered by these
inherent limitations.
Finite Element Method (FEM) - Rule Model and Behavior Model:
FEM represents a crucial branch within the sphere of Computer-Aided En-
gineering (CAE). It is especially noteworthy for its process of discretization,
which simplifies complex systems into manageable elements. This procedure is
particularly useful when dealing with irregular geometric shapes, heterogeneous
material properties, and complex boundary conditions, all of which often prove
unmanageable for analytical methods [122]. Rather than deriving and solving
equations as a whole, the components are divided into smaller parts, each gov-
erned by simpler equations. The solutions to these are subsequently combined
to yield the final results (e.g., dislocation in structural analysis, temperature
in heat transfer analysis, etc.). This makes FEM an ideal candidate for both
rule and behavior modeling of intricate structures in the context of PMx DT.
In static problems, FEM is used to determine the state of the system under a
specific set of conditions at a particular point in time [46]. In dynamic problems,
FEM can also be used when the state of the system changes over time due to
forces, heat transfer, etc. In these cases, FEM is used to determine the relation-
ship between states at different points in time [102]. FEM is commonly applied
to a wide variety of assets, such as structural components [47] and mechanical
systems [100]. Similar to CFD, the creation of the model typically occurs during
the design phase and operational phase. Particularly in the operational phase
to aid maintenance, The FEM could be used in various levels of PMx tasks,
including anomaly detection, diagnosis, and prognosis [100]. However, like many
other CAE approaches, FEM is not without its challenges. Notably, it grapples
with complexity when addressing sophisticated systems [46]. To tackle this issue,
reduced-order modeling is frequently employed in tandem with FEM in practical


---

Page 15

---

SOTA: AI-Guided PMx DT
15
DT contexts. This combination allows for the fulfillment of real-time operation
requirements, a crucial aspect of effective PMx strategies [39, 46]. However, the
application of such reduced-order models requires careful consideration of their
validity range and potential inaccuracies. As such, a thorough understanding of
the system and its nuances is essential for the successful implementation of FEM
in the PMx DT context.
Fuzzy Logic Modeling - Rule Model and Behavior Model: The ap-
plication of DT, especially within the context of PMx, is substantially driven
by the necessity to generate precise and adaptive input-output projections from
the data. Catering to this requirement, fuzzy logic modeling has been leveraged
as the static rule and dynamic behavior model of DT, due in large part to its
capabilities as a universal approximator [6]. Fuzzy logic modeling is frequently
applied in PMx scenarios involving assets that have complex or non-linear be-
havior, uncertainty, imprecision, or where data is ambiguous or incomplete, such
as automotive systems [104]. In the context of PMx, experts build a fuzzy logic
model based on the understanding of the system and its potential failure modes
during the design phase. The model is then updated during the operational
phase and used primarily during the maintenance phase. Due to the lack of tem-
poral information and confidence interval, fuzzy logic modeling is mainly used
for PMx tasks such as anomaly detection and fault diagnosis. Beyond its ap-
proximation abilities, fuzzy logic also offers the interpretability of input-output
projections. This characteristic fulfills a vital functional requirement mentioned
earlier in Section 2.2 [5]. Consequently, the interpretability of fuzzy logic models
aids in understanding the reasoning behind specific outputs, providing crucial
insights for decision-making. Despite its many benefits, the scalability of fuzzy
logic models may pose a limitation to their practical application. As the number
of inputs, outputs, and fuzzy sets grows, there is a corresponding exponential
growth in the number of rules and membership functions within a fuzzy logic
model [6]. This steep increase can complicate the model’s application, making it
a potential barrier to scalability in real-world settings.
Computational Fluid Dynamics (CFD) Modeling - Behavior Model:
CFD modeling constitutes another significant branch within the realm of Computer-
Aided Engineering (CAE). While the use of FEM may occasionally be part of
CFD modeling, commercial CFD packages typically employ Finite Volume Meth-
ods (FVM), as the convection term in fluid dynamics proves too computationally
demanding for FEM to handle effectively. Consequently, the forthcoming discus-
sion on CFD primarily revolves around the use of FVM. CFD is specifically
dedicated to analyzing and solving issues related to fluid flows through the ap-
plication of numerical analysis and data structures. The variables within the fluid
flow, such as mass and momentum, adhere to certain differential equations that
define dynamic behaviors, making CFD an indispensable modeling technique for
DTs involving fluid dynamics [78]. In the context of PMx, fluid dynamics mean
assets such as turbines, pipelines and pumps, and HVAC systems [20]. The cre-


---

Page 16

---

16
S. Ma et al.
ation of this dynamic behavior model typically occurs during the design phase
to support the design process and is subsequently utilized during the operational
phase to assist with maintenance tasks. The CFD modeling could be used in var-
ious levels of PMx tasks, including anomaly detection, diagnosis, and prognosis.
However, CFD modeling, like other CAE applications, is not without its draw-
backs. The primary challenge resides in the complexity involved in simulations
using differential equations, which often renders real-time responses unachiev-
able. This issue is particularly pronounced in the context of PMx DT, where
timely information and responses are essential. In practice, these challenges are
frequently mitigated by integrating ML techniques and reduced-order modeling.
These methods effectively cover a broad spectrum of operating conditions, by-
passing the need for brute-force simulations [8, 70].
Bayesian Network (BN) - Rule Model and Behavior Model: As a
probabilistic graphical model, BN serves as a vital tool for representing knowl-
edge and uncertainties within a modeling domain. In BNs, nodes stand for ran-
dom variables that can be either discrete or continuous, based on different dis-
tributions, while edges depict the conditional probability between two connected
variables [120]. In the context of a complex physical entity, uncertainties often
arise even when subsystems or components are clearly identified. This is espe-
cially true when defining rules or mechanisms that express system-level interac-
tions. In these situations, BNs can be used as static rule models and articulate
the propagation of uncertainty using a bottom-up approach facilitated by sim-
ulations or real-time data. By adding new edges between time steps, BNs can
be extended to dynamic behavior models known as Dynamic Bayesian Networks
(DBNs), enabling the expression of propagation over time and acting as a behav-
ior model within DTF [110]. For both two cases, BNs are utilized as a diagnostic
and prognostic tool in a wide variety of systems across different PMx-related
domains, such as industrial machinery [120] and automotive and aircraft sys-
tems [54], where uncertainty and model complex dependencies are presented.
BNs are typically formulated during the design and deployment phase to inform
and guide the design process, while the dependencies and uncertainties are up-
dated and refined throughout the operational phase to facilitate maintenance
strategies. Furthermore, BNs can effectively handle heterogeneous information
typically encountered in DT applications, including operational data, laboratory
data, reliability data, expert opinions, and mathematical models [12], making it
suitable for different levels of PMx tasks, such as diagnosis and prognosis. How-
ever, BNs are not without their challenges. Perhaps the most significant of these
is the lack of a universally acknowledged method for constructing networks from
data [54]. This issue can become particularly pronounced in the context of PMx,
where experts from each subsystem are often required to collaborate and iden-
tify the edges within the network. As the physical entity evolves or deteriorates
over time, these experts are needed continuously in close interaction, adding
or deleting edges. The need for constant expert intervention not only increases
the resource requirements but also potentially slows down the response times,


---

Page 17

---

SOTA: AI-Guided PMx DT
17
thereby reducing the effectiveness of the PMx operations.
The Gaussian Process (GP) - Behavior Model: In the realm of PMx
literature, GP stands as a recurrently utilized surrogate model. This stochastic
process is engineered to model a cluster of random variables, which are indexed
either temporally or spatially, operating on the principles of multivariate nor-
mal distribution. This similarity in function to BN enables GP to gather and
utilize heterogeneous data, thus making it a fitting model for the implemen-
tation of DT. However, GPs are often used to deal with assets where discrete
states or event dependencies are unclear, such as fatigue crack initiation and
growth [25]. In most cases, it models the dynamic behavior, as the assets change
continuously over time due to usage, wear and tear, environmental conditions,
maintenance activities, and other factors. In limited cases, GPs could be used
in a static setting to model the impact of different operational parameters (like
temperature, pressure, etc.) on the health of an asset. In literature, GPs are often
used to tackle diagnosis and prognosis tasks [16]. Unlike non-probabilistic ML
techniques, which are susceptible to overfitting when confronted with corrupted
data, GP exhibits an immunity to this phenomenon [16]. This advantage is inte-
gral in scenarios where data integrity might be compromised. Furthermore, GP
demonstrates commendable performance when dealing with datasets that are
not only limited in volume but are also inundated with noise. This capability
stems from its inherent ability to model uncertainties, making it exceptionally
beneficial in environments where data can be sparse or unreliable [49].
Other Surrogate Models: The development of DT involves the integra-
tion of a variety of models, a process during which complexity can become a
significant impediment to the real-time operation of DTF. This complexity is
particularly noticeable when integrating models with CAE, leading to the nat-
ural inclination to employ surrogate models as a means of enhancing efficiency.
In addition to the surrogate models detailed above, reduced-order models repre-
sent another commonly used class within the context of CAE-DT. These models
function by projecting the governing equations onto a subspace of reduced di-
mensionality, which can significantly accelerate the processing speed of rule and
behavior models [9, 47]. In the context of PMx, systems characterized by compu-
tationally intensive physical behaviors, yet necessitating real-time functionality,
are appropriate targets for the implementation of reduced-order models, such as
autonomous vehicle [62]. Reduced-order models display versatility across vari-
ous levels of PMx tasks, without particular restriction. Their applicability spans
from anomaly detection and diagnosis to prognosis, accommodating a wide range
of PMx functionalities. There are even models that provide transferable rule or
behavior basis, facilitating the application of surrogate models in different con-
texts [46]. However, surrogate models often come with limitations pertaining to
their validity range, a problem that is accentuated within the context of DT
[11]. Given that these models are typically constructed based on a limited span
of input data, their validity and accuracy may not extend beyond the range of


---

Page 18

---

18
S. Ma et al.
the training data. This poses a challenge when the DT is used for extrapolation
or prediction in scenarios outside the training range of the surrogate model. In
such instances, the generated results may be unreliable or even inaccurate, which
could potentially compromise the effectiveness and utility of the DT.
Digital Environments and Digital Tools DEs serves as the foundational
platforms that support the operation and functionality of DT, due to their abil-
ity to data and model integration and model execution. These software packages
harbor a variety of computational models and facilitate the crucial data ex-
change between PTs and DTs. Due to the inherent complexities and multifaceted
nature of DT and PMx, these environments or tools are often represented by
programming languages or software solutions that are proficient in simulating,
optimizing, and analyzing intricate dynamic systems. The choice of a specific
environment is typically dictated by the expected requirements of the DT. For
instance, some environments may be better suited for real-time data processing
and analytics, while others may excel in multi-domain modeling or large-scale
system simulations. As such, selecting an appropriate DE necessitates a compre-
hensive understanding of both the demands of the PMx task and the capabilities
of the potential DE. This ensures that the chosen environment not only caters
to the current needs of the DT but also possesses the flexibility and scalabil-
ity to accommodate future enhancements and modifications. In the subsequent
subsections of this document, we will delve deeper into exploring some of these
environments individually, with examples to illustrate their capabilities and ap-
plications in the context of PMx DT. This is by no means an exhaustive list
of DEs and digital tools used in the context of PMx, but it covers all of the
types that were found through our literature review. Furthermore, to provide a
succinct overview, Table 2, at the end of this section, serves as a summary of
the modeling capabilities, strengths, and limitations of each environment.
Standardized Digital Twin Environments/Tools:
OpenModelica (OM): As one of two the most common choices used in
PMx DTs, OpenModelica is a programming language that is capable of inte-
grating numerous models over various domains. Its objected-oriented design and
capability of modeling relationships between components make it ideal for the re-
lated information model [2]. Additionally, OpenModelica’s free and open-source
library offers both rule-based and behavior-based models across a wide range of
applications (e.g., hydraulics, mechanics, thermal), capable of fulfilling the need
of accurate current (e.g., diagnosis, replica) and future (e.g., prognosis, simula-
tion) estimation of a physical entity [27, 103]. OMEdit is often utilized in these
OpenModelica-Based implementations, as it provides a concise user interface
and interactive API to fulfill the integration of multiple models [3].


---

Page 19

---

SOTA: AI-Guided PMx DT
19
Simulink: As the other commonly used DE in PMx field, Simulink is a
MATLAB-based graphical programming environment that enables modeling,
simulating, and analyzing dynamic multi-domain systems. The designed physical
phenomenon can either be learned through data-driven methods or defined from
scratch [10]. For physics-based simulation models, most Simulink implementa-
tions use Simscape, a specialized tool in the Simulink environment for rule and
behavior modeling over mechanical, hydraulic, and electrical components[51].
Simscape connects components via ports that represent physical connections
and enables flexible integration over differing models and physical effects (e.g.,
friction, electrical losses, or temperature-dependent behavior) [106].
Ansys: As a finite-element modeling package, Ansys has risen to popular-
ity in the past few years due to its extensibility over its extensive software list.
Ansys itself is capable of providing elements resembling components of DTs.
Information Models can be designed or imported through general-purpose soft-
ware (e.g., Ansys SpaceClaim, Ansys Design Modeler) or specialized soft-
ware (e.g., Ansys BladeModeler) [23]. Rule or behavior models are captured
within Ansys Mechanical (e.g., structure, thermal), Ansys Fluent (e.g., hy-
draulics), Ansys Exalto (e.g., electromagnetics), etc [62, 79]. The majority of
Ansys software inherently possesses simulation capabilities, both predefined and
customizable, to accommodate different behavior or propagation laws. Concur-
rently, Ansys offers various software tools to facilitate the construction of DTF.
Ansys Twin Builder allows integrating models built in aforementioned soft-
ware and performing both component- and system-level simulation. In addition,
Twin Builder seamlessly merges embedded control software and human-machine
interface (HMI) design, thereby enabling the performance testing of embedded
controls in tandem with models of the physical system [82]. For more complex
system-level, multi-domain modeling of embedded software, Ansys SCADE is
used to integrate software control systems into a DT [62].
Unity3D: Originally developed for game designs, game engines, such as
Unity3D and Unreal Engine, are popular tools nowadays to create industry-level
simulations [85]. Although the environment might not be as accurate or realistic
as a specialized industry-level environment, they can be utilized to balance three
important features of DTs at the same time: built-in physics-engine simulation,
real-time operation, and realistic visualization [85]. Apart from these features,
Unity3D excels at creating engaging and interactive experiences. By incorporat-
ing interactivity into digital twins, users can directly interact with the virtual
environment to explore various scenarios, troubleshoot issues, or conduct train-
ing exercises. This improves the overall user experience and helps stakeholders
to better understand and manage their assets and systems.
Flexsim: Flexsim, at its core, is a simulation modeling software used to cre-
ate 3D models that represent the characteristics and properties of the physical
entity. Flexsim can utilize existing point clouds or BIM information to create


---

Page 20

---

20
S. Ma et al.
information models and bring the input data to life [48]. Discrete event simu-
lators, like Flexsim, do not follow high-fidelity rules and behavior models [123].
Instead, these simulators model the entirety of a whole facility (e.g., the shop
floor, production line) [80]. Simplified assumptions enable the simulation to run
at accelerated speeds. Additionally, Flexsim is capable of managing the integra-
tion between models by leveraging its built-in API, user-customized library, and
interactions between the two entities with embedded OPC Unified Architecture
ensuring high fidelity [57].
Revit: The building information modeling (BIM) software tool can provide
the information model for DTs. BIM is a process, meaning it could encompass
nearly all aspects, areas, and individual systems found within the physical entity,
making it a good choice for an accurate, centralized, and collaborated geometric
information source [44]. Revit could produce limited simulated behaviors, making
it capable of simulation in some PMx contexts (e.g., timetables, environmental
factors). Apart from Revit, other BIM software tools, such as ProStructures and
ArchiCAD, are also available and can create geographic models with the intrin-
sic characteristics of BIM.
Simpack: Instead of covering multiple types of models, Simpack puts concen-
trated focus on behavior models of mechanical systems [67]. With a user-defined
or data-learned behavior, Simpack is normally used for vibration or force simula-
tions in literature. Although it does not provide comprehensive types of models,
Simpack and its features are compatible with most environments that enable
multi-physics (e.g., OpenModelica, Simulink).
GeNIe Modeler: This Bayesian modeling environment implements influ-
ence diagrams and BNs to represent how humans reason with the interactions
between various sub-systems/structures at any given time, making this envi-
ronment a natural tool for Rule-based Modeling [64]. Furthermore, the GeNIe
Modeler can extend to include dynamic BNs and describe system changes in
discrete time without additional add-on packages. The DNBs can also be imple-
mented as a behavior model for simulation purposes.
3.5
Predictive Maintenance Digital Twin Literature
The following table includes an analysis of a portion of selected literature that we
used to synthesize DT Models and Environments (Section 3.4), and each work
is presented individually. Each row (work/works) has the following columns to
help guide the reader’s understanding: (1) Paper index - References to basic
information; (2) Main DT characteristics - Key feature of this DT implemen-
tation/deployment (3) DT description - Summary of its DT (4) DThread de-
scription - Summary of its data exchange process between DT and PT. In the
last column, we utilize the IRs and FRs identified in Section 2 to evaluate each


---

Page 21

---

SOTA: AI-Guided PMx DT
21
Table 2: Modeling Capability of Different Digital Environment/Tools.
Name
Information Rule Behavior Integration
OM
x
x
x
x
Simulink
x
x
x
x
Ansys
x
x
x
x
Unity 3D
x
x
x
Flexsim
x
x
Revit
x
x
Simpack
x
x
GM
x
DT solution and understand their capabilities and limits, thus exposing the gaps
which currently exist in the field in Section 4.


---

Page 22

---

22
S. Ma et al.
PMx DT Literature
Paper
Index
Field
Main
DT
characteris-
tics
(up
to
three)
DT description
DThreads description
Requirements Identified
[46]
Aviation
Knowledge-
embedded,
Simulation,
Replication
Component-based
reduced-order models
for the UAV, derived
from high-fidelity finite
element simulations,
representing pristine
and damaged states,
updated via
probabilistic graphical
model.
PT transmits sensor
data to DT; DT uses
component-based
reduced-order models
and optimal decision
trees to determine state
and updates PT with
relevant structural
information.
Information Requirements
IR1
IR2
IR3
IR4
IR5
IR6
x
x
x
x
x
x
Functional Requirements
FR1 FR2 FR3 FR4 FR5 FR6 FR7 FR8
x
x
x
x
x
[15]
Energy,
Utility
Simulation,
Replication,
System
Automation
‘Screenshot’ of the
equipment combining
state detection,
diagnosis, and prognosis
using a random
coefficient statistical
method and
Exponential
Degradation Model.
PT transmits sensor
data to DT for state
determination using
real-time monitoring
and the Exponential
Degradation Model; DT
returns prognostic
advice to PT.
Information Requirements
IR1
IR2
IR3
IR4
IR5
IR6
x
x
x
x
Functional Requirements
FR1 FR2 FR3 FR4 FR5 FR6 FR7 FR8
x
x
x


---

Page 23

---

SOTA: AI-Guided PMx DT
23
PMx DT Literature (Continued)
Paper
Index
Field
Main
DT
characteris-
tics
(up
to
three)
DT description
DThreads description
Requirements Identified
[21]
Energy,
Utility
Simulation,
Real-time
Monitoring,
Integrated
Information
Smart agents combining
physics-based prognosis,
data repository, and
communication
protocols with other
agents (e.g., Mediator
agents).
PT transmits real-time
data to DT to estimate
function parameters and
impending failure; DT
returns individual
maintenance decisions
or facilitates central
maintenance decisions
toward PT.
Information Requirements
IR1
IR2
IR3
IR4
IR5
IR6
x
x
x
x
x
Functional Requirements
FR1 FR2 FR3 FR4 FR5 FR6 FR7 FR8
x
x
x
x
[1]
Manufac-
turing
Knowledge-
embedded,
Simulation,
Integrated
Information
Integrated information
model combining a
kinetic model and
structural model,
equipped with virtual
sensors for real-time
monitoring and
degradation analysis.
PT transmits real-time
and degradation data to
DT for updating
predefined parameters;
DT provides future
modeling parameters to
prognosis module for
advice towards PT.
Information Requirements
IR1
IR2
IR3
IR4
IR5
IR6
x
x
x
x
x
Functional Requirements
FR1 FR2 FR3 FR4 FR5 FR6 FR7 FR8
x
x
x


---

Page 24

---

24
S. Ma et al.
PMx DT Literature (Continued)
Paper
Index
Field
Main
DT
characteris-
tics
(up
to
three)
DT description
DThreads description
Requirements Identified
[19]
Energy,
Utility
Simulation,
Replication,
System
Automation
Autoencoder
representing
equipment’s geometry
and configurations with
a low-dimensional
vector.
DT is trained with
simulation data; PT
data applies deep
transfer learning model
using DT parameters.
Information Requirements
IR1
IR2
IR3
IR4
IR5
IR6
x
x
x
Functional Requirements
FR1 FR2 FR3 FR4 FR5 FR6 FR7 FR8
x
x
x
[117]
Manufac-
turing
Simulation,
Real-time
Monitoring,
System
Automation
Representation of the
shop floor constructed
by virtual design and
manufacturing platform,
combining geometry,
material properties, and
physical behaviors with
virtual sensors.
PT transmits real-time
and degradation data to
DT for simulation,
providing repair advice
and acting as a ‘fault
dictionary’ for enhanced
diagnosis through a
parallel network.
Information Requirements
IR1
IR2
IR3
IR4
IR5
IR6
x
x
x
Functional Requirements
FR1 FR2 FR3 FR4 FR5 FR6 FR7 FR8
x
x
x


---

Page 25

---

SOTA: AI-Guided PMx DT
25
PMx DT Literature (Continued)
Paper
Index
Field
Main
DT
characteris-
tics
(up
to
three)
DT description
DThreads description
Requirements Identified
[119]
Aviation
Knowledge-
embedded,
Simulation,
Real-time
Monitoring
Integrated modules
including a geometric
model in CAD,
simulation models
constituted by FEM to
monitor cracks,
dynamic BN to monitor
system deterioration,
and data libraries.
Online: PT transmits
data to DT for
diagnosis, prognosis,
and updating data
library; Offline: DT uses
data and knowledge
library to perform
simulations as needed.
Information Requirements
IR1
IR2
IR3
IR4
IR5
IR6
x
x
x
x
x
Functional Requirements
FR1 FR2 FR3 FR4 FR5 FR6 FR7 FR8
x
x
x
x
x
[120]
Aviation Replica,
Simulation
BN where each node
represents a subsystem
(e.g., diffraction model,
aberration model) of
the physical entity.
PT transmits real-time
data to update and
predict DT; DT uses
this data to propagate
uncertainties and
calibrate the BN with
posterior probabilities,
providing maintenance
guidance to PT.
Information Requirements
IR1
IR2
IR3
IR4
IR5
IR6
x
x
x
x
x
Functional Requirements
FR1 FR2 FR3 FR4 FR5 FR6 FR7 FR8
x
x
x


---

Page 26

---

26
S. Ma et al.
PMx DT Literature (Continued)
Paper
Index
Field
Main
DT
characteris-
tics
(up
to
three)
DT description
DThreads description
Requirements Identified
[59]
Manufac-
turing
Simulation,
Replication,
Integrated
information
Multi-domain model
integrating subsystems
(e.g., spindle, controller)
with geometry, domain
knowledge (e.g.,
degradation
mechanisms), and
virtual sensors.
PT transmits real-time
data and boundary
conditions to DT for
synchronization and
simulation; DT
produces input for state
space model and output
system state for PT
maintenance.
Information Requirements
IR1
IR2
IR3
IR4
IR5
IR6
x
x
x
x
x
x
Functional Requirements
FR1 FR2 FR3 FR4 FR5 FR6 FR7 FR8
x
x
x
[65]
Energy,
Utility
Real-time
Monitoring,
System
Automation
Two stacked denoising
autoencoders
(Online/Offline)
transforming voltage
signal and experiment
parameters into RUL.
Online: PT transmits
data to DT to generate
RUL for PT
maintenance; Offline:
DT uses historical data
to train the
autoencoder, enabling
deep transfer learning
for online applications.
Information Requirements
IR1
IR2
IR3
IR4
IR5
IR6
x
x
x
Functional Requirements
FR1 FR2 FR3 FR4 FR5 FR6 FR7 FR8
x
x
x


---

Page 27

---

SOTA: AI-Guided PMx DT
27
PMx DT Literature (Continued)
Paper
Index
Field
Main
DT
characteris-
tics
(up
to
three)
DT description
DThreads description
Requirements Identified
[67]
Energy,
Utility
Simulation,
Replication,
Real-time
Monitoring
Set of vectors represents
the real-time drivetrain
torsional model based
on its corresponding
equation of motion.
PT uses the physical
updating strategy and
real-time data to track,
update, and predict the
DT; DT returns
simulation data (e.g.,
DT parameters) to PT
to facilitate
maintenance.
Information Requirements
IR1
IR2
IR3
IR4
IR5
IR6
x
x
x
x
x
Functional Requirements
FR1 FR2 FR3 FR4 FR5 FR6 FR7 FR8
x
x
x
x
[99]
Energy,
Utility
Knowledge-
embedded,
Replication,
Integrated
Information
Integrated model with
four components:
Geometry model
(CAD), physics model
(FEM), behavior model
(power generation
function), and rule
model (static
constraints).
PT transmits real-time
and degradation data to
create, calibrate, and
update DT based on the
phase of operation; DT
performs model
simulation for
consistency judgment
and maintenance
advice.
Information Requirements
IR1
IR2
IR3
IR4
IR5
IR6
x
x
x
x
x
x
Functional Requirements
FR1 FR2 FR3 FR4 FR5 FR6 FR7 FR8
x
x
x


---

Page 28

---

28
S. Ma et al.
PMx DT Literature (Continued)
Paper
Index
Field
Main
DT
characteris-
tics
(up
to
three)
DT description
DThreads description
Requirements Identified
[17]
Manufac-
turing
Knowledge-
embedded,
Simulation,
System
Automation
‘Snapshot’ of the
current process
situation, including
dimensional properties,
dominant frequency of
real-time signal, heat,
and humidity.
PT transmits
preprocessed data to
DT for state and factor
analysis to update DT
parameters; DT runs
‘what-if’ scenarios to
initiate the prognosis
process for PT.
Information Requirements
IR1
IR2
IR3
IR4
IR5
IR6
x
x
x
x
Functional Requirements
FR1 FR2 FR3 FR4 FR5 FR6 FR7 FR8
x
x
x
[56]
Energy,
Utility
Integrated
information,
Automatic
communica-
tions
between
entities
‘Snapshot’ of the
physical entity,
comprising an
integrated information
model with geometries,
working regimes, and
degradation patterns.
PT transmits real-time
features to DT as input
for embedded
algorithms (e.g.,
peer-to-peer modeling,
collaborative modeling);
DT produces inputs for
the decision module,
guiding PT
maintenance.
Information Requirements
IR1
IR2
IR3
IR4
IR5
IR6
x
x
x
x
x
Functional Requirements
FR1 FR2 FR3 FR4 FR5 FR6 FR7 FR8
x
x
x
x
x


---

Page 29

---

SOTA: AI-Guided PMx DT
29
PMx DT Literature (Continued)
Paper
Index
Field
Main
DT
characteris-
tics
(up
to
three)
DT description
DThreads description
Requirements Identified
[92]
Energy,
Utility
Knowledge-
embedded,
Simulation,
Real-time
Monitoring
Vector containing
transducer signals (e.g.,
temperature), used to
estimate critical internal
parameters with sliding
mode techniques.
PT transmits real-time
transducer data to
update DT; DT uses a
preset differential
equation to estimate
bearing friction factor
and coolant flow,
guiding maintenance.
Information Requirements
IR1
IR2
IR3
IR4
IR5
IR6
x
x
x
Functional Requirements
FR1 FR2 FR3 FR4 FR5 FR6 FR7 FR8
x
x
x
x
x
[109]
Manufac-
turing
Digital
Dashboard,
Replica
Integrated structure
with an intelligent
module that visualizes
and analyzes real-time
data, and a data module
that explains the inputs
and outputs of the
intelligent module.
PT produces real-time
data to be visualized in
DT dashboards to
uncover the real-time
condition of PT; DT
intelligent module
conducts simulations to
generate data for
evaluating PT.
Information Requirements
IR1
IR2
IR3
IR4
IR5
IR6
x
x
Functional Requirements
FR1 FR2 FR3 FR4 FR5 FR6 FR7 FR8
x


---

Page 30

---

30
S. Ma et al.
PMx DT Literature (Continued)
Paper
Index
Field
Main
DT
characteris-
tics
(up
to
three)
DT description
DThreads description
Requirements Identified
[114]
Manufac-
turing
Simulation,
Replication,
Integrated
Information
Integrated information
model including lifecycle
data, FE simulation,
geometry, material, and
process data.
With sensor data: PT
transmits data to DT
for validation and
prognosis; Without
sensor data: DT runs
‘what-if’ simulations to
generate data and
provide prognosis for
PT.
Information Requirements
IR1
IR2
IR3
IR4
IR5
IR6
x
x
x
Functional Requirements
FR1 FR2 FR3 FR4 FR5 FR6 FR7 FR8
x
x
x
[116]
Aviation
Simulation,
Real-time
Monitoring,
Visualization
Integrated information
model includes data
from multiple sources,
such as operational
data, service data, and
knowledge data.
Verification: DT is
simulated and compared
with PT to validate DT
effectiveness. Operation:
PT transmits real-time
data to DT to build a
high-fidelity information
source for prognosis
towards PT.
Information Requirements
IR1
IR2
IR3
IR4
IR5
IR6
x
x
x
x
Functional Requirements
FR1 FR2 FR3 FR4 FR5 FR6 FR7 FR8
x


---

Page 31

---

SOTA: AI-Guided PMx DT
31
PMx DT Literature (Continued)
Paper
Index
Field
Main
DT
characteris-
tics
(up
to
three)
DT description
DThreads description
Requirements Identified
[86,
105]
Aviation
Simulation,
Integrated
Information,
System
Automation
Central data model in
unified modeling
language, each element
represents a
sub-component of the
asset, defined by
disciplines, components,
and levels of detail (e.g.,
1D, 2D).
Service domain
communicates with DT
through the
administrative domain;
service domain
disciplines update or
acquire information
from DT via central
model API interfaces.
Information Requirements
IR1
IR2
IR3
IR4
IR5
IR6
x
x
x
x
Functional Requirements
FR1 FR2 FR3 FR4 FR5 FR6 FR7 FR8
x
x
x
x
x
x
[101]
Energy,
Utility
Replica
FEM model that
accurately represents
the real offshore
structure’s dynamic
behavior.
PT transmits real-time
data to update the DT
parameters; DT
provides an accurate
expansion of limited
sensors which can be
used to guide prognosis
towards PT.
Information Requirements
IR1
IR2
IR3
IR4
IR5
IR6
x
x
x
x
Functional Requirements
FR1 FR2 FR3 FR4 FR5 FR6 FR7 FR8
x
x
x


---

Page 32

---

32
S. Ma et al.
PMx DT Literature (Continued)
Paper
Index
Field
Main
DT
characteris-
tics
(up
to
three)
DT description
DThreads description
Requirements Identified
[69]
Manufac-
turing
Simulation
Real-time FEM model
that determines stresses,
strains, and loads at
numerous hot spots.
PT transmits real-time
data to solve the inverse
problem in DT; DT
outputs real-time
simulation results for
PT maintenance.
Information Requirements
IR1
IR2
IR3
IR4
IR5
IR6
x
x
x
Functional Requirements
FR1 FR2 FR3 FR4 FR5 FR6 FR7 FR8
x
x
[112]
Aviation
Integrated
information,
Replica
Integrated information
model with structure
geometry (e.g., 3D
model) including
material properties, load
conditions, degradation
observations, and failure
thresholds.
PT transmits real-time
strain data to DT,
which updates critical
fatigue crack locations;
DT uses historical data
and degradation
patterns to provide
prognosis inputs for PT
maintenance.
Information Requirements
IR1
IR2
IR3
IR4
IR5
IR6
x
x
x
x
x
Functional Requirements
FR1 FR2 FR3 FR4 FR5 FR6 FR7 FR8
x
x
x
x


---

Page 33

---

SOTA: AI-Guided PMx DT
33
PMx DT Literature (Continued)
Paper
Index
Field
Main
DT
characteris-
tics
(up
to
three)
DT description
DThreads description
Requirements Identified
[88]
Manufac-
turing
Integrated
information,
Real-time
Monitoring,
Digital
Dashboard
Virtual machine
composed of multiple
modules, including a
simulation module,
signal processing
module, and machine
learning algorithms.
PT transmits sensor
measurements to
update the information
model in DT; DT
performs simulations of
the operations being
carried out in PT.
Information Requirements
IR1
IR2
IR3
IR4
IR5
IR6
x
x
x
x
x
x
Functional Requirements
FR1 FR2 FR3 FR4 FR5 FR6 FR7 FR8
x
x
[38]
Energy,
Utility
Real-time
Monitoring
Integrated informational
model includes
Industrial Foundation
Classes (IFC) data,
Construction
Operations Building
Information Exchange
(COBie) data, and an
ontology graph.
PT transmits sensor
data to update
information models; DT
provides necessary
information and
metadata, such as Brick
Schema, to fault
classifier and
maintenance planner for
PT.
Information Requirements
IR1
IR2
IR3
IR4
IR5
IR6
x
x
x
x
x
x
Functional Requirements
FR1 FR2 FR3 FR4 FR5 FR6 FR7 FR8
x
x
x


---

Page 34

---

34
S. Ma et al.
PMx DT Literature (Continued)
Paper
Index
Field
Main
DT
characteris-
tics
(up
to
three)
DT description
DThreads description
Requirements Identified
[54]
Aviation
Integrated
Information,
Replica,
Simulation
FEM model without
actual crack geometry
and DBN modeling
random variables to
estimate crack
propagation.
PT transfers real-time
data to DT, enabling
uncertainties to
propagate through time;
DT uses this data to
calibrate the BN with
posterior probabilities,
updating crack
propagation estimates .
Information Requirements
IR1
IR2
IR3
IR4
IR5
IR6
x
x
x
x
Functional Requirements
FR1 FR2 FR3 FR4 FR5 FR6 FR7 FR8
x
x
x
x
x
x


---

Page 35

---

SOTA: AI-Guided PMx DT
35
4
Gaps
Sections 2 and 3 serve as crucial cornerstones for this section. The deep-rooted
understanding of these requirements and their effective mapping to DT and
DThread have been instrumental in delineating gaps and research questions
that need to be addressed before fully harnessing DT’s potential in this field,
thereby ensuring that our work is situated within a well-defined and substanti-
ated research space. In the subsequent sections, we identify each of these gaps
and explore their implications.
4.1
Standardized Requirements
– RQ1.1: How can the standard-setting organizations and indepen-
dent contributions be synergized towards the development of a
unified standard of PMx-related DTF?
Explanation: The adoption and reproducibility of DT and DTF across AI-
guided PMx necessitate standardization of information and functional re-
quirements. There is a certain urgency to this process, as attempts to stan-
dardize PMx and DTs individually have been made, but a unified, industry-
wide standard has not yet emerged. Apart from the aforementioned PMx
standards in section 2.1, numerous organizations and independent entities
have put forward proposals for developing standards for DTs and DTFs.
These organizations include notable standard-setting organizations such as
ISO [40], the National Institute of Standards and Technology (NIST) [74],
the Internet Engineering Task Force (IETF) [41], and the Industry IoT Con-
sortium (IIC) [34]. There have also been independent contributions that have
made strides in the space, such as proposing a classification scheme for DT
and IoT standards to scrutinize the overlap between DT and IoT standards
[42]. Given the fact that each of these efforts focused on one or a few rela-
tively narrow aspects of PMx DT, there is a need for research that explores
how these individual efforts can be synergized. Understanding how to align
these independent contributions can facilitate the development of a unified
standard that caters to a broad range of scenarios and requirements.
– RQ1.2: What are the potential challenges and solutions in devel-
oping a standard that can accommodate the diverse applications
of PMx-related DTF?
Explanation: PMx is distinctively characterized by a wide range of asset
uniformity across diverse applications [60]. However, this trait also presents
a hurdle in the development of a unified standard, considering the diver-
sity of DTs utilized in PMx. As illustrated in Table 3.5, these DTs are often
custom-crafted for highly specific applications, each adhering to unique rules,
behaviors, and objectives. This customization could potentially impede the
development of a unified DT framework within the PMx landscape, simi-
lar to the manufacturing landscape [45]. This presents an opportunity to
investigate the potential challenges in developing a standard that can ac-
commodate such diverse scenarios. Moreover, proposing potential solutions


---

Page 36

---

36
S. Ma et al.
to these challenges could significantly contribute to the formation of a unified
standard, thus boosting the adoption and effectiveness of DT across different
PMx scenarios.
– RQ1.3: How would the establishment of a standard for PMx DT
facilitate the field towards an automated and efficient PMx pro-
cess?
Explanation: The establishment of a unified standard for PMx DT has the
potential to make significant contributions to the field. Not only could it
facilitate the adoption of DT across diverse PMx scenarios, but it could also
guide the field toward more automated and efficient PMx processes [26, 52].
Given the benefits, there is a need for research to investigate how exactly
a unified standard could streamline the PMx process. Understanding this
could provide valuable insights towards two of the top-priority issues related
to automation, which are “levels of automation” and “interfaces to automa-
tion” [75].
4.2
Ethical Issues
– RQ2.1: How can PMx DT’s capacity to serve as comprehensive
sources of information be balanced with the need for privacy?
Explanation: One of the defining features of DTs is their capacity to serve
as comprehensive sources of information. Consequently, DTFs encompass
an array of mechanisms, including data exchange, processing, and analysis
that occur within interactions among humans, physical entities, and digital
environments. In practical terms, this data is gleaned from multiple sources
and subjected to analysis. The information held within a DT might be con-
tributed by and shared among the parent company, partners, and customers
[72]. In a PMx context, for example, aviation data could potentially reveal
sensing information and operational pattern; HVAC data could potentially
reveal sensitive information about business operations in commercial settings
and about occupants’ daily routines in residential settings. This necessitates
a heightened focus on privacy, particularly in industries handling sensitive
data. Accordingly, PMx DT developers must incorporate appropriate secu-
rity measures and privacy protocols to address these ethical considerations,
meaning it is essential not only to incorporate a mechanism for identity con-
firmation of physical entities but also to establish a verification procedure
for digital interactions and machine-to-machine transmissions [83].
– RQ2.2: What countermeasures can be developed and integrated
into the DT systems to mitigate cyber-attacks aiming at data in-
tegrity in IoT devices, gateways, and the DT itself?
Explanation: Assets related to PMx are often subjected to high failure
costs and collateral damage, as mentioned in section 2.1. In the meantime,
DThread, as a critical component of DTF, allows decisions driven by data
to be harmoniously integrated with DT within the operational environment.
Given DTF’s inherent cyber-physical attributes, PMx is exposed to poten-
tial cyber-attacks, which could adversely impact the system, the products,


---

Page 37

---

SOTA: AI-Guided PMx DT
37
causing catastrophic events. For instance, integrity attacks targeting physical
hardware and sensors could result in the upload of deceptive sensor readings
[83]. This could lead to erroneous learning processes in models concerning
degradation. As such, the effective and swift identification of cyber-attacks
becomes an essential prerequisite for the successful deployment and security
of high-performing PMx DT. Moreover, proposing and validating counter-
measures could further reduce the impact of attacks.
4.3
Integrated Simulation Engines
– RQ3.1: What are the advantages and disadvantages of using differ-
ent types of models, such as data-driven and physics-based models,
in the construction of PMx DT, and how can these models be ef-
fectively combined for better performance?
Explanation: The construction of PMx DT typically requires models that can
accurately represent physical entities according to static and dynamic laws.
Both data-driven models and physics-based models have been employed for
this purpose, each with its unique advantages and drawbacks [18, 87]. While
physics-based models provide stable and high-fidelity representations, they
are computationally intensive and not well-suited for real-time analysis. On
the other hand, data-driven models derive rules from data and avoid compu-
tational complexity, yet their lack of accountability can limit their industrial
use [29]. Given these considerations, understanding how these different types
of models can be effectively integrated for constructing PMx DT is a research
question that needs further investigation.
– RQ3.2: How can integrated simulators be utilized in PMx DT to
explicitly define, learn, and update rules or laws, and what im-
pact would this have on fulfilling the information and functional
requirements?
Explanation: Despite the advantages of combining different models in con-
structing PMx DT, it’s observed that the use of this approach often results
in the implicit utilization of knowledge without a guarantee of consistent
physical representation [30]. There are suggestions that integrated simula-
tors, which explicitly define, learn and update rules or laws, could effectively
address this issue and fulfill the functional and information requirements of
DTs supporting PMx. However, more research is needed to understand the
potential and application of integrated simulators.
4.4
Explainable Simulators and Decision Models
– RQ4.1: How can model-agnostic methods be used to provide local
explanations of simulators and decision models in PMx DT, and
what are the potential benefits of this approach in terms of flexi-
bility, adaptability, and addressing ethical issues?
Explanation: Local interpretability holds paramount importance in the PMx
context, as mentioned in section 2, especially concerning high-value assets, as


---

Page 38

---

38
S. Ma et al.
it facilitates clarifying and distributing responsibilities among various teams
involved. For instance, in the event of an error in a DT’s recommended
decision, the ability to explain the origin of such a mishap and identify
the responsible party is critical. Some studies in PMx DT literature have
begun to include interpretability as a desirable feature, opting for intrinsi-
cally interpretable models/techniques to ensure accountability. Such mod-
els typically boast simpler structures designed for human comprehension,
allowing them to justify their decisions independently, examples of which
include short Decision Trees, sparse linear models, and Bayesian Networks
[47, 54, 120]. However, a trade-off often exists between model interpretabil-
ity and predictive performance; intrinsically interpretable models may not
rival the accuracy of complex models in practical PMx scenarios. Conversely,
model-agnostic methods, which provide post-hoc explanations of simulators
and decision models, possess inherent advantages beyond flexibility. These
methods can address ethical issues highlighted in section 4.2, as they can
elucidate models retrospectively without accessing original data. Addition-
ally, their flexibility and adaptability expand the range of available options
for simulators/decision models. However, there is a limited understanding of
how these methods can be effectively used in PMx DT.
4.5
Scalable Digital Twin Framework
– RQ5.1: What are the advantages and limitations of deploying PMx
DT in edge devices compared to centralized deployment?
Explanation: Investigating the advantages and limitations of deploying PMx
DTs in edge devices compared to centralized deployment is crucial due to
the distinctive characteristics each offers [21]. Centralized deployment can
handle extensive data and complex models with its robust computational
resources but may incur latency issues. Conversely, edge deployment offers
lower latency by processing data locally, though it may be constrained by
the devices’ computational capabilities. Hence, understanding these trade-
offs is essential in formulating efficient deployment strategies for PMx DTs
to optimize maintenance outcomes and overall system performance.
– RQ5.2: How can edge deployment of DTF in PMx be made more
efficient, especially when computational resources are limited?
Explanation: As mentioned in section 2, instances of ”scale-down” are rarely
encountered and are primarily addressed from an application standpoint
at the theoretical level. Nevertheless, edge deployment remains a prevalent
practice in PMx DT [21]. For instance, a DTF for aviation-related PMx on a
fleet may be deployed either remotely from assets or individually on board.
The latter approach offers benefits, provided the individual assets have ade-
quate computational resources, as it minimizes delays resulting from signal
transmission between the edge-deployed system and the central computa-
tional setup. This reduction in delay becomes increasingly important for
PMx tasks demanding rapid decision-making or synchronization among en-
tities [22]. Simultaneously, edge deployment offers a fitting scenario to ensure


---

Page 39

---

SOTA: AI-Guided PMx DT
39
privacy through federated learning [111], as mentioned earlier in 4.2, thereby
facilitating privacy and transparency. However, the challenge remains in
leveraging AI with computational strategies to circumvent the limitations
imposed by energy and equipment resources within the edge environment.
4.6
Robust Data Pipeline
– RQ6.1: How can the robustness and reliability of the data pipeline
in PMx DT be enhanced to ensure practical deployment?
Explanation: The robustness and reliability of DT are fundamental for prac-
tical deployment [81]. While there are some preliminary implementations
exploring robust DT, the advent of Industry 4.0 requires a higher level of
robustness in the data pipeline for full-scale implementation. In developing
a DT of a sophisticated real-world system, it is crucial to ensure the data
pipeline’s consistency across various sub-spaces, each with unique environ-
ments and software. Local errors within a sub-space could potentially com-
promise the entire pipeline or even the framework. Nonetheless, discussions
about enhancing data pipeline robustness, either through intricate architec-
ture design or cutting-edge AI technology, remain sparse in the DT literature.
Consequently, a robust mechanism or structure for the data pipeline would
significantly contribute to the development of PMx DT and DTs themselves.
4.7
Adaptive and transferable Digital Twin Framework
– RQ7.1: How can a bidirectional model library be implemented
within the Digital Twin framework, and what are the potential
benefits of this approach in terms of robustness, adaptability, and
transferability?
Establishing a library to store models is a novel approach in PMx DT,
aiming to expedite diagnosis or prognosis [46]. The constituents of these
libraries are referenced models, which can metaphorically be perceived as
hyperplanes in a high-dimensional space. A model, trained in real-time, is
contrasted with these hyperplanes with respect to distance to signify the
assets’ status. However, this uni-directional approach overlooks the connec-
tions between the referenced instance, the deteriorating instance, or other
possible instances. The proposition of a bidirectional library, which provides
feedback to the DT, particularly in circumstances of extrapolation, concept
drift, or domain adaptation, is not yet fully investigated. The implementa-
tion of such a bidirectional system could potentially propose a more versa-
tile approach, encouraging a two-way information flow and amplifying the
robustness, adaptability, and transferability of DTF across diverse scenarios
and domains.
5
Conclusions
This paper sets the stage for PMx DT and creates a roadmap for future research
on this topic by identifying several existing gaps in order to transfer PMx DT


---

Page 40

---

40
S. Ma et al.
from a novel and research-level topic to an industry-level solution. First, IRs
and FRs of PMx tasks based on a comprehensive review of PMx research stud-
ies are presented. Such requirements provided a solid foundation, not only for
researchers working on PMx DT, but also for practitioners and decision-makers
working in the PMx field. It could assist them in designing a new PMx system
from scratch, understanding the current system status, and gaining perspectives
on future PMx system developments. Next, based on certain selection criteria,
we summarized and categorized DT frameworks, standardized DT models and
environments used in research, and their connections with the identified IRs and
FRs. Based on the applications, models, and environments, this step could help
researchers to gain valuable insights when building DT and DTF architectures.
Additionally, we presented a portion of selected works with respect to applica-
tions, DT descriptions, DThread descriptions, etc., to provide the readers with
the context for further endeavors. Finally, by analyzing the mappings between
the requirements of PMx task and DT solutions in literature, knowledge gaps
are identified in the development and transition of PMx DT.


---

Page 41

---

Bibliography
[1] Aivaliotis, P., Arkouli, Z., Georgoulias, K., Makris, S.: Degradation curves
integration in physics-based models: Towards the predictive maintenance
of industrial robots. Rob. Comput. Integr. Manuf. 71, 102177 (2021).
https://doi.org/10.1016/j.rcim.2021.102177
[2] Aivaliotis, P., Georgoulias, K., Arkouli, Z., Makris, S.: Methodol-
ogy
for
enabling
digital
twin
using
advanced
physics-based
mod-
elling in predictive maintenance. Procedia CIRP 81, 417–422 (2019).
https://doi.org/10.1016/j.procir.2019.03.072
[3] Aivaliotis,
P.,
Georgoulias,
K.,
Chryssolouris,
G.:
The
use
of
Digital
Twin
for
predictive
maintenance
in
manufactur-
ing.
Int.
J.
Comput.
Integr.
Manuf.
32(11),
1067–1080
(2019).
https://doi.org/10.1080/0951192X.2019.1686173
[4] Alimohammadi,
H.,
Vassiljeva,
K.,
Petlenkov,
E.,
Mall
Kull,
T.,
Thalfeldt,
M.:
Predict
the
remaining
useful
life
in
HVAC
fil-
ters
using
a
hybrid
strategy.
CLIMA
2022
Conf.
(May
2022).
https://doi.org/10.34641/clima.2022.273
[5] Antonelli, M., Ducange, P., Marcelloni, F., Segatori, A.: On the influence
of feature selection in fuzzy rule-based regression model generation. Inf.
Sci. 329, 649–669 (2016). https://doi.org/10.1016/j.ins.2015.09.045
[6] Alves de Araujo Junior, C.A., Mauricio Villanueva, J.M., Almeida,
R.J.S.d., Azevedo de Medeiros, I.E.: Digital Twins of the Water Cool-
ing System in a Power Plant Based on Fuzzy Logic. Sens. 21(20), 6737
(2021). https://doi.org/10.3390/s21206737
[7] Arayici,
Y.:
Towards
building
information
modelling
for
ex-
isting
structures.
Struct.
Surv.
26,
210–222
(07
2008).
https://doi.org/10.1108/02630800810887108
[8] Aversano,
G.,
Bellemans,
A.,
Li,
Z.,
Coussement,
A.,
Gicquel,
O.,
Parente,
A.:
Application
of
reduced-order
models
based
on
PCA
&
Kriging
for
the
development
of
digital
twins
of
react-
ing flow applications. Comput. & Chem. Eng. 121, 422–441 (2019).
https://doi.org/10.1016/j.compchemeng.2018.09.022
[9] Aversano, G., Ferrarotti, M., Parente, A.: Digital twin of a combustion fur-
nace operating in flameless conditions: reduced-order model development
from CFD simulations. Proc. Combust. Inst. 38(4), 5373–5381 (2021).
https://doi.org/10.1016/j.proci.2020.06.045
[10] Balderas, D., Ortiz, A., M´endez, E., Ponce, P., Molina, A.: Empowering
Digital Twin for Industry 4.0 using metaheuristic optimization algorithms:
case study PCB drilling optimization. Int. J. Adv. Manuf. Technol. 113(5),
1295–1306 (2021). https://doi.org/10.1007/s00170-021-06649-8
[11] B´ark´anyi, ´A., Chovan, T., Nemeth, S., Abonyi, J.: Modelling for digital
twins—potential role of surrogate models. Processes 9(3),
476 (2021).
https://doi.org/10.3390/pr9030476


---

Page 42

---

42
S. Ma et al.
[12] Bartram, G., Mahadevan, S.: Integration of heterogeneous information
in SHM models. Struct. Control Health Monit. 21(3), 403–422 (2014).
https://doi.org/10.1002/stc.1572
[13] Boje, C., Guerriero, A., Kubicki, S., Rezgui, Y.: Towards a semantic con-
struction digital twin: Directions for future research. Autom. Constr. 114,
103179 (2020). https://doi.org/10.1016/j.autcon.2020.103179
[14] Bot´ın-Sanabria, D.M., Mihaita, A.S., Peimbert-Garc´ıa, R.E., Ram´ırez-
Moreno, M.A., Ram´ırez-Mendoza, R.A., Lozoya-Santos, J.d.J.: Digital
twin technology challenges and applications: A comprehensive review. Re-
mote Sens. 14(6), 1335 (Mar 2022). https://doi.org/10.3390/rs14061335
[15] Cattaneo,
L.,
Macchi,
M.:
A
Digital
Twin
Proof
of
Concept
to
Support
Machine
Prognostics
with
Low
Availability
of
Run-
To-Failure
Data.
IFAC-PapersOnLine
52(10),
37–42
(2019).
https://doi.org/10.1016/j.ifacol.2019.10.016
[16] Chakraborty, S., Adhikari, S., Ganguli, R.: The role of surrogate models in
the development of digital twins of dynamic systems. Appl. Math. Modell.
90, 662–681 (2021). https://doi.org/10.1016/j.apm.2020.09.037
[17] Cohen, Y., Singer, G.: A smart process controller framework for
industry
4.0
settings.
J.
Intell.
Manuf.
32(7),
1975–1995
(2021).
https://doi.org/10.1007/s10845-021-01748-5
[18] Coraddu, A., Oneto, L., Baldi, F., Cipollini, F., Atlar, M., Savio,
S.:
Data-driven
ship
digital
twin
for
estimating
the
speed
loss
caused
by
the
marine
fouling.
Ocean
Eng.
186,
106063
(2019).
https://doi.org/10.1016/j.oceaneng.2019.05.045
[19] Deebak, B.D., Al-Turjman, F.: Digital-twin assisted: Fault diagnosis using
deep transfer learning for machining tool condition. Int. J. Intell. Syst.
37(12), 10289–10316 (2022). https://doi.org/10.1002/int.22493
[20] Deng, M., Menassa, C.C., Kamat, V.R.: From BIM to digital twins:
a systematic review of the evolution of intelligent building representa-
tions in the AEC-FM industry. J. Inf. Technol. Construct. 26 (2021).
https://doi.org/10.36680/j.itcon.2021.005
[21] Dhada, M., Hern´andez, M.P., Salvador Palau, A., Parlikad, A.K.: Com-
parison of Agent Deployment Strategies for Collaborative Prognosis.
In: 2021 IEEE Int. Conf. Progn. Health Manage. pp. 1–8 (2021).
https://doi.org/10.1109/ICPHM51084.2021.9486628
[22] Dong, R., She, C., Hardjawana, W., Li, Y., Vucetic, B.: Deep learning
for hybrid 5G services in mobile edge computing systems: Learn from a
digital twin. IEEE Trans. Wireless Commun. 18(10), 4692–4707 (2019).
https://doi.org/10.1109/TWC.2019.2927312
[23] Eyre, J.M., Dodd, T.J., Freeman, C., Lanyon-Hogg, R., Lockwood, A.J.,
Scott, R.W.: Demonstration of an industrial framework for an implementa-
tion of a process digital twin. In: ASME Int. Mech. Eng. Congr. Exposition.
vol. 52019, p. V002T02A070. American Society of Mechanical Engineers
(2018). https://doi.org/10.1115/IMECE2018-87361
[24] Ezhilarasu, C.M., Skaf, Z., Jennions, I.K.: Understanding the role of
a Digital Twin in Integrated Vehicle Health Management (IVHM).


---

Page 43

---

SOTA: AI-Guided PMx DT
43
In: 2019 IEEE Int. Conf. Syst. Man Cybern. pp. 1484–1491 (2019).
https://doi.org/10.1109/SMC.2019.8914244
[25] Fang, X., Wang, H., Li, W., Liu, G., Cai, B.: Fatigue crack growth predic-
tion method for offshore platform based on digital twin. Ocean Eng. 244,
110320 (2022). https://doi.org/10.1016/j.oceaneng.2021.110320
[26] Flanigan, K.A., Ma, S., Berg´es, M.: Functional Requirements Enabling
Levels of Predictive Maintenance Automation and Autonomy. In: 2022
IEEE 2nd Int. Conf. Digital Twins Parallel Intell. pp. 1–2 (2022).
https://doi.org/10.1109/DTPI55838.2022.10036152
[27] Fritzson, P.: The OpenModelica environment for building digital twins of
sustainable cyber-physical systems. In: 2021 Winter Simul. Conf. pp. 1–12.
IEEE (2021). https://doi.org/10.1109/WSC52266.2021.9715443
[28] Galar, D., Thaduri, A., Catelani, M., Ciani, L.: Context awareness for
maintenance decision making: A diagnosis and prognosis approach. Meas.
67, 137–150 (2015). https://doi.org/10.1016/j.measurement.2015.01.015
[29] Gilpin, L.H., Bau, D., Yuan, B.Z., Bajwa, A., Specter, M., Kagal, L.: Ex-
plaining Explanations: An Overview of Interpretability of Machine Learn-
ing. In: 2018 IEEE 5th Int. Conf. Data Sci. Adv. Anal. pp. 80–89. IEEE
(2018). https://doi.org/10.1109/DSAA.2018.00018
[30] Gong, H., Cheng, S., Chen, Z., Li, Q.: Data-enabled physics-informed
machine learning for reduced-order modeling digital twin: application
to nuclear reactor physics. Nucl. Sci. Eng. 196(6), 668–693 (2022).
https://doi.org/10.1080/00295639.2021.2014752
[31] Grieves, M., Vickers, J.: Digital Twin: Mitigating Unpredictable, Undesir-
able Emergent Behavior in Complex Systems, pp. 85–113. Springer Int.
Publ. (2017). https://doi.org/10.1007/978-3-319-38756-7 4
[32] Haarman, M., Mulders, M., Vassiliadis, C.: Predictive maintenance 4.0:
Predict the unpredictable. Tech. rep., PwC Belgium (2017)
[33] Haleem,
A.,
Javaid,
M.,
Pratap
Singh,
R.,
Suman,
R.:
Explor-
ing
the
revolution
in
healthcare
systems
through
the
applica-
tions of digital twin technology. Biomed. Technol. 4, 28–38 (2023).
https://doi.org/10.1016/j.bmt.2023.02.001
[34] Harper, K.E., Malakuti, S., Ganz, C.: Digital Twin Architecture and Stan-
dards (2019)
[35] Hedberg Jr, T.D., Bajaj, M., Camelio, J.A.: Using graphs to link
data
across
the
product
lifecycle
for
enabling
smart
manufactur-
ing digital threads. J. Comput. Inf. Sci. Eng. 20(1), 011011 (2020).
https://doi.org/10.1115/1.4044921
[36] Hichri, N., Stefani, C., De Luca, L., Veron, P., Hamon, G.: From point
cloud to BIM: A survey of existing approaches. In: XXIV Int. CIPA
Symp. Proceedings of the XXIV International CIPA Symposium (2013).
https://doi.org/10.5194/isprsarchives-XL-5-W2-343-2013
[37] Hong Lim, K.Y., Zheng, P., Liew, D.W.: Chapter 4 - digital twin-enhanced
product family design and optimization service. In: Tao, F., Qi, Q., Nee,
A. (eds.) Digital Twin Driven Serv., pp. 89–118. Acad. Press (2022).
https://doi.org/10.1016/B978-0-323-91300-3.00003-6


---

Page 44

---

44
S. Ma et al.
[38] Hosamo, H.H., Svennevig, P.R., Svidt, K., Han, D., Nielsen, H.K.: A Dig-
ital Twin predictive maintenance framework of air handling units based
on automatic fault detection and diagnostics. Energy Build. 261, 111988
(2022). https://doi.org/10.1016/j.enbuild.2022.111988
[39] H¨urkamp, A., Gellrich, S., Ossowski, T., Beuscher, J., Thiede, S.,
Herrmann, C., Dr¨oder, K.: Combining simulation and machine learn-
ing as digital twin for the manufacturing of overmolded thermo-
plastic
composites.
J.
Manuf.
Mater.
Process.
4(3),
92
(2020).
https://doi.org/10.3390/jmmp4030092
[40] International Organization for Standardization: Automation systems and
integration — digital twin framework for manufacturing (2021)
[41] Internet Research Task Force: Digital Twin Network: Concepts and Ref-
erence Architecture (2023)
[42] Jacoby,
M.,
Usl¨ander,
T.:
Digital
twin
and
internet
of
things—Current standards landscape. Appl. Sci. 10(18),
6519 (2020).
https://doi.org/10.3390/app10186519
[43] Jiang, F., Ma, L., Broyd, T., Chen, K.: Digital twin and its implementa-
tions in the civil engineering sector. Autom. Constr. 130, 103838 (2021).
https://doi.org/10.1016/j.autcon.2021.103838
[44] Kaewunruen, S., Xu, N.: Digital twin for sustainability evaluation
of railway station buildings. Front. Built Environ. 4,
77 (2018).
https://doi.org/10.3389/fbuil.2018.00077
[45] Kamble,
S.S.,
Gunasekaran,
A.,
Parekh,
H.,
Mani,
V.,
Belhadi,
A., Sharma, R.: Digital twin for sustainable manufacturing supply
chains: Current trends, future perspectives, and an implementation
framework. Technol. Forecasting Social Change 176, 121448 (2022).
https://doi.org/10.1016/j.techfore.2021.121448
[46] Kapteyn, M., Knezevic, D., Huynh, D., Tran, M., Willcox, K.: Data-driven
physics-based digital twins via a library of component-based reduced-
order models. Int. J. Numer. Methods Eng. 123(13), 2986–3003 (2022).
https://doi.org/10.1002/nme.6423
[47] Kapteyn, M.G., Knezevic, D.J., Willcox, K.: Toward predictive dig-
ital
twins
via
component-based
reduced-order
models
and
inter-
pretable
machine
learning.
In:
AIAA
Scitech
2020
Forum
(2020).
https://doi.org/10.2514/6.2020-0418
[48] Karakra, A., Fontanili, F., Lamine, E., Lamothe, J., Taweel, A.: Pervasive
computing integrated discrete event simulation for a hospital digital twin.
In: 2018 IEEE/ACS 15th Int. Conf. Comput. Syst. Appl. pp. 1–6. IEEE
(2018). https://doi.org/10.1109/AICCSA.2018.8612796
[49] Karve,
P.M.,
Guo,
Y.,
Kapusuzoglu,
B.,
Mahadevan,
S.,
Haile,
M.A.:
Digital
twin
approach
for
damage-tolerant
mission
plan-
ning
under
uncertainty.
Eng.
Fract.
Mech.
225,
106766
(2020).
https://doi.org/10.1016/j.engfracmech.2019.106766
[50] Khajavi,
S.H.,
Motlagh,
N.H.,
Jaribion,
A.,
Werner,
L.C.,
Holm-
str¨om,
J.:
Digital
Twin:
Vision,
Benefits,
Boundaries,
and
cre-


---

Page 45

---

SOTA: AI-Guided PMx DT
45
ation
for
buildings.
IEEE
Access
7,
147406–147419
(2019).
https://doi.org/10.1109/ACCESS.2019.2946515
[51] Khaled, N., Pattel, B., Siddiqui, A.: Digital Twin Development and De-
ployment on the Cloud: Developing Cloud-Friendly Dynamic Models Us-
ing Simulink®/SimscapeTM and Amazon AWS. Academic Press (2020).
https://doi.org/10.1016/C2019-0-03782-X
[52] Kunzer, B., Berg´es, M., Dubrawski, A.: The Digital Twin Landscape at
the Crossroads of Predictive Maintenance, Machine Learning and Physics
Based Modeling (2022). https://doi.org/10.48550/arXiv.2206.10462
[53] La˜na, I., Sanchez-Medina, J.J., Vlahogianni, E.I., Del Ser, J.: From Data
to Actions in Intelligent Transportation Systems: A Prescription of Func-
tional Requirements for Model Actionability. Sens. 21(4), 1121 (Feb 2021).
https://doi.org/10.3390/s21041121
[54] Li, C., Mahadevan, S., Ling, Y., Choze, S., Wang, L.: Dynamic Bayesian
network for aircraft wing health monitoring digital twin. AIAA J. 55(3),
930–941 (2017). https://doi.org/10.2514/1.J055201
[55] Liu,
S.,
Bao,
J.,
Lu,
Y.,
Li,
J.,
Lu,
S.,
Sun,
X.:
Digital
twin
modeling
method
based
on
biomimicry
for
machining
aerospace
components.
J.
Manuf.
Syst.
58,
180–195
(2021).
https://doi.org/10.1016/j.jmsy.2020.04.014
[56] Liu, Z., Jin, C., Jin, W., Lee, J., Zhang, Z., Peng, C., Xu, G.:
Industrial
AI
enabled
prognostics
for
high-speed
railway
systems.
In: 2018 IEEE Int. Conf. Progn. Health Manage. pp. 1–8 (2018).
https://doi.org/10.1109/ICPHM.2018.8448431
[57] Lohtander,
M.,
Ahonen,
N.,
Lanz,
M.,
Ratava,
J.,
Kaakkunen,
J.:
Micro
manufacturing
unit
and
the
corresponding
3D-
model
for
the
digital
twin.
Procedia
Manuf.
25,
55–61
(2018).
https://doi.org/10.1016/j.promfg.2018.06.057
[58] Lu, Q., Xie, X., Heaton, J., Parlikad, A.K., Schooling, J.: From BIM To-
wards Digital Twin: Strategy and Future Development for Smart Asset
Management. In: Borangiu, T., Trentesaux, D., Leit˜ao, P., Giret Boggino,
A., Botti, V. (eds.) Service Oriented, Holonic and Multi-agent Manufactur-
ing Systems for Industry of the Future. pp. 392–404. Springer International
Publishing, Cham (2020). https://doi.org/10.1007/978-3-030-27477-1 30
[59] Luo,
W.,
Hu,
T.,
Ye,
Y.,
Zhang,
C.,
Wei,
Y.:
A
hybrid
pre-
dictive
maintenance
approach
for
cnc
machine
tool
driven
by
digital
twin.
Rob.
Comput.
Integr.
Manuf.
65,
101974
(2020).
https://doi.org/10.1016/j.rcim.2020.101974
[60] Ma,
S.,
Flanigan,
K.A.,
Berg´es,
M.:
State-of-the-Art
Review
and
Synthesis: A Requirement-based Roadmap for Standardized Predic-
tive Maintenance Automation Using Digital Twin Technologies (2023).
https://doi.org/10.48550/arXiv.2311.06993
[61] Macher, H., Landes, T., Grussenmeyer, P.: From Point Clouds to
Building Information Models: 3D Semi-Automatic Reconstruction of
Indoors of Existing Buildings. Appl. Sci. 7(10),
1030 (Oct 2017).
https://doi.org/10.3390/app7101030


---

Page 46

---

46
S. Ma et al.
[62] Magargle, R., Johnson, L., Mandloi, P., Davoudabadi, P., Kesarkar, O.,
Krishnaswamy, S., Batteh, J., Pitchaikani, A.: A simulation-based digital
twin for model-driven health monitoring and predictive maintenance of an
automotive braking system. In: Proc. 12th Int. Modelica Conf. pp. 35–46.
No. 132 (2017). https://doi.org/10.3384/ecp1713235
[63] Margaria,
T.,
Schieweck,
A.:
The
digital
thread
in
industry
4.0.
In: Int. Conf. Integr. Formal Methods. pp. 3–24. Springer (2019).
https://doi.org/10.1007/978-3-030-34968-4 1
[64] Meng,
H.,
An,
X.,
Xing,
J.:
A
data-driven
Bayesian
network
model integrating physical knowledge for prioritization of risk in-
fluencing factors. Process Saf. Environ. Prot. 160, 434–449 (2022).
https://doi.org/10.1016/j.psep.2022.02.010
[65] Meraghni, S., Terrissa, L.S., Yue, M., Ma, J., Jemei, S., Zerhouni, N.:
A data-driven digital-twin prognostics method for proton exchange mem-
brane fuel cell remaining useful life prediction. Int. J. Hydrogen Energy
46(2), 2555–2564 (2021). https://doi.org/10.1016/j.ijhydene.2020.10.108
[66] Mobley, R.K.: 4 - benefits of predictive maintenance. In: Mobley,
R.K. (ed.) An Introduction to Predictive Maintenance, pp. 60–73.
Butterworth-Heinemann, 2 edn. (2002). https://doi.org/10.1016/B978-
075067531-4/50004-X
[67] Moghadam, F.K., Rebou¸cas, G.F.d.S., Nejad, A.R.: Digital twin mod-
eling
for
predictive
maintenance
of
gearboxes
in
floating
offshore
wind turbine drivetrains. Forsch. Ingenieurwes. 85(2), 273–286 (2021).
https://doi.org/10.1007/s10010-021-00468-9
[68] Mohammadi, M., Rashidi, M., Mousavi, V., Karami, A., Yu, Y., Samali, B.:
Quality evaluation of digital twins generated based on UAV photogram-
metry and TLS: Bridge case study. Remote Sens 13(17),
3499 (2021).
https://doi.org/10.3390/rs13173499
[69] Moi, T., Cibicik, A., Rølv˚ag, T.: Digital twin based condition monitoring
of a knuckle boom crane: An experimental study. Eng. Fail. Anal. 112,
104517 (2020). https://doi.org/10.1016/j.engfailanal.2020.104517
[70] Molinaro,
R.,
Singh,
J.S.,
Catsoulis,
S.,
Narayanan,
C.,
Lake-
hal,
D.:
Embedding
data
analytics
and
CFD
into
the
dig-
ital
twin
concept.
Comput.
Fluids
214,
104759
(2021).
https://doi.org/10.1016/j.compfluid.2020.104759
[71] Montero Jim´enez, J.J., Vingerhoeds, R.: A system engineering ap-
proach to predictive maintenance systems: from needs and desires to
logical architecture. In: 2019 Int. Symp. Syst. Eng. pp. 1–8 (2019).
https://doi.org/10.1109/ISSE46696.2019.8984559
[72] Moshrefzadeh, M., Machl, T., Gackstetter, D., Donaubauer, A., Kolbe,
T.H.: Towards a distributed digital twin of the agricultural landscape. J.
Digit. Landsc. Archit 5, 173–186 (2020)
[73] Nascimento,
R.G.,
Viana,
F.A.C.:
Fleet
Prognosis
with
Physics-informed
Recurrent
Neural
Networks
(2019).
https://doi.org/10.48550/arXiv.1901.05512


---

Page 47

---

SOTA: AI-Guided PMx DT
47
[74] National Institute of Standards and Technology: Considerations for digital
twin technology and emerging standards (2021)
[75] OHara,
J.M.,
Higgins,
J.:
Human-system
interfaces
to
auto-
matic
systems:
Review
guidance
and
technical
basis
(2010).
https://doi.org/10.2172/1013461
[76] Onaji,
I.,
Tiwari,
D.,
Soulatiantork,
P.,
Song,
B.,
Tiwari,
A.:
Digital
twin
in
manufacturing:
conceptual
framework
and
case
studies.
Int.
J.
Comput.
Integr.
Manuf.
35(8),
831–858
(2022).
https://doi.org/10.1080/0951192X.2022.2027014
[77] Pan, Y., Zhang, L.: A BIM-data mining integrated digital twin framework
for advanced project management. Autom. Constr. 124, 103564 (2021).
https://doi.org/10.1016/j.autcon.2021.103564
[78] Phanden, R.K., Sharma, P., Dubey, A.: A review on simulation in digital
twin for aerospace, manufacturing and robotics. Mater. Today Proc. 38,
174–178 (2021). https://doi.org/10.1016/j.matpr.2020.06.446
[79] Pimenta, F., Pacheco, J., Branco, C., Teixeira, C., Magalh˜aes, F.: De-
velopment of a digital twin of an onshore wind turbine using mon-
itoring data. In: J. Phys. Conf. Ser. vol. 1618, p. 022065 (2020).
https://doi.org/10.1088/1742-6596/1618/2/022065
[80] Pires,
F.,
Ahmad,
B.,
Moreira,
A.P.,
Leit˜ao,
P.:
Digital
twin
based
what-if
simulation
for
energy
management.
In:
2021
4th
IEEE Int. Conf. Ind. Cyber-Phys. Syst. pp. 309–314. IEEE (2021).
https://doi.org/10.1109/ICPS49255.2021.9468224
[81] Preuveneers, D., Joosen, W., Ilie-Zudor, E.: Robust digital twin composi-
tions for industry 4.0 smart manufacturing systems. In: 2018 IEEE 22nd
Int. Enterp. Distrib. Object Comput. Workshop. pp. 69–78. IEEE (2018).
https://doi.org/10.1109/EDOCW.2018.00021
[82] Qi, Q., Tao, F., Hu, T., Anwer, N., Liu, A., Wei, Y., Wang, L., Nee, A.:
Enabling technologies and tools for digital twin. J. Manuf. Syst. 58, 3–21
(2021). https://doi.org/10.1016/j.jmsy.2019.10.001
[83] Qian, C., Liu, X., Ripley, C., Qian, M., Liang, F., Yu, W.: Digi-
tal Twin—Cyber Replica of Physical Things: Architecture, Applications
and Future Research Directions. Future Internet 14(2),
64 (2022).
https://doi.org/10.3390/fi14020064
[84] Ran,
Y.,
Zhou,
X.,
Lin,
P.,
Wen,
Y.,
Deng,
R.:
A
Survey
of
Predictive Maintenance: Systems, Purposes and Approaches (2019).
https://doi.org/10.48550/arXiv.1912.07383
[85] Rass˜olkin, A., Rjabtˇsikov, V., Vaimann, T., Kallaste, A., Kuts, V., Par-
tyshev, A.: Digital Twin of an Electrical Motor Based on Empirical Per-
formance Model. In: 2020 XI Int. Conf. Electr. Power Drive Syst. pp. 1–4
(2020). https://doi.org/10.1109/ICEPDS47235.2020.9249366
[86] Reitenbach, S., Vieweg, M., Becker, R., Hollmann, C., Wolters, F.,
Schmeink, J., Otten, T., Siggel, M.: Collaborative Aircraft Engine Pre-
liminary Design using a Virtual Engine Platform, Part A: Architecture
and Methodology p. 0867 (2020). https://doi.org/10.2514/6.2020-0867


---

Page 48

---

48
S. Ma et al.
[87] Ritto, T., Rochinha, F.: Digital twin, physics-based model, and machine
learning applied to damage detection in structures. Mech. Syst. Signal Pro-
cess. 155, 107614 (2021). https://doi.org/10.1016/j.ymssp.2021.107614
[88] Roy, R.B., Mishra, D., Pal, S.K., Chakravarty, T., Panda, S., Chandra,
M.G., Pal, A., Misra, P., Chakravarty, D., Misra, S.: Digital twin: Cur-
rent scenario and a case study on a manufacturing process. Int. J. Adv.
Manuf. Technol. 107, 3691–3714 (2020). https://doi.org/10.1007/s00170-
020-05306-w
[89] Sakib, N., Wuest, T.: Challenges and Opportunities of Condition-based
Predictive Maintenance: A Review. Procedia CIRP 78, 267–272 (2018).
https://doi.org/10.1016/j.procir.2018.08.318
[90] Sepe, M., Graziano, A., Badora, M., Di Stazio, A., Bellani, L., Compare,
M., Zio, E.: A physics-informed machine learning framework for predictive
maintenance applied to turbomachinery assets. J. Global Power Propul.
Soc. pp. 1–15 (2021). https://doi.org/10.33737/jgpps/134845
[91] Serradilla, O., Zugasti, E., Rodriguez, J., Zurutuza, U.: Deep learn-
ing models for predictive maintenance: A survey, comparison, chal-
lenges
and
prospects.
Appl.
Intell.
52(10),
10934–10964
(2022).
https://doi.org/10.1007/s10489-021-03004-y
[92] Short, M., Twiddle, J.: An Industrial Digitalization Platform for Condi-
tion Monitoring and Predictive Maintenance of Pumping Equipment. Sens.
19(17), 3781 (2019). https://doi.org/10.3390/s19173781
[93] Shukla,
B.,
Fan,
I.S.,
Jennions,
I.:
Opportunities
for
Explain-
able Artificial Intelligence in Aerospace Predictive Maintenance. In:
Progn. Health Manage. Soci. Eur. Conf. vol. 5, pp. 1–11 (2020).
https://doi.org/10.36001/phme.2020.v5i1.1231
[94] Singh, M., Fuenmayor, E., Hinchy, E., Qiao, Y., Murray, N., Devine, D.:
Digital twin: Origin to future. Appl. Syst. Innovation 4(2), 36 (May 2021).
https://doi.org/10.3390/asi4020036
[95] Singh, V., Willcox, K.E.: Engineering design with digital thread. AIAA J.
56(11), 4515–4528 (2018). https://doi.org/10.2514/1.J057255
[96] Sommer, M., Stjepandi´c, J., Stobrawa, S., von Soden, M.: Automatic
generation of digital twin based on scanning and object recognition. In:
Transdisciplinary Eng. Complex Socio-Tech. Syst., pp. 645–654. IOS Press
(2019). https://doi.org/10.3233/ATDE190174
[97] Sommerville, I., Lock, R., Storer, T., Dobson, J.: Deriving Informa-
tion Requirements from Responsibility Models. In: van Eck, P., Gordijn,
J., Wieringa, R. (eds.) Adv. Inf. Syst. Eng. pp. 515–529 (2009).
https://doi.org/10.1007/978-3-642-02144-2 40
[98] Stojanovic, V., Trapp, M., Richter, R., Hagedorn, B., D¨ollner, J.: Towards
the generation of digital twins for facility management based on 3D point
clouds. Manage. 270, 279 (2018)
[99] Tao, F., Zhang, M., Liu, Y., Nee, A.: Digital twin driven prognostics and
health management for complex equipment. CIRP Ann. 67(1), 169–172
(2018). https://doi.org/10.1016/j.cirp.2018.04.055


---

Page 49

---

SOTA: AI-Guided PMx DT
49
[100] Tuegel, E.J., Ingraffea, A.R., Eason, T.G., Spottswood, S.M.: Reengineer-
ing aircraft structural life prediction using a digital twin. Int. J. Aerosp.
Eng. 2011 (2011). https://doi.org/10.1155/2011/154798
[101] Tygesen, U.T., Worden, K., Rogers, T., Manson, G., Cross, E.J.: State-of-
the-Art and Future Directions for Predictive Modelling of Offshore Struc-
ture Dynamics Using Machine Learning. In: Pakzad, S. (ed.) Dyn. Civ.
Struct., Vol. 2. pp. 223–233 (2019). https://doi.org/10.1007/978-3-319-
74421-6 30
[102] Urbas, U., Zorko, D., Vukaˇsinovi´c, N.: Machine learning based nom-
inal
root
stress
calculation
model
for
gears
with
a
progressive
curved path of contact. Mech. Mach. Theory 165, 104430 (2021).
https://doi.org/10.1016/j.mechmachtheory.2021.104430
[103] Vathoopan, M., Johny, M., Zoitl, A., Knoll, A.: Modular fault ascrip-
tion and corrective maintenance using a digital twin. IFAC-PapersOnLine
51(11), 1041–1046 (2018). https://doi.org/10.1016/j.ifacol.2018.08.470
[104] Venkatesan, S., Manickavasagam, K., Tengenkai, N., Vijayalakshmi,
N.: Health monitoring and prognosis of electric vehicle motor using
intelligent-digital twin. IET Electr. Power Appl. 13(9), 1328–1335 (2019).
https://doi.org/10.1049/iet-epa.2018.5732
[105] Vieweg, M., Reitenbach, S., Hollmann, C., Schn¨os, M., Behrendt, T.,
Krumme, A., Otten, T., zu Ummeln, R.M.: Collaborative aircraft engine
preliminary design using a virtual engine platform, part b: Application
p. 0124 (2020). https://doi.org/10.2514/6.2020-0124
[106] Viola, J., Chen, Y.: Digital twin enabled smart control engineer-
ing
as
an
industrial
AI:
A
new
framework
and
case
study.
In:
2020
2nd
Int.
Conf.
Ind.
Artif.
Intell.
pp.
1–6.
IEEE
(2020).
https://doi.org/10.1109/IAI50351.2020.9262203
[107] Vollert, S., Atzmueller, M., Theissler, A.: Interpretable machine learn-
ing: A brief survey from the predictive maintenance perspective. In: 2021
26th IEEE Int. Conf. Emerging Technol. Factory Autom. pp. 1–8 (2021).
https://doi.org/10.1109/ETFA45728.2021.9613467
[108] Wang, J., Li, Y., Huang, Z., Qiao, Q.: Digital twin-driven fault diagnosis
service of rotating machinery. In: Digital Twin Driven Serv., pp. 119–138.
Elsevier (2022). https://doi.org/10.1016/B978-0-323-91300-3.00004-8
[109] Wang, K.J., Lee, Y.H., Angelica, S.: Digital twin design for real-time mon-
itoring – a case study of die cutting machine. Int. J. Prod. Res. 59(21),
6471–6485 (2021). https://doi.org/10.1080/00207543.2020.1817999
[110] Wang, M., Feng, S., Incecik, A., Kr´olczyk, G., Li, Z.: Structural fatigue
life prediction considering model uncertainties through a novel digital twin-
driven approach. Comput. Methods Appl. Mech. Eng. 391, 114512 (2022).
https://doi.org/10.1016/j.cma.2021.114512
[111] Wang, S., Tuor, T., Salonidis, T., Leung, K.K., Makaya, C., He, T.,
Chan, K.: Adaptive federated learning in resource constrained edge com-
puting systems. IEEE J. Sel. Areas Commun. 37(6), 1205–1221 (2019).
https://doi.org/10.1109/JSAC.2019.2904348


---

Page 50

---

50
S. Ma et al.
[112] Wang,
T.,
Liu,
Z.,
Liao,
M.,
Mrad,
N.:
Life
prediction
for
air-
craft structure based on Bayesian inference: towards a digital twin
ecosystem.
In:
Annu.
Conf.
PHM
Soc.
vol.
12,
pp.
8–8
(2020).
https://doi.org/10.36001/phmconf.2020.v12i1.1261
[113] Wen,
Y.,
Fashiar
Rahman,
M.,
Xu,
H.,
Tseng,
T.L.B.:
Re-
cent
advances
and
trends
of
predictive
maintenance
from
data-
driven machine prognostics perspective. Meas. 187, 110276 (2022).
https://doi.org/10.1016/j.measurement.2021.110276
[114] Werner, A., Zimmermann, N., Lentes, J.: Approach for a holistic predictive
maintenance strategy by incorporating a digital twin. Procedia Manuf. 39,
1743–1751 (2019). https://doi.org/10.1016/j.promfg.2020.01.265
[115] Wu,
Z.Y.,
Chew,
A.,
Meng,
X.,
Cai,
J.,
Pok,
J.,
Kalfarisi,
R.,
Lai,
K.C.,
Hew,
S.F.,
Wong,
J.J.:
High
Fidelity
Digital
Twin-
Based Anomaly Detection and Localization for Smart Water Grid
Operation Management. Sustainable Cities Soc. 91, 104446 (2023).
https://doi.org/10.1016/j.scs.2023.104446
[116] Xiong, M., Wang, H., Fu, Q., Xu, Y.: Digital twin–driven aero-engine in-
telligent predictive maintenance. Int. J. Adv. Manuf. Technol. 114(11),
3751–3761 (2021). https://doi.org/10.1007/s00170-021-06976-w
[117] Xu, Y., Sun, Y., Liu, X., Zheng, Y.: A Digital-Twin-Assisted Fault Diag-
nosis Using Deep Transfer Learning. IEEE Access 7, 19990–19999 (2019).
https://doi.org/10.1109/ACCESS.2018.2890566
[118] Xue, F., Lu, W., Chen, Z., Webster, C.J.: From LiDAR point cloud
towards digital twin city: Clustering city objects based on Gestalt
principles. ISPRS J. Photogramm. Remote Sens. 167, 418–431 (2020).
https://doi.org/10.1016/j.isprsjprs.2020.07.020
[119] Ye,
Y.,
Yang,
Q.,
Yang,
F.,
Huo,
Y.,
Meng,
S.:
Digital
twin
for
the
structural
health
management
of
reusable
space-
craft:
A
case
study.
Eng.
Fract.
Mech.
234,
107076
(2020).
https://doi.org/https://doi.org/10.1016/j.engfracmech.2020.107076
[120] Yu,
J.,
Song,
Y.,
Tang,
D.,
Dai,
J.:
A
digital
twin
approach
based
on
nonparametric
Bayesian
network
for
complex
sys-
tem
health
monitoring.
J.
Manuf.
Syst.
58,
293–304
(2021).
https://doi.org/https://doi.org/10.1016/j.jmsy.2020.07.005
[121] Zhang, J., Li, S., Zhao, Z., Gao, Y., Liu, D., Wang, J., Wang,
Z.L.:
Highly
sensitive
three-dimensional
scanning
triboelectric
sen-
sor for digital twin applications. Nano Energy 97, 107198 (2022).
https://doi.org/10.1016/j.nanoen.2022.107198
[122] Zhang, J., Chauhan, S.: Fast explicit dynamics finite element algorithm
for transient heat transfer. Int. J. Therm. Sci. 139, 160–175 (2019).
https://doi.org/10.1016/j.ijthermalsci.2019.01.030
[123] Zhang, Q., Zhang, X., Xu, W., Liu, A., Zhou, Z., Pham, D.T.: Modeling
of digital twin workshop based on perception data. In: Int. Conf. Intell.
Rob. Appl. pp. 3–14. Springer (2017). https://doi.org/10.1007/978-3-319-
65298-6 1
