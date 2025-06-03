

---

Page 1

---

1
CPES-QSM: A Quantitative Method Towards the
Secure Operation of Cyber-Physical Energy Systems
Juan Ospina, Member, IEEE, Venkatesh Venkataramanan, Member, IEEE,
Charalambos Konstantinou, Senior Member, IEEE
Abstract—Power systems are evolving into cyber-physical en-
ergy systems (CPES) mainly due to the integration of modern
communication and Internet-of-Things (IoT) devices. CPES se-
curity evaluation is challenging since the physical and cyber
layers are often not considered holistically. Existing literature
focuses on only optimizing the operation of either the physical
or cyber layer while ignoring the interactions between them.
This paper proposes a metric, the Cyber-Physical Energy System
Quantitative Security Metric (CPES-QSM), that quantiﬁes the
interaction between the cyber and physical layers across three
domains: electrical, cyber-risk, and network topology. A method
for incorporating the proposed cyber-metric into operational
decisions is also proposed by formulating a cyber-constrained
AC optimal power ﬂow (C-ACOPF) that considers the status of
all the CPES layers. The C-ACOPF considers the vulnerabilities
of physical and cyber networks by incorporating factors such
as voltage stability, contingencies, graph-theory, and IoT cyber
risks, while using a multi-criteria decision-making technique.
Simulation studies are conducted using standard IEEE test
systems to evaluate the effectiveness of the proposed metric and
the C-ACOPF formulation.
Index Terms—Cyber-physical energy systems, cyber-metric,
cybersecurity, power systems, optimal power ﬂow, optimization.
NOMENCLATURE
General Abbreviations
ACOPF
AC optimal power ﬂow.
ACPF
AC power ﬂow.
C-ACOPF
Cyber-constrained ACOPF.
CPES
Cyber-physical energy systems.
CPES-QSM
Cyber-Physical Energy System Quantitative
Security Metric.
CPS
Cyber-physical systems.
CVSS
Common vulnerability scoring system.
DAAs
Data availability attacks.
DIAs
Data integrity attacks.
EPS
Electric power systems.
DERs
Distributed energy resources.
FDPF
Fast decoupled power ﬂow.
HiTL
Human-in-the-loop.
(Corresponding author: Juan Ospina)
Juan Ospina is with the A-1 Information Systems and Modeling Group at
Los Alamos National Laboratory, Los Alamos, NM, 87545, USA. (e-mail:
jjospina@lanl.gov).
Venkatesh Venkataramanan is with the National Renewable Energy Labo-
ratory, Golden, CO, 80401, USA. (email: vvenkata@nrel.gov)
Charalambos Konstantinou is with the Computer, Electrical and Mathemat-
ical Sciences and Engineering (CEMSE) Division, King Abdullah University
of Science and Technology (KAUST), Thuwal 23955-6900, Saudi Arabia.
(e-mail: charalambos.konstantinou@kaust.edu.sa)
ICT
Information & communication technologies.
IoT
Internet-of-things.
IT
Information technology.
MCDM
Multi-criteria decision making.
PMU
Phasor measurement units.
RED
Relative electrical distance.
SE
State estimation.
T-ACOPF
Traditional ACOPF.
Cyber-Constrained ACOPF
N
Set of buses.
R
Set of reference buses.
G
Set of generators.
Gi
Generator at bus i.
L
Set of loads.
Li
Load at bus i.
S
Set of shunts.
Si
Shunt at bus i.
E, ER
Set of branches (forward and reverse).
ℜ
Real part.
ℑ
Imaginary part.
vl
i
Voltage lower bounds.
vu
i
Voltage upper bounds.
P g,l
Gen. active power lower bounds.
P g,u
Gen. active power upper bounds.
Qg,l
Gen. reactive power lower bounds.
Qg,u
Gen. reactive power upper bounds
Sg,l
Gen. complex power lower bounds.
Sg,u
Gen. complex power upper bounds.
c2, c1, c0
Gen. cost components.
Sd
Load complex power demand.
Y s
Shunt admittance.
Y, Y c
Branch pi-section parameters.
su
ij
Complex power ﬂow on line (i, j) upper
bounds.
iu
ij
Current ﬂow on line (i, j) upper bounds.
θ∆l
ij
Branch angle difference lower bounds.
θ∆u
ij
Branch angle difference upper bounds.
ρ
Threshold value to consider bus ‘unreliable’.
α
Cyber-physical upper bound variable.
ζ
Cyber-physical lower bound variable.
CQk
CPES-QSM score value at bus k.
ℜ(Sg
k) = P g
k
Gen. k active power output.
ℑ(Sg
k) = Qg
k Gen. k reactive power output.
Vi
Voltage magnitude at bus i.
θi
Voltage angle at bus i.
Sij
Complex power ﬂow on line (i, j).
arXiv:2206.03543v2  [eess.SY]  26 Sep 2022


---

Page 2

---

2
CPES-QSM Electrical Factors
PI
Performance Index.
CRPI
Contingency Ranking Performance Index.
P
flow
l,i
Power ﬂow on line l with line i out.
P
max
l
Max. power rating for line l.
nP I
PI overloaded lines parameter.
VDI
Voltage Deviation Index.
VCPI
Voltage Collapse Prediction Index.
SVSI
Simpliﬁed Voltage Stability Index.
β
SVSI correction factor.
∆V
Voltage difference.
CPES-QSM Graph-Theory Factors
G
Graph.
Gp
Physical graph.
Gc
Cyber graph.
N
Nodes.
E
Edges.
s, t, v
Origin, destination, and evaluated node.
V
Set of all nodes.
σ(s, t)
Total shortest-paths between s and t .
d(u, v)
Shortest-path between node u and v.
BC
Betweenness Centrality.
CC
Closeness Centrality.
EBC
Edge Betweenness Centrality.
CPES-QSM Cyber Factors
P
Probability.
I
Impact.
AV
Attack Vector.
AC
Attack Complexity.
UI
User Interaction.
PR
Privileges Required.
QCR-B
Quantitative Cyber Risk Base.
QCR-A
Quantitative Cyber Risk Attack-Graph.
CPES-QSM Computation
ν
Fuzzy measure.
N
Set of all criteria.
A, B
Subsets of N.
∅
Empty set.
λ
Interaction Index.
CI
Choquet Integral.
I. INTRODUCTION
T
HE modernization and decentralization of electric power
systems (EPS) are being facilitated by the integration
of distributed energy resources (DERs) and the wide-scale
deployment of internet-of-things (IoT) devices and information
and communication technologies (ICTs). However, this mod-
ernization and transformation from old passive EPS to cyber-
physical energy systems (CPES) have their disadvantages.
Progressively, CPES are becoming more challenging to secure
due to the incorporation of IoT/ICT devices that introduce
cyber vulnerabilities to physical systems, thus creating attack
vectors not previously considered in traditional power system
operations [1].
Recent attack incidents such as BlackEnergy, CrashOver-
ride, and Triton illustrate the growing threat of vulnerabilities
in the IoT/ICT infrastructure of power systems [2], [3]. One
prominent example of an attack incident affecting the power
grid is the 2015 Ukraine cyber-attack [4]. In this case, ad-
versaries were able to trip important circuit breakers causing
a blackout that affected almost 225,000 customers. Other
examples of potential threats to EPS are explored in [5], [6],
where authors demonstrated how attackers can compromise
phasor measurement units (PMUs) by spooﬁng GPS signals
via the use of open-source exploitation methods and open-
source intelligence (OSINT) techniques.
Even though the electricity sector has matured in the deploy-
ment of protection systems, researchers and stakeholders still
struggle when quantifying the cybersecurity status and vulner-
abilities of systems operating in a CPES [7]. Conventionally,
metrics exist to quantify either the cyber or the physical
domain independently. For instance in the cyber domain, Infor-
mation Technology (IT) systems metrics such as the Common
Vulnerability Scoring System (CVSS) [8] exist, which only
relies on IT experts’ opinions to grade vulnerabilities based
on several factors, such as attack vector and attack complexity.
While CVSS is useful for analyzing vulnerabilities for IT sys-
tems, the framework is insufﬁcient when considering critical
infrastructure systems. Trying to address these issues, efforts
such as the CERT Resilience Management Model [9], the
MITRE’s Cyber Resilience Engineering Framework (CREF)
[10], and the Infrastructure Resilience Analysis Methodology
(IRAM) [4], have been proposed but fail to provide sufﬁciently
useful information to system operators due to not having direct
interpretations related to the operation of CPES.
While there are metrics that compute individual physical and
cyber resiliency factors, there is a lack of metrics designed
to study cyber-physical security rigorously in an integrated
manner. Also, many of the metrics proposed in the literature
are an aggregation of existing metrics, that need domain
specialists to interpret them. That is why authors have focused
on addressing this lack of existing metrics by proposing
different resiliency metrics and methods specially tailored for
small-scale CPES. An example is presented in [11], where
authors propose resiliency metrics that capture the level of
preparedness of a distribution system to resist extreme adverse
conditions. In [12], authors propose a stochastic security-
oriented risk management technique devised to estimate cyber-
physical security indices tailored to measure the security level
of a cyber-physical system (CPS).
The papers presented in [13] and [14] are the ones that are
closer to the idea proposed in this paper, since the metrics and
methods proposed in these papers follow a similar formulation
based on a multi-criteria decision making (MCDM) approach.
In these papers, the authors explore the concept of combining
different factors, coming from different domains such as
the physical, cyber, and device-management domains, using
Choquet Integrals (CI) to compute an overall resiliency score
of the system. The main differences between our proposed
approach and the methods presented in these papers are related
to the: (a) factors considered (different physical, graph-theory,
and cyber factors), (b) individual scoring metric for each


---

Page 3

---

3
Physical-system
Cyber-system
Factors
Attack-graph
P = 155 MW
P = 54.3 MW
Fig. 1. Overall framework for Cyber-Constrained ACOPF (C-ACOPF) operation based on the Cyber-Physical Energy System Quantitative Security Metric
(CPES-QSM).
node/bus in the CPES (thus improving visibility and human-
in-the-loop (HiTL) processes), and (c) the utilization of the
proposed cyber-metric as a deciding factor to improve not only
the resilience but the overall cyber-physical security state of
AC optimal power ﬂow (ACOPF) solutions for CPES.
Another major contribution of this paper is related to the
utilization of the proposed cyber-metric as a factor that directly
alters the traditional ACOPF solutions of a CPES based on the
real-time cybersecurity status of the system, and thus, in a way
merging the physical and the cyber domains. A limited number
of papers have explored the idea of modifying the ACOPF
formulation so that it can integrate the status of the cyber layer
of the CPES. One example is the paper presented in [15],
where authors propose a cyber-constrained OPF model for
the emergency response of smart grids. The proposed model
considers both the physical and cyber network by adding
cyber-related constraints to the traditional ACOPF but has the
disadvantage of being a ‘black-and-white’ mapping process
that assumes the total loss of control of a physical bus mapped
to a ‘cyber-blind’ cyber node (cyber-blind meaning a cyber
node that becomes invisible due to failing). Another similar
paper is the one presented in [16], where authors develop a
multi-agent-based algorithm designed to optimize the power
ﬂow of a CPES based on power ﬂow constraints derived
from ‘community resilience’ factors such as levels of emotion,
empathy, cooperation, and physical health of consumers. The
community and cyber-layer factors are measured based on
social media sentiment analysis and other social and human
factors related to cognitive science and psychology.
A. Contributions
Contrasting from the papers examined, this paper aims
to address the speciﬁc problem of quantitatively measuring
the real-time cyber-physical security of a CPES considering
factors that affect both its physical and cyber domains by
proposing a novel cyber-metric. It intends to provide an
intuitive and easy-to-understand metric that can be used for
HiTL operations and can directly reﬂect the cyber-physical
status of the CPES into the ACOPF solutions so that the
optimization can be performed not only based on the physical
status of the system but considering its current cyber status.
The contributions of this paper can be summarized as follows:
• A quantitative cyber-physical security metric for CPES is
proposed. The Cyber-Physical Energy System Quantita-
tive Security Metric (CPES-QSM) is designed to quantify
the current cyber-physical status of every IoT-connected
node in a CPES by combining factors from the electrical,
IT, and graph-theory domains using an MCDM approach.
The metric provides an easy-to-interpret way to evaluate
the current state of the CPES.
• A cyber-constrained ACOPF formulation that takes into
account not only the physical state of the system but
also considers the current status of its cyber domain,
using the proposed CPES-QSM as a proxy, is proposed.
The formulation is intended to restrict the OPF solution
space based on the current cyber status of nodes in
the system, which can make them ‘unreliable’ based on
vulnerabilities or modeled attack-graphs threats targeting
IoT devices deployed in the respective nodes of the CPES.
• Experimental case studies are investigated using standard
IEEE test systems to demonstrate the usefulness of the
proposed cyber-metric and validate the utilization of
the cyber-constrained ACOPF formulation for achieving
more secure OPF solutions (i.e., considering both the
physical and cyber status). The results show how the pro-
posed formulation improves the security and stability of
the system when a cyberattack compromises vulnerable
nodes.
Fig. 1 depicts the overall framework for the use of the pro-
posed CPES-QSM in conjunction with the cyber-constrained
ACOPF formulation with the objective of reaching a more
secure operating state by adjusting the system’s dispatch. The
ﬁgure illustrates how different factors coming from the cyber,
physical, and graph environments are combined into a single
quantitative score that is used to improve system’s operation.
The rest of the paper is organized as follows. Section
II presents the proposed quantitative cyber-physical security
metric, CPES-QSM. Section III focuses on presenting the
proposed cyber-constrained ACOPF formulation that makes
use of the CPES-QSM as a proxy for constraining the optimal
solutions based on the cyber factors of the CPES. Section IV


---

Page 4

---

4
presents the experimental setup and case studies performed to
evaluate the utility of the proposed cyber-metric and demon-
strate its effectiveness for constraining the traditional ACOPF.
Finally, Section V presents conclusions and future work.
II. CPES-QSM COMPUTATION & FACTORS
This section presents the proposed quantitative cyber-
physical metric, CPES-QSM, that is designed to provide a
real-time numerical value to the cyber and physical status of an
operating CPES. The CPES-QSM cyber-metric provides, via
an easy-to-interpret score, operating observability of individual
components and/or nodes in a CPES that can be used and
interpreted by both human operators and control systems for
improving the secure and resilient operation of CPES.
Before the computation of the CPES-QSM is presented,
we need to examine the different factors that affect the ﬁnal
computation of the score. Since our focus is towards CPES,
the factors considered cover the following three main domains:
(1) Electrical, (2) IT, and (3) Graph theory-based. Within
these domains, factors are also classiﬁed according to the
environment they affect. The environments being considered
are: (1) Physical, (2) Cyber, and (3) Network. Each factor,
explained in the next subsections, has been categorized using
one domain and one environment. Additional details about
each factor are presented in Table I using a similar format as
the one presented by EPRI in [17], [18]. It is important to note
that the cyber-metric framework presented in this paper is not
tied to the speciﬁc factors presented throughout the manuscript
and the user/operator has the liberty to choose the factors that
he/she thinks better characterizes the physical/cyber/network
system being analyzed.
A. Electrical Domain Factors
The Electrical Domain factors encompass all factors directly
related to the electrical or physical operation of the CPES.
1) Contingency Ranking Performance Index (CRPI): This
factor calculates a contingency performance index, using the
fast decoupled power ﬂow (FDPF) 1P1Q contingency ranking
method [19], that provides information about the most suscep-
tible lines and buses in a CPES. The speciﬁc details for the
CRPI factor are shown in Table I. The goal of this factor is
to calculate the performance index (PI) that tells which lines
are most susceptible to overload. Note that Target represents
the objective value of the factor, i.e., the best value is 0 while
the worst is 1 (CRPI values are scaled to the [0-1] range).
The process for computing the CRPI is based on the process
presented in [19]. A PI value is assigned to each line outage
scenario that can occur in a system. The deﬁnition of the PI
for a contingency outage i is:
PIi =
N
X
l,l̸=i
 P
flow
l,i
P
max
l
2nP I
for i = 1, ..., N
(1)
where N is the total number of lines in the system, P
flow
l,i
is the
power ﬂow on line l with line i out, and P
max
l
is the maximum
power rating for line l. The constant nP I is a parameter that
allows us to clearly distinguish between overloaded lines and
lines with ﬂows within limit. The use of a large value for
State Estimation (SE) or 
Power Flow (PF)
Define constants
•
MW line limits
•
𝑛𝑃𝐼
Remove line(s) i from network
𝑓𝑜𝑟𝑖= 1 𝑡𝑜𝑁:
Run FDPF (1P1Q, i.e., 1 iteration) 
Use ‘new’ line flows to compute PI
Add PI for contingency in line i to list
Final 
case ?
No
Yes
End
Sort Final 
PI List 
Assign max PI 
line to bus 
(CRPI)
Fig. 2.
Contingency Ranking Performance Index (CRPI) ﬂowchart process.
nP I produces a small PI value (i.e., ≈0) if all line ﬂows
are within the limit. On the other hand, if one or more lines
are overloaded, the PI value produced will be large. For our
test cases, nP I = 2 is used. The use of the PI value helps
us to quickly determine which lines of the system will have
a higher impact when taken out, thus which buses are more
important in terms of physical contingency security. Using
these PI values, a table for each line in the network can be
created and sorted from largest to smallest. The values at the
top of the list represent the lines that are most important in
the contingency ranking; thus they are assigned a higher value.
The complete process for computing the CRPI value for each
bus in the system is shown in Fig. 2.
As seen in Fig. 2, the process for calculating the PI values
for each line in the system starts by obtaining the current
status of the system via SE, PF, and/or real-time measurements
from in-ﬁeld IoT devices. Then, using these values alongside
the deﬁned constants of the process (i.e., MW limits for lines
and nP I), the loop in charge of computing the individual PI
value for each line in the system is executed. In this loop, line
(i) is ﬁrst removed from the network (outage scenario); then
an FDPF using the 1P1Q method is performed in order to
estimate the ‘new’ power ﬂows of the system [19]. The use of
the 1P1Q method, instead of a traditional full ACPF, allows
the fast execution of a relatively accurate ACPF without the
need of an exact result and multiple iterations, thus reducing
the computational complexity and allowing its use in both
transmission and distribution systems. After the FDPF is
performed, the ‘new’ line ﬂows are computed and used to
calculate the corresponding PI value for line i using Eq. (1).
Finally, the PI value is added to a table or list which will be
sorted at the end of the process. After all lines are processed,
the ﬁnal list is sorted from largest to smallest, and the PI
value for the line ia,b connecting buses a and b is assigned to
buses a and b. If a bus is connected to more than one line, the
maximum PI of all the lines connected to the bus is selected
as the CRPI value for the bus.
2) Voltage Deviation Index (VDI): This factor calculates
the voltage deviation for each bus in the CPES from the
nominal 1.0 pu. Similar to CRPI, VDI is considered to be
in the Electrical domain and the Physical environment. The


---

Page 5

---

5
TABLE I
DETAILS OF FACTORS CONSIDERED FOR CPES-QSM COMPUTATION.
STATE ESTIMATION (SE), POWER FLOW (PF), SMART-METERS (SMS), PHASOR MEASUREMENT UNITS (PMUS).
ID
Name
Domain Environment
Measurement
Formula(s)
Target
Data Source
Report Format
CRPI
Contigency Ranking
Performance Index
Electrical
Physical
Voltages & Angles
Eq. (1)
0
SE, PF, IoTs, SMs, PMUs
Decimal
VDI
Voltage Deviation
Index
Electrical
Physical
Voltage Magnitude
Eq. (2)
0
SE, PF, IoTs, SMs, PMUs
Decimal
VCPI
Voltage Collapse
Prediction Index
Electrical
Physical
Voltages/Admittance matrix Eq. (3) - (4)
0
SE, PF, IoTs, SMs, PMUs
Decimal
SVSI
Simpliﬁed Voltage
Stability Index
Electrical
Physical
Voltage Phasors
Eq. (5) - (7)
0
SE, PF, IoTs, SMs, PMUs
Decimal
QCR-B
Quantitative Cyber Risk
Base
IT
Cyber
CVSS v3.1 Vulnerabilities Eq. (12) - (13)
≈0
Cybersecurity Assessment
Decimal
QCR-A
Quantitative Cyber Risk
Attack Graph
IT
Cyber
CVSS v3.1 Vulnerabilities Eq. (13) - (17)
≈0
Cybersecurity Assessment
Decimal
BC
Betweenness Centrality
Graph
Network
Topology
Eq. (9)
≈0
Operation Center
Integer
CC
Closeness Centrality
Graph
Network
Topology
Eq. (10)
≈0
Operation Center
Integer
EBC
Edge Betweenness Centrality
Graph
Network
Topology
Eq. (11)
≈0
Operation Center
Integer
formula to compute the VDI factor is:
V DIk = |1.0 −V mag
k(in pu)|
(2)
where V mag
k(in pu) is the voltage magnitude measured (in pu)
at bus k in the system. The target of the value is 0 since this
would mean the bus is exactly at the 1.0 nominal value. This is
an easy-to-calculate factor that provides important information
related to how far the voltage in a bus is from the nominal
1.0 pu. The speciﬁc details for this factor are shown in Table
I. The goal of this factor is to calculate the voltage deviation
(in pu) of a node/bus.
3) Voltage Collapse Prediction Index (VCPI): This factor
calculates a predicted voltage collapse index, which is de-
signed to determine how close a bus is to voltage collapse.
This factor is based on the technique proposed in [20], which is
an online technique designed to predict voltage collapse. This
factor makes use of voltage magnitudes and voltage angles
measured at the respective buses together with the network
admittance matrix of the system in order to estimate how
close a bus is to voltage collapse when compared to other
buses in the system. The method is considered computationally
efﬁcient for real-time prediction of voltage collapse in EPS
[20] since it only needs real-time voltage measurements for
its computation. The speciﬁc details for the VCPI factor are
shown in Table I. The goal of this factor is to estimate how
close the bus is to voltage collapse and the measurements
used are the voltage phasors at sending & receiving buses,
and admittance matrix. The VCPI factor for bus k (receiving
bus) is calculated with Eq. (3).
V CPIk =
1 −
PN
m=1;m̸=k V
′
m
Vk

(3)
where Vk is the voltage measured at bus k and N is the total
number of buses in the system. The term V
′
m is given by:
V
′
m =
Ykm
PN
j=1;j̸=k Ykj
Vm
(4)
where Vm is the voltage phasor at bus m (sending bus), Ykm
is the admittance between buses k and m, and Ykj is the
admittance between bus k and j. The VCPI factor is computed
for each bus in the system.
4) Simpliﬁed Voltage Stability Index (SVSI): This factor
calculates a simpliﬁed voltage stability index (SVSI) based on
the voltage measurements of the system and load ﬂow results.
This factor is based on the indicator presented in [21], and
the relative electrical distance (RED) concept detailed in [22].
This factor has a similar, but not equal, objective as the VCPI
factor presented previously as it is designed to determine how
stable a bus in the system is, in terms of voltage collapse.
However, the main difference with VCPI is its ability to
estimate the voltage stability of a bus based on the RED to the
nearest generation bus. In other words, it uses the difference in
voltage between the nearest generation bus and the analyzed
bus while comparing them to the maximum voltage change
in the system (measured considering the substation as the bus
with the maximum voltage value). In essence, the estimation
of the voltage stability, using this factor, is directly related
to how well the generation resources can modify and adjust
the voltage at the respective bus. The inputs to compute this
factor are: the voltage phasors (voltage magnitude and angle)
from the closest generator (g), substation (m), and receiving
(k) buses. The admittance matrix is also needed to ﬁnd the
nearest generator to bus k, which in turn, can be determined
using the RED. The details for the SVSI factor are shown in
Table I. The SVSI factor for node k can be computed using:
SV SIk = ∆Vk
βVk
(5)
where Vk is the voltage phasor at bus k, i.e., our analyzed
bus, and β is a correction factor that computes the highest
difference of voltage magnitudes between any two buses in
the system (in the equation, buses m and l). The term β is
computed using:
β = 1 −

max(|Vm| −|Vl|)
2
(6)
Finally, the ∆Vk can be estimated using:
∆Vk ∼= |Vg −Vk|
(7)
where Vg is the voltage phasor of the nearest generator bus
(at bus g) to bus k. This value is computed using the RED
concept that indicates the relative distance of each load bus to
all the generator buses in the system [22], [23].


---

Page 6

---

6
Physical & Cyber Nodes Isomorphic
DG
Load
Cyber 
network
Power
network
Measurement Controller
Fig. 3.
Isomorphic physical and cyber network graphs.
B. Graph-Theory Domain Factors
The Graph-theory Domain factors encompass all factors that
are directly related to the topology of the evaluated network.
The topology of the overall CPES is assumed so that the physi-
cal and cyber networks are isomorphic graphs. This means that
each node in the physical-layer of the system is mapped one-
to-one with a node in the cyber-layer of the system [14]. For
instance, if we assume that the physical graph of the system,
i.e., the power network, is represented by Gp, while the cyber
graph, i.e., the cyber network, is represented by Gc, a bijective
relationship can be deﬁned as:
f : Gp →Gc, |(x, y) ∈Gp ⇒(a, b) ∈Gc
(8)
It is important to remark that the assumption of ‘isomor-
phism’ between the cyber and power networks is only con-
sidered when mapping the cyber elements with power sys-
tems components. This assumption ensures that each physi-
cal (power system) node has a representative ‘mapped’ cyber
node, which in turn, can be composed of various devices such
as multiple measurement and control devices. This mapping al-
lows us to include very detailed cyber models, while retaining
the overall structure of the system and thus, lets us determine
how a compromised cyber node may directly affect the physi-
cal system mapped to it. In other words, isomorphism is only
maintained between the primary physical and cyber graphs and
minor graphs, composed by multiple devices, can exist inside
nodes of these primary graphs. Fig. 3 shows an example of
the isomorphic power and cyber graphs. This assumption is
not made for the communication topology between devices, in
fact, various types of communication topologies, such as star,
ring, or point-to-point, can exist without any discrepancies.
Based on the assumptions described above, different graph-
theory factors are considered to be included in the compu-
tation of the CPES-QSM. These factors are the betweenness
centrality (BC), the closeness centrality (CC), and the edge
betweenness centrality (EBC) of the graph. To calculate these
factors, we consider a graph G composed of N nodes and E
edges. The order of this graph is given by G = (N, E).
1) Betweenness Centrality (BC): This factor estimates the
importance, i.e., the shortest-path betweenness centrality, of
the analyzed node on the overall graph. It quantiﬁes the num-
ber of times a particular node acts as a bridge along the shortest
path between two other nodes. The BC of a node v can be
calculated as the summation of the fraction of all-pairs shortest
paths that pass through v:
BC(v) =
X
s̸=t̸=v∈V
σ(s, t|v)
σ(s, t)
(9)
where s, t, and v are nodes in the set of nodes V. The term
σ(s, t) is the total number of shortest paths between nodes s
and t, and the term σ(s, t|v) is the number of those paths that
pass through node v. If s = t, then σ(s, t) = 1 and if v ∈s, t
then σ(s, t|v) = 0 [24].
2) Closeness Centrality (CC): This factor estimates the
mean distance (geodesic path) from a vertex/node v to every
other node. The more ‘central’ a node is, the closer it is to all
other nodes, thus, the more important in terms of centrality to
the overall graph. The CC of node v can be calculated as:
CC(v) =
n −1
Pn−1
u=1 d(u, v)
(10)
where d(u, v) is the shortest-path between node u and v, and
n is the number of nodes that can be reached from node v. A
higher value of CC indicates higher centrality [25].
3) Edge Betweenness Centrality (EBC): This factor es-
timates the importance of the edges/lines connected to the
analyzed node. The EBC is a factor very similar to BC but
calculated for the edges of the graph. The EBC of an edge e
can be calculated as the sum of the fraction of all-pairs shortest
paths that pass through the edge e. This can be calculated as:
EBC(e) =
X
s̸=t∈V
σ(s, t|e)
σ(s, t)
(11)
where s and t are two arbitrary nodes that exist in the set of
nodes V. The term σ(s, t) is the total number of shortest paths
between nodes s and t, and σ(s, t|e) is the number of those
paths that pass through the edge e. The maximum EBC of all
the edges connected to a particular node v is the EBC value
assigned to that node v; since for our purposes, we are mainly
interested in characterizing nodes instead of lines. The details
for the BC, CC, and EBC factors are shown in Table I.
C. Cyber Domain Factors
The Cyber Domain factors encompass all factors that are
directly related to the cyber-layer structure and operation of the
CPES. These factors provide a quantitative way of factoring
cybersecurity risks that IoT systems introduce into EPS. The
processes followed to calculate the quantitative cyber risk base
model (QCR-B) factor or the quantitative cyber risk attack
graph-based model (QCR-A) factor are inspired from the cyber
risk assessment methodology presented in [26]. The CVSS
v3.1 is used as the scoring system that quantiﬁes the cyber risk
of the vulnerabilities that exist in the system [27]. Essentially,
it estimates the difﬁculty of vulnerability exploitation for each
electronic device that exists in a particular node of the cyber-
layer of the CPES. The general cyber risk formula used for
both QCR-A and QCR-B is QCRB/A = P × I, where QCR
is the risk, P is the probability, and I is the impact. The
metric values shown in Table II are used to calculate the P
variable according to its corresponding calculation process.
More details regarding these metrics are given in [28].


---

Page 7

---

7
TABLE II
EXPLOITABILITY METRICS IN COMMON VULNERABILITY SCORING
SYSTEM VERSION V3.1 (CVSS V3.1)
Score
System
Metric
Abb.
Metric
Value
Numerical
Value
CVSS
v3.1
Attack
Vector
AV
Network
0.85
Adjacent
network
0.62
Local
network
0.55
Physical
0.2
Attack
Complexity
AC
Low
0.77
High
0.44
User
Interaction
UI
None
0.85
Required
0.62
Privileges
Required
PR
None
0.85
Low
0.62 if S = Unchanged
0.68 if S = Changed
High
0.27 if S = Unchanged
0.50 if S = Changed
1) Quantitative Cyber Risk Base Model (QCR-B): This
factor estimates the cyber risk of a cyber node based on CVSS
v3.1 and the vulnerabilities identiﬁed in the device that exists
in that particular node. This is designed to be the base model of
the QCR factor that should be used at nodes that are composed
of only one IoT device or access point. The probability P in
the risk formulation calculation can be computed as:
P = AV × AC × UI × PR
(12)
The impact I of the risk formula is computed using the
graph-theory factors presented in the previous subsection times
the total bulk impact on the system.
I = (BC + CC + EBC) × P %
g/l
(13)
where P %
g/l is the generation or load percentage of the total
generation or load in the system. The risk assessment model
that describes this calculation process is presented in Fig. 4. As
seen in this ﬁgure, this factor estimates what is the probability
or likelihood a vulnerability is exploited on the cyber-physical
assets, thus causing an impact on the system. Nodes with high
P values (very easy to compromise) and generating/consuming
a high percentage of power, with respect to the total load in
the system (high I values), are the nodes that are considered
more dangerous to the cyber-secure operation of the system.
2) Quantitative Cyber Risk Attack Graph-based Model
(QCR-A): This factor estimates the cyber risk of a cyber
node based on CVSS v3.1 and the vulnerabilities identiﬁed
in multiple IoT devices that exist in that particular node. This
is designed to be the model that should be used at nodes that
are composed of multiple electronic devices or access points
where serial and parallel attack graphs can be modeled. Fig. 5
shows the QCR-A risk assessment process, which differs from
the QCR-B process presented previously due to the inclusion
of attack graphs that model the path followed by threats that
compromise the devices that make up the cyber node.
The probability P in the risk formulation calculation for
this version of the factor needs to consider the attack graph
method followed to compromise the vulnerabilities in the
corresponding devices. Depending on the movement method
of the threat, i.e., serial or parallel, the leading probability
Vulnerability on 
device
Threat
exploits with 
a probability
causing
Impact in 
system
Fig. 4. Quantitative Cyber Risk Base Model (QCR-B) Probability and Impact.
Vulnerability on 
device
Threat
exploits with 
a probability
causing
Impact in 
system
follows
Attack
Graph
Fig. 5.
Quantitative Cyber Risk Attack Graph-based Model (QCR-A)
Probability and Impact.
P is calculated differently. The ‘leading probability’ term is
deﬁned as the multiplication of all the probabilities leading to
the targeted device. The probability P for a serial movement
is calculated by multiplying the leading probabilities with the
interim probability at the last device, where the interim prob-
ability is deﬁned as the probability of the device calculated
from the CVSS scores of the device’s vulnerabilities. The
probabilities for a cyber-node with n devices are calculated
as follows:
P leading
n
=
n−1
Y
i=1
Pi
(14)
P ag
n
= P leading
n
× Pn
(15)
where P ag
n is the total serial attack-graph probability of a threat
that ends up at device #n. Pn is the interim probability of
device #n and P leading
n
is the leading probability for the path
ending at device #n. On the other hand, for a parallel move-
ment of the threat, the total parallel attack-graph probability
is calculated by multiplying the parallel probabilities of the
leading devices as follows:
P leading
n
= 1 −
n−1
Y
i=1
(1 −Pi)
(16)
P ag
n
= P leading
n
× Pn
(17)
The impact I of QCR-A can be estimated using the same
approach used by the QCR-B factor, i.e., Eq. (13). In a real-
time application, both of these factors will be mainly affected
by the impact (I), which changes according to the percentage
of generation or load (at the speciﬁc time) with respect to the
total load in the system. The speciﬁc details for these factors
are shown in Table I.
D. Cyber-Physical Energy System Quantitative Security Met-
ric (CPES-QSM) Computation
After the required factors are computed, they are combined
using an MCDM approach called the Choquet Integral (CI)
[29]. The main advantage of using the CI for aggregating
the factors is that it allows the aggregation of criteria (i.e.,
factors), xn, that can have different units, with the objective
of providing an overall score. The CI acts as an aggregation
function deﬁned with respect to fuzzy measures. A fuzzy
measure (ν) is deﬁned as a set function that acts on the domain
of all possible combinations of a criteria set [30]. In other
words, fuzzy measures can be thought of as a function that


---

Page 8

---

8
provides a value to every possible combination of inputs. The
complexity of the set is determined by the 2n subsets that
compose it, where n is the number of criteria, i.e., the number
of input factors in the aggregation.
Formally, a general fuzzy measure is deﬁned as a set func-
tion ν : 2n →[0, 1], where N = {x1, x2, ..., xn} represents the
set that contains all criteria. The function ν must be mono-
tonic (i.e., ν(A) ≤ν(B) whenever A ⊂B), and must satisfy
ν(∅) = 0 and ν(N) = 1, where sets A and B contain combi-
nations of criteria. Considering that A ⊂B ⊂N, ν(A) repre-
sents the fuzzy measure or ‘importance’ of the group/subset
A. Fuzzy measures give weights to all possible combinations
of criteria, which offers great ﬂexibility when aggregating dif-
ferent types of criteria using the CI for decision-making pro-
cesses.
The initial weights (i.e., fuzzy measures) for the individual
criteria (e.g., ν({x1}), ν({x2}), etc.) must be assigned by
‘experts’, which are in charge of giving importance to the
respective individual factors. This ‘weighting’ process can be
performed iteratively using a HiTL approach. On the other
hand, the fuzzy measures of the sets that combine multiple
factors (e.g., ν({x1, x2}), ν({x2, x3}), etc.) are computed us-
ing the interaction index λ estimated as:
λ + 1 =
n
Y
i=1
(1 + λνi),
where −1 ≤λ < 0
(18)
The interaction index measures the interaction among criteria,
i.e., it can be considered as a measurement of the interaction
between criteria (factors) in the decision-making process. If
λ < 0, a correlating relationship between the criteria exists.
If λ ≈0, no relationship between the factors exists, i.e., they
contribute independently to the score [29].
Using the calculated interaction index (λ), the fuzzy mea-
sures of sets that combine multiple factors are calculated as:
ν({x1, x2, ..., xn}) = 1
λ

n
Y
i=1
(1 + λνi) −1

(19)
Finally, using the calculated fuzzy measures and the values
of the factors x1, x2, ..., xn, the CI can be computed as:
CIν =
n
X
i=1
[xi −xi−1]ν(Fi)
(20)
where x0 = 0 by convention, and Fi = i, ..., n is the subset
of indexes of the n −i + 1 largest component. The output of
the CI usually lies in the unit interval [0, 1]; however, other
choices can be deﬁned [29]. A simple numerical example of
how to compute λ and all the fuzzy measures of a set of three
criteria (i.e., three factors) is presented below.
Let us assume that there exist a set of three criteria
x1, x2, x3 that we want to combine using the CI. To compute
the CI, we must ﬁrst compute the fuzzy measures using Eq.
(19) and their corresponding λ using Eq. (18). To do this, fuzzy
measures for the individual inputs x must be assigned. These
are assigned as ‘expert’ weights (i.e., fuzzy measure values)
given by experts. So, ν0 = 0, ν1 = 0.42, ν2 = 0.5, and
ν3 = 0.62, where ν0 ≡ν({∅}), ν1 ≡ν({x1}), ν2 ≡ν({x2}),
and ν3 ≡ν({x3}). Then, using Eq. (18), λ can be solved for
as λ + 1 = (1 + λν1)(1 + λν2)(1 + λν3). For this particular
example, λ = −0.748. Finally, using the calculated λ, we
can use Eq. (19) to compute the remaining fuzzy measure
values for all the combinations of the set of criteria. The
corresponding values calculated for the example given are
ν({x1, x2}) = 0.75, ν({x1, x3}) = 0.82, ν({x2, x3}) = 0.86,
and ν({x1, x2, x3}) = 1.0. With the fuzzy measure (i.e,
weights) calculated, the CI can be then computed for any input
values x1, x2, and x3 using Eq. (20).
For our case, the CI is the method used to combine the
different Electrical, IT, and Graph-theory factors that charac-
terize the current state of a CPES, and thus compute the CPES-
QSM for each node that exists in the CPES. For instance,
the factors used as inputs to the CI that produces the CPES-
QSM for node i could be xi
1 = CRPIi, xi
2 = QCR-Bi,
xi
3 = V DIi, xi
4 = SV SIi, and xi
5 = V CPIi. Each one
of these factors is given a corresponding ‘importance’ or
‘expert’ weight (fuzzy measure) ν1, ν2, ..., ν5. It is important
to note that other papers in the literature, such as [14] and
[13], have also used the CI approach for combining different
factors in the process of computing cyber-physical resilient
analysis metrics, due to the CI characteristics of allowing the
aggregation of non-additive nonlinear criteria without assum-
ing independence of each criterion. More details about the
main differences between our proposed approach and works
in the literature are speciﬁed in Section I.
III. CYBER-CONSTRAINED ACOPF FORMULATION
This section presents an overview of the proposed cyber-
constrained ACOPF
(C-ACOPF) formulation. Subsection
III-A focuses on presenting and discussing the traditional
ACOPF (T-ACOPF) formulation. Subsection III-B presents
the modiﬁcations made to the traditional mathematical for-
mulation of the ACOPF so that it can take into account
both physical and cyber operating factors of the CPES being
optimized; allowing for the consideration of cyber factors in
its decision-making process.
A. Traditional ACOPF Full Formulation
The classical ACOPF formulation can be written as pre-
sented in Eqs. (21) - (30). Eq. (21) is the objective cost
function of the system, Eq. (23) - (25) represent the operational
power constraints, Eq. (26) - (29) represent the branch power
and current constraints, and Eq. (30) represent the voltage
angle difference constraints. There exist other formulations
and extensions such as security-constrained optimal power
ﬂow, DC OPF, and other relaxations [31]–[34]. However, our
proposed C-ACOPF is based on the traditional nonconvex
ACOPF polar formulation presented.
min
X
k∈G
c2k(ℜ(Sg
k))2 + c1k(ℜ(Sg
k)) + c0k
(21)
S.t.:


---

Page 9

---

9
θr = 0, ∀r ∈R
(22)
Sgl
k ≤Sg
k ≤Sgu
k , ∀k ∈G
(23)
vl
i ≤|Vi| ≤vu
i , ∀i ∈N
(24)
X
k∈Gi
Sg
k −
X
k∈Li
Sd
k −
X
k∈Si
(Y s
k )∗|Vi|2 =
X
(i,j)∈Ei∪ER
i
Sij
, ∀i ∈N
(25)
Sij = (Yij + Y c
ij)∗|Vi|2 −Y ∗
ijViV ∗
j , ∀(i, j) ∈E
(26)
Sji = (Yij + Y c
ji)∗|Vj|2 −Y ∗
ijV ∗
i Vj, ∀(i, j) ∈E
(27)
|Sij| ≤su
ij, ∀(i, j) ∈E ∪ER
(28)
|Iij| ≤iu
ij, ∀(i, j) ∈E ∪ER
(29)
θ∆l
ij ≤(ViV ∗
j ) ≤θ∆u
ij , ∀(i, j) ∈E
(30)
B. Cyber-Constrained ACOPF Formulation
From the formulation presented in the last subsection, it
can be observed how the T-ACOPF formulation essentially
prioritizes minimizing a cost function that only takes into
account the physical states of the system. However, the C-
ACOPF formulation presented in this subsection is intended
to include the cyber-physical perspective of the system. This
perspective is facilitated by using the CPES-QSM, presented in
the previous section, as a proxy for the cyber-physical factors
operating conditions that make up the CPES. The general
formulation in Eq. (21)-(30) can be stated in a simpliﬁed form
as:
min C(x)
(31)
s.t. G(x) = 0
(32)
H(x) ≤l
(33)
xmin ≤x ≤xmax
(34)
where C(x) is the cost function, G(x) are the equality
constraints, and H(x) are the inequality constraints of the
problem. The state variables consist of x for a particular
generation node k. Note that the metric can also be extended
to controllable load buses. The CPES-QSM is included in the
formulation to bias the optimization solution towards ‘reliable’
generation sources, i.e, the OPF formulation will aim to de-
crease the power injections from buses where the CPES-QSM
value are above a particular threshold. The variable ρ provides
the threshold value for which a bus with a CPES-QSM score
above this threshold is considered ‘unreliable’. In practice, this
value must be determined by expert operators in charge of
managing the system being analyzed and may be different
for different systems. Considering the particular threshold
deﬁned, the CPES-QSM score (CQk) directly impacts the
upper bounds of the state variables P g
k and Qg
k as a scalar
multiple. It is important to note that the CQk value/score is
computed using Eq. (20), i.e., CQk = CI. The variables ζ
and α are deﬁned for the lower and upper bounds of the
state variables. The new cyber-physical variables ρ, α, ζ, and
CQk are included in the inequality constraints of the simpliﬁed
ACOPF formulation by expanding Eq. (33) as follows,
(1 −ζ)P gl
k ≤P g
k ≤αP gu
k , ∀k ∈G
(35)
(1 −ζ)Qgl
k ≤Qg
k ≤αQgu
k , ∀k ∈G
(36)
α(ρ,CQk,ζ)=







0,
if CQk ≥ρ for ζ = 1
( P gl
k
P gu
k , 1),
if CQk ≥ρ for ζ = 0
1,
if CQk <ρ for ζ = 0
(37)
The new lower bounds of the state variables become
(1 −ζ) × P gl
k
and (1 −ζ) × Qgl
k . Similarly, the new upper
bounds are α × P gu
k
and α × Qgu
k . The value of CQk
changes according to the current cyber-physical state of the
system and differs according to different types of attacks,
e.g., data integrity attacks (DIAs), data availability attacks
(DAAs), etc, which directly affect the QCR-A/B factors. The
generation limits inequality condition of Eq. (23) is modiﬁed
with Eqs. (35)–(37), while the other inequality conditions of
the problem remain the same. The binary variable ζ determines
if the generator k must be disabled or adjusted according
to HiTL preferences, e.g. if a generator is considered fully
compromised and must be disconnected (ζ = 1) instead of
just curtailed (ζ = 0).
As seen in the above formulation, ρ deﬁnes the boundaries,
which must be deﬁned by experts operating the system,
between a ‘reliable’ and an ‘unreliable’ generation node. If the
CPES-QSM value (shown here as CQ) is greater than or equal
to ρ then the node is considered ‘unreliable’ and its generation
is either curtailed to a range of its minimum to maximum
values or completely turned off. On the other hand, if CQ is
lower than ρ then the node is considered ‘reliable’ and there
is no change in its maximum dispatch capacity. It is important
to note that the curtailment of the generators can be deﬁned as
a continuous function that curtails generation according to a
speciﬁc percentage value instead of P gl
k . By constraining the
generation in ‘unreliable’ nodes, the OPF solution provides a
more ‘secure’ solution that relies on the generation of more
reliable nodes at the cost of more expensive generation that
yields a higher traditional cost. The ﬁnal C-ACOPF solution
makes the system more secure in terms of the cyber-physical
security of the CPES while sacriﬁcing generation cost.
In terms of complexity, it should be noted that the C-ACOPF
problem is unchanged from the original ACOPF, as no new
constraints are added. However, the feasible solution space for
the optimization solver is reduced based on the newly added
cyber-physical variables. The C-ACOPF is still a fully non-
linear nonconvex formulation that is solved using a primal-
dual interior-point method.
IV. EXPERIMENTAL SETUP AND CASE STUDIES
The code used to run the case studies presented in this
section can be found in [35]. The case study presented here
is based on the IEEE RTS-24 test system, which is the
ﬁrst part of the IEEE RTS-96 test system presented in [36].
This system has 10 generators, 1 slack bus (bus #12), 17
loads, and 32 transmission lines. The speciﬁc loads, lines,
and generators capacities/parameters are taken from the case
model ‘case24 ieee rts.m’ available in MATPOWER [37].


---

Page 10

---

10
TABLE III
TRADITIONAL ACOPF RESULTS FOR IEEE RTS-24 BUS TEST SYSTEM.
Gen # Bus # P (MW) Q (MVAR) |V |pu ∠V
0
0
192.00
13.42
1.050
-7.38
1
1
192.00
10.86
1.050
-7.47
2
6
131.60
66.68
1.022 -17.84
3
13
0.00
172.03
1.049
1.02
4
14
215.0
110.00
1.042
10.03
5
15
155.00
80.00
1.046
8.98
6
17
400.00
69.02
1.050
14.83
7
20
400.00
-12.42
1.050
15.64
8
21
300.00
-39.00
1.050
21.27
9
22
660.00
70.37
1.050
9.80
10
(slack)
12
258.54
53.05
1.020
0.00
For this case study, we assume that every physical node
that exists in the electrical transmission network is mapped
with a cyber node composed of just one IoT device at the
cyber-layer of the CPES. This will greatly simplify the
cybersecurity model of the system for explanation purposes
since only the QCR-B factor will be used to characterize the
vulnerabilities on the node; but, for more complex CPES,
the QCR-A model can be used to model complex attack
graph-based vulnerabilities that exist in multiple IoT devices.
A. Traditional ACOPF Results
In order to evaluate the advantages, in terms of the CPES
security, of using the proposed C-ACOPF formulation, the
solution of the T-ACOPF formulation is used as a baseline.
The T-ACOPF solution is obtained by running the ACOPF
PandaPower solver [38], which uses the primal-dual interior-
point method implemented using the Python Interior Point
Solver (PIPS) in the PyPower package. Table III shows the
generator dispatch solution for the T-ACOPF formulation. The
total cost for the solution is $49,903.5432. Fig. 6 shows the
bus voltages and line congestion of the solution.
B. Cyber-Constrained ACOPF using CPES-QSM
In order to compute the C-ACOPF solution for the IEEE
RTS-24 test system, we must ﬁrst calculate the CPES-QSM
metric value for each node in the system and ‘adjust’ the
corresponding generation and power ﬂow of ‘unreliable’ nodes
identiﬁed based on the current status of the system. The ﬁrst
step in the process is to select the factors to be considered for
this case study and assign the respective ‘expert’ weights for
each one of these factors. The factors selected for this case
study are: CRPI, QCR-B, VDI, SVSI, and VCPI. The ‘expert’
weights, i.e., fuzzy measure values, assigned to each one of
these factors are: [0.26, 0.55, 0.61, 0.65, 0.66], respectively. A
higher value represents higher individual importance of the
factor in the ﬁnal score computation. These weights were
estimated after running multiple test cases and manually evalu-
ating the operating conditions of the test system. Based on the
number of factors used, there are 25 = 32 total fuzzy measure
values that go from ν(∅) = 0.0 to ν({x1, x2, x3, x4, x5}) =
1.0. Some of the intermediate values are ν({x1, x2}) = 0.669,
ν({x1, x3}) = 0.714, and, ν({x1, x4}) = 0.743. Some of
them are not listed due to space limitations, but their calcula-
tion is trivial. The corresponding λ computed is λ = −0.983.
TABLE IV
CPES-QSM (CQ) RESULTS FOR IEEE RTS-24 BUS TEST SYSTEM.
TRADITIONAL (T-ACOPF) (REFERRED AS T) VS CYBER-CONSTRAINED
ACOPF (C-ACOPF) (REFERRED AS C).
Bus
#
CRPI
QCR-B
VDI
SVSI
VCPI
CQ
Case
T
C
T
C
T
C
T
C
T
C
T
C
0
0.11 0.11
0.0
0.0
0.05 0.05
0.0
0.0
0.0
0.0
0.05 0.05
1
0.22 0.22
0.0
0.0
0.05 0.05
0.0
0.0
0.0
0.0
0.08 0.08
2
0.12 0.12 0.03 0.03
0.01 0.01 0.02 0.0
0.01 0.01
0.05 0.04
3
0.11 0.11 0.02 0.02
0.02 0.02 0.01 0.0
0.02 0.02
0.04 0.04
4
0.11 0.11 0.01 0.01
0.03 0.03 0.01 0.01
0.01 0.01
0.05 0.05
5
0.47 0.47 0.02 0.01
0.03 0.03 0.01 0.01
0.02 0.02
0.14 0.14
6
0.09 0.09 0.01 0.01
0.05 0.05
0.0
0.0
0.03 0.03
0.04 0.04
7
0.11 0.11 0.02 0.02
0.01 0.01 0.02 0.02
0.03 0.03
0.05 0.05
8
0.12 0.12 0.03 0.03
0.02 0.02 0.01 0.01
0.01 0.01
0.04 0.04
9
0.47 0.47 0.03 0.03
0.05 0.05 0.03 0.03
0.02 0.02
0.15 0.15
10
0.19 0.19 0.03 0.03
0.02 0.02 0.01 0.01
0.02 0.02
0.07 0.07
11
0.40 0.40 0.02 0.02
0.01 0.01
0.0
0.0
0.02 0.02
0.12 0.12
12
0.53 0.53 0.01 0.01
0.02 0.02
0.0
0.0
0.0
0.0
0.15 0.15
13
0.23 0.23
0.0
0.0
0.04 0.04
0.0
0.0
0.01 0.01
0.08 0.08
14
1.0
1.0
0.02 0.0
0.04 0.04
0.0
0.0
0.0
0.0
0.27 0.27
15
0.50 0.50 0.20 0.07
0.05 0.04
0.0
0.0
0.0
0.0
0.21 0.16
16
0.41 0.41 0.02 0.02
0.05 0.05 0.03 0.03
0.0
0.0
0.13 0.13
17
0.1
0.1
0.02 0.02
0.05 0.05
0.0
0.0
0.0
0.0
0.05 0.05
18
0.50 0.50 0.02 0.02
0.04 0.04 0.03 0.02
0.0
0.0
0.15 0.15
19
0.1
0.1
0.02 0.02
0.04 0.04 0.03 0.03
0.0
0.0
0.05 0.05
20
0.31 0.31 0.04 0.04
0.05 0.05
0.0
0.0
0.0
0.0
0.10 0.10
21
0.14 0.14
0.0
0.0
0.05 0.05
0.0
0.0
0.0
0.0
0.06 0.06
22
0.53 0.53 0.02 0.02
0.05 0.05
0.0
0.0
0.01 0.01
0.16 0.16
23
1.0
1.0
0.02 0.02
0.01 0.01 0.01 0.01
0.02 0.02
0.27 0.27
Using the λ and fuzzy measure values estimated, we can
proceed to evaluate the current status of the operating CPES
by calculating the CPES-QSM metric value for each node in
the system. It is important to remark that at this point, the
weights or fuzzy measure values are set and do not need
to be recomputed every time the CPES-QSM metric value
is estimated. Hence, for computing the CPES-QSM metric
for each node, the current operating measurements for each
factor considered are obtained and processed to compute the
corresponding CPES-QSM for that speciﬁc node. For this
case study, an ACPF is run in order to estimate the current
operating measurements for each node, which in turn are used
to compute each factor considered. It is important to note that
in a ‘real’ system, these values are obtained either through IoTs
and/or SE. Table IV presents the calculated CPES-QSM values
for each node in the system according to the corresponding
factors computed. The time execution of the T-ACOPF is
1.1209 seconds, while the time execution of the entire CPES-
QSM value computation and C-ACOPF is 1.3647 seconds.
The speciﬁcations of the machine in which the tests were
performed are: CPU - AMD 4900HS clocked at 3.00 GHz
and 16 GB RAM. Based on the tests conducted, the entire
CPES-QSM computation and C-ACOPF process seemed to
be 0.82x slower, on average, than the T-ACOPF process.
As seen in Table IV, and using a ρ = 0.2 value (where ρ
is the limit given by experts that provides the limit difference
between a ‘reliable’ node and an ‘unreliable’ node), there are
a few nodes that can be categorized as ‘unreliable‘. This is
due to the fact that the estimated CPES-QSM value (i.e, CQ)
is higher than the limit given by the ρ = 0.2, and in turn,
some of the factors of these nodes tend to be higher than the


---

Page 11

---

11
6
7
5
9
12
11
22
19
18
10
3
8
13
15
16
21
17
20
14
23
0
2
1
4
7.57%
34.67%
6
7
5
9
12
11
22
19
18
10
3
8
13
15
16
21
17
20
14
23
0
2
1
4
7.14%
35.93%
Traditional ACOPF
Cyber-Constrained ACOPF
1.1
100
80
60
40
20
0
1.05
0.9
0.95
Line Loading [%]
1
Bus Voltage [pu]
Fig. 6. Traditional ACOPF result (left) vs. Cyber-Constrained ACOPF (right) result for IEEE RTS-24 bus test system. The shields represent the cyber-status
of each node in the system. Green means low QCR and red means high QCR.
rest, making them more susceptible to be targeted by attackers.
‘Case’ T represents the case where the CPES-QSM value is
estimated based on the T-ACOPF. ‘Case’ C represents the case
where the CPES-QSM value is estimated after the C-ACOPF
is run and adjustments are made based on Eqs. (35)-(37).
It should be noted that the values in the table were cut to
two signiﬁcant ﬁgures due to space limitations. Results are
normally presented using 5-6 signiﬁcant ﬁgures, so further
minor differences can be observed in some cases. For this case
study, a DAA-type attack, e.g., Denial-of-Service (DoS), is
considered as the threat to the system. The threat model for the
cyberthreat is based on the threat model presented in [1]. This
DAA threat has the capability of exploiting the vulnerabilities
of the affected node(s) making them unresponsive (by delaying
control and measurements) to operating commands. In our
speciﬁc case, all nodes except bus #15 (the affected node)
are considered to have a very ‘secure’ operation based on
the QCR-B factor estimated. These are categorized using
the following parameters {AV: Local, PR: High, AC: High,
UI: Required}, while bus #15 is categorized as ‘unreliable’
based on {AV: Network, PR: None, AC: Low, UI: None}
vulnerabilities exploited by the threat. The results obtained
showcase how the cyber factors are taken into consideration
when deciding the optimal AC power ﬂow of a CPES that is
currently under attack from a cyber perspective. Table V shows
the generator dispatch solution for the C-ACOPF formulation.
The total cost for the solution is $53,621.1357.
Fig. 6 shows the bus voltages and line congestion of the C-
ACOPF solution. As seen in the ﬁgure, the OPF solution gets
adjusted to take into account the ‘unreliable’ nature of bus #15
(currently under attack), which in turn derives from the high
cyber and physical factors. The power ﬂows from bus #15 to
bus #13 and from bus #15 to #18 get reduced by ≈8%, while
the power ﬂows from bus #14 to bus #15 and from bus #16
to bus #15 increase by ≈7% and 0.45%, respectively. The
corresponding CPES-QSM values of the cyber-constrained
solution are shown in the last column of Table IV. As seen,
the CQ value for node #15 (affected) decreased from 0.21 to
0.16, putting it below the ρ threshold. These results clearly
demonstrate how the C-ACOPF increases the generation from
other more ‘reliable’ sources and takes into account the current
status of not only the physical system but the cyber-system
components; thus, producing results that make the system
TABLE V
CYBER-CONSTRAINED ACOPF RESULTS FOR IEEE RTS-24 BUS TEST
SYSTEM
Gen # Bus # P (MW) Q (MVAR) |V |pu ∠V
0
0
192.00
12.55
1.050
-8.33
1
1
192.00
10.54
1.050
-8.40
2
6
141.64
64.54
1.024 -17.76
3
13
0.00
146.10
1.044
-0.79
4
14
215.0
110.00
1.042
7.47
5
15
54.30
80.00
1.044
6.32
6
17
400.00
73.54
1.050
12.22
7
20
400.00
-10.61
1.050
13.05
8
21
300.00
-38.39
1.050
18.67
9
22
660.00
68.44
1.050
8.40
10
(slack)
12
344.70
43.15
1.021
0.00
more secure and resilient from the cybersecurity point of view.
It is important to note how the CPES-QSM values for nodes
#14 and #23 are still over the ρ threshold; however, these
cannot be directly adjusted based on the ACOPF solution since
their criticality is derived from the CRPI factor, which in turn,
is related to the physical topology of the system. This factor
can be reduced by performing other control operations that
directly change the topology of the system, but these control
operations are not in the scope of this paper. Future work will
focus on exploring other control solutions that can be adjusted
based on the CPES-QSM metric.
C. Effects of Cyberattacks in Traditional ACOPF and Cyber-
Constrained ACOPF Formulations
In this subsection, the effects that a cyberattack may have
in a system, as the one evaluated in the previous subsection,
are explored. The effects are evaluated by comparing the
frequency and voltage effects of the system when a cyberattack
compromises a vulnerable node. For this case study, we use the
dispatch results from the T-ACOPF and the C-ACOPF in order
to examine the different responses these systems would have
when a DAA threat (capable of exploiting the vulnerabilities
of the affected node(s) by making them unresponsive via
the delay of control and measurements) is deployed. More
speciﬁcally, in this case, the cyber threat compromises the
vulnerable generator at the ‘unreliable’ bus identiﬁed by the
C-ACOPF formulation, i.e., generator at bus #15, by making
it inoperable for 5 seconds. The threat model of such an attack


---

Page 12

---

12
10
20
30
40
50
Time (s)
59.85
59.9
59.95
60
60.05
60.1
60.15
Frequency (Hz)
Attack at Bus #15 Generator
UL
LL
C-ACOPF
T-ACOPF
Fig. 7.
Frequency response comparison for both T-ACOPF and C-ACOPF
solutions when a 5 seconds cyberattack is used to compromise the generator
at bus #15. (UL means upper limit while LL means lower limit.)
10
20
30
40
50
Time (s)
0.94
0.96
0.98
1
1.02
1.04
1.06
Voltage(pu)
T-ACOPF: Attack at Bus #15 Generator
UL
LL
Fig. 8.
Voltage values (in pu) for T-ACOPF solution when a 5 seconds
cyberattack is used to compromise the generator at bus #15. Voltage of all
buses in the system are represented by different color lines. (UL means upper
limit while LL means lower limit.)
is similar to existing attacks found in the literature [1], [39].
The time-domain simulation of the IEEE RTS-24 test system
used for this analysis is performed using the Power System
Analysis Toolbox (PSAT) [40].
Fig. 7 showcases the differences in the frequency response
for both the T-ACOPF and C-ACOPF solutions when a 5
seconds DAA is used to compromise the IoT(s) connected to
the generator at bus #15. The cyberattack was carried out at
t=30s to t=35s. As seen in the ﬁgure, the frequency variation
of the T-ACOPF solution system is signiﬁcantly higher than
the frequency variation caused by the cyberattack in the C-
ACOPF solution system. The frequency even crosses for an
instance the upper limit (at 60.1 Hz) of the system’s frequency.
Figs. 8 and 9 depict the voltages for all the nodes in the
system for the time period evaluated. As observed in these
ﬁgures, the voltage variations are also much more notable in
the T-ACOPF system when compared to the C-ACOPF system.
In fact, in the C-ACOPF solution system, the cyberattack is
barely noticeable, in terms of voltage values.
These results clearly demonstrate that the use of the pro-
posed C-ACOPF formulation, enhanced by the CPES-QSM,
has major advantages when compared to the T-ACOPF for-
mulation due to the fact that this new formulation and metric
consider not only the physical state of the system but also the
current cyber state in order to improve control and operation
decisions that could make the system more secure and stable.
In this case study, the C-ACOPF correctly cataloged bus #15 as
an ‘unreliable’ node due to its high QCR-B value and limited
10
20
30
40
50
Time (s)
0.94
0.96
0.98
1
1.02
1.04
1.06
Voltage(pu)
C-ACOPF: Attack at Bus #15 Generator
UL
LL
Fig. 9.
Voltage values (in pu) for C-ACOPF solution when a 5 seconds
cyberattack is used to compromise the generator at bus #15. Voltage of all
buses in the system are represented by different color lines. (UL means upper
limit while LL means lower limit.)
its generation output to a minimum. So, when the node got
compromised (attacked by an adversary), the system did not
suffer much and was able to endure any possible subsequent
damage. Since the T-ACOPF solution was not ‘cyber aware’
as the C-ACOPF solution, the system presented a higher
variability when the attack happened and a longer attack (e.g.,
15+ seconds) may have caused more substantial damage. The
loss of 54.30 MW generation is not the same as the loss of
155 MW generation and this is reﬂected in the results.
V. CONCLUSIONS
In this paper, a quantitative cyber-physical security metric
for CPES and a cyber-constrained ACOPF formulation are
proposed to cope with the security challenges of modern
CPES. The CPES-QSM cyber-metric is designed to incorpo-
rate diverse types of critical factors affecting the cybersecurity
and operation of CPES while providing a quantitative value
to the cyber and physical status of the operating CPES. This
cyber-metric is integrated, as a proxy, to transform the tradi-
tional ACOPF formulation into a cyber-constrained ACOPF
formulation designed to produce a more secure operating
point that considers vulnerabilities existing in IoT and OT
devices deployed in the system’s physical and cyber networks.
Experimental case studies, based on a DAA-type of attack and
using the IEEE RTS-24 bus system, are presented to show the
effectiveness of the proposed CPES cyber-metric. The results
of the case study are discussed and evaluated against the
traditional ACOPF formulation, in terms of cost, line loading
percentage, and CPES security.
Based on tests conducted, some of the factors considered
when computing the CPES-QSM may have a significant im-
pact in the scalability of the proposed method. Therefore, fu-
ture work will focus on exploring the scalability of the pro-
posed approach by evaluating its performance in large-scale
integrated transmission-distribution systems using tools such
as PowerModelsITD.jl1. Furthermore, the stability of the CI
will be examined for the case when a large number of factors
are considered simultaneously.
1https://github.com/lanl-ansi/PowerModelsITD.jl


---

Page 13

---

13
ACKNOWLEDGMENT
The authors are thankful to Dr. David Fobes from Los
Alamos National Laboratory for his valuable insights and
recommendations.
REFERENCES
[1] I. Zografopoulos, J. Ospina, X. Liu, and C. Konstantinou, “Cyber-
physical energy systems security: Threat modeling, risk assessment,
resources, metrics, and case studies,” IEEE Access, vol. 9, pp. 29 775–
29 818, 2021.
[2] D. He, S. Chan, Y. Zhang, C. Wu, and B. Wang, “How effective are
the prevailing attack-defense models for cybersecurity anyway?” IEEE
Intelligent Systems, Sept 2014.
[3] I. Zografopoulos, C. Konstantinou, and N. D. Hatziargyriou, “Distributed
energy resources cybersecurity outlook: Vulnerabilities, attacks, impacts,
and mitigations,” arXiv preprint arXiv:2205.11171, 2022.
[4] N. Jacobs, S. Hossain-McKenzie, and E. Vugrin, “Measurement and
analysis of cyber resilience for control systems: An illustrative example,”
in 2018 Resilience Week (RWS).
IEEE, 2018, pp. 38–46.
[5] A. Keliris, C. Konstantinou, M. Sazos, and M. Maniatakos, “Open source
intelligence for energy sector cyberattacks,” in Critical Infrastructure
Security and Resilience.
Springer, 2019, pp. 261–281.
[6] X. Liu, A. Keliris, C. Konstantinou, M. Sazos, and M. Maniatakos, “As-
sessment of low-budget targeted cyberattacks against power systems,” in
IFIP/IEEE International Conference on Very Large Scale Integration-
System on a Chip.
Springer, 2018, pp. 232–256.
[7] A. Lee, “Creating security metrics for the electric sector,” EPRI Product
ID: 3002005947, 2015.
[8] M.
Schiffman,
“Common
vulnerability
scoring
system
(CVSS),”
http://www. ﬁrst. org/cvss/cvss-guide.html, 2011.
[9] R. A. Caralli, J. H. Allen, and D. W. White, CERT resilience man-
agement model: A maturity model for managing operational resilience.
Addison-Wesley Professional, 2010.
[10] D. e. a. Bodeau, “Cyber resiliency engineering framework (CREF),”
https://www.mitre.org/publications/technical-papers/cyber-resiliency-
engineering-framework, 2012.
[11] P. Bajpai, S. Chanda, and A. K. Srivastava, “A novel metric to quantify
and enable resilient distribution system using graph theory and choquet
integral,” IEEE Transactions on Smart Grid, vol. 9, no. 4, pp. 2918–
2929, 2018.
[12] C. Vellaithurai, A. Srivastava, S. Zonouz, and R. Berthier, “CPIndex:
Cyber-physical vulnerability assessment for power-grid infrastructures,”
IEEE Transactions on Smart Grid, vol. 6, no. 2, pp. 566–575, 2015.
[13] V. Venkataramanan, A. Hahn, and A. Srivastava, “CyPhyR: A cyber-
physical analysis tool for measuring and enabling resiliency in micro-
grids,” IET Cyber-Physical Systems: Theory & Applications, vol. 4,
no. 4, pp. 313–321, 2019.
[14] V. Venkataramanan, A. Hahn, and A. Srivastava, “CP-SAM: Cyber-
physical security assessment metric for monitoring microgrid resiliency,”
IEEE Transactions on Smart Grid, vol. 11, no. 2, pp. 1055–1065, 2020.
[15] G. Huang, J. Wang, C. Chen, and C. Guo, “Cyber-constrained optimal
power ﬂow model for smart grid resilience enhancement,” IEEE Trans-
actions on Smart Grid, vol. 10, no. 5, pp. 5547–5555, 2019.
[16] J. Valinejad and L. Mili, “Community resilience optimization subject
to power ﬂow constraints in cyber-physical-social systems in power
engineering,” arXiv preprint arXiv:2004.00772, 2020.
[17] A. Lee, “Creating Security Metrics for the Electric Sector,” EPRI
Product ID: 3002005947, 2015.
[18] C. Suh-Lee, “EPRI Cyber Security Metrics Operationalization and
Benchmarking Pilot,” EPRI Product ID: 3002016796, 2020.
[19] A. J. Wood, B. F. Wollenberg, and G. B. Shebl´e, Power generation,
operation, and control.
John Wiley & Sons, 2013.
[20] V. Balamourougan, T. Sidhu, and M. Sachdev, “Technique for online
prediction of voltage collapse,” IEE Proceedings-Generation, Transmis-
sion and Distribution, vol. 151, no. 4, pp. 453–460, 2004.
[21] S. P´erez-Londo˜no, L. Rodr´ıguez, and G. Olivar, “A simpliﬁed voltage
stability index (SVSI),” International Journal of Electrical Power &
Energy Systems, vol. 63, pp. 806–813, 2014.
[22] G. Yesuratnam and D. Thukaram, “Congestion management in open
access based on relative electrical distances using voltage stability
criteria,” Electric power systems research, vol. 77, no. 12, pp. 1608–
1618, 2007.
[23] I. Dassios, P. Cuffe, and A. Keane, “On the unity row summation and
real valued nature of the FLG matrix,” arXiv preprint arXiv:1503.08652,
2015.
[24] “NetworkX:
Network
analysis
in
Python
-
Betweenness
Centrality,”
2020,
Accessed:
Jan.
26,
2021.
[Online].
Available:
https://networkx.org/documentation/stable/reference/
algorithms/generated/networkx.algorithms.centrality.betweenness
centrality.html#networkx.algorithms.centrality.betweenness centrality
[25] “NetworkX: Network analysis in Python - Closeness Centrality,”
2020,
Accessed:
Jan.
26,
2021.
[Online].
Available:
https://networkx.org/documentation/stable/reference/algorithms/
generated/networkx.algorithms.centrality.closeness centrality.html#
networkx.algorithms.centrality.closeness centrality
[26] M. U. Aksu, M. H. Dilek, E. ˙I. Tatlı, K. Bicakci, H. I. Dirik, M. U.
Demirezen, and T. Aykır, “A quantitative CVSS-based cyber security
risk assessment methodology for IT systems,” in 2017 International
Carnahan Conference on Security Technology (ICCST).
IEEE, 2017,
pp. 1–8.
[27] “Common Vulnerability Scoring System version 3.1, Speciﬁcation
Document, Revision 1,” 2020, Accessed: Jan. 26, 2021. [Online].
Available: https://www.ﬁrst.org/cvss/v3-1/cvss-v31-speciﬁcation r1.pdf
[28] X. Liu, J. Ospina, and C. Konstantinou, “Deep reinforcement learning
for cybersecurity assessment of wind integrated power systems,” IEEE
Access, vol. 8, pp. 208 378–208 394, 2020.
[29] H. Q. Vu, G. Beliakov, and G. Li, “A choquet integral toolbox and its
application in customer preference analysis,” Data Mining Applications
with R, 2014.
[30] P. Meyer and M. Roubens, “On the use of the choquet integral with
fuzzy numbers in multiple criteria decision support,” Fuzzy Sets and
Systems, vol. 157, no. 7, pp. 927–938, 2006.
[31] H. Wang, C. E. Murillo-Sanchez, R. D. Zimmerman, and R. J. Thomas,
“On computational issues of market-based optimal power ﬂow,” IEEE
Transactions on Power Systems, vol. 22, no. 3, pp. 1185–1193, 2007.
[32] H. Wang, “On the computation and application of multi-period security-
constrained optimal power ﬂow for real-time electricity market opera-
tions,” Cornell University, 2007.
[33] Yong Fu, M. Shahidehpour, and Zuyi Li, “AC contingency dispatch
based on security-constrained unit commitment,” IEEE Transactions on
Power Systems, vol. 21, no. 2, pp. 897–908, 2006.
[34] A. Venzke and S. Chatzivasileiadis, “Convex relaxations of probabilistic
AC optimal power ﬂow for interconnected AC and HVDC grids,” IEEE
Transactions on Power Systems, vol. 34, no. 4, pp. 2706–2718, 2019.
[35] J. Ospina, V. Venkataramanan, and C. Konstantinou, “Quantitative
Cyber-Metric Repository,” 2021, Accessed: Sept. 28, 2021. [Online].
Available: https://gitlab.com/juanjospina/quantitative-cyber-metric
[36] Probability Methods Subcommittee, “IEEE reliability test system,” IEEE
Transactions on power apparatus and systems, no. 6, pp. 2047–2054,
1979.
[37] R. D. Zimmerman, C. E. Murillo-S´anchez, and R. J. Thomas, “MAT-
POWER: Steady-state operations, planning, and analysis tools for power
systems research and education,” IEEE Transactions on Power Systems,
vol. 26, no. 1, pp. 12–19, 2011.
[38] “PandaPower v.2.5.0,” 2020, Accessed: Jan. 28, 2021. [Online].
Available: https://pandapower.readthedocs.io/en/v2.5.0/about.html
[39] C. Xenofontos, I. Zografopoulos, C. Konstantinou, A. Jolfaei, M. K.
Khan, and K.-K. R. Choo, “Consumer, commercial, and industrial iot
(in)security: Attack taxonomy and case studies,” IEEE Internet of Things
Journal, vol. 9, no. 1, pp. 199–221, 2022.
[40] F. Milano, L. Vanfretti, and J. C. Morataya, “An open source power
system virtual laboratory: The PSAT case and experience,” IEEE Trans-
actions on Education, vol. 51, no. 1, pp. 17–23, 2008.
LA-UR-21-32027
