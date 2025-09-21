# Chen2017 Supporting Control Room Operators in Highly Automated Future Power Networks

## Paper Metadata

- **Filename:** Chen2017_Supporting_Control_Room_Operators_in_Highly_Automated_Future_Power_Networks_DOI_10-1049_OAP-CIRED-2017-1107.pdf
- **DOI:** 10.1049/OAP.CIRED.2017.1107
- **Authors:** Not available
- **Year:** Not available
- **Journal/Venue:** Not available
- **URL:** Not available
- **Extraction Date:** 2025-06-03T15:04:11.299505
- **Total Pages:** 6

## Abstract

Abstract not available from BibTeX metadata.

## Keywords

Keywords not available from BibTeX metadata.

---

## Full Text Content



### Page 1

General rights 
Copyright and moral rights for the publications made accessible in the public portal are retained by the authors and/or other copyright 
owners and it is a condition of accessing publications that users recognise and abide by the legal requirements associated with these rights. 
 
 Users may download and print one copy of any publication from the public portal for the purpose of private study or research. 
 You may not further distribute the material or use it for any profit-making activity or commercial gain 
 You may freely distribute the URL identifying the publication in the public portal 
 
If you believe that this document breaches copyright please contact us providing details, and we will remove access to the work immediately 
and investigate your claim. 

Downloaded from orbit.dtu.dk on: Jun 03, 2025
Supporting Control Room Operators in Highly Automated Future Power Networks
Chen, Minjiang; Catterson, Victoria ; Syed, Mazheruddin; MCarthur, Stephen; Burt, Graeme M.; Marinelli,
Mattia; Prostejovsky, Alexander; Heussen, Kai
Published in:
Cired - Open Access Proceedings Journal
Link to article, DOI:
10.1049/oap-cired.2017.1107
Publication date:
2017
Document Version
Peer reviewed version
Link back to DTU Orbit
Citation (APA):
Chen, M., Catterson, V., Syed, M., MCarthur, S., Burt, G. M., Marinelli, M., Prostejovsky, A., & Heussen, K.
(2017). Supporting Control Room Operators in Highly Automated Future Power Networks. Cired - Open Access
Proceedings Journal, 2017(1), 1492-5. https://doi.org/10.1049/oap-cired.2017.1107

---


### Page 2

24th International Conference on Electricity Distribution 
Glasgow, 12-15 June 2017 
 
Paper 1107 

CIRED 2017 
1/5 
SUPPORTING CONTROL ROOM OPERATORS IN 
HIGHLY AUTOMATED FUTURE POWER NETWORKS 

Minjiang CHEN 
University of 
Strathclyde – UK 
minjiang.chen@ 
strath.ac.uk 
 
Graeme BURT 
University of 
Strathclyde – UK 
graeme.burt@ 
strath.ac.uk 
 
Victoria CATTERSON 
University of 
Strathclyde – UK 
v.m.catterson@ 
strath.ac.uk 
 
Mattia MARINELLI 
Technical University of 
Denmark – Denmark 
matm@elektro.dtu.dk 

Mazheruddin SYED 
University of 
Strathclyde – UK 
mazheruddin.syed@ 
strath.ac.uk 
 
Alexander M. 
PROSTEJOVSKY 
Technical University of 
Denmark – Denmark 
alepros@elektro.dtu.dk 
 
Stephen MCARTHUR 
University of 
Strathclyde – UK 
s.mcarthur@ 
strath.ac.uk 
 
Kai HEUSSEN 
Technical University of 
Denmark – Denmark 
kh@elektro.dtu.dk 
 
ABSTRACT 
Operating power systems is an extremely challenging 
task, not least because power systems have become 
highly interconnected, as well as the range of network 
issues that can occur. It is therefore a necessity to 
develop decision support systems and visualisation that 
can effectively support the human operators for decisionmaking in the complex and dynamic environment of 
future highly automated power system. This paper aims 
to investigate the decision support functions associated 
with frequency deviation events for the proposed Web of 
Cells concept. 
INTRODUCTION 
Electric power systems have recently experienced 
unprecedented changes due to the emergence of 
renewable energy resources, such as 
wind and 
photovoltaics, in addition to growing demand. These 
changes have caused an increase in the size and 
operational complexity of modern power systems. It is 
anticipated that in the future, networks will be pushed 
further towards stability limits and power flow 
constraints. As a result, human operators may have 
difficulties in forming a complete and accurate picture of 
the large-scale interconnected power system region they 
are responsible for. Moreover, operators should be 
presented with the data and information that they need to 
understand the current state of the system and be able to 
see projected future behaviours. Therefore, acquiring 
adequate situational awareness (SA) is particularly 
critical in assisting operators to make the right decisions 
and respond effectively during system events. It has been 
shown that several power system blackouts occurred 
because of operator errors due to insufficient SA [1-3]. 
In order to address the problems described above, it is 
very important to develop an advanced decision support 
system (DSS) to incorporate pertinent information and 
knowledge to help human operators make control 
decisions quickly and correctly. The DSS aim is to 
provide SA and, where operator action is required, 
prioritised alternative solutions to a problem by utilising 
decision theory techniques. In addition, the DSS should 
be able to apply the optimal solution if there is no 
response from the human operator within a certain time, 
to ensure that the power system recovers from events. 
There are a variety of DSS applications in the power 
domain that includes demand response [4], fault 
diagnosis of generated alarms [5], power system 
restoration [6], and nuclear power plant operation [7]. 
Visualisation is critical to relay key information to the 
operator to better comprehend a situation and to make 
accurate decisions and faster actions. 
This paper considers one of the future network visions 
called the Web of Cells (Wo C), proposed by the 
ELECTRA (European Liaison on Electricity Committed 
Towards 
long-term 
Research 
Activity) 
Integrated 
Research Programme [8,9]. This vision aims to achieve 
distributed control of autonomous regions within the 
power system, called cells. Hence, the future power 
system is foreseen to drive a move from centralised to a 
more 
distributed 
power 
system. 
Developing 
a 
decentralized 
control 
strategy 
for 
a 
large-scale 
interconnected power system may be preferable since 
there is no requirement for global knowledge of the 
whole power system. Thus, decentralized control may 
offer efficient, reliable and robust solutions. 
The aim of this paper is to explore the functions of the 
DSS associated with decentralized control during 
frequency deviation events under the Wo C architecture. It 
demonstrates 
the 
required 
local 
parameters 
and 
measurements that can assist the human operator to 
resolve incidents by actions taken within the cell, or by 
requesting support from neighbouring cells. 
In this paper, the human operator is intended to mean the 
power engineer with responsibility for online supervision 
of the network, and it does not necessarily imply the 
existence of a physical cell control room. This means that 
the role of the human operator will inevitably change

---


### Page 3

24th International Conference on Electricity Distribution 
Glasgow, 12-15 June 2017 
 
Paper 1107 

CIRED 2017 
2/5 
from their current responsibilities. The human operator is 
responsible for one or more cells, potentially remotely, 
and the DSS assists operators to ensure emergency 
situations can be recovered when the system reaches its 
limits of operation. 
FUTURE DISTRIBUTED POWER SYSTEM 
ARCHITECURE 
The ELECTRA Wo C architecture is one particular view 
of future power systems. A cell is defined as "a group of 
interconnected loads, distributed energy resources and 
storage units within well-defined grid boundaries 
corresponding to a physical portion of the grid and to a 
confined geographical area" [8]. Under this vision, a 
larger network can be divided into several cells. Each cell 
is equipped with a basic set of control functions, and is a 
peer of other cells and there is no hierarchical control 
over cells by a superior entity (i.e. system operator). Peer 
cells will collaborate with each other to allocate 
resources, such as power exchange via tie lines between 
cells. Furthermore, a cell is not limited to a particular 
voltage level, and some cells may span voltage levels. 
With this in mind, there may not be transmission system 
operators and distribution system operators, but simply 
cell operators [9]. Hence, the task of the cell operator is 
to supervise one or more cells and their automatic control 
systems to manage network deviations, such as voltage 
excursions, 
thermal 
constraints, 
and 
frequency 
disturbances. 
WEB 
OF 
CELL 
FREQUENCY 
MANAGEMENT 
This paper aims to investigate frequency events within 
the Wo C architecture. Here, frequency is considered a 
local quantity that is treated independently in order to 
limit control responses from other cells. Automated data 
exchange with the rest of the system ensure that global 
balancing requirements are met. There are three 
automated services to handle the frequency if it deviates 
beyond the operational limits: frequency containment 
control (FCC), balance restoration control (BRC), and 
balance steering control (BSC) [10]. The descriptions of 
each control are explained in the following. 
Frequency Containment Control 
Once a frequency deviation occurs, FCC aims to stop the 
rise or fall of frequency and to contain the frequency to a 
pre-defined value. 
Balance Restoration Control 
After the frequency deviation is contained, BRC aims to 
restore the frequency within set bounds by activating 
local devices and/or exchanging power with other cells. 
Balance Steering Control 
Even although the frequency has been restored within the 
operational limits by BRC, the reserves used at the BRC 
stage are fast acting and may be expensive. BSC aims to 
replace the BRC reserves with the most economical 
resources. 
Two phases of frequency management are considered as 
shown in Figure 1. One is the procurement phase, where 
reserves for FCC and BRC services are procured by an 
algorithm distributed among the cells within the network. 
The implementation of this algorithm is out of scope of 
this paper, which focuses instead on the functions of the 
DSS within the cell. The other is the real-time operation 
phase which executes these three services within the cell 
to solve any frequency deviations. 

Figure 1. Frequency management in the web of cell 
REQUIREMENTS FOR NOVEL DECISION 
SUPPORT 
DURING 
FREQUENCY 
DEVIATIONS 
Based on the automated Wo C frequency management 
described above, the DSS to support operators has 
specific requirements that differ from current network 
management. The human operator should not be required 
to constantly monitor what the system is doing, but 
instead should be alerted to changes in status that may 
eventually lead to problems. However, there should 
always be the option for the operator to see what the 
automation is doing. Information regarding the state of 
the automation should be clearly presented to the human 
operators. 
For frequency management, once a frequency deviation 
occurs, FCC takes control and reports to the DSS that 
frequency containment is operational. If FCC is executed 
automatically as expected, there is no operator action 
required. After frequency is contained, BRC starts to 
restore the frequency and reports to the DSS a forecast of 
when the frequency should return to operational limits. 
Assuming BRC operates correctly, there is again no 
operator action required. 
If and when these automated control systems fail to take 
sufficient action, the human operator must be able to 
resolve 
the 
issue. 
Therefore, 
the 
forecast 
of 
contained/restored frequency must be compared with 
online measurements, in order to highlight any failure to

---


### Page 4

24th International Conference on Electricity Distribution 
Glasgow, 12-15 June 2017 
 
Paper 1107 

CIRED 2017 
3/5 
operate. In such a situation the decision support should 
guide the operator as to what actions are available, and 
their expected outcomes. 
These actions can be 
automatically prioritised, with the best solution applied 
automatically after a given time window. In this way full 
automation is possible, as there are no actions that are 
really necessary from an operator’s point of view. 
However, operators still require tools for re-prioritising 
the options, particularly in unusual circumstances such as 
extreme network events where the operator may have 
pertinent local information. As a result, the DSS can aid 
the operator to process situations and provide the list of 
options for the operator to select. 
DECISION SUPPORT DESIGN 
In order to design the decision support for frequency 
events, there are two frequency scenarios developed here. 
One is the single frequency event within one cell that is 
illustrated in Figure 2, and the other is two frequency 
events in close succession within one cell which is 
depicted in Figure 3. Each frequency scenario has two 
decision points where human intervention may improve 
the outcomes. For each decision point, metrics for 
selecting between alternative actions to resolve the 
decision are determined. It is assumed for each scenario 
that the cell has already procured containment reserves 
and restoration reserves for FCC and BRC during the 
procurement phase. This paper only focuses on the realtime operation phase for each scenario. 

Figure 2. Single frequency event 

Figure 3. Two frequency events in close succession 
Single Frequency Event 
For the single frequency event, it is assumed that the 
frequency deviation can be mitigated by BRC reserves 
previously procured during the procurement phase. 
Hence, 
the 
Wo C 
frequency 
management 
will 
automatically return the frequency within operational 
limits. The intra- and inter-cell messaging required to 
gather situational awareness data of this event was 
discussed in [10], where it was highlighted that the DSS 
of the problem cell will require more detailed information 
than the DSS of the neighbouring cell. Further to this, the 
scenario has two key decision points where only the 
problem cell DSS need be involved. 
Procurement of New BRC Reserves 
After frequency is restored, the cell may need to replenish 
the BRC reserves in case of a future event. The Wo C 
concept includes a periodic planning phase, where 
neighbouring cells can negotiate to provide each other 
with support in case of events during real time operation. 
If this frequency scenario occurs very quickly after the 
previous planning phase, the cell operator may wish to 
procure new reserves to mitigate the further loss of 
generation. 
In this scenario, the DSS aims to decide which reserves 
should be procured for BRC. There are three different 
metrics that need to be considered. First is the time 
remaining until the next planning phase. If there is a very 
short period before the next scheduled planning phase, 
the operator may prefer to take the risk of operating with 
depleted reserves, instead of procuring further reserves 
which could be expensive. The second metric is the 
available reserves within its own cell and neighbouring 
cells, with properties of speed of response, cost, and 
capacity. Some reserves are fast acting (e.g. Hydro) and 
some reserves are slower and possibly cheaper, but a fast 
response is needed to restore the frequency during an 
event. The last metric is that all reserve provision must 
stay within the tie-line operation margin. 
The DSS must trade off these metrics in order to present 
a prioritised list of options for BRC procurement. It may 
be the case that the human operator has specific local 
knowledge that leads them to re-prioritise the options, 
perhaps to preferentially procure only local reserves, or to 
avoid typically fast acting reserves that are temporarily 
responding more slowly. Therefore, the DSS offers 
suggestions rather than imposing a solution. The operator 
may choose to delegate the choice to the DSS, or to 
adjust the list before procurement. A successful outcome 
would be that the operator is satisfied that sufficient 
reserves have been procured if needed for BRC for the 
remainder of this real time operation period. 
BSC Replacement of BRC Deployed Reserves 
As the reserves used at the BRC stage are fast acting and 
therefore expensive, BSC is responsible for replacing 
these reserves with the most economical choices. 
However, the most economical solution is not necessarily 
the best solution. In this case, the DSS aims to replace the 
deployed BRC reserves with economical resources. Thus, 
the metrics applied are available reserves from its own 
cell and neighbouring cells (speed of respond, cost and 
capacity) and tie-line operation margins. A successful 
outcome would be any expensive BRC deployed reserves 
being replaced with cheaper options, and thereby making 
them available for any future imbalance event.

---


### Page 5

24th International Conference on Electricity Distribution 
Glasgow, 12-15 June 2017 
 
Paper 1107 

CIRED 2017 
4/5 
Figure 4. Cell visualization example 
 
Two Frequency Events in Close Succession 
The second scenario involves two frequency events 
occurring in close time proximity within one cell that 
disturb the system balance. It is assumed that the 
combined effect of the events is more significant than the 
BRC reserves can mitigate. As a result, further action 
must be taken to procure emergency support and return 
the frequency within operational limits. As before, the 
intra- and inter-cell messaging which gathers situational 
awareness data of this event was discussed in [10]. 
Response to a Frequency Event Larger than the BRC 
Reserves Can Handle 
The first decision point involves the problem cell 
operator. After the second frequency deviation is 
contained, BRC reserves are deployed. However, the 
frequency does not return within operational limits as the 
planned reserves do not have the required capacity. At 
this point, the problem cell contacts its local devices and 
neighbouring cells to ask how much support can be 
offered to mitigate this emergency situation. 
The DSS aims to restore the frequency within operational 
limits as soon as possible by considering the available 
reserves from its own cell and neighbouring cells (speed 
of respond, cost and capacity) and tie-line operation 
limits. These options are presented to the operator as in 
the previous scenario, with a time-out ensuring that the 
highest priority solution is implemented even in the 
absence of human input. The successful outcome is 
balance being restored to the system. 
Response 
to 
an 
Emergency 
Request 
from 
a 
Neighbouring Cell for BRC Support 
This decision point is complementary to the previous one, 
and considers the scenario for the neighbouring cell. The 
operator of the cell neighbouring the problem cell needs 
to decide how much support can be committed to the 
problem cell. There are four different metrics that need to 
be taken into account. One is the uncommitted reserves. 
If this cell has spare capacity which is uncommitted, it 
should generally be offered to the problem cell. However, 
if this cell has committed reserves, which is the second 
metric, it may decide to offer these reserves to support 
the other cell, depending on how soon the next planning 
phase begins (the third metric). If this real time operation 
phase finishes in 10 minutes, compared to it finishing in 
two hours, it is very low risk to offer committed reserves. 
The last metric is the tie-line operation limit. 
As before, the DSS should trade off these metrics to 
produce alternative plans of how much support from 
which devices to the problem cell. The prioritised list of 
options is presented to the operator, who may delegate 
the choice to the DSS, or select an alternative to the top 
ranked option. A successful outcome would be where 
sufficient reserves are offered to the problem cell without 
compromising this cell’s commitments. 
CELL VISUALIZATION EXAMPLE 
The DSS aims to present a visualization that allows the 
operator to observe the system state at a glance and

---


### Page 6

24th International Conference on Electricity Distribution 
Glasgow, 12-15 June 2017 
 
Paper 1107 

CIRED 2017 
5/5 
enable intuitive situational awareness. Some elements of 
the cell visualisation within the Wo C architecture are 
shown in Figure 4. The frequency deviation is 
highlighted by colour on the right hand side. Graphs on 
the left show the status of frequency and tie-line power 
flow of the cell (only one tie-line interconnected). In 
addition, it is essential to assist the operator with 
projections of the system state into the future. In order to 
do that, a forecast of the planned frequency restoration 
after containment is shown with a starred line in the 
frequency status graph (the time 0 indicates the time now 
and negative time and positive time shows measurements 
and forecast separately). Moreover, it predicts the time 
when frequency will be restored underneath the graph. 
As already mentioned, the human operator needs to be 
able to see which automatic control actions are operating. 
Therefore, check boxes display the status of automated 
control including FCC, BRC, and BSC. If one of the 
automated controllers fails, the operator can manually 
take action to resolve this issue. 
In the top right, there is an indicator to show the available 
reserves within the cell. This is to help the operator to 
make decisions if the cell needs to procure more BRC 
reserves for the remaining time period or not. In order to 
let the operator be aware of what is happening in the 
network, the bottom right shows a network activity log 
which records network information, such as location and 
magnitude of frequency disturbance. 
In the bottom left a decision support box lists options for 
the operator to select. If there is no need for operator 
action, this box remains blank. The DSS also allows 
control actions to be input by the operator, because the 
human operator may know of alternative strategies, or 
may wish to alter the priority of provided options. Hence, 
the operator has a certain window of time in which to 
override the decision support in such a case, after which 
if no response has been received, the DSS automatically 
applies the most optimal solution. 
CONCLUSION 
This paper has explored the functions of DSS within the 
Wo C architecture. Despite increasing automation, human 
operators remain an integral part of modern power 
systems. It is therefore vitally important to provide 
effective and timely DSS during the real-time operation 
of power systems. This paper explores the role of DSS in 
suggesting 
appropriate 
decisions 
within 
different 
frequency scenarios based on key metrics. Based on the 
Wo C architecture, the operator must be able to gain 
situational awareness of the system state, be alerted when 
a decision can be made, and be offered a prioritised list of 
suggested actions along with their expected outcomes. 
With a visualisation of this critical information, the DSS 
can support an effective response of human operators in 
challenging situations. As the next step, an appropriate 
tool, such as constraint satisfaction, optimization 
algorithms and case base reasoning, will be selected to 
design the above DSS. Then, DSS will be implemented 
and tested in the lab. 
Acknowledgments 
The work in this paper has been in part supported by the 
European Commission under the FP7 project ELECTRA 
(grant no: 609687). 
REFERENCES 
[1] 
M. Panteli, D. S. Kirschen, 2015, “Situation 
awareness in power systems: Theory, challenges and 
applications”, Electric Power Systems Research, Volume 
122, pp. 140-151. 
[2] 
UCTE, 2006, Final Report System Disturbance 
on 4 November 2006, Available: https://www.entsoe.eu. 
[3] 
U.S.-Canada Power System Outage Task Force, 
2004, Final Report on the August 14, 2003 Blackout in 
the 
United 
States 
and 
Canada: 
Causes 
and 
Recommendations, Available: http://www.nerc.com. 
[4] 
F. Pedro, and Z. Vale, 2014, "Decision Support 
Concerning Demand Response Programs Design and 
Use-A Conceptual Framework and Simulation Tool", 
Applied Mathematics & Information Sciences, vol.1, 
p.161. 
[5] 
G. M. Burt, J. R. Mc Donald, A. G. King, J. 
Spiller, D. Brooke and R. Samwell, 1994, "A real-time 
decision support system for the operation of a 132 k V 
power network," Control, International Conference on, 
vol.1, pp. 153-158. 
[6] 
A. Stefanov, C. Liu, M. Sforna, M. Eremia and 
R. Balaurescu, 2015, "Decision support for restoration of 
interconnected power systems using tie lines", IET 
Generation, 
Transmission 
& 
Distribution, 
vol.11, 
pp.1006-1018. 
[7] 
S. J. Lee, K. Mo and P. H. Seong, 2007, 
"Development of an integrated decision support system to 
aid the cognitive activities of operators in main control 
rooms of nuclear power plants", In IEEE Symposium on 
Computational Intelligence in Multicriteria Decision 
Making, pp. 146-152. 
[8] 
L. Martini, L. Radaelli, H. Brunner, C. Caerts, 
A. Morch, S. Hanninen and C. Tornelli, 2015, 
“ELECTRA IRP Approach to Voltage and Frequency 
Control for Future Power Systems with High DER 
Penetration”, 
23rd 
International 
Conference 
on 
Electricity Distribution (CIRED). 
[9] 
M. H. Syed, G. M. Burt, J. K. Kok and R. 
D’Hulst, 
2015, 
“Demand 
Side 
Participation 
for 
Frequency 
Containment 
in 
the 
Web 
of 
Cells 
Architecture”, 
International 
Symposium 
on 
Smart 
Electric Distribution Systems and Technologies (EDST). 
[10] 
A. S. Zaher, V. M. Catterson, M. H. Syed, S. D. 
J. Mc Arthur, G. M. Burt, M. Chen, M. Marinelli and A. 
Prostejovsky, 2016, “Enhanced Situational Awareness 
and Decision Support for Operators of Future Distributed 
Power Network Architectures,” in IEEE PES Innovative 
Smart Grid Technologies (ISGT Europe) Conference and 
Exhibition, pp. 1-6.

---
