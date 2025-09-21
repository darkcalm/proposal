

---

Page 1

---

Digital Twins based Day-ahead Integrated Energy System
Scheduling under Load and Renewable Energy
Uncertainties
Minglei Youa, Qian Wangb, Hongjian Suna,∗, Iv´an Castroc, and Jing Jiangd
aDepartment of Engineering, Durham University, Durham, UK
bDepartment of Computer Sciences, Durham University, Durham, UK
cLevelise Ltd, Oxford, UK
dNorthumbria University, Newcastle, UK
Abstract
By constructing digital twins (DT) of an integrated energy system (IES),
one can beneﬁt from DT’s predictive capabilities to improve coordinations
among various energy converters, hence enhancing energy eﬃciency and cost
saving.energy eﬃciency, cost savings and carbon emission reduction. This
paper is motivated by the fact that practical IESs suﬀer from multiple uncer-
tainty sources, and complicated surrounding environment. To address this
problem, a novel DT-based day-ahead scheduling method is proposed. The
physical IES is modelled as a multi-vector energy system in its virtual space
that interacts with the physical IES to manipulate its operations. A deep
neural network is trained to make statistical cost-saving scheduling by learn-
ing from both historical forecasting errors and day-ahead forecasts. Case
studies of IESs show that the proposed DT-based method is able to reduce
the operating cost of IES by 63.5%, comparing to the existing forecast-based
scheduling methods.much lower long-term operating costs than those of ex-
isting forecast-based scheduling methods. It is also found that both electric
vehicles and thermal energy storages play proactive roles in the proposed
method, highlighting their importance in future energy system integration
and decarbonisation.
Keywords:
Digital twins, Multi-vector energy system, Integrated energy
system, and Machine learning.
∗Corresponding author.
Email address: hongjian.sun@durham.ac.uk (Hongjian Sun)
Preprint submitted to Applied Energy
August 15, 2021


---

Page 2

---

1. Introduction
Besides meeting increasing energy demands, integrated energy systems
(IESs) are playing a vital role in reducing carbon emissions for tackling cli-
mate crisis [1]. Eﬀorts have been devoted to decarbonising both energy sup-
plies and energy consumption, e.g., promotion of renewable energy sources,
and adoption of electric vehicles (EVs) to replace fossil-fuelled vehicles. Ver-
satile energy converters, e.g., combined heat and power (CHP) generation,
show great potentials in further improving energy eﬃciency by jointly meet-
ing multiple energy demands [2]. This has stimulated a multi-vector energy
system (MVES) modelling method that characterises the operations of mul-
tiple energy converters to better coordinate both supply and demand in
multi-vector energy forms [3].
Recently a new concept called digital twins (DT) has received much
attention in the literature of IES [4]. With this DT concept, a MVES model
can be regarded as a virtual replica of a physical IES [5]. One key feature
of DT technologies is the interaction between the virtual replica and its
physical twin (real-world IES), as well as with external environment. The
twinning process between a virtual replica and its physical twin can be
achieved by using advanced communication technologies, such as Internet of
Things and 5G technologies. The real-time information of physical system
status and operations can be continuously collected and fed to the MVES
model, which then simulates, optimises and predicts the future status of its
physical twin. These predictions or optimised conﬁgurations can be sent
to physical devices. Hence, the physical counterparts of DTs, e.g., energy
converters and renewable energy sources, could be better coordinated and
managed, leading to the reduction of operating cost for IESs.
Through the use of DT technologies, IESs could not only participate in
wholesale energy market, but also provide ancillary services, such as bal-
ancing services [6]. Moreover, by integrating renewable energy sources and
ﬂexible loads, the DT can help improve energy eﬃciency, leading to more
cost-savings for both IES owners and energy consumers [7]. However, there
are multiple uncertainty sources in such a system [8] that might compromise
DT’s cost-saving potential [7]. Besides the intermittency of renewable en-
ergy sources, forecasts could introduce errors that result in uncertainties of
system operations [9]. In traditional IES operation scheduling studies, the
uncertainty is usually addressed by providing conserved performance with
worst-case assumptions, or simplifying the distribution of the uncertainty
sources. For example, in [10], the formulated IES integrates with renewable
energy, where the renewable energy forecasting errors are considered as un-
2


---

Page 3

---

certainty sources. The distribution of the forecasting errors is mapped to
intervals with ﬁxed proportion method, whose performance might depend
on the adopted intervals. In [11], Salkuti proposed a multi-objective opti-
mization based method for the day-ahead scheduling problem in the IES,
where the system uncertainty is due to the intermittent renewable energy
generation. The uncertainty is addressed by assuming that the distributions
of the uncertainty sources are known in prior, which might not be valid if the
uncertainty sources are of unknown patterns and unknown distributions in
a practical environment. In the literature, an economic reserve scheduling
problem was formulated for an IES with both electricity and natural gas
[10], where the renewable energy forecasting error was accounted by an in-
terval with ﬁxed proportion method. Salkuti [11] studied a multi-objective
optimization based method for the day-ahead scheduling of an IES with
thermal, wind, and solar energy. In this work, renewable energy generation
was assumed to follow a prior probability distribution. But such a strong
assumption may not be valid in a practical environment where obtaining
priors would be challenging.
Recently, machine learning based methods are providing promising so-
lutions to the uncertainty problem in IESs. Comparing to traditional ana-
lytical based methods, machine learning based methods have the potential
to learn from the data to mitigate the issues caused by introducing inap-
propriate simpliﬁcations or assumptions to the IESs. There have been ex-
tensive studies using the predictions from the machine learning algorithms
to improve forecasting accuracy. For example, Fan et al. [12] used recur-
rent neural networks to predict the building’s short-term energy demand,
while Theocharides et al.
[13] studied a data-driven method to forecast
the hourly-averaged day-ahead photovoltaic power generation. There are
also works that use machine learning algorithms to calibrate the energy
forecasting errors in IESs, for example, Zhu et al. proposed an approxi-
mate Bayesian computation based method to calibrate the building energy
models in [14]. A detailed review of the recent advances of using machine
learning for building load prediction can be found in [15]. To address the
uncertainty problem in IESs, machine learning based methods were exten-
sively studied. Fan et al. [12] used recurrent neural networks to predict the
building’s short-term energy demand. In [13], Theocharides et al. studied a
data-driven method to forecast the hourly-averaged day-ahead photovoltaic
power generation. Zhu et al. [14] studied an approximate Bayesian compu-
tation based machine learning method for calibrating the building energy
models to address the energy forecasting errors. To understand the full lit-
erature of this research area, please refer to a classic work [15] by Zhang et
3


---

Page 4

---

al. who summarised recent advances of using machine learning for build-
ing load prediction. Moreover, there have been several successful attempts
in addressing the day-ahead scheduling problem. In [16], Teo et al. pro-
posed an extreme learning machine method for the day-ahead scheduling
and real-time dispatching schemes by training historical data to make ac-
curate forecasts. In [17], Zhou et al. used long short-term memory neural
networks to make probabilistic forecasts on load demands and wind energy
generations, and integrated them into the look-ahead dispatching schemes.
Zhou et al. [18] further studied the day-ahead scheduling problem for fore-
casting the electricity price by using a recurrent deep learning method. The
performance of this method was veriﬁed against real-world data in the New
England electricity market. While aforesaid attempts were made to address
single source of uncertainties, there are still some serious limitations when
the day-ahead IES scheduling comes to real-life deployments where multiple
uncertainty sources co-exist, which is the main focus of this paper.
Besides the literature focusing on improving the prediction accuracy,
there are also successful attempts in integrating the machine learning based
forecasts into the IES operation scheduling problems. In [16], Teo et al.
proposed an extreme learning machine method for the day-ahead schedul-
ing and real-time dispatching schemes by training historical data to make
accurate forecasts. In [17], Zhou et al. used long short-term memory neural
networks to make probabilistic forecasts on load demands and wind energy
generations, and integrated them into the look-ahead dispatching schemes.
Zhou et al. [18] further studied the day-ahead scheduling problem for fore-
casting the electricity price by using a recurrent deep learning method. The
performance of this method was veriﬁed against real-world data in the New
England electricity market. However, the aforesaid attempts were made to
address a single source of uncertainties, while it leaves an open research
challenge to addressing the real-life IESs where multiple uncertainty sources
co-exist. This is also the main focus of this paper.
With the advent of DT, there is also a novel and promising trend in
addressing the IES operation scheduling problem by the integration of DT
and machine learning algorithms. In [19], Agostinelli et al. exploited the
machine learning algorithms as part of the co-simulators in the DT models,
which helps to improve the building energy management by jointly consider-
ing the energy eﬃciency, internal comfort, and climate conditions. Edward
et al. [20] proposed a versatile energy management tool based on DT, which
utilized machine learning modules to forecast the energy system demands,
coordinated the control of multi-vector smart energy systems. Diﬀerent from
[19] and [20], this work did not make local forecasts of the demands or gen-
4


---

Page 5

---

erations, but instead the machine learning technique was used to directly
address the IES scheduling problem with multiple uncertainties, whose out-
puts were the day-ahead scheduling values.
To ﬁll these research gaps, this paper presents a novel deep learning
and DT based IES scheduling method. In contrast to the literature, new
contributions of this paper are:
1. This deep learning and DT based IES scheduling method is designed
to address the problem of multiple uncertainty sources. It provides a
more practical solution for operating the real-life IESs embedded with
multiple uncertainty sources.
2. Diﬀerent from existing work which focus on improving the accuracy
of predictions, the proposed IES scheduling method is designed for
enabling real-time intervention and prevention of IESs by taking ad-
vantages of DT technologies. Ultimate performance of a physical IES
is directly linked to and addressed by its virtual replica’s predictive
capability.
3. A data augmentation based deep learning method is proposed to re-
duce the MVES’s long-term operating cost by learning from both his-
torical forecasting errors and day-ahead forecasts.
The remaining parts of this paper are organised as follows.
The DT
model of the IES is given in Section 2, and the proposed DT based IES
scheduling method is introduced in Section 3. Case studies with real-world
U.K. data are performed in Section 4. Finally the conclusions are presented
in Section 5.
2. System Model
The DT model consists of energy ﬂows and data ﬂows, which are given
in Fig. 1 and Fig. 2. The IES supplies both electricity loads and heat loads
with energy sourcing from the electricity, the renewable energy and the
natural gas. The IES components are aggregated according to their energy
forms, which is to facilitate the DT operation. Please kindly note that since
all IES components are studied in an aggregated manner, it is expected that
for each type of IES component, there will be multiple of them in numbers,
e.g., wind energy could represent a wind farm, while the electricity load could
be an aggregated electricity demand from thousands of buildings. Various
energy converters are considered, including electrical transformers, natural
gas boilers, and CHP systems (from natural gas to electricity and heat).
5


---

Page 6

---

Thermal energy storages (TESs) and EVs are also considered, which can
charge and discharge energy as scheduled by the MVES.
The DT integration with the real-time operation of the IES is illustrated
in Fig. 2. Speciﬁcally, the virtual replica MVES coordinates all the data
ﬂow within the physical IES and among the physical IES devices. During
the day-ahead scheduling phase, the MVES makes day-ahead scheduling de-
cisions for the IES devices, including the TESs and EVs, which are based
on the forecasts, energy market prices, and the TESs and EVs status. Then
the MVES coordinates the IES to make purchases from the day-ahead en-
ergy markets, and stores the day-ahead scheduling plans for the next-day
operations. During the real-time operation phase, the MVES commits the
day-ahead scheduling and monitors the operating status within the IES,
while it coordinates the physical energy converters to meet real-time energy
demands.
The day-ahead scheduling and real-time coordination between
the virtual replica MVES and the physical IES devices will be detailed in
the following subsections.
2.1. Multi-vector Energy System Model
Figure 1: The energy ﬂow of a typical IES, which consists of transformers, wind turbines,
solar panels, CHP systems, TESs, boilers and EVs.
Let T denote the total number of scheduling slots in one day, where
time intervals throughout the day have the same length (e.g., 1 hour). At
6


---

Page 7

---

Figure 2: The data ﬂow of a typical IES, where its virtual replica - MVES, and physical
IES devices form a DT system to interact with external environment.
each scheduling slot t ∈[1, T], let St
E and St
G denote the imported elec-
tricity and natural gas, respectively. Within the IES, there are KW wind
turbines, KPV solar panels, KEV EVs and KTES TES systems, whose energy
ﬂows at scheduling slot t are denoted as Sk,t
W with k = 1, . . . , KW, Sk,t
PV with
k = 1, . . . , KPV, Sk,t
EV with k = 1, . . . , KEV and Sk,t
TES with k = 1, . . . , KTES,
respectively. The sign of the energy ﬂow is positive if the energy is injected
into the IES, or negative if the energy is sourced from the IES. In the consid-
ered system in Fig. 1, the elements of vt = {vt
CHP, vt
B} are the dispatching
factors of the CHP and the boiler, respectively. The converters are subject
to physical constraints during the operations, which are detailed as follows:
• The Electricity Load Constraint:
The electricity supplied by the IES should meet the electricity load
demands Lt
E at each scheduling slot, which can be given by:
ηTFSt
E + vt
CHPηE
CHPSt
G +
KW
X
k=1
Sk,t
W +
KPV
X
k=1
Sk,t
PV +
KEV
X
k=1
Sk,t
EV = Lt
E,
(1)
where ηTF and ηE
CHPηE
CHP are the transformer’s energy eﬃciency and
the CHP’s electricity generation eﬃciency, respectively.
• The Heat Load Constraint:
The thermal energy supplied by the IES should meet the heat load
7


---

Page 8

---

demands Lt
H at each scheduling slot, which can be given by:
vt
CHPηH
CHPSt
G + vt
BηBSt
G +
KTES
X
k=1
Sk,t
TES = Lt
H,
(2)
where ηH
CHP is the thermal recovery eﬃciency of the CHPs, and ηB is
the energy eﬃciency of the boilers.
• The Energy Flow Constraints of Transformers, Natural Gas,
Wind Turbines, Solar Panels, CHPs and Boilers:
If we denote the maximum energy ﬂow of transformers, natural gas,
wind turbines, solar panels, CHPs and boilers at a scheduling slot
as SMAX
TF
, SMAX
G
, SMAX
W
, SMAX
PV
, SMAX
CHP and SMAX
B
, respectively, then
the scheduled energy ﬂows should satisfy corresponding minimal and
maximal energy ﬂow constraints at each scheduling slot, which can be
formulated as follows:
0 ≤St
E ≤SMAX
TF
,
(3)
0 ≤St
G ≤SMAX
G
,
(4)
0 ≤Sk,t
W ≤SMAX
W
, k = 1, . . . , KW,
(5)
0 ≤Sk,t
PV ≤SMAX
PV
, k = 1, . . . , KPV,
(6)
0 ≤vt
CHPSt
G ≤SMAX
CHP ,
(7)
0 ≤vt
BSt
B ≤SMAX
B
.
(8)
• The EVs’ Charging and Discharging Constraints:
A total of KEV EVs are considered, where the kth EV’s scheduled start
and end of service time are denoted as T In,k
EV and T Out,k
EV
, respectively.
The energy ﬂow observed from the kth EV’s aspect is denoted as Sk,t
EV,
which can be: a) positive if discharging, b) negative if charging, and
c) 0 if neither charging nor discharging. For notation convenience, the
EV’s charging state indicator ICh,k
EV
and discharging state indicator
IDCh,k
EV
are deﬁned as follows:
ICh,k,t
EV
≜1 −sgn{Sk,t
EV}
2
, IDCh,k,t
EV
≜1 + sgn{Sk,t
EV}
2
,
(9)
where the sign operator sgn{x} returns 1 if x > 0 and -1 if x < 0,
otherwise it will return 0.
Note that due to the charging and dis-
8


---

Page 9

---

charging eﬃciency, the energy ﬂow observed from the aspect of MVES
is the total energy consumed by this EV, consisting of both the en-
ergy charged to or discharged from this EV, and the energy loss due
to the charging and discharging operations. Denote the charging and
discharging eﬃciency as ηCh
EV and ηDCh
EV , then the consumed energy by
the EV can be given as Sk,t
EV

ICh,k,t
EV
ηCh
EV
+ IDCh,k,t
EV
ηDCh
EV

. With the indicators
ICh,k,t
EV
and IDCh,k,t
EV
, it can be seen that the energy ﬂow observed from
the aspect of MVES is: a) Sk,t
EV
ηCh
EV , when the EV is charging, b)
Sk,t
EV
ηDCh
EV ,
when the EV is discharging, and c) 0, when the EV is neither charg-
ing nor discharging. Then the kth EV’s energy ﬂow constraint at the
scheduling slot t ∈[T In,k
EV , T Out,k
EV
] can be given as follows:
−SCh, MAX
EV
≤Sk,t
EV
 
ICh,k,t
EV
ηCh
EV
+ IDCh,k,t
EV
ηDCh
EV
!
≤SDCh, MAX
EV
,
(10)
where SCh, MAX
EV
and SDCh, MAX
EV
are the maximal charging and dis-
charging energy ﬂows within a scheduling slot period. In the mean-
time, the MVES rewards EVs by leasing their available capacities
as electricity energy buﬀers, therefore the EVs’ original energy levels
should be restored at the end of their service time. This corresponds
to a zero net energy ﬂow for the kth EV during [T In,k
EV , T Out,k
EV
], which
can be formulated as follows:
T Out,k
EV
X
t=T In,k
EV
Sk,t
EV = 0.
(11)
In this paper, we use SOC
k,T In,k
EV
EV
to represent the kth EV’s State-of-
Charge (SOC) at its start service time T In,k
EV , then the SOCk,t
EV for the
scheduling slot t ∈[T In,k
EV , T Out,k
EV
] can be given as follows:
SOCk,t
EV = SOC
k,T In,k
EV
EV
+
t
X
τ=T In,k
EV
Sk,t
EV.
(12)
It should be noted that for any scheduling slot t, the kth EV’s SOCk,t
EV
should be bounded by the minimal energy capacity SOCMIN
EV
and the
9


---

Page 10

---

maximal energy capacity SOCMAX
EV
, which can be formulated as fol-
lows:
SOCMIN
EV ≤SOCk,t
EV ≤SOCMAX
EV
.
(13)
• The TES Charging and Discharging Constraints:
The TES is a ﬂexible thermal energy storage, whose model is similar
to the EVs as above. The start and end of the service time for the kth
TES system are denoted as T In,k
TES and T Out,k
TES , respectively. The TES’s
charging state indicator ICh,k
TES and discharging state indicator IDCh,k
TES
are deﬁned as follows:
ICh,k,t
TES
≜1 −sgn{Sk,t
TES}
2
, IDCh,k,t
TES
≜1 + sgn{Sk,t
TES}
2
.
(14)
The energy ﬂow Sk,t
TES of the kth TES at the scheduling slot t ∈
[T In,k
TES, T Out,k
TES ] are constrained as follows:
−SCh, MAX
TES
≤Sk,t
TES
 
ICh,k,t
TES
ηCh
TES
+ IDCh,k,t
TES
ηDCh
TES
!
≤SDCh, MAX
TES
,
(15)
where SCh, MAX
TES
and SDCh, MAX
TES
are the maximal charging and dis-
charging energy ﬂow within a scheduling slot period, while ηDCh
TES and
ηCh
TES denote the energy eﬃciency of the TES during discharging and
charging. In the meantime, the MVES rewards TESs by leasing their
available capacities as thermal energy buﬀers, therefore the TESs’ orig-
inal energy levels should be restored at the end of their service time.
This equivalents to a zero net energy ﬂow during [T In,k
TES, T Out,k
TES ] as
follows:
T Out,k
TES
X
t=T In,k
TES
Sk,t
TES = 0.
(16)
Let SOC
k,T In,k
TES
TES
denote the kth TES’s SOC at T In,k
TES, then the SOCk,t
TES
for the scheduling slot t ∈[T In,k
TES, T Out,k
TES ] can be given as follows:
SOCk,t
TES = SOC
k,T In,k
TES
TES
+
t
X
τ=T In,k
TES
Sk,t
TES.
(17)
For any scheduling slot t, the TES’s SOCk,t
TES should be bounded as
10


---

Page 11

---

follows:
SOCMIN
TES ≤SOCk,t
TES ≤SOCMAX
TES ,
(18)
where SOCMIN
TES and SOCMAX
TES
are the TES’s minimal and maximal
energy capacities, respectively.
2.2. Day-ahead Scheduling with Multiple Uncertainty Sources
In the problem of day-ahead scheduling with multiple uncertainty sources,
the system inputs are the day-ahead forecasts Ft ≜{Lt
E, Lt
H, Sk,t
W , Sk,t
PV},
while the outputs are the day-ahead scheduling St
Sch ≜{St
E, St
G, Sk,t
EV, Sk,t
TES, vt}.
The overall objective is to minimize the total cost Ct
All given as follows:
Ct
All = Ct
Sch + Ct
Extra,
(19)
where the scheduling cost Ct
Sch and the extra cost Ct
Extra are detailed as
follows:
• The Day-Ahead Scheduling Cost Ct
Sch:
For the scheduling slot t in the day-ahead markets, the electricity price
and the natural gas price are denoted as CDA,t
E
and CDA,t
G
, respectively.
Meantime, the reward price for the wind energy, solar energy, EVs
and TESs are ﬁxed all day and denoted as CW, CPV, CEV and CTES,
respectively. Therefore the total day-ahead scheduling cost Ct
Sch can
be formulated as follows:
Ct
Sch = CDA,t
E
St
E + CDA,t
G
St
G −
KTES
X
k=1
CTES|Sk,t
TES|
−
KEV
X
k=1
CEV|Sk,t
EV| −
KPV
X
k=1
CPVSk,t
PV −
KW
X
k=1
CWSk,t
W ,
(20)
where the EVs and TESs are rewarded based on their service to the
DT system, which is quantiﬁed by their absolute energy ﬂows.where
the rewards to the EVs and TESs are based on their absolute energy
ﬂows.
• The Real-Time Operation Extra Cost Ct
Extra:
During the real-time operation, the IES follows the day-ahead schedul-
ing St
Sch to operate the CHPs, EVs and TESs. Due to the forecasting
errors, the actual electricity load demands ˜Lt
E, the actual heat load
demands ˜Lt
H, the actual wind energy generation ˜St
W and the actual
11


---

Page 12

---

solar energy generation ˜St
PV can be diﬀerent from their forecasting
values, which results in the mismatch between real-time demands and
supplies. The MVES addresses this real-time mismatch via the trans-
former and the boiler as follows: a) in the case of insuﬃcient electricity
energy, the MVES will purchase the insuﬃcient amount of electricity in
the real-time energy markets with a price C+
E , and inject to the MVES
via the transformer, b) in the case of redundant electricity energy, the
MVES will refund or trade-in the redundant amount of electricity in
the real-time energy markets with a price C−
E , and reduce the injected
electricity from transformer, c) in the case of insuﬃcient thermal en-
ergy, the MVES will purchase the insuﬃcient amount of natural gas in
the real-time energy markets with a price C+
G, and inject to the boiler
to compensate the insuﬃcient thermal energy, and d) in the case of
redundant thermal energy, the MVES will refund or trade-in the re-
dundant amount of natural gas in the real-time energy markets with
a price C−
G, and reduce the consumed natural gas by the boiler. Note
that during the real-time operation, the charging and discharging of
the EVs and TESs are following the day-ahead scheduling decisions.
This is because the charging and discharging control of the EVs and
TESs not only depends on their historical operations, but also impacts
their future operations. Therefore the real-time adjustment might not
be optimal from the view of the whole day operation cost reduction.
Then the extra cost Ct
Extra can be given as follows:
Ct
Extra = Ct
Extra,E + Ct
Extra,G,
(21)
where the extra cost for electricity Ct
Extra,E and natural gas Ct
Extra,G
can be given as follows:
Ct
Extra,E =

C+
E ∆St
E,
∆St
E ≥0,
(CDA,t
E
−C−
E )∆St
E,
∆St
E < 0.
Ct
Extra,G =

C+
G∆St
G,
∆St
G ≥0,
(CDA,t
G
−C−
G)∆St
G,
∆St
G < 0.
(22)
where ∆St
E and ∆St
G denote the mismatched electricity and natural
12


---

Page 13

---

gas, which are calculated as follows:
∆St
E = 1
ηTF

˜Lt
E −ηTFSt
E −vt
CHPηE
CHPSt
G
−
KW
X
k=1
˜Sk,t
W −
KPV
X
k=1
˜Sk,t
PV −
KEV
X
k=1
Sk,t
EV

,
(23)
∆St
G = 1
ηB

˜Lt
H −vt
CHPηH
CHPSt
G −vt
BηBSt
G −
KTES
X
k=1
Sk,t
TES

.
(24)
If with no forecasting errors, the IES operator can avoid any extra cost
Ct
Extra, because both ∆St
E and ∆St
G will be zero. However, during the day-
ahead scheduling, the exact forecasting errors δt cannot be known, which
means the extra costs Ct
Extra are random and unavoidable. With the con-
sideration of the day-ahead forecasts and the potential forecasting errors δt,
it is potential to make more cost-eﬀective day-ahead scheduling, comparing
to schedules based solely on the day-ahead forecasts. Please also note that
the forecast errors are random in nature, while the reported forecasting per-
formances are usually referring to its average performance in the long-term,
e.g., the historical U.K. dataset is referring to a period of 1 year. How-
ever, the uncertainty introduced by these forecasting errors are impacting
the IES system hourly (or less then 1 hour depending on the forecast reso-
lutions). These time-varying forecasting errors can have unknown patterns,
which are also not possible to be bounded in the real-world (e.g., due to un-
expected conditions like bad weather). Therefore the averaged forecasting
performance (e.g., the yearly averaged forecasting errors) only reﬂects part
of the uncertainty in the practical IES. By addressing the uncertainty with
the consideration of their time-varying patterns, it is potential to further
reduce the extra costs induced by these uncertainties.
The day-ahead scheduling objective is formulated as the minimisation of
the mathematical expectation of the actual total cost Ct
All against potential
forecasting errors δt for the whole 24 hour period as follows:
P1 :
min
St
Sch
Eδt
( T
X
t=1
Ct
All
)
(25)
s.t. (1) −(8), (10) −(11),
(13), (15) −(16) and (18),
13


---

Page 14

---

where Ex{y(x)}=
R ∞
−∞y(x)p(x)dx is the mathematical expectation opera-
tion and p(x) is the probability distribution function (PDF) of x.
The formulation of P1 can be further interpreted as follows. With the
given day-ahead forecasts Ft, the MVES is to make a day-ahead scheduling
St
Sch, such that it can: a) have the lowest cost in a statistical manner against
the potential forecasting errors δt, and b) meet the physical constraints as
speciﬁed in (13), (15)-(16) and (18). This makes P1 a very challenging
problem, because each forecast Ft could correspond to countless actual val-
ues ˜Ft due to the random forecasting errors δt, where any day-ahead schedul-
ing could be saving costs for some actual values ˜Ft, while increasing costs
in other cases at the same time. Here ˜Ft ≜{˜Lt
E, ˜Lt
H, ˜Sk,t
W , ˜Sk,t
PV}, whose ele-
ments are the actual electricity load demand, the actual heat load demand,
the actual wind energy generation, and the actual solar energy generation,
respectively. In this paper, this challenge is addressed via a deep learning
embedded scheduling scheme, which is detailed in the next section.
3. Deep Learning Embedded Integrated Energy System Schedul-
ing Scheme
To address the challenge of day-ahead scheduling under multiple uncer-
tainties for IESs, we propose a novel deep learning embedded scheduling
scheme, which learns the statistical optimal day-ahead scheduling from the
historical forecasts and forecasting errors.
Figure 3: The proposed deep learning based training approach for deep neural network
gθ(·; θg), which takes the day-ahead forecasts Ft ≜{Lt
E, Lt
H, Sk,t
W , Sk,t
PV} as inputs and gives
the statistical day-ahead scheduling St
Sch ≜{St
E, St
G, Sk,t
EV, Sk,t
TES, vt} as outputs.
14


---

Page 15

---

3.1. A Deep Learning Based Approach for the Day-Ahead Scheduling under
Multiple Uncertainties
The proposed deep learning based approach for the day-ahead scheduling
under multiple uncertainties is illustrated in Fig. 3. It consists of a deep
neural network gθ(·; θg) with a parameter set θg, whose inputs are the day-
ahead forecasts Ft and outputs are the day-ahead scheduling St
Sch as follows:
St
Sch = gθ(Ft; θg),
(26)
where the parameter set θg is trained following Fig. 3. Once the train-
ing procedure is completed, the deep neural network (DNN) gθ(·; θg) itself
is suﬃcient to commit the day-ahead scheduling task.
The actual total
cost Ct
ALL in (19) can be rewritten by the outputs of the DNN gθ(·; θg)
as Ct
ALL(˜Ft, gθ(Ft; θg))Ct
ALL(˜Ft, g(Ft; θg)). In this way, the original prob-
lem P1 is transformed to a deep learning problem in ﬁnding the optimal
parameter set θg.
3.2. Enforcing the Physical Constraints
It is challenging to exploit the DNN to address general problems with
physical constraints. This is because in the context of energy systems, each
DNN output is with physical interpretations, e.g., the energy amounts or
the control ratios. Based on their physical meanings in the real world, they
could be involved in multiple physical constraints at the same time. This
paper addresses all physical constraints via: a) the “Constraint Enforce-
ment” module at the DNN’s output layer as illustrated in Fig. 3, and b)
the penalty terms in the loss function design, which are detailed as follows:
• The energy ﬂow constraints in (3)-(7), (10) and (15) are enforced by
scaling the energy ﬂow values to the range speciﬁed by the minimal and
maximal limits. Speciﬁcally, this is implemented by: a) transforming
energy ﬂow output of the transformer, wind turbines, PVs, and CHPs
into the range of [0, 1], and then scaling them by their corresponding
minimal and maximal limits, and b) transforming each energy ﬂow
output of EVs and TESs into the range of [−1, 1], and then scaling
them by their corresponding minimal and maximal limits.
• The daily net energy ﬂow constraints of EVs and TESs in (11) and (16)
are enforced by subtracting their corresponding daily average values.
Speciﬁcally, this is implemented by: a) ﬁrstly calculating the daily
average energy ﬂows of each EV and TES, b) substracting each energy
15


---

Page 16

---

ﬂow value by the corresponding daily average energy ﬂow value, and
c) scaling each energy ﬂow value to meet the energy ﬂow constraints
(10) and (15).
• The EVs’ SOC and TESs’ SOC related constraints in (13) and (18)
are regarded as penalty terms, which is formulated as follows:
Ct
Penalty

gθ(Ft; θg)

=
max{SOCMIN
EV −SOCk,t
EV, SOCk,t
EV −SOCMAX
EV
, 0}
|
{z
}
EVs’ SOC Constraints
+
max{SOCMIN
TES −SOCk,t
TES, SOCk,t
TES −SOCMAX
TES , 0}
|
{z
}
TESs’ SOC Constraints
.
(27)
• The loss function L(θg) in Fig. 3 is deﬁned as follows:
L(θg) =EFt,δt
(
T
X
t=1
Ct
ALL

˜Ft, gθ(Ft; θg)

+ λ
T
X
t=1
Ct
Penalty

gθ(Ft; θg)
)
,
(28)
where the penalty parameter λ is a positive scalar.
Then the day-ahead scheduling under multiple uncertainties can be trans-
formed to the equivalent unconstrained deep learning problem as follows:
min
θg L(θg),
(29)
which is trained in an unsupervised manner in this paper. Note that here
the unsupervised training method is used instead of the supervised training
method. This is because, in the studied practical DT system, the multiple
uncertainty sources can have unknown statistical properties, which makes
it impractical to calculate the optimal solutions with each DT system in-
put required by the supervised training method. Instead, the unsupervised
training method is applied, which trains the NN to optimize the DT end
performance, by learning from the underlying relationship between the DT
system input, multiple uncertainty sources, and the DT system end perfor-
mance.
Note that in P1, the expectation is with regard to δt, i.e., the solution
16


---

Page 17

---

is bind to the speciﬁc day-ahead forecast Ft, while it requires a totally new
search for other inputs. Diﬀerent from that, the mathematical expectation
of L(θg) in (28) is with respect to both δt and Ft, i.e., the solutions for
diﬀerent Ft can be obtained via the same trained DNN gθ(·; θg).
3.3. Data Augmentation based Approach for Statistical Training
During the training procedure, the outputs of gθ(·; θg) need to be eval-
uated in a statistical way, which is achieved by calculating the loss function
L(θg) against all potential actual values under random forecasting errors.
In this paper, we study the day-ahead scheduling problem with multiple un-
certainties δt = {δt
E, δt
H, δt
W, δt
PV}, including the electricity load forecasting
error δt
E =
˜Lt
E−Lt
E
Lt
E
, the heat load forecasting error δt
H =
˜Lt
H−Lt
H
Lt
H
, the wind
energy forecasting error δt
W =
˜St
W−St
W
St
W
, and the solar energy forecasting error
δt
PV =
˜St
PV−St
PV
St
PV
. In this way, for each given day-ahead forecast Ft, a set of
forecasting errors δt can be randomly selected from historical observations
or simulations, which together generate an augmented set of actual values
˜Ft as illustrated in Fig. 3.
The data augmentation based approach for the statistical training of
gθ(·; θg) is detailed as follows:
• For each forecast vectors, a training data set can be generated by
historical observations or simulations, which forms the total forecast
dataset Ft. During the training procedure, a subset of day-ahead fore-
casts Ft is randomly sampled from the total forecast dataset Ft.
• The forecasting error data set ∆t can be generated by historical obser-
vations or simulations. During the training procedure, a subset of fore-
casting errors δt is randomly sampled from ∆t. Then the correspond-
ing potential actual values ˜Ft are calculated via the day-ahead fore-
casts Ft and the sampled forecasting errors δt, where ˜Ft = { ˜F t| ˜F t =
(1 + δt)F t, ∀δt ∈δt, ∀F t ∈Ft}.
• The DNN gθ(·; θg) takes the day-ahead forecasts Ft as inputs, and
gives the statistical day-ahead scheduling St
Sch as outputs.
• For each statistical day-ahead scheduling St
Sch, it is evaluated against
each potential actual values from the augmented data set ˜Ft, which
forms the loss function L(θg) in (28).
17


---

Page 18

---

• For each training step τ, the DNN parameters θg are updated via the
Gradient Descent algorithm [21] as follows:
θ(τ)
g
= θ(τ−1)
g
−α∇θgL(θ(τ−1)
g
),
(30)
where α is the learning rate of the training procedure.
Table 1: Parameters in the Case Studies
Parameter
Description
Value
ηTF
Transformer’s eﬃciency
0.980
ηE
CHP
CHP’s power generation eﬃciency
0.404
ηH
CHP
CHP’s thermal recovery eﬃciency
0.566
ηB
Boiler’s thermal eﬃciency
0.900
ηCh
EV
EV’s charging eﬃciency
0.900
ηDCh
EV
EV’s discharging eﬃciency
0.900
ηCh
TES
TES’s charging eﬃciency
0.900
ηDCh
TES
TES’s discharging eﬃciency
0.900
SMAX
TF
Transformer’s Max. energy ﬂow per hour
1000 kWh
SMAX
G
Natural Gas’s Max. energy ﬂow per hour
1200 kWh
SMAX
W
Wind Turbine’s Max. energy ﬂow per hour
200 kWh
SMAX
PV
Solar Panel’s Max. energy ﬂow per hour
200 kWh
SMAX
CHP
CHP’s Max. energy ﬂow per hour
300 kWh
SMAX
B
Boiler’s Max. energy ﬂow per hour
800 kWh
SCh, MAX
EV
EV’s Max. Charging energy ﬂow per hour
80 kWh
SDCh, MAX
EV
EV’s Max. Discharging energy ﬂow per hour
80 kWh
SCh, MAX
TES
TES’s Max. Charging energy ﬂow per hour
50 kWh
SDCh, MAX
TES
TES’s Max. Discharging energy ﬂow per hour
50 kWh
SOCMIN
EV
EV’s Min. energy capacity
40 kWh
SOCMAX
EV
EV’s Max. energy capacity
80 kWh
SOCMIN
TES
TES’s Min. energy capacity
40 kWh
SOCMAX
TES
TES’s Max. energy capacity
200 kWh
4. Case Studies
To evaluate the proposed method, an IES with 4 EVs and 2 TESs is
considered. The virtual replica of the IES is modelled as a MVES model that
interacts with its physical twin, as well as the forecasting services and energy
markets, as illustrated in Fig. 2. The time interval for each scheduling slot
is 1 hour, thus one day has T = 24 scheduling slots. Note that this 1 hour
time interval is selected as an example because the hourly forecasts and
actual data are used in the case study, which can be adjusted according
to speciﬁc system conﬁgurations.
Correspondingly, the input day-ahead
forecasts Ft ≜{Lt
E, Lt
H, Sk,t
W , Sk,t
PV} are row vectors with a length of 96, while
the output day-ahead scheduling St
Sch ≜{St
E, St
G, Sk,t
EV, Sk,t
TES, vt} are row
vectors with a length of 216. A DNN with 3 hidden layers is used, where
18


---

Page 19

---

each hidden layer is implemented via a fully connected layer with the size of
768, 576 and 384, respectively. The Parametric ReLU function is exploited
as the activation function for the input layer and each hidden layer, which
returns max(0, x) + 0.25 min(0, x) for a given input x. The outputs of the
ﬁnal fully connected layer are processed via the “Constraint Enforcement”
module, which is illustrated in Fig. 3 and speciﬁed in Section 3.2.
The day-ahead forecasts and real-time actual values of electricity loads,
the wind energy generation and the solar energy generation are scaled from
the U.K. historical records [6], while the heat loads are following the proﬁle of
domestic hot water consumption in [22], whose forecasting errors are gener-
ated with the proﬁle in [23]. The training dataset is generated as follows: a)
for the forecast dataset, the full year’s forecasts in 2019 are linearly combined
in a random manner to form a dataset with a total of 56172 forecast vectors,
and b) for the forecasting error dataset, the forecasts and actual values in
2019 are used to calculate the forecasting errors and a dataset with a length
of 233 is generated, where the days with missing records and extreme errors
(e.g., forecasting errors large than 45%) are excluded. The average day-
ahead wholesale prices and real-time prices in the 2019 U.K. markets [6][24]
are used, where CDA
E =£0.031/kWh, CDA
G =£0.013/kWh, C+
E =£0.058/kWh,
C−
E =£0.025/kWh, C+
G=£0.022/kWh and C−
G=£0.011/kWh. The reward-
ing rates are CW = £0.02/kWh, CPV = £0.02/kWh, CEV = £0.03/kWh
and CTES = £0.01/kWh.
The proposed training method in Section III is used, which is illustrated
in Fig. 3. The Adam optimiser [25] with a learning rate of 10−5 is used
to train the DNN in an unsupervised manner, where the penalty parameter
λ = 1 is used. To accelerate the training procedure, the mini-batch method
is used, where the batch sizes for the day-ahead forecasts and the forecast-
ing errors are empirically set as 4 and 55, respectively. During each training
epoch, 10000 batches of day-ahead forecasts are used. To evaluate the pro-
posed method, the trained DNN is used for several case studies detailed
in the following subsection, while the existing scheduling method based on
day-ahead forecasts without forecasting error considerations is used as the
benchmark algorithm.
To evaluate the proposed method, the trained DNN with the historical
forecasts and forecast errors is used for the case studies to be detailed in
the following subsections. Moreover, the day-ahead scheduling outputs of
the DNN are used as the MVES scheduling decisions, while the real-time
operation between the virtual replica MVES and the physical IES is detailed
in Section 2.2.
For the benchmark algorithm, the existing scheduling method based on
19


---

Page 20

---

day-ahead forecasts without forecasting error considerations is used. Specif-
ically, the benchmark scheduling algorithm takes the day-ahead forecasts as
inputs, and makes scheduling decisions so that for each scheduling slot, the
energy supply by the IES meets the forecasted energy demands.
4.1. A Case Study on the Hourly Cost Performance
The IES day-ahead scheduling outputs are the hourly scheduled oper-
ations for the CHPs, EVs and TESs, as well as the purchased electricity
and natural gas from the day-ahead markets. Therefore the ﬁrst case study
is focused on the hourly cost performance, where the trained DNN via the
proposed deep learning method is evaluated using a whole day’s data (i.e.,
the complete 24 hours) in 2019, and the detailed hourly cost performance is
reported in Fig. 4.
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
11
12
13
14
15
16
17
18
19
20
21
22
23
24
Hour
5
10
15
20
25
30
Cost (GBP)
Proposed Deep Learning Based Method
Benchmark using Forecasts Directly
Figure 4: The hourly cost for 24 hours within one day, with 4 EVs and 2 TESs.
Comparing to the benchmark method, the proposed deep learning based
method achieves better performance with reduced costs for most hours, while
there are a few exceptions for the 3rd, 7th, 20th and 23rd hour, as illustrated
in Fig.
4.
This performance is expected, because the proposed method
learns from historical errors and makes the statistically optimal schedul-
ing decisions, i.e., the scheduling decision will: a) reduce the cost as much
as possible for the most possible scenarios with the multiple uncertainty
sources, and b) allow the cost to be increased for some scenarios while the
long-term costs are still reduced. Regarding the performance of executing
time, the benchmark algorithm completes the day-ahead scheduling with
20


---

Page 21

---

an average of 0.355 s, while the proposed method completes the day-ahead
scheduling with an average of 0.002 s. The millisecond-level execution time
of the proposed method is because after the DNN is trained, the day-ahead
scheduling decision can be obtained by feeding the day-ahead forecasts to
the DNN. Since the NN parameters and structures are ﬁxed, the execution
time of inference is short.
4.2. A Case Study on the Daily Cost Performance
The day-ahead scheduling decisions via the proposed method are for the
24-hour period (i.e., the whole day), where the IES devices are coordinated
and scheduled to reduce the cost on a daily basis. Therefore in this case
study, the daily cost performance is evaluated using the 31 days’ data within
one calendar month in May, 2019, whose results are presented in Fig. 5. It
can be seen that the proposed method is capable to reduce the daily costs
for 27 days out of the total 31 days. This agrees well with the aim of the
proposed method, which generally reduces the daily cost for the IES.
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
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
Day
300
400
500
600
Cost (GBP)
Proposed Deep Learning Based Method
Benchmark using Forecasts Directly
Figure 5: The daily cost for 31 days within one calendar month, with 4 EVs and 2 TESs.
4.3. A Case Study on the EV and TES Performance
The considered IES integrates multiple EVs and TESs, which are ex-
ploited as energy buﬀers in support of both electricity and thermal energy
scheduling across the whole day. The averaged cost performance for each
cost category is studied using 31 days’ data in May, 2019, and the perfor-
mance for the benchmark method and the proposed method are presented
in Fig. 6.
21


---

Page 22

---

The Benchmark Method
EV(66GBP)
TES(25GBP)
CExtra (88GBP)
Scheduled
 Electricity
(269GBP)
Wind(44GBP)
PV(49GBP)
Scheduled
Natural Gas
(256GBP)
The Proposed Method
EV(78GBP)
TES(39GBP)
CExtra (68GBP)
Scheduled 
Electricity
(293GBP)
Wind(44GBP)
PV(49GBP)
Scheduled 
Natural Gas
(256GBP)
Figure 6: The daily averaged cost performance of the benchmark method using forecasts
directly and the proposed deep learning based method, with 4 EVs and 2 TESs.
Comparing to the benchmark method, it can be seen from Fig. 6 that
the proposed method pays more to the usage of EVs and TESs.
Since
EVs and TESs are paid by their absolute energy ﬂows, it indicates the
proposed method is scheduling more usage (charging or discharging) of the
EVs and TESs across the day, comparing to the benchmark method. By
jointly considering the reduced extra cost CExtra from Fig. 6, as well as the
daily cost reduction for most days from Fig. 5, it can be inferred that the
proposed method shows a better performance in coordinating the EVs and
TESs to help address the multiple uncertainty challenges, comparing to the
benchmark method. The payments to the EVs and TESs are increased by
18.2% and 56%, respectively, which is beneﬁcial to the IES as it will further
encourage the participants of the EVs and TESs with a ﬁnancial stimulation.
4.4. A Case Study on the 2018 U.K. Dataset
During the training procedure of the proposed method, the training
dataset for day-ahead forecasts and errors is generated from the U.K. histori-
cal data in 2019. In this case study, the trained DNN model will be evaluated
using the U.K. historical data in 2018, in order to test if the obtained model
is general to be applicable with the unknown dataset. The monthly cost
for each calendar month in 2018 is reported in Fig. 7. It can be seen that
the trained DNN model can still achieve the expected cost reduction per-
formance, comparing to the benchmark method. It should be noticed that
the proposed method exploits unsupervised training method, i.e., the DNN
learns to reduce the cost without knowing the theoretical optimal day-ahead
scheduling. This case study using U.K. data in 2018, together with the re-
sults in previous case studies, demonstrates that the proposed deep learning
method is able to learn a practical and statistical solution for the day-ahead
scheduling problem under multiple uncertain sources.
22


---

Page 23

---

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
11
12
Month
0.8
1
1.2
1.4
1.6
Cost (GBP)
10 4
Proposed Deep Learning Based Method
Benchmark using Forecasts Directly
Figure 7: The monthly cost for the complete 12 months using 2018 U.K. dataset, with 4
EVs and 2 TESs.
The average daily costs in 2018 are detailed in Table 2, where the ideal
case is calculated with no forecasting errors. Comparing to the ideal case, it
can be calculated that the benchmark method pays a daily extra operating
cost of £34.5, while the proposed method pays a daily extra operating cost
of £12.6. This means the proposed method reduces 63.5% of the average
daily extra operating cost induced by the multiple uncertainties, and a 5.1%
of the total average daily operating cost.
Table 2: Daily Cost Performance with 4 EVs and 2 TESs
Ideal
Case
Proposed
Method
Benchmark
Method
Cost Due to
Physical Constraint
Adjustment
Cost
(£)
393.9
406.5
428.4
0.0012
4.5. A Case Study on Physical Constraint Adjustment Costs
In this paper, the day-ahead scheduling decisions are outputs from a
DNN, which should satisfy all the physical constraints as detailed in Sec-
tion III. In the proposed method, the physical constraints regarding EVs’
SOC and TESs’ SOC are addressed via the loss function in (28), while the
rest constraints are enforced via the “Constraint Enforcement” module em-
bedded in DNN output layer. During the aforementioned case studies, the
outputs of the trained DNN are further enforced to meet the EVs’ SOC
and TESs’ SOC, where the scheduled EVs’ energy ﬂow and TESs’ energy
ﬂow will be adjusted if their SOC are not met at any scheduled slot. This
23


---

Page 24

---

ensures the DNN satisﬁes all IES physical constraints for practical usage,
but it could incur some additional costs since it is not as initially scheduled.
As detailed in Table 2, it is seen the average additional cost due to physical
constraint adjustment is £0.0012, which is marginal to the daily costs. This
also demonstrates that the proposed deep learning method is able to address
the practical problems with multiple physical constraints.
4.6. A Case Study on Large System Setup
This case study evaluates the proposed method with a larger system
setup, where the numbers of EVs and TESs are increased to 6 and 4, re-
spectively. Besides, the thermal load demands have been increased by 20%,
which together with the increased number of EVs and TESs will test the
eﬀectiveness of the proposed method with the increased balance of supply
and demand.
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
11
12
Month
0.8
1
1.2
1.4
1.6
Cost (GBP)
10 4
Proposed Deep Learning Based Method
Benchmark using Forecasts Directly
Figure 8: The monthly cost for the complete 12 months using 2018 U.K. dataset, with 6
EVs and 4 TESs.
We use the 2019 UK dataset as the training data and the 2018 UK
dataset for testing. The experimental results are illustrated in Fig. 8. It
can be observed that for 11 out of 12 months, the proposed method is able
to reduce the monthly cost, comparing against the benchmark method. It
also demonstrates the eﬀectiveness of the proposed method under diﬀerent
system setups, e.g., more EVs and TESs as well as an increased balance of
supply and demand. By jointly considering Fig. 7, it can be seen that for
each month, the monthly cost has been much reduced in Fig. 8. This is
because although the thermal load demands have been increased by 20%,
the eﬀect of the operating cost reduction due to EVs and TESs is more
prominent when their numbers are increased. Together with the case study
24


---

Page 25

---

on EVs and TESs in Section 4.3, the proposed method illustrates a better
coordination strategy than the benchmark method.
5. Conclusions
In this paper, a novel day-ahead scheduling scheme is proposed for the
DT based IES. The proposed method enables active interactions between
virtual replica and physical IES to form a DT system.
Additionally, a
deep learning method is proposed to make a statistically optimal day-ahead
scheduling, by learning from historical forecasting errors and day-ahead fore-
casts. The challenging issue of multiple uncertainty sources is addressed via
the proposed data augmentation based training method.
Meanwhile, all
physical constraints are enforced via both the designs of network architec-
tures and the loss functions design.
The performance is evaluated using
case studies of historical U.K. data in 2018 and 2019. Comparing with the
benchmark method using forecasts directly, the proposed method reduces
the average daily extra operating cost by 63.5%, which shows a promis-
ing solution to reduce the long-term IES operating cost.Compared with the
benchmark method, the proposed method reduces the long-term IES oper-
ating cost. It can actively schedule EVs and TESs to better address the
multiple uncertainty challenges in future energy systems, paving the way for
realising net-zero target.
For future research, we will further extend the proposed model and
method to study their potential in carbon emission reduction. Moreover,
the short-term forecasts and energy markets will be considered, where the
proposed scheduling might be improved to further reduce the operation cost,
e.g., by the intra-day rolling forecasts to update the scheduling decisions.
Besides, we will evaluate the proposed method in larger systems, includ-
ing more equipment types, more EVs and TESs in numbers, and a larger
balance of energy supply and demand. In addition, more advanced real-
time scheduling to involve diﬀerent IES facilities will be considered, which
might lead to further reduced operating costs together with the day-ahead
scheduling.
Besides the random based data augmentation method, other
general data augmentation methods will be investigated to better prepare
the training data set and support the NN to learn the hidden forecasting
error patterns.
25


---

Page 26

---

Acknowledgement
This work was supported by the Department for Business, Energy &
Industrial Strategy (BEIS) through the project of “Ubiquitous Storage Em-
powering Response (USER)” https://www.theuserproject.co.uk/.
References
[1] Skarvelis-Kazakos S, Papadopoulos P, Grau Unda I, Gorman T, Belaidi
A, Zigan S. Multiple energy carrier optimisation with intelligent agents.
Applied Energy 2016; 167:323–35. doi:10.1016/j.apenergy.2015.10.130.
[2] Wang H, Gu C, Zhang X, Li F. Optimal CHP planning in integrated
energy systems considering network charges. IEEE Systems Journal
2020; 14(2):2684–93. doi:10.1109/JSYST.2019.2921218.
[3] Moeini-Aghtaie M, Dehghanian P, Fotuhi-Firuzabad M, Abbaspour
A.
Multiagent genetic algorithm:
an online probabilistic view on
economic dispatch of energy hubs constrained by wind availabil-
ity.
IEEE Transactions on Sustainable Energy 2014; 5(2):699–708.
doi:10.1109/TSTE.2013.2271517.
[4] Darbali-Zamora R, Johnson J, Summers A, Jones CB, Hansen C,
Showalter C. State estimation-based distributed energy resource op-
timization for distribution voltage regulation in telemetry-sparse en-
vironments using a real-time digital twin.
Energies 2021; 14(3).
doi:10.3390/en14030774.
[5] Barricelli BR, Casiraghi E, Fogli D. A survey on digital twin: Def-
initions, characteristics, applications, and design implications. IEEE
Access 2019; 7:167653–7. doi:10.1109/ACCESS.2019.2953499.
[6] Balancing
Mechanism
Reporting
Service.
2020.
URL:
https://www.bmreports.com/; [Accessed 21 January 2020].
[7] Xiang Y, Cai H, Gu C, Shen X. Cost-beneﬁt analysis of integrated
energy system planning considering demand response. Energy 2020;
192:116632. doi:https://doi.org/10.1016/j.energy.2019.116632.
[8] National Grid ESO . Future energy scenarios 2019 documents. 2020.
URL: http://fes.nationalgrid.com/fes-document/; [Accessed 21
January 2020].
26


---

Page 27

---

[9] Ge S, Xu Z, Liu H, Gu C, Li F. Flexibility evaluation of active distribu-
tion networks considering probabilistic characteristics of uncertain vari-
ables. IET Generation, Transmission & Distribution 2019; 13(14):3148–
57. doi:10.1049/iet-gtd.2019.0181.
[10] Liu F, Bie Z, Wang X. Day-ahead dispatch of integrated electricity and
natural gas system considering reserve scheduling and renewable uncer-
tainties. IEEE Transactions on Sustainable Energy 2018; 10(2):646–58.
doi:10.1109/TSTE.2018.2843121.
[11] Salkuti SR.
Day-ahead thermal and renewable power generation
scheduling considering uncertainty. Renewable energy 2019; 131:956–
65. doi:10.1016/j.renene.2018.07.106.
[12] Fan C, Wang J, Gang W, Li S.
Assessment of deep recurrent neu-
ral network-based strategies for short-term building energy predictions.
Applied Energy 2019; 236:700–10. doi:10.1016/j.apenergy.2018.12.004.
[13] Theocharides S, Makrides G, Livera A, Theristis M, Kaimakis P,
Georghiou GE. Day-ahead photovoltaic power production forecasting
methodology based on machine learning and statistical post-processing.
Applied Energy 2020; 268:115023. doi:10.1016/j.apenergy.2020.115023.
[14] Zhu C, Tian W, Yin B, Li Z, Shi J. Uncertainty calibration of build-
ing energy models by combining approximate bayesian computation
and machine learning algorithms. Applied Energy 2020; 268:115025.
doi:10.1016/j.apenergy.2020.115025.
[15] Zhang L, Wen J, Li Y, Chen J, Ye Y, Fu Y, et al. A review of machine
learning in building load prediction. Applied Energy 2021; 285:116452.
doi:10.1016/j.apenergy.2021.116452.
[16] Teo T, Logenthiran T, Woo WL, Abidi K. Near-optimal day-ahead
scheduling of energy storage system in grid-connected microgrid. In:
Proc. IEEE Innovative Smart Grid Technologies-Asia. Singapore; 2018,
p. 1257–61. doi:10.1109/ISGT-Asia.2018.8467921.
[17] Zhou M, Wang B, Watada J. Deep learning-based rolling horizon unit
commitment under hybrid uncertainties.
Energy 2019; 186:115843.
doi:10.1016/j.energy.2019.07.173.
[18] Zhang C, Li R, Shi H, Li F. Deep learning for day-ahead electricity
price forecasting. IET Smart Grid 2020; 3(4):462–9. doi:10.1049/iet-
stg.2019.0258.
27


---

Page 28

---

[19] Agostinelli S, Cumo F, Guidi G, Tomazzoli C. Cyber-Physical Systems
Improving Building Energy Management: Digital Twin and Artiﬁcial
Intelligence. Energies 2021; 14(8):2338. doi:10.3390/en14082338.
[20] Edward O’D, Indranil P, Richard C, Sarah B, Nilay S. Integration of an
energy management tool and digital twin for coordination and control
of multi-vector smart energy systems. Sustainable Cities and Society
2020; 62:102412. doi:10.1016/j.scs.2020.102412.
[21] Sutskever I, Martens J, Dahl G, Hinton G. On the importance of ini-
tialization and momentum in deep learning. In: Proceedings of the 30th
International Conference on Machine Learning. Atlanta, USA; 2013, p.
1139–47.
[22] Gelaˇzanskas L, Gamage KA. Forecasting hot water consumption in resi-
dential houses. Energies 2015; 8(11):12702–17. doi:10.3390/en81112336.
[23] Balint A, Kazmi H.
Determinants of energy ﬂexibility in residen-
tial hot water systems.
Energy and Buildings 2019; 188:286–96.
doi:10.1016/j.enbuild.2019.02.016.
[24] National Grid Gas. National grid gas transmission data. 2020. URL:
https://www.nationalgridgas.com/balancing; [Accessed 21 Jan-
uary 2020].
[25] Kingma DP, Ba J. Adam: A method for stochastic optimization. In:
Proc. 3rd International Conference on Learning Representations, San
Diego, CA, USA. 2015, p. 1–15.
28
