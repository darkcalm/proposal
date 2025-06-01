

---

Page 1

---

Smart Grids Co-Simulations: Survey & Research Directions
Peter Mihala, Martin Schvarcbacherb, Bruno Rossia, Tom´aˇs Pitnera
aFaculty of Informatics, Masaryk University, Brno, Czech Republic
bFaculty of Science, University of Amsterdam, Netherlands
Abstract
The integration of renewable sources, communication and power networks with infor-
mation and communication technologies is one of the main challenges in Smart Grids
(SG) large-scale testing. For this reason, the coupling of simulators is commonly used
to dynamically simulate several aspects of the SG infrastructure, in the so-called co-
simulations. In this paper, we provide a scoping review of research of co-simulations
in the context of Smart Grids: i) research areas and research problems addressed by
co-simulations, ii) speciﬁc co-simulation aspects focus of research, iii) typical coupling of
simulators in co-simulation studies. Based on the results, we discuss research directions
of future SG co-simulation research in each of the identiﬁed areas.
Keywords:
Smart Grids; Power Grids; Co-Simulations; Power simulations; Survey
Research; Scoping study
1. Introduction
The complexity of the modern smart power distribution network, the Smart Grid
(SG), presents key challenges for the systems being developed. The plethora of technolo-
gies, communication protocols, and algorithms requires integrated approaches for system
development, testing and validation (Buscher et al., 2015). One solution to tackle such
complexity is to use simulations to test diﬀerent scenarios and interactions with the
environment—such as modelling renewable production and energy pricing interactions
in microgrids (Luo et al., 2018; Hwang et al., 2017). However, isolated simulations alone
are not enough to represent the dynamic behaviors and interplays between a variety of
systems and the complex energy-related ecosystems: coupling of multiple simulation en-
vironments involving both software and hardware devices is necessary to create realistic
scenarios (Besanger et al., 2017; Vogt et al., 2018).
In the SG context, both the power and the data communication domain can be
modelled concurrently to understand complex interactions, often with some hardware-
in-the-loop (HiL) support (Li & Zhang, 2014). Co-simulations have been useful for many
research goals in the SG area, such as modelling power failures and recovering capability
of the power network, investigating device failures, simulating electrical vehicles charging
for demand / response management, simulating the impact of communication packets loss
on the power network, as well as diﬀerent forms of data injection attacks. Such coupling
of diﬀerent simulators poses several challenges in time-synchronization between the simu-
lators, being some simulators based on discrete events, such as network simulators, while
Submitted for review Feb 2020.
arXiv:2109.02349v1  [cs.OH]  6 Sep 2021


---

Page 2

---

others on continuous time, such as power simulators (Vogt et al., 2018). Furthermore,
such simulations have to be contextualized to SG testbeds experiments (Cintuglu et al.,
2017), large infrastructures for testing of SG components in terms of both functional and
non-functional requirements. To conduct such large-scale experiments, multiple locations
can be used and thus be part of the experiment (Buscher et al., 2015). Communication
across large distances and multiple hardware / software solutions, can bring even more
stringent real-time and synchronization challenges (Buscher et al., 2015).
The coupling of distinct simulators, each one running in its own runtime environment,
is commonly deﬁned as co-simulation. A co-simulator allows the connection of multiple
software simulators and hardware emulators to enable multiple uniﬁed simulation sce-
narios (Vogt et al., 2018). In this way, multiple domains can be tested and simulated
transparently as being part of a single system. Connecting multiple simulators presents
many challenges, which are addressed in diﬀerent ways by the various co-simulation
frameworks, such as the mentioned time-synchronization, and the type of architecture
for orchestrating the simulators.
The goal of this paper is to provide a scoping review of co-simulations usage in the SG
domain by giving an aggregated view about the research performed: i) research areas and
research problems addressed by SG co-simulations, ii) speciﬁc SG co-simulation aspects
focus of research, iii) typical coupling of simulators in SG co-simulation studies. All the
knowledge from the review is then used to delineate future research directions.
The structure of the paper is as follows: Section 2 introduces the concept of SGs, typi-
cal research focus on co-simulations and results from previous reviews. Section 3 presents
the methodology of conducting the review together with the review needs, and the set
of research questions to answer. Section 4 presents the main results by answering the
main research questions together with threats to validity: what problems were addressed
by co-simulations, the main focus of research, and the main simulators used. Section 5
presents the main research directions for all the SG areas reviewed in this article, while
Section 6 provides the conclusions.
2. Co-Simulations for Smart Grids
A Smart Grid is an electricity network that represents the convergence of Information
and Communication Technology (ICT), sensors, and power systems to supply electricity
to consumers via two-way digital communication with the goals to improve reliability,
eﬃciency, and resilience (Fang et al., 2011).
Controllers, sensors, computer systems,
automation equipment work together to provide eﬃcient transmission of electricity, fast
restoration of electricity after power disturbances, reduced costs for utilities, lower power
costs for consumers, reduced peak demand, increased integration of large-scale renewable
energy systems, better integration of customer-owner power generation systems, and
improved security. The sustainability and security of the existing communication network
is reached by adding digital infrastructures to the electrical grid to achieve real-time
monitoring of power generation and distribution (Goel et al., 2015).
The area of SGs is highly complex due to the intersection of multiple multidisciplinary
areas, from the services oﬀered, to the technical aspects and the social impacts. Over
time, diﬀerent conceptual reference models have been proposed to represent the SGs. The
CEN-CENELEC-ETSI standardization Group used as base the same conceptual model
2


---

Page 3

---

proposed by the National Institute of Standards and Technology (NIST), to create the
Smart Grid Architecture Model (SGAM) (Bruinenberg et al., 2012).
SGAM provides a three-dimensional model including domain, zones and layers, to
represent the complex SG context (Bruinenberg et al., 2012). The zones constitute dif-
ferent levels of power system management and are constituted by process, ﬁeld, station,
operation, enterprise, and market levels. For example, the station level can provide the
information-level abstraction for data concentration, and substation automation. The
domains represent the energy conversion ﬂow (Bruinenberg et al., 2012): generation,
transmission, distribution, distributed electrical resources (DER), customer premises.
For example, the distribution level constitute the infrastructure for power distribution to
customers. The layers represent diﬀerent cross-cutting concerns for SG architectures, and
are represented by the component, communication, information, function, and business
layers. The component layer is composed of physical and virtual devices, the communi-
cation layer by the protocols used, the information layer by the information models, the
function layer by the functionality requirements, and the business layer by the business
goals for the provided services. The SGAM view provides a way to consider the variety
of aspects involved in SG-related implementation and research.
2.1. SG Research Areas
So far, the research in the SG domain has covered a variety of aspects. To classify
co-simulation articles in this review, we used a classiﬁcation of SG research in nine main
areas (A1-A9) as deﬁned in Cintuglu et al. (2017), in which the last two areas (A8. Cy-
bersecurity and A9. Network communications) are meant to be seen as complementary
to the research goals in the other main seven areas.
A1.
Reliability and wide-area awareness. The aim of the situational awareness
research is to diagnose, anticipate, and respond to prevent problems before disruptions
arise (Cintuglu et al., 2017; Arnold et al., 2010). In the context of SGs, the self-healing
property means that SGs can detect issues and resume normal operations.
By this
automated process, the time needed to repair is signiﬁcantly reduced (Amin, 2008; Beidou
et al., 2010). Achieving this requires an important eﬀort put into strong and reliable
protection, control and communication network (Amin, 2008).
A2. Consumer energy eﬃciency. The goal is to lower energy use during times of
peak demand or when the power reliability is at risk (Cintuglu et al., 2017). This eﬀect
is crucial for optimizing the balance of the distributed power (Arnold et al., 2010).
A3. Distributed Energy Resources (DER). This research area covers energy storage
and utility-independent generation units. The generated power is mainly consumed at
the prosumer premises as a negative load (Cintuglu et al., 2017; Arnold et al., 2010).
The integration of renewable energy sources with the grid is also an important aspect of
research. Alternative power sources such as wind or photovoltaic units provide additional
power to the grid and make it more stable, especially during peak demand times. In
addition, the generation of this kind of electric power provides a more environmental-
friendly output (Beidou et al., 2010).
A4. Grid energy storage. The research focuses on the development of new storage
capabilities. The energy storage concept covers the conversion of electrical energy from a
power network into a form of energy that can be stored and converted back to electrical
energy (Mohd et al., 2008; Cintuglu et al., 2017; Arnold et al., 2010). A very promising
3


---

Page 4

---

research aspect is the usage of plug-in electric vehicles, which bring a way to store
additional energy (known as vehicle-to-grid).
A5. Electric Transportation. Research in this area mainly focuses on wired-wireless,
battery banks, large-scale grid integration and charging stations (Cintuglu et al., 2017).
Another signiﬁcant research aspect is the opportunity to use electric vehicles as a mobile
power storage unit (Arnold et al., 2010).
A6. Advanced Metering Infrastructure. The research on the power quality side
mostly focuses on smart meters technology in order to localize and detect diﬀerent types
of distortion. A smart meter is an electronic device that monitors and records electric
energy consumption and communicates the information to the electricity supplier for
monitoring and billing. The main research goal of this area is an integration of various
technologies that provide an intelligent connection between consumers and system oper-
ators (Zhang & Chen, 2010). System operators implement demand response and price
signaling mechanism to serve according to dynamic pricing (Cintuglu et al., 2017; Arnold
et al., 2010).
A7. Management of distribution grid. Advanced cyber-physical architectures for
distribution grid management aim to maximize the performance of feeders, transformers
and other components of the networked distribution systems and integrate them with
transmission systems and customer operations (Cintuglu et al., 2017; Arnold et al., 2010).
A8.
Cybersecurity.
Since SGs are built on top of ICT infrastructures, they are
vulnerable to cyber-attack threats. Cybersecurity in the SG context considers speciﬁc
communication protocols in various domains (Cintuglu et al., 2017; Arnold et al., 2010).
In addition, the electric grid is very sensitive and represents a potential national target,
increasing the gains and motivations for attackers (Wang & Lu, 2013).
A9. Network communications. SGs make use of two-way communication to provide
improved protection, monitoring, and optimization for all grids components. Customers
use a variety of public and private communication networks, both wired and wireless (Za-
ballos et al., 2011). Prosumer network communication adopts mainly Home Area Net-
work (HAN) to intelligently manage devices. Wireless machine-to-machine (M2M) com-
munication between smart meters eliminates human intervention necessity to operate the
grid intelligently (Cintuglu et al., 2017; Arnold et al., 2010).
2.2. Co-simulation Aspects
In general terms, a simulation is represented by a mathematical model describing
properties of the system being modelled and an independent solver that is applied to
ﬁnd a more or less approximate solution (Vogt et al., 2018).
The model represents
key characteristics of the simulated system, which can be obtained by an abstraction of
the real system. Power systems can be studied under varying conditions and scenarios.
One of the beneﬁts that simulations provide is the option to control simulation time.
Researchers can adjust the running of time, so simulations can run faster than real
systems. This can be helpful to reduce time required to evaluate diﬀerent scenarios,
while granting synchronization with real-time devices, if necessary.
Co-simulations consist of multiple simulators which are coupled together and run sep-
arately. Each can cover a diﬀerent subsystem or aspect of the SG, giving results that can
provide better understanding of coupling eﬀects. Co-simulations pose several challenges
in terms of the run-time infrastructure adopted and the way events are synchronized. In
4


---

Page 5

---

general, simulated systems can be of two types, either discrete or continuous in nature,
depending if state variables change at ﬁxed points in time or continuously (Law et al.,
2000). To model such systems, discrete events and continuous time based models can
be used depending on the needs of the simulations (e.g., if considering the continuous
nature of a phenomenon can be important based on the research goals). One of the
main issues in the integration in a co-simulation is to combine continuous time models
of power systems with discrete events simulations from communication networks (Mets
et al., 2014).
• Discrete Events Models — (co)simulators that model a system as it evolves by
considering variables state changes at speciﬁc points in time, where an event is an
occurrence that can modify the system’s state (Law et al., 2000).
• Continuous Time Models — (co)simulators that consider continuous change of vari-
able states based on the ﬂow of time. There might be some function that expresses
changes of states over time and that could be potentially solved analytically. How-
ever, the complexity might lead to the usage of simulations in the ﬁrst place (Law
et al., 2000).
• Hybrid — (co)simulators that integrate both discrete events and continuous time
simulators and are not limited to one of the two instances (Gomes et al., 2018).
In this sense, an important aspect about co-simulations is the way in which diﬀerent
simulators are synchronized—that is how data is exchanged between simulation solvers:
• Conservative synchronization — in this type of synchronization, ”each simulator
strictly processes events in a time stamp order” (Cintuglu et al., 2017). For in-
stance, a dynamically deﬁned barrier for all simulators, which only allows a next
simulation iteration after all simulators have ﬁnished. It is referred also as “barrier
synchronization”.
• Optimistic synchronization — errors are detected during the simulation and dif-
ferent mechanisms are used to revert them. For example, a pre-deﬁned number of
events are stored and in case of an out-of-order event, the simulation is reversed to
a time before this event and executed again with this event in order; hence it is also
called “Time Warp”. The name “optimistic” assumes that there are no causality
errors (Law et al., 2000).
The runtime infrastructure represents the mechanisms and architectures used to coordi-
nate the diﬀerent simulators within a co-simulation context (Cintuglu et al., 2017; Law
et al., 2000). Single simulation architectures only use one solver. In this context, com-
munication between diﬀerent simulators is not an issue. Parallel simulation architectures
are tightly coupled systems which often share the same memory and are able to perform
inter-process communication. Their communication latency must be reduced to mini-
mum to avoid the introduction of bottlenecks. Distributed simulations architectures are
more complex. often composed of several computers distributed over diﬀerent remote
locations with higher latency than in the parallel simulation architectures. Methods of
events synchronization can also vary in each co-simulation platform:
5


---

Page 6

---

Table 1: Some of the main co-simulation platforms applied to the SG area.
Name
Year
Syncronization
Architecture
Daccosim-NG (´Evora G´omez et al., 2019)
2019
Discrete Events
FMI-based
CyDER (Nouidui et al., 2019)
2019
Discrete Events
FMI-based
HELICS (Palmintier et al., 2017)
2017
Discrete Events
Federated
MECSYCO (Camus et al., 2016)
2015
Discrete Events
Ad-hoc
Daccosim (Galtier et al., 2015)
2015
Discrete Events
FMI-based
FNCS (Ciraci et al., 2014)
2014
Discrete Events
HLA
INSPIRE (Georg et al., 2013)
2013
Discrete Events
HLA
GECO (Lin et al., 2012)
2012
Discrete Events
Ad-hoc
MOSAIK (Sch¨utte et al., 2011)
2011
Discrete Events
Ad-hoc
VPNET (Li et al., 2011)
2011
Continuous Time
Ad-hoc
EPOCHS (Hopkinson et al., 2006)
2006
Continuous Time
Ad-hoc
Co-simulation frameworks are responsible of data exchange and synchronization be-
tween diﬀerent simulators. From the architecture point of view, they can follow several
styles for structuring components. One way is to have a central orchestrator component
that deals with the synchronization issues, but other ways of management are possible,
such as federated models typical of High Level Architecture (HLA) (Albagli et al., 2016).
HLA is a domain-independent reference architecture and a standard aimed at the inte-
gration of diﬀerent simulators and at the synchronization among them (Albagli et al.,
2016). In 2000, it became the oﬃcial IEEE-1516 standard (IEEE, 2010).
In HLA, all components of this architecture are federated and work independently.
Each component is connected to a bus known as a run-time infrastructure. The run-time
infrastructure bus provides services, which are responsible for data ﬂow coordination
between them (synchronization) in order to guard the correct time advancement (Albagli
et al., 2016; IEEE, 2010). Albagli et al. (2016) showcases the orchestration process of
the OMNET++ network simulator, the Jade framework for a multi-agent system, and
the Simulink modeller coordinated into a HLA architecture.
The Functional Mock-up Interface (FMI) was introduced as a standard to allow the
integration and coupling of several models from diﬀerent domains (e.g., mechanical, elec-
trical) (Blochwitz et al., 2011). Through the usage of the API provided by the stan-
dard, co-simulation platforms supporting FMI can be more easily integrate components
(like the co-simulations platforms Daccosim-NG (´Evora G´omez et al., 2019) and Cy-
DER (Nouidui et al., 2019)).
Over time, many co-simulation platforms have been proposed to solve mainly the
issue of synchronization between simulators, starting from the EPOCHS framework that
was proposed in 2006 (Hopkinson et al., 2006) to the Hierarchical Engine for Large-
scale Infrastructure Co-Simulation (HELICS) (Palmintier et al., 2017) and Daccosim-
NG (´Evora G´omez et al., 2019) that are the most recent frameworks proposed to address
scalability and usability issues of previous co-simulators. While HLA provides a domain-
independent co-simulation reference architecture that can be used, other types of ”ad-
hoc” architectures emerged over time. For example, the Framework for Network Co-
simulation (FNCS) provides intentionally a lightweight set of functionalities for data
exchange adopting some ideas from HLA, but not not utilizing the whole standard (Ciraci
et al., 2014). As well, the Mosaik framework Sch¨utte et al. (2011), was speciﬁcally focused
on SGs, thus adopting a simpler architecture than HLA Steinbrink et al. (2018a). We
6


---

Page 7

---

Smart Grid
Co-Simulations
Environment
beneﬁts
Electricity
generation
and dis-
tribution
Energy
usage
optimized
Cost
reducing
eﬀects
Decrease of
pollution
levels
Decrease
peak
demand
Simulation
architectures
Heterogeneous
domains
Single
simulation
archi-
tectures
Parallel
simulation
archi-
tectures
Distributed
simulations
archi-
tectures
Platform
selection
Simulation
model val-
idation
Simulation
techniques
support
HiL
support
Real-time
needs
Open
source
support
Scenarios
supported
Applications
Electrical
supply
Renewable
power
sources
SG infrastructure
optimization
Vehicle-to-grid
Security
modelling
Synchronization
Conservative
sync.
Optimistic
sync.
Discrete
event sync.
Time stepped
sync.
Barrier sync.
Figure 1: Smart Grids simulations concept map
summarize in table 1 some of the main co-simulation architectures used in SG studies so
far, with the year of appearance of the platform, the type of synchronization (if discrete
events or continuous time), and the type of architecture (if adopting HLA or some ad-hoc
architectural style).
In this introductory part, we only scratched the complexity of co-simulations dis-
cussing aspects useful for the scoping review. Given the complexity of the domain, the
interested reader can ﬁnd more challenges and research problems in a recent extensive
survey by Gomes et al. (2018), speciﬁcally focused on co-simulations. As a summary,
we provide a concept map of common concepts found in the SG co-simulation domain
(Fig. 1), covering several relevant aspects: applications, platform selections, synchroniza-
tion aspects, architectures, and beneﬁts.
7


---

Page 8

---

2.3. Previous SG co-simulation reviews
There are not many previous surveys that focus on SG co-simulations—the main
representatives being Vogt et al. (2018); Li et al. (2014); Mets et al. (2014); Yi et al.
(2016); Schloegl et al. (2015). Furthermore, the focus of previous surveys is mainly on
discussing and categorizing the (co)simulation platforms and characteristics, rather than
looking at the application scenarios like the current survey.
Mets et al. (2014) provided an extensive overview of the area of co-simulations for
power systems, focusing on aspects such as synchronization, and providing a classiﬁcation
of both power and network simulators typically used in the area. Authors divide the
frameworks available for research in three categories: power systems (e.g., OpenDSS),
communication networks (e.g., OMNeT++), and SGs simulators (e.g., GridLAB-D).
Overall, the review covers twelve power system simulators, four network simulators and
several SGs simulators.
Yi et al. (2016) classify co-simulation methods in three types: i) uniﬁed, ii) non-real-
time, and iii) real-time simulation methods. Authors review several power and com-
munication co-simulation platforms based on the combination of distinct frameworks,
such as OpenDSS, Modelica, ns2, OMNeT++, together with the application area of the
co-simulation solution (e.g., for SCADA security or wide-area monitor/control and pro-
tection). They further discuss implications about co-simulation platform architectures
for time synchronization.
Li & Zhang (2014) propose an overview of simulation techniques available in the
area of SG co-simulations, focusing more at the communication level.
Authors pro-
vide a comparison of the main communication simulators used in the area (ns-2, OP-
NET,OMNeT++). A discussion of existing SG simulators is presented (SmartGridLab,
GridSim, SCORE, GridLAB-D). Furthermore, extensions necessary to power simulators
to include network simulations (and vice-versa) are discussed. Several platforms for co-
simulations integrating both power and communication aspects are discussed, such as
EPOCHS, GECO, and VPNET.
Schloegl et al. (2015) propose a classiﬁcation scheme for co-simulation tools in SG to
help developers and users to have a common understanding of the domain. Co-simulation
frameworks are categorized according to time-resolution (steady-state, electro-mechanic
range, electro-magnetic range), synchronization (continuous, ﬁxed step, variable step,
event driven), time ratio (faster / same / slower than wall clock time). Furthermore,
authors distinguish between hybrid simulations (one solver per multiple models), co-
simulations (several solvers interacting), hardware supported simulation, hardware in
the loop simulation (Schloegl et al., 2015).
Vogt et al. (2018) survey 26 SG simulation platforms (e.g., Mosaik, EPOCHS), look-
ing at their main diﬀerences. The ﬁnal result is a classiﬁcation of co-simulation platforms
by research areas using the European Technology SG categorization, with indications of
types of co-simulation and simulators used, correlation between research topics and simu-
lation tools, research areas, synchronization types and real-time and HiL support. Based
on the review, future research directions for co-simulations are discussed, in terms of
investigation of ﬂexibility of the markets, simulating interactions between grid operators,
and to estimate cost savings during power grids expansions.
Among the reported research, the only previous study directly comparable to the
current review is the survey by Vogt et al. (2018). However, our review is focused on
8


---

Page 9

---

Table 2: Comparison of current review and Vogt et al. (Vogt et al., 2018).
Aspect
Vogt et al. (Vogt et al., 2018)
This survey
# Studies
50 articles (26 platforms)
82 articles
Main Focus
SG co-sim platforms
SG co-sim applications
Research Method
scoping / mapping study
scoping / mapping study
SG research areas
30 Research Areas from the Euro-
pean Technology Platform SG
9 Research Areas for SG testbeds de-
ﬁned in Cintuglu et al. (2017)
Research Questions
• correlation
btw
simulation
tools and research topics
• distribution of research areas
of the co-sim platforms
• number of buses and distribu-
tion of simulation time spans
• synchronization, open source,
real-time and HiL support
• identiﬁcation of research ar-
eas of application of SG co-
sim.
• focus
of
the
co-sim
appli-
cation (e.g., for power and
comm integration)
• simulators applied the studies
and their coupling
research articles reporting the application of co-simulations to the context of SGs rather
on the usage of co-simulations platforms themselves. Our goal is more focused on the
aspects investigated by means of co-simulation platforms, the type of components and
simulators involved, and research directions for co-simulation research.
As such, the
current review can complement the ﬁndings derived from Vogt et al. (2018) that is more
focused on the speciﬁc SG co-simulation platforms. We highlight the main diﬀerences
between the two reviews in Table 2. Although not explicitly mentioned in Vogt et al.
(2018), we can consider both survey to follow the same research methodology as a scoping
study (Arksey & O’Malley, 2005) / mapping study (Petersen et al., 2008; Barn et al.,
2017)—attempting to map the identiﬁed frameworks / studies / research outcomes to
diﬀerent facets to derive research gaps and future research directions.
3. Smart Grids Co-simulations Review
Based on the published research in the area of co-simulations, we run a formal lit-
erature review about the application of co-simulations in the area of SG, in terms of
focus of research, technologies and frameworks adopted. We follow the search protocol
of systematic mapping studies (Petersen et al., 2008; Barn et al., 2017), in which the fo-
cus is more on collecting quantitative information about published research rather than
in-depth discussion of each source. The advantage of such methodology is that it allows
to get an overview of the whole research area. We set three main research questions to
drive the whole research analysis process.
3.1. Main Research Questions
RQ1. What are the research areas and research problems that co-simulations studies ad-
dressed so far in the SG domain (e.g., cyber-security by simulating data injection
attacks);
9


---

Page 10

---

RQ2. What are the speciﬁc aspects of co-simulations in the SG domain that are the focus
of the articles (e.g., it could be related to the deﬁnition of a new synchronization
method);
RQ3. What is the typical coupling of simulators adopted in each of the case studies in
the SG domain (e.g., we might ﬁnd a speciﬁc power simulator, PyPower, used more
often in combination with ns-3 as a network simulator);
Based on the results answering these main research questions, we elaborate further on re-
search applying co-simulations to the SG context, providing a series of research directions
(Section 5).
3.2. Review Process
For the review process, we selected four main digital repositories: IEEE Xplore, ACM
Digital Library (DL), Springerlink, and ScienceDirect. These repositories were selected
based on the heterogeneity of results that would be expected, reaching a low number of
duplications. Overall, we used the queries listed in Table 3.
Table 3: Review queries and total number of papers.
Repo
Query
#
IEEE Xplore
Metadata (abstract+title text+indexing
terms:((smart grid*) AND co-simulation*)
196
ACM DL
((+smart +grid* +co-simulation*) (ANY FIELD:
title, abstract, full text)
266
SpringerLink
(’smart AND grid AND co-simulation’) (Full-text
search)
200
ScienceDirect
("smart grid" OR "smart grids") AND
("co-simulation" OR "co-simulations") (Full-text
search)
129
We did not set any a-priori range for years of the queries. The overall main idea of
using co-simulations in the area of SG emerged in year 2006 (see the EPOCHS frame-
work Hopkinson et al. (2006)), but the work of Godfrey et al. [R28] was one of the ﬁrst
to provide some case study). Conversely, the general concept of co-simulations in other
domains dates back longer time before (see recent co-simulation reviews by Gomes et al.
(2017, 2018), e.g. for the automotive domain usage of co-simulations dates back to 1998).
Overall, after running the queries on the four digital repositories, we had 791 articles
after the ﬁrst phase of querying. By merging all the results there were 47 duplicates, so
we had 744 articles in total for the scoping review. Based on the research questions of
the review, we set some inclusion criteria: IC1) papers in which one/more co-simulation
frameworks were discussed in the context of SGs, IC2) papers in which there was at
least one practical example / case study of the application of the adopted co-simulation
framework for a concrete SG research problem. Only articles in English were included.
A ﬁrst phase of ﬁltering was done based on the title and abstract of the papers. 567
articles were removed mainly because the main focus was not about co-simulations. At
this stage, we had 177 papers (56 articles to be included, and 121 to be reviewed again).
The ﬁnal phase of inclusion for ”undecided” papers, yielded the ﬁnal 123 articles that
were included in the pre-ﬁnal step of the review.
10


---

Page 11

---

The last step was about extracting all the required information from the papers
to answer the four main research questions. During this process, as a collateral eﬀect
some papers were removed as not found relevant according to the goals of this review
(e.g., papers not covering the deﬁnition of co-simulation frameworks, rather then just
discussion about qualities of frameworks). Overall, 41 papers were removed in this step,
leaving a ﬁnal set of 82 papers.
4. Main Review Results
4.1. Research Areas and Research Problems (RQ1)
We ﬁrst address the research areas and problems that co-simulations are meant to
address in the papers (e.g., cyber-security by simulating data injection attacks). For this
goal, we mapped all the co-simulation articles in the categories of SGs research (A1-A9)
deﬁned in Cintuglu et al. (2017), that we deﬁned in Section 2.1 ”SG Research Areas”
(Table 4).
Each paper was mapped to one or more categories, depending on the problem ad-
dressed by the usage of co-simulations: A1.
Reliability and wide-area awareness (32
papers), A2. Customer energy eﬃciency (18), A3. Energy resource distribution (16),
A4. Grid energy storage (11), A5. Electric Transportation (11), A6. Advanced Metering
Infrastructure (14), A7. Management of distribution grid (34), A8. Cybersecurity (15),
A9. Network communications (29). Overall, co-simulations have been useful for a variety
of research goals in the SG area, by allowing the coupling of diﬀerent simulators, mainly
power and communication ones.
A1. Reliability and wide-area awareness. Co-simulations have been often used for
performance and reliability of the power networks wide area monitoring and control sys-
tems using data provided by phase measurement units, generally analyzing the combined
eﬀects of communication, network, power levels for wide-area monitoring, protection and
control (Bottura et al., 2013; Lin et al., 2011, 2012b; M¨uller et al., 2012). There are also
studies that looked into bad data measurements and the impact of cyberattacks, look-
ing at the latency and bandwith for control and protection applications, and simulating
cascading failures in SGs (Ravikumar et al., 2017; Saxena et al., 2017; Zhao et al., 2013).
A2. Customer energy eﬃciency. Co-simulations have been used for load control,
to model customers and prosumers behaviour, voltage control for demand and supply
load balancing, simulating residential loads, studying demand and response and energy
pricing (Awad et al., 2016; Ayon et al., 2017; Bompard et al., 2016; Duerr et al., 2017;
Hess et al., 2016; Lehnhoﬀet al., 2015; Makhmalbaf et al., 2014; Moulema et al., 2015).
A3.
Energy resource distribution.
Co-simulations have been used for studying
the integration of PV panels for household power consumption, optimal strategies for
electrical vehicles recharging, the plug-in strategies of electric vehicles to stabilize grid
voltage (Nannen et al., 2015; Li et al., 2017; Broderick et al., 2017).
A4. Grid energy storage. Co-simulations have been used for electric vehicles charging
events simulations in the context of the grid, to investigate wireless and sensor technolo-
gies for electric vehicles charging, investigating ﬂexible charging algorithms (Broderick
et al., 2017; Li et al., 2017; Shum et al., 2013; Stifter et al., 2013; Palensky et al., 2013).
A5. Electric Transportation. Co-simulation was used for simulating control algo-
rithms for energy distribution networks, using electric vehicles as power storage units to
stabilize the grid (Li et al., 2017; Shum et al., 2013; Barbierato et al., 2018).
11


---

Page 12

---

Table 4: (RQ1) Problems addressed by co-simulations and research areas.
Problems addressed
co-sim platform
A1
A2
A3
A4
A5
A6
A7
A8
A9
[R2] Power failures recovery
JADE


[R13] Reliability of Monitoring and Control
Custom


[R26] Reliability of the ICT network
Matlab

[R28] Communication failures
Custom



[R35] Protection relays reliability
FNCS


[R38] Power and communication failures
Custom


[R47] Agent-based remote relay protection
Custom



[R46] Remote relay protection
GECO



[R56] Monitoring, protection and control
FNCS


[R64] Communication in control applications
Custom




[R66] Monitoring and control applications
Matlab + JADE


[R68] Bad data measurements
Matlab + JADE


[R69] Agent-based fault location, restoration
JADE

[R75] Reliability of the control strategies
Matlab


[R80] Operation, control strategies
OpSim


[R81] Voltage control of photovoltaic stations
Custom



[R82] Cascading Failures
Custom


[R63] Reconﬁguration after faults
GECO



[R5] Power monitoring & control
Custom



[R50] Demand and supply load balancing
FNCS



[R22] Cybersecurity Distribution Grid
HELICS



[R54] Voltage control distribution power grid
Custom



[R3] Distribution network models
Custom



[R4] Power distribution network events
Custom


[R7] Voltage proﬁles
Sgsim


[R8] Users power consumption behaviour
Custom

[R12] Control strategies for prosumers
Custom



[R23] Optimization techniques for SGs
EnergyPlus


[R31] Residential loads balancing
Mosaik


[R39] Thermostatically controlled loads
Custom

[R42] Grid modelling analysis
Mosaik


[R55] Demand / response and energy pricing
FNCS



[R57] Integration of low-cost HiL
Mosaik



[R60] Power system control applications
Lablink



[R53] Home energy management and tariﬀs
Custom



[R20] SG market applications for pricing
FNCS


[R21] Real-time market-grid coupling
GridLAB-D


[R32] Transmission / distribution networks
FNCS


[R34] Voltage regulation in distribution
JADE


[R51] Power load and market pricing
FNCS


[R52] Control algor. distribution network
Custom



[R37] Power supply to oﬀshore production
Matlab


[R36] Power-balancing in the isolated grid
Mosaik + JADE



[R14] Electric Vehicles charging events
Custom


[R44] Stable grid charging electric vehicles
GridLab-D



[R71] Vehicle to grid voltage support
FNCS



[R74] Electric Vehicles smart charging
Modelica


[R33] Voltage control in generators
Matlab


[R43] Control algorithms of electric vehicles
Custom




[R61] Flexible electric vehicles charging
Modelica



[R9] Demand Response management
Custom

[R77] Communication Demand Response
Custom


[R76] Demand side management for services
Custom

[R24] Pricing, and comm. delays in DR
GridLab-D


[R15] Synchronization for SCADA
EPOCHS


[R78] Power load balancing
Custom


[R73] Power distribution voltage control
Custom

[R10] Wide-area grid monitoring
Custom



[R18] Network voltage regulation
Matlab


[R1] Voltage regulation power distribution
JADE

[R40] Voltage control
Matlab

[R58] Power and ICT testing
Mosaik

[R46] Injected data and cyber attacks
Custom



12


---

Page 13

---

[R30] Control sys resilience to cyber threats
Matlab

[R72] Simulating cyberattacks
Matlab


[R16] Grids vulnerabilities identiﬁcation
Custom


[R17] Data attacks to the grid
Custom



[R11] Distribution comm. performance
Custom


[R19] Context-aware intrusion detection
Mosaik


[R25] Communication in energy distribution
Matlab


[R27] Network communication monitoring
Custom


[R29] Communication network performance
Custom


[R41] Grid components communication
Custom


[R45] Voltage control real-time comm.
Modelica



[R49] HiL cyber-attacks
Custom



[R59] Cyber-attacks on voltage control
Matlab


[R62] Data attacks in energy management
Matlab


[R65] Network simulators power distribution
GridLab-D


[R67] SCADA systems cyber-attacks
Matlab


[R69] Data transmission voltage control
Mosaik


[R6] Electrical vehicle recharging
Sgsim




[R79] Data communication attacks microgrid
Custom



A6. Advanced Metering Infrastructure. Co-simulations were used for modelling
demand / response scenarios and energy pricing, studying both the inﬂuence of physical
aspects of the grid and the energy market (Mittal et al., 2015; Ciraci et al., 2014; Ding
et al., 2016; Mallapuram et al., 2017; Tariq et al., 2014; Syed et al., 2015; Fuller et al.,
2013).
A7. Management of the distribution grid. Co-simulations were focused on syn-
chronization mechanisms for SCADA systems, power feeders load balancing and power
control, voltage regulation in power distribution networks, phasor measurement units
regulation (Bytschkow et al., 2015; Troiano et al., 2016; Stevic et al., 2013; Bhor et al.,
2016; Ahmad et al., 2015; Nguyen et al., 2017).
A8. Cybersecurity. Co-simulations have looked into the integration of network failures
simulations, data injection attacks in diﬀerent parts of the SG infrastructure, simulation
of cyberattacks, evaluation of intrusion detection algorithms, identiﬁcation of the vulner-
abilities of the integration of the power network and ICT (Stefanov & Liu, 2012; Caire
et al., 2013; Chromik et al., 2017; Liu et al., 2018; Ni et al., 2018; Pan et al., 2017; Sadi
et al., 2015; Venkataramanan et al., 2016).
A9. Network communications. Co-simulations were deployed to analyze communi-
cation networks performance in the integration within the SG infrastructure, real-time
communication, evaluation of wireless and wired communication networks, communica-
tion between grid components and control systems (Bian et al., 2015; Garau et al., 2017;
Georg et al., 2013; Gurusinghe et al., 2016; Lau et al., 2012; Liberatore & Al-Hammouri,
2011; Schloegl et al., 2016; Awad et al., 2014).
4.2. Speciﬁc research aspects of SG co-simulations (RQ2)
In this research question, we look at the main focus of the application of a co-
simulation platform, in terms of the problems the solution addresses.
We identiﬁed
four main research focuses:
F1. Approaches for time and objects synchronization in co-simulations. The
focus of the co-simulation platform is about addressing the issues of time and object
synchronization between two diﬀerent simulation environments—e.g. (Amarasekara
13


---

Page 14

---

et al., 2015; Georg et al., 2013). For example, a synchronization method for coor-
dinating simulators that can be tuned according to the simulation applications was
presented in (Pan et al., 2016). A novel co-simulation scheduler taking into account
events from power and communication network simulators, with the timing of each
embedded controller’s execution loop was proposed for synchronization in (Kounev
et al., 2015).
F2. Real-time monitoring and testing. The focus is on the real-time properties
of the co-simulation platform. For example, the co-simulation platform is focused
on allowing to perform real-time monitoring and control tests and simulations for
MV/LV grids (Armendariz et al., 2014). A real-time software-in-the-loop set-up
which emulates the behavior of the real-world systems integrating inputs from IoT
devices from customers to retrieve energy information is presented in (Barbierato
et al., 2018).
F3. Integration of power and communication simulators. Many papers discuss
the eﬀectiveness of co-simulations in analysing the coupled eﬀects between power
system and communication infrastructure, being very convenient to co-simulate
diﬀerent aspects instead of building a single tool with all the capabilities (power
system modelling, intelligent control and communication) (Ahmad et al., 2015). For
example, a simpliﬁed co-simulation model is used to analyze the interdependencies
between energy and information ﬂows (Cao et al., 2018). The FNCS framework
using a federated co-simulation model for integrating transmission and distribution
network simulators was discussed in (Huang et al., 2017).
F4. Co-simulation architecture. The focus is on the evaluation of diﬀerent com-
ponents within a co-simulation platform.
For example, several aspects of co-
simulations, required to develop a framework, together with the simulation ar-
chitecture design are discussed in (Albagli et al., 2016). The architecture and con-
ﬁguration of two diﬀerent co-simulation approaches, SITL (System in the Loop)
and HLA are discussed in (Bottura et al., 2013). Comparison of running simula-
tions with Mosaik support are discussed in (Hess et al., 2016; Lehnhoﬀet al., 2015).
Loose coupling of heterogeneous components (i.e. continuous and time-triggered
subsystems) is evaluated by means of a message bus, to allow multiple simulators
to exchange messages in (Mosshammer et al., 2013).
F1. Synchronization
F2. Real-time
F3. Integration
F4. Architecture
14.82%
11.11%
27.16%
46.91%
Figure 2: Focuses of co-simulation research
We mapped all papers to each of the four main types of focus of the articles. Looking
at the number of papers (Fig. 2), the deﬁnition of co-simulation platforms was focused, in
14


---

Page 15

---

increasing order of frequency, on F4. Architecture (46.91%), F3. Integration (27.16%),
F1.
Synchronization aspects (14.82%), and F2.
Real-time aspects (11.11%).
While
running a complete trend analysis would be inconclusive due to the sample size and
diﬀerences in each category, the impression is that the discussion about architectural
aspects was more the focus of recent years of publications.
Considering the SG research areas (A1-A9) previously discussed, we then mapped
each type of focus by the area of research in Fig. 3. This view can give a representation
of the distribution of the research interest by each of the identiﬁed categories.
We can see that F1.Synchronization aspects were more investigated in papers related
to the categories A1. Reliability and wide-are awareness and A9. Network communica-
tions. F2.Real-time aspects were more related to A6. Advanced Metering Infrastructure,
F3.Integration aspects more for A8. Cybersecurity, A9. Network communications, and
F4. Architecture aspects more for A2. Customer energy eﬃciency, A7. Management of
distribution grid, and A9. Network communications.
The adoption of co-simulations faces several challenges from the integration of plat-
form from diﬀerent domain, and scaling to a level that can be considered comparable to
real-world electricity grids.
About the issues in the creation of co-simulation platforms, FMI (Section 2.2) was
introduced as a way to reduce the complexity of coupling simulators from diﬀerent
domains via a common API (Blochwitz et al., 2011).
The standard has been eﬀec-
tively adopted by platforms such as Daccosim-NG (´Evora G´omez et al., 2019) and Cy-
DER (Nouidui et al., 2019). However, the standard was not considered for platforms such
as HELICS (Palmintier et al., 2017) due to scalability concerns over a certain number of
federates and for high-speed requirements.
While HLA (Section 2.2) aims to support multiple development environments and
platforms (Albagli et al., 2016; IEEE, 2010), some co-simulation platforms take a diﬀerent
approach. For example, the Mosaik framework Sch¨utte et al. (2011), diﬀerently from
HLA, was built as platform for co-simulations speciﬁcally focused on SGs. Being focused
on the context, the architecture was simpliﬁed, based on a simulation manager and a
scheduler
Steinbrink et al. (2018a). Conversely, the HELICS platform considered the
runtime infrastructure in HLA of open source implementations not to be scalable over
100K federates.
However, HLA principles and time synchronization approaches were
considered for the design of HELICS (Palmintier et al., 2017).
4.3. Coupling of simulators adopted (RQ3)
In this research question, we looked into the speciﬁc simulators that are used: the
main simulators mentioned are mostly power, communication, and general purpose sim-
ulators (Table 5).
As a ﬁrst step, we looked at the frequency of usage of the main simulators mentioned
(Table 5). GridLab-D (16) was the most used power simulator, followed by PowerFac-
tory (13), and OpenDSS (11). However, compared to the other simulators, GridLab-D
provides a whole management environment that can be also used for coordination of
simulators, so its high usage level is justiﬁed by the more functionality oﬀered compared
to other frameworks providing only power simulation functionality. In fact, Mets et al.
(Mets et al., 2014) consider it as a whole SG simulator, providing more functionality
than a simple power simulator. For networks simulators, OmNeT++ (14), NS-3 (11),
15


---

Page 16

---

Figure 3: F1-F4 co-simulation focuses by SG research area
OPNET (10), and NS-2 (8) were the most used ones. There is, however, a good level of
variability of the adoption of the simulators mentioned. There are also some temporal
variations in the usage of the simulators, like NS-2 that is mostly mentioned in articles
from years 2010-2011, less used in recent years due to the newer version NS-3.
As a second step, we looked at how are the simulators combined for co-simulation
purposes (Fig. 4). We divided the simulators in three categories: power, network, and
others.
In the third category we included frameworks that can be used for diﬀerent
purposes, like GridLab-D that can be used as power simulator or for coordination of
simulators, as previously mentioned. For Modelica, Matlab/Simulink, and JADE, these
are used to either model or implement diﬀerent aspects related to simulations.
While we observed that OPNET is the most used network simulator in the studies
provided (even though NS-3, NS-2, and OMNeT++ follow close), we can see in the
heatmap that OPNET is mostly used with PSCAD and Opal-RT. OMNeT++ is more
used in combination with OpenDSS, PowerFactory and JADE. NS-2 is more applied
together with Modelica, OpenDSS, and PSLF, while NS-3 is more used coupled with
GridLab-D, with OpenDSS, MatPower, PowerWorld and Matlab/Simulink that follow.
These couplings represent the cases in which integration between the diﬀerent simulators
can be considered more easier from the implementation point of view.
Furthermore, we looked into the adoption of three diﬀerent architecture-related con-
cepts in the SG domain: i) the usage of agent-based systems within the architecture,
ii) the support of the HLA, and iii) the support of HiL devices. Agent-based systems
are an architectural style that is used in the context of simulations. The main idea is
to model the behaviour of several software agents and collecting the outcomes from the
evolving interactions, where an agent is an autonomous entity that can interact with the
simulation environment. The capabilities of learning and adapting are key characteris-
16


---

Page 17

---

Table 5: Main simulators and frequency of usage in the surveyed articles.
Simulator
Type
URL
Description
Freq
GridLab-D
Power
https://www.gridlabd.org
Power distribution system simula-
tion and analysis tool
16
JADE
Agent-
based
https://jade.tilab.com
Java-based Open Source platform
for agent-based applications
6
Matlab
Simulink
General
https://www.mathworks.com/
products/simulink.html
Design and simulation software
6
MATPOWER
Power
http://www.pserc.cornell.
edu/matpower/
Power system simulation and opti-
mization software
3
NS-2
Network
https://www.isi.edu/nsnam/
ns/
Network communication simulator
8
NS-3
Network
https://www.nsnam.org
Network communication simulator
12
Opal-RT
Power
https://www.opal-rt.com/
software-rt-lab/
Real-time simulation software
5
OMNeT++
Network
https://omnetpp.org
Network communication simulator
14
OpenDSS
Power
https://www.epri.com/#/
pages/sa/opendss
Power distribution system simulator
11
OpenModelica
General
https://openmodelica.org
Open source modeling and simula-
tion environment based on the Mod-
elica language
7
OPNET
Network
https://www.riverbed.com/gb/
products/steelcentral/opnet.
html
Network communication simulator
10
PowerFactory
Power
https://www.digsilent.de/en/
powerfactory.html
Power system analysis software
13
PowerWorld
Power
https://www.powerworld.com/
Power system simulator
3
PSCAD
Power
https://hvdc.ca/pscad/
Power system simulator
6
PSLF
Power
https://www.
geenergyconsulting.
com/practice-area/
software-products/pslf
Power system analysis software
3
PYPOWER
Power
https://pypi.org/project/
PYPOWER/
Power system analysis software, port
of MatPower to Python
3
tics of the software agents (Law et al., 2000). HiL represents the availability of hardware
devices that can be integrated by means of the co-simulation platform. Either interfaces
or other means of support need to be present in the co-simulation platform. As described
in Section 2.2, HLA provides a reference architecture for integrating diﬀerent simulators,
so it is interesting to know the level of usage in the SG domain.
The ﬁndings about the distribution of these three aspects (agent-based, Hil, HLA)
are quite compelling (Fig. 5). Agent-based systems are quit often used in the diﬀerent
SG research areas, with some (such as A4-A5 in which almost half of the articles report
the usage of some form of agent-based system—typically adopting the JADE framework.
HiL is available and discussed in many of the platforms, with the studies proposing the
integration with hardware devices in a large number of cases (like 70% of the cases in
category A7). Integration of hardware devices is thus an important aspect in the context
of SG research. HLA was not instead widely discussed, one main reason being that many
co-simulation platforms (see Section 2.2, Table 5) are using some ad-hoc architecture,
while only federated solutions discuss the application of HLA standard.
17


---

Page 18

---

Figure 4: Simulators used in combination with network simulators
5. Research Directions
The review conﬁrmed some trends of research that were reported in previous studies
(e.g., from Steinbrink et al. (2018b)), like the fact that the discussion between discrete /
continuous time events was one aspect mostly focused in earlier studies, while nowadays
a common focus seems more on the scalability of co-simulation studies. While in the
reviewed studies we could not ﬁnd yet a discussion about big data analysis, it is one
research direction that will acquire more importance in the next years, together with
ways to scale the analysis to larger number of sensors and IoT devices.
From the point of view of the aspects investigated, a trend we observed is that the
initial focus of co-simulation papers was more on pure energy-related issues (such as
simulations for voltage control), while nowadays quality aspects such as network com-
munication, security, and privacy play a major role. We expect this trend to become
even more signiﬁcant in future years. The expectations are that co-simulations studies
will acquire more importance for these aspects, for example for integrating better cyber-
security threats analysis into the context of the power network. In this view, the coupling
between power and communication simulators seems an acquired reality that is used in
the majority of the case studies to represent the complexity of the SG infrastructure.
Another trend we expect to be increasing in the next years is the inclusion of HiL
devices. In our review, we found that 59% of the articles had some form of interaction
18


---

Page 19

---

Figure 5: A1-A9 categories mapped to agent-based, HAL and HiL support.
with hardware devices. We expect that with the explosion of the IoT movement and
the large availability of commodity hardware such as Arduinos and Raspberry PIs, such
trend will increase, allowing hybrid simulations to take place in this context, as recent
research has already shown—Schvarcbacher & Rossi (2017); Schvarcbacher et al. (2018),
(Nannen et al., 2015).
Another trend we expect to see is an increase in the discussion of co-simulation in
the context of SG testbeds (e.g. Cintuglu et al. (2017)), leading to needs in terms of
the integration in larger-scale contexts of the research performed so far in the area.
This can mean more needs of integration of distributed hardware devices and software
simulators. While remote access requirements have been limited so far, we expect such
needs to increase in the future, leading to similar systems as DeterLab (Mirkovic &
Benzel, 2012) for teaching cybersecurity testing and simulation scenarios. Integration of
the connection between cloud-based testing and expensive laboratory devices for remote
real-time testing can be an alternative over cheaper solutions based on commodity IoT
devices for the emulation of real hardware—like showed in Schvarcbacher & Rossi (2017);
Aurilio et al. (2014), (Nannen et al., 2015). There are many challenges involved in such
”scaling-up”, but also many opportunities in terms of the complexity of the simulated
scenarios, sharing of knowledge between researchers and educational opportunities.
More ﬁne-grained research directions can be based on the categorization of relevant
SG research into diﬀerent research areas that we used to map co-simulation research
(A1-A9 categories) Cintuglu et al. (2017).
A1. Reliability and wide-area awareness. Reliable protection, control and com-
munication networks will continue to be a focus of research supported by co-simulation
frameworks. We expect that self-healing mechanisms will play an increasing role in the
19


---

Page 20

---

future, by means of simulations about interruption of services, and the evaluation of
the eﬃciency of self-healing mechanisms. Integration of hardware devices and software
simulators can help in reaching these goals.
A2. Consumer energy eﬃciency. This was an area in which earlier co-simulation
studies were focused and will still be relevant area of research. We expect co-simulations
to still continue to help for the evaluation of new algorithms for customers behaviour
prediction and optimization, aiding in combining power simulators and real-time power
systems. We expect also the increase of usage of IoT devices and commodity hardware
to emulate hardware components such as smart meters.
A3. Distributed Energy Resources (DER). We expect the area to continue being
focus of research for alternative power sources such as wind or photovoltaic units to
provide additional power to the grid and make it more stable, especially during peak
demand times. Co-simulations can help in identifying optimizations for load balancing
of the overall network.
A4. Grid energy storage. We expect this area to grow in terms of research related
to plug-in electric vehicles, that can bring additional ways to store energy and create
vehicles-to-grid networks. In the review we had already several articles discussing inte-
gration of electric vehicles, we expect more frameworks to emerge to simulate diﬀerent
aspects. One example is Bompard et al. (2016) in which authors are testing a man-
agement strategy for distributed storage and 120 vehicles-to-grid, connected to a real
distribution network model.
A5. Electric Transportation. We expect co-simulations to play an important role in
this area, considering the growing needs of energy transportation, e.g. thinking about
charging stations and battery banks. Also in this context, the usage of electrical vehicles
as mobile power storage units will make use of simulations relevant, in similar way as the
area A4. Grid energy storage. As such, we expect more research in the line of Palensky
et al. (2013), looking to create a versatile platform for simulating electric vehicle charging
algorithms for demand response, coupling a Modelica-based physical simulation engine,
a power network simulation tool and an agent-based simulator.
A6. Advanced Metering Infrastructure. Research about smart metering devices
played a large role in initial SG co-simulation research. The possibility to emulate /
simulate large number smart metering devices allowed to look at the scalability of the
solutions provided. In this area, the usage of co-simulation platforms with power and
communication simulators has reached a certain maturity, and will still continue to be
relevant for the provision of SG services.
A7.
Management of distribution grid. This area will continue to be supported
by co-simulations for the optimization of power distribution systems. In this area, we
see even more the interest of the integration of renewable energy power sources within
the electric grid that can beneﬁt from co-simulation and HiL research. These, along
with a forecast-based production and eﬃcient energy storage systems still need to be
investigated (Beidou et al., 2010).
A8.
Cybersecurity.
While initial research on co-simulation was more focused on
power and communication networks, we expect the area of cyber-security to become more
relevant for co-simulations. We expect larger scale integration with SG testbeds Cintuglu
et al. (2017), in which co-simulation can be integrated with security scenarios deﬁned in
cyber-security ranges (Vykopal. et al., 2017). In any case, we expect these aspects to be
more and more integrated into SG co-simulation scenarios.
20


---

Page 21

---

A9.
Network communications. Initial co-simulation frameworks were focused on
the integration of power and communication networks for simulating packet transmis-
sion. We expect in this area a constant move towards more complex scenarios, e.g. the
best wireless-wired scenarios to connect smart meters and data concentrators, packet
losses, and data injection attacks. We see this area more and more connected to A8.
Cybersecurity, as reliability of the information ﬂow within the SG infrastructure is a key
element for the correctness of operations. Furthermore, both simulations and HiL can
be useful in this area to determine the most eﬃcient communication means.
6. Conclusions
To address the complexity of the SG infrastructure, multiple simulation environ-
ments are used to capture the dynamic aspects of the interplay between the many sys-
tems, sensors, communication means, and energy-related ecosystems.
Co-simulations
were adopted in the SG domain as a way to couple and synchronize diﬀerent simulators
to grant more realistic scenarios involving also hardware devices.
The goal of this paper was to provide an aggregated view about the usage of co-
simulations in the SG context by means of a scoping review: i) research areas and
research problems addressed by SG co-simulations, ii) speciﬁc SG co-simulation aspects
focus of research, iii) typical coupling of simulators in SG co-simulation studies. Based
on the reviewed studies, we delineated future research directions for SG co-simulations.
In general, co-simulations have been used for a variety of goals and cross-cutting con-
cerns. They have been used initially as a way to combine both power and communication
aspects of the grid, but later on to integrate other views, such as market pricing simu-
lations or vehicle-to-grid aspects that are quite relevant in recent years. Co-simulations
have been useful for many research goals in the SG area, such as modelling power failures
and recovering capability of the power network, investigating device failures, simulating
electrical vehicles charging for demand/response management, simulating the impact of
communication packets loss on the power network, as well as to investigate diﬀerent
forms of data injection attacks. Overall, our ﬁnal remark is that co-simulations will con-
tinue to play a major role with even greater challenges to be addressed in the future,
like the needs of integration in the context of the emergence of larger SG testbeds and
new emerging cyber-threats that will challenge existing countermeasures. Furthermore,
the increasing interest in renewables and electric vehicles integration within the grid can
constitute a relevant application domain for co-simulation platforms.
Acknowledgments
The research was supported from ERDF/ESF ”CyberSecurity, CyberCrime and Criti-
cal Information Infrastructures Center of Excellence” (No. CZ.02.1.01/0.0/0.0/16 019/0000822).
References
Albagli, A. N., Falc˜ao, D. M., & de Rezende, J. F. (2016). Smart grid framework co-simulation using
hla architecture. Electric Power Systems Research, 130, 22 – 33.
Amin, M. (2008). Challenges in reliability, security, eﬃciency, and resilience of energy infrastructure:
Toward smart self-healing electric power grid.
In 2008 IEEE Power and energy society general
meeting-conversion and delivery of electrical energy in the 21st century (pp. 1–5). IEEE.
21


---

Page 22

---

Arksey, H., & O’Malley, L. (2005). Scoping studies: towards a methodological framework. International
Journal of Social Research Methodology, 8, 19–32.
Arnold, G. W., Wollman, D. A., FitzPatrick, G. J., Prochaska, D., Holmberg, D. G., Su, D. H., Hefner Jr,
A. R., Golmie, N. T., Brewer, T. L., Bello, M. et al. (2010). NIST Framework and Roadmap for Smart
Grid Interoperability Standards, Release 1.0. Technical Report.
Aurilio, G., Gallo, D., Landi, C., Luiso, M., & Graditi, G. (2014). A low cost smart meter network for a
smart utility. In 2014 IEEE International Instrumentation and Measurement Technology Conference
(I2MTC) Proceedings (pp. 380–385). IEEE.
Barn, B., Barat, S., & Clark, T. (2017).
Conducting systematic literature reviews and systematic
mapping studies. In 10th Innovations in Software Engineering Conference (pp. 212–213). ACM.
Beidou, F. B., Morsi, W. G., Diduch, C. P., & Chang, L. (2010). Smart grid: Challenges, research
directions and possible solutions.
In The 2nd International Symposium on Power Electronics for
Distributed Generation Systems (pp. 670–673).
Besanger, Y., Tran, Q. T., Boudinnet, C., Nguyen, T. L., Brandl, R., Strasser, T. I. et al. (2017).
Using power-hardware-in-the-loop experiments together with co-simulation for the holistic validation
of cyber-physical energy systems. In Innovative Smart Grid Technologies Conference Europe (ISGT-
Europe), 2017 IEEE PES (pp. 1–6). IEEE.
Blochwitz, T., Otter, M., Arnold, M., Bausch, C., Clauß, C., Elmqvist, H., Junghanns, A., Mauss,
J., Monteiro, M., Neidhold, T. et al. (2011). The functional mockup interface for tool independent
exchange of simulation models. In Proceedings of the 8th International Modelica Conference (pp.
105–114). Link¨oping University Press.
Bruinenberg, J. et al. (2012). Smart grid reference architecture. CEN, CENELEC, ETSI, Tech. Rep, .
Buscher, M., Lehnhoﬀ, S., Rohjans, S., Andr´en, F., & Strasser, T. (2015). Using large-scale local and
cross-location experiments for smart grid system validation. In Industrial Electronics Society, IECON
2015-41st Annual Conference of the IEEE (pp. 004621–004626). IEEE.
Camus, B., Paris, T., Vaubourg, J., Presse, Y., Bourjot, C., Ciarletta, L., & Chevrier, V. (2016).
MECSYCO: a Multi-agent DEVS Wrapping Platform for the Co-simulation of Complex Systems.
Research Report LORIA, UMR 7503, Universit´e de Lorraine, CNRS, Vandoeuvre-l`es-Nancy ; Inria
Nancy - Grand Est (Villers-l`es-Nancy, France).
Cintuglu, M. H., Mohammed, O. A., Akkaya, K., & Uluagac, A. S. (2017). A survey on smart grid
cyber-physical system testbeds. IEEE Communications Surveys & Tutorials, 19, 446–464.
Ciraci, S., Daily, J., Fuller, J., Fisher, A., Marinovici, L., & Agarwal, K. (2014). Fncs: a framework for
power system and communication networks co-simulation. In Proceedings of the symposium on theory
of modeling & simulation-DEVS integrative (p. 36). Society for Computer Simulation International.
´Evora G´omez, J., Hern´andez Cabrera, J. J., Tavella, J.-P., Vialle, S., Kremers, E., & Frayssinet, L.
(2019).
Daccosim ng: co-simulation made simpler and faster.
In Link¨oping electronic conference
proceedings.
Fang, X., Misra, S., Xue, G., & Yang, D. (2011). Smart grid—the new and improved power grid: A
survey. IEEE communications surveys & tutorials, 14, 944–980.
Galtier, V., Vialle, S., Dad, C., Tavella, J.-P., Lam-Yee-Mui, J.-P., & Plessis, G. (2015). Fmi-based
distributed multi-simulation with daccosim. In Proceedings of the Symposium on Theory of Modeling
& Simulation: DEVS Integrative M&S Symposium (pp. 39–46).
Georg, H., M¨uller, S. C., Dorsch, N., Rehtanz, C., & Wietfeld, C. (2013).
Inspire: Integrated co-
simulation of power and ict systems for real-time evaluation. In 2013 IEEE International Conference
on Smart Grid Communications (SmartGridComm) (pp. 576–581). IEEE.
Goel, S., Hong, Y., Papakonstantinou, V., & Kloza, D. (2015). Smart grid security. Springer.
Gomes, C., Thule, C., Broman, D., Larsen, P. G., & Vangheluwe, H. (2017). Co-simulation: State of
the art. arXiv preprint arXiv:1702.00686, .
Gomes, C., Thule, C., Broman, D., Larsen, P. G., & Vangheluwe, H. (2018). Co-simulation: a survey.
ACM Computing Surveys (CSUR), 51, 49.
Hopkinson, K., Wang, X., Giovanini, R., Thorp, J., Birman, K., & Coury, D. (2006).
Epochs:
a
platform for agent-based electric power and communication simulation built from commercial oﬀ-the-
shelf components. IEEE Transactions on Power Systems, 21, 548–558.
Hwang, J., Choi, M.-i., Lee, T., Jeon, S., Kim, S., Park, S., & Park, S. (2017). Energy prosumer business
model using blockchain system to ensure transparency and safety. Energy Procedia, 141, 194–198.
IEEE (2010). Ieee standard for modeling and simulation (m&s) high level architecture (hla)– framework
and rules - redline. IEEE Std 1516-2010 (Revision of IEEE Std 1516-2000) - Redline, (pp. 1–38).
Law, A. M., Kelton, W. D., & Kelton, W. D. (2000).
Simulation modeling and analysis volume 3.
22


---

Page 23

---

McGraw-Hill New York.
Li, W., Monti, A., Luo, M., & Dougal, R. A. (2011). Vpnet: A co-simulation framework for analyzing
communication channel eﬀects on power systems. In 2011 IEEE Electric Ship Technologies Symposium
(pp. 143–149). IEEE.
Li, W., & Zhang, X. (2014). Simulation of the smart grid communications: Challenges, techniques, and
future trends. Computers & Electrical Engineering, 40, 270–288.
Li, W., Zhang, X., & Li, H. (2014). Co-simulation platforms for co-design of networked control systems:
An overview. Control Engineering Practice, 23, 44–56.
Lin, H., Veda, S. S., Shukla, S. S., Mili, L., & Thorp, J. (2012). Geco: Global event-driven co-simulation
framework for interconnected power system and communication network.
IEEE Transactions on
Smart Grid, 3, 1444–1456.
Luo, F., Dong, Z. Y., Liang, G., Murata, J., & Xu, Z. (2018). A distributed electricity trading system
in active distribution networks based on multi-agent coalition and blockchain. IEEE Transactions on
Power Systems, .
Mets, K., Ojea, J. A., & Develder, C. (2014). Combining power and communication network simulation
for cost-eﬀective smart grid analysis. IEEE Communications Surveys & Tutorials, 16, 1771–1796.
Mirkovic, J., & Benzel, T. (2012). Teaching cybersecurity with deterlab. IEEE Security & Privacy, 10,
73–76.
Mohd, A., Ortjohann, E., Schmelter, A., Hamsic, N., & Morton, D. (2008). Challenges in integrating
distributed energy storage systems into future smart grid. In 2008 IEEE international symposium on
industrial electronics (pp. 1627–1632). IEEE.
Nouidui, T. S., Coignard, J., Gehbauer, C., Wetter, M., Joo, J.-Y., & Vrettos, E. (2019). Cyder – an
fmi-based co-simulation platform for distributed energy resources. Journal of Building Performance
Simulation, 12, 566–579.
Palmintier, B., Krishnamurthy, D., Top, P., Smith, S., Daily, J., & Fuller, J. (2017). Design of the helics
high-performance transmission-distribution-communication-market co-simulation framework. In 2017
Workshop on Modeling and Simulation of Cyber-Physical Energy Systems (MSCPES) (pp. 1–6).
IEEE.
Petersen, K., Feldt, R., Mujtaba, S., & Mattsson, M. (2008). Systematic mapping studies in software
engineering. In EASE (pp. 68–77). volume 8.
Schloegl, F., Rohjans, S., Lehnhoﬀ, S., Velasquez, J., Steinbrink, C., & Palensky, P. (2015). Towards a
classiﬁcation scheme for co-simulation approaches in energy systems. In Smart Electric Distribution
Systems and Technologies (EDST), 2015 International Symposium on (pp. 516–521). IEEE.
Schvarcbacher, M., Hrabovsk´a, K., Rossi, B., & Pitner, T. (2018).
Smart grid testing management
platform (sgtmp). Applied Sciences, 8.
Schvarcbacher, M., & Rossi, B. (2017).
Smart Grids Co-Simulations with Low-Cost Hardware.
In
2017 43rd Euromicro Conference on Software Engineering and Advanced Applications (SEAA) (pp.
252–255).
Sch¨utte, S., Scherfke, S., & Tr¨oschel, M. (2011). Mosaik: A framework for modular simulation of active
components in smart grids. In 2011 IEEE First International Workshop on Smart Grid Modeling
and Simulation (SGMS) (pp. 55–60).
Steinbrink, C., van der Meer, A. A., Cvetkovic, M., Babazadeh, D., Rohjans, S., Palensky, P., & Lehnhoﬀ,
S. (2018a). Smart grid co-simulation with MOSAIK and HLA: a comparison study. Computer Science
- Research and Development, 33, 135–143.
Steinbrink, C., Schl¨ogl, F., Babazadeh, D., Lehnhoﬀ, S., Rohjans, S., & Narayan, A. (2018b). Future per-
spectives of co-simulation in the smart grid domain. In 2018 IEEE International Energy Conference
(Energycon) (pp. 1–6). IEEE.
Vogt, M., Marten, F., & Braun, M. (2018). A survey and statistical analysis of smart grid co-simulations.
Applied Energy, 222, 67–78.
Vykopal., J., Oslejsek., R., Celeda., P., Vizvary., M., & Tovarnak., D. (2017). Kypo cyber range: Design
and use cases. In Proceedings of the 12th International Conference on Software Technologies - Volume
1: ICSOFT, (pp. 310–321). INSTICC SciTePress.
Wang, W., & Lu, Z. (2013). Survey cyber security in the smart grid: Survey and challenges. Comput.
Netw., 57, 1344–1371.
Yi, T., Feng, L., Qi, W., Bin, C., & Ming, N. (2016). Overview of the co-simulation methods for power
and communication system.
In Real-time Computing and Robotics (RCAR), IEEE International
Conference on (pp. 94–98). IEEE.
Zaballos, A., Vallejo, A., & Selga, J. M. (2011). Heterogeneous communication architecture for the smart
grid. IEEE network, 25, 30–37.
23


---

Page 24

---

Zhang, J., & Chen, Z. (2010). The impact of ami on the future power system. Automation of Electric
Power Systems, 34, 20–23.
Reviewed Articles
Ahmad, I., Kazmi, J. H., Shahzad, M., Palensky, P., & Gawlik, W. (2015). Co-simulation framework
based on power system, AI and communication tools for evaluating smart grid applications. In 2015
IEEE Innovative Smart Grid Technologies - Asia (ISGT ASIA) (pp. 1–6).
Albagli, A. N., Falc˜ao, D. M., & de Rezende, J. F. (2016). Smart grid framework co-simulation using
HLA architecture. Electric Power Systems Research, 130, 22–33.
Alishov, R., Sp¨ahn, M., & Witzmann, R. (2016). Co-simulation architecture for centralised direct load
control in smart grid. In CIRED Workshop 2016 (pp. 1–4).
Amarasekara, B., Ranaweera, C., Nirmalathas, A., & Evans, R. (2015). Co-simulation platform for smart
grid applications. In 2015 IEEE Innovative Smart Grid Technologies - Asia (ISGT ASIA) (pp. 1–6).
Armendariz, M., Chenine, M., Nordstr¨om, L., & Al-Hammouri, A. (2014). A co-simulation platform for
medium/low voltage monitoring and control applications. In ISGT 2014 (pp. 1–5).
Awad, A., Bazan, P., & German, R. (2014). SGsim: A simulation framework for smart grid applications.
In 2014 IEEE International Energy Conference (ENERGYCON) (pp. 730–736).
Awad, A., Bazan, P., Kassem, R., & German, R. (2016). Co-simulation-based evaluation of volt-VAR
control. In 2016 IEEE PES Innovative Smart Grid Technologies Conference Europe (ISGT-Europe)
(pp. 1–6).
Ayon, V., Robinson, M., Mammoli, A., Fisher, A., & Fuller, J. (2017).
Integration of bottom-up
statistical models of loads on a residential feeder with the GridLAB-D distribution system simulator,
and applications. In 2017 IEEE PES Innovative Smart Grid Technologies Conference Europe (ISGT-
Europe) (pp. 1–6).
Barbierato, L., Estebsari, A., Pons, E., Pau, M., Salassa, F., Ghirardi, M., & Patti, E. (2018).
A
Distributed IoT Infrastructure to Test and Deploy Real-Time Demand Response in Smart Grids.
IEEE Internet of Things Journal, (p. 1).
Bhor, D., Angappan, K., & Sivalingam, K. M. (2016). Network and power-grid co-simulation framework
for Smart Grid wide-area monitoring networks. Journal of Network and Computer Applications, 59,
274–284.
Bian, D., Kuzlu, M., Pipattanasomporn, M., Rahman, S., & Wu, Y. (2015). Real-time co-simulation
platform using OPAL-RT and OPNET for analyzing smart grid performance. In 2015 IEEE Power
Energy Society General Meeting (pp. 1–5).
Bompard, E., Monti, A., Tenconi, A., Estebsari, A., Huang, T., Pons, E., Stevic, M., Vaschetto, S., &
Vogel, S. (2016). A multi-site real-time co-simulation platform for the testing of control strategies of
distributed storage and V2G in distribution networks. In 2016 18th European Conference on Power
Electronics and Applications (EPE’16 ECCE Europe) (pp. 1–9).
Bottura, R., Babazadeh, D., Zhu, K., Borghetti, A., Nordstr¨om, L., & Nucci, C. A. (2013). SITL and
HLA co-simulation platforms: Tools for analysis of the integrated ICT and electric power system. In
Eurocon 2013 (pp. 918–925).
Broderick, S., Cruden, A., Sharkh, S., & Bessant, N. (2017). Technique to interconnect and control
co-simulation systems. IET Generation, Transmission Distribution, 11, 3115–3124.
Bytschkow, D., Zellner, M., & Duchon, M. (2015). Combining SCADA, CIM, GridLab-D and AKKA for
smart grid co-simulation. In 2015 IEEE Power Energy Society Innovative Smart Grid Technologies
Conference (ISGT) (pp. 1–5).
Caire, R., S´anchez, J., & Hadjsaid, N. (2013). Vulnerability analysis of coupled heterogeneous critical
infrastructures: A Co-simulation approach with a testbed validation. In IEEE PES ISGT Europe
2013 (pp. 1–5).
Cao, Y., Shi, X., Li, Y., Tan, Y., Shahidehpour, M., & Shi, S. (2018). A Simpliﬁed Co-Simulation Model
for Investigating Impacts of Cyber-Contingency on Power System Operations. IEEE Transactions on
Smart Grid, 9, 4893–4905.
Celli, G., Garau, M., Ghiani, E., Pilo, F., & Corti, S. (2016). Co-simulation of ICT technologies for
smart distribution networks. In CIRED Workshop 2016 (pp. 1–5).
Chromik, J. J., Pilch, C., Brackmann, P., Duhme, C., Everinghoﬀ, F., Giberlein, A., Teodorowicz, T.,
Wieland, J., Haverkort, B. R., & Remke, A. (2017).
Context-aware local Intrusion Detection in
SCADA systems: A testbed and two showcases. In 2017 IEEE International Conference on Smart
Grid Communications (SmartGridComm) (pp. 467–472).
24


---

Page 25

---

Ciraci, S., Daily, J., Fuller, J., Fisher, A., Marinovici, L., & Agarwal, K. (2014). FNCS: A Framework
for Power System and Communication Networks Co-simulation. In Proceedings of the Symposium on
Theory of Modeling & Simulation - DEVS Integrative DEVS ’14 (pp. 36:1—-36:8). San Diego, CA,
USA: Society for Computer Simulation International.
Ding, Y., Morawietz, A., & Beigl, M. (2016).
Investigation of a grid-driven real-time pricing in a
simulation environment. In 2016 IEEE International Energy Conference (ENERGYCON) (pp. 1–6).
Duan, N., Yee, N., Salazar, B., Joo, J.-Y., Stewart, E., & Cortez, E. (2020). Cybersecurity analysis of
distribution grid operation with distributed energy resources via co-simulation. In 2020 IEEE Power
& Energy Society General Meeting (PESGM) (pp. 1–5). IEEE.
Duerr, S., Ababei, C., & Ionel, D. M. (2017). Load balancing with energy storage systems based on
co-simulation of multiple smart buildings and distribution networks. In 2017 IEEE 6th International
Conference on Renewable Energy Research and Applications (ICRERA) (pp. 175–180).
Fuller, J. C., Ciraci, S., Daily, J. A., Fisher, A. R., & Hauer, M. (2013). Communication simulations for
power system applications. In 2013 Workshop on Modeling and Simulation of Cyber-Physical Energy
Systems (MSCPES) (pp. 1–6).
Garau, M., Celli, G., Ghiani, E., Pilo, F., & Corti, S. (2017). Evaluation of Smart Grid Communication
Technologies with a Co-Simulation Platform. IEEE Wireless Communications, 24, 42–49.
Garau, M., Celli, G., Ghiani, E., Soma, G. G., Pilo, F., & Corti, S. (2015). ICT reliability modelling
in co-simulation of smart distribution networks. In 2015 IEEE 1st International Forum on Research
and Technologies for Society and Industry Leveraging a better tomorrow (RTSI) (pp. 365–370).
Georg, H., M¨uller, S. C., Dorsch, N., Rehtanz, C., & Wietfeld, C. (2013). INSPIRE: Integrated co-
simulation of power and ICT systems for real-time evaluation. In 2013 IEEE International Conference
on Smart Grid Communications (SmartGridComm) (pp. 576–581).
Godfrey, T., Mullen, S., Griﬃth, D. W., Golmie, N., Dugan, R. C., & Rodine, C. (2010). Modeling Smart
Grid Applications with Co-Simulation. In 2010 First IEEE International Conference on Smart Grid
Communications (pp. 291–296).
Gurusinghe, D. R., Menike, S., Konara, A., Rajapakse, A. D., Yahampath, P., Annakkage, U., Archer,
B. A., & Weekes, T. (2016). Co-simulation of power system and synchrophasor communication network
on a single simulation platform. Technology and Economics of Smart Grids and Sustainable Energy,
1, 6.
Hammad, E., Ezeme, M., & Farraj, A. (2019).
Implementation and development of an oﬄine co-
simulation testbed for studies of power systems cyber security and control veriﬁcation. International
Journal of Electrical Power & Energy Systems, 104, 817–826.
Hess, T., Dickert, J., & Schegner, P. (2016). Multivariate power ﬂow analyses for smart grid applications
utilizing Mosaik. In 2016 IEEE PES Innovative Smart Grid Technologies Conference Europe (ISGT-
Europe) (pp. 1–6).
Huang, R., Fan, R., Daily, J., Fisher, A., & Fuller, J. (2017). Open-source framework for power system
transmission and distribution dynamics co-simulation. IET Generation, Transmission Distribution,
11, 3152–3162.
Johnstone, K., Blair, S. M., Syed, M. H., Emhemed, A., Burt, G. M., & Strasser, T. I. (2017). Co-
simulation approach using PowerFactory and MATLAB/Simulink to enable validation of distributed
control concepts within future power systems. CIRED - Open Access Proceedings Journal, 2017,
2192–2196.
Kazmi, J. H., Latif, A., Ahmad, I., Palensky, P., & Gawlik, W. (2016).
A ﬂexible smart grid co-
simulation environment for cyber-physical interdependence analysis. In 2016 Workshop on Modeling
and Simulation of Cyber-Physical Energy Systems (MSCPES) (pp. 1–6).
Kelley, B. M., Top, P., Smith, S. G., Woodward, C. S., & Min, L. (2015). A federated simulation toolkit
for electric power grid and communication network co-simulation. In 2015 Workshop on Modeling
and Simulation of Cyber-Physical Energy Systems (MSCPES) (pp. 1–6).
Kosek, A. M., L¨unsdorf, O., Scherfke, S., Gehrke, O., & Rohjans, S. (2014). Evaluation of smart grid
control strategies in co-simulation — integration of IPSYS and mosaik.
In 2014 Power Systems
Computation Conference (pp. 1–7).
Kounev, V., Tipper, D., Levesque, M., Grainger, B. M., Mcdermott, T., & Reed, G. F. (2015).
A
microgrid co-simulation framework. In 2015 Workshop on Modeling and Simulation of Cyber-Physical
Energy Systems (MSCPES) (pp. 1–6).
Lai, L. L., Shum, C., Wang, L., Lau, W. H., Tse, N., Chung, H., Tsang, K. F., & Xu, F. (2014). Design
a co-simulation platform for power system and communication network. In 2014 IEEE International
Conference on Systems, Man, and Cybernetics (SMC) (pp. 3036–3041).
Latif, A., Khan, S., Palensky, P., & Gawlik, W. (2016). Co-simulation based platform for thermostatically
25


---

Page 26

---

controlled loads as a frequency reserve. In 2016 Workshop on Modeling and Simulation of Cyber-
Physical Energy Systems (MSCPES) (pp. 1–6).
Latif, A., Shahzad, M., Palensky, P., & Gawlik, W. (2015). An alternate PowerFactory Matlab coupling
approach. In 2015 International Symposium on Smart Electric Distribution Systems and Technologies
(EDST) (pp. 486–491).
Lau, W. H., Shum, S., Lam, R., Chung, H., Tse, N. C. F., & Lai, L. L. (2012). The development of
a smart grid and communication co-simulator. In 9th IET International Conference on Advances in
Power System Control, Operation and Management (APSCOM 2012) (pp. 1–6).
Lehnhoﬀ, S., Nannen, O., Rohjans, S., Schlogl, F., Dalhues, S., Robitzky, L., Hager, U., & Rehtanz, C.
(2015). Exchangeability of power ﬂow simulators in smart grid co-simulations with mosaik. In 2015
Workshop on Modeling and Simulation of Cyber-Physical Energy Systems (MSCPES) (pp. 1–6).
L´evesque, M., Xu, D. Q., Jo´os, G., & Maier, M. (2012). Communications and power distribution network
co-simulation for multidisciplinary smart grid experimentations. In Simulation Series (pp. 55–61).
volume 44.
Li, X., Huang, Q., & Wu, D. (2017). Distributed Large-Scale Co-Simulation for IoT-Aided Smart Grid
Control. IEEE Access, 5, 19951–19960.
Liberatore, V., & Al-Hammouri, A. (2011). Smart grid communication and co-simulation. In IEEE 2011
EnergyTech (pp. 1–5).
Lin, H., Deng, Y., Shukla, S., Thorp, J., & Mili, L. (2012a).
Cyber security impacts on all-PMU
state estimator - a case study on co-simulation platform GECO. In 2012 IEEE Third International
Conference on Smart Grid Communications (SmartGridComm) (pp. 587–592).
Lin, H., Sambamoorthy, S., Shukla, S., Thorp, J., & Mili, L. (2011). Power system and communication
network co-simulation for smart grid applications. In ISGT 2011 (pp. 1–6).
Lin, H., Veda, S. S., Shukla, S. S., Mili, L., & Thorp, J. (2012b). GECO: Global Event-Driven Co-
Simulation Framework for Interconnected Power System and Communication Network. IEEE Trans-
actions on Smart Grid, 3, 1444–1456.
Liu, Z., Wang, Q., Tang, Y., & Ni, M. (2018). The Real-Time Co-Simulation Platform with Hardware-
in-Loop for Cyber-Attack in Smart Grid. In 2018 IEEE Innovative Smart Grid Technologies - Asia
(ISGT Asia) (pp. 845–849).
Makhmalbaf, A., Fuller, J., Srivastava, V., Ciraci, S., & Daily, J. (2014).
Co-simulation of detailed
whole building with the power system to study smart grid applications. In 2014 IEEE Conference on
Technologies for Sustainability (SusTech) (pp. 192–198).
Mallapuram, S., Yu, W., Moulema, P., Griﬃth, D., Golmie, N., & Liang, F. (2017). An Integrated Sim-
ulation Study on Reliable and Eﬀective Distributed Energy Resources in Smart Grid. In Proceedings
of the International Conference on Research in Adaptive and Convergent Systems RACS ’17 (pp.
140–145). New York, NY, USA: ACM.
Mirtaheri, H., Chicco, G., del Razo, V., & Jacobsen, H. (2016). A framework for control and co-simulation
in distribution networks applied to electric vehicle charging with Vehicle-Originating-Signals. In 2016
IEEE International Energy Conference (ENERGYCON) (pp. 1–6).
Mittal, S., Ruth, M., Pratt, A., Lunacek, M., Krishnamurthy, D., & Jones, W. (2015). A System-of-
systems Approach for Integrated Energy Systems Modeling and Simulation. In Proceedings of the
Conference on Summer Computer Simulation SummerSim ’15 (pp. 1–10).
San Diego, CA, USA:
Society for Computer Simulation International.
Mosshammer, R., Kupzog, F., Faschang, M., & Stifter, M. (2013). Loose coupling architecture for co-
simulation of heterogeneous components. In IECON 2013 - 39th Annual Conference of the IEEE
Industrial Electronics Society (pp. 7570–7575).
Moulema, P., Yu, W., Griﬃth, D., & Golmie, N. (2015). On Eﬀectiveness of Smart Grid Applications
Using Co-Simulation.
In 2015 24th International Conference on Computer Communication and
Networks (ICCCN) (pp. 1–8).
M¨uller, S. C., Georg, H., Rehtanz, C., & Wietfeld, C. (2012). Hybrid simulation of power systems and
ICT for real-time applications. In 2012 3rd IEEE PES Innovative Smart Grid Technologies Europe
(ISGT Europe) (pp. 1–7).
Nannen, O., Piech, K., Lehnhoﬀ, S., Rohjans, S., Schl¨ogl, F., Velasquez, J., Andren, F., & Strasser, T.
(2015). Low-cost integration of hardware components into co-simulation for future power and energy
systems. In IECON 2015 - 41st Annual Conference of the IEEE Industrial Electronics Society (pp.
5304–5309).
Nguyen, V. H., Besanger, Y., Tran, Q. T., Boudinnet, C., Nguyen, T. L., Brandl, R., & Strasser, T. I.
(2017). Using power-hardware-in-the-loop experiments together with co-simulation for the holistic
validation of cyber-physical energy systems. In 2017 IEEE PES Innovative Smart Grid Technologies
26


---

Page 27

---

Conference Europe (ISGT-Europe) (pp. 1–6).
Ni, M., Xue, Y., Tong, H., & Li, M. (2018). A cyber physical power system co-simulation platform.
In 2018 Workshop on Modeling and Simulation of Cyber-Physical Energy Systems (MSCPES) (pp.
1–5).
Otte, M., Leimgruber, F., Br¨undlinger, R., Rohjans, S., Latif, A., & Strasser, T. I. (2018). Hardware-
in-the-Loop Co-Simulation Based Validation of Power System Control Applications. In 2018 IEEE
27th International Symposium on Industrial Electronics (ISIE) (pp. 1229–1234).
Palensky, P., Widl, E., Stifter, M., & Elsheikh, A. (2013). Modeling Intelligent Energy Systems: Co-
Simulation Platform for Validating Flexible-Demand EV Charging Management. IEEE Transactions
on Smart Grid, 4, 1939–1947.
Pan, K., Teixeira, A., L´opez, C. D., & Palensky, P. (2017). Co-simulation for cyber security analysis:
Data attacks against energy management system. In 2017 IEEE International Conference on Smart
Grid Communications (SmartGridComm) (pp. 253–258).
Pan, Z., Xu, Q., Chen, C., & Guan, X. (2016). NS3-MATLAB co-simulator for cyber-physical systems
in smart grid. In 2016 35th Chinese Control Conference (CCC) (pp. 9831–9836).
Ravikumar, G., Ramya, G., Misra, S., Brahma, S., & Khaparde, S. A. (2017). iPaCS: An integrative
power and cyber systems co-simulation framework for smart grid. In 2017 IEEE Power Energy Society
General Meeting (pp. 1–5).
Razaq, A., Pranggono, B., Tianﬁeld, H., & Yue, H. (2015).
Simulating smart grid: Co-simulation
of power and communication network. In 2015 50th International Universities Power Engineering
Conference (UPEC) (pp. 1–6).
Roche, R., Natarajan, S., Bhattacharyya, A., & Suryanarayanan, S. (2012).
A Framework for Co-
simulation of AI Tools with Power Systems Analysis Software. In 2012 23rd International Workshop
on Database and Expert Systems Applications (pp. 350–354).
Sadi, M. A. H., Ali, M. H., Dasgupta, D., Abercrombie, R. K., & Kher, S. (2015).
Co-Simulation
Platform for Characterizing Cyber Attacks in Cyber Physical Systems. In 2015 IEEE Symposium
Series on Computational Intelligence (pp. 1244–1251).
Saxena, N., Chukwuka, V., Xiong, L., & Grijalva, S. (2017). CPSA: A Cyber-Physical Security As-
sessment Tool for Situational Awareness in Smart Grid. In Proceedings of the 2017 Workshop on
Cyber-Physical Systems Security and PrivaCy CPS ’17 (pp. 69–79). New York, NY, USA: ACM.
Schloegl, F., Buescher, M., Diwold, K., Lehnhoﬀ, S., Fischer, L., Zeilinger, F., & Gawron-Deutsch, T.
(2016). Performance testing Smart Grid applications using a distributed co-simulation approach. In
IECON 2016 - 42nd Annual Conference of the IEEE Industrial Electronics Society (pp. 6305–6310).
Shum, C., Lau, W., Mao, T., Chung, H. S., Tsang, K., Tse, N. C., & Lai, L. L. (2018). Co-Simulation of
Distributed Smart Grid Software Using Direct-Execution Simulation. IEEE Access, 6, 20531–20544.
Shum, C., Lau, W. H., Lam, K. L., He, Y., Chung, H., Tse, N. C. F., Tsang, K. F., & Lai, L. L.
(2013). The development of a smart grid co-simulation platform and case study on Vehicle-to-Grid
voltage support application. In 2013 IEEE International Conference on Smart Grid Communications
(SmartGridComm) (pp. 594–599).
Stefanov, A., & Liu, C. (2012). ICT modeling for integrated simulation of cyber-physical power systems.
In 2012 3rd IEEE PES Innovative Smart Grid Technologies Europe (ISGT Europe) (pp. 1–8).
Stevic, M., Li, W., Ferdowsi, M., Benigni, A., Ponci, F., & Monti, A. (2013). A two-step simulation
approach for joint analysis of power systems and communication infrastructures. In IEEE PES ISGT
Europe 2013 (pp. 1–5).
Stifter, M., Widl, E., Andr´en, F., Elsheikh, A., Strasser, T., & Palensky, P. (2013). Co-simulation of
components, controls and power systems based on open source software. In 2013 IEEE Power Energy
Society General Meeting (pp. 1–5).
Sun, X., Chen, Y., Liu, J., & Huang, S. (2014). A co-simulation platform for smart grid considering
interaction between information and power systems.
In 2014 IEEE PES Innovative Smart Grid
Technologies Conference, ISGT 2014.
Syed, M. H., Crolla, P., Burt, G. M., & Kok, J. K. (2015).
Ancillary service provision by demand
side management: A real-time power hardware-in-the-loop co-simulation demonstration.
In 2015
International Symposium on Smart Electric Distribution Systems and Technologies (EDST) (pp.
492–498).
Tariq, M. U., Swenson, B. P., Narasimhan, A. P., Grijalva, S., Riley, G. F., & Wolf, M. (2014). Cyber-
physical Co-simulation of Smart Grid Applications Using Ns-3. In Proceedings of the 2014 Workshop
on Ns-3 WNS3 ’14 (pp. 8:1—-8:8). New York, NY, USA: ACM.
Troiano, G. O., Ferreira, H. S., Trindade, F. C. L., & Ochoa, L. F. (2016). Co-simulator of power and
communication networks using OpenDSS and OMNeT++. In 2016 IEEE Innovative Smart Grid
27


---

Page 28

---

Technologies - Asia (ISGT-Asia) (pp. 1094–1099).
Venkataramanan, V., Srivastava, A., & Hahn, A. (2016). Real-time co-simulation testbed for microgrid
cyber-physical analysis. In 2016 Workshop on Modeling and Simulation of Cyber-Physical Energy
Systems (MSCPES) (pp. 1–6).
Vogt, M., Marten, F., L¨ower, L., Horst, D., Brauns, K., Fetzer, D., Menke, J., Troncia, M., Hegemann,
J., T¨obermann, C., & Braun, M. (2015). Evaluation of interactions between multiple grid operators
based on sparse grid knowledge in context of a smart grid co-simulation environment. In 2015 IEEE
Eindhoven PowerTech (pp. 1–6).
Wang, Q., Tai, W., Tang, Y., Liang, Y., Huang, L., & Wang, D. (2017). Architecture and Application
of Real-time Co-simulation Platform for Cyber-physical Power System. In 2017 IEEE 7th Annual
International Conference on CYBER Technology in Automation, Control, and Intelligent Systems
(CYBER) (pp. 81–85).
Zhao, C., Cao, H., Zhu, P., & Pan, Y. (2013).
A CO-simulation platform for simulating cascading
failures in smart grid. In Proceedings of 2013 3rd International Conference on Computer Science and
Network Technology (pp. 630–634).
28
