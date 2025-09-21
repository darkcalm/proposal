# Operational Issues of Contemporary Distribution Systems- A Review on Recent and Emerging Concern

## Paper Metadata

- **Filename:** Operational Issues of Contemporary Distribution Systems- A Review on Recent and Emerging Concern.pdf
- **DOI:** None
- **Authors:** Not available
- **Year:** Not available
- **Journal/Venue:** Not available
- **URL:** Not available
- **Extraction Date:** 2025-06-03T15:04:08.743089
- **Total Pages:** 21

## Abstract

Abstract not available from BibTeX metadata.

## Keywords

Keywords not available from BibTeX metadata.

---

## Full Text Content



### Page 1

Citation: Loji, K.; Sharma, S.; Loji, N.;
Sharma, G.; Bokoro, P.N. Operational
Issues of Contemporary Distribution
Systems: A Review on Recent and
Emerging Concerns. Energies 2023, 16,
1732. https://doi.org/10.3390/
en16041732
Academic Editors: Tek Tjing Lie and
Yogendra Arya
Received: 22 October 2022
Revised: 28 January 2023
Accepted: 6 February 2023
Published: 9 February 2023
Copyright:
© 2023 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed
under
the
terms
and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).
energies
Review
Operational Issues of Contemporary Distribution Systems:
A Review on Recent and Emerging Concerns
Kabulo Loji 1,2, Sachin Sharma 3, Nomhle Loji 1, Gulshan Sharma 2,*
and Pitshou N. Bokoro 2
1
Department of Electrical Power Engineering, Durban University of Technology, Durban 4001, South Africa
2
Department of Electrical Engineering Technology, University of Johannesburg,
Johannesburg 2006, South Africa
3
Department of Electrical Engineering, Graphic Era Deemed to be University, Dehradun 248002, India
*
Correspondence: gulshans@uj.ac.za
Abstract: Distribution systems in traditional power systems (PS) constituted of passive elements and
the distribution issues were then limited to voltage and thermal constraints, harmonics, overloading
and unbalanced loading, reactive power compensation issues, faults and transients, loss minimization
and frequency stability problems, to name a few. Contemporary distribution systems are becoming
active distributed networks (ADNs) that integrate a substantially increasing amount of distributed
energy resources (DERs). DERS include distributed generation (DG) sources, energy storage resources
and demand side management (DSM) options. Despite their evidenced great beneﬁts, the largescale deployment and integration of DERs remain a challenge as they subsequently lead to the
network operational and efﬁciency issues, hampering PS network reliability and stability. This paper
carries out a comprehensive literature survey based on the last decade’s research on operational
challenges reported and focusing on dispatchable and non-dispatchable DGs grid integration, on
various demand response (DR) mechanisms and, on battery energy storage system (BESS) charging
and discharging challenges, with the aim to pave the way to developing suitable optimization
techniques that will solve the coordination of multiple renewable sources, storage systems and DRs
to minimize distribution systems’ operational issues and thus improve stability and reliability. This
paper’s ﬁndings assist the researchers in the ﬁeld to conduct further research and to help PS planners
and operators decide on appropriate relevant technologies that address challenges inherent to DG
grid integration.
Keywords: demand response strategies; demand side management; distributed energy resources;
battery energy storage systems; distribution generation; operational challenges; optimization techniques
1. Introduction
1.1. Traditional vs. Contemporary PS Networks
From the ﬁrst built PS network, more than 100 years have seen a huge development of
the electricity generation and supply systems. Points of generation of electric power were
indeed situated several kilometres away from points of consumption as shown in Figure 1,
since for economic reasons and a secure supply of electrical power, long distance bulk
power transfer was essential [1]. Until the 1990s, the electric power industry was inclined
to have a vertical integration approach to generation and transmission, justiﬁed mostly
by economic reasons as mentioned above, rather than the improvement of the overall
efﬁciency/reliability of the system [2].
The quasi-increasing amount of diverse electrical nature’s loads over time resulted
in the change of the grid topology, prompting grid complexity growth as illustrated in
Figure 2, requiring much more attention on PS operational issues than ever. Current
transformations have been driven for the last two decades by the increasing integration
of renewable energy sources (RES), particularly solar and wind sources, known for their
intermittency and unpredictability, into national grids.
Energies 2023, 16, 1732. https://doi.org/10.3390/en16041732
https://www.mdpi.com/journal/energies

---


### Page 2

Energies 2023, 16, 1732
2 of 21
 
Figure 1. Traditional PS network topology.
 
Figure 2. Contemporary network topology [3].
These transformations, commonly referred to as Smart Grid (SG), provide a combination of electrical power infrastructure with modern distributed computing facilities
and communication networks [4]. Interest in RES grid integration has indeed developed
because of the exponentially increasing demand for power delivery, a more secure energy
future and energy policies adopted by governments in an effort to reduce CO2 and greenhouse gas emissions [5–7]. Integration of renewable DGs, the most popular of them being
solar and wind, into PS has positive and negative impacts on both power utilities and
customers. Indeed, RES grid integration has evidenced substantial technical, environmental
and economic beneﬁts but at the same time, their increasing penetration leads to technical
issues such as reverse energy ﬂow from the customer end back into the transmission system [4], with negligible or reduced reactive power contribution [8,9]. One essential criterion
for PS stability is to continuously balance power generation and consumption. Since for
various reasons, the demand is volatile, generation must be ﬂexible to accommodate the
demand at any time [10]. The need to curtail consumers’ peak hours and ﬁll the gap caused
by the mismatch between the amount of power generated and consumed at a speciﬁc time
has become a very challenging task [11] for PS network researchers and operators.
1.2. Wind and PV Solar Trends and Contribution to Global Energy
The wind and solar-based RES footprint has been growing rapidly as shown in Table 1.
Data extracted from the U.S. Energy Information Administration (EIA) indicate that from
2011 the global energy production increased by 28.59 % over a period of 10 years [12].
From a 2.36 % contribution to the global energy production in 2011, the combined solar
PV and wind energy production has reached 10.41 % contribution to the world electricity
generation in 2021.

---


### Page 3

Energies 2023, 16, 1732
3 of 21
Table 1. Solar PV and wind electricity generation growth from 2011 to 2021.
Energy Source/Activity
2011
2016
2021
Total Generation [billion k Wh]
21,226
23,971
27,295
Solar [billion k Wh]
66
341
1035
Wind [billion k Wh]
435
957
1808
According to the International Renewable Energy Agency (IRENA), it is projected that
in the next three decades, about 65% of the world energy will be produced from RES as
shown in Figure 3 [13]. Consequently, the complexity of distribution issues will continue to
grow with the increase of the number of DERs and micro grids (MG), especially because
of the fact that most solar is connected to the DS rather than to the transmission system.
PS networks will continue to encounter numerous variabilities, affecting fundamentally
the planning and the operation of the electric distribution system, both technically and
economically, prompting on one side the upgrade of the aging electricity infrastructure
and on the other side, a subsequent transformation of the PS into Smart Grid (SG) process
otherwise referred to as Grid modernisation. Uluski et al. in [14] project that the next
generation distribution management shall need to incorporate more intelligence and advanced functionality to support these changes in the operation, monitoring and control of
the distribution grid.
 
Figure 3. Renewable energy shares in the total ﬁnal energy consumption [13].
1.3. DS Grid-Integration Challenges
DS Grid-integration challenges can be categorised into technical and non-technical.
Technical challenges can be subdivided into operational and non-operational challenges.
Operational challenges may be described as those pertaining to the hindrance of accomplishing the PS’s main functions of secured and efﬁcient generation, transmission and delivery of
quality and reliable power. These may include actions or/and decisions taken timeously by
PS operators to assure and maintain satisfactory PS operation. Non-operational challenges
may be termed as those related to particularly the planning and the design activities that
are initiated to minimize operational challenges. Non-technical challenges are essentially
socio-economic and environmental challenges. Only operational challenges will be considered in this review paper. Figure 4 provides a comprehensive and up to date categorization
of DG challenges.

---


### Page 4

Energies 2023, 16, 1732
4 of 21
 
Figure 4. Categorization of DS grid integration challenges.
In order to approach those emerging challenges and address them efﬁciently, the
authors in Ref. [15] suggest that both evolutionary and revolutionary technological changes
would be required together with grid-integration technologies and techniques as well as
substantial ﬁnancial resources and strategies. The severity impact of the challenges resides
mainly in:
•
The difﬁculty to predict the system behaviour due to the fact that the optimal distribution network solutions must include the types of DG technologies, with their
associated intricacies such as climatic conditions dependency and power generation compatibility.
•
Higher penetration and inappropriate accommodation of DGs can jeopardise the
system’s protection and coordination and ultimately lead to system instability and
excessive network losses [16,17].
•
Energy storage capacity and location [18].
•
Load demand scenarios and DR strategies for maximum possible utility and consumers’ beneﬁts.
2. Research Methodology and Organization of the Paper
2.1. Paper Methodology
Research data were collected using various search libraries with the major ones including IEEE Xplore, MDPI, Science Direct, Springer Link and Wiley Online Library. Figure 5
presents the summary of the data collection distribution from various sources used with the
most relevant information coming from the IEEE Xplore. The category “others” included
Elsevier, the National Renewable Energy Laboratory (NREL), Research gate and Google
Scholar, particularly by searching up on pre-selected authors from the major libraries
mentioned above. Six keywords were used to search for the data, namely: “Distribution
systems issues”, “Distributed Energy resources: review”, “Review on operational issues
on DS”, “Renewable energy optimization techniques and objectives: review” and “Smart
Grids”. The search was conducted and ﬁnalized using a three-level ﬁltering process for
each search library as follows:

---


### Page 5

Energies 2023, 16, 1732
5 of 21
•
Step 1: Relevance: using the above-mentioned keywords, run the search and obtain journal and conference papers that match the searching keywords. A total of
168 articles deemed to be relevant were collected at this stage.
•
Step 2: Year of publication: from previous ﬁlter level results, only research papers of the
last decade were selected, and 41 papers were excluded from step 1 selection. However,
due to their strong relevance and valuable contribution to the topic in discussion,
17 papers out of this selection, published between 1994 and 2011 were rescued from the
exclusion [1,2,6,19–28]. Figure 6 provides the collected data breakdown’s distribution
based on the year of publication.
•
Step 3: Titles and abstracts: the last step was concerned with ﬁltering using paper
titles and abstracts.

Figure 5. Distribution of collected data with reference to sources used.
0
5
10
15
20
Number of references consulted
Year of publication
Distribution of collected data based on the year of 
publication
Figure 6. Distribution of collected data based on the year of publication.
2.2. Contributions of the Paper
The prime drive of this paper is to discuss and summarize various reported concerns
on DS operational issues due to renewable energy grid integration and available remedies
thus far. The main contributions of this article are:
•
The paper reviews and presents DG grid integration challenges with regards to technoeconomic aspects. The challenges addressed include intermittency and the no-dispatchability of RES, network power quality, stability and reliability, electricity market
penetration and (de)regulation.
•
Existing solutions and strategies are aggregated, packaged and presented in ready-touse formats that are simple to refer to. The discussed solutions include DR strategies,
charging and discharging techniques of battery energy storage, optimization techniques used for DERs in smart grids, coordination of multiple renewable sources,
storage systems and DRs to minimize distribution systems’ operational issues.

---


### Page 6

Energies 2023, 16, 1732
6 of 21
•
The ﬁndings of this research paper will assist fellow PS renewable energy scholars and
researchers to undertake further investigations and development in the ﬁeld.
The rest of the paper is structured as follows: Section 3 highlights technical aspects of
RE grid integration challenges with emphasis on DS grid integration operational challenges.
Section 4 discusses the current status of solution strategies to overcome these challenges
while identifying all possible gaps in the implementation of the strategies. Section 5 presents
and discusses the conclusions as well as some future research directions that are corollary
to the discussions.
3. Highlights of RES Grid-Integration Challenges
3.1. Review of Past Reviews on DS Issues
For more than a decade, DGs grid integration challenges have been the subjects of
research surveys from several authors with numerous operational issues substantially
reviewed. As earlier as 2009, Basso in Ref. [29] amongst others, documented and evaluated through a National Renewable Energy Laboratory (NREL) report, system impacts
of DG penetration into transmission and distribution systems with a focus on renewable
distributed resources technologies. The objectives of the report were to identify: (1) critical
impact areas on transmission and distribution systems, (2) the best practices studies and
challenge mitigation techniques related to the resolution of the system impacts, as well as
(3) the then challenges and needs for further development to improve DG grid penetration.
In [29], the author suggests that system impacts be categorised under the following headings: voltage regulation, power quality, voltage and system frequency stability, protection
coordination, grounding, unintentional DG islanding, special issues related to DGs on
secondary distribution network systems and special issues related to RES. Adding to the
above categories, Prakash and Darbari in Ref. [30] spotted the development of secured
and trusted system as a critical issue and identiﬁed the following security critical issues:
methodologies to assess the security level of any system and monitoring of the system security including the development of security matrices, implementation of novel techniques
for secure data communications, application of middle ware in DS security and applications of web services in security purposes. With solar and wind energy suppliers ramping
up their energy capacity, Palmintier et al. [15] identiﬁed and reported further emerging
challenges of concern, namely reverse power ﬂow, increased duty on line regulators leading
to equipment wear and tear, variability due weather uncertainty and capacitor switching.
In the last past ﬁve years, research and the need for further development to improve DG
grid penetration have been focussing on system efﬁciency, optimal planning and optimal
integration. Researchers’ attention is being drawn particularly on the following concerns:
optimization techniques under various scenarios to enable higher penetration capacity,
DSM and DR [31], energy storage systems to improve reliability, communication protocols,
and cyber security. There is a general consensus that RES grid integration is an ongoing
ﬁeld for investigation and to respond to the anticipated RER integration challenges highlighted above, PS researchers propose advanced technologies and solution methodologies
that will be discussed later in the paper.
The literature review conducted in this paper considered a number of relevant previous
review papers that cover speciﬁc areas of DS challenges associated with DG grid-integration
such as: reviews on DG penetration issues [15,32–38], ﬂexibility issues in DS [10,39,40],
protection issues [16,17,41,42], voltage stability and voltage regulation [43–46], uncertainty
analysis and assessment [47,48], DR programs and DSM [31,49–53], unintentional islanding [54], cyber security issues [4,30], islanding [54], and vehicle grid system integration
and applications [55–57]. Table 2 provides a comprehensive summary of the review papers
samples used for the literature review of this paper.

---


### Page 7

Energies 2023, 16, 1732
7 of 21
Table 2. Sample review papers considered in the literature review.
Review Aspect
Paper Title
Ref.
Penetration issues
On the Path to Sun Shot: Emerging issues and Challenges in
Integrating Solar with the Distribution System
[15]
Integration of renewable distributed generators into the
distribution system: a review
[32]
Integrating Variable Renewable Energy: Challenges and
Solutions
[33]
Distributed generation: A review of factors that can contribute
most to achieve a scenario of DG units embedded in the new
distribution networks
[34]
On the Path to Sun Shot: Emerging issues and Challenges in
Integrating High Levels of Solar into the Electrical Generation
and Transmission System
[35]
A critical review of the integration of renewable energy sources
with various technologies,
[36]
Photovoltaic penetration issues and impacts in distribution
network—A review
[37]
Grid Integration Challenges and Solution Strategies for Solar
PV Systems: A Review
[38]
Flexibility issues in DS
Research and Practice of Flexibility in Distribution Systems: A
Review
[10]
A review of demand side ﬂexibility potential in Northern
Europe
[40]
Aggregation of Demand-Side Flexibilities: A Comparative
Study of Approximation Algorithms
[39]
Wind and hybrid-systems operational issues
Solar–wind hybrid renewable energy system: A review
[58]
Hybrid renewable energy systems for off-grid electric power:
Review of substantial issue
[59]
Wind Resources and Future Energy Security: Environmental,
Social, and Economic Issues,
[60]
Protection issues
Renewable Energy Integration Challenge on Power System
Protection and its Mitigation for Reliable Operation
[16]
Renewable distributed generation: The hidden challenges—A
review from protection perspective
[17]
A comprehensive review on issues, investigations, control and
protection trends, technical challenges and future directions for
Microgrid technology
[41]
A review of protection systems for distribution networks
embedded with renewable generation
[42]
Voltage stability and voltage regulation
Voltage Stability Analysis with High Distributed Generation
(DG) Penetration,
[43]
A comprehensive review of the voltage stability indices
[44]
Impact of distributed generation on protection and voltage
regulation of distribution systems: A review
[45]
Grid-connected photovoltaic system in Malaysia: A review on
voltage issues,
[46]
DR programs and DSM strategies
Survey on Demand Response Programs in Smart Grids: Pricing
Methods and Optimization Algorithms
[31]
Residential peak electricity demand response—Highlights of
some behavioural issues
[49]
Particle Swarm Optimization in Residential Demand-Side
Management: A Review on Scheduling and Control Algorithms
for Demand Response Provision
[50]
Residential Sector Demand Side Management: A Review
[51]
A Survey of Efﬁcient Demand-Side Management Techniques for
the Residential Appliance Scheduling Problem in Smart Homes
[52]
A review on price-driven residential demand response,
[53]

---


### Page 8

Energies 2023, 16, 1732
8 of 21
Table 2. Cont.
Review Aspect
Paper Title
Ref.
Vehicles grid system integration and
applications
Comprehensive review & impact analysis of integrating
projected electric vehicle charging load to the existing low
voltage distribution system
[56]
A comprehensive analysis of Vehicle to Grid (V2G) systems and
scholarly literature on the application of such systems,
[55]
A review on the state-of-the-art technologies of electric vehicle,
its impacts and prospects
[57]
Unintentional Islanding
A review on islanding operation and control for distribution
network connected with small hydro power plant
[54]
3.2. Impacts of Operational Challenges
The power output of most dominant DG resources is dependent on weather conditions, making these resources characterized by a variable generation property [38,61] that
constitutes its own challenge. In traditional grids, operational uncertainties usually result
from the demand side only. Distributed energy sources (DES) grid integration introduces
new challenges, as the operational uncertainties emanate from both the demand and the
generation sides [38] and have consequently signiﬁcant impact on optimal planning of
DGs [62]. Beside the technical considerations, Liu et. al. in Ref. [63] warn that these
uncertainties can inﬂuence electricity users’ economic beneﬁts. Shaﬁullah et al. [38] note
that accurate prediction of PV power for instance, has become an essential task for safe and
stable PS operation and the prediction can focus on energy output or rate of change. The
prediction types depend on the tools and information available from the meteorological
stations. Ref. [38] also present the prediction models that were developed by [64,65]. Recent reported models for the prediction of power output are based on machine learning
techniques as presented in Refs. [66–68].
The following challenges have been highlighted and dealt with by several researchers
worldwide:
•
Design and sizing of the system [5,15,32,33,47,69–74];
•
Power balancing and voltage stability [7,43,69,71,75–78];
•
Optimal energy management [11,79–94];
•
Optimal DG allocation and penetration level [8,9,16,34,38,69,71,90,95–98];
•
System cost minimization [22,82,99];
•
Energy storage: operation strategies, coordination, optimization;
•
Optimal coordination of various DERs [62,80,92,100–103];
•
Localized overloading due to electric vehicle chargers [55,56,104].
Table 3 provides some references addressing design and integration, power quality
and voltage stability, protection coordination, optimal distributed generation allocation,
level of penetration as well as energy storage issues.
Table 3. Sample of some references and issues that they are addressing.
Ref.
Design and
Integration of the
System
Power Quality and
Voltage Stability
Protection
Coordination
Optimal DG
Allocation
Penetration
Energy Storage
[5]


[43]



[69]


[98]


[33]

[7]


[8]


[16]




---


### Page 9

Energies 2023, 16, 1732
9 of 21
Table 3. Cont.
Ref.
Design and
Integration of the
System
Power Quality and
Voltage Stability
Protection
Coordination
Optimal DG
Allocation
Penetration
Energy Storage
[38]

[45]




[71]



[105]



[106]


4. Solutions Strategies for DS Grid Integration
To overcome the above challenges, researchers are exploring solutions that will provide satisfactory results to the power system network as a whole, as well as to procure
beneﬁts to both the utilities and the customers. The solutions that have been provided are
summarized below.
4.1. Optimal Integration and Planning of Renewable Distributed Generation
DG optimal integration can improve network performance [103]. The optimal integration of DGs can be achieved through several strategies, the most popular one being
through use of mathematical optimization models. Ehsan and Yang [62] have provided a
good account of analytical techniques that are used for optimal integration and planning
of renewable DG in the power distribution network. The strategies can, in a particular
context and environment, invariably be used to address most of the challenges that have
been mentioned in the previous section.
•
The following, researched and presented by Georgilakis et al. in Ref. [107], are the
mathematical formulations components for optimization approaches: a general problem statement, problem objectives whether single or multi, number of DGs and type
of DG technology and a number of constraints to be considered.
•
This is in the agreement that indeed, as mentioned by [32,94,95], the performance
beneﬁts depend mainly on the optimal sizing and location of the DG units, the DS
conﬁguration and the types of DG technologies used for conversion of energy. In
Ref. [76], Esmaili was one of the earliest researchers to propose a multi-objective
framework for placing and sizing DG units with the combination of the number of DGs,
voltage stability margin and minimization of power loss into one objective function.
•
In Ref. [108], the authors reviewed probabilistic optimization techniques (POT) in
Smart Power Systems and noted that in order to account for uncertainties in optimization processes, stochastic optimization is essential. From their review, probabilistic
optimization techniques were classiﬁed into stochastic optimization (SO), robust optimization (RO), distributionally robust optimization (DRO) and chance constraints
optimization (CCO), each of which having their own advantages and drawbacks over
the others, with the common drawback to all being their high computational requirements. Riaz et. al. [108] further proposed that the most advanced and less costly
technique is the robust optimization in which a deterministic, set-based uncertainty
model is used instead of a stochastic one. The authors suggest that POTs must be used
in combination in order to deal with new challenges to achieve proliﬁc outcomes.
•
The authors in [92,101–103,109–112] have worked on various aspects related to DG
grid integration optimization. The solutions proposed include the following beneﬁts:
more energy savings, improvement of voltage proﬁle, reduced purchased power from
the DGs, increased sold power to the distributed grid, decreased non-supply load,
reduced overall cost of smart grid and mitigation of fault severity.
•
Fast dispatch is one of the techniques that helps manage the variability of renewable
generation because it reduces the need for regulating resources, improves efﬁciency
and provides access to a broader set of resources to balance the system [33].

---


### Page 10

Energies 2023, 16, 1732
10 of 21
With regards to planning, to handle the high complexity of the investment planning
problem for instance, Ref. [102] used a bi-level optimization framework that maximizes the
net present value (NPV). Level-1 determines the optimal sizing of BESS in the presence of
high PV penetration with the aim of minimizing the net present cost (NPC). The optimal
BESS power dispatch in coordination with the DR aggregator is obtained in level-2, aiming
to minimize NPC for voltage deviation penalty and PS losses with the scheduling of
BESS and DR only [102]. In Ref. [61], a method to determine the optimal location, power
and energy capacity of storage by creating an independent objective function for the
voltage proﬁle and power losses was proposed. The authors used the symbiotic organism
search algorithm (SOSA) to solve the optimization problem with the following objectives:
improvement of voltage proﬁle, loss reduction, network reliability and minimization
of storage costs including investment, operation and maintenance costs. SOSA has the
advantage over other conventional algorithm (PSO and GA) of having speciﬁc adjusting
parameters allowing for the conversion rate increase.
4.2. DER Coordination
Sharma et al. in [80] investigated the coordination of multiple DERs to address the
techno-economic aspects of distribution network operation. The study aimed to ﬁnd optimal dispatches of BESS in coordination with DR for wind generation and shunt capacitor
with the target of minimizing distribution power loss. In [103], the authors developed a
bi-level optimization framework for impact analysis of DR on PV and BESS accommodation
in DS. The study was motivated by the undergoing intensive research on responsive loads
driven by dynamic pricing that have shown beneﬁts for utilities and consumers by shifting
the demand peak to off-peak periods by utilizing renewable energy.
Achieving optimal integration of DGs is a complex problem involving many components, variables and constraints, network status, load dynamics and faults events, protection
schemes, weather conditions and consumers’ behaviour. Optimal integration requires the
minimization as much as possible of operational issues. This is largely achievable through
the coordination of multiple DERs. The following types of coordination have been under research with progressive results to achieve efﬁcient, reliable and economical use of
grid-integrated renewable energy resources:
•
Coordination of DGs, BESS and DR for multi optimization of distribution
networks [80,102];
•
Energy scheduling with BESS cost [87];
•
Energy management with electricity price;
•
Accommodation of PV, DR and BESS [103];
•
Solar PV with BESS under uncertain environment [112];
•
Investment planning of DG resources with DR [102];
•
DR analysis for optimal allocation of wind and solar [90];
•
Optimal sizing of PV/wind and hybrid considering DSM [113];
•
DR trends: users, network services, markets, and DERs [114];
•
DR and intermittent RERs [115];
•
Price-driven DR [53];
•
Household appliances and DR [116];
•
Joint allocation and operational management of DG and BESS in presence of DR [92];
•
Pricing schemes, optimization objectives and solution methodologies of DSM [11];
•
DR: Pricing, optimization and appliance scheduling [117];
•
DSM model and optimization;
•
Optimal planning and investment beneﬁts of shared BESS;
•
DGs, power losses and voltage stability.
4.3. Energy Storage Systems and Complementary Technologies
Kucur et al. [18] examined worldwide energy storage applications, their best location,
applied technologies, total energy and power capacity and quality. Pumped storage are

---


### Page 11

Energies 2023, 16, 1732
11 of 21
the most common type of grid-scale energy storage, but lead acid and lithium ion batteries
are the most prominent for solar PV systems [18]. Although they have relatively high
capital costs as indicated amongst other drawbacks by Liu et al. in Ref. [72], energy storage
systems are essential technologies as they provide support to overcome the challenge of
balancing supply and demand [18] and to cope with the intermittent renewable generation
as well as to reduce the user’s electricity purchase cost [63].
Installing BESS at any location with any random and non-optimum size can lead
to high costs [61]. Using a storage device in the operation indices depends more on the
installation location than the storage capacity. The authors in Ref. [118] have assessed the
simultaneous impact of BESS, controllable load and network reconﬁguration on contemporary distribution networks under uncertainties. The multi-constraint complex optimization
problem was solved using an improved water evaporation optimization algorithm and the
authors found that the coordination strategy reduced network loss while improving the
voltage proﬁle of the systems. The impact of multiple BESS strategies on energy loss of
ADNs was investigated by Sharma et al. in [110]. With regards to the function of regulating
the voltage on the utility side, Gamage et al. in Ref. [105] proposed an approach to integrate
BESS to curb grid voltage violations.
•
Ref. [63] proposed an approach of optimal planning of shared energy storage based on
cost–beneﬁt analysis to minimize the electricity procurement of retailers. They found
that ES can effectively reduce the cost of retailers and high matching degree can be
used as the selection criterion to obtain greater beneﬁts from the shared ES [63].
•
Ref. [72] proposed a comprehensive optimal allocation model of BESS considering
operation strategy with the optimal capacity problem solved by cost–beneﬁt analysis
taking into account the reliability improvement beneﬁts of BESS.
•
The authors in Ref. [72] proposed system reliability improvements with BESS in
planning operation strategies. The optimal BESS capacity and sizing problem was
solved by cost–beneﬁt analysis. The authors concluded that from an economic point of
view, the distributed mode is preferable to centralized modes and the beneﬁts of BESS
can be improved by increasing the peak–valley difference of electricity price within a
certain range.
•
Ref. [72] was one of the earlier studies that proposed a comprehensive optimal allocation model of BESS that considered reliability beneﬁts.
Table 4 presents a useful summary of important contribution, challenges, methodologies used and potential solutions to DG.
Table 4. Summary of major contributions, challenges, methodologies and potential solutions.
Ref.
Challenges or Issues
Solution
Methodology
Research Objectives
Constraints/Objective
Function
Paper Contribution
[90]

Optimal
accommodation
in coordination
with DR

Impact on
planning of
wind-based and
solar-based DGs
in DS
MISOCP

Energy savings

Improvement of
voltage proﬁle

Energy losses

Minimum
voltage

Average voltage
deviation

DG penetration
level

Peak demand

Integrating DR
with planning of
DGs leads to more
energy savings and
improvement of
voltage proﬁle
[16]

Secure protection
for DS network

Protection
blinding issue
Adaptive Over
Current Protection
(AOCP)

High DER
penetration

Grid connected
and islanded
modes

Provided an
alternative
protection scheme
working regardless
connection to grid
or islanding
condition,

---


### Page 12

Energies 2023, 16, 1732
12 of 21
Table 4. Cont.
Ref.
Challenges or Issues
Solution
Methodology
Research Objectives
Constraints/Objective
Function
Paper Contribution
[119]

PV boosting
development

LSPV modelling
and simulation
techniques

LSPV integration
impacts on grid
static and
dynamic
characteristics

Key techniques
for improving
LSPV
transmission and
consumption

RE integration

Large-scale PV
development in
China

Review of large
scale PV
integration (LSPV)

Recommendations
for further research
with regards to
modelling and
simulations,
system integration
and power
generation delivery
and co
consumption
[115]

Reduce overall
cost of smart grid
and maximize
reliability

PSO

Optimal size of
units for the
smart grid

Cooling and
heating
management

Impact on smart
grid cost

Power
consumption of
heating and
cooling systems
resulted in
decreasing the size
of DGs

Reduced the
purchase power
from the DGs

Increased the sold
power to
distributed grid

Decreased
non-supply loads

Reduced the
overall cost of
smart grids
[74]

Mitigation of
fault severity
brought by DG
penetration

Causes
protection
devices not to
operate properly

Fault at
various
locations

Balanced
three-phase
faults are used

Protection
planning and
coordination
without and in
the presence of
DGs

Voltage
constraint

Thermal limits

Addressed
challenges
associated with the
operation of DS in
both normal and
contingency
operation states
[86]

Optimal use of
DERs

MPSO

Minimization of
operating cost of
a microgrid

Optimization
problem of a
community
micro-grid

Problem with
optimization of a
community
micro-grid

However, solutions
had signiﬁcant
deviations due to
prediction errors
[87]

Overall Minigrid
cost reduction

PSO (for model
optimization)
and Rainﬂow
(for battery
degradation
cost)

Electricity cost
management
through efﬁcient
control of BESS

Battery
degradation cost

Dynamic
electricity price

Proposed a
day-ahead energy
management for a
community micro
grid with
consideration of
battery
degradation costs

40% cost reduction
compared to the
baseline approach

---


### Page 13

Energies 2023, 16, 1732
13 of 21
Table 4. Cont.
Ref.
Challenges or Issues
Solution
Methodology
Research Objectives
Constraints/Objective
Function
Paper Contribution
[92]

Energy losses

Voltage deviation
(stability)

Mixed integer
second order
conic
programming
(MISOCP)

To propose
framework for
joint allocation
and operational
management of
wind DG and
BESS

Optimally
allocate windbased DG and
BESS

Power ﬂow

Wind-based DG
constraints

BESS constraints

Demand
response
constraint

Simultaneous
allocation and
operation
management of
wind-based DG
and BESS in
distribution system
considering DR

Optimal sizing and
siting of wind DG
and BESS along
with DR
participation leads
to signiﬁcant
energy savings and
improvement of
power quality

When DR
participation rate
increased, BESS
capacity decreased
[120]

Determination of
dynamic electric
energy retail
pricing tariffs

Statistical
analysis

Improve the
performance of
demand
response
techniques

Minimum power
demand

Load variation

Novel quantitative
measure of the load
proﬁle that
accurately reﬂected
the overall
generation
expansion
planning and
utilization costs

Peak-to-average
ratio (PAR) did not
reﬂect the load
characteristics
[53]

Price-driven
demand
response (PDDR)
to affect
customers’
consumption
(including critical
peak pricing,
TOU pricing,
real-time pricing

Evaluation of
advantages and
disadvantages of
PDDR

Review of three
different PDDR
programs at
residential sector

TOU

CPP

RTP
[51]

Lack of informed
decision from
both the supplier
and the
consumer

DSM to redesign
the load proﬁle
and to decrease
the peak load
demand

Review of DSM
strategies with both
DR and energy
efﬁciency policies
[110]

Generic
Algorithm
(GA)

Optimal
operation
strategies

Validation of
economic beneﬁt

Node voltage
limit

Feeder current
limit

Nodal power
balance

Optimal operation
of BESS can reduce
energy loss and
increase economic
beneﬁts of the DS

---


### Page 14

Energies 2023, 16, 1732
14 of 21
Table 4. Cont.
Ref.
Challenges or Issues
Solution
Methodology
Research Objectives
Constraints/Objective
Function
Paper Contribution
[103]

Optimal
integration of
emerging DERs

Bi-level GA
using Matlab

PV generation
limits

BESS constraints

Feeder thermal
limit constraints

Power balance
constraints

DGs were effective
in annual energy
loss reduction

BESSS facilitated
higher DG
penetration and
levelled the load
proﬁle

DR bridged the gap
between peak and
valley demands
and therefore
distresses to the
system
[118]

Innovative
Water
Evaporation
(IWEO)
algorithm

Optimal
coordination of
controllable load
scheduling, BESS
and uncertain
wind power

Nodal power
balance

Feeder thermal
limits

Controllable load
management

Network
conﬁguration

Two-stage
framework was
developed to
coordinate the
generation of DGs,
scheduling of
BESSs, optimal
management of
controllable load
[105]

Fluctuation of
grid voltage

Power ﬂow
simulation

Incorporation of
BESS can mitigate
voltage violation

More effective in
rural distribution
feeder suggesting
when the line
impedance is high
[80]

Non-sorted
generic
algorithm
(NSGA-II)

Technique for
order of
preference by
similarity to
ideal solution
(TOPSIS)

Optimal
dispatches of
BESS

Minimize
distribution
power loss and
grid demand cost

Nodal voltage
limit

Power loss
minimization

Grid demand
cost
minimization

Nodal power
balance

Feeder thermal
limits

Optimal
coordination of
wind power, BESS,
SC and TOU-DR
signiﬁcantly
reduced the
network losses and
grid demand
consumption cost
[76]

To place DG
units at more
efﬁcient buses
rather than end
buses of radial
links usually
used for voltage
stability
improvement

Non-Linear
Programming
(NLP)

Fuzziﬁcation
applied to
objective
functions

Optimal sizing
and location of
DG units

Number of DGs

Power loss
minimization

Maximize
voltage stability
margin

Branch and
voltage limits

Modelled all types
of DGs

Employed adaptive
reactive limits
rather than ﬁxed
limits

New technique to
formulate the
number of DGs
without converting
the NLP problem
into mixed-integer
NLP

Minimization of
the number of DG
units led to
placement of these
units at more
efﬁcient buses
rather than end
buses of radial link

---


### Page 15

Energies 2023, 16, 1732
15 of 21
Table 4. Cont.
Ref.
Challenges or Issues
Solution
Methodology
Research Objectives
Constraints/Objective
Function
Paper Contribution
[102]

Simultaneous
consideration of
cost of energy
purchased from
the grid, energy
losses, emission
penalty cost,
demand
deviation penalty,
operation and
maintenance cost
for NPV beneﬁts

Complex
mixed-integer,
non-linear and
non-convex
optimization
techniques

Bi-level
optimization
problem
(BLOP)

Multilayer DS
and BESS
investment
planning with
coordination of
DR

The coordination
aimed to
maximize Net
Present Value
(NPV) proﬁt

PV generation
limits

BESS capacity
limits

Power dispatch
and SOC limits

DR constraints

Thermal feeder
limits

Power balance
constraints

Cost of energy
purchased from
the grid

Energy losses

Emission penalty
cost

Demand
deviation penalty

Operation and
maintenance cost

Impact of DR on
investment
planning of DG
and BESS

Simultaneous
consideration of
cost of energy
purchased from the
grid, energy losses,
emission penalty
cost, demand
deviation penalty,
operation and
maintenance cost
for NPV beneﬁts

Higher NPV
beneﬁts

Analysed impact of
DR on payback
period: payback
within 9 of 20 years
of planning was
signiﬁcant
compared to
non-DR-based
investment
planning

Other technical
beneﬁts
[32]

Optimal sizing,
siting and
conﬁguration of
DGs

Review on
technical beneﬁts
of renewable DG

Review current
status of REN

Signiﬁcant roles
that renewable
DGs can play in
technical, economic
and environmental
operation
[72]

Intelligent
Single Particle
Optimiser
(ISPO)

Sequential
Monte Carlo
simulation
method

Operation
strategy of BESS
(power and time
periods of
charging and
discharging)

Reliability
improvement
beneﬁts of BESS

Optimal
planning model
of BESS

Comprehensive
optimal allocation
model of BESS
considering
operation strategy

Numerical method
based on
expectation for the
calculation of
system reliability
improvement with
BESS in planning
was proposed

Optimal BESS
capacity and sizing
problems were
(simultaneously?)
solved by
cost–beneﬁt
analyses
[62]

Optimal
planning of DGs

Power quality,
voltage stability,
power loss,
reliability and
proﬁtability

Conventional and
metaheuristic
techniques

Metaheuristics
algorithms were
popular choice
because of their
ﬂexibility in
multi-objective
planning problems

---


### Page 16

Energies 2023, 16, 1732
16 of 21
Table 4. Cont.
Ref.
Challenges or Issues
Solution
Methodology
Research Objectives
Constraints/Objective
Function
Paper Contribution
[106]

Determination of
optimal location
and sizes

Optimal DG
placement and
sizing

Models and
solutions

Classify current
and future
research trends
in this ﬁeld

DG capacity
constraints

Operating
constraints

Investment
constraints
[63]

Cope with
intermittency
and reduce
customer
electricity
purchase cost

Fluctuation of
electricity prices
and the uncertainty
of RE resources’
output did not
inﬂuence users’
economic beneﬁts

Shared energy
storage (ES) system
among multiple
electricity retailers
showed more
beneﬁt rather than
the separately
conﬁgured ES
5. Further Research Priorities and Conclusions
5.1. Further Research Priorities
From this review study, the following concerns have not been appropriately and
exhaustively attended to and therefore still require researchers’ attention:
•
All-in-One multi-objective DER optimal planning solutions that include the coordination of various variables such as the type of DG technologies, the types of energy
storage integration, DSM mechanisms and different DR strategies, for maximum
beneﬁts both for the utility and consumers have not yet been sufﬁciently researched.
•
Further investigations are needed in establishing optimization techniques using hybrid
techniques that combine analytical, metaheuristic and computational methods to
achieve better results.
•
The use of optimization algorithms, ensemble methods and weather forecasting to
develop models that can predict renewable energy power output considering weather
conditions and seasonal variation still need attention and focus from researchers.
•
Development of robust models to quantify the impact of uncertainties related to
intermittency of renewable DGs. There is a need to gather resources and tools for
weather condition predictions.
5.2. Conclusions
The transformation of PS around the world is effective and largely impacted by a
rapid growth of various renewable energy grid integration thus affecting the control and
operation of contemporary DS which are becoming more and more active network systems.
Supporting and remedial actions are required and should be planned accordingly. This
paper presents various operational and technical challenges associated with DG integration
into DS. It was shown that the challenges of different natures at different levels of the
PS are usually addressed individually, prompting that a holistic approach be considered
when addressing them. Power quality, voltage stability, PS reliability, loss minimization,
cost–beneﬁts and so many other objectives can be achieved with optimal integration
and appropriate planning of DGs. The DG grid integration problem is a multi-objective
and hence needs advance multi-objective algorithms to address more than one challenge

---


### Page 17

Energies 2023, 16, 1732
17 of 21
simultaneously. In order to reduce the variability and increase predictability, robust models
need to be designed to include accurate forecasting methods, reliable data collection and
safe communication to cater to RE technologies’ uncertainties and intermittent nature.
Further energy storage and demand side management can play a major role in supplying
quality and reliable power to the customers and at the same time reduce the burden on
DGs and their intricacies such as variability.
Author Contributions: All authors planned the study, contributed to the idea and ﬁeld of information;
Introduction, K.L.; Software, K.L. and S.S.; Analysis, K.L., S.S., N.L., G.S. and P.N.B.; Conclusion, K.L.
and G.S.; writing—original draft preparation, K.L., P.N.B. and N.L.; writing—review and editing,
K.L. and G.S.; supervision, S.S. and G.S. All authors have read and agreed to the published version of
the manuscript.
Funding: This research received no external funding.
Data Availability Statement: Not applicable here.
Conﬂicts of Interest: The authors declare no conﬂict of interest.
References
1.
Dobson, I.; Green, S.; Rajaraman, R.; De Marco, C.; Alvarado, F.; Galavic, M.; Zang, J.; Zimmerman, R. Electric Power Transfer
Capability: Concepts, Applications, Sensitivity and Uncertainty; University of Wisconsin–Madison: Madison, WI, USA, 2001.
2.
Machowski, J.; Bialek, J.W.; Bumby, J.R. Power System Dynamics: Stability and Control, 2nd ed.; Sons, J.W., Ed.; John Wiley & Sons,
Ltd.: Hoboken, NJ, USA, 2008.
3.
Gafaro, F.; Portugal, I. Planning the Operability of Power Systems–Overcoming Technical and Operational Bottlenecks.
Available online: https://www.irena.org/-/media/Files/IRENA/Agency/Events/2017/Jan/17/IRENA-WFES-Scaling-upVRE---Operation-Planning---Final.pdf?la=en&hash=DA778DAF2644A2D6DBC70665B109E6B3AACA6673 (accessed on 17
January 2023).
4.
Berger, L.T.; Iniewski, K. Smart Grid: Applications, Communications and Security; John Wiley & Sons: Hoboken, NJ, USA, 2012.
5.
Banerjee, S.; Mesram, A.; Swamy, N.K. Integration of Renewable Energy Sources in Smart Grid. Int. J. Sci. Res. 2015, 4, 247–250.
6.
Freris, L.; Inﬁeld, D.G. Renewable Energy in Power Systems; John Wiley & Sons Ltd: Hoboken, NJ, USA, 2008.
7.
Loji, K.; Davidson, I.E.; Tiako, R. Voltage Proﬁle and Power Losses Analysis on a Modiﬁed IEEE 9-Bus System with PV Penetration
at the Distributed Ends. In Proceedings of the Southern African Universities Power Engineering Conference/Robotics and
Mechatronics/Pattern Recognition Association of South Africa (SAUPEC/Rob Mech/PRASA), Bloemfontein, South Africa, 27–29
January 2019.
8.
Kumar, A.K.; Selvan, M.P.; Rajapandiyan, K. Dynamic Grid Support System for Mitigation of Impact of High Penetration Solar
PV into Grid. In Proceedings of the 2017th International Conference on Power Systems (ICPS), Pune, India, 21–23 December 2017.
9.
Von Appen, J.; Braun, M.; Stetz, T.; Diwold, K.; Geibel, D. Time in the Sun: The Challenge of High PV Penetration in the German
Electric Grid. IEEE Power Energy Mag. 2013, 11, 55–64. [Cross Ref]
10.
Dalhues, S.; Zhou, Y.; Pohl, O.; Rewald, F.; Erlemeyer, F.; Schmid, D.; Zwartscholten, J.; Hagemann, Z.; Wagner, C.; Gonzalez,
M.D.; et al. Research and Practice of Flexibility in Distribution Systems: A Review. CSEE J. Power Energy Syst. 2019, 5, 285–294.
11.
Ahmad, S.; Ahmad, A.; Naeem, M.; Ejaz, W.; Kim, H.S. A Compedium of Performance Metrics, Pricing Schemes, Optimization
objectives and Solution Methodologies of Demand Side Management for the Smart Grid. Energies 2018, 11, 2801. [Cross Ref]
12.
US Energy Information Administration. Energy Sources/Activity. Available online: https://www.eia.gov/electricity/reports.
php#/T194 (accessed on 22 December 2022).
13.
IRENA(2018). Global Energy Transformation: A Roadmap to 2050; International Renewable Energy Agency (IRENA): Masdar City,
Abu Dhabi, 2018.
14.
Uluski, R.; Borlase, S. Next Generation Distribution Management. Power Ind. 2022 Trends Predict. 2022, 2022.
15.
Palmintier, B.; Broderick, R.; Mather, B.; Coddington, M.; Baker, K.; Ding, F.; Reno, M.; Lave, M.; Bharatkumar, A. On the Path to
Sun Shot: Emerging Issues and Challenges in Integrating Solar with the Distribution System; NREL/TP-5D00-65331; National Renewable
Energy Laboratories: Golden, CO, USA, 2016.
16.
Altaf, M.W.; Arif, M.T.; Saha, S.; Islam, N.; Haque, M.E.; Oo, A. Renewable Energy Integration Challenge on Power System
Protection and its Mitigation for Reliable Operation. In Proceedings of the IECON 2020 The 46th Annual Conference of the IEEE
Industrial Electronics Society, Singapore, 18–21 October 2020; pp. 1917–1922.
17.
Manditereza, P.T.; Bansal, R. Renewable distributed generation: The hidden challenges-A review from protection perspective.
Renew. Sustain. Energy Rev. 2016, 58, 1457–1465. [Cross Ref]
18.
Kucur, G.; Tur, M.R.; Bayindir, R.; Shabinzadeh, H.; Gharehhpetian. A review of Emerging Cutting-Edge Energy Storage
Technologies for Smart Grids Purposes. In Proceedings of the 2022 9th Iranian Conference on Renewable Energy & Disitributed
Generation (ICREDG), Mashhad, Iran, 23–24 February 2022.

---


### Page 18

Energies 2023, 16, 1732
18 of 21
19.
CIGRE, W.G. 37-23, Impact of Increasing Contribution of Dispersed Generation on Power System: Final Report; Electra: Ramat Gan,
Israel, 1998.
20.
Barker, P.P.; De Mello, R.W. Determining the Impact of Distributed Generation on Power Systems. Part-1. radial Distribution
systems. In Proceedings of the IEEE PES Summer Meeting, Seatle, DC, USA, 16–20 July 2000; pp. 1645–1656.
21.
Cossent, R.; Gómez, T.; Frías, P. Towards a future with large penetration of distributed generation: Is the current regulation of
electricity distribution ready? Regulatory recommendations under a European perspective. Energy Policy 2009, 37, 1145–1155.
[Cross Ref]
22.
Feinstein, C.D.; Orans, R.; Chapel, S.W. THE DISTRIBUTED UTILITY: A New Electric Utility Planning and Pricing Paradigm.
Annu. Rev. Energy Environ. 1997, 22, 155–185. [Cross Ref]
23.
Kundur, P.; Paserba, J.; Ajjarapu, V.; Andersson, G.; Bose, A.; Canizares, C.; Hatziargyriou, N.; Hill, D.; Stankovic, A.; Taylor, C.;
et al. Deﬁnition and Classiﬁcation of Power System Stability-IEEE/CIGRE Joint Task Force on Stability Terms and Deﬁnitions.
IEEE Trans. Power Syst. 2004, 19, 1387–1401.
24.
Kundur, P. Power Ssytem Stability and Control; Mc Graw-Hill: New York, NY, USA, 1994.
25.
Mangoyana, R.B.; Smith, T.F. Decentralised bioenergy systems: A review of opportunities and threats. Energy Policy 2011, 39,
1286–1295. [Cross Ref]
26.
Reza, M.; Schavemaker, P.H.; Slootweg, J.G.; Van Der Sluis, S.L. Impacts of Distributed Generation Penetration Levels on Power
Systems Stability. IEEE PES Gen. Meet. 2004, 2, 2150–2155.
27.
Slootweg, J.G.; Kling, W.L. Impacts of Distributed Generation on Power system Transient Stability. IEEE PES Gen. Meet. 2002, 2,
862–867.
28.
Vournas, C.D.; Sauer, P.W.; Pai, M.A. Relashionship Between Voltage and Angle Stability of Power Systems. Int. J. Electr. Power
Energy Syst. 1996, 18, 493–500. [Cross Ref]
29.
Basso, T.S. System Impacts from Interconnection of Distributed Resources: Current Status and Identiﬁcation of Needs for Further
Development; NREL/TP-550-44727 National Renewable Energy Laboratory NREL: Oak Ridge, TN, USA, 2009.
30.
Prakash, V.; Darbari, M. A Review on Security Issues in distributed Systems. Int. J. Sci. Eng. Res. 2012, 3, 1–5.
31.
Vardakas, J.S.; Zorba, N.; Verikoukis, C.V. Survey on Demand Response Programs in Smart Grids: Pricing Methods and
Optimization Algorithms. IEEE Commun. Surv. Tutor. 2015, 17, 152–178. [Cross Ref]
32.
Adefarati, T.; Bansal, R.C. Integration of renewable distributed generators into the distribution system: A review. IET Renew.
Power Gener. (Wiley-Blackwell) 2016, 10, 873–884. [Cross Ref]
33.
Bird, L.; Milligan, M.; Lew, D. Integrating Variable Renewable Energy: Challenges and Solutions; National Renewable Energy
Laboratory: Golden, CO, USA, 2013.
34.
Colmenar-Santos, A.; Reino-Rio, C.; Borge-Diez, D.; Collado-Fernández, E. Distributed generation: A review of factors that can
contribute most to achieve a scenario of DG units embedded in the new distribution networks. Renew. Sustain. Energy Rev. 2016,
59, 1130–1148. [Cross Ref]
35.
Denholm, P.; Clark, K.; O’Connell, M. On the Path to Sun Shot: Emerging Issues and Challenges in Integrating High Levels of Solar into
the Electrical Generation and Transmission System; NREL08563; National Renewable Energy La: Golden, CO, USA, 2016.
36.
Erdiwansyah, E.; Mahidin; Husin, H.; Nasaruddin, N.; Zaki, M.; Muhibbuddin. A critical review of the integration of renewable
energy sources with various technologies. Prot. Control Mod. Power Syst. 2021, 6, 1–18. [Cross Ref]
37.
Karimi, M.; Mokhlis, H.; Naidu, K.; Uddin, S.; Bakar, A.H.A. Photovoltaic penetration issues and impacts in distribution
network–A review. Renew. Sustain. Energy Rev. 2016, 53, 594–605. [Cross Ref]
38.
Shaﬁullah, M.; Ahmed, S.D.; Al-Sulaiman, F.A. Grid Integration Challenges and Solution Strategies for Solar PV Systems: A
Review. IEEE Access 2022, 10, 52233–52257. [Cross Ref]
39.
Öztürk, E.; Rheinberger, K.; Faulwasser, T.; Worthmann, K.; Preißinger, M. Aggregation of Demand-Side Flexibilities: A
Comparative Study of Approximation Algorithms. Energies 2022, 15, 2501. [Cross Ref]
40.
Söder, L.; Lund, P.D.; Koduvere, H.; Bolkesjø, T.F.; Rossebø, G.H.; Rosenlund-Soysal, E.; Skytte, K.; Katz, J.; Blumberga, D. A
review of demand side ﬂexibility potential in Northern Europe. Renew. Sustain. Energy Rev. 2018, 91, 654–664. [Cross Ref]
41.
Choudhury, S. A comprehensive review on issues, investigations, control and protection trends, technical challenges and future
directions for Microgrid technology. Int. Trans. Electr. Energy Syst. 2020, 30, 1–16. [Cross Ref]
42.
Kennedy, J.; Ciufo, P.; Agalgaonkar, A. A review of protection systems for distribution networks embedded with renewable
generation. Renew. Sustain. Energy Rev. 2016, 58, 1308–1317. [Cross Ref]
43.
Al-Abri, R. Voltage Stability Analysis with High Distributed Generation (DG) Penetration. University of Waterloo: Waterloo, ON,
USA, 2012.
44.
Modarresi, J.; Gholipour, E.; Khodabakhshian, A. A comprehensive review of the voltage stability indices. Renew. Sustain. Energy
Rev. 2016, 63, 1–12. [Cross Ref]
45.
Razavi, S.-E.; Rahimi, E.; Javadi, M.S.; Nezhad, A.E.; Lotﬁ, M.; Shaﬁe-khah, M.; Catalão, J.P.S. Impact of distributed generation on
protection and voltage regulation of distribution systems: A review. Renew. Sustain. Energy Rev. 2019, 105, 157–167. [Cross Ref]
46.
Wong, J.; Lim, Y.S.; Tang, J.H.; Morris, E. Grid-connected photovoltaic system in Malaysia: A review on voltage issues. Renew.
Sustain. Energy Rev. 2014, 29, 535–545. [Cross Ref]
47.
Gensler, A.; Sick, B.; Vogt, S. A review of uncertainty representations and metaveriﬁcation of uncertainty assessment techniques
for renewable energies. Renew. Sustain. Energy Rev. 2018, 96, 352–379. [Cross Ref]

---


### Page 19

Energies 2023, 16, 1732
19 of 21
48.
Tian, W.; Heo, Y.; de Wilde, P.; Li, Z.; Yan, D.; Park, C.S.; Feng, X.; Augenbroe, G. A review of uncertainty analysis in building
energy assessment. Renew. Sustain. Energy Rev. 2018, 93, 285–301. [Cross Ref]
49.
Gyamﬁ, S.; Krumdieck, S.; Urmee, T. Residential peak electricity demand response—Highlights of some behavioural issues.
Renew. Sustain. Energy Rev. 2013, 25, 71–77. [Cross Ref]
50.
Menos-Aikateriniadis, C.; Lamprinos, I.; Georgilakis, P.S. Particle Swarm Optimization in Residential Demand-Side Management:
A Review on Scheduling and Control Algorithms for Demand Response Provision. Energies 2022, 15, 2211–2236. [Cross Ref]
51.
Panda, S.; Rout, P.K.; Sahu, B.K. Residential Sector Demand Side Management: A Review. In Proceedings of the 2021 1st
Odisha International Conference on Electrical Power Engineering, Communication and Computing Technology (ODICON),
Bhubaneswar, India, 8–9 January 2021; pp. 1–6.
52.
Shewale, A.; Mokhade, A.; Funde, N.; Bokde, N.D. A Survey of Efﬁcient Demand-Side Management Techniques for the Residential
Appliance Scheduling Problem in Smart Homes. Energies 2022, 15, 2863–2896. [Cross Ref]
53.
Yan, X.; Ozturk, Y.; Hu, Z.; Song, Y. A review on price-driven residential demand response. Renew. Dustainable Energy Rev. 2018,
96, 411–419. [Cross Ref]
54.
Mohamad, H.; Mokhlis, H.; Bakar, A.H.A.; Ping, H.W. A review on islanding operation and control for distribution network
connected with small hydro power plant. Renew. Sustain. Energy Rev. 2011, 15, 3952–3962. [Cross Ref]
55.
Bibak, B.; Tekiner-Mo˘gulkoç, H. A comprehensive analysis of Vehicle to Grid (V2G) systems and scholarly literature on the
application of such systems. Renew. Energy Focus 2021, 36, 1–20. [Cross Ref]
56.
Rahman, S.; Khan, I.A.; Khan, A.A.; Mallik, A.; Nadeem, M.F. Comprehensive review & impact analysis of integrating projected
electric vehicle charging load to the existing low voltage distribution system. Renew. Sustain. Energy Rev. 2022, 153, 111756.
[Cross Ref]
57.
Yong, J.Y.; Ramachandaramurthy, V.K.; Tan, K.M.; Mithulananthan, N. A review on the state-of-the-art technologies of electric
vehicle, its impacts and prospects. Renew. Sustain. Energy Rev. 2015, 49, 365–385. [Cross Ref]
58.
Khare, V.; Nema, S.; Baredar, P. Solar–wind hybrid renewable energy system: A review. Renew. Sustain. Energy Rev. 2016, 58,
23–33. [Cross Ref]
59.
Mohammed, Y.S.; Mustafa, M.W.; Bashir, N. Hybrid renewable energy systems for off-grid electric power: Review of substantial
issues. Renew. Sustain. Energy Rev. 2014, 35, 527–539. [Cross Ref]
60.
Muyiwa, A. Wind Resources and Future Energy Security: Environmental, Social, and Economic Issues. 2015. Available online:
https://search.ebscohost.com/login.aspx?direct=true&db=nlebk&AN=996965&site=eds-live (accessed on 1 January 2015).
61.
Saﬁpour, R.; Sadegh, M.O. Optimal Planning of Energy storage Systems in Microgrids for Improvement of operation Indices. Int.
J. Renew. Energy Res. 2018, 8, 1483–1498.
62.
Ehsan, A.; Yang, Q. Optimal integration and planning of renewable distributed generation in the power distribution networks: A
review of analytical techniques. Appl. Energy 2018, 210, 44–59. [Cross Ref]
63.
Liu, J.; Chen, X.; Xiang, Y.; Huo, D.; Liu, J. Optimal palanning and investment beneﬁt analysis of shared energy storage of retailers.
Int. J. Electr. Power Energy Syst. 2020, 126, 106561. [Cross Ref]
64.
Lin, P.; Peng, Z.; Lai, Y.; Cheng, S.; Chen, Z.; Wu, L. Short-term power prediction for photovoltaic power plants using improved
Kmeans-GRA-Elman model based on multivariate meteorological factors and historical power datasets. Energy Convers. Manag.
2018, 177, 704–717. [Cross Ref]
65.
Eseye, A.T.; Zhang, J.; Zheng, D. Short-term photovoltaic solar power forecasting using a hybrid Wavelet-PSO-SVM model based
on SCADA and meteorological information. Renew. Energy 2017, 118, 357–367. [Cross Ref]
66.
Ahmad, M.W.; Mourshed, M.; Rezgui, Y. Tree-based ensemble methods for predicting PV poer generation and their comparison
with support vector regression. Energy 2018, 164, 465–474. [Cross Ref]
67.
Khan, W.; Walker, S.; Zeiler, W. Improved solar photovoltaic energy generation forecast using deep learnin-based ensemble
stacking approach. Energy 2022, 240, 122812. [Cross Ref]
68.
Patel, A.; Swathika, O.V.G.; Subramanian, U.; Babu, T.S.; Tripathi, A.; Nag, S.; Karthick, A.; Muhibbullah, M. A practical approach
for predicting predicting power in a small-scale off-grid photovoltaic system using machine learning algorithms. Int. J. Photoenergy
2022, 2022, 9194537. [Cross Ref]
69.
Adibah, Z.; Kamaruzzaman; Mohamed, A. Dynamic Voltage Stability of a Distribution System with High Penetration of
Grid-Connected Photovoltaic Type Solar Generator. J. Electr. Syst. 2016, 12, 239–248.
70.
Al Shammari, M.M. Evolution of Issues on Distributed Systems: A Systematic Review. In Proceedings of the 2020 19th International
Symposium on Distributed Computing and Applications for Business Engineering and Science (DCABES), Xuzhou, China, 16–19
October 2020; pp. 33–37.
71.
Das, C.K.; Bass, O.; Kothapalli, G.; Mahmoud, T.S.; Habibi, D. Overview of energy storage systems in distribution networks:
Placement, sizing, operation, and power quality. Renew. Sustain. Energy Rev. 2018, 91, 1205–1230. [Cross Ref]
72.
Liu, W.; Niu, S.; Xu, H. Optimal planning of battery energy storage considering reliability beneﬁt and operation strategy in active
distribution system. J. Mod. Power Syst. Clean Energy 2016, 5, 177–186. [Cross Ref]
73.
Phuangpornpitak, N.; Tia, S. Opportunities and Challenges of Integrating Renewable Energy in Smart Grid System. In 10th
Eco-Energy and Materials Science and Engineering Symposium; Elsevier: Amsterdam, The Netherlands, 2013; pp. 282–290.
74.
Strezosky, L.; Sajadi, A.; Prica, M.; Loparo, K.A. Distribution System Operational Challenges Following integration of Renewable
Generation. In Proceedings of the IEEE Energy Tech, Cleveland, OH, USA, 5 September 2016.

---


### Page 20

Energies 2023, 16, 1732
20 of 21
75.
Almas, H.; Shahrouz, A.; Jörn, A. The Development of Renewable Energy Sources and Its Signiﬁcance for the Environment. 2015.
Available online: https://search.ebscohost.com/login.aspx?direct=true&db=nlebk&AN=980370&site=eds-live (accessed on 1
January 2015).
76.
Esmaili, M. Placement of minimum distributed generation units observing power losses and voltage stability with network
constraints. IET Gener. Transm. Distrib. 2013, 7, 813–821. [Cross Ref]
77.
Anderson, P.M.; Fouad, A.A. Power System Control and Stability, 2nd ed.; IEEE Press, Inc.: Piscataway, NJ, USA, 2003.
78.
Xu, X.; Yan, Z.; Shahidehpour, M.; Wang, H.; Chen, S. Power System Voltage Stability Evaluation Considering Renewable Energy
with Correlated Variability. IEEE Trans. Power Syst. 2018, 33, 3236–3245. [Cross Ref]
79.
Ayub, M.A.; Khan, H.; Peng, J.; Liu, Y. Consumer-Driven Demand-Side Management Using K-Mean Clustering and Integer
Programming in Standalone Renewable Grid. Energies 2022, 15, 1006. [Cross Ref]
80.
Sharma, S.; Niazi, K.R.; Verma, K.; Rawat, T. Coordination of different DGs, BESS and demand response for multi-objective
optimization of distribution network with special reference to Indian power sector. Int. J. Electr. Power Energy Syst. 2020, 121,
106074. [Cross Ref]
81.
Liang, Y.; Deng, T.; Max Shen, Z.-J. Demand-side energy management under time-varying prices. IISE Trans. 2019, 51, 422–436.
[Cross Ref]
82.
Dey, B.; Basak, S.; Pal, A. Demand-side management based optimal scheduling of distributed generators for clean and economic
operation of a microgrid system. Int. J. Energy Res. 2022, 46, 8817–8837. [Cross Ref]
83.
Qin, H.; Wu, Z.; Wang, M. Demand-side management for smart grid networks using stochastic linear programming game. Neural
Comput. Appl. 2020, 32, 139–149. [Cross Ref]
84.
Latiﬁ, M.; Khalili, A.; Rastegarnia, A.; Bazzi, W.M.; Sanel, S. Demand-side management for smart grid via diffusion adaptation.
IThe Inst. Eng. Technol. Smart Grid 2020, 3, 69–82. [Cross Ref]
85.
Hecht, C.; Sprake, D.; Vagapov, Y.; Anuchin, A. Domestic demand-side management: Analysis of microgrid with renewable
energy sources using historical load data. Electr. Eng. 2021, 103, 1791–1806. [Cross Ref]
86.
Hossain, A.M.; Chakrabortty, R.K.; Ryan, M.J.; Pota, H.R. Energy Management of Community Energy Storage in Grid-connected
Microgrid under Real-time Prices. Sustain. Cities Soc. 2020, 66, 102658. [Cross Ref]
87.
Hossain, A.M.; Pota, H.R.; Squartini, S.; Zaman, F.; Guerrero, J.M. Energy Scheduling of Community Microgrid with Battery Cost
using Particle Swarm Optimisation. Appl. Energy 2019, 254, 113723. [Cross Ref]
88.
Gallo, A.B.; Simões-Moreira, J.R.; Costa, H.K.M.; Santos, M.M.; Moutinho dos Santos, E. Energy storage in the energy transition
context: A technology review. Renew. Sustain. Energy Rev. 2016, 65, 800–822. [Cross Ref]
89.
Boampong, R. Evaluating the Energy-Saving Effects of a Utility Demand-Side Management Program: A Difference-in-Difference
Coarsened Exact Matching Approach. Energy J. 2020, 41, 185–207. [Cross Ref]
90.
Rawat, T.; Niazi, K.R.; Gupta, N.; Sharma, S. Impact analysis of demand response on optimal allocation of wind and solar based
distributed generations in distribution system. Energy Sources Part B Econ. Plan. Policy 2021, 16, 75–90. [Cross Ref]
91.
Mulleriyawage, U.G.K.; Shen, W.X. Impact of demand side management on optimal sizing of residential battery energy storage
system. Renew. Energy Int. J. 2021, 172, 1250–1266. [Cross Ref]
92.
Rawat, T.; Niazi, K.R.; Gupta, N.; Sharma, S. Joint Allocation and Operational management of DG and BESS in Distribution
System in Presence of Demand Response. In Proceedings of the 2019 8th International Conference on Power Systems (ICPS),
Jaipur, India, 20–22 December 2019.
93.
Ahmad, S.; Alhaisoni, M.; Naeem, M.; Ahmad, A.; Altaf, M. Joint Energy Management and Energy Trading in Residential
Microgrid System. IEEE Access 2017, 4, 123334–123346. [Cross Ref]
94.
Ochoa, L.F.; Harrison, G.P. Minimizing energy losses: Optimal accommodation and and smart operation of renewable distributed
generation. IEEE Trans. Power Syst. 2011, 26, 198–205. [Cross Ref]
95.
Hung, D.Q.; Mithulanantan, N. DG allocation in primary distribution systems considering loss reduction. In Handbook of Renewable
Energy Technology; Zobaa, A.F., Bansal, R.C., Eds.; World Scientiﬁc Publishers: Singapore, 2011.
96.
Kyritsis, A.; Voglitsis, D.; Papanikolaou, N.; Tselepis, S.; Christodoulou, C.; Gonos, I.; Kalogirou, S.A. Evolution of PV systems in
Greece and review of applicable solutions for higher penetration levels. Renew. Energy Int. J. 2017, 109, 487–499. [Cross Ref]
97.
Kapoor, K.; Pandey, K.K.; Jain, A.K.; Nandan, A. Evolution of solar energy in India: A review. Renew. Sustain. Energy Rev. 2014,
40, 475–487. [Cross Ref]
98.
Castillo-Calzadilla, T.; Cuesta, M.A.; Olivares-Rodriguez, C.; Macarulla, A.M.; Legarda, J.; Borges, C.E. Is it feasible a massive
deployment of low voltage direct current microgrids renewable-based? A technical and social sight. Renew. Sustain. Energy Rev.
2022, 161, 112198. [Cross Ref]
99.
Centre/BNEF, F.S.-U. Global Trends in Renewable Energy Investment. Available online: http://www.fs-unep-centre.org (accessed
on 24 June 2019).
100. Rawat, T.; Niazi, K.R.; Gupta, N.; Sharma, S. A two-stage optimization framework for scheduling of responsive loads in smart
distribution system. Int. J. Electr. Power Energy Syst. 2021, 129, 106859. [Cross Ref]
101. Sharma, S.; Niazi, K.R.; Verma, K.; Meena, N.K. Multiple DRPs to maximise the techno-economic beneﬁts of the distribution
network. J. Eng. 2019, 2019, 5240–5244. [Cross Ref]
102. Sharma, S.; Niazi, K.R.; Verma, K.; Rawat, T. A bi-level optimization framework for investment planning of distributed generation
resources in coordination with demand response. Energy Sources Part A Recovery Util. Environ. Eff. 2020, 42, 1–18. [Cross Ref]

---


### Page 21

Energies 2023, 16, 1732
21 of 21
103. Sharma, S.; Niazi, K.R.; Verma, K.; Thokar, R.A. Bilevel optimization framework for impact analysis of DR on optimal accommodation of PV and BESS in distribution system. Int. J. Electr. Energy Syst. 2019, 29, e12062. [Cross Ref]
104. Rawat, T.; Niazi, K.R.; Gupta, N.; Sharma, S. Impact assessment of electric vehicle charging/discharging strategies on the
operation management of grid accessible and remote microgrids. Int. J. Energy Res. 2019, 43, 9034–9048. [Cross Ref]
105. Gamage, G.; Withana, N.; Silva, C.; Samarasinghe, R. Battery Energy Storage based Approach for Grid Voltage Regulation in
Renewable Rich Distribution Network. In Proceedings of the 2020 2nd IEEE International Conference on Industrial Electronics
for Sustainable Energy Systems (IESES), Cagliari, Italy, 1–3 September 2020.
106. Chauhan, A.; Saini, R.P. A review on Integrated Renewable Energy System based power generation for stand-alone applications:
Conﬁgurations, storage options, sizing methodologies and control. Renew. Sustain. Energy Rev. 2014, 38, 99–120. [Cross Ref]
107. Georgilakis, P.S.; Hatziargyriou, N.D. Optimal Distributed Generation Placement in Power Distribution Networks: Models,
Methods and future Research. IEEE Trans. Power Syst. 2013, 28, 3420–3428. [Cross Ref]
108. Riaz, M.; Ahmad, S.; Hussain, I.; Mihet-Popa, L. Probabilistic Optimization Techniques in Smart Power System. Energies 2022, 15,
825. [Cross Ref]
109. Rawat, T.; Niazi, K.R.; Gupta, N.; Sharma, S. A linearized multi-objective Bi-level approach for operation of smart distribution
systems encompassing demand response. Energy 2022, 238, 121991. [Cross Ref]
110. Sharma, S.; Niazi, K.R.; Verma, K.; Rawat, T. Impact of Multiple Battery Energy Storage System Strategies on Energy Loss of
Active Distribution Network. Int. J. Renew. Energy Res. 2019, 9, 1705–1711.
111. Tan, W.-S.; Hassan, M.Y.; Majid, M.S.; Abdul Rahman, H. Optimal distributed renewable generation planning: A review of
different approaches. Renew. Sustain. Energy Rev. 2013, 18, 626–645. [Cross Ref]
112. Thokar, R.A.; Gupta, N.; Swarnkar, A.; Sharma, S.; Meena, N.K. Optimal Integration and Management of Solar Generation and
Battery Storage System in Distribution Systems under Uncertain Environment. Int. J. Renew. Energy Res. 2020, 10, 11–12.
113. Sandhu, K.S.; Mahesh, A. Optimal sizing of PV/wind/battery Hybrid Renewable Energy System Considering Demand Side
Management. Int. J. Electr. Eng. Inform. 2018, 10, 79–93. [Cross Ref]
114. Arias, L.A.; Rivas, E.; Santamaria, F.; Hernandez, V. A Review and Analysis of Trends Related to Demand Response. Energies
2018, 11, 1617. [Cross Ref]
115. Hakimi, S.M.; Moghaddas-Tafreshi, S.M. Optimal Planning of a Smart Microgrid Including Demand Response and Intermittent
Renewable Energy Resources. IEEE Trans. Smart Grid 2014, 5, 2889–2900. [Cross Ref]
116. Setlhaolo, D.; Xia, X.; Zhang, J. Optimal scheduling of household apppliances for demand response. Electr. Power Syst. Res. 2014,
116, 24–28. [Cross Ref]
117. Hussain, I.; Mohsin, S.; Basit, A.; Khan, Z.A.; Qasim, U.; Javai, N. A review on Demand Response: Pricing, Optimization,
and Appliance Scheduling. In 6th International Conference on Ambient Systems, Network and Technologies, ANT 2015; Elsevier:
Amsterdam, The Netherlands, 2015.
118. Sharma, S.; Niazi, K.R.; Verma, K.; Rawat, T. Impact of battery energy storage, controllable load and network reconﬁguration on
contemporary distribution network under uncertain environment. IET Gener. Transm. Distrib. 2020, 14, 4719–4727. [Cross Ref]
119. Ding, M.; Xu, Z.; Wang, W.; Wang, X.; Song, Y.; Chen, D. A review on China’s large-scale PV integration: Progress, challenges and
recommendations. Renew. Sustain. Energy Rev. 2016, 53, 630–652. [Cross Ref]
120. Parizy, E.S.; Ardakani, A.J.; Mahammadi, A.; Loparo, K.A. A new quantitative load proﬁle measure for demand response
performance evaluation. Electr. Power Energy Syst. 2020, 121, 106073. [Cross Ref]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

---
