

---

Page 1

---

© 2019 IEEE. Personal use of this material is permitted.  Permission from IEEE must be obtained for all other uses, in any cur-
rent or future media, including reprinting/republishing this material for advertising or promotional purposes, creating new col-
lective works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of this work in other works.
 
 
 
 


---

Page 2

---

1949-3053 (c) 2019 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TSG.2019.2945694, IEEE
Transactions on Smart Grid
 
1
 
Abstract--Future distribution systems are expected to display 
increased complexity, mainly due to looped/meshed operation, 
switch between grid-connected and islanded mode and consider-
able integration of distributed generation. This paper investigates 
a plug-and-play protection solution for overhead distribution 
systems with such variable operation conditions, employing exist-
ing numerical relay capabilities. This solution is applied by de-
signing plug-and-play, communication-assisted, multifunctional 
relays with integrated protection element settings, which apply 
universally to all distribution system conditions, rendering the 
protection scheme independent of a specific system. Hence, the 
need for user-defined settings or future revisions due to system 
changes is eliminated. The scheme ensures coordination between 
main line relays and backup protection of laterals, without a co-
ordination study. There is no need to replace or modify existing 
lateral protection means for this purpose; only their known time-
overcurrent curves are uploaded to the relays by the user. The 
scheme is described and evaluated through simulations in two 
test systems. Meaningful conclusions are finally derived. 
 
Index Terms--Distributed generation, distribution system, 
meshed network, plug-and-play protection. 
I.  INTRODUCTION 
UTURE distribution systems are envisioned including a 
considerable amount of distributed generation (DG), oper-
ating in a looped or meshed network configuration (i.e. in a 
looped configuration, also including interconnection line seg-
ments) and freely switching between grid-connected (GC) and 
islanded (ISL) mode. Among others, advanced protection 
schemes are needed for such a complex system operation. 
Determining proper relay settings is a challenging task. In 
fact, besides technical reasons, a common cause of protection 
maloperation is incorrect relay setting [1]. Even in conven-
tional overhead (OH) radial distribution systems, setting the 
main line relay(s) requires a cumbersome simulation study, 
mainly due to the need for coordination with lateral protection 
means. Obviously, the difficulty increases considerably in 
looped/meshed distribution networks with DG, due to the in-
creased network’s complexity and the need for frequent relay 
setting revisions, given the continuous expected changes (e.g. 
connection of new DG units). Hence, it becomes a necessity to 
investigate reliable protection concepts, which eliminate the 
 
The research work was supported by the Hellenic Foundation for Research 
and Innovation (HFRI) and the General Secretariat for Research and Technol-
ogy (GSRT), under the HFRI PhD Fellowship grant (GA. no. 19773). 
A. M. Tsimtsios and V. C. Nikolaidis are with the Department of Electri-
cal and Computer Engineering, Democritus University of Thrace, Xanthi 
67100, Greece (e-mails: atsimtsi@ee.duth.gr; vnikolai@ee.duth.gr). 
need for simulation-based user-defined settings, being, as far 
as possible, independent of a specific network. Distribution 
system particularities (e.g. existence of laterals) and existing 
relay capabilities should also be considered. To the best of the 
authors’ knowledge, so far, papers focusing on protection of 
looped/meshed distribution systems have not addressed a 
“leave-and-forget” concept including all the above attributes. 
Several papers focusing on the protection of looped or 
meshed distribution systems with DG apply directional over-
current relays (DOCRs). Optimization algorithms have been 
recently proposed for setting DOCRs [2]-[4]. In [2], DOCRs 
are optimally set for both the GC and the ISL mode of system 
operation, without using communication means. In [3], [4], 
communication-assisted protection schemes are applied, using 
dual-setting DOCRs. The latter are optimally set, while, block-
ing signals are used to ensure selectivity. However, to produce 
optimal settings, these algorithms require data extracted from 
the specific system and/or system conditions considered. Also, 
they do not address coordination with lateral protection. 
Communication/pilot-based DOCR schemes have been also 
proposed in [5]-[8]. The authors of [5] apply DOCRs employ-
ing blocking and inter-trip signals, to ensure selectivity and 
isolation of the faulted line segment, respectively. The exten-
sion of this scheme to looped and meshed networks is also 
discussed. DOCRs are applied to protect a looped distribution 
network with DG in [6], based on a permissive logic. In [7], 
[8], permissive/blocking-based DOCR schemes are considered 
for real looped distribution networks. Proper relay setting is 
required in [5]-[8], based on the specific system to protect. 
Differential protection has been also considered for 
looped/meshed distribution systems with DG [9]-[11]. To en-
sure both sensitivity and security, proper setting of differential 
relays is required, especially when loads and/or DG units are 
connected within the differential protection zone [11], [12]. 
Especially in [11], where the proposed multi-agent differential 
scheme must coordinate with the lateral fuses, the relays must 
be further set for this purpose. Also, a drawback of commer-
cial differential relays is their inability to inherently protect 
network-parts outside of their primary protection zone [12]. 
In [13], a communication-assisted multi-agent protection 
scheme is proposed, using current phase angle comparison. To 
define the angle setting, an extensive simulation study is need-
ed. Coordination with lateral protection is also not addressed. 
Communication/pilot-based distance protection schemes 
for looped/meshed distribution systems with DG are proposed 
in [14], [15]. The scheme of [14] mainly applies a permissive 
logic, while, it also uses blocking signals only against weak-
Towards Plug-and-Play Protection for     
Meshed Distribution Systems with DG 
Aristotelis M. Tsimtsios, Student Member, IEEE, and Vassilis C. Nikolaidis, Senior Member, IEEE 
F


---

Page 3

---

1949-3053 (c) 2019 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TSG.2019.2945694, IEEE
Transactions on Smart Grid
 
2
infeed conditions. An extensive simulation study in the pro-
tected network is required to set the distance relays. In [15], 
both a pilot-based (using permissive and blocking signals) and 
a central distance protection scheme are proposed. Proper set-
ting is required for the distance relays, while, coordination 
with common lateral protection means is not addressed. 
Multifunctional protection schemes for distribution systems 
with DG, using communication means, are proposed in [16] 
(employing, among others, directional-overcurrent, undervolt-
age and high-impedance-fault-detection functions) and [17] 
(employing differential and directional-overcurrent functions). 
Proper relay settings have to be determined for these schemes, 
especially for backup protection coordination purposes. 
Communication-assisted adaptive protection schemes have 
been also proposed for looped/meshed distribution systems 
with DG, employing different setting groups [18]-[20]. In 
[18], [19], each setting group of the applied DOCRs is defined 
in advance using optimization algorithms. Adaptive distance 
relays are considered in [20]. The main challenge in these ap-
proaches is that they require offline load-flow/short-circuit 
studies in the protected network, considering all the possible 
configurations. A solution to optimally determine the required 
number of setting groups for each DOCR is proposed in [21]. 
A different adaptive approach is followed in [22], which cal-
culates the new DOCR settings based on an initial setting 
group, stored in the relays in advance. The initial settings are 
calculated based on the specific system to protect. Multi-agent 
adaptive approaches are proposed in [23], [24], while, online 
adaptive protection is applied in [25]. These schemes have to 
be set/designed based on data extracted from the specific sys-
tem protected. Moreover, none of [18]-[25] addresses coordi-
nation with existing lateral protection means. 
Finally, several research efforts examine alternative protec-
tion solutions for looped/meshed distribution networks, not 
based on commercial relay functions. Protection techniques 
applying data-mining [26], [27], machine learning [28] and 
deep neural networks [29] have been proposed among others, 
which, however, require a training process, based on scenarios 
of the specific network examined. Other techniques regard 
dynamic-state-estimation-based protection [30], interval type-
2 fuzzy logic [31] and checking power direction of the posi-
tive-sequence fault component, as part of a blocking-signal-
based pilot protection scheme [32]. In [26]-[32], coordination 
with existing lateral protection means is not addressed. 
To sum up, the protection schemes proposed so far for 
looped/meshed distribution systems are characterized by one 
or more of the following drawbacks: 
i) 
They require extensive relay setting studies, taking into 
account any possible fault and system configuration sce-
nario. As mentioned before, this might be complex in 
looped/meshed distribution systems with DG. 
ii) They are set/designed based on data of the specific net-
work to protect, which renders them vulnerable to un-
planned system changes (e.g. new DG connection, change 
in the short-circuit capacity of the external grid, etc.). 
iii) Either they do not address coordination between the main 
line relays and existing lateral protection means, or they 
require properly setting the relays to achieve coordination. 
To address all the above drawbacks, eliminating protection 
system design complexity in modern OH distribution systems, 
a plug-and-play (PnP) protection solution is investigated in 
this work. The main contribution/novelty of this solution, 
compared to other proposed protection solutions, is reflected 
on the concurrent fulfillment of the following: 
 
The PnP relays do not need user-defined settings, typical-
ly resulting from a simulation study. Instead, they are de-
signed by default to deal with any fault/system scenario. 
 
The protection scheme is independent of a specific OH 
distribution system and immune to planned or unplanned 
system changes, such as switch between GC and ISL 
mode, connection/disconnection of DG units or line seg-
ments etc. Hence, applying adaptive logic is not needed, 
while, the need for future setting revisions is eliminated. 
 
The PnP relays operate selectively with each other and 
with the existing lateral protection (even non-settable fus-
es), without needing a coordination study. Especially the 
latter is automatically achieved, by simply uploading the 
characteristics of lateral protection means to the relays. 
It should be mentioned that the proposed scheme addresses 
non-resistive/resistive faults of any type/location. Also, the 
PnP relays are intentionally designed by properly combining 
existing protection techniques, applicable with commercial 
relay technology. This is to enhance the schemes’ practicality. 
The novelty of the proposed solution is also reflected on the 
way that these individual techniques are combined. 
This paper is organized as follows. The basic logic of the 
proposed scheme and its design using PnP relays is described 
in Section II and III, respectively, while, its performance is 
evaluated in Section IV. Section V includes a comparison with 
differential protection. Conclusions are drawn in Section VI. 
II.  BASIC LOGIC OF THE PROTECTION SCHEME 
The PnP protection scheme is basically described via Fig. 
1, showing a part of a generic OH meshed distribution system. 
Note that the scheme’s logic, addressed below, ensures isola-
tion of the faulted line part, even if the network-loop is open. 
A.  Main Line Segment Protection 
Each main line segment Li,j, connecting buses Bi and Bj, is 
protected by two PnP, communication-assisted, multifunction-
al, numerical relays Ri,j and Rj,i, installed at its opponent ends, 
which supervise for forward faults (i.e. fault currents flowing 
into Li,j). A protection security measure is necessary here, to 
ensure that none of these relays will undesirably trip for a 
main line fault outside of Li,j. A reliable option would be to 
apply a directional-comparison-blocking (DCB)-based logic 
[1]. According to this logic, each of Ri,j and Rj,i, would block 
its opponent relay in case of detecting a reverse fault (i.e. out-
side of Li,j). An advantage of such a logic (e.g. compared to 
the permissive one) is its operability even if the looped con-
figuration is lost [7]. Although such schemes are typically 
applied to transmission lines, the use of blocking signals for 
selectivity purposes has been also proposed for distribution 
systems [3]-[5], [7], [8], [14], [15], [32]. In these applications, 


---

Page 4

---

1949-3053 (c) 2019 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TSG.2019.2945694, IEEE
Transactions on Smart Grid
 
3
blocking signals are transmitted by the relays, once they detect 
a fault in a specific direction. The particularity of this work 
compared to other relevant applications, as well as the tradi-
tional DCB logic, is that a relay does not decide on whether to 
block another relay, after determining fault direction. Instead, 
each of Ri,j and Rj,i sends a blocking signal (signals bf in Fig. 1) 
to the forward element of its opponent relay, immediately after 
detecting a probable fault situation. Only if, after at least one 
fundamental period of processing (i.e. starting, phase selection 
and fault direction determination), this situation is found to be 
a forward fault (i.e. a fault inside Li,j), bf-signal is cancelled, 
and the opponent relay is allowed to instantaneously trip its 
circuit breaker (CBi,j and CBj,i, respectively). In this way, it is 
ensured that a relay will be timely blocked in case of an exter-
nal fault, without the need to consider an intentional time de-
lay in its operation, to allow for blocking signal transmission 
(as it is a common practice [7], [32]). Finally, once a relay 
trips its CB, it inter-trips the opponent CB as well. Note that 
the inter-trip order is redundant and it is issued to ensure fault 
clearance, in the case where one of the two opponent relays 
fails to send a trip order to its CB or it cannot sense the fault. 
The latter regards either weak-infeed conditions or loss of the 
looped configuration. 
B.  Bus Protection 
For bus protection, we exploit the already installed adjacent 
relays. For instance, bus Bi in Fig. 1 is protected by Ri,j, Ri,h 
and Ri,l, which, besides supervising for forward faults to pro-
tect Li,j, Lh,i and Li,l, respectively, they also supervise for re-
verse faults to protect Bi. These relays are assumed forming a 
group of relays GRi. To enhance protection security as previ-
ously, each GRi-relay sends a blocking signal (signals br in 
Fig. 1) to the reverse element of the rest GRi-relays, immedi-
ately after detecting a probable fault situation. If, ultimately, 
this situation is found to be a reverse fault, br-signal is can-
celled. Hence, the rest GRi-relays are let trip their assigned CB 
instantaneously. In this case too, once a GRi-relay trips its CB, 
it also inter-trips the CBs of the rest GRi-relays (CBi). 
C.  Lateral Protection 
Each lateral Li is primarily protected by the protection 
means Pi installed at its departure. Pi is usually a fuse, due to 
its relatively low cost, and, less often, a conventional overcur-
rent relay. In this work, existing Pi is maintained, so as to 
avoid Pi-replacement cost. We also assume that Pi always co-
ordinates with its downstream protection means. Besides 
providing primary protection to the main line segments and 
buses, the proposed scheme also aims to provide backup pro-
tection for each lateral Li. This task is assigned to the GRi-
relays, using the same basic logic as that used for Bi protec-
tion. However, GRi-relays must further coordinate with Pi. 
Research efforts which address the issue of coordination be-
tween the main line relays and common lateral protection 
means in looped/meshed distribution systems (e.g. [11], [14]) 
require setting the main line relays properly for this purpose. 
The latter is not required by the proposed scheme, thanks to 
the internal protection logic described in the next section.  
 
Fig. 1.  Basic logic of the proposed protection scheme. 
III.  DESIGN OF THE PROPOSED PLUG-AND-PLAY RELAY 
In the following, the functional logic of a designed PnP re-
lay Ri,j is described, and is illustrated in Fig. 2. A dedicated 
element is designed against three-phase (3PH), double-phase 
(2PH), and ground (double-phase-ground (2PHG) and single-
line-ground (SLG)) faults. Two additional elements are de-
signed for addressing reverse bus/lateral faults and backup 
protection of main line segments and buses. The basic-
calculations block processes the relay measurements and gen-
erates signals which are used as an input to the rest elements. 
Fig. 2 also indicates the subsections of the paper where each 
element or element-part is discussed. 
A.  Ground (SLG/2PHG)-Fault Protection Element 
1) Starting 
To initiate the ground-fault protection element, preserving 
adequate sensitivity, an overcurrent starting function based on 
superimposed quantities is used. In general, the superimposed 
quantity ns, of a quantity n at instant t, is calculated as [33]:  
( )
( )
(
)
sn t
n t
n t
kT



                           (1) 
where k is an integer (here k = 3) and T is the fundamental 
period. ns reflects a change in n and equals (almost) zero under 
pre-fault conditions, while, it gives the pure fault signal during 
a fault.  
The starting function of the ground-fault protection element 
asserts (see Fig. 2) when the magnitude of the superimposed 
zero-sequence current (I0,s) satisfies the following condition: 
0,
3
5%
s
n
I
I


                                  (2) 
In (2), 3ꞏI0,s is the superimposed residual current; the latter is 
chosen here for the starting criterion, as it characterizes unbal-
anced ground faults. In is the nominal current of the relay’s 
current transformer (CT) and 5%In is a default overcurrent 
threshold. This threshold corresponds to a typical maximum 
current sensitivity, adopted by several commercial relays 
nowadays (e.g. [34]). The default 5%In threshold has been 
chosen so as to sensitize the starting function as much as pos-
sible, keeping up with the capabilities of commercial relays. 
Note that this threshold is not binding; if a lower current sensi-
tivity can be achieved by a relay manufacturer, a lower default 
threshold can be defined in advance. Despite sensitization, 
protection security is ensured through the proposed protection 
and communication logic (refer to the previous section).  


---

Page 5

---

1949-3053 (c) 2019 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TSG.2019.2945694, IEEE
Transactions on Smart Grid
 
4
 
Fig. 2.  Overall internal protection and communication logic of a PnP relay Ri,j designed for the proposed scheme. 
 
Equation (2) is applicable no matter the mode of system 
operation (i.e. GC vs. ISL), and even if single-phase DG units 
are connected to the network, on condition that the main sub-
station transformer or the step-up transformer of the DG units 
is grounded at the medium-voltage (MV) side. This is because, 
3ꞏI0,s will always appear in case of unbalanced ground faults. 
Dealing with erroneous ground fault detection due to unbal-
anced loads is discussed later in Subsection III.E. 


---

Page 6

---

1949-3053 (c) 2019 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TSG.2019.2945694, IEEE
Transactions on Smart Grid
 
5
An exception regarding the applicability of (2) might ap-
pear in case of isolated/compensated networks. However, in 
these networks, a very small earth current flows during SLG 
faults. In fact, the fault may self-extinguish, or the system may 
operate with the continuous earth current flowing, without 
disruption to consumers. Hence, protection means should not 
undesirably trip in this case anyway; instead, special methods 
should be used just for fault detection [35]. In case of isolat-
ed/compensated networks, the ground-fault protection element 
is not used at all. 2PHG faults can be dealt with by the 2PH-
fault protection element (seen as 2PH faults), described later. 
Assuming a full-cycle Discrete Fourier Transform (DFT) 
filter, reliable enough signals are obtained 1 cycle after the 
initiation. Hence, indicatively assuming a system frequency of 
50 Hz, the overall starting (response) time tS equals: 

1 cycle at 50 Hz
20 ms
S
D
t
t


                               (3) 
where tD is the time needed for the starting condition to be-
come valid, after fault inception. All the signals used in the 
algorithm-steps 2) and 3), described next, are those meas-
ured/calculated at t = tS. Note that once (2) becomes valid, bfi,j 
and bri,j are sent to block the forward operation of Rj,i and the 
reverse operation of the rest GRi-relays, respectively.  
 
2) Phase selection (PS) 
Next, the fault type/faulted phase is determined by examin-
ing the phase-angle relationship between the superimposed 
negative- (
2,s
I

) and positive-sequence (
1,s
I

) current phasors 
(hereafter referred to as I2,s vs. I1,s principle), as well as that 
between the negative- and zero-sequence (
0,s
I

) current phas-
ors (hereafter referred to as I2,s vs. I0,s principle). As these 
principles are based on the phase-angle difference between 
sequence-current phasors, they are independent of the exact 
position of each individual phasor (which varies depending on 
the fault/system conditions). The above principles have been 
used for many years in commercial relays and are considered 
reliable under various fault/system conditions [35], [36]. 
Table I shows the range of phase-angle difference φΙs,21 be-
tween 
2,s
I

 and 
1,s
I

, as well as that of phase-angle difference 
φΙs,20 between 
2,s
I

 and 
0,s
I

, each constituting a signature of a 
specific fault type [36], [37]. For security, both PS principles 
must agree on the fault-type for the latter to be specified. In 
that way, we also achieve fault-type distinction in I2,s vs. I0,s 
(e.g. 90o < φΙs,20 < 150o could mean either a-b-g or c-g fault). 
 
TABLE Ι 
SEQUENCE-CURRENT AND SEQUENCE-VOLTAGE PS PATTERNS 
Fault type 
I2,s vs. I1,s 
I2,s vs. I0,s 
V2 vs. V1 
V2 vs. V0 
φΙs,21 
φΙs,20 
φV,21 
φV,20 
a-b 
45o – 75o 
- 
180o – 300o 
- 
b-c 
165o – 195o 
- 
(-60o) – 60o 
- 
c-a 
(-75o) – (-45o) 
- 
60o – 180o 
- 
a-b-g 
45o – 75o 
90o – 150o 180o – 300o 
30o – 150o 
b-c-g 
165o – 195o 
(-30o) – 30o (-60o) – 60o (-90o) – 30o 
c-a-g 
(-75o) – (-45o) 210o – 270o 60o – 180o 
150o – 270o 
a-g 
(-15o) – 15o 
(-30o) – 30o 150o – 270o (-90o) – 30o 
b-g 
105o – 135o 
210o – 270o (-90o) – 30o 150o – 270o 
c-g 
225o – 255o 
90o – 150o 
30o – 150o 
30o – 150o 
Some commercial relays switch to sequence-voltage-based 
PS, if sequence-current-based PS fails [36]. In this work, if 
sequence-current-based PS fails, PS patterns [38] based on the 
actually measured sequence-voltage phasors are applied (see 
Fig. 2), which, in fact, are reliable (among others) in mi-
crogrids, even including photovoltaic (PV) units. Actually, the 
voltage-based PS is used as backup for the current-based PS. 
To this end, Table I also gives the range of phase-angle differ-
ence φV,21 between the negative- (
2
V

) and positive-sequence   
(
1V

) voltage phasors, as well as that of phase-angle difference 
φV,20 between the negative- and zero-sequence (
0
V

) voltage 
phasors, each indicating a specific fault type. Hereafter, these 
principles are referred to as V2 vs. V1 and V2 vs. V0, respective-
ly. Note that V2 vs. V0 is used against ground faults, whereas, 
V2 vs. V1 is used against 2PH faults (described later). To dis-
criminate between a SLG and a 2PHG fault when using V2 vs. 
V0 (e.g. 30o < φV,20 < 150o could mean either a-b-g or c-g 
fault), the voltage drop in each phase (ΔUa, ΔUb and ΔUc) is 
examined. For instance, in the above example, if both ΔUa > 
ΔUc and ΔUb > ΔUc hold, a-b-g fault is specified, whereas, c-g 
fault is determined if both ΔUc > ΔUa and ΔUc > ΔUb hold. 
The current-based PS is quite reliable when the short-
circuit current source includes not only inverter-interfaced DG 
units (IIDGs), but also the external grid and/or synchronous 
DG units. The current-based PS has been defined as primary, 
since the above is the most common case (especially in looped 
or meshed networks), while, this kind of PS has proved its 
efficacy over the years in the field; however, this is not bind-
ing. Since this PS is more probable to fail if IIDGs constitute 
the only short-circuit current source [37], [38] (e.g. in a fully 
IIDG-based islanded network), in this special case, the prima-
ry PS can switch to the voltage-based method (which is ex-
pected to perform well [38]). This task is very simple, and 
could by even performed by the relay vendor in advance, if the 
relay is meant for networks with the above peculiarity. 
 
3) Fault direction determination 
After a specific fault type is specified (indicated by a signal 
ft in Fig. 2), the fault direction is determined using a distance 
element. Although other types of directional elements (e.g. 
sequence-component-based) could be used for this purpose, a 
properly applied distance element can be a simple, setting-free 
and practical way to determine fault direction. After receiving 
signal ft, the distance element calculates the impedance angle 
θl corresponding to the fault loop l (out of six) involved in the 
fault (see basic-calculations block in Fig. 2). The impedance 
angle of a phase- (e.g. a-b) and a ground-fault loop (e.g. a-g) 
is, respectively, equal to: 
(
) (
)
(
)
,
,
,
0
0,
arg
  
arg
3
a b
a
b
a s
b s
a
g
a
a s
s
V
V
I
I
V
I
K
I
q
q
-
-
é
ù
=
-
-
ê
ú
ë
û
é
ù
é
ù
=
+
⋅
⋅
ê
ú
ê
ú
ë
û
ë
û








                 (4) 
where 
a
V

, 
b
V

, 
,
a s
I

, 
,
b s
I

, are the phase-a voltage, phase-b 
voltage, superimposed phase-a current and superimposed 
phase-b current phasors, respectively, measured by the relay, 


---

Page 7

---

1949-3053 (c) 2019 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TSG.2019.2945694, IEEE
Transactions on Smart Grid
 
6
and 
0
K

 is the zero-sequence compensation factor [35].  
Note that superimposed currents are used for θl calculation, 
to keep the latter uninfluenced by the pre-fault load. If the 
voltage of the faulted loop is not adequate (e.g. in case of 
close-in unbalanced faults), the voltage of the healthy phases 
is used [35]. Also note that setting 
0
K

 accurately, based on 
the impedance of the protected line, is important in multi-zone 
distance protection applications [39], where discrimination 
between distance zones must be ensured. However, since here 
the distance element is used for fault direction determination 
only (i.e. without applying distance zones), absolute 
0
K

 set-
ting accuracy is not required and a value based on the imped-
ance of a typical MV OH line [35] can be applied by default. 
In principle, the calculated faulted-loop impedance lies in 
the first quadrant of the complex impedance (R-X) plane dur-
ing a forward fault and in the third quadrant during a reverse 
fault [35]. However, intermediate infeeds and fault resistance 
can cause underreach or overreach of the distance element (see 
Fig. 3a). Since overreach can even lead to angle θl lying in the 
fourth/second quadrant [14], a forward fault is determined if 
o
o
90
90
l



                                 (5) 
whereas, a reverse fault is determined if 
o
o
90
270
l


                                (6) 
4) Trip decision 
If (5) holds (forward fault), a signal cf is generated (see Fig. 
2) to cancel signal bfi,j, blocking the forward operation of Rj,i. 
If the respective signal bfj,i from Rj,i is not active, Ri,j trips CBi,j. 
If (6) holds (reverse fault), a signal cr is generated (see Fig. 2) 
to cancel signal bri,j, blocking the reverse operation of the rest 
GRi-relays. If the blocking signals from the rest GRi-relays 
(shown as a single signal bri in Fig. 2) are not active, Ri,j sends 
a signal sg to the reverse-fault block (RFB) (see Fig. 2). RFB, 
described in detail later, discriminates between a reverse fault 
at bus Bi and a reverse fault in lateral Li, and, in the latter case, 
ensures coordination between GRi-relays and Pi.  
Since, after tS expires, any signal bfj,i (resp. signals bri), sent 
by Rj,i (resp. GRi-relays), must be cancelled by the transmitting 
relay(s) for a trip to be issued (resp. for a signal sg to be sent), 
the tripping time tTF of Ri,j during a forward fault in Li,j (resp. 
the time tSR to send sg during a reverse fault in Bi/Li) will be: 




,1
,2
,
max
, 
max
, 
, 
,....., 
TF
S
SO
SR
S
S
S
S NR
t
t
t
t
t
t
t
t


              (7) 
 
where tSO is the starting time of Rj,i and tS,1, tS,2,…., tS,NR are the 
starting times of the rest GRi-relays (NR in total). Note that, 
assuming a fast means, communication latency can be consid-
ered negligible (e.g. it equals 4.9 μs/km for fiber optic cable). 
B.  2PH-Fault Protection Element 
1) Starting 
Current unbalance (iu) is applied as starting criterion for 
the 2PH-fault protection element. The most accurate definition 
of iu is [40]: 
2
1
iu
I
I

                                     (8) 
      
 
Fig. 3.  (a) Applied distance element, (b) 51-element of RFB. 
 
where I1 and I2 is the magnitude of the actual positive- and 
negative-sequence current, respectively, measured by the re-
lay. iu has been chosen here for the starting criterion, as it 
characterizes 2PH faults and their unbalanced nature. Accord-
ing to [40], the greatest expected iu under normal load (non-
fault) conditions is 0.3. The latter value is adopted here as the 
default starting threshold (see Fig. 2), and can be considered 
robust under various conditions. Given that only a small arc 
resistance appears during 2PH faults in distribution systems, 
the above threshold is always expected to be exceeded during 
2PH faults, remaining secure under non-fault conditions. 
A signal p must be also active in order for the 2PH-fault 
protection element to start, which is generated as long as ade-
quate 3ꞏI0,s is absent (see Fig. 2). In this way, any overlaps 
between specifying 2PH and SLG faults are avoided, especial-
ly when applying V2 vs. V1 in the next step (also see Table I). 
The overall starting time is given by (3) in this case too, 
while, once iu exceeds 0.3 and p is active, bfi,j and bri,j are 
generated, similarly to the previous element (see Fig. 2). 
 
2) Phase selection (PS) 
For PS, I2,s vs. I1,s, as well as V2 vs. V1 (if I2,s vs. I1,s fails), 
described previously, are applied. 
The logic of fault direction determination and trip decision 
(steps 3) and 4), respectively) is similar to that of the previous 
element. Note that if a reverse fault is determined and any 
signals bri are not active, a signal sp1 is sent to RFB (Fig. 2). 
C.  3PH-Fault Protection Element 
1) Starting 
Given that a balanced fault occurs, the following condition 
must hold so as for the 3PH-fault protection element to start: 






,
,
,
5%
 AND 
5%
 AND 
5%
a s
n
b s
n
c s
n
I
I
I
I
I
I



    (9)            
where Ia,s, Ib,s and Ic,s is the magnitude of the superimposed  
phase-a, phase-b and phase-c current, respectively. The above 
starting criterion is chosen as it characterizes only 3PH faults 
(i.e. overlaps with other protection elements are avoided). The 
superimposed phase currents are examined to enhance sensi-
tivity, disengaging the overcurrent threshold from the pre-fault 
load. The default threshold 5%In is chosen, following the same 
philosophy as that explained for (2). Despite sensitization, 
protection security is ensured by the proposed protec-
tion/communication logic (see Section II). Undesired tripping 
due to a load change is also avoided, as explained later. 
The overall starting time is given by (3). Once (9) asserts, 
bfi,j and bri,j are generated, as in the previous elements (Fig. 2). 
 
2) Fault direction determination 
Since 3PH faults are balanced, PS is not applied. Instead, it 


---

Page 8

---

1949-3053 (c) 2019 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TSG.2019.2945694, IEEE
Transactions on Smart Grid
 
7
is directly checked whether all the angles θl of the six fault 
loops (θl,tot) satisfy (5) (forward fault) or (6) (reverse fault). 
Except for indicating fault direction, fulfilling one of these 
conditions, along with (9), could signify a 3PH fault. If, during 
close-in 3PH faults, fault-loops voltage is not adequate, the 
pre-fault (memorized) voltage is used [35] to calculate θl,tot. 
 
3) Trip decision 
The trip-decision logic is similar to that of the previous el-
ements. Note that if a reverse fault is determined and any sig-
nals bri are not active, a signal sp2 is sent to RFB (Fig. 2). 
Theoretically, the fulfillment of (9) and (5) or (6) (by θl,tot) 
could be also due to load rise. However, since load in a seg-
ment Li,j is unidirectional, a load rise will not be seen as a for-
ward 3PH fault by one of the two relays protecting Li,j. Hence, 
this relay will not cancel the bf-signal sent to its opponent re-
lay (which sees a 3PH fault), avoiding incorrect tripping. In 
contrast, a load rise could theoretically “mislead” GRi-relays 
into seeing a reverse 3PH fault. This is dealt with by RFB. 
Finally, in the three elements described above, cf/cr can be 
generated not only in the trip-decision step, but also if, in any 
step, it is realized that an actual fault has not occurred (Fig. 2). 
D.  Reverse-Fault Block (RFB) 
Once one of the three basic protection elements of a relay 
Ri,j specifies a reverse fault and generates an s-signal, the role 
of RFB (see Fig. 2) is to discriminate between a fault at bus Bi 
and a fault in lateral Li. In the former case, RFB trips instanta-
neously, whereas, in the latter case, it introduces a proper time 
delay to coordinate Ri,j with the lateral protection means Pi. 
Let us explain the basic logic used by RFB to ensure coor-
dination between Ri,j and Pi. In the first place, the magnitudes 
of the actual phase currents flowing through Pi (IPi,a, IPi,b, IPi,c) 
are continuously measured by Ri,j through a CT at Pi location. 
From these currents, the maximum current magnitude IPi,max is 
extracted (see basic-calculations block in Fig. 2). The latter is 
the current magnitude that would make Pi operate, in case of a 
fault in Li, and would determine its operating time, based on 
its time-overcurrent characteristic (TOCPi). To coordinate Ri,j 
with Pi, RFB applies an overcurrent (51) element, which maps 
IPi,max onto TOCPi, as shown in Fig. 3b. If Pi is a fuse (resp. an 
overcurrent relay), its known total-clearing (resp. tripping) 
characteristic is considered as TOCPi. The latter is uploaded to 
each GRi-relay and is the only information inserted by the us-
er. Note, however, that this is a simple and effortless task. 
Using this logic, RFB calculates the melting/tripping time of 
Pi (tPi), based on TOCPi and the measured current IPi,max. Then, 
it adds a default coordination time interval (CTI) to this melt-
ing/tripping time, to determine the required time delay of Ri,j, 
so that coordination with Pi is ensured (see Fig. 3b). Hence, no 
matter the fault/system conditions, RFB achieves coordination 
with Pi by adjusting the time delay of Ri,j, based on the varying 
measured IPi,max and the default TOCPi and CTI. 
The designed internal logic of RFB, concerning both its de-
layed operation for coordination purposes and its instantane-
ous operation in any other reverse-fault case, is shown in Fig. 
2 and is also described next. 
 
1) Delayed operation 
First of all, RFB realizes that a fault in Li has occurred 
when IPi,max starts intersecting TOCPi. This happens when:  
,max
,
Pi
Pi MI
I
I

                                   (10) 
IPi,MI is the minimum intersecting current of TOCPi (Fig. 3b). 
To ensure that a reverse fault has indeed occurred, sg, sp1, 
or sp2 must also be sent (at t = tSR) to initiate the timer of 51-
element. This timer expires after tPi, which is calculated as 
described previously. Considering the CTI added for coordina-
tion, Ri,j will be ultimately ready to trip at: 
TR
SR
Pi
t
t
t
CTI



                           (11) 
In this work, a default CTI of 0.3 s is considered, which is the 
most frequent CTI value used by protection engineers [1]. 
If, after tTR expires, (10) still holds, it means that Pi failed to 
blow/trip, so Ri,j trips CBi,j, acting as backup protection for 
lateral Li. Of course, the rest GRi-relays operate similarly. 
 
2) Instantaneous operation 
If IPi,max < IPi,MI holds, this could mean either that:  
i) 
A fault has not occurred at Bi or Li. 
ii) A fault has occurred at Bi. 
iii) A (ground) fault with considerable resistance, not detect-
able by Pi, has occurred in Li. 
iv) A remote fault, not detectable by Pi, has occurred at the 
secondary side of a distribution transformer of Li.  
Case-i is excluded if a signal sg, sp1, or sp2 is sent. It is also 
desirable that GRi-relays not trip in case-iv (addressed later). 
To recognize case-ii and case-iii faults in a simple way, an 
undervoltage (27) element is examined only if IPi,max < IPi,MI 
(see Fig. 2), and is set by default to assert if: 






 0.9 p.u.
 0.9 p
OR
.u.
 0.9 p.
 
.
OR 
u
 
 
a
b
c
V
V
V



 (12)          
where Va, Vb, Vc are the magnitudes of the Bi phase voltages 
and 0.9 per unit (p.u.) is the voltage limit indicating an un-
dervoltage disturbance [40]. Two cases are examined: 
 
If 27-element asserts and sg, sp1, or sp2 is generated as 
well, then (since it is known that IPi,max < IPi,MI), a Bi-fault 
is recognized (case-ii) and the relay trips instantaneously.  
 
If IPi,max < IPi,MI holds, 27-element does not assert, but a 
signal sg is generated, then, a (ground) fault with consid-
erable resistance has expectedly occurred at Bi (case-ii) or 
Li (case-iii), so the relay trips again instantaneously.  
E.  Protection Reliability Aspects 
In the special case where sp2 is due to a load rise, neither 
(10) nor (12) should hold, so RFB will not trip undesirably. 
Assuming distribution transformers which are not double-
side grounded (as it is usually the case in many countries), a 
ground fault in the low-voltage (LV) network (previous case-
iv) will not be detected by the ground-fault protection element, 
due to zero-sequence current absence; hence, undesired RFB 
trip is avoided. The same also holds in case of load unbalanc-
es, given the negligible capacitance of OH distribution lines.  
However, even if double-side-grounded distribution trans-
formers are connected to Li, this can be addressed by the ven-
dor/user of the PnP relay, by disabling the part of RFB shown 
in Fig. 2 into the dashed frame. Hence, the generation of a sg-
signal alone is no longer enough for a trip to be issued (since 
now it could theoretically be due to a change in an unbalanced 
load or a LV ground fault), but either (10) or (12) must also 
hold. To detect bus faults with high resistance in that case, sg-
generation in combination with the non-detection of a forward 
ground fault at Pi location could be used as a signature. Also, 


---

Page 9

---

1949-3053 (c) 2019 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TSG.2019.2945694, IEEE
Transactions on Smart Grid
 
8
only in that case, faults with high resistance in Li are recog-
nized by RFB as long as (10) holds. Note, however, that a 
lateral protection means can sense faults with a considerable 
resistance (as shown later in Section IV), while, it must be 
borne in mind that GRi-relays only secondarily protect Li, 
meaning that their actual purpose is to just recognize all the 
faults that Pi is designed to protect against. 
If GRi-relays see a 2PH/3PH fault due to a LV-fault, RFB 
will not trip, unless (10) holds. Also note that if a LV-fault 
results in IPi,max < IPi,MI, 27-element is not expected to assert. 
In the case where one or more DG units are connected to Li, 
downstream to Pi, and the fault current injected by them is 
strong, (10) could also hold for a Bi-fault, “misleading” RFB 
into applying a time delay, instead of instantaneously tripping. 
For that reason, RFB is supplemented with the dotted part of 
Fig. 2, which checks the direction of the fault current flowing 
through Pi. Specifically, based on Bi phase voltages and the 
superimposed phase currents at Pi (
, ,
Pi a s
I

, 
, ,
Pi b s
I

, 
, ,
Pi c s
I

), the 
impedance angle(s) θl,Pi (θl,tot,Pi) of the fault loop(s) indicated 
by signal ft is (are) calculated by a distance element. Fault 
direction is specified based on (5) or (6). If a reverse fault (i.e. 
leading to fault current flowing towards Bi) is determined, (10) 
holds (indicated by a signal s) and sg, sp1, or sp2 is sent, the 
above case is recognized, so, instantaneous trip is issued. 
It should be also mentioned that the proposed scheme can 
detect ground faults with a considerable resistance, greater 
than the resistance dealt with by conventional distribution sys-
tem protection schemes. This is because, the respective start-
ing function is sensitized as much as possible, by examining 
the superimposed residual current and considering a typical 
maximum current sensitivity of commercial relays as the de-
fault overcurrent starting threshold. However, there might be 
cases where high-resistance faults lead to short-circuit currents 
even lower than the inherent maximum current sensitivity of 
the relay. In such cases, special methods are required for fault 
detection, which is an issue requiring dedicated study [41].  
Finally, although out of scope, communication operability 
can be ensured through signal-exchange check or redundancy. 
F.  Backup Protection of Main Line Segments and Buses 
For backup protection of main line segments and buses (a 
lateral Li is secondarily protected by GRi-relays), a breaker-
failure (BF) protection element is designed (see Fig. 2). The 
BF element ensures that if a CB fails to open, its adjacent CBs 
will be tripped instead. Specifically, once a relay Ri,j issues a 
trip order, either for main line protection (forward faults), or 
bus protection (reverse faults), a breaker-failure initiation 
(BFI) signal is simultaneously generated (BFIfi,j and BFIri,j, 
respectively), as shown in Fig. 2. Then, the state of CBi,j is 
checked for a time period tBF, compensating for the CBi,j inter-
rupting time. A tBF of 0.24 s is adopted here by default; this 
corresponds to the maximum typical BF-timer setting accord-
ing to [42], indicatively considering a system frequency of 50 
Hz. If CBi,j remains closed after tBF expires, a trip order is sent 
to its adjacent CBs. Note that the designed BF element dis-
criminates between a BFI signal generated due to a forward or 
a reverse fault, so as to trip the proper adjacent CBs (CBfi,j and 
CBri,j, respectively, in Fig. 2). Once a BFI signal is sent, an 
instantaneous redundant trip (re-trip) signal is also sent to 
CBi,j, as an attempt to avoid tripping the adjacent CBs. 
G.   Economic Evaluation 
It is a fact that the use of communication means as part of 
the proposed protection scheme requires an investment that is 
not negligible. However, one should bear in mind that the op-
eration of distribution networks in a looped or meshed config-
uration is envisioned as a solution to maximize the reliability 
of future distribution networks, especially in light of increas-
ing DG penetration [9]. For this purpose, the reliability and the 
efficacy of protection schemes must be, in turn, enhanced. To 
design advanced protection schemes which satisfy these relia-
bility/efficacy requirements, the use of communication means 
might be needed. The required investment should be evaluat-
ed, taking into account the operational and maintenance bene-
fits gained by the Distribution System Operators (DSOs) and 
DG producers, due to the efficacy of the protection scheme 
[43]. For example, the cost of electricity supply interruptions 
and the outage cost of DG units are critical measures that 
should be considered in the economic evaluation of the protec-
tion scheme [44], [45]. The trend towards using communica-
tion means for protecting distribution systems is also reflected 
on the numerous research papers adopting this philosophy [3]-
[11], [13]-[25], [27], [28], [31], [32]. In fact, in [7], [8], com-
munication-based protection schemes are considered for real 
looped distribution networks. Based on the above, proper mo-
tives are expected to arise in the future for DSOs and DG pro-
ducers, towards the investment in communication-assisted 
protection schemes. The investment could be possibly shared 
between DSOs and DG producers, in return for the increased 
reliability of the distribution system and the avoidance of un-
necessary DG disconnection, respectively. 
IV.  PERFORMANCE EVALUATION 
The PnP scheme is mainly tested on the 20 kV, 50 Hz, OH 
meshed distribution system of Fig. 4, which is designed using 
realistic data received by the Hellenic Electricity Distribution 
Network Operator S.A. (HEDNO S.A.), and includes both 
PVs and synchronous generators (SGs). The system’s basic 
data are shown in Fig. 4, while, a detailed description is in-
cluded in [14]. Note that the total load of each lateral is shown 
as a single load, fed by a single distribution transformer, for 
illustration simplicity. PnP relays are installed at main line 
segments according to Section II, operating as described pre-
viously. Each relay Ri,j is accompanied by a circuit breaker 
CBi,j, installed at the same location, while, in this study, it is 
assumed receiving current and voltage measurements from a 
local current and voltage transformer with a ratio of 200:5 and 
20000:100, respectively. Laterals (Li) are primarily protected 
by 30-T fuses (Pi), commonly applied in Greece, which are 
assumed existing in the system.  
The system of Fig. 4 is modeled with PowerFactory 2018, 
used for dynamically simulating faults and extracting the volt-
age/current signals measured at the relays’ locations. Then, 
these signals are processed with MATLAB, where the rest 
relay elements and functions are modeled and evaluated. 
A.  Main Simulation Results  
The relay R2,3, protecting L2,3 (along with R3,2) and B2/L2 
(along with R2,1, R2,10), is arbitrarily chosen to demonstrate the 
scheme’s performance against a-b-c, a-b, b-c-g and a-g faults 
at different locations, in GC/ISL system mode. An arc re-


---

Page 10

---

1949-3053 (c) 2019 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TSG.2019.2945694, IEEE
Transactions on Smart Grid
 
9
sistance (Rarc) of 2.5 Ω is considered for 3PH/2PH faults, 
which is a typical maximum Rarc in OH MV networks [35]. 
This is also considered as the minimum fault resistance (Rf,min) 
for 2PHG faults. A maximum fault resistance (Rf,max) of 100 Ω 
is considered for SLG/2PHG faults. Tables II-V present the 
critical measurements/calculations of R2,3, referring to each 
algorithm-step, during the above faults at the midpoint of L2,3 
(forward faults), as well as at buses B2 (reverse bus-faults) and 
B2.R (reverse lateral-faults). Fault positions are shown in Fig. 4.  
The results of Tables II-IV reflect the performance of R2,3 
until the latter trips (in case of a forward fault) or sends an s-
signal to RFB (in case of a reverse bus/lateral fault). First of 
all, based on the tS values shown (refer to (3)), the starting 
functions of R2,3 always quickly detect the faults and assert.  
Then, the fault type (regarding only 2PH/2PHG/SLG 
faults) is always correctly specified by both the corresponding 
primary and backup phase selector, as can be realized by the φ 
values of Tables II and III (compare these values to the respec-
tive angle ranges of Τable I for each fault type), as well as the 
ΔU values used to assist fault-type distinction in V2 vs. V0 PS 
(see Subsection III.A.2). Only in one case in Table II (bolded), 
the I2,s vs. I1,s PS fails to specify the fault type, which is, how-
ever, then correctly specified by the backup V2 vs. V0 PS. Note 
that the results for the backup PS are shown even in the rest 
fault cases, just to show its effectiveness. 
Fault direction is correctly determined in all the examined 
fault cases, as the calculated impedance angle(s) (θl in Tables 
II, III and θl,tot in Table IV) corresponding to each fault type 
examined (see the basic-calculations block of Fig. 2), lie(s) 
within (-90o, 90o) during forward (main line) faults and     
(90o, 270o) during reverse (bus/lateral) faults (refer to (5), (6)). 
Based on the tTF and tSR values of Tables II-IV, it appears 
that the relay trips (in case of forward main line faults in Ta-
bles II, IV) or sends an s-signal to RFB (in case of reverse 
bus/lateral faults in Tables III, IV) quickly after fault incep-
tion. tTF and tSR either coincide with the respective tS values or 
they are slightly higher, depending on the time needed for the 
opponent/adjacent relay/s to process their input signals and 
cancel the blocking signal initially sent to R2,3 (refer to (7)). 
Table V shows the critical measurements/calculations of 
RFB of R2,3, during reverse main line bus (bus B2) and lateral 
(bus B2.R) faults. During faults at B2, R2,3 measures a current 
IP2,max flowing through fuse P2, which does not intersect its 
time-overcurrent characteristic (TOCP2), as it is lower than its 
minimum intersecting current IP2,MI (which equals 74 A, as 
shown in Fig. 4). Hence, according to Fig. 2, RFB recognizes 
a non-lateral fault and checks its undervoltage element. As 
shown in Table V, in case of low-resistance or solid faults at 
B2, at least one of the three phase voltages drops below 0.9 
p.u. (refer to (12)), so, RFB trips instantaneously (as tTR equals 
the respective tSR of Table III, i.e. the time instant when a s-
signal is sent to RFB). In case of 100-Ω ground faults at B2, 
the undervoltage element does not assert; however, as a sg-
signal has been sent to RFB from the ground-fault protection 
element, the former recognizes a high-resistance fault and trips 
instantaneously (as tTR = tSR). As for reverse faults at B2.R, R2,3 
always measures a current IP2,max which intersects TOCP2 (see 
Table V). Hence, RFB recognizes a lateral fault and calculates 
the tripping time tTR, so as to ensure coordination with P2. The 
tTR values of Table V, in case of B2.R-faults, are calculated 
based on the melting time tP2 of P2 for the respective measured 
IP2,max (see tP2 values in Table V) and the CTI added for coor-
dination (refer to Fig. 2 and (11)). Note that, in case of B2.R-
faults, we always assume that P2 fails to blow. Just to mention, 
the high tTR in some cases is due to the high tP2. 
 
 
 
Fig. 4.  Test distribution system. 


---

Page 11

---

1949-3053 (c) 2019 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TSG.2019.2945694, IEEE
Transactions on Smart Grid
 
10 
TABLE ΙI 
CRITICAL CALCULATIONS OF RELAY R2,3 DURING UNBALANCED FAULTS AT ΤHE MIDPOINT OF L2,3 
Fault 
type 
Rf,min/ 
Rf,max 
(Ω) 
Grid-connected mode 
Islanded mode 
tS 
(ms) 
φΙs,21 
(o) 
φΙs,20 
(o) 
φV,21 
(o) 
φV,20 
(o) 
ΔUa 
(%) 
ΔUb 
(%) 
ΔUc 
(%) 
θl 
(o) 
tTF 
(ms) 
tS 
 (ms) 
φΙs,21 
(o) 
φΙs,20 
(o) 
φV,21 
(o) 
φV,20 
(o) 
ΔUa 
(%) 
ΔUb 
(%) 
ΔUc 
(%) 
θl 
(o) 
tTF 
(ms) 
a-b 
2.5 
20.5 
60.9 
- 
269.8 
- 
- 
- 
- 
20.0 20.5 22.6 
61.7 
- 
252.8 
- 
- 
- 
- 
8.2 
22.6 
b-c-g 
2.5/ 
100 
20.3/ 
22.2 
186.5/ 
180.2 
15.0/ 
3.1 
-/ 
- 
5.3/ 
-6.6 
1.2/ 
1.2 
43.4/ 
2.0 
40.9/ 
1.9 
9.5/ 
-1.5 
20.3/ 
22.2 
20.4/ 
22.4 
178.9/ 
189.0 
-0.1/ 
5.8 
-/ 
- 
-15.3/ 
-9.4 
31.1/ 
2.4 
69.8/ 
2.7 
74.2/ 
5.5 
4.9/ 
0.9 
20.4/ 
22.4 
a-g 
0/ 
100 
20.2/ 
22.2 
1.9/ 
-0.6 
2.2/ 
2.2 
-/ 
- 
-7.5/ 
-7.5 
72.0/ 
2.0 
-3.3a/ 
1.1 
4.8/ 
1.2 
56.7/ 
-12.5 
20.2/ 
22.2 
21.2/ 
22.5 
-0.2/ 
20.6 
8.6/ 
8.6 
-/ 
- 
-6.5/ 
-6.5 
90.5/ 
4.4 
7.7/ 
3.2 
15.0/ 
0.3 
57.1/ 
-14.0 
21.2/ 
22.5 
aNegative voltage drop signifies voltage rise. 
 
TABLE ΙΙI 
CRITICAL CALCULATIONS OF RELAY R2,3 DURING UNBALANCED FAULTS AT BUSES B2 AND B2.R 
Fault 
type 
Faulted 
bus 
Rf,min/ 
Rf,max 
(Ω) 
Grid-connected mode 
Islanded mode 
tS 
(ms) 
φΙs,21 
(o) 
φΙs,20 
(o) 
φV,21 
(o) 
φV,20 
(o) 
ΔUa 
(%) 
ΔUb 
(%) 
ΔUc 
(%) 
θl 
(o) 
tSR 
(ms) 
tS 
(ms) 
φΙs,21 
(o) 
φΙs,20 
(o) 
φV,21 
(o) 
φV,20 
(o) 
ΔUa 
(%) 
ΔUb 
(%) 
ΔUc 
(%) 
θl 
(o) 
tSR 
(ms) 
a-b 
B2 
2.5 
21.2 58.1 
- 
272.2 
- 
- 
- 
- 
187.3 21.2 21.3 59.4 
- 
252.3 
- 
- 
- 
- 
187.8 21.4 
B2.R 
2.5 
21.8 59.1 
- 
287.4 
- 
- 
- 
- 
199.3 21.8 21.6 58.7 
- 
216.6 
- 
- 
- 
- 
202.5 21.6 
b-c-g 
B2 
2.5/ 
100 
20.4/ 
23.6 
184.0/ 
178.5 
7.3/ 
-4.0 
-/ 
- 
3.44/ 
-7.9 
-4.6a/ 
1.2 
56.6/ 
2.5 
41.6/ 
1.8 
181.0/ 
181.0 
21.2/ 
30.7 
21.2/ 
23.6 
171.9/ 
172.7 
-16.9/ 
-10.6 
-/ 
- 
-16.9/ 
-10.6 
28.7/ 
2.2 
76.9/ 
3.2 
72.7/ 
5.6 
183.7/ 
179.5 
21.6/ 
31.7 
B2.R 
2.5/ 
100 
21.7/ 
24.2 
188.0/ 
180.6 
18.6/ 
-0.8 
-/ 
- 
14.7/ 
-4.6 
-0.7a/ 
1.1 
17.8/ 
2.4 
19.1/ 
1.8 
195.2/ 
182.2 
22.1/ 
31.5 
21.7/ 
24.2 
180.0/ 
174.5 
-3.1/ 
-6.9 
-/ 
- 
-3.1/ 
-6.9 
18.7/ 
2.2 
39.0/ 
3.1 
46.0/ 
5.6 
196.7/ 
180.5 
22.6/ 
32.4 
a-g 
B2 
0/ 
100 
20.3/ 
23.6 
-4.0/ 
0.3 
-4.7/ 
-4.7 
-/ 
- 
-8.5/ 
-8.5 
99.9/ 
2.1 
-10.8a/ 
0.8 
0.8/ 
1.5 
238.5b/ 
164.4 
20.4/ 
30.7 
21.4/ 
23.7 
0.0/ 
-4.3 
-7.3/ 
-7.3 
-/ 
- 
-7.3/ 
-7.3 
100.0/ 
4.6 
5.6/ 
2.9 
15.1/ 
2.7 
245.3b/ 
168.8 
22.0/ 
31.8 
B2.R 
0/ 
100 
21.4/ 
24.1 
-1.3/ 
0.9 
-4.6/ 
-4.6 
-/ 
- 
-8.4/ 
-8.4 
26.9/ 
2.1 
-3.1a/ 
0.8 
2.8/ 
1.5 
204.8/ 
166.4 
21.8/ 
31.4 
21.7/ 
24.2 
-0.6/ 
-8.3 
-7.2/ 
-7.2 
-/ 
- 
-7.2/ 
-7.2 
47.2/ 
4.0 
8.6/ 
2.6 
7.7/ 
2.5 
201.6/ 
169.6 
22.6/ 
32.5 
aNegative voltage drop signifies voltage rise. 
bThe voltage of the healthy phases (cross-polarization) has been used to calculate θa-g, due to inadequate voltage magnitude in the faulted phase. 
 
TABLE ΙV 
CRITICAL CALCULATIONS OF RELAY R2,3 DURING 2.5-Ω 3PH FAULTS AT THE MIDPOINT OF L2,3 AND BUSES B2 AND B2.R 
Fault 
position 
Grid-connected mode 
Islanded mode 
tS 
 (ms) 
θa-b 
(ο) 
θb-c 
(ο) 
θc-a 
(ο) 
θa-g 
(ο) 
θb-g 
(ο) 
θc-g 
(ο) 
tTF 
(ms) 
tSR 
(ms) 
tS 
 (ms) 
θa-b 
(ο) 
θb-c 
(ο) 
θc-a 
(ο) 
θa-g 
(ο) 
θb-g 
(ο) 
θc-g 
(ο) 
tTF 
(ms) 
tSR 
(ms) 
L2,3 midpoint 
20.3 
10.2 
8.6 
9.6 
9.5 
9.4 
9.5 
20.3 
- 
20.1 
6.9 
4.4 
5.1 
5.1 
6.6 
5.0 
20.2 
- 
B2 
20.1 182.4 181.6 181.8 181.9 182.1 181.8 
- 
20.2 20.2 180.3 179.7 180.4 180.3 179.8 180.3 
- 
20.2 
B2.R 
20.1 196.8 194.3 196.2 195.8 196.2 195.3 
- 
20.2 20.2 193.6 193.2 192.6 193.3 192.6 193.4 
- 
20.2 
 
TABLE V 
CRITICAL MEASUREMENTS/CALCULATIONS OF RFB OF RELAY R2,3 DURING FAULTS AT BUSES B2 AND B2.R 
Fault 
type 
Faulted 
bus 
Rf,min/ 
Rf,max 
(Ω) 
Grid-connected mode 
Islanded mode 
IP2,max 
(pri. A) 
Va 
(% p.u.) 
Vb 
(% p.u.) 
Vc 
(% p.u.) 
tP2 
(ms) 
tTR 
(ms) 
IP2,max 
(pri. A) 
Va 
(% p.u.) 
Vb 
(% p.u.) 
Vc 
(% p.u.) 
tP2 
(ms) 
tTR 
(ms) 
a-b-c 
B2 
2.5 
14.8 
53.4 
47.8 
57.8 
- 
20.2 
8.4 
23.1 
18.7 
23.0 
- 
20.2 
B2.R 
2.5 
1069.2 
- 
- 
- 
107.2 
427.4 
701.6 
- 
- 
- 
220.6 
540.8 
a-b 
B2 
2.5 
26.0 
72.5 
35.8 
100.6 
- 
21.2 
26.8 
58.0 
42.8 
100.3 
- 
21.4 
B2.R 
2.5 
968.7 
- 
- 
- 
127.0 
448.8 
562.2 
- 
- 
- 
334.0 
655.6 
b-c-g 
B2 
2.5/ 
100 
21.5/ 
25.9 
106.2/ 
100.6 
47.5/ 
99.3 
60.6/ 
100.0 
-/ 
- 
21.2/ 
30.7 
15.1/ 
26.3 
66.9/ 
97.2 
23.4/ 
96.1 
27.3/ 
94.0 
-/ 
- 
21.6/ 
31.7 
B2.R 
2.5/ 
100 
1124.3/ 
131.0 
-/ 
- 
-/ 
- 
-/ 
- 
98.3/ 
10180.0 
420.4/ 
10511.5 
754.0/ 
124.6 
-/ 
- 
-/ 
- 
-/ 
- 
193.5/ 
12341.0 
516.1/ 
12673.4 
a-g 
B2 
0/ 
100 
24.0/ 
26.1 
0.1/ 
99.7 
112.7/ 
101.0 
101.0/ 
100.3 
-/ 
- 
20.4/ 
30.7 
23.6/ 
26.6 
0.0/ 
94.2 
93.1/ 
95.0 
84.8/ 
98.2 
-/ 
- 
22.0/ 
31.8 
B2.R 
0/ 
100 
1075.5/ 
129.3 
-/ 
- 
-/ 
- 
-/ 
- 
105.9/ 
10614.0 
427.7/ 
10945.4 
765.7/ 
123.6 
-/ 
- 
-/ 
- 
-/ 
- 
188.2/ 
12840.0 
510.8/ 
13172.5 
 
  
               
                        
 
Fig. 5.  R2,3 calculations during a-b fault at B2.R (GC mode). (a) iu (starting), (b) 
1,s
I

, 
2,s
I

 (PS) and 
a b
Z 

 (loop a-b impedance) at t = tS, (c) Coordination with P2. 


---

Page 12

---

1949-3053 (c) 2019 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TSG.2019.2945694, IEEE
Transactions on Smart Grid
 
11 
It is worth noting that the maximum fault resistance sensed 
by the ground-fault starting function of a PnP relay can be 
even greater than the 100-Ω value considered in this study, 
depending on the fault/system conditions. To provide an ex-
ample, SLG faults have been simulated at the midpoint of L2,3, 
in order to calculate the maximum fault resistance sensed by 
R2,3 for this specific fault type and fault position. This maxi-
mum fault resistance has been found equal to 545 Ω for the 
GC mode and 529 Ω for the ISL mode of system operation. 
Note that 3PH-ground faults would be dealt with similarly 
to 3PH faults. It is worth mentioning that high-resistance 3PH-
ground faults are highly unlikely [16]. 
In Fig. 5a - Fig. 5c, the representative case of a-b fault at 
B2.R (GC mode) is chosen, to illustrate the critical operations 
of R2,3. Fault inception is assumed at t = 0.01 s. Note that only 
the primary phase selector is illustrated as part of Fig. 5b. 
B.  Additional Simulation Results  
To further demonstrate the efficacy of the proposed protec-
tion scheme and its independence from specific fault/system 
conditions, a number of additional simulation scenarios is con-
sidered. Note that the default settings of the PnP relays have 
remained unchanged. In the tables of this subsection, the re-
sults regarding only the primary phase selector are given in 
each case. Moreover, wherever θl,tot or θl,tot,Pi is given (3PH 
faults), the impedance angle corresponding to fault loop a-g is 
shown as a representative value, given that there might by 
slight divergences between the values of the six fault loops. 
 
1) Scenario 1: Sudden load change 
In the following, a simulation-based example is given to 
demonstrate the immunity of the relays protecting a bus/lateral 
(based on their reverse operation) to a sudden load change. 
To simulate a severe load change, we assume that (consid-
ering the GC mode of the system) the whole load of lateral L2 
is initially disconnected, and is re-connected at t = 0.01 s. Fig. 
6a and Fig. 6b show the measured phase currents flowing 
through fuse P2 and the phase voltages measured at bus B2, 
respectively. As it is apparent in Fig. 6a, all the phase currents 
are safely below IP2,MI, so, (10) does not hold. Hence, a reverse 
3PH lateral fault is not mistakenly specified by the relays con-
stituting GR2 (i.e. R2,3, R2,1 and R2,10). Based on the RFB logic 
described in Subsection III.D, the phase voltages at bus B2 are 
checked then. As shown in Fig. 6b, these voltages are far from 
dropping below the default threshold of (12). Therefore, the 
simulated load change is not mistakenly seen as a reverse 3PH 
bus fault by the GR2-relays. Obviously, a sg-signal is not gen-
erated during the load change, so, a ground fault with high 
resistance is not mistakenly specified either. Moreover, as 
explained in Subsection III.C.3, a load change would not be of 
concern as regards the forward operation of the opponent re-
lays protecting a main line segment. To provide an example, 
during the simulated load change, the opponent relays R2,3 and 
R3,2 protecting L2,3 (based on their forward operation), calcu-
late an impedance angle (θl,tot) of approximately 180.4o and 
0.8o, respectively; hence, they see this load change in opposite 
directions, which means that they cannot undesirably trip. 
 
 
 
Fig. 6.  Scenario 1. (a) Current flowing through P2, (b) Voltage at bus B2. 
 
2) Scenario 2: Connection of DG to a lateral 
In this scenario, we assume that SG1 is disconnected from 
main line bus B4 and is connected to the endpoint of lateral L2 
(bus B2.R). This scenario intends not only to demonstrate the 
independence of the proposed protection scheme from discon-
necting/connecting DG units from/to any network bus, but 
also to show the ability of a PnP relay to recognize a main line 
bus fault and trip instantaneously, even if the short-circuit cur-
rent coming from a DG unit connected to the respective lateral 
(departing from this bus) intersects the TOCPi of the lateral 
protection means (refer to Subsection III.E). 
Table VI shows the critical calculations of relay R2,3 during 
faults at bus B2, assuming all the fault-type, fault-resistance 
and operation mode (O/M) cases considered in the previous 
subsection. According to the results, the three basic protection 
elements of the relay always quickly detect the fault, correctly 
specify the fault type and the fault direction (reverse) and send 
an s-signal to the RFB of the relay, after t = tSR (i.e. after all 
the relays of GR2 cancel their blocking signals).  
Table VII shows the critical measurements/calculations of 
RFB. In the vast majority of the simulated cases, the measured 
IP2,max intersects TOCP2 (as IP2,max > 74 A), due to the short-
circuit current contribution of SG1, connected to B2.R. This fact 
“misleads” RFB into specifying a lateral fault instead of a 
main line bus fault (note that the undervoltage element is ig-
nored in these cases). However, this issue is addressed as ex-
plained in Subsection III.E (i.e. through the dotted part of Fig. 
2). In particular, the direction of IP2,max is specified as reverse 
in all cases (as it is derived from the θl,P2/θl,tot,P2 values of Ta-
ble VII), which indicates a fault at B2. Subsequently, a trip 
order with no intentional time delay is issued (see the tTR val-
ues of Table VII), instead of mistakenly tripping after the re-
spective tP2 (also shown in Table VII) and CTI elapses. 
 
 


---

Page 13

---

1949-3053 (c) 2019 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TSG.2019.2945694, IEEE
Transactions on Smart Grid
 
12 
TABLE VI 
CRITICAL CALCULATIONS OF RELAY R2,3 DURING FAULTS AT BUS B2 
(SCENARIO 2) 
O/M Fault 
type 
Rf,min/ 
Rf,max 
(Ω) 
tS 
(ms) 
φΙs,21 
(o) 
φΙs,20 
(o) 
θl/θl,tot 
(o) 
tSR 
(ms) 
GC 
a-b-c 
2.5 
22.2 
- 
- 
181.6 22.2 
a-b 
2.5 
21.6 
57.0 
- 
183.1 21.6 
b-c-g 
2.5/ 
100 
20.5/ 
29.0 
178.6/ 
177.1 
4.2/ 
1.4 
182.6/ 
182.6 
21.5/ 
32.6 
a-g 
0/ 
100 
20.4/ 
29.0 
-3.0/ 
-3.0 
1.3/ 
1.3 
241.6/ 
170.4 
21.1/ 
32.6 
ISL 
a-b-c 
2.5 
22.7 
- 
- 
184.5 23.6 
a-b 
2.5 
21.6 
58.2 
- 
185.4 22.5 
b-c-g 
2.5/ 
100 
22.1/ 
29.4 
167.1/ 
176.2 
27.4/ 
-6.8 
185.0/ 
185.3 
22.3/ 
34.1 
a-g 
0/ 
100 
21.8/ 
29.7 
-1.8/ 
-1.3 
-2.4/ 
-2.4 
248.1/ 
173.3 
22.3/ 
34.4 
  
TABLE VII 
CRITICAL MEASUREMENTS/CALCULATIONS OF RFB OF RELAY R2,3 DURING 
FAULTS AT BUS B2 (SCENARIO 2) 
O/M Fault 
type 
Rf,min/ 
Rf,max 
(Ω) 
IP2,max 
(pri. A) 
Va 
(% p.u.)
Vb 
(% p.u.)
Vc 
(% p.u.)
tP2 
(ms) 
θl,P2/ 
θl,tot,P2 
(o) 
tTR 
(ms) 
GC 
a-b-c 
2.5 
335.2 
- 
- 
- 
917.8 
171.1 
22.2 
a-b 
2.5 
339.5 
- 
- 
- 
893.8 
176.5 
21.6 
b-c-g 2.5/ 
100 
394.7/ 
49.9 
-/ 
100.7 
-/ 
99.5 
-/ 
99.8 
658.0/ 
- 
174.8/ 
174.7 
21.5/ 
32.6 
a-g 
0/ 
100 
666.6/ 
52.6 
-/ 
99.7 
-/ 
100.9 
-/ 
100.6 
242.6/ 
- 
218.0/ 
146.9 
21.1/ 
32.6 
ISL 
a-b-c 
2.5 
530.8 
- 
- 
- 
371.2 
171.3 
23.6 
a-b 
2.5 
428.7 
- 
- 
- 
555.9 
172.4 
22.5 
b-c-g 2.5/ 
100 
553.9/ 
95.3 
-/ 
- 
-/ 
- 
-/ 
- 
343.0/ 
49552.2 
172.3/ 
171.2 
22.3/ 
34.1 
a-g 
0/ 
100 
614.9/ 
90.0 
-/ 
- 
-/ 
- 
-/ 
- 
282.0/ 
69771.3 
229.3/ 
153.6 
22.3/ 
34.4 
 
3) Scenario 3: Loss of network-part and looped configuration 
As part of this scenario, we suppose that R3,2, R3,7 and R3,4 
have tripped (e.g. after a fault at B3/L3) and the respective CBs 
are open. This fact leads to a loss of short-circuit contribution 
through both line segments L3,4 and L3,7, in case of a fault at 
L2,3. Actually, in this case, the relay R2,3 protects a radial main 
line segment, as a fault in L2,3 is fed from only one direction. 
To show the immunity of a PnP relay (e.g. R2,3) to the loss 
of a network-part, even if the latter leads to loss of the looped 
configuration, all the fault cases of the previous subsection are 
simulated at the midpoint of L2,3, assuming the above scenario. 
The simulation results are shown in Table VIII. As it is appar-
ent, R2,3 operates quickly and correctly in all the simulated 
fault cases, sending an immediate trip order to CB2,3, so as to 
isolate L2,3. Note that, since the opponent relay R3,2 does not 
initiate its operation for any of the simulated faults (as it does 
not see any current), it never sends a blocking signal to R2,3. 
 
4) Scenario 4: Loss of DG 
In order to show the independence of the PnP protection 
scheme from any DG loss, we assume a marginal (worst-case) 
scenario, where all the DG units of the test distribution system 
are disconnected. Since no DG is present, only the GC mode 
of the system is examined. Table IX shows the critical calcula-
tions of relay R2,3, during faults at the midpoint of L2,3, consid-
ering the above system case. It appears that the relay always 
operates quickly and correctly, despite the mass DG loss, fur-
ther proving the scheme’s immunity to DG intermittence. 
 
TABLE VIII 
CRITICAL CALCULATIONS OF RELAY R2,3 DURING FAULTS AT ΤHE MIDPOINT 
OF L2,3 (SCENARIO 3) 
O/M Fault 
type 
Rf,min/ 
Rf,max 
(Ω) 
tS 
(ms) 
φΙs,21 
(o) 
φΙs,20 
(o) 
θl/θl,tot 
(o) 
tTF 
(ms) 
GC 
a-b-c 
2.5 
21.3 
- 
- 
15.4 
21.3 
a-b 
2.5 
20.2 
60.0 
- 
25.0 
20.2 
b-c-g 
2.5/ 
100 
20.2/ 
21.4 
187.6/ 
181.5 
21.4/ 
3.1 
15.4/ 
0.5 
20.2/ 
21.4 
a-g 
0/ 
100 
20.2/ 
21.3 
0.0/ 
0.0 
0.0/ 
0.0 
56.8/ 
-12.5 
20.2/ 
21.3 
ISL 
a-b-c 
2.5 
21.6 
- 
- 
15.4 
21.6 
a-b 
2.5 
20.2 
59.9 
- 
25.0 
20.2 
b-c-g 
2.5/ 
100 
20.3/ 
21.5 
178.9/ 
178.5 
-1.7/ 
-2.8 
15.4/ 
0.4 
20.3/ 
21.5 
a-g 
0/ 
100 
20.4/ 
21.5 
0.0/ 
-0.3 
0.0/ 
0.0 
56.8/ 
-12.6 
20.4/ 
21.5 
 
TABLE IX 
CRITICAL CALCULATIONS OF RELAY R2,3 DURING FAULTS AT ΤHE MIDPOINT 
OF L2,3 (SCENARIO 4) 
Fault 
type 
Rf,min/ 
Rf,max 
(Ω) 
tS 
(ms) 
φΙs,21 
(o) 
φΙs,20 
(o) 
θl/θl,tot 
(o) 
tTF 
(ms) 
a-b-c 
2.5 
21.3 
- 
- 
12.2 
22.2 
a-b 
2.5 
21.7 
60.0 
- 
20.8 
21.9 
b-c-g 
2.5/ 
100 
21.2/ 
22.1 
176.6/ 
181.0 
-28.8/ 
2.4 
12.2/ 
0.4 
22.1/ 
29.3 
a-g 
0/ 
100 
20.3/ 
21.9 
0.0/ 
0.0 
0.0/ 
0.0 
56.8/ 
-12.8 
21.5/ 
25.4 
 
5) Scenario 5: IIDG-based islanded network 
A well-known protection issue when the network is IIDG-
dominated, especially if it operates as an island, is the de-
creased relay sensitivity due to the low short-circuit current 
contribution of IIDGs. As also explained in Subsection III.E 
for resistive faults, the proposed PnP relay can detect faults 
characterized by a quite low short-circuit current, as its start-
ing functions are desensitized as much as possible, in compli-
ance with the capabilities of commercial relays. To consider 
an extreme case, we assume that the system of Fig. 4 can op-
erate as a fully (100%) IIDG-based island. To this end, SG1 
and SG2 are assumed being disconnected, while, two PV units 
of the same MW rating are instead connected to the respective 
buses. It is also assumed that all the PV units provide reactive 
support. Table X includes the critical calculations of relay R2,3, 
during faults at the midpoint of L2,3. According to the relevant 
explanation of Subsection III.A.2, in this special case, we rely 
on the voltage-based PS. Although the measured short-circuit 
currents are relatively low in Scenario 5, the starting quantities 
always quickly exceed the respective starting thresholds. After 
initiation, the relay always specifies the fault type and the fault 
direction correctly, issuing an instantaneous trip order. 
 
 
 
 
 


---

Page 14

---

1949-3053 (c) 2019 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TSG.2019.2945694, IEEE
Transactions on Smart Grid
 
13 
TABLE X 
CRITICAL CALCULATIONS OF RELAY R2,3 DURING FAULTS AT ΤHE MIDPOINT 
OF L2,3 (SCENARIO 5) 
Fault 
type 
Rf,min/ 
Rf,max 
(Ω) 
tS 
(ms) 
φV,21 
(o) 
φV,20 
(o) 
ΔUa 
(%) 
ΔUb 
(%) 
ΔUc 
(%) 
θl/θl,tot 
(o) 
tTF 
(ms) 
a-b-c 
2.5 
21.4 
- 
- 
- 
- 
- 
9.6 
21.4 
a-b 
2.5 
24.9 240.7 
- 
- 
- 
- 
15.9 
24.9 
b-c-g 2.5/ 
100 
27.3/ 
22.4 
-/ 
- 
-23.8/ 
-63.4 
63.2/ 
-2.1 
87.3/ 
10.3 
89.5/ 
15.3 
9.6/ 
5.6 
27.3/ 
22.9 
a-g 
0/ 
100 
23.1/ 
22.4 
-/ 
- 
-58.7/ 
-58.7 
96.1/ 
15.4 
-7.5/ 
0.1 
6.3/ 
-5.4 
56.7/ 
-9.4 
23.4/ 
22.9 
 
6) Scenario 6: Application to the IEEE 14-bus test system 
To further validate the independence of the proposed PnP 
protection scheme from specific system conditions, the 
scheme is applied to the 33-kV (distribution) part of the IEEE 
14-bus test system [46], shown in Fig. 7. This part is connect-
ed to a 132-kV system, through the transformers feeding buses 
B6 and B9 of Fig. 7. We assume that the 33-kV system operates 
in the ISL mode when it is disconnected from these transform-
ers and is fed solely from the synchronous generator SG. Alt-
hough SG injects only reactive power during the GC mode, it 
also assumed injecting active power to support the ISL opera-
tion. The proposed protection scheme can protect the line 
segments and buses of the system of Fig. 7 in the same logic 
as that described previously throughout the paper. In the pre-
sent example, we focus on the relay R12,6 of Fig. 7, protecting 
line segment L6,12 (along with its opponent relay R6,12).  
 
 
 
Fig. 7.  33-kV part of the IEEE 14-bus test system. 
 
TABLE XI 
CRITICAL CALCULATIONS OF RELAY R12,6 DURING FAULTS AT ΤHE MIDPOINT 
OF L6,12 IN THE IEEE 14-BUS TEST SYSTEM (SCENARIO 6) 
O/M Fault 
type 
Rf,min/ 
Rf,max 
(Ω) 
tS 
(ms) 
φΙs,21 
(o) 
φΙs,20 
(o) 
θl/θl,tot 
(o) 
tTF 
(ms) 
GC 
a-b-c 
2.5 
18.0 
- 
- 
-3.1 
18.0 
a-b 
2.5 
19.0 
59.9 
- 
3.4 
19.0 
b-c-g 
2.5/ 
100 
16.9/ 
23.2 
171.6/ 
180.1 
-14.9/ 
0.1 
-3.1/ 
-9.8 
16.9/ 
23.2 
a-g 
0/ 
100 
16.9/ 
23.2 
0.0/ 
0.8 
0.7/ 
0.7 
51.3/ 
-22.7 
16.9/ 
23.2 
ISL 
a-b-c 
2.5 
18.0 
- 
- 
-2.8 
18.0 
a-b 
2.5 
22.0 
60.0 
- 
3.2 
22.0 
b-c-g 
2.5/ 
100 
17.0/ 
23.3 
173.8/ 
179.7 
-11.4/ 
-0.6 
-2.8/ 
-9.3 
17.0/ 
23.3 
a-g 
0/ 
100 
17.0/ 
23.3 
0.0/ 
0.0 
0.0/ 
0.0 
50.7/ 
-22.9 
17.0/ 
23.3 
 
Table XI shows the critical calculations of relay R12,6, dur-
ing faults at the midpoint of L6,12, in both the GC and the ISL 
mode of system operation. It appears that the relay operates 
quickly and correctly in all the simulated fault cases. Just to 
mention, the opponent relay R6,12 also operates correctly in all 
cases and cancels its blocking signal, letting R12,6 trip at t = tTF 
(as respectively performed by R12,6). Note that the starting 
times (tS) of Table XI result from (3), bearing in mind that a 
60-Hz system is examined in this scenario. 
V.  COMPARISON WITH CURRENT DIFFERENTIAL PROTECTION 
The main drawbacks of a differential scheme compared to 
the proposed PnP scheme are practical, and regard the need for 
properly setting the differential relays due to sensitivity, secu-
rity and coordination purposes (unlike the PnP relays), as well 
as the need for separate schemes/relays to protect a main line 
segment and its adjacent bus/lateral (also refer to Section I). 
However, it would be interesting to also compare the two 
protection schemes in terms of performance. For this purpose, 
a differential scheme is assumed protecting each main line 
segment Li,j, while, a differential scheme is also considered 
protecting each bus/lateral Bi/Li of the system of Fig. 4. The 
pickup differential current (Id,p) is set equal to 5%In for main 
line differential relays, i.e. as the default threshold of (2) and 
(9). Assuming a uniform CT ratio of 200:5 (as before), 5%In 
equals 10 pri. A. As for the differential relays protecting bus-
es/laterals, Id,p is set greater than the differential current meas-
ured during normal load conditions. To this end, the maximum 
load current flowing through each lateral and any infeed load 
currents from DG units are taken into account. A safety factor 
of 1.2 [11] is also considered in the latter cases. 
In this study, faults of all types have been simulated at the 
midpoint of all segments Li,j, at all main line buses Bi and at 
the endpoint of all laterals Li. The same fault resistance cases 
as before have been considered, while, each fault has been 
simulated in both the GC and the ISL mode of the system. 
As for the main line segments, both the differential and the 
PnP scheme have detected and cleared all the faults. Regard-
ing bus/lateral faults, the differential scheme has displayed 
similar performance in the vast majority of fault cases; how-
ever, it has failed to detect and clear most of the 100-Ω ground 
faults at buses B4 and B4.R, as well as B7 and B7.R. On the other 
hand, the PnP scheme have detected and cleared all the faults. 
Due to the great amount of results, only those concerning 
the above critical faults at B4 and B4.R are indicatively provid-
ed in Table XII. This table includes the differential current 
measured by the differential scheme protecting B4/L4. The 
values in bold are lower than the corresponding Id,p setting 
(shown in Table XII), leading to differential protection failure. 
The main reason for that is the need to desensitize the Id,p set-
ting, due to the connection of SG1 to B4. Exactly the same sit-
uation appears during 100-Ω ground faults at B7 and B7.R. 
Table XII also includes the starting quantities measured by 
the GR4 PnP relays in the same fault cases. 3ꞏI0,s,4,3, 3ꞏI0,s,4,8 
and 3ꞏI0,s,4,5 is the superimposed residual current measured by 
R4,3, R4,8 and R4,5, respectively. As can be seen, sensitivity is-
sues appear in this case as well, as R4,5 fails to detect the faults 
and start its operation (see the bolded values). In this regard, 
R4,5 does not transmit a blocking signal either. However, the 


---

Page 15

---

1949-3053 (c) 2019 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TSG.2019.2945694, IEEE
Transactions on Smart Grid
 
14 
use of the redundant trip (inter-trip) order (see Section II), 
renders the PnP scheme able to clear a fault, on condition that 
at least one of the assigned relays senses the fault. Hence, in 
all the cases of Table XII, R4,3 and R4,8 detect the fault, trip-
ping not only their own CB, but also the CB of the rest GR4-
relays (including that of R4,5). Exactly the same situation ap-
pears during 100-Ω ground faults at B7 and B7.R. Note that in 
all the cases of this study, after initiation, the PnP scheme al-
ways correctly specifies the fault type and the fault direction. 
Just to mention, it would be even easier for the PnP relays 
protecting B4/L4 and B7/L7 to detect the simulated 100-Ω 
ground faults, if a CT with a In lower than 200 pri. A was con-
sidered for each relay. This would be permissible, based on 
the maximum load of the line segments where these relays are 
installed. However, the 200:5 CT ratio has been universally 
considered, for the sake of uniformity. On the other hand, a 
different CT ratio would not affect (sensitize) the Ip,d setting of 
the differential scheme protecting B4/L4 and B7/L7. 
 
TABLE XII 
PICKUP/STARTING QUANTITIES MEASURED BY THE DIFFERENTIAL AND THE 
PLUG-AND-PLAY SCHEME DURING 100-Ω GROUND FAULTS AT B4/B4.R 
 
Pickup/starting 
quantity shown 
Fault 
type 
Faulted 
bus 
GC 
mode 
ISL 
mode 
Differential 
protection 
scheme 
Differential 
current (pri. A) 
(Id,p = 76 pri. A) 
b-c-g 
B4 
80.4 
68.8 
B4.R 
78.2 
64.2 
a-g 
B4 
62.2 
55.2 
B4.R 
54.6 
51.2 
PnP  
protection 
scheme 
3ꞏI0,s,4,3 (pri. A)  
3ꞏI0,s,4,8 (pri. A)  
3ꞏI0,s,4,5 (pri. A) 
(default starting 
threshold = 10 pri. A) 
b-c-g 
B4 
11.7 
11.7 
6.2 
11.5 
11.5 
6.1 
B4.R 
10.6 
10.6 
5.6 
10.3 
10.3 
5.5 
a-g 
B4 
11.6 
11.6 
6.2 
11.2 
11.2 
6.1 
B4.R 
10.5 
10.5 
5.6 
10.2 
10.2 
5.5 
VI.  CONCLUSION 
To provide a reliable protection solution for future OH 
looped/meshed distribution systems with DG, eliminating pro-
tection design complexity, this paper proposes a protection 
scheme, which relies on PnP, communication-assisted, numer-
ical relays. The PnP relays are beforehand designed so that 
they do not require user-defined settings, being unaffected by 
system changes and independent of a particular network. As 
such, coordination of main line relays with each other as well 
as coordination between main line relays and lateral protection 
means is guaranteed, without needing a coordination study. 
Only the upload of existing lateral protection means’ charac-
teristics to the relays is required, which is, however, a simple 
and effortless task. Replacement of existing lateral protection 
means is also not needed. The latter fact, as well as the em-
ployment of existing relay capabilities, enhance the scheme’s 
applicability. The simulation results are very promising, as the 
scheme proves effective against a variety of different fault and 
system conditions. Hardware experiments, to further validate 
the proposed scheme, are still pending. It is the authors’ goal 
to conduct such experiments as part of future work. 
VII.  REFERENCES 
[1] 
J. L. Blackburn and T. J. Domin, Protective relaying: Principles and 
applications. Boca Raton, FL, USA: CRC Press, 2014. 
[2] 
E. Dehghanpour, H. K. Karegar, R. Kheirollahi, and T. Soleymani, 
“Optimal coordination of directional overcurrent relays in microgrids by 
using cuckoo-linear optimization algorithm and fault current limiter,” 
IEEE Trans. Smart Grid, vol. 9, no. 2, pp. 1365-1375, Mar. 2018. 
[3] 
H. M. Sharaf, H. H. Zeineldin, and E. El-Saadany, “Protection coordina-
tion for microgrids with grid-connected and islanded capabilities using 
communication assisted dual setting directional overcurrent relays,” 
IEEE Trans. Smart Grid, vol. 9, no. 1, pp. 143-151, Jan. 2018. 
[4] 
A. Yazdaninejadi, S. Golshannavaz, D. Nazarpour, S. Teimourzadeh, 
and F. Aminifar, “Dual-setting directional overcurrent relays for protect-
ing automated distribution networks,” IEEE Trans. Ind. Informat., vol. 
15, no. 2, pp. 730-740, Feb. 2019. 
[5] 
V. C. Nikolaidis, E. Papanikolaou, and A. S. Safigianni, “A communica-
tion-assisted overcurrent protection scheme for radial distribution sys-
tems with distributed generation,” IEEE Trans. Smart Grid, vol. 7, no. 1, 
pp. 114-123, Jan. 2016. 
[6] 
L. Che, M. E. Khodayar, and M. Shahidehpour, “Adaptive protection 
system for microgrids: Protection practices of a functional microgrid 
system,” IEEE Electrific. Mag., vol. 2, no. 1, pp. 66-80, Mar. 2014. 
[7] 
J. R. Fairman, K. Zimmerman, J. W. Gregory, and J. K. Niemira, “Inter-
national drive distribution automation and protection,” presented at the 
27th Annu. Western Protective Relay Conf., Spokane, WA, USA, 2000. 
[8] 
S. Lauria, A. Codino, and R. Calone, “Protection system studies for 
ENEL Distribuzione's MV loop lines,” in Proc. PowerTech, Eindhoven, 
Netherlands, 2015, pp. 1-6. 
[9] 
E. Sortomme, S. S. Venkata, and J. Mitra, “Microgrid protection using 
communication-assisted digital relays,” IEEE Trans. Power Del., vol. 
25, no. 4, pp. 2789-2796, Oct. 2010. 
[10] X. Liu, M. Shahidehpour, Z. Li, X. Liu, Y. Cao, and W. Tian, “Protec-
tion scheme for loop-based microgrids,” IEEE Trans. Smart Grid, vol. 8, 
no. 3, pp. 1340-1349, May 2017. 
[11] T. S. Aghdam, H. K. Karegar, and H. H. Zeineldin, “Variable tripping 
time differential protection for microgrids considering DG stability,” 
IEEE Trans. Smart Grid, vol. 10, no. 3, pp. 2407-2415, May 2019. 
[12] G. Ziegler, Numerical Differential Protection: Principles and Applica-
tions. Erlangen, Germany: Publicis Publishing, 2012. 
[13] H. F. Habib, T. Youssef, M. H. Cintuglu, and O. Mohammed, “Multi-
agent-based technique for fault location, isolation and service restora-
tion,” IEEE. Trans. Ind. Appl., vol. 53, no. 3, pp. 1841-1851, May 2017. 
[14] A. M. Tsimtsios, G. N. Korres, and V. C. Nikolaidis, “A pilot-based 
distance protection scheme for meshed distribution systems with distrib-
uted generation,” Int. J. Elect. Power Energy Syst., vol. 105, pp. 454-
469, Feb. 2019. 
[15] M. Elkhatib, A. Ellis, M. Biswal, S. Brahma, and S. Ranade, “Protection 
of renewable-dominated microgrids: Challenges and potential solu-
tions,” Sandia National Laboratories, Albuquerque, NM, USA, Rep. 
SAND2016-11210, Nov. 2016. 
[16] M. A. Zamani, A. Yazdani, and T. S. Sidhu, “A communication-assisted 
protection strategy for inverter-based medium-voltage microgrids,” 
IEEE Trans. Smart Grid, vol. 3, no. 4, pp. 2088-2099, Dec. 2012. 
[17] C. Yuan, K. Lai, M. S. Illindala, M. A. Haj-ahmed, and A. S. Khalsa, 
“Multilayered protection strategy for developing community microgrids 
in village distribution systems,” IEEE Trans. Power Del., vol. 32, no. 1, 
pp. 495-503, Feb. 2017. 
[18] V. A. Papaspiliotopoulos, G. N. Korres, V. A. Kleftakis, and N. D. Hat-
ziargyriou, “Hardware-in-the-loop design and optimal setting of adap-
tive protection schemes for distribution systems with distributed genera-
tion,” IEEE Trans. Power Del., vol. 32, no. 1, pp. 393-400, Feb. 2017. 
[19] E. Purwar, D. N. Vishwakarma, and S. P. Singh, “A novel constraints 
reduction based optimal relay coordination method considering variable 
operational status of distribution system with DGs,” IEEE Trans. Smart 
Grid, vol. 10, no. 1, pp. 889-898, Jan. 2019. 
[20] Z. Liu, H. K. Høidalen, and M. M. Saha, “An intelligent coordinated 
protection and control strategy for distribution network with wind gener-
ation integration,” CSEE J. Power Energy Syst., vol. 2, no. 4, pp. 23-30, 
Dec. 2016. 


---

Page 16

---

1949-3053 (c) 2019 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
This article has been accepted for publication in a future issue of this journal, but has not been fully edited. Content may change prior to final publication. Citation information: DOI 10.1109/TSG.2019.2945694, IEEE
Transactions on Smart Grid
 
15 
[21] A. Abbasi, H. K. Karegar, and T. S. Aghdam, “Adaptive protection 
coordination with setting groups allocation,” Int. J. Renewable Energy 
Res., vol. 9, no. 2, pp. 795-803, Jun. 2019. 
[22] H. Muda and P. Jena, “Sequence currents based adaptive protection 
approach for DNs with distributed energy resources,” IET Gen., Transm. 
Distrib., vol. 11, no. 1, pp. 154-165, May 2017. 
[23] Z. Liu, C. Su, H. K. Høidalen, and Z. Chen, “A Multiagent system-based 
protection and control scheme for distribution system with distributed-
generation integration,” IEEE Trans. Power Del., vol. 32, no. 1, pp. 536-
545, Feb. 2017. 
[24] S. A. Hosseini, A. Nasiri, and S. H. H. Sadeghi, “A decentralized adap-
tive scheme for protection coordination of microgrids based on team 
working of agents,” in Proc. 7th Int. Conf. Renewable Energy Res. 
Appl., Paris, France, 2018, pp. 1315-1320. 
[25]  M. Y. Shih, A. Conde, Z. Leonowicz, and L. Martirano, “An adaptive 
overcurrent coordination scheme to improve relay sensitivity and over-
come drawbacks due to distributed generation in smart grids,” IEEE 
Trans. Ind. Appl., vol. 53, no. 6, pp. 5217-5228, Nov.-Dec. 2017. 
[26] D. P. Mishra, S. R. Samantaray, and G. Joos, “A combined wavelet and 
data-mining based intelligent protection scheme for microgrid,” IEEE 
Trans. Smart Grid, vol. 7, no. 5, pp. 2295-2304, Sep. 2016. 
[27] S. Kar, S. R. Samantaray, and M. D. Zadeh, “Data-mining model based 
intelligent differential microgrid protection scheme,” IEEE Syst. J., vol. 
11, no. 2, pp. 1161-1169, Jun. 2017. 
[28] M. Mishra and P. K. Rout, “Detection and classification of micro-grid 
faults based on HHT and machine learning techniques,” IET Gen., 
Transm. Distrib., vol. 12, no. 2, pp. 388-397, Jan. 2018. 
[29] J. J. Q. Yu, Y. Hou, A. Y. S. Lam, V. O. K. Li, “Intelligent fault detec-
tion scheme for microgrids with wavelet-based deep neural networks,” 
IEEE Trans. Smart Grid, vol. 10, no. 2, pp. 1694-1703, Mar. 2019. 
[30] Y. Liu, A. P. Meliopoulos, L. Sun, and S. Choi, “Protection and control 
of microgrids using dynamic state estimation,” Prot. Control Mod. Pow-
er Syst., vol. 3, no. 1, pp. 1-13, Dec. 2018. 
[31] S. B. A. Bukhari, R. Haider, M. S. U. Zaman, Y. Oh, G. Cho, C. Kim, 
“An interval type-2 fuzzy logic based strategy for microgrid protection,” 
Int. J. Elect. Power Energy Syst., vol. 98, pp. 209-218, Jun. 2018. 
[32] Z. Zhang, B. Xu, P. Crossley, and L. Li, “Positive-sequence-fault-
component-based blocking pilot protection for closed-loop distribution 
network with underground cable,” Int. J. Elect. Power Energy Syst., vol. 
94, pp. 57-66, Jan. 2018. 
[33] G. Benmouyal and J. Roberts, “Superimposed quantities: Their true 
nature and application in relays,” presented at the 26th Annu. Western 
Protective Relay Conf., Spokane, WA, USA, Oct. 26-28, 1999. 
[34] D60 Line Distance Relay, GE, Markham, ON, Canada, 2009. [Online]. 
Available:         https://www.gegridsolutions.com/products/manuals/d60/ 
d60man-f5.pdf 
[35] G. Ziegler, Numerical Distance Protection: Principles and Applications. 
Erlangen, Germany: Publicis Publishing, 2011. 
[36] B. Kasztenny, B. Cambell, and J. Mazereeuw, “Phase selection for sin-
gle-pole tripping–Weak infeed conditions and cross-country faults,” pre-
sented at the 27th Annu. Western Protective Relay Conf., Spokane, WA, 
USA, Oct. 24-26, 2000. 
[37] M. A. Azzouz, A. Hooshyar, and E. F. El-Saadany, “Resilience en-
hancement of microgrids with inverter-interfaced DGs by enabling 
faulty phase selection,” IEEE Trans. Smart Grid, vol. 9, no. 6, pp. 6578-
6589, Nov. 2018. 
[38] A. Hooshyar, E. F. El-Saadany, and M. Sanaye-Pasand, “Fault type 
classification in microgrids including photovoltaic DGs,” IEEE Trans. 
Smart Grid, vol. 7, no. 5, pp. 2218-2229, Sep. 2016. 
[39] A. M. Tsimtsios and V. C. Nikolaidis, “Setting zero-sequence compen-
sation factor in distance relays protecting distribution systems,” IEEE 
Trans. Power Del., vol. 33, no. 3, pp. 1236-1246, Jun. 2018. 
[40] IEEE Recommended Practice for Monitoring Electric Power Quality, 
IEEE Standard 1159, 2009. 
[41] V. C. Nikolaidis, A. D. Patsidis, and A. M. Tsimtsios, “High impedance 
fault modelling and application of detection techniques with EMTP-
RV,” J. Eng., vol. 2018, no. 15, pp. 1120-1124, Oct. 2018. 
[42] IEEE Guide for Breaker Failure Protection of Power Circuit Breakers, 
IEEE Standard C37.119, 2016. 
[43] C. Gellings, “Estimating the costs and benefits of the smart grid: A 
preliminary estimate of the investment requirements and the resultant 
benefits of a fully functioning smart grid,” Electric Power Research In-
stitute, Palo Alto, CA, USA, Rep. 1022519, 2011. 
[44] C. A. P. Meneses and J. R. S. Mantovani, “Improving the grid operation 
and reliability cost of distribution systems with dispersed generation,” 
IEEE Trans. Power Syst., vol. 28, no. 3, pp. 2485-2496, Aug. 2013. 
[45] M. E. Samper and A. Vargas, “Investment decisions in distribution 
networks under uncertainty with distributed generation—Part I: Model 
formulation,” IEEE Trans. Power Syst., vol. 28, no. 3, pp. 2331-2340, 
Aug. 2013. 
[46] University of Washington, “Power systems test case archive,” Seattle, 
WA, USA, Aug. 1993. [Online]. Available: http://labs.ece.uw.edu/pstca/ 
pf14/pg_tca14bus.htm 
VIII.  BIOGRAPHIES 
Aristotelis M. Tsimtsios (S’17) received the Diploma of Electrical and Com-
puter Engineering and the M.Sc. in Energy Systems and Renewable Energy 
Sources from the Department of Electrical and Computer Engineering, 
Democritus University of Thrace, Xanthi, Greece, in 2013 and 2015, respec-
tively. He is now pursuing a Ph.D. at the same Department. His research in-
terests include power system protection/reliability and distributed generation. 
 
Vassilis C. Nikolaidis (M’ 2011, SM’ 2018) received the five-year Diploma 
of Electrical and Computer Engineering from the Department of Electrical and 
Computer Engineering, Democritus University of Thrace, Xanthi, Greece, in 
2001, the M.Eng. degree in Energy Engineering and Management from Na-
tional Technical University of Athens (NTUA), Athens, Greece, in 2002, and 
the Doctor of Engineering from NTUA, in 2007. Since 2008 he has been 
working as a power systems consulting engineer. Currently he is an Assistant 
Professor in the Department of Electrical and Computer Engineering, 
Democritus University of Thrace, Greece. His research interests mainly deal 
with power system protection, control, stability, and transients. 
 
 
 
