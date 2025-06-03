# Distributed Topology Optimization for Agent-based Peer-to-Peer Energy Market

## Paper Metadata

- **Filename:** Distributed Topology Optimization for Agent-based Peer-to-Peer Energy Market.pdf
- **DOI:** 10.1109/smartgridcomm57358.2023.10333916
- **Authors:** Kilthau, Maximilian and Ansari, Daniel and Fay, Alexander
- **Year:** 2023
- **Journal/Venue:** 2023 {IEEE} {International} {Conference} on {Communications}, {Control}, and {Computing} {Technologies} for {Smart} {Grids} ({SmartGridComm})
- **URL:** http://dx.doi.org/10.1109/SmartGridComm57358.2023.10333916
- **Extraction Date:** 2025-06-03T15:01:22.800895
- **Total Pages:** 7

## Abstract



## Keywords



---

## Full Text Content



### Page 1

See discussions, stats, and author profiles for this publication at: https://www.researchgate.net/publication/375091240
Distributed Topology Optimization for Agent-based Peer-to-Peer Energy
Market
Conference Paper · October 2023
DOI: 10.1109/Smart Grid Comm57358.2023.10333916
CITATIONS
5
READS
69
3 authors, including:
Maximilian Kilthau
Helmut Schmidt University
25 PUBLICATIONS   105 CITATIONS   
SEE PROFILE
Alexander Fay
Ruhr University Bochum
778 PUBLICATIONS   5,941 CITATIONS   
SEE PROFILE
All content following this page was uploaded by Maximilian Kilthau on 31 October 2023.
The user has requested enhancement of the downloaded file.

---


### Page 2

Distributed Topology Optimization for Agent-based 
Peer-to-Peer Energy Market 
Maximilian Kilthau 
Institute for Automation Technology 
Helmut-Schmidt-University/University 
of the Federal Armed Forces Hamburg 
Germany 
maximilian.kilthau@hsu-hh.de
 Daniel Ansari 
Institute for Automation Technology 
Helmut-Schmidt-University/University 
of the Federal Armed Forces Hamburg 
Germany 
daniel@ansari.de
 Alexander Fay 
Institute for Automation Technology 
Helmut-Schmidt-University/University 
of the Federal Armed Forces Hamburg 
Germany 
alexander.fay@hsu-hh.de 
Abstract— Due to the ongoing energy transition the 
coordination of the power flow is shifting from centralized to 
decentralized, where autonomous systems such as software 
agents interact with each other. However, in contrast to 
centralized approaches, the communication effort of the agents 
significantly increases to share information among all agents, 
thereby an efficient communication approach in multi-agent 
systems is necessary. This paper proposes a novel distributed 
topology 
optimization 
approach 
that 
minimizes 
the 
communication effort in a peer-to-peer energy market, where 
agents buy and sell energy to efficiently dispatch energy flow. 
The approach is applied to a multi-agent system and simulations 
on an IEEE-33 and IEEE-119 bus network show that the 
proposed approach results in a higher financial gain with 
reduced communication effort compared to not applying the 
topology optimization. Overall, this approach has the potential 
to enhance the efficiency and scalability of energy management 
systems in a decentralized energy market. 
Keywords—decentralized control, communication, topology 
optimization, peer-to-peer energy market 
I. INTRODUCTION
The increasing integration of renewable energy sources 
and the growing number of energy consumers, such as 
electric vehicles or heat pumps, have led to significant 
challenges in the operation and management of modern 
power grids. Especially a reliable energy supply by 
photovoltaic systems and energy dispatch among households 
will be a major challenge. Traditional centralized approaches 
for energy dispatch may not be scalable and flexible enough 
to handle the complexities of modern power grids [1]. 
Furthermore, households are not actively involved into grid 
control, which can lead to non-grid-friendly behaviours and a 
reduction in overall comfort. To overcome the problem, peerto-peer energy markets exist where households can trade 
energy locally, as presented in [2]. With the emergence of 
distributed energy resources (DER) and advancements in 
communication and control technologies, agent-based 
approaches have gained attention as promising solutions for 
addressing these challenges [3]. 
Agent-based approaches leverage the capabilities of 
autonomous agents, e.g. generators, loads, and energy storage 
systems, to autonomously make decisions and interact with 
each other in approximately real-time [4]. These agents can 
communicate, coordinate, and collaborate to optimize the 
operation of the power grid. One key aspect of agent-based 
approaches is the design of the agent´s topology [5]. The 
agent´s topology describes which agents are communicating 
and interacting with each other to achieve efficiency and 
coordination. In addition to the agent´s topology, the grid 
architecture exists which describes the electrical connection 
between households. In this case, the grid architecture is 
given by an IEEE-33 as well as an IEEE 119 bus-network [6]. 
A. Problem Formulation
Besides the benefits of decentralization of the energy
market, it poses new challenges as well. Individual market 
participants are represented by multi-agent systems (MAS), 
which exchange information with other agents about the grid 
state, energy offers and energy demand. The task of energy 
trading between participants is distributed among the 
participating agents. To accomplish this, the participating 
agents 
must 
be 
capable 
of 
self-optimization 
and 
communication [7]. The more agents in a defined MAS that 
communicate and trade with one another, the closer the 
trading results are to the mathematical optimum, which can 
be achieved by applying central optimization [5]. On the 
other hand, a high number of interacting agents results in 
larger computational time which can be disadvantageous in 
case of volatile energy production by DER [8]. Thus, it is 
necessary to limit the number of interacting peers. This 
conflict can be addressed by mathematically optimizing the 
topology, which can improve the efficiency and scalability of 
the decentralized energy market. 
B. Contribution of the paper
In this paper, we propose a reliable distributed topology
optimization concept for agent-based energy trading in power 
grids. The concept aims to minimize agent communication 
while achieving better results compared to a scenario without 
topology optimization. The concept is based on defined 
properties of households to determine the most potential 
trading partners. It is implemented in an IEEE-33-busnetwork representing a standardised low-voltage-grid. The 
results are compared to the scenario where topology 
optimization is not applied to demonstrate the efficiency of 
the concept. 
C. Requirements of the distributed topology optimization
To guide the approach´s design and to enable a structured
verification, requirements are defined which are presented in 
this subsection. As a first requirement (R1), the system 
should minimize the agents’ communication while still 
achieving better results than what would be possible without 
topology optimization. The minimization should be 
employed decentrally. The second requirement (R2) 
describes that the topology optimization should be designed 
in combination with an agent-based peer-to-peer energy 
market to test the optimization´s performance. R3 represent 
978-1-6654-5556-5/23/$31.00 ©2023 IEEE

---


### Page 3

the privacy of the households. Thus, households’ properties, 
e.g., the yearly energy consumption, should be raised 
anonymously, and the numbers should be abstracted. As an 
additional requirement to the properties, the concept should 
consider the grid´s structure and be able to react dynamically 
to changes in the structure, e.g. the position of the power 
switches (R4). 
Furthermore, R5 describes the requirement that the 
approach should be able to handle an agent´s failure to ensure 
the concept´s reliability. A further requirement (R6) is the 
simplicity of the approach. This is important to achieve a 
higher software quality as well as a better maintenance of the 
code. In addition, simple concepts meet more acceptance of 
distributed system operators who are responsible for 
implementing the system in real low-voltage grids. 
II. STATE-OF-THE-ART 
Several approaches for optimizing the topology applied in 
a peer-to-peer energy market already exist in the literature. In 
this study, we analyse these approaches considering the 
requirements outlined in subchapter I.C. 
The authors of [9] present an agent system that optimizes 
its 
own 
energy 
consumption 
by 
applying 
internal 
optimization. Furthermore, an approach for grid control in an 
island grid using corresponding sensors is implemented. 
Decentralized optimization of energy flow is the focus of this 
publication, while requirements such as topology optimization 
are not considered. In contrast to [9], the authors of [10] 
present a topology optimization using a few larger renewable 
generation plants as energy producers in addition to 
consumers. Island grids are created based on these generators. 
This publication includes topology optimization of the agent´s 
communication; however, it is a one-time process that cannot 
be dynamically adapted to changing conditions. In [11], the 
topology optimization of [10] is further developed by 
considering the characteristics of grid participants to create 
optimized island grids that reflect their individuality. 
However, this approach fails to address dynamic grid changes, 
such as the failure of cables or agents. 
In [12], agents are introduced that control renewable 
energy generators to operate an island grid, with the agents 
collaborating to maintain grid stability. This publication 
focuses on the use of an agent system implemented within the 
Java Agent Development Framework (JADE) [13]. However, 
it does not incorporate communication cost minimization into 
the optimization process. 
In the publication of [14], a large power grid is partitioned 
into island grids with a focus on energy dispatch and the 
handling of partial failures within those grids. The 
optimization of network topology and energy dispatch are 
both considered, and there is an approach for responding to 
dynamic network changes. However, this publication does not 
utilize an agent system. Thus, a failure of a subsystem can´t 
be handled. 
The authors of [15] present a topology optimization using 
the Dijkstra algorithm. Thus, the agents can conduct 
decentralized grid control using the nearest power provider. 
Although no concrete time frames were determined for grid 
control, this publication addresses the need for efficient and 
reliable grid control. Besides the presented concept in [15], the 
authors of [16] present a concept which adapts the topology 
to dynamic grid changes using the Dijkstra algorithm. This is 
intended to ensure a stable and reliable power grid. This work 
stands out by introducing a plug-and-play principle for 
expandability of the power grid, which was not addressed in 
the other publications. However, [15] and [16] are not applied 
to a peer-to-peer energy market. 
[17] proposes a method for reconfiguring the network 
topology in response to critical grid states, which involves 
isolating faults to ensure grid operation. The approach 
responds to dynamic network changes and utilizes an agent 
system. However, a centralized topology with a master agent 
was employed instead of a decentralized topology. A 
summary of these results from the literature research is 
presented in TABLE I. 
TABLE I ANALYSIS OF THE LITERATURE REGARDING THE 
FULFILLMENT OF THE REQUIREMENTS, WHERE “X” REPRESENTS A FULMENT 
AND A “-“ NO FULFILMENT 
 
R1 
R2 
R3 
R4 
R5 
R6 
[9] 
- 
X 
X 
- 
X 
- 
[10] 
X 
X 
- 
- 
- 
X 
[11] 
X 
X 
X 
- 
- 
- 
[12] 
X 
X 
X 
- 
- 
X 
[14] 
X 
- 
X 
X 
- 
- 
[15] 
X 
- 
- 
X 
X 
X 
[16] 
X 
- 
- 
X 
- 
X 
[17] 
X 
- 
- 
X 
X 
X 
Although various works on the topic of topology 
optimization of an island grid exist, the requirements 
presented in I.C have not yet been fully met. This research gap 
is addressed in this paper. 
III. METHOD 
The development of the presented approach follows a 
modelling cycle and is based on four steps. In the first step, 
the real system - in this case, the low-voltage grid - is analysed 
to identify the network participants, their tasks, and interests. 
Based on the resulting structures, a preliminary model is 
constructed to represent a low-voltage grid and the grid 
participants therein. In the second step, this preliminary model 
is transformed into a mathematical model by parameterizing 
and quantifying the properties of individual grid participants 
and the boundary conditions of the preliminary model, while 
also making assumptions about the limitations of the 
preliminary model. In the third step, the mathematical model 
is implemented in JADE and the validation of the developed 
approach represents the fourth step. 
IV. AGENT MODELLING 
This chapter presents the concept of topology 
optimization, applying the first two steps of the presented 
modelling cycle. Since the topology optimization should be 
applied to a peer-to-peer energy market, this concept is 
presented as well. 
A. Peer-to-Peer Energy Market 
There are several approaches for a peer-to-peer energy 
market design as presented in [18]. One of them consists of 
agents which trade energy among each other without having 
a central coordination instance. This trading is based on 
competition since every agent seeks the maximum own profit 
In peer-to-peer markets are classified into fully connected and 
partly connected [5]. To provide a scalable system, a partly 
connected peer-to-peer market is applied. In [19] it was

---


### Page 4

shown that competitive trading algorithms are more efficient 
for use in competitive environments, such as trading energy 
quantity and price. Therefore, a competitive trading 
algorithm is applied for the presented peer-to-peer energy 
market. 
According to [5], a competitive leader-follower game is 
one of the most efficient competitive trading algorithms for 
designing the pricing model of the smart grid control, and is 
therefore used for the present study. In this work, a leader 𝑙𝑙 is 
an agent with surplus energy. Hence, leaders are willing to 
offer energy to other participants and begin the trading by 
offering energy. Agents that need energy decide how much 
of the offered energy they are willing to buy and act as 
followers 𝑓𝑓. The presented leader-follower game is 
mathematically defined as follows according to [20]: 
𝐺𝐺= {𝐿𝐿∪𝐹𝐹, {𝑋𝑋𝑙𝑙}𝑙𝑙∈𝐿𝐿, {𝑋𝑋𝑓𝑓}𝑓𝑓∈𝐹𝐹, {𝑈𝑈𝑙𝑙}𝑙𝑙∈𝐿𝐿 , {𝑈𝑈𝑓𝑓}𝑓𝑓∈𝐹𝐹} 
(1) 
Let 𝐿𝐿 be the set of offering prosumers acting as leaders 𝑙𝑙, 
and 𝐹𝐹 be the set of demanding prosumers acting as followers 
𝑓𝑓. Let 𝑋𝑋𝑙𝑙 and 𝑋𝑋𝑓𝑓 represent the strategy sets of leaders and 
followers, respectively. Further, let 𝑈𝑈𝑙𝑙 and 𝑈𝑈𝑓𝑓 represent the 
utility functions of leaders and followers, respectively, which 
mathematically describe the agent´s optimization objective. 
Consequently, every agent provides its own strategy and own 
utility function which is unknown to other agents. To avoid 
double-selling of energy, the energy amount is locked for 
trading as soon as a leader sends an energy offer until they 
receive a response. The followers have the following 
objective function to minimize their energy costs: 
𝑈𝑈𝑓𝑓= min ෍𝐸𝐸𝑙𝑙𝑙𝑙,𝑘𝑘∙𝑃𝑃𝑓𝑓𝑓𝑓,𝑘𝑘, ∀𝑘𝑘∈𝐾𝐾
𝑓𝑓∈𝐹𝐹
 
(2) 
Where 𝐸𝐸𝑙𝑙𝑙𝑙 represents the energy flow from 𝑙𝑙 to 𝑓𝑓 and 𝑃𝑃 
is the energy price that 𝑓𝑓 must pay to 𝑙𝑙. The index 𝑘𝑘 describes 
the discrete 15-minute time interval as a subset of K, the total 
simulation time. Unlike followers, leaders aim to maximize 
the price of the sold energy. Thus, they pursue the following 
objective function: 
𝑈𝑈𝑙𝑙= max ෍𝐸𝐸𝑙𝑙𝑙𝑙,𝑘𝑘∙𝑃𝑃𝑓𝑓𝑓𝑓,𝑘𝑘, ∀𝑘𝑘∈𝐾𝐾
𝑓𝑓∈𝐹𝐹
 
(3) 
If there is not enough energy offered, the follower will 
proactively send their remaining energy demand to other 
leaders. 
One challenge of decentralized optimization is the 
decision-making without a central authority. Thus, a criterion 
must be defined for when the negotiation is completed. Such 
a termination criterion is presented in [21], where the 
difference in price from the previous iteration step is used. 
When the difference falls below a defined value ε, the 
iteration ends. The termination criterion is mathematically 
described as follows: 
ห𝑃𝑃𝑓𝑓𝑓𝑓,𝑘𝑘+1 −𝑃𝑃𝑓𝑓𝑓𝑓,𝑘𝑘ห< 𝜀𝜀 
(4) 
If the final criterion has not been met, counteroffers will 
be created and sent. Once the final criterion has been reached, 
an acceptance message will be sent and energy delivery, as 
well as money transfer, can take place. 
Moreover, in case of an energy deficit that cannot be met 
by other prosumers, the prosumer must procure energy from 
an external energy supplier at a fixed energy price of 0.36 
€/k Wh. If a prosumer is unable to sell its surplus energy 
within the 15-minute trading interval, the surplus energy must 
be fed into the grid, and the prosumer receives a feed-in tariff 
of 0.08 €/k Wh. Thus, the maximum and minimum prices of 
the energy trading are set to the feed-in-tariff and external 
energy price, respectively. The fixed prices are based on 
current electricity prices in Germany and can be replaced 
variably. 
In addition, the trading interval consists of trading cycles 
with a duration of five seconds. Within these five seconds, 
every follower can optimize the incoming energy offers 
received in the previous trading cycle and send reoffers or 
rejects if necessary. Every leader can either create new energy 
offers or calculate reoffers based on received reoffers of the 
follower. In addition, if the end criterium is reached, both, 
leader and follower can send energy results. Thus, the number 
of actions an agent can conduct within a trading interval is 
limited to 𝑚𝑚 
𝑚𝑚= 𝑡𝑡𝑖𝑖𝑖𝑖𝑖𝑖
𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡
= 15 𝑚𝑚𝑚𝑚𝑚𝑚
5 𝑠𝑠
= 180 
(5) 
The value of 5 s is chosen because by applying lower 
trading-cycle duration, agents might not be able to finish all 
their computational tasks, including sending messages. This 
design of a peer-to-peer energy market is called discrete call 
auctions. Regener et al. [18] show that discrete call auctions 
result in a higher financial gain of the agents than continuous 
ones. Thus, the discrete call auction is applied in the work. 
 
B. Influence Factors for the topology optimization 
The topology optimization is an algorithm every agent 
executes when a 15-minute trading interval starts. The 
algorithm yields a list of agents which is sorted by relevance 
for the trading. Every agent has its own list which serves as a 
guide for the agents to determine the order in which they offer 
energy to their trading partners. To determine the relevance 
of every agent, influence factors need to be established which 
is described in the current subchapter. 
Yearly 
energy 
consumption: 
The 
yearly 
energy 
consumption of a household plays a crucial role in 
determining whether a household can be a potential buyer of 
energy. This information is critical for energy producers and 
traders to assess the potential profitability of selling energy to 
the household. A household with a high yearly energy 
consumption is more likely to have a significant energy 
demand, which makes it a potential buyer of energy. 
Flexible Energy Systems: Flexible energy systems of 
households refer to the ability of households to actively 
participate in the power grid operation by adjusting their 
energy consumption or generation based on external signals

---


### Page 5

or incentives. These flexible energy systems can include 
various DER such as photovoltaic (PV), battery energy 
storage systems (BESS), and electric vehicles (EV). The 
availability and behavior of flexible energy systems are 
crucial factors that can significantly impact the performance 
of the peer-to-peer energy market. Therefore, they are 
considered as one of the influencing factors in the presented 
distributed topology optimization approach. 
Solar Irradiation: Weather data, including meteorological 
measurements such as temperature, wind speed, solar 
irradiance, and precipitation, plays a crucial role in the 
operation of power grids. Since in low-voltage grids, only PV 
plants as DER exist, solar irradiation 𝑟𝑟𝑠𝑠 is taken as the 
measure for the weather data. 𝑟𝑟𝑠𝑠 has a direct impact on the 
generation and consumption of electricity, as well as the 
availability 
and 
performance 
of 
DERs. 
Therefore, 
incorporating 𝑟𝑟𝑠𝑠 into the distributed topology optimization 
approach is essential for accurate decision-making and 
optimal power grid operation. 𝑟𝑟𝑠𝑠 will be forecasted for the 
next 15 min in the region where the low-voltage grid is 
implemented. 
Thus, the yearly energy consumption, the flexible energy 
systems, and the forecasted solar irradiation are considered as 
influencing factors into the presented topology optimization. 
C. Mathematical Model of the Influencing factors 
To optimize the agent´s communication topology, it is 
important to quantify the influencing factors described in 
IV.B above. Since only agents having an energy surplus can 
start a negotiation, the influencing factors are rated based on 
producer´s perspective. A household that consumes a 
significant amount of energy annually is more likely to be an 
attractive negotiation partner as they have a high potential for 
energy consumption. This can result in a more stable and 
profitable trading partnership. Because of privacy issues, 
other agents are not allowed to know about the exact energy 
consumptions of other households. Consequently, the 
consumption rate is discretized and abstracted into High (H), 
medium (M) and low (L). According to [22], the energy 
yearly consumption 𝑐𝑐𝑦𝑦 per household can be rated between 2 
MWh to 5 MWh. 
In addition to the consumption rate, the amount of flexible 
systems of a household is important since a high share of 
flexible energy systems increases the possibility to buy 
energy on a peer-to-peer energy market. Thus, the percentage 
of flexible energy systems 𝑠𝑠𝑓𝑓 in relation to all energy 
consuming systems of a household is classified into H, M, 
and L as well. 
According to the three-level classification of the 𝑐𝑐𝑦𝑦 and 
𝑠𝑠𝑓𝑓, the 𝑟𝑟𝑠𝑠 is levelled in H, M and L as well. Therefore, the 
solar irradiation range of the actual day is divided into three 
equal parts (terciles) based on the maximum value of 
𝑟𝑟𝑠𝑠= 𝑟𝑟𝑠𝑠𝑚𝑚𝑚𝑚𝑚𝑚. Thus, 𝑟𝑟𝑠𝑠𝑚𝑚𝑚𝑚𝑚𝑚 of the current day needs to be 
forecasted. The forecasted solar irradiation for the next 15 
minutes is levelled into these terciles, where values in the first 
tercile labelled as H, the second in M and the third in L. A 
high solar irradiation level results in a lower priority level, as 
many other PV plants are likely to produce a significant 
amount of energy and offer it to other agents, thereby 
reducing the energy price paid by other consumers. This 
correlation is only given when consumers provide a flexible 
energy consumption to react dynamically to market prices. 
Based on the classification of yearly consumption, flexible 
energy systems, and solar irradiance, a priority score (PS) can 
be determined. The higher a household´s priority score, the 
more likely it is to buy energy. PS is composed of the 
combination of the levels of 𝑐𝑐𝑦𝑦, 𝑠𝑠𝑓𝑓 and 𝐺𝐺, consequently it can 
range from H-H-H to L-L-L, encompassing all possible 
combination in between. If an agent´s failure is detected, it is 
not listed on the priority list generated out of the topology 
optimization. The quantified classification is presented in 
TABLE II. 
TABLE II CLASSIFICATION OF YEARLY CONSUMPTION PER 
HOUSEHOLD, FLEXIBLE ENERGY SYSTEMS AND SOLAR IRRADIATION INTO 
HIGH(H), MEDIUM (M) AND LOW(L) 
Levels 
Yearly 
consumption per 
household 𝒄𝒄𝒚𝒚 
Percentage of 
flexible 
consuming 
systems 𝒔𝒔𝒇𝒇 
Solar irradiation 
𝑟𝑟𝑠𝑠 
H 
𝑐𝑐𝑦𝑦> 5 𝑀𝑀𝑀𝑀ℎ 
𝑠𝑠𝑓𝑓> 67 % 
𝑟𝑟𝑠𝑠
𝑟𝑟𝑠𝑠𝑚𝑚𝑚𝑚𝑚𝑚
< 33 % 
M 
2 𝑀𝑀𝑀𝑀ℎ< 𝑐𝑐𝑦𝑦
< 5 𝑀𝑀𝑀𝑀ℎ 
33% < 𝑠𝑠𝑓𝑓
< 67 % 
33% <
𝑟𝑟𝑠𝑠
𝑟𝑟𝑠𝑠𝑚𝑚𝑚𝑚𝑚𝑚
< 67 % 
L 
𝑐𝑐𝑦𝑦< 2 𝑀𝑀𝑀𝑀ℎ 
𝑠𝑠𝑓𝑓< 33 % 
𝑟𝑟𝑠𝑠
𝑟𝑟𝑠𝑠𝑚𝑚𝑚𝑚𝑚𝑚
> 67 % 
The process from starting the MAS to the start of the peerto-peer energy trading is depicted as an activity diagram in 
Fig. 1. After requesting the Agent Management Service 
(AMS) to get a list of all agents operating in the current 
system, every agent sends its consumption and flexibleenergy-systems level as a broadcast to all agents. After 
receiving others agent´s consumption and flexible-energysystems levels, the first trading interval can start. At the 
beginning of every trading interval, the weather forecast is 
called. Then, the priority list can be calculated. 
 
Fig. 1. UML-activity diagram of the topology optimization

---


### Page 6

Simultaneously, a simple check Alive message is sent as 
broadcast message. If an agent does not return the check Alive 
message, the agent is declared as failed and consequently will 
not be listed at the priority list. Once all these steps have been 
completed, the actual peer-to-peer energy trading can begin 
and continue until the start of the next trading interval. 
V. SIMULATION 
This chapter presents the simulation, its periphery as well 
as its results. Thus, the third and fourth step of the applied 
modelling cycle is presented. 
A. Simulation and Simulation Periphery 
To simulate the developed topology optimization both, a 
standardised low-voltage grid according to IEEE-33-test grid 
and a IEEE-119-test grid was used [6]. These test grids 
provide 33 and 119 nodes, respectively. To each node, 
different energy systems are assigned, which are based on the 
2050 expansion scenario of the electrical distribution grid 
[23]. According to [23] and [22] 80 to 90 % of residential 
buildings will be equipped with a PV system in 2050 and will 
be able to feed in or offer energy accordingly if there is 
sufficient solar radiation. The other households can only 
demand energy. The energy resource are modelled according 
to the findings of [24] as black-box models. A projected 
consumption pattern from the year 2050 is used to represent 
consumer´s behaviour. The household´s yearly energy 
consumption is randomly assigned to the households. The 
agent-based topology optimization as well as the peer-to-peer 
energy market is implemented in Eclipse utilizing JADE. The 
simulation is performed using the simulation environment 
Agent.Workbench [25]. 
The proposed approach is validated, and its advantages 
are quantified by comparing it with a decentralized energy 
dispatch in which energy offers are sent by agents in a 
randomly set order (referred to as RS). Furthermore, four key 
performance indicators (KPIs) are evaluated across all 
scenarios: the RS method and the topology-optimized (TO) 
agent selection, both of which are applied to IEEE-33 and 
IEEE-119 test grid. 
The first KPI depicts the average financial profit (FP) per 
prosumer, representing each leader's monetary gain in the 
energy market. The second KPI, the number of messages 
(NM) exchanged daily, signifies the system's communication 
load. The third KPI, the average performance (AP), evaluates 
the efficiency by relating financial gains to communication 
efforts. The last KPI assesses the nominated standard 
deviation of received messages, highlighting prosumer 
discrimination 
(DF). 
These 
KPIs 
are 
formulated 
mathematically in [19]. 
B. Results 
1) 
Presentation of Results 
The results of the peer-to-peer energy trading using TO 
compared to a RS are presented in TABLE III. The proposed 
TO method results in a higher financial profit for agents 
offering energy due to the improved selection of trading 
partners. Additionally, there's a noticeable reduction in the 
NM exchanged among agents, indicating the successful 
achievement of the approach's objective to minimize 
communication. In terms of scalability, when agents 
negotiate based on a TO in the IEEE 119 test grid, they 
require only 378 messages per prosumer daily for 
negotiations. This contributes to a better AP. When 
comparing TO with RS, the performance of DF is worse due 
to prioritization of prosumers in both test grids. 
TABLE III - RESULTS OF THE PEER-TO-PEER-ENERGY TRADING USING 
TOPOLOGY OPTIMIZATION (TO) AND RANDOM SELECTION (RS) 
 
Grid 
FP 
(€/k Wh) 
NM 
AP 
DF 
TO 
IEEE 33 
0,254 
226 
0,122 
0,4231 
RS 
IEEE 33 
0,249 
707 
0,035 
0,301 
TO 
IEEE 119 
0,265 
378 
0,070 
0,9134 
RS 
IEEE 119 
0,248 
1217 
0,020 
0,5957 
Regarding the differences between 33 prosumers and 119 
Beyond the recorded performance metrics, Fig. 2. also 
depicts the energy price aggregated for all 119 prosumers for 
every 15 min trading period. The graph suggests that the 
prosumer attains a more favorable average price due to 
improved communication with more suitable trading 
partners, as prioritized on the list. 
 
Fig. 2. Energy prices of TO and RS during one day for an IEEE-119 busnetwork 
The RS-simulation was conducted three times for each test 
grid to show that the results are reproducible. The variation 
among these three identical tests was quantified using the 𝑅𝑅2 
value of the matched prices. Consequently, the average 𝑅𝑅2 
value across all tests was found to be 0,9935. 
2) 
Result´s Discussion 
The presented TO provides a list of agents to 
communicate with aiming to trade energy. The list is sorted 
by priority to reduce communication effort. However, a 
household providing a high consumption potential is offered 
a lot of energy by agents having surplus energy. Thus, the 
household has to reject some energy offers which exceed its 
own energy need. Thus, there is still a communication 
overhead. This communication overhead can be reduced by 
applying learning algorithms or more complex dependencies. 
This however would reduce the simplicity of the presented 
concept. Furthermore, all agents are required to calculate a 
priority list, which remains the same for agents within the 
same low-voltage grid. However, if agents trade energy to 
households situating in other low-voltage grid, the distance 
between agents should be considered in the priority list. In 
addition, every agent can add personal preferences into the 
PS, e.g., the size of others consumer. Consequently, every 
prosumer needs its own priority list.

---


### Page 7

VI. CONCLUSION 
This paper presents a decentralized agent-based topology 
optimization which is applied to an agent-based peer-to-peer 
energy market. The topology optimization represents an 
algorithm which is based on three influencing factors and 
provides a priority list for every agent, i.e. an order of other 
agents which are the most attractive trading partners. The 
concept was simulated on an both, an IEEE-33 as well as 
IEEE-119 bus network. The simulation has demonstrated the 
benefits of applying decentral topology optimization in a 
local peer-to-peer energy market. The results clearly indicate 
that agents can achieve higher financial profits by using the 
proposed approach compared to not using it. Moreover, the 
reduction in the number of exchanged messages further 
enhances the efficiency and scalability of the energy 
management system. The results of this study contribute to 
advancing the understanding of decentralized energy systems 
and provide practical insights for the implementation of 
effective topology optimization strategies. 
In future work, the combination of topology-optimization 
and energy trading will be extended to decentral congestion 
management. Thus, agents can manage energy dispatch and 
additionally identify as well as manage congestions in a 
decentralized manner. In addition, the approach will be 
further adjusted to consider discrimination issues of 
prosumers. 
ACKNOWLEDGMENT 
 
This work was supported by the 
Federal 
Ministry 
for 
Economic 
Affairs and Climate Action and the 
Projektträger Jülich Gmb H (PTJ, 
FKZ: 03EI6035A) 
VII. REFERENCES 
[1] 
Zhou, Q., Shahidehpour, M., Paaso, A., Bahramirad, S., 
Alabdulwahab, A., and Abusorrah, A. 2020. Distributed Control 
and Communication Strategies in Networked Microgrids. IEEE 
Commun. Surv. Tutorials 22, 4, 2586–2633. 
[2] 
Mengelkamp, E. 2019. Engineering Local Electricity Markets for 
Residential Communities. 
[3] 
Paudel, A., Sampath, L. P. M. I., Yang, J., and Gooi, H. B. 2020. 
Peer-to-Peer Energy Trading in Smart Grid Considering Power 
Losses and Network Fees. IEEE Trans. Smart Grid 11, 6, 4727–
4737. 
[4] 
Derksen, C., Linnenberg, T., Unland, R., and Fay, A. 2013. 
Unified Energy Agents as a Base for the Systematic Development 
of Future Energy Grids. In Multiagent system technologies. 
Springer, Berlin. 
[5] 
Nedic, A., Olshevsky, A., and Rabbat, M. G. 2018. Network 
Topology and Communication-Computation Tradeoffs in 
Decentralized Optimization. Proc. IEEE 106, 5, 953–976. 
[6] 
Baran, M. E. and Wu, F. F. 1989. Network reconfiguration in 
distribution systems for loss reduction and load balancing. IEEE 
Trans. Power Delivery 4, 2, 1401–1407. 
[7] 
Yang, T., Yi, X., Wu, J., Yuan, Y., Di Wu, Meng, Z., Hong, Y., 
Wang, H., Lin, Z., and Johansson, K. H. 2019. A survey of 
distributed optimization. Annual Reviews in Control 47, 278–305. 
[8] 
Sarafraz, M. S. and Tavazoei, M. S. 2021. A Unified 
Optimization-Based Framework to Adjust Consensus 
Convergence Rate and Optimize the Network Topology in 
Uncertain Multi-Agent Systems. IEEE/CAA J. Autom. Sinica 8, 9, 
1539–1548. 
[9] 
Leo, R., Milton, R. S., and Kaviya, A. 2014. Multi agent 
reinforcement learning based distributed optimization of solar 
microgrid. In 2014 IEEE International Conference on 
Computational Intelligence and Computing Research. IEEE, 1–7. 
DOI=10.1109/ICCIC.2014.7238438. 
[10] 
Che, L., Zhang, X., Shahidehpour, M., Alabdulwahab, A., and AlTurki, Y. 2017. Optimal Planning of Loop-Based Microgrid 
Topology. IEEE Trans. Smart Grid 8, 4, 1771–1781. 
[11] 
Cortes, C. A., Contreras, S. F., and Shahidehpour, M. 2018. 
Microgrid Topology Planning for Enhancing the Reliability of 
Active Distribution Networks. IEEE Trans. Smart Grid 9, 6, 
6369–6377. 
[12] 
Logenthiran, T., Srinivasan, D., and Wong, D. 2008. Multi-Agent 
Coordination for DER in Micro Grid. In International Conference 
on E-Society, E-Education and E-Technology. 
[13] 
Bellifemine, F., Caire Giovanni, and Greenwood, D. 2007. 
Developing multi-agent systems with JADE. In Wiley Series in 
Agent Technology. 
[14] 
Arefifar, S. A., Mohamed, Y. A.-R. I., and EL-Fouly, T. H. M. 
2013. Optimum Microgrid Design for Enhancing Reliability and 
Supply-Security. IEEE Trans. Smart Grid 4, 3, 1567–1575. 
[15] 
Rishab Arya, Rishabh Yadav, and Raghav Agarwal and O.V. 
Gnana Swathika. 2018. Dijkstra’s Algorithm for Shortest Path 
Identification in Reconfigurable Microgrid. Journal of 
Engineering and Applied Sciences. 
[16] 
Taha Selim Ustun, Cagil Ozansoy, and Aladin Zayegh. 2011. 
Implementation of Dijkstra’s Algorithm in a Dynamic Microgrid 
for Relay Hierarchy Detection. In IEEE Smart Grid Comm. 
[17] 
Bawayan, H. and Younis, M. 2020. Mitigating failure propagation 
in microgrids through topology reconfiguration. Sustainable 
Energy, Grids and Networks 23. 
[18] 
Regener, V., Römmelt, G., Zeiselmair, A., Wasmeier, L., and 
Bogensperger, A. 2022. Design choices in peer‐to‐peer energy 
markets with active network management. IET Smart Grid 5, 4, 
281–296. 
[19] 
Kilthau, M., Karmann, A., Derksen, C., and Fay, A. 2023. Metric 
for Analysing cooperative and competitive algorithms for 
distributed frequency control in microgrids, CIRED 2023 - 27th 
International Conference on Electricity Distribution. 
[20] 
Maddouri, M., Debbiche, A., Elkhorchani, H., and Grayaa, K. 
2018. Game Theory and Hybrid Genetic Algorithm for Energy 
Management and Real Time Pricing in Smart Grid. In 2018 
International Conference on Electrical Sciences and Technologies 
in Maghreb (CISTEM). IEEE, 1–6. 
DOI=10.1109/CISTEM.2018.8613383. 
[21] 
Tofighi-Milani, M., Fattaheian-Dehkordi, S., Fotuhi-Firuzabad, 
M., and Lehtonen, M. 2022. Decentralized Active Power 
Management in Multi-Agent Distribution Systems Considering 
Congestion Issue. IEEE Trans. Smart Grid 13, 5, 3582–3593. 
[22] 
International Renewable Energy Agency (IRENA). 2018. Global 
Energy Transformation. A Roadmap to 2050. 
[23] 
Agora Energiewende. 2021. Klimaneutrales Deutschland. In drei 
Schritten zu null Treibhausgasen bis 2050 über ein Zwischenziel 
von -65 % im Jahr 2030 als Teil des EU-Green-Deals. 
[24] 
Wagner, L. P., Reinpold, L. M., Kilthau, M., and Fay, A. 2023. A 
systematic review of modeling approaches for flexible energy 
resources. Renewable and Sustainable Energy Reviews 184, 
113541. 
[25] 
Derksen, C., Branki, C., and Unland, R. 2011. Agent. gui: A multiagent based simulation framework. In Proceesdings of the 
Federated Conference on Computer Science and Information 
Systems, 623–630.
View publication stats

---
