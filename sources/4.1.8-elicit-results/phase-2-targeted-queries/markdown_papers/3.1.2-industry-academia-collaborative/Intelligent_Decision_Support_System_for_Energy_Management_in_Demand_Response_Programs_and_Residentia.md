# Intelligent Decision Support System for Energy Management in Demand Response Programs and Residential and Industrial Sectors of the Smart Grid

## Paper Metadata

- **Filename:** Intelligent Decision Support System for Energy Management in Demand Response Programs and Residential and Industrial Sectors of the Smart Grid.pdf
- **DOI:** None
- **Authors:** Not available
- **Year:** Not available
- **Journal/Venue:** Not available
- **URL:** Not available
- **Extraction Date:** 2025-06-03T15:04:04.399434
- **Total Pages:** 7

## Abstract

Abstract not available from BibTeX metadata.

## Keywords

Keywords not available from BibTeX metadata.

---

## Full Text Content



### Page 1

See discussions, stats, and author profiles for this publication at: https://www.researchgate.net/publication/224215097
Intelligent Decision Support System for Including Consumers' Preferences in
Residential Energy Consumption in Smart Grid
Conference Paper · October 2010
DOI: 10.1109/CIMSi M.2010.84 · Source: IEEE Xplore
CITATIONS
43
READS
5,781
4 authors, including:
Omid Ameri Sianaki
Victoria University Sydney
28 PUBLICATIONS   611 CITATIONS   
SEE PROFILE
Omar Khadeer Hussain
Australian Defence Force Academy
310 PUBLICATIONS   5,871 CITATIONS   
SEE PROFILE
Azadeh R. Tabesh
Curtin University
5 PUBLICATIONS   134 CITATIONS   
SEE PROFILE
All content following this page was uploaded by Omid Ameri Sianaki on 19 May 2014.
The user has requested enhancement of the downloaded file.

---


### Page 2

Intelligent Decision Support System for Including Consumers’ Preferences in Residential 
Energy Consumption in Smart Grid 
 Omid Ameri Sianaki , Omar Hussain, Tharam Dillon, Azadeh Rajabian Tabesh 
Digital Ecosystem and Business Intelligence Institute 
Curtin University of Technology 
Perth, Australia 
Omid.Ameri Sianaki@postgrad.curtin.edu.au, {O.Hussain, Tharam.Dillon}@cbs.curtin.edu.au, A.Rajabian Tabesh@curtin.edu.au 

Abstract—Smart Grid is a novel initiative the aim of which is 
to deliver energy to the users and also to achieve 
consumption 
efficiency 
by 
means 
of 
two-way 
communication. 
The 
Smart 
Grid 
architecture 
is 
a 
combination of various hardware devices, management and 
reporting software tools that are combined within an ICT 
infrastructure. This infrastructure is needed to make the 
smart grid sustainable, creative and intelligent. One of the 
main goals of Smart Grid is to achieve Demand Response 
(DR) by increasing the end users’ participation in decision 
making and increasing the awareness that will lead them to 
manage their energy consumption in an efficient way. 
Approaches proposed in the literature achieve demand 
response at the different levels of the Smart Grid, but no 
approach focuses on the users’ point of view at the home 
level on a continuous basis and in an intelligent way to 
achieve demand response. In this paper, we develop such an 
approach by which demand response can be achieved on a 
continuous basis at the home level. To achieve this, the 
dynamic notion of price will be utilized to develop an 
intelligent decision-making model that will assist the users in 
achieving demand response. 
I. 
INTRODUCTION 
 It is estimated that the global demand for energy will rise 
by 44 percent by the year 2030 [1]. As shown in Figure 1, 
in order to meet that demand, renewable sources of energy 
are the fastest-growing source of world energy, with 
consumption increasing by 3.0 percent per year; 
meanwhile, this rate is 1.7 % for coal and 2.1 % for natural 
gas [2]. This is in accordance with the trend where the 
dependence on resources to meet the energy demand is 
shifting from non-renewable to renewable sources to 
utilize green energy. Consequently, with such a shift, the 
costs of upgrading the old electricity delivery system, 
pricing and service networks have risen as these systems 
have the traditional supply-side options and an inadequate 
central capacity plan to meet the growing demand and 
energy shift. The new system demands a framework in 
which people, systems, solutions, and business processes 
are dynamic and flexible in responding to changes in 
technology, customer needs, prices, standards, policies, 
and other requirements [3]. This is achieved by the notion 
of Smart Grid. Smart Grid is an electricity network that 
can intelligently integrate the actions of all users connected 
to it in order to efficiently deliver sustainable, economic 
and secure electricity supplies [4]. 
 
Figure 1. The use of all energy sources increases over the time frame of 
the IEO2009 reference case [2]. 
 In this system, the consumers simultaneously consume 
the energy from different sources and at the same time 
produce it to return it to the grid or use it during peak 
times. The need for two-way communication between the 
utility and its customers lies at the heart of all Smart Grid 
initiatives. In this fashion, both parties work synergistically 
to manage the cost, delivery and environmental impact of 
power generation and energy services delivery. But to 
achieve energy efficiency, apart from having such 
architecture, mechanisms are needed that add intelligence 
to it at different levels. Such added intelligence varies 
according to the level at which it is being considered. For 
example, if considered from the generation side, one of the 
areas in which intelligence has to be added is dynamic 
pricing; whereas, from the consumer’s perspective, it may 
be in the efficient utilization of energy at home level based 
on the price. This is supported by Schneider Electric which 
states that energy management needs intelligence not only 
to reduce energy consumption, but also to reduce 
operational costs [5]. Once developed, the approaches will 
add intelligence at the home level and will encourage 
customers to change their energy consumption behaviour 
in order to achieve energy efficiency. It has been 
mentioned in the literature that consumers are ready to 
change when they are presented with the appropriate 
information, but they lack the data or tools to do so [6]. 
Therefore, we need an approach by which we can 
investigate, identify and address the issues which arise for 
the consumers, and which adds intelligence for efficient 
and smart energy consumption in line with the real costs 
and 
environmental 
impact 
which 
will 
encourage 
consumers to utilize energy efficiently. We aim to achieve 
that in this paper by developing an intelligent decisionmaking support system at the smart home level in Smart 
 
Second International Conference on Computational Intelligence, Modelling and Simulation
978-0-7695-4262-1/10 $26.00 © 2010 IEEE
DOI 10.1109/CIMSi M.2010.84
136
Second International Conference on Computational Intelligence, Modelling and Simulation
978-0-7695-4262-1/10 $26.00 © 2010 IEEE
DOI 10.1109/CIMSi M.2010.84
154
Second International Conference on Computational Intelligence, Modelling and Simulation
978-0-7695-4262-1/10 $26.00 © 2010 IEEE
DOI 10.1109/CIMSi M.2010.84
154

---


### Page 3

Grid that works on behalf of the consumers, according to 
their consumption profile and utilities and leads them to 
the efficient utilization of energy. The paper is organized 
as follows. In Section II, we will discuss the literature 
relevant to the Smart Grid and Demand Response. In 
Section III, we will identify the issue that needs to be 
added. In Sections IV and V we propose an intelligent 
decision support system to achieve demand response at the 
home level. In Section VI, we conclude the paper. 
II. 
LITERATURE REVIEW 
A. Smart Grid 
 The initiatives taken in the form of smart grids are to 
shift the pattern of energy consumption from nonrenewable to renewable sources and to make the 
consumers equal participants in the process of tuning and 
shifting their energy consumption to clean resources [9]. 
The concept of Smart Grid aims to use electricity more 
efficiently, support “green” sources and bring intelligence 
and standardization to the way that energy is transmitted, 
distributed, managed and consumed. A survey of the 
literature allows us to identify the various main elements 
of Smart Grid as shown in Figure2. 
 
Figure 2. Smart Grid Architecture Concept 
 
 At the micro level, from the viewpoint of a smart 
home, there are various sophisticated ubiquitous electronic 
devices with the ability to communicate with each other 
and with a smart meter. Smart meters are microprocessorbased 
devices 
providing 
two-way 
communications 
capability, and will help home owners to manage their 
electricity usage. Through a website, for example, or a 
customer portal, parameters as to when loads in the home 
turn on and off, based on the price of electricity, could be 
set. The dishwasher, for instance, could be loaded and set 
to stand-by until the price of energy is below a certain 
level – typically off peak – when it would start 
automatically [8]. The aim of a smart meter is to act as a 
central point connecting all such internal devices with the 
outside world. The smart meters integrate data collected 
from the meters into billing, customer service, field 
services and energy-demand management. This gives a 
real-time view into a greater volume of data at a more 
granular level, leading to faster analysis and better 
decision-making regarding capacity demand, and the 
carrying out of other business processes. At smart home 
level, the Smart Grid, apart from providing detailed 
information about consumption of electricity to both users 
and network operators for preventing electricity wastage, 
also enables renewable energy resources to be connected 
to the grid [10]. A fully interactive ICT infrastructure is 
needed that helps to support the complex communication 
of business processes. Already, a number of initiatives 
propagate the use of such ICT techniques at the device 
level. For example, the concept of Internet of Things has 
been proposed that enables and facilitates wireless 
communication between different devices across the Smart 
Grid. Zig Bee Smart Energy Home Area Network (HAN) 
Device Communications and Information Model provide 
secure, easy-to-use wireless home area networks for 
managing energy. The IPSO alliance [11] is supporting 
and promoting IP as a protocol for smart objects, creating 
the "Internet of Things” infrastructure where the Web 
standards are used to connect and to integrate the smart 
appliances for accessing their functionality. Google [7] 
presents Google Power Meter which receives information 
from utility smart meters and energy management devices 
and provides customers with access to their home 
electricity consumption on their personal i Google 
homepage. Industries are working on supports for the IP 
protocol for wireless communication standards for home 
automation, such as Zig Bee, Z-Wave [8], IEEE 802.15.4 
and ANSI C12 [9]. For interoperability and seamless 
communication 
between 
different 
devices 
and 
architectures, researchers have proposed the utilization of 
either SOA or Ontology in Smart Grid. For example, 
ٌWood et al. [10] proposed an approach for advanced 
energy consumption displays (ECDs) in the home. Koen et 
al. [11] developed a concept that seriously considers smart 
homes and buildings as proactive customers (prosumers) 
that negotiate and collaborate as an intelligent network in 
close interaction with their external environment. Warmer 
et al. [8] proposed that an intelligent networked 
collaboration of homes relied on Information and 
Communication 
Technologies 
(ICT) 
to 
address 
interactions both within the smart house as well as between 
the smart houses, the Smart Grid and the enterprises. They 
found that IP-based technologies, and service-oriented 
approaches in particular, such as Web services, are 
required to interconnect all of the Smart Grid components 
when an information dissemination and exploitation is to 
coincide in an open and interoperable way. The aim of 
integrating such ICT technologies into the Smart Grid is to 
enable the efficient communication of information among 
different devices and sources that help to achieve Demand 
Response for efficient utilization of energy. 
B. Demand Response 
 Demand Response (DR) activities are defined as 
“actions voluntarily taken by a consumer to adjust the 
amount or timing of his energy consumption”. Actions are 
generally in response to an economic signal (e.g. energy 
price, or government and/or utility incentive) [12]. 
Demand Response is a reduction in demand designed to 
reduce peak demand or avoid system emergencies. Hence, 
Demand response can be a more cost-effective alternative 
than adding generation capabilities to meet the peak and or 
137
155
155

---


### Page 4

occasional demand spikes [13]. The underlying objective 
of DR is to actively engage customers in modifying their 
consumption in response to pricing signals. The goal is to 
reflect supply expectations through consumer price signals 
or controls and enable dynamic changes in consumption 
relative to price. According to the literature, much work 
has been done to achieve demand response. For example, 
Bilton et al. [14] explore the diversity of timescales, types 
of signals and involvement of customers in different types 
of demand side action. Earle et al. [13] proposed an 
approach for measuring the capacity impacts of demand 
response by California SPP and found that the uncertainty 
of the level of response is likely to have little effect on the 
capacity and reliability value of these demand response 
programs. Faruqui et al. [15] present a methodology for 
quantifying the benefits to customers and utilities of 
dynamic pricing programs and also proposed another 
approach [16] for quantifying customer response to 
dynamic pricing. Irastorza [17] believes more sophisticated 
metering and communications technologies are now 
economically feasible for many more customers, allowing 
for rate designs that provide improved economic 
efficiency, transparency, simplicity and fairness, and allow 
customers to make efficient energy choices. Kuhn [18] 
believes that advances such as ‘‘smart’’ meters, two-way 
communication, and automation technology are rapidly 
improving information exchange between utilities and 
their customers, and enabling further energy efficiency 
gains. Faruqui et al. have proposed a variety of rates 
including critical peak periods (CPP), peak-time rebate 
(PTR), and time of use (TOU) to demonstrate how benefits 
vary based on rate design. Earle et al. [13] proved that 
increased flexibility in program design as well as programs 
complementary to CPP/PTR could greatly increase their 
value. Discussions of CPP/PTR programs show that these 
tend to have fixed hours for critical peak periods and a 
limited number of days in which they occur. This is 
because rate designers and regulators are concerned 
whether consumers are able to understand and react to 
dynamic prices. Sezgen et al. [19] demonstrated how 
option-pricing methodologies can be used to value 
investments in three different kinds of demand-response 
strategies and they stated that enabling technologies and 
information/ analysis tools are essential for customers to 
assess the risks and value of participating in energy 
markets. Borenstein et al. [20] argued that participants in 
an RTP tariff must gain access to their own usage data in 
order to develop an understanding of how the facility 
responds to one or more load reduction actions. Since few 
customers have knowledge of the load shape patterns of 
their cumulative monthly usage, any decision to participate 
in an RTP tariff should be preceded by a period of time in 
which the customer’s usage data are available through the 
metering and telecommunication system and a customer 
most likely will require some software package with which 
to assess the information and make sense of it. Kilanc et al. 
[21] developed a decision support tool for the analysis of 
pricing, investment and regulatory processes in a 
decentralized electricity market where public regulators 
and power companies are potential users of the model, for 
learning and decision support in policy design and 
strategic planning. Sancho et al. [22], describe software 
which could be used as a decision support tool for decision 
makers in competitive electricity markets. The main aim of 
their work is to simulate the way that the competitive 
electricity market functions by means of simple offers in 
the daily market. Sueyoshi et al. [23] developed an 
application software for analyzing and understanding a 
dynamic price change in the US wholesale power market. 
Traders can use the software as an effective decisionmaking tool by modeling and simulating a power market. 
E. M. R. Mike et al. [24] propose innovative electric power 
architecture, rooted in lessons learned from the Internet 
and microgrids, which addresses these problems while 
interfacing seamlessly into the current grid to allow for 
non-disruptive incremental adoption. Mayor et al. [25] 
believe that the future of power grids is expected to 
involve an increasing level of intelligence and integration 
of new information and communication technologies in 
every aspect of the electricity system, from demand-side 
devices to wide-scale distributed generation to a variety of 
energy markets. But by considering the structure of the 
Smart Grid, all of the abovementioned approaches aim to 
achieve demand response either at the generation level or 
transmission level. 
III. 
NEED TO ACHIEVE DEMAND RESPONSE AT THE 
END-USER LEVEL 
 The approaches proposed in the literature consider the 
different areas of energy generation and transmission to 
achieve demand response. However, less progress has been 
made to achieve DR effectiveness on the customer-side. 
By customer-side, we mean at each home level. As each 
user has to play its own active part in order to achieve DR, 
we need a system that captures the user’s preference and 
behaviour and then assist it in changing its consumption 
behaviour according to the dynamic notion of price - and 
achieve DR; such an intelligent approach is missing in the 
literature. This is different from the other areas of Smart 
Grid that have efficient techniques to achieve demand 
response. Therefore, the primary issues that have been 
identified in the literature and which we intend to address 
are: 
a) No approach has been proposed by which 
consumers’ preferences and consumption profiles are 
considered for efficient utilization of energy. 
b) Much research has been done to achieve demand 
response and price efficiency [13, 26-29]. But none has 
proposed a solution for studying the effectiveness of such 
systems when customers are not well trained, unwilling or 
too passive to respond to price signals, resulting in an 
increase in demand. To overcome this, we need an 
intelligent decision-making support system (IDSS) that 
assists in the decision-making process by considering 
customers’ criteria for demand response. 
c) Significant researches have highlighted the 
benefits of using renewable sources of energy and also 
integrating it with the local grid [30-34]. But no approach 
has been proposed that encourages the customers to 
increase 
their 
use 
of 
renewable 
sources 
and 
simultaneously shift their dependence on them and later 
autonomously trade off the energy with the local grid on 
behalf of the customers in a dynamic pricing system. 
138
156
156

---


### Page 5

d) Many researchers present alternative interfaces, 
such as Energy-orb or Web interfaces like Wattson and 
Holmes, for sending information to customers to assist 
them in making decisions. In most of these approaches, 
the customers should be trained in the use of these 
interfaces and subsequently be able to react and send 
feedback to these signals. But instead of such interfaces, 
the IDSS needs to be able to make decisions on behalf of 
the customers and to increase the reliability of the service 
and customer management and consequently the Smart 
Grid. 
e) Many researchers have presented solutions for 
decreasing the consumption of energy by forcing the end 
users to switch off the appliances or postpone their energy 
consumption. But none of them proposes an approach by 
which the users can have different alternatives which 
allow 
them 
to 
achieve 
what 
they 
want 
while 
simultaneously reducing the consumption of energy. The 
absence of such an approach means that end users will be 
unable to achieve demand response in an intelligent way. 
IV. 
DEMAND RESPONSE AND END-USERS PREFERENCES 
FOR EFFICIENT CONSUMPTION OF ENERGY 
 An effective approach for achieving demand 
response requires techniques at the consumption level too. 
This is done by having an intelligent framework at the 
consumption side. For example, at home level, input is 
taken from the grid and, depending on various underlying 
factors, the framework assists the consumer to achieve 
demand response. There are no related works in the 
literature in this regard but the importance of such work 
has been discussed by Hopper et al. [27] who state that 
there is a role for targeted technical assistance programs to 
help customers to develop more sophisticated price 
response strategies as shown in Figure 3. There is a utility 
provider which sends price signals to end-users and 
receives the consumption information by means of a smart 
meter and wireless communication of the sensors (smart 
appliances). 
 
Figure 3. Intelligent Decision Support System for Energy Efficiency 
Consumption by End Users 
 The consumer mutually receives some information from 
the utility provider about consumption profile and price 
signals from various portals. It is expected that, by 
receiving consumption information, the consumers will 
change their consumption behaviour in order to mitigate 
cost and save on their power bill. However, in a dynamic 
pricing system, the consumers have no way of knowing 
whether their decision to modify their energy consumption 
is effective and efficient. This is overcome by adding 
intelligence at each home level. In this paper, we will 
develop a model by which such intelligence is added at 
each home level on a continuous basis by which demand 
response is achieved. We will propose our model in the 
next section. 
V. 
INTELLIGENT DECISION SUPPORT SYSTEM MODEL 
 To achieve more effective demand response on the enduser side, we utilize the dynamic notion of price and 
develop an intelligent decision support system model that 
will assist demand response as shown in Figure 4. 
 
Figure 4. Intelligent decision support system model for achieving 
Demand Response in home level 
 This model is achievable by utilizing four steps as 
depicted in Table I. The first step is to determine the 
effective variables and parameters required for achieving 
the objectives of the next steps. By analyzing the variables, 
the 
variety 
of 
variables 
(qualitative, 
quantitative, 
dependent, independent, exogenous, endogenous) will be 
specified and then relationships and effects of the variables 
on each other should be clarified. For example, when 
consumers prepare to use the A/C, variables such as the 
inside and outside temperatures or the level of humidity 
will influence their preferred A/C settings; another factor 
to consider is that there may be several occupants in a 
house, whose preferences may be different. Residents are 
able to alert the system of their existence in a different way 
such as smart cards. In the second step, a user interface 
will capture the consumers’ inputs on the identified 
variables and preferences in different scenarios that will 
provide an input to the learning phase and also inform the 
consumers about the result of the computed decision and 
let them modify the parameters according to their 
preferences. 

139
157
157

---


### Page 6

TABLE I. 
FOUR STEPS FOR MODEL UTILIZATION 
 
Step 3 has a two-fold purpose. The first is to capture the 
outside variables like price signal from the grid, 
environmental conditions and available renewable sources. 
Once that is done, the second is to utilize that information 
and develop a fuzzy rule based on the Fuzzy Multi Criteria 
Decision Making (MCDM) model that will assist the 
consumer to achieve demand response. MCDM methods 
include two techniques. One is a Multi Objective Decision 
Making (MODM) technique which will apply when the 
system objectives are different. In this case, when the 
objective is cost reduction, the system behaviour is 
different, whereas the system objective is to maintain 
lifestyle. The second is a Multi Attribute Decision Making 
(MADM) technique that will apply when there are many 
decision makers in the system and their decision should be 
considered in the decision-making process. According to 
the nature of variables such as temperature, price, comfort 
and economical consumption etc. and also considering the 
core meaning of variables and accurate communication 
between users and system, the Fuzzy techniques will 
develop terms most appropriate for this model. In this step, 
feedback (shown as number 2 in the model) is included in 
terms of addressing any changes in user behaviour or 
preferences and any event will be recognized by the model 
and will create a learning model to adapt to such events 
and changes. In Step 4, where a neural network model is 
developed, we expect to learn about the fuzzy rule-based 
and consumption pattern based on the preliminary data 
obtained in Step 2 and fuzzy MCDM in step three. Such a 
model will be responsible for acting autonomously on 
behalf of the user and in turn facilitates the decisionmaking process. Such a model will evolve on a continuous 
basis when the users modify their preferences in different 
scenarios. In order to develop a model that captures 
various terms of cost function for different classified 
consumption patterns, the neural networks techniques will 
be utilized to derive meaning from complicated or 
imprecise data and can be used to extract consumption 
patterns and detect trends that are too complex to be 
noticed by computers. In neural networks, the learning 
scheme 
is 
divided 
into 
supervised 
learning 
and 
unsupervised learning[35]. At first, when the system is 
going to recognize patterns or features in data sets, which 
include the correct output for each input, supervised 
learning will apply and then after capturing the data, an 
unsupervised learning technique will be applicable so that 
the system can act on its own in a kind of self-reflection, 
for this purpose a feedback (shown as number 1 in the 
model) is considered for identifying and capturing new 
emerged variables in terms of any consumer behaviour 
modification. 
VI. 
 CONCLUSION 
 The Smart Grid is a novel initiative the aim of which 
is to increase energy efficiency and decrease energy 
wastage from electricity generation to consumption. 
Various architectures and technologies are needed at 
different levels to achieve these goals. One of them is 
demand response that has to be achieved at the 
consumption side. In this paper, we developed an 
intelligent decision supporting system model at home level 
for increasing the efficiency of energy consumption in the 
Smart Grid. This system, which will be installed in 
conjunction with a smart meter, will adapt to consumers’ 
preferences and be compatible with demand response in 
the Smart Grid. The analysis of our proposed approach 
will be according to the end users’ utilities and aims to 
urge them to increase their consumption of renewable 
sources of energy and decrease the consumption of nonrenewable sources. 
The major significances and contributions that arise 
from this model are: 
a. It will increase the efficiency and flexibility of the 
Smart Grid by which energy is utilized efficiently at home 
level, thereby transforming it into a smart home. This is 
different from the concepts of smart home that have been 
proposed in the literature which focus mainly on 
improving the lifestyle of the users. 
b. It will enable a user to be actively involved in the 
process of achieving demand response at the consumption 
side. This is different from the existing approaches 
proposed in the literature which aim to achieve demand 
response at the consumption level either by voluntary load 
shedding or by price response only when the energy 
demand reaches the maximum peak of the grid. 
c. A knowledge base is formed after capturing the 
users’ various preferences and characteristics and this 
helps it to act autonomously on the users’ behalf to achieve 
demand response. If any change or variation in the user’s 
behaviour and preference is determined, then the 
knowledge base is updated automatically. 
d. Depending on the different characteristics and 
preferences of the users and the energy price, the proposed 
IDSS determines the various alternatives such as deciding 
on the source from which the energy demand can be met or 
the level of importance according to which the energy 
demand of the different devices has to be met. 
e. It will greatly contribute to knowledge about ways to 
improve energy efficiency since currently no work has 
been proposed in the literature that can be applied to 
achieving demand response at the consumption level by 
proactively involving the users. 
 We believe that this model will support end-users to 
adapt their consumption with dynamic pricing and to 
enable them to respond more intelligently to achieve 
demand response. 
Step 1: To identify the different types of variables that need to be 
captured for studying the consumer’s preferences and consumption 
profile. 
Step 2: To develop a user interface for capturing the consumers’ 
inputs on the identified variables and preferences 
Step 3: To capture the outside variables like price signal from the 
grid, environmental conditions and available renewable sources and 
then to utilize that information and develop a Fuzzy Multi Criteria 
Decision Making model that will assist the consumer to achieve 
demand response 
Step 4: To develop a neural-network-based model that learns about 
the consumer’s preferences and consumption profile based on the 
preliminary data obtained from Step 2. 
140
158
158

---


### Page 7

VII. REFERENCES 
[1] 
 T. Reuters, "Global energy demand seen up 44 percent by 
2030: EIA." vol. 2009, A. R. Tom Doggett Ed.: Thomson 
Reuters , 2009. 
[2] 
 U. S. EIA, "World Energy and Economic Outlook ". vol. 
2010: EIA, 2010. 
[3] 
 A. Vojdani, "Smart Integration," ieee power & energy 
magazine, 2008. 
[4] 
 P. Nabuurs, "Strategic Deployment Document For 
Eoroupe 's Elictricity Networks of the Future," N.V. KEMA, 
Draft September 2008. 
[5] 
 S. Electric, "Leading the way in energy efficiency." vol. 2009: 
Schneider, 2009. 
[6] 
 J. Torriti, M. G. Hassan, and M. Leach, "Demand response 
experience 
in 
Europe: 
Policies, 
programmes 
and 
implementation," Energy, vol. In Press, Corrected Proof, 26 
May 2009. 
[7] 
 Google, "Google Power Meter," 2009. 
[8] 
 C. Warmer, K. O. K. Koen, S. Karnouskos, A. Weidlich, D. 
Nestle, P. Selzam, J. Ringelstein, A. Dimeas, and S. 
Drenkard, "Web services for integration of smart houses in 
the smart grid," 2009. 
[9] 
 E. Miller, "Renewables and the smart grid," Renewable 
Energy Focus, vol. 10, pp. 67-69, 2009. 
[10] 
 G. Wood and M. Newborough, "Energy-use information 
transfer for intelligent homes: Enabling energy conservation 
with central and local displays," Energy and Buildings, vol. 
39, pp. 495-503, 2007. 
[11] 
 K. O. K. Koen, S. Karnouskos, D. Nestle, A. Dimeas, A. 
Weidlich, C. Warmer, P. Strauss, B. Buchholz, S. Drenkard, 
and N. Hatziargyriou, "SMART HOUSES FOR A SMART 
GRID," in 20th International Conference on Electricity 
Distribution Prague, 2009. 
[12] 
 Ind Eco,"Demand side management and demand response in 
municipalities," Ind Eco Strategic Consulting Inc, Toronto 27 
January 2004 
[13] 
 R. Earle, E. P. Kahn, and E. Macan, "Measuring the Capacity 
Impacts of Demand Response," The Electricity Journal, vol. 
22, pp. 47-58, 2009. 
[14] 
 R. C. Bilton M, Leach M, Devine Wright H, Johnstone C, 
Kirschen D, ‘‘Demand Side Management’’ in delivering a 
low carbon electricity system:technologies, economics and 
policy. Cambridge: Cambridge University Press. 
[15] 
 A. a. L. W. Faruqui, "Quantifying the Benefits Of Dynamic 
Pricing In the Mass Market," Edison Electric Institute, 
Washington, D.C. January 2008. 
[16] 
 A. Faruqui and S. George, "Quantifying Customer Response 
to Dynamic Pricing," The Electricity Journal, vol. 18, pp. 5363, 2005. 
[17] 
 V. Irastorza, "New Metering Enables Simplified and More 
Efficient Rate Structures," The Electricity Journal, vol. 18, 
pp. 53-61, 2005. 
[18] 
 T. R. Kuhn, "Energizing Efficiency's Potential," The 
Electricity Journal, vol. 19, pp. 83-87, 2006. 
[19] 
 O. Sezgen, C. A. Goldman, and P. Krishnarao, "Option value 
of electricity demand response," Energy, vol. 32, pp. 108119, 2007. 
[20] 
 S. Borenstein, M. Jaske, and A. Rosenfeld, "Dynamic pricing, 
advanced metering and demand response in electricity 
markets" UC Berkeley: Center for the Study of Energy 
Markets. 
Retrieved 
from: 
http://www. 
escholarship. 
org/uc/item/11w8d6m4, 2002. 
[21] 
 G. Pasaoglu Kilanc and I. Or, "A decision support tool for the 
analysis of pricing, investment and regulatory processes in a 
decentralized electricity market," Energy Policy, vol. 36, pp. 
3036-3044, 2008. 
[22] 
 J. Sancho, J. Sánchez-Soriano, J. A. Chazarra, and J. 
Aparicio, "Design and implementation of a decision support 
system for competitive electricity markets," Decision Support 
Systems, vol. 44, pp. 765-784, 2008. 
[23] 
 T. Sueyoshi and G. R. Tadiparthi, "An agent-based decision 
support system for wholesale electricity market," Decision 
Support Systems, vol. 44, pp. 425-446, 2008. 
[24] 
 E. M. R. Mike M. He, Xiaofan Jiang "An Architecture for 
Local Energy Generation, Distribution, and Sharing," in 
IEEE Energy 2030 Atlanta, Georgia, USA, 2008. 
[25] 
 D. Coll-Mayor, M. Paget, and E. Lightner, "Future intelligent 
power grids: Analysis of the vision in the European Union 
and the United States," Energy Policy, vol. 35, pp. 24532465, 2007. 
[26] 
 A. Faruqui, R. Hledik, and J. Tsoukalis, "The Power of 
Dynamic Pricing," The Electricity Journal, vol. 22, pp. 4256, 2009. 
[27] 
 N. Hopper, C. Goldman, and B. Neenan, "Demand Response 
from Day-Ahead Hourly Pricing for Large Customers," The 
Electricity Journal, vol. 19, pp. 52-63, 2006. 
[28] 
 P. C. Honebein, R. F. Cammarano, and K. A. Donnelly, "Will 
Smart Meters Ripen or Rot? Five First Principles for 
Embracing Customers as Co-Creators of Value," The 
Electricity Journal, vol. 22, pp. 39-44, 2009. 
[29] 
 M. Hinnells, "Technologies to achieve demand reduction and 
microgeneration in buildings," Energy Policy, vol. 36, pp. 
4427-4433, 2008. 
[30] 
 I. Stadler, "Power grid balancing of energy systems with high 
renewable energy penetration by demand response," Utilities 
Policy, vol. 16, pp. 90-98, 2008. 
[31] 
 T. J. Hammons, "Integrating renewable energy sources into 
European grids," International Journal of Electrical Power & 
Energy Systems, vol. 30, pp. 462-475, 2008. 
[32] 
 T. M. Lenard, "Renewable Electricity Standards, Energy 
Efficiency, and Cost-Effective Climate-Change Policy," The 
Electricity Journal, vol. 22, pp. 55-64, 2009. 
[33] 
 I. M. de Alegría Mancisidor, P. Díaz de Basurto Uraga, I. 
Martínez de Alegría Mancisidor, and P. Ruiz de Arbulo 
López, "European Union's renewable energy sources and 
energy efficiency policy review: The Spanish perspective," 
Renewable and Sustainable Energy Reviews, vol. 13, pp. 100114, 2009. 
[34] 
 R. Wiser, C. Namovicz, M. Gielecki, and R. Smith, "The 
Experience with Renewable Portfolio Standards in the United 
States," The Electricity Journal, vol. 20, pp. 8-20, 2007. 
[35] 
 A. Mellit and S. A. Kalogirou, "Artificial intelligence 
techniques for photovoltaic applications: A review," Progress 
in Energy and Combustion Science, vol. 34, pp. 574-632, 
2008. 
141
159
159
View publication stats

---
