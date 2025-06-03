

---

Page 1

---

	
M. Lamagna, et al., Int. J. of Energy Prod. & Mgmt., Vol. 6, No. 4 (2021) 323–334
© 2021 WIT Press, www.witpress.com
ISSN: 2056-3272 (paper format), ISSN: 2056-3280 (online), http://www.witpress.com/journals
DOI: 10.2495/EQ-V6-N4-323-334
A COMPREHENSIVE REVIEW ON DIGITAL TWINS FOR 
SMART ENERGY MANAGEMENT SYSTEM
MARIO LAMAGNA, DANIELE GROPPI, MEYSAM M. NEZHAD & GIUSEPPE PIRAS
Department of Astronautic, Electrical and Energy Engineering of Sapienza University of Rome, Italy.
ABSTRACT
Energy systems digitalisation represents the energy sector’s future, and Digital Twins represent the 
most advanced and complete way to monitor and optimally manage a complex system such as the 
upcoming solutions. Those latter will comprehend several energy generators, traditional and/or from 
renewable energy sources (RESs), different energy storage systems using several energy vectors and 
that interconnect different energy-consuming sectors (power, thermal, transport sectors) and that fully 
exploit the potential synergies offered by such interconnected system. Nevertheless, since the first 
conceptualisation of digital twins in the first years of the 21st century, its use has not started yet for dif­
ferent reasons that are affecting the adoption of this game-changer approach. Hence, what are the main 
barriers that are holding back the adoption of digital twins in smart energy systems? The present review 
paper answers this research question while discussing the case studies that can be found in literature 
and analysing the different approaches and the system architectures that have been tested or simply 
idealised. This paper provides a basis for future research that aims at applying the digital twin concept 
in the energy sector and particularly for power grid management. It deals with the challenges of big 
data management, the ones related to real-time measurements and continuous communication between 
the real-world system and its digital twin, the investment for measuring systems, the issues connected 
with the use of large data centres and the correlated energy-related challenges and doubts. The review 
analyses the challenges that have been encountered so far, the proposed solutions and the opportunities 
that such a ‘work in progress’ topic offers.
Keywords: barriers, digital twin, energy systems, modelling, real-time analyses.
1  INTRODUCTION
Today’s energy system architecture is turning toward a massive electrification of consumptions 
and renewable energy source (RES) penetration [1]. In this regard, it is key to rely on technolo­
gies able to monitor and coordinate the energy fluxes, expressed in terms of demand and 
production. In the real world, this technology is translated into a series of sensors installed in the 
system that feed databases and algorithms dedicated to analysing the different fluctuations at 
any time. Furthermore, this is also coupled with the ability to predict the possible variations in 
future conditions, so as to be able to promptly adapt the operating technologies accordingly [2].
The digital twin (DT) concept, introduced by Micheal Grieves, reflects this idea which is 
fundamental to support the future energy system [3]. According to Grieves, the DT system is 
based on three concepts: physical products in real space, virtual products in virtual space and 
the connections of data and information that connect the physical and virtual space [4].
Such a system will be able to mirror the behaviour of the object in the real environment. 
The data availability assures a high-fidelity model, and by combining all of this information, 
compared also with the history data, the DT can forecast and predict the system response in 
different possible future scenarios [5]. The prediction is fundamental to maintain our system 
working efficiently and in safe conditions. Additionally, there are also hybrid DT versions 
where parts of the parameters are not evaluated by sensors; instead, they come directly from 
the model itself.
The operators working in the energy field understand the potential offered by this approach. 
For instance, although the investment in electricity grids has decreased by 7% from 2018, 


---

Page 2

---

324	
M. Lamagna, et al., Int. J. of Energy Prod. & Mgmt., Vol. 6, No. 4 (2021) 
investment in digital twinning technologies, including the required advanced metering infra­
structure, utility automation and artificial intelligence, made up more than 15% of total grid 
spending [6].
Digital technologies are arising and develop faster than other technologies used in the 
power system [7]. Gartner has plotted the key digital technologies in the hype-cycle curve, 
reported in Fig. 1, to enable an assessment of the expectations of these technologies [8].
Although substation automation has been a trend in recent years [9], in 2019, utilities 
expanded the use of software platforms to monitor and control them, notably through DTs. 
National grid operators partnered with data management utilities and sensor manufacturers to 
create grid and energy systems twins, mapping power flow, voltage and infrastructure from 
substations to homes [10]. The American Electric Power Authority also announced the digital 
twinning of its transmission infrastructure [11]. From Gartner work, the high expectations 
placed on DT technologies are clear. Nevertheless, it is expected that they could reach a sat­
isfactory level of productivity and common use in our everyday life only in a period varying 
from 5 to 10 years from 2018 [8]. The scope of this review is to analyse the possible barriers 
hampering the DT technologies to reach their productivity plateau and, at the same time, 
illustrate the positive results already obtained. In so doing, particular attention will be paid to 
the energy sector as a whole and energy management systems and power grids that have to 
communicate and interoperate with homes and transport. The review discussion will be 
organised in five sections, concerning five different but nevertheless complementary aspects:
•  Functioning/operative technologies
•• Power grid
•• Energy systems
•• Buildings
•  Transport
Figure 1: Hype cycle (source: Gartner 2018 [8]).


---

Page 3

---

	
M. Lamagna, et al., Int. J. of Energy Prod. & Mgmt., Vol. 6, No. 4 (2021) 
325
2  DISCUSSION
In this paragraph, the five sections will be dealt with in specific chapters. Each of those has 
been analysed in terms of development and encountered barriers.
2.1  Functioning/operative technologies
The DT technology is considered the optimal solution for the control of smart energy systems 
(SESs). SES are those systems that comprise different energy vectors, several RES genera­
tors and storage technologies and most importantly exploit the opportunities offered by sector 
coupling and demand response (DR) strategies [12]. Many studies have proven that this solu­
tion allows better exploitation of non-dispatchable RES [13]. The most analysed sectors are 
the heating sector and the transportation one that are experiencing the fastest electrification 
process. This enables them to grow their demand response potential and also the impact on 
the power grid in terms of higher peak loads. In this framework, there is an extraordinary 
amount of data to gather, process and analyse to properly control SESs. The DT approach is 
the best candidate for grasping such complicated problems.
Indeed, a DT is able to:
•  Monitor the physical system: through on-field sensors and external sources. All the data 
necessary for the next steps are called digital thread [14].
•• Analyse and plan: this is done thanks to the digital model of the real system and several 
algorithms and techniques to identify the optimal measures to control the physical system.
•  Execute/control the real system: this is done through physical assets (i.e. controllers).
In order to realise it, a DT entails different levels, the physical assets (i.e. sensors and con­
trollers) that have to be connected with digital assets (often cloud-based) in order to store the 
data, process and analyse them and then simulate the real system behaviour through the dig­
ital model in order to find the optimal control strategy that will then be fulfilled by the 
controllers [15].
The management of such an intricate network is challenging for several reasons such as 
communication protocols, real-time processes and analyses, security and privacy and all the 
challenges that are linked to big data (e.g. management, storage, privacy and security). In 
[16], an edge computing architecture is proposed to overcome such difficulties given their 
ability to manage heterogeneous data. The proposed system can be divided in three layers: 
IoT and sensors for data gathering and physical control of the real assets, edge nodes for data 
processing and computing, and cloud services for statistical analysis and visualisation of data 
and all operations linked to artificial intelligence.
As said, the main objective of an energy management system is to control all the partici­
pating assets optimising different parameters while ensuring several constraints. If the overall 
objective can be always considered the least economic expenses, each subsystem requires 
different specific constraints. The power sector must always consider the constraints repre­
sented by the power grid in terms of stability and security of supply while also considering 
the technical characteristics of generators, both traditional and renewable, storage systems 
and loads. Regarding the thermal sector (i.e. heating and cooling), aside from the constraints 
connected to the technical characteristics of the thermal generators, the major constraints are 
connected to the indoor environmental quality that has to be ensured at all times. A similar 
constraint is necessary for the transport sector when considering electric vehicles (EVs). The 
power grid must always ensure a proper state of charge when the vehicle is supposed to 


---

Page 4

---

326	
M. Lamagna, et al., Int. J. of Energy Prod. & Mgmt., Vol. 6, No. 4 (2021) 
detach from the grid (each vehicle will require a different state of charge and different time 
of connection). Also, it should be considered that several other data, external to the energy 
system, are necessary to properly analyse the optimal management strategy (e.g. electricity 
price, gas price, emission indicators and weather data) [15]. A general architecture of such 
DT is shown in Fig. 2.
The advantage offered by the DT is the possibility to constantly monitor the system with 
the appropriate sensors and communication. This enables the DT to check that the real sys­
tem reacted to an input as expected; otherwise the control system will automatically order a 
different control strategy. Such a difference between the expected result and the obtained one 
in a perfect model could be attributed to a change in the real-world system. The additional 
advantage offered by DT is that the model will automatically analyse the reasons that lead to 
the deviations and will recalibrate itself. This is particularly important in an energy system 
that entails different sectors and an uncountable number of devices. Indeed, the installation 
of new charging stations, or heat pumps, or simply the modification of efficiency of some 
assets might modify the overall system response to a certain control manoeuvre. Thus, the 
ability of the digital model to modify its parameters to always be updated and able to mirror 
the real system is priceless.
Even additional challenges and barriers are found when transferring the aforementioned 
concepts in a business-oriented framework. This is true, for instance, in the case of demand 
response markets that involve several flexibility providers.
2.2  The power grid
National or local power grids offer a perfect field of application to the twinning technology 
regardless of their sizes.
Figure 2: DT synoptic.


---

Page 5

---

	
M. Lamagna, et al., Int. J. of Energy Prod. & Mgmt., Vol. 6, No. 4 (2021) 
327
The DT framework in the context of the Chinese national power grid was analysed in [17], 
and a new online analysis digital twin (OADT) was presented to solve real-world complex 
system problems in large scale (40k+ buses). The results presented in the paper show that the 
OADT can track the operation state of a large-scale power grid in real time with only a 
sub-second delay. The only impediment found for the DT application is inferable to software 
development problems, which needs an exhaustive software platform to be supported. How­
ever, the recent information technology advances enable more feasible and practical DT 
implementation. Similarly, in [18], the DT methodology was applied to understanding the 
power system dynamics in a way to set the grid to work at the optimum active and reactive 
settings, by adjusting the voltage stability which is reflected in an overall system reliability 
increase. The final objective of this research was to demonstrate that thanks to this approach, 
it is possible to integrate more variable RES technologies (in this case PV panels) in the 
actual grid, avoiding dangerous voltage variations. The proposed approach was successful, 
and the only limitation seems to be represented by a limited number of measurement devices 
installed on the grid.
Similarly, the objective in [19] was to apply the DT to the offshore wind farms transmission 
systems. The related voltage stability problems can become even a more challenging issue in 
these conditions. The paper proposed a direct voltage control (DVC) strategy in a real-time 
environment to stabilise voltage and frequency oscillations by means of a DT model. Moreo­
ver, the converters’ representation offers a better depiction of the real-world operation.
Reducing the research perimeter, in [20], the attention was focused on distribution network 
(DN) and the need to create an adequate interface able to gather all the information coming 
from sensors. Additionally, the authors in [21, 22] focused their work on the DN issues. Their 
objective was to increase the flexibility of the grid connecting both the local network and the 
regional power system. In these papers, the DT concept was used to modify the DN planning 
in execution, individualising in real time the future performance ratings and weak points 
according to the proposed changes. To reconstruct the virtual model, real-time operating data 
were assessed and used to build the DT algorithms. In conclusion, this work did not directly 
analyse the ongoing performances of the grid. Instead, forecasting the possible performances, 
it proposed different planning adjustments, supporting the applicability of the DT already 
from the project early stages. This approach is further investigated in [22], where the concept 
was enlarged by the authors to the distributed production penetration, to help the operators in 
making better operational decisions. Nevertheless, the presence of massive measuring instru­
mentation and other devices, many of those accessible by remote control, expose the power 
grid management to cyberattacks risk. In this regards, in [23], the authors proposed an innova­
tive solution to cope with this problem, a solution based on a IoT-DT model of the cyber-physical 
system that interacts with the control system to ensure its proper operation. The obtained 
results demonstrated how the proposed IoT-DT model is able to mitigate a cyberattack simu­
lated as a coordinated false data injection or as an attempted normal service interruption.
2.3  Energy systems
DT is a key aspect to increase the efficiency and the management of the energy systems. Fast 
response and analysis are required while working with electricity independently if the focus 
is on a transmission grid or a domestic system. Regarding affirmed technologies, most of the 
research prefers to analyse the entire system instead of a single one. For instance in [24], the 
analysis was focused on the entire city’s energy systems. In this latter research, the energy 


---

Page 6

---

328	
M. Lamagna, et al., Int. J. of Energy Prod. & Mgmt., Vol. 6, No. 4 (2021) 
systems were extended to the buildings energy performance, underlying the applicability and 
the possible interconnectivity with different topics such the Building Information Modelling 
(BIM) as it will be presented in the next section. Also, in [25], the energy systems are con­
verted in the DT model to recreate the smart grid to be analysed. Differently, when analysing 
new emerging technologies, the research perimeter remains closer to the system level. For 
example, hydrogen is confirming its role as enabling technology, representing a promising 
mechanism to realise sector coupling [26]. Following the other energy system technologies, 
also hydrogen solutions are experimenting with an exploration phase with DT models. At the 
moment, it was not possible to find works related to the DT applied to a fuel cell or electro­
lyser operating in a real context; instead, since the hydrogen topic is still gaining momentum, 
it was easier to find work related to the performance analysis at lab scale. The most researched 
aspects are related to the manufacturing and the advancement of this technology. To cope 
with this technical issue, surrogate modelling methods that combine a state-of-the-art 
three-dimensional physical model and a data-driven model are investigated in different 
researches. The result obtained in [27], concerning the DT of a proton exchange membrane 
fuel cell, can predict its outputs with a root-mean-square error from 3.88% to 24.80%. This 
architecture is used to control the healthy operation envelope and state map. Similarly, in 
[28], a DT model was made for a solid oxide fuel cell (SOFC), starting from a 1 kW SOFC 
data were used to regress the parameters to scale-up the model to 25 kW. The final obtained 
DT was validated by steady-state data and applied to on-site operation prediction with very 
high accuracy. The scope of the project was to help operators in the operation strategies selec­
tion, by means of simulations to execute the process safely and stably. Being relatively new 
as a subject, also the manufacturing itself is being investigated to lower initial costs and 
enhance the manufacturing process, in this regard it could be useful to analyse the informa­
tion reported in [29] where an exhaustive review on DT-based sustainable intelligent 
manufacturing is presented.
2.4  Buildings
Buildings account for a large portion of the overall energy consumption, and this is divided 
into electricity and thermal demand that are further split in heating and cooling. As for cool­
ing, this is mostly translated into electricity since the most used technology is heat pumps. 
Regarding heating instead, the framework is more varied since this can be supplied not only 
through several different means, such as gas, biomass, and other fossil fuels, but also through 
electricity thanks to heat pumps (also electric boiler but mostly for hot water instead than 
indoor ambient heating). Indeed, the energy intensity of buildings also varies depending on 
the end-use. Commercial buildings will have a much higher energy consumption compared 
to residential. Given buildings’ important role in the energy system, a SES must consider 
their role in the system both as consumers and service providers, particularly for flexibility 
services through demand response programmes. For these reasons as well as for a better 
monitoring and understanding of the energy system, smart metering and IoT devices pres­
ence in the building sector have been proliferating in the last years and are expected to keep 
growing in the years to come. This enables the application of DT concepts in the building 
sector, and several studies can be found in literature with different objectives and focus.
In [30], the authors apply a DT framework with the aim of monitoring several parameters 
and, through a serious game, reduce energy consumption and proving that a 40% energy 


---

Page 7

---

	
M. Lamagna, et al., Int. J. of Energy Prod. & Mgmt., Vol. 6, No. 4 (2021) 
329
saving can be achieved. This is an example of different services that can be offered by means 
of DT structure and architecture.
In [31], the authors adopt a DT approach in order to monitor buildings performance as well 
as renewable energy generation in order to improve overall performance of the smart city by 
means of an optimal scheduling. They classify home devices in three categories depending 
on their flexibility, such as shiftable (e.g. dryer), interruptible (e.g. hot water) and weather 
based (e.g. HVAC).
In [32], the authors presented a framework for near real-time management DR in SES 
which is able to fully exploit the potential offered by internet of things by means of a soft­
ware-in-the-loop strategy. They proved the benefits that could be provided to the grid by 
means of DR strategies at building level. Nevertheless, it is interesting to notice that the term 
‘digital twin’ is never mentioned in the whole article.
Zhou and Zhang [33] focused on a key feature of a DT control system that is the demand 
forecasting. Particularly, they proposed a model for smart homes based on edge computing 
that uses the cloud for data processing and for further analysis. The input data are collected 
both by sensors (i.e. IoT devices) and external/environmental data.
In [34], authors analyse a DT based on machine learning coupled with an urban-scale 
EnergyPLUS model with the aim of analysing the demand response potential of buildings to 
provide flexibility services to the grid.
In [35], the authors analyse the importance of edge computing for smart buildings and 
propose an approach based on the CAFCLA framework (Context-Aware Framework for Col­
laborative Learning Activities).
In [36], the authors apply a DT approach based on BIM and GIS on the case study in 
Rome, Italy. The proposed DT model is useful both in the design phase and in the operation 
phase for optimal management and control thanks to the use of artificial intelligence. The 
authors conclude that the proposed system is able to optimally modulate loads increasing 
self-consumption from RESs and decreasing the overall energy consumption.
Particular attention should be paid to the use of BIM in DTs, a phenomenon that has been 
growing and organically developing in the last period taking on the lesson learned in the man­
ufacturing sector [37]. A remarkable example is provided by Shahinmoghadam et al. [38]; the 
authors develop a BIM-IoT-based DT that also makes use of virtual reality for thermal and 
comfort monitoring. In [39], Desogus et al. analysed the use of BIM and IoT in a DT frame­
work for monitoring of indoor conditions (not only temperature and comfort but also luminance, 
etc.) and of energy consumption. A further trend is that of adopting geo-referencing in parallel 
to BIM and IoT for an all-inclusive DT able to integrate spatial data for a better visualisation 
and consequently a better decision making as presented in [40]. Here, the authors develop a 
common approach for geo-referencing in the framework of GIS/BIM in Industry Foundation 
Classes (IFCs) format. Also in [41], the topic of integrating GIS and BIM models is analysed. 
Specifically, the difficulties that lie in the intrinsic differences between the two frameworks 
that make it complex to convert data into one format to another. Particularly, the authors devel­
oped a method to easily convert IFCs into shapefiles in an efficient and reliable way.
2.5  Transport
Transport solutions can be associated with moving energy management systems, where the 
energy source is transformed in motion. Additionally, the recent processes in the transport 
sectors of electrification and digitalisation are opening interesting new scenarios for the entire 


---

Page 8

---

330	
M. Lamagna, et al., Int. J. of Energy Prod. & Mgmt., Vol. 6, No. 4 (2021) 
industry. The DT approach integration in this sector has been addressed by many authors with 
different focuses also outside energy-related topics. Regarding those latter, the DT was stud­
ied to forecast components failures [42], traffic management [43] and autonomous guide 
[44]. NASA was a precursor of the adoption of DT to enhance transport efficiency and safety 
[45]. In terms of energy-related investigation, in [46], the authors analysed a part of the rail­
ways system as a high-power demanding load in the power grids. During the work, a DT 
model to perform a proper monitoring and control of operations was modelled. This approach, 
oriented to grid management, was adopted also in smaller cases addressing the issue of EV 
charging. The DT was used in [47] to perform a smart battery charging strategy to extend the 
battery lifetime, and similarly in [48], the same issue was assessed. Differently in [49], the 
focus was moved towards the grid perspective, analysing the possible auxiliary services that 
can be offered by the batteries to this latter. The methodology proposed in this work com­
prises an architecture for a DT in the domain of the high-voltage battery system and then to 
offer digital services for various stakeholders. Nevertheless, to reach a fully functional DT, 
this model needs to be implemented in a cloud computing environment which is not well 
defined yet. With a comprehensive approach, the authors in [50] have undertaken an ambi­
tious investigation where a DT of an extensive portion of the city with all physical components 
was made. For the model, a total of 14,000 buildings including all locations of activities such 
as parking lots, transformers, middle-voltage lines, low-voltage lines of the distribution grid, 
and shops and homes were geo-referenced and modelled. Additionally, to correctly evaluate 
the population and mobility, also the city’s inhabitants and commuters are modelled using 
agent-based simulations. Finally, this innovative method has been demonstrated using meas­
urement data. Indeed, a system so defined can help in many ways in the city planning, 
management and resiliency, but it relies on a massive database system.
3  CONCLUSIONS
The paper reviewed the state of the art in terms of the use of the DT approach and concept 
applied to SESs. It firstly explained the particular application to SESs and the difficulties to 
such a wide and omni-comprehensive approach, and then it focused on the most interesting 
sectors and features of such systems. In conclusion, it can be stated that the powerful advan­
tages offered by the DT concept are clear. Several barriers that hinder the spread of this 
concept can still be found, and they vary from technical, mainly connected to big data and 
communication protocols, to economic but especially in a lack of regulation and a clear mar­
ket around the concept of demand response programmes. This uncertain and unclear 
framework led to many studies that developed different versions of DTs that can theoretically 
work in different frameworks based on different algorithms. Nevertheless, more specific DT 
can be found in single buildings or in other sectors such as the industrial.
Another common feature that has been noticed is that even though the DT concept is 
applied in several different studies regarding smart grid and SES, the keyword ‘digital twin’ 
is not always used. This signals the need for a further effort for interdisciplinary projects 
since, mostly from the energy/electricity sector, this term is not very well-known while it is 
always used by electronic/information professionals.
REFERENCES
  [1]	 Mai, T.T., Jadun, P., Logan, J.S., McMillan, C.A., Muratori, M., Steinberg, D.C., Vim­
merstedt, L.J., Haley, B., Jones, R. & Nelson, B., Electrification Futures Study: Sce­
narios of Electric Technology Adoption and Power Consumption for the United States. 
United States: N., 2018.  https://doi.org/10.2172/1459351


---

Page 9

---

	
M. Lamagna, et al., Int. J. of Energy Prod. & Mgmt., Vol. 6, No. 4 (2021) 
331
  [2]	 Philipp, G. & Singaravel, S., Component-based machine learning for performance 
prediction in building design. Applied Energy, 228, pp. 1439–1453, 2018. https://doi.
org/10.1016/j.apenergy.2018.07.011
  [3]	 Grieves, M. & Vickers, J., Digital twin: Mitigating unpredictable, undesirable emer­
gent behavior in complex systems. In: Kahlen F.J., Flumerfelt, S., Alves, A. (eds.) 
Transdisciplinary Perspectives on Complex Systems. Springer, Cham, 2017. https://doi.
org/10.1007/978-3-319-38756-7_4
  [4]	 Barricelli, B.R., Casiraghi E. & Fogli, D., A survey on digital twin: Definitions, charac­
teristics, applications, and design implications. In IEEE Access, 7, pp. 167653–167671, 
2019. https://doi.org/10.1109/ACCESS.2019.2953499
  [5]	 Kong, T., Hu, T., Zhou, T. & Ye, Y., Data construction method for the applications of 
workshop digital twin system. Journal of Manufacturing Systems, 58, Part B, pp. 323–
328, 2021. https://doi.org/10.1016/j.jmsy.2020.02.003
  [6]	 IEA, Smart Grids, IEA, Paris, 2020. https://www.iea.org/reports/smart-grids
  [7]	 ENTSO-E  , Digital Report: The cyber-physical system for the energy transition, 
ENTSO-E  , 2019. https://www.entsoe.eu/news/2019/11/18/cyber-meets-the-physical-
grid-entso-e-s-digital-report-is-out/
  [8]	 Blosch, M. & Fenn, J., Understanding Gartner’s Hype Cycles, Gartner, 2018.
  [9]	 Brosinsky, C., Westermann, D. & Krebs, R., Recent and prospective developments in 
power system control centers: Adapting the digital twin technology for application in 
power system control centers. 2018 IEEE International Energy Conference (ENERGY­
CON), pp. 1–6, 2018. https://doi.org/10.1109/ENERGYCON.2018.8398846
[10]	 Zheng, Y., Yang, S. & Cheng, H., An application framework of digital twin and its 
case study. J Ambient Intell Human Comput, 10, pp. 1141–1153, 2019. https://doi.
org/10.1007/s12652-018-0911-3
[11]	 Atalay, M. & Angin, P., A digital twins approach to smart grid security testing and 
standardization. 2020 IEEE International Workshop on Metrology for Industry 4.0 & 
IoT, pp. 435–440, 2020. https://doi.org/10.1109/MetroInd4.0IoT48571.2020.9138264
[12]	 Bellocchi, S., De Iulio, R., Guidi, G., Manno, M., Nastasi, B., Noussan, M., ... Roberto, 
R., Analysis of smart energy system approach in local alpine regions - A case study in 
northern italy. Energy, 202, 2020. https://doi.org/10.1016/j.energy.2020.117748
[13]	 Guelpa, E., Bischi, A., Verda, V., Chertkov, M. & Lund, H., Towards future infrastruc­
tures for sustainable multi-energy systems: A review. Energy, 184, pp. 2–21, 2019. 
https://doi.org/10.1016/j.energy.2019.05.057
[14]	 Snijders, R., Pileggi, P., Broekhuijsen, J., Verriet, J., Wiering, M. & Kok, K., Machine 
learning for digital twins to predict responsiveness of cyber-physical energy systems. 
Paper presented at the 8th Workshop on Modeling and Simulation of Cyber-Phys­
ical Energy Systems, MSCPES 2020 – Proceedings, 2020. https://doi.org/10.1109/
MSCPES49613.2020.9133695
[15]	 Park, H., Byeon, G., Son, W., Jo, H., Kim, J. & Kim, S., Digital twin for operation of 
microgrid: Optimal scheduling in virtual space of digital twin. Energies, 13(20), 2020. 
https://doi.org/10.3390/en13205504
[16]	 Sittón-Candanedo, I., Alonso, R. S., García, Ó., Muñoz, L. & Rodríguez-González, S., 
Edge computing, iot and social computing in smart energy scenarios. Sensors (Switzer­
land), 19(15), 2019. https://doi.org/10.3390/s19153353
[17]	 Zhou, M., Yan J. & Feng, D., “Digital twin framework and its application to power grid 
online analysis. In CSEE Journal of Power and Energy Systems, 5(3), pp. 391–398, 
September 2019. https://doi.org/10.17775/CSEEJPES.2018.01460


---

Page 10

---

332	
M. Lamagna, et al., Int. J. of Energy Prod. & Mgmt., Vol. 6, No. 4 (2021) 
[18]	 Jain, P., Poon, J., Singh, J. P., Spanos, C., Sanders, S. R. & Panda, S. K., A digital 
twin approach for fault diagnosis in distributed photovoltaic systems. In IEEE Transac­
tions on Power Electronics, 35(1), pp. 940–956, January 2020. https://doi.org/10.1109/
TPEL.2019.2911594
[19]	 Ganesh, S., Perilla, A., Torres, J.R., Palensky, P. & van der Meijden, M., Validation 
of EMT digital twin models for dynamic voltage performance assessment of 66 kV 
offshore transmission network. Appl. Sci., 11, p. 244, 2021. https://doi.org/10.3390/
app11010244
[20]	 Wagner, T., Mehlmann, G. & Richter, M., Application of the digital twin concept for a dis­
tribution network. PESS 2020; IEEE Power and Energy Student Summit, 2020, pp. 1–5.
[21]	 Feng, Z., et al., Online assessment of flexibility on active distribution network plan­
ning through digital twin. 2020 2nd International Conference on Electrical, Control 
and Instrumentation Engineering (ICECIE), pp. 1–6, 2020. https://doi.org/10.1109/
ICECIE50279.2020.9309627
[22]	 Feng, Z., Wu, Y., Gao, H. & Zhu, S., Digital twin framework for ADN flexible resources 
assessment. 2020 IEEE Eurasia Conference on IOT, Communication and Engineering 
(ECICE), pp. 209–212, 2020. https://doi.org/10.1109/ECICE50847.2020.9302004
[23]	 Saad, A., Faddel, S., Youssef, T. & Mohammed, O.A., On the implementation of 
IoT-based digital twin for networked microgrids resiliency against cyber attacks. In 
IEEE Transactions on Smart Grid, 11(6), pp. 5138–5150, November 2020. https://doi.
org/10.1109/TSG.2020.3000958
[24]	 Francisco, A., Neda, M. & Taylor, J.E., Smart city digital twin–enabled energy manage­
ment: Toward real-time urban building energy. Journal of Management in Engineering, 
36(2), March 2020. https://doi.org/10.1061/(ASCE)ME.1943-5479.0000741
[25]	 Ruohomäki, T., Airaksinen, E., Huuska, P., Kesäniemi, O., Martikka, M. & Suomisto, 
J., Smart city platform enabling digital twin. 2018 International Conference on Intel­
ligent Systems (IS), pp. 155–161, 2018. https://doi.org/10.1109/IS.2018.8710517
[26]	 Nastasi, B., Hydrogen policy, market and R&D project. In Calise, F., D’Accadia, M.D., 
Santerelli, M., Lanzini, A., Ferrero, D., (eds.), Solar Hydrogen Production. Elsevier: 
Cambridge, MA, USA.
[27]	 Bowen, W., Guobin, Z., Huizhi, W., Jin, X. & Kui, J., Multi-physics-resolved digi­
tal twin of proton exchange membrane fuel cells with a data-driven surrogate model. 
Energy and AI, 1, 2020, https://doi.org/10.1016/j.egyai.2020.100004
[28]	 Jia-Lin, K., Chien-Cheng, W., David Shan-Hill, W., Shi-Shang, J. & Chun-Hsiu, W., 
Digital twin model and dynamic operation for a plant-scale solid oxide fuel cell system. 
Journal of the Taiwan Institute of Chemical Engineers, 118, pp. 60–67, 2021. https://
doi.org/10.1016/j.jtice.2021.01.001
[29]	 He, B. & Bai, K.J., Digital twin-based sustainable intelligent manufacturing: A review. 
Adv. Manuf., 9, pp. 1–21, 2021. https://doi.org/10.1007/s40436-020-00302-5
[30]	 García, Ó., Alonso, R.S., Prieto, J. & Corchado, J.M., Energy efficiency in public 
buildings through context-aware social computing. Sensors (Switzerland), 17(4), 2017. 
https://doi.org/10.3390/s17040826
[31]	 Ejaz, W., Naeem, M., Shahid, A., Anpalagan A. & Jo, M., Efficient energy management 
for the internet of things in smart cities. In IEEE Communications Magazine, 55(1), pp. 
84–91, January 2017. https://doi.org/10.1109/MCOM.2017.1600218CM
[32]	 Barbierato, L., et al., A distributed IoT infrastructure to test and deploy real-time 
demand response in smart grids. In IEEE Internet of Things Journal, 6(1), pp. 1136–
1146, February 2019. https://doi.org/10.1109/JIOT.2018.2867511


---

Page 11

---

	
M. Lamagna, et al., Int. J. of Energy Prod. & Mgmt., Vol. 6, No. 4 (2021) 
333
[33]	 Zhou, S. & Zhang, L., Smart home electricity demand forecasting system based on 
edge computing. 2018 IEEE 9th International Conference on Software Engineer­
ing and Service Science (ICSESS), pp. 164–167, 2018, https://doi.org/10.1109/
ICSESS.2018.8663894
[34]	 Agostinelli, S., Cumo, F., Guidi, G. & Tomazzoli, C. Cyber-physical systems improv­
ing building energy management: Digital twin and artificial intelligence. Energies, 14, 
p. 2338, 2021. https://doi.org/10.3390/en14082338
[35]	 Sittón-Candanedo, I., Alonso, R. S., García, Ó., Muñoz, L. & Rodríguez-González, S., 
Edge computing, iot and social computing in smart energy scenarios. Sensors (Switzer­
land), 19(15), 2019. https://doi.org/10.3390/s19153353
[36]	 Agostinelli, S., Cumo, F., Guidi, G. & Tomazzoli, C., The potential of digital twin 
model integrated with artificial intelligence systems. Paper presented at the Proceed­
ings - 2020 IEEE International Conference on Environment and Electrical Engineering 
and 2020 IEEE Industrial and Commercial Power Systems Europe, EEEIC / I and CPS 
Europe 2020, 2020. https://doi.org/10.1109/EEEIC/ICPSEurope49358.2020.9160810
[37]	 Davila Delgado, J.M. & Oyedele, L., Digital twins for the built environment: Learning 
from conceptual and process models in manufacturing. Advanced Engineering Infor­
matics, 49, 2021. https://doi.org/10.1016/j.aei.2021.101332
[38]	 Shahinmoghadam, M., Natephra, W. & Motamedi, A., BIM- and IoT-based virtual real­
ity tool for real-time thermal comfort assessment in building enclosures. Building and 
Environment, 199, 2021. https://doi.org/10.1016/j.buildenv.2021.107905
[39]	 Desogus, G., Quaquero, E., Rubiu, G., Gatto, G. & Perra, C., Bim and iot sensors 
integration: A framework for consumption and indoor conditions data monitoring of 
existing buildings. Sustainability (Switzerland), 13(8), 2021. https://doi.org/10.3390/
su13084496
[40]	 Zhu, J. & Wu, P., A common approach to geo-referencing building models in industry 
foundation classes for bim/gis integration. ISPRS International Journal of Geo-Infor­
mation, 10(6), 2021. https://doi.org/10.3390/ijgi10060362
[41]	 Zhu, J. & Wu, P., Towards effective bim/gis data integration for smart city by integrating 
computer graphics technique. Remote Sensing, 13(10), 2021. https://doi.org/10.3390/
rs13101889
[42]	 Bhatti, G., Mohan, H. & Singh, R.R., Towards the future of smart electric vehicles: Dig­
ital twin technology. Renewable and Sustainable Energy Reviews, 141, 2021. https://
doi.org/10.1016/j.rser.2021.110801
[43]	 Kumar, S.A.P., Madhumathi, R. & Chelliah, P.R., et al., A novel digital twin-centric 
approach for driver intention prediction and traffic congestion avoidance. J Reliable 
Intell Environ, 4, pp. 199–209, 2018. https://doi.org/10.1007/s40860-018-0069-y
[44]	 Bottani, E., Cammardella, A., Murino, T. & Vespoli B., From the cyber-physical system 
to the digital twin: The process development for behaviour modelling of a cyber guided 
vehicle in M2M logic, 2017.
[45]	 Glaessgen, E.H. & Stargel, D.S., The digital twin paradigm for future NASA and U.S. 
air force vehicles. Paper for the 53rd Structures, Structural Dynamics, and Materi­
als Conference: Special Session on the Digital Twin. https://doi.org/10.2514/6.2012-
1818
[46]	 Ahmadi, M., Kaleybar, H.J., Brenna, M., Castelli-Dezza F. & Carmeli, M.S., Adapting 
digital twin technology in electric railway power systems. 2021 12th Power Electron­
ics, Drive Systems, and Technologies Conference (PEDSTC), pp. 1–6, 2021. https://doi.
org/10.1109/PEDSTC52094.2021.9405876


---

Page 12

---

334	
M. Lamagna, et al., Int. J. of Energy Prod. & Mgmt., Vol. 6, No. 4 (2021) 
[47]	 Ali, M.U., Zafar, A., Nengroo, S.H., Hussain, S., Alvi, M.J. & Kim, H.J., Towards a 
smarter battery management system for electric vehicle applications: A critical review 
of lithium-ion battery state of charge estimation. Energies, 2019.
[48]	 Li, W., Kwiecien, M., Badeda, J, Jöst, D., Schulte, D. & Sauer, D., Digital twin for 
battery systems: Cloud battery management system with online state-of-charge and 
state-of-health estimation. J Energy Storage, 30, p. 101557, 2020. https://doi.1016/j.
est.2020.101557
[49]	 Merkle, L., Segura, A. S., Torben Grummel, J. & Lienkamp, M., Architecture of a digi­
tal twin for enabling digital services for battery systems. 2019 IEEE International Con­
ference on Industrial Cyber Physical Systems (ICPS), pp. 155–160, 2019. https://doi.
org/10.1109/ICPHYS.2019.8780347
[50]	 Pagani, M., Korosec, W., Chokani, N. & Abhari, R.S., User behaviour and electric vehi­
cle charging infrastructure: An agent-based model assessment. Applied Energy, 254, 
2019. https://doi.org/10.1016/j.apenergy.2019.113680
