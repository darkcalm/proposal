

---

Page 1

---

 
Coordination of Load Tap Changer and Distributed Energy
Resources to Improve Long-term Voltage Stability
Citation for published version (APA):
Tran, M.-Q., Tran, T. T., Nguyen, P. H., & Tuan, L. A. (2022). Coordination of Load Tap Changer and Distributed
Energy Resources to Improve Long-term Voltage Stability. In ENERGYCON 2022 - 2022 IEEE 7th International
Energy Conference, Proceedings Article 9830224 Institute of Electrical and Electronics Engineers.
https://doi.org/10.1109/ENERGYCON53164.2022.9830224
DOI:
10.1109/ENERGYCON53164.2022.9830224
Document status and date:
Published: 21/07/2022
Document Version:
Accepted manuscript including changes made at the peer-review stage
Please check the document version of this publication:
• A submitted manuscript is the version of the article upon submission and before peer-review. There can be
important differences between the submitted version and the official published version of record. People
interested in the research are advised to contact the author for the final version of the publication, or visit the
DOI to the publisher's website.
• The final author version and the galley proof are versions of the publication after peer review.
• The final published version features the final layout of the paper including the volume, issue and page
numbers.
Link to publication
General rights
Copyright and moral rights for the publications made accessible in the public portal are retained by the authors and/or other copyright owners
and it is a condition of accessing publications that users recognise and abide by the legal requirements associated with these rights.
            • Users may download and print one copy of any publication from the public portal for the purpose of private study or research.
            • You may not further distribute the material or use it for any profit-making activity or commercial gain
            • You may freely distribute the URL identifying the publication in the public portal.
If the publication is distributed under the terms of Article 25fa of the Dutch Copyright Act, indicated by the “Taverne” license above, please
follow below link for the End User Agreement:
www.tue.nl/taverne
Take down policy
If you believe that this document breaches copyright please contact us at:
openaccess@tue.nl
providing details and we will investigate your claim.
Download date: 01. Jun. 2025


---

Page 2

---

Coordination of Load Tap Changer and Distributed
Energy Resources to Improve Long-term Voltage
Stability
Minh-Quan Tran, Trung Thai Tran, Phuong H. Nguyen
Department of Electrical Engineering
Eindhoven University of Technology
Eindhoven, The Netherlands
{m.q.tran, t.t.tran, p.nguyen.hong}@tue.nl
Le Anh Tuan
Department of Electrical Engineering
Chalmers University of Technology
Gothenburg, Sweden
tuan.le@chalmers.se
Abstract—Along with the increased installation of the dis-
tributed energy resources (DER) in distribution system, long-
term voltage stability at the transmission level can be improved
if proper coordination is developed between DERs and the
existing grid controllers, e.g., load tap changer (LTC). This
paper analyzes the problem of long-term voltage instability
and presenting possible countermeasures. The study summarizes
essential aspects for modelling, including LTC, DERs, and es-
pecially voltage dependent load. A coordination between DERs
and LTC is proposed to allocate better power supply, especially
at the coupling points between transmission and distribution
networks, i.e. primary substation. A case study is performed
using a modified CIGRE medium-voltage benchmark network.
The simulation results have shown that the coordination has
substantially improved the long-term voltage stability in the way
of using the reactive power support from DERs and increasing
the LTC position instated of decreasing as the traditional method.
Index Terms—Distribution energy resource, control coordina-
tion, long-term voltage stability.
I. INTRODUCTION
Due to a lack of power supply to the (passive) distribution
network after emergencies, an issue of long-term voltage
instability might occur [1]. One the one hand, the presence
of distributed energy resources (DER), e.g. solar PV, wind,
or storage, can be considered to resolve this issue. On the
other hand, the coordination of DERs with the existing grid
controller, i.e. load tap changer (LTC) is essential to secure
the operation between transmission and distribution networks.
This has been highlighted also by ENTSO, ISGAN, NERC
[2]–[4].
As defined in [5], voltage stability refers to the ability
of a power system to maintain steady voltages at all buses
in the system after being violated from a given operating
condition by disturbances. The time frame for voltage stability
may vary from few seconds (short-term) to tens of minutes
(long-term). This paper deals with long-term voltage stability
in the transmission system, especially at the coupling points
The work leading to this paper is from work-package 3 of FlexiGrid
project that is funded by the European Community’s Horizon 2020 Framework
Programme under grant agreement no. 864048.
between transmission and distribution networks. Investigating
long-term voltage stability requires proper models to capture
accurately grid dynamics. In [1], conventional components
such as LTC and dynamic load have been included. Especially,
voltage dependent load, i.e. induction motor, plays a crucial
role in causing the instability. To analyze the impact of DERs
on long-term voltage stability, various models are presented
in [6]–[9]. A simplified version of the Western Electricity
Coordinating Council (WECC) model is used in [6], which
omitted fast reactive current injection characteristic during the
fault as well as the plant-level controller of inverter-based
generator model. A model for large-scale DER generation
is presented in [7]. An improved PQ controller at the plant
level is proposed to effectively support the long-term voltage
stability. Furthermore, in [8], [9], the impact of tripping of
DER due to the terminal voltage drop and the interaction
among multiple DERs is considered by using a detailed DER
model.
The availability of DERs in distribution networks can
contribute to support long-term voltage stability. In [10], a
distributed model predictive control (MPC) is developed to
keep the voltage of multi-area within the acceptable bounds.
Authors in [11] presented a centralized MPC to regulate the
voltage at coupling points of DERs. In [12], authors inves-
tigated the challenges of DERs integration into low voltage
(LV) networks. The risks of voltage rise related to the discon-
nection of DERs were identified, and active power curtailment
approaches were proposed to mitigate the problem of voltage
rise. Further, adaptive coordination of sequential droop for PV
is developed in [13] to solve the voltage rise problem while
being able to reduce the amount of power curtailment. In
[9], an adaptive proportional-integral controller is developed
for multiple inverters to regulate DERs’s terminal voltages.
It showed that the voltage correction of the one or several
DERs may result in over-voltage at another DER’s terminal
bus, leading to a need for system-wide coordination. The
coordination between DERs and LTC has been investigated
in [6], [10], [11], [14] to address instability issue at the
primary side of the high-voltage/medium-voltage (HV/MV)


---

Page 3

---

transformer. However, the coordination, especially between
DERs and LTC, during stressed operation conditions (e.g.,
after a large disturbance) is still a challenge.
This paper aims to investigate the capability of DERs
to support long-term voltage stability. First, we reformulate
the stability problem, considering essential elements such as
LTC, and voltage dependent load. Second, we investigate a
possible coordination scheme to ensure the support of DERs
and LTC in emergencies. Lastly, a simulation is performed
in a modified CIGRE MV benchmark network to show the
benefit of adequately coordinating between the grid operator
and DERs.
II. COMPONENTS AFFECTING LONG-TERM VOLTAGE
INSTABILITY
In this section, the long-term voltage instability is discussed.
First, different elements affecting long-term voltage instability
such as LTC and dynamic load are presented. Then, a sim-
ulation is performed using MATLAB/Simulink to illustrate
the issue of voltage instability at the coupling point between
transmission and distribution (T-D) networks.
A. Load Tap Changer
The HV/MV transformer is considered as an interface
between the T-D network. Normally, it is installed with the
LTC which operates automatically to maintain voltage of the
secondary side of the transformer within a predefined limit.
While a disturbance occurs that cause a voltage drop, the LTC
adjusts transformer’s tap-setting to bring back the secondary
voltage to its pre-disturbance level. The operation of taps can
be summarized as follows [6]:
tapk+1 =





tapk + △tap , if V > V0 + d and tapk < tapmax
tapk −△tap , if V < V0 −d and tapk > tapmin
tapk , otherwise
(1)
where: tapk and tapk+1 are the current and next tap position;
△tap is the size of each tap step; and the tapmin, tapmax are
the minimum and maximum tap limit, respectively.
The tap is activated depending on the measured voltage V .
The tap position tapk+1 will be increased or decreased if V
is out of a deadband V0 ±d, where V0 is the voltage reference
and d is the deadband limit. Furthermore, tap movement needs
a fixed delay time (normally, from 5-8 seconds) to reach a new
position due to mechanical requirements.
B. Dynamic Load Model
Long-term voltage stability involves slow-acting equipment
devices such as generator current limiters, LTC, and con-
trolled loads. The attempt to restore power consumption of
the dynamic load is usually the reason for long-term voltage
instability [15], [16]. So, that is important to consider the load
model in long-term voltage study. In this work, the exponential
load model is expressed as follows:
P = P0
 V
V0
α
,
(2)
TABLE I
THE α AND β VALUE FOR DIFFERENT LOAD COMPONENTS
Load component
α
β
Incandescent lamps
1.45
-
Room air conditioner
0.5
2.5
Furnace fan
0.08
1.6
Battery charger
2.59
4.06
Electronic compact fluorescent
0.95-1.03
0.31-0.46
Conventional fluorescent
2.07
3.21
Q = Q0
 V
V0
β
(3)
where: V0, P0, and Q0 are the rated terminal voltage, active
power, and reactive power, respectively. α and β are the
exponents controlling the nature of the load.
Table I shows different load devices, which has been
modelled as the exponential load model with different α and
β values [1]. However, the values α and β are normally
set to 1 and 2 for constant current and constant impedance,
respectively.
C. Over Excitation Limiter
Over excitation limiters (OEL) are also named as maximum
excitation limiters or field current limiters. It was designed
to protect the field winding circuit under stress conditions
(i.e., under the large disturbance) [1]. The operation of OEL
can be explained briefly as follows. When a fault happens
nearby, the generator terminal voltage is dropped below the
normal operation. The excitation system will react to support
the voltage by increasing the field current, causing the field
winding is overloaded. The OEL, then, will reduce this high
current to a normal setting after a predefined time interval
due to the thermal limit. As can be seen in Fig. 1, there are
two types of delay interval for the OEL, namely fixed delay
time (Fig. 1 (a)), and inverse delay time (Fig. 1 (b)). When
the field current exceeds the limited value for a fixed delay
time, the field current will be reduced to the limit value after
the corresponding delay time (normally in the range of 10-20
seconds). In the case of using the inverse delay time setting,
the higher field current level is allowed for a shorter time,
Fig. 1. Time delay characteristic of over excitation limiter.


---

Page 4

---

and the lower field current level is allowed for a longer time.
The operation of OEL is to protect the generator winding.
However, due to the limited field current, the reactive power
support from the generator is reduced, which could affect long-
term voltage stability.
D. Distributed Energy Resources
In this paper, DERs are modelled as voltage sourced con-
verter connected with an LCL filter. The DC side is assumed
as a constant DC voltage. The DER is interfaced with the grid
through a transformer. In this work, the DERs are operated
in grid following mode [17], which includes a single current
control loop to follow the P ∗, Q∗control signals from
the higher control layer. The current reference signals are
determined in the dq frame, as follow:
I∗
d
I∗
q

= 3
2
"
P ∗
Vd
Q∗
Vd
#
(4)
where: Vd, Vq, and Id, Iq are the inverter voltages, current in
dq frame, respectively.
The PI controller is designed to minimize the error between
input current references (obtained from equation (4)) and
measured inverter currents. Finally, the output of PI controller
is used as modulation signals for the PWM to generate the
inverter gating signals.
III. INSTABILITY FORMULATION
In this section, a test case is presented using a modified
CIGRE medium voltage benchmark network, as described
[18], [19]. The single-line schematic diagram of the test
network is shown in Fig. 2. The grid is a three-phase system
with 20 kV nominal phase to phase voltage, and the system
frequency is 50 Hz. There are two parallel transmission lines
that have been added to connect the external grid and the
HV-MV substations. The external network is represented by a
110 kV/50 Hz three-phase voltage source, with a short-circuit
power of 500 MVA and R/X ratio of 0.1. The transformer
with a LTC controller is installed between Bus 0 and Bus
1, which is designed to keep the voltage at Bus 1 within a
range from 0.985 p.u. to 1.015 p.u. A synchronous generator
is installed at the HV-MV substation. The MV network is fed
by the two 25 MVA transformers associated with LTC. There
is a mix of residential (LiR) and industrial load (LiC) in the
network (with i is the bus number, where load is connected).
The residential loads are modelled as the power constant loads
with α = β = 0. The voltage dependent model are used to
present the industrial load. The details of line parameters of
this benchmark network are provided in Appendix (Table III).
Consider a three-phase fault occurs at one of the two parallel
transmission lines between external bus and Bus 0, as depicted
in Fig. 2. This transmission line trips at time t = 0 to isolate
the fault. After a short-term period with dynamics assumed to
be stable, the system enters a long-term stage where voltage
stability is of concern. A simulation for this study of long-term
voltage stability involves slow-acting equipment (e.g., LTC,
OEL). In this simulation, the voltage measurement at HV bus
Fig. 2. Modified CIGRE MV distribution network benchmark.
(a)
(b)
(c)
20
20
20
40
40
40
60
60
60
80
80
80
100
100
100
120
120
120
140
140
140
160
160
160
180
180
180
200
200
200
0.7
0.8
0.8
0.9
0.9
1
1
0
−10
−20
Time [s]
VHV [p.u.]
VMV [p.u.]
LTC
LTC actions
OEL operation
First LTC action
LTC is activated
Minimum Tap position
Fig. 3.
Long-term voltage instability. VHV
and VMV
are the voltage
magnitude measured at Bus 1 and Bus 2, respectively. LTC is tap position of
the HV/MV transformer between Bus 1 and Bus 2.
(i.e., Bus 0) and at MV bus (i.e., Bus 1) are shown in Fig. 3.
After a short-term dynamic period, the voltages at HV and MV
buses are stable at VHV = 0.973 p.u., and VMV = 0.928 p.u.,
respectively. Thus, the LTC controller is activated to increase
the voltage at Bus 1. The increasing of the voltage at Bus 1,
following the tap movement is shown in the Fig. 3. The first
LTC action is activated after 15 seconds.
In the sequence of long-term voltage stability, it is important
to take into account the operation of OEL. The field current of


---

Page 5

---

(a)
(b)
20
20
40
40
40
60
60
80
80
100
100
120
120
140
140
160
160
180
180
200
200
6
5
4
3
2
38
36
34
32
Time [s]
Field current [p.u.]
Power [MW]
OEL is activated
Field current is kept
at the limited value
Active power ﬂow
between HV-MV buses line
Fig. 4.
(a) - Field current of the synchronous generator. (b) - Power flow
between HV-MV buses in feeder 1.
TABLE II
SIMULATION CASE WITH DIFFERENT α AND β VALUES
Simulation case
α
β
Case 1
1
1
Case 2
1
1.5
Case 3
1.5
1.5
Case 4
1.5
2
Case 5
1.5
2.5
Case 6
2
2
Case 7
2.5
2.5
synchronous generator is allowed to be overloaded (i.e., ifd >
3.0618 p.u.) for a fixed 20 seconds, as shown in Fig. 4-(a).
Thus, the OEL is activated at t = 24s to protect the generator
winding circuit. As the result, the voltages at HV and MV
buses are dropped to VHV = 0.815 p.u., and VMV = 0.824
p.u., respectively.
It is worth to mention that the MV grid consists of a mix of
residential and industrial load (i.e., dynamic load). In Section
II-B, the model of dynamic load was discussed. The active
and reactive power consumption of a dynamic load depends
on its terminal voltage. Thus, higher voltage at the MV side
of the primary substation causes the increase of the total load
consumption in the MV network. The active power flowing
through the HV-MV buses in the feeder 1 is presented in
Fig. 4-(b). The active power supplying to the distribution grid
increases along with the LTC actions. However, the limited
power transfer capability is reached due to the tripping of
transmission lines. Consequently, the voltage at the HV side of
the transformer (i.e., Bus 0) is decreased below the acceptable
operating range. This may activate the low voltage protection
system, which could lead to cascading tripping of transmission
lines and a possible voltage collapse.
Case 1
Case 2
Case 3
Case 4
Case 5
Case 6
Case 7
20
40
60
80
100
120
140
160
180
200
0.7
0.8
0.9
1
Time [s]
VHV [p.u.]
Fig. 5. Voltage profiles at the Bus 0 (HV bus) with different load character-
istic.
To analyze the impact of load modelling into the long-
term voltage stability, different simulation cases in Table II
were performed. As discussed in Section II-B, different load
components will have different set of α and β values. Thus, the
Table II presents aggregated load model. The voltage profile
at transmission network, VHV is shown in Fig. 5. It can be
observed that the simulation case 1 with α = 1 and β = 1 is
the worst case with lowest VHV profile after the fault. Thus,
having the proper is important aspect for long-term voltage
stability study.
IV. COORDINATION SCHEME FOR DERS AND LTC
As aforementioned, the coordination between DERs and
LTC can contribute to improve the voltage instability issue at
the primary side of the HV/MV transformer. The coordination
strategy needs to consider DER’s local control objectives to
avoid possible conflicts. In addition, the nonlinear dynamic of
DERs needs to be taken into account when their capability
in voltage control is explored [9], [12], [13]. In [9], an adap-
tive proportional-integral controller is developed for multiple
DERs to regulate DERs’s terminal voltages. It shows that the
voltage correction of other DERs may result in over-voltage at
another DER’s terminal bus, leading to a need for system-wide
coordination.
Fig. 6. A centralized coordination control. P DERi
k
, QDERi
k
, and Tapk are
the active, reactive power measurement of DERi, and LTC position at time
step k, respectively. Furthermore, P DERi
k+1
, QDERi
k+1
, and Tapk+1 are the
control signal of active, reactive power of DERi, and LTC position will be
used at time step k + 1, respectively.


---

Page 6

---

(a)
(b)
(c)
20
20
20
40
40
40
60
60
60
80
80
80
100
100
100
120
120
120
140
140
140
160
160
160
180
180
180
200
200
200
0.8
0.9
0.9
0.95
1
1
10
0
−10
−20
Time [s]
VHV [p.u.]
VMV [p.u.]
LTC
Without Coordination
Without Coordination
Without Coordination
With Coordination
With Coordination
With Coordination
Fig. 7. Voltage profiles in case of with and without the coordination. VHV and
VMV are the voltage magnitude measured at Bus 0 and Bus 1, respectively.
LTC is tap position of the HV/MV transformer between Bus 0 and Bus 1.
(a)
(b)
20
20
40
40
60
60
80
80
100
100
120
120
140
140
160
160
180
180
200
200
1
1
0.95
0.95
0.9
0.9
0.85
Time [s]
VHV [p.u.]
VMV [p.u.]
16% DER
16% DER
32% DER
32% DER
Fig. 8. Voltage profiles in case of with and without the coordination of VHV
and VMV with different DER penetration levels.
In this study, it is assumed that a coordination scheme
can overwrite DER’s local controllers with its control signals
from the coordination scheme. The centralized coordination
control is presented in Fig. 6, which aims to coordinate
the operation of LTC and available DER resources to avoid
long-term voltage instability after fault. The active, reactive
power output (i.e., P DERi
k
, QDERi
k
) of DER and current
position of LTC (i.e., Tapk) are collected at the centralized
control. Then, the new control signals for LTC and DERs
are processed depending on the voltage level and available
DERs power. In this section, the modified CIGRE benchmark
network in Section III is used again to show the benefit of
having coordination between LTC and DERs. There are three
DER units which are added at Buses 3, 14, and 9 with their
rating power of S1 = 4.3 MVA, S2 = 4.75 MVA, and S3 =
4.2 MVA, respectively [20]. In this case, the DER can support
16% total power consumption of loads.
In this simulation, the proposed strategy is implemented
in the Simulink model to coordinate DERs and LTC. The
necessary information (i.e., voltage magnitude, DER’s power)
can be collected via measurement or estimated using state esti-
mation [21]. In this work, that information is collected via the
communication system. Then, the long-term voltage stability
is analysed in the case of with and without coordination. Fig.
7 presents the time sequence of control actions. The recorded
primary voltage at the pre-fault stage is V 0
HV = 0.996 p.u. The
coordination scheme is activated based on the alarm signal
with the objective is to bring the primary voltage back to the
pre-fault value. The simulation results show that, the proposed
coordination smoothly brings the primary voltage back to the
pre-fault value while keeping the secondary voltage in its
limits [0.9 1.1] p.u. As can be seen from Fig. 7, in the range
of time t = 20s to t = 60s the voltage is slightly increased
while the LTC is kept unchanged. This is an advantage of
coordinated control. In this period, the power from DERs is
still available. Thus, the controller keeps the LTC unchanged
and used only power from DERs to support the voltage. In the
next period from t = 60s to t = 140s, the powers from DERs
reach their limits. Thus, the controller must use the support
from LTC operation with a higher cost (i.e., operation and
maintenance cost of LTC). The LTC increases its position to
increase the primary voltage of the transformer. Due to the
increasing LTC position, the secondary voltage is decreased.
However, the secondary voltage of the transformer is kept at
the limit of [0.9 1.1] p.u.
To show how the DER can support the long-term voltage
stability, there more DERs are added to the network (S4 = 4.3
MVA at Bus 3, S5 = 4.75 MVA at Bus 14, and S6 = 4.2 MVA
at Bus 9). So, the DER penetration level is increased up to
32%. The Fig. 8 shown the voltage profiles of VHV and VMV
in case of different DER penetration levels. It clearly shows
the benefit of having more DERs into the network. The VMV
voltage is controlled to be stable faster with higher penetration
of DER. It is important to note that, the coordination can
improve the voltage at HV bus while keeping the voltage
at MV bus in the limit of 0.9 p.u. So, this is the trade-off
between the HV-MV buses. This simulation results show the
proposed control method can support the long-term voltage
stability after the large disturbance.
V. CONCLUSION
The long-term voltage stability at the T-D interface is dis-
cussed in this paper. Essential aspects for modelling, including
load tap changer (LTC), distributed energy resources (DER),
and especially voltage dependent load is summarized in this
study. Coordination between DERs and LTC is proposed to
allocate better power supply at the coupling points between
transmission and distribution networks, i.e. primary substation.
The study is performed using a modified CIGRE medium-
voltage benchmark network. The numerical results show a
better voltage profile with the coordination scheme after the
large disturbance. The centralized control collected the LTC
status as well as the active, reactive power output of DERs.


---

Page 7

---

In case of emergency conditions, the reactive power from the
DERs is used to support the voltage. The LTC is used in the
later phase (due to the high operation cost) when DERs reach
their capacity limit. Instated of decreasing the tap position as
which was designed for LTC, the centralized control increased
the tap position to support the HV voltage while keeping the
medium voltage in the operation range.
The case study shows the advantage of having coordination
between grid operators and DERs. Thus, we expect that
different coordination controls will be developed to support the
long-term voltage stability taking into account other aspects
such as dynamic behaviour or uncertainty from DERs. Fur-
thermore, long-term voltage control using advanced controllers
(e.g., model predictive control, reinforcement learning), which
optimally control the voltage could bring other advantages for
system operators.
APPENDIX
The line data of the CIGRE MV distribution network is
given in Table III. It is worth to mention that, the unit of
resistance, reactance, and susceptance are given in ohm/km,
ohm/km, and uS/km, and the line length is shown in Fig. 2.
TABLE III
LINE DATA OF CIGRE MV DISTRIBUTION NETWORK
From
To
R
X
B
R0
X0
B0
1
2
0.50
0.72
47.49
0.82
1.60
47.49
2
3
0.50
0.72
47.49
0.82
1.60
47.49
3
4
0.50
0.72
47.49
0.82
1.60
47.49
4
5
0.50
0.72
47.49
0.82
1.60
47.49
5
6
0.50
0.72
47.49
0.82
1.60
47.49
6
7
0.50
0.72
47.49
0.82
1.60
47.49
7
8
0.50
0.72
47.49
0.82
1.60
47.49
8
9
0.50
0.72
47.49
0.82
1.60
47.49
9
10
0.50
0.72
47.49
0.82
1.60
47.49
10
11
0.50
0.72
47.49
0.82
1.60
47.49
11
4
0.50
0.72
47.49
0.82
1.60
47.49
3
8
0.50
0.72
47.49
0.82
1.60
47.49
12
13
0.51
0.37
3.17
0.66
1.61
1.28
13
14
0.51
0.37
3.17
0.66
1.61
1.28
14
8
0.51
0.37
3.17
0.66
1.61
1.28
ACKNOWLEDGMENT
The authors would like to acknowledge the financial support
for this work from the enabling flexibility for future distribu-
tion grid project FlexiGrid, https://flexigrid.org/.
REFERENCES
[1] T. Van Cutsem and C. Vournas., Voltage Stability of Electric Power
Systems.
Springer Science & Business Media, 1998, vol. 148.
[2] ENTSO (European Network of Transmission System Operators), “Gen-
eral Guidelines fot Reinforcing the Cooperation Between TSOs and
DSOs,” Eurelectric, 2015.
[3] H. B. Antony Zegers, “TSO-DSO interaction: An Overview of current
interaction between transmission and distribution system operators and
an assessment of their cooperation in Smart Grids,” Tech. Rep.
[4] NERC (North American Electric Reliability Corp.), “Essential Reliabil-
ity Services Task Force Measures Framework Report,” no. November,
2015.
[5] N. Hatziargyriou, J. Milanovic, C. Rahmann, V. Ajjarapu, C. Canizares,
I. Erlich, D. Hill, I. Hiskens, I. Kamwa, B. Pal, P. Pourbeik, J. Sanchez-
Gasca, A. Stankovic, T. Van Cutsem, V. Vittal, and C. Vournas,
“Definition and Classification of Power System Stability - Revisited &
Extended,” IEEE Transactions on Power Systems, vol. 36, no. 4, pp.
3271–3281, 2021.
[6] L. D. P. Ospina and T. Van Cutsem, “Power factor improvement
by active distribution networks during voltage emergency situations,”
Electric Power Systems Research, vol. 189, no. April, p. 106771, 2020.
[Online]. Available: https://doi.org/10.1016/j.epsr.2020.106771
[7] E. Munkhchuluun, L. Meegahapola, and A. Vahidnia, “Long-term
voltage stability with large-scale solar-photovoltaic (PV) generation,”
International Journal of Electrical Power and Energy Systems, vol.
117, no. September 2019, p. 105663, 2020. [Online]. Available:
https://doi.org/10.1016/j.ijepes.2019.105663
[8] Z. Li, Q. Guo, S. Member, H. Sun, and S. Member, “A Distributed
Transmission-Distribution-Coupled Static Voltage Stability Assessment
Method Considering Distributed Generation,” vol. 33, no. 3, pp. 2621–
2632, 2018.
[9] H. Li, F. Li, Y. Xu, D. T. Rizy, and S. Adhikari, “Autonomous and
adaptive voltage control using multiple distributed energy resources,”
IEEE Transactions on Power Systems, vol. 28, no. 2, pp. 718–730, 2013.
[10] M. Moradzadeh, R. Boel, and L. Vandevelde, “Voltage coordination in
multi-area power systems via distributed model predictive control,” IEEE
Transactions on Power Systems, vol. 28, no. 1, pp. 513–521, 2013.
[11] G. Valverde and T. Van Cutsem, “Model predictive control of voltages in
active distribution networks,” IEEE Transactions on Smart Grid, vol. 4,
no. 4, pp. 2152–2161, 2013.
[12] P. D. Ferreira, P. M. Carvalho, L. A. Ferreira, and M. D. Ilic, “Distributed
energy resources integration challenges in low-voltage networks: Volt-
age control limitations and risk of cascading,” IEEE Transactions on
Sustainable Energy, vol. 4, no. 1, pp. 82–88, 2013.
[13] T. T. Mai, A. N. M. Haque, P. P. Vergara, P. H. Nguyen, and G. Pemen,
“Adaptive coordination of sequential droop control for PV inverters to
mitigate voltage rise in PV-Rich LV distribution networks,” Electric
Power Systems Research, vol. 192, no. July 2020, p. 106931, 2021.
[Online]. Available: https://doi.org/10.1016/j.epsr.2020.106931
[14] G. Prionistis, T. Souxes, and C. Vournas, “Voltage stability support
offered by active distribution networks,” Electric Power Systems
Research, vol. 190, no. April 2020, p. 106728, 2021. [Online].
Available: https://doi.org/10.1016/j.epsr.2020.106728
[15] H. Hagmar, L. A. Tuan, and R. Eriksson, “Impact of static and
dynamic load models on security margin estimation methods,” Electric
Power Systems Research, vol. 202, no. March 2021, p. 107581, 2022.
[Online]. Available: https://doi.org/10.1016/j.epsr.2021.107581
[16] N. Hatziargyriou, J. Milanovic, C. Rahmann, V. Ajjarapu, C. Canizares,
I. Erlich, D. Hill, I. Hiskens, I. Kamwa, B. Pal, P. Pourbeik, J. Sanchez-
Gasca, A. Stankovic, T. Van Cutsem, V. Vittal, and C. Vournas,
“Definition and Classification of Power System Stability - Revisited &
Extended,” IEEE Transactions on Power Systems, vol. 36, no. 4, pp.
3271–3281, 2021.
[17] D. Raisz, T. T. Thai, and A. Monti, “Power Control of Virtual Oscillator
Controlled Inverters in Grid-Connected Mode,” IEEE Transactions on
Power Electronics, vol. 34, no. 6, pp. 5916–5926, 2019.
[18] K. Strunz, E. Abbasi, C. Abbey, C. Andrieu, U. Annakkage, S. Barsali,
R. C. Campbell, R. Fletcher, F. Gao, T. Gaunt, A. Gole, N. Hatziargyriou,
R. Iravani, G. Joos, H. Konishi, M. Kuschke, E. Lakervi, C.-C. Liu,
J. Mahseredjian, F. Mosallat, D. Muthumuni, A. Orths, S. Papathanas-
siou, K. Rudion, Z. Styczynski, and S. C. Verma, “Benchmark Systems
for Network Integration of Renewable Energy Resources,” no. 273, pp.
4–6, 2011.
[19] K. Strunz, C. Abbey, C. Andrieu, R. C. Campbell, and R. Fletcher,
Benchmark Systems for Network Integration of Renewable and Dis-
tributed Energy Resources, 2014, no. July.
[20] R. Perez-Ibacache, C. A. Silva, and A. Yazdani, “Linear State-Feedback
Primary Control for Enhanced Dynamic Response of AC Microgrids,”
IEEE Transactions on Smart Grid, vol. 10, no. 3, pp. 3149–3161, 2019.
[21] M. Q. Tran, A. S. Zamzam, P. H. Nguyen, and G. Pemen, “Multi-area
distribution system state estimation using decentralized physics-aware
neural networks,” Energies, vol. 14, no. 11, pp. 1–13, 2021.
