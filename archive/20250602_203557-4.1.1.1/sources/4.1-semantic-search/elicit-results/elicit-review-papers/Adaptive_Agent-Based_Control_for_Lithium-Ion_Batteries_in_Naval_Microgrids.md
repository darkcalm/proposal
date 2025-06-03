

---

Page 1

---

Voltage Restoration in MVDC Shipboard Microgrids with Economic
Nonlinear Model Predictive Control
Saskia Putri1, Ali Hosseinipour2, Xiaoyu Ge3, Faegheh Moazeni4, Javad Khazaei5,∗
This work has been submitted to the IEEE for possible publication.
Copyright may be transferred without notice, after which this version may no longer be accessible.
Abstract— Future Naval Microgrids (MGs) will include hybrid
energy storage systems (ESS), including battery and superca-
pacitors to respond to emerging constant power loads (CPLs)
and fluctuating pulsed power loads (PPLs). Voltage regulation
of naval microgrids and power sharing among these resources
become critical for success of a mission. This paper presents a
novel control strategy using nonlinear model predictive controller
embedded with a complex droop control architecture for voltage
restoration and power sharing in medium voltage DC (MVDC)
Naval MGs. The complex droop control ensures allocating
supercapacitors (SCs) for high-frequency loads (i.e., PPLs), while
battery energy storage system (BESS) and auxiliary generators
share the steady-state load (i.e., CPL). Compared to state-of-the-
art control of the naval ship MGs that relies on linear models,
the proposed method incorporates the nonlinear behavior of the
MGs in the closed-loop control framework via nonlinear model
predictive control (NMPC). A reduced order representation
of the MVDC dynamic is employed as the prediction model,
augmented with a multi-objective, constraints-based, optimal
control formulation. The results demonstrate the effectiveness
of the proposed control framework for voltage restoration and
power sharing of resources in naval MGs.
I. INTRODUCTION
With the rapid advancements in the technology and
operation of navy ships, there is an increasing demand for
the development of reliable and adaptable naval microgrid
architectures [1]. Traditional AC systems, characterized by
their rigid architectures and the need for multiple power
transformers that put a burden on the cargo weight, may
not be adequate to accommodate future shipboard power
systems [2]. Therefore, future ship electrification has moved
towards medium voltage DC (MVDC) power systems [3],
[4]. It offers a reliable, low-noise, and highly efficient power
system equipped with environmental protection [4]. How-
ever, within MVDC power systems, formidable challenges
arise, particularly in addressing fast, intermittent, and high-
frequency power demands, such as those from pulsed power
loads (PPL) during railgun operations, laser usage, and high-
power radar application [5]. Furthermore, MVDC systems
in naval vessels face issues pertaining to voltage variation
and power quality degradation due to PPLs and continuous
This work was in part under support from the Department of
Defense,
Office
of
Naval
Research
award
number
N00014-23-1-
2602. The authors are with the Rossin college of engineering and
applied science at Lehigh University, Bethlehem, PA 18015, USA.
(Emails:
sap322@lehigh.edu, alh621@lehigh.edu,
xig620@lehigh.edu, moazeni@lehigh.edu,
khazaei@lehigh.edu)
∗Corresponding author: Javad Khazaei.
variation in propulsion speed [6]. Consequently, an optimal
control approach that is capable of effectively managing these
multi-variate and complex systems is essential.
Many studies have been conducted to optimize MVDC ship
microgrids. In our preliminary results in [6], we proposed a
novel power flow optimization for MVDC shipboard power
systems with hybrid energy storage systems. Optimal power
flow was guaranteed using virtual resistive and capacitive
controllers to manage power fluctuations and minimize
operational costs subject to various system constraints. More-
over, energy management of MVDC power system was
studied in [7] by optimizing load operability and ramp-
rate characteristics of the energy storage systems (ESSs).
The authors utilized receding horizon optimization to reduce
the computational burden when using mixed-integer linear
programming (MILP). However, these studies are performed
in an open-loop configuration. A closed-loop framework that
continuously allows correction of the control input based on
the system’s output is vital when optimizing the MVDC navy
MGs. In [8], the authors implemented a voltage control to
accommodate CPLs in a ship under three control strategies:
state feedback, active damping, and linearization via state
feedback. The study, however, did not accommodate PPLs
that pertain to being the most challenging load to supply due
to their fast-changing demands within seconds. In addition,
the control approach did not explicitly include all constraints
related to generation units and voltage regulation. Given
the existing challenges, model predictive control (MPC) has
emerged as a powerful tool capable of handling constraints
and providing a preview of the system output to yield an
optimal control approach tailored to MVDC power systems
characteristics [9].
MPC utilizes dynamical models of the system as the
prediction model to optimize future control actions while
accommodating system disturbances [10]. It solves online
multiple open-loop control problems over a receding time
horizon, subject to constraints. Various studies have been
conducted on the energy management system of MVDC
shipboard power systems using MPC. In [11], MPC is utilized
to optimize power distribution to loads based on load priorities
and operational constraints. However, the study did not
consider voltage variation that may be caused due to the
abrupt changes in the load and may continuously degrade the
power system performance when left uncontrolled. In another
study, the energy management system of navy MGs integrated
arXiv:2312.03603v2  [eess.SY]  2 May 2024


---

Page 2

---

with ESSs during high-ramp conditions was proposed [12].
Nonetheless, the study utilized a linear prediction model
within the optimal control problem formulation of MPC.
Although the trajectory of the prediction model showed similar
behavior, a distinct level of the variables was observed. This
may be due to the linear prediction model, which may suffer
from a lack of representation of an actual system that exhibits
nonlinear behavior. In addition, none of the existing MPC
approaches considered power sharing between multiple energy
resources, including batteries, supercapacitors, and generators
within a ship. There is currently a research gap for a closed-
loop energy management system of a navy ship that not only
can regulate the DC voltage on the ship but also accommodate
multiple energy resources in the presence of PPLs and CPLs.
To address the aforementioned knowledge gaps, this paper
proposes a novel NPMC formulation with complex droop
control for power sharing among multiple resources and
voltage regulation of MVDC shipboard MGs integrated with
hybrid energy storage systems. The main contributions of the
paper are:
1) Voltage control algorithm of MVDC navy shipboard
MGs is formulated using nonlinear (NMPC). The
control algorithm is capable of restoring the voltage at
a steady level with reliable power management to meet
the pulsed and constant power loads.
2) A complex power sharing algorithm is embedded in the
MPC design to share the high-frequency PPL demand
via supercapacitors and the steady-state CPL demand
via generators and batteries.
3) A reduced order model of MVDC Naval ship MGs is
integrated with virtual capacitive and resistive droop
controllers for energy resources within MG to ensure
voltage restoration and power balance.
4) Optimal control formulation that provides a trade-off
between power-rated and economically-driven power
sharing between the energy resources is provided.
5) The impact of varying duration and magnitude of pulsed
power load on the voltage stabilization performance is
investigated. The control performance is compared to
droop-controlled power management at the component
level to validate the robustness and reliability of the
proposed controller.
The rest of the paper is structured as follows. The
architecture of the proposed MVDC is explained in Section II
while the optimal control problem formulation from the
NMPC framework is described in Section III. Section IV
illustrates the validation of the proposed control algorithm
through a variety of case studies. The conclusions are drawn
in Section V.
II. MVDC NAVY SHIPBOARD MICROGRIDS
A. Proposed model description
Fig. 1 illustrates a generalized architecture of a 6kV
shipboard power system. The generation unit in this system
ensembles a pair of gas turbine-driven generators (SG),
BESSs, and SCs. Considering the high energy density
SGa
DC
DC
DC
DC
DC
DC
AC
DC
AC
DC
AC
DC
AC
DC
AC
DC
M
M
DC
DC
DC
DC
Auxiliary load
Propulsion motor load
Propulsion motor load
Pulsed power load
PG1
PG2
Gas 
Turbine
BESS a
BESS b
SCESS b
SCESS a
Gas 
Turbine
Generator a
Generator b
SGb
ECONOMIC 
NONLINEAR MODEL 
PREDICTIVE CONTROL
NAVAL SHIP ENERGY MANAGEMENT  SYSTEM
Prediction Model
Ref. point
Cost fcn
Optimal control actions,
Finds an optimal 
future trajectory
6kV MVDC SPS
Constraints
Fig. 1.
Proposed layout of the management of the MVDC shipboard power
system (SPS)
attributes of BESSs, they serve as backup sources for the SGs,
ensuring a consistent power supply to meet the auxiliary and
the propulsion motor loads (CPL). On the contrary, the SCs,
equipped with a high power density feature, are intended to
solely accommodate high-frequency power transients in the
system stemming from the PPLs. Given the voltage variation
that occurs in the system, the main control objective in this
paper is to stabilize the voltage trajectory while ensuring load
balance and power sharing between the distributed generation
units (DGUs). In addition, a trade-off to economically dispatch
the DGUs is offered through the addition of a cost-effective
objective. As depicted in Fig. 1, a summary of optimal control
problem formulation is sent to the NMPC framework to find
the optimal future trajectory to operate the proposed MVDC
navy shipboard MGs effectively.
B. Reduced order model representation of the MVDC ship-
board microgrids
In this section, dynamic models of the proposed MVDC
navy shipboard MGs are presented. Given the widespread
practice of DC power systems with short distances, an
equivalent circuit of the system can be derived that neglects
cable longitudinal parameters [13]. Therefore, all capacitors
and nonlinear loads can be designed in parallel, as illustrated
in Fig. 2. Extending from these assumptions, the dynamic
models of the proposed system are expressed in (1), developed
from [13].


---

Page 3

---

Fig. 2.
Equivalent circuit of the proposed MVDC shipboard microgrids
Ceq ˙Vo =
X
i∈NSG
(ISGi) +
X
i∈NB
(IBi) +
X
i∈NSC
(ISCi)
−PCPL
Vo
−PPPL
Vo
(1a)
Li ˙Ii = Vref −RiIi −Vo + δVi
∀i ∈{NSG, NB} (1b)
Li ˙Ii = Vref −RiIi −VCi −Vo
∀i ∈NSC
(1c)
Ci ˙VCi = Ii
∀i ∈NSC
(1d)
where Ceq is the equivalent capacitor in F, Lk is the
inductance of the k-th generation unit in H, Vo denotes the
output voltage in V , Ik as the current of the k-th generation
unit in A, Ri, CSCi are the resistive droop gains for the
conventional generators and BESSs, and capacitive droop
gains for SCs, respectively. Details on the complex droop
control design for the ship can be found in [6], [14], and
detailed parameters of the MGs are listed in Table I, adopted
from [14]. To ensure that the SCs are operated during transient
conditions and deactivated during steady state, capacitive
droop characteristics and voltages of the SCs are embedded
in (1c), with additional SCs’ voltage dynamics in (1d) adopted
from [6], [14].
C. State space model
Accordingly, the state space representation of (1) can be
summarized as follows:
˙x = f(x(t), u(t), d(t))
(2)
where x ∈Rnx = [Vo ISGa ISGb IBa IBb ISCa ISCa]T
is
the
state
variable
vector,
u
∈
Rnu
=
[δVSGa δVSGb δVBa δVBb]T denotes the control input vector,
and d ∈Rnd = [PCP L PP P L]T represents the disturbances
of the system. In this paper, localized and centralized δV
will be used to offer different approaches to the power
sharing. In the first case study, centralized δV will be used
with u ∈R, which guarantees power sharing based on the
droop gains. In the second case study localized δV with
u ∈Rnu to ensure economic dispatch.
III. NONLINEAR MODEL PREDICTIVE CONTROL
FRAMEWORK
MPC is comprised of four components: 1) a prediction
model, 2) a set of constraints, 3) a cost function, and 4)
an optimization algorithm [9]. In this work, the prediction
model utilizes the discretized state-space model in (2) over
the prediction horizon (Np), expressed as follows:
x(k + j + 1) = f(x(k + j), u(k + j), d(k + j))
∀j ∈{0, . . . , Np −1}
(3)
TABLE I
MVDC SHIPBOARD MICROGRIDS PARAMETERS
Parameter
Qty
Parameter
Qty
RSCi
0.05 Ω
LSGi
0.001 H
RSGa
0.05 Ω
LBi
0.0008 H
RSGb
0.1 Ω
LSCi
0.0004 H
RBa
0.225 Ω
CSCa
5 F
RBb
0.45 Ω
CSCb
10 F
Ceq
0.01 F
NMPC simulation setup
Tf
20 s
V SP
6000 V
ts
0.05 s
Q
1
Np
10
R
0.001
CS-II: Cost-effective weight
ψSGi
0.002
ψBi
0.005
ψSCi
0.005
where k = k0 →T −1 represents the duration of the
simulation time from the initial (k0) to the final simulation
time (T), j is the sampling time-step over Np. Note that in this
paper, the prediction model fully utilizes the nonlinearity of
the MGs in (1) to allow the controller to predict the system’s
future behavior accurately.
Furthermore, a set of constraints is explicitly added to ac-
count for the operable range of the bus voltage, currents of the
energy sources, and the auxiliary voltage restoration signals
assigned as the control inputs. Assuming full observability
(y = x), the objective function is derived based on optimal
control formulation over a finite horizon integrated with the
cost-effective objective of the MVDC shipboard MGs. The
optimization algorithm, incorporating the above-mentioned
three components, is utilized to yield a sequence of optimal
control actions over the prediction horizon, summarized as
follows:
min
Uk,XkJ(k) :=
Np−1
X
j=0
∥x(k + j) −xref(k + j)∥2
Qj
+ ∥∆u(k + j)∥2
Rj + ∥x(k + j)∥2
Ψj
(4a)
s.t.
x(k + j + 1) = f(x(k + j), u(k + j), d(k + j))
j = 0, 1, . . . , Np −1
(4b)
u(k + j) ∈U,
j = 0, 1, . . . , Np −1
(4c)
x(k + j) ∈X,
j = 1, 2, . . . , Np −1
(4d)
˜x0 = xplant(t0)
(4e)
where Np ∈N+ is the prediction horizon, k := kts ∈R+ is
the current time step at sampling time ts, Q ≻0, Ψ ≻0,
and R ≻0 are the penalty weights for the states and the rate
control inputs, respectively. Also, ∆u(k) ∈Rnu denotes the
input’s rate of change vector at time step t, xref ∈Rnx is
the vector of desired set-points, and (4b) is the discretized
prediction model. The first term of the objective function
in (4a) ensures the setpoint tracking such that the bus voltage
remains at a constant level, while the second term limits the
step changes of the restoration signals. Given that the voltage
variation is restricted to within ±4% with Ii ≈Pi, the cost
associated with using the DGUs (ψ ∈Rn) is added as the


---

Page 4

---

Fig. 3.
Load profile of the MVDC shipboard MGs with onboard pulsed
power loads (PPL) and constant power loads (CPL).
0
5
10
15
20
0.5
1
1.5
2
107
3.95
4
4.05 4.1
1
1.5
2
107
Fig. 4.
Power balance of the MVDC shipboard MGs under primary control
and δV c-NMPC integration.
third term in (4a), thereby, achieving economic dispatch. Note
that the third term is only applied to the second case study.
Table I detailed the control setup for utilizing NMPC. An
overview of NMPC implementation in this work can be found
in Algorithm 1.
IV. CASE STUDIES
The nonlinear optimization problem in (4) is solved in
MATLAB using “fmincon” nonlinear solver with a solution
method specified to sequential quadratic programming (SQP).
The models are carried out on an Intel Core CPU i7-6700
processor at 3.40 GHz and 32GB RAM. Two case studies
are performed in this paper to verify the effectiveness of the
proposed nonlinear MPC algorithm for the MVDC navy
Algorithm 1 Economic Nonlinear MPC(NMPC)
1: Input Parameters: Np, Q, R, Ψ, Tf, nx, nu
2: Input Data: xref, f(x(t), u(t), d(t))
3: Initialize x0 ∈Rnx, u0 ∈Rnu, d0 ∈Rnd, k = 0
4: for k = 0 →Tf −1 do
▷Simulation time
5:
for j = 0 to Np −1 do
6:
Define & Discretize state-space model, (2)
7:
Construct prediction model, (3)
8:
Formulate J(x(k + j), u(k + j)), (4a)
9:
end for
10:
Solve J(k + j) s.t. (4b)-(4d)
11:
Extract [u∗(0|k), . . . , u∗(Np −1|k)].
12:
Apply only u∗(0|k)
▷RHC
13:
Measure x(k + 1|k) from (1)
14:
Update for k+1, x0 = x(k+1|k) and u0 = u∗(0|k)
15: end for
0
5
10
15
20
5800
6000
6200
0
5
10
15
20
0
50
100
150
12
12.05
12.1
5900
6000
12
12.2
12.4
50
100
150
Fig. 5.
CS-I: Output voltage of the MVDC shipboard MG when using
only primary control versus nonlinear MPC.
Fig. 6.
CS-II: Output voltage of the MVDC shipboard MG via economic
NMPC.
shipboard MGs. The main objective is to maintain the
nominal voltage of the MVDC bus and confirm the load-
power generation balance. A trade-off between power sharing
at a component level and power allocation based on cost-
effectiveness is provided in the first and second case studies,
respectively. Mean absolute percentage error (MAPE) is used
to quantify the performance, as follows:
MAPE = 1
n
n
X
i=1

xi −ˆxi
xi
 × 100%
(5)
where, n represents the total number of samples, xi represents
the desired value, and ˆxi represents the predicted value.
A consistent pattern of the load profile is utilized in all
case studies, as illustrated in Fig. 3.
A. Case study 1 (CS-I): NMPC with centralized auxiliary
voltage restoration signal (δV c)
In this case study, a classical NMPC formulation is
employed, prioritizing control objectives related to voltage
stability and stable output power with proper load sharing.
To validate the efficacy of the integrated centralized voltage
restoration signal using NMPC, herein referred to as δV c-
NMPC, its performance is collocated with a conventional


---

Page 5

---

0
5
10
15
20
-5
0
5
10
106
0
5
10
15
20
-5
0
5
106
0
5
10
15
20
-5
0
5
106
0
5
10
15
20
-5
0
5
106
Fig. 7.
Output power comparison of the distributed generation units in MVDC shipboard MGs.
droop-controlled power management system from the primary
layer, herein referred to as the primary control. Fig. 4 shows
the aggregate power generated from the DGUs against the
total power demand for both control configurations (P P RI
Gen
represents primary control via virtual droop control and
P NMP C
Gen
designates δV -NMPC). It is observed that both
controllers consistently converge to the load trajectory, thereby
ensuring adherence to the demand.
Fig. 5(a) shows the voltage trajectory over the 20s simula-
tion with both controllers. As expected, solely using virtual
droop control is not sufficient to restore the voltage of the
MVDC bus to the nominal value with MAPE at 1.67%. This
is due to the presence of voltage-sensitive loads, PPL, which
required the system to withdraw the currents excessively. As
a result continuous voltage drop is observed. On the contrary,
δV c-NMPC outperforms the primary control with voltage
consistently reaching the reference point at 6kV with MAPE
at 0.02%. A transient state of the voltage trajectory is also
observed during the sudden changes in the loads. In the
proposed method, the excessive withdrawal of the currents is
managed by the bounded auxiliary voltage signal, exhibited
in Fig. 5(b), ensuring voltage stabilization to the nominal
value.
In Fig. 7, the power generation trajectories of the DGUs
under both primary control and δV c-NMPC integration are
exhibited. In the presence of time-varying PPL, δV c-NMPC
managed to stabilize the power output of each DGU four times
faster than the primary control, confirming the robustness of
the proposed controller. Furthermore, the incorporation of
capacitive droop gains into the dynamics of the SCs played a
significant role in the power output, where they consistently
adapt to transient load conditions. Under the δV c-NMPC
configuration, SCs are rapidly adjusted to 0MW during steady
state conditions within 0.5s, whereas the primary control
requires a 2s longer time frame to reach a similar condition.
Fig. 8 shows the power sharing between the DGUs of
the MVDC navy MG. During steady state conditions, the
output power of SGa and BESSa approximately doubled
that of SGb and BESSb. This is because the droop gains
(see Table I) are reversely proportional to the steady state
power [14].
B. Case study 2 (CS-II): Economic NMPC with localized
auxiliary voltage restoration signals (δV l
i )
In this case study, the proposed economic NMPC (ENMPC)
is utilized to also factor in the cost-effectiveness of the power
allocation in the MVDC navy MG. The final optimization
problem formulation is detailed in (4). In addition, localized
auxiliary voltage restoration signals (δVi) for the i-th DG
are employed to regulate the loss at the component level.
Given the power balance constraint embedded in the system’s
dynamics, the total power generated by the MGs consistently
complies with the total load (figure not shown for brevity)
with a similar trajectory as shown in CS-I. During sudden
load fluctuations, the system experiences noticeable voltage
drops and surges as illustrated in Fig 6. However, the
proposed controller maintained a voltage stability of less
than 0.5s. The addition of δVi to the system’s dynamics is
used to compensate for the virtual impedance (δVi ≈RiIi)
such that constant MVDC bus voltage can be obtained.
In both case studies, it is visualized that δV fulfilled the
objective. Furthermore, leveraging the MPC framework that
can explicitly take into account constraints on the system’s
variables, here, δVi for each DGU is bounded to 150V to
be consistent with the boundary in CS-I. As observed in
Fig 6 (b), optimal control actions are achieved that satisfy
the constraints, secure power balance, and restore the bus
voltage.
Fig. 9 shows the load sharing among the DGUs. Generally,
the order of the output power is consistent with CS-I
during steady state conditions (see Fig. 8), where PSGa
contributes the highest power while PBb is the lowest and
PSCi only utilized during transient conditions. However, the
ratio between the DGUs differs, closely reaching 1:1. Given
the economic objectives in (4a), this result is anticipated.
When the objectives of the composite optimization conflict
with one another, a compromised solution is generated in
which no improvement can be made without deteriorating at
least one other solution [9]. Furthermore, 15% cost savings
are obtained in this case study when compared to CS-I with
cost coefficients adopted from [15], [16].


---

Page 6

---

0
2
4
6
8
10
12
14
16
18
20
-4
-2
0
2
4
6
8
106
12
12.05
12.1
0
4
8
106
Fig. 8.
CS-I: Power sharing with δC-NMPC.
0
2
4
6
8
10
12
14
16
18
20
-4
-2
0
2
4
6
8
106
12
12.05
12.1
0
4
8
106
Fig. 9.
CS-II: Power sharing with δl-ENMPC.
V. CONCLUSIONS
This paper proposes a novel approach for voltage control
and power sharing among hybrid storage and conventional
generation units in MVDC navy shipboard microgrids by
leveraging a nonlinear model predictive control framework.
The results demonstrate that both approaches constantly
maintain the bus voltage at a steady level with a tracking
error of 0.02%, in spite of the varying, voltage-sensitive,
and high load requirement. The controller adeptly stabilizes
the generated power within 0.5s during abrupt changes
in the load. These results confirm the robustness of the
controller. Furthermore, demand compliance is effectively
achieved across the DGUs with SGs and BESSs catering to
the constant power loads (PCP L), while SCs adeptly supply
the demands from the pulsed power loads (PP P L). Moreover,
the integration of the MVDC navy shipboard MGs with
NMPC as the controller allows a flexible tuning mechanism
for power allocation. Droop-control-based power sharing is
achieved when utilizing centralized-δV . In contrast, localized-
δVi prioritizes economic power generation with 15% cost
savings. Future work will develop a fast and guaranteed
stability trajectory of the MVDC MGs for naval vessels. The
algorithm will leverage the Lyapunov stability theorem and
input parameterization under different layers of hierarchical
control in MGs.
ACKNOWLEDGMENT
The authors would like to acknowledge the Department
of Defense, Office of Naval Research for supporting this
research.
REFERENCES
[1] M. Cupelli, S. K. Bhanderi, S. K. Gurumurthy, and A. Monti, “Voltage
control for buck converter based mvdc microgrids with interconnection
and damping assignment passivity based control,” in 2018 19th IEEE
Mediterranean Electrotechnical Conference (MELECON). IEEE, 2018,
pp. 14–19.
[2] S. Faddel, A. A. Saad, M. El Hariri, and O. A. Mohammed, “Coordi-
nation of hybrid energy storage for ship power systems with pulsed
loads,” IEEE Transactions on Industry Applications, vol. 56, no. 2, pp.
1136–1145, 2019.
[3] X. Chen, J. Zhou, M. Shi, L. Yan, W. Zuo, and J. Wen, “A novel
virtual resistor and capacitor droop control for hess in medium-voltage
dc system,” IEEE Transactions on Power Systems, vol. 34, no. 4, pp.
2518–2527, 2019.
[4] I. S. Association et al., “Ieee recommended practice for 1 kv to
35 kv medium-voltage dc power systems on ships,” IEEE Industry
Applications Society: New York, NY, USA, 2010.
[5] J. Young, M. A. Cook, D. G. Wilson, and W. Weaver, “Model predictive
control for the operation of a hybrid mvac and mvdc electric warship,”
in 2023 IEEE Electric Ship Technologies Symposium (ESTS).
IEEE,
2023, pp. 317–326.
[6] J. Khazaei, “Optimal flow of mvdc shipboard microgrids with hybrid
storage enhanced with capacitive and resistive droop controllers,” IEEE
Transactions on Power Systems, vol. 36, no. 4, pp. 3728–3739, 2021.
[7] T.-T. Nguyen, B. L.-H. Nguyen, and T. Vu, “Energy management
system for resilience-oriented operation of ship power systems,” arXiv
preprint arXiv:2110.10053, 2021.
[8] D. Bosich, G. Giadrossi, and G. Sulligoi, “Voltage control solutions
to face the cpl instability in mvdc shipboard power systems,” in 2014
AEIT Annual Conference-From Research to Industry: The Need for a
More Effective Technology Transfer (AEIT).
IEEE, 2014, pp. 1–6.
[9] C. Bordons, F. Garcia-Torres, and M. A. Ridao, Model Predictive
Control of Microgrids, ser. Advances in Industrial Control.
Cham:
Springer International Publishing, 2020.
[10] J. M. Maciejowski, Predictive Control with Constraints.
Prentice Hall,
2002.
[11] N. Zohrabi, S. Abdelwahed, and J. Shi, “Reconfiguration of mvdc
shipboard power systems: A model predictive control approach,” in
2017 IEEE Electric Ship Technologies Symposium (ESTS).
IEEE,
2017, pp. 253–258.
[12] T. Van Vu, D. Gonsoulin, F. Diaz, C. S. Edrington, and T. El-Mezyani,
“Predictive control for energy management in ship power systems under
high-power ramp rate loads,” IEEE Transactions on Energy Conversion,
vol. 32, no. 2, pp. 788–797, 2017.
[13] G. Sulligoi, D. Bosich, G. Giadrossi, L. Zhu, M. Cupelli, and A. Monti,
“Multiconverter medium voltage dc power systems on ships: Constant-
power loads instability solution using linearization via state feedback
control,” IEEE Transactions on Smart Grid, vol. 5, no. 5, pp. 2543–
2552, 2014.
[14] A. Hosseinipour and J. Khazaei, “A multifunctional complex droop
control scheme for dynamic power management in hybrid dc micro-
grids,” International Journal of Electrical Power & Energy Systems,
vol. 152, p. 109224, 2023.
[15] P. K. S. Roy, H. B. Karayaka, J. He, and Y.-H. Yu, “Economic
comparison between battery and supercapacitor for hourly dispatching
wave energy converter power,” in 2020 52nd North American power
symposium (NAPS).
IEEE, 2021, pp. 1–6.
[16] U. EIA, “Levelized cost of new generation resources in the annual
energy outlook 2022,” Washington DC: US Energy Information
Administration, 2022.
