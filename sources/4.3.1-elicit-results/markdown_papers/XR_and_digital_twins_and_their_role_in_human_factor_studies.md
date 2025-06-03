

---

Page 1

---

TYPE Perspective
PUBLISHED 20 March 2024
DOI 10.3389/fenrg.2024.1359688
OPEN ACCESS
EDITED BY
Prashant K. Jain,
Oak Ridge National Laboratory (DOE),
United States
REVIEWED BY
Roberto Alonso González-Lezcano,
CEU San Pablo University, Spain
Sanjoy Moulik,
University of California, Riverside,
United States
*CORRESPONDENCE
Samrendra Roy,
roysam@illinois.edu
RECEIVED 21 December 2023
ACCEPTED 04 March 2024
PUBLISHED 20 March 2024
CITATION
Roy S, Singh S and Rizwan-uddin (2024), XR
and digital twins, and their role in human
factor studies.
Front. Energy Res. 12:1359688.
doi: 10.3389/fenrg.2024.1359688
COPYRIGHT
© 2024 Roy, Singh and Rizwan-uddin. This is
an open-access article distributed under the
terms of the Creative Commons Attribution
License (CC BY). The use, distribution or
reproduction in other forums is permitted,
provided the original author(s) and the
copyright owner(s) are credited and that the
original publication in this journal is cited, in
accordance with accepted academic practice.
No use, distribution or reproduction is
permitted which does not comply with
these terms.
XR and digital twins, and their
role in human factor studies
Samrendra Roy1,2*, Suneet Singh2 and Rizwan-uddin1
1Virtual Education and Research Laboratory (VERL), Department of Nuclear, Plasma, and Radiological
Engineering, University of Illinois at Urbana-Champaign, Urbana, IL, United States, 2Department of
Energy Science and Engineering, Indian Institute of Technology Bombay, Mumbai, India
Digital twins (DT) are synchronized clones that mirror their physical counterparts
at all times, enabling real-time monitoring, analysis, decision-making, and
planning for optimized operations. Digital twins can transcend traditional two-
dimensional interfaces by incorporating VR/AR/MR (XR) technology, providing
immersive, intuitive, and interactive representations of systems, assets, and
processes. Furthermore, real-time data from sensors, simulations, and other
sources can be integrated into the XR-enabled digital twins, leading to better
and more intuitive understanding and to more efficiently monitor, analyze,
and maintain complex systems such as nuclear assets. Immersive, interactive,
multi-player XR capabilities embedded in DTs will allow spatially accurate and
more realistic representation, leading to improved risk assessment, optimized
and predictive maintenance scheduling, enhanced situational awareness, and
more effective communication among interdisciplinary teams. By combining the
strengths of XR and digital twins, nuclear facilities can achieve heightened safety,
operational efficiency, and decision-making accuracy. Marrying XR technology
with digital twins is also likely to extend the utilization of digital twins to
optimize those aspects of the design and operation of nuclear assets that
involve human beings–specifically in human factors engineering. Training can
also be significantly enhanced if DTs are linked with XR technology. These
systems may also be used to assess human performance through human factors
engineering for the safety analysis of nuclear assets. A specific example is
assessing human performance in semi-autonomous nuclear assets or operating
multiple nuclear assets. After briefly reviewing digital twins of nuclear systems
from the perspective of XR technology, this paper summarises our work in
the nuclear energy space on VR/AR/MR and how these can be integrated
into the newly evolving DTs of nuclear assets. The paper also describes the
potential use of such systems in optimizing the design and operations of nuclear
systems. As XR technology advances, its symbiotic relationship with digital
twins can significantly reshape the landscape of nuclear operations and asset
management.
KEYWORDS
virtual reality, augmented reality, mixed reality, human factors, digital twins, nuclear
environments, real-time monitoring, asset management
1 Introduction
Significant advances over the past 20 years in computing and digital technology
have resulted in the emergence of artificial intelligence (AI) and virtual reality
(VR) as two of the most promising and groundbreaking enabling technologies.
Frontiers in Energy Research
01
frontiersin.org


---

Page 2

---

Roy et al.
10.3389/fenrg.2024.1359688
While AI and Machine Learning (ML) are slowly gaining traction
in the nuclear sector for various applications, the widespread
integration of VR technology, which has been around in a fairly
mature form for longer than the AI, is yet to be realized.
This paper aims to shed light on the untapped potential of
integrating VR technology with digital twins for nuclear asset
management. VR is not presently utilized in DTs of NPP. Instead,
we propose it as an integrable technology to DTs, introducing
an additional layer to human vision and perception. This paper
presents a perspective (derived through various studies) that
anticipates a reduction in cost and time when used to include direct
human involvement in designing and evaluating semi-autonomous
DT components. Furthermore, VR is highlighted as a significant
enhancer of human perception that has the potential for intuitive
visualization of real-time data of DTs, surpassing traditional 2D
screens. By exploring the possibilities and benefits, this paper aims
to inspire and motivate researchers to delve deeper into the realm of
VR technologies, fostering innovation and advancements in nuclear
science and technology in the context of digital twins.
2 Digital twin
The term digital twin refers to any virtual representation of
a physical system, such as a turbine, a chemical plant, or an
automobile. Yadav et al. (2021) noted that the term digital twin can
have different definitions based on context and industries. Generally,
the terms digital twins or digital twin system refer to a digital
representation of a currently existing or under-design physical
counterpart. When the physical system is already in existence, there
is a link between the physical system and its digital twin. This
connection facilitates the continuous data exchange between the two
systems. The digital twin is expected to be in the same state as that
of the physical system at all times. If the prediction by the digital
twin deviates from the actual state of the physical system at any
time, the data from the physical system is used to correct and bring
the digital twin in conformity with the current state of the physical
system. Among other goals, digital twins are expected to be used to
predict the future state for operational management and planning.
DTs are to be used for monitoring, diagnostics and prognostics, and
to optimize asset performance and utilization. By combining sensory
data with past experience (through AI) and human expertise, DTs
can be used to improve performance and productivity.
As technology advances, it is crucial to explore the use of other
emerging and enabling technologies that can be integrated in digital
twins. While continuously advancing computing and AI/ML are
likely to impact the evolution of digital twins in many ways, VR
(and its variations) is in a unique position to help integrate humans
and introduce realistic human-machine-interface in the digital twin.
This is likely to address ergonomics, evaluation of human factors,
and human interactions with machines through realistic digital
interfaces. Introduction of VR in digital twins will allow to more
realistically capture and simulate the important role that humans
play in the operation of any physical system. The subsequent sections
will delve into different types of VR technologies and some of their
applications in academia and in the nuclear industry. This will be
followed by a discussion on the prospects of integration of VR in
digital twins.
3 Virtual reality
Virtual Reality (VR) comprises of technologies that enable
immersive human interaction with digitally created entities. VR
refers to technology and devices in which the user is completely
immersed in the digital world, with no interactions with the physical
surroundings. The user in VR may interact with the digital content.
While current VR technologies primarily focus on stereoscopic
vision for complete 3-D immersion, ongoing advancements aim to
enhance immersion by targeting additional senses such as haptic,
taste, and olfactory, mimicking even more realistic real-world
experiences. VR hardware over the last few decades has evolved
from the early million-dollar CAVE systems to few-hundred-dollars
head-mounted displays (HMDs), to even few-dollars cardboard
boxes in which regular smart phones can be used to experience
3-D immersion. Software for application development has also
evolved from early developments being done in OPEN-GL to
modern game development platforms (Early VR technologies, like
the CAVE, and their use in the nuclear field are discussed in Rizwan-
uddin et al. (2003). Head-mounted displays (HMDs) are the most
recent technological developments in VR. Discussion in this article
is limited to HMDs.)
Extensions of VR have led to augmented (AR) and mixed reality
(MR). Augmented reality (AR) entails experiencing the physical
and the digital (virtual) worlds simultaneously, through inputs
such as vision. It is, for example, achieved by seeing the physical
world through the transparent part of the HMD’s screen, while
simultaneously having access to digital contents on another part of
the HMD. The digital content can even be overlaid on the physical
objects. In general, there is none to very limited interactivity in
AR between the user and the digital content. Currently the most
advanced of these technologies is called mixed reality (MR). MR
is AR with interactive digital content. Feeding AR devices with
sensory inputs and data from the physical system allows interactivity
between the digital content and the physical world. Most XR devices
are now incorporating some MR capabilities, for example, in the
form of depth sensors or interactive digital/virtual drop-down menu
(Note that the definition of VR, AR, MR and other similar terms such
as extended reality (XR, a term sometimes used to collectively refer
to AR, MR and VR) are continuously evolving.)
4 Virtual reality in the nuclear industry
Research and development in virtual technology for nuclear
applications can be traced back to the early 2000s in Karancevic
and Rizwan-uddin (2003) and Andritsos et al. (2004). That was pre-
HMD period. Earlier developments included walk-through models
of nuclear power plants and 3-D models of other assets that could
be visualized in VR hardware. Later developments included several
interactive capabilities such as “displaying” the radiation field in 2-D
and 3-D and virtual interactive models of modern control rooms. As
in academia, nuclear industry has also taken only limited advantage
of advances in the VR technology (Pitkänen, 2020). Outsourcing
the development of the VR models and early VR hardware had
both been expensive. However, decreasing cost of VR hardware and
increasing awareness and familiarity of the new workforce with this
technology are making VR more appealing to the nuclear industry.
Frontiers in Energy Research
02
frontiersin.org


---

Page 3

---

Roy et al.
10.3389/fenrg.2024.1359688
There is recognition that the VR technology can be effectively used
for education and training, as well as in dose minimisation efforts at
nuclear power plants (NPPs). There is potential for VR to transform
safety protocols, training methods, and operation and maintenance
practices within the nuclear sector. State of specific aspects of VR
and its use in the nuclear sector–both, industrial and academic–are
reviewed in the following subsections.
4.1 Dose minimisation and
decontamination & decommissioning
Minimising the dose that workers receive when working in
radiation environment is critical. Minimising the amount of time
spent around radiation and avoiding the high radiation areas
whenever possible will help in dose minimisation. Familiarity with
the work environment, familiarity with the radiation field in the
work area, and excessive practice of the task to be completed
can significantly reduce the amount of time workers spend in
radiation environments and thus the total dose they receive.
Ideally, a facility that is an identical twin of the workspace, but
without the radiation, can be used for training the workforce.
Radiation-related situational awareness can be communicated in
this physical twin by marking high and low radiation areas. This
is however an expensive preposition. On the other hand, VR
technology excels in communicating spatial awareness and 3-D
visualization, and is inexpensive. Any VR experience in the virtual
equivalent of a physical space is likely to be remembered and
impact actions and behavior when the user is later operating in
the corresponding physical space. Employing VR to train for work
in such a harmful environment offers a much simpler and more
cost effective approach. Not only the worker can become familiar
with the space in which work needs to be performed, even the
radiation levels in different parts of the virtual 3-D facility can be
shown. By developing a virtual replica of the workspace, workers
can be trained in a safe and radiation-free environment, and
develop situational and radiation awareness before setting foot in the
hazardous physical workspace.
Hanifah et al. (2017) reported the culmination of efforts that
resulted in a virtual dose minimization game that can be played
on smart phones. The game was initially developed for computers
and immersive devices. The game is played in a 3-D virtual model
of the TRIGA Mark II1 nuclear reactor, which was located at the
University of Illinois campus in Urbana (Yoshinori et al., 2014). This
virtual model has gone through several upgrades. This model is a
fairly accurate and to-scale representation of the TRIGA facility. The
facility had several levels, with the reactor bay near the center. Stairs
led to the top of the bay. The neutron beam lines were in the large
open area at the lowest level. The virtual, 3D, interactive model of
the TRIGA research reactor was created using the Unity-3D game
engine. It allows users to explore the facility. This virtual facility was
selected for the dose minimization game as it is a multi-level building
with several floors and many rooms, making the game challenging
and engaging. For the dose minimization game, this model is used
1
https://distributedmuseum.illinois.edu/exhibit/triga-mark-ii-nuclear-
reactor/
as a facility with varying levels of radiation due to multiple (virtual)
radiation sources of different strengths, stored in different locations
in the multi-level building, leading to a realistic radiation field.
Additionally, virtual objects are placed in the building, which are to
be collected by the player. In this scavenger hunt game, the player
is to navigate through the reactor building and collect the desired
objects while receiving minimal radiation dose. This game built
upon capabilities developed earlier that included the capability to
display the radiation level in the 3-D virtual model of a facility by
coloring the floor. The display of the radiation level can be turned
on or off. Virtual dosimeter developed earlier, is also integrated in
this dose minimisation game. Player simply picks up the dosimeter
and starts performing the assigned tasks. Based on the radiation
level, location of the player and time spent, a counter at the bottom
of the screen shows the dose received. Dosimeter feature can also
have a beeping sound similar to that of a Geiger counter. At the
end of the game, the dose received (in mSv), the time duration over
which the radiation map was viewed, and a score based on these two
factors, are displayed. Player can thus learn about three important
concepts in radiation protection: time, distance, and shielding. The
radiation field in these models is provided as an input. It can be
pre-calculated using radiation transport codes such as MCNP, or
a simplified version of the field can be on the fly calculated using
simple point kernel type method (Rizwan-uddin, 2018; Hagita et al.,
2020).
The virtual model of the reactor facility was used in a study
to assess the feasibility of using 3-D models to train personnel for
operations in an alien environment (Kriz et al., 2010) through prior
training in the virtual 3-D model of the facility.
Nuclear decommissioning poses significant challenges due to
potential exposure to high radiation levels. VR has been shown
to be effective in training workers for decommissioning scenarios,
addressing the critical need to prepare them for handling radioactive
materials during decontamination and decommissioning. A VR
training system was proposed by Jeong et al. (2014) to enhance
safety during nuclear power plant decommissioning, emphasizing
a framework for system development and the inclusion of
multiplayer capabilities. While the study demonstrated improved
worker familiarity with the environment, data were lacking. A
subsequent study (Jeong et al., 2016) provided extensive results,
focusing on ergonomic assessment in a radiation environment.
The study assessed optimal postures for descending in various
scenarios, acknowledging limitations in evaluating postures due
to the restricted motion control using mouse and keyboard
controls. Despite the limitations, these studies offer a foundation
for the future use of VR in nuclear power plant operations, as
well as decontamination and decommissioning. Another study
by Sato et al. (2020) also discusses the use of VR and 3D
imaging technique for visualization of radioactive substances during
decommissioning training.
4.2 Labs and training
VR provides a cost effective method of “hands on” training
with equipment. It can also be used to conduct virtual experiments
in a virtual lab to better communicate physics concepts (Rizwan-
uddin, 2020; Ilie, 2021). It can be used to supplement physical
Frontiers in Energy Research
03
frontiersin.org


---

Page 4

---

Roy et al.
10.3389/fenrg.2024.1359688
labs in academia, and equipment training in industry. The Virtual
Education and Research Laboratory (VERL) at the University
of Illinois at Urbana-Champaign has developed 3-D and VR
models, including labs for radiation shielding experiment, half-
life measurement experiment, and calorimetry experiment. These
virtual labs offer hands-on experience, integrating cutting-edge
virtual technologies into education (Xi et al., 2009; Haddish et al.,
2013; Satoh et al., 2015). Some of these are briefly described below.
4.2.1 Shielding lab
One of the first developed for nuclear applications, the player
in this virtual lab can measure the attenuation coefficients of four
different materials. This VR lab aims to provide a highly realistic
environment, emphasizing lifelike graphics, detailed 3-D models,
textures, and realistic lighting to enhance immersion. While the
physics is simple, the focus is on crafting an intricately detailed
setting. The model is shown in Figures 1A, B. The goal of this lab
is to make users feel present in the lab environment when doing
the experiments. Users can manipulate shielding blocks made of
different materials, place multiple blocks between the radiation
source and the detector, thus effectively changing the thickness of
the shielding, and operate the radiation measurement equipment.
The student clicks on the shielding blocks placed on the table, which
moves them next to a scale, allowing the student to measure their
thickness. Next, clicking on the block moves it to the space between
the radiation source and the detector. Counts can then be measured
by setting the time interval and clicking on the counter button. The
process is repeated for different numbers of shielding blocks, thus
gathering data for different thicknesses. The entire process can then
be repeated for blocks made of different materials. The physics model
is based on the attenuation model (e-μΔ x), where Δ x is the thickness
of the shielding material. The data displayed is realistic and can be
used to estimate the attenuation coefficient of the shielding material.
The virtual model has gone through several upgrades over the years.
Figure 1A shows the virtual lab. Figure 1B shows two of the shielding
blocks placed in between the radiation source (on the left) and the
detector (on the right). Other shielding blocks (C, D and E) are
placed on the table. Collimator blocks can also be seen.
4.2.2 Calorimetry lab
The virtual calorimetry lab is designed to measure the specific
heat of metals. This laboratory has virtual instruments (like scale
and hotplate) and virtual monitors. Virtual instruments in the model
are interactive, and can be moved and/or operated by the player.
For example, the specimens in the experiment can be moved. When
a specimen is placed on the scale, the virtual scale displays its
weight in its digital window. The virtual hotplate can (virtually)
heat the objects placed on it (Figure 1C). Clicking the knob on
the hotplate turns it on/off. Thermocouples can be connected to
objects. The temperature is displayed on the computer monitor
in real time. Step-by-step instructions are displayed through GUI.
Steps include measuring the mass of the metal specimens, heating
the water to 100°C (when the temperature reaches 100 C, bubbles
are generated in the beaker), heating the specimen to 100°C by
placing it in the boiling water, measuring and pouring water at
room temperature (20°C) in the calorimeter, placing the specimen
in the calorimeter, attaching the thermocouples, and observing and
noting down the temperature change on the virtual computer screen.
A simple physics model based on conservation of thermal energy
is coded to evaluate the temperature of the water and the metal
specimen as a function of time.
A recent improvement is the introduction of improved haptic
feedback with new controllers. Through the Virtual Grasp API,2
users can hold two objects, like beakers and metal specimens (at
any angle, to facilitate the pouring action), in two different hands
as shown in Figure 1C, mimicking real lab setups. The sensation
of different weights can be replicated using strong or gentle haptic
vibrations. Another improvement made in this lab is by making
the lab setup more realistic. For example, a single click in the older
version connected a wire (such as a thermocouple) to its intended
location. The user in the new version can “grab” the tip of the wire
and then “insert” it at the desired port or object where it needs to be
connected (Figure 1D).
4.2.3 TRIGA reactor lab
3-D model of the TRIGA reactor facility described in Section 4.1
(Stefano and Rizwan-uddin, 2006) was used to develop the TRIGA
reactor lab. A virtual control room, very similar to the actual
control room, was developed to conduct reactor experiments.
The development process of the virtual reactor consists of three
major parts: 3D modeling; event scripting; and user interactions.
Specifically, the buttons and knobs in the virtual control room
were made interactive, and a reactor physics model was added to
determine the reactor behavior in response to specific operator
actions. Point reactor kinetics (one delayed neutron precursor)
with simplified thermal (fuel temperature) feedback model is
implemented to determine the real time reactor response to operator
actions. Measured differential rod worth tables from the original
reactor are used to determine the amount of reactivity that is inserted
for each rod at each rod position. Reactivity and power levels are
displayed on the panel. This virtual model of the reactor allows users
to explore the facility, and virtually operate the reactor from the
control room.
Figure 2A shows the reactor control room in the virtual model.
Reactor bay can be seen through the glass panel in front of the
control desk in Figure 2B shows a zoomed-in view of the control
panel. Figure 2C shows additional parts of the control panel. The
buttons and knobs of the control panel in the model are interactive,
and can be operated by the player or operator. The power key,
the switch labeled FIRE and the knob labeled TR SELECT in
the left side of Figure 2C; and switches labeled AIR, MAGNET,
UP, DOWN, ACKNOWLEDGE, and SCRAM in the right side of
Figure 2C can be manipulated (clicked on) by the operator. For
example, a supervisor must turn the (virtual) power key to the
ON position before any other action can be carried out. Clicking
on the Fire button fully raises the transient rod, which is one of
the control rods.
Several other features reported earlier—such as displaying the
radiation level by coloring the floors, virtual dosimeter, in-game
step-by-step instructions, and remote security cameras—have also
been implemented in this reactor model. Virtual and interactive
research reactor model is fairly realistic. It can be used to supplement
reactor lab experience for students as well as reactor operators. If
2
https://www.virtualgrasp.com/
Frontiers in Energy Research
04
frontiersin.org


---

Page 5

---

Roy et al.
10.3389/fenrg.2024.1359688
FIGURE 1
Pictures showing (A) Side by side comparison of the virtual and physical labs (B) Virtual model of the shielding lab, and (C,D) show VR calorimetry lab.
used judiciously, it offers a cost effective approach to enhance reactor
operations experience.
Key contribution in another study (Kiryukhin et al., 2020),
focused on replicating a graphite-uranium subcritical (GUS)
assembly experiment, is in visualizing neutron flux in 3-D (in VR)
using pre-calculated data.
4.3 Control room simulator
The need to develop virtual models of NPP control rooms first
arose when there was a desire to assess conversion of analog control
rooms in currently operating NPPs to digital control rooms, and
to develop fully digital control rooms for advanced NPP designs.
Issues surrounding human factors, personnel interactions, line of
sight, and situational awareness, could potentially be researched
and addressed using 3D virtual models of NPP control rooms.
However, VR’s limitations, including resolution issues, susceptibility
to motion sickness, discomfort, limited field of view, and restricted
haptic feedback, have so far hindered its widespread adoption as an
alternative for control room training.
Simulators for nuclear power plant control room (NPP-CR), to
be used for design and training, can include multiple components
such as control consoles, simulation software, safety systems,
communication setups, and more. Transforming these elements into
VR requires integration across domains, including 3-D designers,
Frontiers in Energy Research
05
frontiersin.org


---

Page 6

---

Roy et al.
10.3389/fenrg.2024.1359688
FIGURE 2
Virtual models of UIUC TRIGA reactor. (A) A view of the control room. (B) A close-up control panel view. (C) Further close-up views of the right and left
sides of the control panel shown in (B).
software developers, and CR operators. Bergroth et al. (2018)
report the use of VR in control room assessment. Experienced
NPP operators participated in this study, which was centered
around operator response in an emergency scenario. The crew
had to follow procedural instructions in VR. The crew identified
(through questionnaires on monitoring, operation, and procedural
adherence)
VR’s
limitations,
such
as
resolution
challenges,
communication, and lack of tactile feedback during operation. The
study suggested that with improvements, Virtual Reality Control
Rooms (VR CR) can offer realistic early-stage design and ergonomic
evaluation (Gatto et al., 2013; Lee and Cha,2019), facilitating flexible
design changes and cost savings (Qin et al., 2020) through multiple
validations before physical modification. This study provides a
blueprint for VR development in control room training, addressing
both human and technical factors.
Another study (Pitkänen, 2020) briefly outlines the tools used
to construct the VR CR model. A notable aspect in this study
is the introduction of small VR simulator applications, offering
fundamental VR training before participants enter more complex
environments like a control room simulator. These applications,
covering fire safety evacuation and valve operation training, proved
highly beneficial for participants unfamiliar with VR, helping them
become acquainted with the technology, evident in comprehensive
participant ratings expressing satisfaction with the virtual CR
experience.
5 VR, digital twins, and human factors
Digital twins of various assets in the NPPs and of entire nuclear
power plants promise a framework in which a digital and time-
synchronized replica of the asset is available to the operators. These
DTs can be used for operational and planning purposes.
DTs have so far been in general described as uber-simulators,
available on (2D) computer screens. DTs on their own do not
have any three-dimensional equivalence with the actual equipment
or plant they represent. This lack of 3-dimensionality in DTs
restricts embedding of humans in the loop in a realistic fashion.
Thus, assessments and studies that involve humans cannot be
realistically carried out on classical DTs. Thus, integrating DTs
and VR is likely to improve DTs in three significant ways. First,
a VR/AR/MR (XR) model of the equipment or the facility will
allow a much more realistic training environment for the workforce,
enhancing the safety and ergonomic considerations of NPPs and
their assets. The immersive visualizations facilitated by VR will
offer a considerable advantage in the real-time monitoring of
Frontiers in Energy Research
06
frontiersin.org


---

Page 7

---

Roy et al.
10.3389/fenrg.2024.1359688
nuclear assets. Second, it will provide situational awareness (around
the equipment) to the plant operators as they take advantage
of the DT to improve operational efficiency through the control
and management of nuclear assets. XR will enhance decision-
making capabilities by overlaying critical data directly in front
of equipment operators. And third, VR+DT systems will allow
human factor studies to be conducted on DT providing valuable
feedback in the design and manufacturing stages of NPP’s lifecycle
by employing human operators in the virtual framework of the
digital twin.
There have been limited integration or even discussion of
integration of DTs and VR thus far in any industry. One
recent study (Coupry et al., 2021) reviewed literature on DTs
of building information modeling (BIM) and XR devices to
improve maintenance procedures in smart buildings. This is a
fairly exhaustive review with a large bibliography and extensive
review of both, DT and XR technologies. From varying definitions
of “digital model,” “digital shadow,” and “digital twin,” to ever
rapidly evolving XR technologies, authors have extensively discussed
the background as well as potential use of XR with DTs. This
review goes beyond just the application of these technologies
to building maintenance. Demonstrations of the use of the XR
technology to nuclear applications discussed in the previous sections
are similar to what is being implemented in other industries.
Thus, integration of XR in DT of nuclear systems can also
benefit from similar efforts in other industries, such as building
maintenance.
There are two areas specific to nuclear that may benefit from
the integration of XR in DTs more than in some other industries.
First is the assessment of human performance, and the second is the
facilitation of semi-autonomous control and operations of nuclear
assets. During the design phase of semi-autonomous digital twin
(DT) systems, evaluating their interaction with humans is crucial.
Gathering direct data on human interaction becomes essential
for conducting risk and ergonomic assessments throughout the
design process of these semi-autonomous systems. Traditionally,
gathering such data should involve iterative changes to the physical
components based on their interaction with humans, incurring both
cost and time; virtual generation of this data facilitated through VR
can be cost-effective and faster. Furthermore, XR devices have the
potential to enhance semi-autonomous control and operations in
the nuclear asset management of DTs. They can offer operators an
immersive interface, projecting 3D representations and real-time
data overlays directly onto physical components. When integrated
with IoT sensors, XR can facilitate emergency responses and foster
collaborative decision-making, potentially improving overall plant
efficiency and ensuring a safer and more responsive nuclear power
plant operation.
Kuts et al. (2019) described the synchronized control of
industrial robotic cell through a combination of its digital twin
and VR. This is of relevance to the nuclear industry as with better
VR controls, it will be feasible to manage nuclear assets in 3-
D in real-time using robotics, networking, and low-latency IoT
devices, offering increased precision and safety. Overseeing of semi-
autonomous assets using DTs, especially those assets that employ
machine learning (ML) and artificial intelligence (AI) for safety and
maintenance decisions, may be facilitated by improved training on
a combination of DT and XR.
Integration of VR with DT can play a pivotal role in
nuclear asset management, evident by ongoing technological
advancements aligning with the sector’s specific needs. This
integration of VR and digital twins is expected to create a
symbiotic relationship covering the entire lifecycle of nuclear asset
management, including human factor studies. Despite limited
studies, increased research engagement is expected to expedite its
implementation. This paper provides insights into potential VR and
DT applications, urging further exploration. It also advocates for
additional research to enhance the reliability of VR-DT systems
and position them as a cost-effective alternative in nuclear asset
management.
Data availability statement
The raw data supporting the conclusion of this article will be
made available by the authors, without undue reservation.
Author contributions
SR: Conceptualization, Formal Analysis, Writing–original
draft. SS: Investigation, Validation, Writing–review and editing.
R-u:
Investigation,
Supervision,
Validation,
Writing–review
and editing.
Funding
The authors declare that no financial support was received for
the research, authorship, and/or publication of this article.
Acknowledgments
We
would
like
to
acknowledge
the
large
number
of
undergraduate
students
in
NPRE
and
other
departments
at
the
University
of
Illinois
at
Urbana
Champaign
who,
over
the
last
20 years,
have
contributed
to
the
work
reviewed here.
Conflict of interest
The authors declare that the research was conducted in the
absence of any commercial or financial relationships that could be
construed as a potential conflict of interest.
Publisher’s note
All claims expressed in this article are solely those of the
authors and do not necessarily represent those of their affiliated
organizations, or those of the publisher, the editors and the
reviewers. Any product that may be evaluated in this article, or claim
that may be made by its manufacturer, is not guaranteed or endorsed
by the publisher.
Frontiers in Energy Research
07
frontiersin.org


---

Page 8

---

Roy et al.
10.3389/fenrg.2024.1359688
References
Andritsos, D., Griffith, J., Karancevic, N., Jevremovic, T., Stubbins, J., and Rizwan-
uddin,
(2004). INIE collaboration between UIUC and Purdue on virtual reactor
development. Trans. Am. Nucl. Soc. 91, 992–993.
Bergroth, J. D., Koskinen, H. M. K., and Laarni, J. O. (2018). Use of immersive 3-D
virtual reality environments in control room validations. Nucl. Technol. 202, 278–289.
doi:10.1080/00295450.2017.1420335
Coupry, C., Noblecourt, S., Richard, P., Baudry, D., and Bigaud, D. (2021). BIM-based
digital twin and XR devices to improve maintenance procedures in smart buildings: a
literature review. Appl. Sci. 11, 6810. doi:10.3390/app11156810
Gatto, L. B. S., Mól, A. C. A., Luquetti dos Santos, I. J., Jorge, C. A. F., and Legey,
A. P. (2013). Virtual simulation of a nuclear power plant’s control room as a tool for
ergonomic evaluation. Prog. Nucl. Energy 64, 8–15. doi:10.1016/j.pnucene.2012.11.006
Haddish, I., Rizwan-uddin, and Li, Y. (2013). “Fully interactive virtual labs for
training and education,” in Proc. Conference on Nuclear Training and Education
CONTE 2013 (Jacksonville, FL: American Nuclear Society).
Hagita, K., Kodama, Y., and Takada, M. (2020). Simplified virtual reality training
system for radiation shielding and measurement in nuclear engineering. Prog. Nucl.
Energy 118, 103127. doi:10.1016/j.pnucene.2019.103127
Hanifah, Z., Mattingly, G., Riewski, E., Tan, Q., Chun, D., and Rizwan-uddin, (2017).
“Recent developments in virtual dose minimization game for education, training and
outreach,” in ETrap 2017, Valencia, Spain, 30 May 2017 - 2nd June 2017.
Ilie, R. (2021). Developing virtual reality labs for EM courses, VRIllinois.
Available at: https://vr.illinois.edu/2021/04/21/developing-virtual-reality-labs-for-em-
courses/ (Accessed December 17, 2023).
Jeong, K., Choi, B., Moon, J., Hyun, D., Lee, J., Kim, I., et al. (2014). The scenario-
based system of workers training to prevent accidents during decommissioning of
nuclear facilities. Ann. Nucl. Energy 71, 475–479. doi:10.1016/j.anucene.2014.04.033
Jeong, K., Choi, B., Moon, J., Hyun, D., Lee, J., Kim, I., et al. (2016). An
evaluation on the scenarios of work trajectory during installation of dismantling
equipment for decommissioning of nuclear facilities. Ann. Nucl. Energy 91, 25–35.
doi:10.1016/j.anucene.2016.01.002
Karancevic, N., and Rizwan-uddin, (2003). Virtual systems for understanding and
advancement of nuclear power. Trans. Am. Nucl. Soc. 88.
Kiryukhin, P., Shcherbakov, A., Romanenko, V., Pugachev, P., Khomyakov, D.,
Tikhomirov, G., et al. (2020). Development of a virtual analogue of uranium-graphite
subcritical assembly and visualization of the neutron flux distribution in virtual reality.
Procedia Comput. Sci. 169, 192–197. doi:10.1016/j.procs.2020.02.135
Kriz, Z., Wu, H., Aaron, M. C., Rytych, C., Conley, L., Prochaska, R., et al. (2010). An
assessment of a game-like 3-D model for training at NPPs. Trans. Am. Nucl. Soc. 102,
65–66.
Kuts, V., Otto, T., Tähemaa, T., and Bondarenko, Y. (2019). Digital twin based
synchronised control and simulation of the industrial robotic cell using virtual reality.
J. Mach. Eng. 19, 128–144. doi:10.5604/01.3001.0013.0464
Lee, H., and Cha, W. C. (2019). Virtual reality-based ergonomic modeling and
evaluation framework for nuclear power plant operation and control. Sustainability 11,
2630. doi:10.3390/su11092630
Pitkänen, V. (2020). “Utilization of virtual reality in loviisa nuclear power plant,”.
Master’s Thesis (Finland: LUTPub).
Qin, S., Wang, Q., and Chen, X. (2020). Application of virtual reality
technology in nuclear device design and research. Fusion Eng. Des. 161, 111906.
doi:10.1016/j.fusengdes.2020.111906
Rizwan-uddin, (2018). Virtual reality for education, training and dose reduction.
Nucl. Plant J. 36, 30–33. Online/Virtual.
Rizwan-uddin, (2020). “Role and status of VR/AR/MR in digital twins in the nuclear
industry,” in Presentation at the Workshop on Digital Twin Applications for Advanced
Nuclear Technologies (INL/ORNL) Virtual/online.
Rizwan-uddin, Karancevic, N., and Tikves, S. (2003). “Virtual reality: at the service
of GEN-IV, and V,” in Proc. Int Congress Advances in Nuclear Power Plants, Cordoba,
Spain, May 4 2003 - May 7 2003.
Sato, Y., Minemoto, K., Nemoto, M., and Torii, T. (2020). Construction of
virtual reality system for radiation working environment reproduced by gamma-
ray imagers combined with slam technologies. Nucl. Instrum. Methods Phys. Res.
Sect. A Accel. Spectrom. Detect. Assoc. Equip. 976, 164286. doi:10.1016/j.nima.
2020.164286
Satoh, Y., Zhu, X., Li, Y., Kuprianczyk, C. A., and Rizwan-uddin, (2015). “Virtual
research reactor with interactive control room for reactor operator training,” in Proc. 9th
International Topical Meeting on Nuclear Plant Instrumentation, Control, and Human-
Machine Interface Technologies 2015, February 22–26, 2015, (Charlotte: American
Nuclear Society), 1589–1596.
Stefano, M., and Rizwan-uddin, (2006). “A virtual control room with an embedded,
interactive nuclear reactor simulator,” in Proc. 5th International Topical Meeting on
Nuclear Plant Instrumentation Controls, and Human Machine Interface Technology
2015, Albuquerque, USA, 675–679.
Xi, C., Wu, H., Joher, A., Kirsch, L., Luo, C., Khasawneh, M., et al. (2009).
“3-D
virtual
reality
for
education,
training
and
improved
human
performance
in
nuclear
applications,”
in
Proc.
6th
American
Nuclear
Society
International
Topical
Meeting
on
Nuclear
Plant
Instrumentation,
Control,
and
Human-Machine
Interface
Technologies
2009,
Knoxville,
Tennessee, April 5-9, 2009 (LaGrange Park, IL: American Nuclear Society),
2347–2356.
Yadav, V., Zhang, H., Chwasz, C. P., Gribok, A. V., Ritter, C., Lybeck, N. J., et al. (2021).
“The state of technology of application of digital twins,”. Tech. rep. (Washington, DC:
U.S. Nuclear Regulatory Commission).
Yoshinori, S., Ye, L., Xuefeng, Z., and Rizwan-uddin, (2014). “Interactive virtual
reactor and control room for education and training at universities and nuclear power
plants,” in Proc. of the ISOFIC/ISSNP 2014 (Korea: Republic of Korean Nuclear
Society).
Frontiers in Energy Research
08
frontiersin.org
