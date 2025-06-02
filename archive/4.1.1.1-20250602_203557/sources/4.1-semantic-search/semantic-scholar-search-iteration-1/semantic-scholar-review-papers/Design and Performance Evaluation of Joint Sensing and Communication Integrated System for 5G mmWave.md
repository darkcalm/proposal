

---

Page 1

---

1
Design and Performance Evaluation of Joint
Sensing and Communication Integrated System for
5G MmWave Enabled CAVs
Qixun Zhang, Member, IEEE, Xinna Wang, Zhenhao Li, Zhiqing Wei, Member, IEEE
Abstract—The safety of connected automated vehicles (CAVs)
relies on the reliable and efﬁcient raw data sharing from
multiple types of sensors. The 5G millimeter wave (mmWave)
communication technology can enhance the environment sensing
ability of different isolated vehicles. In this paper, a joint sensing
and communication integrated system (JSCIS) is designed to
support the dynamic frame structure conﬁguration for sensing
and communication dual functions based on the 5G New Radio
protocol in the mmWave frequency band, which can solve
the low latency and high data rate problems of raw sensing
data sharing among CAVs. To evaluate the timeliness of raw
sensing data transmission, the best time duration allocation ratio
of sensing and communication dual functions for one vehicle
is achieved by modeling the M/M/1 queuing problem using
the age of information (AoI) in this paper. Furthermore, the
resource allocation optimization problem among multiple CAVs
is formulated as a non-cooperative game using the radar mutual
information as a key indicator. And the feasibility and existence
of pure strategy Nash equilibrium (NE) are proved theoretically,
and a centralized time resource allocation (CTRA) algorithm is
proposed to achieve the best feasible pure strategy NE. Finally,
both simulation and hardware testbed are designed, and the
results show that the proposed CTRA algorithm can improve
the radar total mutual information by 26%, and the feasibility of
the proposed JSCIS is achieved with an acceptable radar ranging
accuracy within ± 0.25 m, as well as a stable data rate of 2.8
Gbps using the 28 GHz mmWave frequency band.
Index Terms—Connected Automated Vehicles, Joint Sensing
and Communication, 5G New Radio, Millimeter wave, Age of
Information
I. INTRODUCTION
In recent years, the rapid development of artiﬁcial intel-
ligence and mobile communication technology has brought
revolutionary progresses for the autonomous driving vehicles
(ADVs). Typical sensors in ADVs include the optical cam-
eras, light detection and ranging (LiDAR), ultrasonic sensors,
mmWave radars and so on. However, the detection perfor-
mance of different sensors is vulnerable to the dynamic chang-
ing radio environment and the blockage of other vehicles. In
order to ensure the safety of ADVs, the cooperation of multi-
sensors in different vehicles via wideband communication
Corresponding author is Q. Zhang. Q. Zhang, X. Wang, Z. Li and Z. Wei
are with the Key Laboratory of Universal Wireless Communications Ministry
of Education, Beijing University of Posts and Telecommunications, Beijing
100876, China (e-mail: zhangqixun@bupt.edu.cn, xinna wang@bupt.edu.cn,
zhenhao918@bupt.edu.cn, weizhiqing@bupt.edu.cn).
This work was partly supported by National Natural Science Foundation
of China (NSFC) (Grant No. 62022020) and National Key Research and
Development Project (Grant No. 2020YFB1807600).
Manuscript submitted to Journal of Selected Topics in Signal Processing
on Feb. 18, 2021; Major revision submitted on Jun. 18, 2021.
technology is an effective way to extend the environment
information sensing ability and facilitate vehicles’ decision-
making [1]. But, multiple sensors in ADVs can generate an
excessive amount of raw data over several Gbps [2], leading to
the efﬁcient raw data sharing among vehicles a big problem.
It is envisioned that the Internet of Vehicles (IoV) and
the 5G mmWave communications [3] would be a promising
solution to tackle the aforementioned challenges, which may
signiﬁcantly improve the see-through ability of ADVs [4]. As a
fast-developing technology, 5G cellular vehicle-to-everything
(C-V2X) is able to support a higher data rate [5]. Besides, the
information interaction between vehicles via 5G communica-
tion can effectively ﬁll the blind area of sensing, achieving the
high-accuracy information integration. Furthermore, vehicles
mounted with in-vehicle sensors and V2X communication
equipment to support autonomous driving applications are de-
ﬁned as the connected automated vehicles (CAVs) [6]. Consid-
ering the limited spectrum resources for 5G C-V2X, the idea
of spectrum sharing technology [7] using joint sensing and
communication design has attracted much attention recently,
which may solve the problem of low latency raw sensing
data sharing and improve the sensing ability of CAVs. A
distributed networking protocol RadChat was proposed in [7]
to mitigate the interference among FMCW based automotive
radars by using radar and communication cooperation. And
the results show that RadChat can signiﬁcantly reduce radar
mutual interference in single-hop vehicular networks in less
than 80 ms.
From the perspective of simple dual-functional aggrega-
tion, the information from radar has been used to assist
the beam alignment of 60 GHz mmWave communication
through the Dedicated Short Range Communication (DSRC)
[1]. Furthermore, the combination design of the automotive
radar at 76.5 GHz and the mmWave communication at 65
GHz has been proposed for the radar-aided communication
with separate antennas [8], which only considers the vehicle-
to-infrastructure (V2I) scenario in different spectrum bands
without considering the V2V scenario. Although these afore-
mentioned schemes have the basic sensing and communication
functionalities, they only focus on the simple coexistence issue
of two systems, which lead to severe signaling overhead and
hardware cost, and are consequently unable to realize the
integrated system.
In terms of the sensing and communication integration
perspective, the existing research works focus on the joint
frame structure and waveform design. Pioneered by [9], a
arXiv:2108.10535v2  [eess.SY]  25 Aug 2021


---

Page 2

---

2
radar information measurement using mutual information (MI)
has been proposed. Furthermore, the fusion of radar and
communication can be realized by using the radio frequency
convergence schemes [10]. Moreover, MIMO radar and the
cellular base stations can coexist through spectrum sharing,
where the radar waveform can be used as a pilot signal [11].
Second, for the joint frame structure design, the radar and
communication signals can be transmitted in different time
slots without causing the interference to each other based on
the time division framework [12]. A novel time division duplex
frame structure which is capable of unifying the radar and
communication operations is proposed in [13], and the signal
processing is divided into three stages to realize basic radar
and communication operations. For the purpose of designing a
joint waveform, one may embed communication data into the
radar probing signal [14]. Alternatively, the communication
preambles of IEEE 802.11ad standard can also be exploited
to design radar waveforms [15], but there is no system-
level design and simulation for the integrated waveform. By
using spatial and time division methods, both sensing and
communication stages can be switched periodically with a
set of conﬁgured antennas in [16]. Above all, the radar and
communication functions can be complementary to each other
in the integrated system. However, the sharing of mmWave
band between radar and communication dual functions has
not been fully considered in the existing research works, and
the performances of sensing and communication cannot be
balanced effectively given the limited computation resources
and hardware constraints. Therefore, the resource allocation
problem needs to be taken into account for the design of
radar and communication dual functions. In [17], the non-
cooperative game based resource allocation method is pro-
posed to optimize the sum rate of the self-backhaul dense
mmWave cellular network, which can also be used in the
vehicle network. But, the radar and communication integrated
system faces the challenging problem of complex interactions
of sensing and communication signal. As a proper metric
to characterize the information freshness [18] among CAVs,
the Age of Information (AoI) is deﬁned as the freshness
of the received information. The AoI performance of a N-
hop network with time-invariant packet loss probabilities on
each link is analyzed in [19]. However, the packet loss
probability will change with the variation of the network state,
which is particularly serious in the vehicle network. Besides,
a method to minimize the expected AoI satisfying timely-
throughput constraints is proposed for a single-hop wireless
network with a number of nodes transmitting the time-sensitive
information to a base station in [20]. The average AoI for
stationary randomized and round-robin scheduling policies in
a multi-source status update system is analyzed in [21], but
these policies are not suitable for the timeliness data sharing
in the vehicle network. The vehicular beacon broadcasting
scheduling problem with respect to the AoI is investigated
in [22]. However, these research works have not considered
the problem of data freshness in the radar and communication
integrated system.
To cope with these challenges, we propose a time-division
based joint sensing and communication integrated system
(JSCIS) for 5G mmWave enabled CAVs. To tackle the low
latency and efﬁcient raw sensing data delivery problem, we
model the source-destination link for CAVs using M/M/1
queuing theory and analyze the packet loss probability and
average AoI. And the best time duration allocation ratio of
sensing and communication dual functions for one vehicle
is achieved. For multiple CAVs, we propose the Centralized
Time Resource Allocation (CTRA) algorithm based on the
non-cooperative game to reduce the computational complexity
of time resource allocation. To the best of our knowledge, we
are the ﬁrst to consider the time resource allocation problem
for sensing and communication dual functions in the time-
division based JSCIS. The main contributions of this paper
are summarized as follows.
• A time-division based JSCIS for CAVs in the mmWave
frequency band is proposed. And 5G New Radio (NR)
based dynamic frame structure for JSCIS is designed,
so that each vehicle can allocate the time duration ratio
according to the service requirements. Based on the time-
division frame structure and the interference analysis, the
average AoI equation of single vehicle as a function of
server load rate is derived using First-Come-First-Served
(FCFS) M/M/1 queuing theory. We analyze the effects
of different duration allocation ratios on the packet loss
probability and the average AoI. The best time duration
allocation ratio range for one vehicle is achieved through
the analysis of the packet loss probability and the average
AoI.
• We establish the optimization problem with the radar total
MI as the performance evaluation indicator, and further
formulate the optimization problem as a non-cooperative
game to tackle the resource allocation of multiple CAVs,
and the feasibility and existence of the pure strategy Nash
equilibrium (NE) is proved theoretically. To achieve the
best NE, we design the CTRA algorithm with the low
complexity and fast convergence speed, and derive a set
of optimal allocation ratios for JSCIS.
• To verify the feasibility of JSCIS and the performance of
CTRA algorithm, both software simulation and hardware
testbed are developed. The software simulation results
denote that the best time duration allocation ratio of
one vehicle can be achieved. For multiple CAVs, the
software simulation results show that the proposed CTRA
algorithm can improve the radar total mutual informa-
tion by 26% compared to conventional algorithms. And
the proportional set of vehicle time allocation can be
obtained. The hardware testbed results prove that the
feasibility of the proposed JSCIS can be achieved with
an acceptable radar ranging accuracy within ± 0.25 m,
as well as a stable data rate of 2.8 Gbps using the 28
GHz mmWave frequency band.
The rest of this paper is organized as follows. In Section
II, we present the system model and problem formulation.
A novel time-division based resource allocation algorithm
with non-uniform durations are proposed in Section III. In
Section IV, both software simulation and hardware testbed
are designed and the results are discussed in detail. Finally,


---

Page 3

---

3
Driver
A
E
C
D
C
F
B
F
RSU
Communication
Sensing
V2I
V2V
Blind Spot
Driver View
Joint Sensing 
and
Communication
D
B
F
E
C
Autonomous
Sensing
D
E
B
Cooperative 
Sensing 
C
F
5G NR
Fig. 1. The sensing and communication integration scenario
with multiple cooperative CAVs.
Section V concludes this paper.
II. SYSTEM MODEL AND PROBLEM FORMULATION
We consider a 5G mmWave enabled CAVs scenario with
JSCIS design. In this section, we describe the scenario and
the frame structure design for JSCIS. Based on the time-
division JSCIS, both radar signal and communication signal
interferences scenario are analyzed in detail, respectively.
Furthermore, the source to destination link is modeled by
M/M/1 queuing theory and the average Age of Information
(AoI) for one vehicle is also deﬁned, which is a function
of server load rate under the packet loss probability. Finally,
we establish a resource allocation optimization function to
maximize the radar total MI considering multiple CAVs. The
symbols and deﬁnitions are summarized in Table I.
A. Scenario Description
The scenario of JSCIS for 5G mmWave enabled CAVs is
shown in Fig. 1. Vehicle A can obtain the position information
of vehicle B, D, and E through radar detection. However,
vehicle A cannot detect vehicle C due to the blockage by
vehicle B. By communicating with vehicle B, vehicle A can
obtain the information about vehicle C. Each vehicle near
vehicle A can use the mmWave link to directly communi-
cate with vehicle A instantly, which can effectively reduce
the transmission delay and assist vehicle A to be aware of
the environment information nearby. In the same way, other
vehicles outside the sensing distance of vehicle A or in the
blind spot of the driver’s view can also realize raw sensing
information sharing using the mmWave communication links
among vehicles. Vehicle A can also collect the information and
communicate with the infrastructure on the roadside, while
uploading the collected information and downloading other
trafﬁc or entertainment information. Therefore, vehicle A is
considered as the central vehicle which is responsible for
information processing in this paper based on ITU standard in
[23], so as to effectively expand the sensing range. All time
resource conﬁguration sets, vehicle power conﬁguration and
channel state information (CSI) of all vehicles are known by
vehicle A in the system. In addition, the resource allocation
ĂĂ
Subframe
n-2
Subframe
n-1
Subframe
n
Subframe
n+1
Subframe
n+2
Data
Data
Data
ĂĂ
Flexible adjustable mini slot
Control information slot
Data
1ms
Subframe
n-1
Subframe
n+1
P sensing subframes
Q communication subframes
ĂĂ
ĂĂ
Fig. 2. The dynamic frame structure design of JSCIS.
strategies adjusted by other vehicles can be sent back to the
central vehicle A efﬁciently.
B. Dynamic Frame Structure Design
Compared with the ﬁxed 15kHz subcarrier interval in
4G LTE, 5G NR supports different subcarrier intervals [24].
For 5G NR V2X, the 15kHz, 30kHz and 60kHz subcarrier
intervals are used to support the communication below 6GHz,
while 60kHz and 120kHz can support the communication
above 6GHz. Both transmitters and receivers can occupy more
bandwidth resources in mmWave frequency bands. And the
time delay will be considerably reduced by utilizing the longer
subcarrier interval and shorter time slot. In the time domain,
the length of a NR subframe is 1 ms, and the number of time
slots in each subframe is integer.
As shown in Fig. 2, the subframe is used as the minimum
unit of resource allocation for JSCIS. We design a P/Q
adjustable frame format consisting of P sensing subframes and
Q communication subframes. Considering the latency sensitive
radar information requirements in the practical scenario, all
the information detected by radar in different CAVs need to
be transmitted within the next communication subframe.
Taking into account different delay sensitivities of com-
munication data, it is necessary to adopt a ﬂexible time slots
allocation algorithm in the communication subframe based
on the 5G NR frame structure. Compared with 4G LTE
system, the frame structure of 5G NR system is more ﬂexible,
where the mini-slot can meet the low-latency transmission
requirements and support the small data packet transmission.
The mini-slot can carry not only fewer OFDM symbols
than ordinary time slots, but also the control information
[24]. Therefore, we propose a ﬂexible multi-slot combination
strategy to realize the transmission of control information,
sensing information, emergency information, and etc. When
the emergency information needs to be transmitted, such as
a car accident within a short distance ahead or pedestrians
suddenly crossing the road, the adjustable mini-slots are used
to achieve the low-latency transmission. For the ordinary data
information transmission, the ordinary time slots are used. The
low-latency and high-reliability information can be transmitted


---

Page 4

---

4
Table I. Symbols and deﬁnitions.
Symbol
Deﬁnition
Ns
Number of subframes in each scheduling cycle
N
Number of vehicles
an
Normalized radar sensing duration series
Ii
Time allocation index of vehicle i
nr−com
Communication interference from other vehicles to radar signal of vehicle i
nr−rad
Radar interference from other vehicles to radar signal of vehicle i
nc−com
Communication interference from other vehicles to communication signal of vehicle i
nc−rad
Radar interference from other vehicles to communication signal of vehicle i
ht
i,i
Propagation gain for the radar i-target-radar i path
ht
i,j
Propagation gain for the radar j-target-radar i path
Gt
Antenna gain at transmitter
Gr
Antenna gain at receiver
σRCS
i,i
Radar Cross Section from target to radar i
σRCS
i,j
Radar Cross Section from radar j to radar i
Ri
Distance from radar i to target
Rj
Distance from radar j to target
Pj
Transmit power of vehicle j
gch−r
i,i
Fading gain of vehicle j in communication duration to vehicle i in radar duration
γrad
i
SINR of vehicle i in radar duration of ¯an −¯an−1
γcom
i
SINR of vehicle i in communication duration of ¯an −¯an−1
in the communication subframe through the proposed P/Q
adjustable frame format and mini-slot methods.
C. System Performance Evaluation Indicators
To evaluate the performance of the proposed JSCIS, the
performance metrics are proposed as follows. The radar sys-
tem is designed to reduce the prior uncertainty of target by
measuring and obtaining the target information. According to
information theory, the larger the MI, the more information
about the target can be obtained via measurements. Related
researches have found that maximizing MI can effectively
improve the target recognition ability of radar system in
[25] and [26]. Therefore, to evaluate the performance of
radar system, MI between the target response and the radar
received signal is used as the metric for the radar estimation
performance.
1) Radar Metric: For a radar system, the baseband re-
ceived signal model is established as
y = shrad + n,
(1)
where y denotes the received signal, hrad is the propagation
gain of radar response signal in the channel, and n is the
interference to the signal receiver (including internal thermal
noise and other external signal interference). In order to
compare the performance of radar and communication in the
same dimension, we introduce the radar mutual information
(MI) as the metric of radar signal design [27] to measure
radar performance from the perspective of communication. In
the communication system, the mutual information between X
and Y refers to the amount of information in X containing Y
or the amount of information in Y containing X. Therefore,
the meaning of radar MI is the information amount of channel
state information contained in the radar received signal. The
goal in this paper is to maximize the utilization of MI.
Therefore, we use MI to characterize the information amount
of channel state information contained in the radar received
signal in this paper, as I (y; h) in
Irad (y; hrad) = H (y) −H (y|hrad) = H (y) −H (n)
= log
 1 + shrad
n

.
(2)
2) Communication Metric: For a communication system,
the channel capacity of an Additive White Gaussian Noise
(AWGN) channel is deﬁned as the maximum information
transmission rate based on Shannon’s theorem in [28] as
Ccom = Blog2 (1 + Γcom) ,
(3)
where B represents the system bandwidth, Γcom represents
the signal to interference plus noise ratio (SINR). According
to information theory, the channel capacity is the supremum of
all achievable rates, which can also be deﬁned as the maximum
MI. Based on [29], the communication channel capacity during
T time can be expressed as
Icom = T·Blog2 (1 + Γcom) .
(4)
D. Problem Formulation
The mmWave communication system uses the narrow
beam to minimize the interference, making it possible for each
vehicle to conﬁgure sensing and communication durations
dynamically. In the proposed dynamic frame structure, each
vehicle adopts a non-uniform frame which can adjust the
time allocation for radar and communication according to


---

Page 5

---

5
Radar Duration
Communication Duration
Communication to Radar Interference
Vehicle Number
Sensing Duration Ratio
Radar to Radar Interference
Fig. 3. Interference analysis in the radar duration of JSCIS.
different requirements. When the cross-interference between
radar detection and communication transmission in CAVs is
serious, this solution can also be degraded into a uniform
time allocation strategy. Without loss of generality, we for-
mulate and analyze the objective function of non-uniform
time resource allocation scheme based on the dynamic frame
structure.
The frame length of JSCIS is ﬁxed, and the sensing
duration of each vehicle can change dynamically according
to the sensing and communication requirements. Assuming the
number of vehicles in the multi-vehicle cooperative scenario is
N, there are Ns subframes in each scheduling cycle. We deﬁne
an ∈A = [a1, a2, · · · , aN] as the radar sensing normalized
duration series for all vehicles, where n represents the time
index. The set of values for an is Ωt = [ 1
Ns ,
2
Ns , · · · , Ns−1
Ns ].
The sensing duration of each vehicle is arranged in an as-
cending order and renumbered as ¯an = [¯a1, ¯a2, · · · , ¯aN],
where ¯a1 and ¯aN are the smallest and the biggest normalized
sensing durations, respectively. At the same time, two addi-
tional constants are introduced, ¯a0 = 0 and ¯aN+1 = 1. The
index collection of these sensing duration series can be set as
I = [I1, I2, · · · , IN], where Ii represents the time allocation
index of vehicle i.
Based on the time-division frame structure in Fig. 2, the
interference analysis among vehicles is based on the synchro-
nization among vehicles, which is feasible and supported by
the Primary Synchronization Signal (PSS) and Secondary Syn-
chronization Signal (SSS) within the 5G NR communication
system in [38] and [42]. Therefore, the interference among
vehicles in the radar and communication durations is analyzed
as follows, based on the non-uniform time allocation scheme
in JSCIS.
1) Signal Analysis During Radar Detection Process: As
shown in Fig. 3, in the radar duration ¯an −¯an−1 of vehicle
i, and the time index 1 ≤n ≤Ii, there are two types
of interference, where the other vehicles are denoted by j
and j′. The radar signal of vehicle i will be interfered by
the communication signal of other vehicles when the index
of other vehicles is smaller than n. And when the index of
other vehicles is bigger than n, vehicle i will experience the
radar signal interference from other vehicles. Therefore, during
Fig. 4. The propagation gain of radar path in the CAV scenario.
the radar detection process, the radar received signal can be
described as
yrad = sradhrad + nr−com + nr−rad + n,
(5)
where nr−com is the interference caused by communication
signals from other vehicles to radar signals of vehicle i, and
nr−rad is the interference caused by radar signals of other
vehicles to radar signal of vehicle i.
There are two main paths for radar signal propagation,
namely the reﬂection path and the refraction path. The corre-
sponding path propagation gain is as follows



ht
i,i =
GtGrσRCS
i,i
λ2
(4π)3R4
i
,
ht
i,j =
GtGrσRCS
i,j
λ2
(4π)3R2
i R2
j ,
(6)
where ht
i,i represents the propagation gain for the radar i-
target-radar i path, and ht
i,j represents the propagation gain
for the radar j-target-radar i path. The detailed diagram is
showed in Fig. 4.
Considering the narrow beam of the mmWave communi-
cation system, the main lobe gain is used for the interference
analysis. Gt and Gr represent the antenna transmitting gain
and the antenna receiving gain. σRCS
i,i
represents the Radar
Cross Section (RCS) from target to radar i, σRCS
i,j
represents
the RCS from radar j to radar i, λ represents the wave length,
Ri represents the distance from radar i to target, and Rj
represents the distance from radar j to target. It is also assumed
that all channel gains are ﬁxed during current observation time.
Assuming that vehicle j is the interfering vehicle, when
the index of vehicle j is smaller than n, the communication
interference from vehicle j to vehicle i during the radar
sensing duration ¯an −¯an−1 of vehicle i is deﬁned by
nr−com
i
=
X
j∈Nn
PjGtgch−r
i,j
Gr,
(7)
where Pj is the signal transmission power of vehicle j, and
gch−r
i,j
represents the path loss of the communication signal of
vehicle j transmitted from vehicle j to vehicle i during the
communication duration. Nn is the vehicle set with the time
allocation index number smaller than n, and N is the set of
all vehicles’ time indexes.


---

Page 6

---

6
Communication to Communication Interference
Radar Duration
Communication Duration
Vehicle Number
Sensing Duration Ratio
Radar to Communication Interference
Fig. 5. Interference analysis in the communication duration of
JSCIS.
When the index of vehicle j is bigger than n, the radar
interference on vehicle i during the radar sensing duration
¯an −¯an−1 of vehicle i is
nr−rad
i
=
X
j∈N\Nn
Pjht
i,j,
(8)
where N\Nn denotes the vehicle set with the time allocation
index bigger than n.
Combining two types of interference above, the SINR of
vehicle i in the radar duration ¯an −¯an−1 can be expressed as
γrad
i
=
Piht
i,i
nr−rad
i
+ nr−com
i
+ N0B
,
(9)
where N0 and B represent the power spectral density of
background noise and the mmWave band bandwidth of JSCIS.
Furthermore, the radar MI for vehicle i in the radar sensing
duration can be expressed as
Irad
i
 y; ht
i,i

= H (y) −H
 y|ht
i,i

= log
 1 + shrad
n

= H (y) −H
 nr−com
i
+ nr−rad
i
+ n

,
(10)
which can be further written as
Irad
i
 y; ht
i,i

=
Ii
P
n=1
(¯an −¯an−1) log
 1 + γrad
i

.
(11)
Considering the cooperative sensing of N vehicles, the
total radar MI is
Irad =
N
X
i=1
Irad
i
.
(12)
2) Signal Analysis During Communication Transmission
Process: In Fig. 5, for the communication part of vehicle i, we
assume that vehicle j can communicate with vehicle i. In the
duration ¯an+1 −¯an of vehicle i, where Ii ≤n ≤N, there are
two types of interferences, and the other vehicles are denoted
by k and k′. Vehicle i will experience the communication
signal interference from other vehicles, when the index of
other vehicles is smaller than n. When the index of other
vehicles is bigger than n, vehicle i will experience the radar
signal interference from other vehicles. Thus, the received
communication signal is depicted by
ycom = scomhcom + nc−com + nc−rad + n,
(13)
where nc−com is the interference caused by communication
signals of other vehicles to communication signals of vehicle
i, and nc−rad is the interference caused by radar signals of
other vehicles to communication signals of vehicle i.
Assuming that vehicle k is the interfering vehicle, when
the time allocation index of vehicle k is smaller than n, the
communication interference of vehicle k to the current vehicle
i in the communication duration can be expressed as
nc−com
i
=
X
k∈Nn,k̸=j
PkGtgch
i,kGr,
(14)
where Pk is the signal transmission power of vehicle k, and
gch
i,k represents the path loss from vehicle k to vehicle i.
When the index of the vehicle k is bigger than n, the radar
interference from vehicle k in the radar duration to vehicle i
in the communication duration is
nc−rad
i
=
X
k∈N \Nn,k̸=j
Pk
GtGrλ2
(4π)2d2
i,k
,
(15)
where di,k represents the distance between vehicle i and
vehicle k.
Combining these two types of interferences, the SINR of
vehicle i in the communication duration ¯an+1 −¯an can be
expressed as
γcom
i
=
PiGtgch
i,jGr
nc−com
i
+ nc−rad
i
+ N0B
.
(16)
Then, the communication rate of vehicle i is deﬁned by
Rcom
i
= B
N
X
n=Ii
(¯an+1 −¯an)log2(1 + γcom
i
).
(17)
Therefore, the communication channel capacity can be
expressed as
Icom
i
= (1 −aIi) T · B
N
X
n=Ii
(¯an+1 −¯an) log2 (1 + γcom
i
).
(18)
Considering the cooperative sensing of N vehicles, the
total communication channel capacity is
Icom =
N
X
i=1
Icom
i
.
(19)
3) AoI Analysis: AoI stands for the timeliness of informa-
tion, which should be as small as possible to meet the service
requirements [18]. In this paper, to evaluate the timeliness of
raw sensing data sharing among vehicles and RSUs, we use
AoI to model the performance of M/M/1 queuing problem to
achieve the best time duration allocation ratio for sensing and
communication dual functions for each vehicle in the proposed
CAV scenario. Furthermore, we analyze the effects of different
duration allocation ratios on the packet loss probability and the
average AoI.


---

Page 7

---

7
Fig. 6. Status update age for a system with a FCFS queue.
Source 1
ĂĂ
Ă
Destination
Λ 
queue
Δ 
Source M
Fig. 7. The FCFS queue model of multiple sources to one
destination with packet loss.
Fig. 6 shows a sample variation of AoI ∆(t) as a function
of time t. The ﬁrst status update is generated at t1, followed
by updates at t2, t3, . . . , tm. AoI at time t is deﬁned as
∆(t) = t−u (t), where the u (t) is the timestamp of the most
recent information at the receiver. X is the interval between
two arrived updates, and T is the time of one update served in
the system. Both X and T are random variables. The average
AoI can be calculated during the observation interval (0, τ) as
[18]
⟨∆i⟩τ = lim
τ→∞
1
τ
Z τ
0
∆(t) dt,
(20)
which can be further converted to
∆i = Λ
1
2E

X2
+ E [XT]

.
(21)
The information system in this paper is assumed as a
centralized network of multi-source status update with packet
loss, in which all vehicles transmit their detection informa-
tion via the communication links to the central vehicle. As
shown in Fig. 7, the FCFS queue model of multiple sources
i = 1, 2, . . . , N with packet loss is depicted. The FCFS
scheduling strategy can effectively ensue the timeliness of
the radar detection information transmission. Considering the
timeliness requirement of information transmission between
vehicles as well as the cache and computation capacities
of vehicles, the computation model is modeled as a typical
M/M/1 queue based on [30], and each vehicle only carries out
serial calculation for task packets. The sources generate data
packets according to a Poisson process with an arrival rate Λ.
The service time for each packet is exponentially distributed
with the service rate µ. The server load rate is ρ=Λ/µ. In
[31], the average AoI for the M/M/1 queue is given by
∆i = 1
µ

1 + 1
ρ +
ρ2
1 −ρ

.
(22)
In the communication system, the packet is successfully
transmitted only if the SINR at the receiver does not fall below
a threshold γc. Combined with the interference analysis in
Section II-B, the success transmission probability p can be
expressed as
p = P

min
i∈{1,2,...,N} γcom
i

> γc

.
(23)
Based on [32], (23) can be simpliﬁed as
p = exp

−
 ϕ
2π
2
aλπ
 γc
d−α
 2
α 
,
(24)
where ϕ is the width of the main lobe of antenna, which
is ﬁxed to π/6, a is the time allocation ratio, λ is the net-
work density. We assume that vehicles follow a homogeneous
Poisson point process with the intensity λ. d is the distance
between vehicles, which is limited to 200 m. And the packet
loss rate is 1 −p.
Considering the packet loss probability, the server load rate
ρ turns to ρ′ = p Λ
µ , and the average AoI of M/M/1 queue
(22) turns to
∆i = 1
µ

1 + 1
ρ′ +
ρ′2
1 −ρ′

.
(25)
4) Objective Function: According to the existing research,
the using of current mmWave on-board radars in the middle
and high frequency bands can obtain the location information
of vehicles accurately, such as distance and direction, which
can be used to establish the vehicle network topology via
the communication links among vehicles. In [33], a new
millimeter-wave distance-measurement sensor prototype was
developed for the ﬁrst time, and small errors between mea-
sured and actual distances were achieved. The mmWave radar
can obtain the network topology through detecting with low
transmission power and small absolute error, then the detection
information can be transmitted to the central vehicle via
communication links. The optimized beam can be determined
by the beam training algorithm [34]. The performance opti-
mization of JSCIS is a multi-objective (dual-objective) prob-
lem that optimizes both radar and communication systems’s
performance at the same time. The solution to this problem is
to obtain the Pareto optimality for the objective function.
To maximize the amount of information detected by radars,
the performance optimization of JSCIS can be modeled as


---

Page 8

---

8
a maximization problem of radar total MI with the com-
munication channel capacity as a constraint. Therefore, the
optimization problem can be deﬁned as
max
a
Irad
s.t.
C1 : an ∈Ωt, ∀n,
C2 : Irad
i
≤Icom
i
,
C3 : ∆i ≤∆max
i
,
(26)
where constraint C1 provides the available radar duration
set for each vehicle, constraint C2 is to guarantee that the
radar information of each vehicle can be efﬁciently transmitted
within the communication time of T, constraint C3 is used to
ensure that the data transmission efﬁciency is below a certain
threshold in case of a success packet transmission.
III. TIME RESOURCE ALLOCATION METHOD BASED ON
NON-COOPERATIVE GAME
The resource allocation optimization problem for multiple
CAVs is formulated as a non-cooperative game, and the
feasibility and existence of the pure strategy NE are proved.
To achieve the NE of the non-cooperative game problem, we
proposed the CTRA algorithm, and the convergence of the
CTRA algorithm is also proved theoretically.
A. The Formulation of the Non-cooperative Game
It can be observed that the optimization problem of JSCIS
is combinatorial and non-convex. The combinational nature
comes from the constraint C1. Based on the constraint C2
in (26), the problem is non-convex. Although the exhaus-
tive method can obtain the optimal time resource allocation
strategy, it is computationally infeasible for CAVs and also
not effective for the system design. In order to reduce the
computational complexity and select a suitable resource al-
location strategy, we propose a utility function and use the
non-cooperative game method to solve this problem.
The duration occupied by radar process will affect the time
allocation and the information transmission in the communi-
cation process, and vice versa. Therefore, the optimal time
allocation problem of JSCIS is deﬁned as a non-cooperative
game problem as
G =

K, {Am}m∈K, {Um}m∈K

,
(27)
where K = {1, 2, · · · , N} is the set of players (i.e., vehicles in
the CAVs scenario). Am is the set of available pure strategies
for all players m, and Um = U is the utility function of player
m.
The goal of each player is to maximize its own util-
ity function by choosing a suitable time allocation strategy.
Considering the objective function and constraints, the utility
function can be deﬁned as
U = Irad + η
N
X
i=1
Φ(Icom
i
, Irad
i
),
(28)
where η is the penalty scalar whose unit is “bps”, and Φ(x, y)
is the penalty function, which satisﬁes that Φ(x, y) = −1,
if x < y, and Φ(x, y) = 0, if x ≥y. It is worth noting
that the ﬁrst term in (28) corresponds to the radar total
MI, and the second term in (28) indicates the limitation of
the communication channel capacity. If the communication
channel capacity is smaller than the radar MI, the utility
function will be punished.
Under the condition that η > max Irad and each player
has a feasible solution that satisﬁes the constraints C1 and C2,
there will be U < 0 if an arbitrary player chooses a strategy
that violates the constraint C2. It means that any strategy
proﬁles violating the constraint C2 will never be the optimal
solution. Therefore, the optimal solution for maximizing U is
equivalent to the optimal solution of the objective function in
(26).
Let Am ∈Am denotes the strategy of player m, and
A−m ∈A1 × · · · × Am × · · · AN represents the strategy
proﬁles of all players excluding player m, where × is the
Cartesian product. In this paper, Am = am represents the
radar duration proportion of vehicle m in each frame. Given a
strategy of an arbitrary player m, Am ∈Am, and an alternative
strategy A′
m ∈Am, while the strategies of other players
remain unchanged, then we have
Um(Am, A−m) −Um(A′
m, A−m)
= U(Am, A−m) −U(A′
m, A−m).
(29)
The formulated game G is a potential game with the
potential function U. The selection of each player’s strategy
can be mapped into the potential function. According to the
properties of potential games, each potential game has at
least one pure strategy Nash equilibrium (NE). If there is
no constraint C2, each NE of game G will be the solution.
However, due to the constraint C2, whether a pure strategy NE
exists or not is unclear. Therefore, the existence of feasible NE
for the proposed game G need to be proved. To simplify the
subsequent proof and derivation process, the maximum radar
MI is deﬁned as ˜η = max Irad.
B. The Feasibility of Pure Strategy Nash Equilibrium
Assuming that there are enough time slots for each
scheduling cycle, we analyze the feasibility of pure strategy
NE for the proposed game.
Deﬁnition 1 (Pure Strategy NE): The strategy proﬁle
(A∗
1, . . . , A∗
N) is a pure strategy NE of G. If any m ∈K
has an alternate Am ̸= A∗
m, the following conditions will be
always true for all Am ∈Am [35],
Um(A∗
m, A∗
−m) ≥Um(Am, A∗
−m).
(30)
Theorem 1. If η ≥˜η , each scheduling cycle consists of
enough time slots, and there is no impact on other vehicles
when each participating vehicle adjusts its time allocation
under the constraint C2. Then the pure strategy NE of the
proposed game G must be feasible.
Proof. Assume that the strategy proﬁle (A∗
1, . . . , A∗
N), which
violates the constraint C2, is a pure strategy NE of G. Then,
there must be some vehicles whose communication channel
capacity is smaller than radar MI. We denote these vehicles


---

Page 9

---

9
by player m′ (1 ≤m′ ≤N). Since we assume that each
scheduling cycle consists of enough time slots, player m′ must
be able to choose another strategy A′
m′ with a smaller radar
detection duration to make its radar MI be smaller than the
communication data information. Then, we have
Um′(A∗
m′, A∗
−m′) −Um′(A′m′, A∗
−m′)
= Irad(A∗
m′, A∗
−m′) −Irad(A′m′, A∗
−m′)
+η[
N
P
i=1
Φ(Icom
i
(A∗
m′, A∗
−m′), Irad
i
(A∗
m′, A∗
−m′))
−
N
P
i=1
Φ(Icom
i
(A′m′, A∗
−m′), Irad
i
(A′m′, A∗
−m′))]
= Irad(A∗
m′, A∗
−m′) −Irad(A′m′, A∗
−m′) −η < 0.
(31)
Apparently,
(31)
contradicts
the
assumption
that
(A∗
1, · · · , A∗
N) is a pure strategy NE of G. Therefore,
the pure strategy NE of G must be feasible if the conditions
of this theorem hold, which concludes this proof.
According to Theorem 1, the solution of game G that
meets certain conditions is feasible, which means that when
certain conditions are not met, not all pure strategies NE can
work. Therefore, the existence of pure strategies NE of G is
described below.
C. The Existence of pure strategy Nash Equilibrium
Theorem 2. If η ≥˜η and each scheduling cycle consists
of enough time slots, the proposed game G has at least one
feasible pure strategy NE.
Proof. Following
the
proof
in
[36],
we
assume
that
(A∗
1, . . . , A∗
N) can maximize U. If these conditions hold, then
we have U (A∗
1, . . . , A∗
N) > 0. If (A∗
1, . . . , A∗
N) is infeasible,
we have U (A∗
1, . . . , A∗
N) < 0, which contradicts the above
inequality. Hence, (A∗
1, . . . , A∗
N) must be feasible, and we
have U(A∗
1, · · · , A∗
N) = Rrad(A∗
1, · · · , A∗
N), when η ≥˜η
holds. Since U(A∗
1, · · · , A∗
N) satisfy
U(A∗
1, · · · , A∗
N)
≥U(A1, · · · , AN), ∀(A1, · · · , AN) ∈{Am}m∈K,
(32)
then we have Rrad(A∗
1, · · · , A∗
N) ≥Rrad(A1, · · · , AN) for
any feasible strategy proﬁle (A1, . . . , AN) with the condi-
tions of Theorem 2. Therefore, (A∗
1, . . . , A∗
N) is the opti-
mal solution to the objective function. Obviously, there is
no other feasible strategy proﬁle that can further improve
the utility function, which means that no strategy proﬁles
(A1, · · · , AN) ∈{Am}m∈K satisﬁes
Um(A1, · · · , AN) = U(A1, · · · , AN)
> Um(A∗
1, · · · , A∗
N) = U(A∗
1, · · · , A∗
N), ∀m ∈K.
(33)
Suppose for ∀m ∈K, if Am ∈Am and Am ̸= A∗
m is
other strategies of player m, then
Um(Am, A∗
−m) ≤Um(A∗
m, A∗
−m).
(34)
Algorithm 1 Centralized Time Resource Allocation (CTRA)
Algorithm
1: Initialization: Initialization strategy Am = Ωt(1), 1 ≤
m ≤N, iteration number t = 0, Umax = 0;
2: repeat
3:
for m = 1 : N
4:
At+1
m
= argmax
Am∈Am
Um(Am, A−m);
5:
if U > Umax
6:
update At
m=At+1
m , Umax = U;
7:
end for
8:
update t = t + 1.
9: until Um(At
m, At
−m) = Um(At−1
m , At−1
−m), ∀m ∈K.
10: return (Am, A−m).
Similarly, no players can unilaterally change their strate-
gies to improve the utility. Therefore, according to the deﬁni-
tion of NE, (A∗
1, · · · , A∗
N) is the pure strategy NE of G, which
concludes this proof.
Theorem 2 denotes that there is at least one feasible pure
strategy NE. If there is a single pure strategy NE, the only
pure strategy NE must be the Pareto optimal solution when
the condition of Theorem 2 holds.
D. CTRA Algorithm Design Based on Non-cooperative Game
According to the above analysis, based on the best strat-
egy game, a low-complexity CTRA algorithm is designed to
achieve the pure strategy NE. Assuming that m represents
the total number of iterations, n represents the number of
vehicles, and p represents the number of sub-frames contained
in each frame, the algorithm needs to calculate n × p times
of utility function for each iteration. Therefore, the algorithm
complexity can be expressed by O (mnp).
Since not all pure policy NEs of game G are feasible, it is
necessary to start Algorithm 1 from a feasible strategy proﬁle
to ensure that it can converge to a feasible pure policy NE.
Therefore, the initial detection duration for each vehicle is set
to be the minimum in its available duration set, which ensures
that the initial strategy proﬁle is feasible under previous
assumption. Based on the proof in [36], the convergence of
Algorithm 1 can be proved.
Theorem 3. If η ≥˜η and each scheduling cycle consists of
enough time slots, the proposed Algorithm 1 converges to a
feasible pure strategy NE of G in ﬁnite steps from any initial
feasible strategy proﬁles.
Proof. Starting from any initial feasible strategy proﬁles,
according to the best response procedure, we have
Um(At+1
m , At
−m) −Um(At
m, At
−m) > 0, ∀m ∈K,
(35)
which states that the utilities of all players are strictly in-
creasing in each iteration of CTRA. Suppose that U ∗is the
maximum value of U, we have U ∗< ∞, since the number
of each player’s strategies and the number of players are both


---

Page 10

---

10
Table II. Key simulation parameters of JSCIS.
Parameter
Value
Carrier frequency
28 GHz
System bandwidth B
800 MHz
Thermal noise power spectral density N0
-174 dBm/Hz
Shadow fading standard deviation
8 dB
Transmit power
10 W
Tx/Rx antenna gain
18 dB
Communication SINR threshold γc
5
Distance between vehicles
200 m
Normalization parameter ˜η
10 Gbps
Maximum acceptable average AoI ∆max
i
4
ﬁnite. Moreover, the proposed game G is a potential game with
the potential function U, then we have
Um(At+1
m , At
−m) −Um(At
m, At
−m)
= U(At+1
m , At
−m) −U(At
m, At
−m), ∀m ∈K.
(36)
According to (35) and (36), we can conclude that each
update of a player’s strategy at each iteration will result in a
strictly increasing quantity of U. Since U ∗< ∞, then there
must exist a t∗(0 ≤t∗< ∞) such that Um(At∗
m, At∗
−m) = U ∗,
when t∗is sufﬁciently large. That is, the strictly increasing
procedure of the proposed CTRA algorithm converges within
ﬁnite steps, which concludes this proof.
IV. RESULTS AND ANALYSIS
Both software simulation and hardware testbed are de-
signed and developed to verify the feasibility of the proposed
JSCIS and the performance of the CTRA algorithm. The effect
of different time duration ratios on packet loss probability and
average AoI is simulated and analyzed. Besides, by comparing
the performance of different algorithms, the solution of the
time resource allocation optimization problem is veriﬁed and
the performance of the proposed algorithm under different
impact factors is evaluated with discussions in detail. Finally,
the hardware testbed is setup and results are analyzed to verify
the feasibility of the proposed JSCIS.
A. Software Simulation Setup and Results Analysis
The key simulation parameters are listed in Table II. The
antenna gains of transmitter and receiver of radar system are
the same as those of communication system, which are set
to 18 dB inside the main lobe beamwidth of ϕ. The transmit
power of communication and radar systems is set to 10 W [37].
According to the link budget analysis, the maximum distance
between vehicles is set to 200 m to ensure the effective radar
detection and communication. The number of subframes Ns
in each frame is set to 14 based on [38]. The JSCIS operates
at 28 GHz, and the bandwidth is 800 MHz [38]-[39]. The
normalization parameter ˜η in the CTRA algorithm is 10 Gbps.
We assume that the RCS model of radar system has a uniform
reﬂectivity, which is σRCS = 1.
10-4
10-3
10-2
10-1
100
Network Density 
10-1
100
Packet Loss Probability 1-p
a=0.1
a=0.2
a=0.3
a=0.4
a=0.5
a=0.6
a=0.7
a=0.8
a=0.9
Fig. 8. The change of packet loss rate under different time
allocation ratios.
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
Load Rate 
2
2.5
3
3.5
4
4.5
5
5.5
6
Average AoI 
a=0.1
a=0.2
a=0.3
a=0.4
a=0.5
a=0.6
a=0.7
a=0.8
a=0.9
Fig. 9. The change of average AoI under different time
allocation ratios.
The inﬂuence of different time allocation ratio and network
density on the packet loss rate are shown in Fig. 8. And
the number of vehicles is set to 10. As the network density
increases, the packet loss rate gradually increases, and the
performance of communication system decreases. When λ >
10−2, the performance of communication system deteriorates,
and the packet loss rate is approaching 1. Moreover, when
the network density is constant, with the increase of time
allocation ratio, the packet loss rate also increases. When
a = 0.1, the communication performance is the best.
The relationship among average AoI ∆, time ratio a and
server load rate ρ′ is shown in Fig. 9. With the increase
of allocation ratio, the average AoI decreases. When a =
0.1, 0.2, 0.3, 0.4, the average AoI can satisfy the limit of the
maximum average AoI. Therefore, based on the analysis of
packet loss probability and AoI, the time allocation ratio is
limited from 0.1 to 0.4, while considering the size limit of


---

Page 11

---

11
10
20
30
40
50
60
70
80
90
100
Number of Interations
5.5
6
6.5
7
7.5
8
8.5
Radar Total Mutual Information(bit)
108
Global Optimal
CTRA
(a)
50
100
150
200
250
Number of Interations
0.8
1
1.2
1.4
1.6
1.8
2
Radar Total Mutual Information(bit)
109
Global Optimal
CTRA
(b)
Fig. 10. Convergence of proposed CTRA algorithm with
different number of vehicles. (a) N = 5, (b) N = 10.
radar information rate simultaneously.
Fig. 10 shows the convergence performance of the pro-
posed CTRA algorithm in the case of a small number of
vehicles N = 5, and a large number of vehicles N = 10.
The initial time allocation strategy of all vehicles is set to the
minimum value am = 0.1 to ensure that a feasible optimal
solution can be achieved. The simulation results show that the
radar total MI increases with the increase of iterations. After
a limited number of iterations, the system is stable, which
can achieve a stable and feasible strategy. When the vehicle
group size is large in Fig. 10(b), the convergence speed of
the proposed CTRA algorithm is lower than that of the small
vehicle group in Fig. 10(a), and the radar total MI is higher
than that of the small vehicle group.
Fig. 11 shows the conﬁguration of the radar MI and
the communication channel capacity of an isolated vehicle
under the optimal allocation of time resources of the CTRA
algorithm when N = 10. Although the radar MI and the com-
1
2
3
4
5
6
7
8
9
10
Vehicle Number
0
2
4
6
8
10
12
14
16
Radar Mutual Information(bit)
107
0
0.5
1
1.5
2
2.5
3
3.5
4
Communication Channel Capaciity(bit)
109
Radar
Communication
Fig. 11. The radar mutual information and communication
channel capacity allocation using CTRA algorithm.
5
10
15
Numbers of Vehicle
0
2
4
6
8
10
12
Radar Mutual Information(bit)
108
Unified Allocation
Random Allocation
ABSA[40]
CTRA
Fig. 12. Comparison of the radar total mutual information
under different number of vehicles.
munication channel capacity of each vehicle are different, the
optimal time allocation scheme can meet the restrictions that
the amount of radar MI of each vehicle is less than the amount
of communication channel capacity, which means that the
information detected by each vehicle’s radar can be efﬁciently
transmitted within the communication duration. And under
the current mmWave system parameters, the communication
channel capacity of an isolated vehicle can reach more than
3.5Gbits, and additional data can be transmitted according to
the task requirements, which can support the high data rate
transmission.
In order to verify the effectiveness and superiority of the
CTRA algorithm for the time resource allocation of JSCIS,
the performance comparison and evaluation of typical time
resource allocation methods are performed, including the
uniform time allocation method, the random time resource
allocation strategy, the simulated annealing method (ABSA)
[40], and the proposed CTRA algorithm in this paper. In


---

Page 12

---

12
5
10
Numbers of Scheduling Cycles Ns
0
2
4
6
8
10
12
14
Radar Mutual Information(bit)
108
Unified Allocation
Random Allocation
ABSA[40]
CTRA
Fig. 13. Comparison of radar total mutual information under
different scheduling cycles.
the uniform time allocation method, each vehicle adopts the
same duration allocation ratio, which is lack of ﬂexibility. It is
worth noting that the uniform allocation and random allocation
strategies may result in a negative value for the ﬁnal utility
function. Furthermore, a time allocation strategy to make the
radar total MI positive is selected for performance comparison
in the simulation. Fig. 12 compares the performance of several
typical time resource allocation methods for different numbers
of vehicles, and evaluates the performance of different algo-
rithms based on the radar total MI. The higher the radar total
MI, the better the ﬁnal utility. The results show that the CTRA
algorithm has a better performance than other algorithms,
which can achieve a higher radar total MI and improve the
performance of communication system. The random allocation
method has a large contingency, with no obvious advantages
compared with the uniform allocation method. However, other
algorithms using non-uniform time allocation are better than
the uniform time allocation. The ABSA method can also
improve system performance to some extent, but it is slightly
inferior to the proposed CTRA algorithm. Speciﬁcally, com-
pared with the ABSA method, the proposed CTRA algorithm
can increase the radar total MI by 40%, 26.29%, and 14.53%
when the number of vehicles is 5, 10, and 15, respectively.
In order to compare the effect of different Ns on various
algorithms in a scheduling cycle, taking the practical frame
structure of 10 ms into account, the number of subframes is
set to 5 slots and 10 slots, respectively. As shown in Fig. 13,
regardless of the value of Ns, excluding the random allocation,
the radar total MI obtained by the non-uniform time allocation
method is much better than the uniform allocation strategy.
With the increase of Ns, the radar total MI obtained by
different time allocation strategies increases. Therefore, the
current system using Ns = 10 can obtain a better performance,
making the overall system the highest utility.
To evaluate the effect of different radar RCS conﬁgurations
on the performance of various algorithms, four cases are
considered as follows. Case 1 sets all σRCS = 1; Case 2
Case 1
Case 2
Case 3
Case 4
Radar RCS Configuration
0
2
4
6
8
10
12
14
16
18
Radar Mutual Information(bit)
108
Unified Allocation
Random Allocation
ABSA[40]
CTRA
Fig. 14. Comparison of radar total mutual information under
different radar RCS conﬁgurations.
sets the RCS of radar i itself to σRCS = 1, and the RCS
between different radars is σRCS = 0.5; Case 3 sets the RCS
of radar i itself to σRCS = 1, and the RCS between different
radars is σRCS = 2; Case 4 sets the RCS of radar I itself
to =1, and the RCS between different radars randomly takes
a value from 0.5 to 2. The simulation results are shown in
Fig. 14. All the algorithms in Case 2 can achieve the highest
radar total MI, and the performance of the proposed CTRA
algorithm is much better than other algorithms, while Case 3
has the lowest radar total MI. The performance of Case 1 and
Case 4 are among the middle of all four cases, where Case 1 is
slightly better than Case 4. Result shows that when the RCS
of the current vehicle is smaller than that of other vehicles
to the current vehicle i, the system impact on the current
radar duration is also relatively small, and a larger radar total
MI can be obtained. When the RCS of other vehicles on the
current vehicle is large, radar interference will increase, and
the radar total MI will be severely reduced. To sum up, in
order to achieve a better performance, the impact of other
radars on the current radar should be minimized in the practical
implementation process.
To analyze the convergence of the proposed CTRA, Fig.
15 shows the time resource allocation strategy of each vehicle
with N = 10 as a function of the number of iterations. Due
to the large number of vehicles, 10 vehicles are divided into
two sub-graphs. It can be observed that the optimal time
resource allocation strategy can be expressed as 0.9, 0.1,
0.1, 0.4, 0.6, 0.8, 0.3, 0.6, 0.3, 0.9 in the order of vehicle
series 1-10. When the initial time is allocated as a minimum
conﬁguration, each vehicle is selected in turn for optimization,
and the strategy is updated according to the proposed CTRA
algorithm. As the number of iterations increases, each vehicle
continuously optimizes its own time conﬁguration. Finally, the
CTRA algorithm is converged to the optimal time resource
allocation strategy within 85 iterations.
In summary, the software simulation results prove that
the best time duration allocation ratio for one vehicle can be


---

Page 13

---

13
0
20
40
60
80
100
120
Number of Iterations
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
vehicle1
vehicle2
vehicle3
vehicle4
vehicle5
(a)
0
20
40
60
80
100
120
Number of Iterations
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
vehicle6
vehicle7
vehicle8
vehicle9
vehicle10
(b)
Fig. 15. The status of changes of isolated vehicle’s time
resource allocation strategy with iterations. (a) Vehicle number
1-5, (b) Vehicle number 6-10.
achieved based on the analysis of queuing theory and AoI in
Section II. In the multiple CAVs condition, the convergence of
the proposed CTRA algorithm and the existence of the stable
allocation ratio set for CAVs are proved. The proposed CTRA
algorithm can ensure that all the radar sensing information
can be efﬁciently transmitted in the communication duration.
The performances of CTRA algorithm under different impact
factors are also analyzed.
B. Hardware Setup and Testbed Results Analysis
In order to realize the radar detection function in the
perception phase of sensing and communication integrated
system, the radar data frame is added to 5G NR mmWave
communication frame. And the JSCIS hardware testbed is
setup in the 28 GHz mmWave frequency band, which consists
of two NI 5G mmWave communication platforms, two 64-
elements phased array antennas and two horn antennas as
shown in Fig. 16. The ﬁeld test video of the proposed testbed
is available in [41].
The hardware testbed architecture of JSCIS is shown
in Fig. 16(a), where both horn antennas and phased array
antennas are used at the transmitter and receiver sides. In stage
1, two JSCIS integrated equipments (IEs) are operating in the
Rx
Tx
Target
+
v
-
v
Transmitter Chassis
RF Head
28 GHz
Tx
Rx
Receiver Chassis
RF Head
28 GHz
NI 6581B
Stage1 Radar Sensing
Stage2 
Joint Radar and 
Communicaion
Stage3 
Merge
(a)
ķ
ĸ
Ĺ
(b)
Fig. 16. Hardware testbed of JSCIS system. (a) Hardware
architecture of JSCIS system, (b) Field test scenario of JSCIS
system. x Phased array antenna HDTX270280-64CH. y Test
distance. z Moving target.
radar mode to detect the target independently. In stage 2, the
IEs switch to the communication mode, establish one mmWave
communication link from IE 1 to IE 2 via two phased array
antennas, and transmit the raw sensing data of IE 1 in stage
1 to IE 2.
The hardware testbed is shown in Fig. 16(b). In the ﬁeld
test, one of the 5G mmWave platforms is set as a transceiver,
and two phased array antennas are connected to Tx and Rx
ends of the RF head as transmitter and receiver. The distance
range is set from 0.5 m to 9 m. The radar detection data is
compared with the actual range data to obtain the accuracy
of the radar ranging in the JSCIS. Two phased array antennas
x are used as a ﬁxed IE to send integrated detection signals.
In the test, z is used as the target with a moving speed of 1
m/s. The receiver performs 4096 points Inverse Fast Fourier
Transform (IFFT) radar signal processing on the reﬂected
echo, which can achieve the ranging radar performance with
a resolution of 0.488 m. The refresh rate of radar data is 10
ms, and the system updates the detection data in the form of
average value every 3 seconds, as shown in y. When the target
is placed at a distance of 2 m, the test result is 1.956 m, and


---

Page 14

---

14
Slot 
Allocation 1
1 subframe = 0.2ms(14 OFDM symbols)
PSS
DL  DMRS
Radar
xPDSCH
xPDSCH
xPDSCH
xPDSCH
xPDSCH
xPDSCH
xPDSCH
xPDSCH
xPDSCH
0
1
2
3
4
5
6
7
8
9 10 11 12 13
xPDSCH
xPDSCH
1 Radio frame = 10ms (50 subframes)
0
1
1
1
1
1
1 ...
1
xPDCCH
DL  DMRS
xPDSCH
xPDSCH
xPDSCH
xPDSCH
xPDSCH
xPDSCH
xPDSCH
xPDSCH
xPDSCH
0
1
2
3
4
5
6
7
8
9 10 11 12 13
xPDSCH
xPDSCH
xPDSCH
Radar
PSS
DL  DMRS
Radar
xPDSCH
xPDSCH
xPDSCH
xPDSCH
xPDSCH
xPDSCH
xPDSCH
xPDSCH
xPDSCH
0
1
2
3
4
5
6
7
8
9 10 11 12 13
xPDSCH
xPDSCH
xPDCCH
DL  DMRS
xPDSCH
xPDSCH
xPDSCH
xPDSCH
xPDSCH
xPDSCH
xPDSCH
xPDSCH
xPDSCH
0
1
2
3
4
5
6
7
8
9 10 11 12 13
xPDSCH
xPDSCH
Slot 
Allocation 2
Radar 
symbol
14.28μs
...
1200 subCarriers
Fig. 17. Frame structure design of JSCIS system.
1.5 2.0 2.5 3.0 3.5 4.0 4.5 5.0 5.5 6.0 6.5 7.0 7.5 8.0 8.5 9.0 9.5 10.0
Distance /m
0
0.05
0.1
0.15
0.2
0.25
Distance error /m
R1
R2
Fig. 18. Ranging results of JSCIS system.
the distance accuracy of target detection is ± 0.044 m.
Fig. 17 shows the slot allocation (SA) design of JSCIS.
Each frame of JSCIS is 10 ms, which contains 50 subframes
(SFs) in [42]. Each SF contains 14 Orthogonal Frequency
Division Multiplexing (OFDM) symbols, and each symbol
length is 14.28µs. The SF type contains SF type0 and SF
type1. Both Slot Allocation 1 (SA 1) and Slot Allocation 2
(SA 2) are shown in Fig. 17. Different slot allocation methods
are realized by R = KR/ (KR + KC), where KR is the
number of radar symbols and KC is the number of physical
downlink shared channel (PDSCH) symbols in one radio
frame. R1 = 1/ (12 × 50) = 1/600 in SA 1 denotes only one
radar symbol is ﬁlled in SF 0. R2 = 50/ (12 × 50) = 50/600
in SA 2 denotes one radar symbol is added in SF 0 and SF 1.
The number of subCarriers is 1200, and the ﬁlled 1200 valid
data is used to complete the function of radar detection range
in the process of JSCIS.
Fig. 18 shows the radar test results of JSCIS under different
time slot allocations with the target moving. The ranging
accuracy is expressed in the form of distance error, where R1
and R2 correspond to SA 1 and SA 2 in Fig. 17, respectively.
The target distance is set between 1.5 m and 10 m. The results
show that the radar ranging accuracy of the integrated system
is within ± 0.25 m, where the communication throughput of
JSCIS can achieve a stable data rate of 2.8 Gbps. With the
increase of radar time slot allocation ratio from R1 to R2, the
radar ranging performance is also improved depicted by the
decrease of distance error.
V. CONCLUSION
In this paper, we have proposed the JSCIS to support
the dynamic frame structure conﬁguration for sensing and
communication dual functions based on the 5G NR protocol in
28 GHz mmWave frequency band. And the best time duration
allocation ratio of sensing and communication dual functions
for one vehicle is achieved by modeling the M/M/1 queuing
problem using the age of information (AoI) in this paper. Con-
sidering multiple CAVs, the resource allocation optimization
problem has been formulated as a non-cooperative game, and
the feasibility and existence of pure strategy NE are proved
theoretically. Further, the CTRA algorithm is proposed to
achieve the best feasible pure strategy NE. Both simulation
and hardware testbed are designed and developed in this
paper. The simulation results show that the proposed CTRA
algorithm is convergent and can obtain the optimal system
time allocation strategy more effectively than other algorithms.
And the proposed CTRA algorithm can improve the radar
total mutual information by 26%. Finally, the hardware testbed
results verify that the feasibility of the proposed JSCIS is
achieved with an acceptable radar ranging accuracy within
± 0.25 m, as well as a stable data rate of 2.8 Gbps, which
paves the way for the implementation of joint sensing and
communication design in CAVs.
REFERENCES
[1] J. Wang, J. Liu and N. Kato, “Networking and Communications in
Autonomous Driving: A Survey,” IEEE Communications Surveys &
Tutorials, vol. 21, no. 2, pp. 1243-1274, Secondquarter 2019.
[2] S. Liu, L. Liu, J. Tang et al., “Edge Computing for Autonomous Driving:
Opportunities and Challenges,” Proceedings of the IEEE, vol. 107, no.
8, pp. 1697-1716, Aug. 2019.
[3] L. Kong, M. K. Khan, F. Wu et al., “Millimeter-Wave Wireless Com-
munications for IoT-Cloud Supported Autonomous Vehicles: Overview,
Design, and Challenges,” IEEE Communications Magazine, vol. 55, no.
1, pp. 62-68, Jan. 2017.
[4] A. E. Fernandez, A. Servel, J. Tiphene et al., “Fifth Generation Commu-
nication Automotive Research and innovation Project Deliverable D2.1
5GCAR Scenarios, Use Cases, Requirements and KPIs,” v2.0, Feb. 2019.
[5] Z. Feng, Z. Fang, Z. Wei et al., “Joint radar and communication: A
survey,” China Communications, vol. 17, no. 1, pp. 1-27, Jan. 2020.
[6] International Telecommunication Union, “Annex 16 to Working Party
5A Chairman’s Report on Working Document Towards A Preliminary
Draft New Report ITU-R M.[CAV] Connected Automated Vehicles
(CAV),” Nov. 2020.
[7] C. Aydogdu, M. F. Keskin, N. Garcia et al., “RadChat: Spectrum sharing
for automotive radar interference mitigation,” IEEE Transactions on
Intelligent Transportation Systems, vol. 22, no. 1, pp. 416-429, Jan.
2021.
[8] N. Gonz´alez-Prelcic, R. M´endez-Rial and R. W. Heath, “Radar aided
beam alignment in MmWave V2I communications supporting antenna
diversity,” 2016 Information Theory and Applications Workshop (ITA),
La Jolla, CA, 2016.
[9] A. R. Chiriyath, B. Paul, D. W. Bliss et al., “Inner Bounds on Perfor-
mance of Radar and Communications Co-Existence,” IEEE Transactions
on Signal Processing, vol. 64, no. 2, pp. 464-474, Jan. 2016.
[10] O. B. Akan and M. Arik, “Internet of Radars: Sensing versus Sending
with Joint Radar-Communications,” IEEE Communications Magazine,
vol. 58, no. 9, pp. 13-19, Sept. 2020.
[11] F. Liu, A. Garcia-Rodriguez, C. Masouros et al., “Interfering Channel
Estimation in Radar-Cellular Coexistence: How Much Information Do
We Need?,” IEEE Transactions on Wireless Communications, vol. 18,
no. 9, pp. 4238-4253, Sept. 2019.


---

Page 15

---

15
[12] L. Han, K. Wu, “Joint wireless communication and radar sensing
systems-state of the art and future prospects,” IET Microwaves, Antennas
and Propagation, vol. 11, no. 7, pp. 876-885, May 2013.
[13] F. Liu, C. Masouros, A. Petropulu et al., “Joint Radar and Communica-
tion Design: Applications, State-of-the-art, and the Road Ahead,” IEEE
Transactions on Communications, vol. 68, no. 6, pp. 3834-3862, June
2020.
[14] A. Hassanien, M. G. Amin, Y. D. Zhang et al., “Signaling strategies
for dual-function radar communications: an overview,” IEEE Aerospace
and Electronic Systems Magazine, vol. 31, no. 10, pp. 36-45, Oct. 2016.
[15] P. Kumari, J. Choi, R. W. Heath et al., “IEEE 802.11ad-Based Radar:
An Approach to Joint Vehicular Communication-Radar System,” IEEE
Transactions on Vehicular Technology, vol.67, no.4, pp. 3012-3027, Apr.
2018.
[16] J. A. Zhang, A. Cantoni, R. W. Heath et al., “Framework for an
Innovative Perceptive Mobile Network Using Joint Communication
and Sensing,” 2017 IEEE 85th Vehicular Technology Conference (VTC
Spring), Sydney, NSW, 2017.
[17] Y. Liu, X. Fang and M. Xiao, “Discrete Power Control and Transmission
Duration Allocation for Self-Backhauling Dense mmWave Cellular
Networks,” IEEE Transactions on Communications, vol. 66, no. 1, pp.
432-447, Jan. 2018.
[18] M. Costa, M. Codreanu and A. Ephremides, “On the Age of Information
in Status Update Systems With Packet Management,” IEEE Transactions
on Information Theory, vol. 62, no. 4, pp. 1897-1910, Apr. 2016.
[19] O. Ayan, H. Murat G¨ursu, A. Papa et al., “Probability Analysis of Age
of Information in Multi-Hop Networks,” IEEE Networking Letters, vol.
2, no. 2, pp. 76-80, June 2020.
[20] I. Kadota, A. Sinha and E. Modiano, “Scheduling Algorithms for
Optimizing Age of Information in Wireless Networks With Throughput
Constraints,” IEEE/ACM Transactions on Networking, vol. 27, no. 4, pp.
1359-1372, Aug. 2019.
[21] S. Farazi, A. G. Klein and D. R. Brown, “Average Age of Information
in Update Systems with Active Sources and Packet Delivery Errors,”
IEEE Wireless Communications Letters, vol. 9, no. 8, pp. 1164-1168,
Aug. 2020.
[22] Y. Ni, L. Cai and Y. Bo, “Vehicular beacon broadcast scheduling based
on age of information (AoI),” China Communications, vol. 15, no. 7,
pp. 67-76, July 2018.
[23] ITU-R
WP5A
Document
5A/TEMP/106-E,
“WORKING
DOCU-
MENT TOWARDS A PRELIMINARY DRAFT NEW REPORT ITU-
R M.[CAV] Connected Automated Vehicles (CAV),” May 2021.
https://www.itu.int/md/R19-WP5A-210428-TD-0106/en
[24] S. Lien, S. Shieh, Y. Huang et al., “5G New Radio: Waveform, Frame
Structure, Multiple Access, and Initial Access,” IEEE Communications
Magazine, vol. 55, no. 6, pp. 64-71, Jun. 2017.
[25] M. R. Bell, “Information Theory and Radar: Mutual Information and
the Design and Analysis of Radar Waveforms and Systems,” Pasadena,
CA, USA: California Institute of Technology, 1988.
[26] B. Tang and J. Li, “Spectrally Constrained MIMO Radar Waveform
Design Based on Mutual Information,” IEEE Transactions on Signal
Processing, vol. 67, no. 3, pp. 821-834, Feb. 2019.
[27] A. R. Chiriyath, B. Paul and D. W. Bliss, “Radar-Communications
Convergence: Coexistence, Cooperation, and Co-Design,” IEEE Trans-
actions on Cognitive Communications and Networking, vol. 3, no. 1,
pp. 1-12, Mar. 2017.
[28] C. E. Shannon, “A Mathematical Theory of Communication,” The Bell
System Technical Journal, vol. 27, pp. 379-423, 623-656, July, October,
1948.
[29] T. M. Cover and J. A. Thomas, “Elements of Information Theory -2nd
ed.,” John Wiley & Sons, Inc., Hoboken, New Jersey, 2006.
[30] M. Moltafet, M. Leinonen and M. Codreanu, “On the Age of Information
in Multi-Source Queueing Models,” IEEE Transactions on Communica-
tions, vol. 68, no. 8, pp. 5003-5017, Aug. 2020.
[31] R. D. Yates and S. Kaul, “Real-time status updating: Multiple sources,”
IEEE International Symposium on Information Theory Proceedings,
Cambridge, MA, 2012.
[32] P. Ren, A. Munari and M. Petrova, “Performance Tradeoffs of Joint
Radar-Communication Networks,” IEEE Wireless Communications Let-
ters, vol. 8, no. 1, pp. 165-168, Feb. 2019.
[33] J. Park and C. Nguyen, “A new millimeter-wave step-frequency radar
sensor for distance measurement,” IEEE Microwave and Wireless Com-
ponents Letters, vol. 12, no. 6, pp. 221-222, Jun. 2002.
[34] V. Raghavan, S. Subramanian, J. Cezanne et al., “Single-User Versus
Multi-User Precoding for Millimeter Wave MIMO Systems,” IEEE
Journal on Selected Areas in Communications, vol. 35, no. 6, pp. 1387-
1401, Jun. 2017.
[35] D. Monderer and L. S. Shapley, “Potential games,” Games Econ.
Behavior, vol. 14, no. 1, pp. 124-143, 1996.
[36] W. Zhong, G. Chen, S. Jin et al., “Relay Selection and Discrete
Power Control for Cognitive Relay Networks via Potential Game,” IEEE
Transactions on Signal Processing, vol. 62, no. 20, pp. 5411-5424, Oct.
2014.
[37] W. Yi, Y. Liu, Y. Deng et al., “Modeling and Analysis of MmWave V2X
Networks With Vehicular Platoon Systems,” IEEE Journal on Selected
Areas in Communications, vol. 37, no. 12, pp. 2851-2866, Dec. 2019.
[38] 3GPP TR 38.886, User Equipment (UE) radio transmission and recep-
tion, Rel.16, V16.3.0, Mar. 2021.
[39] Q. Zhang, H. Sun, Z.Wei et al., “Sensing and Communication Integrated
System for Autonomous Driving Vehicles,” IEEE INFOCOM Workshop,
July 6, 2020, pp. 1278-1279.
[40] J. Zheng, Y. Cai, X. Chen et al., “Optimal base station sleeping in green
cellular networks: A distributed cooperative framework based on game
theory,” IEEE Transactions on Wireless Communications, vol. 14, no. 8,
pp. 4391-4406, Aug. 2015.
[41] Hardware testbed video of JSCIS for 5G mmWave Enabled CAVs.
https://youtu.be/LrQX3Y4poK0.
[42] 3GPP TS 38.211, Physical channels and modulation, Rel.16, V16.5.0,
Mar. 2021.
