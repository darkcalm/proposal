

---

Page 1

---

Agent-Based Distributed Energy Resources for 
Supporting Intelligence at the Grid Edge 
Abstract— This paper proposes a novel multi-agent framework 
that can link various forms of resources and power electronic 
systems into distributed energy resources (DER). The proposed 
multi-agent architecture can also integrate DERs to a central 
controller for optimization and control to support the grid. To 
demonstrate the flexibility of this novel framework, the developed 
agent system is applied to a set of end-use systems. The agent 
framework is validated in hardware using controller-hardware-
in-the-loop (CHIL) simulation platform.   
Index Terms-- agents, distributed energy resources, energy 
storage, power electronics, renewables 
I.  INTRODUCTION 
The electric grid has seen significant advancements driven 
by an evolution in available low-cost computational 
horsepower and intelligent systems that are pushing 
technological development to the grid edge. One area where 
distributed intelligence is having a significant impact is in 
distributed energy resources (DERs). 
In recent years, renewable energy (RE) and energy storage 
(ES) costs have seen significant reductions as the technologies 
continue to mature and reach market acceptance [1]-[3]. This 
has led to growing deployments and a shift in generation from 
centralized systems to DERs. This is a key challenge as large 
generators that previously provided our system energy needs 
and stability are being replaced with large volumes of small 
hierarchal systems. In the past, these small systems have only 
represented a small percentage of the overall system capacity 
and could be adopted into electric grid without significant 
oversight. However, as these numbers grow, advanced controls 
and low-cost integration and implementation techniques are 
becoming vital [1]-[3].  
Many RE and ES system technologies utilize power 
electronic systems (PES) for energy conversion and grid 
integration. The integration of the resource with a PES often 
requires significant engineering and development even as 
communication standards become available. As presented in 
[4], the integration of systems is challenging and must be 
conducted by considering the integrating technology, the 
architecture, semantics, and user. Systems that have not been 
integrated efficiently lead to configurations that underutilize the 
capabilities, poor testing results of the prototype (adequate and 
long-term testing requirements due to problems or failures), and 
potential early system failure [5].  
While systems integration is discussed in various 
publications with varying focus on PES, discussion of PES 
integration with a generation or load resource system in a 
general architecture has been limited. PES design with 
electrical, thermal, and mechanical considerations and how 
these considerations are interconnected are discussed in [6]. 
Closed loop PES controls for different renewable systems are 
discussed in [7]. Architectures for the integration options for 
AC and DC networks and PES are discussed in [8]. Finally, 
integration of PES into the electric grid and necessary functions 
are presented in [9]. The work presented in these publications 
are directed to solve key single layers of systems integration, 
however, a holistic view of the broader implementation 
challenges (integration of multiple vendor systems into a 
common framework efficiently) is not presented. Integration 
across multiple technologies and vendors is presented as a key 
challenge for this decade in [10]. 
As shown in Fig. 1, the integration of PES and resources to 
construct a DER can be performed through a multiple vendor 
‘black-box’ integration effort [11]-[12]. The ‘black-box’ 
designation signifies that only the interface information is 
disclosed. The traditional approach is for a vendor to develop 
all the integrated solution for the technology for a single 
product concept with the focus on a specific PES topology.  
This works proposes to address DER systems integration 
challenges (considering multiple vendors) through the 
utilization of a collection of agents that represent a novel 
approach to systems. The concept of applying agent-based to 
solve electric power system problems has been widely reported 
in literature. For example, use of agent systems in distribution 
networks for improvement of electric grid resiliency, state 
estimation, and for resource management has been shown [13]-
[24].  In microgrids, agents have been used for optimization and 
general integrated system bidding as means to manage energy 
[25]-[31]. For DERs, agent systems have also been developed 
to represent full resource systems such as in the case of ES, RE, 
and load control [32]-[37]. Agent systems have also been 
developed for interlinking multiple power electronic converter 
systems in parallel [38]-[44]. However, integration of DERs 
with power electronic systems has not been addressed.  
The proposed agent framework provides flexibility and 
opportunities to try new topologies without changing the full 
system architecture speeding up development and testing of 
new concepts. Utilizing the general architecture as presented in 
Fig. 1, layers of systems can be integrated from energy storage, 
M. Starke, Senior Member, IEEE, B. Xiao, Member, IEEE, P. Bhowmik, Member, IEEE, S. Campbell, 
Member, IEEE, M. Chinthavali, Senior Member, IEEE,  B. Dean, Member, IEEE, R.S. K. Moorthy, Member, 
IEEE, M. Smith, Member, IEEE, A. Thapa, Member, IEEE 
Notice: This manuscript has been authored by UT-Battelle, LLC under Contract No. DE-AC05-00OR22725 with the U.S. Department of Energy. The United States 
Government retains and the publisher, by accepting the article for publication, acknowledges that the United States Government retains a non-exclusive, paid-up, 
irrevocable, world-wide license to publish or reproduce the published form of this manuscript, or allow others to do so, for United States Government purposes. The 
Department of Energy will provide public access to these results of federally sponsored research in accordance with the DOE Public Access Plan 
(http://energy.gov/downloads/doe-public-access-plan). 


---

Page 2

---

renewables, and loads seamlessly into full systems such as 
microgrids or distribution management systems. The proposed 
agent system supports full integrated technology capabilities 
including integrated safety, plug-and-play capability, unit 
commissioning and operation, and DER peer-to-peer 
coordination.  
 
This paper is organized as follows: Section II provides a 
general background on the proposed hierarchal architecture for 
the various systems that construct a DER, Section III presents 
the proposed agent integration strategy, Section IV provides a 
system example of an AC implementation, Section V provides 
validation of the full system working on a CHIL platform, and 
Section VI ends the paper with the Conclusion.  
II.  PROPOSED DISTRIBUTED ENERGY RESOURCE 
ARCHITECTURE APPLIED IN THIS WORK 
A DER is a system of systems that links energy resources 
to the electric grid. This integration is usually conducted 
through a power electronic interface that converts and controls 
the output of the DER.  Changing function requirements, 
nomenclature, 
state 
machine 
operations, 
and 
safety 
mechanisms represent only a few of the challenges with 
integrating technologies to construct and control a DER.  
A depiction of a proposed architecture considering the 
hardware and systems integration of a PES, resource, and 
central controller is presented in Fig. 2. In this design, six 
distinct layers are presented: 1) central controller, 2) 
computational node (integration layer via agents), 3) resource 
controller (e.g., a battery management system, solar forecaster), 
4) resource (e.g., batteries, photovoltaic array), 5) converter 
controller, and 6) converter (hardware stack) layer. These layers 
each support different purposes and operate in different timing 
regimes. The converter and converter controller collect data and 
perform closed loop control in spans of microseconds to 
milliseconds while at the central controller, resource 
optimization is on the order of minutes. Details on these 
subsystems that pertain to the agent system are described in the 
next subsections.  
 
A. Converter and Converter Controller 
A power electronic system (PES) is a self-contained, 
collection of hardware and software that converts current and 
voltage from one form to another (AC or DC). A conventional 
PES includes the following hardware systems: a power stack - 
power electronic switching modules/devices and associated 
gate drive circuitry; filter - power conditioning and 
electromagnetic interference (EMI) systems that reduce 
electrical noise; protection devices – provide automatic 
isolation of system components; sensors – used for collecting 
measurement data; and controllers - embedded software on 
digital signal processors (DSPs) or field programmable gate 
arrays (FPGAs) (Converter Controller). These systems as 
integrated into a PES are shown in Fig. 3. 
In this work, the converter controller supports three core 
processes to perform the needed functions and communicate 
with the agent system: 1) a state machine (~5ms), 2) 
background loop for communications with the computational 
node (~10ms), and 3) closed loop control (~100us), as shown 
in Fig. 4. The converter controller state machine determines 
allowed operational modes of the converter and limits 
activation of specific functions based on the state. The state 
machine is also responsible for the coordination of the 
protection devices. 
The background loop receives and sends data to the 
computer node (agent system) through a datagram protocol 
(UDP). A plug-and-play solution developed and described in 
[45] has been adopted to integrate the converter system 
automatically. The UDP communication systems developed is 
based on 4-byte messages. The first byte represents the data 
type (01- Configuration Control, 02-Status, 03-Measurements, 
04-Setting, 05-Control, 06-Setpoints), the second byte the 
designation of the information contained such as Mode, and the 
third and fourth bytes the actual data (which could be a number 
representation for the example of Mode). Two communication 
 
Fig.  2.  Data/Signal flow from Converter to Central Controller 
 
 
Fig.  1. Depiction of system integration from DER perspective 


---

Page 3

---

ports are established on both ends for sending and receiving of 
data between computer node (in this case a Raspberry Pi) and 
converter controller. This is all performed over ethernet with a 
dedicated Internet Protocol address (ipaddress) on both the 
computer node and converter controller. The computer node 
and converter controller have a dedicated communication 
connection to provide high bandwidth communications, limit 
vulnerabilities, and ensure plug-and-play capability (ipaddress 
for setup is static and always the same).  
 
Through the UDP communications, the converter controller 
provides unique configuration information regarding the 
converter including converter type (AC/DC, AC/AC, DC/AC, 
or DC/DC), available control modes, and system ratings. While 
this provides a demonstration of one communication approach, 
others such as Modbus or IEC 61850 can be used.   
 
The closed loop control is based on the different modes 
programmed for supporting DER integration. Modes are 
chosen by the integration layer (agent system) based on 
availability as provided by the converter controller, however 
under anormal conditions the modes are overwritten by the 
converter controller based on need (such as the case in a fault). 
A 
control 
interrupt 
service 
routine 
(ISR) 
collects 
measurements, scales the measurements, and confirms no faults 
or limits have been exceeded while also performing closed loop 
control.  
B. Resource and Resource Controller  
In many DER systems, the energy resources (energy 
storage, wind, solar, or variable load) utilize separate 
controllers and system managers for thermal management, 
data collection, and system monitoring and protection. In this 
work, these are recognized as the resource and resource 
controllers. These systems must be coordinated with the PES 
to create a fully integrated system.  
An example of an energy storage system is shown in Fig. 
3. In the presented example, the energy storage system utilizes 
a battery management system (BMS) that controls the various 
subsystems and represents the main communication interface.  
The BMS controls the isolation contactors, measures the cell 
voltages, and currents, enacts cell balancing, and determines 
the operations of the thermal management system. For an 
energy storage system, the BMS represents the resource 
controller and the energy storage medium (in this case the 
batteries) the resource. 
C. Central Controller 
At the other end of the proposed hierarchy, a central 
controller has been developed that is able to coordinate, 
optimize, and graphically represent device performance 
through a data historian. A depiction of the central controller 
architecture is presented in Fig. 5. Since the system has been 
designed to support various integrations of DER systems and 
be plug-and-play, the central controller optimization was 
formulated to consider both AC and DC systems and to identify 
the coupling of the various integrated systems. A state machine 
has also been programmed as part of the central controller to 
orchestrate start-up and shutdowns of the devices within the 
system as needed. Optimization formulations considered in this 
work include utility economic signals, voltage limitations, 
energy storage capacity limitations, and device limits to name a 
few and are performed in each central controller state. These 
formulations are represented in previous work [46]. Linear 
programming optimization methods are used within the central 
controller to perform the functions of energy management.  
A message queuing telemetry transport (MQTT) protocol 
has been employed between the agent system (computer node) 
and central controller to create flexibility and plug-and-play 
type capabilities [45]. MQTT is a lightweight publish/subscribe 
protocol that uses TCP as a transport protocol and TLS/SSL for 
security and supports Quality of Service (QoS) for delivery of 
messages [47]. MQTT has been evaluated as a communication 
protocol in [48] and is used heavily in many different 
applications. This includes wireless sensors communications 
[49], home automation [50], and microgrids [51] to name a few.  
Using MQTT and approaches such as self-discovery [52], 
each DER can self-identify and register with the central 
controller. This plug-and-play capability enables the integration 
of different single resource assets into a common framework 
without significant configuration. 
 
For historical data capture, all the communication messages 
observed by the MQTT broker are recorded in Structured Query 
Language (SQL).  A utility application programming interface 
 
(a) 
 
(b) 
Fig.  3. Depiction of a) power electronic system and b) battery system 
 
Fig.  4. Converter Controller - DSP loops and functions 
 
Fig.  5. Central controller workflow. 


---

Page 4

---

(API) is used to pull optimization objectives and reference 
signals.  
III.  AGENTS AS APPLIED TO GRID EDGE  
In this work, agents represent the lynchpin of the systems 
integration approach. Agents in this work are responsible for 
safely integrating multiple systems, commissioning and 
operation of a DER, addressing plug-and-play capabilities, 
and providing DER peer-to-peer coordination. Agents 
represent the primary decision-making interfaces to the 
subsystems integrating the PES and resources into a common 
framework for DER coordination through a central controller. 
Features of agents that inherently benefit DER integration 
include [53]: 
▪ 
Agents are social – agents share knowledge as 
requested information to improve performance on 
reaching a goal.  
▪ 
Agents have autonomy - agents can act independently 
and execute based on information received 
▪ 
Agents are proactive – agents use historical information 
and data to predict future actions.  
In the following sections, the agents as applied to PES and 
resource integration is described in detail along with the 
features.  
A.  Core Agent Architecture 
The developed agent framework centers around four core 
agents: 1) a resource agent (represented by a source or load), 2) 
converter agent, 3) interface agent, and 4) intelligence agent as 
shown in Fig. 6 and initially presented conceptually in [54]. 
These set of agents create a standardized configuration to best 
represent the respective integrated technologies needed to 
construct a DER and the use of a facilitator as described in [53]. 
In this framework, only a single agent of each type is needed 
for the computer node.  
The resource agent interfaces with the integrated DER 
resource controller and is either in the form of a load or a source. 
The resource agents that have been developed and readily 
available today include: energy storage, photovoltaic (PV), AC 
and DC load, electric vehicle, and grid to name a few. These 
agents collect and provide information to be used by the central 
controller in terms of forecasts, system configuration, ratings, 
and measurements. These agents and the corresponding 
communication and control capabilities are described in Table 
I.  
The converter agent interacts with the converter controller 
(or DSP) and is able configure according to the data 
communicated by the converter. This information includes the 
converter configuration, ratings, available modes (both on the 
input and output sides of the converter), and any available 
precharge circuity. The facilitator (intelligence agent) is the 
agent that ties the systems into a single representable DER. The 
intelligence agent is responsible for ensuring the core agents are 
present, establishing the type of DER represented by the agents 
and subsystems, ensuring capability between the systems, 
ensuring modes and control options are available, and 
orchestrating system commands into targeted requests to the 
various DER subcomponents. Communication through the core 
agent system is represented in Fig. 7. As shown, the central 
controller obtains the various measurement, configuration, and 
status data and uses this information to determine the optimal 
trajectory for the set of resources based on user specifications 
and utility economic signal.  In the next section, details 
regarding the agent system features developed are presented. 
These features support the rapid deployment and integration of 
DER technologies.  
 
 
B. Core Features offered by DER agent system 
A set of core agent system features have been developed to 
support the integration of PES and resources to construct a DER 
and include integrated safety, unit commissioning and 
operation, plug-and-play capability, and DER peer to peer 
coordination. These are critical to rapid expansion of DER 
systems.  
While the agents represented by DER subcomponents 
(resource, converter, and interface) act primarily as 
communication interfaces to the various interconnected 
technologies, the agents also contain independent state 
machines, system monitoring, and decision making (or 
autonomy and proactive capabilities). Hence, these systems can 
monitor the integrated device data sets and act as another layer 
of verification and safety. The intelligence agent is used to 
combine the resources and verify device compatibility ensuring 
the systems are configured correctly and integrated safely. The 
intelligence agent is also responsible for hosting the DER 
system state machine. 
 
Fig.  6. Agents interactions to systems. 
TABLE I. RESOURCE AGENT DESCRIPTIONS 
Agent 
Purpose 
PV 
Communicates and obtains data regarding PV forecasts 
and measured data and issues electrical isolation 
control requests  
ES 
Communicates with the battery management system 
and obtains data regarding cell voltage, cell 
temperature, pack current, and pack state of charge.  
EV 
Communicates with the EV battery management 
system and obtains data regarding cell voltage, cell 
temperature, pack current, and pack state of charge and 
charging profile 
AC Load, 
DC Load 
Communicates and obtains data regarding load 
forecasts and measured data and issues electrical 
isolation control requests 
Grid 
Communicates and obtains grid configuration and 
measurement data. 


---

Page 5

---

The states represented for the individual agents and DER 
system include commissioning, standby, startup, normal, 
shutdown, faulted, error, and lockout. These states create a 
common framework for the agents independent of the 
interconnected 
resource. 
This 
ensures 
a 
consistent 
nomenclature is used within the agent framework to integrate 
systems independent of vendor-based protocols. Any faulted or 
errored state within an agent immediately results in messaging 
to the other agents to error and enact safety measures in the 
independent systems. 
 Each agent is launched in the commissioning state and upon 
completion of communication initiation and basic system 
parameter collection can transition to a standby state. In this 
state, the agent waits for further instructions from the 
intelligence agent. Fig. 7 shows a flow diagram of the 
intelligence agent decision-making process for DER system 
startup. As shown, the intelligence agent examines the resource 
types, converter type, the overall system type, configuration 
data including AC and DC interconnection, nominal voltage, 
and power ratings, enacts and verifies contactor closings, mode 
and setpoint collection as well as converter activation.  
As shown in Fig. 8, each agent has a core set of capabilities 
that are run in separate threads within a main program. These 
capabilities represent the social, autonomy, and proactive 
nature of the agent. These are run asynchronously and are 
constantly exchanging information with stored variables in 
local memory as global variables. Depending on the need, the 
various functions are either called at different intervals, upon 
receipt of data, or upon request from another function. Hence, 
each agent operates independently, reviewing data from the 
resource, and awaiting instructions from other agents. Since 
these systems are operated as independent entities, watchdogs 
have been added to each agent to ensure intercommunication 
between agents. 
For agent-to-agent communications, the MQTT protocol 
has been chosen. On commissioning, the resource agent, 
converter agent, and interface agent all compile data and 
publish messages on the localhost to the intelligence agent to 
self-identify and to provide information regarding the integrated 
technology. Since, the four core agents are part of the 
standardized framework, the intelligence agent automatically 
begins to orchestrate system processes providing for plug-and-
play configurability. The message topic in the MQTT schema 
is based on the recipient of the message and the type of 
information being shared [52]. Message data types are based on 
those on Fig. 2. (Configuration, Status, Measurements, 
Settings, Control, Setpoints). JavaScript object notation (JSON) 
is used to contain the message payload allowing for simplified 
messaging structure and expansion of the architecture to 
support a growing evolution of system needs.  
As an example, to best illustrate the threading functions of 
the agents (Fig. 8) and communication linkage between the 
agents and devices (Fig. 2), consider a message being sent from 
the converter controller to the central controller. The converter 
agent will receive a UDP message from the converter 
controller on converter status which is saved into local variable 
in the converter agent program. Data is retrieved from this 
variable and used to transmit information through the MQTT 
protocol (local host) to other agents (including the interface 
agent). The interface agent subscribes to the message and 
stores the information into a separate local variable. The 
message is retrieved and transmitted on the communication 
network via the MQTT protocol to the central controller.  
 
 
 
Device coordination has also been enacted in the central 
controller and intelligence agent. A separate set of messages 
have been created to allow one DER system to follow another 
 
Fig. 7. Intelligence Agent Proposed Decision Making for 
Commissioning and Startup 
 
Fig.  8. Single agent threaded functions 


---

Page 6

---

DER systems messages [45]. This provides device 
coordination functions such as PV smoothing and load 
following. The intelligence agent enacts a proportional-
integral calculation to perform the closed loop coordination 
control with the other DER resource. In the next several 
sections, an example of the agent system applied to a single 
use case is provided.  
IV.  EXAMPLE USE CASES FOR PROPOSED AGENT SYSTEMS 
AS APPLIED TO DISTRIBUTED ENERGY SYSTEMS  
In this section, the integration of systems is discussed and 
presented through a detailed examination of a single use case 
(energy storage, PV, and load systems connected by a AC bus). 
As presented in Fig. 9, the integration of the resource, PES, and 
the electrical interconnection to create a DER can be coupled 
in many ways. The proposed agent system can intercouple 
these different configurations without any modifications in 
architecture because of the agent design. This capability is not 
present in existing work. 
 
For this work, a single use case is discussed with 
implementation of a agent-based residential networks system. 
The objective is to demonstrate the ability for this framework 
to support multiple resources, converter topologies, and how 
this system could be applied to real hardware implementations.  
A. Individual Coupled AC Systems (Residential System)  
An example depiction of a grid connected DC home with 
integrated PV and energy storage technologies is presented in 
Fig. 10. The single-phase energy storage system presented in 
this implementation has been fully developed in hardware as 
presented in [55] and shown to be able to be controlled to 
support multiple use cases in [56].  
As shown, in this configuration 380VDC has been 
identified as the DC high bus voltage for a home while a 
separate 12/24 VDC system is available for low power 
devices. The proposed agent system has been incorporated into 
each of the DERs (all single-phase AC/DC systems 
interconnected to a AC system but with different integrated 
resources and control mode needs [56]). These converters 
systems are comprised of a single-phase H-bridge inverter 
supporting a nominal 400Vdc link and 240V AC grid 
connection. The details for the converter system modeled are 
presented in [56].  In this configuration, the dc side has been 
defined by the converter controller as the input and the ac grid 
interconnection as the output. Input signals to the system 
include contactor signals for input and output precharge 
circuits and pulse-width modulation (PWM) signals for 
controlling the semi-conductor switching that come from the 
converter controller (and other supporting circuits not 
discussed). DC and AC voltage and AC current measurements 
are used as the primary measurements for closed loop control.  
 
These systems include grid-connected energy storage 
system, grid-connected PV system, and grid-connected DC 
home converter. The DC home and PV system resource agents 
support forecasting of expected consumption or production of 
the interconnected systems (24-hour at 5- minute resolution.) 
The energy storage resource agent communicates with the 
energy storage resource controller or battery management 
system (BMS) to extract SOC, status, and other information 
regarding the energy storage system. 
The control modes offered by the programmed converter 
controllers for the different resources include: maximum 
power point tracking (MPPT) for maximizing PV output; 
Vdcreg for regulating the DC voltage at the load side; and 
constant P for dispatching real power to charge and discharge 
the energy storage system. These modes are automatically 
adopted through the intelligence agent upon commissioning 
and startup of the system. The modes are also provided to the 
central controller where optimization is performed considering 
the available modes. In this use case, the optimization is 
focused on minimizing home-owner cost as driven by a price 
signal by the utility.  
A. Other Examples 
The agent framework has also been applied to DC 
networks as described in [57] and [58]. These include the 
construction of a multi-chemistry energy storage system 
composed of multiple batteries and a low voltage hub that 
 
Fig.  9. Agent integration flexibility to support multiple system designs 
and DER topologies. 
 
Fig.  10. Agent-based DER System to Support Residential Home  


---

Page 7

---

integrates resources (load, PV, and ES) for commercial 
building applications. This demonstrates the flexibility of the 
agent system to be utilized across multiple platforms. 
V. VALIDATION OF AGENT SYSTEMS VIA CONTROLLER 
HARDWARE IN THE LOOP 
For demonstration, a Typhoon HIL platform has been 
applied to the model the resources, resource controllers, and 
the 
converter 
stacks. 
The 
converter 
controllers 
are 
implemented in a digital signal processor (DSP) and 
programmed to perform the closed loop control modes 
described for the various use cases.  The modelled power 
electronic systems include power electronic switch models, 
filtering, pre-charge and contactor circuitry, and system 
measurements. To provide closed loop control capabilities, the 
measurements from the circuit model are fed to the converter 
controller from analog I/O ports on the Typhoon. Digital 
control signals (switching and contactor control) from the 
converter controller are provided to separate digital I/O ports 
on the Typhoon to interact with the model.  
Resource models already existing in the Typhoon system 
(including energy storage, PV, and load) have been leveraged 
as part of this work. Load profiles for the electrical 
consumption of the loads and solar irradiance have been 
integrated through a Python extension on the Typhoon 
platform. Resource controllers have been modeled in the 
Typhoon system and employ a Modbus communication 
interface for communication with the resource agent. Modbus 
is employed as the resource communication protocol as this 
has been found to be the most readily available communication 
capability constructed within the Typhoon HIL platform. 
The agent systems have been deployed on Raspberry Pi 
3.0 B+ as computational nodes with UDP and MQTT/Modbus 
communications performed through an onboard ethernet and 
USB connection (USB to ethernet adapter). Agents have been 
developed in Python 3.0. 
 Network switches are used to tie the communication 
between the resource, converter controller, computer node, and 
central controller, and Typhoon HIL system. A HP notebook 
computer is used as the central controller supporting Linux.  
Commissioning of the systems begins with the agent 
systems that lie within the computer node. The agents are 
launched consecutively with a batch file and begin 
communicating with the interconnected converter controllers 
and resource controllers (in this case the Typhoon HIL 
simulator) and self-identify with the intelligence agent.  This 
is shown in Fig. 11. The intelligence agent confirms the 
existence of the interface agent, resource (source/load) agent, 
and converter agent. Once the configuration data is obtained 
by the intelligence agent from the other agents, the intelligence 
agent validated configurability and creates a system type. At 
this stage, the system is commissioned and awaiting a ‘startup’ 
request from the central controller.  
Upon startup request from the central controller to start the 
DER (received and sent via the interface agent), the 
intelligence agent reviews the selected control mode and 
enacts 
a 
startup 
sequence. 
The 
intelligence 
agent 
communicates both with the energy storage system (modeled 
in the HIL system) through the resource agent and converter 
controller via the converter agent to coordinate the sequence of 
precharge and contactor settings as shown in Fig. 12.  
 
 
As part of the startup sequence for the systems, the central 
controller identifies the available resources (via the 
intelligence agent designation) and optimizes the startup 
sequence. The optimization has been formulated based on two 
system types: 1) isolated systems and 2) systems connected to 
the grid. For isolated systems, the resources able to inject 
power into the bus are activated first followed by load assets. 
Systems that are grid connected are assumed to have sufficient 
supply and load is activated first. Fig 13 show the data 
collected for startup from the central controller for the energy 
storage system and residential building. In each case, the 
central controller waits for full startup of each resource (which 
could take about 1min for closing contactors, confirming 
voltages, and communicating data) before issuing startup 
command to the next resource. Fig. 14 shows the measured  
currents of the converters within the residential system 
measured from the perspective of the Typhoon system. 
A utility price signal has been added to the central 
controller to provide a reference for the optimization and 
dispatch of the systems [59]. Long-term runs (exceeding 24 
hours) have been conducted and are presented here to 
 
Fig.  11. Depiction of Terminal showing the intelligence agent and 
DER commissioning process. 
 
Fig.  12. Depiction of Terminal showing the intelligence agent and DER 
commissioning process. 


---

Page 8

---

demonstrate the stability of the proposed hierarchy, agent 
system, central controller, computer node, and converter 
controller.  In a 24-hour run, the agent systems will have 
communicated, processed, and responded to thousands of 
messages from the various interfaces. This provides a layer of 
confidence as the agent technology transfers to hardware 
implementation. 
 
 
 
A periodic irradiance and load consumption signal have 
been applied to the PV and DC load within the Typhoon. As 
shown in 15, the PV system tracked the maximum power point 
successfully and produced maximum available power. The DC 
home also consumed power (showed as a negative value) as 
anticipated based on a constantly changing load. The periodic 
price signal incentivized the utilization of the energy storage 
system during peak hours. Fig. 16 presents the real power and 
state of charge (SOC) of the energy storage system as 
dispatched by the central controller. As shown, the energy 
storage system was dispatched to charge (negative power) 
before the 12pm time frame and discharge (positive power) at  
the highest price period at 3pm. This demonstrates that the agent 
systems have 1) integrated multiple types of resources 
 
 
 
(PV, DC load, and energy storage) and PES (single phase 
inverter) into DERs effectively for optimization by a central 
controller, 2) provided AC system DER integration, and 3) 
operated the DER systems reliably. 
VI. CONCLUSION AND FUTURE WORK 
In this work, an agent system is proposed that can integrate 
different power electronic systems and resources into a 
distributed energy resource (DERs).  This system of agents is 
focused on four different core agents that provide the basic 
premise of the agent system: interface agent, intelligence agent, 
converter agent, and resource agent. This paper demonstrates 
that the developed agent works for single converter systems 
interconnected on a AC system but also presents other work 
which applies to DC systems.  
Work is in progress to demonstrate this agent system as 
applied to full hardware systems and communication networks 
and applications. This includes the utilization of a power stack, 
filters, contactors, and other components modeled within the 
CHIL platform.    
VII.  ACKNOWLEDGMENTS 
This work was funded by the U.S. Department of Energy, 
Office of Electricity, Energy Storage Program and Office of 
Energy Efficiency Renewable Energy, Building Technologies 
Program under contract number DE-AC05-00OR22725. 
REFERENCES 
[1] 
M. Yao and X. Cai, "An Overview of the Photovoltaic Industry Status 
and Perspective in China," in IEEE Access, vol. 7, pp. 181051-181060, 
2019. 
[2] 
W. J. Cole, C. Marcy, V. K. Krishnan and R. Margolis, "Utility-scale 
lithium-ion storage cost projections for use in capacity expansion 
models," 2016 North American Power Symposium (NAPS), Denver, 
CO, 2016. 
[3] 
M. Stecca, L. R. Elizondo, T. B. Soeiro, P. Bauer and P. Palensky, "A 
Comprehensive Review of the Integration of Battery Energy Storage 
Systems Into Distribution Networks," in IEEE Open Journal of the 
Industrial Electronics Society, vol. 1, pp. 46-65, 2020. 
[4] 
E. G. Nilsson, E. K. Nordhagen and G. Oftedal, "Aspects of systems 
integration," Systems Integration '90. Proceedings of the First 
International Conference on Systems Integration, 1990, pp. 434-443. 
[5] 
A. C. Silva and G. Loureiro, "System integration issues - Causes, 
consequences & mitigations," 2011 IEEE International Conference on 
Industrial Engineering and Engineering Management, 2011, pp. 1338-
1342. 
[6] 
M. Gerber and J. A. Ferreira, "A System Integration Philosophy for 
Demanding Requirements in Power Electronics," 2007 IEEE Industry 
Applications Annual Meeting, 2007, pp. 1389-1396. 
[7] 
J. M. Carrasco et al., "Power-Electronic Systems for the Grid Integration 
of Renewable Energy Sources: A Survey," in IEEE Transactions on 
Industrial Electronics, vol. 53, no. 4, pp. 1002-1016. 
[8] 
D. Boroyevich, F. Wang, J. D. v. Wyk, F. C. Lee, Q. Liu and R. Burgos, 
"Systems Integration at CPES," 4th International Conference on 
Integrated Power Systems, 2006, pp. 1-6. 
[9] 
B. Kroposki, C. Pink, R. DeBlasio, H. Thomas, M. Simões and P. K. Sen, 
"Benefits of Power Electronic Interfaces for Distributed Energy 
Systems," in IEEE Transactions on Energy Conversion, vol. 25, no. 3, 
pp. 901-908, Sept. 2010. 
[10] I. Batarseh and K. Alluhaybi, "Emerging Opportunities in Distributed 
Power Electronics and Battery Integration: Setting the Stage for an 
Energy Storage Revolution," in IEEE Power Electronics Magazine, vol. 
7, no. 2, pp. 22-32, June 2020. 
[11] L. Arnedo, R. Burgos, D. Boroyevich and F. Wang, "System-Level 
Black-Box Dc-to-Dc Converter Models," 2009 Twenty-Fourth Annual 
 
Fig.  13. System startup for residential system (‘Standby State’-1, 
‘Startup State’-2, and ‘Normal State’ -3 ) 
 
Fig.  14. Screen shot of the observed measurement data in Typhoon HIL  
Fig.  15. DC home and PV power profile 
 
Fig.  16. Energy storage power and state of charge 


---

Page 9

---

IEEE Applied Power Electronics Conference and Exposition, 2009, pp. 
1476-1481. 
[12] V. Valdivia, A. Barrado, A. Lazaro, P. Zumel and C. Raga, "Easy 
Modeling and Identification Procedure for "Black Box" Behavioral 
Models of Power Electronics Converters with Reduced Order Based on 
Transient Response Analysis," 2009 Twenty-Fourth Annual IEEE 
Applied Power Electronics Conference and Exposition, 2009, pp. 318-
324. 
[13] G. Zhabelova, V. Vyatkin and V. Dubinin, "Decision making for 
industrial agents in Smart Grid applications," IECON 2014 - 40th Annual 
Conference of the IEEE Industrial Electronics Society, Dallas, TX, 2014, 
pp. 3584-3590. 
[14] A. Deshmukh et al., "Multi Agent Systems: an Example of Dynamic 
Reconfiguration," 2006 IEEE Instrumentation and Measurement 
Technology Conference Proceedings, Sorrento, 2006, pp. 1172-1177. 
[15] K. Eshghi, B. K. Johnson and C. G. Rieger, "Resilient Agent for Power 
System Operations and Protection," IECON 2018 - 44th Annual 
Conference of the IEEE Industrial Electronics Society, Washington, DC, 
2018, pp. 780-785.  
[16] Y. Liu, Y. Hou, S. Lei, and D. Wang, “A distribution network restoration 
decision support algorithm based on multi-agent system,” Asia-Pacific 
Power Energy Eng. Conf. APPEEC, vol. 2016-December, pp. 33–37, 
2016. 
[17] J. M. Solanki, S. Khushalani and N. N. Schulz, "A Multi-Agent Solution 
to Distribution Systems Restoration," in IEEE Transactions on Power 
Systems, vol. 22, no. 3, pp. 1026-1034, Aug. 2007. 
[18] T. Nagata, Y. Tao, H. Sasaki and H. Fujita, "A multiagent approach to 
distribution system restoration," 2003 IEEE Power Engineering Society 
General Meeting (IEEE Cat. No.03CH37491), Toronto, ON, Canada, 
2003, pp. 655-660 Vol. 2. 
[19] X. Chen, B. Kong, F. Liu, X. Gong and X. Shen, "System Service 
Restoration of Distribution Network Based on Multi-agent Technology," 
2013 Fourth International Conference on Digital Manufacturing & 
Automation, Shinan, China, 2013, pp. 1371-1374. 
[20] K. Anisha, M. Rathinakumar, N. Veerappan and O. K. Satya Prakash, 
"Multi agent based distribution system restoration with distributed 
generation," 2014 IEEE National Conference on Emerging Trends In 
New & Renewable Energy Sources And Energy Management (NCET 
NRES EM), Chennai, India, 2014. 
[21] P. Prabawa and D. Choi, "Multi-Agent Framework for Service 
Restoration in Distribution Systems With Distributed Generators and 
Static/Mobile Energy Storage Systems," in IEEE Access, vol. 8, pp. 
51736-51752, 2020. 
[22] M. J. Ghorbani, M. A. Choudhry and A. Feliachi, "A Multiagent Design 
for Power Distribution Systems Automation," in IEEE Transactions on 
Smart Grid, vol. 7, no. 1, pp. 329-339, Jan. 2016.  
[23] S. M. Shafiul Alam, B. Natarajan and A. Pahwa, "Agent based state 
estimation in smart distribution grid," 2013 IEEE Latin-America 
Conference on Communications, Santiago, Chile, 2013, pp. 1-7. 
[24] I. Ahmad, P. Palensky and W. Gawlik, "Multi-Agent System based 
voltage support by distributed generation in smart distribution network," 
2015 International Symposium on Smart Electric Distribution Systems 
and Technologies (EDST), Vienna, Austria, 2015, pp. 329-334. 
[25] F. I. Hernandez, C. A. Canesin, R. Zamora and A. K. Srivastava, "Active 
power management in multiple microgrids using a multi-agent system 
with JADE," 2014 11th IEEE/IAS International Conference on Industry 
Applications, Juiz de Fora, 2014, pp. 1-8. 
[26] H. S. V. S. K. Nunna and D. Srinivasan, "An agent based energy market 
model for microgrids with Distributed Energy Storage Systems," 2016 
IEEE International Conference on Power Electronics, Drives and Energy 
Systems (PEDES), Trivandrum, 2016, pp. 1-5. 
[27] H. S. V. S. K. Nunna, A. Sesetti, A. K. Rathore, and S. Doolla, 
“Multiagent-Based Energy Trading Platform for Energy Storage 
Systems in Distribution Systems with Interconnected Microgrids,” IEEE 
Trans. Ind. Appl., vol. 56, no. 3, pp. 3207–3217, 2020. 
[28] F. Y. S. Eddy and H. B. Gooi, "Multi-agent system for optimization of 
microgrids," 8th International Conference on Power Electronics - ECCE 
Asia, Jeju, 2011, pp. 2374-2381. 
[29] K. Nunna and D. Srinivasan, “A Multi-Agent System for Energy 
Management in Smart Microgrids with Distributed Energy Storage and 
Demand Response,” IEEE Int. Conf. Power Electron. Drives Energy 
Syst. PEDES 2016, vol. 2016-January, pp. 1–5, 2017. 
[30] M. Meiqin, D. Wei and L. Chang, "Multi-agent based simulation for 
Microgrid energy management," 8th International Conference on Power 
Electronics - ECCE Asia, Jeju, 2011, pp. 1219-1223. 
[31] Z. Jiang, "Agent-Based Control Framework for Distributed Energy 
Resources Microgrids," 2006 IEEE/WIC/ACM International Conference 
on Intelligent Agent Technology, Hong Kong, China, 2006, pp. 646-652.  
[32] M. Starke et al., "Agent-Based System for Transactive Control of Smart 
Residential Neighborhoods," 2019 IEEE Power & Energy Society 
General Meeting (PESGM), 2019, pp. 1-5. 
[33] M. Starke et al., "Real-Time MPC for Residential Building Water Heater 
Systems to Support the Electric Grid," 2020 IEEE Power & Energy 
Society Innovative Smart Grid Technologies Conference (ISGT), 2020, 
pp. 1-5.  
[34] T. Logenthiran, D. Srinivasan and T. Z. Shun, "Multi-Agent System for 
Demand Side Management in smart grid," 2011 IEEE Ninth 
International Conference on Power Electronics and Drive Systems, 
Singapore, 2011, pp. 424-429. 
[35] H. Guo, J. Wu, L. Kong and X. Qiu, "Distributed hybrid wind-PV power 
system based on multi-agent," 2009 3rd International Conference on 
Power Electronics Systems and Applications (PESA), Hong Kong, 2009, 
pp. 1-3. 
[36] Sangsoo Park, Y. Miura, and T. Ise, “A maximum power control scheme 
based on multi-agent system for distributed flexible network 
photovoltaic system,” in 2012 International Conference on Renewable 
Energy Research and Applications (ICRERA), Nov. 2012, pp. 1–6. 
[37] X. Li and D. Zhang, “Coordinated control and energy management 
strategies for hundred megawatt-level battery energy storage stations 
based on multi-agent theory,” Int. Conf. Adv. Mechatron. Syst. 
ICAMechS, vol. 2018-Augus, pp. 152–156, 2018. 
[38] J. Hamar, "Decentralized, agent-based control of low and moderate 
power DC-DC converters," 2009 Brazilian Power Electronics 
Conference, Bonito-Mato Grosso do Sul, 2009, pp. 410-416. 
[39] P. Bartal, J. Hamar and I. Nagy, "Parallel DC/DC converters with multi-
agent based multi-objective optimization for consumer electronics," 
2011 IEEE International Conference on Consumer Electronics -Berlin 
(ICCE-Berlin), Berlin, 2011, pp. 276-280. 
[40] E. Krüger, J. Liu, F. Ponci, and A. Monti, “Optimization of task sharing 
towards multi-agent control of PEBB based power systems,” 2012 IEEE 
PES Innov. Smart Grid Technol. ISGT 2012, pp. 1–7, 2012. 
[41] A. Benigni, H. L. Ginn, A. Lowen, F. Ponci and A. Monti, "An 
embedded solution for multi-agent control of PEBB based power 
electronic systems," 2014 IEEE International Workshop on Intelligent 
Energy Systems (IWIES), San Diego, CA, 2014, pp. 12-17. 
[42] H. L. Ginn, F. Ponci, and A. Monti, “Multi-agent control of PEBB based 
power electronic systems,” 2011 IEEE PES Trondheim PowerTech 
Power Technol. a Sustain. Soc. POWERTECH 2011, pp. 1–6, 2011. 
[43] A. Monti and F. Ponci, “PEBB standardization as key enabler for power 
control flexibility,” IEEE Int. Symp. Ind. Electron., pp. 3695–3699, 
2010. 
[44] A. Monti, R. Liu, A. Deshmukh, F. Ponci and R. Dougal, "Towards a 
new fully-flexible control approach for distributed Power Electronics 
Building Block systems," 2008 34th Annual Conference of IEEE 
Industrial Electronics, Orlando, FL, 2008, pp. 2955-2961. 
[45] M. Starke et al., "A Plug-and-Play Design Suite of Converters for the 
Electric Grid," 2020 IEEE Energy Conversion Congress and Exposition 
(ECCE), 2020, pp. 2314-2321. 
[46] G. Liu, M. Starke, Xiaohu Zhang and K. Tomsovic, "A MILP-based 
distribution optimal power flow model for microgrid operation," 2016 
IEEE Power and Energy Society General Meeting, 2016, pp. 1-5.  
[47] N. Naik, "Choice of effective messaging protocols for IoT systems: 
MQTT, CoAP, AMQP and HTTP," 2017 IEEE International Systems 
Engineering Symposium (ISSE), Vienna, Austria, 2017, pp. 1-7.  
[48] M. Houimli, L. Kahloul and S. Benaoun, "Formal specification, 
verification and evaluation of the MQTT protocol in the Internet of 


---

Page 10

---

Things," 2017 International Conference on Mathematics and 
Information Technology (ICMIT), Adrar, Algeria, 2017, pp. 214-221. 
[49] U. Hunkeler, H. L. Truong and A. Stanford-Clark, "MQTT-S — A 
publish/subscribe protocol for Wireless Sensor Networks," 2008 3rd 
International Conference on Communication Systems Software and 
Middleware and Workshops (COMSWARE '08), Bangalore, India, 
2008.  
[50] Y. Upadhyay, A. Borole and D. Dileepan, "MQTT based secured home 
automation system," 2016 Symposium on Colossal Data Analysis and 
Networking (CDAN), Indore, India, 2016, pp. 1-4. 
[51] A. Vukojevic, S. Laval and J. Handley, "An integrated utility microgrid 
test site ecosystem optimized by an open interoperable distributed 
intelligence platform," 2015 IEEE Power & Energy Society Innovative 
Smart Grid Technologies Conference (ISGT), Washington, DC, USA, 
2015, pp. 1-5.  
[52] Starke, Michael; King, Dan; Herron, Drew, “Implementation of a DDS 
protocol in Microgrid Islanding and Resynchronization with Self-
Discovery”, IEEE Transactions on Smart Grid, September 2017. 
[53] A. Dorri, S. S. Kanhere and R. Jurdak, "Multi-Agent Systems: A 
Survey," in IEEE Access, vol. 6, pp. 28573-28593, 2018 
[54] M. Starke et al., "Agent-Based Framework for Supporting Behind the 
Meter Transactive Power Electronic Systems," 2020 IEEE Power & 
Energy Society Innovative Smart Grid Technologies Conference (ISGT), 
2020, pp. 1-5.  
[55] M. Starke et al., "Residential (Secondary-Use) Energy Storage System 
with Modular Software and Hardware Power Electronic Interfaces," 
2019 IEEE Energy Conversion Congress and Exposition (ECCE), 2019, 
pp. 2445-2451.  
[56] M. Starke et al., "Control and Management of Multiple Converters in a 
Residential Smart Grid," 2021 IEEE Applied Power Electronics 
Conference and Exposition (APEC), 2021, pp. 668-674. 
[57] M. Starke et al., "Secondary Use-Plug-and-Play Energy Storage System 
Composed of Multiple Energy Storage Technologies," 2021 IEEE Power 
& Energy Society Innovative Smart Grid Technologies Conference 
(ISGT), 2021. 
[58] M. Starke, B. Xiao and M. Chinthavali, "A Low Voltage DC Power 
Electronic Hub to Support Buildings," 2021 IEEE Fourth International 
Conference on DC Microgrids (ICDCM), 2021, pp. 1-8. 
[59] Georgia Power, Electric Service Tarriff, Time of Use – General Service 
Demand 
Schedule 
(TOU-GSD-10) 
https://www.georgiapower.com/content/dam/georgia-
power/pdfs/business-pdfs/rates-schedules/small-business/TOU-GSD-
10.pdf 
BIBLIOGRAPHY 
Michael Starke is a Electrical Engineering System 
Integrator at the Oak Ridge National Laboratory. He 
has been at ORNL for over 10 years performing 
research in different areas of optimization, control, 
and communications in power systems. He received 
his B.S, M.S. and Ph.D. in electrical and computer 
engineering at The University of Tennessee in 2004, 
2006, and 2009 respectively. His research interest lie 
in systems integration, optimization, controls, and 
communications. 
 
Bailu Xiao (S’09-M’14) received the B.S. and M.S. 
degrees in electrical engineering from Huazhong 
University of Science and Technology, Wuhan, 
China, in 2006 and 2008, respectively, and the Ph.D. 
degree in electrical engineering from the University 
of Tennessee, Knoxville, TN, USA, in 2014. She is 
currently a R&D staff at Oak Ridge National 
Laboratory (ORNL). Her current areas of interest 
include 
power 
electronics 
system 
integration, 
multilevel converters, and microgrid modeling and control. 
 
Radha Sree Krishna Moorthy received the B. E  in 
electrical and electronics engineering and  Ph.D. in 
electrical and computer engineering from Anna 
University, Chennai, India in 2012 and National 
University of Singapore (NUS), Singapore in 2016 
respectively. Currently she is a R&D Associate Staff 
Member in Oak Ridge National Laboratory (ORNL) 
in Knoxville, Tennessee with research interests 
include wide band gap devices-based power 
electronics and advanced power electronic interfaces for grid and vehicular 
applications.    
 Benjamin R. Dean (S 2018) received the B.S. in 
electrical 
engineering 
from 
the 
University 
of 
Tennessee, Knoxville, Tennessee. He presently is an 
M.S. student in electrical engineering at The University 
of Tennessee. His research interests include power 
electronic system communication and energy storage 
systems. 
 
Anup Thapa received his M.S. and B.S. in Electrical 
Engineering from Clemson University in 2016 and 
Tribhuvan University, Nepal in 2011, respectively. He 
is currently with the group as an R&D Assistant Staff. 
His research interests are power electronics for power 
systems, motor drives, and embedded systems 
programming. 
Mitchell Smith received his Bachelor of Science in 
Physics from Ursinus College in 2012 and PhD in 
electrical engineering at the University of Tennessee in 
2019.  He is presently a post-doctoral research 
associate at Oak Ridge National Laboratory.   Research 
interests include systems design and integration, utility 
scale energy storage, and modular power electronics 
systems. 
 
Pankaj Kumar Bhowmik (S’15-M’19) received the 
B.Tech. degree in Electrical Engineering from 
National Institute of Technology, Silchar, India, in 
2012, M.S. and Ph.D. degree in Electrical and 
Computer Engineering from University of North 
Carolina, Charlotte, USA, in 2015 and 2019 
respectively. He is a Post-Doctoral Research 
Associate at Oak Ridge National Laboratory (ORNL). 
His research interests are utility applications of power electronics and power 
quality issues. 
 
Madhu Chinthavali received his M.S. and Ph.D. 
degrees in electrical engineering from the University 
of Tennessee, Knoxville, TN, USA, in 2003 and 
2015, respectively. He is presently a group leader for 
the power electronics systems integration group and 
also director of Grid Research Integration and 
Deployment Center GRID-C at Oak Ridge National 
Laboratory. Dr. Chinthavali’s research includes 
developing power electronics systems with advance semiconductor devices 
and developing device and system level models.  
 
Steven L. Campbell (M’18) received the A.A.S. 
degree in electrical engineering technology from 
Pellissippi State Community College, Knoxville, TN, 
USA in 2007 and the B.S. degree in electrical 
engineering from The University of Tennessee, 
Knoxville, TN, USA in 2018. Steven is a Technician 
at Oak Ridge National Laboratory. His research 
interest includes the development of power electronics 
for vehicle, grid, and wireless applications from 
packaging at the device level to designing full systems. 
 
 
