

---

Page 1

---

Renewable and Sustainable Energy Reviews 195 (2024) 114342
Available online 29 February 2024
1364-0321/© 2024 The Author(s). Published by Elsevier Ltd. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-
nc-nd/4.0/).
Contents lists available at ScienceDirect
Renewable and Sustainable Energy Reviews
journal homepage: www.elsevier.com/locate/rser
Photovoltaic systems operation and maintenance: A review and future
directions
Hind Abdulla a, Andrei Sleptchenko a,∗, Ammar Nayfeh b
a Department of Management Science and Engineering, Research Center on Digital Supply Chain and Operations Management, Khalifa University, Abu
Dhabi, 127788, United Arab Emirates
b Department of Electrical Engineering, Khalifa University, Abu Dhabi, 127788, United Arab Emirates
A R T I C L E
I N F O
Keywords:
Photovoltaic systems
Operation and maintenance
System approach
Bibliometric analysis
PRISMA
Systematic review
A B S T R A C T
The expansion of photovoltaic systems emphasizes the crucial requirement for effective operations and
maintenance, drawing insights from advanced maintenance approaches evident in the wind industry. This
review systematically explores the existing literature on the management of photovoltaic operation and
maintenance. Through the integration of bibliometric analysis and the Preferred Reporting Items for Systematic
Reviews and Meta-Analyses (PRISMA) framework, 186 articles are selected for further comprehensive review.
The selected articles are examined and categorized into four interconnected research domains: maintenance
strategies, performance indicators, degradation modeling, and maintenance optimization and planning. The
presented analysis underscores the importance of integrating maintenance strategies to enhance system
effectiveness. It also emphasizes the necessity of a systematic approach that integrates reliability assessment
with economic and technical considerations to optimize maintenance planning and enhance system availability
and resource efficiency. This aligns with the Sustainable Development Goals for affordable, reliable, and
sustainable energy, while also ensuring grid security. Furthermore, the study identifies gaps and proposes
avenues for improvement, recommending a shift towards prognostic approaches and the advancement of
predictive maintenance in photovoltaic systems. Key suggestions also include customizing metrics for large
installations, implementing adaptive protocols that move away from traditional component-centric scheduling,
and using reinforcement learning to prioritize risk and optimize long-term performance. Compared to previous
reviews focusing on specific maintenance elements, this work provides a broader perspective by incorporating
planning and organizational factors into the maintenance discussion.
1. Introduction
The depletion of traditional energy sources and the environmental
impact of large carbon emissions have led to a growing shift towards
renewable energy. According to the International Energy Agency (IEA),
achieving net zero emissions by 2050 requires a 70% contribution from
wind and solar power. The European Union has set more ambitious
goals, with the aim of 80% reduction in greenhouse gas emissions
(from a 1990 baseline) and 100% generation of renewable energy by
2050 [1]. Solar photovoltaic (PV) power generation, with abundant
irradiance, stands out among various renewable energy sources. The
global deployment of solar energy has experienced significant growth
in the last 10 years. In 2022, a significant 231 GWdc of PV capacity
was installed globally, resulting in a total cumulative PV installation
of 1.2 TWdc [2]. There has also been a significant increase in the
number of publications dedicated to solar energy in various regions.
Fig. 1 illustrates this upward trend, highlighting the growing volume
∗Corresponding author.
E-mail addresses: 100057555@ku.ac.ae (H. Abdulla), andrei.sleptchenko@ku.ac.ae (A. Sleptchenko), ammar.nayfeh@ku.ac.ae (A. Nayfeh).
of publications per region in the field of solar energy publications from
2013 to 2022.
It can be seen that the main growth of the publications comes from
the Asia-Pacific and Middle East North Africa (MENA) regions. In 2022,
China emerged as the leader in solar energy research, with a remark-
able 8602 published articles. Similarly, in the MENA region, Saudi
Arabia made significant progress in solar energy research, presenting
1367 articles that highlight its strong commitment to harnessing the
solar potential of its desert landscape.
The expansion of the capacity of PV systems and the interde-
pendencies among their components can complicate operation and
maintenance (O&M) tasks, despite their relatively simple design. At
the same time, the energy market for large-scale PV installations is
characterized by low profit margins and intense competition, where
even slight performance reductions can significantly affect the final
https://doi.org/10.1016/j.rser.2024.114342
Received 8 October 2023; Received in revised form 18 December 2023; Accepted 20 February 2024


---

Page 2

---

Renewable and Sustainable Energy Reviews 195 (2024) 114342
2
H. Abdulla et al.
Nomenclature
Abbreviations
𝐼𝐸𝐶
International Electrotechnical
Commission
𝑅𝐵𝐷
Reliability block diagrams
CPN
Cost priority number
CSP
Concentrated solar power
DP
Dynamic Programming
DSS
Decision support systems
FMEA
Failure modes and effect analysis
FMECA
Failure mode, effects, and criticality analy-
sis
FTA
Fault tree analysis
FV
Fussel–Vesely
IP
Integer programming
KPIs
Key performance indicators
MCDA
Multi-criteria decision analysis
MENA
Middle East North Africa
MIP
Mixed integer programming
ML
Machine learning
O&M
Operation and maintenance
PRISMA
Preferred Reporting Items for
Systematic Reviews and
Meta-Analyses
PV
Photovoltaic
RAM
Reliability, availability, and maintainabil-
ity
RL
Reinforcement learning
TSP
Traveling salesman problem
UAVs
Unmanned aerial vehicles
Notations/Symbols
𝜂𝐴
Array efficiency
𝜂𝑖𝑛𝑣
Inverter efficiency
𝜂𝑝𝑣
System efficiency
𝐴𝑡
Availability
𝐶𝐴𝑃𝐸𝑋
Capital expenditures
𝐶𝐹
Capacity factor
𝐶𝑀
Corrective maintenance ratio
𝐷𝑆
System degradation
𝐸𝐴
Energy-based availability
𝐸𝐿𝐶
Equivalent labor cost
𝐸𝑆𝑃𝐶
Equivalent spare parts cost
𝐼𝑅𝑅
Internal rate of return
𝐿𝐶𝑜𝐸
Levelized cost of energy
𝑀𝑃
Maintenance planning factor
𝑀𝑇𝐵𝐹
Mean time between failures
𝑀𝑇𝑇𝐹
Mean time to failure
𝑀𝑇𝑇𝑅
Mean time to repair
𝑁𝑃𝑉
Net present value
𝑂𝑃𝐸𝑋
Operational expenditures
𝑃𝐼
Performance index
𝑃𝑀
Preventive maintenance ratio
𝑃𝑅
Performance ratio
𝑅𝑡
Reliability
profit. Consequently, achieving maximum performance is essential to
ensure long-term profitability. In the PV industry, a dominating ‘‘install
and forget’’ mentality is observed, with operators performing minimal
𝑅𝑇
Response time
𝑆𝑅
Soiling ratio
𝑌𝑓
Final yield
𝑌𝑟
Reference yield
Units
GWdc
Gigawatt for direct current
h
hour
kW
Kilowatt
kW/m2
Kilowatt per square meter
kWh
Kilowatt hour
kWh/m2
Kilowatt-hours per square meter
kWp
Kilowatt peak
m2
Square meter
MW
Megawatt
MWp
Megawatt peak
t
time period
TWdc
Terawatt for direct current
maintenance beyond the essential periodic cleaning. This practice is
driven by the belief in the reliability of the components. However,
following this approach often leads to unexpected failures, production
losses, higher costs, and compromised power quality [3]. Consistent
management and maintenance of large-scale solar power plants are
crucial to ensure grid stability, which goes beyond individual solar
arrays.
The described challenge of O&M also applies to smaller-capacity dis-
tributed installations, such as PV fleets, which are often scattered across
rooftops and hills, making them difficult to access. The importance of
maintenance in PV systems has garnered significant interest, prompting
research and initiatives from various institutions to establish ‘‘best
practices’’ for the O&M of PV systems [4]. It has been reported that
optimized O&M strategies can recover an average energy of 5.27% for
a typical 16.1 MWp PV plant, equivalent to $10 000 per MW annually.
Without effective O&M strategies, the global PV industry could face
an annual loss of $14.5 billion by 2024 [5]. Therefore, maintenance
management is essential for reliable and effective operation of PV
power plants, ensuring uninterrupted system operation and minimizing
downtime.
Compared to well-established technologies such as hydro, thermal,
and wind, the O&M processes for PV systems are not yet fully structured
in many operating companies [6]. In particular, the wind industry
has made substantial progress in O&M, as evidenced by the extensive
research landscape. For instance, Shafiee and Sørensen [7] emphasized
the importance of developing optimal maintenance plans for wind
farms considering factors such as inspection time, frequency, work
preparation, and necessary resources. Ren et al. [8] highlighted the
need for effective maintenance strategies for cost control and energy
production optimization, covering elements such as strategy selection,
schedule optimization, assessment criteria, recycling and environmen-
tal concerns. Furthermore, Tusar and Sarker [9] elaborated on efficient
maintenance practices for offshore wind farms considering inventory
management, transportation operations, and reliability improvement.
The extensive body of research in wind energy O&M covers a wide
range of aspects, indicating a higher level of depth compared to the
existing literature on O&M for PV systems. To achieve a sustainable
energy landscape, it is essential to recognize the crucial roles of wind
and PV energy in the overall energy system. This requires concentrated
research efforts and widespread sharing of best practices. Motivated
by the substantial body of work in wind O&M, there is a need to
systematically expand this knowledge to comprehensively review the
current literature on PV O&M. The goal is to modify and implement


---

Page 3

---

Renewable and Sustainable Energy Reviews 195 (2024) 114342
3
H. Abdulla et al.
Fig. 1. Growth in solar energy publications across regions and years [https://www.scopus.com].
similar principles in the context of PV systems, thereby enhancing the
understanding of effective O&M strategies.
The main objective of this review is to comprehensively examine the
development of PV O&M over the past decade and systematically ana-
lyze key topics and their interconnections in the field. In Section 2.1,
it is highlighted that the majority of existing research has focused
primarily on individual aspects of O&M, neglecting the integration of
crucial elements such as human resources, inventory, transportation,
and supply network management. Maintenance of PV systems extends
beyond addressing technical issues, including strategic allocation of
resources, prioritization of tasks, and formulation of contingency plans.
Understanding the interconnections between these aspects is essential
for optimizing maintenance and making well-informed decisions.
The main contributions of this review, in comparison to existing
reviews, include:
• A timely analysis of PV O&M evolution, considering recent ad-
vancements and challenges through a holistic approach.
• A broader scope by exploring often overlooked factors related to
maintenance assessment, economic considerations, and logistical
elements crucial for effective real-world management.
• An outlook of future research scopes in PV systems O&M man-
agement, aiming to contribute to the establishment of future
standards and best practices.
To achieve a comprehensive review of PV system O&M manage-
ment, a systematic methodology is employed, integrating bibliometric
and content analyses. While bibliometric studies offer valuable quanti-
tative insights, their limitations in providing a complete understanding
of the field are acknowledged. To address this, systematic literature
review methods are incorporated to evaluate the inherent characteris-
tics of the O&M research landscape. A bibliometric analysis of research
publications is initially performed from 2010 to 2023 to evaluate
academic output and identify significant trends. Subsequently, the
Preferred Reporting Items for Systematic Reviews and Meta-Analyses
(PRISMA) method is employed to extract relevant articles for systematic
analysis and identification of research themes. These efforts aim to
improve the understanding of PV O&M and establish a research agenda
for future exploration by identifying gaps within the specified themes.
The remaining sections of this work are organized as follows. Sec-
tion 2 presents a preliminary analysis, including an overview of existing
review articles and bibliometric studies. This section also outlines
the literature search strategy and selection process, and provides an
overview of PV systems O&M management through analysis of biblio-
metric results. A PRISMA analysis is implemented to select relevant
articles, which concludes with the classification of articles into re-
search themes. Building on this, Section 3 presents an overview of PV
maintenance strategies, Section 4 summarizes PV performance metrics,
Section 5 discusses approaches for PV degradation modeling, and Sec-
tion 6 reviews the existing literature on PV maintenance optimization
Table 1
Categorization of literature reviews on topics related to PV O&M and solar energy
bibliometric research.
Article type
Scope
Related articles
Review
articles
Monitoring and fault diagnosis techniques
[10–13]
Performance degradation and mitigation
approaches
[14–22]
Impact of dust and soiling on PV panels
and methods for cleaning
[23–26]
Overview of maintenance strategies
[27–29]
Predictive maintenance and energy
forecasting techniques
[3,30–32]
Bibliometric
analyses
Progression of concentrated solar power
(CSP) and PV thermal systems
[33–36]
Applications of PV systems such as rooftop
installations or PV systems integrated into
power networks
[37,38]
Solar energy research trends in specific
countries or regions
[39,40]
Trends in PV energy management
[41]
and inspection planning. At the end of this review, Section 7 explores
the identified gaps and proposes future research directions. Finally,
Section 8 provides a concise summary of the main findings of the study,
including limitations and future recommendations.
2. Preliminary analysis
2.1. Existing reviews
The literature reveals a wealth of review studies on topics re-
lated to PV O&M, as well as bibliometric studies within the solar PV
research domain. Table 1 classifies the literature reviews on PV O&M-
related subjects based on their scope and also categorizes the different
bibliometric studies in the field of solar energy.
Several review articles have conducted comprehensive investiga-
tions on monitoring and fault diagnosis techniques in the field of PV
systems. Specifically, Høiaas et al. [11] reviewed optics-based tools
for large-scale PV module inspection, including fault classification and
evaluations of infrared thermography and luminescence imaging tech-
nologies. These techniques are pivotal in aiding O&M operators in
accurately identifying faults in PV plants. Similarly, Jaen-Cuellar et al.
[12] investigated faults in solar PV and wind power systems, analyzing
their causes and impact on efficiency and maintenance costs. The
study emphasized the growing utilization of data-driven techniques,
such as machine learning (ML), for fault detection and diagnosis.
Investigating failure and degradation modes in PV systems has also


---

Page 4

---

Renewable and Sustainable Energy Reviews 195 (2024) 114342
4
H. Abdulla et al.
received considerable attention in the literature. Peinado Gonzalo et al.
[19] analyzed failure and degradation mechanisms in PV modules,
emphasizing the identification of root causes and prevention techniques
for issues such as soiling, snow deposition, corrosion, cracks, and
hot spots. The study emphasized preventive maintenance techniques
such as surface modifications, coatings, and fatigue analysis. Another
study by Hernández-Callejo et al. [20] discussed critical components,
design factors, and O&M of PV systems, addressing energy control
mechanisms, module degradation, and the influence of meteorological
factors. Mitigation techniques such as uniform cooling were studied,
and operational risk management was utilized to identify risks asso-
ciated with electric current, fire hazards, natural events, and human
factors.
Some reviews have focused on the effect of dust and soiling on PV
panels and investigated various cleaning methods for enhanced per-
formance. Conceicao et al. [26] examined the advancement of soiling
research in solar energy, covering soiling characterization, modeling,
and various cleaning techniques and their influence on O&M costs.
Other studies have explored various maintenance schemes for PV sys-
tems. In their study, Keisang et al. [28] investigated O&M strategies in
PV microgrid systems, including corrective, preventive, and predictive
maintenance. The study focused on O&M challenges and solutions
in PV microgrids in Sub-Saharan Africa, highlighting the importance
of decentralized PV generation in addressing electricity access and
poverty. Considerable focus has also been directed towards predictive
maintenance and energy forecasting methods. For example, Ramirez-
Vergara et al. [30] looked into predictive maintenance models as an
economical option for solar PV systems. The article assessed forecasting
methods for critical factors such as solar irradiance and temperature,
particularly highlighting the potential of ML models.
It is evident that the O&M management of PV systems lacks compre-
hensive research that addresses the broader challenges and complexi-
ties of maintenance. As mentioned by Márquez [42], a comprehensive
examination of maintenance management issues in solar energy sys-
tems is needed. Although Keisang et al. [28] recognized the importance
of developing a maintenance itinerary and engaging stakeholders, their
emphasis was primarily on managerial guidelines for O&M approaches.
Furthermore, their assessment criteria overlooked essential technical
system-related parameters, such as equipment reliability, failure rates,
maintenance costs, and system availability. A successful maintenance
program seeks to minimize failures, maximize production uptime, and
reduce production loss through timely interventions. Once a mainte-
nance strategy is determined, the focus shifts to scheduling, presenting
an optimization challenge to ensure continuous and reliable operation
of the PV system. However, there is a lack of comprehensive guidance
on how to effectively coordinate the timing and sequencing of mainte-
nance interventions and strategically integrate them within the broader
operational context of a PV system. In addition, the effectiveness of
O&M programs relies on the inclusion of factors such as staff coordina-
tion, required spare parts, and logistics and supply chain management,
which have not received sufficient attention despite being crucial for
effective maintenance.
There is also a stream of review articles that integrated bibliometric
analysis in solar energy research to understand the development of the
field, technological trends, and areas for further exploration. In a study
by Azad and Parvin [35], an analysis was performed to monitor the
progress of concentrated solar power (CSP) and PV thermal systems,
highlighting key research themes such as performance analysis and
nanofluid integration. Other bibliometric studies have investigated spe-
cific applications within PV systems, including rooftop PV systems [37]
and the integration of PV systems into power networks [38]. These
studies have identified trends in optimal design, power quality, and
challenges such as voltage and frequency fluctuations. Furthermore, re-
search has explored current solar energy trends in specific countries or
regions. Zwane et al. [39] examined the evolution of solar forecasting
in Africa, highlighting solar irradiance and ML algorithms in modeling
techniques. Madsuha et al. [40] analyzed solar research in Indonesia,
covering semiconductors, simulation, and integration of technology and
regulation. In addition, a comprehensive analysis conducted by David
et al. [41] observed the evolving trends in PV energy management,
discovering crucial aspects such as demand management, consumer
behavior, and module materials. It is evident that the application of
bibliometrics in the context of PV systems O&M management remains
underexplored. The existing literature lacks detailed thematic descrip-
tions of the management and planning of maintenance tasks, which
are essential to ensure optimal performance. This gap calls for a more
thorough and systematic analysis, tracking the evolving trends, and
exploring key themes in PV O&M beyond the conventional domains.
Embracing a holistic approach to O&M management enables a com-
prehensive understanding of the technical, operational, and financial
elements involved. This ensures that maintenance practices are not
limited to isolated tasks, but are integrated into a cohesive and efficient
system.
2.2. Search strategy and initial data retrieval process
In the initial data retrieval phase, a draft protocol was developed,
and an informal preliminary scan confirmed the research gap high-
lighted in Section 2.1. This scan helped determine potential review
themes and exclusion criteria, as well as establish the time frame
and keywords for the systematic search. Subsequently, an extensive
literature search was conducted using the Scopus and Web of Science
databases. A detailed description of the search strategy used in this
study is presented in Table 2.
In the search strings, keywords related to ‘‘maintenance’’ and ‘‘op-
erations’’ were carefully applied to the title, abstract, and keyword
sections of the publications. The inclusion of the special character
‘‘*’’ at the end of specific terms enables the capture of variations
and expansion of the search scope by accommodating different forms
and extensions of the specified keywords. To ensure inclusiveness, the
search focused on publications between 2010 and September 2023
(the date of the search). This time range was chosen to account for
the remarkable technological advancements that have occurred within
the solar PV industry over the past decade. The indicated search
strings produced 3429 references (after removing duplicates) that were
used for the bibliometric analysis. To perform the initial bibliometric
analysis, several tools and software were employed. This includes the
‘Bibliometrix’’ [43] package for the statistical programming language
R [44], and the VOSViewer software [www.vosviewer.com, [45]].
These resources support exploration in various dimensions, such as pub-
lication trends, prominent journals, influential countries, and thematic
evolution.
2.3. Basic bibliometric analysis
The obtained 3429 references contained 1920 journal articles and
1509 conference papers. Fig. 2 presents a further analysis of the col-
lected references across years and sources where only sources with
more than 50 publications in total are highlighted. Notably, there has
been a significant rise in the number of publications, particularly in the
last five years. This surge in publications reflects the industry’s recog-
nition of the importance of efficient O&M practices and the growing
significance of PV systems in the energy sector. It can also be noted
that more than 55% of the collected references have been published
in the last five years, highlighting the accelerated pace of research
and innovation within the PV industry. Furthermore, Fig. 2 shows that
‘‘Energies’’, ‘‘Solar Energy’’, and ‘‘Renewable Energy’’ demonstrate the
highest productivity, with 172, 102, and 94 publications, respectively.
At the same time, the primary venue for conference papers was the
‘‘Conference Record of the IEEE Photovoltaic Specialists Conference’’,
with 62 papers.


---

Page 5

---

Renewable and Sustainable Energy Reviews 195 (2024) 114342
5
H. Abdulla et al.
Table 2
Overview of search strategy including search string, inclusion and exclusion criteria, and language considerations.
Database
Search string
SCOPUS
( TITLE ( ( "Photovoltaic*" OR "PV" ) AND ( "Maintenance" OR "Operations and Maintenance"
OR "Operation and Maintenance" OR "O&M" OR "Operation & Maintenance" OR "Operations &
Maintenance" OR "Maintenance Management" OR "Schedul*" OR "Plan*" OR "Decision" ) ) AND
ABS ( ( "Photovoltaic*" OR "PV" ) AND ( "Maintenance" OR "Operations and Maintenance" OR
"Operation and Maintenance" OR "O&M" OR "Operation & Maintenance" OR "Operations &
Maintenance" OR "Maintenance Management" OR "Schedul*" OR "Plan*" OR "Decision" ) ) ) AND
PUBYEAR > 2009 AND PUBYEAR < 2024 AND ( LIMIT-TO ( SRCTYPE , "p" ) OR LIMIT-TO ( SRCTYPE
, "j" ) ) AND ( LIMIT-TO ( PUBSTAGE , "final" ) ) AND ( LIMIT-TO ( SUBJAREA , "ENGI" ) OR
LIMIT-TO ( SUBJAREA , "ENER" ) OR LIMIT-TO ( SUBJAREA , "DECI" ) ) AND ( LIMIT-TO (
DOCTYPE , "ar" ) OR LIMIT-TO ( DOCTYPE , "cp" ) ) AND ( LIMIT-TO ( LANGUAGE , "English" ) )
Web of Science
(TI=(( "Photovoltaic*" OR "PV" ) AND ( "Maintenance" OR "Operations and Maintenance" OR
"Operation and Maintenance" OR "O&M" OR "Operation & Maintenance" OR "Operations &
Maintenance" OR "Maintenance Management" OR "Schedul*" OR "Plan*" OR "Decision" )) AND
AB=( ( "Photovoltaic*" OR "PV" ) AND ( "Maintenance" OR "Operations and Maintenance" OR
"Operation and Maintenance" OR "O&M" OR "Operation & Maintenance" OR "Operations &
Maintenance" OR "Maintenance Management" OR "Schedul*" OR "Plan*" OR "Decision" ))) AND
(DT==("ARTICLE" OR "PROCEEDINGS PAPER") AND LA==("ENGLISH") AND SJ==("ENERGY FUELS" OR
"ENGINEERING" OR "SCIENCE TECHNOLOGY OTHER TOPICS" OR "OPERATIONS RESEARCH MANAGEMENT
SCIENCE"))
Inclusion criteria
✓Full-text accessibility
✓Publication in the final stage
✓Academic journals and conference papers
✓Published between 2010 and September 2023
✓Subject areas related to engineering, energy, operations research and decision sciences
Exclusion criteria
×Abstracts, book chapters, dissertations, technical reports, and review papers
×Papers covering non-renewable or alternative renewable energy sources, other than PV technologies
×Papers that cannot be accessed
Language
✓English
Fig. 2. Yearly distribution of publications between different sources.
The geographical distribution of publications across the world is
shown in Fig. 3 with the density of the blue color indicating the relative
degree of contribution for each country.
In particular, China had the highest number of publications, to-
taling 751 papers. This substantial publication count in China can be
attributed to generous funding and sponsorship that supported research
efforts in the country. The United States followed in second place with
329 articles, closely followed by India and Italy, with 295 and 289
papers, respectively. These findings highlight strong research activity
in European, American and East Asian markets.
2.4. Keywords and thematic evolution
Keywords and thematic evolution analysis can help to understand
the development of the most important research topics in the PV
industry, and to highlight the essential research gaps. Fig. 4 displays
the heat map generated to identify significant keywords within the
publications.
These keywords covered a range of topics, such as optimization,
photovoltaic modules and plants, electricity generation, storage and
distribution, efficiency and maintenance. Keywords ‘‘optimization’’ and
‘‘integer programming’’ are located in the most prominent areas of the
map, indicating the importance of optimization among the collected
references. This can be attributed to the general scope of the search
strings. At the same time, ‘‘maintenance’’ and ‘‘efficiency’’ have rel-
atively low weights in the obtained results. This highlights that the
management of PV systems often focuses on closely monitoring energy
production, neglecting the overall efficiency of the system affected
by global operations such as preventive maintenance, cleaning, and
relevant logistical tasks.
Following this, a thorough examination of the thematic evolution
in PV O&M literature from 2010 to 2023 was conducted employing the


---

Page 6

---

Renewable and Sustainable Energy Reviews 195 (2024) 114342
6
H. Abdulla et al.
Fig. 3. Countries’ scientific production.
Fig. 4. Density diagram of the bibliographic coupling of keywords from VOSViewer.
‘‘Bibliometrix’’ package. Four distinct time periods were identified, each
marked by varying volumes of publication, which signified a dynamic
change in research focus over time. This thematic evolution of the main
keywords is visualized in Fig. 5.
In the initial period (2010–2014), research made pivotal contri-
butions to the advancement of solar energy. This period focused on
PV module technology, monitoring methods, and efficient power gen-
eration. Studies also investigated essential components, such as DC–
DC converters and effective reactive power management. Collectively,
these efforts established a robust foundation for understanding PV
system fundamentals and significantly contributed to the progress of
the solar energy sector in subsequent years.
During the second research period (2015–2017), there was a notable
shift in the research landscape towards emerging thematic areas. While
research continued on topics such as PV plants, reactive power, and PV
module technology, there was a growing focus on new topics such as
optimization and energy storage. In the domain of optimization, studies
focused their attention on topology optimization methods, specifically
aiming to improve the efficiency and reliability of PV installations.
This emphasis involved prioritizing optimal system design and strategic
location selection to enhance overall performance.
In the subsequent period between 2018 and 2020, the research
within the field continued to evolve, exploring new dimensions of PV
systems. Studies focused their efforts on key topics, including schedul-
ing, maximum power point trackers, energy storage solutions, and
performance assessment methods. Scheduling related research during
this period was aimed at optimizing the use of available resources,
particularly solar irradiance. Additionally, there was considerable at-
tention given to integrating PV power plants with charging stations,
storage systems, and distribution networks. This emphasis revolved
around the effective management of power generation and demand,
marking a pivotal aspect of research during this time frame.
In the recent period from 2021 to 2023, research has notably shifted
its focus towards forecasting and decision-making, reflecting a growing
interest in enhancing the intelligence and adaptability of PV instal-
lations. Techniques such as artificial neural networks and stochastic


---

Page 7

---

Renewable and Sustainable Energy Reviews 195 (2024) 114342
7
H. Abdulla et al.
Fig. 5. Thematic evolution of keywords extracted using Biblioshiny.
Fig. 6. PRISMA-based flowchart of the systematic selection of relevant studies.
optimization have been crucial for precise solar irradiance and PV
system output forecasts, vital for efficient grid integration and energy
planning. Studies have also examined decision-making frameworks and
governance for utility-scale PV plant procurement, conducting thor-
ough economic evaluations to ensure informed choices in the adoption
and deployment of solar technology.
The presented thematic evolution analysis revealed a significant
disparity within the academic literature, where O&M has gained less
attention compared to other research areas. Despite the shift in research
towards operational aspects such as control strategies, battery storage,
energy dispatch, scheduling, and power forecasting, it is essential not
to overlook the importance of maintenance considerations. Recognizing
the complex connection between PV maintenance and these other
themes is crucial. However, it is equally essential to acknowledge that
the full potential of PV maintenance remains largely unexplored. This
research gap serves as a clear indicator, which underlines the impera-
tive need for future studies to thoroughly investigate the maintenance
aspects of PV systems.
2.5. Article selection process for systematic and content analysis
The PRISMA 2020 flow diagram [46], depicted in Fig. 6, was
employed to assess and choose articles for systematic review and
content analysis. The initial dataset for bibliometric analysis, consist-
ing of 3429 articles, was subjected to a screening and refinement
process. This screening process utilized specific keyword filters that
had been identified and confirmed during the preliminary literature
scan. The filters included terms such as ((Optimization OR Cost
OR Forecasting OR Economic analysis OR Performance OR
Efficiency) AND (Maintenance OR Reliability)), applied
to the titles and abstracts of the articles. Additionally, articles lacking
digital object identifiers (DOIs) and those originating from conferences
held before 2017 were excluded from the dataset. The decision was
influenced by the rigorous peer review process associated with articles
with DOI. Furthermore, it was assumed that conference papers before
2017 were subsequently published as journal articles. The focus on


---

Page 8

---

Renewable and Sustainable Energy Reviews 195 (2024) 114342
8
H. Abdulla et al.
Fig. 7. Keyword clustering for selected 186 articles using VOSViewer
(normalization: LinLog/modularity, attraction: 10, repulsion: 3, resolution 1.00, min.cluster size: 1).
conference papers after 2017 aligns with the latest developments in
O&M management for PV systems, enabling the capture of recent
progress in the field. As a result of these filtering measures, a total of
511 articles remained, meeting the initial eligibility criteria. To further
narrow down the selection, exclusion criteria were established.
These criteria excluded articles related to engineering topics such
as PV system design, installation, sizing, optimal configuration, compo-
nent selection, material selection, and site location. Articles exclusively
focusing on technical aspects of PV system integration into power
grids, hybrid systems (e.g., CSP, PV-Wind), or specific PV applications
(e.g., pumping systems, desalination plants, electric vehicles) without
addressing maintenance-related topics were also excluded. Moreover,
technical articles discussing PV system operations and control, such
as battery operations, energy storage, and voltage stability, without
incorporating maintenance practices were eliminated. Lastly, articles
addressing PV system energy policies, sustainability, and government
regulations were also excluded. Following this comprehensive exami-
nation, a total of 325 articles were removed from the dataset, resulting
in 186 articles that remained eligible for systematic review and content
analysis.
2.6. Article classification and research areas in PV systems maintenance
The selected articles were classified using the VOSViewer software,
with the resulting clusters visually depicted in Fig. 7. This method
enabled a comprehensive examination of the keywords, leading to
the categorization of the articles into four main areas. Furthermore,
the approach revealed the interconnected nature and highlighted the
common themes evident in the papers.
Further analysis of the proposed clusters suggests that the main
research topics are related to maintenance strategies, key performance
indicators (KPIs), degradation modeling, and maintenance optimization
and inspection planning. It is also obvious that there are no clear
boundaries between the areas, highlighting the need for a holistic
approach in this field and emphasizing the importance of integrat-
ing maintenance practices, system performance evaluation, deteriora-
tion modeling, and strategic planning to achieve optimal maintenance
outcomes.
Furthermore, it is clear that many of the selected papers fall into
multiple categories. For example, a single paper might address various
aspects, including different maintenance strategies for PV systems,
assessing system performance using specific metrics, and exploring
how maintenance decisions affect overall system conditions. It would
be ideal to categorize these papers into multiple themes that corre-
spond to their various research dimensions. As a result, articles were
allowed to be associated with multiple subject areas, aligning with
the methodology seen in previous bibliometric studies by Cosh et al.
[47] and Leefmann et al. [48]. The detailed results of the keyword
analysis, including research areas, primary keywords, and the top 10
cited articles, are presented in Table 3.
In the following sections, a more thorough and systematic analysis
of the research areas will be presented.
3. Overview of PV maintenance strategies
Many studies have classified maintenance strategies in different
ways [5,28,29,56,89]. In literature, three general maintenance strate-
gies for solar PV systems are mentioned: corrective, preventive, and
predictive maintenance. Fig. 8 shows the evolution of maintenance
strategies over time, along with examples of maintenance activities for
PV systems.
3.1. Corrective maintenance
Corrective maintenance involves addressing failures, malfunctions,
or damages identified by remote monitoring or routine inspections. It
is an unscheduled procedure aimed at resolving problems and restoring
normal operation. However, it can be costly and cause power gen-
eration shortages and potential damage to critical components [89].
The accessibility challenges of remote sites further escalate the prob-
lem, as the need to dispatch personnel to these locations leads to
increased maintenance costs. Reducing response times is crucial in
corrective maintenance, involving acknowledgment, intervention, and
repair times. Studies have explored decision support systems (DSS) to
optimize the decision-making process, such as the work by Livera et al.


---

Page 9

---

Renewable and Sustainable Energy Reviews 195 (2024) 114342
9
H. Abdulla et al.
Table 3
Overview of research areas and frequency of main keywords.
Research area
Main keywords (frequency)
Top cited
(color)
articles
Maintenance
strategies (red)
Artificial intelligence (8), Artificial neural network (6), Condition-based maintenance (7),
Condition monitoring (7), Data acquisition (10), Deep learning (8), Environmental conditions
(9), Fault detection (15), Forecasting (11), Image processing (5), Inspection (10), Machine
learning (8), Maintenance (45), Maintenance management (5), Maintenance strategies (7),
Neural networks (13), Preventive maintenance (8), Predictive maintenance (5), Unmanned
aerial vehicles (12).
[49–58]
Key performance
indicators (KPIs)
(green)
Cost Analysis (13), Cost benefit analysis (8), Cost effectiveness (11), Degradation (16),
Degradation rate (6), Efficiency (5), Energy productions (6), Operation and maintenance (19),
Performance (10), Performance analysis (5), Performance assessment (13), Performance loss
(7), Performance ratio (12), Photovoltaic modules (13), Photovoltaic system (48), Profitability
(6), Sensitivity analysis (6).
[59–68]
Degradation
modeling (blue)
Availability (20), Economic analysis (13), Electric inverters (11), Energy yields (5),
Environmental conditions (9), Failure analysis (15), Failure modes (5), Failure rate (10),
Grid-connected photovoltaic system (6), Markov chain (5), Markov processes (11), Reliability
analysis (32), Reliability assessments (5), Repair (7), Risk assessment (6).
[69–78]
Optimal Cleaning
(yellow)
Cleaning (17), Cleaning frequencies (6), Cleaning schedules (6), Decision making (6), Decision
Support System (5), Dust (10), Dust accumulation (8), Economics (5), Energy efficiency (12),
Optimization (18), Profit (5), Soiling (12), Scheduling (5).
[79–88]
Fig. 8. Evolution of maintenance strategies. Inspired by Lee et al. [90], modified specifically to PV systems, taking into consideration the current focus of literature in the field.
[5] that aimed to reduce the time between response and resolution
of corrective activities. Reducing unnecessary maintenance visits and
inspections improves the effectiveness of the corrective maintenance
plan, leading to higher availability and minimal downtime. However,
with increasing PV plant size, the number of components also increases
and the failure rate increases. Thus, relying solely on corrective mainte-
nance has been shown to be ineffective and undesirable for large-scale
PV systems [56].
3.2. Preventive maintenance
Preventive maintenance strategies aim to prevent failures by ad-
dressing minor faults before they escalate. There are two main ap-
proaches: time-based and condition-based preventive maintenance
[56]. Time-based preventive maintenance involves scheduled inspec-
tions, repairs, and adherence to operations manuals [29]. Studies
have developed models for PV time-based preventive maintenance,
such as the work by Baklouti et al. [91], which aimed to determine
inspection intervals and optimize degradation thresholds. Although the
time-based approach can enhance maintenance practices and reduce
component failures, it can incur higher costs due to unnecessary and
inefficient site visits, particularly for large-scale PV systems in remote
locations [68,92].
Condition-based preventive maintenance relies on monitoring sys-
tems and health analysis to detect early signs of failure or performance
issues [28,93]. Swift fault detection and identification are crucial for
preventing disruptions or damage in PV systems. Various methods are
used for fault diagnosis, including visual inspections [92], electrical
parameter evaluations [93], image processing [94,95], and statistical
analysis [96]. However, manual or visual monitoring may be insuf-
ficient for large and complex PV systems, as it focuses primarily on
panel performance rather than the entire system. Fault detection based
on electrical measurements, such as current–voltage (I–V) characteri-
zation, is impractical for PV farms due to the requirement of extensive
sensing and communication infrastructure. To address these challenges,
advanced diagnostic and automated monitoring systems have been
developed for fault identification and root cause analysis.
These systems use tools such as supervisory control and data ac-
quisition (SCADA) systems [55,89,97–100], thermal imaging with un-
manned aerial vehicles (UAVs) [51,53,58,94,95,101–105], and intel-
ligent maintenance systems [5,106–113]. Artificial intelligence algo-
rithms, such as support vector machine, k-nearest neighbors, decision


---

Page 10

---

Renewable and Sustainable Energy Reviews 195 (2024) 114342
10
H. Abdulla et al.
trees, and artificial neural networks, are integrated to analyze large
datasets and detect anomalies in real-time [31,51,53,55,114–118]. This
proactive approach enables the anticipation of failures, maintenance
alerts, and recommendations to optimize performance and minimize
downtime. However, implementing advanced monitoring techniques in
large-scale PV systems can result in higher maintenance costs due to
additional hardware installation, increased power demands, and the
need for trained personnel.
3.3. Predictive maintenance
Condition-based maintenance and predictive maintenance are of-
ten used interchangeably in the research literature when discussing
maintenance strategies [14,119,120]. However, there are important
distinctions between the two approaches. Condition-based maintenance
relies on sensors to collect real-time operational data from a sys-
tem. The data is then analyzed to make informed decisions about
the system’s health. In contrast, predictive maintenance uses anomaly
detection, fault diagnosis, and historical performance data to perform
parametric analyses and employ forecasting models [3,110]. PV sys-
tems and their components are analyzed to generate forecasts, identify
deterioration trends, and estimate the remaining useful life of the
components [121]. This enables predicting when a component is likely
to fail. Thus, condition-based maintenance is executed at the exact mo-
ment required, prior to significant failure. Predictive maintenance, on
the contrary, involves anticipating equipment failure and deterioration
in advance during normal operating conditions. This allows planned
maintenance activities to be effectively implemented.
The use of artificial intelligence algorithms has gained popularity
for fault prediction within a specific timeframe. In the PV industry, the
primary emphasis on predictive maintenance has been on inverters [52,
122] and PV panels [54,123]. For example, Betti et al. [122] utilized
artificial neural networks to predict faults, achieving a sensitivity of up
to 95% and a specificity of around 80%. Their solution successfully pre-
dicted high-frequency inverter failures up to almost seven days ahead.
Similarly, De Benedetti et al. [52] used an artificial neural network
trained on historical data of solar irradiance, ambient temperature, cell
temperature, and power output to accurately forecast inverter faults
several weeks in advance.
Accurate forecasting of energy production is crucial for PV systems
due to weather-related issues. The integration of predictive mainte-
nance and power forecasting techniques has received significant atten-
tion, especially for large-scale PV systems [49,50,124–129]. Short-term
power forecasting (0–72 h) helps in system operation planning and
facilitates maintenance scheduling adjustments. Du Plessis et al. [126]
developed neural network models for power forecasting within a six-
hour horizon in a 75 MW PV system, while Gao et al. [127] used long-
short-term memory networks for day-ahead power forecasting in a 10
MWp solar power plant. Accurate power forecasting enables operators
to predict peak electricity production periods, allowing maintenance
scheduling during low radiation periods without affecting power gener-
ation. This approach reduces system downtime and minimizes the risk
of unexpected failures.
Furthermore, predictive maintenance techniques play a vital role
in monitoring and managing environmental factors such as soiling
and snow in PV systems, which significantly affect efficiency [130].
Analysts can forecast the seasonal impacts of these factors using readily
available environmental data such as rainfall and particulate mat-
ter [131,132]. This forecasting is crucial for planning maintenance
tasks such as snow removal and cleaning. Implementing predictive
maintenance protocols enables the optimization of technician site visits
and early fault notifications, leading to lower costs associated with
unexpected corrective maintenance and excessive preventive mainte-
nance. According to Benabbou et al. [133], predictive maintenance
has the potential to reduce maintenance expenses from 10% to 40%.
However, in situations where the consequences of failure are minor,
when regular failures occur, or when parts replacement costs are low,
implementing predictive maintenance may not be feasible.
4. Comprehensive analysis of key performance indicators (KPIs)
As PV plants age, O&M procedures become increasingly important
for maintaining or improving performance. This involves evaluating
metrics and indicators while creating action plans to address problems.
KPIs play a critical role in evaluating and quantifying PV plant oper-
ation and management, providing comprehensible results for multiple
stakeholders to monitor plant operation over time. Based on the clas-
sification scheme obtained from Rediske et al. [6], Table 4 categorizes
PV system KPIs into operation, economic, and maintenance KPIs. This
classification scheme is used to classify articles within this cluster,
enabling a comprehensive evaluation of various aspects related to PV
system performance.
4.1. Operation KPIs
Operation KPIs play a crucial role in assessing the performance of
PV plants in generating and delivering electricity. The International
Electrotechnical Commission (IEC) [181] has established the standard
IEC 61724, which outlines the essential parameters for evaluating the
performance of solar PV systems. These indicators define the perfor-
mance of the plant and allow comparisons between plants based on
factors such as location, solar irradiation, technology, energy genera-
tion, and system losses. For example, the soiling ratio (𝑆𝑅) quantifies
the impact of dirt and debris on the performance of PV arrays. In
addition, energy-based availability (𝐸𝐴) calculates the ratio between
the actual energy produced by the system and the maximum potential
energy that could be generated if the system operated continuously for
a specific time frame [137]. It is important to differentiate between
energy-based and time-based availability, a distinction that will be
examined in Section 4.3. Both metrics are crucial for evaluating PV
system performance and assessing the effectiveness of maintenance
strategies.
Significant research has been conducted on the performance evalu-
ation of large-scale PV systems, primarily focused on the MW range [59,
60,62–67,89,98,99,116,130,134–139].
Additionally,
studies
have
shown interest in evaluating the performance of utility-scale PV fleets,
which face specific operational challenges, by employing various opera-
tional metrics [140–147]. For example, Lindig et al. [142] conducted a
comprehensive study in Europe, focusing on an extensive fleet of more
than 8400 PV systems. Their main goal was to compute the annual
final yield (𝑌𝑓) and performance ratio (𝑃𝑅) of these systems, offering
valuable insights into managing vast PV performance data. The study
underscored the significance of effective O&M practices in reducing
system losses.
4.2. Economic KPIs
The financial aspects of a PV plant are based on different eco-
nomic indicators. Capital expenditure (𝐶𝐴𝑃𝐸𝑋) represents the initial
costs of PV installations, while operational expenditure (𝑂𝑃𝐸𝑋) covers
expenses related to site operation, maintenance, taxes, labor, and out-
sourced services, among others. These metrics are commonly used in
the literature to assess the cost competitiveness of PV installations [68,
84,154–157]. For example, Muñoz-Cerón et al. [68] investigated the
financial impact of 𝑂𝑃𝐸𝑋on the performance and viability of a
utility-scale PV plant in Spain. Their findings suggested that, in certain
scenarios, it may be financially advantageous to prioritize corrective
actions over preventive maintenance, rather than investing in regular
O&M activities. However, relying solely on capital and operational
expenses may not offer a complete insight into the profitability of the
system.
Additional parameters, including the levelized cost of energy
(𝐿𝐶𝑜𝐸), net present value (𝑁𝑃𝑉), and internal rate of return (𝐼𝑅𝑅),
have been considered to provide a more comprehensive understand-
ing [5,55,56,61,75,111,154,156,158–164]. These indicators incorpo-
rate factors such as the lifetime of the system and energy yield,


---

Page 11

---

Renewable and Sustainable Energy Reviews 195 (2024) 114342
11
H. Abdulla et al.
Table 4
Key performance indicators for O&M management of PV systems.
Group
KPIs
Operations
[59,60,62–67,85,89,98–100,116,130–132,134–153]
Array yield (𝑌𝑎) = Actual array output energy (kWh) DC
Rated power (kW)
Final yield (𝑌𝑓) = Actual AC output energy (kWh) AC
Rated power (kW)
Reference yield (𝑌𝑟) =
Solar radiation on PV panel (kWh/m2)
Standard test condition reference irradiance (kW/m2)
Performance ratio (𝑃𝑅) =
Final yield (h)
Reference yield (h)
Performance index (𝑃𝐼) =
Actual AC output energy (kWh) AC
Global radiation (kWh) × System efficiency (%) × Inverter efficiency (%)
Capacity factor (𝐶𝐹) = Energy production in period 𝑡(kWh) AC
Rated power (kW) × Time interval (h)
Soiling ratio (𝑆𝑅) = Soiled PV array power output (kWh)
Clean PV array power output (kWh)
Array efficiency (𝜂𝐴) =
Actual array output energy (kWh) DC
Active array area (m2) × Total radiation on panel surface (kWh/m2)
Inverter efficiency (𝜂𝑖𝑛𝑣) =
Actual AC output energy (kWh) AC
Actual array output energy (kWh) DC
System efficiency (𝜂𝑝𝑣) =
Actual AC output energy (kWh) AC
Active array area (m2) × Solar radiation on PV panel (kWh/m2)
Energy-based availability (𝐸𝐴) = Actual AC output energy (kWh) AC
Energy potentially expected (kWh)
Economics [5,55,56,61,68,75,84,111,154–164]
Capital expenditures (𝐶𝐴𝑃𝐸𝑋) = Cost per peak power ($/kWp) × Total peak power (kWp)
Operational expenditures (𝑂𝑃𝐸𝑋) = Operational expenditures ($)
Rated power (kW)
Levelized cost of energy (𝐿𝐶𝑜𝐸) =
Total life cycle costs ($)
Total lifetime energy output (kWh)
Net present value (𝑁𝑃𝑉) =
𝑇∑
𝑡=0
Net cash flow during year 𝑡($)
(1 + Discount rate (%))𝑡
−Capital expenditures ($)
Internal rate of return (𝐼𝑅𝑅) =
𝑇∑
𝑡=0
Net cash flow during year 𝑡($)
(1 + Internal rate of return (%))𝑡−Capital expenditures ($) = 0
Technical maintenance
[56,57,70,119,134,138,142,165–178]
Mean time between failures (𝑀𝑇𝐵𝐹) = System operation time (h)
Number of failures
Mean time to repair (𝑀𝑇𝑇𝑅) = Total repair time (h)
Number of failures
Mean time to failure (𝑀𝑇𝑇𝐹) =
System operation time (h)
Number of non-repairable failures
System degradation (𝐷𝑆) = Current year power (kW)
Previous year power (kW)
Response time (𝑅𝑇) =
Failure detection time (h)
Failure intervention time (h)
Reliability (𝑅𝑡) = 𝑒−failure rate (failures/h)×time (h)
Availability (𝐴𝑡) =
System operation time (h)
Expected operational time (h)
Corrective maintenance ratio (𝐶𝑀) = Number of corrective interventions
Total number of interventions
Preventive maintenance ratio (𝑃𝑀) = Number of preventive interventions
Total number of interventions
Economic maintenance [56,75,111,159,179,180]
Equivalent labor cost (𝐸𝐿𝐶) = Maintenance labor cost ($)
Total maintenance cost ($)
Equivalent spare parts cost (𝐸𝑆𝑃𝐶) =
Spare parts cost ($)
Total maintenance cost ($)
Maintenance planning factor (𝑀𝑃) = Annual maintenance budget ($)
Total maintenance cost ($)
enabling a deeper analysis of the financial performance of the PV plant.
The 𝐿𝐶𝑜𝐸is particularly popular as a standard unit of energy cost
measurement to evaluate the financial viability of PV installations. This
metric calculates the total cost of constructing and operating a PV plant
over its lifetime, as a ratio to the total electricity output. It is projected
that the 𝐿𝐶𝑜𝐸will decrease by 0.8% to 1.4% between 2015 and 2030,
driven by advancements and innovations in O&M services within the
PV industry [138,182]. This decrease drives global PV system adoption,
emphasizing the need to prioritize system uptime and minimize O&M
expenses to achieve a favorable 𝐿𝐶𝑜𝐸value.
4.3. Maintenance KPIs
Efficient maintenance analysis is crucial to ensure the optimal per-
formance and long-term reliability of PV systems. This involves select-
ing the appropriate maintenance strategy and evaluating its effective-
ness using various measures. Maintenance KPIs play a vital role in
helping managers make strategic decisions to optimize the operation
of PV plants. These KPIs assess maintenance quality based on factors
such as intervention time and associated costs, classified as technical
and economic indicators.
Maintenance-related technical indicators focus on assessing the re-
liability and availability of equipment, as well as the workforce re-
sponsible for repair procedures. In the context of PV systems, relia-
bility (𝑅𝑡) refers to the system’s ability to operate efficiently with-
out failures throughout its expected useful life, typically 25 years or
more [183]. Availability (𝐴𝑡), or time-based availability, is a reliability
metric that assesses the uninterrupted power generation capability of
a PV system. It measures plant operation time, including scheduled
maintenance, repairs, and unexpected failures, without interruptions or
limitations [184]. The industry employs various indicators to evaluate
the reliability and availability of PV systems. The most commonly used
indicators include mean time between failures (𝑀𝑇𝐵𝐹) and failure


---

Page 12

---

Renewable and Sustainable Energy Reviews 195 (2024) 114342
12
H. Abdulla et al.
Table 5
Methods for evaluating the reliability of PV systems and components.
Reference(s)
Methods used for reliability evaluation
RBD
FTA
Markov chains
Monte Carlo
Others
[73,168,185]
✓
[154]
✓
✓
[186]
✓
✓
[70,72,78,167,187–190]
✓
[191]
✓
✓
[192]
✓Petri networks
[69,193,194]
✓State enumeration
[195]
✓
✓Bayesian networks
[74–76,165,196]
✓
[197,198]
✓
✓
[56,199–202]
✓
rate, mean time to repair (𝑀𝑇𝑇𝑅) and repair rate, and mean time to
failure (𝑀𝑇𝑇𝐹) [70,165–171,176].
In addition, system degradation (𝐷𝑆) measures the decrease in
efficiency of a PV system over time, quantifying the annual decrease in
production as a percentage of the total annual output [57,134,142,172–
175]. For example, a degradation rate of 0.5% per year means a 5%
reduction in generation capacity each year compared to the previous
year. Other maintenance metrics such as response time (𝑅𝑇) and the
proportions of corrective maintenance (𝐶𝑀) and preventive mainte-
nance (𝑃𝑀) have been utilized for both the entire PV plant and specific
subsystems with multiple arrays and inverters [56,119,138].
Maintenance-related economic indicators are vital to assess the
financial viability of the PV plant [56,75,111,159,179,180]. Indicators
such as equivalent labor cost (𝐸𝐿𝐶) and equivalent spare parts cost
(𝐸𝑆𝑃𝐶) evaluate labor and spare parts costs as percentages of the total
maintenance cost. These indicators help optimize resource allocation
and enhance maintenance strategies to improve performance and cost
control. The maintenance planning (𝑀𝑃) factor is determined by as-
sessing the efficiency of the total maintenance cost in relation to the
annual maintenance budget. This evaluation ensures that maintenance
costs are adequately covered while optimizing the planning process.
In their study, Peters and Madlener [56] compared the economic
feasibility of preventive and corrective maintenance strategies for PV
plants of different sizes in Germany. The authors found that preven-
tive maintenance is more cost-effective, as it reduces downtime and
increases energy yield. However, it was highlighted that the optimal
maintenance strategy depends on factors such as plant size, PV module
type, and local climate conditions. Thus, a systematic approach to
maintenance planning and optimization can help maximize economic
benefits.
5. Analysis of degradation modeling approaches
The evolving nature of PV system deterioration and fault progres-
sion presents a significant challenge in creating precise models and
assessing the overall reliability of the system. The reliability of PV
systems has been a concern for more than a decade due to their
complexity, making it challenging to evaluate the overall reliability.
Until recent years, reliability assessment was focused on individual
components, mainly modules and inverters, using failure data [203,
204]. Accurate measurement of reliability is crucial for evaluating
energy output, O&M expenses, and estimating 𝐿𝐶𝑜𝐸, as evidenced by
the numerous publications on this topic.
The growth of PV installations has intensified the focus on assessing
and quantifying the reliability of large-scale PV systems [69,70,72,
75,78,167,168,186,188,189,192,197,198,201,205]. This involves eval-
uating the reliability of subsystems and individual components and
understanding their impact on the overall system reliability. Addition-
ally, it is essential to identify critical components that are more prone
to failure or malfunction to implement suitable maintenance measures.
In the analysis of larger PV systems, factors such as weather conditions,
maintenance schedules, and overall system performance need to be
considered in the reliability assessment. For example, Altamimi and
Jayaweera [198] conducted a comprehensive analysis of a 1 MW PV
farm, identifying critical components and subsystems prone to climate-
related failures. Their reliability model incorporated geographical and
environmental factors, such as cloud shading and climate change, to
provide a comprehensive analysis.
5.1. Reliability modeling techniques
Studies have used different techniques to assess the reliability and
availability of PV systems and their components. Table 5 illustrates the
most common reliability analysis techniques, such as reliability block
diagrams (RBD), fault tree analysis (FTA), Markov chains, Monte Carlo
simulations, among others.
Although various reliability analysis techniques have been em-
ployed, certain methods have inherent limitations. For example, FTA
is suitable for small-scale systems, but it struggles to handle intercon-
nected modes effectively [116]. To accurately represent PV systems, a
multi-state model is necessary to account for the intermittent nature
of solar radiation. This requires a modeling approach that captures the
stochastic behavior and dynamic characteristics of the components. It
is important to note that the failure of PV modules does not necessarily
result in a complete system failure, but rather a partial failure that
leads to reduced power output. FTA and RBD are restricted to han-
dling only binary states (down or functional) [116]. To address these
limitations, alternative stochastic methods such as Markov models have
been extensively utilized in the literature. These approaches enable the
accurate characterization of MTTF in PV systems, providing a more
comprehensive understanding of system performance.
5.2. PV reliability and effects on economics
Several articles have integrated reliability models in their cost anal-
ysis to estimate or minimize the effect of component failure on the
economics of PV systems [56,74–76,78,166,200,202,206]. Shin et al.
[206] developed a reliability-centered approach to O&M scheduling of
PV components and evaluated the scheduling plan considering the du-
ration of failure. Their results suggested that it is more cost-effective to
implement corrective replacement instead of preventive maintenance,
due to the low failure rate. Similarly, Baschel et al. [78] concluded
that while certain components could theoretically be repaired sooner,
arranging a maintenance visit is often not cost-effective when the
failure has only a minimal impact on the system’s energy yield. These
studies aimed to assess and mitigate the financial consequences that
arise from component failure within PV plants, allowing stakeholders
to make informed decisions about maintenance strategies, component
selection, and overall system design.


---

Page 13

---

Renewable and Sustainable Energy Reviews 195 (2024) 114342
13
H. Abdulla et al.
Table 6
Utilized methods for criticality analysis and quantification of technical risks in PV systems.
Reference(s)
Criticality and risk analysis method
FMEA/FMECA
RAM
MCD
FV
CPN
[71,84,112,119,128,159,175,207,208]
✓
[77]
✓
✓
[5]
✓
✓
✓
✓
[73,168,171,180]
✓
[176]
✓
✓
[111]
✓
[190]
✓
[18,209]
✓
✓
5.3. PV reliability and criticality analysis
Integration of reliability, criticality analysis, and technical risk
quantification has led to the development of prioritization functions
that support O&M teams in efficient and cost-effective maintenance
scheduling. With limited resources, the optimal selection of compo-
nents for maintenance becomes crucial. Reliability-centered mainte-
nance is a crucial process that incorporates reliability analysis and iden-
tification of critical components. It assesses the economic implications
to tailor maintenance strategies, facilitating effective prioritization
and scheduling of corrective actions [84]. PV research has introduced
various approaches to assess component criticality and mitigate main-
tenance incident risks, aiming to minimize energy generation losses.
Table 6 presents an overview of these methods.
These methods include failure modes and effect analysis (FMEA)/
failure mode, effects, and criticality analysis (FMECA), reliability,
availability, and maintainability (RAM) analysis, multi-criteria decision
analysis (MCDA), Fussel–Vesely (FV) importance, and cost priority
number (CPN). For example, Bansal et al. [175] used FMECA to
analyze degradation and failures in a 5 MW PV plant operating in a
hot semi-arid climate. The study focused on O&M practices, module
degradation, and reliability assessment, identifying dark encapsulant
discoloration as a significant and damaging defect that accelerated
plant deterioration. Similarly, Barkhouse et al. [209] employed a cost-
based FMEA with CPN to prioritize risks based on their economic
impact, highlighting major failures in PV modules and inverters. These
methods provide valuable insights for decision-making and resource
allocation to minimize energy generation losses.
6. Review of maintenance optimization and inspection planning
approaches
In recent years, there has been a growing interest in the field of
optimization of maintenance policies and inspection planning for PV
systems. Table 7 offers a comprehensive compilation of studies related
to PV maintenance optimization, highlighting optimization outcomes
and influential factors.
In addition, a detailed description of the key elements used in
the formulation of optimization models within the studies has been
included. This comprehensive overview, depicted in Fig. 9, provides
a thorough understanding of the current focus and methodologies used
to optimize and plan PV maintenance activities.
6.1. Objectives in PV maintenance optimization
Maintenance schedules for PV systems are usually based on best
practices and heuristics [4], lacking structured optimization models.
Aboagye et al. [57] examined the impact of design, installation, and
O&M practices on PV system performance in different climatic zones
in Ghana. The authors used data from measurements, interviews, pho-
tography, and visual inspections to propose maintenance schedules.
However, these schedules may not be optimal as they are heavily
based on subjective recommendations from system owners. Most PV
plants employ a combination of corrective and preventive maintenance
according to the manufacturer’s guidelines and best practices [4].
Although immediate corrective maintenance ensures high availability,
it may not always be cost-effective. Hence, it is essential to adopt a
systematic approach to optimize the maintenance strategy and achieve
a balance between various objectives in PV systems.
The primary focus of PV maintenance optimization has been to
achieve various crucial objectives, including maximizing reliability and
availability, minimizing expected costs, optimizing scheduling oper-
ations, and efficiently allocating resources. In their studies, Mahani
et al. [88] and Baklouti et al. [91] proposed optimization strategies to
minimize the overall expected maintenance cost in solar PV systems.
The first study considered penalty costs resulting from performance
degradation or failure, while the second study highlighted the impor-
tance of the reliability threshold in identifying components that require
maintenance. Similarly, Sa’ad et al. [180] developed an algorithm to
optimize the selection and cost of preventive maintenance actions in PV
systems. This algorithm led to the implementation of five maintenance
actions performed in multiple streaks, targeting components based on
their reliability index.
Research has also explored the integration of maintenance consider-
ations into the design of renewable energy systems. Jiménez-Fernández
et al. [87] conducted a study on a standalone PV-hydrogen facility.
Their objective was to determine an optimal maintenance plan consid-
ering system size and maintenance visits, with the aim of minimizing
the total annual cost. Other studies have focused on prioritizing system
reliability and availability. For example, Sa’ad et al. [210] proposed
an optimal preventive maintenance strategy that takes into account
environmental conditions to achieve maximum availability. Research
has shown a growing interest in utilizing a multi-objective optimization
approach for PV maintenance. This approach aims to maximize the
reliability and availability of the system while minimizing overall
maintenance costs. The studies conducted by Li et al. [222], Sa’ad
et al. [180], Chen et al. [223], and Qi et al. [224] have explored this
approach, recognizing the interdependencies between these objectives
and seeking a balanced solution.
6.2. Approaches for PV maintenance optimization
Once O&M objectives and strategies are set, the decision-making
process for maintenance parameters can be enhanced through the
application of modeling and optimization techniques. These techniques
can be broadly categorized into qualitative analysis, which relies on
subjective judgments [57], and quantitative analysis, which utilizes
mathematical and statistical methods. The quantitative methods used
in optimizing PV maintenance studies are presented in Table 8, and
include operations research models such as integer programming (IP),
mixed integer programming (MIP), dynamic programming (DP), and
problem-specific models such as the traveling salesman problem (TSP).
In addition, stochastic models focus on probabilistic modeling and
simulation, including Markov chains and stochastic simulation tools.
Analytical models offer precise closed-form solutions for the prediction
of PV system behavior through mathematical equations. Intelligent
algorithmic models, such as ML and deep learning, predict PV system
performance and guide maintenance planning. Metaheuristic search


---

Page 14

---

Renewable and Sustainable Energy Reviews 195 (2024) 114342
14
H. Abdulla et al.
Table 7
Classification of papers on PV maintenance optimization and inspection planning based on outcomes and factors considered.
Reference(s)
Outcome
Factors affecting PV maintenance optimization and planning
Assessment of
maintenance
alternatives
Optimal
maintenance
strategy
Optimal component
grouping for
maintenance
Optimized
resources
Reliability
indicators
Economic
parameters
Weather
factors
Resource
logistics
management
Route
planning
[111]
✓
✓
✓
✓
✓
✓
[113]
✓
✓
✓
✓
[5,112]
✓
✓
✓
✓
✓
[206]
✓
✓
✓
✓
[180]
✓
✓
✓
[210]
✓
✓
✓
✓
[211]
✓
✓
✓
✓
[131,149,212]
✓
✓
[80–83,85–87,132,139,
148,151,153,213–220]
✓
✓
✓
[150]
✓
✓
✓
✓
[221]
✓
✓
✓
✓
[222,223]
✓
✓
✓
✓
✓
[88,91,224]
✓
✓
✓
[56]
✓
✓
✓
✓
✓
[165]
✓
✓
✓
[225,226]
✓
✓
✓
[155,157]
✓
✓
✓
✓
✓
[159]
✓
✓
✓
✓
[227]
✓
✓
✓
✓
[228–236]
✓
✓
✓
Fig. 9. Key elements in PV maintenance optimization. Note: NPV — net present value, UAVs — unmanned aerial vehicles, DSS — decision support system, ML — machine
learning, DL — deep learning, O&M — Operation and maintenance.
algorithms, such as genetic and evolutionary algorithms also play a
role. Some studies combined elements from these various method-
ologies, while others relied on experimental analysis to inform their
maintenance optimization approaches.
Research has also developed decision tools for PV system O&M
scheduling, guiding operators on timing, frequency, and task sequenc-
ing. In a study by Kothona et al. [111], MCDA was used to rank
maintenance plans for six PV plants in Türkiye, considering criteria
such as personnel expertise, fault severity, and travel time. The model
also assessed maintenance costs, including fuel and labor, and the costs
associated with energy losses caused by faults. Additionally, DSS as
demonstrated by Livera et al. [5,112,113] and Lindig et al. [237],
provided data analysis, reporting, and visualization features, offering
quantitative assessments of issues and recommending O&M actions for
performance optimization. For instance, Livera et al. [5] discovered
that implementing extra cleaning for a PV plant was not cost-effective,
and their DSS recommended deferring the cleaning event until the next
periodic maintenance.
6.3. PV cleaning scheduling
Regular cleaning is crucial for optimal energy production in PV
systems due to the negative impact of dirt accumulation on solar panels,
known as ‘‘soiling’’ [79]. In the United States, the cost of cleaning a


---

Page 15

---

Renewable and Sustainable Energy Reviews 195 (2024) 114342
15
H. Abdulla et al.
Table 8
Overview of literature approaches for optimizing PV maintenance and inspection planning.
Reference(s)
Operations
research models
(IP, MIP, DP, TSP)
Stochastic models
(Simulation,
Markov chains)
Analytical
models
Intelligent
algorithmic
models
Metaheuristic
Search
algorithms
Decision support
systems (DSS)
and tools
Experimental
analysis
[155,157,218,220,225,233]
✓
[131,139,159,165,206,216,
217,220]
✓
[56,80,83,85,86,91,132,148–
151,153,180,210,215,219,226]
✓
[81,214,230,232,235]
✓
[87,211,227–229,231,236]
✓
[111–113]
✓
[213,222,223]
✓
✓
[88]
✓
✓
[224]
✓
✓
[221,234]
✓
✓
[82,212]
✓
10 MW system with 365 Watt-rated modules would exceed $5000 for
one-time cleaning. Therefore, careful consideration of the economic
benefits and associated costs is important when planning the cleaning
schedule [131]. The MENA region, with its dusty environment and
frequent sandstorms, presents significant challenges for solar panels. In
the worst-case scenario, these conditions can cause an 80% reduction
in panel efficiency [212]. Soiling in the PV field has gained attention
as an optimization problem, with the aim of finding the best cleaning
strategy (frequency or interval) to minimize expenses and maximize
productivity.
Numerous studies have focused on determining cleaning sched-
ules for soiled PV plants, especially large-scale systems [80–83,85,86,
132,139,148–151,153,213–218,220,221]. While some studies relied on
operational experience or predetermined power loss thresholds to rec-
ommend cleaning schedules [132,139], neglecting site-specific factors
such as local climate and geographical location can result in financial
losses. Many research efforts utilized empirical methods incorporating
meteorological parameters to create models that quantify performance
reduction due to soiling. These models were then combined with factors
such as cleaning costs, revenue generation, electricity prices, and 𝐿𝐶𝑜𝐸
to determine the optimal cleaning frequency. Although Wang et al.
[219] focused on a small-scale PV plant, they successfully developed
a cleaning schedule that leverages environmental forecasts, PV power
generation, and dust deposition. This approach improves resource uti-
lization, reduces costs, and optimizes PV system performance. The
methodology showed great potential and can be extended to large-scale
PV systems.
Stochastic approaches have also been investigated to determine
the optimal cleaning frequency for utility-scale PV plants [213,216,
217,220]. For instance, Cheema et al. [213] introduced an innovative
method for optimizing PV system cleaning schedules. This method
uses virtual scenarios to predict dust accumulation and actively adjusts
cleaning schedules based on changing conditions, outperforming fixed
schedules. In a study by González-Castillo et al. [220], a stochastic
Markov decision process was employed to handle environmental un-
certainty, especially concerning rainfall and irradiance, in maintenance
scheduling. This approach treated the problem as a stochastic optimiza-
tion problem, factoring in various weather scenarios to make optimal
cleaning decisions under uncertainty.
6.4. Optimizing maintenance resources
Resource optimization strategies involve identifying critical compo-
nents and maintaining spare parts inventories to minimize downtime
and maximize system performance. Efficient resource optimization is
crucial for managing multiple O&M bases and PV systems, particularly
in remote areas. Conventional preventive maintenance policies aim to
reduce system downtime, but relying solely on subjective risk assess-
ment and operator expectations for spare parts can be problematic. In
practice, critical spare parts are stored near the site to minimize losses
caused by delayed deliveries [238]. However, the dynamic nature of
PV systems introduces uncertainties and unexpected failures. Accurate
risk assessment and spare parts management require a systematic, data-
driven approach that considers equipment reliability, failure patterns,
historical data, and predictive maintenance techniques.
Several research studies have explored the integration of main-
tenance resources, such as personnel management and spare parts
inventory, in the evaluation of energy yield and operational costs of
PV systems [56,111,154,155,157,159,165,211,225–227,239]. Logistic
delay time, including spare parts replenishment and crew arrival, is
critical for evaluating PV system availability and functionality restora-
tion. The resulting downtime greatly impacts plant performance and
productivity [56,154]. In their study, Peters and Madlener [56] con-
sidered component reliability, operational costs, and the driving time
of the service team to the PV plant, with the objective of determining an
optimal maintenance strategy that minimizes total maintenance costs.
Other studies have expanded their focus beyond the deterministic
delay time of PV spare parts, emphasizing the stochastic nature of spare
parts inventory and maintenance activities. These studies used proba-
bilistic models, Markov chains, and optimization techniques to provide
valuable insights into spare parts inventory planning and optimiza-
tion [159,165]. Guo et al. [159] developed an optimization model that
integrated spare parts inventory policies for micro-inverter PV systems,
combining continuous-time Markov chains with stochastic inventory
theory to optimize the energy yield of the system. Similarly, Oprea
et al. [165] utilized a probabilistic model based on Markov chains
to calculate the reliability index. This index guided the proposal of
maintenance activities that optimized spare parts inventory, ensuring
a timely response to equipment failures.
The provision of electricity to remote areas with limited access
to traditional electrical networks has been addressed using renewable
energy sources such as PV and wind systems [240]. The electrification
of rural areas, particularly through off-grid PV systems, has emerged
as a promising solution. Operational costs, such as spare parts and
logistics, are crucial due to factors such as population sparsity, difficult
access, and maintenance requirements in remote areas [6]. Several
studies have focused on optimizing maintenance activities in off-grid
systems, particularly in the context of rural electrification programs
using solar home systems [155,157,225,226]. In Morocco, case studies
were conducted to minimize maintenance costs [225,226], considering
factors such as location, transportation conditions, and daily dispatch of
teams and vehicles. These studies identified optimal agency locations,
optimized maintenance structures, scheduled preventive maintenance
and fee collection, and calculated the total service cost.


---

Page 16

---

Renewable and Sustainable Energy Reviews 195 (2024) 114342
16
H. Abdulla et al.
6.5. Optimizing the planning of transport and inspection routes
To ensure optimal performance, careful planning of transport routes
and finding the most efficient maintenance path are crucial. Several
studies have focused on determining the optimal maintenance path
considering available resources [155,157,211,221,227]. The objective
is to improve maintenance processes, reduce travel time and costs,
and optimize resource utilization. In the field of PV maintenance,
metaheuristic and computational intelligence algorithms have been
used for route planning and scheduling. For example, Yin et al. [211]
combined particle swarm optimization and genetic algorithm to find
efficient routes to dispatch personnel and schedule intelligent devices
for inspecting distributed PV systems. Hua et al. [227] applied a genetic
algorithm to determine an optimal path for maintenance teams han-
dling large-scale distributed PV plants. Their study considered factors
such as cost, multiple technicians, multipoint departure and different
dispatch conditions, providing flexibility in setting arrival times or
minimizing transportation costs.
Other studies used the TSP as a modeling framework to optimize
transportation routes in off-grid PV systems [155,157]. These studies
considered factors such as distance, road conditions, environmental
complexity, and availability of transportation resources. The objective
is to optimize maintenance schedules and enhance effectiveness by
coordinating task scheduling, transport route planning, team dispatch,
inventory estimation, and vehicle estimation. In addition, TSP has been
employed to plan PV cleaning routes in large-scale PV plants. Wang
et al. [221] expanded the conventional TSP to a production-driven
TSP with time-dependent cost. Their primary focus was optimizing the
temporal scheduling and spatial routing for PV cleaning, with the aim
of minimizing the overall economic loss associated with the cleaning
process.
Since the long-term performance of PV plants is influenced by
environmental factors and potential module faults, regular inspection
is crucial. Given the large scale and distribution of current solar infras-
tructures, consisting of more than 10 000 modules, UAVs are well suited
for efficient visual inspections. Consequently, efforts have been directed
towards optimizing UAV path planning for monitoring and inspection
of PV systems [228–236]. The main challenge lies in scheduling, which
involves determining the most efficient path to visit all modules and
collect maintenance data. The objective is to minimize the energy
consumption of the UAVs during inspections and to significantly reduce
the aerial inspection time. For example, An et al. [228] proposed a
novel scheduling model and evolutionary algorithm to optimize remote
sensing schedules for UAV swarms in urban distributed PV arrays. Their
approach was to assign tasks to UAVs, minimizing total inspection time
while maximizing maintenance efficiency. Furthermore, Di Placido
et al. [234] introduced the close-enough TSP and proposed a novel
genetic algorithm to minimize the length of UAV inspection routes to
assess the operational condition of PV fields.
7. Research gaps and perspectives into the future
This study has identified three critical research domains that re-
quire further exploration and development. These domains include
PV maintenance strategies, maintenance practices for large-scale and
distributed PV installations, and optimization and scheduling of main-
tenance activities. The representation of these research gaps in Fig. 10
serves as a valuable roadmap, guiding future research efforts aimed at
advancing the O&M landscape of PV systems.
The O&M of PV systems places greater emphasis on diagnosis than
prognosis, as the latter is still in development. The wind energy sector
has made progress in data-driven predictive maintenance [241–244],
while the solar PV industry is still in its early stages, with limited
research mainly on PV modules or inverters. The complexity of multiple
components and interdependencies, especially in large-scale systems,
poses challenges. As PV farms expand rapidly, the transition from
corrective maintenance to predictive maintenance is crucial to improve
operational efficiency. Although corrective maintenance will remain a
priority in addressing equipment damage, the PV energy sector antici-
pates significant advances in predictive maintenance. Artificial intelli-
gence techniques, Internet of things devices, and digitization facilitated
by digital twin technologies are driving this advancement, aiming to
replicate expected system behavior and improving the management and
operation of the PV plant [245].
Furthermore, when dealing with large PV portfolios, which involve
installations such as farms, parks, and distributed fleets across multi-
ple sites, the lack of well-established maintenance strategies becomes
apparent. The expansion of PV installations introduces manufacturing
and cost challenges, necessitating a reevaluation of O&M practices to
adapt to the evolving dynamics of the solar industry. Scaling up mainte-
nance practices while addressing resource limitations poses significant
challenges. It is essential to consider interdependencies among PV
systems, as they impact neighboring systems and fleet performance. Ex-
isting single-unit maintenance models serve as a foundation, but fail to
address real-world complexities. In addition, component-level models
often assume independence among components, neglecting stochastic
dependencies within PV systems. This is reflected by the industry’s pre-
dominant focus on individual component availability, often neglecting
the broader system’s availability perspective.
Although advances are being achieved in developing KPIs for large-
scale PV installations, these indicators may not comprehensively cap-
ture individual system performance and the complex interdependencies
within multi-system fleets. Traditional KPIs often focus on factors such
as energy generation and efficiency for individual PV systems, over-
looking how the performance of one system affects others in the same
fleet. Factors such as mutual panel shading, load distribution, and
resource sharing can significantly impact overall fleet performance.
Standardized metrics are essential for a comprehensive evaluation of
system performance and maintenance effectiveness. Specialized indica-
tor models should be developed to monitor and predict O&M outcomes,
especially for difficult-to-access large installations. The expansion of PV
projects requires a well-coordinated approach that involves multiple
stakeholders and the establishment of clear channels and collaborative
tools.
A notable gap in the existing literature revolves around the limited
attention given to PV system maintenance optimization, which has
primarily focused on individual components, especially in the context
of optimizing PV module cleaning schedules. This approach tends to
overlook the comprehensive perspective of the entire plant. In contrast,
the field of wind farms O&M optimization has seen substantial devel-
opment, but the same level of emphasis has not been placed on the
maintenance of PV systems. This disparity arises from the fundamental
differences between the two fields, which complicates the direct appli-
cation of the findings from the wind industry to the PV sector. Wind
farms involve a diverse range of complex configurations, including
onshore and offshore installations, each posing unique operational
challenges. Conversely, PV systems tend to exhibit a more standardized
structure with fewer moving parts, simplifying maintenance procedures
compared to the intricate nature of wind turbines. Hence, insights and
methodologies from wind farms O&M optimization may not be directly
applied to PV systems due to their distinct characteristics and inherent
differences as renewable energy technologies.
It is crucial to recognize that current PV optimization models pre-
dominantly revolve around fixed maintenance schedules, which prove
inadequate for modern large-scale PV systems. These expansive installa-
tions span vast areas, leading to varying levels of soiling across different
zones within the solar field. Implementing fixed cleaning schedules
for the entire installation can prove impractical and expensive. The
complexity increases when managing multi-system fleets, as different
systems exhibit unique cleaning requirements, with some necessitat-
ing more frequent cleaning than others. To maximize efficiency, it is


---

Page 17

---

Renewable and Sustainable Energy Reviews 195 (2024) 114342
17
H. Abdulla et al.
Fig. 10. Identified research gaps in PV system maintenance literature.
crucial to consider the unique characteristics and operational require-
ments of each system when developing maintenance plans. Tailoring
maintenance strategies to site-specific challenges, such as location and
climate, requires customized approaches, regular site assessments, and
the adoption of adaptive maintenance protocols.
Furthermore, within the PV industry, the prevailing research focus
often centers on short-term optimization and immediate maintenance,
often failing to consider the potential enduring effects on system per-
formance. Despite progress in dynamic maintenance strategies, the
literature in the PV field generally tends to neglect the persistent conse-
quences of maintenance actions, their interconnected nature, and their
susceptibility to changing factors. An emerging and adaptable approach
that is gaining interest is prescriptive maintenance, as discussed by Fox
et al. [242], employing reinforcement learning (RL) to directly identify
optimal actions, eliminating the need for predefined strategies. The
use of RL techniques in the PV industry has been limited, with recent
research focusing primarily on fault detection in specific components
such as inverters [117] and arrays [246,247].
RL has also been applied to optimize operational scheduling in
solar thermal energy-driven hot water systems [248] and wind farm
O&M [249]. These studies highlight the potential of using RL tech-
niques to efficiently optimize long-term PV system maintenance. This
approach ensures that maintenance decisions are aligned with the
core goals of enhancing system reliability, maximizing efficiency, and
promoting sustainability. Additionally, RL offers the opportunity to
introduce customized KPIs for large PV installations, addressing a
previously identified research gap within this study. The integration of
RL offers the capability to fine-tune the performance evaluation criteria
within particular environmental and operational contexts, whether at
the system or fleet level. Therefore, expanding the application of RL
techniques in PV O&M creates an opportunity to ensure the continued
relevance and effectiveness of KPIs, thereby continuously enhancing the
performance and maintenance action of PV systems.
8. Conclusion
This systematic review explores the current literature on O&M
management for PV systems. With the growing capacity of PV systems,
there is growing recognition of the critical necessity for systematic
O&M practices to guarantee sustained performance and longevity. The
advancements in maintenance practices and operational enhancements
implemented by other renewable energy sectors, particularly the wind
industry, have set a standard for the PV sector. As a result, this
review goes beyond the usual technical focus in PV energy, incorpo-
rating planning and organizational factors into the broader mainte-
nance discussion. Through the application of the PRISMA framework
and bibliometric analysis, the examination of 186 articles revealed
four interconnected research domains: maintenance strategies, KPIs,
degradation modeling, and maintenance optimization and planning.
Analysis of thematic evolution reveals that maintenance receives
relatively less emphasis in PV research compared to other operational
aspects of energy management. Various maintenance strategies have
been investigated for PV systems, each with its own importance. How-
ever, relying solely on a single maintenance strategy may be ineffective,
especially for large-scale installations. Strategic selection and synergis-
tic integration of maintenance strategies significantly improve system
reliability. The management of O&M for PV systems is also closely
related to a range of operational, economic, and maintenance-related
KPIs. The integrated consideration of these KPIs guides decision-making
processes by helping managers prioritize efficient maintenance actions.
Modeling PV system degradation is also crucial to identify critical com-
ponents and implement effective maintenance measures. Integrating
the reliability assessment with the criticality analysis, economic con-
siderations, and quantification of technical risks supports informed de-
cision making on maintenance strategies and component selection. The
literature on PV maintenance optimization places a primary emphasis
on scheduling PV panel cleaning to mitigate the impact of soiling,
considering economic factors. A structured maintenance optimization
approach, utilizing various modeling and optimization techniques, is
essential to achieve key objectives such as maximizing availability,
minimizing costs and travel time, and efficiently allocating resources.
Furthermore, this review highlights gaps in the current literature,
emphasizing areas that require further research. Maintenance strategies
for PV systems prioritize diagnostic activities over prognostic measures
and lack the integration of predictive maintenance. Additionally, there
is insufficient attention to large-scale maintenance, with a tendency to
prioritize component repair over holistic system considerations. Chal-
lenges in PV system maintenance scheduling and optimization include a
component-centric focus, a single-objective approach, and reliance on
static schedules that neglect the long-term maintenance impact. The
growing PV sector requires strategic planning that involves multiple
stakeholders in a well-coordinated maintenance approach. Intelligent
technologies, such as Internet of things and digital twins, are vital for
coordinated maintenance and resource sharing, enabling virtual test-
ing. Improved communication, collaboration, and standardized metrics
are essential for assessing system performance and interconnections
between PV sites. Customizing maintenance plans to site-specific needs
is equally crucial, demanding a shift from fixed to adaptive protocols.
Despite advances in dynamic maintenance, the PV industry tends to
favor short-term gains, neglecting long-term consequences. Addressing
this presents an opportunity for prescriptive maintenance, using RL
techniques to provide actionable insights based on real-time data and


---

Page 18

---

Renewable and Sustainable Energy Reviews 195 (2024) 114342
18
H. Abdulla et al.
predictive models. Finally, this review underscores the need for a
comprehensive approach in PV O&M to enhance the competitiveness
of PV systems in delivering clean energy. Maintenance is vital for sus-
tainable production, aligning with the Sustainable Development Goals
of the United Nations for affordable, reliable, and sustainable energy.
The study provides key insights into effective PV system integration,
emphasizing maintenance strategies for improved reliability, seamless
integration, and grid security.
Some limitations are recognized in the methodology and scope of
this review, such as the reliance on selected search terms and the
focus on publications from the past decade. These constraints may
have affected the results by potentially excluding relevant articles and
overlooking valuable contributions from earlier work. Additionally,
while the PRISMA framework is robust, it might have excluded valuable
articles that did not meet its specific criteria. To overcome these
limitations, future studies are encouraged to use alternative keywords
and employ a broader methodology with a more extensive temporal
scope. In addition, the sustainability impact of maintenance practices,
including waste minimization and resource management, is not ad-
dressed in this work. Striking a balance between profitability and
environmental sustainability is crucial in developing suitable mainte-
nance strategies. Future research should explore sustainable technolo-
gies, conducting a comprehensive life-cycle sustainability assessment
with a focus on eco-friendly materials, energy-efficient procedures, and
responsible maintenance protocols.
CRediT authorship contribution statement
Hind Abdulla: Conceptualization, Methodology, Visualization, Writ-
ing – original draft. Andrei Sleptchenko: Supervision, Conceptualiza-
tion, Validation, Writing – review & editing. Ammar Nayfeh: Concep-
tualization, Writing – review & editing.
Declaration of competing interest
The authors declare that they have no known competing finan-
cial interests or personal relationships that could have appeared to
influence the work reported in this paper.
Data availability
Data will be made available on request.
References
[1] Bouckaert
S,
Pales
AF,
McGlade
C,
Remme
U,
Wanner
B,
Varro
L,
D’Ambrosio D, Spencer T. Net zero by 2050: A roadmap for the global
energy
sector.
Technical
report,
International
Energy
Agency;
2021,
URL
https://iea.blob.core.windows.net/assets/063ae08a-7114-4b58-a34e-
39db2112d0a2/NetZeroby2050-ARoadmapfortheGlobalEnergySector.pdf.
[2] Feldman D, Dummit K, Zuboy J, Margolis R. Spring 2023 solar industry update.
Technical report, Golden, CO (United States): National Renewable Energy Lab.
(NREL); 2023, URL https://www.nrel.gov/docs/fy23osti/86215.pdf.
[3] Bosman LB, Leon-Salas WD, Hutzel W, Soto EA. PV system predictive mainte-
nance: Challenges, current approaches, and opportunities. Energies 2020;16(3).
http://dx.doi.org/10.3390/en13061398.
[4] Walker A. Best practices for operation and maintenance of photovoltaic and
energy storage systems. Technical report NREL/TP-7A40-73822, Golden, CO
(United States): National Renewable Energy Lab. (NREL); 2018, URL https:
//www.nrel.gov/docs/fy19osti/73822.pdf.
[5] Livera A, Theristis M, Micheli L, Fernandez EF, Stein JS, Georghiou GE. Oper-
ation and maintenance decision support system for photovoltaic systems. IEEE
Access 2022;10:42481–96. http://dx.doi.org/10.1109/ACCESS.2022.3168140.
[6] Rediske G, Michels L, Cezar Mairesse Siluk J, Donaduzzi Rigo P, Brum Rosa C,
Jochann Franceschi Bortolini R. Management of operation and maintenance
practices in photovoltaic plants: Key performance indicators. Int J Energy Res
2022;46(6):7118–36. http://dx.doi.org/10.1002/er.7737.
[7] Shafiee M, Sørensen JD. Maintenance optimization and inspection planning
of wind energy assets: Models, methods and strategies. Reliab Eng Syst Saf
2019;192:105993. http://dx.doi.org/10.1016/j.ress.2017.10.025.
[8] Ren Z, Verma AS, Li Y, Teuwen JJ, Jiang Z. Offshore wind turbine opera-
tions and maintenance: A state-of-the-art review. Renew Sustain Energy Rev
2021;144(March). http://dx.doi.org/10.1016/j.rser.2021.110886.
[9] Tusar MIH, Sarker BR. Maintenance cost minimization models for offshore wind
farms: A systematic and critical review. Int J Energy Res 2022;46(4):3739–65.
http://dx.doi.org/10.1002/er.7425.
[10] Navid Q, Hassan A, Fardoun AA, Ramzan R, Alraeesi A. Fault diagnostic
methodologies for utility-scale photovoltaic power plants: A state of the
art review. Sustainability (Switzerland) 2021;13(4):1–22. http://dx.doi.org/10.
3390/su13041629.
[11] Høiaas I, Grujic K, Imenes AG, Burud I, Olsen E, Belbachir N. Inspection
and condition monitoring of large-scale photovoltaic power plants: A review
of imaging technologies. Renew Sustain Energy Rev 2022;161(March):112353.
http://dx.doi.org/10.1016/j.rser.2022.112353.
[12] Jaen-Cuellar AY, Elvira-Ortiz DA, Osornio-Rios RA, Antonino-Daviu JA. Ad-
vances in fault condition monitoring for solar photovoltaic and wind turbine
energy generation: A review. Energies 2022;15(15). http://dx.doi.org/10.3390/
en15155404.
[13] Dhanraj JA, Mostafaeipour A, Velmurugan K, Techato K, Chaurasiya PK,
Solomon JM, Gopalan A, Phoungthong K. An effective evaluation on fault
detection in solar panels. Energies 2021;14(22):1–14. http://dx.doi.org/10.
3390/en14227770.
[14] Protection P. A review of the mitigating methods against the energy con-
version decrease in solar panels. Energies 2022. http://dx.doi.org/10.3390/
en15186558.
[15] Alimi OA, Meyer EL, Olayiwola OI. Solar photovoltaic modules’ performance
reliability and degradation analysis—A review. Energies 2022;15(16). http:
//dx.doi.org/10.3390/en15165964.
[16] Kim J, Rabelo M, Padi SP, Yousuf H, Cho EC, Yi J. A review of the degradation
of photovoltaic modules for life expectancy. Energies 2021;14(14):1–21. http:
//dx.doi.org/10.3390/en14144278.
[17] Aghaei M, Fairbrother A, Gok A, Ahmad S, Kazim S, Lobato K, Oreski G,
Reinders A, Schmitz J, Theelen M, et al. Review of degradation and failure
phenomena in photovoltaic modules. Renew Sustain Energy Rev 2022;159(July
2021):112160. http://dx.doi.org/10.1016/j.rser.2022.112160.
[18] Koester L, Lindig S, Louwen A, Astigarraga A, Manzolini G, Moser D. Review
of photovoltaic module degradation, field inspection techniques and techno-
economic assessment. Renew Sustain Energy Rev 2022;165(May):112616. http:
//dx.doi.org/10.1016/j.rser.2022.112616.
[19] Peinado Gonzalo A, Pliego Marugán A, García Márquez FP. Survey of mainte-
nance management for photovoltaic power systems. Renew Sustain Energy Rev
2020;134(July). http://dx.doi.org/10.1016/j.rser.2020.110347.
[20] Hernández-Callejo
L,
Gallardo-Saavedra
S,
Alonso-Gómez
V.
A
review
of photovoltaic systems: Design, operation and maintenance. Sol Energy
2019;188(March):426–40. http://dx.doi.org/10.1016/j.solener.2019.06.017.
[21] Rahman MM, Khan I, Alameh K. Potential measurement techniques for pho-
tovoltaic module failure diagnosis: A review. Renew Sustain Energy Rev
2021;151:111532. http://dx.doi.org/10.1016/j.rser.2021.111532.
[22] Pillai DS, Shabunko V, Krishna A. A comprehensive review on building
integrated photovoltaic systems: Emphasis to technological advancements,
outdoor testing, and predictive maintenance. Renew Sustain Energy Rev
2022;156:111946. http://dx.doi.org/10.1016/j.rser.2021.111946.
[23] Olorunfemi BO, Ogbolumani OA, Nwulu N. Solar panels dirt monitoring and
cleaning for performance improvement: A systematic review on smart systems.
Sustainability 2022;14(17):10920. http://dx.doi.org/10.3390/su141710920.
[24] Jamil WJ, Abdul Rahman H, Shaari S, Salam Z. Performance degradation of
photovoltaic power system: Review on mitigation methods. Renew Sustain
Energy Rev 2017;67:876–91. http://dx.doi.org/10.1016/j.rser.2016.09.072.
[25] Kazem HA, Chaichan MT, Al-Waeli AH, Sopian K. A review of dust accu-
mulation and cleaning methods for solar photovoltaic systems. J Clean Prod
2020;276:123187. http://dx.doi.org/10.1016/j.jclepro.2020.123187.
[26] Conceicao R, Gonzalez-Aguilar J, Merrouni AA, Romero M. Soiling effect
in solar energy conversion systems: A review. Renew Sustain Energy Rev
2022;162:112434. http://dx.doi.org/10.1016/j.rser.2022.112434.
[27] Osmani K, Haddad A, Lemenand T, Castanier B, Ramadan M. A review on
maintenance strategies for PV systems. Sci Total Environ 2020;746:141753.
http://dx.doi.org/10.1016/j.scitotenv.2020.141753.
[28] Keisang K, Bader T, Samikannu R. Review of operation and maintenance
methodologies for solar photovoltaic microgrids. Front Energy Res 2021. http:
//dx.doi.org/10.3389/fenrg.2021.730230.
[29] Abubakar A, Almeida CFM, Gemignani M. A review of solar photovoltaic system
maintenance strategies. In: 2021 14th IEEE international conference on industry
applications. INDUSCON, IEEE; 2021, p. 1400–7. http://dx.doi.org/10.1109/
INDUSCON51756.2021.9529669.
[30] Ramirez-Vergara J, Bosman LB, Wollega E, Leon-Salas WD. Review of forecast-
ing methods to support photovoltaic predictive maintenance. Clean Eng Technol
2022;8(March):100460. http://dx.doi.org/10.1016/j.clet.2022.100460.
[31] Bermejo JF, Fernández JFG, Pino R, Márquez AC, López AJG. Review and
comparison of intelligent optimization modelling techniques for energy fore-
casting and condition-based maintenance in PV plants. Energies 2019;12(21).
http://dx.doi.org/10.3390/en12214163.


---

Page 19

---

Renewable and Sustainable Energy Reviews 195 (2024) 114342
19
H. Abdulla et al.
[32] Ahmed R, Sreeram V, Mishra Y, Arif M. A review and evaluation of the state-
of-the-art in PV solar power forecasting: Techniques and optimization. Renew
Sustain Energy Rev 2020;124:109792. http://dx.doi.org/10.1016/j.rser.2020.
109792.
[33] Chen Q, Wang Y, Zhang J, Wang Z. The knowledge mapping of concentrating
solar power development based on literature analysis technology. Energies
2020;13(8):1988. http://dx.doi.org/10.3390/en13081988.
[34] Calderón A, Barreneche C, Prieto C, Segarra M, Fernández AI. Concentrating
solar power technologies: a bibliometric study of past, present and future
trends in concentrating solar power research. Front Mech Eng 2021;7:682592.
http://dx.doi.org/10.3389/fmech.2021.682592.
[35] Azad A, Parvin S. Bibliometric analysis of photovoltaic thermal (PV/T) system:
From citation mapping to research agenda. Energy Rep 2022;8:2699–711.
http://dx.doi.org/10.1016/j.egyr.2022.01.182.
[36] Saikia K, Vallès M, Fabregat A, Saez R, Boer D. A bibliometric analysis of trends
in solar cooling technology. Sol Energy 2020;199:100–14. http://dx.doi.org/10.
1016/j.solener.2020.02.013.
[37] Shen Y, Ji L, Xie Y, Huang G, Li X, Huang L. Research landscape and
hot topics of rooftop PV: A bibliometric and network analysis. Energy Build
2021;251:111333. http://dx.doi.org/10.1016/j.enbuild.2021.111333.
[38] Elomari Y, Norouzi M, Marín-Genescà M, Fernández A, Boer D. Integration of
solar photovoltaic systems into power networks: A scientific evolution analysis.
Sustainability 2022;14(15):9249. http://dx.doi.org/10.3390/su14159249.
[39] Zwane N, Tazvinga H, Botai C, Murambadoro M, Botai J, de Wit J, Mabasa B,
Daniel S, Mabhaudhi T. A bibliometric analysis of solar energy forecast-
ing studies in Africa. Energies 2022;15(15):5520. http://dx.doi.org/10.3390/
en15155520.
[40] Madsuha AF, Setiawan EA, Wibowo N, Habiburrahman M, Nurcahyo R,
Sumaedi S. Mapping 30 years of sustainability of solar energy research in
developing countries: Indonesia case. Sustainability 2021;13(20):11415. http:
//dx.doi.org/10.3390/su132011415.
[41] David TM, Rizol PMSR, Machado MAG, Buccieri GP. Future research tendencies
for solar energy management using a bibliometric analysis, 2000–2019. Heliyon
2020;6(7). http://dx.doi.org/10.1016/j.heliyon.2020.e04452.
[42] Márquez FPG. Maintenance management in solar energy systems. Energies
2022;15(10):10–2. http://dx.doi.org/10.3390/en15103727.
[43] Aria M, Cuccurullo C. Bibliometrix: An R-tool for comprehensive science
mapping analysis. J Informetr 2017. http://dx.doi.org/10.1016/j.joi.2017.08.
007.
[44] R Core Team. R: A language and environment for statistical computing. Vienna,
Austria: R Foundation for Statistical Computing; 2021, URL https://www.R-
project.org/.
[45] Van Eck N, Waltman L. Software survey: VOSviewer, a computer program for
bibliometric mapping. Scientometrics 2010;84(2):523–38. http://dx.doi.org/10.
1007/s11192-009-0146-3.
[46] Page MJ, McKenzie JE, Bossuyt PM, Boutron I, Hoffmann TC, Mulrow CD,
Shamseer L, Tetzlaff JM, Akl EA, Brennan SE, et al. The PRISMA 2020
statement: an updated guideline for reporting systematic reviews. Int J Surg
2021;88:105906. http://dx.doi.org/10.1136/bmj.n71.
[47] Cosh K, Ramingwong S, Ramingwong L. A bibliometric analysis of library
review trends. In: Global knowledge, memory and communication. Emerald
Publishing Limited; 2022, http://dx.doi.org/10.1108/GKMC-06-2022-0149.
[48] Leefmann J, Levallois C, Hildt E. Neuroethics 1995–2012. a bibliometric
analysis of the guiding themes of an emerging research field. Front Hum
Neurosci 2016;10:336. http://dx.doi.org/10.3389/fnhum.2016.00336.
[49] Sharadga H, Hajimirza S, Balog RS. Time series forecasting of solar power gen-
eration for large-scale photovoltaic plants. Renew Energy 2020;150:797–807.
http://dx.doi.org/10.1016/j.renene.2019.12.131.
[50] Mellit A, Massi Pavan A, Lughi V. Short-term forecasting of power production
in a large-scale photovoltaic plant. Sol Energy 2014;105:401–13. http://dx.doi.
org/10.1016/j.solener.2014.03.018.
[51] Li X, Yang Q, Lou Z, Yan W. Deep learning based module defect analysis for
large-scale photovoltaic farms. IEEE Trans Energy Convers 2019;34(1):520–9.
http://dx.doi.org/10.1109/TEC.2018.2873358.
[52] De Benedetti M, Leonardi F, Messina F, Santoro C, Vasilakos A. Anomaly
detection and predictive maintenance for photovoltaic systems. Neurocomputing
2018;310:59–68. http://dx.doi.org/10.1016/j.neucom.2018.05.017.
[53] Li X, Li W, Yang Q, Yan W, Zomaya AY. An unmanned inspection sys-
tem for multiple defects detection in photovoltaic plants. IEEE J Photovolt
2020;10(2):568–76. http://dx.doi.org/10.1109/JPHOTOV.2019.2955183.
[54] Huuhtanen T, Jung A. Predictive maintenance of photovoltaic panels via deep
learning. In: 2018 IEEE data science workshop. DSW, IEEE; 2018, p. 66–70.
http://dx.doi.org/10.1109/DSW.2018.8439898.
[55] Zhao Y, Liu Q, Li D, Kang D, Lv Q, Shang L. Hierarchical anomaly detection and
multimodal classification in large-scale photovoltaic systems. IEEE Trans Sustain
Energy 2019;10(3):1351–61. http://dx.doi.org/10.1109/TSTE.2018.2867009.
[56] Peters L, Madlener R. Economic evaluation of maintenance strategies for
ground-mounted solar photovoltaic plants. Appl Energy 2017;199:264–80. http:
//dx.doi.org/10.1016/j.apenergy.2017.04.060.
[57] Aboagye B, Gyamfi S, Ofosu EA, Djordjevic S. Investigation into the impacts
of design, installation, operation and maintenance issues on performance and
degradation of installed solar photovoltaic (PV) systems. Energy Sustain Dev
2022;66:165–76. http://dx.doi.org/10.1016/j.esd.2021.12.003.
[58] Fernández A, Usamentiaga R, de Arquer P, Fernández MÁ, Fernández D,
Carús JL, Fernández M. Robust detection, classification and localization of
defects in large photovoltaic plants based on unmanned aerial vehicles and
infrared thermography. Appl Sci 2020;10(17):5948. http://dx.doi.org/10.3390/
app10175948.
[59] Shiva Kumar B, Sudhakar K. Performance evaluation of 10 MW grid connected
solar photovoltaic power plant in India. Energy Rep 2015;1:184–92. http:
//dx.doi.org/10.1016/j.egyr.2015.10.001.
[60] Elhadj Sidi CEB, Ndiaye ML, El Bah M, Mbodji A, Ndiaye A, Ndiaye PA.
Performance analysis of the first large-scale (15 MWp) grid-connected photo-
voltaic plant in Mauritania. Energy Convers Manage 2016;119:411–21. http:
//dx.doi.org/10.1016/j.enconman.2016.04.070.
[61] Harder E, Gibson JMD. The costs and benefits of large-scale solar photo-
voltaic power production in Abu Dhabi, United Arab Emirates. Renew Energy
2011;36(2):789–96. http://dx.doi.org/10.1016/j.renene.2010.08.006.
[62] Martín-Martínez S, Cañas-Carretón M, Honrubia-Escribano A, Gómez-Lázaro E.
Performance evaluation of large solar photovoltaic power plants in Spain.
Energy Convers Manage 2019;183(December 2018):515–28. http://dx.doi.org/
10.1016/j.enconman.2018.12.116.
[63] Malvoni M, Manoj N, Chopra SS, Hatziargyriou N. Performance and degradation
assessment of large-scale grid-connected solar photovoltaic power plant in
tropical semi-arid environment of India. Sol Energy 2020;203(April):101–13.
http://dx.doi.org/10.1016/j.solener.2020.04.011.
[64] Mensah LD, Yamoah JO, Adaramola MS. Performance evaluation of a utility-
scale grid-tied solar photovoltaic (PV) installation in Ghana. Energy Sustain Dev
2019;48:82–7. http://dx.doi.org/10.1016/j.esd.2018.11.003.
[65] Thotakura S, Kondamudi SC, Xavier JF, Quanjin M, Reddy GR, Gangwar P,
Davuluri SL. Operational performance of megawatt-scale grid integrated rooftop
solar PV system in tropical wet and dry climates of India. Case Stud Therm
Eng 2020;18(November 2019):100602. http://dx.doi.org/10.1016/j.csite.2020.
100602.
[66] Dahmoun MEH, Bekkouche B, Sudhakar K, Guezgouz M, Chenafi A, Chaouch A.
Performance evaluation and analysis of grid-tied large scale PV plant in Algeria.
Energy Sustain Dev 2021;61:181–95. http://dx.doi.org/10.1016/j.esd.2021.02.
004.
[67] AL-Rasheedi M, Gueymard CA, Al-Khayat M, Ismail A, Lee JA, Al-Duaj H.
Performance evaluation of a utility-scale dual-technology photovoltaic power
plant at the Shagaya renewable energy park in Kuwait. Renew Sustain Energy
Rev 2020;133(July):110139. http://dx.doi.org/10.1016/j.rser.2020.110139.
[68] Muñoz-Cerón E, Lomas J, Aguilera J, De la Casa J. Influence of operation and
maintenance expenditures in the feasibility of photovoltaic projects: The case of
a tracking PV plant in Spain. Energy Policy 2018;121(December 2017):506–18.
http://dx.doi.org/10.1016/j.enpol.2018.07.014.
[69] Zhang P, Wang Y, Xiao W, Li W. Reliability evaluation of grid-connected
photovoltaic power systems. IEEE Trans Sustain Energy 2012;3(3):379–89.
http://dx.doi.org/10.1109/TSTE.2012.2186644.
[70] Ahadi A, Ghadimi N, Mirabbasi D. Reliability assessment for components of
large scale photovoltaic systems. J Power Sources 2014;264:211–9. http://dx.
doi.org/10.1016/j.jpowsour.2014.04.041.
[71] Colli A. Failure mode and effect analysis for photovoltaic systems. Renew
Sustain Energy Rev 2015;50:804–9. http://dx.doi.org/10.1016/j.rser.2015.05.
056.
[72] Zini G, Mangeant C, Merten J. Reliability of large-scale grid-connected photo-
voltaic systems. Renew Energy 2011;36(9):2334–40. http://dx.doi.org/10.1016/
j.renene.2011.01.036.
[73] Sayed A, El-Shimy M, El-Metwally M, Elshahed M. Reliability, availability and
maintainability analysis for grid-connected solar photovoltaic systems. Energies
2019;12(7). http://dx.doi.org/10.3390/en12071213.
[74] Dhople SV, Domínguez-García AD. Estimation of photovoltaic system reliability
and performance metrics. IEEE Trans Power Syst 2012;27(1):554–63. http:
//dx.doi.org/10.1109/TPWRS.2011.2165088.
[75] Moradi-Shahrbabak Z, Tabesh A, Yousefi GR. Economical design of utility-scale
photovoltaic power plants with optimum availability. IEEE Trans Ind Electron
2014;61(7):3399–406. http://dx.doi.org/10.1109/TIE.2013.2278525.
[76] Theristis M, Papazoglou IA. Markovian reliability analysis of standalone pho-
tovoltaic systems incorporating repairs. IEEE J Photovolt 2014;4(1):414–22.
http://dx.doi.org/10.1109/JPHOTOV.2013.2284852.
[77] Shrestha SM, Mallineni JK, Yedidi KR, Knisely B, Tatapudi S, Kuitche J,
Tamizhmani G. Determination of dominant failure modes using FMECA on the
field deployed c-Si modules under hot-dry desert climate. IEEE J Photovolt
2015;5(1):174–82. http://dx.doi.org/10.1109/JPHOTOV.2014.2366872.
[78] Baschel S, Koubli E, Roy J, Gottschalg R. Impact of component reliability
on large scale photovoltaic systems’ performance. Energies 2018;11(6). http:
//dx.doi.org/10.3390/en11061579.
[79] Massi Pavan A, Mellit A, De Pieri D. The effect of soiling on energy production
for large-scale photovoltaic plants. Sol Energy 2011;85(5):1128–36. http://dx.
doi.org/10.1016/j.solener.2011.03.006.


---

Page 20

---

Renewable and Sustainable Energy Reviews 195 (2024) 114342
20
H. Abdulla et al.
[80] Jones RK, Baras A, Saeeri AA, Al Qahtani A, Al Amoudi AO, Al Shaya Y,
Alodan M, Al-Hsaien SA. Optimized cleaning cost and schedule based on
observed soiling conditions for photovoltaic plants in central Saudi Arabia.
IEEE J Photovolt 2016;6(3):730–8. http://dx.doi.org/10.1109/JPHOTOV.2016.
2535308.
[81] Hammad B, Al-Abed M, Al-Ghandoor A, Al-Sardeah A, Al-Bashir A. Modeling
and analysis of dust and temperature effects on photovoltaic systems’ per-
formance and optimal cleaning frequency: Jordan case study. Renew Sustain
Energy Rev 2018;82(April):2218–34. http://dx.doi.org/10.1016/j.rser.2017.08.
070.
[82] Al-Housani M, Bicer Y, Koç M. Experimental investigations on PV cleaning
of large-scale solar power plants in desert climates: Comparison of cleaning
techniques for drone retrofitting. Energy Convers Manage 2019;185:800–15.
http://dx.doi.org/10.1016/j.enconman.2019.01.058.
[83] Ullah A, Amin A, Haider T, Saleem M, Butt NZ. Investigation of soiling effects,
dust chemistry and optimum cleaning schedule for PV modules in Lahore,
Pakistan. Renew Energy 2020;150:456–68. http://dx.doi.org/10.1016/j.renene.
2019.12.090.
[84] Villarini M, Cesarotti V, Alfonsi L, Introna V. Optimization of photovoltaic
maintenance plan by means of a FMEA approach based on real data. Energy
Convers Manage 2017;152(May):1–12. http://dx.doi.org/10.1016/j.enconman.
2017.08.090.
[85] Rodrigo PM, Gutiérrez S, Micheli L, Fernández EF, Almonacid FM. Optimum
cleaning schedule of photovoltaic systems based on levelised cost of energy
and case study in central Mexico. Sol Energy 2020;209(September 2019):11–20.
http://dx.doi.org/10.1016/j.solener.2020.08.074.
[86] Alvarez DL, Al-Sumaiti AS, Rivera SR. Estimation of an optimal PV panel
cleaning strategy based on both annual radiation profile and module degra-
dation. IEEE Access 2020;8:63832–9. http://dx.doi.org/10.1109/ACCESS.2020.
2983322.
[87] Jiménez-Fernández S, Salcedo-Sanz S, Gallo-Marazuela D, Gómez-Prada G,
Maellas J, Portilla-Figueras A. Sizing and maintenance visits optimization
of a hybrid photovoltaic-hydrogen stand-alone facility using evolutionary al-
gorithms. Renew Energy 2014;66:402–13. http://dx.doi.org/10.1016/j.renene.
2013.12.028.
[88] Mahani K, Liang Z, Parlikad AK, Jafari MA. Joint optimization of operation and
maintenance policies for solar-powered microgrids. IEEE Trans Sustain Energy
2018;10(2):833–42. http://dx.doi.org/10.1109/TSTE.2018.2849318.
[89] Talayero AP, Melero JJ, Llombart A, Casado A. Operation and mainte-
nance in solar plants: Eight study cases. Renew Energy Power Qual J
2018;1(16):499–504. http://dx.doi.org/10.24084/repqj16.363.
[90] Lee J, Ni J, Singh J, Jiang B, Azamfar M, Feng J. Intelligent mainte-
nance systems and predictive manufacturing.
Trans ASME, J Manuf Sci Eng
2020;142(11). http://dx.doi.org/10.1115/1.4047856.
[91] Baklouti A, Mifdal L, Dellagi S, Chelbi A. An optimal preventive maintenance
policy for a solar photovoltaic system. Sustainability (Switzerland) 2020;12(10).
http://dx.doi.org/10.3390/su12104266.
[92] Deli K, Tchoffo Houdji E, Djongyang N, Njomo D. Operation and maintenance of
back-up photovoltaic systems: An analysis based on a field study in Cameroon.
Afr J Sci Technol Innov Dev 2017;9(4):437–48. http://dx.doi.org/10.1080/
20421338.2017.1341731.
[93] Felipe TA, Melo FC, Freitas LC. Design and development of an online
smart monitoring and diagnosis system for photovoltaic distributed generation.
Energies 2021;14(24). http://dx.doi.org/10.3390/en14248552.
[94] Aghaei M, Kirsten A, Oliveira VD, Matheus K, Rüther R. Automatic fault
detection of utility-scale photovoltaic solar generators applying aerial in-
frared thermography and orthomosaicking. Sol Energy 2023;252(November
2022):272–83. http://dx.doi.org/10.1016/j.solener.2023.01.058.
[95] Pierdicca R, Paolanti M, Felicetti A, Piccinini F, Zingaretti P. Automatic
faults detection of photovoltaic farms: Solair, a deep learning-based system
for thermal images. Energies 2020;13(24):1–17. http://dx.doi.org/10.3390/
en13246496.
[96] Saad M, Amir Y, Niazi K, Amir U, Lee B-w. Real-time fault detection system
for large scale grid integrated solar photovoltaic power plants. Int J Electr
Power Energy Syst 2021;130(August 2020):106902. http://dx.doi.org/10.1016/
j.ijepes.2021.106902.
[97] Liu Q, Zhao Y, Zhang Y, Kang D, Lv Q, Shang L. Hierarchical context-aware
anomaly diagnosis in large-scale PV systems using SCADA data. In: 2017 IEEE
15th international conference on industrial informatics. INDIN, IEEE; 2017, p.
1025–30. http://dx.doi.org/10.1109/INDIN.2017.8104914.
[98] Hoarcă IC. Energy management for a photovoltaic power plant based on SCADA
system. In: 2021 13th international conference on electronics, computers and
artificial intelligence. ECAI, IEEE; 2021, p. 1–9. http://dx.doi.org/10.1109/
ECAI52376.2021.9515136.
[99] Ventura C, Tina GM. Development of models for on-line diagnostic and energy
assessment analysis of PV power plants: The study case of 1 MW sicilian
PV plant. Energy Procedia 2015;83:248–57. http://dx.doi.org/10.1016/j.egypro.
2015.12.179.
[100] Gradwohl C, Dimitrievska V, Pittino F, Muehleisen W, Montvay A, Langmayr F,
Kienberger T. A combined approach for model-based PV power plant fail-
ure detection and diagnostic. Energies 2021;14(5). http://dx.doi.org/10.3390/
en14051261.
[101] Niccolai A, Grimaccia F, Leva S. Advanced asset management tools in pho-
tovoltaic plant monitoring: UAV-based digital mapping. Energies 2019;12(24).
http://dx.doi.org/10.3390/en12244736.
[102] Kirsten Vidal de Oliveira A, Aghaei M, Rüther R. Aerial infrared thermography
for low-cost and fast fault detection in utility-scale PV power plants. Sol Energy
2020;211(July):712–24. http://dx.doi.org/10.1016/j.solener.2020.09.066.
[103] Kuo C-FJ, Chen S-H, Huang C-Y. Automatic detection, classification and
localization of defects in large photovoltaic plants using unmanned aerial
vehicles (UAV) based infrared (IR) and RGB imaging. Energy Convers Manage
2023;276:116495. http://dx.doi.org/10.1016/j.enconman.2022.116495.
[104] Segovia Ramirez I, Garcia Marquez FP. Fault detection and identification
for maintenance management. In: Proceedings of the fourteenth international
conference on management science and engineering management: volume 1.
Springer; 2020, p. 460–9. http://dx.doi.org/10.1007/978-3-030-49829-0_34.
[105] Grimaccia F, Aghaei M, Mussetta M, Leva S, Quater PB. Planning for PV plant
performance monitoring by means of unmanned aerial systems (UAS). Int J
Energy Environ Eng 2015;6(1):47–54. http://dx.doi.org/10.1007/s40095-014-
0149-6.
[106] Shapsough S, Takrouri M, Dhaouadi R, Zualkernan IA. Using IoT and smart
monitoring devices to optimize the efficiency of large-scale distributed so-
lar farms. Wirel Netw 2021;27(6):4313–29. http://dx.doi.org/10.1007/s11276-
018-01918-z.
[107] Del Río AM, Ramírez IS, Márquez FPG. Photovoltaic solar power plant mainte-
nance management based on IoT and machine learning. In: 2021 international
conference on innovation and intelligence for informatics, computing, and tech-
nologies. 3ICT, IEEE; 2021, p. 423–8. http://dx.doi.org/10.1109/3ICT53449.
2021.9581504.
[108] Kusznier J, Wojtkowski W. IoT solutions for maintenance and evaluation
of photovoltaic systems. Energies 2021;14(24). http://dx.doi.org/10.3390/
en14248567.
[109] Ramírez IS, Del Río AM, Márquez FPG. IoT platform combined with machine
learning techniques for fault detection and diagnosis of large photovoltaic
plants. In: 2022 3rd international conference on computing, analytics and
networks. ICAN, IEEE; 2022, p. 1–6. http://dx.doi.org/10.1109/ICAN56228.
2022.10007163.
[110] Chebel-Morello B, Medjaher K, Hadj Arab A, Bandou F, Bouchaib S, Zerhouni N.
E-maintenance for photovoltaic power generation system. Energy Procedia
2012;18:640–3. http://dx.doi.org/10.1016/j.egypro.2012.05.077.
[111] Kothona D, Panapakidis IP, Christoforidis GC. Prescriptive maintenance tech-
nique for photovoltaic systems. In: 2022 IEEE international conference on
environment and electrical engineering and 2022 IEEE industrial and com-
mercial power systems Europe. EEEIC/I&CPS Europe, IEEE; 2022, p. 1–5.
http://dx.doi.org/10.1109/EEEIC/ICPSEurope54979.2022.9854790.
[112] Livera A, Tziolis G, Franquelo JG, Bernal RG, Georghiou GE. Cloud-based plat-
form for photovoltaic assets diagnosis and maintenance. Energies 2022;103–13.
http://dx.doi.org/10.3390/en15207760.
[113] Livera A, Theristis M, Charalambous A, Stein JS, Georghiou GE. Decision
support system for corrective maintenance in large-scale photovoltaic systems.
In: 2021 IEEE 48th photovoltaic specialists conference. PVSC, IEEE; 2021, p.
0306–11. http://dx.doi.org/10.1109/PVSC43889.2021.9518796.
[114] Alam M, Haque A, Khan MA, Sobahi NM, Mehedi IM, Khan AI. Condition
monitoring and maintenance management with grid-connected renewable en-
ergy systems. Comput Mater Contin 2022;72(2):3999–4017. http://dx.doi.org/
10.32604/cmc.2022.026353.
[115] Starzyński J, Zawadzki P, Harańczyk D. Machine learning in solar plants
inspection automation. Energies 2022;15(16):5966. http://dx.doi.org/10.3390/
en15165966.
[116] Hopwood MW, Patel L, Gunda T. Classification of photovoltaic failures
with hidden Markov modeling, an unsupervised statistical approach. Energies
2022;15(14):1–12. http://dx.doi.org/10.3390/en15145104.
[117] Seo G, Yoon S, Song J, Srivastava E, Hwang E. Label-free fault detection
scheme for inverters of PV systems: Deep reinforcement learning-based dynamic
threshold. Appl Sci 2023;13(4):2470. http://dx.doi.org/10.3390/app13042470.
[118] Klinsuwan T, Ratiphaphongthon W, Wangkeeree R, Wangkeeree R, Sirisam-
phanwong
C.
Evaluation
of
machine
learning
algorithms
for
supervised
anomaly detection and comparison between static and dynamic thresholds
in photovoltaic systems. Energies 2023;16(4):1947. http://dx.doi.org/10.3390/
en16041947.
[119] Rukijkanpanich J, Mingmongkol M. Enhancing performance of maintenance in
solar power plant. J Qual Maint Eng 2020;26(4):575–91. http://dx.doi.org/10.
1108/JQME-11-2018-0098.
[120] Selcuk
S.
Predictive
maintenance,
its
implementation
and
latest
trends.
Proc
Inst
Mech
Eng
B
2017;231(9):1670–9.
http://dx.doi.org/10.1177/
0954405415601640.
[121] Liu Q, Hu Q, Zhou J, Yu D, Mo H. Remaining useful life prediction of
PV systems under dynamic environmental conditions. IEEE J Photovolt 2023.
http://dx.doi.org/10.1109/JPHOTOV.2023.3272071.


---

Page 21

---

Renewable and Sustainable Energy Reviews 195 (2024) 114342
21
H. Abdulla et al.
[122] Betti A, Tucci M, Crisostomi E, Piazzi A, Barmada S, Thomopulos D. Fault
prediction and early-detection in large PV power plants based on self-organizing
maps. Sensors 2021;21(5):1–16. http://dx.doi.org/10.3390/s21051687.
[123] Sepúlveda Oviedo EH, Travé-Massuyès L, Subias A, Alonso C, Pavlov M.
Feature extraction and health status prediction in PV systems. Adv Eng Inform
2022;53(July):101696. http://dx.doi.org/10.1016/j.aei.2022.101696.
[124] Li Z, Mahbobur Rahman S, Vega R, Dong B. A hierarchical approach using
machine learning methods in solar photovoltaic energy production forecasting.
Energies 2016;9(1). http://dx.doi.org/10.3390/en9010055.
[125] Sa’ad A, Zied H, Nyoungue A. A day-ahead multi-approach machine learning
technique for photovoltaic power forecasting. In: 2020 9th international con-
ference on renewable energy research and application. ICRERA, IEEE; 2020, p.
257–62. http://dx.doi.org/10.1109/ICRERA49962.2020.9242897.
[126] Du Plessis A, Strauss J, Rix A. Short-term solar power forecasting: Investigating
the ability of deep learning models to capture low-level utility-scale photo-
voltaic system behaviour. Appl Energy 2021;285:116395. http://dx.doi.org/10.
1016/j.apenergy.2020.116395.
[127] Gao M, Li J, Hong F, Long D. Day-ahead power forecasting in a large-
scale photovoltaic plant based on weather classification using LSTM. Energy
2019;187:115838. http://dx.doi.org/10.1016/j.energy.2019.07.168.
[128] Olivencia Polo FA, Ferrero Bermejo J, Gómez Fernández JF, Crespo Márquez A.
Failure mode prediction and energy forecasting of PV plants to assist dynamic
maintenance tasks by ANN based models. Renew Energy 2015;81:227–38.
http://dx.doi.org/10.1016/j.renene.2015.03.023.
[129] Dimitropoulos N, Sofias N, Kapsalis P, Mylona Z, Marinakis V, Primo N,
Doukas H. Forecasting of short-term PV production in energy communities
through machine learning and deep learning algorithms. In: 2021 12th inter-
national conference on information, intelligence, systems & applications. IISA,
IEEE; 2021, p. 1–6. http://dx.doi.org/10.1109/IISA52424.2021.9555544.
[130] Jackson ND, Gunda T. Evaluation of extreme weather impacts on utility-
scale photovoltaic plant performance in the United States. Appl Energy
2021;302(April):117508. http://dx.doi.org/10.1016/j.apenergy.2021.117508.
[131] Micheli L, Fernández EF, Muller M, Almonacid F. Extracting and generating
PV soiling profiles for analysis, forecasting, and cleaning optimization. IEEE
J Photovolt 2020;10(1):197–205. http://dx.doi.org/10.1109/JPHOTOV.2019.
2943706.
[132] Micheli L, Fernández EF, Almonacid F. Photovoltaic cleaning optimization
through the analysis of historical time series of environmental parameters. Sol
Energy 2021;227(December 2020):645–54. http://dx.doi.org/10.1016/j.solener.
2021.08.081.
[133] Benabbou L, Malki Z, Sankaran K, Bouzekri H. Machine learning-based pre-
dictive maintenance for renewable energy : The case of power plants in
Morocco. In: Proceedings of the 36th international conference on machine learn-
ing. 2019, p. 5–7, URL https://s3.us-east-1.amazonaws.com/climate-change-
ai/papers/icml2019/35/paper.pdf.
[134] Livera A, Theristis M, Micheli L, Stein JS, Georghiou GE. Failure diagnosis
and trend-based performance losses routines for the detection and classification
of incidents in large-scale photovoltaic systems. Prog Photovolt, Res Appl
2022;30(8):921–37. http://dx.doi.org/10.1002/pip.3578.
[135] Ventura C, Tina GM. Utility scale photovoltaic plant indices and models
for on-line monitoring and fault detection purposes. Electr Power Syst Res
2016;136:43–56. http://dx.doi.org/10.1016/j.epsr.2016.02.006.
[136] Bizzarri F, Brambilla A, Caretta L, Guardiani C. Monitoring performance and
efficiency of photovoltaic parks. Renew Energy 2015;78:314–21. http://dx.doi.
org/10.1016/j.renene.2015.01.002.
[137] Ketjoy N, Thanarak P, Yaowarat P. Case studies on system availability of PVP
plants in Thailand. Energy Rep 2022;8:514–26. http://dx.doi.org/10.1016/j.
egyr.2021.11.266.
[138] Iftikhar H, Sarquis E, Costa Branco PJ. Why can simple operation and
maintenance (O&M) practices in large-scale grid-connected PV power plants
play a key role in improving its energy output? Energies 2021;14(13). http:
//dx.doi.org/10.3390/en14133798.
[139] Fathi M, Abderrezek M, Grana P. Technical and economic assessment of
cleaning protocol for photovoltaic power plants: Case of Algerian Sahara sites.
Sol Energy 2017;147:358–67. http://dx.doi.org/10.1016/j.solener.2017.03.053.
[140] Bolinger M, Gorman W, Millstein D, Jordan D. System-level performance and
degradation of 21 GWDC of utility-scale PV plants in the United States. J Renew
Sustain Energy 2020;12(4). http://dx.doi.org/10.1063/5.0004710.
[141] Jordan DC, Anderson K, Perry K, Muller M, Deceglie M, White R, De-
line C. Photovoltaic fleet degradation insights. Prog Photovolt, Res Appl
2022;30(10):1166–75. http://dx.doi.org/10.1002/pip.3566.
[142] Lindig S, Ascencio-Vasquez J, Leloux J, Moser D, Reinders A. Performance
analysis and degradation of a large fleet of PV systems. IEEE J Photovolt
2021;11(5):1312–8. http://dx.doi.org/10.1109/JPHOTOV.2021.3093049.
[143] Deline C, White R, Muller M, Anderson K, Perry K, Deceglie M, Simpson L,
Jordan D. PV fleet performance data initiative program and methodology.
In: 2020 47th IEEE photovoltaic specialists conference. PVSC, IEEE; 2020, p.
1363–7. http://dx.doi.org/10.1109/PVSC45281.2020.9300583.
[144] Jordan DC, Marion B, Deline C, Barnes T, Bolinger M. PV field reliabil-
ity status—Analysis of 100 000 solar systems. Prog Photovolt, Res Appl
2020;28(8):739–54. http://dx.doi.org/10.1002/pip.3262.
[145] Nobre AM, Agarwal A, Pranav S. Ongoing performance assessment strategies &
operational challenges when managing hundreds of distributed photovoltaic as-
sets across Asia. In: 2022 IEEE 49th photovoltaics specialists conference. PVSC,
IEEE; 2022, p. 0614–9. http://dx.doi.org/10.1109/PVSC48317.2022.9938578.
[146] Nobre AM, Karthik S, Liew WY, Baker R, Malhotra R, Khor A. Performance
evaluation of a fleet of photovoltaic systems across India and southeast Asia.
In: 2019 IEEE 46th photovoltaic specialists conference. PVSC, IEEE; 2019, p.
1372–6. http://dx.doi.org/10.1109/PVSC40753.2019.8981226.
[147] Ascencio-Vásquez J, Osorio-Aravena JC, Brecl K, Muñoz-Cerón E, Topič M. Typ-
ical daily profiles, a novel approach for photovoltaics performance assessment:
Case study on large-scale systems in Chile. Sol Energy 2021;225(July):357–74.
http://dx.doi.org/10.1016/j.solener.2021.07.007.
[148] Micheli L, Fernández EF, Aguilera JT, Almonacid F. Economics of seasonal
photovoltaic soiling and cleaning optimization scenarios. Energy 2021;215.
http://dx.doi.org/10.1016/j.energy.2020.119018.
[149] Redondo M, Platero CA, Moset A, Rodríguez F, Donate V. Soiling mod-
elling in large grid-connected PV plants for cleaning optimization. Energies
2023;16(2):1–13. http://dx.doi.org/10.3390/en16020904.
[150] Micheli L, Theristis M, Talavera DL, Almonacid F, Stein JS, Fernández EF.
Photovoltaic cleaning frequency optimization under different degradation rate
patterns. Renew Energy 2020;166:136–46. http://dx.doi.org/10.1016/j.renene.
2020.11.044.
[151] Yazdani H, Yaghoubi M. Dust deposition effect on photovoltaic modules
performance and optimization of cleaning period: A combined experimental–
numerical study. Sustain Energy Technol Assess 2022;51(June 2021):101946.
http://dx.doi.org/10.1016/j.seta.2021.101946.
[152] Deceglie MG, Anderson K, Fregosi D, Hobbs WB, Mikofski MA, Theristis M,
Meyers BE. Perspective: Performance loss rate in photovoltaic systems. Solar
RRL 2023;7(15):2300196. http://dx.doi.org/10.1002/solr.202300196.
[153] Zuñiga-Cortes F, Garcia-Racines JD, Caicedo-Bravo E, Moncada-Vega H. Mini-
mization of economic losses in photovoltaic system cleaning schedules based
on a novel methodological framework for performance ratio forecast and cost
analysis. Energies 2023;16(16):6091. http://dx.doi.org/10.3390/en16166091.
[154] Shimura S, Herrero R, Zuffo MK, Baesso Grimoni JA. Production costs
estimation
in
photovoltaic
power
plants
using
reliability.
Sol
Energy
2016;133:294–304. http://dx.doi.org/10.1016/j.solener.2016.03.070.
[155] dos Santos Pereira GM, Weigert GR, Morais PS, e Silva KA, Segura-Salas CS,
de Matos Gonçalves AM, do Nascimento HHS. Transport route planning for
operation and maintenance of off-grid photovoltaic energy systems in the
pantanal of mato grosso do sul. In: 2020 IEEE PES transmission & distribution
conference and exhibition-Latin America. (T&D LA), IEEE; 2020, p. 1–6. http:
//dx.doi.org/10.1109/TDLA47668.2020.9326099.
[156] Bolinger M, Wiser R, O’Shaughnessy E. Levelized cost-based learning analysis of
utility-scale wind and solar in the United States. iScience 2022;25(6):104378.
http://dx.doi.org/10.1016/j.isci.2022.104378.
[157] Pereira
GMdS,
Weigert
GR,
Macedo
PL,
Silva
KAe,
Segura
Salas
CS,
Gonçalves AMd, do Nascimento HHS. Quasi-dynamic operation and main-
tenance plan for photovoltaic systems in remote areas: The framework of
Pantanal-MS. Renew Energy 2022;181:404–16. http://dx.doi.org/10.1016/j.
renene.2021.08.119.
[158] Konde AL, Kusaf M, Dagbasi M. An effective design method for grid-connected
solar PV power plants for power supply reliability. Energy Sustain Dev
2022;70:301–13. http://dx.doi.org/10.1016/j.esd.2022.08.006.
[159] Guo L, Wang Y, Kang R, Wang R, Li Y, Yang S. Energy yield optimization
for micro-inverter photovoltaic systems with spare parts inventory. Sustain
Energy Technol Assess 2022;53(PC):102729. http://dx.doi.org/10.1016/j.seta.
2022.102729.
[160] Alhammami H, An H. Techno-economic analysis and policy implications for
promoting residential rooftop solar photovoltaics in Abu Dhabi, UAE. Renew
Energy 2021;167:359–68. http://dx.doi.org/10.1016/j.renene.2020.11.091.
[161] Sewchurran S, Davidson IE. Technical and financial analysis of large-scale solar-
PV in ethekwini municipality: Residential, business and bulk customers. Energy
Rep 2021;7:4961–76. http://dx.doi.org/10.1016/j.egyr.2021.07.134.
[162] Al-Sumaiti
AS,
Kavousi-Fard
A,
Salama
M,
Pourbehzadi
M,
Reddy
S,
Rasheed MB. Economic assessment of distributed generation technologies: A
feasibility study and comparison with the literature. Energies 2020;13(11).
http://dx.doi.org/10.3390/en13112764.
[163] Alashqar M, Xue Y, Yang C, Zhang XP. Comprehensive economic analysis of
PV farm -A case study of Alkarsaah PV farm in Qatar. Front Energy Res
2022;10(September):1–17. http://dx.doi.org/10.3389/fenrg.2022.987773.
[164] Virtuani A, Morganti L. Profitability of solar photovoltaic projects: A sensitivity
analysis of performance loss curves and operation and maintenance expenses.
Solar RRL 2022;2200663:1–9. http://dx.doi.org/10.1002/solr.202200663.
[165] Oprea S-V, Bâra A, Preoţescu D, Elefterescu L. Photovoltaic power plants (PV-
PP) reliability indicators for improving operation and maintenance activities. a
case study of PV-PP Agigea located in Romania. IEEE Access 2019;7:39142–57.
http://dx.doi.org/10.1109/ACCESS.2019.2907098.
[166] Spertino F, Chiodo E, Ciocia A, Malgaroli G, Ratclif A. Maintenance activity,
reliability, availability, and related energy losses in ten operating photovoltaic
systems up to 1.8 MW. IEEE Trans Ind Appl 2021;57(1):83–93. http://dx.doi.
org/10.1109/TIA.2020.3031547.


---

Page 22

---

Renewable and Sustainable Energy Reviews 195 (2024) 114342
22
H. Abdulla et al.
[167] Spertino F, Amato A, Casali G, Ciocia A, Malgaroli G. Reliability analysis
and repair activity for the components of 350 kW inverters in a large scale
grid-connected photovoltaic system. Electronics (Switzerland) 2021;10(5):1–13.
http://dx.doi.org/10.3390/electronics10050564.
[168] Sayed A, EL-Shimy M, El-Metwally M, Elshahed M. Impact of subsystems on
the overall system availability for the large scale grid-connected photovoltaic
systems. Reliab Eng Syst Saf 2020;196:106742. http://dx.doi.org/10.1016/j.
ress.2019.106742.
[169] Vargas JP, Goss B, Gottschalg R. Large scale PV systems under non-uniform
and fault conditions. Sol Energy 2015;116:303–13. http://dx.doi.org/10.1016/
j.solener.2015.03.041.
[170] Gallardo-Saavedra S, Hernández-Callejo L, Duque-Pérez O. Quantitative failure
rates and modes analysis in photovoltaic plants. Energy 2019;183:825–36.
http://dx.doi.org/10.1016/j.energy.2019.06.185.
[171] Maihulla AS, Yusuf I. Performance analysis of photovoltaic systems using
(RAMD) analysis. J Niger Soc Phys Sci 2021;3(3):172–80. http://dx.doi.org/
10.46481/jnsps.2021.194.
[172] Quansah DA, Adaramola MS, Takyi G. Degradation and longevity of solar
photovoltaic modules—An analysis of recent field studies in Ghana. Energy Sci
Eng 2020;8(6):2116–28. http://dx.doi.org/10.1002/ese3.651.
[173] Kudelas D, Taušová M, Tauš P, Gabániová L, Koščo J. Investigation of operating
parameters and degradation of photovoltaic panels in a photovoltaic power
plant. Energies 2019;12(19). http://dx.doi.org/10.3390/en12193631.
[174] Singh R, Sharma M, Yadav K. Degradation and reliability analysis of photo-
voltaic modules after operating for 12 years: A case study with comparisons.
Renew Energy 2022;196:1170–86. http://dx.doi.org/10.1016/j.renene.2022.07.
048.
[175] Bansal N, Jaiswal SP, Singh G. Prolonged degradation and reliability assessment
of installed modules operational for 10 years in 5 MW PV plant in hot semi-arid
climate. Energy Sustain Dev 2022;68:373–89. http://dx.doi.org/10.1016/j.esd.
2022.04.008.
[176] Leccese F, Petritoli E, Cagnetti M, Sangiovanni S, Podestà L, Spagnolo GS. An
analysis for a precise reliability and availability assessment of ‘‘photovoltaic
system’’ pilot site: a case study. In: 2021 IEEE 6th international forum on
research and technology for society and industry. RTSI, IEEE; 2021, p. 1–6.
http://dx.doi.org/10.1109/RTSI50628.2021.9597225.
[177] Adler SW, Wiig MS, Skomedal A, Haug H, Marstein ES. Degradation anal-
ysis of utility-scale PV plants in different climate zones. IEEE J Photovolt
2021;11(2):513–8. http://dx.doi.org/10.1109/JPHOTOV.2020.3043120.
[178] Kaaya I, Lindig S, Weiss KA, Virtuani A, Sidrach de Cardona Ortin M, Moser D.
Photovoltaic lifetime forecast model based on degradation patterns. Prog
Photovolt, Res Appl 2020;28(10):979–92. http://dx.doi.org/10.1002/pip.3280.
[179] Bensebaa F. Solar based large scale power plants: What is the best option? Prog
Photovolt, Res Appl 2011;19(2):240–6. http://dx.doi.org/10.1002/pip.998.
[180] Sa’ad A, Nyoungue AC, Hajej Z. Bi-objective preventive maintenance scheduling
optimization of photovoltaic system based on availability. In: IOP conference
series: earth and environmental science. Vol. 1054, IOP Publishing; 2022,
012041. http://dx.doi.org/10.1088/1755-1315/1054/1/012041.
[181] International Electrotechnical Commission (IEC). Photovoltaic system perfor-
mance monitoring-guidelines for measurement, data exchange and analysis -
part 1: Monitoring. In: International standard international electrotechnical
commission. International Electrotechnical Commission Central Office; 2017,
p. 1–10, URL https://webstore.iec.ch/preview/info_iec61724-1%7Bed2.0.RLV%
7Den.pdf.
[182] Emblemsvåg J. On the levelised cost of energy of solar photovoltaics. Int J
Sustain Energy 2021;40(8):755–80. http://dx.doi.org/10.1080/14786451.2020.
1867139.
[183] Mgonja CT, Saidi H. Effectiveness on implementation of maintenance man-
agement system for off-grid solar PV systems in public facilities - A case
study of ssmp1 project in Tanzania. Int J Mech Eng Technol 2017;8(7):869–
80, URL https://iaeme.com/MasterAdmin/Journal_uploads/IJMET/VOLUME_8_
ISSUE_7/IJMET_08_07_095.pdf.
[184] Klise GT, Hill R, Walker A, Dobos A, Freeman J. PV system ‘‘availability’’ as
a reliability metric—Improving standards, contract language and performance
models. In: 2016 IEEE 43rd photovoltaic specialists conference. PVSC, IEEE;
2016, p. 1719–23. http://dx.doi.org/10.1109/PVSC.2016.7749918.
[185] Qadeer A, Huawei L, Ikram MT. Research on reliability of grid connected
photovoltaic renewable generation system. In: IOP conference series: earth
and environmental science. Vol. 804, IOP Publishing; 2021, 032058. http:
//dx.doi.org/10.1088/1755-1315/804/3/032058.
[186] Elshahed M, Al-Mufadi FA, Sayed A. Temporary faults impact on the overall
availability and reliability of practical large-scale grid-connected photovoltaic
systems. Energy Rep 2023;9:5336–49. http://dx.doi.org/10.1016/j.egyr.2023.
04.353.
[187] Li T, Tao S, Zhang R, Liu Z, Ma L, Sun J, Sun Y. Reliability eval-
uation
of
photovoltaic
system
considering
inverter
thermal
characteris-
tics. Electronics (Switzerland) 2021;10(15):1–15. http://dx.doi.org/10.3390/
electronics10151763.
[188] Spertino F, Chiodo E, Ciocia A, Malgaroli G, Ratclif A. Maintenance activity,
reliability analysis and related energy losses in five operating photovoltaic
plants. In: 2019 IEEE international conference on environment and electrical
engineering and 2019 IEEE industrial and commercial power systems Europe.
EEEIC/I&CPS Europe, IEEE; 2019, p. 1–6. http://dx.doi.org/10.1109/EEEIC.
2019.8783240.
[189] Nageh M, Abdullah MP, Yousef B. Reliability evaluation and cost analysis for
optimized large scale solar PV system. In: 2021 IEEE industrial electronics and
applications conference. IEACon, IEEE; 2021, p. 195–200. http://dx.doi.org/10.
1109/IEACon51066.2021.9654682.
[190] Sonawane PR, Bhandari S, Patil RB, Al-Dahidi S. Reliability and criticality anal-
ysis of a large-scale solar photovoltaic system using fault tree analysis approach.
Sustainability 2023;15(5):4609. http://dx.doi.org/10.3390/su15054609.
[191] Ahadi A, Hayati H, Miryousefi Aval SM. Reliability evaluation of future photo-
voltaic systems with smart operation strategy. Front Energy 2016;10(2):125–35.
http://dx.doi.org/10.1007/s11708-015-0392-4.
[192] Simon DF, Teixeira M, da Costa JP. Availability estimation in photovoltaic
generation systems using timed Petri net simulation models. Int J Electr Power
Energy Syst 2022;137(June 2020):106897. http://dx.doi.org/10.1016/j.ijepes.
2021.106897.
[193] Maihulla AS, Yusuf I, Salihu Isa M. Reliability modeling and performance
evaluation of solar photovoltaic system using Gumbel–Hougaard family copula.
Int J Qual Reliab Manage 2022;39(8):2041–57. http://dx.doi.org/10.1108/
IJQRM-03-2021-0071.
[194] Wang Y, Zhang P, Li W, Kan’An NH. Comparative analysis of the reliability
of grid-connected photovoltaic power systems. IEEE Power Energy Soc Gener
Meet 2012;5:1–8. http://dx.doi.org/10.1109/PESGM.2012.6345373.
[195] Cai B, Liu Y, Ma Y, Huang L, Liu Z. A framework for the reliability evaluation
of grid-connected photovoltaic systems in the presence of intermittent faults.
Energy 2015;93:1308–20. http://dx.doi.org/10.1016/j.energy.2015.10.068.
[196] Khalilnejad A, Member S, Pour MM, Member S, Zarafshan E. Long term
reliability analysis of components of photovoltaic system based on Markov
process. IEEE 2016;1–5. http://dx.doi.org/10.1109/SECON.2016.7506762.
[197] Miao S, Ning G, Gu Y, Yan J, Ma B. Markov chain model for solar farm
generation and its application to generation performance evaluation. J Clean
Prod 2018;186:905–17. http://dx.doi.org/10.1016/j.jclepro.2018.03.173.
[198] Altamimi
A,
Jayaweera
D.
Reliability
of
power
systems
with
climate
change impacts on hierarchical levels of PV systems. Electr Power Syst
Res 2021;190(December 2019):106830. http://dx.doi.org/10.1016/j.epsr.2020.
106830.
[199] Abunima H, Teh J. Reliability modeling of PV systems based on time-varying
failure rates. IEEE Access 2020;8:14367–76. http://dx.doi.org/10.1109/aCCESS.
2020.2966922.
[200] Shahidirad N, Niroomand M, Hooshmand RA. Investigation of PV power
plant
structures
based
on
Monte
Carlo
reliability
and
economic
analy-
sis. IEEE J Photovolt 2018;8(3):825–33. http://dx.doi.org/10.1109/JPHOTOV.
2018.2814922.
[201] Li H, Ding J, Huang J, Dong Y, Li X. Reliability evaluation of PV power systems
with consideration of time-varying factors. J Eng 2017;2017(13):1783–7. http:
//dx.doi.org/10.1049/joe.2017.0638.
[202] Perdue M, Gottschalg R. Energy yields of small grid connected photovoltaic
system: Effects of component reliability and maintenance. IET Renew Power
Gener 2015;9(5):432–7. http://dx.doi.org/10.1049/iet-rpg.2014.0389.
[203] Golnas A. PV system reliability: An operator’s perspective. IEEE J Photovolt
2013;3(1):416–21. http://dx.doi.org/10.1109/JPHOTOV.2012.2215015.
[204] Gunda T, Hackett S, Kraus L, Downs C, Jones R, McNalley C, Bolen M,
Walker A. A machine learning evaluation of maintenance records for common
failure modes in PV inverters. IEEE Access 2020;8:211610–20. http://dx.doi.
org/10.1109/ACCESS.2020.3039182.
[205] Tao S, Li C, Zhang L, Tang Y. Operational risk assessment of grid-connected
PV system considering weather variability and component availability. Energy
Procedia 2018;145:252–8. http://dx.doi.org/10.1016/j.egypro.2018.04.047.
[206] Shin JW, Yoon KH, Chai HS, Kim JC. Reliability-centered maintenance
scheduling of photovoltaic components according to failure effects. Energies
2022;15(7):1–15. http://dx.doi.org/10.3390/en15072529.
[207] Rajput P, Malvoni M, Kumar NM, Sastry OS, Tiwari GN. Risk priority number
for understanding the severity of photovoltaic failure modes and their impacts
on performance degradation. Case Stud Therm Eng 2019;16(October):100563.
http://dx.doi.org/10.1016/j.csite.2019.100563.
[208] Rajput P, Malvoni M, Sastry O, Tiwari G. Failure mode and effect analysis of
monocrystalline silicon photovoltaic modules after 24 years outdoor exposure
in semi-arid climate. In: AIP conference proceedings. Vol. 2276, AIP Publishing
LLC; 2020, 020004. http://dx.doi.org/10.1063/5.0025707.
[209] Barkhouse DAR, Gunawan O, Gokmen T, Todorov TK, Mitzi DB. Identification
of technical risks in the photovoltaic value chain and quantification of the
economic impact. Prog Photovolt, Res Appl 2015;20(1):6–11. http://dx.doi.org/
10.1002/pip.2857, arXiv:1303.4604.
[210] Sa’ad A, Nyoungue AC, Hajej Z. Improved preventive maintenance schedul-
ing for a photovoltaic plant under environmental constraints. Sustainability
(Switzerland) 2021;13(18). http://dx.doi.org/10.3390/su131810472.


---

Page 23

---

Renewable and Sustainable Energy Reviews 195 (2024) 114342
23
H. Abdulla et al.
[211] Yin H, Yin D, Mei F, Zheng J. Distributed PV operation and maintenance
scheduling method based on improved PSO-PRGA algorithm. In: 2022 4th
international conference on electrical engineering and control technologies.
CEECT, IEEE; 2022, p. 216–23. http://dx.doi.org/10.1109/CEECT55960.2022.
10030204.
[212] Abdallah R, Juaidi A, Abdel-Fattah S, Qadi M, Shadid M, Albatayneh A,
Çamur
H,
García-Cruz
A,
Manzano-Agugliaro
F.
The
effects
of
soiling
and
frequency
of
optimal
cleaning
of
PV
panels
in
palestine.
Energies
2022;15(12):4232. http://dx.doi.org/10.3390/en15124232.
[213] Cheema A, Shaaban MF, Ismail MH, Azzouz MA. A new approach for long-
term optimal scheduling of photovoltaic panels cleaning. In: 2021 international
conference on electromechanical and energy systems. SIELMEN, IEEE; 2021, p.
319–24. http://dx.doi.org/10.1109/SIELMEN53755.2021.9600271.
[214] Al-Kouz W, Al-Dahidi S, Hammad B, Al-Abed M. Modeling and analysis
framework for investigating the impact of dust and temperature on PV sys-
tems’ performance and optimum cleaning frequency. Appl Sci (Switzerland)
2019;9(7). http://dx.doi.org/10.3390/app9071397.
[215] Mithhu MMH, Rima TA, Khan MR. Global analysis of optimal cleaning cycle
and profit of soiling affected solar panels. Appl Energy 2021;285(September
2020). http://dx.doi.org/10.1016/j.apenergy.2021.116436.
[216] Sánchez-Barroso G, González-Domínguez J, García-Sanz-Calcedo J, Sanz JG.
Markov chains estimation of the optimal periodicity for cleaning photovoltaic
panels installed in the dehesa. Renew Energy 2021;179:537–49. http://dx.doi.
org/10.1016/j.renene.2021.07.075.
[217] Alrabghi A, Almaraashi M. Investigating cleaning frequency of photovoltaic
solar plants prone to soiling through stochastic simulation. Int J Simul: Syst
Sci Technol 2017;18(2):4.1–5. http://dx.doi.org/10.5013/IJSSST.a.18.02.04.
[218] Fan S, Yao X, Cao S, Zhao B. An optimization method based on adaptive
dynamic programming for cleaning photovoltaic panels. In: 2020 39th Chinese
control conference. CCC, IEEE; 2020, p. 1565–8. http://dx.doi.org/10.23919/
CCC50068.2020.9189437.
[219] Wang Z, Xu Z, Zhang Y, Xie M. Optimal cleaning scheduling for photovoltaic
systems in the field based on electricity generation and dust deposition
forecasting. IEEE J Photovolt 2020;10(4):1126–32. http://dx.doi.org/10.1109/
JPHOTOV.2020.2981810.
[220] González-Castillo M, Navarrete P, Tapia T, Lorca Á, Olivares D, Negrete-
Pincetic M. Cleaning scheduling in photovoltaic solar farms with deterministic
and stochastic optimization. Sustain Energy Grids Netw 2023;36:101147. http:
//dx.doi.org/10.1016/j.segan.2023.101147.
[221] Wang Z, Xu Z, Wang X, Xie M. A temporal-spatial cleaning optimization method
for photovoltaic power plants. Sustain Energy Technol Assess 2021;49(August
2021):101691. http://dx.doi.org/10.1016/j.seta.2021.101691.
[222] Li X, Chen W, Lei H, Pei T, Pei X. A double-layer optimization maintenance
strategy for photovoltaic power generation systems considering component
correlation and availability. Front Energy Res 2022;10(May):1–13. http://dx.
doi.org/10.3389/fenrg.2022.850954.
[223] Chen W, Li X, Ji Q, Pei X, Wang Z, He F. A dynamic and combined mainte-
nance strategy for photovoltaic power plants considering the dependencies and
availability of components. Electr Eng 2022;104(6):3779–92. http://dx.doi.org/
10.1007/s00202-022-01576-7.
[224] Qi X, Zheng J, He W, Yin D, Yin H. Multi-objective maintenance strategy
optimization of distributed photovoltaic plants. In: 2020 IEEE 1st China
international youth conference on electrical engineering. CIYCEE, IEEE; 2020,
p. 1–6. http://dx.doi.org/10.1109/CIYCEE49808.2020.9332730.
[225] León J, Martín-Campo FJ, Ortuño MT, Vitoriano B, Carrasco LM, Narvarte L.
A methodology for designing electrification programs for remote areas. CEJOR
Cent Eur J Oper Res 2020;28(4):1265–90. http://dx.doi.org/10.1007/s10100-
019-00649-6.
[226] Carrasco LM, Martín-Campo FJ, Narvarte L, Ortuño MT, Vitoriano B. Design of
maintenance structures for rural electrification with solar home systems. The
case of the moroccan program. Energy 2016;117:47–57. http://dx.doi.org/10.
1016/j.energy.2016.10.073.
[227] Hua C, Kuang L, Pi D. Maintenance and operation optimization algorithm
of PV plants under multiconstraint conditions. Complexity 2020;2020. http:
//dx.doi.org/10.1155/2020/7975952.
[228] An Q, Hu Q, Tang R, Rao L. Intelligent scheduling methodology for UAV
swarm remote sensing in distributed photovoltaic array maintenance. Sensors
2022;22(12). http://dx.doi.org/10.3390/s22124467.
[229] Pedro F, García M, Segovia I, Pliego A. A novel approach to optimize the
positioning and measurement parameters in photovoltaic aerial inspections.
Renew Energy 2022;187. http://dx.doi.org/10.1016/j.renene.2022.01.071.
[230] Sizkouhi
AMM,
Esmailifar
SM,
Aghaei
M,
De
Oliveira
AKV,
Rüther
R.
Autonomous path planning by unmanned aerial vehicle (UAV) for precise
monitoring of large-scale PV plants. In: 2019 IEEE 46th photovoltaic special-
ists conference. PVSC, IEEE; 2019, p. 1398–402. http://dx.doi.org/10.1109/
PVSC40753.2019.8980862.
[231] Lofstad-Lie
V,
Marstein
ES,
Simonsen
A,
Skauli
T.
Cost-effective
flight
strategy for aerial thermography inspection of photovoltaic power plants.
IEEE J Photovolt 2022;12(6):1543–9. http://dx.doi.org/10.1109/JPHOTOV.
2022.3202072.
[232] Ding Y, Cao R, Liang S, Qi F, Yang Q, Yan W. Density-based optimal UAV
path planning for photovoltaic farm inspection in complex topography. In:
2020 Chinese control and decision conference. CCDC, IEEE; 2020, p. 3931–6.
http://dx.doi.org/10.1109/CCDC49329.2020.9164257.
[233] Salahat E, Asselineau C-A, Coventry J, Mahony R. Waypoint planning for
autonomous aerial inspection of large-scale solar farms. In: IECON 2019-45th
annual conference of the IEEE industrial electronics society. Vol. 1, IEEE; 2019,
p. 763–9. http://dx.doi.org/10.1109/IECON.2019.8927123.
[234] Di Placido A, Archetti C, Cerrone C. A genetic algorithm for the close-
enough traveling salesman problem with application to solar panels diagnostic
reconnaissance. Comput Oper Res 2022;145(July 2021):105831. http://dx.doi.
org/10.1016/j.cor.2022.105831.
[235] Rosende SB, Sánchez-Soriano J, Muñoz CQG, Andrés JF. Remote manage-
ment architecture of UAV fleets for maintenance, surveillance, and security
tasks in solar power plants. Energies 2020;13(21). http://dx.doi.org/10.3390/
en13215712.
[236] Luo X, Li X, Yang Q, Wu F, Zhang D, Yan W, Xi Z. Optimal path planning
for UAV based inspection system of large-scale photovoltaic farm. In: 2017
Chinese automation congress. CAC, IEEE; 2017, p. 4495–500. http://dx.doi.
org/10.1109/CAC.2017.8243572.
[237] Lindig S, Gallmetzer S, Herz M, Louwen A, Koumpli E, Sebastian En-
riquez Paez P, Moser D. Towards the development of an optimized decision
support system for the PV industry: A comprehensive statistical and economical
assessment of over 35,000 O&M tickets. Prog Photovolt, Res Appl 2022. http:
//dx.doi.org/10.1002/pip.3637.
[238] Woyte A, Goy S. Large grid-connected photovoltaic power plants: Best practices
for the design and operation of large photovoltaic power plants. In: The
performance of photovoltaic (PV) systems. Elsevier; 2017, p. 321–37. http:
//dx.doi.org/10.1016/B978-1-78242-336-2.00011-2.
[239] Garralaga Rojas E, Sadri H, Krueger W. Case study of MW-sized power
generation at St. Eustatius island combining photovoltaics, battery storage,
and gensets. Prog Photovolt, Res Appl 2020;28(6):562–8. http://dx.doi.org/10.
1002/pip.3222.
[240] Al-Quraan A, Al-Qaisi M. Modelling, design and control of a standalone hybrid
PV-wind micro-grid system. Energies 2021;14(16):4849. http://dx.doi.org/10.
3390/en14164849.
[241] Zhang W, Vatn J, Rasheed A. A review of failure prognostics for predictive
maintenance of offshore wind turbines. In: Journal of physics: conference series.
Vol. 2362, IOP Publishing; 2022, 012043. http://dx.doi.org/10.1088/1742-
6596/2362/1/012043.
[242] Fox H, Pillai AC, Friedrich D, Collu M, Dawood T, Johanning L. A review
of predictive and prescriptive offshore wind farm operation and maintenance.
Energies 2022;15(2):504. http://dx.doi.org/10.3390/en15020504.
[243] Tian Z, Zhang H. Wind farm predictive maintenance considering component
level repairs and economic dependency. Renew Energy 2022;192:495–506.
http://dx.doi.org/10.1016/j.renene.2022.04.060.
[244] Hsu J-Y, Wang Y-F, Lin K-C, Chen M-Y, Hsu JH-Y. Wind turbine fault
diagnosis and predictive maintenance through statistical process control and
machine learning. IEEE Access 2020;8:23427–39. http://dx.doi.org/10.1109/
access.2020.2968615.
[245] Yalçin T, Paradell Solà P, Stefanidou-Voziki P, Domínguez-García JL, Demirde-
len T. Exploiting digitalization of solar PV plants using machine learning: Digital
twin concept for operation. Energies 2023;16(13):5044. http://dx.doi.org/10.
3390/en16135044.
[246] Avila L, De Paula M, Trimboli M, Carlucho I. Deep reinforcement learning
approach for MPPT control of partially shaded PV systems in smart grids. Appl
Soft Comput 2020;97:106711. http://dx.doi.org/10.1016/j.asoc.2020.106711.
[247] Zhang J, Liu Y, Li Y, Ding K, Feng L, Chen X, Chen X, Wu J. A reinforce-
ment learning based approach for on-line adaptive parameter extraction of
photovoltaic array models. Energy Convers Manage 2020;214(January):112875.
http://dx.doi.org/10.1016/j.enconman.2020.112875.
[248] Correa-Jullian C, López Droguett E, Cardemil JM. Operation scheduling in a
solar thermal system: A reinforcement learning-based framework. Appl Energy
2020;268(April):114943. http://dx.doi.org/10.1016/j.apenergy.2020.114943.
[249] Pinciroli L, Baraldi P, Ballabio G, Compare M, Zio E. Optimization of the
operation and maintenance of renewable energy systems by deep reinforcement
learning. Renew Energy 2022;183:752–63. http://dx.doi.org/10.1016/j.renene.
2021.11.052.
