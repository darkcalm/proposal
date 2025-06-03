# Xia2019 A Fully Distributed Hierarchical Control Framework for Coordinated Operation of DERs in Active Distribution Power Networks

## Paper Metadata

- **Filename:** Xia2019_A_Fully_Distributed_Hierarchical_Control_Framework_for_Coordinated_Operation_of_DERs_in_Active_Distribution_Power_Networks_DOI_10-1109_TPWRS-2018-2870153.pdf
- **DOI:** 10.1109/TPWRS.2018.2870153
- **Authors:** Not available
- **Year:** Not available
- **Journal/Venue:** Not available
- **URL:** Not available
- **Extraction Date:** 2025-06-03T15:04:06.359428
- **Total Pages:** 12

## Abstract

Abstract not available from BibTeX metadata.

## Keywords

Keywords not available from BibTeX metadata.

---

## Full Text Content



### Page 1

A fully distributed hierarchical control framework for 
coordinated operation of DERs in active distribution 
power networks 
Shiwei Xia, Member, IEEE, S. Q. Bu, Senior Member, IEEE, Can Wan, Member, IEEE, Xi Lu, Ka Wing Chan, 
Member, IEEE, and Bin Zhou, Senior Member, IEEE
Abstract—In order to effectively accommodate large-scale DERs in 
active distribution power networks, this paper proposes a fully 
distributed hierarchical framework to economically manage multiple 
DERs within three layers: the tertiary, the secondary generation 
regulation layer and the primary frequency droop control layer. In the 
tertiary layer, a fully distributed dispatch strategy is designed to 
optimally allocate the active power base point of DERs in a 
center-free manner, with total generation and load imbalance locally 
estimated by individual DER using the discrete finite-time consensus 
algorithm. In the secondary layer, a distributed fair generation 
correction strategy is designed based on power sharing ratio to timely 
counterbalance the load deviations on top of the tertiary layer. In the 
primary layer, a droop controller is presented for DER, battery 
energy storage and controllable load to maintain satisfactory system 
frequency performance. The proposed hierarchical framework is a 
fully distributed generation coordinating approach, which could 
optimally control active power outputs of multiple DERs with the 
minimal cost while ensuring satisfactory system frequency, and is 
also robust to DERs’ uncertainties. Case studies have demonstrated 
the effectiveness of proposed fully distributed hierarchical 
framework for optimally coordinating DERs power outputs and 
regulating system frequency. 
 Index Terms—active distribution power network, distributed 
energy resources, hierarchical control framework, generation 
correction strategy 
I.
INTRODUCTION
With the development of renewable energy generation 
technology, distributed energy resources (DERs) such as wind 
power generation, photovoltaic power generation and 
gas-fired generation etc., are extensively integrated into 
distribution networks. This requires a change in the paradigm 
of distribution power network from conventional passive into 
active, thus resulting in the active distribution power network 
(ADPN), in order to reduce the negative impacts of DERs and 
effectively manage DERs in a large scale [1]. In addition, 
current smart grid technologies such as the information and 
communication technology (ICT) and the multi-agent 
technology make it possible to proactively coordinate DERs 
operating in an optimal manner [2]. It is necessary to develop 
a general paradigm with suitable control strategies for the 
coordinated operation of DERs to achieve better power 
quality and more economical operation for the whole network. 
Conventional 
optimization 
methods 
for 
distribution 
network operation are mainly centralized, which rely on a 
powerful hub to collect global information of all components 
and conduct the computational procedure. However, because 
of the ever-growing penetration level and the distributed 
nature of DERs, centralized strategies are going to encounter 
some technical challenges [3]. Firstly, the large volume of 
data caused by DERs’ integration will result in the heavy 
computational burden and communication complexity of 
control 
center. 
Then, 
the 
system 
is 
susceptible 
to 
single-point-failure. Moreover, the plug-and-play operational 
requirements of DERs are unable to be flexibly satisfied. 
Therefore, the fully distributed strategies are preferred for 
their superiorities of scalability, sparse network, and improved 
resiliency to faults or unknown parameters [4, 5]. 
Recently, some studies have applied distributed algorithms 
in solving economic dispatch (ED) problems [4, 5]. For 
instance, in [7] a decentralized ED approach was proposed 
based on generators’ incremental costs and a leader agent was 
used to collect the global generation and load demand 
information for calculating the power mismatch. In [8] the 
average consensus strategy was used for the local estimation 
of power mismatch shared among distributed generators, and 
a novel distributed dispatch algorithm was established for 
solving the ED problem. In [9, 10], a fully distributed ED 
algorithm was proposed by using an additional innovation 
term to ensure that the power mismatch gradually approaches 
to zero. In [11], the consensus algorithm was hybrid with the 
alternating direction method of multipliers (ADMM) for 
solving the optimal power flow problem with demand 
response in a distributed manner. The above literatures mainly 
focused on applying distributed algorithms for off-line 
optimal operation of DERs in tertiary generation regulation 
layer, while the off-line solutions are not suitable to be 
implemented for the real-time coordination of DERs in 
distribution networks. 
As a complement to the off-line optimization in a single 
layer, some scholars have put forward the hierarchical control 
structure to address different requirements with different 
control hierarchy. For example, authors of [12] proposed a 
hierarchical control scheme to improve the system overall 
efficiency while considering the State-of-Charge balance at 
the same time, while the secondary and tertiary control were 
implemented in a micro-grid central controller. In [13], a 
potential-function was used for the secondary and tertiary 
control of a micro-grid, and an all-round central controller 
was needed to communicate with all DERs. Besides of these 
centralized hierarchical control schemes for power system 
operation, some center-free hierarchical control strategies 
were also put forward. For instance, a decentralized 
hierarchical framework was proposed in [14] and [15] to 
optimize the charging process of PEVs for frequency 
regulation in a competitive electricity market. In [16, 17], new 
distributed control strategies were established for both the 
frequency and voltage regulation of micro grids, in which 
only 
the 
localized 
information 
and 
nearest-neighbor 
communication were needed. Dr. M. A. Mahmud of [18] 
designed a nonlinear distributed controller capable of 
maintaining both active and reactive power balance to prevent 
overloading. Further, the work in [19] is not only able to 
restore the system frequency and network voltage in a 
distributed manner but also ensure its reactive power sharing. 
However, the above works mainly perform the power quality 
regulation 
and 
solve 
the 
power 
sharing 
problem 
proportionally according to DERs’ power ratings, while the 
economical operation of the whole system is not taken into 
account and thus optimal power sharing cannot be achieved. 
Motivated by the above works, this paper proposed a fully 
distributed hierarchical control framework for optimally 
coordinating DERs operation in ADPN by three layers. In the 
tertiary generation regulation layer, a fully distributed dispatch 
This is the Pre-Published Version.
The following publication S. Xia, S. Bu, C. Wan, X. Lu, K. W. Chan and B. Zhou, "A Fully Distributed Hierarchical Control Framework for Coordinated Operation of DERs in Active Distribution 
Power Networks," in IEEE Transactions on Power Systems, vol. 34, no. 6, pp. 5184-5197, Nov. 2019 is available at https://doi.org/10.1109/TPWRS.2018.2870153
© 2018 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, in any current or future media, including 
reprinting/republishing this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or 
reuse of any copyrighted component of this work in other works.

---


### Page 2

strategy incorporating the ADMM into discrete finite-time 
consensus algorithm (DFCA) was properly designed to 
optimize the active power base point of DERs in a center-free 
manner. In the secondary generation regulation layer, a 
distributed fair generation correction strategy was proposed 
by using the DFCA to counterbalance the load deviations in a 
shorter timescale on top of the tertiary generation regulation, 
which was also without relying on a central coordinator. 
Collectively, the tertiary and secondary layers provided the 
primary control layer with active power tracking reference 
points. In the primary layer, by using locally measured 
frequency deviations, the power droop controller was 
designed for the fast acting devices including the DERs, 
battery energy storages (ESs) and the controllable load to 
maintain satisfactory frequency dynamic performance of 
ADPN. In this way, all the three layers are designed to operate 
without a central coordinator and therefore a fully distributed 
hierarchical control framework is well established. 
The main contributions of this paper are as follows. 
1) To accommodate the feature of highly penetrating and 
widely scattering DERs, a fully distributed hierarchical 
framework without requiring a centralized coordinator, as 
comparisons to the centralized hierarchical framework in [12, 
13] or decentralized one in [14, 15], is innovatively designed 
for ADPN economical operation by using ADMM and DFCA 
for the tertiary and secondary layer as well as the local droop 
controller for the primary layer, respectively. 
Compared with ordinary consensus based ADMM for 
DC-OPF problem [11], here the DFCA is incorporated into 
ADMM for formulating an efficient distributed optimization 
algorithm with less complexity and good data privacy, which 
only needs very few iterations to calculate the power 
imbalances in tertiary layer compared with the ordinary
consensus algorithm as demonstrated by Fig.5. Different from 
the conventional centralized generation correction approach 
implemented with a control center to collect fuel cost 
coefficients of all DERs for calculating power participation 
factors [20], the DFCA is utilized in this paper to form a 
distributed generation correction strategy and conduct the 
economical generation correction without any central 
controller in the secondary layer. 
2) 
The proposed fully distributed framework could 
optimally control the active power output of multiple DERs 
with the minimal cost under the fluctuating load condition, 
while ensuring satisfactory system dynamic frequency 
performance. Compared with the distributed control scheme 
in [4, 16-19] to conduct the generation corrections according 
to its rated power, which neglected the economy of the 
generation corrections in the secondary layer, the proposed 
distributed approach utilizes the DFCA to realize the 
economical generation corrections in the secondary layer and 
thereby the corporation of tertiary and secondary layer can 
obtain the real time optimal solution of DERs outputs, which 
has been validated by the benchmark results of traditional 
centralized methods. (please refer to the Table 1 in page 7). 
3) The proposed hierarchical framework is robust to 
accommodate the complexities and uncertainties of DERs, 
such as the random plug-in/out behaviors of DERs. 
4) Comprehensive simulations on a distribution system 
with multiple DERs have demonstrated that the proposed fully 
distributed hierarchical framework is effective to optimally 
coordinate the power output of DERs and can well regulate 
the system frequency. 
The rest of this paper is organized as follows. The 
preliminary of DERs’ economically coordinated operation and 
the discrete finite-time algorithm are introduced in Section II, 
and then a fully distributed three-layer hierarchical control 
framework is designed in Section III. Afterwards three case 
studies are conducted in Section IV and V to validate the 
effectiveness of the proposed hierarchical scheme, and the 
conclusion is drawn in the last section. 
II.
PRELIMINARY
This section first presents the problem formulation of 
DERs coordinated operation, and then the background of 
discrete time finite algorithm used for dispatching DERs in 
the later section is introduced. It is also noted that the ramping 
constraints, startup/shutdown constraints etc. of DERs could 
be readily handled by many techniques in a multiple timescale 
paradigm including the day-ahead security constrained unit 
commitment and the real time security constrained unit 
commitment (several hours ahead) [21, 22], these constraints 
are not considered in this paper due to the page limits and the 
focus of this research is to optimally coordinate DERs 
operation for a short timescale, in specific from 5 minutes 
approaching the real time. 
A. problem formulation of DERs’ coordinated operation
The emerging generation technologies have enriched the
diversities of DERs, which could be generally categorized 
into dispatchable and non-dispatchable. The gas-fired power 
generator and diesel combustion turbines etc. with good 
controllability are the common dispatchable DERs, while the 
photovoltaic generators and wind power generators etc. highly 
relying on intermittent renewable energy sources driven by 
weather are the common non-dispatchable DERs. In this 
paper, non-dispatchable DERs will be treated as negative 
loads, and their actual power outputs are formed in terms of 
power generation predictions plus generation deviations. The 
purpose of DERs coordinated operation is to effectively and 
economically control the dispatchable DERs in ADPN to 
match conventional load demands and the negative load 
demands for non-dispatchable DERs in real time. 
Assume n dispatchable DERs in ADPN, the objective of 
DERs coordinated operation is to minimize the total 
generation cost, i.e., 


2
1
1
min
min
(
)
n
n
i
i
i
i
i
i
i
i
i
F G
a G
b G
c






 
(1) 
where Fi(Gi) is the fuel cost of gas-fired power generators or 
diesel combustion turbines with coefficients ai , bi and ci. The 
power balance constraint and DER output limits are for the 
real time load and generation balance as (2). 
1
n
m
i
j
i
j
G
D



 
(2) 
min
max
i
i
i
P
G
P

 
(3) 
where Gi and Dj stand for the ith DER output and jth load 
respectively; n and m are the numbers of DERs and loads. 
Distinguished from the conventional ED model which only 
considers the offline load predictions in (2), we would like to 
emphasize Dj in (2) is the actual load demand in this paper and 
the objective of DERs coordinated operation is to optimally 
control a large number of DERs for the actual load demand. 
The real time actual load demand would be denoted by the 
off-line load prediction Dprej plus the on-line load deviation 
Ddevj as (4). 
=
j
prej
devj
D
D
D
 
(4) 
As DERs have the advantage of being flexibly ramped 
up/down or turned on/off, the presented model (1)-(4) could 
explore the fast response capability of DERs to match the real 
time load demands. In Section III, a fully distributed

---


### Page 3

hierarchical control scheme will be designed by economically 
dispatching DERs operation base point for load predictions 
Dprej in the tertiary layer plus conducting DERs generation 
corrections for on-line load deviations Ddevj in the secondary 
generation regulation layer. 
B. Discrete finite-time consensus algorithm (DFCA)
In Section III, a fully distributed control scheme will be
proposed to solve the model (1)-(4) in a center-free manner. 
As preliminaries for designing this control scheme, the basic 
concept of the graph theory and discrete finite-time consensus 
algorithm are briefly reviewed in the following. 
A graph G is usually used to represent the communication 
network topology coupled with power devices. The graph G is 
a pair of set (VG, EG), where VG ={ V1 ,V2 ,...,Vn } is the 
non-empty set for vertices and 
G
E ={e1,e2,...,ek} is the set for 
edges with ek=(Vi ,Vj). Ni is the set of neighbor agents of agent 
i. The adjacency matrix A of G is a n×n symmetric matrix with
elements aij=aji=1 if j∈Ni, otherwise aij =aji=0. The Laplacian
matrix L of G is formed with lii=∑aij (j∈Ni ) and lij=-aij (j≠i).
The conventional consensus algorithm is described as [7] 
( )
( -1)
( -1)
( -1)
(
)
i
k
k
k
k
i
ii
i
ij
i
j
j N
y
y
y
y






 
(5) 
where yi(k) is the physical state of agent i at iteration k, ωii and 
ωij are the weighting factors of agent i and neighbor agent j, 
respectively. 
Lemma [23, 24]: If λ2 ≠λ3≠... ≠λK+1≠0 be the K distinct 
nonzero eigenvalues of the Laplacian matrix L, then yi in (5) 
would converge to the average value in K steps, i.e.,
( )
( )
(0)
1
=(
)
n
k
k
i
j
i
i
y
y
y
n



, if the weighting factors are 
updated as follows. 
( )
1
(
)
1
(
)
i
s
s
ij
s
i
a
i
j
j
N










(s=2,..., K+1) 
(6) 
where ai =|Ni| is the number of neighboring agents of agent i. 
To implement (6), each agent needs to know the nonzero 
eigenvalues of Laplacian matrix L. To address this concern, a 
graph discovery strategy based on the network flooding 
method is used to determine L locally for each agent, and then 
the eigenvalues of L are calculated to update the weighting 
factors in (6) for distributed algorithms [24, 25]. 
III.
PROPOSED FULLY DISTRIBUTED THREE-LAYER
HIERARCHICAL FRAMEWORK 
Communication networks
Communication networks
Distribution Network
DER
1
1+s T
mi
+
ai
bi
K
K
s

''
1
i F
1
Ms
D

Tertiary Generation Regulation 
based on ADMM with discrete 
consensus algorithm 
DERi
P
iy
(
)
j
i
y
j
N

(
1)
( )
( )
( )
(
)
i
k
k
k
k
i
i
ij
i
j
j N
y
y
y
y







iy
refi
P
si
P
ti P
Fluctuating 
Load j 
Wind 
Farm j 
f
f*
(
)
prej
i
D
j
N

prei
D
Secondary Generation Regulation
 Primary Frequency 
Droop Control
For DER i(i =1,…,N)
Battery energy storage i
 Pbatt,i 
+
-
+
+
-
+
-
+
+
+
f*
f*
Controllable 
load i 
-
devj
D 
Fig. 1 Proposed fully distributed hierarchical control framework 
Fig. 1 depicts the proposed fully distributed hierarchical 
control framework for DERs coordinated operation. It has 
three control layers: the tertiary generation regulation layer, 
the secondary generation regulation layer and the droop 
characteristic based primary frequency control layer. The 
tertiary layer, which is the top and also the slowest one, is 
mainly concerned with the DER distributed off-line economic 
dispatch for predicted load demands. The secondary layer is 
designed to have faster dynamics response than that of the 
tertiary layer and is used to conduct the generation corrections 
for load deviations in distributed manner. The bottom layer is 
the primary control which locally provides the frequency 
regulation and ensures reference tracking with fast responses. 
In the tertiary layer, a fully distributed dispatch strategy 
based on DFCA is properly designed to optimally allocate the 
active power base point of DERs in a center-free manner. For 
the secondary generation regulation, a distributed fair 
generation correction strategy is proposed by using DFCA 
based on the power sharing ratio to timely counterbalance the 
load deviations in a shorter timescale on top of the tertiary 
generation regulation. Collectively, the tertiary and secondary 
layers provide the primary control layer with active power 
tracking reference points. In the primary layer, a local 
frequency droop controller is presented for DERs, battery 
energy storage and controllable load to maintain satisfactory 
system frequency dynamics. In the following, we will 
describe the three-layer generation regulation scheme in 
detail. 
A. Distributed tertiary generation regulation
In the tertiary generation regulation layer, we designed a 
fully distributed optimization approach based on ADMM and 
DFCA to conduct the off-line generation dispatch for the 
predicted load Dprej, and this optimal generation of DER in 
tertiary layer is indicated as Pti in Fig.1. If Gi and Dj are 
substituted by Pti and Dprej in (1)-(2) for merely considering 
load predictions, DERs off-line generation dispatch problem 
could be converted to the extended Lagrangian formulation as 
2
2
1
1
1
1
1
2
(
)
(
)
(
)
2
n
n
m
n
m
e
i ti
i ti
i
ti
prej
ti
prej
i
i
j
i
j
L
a P
b P
c
P
D
P
D



















(7) 
where λ is the Lagrange multiplier and ρ is a positive constant 
parameter. As a typical decentralized algorithm, the 
Alternating Direction Method with Multiplier (ADMM) 
algorithm could solve complex optimization problems in 
divide-and-conquer manner and is therefore a powerful 
optimization engine with attractive convergence performance. 
According to ADMM theory [26, 27], the output of DER i is 
solved as 
min
max
( )
( )
( )
( )
(
1)
( )
1
2
(
1)
(
1)
argmin
(
,
,...,
,
,
,...,
,
)
i
ti
i
k
k
k
k
k
k
k
ti
e
ti
tn
t
t
t i
t i
P
P
P
P
L P
P
P
P P
P






 
min
max
2
( )
( )
1
( )
( )
1
argmin [
(
)
(
]
2
i
ti
i
n
m
k
k
k
i ti
i ti
i
tj
ti
ti
prej
P
P
P
j
j
n
m
k
k
tj
ti
ti
prej
j
j
a P
b P
c
P
P
P
D
P
P
P
D





















(8) 
Denote
( )
( )
1
n
m
k
k
tj
prej
j
j
P
D
e





, then (8) can be simplified as 
( )
( )
( )
(
1)
[
]
(
1,..., )
2
k
k
k
k
ti
i
ti
i
P
e
b
P
i
n
a









 
(9) 
with constraint Pimin<Pti(k+1)< Pimax for ith DER output Pti. The 
dual variable is updated by 
(
1)
( )
(
1)
( )
(
1)
1
(
)
n
m
k
k
k
k
k
ti
prej
i
j
P
D
e
















 (10) 
Equation (9) and (10) are updated iteratively for the optimal 
solution until the following criterions are both satisfied [28].

---


### Page 4

(
1)
(
1)
2
1
(
1)
(
1)
( ) 2
2
1
||
||
(
)
||
||
(
)
n
m
k
k
pri
ti
prej
i
j
n
k
k
k
dual
ti
ti
i
r
P
D
s
P
P

















 
(11) 
where εpri and εdual are tolerance parameters pre-specified in 
terms of expected accuracy. 
From formula (9), the updating of Pti (k+1) relies on ith 
DER’s local parameters ai, bi, and the system total power 
imbalance e(k). As e(k) is the global information of the whole 
system and needs to be estimated by collecting all DERs’ 
outputs and all loads in distribution networks with an 
information hub, it is just a decentralized approach instead of 
a fully distributed one when directly using ADMM to solve 
the problem. A fully distributed approach should be capable of 
calculating the global imbalanced power e(k) only based on the 
local information without any central coordinator. For this 
purpose, the previous introduced DFCA in Section II.B could 
be introduced to estimate e(k) by sharing limited information 
with neighbor agents as below. 
Algorithm 1: DFCA for locally estimating e(k) 
1) Suppose there are totally n buses connected with loads
and DERs, and the power imbalance for node i is initialized as 
yi(0) =Pti(0)-Dprei, where Pti(0) and Dprei stand for the DER initial 
output and load prediction at bus i. (Note: for a bus only with 
load then Pti(0)=0, and similarly Dprei =0 for a node only with 
DER). Initialize the weighting factors ωij by (5) based on the 
pre-configured communication network; 
2) Repeat to update yi(k) by DFCA using (5) in K steps, 
where yi(k) stands for the average power imbalance estimated 
at bus i; 
3) The total unbalanced power e(k) could be calculated as 
n×yi(k) for bus i, where n is the total number of buses. 
The proposed distributed dispatch approach based on 
ADMM and DFCA mainly includes the following steps for 
the tertiary generation regulation. 
1) Initialize the output of DER i as Pti(0) and the dual variable
λ(0), prepare the weighting factors ωii and ωij by (5)
according to the communication network;
2) Estimate the total power imbalance e(k) of distributed
system networks by Algorithm 1;
3) Update ith DER output Pti(k+1) by (9) and the dual variable
λ(k+1) by (10);
4) If the stop condition (11) is satisfied, output Pti(k+1) as the
final optimal solution; otherwise go to step 2).
B. Distributed secondary generation regulation
In the tertiary generation regulation, we only find the DER
optimal output (called base point hereafter) for the predicted 
load demand Dprej. However, the actual load demand Dj in real 
time is usually different from the predicted load as expressed 
in (4), and our ultimate goal is to economically coordinate the 
DERs outputs for the real-time actual load demand. 
As the tertiary layer has already optimized DER operation 
base point Pti for the predicted load Dprej, if we could further 
conduct the economical generation correction (indicated as Psi 
here) for the real time load deviation Ddevj on top of the base 
point, then the integrated generation in tertiary and secondary 
layer as Prefi=Pti+Psi would be the DER optimal solution for the 
real-time actual load demands. In other words, as the actual 
load deviates from the load prediction, we need to investigate 
how much each DER should be adjusted (i.e., ‘participate’ in 
the load change) from the base point in order that the actual 
load can be served by DERs in the most economical manner. 
Assume both the first and second order derivatives of fuel 
cost function with respect to DER output are available (i.e., 
both Fi' and Fi" exist for fuel cost function Fi in (1)). It is 
well-known that the incremental costs or the first order 
derivatives Fi' (i=1,...n) of all DERs are equal to the Lagrange 
multiplier λ when DERs reach the optimal solution. Denote 
the incremental cost of DER i for the base point Pti in tertiary 
layer as λ0= Fi'(Pti). Since the system total load is changed by 
a total amount of ∑Ddevj, the marginal cost and optimal output 
of DER i should move to λ0+Δλ and Pti+Psi accordingly with 
the relationship λ0+Δλ= Fi'(Pti+Psi), then we have 
'
'
''
(
)
(
)
(
)
i
ti
si
i
ti
i
ti
si
F P
P
F P
F P
P





 
for i=1,...n (12) 
To satisfy the power generation and load balance, we have 
1
1
n
m
si
devj
i
j
P
D




 
(13) 
The solution of (12) and (13) is 
1
(
)
m
si
i
devj
j
P
pf
D


 
(14) 
where 
''
''
1
1
1
n
i
i
j
j
pf
F
F



is the power participation factor for 
DER i. Formula (14) indicates that the economical generation 
correction Psi of DER i for the total load deviation ∑Ddevj is 
inversely proportional to the second derivative Fi" of fuel cost. 
For conventional generation correction, a central controller is 
needed to collect fuel cost coefficients of all DERs for 
calculating the summation of Fj'' (j=1,...n) and the power 
participation factors pfi [20]. In order to design a distributed 
generation, formula (14) is rewritten in the form of (15) for 
DER i and j. 
1
/
/
m
devj
si
i
sj
j
j
D
P
pf
P
pf



 
or 
''
''
1
1
/
/
i
si
sj
j
i
j
y
P
P
y
F
F



(15) 
where yi and yj are the defined power sharing ratio in terms of 
DER generation correction to DER power participation factor. 
These power sharing ratios yi and yj are also the tailored 
consensus variables for DER i and j which could be used in 
the discrete finite-time consensus algorithm as shown in Fig.1. 
With (15), the secondary regulator compares the local 
power sharing ratio yi of DER i with its neighbors’ power 
sharing ratio yj on a communication graph and accordingly 
ensures all DERs’ power sharing ratio converging to the 
consensus value in finite-time, which could be guaranteed by 
Lemma of DFCA introduced in Section II.B. Thereby the 
equality (15) is satisfied in finite time, and an economical 
generation correction strategy is established based on the 
power sharing ratio to timely counterbalance load deviations 
∑Ddevj on top of the tertiary generation regulation layer. 
To provide the input signal for secondary generation 
regulation in Fig.1, the frequency deviation Δf, calculated as 
the frequency reference f* minus the distribution network 
actual frequency f, is controlled by a PI controller, which 
would increase or decrease the generation correction of DER i 
accordingly for the positive or negative frequency deviations 
until the frequency deviation approaches zero. 
With the help of distributed tertiary and secondary 
generation regulation, the DER economical outputs for actual 
load demands mainly compose of two parts: the economic 
base point Pti for predicted load ∑Dprej and the economical 
generation corrections Psi for load deviation ∑Ddevj. The 
summation Pti+Psi will provide the complete optimal power 
reference point Prefi for the primary frequency droop controller 
to track as shown in Fig.1. 
C. Local primary frequency regulation

---


### Page 5

In the primary frequency regulation layer, the frequency 
droop controller is presented to ensure the fast acting devices 
can perfectly track the reference point and maintain 
satisfactory system frequency with quick responses. In this 
paper, the DERs, battery Energy Storages (ESs) and 
controllable load are integrated for primary frequency 
regulation. 
1) Primary Frequency Regulation of DER 
In the primary layer, we utilize the feedback of frequency
deviation Δf as the input of droop controller as shown in Fig.1. 
Since DER with small initial belongs to the fast acting devices, 
a simplified first-order inertia dynamic model with small time 
constant is used to represent the input-output characteristics. 
Hence, DER dynamic model incorporating the power 
reference and droop control can be described by (16) 
1
(
(
*
))
1
DERi
refi
i
DERi
P
P
m
f
f
s T




 
(16) 
where TDERi and mi are the inertia time constant and droop 
coefficient of DER i; Prefi is the optimal power reference of 
DER i provided by the tertiary and secondary generation 
regulation layer; f* and f are the frequency reference and the 
network actual frequency. 
2) Primary Frequency Regulation of Controllable Load 
With the development of smart grid paradigm, the load
control on the demand side is the impressive supplement to 
the power generation control from the generation side. The 
simplest way of realizing this is by utilizing the so-called 
controllable load such as the combined cooling heating and 
power, controllable water heater etc. Due to its outstanding 
flexibility, the controllable load can be appropriately adjusted 
to reduce/increase power consuming so as to counterbalance 
the supply-demand imbalance [29, 30], and therefore it is very 
effective for frequency regulation from the load side. In this 
paper, the controllable load is model as one inertial block with 
the ramp up/down and anti-windup limits as shown in Fig.2. 
The input signal is the system frequency deviation and output 
is the controlled load (CL) demand. 
1
CL
CL
K
T s


*f

CL
p
CLmax
p
CLmin
p
Ramp 
limits
f 
Fig. 2 Dynamic model of controllable load for frequency regulation 
3) Ancillary Frequency Regulation Service of ESs 
ESs are the power electronics based devices which has 
extremely fast response and therefore the ancillary frequency 
regulation service is one of the most valuable applications 
which could fully exploit the merits of ESs instantaneous high 
power. In this paper, ES is controlled with the droop 
characteristics against the frequency deviation, with the 
discharging/charging power limits and State of Charge (SOC) 
constraints also be satisfied during the frequency regulation 
procedure. 
The completed ancillary frequency regulation service of 
ES could be described by formula (17) at the bottom of this 
page, where PESimax , SOCmin and SOCmax are the maximal 
discharging power, the minimal and maximal SOC; Δf is the 
frequency deviation; KESi is ES droop coefficient for 
frequency regulation; Preq,i,t and SOCt are the power reference 
determined by the frequency droop control which is the 
control signal for modeling ES dynamics in Fig.3. 
The ES can be modeled as a Thevenin-based voltage 
source in series with an internal resistance Rseries and a 
paralleled RC network (consisting of the resistance Rtrans and 
capacitor Ctrans) [31]. The terminal voltage is related to SOC 
and defined as a nonlinear term of SOC by Nernst equation. 
oc
nom
nom
(
/
)ln(SOC / (
SOC))
V
V
RT
F
C




(18) 
where α is a sensitivity parameter of Voc to SOC; R, F and T 
are the gas constant, the Faraday constant and battery 
temperature, respectively. When SOC is kept within a range of 
10%−95% to preserve battery life, Rseries, Rtrans and Ctrans can 
be approximated as constants with typical values obtained 
from [31]. The dynamics of battery charging could be 
described by the block diagram in Fig. 3 [25],where Preq,i,t is 
the reference point of ES charging/discharging power 
determined by the primary frequency regulation controller 
using (17). 
Fig. 3 Model for PEV battery charging dynamics 
For the distribution network dynamic, an inertia block 
diagram 1/(Ms+D) is used to model the effect of the net load 
change on frequency deviation by parameter D and the inertia 
M of distribution network as shown in Fig.1. 
Remarks: 
1) Based on the proposed hierarchical framework, DER 
generations could be effectively coordinated based on the 
DFCA (in the tertiary and secondary generation regulation 
layer) and the local frequency droop control (in the primary 
frequency regulation layer), which only needs the local 
information and parameters without any central information 
hub, and hence the proposed hierarchical framework is a fully 
distributed control approach; 
2) The proposed fully distributed hierarchical framework 
can optimally coordinate the active power output of multiple 
DERs with the minimal cost by optimizing the base point in 
the tertiary layer plus economically conducting generation 
correction in the secondary layer, while ensuring satisfactory 
system frequency with fast response in the primary layer. 
3) The proposed distributed framework can be fitted in a
two-segment power market composed of intra-day market and 
real-time spot market. The power generation scheduling of 
tertiary layer could be performed in the intra-day market 
based on the price signals such as the fuel costs of local 
generators, and the combination of ADMM and DFCA could 
be used to address the optimal solutions in a center-free 
intra-day market, in which the market participants will 
coordinate to make bids periodically for each timeslot (such 
as 5-15 minutes) without market decision center and update 
their generators output accordingly. The secondary and 
primary frequency regulation layers can be used to provide 
balancing services in the real-time spot market, and the 
generation correction and droop control strategies will be used 
to reallocate the supply-demand unbalance among generators 
and ES. While the technical content of the proposed 
distributed scheme is the focus here, the application of 
proposed scheme in a centre-free market environment will be 
thoroughly investigated in the future.

---


### Page 6

max
max
max
max
max
min
max
, ,
max
max
min
(
) &(
)
(
*
)
(
) &(
)
(
) &(
)
0
i
i
i
i
i
ESi
ES
ESi
t
ES
ES
ESi
ES
ESi
t
req i t
ESi
ES
ESi
t
P
K
f
P
SOC
SOC
K
f
f
K
f
P
K
f
P
SOC
SOC
SOC
P
P
K
f
P
SOC
SOC














 
max
min
(
0) &(
)
0
(
0) &(
)
i
i
ES
t
ES
t
K
f
SOC
SOC
K
f
SOC
SOC












 
(17) 
IV. CASE STUDY FOR 33-BUS ADPN WITH WIND FARMS
The performance of proposed hierarchical framework for
DERs coordinated operation was firstly tested on a modified 
33-bus ADPN [32] with a single Point of Common Coupling
(PCC) as shown in Fig. 4, which consists of 15 DERs, 32
loads, 2 energy storages, 1 controllable load and 3 wind farms.
The 15 DERs are deployed in the bus set {1, 3, 5, 7, 9, 11, 13,
15, 17, 19, 21, 23, 25, 27, 29} while the fuel cost coefficients
are cited from TABLE II of [33] and the upper limits of power
outputs are enlarged 2.5 times to match the system total load
level. As illustrated in Fig.4, the communication links
(indicated as blue dash line) are mainly configured based on
the physical network, which can conveniently utilize the
power line communication techniques, plus extra links
between bus 8-22, 18-33, 25-29 to satisfy the n-1
communication reliability. Each bus in Fig.4 is deployed with
a smart agent, which is capable of communicating with its
neighbor agents for sharing the load and generation
information. The tertiary generation regulation layer is 
updated every 300s based on the short-term load and wind 
power prediction, while the secondary generation regulation
and the first layer control are updated in real time. The
parameters of ADPN inertia block are D=1.25MW/Hz, M=50s.
The droop coefficient of DERs is mi=0.1MW/Hz. And the
parameters of controllable load are KCL=1.5 MW/Hz and
TCL=5s MW/Hz. The droop coefficient of two ESs are KES1=2
MW/Hz for KES2=1 MW/Hz.
For the parameter ρ of ADMM, as there are no general 
rules of how to select the optimal penalty parameter ρ, in the 
following case studies we choose ρ by trial and errors and fix 
it as 10-5 to guarantee the good convergence and yield the 
optimal solutions. 
0
1
24
25
23
3
2
19
20
21
22
4
5
7
6
8
9
12
11
10
13
14
15
16
17
18
26
27
28
29
30
31
32
33
DG
WF
ES
Load
Feeder
Link
PCC
CL 
Fig.4 Modified IEEE 33-bus ADPN with 3 WFs and 15 DERs 
A. Case 1: investigate the performance of proposed scheme
by 33-bus ADPN with simplified load condition
For zooming in the performance of proposed scheme, we 
firstly conducted simulations for the following simplified 
scenarios: 1) To check the effectiveness of the tertiary 
generation regulation layer, the predicted total load level of 
the 33-bus ADPN is assumed as 3715k W during 0-300s, 
while at 300s bus1 to bus10 each increases 20k W and 
therefore 
the 
predicted 
load 
demand 
changes 
to 
3715k W+200k W=3915k W during 300s-2400s; 2) To validate 
the performance of the secondary generation correction layer, 
the total load deviation of this 33-bus ADPN is assumed zero 
during 0s-700s and 450k W during 700s-2400s, and the step 
moment is indicated by the blue dot-line B in Fig.5; 3) DER11 
is disconnected at 1300s indicated by the blue dot-line C and 
reconnected at 1900s marked by the blue dot-line D in Fig.5 
to investigate the robustness of proposed scheme for random 
plug-in/out behaviors of DERs. 
Fig.5 Simplified load conditions for 33-bus ADPN 
1) Convergence of DFCA for estimating load imbalance e(k) 
a) by discrete finite-time consensus algorithm
b) by conventional consensus algorithm
Fig. 6 Convergence for estimating average load imbalance 
The prowess of DFCA for locally estimating the total 
generation and load imbalance (described by algorithm 1) is 
firstly investigated for the stepping moment 300s, when the 
power imbalance 200k W occurs. Fig 6 shows the convergence 
performance of DFCA and the conventional consensus 
algorithm [7,11]. As illustrated in Fig.6a), the DFCA 
estimated the average load imbalance of 33 buses as 6.06k W 
in very fewer iterations indicating the total power imbalance 
(equal to the average value multiplied by total number of 
buses) is 6.06k W*33=199.98k W which is almost the same as 
the practical power imbalance 200k W. However, the 
conventional consensus algorithm could only reach an average 
estimation of 5.74k W at 100 iterations as shown in Fig. 6b) 
indicating a total power imbalance 5.74k W*33=189.42k W, 
which would converge to a satisfied estimation by several 
hundred iterations. This comparison shows that the DFCA is

---


### Page 7

more powerful than the conventional consensus algorithm to 
accurately estimate the power imbalance at the cost of fewer 
iterations. 
2) Optimality performance of proposed scheme 
Based on the accurately estimated power imbalance,
ADMM would be used to effectively seek DERs’ optimal 
operation base point of tertiary layer. As shown in Fig.7a), 
when the predicted load level changes from 3715k W to 
3915k W at 300s (indicated by the first blue dot-line), the 
ADMM approach only costs several iterations to obtain DERs 
optimal solutions as detailed in the second column of Table I. 
Due to the suddenly enlarged load demands at 300s, the 
system frequency is slightly reduced with the help of the 
primary frequency droop controller in the primary layer at 
first. However, the secondary generation regulation layer 
immediately detects the frequency droop and tries to make up 
the power deficiency and results in a small fleeting power 
perturbation nearby 300s in Fig.7b). When the load deviation 
450k W occurs at 700s (at the second blue dot-lined), the 
secondary generation regulation layer timely conducts 
generation corrections to counterbalance the load deviation 
accordingly as shown in Fig.7b). With a short transition, all 
DERs generation corrections reach static until the next 
disturbance occurs at 1300s. 
To check the global optimization capability of secondary 
generation regulation layer when counterbalancing load 
deviations, DERs optimal generation corrections in the 
secondary layer at 900s are detailed in the third column of 
Table I, while the summations of the generation corrections 
and the optimal base points in the tertiary layer are also shown 
in the forth column. Considering that we cannot accurately 
know the system actual load level in advance, the one-off 
optimized solutions of conventional centralized ED for the 
total load 3915k W+450k W=4365k W are used as the 
benchmark only for comparison purpose, which are provided 
in the fifth column of Table I. Compared with conventional 
ED solution, the proposed scheme could solve comparable 
DER optimal solutions with a satisfied minimal cost as shown 
in the last row of Table I. These comparisons indicate that the 
proposed scheme can effectively coordinate multiple DERs 
operations with the satisfactory optimality performance in a 
distributed manner. 
a）DER optimal operation base point in tertiary layer
b) DER generation corrections in secondary layer
c) DER actual power outputs
d) Energy storage outputs and Controllable load demand
e) Frequency regulation performance
Fig.7 Performance of proposed scheme in simplified load conditions 
Table I Solutions of proposed scheme and centralized ED at 900s 
DER 
index 
Proposed Scheme(k W) 
Centralized 
ED for 
4365k W 
(k W) 
Tertiary 
generation 
dispatch for 
3915k W 
Secondary 
generation 
corrections 
for 450k W 
Individual 
total 
outputs 
1 
696.62 
53.38 
750.00 
750.00 
2 
163.33 
22.15 
185.48 
185.43 
3 
221.12 
27.72 
248.83 
248.78 
4 
96.39 
12.32 
108.72 
108.74 
5 
96.46 
10.09 
106.55 
106.60 
6 
519.16 
55.53 
574.70 
575.06 
7 
96.31 
12.35 
108.66 
108.74 
8 
163.12 
22.23 
185.35 
185.43 
9 
127.23 
12.35 
139.58 
139.57 
10 
127.30 
12.30 
139.60 
139.57 
11 
696.62 
53.38 
750.00 
750.00 
12 
315.33 
55.35 
370.69 
370.56 
13 
315.32 
55.35 
370.67 
370.56 
14 
74.59 
8.53 
83.12 
83.09 
15 
206.11 
36.96 
243.07 
242.88 
Cost 
($/h) 
832.4169 
832.4171 
3) Robustness of proposed scheme 
To investigate the robustness of proposed scheme for 
accommodating random plug-in/out behaviors of DERs, 
DER11 was disconnected at 1300s and reconnected as 1900s 
as indicated in Fig.5. Since the tertiary generation regulation 
layer updated the optimal base point every 300s while the 
secondary 
generation 
regulation 
layer 
conducted 
the 
generation corrections in real time, with loss of 750k W power 
generation at 1300s due to the disconnection of DER11, the 
secondary 
layer 
immediately 
provided 
the 
increased

---


### Page 8

generation corrections to complement the power insufficiency 
as shown in Fig.7b) during 1300s-1500s. Afterward at 1500s, 
the tertiary generation regulation layer started to take effects 
and re-dispatched the total predicted load 3915k W among the 
other 14 DERs except the DER11 as shown in Fig.7a), 
meanwhile the secondary layer reduced DERs generation 
corrections accordingly and reallocated the original load 
deviation 450 k W among all DERs except the DER11 at 
1500s. Afterward, though DER11 was reconnected at 1900s, it 
was designed that the system reserves a short time interval to 
prepare for DER11 back, and DER11 was schedulable at the 
next updating interval 300s. Therefore the tertiary and 
secondary generation regulation layer only began to take 
effect at 2100s and finally reached the optimal operation 
points, which are exactly the same as the operation states 
during 700s-1300s before DER11 disconnection. 
Fig. 7c) and Fig. 7d) also displayed the actual outputs of 
DERs, ESs and the controllable load for the aforementioned 
conditions during 2400s, respectively. The simulation results 
indicated that the DERs could always be coordinated to 
undertake certain amount of load demands, while for the ESs 
and controllable load, they only support power outputs during 
the transient period when the frequency deviations occur. This 
is because the DERs has three control layers while the ESs 
and controllable load only work with frequency droop 
controller for primary frequency regulation. 
In order to demonstrate the functionality of the secondary 
layer, the ESs and controllable load in the primary layer, the 
following three schemes are implemented separately for 
frequency regulation. 1) the ED algorithm with DERs primary 
frequency droop control; 2) the proposed three-layer 
hierarchical control scheme excluding the primary frequency 
droop control of ESs and controllable load; 3) the proposed 
completed three-layer hierarchical control scheme. As shown 
in Fig.7e), the Scheme 1) has large frequency deviations when 
the load unbalance occurs since 700s, while for scheme 2) and 
3), their frequency deviations are zero during most of time and 
they only slightly fluctuate with many small burrs at the 
ephemeral power imbalance moment. This is because both 
scheme 2) and 3) have the generation corrections in the 
secondary layer and therefore they could well compensate the 
power imbalance. When further make comparisons between 
scheme 2) and 3), it is clear that scheme 3) is much better in 
terms of frequency dynamic response, and the ESSs and 
controllable load could indeed improve the dynamic response 
of frequency regulation. 
It is worthy to mention that the proposed distributed 
hierarchical 
framework 
is 
also 
very 
robust 
to 
the 
communication errors and time delay from the tertiary layer 
and the secondary layer. In the very serious condition that the 
generation data of both the tertiary and secondary layer or 
either of them is completely delayed or lost for one DER, the 
other DERs would pick up this generation shortage, which is 
very similar to the situation that one DER randomly 
disconnect from the network. Please refer to the simulation 
results in Fig.7 for the time period 1300s to 2100s as 
discussed earlier. Moreover, even for the worst scenario that 
the generation data in both the tertiary and secondary layer is 
lost for all DERs, the proposed three hierarchical framework 
would degrade into a primary frequency regulation layer only, 
which could also work but with the cost of non-zero 
frequency deviations. 
B. Case 2: investigate the performance of proposed scheme 
in 33-bus network with practical load conditions 
In case 2, the following practical load conditions are 
settled to validate the performance of proposed scheme: 1) as 
shown in Fig. 8, the predicted load demand and wind power 
generation are updated every 300s, and the real time wind 
power deviations for 3 wind farms (WFs) are generated based 
on the composite model consisting of the base, the ramp, the 
gust and the turbulence components [34, 35]; 2) in order to 
test the plug-in and play capability of proposed scheme, 
DER11 is plugged out at 6000s and plugged in at 12000s. 
Fig. 9 displayed how the 15 DERs were coordinated by the 
proposed hierarchical scheme to match the real-time load 
demands and fluctuating wind power generation. As shown in 
Fig.9a), the tertiary generation regulation layer economically 
dispatched the predicted load demand by ADMM with a time 
interval of 300s, while the secondary generation regulation 
layer further economically conducted generation corrections 
to timely counterbalance load deviations on top of the tertiary 
layer in Fig.9b), and finally the 15 DERs actual outputs are 
obtained in Fig.9c). It is noteworthy that: 1) as DER11 was 
disconnected during 6000s-12000s, the outputs of DER11 
quickly decreased to zero in Fig.9a) to Fig.9c), while for other 
14 DERs, their dispatched generations in the tertiary layer, the 
generation corrections in the secondary layer and their actual 
outputs obviously increased to a high level for making up the 
DER11 generation loss; 2) during 6000s-12000s for DER11 
disconnection, as DER1 is the most economical generator 
with the cheapest cost coefficients, its generation output 
increases extensively even that sometimes DER1 approaches 
the power upper limit at 750k W. Fig.9d) demonstrates the ESs 
power outputs and the controllable load level, which indicate 
that 
their 
outputs 
are 
always 
quickly 
adjusted 
to 
counterbalance the frequency deviations. 
Fig.8 Load/wind prediction and actual deviations for 33-bus ADPN 
a) Base operation point in tertiary layer 
b) Generation corrections in secondary layer

---


### Page 9

c) DER actual outputs 
d) Energy storage outputs and Controllable load demands
Fig.9 DER outputs in 33-bus ADPN with practical load conditions 
Fig.10 Frequency regulation in 33-bus ADPN with practical conditions 
Fig.10 further compared 
the frequency regulation 
performance for three different implementations: 1) the ED 
algorithm with DER primary frequency droop control only; 2) 
the 
proposed 
three-layer 
hierarchical 
control 
scheme 
excluding the primary frequency droop control of ESs and 
controllable load; 3) the proposed completed three-layer 
hierarchical control scheme. As illustrated by the red line in 
Fig.10, the proposed distributed scheme could ensure the 
frequency deviations always in the vicinity of zero with 
occasionally slight fluctuations not exceeding 0.1Hz. However, 
the scheme 1) would usually result in non-zero frequency 
deviations with the maximum as large as 0.3Hz, while scheme 
2) also has satisfied frequency regulation performance but 
worse than the performance of scheme 3). These comparisons 
demonstrated that for a ADPN with fluctuating wind power 
generation, as DER generation corrections (on top of the base 
point in tertiary layer) are conducted in the secondary layer to 
compensate the fluctuating wind power generation, scheme 2) 
and 3) can effectively improve the frequency regulation 
performance, while the later is the most outstanding one 
because there is plenty of ESs and controllable load with good 
fast response capability. 
V.
CASE STUDY FOR 132-BUS WITH LARGE-SCALE DERS
To further investigate the effectiveness of proposed 
distributed hierarchical scheme to optimally coordinate 
large-scale DERs, a 132-bus ADPN is deployed with 60 
DERs and 12 WFs as shown in Fig.11, which is formed by 
replicating the aforementioned 33-bus ADPN four times with 
extra feeders between bus 33 and bus 1. The fuel cost 
coefficients (ai, bi, and ci ) of DERs in area A are the same as 
those in case 1,while coefficients for other 45 DERs are 
partially modified as follows: 1.2ai for DERs in area B, 0.8bi 
for DERs in area C and 1.5ai for DERs in area D. The 
predicted load and wind power generation are similarly 
generated as that for 33-bus ADPN with proportional 
modifications, which is indicated by the black line in Fig. 12a). 
The wind power deviations and the ultimately resultant load 
demand are provided as the pink and green line in Fig.12a). 
To observe the plug-in/out behaviors of DERs, DER1 in 
subsystem A is assumed to be plugged out at 9000s and 
plugged in at 15000s. 
IEEE 33-bus 
system
A
IEEE 33-bus 
system
C
IEEE 33-bus 
system
B
IEEE 33-bus 
system
D
1
1
1
1
33
33 
Fig.11 Structure of 132-bus ADPN with 60 DERs 
a) Predicted load with total wind generation deviations
b) Base operation point in tertiary layer
c) Generation corrections in secondary layer 
d) DER actual outputs

---


### Page 10

e) ES power outputs and controllable load demand
Fig.12 DER outputs in 132-bus ADPN with practical load conditions 
Fig. 12b) to Fig. 12d) demonstrated the optimized base 
operation point in tertiary regulation layer, the generation 
corrections in secondary regulation layer and the actual 
generation outputs of 60 DERs solved by the proposed 
hierarchical scheme. As illustrated by these figures, the 
tertiary layer could effectively address the optimal base point 
according to the predicted load demand and wind power 
generation, while the secondary generation regulation layer 
could further economically conduct generation corrections on 
top of tertiary generation regulation, and finally the outputs of 
60 DERs are coordinated to match the real time load demands 
of 132-bus ADPN as shown in Fig. 12d). It is also noted that 
when DER1 is disconnected during 9000s-15000s, the optimal 
generation base point in tertiary layer, the generation 
corrections of secondary layer and the actual generation 
outputs for DER1 are all decreased to zero. And the proposed 
scheme is still effective to guide other 59 DERs to seek the 
optimal outputs for minimizing the fuel cost and regulating 
system frequency well. As DER41 is much cheaper than other 
DERs, its generation output is very large and frequently 
restricted by the upper generation limit, while DER7, 8, 9, 10, 
34, 35, 37 and 39 etc. occasionally reach their lower 
generation limits during 7000s-14000s as shown in Fig. 12d) 
because of their expensive marginal fuel costs. Fig.12e) also 
demonstrates the ESs power outputs and the controllable load 
level accordingly during the procedure of counterbalancing 
the frequency deviations. 
Fig.13 Frequency regulation performance for 132-bus ADPN 
Fig. 13 plotted the frequency deviations of 132-bus ADPN 
for three different schemes: 1) the ED algorithm with DER 
primary frequency droop control; 2) the proposed three-layer 
hierarchical control scheme without the primary frequency 
droop control of ESs and controllable load; 3) the proposed 
completed three-layer hierarchical control scheme. It is 
evident that the proposed scheme 3) can effectively regulate 
the system frequency and the maximal frequency deviation is 
near zero as the blue line shown in Fig. 13. However, the 
scheme 1) or 2) could only regulate the system at large 
non-zero frequency deviations. These simulation results 
demonstrated that the proposed scheme is the best one capable 
of effectively regulating the system frequency. 
VI. CONCLUSION 
In this paper, a fully distributed three-layer control 
framework is proposed for the coordinated operation of 
multiple DERs in ADPN. Based on the discrete finite-time 
consensus algorithm, a fully distributed dispatch scheme and a 
fair generation correction strategy are designed in the tertiary 
and secondary generation regulation layer respectively. While 
in the primary generation regulation layer, a frequency droop 
controller is presented to ensure DERs outputs perfectly 
tracking the power reference of the tertiary and secondary 
layers, and DERs with energy storage and controllable load 
could well maintain satisfactory system dynamic frequency in 
real time. Tests on the modified IEEE 33-bus and 132-bus 
ADPN with large-scale DERs have demonstrated the 
effectiveness of the proposed control scheme in optimally 
coordinating DERs outputs, ensuring satisfactory system 
frequency and robustly accommodating uncertainties of DERs. 
Since the proposed fully distributed hierarchical scheme to 
exclusively regulate system frequency may result in operation 
constraint violations, such as violating the voltage or line 
capacity limits, further ongoing research would elaborately 
design an all-round distributed hierarchical scheme (e.g., 
based on fully distributed optimal power flow model) to 
simultaneously regulate system frequency and ensure static 
security of distribution networks. 
VII. ACKNOWLEDGMENT
 The authors would like to acknowledge the support from 
Department of Electrical Engineering, The Hong Kong 
Polytechnic University for the Start-up Fund Research Project 
(1-ZE68), Hong Kong Research Grant Council for the 
Research Projects (25203917) and (15200418), and National 
Natural Science Foundation of China for the Research Project 
(51807171). 
VIII. REFERENCE
[1] X. Shen, M. Shahidehpour, S. Zhu, Y. Han, and J. Zheng, "Multi-Stage 
Planning 
of 
Active 
Distribution 
Networks 
Considering 
the 
Co-Optimization of Operation Strategies," IEEE Trans. Smart Grid, vol.
9, no. 2, pp. 1425-1433, Mar. 2018. 
[2] A. Madureira, C. Gouveia, C. Moreira, L. Seca, and J. P. Lopes,
"Coordinated management of distributed energy resources in electrical 
distribution systems," in Proc. 2013 IEEE PES Conference on 
Innovative Smart Grid Technologies (ISGT Latin America), 15-17 April 
2013, pp. 1-8. 
[3] W. Zheng, W. Wu, B. Zhang, H. Sun, and Y. Liu, "A Fully Distributed 
Reactive Power Optimization and Control Method for Active
Distribution Networks," IEEE Trans. Smart Grid, vol. 7, no. 2, pp. 
1021-1033, Mar. 2016. 
[4] Q. Shafiee, V. Nasirian, J. C. Vasquez, J. M. Guerrero, and A. Davoudi, 
"A Multi-Functional Fully Distributed Control Framework for AC
Microgrids," IEEE Trans. Smart Grid, vol. PP, no. 99, p. 1-1, 2017. 
[5] W. T. Elsayed and E. F. El-Saadany, "A Fully Decentralized Approach
for Solving the Economic Dispatch Problem," IEEE Trans. Power 
Systems, vol. 30, no. 4, pp. 2179-2189, July 2015. 
[6] S. Yang, S. Tan, and J. Xu, "Consensus Based Approach for Economic
Dispatch Problem in a Smart Grid," IEEE Trans. Power Systems, vol. 28,
no. 4, pp. 4416-4426, Nov. 2013. 
[7] Z. Zhang and M. Chow, "Convergence Analysis of the Incremental Cost 
Consensus Algorithm Under Different Communication Network
Topologies in a Smart Grid," IEEE Trans. Power Systems, vol. 27, no. 4,
pp. 1761-1768, Nov. 2012. 
[8] H. Pourbabak, J. Luo, T. Chen, and W. Su, "A Novel Consensus-based
Distributed Algorithm for Economic Dispatch Based on Local
Estimation of Power Mismatch," IEEE Trans. Smart Grid, vol. PP, no.

---


### Page 11

99, p. 1-1, 2017. 
[9] G. Hug, S. Kar, and C. Wu, "Consensus Innovations Approach for
Distributed Multiagent Coordination in a Microgrid," IEEE Trans. Smart 
Grid, vol. 6, no. 4, pp. 1893-1903, Jul. 2015. 
[10] S. Kar and G. Hug, "Distributed robust economic dispatch in power
systems: A consensus+innovations approach," in Proc. 2012 IEEE
Power and Energy Society General Meeting, 22-26 July 2012, pp. 1-8. 
[11] Y. 
Wang, 
L. 
Wu, 
and 
S. 
Wang, 
"A 
Fully-Decentralized
Consensus-Based ADMM Approach for DC-OPF With Demand 
Response," IEEE Trans. Smart Grid, vol. 8, no. 6, pp. 2637-2647, Nov.
2017. 
[12] L. Meng, T. Dragicevic, J. Vasquez, J. Guerrero, and E. R. Sanseverino,
"Hierarchical control with virtual resistance optimization for efficiency 
enhancement and State-of-Charge balancing in DC microgrids," in Proc. 
2015 IEEE First International Conference on DC Microgrids (ICDCM), 
7-10 June 2015, pp. 1-6. 
[13] A. Mehrizi-Sani and R. Iravani, "Potential-Function Based Control of a 
Microgrid in Islanded and Grid-Connected Modes," IEEE Trans. Power
Systems, vol. 25, no. 4, pp. 1883-1891, Nov. 2010. 
[14] J. Tan and L. Wang, "A Game-Theoretic Framework for Vehicle-to-Grid
Frequency Regulation Considering Smart Charging Mechanism," IEEE 
Trans. Smart Grid, vol. PP, no. 99, pp. 1-12, 2016. 
[15] J. Tan and L. Wang, "Coordinated optimization of PHEVs for frequency 
regulation capacity bids using hierarchical game," in Proc. 2015 IEEE 
PES General Meeting, Jul. 2015, pp. 1-5. 
[16] J. W. Simpson-Porco, Q. Shafiee, F. Dörfler, J. C. Vasquez, J. M. 
Guerrero, and F. Bullo, "Secondary Frequency and Voltage Control of
Islanded Microgrids via Distributed Averaging," IEEE Trans. Industrial
Electronics, vol. 62, no. 11, pp. 7025-7038, Nov. 2015. 
[17] X. Lu, X. Yu, J. Lai, J. M. Guerrero, and H. Zhou, "Distributed
Secondary Voltage and Frequency Control for Islanded Microgrids With 
Uncertain Communication Links," IEEE Trans. Industrial Informatics, 
vol. 13, no. 2, pp. 448-460, Apr. 2017.
[18] M. A. Mahmud, M. J. Hossain, H. R. Pota, and N. K. Roy, "Nonlinear 
distributed controller design for maintaining power balance in Islanded
microgrids," in Proc. 2014 IEEE PES General Meeting | Conference & 
Exposition, 27-31 July 2014, pp. 1-5. 
[19] Q. Shafiee, J. M. Guerrero, and J. C. Vasquez, "Distributed Secondary 
Control for Islanded Microgrids-A Novel Approach," IEEE Trans. 
Power Electronics, vol. 29, no. 2, pp. 1018-1031, Feb. 2014.
[20] A. J. Wood and B. F. Wollenberg, Power generation, operation, and
control: John Wiley & Sons, 2012. 
[21] X. Luo, S. W. Xia, K. W. Chan, and X. Lu, "A Hierarchical Scheme for
Utilizing 
Plug-In 
Electric 
Vehicle 
Power 
to 
Hedge 
Against
Wind-Induced Unit Ramp Cycling Operations," IEEE Transactions on 
Power Systems, vol. 33, no. 1, pp. 55-69, Jan. 2018. 
[22] E. Ela and M. O'Malley, "Studying the Variability and Uncertainty 
Impacts of Variable Generation at Multiple Timescales," IEEE
Transactions on Power Systems, vol. 27, no. 3, pp. 1324-1333, Aug.
2012. 
[23] A. Y. Kibangou, "Graph Laplacian based matrix design for finite-time
distributed average consensus," in Proc. 2012 American Control
Conference (ACC), 27-29 June 2012, pp. 1901-1906. 
[24] T. M. D. Tran and A. Y. Kibangou, "Distributed Estimation of Graph
Laplacian Eigenvalues by the Alternating Direction of Multipliers
Method," IFAC Proceedings, vol. 47, no. 3, pp. 5526-5531, 2014. 
[25] A. Y. Kibangou and C. Commault, "Decentralized Laplacian 
Eigenvalues 
Estimation 
and 
Collaborative 
Network 
Topology 
Identification," IFAC Proceedings, vol. 45, no. 26, pp. 7-12, 2012. 
[26] E. Ghadimi, A. Teixeira, I. Shames, and M. Johansson, "Optimal 
parameter selection for the alternating direction method of multipliers
(ADMM): quadratic problems," IEEE Trans. Automatic Control, vol. 60,
no. 3, pp. 644-658, Mar. 2015. 
[27] T. H. Chang, M. Hong, and X. Wang, "Multi-Agent Distributed
Optimization via Inexact Consensus ADMM," IEEE Trans. Signal 
Processing, vol. 63, no. 2, pp. 482-497, Jan. 2015.
[28] S. Boyd, N. Parikh, E. Chu, B. Peleato, and J. Eckstein, "Distributed
optimization and statistical learning via the alternating direction method 
of multipliers," Foundations and Trends in Communications and 
Information Theory, vol. 1, no. 3, pp. 1-122, 2011. 
[29] A. Khalil and Z. Rajab, "Load frequency control system with smart
meter and controllable loads," in Proc. The 8th International Renewable 
Energy Congress (IREC 2017), Amman, Jordan, 21-23 March 2017, pp.
1-5. 
[30] C. Jiang, B. Li, and J. Shen, "Controllable Load Management
Approaches in Smart Grids," Energies, vol. 2015, no. 8, pp.
11187-11202, 2015. 
[31] T. Kim and W. Qiao, "A Hybrid Battery Model Capable of Capturing 
Dynamic Circuit Characteristics and Nonlinear Capacity Effects," IEEE
Transactions on Energy Conversion, vol. 26, no. 4, pp. 1172-1180, Dec. 
2011. 
[32] V. B., C. S., K. N., and P. K. D. R., "Optimal reconfiguration of radial 
distribuion system using artificial intelligence methods," in Proc. 2009 
IEEE Toronto International Conference Science and Technology for 
Humanity, 26-27 Sept. 2009, pp. 660-665. 
[33] S. J. Ahn, S. R. Nam, J. H. Choi, and S. I. Moon, "Power Scheduling of
Distributed Generators for Economic and Stable Operation of a
Microgrid," IEEE Trans. Smart Grid, vol. 4, no. 1, pp. 398-405, Mar.
2013. 
[34] X. Luo, S. Xia, and K. W. Chan, "A decentralized charging control
strategy for plug-in electric vehicles to mitigate wind farm intermittency 
and enhance frequency regulation," Journal of Power Sources, vol. 248, 
pp. 604-614, Feb. 2014. 
[35] F. Milano, "An Open Source Power System Analysis Toolbox," IEEE
Trans. Power Systems, vol. 20, no. 3, pp. 1199-1206, Aug. 2005. 
IX.
BIOGRAPHY
Shiwei Xia (M’12) received the B.Eng. and M.Eng. 
degrees in electrical engineering from Harbin 
Institute of Technology, Harbin, China, in 2007 and 
2009 respectively, and the Ph.D. degree in power 
systems from The Hong Kong Polytechnic 
University, Hung Hom, Hong Kong, in 2015. Then, 
he 
worked 
as 
a 
Research 
Associate 
and 
subsequently as a Postdoctoral Fellow with the 
Department of Electrical Engineering, The Hong 
Kong Polytechnic University, in 2016-2018. 
Currently, he is with the State Key Laboratory of 
Alternate Electrical Power System with Renewable 
Energy Sources, School of Electrical and Electronic Engineering, North 
China Electric Power University, Beijing, and also with The Hong Kong 
Polytechnic University, Hong Kong. His research interests include security 
and risk analysis for power systems with renewable energies, distributed 
optimization and control of multiple sustainable energy sources in active 
distribution network. smart grid. 
S. Q. Bu (S’11-M’12-SM’17) received the Ph.D. 
degree from the electric power and energy research 
cluster, The Queen’s University of Belfast, Belfast, 
U.K., in 2012, where he continued his postdoctoral 
research work before entering industry. Subsequently,
he joined National Grid UK as a Power System
Engineer and then became an experienced UK 
National Transmission System Planner and Operator. 
He is an Assistant Professor with The Hong Kong 
Polytechnic University, Kowloon, Hong Kong, and 
also a Chartered Engineer with UK Engineering Council, London, U.K.. His 
research interests are power system stability analysis and operation control, 
including wind power generation, PEV, HVDC, FACTS, ESS and VSG. 
 He has received various prizes due to excellent performances and 
outstanding contributions in operational and commissioning projects during 
the employment with National Grid UK. He is also the recipient of 
Outstanding Reviewer Awards from IEEE Transactions on Sustainable 
Energy, IEEE Transactions on Power Systems, Renewable Energy and 
International Journal of Electrical Power and Energy Systems.

---


### Page 12

Can Wan (M’15) received his B.Eng. and Ph.D. 
degrees from Zhejiang University, China, in 2008, and 
The Hong Kong Polytechnic University in 2015, 
respectively. 
 He is a Research Professor with College of 
Electrical 
Engineering, 
Zhejiang 
University, 
Hangzhou, China, under the university Hundred 
Talents Program. He was a Postdoc Fellow at 
Department of Electrical Engineering, Tsinghua 
University, Beijing, China, and held research 
positions at Technical University of Denmark, The Hong Kong Polytechnic 
University, and City University of Hong Kong. He was a visiting scholar at 
the Center for Electric Power and Energy, Technical University of Denmark, 
and Argonne National Laboratory, IL, USA. His research interests include 
forecasting, renewable energy, active distribution network, integrated energy 
systems, and machine learning. 
Xi Lu received the B.Eng. degree in Electrical 
Engineering from North China Electric Power 
University in Beijing, China in 2015. He is currently 
pursuing the Ph D degree in Electrical Engineering at 
the Hong Kong Polytechnic University, Hong Kong. 
His research interests include application of robust 
optimization and distributionally robust optimization 
in power system operation. 
Ka Wing Chan (M’98) received the B.Sc. (Hons) 
and Ph.D. degrees in electronic and electrical 
engineering from the University of Bath, U.K., in 
1988 and 1992, respectively. He currently is an 
Associate Professor and Associate Head in the 
Department of Electrical Engineering of the Hong 
Kong Polytechnic University. His general research 
interests include power system stability, analysis and 
control, power grid integration, security, resilience 
and optimization, demand response management. 
Bin Zhou (S’11-M’13-SM’17) received the B.Sc. 
degree in electrical engineering from Zhengzhou 
University, Zhengzhou, China, in 2006, the M.S. 
degree in electrical engineering from South China 
University of Technology, Guangzhou, China, in 
2009, and the Ph.D. degree from The Hong Kong 
Polytechnic University, Hong Kong, in 2013. 
Afterwards, he worked as a Research Associate and 
subsequently 
a 
Postdoctoral 
Fellow 
in 
the 
Department of Electrical Engineering of The Hong 
Kong Polytechnic University. Now, he is an 
Associate Professor in the College of Electrical and Information Engineering, 
Hunan University, Changsha, China. His main fields of research include 
smart grid operation and planning, renewable energy generation, and energy 
efficiency.

---
