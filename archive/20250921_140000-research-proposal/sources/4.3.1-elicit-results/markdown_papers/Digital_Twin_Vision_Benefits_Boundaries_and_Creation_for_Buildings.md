

---

Page 1

---

Received September 19, 2019, accepted October 7, 2019, date of publication October 9, 2019, date of current version October 23, 2019.
Digital Object Identifier 10.1109/ACCESS.2019.2946515
Digital Twin: Vision, Benefits, Boundaries, and
Creation for Buildings
SIAVASH H. KHAJAVI
1, NASER HOSSEIN MOTLAGH
2, ALIREZA JARIBION
1,
LISS C. WERNER
3, AND JAN HOLMSTRÖM
1
1Department of Industrial Engineering and Management, Aalto University, 02150 Espoo, Finland
2Department of Computer Science, University of Helsinki, 00014 Helsinki, Finland
3Institute of Architecture, Technical University Berlin, 10623 Berlin, Germany
Corresponding author: Siavash H. Khajavi (siavash.khajavi@aalto.ﬁ)
This work was supported in part by the EIT Digital and Academy of Finland Projects Built by Data under Project 680570-T30805, in part
by the Get Home Safely under Project 680377-T30805, and in part by the Direct Operations under Grant 323831.
ABSTRACT The concept of a digital twin has been used in some industries where an accurate digital model
of the equipment can be used for predictive maintenance. The use of a digital twin for performance is critical,
and for capital-intensive equipment such as jet engines it proved to be successful in terms of cost savings
and reliability improvements. In this paper, we aim to study the expansion of the digital twin in including
building life cycle management and explore the beneﬁts and shortcomings of such implementation. In four
rounds of experimentation, more than 25,000 sensor reading instances were collected, analyzed, and utilized
to create and test a limited digital twin of an ofﬁce building facade element. This is performed to point out
the method of implementation, highlight the beneﬁts gained from digital twin, and to uncover some of the
technical shortcomings of the current Internet of Things systems for this purpose.
INDEX TERMS Building information modeling, digital twin, life cycle management, Internet of Things,
wireless sensor network.
I. INTRODUCTION
The emergence of the Internet of Things (IoT) which is partly
the result of Moore’s law that allowed powerful semiconduc-
tor chips to be produced at very low prices [1] can impact
every aspect of our economy [2], [3]. Developments such
as cars that are connected and autonomous [4] to ﬂying
robots [5] and smart houses [6] are all examples of either IoT
being integrated into legacy systems or IoT enabling the cre-
ation of entirely new concepts. Smart buildings are emerging
as the next frontier in the development cycle of architectural
structures [7]. Embedding programmable services into the
residential buildings is currently underway, including ser-
vices such as heating and cooling as well as the integration
of household appliances. This collaboration is taking place
between the largest household appliance manufacturers and
internet companies such as Amazon, Google, and Microsoft.
A concept that is explored extensively in the litera-
ture and has been implemented in real-world construction
projects around the world is building information modeling
(BIM) [8]–[10].
The associate editor coordinating the review of this manuscript and
approving it for publication was Antonino Orsino
.
BIM is a platform for keeping an accurate and interop-
erable record of building information to enhance planning,
construction, and maintenance over the life cycle of a facil-
ity [10], [11]. In particular, BIM has been developed for
embedding the building’s 3D computer aided design (CAD)
model with additional data related to building speciﬁcation,
time schedule, cost estimation, and maintenance management
(i.e., 4D, 5D, and 6D) [12]–[14] to reduce cost by preventing
mistakes in the design and construction phase [15]. Currently,
BIM is used in architecture, construction, engineering and
facility management (AEC/FM) functions for design visu-
alization and consistency, clash detection, lean construction,
cost and time estimation, and enhanced stakeholders’ inter-
operability [10]. Efforts [16, p. 19] to ensure BIM beneﬁts
from real-time data inputs (e.g. from sensors and IoT devices)
are underway [17]; these efforts, in turn would beneﬁt the
buildings that already have implemented BIM or are willing
to undertake the effort and cost of creating BIM documenta-
tion. More than 80% of buildings in Europe are constructed
prior to 1990, and therefore do not have BIM [10], [18]–[21].
For existing buildings without BIM documentation, there
exist major obstacles to produce it (i.e., high effort require-
ment for creating and updating the BIM model and difﬁculties
147406
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see http://creativecommons.org/licenses/by/4.0/
VOLUME 7, 2019


---

Page 2

---

S. H. Khajavi et al.: Digital Twin: Vision, Benefits, Boundaries, and Creation for Buildings
FIGURE 1. Essential components to create a digital twin of building and difference with BIM.
related to the solving the issues of uncertain data and rela-
tionships in the BIM [10]). Existing buildings can therefore
beneﬁt from the implementation of a digital twin, which is
a known concept in the ﬁeld of manufacturing [22], for the
enhancement of building operation and maintenance and for
the implementation of a closed-loop design [23].
Wireless sensor network (WSN) integration and data ana-
lytics are two of the components required for the creation of
a digital twin [24]. Digital twin visualization for a building
can rely on 3D CAD model extracted from BIM or a custom
3D model of the building. The digital twin of a building can
utilize various sensor networks to create a real-time view of
the asset (see Fig. 1). This dynamic view allows for real-time
analytics, informed decision-making, building efﬁciency, and
comfort enhancement.
The ﬁrst major difference between a building’s BIM and
digital twin is that the former was designed to improve the
efﬁciency of design and construction and is still used in
these phases of the building life cycle [25], whereas the
latter is designed to monitor a physical asset and improve
its operational efﬁciency and to enable predictive mainte-
nance [26]. The second major difference is that BIM was
not designed to work with real-time data and is still used in
the industry for design, construction, and maintenance tasks
and interoperability, which do not necessarily require real-
time capability [27]; meanwhile, digital twin is the digital
counterpart of a physical asset and works contrary to the
current BIM platform. Digital twin works speciﬁcally with
real-time data fed by the sensor systems to record and ana-
lyze the real-time structural and environmental parameters
of a physical asset for the purpose of performing highly
accurate digital twin simulation and data analytics [26]. The
third difference between the two concepts is related to the
type of data required for the construction of each model.
While BIM is suitable for the integration of cost estima-
tion and time schedule data to enhance the efﬁciency of
a construction project [8], [28], digital twin is designed to
integrate real-time sensor readings to analyze and improve
the building’s interaction with the environment and with
users [29].
In this paper, we aim to explore issues related to the cre-
ation of a building’s digital twin and propose a method for its
implementation for a building facade. Moreover, the paper
discusses some of the applications of the digital twin of a
building facade.
This paper is organized in the following manner. After
the research introduction, the study presents the literature
review, which explores the research conducted on digital
twin, building information modeling, comparison of BIM and
digital twin of building, and smart buildings. In the third
section, the research methodology and the case study setup
are explained in detail. Following this, the results are pre-
sented in the sections that concern technical obstacles, valida-
tion of data, sensor conﬁguration, and digital twin creation.
The next section is the discussion of beneﬁts of the digital
twin of buildings, and the study ends with the conclusions.
II. LITERATURE REVIEW
A. DIGITAL TWIN
At present, one of the standard methods for enhancing system
design, testing, and maintenance is through modeling and
simulation. Modeling and simulation play a decisive role
in supporting design tasks and validating system properties.
However, the ﬁrst simulation-based solutions are known for
optimized operations and failure prediction [34]. The digital
twin emerged from the integration of sensor networks and
the digitalization of machinery and production systems in the
manufacturing industry [35]. The main difference between
simulation in the design phase and a digital twin is that the
latter requires a physical asset and a sensor network, while
the former does not [24]. Accordingly, the study in [35] pre-
sented an expanded deﬁnition: ‘‘digital twins will facilitate
the means to monitor, understand, and optimize the functions
of all physical entities, living as well as nonliving, by enabling
the seamless transmission of data between the physical and
virtual world.’’
VOLUME 7, 2019
147407


---

Page 3

---

S. H. Khajavi et al.: Digital Twin: Vision, Benefits, Boundaries, and Creation for Buildings
TABLE 1. A detailed comparison of BIM and digital twin of building.
The research in [36] described the simulation aspect of
digital twins as the collection of relevant digital artifacts
that involves engineering and operation data, in addition to
behavior description using various simulation models. Digital
twins utilize these speciﬁc simulation models based on their
capability for solving problems, deriving relevant solutions
for real-life systems, and describing behavior. In general,
the study in [36] deﬁned the vision of the digital twin as
‘‘a comprehensive physical and functional description of a
component, product or system together with all available
operational data.’’
The digital twin is a concept that can be exerted to many
ﬁelds and technologies [37], and therefore it seems the
concept could disrupt industries beyond manufacturing.
In addition, the digital twin was one of the top ten strategic
technology trends of 2018, and based on research future pre-
dictions, the digital twin market will reach 15 billion dollars
by 2023 [35], [38]. The research in [39] deﬁned the digital
twin of a building as the ‘‘interaction between the real-world
building’s indoor environment and a digital yet realistic vir-
tual representation model of building environment, which
provides the opportunity on real-time monitoring and data
acquisition.’’ In their delineation, an indoor environment indi-
cates information on the air temperature, airﬂow, relative
humidity, and lighting condition, while a digital virtual one
indicates computational ﬂuid dynamics and luminance level.
Moreover, based on study presented in [39], some of the
considerable beneﬁts of creating digital twin of a building
are as follows: 1) gathering, generating and visualizing the
environment of the building, 2) analyzing data irregularities,
and 3) optimizing building services.
B. BUILDING INFORMATION MODELING
According to the US National Building Information Model
Standard Project Committee [30], BIM is ‘‘a digital represen-
tation of physical and functional characteristics of a facility.
A BIM is a shared knowledge resource for information about
a facility, forming a reliable basis for decisions during its life
cycle; deﬁned as existing from earliest conception to demoli-
tion.’’ Meanwhile, [31] deﬁnes BIM as ‘‘an overarching term
to describe a variety of activities in object-oriented Com-
puter Aided Design (CAD), which supports the representa-
tion of building elements in terms of their 3D geometric and
non-geometric (functional) attributes and relationships.’’
BIM is different from 3D CAD modeling [30], [31], [40].
The main emphasis of BIM is on embedded information
(e.g., speciﬁcation, material type, installation method, time,
cost) in the design model and on the interoperability of this
comprehensive information-rich model for enhanced collab-
oration in the AEC/FM community.
In an ideal case scenario, BIM can also be used to simulate
operations management on a construction site during con-
struction and can thus support and optimize the development
of the construction schedule [41].
BIM has been changing over the history of its exis-
tence. According to the BIM maturity model presented
in [16, p. 15-16], Level 0 BIM in the 1990s took advantage
of early CAD modeling software, hence, information was
scattered, and data sharing was mostly on paper drawings.
During the 2000s, Level 1 BIM became popular; companies
started to use 3D CAD modeling, and common data envi-
ronment (CDE) was used for digital data sharing. However,
Level 1 BIM did not allow project team members to share
the models with one another. Level 2 BIM gained traction
during the 2010s when collaboration and sharing of digital
ﬁles and models entered the next evolution level through the
use of common ﬁle formats and the introduction of Industry
Foundation Class (IFC) and Construction Operations Build-
ing Information Exchange (COBie). Most companies are cur-
rently at Level 1 or Level 2 however; nonetheless, Level 3
BIM is being developed with an emphasis on stakeholders’
collaboration (i.e., through the use of same design model).
The design model of Level 3 BIM is stored in a centralized
cloud-based repository to ensure collaboration throughout the
building life cycle.
BIM is still mostly used for resource efﬁciency enhance-
ment during facility design and construction [10], [42] and
knowledge exchange [11]. The purpose is to facilitate the
tasks of building architects, engineers, and facility managers
and avoid costly design mistakes [11]–[14].
C. COMPARISON OF BIM AND DIGITAL TWIN OF
BUILDING
BIM and digital twin of building can be compared in detail
based on the following aspects; application focus, users, sup-
porting technology, software, stages of life cycle, and origin
(see Table 1). BIM is mainly used to prevent errors during
the design of a building, facilitate communication between
147408
VOLUME 7, 2019


---

Page 4

---

S. H. Khajavi et al.: Digital Twin: Vision, Benefits, Boundaries, and Creation for Buildings
stakeholders, improve construction efﬁciency, and monitor
the construction project’s time and cost [10]. Meanwhile,
the digital twin of a building can be used for predictive main-
tenance [26], resource efﬁciency improvement, enhancement
of tenants’ comfort, what-if analysis for optimization of the
building design, and enabling closed-loop design [23] to
transfer learnings from a building to the future ones. The users
of BIM are architects, engineers, and constructors who utilize
it during the design and construction phase [9], [16]. BIM is
also used by facility managers [30] for maintenance planning
throughout the building life cycle. Notably, BIM can be used
during the demolition [31] as it contains relevant information.
Digital twin is utilized by facility managers in the use phase
of the building life cycle to enhance its operation. Digital
twin also provides architects valuable inputs for the design of
future buildings based on the detected ﬂaws and improvement
areas unveiled during the use phase of a building.
Technologies that support BIM at its current form are
detailed 3D CAD modeling, CDE to create a single source
of information for the collaboration of project teams, and
standard data formats for sharing and exchanging BIM data
between different software applications such as IFC and
COBie [16]. Supporting technologies for digital twin are 3D
CAD modeling, WSNs, machine learning algorithms [32],
and data analytics. The major software applications used for
BIM are Autodesk Revit, ArchiCAD by Graphisoft, Micro-
Station by Bentley Systems, and the open source BIMserver
by TNO [16]. Meanwhile, some of the software applications
used to create a digital twin are Predix from General Elec-
tric, Dasher 360 from Autodesk, and Ecodomus. Notably,
the origin of the two concepts are also different. BIM was
conceptualized by Charles Eastman in the mid-1970s [16]
and was implemented for the ﬁrst time in the RUCAPS CAD
system for the London Heathrow Airport Terminal 3 design
and construction [43], [44]. Digital twin conceptualization
originates from the Apollo program at NASA [22], where a
physical twin of the crew module was kept on the ground to
simulate conditions and resolve possible issues that the space-
craft may face in space. However, the actual implementation
of digital twin occurred only recently when General Electric
developed the Predix software platform for the collection
and analysis of the data from sensors installed in GE90 jet
engines for blades degradation monitoring and predictive
maintenance [45]–[47].
Regarding ﬂexibility, although some buildings are still
constructed using pre-BIM traditional practices, they can
beneﬁt from digital twin by being retroﬁtted with sensors and
by taking advantage of cloud-based analytics tools.
D. INTERNET OF THINGS AND SMART BUILDINGS
The IoT is signiﬁcantly expanding, and it is predicted to
reach a staggering 20 billion internet-connected things by
2020 [48]. The study in [49] deﬁned IoT as ‘‘an open
and comprehensive network of intelligent objects that have
the capacity to auto-organize, share information, data, and
resources, reacting and acting in the face of situations and
changes in the environment.’’ In discussing modern advance-
ment in innovative internet technologies and WSN, IoT has
emerged as a ubiquitous global computing network where
the collected data from more affordable and available sensors
and actuators can be utilized for data analysis-based control
of the resources or physical environments [48], [50], [51].
With the enhancement of computing and communication
capabilities for the physical objects (i.e., the things in IoT),
these objects can provide high-quality services for the users
through their wired or wireless communications [9]. The
concept of a smart city can be pragmatic in light of this
breakthrough. One of the main service domains in a smart
city is a smart building [50]. According to the research in [52],
three primary characteristics that identify a smart building are
its components, functions, and outcomes. Components con-
sist of multiple interconnected pieces of technical building
equipment and appliances, sensing and control infrastructure,
and emerging technologies. All of these components behave
according to their functions, which deﬁne the intelligence and
effectiveness of the building and which eventually result in
certain outcomes, such as health, comfort, productivity, and
energy efﬁciency [53]; all these would beneﬁt the environ-
ment, society, and the economy.
E. GAP IN THE LITERATURE
Although the concept of IoT has been studied extensively
in the context of future connected equipment and the possi-
bilities that come from it [54]–[57], the use of IoT-enabled
sensor networks to build a digital twin of a smart building
was not extensively studied. The study in [39] presented a
brief overview of a conceptual framework for a transition
from a physical room to a digital twin, but the study fell short
in providing an in-depth technical analysis of the framework
for the transition, and they also did not present any empirical
experimentation to support their concept. The study in [58]
provided a background on the concept of the digital twin of a
building and brieﬂy pinpointed the potential applications, but
it did not provide any real-world proof or data. In another arti-
cle, [59] presented a case of digital twin utilization by Kone
company to improve the elevator service in buildings while
reducing maintenance cost. Fraunhofer Building Innovation
Alliance is studying the digital twin of buildings, and in a pub-
lished short note, it highlighted the digital twin of a building’s
potential beneﬁts throughout the building life cycle [60]. The
study in [61] utilized the concept of digital twin of a building
to calculate the rate of return on investment in upgrading
existing buildings to net-zero energy buildings (NZEB). Their
research was based on a BIM model that was simulated in
Revit software for energy saving calculations. However, they
stopped short of implementing the digital twin of a build-
ing and collecting real-time empirical data. In this research,
we contribute to ﬁlling the knowledge gap by investigating
the creation of a sensor network for the digital twin of a
building and by studying the current technical shortcomings
of establishing a digital twin. The application and the beneﬁts
VOLUME 7, 2019
147409


---

Page 5

---

S. H. Khajavi et al.: Digital Twin: Vision, Benefits, Boundaries, and Creation for Buildings
FIGURE 2. Data flow diagram of the designed sensor network.
of the digital twin of a building are also discussed in this
paper.
III. METHODOLOGY
The methodology used in this research is experimentation
using a testbed. To collect data, we created a WSN that was
installed on the building facade of an ofﬁce building at the
Aalto University in Finland. The aim was to collect light,
ambient temperature, and relative humidity measurements
data of the environment.
A. EXPERIMENT TESTBED SETUP
Texas Instruments (TI) Sensortag CC2650 was selected due
to its characteristics, such as the availability of various sen-
sors on each tag, Bluetooth Low Energy (BLE) commu-
nication technology, coin-cell power source, and low cost.
Another important aspect that led to this selection was the
existence of a large community of developers around this
sensor hardware platform. In addition, we used a Raspberry
Pi 3B+ as the sensor network gateway. We utilized Raspbian
as the operating system on the network gateway, and we
used an open source collector code by the IBM company in
Python programming language for communication and for
recording the data that were generated by TI Sensortags. This
code was modiﬁed to lengthen the period between sensor
data recordings up to 240 seconds, and further developments
allowed for ofﬂine and cloud-based recording of the sensors’
data. For the ofﬂine part, which was used for the development
of this paper, the data recordings were stored in .csv ﬁles
on the gateway’s local memory. Fig. 2 shows the data ﬂow
diagram for our sensor network.
B. DATA COLLECTION STEPS
The process of data collection followed a four-step process,
as illustrated in Fig. 3. Step 1 is initial testing, debugging,
and WSN setup veriﬁcation. Step 2 pertains to expanding
the WSN. Step 3 relates to sensors’ reading validation, while
Step 4 describes the creation and visualization of a limited
facade digital twin. All of these steps are explained individu-
ally in the following subsections.
1) INITIAL TESTING, DEBUGGING, AND WSN SETUP
VERIFICATION
During the initial testing, we evaluated the performance of
WSN inside the building using three Sensortags. We then
FIGURE 3. Four phases of data collection.
initiated several data collection tests over a period of one
month while the sensors were installed on the inside and
outside of the building facade. During this time, we examined
the impact of distance and data recording time interval on
the battery life of the Sensortags. Moreover, the continuous
connectivity between the gateway and the Sensortags was
investigated. We encountered a number of serious issues with
the stability of the communication between the Sensortags
and the gateway. After analyzing the data collected from the
initial tests, we formulated solutions for the communication
issues encountered during the tests to expand the sensor
network.
2) EXPANDING THE WSN
We expanded the sensor network from three sensors to seven.
Fig. 4 shows the arrangement of the seven sensors. A data
set was collected for a period of 10 days, during which the
sensors were on the building facade, both inside (i.e., on the
windows) and outside. Three sensors were installed inside
the room, speciﬁcally on the windows facing outward, and
four sensors were installed on the facade, facing outward
of the same wall as the inside sensors. This data set was
utilized to determine the optimal mesh of the WSN on the
building facade. Throughout the data collection campaign,
in order to prevent confusion regarding the assignment of
sensor readings to the sensor that it belongs to, a constant one-
to-one matching is used where the name of the sensor data
ﬁle on the gateway corresponds to a similar physical designa-
tion, which is based on each sensor’s constant MAC address
(see Table 2).
147410
VOLUME 7, 2019


---

Page 6

---

S. H. Khajavi et al.: Digital Twin: Vision, Benefits, Boundaries, and Creation for Buildings
FIGURE 4. Sensor configurations at the office building.
TABLE 2. Sample of the table used for the sensors’ physical and virtual
designations in relation to MAC addresses.
3) SENSORS’ READING VALIDATION
A different data set was collected to examine the validity of
the sensors’ readings and to determine each sensor’s error
range for each environmental parameter of light, ambient
temperature, and relative humidity. This data set was col-
lected while sensors were placed adjacent to one another on
the surface of an ofﬁce desk where light, ambient tempera-
ture, and relative humidity were the same for all the sensors.
The data collection interval was set to 90 seconds for all
sensors. Section V uses this data set to calculate the sensors’
error range. We used Minitab and Microsoft Excel software
to analyze the sensors’ data sets and produce the time series
graphs.
4) DATA COLLECTION FOR THE FACADE DIGITAL TWIN
In the last round of data collection, six sensors were installed
on the facade of a building at the Aalto University campus,
and a data set of environmental lighting, ambient temperature,
and relative humidity was collected. This data set was used
for the creation and visualization of the digital twin of the
building facade.
C. RAW SENSOR DATA PROCESSING
The data collected from the sensors contained noise due to
multiple factors. These factors caused the sensors to discon-
nect or to not be able to send the correct data to the gateway.
One of the reasons was the low battery level, which caused the
energy-intensive sensors to send wrong readings (noise) to
FIGURE 5. Time series plot for temperature, and humidity measurements
before noise cleansing.
the gateway. The ambient temperature and relative humidity
sensors on TI Sensortags are energy-intensive and they can
stop sending accurate readings when the battery levels are
low even before the TI Sensortag itself runs out of power and
turns off. The other source of noise was produced when the
sensors were disconnected from the gateway for any reason.
One of the main disconnectivity causes was the obstacles
between the sensor and the gateway. For instance, the dual
layer glass of the building windows signiﬁcantly attenuated
the Bluetooth signal strength and disrupted the connectivity.
Fig. 5(a) and Fig. 5(b) illustrate the noise in one of the sensor
data recordings before data cleansing. In order to remove the
noise from temperature (e.g., −40.0 readings) and relative
humidity (e.g.: 0.0 and 99.0 readings), we initially reviewed
the data and then cleansed it. It should be noted that light
readings of the sensors did not have noise and could thus be
utilized without cleansing.
IV. TECHNICAL OBSTACLES
In this section, we present the important technical shortcom-
ings and challenges that we faced while creating our limited
building’s facade digital twin. We also present the solutions
VOLUME 7, 2019
147411


---

Page 7

---

S. H. Khajavi et al.: Digital Twin: Vision, Benefits, Boundaries, and Creation for Buildings
that were utilized to address them. In the developed testbed,
the gateway used Bluetooth to communicate with the TI Sen-
sortags. Therefore, the Bluetooth channel was continuously
receiving the data sent from the Sensortags. Our experiments
showed that when the gateway was continuously connected
to the cloud through Wi-Fi, it caused disruptions to the
Bluetooth channel and resulted in a disconnection between
the sensors and the gateway. To resolve this technical issue,
we disabled the Bluetooth link of the gateway, and we used a
USB Bluetooth dongle to enable the Bluetooth communica-
tions. In this fashion, we resolved the disconnectivity issue
of the gateway while keeping it connected to the internet
through Wi-Fi.
In another experiment, we measured the light values for
indoor and outdoor environments. Our tests showed that
locating the sensor behind the window glass attenuates the
Bluetooth signal strength considerably while putting a strain
on the sensor’s battery. This often caused the disconnectivity
between the sensor and the gateway. The solution to this issue
was found to be the placement of the gateway on the same side
of the window that the sensors are located.
The other concern that needed to be addressed was the
number of sensors. We considered a scenario where there
was a need for more than 10 Sensortags to be used for
data collection. Thus, to decrease the trafﬁc caused by the
Sensortags data transmission, we tried using two parallel
gateways. The result of this test showed that using parallel
gateways without software modiﬁcations would cause com-
munication disruptions. A software solution can resolve this
hardware issue by dedicating speciﬁc sensors to a speciﬁc
gateway and disabling blind pairing with Bluetooth devices
on the gateway. A solution to sensor disconnectivity for cases
where the number of sensors is higher than seven can involve
lengthening the data upload intervals for the sensors; we
suggest setting this interval to be over three minutes, as our
experimentation showed that this would provide a highly
reliable connection between the sensors and the gateway.
In the following round of hands-on testing, which was per-
formed to ﬁnd a better economically justiﬁed sensor option,
a test was conducted utilizing a different Sensortag that
was built by another manufacturer with our gateway. Blue-
tooth 4.0 BLE Sensor Tag/iBeacon Station NRF51822 was
the tested Sensortag. The results showed that although
NRF51822 Sensortag has an ambient light sensor as well as
temperature and relative humidity sensors, these might not be
suitable for this project because of two reasons. Firstly, there
was a lack of support availability by the supplier company
and user community while, user-friendly software resources
for the NRF51822 Sensortags were also scarce. These are
important negative points in comparison to the TI Sensortags.
The second reason was related to the power management on
NRF51822 Sensortags, which does not allow for smart power
management. In such a setting, a sensor would run out of
battery signiﬁcantly earlier than the TI Sensortags, which
offer smart power management. Therefore, the application
of NRF51822 Sensortags would be very costly from the
management perspective, although their initial purchasing
price is one-third that of TI Sensortags.
We conducted tests where the battery level readings of the
Sensortags were activated in the code. In this way, the oper-
ator can gain visibility into the inner workings of the sen-
sor from an energy consumption perspective and implement
a better battery replacement policy. Furthermore, to fully
understand the impact of sensor data transfer frequency on
their battery life, we tested different time intervals to ﬁnd
an optimal data transfer latency between every two mea-
surements. We performed data collection with intervals of
20, 30, 60, 90, 120, and 240 seconds using three Sensortags.
This test was performed to understand the optimal setting
for the data collection while considering the Sensortags’
battery consumption and the number and types of parameters
measured. Our conclusion is that setting a short time inter-
val decreases the battery life of the Sensortags and causes
connectivity issues between the Sensortags and the gateway.
Thus, using a short time interval is not an optimal method
for data measurement. Moreover, the short time interval also
increases the amount of collected data, which would be sim-
ilar in the measured values since little change occurs in a
short time, and consequently the complexity of data analysis
is increased. However, using a longer time interval is also
not an accurate solution for certain environmental factors
with rapid ﬂuctuations such as light; while factors such as
temperature and relative humidity that change gradually can
beneﬁt from longer data recording intervals. Our conclusion
is that when setting the time interval, three major points
should be considered: 1) the number of deployed Sensortags,
2) the number of measured environmental factors, and 3) the
type of measured environmental factors. Considering these
points, in our setting we set the recording time interval to
90 seconds.
In this research, we used BLE technology for the com-
munication between sensors and gateway due to its afford-
ability, availability, and low energy consumption [62] that
allow battery-powered sensors. In contrast to Zigbee, BLE
communication technology is widely and out of the box
available in consumer electronic devices [63] such as laptops,
smartphones, and in our case, Raspberry Pi 3B+. BLE con-
sumes less energy than Zigbee [62]. The data rate for BLE
(i.e., 1 Mbit/s for short bursts) is four times greater than Zig-
bee (i.e., 250 Kbit/s) [64], [65]. Moreover, in performing the
experiments for this research, we did not require data trans-
mission over long distances; thus, BLE was a suitable choice.
Nonetheless, based on the comparison presented in Table 3
for a real-world digital twin creation project for a building,
Zigbee is more suitable.
Zigbee by design offers meshing capability [66] and thus,
requires a lower number of gateways compared to the BLE
technology. Zigbee-enabled sensors relay the information
through the mesh network. In other words, the data travels
from a single sensor device across a group of routers (i.e.,
Zigbee nodes) until the transmission reaches the IoT gateway.
In the case of data transmission failure at any router, data
147412
VOLUME 7, 2019


---

Page 8

---

S. H. Khajavi et al.: Digital Twin: Vision, Benefits, Boundaries, and Creation for Buildings
TABLE 3. Comparison of Zigbee and BLE.
FIGURE 6. Time series plot for light measurements of sensors 4 (black),
5 (green), and 7 (red).
is automatically transferred to another router; thus, Zigbee
offers a highly reliable network with almost zero information
loss [67]. The mesh networking feature of the technology
signiﬁcantly extends the communication range [68]. The
maximum range of Zigbee is up to 100 meters [64], [66], [69]
in node-to-node communication. These features of Zigbee,
hence, makes it a suitable candidate [70] for a WSN for the
digital twin of a building.
On the contrary, BLE works in a star network topology [66]
with limited connected nodes, where the gateway is at the
center. In other words, each BLE-enabled sensor requires
to be directly connected to a gateway. BLE communication
is vulnerable to interruptions and data loss under certain
conditions [72]. Thus, BLE communication is not preferable
for real-world implementation of large WSNs that cover large
areas.
V. VALIDATION OF DATA
Using the data set collected to evaluate the validity of sen-
sors’ readings, we realized that measurable differences exist
between the readings of various sensors, and these differences
can lead to inaccurate interpretation of experimental data.
A time series plot for the light measurements by three Sen-
sortags in a similar lighting condition is presented in Fig. 6,
which shows the differences in the readings of the sensors and
the increased deviation while the lighting is increased.
The same pattern was identiﬁed for all the sensor record-
ings related to the ambient temperature and the relative
humidity. Therefore, before analyzing the data collected from
TABLE 4. Error range for different sensortags.
the sensors in order to create the digital twin, we needed to
eliminate the error range of the sensors. After calculating
the percentage of error for each sensor, an error correc-
tion coefﬁcient was introduced for each sensor. This assists
in removing false variations from sensor readings. Table 4
presents the error range for seven Sensortags. This table is
used for determining the error percentage of various sensors
compared to sensor 5 (S5), which has been selected as the
reference Sensortag. Among all Sensortags used in our exper-
imentation, S5 was selected as the golden sample since the
readings of this sensor (i.e., light, ambient temperature, and
relative humidity) were closest to the readings of recently cal-
ibrated industrial sensors at the Aalto University’s Metrology
Research Institute.
VI. DETERMINING THE SENSOR CONFIGURATION
It is important to optimize the number of sensors required for
a building from a cost perspective as well as the usability of
the system. To be more speciﬁc, the cost factors related to the
implementation of a sensor network on the building facade for
the purpose of creating a digital twin are as follows: 1) sensor
network design; 2) the procurement of sensors, gateways,
and other related hardware and software; 3) installation costs
related to sensors and back-end systems; 4) the monitoring
and data collection as well as the analysis and fusion of results
into the smart building systems; and 5) system maintenance
related to the sensors’ battery replacement (in case of battery-
powered systems), sensor replacement in case of damage and
loss, connectivity maintenance for both wired and wireless
connections, as well as gateway and software maintenance
and updates.
After we selected and cleansed the data set and deter-
mined the error range, we started the analysis of the data
that was collected from the sensors on the building facade
to determine a suitable conﬁguration for the Sensortags.
Figs. 7(a), 7(b), and 7(c) illustrate the light, temperature,
and humidity recordings by four Sensortags. These four
Sensortags are part of the seven Sensortags conﬁguration
illustrated in Fig. 4. Three of the sensors are installed on a
straight horizontal line, one meter apart. The fourth sensor is
installed at 0.6 meters above the middle sensor.
For the sensor conﬁguration optimization, the following
Algorithm 1 is applied. Given that the sensor mesh includes
m rows and n columns, sij refers to spatial grid for sensor
in the row i and column j and αij is the measurement of
sensor sij. This algorithm performs in two steps: The hor-
VOLUME 7, 2019
147413


---

Page 9

---

S. H. Khajavi et al.: Digital Twin: Vision, Benefits, Boundaries, and Creation for Buildings
FIGURE 7. Time series plots for light, temperature, and humidity
measurements by sensors 3 (black), 4 (red), 5 (green), and 7 (blue) that
were installed on the building facade over an eight-day time span.
izontal optimization of sensors’ conﬁguration, followed by
the vertical optimization of sensors’ conﬁguration. In the
horizontal optimization, the difference between two imme-
diately adjacent sensors’ measurements is compared with
the difference of the error range of the same sensors, while
taking into account the intended accuracy. Intended accuracy
(IA) in this algorithm refers to the decision maker or facility
manager’s required sensor network accuracy. As long as the
difference between the measurements of adjacent sensors is
Algorithm 1 Sensor Mesh Optimization
Initialization:
1: sij: Sensor in row i and column j
2: αij: Measurement of sensor sij
3: S : Matrix of αij for all i and j
4: Set m : The number of sensors’ rows
5: Set n : The number of sensors’ column
6: Set eij : Error range of sensor sij
7: Set IA : Intended accuracy set by decision maker
8: Set A = B = C = ∅
Horizontal optimization
9: for i = 1 to m do
10:
Set j = 1, j′ = 2
11:
while (j′ < m + 1) do
12:
if (αij −αij′ ⩽|eij −eij′| + IA) then
13:
A ←−A ∪sij′
14:
j′ ←−j′ + 1
15:
else
16:
j ←−j′
17:
j′ ←−j′ + 1
18:
end if
19:
end while
20: end for
Vertical optimization
21: for j = 1 to n do
22:
Set i = 1, i′ = 2
23:
while (i′ < n + 1) do
24:
if (αij −αi′j ⩽|eij −ei′j| + IA) then
25:
B ←−B ∪si′j
26:
i′ ←−i′ + 1
27:
else
28:
i ←−i′
29:
i′ ←−i′ + 1
30:
end if
31:
end while
32: end for
Set of all redundant sensors
33: C ←−A ∩B
34: Return C
lower than the difference of their error range plus the IA,
the algorithm replaces the adjacent sensor measurements with
the next immediate horizontally adjacent sensor measure-
ments and performs the same calculation until the difference
between the measurements of two sensors compared exceeds
the difference of the error range of the same sensors plus
the IA. Subsequently, the algorithm stores all the redundant
sensors in set A. By completing the ﬁrst full row, the algo-
rithm continues the horizontal optimization by performing
the same steps for the immediate next row. The same steps
are consequently performed for the vertical optimization of
sensor conﬁguration, and the algorithm stores all the yielding
redundant sensors in set B. Finally, the overall optimized
sensor mesh is determined by removing the sensors in set C,
which is the intersection of A and B.
147414
VOLUME 7, 2019


---

Page 10

---

S. H. Khajavi et al.: Digital Twin: Vision, Benefits, Boundaries, and Creation for Buildings
FIGURE 8. Suggested sensors’ mesh on a simple building facade that was
used in Section VII for the creation of a limited digital twin of the building
facade.
The data collected by all seven sensors contained infor-
mation on lighting (lx), temperature (C◦), and relative
humidity (%), and the sensors were installed in a conﬁgu-
ration that covered 3.4 meters horizontally and 0.6 meters
vertically. The preliminary analysis of this data illustrated
that the deviation among the recording of the sensors is
largely due to the sensors’ deﬁned error range. Therefore,
we conclude that a digital twin of the building facade can
be created with an acceptable accuracy using a conﬁguration
where the sensors covering the building facade are installed
in a mesh with a horizontal distance of greater than 3.4 meters
from one another and a vertical distance of greater than 0.6
meters.
Fig. 8 presents the proposed sensor mesh for creating
digital twin of a building in this research. This sensor conﬁg-
uration is used for minimizing the cost of the sensor network,
while maintaining the IA of the WSN readings at a high
level. In this sensor mesh, the horizontal distance between
the sensors is 4 meters, and the vertical distance between the
sensors is 1.5 meters. The proposed sensor mesh in Fig. 8 is
utilized in a limited experiment with six Sensortags to create
the digital twin of the building facade. Section VII explains
the method used and the results of our digital twin creation
and visualization experiment.
In this research, the digital twin of building facade was
created based on a WSN with a mesh topology. The rea-
son behind the selection of mesh topology over star and
tree topologies is that the mesh topology is a common
and preferable conﬁguration for real-world smart building
WSNs [73]; thus, mesh is used to retain the applicability
of the research results for real-world building’s digital twin
creation while using other communication technologies such
as Zigbee or LoRa.
VII. DIGITAL TWIN CREATION AND VISUALIZATION
The location of sensors on the building facade for the creation
of the digital twin is shown in Fig. 9. The sensors are located
at the center of each rectangular area, and in this conﬁguration
each sensor covers 6 m2 of the building facade. The collected
data by the light sensors of Sensortags were processed before
being utilized by software to visualize the real-time state of
facade brightness; this visualization was done by assigning a
speciﬁc color to the lux values in a color spectrum. The color
spectrum was deﬁned by selecting the yellow color range
and by assigning a light shade of yellow to the bright lights
with a light intensity of 2400 lux and higher, while a dark
shade of yellow was assigned to an 800-lux light intensity
and lower. The light intensities between 800 and 2400 lux are
automatically assigned different shades of yellow between
the two selected colors according to their light intensity val-
ues. In this research, we selected this high color contrast for
a relatively small light intensity range in order to facilitate
the illustration; however, in real-world implementation the
range can be wider. This method of creating a building facade
digital twin through the real-time visualization of sensor
readings can be performed using other sensor types (e.g.,
ambient temperature, relative humidity or sensors measuring
other environmental attributes); this can be done by only
assigning a suitable data variation range and the selection of
a distinct color spectrum. For instance, a temperature digital
twin of the building facade can be created by assigning a color
spectrum, starting with dark blue and ending with dark red to
a temperature range of −30◦C to +40◦C.
Fig. 9 illustrates the creation, visualization, and testing of
the building facade digital twin that was implemented in this
research. The presence of an obstacle such as a person or a
car can be detected visually by the digital twin in real-time.
In Fig. 9(e), the person’s distance to the wall is 0.5 meters,
while the vehicle and the tree are 6.2 meters and 5.3 meters
away from it, respectively. In this illustration, the reading
of the light sensor that is adjacent to the person shows a
signiﬁcant value drop compared to the other sensors’ readings
(i.e., 875 lux compared to above 2000 lux). As Fig. 9(f)
illustrates, this sudden change of lighting is visualized by the
building facade digital twin.
VIII. DISCUSSION OF BENEFITS OF THE DIGITAL TWIN
OF BUILDINGS
Several beneﬁts can be found in using the digital twin of
a building, and one of them is the building energy efﬁ-
ciency [61] with regard to the heating and light distribution
when and where required. A digital twin can provide data
regarding the building’s maintenance needs. Moreover, a dig-
ital twin can be used by the architects to improve the perfor-
mance of future buildings. We discuss these applications in
detail in this section.
An air conditioning system can source its air from a cooler
part of a building outdoors rather than expend energy to
cool and recirculate the same air. This requires real-time
monitoring of air pollution and air temperature and relative
humidity of the whole building facade. The digital twin of
a building with sensors measuring air quality, temperature,
and relative humidity can provide the required data for
such a hybrid air conditioning system for the indoor
spaces [74], [75].
VOLUME 7, 2019
147415


---

Page 11

---

S. H. Khajavi et al.: Digital Twin: Vision, Benefits, Boundaries, and Creation for Buildings
FIGURE 9. Facade digital twin created based on real-time sensor data of lighting.
In addition, an indoor measurement of the ambient light
that is received from the outdoors allows for a ﬁne adjustment
of the lighting level inside the building [53]. As a result,
the amount of energy consumed by the lighting system dur-
ing the daytime can be drastically decreased. For instance,
if operators are aware of the level of light reduction from the
window glass, it would be possible for them to utilize smart
curtains for controlling the level of light on a real-time basis
inside building spaces. Accordingly, the temperature varia-
tions sourced from the sunlight received inside the building
can be purposefully utilized for heating and cooling by the air
conditioning systems.
Moreover, designing a sensor network for the building
facade and obtaining a digital twin enables the building
designers and architects to improve the efﬁciency of the
building during modiﬁcations, renovation, [76] and also
when designing the future buildings. For example, the archi-
tects utilizing the information on the directions of sunlight
and wind obtained at the building facade can design a building
that uses these natural resources to improve the lighting and
airﬂow inside the building. In this way, they can potentially
design a system that enables energy savings in lighting, venti-
lation, and cooling while offering visual and thermal comfort
for the building tenants.
Another potential application of buildings’ digital twin is
in the creation of accurate city digital twin. By integrating the
components of buildings’ digital twin that are not proprietary,
a more comprehensive and holistic model can be created
which enables city planners to access an unprecedented level
of accuracy for city planning, project implementations and
operations [77].
IX. CONCLUSION
In this research, we presented a method for establishing a sen-
sor network to create a building real-time digital model, also
known as a digital twin. The paper accomplished this through
the collection and analysis of the speciﬁc environmental
factors in the exact surroundings of the building. Although
the extent of this study did not go further than utilizing a
limited sensor network and three environmental parameters
for sensing (i.e., light, temperature and relative humidity),
the step-by-step framework introduced in this research can
be utilized to create a more comprehensive digital twin of
a building facade as well as a building interior. This can
be done using different types of sensors and communication
protocols. Some of the technical obstacles in creating the
digital twin of a building were also explained in detail, and
the implementable solutions were proposed. This research
concluded by suggesting a framework to determine the sensor
arrangement on a building facade to enable a digital twin and
by discussing the beneﬁts of the digital twin of a building.
Among the applications of a digital twin, we focused on
147416
VOLUME 7, 2019


---

Page 12

---

S. H. Khajavi et al.: Digital Twin: Vision, Benefits, Boundaries, and Creation for Buildings
lowering maintenance cost, increasing tenants’ comfort, and
lowering the overall management and operational cost of a
building.
This research was conducted on a building facade, this
means the future research can examine the implementation of
the digital twin for a building interior. Moreover, another area
of exploration for future studies can be the expansion of sen-
sor network presented in this research to include more sensors
with a higher variety to allow for additional applications for
the digital twin of a building. For instance, the integration of
other sensing devices (e.g., visual or stereoscopic sensors on
a building facade) can have applications in real-time security
and in people movement monitoring while enhancing the
accuracy and resilience of the data feed. In addition to this,
a study of system affordability versus its beneﬁts is also
worthwhile.
ACKNOWLEDGMENT
The authors would like to thank the anonymous reviewers for
their insightful comments that strengthened this manuscript.
REFERENCES
[1] M. Chui, M. Löfﬂer, and R. Roberts, The Internet of Things, vol. 2.
New York, NY, USA: McKinsey, 2010, pp. 1–9.
[2] T. Baranwal and P. K. Pateriya, ‘‘Development of IoT based smart security
and monitoring devices for agriculture,’’ in Proc. IEEE 6th Int. Conf. Cloud
Syst. Big Data Eng. (Conﬂuence), Jan. 2016, pp. 597–602.
[3] S. Leminen, M. Westerlund, M. Rajahonka, and R. Siuruainen, ‘‘Towards
IoT ecosystems and business models,’’ in Internet of Things, Smart
Spaces, and Next Generation Networking. Berlin, Germany: Springer,
2012, pp. 15–26.
[4] M. Gerla, E.-K. Lee, G. Pau, and U. Lee, ‘‘Internet of vehicles: From
intelligent grid to autonomous cars and vehicular clouds,’’ in Proc. IEEE
World Forum Internet Things (WF-IoT), Mar. 2014, pp. 241–246.
[5] N. H. Motlagh, T. Taleb, and O. Arouk, ‘‘Low-altitude unmanned aerial
vehicles-based Internet of Things services: Comprehensive survey and
future perspectives,’’ IEEE Internet Things J., vol. 3, no. 6, pp. 899–922,
Dec. 2016.
[6] M. Wang, G. Zhang, C. Zhang, J. Zhang, and C. Li, ‘‘An IoT-based
appliance control system for smart homes,’’ in Proc. IEEE 4th Int. Conf.
Intell. Control Inf. Process. (ICICIP), 2013, pp. 744–747.
[7] D. Minoli, K. Sohraby, and B. Occhiogrosso, ‘‘IoT considerations, require-
ments, and architectures for smart buildings—Energy optimization and
next-generation building management systems,’’ IEEE Internet Things J.,
vol. 4, no. 1, pp. 269–283, Feb. 2017.
[8] S. Azhar, ‘‘Building information modeling (BIM): Trends, beneﬁts, risks,
and challenges for the AEC industry,’’ Leadership Manage. Eng., vol. 11,
no. 3, pp. 241–252, 2011.
[9] C. Eastman, P. Teicholz, R. Sacks, and K. Liston, BIM Handbook: A Guide
to Building Information Modeling for Owners, Managers, Designers, Engi-
neers and Contractors. Hoboken, NJ, USA: Wiley, 2011.
[10] R. Volk, J. Stengel, and F. Schultmann, ‘‘Building Information Modeling
(BIM) for existing buildings—Literature review and future needs,’’ Autom.
Construct., vol. 38, pp. 109–127, Mar. 2014.
[11] P. Tang, D. Huber, B. Akinci, R. Lipman, and A. Lytle, ‘‘Automatic
reconstruction of as-built building information models from laser-scanned
point clouds: A review of related techniques,’’ Autom. Construct., vol. 19,
no. 7, pp. 829–843, 2010.
[12] B. Succar, ‘‘Building information modelling framework: A research and
delivery foundation for industry stakeholders,’’ Autom. Construct., vol. 18,
no. 3, pp. 357–375, 2009.
[13] D. Bryde, M. Broquetas, and J. M. Volm, ‘‘The project beneﬁts of building
information modelling (BIM),’’ Int. J. Project Manage., vol. 31, no. 7,
pp. 971–980, 2013.
[14] K. Wong and Q. Fan, ‘‘Building information modelling (BIM) for sustain-
able building design,’’ Facilities, vol. 31, nos. 3–4, pp. 138–157, 2013.
[15] H. W. Lee, H. Oh, Y. Kim, and K. Choi, ‘‘Quantitative analysis of warnings
in building information modeling (BIM),’’ Autom. Construct., vol. 51,
pp. 23–31, Mar. 2015.
[16] R. Sacks, C. Eastman, G. Lee, and P. Teicholz, BIM Handbook: A Guide
to Building Information Modeling for Owners, Designers, Engineers, Con-
tractors, and Facility Managers. Hoboken, NJ, USA: Wiley, 2018.
[17] S. Tang, D. R. Shelden, C. M. Eastman, P. Pishdad-Bozorgi, and X. Gao,
‘‘A review of building information modeling (BIM) and the Internet
of Things (IoT) devices integration: Present status and future trends,’’
Automat. Construct., vol. 101, pp. 127–139, May 2019.
[18] Y. Arayici, ‘‘Towards building information modelling for existing struc-
tures,’’ Struct. Surv., vol. 26, no. 3, pp. 210–222, 2008.
[19] J. Armesto, I. Lubowiecka, C. Ordóñez, and F. I. Rial, ‘‘FEM modeling
of structures based on close range digital photogrammetry,’’ Autom. Con-
struct., vol. 18, no. 5, pp. 559–569, 2009.
[20] J. Dickinson, A. Pardasani, S. Ahamed, and S. Kruithof, ‘‘A survey of
automation technology for realising as-built models of services,’’ in Proc.
1st Int. Conf. Improving Construct. Use Through Integr. Design Solutions,
2009, pp. 365–381.
[21] R. Attar, V. Prabhu, M. Glueck, and A. Khan, ‘‘210 King Street: A dataset
for integrated performance assessment,’’ in Proc. Spring Simulation Mul-
ticonf., 2010, Art. no. 177.
[22] B. Schleich, N. Anwer, L. Mathieu, and S. Wartzack, ‘‘Shaping the digital
twin for design and production engineering,’’ CIRP Ann., vol. 66, no. 1,
pp. 141–144, 2017.
[23] Q. Qi, F. Tao, Y. Zuo, and D. Zhao, ‘‘Digital twin service towards smart
manufacturing,’’ in Proc. CIRP, vol. 72, 2018, pp. 237–242.
[24] F. Tao, J. Cheng, Q. Qi, M. Zhang, H. Zhang, and F. Sui, ‘‘Dig-
ital twin-driven product design, manufacturing and service with big
data,’’ Int. J. Adv. Manuf. Technol., vol. 94, nos. 9–12, pp. 3563–3576,
Feb. 2018.
[25] Y. Liu, S. van Nederveen, and M. Hertogh, ‘‘Understanding effects of BIM
on collaborative design and construction: An empirical study in China,’’
Int. J. Project Manage., vol. 35, no. 4, pp. 686–698, 2017.
[26] Q. Qi and F. Tao, ‘‘Digital twin and big data towards smart manufac-
turing and industry 4.0: 360 degree comparison,’’ IEEE Access, vol. 6,
pp. 3585–3593, 2018.
[27] S. Bruno, M. De Fino, and F. Fatiguso, ‘‘Historic building informa-
tion modelling: Performance assessment for diagnosis-aided information
modelling and management,’’ Autom. Construct., vol. 86, pp. 256–276,
Feb. 2018.
[28] S.-K. Lee, K.-R. Kim, and J.-H. Yu, ‘‘BIM and ontology-based approach
for building cost estimation,’’ Autom. Construct., vol. 41, pp. 96–105,
May 2014.
[29] F. Tao, F. Sui, A. Liu, Q. Qi, M. Zhang, B. Song, Z. Guo, S. C.-Y. Lu,
and A. Nee, ‘‘Digital twin-driven product design framework,’’ Int. J. Prod.
Res., vol. 57, no. 12, pp. 3935–3953, 2019.
[30] S. Azhar, M. Khalfan, and T. Maqsood, ‘‘Building information modelling
(BIM): Now and beyond,’’ Construct. Econ. Building, vol. 12, no. 4,
pp. 15–28, 2012.
[31] A. Ghaffarianhoseini, J. Tookey, A. Ghaffarianhoseini, N. Naismith,
S. Azhar, O. Eﬁmova, and K. Raahemifar, ‘‘Building information
modelling (BIM) uptake: Clear beneﬁts, understanding its implemen-
tation, risks and challenges,’’ Renew. Sustain. Energy Rev., vol. 75,
pp. 1046–1053, Aug. 2017.
[32] Y. Xu, Y. Sun, X. Liu, and Y. Zheng, ‘‘A digital-twin-assisted fault diagno-
sis using deep transfer learning,’’ IEEE Access, vol. 7, pp. 19990–19999,
2019.
[33] M. Grieves and J. Vickers, ‘‘Digital twin: Mitigating unpredictable, unde-
sirable emergent behavior in complex systems,’’ in Transdisciplinary
Perspectives on Complex Systems. Cham, Switzerland: Springer, 2017,
pp. 85–113.
[34] S.
Boschert,
C.
Heinrich,
and
R.
Rosen,
‘‘Next
generation
digital twin,’’ in Proc. TMCE, I. Horvath, J. P. S. Riviero, and
P. M. H. Castellano, Eds. Las Palmas de Gran Canaria, Spain, May 2018,
pp. 209–217.
[35] A. E. Saddik, ‘‘Digital twins: The convergence of multimedia technolo-
gies,’’ IEEE Multimed., vol. 25, no. 2, pp. 87–92, Apr./Jun. 2018.
[36] S. Boschert and R. Rosen, ‘‘Digital twin—The simulation aspect,’’ in
Mechatronic Futures. Cham, Switzerland: Springer, 2016, pp. 59–74.
[37] J. Daily and J. Peterson, ‘‘Predictive maintenance: How big data analysis
can improve maintenance,’’ in Supply Chain Integration Challenges in
Commercial Aerospace. Cham, Switzerland: Springer, 2017, pp. 267–278.
VOLUME 7, 2019
147417


---

Page 13

---

S. H. Khajavi et al.: Digital Twin: Vision, Benefits, Boundaries, and Creation for Buildings
[38] Market Research Future. (Oct. 2017). Global Digital Twin Market is
Estimated to Grow at a Cagr of 37% From 2017 to 2023. Accessed:
Jan. 23, 2019. [Online]. Available: https://www.marketresearchfuture.com/
reports/digital-twin-market-4504
[39] A. N. Nasaruddin, T. Ito, and T. B. Tuan, ‘‘Digital twin approach to building
information management,’’ in Proc. Manuf. Syst. Division Conf., 2018,
p. 304.
[40] H. Kerosuo, R. Miettinen, S. Paavola, T. Mäki, and J. Korpela, ‘‘Challenges
of the expansive use of building information modeling (BIM) in construc-
tion projects,’’ Production, vol. 25, no. 2, pp. 289–297, 2015.
[41] U. M. Coraglia, D. Simeone, S. Cursi, A. Fioravanti, G. Wurzer, and
D. D’Alessandro, ‘‘A simulation model for logical and operative clash
detection,’’ Sharing Computable Knowl.!, vol. 2, pp. 519–534, Sep. 2017.
[42] X. Liu, M. Eybpoosh, and B. Akinci, ‘‘Developing as-built building infor-
mation model using construction process history captured by a laser scan-
ner and a camera,’’ in Proc. Construct. Res. Congr., Construct. Challenges
Flat World, 2012, pp. 1232–1241.
[43] S. Rufﬂe, ‘‘Architectural design exposed: From computer-aided drawing
to computer-aided design,’’ Environ. Planning B, Planning Des., vol. 13,
no. 4, pp. 385–389, 1986.
[44] R. Aish, ‘‘Building modelling the key to integrated construction CAD,’’ in
Proc. CIB 5th Int. Symp. Use Comput. Environ. Eng. Rel. Buildings, vol. 5,
1986, pp. 7–9.
[45] C. Parris. (Oct. 2017). A Twin-Building Army: GE Previews First-
Ever Digital Twin Analytics Workbench. Accessed: Sep. 13, 2019.
[Online]. Available: https://www.linkedin.com/pulse/twin-building-army-
ge-previews-ﬁrst-ever-digital-twin-colin-parris/
[46] GE Research. Digital Twin Creation. Accessed: Sep. 13, 2019. [Online].
Available: https://www.ge.com/research/offering/digital-twin-creation
[47] C. Preimesberger. (Jul. 2017). Why GE Digital Believes all Machines
Should Have a Digital Twin. Accessed: Sep. 13, 2019. [Online].
Available:
https://www.eweek.com/innovation/why-ge-digital-believes-
all-machines-should-have-a-digital-twin
[48] A. Jaribion, S. H. Khajavi, N. H. Motlagh, and J. Holmström, ‘‘[WiP] a
novel method for big data analytics and summarization based on fuzzy sim-
ilarity measure,’’ in Proc. IEEE 11th Int. Conf. Service Oriented Comput.
Appl. (SOCA), Nov. 2018, pp. 221–226.
[49] S. Madakam, R. Ramaswamy, and S. Tripathi, ‘‘Internet of Things (IoT):
A literature review,’’ J. Comput. Commun., vol. 3, no. 5, p. 164, 2015.
[50] K. M. Alam and A. El Saddik, ‘‘C2PS: A digital twin architecture reference
model for the cloud-based cyber-physical systems,’’ IEEE Access, vol. 5,
pp. 2050–2062, 2017.
[51] S. D. T. Kelly, N. K. Suryadevara, and S. C. Mukhopadhyay, ‘‘Towards the
implementation of IoT for environmental condition monitoring in homes,’’
IEEE Sensors J., vol. 13, no. 10, pp. 3846–3853, Oct. 2013.
[52] R. Jia, B. Jin, M. Jin, Y. Zhou, I. C. Konstantakopoulos, H. Zou, J. Kim,
D. Li, W. Gu, P. Nuzzo, S. Schiavon, A. L. Sangiovanni-Vincentelli,
C. J. Spanos, and R. Arghandeh, ‘‘Design automation for smart building
systems,’’ Proc. IEEE, vol. 106, no. 9, pp. 1680–1699, Sep. 2018.
[53] N. H. Motlagh, S. H. Khajavi, A. Jaribion, and J. Holmström, ‘‘An IoT-
based automation system for older homes: A use case for lighting system,’’
in Proc. IEEE 11th Int. Conf. Service-Oriented Comput. Appl. (SOCA),
Nov. 2018, pp. 1–6.
[54] D. Pavithra and R. Balakrishnan, ‘‘IoT based monitoring and con-
trol system for home automation,’’ in Proc. Global Conf. Commun.
Technol. (GCCT), Apr. 2015, pp. 169–173.
[55] H. Ghayvat, S. Mukhopadhyay, X. Gui, and N. Suryadevara, ‘‘WSN-
and IOT-based smart homes and their extension to smart buildings,’’
Sensors, vol. 15, no. 5, pp. 10350–10379, 2015. [Online]. Available:
http://www.mdpi.com/1424-8220/15/5/10350
[56] D. Wang, D. Lo, J. Bhimani, and K. Sugiura, ‘‘AnyControl—IoT based
home appliances monitoring and controlling,’’ in Proc. IEEE 39th Annu.
Comput. Softw. Appl. Conf., vol. 3, Jul. 2015, pp. 487–492.
[57] M. Alaa, A. A. Zaidan, B. B. Zaidan, M. Talal, and M. L. M. Kiah,
‘‘A review of smart home applications based on Internet of Things,’’
J. Netw. Comput. Appl., vol. 97, pp. 48–65, Nov. 2017. [Online]. Available:
http://www.sciencedirect.com/science/article/pii/S1084804517302801
[58] U. Verma. (Oct. 2018). What are Digital Twins in Smart Buildings?.
Accessed: Feb. 19, 2019. [Online]. Available: https://inbuildingtech.
com/bms/digital-twin-commercial-ofﬁce-building/
[59] U. Verma. (Nov. 2018). PropTech: How Digital Twins Impact OPM
in Smart Buildings. Accessed: Feb. 19, 2019. [Online]. Available:
https://inbuildingtech.com/uncategorized/digital-twins-proptech/
[60] Fraunhofer.
(Nov.
2019).
Building
From
Design
to
Demolition.
Accessed: Feb. 19, 2019. [Online]. Available: https://www.bau.fraunhofer.
de/en/ﬁeldsofresearch/smartbuilding/digital-twin.html
[61] S. Kaewunruen, P. Rungskunroch, and J. Welsh, ‘‘A digital-twin eval-
uation of net zero energy building for existing buildings,’’ Sustain-
ability, vol. 11, no. 1, p. 159, 2018. [Online]. Available: http://www.
mdpi.com/2071-1050/11/1/159
[62] A. Dementyev, S. Hodges, S. Taylor, and J. R. Smith, ‘‘Power consumption
analysis of Bluetooth low energy, ZigBee and ant sensor nodes in a cyclic
sleep scenario,’’ in Proc. IEEE Int. Wireless Symp. (IWS), Apr. 2013,
pp. 1–4.
[63] C. Gomez, J. Oller, and J. Paradells, ‘‘Overview and evaluation of
Bluetooth low energy: An emerging low-power wireless technology,’’
Sensors, vol. 12, no. 9, pp. 11734–11753, 2012.
[64] M. Siekkinen, M. Hiienkari, J. K. Nurminen, and J. Nieminen, ‘‘How low
energy is Bluetooth low energy? Comparative measurements with Zig-
Bee/802.15. 4,’’ in Proc. IEEE Wireless Commun. Netw. Conf. Workshops
(WCNCW), Apr. 2012, pp. 232–237.
[65] J.-S. Lee, M.-F. Dong, and Y.-H. Sun, ‘‘A preliminary study of low power
wireless technologies: ZigBee and Bluetooth low energy,’’ in Proc. IEEE
10th Conf. Ind. Electron. Appl. (ICIEA), Jun. 2015, pp. 135–139.
[66] H. Cao, V. Leung, C. Chow, and H. Chan, ‘‘Enabling technologies for
wireless body area networks: A survey and outlook,’’ IEEE Commun.
Mag., vol. 47, no. 12, pp. 84–93, Dec. 2009.
[67] T. Kumar and P. B. Mane, ‘‘ZigBee topology: A survey,’’ in Proc. Int. Conf.
Control, Instrum., Commun. Comput. Technol. (ICCICCT), Dec. 2016,
pp. 164–166.
[68] I. Kuzminykh, A. Snihurov, and A. Carlsson, ‘‘Testing of communication
range in ZigBee technology,’’ in Proc. 14th Int. Conf. The Exper. Designing
Appl. CAD Syst. Microelectron. (CADSM), Feb. 2017, pp. 133–136.
[69] A. R. Raut and L. Malik, ‘‘ZigBee: The emerging technology in building
automation,’’ Int. J. Comput. Sci. Eng., vol. 3, no. 4, pp. 1479–1484, 2011.
[70] S.-M. Darroudi and C. Gomez, ‘‘Bluetooth low energy mesh networks:
A survey,’’ Sensors, vol. 17, no. 7, p. 1467, Jul. 2017.
[71] R. Morais, M. A. Fernandes, S. G. Matos, C. Serôdio, P. J. S. G. Ferreira,
and M. J. C. S. Reis, ‘‘A ZigBee multi-powered wireless acquisition
device for remote sensing applications in precision viticulture,’’ Comput.
Electron. Agricult., vol. 62, no. 2, pp. 94–106, 2008.
[72] W. Bronzi, R. Frank, G. Castignani, and T. Engel, ‘‘Bluetooth low energy
performance and robustness analysis for inter-vehicular communications,’’
Ad Hoc Netw., vol. 37, pp. 76–86, Feb. 2016.
[73] B. L. R. Stojkoska and K. V. Trivodaliev, ‘‘A review of Internet of Things
for smart home: Challenges and solutions,’’ J. Cleaner Prod., vol. 140,
no. 3, pp. 1454–1464, 2017.
[74] S.
Salim.
(Jan.
2019).
Cool,
Comfortable
Homes
for
all.
Accessed: Feb. 15, 2019. [Online]. Available: https://www.straitstimes.
com/singapore/education/cool-comfortable-homes-for-all
[75] A. Amsyar. (Jan. 2019). NUS Launches Building With Net-Zero Energy
Consumption. Accessed: Feb. 15, 2019. [Online]. Available: https://www.
channelnewsasia.com/news/singapore/nus-building-net-zero-energy-
consumption-11184878
[76] F. Guerrini. (Jun. 2018). Built by Data: A Closed-Loop Digital Design
Workﬂow for Building Construction. Accessed: Feb. 17, 2019. [Online].
Available: https://www.eitdigital.eu/newsroom/news/article/built-by-data-
a-closed-loop-digital-design-workﬂow-for-building-construction/
[77] K. Främling, T. Ala-Risku, M. Kärkkäinen, and J. Holmström, ‘‘Design
patterns for managing product life cycle information,’’ Commun. ACM,
vol. 50, no. 6, pp. 75–79, 2007.
SIAVASH H. KHAJAVI received the Ph.D. degree
from Aalto University, Finland, in 2018. In his
Ph.D. dissertation, he explored the operations
management of additive manufacturing. He is cur-
rently a Postdoctoral Researcher and the Project
Manager with the Department of Industrial Engi-
neering and Management, Aalto University. His
research interests include additive manufacturing,
the Internet of Things, and digital twins.
147418
VOLUME 7, 2019


---

Page 14

---

S. H. Khajavi et al.: Digital Twin: Vision, Benefits, Boundaries, and Creation for Buildings
NASER HOSSEIN MOTLAGH received the Ph.D.
degree in networking technology from the School
of Electrical Engineering, Aalto University, Fin-
land, in 2018. He is currently a Postdoctoral
Researcher with the Department of Computer Sci-
ence, University of Helsinki. His research inter-
ests include the Internet of Things, environmental
sensing, wireless sensor networks, and unmanned
aerial vehicles.
ALIREZA JARIBION received the master’s degree
in industrial engineering, management, and sys-
tems efﬁciency. He is currently pursuing the Ph.D.
degree with the Department of Industrial Engi-
neering and Management, Aalto University, Fin-
land. His research interests include the Internet
of Things, digital twins, fuzzy logic, and big data
analytics.
LISS C. WERNER was a Guest Professor with
Carnegie Mellon University and Taylor’s Univer-
sity, Kuala Lumpur. She is currently an Archi-
tect and an Assistant Professor with the Institute
of Architecture, TU Berlin. She is also the Head
of the CyPhyLab, the IoT intelligent Prototype
Development Group, Department of Sustainable
Urban Planning and Design. She has lectured and
published internationally on cybernetics and com-
putational architecture.
JAN HOLMSTRÖM is currently a Professor
of operations management with Aalto Univer-
sity, Helsinki, Finland. He is also an Expert in
supply chain management and design science
research. He has published extensively on the
improvement of operations in industrial, project,
and retail supply chain contexts.
VOLUME 7, 2019
147419
