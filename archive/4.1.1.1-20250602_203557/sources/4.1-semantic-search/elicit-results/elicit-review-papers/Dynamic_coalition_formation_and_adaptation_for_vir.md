

---

Page 1

---

See discussions, stats, and author profiles for this publication at: https://www.researchgate.net/publication/229003714
Dynamic coalition formation and adaptation for virtual power stations in smart
grids
Article · January 2011
CITATIONS
4
READS
172
3 authors, including:
S. Ossowski
Rey Juan Carlos University
289 PUBLICATIONS   9,018 CITATIONS   
SEE PROFILE
All content following this page was uploaded by S. Ossowski on 24 January 2014.
The user has requested enhancement of the downloaded file.


---

Page 2

---

Dynamic coalition formation and adaptation for virtual
power stations in smart grids
Radu-Casian Mihailescu
University Rey Juan Carlos
Madrid, Spain
radu.mihailescu@urjc.es
Matteo Vasirani
University Rey Juan Carlos
Madrid, Spain
matteo.vasirani@urjc.es
Sascha Ossowski
University Rey Juan Carlos
Madrid, Spain
sascha.ossowski@urjc.es
ABSTRACT
An agent-based organizational model for a smart energy sys-
tem is introduced relying on a dynamic coalition formation
mechanism for virtual power station (VPS) creation. Fol-
lowing, for VPS maintenance a solution concept is proposed
that stems from the existent stability solutions in coalitional
games and is introduced in conjunction with a corresponding
algorithm, deployed in distributed environments populated
by negotiating agents. The algorithm is intended as an open-
ended organizational adaptation, concerned with achieving
stable conﬁgurations that meet the desired functionalities
within stochastic scenarios.
Categories and Subject Descriptors
I.2.11 [Artiﬁcial Intelligence]:
Distributed Artiﬁcial In-
telligence Coherence and coordination, intelligent agents, mul-
tiagent systems
General Terms
Algorithms, Design
Keywords
virtual power stations, distributed generation, multi-agent
systems, coalition formation, emergent organization
1.
INTRODUCTION
In recent years, there is an increasing interest in the inte-
gration of distributed, small-scale, renewable generation into
the power system. An eﬃcient use of distributed energy re-
sources (DER) may increase the ﬂexibility and the resilience
of the power system at distribution level. Furthermore, it
is possible to reduce the dependence from large-scale, non-
renewable, power plants and therefore to contribute to a
sensible reduction of CO2 emissions. According to the US
department of Energy, a 5% increase in grid’s eﬃciency is
equivalent to the fuel and CO2 emission of 53 million cars.
The potential allure of the multiagent system paradigm
(MAS) to the power industry has been extensively docu-
mented so far [1]. To this respect, several management sys-
tems have been proposed for the organization of micro-grids
[3]. A micro-grids is deﬁned as a subsystem of the distri-
bution grid, formed by generation, storage and load device,
interconnected at the electrical and the informational level.
Micro-grids can be intended as a systemic approach to real-
ize the emerging potential of distributed generation.
Setting aside from this approach that aims at imposing an
architectural control, whether centralized or not, on already
predeﬁned micro-grids, our vision is intended at proposing
a method for congregating the smart-grid actors to dynami-
cally approximate optimal micro-grid conﬁgurations. Thus,
the main concern is developing techniques aimed at estab-
lishing and adapting a suitable virtual organizational struc-
ture. The procedure is designed such that it develops on the
concept of integrating DERs in the form of virtual power
stations [5]. A virtual power station (VPS) is conceived as
a bundle of DERs that are connected through an informa-
tional infrastructure and act in a coordinated way as a single
entity. The challenging problem related to the implementa-
tion of the VPS concept is the distributed control of the
DERs, mainly due to the stochastic behaviour of the system
and the heterogeneity of the devices involved.
The aim of this work is modelling the coordination of vir-
tual power plants in the sense of coalitional games. Instead
of considering centralized architectures [4, 5], we claim that a
dynamic, bottom-up, approximation of optimal VPS conﬁg-
urations is more eﬀective to ensure ﬂexibility and robustness
to the system.
2.
PROBLEM REPRESENTATION
The coalition games we aim to address in our approach
are the ones where the coalition formation problem is pro-
jected on an underlying network topology, given that the
cost for cooperation also plays a major role. This class of
games is primarily characterized by non-superadditivity, in
the sense that gains resultant from forming coalitions are
limited by the actual cost of coalition formation1 and co-
ordination, thus the grand coalition is seldom the optimal
structure. Furthermore, the coalitional game is subject to
the dynamism of the environment. The challenge is to de-
velop mechanisms that permit large number of autonomous
agents to collectively achieve a desired functionality by per-
manent adaptive dynamics.
In our scenario, we set to investigate the integration of
renewable energy resources to the grid in the form of virtual
power stations by means of aggregating the power generat-
ing potential of various devices in a novel way in the context
of MAS. As system designers, we choose to enable the au-
tonomous agents with the basic coordination primitives, and
leave to the agents to self-organize and coordinate as the sit-
uation may demand, in a fully distributed manner.
1The cost of forming a coalition can be perceived through
the negotiation process and information exchange which in-
cur costs.


---

Page 3

---

We model the problem as a dynamic coalition formation
game with the following formalization:
Let M = ￿A, βi, S, Φ, v￿be a multi-agent system where:
• A = {a1, a2, ..., an} represents the set of agents of a
given portion of the distribution grid. We assume that
each stakeholder that is connected to the grid is rep-
resented by a software agent that manages the corre-
sponding device (e.g., generators, storage devices, in-
telligent loads).
• βi is the forecast amount of electricity for the following
day associated with agent ai. If βi > 0, then agent ai is
a provider, whilst if βi < 0 then agent ai is a consumer
(or load).
Let P ⊆A denote the set of providers,
and L ⊆A the set of consumers.
In this work we
assume that an agent is either a provider or a load,
and therefore P ∪L = A, P ∩L = ∅. We will refer
onwards generically, to an agent belonging to set P as
PA, and to an agent belonging to set L as LA.
• S = {S1, S2, ..., Sm} is the set of coalitions that par-
tition the set A.
We assume that all coalitions are
disjoint, and therefore:
m
￿
j=1
Sj = A,
Sj ∩Sk = ∅, ∀j ￿= k
• Φ = {φ1, φ2, φ3} is a set of constraints that must hold
for every coalition. In this work, we enforce that the
number of members of each coalition does not exceed
a predeﬁned value N, which corresponds to the safety
limit imposed by technological constraints (φ1). We
also want that each coalition is able to supply electric-
ity to all the loads, so as the energetic balance between
generation and consumption must be positive (φ2). Fi-
nally, each coalition must realise a desired generation
proﬁle of electricity that would qualify them as VPS
(φ3). Formally:
φ1 : |Sj| ≤N ∀j ∈{1, ..., m}
φ2 :
￿
ai∈Sj
βi > 0
φ3 :
￿
ai∈Pj
βi = ψ
where Pj = P ∩Sj, and ψ represents the desired ener-
getic proﬁle that each coalition wants to achieve.
• v : S →R is a function that for every coalition of the
set S returns its utility value, representing a multi-
criterion evaluation of domain speciﬁc parameters.
The goal of the coordination problem is obtaining a parti-
tioning of A into a coalition structure S that complies with
the set of constraints Φ and at the same time maximises
the social welfare2 of the system, without jeopardizing the
functionality of any of the coalitions. We leave aside for now
what this trade-oﬀimplies and further develop on this issue
in Sections 5.
2For computing the social welfare of the system we mean
the typical interpretation of averaging over the utilities of
all coalitions.
3.
COALITION FORMATION MECHANISM
Our proposed approach is intended as a decentralized and
dynamic method. Here coalition formation is achieved by
opportunistic aggregation of agents, while maximizing coali-
tional beneﬁts by means of taking advantage of local re-
sources in the grid. It consists of three phases.
• Coalition initiation.
To accomplishing this task we
have chosen a straightforward approach: the PAs whose
energy availability exceeds a predeﬁned threshold value
are entitled of establishing themselves as VPS initia-
tors and will do so with a probability p inversly propor-
tional to the number of the agent’s PA uncommitted
neighbors that are also set to do so.
• Provider aggregation phase. This procedure dynami-
cally constructs the organizational structure via a ne-
gotiation mechanism, where proposals and requests are
handled opportunistically. The initiator PA assumes
the role of CA (coordinator agent) for the emergent
coalition. The mechanism proceeds in a Contract Net-
like fashion with the following steps: CAs send re-
quests to their neighboring PAs indicating the VPS
proﬁle that they want to realize, in terms of scale
and energetic potential 3. Based upon these speciﬁca-
tions PAs evaluate CAs’ oﬀers and select the preferred
choice from their candidate set. Eventually, CAs re-
ceive oﬀer responses and decide committing PAs.
The CA’s decision is based on calculating an associa-
tion coeﬃcient that reﬂects the self-suﬃciency of the
potential coalition i assuming the joining of actor j.
This is denoted as a linear combination of the parame-
ters that apply for this particular case study: security
measures (which implies computing contingency analy-
sis - Cj), transmission costs (Tj) and energetic balance
(Ej):
ϕi,j = w1 · Cj + w2 · Tj + w3 · Ej
(1)
We note that the ﬁrst two parameters (of negative val-
ues) are ought to give an indication of the network’s ca-
pability of avoiding line overloads and incurred trans-
mission costs. The former gives an indication of the
impact that the integration of the LA’s load would pro-
duce on the system’s buses in terms of the percentage
of capacity drop. By transmission costs we imply the
eﬀect of the power loss in the course of transmission,
over the coalition’s total power, represented by this ra-
tio. The last parameter represents the percent increase
or decrease of the coalition’s energetic balance, given
the desired state of oﬀer matching demand. Formu-
lating the association coeﬃcient in this manner allows
placing more emphasis on the contingency and trans-
mission coeﬃcients at the beginning of the aggregation
of actors, while the energetic balance gains more signif-
icance proportionally to the number of actors involved.
This is obviously a key aspect since one cannot expect
attaining a reasonable energetic balance at the very
3The constraints imposed on the coalition formation process
may vary according to the desired feature of the emerging
VPS.


---

Page 4

---

beginning of the coalition formation process. The util-
ity function of the coalition, v, represents the sum of
the association coeﬃcients for the coalition members,
as shown in Equation 2.
v(Si) =
￿
j∈Si
ϕi,j
(2)
• Consumer aggregation phase.
Once the VPS energetic potential has been ensured,
the only remaining phase requires the aggregation of
LAs. This operates in a similar manner. LAs proceed
by submitting their forecasted demand to the CAs in
their proximity. For each such request, the CAs cal-
culate the corresponding association coeﬃcient. Based
on this information, a proposal response is being awarded
to the most suitable LAs for joining the coalition, by
enclosing its corresponding association coeﬃcient. LAs
will conclude the procedure by selecting the coalition
whose utility is mostly increased by their commitment.
The decision is unequivocally accepted by the CA since
it comes as a response to its precedent proposal and it
is exclusively addressed to the CA. The LAs’ prefer-
ence for acting in this sense is justiﬁed by the fact that
the utility of the coalition would have a direct eﬀect
on its reliability.
To be noted that the decision of selecting the best can-
didate is carried without a complete representation of
the environment, but rather based on local and possi-
bly incomplete knowledge. This is the underlying rea-
son for the evolutionary nature of the algorithm that
iteratively approximates a solution through reﬁnement
steps.
4.
COALITION SELF-ADAPTATION
The second important issue we tackle regards the notion
of stability that the system is capable to achieve, given the
dynamism of the environment. Thus, the problem we are
facing in open organizations requires a modiﬁcation of the
coalition structure due to the variations occurring within
the system. All actors submit on a daily basis their fore-
casted proﬁle, which typically does not diﬀer exceedingly
from their previous one. Nevertheless these cumulated vari-
ations would entail a reorganization of the coalitions for the
following forcasted period in order to assure enhanced co-
ordination at the coalition level. Therefore, consequent to
calculating the energetic balance of the coalition, it is to
be determined the actors that would qualify to be signed-
oﬀ, or the proﬁle of the actors that would be eligible to be
signed-in to the coalition. The association network gener-
ated during the coalition formation process, revealing the
existing interdependencies within the coalition, plays a key
role at this stage. The weakest links signify the actors the
coalition is least dependent on, based on which agents are
to be proposed for being signed out of a coalition.
With these considerations in mind we seek a notion of
equilibrium that intrinsically provides an argumentation scheme,
which allows for a reorganization of the coalition structure.
Furthermore, the solution concept should reﬂect the decen-
tralization outlook of our scenario, while minimizing the
structural adaptations by providing a minimum set of inter-
action rules in order of attaining the desired stability prop-
erties amongst negotiating agents.
The solution we propose can be directly referenced to
game-theoretic approaches on issues of stability and nego-
tiation. For further considerations on notions of stability,
their strength, limitations and interrelations we refer the
reader to [2]. In our scenario, of utmost importance is the
agents’ capability to coordinate and reorganize into groups
or coalitions by transforming traditional game-theory criteri-
ons of stability towards operating in dynamic environments.
Moreover, we advocate for reorienting game-theory to ac-
comodate situations where coordination is a more natural
operational descriptor of the game rather than simply self-
interested settings. As it is emphasized in [2], an equivalent
formulation for solution concepts can be in interpreted in
terms of objections and counter-objections. More formally,
let x be an imputation in a coalition game with transfer-
able payoﬀ(A, v), we deﬁne our argumentation scheme as
follows:
• (S, y) is an objection of coalition S to x against T if S
excludes i and e (S ∪{i} , x) > e (S, y)
• coalition T counteracts to the objection of coalition S
against accepting player i if e (T ∪{i} , y) /e (T, x) >
1+µ or e (T ∪{i} , y)+e (S, y) > e (T, x)+e (S ∪{i} , x)−
τ.
To correlate the game-theoretic terms introduced above
to our setting, we give the interpretation of these terms for
our scenario. Speciﬁcally, by imputation we mean the distri-
bution of utilities over the coalitions’ set, whereas the excess
e of each coalition represents the diﬀerence between its po-
tential maximum (see Section 2) and its current utility v
We reason that the excess criteria applied for solution con-
cepts such as the kernel and the nucleolus appears to be an
appropriate measure of the coalition’s eﬃciency, especially
in games where the primary concern lies rather in the perfor-
mance of the coalition itself. This basis further advocates
for argumentation settings where objections are raised by
coalitions and not by single players, such as the case of the
bargaining set or the kernel. The objection (S, y) may be
interpreted as an argument of coalition S for excluding i re-
sulting in imputation y where its excess is being decreased.
Our solution models situations where such objections cause
unstable outcomes only if coalition T to which the objec-
tion has been addressed fails to counterobject by asserting
that S’s demand is not justiﬁed since T’s excess under y
by accepting i would be larger than it was under x. Such
a response would have hold if we simply presumed players
to be self-interested and not mind the social welfare of the
system. If on the contrary, players are concerned with the
overall eﬃciency of the system, they would consider accept-
ing the greater sacriﬁce of y in comparison to x only if this
would account for an improvement of S that exceeds the
deterioration of T’s performance by at least the margin τ.
Thus, τ is the threshhold gain required in order for justi-
fying the deviation, whereas µ represents S ’s tolerance to
suboptimal gains.
For applying this solution concept to our setting, we ad-
ditionally need to take into account the underlying topology
and thus restrain the inter-coalition argumentation to the
given network structure, representing a particularization of
the more generic outline presented herein. When multiple
objections are being adressed to one coalition, its decision of
considering one would be based on the criteria of maximiz-
ing parameter τ, while minimizing parameter µ. Also worth


---

Page 5

---

Figure 1: a) Social welfare of the system in num-
ber of steps.
b) Histogram representation for the
utilities of the coalitions
reminding is that the procedure is ought to occur within the
domain dependent constraints, that impose maintaining the
proﬁle of the coalition within certain limits (see Section 2).
Finally, we stress that the aim for our proposed scheme is
intended towards an open-ended organizational adaptation
concerned with achieving stable conﬁgurations in dynamic
environments where one-shot optimization procedure are un-
applicable.
5.
EXPERIMENTAL RESULTS
To begin with, we ﬁrst evaluate the performance of our
algorithm attained through the argumentation scheme in-
troduced. Given the cooperative scenario reﬂected by our
chosen solution concept we have set aside from the Pareto
optimal instance4 where self-interested agents agree to par-
ticipate in a trade if and only if the contract increases the
agent’s immediate payoﬀ.
Figure 1(a) points out the average percent increase in so-
cial welfare, that the system manages to attain from an ini-
tial state to a stable one, achieved during the course of the
adaptation phase. A stable conﬁguration of the system is
abruptly reached, meaning that the agreements realized ear-
lier improve the social welfare more than the ones performed
later. Furthermore, the solution applied is an anytime algo-
rithm that achieves a monotonic improvement of the global
(social) welfare of the system
Subsequently we perform a series of experiments to draw
more insight to the solution concept introduced.
On one
hand, our negotiation scheme implies that deviations would
only occur if a certain minimum gain τ has been achieved.
On the other hand, the extent to which a coalition is willing
to decrease its eﬃciency in detriment of the gain in social
welfare is represented by a satisfactory parameter µ. This
represents in eﬀect a percentage, which deﬁnes what an ac-
ceptable performance would be and how tolerant is one coali-
tion towards suboptimal performance. For our simulations
we chose an initial value of 0.4 and considered a homogenous
population of actors in the system. Although this does not
make the objective of our scenario, heterogeneity amongst
the actors involved may as well be introduced.
Following, we analyzed the implications of the dependency
on this parameter for a better understanding of its func-
tionality. Thus, we have analyzed the stationary states the
system falls into as a function of µ. For large values of µ,
4Represented in the graphs as the individualistic approach.
meaning that coalitions are willing to signiﬁcantly decrease
their utility with respect to the improvement of the global
welfare of the system, we encountered an expected global
increase in utility, but a considerable variation in the alloca-
tion of utilities in the system. Figure 1(b) illustrates a his-
togram representation of the coalitions’ utilities discretised
in increasing order of their worth. It can be seen that a 20%
increase of µ reduced signiﬁcantly the number of coalitions
operating at high eﬃciency denoted by the last column of the
histogram, while the number of coalitions operating at lower
levels of eﬃciency has been increased. The results empha-
sized that the best performance of the system was obtained
for values of µ in the vicinity of 0.2 . Somewhat surprisingly,
what the experiments show is that being willing to accept
lower eﬃciencies in the beneﬁt of the global performance is
only advantageous to a certain extent. In actuality, there is
a trade-oﬀto be taken into account. Although the overall
system utility increases, the ratio between the number of
coalitions with low utility and those with high utility is in-
creasing as well. So, for assesing the eﬃciency of the system
not only should we be interested in the global utility, but
also in having a uniform distribution of high utilities for the
majority of the coalitions.
Future work will further look to a greater extent at the
electrical features of the power system and incorporate in
a more factual form load-ﬂow computation analyses, that
veriﬁes for contingencies and maintains the system within
its operational limits.
6.
CONCLUSIONS
As a proof of concept our work has introduced a dy-
namic coalition-based model deployed in distributed envi-
ronments of negotiating agents. The formation and adapta-
tion mechanism introduced perform an open-ended adapta-
tion of groups of organizational agents, converging towards
stable conﬁgurations. In particular, we have highlighted the
applicability of this approach through the design of a dis-
tributed adaptive scheme for the smart electricity grid.
7.
REFERENCES
[1] S. D. J. Mcarthur, E. M. Davidson, V. M. Catterson,
A. L. Dimeas, N. D. Hatziargyriou, F. Ponci, and
T. Funabashi. Multi-agent systems for power
engineering applications - part i: Concepts, approaches,
and technical challenges. Power Systems, IEEE
Transactions on In Power Systems, IEEE Transactions
on, Vol, 22(4):1743–1752, 2007.
[2] M. Osborne and A. Rubinstein. A Course in Game
Theory. MIT Press, 1994.
[3] J. Oyarzabal, J.; Jimeno, J. Ruela, and C. Engler,
A.and Hardt. Agent based micro grid management
system. International Conference on Future Power
Systems, 18(18), Nov 2005.
[4] M. Pielke, M. Troschel, M. Kurrat, and H.-J.
Appelrath. Operation strategies to integrate chp micro
units in domestic appliances into the public power
supply. Proceedings of the VDE-Kongress, 2008.
[5] D. Pudjianto, C. Ramsay, and G. Strbac. Virtual power
plant and system integration of distributed energy
resources. Renewable Power Generation IET(1), pages
10–16, 2007.
View publication stats
