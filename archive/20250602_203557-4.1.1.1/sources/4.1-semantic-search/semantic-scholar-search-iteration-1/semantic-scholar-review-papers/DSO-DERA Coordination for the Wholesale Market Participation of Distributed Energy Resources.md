

---

Page 1

---

arXiv:2211.16585v1  [eess.SY]  29 Nov 2022
1
DSO-DERA Coordination for the Wholesale Market
Participation of Distributed Energy Resources
Cong Chen, Subhonmesh Bose, and Lang Tong
Abstract—We design a coordination mechanism between a
distribution system operator (DSO) and distributed energy re-
source aggregators (DERAs) participating directly in the whole-
sale electricity market. Aimed at ensuring system reliability
while providing open access to DERAs, the coordination mech-
anism includes a forward auction that allocates access limits
to aggregators based on aggregators’ bids that represent their
beneﬁts of aggregation. The proposed coordination mechanism
results in decoupled DSO and DERAs operations that satisfy
the network constraints, independent of the stochasticity of the
renewables, wholesale real-time locational marginal prices, and
individual DERA’s aggregation policy. Optimal bidding strategies
by competitive aggregators are also derived. The efﬁciency of the
coordination mechanism and the locational price distribution at
buses of a radial distribution grid are demonstrated for a 141-bus
radial network.
Index Terms—DER aggregation, behind-the-meter distributed
generation, network access allocation mechanism.
I. INTRODUCTION
The landmark ruling of the Federal Energy Regulatory
Commission (FERC) Order 2222 aims to remove barriers to
the direct participation of distributed energy resource aggrega-
tors (DERAs) in the wholesale market operated by Regional
Transmission Organizations and Independent System Opera-
tors (RTO/ISO) [1]. Since DERs are situated in the distribution
systems, services procured from aggregated DERs must pass
through the distribution grid operated by a distribution utility
or a distribution system operator (DSO1). To this end, a DSO-
DERA coordination mechanism is necessary to ensure system
reliability on the one hand and open access for all DERAs
on the other. FERC Order 2222 recognizes the signiﬁcance
of DSO-DERA coordination but leaves the speciﬁcs of the
coordination to the utility, DERAs, and the regulators.
DSO-DERA coordination poses signiﬁcant theoretical, prac-
tical, and economic challenges. Power injections and with-
drawals from DERs will likely depend on the wholesale market
condition (such as locational marginal prices and real-time
needs for regulation services) and the available resources (e.g.,
behind-the-meter renewables). Yet, with DER and wholesale
price uncertainties, the DSO must ensure the safe operation of
the distribution grid to reliably deliver power to all customers
of the distribution utility and the DERAs. Any coordination
mechanism that the DSO adopts must provide open and
equitable access to multiple competing DERAs operating over
Cong Chen and Lang Tong ({cc2662, lt35}@cornell.edu) are with the School of
Electrical and Computer Engineering, Cornell University, Ithaca NY, USA. Subhonmesh
Bose (boses@illinois.edu) is with the Department of Electrical and Computer Engineering
at the University of Illinois Urbana-Champaign (UIUC), Urbana IL, USA.
1Herein, we assume that the DSO is either the utility or an independent
entity that operates the distribution system.
the same distribution network. By equitable access in this
context, we mean that the mechanism cannot discriminate
among the DERAs in how they participate or are compensated.
DSO-DERA-ISO coordination is being actively debated
since the release of FERC Order 2222. In [2], coordination
models have been classiﬁed into four categories, ranging
from the least to the most DSO involvement. Type I models
assume no DSO control (e.g., see [3]–[5]), and installed DER
capacities are deemed to lie within the network’s hosting
capacity limits. As a result, system reliability is guaranteed for
arbitrary power injection/withdrawal proﬁles from DERs. Type
II models explicitly consider the randomness of power injec-
tions from DERs, where the DSO strives to prevent constraint
violations, e.g., see [6]. Type III models involve coordination
between the DSO and the ISO, where DERAs can also provide
distribution grid services besides wholesale market products.
Type IV models require DERA aggregation through the DSO,
with DSO performing all reliability functions and participating
in the wholesale market on behalf of DERAs as in [7]–[9].
Fig. 1. Power ﬂow, ﬁnancial ﬂow and control interactions in the DERA-DSO
coordination model.
We propose a type-II DSO-DERA coordination mechanism
under the generic interaction model among DSO, RTO/ISO,
and multiple DERAs, as shown in Fig. 1 from [5], where
DERAs and DSO operate independently under clearly deﬁned
operational limits to ensure system reliability. In particular,
the access limit of each DERA is allocated through a forward
auction of available network capacities based on DERAs’
bids and offers ahead of the actual operation. The forward
auction present in Section II is constructed such that system
operation constraints are not violated as long as each DERA
aggregates within its cleared access limits. Each DERA then
exercises its aggregation and wholesale market participation
policies subject to the allocated access limits. We formulate a


---

Page 2

---

2
DERA’s proﬁt maximization problem from DER aggregation
in Section III and compute a DERA’s optimal bid in the
access limit allocation problem. There is no need for DSO
intervention in the ISO dispatch of a DERA in our model as
long as the DER injections from DERA customers respect the
access limit that the DERA procures from the DSO. Thus, our
mechanism entails “minimal” DSO-DERA interaction based
on physical network constraints and DERAs’ economic incen-
tives. Furthermore, the DSO does not need to know DERAs’
aggregation strategies and customer preferences. Likewise,
when designing and executing an aggregation policy, a DERA
does not need to be aware of the network constraints and other
DERAs’ models. Despite the minimal interaction between
the DSO and the DERAs, our design guarantees distribu-
tion system constraint enforcement. In addition, numerical
experiments in Section IV reveal that the social surplus of
the market increases with more customers switching from
incumbent distribution utilities to DERAs, making our design
aligned with the spirit of FERC Order 2222.
We remark that our proposed DSO-DERA coordination
mechanism may appear similar to the transmission right
allocation problem for participants with bilateral contracts
considered in the early years of wholesale market deregulation.
Allocating physical transmission rights was deemed impracti-
cal nor necessary (see [10]) with the “loop-ﬂow” problem in
meshed transmission networks. Ultimately, wholesale markets
evolved to adopt a centrally coordinated economic dispatch
run by the ISO, where bilateral transactions came to be hedged
using ﬁnancial transmission rights–an electricity derivative. In
our coordination mechanism, on the other hand, the access
limit allocation is physical, allowing DERAs to inject or
withdraw any amount of power within their purchased access
limits. The loop-ﬂow problem does not affect our design,
thanks to the radial nature of distribution networks. Also, we
deliberately separate the access limit allocation from dispatch
decisions; we envision the auction for access limits to run
only once every day or week. We posit that tight coordination
of dispatch decisions via a centralized market mechanism
matched to that operated by the ISO may be impractical in
the near term and possibly unnecessary, owing to smaller
trade volumes and less stringent system constraints in the
distribution grid.
II. DSO’S ACCESS ALLOCATION MECHANISM
We consider a mechanism where the DSO auctions off
accesses across the distribution network to the DERAs.
Consider K DERAs operating over a distribution network
across N buses. Let the power injection proﬁle from DERA k
across the network be given by pk ∈RN. Thus, the collection
of DERAs inject p := PK
k=1 pk amount of real power. Let the
power injection proﬁle from the utility’s customers be given
by p0 ∈RN. Assuming a uniform power factor for all power
injections, the reactive power injection proﬁle is given by
α(p+p0). These real and reactive power injections then induce
power ﬂows and voltage magnitudes over the distribution
network that are related via the power ﬂow equations. In this
work, we adopt a linear distribution power ﬂow (LinDistFlow)
model [11] that relates the power ﬂows f ∈RN−1 over the
distribution lines and the voltage magnitudes v ∈RN−1 via
f
v

=
Afp
Afq
Avp
Avq
  p + p0
α(p + p0)

= A(p + p0).
(1)
The derivation of A for the LinDistFlow model is included
in the appendix. The power ﬂows and the voltage magnitudes
must remain within the engineering limits of the network, as
b⊺:= (f ⊺, v⊺)⊺≤(f ⊺, v⊺)⊺≤(f
⊺, v⊺)⊺:= b
⊺.
(2)
With this power ﬂow model in hand, we now describe the
network access auction mechanism that the DSO runs. Notice
that we expect that the auction will take place once every day
or week. As a result, the DSO must account for a variety
of operating conditions over the horizon so that the results
of the auction remain binding. Let DERA k provide a bid,
ϕk : RN×N →R, to acquire the access to an injection
capacity Ck ∈RN and a withdrawal capacity Ck ∈RN
with the understanding that all power injections from assets
controlled by DERA k must respect pk ∈[Ck, Ck]. Deﬁne
C := (Ck), C := (Ck) as the matrices collecting access lim-
its across DERAs. Let (C
max
k , C
max
k ) be the maximum injection
and withdrawal capacities that DERA k decides to purchase.
Let the utility’s own customers have net power injections p0
that take values in the set [p0, p0]. Given these ranges of the
various power injections, the DSO solves the following robust
optimization to clear the forward auction allocating accesses
for the distribution network capacities to each DERA.
maximize
C,C,P ,P
K
X
k=1
ϕk(Ck, Ck) −J(P , P ),
such that
0 ≤Ck ≤C
max
k ,
C
max
k ≤Ck ≤0,
P =
K
X
k=1
Ck + p0,
P =
K
X
k=1
Ck + p0,
p =
K
X
k=1
pk,
b ≤A(p + p0) ≤b,
for all pk ∈[Ck, Ck], p0 ∈[p0, p0].
(3)
Here, the functions ϕk are the induced utilities from DERA
k. The offer formation is described in the next section. P and
P respectively represent the total injection and withdrawal
capacity at each bus. And the function, J : RN×N →R, is
the operation cost of DSO including reactive power support,
network maintenance, etc. The problem in (3) enforces the
engineering constraints of the grid for every possible power
injection proﬁle from the utility’s customers and those of
all DERAs within their acquired capacities. This problem
is a robust linear program with a continuum of constraints.
However, the rectangular nature of the constraint sets for the
variables pk’s and p0 allow an easy reformulation. We rewrite


---

Page 3

---

3
A = A+−A−, where the entries of the matrices on the right-
hand side are constructed out of the positive and negative parts
of the respective entries of A.
maximize
C,C,P ,P
K
X
k=1
ϕk(Ck, Ck) −J(P , P ),
such that
0 ≤Ck ≤C
max
k ,
C
max
k ≤Ck ≤0,
λ :
P =
K
X
k=1
Ck + p0,
λ :
P =
K
X
k=1
Ck + p0,
µ :
A+P −A−P ≤b,
µ :
A+P −A−P ≥b.
(4)
Here, the objective function represents the social surplus, i.e.,
S(C, C, P , P ) :=
K
X
k=1
ϕk(Ck, Ck) −J(P , P ).
(5)
which is the surplus of all DERAs minus the operation cost of
DSO for a certain injection/withdrawal access allocation. As-
sociate Lagrange multipliers with the constraints as indicated
above. We deﬁne the locational allocation price as follows.
Deﬁnition 1 (Locational Allocation Prices). Optimal dual
solutions λ
⋆∈RN, λ⋆∈RN of (4), respectively, deﬁne the
vector of locational injection and withdrawal allocation prices
for DERAs at different buses.
These prices are uniform at each distribution bus and hence,
do not discriminate among DERAs that operate at the same
bus. The prices, however, may differ with location in the
distribution network. Given these prices, DERA k with DER
allocations C
i
k, Ci
k at bus i pays the DSO C
i
kλ
⋆
i −Ci
kλ⋆
i .
One can view our auction pricing as a special case of
marginal pricing as follows. To that end, let ǫ denote the
injection access imbalance, given by P −(PK
k=1 Ck+p0) = ǫ.
(Similarly, the withdrawal access imbalance ǫ.) Then, consider
(4) with the ǫ-perturbed access imbalance equations, and its
optimal social surplus S∗(ǫ, ǫ). With this notation, we have
the following result.
Proposition 1. The locational allocation prices satisfy
λ
⋆= ∇ǫS⋆(0, 0) = ∇P J(P
⋆, P ⋆) + A⊺
+µ⋆−A⊺
−µ⋆,
λ⋆= ∇ǫS⋆(0, 0) = ∇P J(P
⋆, P ⋆) −A⊺
−µ⋆+ A⊺
+µ⋆.
Proof of the above proposition follows the envelope theorem
for the ﬁrst equal sign and KKT conditions of (4) for the
second equal sign. Details are illustrated in the appendix.
Assume that DSOs adopt operation cost J that is uniform
across all buses, and DERAs are homogeneous over different
buses. Then, if no line capacity and voltage constraints bind at
an optimal solution of (4), the access prices become uniform
across the network.
III. BIDS AND OFFERS FROM PROFIT-SEEKING DERAS
We now explain the offer formation for the induced beneﬁt
functions ϕk of DERA k. All variables and parameters in this
section are associate with DERA k, and we omit subscript
k for simplicity. DERAs construct their bids for the network
access auction by maximizing their proﬁts assuming forecast
available renewable.
We ﬁrst extend the DER aggregation approach in [5] to the
case with injection access constraints for the optimal decision-
making of DERA with the aggregated prosumers. With this
injection access-constrained optimization, we compute the op-
timal bids ϕ from DERA to the forward auction (4) allocating
network accesses.
A. Proﬁt Maximizing DER Aggregation
We consider the case that DERA maximizes her own
surplus, while providing ζ > 1 times those surpluses to the
aggregated customers she serves than the utility’s rate for
distributed generation (DG). This section is an extension of
the DER aggregation approach in [5] to the case with injection
access constraints. Without loss of generality, we assume
each bus has one prosumer, thus the DERA aggregating N
prosumers will need to have injection/withdrawal accesses for
these N buses. DERA receives payment ωi ∈R from each
prosumer indexed by i and directly buys or sells its aggregated
energy in the wholesale market with the locational marginal
price πLMP ∈R. To maximize DERA surplus between the
received payment and the payment to the wholesale market,
DERA uses the optimization below.
ϕ(C, C) =maximum
ω,d
N
X
i=1
(ωi −πLMP(di −ri)),
such that
ζSi
NEM(ri) ≤U i(di) −ωi,
di ≤di ≤d
i,
Ci ≤ri −di ≤C
i,
i = 1, . . . , N.
(6)
The ﬁrst constraint encodes the competitive nature of
DERA, which guarantees that the prosumer surplus is at least
ζ times the surplus under the net energy metering (NEM X).
Explicit formulation of prosumer surplus Si
NEM(ri) is shown in
the appendix. The second constraint is prosumer consumption
limits, and the last constraint is injection and withdrawal
access limits.
B. Beneﬁts of Aggregation and Bid Formation
The following proposition introduces the optimal closed-
form solution of (6). The optimal DERA surplus is decom-
posed into three terms, the surplus dependent on the withdraw
access ϕi(Ci), the surplus dependent on the injection access
ϕi(Ci), and the surplus independent of the network access
hi −ζSi
NEM(ri).
Proposition 2 (Optimal DERA Decision). The optimal solu-
tion of (6) is given by
di⋆(πLMP, ri) = min{ri −Ci, max{ ˆdi, ri −C
i}},
ωi⋆(di⋆, ri) = U i(di⋆) −ζSi
NEM(ri),
(7)


---

Page 4

---

4
where ˆdi := min{d
i, max{(V i)−1(πLMP), di}}.
The optimal DERA surplus is given by
ϕ(C, C) =
N
X
i=1
ϕi(Ci) +
N
X
i=1
ϕi(C
i)
(8)
+
N
X
i=1
(hi −ζSi
NEM(ri)),
where hi := U i( ˆdi) −πLMP( ˆdi −ri),
ϕi(Ci) :=
(
U i(ri −Ci) + πLMPCi −hi,
if ri ≤qi
+,
0,
otherwise,
ϕi(C
i) :=
(
U i(ri −C
i) + πLMPC
i −hi,
if qi
−≤ri,
0,
otherwise,
qi
−:= C
i + max{(V i)−1(πLMP), di},
qi
+ := Ci + min{(V i)−1(πLMP), d
i}.
The proof follows the Karush-Kuhn-Tucker optimality con-
ditions for (6) (see appendix for details). When there’s no
binding constraints for network access limits, ˆdi is the optimal
consumption of prosumer i, and hi −ζSi
NEM(ri) is the beneﬁt
of DERA from prosumer i. When there’s binding network ac-
cess constraints, the optimal consumption di⋆(πLMP, ri) equals
to ˆdi truncated by the network access limits, and beneﬁt of
DERA is modiﬁed by ϕi(C
i) and ϕi(Ci).
We remark that the optimal DERA beneﬁt ϕ(C, C) is
separable across injection and withdrawal access, and across
prosumers at different distribution buses. Furthermore, at most
one of ϕi(C
i) and ϕi(Ci) can be nonzero, depending upon
the renewable generation ri for prosumer i. When ri ≤qi
+,
ϕi(Ci) is nonzero and prosumer at bus i is a consumer with
binding network withdrawal access constraints; when qi
−≤ri,
ϕi(C
i) is nonzero and prosumer at bus i is a producer with
binding network injection access constraints.
Therefore, DERA can construct its bids for injection and
withdrawal access as ϕi(C
i) and ϕi(Ci) at different buses.
In practice, piece-wise linear apprixmations of those bids are
needed to be included in the access auction problem (4).
IV. NUMERICAL EXPERIMENTS
We considered a 141-bus radial distribution network with 4
DERAs who aggregate households at different buses with dif-
ferent levels of behind-the-meter distributed generation (BTM
DG). Parameters for resistances and reactances of this system
are taken from [12], [13]. We assumed ﬁxed power factor of
0.98 across all buses and set line ﬂow limit of 15MW for the
ﬁrst 6 branches, consecutively connected to the substation bus,
and 2MW for the rest. All 4 DERAs aggregate resources from
all buses, except that DERA 4 only aggregates over buses 118-
134. The BTM DG for households under DERA 1, 2, 3, and 4
are respectively, 0.2kW, 5.2kW, 10.2kW, and 15.2kW. We set
maximum access limits for all DERAs,i.e., C
max
k , C
max
k , equal
to 0.1 MW. We adopted a quadratic cost for the DSO of the
form J(x) = 1
2bx2 −ax with a = −0.096, b = 0.2.
We used homogeneous utility functions for households [14],
U(x) =
(
ˆax −
ˆb
2x2,
0 ≤x ≤ˆa
ˆb ,
ˆa2
2ˆb ,
x > ˆa
ˆb ,
with ˆa = 0.65,ˆb = 0.2. The percentage of DG adopters
over all households is assumed 80%. For NEM X tariff, we
used π0 = $0, π+ = π−+ $0.03/kWh, ζ = 1.003, and the
wholesale market LMP πLMP = $0.03/kWh [15].
The supply offers can be constructed from (8). We plot here
instead the marginal beneﬁts ϕi,′
k , ϕi,′
k in Fig. 2 with varying
BTM DG generations. The left panel illustrates that DERAs
with lower DG levels choose higher bid prices to purchase
withdrawal access. The right panel shows that DERAs with
higher DG choose higher prices for injection, rather than
withdrawal, access.
-4
-3
-2
-1
0
1
Withdraw access (MW)
0
0.2
0.4
0.6
Mariginal benefit($/MWh)
r=0.2
r=1.2
r=2.2
-1
0
1
2
3
4
Injection access (MW)
0
0.2
0.4
Mariginal benefit($/MWh)
r=3.2
r=4.2
r=5.2
Fig. 2.
Left: Bid-in marginal beneﬁt vs withdrawal access. Right: Bid-in
marginal beneﬁt vs injection access.
0
20
40
60
80
100
120
140
Bus
-0.1
0
0.1
0.2
Access clearing results (MW)
-1
0
1
2
Access price ($/MW)
Fig. 3. Market clearing results of network access.
Results of DSO’s auction with the 4 DERAs is illustrated
in Fig. 3. The positive and negative segments of the left y-axis
respectively represent the allocated injection and withdrawal
ranges. DERA 1 has low DG levels, and behaves as a net
consumer, who bids for and receives withdrawal access. Fig. 3
shows that DERA 1 received withdrawal security operating
range [0, 0.1] MW over most buses. DERAs 2, 3 and 4 largely
act as net producers of power, and they therefore purchase
injection access through the auction. A DERA with higher
DG level has higher marginal surplus for injection access.
One expects this higher marginal surplus to lead to higher
clearing prices for injection. Not surprisingly, buses 118-
134 with DERA 4 exhibit the highest levels of λ
i. Also,
binding line and voltage limits cause access prices to vary
with location. We indeed observe this effect for λi, λ
i across
all buses consecutively connected to buses 28-32, 52, 86-87,
130, and 140-141, which have binding voltage constraints.
Locational allocation prices are gradually increasing along the
branch until reaching the bus with binding voltage constraint.
The left panel of Fig. 4 shows a normalized version of
the social surplus S. Here, S increases, when the ratio of
DERA customer increases, or when DG level increases. To


---

Page 5

---

5
uncover the reason behind such phenomenon, notice that the
ﬁrst constraint of DERA aggregation model (6) schedules its
customers at a demand level with higher surplus compared
to the distribution utility with NEM X tariff. With more
customers switching from the distribution utility to DERAs,
the total social surplus for in the DSO’s auction increases.
1
1
1.5
Social surplus
Ratio of DERA customer
4.5
0.5
2
Renewable (kW)
5
5.5
6
1
0.005
0.01
DERA profit
0.015
Ratio of DERA customer
0.02
Renewable (kW)
0.5
5
6
Fig. 4. Left: social surplus. Right: DERA surplus.
The right panel of Fig. 4 reveals that the total surplus of all
DERAs decreases with increasing DG, it increases with the
ratio of DERA customer base. Since NEM X provides higher
surplus to customers with higher DG, as noted in [16], DERAs
must commensurately reduce their own proﬁts and share them
with the customers to remain competitive with NEM X.
V. CONCLUSIONS
This paper proposes a distribution network injection access
allocation mechanism for DSO to allocate its network injection
access to multiple DERA participants. Such a mechanism
offers a simple decomposition for DERA-DSO coordination.
DSO can guarantee voltage and line ﬂow security for the
distribution network when the DERAs guarantee that power
injections respect DSO’s injection access allocation. Such
an allocation mechanism runs once every day or week, and
gives more freedom to DERAs to coordinate the decentralized
aggregation of prosumers’ assets.
We also derived optimal bid curves for DERAs to participate
in the forward auction for distribution network accesses, when
DERAs offer compensations that are competitive with respect
to distribution tariff structures such as those for NEM. Through
numerical experiments, we observed that DERAs with higher
BTM generation generally bid higher for injection access
than those with lower generation. DERAs with lower BTM
generation tend to bid higher for withdrawal access. We also
observed that. the social surplus of the retail market increases
with more customers switching from incumbent DSO utility
companies to DERAs.
REFERENCES
[1] FERC. (2020) Participation of distributed energy resource aggregations
in
markets
operated
by
regional
transmission
organizations
and
independent system operators, order 2222. 2020. [Online]. Available:
https://www.ferc.gov/sites/default/ﬁles/2020-09/E-1 0.pdf
[2] A.
Renjit,
“TSO-DSO
coordination
frameworks,
2021
PSERC
summer
workshop,”
See
also
TSO-DSO
Coordination
Functions
for DER, 2022. [Online]. Available: https://www.epri.com/research/
products/000000003002016174
[3] K. Alshehri, M. Ndrio, S. Bose, and T. Bas¸ar, “Quantifying market
efﬁciency impacts of aggregated distributed energy resources,” IEEE
Transactions on Power Systems, vol. 35, no. 5, pp. 4067–4077, 2020.
[4] Z. Gao, K. Alshehri, and J. R. Birge, “On efﬁcient aggregation of dis-
tributed energy resources,” in 2021 60th IEEE Conference on Decision
and Control (CDC).
IEEE, 2021, pp. 7064–7069.
[5] C. Chen, A. S. Alahmed, T. D. Mount, and L. Tong, “Competitive
der aggregation for participation in wholesale markets,” in Proc. 2023
Hawaii Intl Conf. Syst. Sci. [Online preprint] arXiv:2207.00290, 2022.
[6] N. Nazir and M. Almassalkhi, “Grid-aware aggregation and realtime
disaggregation of distributed energy resources in radial networks,” IEEE
Transactions on Power Systems, vol. 37, no. 3, pp. 1706–1717, 2021.
[7] “Who
are
controlling
the
DERs?
increasing
DER
hosting
capacity
through
targeted
modeling,
sensing,
and
control,”
2022. [Online]. Available: https://documents.pserc.wisc.edu/documents/
publications/reports/2022 reports/T 64 Final Report
1 .pdf
[8] X. Chen, E. Dall’Anese, C. Zhao, and N. Li, “Aggregate power ﬂexibility
in unbalanced distribution systems,” IEEE Transactions on Smart Grid,
vol. 11, no. 1, pp. 258–269, 2019.
[9] M. Mousavi and M. Wu, “A DSO framework for market participation
of DER aggregators in unbalanced distribution networks,” IEEE Trans-
actions on Power Systems, vol. 37, no. 3, pp. 2247–2258, 2021.
[10] W. W. Hogan, “Contract networks for electric power transmission,”
Journal of regulatory economics, vol. 4, no. 3, pp. 211–242, 1992.
[11] M. Baran and F. F. Wu, “Optimal sizing of capacitors placed on a radial
distribution system,” IEEE Transactions on power Delivery, vol. 4, no. 1,
pp. 735–743, 1989.
[12] H. Khodr, F. Olsina, P. De Oliveira-De Jesus, and J. Yusta, “Maximum
savings approach for location and sizing of capacitors in distribution
systems,” Electric power systems research, vol. 78, no. 7, pp. 1192–
1203, 2008.
[13] “MATPOWER data case141,” 2020. [Online]. Available: https://github.
com/MATPOWER/matpower/blob/master/data/case141.m
[14] P. Samadi, H. Mohsenian-Rad, R. Schober, and V. W. S. Wong,
“Advanced demand side management for the future smart grid using
mechanism design,” IEEE Transactions on Smart Grid, vol. 3, no. 3,
pp. 1170–1180, 2012.
[15] “CAISO price map,” 2022. [Online]. Available: https://www.caiso.com/
todaysoutlook/Pages/prices.html
[16] A. S. Alahmed and L. Tong, “On net energy metering x: Optimal pro-
sumer decisions, social welfare, and cross-subsidies,” IEEE Transactions
on Smart Grid, 2022.
VI. APPENDIX
A. Prosumer Under NEM X Tariff
We explain the optimal decision-making for prosumers with
the behind-the-meter distributed generation (BTM DG) under
net energy metering (NEM X) from the incumbent utility
company. More details and variants of the optimal prosumer
decisions are explained in [5].
Consider a prosumer with energy consumption d ∈R+ and
renewable generation r ∈R+. Assume that the prosumer’s
utility, U : R+ →R, is strictly concave, monotonically in-
creasing, and continuously differentiable with marginal utility
function V := U ′ invertible over [0, +∞). Prosumer index i
is dropped here for simplicity.
We assume that prosumer consumption is independent of the
DG output r, i.e., all generation is used for bill reductions.
The NEM-X tariff is utilized for the retail rate, which is
parameterized by π = (π+, π−, π0) as in [16]. π+ ∈R is
the retail (consumption) rate, π−∈R is the sell (production)
rate, and π0 ∈R is the connection charge. The optimal
consumption of this prosumer is given by
dNEM = argmax
d≤d≤d
 U(d) −π+d

.
(9)
So, we have dNEM = min{d, max{V −1(π+), d}}. The
optimal prosumer surplus is given by
SNEM(r) =
(
U(dNEM) −π−(dNEM −r) −π0,
if r ≥dNEM,
U(dNEM) −π+(dNEM −r) −π0,
otherwise.


---

Page 6

---

6
B. Proof of Proposition 1
We use the envelope theorem to prove the ﬁrst equal sign
and use KKT conditions of (4) for the second equal sign.
Consider (4) with the ǫ-perturbed access imbalance equa-
tions, the optimal social surplus S⋆(ǫ, ǫ) can be computed by
S⋆(ǫ, ǫ) =maximize
C,C,P ,P
K
X
k=1
ϕk(Ck, Ck) −J(P , P ),
such that
(η, η) :
0 ≤Ck ≤C
max
k ,
(ξ, ξ) :
C
max
k ≤Ck ≤0,
λ :
P −(
K
X
k=1
Ck + p0) = ǫ,
λ :
P −(
K
X
k=1
Ck + p0) = ǫ,
µ :
A+P −A−P ≤b,
µ :
A+P −A−P ≥b.
(10)
The Lagrangian function of (10) is
L(C, C, P , P , λ, λ, µ, µ) = J(P , P ) −PK
k=1 ϕk(Ck, Ck)
+ λ
⊺(ǫ −(P −(PK
k=1 Ck + p0))) + η⊺(−Ck)
+ η⊺(Ck −C
max
k ) + λ
⊺(ǫ −(P −(PK
k=1 Ck + p0)))
+ µ⊺(A+P −A−P −b) + µ⊺(A+P −A−P −b)
+ ξ⊺(C
max
k −Ck) + ξ⊺(Ck).
(11)
By envelope theorem ∇ǫL⋆= ∇ǫS⋆, ∇ǫL⋆= ∇ǫS⋆.
And we know that ∇ǫL⋆= λ
⋆, ∇ǫL⋆= λ⋆. The locational
allocation price for DERA injection is solved at ǫ = 0, ǫ = 0.
So, we have λ
⋆= ∇ǫS⋆(0, 0), λ⋆= ∇ǫS⋆(0, 0).
KKT conditions of (4) gives
∇P L⋆= ∇P J(P
⋆, P ⋆) −λ
⋆+ A⊺
+µ⋆−A⊺
−µ⋆= 0,
∇P L⋆= ∇P J(P
⋆, P ⋆) −λ⋆−A⊺
−µ⋆+ A⊺
+µ⋆= 0.
(12)
So, we have λ
⋆= ∇P J(P
⋆, P ⋆)+A⊺
+µ⋆−A⊺
−µ⋆= 0, and
λ⋆= ∇P J(P
⋆, P ⋆) −A⊺
−µ⋆+ A⊺
+µ⋆.
C. Proof of Proposition 2
We prove this proposition with KKT conditions of (6), and
the inventory calculation with the optimal solution.
Assign dual variables to (6), we have
ϕ(C, C) =maximum
ω,d
N
X
i=1
(ωi −πLMP(di −ri)),
such that
χi :
ζSi
NEM(ri) ≤U i(di) −ωi,
(νi, νi) :
di ≤di ≤d
i,
(γi, γi) :
Ci ≤ri −di ≤C
i,
i = 1, . . . , N.
(13)
From KKT conditions of (13), we have ∀i = 1, ..., N
∂L
∂ωi = χi⋆−1 = 0,
∂L
∂di = πLMP −χi⋆V i(di∗) −νi⋆+ νi⋆+ γi⋆−γi⋆= 0.
(14)
Combined with the complementary slackness condition, the
ﬁrst constraint of (13) is always binding with χi⋆= 1, and the
optimal consumption di⋆equals to (V i)−1(πLMP) if it falls into
the interval of the minimum upper bound min{d
i, ri−Ci} and
maximum lower bound max{di, ri −C
i}. So we have
di⋆(πLMP, ri) = min{ri −Ci, max{ ˆdi, ri −C
i}},
(15)
ωi⋆(di⋆, ri) = U i(di⋆) −ζSi
NEM(ri),
(16)
where ˆdi := min{d
i, max{(V i)−1(πLMP), di}}.
When (V i)−1(πLMP) ≥min{d
i, ri −Ci} = ri −Ci,
we
have ri ≤Ci + min{d
i, (V i)−1(πLMP)}. The optimal value
can be computed by
ϕ(C, C) =
N
X
i=1
(ωi⋆−πLMP(di⋆−ri))
=
N
X
i=1
(U i(ri −Ci) −ζSi
NEM(ri) −πLMP(ri −Ci −ri))
=
N
X
i=1
(U i(ri −Ci) + πLMPCi −ζSi
NEM(ri)).
(17)
When (V i)−1(πLMP) ≤max{di, ri −C
i} = ri −C
i,
we
have ri ≥C
i + max{di, (V i)−1(πLMP)}. The optimal value
can be computed by
ϕ(C, C) =
N
X
i=1
(ωi⋆−πLMP(di⋆−ri))
=
N
X
i=1
(U i(ri −C
i) −ζSi
NEM(ri) −πLMP(ri −C
i −ri))
=
N
X
i=1
(U i(ri −C
i) + πLMPC
i −ζSi
NEM(ri)).
(18)
In all other cases, the optimal value is given by the equation
below, which is not a function of (C, C).
ϕ =
N
X
i=1
(U i( ˆdi) −ζSi
NEM(ri) −πLMP( ˆdi −ri)).
(19)
Denote that hi := U i( ˆdi) −πLMP( ˆdi −ri),
ϕi(Ci) :=
(
U i(ri −Ci) + πLMPCi −hi,
if ri ≤qi
+,
0,
otherwise,
ϕi(C
i) :=
(
U i(ri −C
i) + πLMPC
i −hi,
if qi
−≤ri,
0
otherwise,
and
(
qi
−:= C
i + max{(V i)−1(πLMP), di},
qi
+ := Ci + min{(V i)−1(πLMP), d
i}.
To sum up over all cases, we have
ϕ(C, C)
=
PN
i=1 ϕi(Ci) + PN
i=1 ϕi(C
i)
+ PN
i=1(hi −ζSi
NEM(ri)).
(20)


---

Page 7

---

7
D. Example of linearized power ﬂow
In this section, we ﬁrst describe parameters for the lin-
earized distﬂow model [11], and then provide a 5-bus example.
Consider a radial distribution networks with N buses. Denote
ui := (vi)2, ∀i ∈{1, ..., N}, and ubase := v2
base. Let the
parent base bus (bus 1) be the reference bus, i.e., v1 = √ubase.
Consider voltage deviation no larger than 5%. Then, with
reduced shift factor matrix ˜S, the bound for voltage in (2)
is given by 2
(
v := 1.05ubase −˜S⊺(:, 1)ubase,
v := 0.95ubase −˜S⊺(:, 1)ubase,
(21)
where we have v := (v2, v3, v4, v5)⊺∈RN−1 , and similarly
v ∈RN−1 ignoring voltage at the reference bus.
Consider a ﬁxed power factor in our model, we have reactive
power injection αp = (α1p1, ..., αnpn, ..., αNpN) at different
buses, given the active power p. The forward auction for
distribution network accesses in (3) uses A represent the shift
factor matrix for voltage and line ﬂow in the linear power ﬂow
model. Detail parameter settings for A is listed below by
A :=
"
0
˜S
0
2 ˜S⊺(R + αX)
#
,
(22)
where R and X are matrices for resistance and reactance.
Fig. 5. 5-bus radial distribution network.
Consider a 5-bus system shown in the following ﬁgure.
Let the parent base bus (bus 1) be the reference bus. With
matrix rows consecutively related to line 2-1, line 5-2, line
3-5 and line 4-5, and matrix columns to bus 1, 2, 3, 4, 5,
the shift factor matrix and reduced shift factor matrix are
S =


0
1
1
1
1
0
0
1
1
1
0
0
1
0
0
0
0
0
1
0

, ˜S =


1
1
1
1
0
1
1
1
0
1
0
0
0
0
1
0

, respectively.
The matrix for resistance and reactance are respectively
R =


r21
r21
r21
r21
0
r52
r52
r52
0
r35
0
0
0
0
r45
0

, X =


x21
x21
x21
x21
0
x52
x52
x52
0
x35
0
0
0
0
x45
0

.
The power ﬂow equation is
2

R
X
  p-1
αp-1

= ( ˜S⊺)−1u-1 −
ubase
0

⇒2 ˜S⊺(R + αX)p-1 + ˜S⊺(:, 1)ubase = u-1,
(23)
2Reduced shift factor matrix is shift factor matrix without the column for
the reference bus.
where p-1 := (p2 + p2
0, p3 + p3
0, p4 + p4
0, p5 + p5
0)⊺, and u-1 :=
(u2, u3, u4, u5)⊺.
Denote f := (f 21, f 52, f35, f45)⊺∈RN−1 for branch ﬂow
limits (similarly f ∈RN−1), and combine (21) and (23), we
have the following equation.
f
v

≤
"
0
˜S
0
2 ˜S⊺(R + αX)
#
(p + p0) ≤
 ¯f
v

,
(24)
which is the explicit form of the power ﬂow constraint in (3),
i.e., b ≤A(p + p0) ≤b.
