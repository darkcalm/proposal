

---

Page 1

---

 
1
 
Abstract—Microgrids can be isolated from large-scale power 
transmission/distribution systems (macrogrids) to deliver energy 
to their local communities using local energy resources and 
distribution systems when power outages occur in the macrogrids. 
In such situations, microgrids could be considered as the last 
available resource to provide energy to critical infrastructure. 
Research in monitoring and control of microgrids has been 
ongoing for the last two decades to protect and enhance 
communities’ 
socio-economic 
performance. 
However, 
of 
increasing concern are the possible cyber-physical threats that 
could disrupt the provision of macrogrids’ energy services to 
critical infrastructure and consequently impact the resilience and 
sustainability of communities. As cyber-physical systems, 
microgrids are not immune to these threats. Advanced monitoring 
and control are critical for real-time operations of microgrids and, 
therefore, directly influence communities’ resilience. Research 
trends in monitoring have recently shifted from normal situational 
awareness in forecasting, state estimation, and prediction to 
anomalies’ analysis and cyber-physical attacks’ detection to 
support resilient control systems. In addition, confounding the 
interpretation of research findings is the lack of a widely accepted 
definition, analytical methods, and metrics to consistently describe 
the resilience of power grids, especially for microgrids. This paper 
provides an overview of current research in microgrid resilience 
and presents an outlook for future trends. 
 
Index Terms—Cyber-physical microgrids, control, forecasting, 
intrusion, monitoring, resilience, state estimation. 
 
I. OVERVIEW OF CYBER-PHYSICAL MICROGRIDS 
ICROGRIDS play a significant role in ensuring 
resilient and sustainable energy to communities: 
Critical community infrastructures, such as hospitals, water 
treatment plants, and emergency and military services, rely 
heavily on power and energy services for their resilience and 
survivability, especially in the face of natural disasters. 
Catastrophic 
events 
such 
as 
hurricanes, 
blizzards, 
thunderstorms, and earthquakes can severely damage 
community infrastructures and result in power outages (among 
other consequences) that may take weeks to resolve. The 
economic and social hardships [1] of power disruptions caused 
by natural disasters in the U.S. is significant and has been 
estimated to cost $25–70 billion annually [2]. An emerging 
strategy to mitigate the consequences of power outages and 
promote resilience of the power grid is through the introduction 
of microgrids. As controllable entities, microgrids can be 
seamlessly connected or disconnected from macrogrids once 
outage events occur and so maintain required energy services 
to meet local demands. GTM Research forecasts that microgrid 
capacity in the U.S. will grow from 3.2 GW in 2017 to 6.5 GW 
in 2022, a 14.1 percent compound annual growth rate [3]. 
Worldwide, as of the second quarter of 2019, Navigant 
Research 
identified 
nearly 
4500 
microgrid 
projects 
(representing almost 27 GW power capacity) that have been or 
will be installed [4]. 
Advanced monitoring and control are required for optimal 
operations of microgrids: Microgrids are cyber-physical 
systems (CPS) that contain a wide variety of interconnected 
devices that measure, control, and actuate distributed energy 
resources (DER), loads, and power distribution devices. A 
typical microgrid is shown in FIGURE 1, where the monitoring 
and control system communicates internally with local devices 
via a local area network and externally with its enterprise 
network or power distribution systems via a wide area network. 
Since microgrids can be considered as an integrated power and 
energy system with DER, loads, and distribution automation 
devices, their monitoring and control can be as complex as in a 
bulk transmission system. Monitoring functions provide 
overarching information about the current system states; this 
information is also used to predict the system’s future states and 
Tuyen V. Vu, Member, IEEE, Bang H. L. Nguyen, Student Member, IEEE, Zheyuan Cheng, Student 
Member, IEEE, Mo-Yuen Chow, Fellow, IEEE, Bin Zhang, Senior Member, IEEE 
Cyber-Physical Microgrids: Toward Future 
Resilient Communities 
M 
 
FIGURE 1 - Cyber-physical Microgrid. Abbreviations: BR: breaker, CL: 
critical load, ES: energy storage, FC: field controller, NCL: noncritical load, 
PCC: point of common coupling, PV: photovoltaic. 
G
Utility 
Grid
PCC
Microgrid Monitoring & 
Control System
External System 
(e.g. Enterprise 
Network)
FC-G
FC-Wind
FC-PV
FC-ES
FC-CL
FC-NCL
Data Storage 
External Communication
Local Network Communication
Field Communication
PCC
BR


---

Page 2

---

 
2
events. Based upon the nature of the information monitored, a 
properly performing control system would provide optimal 
control actions, ensuring the resilience of the microgrid and 
critical community infrastructures. 
Recent reviews have covered forecasting and restoration 
methods for generic power systems’ resilience under natural 
disasters [5], networked microgrids in enhancing power system 
resilience against extreme events [6], or highlighted specific 
microgrid characteristics and surveyed research directions and 
challenges [7]. However, to the best of our knowledge, a 
comprehensive review of work on critical monitoring and 
control functions that consider future trends pertaining to the 
resilience of cyber-physical microgrids has not yet been 
published.  
The rest of the paper is organized as follows: In Section 2, 
we (1) present an overarching multilayer architecture that 
covers microgrids’ control and monitoring functionalities; (2) 
review critical monitoring functions including forecasting, 
system state estimation, and anomaly detection; and (3) 
summarize recent advanced control efforts that contribute to the 
resilience of a three-layer control system. Informed by this 
review, in Section 3 we identify future research directions to 
promote resilient microgrids against emerging cyber-physical 
threats. In Section 4, we summarize the review and research 
directions. 
II. RECENT TRENDS IN MONITORING AND CONTROL FOR 
CYBER-PHYSICAL MICROGRIDS 
A. Monitoring and Control Architectures 
An architecture that lays out monitoring and control functions 
for microgrids is critical as it provides researchers and 
engineers a framework for effective research and development 
efforts. The recent IEEE standard 2030.7-2017 identifies 
critical control functions for a centralized microgrid controller 
[8]. However, functions for more general purposes (i.e., those 
not specific to either centralized or distributed control) that are 
either consistent with or complementary to this standard are 
illustrated in FIGURE 2. This architecture has three main layers 
of monitoring and control. The first is the primary control and 
monitoring layer, where basic functions occur: DER 
(active/reactive 
power, 
frequency/voltage 
control), 
breakers/switches (on/off and protection functions), loads’ 
control 
(curtailment 
functions), 
advanced 
metering 
infrastructure (AMI) devices (voltage, current, and power 
measurement), and feedback from other devices (DER voltage, 
current, and power)). In the secondary layer, information 
feedback from the primary level can be processed for system 
state estimation to monitor the system’s behavior for control 
purposes. Control functions could also be performed including 
the frequency-restoration function (automatic generation 
control (AGC)), islanding operations and synchronization, and 
fault management (coordination of breakers/switches). In the 
tertiary layer, advanced monitoring functions such as 
forecasting (DER and load forecasting) can be performed, and 
other data analytics such as anomaly detection of AMI 
information (e.g., smart meters) can be conducted. Based upon 
information obtained from monitoring functions, the optimal 
management strategies for DER, load, load tap changer (LTC), 
and capacitor bank could be performed to achieve the system’s 
objectives or missions, whether they pertain to economic, 
resilience, or environmental attributes. The socio-economic 
performance measures associated with these objectives would 
be specified by the microgrid operator.  
 
FIGURE 2  –Monitoring and control functionalities in microgrids. 
Local/Primary Control and Monitoring
Secondary Monitoring and Coordination Control
Tertiary Monitoring and Control
System Objectives/Missions
External Information/Data and Interaction
Breakers/Switches Control
Voltage & Frequency Control
Active & Reactive Power Control
AMI Feedback
System State Estimation
AGC
Islanding & Synchronization
Forecast 
DER, Load
Other Data Analytics
Optimal Management 
DER, Load, LTC, Cap Bank
Economic
Resilience
Enterprise
Market
Weather
Load Control
Fault Management
Environment
Other Device Feedback
External Connections


---

Page 3

---

 
3
B. Monitoring Systems 
The monitoring functionalities in the three possible layers 
provide situational awareness to support control decisions. In 
the following, we review trends in monitoring functions, 
specifically state estimation at the secondary level, DER and 
load forecasting at the tertiary level, and anomaly detection at 
any monitoring level are critical for overall system situational 
awareness. 
1) System State Estimation 
State estimation (SE) is important for microgrid operations, 
particularly for energy management and secondary control of 
system voltage and frequency. State estimation usually 
processes noisy measurements to extract accurate states of 
power networks [9]. FIGURE 3 shows SE in relation to other 
functions in power systems. As a small power network, a 
microgrid requires SE, specifically distribution system state 
estimation (DSSE) algorithms, to extract its true states. Unlike 
conventional SE applied to transmission systems, DSSE 
algorithms suffer from the following limitations [10]: (1) Its 
observability is low due to the massive number of nodes, 
resulting in thousands of states to be estimated versus an 
insufficient number of measurements [10]. (2) Highly dynamic 
load profiles result in inaccurate forecasted load (pseudo 
measurements) [11]. And (3), DSSE is unable to decouple 
active and reactive powers in their formulations because of 
three-phase 
unbalanced 
operations 
and 
low 
reactance/resistance ratios [12]. In the literature, two types of 
DSSE have been reported, categorized as model-based or data-
driven [13]. 
Model-based methods rely on mathematical models of power 
networks and measurements. Conventionally, a weighted least-
squares (WLS) problem can be formulated for static SE [14]. 
However, the WLS process needs to reinitialize at every time-
step with new measurements making future estimated states 
independent from historical states. Therefore, this method 
detects bad data only within the snapshot measured. 
Consequently, it is vulnerable to false data injection attacks 
(FDIA) and other malicious data manipulation activities [15]. 
As an alternative, dynamic SE (DSE) algorithms have been 
studied to provide better situational awareness as they involve 
the state-space model of power networks, revealing the system 
states’ evolution [16]. Various DSE methods have been applied 
to estimate system states [17]; among these are Kalman filter 
(KF) variations, such as extended KF [18], ensemble KF [19], 
unscented KF [20], and particle filter [21], are frequently 
applied. Dynamic SE can track state changes and detect bad 
data using a normalized innovation or chi-square test [20]. 
However, DSE works based on accurate dynamic power system 
models, which are not always available. Therefore, DSE can be 
applied to synchronous generators’ state estimates, whereas the 
tracking SE (TSE) [16] is applied to network states provided 
that their operation is quasi-steady [22]. For loads that are 
forecasted, the forecasting-aided SE (FASE) [23] is applied. To 
improve the robustness of DSE under the presence of outliers, 
least-absolute-value (LAV) and generalized maximum-
likelihood (GML) methods have been proposed [22], [18]. H-
infinity based filtering has also been introduced to bound the 
system’s uncertainties [24]. In DSE, both node voltage and 
branch current states have been adopted in polar or rectangular 
form. The rectangular form yields a simpler formulation and 
more effective computation than the polar form does [25]. State 
estimation also can be realized using centralized or 
decentralized approaches. In decentralized approaches, the 
whole network is partitioned into subareas, where local 
estimators can be executed in parallel [26]. Centralized 
approaches have higher computation and communication 
burdens than decentralized methods [27] in part because 
TABLE 1. SE FRAMEWORKS AND TECHNIQUES MERITS AND DRAWBACKS. 
NOTE: (+) INDICATES ADVANTAGES AND (-) INDICATES DISADVANTAGES. 
SE Framework 
Robustness 
Nonlinearity 
SSE: (+) Simple, robust 
to uncertainties, (-) Do not 
track system dynamics. 
TSE: (+) Simple, suitable 
for stiff system states, (-) 
Cannot track variations of 
flexible loads and 
generation units, and low 
performance with weak 
grids. 
FASE: (+) involving 
states/load forecasting to 
SE, good performance at 
smooth change, (-) 
Neglect dynamics, 
inaccurate results under 
highly state fluctuations. 
DSE: (+) Provide best 
performance with state 
space representations, (-) 
Complex and high 
computation, where 
dynamic models are not 
always available. 
WLS: (+) simple, 
popular for static SE, (-
) sensitive to outliers. 
KF: (+) same cost 
function of WLS, 
popular for dynamic 
SE, (-) sensitive to 
outliers. 
LAV: (+) Robust 
against outliers, less 
sensitive to parameter 
errors (-) high 
computing cost, 
sensitive to attacks and 
measurement errors.  
GML:(+) robust 
against outliers, (-) 
sensitive to parameter 
errors. 
H-infinity: (+) limit 
system uncertainties (-) 
lack robustness to 
outliers and non-
Gaussian noise 
Linearization: Taylor 
approximation: (+) 
Constant Jacobian 
matrix with rational 
state variables, 
relatively simple (-) 
Low performance with 
highly nonlinear 
systems. 
Noises 
Propagation: 
Unscented, ensemble, 
particle 
transformations: 
(+) 
High performance with 
highly 
nonlinear 
systems, (-) Relatively 
complex. 
 
FIGURE 3 – System state estimation. 
State 
Estimation
Topology 
Processing
Observability 
Analysis
Bad Data 
Analysis
Estimated States
Data Acquisition
Fault 
Diagnosis
Security 
Assessment
Control & 
Management


---

Page 4

---

 
4
measurement redundancy is lessened by partitioning of the 
whole power network into subnetworks, and data fusion 
algorithms are required to reconstruct the global estimated 
states [26]. The state estimation frameworks with nonlinearity 
and robustness properties are compared as shown in Table 1. 
Based on the comparison, future work can focus on the 
enhancement of the accuracy and robustness of DSE, especially 
under Gaussian and/or nonGaussian noise, cyber-attacks, and 
bad data [24]. Research in distributed schemes for microgrids 
also needs to keep pace with recent developments [28]. In 
addition, future DSE should cover fault diagnosis and security 
assessment and support fault tolerant control to enhance system 
resilience [29], [30]. 
Data-driven approaches have recently become an attractive 
research direction since they require no physical models to 
estimate system states. The major trend in these approaches is 
to utilize artificial neural networks (ANN) to represent either 
parts of or the entire power network through training processes 
using extensive data collected from various resources. These 
ANN-based methods extract power networks' operational 
patterns and represent them as weights of neural nodes. This 
approach can improve the robustness of the SE against 
erroneous measurements with either a probabilistic neural 
network [31] or a parallel distributed processing model [32]. 
This approach when combined with traditional model-based 
methods results in improved observability with enhanced 
pseudo-measurement generation [33], [34]. Deep neural 
networks such as the stacked auto-encoder have also been 
applied recently to provide AC state estimation against cyber-
attacks [35]. Besides ANN, K-nearest neighbors search, 
supervised learning, and kernel trick methods have also been 
used for grid current state inference [36]. The main advantage 
of data-driven approaches over traditional SE (model-based) 
methods is that data-drive approaches do not depend on the 
system model, which could change during system operations. 
Therefore, they scale more readily than do model-based 
approaches. However, model-based approaches tend to be more 
accurate than data-driven based approaches. Despite the 
promise motivating the emerging usage of data-driven 
approaches, they require further research to prove their 
feasibility, applicability, and superiority compared to 
traditional methods.  
2) Distributed Energy Resources and Load Forecasting 
The DER (particularly PV and wind) and load forecasting 
(FIGURE 4) are critical for optimal operations of microgrids. 
In the following, we review recent literature on forecasting 
algorithms for loads and DER. 
Load forecasting. Load forecasting (LF) is classified as either 
long-term (LTLF) or short-term (STLF). Long-term LF focuses 
on load operations over a range of weeks or more and is used 
for resource planning; STLF focuses on load operations over a 
range of hours [37] and is used for real-time microgrid 
optimization, especially for the energy management system 
(e.g., peak shaving and demand response). However, STLF in 
microgrids is challenging because of the high variability and 
nonlinearity of load demands compared to bulk power systems 
[38]. Load forecasting can be performed using either statistical 
or intelligent approaches [39]. One popular statistical method, 
regression-based techniques, has been applied to probabilistic 
load forecasting using quantile regression averaging [40]. Other 
statistical methods include time-series techniques such as 
autoregressive moving average (ARMA) [41] or autoregressive 
integrated moving average (ARIMA) [42]. However, time-
series statistical methods are infrequently used because 
variations in microgrid load demand are high compared to bulk 
power systems.  Besides time-series and other statistical 
approaches, intelligent approaches such as support vector 
machine (SVM) have been reported for load forecasting of 
buildings [43]. Although the use of SVM for load forecasting 
may be applicable to microgrids, this has not yet been reported. 
However, the utilization of ANN for demand forecasting in 
microgrids has increased. Examples of ANN applications 
include their use in a bilevel forecasting structure, a combined 
neural network, an evolutionary algorithm, and a differential 
evolution algorithm [38], deep neural networks with multilayer 
perceptron [44], combined multilayer perceptron models [45], 
and a self-recurrent wavelet neural network [39]. 
DER forecasting. Forecasting the intermittent energy output of 
DER, including solar PV and wind, is as critical as load 
forecasting for optimal microgrid operations. However, 
because of relatively small geographical space and power size 
available for prediction (and so sensitivity to changes in the 
local environment) forecasting energy output from PV and 
wind is more challenging than in bulk power systems. 
Forecasting durations of wind and solar energy range from very 
short-term (intra-hour), short-term (intra-day), or long-term 
(day-ahead) [46], [47]. Common approaches for solar or wind 
forecasting are statistical, intelligent, physical-based, or hybrid 
approaches [48], [49].  
In solar forecasting, the appropriateness of each forecasting 
approach depends upon the spatial-temporal relationship of the 
application; statistical and intelligent approaches are more 
applicable to microgrids while physical-based approaches 
based on numeric weather prediction (NWP) are more 
applicable to bulk power systems. Statistical approaches 
include persistence and regression-based methods (ARMA and 
ARIMA) in which cloud images and satellite data are used [50]. 
FIGURE 4 – Forecasting in microgrids. 
Forecasting Algorithms
Statistical
Physical 
Intelligent
Control System
Weather
Historical
Forecasted
Power
Wind
PV
Load


---

Page 5

---

 
5
Intelligent approaches include SVM and ANN [51], [52]. 
Recent literature also shows a trend toward utilizing deep ANN 
for solar forecasting to improve prediction accuracy in 
microgrids [53]. In contrast, methods that use NWP models, 
such as European Centre for Medium-Range Weather Forecasts 
(ECMWF), Fifth-Generation Penn State/NCAR Mesoscale 
Model (MM5), and WRF, are more applicable to wide-area 
solar forecasting having resolution of tens of kilometers [46]; 
therefore, they might not be applicable to microgrids.  
Statistical methods such as persistence, ARMA, and ARIMA 
are also used to forecast wind-farm energy output, although 
their time horizon is normally limited to intra-hour and intra-
day forecasts [54]. Intelligent methods including SVM and 
ANN have also been investigated for improved forecasting 
accuracy. The prediction accuracy of SVM has been shown to 
be significantly better than the persistence model’s [55]. Over 
the last decade, ANN has been extensively investigated to 
improve the accuracy of wind-energy prediction using 
architectures with many layers and variations [56], [57]. Wind 
forecasting using physical-based approaches relies on NWP 
data to provide atmospheric variation over time, which becomes 
the input for the physical wind model to predict energy output 
[58]. Similar to solar forecasting, NWP data can be generated 
from ECMWF, MM5, or WRF models; however, the low 
space-resolution makes this physical-based method of limited 
applicability to microgrids. Most recent papers focus on 
forecasting for large wind systems (windfarms); microgrids, in 
contrast, have more distributed wind with relatively small 
energy output. Therefore, the applicability of these methods to 
microgrids needs further investigations. 
3) Anomaly and Intrusion Detection 
Microgrids, as complex cyber-physical systems (CPS), 
comprise physical power networks and information and 
communication technology (ICT) infrastructures that support 
control and monitoring [59]. In such CPS, detection of 
anomalies and intrusion attacks is the principal strategy to 
ensure secure microgrid operations [60]. Anomaly detection 
should be considered at all levels of monitoring. Anomaly 
detection approaches for cyber-physical security of power 
systems can be classified into two categories: physics-based 
and cyber-based [61].  
Physics-based methods build indicators of faults, attacks, and 
anomalies using data related to the physical power network 
[62]. Physical data received from sensors are processed using 
the SE tools. The differences between estimated and received 
data, called residuals, are derived through bad data 
identification algorithms [60]. These algorithms are statistical 
tests pertaining to two main categories: stateless and stateful. In 
a stateless test, a metric indicator, built on a residual or 
innovation vector at a single time step, is compared to a 
threshold 
for 
detection. 
Traditionally, 
in 
static 
SE, 
measurement errors are evaluated by a residual vector ( 𝑱(𝒙̂) 
detector) [14] or the largest normalized residual indicator 
(LNR) as 𝑙∞-norm [63]. Alternatively, the generalized 
likelihood ratio detector has been proved to have better 
performance than the traditional ones on large sample sizes 
[64]. In dynamic SE, measurement errors and sudden changes 
are normally detected via the normalized innovation ratio (NIR) 
[65]. However, NIR does not involve bad data in states or 
inputs; therefore, NIR may be bypassed by these attacks. By 
considering accumulated effects over time, a Chi-square 
detector can be used to detect soft failures such as instrument 
bias shift [66]. However, as a Chi-square detector can be 
bypassed by false data injection attacks (FDIA), the Euclidean 
distance metric, which evaluates the deviation of measured and 
estimated data, is introduced to enhance detection capability 
[66]. However, since straight-forward stateless tests use only 
the spatial relationship of data for detection, both the false 
positive (false alarms) rate is high as is the false negative as 
stealthy attacks may be missed. Alternatively, a stateful test 
better indicates anomalies [67] by tracking the historical 
changes of design metrics over time; in other words, it leverages 
the temporal relationship of measurements. For instance, to 
detect FDIA nonparametric cumulative sum (CUSUM) 
statistics accumulate the expected value of observations [68]. 
However, under unknown statistic attacks, CUSUM can be 
bypassed. Applying the generalized likelihood ratio test 
(GLRT) approach with CUSUM can resolve this problem [69]. 
Another metric, the signal temporal logic, is applied to detect 
anomalies [70]; but, this test only compares the measured value 
with its threshold, which could be fooled by stealthy attacks. To 
detect FDIA, Absolute and Kullback-Leibler distances are 
employed to track the dynamics of adjacent measurements [71]. 
Besides these tests and indicators, data-driven and machine-
learning tools have recently been utilized for anomaly 
detection. Such tools include semisupervised learning [72], 
deep autoencoders [73], naive Bayes classification [74], gate 
recurrent unit with multi-layer perceptron [67], principal 
component analysis [75], advanced multigrained cascade forest 
algorithm [76], and reinforcement learning [77]. Although this 
area is attracting many researchers, the efficiency and 
computational cost of these new methods need to be evaluated 
and compared with traditional methods to identify the most 
efficient and cost-effective physics-based strategies for 
anomaly detection. 
Cyber-based methods identify anomalies by leveraging IT 
data extracted from electronic devices and communication 
channels and can be classified into network-based and host-
based approaches [78]. Network-based methods capture and 
assess communication packets and network behavior, whereas 
host-based methods identify intrusion footprints within a host-
device by evaluating activities’ logging, the integrity of system 
files, and finite machine states [79]. Regarding the host-based 
approach, an embedded intrusion detection method was 
proposed in [80] for intelligent electronic devices (IED) in 
substations that monitor all incoming Generic Object-Oriented 
Substation Events (GOOSE) and  Sampled Values (SV) 
messages to enhance cybersecurity. Another host-based 
algorithm has been proposed based on intrusion footprints in 
user-interfaced computers and IED [81]. Regarding network-
based approaches, [82] proposed an intrusion detection system 


---

Page 6

---

 
6
(IDS) for a ZigBee home area network, where network features 
are analyzed. In [83], a method was proposed that transforms 
behavior rules for network devices to a state machine and 
compares their behavior specifications. A hierarchical IDS 
framework was proposed in [84], which employed an SVM and 
an artificial immune system to analyze network traffic at every 
layer of a smart grid. A similar method was also presented in 
[85] but for individual AMI devices. Besides host- and 
network-based approaches, hybrid anomaly detection systems 
have been proposed to cover both the host and network sides 
for substations [78]. In [86], a SCADA-specific IDS was 
introduced (based on IEC61850 standard) to cover detection 
mechanisms based on access control, protocol whitelisting, the 
cyber model, and combined parameters.  
To attain a robust and secure microgrid protected from 
various kinds of cyber-attacks, a defense-in-depth architecture 
is recommended when designing a microgrid’s control system; 
this strategy focuses on multiple security layers to detect and 
isolate attacks [87], [59]. Software-defined communication, an 
emerging networking paradigm, has also been implemented to 
enhance resilience of smart grids with remarkable results and 
may also be suitable for microgrids [88], [89]. 
C. Control Systems 
As noted, a microgrid control system can be divided into three 
layers: primary, secondary, and tertiary [90]–[92]. This article 
adopts widely acknowledged definitions for these layers from 
[93], which is also consistent with the standard P2030.7-2017. 
The primary layer includes device-level real-time feedback 
controls based on local measurements. The secondary layer 
includes system-level voltage and frequency regulations. The 
tertiary layer consists of slow time-scale system-level controls 
(e.g., energy management system (EMS), load restoration, and 
system reconfigurations).  
The concept of microgrid resilience is not yet standardized in 
the power and energy community [94], [95].  Most published 
work on resilient control focuses on one or a few control 
objectives within specific layers. The key resilient control 
objectives are summarized in FIGURE 5. In the following, we 
systematically discuss recent literature addressing resilience 
control of three layers in microgrids against commonly reported 
threats: 
natural 
disasters, 
disturbances 
and 
faults, 
communication flaws, and cyberattacks [95], [6].  
1) Resilience in Primary Control Layer 
As previously mentioned, the primary layer contains DER 
control and device feedback. With the growth of DER, 
including renewable energy sources in microgrids, advanced 
control is increasingly important. The aim of advanced control 
is to produce accurate and low distorted voltage and current 
under large system disturbances, such as faults and highly 
variable power generation and load demand. Many control 
strategies have been investigated including traditional PID 
control [96], state feedback control [97], model predictive 
control [98], and sliding mode control [99]. Most of these 
approaches, however, are either sensitive to uncertainties and 
disturbances [100] or lead to difﬁculties in low-pass ﬁltering or 
overstress on switching devices [101].  
To asymptotically reject disturbances, resonant control 
(RSC) based on the internal model principle (IMP) was 
proposed [102]. Various modiﬁed RSC schemes, such as 
proportional (P)+RSC [103], proportional-integral (PI)+RSC 
[101], multi-RSC (MRSC), and phase compensation RSC 
[104], were developed to improve transient response as well as 
stability and resilience against disturbances. Due to its 
effectiveness, RSC has become a popular controller for grid 
converters. A modified RSC which is equivalent to a parallel 
combination of a feedback controller (e.g., PID, deadbeat, or 
state feedback) and RSC components at all harmonics has 
attracted extensive attention [105]. Over the past decades, 
signiﬁcant advancements in DER control have been achieved 
including various phase compensation methods [101], selective 
harmonic RC [106], odd harmonic RC [107], discrete Fourier 
transform (DFT)-based RC [106] 6k±1 RC, and more general 
nk ± m RC [108]. 
Although these traditional schemes have demonstrated 
success, they lack frequency adaptability to accommodate 
frequency fluctuation from distributed generation resources 
caused by external disturbances or internal faults. To overcome 
such limitations, fractional order control [109] and variable 
sampling/switching period techniques [110] were developed. 
More recently, universal fractional-order design and software-
based virtual variable sampling schemes have been developed, 
which have greatly improved the reliability and resilience of the 
primary control layer’s operation under frequency fluctuation 
and various disturbances [111], [112].  
Table 2 shows the advantages and disadvantages of the 
above-mentioned methods in terms of structure, optimality, 
periodic signal tracking, and frequency fluctuation. 
 
FIGURE 5 – Key resilience control objectives. 
Tertiary
Secondary
Primary
Virtual Inertia
µs
ms
s
min
hour
day
Demand/supply 
Uncertainty
Disturbance 
Rejection
Coordinated frequency 
voltage control
Communication 
flaw resilience
Cyberattacks
Defensive 
islanding
Post Contingency 
Restoration
Self- healing 
Control


---

Page 7

---

 
7
2) Resilience in Secondary Control Layer 
To improve resilience in the secondary control layer against 
natural disasters, researchers have focused on the development 
of advanced control methodologies capable of maintaining and 
restoring system voltage and frequency during and after large 
system disturbances such as faults and contingencies. Solutions 
are described as either centralized or distributed. Centralized 
solutions reported in the literature include adaptive virtual 
inertia to stabilize system frequency against high renewable 
energy penetration [113] and frequency response rescheduling 
for distributed generators after disturbances [114]. Although 
these centralized solutions are effective and easy to implement, 
they are typically vulnerable to single-point-of-failure and do 
not scale well. To overcome these challenges, distributed 
control techniques are normally utilized, e.g. consensus-based 
methods, to coordinate DER to control the system’s voltage and 
frequency [115], [116].  
Researchers 
have 
also 
investigated 
resilience 
to 
communication flaws (e.g., packet loss, delay, and link failure) 
in the cyber layer of microgrids. Both centralized and 
distributed secondary control paradigms rely on the 
communication of local nodes’ voltage and frequency to 
stabilize the system’s voltage and frequency with accurate 
power-sharing among DER. One extensively reported 
centralized approach is based on software-defined network 
(SDN) [117], [118]; in it, a separate centralized controller is 
deployed to optimally control the cyber layer to ensure network 
QoS (quality of service). Other researchers have leveraged 
distributed peer-to-peer (P2P) communication protocols and 
noise-resilient state-observer techniques to achieve resilience 
against communication channel noise and disturbances [119], 
[120]. However, the scalability of the P2P configuration is 
largely 
constrained 
by 
the 
existing 
communication 
infrastructure. A hierarchical structure that is locally distributed 
and globally centralized is viewed as one of the most promising 
trends in this area. 
In response to another growing threat—cyberattacks—
various efforts have been made to secure both control 
information and decisions that are exposed in the 
communication network. Some researchers approach this topic 
from a conventional cybersecurity perspective: proposing 
resilient control solutions to traditional cyberattacks (e.g., 
denial-of-service attack [121], [122].) This body of work 
assumes a centralized attack detection and mitigation platform. 
Alternatively, other researchers have focused on insider attacks 
that target the system’s secondary control functions (e.g., false 
data injection and malicious interruption of control algorithm.) 
Distributed consensus control frameworks based on state 
observers have been proposed to detect and mitigate these 
attacks [120], [123]. Generally, this field of research typically 
adopts a bottom-up approach, where researchers propose 
solutions to specific vulnerabilities in various components in 
the microgrid control system. A well-recognized cyberattack 
resilience framework has yet to be developed to systematically 
integrate and coordinate the proposed countermeasures. 
3) Resilience in Tertiary Control Layer 
Considerable research on the tertiary control layer has been 
conducted to address natural disaster challenges. The objective 
of the tertiary layer is to optimally coordinate microgrid’s DER 
to minimize a disaster’s impact and to promote efficient 
recovery from it. Related research on tertiary control focuses 
defensive 
and 
intentional 
islanding 
[124], 
improving 
survivability and robustness [125], [126] reconfiguring and 
self-healing [127], [128], and restoring service [129], [130]. 
These efforts assume a centralized controller with full 
observability to optimally dispatch the controllable DER and 
microgrid switches to minimize loss of load under extreme 
events. Some distributed tertiary control approaches assume a 
multi-agent system that can cooperatively solve the underlining 
optimization problem and execute control commands [131], 
[132]. However, the distributed methods that have been adopted 
in the field typically handle standard optimization problems 
(e.g., convex problems). As the complexity of the optimal 
control problems grows, centralized evolutionary algorithms 
must be regularly adopted. 
Another pressing challenge in the tertiary control layer is to 
improve system resilience against communication flaws. This 
is a critical requirement for the distributed, controlled 
microgrid; contingencies in the cyber layer could result in 
wrong or infeasible control decisions and algorithm 
interruption/failure. Centralized approaches typically adopt the 
previously mentioned SDN technique to optimally route the 
network traffic and reconfigure communication links to provide 
acceptable QoS under cyber contingency [88], [133]. 
Distributed approaches leverage robust distributed optimization 
solvers, such as consensus-based subgradient methods, to 
mitigate the negative impact of communication flaws [134].  
Recently, numerous papers have presented centralized 
methods to handle conventional cyber threats (e.g., denial-of-
service attacks [121], sniffing attacks [135]), that target the 
tertiary control communication interface and traffic. In addition 
TABLE 2. COMPARISON AMONG CONTROL METHODS FOR PRIMARY CONTROL 
LAYER. 
 
Methods 
Pros. 
Cons. 
PID 
Simple structure; easy tuning. 
Control result is accurate; 
requires experience in parameter 
tuning. 
State 
feedback 
Simple structure; easy to make 
system stable. 
Cannot achieve zero tracking 
error theoretically. 
RSC 
High magnitude gain at the 
desired frequency. 
Complicated structure to 
compensate multiple high order 
harmonic frequencies. 
MPC 
High accuracy; optimal 
solution for a finite horizon. 
High computation cost; Not take 
advantage of the reference 
signal's periodic property 
RC 
Track any periodic signal with 
known frequency; low 
harmonic distortion. 
Needs to know the accurate 
frequency; cannot respond to 
frequency fluctuation. 
Variable 
sampling 
RC 
Track any periodic signal with 
known frequency and 
frequency fluctuation. 
More computation. 


---

Page 8

---

 
8
to these conventional cyber threats, some recent research 
focuses on advanced attacks such as false data injection attacks 
by using the sliding mode observer-based technique [136], an 
unscented Kalman filter [137], and a reputation-based system 
[138]–[140]. Finally, since tertiary control is closely tied to the 
economic objectives of for-profit entities or the missions of 
other entities, malicious attacks that specifically target energy 
markets have been discussed in the literature [141]–[143]. 
III. FUTURE DIRECTIONS 
In the following, we provide our outlook on future research 
directions that would allow for resilient microgrids against 
cyber-physical threats. 
Emerging cyber-physical threats: While most power outages 
are the result of extreme natural events, there is increasing 
concern about outages caused by man-made incidents including 
cyber-physical attacks. The Ukraine power grid attack in 
December 2015 that left about 230 thousand people without 
electricity for several hours is a now-famous case of a cyber-
attack in power systems [144]. Consequently, an extreme 
outage caused by a natural event coordinated by man-made 
malicious activities could take months to restore and cause 
significant national or international security concerns [145]. To 
perform advanced control functions, microgrids require 
advanced communication system devices that can be remotely 
monitored and controlled. However, advanced communication 
and control devices create vulnerabilities that could be 
exploited in malicious activities such as dial-up access to 
controllers, vendor supports, IT-controlled communication 
gear, access from corporate VPNs, database links, poorly 
configured firewalls, and peer utility links [146]. Therefore, 
more research in cyber-physical situational awareness and 
resilient control systems to guard against malicious activities 
for microgrids is needed. 
Standardization of resilience for microgrids: Effective 
monitoring and control system designs that increase the 
resilience of microgrids against harmful events, require 
clarification and standardization of the definition of resilience, 
associated analytical methods, and metrics. In one definition, 
the term ‘resilience’ means the ability to prepare for and adapt 
to changing conditions and withstand and recover rapidly from 
disruptions. Resilience includes the ability to withstand and 
recover from deliberate attacks, accidents, or naturally 
occurring threats or incidents [147]. By that definition, together 
with additional terms defined in [148], a visualization of 
resilience measurements (resilience level) throughout all stages 
of power grids that are impacted by a cyber-physical event is 
illustrated in FIGURE 6. Although the concept of resilience for 
complex systems has been around for decades, in the power and 
energy community a universally accepted definition of power 
system resilience, metrics, and methodologies is not yet 
available [149]. And although there are multiple solutions that 
could be used to quantify system resilience, no single solution 
is applicable to all systems [150], [151]. Currently, the most 
common approach is to assess the overall social and economic 
impacts of a (potential) event on the system. Based on the 
monitoring of that system, control can be designed to minimize 
the identified impacts. 
Cyber-Social-Physical microgrids: The future of system 
monitoring and control is moving toward the cyber-social-
physical microgrid - resilient communities. An important trend 
in this field is the modeling and integrating the human behavior 
into the resilience control system, such as human behavior 
aware residential community EMS [152], customer-centric 
demand response, human-centric home EMS [153], human 
errors, resilient social network, etc. As human behavior and 
privacy have a large impact on the resilient objectives, these 
additional issues need to be considered in future monitoring and 
control research for microgrids. 
IV. CONCLUDING REMARKS 
Microgrids are the most promising component of the power 
system capable of ensuring resilient energy services for critical 
infrastructure that is impacted by either natural disasters or 
man-made incidents. To guarantee real-time resilient operations 
of microgrids, monitoring and control functionalities are 
required. The trend in monitoring has recently shifted from 
normal situational awareness in forecasting, state estimation, 
and prediction to analysis of anomalies and detection of cyber-
physical attacks. To respond to estimated or forecasted events, 
resilient control systems to ensure optimal power flow and 
guarantee system voltage and frequency stability were 
discussed. Although these monitoring and control systems have 
been investigated in power distribution and transmission 
systems, their applicability to and challenges for microgrids 
need to be addressed. Critically, there is not yet a widely 
accepted (consensus) definition, analytical methods, and 
associated metrics to consistently describe the resilience of 
power grids, especially for microgrids. This issue is tightly 
related to cyber-social-physical system design, monitoring, and 
control of microgrids. Therefore, future research should 
consider (1) cyber-physical situational awareness and resilient 
control systems to guard against malicious activities for 
microgrids, 2) the need for a standardized resilience framework 
for comprehensive and consistent resilience research in 
different monitoring and control layers of microgrids, (3) 
distinguishing and clarifying the definition of resilience for 
FIGURE 6 – Resilient curve. 
Resist
Response
Recover
Restore
Normal
Time
Resilience level
Minimum 
Resilience
Cyber-
physical 
Event
Normal


---

Page 9

---

 
9
microgrids versus for distribution and transmission systems, 
and 4) human behavior in the system monitoring and control 
designs. 
BIOGRAPHIES 
 
Tuyen V. Vu is an Assistant Professor in the Department of 
Electrical and Computer Engineering at Clarkson University. 
He received his B.S. in electrical engineering from Hanoi 
University of Science Technology, Vietnam in 2012, and his 
Ph.D. in electrical engineering from Florida State University in 
2016. From 2016 to 2018, he was a postdoctoral research 
associate and a research faculty at Florida State University - 
Center for Advanced Power Systems. Dr. Vu has worked on 
monitoring and control of cyber-physical microgrids for various 
applications since 2013.  
Bang L. H. Nguyen received his B.S. and M.S. in electrical 
engineering from Ho Chi Minh University of Technology, 
Vietnam, in 2010 and 2013, respectively. In 2015, he was with 
Eastern International University, Binh Duong New City, 
Vietnam, as a lecturer. From 2016 to 2018, he was a research 
assistant in the power electronics and energy conversion lab 
(PEEC), Kyungpook National University, Korea. He is 
currently working towards his Ph.D. degree at Clarkson 
University. His areas of interest include the control and security 
of smart grids using deep learning. 
Zheyuan Cheng received his B.S. degree in electrical 
engineering from Nanjing University of Aeronautics and 
Astronautics, China, in 2015. He is currently pursuing his Ph.D. 
degree in electrical and computer engineering at North Carolina 
State University, Raleigh. He joined the Advanced Diagnosis, 
Automation, and Control Laboratory at North Carolina State 
University in 2016. His research interests include distributed 
control systems, computational intelligence, and distributed 
optimization. He has been working on microgrid distributed 
resilient control related projects since 2016. 
Mo-Yuen Chow is a Professor in the Department of Electrical 
and Computer Engineering at North Carolina State University. 
Dr. Chow’s recent research focuses on distributed control and 
management on smart micro-grids, batteries, and mechatronics 
systems. Dr. Chow has established the Advanced Diagnosis, 
Automation, and Control Laboratory. He is an IEEE Fellow. He 
has received the IEEE Region-3 Joseph M. Biedenbach 
Outstanding Engineering Educator Award, the IEEE Industrial 
Electronics Society Anthony J Hornfeck Service Award. He is 
a Distinguished Lecturer of IEEE IES. Dr. Chow has been 
working on several projects related to the cyber-physical 
microgrids since 2008. 
Bin Zhang is an Associate Professor in the Department of 
Electrical Engineering at the University of South Carolina, 
Columbia, SC. He received B.E. and M.E. degrees from 
Nanjing University of Science and Technology, Nanjing, China 
and Ph.D. degree from Nanyang Technological University, 
Singapore. Before he joined University of South Carolina, he 
was with General Motors, Detroit, MI, Impact Technologies, 
Rochester, NY, and Georgia Institute of Technology, Atlanta, 
GA. His research includes prognostics and health management, 
intelligent systems and controls. He has led and participated in 
some projects related to health management and control in 
recent years. 
REFERENCES 
[1] 
A. Lawson, “Resilience Strategies for Power Outages,” Cent. Clim. 
Energy Solut., pp. 1–22, 2002. 
[2] 
President’s Council of Economic Advisers and the U.S. Department of 
Energy’s Office of Electricity Delivery and Energy Reliability, with 
assistance from the White House Office of Science and Technology 
“Economic Benefits of Increasing Electric Grid Resilience to Weather 
Outages" Executive Office of the President,” Aug. 2013.  
[3] 
E. Wood, “Microgrid Investment in U.S. to Reach $12.5B: GTM 
Research,” Microgrid Knowledge, 30-Nov-2017. [Online]. Available: 
https://microgridknowledge.com/microgrid-investment-gtm/. 
[Accessed: 05-Jun-2019]. 
[4] 
Navigant Research, “Microgrid Deployment Tracker 2Q19,” 2019. 
[5] 
Y. Wang, C. Chen, J. Wang, and R. Baldick, “Research on Resilience of 
Power Systems under Natural Disasters - A Review,” IEEE 
Transactions on Power Systems, vol. 31, no. 2. pp. 1604–1613, 2016. 
[6] 
Z. Li, M. Shahidehpour, F. Aminifar, A. Alabdulwahab, and Y. Al-
Turki, “Networked Microgrids for Enhancing the Power System 
Resilience,” Proceedings of the IEEE, vol. 105, no. 7. pp. 1289–1310, 
2017. 
[7] 
A. Hirsch, Y. Parag, and J. Guerrero, “Microgrids: A review of 
technologies, key drivers, and outstanding issues,” Renewable and 
Sustainable Energy Reviews, vol. 90. pp. 402–411, 2018. 
[8] 
I. P. and E. Society, “I. Power and E. Society IEEE Standard for the 
Specification of Microgrid Controllers IEEE Standard for the 
Specification of Microgrid Controllers,” 2017. 
[9] 
A. G. E. Ali Abur, Power System State Estimation: Theory and 
Implementation - CRC Press Book. 2004. 
[10] 
D. Della Giustina, M. Pau, P. A. Pegoraro, F. Ponci, and S. Sulis, 
“Electrical distribution system state estimation: Measurement issues and 
challenges,” IEEE Instrum. Meas. Mag., vol. 17, no. 6, pp. 36–42, 2014. 
[11] 
W. H. Kersting, Distribution system modeling and analysis. 2001. 
[12] 
A. Monticelli, State Estimation in Electric Power Systems. 1999. 
[13] 
K. Dehghanpour, Z. Wang, J. Wang, Y. Yuan, and F. Bu, “A survey on 
state estimation techniques and challenges in smart distribution 
systems,” IEEE Transactions on Smart Grid, vol. 10, no. 2. pp. 2312–
2322, 2019. 
[14] 
F. C. Schweppe and J. Wildes, “Power System Static-State Estimation, 
Part I: Exact Model,” IEEE Trans. Power Appar. Syst., vol. PAS-89, no. 
1, pp. 120–125, 1970. 
[15] 
Y. Liu, P. Ning, and M. K. Reiter, “False data injection attacks against 
state estimation in electric power grids,” ACM Trans. Info. Syst, vol. 14, 
no. 1, p. 33, 2011. 
[16] 
A. S. Debs and R. E. Larson, “A Dynamic Estimator for Tracking the 
State of a Power System,” IEEE Trans. Power Appar. Syst., vol. PAS-
89, no. 7, pp. 1670–1678, 1970. 
[17] 
D. Simon, Optimal State Estimation: Kalman, H∞, and Nonlinear 
Approaches. 2006. 
[18] 
J. Zhao, M. Netto, and L. Mili, “A Robust Iterated Extended Kalman 
Filter for Power System Dynamic State Estimation,” IEEE Trans. Power 
Syst., vol. 32, no. 4, pp. 3205–3216, 2017. 
[19] 
C. Carquex, C. Rosenberg, and K. Bhattacharya, “State estimation in 
power distribution systems based on ensemble kalman filtering,” IEEE 
Trans. Power Syst., vol. 33, no. 6, pp. 6600–6610, 2018. 
[20] 
A. K. Singh and B. C. Pal, “Decentralized dynamic state estimation in 
power systems using unscented transformation,” IEEE Trans. Power 
Syst., vol. 29, no. 2, pp. 794–804, 2014. 
[21] 
K. Emami, T. Fernando, H. H. C. Iu, H. Trinh, and K. P. Wong, “Particle 
Filter Approach to Dynamic State Estimation of Generators in Power 
Systems,” IEEE Trans. Power Syst., vol. 30, no. 5, pp. 2665–2675, 2015. 
[22] 
A. Rouhani and A. Abur, “Linear phasor estimator assisted dynamic 
state estimation,” IEEE Trans. Smart Grid, vol. 9, no. 1, pp. 211–219, 
2018. 
[23] 
M. B. Do Coutto Filho and J. C. Stacchini de Souza, “Forecasting-aided 
state estimation - Part I: Panorama,” IEEE Trans. Power Syst., vol. 24, 
no. 4, pp. 1667–1677, 2009. 
[24] 
J. Zhao, “Dynamic State Estimation With Model Uncertainties Using 
$H_\infty$ Extended Kalman Filter,” IEEE Trans. Power Syst., vol. 33, 
no. 1, pp. 1099–1100, 2017. 
[25] 
M. Pau, P. A. Pegoraro, and S. Sulis, “Efficient branch-current-based 


---

Page 10

---

 
10 
distribution 
system 
state 
estimation 
including 
synchronized 
measurements,” IEEE Trans. Instrum. Meas., vol. 62, no. 9, pp. 2419–
2429, 2013. 
[26] 
C. Muscas, M. Pau, P. A. Pegoraro, S. Sulis, F. Ponci, and A. Monti, 
“Multiarea distribution system state estimation,” IEEE Trans. Instrum. 
Meas., vol. 64, no. 5, pp. 1140–1148, 2015. 
[27] 
J. Zhao et al., “Power System Dynamic State Estimation: Motivations, 
Definitions, Methodologies, and Future Work,” IEEE Trans. Power 
Syst., vol. 34, no. 4, pp. 3188–3198, 2019. 
[28] 
D. Ding, Q. L. Han, Z. Wang, and X. Ge, “A Survey on Model-Based 
Distributed Control and Filtering for Industrial Cyber-Physical 
Systems,” IEEE Trans. Ind. Informatics, vol. 15, no. 5, pp. 2483–2499, 
2019. 
[29] 
S. Ding, Model-Based Fault Diagnosis Techniques-Design Schemes, 
Algorithms and Tools. London: Springer, 2013. 
[30] 
S. X. Ding, Data-driven Design of Fault Diagnosis and Fault-tolerant 
Control Systems. 2014. 
[31] 
D. Gerbec, S. Gašperič, I. Šmon, and F. Gubina, “Allocation of the load 
profiles to consumers using probabilistic neural networks,” IEEE Trans. 
Power Syst., vol. 20, no. 2, pp. 548–555, 2005. 
[32] 
J. Wu, Y. He, and N. Jenkins, “A robust state estimator for medium 
voltage distribution networks,” IEEE Trans. Power Syst., vol. 28, no. 2, 
pp. 1008–1016, 2013. 
[33] 
E. Manitsas, R. Singh, B. C. Pal, and G. Strbac, “Distribution system 
state estimation using an artificial neural network approach for pseudo 
measurement modeling,” IEEE Trans. Power Syst., vol. 27, no. 4, pp. 
1888–1896, 2012. 
[34] 
Y. Raisee Gahrooyi, A. Khodabakhshian, and R. A. Hooshmand, “A 
New Pseudo Load Profile Determination Approach in Low Voltage 
Distribution Networks,” IEEE Transactions on Power Systems, 2017. 
[35] 
H. Wang et al., “Deep Learning-Based Interval State Estimation of AC 
Smart Grids Against Sparse Cyber Attacks,” IEEE Trans. Ind. 
Informatics, vol. 14, no. 11, pp. 4766–4778, 2018. 
[36] 
Y. Weng, R. Negi, C. Faloutsos, and M. D. Ilic, “Robust Data-Driven 
State Estimation for Smart Grid,” IEEE Trans. Smart Grid, vol. 8, no. 4, 
pp. 1956–1967, 2017. 
[37] 
G. Gross and F. D. Galiana, “Short-Term Load Forecasting,” Proc. 
IEEE, vol. 75, no. 12, pp. 1558–1573, Dec. 1987. 
[38] 
N. Amjady, F. Keynia, and H. Zareipour, “Short-term load forecast of 
microgrids by a new bilevel prediction strategy,” IEEE Trans. Smart 
Grid, vol. 1, no. 3, pp. 286–294, 2010. 
[39] 
H. Chitsaz, H. Shaker, H. Zareipour, D. Wood, and N. Amjady, “Short-
term electricity load forecasting of buildings in microgrids,” Energy 
Build., vol. 99, pp. 50–60, 2015. 
[40] 
B. Liu, J. Nowotarski, T. Hong, and R. Weron, “Probabilistic Load 
Forecasting via Quantile Regression Averaging on Sister Forecasts,” 
IEEE Trans. Smart Grid, vol. 8, no. 2, pp. 730–737, 2017. 
[41] 
S. J. Huang and K. R. Shih, “Short-term load forecasting via ARMA 
model identification including non-Gaussian process considerations,” 
IEEE Trans. Power Syst., vol. 18, no. 2, pp. 673–679, 2003. 
[42] 
M. Y. Cho, J. C. Hwang, and C. S. Chen, “Customer short term load 
forecasting by using ARIMA transfer function model,” in Proceedings 
of the International Conference on Energy Management and Power 
Delivery, EMPD, 1995, vol. 1, pp. 317–322. 
[43] 
Q. Li, Q. Meng, J. Cai, H. Yoshino, and A. Mochida, “Predicting hourly 
cooling load in the building: A comparison of support vector machine 
and different artificial neural networks,” Energy Convers. Manag., vol. 
50, no. 1, pp. 90–96, 2009. 
[44] 
L. Hernández, C. Baladrón, J. M. Aguiar, B. Carro, A. Sánchez-
Esguevillas, and J. Lloret, “Artificial neural networks for short-term load 
forecasting in microgrids environment,” Energy, vol. 75, pp. 252–264, 
2014. 
[45] 
P. P. K. Chan, W. C. Chen, W. W. Y. Ng, and D. S. Yeung, “Multiple 
classifier system for short term load forecast of Microgrid,” in 
Proceedings - International Conference on Machine Learning and 
Cybernetics, 2011, vol. 3, pp. 1268–1273. 
[46] 
M. Diagne, M. David, P. Lauret, J. Boland, and N. Schmutz, “Review of 
solar irradiance forecasting methods and a proposition for small-scale 
insular grids,” Renewable and Sustainable Energy Reviews, vol. 27. pp. 
65–76, 2013. 
[47] 
Q. Wang, C. B. Martinez-Anido, H. Wu, A. R. Florita, and B. M. Hodge, 
“Quantifying the Economic and Grid Reliability Impacts of Improved 
Wind Power Forecasting,” IEEE Trans. Sustain. Energy, vol. 7, no. 4, 
pp. 1525–1537, 2016. 
[48] 
J. Ma and X. Ma, “A review of forecasting algorithms and energy 
management strategies for microgrids,” Syst. Sci. Control Eng., vol. 6, 
no. 1, pp. 237–248, 2018. 
[49] 
J. Jung and R. P. Broadwater, “Current status and future advances for 
wind speed and power forecasting,” Renewable and Sustainable Energy 
Reviews, vol. 31. pp. 762–777, 2014. 
[50] 
R. Huang, T. Huang, R. Gadh, and N. Li, “Solar generation prediction 
using the ARMA model in a laboratory-level micro-grid,” in 2012 IEEE 
3rd International Conference on Smart Grid Communications, 
SmartGridComm 2012, 2012, pp. 528–533. 
[51] 
K. Y. Bae, H. S. Jang, and D. K. Sung, “Hourly Solar Irradiance 
Prediction Based on Support Vector Machine and Its Error Analysis,” 
IEEE Trans. Power Syst., vol. 32, no. 2, pp. 935–945, 2017. 
[52] 
F. Rodríguez, A. Fleetwood, A. Galarza, and L. Fontán, “Predicting 
solar energy generation through artificial neural networks using weather 
forecasts for microgrid control,” Renew. Energy, vol. 126, pp. 855–864, 
2018. 
[53] 
M. Husein and I. Y. Chung, “Day-ahead solar irradiance forecasting for 
microgrids using a long short-term memory recurrent neural network: A 
deep learning approach,” Energies, vol. 12, no. 10, 2019. 
[54] 
M. Lei, L. Shiyan, J. Chuanwen, L. Hongling, and Z. Yan, “A review on 
the forecasting of wind speed and generated power,” Renewable and 
Sustainable Energy Reviews, vol. 13, no. 4. pp. 915–920, 2009. 
[55] 
J. Zeng and W. Qiao, “Short-term wind power prediction using a wavelet 
support vector machine,” IEEE Trans. Sustain. Energy, vol. 3, no. 2, pp. 
255–264, 2012. 
[56] 
D. Díaz–Vico, A. Torres–Barrán, A. Omari, and J. R. Dorronsoro, “Deep 
Neural Networks for Wind and Solar Energy Prediction,” Neural 
Process. Lett., vol. 46, no. 3, pp. 829–844, 2017. 
[57] 
C. Y. Zhang, C. L. P. Chen, M. Gan, and L. Chen, “Predictive Deep 
Boltzmann Machine for Multiperiod Wind Speed Forecasting,” IEEE 
Trans. Sustain. Energy, vol. 6, no. 4, pp. 1416–1425, 2015. 
[58] 
S. Al-Yahyai, Y. Charabi, and A. Gastli, “Review of the use of numerical 
weather prediction (NWP) models for wind energy assessment,” 
Renewable and Sustainable Energy Reviews, vol. 14, no. 9. pp. 3192–
3198, 2010. 
[59] 
A. Ashok, A. Hahn, and M. Govindarasu, “Cyber-physical security of 
wide-area monitoring, protection and control in a smart grid 
environment,” J. Adv. Res., vol. 5, no. 4, pp. 481–489, 2014. 
[60] 
J. Giraldo et al., “A survey of physics-based attack detection in cyber-
physical systems,” ACM Computing Surveys, vol. 51, no. 4. 2018. 
[61] 
S. Tan, D. De, W. Z. Song, J. Yang, and S. K. Das, “Survey of Security 
Advances in Smart Grid: A Data Driven Approach,” IEEE 
Communications Surveys and Tutorials, vol. 19, no. 1. pp. 397–422, 
2017. 
[62] 
A. Monticelli, F. F. Wu, and M. Yen, “Multiple bad data identification 
for state estimation by combinatorial optimization,” IEEE Trans. Power 
Deliv., vol. 1, no. 3, pp. 361–369, 1986. 
[63] 
E. Handschin, F. C. Schweppe, J. Kohlas, and A. Fiechter, “Bad data 
analysis for power system state estimation,” IEEE Trans. Power App. 
Syst., vol. 94, no. 2, pp. 329–337, 1975. 
[64] 
O. Kosut, L. Jia, R. J. Thomas, and L. Tong, “Malicious data attacks on 
the smart grid,” IEEE Trans. Smart Grid, vol. 2, no. 4, pp. 645–658, 
2011. 
[65] 
S. Wang, W. Gao, and A. P. S. Meliopoulos, “An alternative method for 
power system dynamic state estimation based on unscented transform,” 
IEEE Trans. Power Syst., vol. 27, no. 2, pp. 942–950, 2012. 
[66] 
K. Manandhar, X. Cao, F. Hu, and Y. Liu, “Detection of faults and 
attacks including false data injection attack in smart grid using Kalman 
filter,” IEEE Trans. Control Netw. Syst., vol. 1, no. 4, pp. 370–379, 
2014. 
[67] 
J. J. Q. Yu, Y. Hou, and V. O. K. Li, “Online False Data Injection Attack 
Detection with Wavelet Transform and Deep Neural Networks,” IEEE 
Trans. Ind. Informatics, vol. 14, no. 7, pp. 3271–3280, 2018. 
[68] 
Q. Yang, J. Yang, W. Yu, D. An, N. Zhang, and W. Zhao, “On false 
data-injection attacks against power system state estimation: Modeling 
and countermeasures,” IEEE Trans. Parallel Distrib. Syst., vol. 25, no. 
3, pp. 717–729, 2014. 
[69] 
S. Li, Y. Yilmaz, and X. Wang, “Quickest Detection of False Data 
Injection Attack in Wide-Area Smart Grids,” IEEE Trans. Smart Grid, 
vol. 6, no. 6, pp. 2725–2735, 2015. 
[70] 
O. A. Beg, L. V. Nguyen, T. T. Johnson, and A. Davoudi, “Signal 
Temporal Logic-Based Attack Detection in DC Microgrids,” IEEE 
Trans. Smart Grid, vol. 10, no. 4, pp. 3585–3595, 2019. 
[71] 
S. K. Singh, K. Khanna, R. Bose, B. K. Panigrahi, and A. Joshi, “Joint-
Transformation-Based Detection of False Data Injection Attacks in 


---

Page 11

---

 
11 
Smart Grid,” IEEE Trans. Ind. Informatics, vol. 14, no. 1, pp. 89–97, 
2018. 
[72] 
S. A. Foroutan and F. R. Salmasi, “Detection of false data injection 
attacks against state estimation in smart grids based on a mixture 
Gaussian distribution learning method,” IET Cyber-Physical Syst. 
Theory Appl., vol. 2, no. 4, pp. 161–171, 2017. 
[73] 
J. Wang, D. Shi, Y. Li, J. Chen, H. Ding, and X. Duan, “Distributed 
Framework for Detecting PMU Data Manipulation Attacks with Deep 
Autoencoders,” IEEE Trans. Smart Grid, vol. 10, no. 4, pp. 4401–4410, 
2019. 
[74] 
M. Cui, J. Wang, and M. Yue, “Machine Learning Based Anomaly 
Detection for Load Forecasting Under Cyberattacks,” IEEE Trans. 
Smart Grid, pp. 1–1, 2019. 
[75] 
M. Esmalifalak, L. Liu, N. Nguyen, R. Zheng, and Z. Han, “Detecting 
stealthy false data injection using machine learning in smart grid,” IEEE 
Syst. J., vol. 11, no. 3, pp. 1644–1652, 2017. 
[76] 
Y. Cui, F. Bai, Y. Liu, P. Fuhr, and M. Morales-Rodriguez, “Spatio-
Temporal Characterization of Synchrophasor Data Against Spoofing 
Attacks in Smart Grids,” IEEE Trans. Smart Grid, pp. 1–1, 2019. 
[77] 
M. Ozay, I. Esnaola, F. T. Yarman Vural, S. R. Kulkarni, and H. V. Poor, 
“Machine Learning Methods for Attack Detection in the Smart Grid,” 
IEEE Trans. Neural Networks Learn. Syst., vol. 27, no. 8, pp. 1773–
1786, 2016. 
[78] 
J. Hong, C. C. Liu, and M. Govindarasu, “Integrated anomaly detection 
for cyber security of the substations,” IEEE Trans. Smart Grid, vol. 5, 
no. 4, pp. 1643–1653, 2014. 
[79] 
V. Chandola, A. Banerjee, and V. Kumar, “Anomaly detection: A 
survey,” ACM Computing Surveys, vol. 41, no. 3. 2009. 
[80] 
J. Hong and C. C. Liu, “Intelligent Electronic Devices with 
Collaborative Intrusion Detection Systems,” IEEE Trans. Smart Grid, 
vol. 10, no. 1, pp. 271–281, 2019. 
[81] 
C. W. Ten, J. Hong, and C. C. Liu, “Anomaly detection for cybersecurity 
of the substations,” IEEE Trans. Smart Grid, vol. 2, no. 4, pp. 865–873, 
2011. 
[82] 
P. Jokar and V. C. M. Leung, “Intrusion Detection and Prevention for 
ZigBee-Based Home Area Networks in Smart Grids,” IEEE Trans. 
Smart Grid, vol. 9, no. 3, pp. 1800–1811, 2018. 
[83] 
R. Mitchell and I. R. Chen, “Behavior-rule based intrusion detection 
systems for safety critical smart grid applications,” IEEE Trans. Smart 
Grid, vol. 4, no. 3, pp. 1254–1263, 2013. 
[84] 
Y. Zhang, L. Wang, W. Sun, R. C. Green, and M. Alam, “Distributed 
intrusion detection system in a multi-layer network architecture of smart 
grids,” IEEE Trans. Smart Grid, vol. 2, no. 4, pp. 796–808, 2011. 
[85] 
M. A. Faisal, Z. Aung, J. R. Williams, and A. Sanchez, “Data-stream-
based intrusion detection system for advanced metering infrastructure in 
smart grid: A feasibility study,” IEEE Syst. J., vol. 9, no. 1, pp. 31–44, 
2015. 
[86] 
U. K. Premaratne, J. Samarabandu, T. S. Sidhu, R. Beresh, and J. C. Tan, 
“An intrusion detection system for IEC61850 automated substations,” 
IEEE Trans. Power Deliv., vol. 25, no. 4, pp. 2376–2383, 2010. 
[87] 
Homeland Security, “Recommended Practice: Improving Industrial 
Control Systems Cybersecurity with Defense-In-Depth Strategies,” 
2016. 
[88] 
D. Jin et al., “Toward a Cyber Resilient and Secure Microgrid Using 
Software-Defined Networking,” IEEE Trans. Smart Grid, vol. 8, no. 5, 
pp. 2494–2504, 2017. 
[89] 
M. H. Rehmani, A. Davy, B. Jennings, and C. Assi, “Software Defined 
Networks-Based Smart Grid Communication: A Comprehensive 
Survey,” IEEE Commun. Surv. Tutorials, vol. 21, no. 3, pp. 2637–2670, 
2019. 
[90] 
D. E. Olivares et al., “Trends in microgrid control,” IEEE Trans. Smart 
Grid, vol. 5, no. 4, pp. 1905–1919, 2014. 
[91] 
Z. Cheng, J. Duan, and M.-Y. Chow, “To Centralize or to Distribute: 
That Is the Question: A Comparison of Advanced Microgrid 
Management Systems,” IEEE Ind. Electron. Mag., vol. 12, no. 1, pp. 6–
24, Mar. 2018. 
[92] 
T. Van Vu, D. Gonsoulin, F. Diaz, C. S. Edrington, and T. El-Mezyani, 
“Predictive Control for Energy Management in Ship Power Systems 
under High-Power Ramp Rate Loads,” IEEE Trans. Energy Convers., 
2017. 
[93] 
J. M. Guerrero, J. C. Vasquez, J. Matas, L. G. De Vicuña, and M. 
Castilla, “Hierarchical control of droop-controlled AC and DC 
microgrids - A general approach toward standardization,” IEEE Trans. 
Ind. Electron., vol. 58, no. 1, pp. 158–172, 2011. 
[94] 
A. A. Bajwa, H. Mokhlis, S. Mekhilef, and M. Mubin, “Enhancing 
power system resilience leveraging microgrids: A review,” Journal of 
Renewable and Sustainable Energy, vol. 11, no. 3. 2019. 
[95] 
R. Arghandeh, A. Von Meier, L. Mehrmanesh, and L. Mili, “On the 
definition of cyber-physical resilience in power systems,” Renewable 
and Sustainable Energy Reviews, vol. 58. pp. 1060–1069, 2016. 
[96] 
Y. X. Dai, H. Wang, and G. Q. Zeng, “Double Closed-Loop PI Control 
of Three-Phase Inverters by Binary-Coded Extremal Optimization,” 
IEEE Access, vol. 4, pp. 7621–7632, 2016. 
[97] 
C. A. Busada, S. Gomez Jorge, and J. A. Solsona, “Full-State Feedback 
Equivalent Controller for Active Damping in LCL-Filtered Grid-
Connected Inverters Using a Reduced Number of Sensors,” IEEE Trans. 
Ind. Electron., vol. 62, no. 10, pp. 5993–6002, 2015. 
[98] 
X. Li, H. Zhang, M. B. Shadmand, and R. S. Balog, “Model Predictive 
Control of a Voltage-Source Inverter with Seamless Transition between 
Islanded and Grid-Connected Operations,” IEEE Trans. Ind. Electron., 
vol. 64, no. 10, pp. 7906–7918, 2017. 
[99] 
M. Pichan and H. Rastegar, “Sliding-mode control of four-leg inverter 
with fixed switching frequency for uninterruptible power supply 
applications,” IEEE Trans. Ind. Electron., vol. 64, no. 8, pp. 6805–6814, 
2017. 
[100] Y. Shi, L. Wang, and H. Li, “Stability Analysis and Grid Disturbance 
Rejection for a 60-kW SiC-Based Filterless Grid-Connected PV 
Inverter,” IEEE Trans. Ind. Appl., vol. 54, no. 5, pp. 5025–5038, 2018. 
[101] Y. Yang, K. Zhou, M. Cheng, and B. Zhang, “Phase compensation 
multiresonant control of CVCF PWM converters,” IEEE Trans. Power 
Electron., vol. 28, no. 8, pp. 3923–3930, 2013. 
[102] K. Zhou and D. Wang, “Digital repetitive learning controller for three-
phase CVCF PWM inverter,” IEEE Trans. Ind. Electron., vol. 48, no. 4, 
pp. 820–830, 2001. 
[103] M. Rashed, C. Klumpner, and G. Asher, “Repetitive and resonant 
control for a single-phase grid-connected hybrid cascaded multilevel 
converter,” IEEE Trans. Power Electron., vol. 28, no. 5, pp. 2224–2234, 
2013. 
[104] R. Cárdenas, C. Juri, R. Peña, P. Wheeler, and J. Clare, “The application 
of resonant controllers to four-leg matrix converters feeding unbalanced 
or nonlinear loads,” IEEE Trans. Power Electron., vol. 27, no. 3, pp. 
1120–1129, 2012. 
[105] S. Jiang, D. Cao, Y. Li, J. Liu, and F. Z. Peng, “Low-THD, fast-transient, 
and cost-effective synchronous-frame repetitive controller for three-
phase UPS inverters,” IEEE Trans. Power Electron., vol. 27, no. 6, pp. 
2994–3005, 2012. 
[106] P. Mattavelli and F. P. Marafao, “Repetitive-based control for selective 
harmonic compensation in active power filters,” IEEE Trans. Ind. 
Electron., vol. 51, no. 5, pp. 1018–1024, 2004. 
[107] K. Zhou, D. Wang, B. Zhang, and Y. Wang, “Plug-in dual-mode-
structure repetitive controller for CVCF PWM inverters,” in IEEE 
Transactions on Industrial Electronics, 2009, vol. 56, no. 3, pp. 784–
791. 
[108] W. Lu, K. Zhou, D. Wang, and M. Cheng, “A generic digital nk ± m-
order harmonic repetitive control scheme for PWM converters,” IEEE 
Trans. Ind. Electron., vol. 61, no. 3, pp. 1516–1527, 2014. 
[109] T. Liu and D. Wang, “Parallel Structure Fractional Repetitive Control 
for PWM Inverters,” IEEE Trans. Ind. Electron., vol. 62, no. 8, pp. 
5045–5054, 2015. 
[110] M. A. Herran, J. R. Fischer, S. A. Gonzalez, M. G. Judewicz, I. Carugati, 
and D. O. Carrica, “Repetitive control with adaptive sampling frequency 
for wind power generation systems,” IEEE J. Emerg. Sel. Top. Power 
Electron., vol. 2, no. 1, pp. 58–69, 2014. 
[111] Z. Liu, B. Zhang, and K. Zhou, “Universal Fractional-Order Design of 
Linear Phase Lead Compensation Multirate Repetitive Control for PWM 
Inverters,” IEEE Trans. Ind. Electron., vol. 64, no. 9, pp. 7132–7140, 
2017. 
[112] Z. Liu, B. Zhang, K. Zhou, and J. Wang, “Virtual Variable Sampling 
Discrete Fourier Transform Based Selective Odd-Order Harmonic 
Repetitive Control of DC/AC Converters,” IEEE Trans. Power 
Electron., vol. 33, no. 7, Jul. 2018. 
[113] T. Kerdphol, F. S. Rahman, Y. Mitani, K. Hongesombut, and S. 
Küfeoğlu, “Virtual inertia control-based model predictive control for 
microgrid frequency stabilization considering high renewable energy 
integration,” Sustain., vol. 9, no. 5, 2017. 
[114] L. Che, X. Shen, and M. Shahidehpour, “Primary frequency response 
based rescheduling for enhancing microgrid resilience,” J. Mod. Power 
Syst. Clean Energy, 2019. 
[115] M. A. Shahab, B. Mozafari, S. Soleymani, N. M. Dehkordi, H. M. 
Shourkaei, and J. M. Guerrero, “Distributed Consensus-based Fault 


---

Page 12

---

 
12 
Tolerant Control of Islanded Microgrids,” IEEE Trans. Smart Grid, pp. 
1–1, 2019. 
[116] Y. Xu, Q. Guo, H. Sun, and Z. Fei, “Distributed Discrete Robust 
Secondary Cooperative Control for Islanded Microgrids,” IEEE Trans. 
Smart Grid, vol. 10, no. 4, pp. 3620–3629, 2019. 
[117] L. Ren et al., “Enabling resilient distributed power sharing in networked 
microgrids through software defined networking,” Appl. Energy, vol. 
210, pp. 1251–1265, 2018. 
[118] L. Ren, Y. Qin, B. Wang, P. Zhang, P. B. Luh, and R. Jin, “Enabling 
resilient microgrid through programmable network,” IEEE Trans. Smart 
Grid, vol. 8, no. 6, pp. 2826–2836, 2017. 
[119] N. M. Dehkordi, H. R. Baghaee, N. Sadati, and J. M. Guerrero, 
“Distributed Noise-Resilient Secondary Voltage and Frequency Control 
for Islanded Microgrids,” IEEE Trans. Smart Grid, vol. 10, no. 4, pp. 
3780–3790, 2019. 
[120] L. Chen, Y. Wang, X. Lu, T. Zheng, J. Wang, and S. Mei, “Resilient 
Active Power Sharing in Autonomous Microgrids Using Pinning-
Consensus-Based Distributed Control,” IEEE Trans. Smart Grid, pp. 1–
1, Apr. 2019. 
[121] P. Danzi, M. Angjelichinoski, C. Stefanovic, T. Dragicevic, and P. 
Popovski, “Software-Defined Microgrid Control for Resilience Against 
Denial-of-Service Attacks,” IEEE Transactions on Smart Grid, 2018. 
[122] S. Liu, Z. Hu, X. Wang, and L. Wu, “Stochastic Stability Analysis and 
Control of Secondary Frequency Regulation for Islanded Microgrids 
Under Random Denial of Service Attacks,” IEEE Trans. Ind. 
Informatics, vol. 15, no. 7, pp. 4066–4075, 2019. 
[123] L.-Y. Lu, H. J. Liu, H. Zhu, and C.-C. Chu, “Intrusion Detection in 
Distributed Frequency Control of Isolated Microgrids,” IEEE Trans. 
Smart Grid, pp. 1–1, 2019. 
[124] M. Panteli, D. N. Trakas, P. Mancarella, and N. D. Hatziargyriou, 
“Boosting the Power Grid Resilience to Extreme Weather Events Using 
Defensive Islanding,” IEEE Trans. Smart Grid, vol. 7, no. 6, pp. 2913–
2922, 2016. 
[125] H. Qiu et al., “Resilience-directional robust power dispatching of 
microgrids under meteorological disasters,” IET Renew. Power Gener., 
2019. 
[126] A. Hussain, A. Oulis Rousis, I. Konstantelos, G. Strbac, J. Jeon, and H. 
M. Kim, “Impact of Uncertainties on Resilient Operation of Microgrids: 
A Data-Driven Approach,” IEEE Access, vol. 7, pp. 4924–14937, 2019. 
[127] E. Pashajavid, F. Shahnia, and A. Ghosh, “Development of a Self-
Healing Strategy to Enhance the Overloading Resilience of Islanded 
Microgrids,” IEEE Trans. Smart Grid, vol. 8, no. 2, pp. 868–880, 2017. 
[128] Z. Wang, B. Chen, J. Wang, and C. Chen, “Networked microgrids for 
self-healing power systems,” IEEE Trans. Smart Grid, vol. 7, no. 1, pp. 
310–319, 2016. 
[129] Y. Xu, C. C. Liu, K. P. Schneider, F. K. Tuffner, and D. T. Ton, 
“Microgrids for service restoration to critical load in a resilient 
distribution system,” IEEE Trans. Smart Grid, vol. 9, no. 1, pp. 426–
437, 2018. 
[130] Y. Wang et al., “Coordinating Multiple Sources for Service Restoration 
to Enhance Resilience of Distribution Systems,” IEEE Trans. Smart 
Grid, pp. 1–1, 2019. 
[131] H. F. Habib, T. Youssef, M. H. Cintuglu, and O. A. Mohammed, “Multi-
Agent-Based Technique for Fault Location, Isolation, and Service 
Restoration,” IEEE Trans. Ind. Appl., vol. 53, no. 3, pp. 1841–1851, 
2017. 
[132] K. Dehghanpour, C. Colson, and H. Nehrir, “A survey on smart agent-
based microgrids for resilient/self-healing grids,” Energies, vol. 10, no. 
5. 2017. 
[133] V. Venkataramanan, A. Hahn, and A. Srivastava, “CP-SAM: Cyber-
Physical Security Assessment Metric for Monitoring Microgrid 
Resiliency,” IEEE Trans. Smart Grid, pp. 1–1, 2019. 
[134] M. Zholbaryssov, D. Fooladivanda, and A. D. Domínguez-García, 
“Resilient distributed optimal generation dispatch for lossy AC 
microgrids,” Syst. Control Lett., vol. 123, pp. 47–54, Jan. 2019. 
[135] Y. Li, Y. Qin, P. Zhang, and A. Herzberg, “SDN-Enabled Cyber-
Physical Security in Networked Microgrids,” IEEE Trans. Sustain. 
Energy, vol. 10, no. 3, pp. 1613–1622, 2019. 
[136] S. Saha, T. K. Roy, M. A. Mahmud, M. E. Haque, and S. N. Islam, 
“Sensor fault and cyber attack resilient operation of DC microgrids,” Int. 
J. Electr. Power Energy Syst., vol. 99, pp. 540–554, 2018. 
[137] N. Živković and A. T. Sarić, “Detection of false data injection attacks 
using unscented Kalman filter,” J. Mod. Power Syst. Clean Energy, vol. 
6, no. 5, pp. 847–859, 2018. 
[138] J. Duan, W. Zeng, and M. Y. Chow, “Resilient cooperative distributed 
energy scheduling against data integrity attacks,” in IECON Proceedings 
(Industrial Electronics Conference), 2016, pp. 4941–4946. 
[139] J. Duan, W. Zeng, and M.-Y. Chow, “Resilient distributed DC optimal 
power flow against data integrity attack,” IEEE Trans. Smart Grid, vol. 
9, no. 4, pp. 3543–3552, 2018. 
[140] W. Zeng, Y. Zhang, and M.-Y. Chow, “Resilient Distributed Energy 
Management Subject to Unexpected Misbehaving Generation Units,” 
IEEE Trans. Ind. Informatics, vol. 13, no. 1, pp. 208–216, Feb. 2017. 
[141] J. Duan and M. Y. Chow, “A novel data integrity attack on consensus-
based distributed energy management algorithm using local 
information,” IEEE Trans. Ind. Informatics, vol. 15, no. 3, pp. 1544–
1553, 2019. 
[142] C. Zhao, J. He, P. Cheng, and J. Chen, “Analysis of Consensus-Based 
Distributed Economic Dispatch Under Stealthy Attacks,” IEEE Trans. 
Ind. Electron., vol. 64, no. 6, pp. 5107–5117, 2017. 
[143] J. Duan and M.-Y. Chow, “A Novel Data Integrity Attack on Consensus-
based Distributed Energy Management Algorithm using Local 
Information,” IEEE Trans. Ind. Informatics, 2018. 
[144] D. of H. Security, “Alert ( IR-ALERT-H-16-056-01 ) Cyber-Attack 
Against Ukrainian Critical Infrastructure,” ICS-CERT, 2018. . 
[145] Microgrid Knowledge, “Microgrid Cybersecurity: Protecting and 
Building the Grid of the Future,” S&C Electric Company. S&C Electric 
Company, p. 10, 28-Jan-2017. 
[146] US-CERT, “Overview of Cyber Vulnerabilities | ICS-CERT,” Online, 
2006. [Online]. Available: https://ics-cert.us-cert.gov/content/overview-
cyber-vulnerabilities. [Accessed: 06-May-2019]. 
[147] “Presidential policy directive 21: Critical infrastructure security and 
resilience,” in Cybersecurity: Executive Order 13636 and the Critical 
Infrastructure Framework, 2014. 
[148] K. Eshghi, B. K. Johnson, and C. G. Rieger, “Power system protection 
and resilient metrics,” in Proceedings - 2015 Resilience Week, RSW 
2015, 2015, pp. 212–219. 
[149] E. Vugrin, A. Castillo, and C. Silva-Monroy, “Resilience Metrics for the 
Electric 
Power 
System: 
A 
Performance-Based 
Approach,” 
Albuquerque, New Mexico, 2017. 
[150] Edison Electric Institute, “Before And After The Storm,” 2014. 
[151] F. H. Jufri, V. Widiputra, and J. Jung, “State-of-the-art review on power 
grid resilience to extreme weather events: Definitions, frameworks, 
quantitative assessment methodologies, and enhancement strategies,” 
Applied Energy. pp. 1049–1065, 2019. 
[152] B. Aksanli and T. S. Rosing, “Human Behavior Aware Energy 
Management in Residential Cyber-Physical Systems,” IEEE Trans. 
Emerg. Top. Comput., pp. 1–1, 2017. 
[153] S. Chen et al., “Butler, Not Servant: A Human-Centric Smart Home 
Energy Management System,” IEEE Commun. Mag., vol. 55, no. 2, pp. 
27–33, 2017. 
 
 
 
 
 
