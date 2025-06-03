

---

Page 1

---

HAL Id: tel-02511243
https://theses.hal.science/tel-02511243v1
Submitted on 18 Mar 2020
HAL is a multi-disciplinary open access
archive for the deposit and dissemination of sci-
entific research documents, whether they are pub-
lished or not.
The documents may come from
teaching and research institutions in France or
abroad, or from public or private research centers.
L’archive ouverte pluridisciplinaire HAL, est
destinée au dépôt et à la diffusion de documents
scientifiques de niveau recherche, publiés ou non,
émanant des établissements d’enseignement et de
recherche français ou étrangers, des laboratoires
publics ou privés.
Modeling and Coordination of interconnected microgrids
using distributed artificial intelligence approaches
Jin Wei
To cite this version:
Jin Wei. Modeling and Coordination of interconnected microgrids using distributed artificial intelli-
gence approaches. Artificial Intelligence [cs.AI]. Université Bourgogne Franche-Comté, 2019. English.
￿NNT : 2019UBFCA021￿. ￿tel-02511243￿


---

Page 2

---

TH `ESE DE DOCTORAT DE L’ ´ETABLISSEMENT UNIVERSIT ´E BOURGOGNE FRANCHE-COMT ´E
PR ´EPAR ´EE `A L’UNIVERSIT ´E DE TECHNOLOGIE DE BELFORT-MONTB ´ELIARD
´Ecole doctorale n°37
Sciences Pour l’Ing´enieur et Microtechniques
Doctorat d’Informatique
par
JIN WEI
Coordination in Microgrid Networks Using Multi-agent Systems
Th`ese pr´esent´ee et soutenue `a Belfort, le 12 December 2019
Composition du Jury :
WIRA PATRICE
Professeur `a l’Universit´e de Haute
Alsace
Rapporteur
FONLUPT CYRIL
Professeur `a l’Universit´e du Littoral
Rapporteur
IDOUMGHAR LHASSANE
Professeur `a l’Universit´e de Haute
Alsace
Pr´esident du jury
GOUTON PIERRE
Professeur
`a
l’Universit´e
de
Bourgogne
Examinateur
TU XIAOWEI
Professeur `a l’Universit´e de Shanghai
Examinateur
KOUKAM ABDERRAFIAA
Professeur
`a
l’Universit´e
de
Technologie de Belfort Montb´eliard
Directeur de th`ese
ROCHE ROBIN
maˆıtre de conf´erences `a l’Universit´e
de Technologie de Belfort Montb´eliard
Codirecteur de th`ese
N◦
2
0
1
9
U
B
F
C
A
0
2
1


---

Page 3

---



---

Page 4

---

école doctorale sciences pour l’ingénieur et microtechniques
Universit´e Bourgogne Franche-Comt´e
32, avenue de l’Observatoire
25000 Besanon, France


---

Page 5

---



---

Page 6

---

ABSTRACT
As renewable sources penetrate the current electrical system to relief global warming and
energy shortage, microgrid (MG) emerges to reduce the impact of intermittent generation
on the utility grid. Additionally, it improves the automation and intelligence of the power
grid with plug-and-play characteristics. Inserting more MGs into a distribution network
promotes the development of the smart grid. Thus MG networks existing in the power
system are in prospect. Coordinating them could gain a system with high reliability, low
cost, and strong resistance to electrical faults. Achieving these proﬁts relies on developed
technologies of communication, control strategy, and corresponding algorithms.
Dispatching power in distributed MGs while coordinating elements within the individual
MG demands a decentralized control system, in which the multi-agent system possesses
advantages. It is applied to the MG network for establishing a physically and electri-
cally distributed system. Based on the multi-agent system, this thesis mainly studies the
coordination control in the MG network and its modeling. It aims at promoting control
performance in terms of efﬁciency, reliability, economic beneﬁt and scalability. According
to the holonic structure, two methods are considered to enable the system scalability,
including the coordination with neighboring MGs and within the extensive coordinating
area. Then a simulation platform is established to validate the proposed approaches with
Python language.
The control strategies for coordination between MGs and their neighbors are proposed to
maintain the complete load supply and global security operation while minimizing the gen-
eration cost. Centralized control in the coordination group is applied for economic energy
management. It uses a Newton-Raphson method to dispatch power among neighboring
MGs by simplifying the relationship between MG generation cost and its output power into
a quadratic function. An average consensus theorem is adopted to calculate the caused
network power ﬂow, and the results are compared with the maximal capacity on the line
to keep safe operation. To improve the economic beneﬁts, the approximated relationship
between MG output power and the caused generation cost is improved in another strat-
egy. It builds a market for neighboring power trade. Here, the bid is derived from the
average generation cost on maximal output. This method maintains the operation privacy
of individual MG. Power ﬂow calculation is simpliﬁed to be proportional to the angle differ-
ence between the two terminates of the connecting line. Both strategies are tested on a
13-node, and 34-node network. Their performance shows that both approaches possess
scalability and could economically compensate for the lack of load supply in faulted MG.
For the control strategy with higher reliability and proﬁt, the coordination strategy within
a selected extensive area of MGs is proposed. Expanding the coordination area based
on neighboring MGs provides more energy sources to the demanded MG. It ensures
enough power to compensate imbalance and offers more choices for power dispatch-
ing. The selection of the coordination area adopts the distributed evolutionary algorithm
programming to the multi-agent system to accelerate the calculation speed. Quadratic
programming in Gurobi is used to solve the power dispatching problem. Another ge-
v


---

Page 7

---

vi
netic algorithm is also adopted to solve the problem of optimal power dispatching with
a quadratic generation cost for microturbine. The performance of this strategy is tested,
and the results show that it has comprehensive advantages on reliability, scalability, and
proﬁt compared with centralized and market methods.


---

Page 8

---

R´ESUM´E
`A mesure que les sources renouvelables s’int`egrent dans le syst`eme ´electrique actuel
pour att´enuer le r´echauffement plan´etaire et la p´enurie d’´energie fossile, les micro-
r´eseaux (MG) ´emergent comme une solution permettant de r´eduire l’impact de la pro-
duction intermittente sur les r´eseaux publics.
En outre, ils permettent d’am´eliorer
l’automatisation et l’intelligence des r´eseaux avec des caract´eristiques plug-and-play.
L’int´egration d’un plus grand nombre de MG dans un r´eseau de distribution permettrait
d’arriver `a un syst`eme avec une grande ﬁabilit´e, un faible coˆut, et une forte r´esilience aux
pannes. La r´ealisation de ces objectifs repose sur des technologies de communication,
des strat´egies de contrˆole et plusieurs types d’algorithmes.
La r´epartition de la puissance entre MG et la coordination des ´el´ements au sein de
chaque MG exige un syst`eme de contrˆole d´ecentralis´e, pour lequel un syst`eme multi-
agents pr´esentent des avantages. Il est utilis´e pour ´etablir un syst`eme distribu´e physique-
ment et du point de vue de la prise de d´ecision. Bas´ee sur cette approche, cette th`ese
´etudie principalement le contrˆole et la coordination d’un r´eseau de MG. Il vise `a permet-
tre une meilleure performance de contrˆole en termes d’efﬁcacit´e, de ﬁabilit´e, d’avantages
´economiques et d’´evolutivit´e.
Grˆace `a une structure holonique, deux m´ethodes sont
´etudi´ees pour permettre l’´evolutivit´e du syst`eme. Une plateforme de simulation est ´etablie
pour valider les approches propos´ees avec le langage Python.
Dans une premi`ere approche, une strat´egie de contrˆole pour la coordination entre
plusieurs MG voisins est propos´ee. Elle permet de maintenir la charge compl`ete et la
ﬁabilit´e de fonctionnement tout en minimisant le coˆut de production. Le contrˆole cen-
tralis´e dans le groupe de coordination est utilis´e pour r´ealiser le dispatching entre MG
et leurs composants. La m´ethode de Newton-Raphson permet de r´epartir la puissance
entre les MG voisins en simpliﬁant la relation entre le coˆut de production des MG et leur
puissance de sortie par une fonction quadratique. Un th´eor`eme de consensus moyen est
adopt´e pour calculer le ﬂux de puissance qui en r´esultent sur les diff´erentes lignes, et les
r´esultats sont compar´es avec la capacit´e maximale de chaque ligne pour assurer un fonc-
tionnement sˆur. Pour am´eliorer encore les avantages ´economiques, l’approximation de la
relation entre la puissance de production des MG et le coˆut de production est am´elior´ee
dans une autre strat´egie. Elle repose sur un march´e de l’´electricit´e entre MG voisins. Ici,
les offres sont d´eriv´ees du coˆut moyen de production sur la production maximale. Cette
m´ethode pr´eserve la conﬁdentialit´e des informations de chaque MG. Le calcul du ﬂux
de puissance est simpliﬁ´e pour ˆetre proportionnel `a la diff´erence d’angle entre les deux
extr´emit´es de la ligne de raccordement. Les deux strat´egies sont test´ees sur des r´eseaux
de 13 et 34 noeuds. Les r´esultats montrent que les deux approches sont fonctionnelles et
pourraient ´economiquement compenser le manque d’approvisionnement en charge dans
des MG d´efectueux.
Dans une seconde approche, pour encore am´eliorer la ﬁabilit´e et les proﬁts, une strat´egie
de coordination au sein d’une vaste zone int´egrant de multiples MG est propos´ee.
L’´elargissement de la zone de coordination fournit plus de moyens de r´epondre aux be-
vii


---

Page 9

---

viii
soins et annuler le d´es´equilibre en puissance r´esultant d’un d´efaut. La d´etermination de
la zone de coordination repose sur un algorithme ´evolutionnaire distribu´e s’appuyant sur
syst`eme multi-agent pour acc´el´erer la vitesse de calcul. La programmation quadratique
dans Gurobi est ensuite utilis´ee pour r´esoudre le probl`eme de r´epartition de puissance.
Un autre algorithme g´en´etique est ´egalement mis en oeuvre pour r´esoudre le probl`eme
de la r´epartition optimale de la puissance avec un coˆut de production quadratique pour
la microturbine. La performance de cette strat´egie est test´ee, et les r´esultats montrent
qu’elle pr´esente des avantages sur la ﬁabilit´e, l’´evolutivit´e et le proﬁt par rapport aux
m´ethodes centralis´ees et de march´e.


---

Page 10

---

ACKNOWLEDGEMENTS
I want to express my heartfelt gratitude to all those who have been helping me during the
writing of this thesis.
My deepest gratitude goes ﬁrst and foremost to Professor Abderraﬁaa Koukam and Dr.
Robin Roche, my supervisors, for their constant encouragement and guidance. They
have walked me through all the stages of the writing of this thesis. Without their consistent
and illuminating instruction, this thesis could not have reached its present form. I also
thank Mr. Fabrice Lauri very much for his kind guiding on computer science.
Secondly, I would like to thank professor Patrice Wira and professor Cyril Fonlupt for
accepting to review this thesis and for their valuable comments, despite their very busy
schedules. I would also like to thank professor Lhassane Idoumghar, professor Pierre
Gouton and professor Xiaowei Tu for accepting to participate in my dissertation commit-
tee.
Thirdly, I would like to express my gratitude to the professors and teachers at the Depart-
ment of CIAD, who have instructed and helped me a lot in the past four years.
My thanks would also go to the China Scholarship Council (CSC), which provides the
scholarship to me for ﬁnishing this thesis without worrying about expense in life.
Finally, I am extremely grateful to my beloved ﬁance, Xin Su. In a country far away from
my motherland, his support helps me to overcome difﬁculties in life and work. Last but not
the least, I would like to thank my parents and brother for their thoughtful consideration
and great conﬁdence in me all through these years. I also owe my sincere gratitude to my
friends and my fellow colleagues. They listen to me and ﬁgure out my problems during
the difﬁcult course of the thesis.
ix


---

Page 11

---



---

Page 12

---

CONTENTS
I
Context and Objectives
5
1
Introduction
7
1.1
Context
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
1.1.1
Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
1.1.2
Microgrid Deﬁnition
. . . . . . . . . . . . . . . . . . . . . . . . . . .
10
1.1.3
Microgrid Network . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
1.1.4
Muti-agent System . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
1.2
Objectives and concerns of this thesis . . . . . . . . . . . . . . . . . . . . .
17
1.2.1
Problem Statement . . . . . . . . . . . . . . . . . . . . . . . . . . . .
17
1.2.2
Coordination with neighboring MGs
. . . . . . . . . . . . . . . . . .
18
1.2.3
Coordination within extensive MG group . . . . . . . . . . . . . . . .
19
1.2.4
Simulation studies . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
1.3
Outline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20
2
Related Works
23
2.1
Coordination with Reconﬁguring and Maintaining Microgrid
. . . . . . . . .
23
2.1.1
Reconﬁguring Microgrid . . . . . . . . . . . . . . . . . . . . . . . . .
24
2.1.2
Maintaining Microgrid
. . . . . . . . . . . . . . . . . . . . . . . . . .
25
2.2
Coordination with Centralized and Decentralized control . . . . . . . . . . .
27
2.2.1
Centralized Control . . . . . . . . . . . . . . . . . . . . . . . . . . . .
27
2.2.2
Decentralized Control . . . . . . . . . . . . . . . . . . . . . . . . . .
28
2.2.3
Multi-agent System Control . . . . . . . . . . . . . . . . . . . . . . .
29
2.3
Conclusion
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
30
II
Contributions
33
3
Modeling And Simulation Platform
35
3.1
Development of Simulation Platform . . . . . . . . . . . . . . . . . . . . . .
35
3.2
Modeling of MG Network
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
35
xi


---

Page 13

---

xii
CONTENTS
3.2.1
MG Network as Complex System . . . . . . . . . . . . . . . . . . . .
35
3.2.2
Multi-agent System . . . . . . . . . . . . . . . . . . . . . . . . . . . .
37
3.2.2.1
Environment . . . . . . . . . . . . . . . . . . . . . . . . . .
37
3.2.2.2
The Agent
. . . . . . . . . . . . . . . . . . . . . . . . . . .
38
3.2.3
The MG Network Modeling Based on Multi-agent System . . . . . .
39
3.2.3.1
Distributed architecture . . . . . . . . . . . . . . . . . . . .
39
3.2.3.2
Reactivity . . . . . . . . . . . . . . . . . . . . . . . . . . . .
40
3.2.3.3
Pro-activeness . . . . . . . . . . . . . . . . . . . . . . . . .
41
3.2.3.4
Social Ability . . . . . . . . . . . . . . . . . . . . . . . . . .
41
3.2.3.5
Modeling of the MG network . . . . . . . . . . . . . . . . .
42
3.2.4
Multi-agent System Controlling the MG Network
. . . . . . . . . . .
44
3.2.4.1
Topology . . . . . . . . . . . . . . . . . . . . . . . . . . . .
44
3.2.4.2
Control Methods and Algorithms . . . . . . . . . . . . . . .
46
3.3
Platform Implementation with Python . . . . . . . . . . . . . . . . . . . . . .
47
3.3.1
Modeling of the Electrical System
. . . . . . . . . . . . . . . . . . .
47
3.3.2
Simulation Platform
. . . . . . . . . . . . . . . . . . . . . . . . . . .
50
3.3.2.1
Simulation Interface . . . . . . . . . . . . . . . . . . . . . .
50
3.3.2.2
Simulation Object . . . . . . . . . . . . . . . . . . . . . . .
53
4
Multi-agent Based Coordination with Neighboring Microgrid
57
4.1
Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
57
4.2
Coordination Problem
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
57
4.3
Elements Model within MG
. . . . . . . . . . . . . . . . . . . . . . . . . . .
58
4.3.1
Renewable generators . . . . . . . . . . . . . . . . . . . . . . . . . .
58
4.3.1.1
Photovoltaic Generators . . . . . . . . . . . . . . . . . . . .
59
4.3.1.2
Wind Turbine . . . . . . . . . . . . . . . . . . . . . . . . . .
59
4.3.2
Microturbine
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
60
4.3.3
Energy Storage System . . . . . . . . . . . . . . . . . . . . . . . . .
61
4.4
Microgrid Network Coordination System . . . . . . . . . . . . . . . . . . . .
62
4.4.1
Physical Connection among MGs . . . . . . . . . . . . . . . . . . . .
62
4.4.2
Communication Network in MAS . . . . . . . . . . . . . . . . . . . .
62
4.5
Control Strategy within Individual Microgrid
. . . . . . . . . . . . . . . . . .
63
4.5.1
Under Normal Condition . . . . . . . . . . . . . . . . . . . . . . . . .
64
4.5.1.1
Objective and Problem Formulation . . . . . . . . . . . . .
64
4.5.1.2
Control Process . . . . . . . . . . . . . . . . . . . . . . . .
64


---

Page 14

---

CONTENTS
xiii
4.5.2
Under Fault Condition . . . . . . . . . . . . . . . . . . . . . . . . . .
65
4.5.2.1
Objective and Problem Formulation . . . . . . . . . . . . .
65
4.5.2.2
Control Process . . . . . . . . . . . . . . . . . . . . . . . .
66
4.6
Control Strategy for MG Coordination
. . . . . . . . . . . . . . . . . . . . .
67
4.6.1
Strategy 1: Centralized Optimal Dispatching in Partial Area . . . . .
67
4.6.1.1
Motivation
. . . . . . . . . . . . . . . . . . . . . . . . . . .
67
4.6.1.2
Problem Formulation
. . . . . . . . . . . . . . . . . . . . .
67
4.6.1.3
Control Strategy . . . . . . . . . . . . . . . . . . . . . . . .
68
4.6.1.4
Power Flow Algorithm . . . . . . . . . . . . . . . . . . . . .
70
4.6.2
Strategy 2: Bidding in the market . . . . . . . . . . . . . . . . . . . .
73
4.6.2.1
Motivation
. . . . . . . . . . . . . . . . . . . . . . . . . . .
73
4.6.2.2
Problem Formulation
. . . . . . . . . . . . . . . . . . . . .
74
4.6.2.3
Control Strategy . . . . . . . . . . . . . . . . . . . . . . . .
76
4.6.2.4
Power Flow . . . . . . . . . . . . . . . . . . . . . . . . . . .
77
4.7
Simulation Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
79
4.7.1
Test Multi-agent System and Microgrid Network . . . . . . . . . . . .
79
4.7.2
Dispatching Algorithm Comparisons . . . . . . . . . . . . . . . . . .
81
4.7.3
Generation Cost Comparison . . . . . . . . . . . . . . . . . . . . . .
82
4.7.4
Robustness Test . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
82
4.8
Conclusion
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
83
5
Multi-agent based coordination within selected microgrid area
89
5.1
Demand-supply Balance for the Economic Power Dispatching in Network
.
89
5.2
Holonic MAS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
90
5.3
Control Strategy Process of Proposed Strategy . . . . . . . . . . . . . . . .
91
5.3.1
Coordination Process
. . . . . . . . . . . . . . . . . . . . . . . . . .
91
5.3.2
Coordinating Microgrid Selection . . . . . . . . . . . . . . . . . . . .
94
5.3.3
Power Dispatching . . . . . . . . . . . . . . . . . . . . . . . . . . . .
95
5.3.4
Distributed Evolutionary Algorithms with Depth-ﬁrst Search (DFS)
.
96
5.4
Simulation Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
97
5.4.1
Case 1
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
99
5.4.2
Case 2
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
5.4.3
Case 3
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
5.4.4
Impact on Calculation Time and Cost
. . . . . . . . . . . . . . . . . 108
5.5
Conclusion
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109


---

Page 15

---

xiv
CONTENTS
III
Conclusion
111
6
Conclusions
113
6.1
Conclusions on the Proposed Approach . . . . . . . . . . . . . . . . . . . . 113
6.2
Future Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
6.3
Scientiﬁc Production Review
. . . . . . . . . . . . . . . . . . . . . . . . . . 114


---

Page 16

---

NOMENCLATURE
Acronyms
AIMMS advanced integrated multidimensional modeling software
CA
coordination area
CS
centralized strategy
DER
distributed energy resource
DFS
depth-ﬁrst search
DG
distributed generator
GA
genetic algorithm
GAMS general algebraic modeling system
GAUF geometric average utility function
KCL
Kirchhoff’s current law
KVL
Kirchhoff’s voltage law
MAS
multi-agent system
MG
microgrid
MGEMS microgrid energy management system
MILP mixed integer linear problem
MINLP mixed integer non-linear problem
MK
market
MT
micro turbine
NLP
non-linear problem
PF
power ﬂow
PV
photovolataic generator
QP
quadratic programming
S OC
status of charge
WT
wind turbine
1


---

Page 17

---

2
CONTENTS
Indices
i
index for neighboring microgrid
j
index for neighboring microgrid
k
index for microgrid
t
index for time
Sets
∆t
time interval for each time step
∆pMG power error between actual and iterative MG output power
η j
1
MG cost coefﬁcients for linear items
η j
2
MG cost coefﬁcients for quadratic items
ηk
b
proﬁt gain of buyer indexed k
ηk
s
proﬁt gain of seller indexed k
µcoordination
cos t
faulted MG cost on buying enough power from neighbors
µ j i
cos t
the quantity that the faulted MG paying to the neighbor MG indexed of j
µk
max
generation cost under maximal volume of generation in k-index MG
µk
min
generation cost under maximal volume of load in k-index MG
µi
Bat,max generation cost of battery under MG maximal generation.
µi
MT,max generation cost of MT under MG maximal generation
θ
angle of the MG voltage
bi j
Line
susceptance of distribution lines between MGs of i-index and j-index
gi j
Line
reactance of distribution lines between MGs of i-index and j-index
i, j, k
MG index
pi
max,cap the power ﬂexibility of i-index MG, upper limit
pk
max,in maximal volume of input power in k-index MG
pk
max,out maximal volume of output power in k-index MG
pi
min,cap the power ﬂexibility of i-index MG, lower limit
pi
L,equ
equivalent load of line loss for i-index MG
pi j
Line,cap transmission line’s capacity
pi j
Line,loss power loss on lines connecting i-index MG and j-index MG


---

Page 18

---

CONTENTS
3
pi j
Line
power ﬂow on the distribution line connecting j-index and i-index MG
pi
MG, mod equivalent power inputting into i-index MG considering the line loss
pi
MG
power of i -index MG interacting with network
p j i
MG
power volume sold from i-index MG to j-index MG
ri j
Line
transmission line’s resistance
st
MT
the operating status in the time steps of t
T
collection of all the MGs in network
V
amplitude of the MG voltage
W
velocity of wind
wt
ess
battery SOC at time step of t
xi j
Line
impedance of line connecting i-index MG and j-index MG
δi
voltage angle of i-index MG
η1,MT
the cost coefﬁcients of generation corresponding to the linear term
η2,MT
cost coefﬁcients of generation corresponding to the quadratic term
ηch,Bat battery efﬁciency of charging
ηdisch,Bat battery efﬁciency of discharging
ηPV
derating factor considering conversion efﬁciency of PV cells
ηup down,MT cost over each change of MT operation status
ηWT
derating factor considering conversion efﬁciency of WT
µcost
generation cost of MG
µinput,net price of power buying from the network
µMT
total cost generating certain volume of power
µoutput,net price of power selling to the network
πk
bid price of assistant k-index MG
ρ
air densitys
Iirr
density of solar irradiation
pL
value of operating load
pmax,L value of the total load
pmax ch arg e,Bat maximal charging power
pmax disch arg e,Bat maximal discharging power


---

Page 19

---

4
CONTENTS
pcommand,Bat power command for battery
pcommand,MT the command of MG internal control to maintain power balance
pdisch,Bat, pch,Bat battery discharging/charging power
pmax,MT maximal output of MT
pmax,PV the maximal generation of PV
pmax,WT the maximal generation of WT
pmin,MT minimal output of MT
pout,Bat battery output
pout,MT generation of micro turbine
pout,PV output power of PV
pout,WT output power of WT
preq
demanding power of faulted MG
pres
supportive power from assistive MGs
RPV
irradiated area of PV cells
RWT
rotor disk area
TL
collection of load within individual MG
TBat
collection of battery within individual MG
TMT
collection of micro turbine within individual MG


---

Page 20

---

I
CONTEXT AND OBJECTIVES
5


---

Page 21

---



---

Page 22

---

1
INTRODUCTION
1.1/
CONTEXT
1.1.1/
BACKGROUND
The prosperity of the current industry and technology brings abundant life and convenient
tools to human society. However, the increasing consumption of resources and uncon-
scious waste both worsen the earth’s environment. As Charles John Huffam Dickens
said in the book of [Dickens, 2000], ”this is the worst of times, but also the best time,” the
exploration on energy stimulates creative thoughts and breeds new development under
the context in the following:
1) Global warming: due to the increasing carbon emission caused by the use of fossil
fuel, the global warming problem becomes obvious and starts to inﬂuence human
life. From the report of NASA, the global land-ocean annual temperature tends
to increase since 1974, and until 2016 the annual increment has got to 0.96oC
[Aeronautics et al., 2019]. Figure 1.1 from GISS depicts this deterioration, which
attracts human beings’ attention.
Figure 1.1: Annual mean temperature change for land and ocean. Measured in degree.
7


---

Page 23

---

8
CHAPTER 1. INTRODUCTION
2) Increase in renewable sources: renewable sources are famous for renewable origi-
nal energy such as photovoltaic and nuclear generation. This environmental friendly
and economical generation penetrates the current electrical power system and
sharply increases worldwide. For example, it took a percentage of 16.3% until 2017
in French electricity consumption. The condition is published by the European En-
vironmental Agency, which is shown in ﬁgure
1.2 [(EEA), 2019].
However, the
generation pulse worsens the power quality and its intermittency also distorts the
load prediction in the utility grid. The distributed generation also brings challenges
to fault detection.
Figure 1.2: Share of renewable energy in gross ﬁnal energy consumption in France.
3) Energy shortage: current human activities rely on fossil fuel more than any other
time in history. Over-exploitation and large-scale consumption are exposing human
beings under the thread of energy exhaustion.
Currently, the danger of energy
shortage compels people to exploit new energy sources. According to the ﬁgure
1.3 posted in reference [Smil, 2016], the global fossil fuel consumption peaks at
133853.38 TWh in the year of 2017 and the biggest reservation of coal can only
last for 114 years under such a speed [Dudley et al., 2015].
4) Electricity demand of the remote area: for a particular purpose, some electricity
customers are located in a remote area such as a secret military base, island res-
idents, and offshore drilling platform. It is technically difﬁcult and costly to supply
such customers by building a transmission system from the primary grid. The visi-
ble connection is especially challenging to keep privacy for military usage. Thus an


---

Page 24

---

1.1. CONTEXT
9
1800
1850
1900
1950
2000 2017
0 TWh
20,000 TWh
40,000 TWh
60,000 TWh
80,000 TWh
100,000 TWh
120,000 TWh
Figure 1.3: Global fossil fuel consumption. Global primary energy consumption by fossil
fuel source, measured in terawatt-hours (TWh).
electrically and geographically independent generator-customer system is highly
demanded.
5) Security operation: the expansion of power systems brings issues in faults detection
and recovery. Network interconnection promotes coupling between MGs, which
expands the impacts of faults. For example, even a tiny error could cause system
collapse. For the utility grid, establishing enough devices to detect and isolate faults
is not realistic, given the large scale and corresponding cost. Since 1985, when
the ﬁrst AC system was built, the grid infrastructures have lasted for decades. The
aging problems are currently threatening the secure operation [Guarnieri, 2013].
Particularly, aging devices, such as transmission lines, threaten the reliability and
efﬁciency of current emergency solutions.
6) Developing technologies in artiﬁcial intelligence and electronics: artiﬁcial intelli-
gence has participated in every aspect of human activities. Its industrial use high-
lights by automation and complexity analysis. The development of electronics pro-
vides a fast and accurate way to control the high-power system. The combination
of both technologies develops the capability of self-control and determination in the
power system. Their application in the power grid stimulates creative approaches
to optimize the facility operation.
7) Smart grid development: with the insertion of digital technology, the current grid is
becoming smarter on operation prediction and power dispatching based on the sup-
port of communication networks and sensors. It enables the scheduling concept to
transform from traditional peer-to-company to current peer-to-peer. The operation of
dispatchable generators and distributable loads leads to the issues of optimization
on economics, environment, communication, and so on.


---

Page 25

---

10
CHAPTER 1. INTRODUCTION
1.1.2/
MICROGRID DEFINITION
Under the increasing demand for electrical power and the rising deterioration of the en-
vironment in the current world, new types of resources are continuously invented and
integrated into power systems. Cooperating generators of different characteristics chal-
lenge the automatic and intelligent capability of the electrical system. Microgrid (MG)
emerges as an effective method by narrowing the controlling system and coordinating
the selected types of equipment. Such an architecture shares the control pressure of the
main grid. Additionally, it promotes the intelligence and automation of the MG. Due to the
growing interests in MG, the agreement on its deﬁnition is necessary. The U.S. Depart-
ment of Energy Microgrid Exchange Group simply deﬁned the MG in the year of 2012 as
follows, and an example is shown in ﬁgure 1.4 [Ton et al., 2012]:
A microgrid is a group of interconnected loads and distributed energy re-
sources within clearly deﬁned electrical boundaries that acts as a single con-
trollable entity with respect to the grid. A microgrid can connect and discon-
nect from the grid to enable it to operate in both grid-connected or island
mode.
Photovoltaic 
generator
Battery
Micro turbine
Load
Wind turbine
Utility grid
Figure 1.4: An example of MG.
This deﬁnition focuses on the isolating operation, and it puts a loose limitation on con-
stituent elements. While another one proposed by CIGR ´E C6.22 Working Group gives a
detailed description of the MG in 2015 [Marnay et al., 2015]:
Microgrids are electricity distribution systems containing loads and distributed
energy resources, (such as distributed generators (DGs), storage devices, or
controllable loads) that can be operated in a controlled, coordinated way either
while connected to the main power network or while islanded.


---

Page 26

---

1.1. CONTEXT
11
This deﬁnition comes along with the qualiﬁers of MG elements:
Generators cover all sources possible at the scales and within the context of a
microgrid, e.g., fossil or biomass-ﬁred small-scale combined heat and power
(CHP), photovoltaic modules (PV), small wind turbines, mini-hydro, etc.
Storage Devices include all of electrical, pressure, gravitational, ﬂywheel, and
heat storage technologies. While the microgrid concept focuses on a power
system, heat storage can be relevant to its operation whenever its existence
affects the operation of the microgrid. For example, the availability of heat
storage will alter the desirable operating schedule of a CHP system as the
electrical and heat loads are decoupled. Similarly, the pre-cooling or heating
of buildings will change the load shape of heating ventilation and air condition-
ing (HVAC) system, and therefore the requirement faced by electricity supply
resources.
Controlled loads, such as automatically dimmable lighting or delayed pump-
ing, are particularly important to microgrids simply by their scale. Inevitably
in small power systems, load variability will be more extreme than in utility-
scale systems. The result is that load control can make a particularly valuable
contribution to a microgrid.
Both deﬁnitions reveal the main characteristic of MG, which is coordinating its internal
elements. The coordination forms an independent energy unit to achieve local demand-
supply balance. Based on the internal control, this group can bring proﬁts for both utility
grid and interior parts [Ton et al., 2012]. Firstly, it enables the modernization and inte-
gration of multiple Smart Grid technologies. Secondly, the integration of distributed and
renewable energy sources is enhanced. The increasing generation supplies the MG’s
load to reduce the load distortion in the utility grid. Besides local generators decrease
power loss by supplying loads in short transmission distance. Thirdly, the cooperative
method also promotes the participation of customers by demand-side management. Fi-
nally, the self-balanced MG supports macro grid and bulk power systems by providing
ancillary services, such as compensating intermittent generation.
The MG operates as an ancillary while connecting to the utility grid. It could also be iso-
lated as an independent power unit to avoid the faults impacts from outside or to segre-
gate local errors from the global environment for other parts recovery. The combination of
both patterns enables the ﬂexible conﬁguration of the power system connection. It further-
more promotes the transition of the traditional power system to the smart grid. Especially
under the increasing insertion of intelligent elements and electronics infrastructures, the
utility grid becomes more complicated than ever before. The MG imports the concept of
deconstruction to solve the complex issues caused by system expansion. It shows great
potential in solving environmental and economic problems. Incentives of expanding MG
include: 1) Energy demand from an isolated area. Some electricity users are located in
a remote area and have no access to utility grids. They rely on a sustaining power sup-
ply for speciﬁc applications, such as offshore drilling platforms or military bases on high
altitude. 2) The increasing insertion of intermittent renewable generators. Enlarging the
share of renewable generation is an effective way to relive the deteriorating environmen-
tal problems due to low carbon emission. In recent years, the falling cost of renewable
sources furthermore promotes their widespread establishment. However, the output har-
monics from renewable sources lower power quality. Besides its non-dispatchable and


---

Page 27

---

12
CHAPTER 1. INTRODUCTION
intermittent generation cannot match the load curve, which causes demand-supply im-
balance. The low inertia of electronics converters causes rapid change. It breaks the
dynamic power balance as traditional bulk generators of low generation ramp cannot fol-
low the fast change [Roche, 2012]. 3) Proﬁtable objective. Distributable loads emerge as
intelligent devices to adjust the requirement of consumers. Demand-side management
provides a solution for economic power dispatching. For example, peak-load shifting is
widely applied to the domestic consumption with electric vehicles, intelligent heating sys-
tem, and so on. Thus the scheduling method for these loads and energy storage systems
is highly demanded. 4) System reliability. The sufﬁciency of power supplying to cus-
tomers determines the power system reliability. The lack of energy happens mostly under
fault conditions, which could be relieved by inputting the backup sources. However, due
to the lack of sensors and breakers, it is almost impractical to detect the accurate location
of faults and remove it timely without load shedding. Controlling the faulted system is
even more complicated. It could furthermore cause a cascade of failure and extensive
power outages because of the network coupling. Thus the electrical connection between
elements enlarges the impact of faults and lowers the reliability of the system. For ex-
ample, the 2003 Italy blackout and Northeast blackout of 2003 cause huge proﬁtable loss
and affects the lives of millions of people [Andersson et al., 2005]. Deconstruction of the
large scale power system simpliﬁes the problems of failure detection and recovery. The
extensive network is separated into multiple independent parts, and the consisting ele-
ments coordinate and achieve partial power balance. Hence, this operation could isolate
faults and recover all the loads timely [Ross et al., 2011]. 5) Low cost. The expansion
of a power system imports longer and more transmission lines. Thus the power loss
caused by energy transmission increases. Especially in the system of low or middle volt-
age level, the loss could be large even if the volume of power ﬂow is not massive. This
cost motivates new approaches to supply consumers with power from electrically close
sources.
The architecture of the MG reduces the complexity and coupling in the electrical system,
but inserting it into the utility grid raises new issues. This power system still demands
more reliable, proﬁtable, and ﬂexible solutions to compromise with or even tackle the
complicated operating problems. Given the advantages of MG and its wide application,
there are hopefully MG networks in the future electrical grid. However, the operation of
MG faces challenges which hinder its wide application.
1) Weak resistance and reliability under faults. Due to the limited capacity of DGs, the
stability depends on the coordination of all the elements, including load curtailment.
Such a system lacks sufﬁcient backup sources to rescue sudden outages and tends
to shed components for power balance. For example, dispatchable sources could
compensate the intermittent output of renewable sources. Thus their outages will
cause a system shutdown as the shortage of compensating power breaks the power
balance.
2) Economic maximization. Even though the demand-supply balance is a priority for
the MG, maximizing economic beneﬁts in power dispatching is another control ob-
jective.
Taking full advantage of the renewable generation is proﬁtable as their
original sources are free.
However, surplus generation could cause curtailment
of renewable generators. It lowers the device use ratio and furthermore weakens
its contributions. The control strategy, which sustains the renewable generation, is
crucial and imperative.


---

Page 28

---

1.1. CONTEXT
13
3) The combination of isolation and connection to the grid. Independence from the util-
ity grid enables the supply of the island and remote area. Additionally, the control
focuses on the internal elements and optimizes their cooperative behaviors accord-
ing to the diversiﬁed characteristics. Whereas the isolated MG is vulnerable in case
of internal faults. Connecting MGs to the network could maintain a reliable load sup-
ply, but the intermittent generation causes a demand-supply imbalance in the utility
grid. It is beneﬁcial to utilize the advantages of both modes and avoid shortages.
Corresponding control strategy for MG is necessary.
4) Optimal operation.
The optimal service within MG aims at promoting economic
proﬁt, environmental beneﬁts, and so on.
Based on the prediction of elements
operation, it is achieved by optimally dispatching power between various generators
and loads. If the loads and generators are distributed and dispatchable, the power
dispatching issues will become more complicated due to the increased variables
and following constraints. Hence more developed algorithms are required to get a
solution.
5) Communication efﬁciency. Ranging from information sharing to coordination control
within MGs, the underlying communication network guides each element to achieve
common goals. Thus the dynamic and diversiﬁed power system demands an ef-
ﬁcient communication protocol and topology to maintain stability, timely efﬁciency,
and accuracy.
6) Loss reduction. The resistance of distribution lines causes power loss during en-
ergy transmission between MGs. Besides the system voltage level also determines
the power ﬂow on line. In a large scale of MG network, long-distance and dense
connections increase the transmission loss ratio and furthermore reduces the efﬁ-
ciency of power interaction. When the system is a middle-voltage (600V-69kV) or
low-voltage (below 600V) level, the share of the transmitted power is further de-
creased. This problem hinders the scalability of the network. The scalability is a
system property to handle a growing amount of work by adding components to the
system [Bondi, 2000].
7) Calculation pressure. With massive elements underpinning the operation of MG
networks, the power dispatching considering load curve and intermittent generation
becomes complex, especially when coordinating MGs for multiple objectives. The
optimization with a large number of variables usually forms a mixed-integer nonlin-
ear model, which challenges the combination of computation speed and quality of
results.
8) MG network scalability. A large scale of network imports more elements and com-
plex connections which increases the control complexity. Even though the traditional
centralized approaches possess a global view, its reaction delay reduces accuracy
and efﬁciency dramatically. Decentralized methods are widely applied to increase
partial automation and intelligence. However, the solution to global optimization is
limited due to horizon constraints, especially in an expanding network.
With incentives from advanced technologies and appeals of the electrical participant,
the future electrical grid likely includes MG networks, which consists of multiple MGs.
An example is shown in ﬁgure 1.5. Here, the MG usually contains renewable energy
sources (e.g., photovoltaic generators, wind turbines), microturbines, loads and energy


---

Page 29

---

14
CHAPTER 1. INTRODUCTION
storage systems (e.g., batteries). Due to the dispatchable generators and energy storage
system, the MG has limited ﬂexibility in the volume of absorbing and outputting power.
Thus it could be treated as a power unit which can behave as a battery.
MICROGRID NETWORK
PV
WT
MT
EV
GRID
MG
LOAD
Figure 1.5: Contents of future MG network.
1.1.3/
MICROGRID NETWORK
Independent MG maintains self-stability by coordinating internal elements. On one hand,
the isolation avoids the impacts from the main grid, such as a system collapse. On the
other hand, it consumes the intermittent generation locally to eliminate the distortion to
the generation schedule in utility grids. However, due to the limited backup facility, the
rescuing method to faults of internal elements (especially generator errors) is unique: load
shedding or generator curtailment. It reduces the use of elements and supply stability.
Connecting to the grid provides MGs with enough power support, but the intermittent
generation disturbs the generation plan and brings interference to the balance of the
main grid. Given the advantages of both modes, the faulted MG can be rescued by the
supported power from other MGs, while the isolation from the main grid is maintained.
This method is available due to plug-in plug-out characteristics, dispatchable generators,
and loads. The MG network could be found in areas with densely MGs settled such as a
community of domestic MGs and the faulted area restarted by splitting into MG collection.
As the coordination and independence coexist, it is more complex than simple elements
coordination. Each self-governed MG must participate in the system cooperative actions
as an autonomous entity. Problems in MG coordination include:
1) Modeling of MG coordination which involves the internal elements and MG behav-
iors. The coupling between elements and MG operation complexiﬁes the coordina-
tion control. The dynamic environment changes elements operation, which further
modiﬁes the system status. To maintain the global and individual objectives, MGs
coordinate the behavior of components to adjust to the new situation. The mutual


---

Page 30

---

1.1. CONTEXT
15
impacts between coordination behaviors and the system performance complex the
elements control. Its diagram is demonstrated in ﬁgure 1.6. An MG model shows
the essential characteristics which are determined by the operation of internal ele-
ments cluster. In this thesis, it includes the maximal taking in and sending out power.
The devices are operated to satisfy the coordination objective reversely. Thus the
lack of methods for decoupling the internal and coordinating control hinders the
modeling of the MG network.
Elements model
MG model
MG internal optimization
Network coordination
Figure 1.6: Diagram of mutual impacts between MG coordination and operation of internal
elements.
2) Allocation of MG operation mode (i.e., isolation and connection). As the coordina-
tion control sets a common objective to all the participating MGs, the information
sharing and optimal calculation among them are essential. However, a large scale
of coordinating group delays the time cost in both procedures. Thus the election
of connecting to the coordination group or isolation relies on new control strategies
and coordination architectures to improve the coordinating efﬁciency.
3) Optimal power dispatching algorithms. With the development of intelligent tools and
algorithms, the control is expected to promote the performance of networks in terms
of multiple aspects, such as reliability, environmental beneﬁt, and so on. Balancing
the weights of several objectives with appropriate algorithms is not easy, especially
when some control goals are contradictive. For example, the control for network
power balance reduces economic beneﬁts within individual MGs as the assistant
MGs generate excessively to supply the faulted MG. Thus the optimal power dis-
patching algorithms should take full advantage of the distributed network, the MG
operating feature and the diversiﬁed elements to optimize the system coordination
in a comprehensive way.
4) Network scalability. The extending system consists of more MGs and more ele-
ments. Therefore, it increases communication connections and calculation pressure
to the coordination control. The time cost in both procedures could cause reaction
delay and even invalidate the control behaviors. Thus the methods adjusted to a
wide range of network scales are essential to maintain timely performance, includ-
ing efﬁciency, reliability, and timeliness under a dynamic environment.
5) Intelligent control for distributed network. In the distributed MG network, centralized
methods control the elements collectively to achieve global goals. Promoting the
optimization performance of network coordination while maintaining the beneﬁts of
individual MGs generates a multiple-objective problem consisting of global and indi-
vidual goals. A large scale of information connection and calculation are demanded


---

Page 31

---

16
CHAPTER 1. INTRODUCTION
with the centralized approach. Besides, it has a risk of single-point failure. In the
decentralized methods, the coordination problem is split into multiple subtasks, and
each of them is addressed separately by distributed intelligence. However, it is
time-consuming, power redundant, and energy waste to coordinate all of the MGs
for compensating power lack in an individual MG.
6) Prevention of transmission overﬂow. The power ﬂow in MG networks should be lim-
ited by the transmission capacity to protect the infrastructure. As it is determined
by the power interaction between MGs, the power dispatching problem should con-
sider these constraints. Getting access to all the MG output directly from the as-
signed agents is not economical, considering the redundancy communication net-
work. Thus establishing an efﬁcient and practical interaction protocol for information
sharing is necessary for the power ﬂow calculation. Besides in the control sys-
tem, how to develop the power ﬂow calculation algorithms to match the distributed
system and individual intelligence are the main problems to improve the network
security operation.
1.1.4/
MUTI-AGENT SYSTEM
The MG network operates to gain individual MG objectives (e.g., maximizing economic
beneﬁts, minimizing emission, and so on) and global goals (e.g., maintaining stability).
Elements in the same MG should operate in a coherent and coordinated way. Thus, a
control system for individual MG is necessary to save generation costs, maintain device
constraints, and achieve global goals. Due to such characteristics of the MG network,
the multi-agent system (MAS) is applied as the MG control system. The reference of
[Wooldridge et al., 1995] deﬁned the agent as:
An agent is a computer system that is situated in some environment, and
that is capable of autonomous action in this environment to meet its design
objectives.
Agents are endowed with ﬂexible and autonomous actions, including environment per-
ception, reactions for self-interest , and interaction with each other to gain common ob-
jectives. A system consisting of such agents being the only one to act, an environment,
objects, relations between all the entities, a set of operations that can be performed by the
bodies and the changes of the universe in time and due to these actions, is called multi-
agent system [Ferber et al., 1999]. Agents communicate with each other to get global
objectives and are intelligent enough to react to the dynamic environment. These ad-
vantages match well to the control system as they enable the operation of plug-and-play,
active, and distributed approaches. Additionally, they make the system scalable and al-
lows modularity. Overall the characteristics allow the easy and quick adaption of MAS-
based control systems to MG networks according to consisting devices, control methods,
and size. Based on these factors, new communication topology is stimulated to support
the MAS. The research ﬁeld in intelligent systems is enlarged and furthermore applied
to many areas widely, such as the electrical system, telecommunication industry, and so
on [Pipattanasomporn et al., 2009][Logenthiran et al., 2011]. The optimization algorithms
based on MAS are also proposed to improve the reliability and efﬁciency of the control.
In this thesis, the MG network is an electrical system which consists of multiple MGs.


---

Page 32

---

1.2. OBJECTIVES AND CONCERNS OF THIS THESIS
17
Coordination among MGs is achieved by agent interaction, and single MG maintains their
independence by controlling internal devices. This physically and electrically distributed
system is characterized as a complex system which includes multiple entities in interac-
tion, and they operate to provide emergent rescue [Simon, 1996]. Thus the MAS ﬁts the
MG network well to promote individual intelligence and global management.
Although the MAS has been widely applied to the power system for device control and
energy management, a practical control strategy, which is suitable for the MG network
considering scalability and efﬁciency, is rarely studied. Besides the distributed intelligence
of agents has seldom fully used due to the centralized dispatching in power networks.
Current research of the MG focuses on internal energy management and the interaction
with the utility grid. The power coordination between multiple intelligent micro-power units
is neglected. Now the main problem lying in the MG network is how to optimize the power
dispatching with the ﬂexibility of the construction.
1.2/
OBJECTIVES AND CONCERNS OF THIS THESIS
1.2.1/
PROBLEM STATEMENT
This thesis mainly solves: decentralized optimization for power dispatching in dis-
tributed MG networks based on the MAS, considering system scalability and con-
trol efﬁciency.
The MAS provides a distributed method to operate MGs for individual objectives and co-
ordinate with other MGs for global goals. However, approaches, which match the control
system well in terms of MAS topology, intelligence establishment, coordination process,
and optimal power dispatching, demand to be further studied. They should meet the
control requirement of MG network in terms of stability, the combination of efﬁciency and
scalability, optimal power dispatching and power ﬂow calculation.
Firstly, system stability is a fundamental objective.
Due to the limited backup power
source, independent MG is not resistant to the faults, especially to outages of genera-
tors. MG interconnection allows power assistance between MGs. But the coordination is
not entirely reliable to gain sufﬁcient power for all the loads according to different coordi-
nation strategies. Load shedding is the most common method to prevent it from voltage
collapse and sustain the network system. However, the comfort of consumers is reduced,
and the load stability cannot be guaranteed, which hinders its industrial and commercial
application. Thus how to take advantage of the MG power interaction and the reserved
generation of individual MGs to maintain load and system stability is, therefore, a problem.
Then the open MG network leads to a dynamic construction of the system. The con-
trol methods should assort with a wide range of the system scale. Achieving common
goals among distributed MGs demands efﬁcient communication protocols for information
sharing and advanced calculation algorithms based on the MAS. Given that the MG net-
work is an open system allowing plug-and-play of MGs, its expansion is in expectation
as more DGs and users are inserting into it. However, the large scale of intelligent and
autonomous MGs with individual goals increases the coordination efﬁciency due to the
increasing communication connections and calculation pressure. How to adjust the algo-
rithms and MAS bilaterally to gain an efﬁcient approach for coordination while maintaining
high performance in both small and large scale network is the second problem.


---

Page 33

---

18
CHAPTER 1. INTRODUCTION
Optimizing the power dispatching is the third issue. To relieve the energy shortage and
global warming, renewable and clean sources, such as photovoltaic generators and wind
turbines, are widely penetrating the current power system. Their intermittent genera-
tion complexiﬁes the optimal scheduling of dispatchable generators in terms of demand-
supply balance. Additionally, distributed loads such as batteries of electric vehicles could
comply with the scheduling order. Maintaining demand-supply balance with the econom-
ically and environmentally optimal operation is the coordination objective both for inde-
pendent MGs and for the whole network. To this end, controlling dispatchable generators
and loads to guarantee the total load supply, compensate and allow the full adoption of
the intermittent power is the fundamental solution within individual MGs. However, cen-
tralized control to all the network elements is not practical as the communication link to
all the parts is time-consuming and such topology could cause single-point failure. The
MAS allows distributed power dispatching based on the MG unit, where agents complete
the coordination tasks with a decentralized way to reduce the managing elements. But
the generation cost and emission increased by the interacting power within MGs are non-
linear and discrete, considering internal control and device characteristics. Thus for an
MG, how to formulate the relationship between interacting electricity and the optimization
objects with more approximate approaches is the essential problem of MG-unit coordina-
tion.
Finally, the power ﬂow results from the comprehensive action of global MGs and it inﬂu-
ences the network secure operation. The current power system regulates the facility’s ca-
pacity to maintain the persistence of electrical infrastructures. For the transmission lines,
it limits the maximal volume of power ﬂow which is caused by power dispatching among
MGs. Hence the calculation of power ﬂow based on MG output should be studied. It is
usually solved based on global output information. In the network, the distributed agent
gets system information mediately from communication. But the message transmission
strongly relies on hardware, scalability, and protocols. It increases control delay and re-
duces the accuracy of coordination control. Therefore, accurate and timely methods for
decentralized power ﬂow calculations are demanded to guarantee secure operation.
To solve these concerns, we initially study the coordination of the faulted MG and its
neighboring MGs. A control strategy based on the MAS is proposed for power dispatching
among elements within cooperative MGs. To improve the information in the economic
beneﬁts, a bidding strategy of individual MGs is proposed for the electricity market. Then
the coordination group is extended to a larger scale for more economical operation. The
control strategy, consisting of participant MG selection and optimal power dispatching,
is proposed.
A simulation platform is established in Python to validate the proposed
approaches.
1.2.2/
COORDINATION WITH NEIGHBORING MGS
The coordination is studied among neighboring MGs, which enables network scalability
and minimizes the generation cost. A control strategy for the rescue of elements fault is
developed based on the MAS. It includes two stages: economic power dispatching and
power ﬂow check. The assistant MGs constitute a new segment centrally controlled by the
agent of faulted MG. Here, the method of Lagrange multipliers economically optimizes the
power dispatching. The average consensus theorem takes advantage of the neighboring
communication between agents to spread data of MG interacting power to the network


---

Page 34

---

1.2. OBJECTIVES AND CONCERNS OF THIS THESIS
19
and check the violation of caused power ﬂow. Redispatch happens when power ﬂow
beyond the capacity of the transmission line. This approach guarantees the reliability of
the system and the persistence of total loads during fault periods. However, it mostly
shares the micro turbine to the faulted MG and does not take full advantage of the battery
to reduce generation cost and emission.
Thus the electricity market is established for power trading between MGs to gain the most
economical operation in each MG. A bidding strategy is proposed for MGs to formulate
the mathematical relationship between output power and caused cost. The value of elec-
tricity price under maximal output multiplying the proﬁt coefﬁcient is assumed as the bid-
ding price as the faulted MG buys the most electricity from the cheapest sellers. Power
ﬂow calculation is also improved and well suited to the decentralized intelligence with-
out acknowledge of global information. This strategy saves time delay in gaining global
knowledge to improve control efﬁciency. The economic beneﬁts are also enhanced as
the battery and micro turbine are considered in one integrated formulation.
1.2.3/
COORDINATION WITHIN EXTENSIVE MG GROUP
In order to further improve economic beneﬁts and maintain control efﬁciency, the coor-
dination area is extended by importing more adjacent MGs of the previous neighboring
group and joining the new neighbors of the enlarged group. The coordination strategy
includes two stages: determining cooperative MG group and power dispatching among
elements. A distributed evolutionary algorithm is applied to the global agents to share
the calculation pressure for selecting optimal coordination group in terms of efﬁciency,
power dispatching calculation, and economic power dispatching. The searching routine
is based on the depth-ﬁrst search. In the second stage, the agent assigned to the faulted
MG controls all the elements in the group and solves the power dispatching formulation
for maximal economic beneﬁts based on quadratic programming. This approach gets
comprehensively good performance in terms of both calculation speed and beneﬁcial
results.
1.2.4/
SIMULATION STUDIES
In order to validate the proposed control strategies, this thesis develops a simulation plat-
form based on Python programming. It builds the user interface to input the electrical
system with graphic tools and data ﬁles. Additionally, the model of elements and system
operation represents their characteristics and is embedded as the main part of the simu-
lation. Finally, the MAS is simulated as the control entity and each MG is established to
an MG for operating control methods. The cases of 12-MG, 13-MG, and 34-MG network
are simulated on such a platform. In the 12-MG system, the MG network is connected to
the grid to maintain the system voltage. It is applied to validate the control for coordinating
neighboring MGs. To validate the scalability of proposed methods, the 13-MG and 34-MG
networks are simulated as well.


---

Page 35

---

20
CHAPTER 1. INTRODUCTION
1.3/
OUTLINE
The thesis has six chapters to represent the research of power coordination in the MG
network. The ﬁrst chapter represents the research context and motivations. It shows
the urgent demand for a current electrical system to the MG. The highlighted advantages
include providing electricity to a remote area, increasing the integration of intermittent
energy sources, scheduling various controllable loads to optimize the system operation,
and isolating the normal part from an electrical fault. Given the disadvantages of isolated
MG, the MG network emerges to improve the resistance to faults, ﬂexibility of individual
MG, and preventing the power impact from MGs to the grid.
For promoting the automation and reliability of the MG network, various methodologies
are applied and reviewed in chapter 2. The coordinating strategy contains reconﬁguring
and maintaining the constitution of individual MG. The corresponding control structure is
based on the domination among task-solving operators, including centralized and decen-
tralized control.
Thus the research shortage is mainly on the architecture design of an efﬁcient control sys-
tem and corresponding algorithms. The MAS provides a distributed control method and
a modeling methodology for MG networks, in which a holonic MAS emerges as a ﬂexible
structure. With problems of designing control architecture and promoting the coordination
performance, the requirements on system control are clariﬁed. Finally, the contribution of
this thesis is presented from the view of fundamental to application.
Chapter 3 establishes the simulator of MG network with a detailed conﬁguration of el-
ements based on the load data in UTBM, on which the performance of proposed ap-
proaches in chapter 3 and 4 are tested. It consists of the simulation of electrical infras-
tructures and the control system based on the simulation tools presented in this chapter.
Designing the MAS model involves the complex MG network into a simple system which
enables the control tools of MAS to be applied. Among various agent structures, the
holonic MAS is selected due to allowing the ﬂexibility of MG transmission in the coordina-
tion, and it provides multiple algorithms to the control. Among the problems hindering the
development of MAS, the conﬂict between global control and self-management stands
out. The efﬁciency of global coordination is improved by treating the MG as a unit, while
the internal control is based on the elements operating information. This chapter designs
the MAS architecture to the MG network, including the communication network and pro-
tocol. It is used to develop the framework of simulators testing the performance of the
proposed approaches with Python programming.
Chapter 4 presents two methods to gain a high efﬁciency on power coordination and
resistance to faults for the MG network, under whose framework of negotiation the proﬁt
is maximized. The architecture of holonic MAS is designed to gain high efﬁciency and
low redundancy based on the communication network in chapter 2, which dispatches
power among neighboring MGs. The infrastructures, including PV, WT, energy storage
system, and MT are modeled in this part, and the self-organized control within individual
MG minimizes cost. Thus a method of maximizing proﬁt is proposed by simplifying the
generation cost of each MG to a quadratic relationship with the output power, as well as
a method calculating distributed power ﬂow in the network. The simulation results are
compared with another way with centralized control architecture, demonstrating a faster
reaction on control. Furthermore, the MG generation cost is completed, considering the
generation cost of different sources. An electricity market is established for dispatching


---

Page 36

---

1.3. OUTLINE
21
power among MGs, whose bidding principle enhances the accuracy of generation cost
than the previous method. The power ﬂow calculation is developed by considering distri-
bution resistance as well. Test results verify its advantages over the ﬁrst method.
Chapter 5 focuses on the overall performance on efﬁciency and economic proﬁt of the
coordination while keeping the reliability of the network. The architecture of holonic MAS
is proposed to allow the ﬂexibility of MG reconﬁguration, which enlarges the scale of co-
ordination MGs to gain a more proﬁtable operation. The depth-ﬁrst search is adopted
to avoid communicational redundancy in MAS. For improving the control efﬁciency, dis-
tributed evolutionary algorithm programming is implemented to the coordinating agents
for parallel computation. In this part, the simulation results analyze the factors that inﬂu-
ence the control efﬁciency and economic proﬁts. They also show the advantages of the
proposed approach by comparing the performances of three other methods.
Chapter 6 concludes the previous work and summarizes the research. This part points
out the disadvantages and contributions of the proposed approaches by analyzing the
simulation results obtained from chapters 3 and 4. Perspectives on the development of
the MG network using MAS are listed.


---

Page 37

---



---

Page 38

---

2
RELATED WORKS
In this chapter, the literature about MG energy management is reviewed. As the objec-
tives of power dispatching and constituent elements in MGs are similar to the ones in
the main grid, related researches to both areas are concluded as well. The coordina-
tion problems are intensely studied in terms of physical structure, control architecture,
and optimization algorithms. Keeping the power balance is by adjusting the dispatchable
generation and distributed load given that MGs are self-governed. Fault conditions, es-
pecially generator outages, break the power balance of MG, which could not be rescued
within the isolated unit. Getting support from other MG to regain normal operation im-
proves the generation use ratio and load stability. Besides, the intermittent generation is
isolated from the main grid. This conception is achieved with methods mainly including
two ways. One is the MG reconﬁguration, which means that the components are trans-
ferred between MGs to achieve balanced power allocation. The other one is to keep the
MG unit and transfer energy by connecting lines to the demanding cluster. As for the
tradeoff between optimization area and control complexity in the network, centralized and
decentralized methods and algorithms are reviewed. Finally, given the architecture of the
MG network, the MAS works well in conjunction with it due to the similarity of functionally
and electrically distributed structure.
2.1/
COORDINATION
WITH RECONFIGURING
AND MAINTAINING
MICROGRID
As the development of electronics promotes the automation of electrical devices, the
feature of plug-and-play enables the ﬂexible elements transfer between MGs. The recon-
ﬁguration is essentially to modify the connection of components to form new MGs. It is
based on the breakers and backup transmission lines. This method could isolate faults
and promote supply stability globally. Studies on system self-healing provide referential
methods for the elements reallocation due to their common objectives of self-adequacy,
optimization operation, and so on. On the other hand, the ﬂexibility of MG isolation and
connection to the system enables the power interaction between them. The approach
of maintaining MGs keeps an original construction and only transmits power to support
unbalanced MGs by adjusting the output of distributable generators and energy storage
systems.
23


---

Page 39

---

24
CHAPTER 2. RELATED WORKS
2.1.1/
RECONFIGURING MICROGRID
Highly developed electronics technologies and information collection methods promote
the intelligence and automation of elements. Thus single items can operate indepen-
dently and coordinate within a group of devices. With suitable operation for breakers
and backup lines, devices could be transferred between MGs and compensate for the
power imbalance in the newly formed MG. Due to the limitation of feeder capacity and
system voltage, the reconﬁguration strategy normally includes 2-stages: the operation for
reconstructing MGs, and the limitation of maintenance during power dispatching.
[Yu et al., 2015] proposes a reconﬁguration strategy to maintain the crucial load supply
when faults happen under the limitation of electrical topology and operational infrastruc-
tures. To reduce cost and time delay, the operation number of switches is minimized
by connecting with neighboring groups of sufﬁcient energy. [Zidan et al., 2012] adds a
new control objective: minimizing the transmission loss. This consideration is achieved
by involving the restored loads to the near group directly connected by backup feeder
ﬁrstly, then the indirectly connected one. However, both approaches optimize the recon-
ﬁguration based on the negotiation with neighboring groups and one-by-one message
transmission lower the efﬁciency. Besides, the solution is not unique if the neighbors are
connected similarly.
To get the globally optimal solution with combined objectives including load supply, switch
operation and line loss, the MINLP problem in [Cavalcante et al., 2015] is approximated
to an MILP model considering both active and reactive power balance and limitation on
system operation. Another MILP model is presented by adding the operation of DGs
[Chen et al., 2015]. The optimization is solved based on the global information collected
by consensus theorem. Similar approaches rely on global information collection. Thus the
efﬁciency of the control is reduced. A model is presented to form a new MG to prevent the
impacts of faults [Ding et al., 2017]. It is further approximated to a mixed-integer second-
order cone programming for simplifying the computational complexity.
To further reduce the calculation pressure and improve control efﬁciency, intelligence
is adapted to the system entity. Considering the three-phase load maximization, a Q-
learning method is proposed in [Ghorbani et al., 2015] to endow intelligence to the feed-
ers. They decide their own operations by learning from the previous solutions, which
reduces the pressure of real-time information collection. A disadvantage points to the
inﬂexibility of the dynamic system construction. A hybrid structure is presented to com-
bine the partial element control and global perception [Ye et al., 2011]. The Q-learning
algorithm is applied to a collection of devices for a goal, which is adjusted based on the
network demands. However, this paper does not consider the system operating con-
straints.
Graph theory is a new concept for the reunion of elements in MG networks. To reduce
power loss and improve reliability statistics, The Spanning tree search is to reallocate
DGs and storage units for supplying critical loads, while non-critical loads are selected to
be energized. The optimization problem for reconﬁguration is solved by a linear matrix in-
equality algorithm [Fang et al., 2019]. In order to minimize the switching operation and the
shedding load, [Elkhatib et al., 2015] models the network as a spanning tree, where the
MG is a virtual feeder. This method is limited by the radial topology and it also demands
a sequential switch operation to avoid a loop.
The probabilistic characteristics of DGs are studied to maximize the active and reactive


---

Page 40

---

2.1. COORDINATION WITH RECONFIGURING AND MAINTAINING MICROGRID
25
self-adequacy of reconﬁgured MGs. Distributed energy storage resources and distributed
reactive sources are both allocated with Tabu search to improve the self-adequacy
[Areﬁfar et al., 2012]. Loads and renewable generation are predicted to make plans for
all the faults rescuing in the following one hour [Areﬁfar et al., 2013a]. The temporary and
sustained faults are classiﬁed in paper [Areﬁfar et al., 2013b]. [Baziar et al., 2013] adopts
a 2m Point Estimate Method to consider the uncertainties of elements operation. The
optimization problem is solved based on θ-Particle Swarm algorithm.
Overall, as the switch action causes cost and time delay, the MG reconﬁguration focuses
on the switch operation to supply the outage area timely and sufﬁciently. Limited by the
radial system structure, the sequence of switching behavior is controlled as well. Backup
feeders transmit energy between the newly formed area and its power ﬂow should be re-
stricted within the capacity. Besides, the system voltage drop is another concern referring
to connection modiﬁcation. Thus the priority of this approach is to determine the switch
behavior to supply load maximally and efﬁciently. However, energy management during
the load supply is not considered. Especially when there is sufﬁcient power to restore
outages, the optimal power dispatching becomes a critical issue to select in candidate
solutions.
2.1.2/
MAINTAINING MICROGRID
To avoid the caused problems by reconﬁguration, the MG feature, which is the ﬂexible
transition between isolation and connecting to the utility grid, is fully used for MG coordi-
nation to improve the system stability. By treating the MG as an integrated unit, it could
behave both as a load or source. A cluster of MGs constitutes an isolated network. The
coordination control aims at keeping power balance in the whole system, especially when
faults cause power imbalance. Therefore, energy management among MGs is deeply
studied.
A bi-level method is applied with the ﬁrst level for MG negotiation as a distinct entity and
the second level for device control within the MG. [Wang et al., 2016a] sets a common
point for power interaction between MGs based on their power ﬂexibility (i.e., the max-
imal output and input power of an MG). To minimize generation costs and satisfy the
elements’ operation features, MILP is applied to solve the optimization problem for MG
internal control. But the power congestion at common point limits sufﬁcient load supply
on a large scale of outages. [Wang et al., 2015b] uses the deterministic decomposition
algorithm and the concept of progressive hedging to solve the two-stage problem. The
operation within the MG is optimized and the penalty is added to the objective function
of each MG to maximize load supply and beneﬁts globally. A DC network is established
in [Liu et al., 2018] for MG energy exchange except for the AC exchange network. The
simpliﬁed model for power exchange considering power ﬂow is solved by a distributed
algorithm with convergence assurance based on the alternating direction method of mul-
tipliers. Still, methods in [Wang et al., 2016a] and [Liu et al., 2018] demand a common
bus or point for coordination.
By adding the maintenance cost and main grid trading expense to the economic con-
cern, [Tian et al., 2015] establishes a market for power trade in the MG community. The
bidding price of each MG consists of the linear cost model of internal sources, whose
non-convexity and nonlinearity are removed based on the piecewise linear functions and
logic constraints. This method could cause power trading between self-adequate MGs


---

Page 41

---

26
CHAPTER 2. RELATED WORKS
for maximizing beneﬁts and it is essentially the markets between generators rather than
MGs. The bid for MGs in [Logenthiran et al., 2011] is proposed based on the prediction
of facility operation and equal to the maximal value in all possible candidates. The trading
price and available power volume are derived from the top point of the generation cost
curve without considering system power balance. Besides, it neglects the start-up and
shut-down costs. Given the uncertainties of operation, a probabilistic price based unit
commitment approach using point estimate method is employed to model their impacts to
the MG price [Peik-Herfeh et al., 2013]. For a similar objective, the time-of-use and real-
time-pricing demand response programs are applied for the power interactions among
MGs, which is solved by a metaheuristic algorithm [Nikmehr et al., 2017].
Considering the relationship between the system voltage and power ﬂow, the droop char-
acteristics are applied to the coordination control. The hierarchical control strategy in
[Che et al., 2013] concerns the real-time power coordination to maximize the supply in
faulted MG. Droop control for DGs is the primary layer. The secondary level corrects
frequency and voltage errors from previous control in the MG controller. The tertiary con-
trol manages power interactions between MGs in a distributed system. [Ren et al., 2018]
adopts droop control to the power dispatching among MGs. It adjusts voltage volume and
frequency of each MG by controlling the output active and reactive power. Even though
the adjustment automation and speed are improved greatly, the system stability relies on
the communication speed. As for the droop control, DGs in MG risk becoming a current
source when the generation changes sharply.
Some elements of special features could improve coordination performance considering
power quality. Vanadium redox ﬂow battery is applied in the MGs due to its large ca-
pacity and precise SOC detection [Dong et al., 2014]. Its converters apply V/f control in
the assistant MGs and maintain the voltage level for both neighboring outages and local
elements when the remained capacity is large enough. It also reduces the inrush current
during energizing the transformer in fault MG with a capacity no more than two times of
generation. Two isolated MGs are connected by a back to back converter to compen-
sate for the power balance for each other during contingencies in [Goyal et al., 2016].
[Moreira et al., 2007] applies droop control between microturbines and batteries to in-
crease the capability of supplying all the loads in faulted MGs.
To compromise the generation cost, heat supply, and the caused emission, the power-
sharing schedule is proposed in [Gabbar et al., 2016] with multiple fuel options. Elements
in the MGs are scheduled in an all-in-one optimization and it is solved by a genetic al-
gorithm. [Lasseter, 2011] pays attention to the wasted heat during generation. It locates
the fuel-based generators near heat loads to match the requirement of both heat and
electricity.
[Lv et al., 2016] treats energy utilization as an important factor. To improve it with high
power quality, the MG power coordination strategy is explained by an interactive energy
game matrix. The formulated optimization problem is solved with a hybrid algorithm of
Rough Set Theory–Hierarchical Genetic Algorithm–NSGA-II. The game theory is also
applied in a distributed algorithm to reduce the power loss in transmission for coordination
[Saad et al., 2011]. The formation of MG groups for energy interaction is optimized based
on coalitional game theory.
In order to improve the resiliency of the MG network under emergency conditions, a
comprehensive control architecture is proposed [Colson et al., 2011a]. Each MG is self-
ordered to supply internal vital loads and then supply the faulted MGs.


---

Page 42

---

2.2. COORDINATION WITH CENTRALIZED AND DECENTRALIZED CONTROL
27
The coordination among MGs refers to the process of power dispatching. It includes
the generation cost and emission issues during scheduling. Besides various distributed
generators show advantages for achieving diversiﬁed objectives. Particularly, renewable
energy sources provide clear and free energy to relieve fuel consumption. However, the
power balance is an issue due to the intermittent generation and dynamic load. Especially
during the fault period in MGs, real-time rescue is crucial for the network reliability and
load supply stability. This approach considers power dispatching beneﬁts and optimizes
it in terms of economic proﬁts, environmental factors, and power loss.
However, the
restrictions of infrastructure are not considered during power interaction.
2.2/
COORDINATION WITH CENTRALIZED AND DECENTRALIZED
CONTROL
The control strategies introduced in the last section determine the cooperative behaviors
for certain objectives. On the other hand, the control structures provide a platform for the
implementation of achievable algorithms. Developed approaches and device allocations
are proposed in conjunction with them. Given the complexity of the system and the large
scale of the constituent elements, the perception of the whole network for global man-
agement and the computational difﬁculty for the solution are both challenging the control
methods. According to the literature, the control structures are divided into centralized
and decentralized topology with different advantages respectively.
2.2.1/
CENTRALIZED CONTROL
As each change of the electrical devices could cause voltage and power ﬂow change, they
can further impact the operation of all the other components. Thus analyzing the network
intensively in a centralized controller solves the system problems with a comprehensive
view. This structure is widely applied to the control within individual MG. The functions
focus on the power dispatching while maintaining the operation constraints, which are
similar to the ones in the MG network. Therefore, applications in both areas are included
below.
For the centralized MG coordination, an all-in-one optimizing problem for power dispatch-
ing is normally formulated with a series of constraints for the operation of the elements.
According to its mathematical properties, the solution appropriate algorithms are applied.
[Chen et al., 2016] gets a convex optimization problem to minimize the economic cost
in terms of generation, emission, and maintenance, which is solved by an interior-point
method. Adding the power loss, the objective is formulated by [Faria et al., 2011] a non-
linear programming and the Generalized Reduced Gradient (GRG) method is applied
to get the solution. Other optimization problems such as MINLP in [Wang et al., 2016b]
and MILP in [Moghaddam et al., 2011b] are solved by General Algebraic Modeling Sys-
tems. Another solver called Advanced Integrated Multidimensional Modeling Software in
CPLEX is adopted for MILP in [Elsied et al., 2015][Morais et al., 2010].
Another centralized structure is applied for supervising the power ﬂow and market oper-
ation. Each MG is treated as an integrated entity [Fathi et al., 2013] to trade power in the
market. The electricity market is established by the distribution network operator. This
operator is a service provider consisting of multiple functional software. These functions


---

Page 43

---

28
CHAPTER 2. RELATED WORKS
include supervising the power ﬂow and market operation among MGs. Each function is
treated as an independent activity and all of the MGs are able to achieve it. To reduce
the generation cost and peak-to-average ratio of load, an adaptive scheduling approach
is provided. An online stochastic iteration is applied to capture the randomness of the
uncertain consumer demand over time. The distribution network operator is also used
in [Wang et al., 2015a] for power-balance maintenance and generation cost minimization
in the MG network, considering uncertainties of DG outputs. For similar objectives, a
distributed market operator is deﬁned in [Parhizi et al., 2015] to set electricity prices and
determines the amount of the power exchange between market participators. It collects
power information from all the MGs and manages the network power trading.
The MG reconﬁguration adopts a centralized structure for determining the switch behav-
iors and their sequence globally.
The paper [Fang et al., 2016] collects the operation
condition and characteristics from all the elements to improve the utilization of DGs after
splitting the network. A linear matrix inequality approach is applied to optimize the allo-
cation of MGs. [Wang et al., 2015c] reconﬁgures the MGs during faults to maximize the
load supply. The uncertainties of elements and running conditions are collected. Accord-
ing to them, the network optimization problem is formulated as a stochastic process. A
scenario reduction method is adopted to get the solution to conﬁgure the reunion of all
the components.
The controller in a centralized structure gets perception to the whole network and could
provide a globally optimal solution. The constraints determine the solution space in one-
in-all optimization, which avoids the ﬁtness validation of the results. However, this struc-
ture demands communication links between the center and all the devices, and a fast
calculation for the solution. These factors reduce the practical value.
2.2.2/
DECENTRALIZED CONTROL
Due to the communicational and computational limitations, the system scalability is re-
duced. As each centralized problem could be decentralized to gain advantages in mul-
tiple aspects, the coordination problem is studied with distributed methods. It refers to
that partial components accomplish global goals based on local information. Thus the
communication and calculation pressure lead to an urgent demand for the exploitation of
distributed control strategies. Notably, this structure can further promote the automation
and intelligence of each part of the network.
Authors of [Luo et al., 2017] propose a multiple MG coordination control framework which
motivates resource sharing among MGs by forming a self-adaptive MG coalition. To sim-
plify the communication network, [Xu et al., 2011] offers a distributed average consensus
theorem method for data exploration for each MG to make self-determination for coor-
dination.
However, even though communication in both studies is distributed, agents
need to discover the complete network information, which is similar to centralized control.
The power interaction between the MG network and the main grid is modeled as a bi-level
problem [Asimakopoulou et al., 2013]. The lower level determines the power insufﬁciency
by optimizing the internal operation. Then the power requests are made to the upper level
where the controller determines the electricity price based on the demand value.
As the decentralized control demands a high level of automation and information discov-
ery to the control entity, the multi-agent system is widely studied and applied as a platform
and modeling method for the MG network.


---

Page 44

---

2.2. COORDINATION WITH CENTRALIZED AND DECENTRALIZED CONTROL
29
2.2.3/
MULTI-AGENT SYSTEM CONTROL
As each MG can operate independently as a power unit, a multi-agent system (MAS) is
applied to improve the system automation and intelligence. It will be further introduced in
section 3.2.2. Agents can process data in a distributed way. Thus the controller with this
ability is robust to single-point-failure. It improves the control speed and scalability. The
reliable and proﬁtable operation of the MG network relies on the MAS complementary
control methods considering agent interaction and agent self-organization.
Task-sharing is proposed in [Davis et al., 1983]. Herein, agents with multiple tasks get
support from less busy agents. It allocates the tasks among agents evenly to promote
the efﬁciency of the system. While [Ephrati et al., 1995] presents a result-sharing strat-
egy. Multiple agents solve the same problem to get a result with high conﬁdence. Dis-
tributed planning strategies decide the intention activities of each agent to ﬁnish global
coordination [Von Martial, 1992]. This thesis studies the optimal operation of the MG net-
work. The problem-solving strategies value reaction time to improve the control accuracy.
Agents in the multi-agent system are autonomous and intelligent enough to achieve self-
interest. Therefore, each constituent element can achieve global goals with distributed
control. [Elmitwally et al., 2014] establishes three kinds of agents for reconﬁguring the
electrical groups given the system operation constraints. The load agents check electric-
ity consumers and report the error to the feeder agent, which negotiates with neighbor
feeders for load transfer to avoid power congestion or voltage violation. A regulator agent
accepts requests from all feeder agents and adjusts the transformer to match the system
topology. With similar construction, the MAS is applied to maximize the load supply in
MG conﬁguration [Ghorbani et al., 2014]. The feeder agent is endowed with intelligence
based on Q-learning algorithm.
A multi-agent system, only including neighboring communication, is designed in the
[Solanki et al., 2007] for load maximization. The system consists of switch agents, load
agents, and generator agents. Each agent makes queries to the downstream neighbor-
ing agents and related proposals are answered and transmitted upstream. With the same
communication link and message transmission routine, a two-layer MAS including zone
agents and feeder agents is proposed in [Zidan et al., 2012]. Feeder agents negotiate
with each other for global information and zone agents monitor the local operation and
implement control actions.
Taking advantage of the communication capability of agents, the MAS is applied to model
the participants in the electricity market, which could be an MG. Each agent manages
the assigned facility for the local goals [Pinto et al., 2011].
To maximize load supply,
buying power from DERs to supply unserved loads in MGs has been investigated in
[Li et al., 2010] by controlling each element with corresponding agents. A central control
agent is applied to summarize the information of all the components to make reconﬁgu-
ration decisions.
[Zhao et al., 2015] and [Pipattanasomporn et al., 2009] both allocate agents to the elec-
trical facility to enable their predictive capability.
Thus, the accuracy of the energy
management schedule is improved.
Agents control MGs in two layers: coordinating
local components and negotiating with other agents [Nunna et al., 2013]. The work in
[Logenthiran et al., 2011] establishes a market for power trading between MGs. The as-
signed agents calculate bids based on the prediction of elements operation cost for each
MG.


---

Page 45

---

30
CHAPTER 2. RELATED WORKS
MG network is a complex system where there exist multiple MGs, and each of them
is self-organized by maintaining the supply-demand balance within internal elements.
Modeling it with the MAS is to get its outstanding abstractions by analyzing the sys-
tem from the fundamental items. Based on it, the control framework is provided for the
MAS application. Thus theoretical methodologies could support the design of the sys-
tem with maintaining system complexity [Kinny et al., 1996]. As each agent focuses on
the agent behaviors to gain individual and global objectives, the object-oriented approach
is widely applied to modeling agents such as Believe-Desire-Intension agent systems
[Booch, 2006, Ormandjieva et al., 2015]. It aims at constructing the agent with formu-
lating behaviors to gain the deﬁned individual and global goals. Formal methods pro-
vide mathematical basics, such as tools and techniques, to reliably specify and verify
the MAS model despite the complexity of the real system [Clarke et al., 1996]. It is es-
pecially useful for the system, which includes a large number of agents. Additionally,
bounded-rational and categorical approaches are applied to deﬁne the behavioral mecha-
nism and to guide the decision-making process of agents and the interaction among them
[Le et al., 2008, Ormandjieva et al., 2015]. The former one considers spatial changes,
while the latter focuses on interaction semantics among agents in the system without the
need for mathematics basics. In conclusion, this dissertation selects formal methods to
model the MG system based on its elements in the network. The model of the facility is
mathematically modeled according to electrical laws.
2.3/
CONCLUSION
Previous studies solve the coordination issues from diverse control strategies with differ-
ent control structures. Control strategies mainly involve MG reconﬁguration and main-
taining MGs. Corresponding control structures are divided into centralized and decentral-
ized topology. The control objectives include reducing the reconﬁguration delay, increase
economic beneﬁts, maintaining system security operation, and so on. The MAS, as a
decentralized system with high automation and intelligence individuals, emerges as an
adequate method to control the MG network. Selected references for multiple strategies
and structures are shown in table 2.1.
Table 2.1: Selected papers on coordination approaches.
Refs.
Strategy
Structure
[Zidan et al., 2012]
MG reconﬁguration
decentralized, MAS
[Wang et al., 2015c]
MG reconﬁguration
centralized
[Wang et al., 2016a]
maintaining MG
centralized
[Logenthiran et al., 2011]
maintaining MG
decentralized, MAS
However, there are still several problems with which the previous literature does not deal.
They can be included in the following:
1) How to select the coordinating MG for high reliability of supply and an economic
power dispatching scheme simultaneously?
2) How to coordinate the MGs with an efﬁcient approach which is not inﬂuenced by the
extending network scale?


---

Page 46

---

2.3. CONCLUSION
31
In the next chapter, these issues will be further studied and several solutions to them are
presented.
In conclusion, the current literature presents solutions for MG coordination. To improve
the efﬁciency and supply reliability of power coordination, energy compensation and el-
ements transfer are proposed. Corresponding algorithms and network topologies are
adopted, for instance, the GA, mixed-integer nonlinear programming, electricity market,
minimum spanning tree algorithm, and so on. The control object in a system ranges from
elements to individual MG. Supporting communication topologies and control strategies
are proposed, such as distributed and centralized control structure. Additionally, consen-
sus theorem and game theory are applied to the computation framework to optimize the
control system. The advantages and disadvantages of the coordination approaches are
compared thoroughly and listed in table 2.1. As the MG network is geographically and
electrically distributed, the MG’s automation and intelligence increase the efﬁciency and
supply reliability of achieving individual and global goals. Thus the multi-agent system is
adopted in this thesis as the control system.


---

Page 47

---



---

Page 48

---

II
CONTRIBUTIONS
33


---

Page 49

---



---

Page 50

---

3
MODELING AND SIMULATION
PLATFORM
3.1/
DEVELOPMENT OF SIMULATION PLATFORM
In addition to the simulation of fundamental electrical infrastructures, such as transmis-
sion lines and diverse facilities, the MAS is also involved in the simulated objects as the
control entity. Due to the electrical and physical distributed construction of the MG net-
work, each MG could be functionally independent and cooperative. Hence, the agent
concept is imported to simulate individual MG. It depicts the generation/load characteris-
tics, behavioral rules, and cooperative functions as an integrated entity. With quantitive
results derived from simulation, the characteristics of the MG network are analyzed and
the control performance of proposed approaches for coordination is evaluated.
Currently, popular platforms for the establishment of simulation mainly include Matlab and
Python. As a commercial software, the former one provides a simple programming lan-
guage, a large number of functions and a well-prepared simulation platform based on the
default installation of packages, as well as the support from a wide range of scientiﬁc
community. However, the charging functions, sealing algorithms, and code of no porta-
bility raise time and economic cost. While Python, as a programming language, is free
with a substantial amount of functions and allows the portability. The easy coding brings
Python extensive standard libraries. It is open-source and gives access to the details
of the algorithms. Thus, Python is adopted for simulation in this thesis considering the
demands for MAS simulation and algorithm development.
To build a functional MG network, electrical devices and the consisting network are mod-
eled based on their features and behaviors. With the mathematical representation and
discrete behavioral rules, this physical system could be transferred to a simulation.
3.2/
MODELING OF MG NETWORK
3.2.1/
MG NETWORK AS COMPLEX SYSTEM
The MG network consists of sources and loads with diverse features. Given the diverse
constitutive components for each MG and the various network topology, the power in-
teraction between MGs is complex.
To match them for the system supply reliability,
35


---

Page 51

---

36
CHAPTER 3. MODELING AND SIMULATION PLATFORM
optimal power dispatching for load stability and economic proﬁt is always in the most
crucial topics for electrical systems [Borbely et al., 2001]. Until now, load prediction is
widely applied to generation scheduling in the steady-status power system. The demand-
supply modeling contributes to maintaining the power balance and economic optimiza-
tion by dispatching power among generators according to the predicted load requirement
[Lampropoulos et al., 2010, Mohsenian-Rad et al., 2010]. In traditional power systems,
generators are mathematically modeled as voltage sources. The output is load-oriented
to keep standard voltage levels according to the Kirchhoff voltage/current laws. For exam-
ple, the electricity consumption in a city is predicted 24 hours ago and the local generation
will follow the prediction the next day [Sauer et al., 1998]. However, the integration of in-
termittent resources and various dispatchable loads reduce the guidance of load to the
generation. Electricity price bidding is inﬂuenced by the share of renewable generation,
and it is not completely dependent on the load proﬁle anymore. As for the MG network,
it consists of multiple MGs which are individually self-organized. The individual MG co-
ordinates internal elements including diversiﬁed generators, storages, and loads for self-
interest. The power imbalance caused by faults or disturbances highlights the interaction
among MGs, and the caused power ﬂow emphasizes the interdependence between sin-
gle MG and the whole network. Due to the expanding scale of the network and increasing
facility with different characteristics, it is difﬁcult to approximate the electrical system to
a simple circuit model and analyze it with explicit mathematical expressions, especially
under the fault conditions. Rechecking the system to ﬁnd new modeling methodologies is
urgent to study MG networks and solve current practical issues. Concluding its features,
they are shown in the following:
1) The self-organized MG blocks the interaction between internal elements and the
whole network, but their mutual impact exists. Due to the self-organized control,
elements are controlled within MGs and the interaction with the network is blocked.
However, their mutual impact exists due to electrical interdependence such as volt-
age and power ﬂow transmission. For example, the generator outages in a faulted
MG disorder the voltage frequency in the network and incent the generation in-
crease in other MGs to recover the system. Any change in the network could cause
a systematic chain reaction, while internal elements do not know about that.
2) The MG network is an open system. Thus the cooperative behaviors of individuals
should adjust to the dynamic topology and changing operations of elements. For
instance, the plug-and-play MG could join to the network in a random place at any
time, and the other MGs should constantly be prepared for the new participant to
cooperate with it.
3) The system operation has memory on the past operation. The current activity is
formed based on the previous status of the components. For example, the battery
aging problem collected from the initial start will limit its service time and stop its
current operation.
4) The network is a non-linear system in which a small disturbance could cause ﬂuctu-
ation on voltage or power ﬂow. The interdependence between elements and system
operating status worsens and enlarges the inﬂuences on more normal parts in the
system.
5) There are hierarchical phenomena in the network. Although solving the network
problem ultimately relies on the behaviors of elements such as output and load


---

Page 52

---

3.2. MODELING OF MG NETWORK
37
proﬁle. Other properties could only be studied at a higher level; for instance, the
network power ﬂow caused by power transmission among MGs.
6) The control system has damping or amplifying feedback loops. For example, the
converters of wind turbines apply the PI controller in the voltage control loop to
maintain the command value.
Thus the MG network could be regarded as a complex system considering the previous
characteristics [Bar-Yam, 2002, Randall, 2011]. As the MAS is electrically and physically
distributed and each agent could function independently, this system in conjunction with
the MG network provides a matchable structure for establishing the control entity. Thus,
the model based on it provides adequate paradigms for system design, simulation, and
analysis. A related application of MAS on electricity system backtracks to the year 1994
[Varga et al., 1994], and since then this technology keeps improving its merits and solving
power issues. In nowadays, the multi-agent system has been applied widely, which is
supported by advanced technologies on communication and automation.
3.2.2/
MULTI-AGENT SYSTEM
Consisting of interacting agents and the located environment, the MAS provides the anal-
ysis of the autonomous reactions, which is compensatory for the mathematical model
[Ferber et al., 1999, Orcutt, 1968]. It provides a paradigm for modeling and controlling the
complex system, which is heterogeneous. In the MAS, intelligent agents monitor the dy-
namic environment and react to it for self-interests or common goals. Changes in the sys-
tem could be caused by the agent behaviors or outside factors. Reactivity, pro-activeness,
and social ability are the main features describing agents [Wooldridge et al., 1995]. They
are reﬂected in the interactions between environment and agents, as shown in ﬁgure 3.1.
In the following sections, we introduce the basic concepts of the multi-agent system.
Perception and 
reaction to the 
environment 
Initiative behavior 
Interaction and 
coordination with 
others
Output 
reaction
Agent 1
Agent 2
Perception and 
reaction to the 
environment 
Initiative behavior 
Interaction and 
coordination with 
others
Output 
reaction
Environment
Figure 3.1: Agents and their environment.
3.2.2.1/
ENVIRONMENT
The environment is an important factor inﬂuencing the design and architecture of the
agent network. It is the controlling and monitoring objects for the agents. For explicit


---

Page 53

---

38
CHAPTER 3. MODELING AND SIMULATION PLATFORM
objectives, agents modify self behaviors for adjusting to the dynamic environment or even
inﬂuencing it based on the coupling between them. The environment characteristics are
normally identiﬁed in terms of the following lists [Russell et al., 2016]:
1) Perception of the environment. Getting a complete knowledge of the whole environ-
ment helps an agent to detect the change in time and even to predict the possible
future. However, due to the geographically distributed agents and physical limitation
on information-collecting infrastructures, they have difﬁculties to gain complete, pre-
cise, and real-time information to learn about their environment. The lack of percept
causes difﬁculties in the agent reactivity.
2) Determinacy of effect. The action of the environment could bring changes. The
one, where each action causes a single and ﬁxed result, is called a deterministic
environment. On the contrary, certain activity in the environment causes stochastic
inﬂuence. This environment is non-deterministic and it increases the complexity for
designing agents.
3) ”Memory” of the past scenarios. Memory refers to the dependence of current agent
performance on the prior status. If the agent’s performance only relies on the current
episode of the environment, developing the agent system is simpler as there is no
need to predict future scenarios.
4) Status of the environment. The static environment is only changed by the stimula-
tion of the agent’s action. It is on the contrary with the dynamic one, where a higher
process existing outside of the agents runs and modiﬁes the environment. The most
common dynamic one is the physical world. Agents have a small inﬂuence on such
an environment so that the requirement for dealing emergencies is higher than in a
static one.
5) Continuity of the environment.
If the percept and activity of the situation in the
environment could be described and quantiﬁed by a ﬁnite number, it is discrete.
Reversely, the continuous one demands a high recognition capability for the agent
system.
Identifying the environment in terms of these classiﬁcations is helpful for the establish-
ment of the multi-agent system. The agent behaviors and the system architecture should
be matched with the situated environment for better performance. Even though the tough-
est situation is the combination of dynamic, continuous, continuity, non-deterministic,
time-varying, and inaccessible features, assumptions and simpliﬁcations could reduce
the complexity and help to focus on the main researching ﬁeld.
3.2.2.2/
THE AGENT
Before network modeling, individual MGs are the foundation to construct the network.
However, the dynamic system takes a functional activity both based on the input and the
behaviors of coupling agents. These mutual impacts and random behaviors of agents hin-
der the modeling which is only based on a single mathematical representation. The agent
has advantages in processing dynamic and stochastic systems, especially on modeling
decentralized architecture [Borshchev et al., 2004]. Comparing with the other modeling


---

Page 54

---

3.2. MODELING OF MG NETWORK
39
methods, it represents a new process for dealing with the interactions between distributed
entities, as well as individual behaviors. System robustness is also shown in deﬁning the
global goals for all the agents. Within a complex environment, the agent’s perception and
the corresponding reaction have a mutual effect on each other. Establishing a distributed
modeling and decentralized control system could provide a capable framework which is
detailed to single elements and has a global view simultaneously.
The MAS could be a paradigm of modeling that focuses on the actions of individual agents
and the interaction with others. It is characterized by the following factors in the view of
practical modeling [Macal et al., 2005]. 1) Identiﬁability. The standard for identifying the
agent should be discrete to distinguish it from the other concept according to clear bound-
aries. They should include individual characteristics, rules on behavior management, and
the ability to make decisions. 2) Behavioral rules. Rules for regulating the agent behav-
ior and chasing goals are established to adjust the system to a dynamic environment
and achieve ﬂexible self-operation. 3) Memory. Agents spare data space for storing the
past operation and form experience to guide the current behavior. 4) Resources. The
resources which the agent models multiply the kind of agents. 5) Decision-making so-
phistication. Sophisticated decision making is necessary to tackle the inconsistency in
the dynamic system. For example, the conﬂict between global and individual goals needs
to be considered and ordered based on the mission priority.
The model and simulation based on the MAS are widely applied in the current complex
systems, ranging from abstract models to decision-support models. The former one de-
scribes prominent features based on ideal assumptions, and the latter one tackles the
practical strategy problems in the real power network. To solve the practical issues, the
modeling objects in reality should be analyzed based on the items introduced in this sec-
tion.
3.2.3/
THE MG NETWORK MODELING BASED ON MULTI-AGENT SYSTEM
Given the characteristics of the MG network introduced in section
3.2.1, it could be
regarded as a complex system. The MAS emerges as an outstanding paradigm for mod-
eling and controlling it. Similar to agents, the MGs in-network behave with the features
including distributed architecture, reactivity, pro-activeness, and social ability. Based on
these similarities, current modeling methods with the MAS is reviewed.
3.2.3.1/
DISTRIBUTED ARCHITECTURE
The MGs are geographically distributed and electrically connected, which is much similar
to the MAS. To comply with the MG blocks, the MG behaves in 3 manners including self-
organization, network negotiation, and bottom-up approach. They cover all the elements
operating in the network and provide a clear classiﬁcation for the control framework.
In the MG network, self-organization refers to the individual behavior of MG. It includes
the self-information collection and self-management for achieving individual goals. During
this procedure, the MG pays speciﬁc attention to the primary constituents. For instance,
in each MG, the internal devices coordinate with each other for the power balance and
stability of MG cells. Thus, each element is monitored, and all of their behaviors contribute
to the MG proﬁt and security.


---

Page 55

---

40
CHAPTER 3. MODELING AND SIMULATION PLATFORM
Electrically connected MGs compose the MG network whose supply reliability relies on
the MGs cooperative behaviors. Coordination between MGs emerges as a complemen-
tary method to allocate generators between MGs and to improve the utilization of gener-
ation. The power interaction makes full use of the network connection to match overload
MG with the power-spilling MG. It is dependent on the negotiation among MGs. Espe-
cially, when faults occur to the items, the faulted MG cannot maintain the internal power
balance and risks load shedding or generation curtailment. Negotiating with other MGs
for power support helps to preserve sufﬁcient supply and avoids the disturbance spread-
ing to the utility grid. Additionally, the negotiation between autonomous entities enables
new MGs inserting into the network without reconﬁguration for the whole system. The
characteristic of plug-and-play is proﬁtable for the construction and expansion of the sys-
tem.
A bottom-up approach is adopted on the management of the MG cluster based on the
behaviors of self-organization and negotiation. It is especially helpful to simulate the man-
agement process in a complex system where elements are integrated to form a network.
Given the clear identiﬁcation of fundamental infrastructures and its determination on the
construction of a higher level, it provides a more reliable and detailed approach than the
global model in terms of representing the network. The bottom-up approach is to process
components information in each MG to know their functions, operation, investment, and
so on. It ﬁnally aims at coordinating the monitored elements downward and negotiating
the MGs upward initiative and autonomously. As the global and individual goals of each
MG may be contradictive on operating infrastructures, identifying the priority of tasks is
necessary.
Complexity in modeling the MG network with agents is reduced by distributed information
processes and interaction between MGs.
With a detailed model of the infrastructure
and proper design on coordination behaviors, the operation of MG could be analyzed
comprehensively.
3.2.3.2/
REACTIVITY
Agent reactivity refers to the actions in environment modiﬁcation for damping caused
impacts on operation status and maintaining objectives. Such activity exists in the MG
operation. For example, the load volume and generation are changing according to hu-
man activities and the natural environment. The control system of MGs runs to main-
tain the power balance by coordinating the operation of internal elements and keep the
supply-demand equality within the network by negotiation between MGs with the limita-
tion of system security requirements. This characteristic is especially essential for facing
emergencies in the network. Faults on elements or distribution lines can cause distur-
bance on voltage or frequency. Under such a condition, MGs detect the outages and
reason the errors to isolate faults and maximize the normal operation of elements based
on the information of local infrastructures and the network. In other processes such as
fault restoration and consumption of intermittent power, reactivity contributes most to the
network autonomy, supply reliability, and ﬂexibility.
Inﬂuencing the operation of the MG network, the environment consists of geographical
locations, weather, mechanical entities, and human activities. The agent’s perception of
surroundings could help to predict the operation of components. The environment prop-
erties also affect the establishment complexity of agent modeling and control architecture


---

Page 56

---

3.2. MODELING OF MG NETWORK
41
[Russell et al., 2016]. The MG network environment, consisting of the weather, human
activity, and electrical facility, has the following features. 1) Inaccessible. Considering
the geographically distributed location, the independent operation of elements and the
practical limitation on the communication link, agents could hardly get full, accurate, and
the latest information on it. 2) Deterministic. The reaction of the MG network to the
environment is assumed to be unique. For example, the discrete behavior of human ac-
tivity causes single action to the operation of the elements. The generation of renewable
sources could be represented by a mathematical function based on environmental fac-
tors, such as the PV and WT. 3) Non-episodic. The MG performance relies both on the
current environments and the prior status, such as the aging problem of the storage sys-
tem. 4) Dynamic. The environment is changing even without the operation of agents —
for example, load changes along with human activities. During summer, the use of air
conditioners demands a higher supply of reactive power, while electrical heater increases
the resistive load in winter. 5) Continuous. With the continuous features in the weather
such as photovoltaic radiance, the environment has an uncertain and inﬁnite action and
perception.
With a complex environment, the agent’s knowledge and reaction to it has a mutual effect.
Establishing a distributed modeling and control system could provide an adequate frame
for controlling single elements and has a global view simultaneously. The reactivity of an
individual enables the fast reaction to the environment change, such as compensating for
the imbalance in other MGs.
3.2.3.3/
PRO-ACTIVENESS
Each MG has the initiative to achieve global or individual objectives. A single MG behaves
under the direction of designed goals. The pro-activeness of MG refers to its capability of
achieving goals by ﬁnishing certain procedures based on the assumption of system op-
eration. Spending the minimal cost on generation is, for example, a common objective for
the network operation. To gain this goal, the procedure includes predicting the load curve
in advance and dispatching power within sources according to the prediction to minimize
the generation cost. Achieving both steps and ﬁnally getting proﬁt results present the
pro-activeness. These behaviors are programmed initially and operated during the MG
functioning regardless of environmental stimulation. Pro-activeness enables the predic-
tion for possible situations and makes plans or recipes to deal with it. However, in the MG
network, i.e., a dynamic environment, the prediction is not entirely accurate being given
the practical condition. The error could fail the directed goals. Reactivity could add auxil-
iary activities to compensate for the unexpected changes from outside and maintains the
designed targets.
3.2.3.4/
SOCIAL ABILITY
Negotiation between MGs provides information for the whole network, enables the coor-
dination for achieving global goals, and improves the ﬂexibility of its construction. Due
to the geographically distributed location, large constituent elements, and accompanying
huge operating information in MGs, it is difﬁcult and costly to get a complete perception
timely for each entity. Negotiation helps to transmit the local environment information to
remote ones. In this way, global information could be discovered by each MG. The elec-


---

Page 57

---

42
CHAPTER 3. MODELING AND SIMULATION PLATFORM
trical connection combines the operation of all the MGs, and it also determines the global
operation. Negotiating with others to schedule optimal behaviors for a global objective is
another requirement. Given the non-stability condition in practical applications, negotia-
tion makes the plug-and-play MG easier to be integrated into the network instead of being
rejected by the past structure. This characteristic is particularly contributive to network
emergencies such as speciﬁc faults occurring to the network. According to the commu-
nication information, MGs locate the fault and isolate it in a short period to guarantee the
system security. Supplying power to unbalanced MGs is another social activity to gain
global balance.
3.2.3.5/
MODELING OF THE MG NETWORK
As MGs integrate into networks extensively with maintaining self-independence, the com-
plex system needs an adequate method to model it. Operating information in the MG
network is detailed into the status of the elements such as the output power of wind tur-
bines. Distributed computation in each MG for individual interests is widely applied and
highly developed. These factors enable the MAS to be applied to the MG network. As
an autonomous entity in the MG network, the priority of each MG is to maintain the inter-
nal balance. Based on stable constituents, system supply reliability is guaranteed. The
second task of the entity is to coordinate with faulted ones for maintaining systematic
balance. Independence removes communication redundancy and weakens the coupling
across MG. Therefore, the scalable paradigm allows the MAS to model and control the
distributed network. It furthermore promotes the application of distributed control strategy
and related algorithms. For example, the MG could maintain the internal power balance
and output energy to keep system stability. Agents get access to global information due
to negotiation, which endows the system with advantages of plug-and-play, resilience to
the fault, supply reliability, and ﬂexibility. For the MG network, each MG maintains individ-
ual balance and keeps power interacting with others for system security, which could be
modeled as an agent.
Individual MGs consists of various electrical infrastructures including generations, energy
storage system, loads, and lines according to their functions, as shown in ﬁgure 3.2.
The control objectives determine the element’s behaviors and are constrained by facility
operating features. For instance, the network power balance relies on the stable operation
of elements. Based on the mathematical model for the devices, the activity of the MG
network is simulated by the agents.
In recent research on MAS modeling electrical systems, agents describe the element
features and guide their operation according to system goals. It tends to represent the
functional subparts (e.g. the category of generators) rather than the electrical entity (e.g.
a certain wind turbine). Agents in the model are usually divided into three applications in
terms of the modeling object: modeling devices in MGs, modeling a cluster of elements
and modeling virtual services.
Firstly, the agent models a category of electrical devices. Considering the variety and
automation of elements in MGs, coordinating them to promote the performance of the
MG and maintain the security operation relies on the negotiation and self-adaptation.
Agents represent the operation characteristics of elements such as output limitation of
generators and storage status of batteries. Moreover, agent behaviors are described
explicitly under the guide of global goals. Such models are widely applied in the supply-


---

Page 58

---

3.2. MODELING OF MG NETWORK
43
MG2
MG3
agent1
PV
BATTERY
MT
LOAD
MG1
agent2
agent3
MAS
Figure 3.2: An example of MG constitution.
demand balance control. It enables the equipment of load prediction, economic bidding
strategies, and so on to promote the performance of MG in terms of proﬁts and balance
accuracy [Duan et al., 2008, Kuznetsova et al., 2014, Logenthiran et al., 2008].
Secondly, the agent models a cluster of elements. Forming an independent group by
operating a bunch of components cooperatively for supply-demand balance helps to im-
prove the ﬂexibility and avoid one-point failure. For example, the MG is a collection of
energy entities and consists of the network.
It takes charge of internal coordination
among elements and external interactions with the located network, which determines
the operation status of the system. Individual and global percept is the foundation for
energy management. The agent models the supervisory behaviors, and it designs the
reaction to the dynamic environment to represent the control and operation of the MG.
The corresponding application includes power trading in electricity markets, MG restora-
tion, and self-healing issues. The agent metaphor extends as an integral representa-
tion of collections of goals-oriented entities. For example, agents modeling the MGs as
participators in the market represent the bid in the delegate of its power consumption,
generation, and corresponding cost based on the features and control methods. The bid
ﬁnally conﬁrms trading deals by interactions among agents. Comparing with the previous
modeling, this one considers the variety of coordination behaviors and gives a clue to
the design of cooperative control, especially under the framework of real-time scheduling
[Duan et al., 2008, Wang et al., 2011, Colson et al., 2011b].
Thirdly, the agent models virtual services. Ancillary services such as information trans-
mission and control center help to maintain the security operation and improve the sys-
tem performance in terms of various aspects, including proﬁts, resistance, and ﬂexibil-
ity. These virtual services are modeled by agents based on the function-oriented ob-
jective. Different from the model of substances in electrical systems, they describe the
computational program in controlling the system. The modeling agent is self-activated,
condition-triggered, embedded on a host for the context perception to start functioning
and demands for the support of other services like communication. An example of an
agent modeling data center is widely adopted in the distributed electrical system. It rep-
resents the process of data storage and the contents of the data used for global control
[Colson et al., 2011b, Zhao et al., 2015].
Apart from the agents’ behavior, electrical architectures of the system determine the
topology of MAS modeling, which further impacts the following coordination control. The
distribution lines both possess electrical features such as resistance and resemble the


---

Page 59

---

44
CHAPTER 3. MODELING AND SIMULATION PLATFORM
path of power ﬂow, which thus enables the power interaction and enlarges elements in
coupling. In MAS modeling, such infrastructures are divided into interacting lines and
agents resembling devices. Corresponding control algorithms respecting their limitation
are further studied to achieve optimization objectives based on the MAS.
3.2.4/
MULTI-AGENT SYSTEM CONTROLLING THE MG NETWORK
With electrically and physically distributed MGs in the network, each MG controls com-
ponents autonomously for individual and global beneﬁts. Interactions between agents
provide global information to each agent and enable MG coordination. MG intelligence
relies on the control system, which includes the capability of reacting to the dynamic
environment and operating following default processes. Agents provide perceptual and
reactive functions for MG, which is thus widely applied.
3.2.4.1/
TOPOLOGY
The MAS consists of multiple agents that interact with each other. The communication link
forms its structure, based on which the control strategy is designed, and corresponding
algorithms are proposed. It furthermore determines behaviors with agents’ roles and their
mutual affection. The topology of MAS thus affects the performance of data transmission,
coordination strategy, and so on [Hayden et al., 1999, Weiss, 1999]. Current topologies
suitable for the MAS are described in the following [Horling et al., 2004]:
1) Hierarchies. Agents are allocated as a tree structure, and the ones in a higher layer
have a wider percept than the ones in a lower layer. Interactions are limited within
the connected agents and are forbidden across the branches. Monitoring is bottom-
up while control commands ﬂow downwards. Agents are divided into multiple small
groups which solve distributed problems. Interactions are thus reduced and inde-
pendent from the total population of agents. However, the system is fragile or rigid
under single-point failure.
2) Holarchies. Elements are holons which consist of subordinate entities downstream
and could compose other holons upstream. The autonomy degree of each holon
is undeﬁned, and holons in the same level interact with each other. The control
command ﬂows from superordinate holons to subordinate ones to achieve coop-
erative goals while keeping individual control on operating internal entities. Apart
from the hierarchical topology, it possesses partial autonomy and encapsulated na-
ture. These advantages provide holons sufﬁcient independence, reduce knowledge
stress of demander, and cooperation cost on adapting new conditions. The chal-
lenge is the selection of appropriate agents in holons.
3) Coalitions. The organization is ﬂat, which could be a sub-coalition or overlapping
coalition.
It forms without distinguishing cooperative and self-interest agents as
goals direct and vanishes as missions ﬁnish. The coordination between coalition-
separate agents only happens to achieve global goals. The least selection of par-
ticipants brings better rewards and solutions for more complex missions, as well as
optimal task allocation among agents. The disadvantages include the difﬁculty of
operating in a dynamic environment; partitioning agents keep interaction and dis-
trust between different kinds of agents.


---

Page 60

---

3.2. MODELING OF MG NETWORK
45
4) Teams. Several cooperative agents consist of a team and coordinate for a sharing
goal. Prioritizing the common goal, agents tend to behave consistently and sup-
portively, which endows the system with high resistance to disturbance. Group co-
ordination reduces the difﬁculty of solving signiﬁcant problems in individual agents.
It can reason the routine of agent interaction for increasing the ﬂexibility of operat-
ing in an environment without knowledge and prediction, followed by the advantage
of communication augment. The challenges of agents allocation for the high-level
problem, a consistent problem during execution, and correction of the team under
dynamics mainly hinder its application.
5) Congregations. Groups of entities formed by cooperative agents in a ﬂat organiza-
tion consist of a congregation to gain better performance. Different from the team
or holarchy, the congregation exists long-term to tackle multiple various problems.
Individual agent behaves rationally to gain itself long-term beneﬁts. Thus, the par-
ticipation of an agent to a congregation is interest-oriented individually.
6) Societies. It has a social construct and exists long. This topology is inherently
open for agents to enter and leave freely. It sets structure and order for diverse
participants with maintaining the ﬂexibility of interaction arrangement. To coordinate
diversiﬁed agents and enable their co-existence, certain constraints like universal
laws, norms, and conventions, are imposed on the agent behaviors.
7) Federations. This topology is composed of multiple groups of agents which are
partially controlled by a delegate representing a group. It is identiﬁed as the only
member that group members could interact with and communicate with the outside.
It cooperates with other delegates by driving local agents based on the knowledge
of their skills and needs. Such topology could reduce the amount of communication
and negotiation for local agents based on the delegate’s services.
8) Markets. Similar to federations, markets are usually open, and coordinating local
agents relies on speciﬁc particular individuals. However, participants are competi-
tive and keep self-authority. Agents trade necessary items such as services, tasks,
or goods in the market between agents or third parties. The market has grand
advantages in allocation and pricing. The expected outcomes are highly guaran-
teed based on abundant auction protocols. The derivation of bidding price and the
determination of auctions’ outcome are complicated. Security is another drawback
concerning transaction validation, cooperation, and so on. Maintaining the temporal
integrity and the complete transaction is essential for the formation.
9) Matrix organizations. The agent behaviors are inﬂuenced by multiple managers
or peers, and they can deduce backward the effects of their activities on multiple
entities.
Multiple lines of authority enable agents sharing resources for multiple
tasks.
Revealing the structure and behavioral fashion is for understanding the operation mecha-
nism to further design agents. An MG network with an increasing scale contains elements
of various characteristics. As global control relies on the real-time operating information
from all the elements, more communication connections for information collection are
demanded, which causes time delay. To coordinate diversiﬁed components, more math-
ematical models are built and increase the polynomial in the problem formulation. Both
increments add difﬁculty to control achievement. Hence a proper topology for organizing


---

Page 61

---

46
CHAPTER 3. MODELING AND SIMULATION PLATFORM
the interaction and activities of the MG can improve the speed of data discovery and sim-
plify the problem formulation. The scalability restricts global network coordination due to
transmission loss and time delays during communication. Partial coordination consisting
of selected MGs is a solution to improve system stability. This idea is adopted in this
dissertation. Corresponding selected agents should aggregate and cooperate for a com-
mon objective, while the other agents keep self-control and maintain interaction. To that
end, the agents controlling MGs should be able to form a collaborating group voluntarily.
Cooperative agents prioritize internal balance and coordinate with other agents to gain
the common objective. To maintain the system security, agents in the coordination group
should also keep communication with the self-controlled agents outside of the group for
monitoring the dynamic system power ﬂow and construction. The holarchies topology
endows the holon with partial autonomy and encapsulated nature. Agents with these fea-
tures can determine how best to satisfy the common objective of the assigned holon. The
task decomposition among holons also reduces the knowledge burden of each agent.
Thus the holarchies topology ﬁts the partial coordination of the network as the individual
autonomy of MG and common goals are combined well. Altogether, this topology allows
coordination algorithms to be adopted efﬁciently for diversiﬁed objectives in terms of eco-
nomic beneﬁts, emission reduction, and so on. System stability and scalability are ﬁnally
promoted.
Proposed in 1967 by Arthur Koestler, a holon can model a collection of constituent com-
ponents in the system. It is regarded as an element in a higher layer of the system
[Koestler, 1967].
A holonic MAS is applied to the distributed artiﬁcial intelligence in
[Rodriguez et al., 2006]. An example of the hierarchical architecture is shown in ﬁgure
3.3. Part of the agent herein collaborate to form a speciﬁc group, and this group behaves
as a component of the higher layer. In this research, modeling the MG network with
HMAS to represent the mutual affection among agents and the infrastructures are the
foundation of network coordination. Then applying HMAS control on the system to import
algorithms can furthermore improve the system intelligence and automation. The HMAS
in ﬁgure 3.3 is applied to the proposed approaches in this thesis and it will be further
introduced in chapters 4 and 5.
3.2.4.2/
CONTROL METHODS AND ALGORITHMS
The MAS decentralizes the complex problem in a large electrical system and solves them
in a distributed way.
With distributed artiﬁcial agents, agent’s functions are limited by the information, capa-
bility, and expertise. It is nearly impossible to solve a global problem by one agent in a
large system. The decentralized control is to coordinate multiple agents to distribute the
problem. The solutions to each subtask ﬁnally synthesize a global solution. Task-sharing
and result-sharing are two common strategies in distributed problem-solving. In the for-
mer one, agents pass tasks to the one with fewer tasks to share the calculation stress. In
the latter strategy, agents solve problems individually. The identical results, derived from
the same context, improve the conﬁdence in correctness, completeness, precision, and
timeless [Montgomery et al., 1993, Stankovic et al., 1985].
The algorithms are applied for agents to make optimal decisions. The intelligence en-
dows agents with autonomous activities and identiﬁes their independence. Increasing
infrastructures promotes the standard of communication, and the development of com-


---

Page 62

---

3.3. PLATFORM IMPLEMENTATION WITH PYTHON
47
Agent a1
Agent a2
Agent an
Agent a
Agent b1
Agent b2
Agent bn
Agent b
Agent c1
Agent c2
Agent cn
Agent c
Figure 3.3: HMAS architecture.
puter science supports the negotiation for operative decisions.
Both factors motivate
improvements in intelligence.
Self-interest oriented agents with social capability are
widely applied to the cooperative distributed problem-solving. Thus, the design of in-
teraction protocol and strategy in MAS impacts the operating performance. The negoti-
ation protocols can be evaluated from several aspects: social welfare, Pareto efﬁciency,
individual rationality, stability, computational efﬁciency, distribution efﬁciency, and com-
munication efﬁciency. The design of strategy demonstrates the cooperative behavior of
agents under the constraints of the protocol. For example, neighboring communication
motivates the application of consensus theorem for each agent to explore global infor-
mation. An interaction protocol is applied to the system to combine agents, while the
strategy is unique for each agent to solve particular problems and gain individual goals
[Mas-Colell et al., 1995, Maskin, 1983, Sandholm et al., 1996].
3.3/
PLATFORM IMPLEMENTATION WITH PYTHON
3.3.1/
MODELING OF THE ELECTRICAL SYSTEM
The simulation imitates the operation of the system, which ﬁrstly requires model develop-
ment. MGs compose the MG network. The distribution lines link them together to form
the system architecture and enable the power ﬂow between MGs. Intermittent generation
(e.g., wind turbines) and changing loads cause power disturbance in the grid. Dispatch-
able generators (e.g., micro turbines) compensate for the dynamic power demand coop-
eratively. Such behaviors are designed according to component characteristics and their


---

Page 63

---

48
CHAPTER 3. MODELING AND SIMULATION PLATFORM
physical connections. Thus, the MAS models the system from a global view, with details
of each agent and internal relationships, which reveals the difﬁculties of the control and di-
rects the available control method for objectives. MAS modeling electrical systems focus
on the coordination among multiple components. It includes the agent behavior, electrical
and communicational connections which reveal the power coordination and information
transmission, respectively.
Electrical elements compose MGs and demand coordination control to maintain power
balance within individual MG. These components are encapsulated as an entity of power.
Power distribution happens to strengthen network supply reliability when individual MG
cannot keep self-stability.
Thus models of the MG are divided into two aspects: the
elements model representing electrical characteristics and the behavioral model of MGs
including the coordination command [Duan et al., 2008].
Line connections between MGs depict the electrical topology and have a limitation on
power ﬂow. The impacts of power interaction between MGs to the distribution lines are
analyzed. The power ﬂow is calculated based on KVL, KCL, and iterative algorithms.
In the system consisting of distributed entities, decentralized power ﬂow calculation is
necessary [Stott et al., 2009, Baldick et al., 1999, Kim et al., 1997].
The distributed control of power systems relies on the operating information of electrical
constituents. The global goal is derived from collective behaviors of all the elements. In
control, the interaction between agents provides network percept and enables command
transmission. Thus the communication is designed with high efﬁciency or informational
reliability. Topologies include centralized structure, decentralized, and hierarchical struc-
ture based on the process of global data [Jimeno et al., 2011]. The centralized one has
an agent that supervises others, while decentralized one lacks data center and transmits
information locally. Hierarchical one consists of several layers of agents, in which the
agent in a higher layer manages the behaviors of agents in the lower layer.
In this thesis, modeling objects in an MG network includes MGs, electrical connections,
and communication structures. Considering the automation and intelligence, individual
MG is modeled by the agent-based modeling methods in terms of behavioral features
of elements. The model of the network devices is shown in ﬁgure
3.4, including the
attributes and behaviors of each component. The main components in MGs are mainly
divided into three classes in terms of energy metabolism: energy source, load, and en-
ergy storage system. Renewable generators (e.g., wind turbines) widely exist in MGs
for environmental and economic beneﬁts. The distributable sources, (e.g., fuel cell and
the microturbine), are obligatory to compensate for the supply of intermittent generation
and fulﬁll the load. As the power buffer in MGs, storage systems could store and release
energy to optimize the power allocation and provide energy support in a fault condition.
Herein, batteries are the most common facility currently as the higher energy density
than that of superconducting magnetic energy storage and supercapacitors. The energy
generation and consumption are collectively managed by an agent within each MG to
maintain self-balance. Energy interactions between MGs support the lack of energy and
promote the resilience of the system. This process is achieved based on the distribu-
tion lines connecting MGs. The physical characteristics and electrical requirements limit
power ﬂow, such as the line capacity and voltage standard. Based on the global informa-
tion, power distribution command is made among agents by negotiation, and the attribute
of MGs in the power network is the transmission power.


---

Page 64

---

3.3. PLATFORM IMPLEMENTATION WITH PYTHON
49
source
+operation state: bool
+output power()
+power factor()
photovoltaic generator
+parallel cells: integer
+irradiance: double
+area: double
+temperature: double
+output power()
wind turbine
+parallel cells: integer
+radius: double
+velocity: double
+angle: double
+output power()
fuel cell
+parallel cells: integer
+temperature: double
+output power()
micro turbine
+temperature: double
+output power()
components in micro grid
+PV number: integer
+WT number: integer
+FC number: integer
+load: double
+MG number: integer
+exchange power()
+power losses()
+voltage()
+current()
load
+operation state: bool
+operation power()
storage system
+output power()
bus
+resistance: double
+inductance: double
+power flow capacity()
+voltage()
*
1
micro grid
+power exchange()
*
*
line
+resistance: double
+inductance: double
+power flow capacity()
connection
+power flow capacity()
distribution line
+resistance: double
+inductance: double
+power flow capacity()
capacitor
+capacitance: double
+output power()
battery
+output power()
+SOC()
Superconducting magnetic energy storage
+inductance: double
+output power()
Figure 3.4: Modeling of MG network.


---

Page 65

---

50
CHAPTER 3. MODELING AND SIMULATION PLATFORM
Communications decentralize the system to a cluster of autonomous elements with pri-
vate information. Its topology is limited by the implementation cost and determines the
interaction architecture. The simulation represents the topology and interaction process,
as well as efﬁciency.
3.3.2/
SIMULATION PLATFORM
The simulation platform is established with the Python language, which consists of the
user interface and simulation space. The user interface is for the simulation parameter
input and stores it for running the model. The simulation space is for building an electrical
system set by the user, based on the embedded device model. Herein, the electrical
system is operated according to the control strategy and related algorithms. The cor-
responding diagram for the constituent parts in the platform is shown in 3.5. For the
simulation in this thesis, the MAS is simulated as a functional coding module. In this
dissertation, the 1-phase power system is studied to simplify energy management.
Modify the network
MG
MG
MG
User  interface
Save the network configuration
agent
agent
agent
Electrical system & MAS control platform
Figure 3.5: Diagram of the simulation software.
3.3.2.1/
SIMULATION INTERFACE
network ediction 
on graphical interface 
for small scale 
interface: Pyside
network ediction 
by file input 
for large scale
interface: Mosaik
tool: TortoiseHg
collect configuration to 
the same server  
Save configuration 
into dictionary with 
specific structure
Figure 3.6: Coding architecture of the user interface.
The user interface is applied to input the design of the electrical system by visualized
graph or data cluster. For users, they can select the items shown in the toolbar on the
graphic interface and connect them directly to build the electrical system, without knowing
the mathematical model of devices. For a large network, the numerous conﬁguration data
could be input directly by guiding its locating address. Both methods are achieved based
on the python packages shown in ﬁgure 3.6. The input activity presented in the user
interface includes: 1) creating an MG, 2) modifying the number of component elements
within MGs, 3) conﬁguring the operation parameters of components, 4) changing the
index of MGs, 5) save the created network information. The MG-building information is


---

Page 66

---

3.3. PLATFORM IMPLEMENTATION WITH PYTHON
51
translated into data collection with a speciﬁc structure. Pyside is adopted as a port for
Python programming to the graphic user interface Qt, which enables the graphical input
and establishes a visualized electrical system. Software Mercurial applies TortoiseHg
to achieve the input integration made in both graphical interfaces and ﬁle-reading. The
complete system conﬁguration is reorganized with a speciﬁc structure and stored in a
dictionary for simulating the system.
parameter
+nameParameter: String
+typeValue: emum[...]
+value: typeValue
+setValueType()
+setValue()
+getValueType()
+getValue()
component
+type: emun[...]
+nameComponent: String
+idComponent: int
+icon: String
+creaComponent()
+deleComponent()
+modiComponent()
InternBus
+idInternBus: int
+idComponent: int
+creaInternBus()
+deleInternBus()
microgrid
+nameMicrogrid: String
+idMicrogrid: int
+creaMicrogrid()
+creaComponent(Component)
+deleComponent(Component.idComponent)
*
1
SmartGrid
+Attribute1: type = defaultValue
+Attribute2: type
+Attribute3: type
+creaMicrogrid()
+deleMicrogrid()
DistributionLine
+idDistributionLine: int
+idMicrogrid: int
+creaDistributionLine(Microgrid)
+deleDistributionLine()
ElectricalLine
+idElectricalLine: int
+capacity: float
+creaElectricalLine(ElectricalLine)
+deleElectricalLine(idElectricalLine)
+construction()
Figure 3.7: Diagram of the models in user interface.
ﬁgure 3.7 presents the existent models shown in the toolbar of the user interface. The
relationship between them is clariﬁed with linking lines. Editable objects in the interface in-
clude MG, smart grid, internal bus, distribution line, electrical line, components, and their
parameter. The existent entity demands abstracts to clarify its identity and operations to
execute activities including creation, deletion, and modiﬁcation. Electrical objects in the
network are divided into two basic classes, including components and electrical lines in
terms of their roles in the electrical system. Components are controllable energy facility
which generates, store, and consumes it, while electrical wires are constant elements
transmitting power caused by power supply between components. To add all kinds of
facilities ﬂexibly, attributes of the facility clariﬁes the type (e.g., generator, load or storage)
and provide the link to a speciﬁc icon for the graphical interface. Its feature conﬁguration is
settled in the contained class called parameter which provides abstracts to deﬁne feature
properties and operations to assign them. Apart from standard identiﬁcation and oper-
ation activity, the electrical line also includes a deﬁnition for the capacity and service for
setting impedance. Two specialized inheriting subclasses including the internal bus and
distribution line deﬁne the wires inside and outside MGs correspondingly. Multiple com-
ponents connecting by internal lines form the MG which further consists of MG network
with distribution lines. Graphical input starts from MG network creation downwards to


---

Page 67

---

52
CHAPTER 3. MODELING AND SIMULATION PLATFORM
parameter conﬁguration of the component. Such top-down design clariﬁes the authority
of entities in each layer and streamlining missions to gain goals quickly.
(a)
(b)
(c)
(d)
(e)
Figure 3.8: The user interface: graphical interface and batch command line.
The user interface is shown in ﬁgures 3.8. The graphical initialization interface in 3.8a
includes the edition area, toolbar, component library, and activity options. The dialog
box appears to set the parameter after selecting an item in 3.8b and a complete MG
network is shown graphically in
3.8c.
For an extensive system, it is easier to input


---

Page 68

---

3.3. PLATFORM IMPLEMENTATION WITH PYTHON
53
the conﬁguration parameters directly from ﬁles and generate corresponding simulations.
Figure 3.8d and 3.8e show the user interface which could read the parameter ﬁle and
store the simulation system in the target structure. Modiﬁcation of the same project on
both interfaces is shared and could be shown in the graphic interface.
3.3.2.2/
SIMULATION OBJECT
Simulation for the system covers electrical infrastructure operation and the controlling
system achieved by software programming. Based on the input conﬁguration and con-
structed electrical system, the facility is deﬁned, and the MAS topology is the communi-
cation link achieved by function classes. This platform provides simulation for both actual
and virtual entities which are completely coded in Python. Its architecture is shown in
ﬁgure 3.9.
facility
MAS
communication
control
facility
MAS
communication
control
Figure 3.9: Architecture of the Platform Programming.
The abstracts of the network facility include operating parameters and behavior fea-
tures. A class is identiﬁed for inserting control strategies and related algorithms, which
is called MAS [Schurr et al., 2005].
The communication between agents is simulated
[Genc et al., 2013]. On the simulation platform, models of infrastructures output the op-
erating status in mathematical expression to the MAS system. Simulation on the MAS
should include the interaction process between agents and facility control between the
agent and the infrastructures. As the central function for agents, the control module col-
lects operating information of facility and other MGs to support optimal decision making
comprehensively. In ﬁgure 3.9, displaying the simulation results and providing visualized
exhibition platform complete the practical function of the platforms, as well as debug tools.
Figure 3.10 shows the programming diagram of the simulation platform. Starting each
simulation is by instantiating the classes in the platform and getting the results of run-
ning the instantiations. Chapter 3.3.1 introduces that each MG could be modeled as
an agent, which includes electrical elements, control systems, and its supporting facility.
Thus, the platform is composed of agents and connection lines. Class ”agent” is coded
with abstracts of the agent’s identiﬁcation and the step interval for the simulation object
periodically visiting the conﬁguration of the electrical system. Starting a case of simula-
tion is to instantiate this class with distinct abstracts to model individual MG system. This
class inherits from the class of ”Agent” in Smart Python Agent Development Environment
(SPADE).


---

Page 69

---

54
CHAPTER 3. MODELING AND SIMULATION PLATFORM
For testing cases and control compatibility, the component classes include importing data
parts, electrical facility parts, communication parts, control parts, and display parts, as
shown in ﬁgure 3.8. These parts are for diversifying test cases and control compatibility.
The function of inputting MG conﬁguration is a class. It includes architecture and facility
operation coefﬁcients. Each of its instantiations corresponds to the setting of an individual
MG. Data reading and recognition rely on a Python package called pandas. The facility
contains the classes of load, photovoltaic generator, wind turbine, fuel cell, microturbine,
and battery in terms of the mathematical model of energy generation and consumption.
All the facility begins operation by initiating conﬁguration parameters, stops by turning
off it and calculating the energy consumed or generated during running. Their abstracts
clarify the facility coefﬁcients in the mathematical model. Being an electrical unit, the
MGs calculate the collective characteristics caused by the coordination of elements. The
communication process is used for interactions between agents. Its simulation modules
are ”send” and ”receive” classes. The periodic behaviors are subclasses of the ”Peri-
odicBehaviour” of SPADE with the operations of sending and receiving messages. The
class of ”store” is mainly applied for decoding received messages and providing a buffer
for the previous messages. The class of ”control” is deﬁned as a cluster of various con-
trol algorithms based on the knowledge of the assigned MG and the interaction mes-
sages. The control algorithm concerns internal control and network coordination which
demands commanding assigned elements and communicating with other agents. Python
library provides abundant algorithm packages for simplifying the coding, such as pack-
ages of ”scipy” and ”sopt.” The distributed MAS interaction obeys consensus protocol to
gain global information for agents. Thus it is deﬁned as a component class of control to
provide network information and to simulate new algorithms on consensus theorem. The
”distribution lines” mimics wires between MGs. It is deﬁned by the abstracts of conduc-
tivity characteristics. The power ﬂow on it is calculated in the behavior of class ”control”
based on the voltage and power interaction of MG by getting access to the parameters
of the line. The package of ”PYPOWER” is quoted in this class to optimize the power
distribution as well. The class of ”log” displays the results derived from the platform in
ﬁgures and record the log of simulation, which could further help to debug the errors of
programming.


---

Page 70

---

3.3. PLATFORM IMPLEMENTATION WITH PYTHON
55
PhotovoltaicGenerator
+numCell: int
+valueIrridiance: double
+valueArea: double
+valueEfficiency: double
+valueMaxOutput: double
+getOutput()
+initializePV()
+endPV()
WindTurbine
+numCell: int
+valueVelocity: double
+valueAngle: double
+valueEfficiency: double
+valueRadius: double
+valueMaxOutput: double
+getOutput()
+initializeWT()
+endWT()
FuelCell
+numCell: int
+valueCurrent: double
+valueEfficiency: double
+valueMaxOutput: double
+valueCommand: double
+getOutput()
+initializeFC()
+endFC()
MicroTurbine
+numCell: int
+valueMaxOutput: double
+valueMinOutput: double
+State: bool
+valueCommand: double
+getOutput()
+initializeMT()
+endMT()
Microgrid
+idMG: int
+Mode: int
+valuePVPower: double
+valueWTPower: double
+valueFCPower: double
+valueLPower: double
+valueMTPower: double
+valueBatPower: double
+getPowerFlexibility()
+initializeMG()
+endMG()
Load
+valueLoad: double
+initializeL()
+endL()
Battery
+numCell: int
+State: bool
+valueCommand: double
+valueInitialSOC
+getSOC()
+initializeBat()
+endBat()
Agent
+idAgent: int
+valueTime: int
+initializeAgent()
+setupAgent()
+teardownAgent()
ImportData
+addrData: string
+valueTime: int
+getConfiguration()
+initializeImportData()
+endImportData()
Receive
+ReceiveInterval: double
+getMessage()
+initializeReceive()
+endReceive()
Send
+SendMessage: string
+idReceiver: int
+Send()
+initializeSend()
+endSend()
Store
+storeDict: dictrionary
+storeInterval: double
+storeMessage()
+initializeStore()
+endStore()
Consensus
+CoefficientsConsensus: metrix
+getNetPowerDistribution()
+initializeConsensus()
+endConsensus()
Control
+valuePowerRequirement
+IterationStep: int
+valueDifference
+initializedControl()
+endControl()
+NewtonRaphson()
+PowerFlow()
+getFacilityCommand()
Log
+axisTime: array
+getPlotArray()
+initializeLog()
+endLog()
DistributionLine
+idLine: int
+valueResistance: double
+valueInductance: double
+valueCapacitance: double
+initialiazeDistributionLine()
+endDistributionLine()
Figure 3.10: Coding diagram of the simulation software including the user interface, elec-
trical system, and MAS.


---

Page 71

---



---

Page 72

---

4
MULTI-AGENT BASED COORDINATION
WITH NEIGHBORING MICROGRID
4.1/
MOTIVATION
MG coordination has been widely applied in the ﬁeld of self-healing, system restoration,
and optimal power scheduling. Due to its capability of ﬂexible connection and isolation
from the utility grid, the electrical elements reunion motivates new solutions to the issues
in the current autonomous electrical system. As the MAS is applied to the electricity
network, the traditional top-down control is generally replaced by more ﬂexible bottom-up
approaches. All-in-one optimization involving large amounts of elements fades out as the
distributed control provides solutions of high quality considering the practical limitation in
terms of information collection, activity delay and calculation pressure.
In the MG network, the distributed control based on the MAS endows automation to
each MG for coordination and getting access to the global information. Thus the power
dispatching between MGs is triggered by the imbalanced MG and, while participants are
selected both by MG initiative intention and global interests. As the load and generation
scale within MGs is small, its demanding assistant power could be satisﬁed only by part of
the network. To reduce the communication amount and calculation pressure in reaction,
the coordination with neighboring MGs highlights because of the short transmission line
between them. Thus, the MAS solves the neighboring coordination by complying with the
functional network and embedding appropriate algorithms.
4.2/
COORDINATION PROBLEM
In this chapter, we mainly study the coordination between faulted MG and its neighboring
MGs. As the power interaction between them involves multiple individual entities consist-
ing of various elements, the cooperative behaviors of MGs and caused impacts to the
operation of internal devices are analyzed. To provide assistant power to the faulted MG
timely and economically, related problems are presented. 1) How to decide the assistant
of MG when multiple neighboring MGs exists. 2) How to dispatch power among elements.
3)How to quantify the impacts of the power interaction to the network power ﬂow, and to
reduce the violation of the line capacity. Two coordination strategies based on holon MAS
are proposed in this section.
57


---

Page 73

---

58CHAPTER 4. MULTI-AGENT BASED COORDINATION WITH NEIGHBORING MICROGRID
1) A centralized control strategy is proposed for the economical and reliable coordi-
nation with neighboring MGs, which consists of two stages: the power dispatching
process and the caused power ﬂow recheck. The Lagrange multiplier is applied to
solve the optimization problem which formulates the power dispatching. An average
consensus theorem is applied to explore global information for the distributed power
ﬂow calculation and check the capacity violation on line.
2) The concept of the electricity market is applied to the second coordination strategy
to further improve the economic beneﬁts and the efﬁciency of decentralized power
ﬂow calculation. The electricity price is approximated in the unit of an integrated
MG based on the internal optimal control. An improved power ﬂow calculation is
proposed by only knowing the neighboring voltage value.
The rest of the chapter consists of the following parts. Section 4.3 models the common
devices in a MG. Section 4.4 introduces the MG network, including physical and commu-
nicational structures. Section 4.5 describes elements control strategy in each MG and
the MG coordination control strategy is clariﬁed in section 4.6. Related simulation results
are presented in section 4.7. Finally, section 4.8 concludes this chapter.
4.3/
ELEMENTS MODEL WITHIN MG
Thanks to the development of electronics technology, electrical facilities with high auton-
omy and diverse generation characteristics are widely inserted into the MG. It enables
the large-scale application of renewable generators to alleviate environmental problems
[Mahmoud et al., 2014]. The variability of elements yet complicates the control and mod-
eling. Cooperating intermittent and controllable energy to supply load stably and ﬂexibly
is the prior issue. The economic proﬁt is another interest of study. For investigating the
elements’ mutual impacts in the same MG, their operations are studied, including de-
vice features, behavior, and generation cost. These characteristics compose the facility
model. The mathematical representation is simpliﬁed to focus on the input-output rela-
tionships and economic affections. Thus the calculation is reduced by maintaining the
main features of the facility based on reasonable assumptions. Assumptions are made
for the system as follows:
1) The objective of MG coordination is to minimize generation cost, which is derived
by the volume of generated active power. Thus the reactive power is neglected and
the power management focuses on the active power dispatching, which determines
the voltage frequency. As the reactive power contributes to the voltage amplitude,
ignoring it will lose the control to voltage volume. Therefore, the voltage drop on line
could not be considered and it will be equivalent to be constant in the network.
2) The operation of the system is discretized, considering the nonlinear characteristics
of the facility and their dynamic operating behaviors.
4.3.1/
RENEWABLE GENERATORS
Renewable sources are widely adopted in MGs to reduce carbon emission and save fuel
costs. The current popular generators are wind turbines and photovoltaic generators.


---

Page 74

---

4.3. ELEMENTS MODEL WITHIN MG
59
Operated by electronics converters, they stand out with small inertia to contribute a fast
reaction to the environment. However, renewable energy is uncontrollable with intermit-
tent characteristics. Such a facility is operated at the maximal generation to maximize the
conversion. The free renewable source such as wind and solar energy has no generation
cost by neglecting the small amount of electricity consumption on electronics facility.
4.3.1.1/
PHOTOVOLTAIC GENERATORS
The output characteristic based on the input of solar energy is represented in equation
( 4.1) and equation ( 4.2). It is based on the mathematical model in [Xu et al., 2013] and
some simpliﬁcation is further made according to more assumptions as follows:
1) Renewable generators are completely sensible to renewable sources. The gener-
ation of threshold to solar irradiation is set as 0, which means that the generator
output power since the solar irradiation exists.
2) The temperature on the PV cell retains as a constant of the standard value. The
assumption neglects the impact of the heat on the generation as the essential en-
vironmental factors inﬂuencing the generation is represented by the irradiation and
the coefﬁcients [Mutoh et al., 2006, Dubey et al., 2013].
3) The position and rotation of PV panels are ideal. As mechanical and geographical
affections to the generation have no direct link with power management, they are
neglectable in the generation.
Thus the output power is proportional to the solar irradiation and limited to the maximal
output by the constraints on hardware.
pout,PV = RPVIirrηPV
(4.1)
pout,PV ≤pmax,PV
(4.2)
Where pout,PV is the output power of PV, RPV is the irradiated area of PV cells, Iirr is the
density of solar irradiation, ηPV is the derating factor considering conversion efﬁciency.
pmax,PV is the maximal generation of PV determined by the hardware of facility.
4.3.1.2/
WIND TURBINE
The generation of the wind turbine is determined by the velocity and angle of the wind.
Such a model is a simpliﬁed representation derived from the mathematical model in
[Fernandez et al., 2006] under steady-status. The based assumptions include:
1) The air density is constant. The wind velocity and cut-in angle mainly represent the
energy volume.
2) The generation of the wind turbine is proportional to the volume of wind input power,
which is the product of the angular speed multiplied by the torque caused by wind.
3) The conversion efﬁciency is approximated as a constant determined by the hard-
ware of the wind turbine. Thus the hardware affections on the generation are sim-
pliﬁed considering the inertia, leakage ﬂux, mechanical damping, and so on.


---

Page 75

---

60CHAPTER 4. MULTI-AGENT BASED COORDINATION WITH NEIGHBORING MICROGRID
The model of wind turbine in equation ( 4.3) represents that the generation is proportional
to the velocity of cubic for a certain wind turbine. It has a maximize output limited by
facility production as shown in equation ( 4.4).
pout,WT = RWTW3ρ
2
ηWT
(4.3)
pout,WT ≤pmax,WT
(4.4)
Where pout,WT is the output power of WT, RWT is the rotor disk area, W is the velocity
of wind, ρ is the air density.ηWT is the derating factor considering conversion efﬁciency.
pmax,WT is the maximal generation of WT.
4.3.2/
MICROTURBINE
The microturbine usually takes charge of complementing the load demand. The gener-
ation is stable and dispatchable. Hence it belongs to the source of MG ﬂexibility. Es-
pecially in an isolated MG, it behaves as a voltage source to adjust the demand-supply
balance by maintaining bus voltage based on the curves of frequency/active power and
phase/reactive power. To simplify the model for power management under stable condi-
tion, assumptions of microturbine modeling include:
1) The inertia of the microturbine is as small as renewable generators.
Thus the
ramping volume of output is unlimited to compensate for the output of convertor-
controlled sources.
2) The time delays over facility control are neglected. The command is achieved imme-
diately to change the operation of the microturbine, without considering the interval
between command input and control output.
Thus the output power of the microturbine becomes a variable. It is derived from the
formulation of supply-demand balance, as shown in equation ( 4.5). The capacity of the
microturbine and its minimal output are shown in the constraints in equation ( 4.6).
pout,MT = pcommand,MT
(4.5)
pmin,MT ≤pout,MT ≤pmax,MT
(4.6)
Where pout,MT is the generation of micro turbine, pcommand,MT is the command of MG inter-
nal control to maintain power balance, pmin,MT and pmax,MT are the minimal and maximal
output of MT respectively.
The generation cost of the microturbine is the fuel expense of fuel, and it directly relies
on the value of output, as shown in equation ( 4.7). The start-up and the shut-down cost
is included in the price considering the establishment of the stator magnetic ﬁeld.
µMT = ηup down,MT
st
MT −st−1
MT
 +

η1,MT pout,MT + η2,MT p2
out,MT

st
MT
(4.7)


---

Page 76

---

4.3. ELEMENTS MODEL WITHIN MG
61
Where µMT is the total cost generating certain volume of power (i.e. pout,MT), ηup down,MT
is the cost over each change of operation status, st
MT and st−1
MT are the operating status
in the time steps of t and t-1, η1,MT and η2,MT are the cost coefﬁcients of generation
corresponding to the linear term and the quadratic term.
4.3.3/
ENERGY STORAGE SYSTEM
The energy storage system behaves as a power buffer in the MG by absorbing or out-
putting power. Thus it is normally applied to design economic scheduling and serve for
emergency rescue. The multiple functions of the storage system come from its bidirec-
tional converters which could be modeled as a current source. Batteries are the most
commonly used facility to store energy and provide portable services such as vehicle bat-
teries. Its modeling assumption is that power leakage is neglected. Thus the status of
charge (SOC) is changed merely by the charging/discharging operations. The storage
facility is operated as equation ( 4.8) shows. It is constrained by the output and capacity,
as shown in equation ( 4.9) to equation ( 4.11) [Dufo-Lopez et al., 2007].
pout,Bat = pcommand,Bat = pdisch,Bat −pch,Bat
(4.8)
pch,Bat ≤pmax ch arg e,Bat, pdisch,Bat ≤pmax disch arg e,Bat, pch,Batpdisch,Bat = 0
(4.9)
wt
ess = wt−1
ess + ηch,Batpch,Bat∆t −
1
ηdisch,Bat
pdisch,Bat∆t
(4.10)
wt
ess,min ≤wt
ess ≤wt
ess,max
(4.11)
Where pout,Bat is the battery output, which is the difference between discharging power
(pdisch,Bat) and charging power (pch,Bat).
It is determined by the system command
(pcommand,Bat). pmax ch arg e,Bat and pmax disch arg e,Bat are the maximal charging and discharg-
ing power, wt
ess and wt−1
ess are the SOC at time step of t and t-1 respective. ∆t is the time
interval for each step. ηch,Bat and ηdisch,Bat are the efﬁciency of charging and discharging.
Even though the fuel cost is zero for the battery, the aging limits the maximal charg-
ing/discharging cycle. Thus battery at charging or discharging status is consuming the
facility itself. Dividing the initial investment by total charging and discharging volume dur-
ing battery life is the cost for the unit operating power of the battery. The equation is
shown in ( 4.12) [Dufo-Lopez et al., 2007].
µBat =

ηch,Batpch,Bat +
1
ηdisch,Bat pdisch,Bat

πinv
2·NBat st
Bat∆t
(4.12)
Where µBat is the battery cost under discharging and charging certain amount of power,
πinv is the expense of initial facility investment. NBat the maximal charging/discharging
cycle during age. ηup down,Bat is the start-up/shut-down cost of battery. st
Bat is the battery
operation status at step t.


---

Page 77

---

62CHAPTER 4. MULTI-AGENT BASED COORDINATION WITH NEIGHBORING MICROGRID
4.4/
MICROGRID NETWORK COORDINATION SYSTEM
Power coordination between MGs involves a set of assistant hardware and software to
support the interactive activities ranging from consisting elements to the global system.
Electrical connections and communication networks, as the skeleton enabling the coor-
dination, possess speciﬁc features impacting the power distribution, interaction objects,
and so on. Similarities on the power supply and hardware establishment between both
connections provide mutual beneﬁts for their design.
4.4.1/
PHYSICAL CONNECTION AMONG MGS
In a system of multiple MGs, as shown in ﬁgure 4.1, the internal bus of MG allows bidi-
rectional power ﬂow, and the inner interacting power is transferred on it. It also connects
to the distribution system through a transformer for voltage adjustment. The power loss
on internal lines is neglected, considering its short distance. Due to the remote distance
between MGs, the optimal power ﬂow on distribution lines is calculated to reduce the
transmission loss. An assistant facility such as circuit brakes, transformers, and switches
are not considered in this thesis to spare less relevant facts and reduce the complexity of
the study.
MG2
MG3
MG4
MG5
MG6
Grid
MG7
MG8
MG9
MG
10
MG
11
MG
1
MG
12
Figure 4.1: An example of the electrical connection in MG network.
4.4.2/
COMMUNICATION NETWORK IN MAS
Communication between agents is the fundamental function of MAS enabling interac-
tions to gain external information and distributed control command. The topology and


---

Page 78

---

4.5. CONTROL STRATEGY WITHIN INDIVIDUAL MICROGRID
63
protocol of message delivery determine control performance, yet limited by the initial
economic investment to the establishment of infrastructure. The decentralized control
eliminates any central controller to monitor network operation. It demands all the agents
to have at least one communicational connection. Such a topology minimizes the re-
dundancy and reduces establishment cost [Petcu et al., 2005].
In practical electricity
grids, the communication line is encapsulated in the cable with energy transmission lines
[Elkhatib et al., 2015]. Thus the MGs connected by the same lines can interact directly.
To take full advantage of the lines and reduce the investment to communicational devices,
the neighboring interaction is adopted as shown in ﬁgure 4.2. Herein, the communication
link exists only between the MGs electrically linked. This topology can avoid information
congestion and prevent single-point failure. As each MG is connected to the network
electrically, neighboring communication guarantees that the information is sent to every
node in the network. Each agent sends messages to neighbors periodically to update the
information without being acknowledged. It saves time on having multiple neighbors and
spreads data globally in time. Besides, this structure can use powerline communication
with limited added cost.
Agent 
4
Agent 
3
Agent 
2
Agent 
5
Agent 
6
Agent 
9
Agent 
8
Agent 
7
Agent 
10
Agent 
11
Agent 
12
Agent 
1
Figure 4.2: Diagram of the communication corresponding to ﬁgure 4.1.
4.5/
CONTROL STRATEGY WITHIN INDIVIDUAL MICROGRID
The elements coordination control within individual MG derives from dynamic operation
status, including MG coordination and independent control. Thus the economic proﬁts
and power balance are both impacted primarily by it. Independent control within MGs
is the normal status for proﬁt and efﬁciency reasons. Internal faults causing power im-
balance switches the MGs status to coordination and involves the neighboring MGs for
power support. The coordination stops after MGs regain balance, only relying on internal
elements. Under both conditions, the control objective is to minimize generation cost to
maximize economic beneﬁts, along with the constraints including:
1) Maintaining power balance to improve MG supply reliability and resistance.
2) Maximizing and guaranteeing the load supply to promote the use ratio of the facility
and customer comfort.


---

Page 79

---

64CHAPTER 4. MULTI-AGENT BASED COORDINATION WITH NEIGHBORING MICROGRID
3) Maximizing the renewable generation to reduce carbon emission and promote the
use ratio of the facility.
Thus the renewable generators operate at the maximal
power point tracking as non-distributable sources.
4) Respecting the features and operational constraints of the facility to guarantee the
security operation and protect the supply reliability.
4.5.1/
UNDER NORMAL CONDITION
4.5.1.1/
OBJECTIVE AND PROBLEM FORMULATION
As an independent energy unit, the MG could keep internal power balance by elements
coordination control. Without intervention from outside, microturbines and batteries take
charge of balancing internal power for achieving the objective referred to at the beginning
of section 4.5. The output of these facility is the control object, which is formulated as
a quadratic constrained programming in equation ( 4.13) to equation ( 4.15). Equation
( 4.13) clariﬁes the balance between supply and demand.
The maximization of load
quantity (i.e., meets the demand as well as possible) is shown in equation ( 4.14) and the
economic optimization is in equation ( 4.15).
X
pout,PV +
X
pout,WT +
X
pout,MT +
X
pdisch,Bat =
X
pL+
X
pch,Bat
(4.13)
X
pL =
X
pmax,L
(4.14)
min µcost = min
X
µMT +
X
µBat

(4.15)
The constraints of facilities are listed in equation ( 4.1) to equation ( 4.12). Where pL is
the value of operating load and pmax,L is the value of all the load existing in the MG. µcost
is the generation cost of MG.
4.5.1.2/
CONTROL PROCESS
For each independent MG, the optimal control is a periodic behavior and starts from col-
lecting the operation information from each component in every cycle, which is shown in
ﬁgure 4.3. Based on these data, the power ﬂexibility of MG is deﬁned by the lower and
upper limits. The lower limit refers to the difference between generation and load under
the condition of distributable generators outputting maximal power as equation ( 4.16)
shows. For the upper limit, it corresponds to the condition of minimal MG generation with
maximal load, which is shown in equation ( 4.17). pmin,cap is the lower limit gotten in the
condition of shutting down microturbines and maximizing the charging power of batter-
ies. pmax,cap is the upper limit corresponding to the maximal output of the microturbine
and discharging of batteries. The Facility operation control means the optimization coor-
dination within individual MG. Without power interaction with others, this control aims at
self-balance with economic internal power dispatching. Related formulation is presented
from equation ( 4.13) to equation ( 4.15).


---

Page 80

---

4.5. CONTROL STRATEGY WITHIN INDIVIDUAL MICROGRID
65
Compute:
using (1)(2)
Power monitoring: 
PV, TW, Load etc.
cap,min
ip
cap,max
ip
Power 
balance?
Receive 
power 
request?
Y
N
Facility operation 
control 
START
Figure 4.3: Independent control ﬂowchart.
pmin,cap =
X
pout,PV +
X
pout,WT −
X
pL+
X
pmax ch arg e,Bat

(4.16)
pmax,cap =
X
pout,PV +
X
pout,WT +
X
pmax,MT +
X
pmax disch arg e,Bat −
X
pL
(4.17)
4.5.2/
UNDER FAULT CONDITION
4.5.2.1/
OBJECTIVE AND PROBLEM FORMULATION
The coordination process is stimulated by the loss of balance within individual MG, which
is essentially the rescue of multiple element groups to the faulted group. Hence the power
interactions happen between the faulted MG and the supporting MGs. Within the faulted
MG, minimizing coordination power is the constraint on coordination power, as shown
in equation ( 4.18). The supportive behaviors include energy import (pinput,net) to supply
overload and energy output (poutput,net) to consume surplus generation, where the value of
coordination power is the smaller limit in power ﬂexibility. While the assistant MGs outputs
power when the request command is positive and absorbs energy when the command is
negative. The power interaction between individual MG and network is unidirectional at
each time point as equation ( 4.20) shows. The power balance in each coordinating MG is
maintained, as shown in equation ( 4.21) and minimizing generation cost is represented
in equation ( 4.22).
preq = min
pmin,cap
 ,
pmax,cap


=
( pinput,net
pmin,cap > 0
poutput,net
pmax,cap < 0
(4.18)
pres =
( poutput,net
pmax,cap < 0
−pinput,net
pmin,cap > 0
(4.19)
pinput,netpoutput,net = 0
(4.20)


---

Page 81

---

66CHAPTER 4. MULTI-AGENT BASED COORDINATION WITH NEIGHBORING MICROGRID
P pout,PV + P pout,WT + P pout,MT + P pdisch,Bat + pinput,net
= P pL+ P pch,Bat+poutput,net
(4.21)
min µcos t = min
X
µMT +
X
µBat + pinput,netµinput,net −poutput,netµoutput,net

(4.22)
Where preq is the demanding power of faulted MG and pres is the supportive power from
assistive MGs. µinput,net and µoutput,net are the price of power buying from and selling to the
network respectively.
4.5.2.2/
CONTROL PROCESS
The internal coordination behavior is to distribute the generation to load under energy
intervention from the outside network as ﬁgure 4.4 shows. Monitoring the power supply
and consumption of all the facilities in MGs ﬁrstly, and the power ﬂexibility is calculated in
terms of equation ( 4.16) and equation ( 4.17), which rely completely on the features and
constraints of the local components. Then, the power imbalance is checked to identify the
faulted MG. For the balanced MG, they are potential assistant MG, which will ﬁnally be
selected to supply power for the faulted one. The one without participating coordination
will operate according to the control in section 4.5.1. To minimize interacting power with
the network, the overload MG maximizes generation and the one with surplus energy
maximizes load and battery charging power. In the assistant MG, the facility operation is
essentially power dispatching considering the coordinating power with the network. The
optimization is formulated from equation ( 4.18) to equation ( 4.22), whose results guide
the output of distributable generators and storage systems.
Compute:
using (1)(2)
Power forecast: 
PV, TW, Load etc.
N
Demand power 
from network
cap,min
ip
cap,max
ip
Power 
balance?
Receive 
power 
request?
Y
Facility 
operation 
control 
Y
Get quality of 
required power
START
Minimize 
interacting power 
with network
Figure 4.4: Fault control ﬂowchart.


---

Page 82

---

4.6. CONTROL STRATEGY FOR MG COORDINATION
67
4.6/
CONTROL STRATEGY FOR MG COORDINATION
Contingencies or faults cause disturbances in MGs and demand power support from the
network to avoid load shedding or generation curtailment. While global coordination helps
consolidate the system resistance to fault conditions and improve the efﬁciency of energy
allocation. Its control mainly aims at maintaining power balancing in the horizon of the net-
work to improve the resilience and supply reliability persistently under dynamic conditions
including steady status, emergent outages. Maximal economic proﬁt and environmental
beneﬁts are to optimize coordination. These global goals guide the process of the inter-
action and impacting self-control based on the MAS to motivate cooperative behaviors of
elements. The power coordination in the network contains two steps: power dispatching
among MGs and power ﬂow calculation on distribution wires. Two decentralized methods
are proposed in this thesis to optimize coordination: the one-in-all optimization and the
market method.
4.6.1/
STRATEGY 1: CENTRALIZED OPTIMAL DISPATCHING IN PARTIAL AREA
4.6.1.1/
MOTIVATION
It is not rational to support individual faulted MG by involving all the MGs into coordina-
tion considering the network scalability, efﬁciency, and economic reasons. Establishing
coordination groups between faulted MGs and its neighbors tackles the previous prob-
lems. The direct communication link and electrical connection help reduce power losses
on lines and communication time. Especially, it eliminates the impacts of the network
expansion to the complexity of coordination control.
4.6.1.2/
PROBLEM FORMULATION
Under the framework of neighboring coordination, the power is distributed for economic
beneﬁt while maintaining the power balance within the network and respecting facility
limitations. For simpliﬁcation objectives, assistant MGs sell energy to the faulted MGs
based on the assumptions in the following:
1) The electricity price of assistant MG is approximated as the generation cost of the
microturbine, which simpliﬁes the economic problem to concentrate on the pro-
posed control strategy. Due to the small inertia and fast ramping up/down output,
the battery is used to supply the local load and compensate for the internal intermit-
tent generation. The micro turbine takes charge of assisting neighboring MGs.
2) The MG privacy is not considered in this method. The operation information of each
assistant MG, including costs, is public to faulted MGs by agents’ interaction.
The problem formulation for optimization is shown in equations ( 4.23) to ( 4.27). The
economic optimization of coordination is represented in equation ( 4.23), where the cost
on each neighboring MG is simpliﬁed and shown in equation ( 4.24). The left side of the
equation ( 4.25) shows the sum of MGs’ interaction power in the network. A positive value
means exporting power, while a negative value represents importing power. It should be


---

Page 83

---

68CHAPTER 4. MULTI-AGENT BASED COORDINATION WITH NEIGHBORING MICROGRID
equal to the total network line losses shown on the right. The power capacity of the
distribution line is demonstrated in equation ( 4.26). Equation ( 4.27) implies that the
sum of the power ﬂowing on all lines connecting to a certain MG should be within the
limitations of its capacity.
minµcoordination
cos t
= min
X
j∈Mi
µ j i
cos t
(4.23)
µ j i
cos t = ηj
1pj i
MG + ηj
2

pj i
MG
2
(4.24)
X
i∈T
pi
MG =
X
i∈T
X
j∈Mi
pi j
Lineri j
Line
(4.25)
pi j
Line ≤pi j
Line,cap
(4.26)
pi
min,cap ≤
X
j∈Mi
pi j
Line ≤pi
max,cap
(4.27)
where µcoordination
cos t
is the faulted MG cost on buying enough power from neighbors and
µ j i
cos t is the quantity that the faulted MG paying to the neighbor MG indexed of j. η j
1 and
η j
2 are the cost coefﬁcients for linear and quadratic items respectively. pj i
MG is the volume
of power sold from i-index MG to j-index MG. pi
MG is the power of i -index MG interacting
with network. pi j
Line are the power ﬂowing on the distribution line connecting j-index and
i-index MG with ri j
Line and pi j
Line,cap as the line’s resistance and capacity. T is the collection
of all the MGs in network. pi
min,cap and pi
max,cap are the power ﬂexibility of i-index MG.
4.6.1.3/
CONTROL STRATEGY
The MG under imbalance is called ”requester,” while ”responder” refers to the assistant
MGs receiving supporting requirements. The requester MG determines the power dis-
patching schedule for all its neighbors, including the supportive MGs and the bought en-
ergy quantity. Such a control architecture is based on the economic optimization demon-
strated in equation ( 4.23)-equation ( 4.24) solved by the requester agent. The neigh-
boring MGs hand in the electricity price and its maximal trading volume to the requester
to fulﬁll the power dispatch, which makes the requester a central controller in the coor-
dination group. The capacity of distribution lines limits the power ﬂow coupling with the
output of network MGs. It is mathematically analyzed in the following section of 4.6.1.4.2.
The calculation on power ﬂow globally demands the perception of the output power of all
the MG in-network whose method is introduced explicitly in 4.6.1.4.1. Thus the infor-
mation transferred between MGs includes the output power and capacity of connecting
distribution lines.
According to the previous essential processes, the coordination problem described in
equation ( 4.23) to equation ( 4.27) is solved based on the steps shown in ﬁgure 4.5.
The Newton-Raphson method [Abbasbandy, 2003], which is commonly used for solving
the optimization of quadratic problems, is adopted for deriving dispatching solution in


---

Page 84

---

4.6. CONTROL STRATEGY FOR MG COORDINATION
69
the system. A distributed PF calculation with a consensus theorem is utilized to avoid
line capacity violations. Results show the security of the schedule by comparing the line
capacity with power ﬂow. The procedure of the PF check will be discussed in detail in the
following section. If there is a secure solution, the scheduling process ﬁnishes, and the
next scheduling step within the MG is run. Otherwise, the schedule fails. If no feasible
plan is obtained, this means that some constraints cannot be met and that the stability
of the system cannot be ensured. To guarantee the secure operation of the grid, the
MG sheds load or curtails renewable power generation. Each responder assists one
requester for each coordination cycle. If it receives multiple requests at the same time, a
priority order is used. The demands of the most massive value are answered ﬁrst. Such
a procedure continues until the responder’s response capacity is reached. The requester
then implements the dispatch resulting from the new exchanges.
power 
command
Compute:
Power monitoring: 
PV, TW, Load etc.
N
Dispatch assistant 
power based on 
Newton-Raphson
Get power 
demand
Power 
balance?
Receive 
power 
request?
Y
N
Facility operation 
control 
Be a 
requester
Be a 
responder
Y
Send power
flexibility: 
Flow check with 
consensus theorem
Receive dispatch 
power plan
Flow  check with 
consensus theorem
N
Capacity 
violation?
Y
Modify 
dispatch
Facility 
operation 
control 
Facility operation 
control 
Flow  check with 
consensus theorem
Flow result
requester role
responder role
Other 
solution?
Y
Shedding 
load or 
generator
N
Choose the 
highest request
START
min,
i
cap
p
max,
i
cap
p
min,
i
cap
p
max,
i
cap
p
Figure 4.5: Centralized control strategy ﬂowchart.
Figure 4.6 shows an example of messages exchanged during the negotiation process


---

Page 85

---

70CHAPTER 4. MULTI-AGENT BASED COORDINATION WITH NEIGHBORING MICROGRID
between two neighboring agents (agent 3 of MG3 is a requester and agent 2 of MG2
is a responder), during the coordination. Based on the facility power forecasts, if MG3
is lacking power or has excess energy, it schedules supportive power demands with its
neighbors. Information on the ﬂexibility of the responder is sent to the requester for power
dispatching with the Newton Raphson method. Requester MG3 then sends to the cor-
responding exchange schedule to responder MG2.
Based on this, the power ﬂow is
calculated in each agent with the consensus theorem. Line capacity constraints are fur-
ther checked, and the results determine whether the schedule is feasible. If no restriction
is violated, the plan is implemented, and a new control cycle starts. Otherwise, the MG3
reduces the interaction power with the MGs which connect or locate nearest with the
overload lines, and the reduced assistant power will be compensated by other MGs of
lower generation cost.
agent3: agent
agent2: agent
1 : predict internal power request
2 : predict MG power flexibility
3 : ask for power flexibility
4 : power flexibility
5 : power dispatching
6 : send power dispatching schedule
7 : choose highest request for schedule
8 : network MG exchanging power
9 : network MG exchanging power
10 : power flow calculation and check the violation
11 : power flow calculation and check the violation
12 : send results
13 : send power commands
Figure 4.6: Coordinating interaction diagram.
4.6.1.4/
POWER FLOW ALGORITHM
4.6.1.4.1/
Consensus Algorithm for Distributed MAS
For distributed MG network,
power ﬂow during coordination is derived from the output of each MG, and it im-
pacts the security operation given the capacity of distribution lines.
A central power
ﬂow calculation is not adopted as a central controller is required and it should com-
municate with all the MGs in the network for global information collection.
It is a
communicational cost and could cause single-point failure.
Besides the information
congestion is in expectation when the network scale expands.
Thus a decentral-


---

Page 86

---

4.6. CONTROL STRATEGY FOR MG COORDINATION
71
ized approach is preferred, and it reduces the cost of communication.
The neigh-
boring communication topology restraints direct access to global output power.
The
consensus theorem emerges for distributed MAS perceiving global information in high
efﬁciency.
The term of ”Consensus” means to accomplish an agreement about a
set of interest according to all the agents’ status [Yu et al., 2012].
The consensus
algorithm (or protocol) deﬁnes interaction rule and is used for data exploration.
It
speciﬁes information exchange between agents and the neighbors in the network
[Yu et al., 2012]. Communication protocols based on it depict the interaction process to
exchange information between neighboring agents. It is widely applied to the distributed
systems including optimal consensus [Shi et al., 2012, Nedic et al., 2010], sampled-
data consensus [Qin et al., 2013, Qin et al., 2010, Wang et al., 2012], adaptive con-
sensus [Yu et al., 2012], second-order consensus [Qin et al., 2011a, Qin et al., 2011b,
Qin et al., 2012], consensus of generic linear agents [Qin et al., 2014, Yang et al., 2011],
and multiple-leader consensus [Peng et al., 2015].
For faster convergence and the
higher probability of getting optimum network information, the average consensus
theorem is adopted to underpin the communication protocol [Olfati-Saber et al., 2007,
Xu et al., 2011, Liu et al., 2016].
Global perception in each agent and the assigned MG is derived by message spreading
in neighbor interaction.
The collected information could include the volume of output
power from all the MGs and their voltage value. They could be used to evaluate the
power ﬂow security and even dispatching generation in a global view. Thus the discovery
algorithm for network information is represented by equation ( 4.28) to equation ( 4.32).
The average consensus algorithm adopted in this thesis develops the convergence speed
based on the neighboring information. It corrects the updated value in updating agent
iteratively by adding the average errors between it and the values stored in all the adjacent
agents. Equation ( 4.28) is the formulation of an MG updating global information based
on neighbor messages.
xt+1
i
= xt
i +
X
j∈Ni
aij

xt
j −xt
i

(4.28)
Xt+1 = (I + A) Xt = DXt
(4.29)
A =

−P
j∈N1
a1 j
· · ·
a1n
...
...
...
an1
· · ·
−P
j∈Nn
anj

(4.30)
Xk =
h
xk
1
· · ·
xk
i
· · ·
xk
n
iT
(4.31)
D =

1 −P
j∈N1
a1j
· · ·
a1n
...
...
...
an1
· · ·
1 −P
j∈Nn
anj

(4.32)


---

Page 87

---

72CHAPTER 4. MULTI-AGENT BASED COORDINATION WITH NEIGHBORING MICROGRID
aij =

1
P
Ni
1+P
Nj
1+ε
j ∈Ni
1 −P
N j
1
P
Ni
1+P
Nj
1
j = i
0
otherwise
(4.33)
Where x is the unknown data containing operation information from remote MG, and the
i points to the index of storage agent, which is also the updating agent. j and Ni repre-
sent the neighboring MG index and neighboring MGs collection to the MG indexed by i
respectively. t resembles the iteration step before convergence. aij is the adaptive cou-
pling gain of error between the data stored in j-index MG and i-index MG. The value is
constant, and it is derived from equation ( 4.33) under constant topology of communica-
tion. Based on equation ( 4.28), the complete system information is discovered by the
matrix calculation shown in equation ( 4.29), where I is the identity matrix, and the other
items are further deﬁned in equations equation ( 4.30) to equation ( 4.33). N1 and Nn
are the neighboring MG collection of 1-index MG and n-index MG respectively. n is the
scale of the MG network, corresponds to the total MG numbers. The value of adaptive
coupling gain for averaging errors determines the stability and adaptivity of the average
consensus algorithm. Thus it is represented ε is very small and could be neglected in a
large complex system.
Agents exchange their operation information with adjacent ones periodically and update
their perception to all the MGs after receiving messages from all neighbors. It helps
reduce single points of failure in the system, in the hope to reduce the impact of any
failure furthermore.
4.6.1.4.2/
Power Flow Calculation
As the MG network is located in the distribution
power system, the connecting lines are short and transmit power with a low voltage level.
Thus an improved DC power ﬂow that considers line resistance (instead of reactance) is
adopted. The loss on a line pi j
Line,loss is shown in equation ( 4.34) which is simpliﬁed and
added onto the value of load at the terminal MGs as shown in equation ( 4.34)-equation
( 4.36) [Hongfu et al., 2014].
pi j
Line,loss = (pi j
Line)2ri j
Line
(4.34)
pi
L,equ =
X
j=1, j∈Mi
pi j
Line,loss
2
(4.35)
pi
MG, mod = pi
MG −pi
L,equ
(4.36)
Where pi j
Line,loss is the power loss on lines connecting i-index MG and j-index MG. pi
L,equ is
the equivalent load of line loss for i-index MG. pi
MG, mod is the equivalent power inputting
into i-index MG considering the line loss.
The resulting improved formulation of DC power ﬂow is shown in equation ( 4.37)-equation
( 4.41) [Stott et al., 2009]:
δ = [δ1, δ2 · · · , δi, · · · , δn]T
(4.37)


---

Page 88

---

4.6. CONTROL STRATEGY FOR MG COORDINATION
73
B =

1 −
P
j=2, j∈Ni
b1 j
· · ·
b1n
...
...
...
bn1
· · ·
1 −
P
j=1, j∈Ni,j,n
bnj

(4.38)
−P = Bδ
(4.39)
pi j
Line = δi −δj
xi j
Line
(4.40)
P = [p1
MG,mod, p2
MG,mod · · · , pi
MG,mod, · · · , pn
MG,mod]T
(4.41)
Where δi is the voltage angle of i-index MG. xi j
Line is the impedance of line connecting
i-index MG and j-index MG.
4.6.2/
STRATEGY 2: BIDDING IN THE MARKET
4.6.2.1/
MOTIVATION
The models of MG generation cost and bidding strategy are simpliﬁed in the method of
section 4.6.1. The quadratic function of price could not reﬂect the generation cost with
multiple renewable generators and batteries. Additionally, even though its communication
is distributed, agents need to discover the complete network information, which is similar
to centralized control. Thus the model of system demands further complementing and a
fully decentralized method for MG coordination has not been proposed yet. In a smart grid
made of interconnected MG clusters, decentralized coordination among MGs could be
expected to enable MGs to rescue each other to mitigate the impacts of faults. Secondly,
it should enable MG clusters to reconﬁgure whenever relevant (e.g., by changing MG
connections). Finally, it must be easily extended to handle a large amount of MGs and
hence facilitate DER and local energy integration. Based on these principles, this method
has the following contributions:
1) A real-time decentralized coordination mechanism between MGs is built. It enables
the rescue of an MG by others, which also limits the impact of faults.
2) Market power dispatching is applied for dividing assistant power among neighbor
MGs to maximize the load supply, energy use, and the MG proﬁts from power trad-
ing. The bidding price and volume are determined by the MG control strategy using
a genetic algorithm. It aims to minimize the generation cost and carbon dioxide
emission, as well as ensure power balance. A more approximate bid model to the
MG generation cost is proposed to maximize the economic proﬁt for both sellers
and buyers.
3) A distributed method is proposed to calculate power ﬂow caused by electricity trad-
ing among MGs. Simulation results are compared with the line capacity to ensure
secure operation. It helps decrease the communication and calculation burden,
especially for large systems.


---

Page 89

---

74CHAPTER 4. MULTI-AGENT BASED COORDINATION WITH NEIGHBORING MICROGRID
4.6.2.2/
PROBLEM FORMULATION
Based on the neighboring coordination in section 4.6.1, the electricity market is adopted
to dispatch the power to solve economic optimization. The faulted MG buys energy from
sellers (i.e., neighbor MGs) of the lowest price to a higher price at the volume of maximal
output until the summation is equal to the demand quantity. Such an operation is depicted
by an example shown in ﬁgure 4.7 [Parhizi et al., 2016].
Volume
Demand of MG7
MG8
MG2
MG10
MG1
Price
Figure 4.7: An example of power trading in the network in ﬁgure 4.7.
Cost
Maximal 
input
Maximal 
output
Maximal 
cost
Maximal 
save
Output
Figure 4.8: The output-cost curve.
As a seller, the neighbor MG makes the bid of selling electricity based on the generation
cost, which is minimized by the internal control based on the problem formulation ( 4.15).
A price determination method more approximate to the generation cost of MG is shown in
( 4.42)- ( 4.48), which are based on the internal economic optimization coordination within
individual MG. It is assumed that the proﬁt is proportional to the cost with a constant ratio
parameter. Hence the expense boosted by the neighbor coordination based on MG in-
ternal balance control underpins the bid strategy of the assistant MGs. It means that the
per-unit cost is obtained by the increased cost dividing the corresponding trading power.
The resulted value is usually multiplied by an economic gain for making a proﬁt to get the
ﬁnal bid. However, the coordination-caused expense still cannot be formulated mathe-
matically by a single function of supportive power quantity considering the diverse facility,
coordination behaviors, and the previous operation status. It could be approximated to a
linear function, as shown in ﬁgure 4.8. The origin represents no assistant behavior, and


---

Page 90

---

4.6. CONTROL STRATEGY FOR MG COORDINATION
75
the terminate point for output resembles the upper limit of MG power ﬂexibility shown in
( 4.17). While for the supportive reaction of absorbing the power, the input-cost line is
determined by the origin and the lower limit of MG ﬂexibility. The cost in both kinds of
coordination is the increased volume or saved volume comparing with the expense un-
der self-balance. This approximation is equal to the real cost when the MG trades in the
maximal power volume. The equations deriving bids are shown in ( 4.42)- ( 4.50) similar
to the MG ﬂexibility.
Equation ( 4.42) shows the bid of MG under conditions of exporting and absorbing power.
The maximal and minimal generation cost corresponding to the upper and lower limit of
MG power ﬂexibility, respectively, are shown in ( 4.43) and ( 4.46). Equations ( 4.44)
and ( 4.45) depict the cost of microturbine and battery under maximal MG output by
maximizing their generation. On the other hand, the maximal MG input cost is derived by
shutting down the microturbine and maximizing the charging power of the battery, whose
expense corresponds to ( 4.47) and ( 4.48). The volume of maximal output and input
are shown in ( 4.49) and ( 4.50), where the input power is negative, and output power is
positive. Network power balance is maintained by the constraint of ( 4.51), which depicts
that the summation of all the MGs generation is 0.
πk =

ηk
s

µk
max −µk
sel f

/pk
max,out

pk
MG > 0

ηk
b

µk
sel f −µk
min

/pk
max,in

pk
MG ≤0

(4.42)
µmax =
X
i∈TMT

µi
MT,max

+
X
i∈TBat

µi
Bat,max

(4.43)
µMT,max = ηup down,MT
1 −st−1
MT
 + η1,MT pmax,MT + η2,MT p2
max,MT
(4.44)
µBat,max =
 
1
ηdisch,Bat
pmax disch arg e,Bat
!
πinv
2 · NBat
∆t
(4.45)
µmin =
X
i∈TMT

µi
MT,min

+
X
i∈TBat

µi
Bat,min

(4.46)
µMT,min = ηup down,MT
0 −st−1
MT

(4.47)
µBat,min =

ηch,Batβch,Batpmax ch arg e,Bat

πinv
2 · NBat
∆t
(4.48)
pmax,out =
P
i∈TWT

pi
out,WT

+ P
i∈TPV

pi
out,PV

+ P
i∈TMT

pi
MT,max

+ P
i∈TBat

pi
maxdischarge,Bat

−P
i∈TL

pi
L

(4.49)
pmax,in =
X
i∈TWT

pi
out,WT

+
X
i∈TPV

pi
out,PV

−
X
i∈TBat

pi
maxcharge,Bat

−
X
i∈TL

pi
L

(4.50)
X
pk
MG = 0
(4.51)


---

Page 91

---

76CHAPTER 4. MULTI-AGENT BASED COORDINATION WITH NEIGHBORING MICROGRID
Where k and i represent the index of MGs and internal elements. πk is the bid price of
assistant MG. ηk
s and ηk
b are the proﬁt gain of the seller. µk
max and µk
min are the generation
cost under the maximal volume of generation and load. µk
sel f is the minimal generation
cost to maintain internal balance. pk
max,out and pk
max,in are the maximal volume of output
and input power. µi
MT,max and µi
Bat,max are the generation cost of the micro turbine and
battery under MG maximal generation. TMT, TBat and TL are the collection of the micro
turbine, battery, and load within individual MG.
4.6.2.3/
CONTROL STRATEGY
In the coordination process, an MG can be a ”requester” or a ”responder” according to
different circumstances. The former one cannot maintain local power balance by itself
and therefore needs to be “rescued”, while the latter can provide power assistance to
requesters.
Get output/
input: PV, 
Load etc.
Be 
requester 
Power 
balance? Y
N
Receive
request?
Y
N
Be 
responder 
Optimal bidding 
bid
Coordination
run market 
pf check
Violate 
capacity?
modify
Y
N
Optimal operation 
Optimal operation 
power command
dispatch plan
pf check
Dispatch 
power
dispatch 
plan
pf check
pf result
Optimal operation 
requester role
responder role
Optimal operation 
Start
Figure 4.9: Market strategy ﬂowchart.


---

Page 92

---

4.6. CONTROL STRATEGY FOR MG COORDINATION
77
The other MGs operate to keep maintaining self-balance without power interaction with
the network. A ﬂowchart of the coordination mechanism is shown in ﬁgure 4.9. In normal
conditions, an MG agent controls its facilities to minimize costs according to ( 4.1)- ( 4.15).
An MG then becomes a requester if its power balance is not met and the neighboring MGs
accordingly act as power responders (if they can do so).
Coordination is based on a market established by the requester to trade power with re-
sponders for imbalance compensation. The bidding of the responder is determined by
( 4.42)- ( 4.45). The requester trades with the MG bidding the lowest price for buying
power, and the one with the highest price for selling electricity. The requester thus ﬁrstly
trades with the MG of the lowest price, as much as it needs. The MG of second-lowest
price trade if power is insufﬁcient. Procedures repeat until the imbalance is replenished.
Next, the network power ﬂow is calculated by the agents based on a distributed algorithm
(see section 4.6.2.4). The resulting line ﬂow is then compared with line capacity. If ca-
pacity violations are detected, the MGs which connect or locate nearest with the overﬂow
line should reduce their trading power and the lacking power is compensated by other
MGs of lower generation cost. As the MGs with the lowest prices have provided the
most power assistance, the neighboring MGs with higher prices have to compensate this
power decrease. Once the dispatching feasibility is veriﬁed, the coordination behavior is
implemented with ( 4.1)- ( 4.12) and ( 4.18)- ( 4.22), setting the MG trading power pi
MG
equal to the dispatching command determined in ( 4.51).
For a responder, it buys electricity from neighboring MGs when the supply is lower than
load, and it sells power to the neighbor MGs when there is surplus energy. The bidding
price of responders in the market is determined using ( 4.42). ηk
s is the ratio between
the selling price and the cost. The responders’ selling price is obtained by multiplying ηk
s
(higher than 1 to generate a proﬁt) to the per-unit expense under maximal output. The
difference in cost is divided by the difference of generation between the operation under
maximal output and the self-balance maintenance under minimum payment. The per-unit
expense under maximal output is thus equal to the quotient. Similarly, the responders’
buying price is obtained based on the cost and output power under operations of maximal
input and the self-balance service at minimum cost. Neighboring MGs send their elec-
tricity price and the maximal power volume they can trade to the requester. For trading in
the market, a requester buys from the responders with the lowest price. For guaranteeing
that assistant power is sufﬁcient, the proposed volume of trading power is set equal to
the MG’s maximum ﬂexibility. It represents the maximal power the MG can absorb and
output. Based on this, the corresponding MG cost can be calculated.
4.6.2.4/
POWER FLOW
As mentioned above, after a dispatching plan having been determined, the resulting
power ﬂow should be calculated to check for possible violations of line capacity val-
ues. Even though the power ﬂow calculation in section 4.6.1.4.1 does not rely on di-
rect communication with all the MGs, all the agent still needs the global output power
to calculate the network power ﬂow.
This method takes the computational sources
of the MGs outside of the coordination group.
Besides, the message content is in-
creasing as the network expands.
Therefore, based on the methods described in
[Mohammadi et al., 2014, Kersting, 2001], we improve an approximate distributed DC
power ﬂow calculation method. It only considers the line resistance (as lines connect-


---

Page 93

---

78CHAPTER 4. MULTI-AGENT BASED COORDINATION WITH NEIGHBORING MICROGRID
ing MGs may be short) and calculates the power ﬂow of agent-connected lines. Several
assumptions are made to decentralize the power ﬂow calculation:
1) The voltage amplitude in the network is equal to the standard per-unit as the reactive
power is not discussed in this thesis, and the power is decoupled for active power
study.
2) The difference of voltage phase between MGs ranges around a small value which
enables the linearization of the relationship between angle value and MG output
power.
Both assumptions are shown in ( 4.52). The resulting formulation of DC power ﬂow is
improved and shown in ( 4.53)-( 4.55) [Mohammadi et al., 2014]:
V ≈1;
sin θi j ≈θi j;
cos θi j ≈1
(4.52)
∆pi,t−1
MG = 0 = pi,t−1
MG −Vi X
j∈Ni
V j(gi j
Line cos θi j,t−1 + bi j
Line sin θi j,t−1)
(4.53)
∆pi,t−1
MG = 0 = pi,t−1
MG −
X
j∈Ni
(gi j
Line + bi j
Lineθi j,t−1)
(4.54)
θi,t = θi,t−1 −γ

∆pi,t−1
(4.55)
Where V and θ are the amplitude and phase difference of the MG voltage, which is as-
sumed to be uniﬁed and equal to the voltage at the grid connection point. ∆pMG is the
power error between actual and iterative MG output power. The latter is derived from the
voltage angle error. The angle error can be used to correct the voltage angle shown in
( 4.55), where γ is adopted to avoid the divergence of the angle. gi j
Line and bi j
Line are the
reactance and susceptance of distribution lines between MGs of i-index and j-index.
In ( 4.53), the ﬁrst item and second item on the right side are the MG exchange power and
the sum of power ﬂow on the lines which are connected to it. According to Kirchhoff’s cur-
rent law, they are equal to each other. As the voltage angle difference between MGs may
be considered negligible (see (4.15)), we obtain ( 4.54). Taking assumptions of ( 4.52)
into ( 4.53), we obtain ( 4.54). Within the network, the MG voltage angle is unknown, as it
is controlled by the active power command. The voltage angle of reference MG maintains
at zero, while the angle of others is initialized at zero. The power ﬂow on lines is ﬁnally
calculated by ( 4.56):
pi j
Line = gi j
Line + bi j
Line(θi −θ j)
(4.56)
The ﬂowchart of the distributed method is shown in ﬁgure 4.10. It is a speciﬁc instruction
for the module of power ﬂow veriﬁcation (“pf check”) in ﬁgure 4.9. The requester sends
the dispatching plan to responders, and the agents in the network start to calculate the
power ﬂow on the lines which are connected with it. The following communication mes-
sage only includes the sender’s voltage angle, which guarantees information privacy for
the MG and reduces the complexity of communication. With equations ( 4.55) to ( 4.56),
each agent calculates the voltage angle of its assigned MG and further the power ﬂow on
the connected lines with ( 4.56). The capacity-check results on all wires are sent back to


---

Page 94

---

4.7. SIMULATION RESULTS
79
the requester to evaluate the dispatching plan for further modiﬁcation, as shown in ﬁgure
4.9. The optimization is achieved by negotiation among MGs. Thus in this chapter, the
communication system is assumed to be reliable. The case of communication loss will
be further studied in the future.
agent3: requester
agent2: responder
1 : dispatch power
2 : power dispatch plan for MG2
3 : set initial voltage angle for MG3
4 : set initial voltage angle for MG2
5 : calculate voltage angel
6 : calculate voltage angel
7 : angle value of MG2
8 : angel value of MG3
9 : power flow calculation and check the violation
10 : power flow calculation and check the violation
11 : violated capacity
12 : violated capacity
Figure 4.10: Distributed power ﬂow algorithm ﬂowchart.
4.7/
SIMULATION RESULTS
The proposed control strategies are tested on the simulation system based on the plat-
form established in chapter 3. Corresponding performance is evaluated on several as-
pects through several cases. They include the effectiveness of control, economic proﬁt,
and the reliability of load supply. The effectiveness of coordination, shedding loads, cur-
tailed generation, and costs are derived from simulation to evaluate the performance of
the control.
4.7.1/
TEST MULTI-AGENT SYSTEM AND MICROGRID NETWORK
Tests are based on the system of a 13-node system shown in ﬁgure 4.1 and the 34-node
system according to the paper of [Mohammadi et al., 2014], which also deﬁnes the pa-
rameters of distribution lines. As the main grid occupies one node and the rest nodes
represent the location of MGs, the simulation systems contain 12 MGs and 33 MGs re-
spectively. The architecture of individual MGs is as shown in ﬁgure 3.2. Both networks
are radial and the MGs are connected like a tree structure. There is no common point


---

Page 95

---

80CHAPTER 4. MULTI-AGENT BASED COORDINATION WITH NEIGHBORING MICROGRID
connecting all of the MGs to present the distributed location. The 12-MG network is big
enough to contain a neighboring group and the MGs without participating in the coor-
dination. By comparing the control performance in the 12-MG network and the 33-MG
network, the system scalability under the proposed control strategy is studied. In the
simulation, the battery in MG3 is assumed to be disconnected in the whole day, e.g., for
maintenance. Consequently, the imbalance in MG3 includes excess PV generation from
8:00 to 16:00 and surplus load from 6:00 to 7:00. The proposed approaches are applied
to the simulation, and their performance is evaluated after the conﬁguration of networks.
The components of each MG are shown in table 4.1, where only photovoltaic generator,
battery, and microturbine are included. The facility parameters for operation referred to
in equations of ( 4.1) to ( 4.12) are summarized in tables 4.2 and 4.3. Load information
is adapted from the power consumption of an actual building at UBFC, and the proﬁle of
solar radiation is collected from the weather in Belfort, France.
Table 4.1: MG facility numbers in the 12-MG system.
MG
MG1
MG2
MG3
MG4
MG5
MG6
PV
5
5
5
5
5
5
Battery
15
15
0
10
15
10
MT
0
0
1
0
0
0
MG
MG7
MG8
MG9
MG10
MG11
MG12
PV
5
5
5
5
5
5
Battery
15
10
15
10
10
10
MT
0
0
0
0
0
0
Table 4.2: MGs facilities rated powers.
Facility
PV
Battery
MT
Pmax (kW)
8
10
5
Prated (kW)
7.5
9
4.2
Table 4.3: Other parameters.
ηch
ηdisch
wess,min (kWh)
ηk
s
0.95
0.95
466.8
1.2
wess,max (kWh)
γ
∆t (s)
ηk
b
2100.6
7.5
3.2
0.8
The generation cost deﬁned in partial centralized control for MGs is endowed with the
proﬁt parameters shown in table 4.4, where the quadratic function refers to the equation
( 4.24). Each neighbor MG sends the cost parameters in table
4.4 to the requester
and the total cost for buying electricity from responders is minimized for maximizing proﬁt
according to the equation ( 4.23).
This problem can then be solved by the Newton-
Raphson method to decide the trading power quantity from neighbors.
Another set of parameters for the economic model proposed for market bidding is shown
in table 4.5, where the operation cost and shut-down/start-up cost for the distributable
generators correspond to the equations of ( 4.43) to ( 4.48). The battery has a wide range
of output volume as it is limited by maximal charging and discharging. It is assumed
to be non-stop as the operation includes non-power interaction, and its cost on shut-


---

Page 96

---

4.7. SIMULATION RESULTS
81
Table 4.4: Electricity price parameters in each MG.
MG3
MG2
MG4
η j i
1 (kW)
1
3.5
6.3
η j i
2 (kW)
0.006
0.004
0.009
down/start-up is 0. The generation cost of the microturbine is supposed to be linear to
the output volume to simplify the solution to economic optimization. Table 4.5 shows the
cost parameters: operation and maintenance (short for OM), startup and shutdown (short
for UD).
Table 4.5: Cost parameters. OM: operation and maintenance, UD: startup and shutdown
[Moghaddam et al., 2011a].
Generator
ESS OM (cent EUR/kWh)
ESS UD (cent EUR)
Price
0.38
0
Generator
MT OM (cent EUR/kWh)
MT UD (cent EUR)
Price
η1,MT
η2,MT
0.96
0.457
0.10
4.7.2/
DISPATCHING ALGORITHM COMPARISONS
Two scenarios are considered to validate the effectiveness of the proposed partial coor-
dination strategy on promoting supply reliability and resilience. We use a selﬁsh, self-
sufﬁcient control strategy for the reference scenario, where MGs do not coordinate with
each other. If the demand and supply of an MG are not balanced, the MG sheds loads
with the lowest priority or curtails power generation to maintain power balance. While
in the scenario with coordination, the method proposed in this chapter is adopted and
evaluated.
For the reference scenario, internal control results of MG3 (which includes no storage)
are shown in ﬁgure 4.11. The blue line represents the photovoltaic generation. The red
curve shows the microturbine output. The operating power of batteries is depicted by the
green dash line, where the negative value means charging status and the positive value
means discharging status. The output of each component is shown in 4.11a, the lack
of power is shown in 4.11b. As there is no MG to absorb the surplus power or supply
overload, load and generation shedding are applied to maintain system stability.
With coordinated control, the network operates as a storage unit to compensate MG
power imbalances, as shown in ﬁgure 4.12. The power outputs of MG2, 3 and 4 are
shown in 4.12a. According to ﬁgure 4.12b, the sum of the power ﬂowing from MG2 and
MG4 to MG3 is equal to the value of the MG3 request. Other MGs do not participate in
the coordination, so their outputs are not shown. Coordination is thus achieved among
MGs.


---

Page 97

---

82CHAPTER 4. MULTI-AGENT BASED COORDINATION WITH NEIGHBORING MICROGRID
4.7.3/
GENERATION COST COMPARISON
To validate the economic proﬁt of the proposed market coordination approach, a central-
ized control strategy in [Wang et al., 2016a] is adopted as the reference strategy. All the
self-balanced MGs supply power to compensate for the insufﬁcient power in the network
and the trading power quantity is proportional to the MG ﬂexibility. The selling bids of all
the MGs are shown in ﬁgure 4.13a derived from equation ( 4.42). The prices of neigh-
bor MGs in the market are demonstrated in ﬁgure 4.13b. The neighbors of MG3, i.e.,
MG2 and MG4, provide the necessary power assistance by bidding competition. During
4:40–6:00, MG3 demands power assistance to the system. The power selling price is
determined by ( 4.42) to ( 4.50).
Power coordination results are shown in ﬁgure 4.14. Based on the price shown in ﬁgure
4.13, the proposed coordination strategy motivates MG3 to buy power from MG4, which
is shown in ﬁgure 4.14b. For the reference strategy from [Faria et al., 2011], the MGs
in the network output power as the power demands and the trading results are shown in
ﬁgure 4.14a. The resulting costs are shown in table 4.6 by multiplying the price and the
volume of trading power.
Table 4.6: Requester MG cost in EUR.
12-MG
33-MG
Market coordination
299.4
299.4
Centralized control
1055.86
1923.43
Numerical results are summarized in table 4.6, which compares the cost of the requester
MG controlled by the proposed coordination strategy (market coordination) and the refer-
ence strategy (centralized control) in the 12-MG and 33-MG systems. With the reference
coordination strategy, the requester MG pays 1055.86 EUR for assistance power, which
is signiﬁcantly larger than 299.4 EUR with the proposed distributed market mechanism.
The cost reduction is because the price of neighboring MG power is lower than the aver-
age rate of the system. Besides, the cost of facility startup or shutdown decreases when
the trading is among fewer MGs. As the number of MGs increases to 33 in the system,
the expense of the requester with the reference strategy increases promptly to 1923.43
EUR, which limits the coordination proﬁt and thus decreases the scalability of the method.
With the proposed distributed market strategy, the cost of the requester remains at 299.4
EUR. As the proﬁt of the requester MG is guaranteed, and thus the system scalability is
improved, the coordination control strategy is therefore proﬁtable and scalable.
4.7.4/
ROBUSTNESS TEST
The power supply reliability and quality under fault or emergency conditions reﬂect the
robustness of the control and impact the customer’s comfort directly. Thus the system
robustness could be evaluated through the volume of facility loss and customer comfort.
Numerical results are summarized in table 4.7, which includes the shed load (SL), the
curtailed generation (CG), the trading cost (TC) and the exchanged power (EG) with the
network, from the point-of-view of MG3. Results without (0) and with (1) coordination
(CO) are compared. Without coordination, MG3 sheds 11.77 kWh of load and 85.28 kWh
of generation over the day, as there is no power exchange possibility between MG3 and


---

Page 98

---

4.8. CONCLUSION
83
the network. The corresponding exchange cost is zero. For the control with coordination,
load shedding and curtailments are avoided. As neighbor MGs absorb the excess power
of MG3, MG3 can thus generate a proﬁt (i.e., a negative cost). The coordination between
MGs helps solve the power imbalance. It improves the system resilience and maximizes
the use of renewable energy. As the power demand from MG3 is satisﬁed by its local
resources and the other MGs, the coordination control strategy achieves its objective. A
further study on MG coordination with distributed MAS will focus on the comparison with
the centralized method, which is lacking ﬂexibility on MG scalability.
Table 4.7: Simulation results.
SL (kWh)
CG (kWh)
TC (EUR)
EG (kWh)
CO
0
1
0
1
0
1
0
1
MG3
11.77
0
85.28
0
0
-16.74
0
97.05
MG2
0
0
0
0
0
3.834
0
33.17
MG4
0
0
0
0
0
-20.57
0
61.97
4.8/
CONCLUSION
This chapter has adopted a concept of partial coordination within the network. Corre-
sponding control strategies are proposed for coordinating power ﬂows among MGs, so
that they can provide power support when necessary. One of these approaches com-
bines consensus, power ﬂow, and dispatching algorithms to achieve coordination of the
different agents. Preliminary results of simulations with an IEEE 13-node network show
that this strategy is feasible on MG coordination for emergency rescue, and can further im-
prove the overall resilience of the system. Another economic control strategy is proposed
for dispatching power among MGs to assist imbalanced MGs. The proposed approach
establishes the distributed market and applies the decentralized power ﬂow calculation to
coordinate the output of MGs. Comparisons of simulation results with a centralized control
show that the proposed approach maximizes the proﬁt of the MGs and helps to improve
the scalability of the system. Both approaches show that the coordination established
between faulted MG and its neighbors could promote the supply reliability and scalability
of the network based on the MAS. It increases power sources and loads for individual MG
to resist faults and maintains the optimal internal operation. Additionally, the partial co-
ordination group allows the algorithms of power dispatching for multiple objectives, such
as economic beneﬁts, environmental reasons, and so on. Simulation results and com-
parisons with the other control strategy have validated that the coordination strategies
could promote reliability of supply without the impacts of system expansion while gaining
economic beneﬁts.
Even though the coordination with neighboring MGs improves control scalability, the as-
sistant facility is limited compared with the one of the network scale. The cooperative
power dispatching could be more economical with a more massive amount of elements
if sources of less cost participate. For example, if the neighboring MGs could not sup-
ply sufﬁcient power to the faulted MG, load shedding is unavoidable. Whereas a larger
coordination area increases the transmission cost, variable number in the optimization
problem, and time delay from communication. Thus a control strategy gaining a compre-
hensively good performance in terms of efﬁciency and economic beneﬁts is demanding.


---

Page 99

---

84CHAPTER 4. MULTI-AGENT BASED COORDINATION WITH NEIGHBORING MICROGRID
The expansion of coordination groups is necessary, which will be studied in the next
chapter.


---

Page 100

---

4.8. CONCLUSION
85
23:00:00 02:00:00 05:00:00 08:00:00 11:00:00 14:00:00 17:00:0020:00:00
Time: /s
0
5
10
15
20
25
30
35
Output: /kW
PV
MT
BA
Load
(a) Local resources output.
23:00:00 02:00:00 05:00:00 08:00:00 11:00:00 14:00:00 17:00:0020:00:00
Time: /s
−20
−10
0
10
20
30
40
Output: /kW
(b) Power deﬁciency.
Figure 4.11: Bidding prices of the MGs.


---

Page 101

---

86CHAPTER 4. MULTI-AGENT BASED COORDINATION WITH NEIGHBORING MICROGRID
06:00:0007:00:0008:00:0009:00:0010:00:0011:00:0012:00:0013:00:0014:00:0015:00:00
Time: /s
−20
−10
0
10
20
30
40
Output: /kW
MG3
MG2
MG4
(a) MG coordinating power.
06:00:0007:00:0008:00:0009:00:0010:00:0011:00:0012:00:0013:00:0014:00:0015:00:00
time: /s
−25
−20
−15
−10
−5
0
5
10
15
power: /kW
L23
L34
L25
(b) Line power ﬂows.
Figure 4.12: Coordination results for MG3.


---

Page 102

---

4.8. CONCLUSION
87
04:40:00 04:50:00 05:00:00 05:10:00 05:20:00 05:30:00 05:40:00 05:50:00
Time: /s
−14
−12
−10
−8
−6
−4
−2
0
2
Output: /kW
grid
MG2
MG3
MG4
MG5
MG6
MG7
MG8
MG9
MG10
MG11
MG1
MG12
(a) Prices for all MGs.
04:40:00 04:50:00 05:00:00 05:10:00 05:20:00 05:30:00 05:40:00 05:50:00
Time: /s
0.025
0.030
0.035
0.040
0.045
Price: EUR cent/kWh
MG4
MG2
(b) Prices of neighboring MGs.
Figure 4.13: Bidding prices of the MGs.


---

Page 103

---

88CHAPTER 4. MULTI-AGENT BASED COORDINATION WITH NEIGHBORING MICROGRID
04:40:00 04:50:00 05:00:00 05:10:00 05:20:00 05:30:00 05:40:00 05:50:00
Time: /s
0.025
0.030
0.035
0.040
0.045
Price: EUR cent/kWh
grid
MG2
MG4
MG5
MG6
MG7
MG8
MG9
MG10
MG11
MG1
MG12
(a) Under centralized control.
04:40:00 04:50:00 05:00:00 05:10:00 05:20:00 05:30:00 05:40:00 05:50:00
Time: /s
−15
−10
−5
0
5
10
15
Power: /kW
MG3
MG4
MG2
(b) Under decentralized control.
Figure 4.14: Coordination power for MG3.


---

Page 104

---

5
MULTI-AGENT BASED COORDINATION
WITHIN SELECTED MICROGRID AREA
5.1/
DEMAND-SUPPLY BALANCE
FOR
THE ECONOMIC POWER
DISPATCHING IN NETWORK
In chapter 4, approaches for the coordination with neighboring MGs are proposed, which
increase the reliability of load supply and generation utilization in an economic way. Ad-
ditionally, such a partial cooperative area enables the scalability of the network by nego-
tiating merely with the directly connected MGs. However, each MG could provide a low
capacity to support load outside after supplying local ones. For the faulted MGs at the
terminal of the distribution network, the available assistant energy is even less. Besides,
more elements are existing outside the neighbors which could provide more candidate
dispatching options economically. On the other hand, more MGs bring more calculation
pressure to the computational entity and an increasement in the communication link. They
cause longer delays for reaction, which worsens the control efﬁciency or even disables it.
Thus the trade-off between practical achievement and optimization quality is presented
for the coordination area selection. To improve the performance of MG coordination in
terms of load demand, economic purpose, and emission concern, related problems are
listed as follows:
1) By what criteria to select the constituent MGs to consist of the coordination area.
As the composing MGs contributes to the coordination area according to the func-
tions and capacity of including elements and their share in this area, selecting MGs
should consider the individual characteristics and the impacts on the MG group.
Formulating both perspectives is necessary.
2) How to dispatch power within the coordination area to take full advantage of all the
participants. As the MGs are selected by estimating the combination features of all
the participated MGs, the power dispatching among MGs should be detailed to the
devices level. Related approaches for it relying on the MAS is required.
Based on the MAS and communication connection designed in section 4.4.2, this chap-
ter proposes a distributed control structure for MG network coordination based on MAS
to improve the supply reliability, resilience to the faults, scalability, and real-time economic
proﬁt. The power assistance is provided by the other MGs to compensate for the power
89


---

Page 105

---

90CHAPTER 5. MULTI-AGENT BASED COORDINATION WITHIN SELECTED MICROGRID AREA
imbalance within MG. The control structure contains a) selecting MGs to form a coordi-
nation area (CA), b) power dispatch among elements in CA. a) delimits an area in which
all the MGs provide power assistance to the faulted MG. It minimizes the participation
elements with sufﬁcient assistant power for compensating the imbalance, high proﬁt, and
low greenhouse gas emission. Based on the neighboring communication, the coordina-
tion cluster extends by adding new directly connected MGs iteratively in this chapter. A
decentralized evolutionary algorithm is applied based on MAS to accelerate the selection
speed. Power dispatching is achieved in CA by controlling internal elements literally. The
optimization objective is to minimize generation costs in real-time. The renewable gener-
ation possesses the operation priority to reduce carbon emission. The microturbines and
energy storage systems are thus controlled to compensate for the power imbalance. The
performance of the proposed approach is tested on the simulation of systems consisting
of 13 MGs and 34 MGs correspondingly.
5.2/
HOLONIC MAS
The holonic MAS represents a hierarchical structure that the agent at a higher level is
composed of multiple agents at a lower level [Rodriguez et al., 2006]. In the MG network,
the components in the lowest layer of holon are the electrical elements. They form the
second holon of MGs, which further aggregate to establish the coordination group. The
top layer of a holon is in charge of distributing power among elements to eliminate the
imbalance in the faulted MG. Such construction allows the ﬂexibility of coordination group
formation in the network. The three levels are thus deﬁned for distinguishing the respon-
sibilities and behavior management. They include social rules describing the interactions
among bottom facility, coordinating rules identifying the agreement between holons at
the same level, and individual rules stating actions generally undertaken in well-deﬁned
situations [Adam et al., 2000].
Coordinating neighboring MGs enlarges the involved facility and increases the power
ﬂexibility to enforce the reliability of individual MG. This method avoids the dependency
on global information and manages partial MGs during coordination. To further improve
the reliability of load supply and ﬁnd more economic power dispatching alternatives, the
coordination group expands by rejoining more MGs. To optimize the economic power
dispatching, the control within CA ignores the blocks of MG and coordinates all the in-
ternal elements in an all-in-one formulation to reduce the generation cost. This problem
is solved centrally by the agent assigned to the faulted MG. Comparing with the coordi-
nation which treats the MG as an integrated entity with an approximated feature for the
cluster of internal elements, this method considers the characteristics of all the elements
individually. The central controller sends the facility operating commands to the assistant
agents and they run the elements directly. When a coordination cycle ﬁnishes, the CA
is dismissed and all the MGs reunion to the optimization group in the next time step if
there is still a fault. Agents cooperate with initiative intension and authorize a common
controller for the CA dispatching. Such a hierarchical structure could be described by
holonic MAS.
Under the holonic structure, the coordination control is divided into two stages: MG se-
lection for the coordination area and power dispatching within this area. Considering the
large scale of the candidate CA options, the algorithm for CA optimization is solved by the
combinational calculation in all the network agents. Then the power dispatching in CA is


---

Page 106

---

5.3. CONTROL STRATEGY PROCESS OF PROPOSED STRATEGY
91
solved by a centralized method.
5.3/
CONTROL STRATEGY PROCESS OF PROPOSED STRATEGY
An example MG clustered system based on the IEEE 13-node network is shown in ﬁgure
5.1, which contains 13 MGs (MG1 replaces the grid in ﬁgure 4.1 to participate in the
coordination). An agent is assigned to each MG. The control framework is shown in
ﬁgure 5.2, where each agent controls the operation of the assigned components and
negotiates with neighbor agents. An MG can include distributed energy sources (DERs)
and loads. We study the DERs, including PV, WT, MT and battery. The MG studied in
this chapter is shown in ﬁgure 5.2 (adding WTs to complement the renewable sources of
ﬁgure 3.2 and the test MG in chapter 4).
MG
2
MG
3
MG
4
MG
5
MG
6
MG
7
MG
8
MG
9
MG
10
MG
11
MG
13
MG
1
MG
12
Figure 5.1: Studied 13-MG System.
For the coordination demand, it is assumed that agents can communicate with the neigh-
boring agent (i.e., the assigned MGs are connected physically) in the system. They com-
municate with each other to store the MG output characteristics in the network. These
features include ﬂexibility (i.e., the maximal output and input power of an MG), genera-
tion cost, and element numbers. These data are used for selecting CA. It will be further
described in section 5.3.2.
5.3.1/
COORDINATION PROCESS
Each agent collects the operation status of their components, including run/stop, load
value, and output power. Once the communication connection is established, the ap-
proach for power dispatching can be achieved based on the MAS. The optimization ob-
jectives include maximizing the proﬁt, minimizing calculation time with low emission in
case of faults. The control strategy is shown in ﬁgure 5.3. It represents the MG control
process with three operations under network faults: keeping self-control, demanding for
and providing assistant power.


---

Page 107

---

92CHAPTER 5. MULTI-AGENT BASED COORDINATION WITHIN SELECTED MICROGRID AREA
MG2
MG3
agent1
PV
BATTERY
MT
LOAD
MG1
agent2
agent3
MAS
WT
Figure 5.2: Part of the Communication Network for the Studied Network.
start
No
Yes
operation status 
of component
imbalance?
making demands 
to the network
receive component 
status in CA
send dispatching results 
to CA agents
optimal power dispatching 
in CA 
end
receive 
demand?
Yes
send componet 
stat to faulted MG
get characteristics 
of relevant MGs in 
data base
is in the  CA?
DEAP for CA
receive dispatching 
demand
Yes
internal 
optimization
component 
control
end
No
No
end
fault 
conduction
assistance 
conduction
self 
control 
Figure 5.3: The Control Strategy for Cooperation.


---

Page 108

---

5.3. CONTROL STRATEGY PROCESS OF PROPOSED STRATEGY
93
When the power imbalance happens in an MG, the assigned agent sends out power
demand to the network.
Other agents assigned to balanced MGs start to calculate
the optimal CA with the distributed evolutionary algorithm programming (DEAP) based
on the variables representing MG characteristics [Stypka et al., 2018]. The agent of the
database shares the stored information with each agent when the optimization algorithm
is achieved. The objective is to ﬁnd the optimal CA based on equation ( 5.6). The agent
evaluates the overall characteristics of the MG groups. With DEAP, every MG agent deals
with a subpopulation, and the derived optimal individuals migrate in a constant probability
among agents. Once CA is decided, the power dispatching is achieved within it. The
agent assigned to the faulted MG collects the internal element’s operation status from
selected agents, including running/stop status, output power, load value, and the corre-
sponding cost. Based on this, it behaves as the central controller of CA and the internal
MGs are reconﬁgured as a new grid. According to the collected information, the optimal
solution for the dispatching is sent to each coordination agent for operating elements. For
the MGs without participating coordination, they run the self-optimization control based
on ( 5.9) to ( 5.10), and it is solved by quadratic programming in Gurobi.
agent3: faulted MG
agent2: normal MG
agent5: normal MG
1 : detect imbalance
2 : power imbalance request and MG characteristics
3 : faulted MG and MG characteristic
4 : MG characteristics
5 : MG characteristics
6 : CA calculation
7 : CA calculation
8 : CA calculation
9 : best individual
10 : best individual
11 : best individual
12 : not in CA, self optimization
13 : in CA, elements information
14 : power dispatching in CA
15 : self control
16 : elements coordination commands in CA
17 : elements control
18 : elements control
Figure 5.4: The Communication Diagram for Cooperation.
The communication diagram is shown in ﬁgure 5.4. To calculate the CA, each agent gain
characteristics of other MGs by communicating with neighbor agents based on the aver-
age consensus algorithm introduced in paper [Wei et al., 2017]. A distributed evolutionary
algorithm is applied in agents, and the best individuals are transferred between agents
to get a globally optimal solution. Once the CA is determined, the internal agents com-
municate for sending elements information to agent3 to solve the optimization problem
in equation ( 5.9) and control the operation of components according to the dispatching


---

Page 109

---

94CHAPTER 5. MULTI-AGENT BASED COORDINATION WITHIN SELECTED MICROGRID AREA
solution. Simultaneously the MGs outside of CA operate for internal balance.
5.3.2/
COORDINATING MICROGRID SELECTION
MG selection aims at establishing a CA, where all the elements participate in the power
dispatching process to maintain balance. All the agents in CA upload operation informa-
tion of the assigned elements to the faulted agent. The agents which do not participate
in it quit negotiating with others to keep the information privacy of the elements in CA.
Thus agents between faulted MG and the edge MGs of CA should be included in the
coordination area. This construction could prevent them from quitting information ex-
change and stop the information collection for power dispatching. Power coordination
among CA can expand the collaboration components to ensure sufﬁcient power supply. It
also provides a faster and proﬁtable solution for power dispatching with importing gener-
ators and storage elements. The power dispatching is optimized in CA than in single MG
[Nunna et al., 2013]. Additionally, it improves the network scalability by solving the power
dispatching under fault in part of the network rather than in the network and isolate the
fault in CA. The main objective in the ﬁrst step is to determine the coordination area pos-
sessing minimal generation cost, fast control speed and high use of renewable source.
For the group, the formulations, which could approximately reﬂect the relationships be-
tween elements and the optimization objectives, are as follows:
rCA
MT =
P
i∈TCA
MT
pi
MT,max
P
i∈TCA
WT
pi
out,WT + P
i∈TCA
PV
pi
out,PV + P
i∈TCA
MT
pi
MT,max + P
i∈TCA
Bat
pi
maxdisch arg e,Bat
(5.1)
cCA
average =
P
k∈CA
µk
max
P
i∈TCA
WT
pi
out,WT + P
i∈TCA
PV
pi
out,PV + P
i∈TCA
MT
pi
MT,max + P
i∈TCA
Bat
pi
maxdisch arg e,Bat
(5.2)
cfault
average =
µ fault
max
P
i∈TCA
WT
pi
out,WT + P
i∈TCA
PV
pi
out,PV + P
i∈TCA
MT
pi
MT,max + P
i∈TCA
Bat
pi
maxdisch arg e,Bat
(5.3)
rCA
cos t =
cCA
average
cfault
average
(5.4)
rCA
speed = 2(NCA
MT +NCA
Bat)
2(NNet
MT +NNet
Bat )
(5.5)
Where the TCA
WT, TCA
PV , TCA
MT, TCA
Bat are the collections of wind turbine, photovoltaic generator,
micro turbine and battery within CA. NCA
MT, NCA
Bat are the numbers of micro turbine and
battery within CA. NNet
MT, NNet
Bat are the numbers of micro turbine and battery in network.
Formulation ( 5.1) is the ratio of fossil fuel energy to the total energy in CA. The power
value corresponds to the maximal output of each power source. Formulation ( 5.2) is the
average cost per unit generation under maximal output and ( 5.3) is the average cost per
unit generation in faulted MG. Because renewable generators rely on renewable energy,


---

Page 110

---

5.3. CONTROL STRATEGY PROCESS OF PROPOSED STRATEGY
95
such as solar and wind, there is no marginal cost. Their start-up and the shut-down cost
is zero due to electrical converters. ( 5.4) is applied to evaluate the generation cost per
unit of power in CA at each time step. The CA, with a lower value, represents that the gen-
eration cost is more proﬁtable. The calculation time is represented in ( 5.5). It inﬂuences
the time needed to solve the optimal power dispatching problem in CA as the output and
operation status (running or stop) of battery and MT are the command variables. Power
dispatching applied a genetic algorithm in which the gene corresponds to the operation
status of MT. There are combinations. Thus reducing the number of combinations can
reduce the searching population of GA and calculation time. This algorithm will be intro-
duced in section 5.3. The optimization formulation in the ﬁrst step is shown in ( 5.6) with
the constraints in ( 5.7) and ( 5.8):
ε = min(ηCA
1 rCA
MT + ηCA
2 rCA
cos t + ηCA
3 rCA
speed)
(5.6)
s.t.:
ηCA
1
+ ηCA
2
+ ηCA
3
= 1
(5.7)
X
i∈TCA
WT
pi
out,WT +
X
i∈TCA
PV
pi
out,PV +
X
i∈TCA
MT
pi
MT,max +
X
i∈TCA
Bat
pi
maxdisch arg e,Bat ≥
X
i∈TCA
L
pi
L
(5.8)
ηCA
1 , ηCA
2 , ηCA
3
are the weights of each optimization objective correspondingly as shown in
( 5.6) with the values of 0.2, 0.5, 0.3 relatively. Their values are determined according to
the priority of the objectives. As the economic power dispatching is the objective for the
optimization in the second-stage, it weighs most. The calculation speed comes second
because the MG number impacts the scale of the collecting information in the next stage.
The share of renewable energy is ranked at last as the intermittent generation cannot
comply with the load requirement and the dispatchable resource is necessary for main-
taining power balance. Constraint ( 5.8) demonstrates that the sources in CA must supply
enough power to the load so that the imbalance caused by fault can be compensated.
5.3.3/
POWER DISPATCHING
After the CA is determined, the power dispatching in the area is achieved by the agent of
faulted MG. Equation ( 5.5) has a constant value in a certain CA. Renewable generation
is the prime source to reduce emission and cost, while MT and batteries operate as
auxiliary sources to keep power balance as their stable and controllable output. Thus
during the second step of coordination, the control objective is to minimize simply the
generation cost by dispatching power among distributable sources. The formulation is
shown in ( 5.9) with the constraint in ( 5.10):
µCA = min(µCA
MT + µCA
Bat)
(5.9)
s.t.:
X
i∈TCA
WT
pi
out,WT +
X
i∈TCA
PV
pi
out,PV +
X
i∈TCA
MT
pi
out,MT +
X
i∈TCA
Bat
pi
disch,Bat =
X
i∈TCA
L
pi
L +
X
i∈TCA
Bat
pi
ch,Bat
(5.10)


---

Page 111

---

96CHAPTER 5. MULTI-AGENT BASED COORDINATION WITHIN SELECTED MICROGRID AREA
Equation ( 5.9) presents the optimization formulation, which is to minimize generation
cost in CA. The ﬁrst and second items are the costs of all the microturbine and bat-
tery in CA. As the main concern of the battery system is the aging depending on fully
charging/discharging cycles, the operation cost model is implemented as equation ( 4.12)
shown in [Mutoh et al., 2006].
As for the generation cost model of microturbine, it is
shown in equation ( 4.7). Equation ( 5.10) is the power balance constraints in CA. The
facility constraints ( 4.1) to ( 4.11) in chapter 4 are also included in the constraints for the
optimization. As the sufﬁcient supply is guaranteed in constraint ( 5.8) belonging to the
previous stage (i.e., CA determination), the power balance is maintained by the power
dispatching among distributable sources. This is similar to the MG internal optimization
under normal conditions. The difference between both methods is the operation proce-
dure: the dispatching decision is made by the central controller (i.e., agent of faulted MG)
and operated by the local agent in CA, while the optimization is solved and achieved all
by the assigned agent in individual MG.
5.3.4/
DISTRIBUTED
EVOLUTIONARY
ALGORITHMS
WITH
DEPTH-FIRST
SEARCH (DFS)
As the scale of CA expands, and the elements involving in the coordination increase
abundantly, the calculation pressure resulting from optimizing power dispatching is the
main challenge for centralized control.
The distributed MAS relies on communica-
tion to chase global goals, which is incompatible with the central controller given the
single-point failure. Thus a decentralized control method is crucial in reducing the cal-
culation complexity and fulﬁlling the advantages of distributed agents of high intelli-
gence and automation.
With multiple agents existing in the system, DEAP in paper
[Stypka et al., 2018] is adopted to reduce calculation pressure and further improve the
network scalability. Decentralized optimization among multi-agent system reduces the
expensive cost on the computation of large population and the distributed machine is
fully used [Sarma et al., 1998, Starkweather et al., 1990, Cant´u-Paz, 1998]. Additionally,
the limitation on communication and perception to the changing operation of elements is
minimized [Stypka et al., 2018, Cant´u-Paz, 1998, Arpaia et al., 2014, Agah et al., 1996].
For solving problem ( 5.6) to get CA, DEAP is achieved in system agents synchronically
and each agent optimizes the subpopulation in which every individual corresponds to an
area formed by connecting MGs. An agent generates subpopulation by assigning the
matching MG as an edge of the CA and involving the faulted MG. As ﬁgure 5.6 shows,
the population in network is shown in ( 5.11).
h
x
x
x
x
x
x
x
x
x
x
x
x
x
i
(5.11)
where ‘x’ is the gene value which could be 0 or 1, showing outside or inside CA. Its
position in the array corresponds to the MG with the same number. The individual is set
by assigning 0 or 1 to each x in ( 5.11). For agent 6 (controlling MG6), the subpopulation
is limited as ( 5.12):
h
x
1
1
x
1
1
x
x
x
x
x
x
x
i
(5.12)
Taking MG6 as the terminal of CA, the MGs between MG3 and MG6 should be involved
in CA according to section 4.1. Thus the items corresponding to MG2 and MG5 are as-


---

Page 112

---

5.4. SIMULATION RESULTS
97
signed to 1. The individual is set by assigning values to the left ‘x,’ whose value represents
whether the assigned MG joins the coordination group.
The CA selection is based on the electrical connection. Thus there should be a mathe-
matical formulation to represent the network construction. Agents must identify a potential
CA. The DFS is therefore adopted to describe the radial network due to its fast speed in
discovering the shortest routine to the faulted MG. As the CA is shaped by the edge MG
and faulted MG, the mediate MGs between them are searched by DFS. Starting from an
arbitrary MG, it explores the network as far as possible along each branch in the system
before backtracking. Based on the graph theory, the network is transferred into a tree
with distribution lines as paths, and the vertices are the points where the MGs access to
the system. The MGs between edges and faulted MG are found by searching their lowest
common ancestor [Korf, 1985].
5.4/
SIMULATION RESULTS
Table 5.1: MG elements parameters in 13-MG system.
MG
MG1
MG2
MG3
MG4
MG5
MG6
MG7
PV (cases 1-2)
5
5
5
5
5
5
5
WT (cases 1-2)
5
5
5
5
5
5
5
Battery (cases 1-2)
10
15
0
10
15
10
15
MT (case 1)
0
0
1
0
0
0
0
MT (case 2)
2
2
1
3
1
1
1
CMT (EUR/kW)
0.4562
0.4569
0.4576
0.4583
0.4590
0.4597
0.4604
MG
MG8
MG9
MG10
MG11
MG12
MG13
PV (cases 1-2)
5
5
5
5
5
5
WT (cases 1-2)
5
5
5
5
5
5
Battery (cases 1-2)
10
15
10
10
10
10
MT (case 1)
0
0
0
0
0
0
MT (case 2)
2
2
1
1
1
2
CMT (EUR/kW)
0.4611
0.4618
0.4625
0.4632
0.4639
0.4646
The proposed approach is tested on 13-MG and 34-MG systems. 13-MG system is shown
in ﬁgure 4.1 [Dufo-Lopez et al., 2007]. The corresponding facility simulation parameters
are summarized in table 5.1 to table 5.3. Python 2.7 is the simulation platform, and it is
installed on a desktop under Microsoft Windows 10. The processor is Intel Core i7-4770
3.4GHz 8GB RAM. Load information is adapted from the power consumption of an actual
building at UBFC in Belfort, France. The simulation for 24 hours is performed, and the fault
happens during 6:25 to 7:25 a.m. to MG3. Its battery suffers an outage and ﬁgure 5.5a
shows the generation curves under maximal output for each generator, as well as load
curve. The total supply within MG3 cannot meet the load demand, and the corresponding
lack of power is shown in ﬁgure 5.5b. Negative values mean the insufﬁciency of power.


---

Page 113

---

98CHAPTER 5. MULTI-AGENT BASED COORDINATION WITHIN SELECTED MICROGRID AREA
(a) Elements operation status
(b) Deﬁcient power of MG3
Figure 5.5: Facility operation status in MG3.
To evaluate the proposed approach, we compare it with centralized control, a market


---

Page 114

---

5.4. SIMULATION RESULTS
99
Table 5.2: Rated power of elements.
Power
PV
Battery
WT
MT
Pmax (kW)
8
10
10
5
Pmin (kW)
0
-10
0
0.5
method, and quadratic programming in Gurobi in 3 cases.
Case 1 and case 2 both
are tested on a 13-MG system.
Case 3 is tested on a 34-MG network.
Faults in 3
cases happen on MG3 as shown in ﬁgure 4.1 and ﬁgure 5.13. For simply testing the
efﬁciency of the proposed approach in case 1, only one MT is involved in MG3 as the
single dispatchable sources. The other MGs do not include the MT. In case 2, all the
MGs include more than one MTs, which is used to show the impacts of the increasing
number of MT on the coordination control. The results demonstrate that the generation
cost and calculation time of dispatching algorithms are also inﬂuenced. In case 3, the
MT is involved in each MG, and the network is expanded to 34 MGs to test the scalability
of the proposed approach by comparing it with the other 2 cases. The summary of the
results in 3 cases is shown in table 5.4.
Table 5.3: Other element parameters.
ηCA
1
ηCA
2
ηCA
3
Vess,max
0.3
0.3
4
466.8 kWh
πinv
βb
Nbat
δMT
470 EUR/kWh
0.95
2000
0.96 EUR
Vess,min
∆t
Oess,cost
2100.6 kWh
1 s
0.38 EUR/kW
5.4.1/
CASE 1
MG
2
MG
3
MG
4
MG
5
MG
6
MG
7
MG
9
MG
10
MG
11
MG
13
MG
12
MG
1
MG
8
Figure 5.6: Coordination Group Formed in Proposed Approach.


---

Page 115

---

100CHAPTER 5. MULTI-AGENT BASED COORDINATION WITHIN SELECTED MICROGRID AREA
With the proposed approach, the CA formed at 6:58, and it includes 10 MGs in the blue
square, as shown in ﬁgure 5.6. The comparison algorithm is a centralized method for
power dispatching. An agent controls all the elements in the network based on the opti-
mization problem ( 5.9) to ( 5.11). A power dispatching in the market is applied as well. It
builds an electricity market for MG trading power in the network, where each MG bids its
maximal price. It is the average generation cost under the maximal output. The faulted
MG buys power from the MG with the lowest price iteratively until the imbalance is com-
pensated [Wei et al., 2018]. Results with different methods are shown in the following.
The red curve with a negative value in ﬁgures represents the output of MG3. Negative
value shows that an MG provides power to compensate for the imbalance.
Figure 5.7a shows the coordination result with the proposed strategy. Herein, the power
dispatching is solved by quadratic programming in Gurobi. The CA in this method con-
sists of part of the network. Figure 5.7b shows the power coordination results derived
from the centralized-controlled system. Then the trading results in the electricity market
for all the MGs are presented in 5.7c. The three methods are short for QP (quadratic
programming), CS (centralized strategy), and MK (market). Comparing the input power of
MG3 in three ﬁgures, the one in ﬁgure 5.7c is higher than the one in ﬁgure 5.7c by 5kW,
which is the maximal output of MT. The total load of MG3 shown in ﬁgure 5.5a is supplied
by the generation from coordination MG with QP and CS. While with MK, MG3 buys en-
ergy from the network to compensate for the internal insufﬁciency shown in ﬁgure 5.5b.
The ﬂuctuation of MG output power in ﬁgures 5.7a and 5.7c is caused by the change of
assistant MG. The renewable generation and the start-up/shut-down of MT change the
ε of each CA in equation ( 5.6), as well as the bidding price of each MG. Thus the con-
struction of optimal CA is dynamic and the participants are reselected at each step just
before the economical power dispatching. When the previous support MG is replaced by
a new one, their interaction power with the network has a ﬂuctuation. Similarly, the switch
of trading MG will also cause sharp ﬂuctuations in the new-in and new-out MGs.
The lines depicting generation cost under three approaches are shown in ﬁgure 5.9. As
the MGs consisting of low-cost generators are included in the CA, its expense has no
signiﬁcant difference with the one gotten from centralized control. They are lower than
the cost from the market at a maximum of near 6.25% from 7:10 to 7:20. The extra
payment is caused by the MT generation as it spends more than the battery per kW.
From the curve of MG3 input power shown in ﬁgure 5.7, in the market trading, the faulted
MG maximizes the internal generation to minimize the internal insufﬁciency. Then the
remaining demand-supply gap is compensated by trading with the network. MTs spend
more than batteries for per unit generation. In this case, MG3 includes one MT which will
operate during coordination under market trading, while it stops in the other two methods.
Thus the faulted MG costs more with the market method.


---

Page 116

---

5.4. SIMULATION RESULTS
101
(a) with QP.
(b) with CS.


---

Page 117

---

102CHAPTER 5. MULTI-AGENT BASED COORDINATION WITHIN SELECTED MICROGRID AREA
(c) with MK.
Figure 5.7: Power dispatching results among MGs in case 1.
Figure 5.8: Calculation time in case 1


---

Page 118

---

5.4. SIMULATION RESULTS
103
06:23:00 06:33:00 06:43:00 06:53:00 07:03:00 07:13:00 07:23:00 07:33:00
Time: /s
0
5000
10000
15000
20000
25000
30000
35000
Cost: euro
QP
CS
MK
Figure 5.9: Generation cost in network in case 1
5.4.2/
CASE 2
In this case, the performance of the proposed approach is tested on the system in ﬁgure
5.2. MGs consist of the components shown in table 5.1 to table 5.3. The faulted MG
stays the same with the one in case 1, while the MT number in balanced MGs increases,
and this inﬂuences the computation time and the quality of the results under different con-
trol methods. The coordination results are shown in ﬁgure 5.10. With more MT joining
into the coordination, the optimal power dispatching problem among MGs becomes more
complex as it increases quadratic terms in equation ( 5.9). The marginal generation cost
and on/off cost of MT are larger than the ones of battery. Thus the coordination between
elements, within the whole network, tends to select batteries as the supplier for the whole
load. The increase of MT causes no modiﬁcation on the coordination results with a cen-
tralized method comparing with ﬁgure 5.10b. As the MT number increases, it contributes
more to the CA characteristic than the other generation due to the larger capacity. Thus
the construction of CA is more stable. Therefore, the interaction power shown in 5.10a
for each MG has less ﬂuctuations than the ﬁgure 5.7a in case 1. Similarly, the bidding
price of the MG is more stable with more MTs. Thus the trading object maintains MG4
and the corresponding volume is shown in ﬁgure 5.10c.
Comparing the calculation time for power dispatch, CS spends the longest time at near
0.6s as the increasing MTs, while the market method has the fastest speed at around
0.05s. QP cost nearly 0.2s for each dispatching. As for the cost, it is similar to the one in
case 1 as the battery costs less than MT. Thus faulted MG is supplied by the batteries in
assistant MGs rather than operating local MTs. With MK, faulted MG operates its internal
MT to reduce the buying of electricity from assistant MGs. To sell enough power to MG3,


---

Page 119

---

104CHAPTER 5. MULTI-AGENT BASED COORDINATION WITHIN SELECTED MICROGRID AREA
MG4 with the lowest price operates internal MTs for generation, and this increases more
cost than the other two methods.
(a) with QP.
(b) with CS.


---

Page 120

---

5.4. SIMULATION RESULTS
105
(c) with MK.
Figure 5.10: Power dispatching results among MGs in case 2.
Figure 5.11: Calculation time in case 2


---

Page 121

---

106CHAPTER 5. MULTI-AGENT BASED COORDINATION WITHIN SELECTED MICROGRID AREA
06:23:00 06:33:00 06:43:00 06:53:00 07:03:00 07:13:00 07:23:00 07:33:00
Time: /s
0
5000
10000
15000
20000
25000
30000
35000
Cost: euro
QP
CS
MK
Figure 5.12: Generation cost in network in case 2
5.4.3/
CASE 3
The MG number increases in the network. Case 3 tests the control methods on a 34-
MG network shown in ﬁgure 5.13. Each MG consists of more than one MTs. Hence
the scalability of the proposed approach is studied. The constituent elements in MG3
maintain the same.
1
5
2
3
4
6
7
8
12
9
13
10
11
14
16
17
18
12
15
19
20
21
25
22
23
26
24
28
27
29
31
30
32
34
33
Figure 5.13: Electrical connection of the 34-MG network.
From ﬁgure 5.14, centralized control spends the longest time of around 1s to ﬁnish the
dispatching calculation for all the elements in the network. But the time cost by market
trading stays at the shortest time: 0.06s. The calculation with QP is around 0.2s. The time
increment is because of the expanding scale of the network and the increasing number


---

Page 122

---

5.4. SIMULATION RESULTS
107
06:23:00 06:33:00 06:43:00 06:53:00 07:03:00 07:13:00 07:23:00 07:33:00
Time: /s
0.0
0.2
0.4
0.6
0.8
1.0
1.2
Calculation time: s
QP
CS
MK
Figure 5.14: Calculation time in case 3
06:23:00 06:33:00 06:43:00 06:53:00 07:03:00 07:13:00 07:23:00 07:33:00
Time: /s
0
10000
20000
30000
40000
50000
60000
70000
80000
90000
Cost: euro
QP
CS
MK
Figure 5.15: Generation cost in network in case 3


---

Page 123

---

108CHAPTER 5. MULTI-AGENT BASED COORDINATION WITHIN SELECTED MICROGRID AREA
of coordination MTs. Regarding ﬁgure 5.15, the cost gotten from the market is more than
the one from QP and CS.
5.4.4/
IMPACT ON CALCULATION TIME AND COST
The results of cost and time in 3 cases are concluded in table 5.4. Comparing the time
gotten from 3 cases, MK has the least calculation time, and QP is in the middle. The
CS causes the longest delay is because it controls all elements in the network, while QP
is achieved among CA. MK selects several MGs for power trading, which is less than
the MGs in CA. Elements increment and network expansion have delayed the calculation
time indeed for CS and QP. However, with MK, the control time even falls from 0.0553 to
0.0539 from case 1 to case 3. As power is dispatched among MGs depending on their
bids and internal elements which are controlled by the assigned agents. The optimization
process is divided into multiple agents. Thus the decentralized algorithm reduces the
calculation time of MK and eliminates the impact of scale expansion to the computational
time. Summary of results shows that the calculation time with QP changes little by 14.09%
from case 1 to case 3. It is much less than the one with CS, which has a sharp increase
of 56.38%.
Table 5.4: Summary of calculation time and cost.
CS
MK
time(s)
cost(EUR/h)
time(s)
cost(EUR/h)
case 1
0.5796
27151.11
0.0490
27821.51
case 2
0.5523
27866.34
0.0553
28619.90
case 3
0.9064
67983.14
0.0539
72813.12
QP
time(s)
cost(EUR/h
case 1
0.1745
27174.26
case 2
0.1912
27888.49
case 3
0.1991
68017.18
The results are reasonable as the control elements of CS consist of all the devices in
34 MGs. On the other hand, the components controlled by QP are much less than the
CS. From the cost, it can be observed that the market spends more than the other three
methods. With market trading, elements are controlled by the assigned agent, and its
priority control is self-balance. The faulted agent maximizes the local generation to min-
imize the power buying from other MGs. Thus local MT costs more than the batteries
in other MG. For single MG, the power balance is the primary objective. Thus local MT
has a priority to the cheaper batteries in other MGs. The simulation shows that the QP
spends a much shorter time than CS to solve the power dispatching problem, and the
expansion of the system has a small inﬂuence on QP. Even though the market method
could cost less time, its cost is higher than QP in a relatively signiﬁcant difference. Thus
the quadratic programming with the proposed control strategy can gain a comprehensive
better performance on the scalability, proﬁt, and calculation time.


---

Page 124

---

5.5. CONCLUSION
109
5.5/
CONCLUSION
This chapter proposes a distributed control strategy based on MAS for power coordina-
tion in the MG network, especially when faults happen and break the balance within single
MG. It applies a distributed evolutionary algorithm to form a coordination area ﬁrstly and
then dispatching power among the internal elements with quadratic programming. Sim-
ulation results reveal that the scalability of the system is limited by the control strategy.
In return, the number of elements and MGs can inﬂuence control performance, including
generation cost and calculation time. A market method and a central strategy are applied
to the simulation to compare with the proposed control strategy, in which quadratic pro-
gramming is adopted for solving the power dispatching. Finally, the comparison results
show that the proposed control strategy with quadratic programming has a good com-
prehensive performance on the scalability, proﬁt, and calculation time. This coordination
strategy could be applied to the community consisting of smart houses.


---

Page 125

---



---

Page 126

---

III
CONCLUSION
111


---

Page 127

---



---

Page 128

---

6
CONCLUSIONS
6.1/
CONCLUSIONS ON THE PROPOSED APPROACH
In this dissertation, we focus on the coordination problem in the MG network to improve
the reliability of individual MG with an economic dispatching scheme. With the similarity
of functionally and physically distributed architecture, the MAS is applied to this system
to promote the automation of individual MGs and enable their interaction (section
3).
The plug-and-play feature enables the ﬂexible MG coalition for power interaction to com-
pensate for the individual insufﬁciency. Limited by the communication delay and compu-
tational pressure, the partial MG coordination is studied. We solve the power dispatch-
ing problems between faulted MG and its neighbors, which is to supply the unbalanced
MG economically. MG cooperative behaviors based on MAS are studied, including eco-
nomical optimization, the approximation of MG integrated features (section 4). For the
coordination within the extensive area, we also consider the practical limitation and the
scalability of control (section 5).
— First, for the coordination strategy with neighboring MGs, current approaches in-
clude MG reconﬁguration and maintaining MGs. Reviewing related researches in
maintaining MGs, the power dispatching approaches are widely solved by market
trading, bi-level strategy and droop control method. In this thesis, the market trading
and bi-level method are adopted for economical energy management.
— Then, for the security operation check in the network, the power ﬂow calculation
is necessary. The traditional method is the centralized iterative calculation. Based
on the communicational agents, a distributed power ﬂow calculation is proposed
by adopting an average consensus theorem. To reduce the message scale, a com-
plete distributed calculation method is presented, with only knowing the neighboring
voltage frequency.
— Finally, the coordination within the extensive area is studied.
We evaluated the
performance of both centralized and decentralized control in section 5.4. A combi-
nation of both structures is applied to solve this issue. A model for evaluating the
comprehensive performance of the integrated cooperative area is deﬁned. A dis-
tributed evolutionary algorithm programming is adopted to solve it in a decentralized
way. A centralized method is applied to solve the power dispatching problem in the
cooperative area.
113


---

Page 129

---

114
CHAPTER 6. CONCLUSIONS
6.2/
FUTURE WORK
Future work will focus on the proposed coordination approaches and their applications.
Considering the limited study in the past on the MG network and its complex construction
involving abundant elements, future research is diversiﬁed and of great interest.
The power ﬂow calculation considering both active and reactive power, as well as voltage
limitations, could be added into the problem formulation to improve the system accu-
racy. The coupling between reactive power and active power inﬂuences the line loss.
Additionally, the phase and amplitude of the system voltage are standardized. They are
determined by the power ﬂow in the network and within MG. Thus the formulation consid-
ering reactive power and voltage amplitude is required to make the system more accurate
and to increase the stability of system control.
The practical factors in this thesis include communication redundancy, time efﬁciency,
and the probability of communicational failure. They are all related to the communication
protocol, and the network scale should be more accurately modeled to represent the
impact on system performance. Speciﬁcally, these communication characteristics are
also impacted by the network scale, whose expansion hinders efﬁcient communication,
which further inﬂuences the control results.
The market bidding strategy could be more elastic to follow the output cost. As the output
cost is derived from the coordination within MG, and it determines the price bidding in
the market, the cost varies as the output changes. Thus the bidding strategy proposed in
this thesis approximates that the price is proportional to the average cost under maximal
output roughly. It is mainly the inaccuracy of price other than the maximal output point
that ﬂuctuates proﬁts and even causes beneﬁts loss. Thus penalty could be added to the
MG bidding strategy to adjust the price of MG without outputting the maximal volume of
power.
Adding distributable or shiftable load, such as electric vehicles and heater, to MG could
derive optimal coordination by shifting load. The distributable part leaves ﬂexibility to the
generation obeying the user habitat. Such load could also bring economic beneﬁts by
peak-shaving.
6.3/
SCIENTIFIC PRODUCTION REVIEW
The research in this thesis leads to multiple publications, as shown in the Appendix:
1) A control strategy is proposed for the MG network. Individual MG aims to operate in-
dependently in normal conditions, and several MGs can support each other in case
of contingencies or insufﬁcient generation. Such coordination aims at reducing load
shedding and generation curtailment and is achieved by coordinating the output
power of MGs. Each MG is equipped with an agent to achieve self-control and to
negotiate with other MGs, for example, to request power to its neighbors to support
its loads. The Newton-Raphson and consensus methods are used to calculate the
output power of each MG. The control strategy is validated using simulations on an
IEEE 13-node test feeder [Wei et al., 2017].
2) An agent-based decentralized coordination method is designed to improve the re-


---

Page 130

---

6.3. SCIENTIFIC PRODUCTION REVIEW
115
silience and ﬂexibility of larger systems. It means that healthy MGs help unhealthy
ones (e.g., in the case of insufﬁcient generation). Coordination is expected to elim-
inate the power imbalance inside MGs, thus limiting the impact for customers and
maximizing local production. Decentralized coordination is especially useful as the
resulting system is not subject to single points-of-failure. A distributed power ﬂow
calculation is used and enables verifying line capacity constraints to ensure the fea-
sibility of the power dispatch resulting from agent interaction. The performance of
the approach is tested on a system including 12 MGs and 33 MGs [Wei et al., 2018].


---

Page 131

---



---

Page 132

---

BIBLIOGRAPHY
[Abbasbandy, 2003] Abbasbandy, S. (2003). Improving newton–raphson method for
nonlinear equations by modiﬁed adomian decomposition method. Applied Math-
ematics and Computation, 145(2–3):887 – 893.
[Adam et al., 2000] Adam, E., Mandiau, R., et Kolski, C. (2000). Homascow: a holonic
multi-agent system for cooperative work. In Proceedings 11th International Work-
shop on Database and Expert Systems Applications, pages 247–253. IEEE.
[Aeronautics et al., 2019] Aeronautics, N., et (NASA), S. A. (2019). Giss surface tem-
perature analysis (v4). https://data.giss.nasa.gov/gistemp/graphs/. Accessed June 1,
2019.
[Agah et al., 1996] Agah, A., et Bekey, G. A. (1996). A genetic algorithm-based con-
troller for decentralized multi-agent robotic systems. In Proceedings of IEEE In-
ternational Conference on Evolutionary Computation, pages 431–436. IEEE.
[Andersson et al., 2005] Andersson, G., Donalek, P., Farmer, R., Hatziargyriou, N.,
Kamwa, I., Kundur, P., Martins, N., Paserba, J., Pourbeik, P., Sanchez-Gasca, J., et
others (2005). Causes of the 2003 major grid blackouts in north america and eu-
rope, and recommended means to improve system dynamic performance. IEEE
transactions on Power Systems, 20(4):1922–1928.
[Areﬁfar et al., 2012] Areﬁfar, S. A., Mohamed, Y. A.-R. I., et El-Fouly, T. H. (2012).
Supply-adequacy-based optimal construction of microgrids in smart distribution
systems. IEEE transactions on smart grid, 3(3):1491–1502.
[Areﬁfar et al., 2013a] Areﬁfar, S. A., Mohamed, Y. A.-R. I., et El-Fouly, T. H. (2013a).
Comprehensive operational planning framework for self-healing control actions
in smart distribution grids. IEEE Transactions on Power Systems, 28(4):4192–4200.
[Areﬁfar et al., 2013b] Areﬁfar, S. A., Yasser, A.-R. M., et El-Fouly, T. H. (2013b). Opti-
mum microgrid design for enhancing reliability and supply-security. IEEE Trans-
actions on Smart Grid, 4(3):1567–1575.
[Arpaia et al., 2014] Arpaia, P., Cimmino, P., Girone, M., Commara, G. L., Maisto, D.,
Manna, C., et Pezzetti, M. (2014). Decentralized diagnostics based on a distributed
micro-genetic algorithm for transducer networks monitoring large experimental
systems. Review of Scientiﬁc Instruments, 85(9):095103.
[Asimakopoulou et al., 2013] Asimakopoulou, G. E., Dimeas, A. L., et Hatziargyriou, N. D.
(2013). Leader-follower strategies for energy management of multi-microgrids.
IEEE Transactions on Smart Grid, 4(4):1909–1916.
[Baldick et al., 1999] Baldick, R., Kim, B. H., Chase, C., et Luo, Y. (1999). A fast dis-
tributed implementation of optimal power ﬂow. IEEE Transactions on Power Sys-
tems, 14(3):858–864.
117


---

Page 133

---

118
BIBLIOGRAPHY
[Bar-Yam, 2002] Bar-Yam, Y. (2002). General features of complex systems. Encyclo-
pedia of Life Support Systems (EOLSS), UNESCO, EOLSS Publishers, Oxford, UK,
1.
[Baziar et al., 2013] Baziar, A., et Kavousi-Fard, A. (2013). Considering uncertainty in
the optimal energy management of renewable micro-grids including storage de-
vices. Renewable Energy, 59:158–166.
[Bondi, 2000] Bondi, A. B. (2000). Characteristics of scalability and their impact on
performance.
In Proceedings of the 2nd international workshop on Software and
performance, pages 195–203.
[Booch, 2006] Booch, G. (2006). Object oriented analysis & design with application.
Pearson Education India.
[Borbely et al., 2001] Borbely, A.-M., et Kreider, J. F. (2001). Distributed generation: the
power paradigm for the new millennium. CRC press.
[Borshchev et al., 2004] Borshchev, A., et Filippov, A. (2004).
From system dynam-
ics and discrete event to practical agent based modeling: reasons, techniques,
tools. In Proceedings of the 22nd international conference of the system dynamics
society, volume 22. Citeseer.
[Cant´u-Paz, 1998] Cant´u-Paz, E. (1998). A survey of parallel genetic algorithms. Cal-
culateurs paralleles, reseaux et systems repartis, 10(2):141–171.
[Cavalcante et al., 2015] Cavalcante, P. L., L´opez, J. C., Franco, J. F., Rider, M. J., Garcia,
A. V., Malveira, M. R., Martins, L. L., et Direito, L. C. M. (2015). Centralized self-
healing scheme for electrical distribution systems. IEEE Transactions on Smart
Grid, 7(1):145–155.
[Che et al., 2013] Che, L., Khodayar, M., et Shahidehpour, M. (2013). Microgrids for
distribution system restoration. IEEE Power and Energy Mag., 2013.
[Chen et al., 2015] Chen, C., Wang, J., Qiu, F., et Zhao, D. (2015). Resilient distribu-
tion system by microgrids formation after natural disasters. IEEE Transactions on
smart grid, 7(2):958–966.
[Chen et al., 2016] Chen, J., et Garcia, H. E. (2016). Economic optimization of opera-
tions for hybrid energy systems under variable markets. Applied energy, 177:11–
24.
[Clarke et al., 1996] Clarke, E. M., et Wing, J. M. (1996). Formal methods: State of the
art and future directions. ACM Computing Surveys (CSUR), 28(4):626–643.
[Colson et al., 2011a] Colson, C., Nehrir, M., et Gunderson, R. (2011a).
Distributed
multi-agent microgrids: a decentralized approach to resilient power system self-
healing. In 2011 4th International Symposium on Resilient Control Systems, pages
83–88. IEEE.
[Colson et al., 2011b] Colson, C. M., et Nehrir, M. H. (2011b). Algorithms for distributed
decision-making for multi-agent microgrid power management.
In 2011 IEEE
Power and Energy Society General Meeting, pages 1–8. IEEE.


---

Page 134

---

BIBLIOGRAPHY
119
[Davis et al., 1983] Davis, R., et Smith, R. G. (1983). Negotiation as a metaphor for
distributed problem solving. Artiﬁcial intelligence, 20(1):63–109.
[Dickens, 2000] Dickens, C. (2000). A tale of two cities. Penguin.
[Ding et al., 2017] Ding, T., Lin, Y., Bie, Z., et Chen, C. (2017). A resilient microgrid for-
mation strategy for load restoration considering master-slave distributed gener-
ators and topology reconﬁguration. Applied energy, 199:205–216.
[Dong et al., 2014] Dong, D., Wang, P., Qin, W., et Han, X. (2014). Investigation of a
microgrid with vanadium redox ﬂow battery storages as a black start source for
power system restoration. In 2014 9th IEEE Conference on Industrial Electronics
and Applications, pages 140–145. IEEE.
[Duan et al., 2008] Duan, R., et Deconinck, G. (2008). Agent coordination for supply
and demand match in microgrids with auction mechanism. In 2008 First Inter-
national Conference on Infrastructure Systems and Services: Building Networks for a
Brighter Future (INFRA), pages 1–4. IEEE.
[Dubey et al., 2013] Dubey, S., Sarvaiya, J. N., et Seshadri, B. (2013). Temperature de-
pendent photovoltaic (pv) efﬁciency and its effect on pv production in the world–
a review. Energy Procedia, 33:311–321.
[Dudley et al., 2015] Dudley, B., et others (2015). Bp statistical review of world energy
2016. London, UK.
[Dufo-Lopez et al., 2007] Dufo-Lopez, R., Bernal-Agust´ın, J. L., et Contreras, J. (2007).
Optimization of control strategies for stand-alone renewable energy systems
with hydrogen storage. Renewable energy, 32(7):1102–1126.
[(EEA), 2019] (EEA), E. E. A. (2019).
Share of renewable energy in gross ﬁnal
energy consumption. https://ec.europa.eu/eurostat/tgm/table.do?tab=table&init=1&
language=en&pcode=t2020 31&plugin=1. Accessed June 14, 2019.
[Elkhatib et al., 2015] Elkhatib, M., Ahmed, M., Elshatshat, R., Salama, M., et Shaban,
K. B. (2015). Distribution system restoration based on cooperative multi-agent
approach. In 2015 International Symposium on Smart Electric Distribution Systems
and Technologies (EDST), pages 42–46. IEEE.
[Elmitwally et al., 2014] Elmitwally, A., Elsaid, M., Elgamal, M., et Chen, Z. (2014).
A
fuzzy-multiagent self-healing scheme for a distribution system with distributed
generations. IEEE Transactions on Power Systems, 30(5):2612–2622.
[Elsied et al., 2015] Elsied, M., Oukaour, A., Gualous, H., et Hassan, R. (2015). Energy
management and optimization in microgrid system based on green energy. En-
ergy, 84:139–151.
[Ephrati et al., 1995] Ephrati, E., Pollack, M. E., et Rosenschein, J. S. (1995). A tractable
heuristic that maximizes global utility through local plan combination. In ICMAS,
pages 94–101.
[Fang et al., 2019] Fang, X., et Yang, Q. (2019). Cooperative energy dispatch for mul-
tiple autonomous microgrids with distributed renewable sources and storages.
In Smart Power Distribution Systems, pages 127–160. Elsevier.


---

Page 135

---

120
BIBLIOGRAPHY
[Fang et al., 2016] Fang, X., Yang, Q., Wang, J., et Yan, W. (2016). Coordinated dis-
patch in multiple cooperative autonomous islanded microgrids. Applied energy,
162:40–48.
[Faria et al., 2011] Faria, P., et Vale, Z. (2011). Demand response in electrical energy
supply: An optimal real time pricing approach. Energy, 36(8):5374–5384.
[Fathi et al., 2013] Fathi, M., et Bevrani, H. (2013).
Adaptive energy consumption
scheduling for connected microgrids under demand uncertainty.
IEEE Trans-
actions on Power Delivery, 28(3):1576–1583.
[Ferber et al., 1999] Ferber, J., et Weiss, G. (1999). Multi-agent systems: an introduc-
tion to distributed artiﬁcial intelligence, volume 1. Addison-Wesley Reading.
[Fernandez et al., 2006] Fernandez, L. M., Saenz, J. R., et Jurado, F. (2006).
Dy-
namic models of wind farms with ﬁxed speed wind turbines. Renewable energy,
31(8):1203–1230.
[Gabbar et al., 2016] Gabbar, H. A., et Zidan, A. (2016). Optimal scheduling of inter-
connected micro energy grids with multiple fuel options.
Sustainable Energy,
Grids and Networks, 7:80–89.
[Genc et al., 2013] Genc, Z., Heidari, F., Oey, M. A., van Splunter, S., et Brazier, F. M.
(2013). Agent-based information infrastructure for disaster management. In In-
telligent systems for crisis management, pages 349–355. Springer.
[Ghorbani et al., 2014] Ghorbani, J., Choudhry, M. A., et Feliachi, A. (2014). A mas learn-
ing framework for power distribution system restoration. In 2014 IEEE PES T&D
Conference and Exposition, pages 1–6. IEEE.
[Ghorbani et al., 2015] Ghorbani, M. J., Choudhry, M. A., et Feliachi, A. (2015). A mul-
tiagent design for power distribution systems automation. IEEE Transactions on
Smart Grid, 7(1):329–339.
[Goyal et al., 2016] Goyal, M., et Ghosh, A. (2016). Microgrids interconnection to sup-
port mutually during any contingency. Sustainable Energy, Grids and Networks,
6:100–108.
[Guarnieri, 2013] Guarnieri, M. (2013). The beginning of electric energy transmission:
Part two [historical]. IEEE Industrial Electronics Magazine, 7(2):52–59.
[Hayden et al., 1999] Hayden, S. C., Carrick, C., et Yang, Q. (1999). A catalog of agent
coordination patterns. In Proceedings of the third annual conference on Autonomous
Agents, pages 412–413. ACM.
[Hongfu et al., 2014] Hongfu, W., Xianghong, T., Zhiqiang, Z., Chong, G., Hao, Y., et
Shixia, M. (2014). An improved dc power ﬂow algorithm with consideration of
network loss. In Power System Technology (POWERCON), 2014 International Con-
ference on, pages 455–460.
[Horling et al., 2004] Horling, B., et Lesser, V. (2004). A survey of multi-agent organi-
zational paradigms. The Knowledge engineering review, 19(4):281–316.


---

Page 136

---

BIBLIOGRAPHY
121
[Jimeno et al., 2011] Jimeno, J., Anduaga, J., Oyarzabal, J., et de Muro, A. G. (2011).
Architecture of a microgrid energy management system. European Transactions
on Electrical Power, 21(2):1142–1158.
[Kersting, 2001] Kersting, W. H. (2001).
Radial distribution test feeders.
In 2001
IEEE Power Engineering Society Winter Meeting. Conference Proceedings (Cat.
No.01CH37194), volume 2, pages 908–912 vol.2.
[Kim et al., 1997] Kim, B. H., et Baldick, R. (1997). Coarse-grained distributed optimal
power ﬂow. IEEE Transactions on Power Systems, 12(2):932–939.
[Kinny et al., 1996] Kinny, D., et Georgeff, M. (1996). Modelling and design of multi-
agent systems.
In International Workshop on Agent Theories, Architectures, and
Languages, pages 1–20. Springer.
[Koestler, 1967] Koestler, A. (1967). The ghost in the machine. 1990 reprint edition.
[Korf, 1985] Korf, R. E. (1985). Depth-ﬁrst iterative-deepening: An optimal admissi-
ble tree search. Artiﬁcial intelligence, 27(1):97–109.
[Kuznetsova et al., 2014] Kuznetsova, E., Li, Y.-F., Ruiz, C., et Zio, E. (2014). An inte-
grated framework of agent-based modelling and robust optimization for micro-
grid energy management. Applied Energy, 129:70–88.
[Lampropoulos et al., 2010] Lampropoulos, I., Vanalme, G. M., et Kling, W. L. (2010). A
methodology for modeling the behavior of electricity prosumers within the smart
grid. In 2010 IEEE PES Innovative Smart Grid Technologies Conference Europe (ISGT
Europe), pages 1–8. IEEE.
[Lasseter, 2011] Lasseter, R. H. (2011). Smart distribution: Coupled microgrids. Pro-
ceedings of the IEEE, 99(6):1074–1082.
[Le et al., 2008] Le, Q. B., Park, S. J., Vlek, P. L., et Cremers, A. B. (2008). Land-use
dynamic simulator (ludas): A multi-agent system model for simulating spatio-
temporal dynamics of coupled human–landscape system. i. structure and theo-
retical speciﬁcation. Ecological Informatics, 3(2):135–153.
[Li et al., 2010] Li, P., Song, B., Wang, W., et Wang, T. (2010). Multi-agent approach for
service restoration of microgrid. In Industrial Electronics and Applications (ICIEA),
2010 the 5th IEEE Conference on, pages 962–966. IEEE.
[Liu et al., 2016] Liu, Q., Fu, W., Qin, J., Zheng, W. X., et Gao, H. (2016). Distributed
k-means algorithm for sensor networks based on multi-agent consensus theory.
In 2016 IEEE International Conference on Industrial Technology (ICIT), pages 2114–
2119. IEEE.
[Liu et al., 2018] Liu, T., Tan, X., Sun, B., Wu, Y., et Tsang, D. H. (2018). Energy man-
agement of cooperative microgrids: A distributed optimization approach. Inter-
national Journal of Electrical Power & Energy Systems, 96:335–346.
[Logenthiran et al., 2011] Logenthiran, T., Srinivasan, D., et Khambadkone, A. M. (2011).
Multi-agent system for energy resource scheduling of integrated microgrids in a
distributed system. Electric Power Systems Research, 81(1):138–148.


---

Page 137

---

122
BIBLIOGRAPHY
[Logenthiran et al., 2008] Logenthiran, T., Srinivasan, D., et Wong, D. (2008). Multi-agent
coordination for der in microgrid. In 2008 IEEE International Conference on Sus-
tainable Energy Technologies, pages 77–82. IEEE.
[Luo et al., 2017] Luo, F., Chen, Y., Xu, Z., Liang, G., Zheng, Y., et Qiu, J. (2017).
Multiagent-based cooperative control framework for microgrids’ energy imbal-
ance. IEEE Transactions on Industrial Informatics, 13(3):1046–1056.
[Lv et al., 2016] Lv, T., et Ai, Q. (2016). Interactive energy management of networked
microgrids-based active distribution system considering large-scale integration
of renewable energy resources. Applied Energy, 163:408–422.
[Macal et al., 2005] Macal, C. M., et North, M. J. (2005). Tutorial on agent-based mod-
eling and simulation. In Proceedings of the Winter Simulation Conference, 2005.,
pages 14–pp. IEEE.
[Mahmoud et al., 2014] Mahmoud, M. S., Hussain, S. A., et Abido, M. A. (2014). Mod-
eling and control of microgrid: An overview.
Journal of the Franklin Institute,
351(5):2822–2859.
[Marnay et al., 2015] Marnay, C., Chatzivasileiadis, S., Abbey, C., Iravani, R., Joos, G.,
Lombardi, P., Mancarella, P., et von Appen, J. (2015). Microgrid evolution roadmap.
In 2015 international symposium on smart electric distribution systems and technolo-
gies (EDST), pages 139–144. IEEE.
[Mas-Colell et al., 1995] Mas-Colell, A., Whinston, M. D., Green, J. R., et others (1995).
Microeconomic theory, volume 1. Oxford university press New York.
[Maskin, 1983] Maskin, E. (1983). The theory of implementation in nash equilibrium:
A survey.
[Moghaddam et al., 2011a] Moghaddam, A. A., Seiﬁ, A., Niknam, T., et Pahlavani, M.
R. A. (2011a). Multi-objective operation management of a renewable mg (micro-
grid) with back-up micro-turbine/fuel cell/battery hybrid power source. Energy,
36(11):6490–6507.
[Moghaddam et al., 2011b] Moghaddam, M. P., Abdollahi, A., et Rashidinejad, M. (2011b).
Flexible demand response programs modeling in competitive electricity mar-
kets. Applied Energy, 88(9):3257–3269.
[Mohammadi et al., 2014] Mohammadi, J., Kar, S., et Hug, G. (2014). Distributed ap-
proach for dc optimal power ﬂow calculations. arXiv preprint arXiv:1410.4236.
[Mohsenian-Rad et al., 2010] Mohsenian-Rad, A.-H., et Leon-Garcia, A. (2010). Optimal
residential load control with price prediction in real-time electricity pricing envi-
ronments. IEEE Trans. Smart Grid, 1(2):120–133.
[Montgomery et al., 1993] Montgomery, T. A., et Durfee, E. H. (1993).
Search reduc-
tion in hierarchical distributed problem solving. Group Decision and Negotiation,
2(3):301–317.
[Morais et al., 2010] Morais, H., Kadar, P., Faria, P., Vale, Z. A., et Khodr, H. (2010). Op-
timal scheduling of a renewable micro-grid in an isolated load area using mixed-
integer linear programming. Renewable Energy, 35(1):151–156.


---

Page 138

---

BIBLIOGRAPHY
123
[Moreira et al., 2007] Moreira, C., Resende, F., et Lopes, J. P. (2007). Using low volt-
age microgrids for service restoration.
IEEE Transactions on Power Systems,
22(1):395–403.
[Mutoh et al., 2006] Mutoh, N., Ohno, M., et Inoue, T. (2006). A method for mppt con-
trol while searching for parameters corresponding to weather conditions for pv
generation systems. IEEE Transactions on industrial electronics, 53(4):1055–1065.
[Nedic et al., 2010] Nedic, A., Ozdaglar, A., et Parrilo, P. A. (2010). Constrained con-
sensus and optimization in multi-agent networks. IEEE Transactions on Automatic
Control, 55(4):922–938.
[Nikmehr et al., 2017] Nikmehr, N., Najaﬁ-Ravadanegh, S., et Khodaei, A. (2017). Proba-
bilistic optimal scheduling of networked microgrids considering time-based de-
mand response programs under uncertainty. Applied energy, 198:267–279.
[Nunna et al., 2013] Nunna, H. K., et Doolla, S. (2013). Multiagent-based distributed-
energy-resource management for intelligent microgrids.
IEEE Transactions on
Industrial Electronics, 60(4):1678–1687.
[Olfati-Saber et al., 2007] Olfati-Saber, R., Fax, J. A., et Murray, R. M. (2007). Consen-
sus and cooperation in networked multi-agent systems. Proceedings of the IEEE,
95(1):215–233.
[Orcutt, 1968] Orcutt, G. H. (1968). Research strategy in modeling economic sys-
tems. The future of statistics (Academic Press, New York), pages 71–95.
[Ormandjieva et al., 2015] Ormandjieva, O., Bentahar, J., Huang, J., et Kuang, H. (2015).
Modelling multi-agent systems with category theory. Procedia Computer Science,
52:538–545.
[Parhizi et al., 2015] Parhizi, S., et Khodaei, A. (2015). Market-based microgrid optimal
scheduling. In Smart Grid Communications (SmartGridComm), 2015 IEEE Interna-
tional Conference on, pages 55–60. IEEE.
[Parhizi et al., 2016] Parhizi, S., Khodaei, A., et Shahidehpour, M. (2016). Market-based
versus price-based microgrid optimal scheduling.
IEEE Transactions on Smart
Grid, 9(2):615–623.
[Peik-Herfeh et al., 2013] Peik-Herfeh, M., Seiﬁ, H., et Sheikh-El-Eslami, M. (2013). De-
cision making of a virtual power plant under uncertainties for bidding in a day-
ahead market using point estimate method. International Journal of Electrical Power
& Energy Systems, 44(1):88–98.
[Peng et al., 2015] Peng, Z., Wang, D., Shi, Y., Wang, H., et Wang, W. (2015). Contain-
ment control of networked autonomous underwater vehicles with model uncer-
tainty and ocean disturbances guided by multiple leaders. Information Sciences,
316:163–179.
[Petcu et al., 2005] Petcu, A., et Faltings, B. (2005). A scalable method for multiagent
constraint optimization. Technical Report.
[Pinto et al., 2011] Pinto, T., Morais, H., Oliveira, P., Vale, Z., Prac¸a, I., et Ramos, C.
(2011). A new approach for multi-agent coalition formation and management in
the scope of electricity markets. Energy, 36(8):5004–5015.


---

Page 139

---

124
BIBLIOGRAPHY
[Pipattanasomporn et al., 2009] Pipattanasomporn, M., Feroze, H., et Rahman, S. (2009).
Multi-agent systems in a distributed smart grid: Design and implementation. In
2009 IEEE/PES Power Systems Conference and Exposition, pages 1–8. IEEE.
[Qin et al., 2012] Qin, J., et Gao, H. (2012). A sufﬁcient condition for convergence
of sampled-data consensus for double-integrator dynamics with nonuniform
and time-varying communication delays. IEEE Transactions on Automatic Control,
57(9):2417–2422.
[Qin et al., 2014] Qin, J., Gao, H., et Zheng, W. X. (2014). Exponential synchroniza-
tion of complex networks of linear systems and nonlinear oscillators: A uniﬁed
analysis. IEEE transactions on neural networks and learning systems, 26(3):510–521.
[Qin et al., 2013] Qin, J., Yu, C., et Gao, H. (2013). Coordination for linear multiagent
systems with dynamic interaction topology in the leader-following framework.
IEEE Transactions on Industrial Electronics, 61(5):2412–2422.
[Qin et al., 2010] Qin, J., Zheng, W. X., et Gao, H. (2010). Sampled-data consensus for
multiple agents with discrete second-order dynamics. In 49th IEEE Conference on
Decision and Control (CDC), pages 1391–1396. IEEE.
[Qin et al., 2011a] Qin, J., Zheng, W. X., et Gao, H. (2011a). Consensus of multiple
second-order vehicles with a time-varying reference signal under directed topol-
ogy. Automatica, 47(9):1983–1991.
[Qin et al., 2011b] Qin, J., Zheng, W. X., et Gao, H. (2011b). Coordination of multiple
agents with double-integrator dynamics under generalized interaction topolo-
gies. IEEE Transactions on Systems, Man, and Cybernetics, Part B (Cybernetics),
42(1):44–57.
[Randall, 2011] Randall, A. (2011). Risk and precaution. Cambridge University Press.
[Ren et al., 2018] Ren, L., Qin, Y., Li, Y., Zhang, P., Wang, B., Luh, P. B., Han, S., Orekan,
T., et Gong, T. (2018). Enabling resilient distributed power sharing in networked
microgrids through software deﬁned networking. Applied Energy, 210:1251–1265.
[Roche, 2012] Roche, R. (2012). Agent-based architectures and algorithms for en-
ergy management in smart grids. PhD thesis, Ph. D. dissertation, Sciences Pour
l’Ing´enieur et Microtechniques, Institut . . . .
[Rodriguez et al., 2006] Rodriguez, S., Gaud, N., Hilaire, V., Galland, S., et Koukam, A.
(2006). An analysis and design concept for self-organization in holonic multi-
agent systems. In International Workshop on Engineering Self-Organising Applica-
tions, pages 15–27. Springer.
[Ross et al., 2011] Ross, M., Hidalgo, R., Abbey, C., et Jo´os, G. (2011). Energy storage
system scheduling for an isolated microgrid.
IET renewable power generation,
5(2):117–123.
[Russell et al., 2016] Russell, S. J., et Norvig, P. (2016). Artiﬁcial intelligence: a mod-
ern approach. Malaysia; Pearson Education Limited,.
[Saad et al., 2011] Saad, W., Han, Z., et Poor, H. V. (2011). Coalitional game theory
for cooperative micro-grid distribution networks. In Communications Workshops
(ICC), 2011 IEEE International Conference on, pages 1–5. IEEE.


---

Page 140

---

BIBLIOGRAPHY
125
[Sandholm et al., 1996] Sandholm, T. W., et Lesser, V. R. (1996). Negotiation among
self-interested computationally limited agents. PhD thesis, Citeseer.
[Sarma et al., 1998] Sarma, J. A., et Jong, K. A. (1998). An analysis of decentralized
and spatially distributed genetic algorithms. Citeseer.
[Sauer et al., 1998] Sauer, P. W., et Pai, M. A. (1998). Power system dynamics and
stability, volume 101. Prentice hall Upper Saddle River, NJ.
[Schurr et al., 2005] Schurr, N., Marecki, J., Tambe, M., Scerri, P., Kasinadhuni, N., et
Lewis, J. P. (2005). The future of disaster response: Humans working with multia-
gent teams using defacto. In AAAI spring symposium: AI technologies for homeland
security, pages 9–16.
[Shi et al., 2012] Shi, G., et Johansson, K. H. (2012). Randomized optimal consensus
of multi-agent systems. Automatica, 48(12):3018–3030.
[Simon, 1996] Simon, H. A. (1996). The sciences of the artiﬁcial. MIT press.
[Smil, 2016] Smil, V. (2016). Energy transitions: global and national perspectives.
ABC-CLIO.
[Solanki et al., 2007] Solanki, J. M., Khushalani, S., et Schulz, N. N. (2007). A multi-
agent solution to distribution systems restoration. IEEE Transactions on Power
systems, 22(3):1026–1034.
[Stankovic et al., 1985] Stankovic, J. A., Ramamritham, K., et Cheng, S. (1985). Evalu-
ation of a ﬂexible task scheduling algorithm for distributed hard real-time sys-
tems. IEEE Transactions on computers, 100(12):1130–1143.
[Starkweather et al., 1990] Starkweather, T., Whitley, D., et Mathias, K. (1990). Optimiza-
tion using distributed genetic algorithms. In International Conference on Parallel
Problem Solving from Nature, pages 176–185. Springer.
[Stott et al., 2009] Stott, B., Jardim, J., et Alsac, O. (2009). Dc power ﬂow revisited.
IEEE Transactions on Power Systems, 24(3):1290–1300.
[Stypka et al., 2018] Stypka, J., Turek, W., Byrski, A., Kisiel-Dorohinicki, M., Barwell, A. D.,
Brown, C., Hammond, K., et Janjic, V. (2018). The missing link! a new skeleton
for evolutionary multi-agent systems in erlang.
International Journal of Parallel
Programming, 46(1):4–22.
[Tian et al., 2015] Tian, P., Xiao, X., Wang, K., et Ding, R. (2015). A hierarchical energy
management system based on hierarchical optimization for microgrid commu-
nity economic operation. IEEE Transactions on Smart Grid, 7(5):2230–2241.
[Ton et al., 2012] Ton, D. T., et Smith, M. A. (2012). The us department of energy’s
microgrid initiative. The Electricity Journal, 25(8):84–94.
[Varga et al., 1994] Varga, L., Jennings, N. R., et Cockburn, D. (1994). Integrating intel-
ligent systems into a cooperating community for electricity distribution manage-
ment. Expert Systems with Applications, 7(4):563–579.
[Von Martial, 1992] Von Martial, F. (1992). Coordinating plans of autonomous agents,
volume 2. Springer.


---

Page 141

---

126
BIBLIOGRAPHY
[Wang et al., 2012] Wang, X., Liu, T., et Qin, J. (2012). Second-order consensus with
unknown dynamics via cyclic-small-gain method. IET Control Theory & Applica-
tions, 6(18):2748–2756.
[Wang et al., 2015a] Wang, Z., Chen, B., Wang, J., Begovic, M. M., et Chen, C. (2015a).
Coordinated energy management of networked microgrids in distribution sys-
tems. IEEE Transactions on Smart Grid, 6(1):45–53.
[Wang et al., 2016a] Wang, Z., Chen, B., Wang, J., et Chen, C. (2016a).
Networked
microgrids for self-healing power systems.
IEEE Transactions on Smart Grid,
7(1):310–319.
[Wang et al., 2015b] Wang, Z., Chen, B., Wang, J., et others (2015b).
Decentralized
energy management system for networked microgrids in grid-connected and is-
landed modes. IEEE Transactions on Smart Grid, 7(2):1097–1105.
[Wang et al., 2016b] Wang, Z., et He, Y. (2016b). Two-stage optimal demand response
with battery energy storage systems. IET Generation, Transmission & Distribution,
10(5):1286–1293.
[Wang et al., 2015c] Wang, Z., et Wang, J. (2015c). Self-healing resilient distribution
systems based on sectionalization into microgrids. IEEE Transactions on Power
Systems, 30(6):3139–3149.
[Wang et al., 2011] Wang, Z., Yang, R., et Wang, L. (2011). Intelligent multi-agent con-
trol for integrated building and micro-grid systems.
In ISGT 2011, pages 1–7.
IEEE.
[Wei et al., 2017] Wei, J., Roche, R., Koukam, A., et Lauri, F. (2017). Agent and consen-
sus approaches to microgrid coordination for resilience improvement. In Pro-
ceedings of the 9th International Conference on Management of Digital EcoSystems,
pages 28–34. ACM.
[Wei et al., 2018] Wei, J., Roche, R., Koukam, A., et Lauri, F. (2018). Decentralized coor-
dination for mutual rescue in microgrid clusters. In 2018 IEEE International Energy
Conference (ENERGYCON), pages 1–6. IEEE.
[Weiss, 1999] Weiss, G. (1999).
Multiagent systems: a modern approach to dis-
tributed artiﬁcial intelligence. MIT press.
[Wooldridge et al., 1995] Wooldridge, M., et Jennings, N. R. (1995). Intelligent agents:
Theory and practice. The knowledge engineering review, 10(2):115–152.
[Xu et al., 2013] Xu, L., Ruan, X., Mao, C., Zhang, B., et Luo, Y. (2013). An improved
optimal sizing method for wind-solar-battery hybrid power system. IEEE transac-
tions on Sustainable Energy, 4(3):774–785.
[Xu et al., 2011] Xu, Y., et Liu, W. (2011). Novel multiagent based load restoration
algorithm for microgrids. IEEE Transactions on Smart Grid, 2(1):152–161.
[Yang et al., 2011] Yang, T., Roy, S., Wan, Y., et Saberi, A. (2011). Constructing con-
sensus controllers for networks with identical general linear agents. International
Journal of Robust and Nonlinear Control, 21(11):1237–1256.


---

Page 142

---

BIBLIOGRAPHY
127
[Ye et al., 2011] Ye, D., Zhang, M., et Sutanto, D. (2011). A hybrid multiagent framework
with q-learning for power grid systems restoration. IEEE Transactions on Power
Systems, 26(4):2434–2441.
[Yu et al., 2012] Yu, W., DeLellis, P., Chen, G., Di Bernardo, M., et Kurths, J. (2012). Dis-
tributed adaptive control of synchronization in complex networks. IEEE Transac-
tions on Automatic Control, 57(8):2153–2158.
[Yu et al., 2015] Yu, W.-Y., Soo, V.-W., et Tsai, M.-S. (2015). Power distribution system
service restoration bases on a committee-based intelligent agent architecture.
Engineering Applications of Artiﬁcial Intelligence, 41:92–102.
[Zhao et al., 2015] Zhao, B., Xue, M., Zhang, X., Wang, C., et Zhao, J. (2015). An mas
based energy management system for a stand-alone microgrid at high altitude.
Applied Energy, 143:251–261.
[Zidan et al., 2012] Zidan, A., et El-Saadany, E. F. (2012). A cooperative multiagent
framework for self-healing mechanisms in distribution systems. IEEE transac-
tions on smart grid, 3(3):1525–1539.


---

Page 143

---



---

Page 144

---

LIST OF FIGURES
1.1
Annual mean temperature change for land and ocean. Measured in degree.
7
1.2
Share of renewable energy in gross ﬁnal energy consumption in France. . .
8
1.3
Global fossil fuel consumption. Global primary energy consumption by fos-
sil fuel source, measured in terawatt-hours (TWh). . . . . . . . . . . . . . .
9
1.4
An example of MG. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10
1.5
Contents of future MG network. . . . . . . . . . . . . . . . . . . . . . . . . .
14
1.6
Diagram of mutual impacts between MG coordination and operation of in-
ternal elements.
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
15
3.1
Agents and their environment.
. . . . . . . . . . . . . . . . . . . . . . . . .
37
3.2
An example of MG constitution. . . . . . . . . . . . . . . . . . . . . . . . . .
43
3.3
HMAS architecture.
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
47
3.4
Modeling of MG network.
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
49
3.5
Diagram of the simulation software. . . . . . . . . . . . . . . . . . . . . . . .
50
3.6
Coding architecture of the user interface.
. . . . . . . . . . . . . . . . . . .
50
3.7
Diagram of the models in user interface. . . . . . . . . . . . . . . . . . . . .
51
3.8
The user interface: graphical interface and batch command line.
. . . . . .
52
3.9
Architecture of the Platform Programming. . . . . . . . . . . . . . . . . . . .
53
3.10 Coding diagram of the simulation software including the user interface,
electrical system, and MAS. . . . . . . . . . . . . . . . . . . . . . . . . . . .
55
4.1
An example of the electrical connection in MG network.
. . . . . . . . . . .
62
4.2
Diagram of the communication corresponding to ﬁgure 4.1. . . . . . . . . .
63
4.3
Independent control ﬂowchart.
. . . . . . . . . . . . . . . . . . . . . . . . .
65
4.4
Fault control ﬂowchart. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
66
4.5
Centralized control strategy ﬂowchart. . . . . . . . . . . . . . . . . . . . . .
69
4.6
Coordinating interaction diagram. . . . . . . . . . . . . . . . . . . . . . . . .
70
4.7
An example of power trading in the network in ﬁgure 4.7. . . . . . . . . . .
74
4.8
The output-cost curve. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
74
4.9
Market strategy ﬂowchart. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
76
4.10 Distributed power ﬂow algorithm ﬂowchart.
. . . . . . . . . . . . . . . . . .
79
129


---

Page 145

---

130
LIST OF FIGURES
4.11 Bidding prices of the MGs. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
85
4.12 Coordination results for MG3. . . . . . . . . . . . . . . . . . . . . . . . . . .
86
4.13 Bidding prices of the MGs. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
87
4.14 Coordination power for MG3. . . . . . . . . . . . . . . . . . . . . . . . . . .
88
5.1
Studied 13-MG System. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
91
5.2
Part of the Communication Network for the Studied Network.
. . . . . . . .
92
5.3
The Control Strategy for Cooperation.
. . . . . . . . . . . . . . . . . . . . .
92
5.4
The Communication Diagram for Cooperation.
. . . . . . . . . . . . . . . .
93
5.5
Facility operation status in MG3.
. . . . . . . . . . . . . . . . . . . . . . . .
98
5.6
Coordination Group Formed in Proposed Approach. . . . . . . . . . . . . .
99
5.7
Power dispatching results among MGs in case 1. . . . . . . . . . . . . . . . 102
5.8
Calculation time in case 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
5.9
Generation cost in network in case 1 . . . . . . . . . . . . . . . . . . . . . . 103
5.10 Power dispatching results among MGs in case 2. . . . . . . . . . . . . . . . 105
5.11 Calculation time in case 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
5.12 Generation cost in network in case 2 . . . . . . . . . . . . . . . . . . . . . . 106
5.13 Electrical connection of the 34-MG network. . . . . . . . . . . . . . . . . . . 106
5.14 Calculation time in case 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
5.15 Generation cost in network in case 3 . . . . . . . . . . . . . . . . . . . . . . 107


---

Page 146

---

LIST OF TABLES
2.1
Selected papers on coordination approaches. . . . . . . . . . . . . . . . . .
30
4.1
MG facility numbers in the 12-MG system.
. . . . . . . . . . . . . . . . . .
80
4.2
MGs facilities rated powers. . . . . . . . . . . . . . . . . . . . . . . . . . . .
80
4.3
Other parameters.
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
80
4.4
Electricity price parameters in each MG. . . . . . . . . . . . . . . . . . . . .
81
4.5
Cost parameters. OM: operation and maintenance, UD: startup and shut-
down [Moghaddam et al., 2011a].
. . . . . . . . . . . . . . . . . . . . . . .
81
4.6
Requester MG cost in EUR. . . . . . . . . . . . . . . . . . . . . . . . . . . .
82
4.7
Simulation results. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
83
5.1
MG elements parameters in 13-MG system.
. . . . . . . . . . . . . . . . .
97
5.2
Rated power of elements. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
99
5.3
Other element parameters.
. . . . . . . . . . . . . . . . . . . . . . . . . . .
99
5.4
Summary of calculation time and cost. . . . . . . . . . . . . . . . . . . . . . 108
131


---

Page 147

---



---

Page 148

---

Document generated with LATEX and:
the LATEX style for PhD Thesis is downloaded — http://www.multiagent.fr/ThesisStyle
the tex-upmethodology package suite — http://www.arakhne.org/tex-upmethodology/
