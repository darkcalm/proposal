

---

Page 1

---

Indonesian Journal of Electrical Engineering and Computer Science 
Vol. 19, No. 1, July 2020, pp. 395~402 
ISSN: 2502-4752, DOI: 10.11591/ijeecs.v19.i1.pp395-402 
     395 
 
 
Journal homepage: http://ijeecs.iaescore.com 
Performance evaluation of wireless sensor networks using 
LEACH protocol 
 
 
Anas Ali Hussien1, Shaymaa W. Al-Shammari2, Mehdi J. Marie3 
1,2Department of Computer Engineering, Al-Nahrain University, Iraq 
3Al-Zawraa State Co., Ministry of Industry and Minerals, Iraq 
 
 
Article Info 
 
ABSTRACT 
Article history: 
Received Nov 1, 2019 
Revised Dec 10, 2019 
Accepted Jan 8, 2020 
 
 
Recent days witnessed considerable developments in the field of wireless 
sensor networks (WSNs). The applications of these networks can be seen in 
the simple consumer electronic devices as well as in the advanced space 
technology. The communication protocols are of prior importance and 
interest; the low-energy adaptive clustering hierarchy (LEACH) protocol is 
used to enhance the performance of power consumption for the WSNs nodes.  
The efficiency of a wireless network can be affected by different factors, 
such as the size of the WSN and the initial energy of the sensor node. This 
can inspire the researchers to develop the optimum structure of the WSNs to 
get its desired functionality. In this paper, the performance of the low-energy 
adaptive clustering hierarchy (LEACH) protocol is investigated using 
MATLAB to study the effect of the initial energy of the sensor node and  
the WSN size on the number of the running nodes. It is found that increasing 
the initial energy of a sensor node increases the life time of the node and 
hence the number of the running nodes. It has been also approved that the 
WSN size has an inverse proportion with the number of running sensor nodes 
during the use of LEACH protocol. 
Keywords: 
LEACH Protocol  
Performance 
WSN 
Copyright © 2020 Institute of Advanced Engineering and Science.  
All rights reserved. 
Corresponding Author: 
Anas Ali Hussien, 
Department of Computer Engineering,  
Al-Nahrain University, Baghdad, Iraq. 
Email: anasali78@yahoo.com 
 
 
1. 
INTRODUCTION  
Wireless Sensor Networks have been employed in managing different and critical situations in life. 
To deal with the problems of energy consumption in WSN, the researchers have used many techniques in 
which they have suggested that Cluster Head CH should be chosen to forward the data of the nodes [1-3]. 
LEACH protocol is a hierarchical protocol; this protocol allows the sensor nodes to send data to  
the cluster heads of the cluster that they belong to. The cluster heads collect and aggregate the received data 
from the other nodes in the cluster and then forward it to the sink, which is called the base station. This 
protocol aims to increase the lifetime of the wireless sensor nodes. The overall operation of the LEACH 
protocol is based on the rounds, where each round consists of two stages, the first is the “set up stage”, while 
the second is the “steady state” stage. “Setup phase” operation consists of creating the cluster and to choose a 
CH for corresponding cluster. The “steady phase” involves the transmission of the collected information by 
the CH to the base station (sink). The architecture of LEACH protocol is represented in Figure 1. LEACH 
helps to balance energy consumption of the sensor nodes [4-9]. 
For the homogeneous cluster based network, the cluster heads as in LEACH are chosen randomly to 
act as relay nodes to transmit the data; then the cluster heads exchange their roles with normal nodes to 
consume a uniform energy of all the nodes. Because of the proposed hybrid technique, the lifetime of nodes 


---

Page 2

---

      
  
 
       ISSN: 2502-4752 
Indonesian J Elec Eng & Comp Sci, Vol. 19, No. 1, July 2020 :  395 - 402 
396 
increases and decreases the transmission energy consumption. The aim of the WSN is to transmit data 
continuously and to maximize the network coverage [10-18]. 
Many points should be taken into consideration that can affect the efficiency of routing of LEACH 
protocol, such as the life time of the sensor node that can be affected by the energy consumption in both  
the communication and computation, another factor is the coverage of nodes in the network area that includes 
both sensor and communication coverage, the scalability of the number of sensor nodes. Attention should be 
also paid to the performance metrics like network life time [18-20]. The continious decrease of the nodes 
energy is one of the disadvantages of the LEACH protocol, this is due to the communication occur among  
the nodes [21, 22].  
The aforementioned points had motivated the authors to consider these factors in studying  
the performance of the wireless sensor network. So, the aim of this paper is to study the effect of the sensor 
node’s initial energy and network size on the number of the running nodes and the consumed energy of  
the WSN. The importance of the study comes from being a reference that can inspire the researchers in the 
filed to develop the optimum structure of the WSNs in order to get its desired functionality. 
 
 
 
 
Figure 1. Hierarical wireless sensor network architecture [6] 
 
 
 
Studying the performance of the WSN taking into consideration the consumed energy has been 
considered by many researchers. Malik et al. (2013) studied the performance of LEACH protocol in WSN,  
the authors considered studying the performance as a result of changing the number of the cluster heads [23]. 
Sharma and Kumar (2017) presented a study of energy consumption using qualitative evaluation and channel 
probing [24] the presented study measured the consumed energy. The research performed by Elhoseny et al. 
(2017) introduced a performance evaluation for the LEACH protocol for a proposed method to elect the CH 
in the WSN [25]. However, the reported results in these researches lacked considering the effect of changing  
the network size or the initial energy of the used sensor nodes. The dissipated energy in the transmitter and 
receiver circuits in LEACH protocol needed to transmit a message composed of k-bits can be defined by the 
following formulas [4]: 
 
𝐸𝑇𝑥( 𝑘, 𝑑 ) =  𝑘 ∗ 𝐸𝑒𝑙𝑒𝑐 +  𝑘 ∗ 𝐸𝑎𝑚𝑝 ∗ 𝑑2          𝑑 <  0 
(1) 
 
= 𝑘 ∗ 𝐸𝑒𝑙𝑒𝑐 +  𝑘 ∗ 𝐸𝑎𝑚𝑝 ∗ 𝑑4   𝑑 ≥ 0 
(2) 
 
where d is the distance, Eelec is the consumed energy in the transmitter circit, 𝐸𝑎𝑚𝑝 is the consumed energy in 
the amplifier used to maintain reliable signal. 
The rest of this paper is organized as follows, an introduction to the WSN system model is presented 
in section 1, section 2 presents the proposed model and mathematical models, section 3 discusses the 
obtained simulation results, the main conclusions are presented in section 4. 
 
 
2. 
PROPOSED WSN SYSTEM MODEL 
In order to model the LEACH protocol, the following assumptions are taken into consideration.  
The sensor nodes and the sink are all stationary after deployment. The sensor nodes are distributed uniformly 
and randomly in the network field. The sensors are homogeneous with the same capabilities. The sensor 
nodes are battery powered; therefore, have limited energy. And the suggested sensor nodes can calculate their 
residual energy. 


---

Page 3

---

Indonesian J Elec Eng & Comp Sci  
ISSN: 2502-4752 
 
 
Performance evaluation of wireless sensor networks using LEACH protocol (Anas Ali Hussien) 
397
A set of sensor nodes Sn and a sink node in the network was considered. Each sensor node has  
the location information (x, y). The sleep mode is used for the sensor node to conserve the energy.  
The communication is accomplished between the sensor nodes using the LEACH protocol. The sink node 
possesses unlimited computation, memory, and battery power. The sink node also contains the identity and 
location of each sensor node. When the sink requires the data from the source node, it constructs the route 
between them.  
 
 
3. 
SIMULATION RESULTS  
This section introduces the simulation of the system, which is done using Matlab 2018 to evaluate  
the LEACH protocol using comparative analysis among different senarios. It is assumed that the 
homogenous sensor network is considered to be in the centre of the WSN, so in the case of 100x100 network, 
the sink will be in the (x=50, y=50) coordinates, and for the case of 50x50 network, the sink will be in the 
(x=25 y=25) and in the case of 150x150 network, the sink will be in the (x=75, y=75). This research 
considered studying the behaviour of the WSN taking into consideration many scenarios. This includes 
reviewing the effect of changing the initial energy of the sensor nodes on the number of the running nodes 
per rounds and transmission, in addition to the energy consumed in each scenario. The study also introduced 
studying the effect of changing the size of the wireless sensor network on the running nodes taking into 
consideration many scenarios. 
The results are discussed for each scenario. The simulation parameters involve the following: the 
data packet size is 512 bytes, the energy of both the transmitter and receiver is 50 nano Joule/bit, and the 
energy spent by the amplifier is 100 pico Joule / bit. 
 
3.1.  The effect of changing the initial energy 
The following scenarios are considered to consider the effect of changing the initiual energy on the 
number of running nodes/rounds, number of running nodes/transmission, in addition to the comsumed 
energy. Table 1 summarises the results obtained in each scenario. 
 
Scenario 1: (running nodes 100) network size 100x100:  
This scenario presents the results obtained in the case of changing the initial energy in the case of 
considering 100 sensor nodes in the field and in the case of 100x100 m2 network dimension. It can be noticed 
from the obtained results in Table 1 that increasing the initial energy will increase the average number of the 
running nodes due to extending the life time of the sensor node. However, it can be noticed that increasing 
the initial energy to 10 Joule caused a degradation in the number of running nodes. 
 
Scenario 2: (running nodes 150) network size 100x100. 
This scenario presents the results obtained in the case of changing the initial energy in the case of 
considering 150 sensor nodes in the field and in the case of 100x100 m2 network dimension. 
 
Scenario 3: (running nodes 50) network size 100x100. 
This scenario presents the results obtained in the case of changing the initial energy in the case of 
considering 50 sensor nodes in the field and in the case of 100x100 m2 network dimension. 
 
Scenario 4: (running nodes 100) network size 50x50. 
This scenario presents the results obtained in the case of changing the initial energy in the case of 
considering 100 sensor nodes in the field and in the case of 50x50 m2 network dimension.  
Scenario 5: (running nodes 150) network size 50x50. 
This scenario presents the results obtained in the case of changing the initial energy in the case of 
considering 150 sensor nodes in the field and in the case of 50x50 m2 network dimension.  
Scenario 6: (running nodes 50) network size 50x50. 
This scenario presents the results obtained in the case of changing the initial energy in the case of considering 
50 sensor nodes in the field and in the case of 50x50 m2 network dimension. 
Scenario 7: (running nodes 100) network size 150x150. 
This scenario presents the results obtained in the case of changing the initial energy in the case of 
considering 100 sensor nodes in the field and in the case of 150x150 m2 network dimension. 
 


---

Page 4

---

      
  
 
       ISSN: 2502-4752 
Indonesian J Elec Eng & Comp Sci, Vol. 19, No. 1, July 2020 :  395 - 402 
398 
Scenario 8: (running nodes 150) network size 150x150. 
This scenario presents the results obtained in the case of changing the initial energy in the case of 
considering 100 sensor nodes in the field and in the case of 150x150 m2 network dimension.  
Scenario 9: (running nodes 50) network size 150x150. 
This scenario presents the results obtained in the case of changing the initial energy in the case of 
considering 50 sensor nodes in the field and in the case of 150x150 m2 network dimension. It can be noticed 
in this scenario that the overall number of sensor nodes for the different initial energies are less than those for 
the other scenarios. This is due to the large size of the network and the small size of the available sensor 
nodes, which affect the number of the operational nodes in the network. Figure 2 shows the wireless sensor 
network for the case of initial energy = 5Joule. 
 
 
 
 
Figure 2. Wireless sensor network (scenario 9 – initial energy = 5 Joule) 
 
 
3.2. The effect of changing the network size on the overall performance 
This section studies the effect of changing the network size on the overall performance of the 
wireless sensor network taking into consideration different values of the initial energies. This kind of results 
helps to indicate and understand the impact of the actually used sensor nodes with respect to the area of the 
sensor network. It can be noticed from the results that increase the network size had led to reducing the 
number of running nodes, this is due to increasing the distance between the nodes from the sink. This is 
proportional to increasing the initial power from the running nodes as shown in Figures 3-7. 
 
 
 
 
Figure 3. The effect of changing the network size on the running nodes – initial energy = 0.1 Joule 
 
 
0
20
40
60
80
100
50x50
100x100
150x150
Running 
nodes/Netwrok size 
(m2)
Number of nodes
50 nodes
100 nodes
150 nodes


---

Page 5

---

Indonesian J Elec Eng & Comp Sci  
ISSN: 2502-4752 
 
 
Performance evaluation of wireless sensor networks using LEACH protocol (Anas Ali Hussien) 
399
 
 
Figure 4. The effect of changing the network size on the running nodes – initial energy = 2 Joule 
 
 
 
 
Figure 5. The effect of changing the network size on the running nodes – initial energy = 5 Joule 
 
 
 
 
Figure 6. The effect of changing the network size on the running nodes – initial energy = 7 Joule 
 
 
 
 
Figure 7. The effect of changing the network size on the running nodes – initial energy = 10 Joule 
 
0
50
100
150
50x50
100x100
150x150
Running nodes/Netwrok 
size (m2)
Number of nodes
50 nodes
100 nodes
150 nodes
0
20
40
60
80
100
120
140
50x50
100x100
150x150
Running nodes/Netwrok size 
(m2)
Number of nodes
50 nodes
100 nodes
150 nodes
0
20
40
60
80
100
120
50x50
100x100
150x150
Running nodes/Netwrok 
size (m2)
Number of nodes
50 nodes
100 nodes
150 nodes
0
20
40
60
80
100
120
140
50x50
100x100
150x150
Running nodes/Netwrok size 
(m2)
Number of nodes
50 nodes
100 nodes
150 nodes


---

Page 6

---

      
  
 
       ISSN: 2502-4752 
Indonesian J Elec Eng & Comp Sci, Vol. 19, No. 1, July 2020 :  395 - 402 
400 
Table 1. Summarizes the running nodes/rounds, running nodes/transmission, and the consumend energy for 
scenarios (1-9) with different initial energies 
 
 
4. 
CONCLUSION 
Through the improvement of communication and processor technology, wireless sensor networks 
are becoming a strong opposition against the wired network. It has also been shown that the effective 
parameters of wireless networks are the power of the transmitted signal; they can cause a degradation of the 
system performance and can make it unstable. The protocol LEACH has been designed to improve the 
lifetime, latency and reliability through discovering multiple paths between the source and the sink. More 
than one routing paths are available for data transmission. If one path fails, an alternate path is used to 
transmit the data. The results showed the effect of increasing the initial energy on the overall number of the 
running nodes in the WSN. It has also been approved that the size of the wireless network could affect the 
transmission of the data in the WSN. Studying the performance of the WSN can be extended in the future 
Scenario 
Initial 
Energy 
Operational 
nodes/Rounds 
Operational 
nodes/Transmission 
Consumed Energy 
Max 
Mean 
Max 
Mean 
Max 
Mean 
Scenario 1  
(running nodes = 100) 
network size (100x100) 
0.1 
100 
31.15 
100 
74.63 
0.1876 
0.08051 
2 
100 
64.87 
100 
83.98 
0.3088 
0.0846 
5 
100 
65.97 
100 
84.03 
0.278 
0.08123 
7 
100 
70.37 
100 
84.83 
0.2705 
0.08118 
10 
100 
68.22 
100 
83.89 
0.272 
0.0845 
Scenario 2  
(running nodes = 150) 
network size (100x100) 
0.1 
150 
96.03 
150 
125 
0.1708 
0.0998 
2 
150 
90.87 
150 
131.4 
0.2934 
0.1011 
5 
150 
67.86 
150 
127.8 
0.4371 
0.1032 
7 
150 
98.61 
150 
132.2 
0.3943 
0.1055 
10 
150 
103.6 
150 
134.9 
0.4123 
0.1021 
Scenario 3  
(running nodes = 50)  
network size (100x100) 
0.1 
50 
10.18 
50 
31.06 
0.1298 
0.05175 
2 
50 
16.67 
50 
33.9 
0.1402 
0.05858 
5 
50 
18.01 
50 
34.04 
0.1256 
0.05876 
7 
50 
17.63 
50 
32.89 
0.1329 
0.05847 
10 
50 
11.56 
50 
31.21 
0.1521 
0.060403 
Scenario 4  
(running nodes = 100) 
network size (50x50) 
0.1 
100 
45.82 
100 
82.26 
0.07818 
0.05105 
2 
100 
70.62 
100 
92.63 
0.1024 
0.05149 
5 
100 
81.05 
100 
95.77 
0.1013 
0.05268 
7 
100 
70.01 
100 
92.93 
0.09922 
0.05112 
10 
100 
83.46 
100 
92.75 
0.1031 
0.05101 
Scenario 5  
(running nodes = 150) 
network size (50x50) 
0.1 
150 
84.22 
150 
124.7 
0.0651 
0.09327 
2 
150 
92.73 
150 
137.4 
0.1498 
0.0723 
5 
150 
113.5 
150 
136.2 
0.1462 
0.07126 
7 
150 
112.4 
150 
136.4 
0.1551 
0.07131 
10 
150 
117.9 
150 
138.3 
0.1546 
0.07212 
Scenario 6  
(running nodes = 50)  
network size (50x50) 
0.1 
50 
25.31 
50 
40.69 
0.0459 
0.0295 
2 
50 
27.47 
50 
45.13 
0.0577 
0.03085 
5 
50 
32.26 
50 
46.86 
0.0517 
0.02946 
7 
50 
45.14 
50 
47.95 
0.04993 
0.02936 
10 
50 
42.73 
50 
47.56 
0.04897 
0.03032 
Scenario 7  
(running nodes = 100) 
network size (150x150) 
0.1 
100 
64.57 
100 
75.7 
0.4376 
0.1255 
2 
100 
34.99 
100 
66.4 
0.3968 
0.1272 
5 
100 
41.94 
100 
69.74 
0.5011 
0.1348 
7 
100 
64.18 
100 
65.37 
0.6376 
0.1413 
10 
100 
51.29 
100 
68.52 
0.6004 
0.1285 
Scenario 8  
(running nodes = 150) 
network size (150x150) 
0.1 
150 
61.52 
150 
84.79 
0.4706 
0.1533 
2 
150 
71.83 
150 
108.6 
0.5734 
0.1578 
5 
150 
78.25 
150 
112.2 
0.734 
0.1532 
7 
150 
68.68 
150 
110.2 
0.8123 
0.1489 
10 
150 
81.9 
150 
117.5 
0.8906 
0.1565 
Scenario 9  
(running nodes = 50)  
network size (150x150) 
0.1 
50 
17.4 
50 
26.05 
0.243 
0.1062 
2 
50 
14.96 
50 
29.16 
0.2855 
0.1017 
5 
50 
16.1 
50 
27.87 
0.2913 
0.1016 
7 
50 
10.28 
50 
27.6 
0.3027 
0.09858 
10 
50 
6.603 
50 
23.92 
0.2925 
0.1019 


---

Page 7

---

Indonesian J Elec Eng & Comp Sci  
ISSN: 2502-4752 
 
 
Performance evaluation of wireless sensor networks using LEACH protocol (Anas Ali Hussien) 
401
work from a simulation to consider a real implementation of the environment taking into consideration the 
studied parameters. 
 
 
REFERENCES  
[1] 
Hussien, Anas Ali, and Muntaha Jameel Eidan, "Automatic ZigBee-Based Wireless Sensor Network for Real Time 
Temperature Control," International Journal of Wireless Communication and Networking Technology, vol. 4, no. 4 
July 2015. 
[2] 
Hussien, Anas A. and Matloob, Safa I., “The Comparative Study Some of Reactive and Proactive Routing 
Protocols in The Wireless Sensor Network,” Journal of University of Babylon for Engineering Sciences, vol. 26, 
no. 4, pp. 195-207, February 2018. 
[3] 
Qian Liao, Hao Zhu, “An Energy Balanced Clustering Algorithm Based on LEACH Protocol,” Proceedings of the 
2nd International Conference On Systems Engineering and Modeling (ICSEM-13), 2013. 
[4] 
Vishwakarma, Sangita, "An analysis of LEACH Protocol in Wireless Sensor Network: A Survey," International 
Journal of Computer Science & Engineering Technology, vol. 6, no. 3, pp. 148-154, March 2015. 
[5] 
Lalita Yadav1, Ch. Sunitha, Lalita Yadav, “Low Energy Adaptive Clustering Hierarchy in Wireless Sensor 
Network (LEACH),” International Journal of Computer Science and Information Technologies, (IJCSIT), vol. 5, 
no. 3, 2014. 
[6] 
Jose Henrique Brand ´ ao Neto, Antoniel da Silva Rego, Andre Ribeiro Cardoso, Joaquim Celestino, “MH-
LEACH: A Distributed Algorithm for Multi-Hop Communication in Wireless Sensor Networks,” ICN 2014: The 
Thirteenth International Conference on Networks, pp. 55-61, 2014. 
[7] 
Singh S. and Sharma S., “A Survey on Cluster Based Routing Protocols in Wireless Sensor Networks,” In Procedia 
Computer Science, vol. 45, pp. 687- 695, 2015. 
[8] 
Belwal, Monika. "Energy Efficient Leach And Improved Leach: A Review," International Journal of Advanced 
Research in Computer Science, vol. 10, no. 3, pp. 51-53, pp. 92-96, May 2019. 
[9] 
Kaur, P., and Kad, S., “Energy-efficient routing protocols for wireless sensor network: a review,” International 
Journal of Scientific & Technolgy Research, vol. 6, no. 12, December 2017. 
[10] Rani, Shalli, Jyoteesh Malhotra, and Rajneesh Talwar, "EEICCP-energy efficient protocol for wireless sensor 
networks," Wireless sensor network, vol. 5, no. 7, pp. 127-136, 2013. 
[11] Stephanie Lindsey Cauligi S. Raghavendra,”PEGASIS: Power-Efficient Gathering in Sensor Information Systems,” 
Proceedings, IEEE Aerospace Conference, Big Sky, MT, USA, pp. 3-3, 2002. 
[12] Jain T., Saini D., and  Bhooshan S., “Lifetime Optimization of a Multiple SinkWireless Sensor Network through 
Energy Balancing,” Journal of Sensors, vol. 2015, pp. 1-6, April 2015. 
[13] P. Kuila and P. K. Jana, “Energy Efficient Clustering and Routing Algorithms for Wireless Sensor Networks: 
Particle Swarm Optimization Approach,” Engineering Applications of Artificial Intelligence, vol. 33, pp. 127-140, 
August 2014. 
[14] Suraj Sharma, “On Energy Efficient Routing Protocols Wireless Sensor Networks,” Ph. D. Dissertation, 
Department of Computer Science and Engineering National Institute of Technology Rourkela Rourkela-769 008, 
Odisha, India, 2016. 
[15] Nishita Payar, Prof. Chandresh R. Parekh, Nishita Payar et al., “Ee-Leach (Low Energy Adaptive Clustering 
Hierarchy) Modified Protocol,” Int. Journal of Engineering Research and Applications, vol. 4, pp. 5-10, May 2014. 
[16] Jain T., Saini D., and Bhooshan S., “Lifetime Optimization of a Multiple Sink Wireless Sensor Network through 
Energy Balancing,” Journal of Sensors, vol. 2015, pp. 1–6, April 2015. 
[17] Siva D. Muruganathan, Daniel C. F. Ma, Rolly I. Bhasin, andabraham, Fapojuwo, “A Centralized Energy-Efficient 
Routing Protocol for Wireless Sensor Networks,” in IEEE Communications Magazine, vol. 43, no. 3, pp. S8-13, 
March 2005. 
[18] Prasad, A. Y., and Balakrishna, R., “Implementation of optimal solution for network lifetime and energy 
consumption metrics using improved energy efficient LEACH protocol in MANET,” TELKOMNIKA, vol. 17, no. 
4, pp. 1758-1766, August 2019. 
[19] Chunyao FU, Zhifang JIANG, Wei WEI and Ang WEI, IJCSI, “An Energy Balanced Algorithm of LEACH 
Protocol in WSN,” International Journal of Computer Science Issues (IJCSI), vol.10, no. 1, pp. 354-359,January 
2013 
[20] Suraj Sharma, Sanjay Kumar Jena, “Cluster-based Multipath Routing Protocol for Wireless Sensor Networks,” 
ACM SIGCOMM Computer Communication Review, vol. 45, no. 2, pp. 15-20, April 2015. 
[21] Ouldzira, H., Lagraini, H., Mouhsen, A., Chhiba, M., & Tabyaoui, A., “MG-leach: an enhanced leach protocol for 
wireless sensor network,” International Journal of Electrical & Computer Engineering(IJECE), vol. 9, no. 4, pp. 
3139-3145, August 2019. 
[22] Kundaliya, B., & Hadia, S. K., “Enhancing network lifetime with an improved MOD-LEACH,” International 
Journal of Electrical & Computer Engineering(IJECE), vol. 9, no. 5, pp. 3615-3622, October 2019. 
[23] Malik, M., Singh, Y., and Arora, A., “Analysis of LEACH protocol in wireless sensor networks,” International 
Journal of Advanced Research in Computer Science and Software Engineering, vol. 3, no. 2, 2013. 
[24] Sharma, B., and Kumar, G., “Performance analysis for qualitative evaluation with comparative study for designing 
energy efficient algorithm for wireless sensor networks for enhancing lifetime of leach protocol using dynamic 
simulation as variation in channel probing for opportunistic power saving mechanism for power evaluation and 
estimation optimization as latest trend used in electronics and communication engineering,” Journal Appl 
Biotechnol Bioeng, vol. 4, no. 3, pp. 622-625, 2017. 


---

Page 8

---

      
  
 
       ISSN: 2502-4752 
Indonesian J Elec Eng & Comp Sci, Vol. 19, No. 1, July 2020 :  395 - 402 
402 
[25] Elhoseny, M., Farouk, A., Zhou, N., Wang, M. M., Abdalla, S., & Batle, J., “Dynamic multi-hop clustering in a 
wireless sensor network: Performance improvement,” Wireless Personal Communications, vol. 95, no.4, pp. 3733-
3753, March 2017. 
 
 
BIOGRAPHY OF AUTHORS 
 
 
Anas Ali Hussien received the B.Sc. in Electronics and Communications Engineering in 1999, 
M.Sc. in Electronics and Communications Engineering / Electronic Circuits and Systems in 2001 
and Ph.D. in Information Engineering in 2007, from Al-Nahrain University. 
He is an associate professor since 2012 and head of the computer-engineering department. 
Dr Anas has published more than 12 published papers all of them in reputed journals and 
conferences 
 
 
Shaymaa Waleed AlShammari received the B.Sc. in Computer Engineering in 2005, M.Sc. in 
Computer Engineering in 2008 from Al-Nahrain University, Baghdad, Iraq, and Ph.D. in 
Computer Engineering / Distributed Systems in 2017 from University of Salford, Manchester, 
UK. 
She is a lecturer in Al-Nahrain University, Baghdad, Iraq since 2008. Her research interests are 
in the subject of cloud computing, web services, QoS, QoE, network performance and published 
many papers related to these subjects. 
 
 
Mehdi J. Marie was born in Baghdad, Iraq in 1970. He received his Bachelor's (1993), Master's 
(2004) Degrees from University of Technology (Iraq) and Ph. D. from the University of Basrah 
(2014).  He has been a lecturer of Control Theory I, II, Electronics and Electrical Networks at the 
Al-Nahrain University, College of Engineering. He is currently a senior engineer at Al-Zawaraa 
State Company, Ministry 
 
