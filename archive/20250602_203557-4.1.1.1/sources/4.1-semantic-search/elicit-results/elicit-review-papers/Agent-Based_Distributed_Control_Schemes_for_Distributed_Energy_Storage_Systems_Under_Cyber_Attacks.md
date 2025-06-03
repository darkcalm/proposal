

---

Page 1

---

1
Vulnerability Assessment of Load Frequency
Control Considering Cyber Security
Chunyu Chen, Yang Chen, Kaifeng Zhang, Wenjun Bi, Meng Tian
Abstract—Security is one of the biggest concern in power
system operation. Recently, the emerging cyber security threats to
operational functions of power systems arouse high public atten-
tion, and cybersecurity vulnerability thus become an emerging
topic to evaluate compromised operational performance under
cyber attack. In this paper, vulnerability of cyber security of load
frequency control (LFC) system, which is the key component in
energy manage system (EMS), is assessed by exploiting the system
response to attacks on LFC variables/parameters. Two types of
attacks: 1) injection attack and 2) scale attack are considered
for evaluation. Two evaluation criteria reﬂecting the damage on
system stability and power generation are used to quantify system
loss under cyber attacks. Through a sensitivity-based method and
attack tree models, the vulnerability of different LFC components
is ranked. In addition, a post-intrusion cyber attack detection
scheme is proposed. Classiﬁcation-based schemes using typical
classiﬁcation algorithms are studied and compared to identify
different attack scenarios.
Index Terms—Load frequency control, cyber attack, attack
tree, classiﬁcation, attack detection.
A. Nomenclature
1) Abbreviations:
LFC
load frequency control.
MLP
multi-perceptron .
NN
neural network.
SVM
support vector machine.
ACE
area control error.
DFT
discrete fourier transform.
LSTM
long short term memory.
CI
computational intelligence.
2) Variables:
f0
nominal frequency.
fij
frequency of Generator j in Area i.
fi
frequency of Area i.
∆fi
frequency deviation of Area i.
comij
LFC command dispatched to Generator j in
Area i.
comi
total LFC command in Area i.
αij
allocation coefﬁcient of Generator j in Area i.
∆f j
i
frequency deviation of Area j interconnected
with Area i.
βij
bias coefﬁcient of Area j interconnected with
Area i.
P ij
tie,0
nominal tie-line power between Area s and i.
Chunyu Chen is with China University of Mining and Technology (email:
chunyuchen@cumt.edu.cn); Yang Chen is with Nanyang Technological Uni-
versity (email: fedora.cy@gmail.com), Yang Chen is the corresponding author;
Kaifeng Zhang and Wenjun Bi are with Southeast University, Meng Tian is
with Wuhan University
P ij
tie
tie-line power between Area j and i.
∆P ij
tie
tie-line power deviation between Area j and i.
I. INTRODUCTION
With the advent of industrial informatization in modern
industrialized societies, cyber security arouses extensive at-
tention, and becomes an emerging issue in performance
evaluation of critical infrastructure, Load frequency control
(LFC) serves a crucial role in system frequency stabilization,
and is greatly dependent on information systems. Hence, by
considering the possibility of cyber intrusion, vulnerability of
cyber security of LFC should be assessed to better reﬂect
its safety status under compromised conditions, which offers
valuable information for subsequent security upgrading and
reinforcement.
Diverse research studies were conducted for LFC by focus-
ing on two aspects: 1) attack strategy [1]–[3] and 2) defense
strategy [4], [5]. Some researchers also consider the interaction
between the attacker and defender by studying these two
aspects together [6].
In this paper, instead of purely analyzing the strategy
and its efﬁcacy to deteriorate (improve) LFC performance,
vulnerability of cyber security of LFC system is systematically
assessed. To the best of the knowledge of the authors, this
speciﬁc problem has not been investigated before. Actually,
the vulnerability research on other operational functions in
EMS has already been conducted [7]–[12]. Ten [7] used attack
trees to evaluate the cyber security of supervisory control
and data acquisition (SCADA) systems, and vulnerabilities
were further evaluated from system, scenarios and access
points [8]. Vulnerability of state estimation under false data
injection attack was analyzed in [11]. Protection systems were
considered when evaluating cyber security by simulating the
physical response of power systems to malicious attacks [12].
In order to construct the assessment system, operational
mechanism under cyber intrusion must be explicitly under-
stood at ﬁrst. For example, assessment for protection system
oriented attacks requires clear understanding of the response
of protection mechanism under attack [12]. Assessment for
power state estimation oriented attacks requires the knowledge
of how the estimated state is falsiﬁed [11]. Apart from
the mechanism, the objectives of speciﬁc function, which
determine the assessment targets, should also be considered.
As for LFC, the objective is to balance the active power
of the control area; hence, the degree of intentional power
imbalance caused by cyber intrusion should be incorporated
into vulnerability assessment. Based on the assessment targets,
arXiv:2003.05661v1  [eess.SY]  12 Mar 2020


---

Page 2

---

2
evaluation criteria can ﬁnally be used realize quantiﬁcation of
vulnerability to cyber intrusions.
According to the abovementioned description of prerequi-
sites for assessment system construction, LFC’s operational
mechanism is analyzed by considering system response when
the attack occurs on different variables (parameters) of LFC
system. The most directly relevant indices associated with
LFC, i.e., frequency and tie-line power deviation, are selected
as evaluation criteria. In addition, generation disruption perfor-
mance is also assessed. To this end, we analyze vulnerability
by simulating intrusions into different LFC components (both
from analytic and numerical analyses). Then, sensitivity-based
method is adopted to quantify the vulnerability, based on
which the attack tree model is used to construct the ﬁnal
vulnerability assessment system.
Vulnerability assessment can’t mitigate the security risks
but reﬂects the security situation of LFC system and provide
apriori guidance on allocation of defense resource. Therefore,
post-intrusion detection strategies are investigated as remedial
countermeasures, which could promptly indicate whether or
not the attack occurs, and then the defender would use the
detection information to take appropriate defensive measures.
Attack detection is itself an emerging trend on cyber phys-
ical system (CPS) safety and privacy. Recent advancement
in computational intelligence (CI) increases its compatibility
for discerning even the slightest difference, which is the
foundation of detection realization [13]–[15]. Unlike natural
intelligence (possessed by humans), CI is capable of analyzing
complex detection (identiﬁcation) problem with high accuracy.
Moreover, it avoids the burdensome mathematical modelling
and analytic reasoning, and is much more user-friendly. When
considering the multidiversity of intrusion and the complexity
of detection task, it is inevitable to adopt CI techniques in
cyber intrusion detection.
In this paper, classiﬁcation-based detectors are studied by
considering typical CI-based classiﬁcation algorithm. Speciﬁ-
cally, multilayer perceptron (MLP), Bayesian network and sup-
port vector machine (SVM) are adopted. In order to reduce the
computational (structural) complexity and high dependency on
massive data, a simple yet effective dimensionality reduction
method using fourier transform is applied to extract low-
dimensional detection-related features.
The main contribution includes:
1) Vulnerability assessment for cyber security of LFC is for
the ﬁrst time considered. LFC performance degradation-
based criteria are used to evaluate the inﬂuence of attacks.
Attack tree models are then established to rank the
criticality of different attack scenarios, thus laying the
groundwork for subsequent protective resource allocation.
2) A post-intrusion detection scheme is presented with
the aid of classiﬁcation algorithms. Time-to-frequency-
domain transform is applied to extract relevant features
for detection, thus reducing computational complexity
and enhancing detection efﬁciency.
The remaining of the paper is as follows: Section II
presents basic backgrounds of cyber attack on LFC system;
the inﬂuence from compromising different LFC components is
systematically studied in Section III. Vulnerability assessment
is performed in Section IV. The two-stage defense paradigm is
discussed in Section V. Case studies are performed in Section
VI.
II. BASICS OF CYBER ATTACK ON LOAD FREQUENCY
CONTROL
Consider Area i which contains m generators and is inter-
connected with other k areas, the diagram of cyber attacks on
load frequency control (LFC) of Area i is as shown in Fig.
1, where fij 1 ≤j ≤m is the frequency measurement of
LFC 
controller
Gim
Gi2
Gi1
Power grid
Area i1
Level 1
Level 2
Level 3
Area i
Area ik
Fig. 1. Diagram of load frequency control
generator j in Area i; P is
tie 1 ≤s ≤k is the interchange
power of tie-line s; comij 1 ≤j ≤m is the LFC command
dispatched to the generator j. Apart from the bottom-level
LFC participating generators, the LFC control system can be
categorized into three levels(in Fig. 1): Level 1(measurement
upload), Level 2(LFC command generation), Level 3 (LFC
order dispatch).
A. Area Control Error (ACE) Control Equation
Before introducing the types of cyber attacks on LFC, ACE
control equations, which will be frequently used in studying
system response (under attack) in Section III, are given as:
ACEi = Pk
s=1 ∆P is
tie + βi∆fi
ACEi1 = −∆P i1
tie + βi1∆f 1
i
...
ACEik = −∆P ik
tie + βik∆f k
i
(1)
where ACEis 1 ≤s ≤k is ACE of Area s; ∆f s
i is the
frequency deviation of Area s; βis is the bias coefﬁcient of
Area s. The goal of LFC can be represented by:
lim
t→∞∆fi (t) →0
lim
t→∞∆P is
tie (t) →0
(2)


---

Page 3

---

3
B. Types of Cyber Attacks on Load Frequency Control
There exist various types of cyber attacks ranging from
wiretapping oriented (e.g., spooﬁng attack) to security com-
promise oriented (e.g., integrity attack). In this paper the
latter is considered. In respect to LFC, breach of integrity is
characterized by parameter/variable falsiﬁcation. Manipulation
schemes of variable falsiﬁcation are particularly divided as two
categories:
• Scale attack: Hackers add a gain before the true mea-
surements:
xa = kxt
(3)
where xa is the falsiﬁed measurements; k is the gain
(k = 1 represents the real measurement); xt is the true
measurement.
• Injection attack: Hackers inject external disturbance
signals to distort the original measurements:
xa = xt + d
(4)
III. INFLUENCE OF CYBER ATTACK ON THREE LEVELS OF
LOAD FREQUENCY CONTROL
Based upon the background introduction in Section II,the
inﬂuence of cyber attack (as is described in Section II-B) on
speciﬁc LFC components is detailed by studying the quasi-
steady-state response of system frequency. LFC components
are categorized into three classes based on which level (in Fig.
1) they belong to. As are shown in Fig. 2, the components in
Level 1 can be easily identiﬁed as the frequency (tie-line power
measurement) fis (P is
tie); the components in Level 3 are LFC
order comis. The components in Level 2 contain intermediate
Information 
system
Physical grid
legend
RTU/PLC
unit
Ethernet
router/switch
data upload channel(Level 1)
order dispatch channel(Level 3)
tie-line
other trasmission line
server
PC
order generation channel(Level 2)
isf
is
tie
P
is
com
firewall
Fig. 2. Diagram of load frequency control
variables/parameters during LFC order generation, which are
shown in the red dashed box in Fig. 3 In the remaining
of this section, the quasi-steady-state response is studied by
considering the attack template in (3) and (4).
A. Cyber Attack on Level 1 components
1) fis oriented attack analysis: It can be learned that no
matter the attacker adopts adopts (3) or (4) to attack frequency
measurement of Generator s, there is a difference between the
falsiﬁed center of inertia frequency fia (perceived by Level 2)
PI
tie
P
D
+
1i
a
im
a
2
i
a
1i
com
2
i
com
im
com
1if
2
if
im
f
+
0f
-
+
if
+
1i
tie
P
1
,0
i
tie
P
+
+
ik
tie
P
,0
ik
tie
P
+
-
-
+
1i
tie
P
D
ik
tie
P
D
if
D
ib
m
å
Fig. 3. Structure of LFC controller
and the real fi, which ultimately causes the miscalculation of
the output feedback signal ACE:
ACEif = ACEi + ei
(5)
where ACEif
is the falsiﬁed ACE; ACEi is the real
ACE, ei= βiHis (k −1) fi
.P
j Hij for scale attack and
ei= βiHisd
.P
j Hij for inject attack.
It follows that ACEif achieves asymptotical stability;
ACEi + ei = 0. It means that lim
t→∞∆fi (t) →ei/P
k βik.
The power deviation of the sth tie-line interconnected with i
lim
t→∞∆P is
tie (t) →−βisei/P
k βik
2) P is
tie oriented attack analysis: Firstly, assume that the
attacker adopts (3) to attack tie-line s, i.e., P is
tie = kP is
tie. It
follows that the falsiﬁed interchange power deviation received
by Area i is ∆P is
tie = kP is
tie −P is
tie,0. However, this deviation
is offset by −∆P is
tie = −(kP is
tie −P is
tie,0), which is received
by Area s. The quasi-steady-state response is not inﬂuenced.
Similar conclusions can be made when the attacker adopts (4).
B. Cyber Attack on Level 2 Components
As can be seen from Fig. 3, the main LFC components
include fi, f0, ∆fi, βi, P ij
tie,0, ∆P ij
tie, ∆P i
tie and αij; hence,
in the remaining of this section, quasi-steady-state-response
considering attack on these components is systematically an-
alyzed.
1) cyber attack on frequency-related components: In this
case, the attack occurs on fi, f0, ∆fi. Firstly, it can be
learned attack on fi and f0 will produce the opposite re-
sponse. For brevity, only fi is considered; using (3) would
lead to
lim
t→∞∆fi (t)
→
βid/P
k βik,
lim
t→∞∆P is
tie (t)
→
−βisβid/P
k βik.
As for ∆fi, it can be proved that system frequency and
tie-line power still converge to nominal values unless k in (3)
satisﬁes
βik + βi1 + · · · + βik = 0
(6)
Using (4) would lead to ∆fi →βid/P
k βik (∆P is
tie →
−βisβid/P
k βik)
As with cyber attack in Section 1, the variables/parameters
under the threat of attack are f0 and P is
tie,0.
Parameter
modiﬁcation
of
f0
(using
(4))
will
lead
to
lim
t→∞∆fi (t)
→
−βid/P
k βik,
lim
t→∞∆P is
tie (t)
→


---

Page 4

---

4
βisβid/P
k βik. Manipulation of P is
tie,0 using (4) will lead to
lim
t→∞∆fi (t) →−d/P
k βik, lim
t→∞∆P is
tie (t) →βisd/P
k βik.
2) cyber attack on tie-line power-related components: In
this case, the attack occurs on P ij
tie,0, ∆P ij
tie, ∆P i
tie. Firstly,
manipulation of P is
tie,0 using (4) will lead to lim
t→∞∆fi (t) →
−d/P
k βik, lim
t→∞∆P is
tie (t) →βisd/P
k βik. As for scale
attack on ∆P is
tie, it can be proved that system frequency and
tie-line power still converge to nominal values unless k in (3)
satisﬁes
βis(k −1) + βi + βi1 + · · · + βik = 0
(7)
Similarly, in scale attack on ∆P i
tie k in (3) should satisfy
βi/k + βi1 + βi2 · · · + βik = 0
(8)
otherwise, system frequency and tie-line power still converge
to nominal values.
C. Cyber Attack on Level 3
In this scenario, comij 1 ≤j ≤m are under threat.When
the total LFC order comi is generated through PI controller,
each LFC participating generator j receives power adjust-
ment command with comij = αijcomi. When the attacker
changes αij to αij,f, which means the falsiﬁed command is
comij,f = αij,fcomi. In this case, only the reference power
adjustment ui is substituted by the sum of the real ui and the
error ue: uif = ui + ue, and asymptotical stability of ACEi
still holds. Moreover, since the output feedback signal is not
compromised, the long-term stability is not disturbed. This
extra command ∆comij = comij,f −comij can be regarded
as the feedforward compensation signal, and the steady-state
uif remains the same as ui. The only differences between ui
and uif are transient dynamics in inception phase.
Attack 
Destabilize LFC 
system
Attack 
Level 1
Attack 
Level 2
Attack 
Level 3
Attack 
isf
is
tie
P
Attack 
ij
com
Attack 
,0
is
tie
P
Attack 
0f
Attack 
if
Attack 
if
D
Attack 
is
tie
P
D
Attack 
i
tie
P
D
Attack 
ij
a
Fig. 4. Attack tree of LFC control system
IV. VULNERABILITY ASSESSMENT OF CYBER SECURITY
OF LOAD FREQUENCY CONTROL
In Section III, integrity attacks on different components of
LFC control system are analyzed with respect to the inﬂuence
on LFC performance. In this section, the inﬂuence is further
quantiﬁed and ranked to better understand the criticality of
different attack scenarios.
A. Inﬂuence on Load Frequency Control Performance
Based upon Section III, the overall laws of attack inﬂuence
on LFC through compromising different components are sum-
marized as follows:
• P is
tie oriented attacks on Level 1, βi oriented attacks on
Level 2 and comij oriented attacks on Level 3 and can
guarantee (2) holds.
• Scale attack (3) on ∆fi, ∆P is
tie and ∆P i
tie has no inﬂu-
ence on quasi-steady-state response, unless (6), (7) and
(8) hold. Inject attack on ∆fi, ∆P is
tie or ∆P i
tie would
cause unexpected deviations.
• Manipulation of fij, f0, fi, P is
tie and P is
tie,0 would cause
unexpected deviations.
In order to quantify the inﬂuence, i.e., assign the value of the
leaf nodes in Fig. 4, the sensitivity-based method is adopted:
ci = βi |∆fi| + Pk
i=1
∆P ik
tie

di
(9)
where di represents the integrity attack on variable/parameter
i in LFC; ci represents the deviation criterion under di.
B. Inﬂuence on Generation of LFC-Participating Units
As for attacks which can cause deviations of frequency
and tie-line power, e.g., fij and f0 oriented attacks, by
manipulation of variables/parameters in LFC, ACE is falsiﬁed
into :
ACEif = ACEi + erri
(10)
where erri is the miscalculation due to cyber attacks, e.g.,
erri can be ei in (5). When erri > 0, the real ACE satisﬁes
ACEi < 0, which means the LFC generating units decrease
generation ui < 0, vice versa. When considering the normal
load variation ∆pdi, the real ACEi can be represented by:
ACEi = ACEpi −erri
(11)
where erri is the same as that in (10). ACEpi is the
area control area induced by the real load variation ∆pdi
(ACEpi = −∆pdi when ignoring transmission loss). If ACEi
in (11) satisﬁes ACEi < 0, then ui < 0, vice versa.
As for attacks which have no inﬂuence on long-term stabil-
ity, e.g., scale attack on ∆fi, suppose that load variation ∆pdi
occurs after the attack, which induces a frequency drop ∆fi.
The falsiﬁed βif∆fi will cause misadjustment of generation.
Nevertheless, ui in the steady-state remains the same as before.
Similarly, it can be proved that falsiﬁcation of comij leads to
the same ui in the steady state.
By replacing the attack goal in Fig. 4 by generation disrup-
tion, a similar attack tree can be constructed. Denote value of
leaf nodes by generation disruption per unit falsiﬁcation:
ci = |∆ui|
di
(12)
quantiﬁcation of inﬂuence on generation by attacking different
variables/parameters can be achieved.
Theorem 1. ci with respect to the same leaf node in two
attack trees are equal when neglecting the transmission loss
and load variation induced by the attack .


---

Page 5

---

5
Proof. Suppose under speciﬁc integrity attack di, the error
of ACE induced is ei. Then, the steady-state generation
disruption ui is ∆ui = −ei when neglecting the transmission
loss and load variation induced, |∆ui| = |ei|. On the other
hand, frequency-tie-line-power deviation can be written by:
βi |∆fi| + Pk
i=1
∆P ik
tie

= βi
 ei
P β
 + Pk
i=1
 βikei
P β

= |ei|

βi
P β + Pk
i=1
βik
P β

= |ei| = |∆ui|
Based on Theorem 1, it is learned that the two vulnerability
indices, disruption of LFC performance and generation, have
the same scores in respect to certain integrity attacks in Section
III, which means that performance and generation disruption
have a strong positive correlation. And the two indices are
interchangeable when assessing vulnerability of LFC.
V. MITIGATION FOR VULNERABILITY OF CYBER
SECURITY OF LOAD FREQUENCY CONTROL
Mitigation for vulnerability can be summarized as two
stages of defense. Stage 1 is the prevention stage where the
operator tries to prevent the attacker from inﬁltrating into
the system; stage 2 is the detection stage where the operator
should single out the compromised signal once the system is
inﬁltrated, which lays the foundation for mitigation through
system reconﬁguration.
With the aid of the designed attack tree model in Section IV,
preventive resource can be allocated based on the criticality of
each attack scenario (indicated by the leaf node in the attack
tree). Preventive resource is used to invalidate potential attacks
before they ever inﬁltrate the system. For example, the oper-
ator can set up multiple sensors for the same variable based
upon the presumption that the attacker cannot compromise all
of them, which is also known as measurement redundancy
method.
Attack detection and identiﬁcation is capable of discerning
attack activity when preventive measures fail to resist it, which
is essential to grasping behavioral pattern of the attacker be-
sides information provision for subsequent mitigatory measure
design. Tough statistical methods can effectively solve the
differentiation problem among normal load variation and cyber
attack scenarios [4], [6], the type of attack scenarios cannot be
identiﬁed. As for cyber attack on LFC studied in this paper,
the type represents the category of the attack signal. In order
to identify to which category a new observation of a scenario
belongs, classiﬁcation-based method is adopted to solve this
typical multi-class anomaly detection techniques.
Classiﬁcation-based techniques operate in a two-phase fash-
ion, where the training phase learns a classiﬁer using labelled
training data and the test phase identiﬁes to which class a
test instance belongs to by using the trained classiﬁer. Apart
from the classiﬁcation algorithm (e.g., neural networks (NNs)-
based and Bayesian networks-based ones), the key element
of determining the classiﬁer quality is input data, which
determines the upper limit of learning algorithm.
A. Input Data for Classiﬁer
Instead of relying on static responses (quasi-steady-state
response) for data generation, the input data should be tightly
connected with the LFC dynamics, which can generate dy-
namic system response containing abundant information about
properties of scenarios. Hence, dynamic responses of area
control error (ACE), which considers both frequency and tie-
line power variation, are used as the input data. Every ACE
instance is a time series, with the expansion of time length and
increase of sampling rate, the amount of data points grows up.
When considering hundreds even thousands of data instances,
the total amount of data becomes even much greater and big
data forms.
There exists much redundant and classiﬁcation-irrelevant
information in data instances, and feature selection or extrac-
tion should be implemented to obtain relevant features, thus
reducing classiﬁer complexity and enhancing generalization
performance. Though deep learning techniques can self-learn
multi-level representations and features for classiﬁcation, it
usually demands a huge quantity of data, which is impossible
in reality since cyber attacks are a small probability events.
In order to deal with the feature generation with limited
data instances, discrete Fourier transform (DFT) is used to
extract the low-dimensional components (DFT coefﬁcients)
in frequency domain. They preserve obvious differences of
different classes and signiﬁcantly reduce data complexity,
which are quite beneﬁcial to data training (testing) in an
efﬁcient fashion.
ACE responses under normal and compromised conditions
are simulated and the results are shown in Fig. 5. As can be
seen, compared the variation of system frequency responses
(in Fig. 5a), the variation of ACEs (in Fig. 5b) is much
more explicit among different conditions. Furthermore, the
dimension of inputs is signiﬁcantly reduced by implementing
DFT on ACEs without deteriorating the explicit variation (in
Fig. 5c).
B. Classiﬁcation Algorithm
1) Neural Networks: In this paper, the feedforward neural
network multilayer perceptron (MLP) is used for classiﬁcation
[16]. The structure is as shown in Fig. 6.
Mathematically, the goal of MLP classiﬁer is derived from
min E (ω) = 1
2
p
X
i=1
y
 xi, ω

−di2
(13)
where ω represent the weights; E is the error term; is the ith
input data, y is the output of classiﬁer, di is the ith desired
output. Through gradient descent approach, the optimal can
be computed to minimize the prediction errors.
Besides MLP, the autoencoder is adopted for data denos-
ing/dimensionality reduction. Dataset of DFT coefﬁcients is
ﬁrstly fed into the autoencoder [17], [18], the output of which
is then used as the input of MLP classiﬁer. Moreover, in case
of data indistinguishable-ness under normal load variation and
some attack scenarios, a threshold-based module is developed.
The architecture of the whole composite MLP classiﬁer is
shown in Fig. 7. Details of the threshold-based module are


---

Page 6

---

6
0
20
40
60
80
100
time/s
59.98
59.985
59.99
59.995
60
60.005
60.01
frequency/Hz
step attack
random attack
oscillating attack
no attack
(a) frequency under different conditions
0
20
40
60
80
100
time/s
-1
-0.5
0
0.5
1
1.5
ACE/p.u.
step attack
random attack
oscillating attack
no attack
(b) ACE under different conditions
0
0.2
0.4
0.6
0.8
1
sampling rate/p.u.
0
0.05
0.1
0.15
0.2
0.25
0.3
magnitude/p.u.
step attack
random attack
oscillating attack
no attack
(c) spectral components under different
conditions
Fig. 5. LFC system responses under different conditions
input
hidden
output
MLP
Class 1
Class n
DFT coefficient
input data
Fig. 6. Attack tree of LFC control system
x
z
y
Original input
reconstructed input
encoder
decoder
MLP classifier
input
output
threshold-based 
module
ACE 
time-
series
N1
N2
N3
N2
N1
N3
N1
M
autoencoder
DFT
Fig. 7. Schematic diagram of composite NN-based attack
detector
given in Algorithm 1.
2) Support Vector Machine: The goal of support vector
machine classiﬁcation (for muli-classiﬁcation) is to divide
a separable dataset into subsets, it can be deﬁned as an
optimization problem [19]
min
ω,b,ξ
kP
m=1
∥ωm∥2 + C
lP
i=1
P
m̸=yi
ξm
i
s.t.ωT
yiφ (xi) + byi ≥ωT
mφ (xi) + bm + 2 −ξm
i
ξm
i
≥0
(14)
where ξm
i
represents slack variables; ωm represents the
weights; C is the regulation parameter which reﬂects satisfac-
tion degree of the constraints; xi is the input of an instance;
φ is the basis function which mapping to a high dimensional
space for better separability. It constructs two-class rules where
ωT
mφ (xi)+bm separates training instances of class from other
classes.
3) Bayesian Network: Naive Bayesian classiﬁer [20] pre-
dicts that a data instance X belongs to the class with the
highest a posteriori probability conditioned on X, which
means X belongs to class Ci if and only if
P (Ci/X) > P (Cj/X) , 1 ≤j ≤m, j ̸= i
(15)
In order to calculate the maximum, P (Ci/X) should be
calculated ﬁrst, Based on Baye’s theorem, it follows that
P (Ci/X) = P (X/Ci) P (Ci)
P (X)
(16)
where P (X) is equal for all classes; P (Ci) can be computed
by counting the frequency of instance belonging to in all data;
based on the naive assumption of conditional independence of
each attribute (data point in DFT coefﬁcients), one has
P (X/Ci) ≈
n
Y
k=1
P (xk/Ci)
(17)
VI. CASE STUDIES
In this section, Kundur’s 4-unit-13-bus system is used
for vulnerability assessment and subsequent attack scenario
identiﬁcation. The single-line diagram is as shown in Fig. 1.
A. Vulnerability Assessment for Cyber Security of LFC
The system is divided into three control areas where Area 1
is the subject for study. The attack model (leaf node in attack
tree) is constructed by simulating each scenario addressed in
Section. 25 total attack scenarios are generated and numbered.
Descriptions of scenarios corresponding to speciﬁc numbers
are given in Appendix A.
Sensitivity index in (3) and (4) are computed respectively
for each scenario. The results are shown as histograms in Fig.
9 where the number on x axis represents the type of sensitivity,
1 means (9) is used; 2 means (12) is used. the number on y


---

Page 7

---

7
Algorithm 1 Threshold-based detection module in Fig. 7
1: Sample ∆fo (the sampling rate is fs, duration of inspection is Ts, the length of the signals is Ls = Tsfs)
2: Set sliding window width sw1 = l1
3: For i = 1 : Ls −l1 + 1
4: y(i) = ∆fo(i : i + l1 −1)
5: x(i) = exp(var(y(i)))
6: End
7: If x(i) >= ςf
8: Then ∆fo is compromised
9: End
20
2
G2
12
G4
1
10
3
101
4
14
13
110
11
G1
G3
120
Area 1
Area 3
Area 2
Fig. 8. Single line diagram of IEEE 13-bus based tree-area
axis represents the attack scenario index. From Fig.9 it can be
learned that attacks on f0, f1 and ∆f1 (Scenario 9-12) produce
the largest degree of disruption on both LFC performance
(684) and generation (657), followed by f11 (f12) oriented
attacks (Scenario 1-4). The difference is from the scale-down
of weighted sum operator Hisd
.Pm
j=1 Hij for the f11 (f12)
oriented attacks, which is smaller than d for f0 (∆f) oriented
attacks.
Nevertheless, tie-line power oriented attacks (e.g., P 11
tie,0
and ∆P 11
tie) produce negligent disruption (1) compared with
frequency oriented attacks. It stems from the ampliﬁcation
effect of β1 in ACE; β1 is the sum of the steady gain 1/R and
damping constant D of generators, which is usually several
hundred to thousand.
It can also be learned that the node values for these two
indices in the same scenario are not completely the same,
which does not contradict with Theorem 1. Since in The-
orem 1, it is assumed there exists no transmission loss. In
practical power systems, transmission loss cannot be ignored.
Moreover, when attack occurs, which is in the form of active
power disturbance, the voltage proﬁles will also change, which
further causes variation of voltage-dependent loads. However,
this does not affect the interchangeableness of disruption of
LFC performance and generation indices in general.
B. Vulnerability Mitigation for Cyber Security of LFC
In this section, classiﬁcation-based scenario identiﬁcation
is simulated using Kundur’s system. The simulated scenarios
include: 1) normal load variation, 2) step attack, 3) random
attack, 4) oscillating attack. The three classiﬁcation algorithms
in Section V-B are executed.
1) Detection using Composite MLP-based Classiﬁer:
MLP-based classiﬁer is ﬁrstly tested. 240 ACE data instances
are produced by simulating LFC on Kundur’s system using
MATLAB/SIMULINK (each scenario contains 60 data in-
stances). It should be mentioned that the simulation model
contains complete electromechanical dynamics and can reﬂect
the characteristics of real system. Hence, the simulation data
can be approximately used as the real-life data.
N1, N2 and N3 in Fig. 7 are chosen as 100, 60 and
30 respectively; M is 3 in this case. The detector is con-
structed with Keras, which is a high-level neural networks
API employing TensorFlow as its backend. The whole dataset
(DFT coefﬁcients) is split into training (70%) and test (30%)
datasets. In Fig. 10, four curves corresponding to loss and
accuracy of the classiﬁer with and without autoencoder are
given. Since the number of epochs to train the model is set as
10, the ﬁrst ten points on each curve quantify the performance
in training epochs, and the last one quantiﬁes the performance
in testing. From Fig. 10, autoencoding assists the classiﬁer in
overﬁtting avoidance; and the generalization performance of
the classiﬁer is enhanced. For comparison, the raw ACE time-
series data are trained using long short time memory (LSTM)
deep networks. The results are shown in Table I
detection accuracy
elapsed time (s)
LSTM
0.95
284.4
MLP
1
0.0023
TABLE I. Detection using LSTM and MLP network
As can be seen from Table I, though the difference of
detection performance using LSTM and MLP is insigniﬁcant,
the training time using LSTM is much larger than MLP.
As is mentioned before, cyber attacks might be rare events.
In this case, the dataset is not evenly distributed. We consider
6 data composition scenarios where the data instances under
normal load variation are set to the ﬁxed value 100 and the
data instances under attack scenarios are changed from 60 to
10 with an interval of 10; meanwhile, the rate of data instances
for test is set to 70% to 30% with an interval of 10%. Accuracy
rate is calculated to identify the probability of each instance’s
belonging to its right class. The results are shown in Fig. 11 In
Fig. 11, the number on x axis represents the data composition
scenario, e.g., 1 indicates the data composition is: 100(normal
load variation): 60(attack scenario 1): 60(attack scenario 2):
60(attack scenario 3); 2 indicates the data composition is:
100(normal load variation): 50(attack scenario 1): 50(attack
scenario 2): 50(attack scenario 3), and so forth. Similarly, the
number on y axis represents the test ratio scenario, e.g., 1
indicates 70% of the data is used for test while 30% is used


---

Page 8

---

8
5
10
15
20
25
1
2
0
500
1000
 
leaf node value in attack tree
attack scenario index
 
sensitivity index
magnitude/p.u.
5
10
15
20
25
1−4
9−12
Fig. 9. Leaf node value of different attack scenarios in attack tree
Fig. 10. Simulation results of MLP-based classiﬁer
1
2
3
4
5
1
2
3
4
5
6
0
0.2
0.4
0.6
0.8
1
test−ratio scenario
detection result
data composition scenario
accuracy rate
Fig. 11. Detection results under different data composition and
test-ratio scenarios (MLP)
for training; 2 indicates 60% of the data is used for test while
40% is used for training, and so forth. As can be seen in Fig.
11, detection results (accuracy rate) under different training
(testing) conditions are generally acceptable, even the ’worst’
performance (under the condition where data composition is:
100:40:40:40 and test rate is 60%) is 0.925. It can also be
found that the scarcity of data instances from attack scenarios
(100:10:10:10) does not signiﬁcantly inﬂuence the detection
performance, which is in compliance with actual detection
conditions.
2) Detection using other classiﬁers: In this section, the
classiﬁers based on Bayesian networks and SVM are tested.
The dataset (including data composition and test-ratio settings)
are the same as Section VI-B1. The DFT coefﬁcients are fed
into Baye’s networks and SVM, respectively. After learning
the model, the test results are shown in Fig. 12 and 13.
Compared with Fig. 11 and 13, it can be learned that
identiﬁcation performance using Bayesian networks is gen-
erally a little worse than MLP or SVM. Still, the ’worst’
performance using Bayesian networks is acceptable (0.854).
That is to say, the extracted feature (DFT coefﬁcients) can
effectively support the common basic classiﬁcation algorithms
for attack scenario identiﬁcation, avoiding resorting to more
complex and computationally inefﬁcient learning models. The
simulation results also show that training data quantities and
the proportion of training (testing) data are permitted to vary
in a wide range, verifying the robustness using the proposed
feature extraction method.
VII. CONCLUSION
In this paper, vulnerability for cyber security of LFC system
is studied. Through the theoretical and numerical analyses in
Section III and VI, it can be learned that system responses to
attacks on different LFC components show varying severity


---

Page 9

---

9
1
2
3
4
5
1
2
3
4
5
6
0
0.2
0.4
0.6
0.8
1
 
test−ratio scenario
detection result
data composition scenario
 
accuracy rate
Fig. 12. Detection results under different data composition and
test-ratio scenarios (Baye’s network)
1
2
3
4
5
1
2
3
4
5
6
0
0.2
0.4
0.6
0.8
1
test−ratio scenario
detection result
data composition scenario
accuracy rate
Fig. 13. Detection results under different data composition and
test-ratio scenarios (SVM)
degrees with frequency oriented attack producing the worst
outcome. It means frequency related settings should be given
priority in respect to protection. As for attack detection, it is
learned that DFT coefﬁcients under time-to-frequency-domain
transform serve an effective feature for classiﬁcation-based
detection algorithm, which can identify different type of attack
scenario and reduce computational burden.
APPENDIX A
ATTACK SCENARIOS IN SECTION VI-A
• Scenario 1(2) injection (scale) attack on frequency mea-
surement f11 of Unit 1 of Area 1
• Scenario 3(4) injection (scale) attack on frequency mea-
surement f12 of Unit 2 of Area 1
• Scenario 5(6) injection (scale) attack on power measure-
ment P 11
tie of Tie-line 1 of Area 1
• Scenario 7(8) injection (scale) attack on power measure-
ment P 12
tie of Tie-line 2 of area 1
• Scenario 9(10) injection (scale) attack on area frequency
measurement f1
• Scenario 11 injection attack on nominal frequency f0
• Scenario 12(13) injection (scale) attack on area frequency
deviation ∆f1 of Area 1
• Scenario 14(15) injection attack on nominal power of Tie-
line 1(Tie-line 2) P 11
tie,0 P 12
tie,0 of Area 1
• Scenario 16(17) injection (scale) attack on power devia-
tion of Tie-line 1 ∆P 11
tie of Area 1
• Scenario 18(19) injection (scale) attack on power devia-
tion of Tie-line 2 ∆P 12
tie of Area 1
• Scenario 20(21) injection (scale) attack on power devia-
tion of Tie-line ∆P 1
tie of Area 1
• Scenario 22(23) injection (scale) attack on LFC order
comm11 to Unit 1 of Area 1
• Scenario 24(25) injection (scale) attack on LFC order
comm12 to Unit 2 of Area 1
REFERENCES
[1] P. M. Esfahani, M. Vrakopoulou, K. Margellos, J. Lygeros, and G. An-
dersson, “A robust policy for automatic generation control cyber attack
in two area power network,” in 49th IEEE Conference on Decision and
Control (CDC), Dec. 2010.
[2] R. Tan, H. H. Nguyen, E. Y. Foo, D. K. Yau, Z. Kalbarczyk, R. K.
Iyer, and H. B. Gooi, “Modeling and mitigating impact of false data
injection attacks on automatic generation control,” IEEE Transactions
on Information Forensics and Security, vol. 12, no. 7, pp. 1609–1624,
2017.
[3] C. Chen, M. Cui, X. Wang, K. Zhang, and Y. Shengfei, “An investigation
of coordinated attack on load frequency control,” IEEE Access, 2018.
[4] S. Siddharth and G. Manimaran, “Model-based attack detection and
mitigation for automatic generation control,” IEEE Transactions on
Smart Grid, vol. 5, pp. 580–591, Mar. 2014.
[5] C. Chen, K. Zhang, K. Yuan, L. Zhu, and M. Qian, “Novel detection
scheme design considering cyber attacks on load frequency control,”
IEEE Transactions on Industrial Informatics, vol. PP, no. 99, pp. 1–1,
2017.
[6] Y. W. Law, T. Alpcan, and M. Palaniswami, “Security games for risk
minimization in automatic generation control,” IEEE Transactions on
Power Systems, vol. 30, pp. 223–232, Jan. 2015.
[7] C.-W. Ten, C.-C. Liu, and M. Govindarasu, “Vulnerability assessment
of cybersecurity for scada systems using attack trees,” in IEEE Power
Engineering Society General Meeting, Jun. 2007.
[8] C.-W. Ten, C.-C. Liu, and G. Manimaran, “Vulnerability assessment of
cybersecurity for scada systems,” IEEE Transactions on Power Systems,
vol. 23, no. 4, pp. 1836–1846, 2008.
[9] N. Liu, J. Zhang, H. Zhang, and W. Liu, “Security assessment for
communication networks of power control systems using attack graph
and mcdm,” IEEE Transactions on Power Delivery, vol. 25, no. 3,
pp. 1492–1500, 2010.
[10] A. Hahn and M. Govindarasu, “Cyber attack exposure evaluation frame-
work for the smart grid,” IEEE Transactions on Smart Grid, vol. 2, no. 4,
pp. 835–843, 2011.
[11] G. Hug and J. A. Giampapa, “Vulnerability assessment of ac state
estimation with respect to false data injection cyber-attacks,” IEEE
Transactions on Smart Grid, vol. 3, no. 3, pp. 1362–1370, 2012.
[12] X. Liu, M. Shahidehpour, Z. Li, X. Liu, Y. Cao, and Z. Li, “Power
system risk assessment in cyber attacks considering the role of protection
systems,” IEEE Transactions on Smart Grid, vol. 8, no. 2, pp. 572–580,
2017.
[13] R. G. Soares, H. Chen, and X. Yao, “A cluster-based semisupervised
ensemble for multiclass classiﬁcation,” IEEE Transactions on Emerging
Topics in Computational Intelligence, vol. 1, no. 6, pp. 408–420, 2017.
[14] G. JayaBrindha and E. G. Subbu, “Ant colony technique for optimizing
the order of cascaded svm classiﬁer for sunﬂower seed classiﬁcation,”
IEEE Transactions on Emerging Topics in Computational Intelligence,
vol. 2, no. 1, pp. 78–88, 2018.
[15] A. Saha, A. Konar, and A. K. Nagar, “Eeg analysis for cognitive failure
detection in driving using type-2 fuzzy classiﬁers,” IEEE Transactions on
Emerging Topics in Computational Intelligence, vol. 1, no. 6, pp. 437–
453, 2017.


---

Page 10

---

10
[16] T. Windeatt, R. Duangsoithong, and R. Smith, “Embedded feature
ranking for ensemble mlp classiﬁers,” IEEE transactions on neural
networks, vol. 22, no. 6, pp. 988–994, 2011.
[17] C.-Y. Liou, W.-C. Cheng, J.-W. Liou, and D.-R. Liou, “Autoencoder for
words,” Neurocomputing, vol. 139, pp. 84–96, 2014.
[18] Z. Chen, C. K. Yeo, B. S. Lee, and C. T. Lau, “Autoencoder-based net-
work anomaly detection,” in Wireless Telecommunications Symposium
(WTS), 2018, pp. 1–5, IEEE, 2018.
[19] C.-W. Hsu and C.-J. Lin, “A comparison of methods for multiclass
support vector machines,” IEEE transactions on Neural Networks,
vol. 13, no. 2, pp. 415–425, 2002.
[20] L. Koc, T. A. Mazzuchi, and S. Sarkani, “A network intrusion detection
system based on a hidden na¨ıve bayes multiclass classiﬁer,” Expert
Systems with Applications, vol. 39, no. 18, pp. 13492–13500, 2012.
