# Impact of Artificial Intelligence on the Planning and Operation of Distributed Energy Systems in Smart Grids

## Paper Metadata

- **Filename:** Impact of Artificial Intelligence on the Planning and Operation of Distributed Energy Systems in Smart Grids.pdf
- **DOI:** None
- **Authors:** Not available
- **Year:** Not available
- **Journal/Venue:** Not available
- **URL:** Not available
- **Extraction Date:** 2025-06-03T15:04:03.408963
- **Total Pages:** 22

## Abstract

Abstract not available from BibTeX metadata.

## Keywords

Keywords not available from BibTeX metadata.

---

## Full Text Content



### Page 1

Citation: Arévalo, P.; Jurado, F.
Impact of Artificial Intelligence on the
Planning and Operation of
Distributed Energy Systems in Smart
Grids. Energies 2024, 17, 4501.
https://doi.org/10.3390/en17174501
Academic Editor: Angela Russo
Received: 8 August 2024
Revised: 30 August 2024
Accepted: 6 September 2024
Published: 8 September 2024
Copyright: © 2024 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).
energies
Review
Impact of Artificial Intelligence on the Planning and Operation
of Distributed Energy Systems in Smart Grids
Paul Arévalo 1,2,*
and Francisco Jurado 2
1
Department of Electrical Engineering, Electronics and Telecommunications (DEET), Faculty of Engineering,
University of Cuenca, Balzay Campus, Cuenca 010107, Azuay, Ecuador
2
Department of Electrical Engineering, EPS Linares, University of Jaen, 23700 Jaen, Spain; fjurado@ujaen.es
*
Correspondence: warevalo@ujaen.es
Abstract: This review paper thoroughly explores the impact of artificial intelligence on the planning
and operation of distributed energy systems in smart grids. With the rapid advancement of artificial
intelligence techniques such as machine learning, optimization, and cognitive computing, new
opportunities are emerging to enhance the efficiency and reliability of electrical grids. From demand
and generation prediction to energy flow optimization and load management, artificial intelligence
is playing a pivotal role in the transformation of energy infrastructure. This paper delves deeply
into the latest advancements in specific artificial intelligence applications within the context of
distributed energy systems, including the coordination of distributed energy resources, the integration
of intermittent renewable energies, and the enhancement of demand response. Furthermore, it
discusses the technical, economic, and regulatory challenges associated with the implementation
of artificial intelligence-based solutions, as well as the ethical considerations related to automation
and autonomous decision-making in the energy sector. This comprehensive analysis provides a
detailed insight into how artificial intelligence is reshaping the planning and operation of smart grids
and highlights future research and development areas that are crucial for achieving a more efficient,
sustainable, and resilient electrical system.
Keywords: artificial intelligence in smart grids; distributed energy systems optimization; renewable
energy integration; demand response
1. Introduction
The integration of artificial intelligence (AI) into smart grids is rapidly transforming
the landscape of energy systems, offering new pathways to optimize the planning and
operation of distributed energy resources (DERs) [1–3]. With the growing adoption of renewable energy sources, challenges such as grid stability, energy distribution optimization,
and the integration of bidirectional energy flows are becoming increasingly complex [4–6].
AI technologies, including machine learning and neural networks, have emerged as critical
tools in addressing these challenges by enabling advanced energy management, fault detection, and predictive maintenance [4,7,8]. Despite these advances, the implementation of
AI in smart grids is not without its hurdles, as technical, economic, and regulatory barriers
persist [6,9,10]. This paper reviews the current state of AI applications in distributed energy
systems, highlighting their transformative impact on smart grid operations and identifying
crucial areas for future research to enhance grid resilience and efficiency.
The integration of AI into smart grids has become a critical driver for enhancing the
efficiency, reliability, and sustainability of energy systems. AI’s ability to process large
amounts of data and optimize energy operations is transforming how DERs are managed
within smart grids [1,4,11]. AI technologies, such as machine learning and neural networks,
play pivotal roles in improving demand forecasting, load management, and integrating
renewable energy sources [9,12,13]. AI-driven energy management systems are key to optimizing energy consumption and generation, significantly reducing operational costs and
Energies 2024, 17, 4501. https://doi.org/10.3390/en17174501
https://www.mdpi.com/journal/energies

---


### Page 2

Energies 2024, 17, 4501
2 of 22
environmental impacts. For example, AI algorithms like neural networks and optimization
techniques have been employed to enhance energy demand forecasting, allowing for more
accurate load predictions and efficient resource allocation [2,14]. Gaussian process regression models, for instance, have been applied to forecast peak demand, thereby improving
grid stability and reducing the need for expensive peak power plants [7]. Machine learning
techniques are also used to optimize voltage profiles and manage reactive power within
smart grids, resulting in improved power quality and system efficiency [8,15]. In particular,
AI-based predictive maintenance strategies extend the lifespan of grid components by
anticipating failures and scheduling proactive maintenance [5,16]. These advancements
illustrate the transformative potential of AI in creating more adaptive and resilient energy
management systems [6,17].
The integration of DERs, such as solar panels and wind turbines, into existing grid
infrastructure poses significant challenges. AI technologies are instrumental in coordinating
and controlling these resources to ensure grid stability and efficiency [18,19]. Virtual power
plants (VPPs) are an excellent example of AI’s potential, as they aggregate DERs to optimize
energy trading and resource distribution [10]. Studies have shown that AI enhances the
reliability of smart grids by improving the integration and management of DERs [3,20].
Moreover, AI facilitates the development of microgrids, which are localized grids that
can operate independently or in conjunction with the main grid [21,22]. AI algorithms
optimize energy flow within microgrids, balancing supply and demand to enhance energy
efficiency and resilience [23,24]. The use of AI in microgrid management has been shown
to improve grid stability and reduce energy costs by optimizing the use of local energy
resources [25,26]. The integration of renewable energy sources, such as solar and wind,
presents unique challenges due to their intermittent nature. AI technologies offer crucial
solutions by providing accurate forecasting and real-time monitoring capabilities [27,28].
Research shows that AI can enhance renewable integration by improving grid stability
and enabling more efficient energy distribution [29,30]. For example, AI algorithms are
used to predict solar and wind energy output, facilitating better scheduling and dispatch of
energy resources [31,32]. These AI-driven solutions are essential for maintaining a balanced
supply-demand equation and ensuring the reliability of power systems [33,34].
Despite these advancements, several challenges remain in deploying AI in smart
grids. Technical issues such as data privacy, cybersecurity, and integrating AI with existing
grid infrastructures present significant hurdles [35,36]. Developing robust cybersecurity
measures is essential to protect sensitive data and ensure AI system integrity [37,38]. Furthermore, economic considerations, including AI implementation costs and potential job
displacement, must be addressed to ensure sustainable adoption [39,40]. Regulatory and
policy frameworks are crucial in facilitating AI integration into smart grids. There is a
need for standardized guidelines that address the ethical implications of automation and
decision-making, as well as policies that encourage innovation while safeguarding consumer interests [41,42]. As AI technologies evolve, they offer promising opportunities for
achieving more resilient, efficient, and sustainable energy systems [43,44]. However, realizing AI’s full potential in distributed energy systems requires addressing these technical,
economic, and regulatory challenges [45,46]. The literature underscores AI’s transformative
potential in enhancing smart grid operations, emphasizing its ability to improve energy
management, optimize DER integration, and support renewable energy adoption [47,48].
As the field progresses, continued exploration of innovative AI applications is vital to
address the growing complexity of energy systems and contribute to a sustainable energy
future [49,50]. This review highlights the importance of leveraging AI to meet the evolving
demands of modern energy infrastructures and identifies key areas for future research and
development [51,52]. Moreover, the application of AI in smart grids also extends to other
areas such as predictive maintenance, fault detection, and grid security [53,54]. By using
AI, utilities can proactively identify potential faults and address them before they lead
to significant disruptions [55,56]. Additionally, AI technologies contribute to enhancing
grid security by monitoring network traffic and identifying potential cyber threats [57,58].

---


### Page 3

Energies 2024, 17, 4501
3 of 22
These capabilities are essential for maintaining the reliability and safety of modern energy
systems [59,60]. The ongoing advancements in AI present numerous opportunities for
further improving the efficiency and resilience of smart grids [61,62].
Despite the extensive research on the integration of AI in smart grids, several gaps
remain in the literature. Many studies focus primarily on the technical aspects of AI
applications, such as demand forecasting and energy management [1,7,12], but often
overlook the challenges of integrating AI-driven solutions with existing grid infrastructures,
particularly in the context of DERs [10,18]. Additionally, while there is considerable
emphasis on the potential of AI to enhance renewable energy integration [27,29], the
literature lacks comprehensive analyses of the regulatory and economic barriers that
impede the widespread adoption of these technologies [35,40]. Furthermore, the ethical
implications of AI in autonomous decision-making within energy systems are seldom
addressed [41,42]. This paper aims to fill these gaps by providing a holistic review of AI
applications in distributed energy systems, focusing not only on the technical innovations
but also on the integration challenges, economic considerations, and regulatory frameworks.
By examining case studies and real-world applications, this paper offers insights into
overcoming the barriers to AI adoption in smart grids and proposes strategies for enhancing
system resilience and efficiency. To contextualize the unique contributions of our review in
comparison to existing works, we have conducted a comparative analysis of several recent
articles that address the use of artificial intelligence (AI) in smart grids. Table 1 summarizes
this comparison, highlighting the key areas where these review articles contribute to the
field and, more importantly, identifying the aspects they do not cover. Unlike these studies,
our paper provides a comprehensive framework that encompasses all phases of the power
system—generation, transmission, and distribution—and addresses critical topics such as
cybersecurity, integration with emerging technologies, and research gaps. This underscores
the originality and breadth of our approach, offering a more holistic and comprehensive
view of AI applications in energy systems.
Table 1. Comparative analysis of key features in AI review papers for smart grids.
Ref.
AI Across
Power Phases
AI for
Cybersecurity
AI with
Emerging Tech
Research Gaps
and Future
Centralized and
Distributed
Comparison of
AI Techniques
Holistic
Framework
[1]
X
X
✔
✔
X
✔
X
[11]
X
X
✔
X
X
X
X
[4]
X
X
✔
✔
✔
✔
X
[9]
X
X
X
X
X
X
X
[12]
X
X
X
X
X
✔
X
[63]
X
✔
X
X
X
X
X
[64]
X
✔
✔
✔
X
X
X
[10]
X
✔
✔
X
✔
✔
X
[65]
X
X
✔
✔
X
X
X
This paper
✔
✔
✔
✔
✔
✔
✔
To provide a clearer and more concise overview of this review paper’s contributions,
we have refined our main contributions into the following key points:
•
Comprehensive analysis of AI applications: This review offers a thorough examination of artificial intelligence (AI) techniques across the key phases of power systems:
generation, transmission, and distribution. We explore the specific roles AI plays in
optimizing operations, enhancing efficiency, and improving system resilience.
•
Identification of research gaps and challenges: We identify significant research gaps in
the application of AI to power systems, particularly in areas such as the integration
of renewable energy sources, the development of robust predictive models, and the
interoperability of diverse energy systems. The paper discusses the current challenges
in deploying AI, including technical, cybersecurity, and regulatory hurdles.
•
Future perspectives and opportunities: This paper outlines future research directions
and opportunities for further development of AI applications in power systems. We

---


### Page 4

Energies 2024, 17, 4501
4 of 22
propose strategies for advancing AI integration, such as combining AI with emerging
technologies like blockchain and Io T, and emphasize the need for interdisciplinary
research to address the complex challenges of modern energy systems.
•
Holistic framework for AI in power systems: We introduce a new holistic framework
that illustrates the application of AI techniques across all phases of the power system, providing a structured approach to understand AI’s impact and guiding future
research and development efforts.
2. Methodology
The methodology for evaluating the impact of AI on the planning and operation
of distributed energy systems in smart grids is structured into four key components, as
illustrated in Figure 1. Each component encompasses specific criteria and strategies to
ensure a comprehensive and systematic review.
Figure 1. Comprehensive methodology framework for evaluating AI impact on distributed energy
systems in smart grids.
2.1. Literature Review Process
The literature review process for this study was conducted systematically to ensure
a comprehensive and unbiased selection of relevant publications. This process involved
clearly defined selection criteria and a structured search strategy to identify pertinent
studies related to the application of AI in smart grids and distributed energy systems.
2.1.1. Selection Criteria
The selection criteria were established to ensure the inclusion of high-quality, relevant
studies that provide comprehensive insights into the research topic. The criteria included
the following:
•
Publication date range: The review focused on articles published between 2014 and
2024 to capture the most recent advancements and trends in AI applications within
smart grids. This range reflects the rapid development of AI technologies and their
growing integration into energy systems.
•
Journal quality: Only peer-reviewed journal articles were included to ensure the
credibility and scientific rigor of the literature reviewed. Journals were selected

---


### Page 5

Energies 2024, 17, 4501
5 of 22
based on their impact factor and relevance to the fields of energy, AI, and smart
grid technology.
•
Language: Only articles published in English were considered, as it is the predominant
language of scientific discourse in this field.
•
Keywords: The review focused on articles that included specific keywords and phrases,
such as “artificial intelligence,” “smart grids,” “distributed energy resources,” “machine learning,” and “renewable energy integration.” These keywords were essential
to capturing studies relevant to the research objectives.
•
Relevance to research objectives: Studies were included if they addressed key themes
such as AI-driven energy management, integration of DERs, challenges and opportunities in AI adoption, and regulatory and ethical considerations related to AI in
energy systems.
2.1.2. Search Strategy
The search strategy was designed to ensure a comprehensive and systematic identification of relevant literature. The following databases were utilized for the search:
•
Scopus: Known for its extensive collection of scientific publications, Scopus was
used to identify articles across a wide range of disciplines, ensuring coverage of both
technical and interdisciplinary studies.
•
Web of Science: This database was selected for its comprehensive indexing of highimpact journals and its ability to track citation networks, allowing for the identification
of influential studies and emerging trends.
•
Search terms: A combination of specific search terms and Boolean operators was used
to refine the search and capture relevant studies. The primary search terms included
“artificial intelligence AND smart grids,” “AI AND distributed energy systems,” “machine learning AND energy management,” “AI AND renewable energy integration,”
and “AI challenges AND opportunities in smart grids.”
2.2. Analytical Framework
The analytical framework for this study is designed to systematically evaluate the
impact of AI on distributed energy systems within smart grids. This framework provides a
structured approach to analyzing the effectiveness of AI applications and their contributions
to enhancing energy management, system resilience, and sustainability.
2.2.1. Methodological Approach
The methodological approach combines qualitative and quantitative analysis to assess
the impact of AI technologies on distributed energy systems. The approach involves the
following key components:
•
Literature synthesis: A thorough synthesis of the selected literature was conducted to
identify common themes, trends, and gaps in the research. This synthesis provides
a foundational understanding of how AI is being applied across various aspects
of smart grids, including demand forecasting, load management, and renewable
energy integration.
•
Case study analysis: Case studies of AI implementations in real-world energy systems
were examined to provide practical insights into the challenges and successes of AI
adoption. These case studies highlight specific applications of AI, such as predictive
maintenance, virtual power plant optimization, and microgrid management, offering
detailed examples of AI’s impact on system performance.
•
Comparative analysis: A comparative analysis was performed to evaluate different
AI techniques and algorithms used in energy systems. This analysis compares the
effectiveness, scalability, and adaptability of various AI approaches, such as machine
learning models, neural networks, and optimization algorithms, in addressing key
challenges in smart grid operations.

---


### Page 6

Energies 2024, 17, 4501
6 of 22
•
Thematic categorization: The literature and case study findings were categorized
into thematic areas such as technical challenges, economic impacts, regulatory considerations, and ethical implications. This categorization enables a comprehensive
understanding of the multidimensional aspects of AI applications in distributed energy systems.
2.2.2. Evaluation Criteria
To evaluate the effectiveness of AI applications in distributed energy systems, the
following criteria were established:
•
Performance improvement: The extent to which AI applications enhance the performance of energy systems, measured by improvements in efficiency, reliability, and grid
stability. Key performance indicators include reductions in energy losses, increased
accuracy of demand forecasts, and enhanced integration of renewable energy sources.
•
Scalability: The ability of AI solutions to be scaled across different sizes and types of
energy systems, from small microgrids to large interconnected networks. Scalability
is assessed by examining the adaptability of AI technologies to varying levels of
complexity and infrastructure.
•
Cost-effectiveness: The economic viability of AI applications, including cost savings achieved through operational efficiencies and reductions in energy costs. Costeffectiveness is evaluated by comparing the implementation and maintenance costs of
AI solutions against the financial benefits realized.
•
Regulatory compliance: The degree to which AI applications align with existing
regulatory frameworks and policies, including considerations for data privacy, security,
and ethical standards. Compliance is assessed by reviewing regulatory guidelines and
identifying areas where AI solutions may need to adapt to meet policy requirements.
•
Stakeholder acceptance: The level of acceptance and support from key stakeholders,
including utility companies, policymakers, and consumers. Stakeholder acceptance is
measured through qualitative assessments of stakeholder engagement and feedback
on AI implementations.
3. AI Applications in Distributed Energy Systems
3.1. AI Techniques and Innovations
3.1.1. Overview of AI Techniques
Artificial intelligence techniques have become foundational in transforming distributed energy systems by enhancing operational efficiency and optimizing resource
utilization. Key AI techniques include machine learning (ML), deep learning, and optimization algorithms. Machine learning algorithms are used to analyze vast datasets,
identify patterns, and predict future energy demands [63,66]. These models are particularly
effective in demand response applications, where they help utilities predict and manage
peak load scenarios [67,68]. Deep learning, especially through neural networks, is utilized
for complex tasks such as power flow analysis and anomaly detection within unbalanced
distribution grids [69,70]. Models like convolutional neural networks (CNNs) and radial
basis function networks (RBFnets) excel at capturing nonlinear relationships within the
grid, making them invaluable for real-time monitoring and fault detection [71,72]. Optimization algorithms, such as genetic algorithms and particle swarm optimization, are
also widely used to solve complex problems related to energy distribution and resource
allocation [73,74]. These algorithms enable the efficient design and operation of microgrids,
ensuring optimal use of both renewable and conventional energy sources [75,76].
3.1.2. Innovations in AI
Recent innovations in AI have significantly advanced the capabilities of energy systems. Reinforcement learning (RL) techniques, such as deep Q-networks, have been applied
to optimize electric vehicle (EV) charging schedules, balancing supply and demand to
maintain grid stability [26,77]. This is particularly important as the adoption of EVs in-

---


### Page 7

Energies 2024, 17, 4501
7 of 22
creases, requiring more sophisticated management of charging infrastructure [78,79]. The
integration of AI with other emerging technologies, such as the internet of things (Io T) and
blockchain, has led to the development of more resilient and efficient power grids [80,81].
AI-driven predictive analytics improve demand forecasting accuracy, enabling better load
management and energy distribution [82,83]. These tools allow grid operators to anticipate
changes in demand and adjust energy flows dynamically, reducing operational costs and
improving service reliability [84,85]. Moreover, AI algorithms are now capable of processing real-time data from smart meters and sensors, facilitating intelligent decision-making
and optimizing grid operations [86,87].
3.1.3. AI Techniques for Planning and Operation of Distributed Energy Systems in
Smart Grids
AI techniques for planning and operation of distributed energy systems in smart grids
are as follows:
•
Artificial intelligence (AI) techniques have become foundational in transforming distributed energy systems by enhancing operational efficiency and optimizing resource
utilization. Key AI techniques include machine learning (ML), deep learning, genetic
algorithms, and multi-agent systems.
•
Machine learning (ML): ML algorithms are widely used for predictive analytics and
demand forecasting in smart grids, particularly in demand response applications
where they help utilities predict and manage peak load scenarios [3,7,67]. These
models excel at handling large datasets and learning from historical data to make
accurate predictions, though they may require significant computational resources,
limiting real-time applicability due to their complexity [70].
•
Deep learning (DL): DL techniques, especially neural networks, are effective for complex pattern recognition and fault detection within power systems. They are used for
real-time monitoring and power flow analysis, making them invaluable for managing
unbalanced distribution grids [8,15,77]. However, their high computational demands
and need for extensive training data can pose challenges in certain applications [61].
•
Genetic algorithms (GA): GA are optimization techniques effective for solving complex
problems related to energy distribution and resource allocation, such as in microgrids.
These algorithms enable efficient energy management and operation of both renewable
and conventional energy sources [75,76,78]. While highly adaptable, GA often require
many iterations to converge to an optimal solution, which can be time-consuming [61].
•
Multi-agent systems (MAS): MAS involve multiple intelligent agents that interact
to achieve a common goal, such as load balancing or fault management. These
systems are highly flexible and can operate in decentralized environments, making
them suitable for distributed energy resources (DERs) integration and grid stability
enhancement [78,88,89]. However, their implementation can be complex, requiring
robust communication protocols and coordination mechanisms [78].
Table 2 provides a comparative analysis of different AI techniques used in smart
grids, highlighting their capabilities in terms of data handling, computational complexity,
real-time applicability, robustness, and adaptability.
Table 2. Comparative analysis of AI techniques for smart grids.
AI Technique
Data Handling
Computational
Complexity
Real-Time
Applicability
Robustness
Adaptability
Machine Learning
High
Medium to High
Medium
Medium
Medium
Deep Learning
Very High
High
Low
High
Low
Genetic Algorithms
Medium
Medium
Low
Medium
High
Multi-Agent Systems
High
High
High
High
High

---


### Page 8

Energies 2024, 17, 4501
8 of 22
3.1.4. AI Techniques for Regression and Classification in Smart Grids
AI techniques for regression and classification in smart grids are as follows:
•
AI techniques play a crucial role in smart grids and distributed energy systems by
providing advanced methods for regression and classification tasks. These tasks are
fundamental in analyzing and predicting various parameters critical for the efficient
operation and planning of energy systems.
•
Regression techniques: Regression is used in smart grids to predict continuous variables, such as energy consumption, power generation from renewable sources, or
electricity prices. Machine learning algorithms, like linear regression, support vector
regression (SVR), and neural networks, are commonly employed for these purposes.
For example, linear regression can be used to model the relationship between electricity demand and influencing factors such as weather conditions or time of day,
which helps utilities in load forecasting and demand management [45,53]. Another
example is using support vector regression to predict solar power generation based on
historical weather data, which enhances the accuracy of energy management in solar
farms [69].
•
Classification techniques: Classification techniques are used to categorize data into
discrete classes, making them essential for fault detection, power quality assessment,
and demand response strategies in smart grids. Algorithms such as decision trees,
random forests, and deep learning classifiers are applied to classify power system
states, detect faults, and manage grid stability. For instance, decision trees can be used
to classify whether a transformer is likely to fail based on sensor data, allowing for
proactive maintenance and reducing downtime [74,90]. Additionally, deep learning
classifiers can analyze patterns in grid data to predict and classify potential grid
anomalies, enhancing the reliability and security of energy distribution systems [82,91].
3.1.5. Advanced AI Techniques for Smart Grids
Recent advancements in artificial intelligence have introduced more sophisticated
techniques that offer promising applications for smart grids, particularly in enhancing
energy management, security, and predictive maintenance:
•
Generative Adversarial Networks (GANs): GANs are a class of machine learning
frameworks where two neural networks, the generator and the discriminator, are
trained simultaneously. GANs have been widely used in image generation and data
augmentation, but their potential extends to smart grids as well. For instance, GANs
can generate realistic synthetic data to enhance the training of AI models used in
demand forecasting and anomaly detection. This synthetic data can simulate various
scenarios of energy consumption and generation, helping improve the robustness and
generalizability of predictive models [43,69]. Moreover, GANs can aid in the detection
and mitigation of cyber threats by generating adversarial examples to test the resilience
of smart grid cybersecurity systems, as discussed by Wang et al. [70]. This technique
helps in identifying potential vulnerabilities in AI models deployed within the grid,
ensuring that they are well-prepared to handle real-world adversarial attacks.
•
Graph Neural Networks (GNNs): GNNs are designed to perform inference on data
represented as graphs, making them particularly suitable for applications in smart
grids, which can be naturally modeled as graphs of interconnected nodes and edges
(e.g., substations, transmission lines, and distributed energy resources). GNNs can
effectively capture the spatial dependencies and topological characteristics of the grid,
enabling enhanced grid management and fault detection capabilities. For example,
GNNs can be used to predict the optimal flow of electricity in the grid by analyzing
the dynamic relationships between different components, thereby improving energy
distribution efficiency and reducing losses [49,76]. Additionally, GNNs are instrumental in identifying critical nodes and potential vulnerabilities in the network, which is
crucial for maintaining grid stability and preventing cascading failures [50,80]. This is

---


### Page 9

Energies 2024, 17, 4501
9 of 22
particularly valuable in scenarios involving complex interdependencies, such as those
seen in large-scale integration of renewable energy sources.
By integrating these advanced AI techniques, smart grids can achieve higher levels of
operational efficiency, security, and resilience. GANs and GNNs provide powerful tools for
enhancing data-driven decision-making processes, ensuring that energy systems are better
equipped to handle the complexities and uncertainties of modern energy landscapes.
3.2. Impact on Energy Management
AI techniques are transforming energy management in distributed energy systems by
enhancing demand forecasting and optimizing energy flow. Below, we expand on these
areas with recent research contributions.
3.2.1. Demand Forecasting
AI plays a crucial role in demand forecasting, which is essential for efficient energy
management in distributed energy systems. Machine learning models, such as support
vector machines and neural networks, are employed to predict energy consumption patterns based on historical data and external factors like weather conditions and market
trends [68,92]. These models enable energy providers to anticipate demand fluctuations
and adjust their operations accordingly, reducing the risk of overloading the grid and
ensuring a stable energy supply [71,79]. Recent studies have further refined these techniques. For example, a review on machine learning approaches for electric vehicle (EV)
energy consumption modeling highlights the use of neural networks to improve prediction
accuracy through feature extraction and pattern recognition [93]. This approach is crucial
for optimizing urban transport systems and supports the integration of EVs into smart
grids by accurately predicting energy consumption under varying conditions. Additionally,
advanced models such as the Autoformer variant have been developed for multi-step EV
charging load forecasting, achieving significant reductions in error margins compared to
traditional models [94]. These models are particularly effective in environments with high
variability, where precise forecasting is needed to manage energy resources efficiently.
AI-driven demand forecasting also facilitates the integration of renewable energy
sources by predicting their output variability and enabling more accurate scheduling of
energy resources [65,75]. This capability is vital for balancing supply and demand in realtime, especially in regions with high penetration of solar and wind energy [69,90]. Recent
advancements in deep learning, particularly in convolutional neural networks (CNNs),
have demonstrated high accuracy in predicting and mitigating climate change impacts on
energy systems, underscoring the versatility of AI in various energy contexts [95].
3.2.2. Energy Flow Optimization
AI techniques optimize energy flow and distribution within smart grids, improving
load balancing and enhancing overall system efficiency. Optimization algorithms, including
linear programming and genetic algorithms, are used to determine the optimal distribution
of energy resources across the grid [88,96]. These algorithms take into account various
constraints, such as generation capacity, transmission losses, and consumer demand, to
minimize energy costs and reduce environmental impact [61,64]. Recent advancements
have introduced hybrid models that integrate multiple AI techniques to enhance optimization processes. For example, a study on energy flow optimization using hybrid algorithms
combines genetic algorithms with machine learning to optimize energy storage and distribution, achieving higher accuracy and reduced computational time compared to standalone
models [94]. Such hybrid approaches enable real-time adjustments to grid operations, ensuring that energy is distributed efficiently and sustainably, minimizing energy losses, and
improving the economic viability of grid operations [97].
Moreover, AI-driven energy flow optimization allows for real-time adjustments to grid
operations, ensuring that energy is distributed efficiently and sustainably [85,98]. This is

---


### Page 10

Energies 2024, 17, 4501
10 of 22
particularly important for minimizing energy losses and improving the economic viability
of grid operations [74,99].
3.3. Coordination and Integration of DERs
Maintaining grid stability is a critical challenge in smart grids, especially with the
increasing integration of renewable energy sources and electric vehicles. AI techniques
enhance grid stability through advanced diagnostics, predictive maintenance, and dynamic
response strategies.
3.3.1. Battery Diagnostics and Predictive Maintenance
AI-driven diagnostics and predictive maintenance are essential for managing the
health of batteries and other critical components in smart grids. Recent studies highlight
the use of deep learning models to manage complex diagnostic tasks, such as battery
life forecasting and anomaly detection, under challenging conditions like inconsistent
data [100]. These models leverage AI for IT operations (AIOps) and explainable AI (XAI)
to improve accuracy and reduce computational costs, making them highly effective for
real-time applications in grid stability.
Furthermore, digital twin-based models are increasingly used for predictive maintenance, integrating multi-source data to accurately predict equipment failures and optimize
maintenance schedules [101]. This approach not only enhances the reliability of grid
operations but also reduces downtime and maintenance costs, contributing to overall
grid stability.
3.3.2. Dynamic Grid Response and Decision Support Systems
AI-based decision support systems (DSS) play a pivotal role in enhancing grid stability
by providing real-time insights and recommendations for grid management. In Industry
4.0 environments, these systems utilize machine learning and deep learning to analyze production data, identify potential faults, and ensure optimal operation [97]. The integration
of DSS with smart grid infrastructure allows for proactive management of grid stability,
reducing the impact of fluctuations in energy supply and demand.
Advanced AI techniques, such as those used in real-world battery diagnostics and
digital twin models, offer robust solutions for dynamic grid response, enabling grids to
adapt to changing conditions and maintain stability even under stress [100,101]. These
technologies provide a comprehensive approach to grid management, combining predictive
capabilities with real-time analytics to ensure a stable and efficient energy supply.
3.3.3. Integration of DERs
The integration of DERs, such as solar panels and wind turbines, is a critical aspect
of modern energy systems, and AI plays a pivotal role in facilitating this process. AI
algorithms coordinate DER operations by optimizing their dispatch and ensuring they work
harmoniously with the central grid [72,87]. Techniques like multi-agent systems and RL
are used to manage the dynamic interactions between DERs and the grid, improving their
efficiency and reliability [76,90]. AI-driven integration of DERs enhances grid flexibility and
supports the transition to a more decentralized and sustainable energy infrastructure [61,89].
These technologies enable more effective use of local resources, reducing dependency on
centralized power plants and minimizing transmission losses [91,102].
3.3.4. Enhancing System Flexibility
AI contributes significantly to enhancing the flexibility and reliability of distributed
energy systems. By leveraging advanced algorithms, AI enables the dynamic balancing
of supply and demand across the grid, allowing for rapid adjustments to changing conditions [91,99]. AI also facilitates the integration of energy storage systems, such as batteries
and pumped hydro storage, by optimizing their operation and ensuring they provide
backup power when needed [89,102]. This enhanced flexibility is crucial for accommodat-

---


### Page 11

Energies 2024, 17, 4501
11 of 22
ing the variability of renewable energy sources and maintaining grid stability [103,104].
Additionally, AI’s ability to predict and respond to system disruptions in real-time helps
prevent blackouts and maintain a consistent energy supply [105,106]. In Table 3, the significant AI techniques and innovations impacting distributed energy systems are presented,
highlighting key findings and citations for further exploration.
Table 3. Key findings on AI applications in distributed energy systems.
AI
Technique/Innovation
Description
Metrics
Performance
Unique Contribution
Ref.
Machine Learning in
Demand Response
ML models analyze datasets
to predict energy demand
and manage peak
load scenarios.
Accuracy, Response
Time
90% accuracy in peak load
prediction, 15% faster
response time than
traditional methods.
Utilizes hybrid ML models
for dynamic demand
response.
[65,77,92]
Deep Learning for
Anomaly Detection
Neural networks, such as
CNNs and RBFnets, detect
anomalies and perform
power flow analysis in
complex grids.
Precision, Recall
95% precision and 92% recall
in fault detection.
Combines deep learning
with real-time monitoring
for enhanced fault
detection.
[61,75,103]
Optimization
Algorithms
Genetic algorithms and
particle swarm optimization
solve complex energy
distribution problems.
Computational
Efficiency, Resource
Allocation
Reduces computational time
by 20%, optimizes resource
allocation by 25%.
Integrates multi-objective
optimization for
balanced energy
distribution.
[61,71,78]
Reinforcement
Learning (RL)
RL techniques, like deep
Q-networks, optimize EV
charging schedules and
energy management.
Learning Rate,
Scalability
Achieves 85% learning rate
improvement, scalable to
larger grids.
Implements RL for
real-time adaptive
scheduling in EV charging.
[61,78,92]
4. Challenges and Opportunities
4.1. Technical, Economic, and Regulatory Challenges
4.1.1. Technical Barriers
The implementation of AI-based solutions in distributed energy systems faces significant technical challenges. Among the most prominent obstacles are the effective integration
of DERs and the management of cybersecurity and data privacy, which are critical in an
increasingly interconnected environment. Current systems have limited capacity to handle
large volumes of real-time data, necessitating advances in infrastructure and technology
to support these demands [26]. Additionally, the inherent complexity of coordinating
multiple renewable energy sources, such as solar and wind, introduces further technical
challenges that require innovative solutions to ensure the stability and efficiency of the
energy system [66,70].
Another crucial technical aspect is the need for advanced AI algorithms capable
of processing and analyzing data with precision and efficiency. These algorithms must
be able to operate in environments with limited computational resources, which is a
significant challenge in remote areas or existing infrastructures not designed to handle AI
technologies [81,92]. Successful implementation of these technologies also depends on the
ability to integrate energy management systems that can optimize energy distribution and
enhance grid resilience [67,96].
4.1.2. Economic Impacts
The adoption of AI technologies in the energy sector involves several economic considerations. The high initial costs of implementation, including investment in advanced
infrastructure and staff training, pose a significant barrier for many organizations and
regions, especially those with limited resources [67,77]. Despite these costs, AI integration
can offer long-term economic benefits by improving operational efficiency, reducing energy
losses, and optimizing the use of renewable energy resources [78]. Conducting a detailed
cost-benefit analysis is essential to justifying the investment in these technologies. AI can
potentially reduce operational costs by automating processes and enhancing energy efficiency, leading to significant long-term savings [68,80]. Moreover, the return on investment
in AI technologies can be boosted by their ability to quickly adapt to changing market
conditions and new regulations [73].

---


### Page 12

Energies 2024, 17, 4501
12 of 22
4.1.3. Regulatory and Policy Issues
The lack of uniform and clear regulations regarding the use of AI in the energy
sector is a major challenge. Energy policies must evolve to support technological innovation while ensuring consumer protection and the integrity of the energy system [63,107].
Regulatory frameworks need to be flexible enough to accommodate rapid technological
changes, allowing the integration of new solutions without compromising grid security
and reliability [64,74]. Additionally, it is crucial to develop standards to ensure the interoperability and security of AI systems in the energy sector. This includes establishing
guidelines for the collection, storage, and use of data, as well as protecting consumer
privacy [69,88]. Energy policies must also address the ethical implications of automation
and AI-assisted decision-making, ensuring that the use of these technologies benefits all
sectors of society [65,108].
4.2. Integration of Renewable Energies
4.2.1. Intermittent Renewable Integration
The integration of intermittent renewable energy sources, such as solar and wind,
presents both a challenge and an opportunity for distributed energy systems. The variable
nature of these energy sources requires advanced management and control systems capable
of balancing supply and demand in real time [66,86]. AI can play a crucial role by improving
the accuracy of energy forecasts and optimizing resource scheduling, enabling more efficient
integration of these sources into the grid [70,82]. AI also facilitates the creation of microgrids
that can operate independently or in conjunction with the main grid. These microgrids
can enhance grid resilience and efficiency by effectively integrating intermittent renewable
energies [67,79]. Additionally, AI-based technologies can help manage energy storage,
optimizing the use of batteries and other storage systems to maximize the utilization of
renewable energies [75,96].
4.2.2. Demand Response Enhancement
Artificial intelligence has the potential to transform demand response mechanisms by
providing more accurate and efficient tools for managing energy consumption. AI algorithms can analyze consumption patterns and adjust energy supply in real-time, thereby
improving system efficiency and reducing the need for backup energy sources [26,92].
AI systems can also facilitate better communication and coordination between energy
providers and consumers, enabling faster and more effective responses to demand fluctuations [74,81]. By enhancing the system’s ability to respond to changes in demand, AI can
help reduce operational costs and improve grid stability, promoting a more efficient and
sustainable use of energy resources [68,83]. Table 4 highlights the innovative applications
of AI in energy systems and smart grids.
Table 4. Innovative AI applications in energy systems and smart grids.
Novel Idea
Description
Ref.
Potential Research Directions
AI-Enhanced Energy
Communities
Utilize AI and blockchain to empower
prosumers in energy trading and
management, enhancing efficiency and
participation in decentralized
energy markets.
[5,12,40]
Develop frameworks for secure and
efficient peer-to-peer energy trading
using AI and blockchain technologies,
focusing on scalability
and sustainability.
Adaptive AI for
Demand-Side
Management
Implement AI-based adaptive
algorithms to optimize demand
response, manage load, and improve
grid reliability.
[29,30]
Explore real-time adaptive AI
techniques for dynamic demand-side
management in smart grids, enhancing
consumer engagement and
grid resilience.

---


### Page 13

Energies 2024, 17, 4501
13 of 22
Table 4. Cont.
Novel Idea
Description
Ref.
Potential Research Directions
AI-Driven Microgrid
Resilience
Integrate AI with Io T for enhanced
microgrid management, focusing on
resilience and efficient
resource allocation.
[22,27,31]
Research AI-driven Io T solutions for
real-time DER management, focusing
on resilience in fluctuating
environments and grid stability.
Federated Learning in
Distributed Energy
Systems
Use federated learning to maintain data
privacy while optimizing distributed
energy resource management.
[5,29,40]
Investigate federated learning
applications for secure, decentralized
energy management, emphasizing data
privacy and collaborative optimization.
AI-Enabled Hybrid
Energy Systems
Employ AI algorithms to optimize the
integration and management of hybrid
renewable energy sources, improving
efficiency and reducing
carbon emissions.
[16,19,30]
Study AI’s role in enhancing hybrid
systems’ performance, focusing on
real-time optimization and
environmental impact assessment.
Stochastic AI Models for
Energy Forecasting
Apply deep learning and stochastic
models to improve forecasting accuracy
in variable renewable energy sources
and grid operations.
[25,31,39]
Develop advanced stochastic AI
models for precise energy forecasting
under variable conditions, considering
market dynamics and weather impacts.
AI-Optimized Smart
Buildings
Integrate AI with smart building
technologies to enhance energy
efficiency, demand response,
and sustainability.
[21,25,56]
Explore AI-driven strategies for
optimizing energy use and reducing
operational costs in smart buildings,
focusing on carbon neutrality and
occupant comfort.
4.3. Cybersecurity in AI Applications for Distributed Energy Systems
The cybersecurity of AI-enabled applications is crucial for their successful implementation and operation in distributed energy systems. As AI technologies become more
integrated into smart grids, a variety of cyber threats have emerged that can compromise
the integrity, availability, and confidentiality of data and systems. These threats include
false data injection attacks, denial of service (Do S) attacks, and load manipulation, all of
which can negatively affect the stability and efficiency of smart grids.
To mitigate these threats, several approaches have been developed to enhance cyber
resilience. For example, intrusion detection and prevention systems (IDPS) are used
as a secondary layer of defense to detect and prevent cyberattacks that might bypass
initial encryption and authorization mechanisms. These systems are effective in advanced
metering infrastructure, SCADA systems, and other critical components of the energy
system [103]. Additionally, multi-agent-based designs for System Integrity Protection
(SIP) have proven effective in enhancing situational awareness and self-adaptiveness of
systems, thereby improving cyber resilience against single points of failure induced by
cyberattacks [104].
Another innovative approach is the use of blockchain technology to enhance the
cyber resilience of microgrids. By utilizing smart contracts in a blockchain environment,
distributed secondary controls and self-healing functions can be secured against false data
injection attacks (FDIAs) in a zero-trust environment [105]. This approach has been shown
to be effective in test environments, maintaining comparable performance to conventional
approaches even under intense cyberattacks. Moreover, the implementation of a CyberResilient Economic Dispatch (CRED) offers a strategy to mitigate Load-Altering Attacks
(LAAs) by coordinating frequency droop controls in Inverter-Based Resources (IBRs) to
minimize the destabilizing effects of these attacks while optimizing operational costs [106].
This strategy considers the system’s frequency dynamics and provides a robust framework
for attack detection and mitigation. Then, the use of Software-Defined Networking (SDN) in
microgrid communication architecture allows for greater visibility, direct network control,
and programmability, significantly enhancing the resilience and security of microgrid

---


### Page 14

Energies 2024, 17, 4501
14 of 22
operations against various cyber threats [107]. This approach enables self-healing network
management and real-time network verification, strengthening the system’s ability to
withstand and recover from cyberattacks. These emerging strategies and technologies
underscore the importance of robust cybersecurity for the successful integration of AIenabled applications in distributed energy systems, ensuring their resilience and secure
operation in an increasingly interconnected and cyber-vulnerable environment [108].
4.4. Holistic Framework for AI Applications in Energy Systems
4.4.1. Overview of AI Applications across Power System Phases
The application of AI techniques in power systems can be comprehensively understood
through a holistic framework that spans the key phases of power generation, transmission,
and distribution. This framework provides a structured approach to analyze the impact
of AI at each stage, highlighting the specific roles these technologies play in optimizing
operations, improving efficiency, and enhancing system resilience:
•
Power generation: AI techniques are extensively used in optimizing power generation,
particularly from renewable sources such as solar and wind energy. Machine learning
algorithms, for instance, have been developed to predict solar irradiance and wind
speeds with greater accuracy, thus allowing for more precise energy output forecasts
and better scheduling of dispatchable resources [10,108]. Moreover, AI is applied to
enhance the operational efficiency of power plants by utilizing predictive maintenance
algorithms that can anticipate equipment failures before they occur. This reduces
downtime and maintenance costs while ensuring continuous power generation [8]. Research has shown that AI-based predictive maintenance strategies extend the lifespan
of grid components by anticipating failures and scheduling proactive maintenance.
•
Power transmission: In the transmission phase, AI technologies are pivotal in optimizing the flow of electricity across vast networks, ensuring stability and reliability.
Deep learning techniques are employed for real-time anomaly detection and fault
diagnosis in transmission lines, which helps in early identification and rectification of
potential issues [15]. AI-driven optimization algorithms are also used to dynamically
adjust power flows and maintain voltage levels within optimal ranges, preventing
grid failures and enhancing overall grid resilience [14]. A multi-agent system can be
implemented to enhance situational awareness and provide adaptive responses to
unexpected grid events, further improving transmission reliability and security [18].
•
Power distribution: AI’s role in the distribution phase is critical for managing the
complexity of modern electrical grids, especially with the increasing penetration of
distributed energy resources (DERs) such as solar panels and wind turbines. AI
techniques, such as reinforcement learning, optimize load management by predicting
consumption patterns and adjusting supply in real-time to match demand [7]. This not
only enhances demand response strategies but also facilitates the seamless integration
of DERs into the grid, ensuring stability and minimizing disruptions [3]. Furthermore,
AI-based predictive analytics are used for voltage regulation and to reduce energy
losses during distribution, which improves the efficiency and reliability of energy
delivery to end-users [9].
4.4.2. Research Gaps, Challenges, and Future Perspectives
Within this framework, several research gaps, challenges, and future perspectives emerge:
•
Research gaps: While AI has significantly advanced power systems, several research
gaps still exist. One notable gap is the need for more robust models that can handle
the variability and uncertainty of renewable energy sources. Current AI models are
often limited in their ability to predict extreme weather events or sudden changes
in generation, which can impact grid stability [5]. Additionally, there is a lack of
comprehensive solutions for the interoperability of diverse energy resources and
systems, which is crucial for the seamless integration of renewable energies and the
overall efficiency of the power grid [13]. Further research is needed to develop AI

---


### Page 15

Energies 2024, 17, 4501
15 of 22
algorithms capable of managing the complex interactions between various energy
sources and storage systems.
•
Challenges: The deployment of AI in power systems faces several challenges. Technically, there is a need for advanced infrastructure, such as high-speed communication
networks and powerful computational resources, to support AI applications [4]. Cybersecurity remains a significant concern, as the integration of AI and digital technologies
exposes power systems to potential cyber threats, including data breaches and cyberattacks [12]. Developing robust cybersecurity measures, such as blockchain-enabled
frameworks, is essential to protect these systems and ensure their reliable operation.
Additionally, regulatory and policy challenges need to be addressed to create standardized frameworks that govern the use of AI in power systems, ensuring data privacy,
security, and ethical use [11].
•
Future perspectives: Looking forward, the future of AI in power systems lies in the
development of more adaptive and scalable AI models that can manage the dynamic
nature of energy systems. Integrating AI with emerging technologies like blockchain
can enhance security and transparency, while Io T can provide real-time data collection
and analytics, further improving system resilience and efficiency [16]. There is also
a need for interdisciplinary research that combines expertise from energy, computer
science, and regulatory fields to address the multifaceted challenges of AI integration
in power systems. Exploring these future directions will help in building smarter,
more efficient, and resilient power systems that can adapt to the evolving demands of
the modern energy landscape.
4.5. Future Trends in AI Impact on the Planning and Operation of Distributed Energy Systems in
Smart Grids
As the landscape of distributed energy systems continues to evolve, AI is poised
to play an increasingly pivotal role in the planning and operation of smart grids. The
integration of AI technologies offers numerous opportunities for enhancing efficiency,
reliability, and sustainability. Here are some of the key future trends we anticipate:
4.5.1. Increased Integration of Advanced AI Techniques:
Advanced AI techniques such as Generative Adversarial Networks (GANs) and Graph
Neural Networks (GNNs) are expected to see wider adoption in smart grids. GANs could
be used to simulate various scenarios of energy consumption and generation, providing
utilities with robust tools for demand forecasting and anomaly detection. Meanwhile,
GNNs are well-suited for optimizing grid operations by modeling the complex interdependencies within a network, thereby improving fault detection, energy distribution, and
overall grid management.
4.5.2. Enhanced Cybersecurity Measures
As smart grids become more interconnected and dependent on digital infrastructure,
the need for advanced cybersecurity measures will grow. AI will play a critical role in
developing predictive and adaptive security frameworks that can detect and respond to
cyber threats in real-time. Techniques such as deep reinforcement learning and adversarial training can be employed to create more resilient systems capable of withstanding
sophisticated attacks.
4.5.3. Autonomous and Decentralized Energy Management
The future of smart grids will likely include a shift towards more autonomous and
decentralized energy management systems. AI will enable distributed energy resources
(DERs) to operate independently, making real-time decisions about energy generation,
storage, and consumption based on current grid conditions and market signals. This
trend will be driven by the development of more sophisticated multi-agent systems and

---


### Page 16

Energies 2024, 17, 4501
16 of 22
AI-powered optimization algorithms that can coordinate a vast array of DERs to maintain
grid stability and efficiency.
Integration with Emerging Technologies
The convergence of AI with other emerging technologies, such as blockchain and
the Internet of Things (Io T), will further transform smart grids. Blockchain can provide
a secure and transparent platform for peer-to-peer energy trading, while Io T devices will
facilitate real-time data collection and analysis. AI algorithms will be crucial for processing
this data and making intelligent decisions that optimize grid operations and enhance
service reliability.
Focus on Sustainable and Resilient Energy Systems
As the world moves towards more sustainable energy practices, AI will play a crucial
role in ensuring that smart grids can efficiently integrate renewable energy sources. AI
techniques will be used to predict renewable energy output, optimize storage solutions,
and manage the variability associated with solar and wind power. Additionally, AI will
help develop more resilient energy systems that can quickly recover from disruptions and
adapt to changing environmental conditions.
5. Discussions
The integration of AI into smart grids and distributed energy systems presents significant opportunities to enhance efficiency, reliability, and sustainability. This paper has
highlighted several transformative AI applications, from energy management optimization
to advanced demand response strategies. These applications demonstrate AI’s potential
to address the complexities associated with modern energy infrastructures. One of the
most significant contributions of AI is its ability to improve demand forecasting and energy
flow optimization. By leveraging machine learning models and neural networks, AI can
predict energy consumption patterns with high accuracy, enabling utilities to better manage
peak loads and integrate renewable energy sources. This capability is particularly crucial
in regions with high penetration of intermittent renewable energies such as solar and
wind [2,7,16,25,27]. AI-driven solutions also enhance the coordination and integration of
DERs, such as solar panels and wind turbines, within the energy grid. Techniques like
RL and multi-agent systems enable more efficient management of DERs, optimizing their
output and ensuring stability in the energy supply [4,9,13,22]. VPPs, facilitated by AI,
aggregate these resources to enhance energy trading and resource distribution, further
strengthening grid resilience [21,26].
Despite these advancements, several challenges must be addressed to fully realize AI’s
potential in energy systems. Technical barriers, including data privacy and cybersecurity,
remain significant concerns as AI systems process vast amounts of sensitive data [35,36,66].
Developing robust cybersecurity measures is essential to protect the integrity of these
systems and maintain public trust. Economic considerations also play a critical role in AI
adoption. While AI technologies can lead to long-term cost savings through enhanced
efficiency and reduced energy losses, the initial investment required for infrastructure
and training can be prohibitive for many organizations [39–41]. Therefore, conducting
comprehensive cost-benefit analyses and exploring funding opportunities are crucial steps
in facilitating wider adoption. Regulatory frameworks must evolve to keep pace with
technological advancements. Clear and flexible regulations that address data privacy,
security, and ethical implications of AI in energy systems are necessary to ensure that AI
solutions align with societal values and consumer interests [41,42,67]. Policymakers should
work closely with industry stakeholders to create guidelines that promote innovation while
safeguarding the public. Therefore, AI has the potential to significantly transform the
planning and operation of distributed energy systems within smart grids. By addressing the technical, economic, and regulatory challenges, stakeholders can unlock the full
benefits of AI, leading to more resilient, efficient, and sustainable energy infrastructures.

---


### Page 17

Energies 2024, 17, 4501
17 of 22
Future research should focus on developing adaptive AI algorithms, enhancing system
interoperability, and fostering collaboration between the public and private sectors to drive
innovation in this rapidly evolving field [47,48,51].
Figure 2 shows the predicted impact levels of various AI techniques—machine learning, neural networks, optimization algorithms, RL, and AI with Io T and blockchain on
key smart grid functions. Impact areas include energy forecasting, load management,
renewable integration, predictive maintenance, and grid stability. The heatmap highlights
the high impact of machine learning and neural networks on energy forecasting and grid
stability and the significant potential for AI with Io T and blockchain in renewable integration. This visualization provides a clear overview of where AI can most effectively enhance
smart grid operations.
Figure 2. Future impact areas of AI in smart grids.
6. Conclusions
This paper presents a comprehensive review of the transformative impact of artificial intelligence on the planning and operation of distributed energy systems within
smart grids. By examining the integration of cutting-edge AI techniques such as machine
learning, neural networks, and optimization algorithms, the study highlights how these
technologies enhance the efficiency, reliability, and sustainability of modern energy infrastructures. Throughout the analysis, several key areas were explored, including AI-driven
energy management systems, advanced demand forecasting methods, and the seamless
integration of DERs like solar panels and wind turbines. The review reveals AI’s ability
to address complex challenges in energy systems by optimizing energy flow, improving
grid resilience, and facilitating the transition towards a more decentralized and flexible
energy infrastructure.
One of the primary findings is that AI significantly improves demand forecasting accuracy, allowing utilities to predict energy consumption patterns and manage peak loads more
effectively. This capability is crucial for integrating intermittent renewable energy sources,
ensuring stable energy supply, and reducing reliance on conventional power generation
methods. AI-driven energy management systems enable better resource allocation and
energy distribution, ultimately leading to increased efficiency and reduced environmental
impact. The study also underscores the importance of AI in optimizing the coordination and control of DERs, enhancing grid flexibility, and supporting the development of
VPPs. These AI-enabled solutions allow for more efficient energy trading and resource
distribution, strengthening grid resilience and promoting sustainable energy practices.

---


### Page 18

Energies 2024, 17, 4501
18 of 22
Despite the promising potential of AI in transforming energy systems, several challenges must be addressed to realize its full benefits. Technical barriers, such as data privacy
and cybersecurity, remain significant concerns as AI systems process large volumes of
sensitive information. Robust cybersecurity measures and data protection frameworks are
essential to maintain system integrity and public trust. Economic considerations also play
a critical role in AI adoption. While AI technologies can lead to long-term cost savings
through improved efficiency, the initial investment required for infrastructure, training,
and deployment can be substantial. Conducting comprehensive cost-benefit analyses
and exploring funding opportunities are crucial to facilitating wider adoption, especially
in regions with limited resources. Furthermore, regulatory frameworks must evolve to
keep pace with technological advancements. Clear and flexible regulations addressing
data privacy, security, and ethical implications are necessary to ensure AI solutions align
with societal values and consumer interests. Collaboration between policymakers, industry stakeholders, and research institutions is vital to creating guidelines that promote
innovation while safeguarding the public.
Finally, the future of AI in energy systems hinges on developing adaptive algorithms,
enhancing interoperability, and addressing cybersecurity and economic challenges. Research should also focus on cost-effective deployment strategies and evolving regulatory
frameworks. By pursuing these directions, stakeholders can unlock AI’s full potential, leading to more resilient, efficient, and sustainable energy systems that address the demands of
modern infrastructures.
Author Contributions: Conceptualization, P.A. and F.J.; data curation, P.A. and F.J.; formal analysis,
P.A. and F.J.; funding acquisition, P.A. and F.J.; methodology, P.A. and F.J.; project administration, F.J.;
resources, P.A. and F.J.; software, P.A.; supervision, F.J.; validation, P.A., visualization, P.A. and F.J;
writing—original draft, P.A.; writing—review and editing, P.A. and F.J. All authors have read and
agreed to the published version of the manuscript.
Funding: This research received no external funding.
Data Availability Statement: Data will be made available on request.
Acknowledgments: The authors thank the Faculty of Engineering, Universidad de Cuenca, Ecuador,
for granting access to the Micro-Grid Laboratory and providing the technical support necessary to
carry out the experiments described in this article.
Conflicts of Interest: The authors declare no conflicts of interest.
References
1.
Szczepaniuk, H.; Szczepaniuk, E.K. Applications of Artificial Intelligence Algorithms in the Energy Sector. Energies 2023, 16, 347.
[Cross Ref]
2.
Kumar, A.; Alaraj, M.; Rizwan, M.; Nangia, U. Novel AI Based Energy Management System for Smart Grid With RES Integration.
IEEE Access 2021, 9, 162530–162542. [Cross Ref]
3.
Ibrahim, M.S.; Dong, W.; Yang, Q. Machine learning driven smart electric power systems: Current trends and new perspectives.
Appl. Energy 2020, 272, 115237. [Cross Ref]
4.
Ali, S.S.; Choi, B.J. State-of-the-Art Artificial Intelligence Techniques for Distributed Smart Grids: A Review. Electronics 2020,
9, 1030. [Cross Ref]
5.
Hua, W.; Chen, Y.; Qadrdan, M.; Jiang, J.; Sun, H.; Wu, J. Applications of blockchain and artificial intelligence technologies for
enabling prosumers in smart grids: A review. Renew. Sustain. Energy Rev. 2022, 161, 112308. [Cross Ref]
6.
Singh, S.; Singh, S. Advancements and Challenges in Integrating Renewable Energy Sources Into Distribution Grid Systems: A
Comprehensive Review. J. Energy Resour. Technol. 2024, 146, 090801. [Cross Ref]
7.
Kumar, M.; Pal, N. Machine Learning-based Electric Load Forecasting for Peak Demand Control in Smart Grid. CMC: Comput.
Mater. Continua 2023, 74, 4785–4799. [Cross Ref]
8.
Durairaj, D.; Wroblewski, L.; Sheela, A.; Hariharasudan, A.; Urbanski, M. Random forest based power sustainability and cost
optimization in smart grid. Prod. Eng. Arch. 2022, 28, 82–92. [Cross Ref]
9.
Nair, D.R.; Nair, M.G.; Thakur, T. A Smart Microgrid System with Artificial Intelligence for Power-Sharing and Power Quality
Improvement. Energies 2022, 15, 5409. [Cross Ref]
10.
Rojek, I.; Mrozi´nski, A.; Kotlarz, P.; Macko, M.; Mikołajewski, D.; Rojek, I.; Mrozi´nski, A.; Kotlarz, P.; Macko, M.; Mikołajewski, D.
AI-Based Computational Model in Sustainable Transformation of Energy Markets. Energies 2023, 16, 8059. [Cross Ref]

---


### Page 19

Energies 2024, 17, 4501
19 of 22
11.
Ferrández-Pastor, F.J.; García-Chamizo, J.M.; Gomez-Trillo, S.; Valdivieso-Sarabia, R.; Nieto-Hidalgo, M. Smart Management
Consumption in Renewable Energy Fed Ecosystems. Sensors 2019, 19, 2967. [Cross Ref]
12.
Beniwal, R.K.; Saini, M.K.; Nayyar, A.; Qureshi, B.; Aggarwal, A. A Critical Analysis of Methodologies for Detection and
Classification of Power Quality Events in Smart Grid. IEEE Access 2021, 9, 83507–83534. [Cross Ref]
13.
Seema, P.N.; Nair, M.G. The key modules involved in the evolution of an effective instrumentation and communication network
in smart grids: A review. Smart Sci. 2023, 11, 519–537. [Cross Ref]
14.
Velasquez, W.; Moreira-Moreira, G.Z.; Alvarez-Alvarado, M.S. Smart Grids Empowered by Software-Defined Network: A
Comprehensive Review of Advancements and Challenges. IEEE Access 2024, 12, 63400–63416. [Cross Ref]
15.
Perger, A.V.; Gamper, P.; Witzmann, R. Behavior Trees for Smart Grid Control. IFAC-Papers On Line 2022, 55, 122–127. [Cross Ref]
16.
Chandrasekaran, K.; Selvaraj, J.; Amaladoss, C.R.; Veerapan, L. Hybrid renewable energy based smart grid system for reactive
power management and voltage profile enhancement using artificial neural network. Energy Sources Part A Recover. Utiliz. Environ.
Effects. 2021, 43, 2419–2442. [Cross Ref]
17.
Bin Kamilin, M.H.; Yamaguchi, S. Resilient Electricity Load Forecasting Network with Collective Intelligence Predictor for Smart
Cities. Electronics 2024, 13, 718. [Cross Ref]
18.
Soares, J.; Pinto, T.; Lezama, F.; Morais, H. Survey on Complex Optimization and Simulation for the New Power Systems
Paradigm. Complexity 2018, 32, 2340628. [Cross Ref]
19.
Colak, M.; Balci, S. Photovoltaic System Parameter Estimation Using Marine Predators Optimization Algorithm Based on
Multilayer Perceptron. Electr. Power Comp. Syst. 2022, 50, 1087–1099. [Cross Ref]
20.
Wesley, B.J.; Babu, G.S.; Kumar, P.S. Design and control of LSTM-ANN controllers for an efficient energy management system in a
smart grid based on hybrid renewable energy sources. Eng. Res. Express 2024, 6, 015074. [Cross Ref]
21.
Khayyat, M.M.; Sami, B. Energy Community Management Based on Artificial Intelligence for the Implementation of Renewable
Energy Systems in Smart Homes. Electronics 2024, 13, 380. [Cross Ref]
22.
Garcia Medina, M.S.; Aguilar, J.; Rodriguez-Moreno, M.D. A Bioinspired Emergent Control for Smart Grids. IEEE Access 2023, 11,
7503–7520. [Cross Ref]
23.
Anthony Jnr, B. Decentralized AIo T based intelligence for sustainable energy prosumption in local energy communities: A
citizen-centric prosumer approach. Cities 2024, 152, 105198. [Cross Ref]
24.
Rimal, B.P.; Kong, C.; Poudel, B.; Wang, Y.; Shahi, P. Smart Electric Vehicle Charging in the Era of Internet of Vehicles, Emerging
Trends, and Open Issues. Energies 2022, 15, 1908. [Cross Ref]
25.
Ahmad, T.; Madonski, R.; Zhang, D.; Huang, C.; Mujeeb, A. Data-driven probabilistic machine learning in sustainable smart
energy/smart energy systems: Key developments, challenges, and future research opportunities in the context of smart grid
paradigm. Renew. Sustain. Energy Rev. 2022, 160, 112128. [Cross Ref]
26.
Khalid, M. Energy 4.0: AI-enabled digital transformation for sustainable power networks. Comput. Ind. Eng. 2024, 193, 110253.
[Cross Ref]
27.
Payne, E.K.; Qian, W.; Lu, S.; Wu, L. Technical risk synthesis and mitigation strategies of distributed energy resources integration
with wireless sensor networks and internet of things—Review. J. Eng. 2019, 18, 4830–4835. [Cross Ref]
28.
Georgilakis, P.S. Review of Computational Intelligence Methods for Local Energy Markets at the Power Distribution Level to
Facilitate the Integration of Distributed Energy Resources: State-of-the-art and Future Research. Energies 2020, 13, 186. [Cross Ref]
29.
Ma, H.; Zhang, H.; Tian, D.; Yue, D.; Hancke, G.P. Optimal demand response based dynamic pricing strategy via Multi-Agent
Federated Twin Delayed Deep Deterministic policy gradient algorithm. Eng. Appl. Artif. Intell. 2024, 133, 108012. [Cross Ref]
30.
Banales, S. The enabling impact of digital technologies on distributed energy resources integration. J. Renew. Sustain. Energy.
2020, 12, 045301. [Cross Ref]
31.
Cicceri, G.; Tricomi, G.; D’Agati, L.; Longo, F.; Merlino, G.; Puliafito, A. A Deep Learning-Driven Self-Conscious Distributed
Cyber-Physical System for Renewable Energy Communities. Sensors 2023, 23, 4549. [Cross Ref] [Pub Med]
32.
Bindi, M.; Piccirilli, M.C.; Luchetta, A.; Grasso, F. A Comprehensive Review of Fault Diagnosis and Prognosis Techniques in High
Voltage and Medium Voltage Electrical Power Lines. Energies 2023, 16, 7317. [Cross Ref]
33.
Ghasemi, A.; Shojaeighadikolaei, A.; Hashemi, M. Combating Uncertainties in Smart Grid Decision Networks: Multiagent
Reinforcement Learning With Imperfect State Information. IEEE Internet Things J. 2024, 11, 23985–23997. [Cross Ref]
34.
Boato, B.; Sueldo, C.S.; Avila, L.; de Paula, M. An improved Soft Actor-Critic strategy for optimal energy management. IEEE Lat.
Am. Trans. 2023, 21, 958–965. [Cross Ref]
35.
Pandiyan, P.; Saravanan, S.; Kannadasan, R.; Krishnaveni, S.; Alsharif, M.H.; Kim, M.-K. A comprehensive review of advancements
in green Io T for smart grids: Paving the path to sustainability. Energy Rep. 2024, 11, 5504–5531. [Cross Ref]
36.
Karanfil, M.; Rebbah, D.E.; Debbabi, M.; Kassouf, M.; Ghafouri, M.; Youssef, E.-N.S.; Hanna, A. Detection of Microgrid
Cyberattacks Using Network and System Management. IEEE Trans. Smart Grid 2023, 14, 2390–2405. [Cross Ref]
37.
Xi, L.; Chen, J.; Huang, Y.; Xu, Y.; Liu, L.; Zhou, Y.; Li, Y. Smart generation control based on multi-agent reinforcement learning
with the idea of the time tunnel. Energy 2018, 153, 977–987. [Cross Ref]
38.
Ma, R.; Yi, Z.; Xiang, Y.; Shi, D.; Xu, C.; Wu, H. A Blockchain-Enabled Demand Management and Control Framework Driven by
Deep Reinforcement Learning. IEEE Trans. Ind. Electron 2023, 70, 430–440. [Cross Ref]
39.
Abdullah, H.M.; Gastli, A.; Ben-Brahim, L. Reinforcement Learning Based EV Charging Management Systems-A Review. IEEE
Access 2021, 9, 41506–41531. [Cross Ref]

---


### Page 20

Energies 2024, 17, 4501
20 of 22
40.
Taik, A.; Nour, B.; Cherkaoui, S. Empowering prosumer communities in smart grid with wireless communications and federated
edge learning. IEEE Wireless Commun. 2021, 28, 26–33. [Cross Ref]
41.
Afzali, P.; Yeganeh, A.; Derakhshan, F. A novel socio-economic-environmental model to maximize prosumer satisfaction in smart
residential complexes. Energy Build. 2024, 308, 114023. [Cross Ref]
42.
Rosato, A.; Panella, M.; Araneo, R.; Andreotti, A. A Neural Network Based Prediction System of Distributed Generation for the
Management of Microgrids. IEEE Trans. Ind. Appl. 2019, 55, 7092–7102. [Cross Ref]
43.
Succetti, F.; Rosato, A.; Araneo, R.; Panella, M. Deep Neural Networks for Multivariate Prediction of Photovoltaic Power Time
Series. IEEE Access 2020, 8, 211490–211505. [Cross Ref]
44.
Aleem, S.A.; Hussain, S.M.S.; Ustun, T.S. A Review of Strategies to Increase PV Penetration Level in Smart Grids. Energies 2020,
13, 636. [Cross Ref]
45.
Nabavi, S.A.; Motlagh, N.H.; Zaidan, M.A.; Aslani, A.; Zakeri, B. Deep Learning in Energy Modeling: Application in Smart
Buildings With Distributed Energy Generation. IEEE Access 2021, 9, 125439–125461. [Cross Ref]
46.
Okampo, E.J.; Nwulu, N.; Bokoro, P.N. Optimal Placement and Operation of FACTS Technologies in a Cyber-Physical Power
System: Critical Review and Future Outlook. Sustainability 2022, 14, 7707. [Cross Ref]
47.
Ucer, E.; Kisacikoglu, M.C.; Yuksel, M. Decentralized Additive Increase and Multiplicative Decrease-Based Electric Vehicle
Charging. IEEE Syst. J. 2021, 15, 4272–4280. [Cross Ref]
48.
Zhang, Y.; Krishnan, V.V.G.; Pi, J.; Kaur, K.; Srivastava, A.; Hahn, A.; Suresh, S. Cyber Physical Security Analytics for Transactive
Energy Systems. IEEE Trans. Smart Grid 2020, 11, 931–941. [Cross Ref]
49.
Shaqour, A.; Hagishima, A. Systematic Review on Deep Reinforcement Learning-Based Energy Management for Different
Building Types. Energies 2022, 15, 8663. [Cross Ref]
50.
Rabie, A.H.; Ali, S.H.; Saleh, A.I.; Ali, H.A. A new outlier rejection methodology for supporting load forecasting in smart grids
based on big data. Cluster Comput. 2020, 23, 509–535. [Cross Ref]
51.
Adnan, M.; Ghadi, Y.; Ahmed, I.; Ali, M. Transmission Network Planning in Super Smart Grids: A Survey. IEEE Access 2023, 11,
77163–77227. [Cross Ref]
52.
Zhou, Y. A regression learner-based approach for battery cycling ageing predictiondadvances in energy management strategy
and techno- economic analysis. Energy 2022, 256, 124668. [Cross Ref]
53.
Tiwari, D.; Zideh, M.J.; Talreja, V.; Verma, V.; Solanki, S.K.; Solanki, J. Power Flow Analysis Using Deep Neural Networks in
Three-Phase Unbalanced Smart Distribution Grids. IEEE Access 2024, 12, 29959–29970. [Cross Ref]
54.
Al-Gabalawy, M. Reinforcement learning for the optimization of electric vehicle virtual power plants. Int. Trans. Electr. Energy
Syst. 2021, 31, 12951. [Cross Ref]
55.
Yap, K.Y.; Chin, H.H.; Klemes, J.J. Future outlook on 6G technology for renewable energy sources (RES). Renew. Sustain. Energy
Rev. 2022, 167, 112722. [Cross Ref]
56.
Qiu, D.; Xue, J.; Zhang, T.; Wang, J.; Sun, M. Federated reinforcement learning for smart building joint peer-to-peer energy and
carbon allowance trading. Appl. Energy 2023, 333, 120526. [Cross Ref]
57.
Dabbaghjamanesh, M.; Kavousi-Fard, A.; Zhang, J. Stochastic Modeling and Integration of Plug-In Hybrid Electric Vehicles in
Reconfigurable Microgrids With Deep Learning-Based Forecasting. IEEE Trans. Intell. Transp. Syst. 2021, 22, 4394–4403. [Cross Ref]
58.
Alhussein, M.; Haider, S.I.; Aurangzeb, K. Microgrid-Level Energy Management Approach Based on Short-Term Forecasting of
Wind Speed and Solar Irradiance. Energies 2019, 12, 1487. [Cross Ref]
59.
Yavuz, M.; Kivanc, O.C. Optimization of a Cluster-Based Energy Management System Using Deep Reinforcement Learning
Without Affecting Prosumer Comfort: V2X Technologies and Peer-to-Peer Energy Trading. IEEE Access 2024, 12, 31551–31575.
[Cross Ref]
60.
Oyucu, S.; Polat, O.; Turkoglu, M.; Polat, H.; Aksoz, A.; Agdas, M.T. Ensemble Learning Framework for DDo S Detection in
SDN-Based SCADA Systems. Sensors 2024, 24, 155. [Cross Ref]
61.
Mohamed, M.A.E.; Mahmoud, A.M.; Saied, E.M.M.; Hadi, H.A. Hybrid cheetah particle swarm optimization based optimal
hierarchical control of multiple microgrids. Sci. Rep. 2024, 14, 9313. [Cross Ref] [Pub Med]
62.
Yaprakdal, F.; Yilmaz, M.B.; Baysal, M.; Anvari-Moghaddam, A. A Deep Neural Network-Assisted Approach to Enhance
Short-Term Optimal Operational Scheduling of a Microgrid. Sustainability 2020, 12, 1653. [Cross Ref]
63.
Sinha, A.; Singh, S.; Verma, H.K. AI-Driven Task Scheduling Strategy with Blockchain Integration for Edge Computing. J. Grid
Comput. 2024, 22, 9743. [Cross Ref]
64.
Alsharif, M.H.; Jahid, A.; Kannadasan, R.; Kim, M.-K. Unleashing the potential of sixth generation (6G) wireless networks in
smart energy grid management: A comprehensive review. Energy Rep. 2024, 11, 1376–1398. [Cross Ref]
65.
Asif, M.; Naeem, G.; Khalid, M. Digitalization for sustainable buildings: Technologies, applications, potential, and challenges. J.
Cleaner Prod. 2024, 450, 141814. [Cross Ref]
66.
Alrubayyi, H.; Alshareef, M.S.; Nadeem, Z.; Abdelmoniem, A.M.; Jaber, M. Security Threats and Promising Solutions Arising
from the Intersection of AI and Io T: A Study of Io MT and Io ET Applications. Futur. Internet 2024, 16, 85. [Cross Ref]
67.
Wu, H.; Wang, X.; Liao, H.; Jiao, X.; Liu, Y.; Shu, X.; Wang, J.; Rao, Y. Signal Processing in Smart Fiber-Optic Distributed Acoustic
Sensor. Acta Opt. Sin. 2024, 44, 231384. [Cross Ref]
68.
Xiong, Y.; Liu, Y.; Yang, J.; Wang, Y.; Xu, N.; Wang, Z.L.; Sun, Q. Machine learning enhanced rigiflex pillar-membrane triboelectric
nanogenerator for universal stereoscopic recognition. Nano Energy 2024, 129, 109956. [Cross Ref]

---


### Page 21

Energies 2024, 17, 4501
21 of 22
69.
Quy, V.K.; Nguyen, D.C.; Van Anh, D.; Quy, N.M. Federated learning for green and sustainable 6G IIo T applications. Internet
Things 2024, 25, 101061. [Cross Ref]
70.
Wang, Q.; Yin, Y.; Chen, Y.; Liu, Y. Carbon peak management strategies for achieving net-zero emissions in smart buildings:
Advances and modeling in digital twin. Sustainable Energy Technol. Assess. 2024, 64, 103661. [Cross Ref]
71.
Udayaprasad, P.K.; Shreyas, J.; Srinidhi, N.N.; Kumar, S.M.D.; Dayananda, P.; Askar, S.S.; Abouhawwash, M. Energy Efficient
Optimized Routing Technique With Distributed SDN-AI to Large Scale I-Io T Networks. IEEE Access 2024, 12, 2742–2759.
[Cross Ref]
72.
Zeng, L.; Ye, S.; Chen, X.; Yang, Y. Implementation of Big Ai Models for Wireless Networks with Collaborative Edge Computing.
IEEE Wireless Commun. 2024, 31, 50–58. [Cross Ref]
73.
Somantri, A.; Surendro, K. Greenhouse Gas Emission Reduction Architecture in Computer Science: A Systematic Review. IEEE
Access 2024, 12, 36239–36256. [Cross Ref]
74.
Gou, H.; Zhang, G.; Medeiros, E.P.; Jagatheesaperumal, S.K.; de Albuquerque, V.H.C. A Cognitive Medical Decision Support
System for Io T-Based Human-Computer Interface in Pervasive Computing Environment. Cogn. Comput. 2024, 16, 2471–2486.
[Cross Ref]
75.
Rajora, G.L.; Sanz-Bobi, M.A.; Tjernberg, L.B.; Urrea Cabus, J.E. A review of asset management using artificial intelligence-based
machine learning models: Applications for the electric power and energy system. IET Gener. Transm. Distrib. 2024, 18, 2155–2170.
[Cross Ref]
76.
Cairone, S.; Hasan, S.W.; Choo, K.-H.; Lekkas, D.F.; Fortunato, L.; Zorpas, A.A.; Korshin, G.; Zarra, T.; Belgiorno, V.; Naddeo, V.
Revolutionizing wastewater treatment toward circular economy and carbon neutrality goals: Pioneering sustainable and efficient
solutions for automation and advanced process control with smart and cutting-edge technologies. J. Water Process Eng. 2024, 63,
105486. [Cross Ref]
77.
Wang, X.; Guo, Y.; Gao, Y. Unmanned Autonomous Intelligent System in 6G Non-Terrestrial Network. Information 2024, 15, 38.
[Cross Ref]
78.
Huang, Y.; Li, M.; Yu, F.R.; Si, P.; Zhang, H.; Qiao, J. Resources Scheduling for Ambient Backscatter Communication-Based
Intelligent IIo T: A Collective Deep Reinforcement Learning Method. IEEE Trans. Cogn. Commun. Netw. 2024, 10, 634–648.
[Cross Ref]
79.
Diefenthaler, M.; Fanelli, C.; Gerlach, L.O.; Guan, W.; Horn, T.; Jentsch, A.; Lin, M.; Nagai, K.; Nayak, H.; Pecar, C.; et al.
AI-assisted detector design for the EIC (AID(2)E). J. Instrum. 2024, 19, 07001. [Cross Ref]
80.
Luo, T.; Wong, W.-F.; Goh, R.S.M.; Do, A.T.; Chen, Z.; Li, H.; Jiang, W.; Yau, W. Achieving Green AI with Energy-Efficient Deep
Learning Using Neuromorphic Computing. Commun. ACM 2023, 66, 52–57. [Cross Ref]
81.
Zhang, H.; Fang, B.; He, P.; Gao, W. The asymmetric impacts of artificial intelligence and oil shocks on clean energy industries by
considering COVID-19. Energy 2024, 291, 130197. [Cross Ref]
82.
Onile, A.E.; Petlenkov, E.; Levron, Y.; Belikov, J. Smartgrid-based hybrid digital twins framework for demand side recommendation
service provision in distributed power systems. Future Gener. Comput. Syst. 2024, 156, 142–156. [Cross Ref]
83.
Du, J.; Lin, T.; Jiang, C.; Yang, Q.; Bader, C.F.; Han, Z. Distributed Foundation Models for Multi-Modal Learning in 6g Wireless
Networks. IEEE Wireless Commun. 2024, 31, 20–30. [Cross Ref]
84.
Jouini, O.; Sethom, K.; Namoun, A.; Aljohani, N.; Alanazi, M.H.; Alanazi, M.N. A Survey of Machine Learning in Edge Computing:
Techniques, Frameworks, Applications, Issues, and Research Directions. Technologies 2024, 12, 81. [Cross Ref]
85.
Mwangi, A.; Sahay, R.; Fumagalli, E.; Gryning, M.; Gibescu, M. Towards a Software-Defined Industrial Io T-Edge Network for
Next-Generation Offshore Wind Farms: State of the Art, Resilience, and Self-X Network and Service Management. Energies 2024,
17, 2897. [Cross Ref]
86.
Naseh, D.; Shinde, S.S.; Tarchi, D. Network Sliced Distributed Learning-as-a-Service for Internet of Vehicles Applications in 6G
Non-Terrestrial Network Scenarios. J. Sens. Actuator Netw. 2024, 13, 14. [Cross Ref]
87.
Lin, Y.-H.; Ciou, J.-C. A privacy-preserving distributed energy management framework based on vertical federated learning-based
smart data cleaning for smart home electricity data. Internet Things 2024, 26, 101222. [Cross Ref]
88.
Sun, Q.; Li, N.; I, C.-L.; Huang, J.; Xu, X.; Xie, Y. Intelligent RAN Automation for 5G and Beyond. IEEE Wireless Commun. 2024, 31,
94–102. [Cross Ref]
89.
Rajesh, M.; Ramachandran, S.; Vengatesan, K.; Dhanabalan, S.S.; Nataraj, S.K. Federated Learning for Personalized Recommendation in Securing Power Traces in Smart Grid Systems. IEEE Trans. Consum. Electron. 2024, 70, 88–95. [Cross Ref]
90.
Rani, S.; Jining, D.; Shoukat, K.; Shoukat, M.U.; Nawaz, S.A. A Human-Machine Interaction Mechanism: Additive Manufacturing
for Industry 5.0-Design and Management. Sustainability 2024, 16, 4158. [Cross Ref]
91.
Aslanpour, M.S.; Toosi, A.N.; Cheema, M.A.; Chhetri, M.B.; Salehi, M.A. Load balancing for heterogeneous serverless edge
computing: A performance-driven and empirical approach. Future Gener. Comput. Syst. 2024, 154, 266–280. [Cross Ref]
92.
Zhang, X.; Wu, Z.; Sun, Q.; Gu, W.; Zheng, S.; Zhao, J. Application and progress of artificial intelligence technology in the field of
distribution network voltage Control:A review. Renew. Sustain. Energy Rev. 2024, 192, 114282. [Cross Ref]
93.
Zhang, X.; Zhang, Z.; Liu, Y.; Xu, Z.; Qu, X. A review of machine learning approaches for electric vehicle energy consumption
modelling in urban transportation. Renew. Energy 2024, 234, 121243. [Cross Ref]
94.
Cheng, F.; Liu, H. Multi-step electric vehicles charging loads forecasting: An autoformer variant with feature extraction, frequency
enhancement, and error correction blocks. Appl. Energy 2024, 376, 124308. [Cross Ref]

---


### Page 22

Energies 2024, 17, 4501
22 of 22
95.
Shaamala, A.; Yigitcanlar, T.; Nili, A.; Nyandega, D. Algorithmic green infrastructure optimisation: Review of artificial intelligence
driven approaches for tackling climate change. Sustainable Cities Soc. 2024, 101, 105182. [Cross Ref]
96.
Santos, P.; Cervantes, G.C.; Zaragoza-Benzal, A.; Byrne, A.; Karaca, F.; Ferrandez, D.; Salles, A.; Braganca, L. Circular Material
Usage Strategies and Principles in Buildings: A Review. Buildings 2024, 14, 281. [Cross Ref]
97.
Soori, M.; Karimi Ghaleh Jough, F.; Dastres, R.; Arezoo, B. AI-Based Decision Support Systems in Industry 4.0, A Review. J. Econ.
Technol. 2024, in press. [Cross Ref]
98.
Wang, X.; Cui, B.; Jing, L.; Wang, X.; Wu, M.; Wen, Y.; Wu, Y.; Liu, J.; Zhang, F.; Lin, Z.; et al. Enabling Low-Power Charge-Domain
Nonvolatile Computing-in-Memory (CIM) With Ferroelectric Memcapacitor. IEEE Trans. Electron Devices 2024, 71, 2404–2410.
[Cross Ref]
99.
Li, W.; Zhou, H.; Lu, Z.; Kamarthi, S. Navigating the Evolution of Digital Twins Research through Keyword Co-Occurence
Network Analysis. Sensors 2024, 24, 1202. [Cross Ref]
100. Ruan, H.; Wei, Z.; Shang, W.; Wang, X.; He, H. Artificial Intelligence-based health diagnostic of Lithium-ion battery leveraging
transient stage of constant current and constant voltage charging. Appl. Energy 2023, 336, 120751. [Cross Ref]
101. Liu, Y.; Ren, Y.; Lin, Q.; Yu, W.; Pan, W.; Su, A.; Zhao, Y. A digital twin-based assembly model for multi-source variation fusion on
vision transformer. J. Manuf. Syst. 2024, 76, 478–501. [Cross Ref]
102. Xu, B.; Bhatti, U.A.; Tang, H.; Yan, J.; Wu, S.; Sarhan, N.; Awwad, E.M.; Syam, S.M.; Ghadi, Y.Y. Towards explainability for
AI-based edge wireless signal automatic modulation classification. J. Cloud Comput. Adv. Syst. Appl. 2024, 13, 10. [Cross Ref]
103. Han, Y.; Yang, D.; Zhang, J.; Min, B.; Liang, Z.-W. Using Al Technology to Optimize Distribution Networks. J. Electr. Syst. 2024, 20,
1259–1264.
104. Ishteyaq, I.; Muzaffar, K.; Shafi, N.; Alathbah, M.A. Unleashing the Power of Tomorrow: Exploration of Next Frontier With 6G
Networks and Cutting Edge Technologies. IEEE Access 2024, 12, 29445–29463. [Cross Ref]
105. Mokhtar, B. AI-Enabled Collaborative Distributed Computing in Networked UAVs. IEEE Access 2024, 12, 96515–96526. [Cross Ref]
106. Rodriguez, E.; Masip-Bruin, X.; Martrat, J.; Diaz, R.; Jukan, A.; Granelli, F.; Trakadas, P.; Xilouris, G. A Security Services
Management Architecture Toward Resilient 6G Wireless and Computing Ecosystems. IEEE Access 2024, 12, 98046–98058.
[Cross Ref]
107. Walia, G.K.; Kumar, M.; Gill, S.S. AI-Empowered Fog/Edge Resource Management for Io T Applications: A Comprehensive
Review, Research Challenges, and Future Perspectives. IEEE Commun. Surv. Tutor. 2024, 26, 619–669. [Cross Ref]
108. Qu, X.; Shi, D.; Zhao, J.; Tran, M.-K.; Wang, Z.; Fowler, M.; Lian, Y.; Burke, A.F. Insights and reviews on battery lifetime prediction
from research to practice. J. Energy Chem. 2024, 94, 716–739. [Cross Ref]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

---
