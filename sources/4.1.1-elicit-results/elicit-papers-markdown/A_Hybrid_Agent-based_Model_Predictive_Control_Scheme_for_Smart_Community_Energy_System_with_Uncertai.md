# A Hybrid Agent-based Model Predictive Control Scheme for Smart Community Energy System with Uncertain DGs and Loads

## Paper Metadata

- **Filename:** A Hybrid Agent-based Model Predictive Control Scheme for Smart Community Energy System with Uncertain DGs and Loads.pdf
- **DOI:** 10.35833/mpce.2019.000090
- **Authors:** Wang, Xiaodi and Liu, Youbo and Zhao, Junbo and Liu, Junyong
- **Year:** 2021
- **Journal/Venue:** Journal of Modern Power Systems and Clean Energy
- **URL:** http://dx.doi.org/10.35833/MPCE.2019.000090
- **Extraction Date:** 2025-06-03T15:01:19.400681
- **Total Pages:** 12

## Abstract



## Keywords



---

## Full Text Content



### Page 1

JOURNAL OF MODERN POWER SYSTEMS AND CLEAN ENERGY, VOL. 9, NO. 3, May 2021
A Hybrid Agent-based Model Predictive
Control Scheme for Smart Community Energy
System with Uncertain DGs and Loads
Xiaodi Wang, Youbo Liu, Junbo Zhao, and Junyong Liu
Abstract—A multi-agent consensus-based market scheme is
proposed for the cooperation of community and multiple mi‐
crogrids (MGs) in a distributed, economic and hierarchal man‐
ner. The proposed community-based market framework with
frequency regulation (FR) market is formulated as a two-level
scheduling problem: the global decision-making process of com‐
munity agent (CA) to participate in the FR market and the in‐
teraction and control process of local MGs to achieve collabora‐
tion in response to the global target with efficient pricing rules.
Specifically, the model predictive control (MPC) is integrated
with the consensus-based theory to allow MG to obtain an eco‐
nomic and reliable dispatch in the presence of uncertainties of
distributed generators and loads. Thanks to the distributed na‐
ture of the proposed scheme, its robustness to communication is‐
sues has been strengthened and a win-win situation for all ener‐
gy stakeholders can be achieved. The robustness of the pro‐
posed scheme is investigated in various conditions, including dif‐
ferent
implementation
strategies,
communication
topologies,
and the level of uncertainties.
Index Terms—Community market, model predictive control
(MPC), energy management, consensus-based market scheme.
I. INTRODUCTION
T
HE microgrid (MG) is regarded as a key block of fu‐
ture smart grid because of its ability to embrace wide
applications of distributed generators (DGs), including con‐
ventional DGs, renewable energy sources (RESs), energy
storage systems, responsive demands, etc. [1]. Meanwhile,
the increasing integration of distributed RESs with stochastic
features challenges the economic operation of MGs [2].
In recent years, a smart community, which is expected to
be a combination of interconnected MGs, has emerged to
provide additional operation flexibility and efficiency of ex‐
isting MGs [3]. The exported/imported energy of geographi‐
cally adjacent MGs can be diverse and complementary [4].
Thus, developing a community energy system that allows
MGs to exchange information, independently trigger actions
and achieve economic collaboration is a promising way to re‐
duce the adverse effect of uncertain factors. Also, a smart
community with large flexible capacity enables this energy
system to participate in frequency regulation (FR) market
more efficiently [5]. However, all these benefits cannot be
achieved without the effective technical architecture design
of the smart community [6]. It contains three main challeng‐
es: ①the participation strategy of FR, in which the flexible
energy resources of the community ought to be integrated to
improve the system economic performance; ②the selfscheduling of each MG, in which an intelligent energy man‐
agement system (EMS) is required to obtain an economic
and reliable dispatching scheme in the presence of uncertain‐
ties of DG generation and load demands; ③the interaction
and interest-coordination mechanism, where the interests of
the community and each local MG need to be considered si‐
multaneously.
This new paradigm has triggered the interest of research‐
ers on community energy management, which has the ability
to coordinate the operation of multiple MGs. To realize this
synergy, the schemes adopted to address the collaboration
problem can be categorized into two cases: centralized and
distributed schemes. The centralized scheme is widely adopt‐
ed to obtain a satisfactory result in a energy management
framework of coordinated community [7], [8]. However, it
leads to security/privacy issues among MGs, vulnerability to
single-point failures, high requirement of information and
communication technology (ICT) deployment and large com‐
putational burden for large-scale systems [9], [10]. To deal
with these challenges, the distributed architecture and its as‐
sociated optimization algorithms are developed [11] - [13],
which are capable to find satisfactory solutions while pre‐
serving the privacy and flexible interaction of energy stake‐
holders [14].
In particular, establishing a community-based market with
an efficient pricing mechanism is a feasible solution to facili‐
tate MGs working in a collaborative manner [5], [6]. Multiclass energy management of a community-based market is
designed in [15], where the preferences of prosumers are
considered. An auction scheme to share energy storage in a
community is implemented [16]. Reference [17] takes into
Manuscript received: October 10, 2019; accepted: February 8, 2020. Date of
Cross Check: February 8, 2020. Date of online publication: October 22, 2020.
This work was supported by National Key R&D Program of China
(No. 2017YFE0112600).
This article is distributed under the terms of the Creative Commons Attribu‐
tion 4.0 International License (http://creativecommons.org/licenses/by/4.0/).
X. Wang, Y. Liu , and J. Liu are with the College of Electrical Engineering,
Sichuan University, Chengdu 610065, China (e-mail: 18280409667@163. com;
liuyoubo@scu.edu.cn; liujy@scu.edu.cn).
J. Zhao (corresponding author) is with the Department of Electrical and Com‐
puter Engineering, Mississippi State University, Starkville 39762, USA (e-mail:
junbo@ece.msstate.edu).
DOI: 10.35833/MPCE.2019.000090
573

---


### Page 2

JOURNAL OF MODERN POWER SYSTEMS AND CLEAN ENERGY, VOL. 9, NO. 3, May 2021
account the self-interests of each MG and presents a hierar‐
chical optimization method for MG community. Additional‐
ly, market-based mechanisms that coordinate multiple energy
entities in a distributed manner to reach a global consensus
have been widely studied. Reference [18] develops a distrib‐
uted model predictive control (MPC) -based scheduling ap‐
proach for a network of interconnected MGs. In addition,
the dual sub-gradient algorithm [19], [20] and a bi-level twostage robust optimal scheduling [21] are utilized to coordi‐
nate the operation of MGs, but no corresponding pricing
rules are designed. Reference [22] establishes an incentive
mechanism for MGs based on Nash bargaining theory to
guarantee the profit of each MG through trading among
MGs, and the optimization model is decomposed and solved
by using the alternating direction method of multipliers (AD‐
MM). Bargaining game [23] can effectively realize the com‐
plex interaction process among independent agents. The ener‐
gy trading among multiple MGs is formulated as an uncon‐
strained Stackelberg game in [24], where the equilibrium can
be achieved through relaxation algorithms.
In summary, existing reseach on market-based mecha‐
nisms to achieve the cooperation of diverse entities is usual‐
ly carried out with several drawbacks: ①most market frame‐
works have not been integrated into the traditional operation
scheme of electricity market, e.g., FR market with strict on‐
line tracking requirements [10]; ②the widely used decentral‐
ized ADMM and dual sub-gradient algorithms are updated
with constant or diminishing step sizes, which do not reflect
explicit market supply-demand status in the collaborative
transaction process; ③the interaction process among all enti‐
ties assumes that communication issues are perfectly handled
with the rich deployment of ICT devices, which is not feasi‐
ble in practice.
To deal with the aforementioned challenges, this paper
proposes an agent-based MPC scheme for a smart communi‐
ty energy system with uncertain DGs and loads. It fully inte‐
grates energy resources within the community in a coopera‐
tive manner to participate in the FR market. The global tar‐
get of the community to profit from the FR market can be
achieved in a distributed manner through interaction and con‐
trol process of local MGs with profitable transaction prices.
The agent-based MPC scheme motivates local agents to en‐
roll in the community transaction scheme and offers a winwin framework for all market stakeholders in the communi‐
ty. The major contributions of this paper can be summarized
as follows.
1) A hybrid market framework is designed for integrating
FR market with the proposed community-based market. The
concepts of this framework can be easily applied to other
market schemes, i.e., ancillary service market, providing po‐
tential economic benefits for the whole community.
2) An agent-based market mechanism with efficient pric‐
ing rules is established for the coordination of distributed
MGs within a smart community. Specifically, the pricing
rules are derived from the interaction process among all
agents, which provides explicit community market informa‐
tion and illustrates the preferences of individual MG in the
energy transaction.
3) An MPC energy management scheme is integrated with
the consensus-based theory to allow MG to obtain economic
and reliable dispatch. The interaction process among all
agents has been spontaneously carried out based on the exist‐
ing
communication
infrastructure
within
a
community.
Thanks to the distributed nature of the proposed scheme, its
robustness to communication issues has been strengthened
and a better economic performance can be achieved.
The remainder of this paper is organized as follows. Sec‐
tion II formulates the problem and presents the detailed
mathematical model description of the proposed scheme.
Case studies are carried out in Section III. And Section IV
concludes the paper.
II. PROBLEM FORMULATION AND PROPOSED SCHEME
The supply and demand fluctuation of an MG not only
brings adverse influence on its economic operation but also
affects its market participation modes. This calls for the de‐
velopment of an efficient energy management framework to
guarantee the economic performance of MGs. To this end, a
hybrid agent-based market scheme for coordinated energy
management of a smart community including multiple MGs
is proposed and shown in Fig. 1.
The proposed energy management scheme is modeled as a
bi-level scheduling problem: the global decision-making pro‐
cess of community agent (CA) to optimize FR market partic‐
ipation strategy of the whole community at the upper level,
and the interaction and control process of local MGs at the
lower level in response to the global requirements from FR
market, i. e., strict energy trajectory tracking requirements
over
the
regulation
period.
Specifically,
the
interaction
among local MGs is carried out on the proposed communitybased market platform, in which pricing signals are utilized
to facilitate the consensus reaching process with existing
communication infrastructure. It consists of the following
major components.
1) CA monitors the global information based on the pre‐
diction of the community future status, and then the optimal
capacity to participant in the FR market can be determined
by CA. After that, the energy trajectory PrefCA executed at
Information flow;
Power flow
Main grid
CA
CA
Interactive layer
Control layer
BESS
DG
DR
PV
BESS
DG
DR
PV
BESS
DG
DR
PV
BESS
DG
DR
PV
BESS
DG
DR
PV
cbuy,CA/
csell,CA
cbuy,1/csell,1
cbuy,3/
csell,3
MG1
MG1
MG2
MG2
MG4
MG5
MG5
MG3
MG3
MG4
cbuy,2/csell,2
cbuy,4/csell,4
cbuy,5/csell,5
Pref,CA
Ptie,1
Ptie,5
Ptie,4
Ptie,2
Ptie,3
Ptie,CA
Consensusbased price
Fig. 1.
Proposed community framework.
574

---


### Page 3

WANG et al.: A HYBRID AGENT-BASED MODEL PREDICTIVE CONTROL SCHEME FOR SMART COMMUNITY ENERGY ...
the lower level can be calculated once the CA received FR
signal from the main grid.
2) Self-organizing MG responds to price signals and deter‐
mines the control scheme of its conventional DG, battery en‐
ergy storage system (BESS), demand response (DR) resourc‐
es as well as the transactive energy flow with the community.
3) Local MG interacts with adjacent MGs to share infor‐
mation of transaction prices/quantity (i. e., csellmcbuym, and
Ptiem) iteratively so as to reach a consensus on transactive
prices. Each of them iteratively updates its control scheme to
optimize transactive energy flow with CA in response to
price signals. Meanwhile, the energy trajectory tracking the
requirement of FR program can be achieved by the coordina‐
tion of MGs through iterations. Finally, from the consensusbased results, the distributed energy management of each
MG can be implemented at each optimization interval in the
distributed MPC framework.
In summary, the proposed scheme performs the compre‐
hensive economic optimization within a community and MG
energy management scheduling, which provides a good plat‐
form for CA to integrate MGs to participate in the FR mar‐
ket.
A. Upper-level Scheduling: Global Decision-making Process
of CA
CA, as a higher-level autonomous entity, aims to deter‐
mine optimal participation strategies in energy and FR mar‐
kets operated by the main grid at the beginning of each opti‐
mization interval. Its objective function at time slot k is:
max
FFR ∑
h= 0
H - 1
(c FR (k + h)FFR (k + h)-
cbuyCA (k + h)PbuyCA (k + h)- csellCA (k + h)PsellCA (k + h)+
∑
m= 1
M
(cbuym (k + h)Pbuym (k + h)- csellm (k + h)Psellm (k + h)))
(1)
where h is the index of prediction horizon; H is the optimiza‐
tion horizon; m is the index of MGs; M is the total number
of MGs in the community; cbuyCA and csellCA are the buying
and selling prices offered by the main grid to CA, respective‐
ly; PbuyCA and PsellCA are the imported/exported power of CA
from/to the main grid, respectively; Pbuym and Psellm are the
imported/exported power of MGm from/to CA, respectively;
cbuym and csellm are the buying and selling prices for MGm,
respectively; and FFR is the committed FR capacity provided
for the main grid by the community. In (1), the first term
represents the FR revenue, while the second term involves
the transaction cost with the main grid, and the third term
represents the energy transaction cost with the multiple MGs.
CA firstly initiates the bilateral trading price with MGs,
i. e., buying price cbuym and selling price csellm, of MGm at
the beginning of the scheduling interval, and predicts supplydemand status as well as the dispatchable energy capacity in
the community. Then, the optimal FR capacity that CA of‐
fered to the main grid is determined accordingly. Since buy‐
ing/selling prices of MGs cannot be accurately predicted and
they are also changeable through interaction process at the
lower level, the predicted transaction prices for all MGs are
set as the initial bilateral transaction prices offered to MGs
by CA.
At real-time practice, only a fraction of committed FR ca‐
pacity is requested by the main grid (averaged every 15
min), i.e., αFFR. α is a scaling of the normalized regulation
signal received from the main grid. Once CA receives the re‐
al regulation signal α(k), the optimal energy trajectory PrefCA
of CA at time slot k can be calculated via (2).
PrefCA (k)=∑
m= 1
M
Pbuym (k)-∑
m= 1
M
Psellm (k)+ α(k)FFR (k)
(2)
Assuming that CA does not have its own flexible energy
sources, the coupling energy constraints among multiple
MGs should therefore be considered as follows:
PtieCA (k)= PbuyCA (k)- PsellCA (k)=∑
m= 1
M
(Pbuym (k)- Psellm (k)) (3)
where PtieCA is the tie-line power between CA and the main
grid. A positive PtieCA means CA needs to import the energy
from the main grid and vice versa. During the operation, CA
aggregates the transactive power flow of MGs to track the
desired energy trajectory within the allowed tracking error
bound εtol in a distributed manner through the scheduling pro‐
cess at the lower level. The constraint for tracking error can
be expressed as:
| PtieCA (k)- PrefCA (k)|£ εtol
(4)
Note that an MG can either sell/buy energy from the main
grid or the community. Thus, a MG benefits from the trad‐
ing with community instead of the main grid at time slot k
only if the following conditions are satisfied.
Condition 1: the selling price csellm offered to MGm with
surplus power by the community is higher than the selling
price csellCA provided by the main grid.
Condition 2: the buying price cbuym offered to MGm with
deficient power by the community is lower than the buying
price cbuyCA provided by the main grid.
In order to aggregate local MGs, the transaction prices of‐
fered to MGs by the community are subject to (5).
{
cmin
buy (k)£ cbuym (k)£ cbuyCA (k)
csellCA (k)£ csellm (k)£ cmax
sell (k)
(5)
where cmin
buy and cmax
sell are the minimum buying price and the
maximum selling price for MGm while MGm trades with
CA, respectively.
In addition, the committed FR must be within the control‐
lable power capacity of the whole community via (6).
0£ FFR (k)£ ηCA∑
m= 1
M
P max
DGm (k)+ P max
dism (k)+ DPloadm (k)
(6)
where ηCA is the maximum allowable FR participation por‐
tion; P max
DGm, P max
dism, and DPloadm are the maximum DG output
power, BESS discharging power, and load curtailment in
MGm, respectively.
B.
Lower-level
Scheduling:
MPC
Control
Process
of
Individual MG
In this subsection, the dynamic model of individual MG is
presented and then the control objective functions subject to
different constraints of different MG components are dis‐
575

---


### Page 4

JOURNAL OF MODERN POWER SYSTEMS AND CLEAN ENERGY, VOL. 9, NO. 3, May 2021
cussed. Each MG consists of controllable DGs, photovoltaic
(PV), BESS and responsive load, and its dynamics can be
formulated as:
EBESSm (k + 1)= EBESSm (k)+
é
ë
ê
ê
ê
ê
ê
ê
ê
ê
ê
ù
û
ú
ú
ú
ú
ú
ú
ú
ú
ú
0
Tηch
- T
ηdis
0
T
é
ë
ê
ê
ê
êêê
ù
û
ú
ú
ú
úúú
PDGm (k)
Pchm (k)
Pdism (k)
DPDRm (k)
(7)
Ptiem (k)=
é
ë
ê
ê
êêê
ê
ù
û
ú
ú
úúú
ú
1
-1
1
1
T é
ë
ê
ê
ê
êêê
ù
û
ú
ú
ú
úúú
PDGm (k)
Pchm (k)
Pdism (k)
DPDRm (k)
+ [1
-1]
é
ë
êê
ù
û
úú
P̂
PVm (k)
P̂
Lm (k)
(8)
where T is the control time interval; PDGm (k)Pchm (k),
Pdism (k), and DPDRm (k) are the DG output, BESS charging
power, BESS discharging power, and load curtail power in
MGm at time slot k, respectively; EBESSm (k) is the state of
BESS at time slot k; Ptiem (k) is the transaction power of
MGm; P̂
PVm (k) and P̂
Lm (k) are the predicted PV output and
the predicted load demand, respectively; and ηch and ηdis are
BESS charging efficiency and BESS discharging efficiency,
respectively.
Thus, the state space form of a MG can be formulated as
follows:
{
x(k + 1)= Ax(k)+ Bu U(k)
y(k)= Cu U(k)+ Bd W(k)
(9)
where A, Bu, Cu, and Bd are the coefficient matrices; x(k) is
the state vector that represents the state of BESS EBESSm (k)
at time slot k; U(k) is the control sequence, which consists
of
the
dispatchable
sources
PDGm (k)Pchm (k)Pdism (k) and
DPDRm (k) in each MG; y(k) is the system output, i. e., the
transaction power Ptiem (k) of MGm; and W(k) is the vector
of
uncertain
factors
and
can
be
expressed
as
W(k)=
[P̂
PVm (k)P̂
Lm (k)]T. In practice, uncertainties are usually asso‐
ciated with the intermittent energy outputs of renewables
P̂
PVm (k) and load demands P̂
Lm (k).
The decision-making objective of an MG is to manage its
dispatchable energy resources and determine the optimal
transactive power to minimize the total cost while satisfying
all the constraints. The local controller of a MG is designed
in an MPC framework for controlling the operation process
on a receding horizon. Specifically, the optimization problem
of MGm at each time slot k can be expressed as:
min fm =∑
h= 0
H - 1
(( f DGm (DPDGm (k + h))+ f DRm (DPDRm (k + h))+
f BESSm (Pchm (k + h)Pdism (k + h))+ ftradem (Ptiem (k + h)))
(10)
where fm is the total costs of MGm on its optimization hori‐
zon, which covers DG operation cost f DGm, BESS operation
cost f BESSm, DR operation cost f DRm and transaction cost
ftradem. At the beginning of each scheduling interval, MPC
controller of MG calculates the control action sequence for
time slots [k + 0k + 1...k + H - 1] based on the predicted sta‐
tus of the MG. The first element of the computed control se‐
quence will be taken as the input at time slot k. The control
action for the future interval will be calculated at the begin‐
ning of the next scheduling interval. Each MG seeks the
least total cost shown in (10), which is subjected to the fol‐
lowing physical constraints.
1) Conventional DG
The fuel cost of a conventional DG can be expressed via
a typical quadratic function [25] and can be written as (11).
f DGm (PDGm (k))= αDGm + βDGm PDGm (k)+ γDGm P 2
DGm (k)
(11)
0£ PDGm (k)£ P max
DGm
(12)
where αDGm, βDGm, and γDGm are the fuel cost coefficients of
conventional DG.
2) BESS
In order to capture the charging and discharging cycles of
BESS, the charging power Pch,m and discharging power Pdis,m
are separately considered and the state of BESS can be ex‐
pressed as:
EBESSm (k + 1)= EBESSm (k)+ ηch TPchm (k)- 1
ηdis
TPdism (k)
(13)
Generally, BESS should satisfy the constraint (14) for the
safe operation and periodic utilization within the scheduling
cycle.
ì
í
î
ïï
ïï
0£ Pchm (k)£ P max
chm
0£ Pdism (k)£ P max
dism
E min
BESSm £ EBESSm (k)£ E max
BESSm
(14)
where P max
chm is the maximum charging power; and E min
BESSm and
E max
BESSm are the lower and upper bounds of the permitted stor‐
age level, respectively.
The cost function of BESS in the scheduling period can
be approximated with a quadratic function with the suitable
cost coefficient αBESSm [26] and can be written as (15).
f BESSm (Pchm (k)Pdism (k))= αBESSm (P 2
chm (k)+ P 2
dism (k)) (15)
Note that simultaneously charging and discharging of
BESS will lead to suboptimal solution due to the quadratic
function of BESS. The theoretical proof can be found
in [27].
3) Flexible Load
Based on the linear demand versus the price expression,
the DR cost function of each MG can be calculated accord‐
ing to the quantity of power curtailment DPDRm. And the cor‐
responding sensitiveness [24] is:
f DRm (DPDRm (k))= -
1
αDRm
DP 2
DRm (k)+ PLm (k)- βDRm
αDRm
DPDRm (k)
(16)
where αDRm and βDRm are the sensitive parameters of flexible
loads inside MGm; and PLm is the benchmark load of MGm.
The load of MGm can be flexibly scheduled, subjecting to
the constraint (17).
0£ DPDRm (k)£ ηLm PLm (k)
(17)
where ηLm is the maximum allowable power curtailment por‐
tion.
Thus, the ultimate load of MGm can be expressed as (18).
576

---


### Page 5

WANG et al.: A HYBRID AGENT-BASED MODEL PREDICTIVE CONTROL SCHEME FOR SMART COMMUNITY ENERGY ...
Ploadm (k)= PLm (k)- DPDRm (k)
(18)
where Ploadm (k) is the actual load in MGm after the imple‐
mentation of DR.
4) Transactive Energy Model of MG
An MG can act as a consumer to buy the power from the
main grid or community when the energy output is insuffi‐
cient to balance the total energy demand within the MG.
Otherwise, it will act as a producer to sell power to the
main grid or community. Hence, the trading cost/revenue of
MG is determined by the direction of tie-line power and the
associated trading price via (19).
ftrade (Ptiem (k))=(cbuym (k)Pbuym (k)- csellm (k)Psellm (k))T (19)
The trading power is limited by the power balance con‐
straint (20) in a MG. Also, and the maximum buying power
P max
buym and the maximum selling power P max
sellm are determined
by the transmission line capacity shown in (21).
Ptiem (k)= Pbuym (k)- Psellm (k)= -PPVm (k)- PDGm (k)+ Pchm (k)-
Pdism (k)+ Ploadm (k)
(20)
{
0£ Pbuym (k)£ P max
buym
0£ Psellm (k)£ P max
sellm
(21)
5) Uncertainties of MG
Additionally, the interval prediction method [26] is ap‐
plied to estimate the lower/upper bounds of the uncertainties
for an MG. The following uncertain set is provided to de‐
scribe the uncertainties of PV generation and load in each
MG. In this case, the actual load PLm (k) and PV output
PPVm (k) in different time periods are all limited in the inter‐
val bounds that are shown as:
{
PLm (k)Î[P̂
Lm (k)- DP max
Lm (k)P̂
Lm (k)+ DP max
Lm (k)]
PPVm (k)Î[P̂
PVm (k)- DP max
PVm (k)P̂
PVm (k)+ DP max
PVm (k)]
(22)
where DP max
Lm (k) and DP max
PVm (k) are the maximum prediction
deviations of load and PV output at time slot k, respectively.
C. Lower-level Scheduling: Interaction Process of Multiple
MGs
Although each MG optimizes its scheduling scheme indi‐
vidually, the tracking requirement of energy trajectory from
CA can only be achieved by the cooperation of all MGs. In
this paper, the first-order adaptive consensus [28] algorithm
is extended to achieve the developed consensus process.
Consider a community consisting of n MGs that interacts
with each other based on the existing communication infra‐
structure. The interaction network among agents can be illus‐
trated by a directed graph denoted as ς ={υε}, where υ=
{12...M} is the set of MGs and ε Í υ´ υ(nmÍ υ) is the
edge set (interaction). In this digraph, each MG is represent‐
ed by a vertex and the this digraph edge provides a commu‐
nication link between MGn and its adjacent MGm. For
MGm, Am =(nÍ υ|(nm)Í ε) represents the set of its neigh‐
boring MGn. Based on these most basic elements, the row
stochastic matrix D=(dnm) of the graph ς can be formulated
as:
dnm =
ì
í
î
ï
ïïï
ï
ïïï
2
zn + zm + ∆
nÎ Am
1- ∑
nÎ Am
(zn + zm + ∆)
n= m
0
otherwise
(23)
where zm and zn are the numbers of neighboring MGs con‐
nected with MGm and MGn, respectively; and ∆is a small
positive value.
Given a strongly connected interaction topology, the adap‐
tive consensus algorithm for the consensus-based iteration
process at each iteration τ can be described as (24).
yτ + 1
m
=∑
n= 1
M
d τ
nm yτ
m
(24)
where ym is the output of MGm (tie-lie power flow, i. e.,
Ptie,m), derived from the system dynamics formulation of (7);
dnm is a normalized distance between MGm and MGn; and τ
is the τth iteration.
The power mismatch DP between aggregated MGs transac‐
tive energy flow and the desired energy trajectory of CA
from the upper-level decision process at each time slot k are
introduced into the following adaptive consensus algorithm.
DPτ (k)=∑
m= 1
M
P τ
tiem ( )
k - PrefCA (k)
(25)
Thus, the consensus-based interaction should be carefully
designed to track the energy trajectory following the rule
shown in (26).
cτ + 1
m (k)=∑
n= 1
M
d τ
mncτ + 1
m ( )
k + μDPτ (k)
(26)
where μ is a positive scalar denoting the adjustment factor of
power mismatch, which controls the convergence speed of
the system. The increase or decrease of prices cτ
m of each
MG follows the sign of DPτ at the τth iteration.
By fully considering the lower and upper limits of transac‐
tion prices, constraint (27) and constraint (28) are derived
from (5). The global target at the upper level can be
achieved when all MGs at the lower level reach a consensus
on transaction prices. Then, the optimal community energy
management scheme can be determined while satisfying vari‐
ous constraints.
ck
buym ={
cmin
buy
cτ
buym £ cmin
buy
cτ
buym
cmin
buy < cτ
buym < cbuyCA
cbuyCA
cτ
buym ³ cbuyCA
(27)
ck
sellm ={
cmin
sell
cτ
sellm £ cmin
sell
cτ
sellm
cmin
sell < cτ
sellm < csellCA
csellCA
cτ
sellm ³ csellCA
(28)
where ck
buym and ck
sellm are the ultimate consensus-based buy‐
ing price and selling price of MGm, respectively.
D. Algorithm Implementation
In this subsection, a bi-level coordinated energy manage‐
ment algorithm is proposed to obtain the solution of the de‐
veloped framework. The upper-level CA solves its own opti‐
mization problem and provides references for the local MG
at the lower layer. The iterative consensus-based strategy is
577

---


### Page 6

JOURNAL OF MODERN POWER SYSTEMS AND CLEAN ENERGY, VOL. 9, NO. 3, May 2021
then developed to exchange information with each agent,
yielding global consensus solutions as the deviation from the
reference energy trajectory decreases to a tolerance threshold
or the maximum iteration time is reached. Detailed imple‐
mentation steps at time slot k are as follows.
Step 1: MGs initiate expected trading prices ĉ buym (k) and
ĉ sellm (k) for further transactions while CA initiates the unan‐
nounced bilateral trading prices for each MG.
Step 2: the global information is monitored by CA, yield‐
ing the commitments FFR (k) by (1).
Step 3: once the actual value α(k) is provided by the main
grid, PrefCA (k) is calculated for the community by (2). And
then, the information of PrefCA (k) is shared among MGs.
Step 4: each MG updates the uncertain forecast set of
P̂
Lm (k) and P̂
PVm (k) for future prediction horizon at time slot
k and obtains the real-time state of PPVm (k) and PLm (k). MG
responds to the announced bilateral trading price signals of‐
fered by CA. As a result, an initial set of its control action
U 0
m by (10) is determined locally.
Step 5: the interaction process is implemented among lo‐
cal MGs and CA at iteration τ (1£ τ £ τmax).
1) The interaction network D is updated among MGs.
2) The consensus-based transaction price cτ
m (k) is updated
among MGs by (25).
3) The new control sequence U τ
m (k) of MGm at the τth iter‐
ation is updated by solving (9) based on PPVm (k), PLm (k),
and cτ
m (k).
4) The tie-line power P τ
tiem (k) of each MG is updated. The
energy mismatch DPτ (k) is calculated by (24).
5) If DPτ (k)£ εtol or τ ³ τmax, the iteration will stop and the
flow goes to Step 6; otherwise, let τ = τ + 1, and the flow
goes back to 2).
Step 6: upon the completion of MG interaction, each MG
applies its optimal control action U τ
m (k) to MG.
Step 7: let k = k + 1 and the flow proceeds to the next cy‐
cle.
The convergence proof of the proposed method is provid‐
ed in the Appendix A.
III. SIMULATION RESULTS
A. Simulation Settings
Numerical simulations are conducted in a communitybased scenario to evaluate the performance of the proposed
method. It encompasses five MGs: MG1, MG2, MG3, MG4,
and MG5. Each MG has the same basic device components,
but different capacities and load profiles. The used parame‐
ters are given in the Appendix B Tables BI and BII, and the
parameters shown in Table BII are drawn from [28]. The
length of each time interval T is set to be 15 min, which
means that the optimization problem will be solved every 15minute interval with 3-hour prediction horizon H. The initial
buying and selling prices offered by CA to all MGs are
drawn from a uniform distribution with 10% heterogeneity
between 60 $/MWh and 80 $/MWh. The minimum buying
price and the maximum selling price for MGs are set as 40
$/MWh and 100 $/MWh, respectively. In addition, the buy‐
ing and selling prices for CA to trade with the main grid are
both 70 $/MWh. Historical data for FR prices and signals
from PJM are extracted from [10]. According to off-line sim‐
ulations, the maximum iteration time τmax of the consensusbased process is set to be 50, while the accepted tracking de‐
viation εtol is 0.002 MW and the adjustment factor μ is 10.
All simulations are carried out on a 64 bit PC with 1.99
GHz CPU and 2 GB RAM, and the YALMIP toolbox in
MATLAB and CPLEX are adopted to solve the quadratic
programming problem.
B. Result Analysis
1) Comparison of Different Implementations
In order to validate the effectiveness of the proposed dis‐
tributed consensus-based scheme, a none-cooperating scheme
and a centralized scheme [29] are used for comparison from
an economic perspective. In the none-cooperating scheme,
each local MG only focuses on its own local objectives and
trades energy with community at the price of grid rate (i.e.,
both the buying price and the selling price are 70 $/MWh).
For the widely used centralized scheme, CA is in charge of
dispatching energy resources of all MGs to participate in FR
market under the assumption that MG agents only trade with
CA at the price of grid rate. All three schemes are designed
in an MPC framework.
Table I reports the daily benefits and costs achieved by
the proposed scheme, the centralized MPC scheme, and the
none-cooperating MPC scheme. Compared with the pro‐
posed scheme, the centralized MPC scheme has provided a
slightly better performance on CA cost and energy trajectory
tracking, i.e., the less energy mismatch between aggregated
MG energy flow and the desired energy trajectory across the
day. However, the total revenue of all MGs obtained by both
the
centralized
MPC
and
the
none-cooperating
MPC
schemes are less than that by the proposed scheme. This
means that the proposed scheme can bring more benefit to
MGs. The reasons lie in two folds: ①in the proposed dis‐
tributed scheme, the community has offered higher selling
price and lower buying price for MGs compared with that of
the centralized/none-cooperating schemes, which leads to CA
benefit loss and MGs profit gaining; ②the centralized
scheme focuses on the energy trajectory tracking instead of
the local interest of each MG. Moreover, although CA may
suffer certain economic loss from trading with MGs, the par‐
ticipation of FR market will bring CA with more revenue to
cover its transaction loss. In this regard, the proposed market
framework has established a win-win situation for all energy
stakeholders. Additionally, it can be noticed that the total op‐
eration cost of all MGs is $1066.4 for the proposed scheme,
higher than $1036.4 for the centralized one. But for largescale interaction problems, it can be acceptable to obtain a
sub-optimal settlement in exchange of more flexibility. In ad‐
dition, compared with the none-cooperating scheme, Table I
demonstrates that the improvement of MG benefits by the
proposed scheme mainly attributes to the transaction plat‐
form provided by the community, where the ultimate consen‐
sus-based bilateral trading prices have coordinated the opera‐
tion of MGs.
578

---


### Page 7

WANG et al.: A HYBRID AGENT-BASED MODEL PREDICTIVE CONTROL SCHEME FOR SMART COMMUNITY ENERGY ...
2) Analysis on Transaction Results
Figure 2 illustrates the power transaction between CA and
each MG and Fig. 3 demonstrates the corresponding control
sequence of each MG. The lower bound of the buying price
and the upper bound of the selling prices between CA and
MGs are 40 $/MWh and 100 $/MWh, respectively, which
can guarantee the profits of CA. The positive transactive
power represents that the MG imports power from CA to
MGs while the negative power means the MGs export pow‐
er to CA. It can be found out that all MGs have done the
transaction at the same prices thanks to the consensus-based
interaction process.
Since each MG operates according to its local objective
and intends to minimize its local cost, it can be observed
that each of them tends to sell power when its PV genera‐
tion is high, e.g., from hour 6 to hour 18 in MG2 and from
hour 8 to hour 22 in MG4. And buying power as PV genera‐
tion is not efficient to achieve the supply-demand balance in
MG, e.g., from hour 0 to hour 6 in MG1 and from hour 18
to 24 in MG4. Though each MG is set with differential com‐
TABLE I
PERFORMANCE COMPARISON BETWEEN PROPOSED DISTRIBUTED SCHEME, CENTRALIZED MPC SCHEME AND NONE-COOPERATING SCHEME
Scheme
Proposed distributed MPC
Centralized MPC
Non-cooperating MPC
Agent
CA
MG1
MG2
MG3
MG4
MG5
CA
MG1
MG2
MG3
MG4
MG5
MG1
MG2
MG3
MG4
MG5
Purchased energy
(k Wh)
4141.9
3335.3
843.3
641.7
1322.0
1041.1
4139.7
2541.1
637.7
545.7
975.6
650.5
3403.5
832.8
601.0
1337.9
1031.1
Sold energy
(k Wh)
11478.5
937.4
4788.3
3749.2
2755.5
2333.3
11465.3
899.1
4332.8
3168.9
2400.9
1873.8
888.0
4581.8
3566.8
2693.4
2248.8
Trading fee ($)
With MG
806.9
114.9
-352.9
-278.9
-153.7
-136.3
512.7
114.9
-258.6
-183.6
-99.7
-85.6
133.1
-316.5
-249.2
-135.2
-118.0
With main grid
513.5
-512.7
Operation
fee ($)
139.8
152.7
281.3
234.7
257.9
190.4
129.5
239.8
230.5
246.2
128.8
132.9
264.6
226.7
248.6
FR revenue
($)
1325.4
1325.4
Total
revenue
($)
1032.0
-254.73
200.20
-2.41
-81.02
-121.60
1325.40
-305.33
129.19
-56.21
-130.74
-160.54
-262.00
183.60
-15.30
-91.50
-130.60
Mismatched
energy
(k Wh)
295.14
97.05
0
6
12
18
24
-400
0
400
800
Power (k W)
Time (hour)
(a)
0
6
12
18
24
Time (hour)
(c)
0
6
12
18
24
Time (hour)
(b)
0
6
12
18
24
Time (hour)
(b)
-400
-800
0
400
800
Power (k W)
-400
-800
0
400
800
Power (k W)
-400
-800
0
400
800
Power (k W)
0
6
12
18
24
Time (hour)
(e)
-400
0
400
800
Power (k W)
 Actual load demand;
Actual PV output;
Transactive power
Fig. 2.
Power transaction between CA and MGs. (a) MG1. (b) MG2. (c)
MG3. (d) MG4. (e) MG5.
0
6
12
18
24
Time (hour)
(a)
0
6
12
18
24
Time (hour)
(c)
0
6
12
18
24
Time (hour)
(e)
0
6
12
18
24
Time (hour)
(b)
0
6
12
18
24
Time (hour)
(d)
-80
0
80
160
240
320
Power (k W)
-150
-100
-50
0
50
100
Price ($MWh)
Price ($MWh)
Price ($MWh)
Price ($MWh)
Price ($MWh)
-80
80
240
400
Power (k W)
-150
-100
-50
0
50
100
150
 
-80
0
80
160
240
320
400
480
Power (k W)
-200
-150
-100
-50
0
50
100
-80
0
80
160
240
320
Power (k W)
-150
-100
-50
0
50
100
-80
0
80
160
240
320
400
Power (k W)
-150
-100
-50
0
50
100
150
 Pbatt;
PDG;
PDR;
 cbuy;
 csell
Fig. 3.
Control sequences of MGs. (a) MG1. (b) MG2. (c) MG3. (d) MG4.
(e) MG5.
579

---


### Page 8

JOURNAL OF MODERN POWER SYSTEMS AND CLEAN ENERGY, VOL. 9, NO. 3, May 2021
ponent capacities and cost functions, the exported/imported
power of the dispatchable devices is largely influenced by
the consensus-based trading prices induced by multi-agent in‐
teraction. Taking MG1 as an example, from hour 0 to hour 6
and from hour 18 to hour 24, MG1 intends to purchase elec‐
tricity from CA due to its insufficient supply status. Howev‐
er, the consensus-based trading prices are all relatively low,
leading to little power generation of DG and nearly no im‐
plementation of the load curtailment. In addition, during this
period, BESS has the potential to charge instead of dis‐
charge due to the optimistic expectation for future trading
prices. An interesting phenomenon can be found here that
BESS would intend to be charged from the controllable ener‐
gy resources (i.e., DG and DR) to fulfill the future economic
object owing to the MPC operation strategy, e.g., from hour
0 to hour 6 in MG1. And then, from hour 6 to hour 18, the
increased buying and selling prices offered to MG1 have mo‐
tivated MG1 to generate more power or curtail more load ac‐
cording to its own cost function. Note that MG1 would in‐
tend to utilize its own flexible energy devices to export
more power to CA with the favorable transaction price dur‐
ing hour 6 to hour 12.
3) Impacts of Communication Interaction Topology
More representative case studies are presented to analyze
the performance of the consensus-based strategy under differ‐
ent communication topologies. Two types of interaction to‐
pologies of the five-MG communities have been utilized to
test the proposed scheme: ①star connection shown in Fig.
4(a); ②random connection in Fig. 4(b), which is also the to‐
pology setting in the previous simulation case.
Figures 5 to 7 illustrate the evolution process of trading
prices, tie-line power/mismatched power, and benefits of all
MGs during the iterations under star connection and random
connection at hour 16, respectively. It can be found that in
one iteration cycle, all MGs are able to converge to the opti‐
mal trading price asymptotically and track the desired trajec‐
tories accurately irrespective of communication topologies.
In addition, the ultimate results of consensus-based trading
prices and iteration times are slightly different under these
two communication topologies.
As
shown
in
Fig.
5,
the
agreed
selling
price
72.47 $/MWh under the star connection is lower than 77.03
$/MWh under the random connection. By contrast, the
agreed buying price 55.56 $/MWh under the star connection
is higher than 51.22 $/MWh under the random connection.
Thus, MGs interacting with adjacent MG agents in the star
connection would bring more benefits to CA compared with
the random connection. It is interesting to observe from Fig.
6 that all communication topologies (star connection or ran‐
dom connection) can promote MGs to reach the ultimate
consensus prices with little tracking deviation tolerance.
Moreover, as illustrated in Fig. 7, the transaction cost of five
MGs increases while the operation cost decreases with the
consensus-based iterations. This is due to the declined ten‐
dency of selling and buying prices. As a result, MGs tend to
buy power from CA instead of utilizing their own devices to
generate power.
In addition, the topology of the communication network
would also affect the convergence rate. The optimal results
can be obtained in 21 iterations to reach an equilibrium
point under star connection, while it only takes 19 iterations
under the random connection.
4) Impacts of Adjustment Factor
The adjustment parameter is a key factor influencing the
convergence speed. More case studies have been carried out
to analyze the impact of parameter μ while other parameters
 Mismatched power (k W)
 Mismatched power (k W)
Mismatched power
No. of iterations
(a)
No. of iterations
(b)
MG1;
MG2;
MG3;
MG4;
MG5
1
5
9
13 17 21
-150
0
150
300
450
600
750
Power (k W)
-500
-400
-300
-200
-100
0
100
1
7
13
19
-150
0
150
300
450
600
750
Power (k W)
-500
-400
-300
-200
-100
0
100
Fig. 6.
Evolution process of tie-line power and mismatched power under
different communication topologies. (a) Star connection. (b) Random con‐
nection.
 MG transaction cost;
 MG operation cost;
CA revenue
1
6
11
16
21
1
2
3
4
5
6
7
Price ($)
1
2
3
4
5
6
7
Price ($)
1
4
7
10 13 16 19
No. of iterations
(a)
No. of iterations
(b)
Fig. 7.
Evolution process of the benefits of all agents under different com‐
munication topologies. (a) Star connection. (b) Random connection.
MG1
MG1
MG2
MG4
MG5
MG3
MG3
MG5
MG2
MG4
(a)
(b)
Fig. 4.
Communication topologies of investigated MG community. (a) Star
connection. (b) Random connection.
1
4
7 10 13 16 19 22
50
60
70
75
71
79
83
87
Buying price
($MWh)
50
60
70
Selling price
($MWh)
Buying price
($MWh)
Selling price
($MWh)
76
72
80
84
88
No. of iterations
(a)
No. of iterations
(b)
1 3 5 7 9 11 13 15 17
MG1;
MG2;
MG3;
MG4;
MG5
Fig. 5.
Evolution process of trading prices among MGs under different
communication topologies. (a) Star connection. (b) Random connection.
580

---


### Page 9

WANG et al.: A HYBRID AGENT-BASED MODEL PREDICTIVE CONTROL SCHEME FOR SMART COMMUNITY ENERGY ...
remain unchanged at the hour 17 (under random connec‐
tion). Four cases with different adjustment parameter μ val‐
ues have been tested: ①case A with μ = 4; ②case B with
μ =10; ③case C with μ equaling to 20; ④case D with μ =
25. Figure 8 shows the evolution process of trading prices
among agents in the four cases, while Fig. 9 further demon‐
strates all MGs can reach a final consensus with little track‐
ing deviation, irrespective of different adjustment factors.
As shown in Fig. 8, the consensus-based buying and sell‐
ing prices are 67.43 $/MWh and 82.11 $/MWh in case A, re‐
spectively, while those for case B are nearly the same as
case A. The agreed buying price 66.04 $/MWh in case C is
lower while the agreed selling price 82.65 $/MWh is higher
compared with the prices of cases A and B. Furthermore, the
buying and selling prices are 62.71 $/MWh and 83.65
$/MWh in case D, respectively, significantly different from
the consensus prices in the previous cases. However, it is no‐
ticeable that the convergence speed has improved greatly
with the increasing value of parameter μ. The simulation re‐
sult illustrates that it takes 27 iterations to reach a consensus
on the ultimate trading prices/quantity (μ= 4), while the num‐
ber of iterations decreases to 8 as the value of parameter μ
increases to 20. The convergence rate does not elevate any‐
more as value μ exceeds a threshold. In fact, a very large μ
may lead to instability, since the termination of iterations re‐
quires the amount of mismatched energy decreases to a cer‐
tain value.
5) Impacts of Communication Failure
For practical applications, the imperfect communication
network may cause the contact loss of some MGs during the
interaction process at the lower level. To investigate that,
more cases are conducted to test the robustness of the pro‐
posed scheme against the communication failure: ①case E:
MG1 agent loses the contact with other MGs at the 10th itera‐
tion; ②case F: based on case E, MG1 agent reconnects
with other MGs at the 30th iteration. Other parameters re‐
main unchanged at the hour 15 (under random connection).
Figure 10 illustrates the evolution process of the trading
prices for each MG in the case E and case F, while the itera‐
tion processes of the mismatched power and tie-line power
of each agent are provided in Fig. 11.
Note that once the MG1 agent is disconnected from the
communication network, it will trade with CA at the price of
grid rate (i.e., both the buying and selling prices are 70 $/
55
60
65
70
75
1
16
31
46
56
67
75
83
91
1
26
51
76
101
Buying price
($MWh)
67
75
83
91
Buying price
($MWh)
Selling price
($MWh)
55
60
65
70
75
Selling price
($MWh)
No. of iterations
(a)
No. of iterations
(b)
MG1;
MG2;
MG3;
MG4;
MG5
Fig. 10.
Evolution process of trading prices among MGs with communica‐
tion failure. (a) Case E. (b) Case F.
1 11 21 31 41
56
-150
0
150
300
450
600
Power (k W)
-800
-600
-400
-200
0
200
1
21 41 61 81 101
-200
0
200
400
600
800
Power (k W)
-800
-600
-400
-200
0
200
 Mismatched power (k W)
 Mismatched power (k W)
No. of iterations
(a)
No. of iterations
(b)
MG1;
MG2;
MG3;
MG4;
MG5;
Mismatched power 
Fig. 11.
Evolution process of tie-line power and mismatched power with
communication failure. (a) Case E. (b) Case F.
Mismatched power
MG1;
MG2;
MG3;
MG4;
MG5
1
5
9
13 17 21
-200
-100
0
100
200
300
Power (k W)
-200
-100
0
100
200
300
Power (k W)
-200
-100
0
100
200
Power (k W)
-600
-400
-200
0
200
400
1 3 5 7 9 11
14
-200
-100
0
100
200
Power (k W)
-750
-500
-250
0
250
 Mismatched power (k W)
 Mismatched power (k W)
 Mismatched power (k W)
 Mismatched power (k W)
No. of iterations
(a)
No. of iterations
(c)
No. of iterations
(b)
1
3
5
7 8
No. of iterations
(d)
1
3
5
8
-800
-600
-400
-200
0
200
7
-750
-500
-250
0
250
Fig. 9.
Evolution process of tie-line power and mismatched power with
different adjustment factors. (a) Case A. (b) Case B. (c) Case C. (d) Case D.
60
65
65
70
1
7
13
19
27
75
79
83
87
1
4
7
10
13
1
2
3
4
5
6
7
8
75
79
83
87
91
76
81
86
91
96
Buying price
($MWh)
Buying price
($MWh)
Buying price
($MWh)
75
79
83
87
Buying price 
($MWh)
Selling price
($MWh)
60
65
70
75
Selling price
($MWh)
60
65
70
75
Selling price 
($MWh)
60
70
Selling price 
($MWh)
No. of iterations
(a)
No. of iterations
(c)
1
2
3
4
5
6
7
8
No. of iterations
(d)
No. of iterations
(b)
MG1;
MG2;
MG3;
MG4;
MG5
Fig. 8.
Evolution process of trading prices among MGs with different ad‐
justment factors. (a) Case A. (b) Case B. (c) Case C. (d) Case D.
581

---


### Page 10

JOURNAL OF MODERN POWER SYSTEMS AND CLEAN ENERGY, VOL. 9, NO. 3, May 2021
MWh) as shown in Fig. 10(a) and (b), which will highly af‐
fect its individual control process and lead to more mis‐
matched power in the community, as shown in Fig. 11(a)
and (b). Thanks to the on-going interaction process of other
MGs, the disturbance brought by MG1 can be well handled,
though it will take more iterations to reach convergence.
Once the MG1 is reconnected to the communication net‐
work, the interaction process stays in the same manner as
the previous cases, where the ultimate consensus-based trans‐
action prices of all MGs reach nearly the same value. The
simulation results have demonstrated the robustness of the
proposed scheme against the communication failure.
6) Impacts of Uncertainties
Different degrees of uncertainties have been set to test the
influences of the uncertain renewable energy and load de‐
mand on the proposed scheme. The reference energy trajecto‐
ry of CA is presented as level A, while the predicted devia‐
tion DP max
Lm (k) and DP max
PVm (k) have been set to be 0%, 5%,
10%, 15% of the prediction value, which are denoted as lev‐
els B, C, D, E, respectively. Figure 12 illustrates the power
curves of tie-line between the CA and the main grid ob‐
tained by the proposed scheme under different uncertainty
degrees on the day. It can be observed that the energy trans‐
action between CA and the main grid is able to successfully
track trajectory with negligible errors in the presence of un‐
certainties. The main reason is that the proposed energy man‐
agement scheme is designed in an MPC framework, where
these uncertainties have been effectively taken into account
when implementing the controls. There may be another rea‐
son, that is, thanks to the consensus-based iteration process,
the flexible bilateral transaction prices can be achieved to
regulate the energy output/demand of all MGs.
IV. CONCLUSION
In this paper, a novel consensus-based distributed MPC
scheme of multiple MGs within a smart community is pro‐
posed in the presence of uncertain renewable energy and
load demand. The concept of community-based market to‐
gether with the FR market provides an alternative choice for
energy stakeholders in the community to gain economic im‐
provement. A feasible interactive structure of the proposed
scheme offers the transaction and information exchange plat‐
form, showing its great advantages on the coordination of
multiple MGs and CA in a distributed manner. In particular,
the global target of CA can be successfully achieved with re‐
spect for interest and privacy of local MGs with efficient
pricing rules. Numerical results have verified that the pro‐
posed scheme facilitates the participation of all agents, yield‐
ing a win-win situation. Meanwhile, thanks to the robustness
of the proposed scheme, the uncertainties of PV power and
load have been effectively taken into account. Future works
involve incorporating peer-to-peer energy sharing market
mechanism in a community. The possible malfunction of the
communication system will be further investigated.
APPENDIX A
Due to the quadratic characteristics of the MG function,
the transaction price cm can be expressed as the linear func‐
tion relating to Ptie, m, which is shown in (A1).
cm = αm Ptiem + βm
(A1)
where αm and βm are the coefficients of MGm.
The pricing rules for MG coordination are represented in
(24) and (25) at each iteration τ, which can be expressed as:
cτ + 1
m
=∑
n= 1
M
d τ
mncτ + 1
m
+ μDPτ
(A2)
P τ + 1
tiem = cτ + 1
m
αm
- βm
αm
(A3)
DPτ + 1 =∑
n= 1
M
d τ
mn[DPτ +(P τ + 1
tiem - P τ
tiem)]
(A4)
To analyze the convergence of the proposed consensus al‐
gorithm, the overall updating rules of (A1) to (A4) can be rewritten in the following matrix forms.
C τ + 1 = DC τ + 1 + μDP τ
(A5)
P τ = HC τ + 1 + F
(A6)
DP τ + 1 = DDP τ + D(P τ + 1 - P τ)
(A7)
where C, P, DP and F are the column vectors of cm,Ptiem, DP
and -βm/αm, respectively; and H = diag(1/α11/α21/αm). De‐
fine [CDP]
T as a new variable vector, the matrix can be ex‐
pressed as:
é
ë
ê
ù
û
ú
C τ + 1
DP τ + 1 = é
ë
ê
ù
û
ú
D
μIm
DH(D - Im)
D + μDH
é
ë
ê
ù
û
ú
C τ
DP τ
(A8)
where Im is an m-dimension identity matrix. Here, G is defined
as:
G = é
ë
ê
ù
û
ú
D
μIm
DH(D - Im)
D + μDH
(A9)
Equation (A10) demonstrates that if μ is small enough,
the eigenvalue of G will be the same as D.
|
| λI2m - G =
|
| λIm - D
2
+ μ
|
| DH
|
| λIm - Im »
|
| λIm - D
2
(A10)
Moreover, D is a double-stochastic matrix with dnm set in
(24) in the model, where D·1m = 1m. Since G and D share
the same eigenvalue, the formulation of (A11) can be ob‐
tained.
é
ë
ê
ù
û
ú
D
μIm
DH(D - Im)
D + μDH
é
ë
ê
ù
û
ú
1m
0m
= é
ë
ê
ù
û
ú
1m
0m
(A11)
-1060
-1590
-530
0
530
1060
Time (hour)
Power (k W)
0
6
12
18
24
A
B
C
D
E
Uncertain level
Fig. 12.
Tie-line power curves between CA and main grid under different
levels of uncertainties.
582

---


### Page 11

WANG et al.: A HYBRID AGENT-BASED MODEL PREDICTIVE CONTROL SCHEME FOR SMART COMMUNITY ENERGY ...
According to this proof, the system can converge to span
[1m, 0m]T as τ goes to infinity with small μ. Thus, cτ
m is able
to converge to a common value c*
m, and the value of ΔPm
gradually decreases.
APPENDIX B
REFERENCES
[1] J. Zeng, Q. Wang, J. Liu et al., “A potential game approach to distrib‐
uted operational optimization for microgrid energy management with
renewable energy and demand response,” IEEE Transactions on Indus‐
trial Electronics, vol. 66, no. 6, pp. 4479-4489, Jun. 2019.
[2] Y. Liu, K. Zuo, J. Liu et al., “Dynamic pricing for decentralized ener‐
gy trading in micro-grids,” Applied Energy, vol. 288, no. 1, pp. 689699, Oct. 2018.
[3] C. Essayeh, M. R. Fenni, and H. Dahmouni, “Optimization of energy
exchange in microgrid networks: a coalition formation approach,” Pro‐
tection and Control of Modern Power System, vol. 4, no. 24, pp. 1-10,
Dec. 2019.
[4] W. Liu, J. Zhan, and C. Y. Chung, “A novel transactive energy control
mechanism for collaborative networked microgrids,” IEEE Transac‐
tion on Power Systems, vol. 34, no. 3, pp. 2048-2060, May 2019.
[5] T. Sousa, T. Soares, P. Pinson et al., “Peer-to-peer and communitybased markets: a comprehensive review,” Renewable and Sustainable
Energy Reviews, vol. 104, pp. 367-378, Apr. 2019.
[6] F. Moret and P. Pinson, “Energy collectives: a community and fairness
based approach to future electricity markets,” IEEE Transactions on
Power Systems, vol. 34, no. 5, pp. 3994-4004, Sept. 2019.
[7] C. Wouters, E. S. Fraga, and A. M. James, “An energy integrated,
multi-microgrid, MILP (mixed-integer linear programming) approach
for residential distributed energy system planning: a South Australian
case-study,” Energy, vol. 85, pp. 30-44, Jun. 2015.
[8] S. D. Beigvand, H. Abdi, and M. L. Scala, “Hybrid gravitational
search algorithm-particle swarm optimization with time varying accel‐
eration coefficients for large scale CHPED problem,” Energy, vol.
126, pp. 841-853, May 2017.
[9] S. M. Amin, “Smart grid security, privacy, and resilient architectures:
opportunities and challenges,” in Proceedings of 2012 IEEE PES Gen‐
eral Meeting, San Diego, USA, Jul. 2012, pp. 1-2.
[10] R. Kumar, M. J. Wenzel, M. J. Ellis et al., “A stochastic model predic‐
tive control framework for stationary battery systems,” IEEE Transac‐
tions on Power Systems, vol. 33, no. 4, pp. 4397-4406, Jul. 2018.
[11] B. P. Koirala, E. Koliou, J. Friege et al., “Energetic communities for
community energy: a review of key issues and trends shaping integrat‐
ed community energy systems,” Renewable and Sustainable Energy
Reviews, vol. 56, pp. 722-744, Apr. 2016.
[12] Z. Zhang and M. Chow, “Convergence analysis of the incremental
cost consensus algorithm under different communication network to‐
pologies in a smart grid,” IEEE Transactions on Power Systems, vol.
27, no. 4, pp. 1761-1768, Nov. 2012.
[13] Z. Tang, D. J. Hill, and T. Liu, “A novel consensus-based economic
dispatch for microgrids,” IEEE Transactions on Smart Grid, vol. 9,
no. 4, pp. 3920-3922, Jul. 2018.
[14] V. P. Singh, N. Kishor, and P. Samuel, “Distributed multi-agent sys‐
tem-based load frequency control for multi-area power system in
smart grid,” IEEE Transactions on Industrial Electronics, vol. 64, no.
6, pp. 5151-5160, Jun. 2017.
[15] T. Morstyn and M. D. Mc Culloch, “Multiclass energy management for
peer-to-peer energy trading driven by prosumer preferences,” IEEE
Transactions on Power Systems, vol. 34, no. 5, pp. 4005-4014, Sept.
2019.
[16] W. Tushar, B. Chai, C. Yuen et al., “Energy storage sharing in smart
grid: a modified auction-based approach,” IEEE Transactions on
Smart Grid, vol. 7, no. 3, pp. 1462-1475, May 2016.
[17] P. Tian, X. Xiao, K. Wang et al., “A hierarchical energy management
system based on hierarchical optimization for microgrid community
economic operation,” IEEE Transactions on Smart Grid, vol. 7, no. 5,
pp. 2230-2241, Sept. 2016.
[18] F. Garcia-Torres, C. Bordons, and M. A. Ridao, “Optimal economic
schedule for a network of microgrids with hybrid energy storage sys‐
tem using distributed model predictive control,” IEEE Transactions on
Industrial Electronics, vol. 66, no. 3, pp. 1919-1929, Mar. 2019.
[19] M. Fathi and H. Bevrani, “Statistical cooperative power dispatching in
interconnected microgrids,” IEEE Transactions on Sustainable Energy,
vol. 4, no. 3, pp. 586-593, Jul. 2013.
[20] D. Gregoratti and J. Matamoros, “Distributed energy trading: the mul‐
tiple-microgrid case,” IEEE Transactions on Industrial Electronics,
vol. 62, no. 4, pp. 2551-2559, Apr. 2015.
[21] H. Qiu, B. Zhao, W. Gu et al., “Bi-level two-stage robust optimal
scheduling for AC/DC hybrid multi-microgrids,” IEEE Transactions
on Smart Grid, vol. 9, no. 5, pp. 5455-5466, Sept. 2018.
[22] H. Wang and J. Huang, “Incentivizing energy trading for interconnect‐
ed microgrids,” IEEE Transactions on Smart Grid, vol. 9, no. 4, pp.
2647-2657, Jul. 2018.
[23] K. Dehghanpour and H. Nehrir, “Real-time multiobjective microgrid
power management using distributed optimization in an agent-based
bargaining framework,” IEEE Transactions on Smart Grid, vol. 9, no.
6, pp. 6318-6327, Nov. 2018.
[24] G. E. Rahi, S. R. Etesami, W. Saad et al., “Managing price uncertain‐
ty in prosumer-centric energy trading: a prospect-theoretic stackelberg
game approach,” IEEE Transactions on Smart Grid, vol. 10, no. 1, pp.
702-713, Jan. 2019.
[25] H. Li, A. T. Eseye, J. Zhang et al., “Optimal energy management for
industrial microgrids with high-penetration renewables,” Protection
and Control of Modern Power System, vol. 2, no. 12, p. 12, Apr. 2017.
[26] Y. Liu, H. B. Gooi, Y. Li et al., “A secure distributed transactive ener‐
gy management scheme for multiple interconnected microgrids consid‐
ering misbehaviors,” IEEE Transactions on Smart Grid, vol. 10, no. 6,
pp. 5975-5986, Nov. 2019.
[27] D. Wu, T. Yang, A. A. Stoorvogel et al., “Distributed optimal coordina‐
tion for distributed energy resources in power systems,” IEEE Transac‐
tions on Automation Science and Engineering, vol. 14, no. 2, pp. 414424, Apr. 2017.
[28] X. Zhang, T. Yu, Z. Xu et al., “A cyber-physical-social system with
parallel learning for distributed energy management of a microgrid,”
Energy, vol. 165, pp. 205-221, Dec. 2018.
[29] P. Kou, D. Liang, and L. Gao, “Distributed EMPC of multiple mi‐
crogrids for coordinated stochastic energy management,” Applied Ener‐
gy, vol. 185, pp. 939-952, Jan. 2017.
Xiaodi Wang received the B.Sc. degree in electrical engineering from Sich‐
uan University, Chengdu, China, in 2016, where she is currently working to‐
ward the Ph.D. degree at the College of Electrical Engineering, Sichuan Uni‐
versity. Her current research interests include energy market design and dis‐
tributed energy management.
Youbo Liu received the B.Sc., M.Sc., and Ph.D. degrees from Sichuan Uni‐
versity, Chengdu, China, in 2005, 2008, and 2011, respectively. He is cur‐
rently an Associate Professor in power system with the College of Electric
Engineering, Sichuan University. His research interests mainly include ma‐
TABLE BI
PARAMETERS OF MGS
Agent
MG1
MG2
MG3
MG4
MG5
P max
DGm
(k W)
150
140
200
120
150
E max
BESSm
(k Wh)
200
500
400
300
200
E min
BESSm
(k Wh)
20
50
40
30
20
P max
chm/P max
dism
(k W)
100
50
125
80
50
P max
buym/P max
sellm
(k W)
500
500
500
500
500
ηch/ηdis
0.9
0.9
0.9
0.9
0.9
TABLE BII
OPERATING COST COEFFICIENTS OF DGS AND DR PROGRAM OF MGS
Agent
MG1
MG2
MG3
MG4
MG5
Operation cost
coefficient of DG
αDG
1.52
1.02
0.76
1.78
1.27
βDG
63
60
42
48
54
γDG
200
167
133
133
100
Operation cost
coefficient of DR
αDR
-0.009
-0.009
-0.009
-0.009
-0.009
βDR
0.8
0.8
0.8
0.8
0.8
Operation cost
coefficients of
BESS αBESS
8000
9000
10000
9000
8000
583

---


### Page 12

JOURNAL OF MODERN POWER SYSTEMS AND CLEAN ENERGY, VOL. 9, NO. 3, May 2021
chine learning in smart grid, energy storage system applications, etc.
Junbo Zhao received the Ph.D. degree from Virginia Tech, Falls Church,
USA, in 2018. He is currently with the Department of Electrical and Com‐
puter Engineering, Mississippi State University, Starkville, USA. He has
written two book chapters and published more than 40 peer-reviewed jour‐
nal and conference papers. He serves as the Associate Editor of the Interna‐
tional Journal of Electrical Power and Energy Systems and the IET Genera‐
tion, Transmission and Distribution. He is currently the Chair of the IEEE
Task Force on Power System Dynamic State and Parameter Estimation, the
Secretary of the IEEE Working Group on State Estimation Algorithms, and
the IEEE Task Force on Synchrophasor Applications in Power System Oper‐
ation and Control. His research interests include power system real-time
monitoring, operation and cyber security that include estimation, dynamics
and stability, cyber-attacks and countermeasures, big-data analytics, and ro‐
bust statistics with applications in the smart grid.
Junyong Liu received the Ph. D. degree from Brunel University, London,
U.K., in 1998. He is currently a Professor with the College of Electric Engi‐
neering, Sichuan University, Chengdu, China. His main research interests in‐
clude power system planning, operation, stability, and power market.
584

---
