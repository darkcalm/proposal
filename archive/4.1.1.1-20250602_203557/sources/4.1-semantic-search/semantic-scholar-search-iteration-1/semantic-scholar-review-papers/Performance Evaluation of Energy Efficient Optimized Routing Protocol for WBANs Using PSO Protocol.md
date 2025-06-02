

---

Page 1

---

International Journal on Recent and Innovation Trends in Computing and Communication 
ISSN: 2321-8169 Volume: 11 Issue: 4s 
DOI: https://doi.org/10.17762/ijritcc.v11i4s.6314 
Article Received: 30 December 2022 Revised: 29 January 2023 Accepted: 05 February 2023 
___________________________________________________________________________________________________________________ 
 
116 
IJRITCC | March 2023, Available @ http://www.ijritcc.org 
Performance Evaluation of Energy Efficient 
Optimized Routing Protocol for WBANs Using PSO 
Protocol 
 
V.C. Diniesh1, L. V. R. Chaitanya Prasad2, R Jennie Bharathi 3,A.Selvarani4, W. Gracy Theresa5, R. Sumathi6, G. 
Dhanalakshmi7 
1Assistant Professor (Sr.G),Department of Electronics and Communication Engineering,Kongu Engineering College, Perundurai, 
Tamil Nadu 638060, India,Email:vcdiniesh@gmail.com 
2Assistant Professor, Department of Electronics and Communication Engineering,Sreenidhi Institute of Science and Technology, 
Hyderabad-501301, Telangana, India.Email:lvrchaitanya@sreenidhi.edu.in 
3Assistant Professor,Department of Electronics and Communication Engineering,,Saveetha Engineering college, Chennai, Tamil Nadu 
602105,India,Email:jenniebharathir@saveetha.ac.in 
4Professor, Department of ECE,Panimalar Engineering college, Poonamallee, Chennai, Tamil Nadu 600123, India, 
Email:selvaraninaac2022@gmail.com 
5Associate Professor, Department of Computer and Science Engineering,Panimalar Engineering College, Chennai, Tamil Nadu 600123, 
India,Email:gracewell02@gmail.com 
6Professor, Department of Electrical and Electronics Engineering,Sri Krishna College of Engineering and Technology Kuniyamuthur, Tamil 
Nadu 641008,India,Email:sumathir@skcet.ac.in 
7Professor,Department of Department of Electronics and Communication Engineering, Siddhartha Institute of Technology and Sciences, 
Hyderabad-500088, Telangana,Email: dhanarjun@gmail.com 
 
Abstract—A Wireless Body Area Network (WBAN) is a network that may be worn on the human body or implanted in the human body to 
transmit data, audio, and video in real-time to assess how vital organs are performing. A WBAN may be either an inter-WBAN or an intra-
WBAN network. Intra-WBAN communication occurs when the various body sensors can share information. This is known as inter-WBAN 
communication, which occurs when two or more WBANs can exchange data with one another. One difficulty involves getting data traffic from 
wireless sensor nodes to the gateway with as little wasted energy, dropped packets, and downtime as possible. In this paper, the WBAN 
protocols have been compared with WBAN under Particle Swarm Optimization (PSO), and the performance of various parameters has been 
analysed for different simulation areas. The WBAN under the PSO protocol reduces the energy consumption by 43.2% against the SIMPLE 
protocoldue to the effective selection of forwarding nodes based on PSO optimization. In addition to that the experimental WBAN testbed is 
conducted in indoor environment to study the performance of the routing metrics towards energy and packet reception.. 
Keywords- WBAN, Energy Efficiency, Routing Protocol, Intra-WBAN communication, PSO, Throughput 
 
 
I. INTRODUCTION 
Wireless technology has advanced so that information can 
be sent quickly between devices, independent of their physical 
location. Wearable, implantable, or subdermal sensors and 
controllers can communicate with one another over a Wireless 
Body Area Network (WBAN). Data transmission between the 
network's nodes can be conducted wirelessly, and the network 
can cover all or a portion of the body. Researchers in sectors as 
disparate as mobile health monitoring, health care, medicine, 
and various media, are exploring promising new applications 
for a WBAN [1]. Everyone takes advantage of the mobility a 
WBAN provides. Wireless body area networks can be used in 
the medical profession to monitor a patient's vital signs, 
including Heart rate, blood pressure (BP), Respiration, 
Temperature, electrocardiogram (ECG), and more. The good 
news is that the patient can stand up, walk around the room, 
and even go home for a short while [2]. The patient's condition 
improves while costs are reduced for the healthcare facility. 
Collecting data on a patient over a longer time frame and in 
their natural environments may provide more valuable insights, 
leading to a quicker and more accurate diagnosis. 
WBAN was explicitly developed for use in medical and 
urgent care environments. The network's little wireless sensor 
nodes collect data from the human body and relay it to the 
hospital's medical server. A physician or doctor at the hospital 
looks at the data and decides. Using physiological 
characteristics (PVs) to identify people can help keep WBAN 
conversations safe [3]. Hence this provides cutting-edge 
medical treatment. Without safeguards, erroneous identification 


---

Page 2

---

International Journal on Recent and Innovation Trends in Computing and Communication 
ISSN: 2321-8169 Volume: 11 Issue: 4s 
DOI: https://doi.org/10.17762/ijritcc.v11i4s.6314 
Article Received: 30 December 2022 Revised: 29 January 2023 Accepted: 05 February 2023 
___________________________________________________________________________________________________________________ 
 
117 
IJRITCC | March 2023, Available @ http://www.ijritcc.org 
will occur, which might have fatal consequences for humans. 
Sensors with short battery lives, dynamic network topologies, 
stringent 
quality-of-service 
requirements, 
varying 
data 
production rates and sizes, and weak transmission power are 
some challenges WBAN technology must overcome. 
 
 
Figure1. WBAN Architecture 
 
In WBAN there are two types of WBANs as shown if 
Figure 1, firstly. Intra-WBANs are private networks built 
around the need to monitor patients' vitals without intruding on 
their daily lives. In WBAN, a large number of wireless sensors 
are dispersed throughout a person to monitor their vitals in real 
time. These sentinel nodes (SNs) record and process data from 
sensors on a person's body and then send it to a base station 
(BS) or a sink. Secondly, Inter-WBAN connects different 
WBANs to networks, such as the Internet and cellular 
networks. This communication happens when two or more 
WBANs talk to each other. The sensor in the intra-network 
communicates with the sink and transmits data to it. The sink 
will be connected to the other WBANs on the inter-network 
[4]. The data is transmitted to the Internet through different 
WBANs and will be destinated to the specific emergency 
locations. In addition to that the MAC [5] layer based 
approaches is considered for improving QOS (i.e) to reduce 
energy with minimum wakeup interval forwarding data packets 
with network or routing approaches makes better network life 
time.  
The detail of the paper is structured as follows: In section 2 
the recent existing WBAN routing protocols are discussed with 
respect to metrics, setback. The detailed working of proposed 
WBAN routing with optimization mechanism is discussedin 
section 3. The performance evaluation of both simulation and 
real-time testbed is presented in section 4, and finally the 
conclusion and future work is presented in section 5 
II. RELATED WORKS 
In [6], Haseeb Ur Rahman et al., stated that enhancing 
network efficiency in WBANs using dual forwarder selection 
technique and new method called the Dual Forwarder Selection 
Technique (DFST). DFST has been designed to boost the 
stability of the network and throughput and make it last longer 
by using less Energy. The DFST behaves by aggregating sensor 
nodes on a human body, on another hand a fitness function has 
chosen both next hop or forwarder nodes to send packets to the 
base station. The effectiveness of the proposed work in terms of 
throughput, and network stability has been judged using 
simulation results. Most of the WBANs have three levels of 
architecture. The first level is called "intra," the second level is 
"inter," and the third level is called "extra" or "outer" BAN. In 
this paper, a new energy-efficient algorithm is made to choose 
the best forwarder node (FN) based on DFST instead of only 
single FN selection in WBANs. The wireless sensor nodes are 
classified as either as Group A or B nodes, and different FN is 
chosen among the sensor nodes in each cluster group. Security 
techniques can also be studied in WBANs because they are so 
important; most of the time, human lives depend on them. 
 In [7], M.Ambigavathi et al.,stated that the Energy efficient 
and load-balanced priority queue algorithm for WBANs to 
show better throughput, PDR, latency, and energy consumption 
than conventional approaches. MAC protocols use different 
standards like IEEE 802.11 (WLAN) and IEEE 802.15.4 
(Zigbee stack) to send data, but they limit data rate, end up 
wasting Energy, aren't suitable for busty traffic, and take too 
long. This paper describes a new algorithm called the Energy 
Efficient and Load Balanced Priority Queue Algorithm 
(ELBPQA) that uses the IEEE 802.15.6 standard to send 
crucial data with as little delay as possible. The Two-Round 
Reservation Medium Access Control (MAC) protocol was 
developed to separate sensor data into bursts and periodic data. 
There are four separate queue types: high-priority lines, 
medium-priority lines, low-priority lines, and normal-priority 
lines. This indicates that the results of the analysis show a 
significant improvement in network throughput, packet 
delivery rate, energy efficiency, and latency. This will make it 
simpler to send sensitive data without worrying about it being 
intercepted. 
In [8], HojjatollahEsmaeili et al., stated that A multi-
objective function such as distance, energy, route loss, and the 
evolutionary-based 
multi-hop 
routing 
protocol 
presents 
expected energy consumption for WBANs for selecting 
forwarder nodes. They proposed the flexible Evolutionary 
Multi-hop Routing Protocol (EMRP) to solve these problems. 
According to the IEEE 802.15.6 standard draught, WBANs can 
only send data in one hop (directly) or two hops (through a 
forwarder node). The genetic algorithm can be used to adapt 
how EMRP is tuned (GA). WBANs are like MANETs in that 
nodes can move around. A Thermal Aware Routing Algorithm 
(TARA) is one-way data packets are sent away from hot spots. 
Energy-efficient Power-and Thermal-Aware (EPTA) is a 
protocol that decidebased on an objective function for routing 
towards residual energy, temperature, and power received from 
one hop neighbors. The simulation results show that the new 


---

Page 3

---

International Journal on Recent and Innovation Trends in Computing and Communication 
ISSN: 2321-8169 Volume: 11 Issue: 4s 
DOI: https://doi.org/10.17762/ijritcc.v11i4s.6314 
Article Received: 30 December 2022 Revised: 29 January 2023 Accepted: 05 February 2023 
___________________________________________________________________________________________________________________ 
 
118 
IJRITCC | March 2023, Available @ http://www.ijritcc.org 
technology is much more reliable than the current ones 
concerning throughput, lifetime, path loss, and energy usage. 
       In [9], Nadeem Javaid et al., stated that the enhanced 
maximum throughput multi-hop link efficient routing protocol 
for WBANs to minimize the energy consumption of the 
network utilizes a multi-hop mode of communication In 
contrast to wireless sensor networks (WSNs), WBANs often 
use star topology as their architecture. In this topology, an 
access point (AP) is placed at the centre of the body to get data 
information from sender nodes up to 1.5 m away. The M-
ATTEMPT (thermally aware) routing protocol adopts multi-
hopping to send data from sensor nodes to the sink. CICADA 
uses the TDMA scheme to plan when nodes will send data. To 
handle both normal and life-critical traffic, the priority-
guaranteed medium access control (PMAC) protocol was 
created. PMAC utilizes 2 contention access periods and one 
contention-free period to send a large number of data packets. 
The simulation output shows that iM-SIMPLE performs better 
than current protocols for increasing the network's throughput 
and period of stability.  
       In [10], N. Javaid et al., stated the New Energy-
Efficient Routing Protocol for WBANs. A prototype has been 
made for using different kinds of sensors placed on the human 
body. While multi-hop communication is exemplary for 
transferring huge amounts of data, it cannot be used for real-
time traffic (critical data) or on-demand data transmission. The 
suggested routing strategy prioritized thermal efficiency during 
its development. Data packets may be diverted to avoid the 
"hot spot" on the connection using this feature. Given that node 
in WBASNs can be located anywhere on the human body, 
much forethought is essential before deployment. It can be 
fixed by moving the nodes with the slowest data rates closer to 
the sink. All other processes must cease while data is sent to a 
sink node. All of the embedded nodes can communicate with 
the central hub in the case of an emergency. The low-
throughput sensors will send data once the most crucial data 
has been delivered, thanks to a prioritization system. The 
outcomes prove that the suggested routing approach is more 
effective and reliable than multi-hop communication. 
In[11],  Q. Nadeem et.al., stated that the Stable Increased-
throughput Multi-hop Protocol for Link Efficiency in WBANs 
use multi-hop fashion to achieve less power consumption and 
increase in network lifetime. It suggests utilizing a fitness 
function to select a forwarder or parent node. The 
recommended cost function chooses a parent node that is near 
the sink and has a high residual energy. While the distance 
parameter assures successful packet reception to the sink, the 
residual energy parameter maintains the balance energy 
consumption among the neighbouring sensor nodes. WBAN 
sensor nodes only need a little power. The transfer of data from 
sensor nodes to sinks uses the least amount of power. The need 
to recharge the batteries is one of WBAN's main challenges. To 
solve the battery charging issue, an effective routing strategy is 
required. An efficient, stable, and high-throughput routing 
approach for WBAN. Set up sensor nodes on the body in the 
predetermined locations. The SIMPLE protocol increases node 
longevity while maximizing network stability. It's essential to 
give the sink more packets over a longer period of time in order 
to maintain patient monitoring. 
From the existing study we noticed that the researchers 
predominantly employ on improving packet reception, network 
lifetime and minimum energy consumption. For smaller 
WBANs, this is trivial, but larger networks require deep review 
on choosing the nodes to forward to reach sink under multi-
hop. Hence in this paper we place our work under two fold 
approaches: First, the selection of node is based on PSO 
optimization and secondly based on the fitness function with 
respect to routing metric. Hence the proposed WBAN in 
optimization leads to best selection of forwarded node makes 
an increase in network lifetime, minimum energy consumption 
under smaller and larger WBANs. 
III. PSO OPTIMIZATION USED IN WBAN MECHANISM  
Forwarding a large number of packets in a network can 
result in network congestion and performance degradation. In 
order to determine the correct and best path and enhance 
network performance, optimization techniques are used. 
A. 
Particle Swarm Optimization (PSO) 
First, Particle swarm optimization assigns positions, 
velocities, and fitness values to each individual particles or 
nodes. It has two equations namely velocity and position. These 
equations are used to discover the maximum or minimum of a 
function based on requirement. The fitness function is 
calculated based on these two equations. Every particle records 
its best fitness position and best fitness velocity. It is called as 
personal best or pbest. A record of the position and value of the 
global best or gbest fitness is also kept [12-13]. 
The velocity of kth particle for the gbest PSO is determined 
by the formula as given in equation (1), 
 



)
(
)
(
)
(
)
(
)
(
2
2
1
1
)
1
(
k
x
p
r
c
k
x
k
p
r
c
k
v
k
w
v
g
b
k
−
+
−
+
=
+
         (1) 
 
PSO defines two positions, referred known as the personal best 
position and the global best position, to update the velocities 
and direct the swarm. The position of kth particle is given by 
equation (2), 
                         
)1
(
)
(
)
1
(
+
+
=
+
k
v
k
X
X k
                   (2) 
where ‘k’ is the iteration number, r1, r2 are random numbers 
between 0 and 1, ѡ(k) is the inertia weight, c1, c2 are 
correction factors, x(k), v(k) are position and velocity at kth 


---

Page 4

---

International Journal on Recent and Innovation Trends in Computing and Communication 
ISSN: 2321-8169 Volume: 11 Issue: 4s 
DOI: https://doi.org/10.17762/ijritcc.v11i4s.6314 
Article Received: 30 December 2022 Revised: 29 January 2023 Accepted: 05 February 2023 
___________________________________________________________________________________________________________________ 
 
119 
IJRITCC | March 2023, Available @ http://www.ijritcc.org 
iteration, P(k)b is the pbest position at kth iteration, Pg is the gbest 
position. 
 
 
Figure 2 Flowchart of protocol 
In Figure 2, the sensors nodes are deployed in various position 
in a human body with a position respect to sink. The nodes are 
considered as particles and their position and velocity are 
initialized respectively. The values of sensor node position and 
velocity are updated based on the evaluated fitness function. 
The current values of velocity and position is compared to the 
previous values and updated. The iterations will continue until 
the best forwarder nodes are found. In Algorithm 1, identifies 
the best forwarded node in WBAN networks. Line 1, 2 
represent the parameter initialization and Line 4-7 represent the 
deployment of nodes based on distance (d). Line 8-18 
calculation of fitness function is done and the solution is 
classified as best and worst, based on the best solution the 
position of nodes will be updated 
 
 
B. 
Selection of forwarder node 
After selection of best particles obtained from equation 1 
and 2, we need to choose the best forwarded node under 
multihop. In order to select here we adopt the cost function 
based on distance, energy and position. The following equation 
is given as. 
                                
n
n
E
d
n
cf

=
)
(
                               (3) 
Where d represent distance and e represents energy and α is 
a tuning parameter and value ranges between 0 to 1 and 
selection is based on different application in WBANs. 
 
IV. SIMULATION AND TESTBED ENVIRONMENT 
This subsection aims to compare the performance of 
existing WBAN routing protocols along with PSO optimization 
with several biomedical devices implant on human body under 
multi-hop fashion. Here we have considered two following 
scenarios to represent WBAN environments: 
• 
Scenario I: WBAN along with different numbers of 
biomedical devices connected to asink node in a star 
topology under simulation. 
• 
Scenario II: WBAN topology under real time testbed 
static sensors. 
A. 
 Testbed environment 
In this section, we evaluated the performance of packet 
delivery ration and energy consumption achieved through real-
time testbed environment for the WBAN topology. The 
testbed environment conducted on sensor motes (JN 5168) 
based on IEEE 802.15.4 Zigbee standard at 2.4GHz [14]. Here 
we deploy the sensor motes placed as like human body 
postures on the floor inside our Vinton Network Laboratory 
under multi-hop fashion. 
 
 
(a) Representationof sensors and sink 
(b) Laboratory testbed environment 


---

Page 5

---

International Journal on Recent and Innovation Trends in Computing and Communication 
ISSN: 2321-8169 Volume: 11 Issue: 4s 
DOI: https://doi.org/10.17762/ijritcc.v11i4s.6314 
Article Received: 30 December 2022 Revised: 29 January 2023 Accepted: 05 February 2023 
___________________________________________________________________________________________________________________ 
 
120 
IJRITCC | March 2023, Available @ http://www.ijritcc.org 
 
(c) Sink mote login window data collection 
Figure4 Experimental WBAN sensor postures 
 
In this experiment we considered 7 nodes (6 coordinators and 1 
sink) as shown in Figure 4a. In figure 4b, the sensors nodes are 
placed in a respective manners assuming human body posture. 
In figure 4c, the data from the sensor nodes are collected and 
sent to the base station 
 
 
 
(a) Offered load vs PDR 
(b) Offered load vs Energy  Consumption 
Figure 5 Testbed environment results 
The realize testbed results as shown in Figure 5. When a traffic 
load is also there is a better performance at 1 packet per second 
(pps) and it attain 89% packet reception and at long traffic load 
it attain 91% PDR. Here there is a decrease in medium traffic 
with unstable fluctuation due to abrupt traffic leads to drop in 
packets. On other hand sensor node power consumption 
depends on radio modules such as transmitted power, Receiver 
power, CPU and it is calculated based on the following 
equation 
 
gy
sidualener
Re
=
rgy
currentene
rgy
Initialene
                   (4) 
 
Where initial and current energy value is the actual energy of 
the mote and the obtained results demonstrate the packets are 
transmitted to Base station with a variable traffic load of 1, 2, 5 
packets/seconds (pps). Figure 5 shows the energy consumption 
in WBAN testbed posture and it is found that energy 
consumption was 10.54 mW, 9.44 mW and 9.21 mW for 1pps, 
2pps and 5pps traffic load. Alternatively, main basic objective 
of WBAN network is packet reception from pan coordinator 
(sender) to coordinator (receiver). Figure 5 shows the PDR in 
WBAN testbed and it found that 2.12%, 10.84% increase 
against 1pps and 2pps. The reason is proper choosing of 
forwarded leads to balanced packet reception at high traffic 
load. 
B. 
Simulation environment 
In this section, we compare WBAN-PSO optimization with 
existing SIMPLE WBAN routing protocol in-terms of selected 
routing metrics such as network lifetime, PDR and energy 
consumption by using MatLab 2022b simulator. Here we have 
taken eight sensors position as (xi, yi) coordinates inside the 
human body, and destination or sink node kept centre of 
position in a network environment. Here we consider areas 
(500 x 500) m and (1000 x 1000) m, initial distance d◦ is 0.1 m, 
threshold energy (Eth) value is 0.4Junder simulation 
environment under multihop. 
 
 
(a) No of nodes vs Average Energy 
Consumption(500x500) 
(b) No of nodes vs Average Energy 
Consumption(1000x1000) 
 
 
(c) Protocols Vs Throughput 
(500x500) 
(d) Protocols Vs Throughput 
(1000x1000) 
Figure 6 Simulation Results on WBAN 
 
In figure 6, the average energy consumption of nodes with 
respect to number of nodes. It is noted from the graph that the 
protocol with an optimizer outperforms the other protocols 
without any optimizing techniques. The WBAN under PSO 
protocol reduces the energy consumption by 41.1% against 
SIMPLE protocoldue to effective selection of forwarding nodes 
due optimizing technique. Also, the throughputs of three 
different protocols are plotted and it shows the increase in 
throughput with the implementation of optimizing technique in 
both simulation areas. In different simulation area also, the 
protocol with optimizer outperforms the other protocols 
without any optimizer 


---

Page 6

---

International Journal on Recent and Innovation Trends in Computing and Communication 
ISSN: 2321-8169 Volume: 11 Issue: 4s 
DOI: https://doi.org/10.17762/ijritcc.v11i4s.6314 
Article Received: 30 December 2022 Revised: 29 January 2023 Accepted: 05 February 2023 
___________________________________________________________________________________________________________________ 
 
121 
IJRITCC | March 2023, Available @ http://www.ijritcc.org 
 
 
(a)No of rounds Vs Lifetime (500 
x 500) 
(b)No of rounds Vs Lifetime (1000 x 
1000) 
Figure7 Variation of rounds Vs Lifetime 
 
      In Figure 7, the lifetime and Time taken of every nodes has 
been analysed with respect to number of rounds. The results 
proving that the lifetime of nodes are constantly increasing as 
numbers of rounds are increasing. Also, the time taken for 
nodes to reach the destination is reducing. This proves that PSO 
is a better optimizing technique when considering the lifetime 
of the nodes in various simulation areas 
CONCLUSION 
In this Paper, a WBAN protocol with an optimizing 
technique is analysed and has been compared with other 
WBAN protocols. The benefits of using an optimization is 
increase in efficiency in terms of energy as well as lifetime in 
addition to that proper selection of best forwards node selection 
leads to better performance under large WBAN network. Here 
we carried out the performance evaluation both in simulation 
and real-time testbed. The simulation results confirm that a 
protocol with an optimization has performed better in terms of 
throughput and average energy consumption. Furthermore the 
energy and packet reception is demonstrated under indoor 
environment with WBAN human posture.  
However the proposed WBAN is considered only for static 
environment. Hence in future dynamic or mobility based 
environment place an important role as the patient’s moves 
once place to other. Hence the design of routing protocol with 
proper selection forwarded node is challenging task under body 
movement. A novel design will be required in the future to 
address problems towards dynamic environment for indoor and 
outdoor under multi-hop for large scale WBANs. 
REFERENCES 
[1] 
Khan, Rahat Ali, Khalid Hussain Mohammadani, Azhar Ali 
Soomro, Jawad Hussain, Sadia Khan, Tahir Hussain Arain, 
and Hima Zafar. "An energy efficient routing protocol for 
wireless body area sensor networks." Wireless Personal 
Communications 99 (2018): 1443-1454.  
[2] 
Javed, Mohsin, Ghufran Ahmed, Danish Mahmood, Mohsin 
Raza, Kamran Ali, and Masood Ur-Rehman. "TAEO-A 
thermal aware & energy optimized routing protocol for 
wireless body area networks." Sensors 19, no. 15 (2019): 
3275. 
[3] 
Singla, Ripty, Navneet Kaur, Deepika Koundal, Saima 
Anwar Lashari, Surbhi Bhatia, and Mohammad Khalid 
Imam Rahmani. "Optimized energy efficient secure routing 
protocol for wireless body area network." IEEE Access 9 
(2021): 116745-116759. 
[4] 
Tsiflikiotis, Antonios, Sotirios K. Goudos, and George K. 
Karagiannidis. "Hybrid teaching‐learning optimization of 
wireless sensor networks." Transactions on Emerging 
Telecommunications Technologies 28, no. 11 (2017): e3194. 
[5] 
G. Murugesan, V. C. Diniesh, M. J. A. Jude, D. N. S, G. P. 
M and C. R, "Performance Analysis of Medium access 
control protocol for Wireless Body Area Network," 2022 
International Conference on Computer Communication and 
Informatics (ICCCI), Coimbatore, India, 2022, pp. 1-4, doi: 
10.1109/ICCCI54379.2022.9740981. 
[6] 
Rahman, Haseeb Ur, Anwar Ghani, Imran Khan, Naved 
Ahmad, S. Vimal, and Muhammad Bilal. "Improving 
network efficiency in wireless body area networks using 
dual 
forwarder 
selection 
technique." 
Personal 
and 
Ubiquitous Computing (2022): 1-14. 
[7] 
Ambigavathi, M., and D. Sridharan. "Energy efficient and 
load balanced priority queue algorithm for Wireless Body 
Area Network." Future Generation Computer Systems 88 
(2018): 586-593. 
[8] 
Esmaeili, Hojjatollah, and Behrouz MinaeiBidgoli. "EMRP: 
Evolutionary-based multi-hop routing protocol for wireless 
body 
area 
networks." 
AEU-international 
journal 
of 
electronics and communications 93 (2018): 63-74. 
[9] 
Javaid, 
Nadeem, 
Ashfaq 
Ahmad, 
Qaisar 
Nadeem, 
Muhammad Imran, and Noman Haider. "iM-SIMPLE: 
iMproved 
stable 
increased-throughput 
multi-hop 
link 
efficient routing protocol for Wireless Body Area 
Networks." Computers in Human Behavior 51 (2015): 1003-
1011. 
[10] 
Khan, Rahat Ali, Khalid Hussain Mohammadani, Azhar Ali 
Soomro, Jawad Hussain, Sadia Khan, Tahir Hussain Arain, 
and Hima Zafar. "An energy efficient routing protocol for 
wireless body area sensor networks." Wireless Personal 
Communications 99 (2018): 1443-1454. 
[11] 
Nadeem, Qaisar, Nadeem Javaid, Saad Noor Mohammad, 
M. Y. Khan, Sohab Sarfraz, and M. Gull. "Simple: Stable 
increased-throughput multi-hop protocol for link efficiency 
in wireless body area networks." In 2013 eighth international 
conference 
on 
broadband 
and 
wireless 
computing, 
communication and applications, pp. 221-226. IEEE, 2013. 
[12] 
Kennedy, James, and Russell Eberhart. "Particle swarm 
optimization." In Proceedings of ICNN'95-international 
conference on neural networks, vol. 4, pp. 1942-1948. IEEE, 
1995. 
[13] 
Wang, Jin, Yiquan Cao, Bin Li, Hye-jin Kim, and 
Sungyoung Lee. "Particle swarm optimization based 
clustering algorithm with mobile sink for WSNs." Future 
Generation Computer Systems 76 (2017): 452-457. 
[14] 
Online:https://www.nxp.com/products/wireless/zigbee/supp
ort-resources-for-jn516x-mcus:SUPPORT-RESOURCES-
JN516X-MCUS. 
 
