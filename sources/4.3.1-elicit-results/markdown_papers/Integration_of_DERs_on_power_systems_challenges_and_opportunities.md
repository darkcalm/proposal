

---

Page 1

---

INTEGRATION 
OF 
DERS 
ON 
POWER 
SYSTEMS: 
CHALLENGES 
AND 
OPPORTUNITIES 
Tomás Gómez San Román 
IEB Working Paper 2017/02 
Energy Sustainability 


---

Page 2

---

 
 
 
IEB Working Paper 2017/01 
INTEGRATION OF DERS ON POWER SYSTEMS:  
CHALLENGES AND OPPORTUNITIES 
 
Tomás Gómez San Román 
 
 
 
The Barcelona Institute of Economics (IEB) is a research centre at the University of 
Barcelona (UB) which specializes in the field of applied economics. The IEB is a 
foundation funded by the following institutions: Applus, Abertis, Ajuntament de 
Barcelona, Diputació de Barcelona, Gas Natural, La Caixa and Universitat de 
Barcelona. 
 
Within the IEB framework, the Chair of Energy Sustainability promotes research into 
the production, supply and use of the energy needed to maintain social welfare and 
development, placing special emphasis on economic, environmental and social aspects. 
There are three main research areas of interest within the program: energy 
sustainability, competition and consumers, and energy firms. The energy sustainability 
research area covers topics as energy efficiency, CO2 capture and storage, R+D in 
energy, green certificate markets, smart grids and meters, green energy and biofuels. 
The competition and consumers area is oriented to research on wholesale markets, retail 
markets, regulation, competition and consumers. The research area on energy firms is 
devoted to the analysis of business strategies, social and corporative responsibility, and 
industrial organization. Disseminating research outputs to a broad audience is an 
important objective of the program, whose results must be relevant both at national and 
international level. 
 
The Chair of Energy Sustainability of the University of Barcelona-IEB is funded by 
the following enterprises ACS, CEPSA, CLH, Enagas, Endesa, FCC Energia, HC 
Energia, Gas Natural Fenosa, and Repsol) through FUNSEAM (Foundation for Energy 
and Environmental Sustainability). 
 
Postal Address: 
Chair in Energy Sustainability 
Institut d’Economia de Barcelona 
Facultat d’Economia i Empresa 
Universitat de Barcelona 
C/John M Keynes, 1-11 
(08034) Barcelona, Spain 
Tel.: + 34 93 403 46 46 
ieb@ub.edu 
http://www.ieb.ub.edu 
 
The IEB working papers represent ongoing research that is circulated to encourage 
discussion and has not undergone a peer review process. Any opinions expressed here 
are those of the author(s) and not those of IEB. 


---

Page 3

---

 
 
 
IEB Working Paper 2017/01 
 
INTEGRATION OF DERS ON POWER SYSTEMS:  
CHALLENGES AND OPPORTUNITIES 
 
Tomás Gómez San Román 
 
 
 
 
ABSTRACT: The integration of large amounts of distributed energy resources (DERs) 
as photovoltaic solar generation, micro-cogeneration, electric vehicles, distributed 
storage or demand response pose new challenges and opportunities on the power sector. 
In this paper, we review the current trends on: i) how consumers adopting DERs can 
self-provide energy services and provide other services at system level, ii) what can be 
expected at distribution networks and how retail markets will evolve with more 
proactive and market engaged consumers, iii) what are the effects and integration of 
DERs on wholesale markets, and iv) what are the challenges that DERs pose on 
cybersecurity and the opportunities for improving system resilience. Several 
recommendations are given for achieving an efficient integration of DERs. For instance, 
the design of a comprehensive system of prices and charges and the elimination of 
existing barriers for market participation are crucial reforms to achieve a level playing 
field between distributed and centralized resources when providing electricity services. 
This paper summarizes part of the work developed under the MIT Utility of the Future 
study. 
 
 
JEL Codes: 
D4, L94, L95, L98 
Keywords: 
Distributed energy resources, distribution networks, power systems, 
wholesale and retail electricity markets, locational marginal prices 
 
 
 
 
Tomás Gómez San Román 
Instituto de Investigación Tecnológica 
Universidad Pontificia Comillas 
C/Santa Cruz de Marcenado, 26 
28015 Madrid, Spain 
E-mail: tomas.gomez@comillas.edu 
 
 
 


---

Page 4

---

 
 
1 
INTRODUCTION 
The future landscape of the power system with a massive presence of distributed energy resources (DERs) 
as photovoltaic (PV) solar generation, distributed storage, commercial and residential cogeneration 
systems, electric vehicles, and demand response programs would present some relevant changes with 
respect today systems. DERs are connected at distribution networks and many of them at the consumer 
premises behind the meter. One of the implications of having distributed resources along the whole system 
would be the end of the traditional “trickling down” paradigm where top-down power flows from central 
generators to end consumers using first transmission and then distribution networks would be replaced 
by power flows in any direction top-down and bottom-up blurring the traditional boundaries between 
transmission and distribution networks. DERs would be another source for decentralized provision of 
services that should be considered in competition or collaboration with traditional centralized generators, 
for instance consumers may opt for producing energy from their own PV generators or to continue 
acquiring the service from the traditional utility. The massive utilization of information and 
communication technologies with capabilities of the Internet of Things empowering network users and 
facilitating the widespread of economics signals for services provision would contribute to make feasible 
this competition between DERs and centralized resources giving choice to customers. Dispersion and 
decentralization of service providers and new business models facilitated by a new structure of the power 
sector would appear in competition with or directly promoted by traditional incumbent utilities that in 
the end would change the current business panorama. The decentralization of trading among millions of 
agents using trading platforms different from the existing centralized approaches that today are mainly 
active in wholesale markets would be a new challenge with opportunities for new traders. Finally, the 
potential existence of agents, in some cases organized as energy communities, that decide to defect from 
the grid self-providing their energy needs would be another threat that appear for traditional utilities and 
challenge the current system. This new landscape poses the question, out of the scope of this paper, on 
whether incumbent utilities are prepared to lead this transformation.  
A future vision in no more than a decade ahead with today´s technology leads us to households and 
buildings fully equipped with chips that control appliances, responding to prices under virtual energy 
boxes in the cloud. Those software platforms would optimize energy bills while preserving customer 
comfort and environmental preferences. There will be a range of possibilities for customers through 
specialized service providers to find trading opportunities, for instance, peer-to-peer transactions, maybe 
departing from the “classical marketplace paradigm”.  
Today this vision is becoming a reality through pilot projects and real experiences in countries with 
advanced regulations and proactive policies. The drivers  for DER customer  adoption , and the challenges 
and opportunities that the integration of DERs pose in current distribution networks and their 
2


---

Page 5

---

 
 
 
 
implications on the functioning of wholesale and retail markets or in cybersecurity and resilience are 
illustrated in this paper mainly in the context of  U.S. and Europe electricity markets. Section 2 presents 
how customers may select different DER technologies under an economic rationale benefiting from the 
savings and revenues derived from the provision of services. Section 3 proposes new ways of revisiting 
the conventional practices to plan and operate distribution networks and the new roles and functions to 
be adopted by distribution companies in the new landscape. Section 4 presents some of the challenges 
related to the effects and integration of DERs on the functioning of wholesale markets. Section 5 
highlights the importance of increasing cybersecurity protection in the presence of DERs, and how, on 
the contrary, DERs may help to increase the resilience of the system in case of cyber-attacks or other 
natural disasters. Finally, Section 6 concludes with some recommendations for a more effective 
integration of DERs on power systems.  
2 DER CUSTOMER ADOPTION  
Customers by adopting distributed resources may self-provide energy services and deliver services for 
the system. For instance, residential customers may reduce their energy bill by installing PV generation 
and storage to self-provide energy and reduce peak consumption. Commercial buildings with high 
electricity consumption, large thermal mass and controllability of heating, ventilation and air 
conditioning (HVAC) providing demand response may participate in energy, capacity and ancillary 
service markets. The same for an electric vehicle (EV) aggregator by scheduling and controlling charging 
periods of a fleet of EVs while meeting the driving requirements of EV users. Energy communities may 
adopt multi-energy management systems to satisfy their energy needs under self-governance, energy 
efficiency, and net-zero emission strategies.  
In this Section, different case studies illustrate how customers may select different DER technologies for 
the provision of electricity services. 
2.1 
Interplay between gas and electricity for space heating and cooling in residential buildings 
Distributed energy resources for space heating and cooling  comprise a set of varied technologies, ranging 
from mature well established systems such as furnaces, boilers, and air conditioning units to emerging 
ones such as micro combined heat and power (micro-CHPs), reversible heat pumps, and hybrid gas-
electricity conditioning systems.  
To illustrate the technical and economic performance of some of those technologies, we consider a single-
family household of 150m2 under two distinctive climatic conditions, namely cold and warm, and two 
combinations of energy prices based on their electricity-to-gas ratio, with values of 3.6 and 1.9 for high 
3


---

Page 6

---

 
 
and low ratio scenarios, respectively. In term of technologies, we consider different type of fuel cells and 
reciprocating engines for micro-CHP and heat pumps (see Figure 1).  
Figure 1 presents the annual energy cost savings and simple payback period for the various technologies 
being tested under several scenarios. We observe that energy prices have a great impact on potential 
energy savings, as well as the upfront costs on the economic viability of the various technologies.  
   
 
Figure 1.: Annual savings of different DERs with respect a high efficient gas-fired condensing boiler (reference case) 
and expected simple payback periods under cold climatic conditions and two electricity-to-gas ratio scenarios, with 
values of 3.6 and 1.9 for high and low ratios (PEMFC: Polymer electrolyte membrane fuel cell; SOFC: Solid oxide 
fuel cell; ICE: Internal combustion engine; SE: Stirling engine; AA HP: Heat pump)1. 
 
The trade-off between electricity costs and fuel costs is key, as high electricity prices with high electricity-
to-gas ratios clearly favor the economics of micro-CHPs over heat pumps.  Markets with low prices and 
low electricity-to-gas differences favor electric heat pumps. Cold climates favor cogeneration systems, 
while mild ones favor heat pumps. 
Regarding micro-CHP, reciprocating engines are the most mature and established technology in the 
market, with upfront costs lower than other cogeneration systems making them attractive for consumers. 
Fuel cell-based systems are promising given their high electrical efficiencies and low primary energy 
consumption. However, their high equipment costs continue to be a barrier for their further deployment. 
2.2 
Commercial buildings providing demand response in ancillary services markets 
U.S. buildings use 74% of total electricity; nearly half of total building electricity consumption is from the 
commercial sector2. Within total consumption, electricity devoted to HVAC systems is the largest and 
frequently, most variable category. Materials used in commercial building envelopes and structures can 
provide energy storage when strategically heated or cooled. Enabling control technologies and software 
combined with HVAC systems that can facilitate more flexibility in building operation may result in 
commercial building participation in ancillary services markets while maintaining thermal comfort.  
-300
0
300
600
900
 CCold RHigh
 CCold Rlow
ANNUAL SAVINGS [$/YR]
PEMFC
SOFC
ICE
SE
AA HP
0
30
60
90
120
150
 CCold RHigh
 CCold Rlow
SIMPLE PAYBACK PERIOD [YEARS]
ICE
SE
PEMFC
SOFC
4


---

Page 7

---

 
 
 
 
For instance, individual small and medium office buildings located in Boston, MA that pay wholesale ISO-
NE locational marginal prices (LMPs) for electricity consumption and obtain revenues from the ISO-NE 
regulation and spinning reserves markets are simulated. Table 1 includes results of two July price 
scenarios A & B, Scenario A features higher ancillary services prices throughout the day compared to 
Scenario B, while the office paying either LMPs for energy cost or a July 2015 average retail rate of $14.50 
¢/kWh. The medium office buildings are able to recover 122-141% of electricity market expenditures for 
HVAC when paying the LMPs, resulting in a negative net operating cost. When paying an average retail 
rate for electricity, under both scenarios the medium office building still reduces its initial electricity cost 
by 13-26%.  
 
 
Scenario A 
Scenario A 
Retail 
Scenario B 
Scenario B 
Retail 
Optimal Energy Cost ($) 
403 
1436 
323 
1422 
Optimal Regulation Revenue ($) 
503 
352 
369 
178 
Optimal Spinning Reserves Revenue ($) 
68 
27 
26 
0 
Reduction in Energy Cost ($) 
571 
379 
395 
178 
Optimal Net Operating Cost ($) 
-168 
1057 
-72 
1243 
Table 1. Monthly weekday scaled estimates for optimal energy cost, ancillary services revenue and net operating 
cost for two July price scenarios under which the medium office pays either the LMP or average retail rate for 
electricity3. 
It can be observed that the tariff design is also important on the response of the office building providing 
ancillary services. Under flat volumetric retail rates for electricity, less ancillary services are provided 
than under dynamic energy market prices (LMPs).  
 
2.3 
Competition between battery storage and demand response.  
Two of the most prominent DERs – demand flexibility and battery energy storage – compete with each 
other providing the same type of services when adopted by residential consumers. 
The analysis is conducted using a model that simulates the operation of DER technologies in response to 
electric tariffs, climate conditions, and technology cost and performance parameters. We simulate the case 
of a single-family household in New York and in Texas. The key variables tested include the amount of 
demand flexibility and the upfront cost of batteries.  
Figures 2 & 3 depict the results in terms of the impact of different levels of demand flexibility and upfront 
battery costs on the profitability of the battery system. Demand flexibility is increased by expanding the 
5


---

Page 8

---

 
 
comfort temperature dead-band and engaging more end energy uses, air conditioning (AC) and water 
heaters (WH).  
 
 
Figure 2. The impact of flexible demand and battery cost on battery profitability in New York 
 
Figure 3.The impact of flexible demand and battery cost on battery profitability in Texas4 
In both cases, we see that demand flexibility has a significant negative impact on the profitability of 
batteries. As the amount of flexibility increases, the cost of batteries must be much lower for them to be 
profitable, indicating that flexibility is cannibalizing the battery revenue streams.  
6


---

Page 9

---

 
 
 
 
The key difference between the cases is the availability of the thermal resource. The hotter climate in 
Texas leads to greater use of air conditioning, which in turn means greater potential for smart energy 
management strategies to reduce customer bills. Without flexible demand, batteries are profitable at a 
higher upfront cost in Texas, but like New York, any amount of flexibility quickly diminishes the revenue 
opportunities.  
As conclusion, demand flexibility significantly reduces the profitability of batteries, but the size of the 
thermal resource and the structure of the tariff, not showed in the presented results, energy volumetric 
versus demand charges, are significant factors affecting the outcome. 
 
2.4 
Aggregators managing the charging of a fleet of electric vehicles 
Electric vehicles (EVs) are expected to play a crucial role in decarbonizing the transportation sector. 
Public policies are actively promoting the adoption of EVs all over the world5. The increasing penetration 
of EVs in the electricity system will increase the electricity demand. However, due to EV demand 
flexibility, EVs are parked most of the time, and possibly plugged-in, it would be possible to meet this 
load growth at minimum cost, for both the system and EVs’ owners. In addition, EVs could even sell 
energy back to the grid and provide electricity services, whenever they are incentivized to do so.  
In order to reduce electricity purchase costs and even obtain revenues from providing electricity services 
to the system, such as balancing energy or operating reserves, smart EV charging strategies would be 
crucial. An independent agent, an aggregator, can coordinate the charging of a fleet of electric vehicles, 
or alternatively, a smart charging system can automatically charge each EV independently.  
The costs and benefits of EV charging strategies would depend on a number of factors that vary from the 
markets where EVs participate, specific market regulations, degree of smartness of charging strategies 
and technology available, mobility patterns of EVs, among others. 
For instance, Figure 4 compares the average annual costs per vehicle charging under different imbalance 
pricing market rules, and charging strategies. Single versus dual imbalance pricing rules are compared. 
In addition, dumb charging, referring to start charging whenever the EV is connected, versus smart 
charging, either through an aggregator or through individual smart charging systems, are analyzed.  
 
7


---

Page 10

---

 
 
 
Figure 1 Value of aggregation depending on the imbalance pricing mechanism6  
The results show that smart strategies, charging EVs whenever wholesale prices are low and selling 
energy back to the grid when prices are high, result in around 40% lower costs than dumb charging. In 
markets with dual imbalance prices, and due to EV unforeseen energy imbalances, the cost of EVs 
charging would be almost 50% more expensive than in markets with single imbalance prices. 
Furthermore, in markets with single imbalance prices there would not be additional benefits of 
aggregating EVs and netting energy imbalances among them. 
In summary, smart EV charging strategies responding to time varying price signals can significantly 
decrease EV charging costs. Furthermore, the profitability of aggregators, assuming alternative 
individual EV smart charging strategies, is strictly related to market pricing rules, which in certain cases, 
such as the presence of dual imbalance prices, create opportunistic value for EV aggregation. However, 
charging of EVs through an aggregator can reduce entry barriers for participation in markets, such as 
the one related to meeting minimum size requirements. 
 
2.5 
Multi-energy services in integrated energy communities. 
Integrated Community Energy Systems (ICESs) are multifaceted smart energy systems, which optimize 
the use of local DERs, dealing effectively with a changing local energy landscape and local communities7. 
ICESs organization may emerge because of economic reasons, but in some other cases, even if these 
alternatives are more expensive, customers may be willing to self-organize and contribute towards a 
sustainable energy transition through local provision of renewable and energy efficiency solutions. 
Currently there are 2,800 energy co-operatives in Europe which indicates huge potential for community 
energy systems8. The recent surge of DERs is providing the enabling environment for ICES. Yet, there 
8


---

Page 11

---

 
 
 
 
are uncertainties on how ICES can emerge under currently centralized institutional settings and what 
value they would have for local communities as well as for the whole energy system. 
Figure 5 presents the annualized total energy costs of different alternatives to supply the energy needs to 
a community of 12 households, first in the base case with no DER installations and then assuming both 
individual household and community DER investment. Although the major cost savings comes from 
technological change from natural gas-based heating systems to heat pumps, the savings in energy costs 
because of self-consumed energy by solar PV, and consequent reduction of payments for policy costs, 
taxes and network costs are also significant. Network costs are mainly recovered through contracted 
individual peak capacity charges. Due to non-coincidental loads among households in the ICES, network 
charges can be reduced as the community peak demand is lower than the sum of the individual peak 
consumptions. Volumetric tariffs also allow savings in energy costs, policy costs and taxes. Overall, the 
cost savings with individual and community DER investment are 37 % and 43 %, respectively. In terms 
of CO2 emissions, they are also reduced from 55  (base case) to 16 and 12 tons, respectively. 
 
Figure 5. Cost-savings through ICES in grid-connected systems9 
In summary, under current energy prices and regulated charges, ICESs are attractive over the solely grid-
supplied option. Diversity of demand as well as generation profiles among the households within ICES 
lead to increased local exchanges. However, some of the cost reductions achieved are on policy or network 
payments that do not create system efficiency. By the contrary, they may create spill-over effects on the 
4889
3478
2975
2551
2170
2057
7309
5073
4304
4166
3030
2638
8642
11027
14353
495
522
-1962
-4448
-10000
-5000
0
5000
10000
15000
20000
25000
30000
35000
40000
Grid supply (Base case)
 Individual DER investment
Individual and community DER
investment
Annualized total energy cost (€)
Electrical Energy
Network
Policy
Taxes
DERcost
Natural Gas
Export
9


---

Page 12

---

 
 
remaining passive customers that will see progressive energy bill increments. On the other hand, ICESs 
also have potential to provide energy services to the bulk power system such as ancillary services 
increasing their revenues, as it has been commented for the case of commercial buildings in Boston.  
 
3 
DERs AT DISTRIBUTION  
The development of DERs would drive a change in paradigm thus require revisiting the conventional 
ways to plan and operate distribution networks, send locational economic signals to network users, and 
define new functions and roles for traditional distribution utilities.  
3.1 
Fit and forget versus active network management 
Traditionally, distribution network planning and operation have been carried out as two almost fully 
decoupled tasks. Firstly, long-term network planning consisted in forecasting the peak demand over the 
planning horizon on a regional basis and reinforcing the grid accordingly. At this stage, the main goal 
was to ensure that no operational constraints, thermal limits or voltage problems in network installations, 
would be encountered during day-to-day operations. As a consequence, the grid was passively operated 
with very low levels of monitoring and control.  
Likewise, the progressive connection of new network users, including DER installations, has been so far 
managed under this paradigm by reinforcing the network whenever the existing grid capacity was not 
enough to ensure that the most unfavorable conditions foreseen can be coped with. Thus, all potential 
problems were tackled at the time of network connection. Hence, this is usually referred to as a “fit & 
forget” approach. This network management approach has proven to be effective and cost-efficient in a 
conventional centralized environment. However, the development of DER is questioning the suitability 
of such a model as the power system becomes more and more decentralized.  
For instance, the UK Smart Grids Forum, participated by public authorities, industry and other 
stakeholders, carried out an analysis of the distribution network investment needs to accommodate DER 
in different scenarios for the year 205010 A business as usual (BAU) scenario, where only conventional 
“iron-and-copper” investments are considered, is compared to the implementation of smart distribution 
grid solutions. In this regard, both a large-scale top-down and a progressive or incremental deployment 
of smart grid solutions were considered. The results, depicted in Figure 6, show that the implementation 
of smarter distribution grids and active network management provide much lower costs as compared to 
the conventional “fit and forget” or BAU paradigm.   
10


---

Page 13

---

 
 
 
 
 
Figure 6: Network investment needs to connect different rates of low carbon technologies to the British 
distribution system by 2050. Source: EA Technology, 2012 
In a nutshell, a passive grid operation and a fit & forget approach to connect new network users is bound 
to lead to an important cost increase, particularly when large shares of DER are to be connected. 
Oftentimes, costly grid reinforcements would be triggered by situations that, at most, would only happen 
a few times per year; for example, when there is a very high solar irradiation. Moreover, the need to 
reinforce the grid can result in long lead times for connecting new network users. Therefore, distribution 
companies will need to adopt innovative ways to manage their networks in order to facilitate an efficient 
transition to a decentralized system.  
This necessarily implies bringing network planning and operation closer together so that network 
thermal and voltage limits are tackled not only at the planning and connection stage, but also during real-
time operation. This active network management approach ultimately relies on smarter distribution grids, 
which integrate an extensive use of ICTs to enable advanced monitoring and control capabilities. 
However, despite the fact that the implementation of smart grid solutions implies a deep change in 
paradigm for distribution utilities, these companies are facing an even greater challenge in this transition.  
Distribution companies will no longer manage network elements alone. Instead, they will need to interact 
closely with DER to operate the distribution grid. Thus, DER flexibilities may become essential for day 
to day network operation. Accordingly, distribution companies will become system operators, which 
acquire network services from DER such as voltage control or congestion management.  
Early examples of such transformation can be already seen in some countries. For instance, since 2012 
German distribution companies can remotely limit the injection of PV installations above 30kW in case 
11


---

Page 14

---

 
 
of local network constraints in exchange for an economic compensation. Smaller PV units may either 
follow the same instructions as larger plants or permanently limit their injection to 70% of their rated 
withdrawal capacity11. Similarly some regulators are promoting such a change in planning and operation 
practices. The UK is an example of this, since distribution companies are required to follow common 
methodologies and indicators to justify their long-term investment plans based on benefit-cost analyses 
and including innovative grid solutions12. 
 
3.2 
Benefits of DER on network operation and planning by responding to prices 
In addition to a more active management of distribution networks, we will need a comprehensive system 
of prices that motivate efficient responses by network users from a system perspective.  
DERs may create value in very different ways and are therefore likely to have very different impacts on 
distribution network operations and in the end in planning. Using a detailed model of a distribution 
network, we compare the network impacts from customer DER investment decisions in response to 
different economic signals, specifically flat average prices (Flat), hourly time varying prices at substation 
level (Substation LMP), and distribution locational energy prices calculated at each node of the 
distribution network (DLMP). Results suggest that the type and location of DERs likely to emerge on 
the distribution network are very sensitive to the structure of energy prices. Furthermore, locational 
prices can effectively align customer DER investment decisions with network benefits, potentially 
relieving network constraints at a cost that is less than traditional ‘iron-and-copper’ solutions. 
Figure 7 shows the location and technology type of the most profitable DER investments– solar PV, 
HVAC controls, or batteries – under different energy price structures. Customers adopt the most 
profitable investments according to the implemented energy price structure. Each panel corresponds to 
the same distribution network (dots are network users and lines are distribution wires), with the network 
congested region highlighted in the upper left. Flat prices, for example, lead to investments in solar PV 
with no discernable geographical pattern that do not help to solve the congestion in the network. In 
contrast, distribution locational marginal prices (DLMP) lead to investments in HVAC controls that are 
clustered around the area of congestion and help to solve the problem by demand reduction in those 
critical hours when the network is congested.  
In summary, flat, volumetric energy rates resulted in solar PV being more profitable from a customer 
perspective relative to either demand management or battery technologies. Energy prices that varied over 
time, but not location, resulted in demand management technologies being the most attractive, while 
12


---

Page 15

---

 
 
 
 
prices that varied across both time and location also resulted in demand management technologies being 
the most attractive, but coordinated around congested areas of the network. 
 
Figure 7 | Most profitable DER investments under different energy price structures13 
Figure 8 compares the net cost of addressing the network congestion with DERs and traditional ‘iron and 
copper’ solutions. Cases are listed in order of least costly to most costly. Three network cost drivers are 
included in the final metric: losses, non-served energy (NSE), and investments (either DERs or 
transformer replacement). Cost reductions (benefits) appear as negative bars, while cost increases (e.g., 
investment) appear as positive bars. A red line for each case represents the net cost. 
13


---

Page 16

---

 
 
 
Figure 8. Net cost of DERs addressing network constraint14 
As shown in Figure 8, the lowest cost solution occurs when the best 10 DER investments are installed 
under the DLMP pricing scenario. Looking back at Figure 7 shows that those investments are HVAC 
controls, all located in the area of congestion. The traditional utility solution upgrading the network – 
replacing the transformer – actually results in greater benefits in the form of reduced non-served energy 
and losses, but carries a higher upfront investment cost, making the total net cost higher than the best 
DER solutions. DER investments that emerge under Flat and LMP prices result in some reduction in 
losses, but because they are located outside of the congested region (see Figure 7), do not reduce non-
served energy, making their net cost much higher. 
In summary, DLMPs can effectively align customer incentives for DER investment with network 
benefits, and DERs can potentially solve network constraints at a cost that is below traditional network 
reinforcement solutions. 
 
3.3 
New roles of distribution utilities and interactions with DERs 
The progressive decentralization of the power system, together with the massive deployment of ICTs and 
enhanced consumer awareness, will require distribution companies to adopt new roles.  
First, we have shown how relevant it will be for distribution companies to take into account the flexibility 
potential of DER when doing network planning and operation. Distribution utilities may adopt a new 
role as active system operators. Distribution companies may additionally need to enhance their role as 
neutral market facilitators, both in terms of retail competition, in those jurisdictions with such feature, i.e. 
as data managers, and providing non-discriminatory access of DER to local and upstream markets and 
14


---

Page 17

---

 
 
 
 
services by enhancing their interaction with other stakeholders including: market operators, transmission 
or independent system operators, suppliers, and aggregators. Finally, distribution companies could play 
an essential role in enabling or directly deploying innovative technologies such as smart metering, 
distribution storage or electric vehicle (EV) recharging infrastructure. In the following, we will introduce 
the drivers for the adoption of these new roles as well as the most relevant implications. 
The interaction between distribution network utilities and network users has been conventionally limited 
to the one-off grid connection process, phone calls in case of a supply interruption and, depending on the 
specific regulation, metering and billing. However, as discussed above, the implementation of active 
network management approaches entails exploiting the existing DER flexibility potential by actively 
managing the resources connected to the grid.  
The regulatory needs to enable this interaction depend largely on the power sector organization and 
structure. In the absence of unbundling requirements, distribution companies may directly own and 
operate DER both for network support and market participation. For instance, in the State of California, 
the Regulatory Commission has mandated large investor-owned utilities to deploy a certain storage 
capacity by 2020 for several applications, including distribution network support. This storage capacity 
may be owned either by the utilities themselves (no more than 50% of the total capacity) or by third-
parties15.  
The main challenges arise precisely when the DER are not directly owned and operated by the 
distribution company. This may happen either because, unbundling rules forbid so, as in the case of 
Europe, or simply because other stakeholders decided to invest in such installations for commercial or 
other reasons, e.g. prosumers, independent renewable producers or EV charging stations. In these cases, 
a level playing field for all types of DER should be established. For that purpose, a neutral platform 
enabling the commercial transactions can be an alternative. For instance, New York authorities, under 
the on-going reform of the electricity sector regulation, envision future utilities as becoming Distributed 
System Platform Providers16 .  
A key missing link for this to happen is that of suitable regulatory mechanisms that would allow 
distribution companies to acquire services from DER in a transparent and non-discriminatory manner. 
The challenge is then how to turn DER flexibility into an additional tool for distribution companies in 
addition to network investments. Some of the main existing mechanisms, beyond mandatory 
requirements, can be broadly categorized into17 18: 
- Bilateral flexibility contracts: this scheme would consist in an agreement between the distribution 
company and DER owners, or the corresponding aggregator, to provide a flexibility service. In 
15


---

Page 18

---

 
 
exchange, the DER would receive a reduced grid connection charge or an agreed fee. These 
contracts are sometimes referred to as flexibility contracts, variable access contracts or non-firm 
connection agreements.  
- Local flexibility markets: in case distribution companies are able to foresee and contract in 
advance the required amount of flexibility, they could organize local markets for this service (i.e. 
periodical auctions to allocate flexibility contracts). For instance, this mechanism may be applied 
to solve expected network overloads in a year-ahead horizon in a distribution area where 
distributed generation (DG), demand response or storage could compete to contract such service.  
It is important to highlight that the implementation of network services at distribution level, in 
combination with a system of prices with locational differentiation, will offer DER additional revenue 
streams.  This will pave the way for new business opportunities for agents such as aggregators that 
combine the flexibilities of a large number of DER to respond to the needs of distribution companies.  
Regarding the deployment of innovative technologies, such as distributed storage, EV recharging 
infrastructure or smart metering, the main question to be addressed by policy makers and regulators is 
whether these technologies should be treated as distribution assets, thus regulated as a natural monopoly, 
or, on the contrary, consider them open to free market competition, limiting the role of distribution 
companies at connecting them to the network. The selection of one alternative or the other will be thus 
largely influenced by existing unbundling rules.  
For instance, smart metering infrastructure is a key enabling technology in a low-carbon decentralized 
power sector, and it is driven by several factors: development of prosumers, increased awareness from end 
consumers, need for flexible demand response, or the desire to promote retail competition. Traditionally, 
metering deployment and ownership has been part of the activities and remuneration of distribution 
utilities. The corresponding costs would be recouped via the tariff or a specific rental fee. Hence, it may 
seem straightforward that distribution companies remain in charge of deploying smart metering 
infrastructure. However, there are a few relevant nuances and alternatives to this.  
EU countries have predominantly opted for a conventional model for smart metering roll-out where 
distribution companies perform a centralized large-scale deployment, although there are a few exceptions 
to this rule19 . For instance, German consumers may choose any metering operator (or remain with their 
conventional meter). Metering operators may compete among them to provide this service, albeit 
distribution companies would remain as the default metering operator.  In the UK, a large-scale smart 
meters roll-out has been mandated. The main difference with respect to the conventional approach is that 
it is the responsibility of suppliers to carry out this deployment.   
16


---

Page 19

---

 
 
 
 
Another added difficulty that has been faced in some jurisdictions is the opposition to smart metering due 
to privacy or health concerns from the population. In these cases, some regulators have decided to 
introduce opt-out clauses in their roll-out programs. This has been the case, for instance, of The 
Netherlands or California20 .  
Another innovative technology are distributed storage systems connected to the distribution network. 
They offer new possibilities for distribution companies. However, going from demonstration projects to 
actual deployment raises two main regulatory concerns: i) whether distribution utilities may own and 
operate storage systems (considering unbundling rules), and ii) how distribution companies may influence 
the location of storage so that it can provide grid support services where they are needed.   
In case distribution utilities were entitled to own the storage systems, as in the aforementioned case of 
California, they could locate these systems where the grid actually needs the flexibility. However, the 
benefits from the provision of grid support services alone may not be enough to yield a positive business 
case. Moreover, given that network constraints may arise only a few times per year, the storage systems 
could be underutilized. This can be avoided by allowing distribution companies to participate in upstream 
markets for price arbitrage or the provision of balancing services. However, this may be hampered or 
undesirable when a strong emphasis is placed on unbundling. Regulators may explore intermediate 
approaches that could allow reconciling these two opposing principles of appropriate storage location and 
sizing, and respecting unbundling rules. These may include enabling distribution companies to own 
storage assets only under certain conditions (e.g. size limitations or limited to non-competitive activities) 
or to organize auctions for the installation of storage at certain locations by third parties. 
 
4 
DERs AND INTERACTIONS WITH THE BULK POWER SYSTEM 
The integration of large amounts of DERs pose several challenges in the functioning of present wholesale 
markets and the need of reviewing some market rules to achieve a level playing field among centralized 
generators and distributed resources. In addition, the participation of DERs in wholesale markets in 
combination with the provision of valuable network services require a more close coordination between 
transmission system operator (TSO) and distribution system operator( DSO) functions.  
 
17


---

Page 20

---

 
 
4.1 
DER active participation in wholesale markets 
The integration of large amounts of DERs in wholesale markets present several challenges related to 
their effects on the functioning of these markets and on the other hand, the elimination of current barriers, 
that difficult their participation on equal footing than conventional centralized technologies. 
Technologies consisting of variable renewable energy (VRE) sources, both utility-scale centralized and 
distributed customer-adopted installations, such as wind and solar, have a great potential to grow in the 
upcoming years. 
The main challenge for the integration of these technologies is indeed its intermittency, which requires 
other resources to rapidly adapt their power output in order to keep the instantaneous balance of 
generation and demand. Both expected and unexpected variations in VRE power output will increase the 
need for flexible generation capacity in power systems. The fact that a rapid change in VRE generation 
can be better predicted does not eliminate the need for fast ramping resources. This is well illustrated by 
the Californian “duck-curve” (Figure 9). Increasing solar penetration in the Californian system results in 
a net load curve that produces significant ramping needs in the evening, and at the same time requires 
thermal generators to drastically reduce their output during the day. 
 
Figure 9: Duck Curve. CAISO 201321. 
The most notorious result of a large penetration of VRE is probably the so-called merit order effect; solar 
and wind zero variable cost generation displaces other generating technologies with higher variable costs, 
having the immediate effect of reducing wholesale market prices. Because VRE are only intermittently 
available, the reduction in prices only affects those periods when solar or wind generation is available, 
although it can result in lower prices on average. 
In power systems where most of the variability of VRE will be absorbed by thermal generation, these 
thermal units will be forced to rapidly change their output and to more frequently start-up and shut-
down. Consequently, generation costs associated to thermal plants cycling will increase and, for a large 
18


---

Page 21

---

 
 
 
 
penetration of VRE the merit-order effect may be offset by thermal cycling costs increasing energy prices. 
Figure 10 depicts this effect in a simulation of the solar generation impact in the ERCOT system. 
 
Figure 10: System and thermal production cost for increasing solar penetration in a thermal-
dominated system (MIT, 2015)22 
The effect of VER on spot prices is, therefore, twofold. Prices can increase due to the cost of thermal 
generation cycling in some periods, while they can drop when VRE production displaces more expensive 
generation. In those latter cases, prices can reach negative values, negative prices reflect the excess in 
electricity supply, when inflexible thermal generators find impossible or uneconomical to come offline. 
This effect will be more pronounced due to VRE priority of dispatch rules or production subsidies. All 
these lead to higher price volatility in spot electricity markets, which combined with the unpredictability 
of VRE, also makes electricity prices diverge between different sequential markets, such as day-ahead and 
intraday or real-time markets. 
On the other hand, facilitating the potential of DERs to provide electricity services in wholesale markets 
requires properly designed markets that shall ensure the efficient deployment and operation of DERs. 
However, current electricity markets present numerous barriers to the participation of DERs. In most 
cases, these barriers are simply the result of technology evolving at a faster pace than electricity market 
rules and regulations. For example, the participation of DERs may be hindered by a lack of clear rules, or 
by rules that were designed with large traditional resources in mind, and have not been updated ever 
since. 
Pioneering experiences in DER integration show the most urgent changes needed in wholesale markets 
to allow for DER participation. In the following, we concentrate on size-related and product definition 
barriers.  
In general, most of the current electricity markets require a minimum size for market participation. This 
limitation is sometimes justified by the computational complexity of market clearing algorithms. This is 
19


---

Page 22

---

 
 
especially true for short-term markets that may not be able to post results in time if the number of 
participating bids is too large. 
Even if there are no limitations to the bid size, market platforms may impose fixed entry fees to 
participants, which may be easily offset by profits for large resources, but can impede the business case 
for small participants. 
The most common approach to remove these two barriers is to permit the aggregation of DERs. This 
allows the participation of DER in current market platforms with minimal changes, managing aggregated 
resources as conventional ones, and “outsourcing” the disaggregation of market payments and dispatch 
instructions to individual resources. For instance, in 2016, the California Independent System Operator 
has been the first ISO in the US approved by the Federal Energy Regulatory Commission (FERC) to 
allow providers to group various distributed energy resources to reach the threshold for market 
participation currently at 0.5 MW23. 
Another existing barrier for DER participation in markets is the current definition of some market 
products. In markets that allow the participation of DERs, their involvement may still be hindered by 
market products that were designed with the capabilities of conventional resources in mind, and do not 
fully reflect the needs of the power system. In addition, the remuneration for these products may not be 
able to capture the additional value of, for example, a more flexible resource than a traditional thermal 
power plant. 
The challenges associated with DER participation can be widely different between each of the market 
segments. For example, in capacity markets, the key challenge is how to assess the contribution to firm 
capacity made by resources with very different technical characteristics. Those markets were initially 
thought for the participation of only conventional generators, more recently demand response offering 
peak-load reductions is increasingly been allowed to participate, but still VRE and storage are the 
technologies that find more barriers for participation in these markets. 
An illustrative example of demand response participation in markets is given by the annual mapping that 
the Smart Energy Demand Coalition (SEDC) makes in Europe. SEDC acknowledges the progress made 
with the inclusion of demand response in European network codes, but still grades some member states 
very negatively due to five main regulatory barriers: 1) Demand response may not be accepted as a 
resource, 2) Inadequate and/or non-standardized baselines, 3) Technology biased program requirements, 
4) Aggregation services are not fully enabled, and 5) Lack of standardized processes between balancing 
responsible parties and aggregators24. 
 
20


---

Page 23

---

 
 
 
 
4.2 
The importance of locational economic signals 
As it has been stated in previous sections, in a more decentralized system, , economic signals will play a 
crucial role in coordinating interactions amongst power system users. Active system users with DERs 
may contribute to not only mitigate negative system impacts but enhance power system efficiency over 
the entire power grid.  
Locational marginal prices (LMPs) of energy changing in time and network location reflect costs of 
production, as well as of the impacts of network losses and technical constraints in those costs. Presently 
LMPs are only used in some countries, mainly in the U.S: and Latin America countries, and exclusively 
at transmission level. While in distribution, they are not used yet. Extending the calculation of LMPs to 
the distribution network appears to be conceptually simple, although difficult computational issues appear 
when the distribution network and DERs response are represented in detail25. In Figure 11, the 
streamlined equivalent to the complete Spanish distribution network in terms of the share of losses at the 
different voltage levels is represented. It can be observed that differences in energy prices of up to 40% 
are shown to exist, which can make all the difference in the viability of investing in a given DER or 
whether to operate it or not at a given time. Note that in the operating conditions shown in the figure the 
power flows trickle down and the lower the voltage the higher the LMP. The situation would be exactly 
the opposite in an exporting, instead of importing, mode26.  
21


---

Page 24

---

 
 
 
Figure 11. Distribution locational marginal prices considering aggregated distribution losses for 
the Spanish system. 
In summary, it is clear that in the context of decentralization of services, sending time and locational 
differentiated energy prices and cost-reflective network charges will be relevant for bringing system 
efficiency in operation and planning stages. This efficiency will be the result of a decentralization economic 
rational making decision process where customers adopt DER in their own benefit.   
 
4.3 
TSO-DSO coordination in presence of large amounts of DERs 
DERs can contribute to the provision of all of the electricity services at transmission and distribution. As 
it has been presented in previous sections, the efficient participation of DERs can only take place if they 
receive the right economic signals and have access to the different markets where these services are traded. 
The key institutions that mange those services are the system operators at transmission (TSO) and 
distribution (DSO) levels, and their coordination is of essence.  
DERs can provide services, such as, but not limited to congestion relief, reactive power and voltage 
control, and frequency reserves. The roles of TSOs and DSOs will be evolving in kind as more DERs 
22


---

Page 25

---

 
 
 
 
start to change load and generation patterns. With increasing penetration of DERs, the coordination 
between system operators will expand, in terms of information exchange, monitoring and analytic 
capabilities, computation of prices of electricity services, forecasting, scheduling and activation of 
resources, as well as system operator responsibilities. DSOs and TSOs must be able to monitor and engage 
resources as well as study and share information in a timely manner to enable efficient markets and reliable 
system operations. The coordination between TSOs and DSOs is of utmost importance for the grid to 
obtain the full value from services provided by DERs. 
The evolution of the DSO/TSO coordination can be foreseen as a two-phase process. In the initial phase, 
DERs would provide services mostly to the TSO in established markets without violating constraints 
within the distribution networks, since these networks would have enough margin to manage flows and 
DSOs would not buy services from DERs. There would be challenges with respect to the effectiveness of 
DERs providing TSO services and the need to extend price signals further into distribution networks to 
guarantee a level playing field between centralized and distributed resources. The deployment of advanced 
metering infrastructure (AMI) would still be low. In the second phase, a higher integration of DERs and 
AMI is expected and new services can be provided by DERs and purchased by both TSOs and DSOs, 
leading to potential conflicts. New roles for DSOs have to be established, as well as the mechanisms for 
purchasing distribution services, which must be coherent and coordinated with those managed by the 
TSO. The developments of both phases are contingent upon many system specific factors and, in 
particular, the evolution of the regulatory frameworks27.  
Different actions are currently under development worldwide to efficiently integrate DERs into the power 
system and to reform the roles of the agents involved in the transformation. The European Commission 
(EC) and the New York State Department of Public Service in Reforming the Energy Vision (REV) are 
two examples of institutions actively pursuing increased coordination between the DSOs or Utilities and 
the TSOs or Independent System Operators (ISOs), respectively. ENTSO-E (European Network of 
Transmission System Operators for electricity), ISGAN (International Smart Grid Action Networks), 
CIRED (International Conference on Electricity Distribution), EDSOs (European Distribution System 
Operators) have task forces and working groups investigating future roles, relationships, markets and 
coordination requirements for and between the operators28. 
 
5 
CYBERSECURITY, RESILIENCE AND PRIVACY WITH DERs 
Widespread connection of DERs in power systems, tied to transactional energy markets, will increase 
digital complexity and attack surfaces, and require more widespread and intensive cybersecurity 
protection. Cyber incidents can cause loss of grid control or damaged equipment from deliberate 
23


---

Page 26

---

 
 
tampering with data, firmware, algorithms, or communications; false data injection into pricing or 
demand systems; data exfiltration; and ransom demands to restore access to data29. 
Utilities and DER providers need to develop approaches to defend against cyber-attacks, and recover 
from possible cyber and physical attacks. To keep up with rapidly evolving cybersecurity threats 
against large and complex electric utility grids, electric utilities, vendors, law enforcement, and 
governments need quickly and effectively to share current cyber threat information. Understanding of 
costs to meet future standards for cybersecurity and resilience is needed. In this direction, regulators 
and policy makers could introduce specific regulation with incentives for utilities to work in practical 
and advanced implementations of pilot projects addressed to improve the level of protection and, in 
case of successful attacks, the resilience of the system. 
Moreover, to maintain the integrity and correct operation of the power system is important to adopt 
minimum cybersecurity regulatory standards for all components of the interconnected network. From 
bulk power central generation and transmission, through distribution systems and distributed energy 
resources, to end connection points in buildings and industrial facilities with smart meters and 
electrical equipment with information connections for the “Internet of Things”. 
On the other hand, future power systems with high penetration of DERs are envisioned to have 
features that would be favorable for their resilient operation. For instance, microgrids with distributed 
energy resources and islanding capabilities would be helpful for increase system resilience in case of 
system blackouts. Microgrids with islanding capabilities can provide black-start services and continue 
local operations if the power bulk transmission grid goes down due to a cyber or physical incident. 
Finally, with expanding connection of electric and telecommunications devices, and vastly more 
information become available, privacy is also a growing concern issue. Private personal and corporate 
information is gathered and stored by utilities and their affiliated companies and shared with other 
market participants and interested parties. Specific procedures to protect data breaches and exfiltration 
of information will be needed. For instance, in the EU a General Data Protection Regulation30 has 
been passed that applies to all sectors, including electric utilities. It sets the basic principles for the 
protection of personal data, including security and “privacy by design”. In the electricity sector, DG 
Energy within the European Commission and the Joint Research Centre developed a Data Protection 
Impact Analysis31, a template to help utilities assess smart grids when evaluating privacy and data 
protection issues.  
 
 
24


---

Page 27

---

 
 
 
 
6 
CONCLUSION 
In this paper we have provided visions of how a future with DERs may look like and how DER may 
transform the power sector. The challenges and opportunities that the integration of DERs pose in 
current distribution networks and their implications on the functioning of wholesale and retail markets 
or in cybersecurity and resilience are illustrated with case studies and evidences collected in U.S. and 
Europe. Customers adopting DER technologies, self-providing services and becoming active 
participants in markets, would drive the fundamental transformation. The analyzed challenges ahead 
that would involve a deep reform in our current power systems can be summarized in two main stream 
lines: i) identify and eliminate inefficient technical, economic, and regulatory existing barriers for the 
deployment of DERs, and ii) design a system of economic signals that would create efficiency for the 
combination of both centralized and decentralized resources in a level playing field.  
ACKNOWLEDGEMENTS 
This paper has been written with contributions from members of the MIT Utility of the Future Study, in 
particular I would like to thank Ignacio Perez-Arriaga, Samuel Huntington, Nora Xu, Jose Pablo Chaves, 
Ignacio Herrero, Carlos Batlle, Pablo Rodilla, Max Luke, Jesse Jenkins, Mikael Birk, Cyril Draffin, Pablo 
Dueñas, Karen Tapia-Ahumada, Scott Burger, Ashwini Bharatkumar, Claudio Vergara, Raanan Miller, 
and Richard Tabors. In addition, the contribution of the Delft-Comillas SETS doctoral student Binod 
Koirala is acknowledged as well. 
 
 
25


---

Page 28

---

 
 
REFERENCES 
26


---

Page 29

---

 
 
 
 
1 Further description of the methodology and results can be found in P. Duenas and K. Tapia-Ahumada “Interplay 
of Gas and Electricity Systems at Distribution Level” Utility of the Future Memo Paper. 2016. 
2 U.S. Energy Information Administration, 2015. “Annual Energy Outlook 2015,” Department of Energy, 
Washington, DC 20585, Apr. 2015. 
3 Further description of the methodology and results can be found in N. Xu “Describing Commercial Buildings’ 
Thermal Response and Optimal Cooling Strategy for Provision of Electricity Services” Utility of the Future Memo 
Paper. 2016. 
4 Further description of the methodology and results can be found in S. Huntington “Case study: Battery Storage vs 
Flexible Demand” Utility of the Future Memo Paper.2016. 
5 I.E.A., 2016. Global EV  Outlook, Available at: 
http://www.iea.org/publications/freepublications/publication/Global_EV_Outlook_2016.pdf [Accessed June 14, 
2016]. 
6 Sanchez-Ventura J., “Computing the economic benefits of electric vehicles aggregation” Master Thesis, Comillas 
University, 2016. 
7 Koirala, B. P.; Koliou, E.; Friege, J.; Hakvoort, R. A.; Herder, P. M. Energetic communities for community energy: 
A review of key issues and trends shaping integrated community energy systems. Renew. Sustain. Energy Rev. 
2016, 56, 722–744. 
8 REN21 Renewables 2016 Global Status Report; 2016. 
9 Further description of the methodology and results can be found in Koirala, B.P., Chaves-Avila J.P. “Case Study: 
Integrated Community Energy Systems” Utility of the Future Memo Paper. 2016.  
10 EA Technology, 2012. "Assessing the Impact of Low Carbon Technologies on Great Britain’s Power Distribution 
Networks." Prepared for: Energy Networks Association on behalf of Smart Grids Forum – Work Stream 3, Version: 
3.1. 31st July 2012. Report No: 82530. 
11 German Renewable Energy Sources Act or EEG. 
12 OFGEM, 2013. "Strategy decisions for the RIIO-ED1 electricity distribution price control. Business plans and 
proportionate treatment. Supplementary annex to RIIO-ED1 overview paper." Office of Gas and Electricity 
Markets. 26b/13. 4 March 2013 
13 Further description of the methodology and results can be found in S. Huntington and C. Vergara “Adoption and 
Operation of DERs: Response of Network Users to Economic Signals” Utility of the Future Memo Paper. 2016. 
14 S. Huntington and C. Vergara “Adoption and Operation of DERs: Response of Network Users to Economic 
Signals” Utility of the Future Memo Paper. 2016. 
 
                                                     
27


---

Page 30

---

 
 
 
 
                                                                                                                                                                           
27 M. Birk, J.P. Chaves-Avila, T. Gomez, R. Tabors, “TSO-DSO coordination in a context of distributed energy 
resources penetration” Memo paper of the MIT Utility of the Future Sudy. 2016. 
28 I.J. Pérez-Arriaga, "The transmission of the future: the impact of distributed energy resources on the network". 
IEEE Power and Energy Magazine. vol. 14, no. 4, pp. 41-53, July 2016. 
29 Campbell, Richard J., June 10, 2015, “Cybersecurity Issues for the Bulk Power System”, Congressional Research 
Service, Available at:  www.crs.gov; R43989; 7-5700. 
30 Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the protection of 
natural persons with regard to the processing of personal data and on the free movement of such data, and repealing 
Directive 95/46/EC (General Data Protection Regulation). 
31 Commission Recommendation of 10 October 2014 on the Data Protection Impact Assessment Template for Smart 
Grid and Smart Metering Systems (2014/724/EU). 
28


---

Page 31

---

 
 
 
IEB Working Papers  
2013 
 
2013/1, Sánchez-Vidal, M.; González-Val, R.; Viladecans-Marsal, E.: "Sequential city growth in the US: does age 
matter?" 
2013/2, Hortas Rico, M.: "Sprawl, blight and the role of urban containment policies. Evidence from US cities" 
2013/3, Lampón, J.F.; Cabanelas-Lorenzo, P-; Lago-Peñas, S.: "Why firms relocate their production overseas? 
The answer lies inside: corporate, logistic and technological determinants" 
2013/4, Montolio, D.; Planells, S.: "Does tourism boost criminal activity? Evidence from a top touristic country" 
2013/5, Garcia-López, M.A.; Holl, A.; Viladecans-Marsal, E.: "Suburbanization and highways: when the Romans, 
the Bourbons and the first cars still shape Spanish cities" 
2013/6, Bosch, N.; Espasa, M.; Montolio, D.: "Should large Spanish municipalities be financially compensated? 
Costs and benefits of being a capital/central municipality" 
2013/7, Escardíbul, J.O.; Mora, T.: "Teacher gender and student performance in mathematics. Evidence from 
Catalonia" 
2013/8, Arqué-Castells, P.; Viladecans-Marsal, E.: "Banking towards development: evidence from the Spanish 
banking expansion plan" 
2013/9, Asensio, J.; Gómez-Lobo, A.; Matas, A.: "How effective are policies to reduce gasoline consumption? 
Evaluating a quasi-natural experiment in Spain" 
2013/10, Jofre-Monseny, J.: "The effects of unemployment benefits on migration in lagging regions" 
2013/11, Segarra, A.; García-Quevedo, J.; Teruel, M.: "Financial constraints and the failure of innovation 
projects" 
2013/12, Jerrim, J.; Choi, A.: "The mathematics skills of school children: How does England compare to the high 
performing East Asian jurisdictions?" 
2013/13, González-Val, R.; Tirado-Fabregat, D.A.; Viladecans-Marsal, E.: "Market potential and city growth: 
Spain 1860-1960" 
2013/14, Lundqvist, H.: "Is it worth it? On the returns to holding political office" 
2013/15, Ahlfeldt, G.M.; Maennig, W.: "Homevoters vs. leasevoters: a spatial analysis of airport effects" 
2013/16, Lampón, J.F.; Lago-Peñas, S.: "Factors behind international relocation and changes in production 
geography in the European automobile components industry" 
2013/17, Guío, J.M.; Choi, A.: "Evolution of the school failure risk during the 2000 decade in Spain: analysis of 
Pisa results with a two-level logistic mode" 
2013/18, Dahlby, B.; Rodden, J.: "A political economy model of the vertical fiscal gap and vertical fiscal 
imbalances in a federation" 
2013/19, Acacia, F.; Cubel, M.: "Strategic voting and happiness" 
2013/20, Hellerstein, J.K.; Kutzbach, M.J.; Neumark, D.: "Do labor market networks have an important spatial 
dimension?" 
2013/21, Pellegrino, G.; Savona, M.: "Is money all? Financing versus knowledge and demand constraints to 
innovation" 
2013/22, Lin, J.: "Regional resilience" 
2013/23, Costa-Campi, M.T.; Duch-Brown, N.; García-Quevedo, J.: "R&D drivers and obstacles to innovation in 
the energy industry" 
2013/24, Huisman, R.; Stradnic, V.; Westgaard, S.: "Renewable energy and electricity prices: indirect empirical 
evidence from hydro power" 
2013/25, Dargaud, E.; Mantovani, A.; Reggiani, C.: "The fight against cartels: a transatlantic perspective" 
2013/26, Lambertini, L.; Mantovani, A.: "Feedback equilibria in a dynamic renewable resource oligopoly: pre-
emption, voracity and exhaustion" 
2013/27, Feld, L.P.; Kalb, A.; Moessinger, M.D.; Osterloh, S.: "Sovereign bond market reactions to fiscal rules 
and no-bailout clauses – the Swiss experience" 
2013/28, Hilber, C.A.L.; Vermeulen, W.: "The impact of supply constraints on house prices in England" 
2013/29, Revelli, F.: "Tax limits and local democracy" 
2013/30, Wang, R.; Wang, W.: "Dress-up contest: a dark side of fiscal decentralization" 
2013/31, Dargaud, E.; Mantovani, A.; Reggiani, C.: "The fight against cartels: a transatlantic perspective" 
2013/32, Saarimaa, T.; Tukiainen, J.: "Local representation and strategic voting: evidence from electoral boundary 
reforms" 
2013/33, Agasisti, T.; Murtinu, S.: "Are we wasting public money? No! The effects of grants on Italian university 
students’ performances" 
2013/34, Flacher, D.; Harari-Kermadec, H.; Moulin, L.: "Financing higher education: a contributory scheme" 
2013/35, Carozzi, F.; Repetto, L.: "Sending the pork home: birth town bias in transfers to Italian municipalities" 
2013/36, Coad, A.; Frankish, J.S.; Roberts, R.G.; Storey, D.J.: "New venture survival and growth: Does the fog 
lift?" 
2013/37, Giulietti, M.; Grossi, L.; Waterson, M.: "Revenues from storage in a competitive electricity market: 
Empirical evidence from Great Britain" 


---

Page 32

---

 
 
 
IEB Working Papers  
 
 
2014 
 
2014/1, Montolio, D.; Planells-Struse, S.: "When police patrols matter. The effect of police proximity on citizens’ 
crime risk perception" 
2014/2, Garcia-López, M.A.; Solé-Ollé, A.; Viladecans-Marsal, E.: "Do land use policies follow road 
construction?" 
2014/3, Piolatto, A.; Rablen, M.D.: "Prospect theory and tax evasion: a reconsideration of the Yitzhaki puzzle" 
2014/4, Cuberes, D.; González-Val, R.: "The effect of the Spanish Reconquest on Iberian Cities" 
2014/5, Durán-Cabré, J.M.; Esteller-Moré, E.: "Tax professionals' view of the Spanish tax system: efficiency, 
equity and tax planning" 
2014/6, Cubel, M.; Sanchez-Pages, S.: "Difference-form group contests" 
2014/7, Del Rey, E.; Racionero, M.: "Choosing the type of income-contingent loan: risk-sharing versus risk-
pooling" 
2014/8, Torregrosa Hetland, S.: "A fiscal revolution? Progressivity in the Spanish tax system, 1960-1990" 
2014/9, Piolatto, A.: "Itemised deductions: a device to reduce tax evasion" 
2014/10, Costa, M.T.; García-Quevedo, J.; Segarra, A.: "Energy efficiency determinants: an empirical analysis of 
Spanish innovative firms" 
2014/11, García-Quevedo, J.; Pellegrino, G.; Savona, M.: "Reviving demand-pull perspectives: the effect of 
demand uncertainty and stagnancy on R&D strategy" 
2014/12, Calero, J.; Escardíbul, J.O.: "Barriers to non-formal professional training in Spain in periods of economic 
growth and crisis. An analysis with special attention to the effect of the previous human capital of workers" 
2014/13, Cubel, M.; Sanchez-Pages, S.: "Gender differences and stereotypes in the beauty" 
2014/14, Piolatto, A.; Schuett, F.: "Media competition and electoral politics" 
2014/15, Montolio, D.; Trillas, F.; Trujillo-Baute, E.: "Regulatory environment and firm performance in EU 
telecommunications services" 
2014/16, Lopez-Rodriguez, J.; Martinez, D.: "Beyond the R&D effects on innovation: the contribution of non-
R&D activities to TFP growth in the EU" 
2014/17, González-Val, R.: "Cross-sectional growth in US cities from 1990 to 2000" 
2014/18, Vona, F.; Nicolli, F.: "Energy market liberalization and renewable energy policies in OECD countries" 
2014/19, Curto-Grau, M.: "Voters’ responsiveness to public employment policies" 
2014/20, Duro, J.A.; Teixidó-Figueras, J.; Padilla, E.: "The causal factors of international inequality in co2 
emissions per capita: a regression-based inequality decomposition analysis" 
2014/21, Fleten, S.E.; Huisman, R.; Kilic, M.; Pennings, E.; Westgaard, S.: "Electricity futures prices: time 
varying sensitivity to fundamentals" 
2014/22, Afcha, S.; García-Quevedo, J,: "The impact of R&D subsidies on R&D employment composition" 
2014/23, Mir-Artigues, P.; del Río, P.: "Combining tariffs, investment subsidies and soft loans in a renewable 
electricity deployment policy" 
2014/24, Romero-Jordán, D.; del Río, P.; Peñasco, C.: "Household electricity demand in Spanish regions. Public 
policy implications" 
2014/25, Salinas, P.: "The effect of decentralization on educational outcomes: real autonomy matters!" 
2014/26, Solé-Ollé, A.; Sorribas-Navarro, P.: "Does corruption erode trust in government? Evidence from a recent 
surge of local scandals in Spain" 
2014/27, Costas-Pérez, E.: "Political corruption and voter turnout: mobilization or disaffection?" 
2014/28, Cubel, M.; Nuevo-Chiquero, A.; Sanchez-Pages, S.; Vidal-Fernandez, M.: "Do personality traits affect 
productivity? Evidence from the LAB" 
2014/29, Teresa Costa, M.T.; Trujillo-Baute, E.: "Retail price effects of feed-in tariff regulation" 
2014/30, Kilic, M.; Trujillo-Baute, E.: "The stabilizing effect of hydro reservoir levels on intraday power prices 
under wind forecast errors" 
2014/31, Costa-Campi, M.T.; Duch-Brown, N.: "The diffusion of patented oil and gas technology with 
environmental uses: a forward patent citation analysis" 
2014/32, Ramos, R.; Sanromá, E.; Simón, H.: "Public-private sector wage differentials by type of contract: 
evidence from Spain" 
2014/33, Backus, P.; Esteller-Moré, A.: "Is income redistribution a form of insurance, a public good or both?" 
2014/34, Huisman, R.; Trujillo-Baute, E.: "Costs of power supply flexibility: the indirect impact of a Spanish 
policy change" 
2014/35, Jerrim, J.; Choi, A.; Simancas Rodríguez, R.: "Two-sample two-stage least squares (TSTSLS) estimates 
of earnings mobility: how consistent are they?" 
2014/36, Mantovani, A.;  Tarola, O.; Vergari, C.: "Hedonic quality, social norms, and environmental campaigns" 
2014/37, Ferraresi, M.; Galmarini, U.; Rizzo, L.: "Local infrastructures and externalities: Does the size matter?" 
2014/38, Ferraresi, M.; Rizzo, L.; Zanardi, A.: "Policy outcomes of single and double-ballot elections" 


---

Page 33

---

 
 
 
IEB Working Papers  
 
 
2015 
 
2015/1, Foremny, D.; Freier, R.; Moessinger, M-D.; Yeter, M.: "Overlapping political budget cycles in the 
legislative and the executive" 
2015/2, Colombo, L.; Galmarini, U.: "Optimality and distortionary lobbying: regulating tobacco consumption" 
2015/3, Pellegrino, G.: "Barriers to innovation: Can firm age help lower them?" 
2015/4, Hémet, C.: "Diversity and employment prospects: neighbors matter!" 
2015/5, Cubel, M.; Sanchez-Pages, S.: "An axiomatization of difference-form contest success functions" 
2015/6, Choi, A.; Jerrim, J.: "The use (and misuse) of Pisa in guiding policy reform: the case of Spain" 
2015/7, Durán-Cabré, J.M.; Esteller-Moré, A.; Salvadori, L.: "Empirical evidence on tax cooperation between 
sub-central administrations" 
2015/8, Batalla-Bejerano, J.; Trujillo-Baute, E.: "Analysing the sensitivity of electricity system operational costs 
to deviations in supply and demand" 
2015/9, Salvadori, L.: "Does tax enforcement counteract the negative effects of terrorism? A case study of the 
Basque Country" 
2015/10, Montolio, D.; Planells-Struse, S.: "How time shapes crime: the temporal impacts of football matches on 
crime" 
2015/11, Piolatto, A.: "Online booking and information: competition and welfare consequences of review 
aggregators" 
2015/12, Boffa, F.; Pingali, V.; Sala, F.: "Strategic investment in merchant transmission: the impact of capacity 
utilization rules" 
2015/13, Slemrod, J.: "Tax administration and tax systems" 
2015/14, Arqué-Castells, P.; Cartaxo, R.M.; García-Quevedo, J.; Mira Godinho, M.: "How inventor royalty 
shares affect patenting and income in Portugal and Spain" 
2015/15, Montolio, D.; Planells-Struse, S.: "Measuring the negative externalities of a private leisure activity: 
hooligans and pickpockets around the stadium" 
2015/16, Batalla-Bejerano, J.; Costa-Campi, M.T.; Trujillo-Baute, E.: "Unexpected consequences of 
liberalisation: metering, losses, load profiles and cost settlement in Spain’s electricity system" 
2015/17, Batalla-Bejerano, J.; Trujillo-Baute, E.: "Impacts of intermittent renewable generation on electricity 
system costs" 
2015/18, Costa-Campi, M.T.; Paniagua, J.; Trujillo-Baute, E.: "Are energy market integrations a green light for 
FDI?" 
2015/19, Jofre-Monseny, J.; Sánchez-Vidal, M.; Viladecans-Marsal, E.: "Big plant closures and agglomeration 
economies" 
2015/20, Garcia-López, M.A.; Hémet, C.; Viladecans-Marsal, E.: "How does transportation shape 
intrametropolitan growth? An answer from the regional express rail" 
2015/21, Esteller-Moré, A.; Galmarini, U.; Rizzo, L.: "Fiscal equalization under political pressures" 
2015/22, Escardíbul, J.O.; Afcha, S.: "Determinants of doctorate holders’ job satisfaction. An analysis by 
employment sector and type of satisfaction in Spain" 
2015/23, Aidt, T.; Asatryan, Z.; Badalyan, L.; Heinemann, F.: "Vote buying or (political) business (cycles) as 
usual?" 
2015/24, Albæk, K.: "A test of the ‘lose it or use it’ hypothesis in labour markets around the world" 
2015/25, Angelucci, C.; Russo, A.: "Petty corruption and citizen feedback" 
2015/26, Moriconi, S.; Picard, P.M.; Zanaj, S.: "Commodity taxation and regulatory competition" 
2015/27, Brekke, K.R.; Garcia Pires, A.J.; Schindler, D.; Schjelderup, G.: "Capital taxation and imperfect 
competition: ACE vs. CBIT" 
2015/28, Redonda, A.: "Market structure, the functional form of demand and the sensitivity of the vertical reaction 
function" 
2015/29, Ramos, R.; Sanromá, E.; Simón, H.: "An analysis of wage differentials between full-and part-time 
workers in Spain" 
2015/30, Garcia-López, M.A.; Pasidis, I.; Viladecans-Marsal, E.: "Express delivery to the suburbs the effects of 
transportation in Europe’s heterogeneous cities" 
2015/31, Torregrosa, S.: "Bypassing progressive taxation: fraud and base erosion in the Spanish income tax (1970-
2001)" 
2015/32, Choi, H.; Choi, A.: "When one door closes: the impact of the hagwon curfew on the consumption of 
private tutoring in the republic of Korea" 
2015/33, Escardíbul, J.O.; Helmy, N.: "Decentralisation and school autonomy impact on the quality of education: 
the case of two MENA countries" 
2015/34, González-Val, R.; Marcén, M.: "Divorce and the business cycle: a cross-country analysis" 


---

Page 34

---

 
 
 
IEB Working Papers  
2015/35, Calero, J.; Choi, A.: "The distribution of skills among the European adult population and unemployment: a 
comparative approach" 
2015/36, Mediavilla, M.; Zancajo, A.: "Is there real freedom of school choice? An analysis from Chile" 
2015/37, Daniele, G.: "Strike one to educate one hundred: organized crime, political selection and politicians’ 
ability" 
2015/38, González-Val, R.; Marcén, M.: "Regional unemployment, marriage, and divorce" 
2015/39, Foremny, D.; Jofre-Monseny, J.; Solé-Ollé, A.: "‘Hold that ghost’: using notches to identify manipulation 
of population-based grants" 
2015/40, Mancebón, M.J.; Ximénez-de-Embún, D.P.; Mediavilla, M.; Gómez-Sancho, J.M.: "Does educational 
management model matter? New evidence for Spain by a quasiexperimental approach" 
2015/41, Daniele, G.; Geys, B.: "Exposing politicians’ ties to criminal organizations: the effects of local government 
dissolutions on electoral outcomes in Southern Italian municipalities" 
2015/42, Ooghe, E.: "Wage policies, employment, and redistributive efficiency" 
 
 
2016 
 
2016/1, Galletta, S.: "Law enforcement, municipal budgets and spillover effects: evidence from a quasi-experiment 
in Italy" 
2016/2, Flatley, L.; Giulietti, M.; Grossi, L.; Trujillo-Baute, E.; Waterson, M.: "Analysing the potential 
economic value of energy storage" 
2016/3, Calero, J.; Murillo Huertas, I.P.; Raymond Bara, J.L.: "Education, age and skills: an analysis using the 
PIAAC survey" 
2016/4, Costa-Campi, M.T.; Daví-Arderius, D.; Trujillo-Baute, E.: "The economic impact of electricity losses" 
2016/5, Falck, O.; Heimisch, A.; Wiederhold, S.: "Returns to ICT skills" 
2016/6, Halmenschlager, C.; Mantovani, A.: "On the private and social desirability of mixed bundling in 
complementary markets with cost savings" 
2016/7, Choi, A.; Gil, M.; Mediavilla, M.; Valbuena, J.: "Double toil and trouble: grade retention and academic 
performance" 
2016/8, González-Val, R.: "Historical urban growth in Europe (1300–1800)" 
2016/9, Guio, J.; Choi, A.; Escardíbul, J.O.: "Labor markets, academic performance and the risk of school dropout: 
evidence for Spain" 
2016/10, Bianchini, S.; Pellegrino, G.; Tamagni, F.: "Innovation strategies and firm growth" 
2016/11, Jofre-Monseny, J.; Silva, J.I.; Vázquez-Grenno, J.: "Local labor market effects of public employment" 
2016/12, Sanchez-Vidal, M.: "Small shops for sale! The effects of big-box openings on grocery stores" 
2016/13, Costa-Campi, M.T.; García-Quevedo, J.; Martínez-Ros, E.: "What are the determinants of investment 
in environmental R&D?" 
2016/14, García-López, M.A; Hémet, C.; Viladecans-Marsal, E.: "Next train to the polycentric city: The effect of 
railroads on subcenter formation" 
2016/15, Matas, A.; Raymond, J.L.; Dominguez, A.: "Changes in fuel economy: An analysis of the Spanish car 
market" 
2016/16, Leme, A.; Escardíbul, J.O.: "The effect of a specialized versus a general upper secondary school 
curriculum on students’ performance and inequality. A difference-in-differences cross country comparison" 
2016/17, Scandurra, R.I.; Calero, J.: “Modelling adult skills in OECD countries” 
2016/18, Fernández-Gutiérrez, M.; Calero, J.: “Leisure and education: insights from a time-use analysis” 
2016/19, Del Rio, P.; Mir-Artigues, P.; Trujillo-Baute, E.: “Analysing the impact of renewable energy regulation 
on retail electricity prices” 
2016/20, Taltavull de la Paz, P.; Juárez, F.; Monllor, P.: “Fuel Poverty: Evidence from housing perspective” 
2016/21, Ferraresi, M.; Galmarini, U.; Rizzo, L.; Zanardi, A.: “Switch towards tax centralization in Italy: A wake 
up for the local political budget cycle” 
2016/22, Ferraresi, M.; Migali, G.; Nordi, F.; Rizzo, L.: “Spatial interaction in local expenditures among Italian 
municipalities: evidence from Italy 2001-2011” 
2016/23, Daví-Arderius, D.; Sanin, M.E.; Trujillo-Baute, E.: “CO2 content of electricity losses” 
2016/24, Arqué-Castells, P.; Viladecans-Marsal, E.: “Banking the unbanked: Evidence from the Spanish banking 
expansion plan“ 
2016/25 Choi, Á.; Gil, M.; Mediavilla, M.; Valbuena, J.: “The evolution of educational inequalities in Spain: 
Dynamic evidence from repeated cross-sections” 
2016/26, Brutti, Z.: “Cities drifting apart: Heterogeneous outcomes of decentralizing public education” 
2016/27, Backus, P.; Cubel, M.; Guid, M.; Sánchez-Pages, S.; Lopez Manas, E.: “Gender, competition and 
performance: evidence from real tournaments” 
2016/28, Costa-Campi, M.T.; Duch-Brown, N.; García-Quevedo, J.: “Innovation strategies of energy firms” 
2016/29, Daniele, G.; Dipoppa, G.: “Mafia, elections and violence against politicians” 


---

Page 35

---

 
 
 
IEB Working Papers  
2016/30, Di Cosmo, V.; Malaguzzi Valeri, L.: “Wind, storage, interconnection and the cost of electricity” 
 
 
2017 
 
2017/1, González Pampillón, N.; Jofre-Monseny, J.; Viladecans-Marsal, E.: "Can urban renewal policies reverse 
neighborhood ethnic dynamics?” 


---

Page 36

---

 
Energy Sustainability 
ieb@ub.edu 
www.ieb.edu 
