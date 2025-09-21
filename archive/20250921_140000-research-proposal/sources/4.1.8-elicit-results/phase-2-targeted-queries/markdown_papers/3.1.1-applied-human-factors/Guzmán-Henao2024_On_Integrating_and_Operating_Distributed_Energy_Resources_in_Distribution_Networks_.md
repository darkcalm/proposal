# Guzmán-Henao2024 On Integrating and Operating Distributed Energy Resources in Distribution Networks  A Review of Current Solution Methods, Challenges, and Opportunitie

## Paper Metadata

- **Filename:** Guzmán-Henao2024_On_Integrating_and_Operating_Distributed_Energy_Resources_in_Distribution_Networks__A_Review_of_Current_Solution_Methods,_Challenges,_and_Opportunitie_DOI_10-1109_ACCESS-2024-3387400.pdf
- **DOI:** 10.1109/ACCESS.2024.3387400
- **Authors:** Not available
- **Year:** Not available
- **Journal/Venue:** Not available
- **URL:** Not available
- **Extraction Date:** 2025-06-03T15:04:06.009662
- **Total Pages:** 23

## Abstract

Abstract not available from BibTeX metadata.

## Keywords

Keywords not available from BibTeX metadata.

---

## Full Text Content



### Page 1

Digital Object Identifier
On Integrating and Operating Distributed
Energy Resources in Distribution
Networks: A Review of Current Solution
Methods, Challenges, and Opportunities
JHONY ANDRÉS GUZMÁN-HENAO1, RUBÉN IVÁN BOLAÑOS1, OSCAR DANILO
MONTOYA2, (SENIOR MEMBER, IEEE), LUIS FERNANDO GRISALES-NOREÑA3, HAROLD R.
CHAMORRO4,(Senior Member, IEEE)
1Departamento de Mecatrónica y Electromecánica, Facultad de Ingeniería, Instituto Tecnológico Metropolitano, Medellín 050036, Colombia (e-mails:
jhonyguzman72415@correo.itm.edu.co, rubenbolanos@itm.edu.co)
2Facultad de Ingeniería, Universidad Distrital Francisco José de Caldas. Carrera 7 No. 40B-53, Bogotá D.C 110231, Colombia (e-mail:
odmontoyag@udistrital.edu.co)
3Department of Electrical Engineering, Universidad de Talca, Curicó 3340000, Chile. (e-mail: luis.grisales@utalca.cl)
4KTH Royal Institute of Technology, 114 28 Stockholm, Sweden. (e-mail: hrcv@kth.se)
Corresponding authors: Oscar Danilo Montoya (email: odmontoyag@udistrital.edu.co) and Luis Fernando Grisales-Noreña (e-mail:
luis.grisales@utalca.cl).
This work was funded by Ringgold ID for KTH: 7655 (RIN 7655).
ABSTRACT The growing demand for electric power and the need for an energy transition that contributes
to the reduction of global greenhouse gas emissions have driven the development of various energy
generation, storage, and offset technologies. These technologies are known as distributed energy resources.
Their integration into distribution power systems not only contributes to improving operating aspects, but
also allows supplying electricity to areas that do not have access to large-scale power systems. Therefore,
the integration and management of these resources has become a topic of interest, and several studies seek to
optimize their impact on technical, economic, and environmental aspects. However, this optimization poses
specific challenges related to the type and number of variables related to the operation of a distribution
power system. This review article aims to describe the main challenges posed by three-phase AC threephase distribution power systems under scenarios involving the integration of distributed energy resources.
In addition, it presents some approaches proposed by different authors to improve the technical, economic,
and environmental aspects of power grids. It can be stated that the strategies presented in the literature fail
to consider scenarios that simultaneously integrate different types of technologies and optimize them while
following a multi-objective approach and considering three-phase systems in a context of variable generation
and demand. Therefore, future work in this field should address these aspects in a holistic manner, taking
into account the computation efforts and processing times required by intelligent algorithms.
INDEX TERMS Electrical mathematical model, DERs, DG, Energy costs, CO2 emissions, Energy losses,
BESS.
I. INTRODUCTION
In recent years, the accelerated growth of the world’s population has posed several challenges associated with the developments needed to ensure the worldwide supply of electrical
energy [1]. Electric power systems (EPS) have enabled the
generation, transmission, distribution, and control of this type
of energy on a large scale. However, they face challenges
of their own, which are related to the need for changes that
allow meeting the growing energy demand. One of the most
significant corresponds to the integration of renewable energy
sources into the energy matrix. [2] [3].
The distribution stage is where the greatest challenges
arise, as it is there that direct interaction with end users takes
place [4]. These users have different characteristics, which
make the system operation model complex and force network
operators to adopt strategies aimed at analyzing technical,
economic, and environmental aspects. These strategies must
ensure the correct supply of electric power to all users, for
VOLUME 4, 2016
1
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3387400
This work is licensed under a Creative Commons Attribution-Non Commercial-No Derivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

---


### Page 2

which aspects such as power quality, voltage profiles, and line
capacity are of vital importance [5].
Most electrical distribution systems (EDS) worldwide are
built with a radial topology, as this implies low investment
costs and constitutes the typical distribution of loads. However, this topology considerably increases energy losses and
has impacts on the operating aspects of the system [6]. In a
radial distribution system, current must flow through a single
path to the loads, which, depending on the distance, can cause
voltage drops in the nodes. Additionally, lines closer to the
generation node experience high current flows, leading to
increased energy losses due to the Joule effect [7].
Electrical energy is transported through three-phase connections with the objective of increasing power capacity
and reducing losses. An ideal three-phase system assumes
a power balance in each of its phases. However, each user
connected to the grid requires a different type of connection (single-phase, two-phase, or three-phase) according to
their consumption requirements (residential, commercial, or
industrial) [8]. In this context, the power levels of each phase
vary according to the type of connection and the users’
consumption requirements. This variability contributes to
voltage and current imbalances in the system. Unbalanced
operation in an EDS system triggers a series of negative effects, such as increased energy losses, increased current flows
(which affects the continuity of the service), and variations
in voltage profiles. All of the above affects the reliability
of the system and has a transversal impact on the technical,
economic, and environmental aspects of the network [9].
Another significant challenge in the operation of EDS lies
in their integration with large EPS. It is important to consider
the topographical, social, economic, demographic, political,
and cultural aspects of the territories within the influence
areas of the EPS, as they determine whether an interconnection between EDS and large EPS is feasible. The geographic
location and the relief of a region, as well as population
density and growth projection, infrastructure cost, regulatory
aspects, and cultural considerations are essential factors to
evaluate the technical, social, and economic viability of interconnecting EDS with large EPS. If this interconnection is
not possible, the EDS should operate independently in what
is known as an isolated area [10].
Isolated areas are highly dependent on fossil fuels for
electricity generation, leading to negative environmental impacts due to high pollutant gas emissions from these energy
sources [11]. In addition, energy distribution is carried out
using systems that, as in interconnected areas, have a radial
topology, which represents both an operating problem due
to the losses associated with the transport of energy and
increased costs related to generation and distribution [6].
In light of the above, it can be concluded that both connected and isolated areas require strategies to meet their
energy needs. However, in isolated areas, service continuity
must also be guaranteed, which adds an additional complication in comparison with grid-connected networks. It
is important to note that a system’s technical, economic,
and environmental aspects determine the efficiency of such
strategies and their potential to impact social and economic
development, as well as the end users’ quality of life. Therefore, this topic is of great interest and has been the subject of
various research projects that seek to improve these aspects.
In recent years, distribution grid operators have implemented strategies to improve the operating aspects of electrical systems. To this effect, they use energy generation devices
based on renewable sources, energy storage devices, and
reactive power compensation systems, which together are
known as distributed energy resources (DERs) and allow for
an adequate management of the energy needs of the grid [12].
DERs contribute to improving voltage profiles and reducing
energy losses as well as the percent load on distribution
system lines.
The impact of DERs depends on their proper integration
and operation. Aspects such as the technology used, size, and
energy injection and storage are of vital importance if the
potential of these systems is to be fully exploited [13].
From a mathematical point of view, the DER integration
problem is difficult to solve due to its nonlinear and nonconvex nature. Its mathematical formulation involves binary
and continuous variables, which may belong to the real or
complex domain [14]. In addition, each scenario involving
the integration of generation, storage, and compensation devices must be validated via power flows that allow determining the state of the EDS variables, such as voltage levels and
current flows. This validation must be carried out through
methodologies that allow evaluating a large number of flows
in acceptable processing times.
Some strategies focus on improving technical aspects,
with notable topics including the reduction of energy losses
[7], [15], [16], the improvement of voltage profiles [17]–
[19], and the reduction of line load percentages [4], [20].
Additionally, economic aspects such as investment and operating costs [21]–[23] are addressed, alongside environmental
considerations [24], [25], such as the reduction of greenhouse
gas emissions. Optimization algorithms are used in these
strategies to determine the most appropriate technologies,
nominal sizes, injection levels, and energy storage solutions
for each device [26].
A. CONTRIBUTIONS AND SCOPE
This article presents a review regarding the main challenges
associated with the operation of three-phase AC EDS, as well
as the strategies employed by grid operators to guarantee the
supply of electric power. In addition, it provides a critical
analysis of several strategies based on intelligent algorithms
which contribute to improving the impact of DER installation
on EDS. The limitations of each study are highlighted, as
well as the need to simultaneously address them in future
work.
B. ARTICLE STRUCTURE
The remainder of this article is structured as follows. In
Section II, the operation of EPS is detailed, with a particular
2
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3387400
This work is licensed under a Creative Commons Attribution-Non Commercial-No Derivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

---


### Page 3

focus on the challenges that arise during the distribution
stage. In addition, this section discusses strategies commonly
employed by grid operators to improve system operation and
ensure reliable power supply in both connected and isolated
areas, and it summarizes the main advances and approaches
presented by the specialized literature to address and implement the proposed strategies. Section III addresses the problem of DER integration in EDS through a critical analysis
of several research works. Finally, Section IV presents the
conclusions of our work, highlighting its main contributions,
providing some recommendations, and outlining future lines
of work.
II. ELECTRIC POWER SYSTEMS
EPS consist of multiple stages that allow effectively meeting
energy demands. Figure 1 shows their three primary stages.
Generation
Transmission
Distribution
FIGURE 1: Stages of an electric power system
Each of these stages plays a crucial role within the system
and has distinctive characteristics that define its operating
model [2]. The first stage, and perhaps one of the most important, is the generation stage. In this stage, the conversion
of energy from different sources takes place. Its main feature
lies in the ability to obtain electrical energy through different
processes (combustion, mechanical power, nuclear power,
and the exploitation of the various forms of energy present
in nature). In addition, at this stage, it is necessary to ensure
that the amount of energy generated is sufficient to meet the
demand while maintaining acceptable frequency and voltage
levels in the system [27].
In large-scale EPS, electric power is generated far from
the final consumption points, so it must be conditioned for
transport over long distances. Once conditioned, this electrical energy is sent to the next stage, which is known as
the transmission stage. The objective here is to ensure the
efficient transport of energy over long distances. To this
effect, transmission lines operate at high voltages, which
reduces energy losses. In addition, by controlling electrical
variables such as frequency and voltage, as well as through
real-time monitoring of the system’s operating conditions, it
must be ensured that the transported power is stable and of
high quality [27].
Once transported, the electrical energy reaches large consumption centers and must be conditioned again to move
on to the distribution stage, where the energy generated is
distributed and marketed. It is at this stage that the greatest
challenges arise, given the direct interaction of the system
with the end users [27].
A. CHALLENGES ASSOCIATED WITH EDS
The main objective of EDS is to distribute the energy coming
from the generation and transmission stages among the end
users. To this effect, proper energy management must be
ensured. This has implications for aspects such as efficiency,
reliability, quality, and energy demand, where the characteristics of EDS have a direct impact [28]. Figure 2 shows
the main characteristics of EDS, which pose a series of
challenges regarding their operation.
1
2
3
4
5
8
6
7
Network
topology
Power transport
Types of
users
Electrical Distribution System 
FIGURE 2: Challenges associated with electrical distribution
systems
1) EDS topology
The topology of any system that connects different elements
determines the most relevant operating aspects. In the case
of EDS, topology impacts efficiency, reliability, and the cost
of energy production. Regarding efficiency, a topology that
minimizes the length of distribution lines can reduce energy
losses due to conductor resistance. Similarly, a topology
favoring redundancy and multiple feeding routes for loads
results in greater reliability, and the implementation of one
with fewer lines entails significant cost savings [29].
A large part of EDS worldwide are radial, which is due
to the way in which the users are connected to it and to the
economic advantages offered by this topology [30].
In a radial EDS, power flows in only one direction: from
the central source or substation to the consumption points
[31]. This results in a smaller infrastructure and, therefore, in
lower implementation costs when compared to other topologies. However, as one moves away from the power source, the
power flow decreases due to increased line resistance, which
causes voltage drops and increases the system’s power losses
[32]. This challenge necessitates strategies to minimize energy losses while meeting the system’s energy demands.
A meshed topology offers advantages in terms of system reliability, operation, and resilience, given its ability
to distribute energy through multiple paths. However, this
results in the need for more infrastructure, which increases
implementation costs and makes it less attractive from an
economic point of view [33].
2) Energy transport in an EDS
Most EPS use three-phase systems for the generation, transmission, and distribution of electric power, as these systems
allow for the efficient transport of large amounts of energy
VOLUME 4, 2016
3
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3387400
This work is licensed under a Creative Commons Attribution-Non Commercial-No Derivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

---


### Page 4

over long distances and ensure a constant flow of energy
[34]. In EDS, power is also transported through three-phase
systems, but some users may be connected to single-phase
grid sections, which is due to the nature of their electrical
loads [35].
The ideal operation of a three-phase EDS implies a balance
between its phases [36]. However, because users can be
connected to the grid in different ways (single-phase, twophase, or three-phase) as shown in Figure 3, the actual operation implies complications associated with the imbalance
resulting from the direct interaction between the system and
the users. This imbalance has an impact on the efficiency,
reliability, and quality of the delivered power [37]. This poses
a challenge regarding the proper operation of the system,
which requires grid operators to develop strategies in order to
guarantee the power supply and reduce energy losses while
complying with quality standards.
In essence, a grid operator must ensure proper load planning. That is to say, they must evenly distribute loads among
the phases of the system. However, effective planning must
be accompanied by a continuous monitoring system with
regard to the operating conditions of the EDS. This allows
the grid operator to promptly detect imbalances and develop strategies to ensure EDS balance [38]. Some of these
strategies could include load redistribution, the integration
of DERs, or the implementation of advanced control and
monitoring technologies [39], [40].
1
3
2
FIGURE 3: Types of connections to an EDS
3) The variability introduced by renewable resources
Over the past years, there has been a remarkable growth in the
utilization of renewable energy sources to meet the energy
needs of various regions. Among the leading technologies
driving this growth are wind energy and photovoltaic (PV)
solar energy. The latter enjoys widespread acceptance due to
its availability in different parts of the world [41].
It is possible to represent the generation potential of PV
sources through a curve over a time interval. For a typical day
of operation, the curve has a characteristic shape, with a peak
during daylight hours when solar radiation is most intense,
declining towards the morning and evening. Similarly, it is
possible to represent the energy consumption of a region as a
function of its power demand during the same time interval
[42]. In Figure 4, the characteristic behavior of both curves
can be observed.
1
2
3
4
5
6
7
8
9
10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
Time (h)
0
20
40
60
80
100
Solar generation (%)
Characteristic curve of photovoltaic solar generation
1
2
3
4
5
6
7
8
9
10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
Time (h)
0
20
40
60
80
100
120
Energy demand (%)
Characteristic curve of power demand
FIGURE 4: Characteristic power generation and demand
curves
From the above, it is understood that there are times of the
day when PV generation has a significant impact on system
power levels, reducing reliance on conventional generators.
While this can bring technical, economic, and environmental
benefits, it also poses a series of challenges.
A clear example of the aforementioned can be seen in
California (USA), a region with a high penetration of PV generation sources and with power demand levels that increase
primarily in the late afternoon and early evening [43]. This
means that, just at the end of the PV generation interval, the
system’s power demand increases significantly, requiring the
extensive deployment of conventional generators to reach the
required power levels. This can destabilize the system and
cause operation failures. This phenomenon is known as the
California duck curve, referring to the shape of the net power
demand curve, which decreases during the peak PV injection
hours at noon and suddenly rises towards the evening [44].
4) Types of users connected to EDS
An EDS must be able to serve users with diverse energy
needs and demands. The way in which users connect to the
grid, the type of loads they demand, and their consumption
habits are characteristics that determine their impact on the
operation of the system.
Loads can be resistive, capacitive, or inductive in nature,
which may pose challenges related to power factor management and power quality control. The nonlinearity present
in capacitive and inductive loads can cause harmonics and
distortions in the current and voltage waveforms. All of the
above contributes to increased current and voltage fluctuations, resulting in higher energy losses and reduced system
reliability [45].
Users can be classified into different groups [46]. The first
of these is known as the residential user group and comprises
a high percentage of the total system demand. Residential
users employ electrical energy to meet their daily needs,
including lighting, heating, cooling, and entertainment. Although there may be capacitive and inductive loads, most of
4
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3387400
This work is licensed under a Creative Commons Attribution-Non Commercial-No Derivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

---


### Page 5

the devices in homes are resistive in nature. Most residential
users are connected to the grid through single-phase network
sections due to their low power demand and the nature of
their needs. However, in buildings that house a significant
number of residential users, three-phase connections may be
required. It is important to note that the consumption habits
of these users tend to vary over time [47].
Another important group of users corresponds to commercial users, who cover a wide variety of sectors. Similarly
to residential users, their energy consumption can vary over
time. These users employ energy to meet specific needs
related to business operations, often requiring the system to
be more efficient and reliable, as well as to provide power of
better quality. The devices and machinery employed by these
users tend to be mostly resistive and inductive and require
a significant amount of power. Therefore, it is common for
them to be connected to the grid through three-phase network
sections [48].
One group that has a significant impact on the operation of
EDS corresponds to industrial users. This group is characterized by a significant demand for electricity, which is used
for productive purposes. It represents several sectors with
specific and unique energy needs, and it is characterized by
three-phase connections to the grid and by combining resistive, inductive, and capacitive loads. Naturally, this impacts
the operation of the system [49].
Other grid-connected users, such as institutional, agricultural, critical, or large consumers may have different
consumption needs and must satisfy different types of loads
(resistive, inductive, and capacitive), requiring single- or
three-phase connections to the grid. In conclusion, different
users have different impacts on the operating aspects of
EDS, which represents a challenge in terms of efficiency,
reliability, and proper operation [50].
Finally, it is essential to highlight that the topology of
the network, the means for transporting electric power, and
the interaction with different user types pose a series of
challenges to ensure the reliable and efficient operation of
EDS. It is also important to mention that, in the operation of
EPS, there are other characteristics that determine whether or
not a given region can be connected to the system.
B. FACTORS INFLUENCING THE INTEGRATION OF
TERRITORIES INTO LARGE EPS
Large EPS make it possible to meet the energy needs of
different types of users, which are generally grouped in
different territories [51]. As already mentioned, the transmission stage is in charge of carrying electrical energy from the
generation site to the centers of mass consumption, which
initiates the distribution stage. However, there are specific
characteristics in each territory which determine the viability
of the connection between both stages or subsystems.
The possibility of integrating a specific territory to a
large EPS is determined by a series of factors that include
topographic, social, economic, demographic, political, and
cultural aspects [52]. Topographic conditions can sometimes
make it difficult or very costly to install the infrastructure
needed to connect the transmission stage to the distribution
stage [53]. Similarly, social aspects such as the reluctance of
inhabitants to the installation of infrastructure and conflicts
related to land use often prevent the connection of a territory
to large EPS [54].
Population density and distribution, together with the energy needs of a specific territory, may render the connection
to large EPS unfeasible from an economic perspective [55].
In addition, it is important to note that political and regulatory
aspects can influence the planning and implementation of
electrical infrastructure projects, which in turn can determine
whether or not a territory is to be connected to a large EPS
[55]. When this is not feasible, the electrical system entrusted
with meeting energy demands must operate independently,
resulting in an isolated zone.
Isolated zones are established when it is impossible to
connect a territory to a large EPS. Consequently, these areas
do not have access to the energy generated and transmitted
through large-scale infrastructures. Instead, these territories
rely mostly on local sources, which are usually based on nonrenewable energy [56].
Isolated areas are highly dependent on fossil fuels. Among
the most commonly used are petroleum derivatives such
as diesel, gasoline, kerosene, and fuel oil. This entails a
negative environmental impact due to increased greenhouse
gas emissions. In addition, this dependence makes energy
production vulnerable to fuel price fluctuations. These types
of areas tend to have a limited generation capacity, which can
contribute to scenarios in which the total energy demand of
the system is not met, especially at times of high demand.
This can also lead to service intermittency.
EDS in isolated areas are also mostly built with radial
topologies, given the low implementation costs [57]. The
energy generated through local sources is distributed through
systems of a three-phase nature and, in some sections of the
network, under a single-phase configuration. As in connected
areas, this type of topology poses some challenges related to
the efficiency, reliability, and quality of the energy supplied
through the system. Likewise, these networks serve users
with different characteristics, behaviors, and needs, which
turns EDS management into a problem of multiple variables,
wherein technical, economic, and environmental aspects are
crucial and have a significant impact on the quality of life
and socioeconomic development of the communities that
inhabit isolated areas. Therefore, strategies are required to
adequately manage the energy needs of both grid-connected
and isolated areas while ensuring a correct system operation.
C. STRATEGIES FOR MANAGING EDS IN
INTERCONNECTED AND ISOLATED AREAS
During the last few years, different devices with an impact
on the operating variables of EDS have been developed.
As previously mentioned, these are called distributed energy resources (DERs). Through the correct integration and
management of DERs, it is possible to obtain significant
VOLUME 4, 2016
5
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3387400
This work is licensed under a Creative Commons Attribution-Non Commercial-No Derivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

---


### Page 6

improvements in the technical, economic, and environmental
aspects of the system, which is why network operators have
focused their efforts on developing strategies to optimize the
use of these devices. Figure 5 shows the main categories into
which these devices can be grouped.
1
2
3
4
5
8
6
7
Distributed
Generation 
Energy storage
systems 
Reactive power
compensation 
Demand
management
FIGURE 5: Main categories of distributed energy resources
1) Distributed generation devices
A distributed generation (DG) device enables power generation closer to the consumption points and reduces the
dependence on the sources of large EPS. In addition, it can
improve efficiency, reliability, and power quality by integrating with EDS. It also contributes to supplying the demand
for electricity in territories that, due to their topographic,
economic, social, cultural, and demographic characteristics,
cannot be provided with electricity from large EPS [58].
Among the most widely used renewable energy sources for
DG are solar, wind, hydro-, and biomass generators, each
with special characteristics that make them relevant under
some scenarios. Even though it is still possible to use sources
that generate power from the use of fossil fuels, this has a
negative impact on the economic and environmental aspects
of the grid [59].
The integration of DG devices impacts the operating aspects of the grid, such as the nodal voltage profiles and the
electrical current flowing through the system’s distribution
lines. This reduces energy losses and operating costs and contributes to reducing greenhouse gas emissions [60]. However,
this integration poses multiple challenges, forcing grid operators to develop strategies aimed at optimizing the impact
of these resources on EDS. Among the decision variables
most widely explored in the literature are the location of the
generators, their rated power, and the amount of energy they
should inject [61].
One of the disadvantages of some DG sources, mainly
those that use renewable energy resources, has to do with
variations in power availability, which hinders the control
of the generated energy and creates the need to incorporate
devices that allow storing it at times of low availability and
delivering it according to the energy demands of the system
[62].
2) Battery energy storage systems
Battery energy storage systems (BESS) are of vital importance for strategies focused on improving the technical, economic, and environmental aspects of EDS. They complement
the integration of DG devices, as they allow storing energy
in times of excess generation and delivering it to end users
when needed. This, in turn, is reflected in a greater power
supply reliability and a significantly improved power quality.
BESS allow controlling the voltage of the network, they help
to efficiently manage the energy demand, and they reduce
the congestion of the distribution lines. All this reduces a
grid’s energy losses and operating costs, and it improves the
environmental aspects related to its operation [63].
Among the decision variables that have been most widely
studied in the specialized literature and have a greater impact
on EDS are the type of technology, the state of charge, and
the location and sizing of batteries [24]. Therefore, the main
challenge when integrating this type of devices lies in determining each of these variables, seeking the best technical,
economic, and environmental impacts on the grid.
3) Reactive power compensation devices
The integration of different types of DERs contributes to the
efficient and reliable operation of an EDS. Relevant aspects
such as energy losses reduction, voltage profile improvement,
and line current reduction are positively impacted by the
proper management of the system’s reactive power [64].
Reactive power plays a critical role in EDS. Although
it is not useful on its own, it is essential for maintaining
voltage levels, power quality, and system stability [65]. The
introduction of active power through DG devices impacts
every component of the system, affecting both its active and
reactive power [65]. It is common to encounter situations
where DG significantly alters the power balance of each
component, resulting in energy losses and adversely affecting
various operational aspects of the system, such as voltage
levels and power quality [66].
A practical solution that has gained traction in recent years
is the installation of reactive power compensation devices.
These devices help to maintain the necessary power balance
and improve the impacts related to the implementation of
DG sources [67]. A variety of devices are currently being
used, such as capacitor banks [68], static compensators [69],
synchronous machines [70], and shunt transformers [71],
among others. These devices differ in their ability to provide
reactive power compensation to the grid. Capacitor banks are
used to correct the power factor through fixed and constant
compensation. They are suitable for applications where the
reactive power demand is predictable [72].
On the other hand, static compensators provide dynamic
reactive power control, allowing for variable and rapid compensation. They enable voltage control and system stabiliza6
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3387400
This work is licensed under a Creative Commons Attribution-Non Commercial-No Derivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

---


### Page 7

tion against rapid changes in load or operating conditions
[73], [74].
Synchronous machines are electrical generators that can
operate in both generation and motor modes. In their generation stage, they can provide reactive power to the system,
helping to maintain voltage levels. However, their ability to
provide reactive power is limited by the nominal characteristics of the generator and its excitation capacity [75].
Shunt transformers can provide reactive power compensation by adjusting the configuration of their windings, allowing them to absorb or supply reactive power according
to the system’s needs. This capability makes them versatile
regarding power factor correction and voltage control [76].
The technology selected depends on the specific needs of
each system and the characteristics of the network. Therefore, it is essential to consider relevant aspects such as the
required power capacity, the necessary compensation speed,
and flexibility and control capabilities to adapt to system
parameters.
The integration and management of these devices have
been the subject of multiple studies, the main objective of
which is to optimize the operating aspects of EDS. Some decision variables extensively studied in the specialized literature include the location, sizing, and reactive power injection
or absorption requirements [77].
It is also possible to combine different types of DERs
to dynamically compensate the active and reactive power
requirements of an EDS, as is evident in the case of PVSTATCOMs, or photovoltaic-based static synchronous converters. These systems are used in medium-voltage distribution networks to dynamically compensate for the active and
reactive power generated by DG sources [78]. Control via
PV-STATCOMs optimizes the use of PV inverter capacities
and maximizes the utilization of the available solar energy.
In addition, this allows them to function as a FACTS (flexible alternating current transmission systems), facilitating a
dynamic reactive power exchange that dampens power oscillations in the EDS [79]. PV-STATCOMs provide variable
reactive power from an alternate source, which adjusts to the
load demand. Additionally, they reduce dependence on the
conventional grid for both active and reactive power. Their
main function is to act as voltage regulators and compensators for fluctuations in reactive power. These devices are
designed to dynamically adjust the supply of reactive power
to the loads connected at the point of common connection in
a grid-connected PV system [80], [81].
BESS can also be integrated with reactive power compensation devices. In this case, the STATCOM device, being a
voltage source converter, can supply reactive power to the
system, injecting or absorbing it as needed. Likewise, BESS
can store or release power, either active or reactive. The
integration of these two technologies allows for a proper control of system voltage and frequency profiles, thus impacting
system efficiency and reliability [82].
4) Demand management systems
Particularly, if energy management by DGs and BESS cannot
ensure continuity of service or achieve the objectives set by
the grid operator, it is possible to consider the disconnection
of non-critical loads in the system. This disconnection must
be carried out carefully, without exceeding the minimum
demand limits established for critical loads within the system
[83].
Finally, it is important to highlight that the integration
and management of DERs allows designing strategies aimed
at improving technical conditions, such as energy losses,
voltage profiles, and current flows. It also improves economic
aspects, such as investment and operating costs, and it has
an impact on environmental aspects, e.g., the reduction of
greenhouse gas emissions. However, DERs involve different
decision variables that, added to the operating constraints
associated with EDS, turn their integration and management
into a multi-variable problem of high complexity.
D. MATHEMATICAL COMPLEXITY IN THE INTEGRATION
AND MANAGEMENT OF DERS WITHIN EDS
The integration and management of DERs in EDS is difficult
to solve from a mathematical point of view. The electrical
variables of a system of this nature exhibit nonlinear behaviors, and some relationships used to determine their operation
are stochastic [84]. In this context, optimization problems
exhibit non-convexities that prevent determining whether the
solutions found are in fact the best ones. Likewise, DG, storage, and reactive power compensation devices incorporate
decision variables representing the DERs’ mode of operation
[85].
Non-convexities arise due to the presence of multiple
non-linear constraints and objective functions, which may
stem from various sources such as the interactions between
different components of the electrical system, DER operating
constraints, and system dynamics [86].
The interaction between DERs and the rest of the electrical
system can generate non-convexities. For instance, the presence of multiple generation sources and the temporal and
spatial variability of renewable generation can lead to nonlinear power balance constraints. These constraints can create
non-convex regions in the solution space, complicating the
design of optimal operation strategies [87].
1) Nature of the variables
Any strategies for integrating and managing DERs must
incorporate variables of a non-linear and non-convex nature
which represent the electrical behavior of the system. These
can be binary, discrete, or continuous.
Many DERs exhibit nonlinear behaviors, which can be
attributed to effects such as component variability and operating constraints. The accurate modeling of these nonlinearities
is a complex issue. Additionally, analyzing the impact of
integrating DERs into a EDS requires evaluating the power
flow of the system, which, given the nonlinear nature of
the electrical variables involved, can result in equations that
VOLUME 4, 2016
7
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3387400
This work is licensed under a Creative Commons Attribution-Non Commercial-No Derivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

---


### Page 8

are difficult to solve and may require the use of numerical
methods.
To determine the type of technology, location, sizing,
and power injection level of each device, a mathematical
model must include variables of binary and continuous nature
[88]. In the case of DG, the location of the generators is
represented through discrete variables indicating the nodes
of the system in which they should be installed. Likewise,
to determine the power injection level and the nominal size
of these generators, variables of a continuous nature are
used. As for BESS, the type of technology is represented
by binary variables, the location of the devices by discrete
variables, and both the state of charge and the nominal size by
continuous variables [89]. Similarly, the location of reactive
power compensation devices is represented through discrete
variables, and aspects such as their nominal size and the
amount of power to be injected or absorbed by them are
represented using continuous variables [90].
Finally, the integration and management of DERs is a
mixed-integer nonlinear linear programming (MINLP) problem that, when represented through a mathematical model, is
highly complex to solve.
2) Mathematical formulation
The mathematical formulation necessary to represent the
operation model of a distribution system in a context of
DER integration considers objective functions that seek to
optimize various aspects. In the specialized literature, these
aspects are technical [91], economic [92], and environmental
[93] in nature.
Regarding the technical objective functions used, one of
the most studied aspects is the minimization of energy losses
(min Eloss), which is mathematically formulated as shown in
Equation (1).
min Eloss =
X
h∈H
X
l∈L
Rl I2
l ∆h
(1)
In the given expression, Rl represents the resistance of line
l; Il denotes the magnitude of the current flowing through
line l; and ∆h corresponds to an interval in which the
electrical variables remain constant. It is crucial to note that
H spans all time periods, while L encompasses all the lines
in the EDS.
Similarly, among the economic objectives of further analysis, it is possible to find the reduction of operating costs
(min Ecost). These costs are represented in the purchase of
energy from conventional generation sources (f1) and in the
costs of DER operation and maintenance (f2), as can be seen
in Equation (2).
min Ecost = f1 + f2
(2)
To calculate f1 and f2, factors such as Ck W h and CO&M
are used to represent the average cost of acquiring energy
from the conventional grid and the operation and maintenance costs of DERs, respectively. This is shown in Equations (3) and (4).
f1 = Ck W h
 X
h∈H
X
i∈N
P cs
i,h∆h
!
(3)
f2 = CO&M
 X
h∈H
X
i∈N
P DERs
i,h
∆h
!
(4)
In Equations (3) and (4), ∆h represents the period during
which the electrical variables remain constant. In addition,
N represents all nodes, and H all periods of EDS operation.
Likewise, P cs
i,h and P DERs
i,h
represent the power injected by
the conventional generators and DERs (respectively) connected to node i during the time period h.
From an environmental point of view, the minimization of
CO2 emissions (min ECO2) has attracted great interest in
recent years [26]. In this vein, a CO2 emissions factor associated with conventional power generation sources (FEcs) is
used, as shown in Equation (5).
min ECO2 = FEcs
 X
h∈H
X
i∈N
P cs
i,h∆h
!
(5)
It is also important to keep in mind that the system has a
number of operating constraints that must be mathematically
modeled in order to analyze its behavior in the face of DER
integration. One of the most studied corresponds to the nodal
active and reactive power balances, as shown in Equations (6)
and (7).
P cs
i,h + P DERs
i,h
−P d
i,h = Vi,h
P
j∈N
Yij Vj,h Cos (θi,h −θj,h −φij) ,

∀i ∈N
∀h ∈H

,
(6)
qcs
i,h + q DERs
i,h
−Qd
i,h = Vi,h
P
j∈N
Yij Vj,h Cos (θi,h −θj,h −φij) ,
∀i ∈N
∀h ∈H

,
(7)
In these equations, P cs
i,h and qcs
i,h represent the active and
reactive power supplied by conventional sources connected
to node i during period h, while P d
i,h and Qd
i,h indicate the
active and reactive power demanded at node i during the
same period. Furthermore, P DERs
i,h
and q DERs
i,h
represent the
active and reactive power injected at node i by DERs during
period h. The terms Vi,h and Vj,h denote the magnitude of the
voltage at nodes i and j (respectively) during time h, while
θi,h and θj,h express the voltage angle at nodes i and j for the
same period. Additionally, Yij is the admittance magnitude
of the line connecting nodes i and j, and φij represents the
angle of the admittance of that line.
The limits regarding active and reactive power in conventional generators and DERs are also commonly taken into
account and can be represented through Inequalities (8), (9),
(10), and (11).
P cs,min
i
≤P cs
i,h ≤P cs,max
i
,
∀i ∈N
∀h ∈H

(8)
8
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3387400
This work is licensed under a Creative Commons Attribution-Non Commercial-No Derivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

---


### Page 9

Qcs,min
i
≤Qcs
i,h ≤Qcs,max
i
,

∀i ∈N
∀h ∈H

(9)
P DERs,min
i
≤P DERs
i,h
≤P DERs,max
i
,
∀i ∈N
∀h ∈H

(10)
QDERs,min
i
≤QDERs
i,h
≤QDERs,max
i
,
∀i ∈N
∀h ∈H

(11)
In these inequalities, P cs
i,h and Qcs
i,h represent the active and
reactive power bought from or injected by the conventional
generator at node i during the time interval h. Likewise,
P cs,min
i
and P cs,max
i
denote the minimum and maximum
active power assigned to the conventional generator at node
i, while Qcs,min
i
and Qcs,max
i
represent the minimum and
maximum reactive power assigned to the same generator.
Additionally, P DERs,min
i
and P DERs,max
i
are the minimum
and maximum active power assigned to the DERs according
to system needs. QDERs,min
i
and QDERs,max
i
are the minimum and maximum reactive power assigned to the DERs.
Other important constraints include nodal voltage limits,
represented by Inequality (12), and current limits, as shown
by Inequality (13) [26].
V min
i
≤Vi,h ≤V max
i
,

∀i ∈N
∀h ∈H

(12)
Il,h ≤Imax
h
,
 ∀l ∈L
∀h ∈H

(13)
Here, V imin and V imax are the minimum and maximum
voltages allowed, respectively. Moreover, Il, h denotes the
current flowing through line l during the time period h, and
Ihmax is the maximum current allowed for each line.
In addition to these constraints, the integration model for
different types of DERs may have constraints associated with
the operation of each device, such as the type of technology
and load and discharge percentages (in the case of BESS),
as well as constraints related to the economic feasibility of
integrating and managing these devices [24].
To the best of our knowledge, there is currently no DER
integration model that allows including all the constraints
associated with the operation of each device. Moreover, only
a few research works address two or more objective functions
simultaneously [94]–[96], which poses a challenge due to
the mathematical complexity involved in the multi-variable
integration of such a problem.
Finally, it is important to highlight that, while optimizing
a single objective may be beneficial for EDS operation, it
is essential to note that the real challenges faced by grid
operators require methodological approaches that address the
simultaneous optimization of multiple aspects. However, the
main complexity of multi-objective optimization lies in the
potential existence of conflicts between the functions to be
optimized. This forces grid operators to develop strategies
allowing to optimize their operation according to their specific interests and to apply expert judgment with the purpose
of selecting the best option [97].
E. ASSESSING THE IMPACT OF DERS ON EDS
The mathematical problem regarding the operation of EDS
is difficult to solve due to the nature of these systems and
their associated variables. A good operation strategy for this
type of system must have tools to evaluate the electrical conditions of the network under different scenarios. Likewise,
they should allow quantifying the impact of DER installation on important operating aspects. Power flow analysis is
an effective tool that provides relevant information about
the operation of a system at a given time. It is used to
describe the energy transfer between different nodes and is
based on Kirchhoff’s laws. Its mathematical model relates
impedances, currents, voltages, and power in the different
elements of the network [98].
1) Power flow
The power flow problem allows for a diagnosis of the system
based on the power demanded and generated within it while
using the parameters of the electrical system (bus types
and location, as well as data on the lines and the constant
impedances at the nodes) [99]. By analyzing initial data
such as the power delivered by the generators and the power
demanded by the consumers, the voltages at each of the system’s nodes are calculated for a permanent regime. Likewise,
the active and reactive power flows in each of the system
components (lines, transformers, reactors, and capacitors) are
calculated in order to guarantee a global power balance. The
power flow problem allows verifying the operating conditions of an EPS, for which two stages are employed. The first
one seeks to determine the complex voltages of all nodes by
solving the system of nonlinear equations representing the
problem. The second one uses the results from the first stage
and, by means of routine calculations, determines the active
and reactive power flows and losses of the elements, as well
as other technical, economic, and environmental indicators
required by the network operator [100].
The nodal voltage method is fundamental for analyzing the
power flow of distribution systems. Through the magnitude
and angle of the voltage at each node, it allows determining
some relevant variables associated with the operation of the
system. To perform this analysis, a set of algebraic equations
is taken into account, which employ six variables of interest
to characterize electrical behavior (voltage magnitude, voltage angle, active power generated, active power demanded,
reactive power generated, and reactive power demanded)
depending on the type of node evaluated – some of these
variables may be known. In distribution systems, two types of
nodes are analyzed. First, there is the slack node, considered
to be the strongest in the system and characterized by its ability to compensate for active and reactive power oscillations,
as it can control the voltage in the system. The second type
of node is the PQ node, to which the loads are connected.
VOLUME 4, 2016
9
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3387400
This work is licensed under a Creative Commons Attribution-Non Commercial-No Derivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

---


### Page 10

For this node, the active and reactive power consumption
is known. The goal of this analysis is to determine the
magnitude and angle of the voltage. In addition, only energy
consumptions are considered [99].
The main objective of power flow analysis is to determine
the magnitude and angle of the voltage present at each of the
nodes. With these data, and through the mathematical formulation that represents the power flow problem, actions can be
proposed to control important aspects of the distribution system. The power flow is obtained from the net power injected
(S). Therefore, the contribution of each node to the system
must be taken into account. This contribution is positive if
it comes from a generation node (Sg), negative if it comes
from a load or a demand node (Sd), or zero if it is associated
with a pass-through node without generation or consumption.
Equation (14) represents the net power injected.
S = Sg −Sd
(14)
The power input at node k (represented by Sk) is determined by the voltage (Vk) and the conjugate current (Ik)
according to Equation (15).
Sk = Vk∗Ik
(15)
To simplify the mathematical model, it is convenient for
the current to not be conjugate. This results in the expression
shown in Equation (16).
Sk = Vk Ik
(16)
Using the concept of nodal admittance (Y ), it is possible
to correlate the currents and voltages of each node in matrix
form, as demonstrated in Equation (17).


I1
Ik
In

=


Y11
Y12
Y13
Yk1
Ykk
Ykn
Yn1
Ynk
Ynn




V1
Vk
Vn


(17)
The current at node k (Ik) can be found through Equation
(18).
Ik =
n
X
j=1
Ykj∗Vj
(18)
Finally, by replacing the above value into Equation (16),
the general formulation of the power flow problem is obtained, as seen in Equation (19).
Sk = Vk
n
X
j=1
Ykj∗Vj
(19)
The expression shown above has real and imaginary terms
and is composed of non-linear equations that make it difficult
to solve. Therefore, it is common to find different mathematical methodologies that allow determining the power flow
through each node via computational tools. These methodologies are compared with a view to optimize some relevant
factors, such as data processing times, repeatability, and
convergence.
2) Power flow evaluation methods
The focus of this paper is on radial networks, as they are most
commonly used in designing distribution power systems.
These networks have a single slack node, for which the
voltage is known, and the remainder are demand nodes with
an unknown voltage. This allows separating the system into
components associating generation buses with generation
buses (Ygg), generation uses with demand buses (Ygd), demand buses with generation buses (Ydg), and demand buses
with demand buses (Ydd), as shown in Equation (20).

Ygg
Ygd
Ydg
Ydd
 
Vg
Vd

=

Ig
Id

(20)
From the expression shown above, and considering Equation (19), it is possible to express this relationship through
Equation (21).
Sg −Sd = Diag(V )(Ybus)V
(21)
However, taking advantage of the aforementioned characteristics of radial grids, this expression can be divided into
one equation for the slack node, i.e., Equation (22), and
another one for the demand nodes, i.e., Equation (23).
Sg = Diag(V g)(Ygg V g + Ygd V d)
(22)
−Sd = Diag(V d)(Ydg V g + Ydd V d)
(23)
Equation (22) is linear, so there are no major complications
when solving it. However, Equation (23) exhibits a non-linear
behavior, since the demand voltages are not known.
In the specialized literature, several methods are used to
solve the power flow problem, which can be adapted to analyze both single- and three-phase systems. In the case of the
latter, more variables must be taken into account. This greater
mathematical complexity leads to an increase in computational efforts and inevitably results in considerably increased
processing times. Among the traditional approaches are some
numerical methods such as the Gauss-Seidel and the NewtonRaphson techniques, which use iterative processes to find the
solution to the problem [26]. In in each iteration of the GaussSeidel method, the values of the stresses are sequentially
updated, gradually converging to the solution. The above
makes this method suitable for determining the power flow
in small EDS [101]. On the other hand, in the NewtonRaphson method, the variables are not updated sequentially,
and each iteration involves a recalculation through the use of
a Jacobian matrix that includes their partial derivatives, leading to a faster convergence in comparison with the GaussSeidel method [102]. This technique is suitable for solving
the power flow of large EDS. However, the solution of the
Jacobian matrix requires a larger number of simultaneous
computations, which makes its implementation more computationally intensive [103].
Another, more recent method to solve the power flow is
the successive approximations method (SA). This method is
10
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3387400
This work is licensed under a Creative Commons Attribution-Non Commercial-No Derivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

---


### Page 11

based on the Gauss-Seidel approach, with the main difference
being the possibility of dealing with the variables directly in
their complex form, which eliminates the need to perform
transformations that ultimately result in a greater mathematical complexity and, therefore, in greater computational
challenges [104].
Other alternatives can be found in the literature, such as the
iterative sweeping method and the triangular method, which
may be useful depending on the specific characteristics of
each system [105].
The iterative sweeping method is similar to the SA method,
and its mathematical formulation does not require derivatives
to obtain the variables. However, the nodal voltages are
distinguished from the voltages in the branches of the system.
The directions of the currents flowing through the lines are
assumed, and their effects are represented by a node-branch
incidence matrix. During the iterative process, all variables
are updated simultaneously from their most recent values,
which prevents the dependence between variables in each
iteration. This method may be appropriate for analyzing large
systems, but its convergence depends on a good estimation
of the initial parameters [105]. As for the triangular method,
its mathematical formulation is derivative-free and, like the
iterative sweeping method, it differentiates between nodal
and branch voltages. The main difference lies in the use of
a triangular matrix representing the nodal currents carried
by each of the branches. Its processing times are reduced
because some components of the mathematical formulation
are only calculated once and not in each iteration [105].
3) Relevant aspects in power flow assessment
Power flow assessment in EDS under DER installation scenarios allows determining the impacts associated with the
integration of each device. This evaluation usually requires
a significant number of iterations depending on the size of
the system and the number of variables integrated into the
mathematical model. To solve the flows, computational tools
are used which, depending on the complexity of the model,
demand specific computational loads and processing times
[106].
A good integration and management strategy must ensure
computational efficiency in evaluating power flows, and it
must also obtain solutions in reasonable times. This is important, considering that the time used to solve the power
flows increases exponentially with respect to the number of
variables in the problem [106].
Another important point of the evaluation has to do with
the repeatability of the obtained solutions, which indicates
their quality and reliability. In addition, this helps network
operators to make better decisions according to the behavior
of the system [106].
Finally, it can be stated that the challenges associated
with the operation of EDS and the fact that systems may
or may not be connected to large EPS necessitate strategies
integrating DERs in both grid-connected and isolated areas.
These strategies require tools such as power flow analysis,
which allows evaluating the operating conditions of the grid
under different scenarios.
4) Impact on the operating aspects the EDS
DERs improve various operating aspects of EDS, with an
impact on their technical, economic, and environmental conditions. Each DER has unique characteristics and different
impacts.
DG devices can inject active power at different points
within the grid, which reduces the need to transport energy
from conventional generation sources to the load. This reduces energy losses, improves the voltage profile at each
node, and reduces the electric current flowing through the
system. All this is reflected in a higher efficiency, a more
reliable system, and a higher-quality power supply [107].
BESS complement the operation of DG devices by storing energy in times of excess generation and releasing it
according to system demands. This, in addition to reducing
energy losses, improving voltage profiles, and reducing current flows, allows for a proper system control and affects the
operating frequency, which translates into a greater reliability, efficiency, and quality of the power supply [108].
Lastly, reactive power compensation devices can inject or
absorb reactive power depending on the needs of the network.
For power factors affected by capacitive components, the
main objective should be to inject reactive power. Although
it is not common in EDS, scenarios may arise where this
contribution is required. On the contrary, for EDS with power
factors impacted by inductive components, the interest shifts
towards the absorption of reactive power [109]. In both
scenarios, the aforementioned devices have an impact on
important system variables, e.g, the power factor, the voltage
profiles at the nodes, and the current flowing through the
lines. This is reflected in the efficiency, reliability, and quality
of the power supplied by the EDS [22].
F. APPROACHES FOUND IN THE SPECIALIZED
LITERATURE FOR THE ENERGY MANAGEMENT OF
DERS IN EDS
During the last few years, different strategies have been
developed in order to manage DERs in EDS through different optimization methods. These strategies seek to improve
technical aspects such as energy losses, voltage profiles, and
current flows. They also address economic aspects, as is the
case of investment and operating costs, and consider environmental aspects such as greenhouse gas emissions reduction.
The most explored approaches are analytical, numerical,
heuristic, and metaheuristic in nature. It is also common to
find a combination between some of these, which may be
convenient depending on the characteristics of the problem
to be solved [26].
1) Analytical approaches
Analytical approaches are based on theoretical analysis
through mathematical models representing the relationships
between the electrical components of the system, which
VOLUME 4, 2016
11
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3387400
This work is licensed under a Creative Commons Attribution-Non Commercial-No Derivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

---


### Page 12

allows obtaining exact solutions when the proposed model
is linear and convex. However, one may find that DER
integration and management problems are mostly non-linear
and non-convex, which would demand an excessive computational load and prohibitive solution times. Among the
most commonly used optimization methods for the analysis of DERs are linear programming techniques, useful
for optimizing the location and sizing of generators, and
quadratic optimization techniques, which allow optimizing
the use of reactive power compensation devices. Nonlinear
optimization techniques are also widely used and contribute
to the analysis of nonlinear constraints within the system,
such as generation limits, nodal current limits, and current
limits across distribution lines [110].
2) Numerical approaches
Numerical methods allow finding solutions that are reliable
and of good quality. In addition, they help to solve optimization problems of a non-linear and non-convex nature,
which are typical of EDS. They allow the optimization model
to include important equality and inequality constraints in
analyzing the feasibility of solutions. Their reliability depends on the accuracy of the data entered into the model,
and their convergence is sensitive to the initial conditions
of the problem [111]. It is important to note that they are
appropriate for addressing optimization problems in systems
of different sizes. However, the processing times and computational load required to find the solutions is proportional
to the number of variables and constraints in the problem,
which, for large EDS, can lead to prohibitive times. Among
the most commonly used approaches are the Gauss-Seidel
and Newton-Raphson methods, useful for analyzing optimal
power flow and network stability problems [102].
3) Heuristic approaches
Heuristic methods, on the other hand, are based on simple
and intuitive rules and do not use precise mathematical calculations, which directly impacts aspects such as computational
efforts and processing times. However, they do not guarantee
that the solution found is indeed the best one, as they may
get stuck in local optima [112]. They are appropriate for
solving optimization problems that combine a large number
of variables and require a simplistic exploration and exploitation of the solution space. They usually converge quickly,
finding acceptable solutions in reasonable periods of time.
Because these types of techniques are used with practical
and specialized approaches, they do not employ recognized
algorithms, and, on the contrary, they use the knowledge
of a given problem to propose algorithms that adapt to the
characteristics of each problem [112].
4) Metaheuristic approaches
Metaheuristic methods share some similarities with heuristic
ones. However, metaheuristic methods are solved exactly by
finding approximations to the global optimal solution. In
addition, the greatest difference lies in their efficiency. Metaheuristic techniques are characterized by the fact that they
are based on mathematical and structured principles, which
allows them to approach different optimization problems in a
systematic way. They are appropriate for solving combinatorial problems of a non-linear and non-convex nature, which
is typical of large-scale EDS. Given their stochastic nature, it
cannot be guaranteed that, through this type of method, any
of the solutions found will be the best one. Nevertheless, they
allow finding solutions of very good quality under a moderate computational load and in acceptable processing times.
Among the most widely used techniques is the particle swarm
optimization (PSO) algorithm, which allows determining the
location and sizing of devices and, in some cases, the type of
technology to be used. It is also common to find the use of
genetic algorithms (GAs) to analyze the behavior of EDS.
In general, different metaheuristic optimization techniques
are employed in the specialized literature to address the
optimization problem regarding EDS operation in the context
of DER installation. However, the optimization technique
selected will depend on the type of problem to be solved and
on the nature of its variables [113].
III. ANALYSIS OF THE ADVANCES MADE IN THE
SPECIALIZED LITERATURE
Considering the growing number of publications on this
topic, a search for articles published since 2018 was performed in different databases, i.e., Science Direct, IEEE, and
Scopus. For this search, keywords such as DG, BESS, reactive power compensation, optimization techniques, and siting
and sizing were used, among others.
Figure 6 shows the recent increase in the number of studies
on the topic.
FIGURE 6: Related publications per year
Figure 7 shows the distribution of subject areas with regard
to related publications.
It can be seen how many authors seek to improve the
operation of EDS through the integration and management
of a single DER technology. However, strategies that simultaneously integrate and manage DG, BESS, and compensation devices have sparked great interest in recent years,
and most of the reported works seek to optimize scenarios
involving the integration of two or more technologies. In
addition, the reported works also differ in the way they an12
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3387400
This work is licensed under a Creative Commons Attribution-Non Commercial-No Derivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

---


### Page 13

FIGURE 7: Related publications per subject area
alyze power distribution. Some studies propose optimization
models based on the analysis of single-phase equivalents.
This type of equivalent simplifies the analysis by ignoring
the imbalances inherent to the operation of EDS. This means
that the improvements obtained do not represent solutions to
the real problems. On the other hand, there are studies that
use models analyzing the problem while considering a threephase operation, which results in useful tools for network
operators.
A. STRATEGIES ADDRESSING THE INTEGRATION AND
MANAGEMENT OF A SINGLE TYPE OF DERS
This section presents some of the works reported in the specialized literature which contain strategies for the integration
and management of a single type of DER. For each work,
the type of technology, the decision variables, the objective
functions, and some relevant aspects are described, such
as test scenarios, their corresponding equivalent (single- or
three-phase), and the main findings.
• The research conducted by Purlu et al. presents a strategy to determine the optimal power factor, the best
locations, and the best power injection level for different types of DG [114]. Using the PSO technique, the
authors define some operating aspects of the system
as the optimization objectives: the annual reduction
of energy losses and the improvement of each node’s
voltage profiles. To validate their results, they use the
33-node test system, which, through an analysis based
on the single-phase equivalent, allows quantifying the
improvements obtained by the proposed algorithm, as
well as comparing the results against those of other algorithms. Among the most relevant results of this research,
the authors highlight energy losses reductions of 39.8%
with the installation of PV generators and of 64.3% with
the implementation of wind turbines. However, energy
storage and compensation devices are not taken into
account, and the economic and environmental aspects
inherent to this type of project are not analyzed.
• The work by Tianming et al. [115] proposes a strategy to
optimize the operating aspects of EDS with DG devices.
This is done through the integration of a BESS and
the proper placement and sizing of storage devices. To
this effect, the authors employ an improved version of
the non-dominated sorting genetic algorithm II (NSGAII), which focuses on reducing the energy losses of
the system and improving the voltage profiles of each
node. To validate the results of the proposed strategy, the
authors use a 33-node, single-phase radial test system.
The implemented optimization technique was compared
against the traditional NSGA-II algorithm and the multiobjective particle swarm optimization (MOPSO) algorithm.
Among the most relevant results reported by the authors, an improved solution repeatability stands out in
comparison with the NSGA-II and MOPSO techniques.
However, the authors do not provide information on
the processing times required by each algorithm. In
addition, the base case involves DG devices with fixed
location and sizing. If not optimized, these aspects condition the improvements obtained. Moreover, reactive
power compensation devices are not included, which,
as in the case of DG, could improve the impacts on the
studied EDS. Finally, it is important to highlight that the
analysis was conducted using a single-phase equivalent,
which, although useful for this type of problem, does
not represent the real behavior of a three-phase EDS.
• Nezhad et al. developed a strategy to manage DG
units via a fuzzy decision-making method (FDMM)
[94]. They used the multi-objective improved manta
ray foraging optimization (MOIMRFO) algorithm to
determine the correct placement and sizing of each
device in order to minimize energy losses and improve
voltage profiles. This strategy was implemented in a 33node three-phase unbalanced test system under variable
generation and load conditions, which allowed quantifying the improvements obtained and comparing them
against those of other optimization techniques reported
in the literature. Among the most relevant results, the
authors highlight a 9.8% reduction in energy losses, a
25% reduction in the nodal voltage imbalance, and a
12% improvement regarding unserved energy. However,
this work does not include energy storage and compensation devices, it does not analyze the repeatability of
the solutions, and it does not quantify the processing
times required by each solution. In addition, the analysis
fails to include the relevant economic and environmental
aspects of this type of projects.
• The work presented by Nassef et al. [116] proposes
a methodology to reduce energy losses through the
optimal allocation of biomass DG units in EDS. Using
a modified version of the hunger game search (HGS)
algorithm, the authors propose the location, sizing, and
power factor of the DG sources as decision variables
in a single-objective optimization environment. The 33-
, 69-, and 119-node test systems are used to validate
this methodology in single-phase balanced systems.
VOLUME 4, 2016
13
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3387400
This work is licensed under a Creative Commons Attribution-Non Commercial-No Derivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

---


### Page 14

Among the main findings, the authors report energy
losses reductions of 94.49% for the 33-node system,
97.68% for the 69-node system, and 88.79% for the
119-node system. However, the published results do not
allow determining the repeatability or the processing
times required. In addition, when performing an analysis under a single-phase equivalent, the line imbalances
corresponding to the real operation of these systems
are not considered. It is important to highlight that
the study is limited to a technical analysis and does
not include the review of economic and environmental
aspects. Furthermore, it only focuses on the integration
of DG sources and does not analyze the possibility of
installing other types of DER such as BESS and DSTATCOMs.
• The research carried out by Cortés et al. [24] seeks to
reduce energy losses and minimize CO2 emissions by
correctly selecting the technology, location, and sizing
of BESS in microgrids with the presence of DG devices.
Through the formulation of a MINLP model, the authors
use a master-slave methodology based on optimization
algorithms, such as the Chu & Beasley genetic algorithm (PCBGA) and the vortex search algorithm (VSA).
In addition, using the SA method to evaluate the power
flow, the results of this strategy are validated on the 33node test system. Among the main findings, the authors
highlight the improvement of the microgrid’s operating
aspects and the mitigation of CO2 emissions, reducing
dependence on traditional sources that use fossil fuels
for power generation.
This analysis used a single-phase equivalent; it failed to
consider a relevant aspect of real operation: the imbalance of the three-phase distribution lines. It is important
to mention that, as the evaluation was performed under
a scenario where the DG sources had already been
installed, the technical, economic, and environmental
aspects associated with the location and sizing of this
technology were not optimized. In addition, the authors
highlight the need for future work that integrates other
optimization techniques while addressing the problem
from a multi-objective perspective, thus allowing to
simultaneously optimize different aspects.
• Cikan et al. [117] propose a methodology to determine
the location, size, connection type, and power factor of
three different technologies related to the installation of
DG installation in unbalanced three-phase systems. This
methodology is based on the equilibrium optimization
(EO) algorithm, which is inspired by the behavior of
animals in nature. The EO algorithm delivers candidate
variables to a three-phase backward and forward unbalanced power flow (UBFLF) evaluator, which allows
determining the impact of each proposed solution. The
authors use the 123-node IEEE system as a test scenario
for their methodology. This test feeder has been barely
explored in the specialized literature.
This work was modeled using the MATLAB environment and simulated in Simulink, IEEE PES, and
Open DSS. For comparison, the authors used six optimization algorithms that have been widely explored in
the literature and applied to the research problem. These
were implemented under the same conditions as the EO
algorithm and helped to demonstrate the improvements
obtained by the proposed method in terms of processing
times, repeatability, and some statistical variables.
Finally, as the main results of their research, the authors present a decrease in energy losses of 92.59%
and improvements in voltage profiles when installing
nine distributed generators. This, in comparison with
the base case. However, they do not address the current
imbalances in the distribution system lines, an inherent aspect of DG systems. Validations under scenarios
with variable generation and power demand were also
not carried out, which is fundamental in studying DG
systems. In addition, the scope of this research was
limited to single-objective optimization, focusing on the
operating aspects of the network. This hindered the
evaluation of impacts on economic and environmental
aspects.
• Mohan et al. focus on improving the operating conditions of BESS in the presence of renewable DG [118].
Through the correct placement and sizing of BESS,
the authors suggest improving aspects such as nodal
voltage profiles and system power losses. To this effect,
they use an optimization algorithm called the water
cycle algorithm (WCA), which, after being evaluated in
test systems with 33 and 43 single-phase nodes, shows
improvements with respect to the base case in relevant
aspects such as the deviation of voltage levels at each
node and the reduction of power losses. The authors also
perform an analysis of the processing times required
by this strategy, which, in comparison with techniques
such as PSO and the gravity search optimization algorithm (GSA), takes less time to find the solutions to
the problem. However, the single-phase approach of the
analysis does not allow considering the typical imbalances of real operation. In addition, this research does
not allow quantifying the economic and environmental
impact of this type of strategies, implying the need for
future works that integrate different objective functions
into a multi-objective optimization model within the
framework of a three-phase analysis.
• The work presented by Ali et al. [119] proposes a
methodology to improve the operating conditions of
EDS through the correct integration of DG units. To this
effect, the authors use a hybrid optimization algorithm
that combines the qualities of the PSO algorithm and the
sine-cosine algorithm (SCO). In a multi-objective optimization environment, the authors suggest improving
key aspects such as the energy losses, voltage profiles,
and line imbalances of three-phase distribution systems.
To validate the efficiency of the proposed methodology,
the authors used test systems of 13, 37, and 123 nodes,
14
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3387400
This work is licensed under a Creative Commons Attribution-Non Commercial-No Derivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

---


### Page 15

and they compared the results obtained against the PSO
and SCO algorithms, which were used separately. The
authors report reductions of 89% in energy losses, 21%
in the imbalance index, and 70% in the voltage profile
index for large-scale systems. However, they do not
evaluate the repeatability and processing times of the
solutions obtained. Energy storage and reactive power
compensation devices are not included either, which
would allow for an integral management of the network.
It is important to mention that the technical analysis
performed does not allow quantifying the improvements obtained in economic and environmental aspects
transversal to this type of integration.
In summary, each of the previously proposed strategies
suggests decision variables tailored to the characteristics of
each scenario. Notably, the locations and power injection
levels of different types of DERs are considered, given their
potential impact on the operating aspects of the EDS. For
instance, installing a DG source at a specific node may reduce
the need to transport energy over long distances, consequently decreasing associated transmission losses. Additionally, this device can reduce the system’s reliance on conventional generation, impacting operating costs and polluting gas
emissions. Another decision variable of interest is the power
factor, given the multiple benefits of optimizing it within a
system, including reduced line currents and improved voltage
profiles at each node.
In addition to the above, it is important to note that
several authors utilize widely explored optimization techniques. Some examples include algorithms such as PSO,
MOIMRFO, HGS, PCBGA, NSGA-II, and FDMM, among
others. Thes algorithms differ from each other primarily in
the way they explore and exploit the solution space. This
defines the evolution of possible solutions and impacts their
convergence, determining relevant aspects such as processing
times and computational load.
The proposed strategies address the operational challenges
of the EDS, such as energy losses, voltage profile variations,
and high line loads. To this effect, they utilize mathematical models that represent the behavior of the EDS in the
context of DERs integration. Furthermore, through different
optimization algorithms, the best scenarios for DERs integration and operation are defined. In this vein, power flow
validation tools are employed, allowing to understand the
impacts associated with the implementation of the proposed
solution.
It is important to mention the limitations of some studies,
as they do not integrate different types of DERs simultaneously. This is relevant, considering that these devices
often complement each other and can achieve significant
improvements by working together. The interaction between
different types of DERs can address challenges such as system stability and the need for dynamic response to variations
in EDS operation. For example, the intermittency associated
with generation from renewable energy sources can be mitigated through energy storage systems. These systems enable
storing power during intervals when the generation exceeds
the demand and supplying it during periods when the demand
surpasses the generated power. This contributes to enhancing
system stability and allows for a greater DERs penetration in
current EDS [120].
It is also important to highlight that some studies solely focus on improving a single objective, overlooking the opportunity to optimize other relevant aspects that are also impacted
by the integration and operation of DERs. Additionally, some
methodologies use equivalent single-phase circuits to model
the behavior of the EDS, which may limit the accuracy of the
results, as most EDS operate with three-phase systems for
energy transportation.
Ultimately, it is essential to emphasize that test systems are
an important validation tool that helps the scientific community to quantify the improvements obtained, especially when
the studied strategies cannot be validated in real situations.
However, key aspects such as the equivalent circuit used,
the quality of the solutions obtained, the processing times
required, and the type of optimization performed are of vital
importance to determine the reproducibility of simulations in
real EDS.
It is common for different authors to compare their results
based on the quantitative reduction of each objective function
value and the impact of decision variables on each element
of a test system. To this effect, it is essential to conduct an
evaluation of the initial conditions of the test system, which
will allow for such comparison. Additionally, it is possible to
compare different methodologies through statistical analysis,
in order to determine the repeatability of the solutions and the
processing times required to obtain them.
Table 1 presents a summary of the related works and their
main characteristics. It shows how technical objective functions have been the subject of different works, demonstrating
their relevance. However, economic and environmental aspects have been scarcely explored, which implies the need to
propose future works that address the integration of DERs in
scenarios aimed at optimizing these aspects. Likewise, there
is a clear need for strategies that operate in a multi-objective
context and are adjusted to the current needs of EDS. Finally,
it is important to note that some authors propose future
studies integrating different types of DERs.
B. STRATEGIES THAT ADDRESS THE SIMULTANEOUS
INTEGRATION AND MANAGEMENT OF DIFFERENT
TYPES OF DERS
Some works in the literature have developed strategies aimed
at simultaneously integrating and managing different types of
DERs, some of which are described below.
• The work presented by Campolina et al. [121] proposes
a strategy to determine the best location of DG devices
and capacitor banks (CBs) in EDS. To this effect, the
authors use a GA entrusted with improving operating
conditions and minimizing energy losses in unbalanced
three-phase distribution systems. The proposed optimization algorithm is responsible for determining the
VOLUME 4, 2016
15
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3387400
This work is licensed under a Creative Commons Attribution-Non Commercial-No Derivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

---


### Page 16

TABLE 1: Related works in the specialized literature and their characteristics
Ref.
DER type
Objective function
Strategy
Solution technique
used
Test
system
Equivalent
circuit
Variable
conditions
Comparison
with other techniques
Statistical
analysis
[114]
DG
Technical
Single-objective
PSO
33 nodes
Single-phase
Yes
Yes
Yes
[115]
BESS
Technical
Multi-objective
NSGA-II
33 nodes
Single-phase
No
Yes
No
[94]
DG
Technical
Multi-objective
MOIMRFO
33 nodes
Three-phase
Yes
Yes
No
[116]
DG
Technical
Single-objective
HGS
33, 69, and 119 nodes
Single-phase
Yes
Yes
Yes
[24]
BESS
Technical, economic,
and environmental
Single-objective
PCBGA and VSA
33 nodes
Single-phase
Yes
Yes
Yes
[117]
DG
technical
Single-objective
EO and UBFLF
123 nodes
Three-phase
No
Yes
Yes
[118]
BESS
Technical
Single-objective
WCA
33 and 43 nodes
Single-phase
No
Yes
No
[119]
DG
Technical
Multi-objective
PSO and SCO
13, 37, and 123 nodes
Three-phase
Yes
No
No
nodes of the EDS where the installation of DG and
CBs yields the best operational impacts, considering
factors such as voltage profiles, line load percentage,
and system stability.
In addition, they propose a methodology to reduce the
search space by analyzing the initial population of the
algorithm. To validate the effectiveness of their strategy,
they use test systems of 4, 7, 37 and 123 nodes in the
context of variable generation and demand. When comparing their results against those of different works using algorithms such as PSO and Montecarlo simulation,
they report a reduction of 60% in the computation times
required for each solution. However, by focusing on the
improvements made to the operation of the system, they
fail to consider the economic and environmental impacts
of the proposed strategy. They also do not take energy
storage systems into account and do not include decision
variables such as the power injection of the devices in
the optimization model. These authors propose future
work dealing with strategies to optimize aspects such as
line imbalances and nodal voltage profiles.
• Leng et al. propose a strategy for coordinated DER
operation that is based on a stochastic programming
model (SPM) [122]. The main objective of this strategy is to minimize energy losses and improve voltage
profiles in three-phase EDS within the framework of
single-objective optimization. To this effect, decision
variables such as power injection by storage devices and
the selection of different types of DG are employed.
The 34-node test system was used to validate the research results. Among the most relevant results is the
creation of a realistic strategy that enables the joint optimization of technical aspects with reasonable operating
costs. To demonstrate this, the authors use some strategies reported in the literature for the sake of comparison. However, they do not quantify the improvements
obtained with respect to the base case or consider the
locations of the devices as decision variables in the
optimization model. In addition, they do not analyze
the environmental impacts associated with the implementation of the strategy and fail to present a statistical
analysis of their results.
• Grisales et al. present a strategy for battery management
in urban and rural distribution networks under a scenario
of variable DG and power consumption [123]. Using
an improved version of the VSA, the authors propose
a single-objective optimization model in which different operating constraints are considered and technical,
economic, and environmental aspects of the network are
improved.
To validate the effectiveness of this strategy, the authors
employ test systems of 27 and 33 nodes adapted to
the characteristic generation and demand conditions of
two regions in Colombia, and, using a single-phase
equivalent, they analyze the operation of the system
before and after the implementation of their proposal.
Among the main results are the quality of the solutions
obtained in comparison with those of other algorithms,
as well as significant improvements in reducing energy
losses and CO2 emissions. Reductions of 4.29% and
7.4% in energy losses were observed in the urban and
rural scenarios. Additionally, reductions of 0.18% and
0.08% in CO2 emissions were recorded, respectively.
However, by analyzing a single-phase equivalent, the
authors fail to consider the behavior of a real threephase distribution system, and therefore the line imbalance inherent to it. It is important to highlight that a
multi-objective analysis of the proposed strategy could
provide a useful tool for decision-making by network
operators.
• The work by Ray et al. [124] proposes a strategy to
determine the optimal allocation of active and reactive
power devices in three-phase distribution networks, with
the objective of improving voltage profiles and reducing
energy losses. This strategy uses the SCO to establish,
under different variable load scenarios, the most appropriate power injection or absorption.
The authors use the 25-node test system to quantify
the improvements obtained, highlighting the enhanced
voltage profiles of each node, as well as reductions in
energy losses between 78.18% and 80.09% for different
load levels. However, it is important to point out some
limitations of this study, such as the absence of a statistical analysis to determine the quality of the solutions
obtained. Likewise, the processing times required to find
the solutions, a fundamental aspect in this type of strat16
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3387400
This work is licensed under a Creative Commons Attribution-Non Commercial-No Derivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

---


### Page 17

egy, are not indicated. In addition, there is no economic
or environmental analysis of the impacts associated with
the implementation of this approach.
• The research conducted by Radosavljevi´c et al. [125]
presents a methodology for the optimal allocation of
active and reactive power in EDS with the presence of
single-phase DG devices and BESS. The authors combine PSO with sigmoid-based acceleration coefficients
(PSOS) and a chaotic gravity search algorithm (CGSA)
within a single-objective optimization environment with
varying generation and demand conditions. The main
objective of this methodology is to reduce the losses
and costs associated with the purchase of energy from
traditional sources.
To carry out this study, the authors implemented the
proposed methodology in the three-phase 13-node test
system, comparing their results against those of other
optimization techniques such as PSO and a GA. A
22% reduction in daily energy losses and enhanced
nodal voltage profiles were observed. However, it is
important to note some limitations regarding their analysis. First, the research does not include an evaluation
of the environmental impacts associated with reduced
energy purchasing from conventional sources, which is
a relevant consideration in the current context of energy
sustainability. In addition, the proposed model does not
regard the current imbalance in each line as a constraint,
an aspect of vital importance to represent the real operation of EDS. No statistical analysis is performed to
validate the quality of the solutions obtained, nor are
details provided with regard to processing times.
• Kumar et al. present a strategy for the optimal integration of DG and energy storage systems in power
distribution grids [95]. This strategy is based on a multiobjective optimization model, whose decision variables
include the location and sizing of different DERs. The
authors use a multi-objective optimization algorithm
based on the velocity butterfly method (MOVBOA). The
main objective of this strategy is to minimize energy
losses and improve stress profiles in various test scenarios. The performance of the proposed strategy was
validated on 33-, 69-, and 118-node single-phase test
systems with variable demand and probabilistic generation. Significant improvements in voltage profiles and
reductions in energy losses were observed in the three
test systems. The reductions in energy losses were 80%,
91%, and 62% for the 33, 69, and 118-node systems,
respectively.
It is important to highlight that this work by Kumar
et al. lacks a statistical analysis to demonstrate the
repeatability of the solutions obtained. In addition, it
does not provide information on the processing times
employed by the algorithms. Furthermore, the analysis
is carried out using the single-phase equivalent of the
different test systems. Although these tools are useful
for evaluating optimization strategies, they do not allow
addressing the aspects inherent to the actual operation
of three-phase EDS, such as line imbalances.
• Kandasamy et al. [126] propose a distributed static synchronous compensation (D-STATCOM) and DG device
integration strategy for radial three-phase EDS. Using
multi-objective optimization and under time-varying
load conditions, their strategy uses the enhanced artificial bee colony (EABC) algorithm to determine the best
combination, placement, and power injection of DG and
D-STATCOM units.
The proposed mathematical model uses a multiobjective function aiming for power losses reductions,
current flow reductions, and nodal voltage profile improvements. To validate the effectiveness of the proposed strategy, test systems of 13 and 33 nodes are used.
With respect to the base case, the authors report a 43%
reduction in energy losses for the 13-node unbalanced
network, as well as 64% for the 33-node system. In
addition, they highlight the impacts on the nodal voltage
profiles and load reductions in the lines of the test
systems. However, they do not consider the effect of
their strategy on current balance, nor do they analyze
the economic and environmental impacts derived from
the implementation of DG and D-STATCOMs.
It is important to mention that this work does not present
any results obtained using other methodologies, which
would certainly be useful to quantify the improvements
made. In addition, the analysis of the solutions lacks
relevant information, such as processing times.
• Tahiliani et al. conducted a research focused on reducing energy losses and improving the operating aspects
of three-phase power distribution grids [127]. To this
effect, they proposed a methodology based on the atom
search optimization (ASO) algorithm, which allows
managing the power injected by DG and D-STATCOM
devices in variable load scenarios. This methodology
was validated using the 25-node test system, and improvements in voltage levels and reductions in power
losses were reported for several scenarios. However,
it is important to note that this study lacks crucial
information that would allow validating the repeatability
of the solutions and evaluating their processing times.
Furthermore, as variable generation scenarios are not
included, it is not possible to analyze the uncertainty
associated with the energy sources used in the study.
Finally, this research does not address the environmental
impacts of DER management.
• The work presented by Fardinfar et al. [69] proposes
a strategy to determine the optimal sizing and placement of DG and DSTATCOM devices in three-phase
distribution power grids. Through a hybrid optimization technique that combines the PSO algorithm and
Monte Carlo (MC) algorithm, the strategy allows improving the voltage profiles at each node and reducing
the energy losses associated with transport. Under a
single-objective optimization environment, the authors
VOLUME 4, 2016
17
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3387400
This work is licensed under a Creative Commons Attribution-Non Commercial-No Derivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

---


### Page 18

implemented the proposed strategy in a real distribution
system located in Kerman, southwestern Iran. The authors highlight, as one of the main contributions of the
proposed strategy, the development of a tool that helps
network operators with the design and planning of radial
distribution networks.
It is important to point out that the study lacks a statistical analysis to determine the quality of the solutions
obtained and their corresponding processing times. In
addition, it does not evaluate the economic and environmental conditions before and after the installation of
the DERs, which are fundamental aspects in this type of
project.
• In their research work, Giridhar et al. present a hybrid power system composed of DG, BESS, and DSTATCOM devices [128]. These devices aim to improve
energy losses in grid-connected systems and ensure an
independent supply for isolated areas. Regarding the
first objective, DG sources are exclusively integrated to
improve the operating aspects of networks that rely on
a conventional feeder. In the second objective, through
the simultaneous integration of the three devices, the
aim is to reduce dependence on conventional generation
sources. This, until energy independence is achieved.
For both cases, the research proposes an optimization
strategy whose decision variables correspond to the
siting and sizing of the devices.
In a context of single-objective optimization, the mayfly
algorithm (MOA) used allows finding appropriate values, which reduce the active power losses by 47.37%
and the reactive power losses by 42.89% in a system
with 33 single-phase nodes. Furthermore, according to
the authors, this strategy is effective in ensuring the
supply of electricity to isolated areas. However, the
analysis performed lacks information to estimate the
repeatability of the solutions and their processing times.
In addition, as the system is analyzed using a singlephase equivalent, the effects of line imbalance, which
is typical of real distribution systems, are not taken
into account. It is important to point out that this work
focused on the technical aspects of the system and did
not consider any economic and environmental aspects.
• The work presented by Sharma et al. [96] proposes an
operation strategy for different types of DERs which is
aimed at minimizing energy losses and energy purchasing from the grid. Through the multi-objective NSGAII, the authors elaborate a methodology that allows determining the optimal power dispatch of batteries under
variable demand and generation scenarios and in the
coordinated presence of wind sources and shunt CBs.
This strategy was implemented in the 33-node singlephase test system and a real 108-node distribution system. Among the main findings, the authors highlight
reductions of 77.97% in the energy losses and 65.11%
in the operating costs of the 108-node system. However,
there is no analysis of the environmental impacts associated with this research. Moreover, this work does
not allow determining the impact of the methodology
on operating aspects of the network such as line loads,
and it does not present the processing times required by
each solution. Moreover, as it evaluates the power flow
using a single-phase equivalent, it does not consider the
line imbalance of a real three-phase distribution system.
Finally, it is important to highlight that, both in scenarios
using only one type of DER and in cases involving the
simultaneous integration of two or more, the works reported
herein take the location, sizing, and operation of different
devices as decision variables. In addition, variables such as
the type of technology become especially relevant given the
specific characteristics of each system.
Table 2 presents a summary of related works that integrate
two or more types of DERs. It shows how different authors
have proposed the simultaneous integration of various devices in variable demand and generation scenarios. However,
as was made evident in the previous subsection, economic
and environmental aspects have been little explored, as well
as the use of multi-objective optimization. All of the above
highlights the need to carry out future work that simultaneously integrates DG, energy storage systems, and reactive
power compensation devices under variable demand and generation conditions, in addition to analyzing scenarios where
technical, economic, and environmental aspects are simultaneously optimized. It is also important to note that these
works should focus on three-phase test systems representing
the real operation of EDS.
It is important to mention that, as far as could be evidenced, most of the reported works elaborate optimization
models aimed at improving technical and economic aspects.
However, environmental aspects are often left unexplored. In
addition, some works lack statistical analyses, scenarios with
variable conditions, and comparisons with other techniques.
Multi-objective approaches have also been little explored in
this type of multi-variable problem and, more specifically,
in the integration of different DERs – some authors even
propose it as future work.
IV. CONCLUSIONS AND FUTURE WORK
After reviewing the state of the art, it is evident that the
search for strategies to improve the operating aspects of
EDS has sparked great interest, and that work in this field
is being done on different fronts. This is reflected in the
development of new technologies that seek to mitigate the
existing inefficiencies of traditional EDS and reduce their
dependence on conventional generation sources. Likewise,
new technologies also make it possible to meet the energy
needs of areas that cannot be connected to large-scale EPS.
Different authors have proposed strategies to optimize the
technical, economic, and environmental aspects of installing
DERs in EDS in both grid-connected and isolated areas.
However, since this is a combinatorial problem, the complexity of the mathematical model representing the operation
of the system is often directly proportional to the number of
18
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3387400
This work is licensed under a Creative Commons Attribution-Non Commercial-No Derivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

---


### Page 19

TABLE 2: Related studies in the specialized literature and their characteristics
Ref.
DER type
Objective function
Strategy
Solution
technique
Test
system
Equivalent
circuit
Variable
conditions
Comparison
with other
techniques
Statistical
analysis
[121]
DG and BC
Technical
Single-objective
GA
4, 7, 37, and
123 nodes
Three-phase
Yes
Yes
Yes
[122]
DG and BESS
Technical
Single-objective
MPE
34 nodes
Three-phase
No
Yes
No
[123]
BESS and DG
Technical,
economic, and environmental
Single-objective
VSA
27 and 33 nodes
Single-phase
Yes
Yes
Yes
[124]
DG and D-STATCOM
Technical
Single-objective
SCO
25 nodes
Three-phase
Yes
No
No
[125]
DG and BESS
Technical and economic
Single-objective
PSOS and CGSA
13 nodes
Three-phase
Yes
Yes
No
[95]
DG and BESS
Technical
Multi-objective
MOVBOA
33, 69, and
118 nodes
Single-phase
Yes
No
No
[126]
DG and D-STATCOM
Technical
Multi-objective
EABC
13 and 33 nodes
Three-phase
Yes
No
No
[127]
DG and D-STATCOM
Technical
Single-objective
ASO
25 nodes
Three-phase
Yes
No
No
[69]
DG and D-STATCOM
Technical
Single-objective
PSO and MC
N/A
Three-phase
No
No
No
[128]
DG, BESS, and
D-STATCOM
Technical
Single-objective
MOA
33 nodes
Single-phase
Yes
Yes
No
[96]
DG and BC
Technical and economic
Multi-objective
NSGA-II
33 and 108 nodes
Single-phase
Yes
Yes
No
variables to be optimized. Therefore, the simultaneous integration and management of DG, BESS, and reactive power
compensation technologies has been little explored. Some
authors resort to relaxing these problems through singlephase equivalents, and they approach the analysis from a
single-objective perspective, sometimes failing to consider
the aforementioned aspects – some works even propose future research aimed at including some of them.
It is for all the above that there is a need to design integration and management strategies for DERs which simultaneously consider DG, BESS, and reactive power compensation
devices using multi-objective optimization while identifying
their impact on the technical, economic, and environmental
aspects of three-phase EDS under conditions of variable generation and demand. All this should be done with adequate
computational loads to obtain solutions of good quality in
decent processing times.
These strategies will allow for an adequate management
of the resources and energy needs of different regions, with
particular effects on isolated areas, where they can contribute
to ensuring a stable, efficient, and high-quality electrical
supply, thus improving local communities’ quality of life
and contributing to social development through an energy
transition that responds to local development plans.
Based on the above, the main contribution of this article
is a comprehensive analysis of the fundamental challenges
related to the operation of three-phase AC distribution systems, highlighting the strategies employed by grid operators
to ensure a reliable delivery of electric power. Additionally,
a critical evaluation of various strategies based on intelligent
algorithms aimed at improving the impact of DERs implementation is carried out. This analysis and review provide
a complete insight into the technical and operational aspects
involved in the integration of such resources, which can serve
as a guide for future research and practices in the field of
electrical distribution systems.
ACKNOWLEDGMENTS
The authors appreciate the support provided by the thematic
network 723RT0150, Red para la integración a gran escala
de energías renovables en sistemas eléctricos (RIBIERSECYTED), which was funded via the 2022 call for thematic
networks of the CYTED (Ibero-American Program of Science and Technology for Development).
REFERENCES
[1] A. Azarpour, O. Mohammadzadeh, N. Rezaei, and S. Zendehboudi,
“Current status and future prospects of renewable and sustainable energy
in north america: Progress and challenges,” Energy Conversion and
Management, vol. 269, p. 115945, 2022.
[2] H. Li, Z. Ren, M. Fan, W. Li, Y. Xu, Y. Jiang, and W. Xia, “A review
of scenario analysis methods in planning and operation of modern power
systems: Methodologies, applications, and challenges,” Electric Power
Systems Research, vol. 205, p. 107722, 2022.
[3] M. O. Qays, I. Ahmad, D. Habibi, A. Aziz, and T. Mahmoud,
“System strength shortfall challenges for renewable energy-based
power
systems:
A
review,”
Renewable
and
Sustainable
Energy
Reviews, vol. 183, p. 113447, 2023. [Online]. Available: https:
//www.sciencedirect.com/science/article/pii/S1364032123003040
[4] J. A. Guzmán-Henao, B. Cortés-Caicedo, B. J. Restrepo-Cuestas,
R. I. Bolaños, and L. F. Grisales-Noreña, “Optimal integration
of photovoltaic generators into urban and rural power distribution
systems,” Solar Energy, vol. 270, p. 112400, 2024. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S0038092X2400094X
[5] S. Mirsaeidi, S. Devkota, X. Wang, D. Tzelepis, G. Abbas, A. Alshahir,
and J. He, “A review on optimization objectives for power system
operation improvement using facts devices,” Energies, vol. 16, p. 161,
2022.
[6] V. Zdraveski, J. Vuletic, J. Angelov, and M. Todorovski, “Radial distribution network planning under uncertainty by implementing robust optimization,” International Journal of Electrical Power & Energy Systems,
vol. 149, p. 109043, 2023.
[7] R. H. Siregar, Y. Away, Tarmizi, and Akhyar, “Minimizing power
losses for distributed generation (dg) placements by considering
voltage profiles on distribution lines for different loads using genetic
algorithm methods,” Energies, vol. 16, no. 14, 2023. [Online]. Available:
https://www.mdpi.com/1996-1073/16/14/5388
[8] S. A. Raza and J. Jiang, “Mathematical foundations for balancing singlephase residential microgrids connected to a three-phase distribution system,” IEEE Access, vol. 10, pp. 5292–5303, 2022.
[9] R. You and X. Lu, “Voltage unbalance compensation in distribution
feeders using soft open points,” Journal of Modern Power Systems and
Clean Energy, vol. 10, pp. 1000–1008, 2022.
[10] B. Cortés-Caicedo, L. F. Grisales-Noreña, O. D. Montoya, M. A.
Rodriguez-Cabal, and J. A. Rosero, “Energy management system for
the optimal operation of pv generators in distribution systems using the
antlion optimizer: A colombian urban and rural case study,” Sustainability (Switzerland), vol. 14, 12 2022.
[11] Y. Rivera-Durán, C. Berna-Escriche, Y. Córdova-Chávez, and J. L.
Muñoz-Cobo, “Assessment of a fully renewable generation system with
storage to cost-effectively cover the electricity demand of standalone
grids: The case of the canary archipelago by 2040,” Machines, vol. 11,
p. 101, 2023.
[12] J. Dong and C. Ye, “Green scheduling of distributed two-stage reentrant hybrid flow shop considering distributed energy resources and
VOLUME 4, 2016
19
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3387400
This work is licensed under a Creative Commons Attribution-Non Commercial-No Derivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

---


### Page 20

energy storage system,” Computers & Industrial Engineering, vol. 169,
p. 108146, 2022.
[13] A. A. Kebede, T. Kalogiannis, J. V. Mierlo, and M. Berecibar, “A
comprehensive review of stationary energy storage devices for large scale
renewable energy sources grid integration,” Renewable and Sustainable
Energy Reviews, vol. 159, p. 112213, 2022.
[14] W. Zheng, H. Lu, M. Zhang, Q. Wu, Y. Hou, and J. Zhu, “Distributed energy management of multi-entity integrated electricity and heat systems:
A review of architectures, optimization algorithms, and prospects,” IEEE
Transactions on Smart Grid, 2023.
[15] M. Jiang and Y. Zhang, “Energy management capability in the
reconfigurable distribution networks with distributed generation for
minimization of energy loss,” Applied Sciences, vol. 13, no. 14, 2023.
[Online]. Available: https://www.mdpi.com/2076-3417/13/14/8265
[16] X. Wu, C. Yang, G. Han, Z. Ye, and Y. Hu, “Energy loss reduction
for distribution networks with energy storage systems via loss sensitive
factor method,” Energies, vol. 15, no. 15, 2022. [Online]. Available:
https://www.mdpi.com/1996-1073/15/15/5453
[17] W. Mariño, J. Muñoz, M. Jaramillo, C. Barrera-Singaña, and W. Pavón,
“Distribution system reconfiguration for voltage profile improvement
using enhanced particle swarm optimization,” 2023 IEEE IAS Global
Conference on Renewable Energy and Hydrogen Technologies (GlobCon HT), pp. 1–6, 2023.
[18] M. Ali Shaik, P. L. Mareddy, and V. N., “Enhancement of voltage profile
in the distribution system by reconfiguring with dg placement using
equilibrium optimizer,” Alexandria Engineering Journal, vol. 61, no. 5,
pp. 4081–4093, 2022. [Online]. Available: https://www.sciencedirect.
com/science/article/pii/S1110016821006657
[19] P.-H. Trinh and I.-Y. Chung, “Optimal control strategy for distributed
energy resources in a dc microgrid for energy cost reduction and
voltage regulation,” Energies, vol. 14, no. 4, 2021. [Online]. Available:
https://www.mdpi.com/1996-1073/14/4/992
[20] A. F. Nematollahi, H. Shahinzadeh, H. Nafisi, B. Vahidi, Y. Amirat,
and M. Benbouzid, “Sizing and sitting of ders in active distribution
networks incorporating load prevailing uncertainties using probabilistic
approaches,” Applied Sciences, vol. 11, no. 9, 2021. [Online]. Available:
https://www.mdpi.com/2076-3417/11/9/4156
[21] W. Gil-González, “Optimal placement and sizing of d-statcoms
in electrical distribution networks using a stochastic mixed-integer
convex model,” Electronics, vol. 12, no. 7, 2023. [Online]. Available:
https://www.mdpi.com/2079-9292/12/7/1565
[22] L. P. García-Pineda and O. D. Montoya, “Optimal reactive power
compensation via d-statcoms in electrical distribution systems by
applying the generalized normal distribution optimizer,” Algorithms,
vol. 16, no. 1, 2023. [Online]. Available: https://www.mdpi.com/
1999-4893/16/1/29
[23] L. F. Grisales-Noreña, O. D. Montoya, J. C. Hernández, C. A.
Ramos-Paja, and A.-J. Perea-Moreno, “A discrete-continuous pso
for the optimal integration of d-statcoms into electrical distribution
systems by considering annual power loss and investment costs,”
Mathematics, vol. 10, no. 14, 2022. [Online]. Available: https:
//www.mdpi.com/2227-7390/10/14/2453
[24] B. Cortés-Caicedo, L. F. Grisales-Noreña, O. D. Montoya, and
R.
I.
Bolaños,
“Optimization
of
bess
placement,
technology
selection,
and
operation
in
microgrids
for
minimizing
energy
losses and co2 emissions: A hybrid approach,” Journal of Energy
Storage, vol. 73, p. 108975, 12 2023. [Online]. Available: https:
//www.sciencedirect.com/science/article/pii/S2352152X23023733https:
//linkinghub.elsevier.com/retrieve/pii/S2352152X23023733
[25] G.-J. Cho, C.-H. Kim, Y.-S. Oh, M.-S. Kim, and J.-S. Kim, “Planning for
the future: Optimization-based distribution planning strategies for integrating distributed energy resources,” IEEE Power and Energy Magazine,
vol. 16, no. 6, pp. 77–87, 2018.
[26] L. F. Grisales, B. J. R. Cuestas, and F. E. Jaramillo***, “Ubicación y
dimensionamiento de generación distribuida: una revisión,” Ciencia e
IngenierÃa Neogranadina, vol. 27, pp. 157–176, 2017.
[27] W. S. Jr and J. Grainger, Power system analysis.
Mc Graw-Hill Education, 1994.
[28] S. Vadari, Electric system operations: evolving to the modern grid.
Artech House, 2020.
[29] C. Eid, P. Codani, Y. Perez, J. Reneses, and R. Hakvoort, “Managing electric flexibility from distributed energy resources: A review of incentives
for market design,” Renewable and Sustainable Energy Reviews, vol. 64,
pp. 237–247, 2016.
[30] C. Francis, R. D. Trevizan, M. J. Reno, and V. Rao, “Enhancing topology
identification of distribution power systems using multi-rate voltage
measurements,” IEEE Transactions on Industry Applications, vol. 59, pp.
412–421, 2023.
[31] O. Eth, V. Vai, L. Bun, S. Eng, and K. Khon, “Optimal radial topology
with phase balancing in lv distribution system considering energy loss
reduction: A case study in cambodia,” 2022 4th International Conference
on Electrical, Control and Instrumentation Engineering (ICECIE), pp. 1–
6, 2022.
[32] W. Mariño, J. Muñoz, M. Jaramillo, C. Barrera-Singaña, and W. Pavón,
“Distribution system reconfiguration for voltage profile improvement
using enhanced particle swarm optimization,” 2023 IEEE IAS Global
Conference on Renewable Energy and Hydrogen Technologies (GlobCon HT), pp. 1–6, 2023.
[33] A. Silos-Sanchez, R. Villafafila-Robles, and P. Lloret-Gallego, “Novel
fault location algorithm for meshed distribution networks with ders,”
Electric Power Systems Research, 2020.
[34] S. Carneiro, D. R. R. Penido, and L. R. de Araujo, “Power
flow algorithms for three-phase unbalanced distribution systems,”
Encyclopedia of Electrical and Electronic Power Engineering, pp. 548–
561, 2023. [Online]. Available: https://www.sciencedirect.com/science/
article/pii/B9780128212042000787
[35] M. A. Toledo, C. M. Álvarez, D. X. Morales, and C. E. Arias, “Errors in
the measurement systems with the inclusion of single-phase loads at 220v
in three-phase distribution networks,” 2019 IEEE CHILEAN Conference
on Electrical, Electronics Engineering, Information and Communication
Technologies (CHILECON), pp. 1–7, 2019.
[36] V. A. Jimenez, A. L. E. Will, and D. F. Lizondo, “Phase reassignment for
load balance in low-voltage distribution networks,” International Journal
of Electrical Power & Energy Systems, vol. 137, p. 107691, 2022.
[Online]. Available: https://www.sciencedirect.com/science/article/pii/
S0142061521009200
[37] C. Zhang, P. Nie, H. Zhang, and K. Ji, “Research on three-phase imbalance control strategy of low-voltage distribution station area,” 2022
China International Conference on Electricity Distribution (CICED), pp.
941–946, 2022.
[38] M. Kisuule, I. Hernando-Gil, J. Serugunda, J. Namaganda-Kiyimba,
and M. B. Ndawula, “Stochastic planning and operational constraint
assessment of system-customer power supply risks in electricity
distribution networks,” Sustainability, vol. 13, no. 17, 2021. [Online].
Available: https://www.mdpi.com/2071-1050/13/17/9579
[39] X. Cui, G. Ruan, F. Vallée, J.-F. Toubeau, and Y. Wang, “A two-level
coordination strategy for distribution network balancing,” IEEE Transactions on Smart Grid, vol. 15, no. 1, pp. 529–544, 2024.
[40] B. Liu, K. Meng, Z. Y. Dong, P. K. C. Wong, and X. Li, “Load
balancing in low-voltage distribution network via phase reconfiguration:
An efficient sensitivity-based approach,” IEEE Transactions on Power
Delivery, vol. 36, no. 4, pp. 2174–2185, 2021.
[41] R. Seminario-Córdova and R. Rojas-Ortega, “Renewable energy sources
and energy production: A bibliometric analysis of the last five
years,” Sustainability, vol. 15, no. 13, 2023. [Online]. Available:
https://www.mdpi.com/2071-1050/15/13/10499
[42] H. Yamamoto, J. Kondoh, and D. Kodaira, “Assessing the impact of
features on probabilistic modeling of photovoltaic power generation,”
Energies, vol. 15, no. 15, 2022. [Online]. Available: https://www.mdpi.
com/1996-1073/15/15/5337
[43] I. Calero, C. A. Cañizares, K. Bhattacharya, and R. Baldick, “Duck-curve
mitigation in power grids with high penetration of pv generation,” IEEE
Transactions on Smart Grid, vol. 13, no. 1, pp. 314–329, 2022.
[44] Q. Wang, P. Chang, R. Bai, W. Liu, J. Dai, and Y. Tang, “Mitigation
strategy for duck curve in high photovoltaic penetration power system
using concentrating solar power station,” Energies, vol. 12, no. 18, 2019.
[Online]. Available: https://www.mdpi.com/1996-1073/12/18/3521
[45] A. S. Abbas, R. A. El-Sehiemy, A. Abou El-Ela, E. S. Ali,
K. Mahmoud, M. Lehtonen, and M. M. F. Darwish, “Optimal harmonic
mitigation in distribution systems with inverter based distributed
generation,” Applied Sciences, vol. 11, no. 2, 2021. [Online]. Available:
https://www.mdpi.com/2076-3417/11/2/774
[46] S. Bahramara, A. Mazza, G. Chicco, M. Shafie-khah, and J. P. S. Catalão,
“Comprehensive review on the decision-making frameworks referring to
the distribution network operation problem in the presence of distributed
energy resources and microgrids,” International Journal of Electrical
Power & Energy Systems, vol. 115, p. 105466, 2020. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S0142061518325493
20
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3387400
This work is licensed under a Creative Commons Attribution-Non Commercial-No Derivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

---


### Page 21

[47] F. Bignucolo, G. Pavoni, R. Turri, P. D. Ronco, A. Scala, and N. Sempreboni, “Characterization of residential users’ behaviour and influence
on distribution network planning,” 2020 55th International Universities
Power Engineering Conference (UPEC), pp. 1–6, 2020.
[48] I.-M. Mindreanu and A.-M. Morega, “Monitoring power flow in end-user
consumption systems,” 2023 13th International Symposium on Advanced
Topics in Electrical Engineering (ATEE), pp. 1–6, 2023.
[49] J. Liu, “Cluster analysis of electricity consumption characteristics and
electricity consumption behavior of typical industry users,” 2023 5th
Asia Energy and Electrical Engineering Symposium (AEEES), pp. 1389–
1395, 2023.
[50] P. D. B. Montani, L. da Luz, B. A. Thomé, R. G. Bento, L. E. R.
Nepomuceno, D. P. Bernardon, and L. N. Canha, “Intelligent energy
management in public institutions,” 2019 IEEE PES Innovative Smart
Grid Technologies Conference - Latin America (ISGT Latin America),
pp. 1–5, 2019.
[51] J. A. P. Lopes, N. Hatziargyriou, J. Mutale, P. Djapic, and N. Jenkins,
“Integrating distributed generation into electric power systems: A
review of drivers, challenges and opportunities,” Electric Power Systems
Research, vol. 77, pp. 1189–1203, 2007, distributed Generation.
[Online]. Available: https://www.sciencedirect.com/science/article/pii/
S0378779606001908
[52] N. Voropai, S. Podkovalnikov, and L. Chudinova, “The evolution of
interstate power grid formation,” Global Energy Interconnection, vol. 4,
pp. 335–353, 2021. [Online]. Available: https://www.sciencedirect.com/
science/article/pii/S2096511721000864
[53] M. Rosenberg, T. French, M. Reynolds, and L. While, “Finding
an optimised infrastructure for electricity distribution networks in
rural areas - a comparison of different approaches,” Swarm and
Evolutionary Computation, vol. 68, p. 101018, 2022. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S2210650221001802
[54] N. Patankar, X. Sarkela-Basset, G. Schivley, E. Leslie, and J. Jenkins,
“Land use trade-offs in decarbonization of electricity generation in the
american west,” Energy and Climate Change, vol. 4, p. 100107, 2023.
[Online]. Available: https://www.sciencedirect.com/science/article/pii/
S2666278723000144
[55] M. Nykyri, T. J. Kärkkäinen, S. Levikari, S. Annala, S. Honkapuro,
and P. Silventoinen, “The impact of intracommunal network service
pricing on the economic feasibility of an energy community,” 2023 19th
International Conference on the European Energy Market (EEM), pp. 1–
6, 2023.
[56] G. Winter-Althaus, A. Pulido-Alonso, L. Trujillo, and E. RosalesAsensio, “Review of research projects that promote eu islands’ energy
systems transition,” EU Islands and the Clean Energy Transition, pp. 1–
7, 2023.
[57] L. You, V. Vai, D. Eam, S. Heang, P. Hem, S. Eng, and C. Chhlonh,
“Optimal topology of lvac in a rural village using water cycle algorithm,”
2022 IEEE International Conference on Power Systems Technology
(POWERCON), pp. 1–5, 2022.
[58] O. Saad and C. Abdeljebbar, “Historical literature review of optimal
placement of electrical devices in power systems: Critical analysis of
renewable distributed generation efforts,” IEEE Systems Journal, vol. 15,
pp. 3820–3831, 2021.
[59] M. C. Das, S. C. Swain, C. K. Nayak, and R. Dash, “Energy management
for a res-powered dc microgrid under variable load,” 2023 International
Conference on Power Electronics and Energy (ICPEE), pp. 1–6, 2023.
[60] L. Gumilar, D. Monika, S. N. Rumokov, and D. E. Cahyani, “Implementation of fcl in hybrid ac/dc distribution network system,” 2022
5th International Seminar on Research of Information Technology and
Intelligent Systems (ISRITI), pp. 1–5, 2022.
[61] M. Q. Duong, T. D. Pham, T. T. Nguyen, A. T. Doan, and H. V. Tran,
“Determination of optimal location and sizing of solar photovoltaic
distribution generation units in radial distribution systems,” Energies,
vol. 12, 2019. [Online]. Available: https://www.mdpi.com/1996-1073/
12/1/174
[62] Z. Azani, H. Shahinzadeh, S. Azani, G. B. Gharehpetian, E. Kabalci,
and M. Benbouzid, “An aggregated revenue-driven vpp model based on
marginal price tracking for profit maximization,” 2022 9th Iranian Joint
Congress on Fuzzy and Intelligent Systems (CFIS), pp. 1–7, 2022.
[63] S. S. M. Isa, M. N. Ibrahim, A. Mohamad, N. Y. Dahlan, and S. Nordin,
“A review of optimization approaches for optimal sizing and placement
of battery energy storage system (bess),” 2023 IEEE 3rd International
Conference in Power Engineering Applications (ICPEA), pp. 258–262,
2023.
[64] L. Strezoski, H. Padullaparti, F. Ding, and M. Baggu, “Integration of
utility distributed energy resource management system and aggregators
for evolving distribution system operators,” Journal of Modern Power
Systems and Clean Energy, vol. 10, no. 2, pp. 277–285, 2022.
[65] S. Ullah, F. Ahmad, M. Hussain, and A. Khan, “Development of a cnnbased time-varying reactive power forecast model for power systems,”
2022 International Conference on Recent Advances in Electrical Engineering & Computer Sciences (RAEE & CS), pp. 1–7, 2022.
[66] W. Rohouma, M. Metry, R. S. Balog, A. A. Peerzada, M. M. Begovic,
and D. Zhou, “Analysis of the capacitor-less d-statcom for voltage profile
improvement in distribution network with high pv penetration,” IEEE
Open Journal of Power Electronics, vol. 3, pp. 255–270, 2022.
[67] M. T. Gayatri, A. M. Parimi, and A. V. P. Kumar, “A review of reactive
power compensation techniques in microgrids,” Renewable and Sustainable Energy Reviews, vol. 81, pp. 1030–1036, 2018.
[68] L. F. Azeredo, I. Yahyaoui, R. Fiorotti, J. F. Fardin, H. Garcia-Pereira,
and H. R. Rocha, “Study of reducing losses, short-circuit currents and
harmonics by allocation of distributed generation, capacitor banks and
fault current limiters in distribution grids,” Applied Energy, vol. 350,
2023.
[69] F. Fardinfar and M. J. K. Pour, “Optimal placement of d-statcom and
pv solar in distribution system using probabilistic load models,” 2023
10th Iranian Conference on Renewable Energy & Distributed Generation
(ICREDG), pp. 1–5, 2023.
[70] A. Komijani, M. Sedighizadeh, and M. Kheradmandi, “Improving fault
ride-through in meshed microgrids with wind and pv by virtual synchronous generator with sfcl and smes,” Journal of Energy Storage,
vol. 50, p. 103952, 2022.
[71] C. R. Sarimuthu, V. K. Ramachandaramurthy, K. R. Agileswari, and
H. Mokhlis, “A review on voltage control methods using on-load tap
changer transformers for networks with renewable energy sources,” Renewable and Sustainable Energy Reviews, vol. 62, pp. 1154–1161, 2016.
[72] P. Kgori, D. E. Okojie, and U. B. Akuru, “Design and analysis of a
proposed multistage capacitor bank compensation scheme,” 2022 IEEE
PES/IAS Power Africa, pp. 1–5, 2022.
[73] M. Ayala-Chauvin, B. S. Kavrakov, J. Buele, and J. Varela-Aldás,
“Static reactive power compensator design, based on three-phase
voltage converter,” Energies, vol. 14, no. 8, 2021. [Online]. Available:
https://www.mdpi.com/1996-1073/14/8/2198
[74] G. S. Chawda and A. G. Shaik, “A reactive power-based adaptive
approach for synchronization of dfig into the weak grid to support
existing we infrastructure,” International Journal of Electrical Power
& Energy Systems, vol. 157, p. 109850, 2024. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S0142061524000711
[75] G. Li, F. Ma, Y. Wang, M. Weng, Z. Chen, and X. Li, “Design and
operation analysis of virtual synchronous compensator,” IEEE Journal
of Emerging and Selected Topics in Power Electronics, vol. 8, no. 4, pp.
3835–3845, 2020.
[76] H. Zhai, F. Zhuo, C. Zhu, H. Yi, Z. Wang, R. Tao, and T. Wei, “An
optimal compensation method of shunt active power filters for systemwide voltage quality improvement,” IEEE Transactions on Industrial
Electronics, vol. 67, no. 2, pp. 1270–1281, 2020.
[77] Prashant, A. S. Siddiqui, M. Sarwar, A. Althobaiti, and S. S. M.
Ghoneim, “Optimal location and sizing of distributed generators in
power system network with power quality enhancement using fuzzy
logic controlled d-statcom,” Sustainability, vol. 14, no. 6, 2022. [Online].
Available: https://www.mdpi.com/2071-1050/14/6/3305
[78] O. D. Montoya, O. D. Florez-Cediel, and W. Gil-González, “Efficient
day-ahead scheduling of pv-statcoms in medium-voltage distribution
networks using a second-order cone relaxation,” Computers, vol. 12,
no. 7, 2023. [Online]. Available: https://www.mdpi.com/2073-431X/12/
7/142
[79] A. S. P. Babu and S. P R, “Power oscillation damping by utilizing pvstatcom,” 2022 IEEE Delhi Section Conference (DELCON), pp. 1–6,
2022.
[80] A. M. Shaheen, R. A. El-Sehiemy, A. Ginidi, A. M. Elsayed, and S. F.
Al-Gahtani, “Optimal allocation of pv-statcom devices in distribution
systems for energy losses minimization and voltage profile improvement
via hunter-prey-based algorithm,” Energies, vol. 16, no. 6, 2023.
[Online]. Available: https://www.mdpi.com/1996-1073/16/6/2790
[81] F. H. Gandoman, A. Ahmadi, A. M. Sharaf, P. Siano, J. Pou, B. Hredzak,
and V. G. Agelidis, “Review of facts technologies and applications
for power quality in smart grids with renewable energy systems,”
Renewable and Sustainable Energy Reviews, vol. 82, pp. 502–514, 2018.
VOLUME 4, 2016
21
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3387400
This work is licensed under a Creative Commons Attribution-Non Commercial-No Derivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

---


### Page 22

[Online]. Available: https://www.sciencedirect.com/science/article/pii/
S1364032117313151
[82] R. S. R. Akshay and R. J. Abraham, “Bilateral load following with a statcom and battery energy storage,” 2020 IEEE International Conference on
Power Electronics, Smart Grid and Renewable Energy (PESGRE2020),
pp. 1–6, 2020.
[83] A. C. Duman, H. S. Erden, Ömer Gönül, and Önder Güler, “Optimal
sizing of pv-bess units for home energy management system-equipped
households considering day-ahead load scheduling for demand response
and self-consumption,” Energy and Buildings, vol. 267, p. 112164, 2022.
[Online]. Available: https://www.sciencedirect.com/science/article/pii/
S0378778822003358
[84] L.
A.
G.
Pareja,
J.
M.
López-Lezama,
and
O.
G.
Carmona,
“A mixed-integer linear programming model for the simultaneous
optimal distribution network reconfiguration and optimal placement of
distributed generation,” Energies, vol. 15, 2022. [Online]. Available:
https://www.mdpi.com/1996-1073/15/9/3063
[85] P. Nikolaidis and A. Poullikkas, “Evolutionary priority-based dynamic
programming for the adaptive integration of intermittent distributed
energy resources in low-inertia power systems,” Eng, vol. 2, pp. 643–660,
2021. [Online]. Available: https://www.mdpi.com/2673-4117/2/4/41
[86] D. Mendoza Osorio, J. Rosero Garcia et al., “Optimization of distributed
energy resources in distribution networks: applications of convex optimal
power flow formulations in distribution networks,” International Transactions on Electrical Energy Systems, vol. 2023, 2023.
[87] O. D. Montoya, W. Gil-González, and A. Garces, “Optimal power flow
on dc microgrids: A quadratic convex approximation,” IEEE Transactions
on Circuits and Systems II: Express Briefs, vol. 66, no. 6, pp. 1018–1022,
2019.
[88] L. F. Grisales-Noreña, B. J. Restrepo-Cuestas, B. Cortés-Caicedo,
J. Montano, A. A. Rosales-Muñoz, and M. Rivera, “Optimal location
and sizing of distributed generators and energy storage systems in
microgrids: A review,” Energies, vol. 16, 2023. [Online]. Available:
https://www.mdpi.com/1996-1073/16/1/106
[89] P. Aaslid, F. Geth, M. Korpås, M. M. Belsnes, and O. B. Fosso,
“Non-linear charge-based battery storage optimization model with
bi-variate cubic spline constraints,” Journal of Energy Storage, vol. 32,
p. 101979, 2020. [Online]. Available: https://www.sciencedirect.com/
science/article/pii/S2352152X20318144
[90] O. D. Montoya, W. Gil-González, and J. C. Hernández, “Efficient
integration of fixed-step capacitor banks and d-statcoms in radial
and meshed distribution networks considering daily operation curves,”
Energies, vol. 16, 2023. [Online]. Available: https://www.mdpi.com/
1996-1073/16/8/3532
[91] S.-E. Razavi, E. Rahimi, M. S. Javadi, A. E. Nezhad, M. Lotfi,
M. Shafie-khah, and J. P. S. Catalão, “Impact of distributed generation
on protection and voltage regulation of distribution systems: A review,”
Renewable and Sustainable Energy Reviews, vol. 105, pp. 157–
167, 2019. [Online]. Available: https://www.sciencedirect.com/science/
article/pii/S1364032119300668
[92] F. Ren, Z. Wei, and X. Zhai, “A review on the integration and
optimization of distributed energy systems,” Renewable and Sustainable
Energy Reviews, vol. 162, p. 112440, 2022. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S136403212200346X
[93] N. Gupta, K. S. Joshal, and A. Tomar, “Chapter 9 - environmental and
technoeconomic aspects of distributed generation,” Advances in Smart
Grid Power System, pp. 237–263, 2021. [Online]. Available: https:
//www.sciencedirect.com/science/article/pii/B9780128243374000096
[94] E. H. Nezhad, R. Ebrahimi, and M. Ghanbari, “Fuzzy multi-objective
allocation of photovoltaic energy resources in unbalanced network using
improved manta ray foraging optimization algorithm,” Expert Systems
with Applications, vol. 234, p. 121048, 2023. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S0957417423015506
[95] T. V. Kumar and S. K. Injeti, “Probabilistic optimal planning of
dispatchable distributed generator units in distribution systems using
a multi-objective velocity-based butterfly optimization algorithm,” Renewable Energy Focus, vol. 43, pp. 191–209, 2022. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S1755008422000813
[96] S. Sharma, K. R. Niazi, K. Verma, and T. Rawat, “Coordination
of different dgs, bess and demand response for multi-objective
optimization of distribution network with special reference to indian
power sector,” International Journal of Electrical Power & Energy
Systems, vol. 121, p. 106074, 2020. [Online]. Available: https:
//www.sciencedirect.com/science/article/pii/S0142061519327322
[97] S. K. Wankhede, P. Paliwal, and M. K. Kirar, “Bi-level multi-objective
planning model of solar pv-battery storage-based ders in smart grid
distribution system,” IEEE Access, vol. 10, pp. 14 897–14 913, 2022.
[98] J. Guerrero, D. Gebbran, S. Mhanna, A. C. Chapman, and G. Verbiˇc,
“Towards a transactive energy system for integration of distributed
energy resources: Home energy management, distributed optimal power
flow, and peer-to-peer energy trading,” Renewable and Sustainable
Energy Reviews, vol. 132, p. 110000, 2020. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S1364032120302914
[99] O. D. Montoya and W. Gil-González, “On the numerical analysis based
on successive approximations for power flow problems in ac distribution
systems,” Electric Power Systems Research, vol. 187, p. 106454, 2020.
[100] F. BARRERO GONZALEZ, Sistemas de energía eléctrica.
Ediciones
Paraninfo, SA, 2004.
[101] Z. Liu, R. Liu, X. Zhang, M. Su, Y. Sun, H. Han, and P. Wang,
“Further results on newton-raphson method in feasible power-flow for
dc distribution networks,” IEEE Transactions on Power Delivery, vol. 37,
pp. 1348–1351, 2022.
[102] L. A. Alnabi, A. K. Dhaher, and M. B. Essa, “Optimal allocation of distributed generation with reconfiguration by genetic algorithm using both
newton raphson and gauss seidel methods for power losses minimizing.”
International Journal of Intelligent Engineering & Systems, vol. 15, 2022.
[103] O.
D.
Montoya,
W.
Gil-González,
and
A.
Garces,
“Numerical
methods for power flow analysis in dc networks: State of the art,
methods and challenges,” International Journal of Electrical Power
& Energy Systems, vol. 123, p. 106299, 2020. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S014206151933577X
[104] O. D. Montoya and W. Gil-González, “On the numerical analysis
based on successive approximations for power flow problems in ac
distribution systems,” Electric Power Systems Research, vol. 187,
p. 106454, 2020. [Online]. Available: https://www.sciencedirect.com/
science/article/pii/S0378779620302583
[105] L. Grisales-Noreña, J. Morales-Duran, S. Velez-Garcia, O. D. Montoya,
and W. Gil-González, “Power flow methods used in ac distribution
networks: An analysis of convergence and processing times in radial
and meshed grid configurations,” Results in Engineering, vol. 17,
p. 100915, 2023. [Online]. Available: https://www.sciencedirect.com/
science/article/pii/S2590123023000427
[106] S. Mishra and Y. S. Brar, “Load flow analysis using matlab,” 2022
IEEE International Students’ Conference on Electrical, Electronics and
Computer Science (SCEECS), pp. 1–4, 2022.
[107] E. A. Almabsout, N. Elnaily, M. Majidi, and A. A. Nazeri, “Optimum
allocation and sizing of multi-distributed generations: Step-by-step injection,” 2022 International Conference on Engineering & MIS (ICEMIS),
pp. 1–6, 2022.
[108] N. Kharlamova and S. Hashemi, “Evaluating machine-learning-based
methods for modeling a digital twin of battery systems providing frequency regulation,” IEEE Systems Journal, vol. 17, pp. 2698–2708, 2023.
[109] J. Salazar, D. Carrión, and M. Jaramillo, “Reactive compensation
planning in unbalanced electrical power systems,” Energies, vol. 15,
2022.
[Online].
Available:
https://www.mdpi.com/1996-1073/15/21/
8048
[110] A. Ehsan and Q. Yang, “Optimal integration and planning of renewable
distributed generation in the power distribution networks: A review
of analytical techniques,” Applied Energy, vol. 210, pp. 44–59, 2018.
[Online]. Available: https://www.sciencedirect.com/science/article/pii/
S0306261917315519
[111] Y. Sun, C. Yang, H. Cui, M. Wu, J. Shao, B. Zhao, and K. He, “Optimization methods for optimal power flow problems in distribution networks:
A brief review,” 2023 8th Asia Conference on Power and Electrical
Engineering (ACPEE), pp. 1400–1406, 2023.
[112] P. S. Georgilakis and N. D. Hatziargyriou, “A review of power
distribution planning in the modern power systems era: Models, methods
and future research,” Electric Power Systems Research, vol. 121,
pp. 89–100, 2015. [Online]. Available: https://www.sciencedirect.com/
science/article/pii/S0378779614004490
[113] K. E. Adetunji, I. W. Hofsajer, A. M. Abu-Mahfouz, and L. Cheng, “A
review of metaheuristic techniques for optimal integration of electrical
units in distribution networks,” IEEE Access, vol. 9, pp. 5046–5068,
2021.
[114] M. Purlu and B. E. Turkay, “Optimal allocation of renewable distributed
generations using heuristic methods to minimize annual energy losses
and voltage deviation index,” IEEE Access, vol. 10, pp. 21 455–21 474,
2022.
22
VOLUME 4, 2016
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3387400
This work is licensed under a Creative Commons Attribution-Non Commercial-No Derivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

---


### Page 23

[115] T. Gu, P. Wang, F. Liang, G. Xie, L. Guo, X.-P. Zhang, and F. Shi,
“Placement and capacity selection of battery energy storage system
in the distributed generation integrated distribution network based on
improved nsga-ii optimization,” Journal of Energy Storage, vol. 52,
p. 104716, 2022. [Online]. Available: https://www.sciencedirect.com/
science/article/pii/S2352152X22007290
[116] A. M. Nassef, E. H. Houssein, H. Rezk, and A. Fathy, “Optimal
allocation of biomass distributed generators using modified hunger
games search to reduce co2 emissions,” Journal of Marine Science and
Engineering, vol. 11, 2023. [Online]. Available: https://www.mdpi.com/
2077-1312/11/2/308
[117] M. Cikan and N. N. Cikan, “Optimum allocation of multiple type
and number of dg units based on ieee 123-bus unbalanced multi-phase
power distribution system,” International Journal of Electrical Power and
Energy Systems, vol. 144, p. 108564, 2023.
[118] M. C. Barla and D. Sarkar, “Optimal placement and sizing of bess
in res integrated distribution systems,” International Journal of System
Assurance Engineering and Management, vol. 14, pp. 1866–1876, 2023.
[Online]. Available: https://doi.org/10.1007/s13198-023-02016-w
[119] E. S. Ali, R. A. El-Sehiemy, A. A. A. El-Ela, S. Kamel, and B. Khan,
“Optimal planning of uncertain renewable energy sources in unbalanced
distribution systems by a multi-objective hybrid pso–sco algorithm,”
IET Renewable Power Generation, vol. 16, pp. 2111–2124, 2022.
[Online]. Available: https://ietresearch.onlinelibrary.wiley.com/doi/abs/
10.1049/rpg2.12499
[120] G. S. Chawda and A. G. Shaik, “Power quality improvement in rural
grid using adaptive control algorithm to enhance wind energy penetration
levels,” IEEE Transactions on Smart Grid, vol. 14, no. 3, pp. 2075–2084,
2023.
[121] A. S. C. Martins, L. R. de Araujo, and D. R. R. Penido, “Sensibility
analysis with genetic algorithm to allocate distributed generation and
capacitor banks in unbalanced distribution systems,” Electric Power
Systems Research, vol. 209, p. 107962, 2022. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S0378779622001924
[122] R. Leng, Z. Li, and Y. Xu, “Two-stage stochastic programming for coordinated operation of distributed energy resources in unbalanced active
distribution networks with diverse correlated uncertainties,” Journal of
Modern Power Systems and Clean Energy, vol. 11, pp. 120–131, 2023.
[123] L. F. Grisales-Noreña, B. Cortés-Caicedo, O. D. Montoya, J. C.
Hernandéz, and G. Alcalá, “A battery energy management system
to improve the financial, technical, and environmental indicators of
colombian urban and rural networks,” Journal of Energy Storage, vol. 65,
p. 107199, 2023. [Online]. Available: https://www.sciencedirect.com/
science/article/pii/S2352152X23005960
[124] R. Ray and A. R. Gupta, “Analysis of radial unbalanced distribution network for different loading conditions with dg and d-statcom placement,”
2022 IEEE Delhi Section Conference (DELCON), pp. 1–8, 2022.
[125] J. Radosavljevi´c, A. Ktena, M. Gaji´c, M. Milovanovi´c, and J. Živi´c,
“Dynamic optimal power dispatch in unbalanced distribution networks
with single-phase solar pv units and bess,” Energies, vol. 16, 2023.
[Online]. Available: https://www.mdpi.com/1996-1073/16/11/4356
[126] M.
Kandasamy,
R.
Thangavel,
T.
Arumugam,
S.
Kumaravel,
S. Aruchamy, W. W. Kim, and Z. W. Geem, “Strategic incorporation of
dstatcom and distributed generations in balanced and unbalanced radial
power distribution networks considering time varying loads,” Energy
Reports, vol. 9, pp. 4345–4359, 2023.
[127] G. Tahiliani and A. R. Gupta, “Electrical distribution system analysis
with atom search optimization based dg and dstatcom allocation,” 2022
IEEE Delhi Section Conference (DELCON), pp. 1–6, 2022.
[128] M. S. Giridhar, K. R. Rani, P. S. Rani, and V. Janamala, “Mayfly
algorithm for optimal integration of hybrid photovoltaic/battery energy
storage/d-statcom system for islanding operation.” International Journal
of Intelligent Engineering & Systems, vol. 15, 2022.
JHONY ANDRÉS GUZMÁN HENAO was born
in Medellín, Colombia in 1987. He obtained his
bachelor’s degree in Electromechanical Engineering in 2022 and his master’s degree in Industrial
Energy Management in 2023, both from Instituto
Tecnológico Metropolitano de Medellín (ITM). he
is currently pursuing a Ph D in Engineering at the
same institute. The author’s research interests include mathematical optimization, the planning and
control of electrical systems, renewable energies,
energy storage, protection devices, and smart grids.
RUBÉN IVÁN BOLAÑOS was born in Garzón,
Huila, Colombia in 1988. The author obtained his
BSc, MSc, and Ph D. degrees in Electrical Engineering from Universidad Tecnológica de Pereira
(UTP, Colombia) in 2013, 2014 and 2021, respectively. He is currently a professor at ITM, Colombia. His research interests include mathematical
optimization with regard to the planning of electrical distribution systems as well as the optimal
location, sizing, and management of renewable
energies. He also specializes in optimization applied to freight and passenger
transport systems.
LUIS FERNANDO GRISALES NOREÑA was
born in Cartago, Valle, Colombia. He received his
BSc and MSc degrees in Electrical Engineering
from UTP in 2013 and 2015, respectively. He
obtained his Ph D in Automation Engineering from
Universidad Nacional de Colombia (UNAL, Manizales campus) in 2020. He currently serves as a
professor in the Electrical Engineering Program at
Universidad de Talca, Chile. His research interests
include mathematical optimization, the planning
and control of energy systems, renewable energies, energy storage, power
electronics, and smart grids.
OSCAR DANILO MONTOYA (Senior Member,
IEEE) was born in Obando, Valle, Colombia, in
1989. He received his BSc, MSc, and Ph D degrees
in Electrical Engineering from UTP in 2012, 2014,
and 2019, respectively. He is currently an assistant
professor in the Electrical Engineering program
of Universidad Distrital Francisco José de Caldas,
Bogotá, Colombia. His research interests include
mathematical optimization, the planning and control of power systems, renewable energies, energy
storage, protective devices, passivity-based control, inverse optimal control,
and dynamical analysis.
Harold R. Camorro (Senior Member, IEEE) is currently with the KTH Royal
Institute of Technology, Stockholm, Sweden.
VOLUME 4, 2016
23
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3387400
This work is licensed under a Creative Commons Attribution-Non Commercial-No Derivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4

---
