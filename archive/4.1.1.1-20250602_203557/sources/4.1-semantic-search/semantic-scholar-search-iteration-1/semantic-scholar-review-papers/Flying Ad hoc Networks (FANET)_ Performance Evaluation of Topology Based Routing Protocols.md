

---

Page 1

---

Paper—Flying Ad hoc Networks (FANET): Performance Evaluation of Topology Based Routing Protocols
Flying Ad hoc Networks (FANET): Performance 
Evaluation of Topology Based Routing Protocols
https://doi.org/10.3991/ijim.v16i04.28235
Ali H. Wheeb(*)
Faculty Member – Lecturer, University of Baghdad, Baghdad, Iraq 
a.wheeb@coeng.uobaghdadedu.iq
Abstract—Flying Ad hoc Networks (FANETs) has developed as an inno-
vative technology for accessing places without permanent infrastructure. This 
emerging form of networking is construct of flying nodes known as unmanned 
aerial vehicles (UAVs) that fly at a fast rate of speed, causing frequent changes 
in the network topology and connection failures. As a result, there is no dedi-
cated FANET routing protocol that enables effective communication between 
these devices. The purpose of this paper is to evaluate the performance of the 
category of topology-based routing protocols in the FANET. In a surveillance 
system involving video traffic, four routing protocols with varying routing mech-
anisms were examined. Additionally, simulation experiments were conducted to 
determine the influence of flying altitude. The results indicate that hybrid routing 
protocols outperform other types of protocols in terms of average throughput. 
Proactive protocols, on the other hand, have the least jitter.
Keywords—multi-UAV, flying ad hoc networks, topology-based routing 
protocol, Gauss Markov, flying altitude
1	
Introduction
Unmanned aerial vehicles (UAVs) have made significant advancements and are now 
extensively utilize, whereas wireless data transfer technologies have indeed made sig-
nificant advancements. All of this contributes to the emergency communications system 
types. The Flying Ad-Hoc Network is one of these communication networks (FANET)
[1]. FANET is an autonomous self-organizing network. Its nodes not only link to their 
neighbors, but they also relay traffic via them [2]. Only a subgroup of UAVs may com-
municate with a satellite or ground station and all flying UAVs form an ad-hoc network. 
Thus, in addition to the base station, the UAVs may communicate with one another. 
FANET has several advantages, including adaptability, increased accuracy, economy, 
continuity, Flexibility, and speed [3] [4].
FANETs are becoming more and more popular with each passing day. Previously, 
FANETs are basic remotely controlled airplanes that have been primarily employed in 
military operations [5]. Nevertheless, in recent years, FANETs have been deployed in 
a growing variety of civil and commercial activities, including search and rescue [6], 
package delivery [7], traffic monitoring in smart cities [8], agriculture [9], engineering 
iJIM ‒ Vol. 16, No. 04, 2022
137


---

Page 2

---

Paper—Flying Ad hoc Networks (FANET): Performance Evaluation of Topology Based Routing Protocols
education [10], mobile drone in indoor localization [11] and disaster monitoring [12]. 
The application of FANET is depict in Figure 1.
Fig. 1. Applications of FANET
The degree of mobility of FANET nodes is significantly higher than that of VANET 
or MANET nodes. Because of the high mobility of FANET nodes, the topology of the 
network changes on a more regular basis. FANET has many unique problems, with the 
routing process being one of the most significant design considerations. To function 
properly in FANET, the routing protocols used must be capable of performing an auto-
mated search for the optimum route to offer one or more subjective parameters for the 
operation of data transmission and receiving [13].
The primary goal of this paper is to define FANET as a unique ad hoc network family 
and to assess the effectiveness of topological routing protocols in FANET. This article 
makes three contributions: (i) presenting various routing challenges; (ii) categorizing 
current topology-based routing protocols in FANET; and (iii) comparing and analyz-
ing them using various performance measures. Our comparison study will aid network 
engineers in selecting optimal routing protocols for the FANET deployment scenario.
138
http://www.i-jim.org


---

Page 3

---

Paper—Flying Ad hoc Networks (FANET): Performance Evaluation of Topology Based Routing Protocols
The remainder of the paper is laid out as follows: Section 2 discusses FANET routing 
problems as well as the taxonomy of topology-based routing systems. Describe the 
simulation setup and the mobility model in Section 3. The results of the analysis will 
be provided in section 4, followed by a discussion. The conclusions are in Section 5.
2	
Routing in FANET
2.1	
Challenge of routing protocols in FANET
Routing protocols are in charge of discovering, creating, and maintaining communi-
cation routes between two nodes. The overhead and bandwidth usage of these protocols 
should be kept to a bare minimum. Due to the high mobility of UAVs, network topol-
ogy might vary over time, making route finding and route maintenance one of the most 
important challenges to solve [14]. To enhance routing performance, including better 
QoS and high route setup success ratio, as well as lower energy consumption. There are 
three major issues to overcome [15]:
High network dynamicity. Due to the obvious high mobility of FANETs, the 
extremely dynamic network topology results in low connections between nodes. as a 
result, and network partitions and link disconnections are common, increasing route 
discovery and maintenance and lowering routing performance [15]. To investigate the 
routing process in FANET, many UAV mobility models have been developed [16].
Residual energy. According to the comparably large distance between UAVs, UAVs 
powered by batteries have limited energy (a) to conduct routing processes such as 
route discovery, updates, and maintenance; (b) to provide extended transmission range; 
(c) retransmit various packets when a link failure occurs. UAVs carrying heavier pay-
loads, on the other hand, consume more energy [17].
High resource costs. Frequent route discovery, updates, reestablish routes, and dif-
ferent packet retransmissions in FANETs can result in three categories of resource 
costs: (a) high routing overhead or inefficient bandwidth usage); (b) computational cost 
owing to route processing time; (c) excessive energy consumption. To improve UAV 
connectivity, multi-UAVs can be deployed in many scenarios [18].
2.2	
Topology based routing protocols in FANETs
FANET routing protocols, as shown in Figure 2, can be classified into four groups 
based on the approach used and the challenges that must be overcome. Topology-based 
routing protocols, which are based on link information, use IP addresses to exchange 
packets between interacting nodes. This category includes four types: static, proactive, 
reactive, and hybrid [19]. The following section delves into the topology-based routing 
protocols category and its most important routing protocols.
iJIM ‒ Vol. 16, No. 04, 2022
139


---

Page 4

---

Paper—Flying Ad hoc Networks (FANET): Performance Evaluation of Topology Based Routing Protocols
Fig. 2. Taxonomy of topology based routing protocols in FANET
In static protocols, the information for UAVs is calculated and loaded to each UAV 
first in this type of routing protocol. It is not possible to modify it during the process, 
and the network topology should always be fixed. As a result, the number of communi-
cation lines between UAVs or between the UAV and the ground station is reduce. This 
routing technique does not offer fault tolerance in a dynamic environment if certain 
UAVs fail since they must wait until the mission is over to rectify the issue.
Load Carry and Deliver (LCAD) [20] is a FANET-specific static routing protocol. 
Before UAVs take off, LCAD configures the navigation path on the ground. UAVs are 
thought of as connections between a source and a destination ground control station, 
collecting packets of data, transporting them, and transmitting them to the destination. 
If the UAVs carrying the packets of data are not heading in the proper direction, other 
UAVs might take over and deliver the data packets. Figure 3 illustrates the LCAD 
routing technique in a FANET. It must be noted that no routing table method is used in 
this technique.
140
http://www.i-jim.org


---

Page 5

---

Paper—Flying Ad hoc Networks (FANET): Performance Evaluation of Topology Based Routing Protocols
Fig. 3. LCAD mechanism in FANET
In reactive protocols, the path between nodes is establish when there is a request to 
transmit packets. When a request to transmit packets is receive, a path between nodes 
is construct in reactive protocols. As a result, there is no need to estimate the routes for 
each node regularly. It appears to resolve the overhead issue. There are two different 
kinds of messages in this mechanism: route request and route reply. The key benefit of 
this approach is its bandwidth efficiency. However, it will be delayed due to the time 
required to identify the path [21].
Dynamic Source Routing (DSR) [22] is a reactive routing technology that enables 
a network to self-organize and customize themselves without the use of infrastructure. 
Since DSR is reactive, a discovery procedure is only used when information is transmit-
ted. A route maintenance system is also used to keep track of any path failures. DSR’s 
flexibility of loop characteristics allows users to choose from numerous routes to any 
target node. Because each transmitted packet must include all of the transited nodes’ 
addresses, it is insufficient for large-scale networks and networks. Figure 4 depicts the 
DSR mechanism for FANET.
iJIM ‒ Vol. 16, No. 04, 2022
141


---

Page 6

---

Paper—Flying Ad hoc Networks (FANET): Performance Evaluation of Topology Based Routing Protocols
Fig. 4. DSR mechanism in FANET
In proactive protocols, the table-based routing contains all of the information about 
all nodes within the network, allowing each node to know everything there is to know 
about the others in the network. This approach has one major benefit: each node’s table 
continuously contains the most up-to-date information about another node. However, we 
must keep in mind that this technique requires bandwidth due to the cost of the updated 
messages for the tables. Due to the limited bandwidth available in the FANETs network, 
customized routing protocols can be utilize to modify the topology of the nodes.
Optimized Link State Routing Protocol (OLSR) [23] [24] is a link-state routing pro-
tocol that establishes a global knowledge of all current UAV-to-UAV connections. This 
is accomplish by periodically exchanging Hello and Topology Control (TC) packets 
between the UAVs to update the network’s topology information. OLSR chooses Multi-
Point Relay (MPR) UAVs to cover two-hop neighbors, produce link-state information, 
and relay data packets to other MPRs, lowering overhead. The OLSR mechanism in 
FANET displays in Figure 5.
Fig. 5. OLSR mechanism in FANET
142
http://www.i-jim.org


---

Page 7

---

Paper—Flying Ad hoc Networks (FANET): Performance Evaluation of Topology Based Routing Protocols
Hybrid protocols integrate the reactive and proactive aspects of protocols. It was 
created with the goal of reducing overhead and maximizing bandwidth use. As a result, 
hybrid protocols are appropriate for large-scale networks with many sub-network 
regions, where intra-zone routing employs proactive mechanisms and inter-zone 
routing employs reactive mechanisms. Hybrid protocol adopted in many FANET 
Application [25].
Temporarily Ordered Routing Algorithm (TORA) [26] is a hybrid distributed routing 
technique that performs well in highly dynamic networks such as FANETs. TORA is 
exclusively responsible for updating and maintaining the communication links between 
nearby UAVs. TORA’s major goal is to minimize the number of control packets sent 
during topology changes. TORA constructs and maintains a Directed Acyclic Graph 
(DAG) between communicating UAVs that have several paths. Furthermore, TORA 
frequently chooses longer routes in order to save overhead. To summarize, TORA 
employs both reactive and proactive techniques depending on the network’s state, and 
it discovers alternate routes in the event of connection failures. Figure 6 depicts the 
TORA mechanism in FANET.
Fig. 6. TORA mechanism in FANET
3	
Simulation set up
Due to the high cost of real UAVs and the time and resources required to create a 
realistic FANET environment, the network simulator was used to deploy the UAVs 
and facilitate communication among them. In the simulation challenge, a network 
iJIM ‒ Vol. 16, No. 04, 2022
143


---

Page 8

---

Paper—Flying Ad hoc Networks (FANET): Performance Evaluation of Topology Based Routing Protocols
environment that is as near to the real world as possible must be suggested [27]. In light 
of this, researchers should attempt to build realistic FANETs application situations.
3.1	
Simulation of FANET
A single source UAV node 1, a single base station node 20, and 18 relaying UAV 
nodes make up the FANETs simulation scenario. To match a realistic flight environ-
ment of Surveillance UAVs, the UAVs are deployed and flown autonomously across a 
vast region of 1 Km x 1 Km. The IEEE 802.11 wireless interface is install on each UAV. 
The UAV flies 5 minutes above the ground at a speed of 30 meters per second, using a 
three-dimensional mobility model as illustrated in Figure 7. After establishing a path 
between the UAV and the base station, the UAV begins transmitting a sensing video 
with a packet size of 1024 bytes.
Fig. 7. FANET for surveillance scenario
3.2	
Mobility models 3D
The Gauss-Markov (GM) mobility model [28] is a three-dimensional time-based 
model that uses several parameters to respond to varying amounts of randomness 
and avoid abrupt movement changes. Each movable node is provide a current speed 
and direction, as illustrated in Figure 8. Based on its previous direction and speed, its 
upcoming movement is then update and describe. Consequently, GM can eliminate the 
abrupt pauses and turns seen in Random models. If the right parameters are set, the 
equations system, which relates prior speed and direction to future ones, enables smooth 
updating. GM is used to communicate among UAVs in a variety of applications [29].
144
http://www.i-jim.org


---

Page 9

---

Paper—Flying Ad hoc Networks (FANET): Performance Evaluation of Topology Based Routing Protocols
Fig. 8. Trajectory of UAVs using GM models
3.3	
Performance metrics
The performance of Topology routing protocols analysis and compare based on the 
following metrics.
• Jitter: The jitter of a packet is measured by the average deviation of the change in 
packet interval at the receiver compared to the sender, for a pairing of packets, in a 
flow of packets among a source node and a destination node.
• Average throughput: this metrics represent the total throughput of FANET divide by 
number of traffic flow for UAVs
• Packet Receive rate: is the rate of the successful received packet by the Base station 
to the total transmitted packets by the UAV during the mission.
4	
Results and discussion
Figure 9 demonstrate the jitter results of a 20-UAV node for FANET with the a low 
altitude of 60–150 m and increments of 10 m. When compared to the other protocols, 
the OLSR protocol has the lowest jitter. This is owing to its proactive nature and access 
to the most up-to-date information for all multi-UAV networks. It is also worth noting 
that when the altitude of UAVs increases, the jitter for all routing protocols goes up as 
well. Due to its static nature, LCAD, on the other hand, has the greatest Jitter.
iJIM ‒ Vol. 16, No. 04, 2022
145


---

Page 10

---

Paper—Flying Ad hoc Networks (FANET): Performance Evaluation of Topology Based Routing Protocols
0
50
100
150
200
250
60
70
80
90
100
110
120
130
140
150
Jitter (msec)
Altitude (Meter)
DSR
OLSR
LCAD
TORA
Fig. 9. Jitter comparison
Figure 10 shows a comparison of the average throughput of DSR, OLSR, LCAD, 
and TORA routing protocols. TORA has the best throughput due to its hybrid nature and 
effective bandwidth use, whereas LCAD has poor performance in most UAV altitudes. 
Nevertheless, as the altitude of the UAV increases, the average throughput of all routing 
protocols drops, particularly beyond 80 meters.
0
5
10
15
20
25
30
35
60
70
80
90
100
110
120
130
140
150
Throughput (kbps)
Altitude (Meter)
DSR
OLSR
LCAD
TORA
Fig. 10. Average throughput comparison
Figure 11 depicts the packet successful rate of four routing protocols with low alti-
tude for UAVS. It is observed that TORA and DSR protocols provides high reliability 
for data routing and have highest PSR rate with all UAV Altitudes. Similarly, to other 
performance metrics LCAD show poor performance and drop many packets. OLSR 
protocols PSR decrease as the altitude of UAVs increase.
146
http://www.i-jim.org


---

Page 11

---

Paper—Flying Ad hoc Networks (FANET): Performance Evaluation of Topology Based Routing Protocols
70%
75%
80%
85%
90%
95%
100%
60
70
80
90
100
110
120
130
140
150
PSR(%)
Altitude (Meter)
DSR
OLSR
LCAD
TORA
Fig. 11. Packet successful rate comparison
5	
Conclusion
This research paper investigates the performance of topology-based routing proto-
cols LCAD, DSR, OLSR, and TORA to determine the optimum protocol for surveil-
lance scenarios in Flying Ad hoc Networks. Multiple network metrics, jitter, average 
throughput, and packet successful rate, were used to analyze and compare the four 
protocols. In terms of average throughput and DSR, TORA was determined to be the 
optimal protocol for monitoring scenarios. In terms of overall performance, DSR and 
OLSR are both ranked second. In simulations, it has been observed that TORA and 
OLSR performance sometimes goes synonymously and that OLSR jitter delay is some-
times the shortest.
6	
References
	 [1]	A. Srivastava and J. Prakash, “Future FANET with application and enabling techniques: 
Anatomization and sustainability issues,” Comput. Sci. Rev. Elsevier, vol. 39, p. 100359, 
2021. https://doi.org/10.1016/j.cosrev.2020.100359
	 [2]	A. Chriki, H. Touati, H. Snoussi, and F. Kamoun, “FANET: Communication, mobility 
models and security issues,” Comput. Networks, Elsevier, vol. 163, p. 106877, 2019. https://
doi.org/10.1016/j.comnet.2019.106877
	 [3]	M. A. Khan, I. M. Qureshi, and F. Khanzada, “A hybrid communication scheme for efficient 
and low-cost deployment of future flying ad-hoc network (FANET),” Drones, MDPI, vol. 3, 
no. 1, p. 16, 2019. https://doi.org/10.3390/drones3010016
	 [4]	A. R. Ragab, “A new classification for ad-hoc network,” Int. J. Interact. Mob. Technol., 
vol. 14, no. 14, pp. 214–223, 2020. https://doi.org/10.3991/ijim.v14i14.14871
iJIM ‒ Vol. 16, No. 04, 2022
147


---

Page 12

---

Paper—Flying Ad hoc Networks (FANET): Performance Evaluation of Topology Based Routing Protocols
	 [5]	V. Roberge, M. Tarbouchi, and G. Labonté, “Fast genetic algorithm path planner for 
fixed-wing military UAV using GPU,” IEEE Trans. Aerosp. Electron. Syst., vol. 54, no. 5, 
pp. 2105–2117, 2018. https://doi.org/10.1109/TAES.2018.2807558
	 [6]	Z. Kashino, G. Nejat, and B. Benhabib, “Aerial wilderness search and rescue with ground 
support,” J. Intell. Robot. Syst. Springer, vol. 99, no. 1, pp. 147–163, 2020. https://doi.
org/10.1007/s10846-019-01105-y
	 [7]	X. Li and J. Huang, “ABPP: An adaptive beacon scheme for geographic routing in FANET,” 
in 2017 18th International Conference on Parallel and Distributed Computing, Appli-
cations and Technologies (PDCAT), IEEE, 2017, pp. 293–299. https://doi.org/10.1109/
PDCAT.2017.00055
	 [8]	A. Bujari, C. E. Palazzi, and D. Ronzani, “FANET application scenarios and mobility mod-
els,” in Proceedings of the 3rd Workshop on Micro Aerial Vehicle Networks, Systems, and 
Applications,ACM, 2017, pp. 43–46. https://doi.org/10.1145/3086439.3086440
	 [9]	F. De Rango, G. Potrino, M. Tropea, A. F. Santamaria, and P. Fazio, “Scalable and ligth-
way bio-inspired coordination protocol for FANET in precision agriculture applications,” 
Comput. Electr. Eng. Elsevier, vol. 74, pp. 305–318, 2019. https://doi.org/10.1016/j.
compeleceng.2019.01.018
	[10]	F. A. Phang et al., “Integrating drone technology in service learning for engineering students,” 
Int. J. Emerg. Technol. Learn., vol. 16, no. 15, pp. 78–90, 2021. https://doi.org/10.3991/ijet.
v16i15.23673
	[11]	M. H. Habaebi, R. K. Omar, and M. R. Islam, “Mobile drone localization in indoor environ-
ment based on passive RFID,” Int. J. Interact. Mob. Technol., vol. 14, no. 5, pp. 4–15, 2020. 
https://doi.org/10.3991/ijim.v14i05.13309
	[12]	A. Joshi, S. Dhongdi, S. Kumar, and K. R. Anupama, “Simulation of multi-UAV ad-hoc 
network for disaster monitoring applications,” in 2020 International Conference on 
Information Networking (ICOIN), IEEE, 2020, pp. 690–695. https://doi.org/10.1109/
ICOIN48656.2020.9016543
	[13]	M. Y. Arafat and S. Moh, “Routing protocols for unmanned aerial vehicle networks: a survey,” 
IEEE Access, vol. 7, pp. 498–516, 2019. https://doi.org/10.1109/ACCESS.2018.2885539
	[14]	J. Souza, J. Jailton, T. Carvalho, J. Araújo, R. Francês, and Z. Kaleem, “A proposal for 
routing protocol for FANET: a fuzzy system approach with QoE/QoS guarantee,” Wirel. 
Commun. Mob. Comput., vol. 2019, 2019. https://doi.org/10.1155/2019/8709249
	[15]	M. F. Khan, K. L. A. Yau, R. M. Noor, and M. A. Imran, “Routing schemes in FANETs: 
A survey,” Sensors ,MDPI., vol. 20, no. 1, pp. 1–33, 2020. https://doi.org/10.3390/s20010038
	[16]	X. Li, T. Zhang, and J. Li, “A particle swarm mobility model for flying ad hoc networks,” in 
GLOBECOM 2017–2017 IEEE Global Communications Conference, IEEE., 2017, pp. 1–6. 
https://doi.org/10.1109/GLOCOM.2017.8253966
	[17]	C. A. Kerrache, E. Barka, N. Lagraa, and A. Lakas, “Reputation-aware energy-efficient solu-
tion for FANET monitoring,” in 2017 10th IFIP Wireless and Mobile Networking Confer-
ence (WMNC),IEEE., 2017, pp. 1–6. https://doi.org/10.1109/WMNC.2017.8248851
	[18]	J. S. Lee, Y. S. Yoo, H. S. Choi, T. Kim, and J. K. Choi, “Group Connectivity-based UAV 
positioning and data slot allocation for tactical MANET,” IEEE Access, vol. 8, 2020. https://
doi.org/10.1109/ACCESS.2020.3042795
	[19]	O. S. Oubbati, M. Atiquzzaman, P. Lorenz, M. H. Tareque, and M. S. Hossain, “Routing 
in flying Ad Hoc networks: Survey, constraints, and future challenge perspectives,” IEEE 
Access, vol. 7, pp. 81057–81105, 2019. https://doi.org/10.1109/ACCESS.2019.2923840
	[20]	C. M. Cheng, P. H. Hsiao, H. T. Kung, and D. Vlah, “Maximizing throughput of UAV-relaying 
networks with the load-carry-and-deliver paradigm,” IEEE Wirel. Commun. Netw. Conf. 
WCNC, pp. 4420–4427, 2007. https://doi.org/10.1109/WCNC.2007.805
148
http://www.i-jim.org


---

Page 13

---

Paper—Flying Ad hoc Networks (FANET): Performance Evaluation of Topology Based Routing Protocols
	[21]	A. H. Wheeb and M. T. Naser, “Simulation based comparison of routing protocols in wire-
less multihop ad hoc networks,” Int. J. Electr. Comput. Eng., vol. 11, no. 4, pp. 3186–3192, 
2021. https://doi.org/10.11591/ijece.v11i4.pp3186-3192
	[22]	O. K. Sahingoz, “Networking models in flying Ad-hoc networks (FANETs): Concepts and 
challenges,” J. Intell. Robot. Syst. Theory Appl., vol. 74, no. 1–2, pp. 513–527, 2014. https://
doi.org/10.1007/s10846-013-9959-7
	[23]	K. Singh and A. K. Verma, “Applying OLSR routing in FANETs,” Proc. 2014 IEEE Int. Conf. 
Adv. Commun. Control Comput. Technol. ICACCCT 2014, IEEE., no. 978, pp. 1212–1215, 
2015. https://doi.org/10.1109/ICACCCT.2014.7019290
	[24]	A. H. Wheeb and N. A. Shiltagh, “Performance analysis of OLSR protocol in mobile ad hoc 
networks,” Int. J. Interact. Mob. Technol., vol. 16, no. 1, 2022. https://doi.org/10.3991/ijim.
v16i01.26663
	[25]	Z. Zheng, A. K. Sangaiah, and T. Wang, “Adaptive communication protocols in flying ad hoc 
network,” IEEE Commun. Mag., vol. 56, no. 1, pp. 136–142, 2018. https://doi.org/10.1109/
MCOM.2017.1700323
	[26]	Z. Zhai, J. Du, and Y. Ren, “The application and improvement of temporally ordered routing 
algorithm in swarm network with unmanned aerial vehicle nodes,” Proc. IEEE ICWMC, 
pp. 7–12, 2013.
	[27]	A. H. Wheeb and D. N. Kanellopoulos, “Simulated performance of SCTP and TFRC over 
MANETs: The impact of traffic load and nodes mobility,” Int. J. Bus. Data Commun. Netw., 
vol. 16, no. 2, pp. 69–83, 2020. https://doi.org/10.4018/IJBDCN.2020070104
	[28]	D. A. Korneev, A. V Leonov, and G. A. Litvinov, “Estimation of mini-UAVs network param-
eters for search and rescue operation scenario with Gauss-Markov mobility model,” in 
2018Systems of Signal Synchronization, Generating and Processing in Telecommunications 
(SYNCHROINFO), 2018, pp. 1–7. https://doi.org/10.1109/SYNCHROINFO.2018.8457047
	[29]	N. Lin, F. Gao, L. Zhao, A. Al-Dubai, and Z. Tan, “A 3D smooth random walk mobility 
model for FANETs,” in IEEE 5th International Conference on Data Science and Systems 
(HPCC/SmartCity/DSS), 2019, pp. 460–467. https://doi.org/10.1109/HPCC/SmartCity/
DSS.2019.00075
7	
Author
Ali H. Wheeb is a Faculty Member - Lecturer at University of Baghdad since 
2014. His ﬁelds of research interest are flying ad hoc network, mobility models, IoT, 
wireless ad hoc networking, routing protocols, networking simulation tools Ns-2 & 
NS-3, transporting protocols. Further, he publish 11 research papers in high reputation 
journals. Also. Lecturer Ali serve as reviewer in several journals and conferences and 
reviewed 100 paper until now. Email: a.wheeb@coeng.uobaghdad.edu.iq
Article submitted 2021-11-11. Resubmitted 2021-12-17. Final acceptance 2021-12-19. Final version 
published as submitted by the authors.
iJIM ‒ Vol. 16, No. 04, 2022
149
