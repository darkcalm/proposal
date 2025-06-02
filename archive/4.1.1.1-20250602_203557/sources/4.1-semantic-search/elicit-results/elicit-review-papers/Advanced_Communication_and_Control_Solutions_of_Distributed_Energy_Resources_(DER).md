

---

Page 1

---

PREPRINT
1
Aggregating Privacy-Conscious Distributed Energy
Resources for Grid Service Provision
Jun-Xing Chin, Member, IEEE, Andrey Bernstein, Member, IEEE,
and Gabriela Hug, Senior Member, IEEE
Abstract—The increasing adoption of advanced metering in-
frastructure has led to growing concerns regarding privacy risks
stemming from the high resolution measurements. This has given
rise to privacy protection techniques that physically alter the
consumer’s energy load proﬁle, masking private information by
using localised devices, e.g. batteries or ﬂexible loads. Mean-
while, there has also been increasing interest in aggregating the
distributed energy resources (DERs) of residential consumers to
provide services to the grid. In this paper, we propose an online
distributed algorithm to aggregate the DERs of privacy-conscious
consumers to provide services to the grid, whilst preserving
their privacy. Results show that the optimisation solution from
the distributed method converges to one close to the optimum
computed using an ideal centralised solution method, balancing
between grid service provision, consumer preferences and privacy
protection. More importantly, the distributed method preserves
consumer privacy, and does not require high-bandwidth two-way
communications infrastructure.
Index Terms—Ancillary Services, Consumer Privacy, Online
Gradient Descent, Mutual Information, Optimisation Methods,
Smart Meter, Advanced Metering Infrastructure
I. INTRODUCTION
In recent years, the adoption rate of advanced metering in-
frastructure (AMI) using smart meters (SMs) has risen steadily
across the globe as part of grid modernisation efforts. As of
January 2017, 52% of the 150 million electricity consumers in
the US have AMI [1], while in Europe, 13 member states are
expected to have AMI adoption rates of over 95% by 2020 [2].
In Switzerland, 80% of all electricity meters are to be replaced
with SMs by 2027 [3]. AMI provides high-frequency energy
consumption measurements to utility operators, allowing for
data-driven grid management and planning techniques that
promise to improve grid efﬁciency and transparency. However,
this data also entails serious privacy risks for consumers,
as it reveals their detailed electricity consumption proﬁles.
Recent studies have shown that potential illnesses, religious
practices, socio-demographic proﬁle, and even appliances used
can be inferred from AMI data through data analytics and non-
intrusive load monitoring techniques [4]–[8].
A. Smart Meter Consumer Privacy
These risks and recent developments in consumer privacy
protection laws such as the European Union’s General Data
This work was supported in part by the Swiss National Science Foundation
for the COPES project under the CHIST-ERA Resilient Trustworthy Cyber-
Physical Systems (RTCPS) initiative.
J.X. Chin, and G. Hug are with the Power Systems Laboratory, ETH Zurich,
8092 Zurich, Switzerland. Email: {chin | hug}@eeh.ee.ethz.ch. A. Bernstein
is with the National Renewable Energy Laboratory, Golden, CO 80401, USA.
Email: Andrey.Bernstein@nrel.gov
Protection Regulation [9], have spurred the development of
privacy-enhancing methods for consumers with AMI, which
can be split into two categories: smart meter data manipulation
(SMDM) and user demand shaping (UDS) [10]. SMDM
involves pre-processing the AMI data before it is reported,
e.g., data aggregation, data anonymisation, and data obfus-
cation. UDS, on the other hand, entails physically shaping
the consumer demand such that the grid-visible load, i.e., the
grid load no longer reveals private information present in
the actual privacy-sensitive consumer load. This is achieved
by using behind-the-meter resources such as energy storage
devices, ﬂexible loads, and distributed energy sources. While
the former may be cheaper to implement, they may impact
the utility of the AMI data due to the distortion in the meter
readings or may require trusted third parties, e.g, as proposed
in [11], [12]. Moreover, as they do not tackle the issue on
the physical level, i.e., the actual energy ﬂow, it might be
possible to still decipher the actual consumption depending
on the protection used [13].
One of the ﬁrst UDS schemes is described in [14], where the
authors implement a best effort scheme to keep the grid load
constant. However, this has been shown to leak information
whenever there is a change in grid load [15], and has since
been followed up by more complex schemes such as [16]–
[19]. In [16], the authors propose a differential-privacy based
protection scheme using an ideal battery to mask the on/off
status of appliances while being cost-friendly. Using a model-
distribution predictive control (MDPC) scheme that balances
between minimising energy cost and a proxy for privacy loss,
the authors in [17] show that a home energy controller can
be designed to directly minimise an approximate of mutual
information between the grid and consumer loads. And in
[18], the authors propose Q-learning based privacy-enhancing
control policies using electric vehicles (EVs), ﬂexible thermal
loads, and energy storage devices to overcome limitations in
modelling consumer load statistics. The control policies are
tested on simulated load proﬁles with an ideal battery and
a linearised thermal load model, and show that reasonable
privacy-cost trade-off can be achieved by combining a small
battery with EVs and an air conditioning device. The authors
in [19] derived fundamental bounds on mutual information
privacy for consumers with renewable energy sources (RES),
both with and without an inﬁnite battery, and proposed a sub-
optimal privacy-enhancing scheme for realistic cases (ﬁnite
battery) based on stochastic gradient descent. Note that in the
absence of a battery, privacy can be enhanced through the
curtailment of the available RES production.
arXiv:1909.01215v2  [eess.SY]  26 Oct 2020


---

Page 2

---

PREPRINT
2
B. Residential Demand Side Aggregation and UDS Schemes
Meanwhile, the increasing availability of behind-the-meter
resources, a.k.a. distributed energy resources (DERs), coupled
with the roll-out of smart grid communications infrastructure
has spurred the development of demand-side management for
smaller loads. Residential consumers, which have traditionally
been neglected due to their size, are being aggregated in order
to provide services to the grid. Residential demand side aggre-
gation (RDSA) schemes can be divided into two main classes:
direct load control, and incentive (signal) based schemes. The
authors in [20] provide an overview of incentive based RDSA
literature, and propose a multi-agent non-cooperative game
framework for integrating RDSA schemes with home energy
management systems (HEMSs). Nonetheless, limitations in
communications infrastructure remain a challenge for most
RDSA schemes [21]. One possible solution is the broadcast
of a common signal as suggested in [22], though the design
of the signal is still an active ﬁeld of research; see, e.g., [23]
and pertinent references therein.
UDS privacy protection methods, by their nature, lend
themselves well to being a part of an RDSA scheme given their
inherent ﬂexibility to alter grid load. Moreover, it is intuitive
that privacy-conscious consumers with UDS protection be
considered potential DERs that can be aggregated to provide
services to the grid. However, there are only few works on
the design of privacy-centric HEMSs for RDSA schemes, with
most works focusing solely on the auction activation, or (and)
accounting mechanisms, e.g., [24]–[26]. These works employ
different cryptographic techniques in the RDSA mechanism in
order ensure privacy while being able to attribute rewards to
demand response participants, but do not provide designs for
the automated HEMSs.
C. Contributions and Outline
In this paper, we design a HEMS for RDSA that also
considers the consumers’ preferences and privacy loss due to
high-frequency SM measurements (SM privacy), without the
need for pervasive real-time AMI metering, a trusted third-
party, nor two-way high-bandwidth communications infras-
tructure to each consumer. Using an online projected gradient
descent approach based on the framework in [27] and the SM
privacy protection scheme in [17], the proposed RDSA scheme
preserves the SM privacy of consumers through UDS and
omits the need for real-time information from each consumer.
It is important to note that the allocation of rewards in
RDSA schemes that do not directly control consumer loads
typically rely on benchmarking metered consumption against
historical records. However, in private-by-design RDSA algo-
rithms, save for a totally ﬂat proﬁle, individual benchmark
proﬁles should not be discernible from measured grid-visible
consumer load proﬁles. Otherwise, private information could
be inferred from repeated disclosures of a private, but static
grid-visible load proﬁle. Hence, rewards for participation in a
private-by-design RDSA scheme in the absence of any trusted
party can only be allocated based on the individual consumer’s
resource commitment. While this could result in a free-loader
problem, such as those explored in game theoretic works, the
resolution of this is outside the scope of this paper.
The rest of this paper is organised as follows: Section
II details the problem considered, Section III introduces the
distributed solution method, Section IV presents and discusses
simulation results and Section V concludes the paper, and
presents an outlook for future work.
II. PROBLEM FORMULATION AND SYSTEM DESCRIPTION
We consider the problem of a HEMS that is part of an
RDSA scheme and is required to consider the consumer’s pref-
erences, and also privacy-loss stemming from high-frequency
smart meter measurements. Each consumer household consists
of a DER, an HEMS controller, and a smart meter that is able
to provide high-frequency measurements locally, but unable
or unwilling to provide real-time high-frequency remote mea-
surements to the utility provider or aggregator. The aggregator
could be a distribution system operator or a third-party energy
services provider that has the capability to broadcast high-
speed uni-directional signals to each consumer, and is able to
measure the real-time aggregated energy consumption of its
consumers, e.g., at the sub-station or transformer. The general
aggregator system setup is illustrated in Fig. 1(a). On the
other hand, the adversary considered in the privacy problem
is assumed to be any entity (including an untrusted utility
provider) that has access to the high-frequency smart meter
measurements, i.e., there are no assumed trustworthy parties
to which unprotected data is directly disclosed to. An ideal
solution to the considered problem would directly disclose
only the following data to third-parties:
i. time-delayed high-frequency SM measurements from in-
dividual consumers that are privacy-protected;
ii. real-time high-frequency aggregated consumer consump-
tion measurements at points-of-common-coupling.
Additionally, we consider the case of the DER being a
battery in this paper, but the proposed method can easily be
extended to incorporate other DERs with convex models. Fig.
1(b) illustrates the system considered at each consumer house-
hold. The problem can be framed as solving the following
optimisation program:
minimise
yl
N
X
l=1
{Λ(yl) + µlΦ(yl)} + ρΓ(y)
subject to
yl ∈Fl,
l = 1, . . . , N,
(1)
where N is the number of consumers in the aggregation, yl
and µl are the grid load and price of privacy loss for consumer
l, respectively, Λ(yl) is the consumer’s utility (preference)
function, Φ(yl) is a measure of real time privacy-loss, ρ is the
coefﬁcient for grid service provision, Γ(y) gives a measure of
the grid service provided (e.g., target load or ancillary service
tracking signal), and y := [y1, y2, · · · , yN]T is a vector of
consumer grid loads. The set Fl, deﬁned by the constraints:
0 ≤s+
l ≤s+,max
l
(2)
0 ≤s−
l ≤s−,max
l
(3)
0 ≤el + ∆t(ηls+
l −1
ηl
s−
l ) ≤ecap
l
(4)


---

Page 3

---

PREPRINT
3
Aggregator
Real-time Information Flow
Energy Flow
Privacy 
Aware
Consumers
(a) RDSA Aggregator System
Smart Meter
System
HEMS
Controller
Energy 
Storage
Load
Aggregator
Real-time Information Flow
Energy Flow
(b) Setup at Consumer Household
Fig. 1.
System setup at consumer households and the aggregator system
yl = xl + s+
l −s−
l
(5)
ymin
l
≤yl ≤ymax
l
(6)
enforces the system constraints for consumer l. Here, s+
l , s−
l
denote the battery’s charging and discharging power; s−,max
l
,
s+,max
l
denote the battery’s maximum discharging and charg-
ing power rating; ηl denotes the battery’s charge/discharge
efﬁciency; el is the battery state of charge; ecap
l
is the battery
capacity; ymin
l
and ymax
l
are the minimum and maximum
allowable grid loads; xl denotes the instantaneous consumer
load; and ∆t is the time interval between each control action.
For the rest of the paper, Al denotes a random variable,
al denotes its realisation, log is the base-2 logarithm, At
denotes the sequence (A1, A2, · · · , At), A is the range space
for variable A, and pA(a) is the probability of A = a.
The functions Λ(yl) , Φ(yl) and Γ(y) are described in the
following.
A. Consumer Preferences
The function Λ(yl) can be any convex utility function that
reﬂects the consumer’s preferences. For simplicity, we con-
sider a function that penalises deviations from the consumer’s
day-ahead grid-load schedule, given by
Λ(yl) := ∥yl −yref
l ∥2
2 ,
(7)
where yref
l
is the day-ahead planned consumption. This sched-
ule can include the consumer’s preferences on a grid visible
load proﬁle, energy cost optimisation and battery state-of-
charge requirements.
B. Privacy Loss Proxy
There has yet to be a consensus amongst researchers on the
best measure of privacy loss for consumers with AMI. The
authors in [28] found that the perceived levels of SM privacy
are greatly affected by the different privacy measurement
methods, and that the privacy guarantees given by protection
schemes based on these various methods are also highly
dependent upon the underlying load proﬁles. Nevertheless, one
widely accepted measure for privacy loss stemming from an
adversary that has access to the individual grid-visible load
proﬁles captured by the SMs is mutual information (MI) [10],
[15]. A method to tractably approximate MI in an optimisation
problem for a single consumer is proposed in [17]. In this
work, we adapt the MI approximate developed in [17] as
the privacy loss objective for multiple privacy-conscious con-
sumers in the RDSA scheme. Let Xl ∈Xl and Yl ∈Yl denote
the random variables modelling the instantaneous consumer
load and the total grid load, respectively. For the purpose
of estimating the MI only, we assume that these random
variables are discrete and have ﬁnite support. In particular,
˜
Xl = {x0
l , x1
l , · · · , xm
l }, ˜Yl = {y0
l , y1
l , · · · , yn
l }, where m and
n are the number of bins used to quantise the consumer and
grid loads, respectively, and I(Xl; Yl) ≈I( ˜Xl; ˜Yl). The MI
function for discrete random variables is given by
I( ˜Xl; ˜Yl) :=
X
xl∈˜
Xl
X
yl∈˜
Yl
p ˜
Xl, ˜Yl(xl, yl) log
p ˜
Xl, ˜Yl(xl, yl)
p ˜
Xl(xl)p ˜Yl(yl),
where p ˜
Xl, ˜Yl, p ˜
Xl, and p ˜Yl are the approximated joint and
marginal probability distribution functions (PDFs) of the
random variables. In order to formulate MI as a function
of the next grid load realisations, binary variables zl =
{zij
l }m,n
i=1,j=1 ∈Zl = {0, 1}m×n are introduced in [17]
to relate the grid load variable, yl to its statistics. More
speciﬁcally, the variables zij
l
count the frequency of yl when
estimating its statistics using the histogram method. Given that
the value of xl falls in the i-th bin, for each value of yl, there
exists exactly one non-zero zij
l
representing the bin where yl
falls. Using zl as the optimisation variables, an approximation
of the MI function, ˜I(zl) is then formulated as an optimisation
objective [17]. A brief summary on the derivation of ˜I(zl) is
provided in online Appendix A [29]; further details can be
found in [17]. Here, we relax the binary constraints on zl,
i.e. zl ∈Z′
l = [0, 1]m×n and allow that for each value of
yl, there exists a set of non-zero zij
l
within the feasible set.
Effectively, this relaxes the constraints imposed on yl by zl,
thereby affecting the statistics perceived by the controller, and
hence, its privacy protection performance [30]. Deﬁne then the
set F′
l as the set of all (yl, zl) that satisﬁes the constraints (2)
to (6), in addition to the following constraints:
n
X
j=1
zi∗j
l
= 1
(8)
zij
l = 0
, ∀i ̸= i∗
(9)
n
X
j=1
zi∗j
l
yj−1
l
≤yl <
n
X
j=1
zi∗j
l
yj
l ,
(10)
where i∗is the index corresponding to the given value of
xl. Constraint (10) links the grid load to its PDF estimate.
Furthermore, let Φ(yl) = ˜I(zl) for any zl satisfying (yl, zl) ∈


---

Page 4

---

PREPRINT
4
F′
l. ˜I(zl) is a quadratic form that is strongly convex for
m > 1. This can be implied from [17] by relaxing the binary
constraints and limiting the optimisation program to a single
time step, and can be shown by analysing its algebraically
manipulated form (see online Appendix B [29]). Note that
˜I(zl) is only strongly convex for m > 1. Furthermore, the
gradient of ˜I(zl) is bounded, thereby making ˜I(zl) Lipschitz
continuous. These properties will be used later to apply the
online gradient descent method to solve (1).
C. Ancillary Service Provision
We consider the tracking of a target aggregate real power
load proﬁle as the ancillary service objective, and penalise
deviations from this target proﬁle, i.e.,
Γ(y) :=

 N
X
l=1
yl
!
−¯y

2
2
,
(11)
where ¯y is the target proﬁle, and y = {y1, y2, . . . , yl}. This
target proﬁle can be shaped to provide services such as peak
shaving, grid balancing, and congestion alleviation, or simply
just to follow a planned consumption proﬁle. Moreover, in
well designed systems, power ﬂow constraints arising from
the provision of ancillary services by DERs are considered
during their pre-qualiﬁcation stage. These constraints are then
taken into account when aggregating them for service pro-
vision; i.e., the aggregation groups can be deﬁned such that
participants within a group face similar constraints, which are
then accounted for when sending out service requests. Note
that one could also track an additional target reactive power
proﬁle in order to provide voltage support, but this is left as
the subject of future work.
III. PROJECTED ONLINE GRADIENT DESCENT
The overall optimisation problem is now given by
minimise
yl,zl,s+
l ,s−
l
N
X
l=1
n
Λ(yl) + µl ˜I(zl)
o
+ ρΓ(y)
subject to
(yl, zl, s+
l , s−
l ) ∈F′
l,
l = 1, . . . , N,
(12)
which can be solved optimally using an ofﬂine centralised
controller by the aggregator if real-time high-resolution SM
measurements and high-bandwidth communication links are
available. However, given that current AMI deployments poll
for readings at intermittent intervals due to communication
infrastructure bandwidth constraints, this solution method re-
mains impractical. Moreover, this would also require that
private information from all consumers, i.e, their actual con-
sumer load, privacy preferences and day-ahead schedules, be
revealed to the aggregator, invalidating the privacy protection
objective. Alternatively, (12) can be solved using an ofﬂine dis-
tributed algorithm in the presence of two-way high-bandwidth
communications infrastructure between scheme participants,
which is again impractical for current grids. Therefore, we
propose solving (12) using a distributed feedback-based online
gradient descent solution method based on the general real-
time feedback-based optimisation framework proposed in [27].
The algorithm replaces the coupling of the grid load variables
across consumers in (11) with the latest real-time aggregated
consumption measurement ˆy at the point of common coupling:
N
X
l=1
yl ≈ˆy.
Hence, only the value ∥ˆy −¯y∥2
2 is communicated in real-
time, and is treated as a constant when computing the gra-
dients. This makes (12) separable and solvable locally, over-
coming the lack of real-time SM data and mitigating privacy
concerns. The availability of ˆy can readily be assumed given
the increasing adoption of phasor measurement units (PMUs),
and that transformers or busbars can easily be outﬁtted with a
high-frequency measurement device. The use of ˆy leads to a
lagged and sub-optimal solution at each time step. However, by
assuming that high-speed control actions can be actuated faster
than the time-varying nature of (12), the distributed algorithm
is shown to converge to a centralised solution in [27], provided
that the optimisation problem is strongly convex.
Recall that (12) is strongly convex for m > 1. Nevertheless,
we add a regularisation term ∥h∥2
2 with a small coefﬁcient
σ2/2, where h is the vector of all the optimisation variables;
this ensures that (12) is at least σ2-strongly convex in all
cases (e.g., when m = 1, or when extending the algorithm to
multiple time steps). It is easy to see that ∥h∥2
2, which is the
sum of the squares of the variables, is separable. Accordingly,
let1 ρ = σ1/2, and
f(yl, zl) =
N
X
l=1
n
Λ(yl) + µl ˜I(zl)
o
+ σ1
2 Γ(y) + σ2
2 ∥h∥2
2 .
We now solve the following quadratic program,
minimise
yl,zl,s+
l ,s−
l
f(yl, zl)
subject to
(yl, zl, s+
l , s−
l ) ∈F′
l ,
(13)
locally at each HEMS by ﬁrst taking a gradient descent step:
˜s+
l,t = s+
l,t−1 −r∇s+
l,tf(yl, zl)
(14)
˜s−
l,t = s−
l,t−1 −r∇s−
l,tf(yl, zl)
(15)
˜zi∗j
l,t = zi∗j
l,t−1 −r∇zi∗j
l,t f(yl, zl), j = 1, . . . , n,
(16)
where r is the gradient descent step size, and ∇A is the
gradient with respect to A. The ﬁnal solution is then obtained
by projecting the interim solution onto the feasible set, i.e.,
[s+
l,t, s−
l,t, zi∗j
l,t ]T = projF′l[˜s+
l,t, ˜s−
l,t, ˜zi∗j
l,t ]T .
(17)
Only variables zi∗j
l
are updated at each time step, with
variables zij
l
for i ̸= i∗being treated as zero when computing
the gradients for zi∗j
l
. Note that the actual values of zij
l , i ̸= i∗
are not re-initialised as zero, and are kept for future time steps
in order to ensure convergence. The gradients ∇s+
l,tf(yl, zl),
∇s−
l,tf(yl, zl), and ∇zi∗j
l,t f(yl, zl) are derived from (5) and
(13), then computed by substituting for ˆy; see online Appendix
B for the details on the gradients [29].
1for simplicity in deriving the gradient


---

Page 5

---

PREPRINT
5
A. Battery Modelling
The convex modelling of realistic batteries while avoiding
physically infeasible but optimal decisions due to simultaneous
charging and discharging remains a research challenge. There
are numerous modelling methods, e.g., using binary variables,
quadratic constraints, or penalising battery use, but they are
either non-convex, or are inapplicable because simultaneous
charging and discharging is allowed and is optimal for (12) in
some scenarios. To circumvent this issue, we assume that the
battery is unable to go directly from charging to discharging,
i.e, it must go through “zero”,
(s+ > 0, s−= 0) →(s+ = 0, s−= 0) →(s+ = 0, s−> 0) ,
and vice versa. This is a reasonable assumption given sufﬁ-
ciently fast control actions and limitations on certain power
converter designs.
The proposed distributed projected online gradient descent
algorithm incorporating this battery modelling work-around is
summarised in Algorithm 1. We note that the convergence
of this algorithm is guaranteed provided that the step size r
in (14) - (16) is small enough, as the optimisation problem
deﬁned by (13) satisﬁes the conditions identiﬁed in [27]; see
[27] for details. The feasibility of the optimisation problem is
also guaranteed as privacy requirements are formulated as a
term in the objective function instead of a hard constraint.
Algorithm 1 algorithm for solving (13) at time t
1: obtain aggregated load measurement ˆyt−1
2: obtain target load ¯yt
3: compute ∥ˆyt−1 −¯yt∥2
2 and broadcast to consumers
4: for consumer 1 to N do
5:
obtain load forecast xl,t and battery state el,t
6:
if charge ﬂag = true then
7:
compute s+
l,t and zi∗j
l,t using (14), (16) and (17)
8:
if s+
l,t ≥0 then
9:
actuate s+
l,t and update zi∗j
l,t
10:
else
11:
charge ﬂag = false
12:
actuate s+
l,t = 0 and update zi∗j
l,t
13:
else
14:
compute s−
l,t and zi∗j
l,t using (15), (16) and (17)
15:
if s−
l,t ≥0 then
16:
actuate s−
l,t and update zi∗j
l,t
17:
else
18:
charge ﬂag = true
19:
actuate s−
l,t = 0 and update zi∗j
l,t
20:
update constants (aij
l , bj
l , ci
l) used in the MI
21:
approximation (see Appendix A in [29] for details)
22: advance to t + 1
IV. NUMERICAL EXPERIMENTS
The proposed scheme is tested using 1 Hz smart meter
data taken from the ECO dataset [31]. As there are only six
houses in this dataset, we emulated more consumers in the
RDSA scheme by drawing data from multiple days over the
period between 26 August and 9 September, 2012 from the six
households. This results in a dataset with homogeneous load
proﬁles, which may decrease target aggregate load tracking
performance. Given more heterogeneous load proﬁles (as in
reality), the resultant aggregate load would likely be smoother
as load peaks are compensated by load troughs, allowing for
better tracking.
A. Simulation Setup
Each household in the RDSA scheme was assigned a
random price of privacy loss, 1 ≤µl
≤9, to mimic
the behaviour of multiple real households. To enforce the
assumption that control actions are actuated faster than the
time varying nature of (13), we assume that the local high
frequency SM measurements have a resolution of 0.2 Hz, and
that the target grid signal also varies every 5 seconds, while
the aggregated load measurements are available every second.
These are realistic assumptions, as local HEMS controllers
obtain measurements from smart meters deployed locally at
each household, which have the ability to sample at 2kHz or
higher; and aggregators receiving continuous real-time reserve
provision signals may choose to broadcast a more stable signal,
so long as they meet the requirements in their service contracts
with the grid operator.
Each household tracks an arbitrary day-ahead schedule,
yref
l , computed using a single multi-time step optimisation for
energy costs and MI privacy, at half-hourly resolution with
the MDPC algorithm described in [17], and on a two-tier
time-of-use energy tariff. Here, we deﬁne ˆy = PN
l=1 yl for
simplicity, omitting grid losses, and assume that grid in-feed
is not allowed, i.e, ymin
l
= 0. Depending on network topology
and size, the grid losses may impact the RDSA scheme’s
performance in reality, but this is outside the scope of this
paper. The general system setup at each consumer household
is summarised in Table I, where battery parameters were taken
from the Tesla Powerwall v1.
The target aggregate load ¯y is generated using the aggre-
gated day-ahead consumer schedules as a base, considering
total RDSA reserve capacity ¯γ = Nγ. For ease of assessment,
this is designed such that the target load is energy neutral with
respect to the aggregate day-ahead schedule within each half-
hourly interval. When generating such a reference curve, we
took into account battery losses (max bias of 0.1% of reserve
capacity), and ensured that the aggregate reserves are sufﬁcient
to meet the ancillary service requests approximately 99.7% of
the time.
Unless otherwise stated, the simulation parameters are as
listed in Table II where applicable. For ease of comparison and
simplicity, we set aside battery energy capacity corresponding
to γ at each consumer household in their day-ahead schedules,
and assume that the battery model in the optimisation problem
is accurate.
The
proposed
distributed
algorithm
(abbreviated
as
Dist.POGD in this section) is compared against an ideal
centralised solution for (13), both with and without relaxing
the binary constraints on zl by modelling it in YALMIP [32],


---

Page 6

---

PREPRINT
6
TABLE I
INDIVIDUAL HOUSEHOLD SYSTEM PARAMETERS
Real-Time PDF Estimation Sample Size, K + 1
901
Number of X Bins, m
15
Number of Y Bins, n
15
Additive Smoothing, ε
0.1
Battery Capacity
6.4 kWh
Battery Power
3.3 kW
One-way Battery Efﬁciency, η
96 %
RDSA Reserve Capacity, γ
0.15 kW
TABLE II
GENERAL SIMULATION PARAMETERS
Initial Battery State of Charge
3.2 kWh
Ancillary Service Coefﬁcient, σ1
5
Regularisation Coefﬁcient, σ2
1e−4
Descent Step Size, r
0.012
No. of Consumers, N
20
and solving it with the Gurobi solver. For the distributed
algorithm, we assume a persistent (rather than perfect) forecast
for xl, i.e., use the latest high-frequency SM measurement for
computing the gradient step. For the centralised solution, a
perfect forecast was used instead in order to provide a better
benchmark. Note that PN
l=1 yl is not substituted with ˆy in
the centralised solution. Table III summarises the information
used in the respective solution methods at time t.
B. Visualisation of Aggregate Loads
Fig. 2 illustrates the target aggregate load proﬁle, the
aggregated grid loads from Dist.POGD and a centralised
solution with relaxed binary constraints, and the total con-
sumer load. Within the speciﬁc illustrated period, the batteries
are discharging, resulting in grid loads less than the total
consumer load; but the converse can be true in other periods.
Using the parameters in Table II and the selected energy
and privacy loss prices, the Dist.POGD solution converges
close to the ideal centralised solution, as seen in Fig. 2, and
overshoots only when there is a signiﬁcant consumer load
change. The performance of Dist.POGD is affected by the
choice of parameters in Table II. These parameters have to
be chosen empirically in a real system, as consumer privacy
preferences would be unknown to the aggregator.
C. Evaluation Metrics
Numerically, we evaluate the performance of the algorithms
over a period of three and a half hours (number of samples
Ks = 12600; simulate four hours, discard the ﬁrst half-hour
for initialisation purposes) with the following metrics. For
TABLE III
VARIABLES USED IN THE OPTIMISATION PROBLEM AT TIME t
Distributed
Centralised
Load Forecast
xl,t−1
xl,t
Target Aggregate Load
¯yl,t
¯yl,t
Day-Ahead Schedule
yref
l,t
yref
l,t
Aggregate Load
ˆyl,t−1
PN
l=1 yl,t
ancillary service provision, the algorithms are evaluated based
on the normalised root mean square error (NRMSE) between
ˆy and ¯y, given by
NRMSE :=
q
1
Ks
PKs
k=1(ˆyk −¯yk)2
¯ymean
× 100% ,
¯ymean = 1
Ks
Ks
X
k=1
¯yk ,
and the mean absolute percentage error (MAPE),
MAPE := 100%
Ks
Ks
X
k=1

ˆyk −¯yk
¯yk
 .
MAPE gives the average of the errors at each time t, while
NRMSE emphasises large deviations from the target load,
which are undesirable, and reﬂects the target load tracking
error relative to the overall mean. The consumer preference
(day-ahead schedule tracking) is evaluated by computing its
normalised mean absolute error (NMAE), i.e., the absolute
error as a percentage of the maximum grid load,
NMAE :=
100%
Ksymax
l
Ks
X
k=1
yl,k −yref
l,k
 .
We used an approximate MI function in the objective func-
tion of the optimisation problem. However, for evaluation
purposes we estimate the average MI, assuming identical
and independently distributed random variables (denoted as
Iiid), and stationary ﬁrst-order Markov processes (denoted
as Imk), as described in [33], [34]. Such evaluation requires
the computation of pX,Y (x, y) log[pX,Y (x, y)/pX(x)pY (y)],
which in the case of pX,Y (x, y) being zero, is set to zero
to avoid computing log 0. The Imk captures some of the time
correlation between the consumer and grid loads, which is
neglected when calculating the Iiid [34]. Note that while
modelling the Xl and Yl as time-varying Markov processes
would yield more accurate MI estimates, there are insufﬁcient
samples from this simulation for its application.
The information that is contained within a consumer’s load
proﬁle has been shown to be dependent on the measurement
frequency [35]. Thus, the privacy risks stemming from high-
frequency SM measurements are also time resolution depen-
dent, i.e, the resolution at which consumers are metered inﬂu-
ences their privacy risks [36]. Given that 1-minute metering
resolution is more likely to be deployed than the 1-second
time resolution of the controller, the MI is also assessed at
this lower time resolution to better understand the realistic
SM privacy loss.
While there is a lack of literature that studies SM privacy
protection considering access to side information, the presence
of such information should not be ignored due to its potential
impact on the performance of privacy protection schemes. In
a recent preliminary work, even the presence of mundane side
information (day of the week) has been shown to degrade the
performance of two different learning-based SMDM privacy
protection mechanisms [37]. While adversarial attack models
are not the focus of this paper, for the sake of completeness,


---

Page 7

---

PREPRINT
7
13500
13550
13600
13650
13700
13750
13800
13850
13900
13950
14000
Simulation Time [s]
6
6.5
7
7.5
8
8.5
9
9.5
10
10.5
11
Aggregate Load [kW]
(a) Target grid load and aggregated grid loads
13500
13550
13600
13650
13700
13750
13800
13850
13900
13950
14000
Simulation Time [s]
12.8
13
13.2
13.4
Aggregate Load [kW]
(b) Aggregated consumer load
Fig. 2.
Target grid load, and aggregated grid and consumer loads
we also considered privacy loss in the presence of some
simple side information, which may increase the information
leakage to the adversary. In our case study, one could rea-
sonably assume that an adversary (possibly the aggregator)
may have the following side information: the ancillary service
provision signal ∥ˆyt−1 −¯yt∥2
2, and each consumer’s day-ahead
schedule yref
l . Each consumer’s grid load on the other hand
is composed of their day-ahead schedule, deviations due to
privacy-protection, ancillary service request, and consumer
load deviations from day-ahead forecasts. Hence, a naive, but
simple assessment of such risk is conducted by estimating the
MI of the grid load proﬁles with the ancillary service portion
removed (denoted as GS or yG
l ), with the day-ahead schedule
removed (dentoed as DA or yD
l ), and with both subtracted
(denoted as DAGS or yDG
l
):
yG
l = yl −
ancillary service request
z
}|
{
(ˆy −¯y)
ymean
l
PN
l=1 ymean
l
,
ymean
l
= 1
ks
ks
X
k=1
yl,k ,
yD
l = yl −yref
l
yDG
l
= yG
l −yref
l
.
Fig. 3 illustrates the original and adjusted grid loads for
consumer 1. Note that the ancillary service request does not
equal the ancillary service provision, and that yDG
l
is the
adversary’s guess that does not reﬂect the actual privacy
sensitive consumer load. The number of bins, m and n, are
1800
1820
1840
1860
1880
1900
1920
Simulation Time [s]
-0.1
0
0.1
0.2
0.3
0.4
0.5
Load [kW]
Fig. 3.
Grid load for consumer 1
kept the same as in the optimisation problem when computing
the MI between xl and yl. However, n is adjusted when
computing the MI for yG
l , yD
l
and yDG
l
to account for the
increased range space; in order to keep a similar quantisation
resolution. The increase in range space for yG
l and yDG
l
can be
seen in Fig. 3; while the range space increase for yD
l occurs
whenever there is a change in the day-ahead schedule (e.g.,
every half hourly in our case study). All else being equal,
increasing the quantisation resolution generally leads to an
increase in the MI estimate as discussed in [17].


---

Page 8

---

PREPRINT
8
D. Results and Discussion
Tables
VI
and
VII
summarise
the
performance
of
Dist.POGD with different parameters, and the two centralised
solutions. While the Dist.POGD solution converges close to
the ideal centralised solution as seen in Fig. 2, there is a dete-
rioration in the overall performance due to the time required
for convergence, forecast error, and the replacement of ˆyl,t−1
for PN
l=1 yl,t. For the simulations, a persistent forecast was
used in Dist.POGD instead of a perfect forecast. This allows
for a better analysis of its performance if deployed in reality.
Moreover, relaxing the binary constraints on zl marginally
improves the NRMSE, MAPE, average NMAE, and most
of the MI estimates, showing that this relaxation does not
signiﬁcantly impact the performance of the MI approximate
in the objective function for a single control action. Note,
however, that this may not be true in general; in fact, the
opposite might occur as shown in [30].
One can also see an increase in information leakage if
MI is assessed at a resolution lower than the controller’s,
e.g., at one minute instead of one second. However, this
increase might not pertain to information that is masked
by the controller at higher resolutions, e.g., information on
the type of device (contained in low time resolution data)
versus a device’s condition (inferable from high frequency
data). By deﬁnition mutual information measures the general
interdependence between two statistical distributions. As such,
it is immune to post-processing for the information it is
designed to hide. However, this does not mean that the grid
load does not carry different (unprotected) information about
the consumer load that is inferable from lower time resolution
(aggregated) data . Recall that time aggregation has signiﬁcant
impact on SM load proﬁle characteristics and by extension,
also on the information contained within them [35].
To gain a better understand the effect of time resolution
(aggregation) on the privacy levels attained by privacy mecha-
nism employed in this paper, Houses 1 and 11 were simulated
and evaluated at different time resolutions, with the controller
objective set to only protect privacy. Tables IV and V show
the results of the different MI estimates. Assuming that the
battery controller is able to maintain a ﬁxed value across
higher time resolutions (i.e., hold a ﬁxed grid load over the
control action interval), it can be seen that evaluating privacy
loss at time resolutions higher than those used for the control
actions always led to less privacy-loss. This is intuitive as it
is akin to load-levelling across the evaluation time interval.
However, it is inconclusive to state that aggregating high
time resolution measurements always leads to more privacy-
loss; e.g., there is less IID MI when evaluating 1-minute
simulations for House 1 at 5-minute resolutions. We believe
that the effects on time aggregation during evaluation may
be dependent on the amount of time-correlated information
present in the underlying consumer load, but the investigation
of this is left for future work.
Note also that the 1-sec Imk values are very small because
the measure is unable to fully capture the time-correlated
privacy leakage that it was designed for. The time-correlation
of the load proﬁles is at least 5 seconds (5 sample intervals),
TABLE IV
HOUSE 1 PRIVACY PROTECTION ONLY
Evaluation Resolution
IID MI
Markov MI
Sim. Reso.
1 Sec
1 Min
5 Min
1 Sec
1 min
5 Min
1 Second
0.068
0.067
0.092
0.011
0.102
0.393
1 Minute
0.412
0.437
0.358
0.0030
0.220
0.522
5 Minutes
0.074
0.079
0.105
6.95e-4
0.038
0.195
TABLE V
HOUSE 11 PRIVACY PROTECTION ONLY
Evaluation Resolution
IID MI
Markov MI
Sim. Reso.
1 Sec
1 Min
5 Min
1 Sec
1 min
5 Min
1 Second
0.681
0.689
0.736
0.031
0.232
0.309
1 Minute
0.446
0.579
0.571
0.006
0.216
0.320
5 Minutes
0.361
0.414
0.552
0.004
0.099
0.318
which cannot be captured by modelling the loads as ﬁrst-order
Markov processes, a drawback that was previously highlighted
in [34].
Table VIII summarises the MI estimates for the compen-
sated grid loads using the reference Dist.POGD setup. In
analysing the effects of the simple grid load compensation
using the possible side information, we consider only added
information leakage as this illustrates the loss of privacy in the
presence of such information. Comparing Tables VII and VIII,
one can see that correcting for ancillary service request results
in higher 1-sec Imk, and 1-min Imk estimates, thus resulting
in more leakage of time-correlated private information. While
there is a slight increase in 1-min Iiid, the results are inconclu-
sive. Having the day-ahead consumer schedule does not appear
to increase information leakage in our experiments. This can
be seen as there is no marked increase in information leakage
when compensating for the day-ahead schedule alone (DA),
or further compensating for it after removing the grid service
request (DAGS). This shows that the ancillary service request
signal constitutes sensitive side-information, while additional
information on the day-ahead schedule may not exacerbate
consumer privacy loss. Note that the day-ahead schedules in
this case study are optimised for half-hourly privacy protection
in addition to energy cost, which may explain the lack of
sensitive information derivable from them. Further study on
ways of incorporating the day-ahead schedules are needed for
a conclusive verdict on their privacy sensitivity.
As discussed, the RDSA parameters are setup-dependent,
and changing the number of consumers in the RDSA while
keeping all else constant affects the convergence rates and
performance. This is illustrated for 25 and 15 consumers in
Fig. 4. The choice of gradient descent step size r affects
the convergence rate of Dist.POGD; too high a value for r
leads to overshoots and instability, while too low a value
hinders convergence to the optimal solution before the problem
changes, as seen in Fig. 5. 1-Sec Imk increases with larger
step sizes (see Table VII), showing an increase in the leakage
of time-correlated private information with larger r values.
On the other hand, the overall tracking performance improves
and Iiid decreases as the rate of convergence (and overshoots)
increases (see Table VI and Fig. 5). An ideal value for the


---

Page 9

---

PREPRINT
9
TABLE VI
PERFORMANCE OF DIFFERENT SOLUTION METHODS AND PARAMETERS
NRMSE
MAPE
Avg. NMAE
Reference Dist.POGD
1.694%
0.7878%
4.699%
Centralised, binary
0.336%
0.295%
3.71%
Centralised, relaxed
0.322%
0.283%
3.53%
15 Consumers
2.69%
1.61%
5.42%
25 Consumers
1.51%
0.827%
4.32%
r = 0.008
2.80%
1.63%
5.13%
r = 0.016
1.56%
0.914%
4.41%
σ2 = 0
1.691%
0.7873%
4.695%
σ2 = 0.001
1.694%
0.7883%
4.703%
µl = 0
1.68%
0.777%
4.61%
11 ≤µl ≤19
1.78%
0.866%
5.21%
K = 600
1.70%
0.796%
4.71%
K = 1200
1.69%
0.785%
4.69%
σ1 = 3
3.17%
2.05%
4.41%
σ1 = 7
1.65%
0.978%
4.86%
TABLE VII
MI ESTIMATES FOR DIFFERENT SOLUTION METHODS AND SETTINGS
Avg. 1 sec
Avg. 1 min
Iiid
Imk
Iiid
Imk
Reference Dist.POGD
0.248
0.020
0.280
0.193
Centralised, binary
0.236
0.018
0.277
0.140
Centralised, relaxed
0.221
0.015
0.270
0.147
15 Consumers
0.301
0.018
0.354
0.228
25 Consumers
0.223
0.020
0.244
0.164
rg = 0.008
0.256
0.019
0.300
0.194
rg = 0.016
0.247
0.022
0.279
0.184
σagg,2 = 0
0.248
0.020
0.281
0.192
σagg,2 = 0.001
0.247
0.020
0.281
0.192
µl = 0
0.254
0.020
0.287
0.194
11 ≤µl ≤19
0.237
0.020
0.269
0.196
K = 600
0.247
0.020
0.276
0.196
K = 1200
0.248
0.020
0.282
0.196
σagg,1 = 3
0.253
0.018
0.294
0.189
σagg,1 = 7
0.250
0.023
0.285
0.204
coefﬁcient σ2 for the regularisation term ∥h∥2
2 would result in
minimal impact on the performance of the algorithm. As seen
in Tables VI and VII, Dist.POGD with σ2 = 1e−4 has similar
performance to an algorithm without regularisation.
As expected, increasing σ1 reduces the ancillary service
provision NRMSE at the expense of increasing the day-ahead
tracking NMAE and most MI estimates. However, a decrease
in σ1 does not necessarily lead to a decrease in Iiid due to a
slower convergence rate (see Fig. 6). Surprisingly, increasing
σ1 could also lead to an increase in ancillary service provision
MAPE due to tracking overshoots as illustrated in Fig. 6.
Increasing µl decreases Iiid, but increases ancillary service
provision NRMSE and MAPE, and the average NMAE for
tracking the day-ahead schedule. Changing the sample size K
TABLE VIII
MI ESTIMATES FOR THE COMPENSATED GRID LOAD
Reference Dist.POGD
Avg. 1 sec
Avg. 1 min
Iiid
Imk
Iiid
Imk
GS
0.236
0.039
0.306
0.249
DA
0.102
0.022
0.139
0.224
DAGS
0.086
0.033
0.138
0.225
13500
13520
13540
13560
13580
13600
13620
Simulation Time [s]
6.5
7
7.5
8
8.5
9
9.5
10
Aggregate Load [kW]
(a) 15 consumers
13500
13520
13540
13560
13580
13600
13620
Simulation Time [s]
11
12
13
14
15
16
17
Aggregate Load [kW]
(b) 25 consumers
Fig. 4.
Tracking performance with different aggregation sizes
13500
13520
13540
13560
13580
13600
13620
Simulation Time [s]
7
8
9
10
11
Aggregate Load [kW]
Fig. 5.
Comparison between different step sizes, r
in the objective function has a similar effect to changing µl
as it increases the importance of the current control action in
estimating the PDF of (Xl, Yl). However, their effects are not
equivalent as reducing K could lead to overﬁtting the PDF.
V. CONCLUSION
In this paper, a distributed projected online gradient de-
scent algorithm for providing ancillary services to the grid
by aggregating privacy-conscious residential consumers was
presented. A balance between the different objectives can be
13500
13520
13540
13560
13580
13600
13620
Simulation Time [s]
7
8
9
10
Aggregate Load [kW]
Fig. 6.
Comparison between different tracking coefﬁcients, σ1


---

Page 10

---

PREPRINT
10
achieved by adjusting their weights. Despite minor perfor-
mance degradation when compared to an ideal centralised
aggregation scheme, the proposed algorithm does not require
high-bandwidth communications infrastructure. Moreover, it
allows for the preservation of consumer privacy as the actual
consumer load does not need to be revealed to the aggregator.
Future work will focus on the provision of other grid
services such as voltage support, incorporating DERs with
uncertainty or more complex constraints, and considering grid
constraints in the formulation of the optimisation problem.
REFERENCES
[1] U.S. Energy Information Administration, “Annual electric power
industry report, form EIA-861,” 2017. [Online]. Available: https:
//www.eia.gov/electricity/annual/html/epa 10 10.html
[2] European
Commission,
“Cost-beneﬁt
analyses
&
state
of
play
of
smart
metering
deployment
in
the
EU-27,”
2014.
[Online].
Available:
https://eur-lex.europa.eu/legal-content/EN/TXT/
PDF/?uri=CELEX:52014SC0189&from=EN
[3] Swiss
Federal
Ofﬁce
of
Energy,
“Wichtigste
Neuerungen
im
Energierecht
ab
2018,”
2017.
[Online].
Available:
https:
//www.newsd.admin.ch/newsd/message/attachments/50166.pdf
[4] T. Hargreaves, M. Nye, and J. Burgess, “Making energy visible: A
qualitative ﬁeld study of how householders interact with feedback from
smart energy monitors,” Energy Policy, vol. 38, no. 10, 2010.
[5] A. Molina-Markham, P. Shenoy, K. Fu, E. Cecchet, and D. Irwin,
“Private memoirs of a smart meter,” in Proceedings of the 2nd ACM
Workshop on Embedded Sensing Systems for Energy-Efﬁciency in Build-
ing, Zurich, Switzerland, Nov. 2010, pp. 61–66.
[6] P. McDaniel and S. McLaughlin, “Security and privacy challenges in
the smart grid,” IEEE Security and Privacy, vol. 7, no. 3, 2009.
[7] V. Becker and W. Kleiminger, “Exploring zero-training algorithms for
occupancy detection based on smart meter measurements,” Computer
Science - Research and Development, vol. 33, no. 1-2, 2018.
[8] Y. Wang, Q. Chen, D. Gan, J. Yang, D. S. Kirschen, and C. Kang, “Deep
learning-based socio-demographic information identiﬁcation from smart
meter data,” IEEE Trans. on Smart Grid, vol. 10, no. 3, pp. 2593–2602,
2019.
[9] European Union, “Regulation (EU) 2016/679 of the European Parlia-
ment and of the Council of 27 April 2016 on the protection of natural
persons with regard to the processing of personal data and on the free
movement of such data, and repealing Directive 95/46/EC (General Data
Protection Regulation),” Ofﬁcial J. of the European Union, May 2016.
[10] G. Giaconi, D. G¨und¨uz, and H. V. Poor, “Privacy-aware smart metering:
Progress and challenges,” IEEE Signal Processing Magazine, vol. 35,
no. 6, pp. 59–78, Nov. 2018.
[11] C. Efthymiou and G. Kalogridis, “Smart grid privacy via anonymization
of smart metering data,” in 2010 First IEEE International Conference
on Smart Grid Communications, Gaithersburg, MD, USA, Oct. 2010.
[12] C. Rottondi, G. Mauri, and G. Verticale, “A data pseudonymization
protocol for smart grids,” in 2012 IEEE Online Conference on Green
Communications (GreenCom), Sept. 2012.
[13] M.
Jawurek,
M.
Johns,
and
K.
Rieck,
“Smart
metering
de-
pseudonymization,” in 27th Annual Computer Security Applications
Conference on - ACSAC ’11, Orlando, FL, USA, Dec. 2011.
[14] G. Kalogridis, C. Efthymiou, S. Z. Denic, T. A. Lewis, and R. Cepeda,
“Privacy for Smart Meters: Towards Undetectable Appliance Load
Signatures,” in First IEEE International Conference on Smart Grid
Communications (SmartGridComm), 2010, pp. 232–237.
[15] W. Yang, N. Li, Y. Qi, W. Qardaji, S. McLaughlin, and P. McDaniel,
“Minimizing private data disclosures in the smart grid,” in Proceedings
of the 19th ACM conference on computer and communications security
(CCS ’12), Raleigh, North Carolina, USA, Oct. 2012.
[16] Z. Zhang, Z. Qin, L. Zhu, J. Weng, and K. Ren, “Cost-friendly
differential privacy for smart meters: Exploiting the dual roles of the
noise,” IEEE Trans. on Smart Grid, vol. 8, no. 2, pp. 619–626, 2017.
[17] J. X. Chin, T. Tinoco De Rubira, and G. Hug, “Privacy-protecting energy
management unit through model-distribution predictive control,” IEEE
Trans. on Smart Grid, vol. 8, no. 6, pp. 3084–3093, 2017.
[18] Y. Sun, L. Lampe, and V. W. S. Wong, “Smart meter privacy: Exploiting
the potential of household energy storage units,” IEEE Internet of Things
Journal, vol. 5, no. 1, pp. 69–78, 2018.
[19] G. Giaconi, D. G¨und¨uz, and H. V. Poor, “Smart meter privacy with
renewable energy and an energy storage device,” IEEE Trans. on
Information Forensics and Security, vol. 13, no. 1, pp. 129–142, 2018.
[20] A. C. Chapman, G. Verbic, and D. J. Hill, “Algorithmic and strategic
aspects to integrating demand-side aggregation and energy management
methods,” IEEE Trans. on Smart Grid, vol. 7, no. 6, 2016.
[21] A. Rajabi, L. Li, J. Zhang, and J. Zhu, “Aggregation of small loads
for demand response programs — implementation and challenges: A
review,” in 2017 IEEE Intl. Conference on Environment and Electrical
Engineering and 2017 IEEE Industrial and Commercial Power Systems
Europe (EEEIC / I&CPS Europe 2017), Milan, Italy, June 2017.
[22] D. S. Callaway and I. A. Hiskens, “Achieving controllability of electric
loads,” Proceedings of the IEEE, vol. 99, no. 1, pp. 184–199, 2011.
[23] A. Bernstein and E. Dall’Anese, “Real-time feedback-based optimization
of distribution grids: A uniﬁed approach,” IEEE Transactions on Control
of Network Systems, vol. 6, no. 3, pp. 1197–1209, 2019.
[24] H. Li, X. Lin, H. Yang, X. Liang, R. Lu, and X. Shen, “EPPDR:
An efﬁcient privacy-preserving demand response scheme with adaptive
key evolution in smart grid,” IEEE Trans. on Parallel and Distributed
Systems, vol. 25, no. 8, pp. 2053–2064, 2014.
[25] Y. Gong, Y. Cai, Y. Guo, and Y. Fang, “A privacy-preserving scheme
for incentive-based demand response in the smart grid,” IEEE Trans. on
Smart Grid, vol. 7, no. 3, pp. 1304–1313, 2016.
[26] M. F. Balli, S. Uludag, A. A. Selcuk, and B. Tavli, “Distributed multi-
unit privacy assured bidding (PAB) for smart grid demand response
programs,” IEEE Trans. on Smart Grid, vol. 9, no. 5, 2018.
[27] E. Dall’Anese, A. Bernstein, and A. Simonetto, “Feedback-based
projected-gradient method for real-time optimization of aggregations
of energy resources,” in 2017 IEEE Global Conference on Signal and
Information Processing (GlobalSIP), Montreal, Canada, Nov. 2017.
[28] V. Arzamasov, R. Schwerdt, S. Karrari, K. B¨ohm, and T. B. Nguyen,
“Privacy measures and storage technologies for battery-based load
hiding - an overview and experimental study,” in Proceedings of the
Eleventh ACM International Conference on Future Energy Systems, ser.
e-Energy ’20, Virtual Event, Australia, 2020, pp. 178–195.
[29] J. X. Chin, A. Bernstein, and G. Hug, “Online appendix for aggregating
privacy-conscious DERs for grid service provision,” 2019. [Online].
Available: https://doi.org/10.5281/zenodo.3384771
[30] J. X. Chin, “Consumer privacy and smart distribution grids: A
cyber-physical ecosystem,” Ph.D. dissertation, ETH Zurich, 2020.
[Online]. Available: https://doi.org/10.3929/ethz-b-000406297
[31] W. Kleiminger, C. Beckel, and S. Santini, “Household occupancy
monitoring using electricity meters,” in Proceedings of the 2015 ACM
International Joint Conference on Pervasive and Ubiquitous Computing
(UbiComp 2015), Osaka, Japan, Sept. 2015.
[32] J. Lofberg, “YALMIP : a toolbox for modeling and optimization in
MATLAB,” in 2004 IEEE International Conference on Computer Aided
Control Systems Design, New Orleans, LA, USA, Sept. 2004.
[33] O. Tan, J. Gomez-Vilardebo, and D. G¨und¨uz, “Privacy-cost trade-offs
in demand-side management with storage,” IEEE Trans. on Information
Forensics and Security, vol. 12, no. 6, pp. 1458–1469, 2017.
[34] J. X. Chin, G. Giaconi, T. Tinoco De Rubira, G. Hug, and D. G¨und¨uz,
“Considering time correlation in the estimation of privacy loss for
consumers with smart meters,” in 2018 Power System Computation
Conference (PSCC), Dublin, Ireland, June 2018.
[35] J. Rousseau, “Impact of time and spatial aggregation of smart meter
data,” Semester Thesis, ETH Zurich, June 2020.
[36] G. Eibl and D. Engel, “Inﬂuence of data granularity on smart meter
privacy,” IEEE Trans. on Smart Grid, vol. 6, no. 2, pp. 930–939, 2015.
[37] M. Shateri, F. Messina, P. Piantanida, and F. Labeau, “On the impact
of side information on smart meter privacy-preserving methods,” 2020,
to be published. [Online]. Available: https://arxiv.org/abs/2006.16062
