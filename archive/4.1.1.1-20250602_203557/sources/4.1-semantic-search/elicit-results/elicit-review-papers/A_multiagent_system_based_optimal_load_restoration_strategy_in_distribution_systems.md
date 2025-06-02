

---

Page 1

---

 
 
1
Abstract—This paper proposes a new deep learning (DL) based 
model-free robust method for bulk system on-line load restoration 
with high penetration of wind power. Inspired by the iterative 
calculation of the two-stage robust load restoration model, the 
deep neural network (DNN) and deep convolutional neural net-
work (CNN) are respectively designed to find the worst-case sys-
tem condition of a load pickup decision and evaluate the corre-
sponding security. In order to find the optimal result within a 
limited number of checks, a load pickup checklist generation 
(LPCG) algorithm is developed to ensure the optimality. Then, 
the fast robust load restoration strategy acquisition is achieved 
based on the designed one-line strategy generation (OSG) algo-
rithm. The proposed method finds the optimal result in a model-
free way, holds the robustness to handle uncertainties, and pro-
vides real-time computation. It can completely replace conven-
tional robust optimization and supports on-line robust load resto-
ration which better satisfies the changeable restoration process. 
The effectiveness of the proposed method is validated using the 
IEEE 30-bus system and the IEEE 118-bus system, showing high 
computational efficiency and considerable accuracy. 
Index Terms—Convolutional neural network (CNN), deep 
learning (DL), power system resilience, load restoration, wind 
power integration. 
NOMENCLATURE 
A.  Indices 
i 
Index of nodes  
Linner 
Indices of iterative calculations 
* 
Index for variables with fixed values 
s 
Index of samples 
k 
Index of neurons  
j 
Index of sample features 
l 
Index of layers of neural networks 
B.  Sets 
NL 
Set of load nodes 
NW 
Set of wind farm nodes 
Ns 
Set of sample data 
C.  Parameters 
Δfmax 
Upper bound of frequency deviation 
Vmax, Vmin 
Maximum and minimum values of voltage 
Smax, Smin 
Set of sample data 
                                                          
J. Zhao and F. Li are with the Department of EECS, The University of 
Tennessee, Knoxville. TN 37996, USA (e-mail: jzhao44@utk.edu; 
fli6@utk.edu). 
X. Chen (e-mail: xi.chen@geirina.net). 
Q. Wu (e-mail: quiwudtu@gmail.com).  
plow,i, pup,i 
Lower and upper bounds of active power   
of node i  
C, D, E, F 
Matrixes of parameters of equalities 
H, I 
Matrixes of parameters of in-equalities 
w
l 
j, b
l 
k 
jth weight and kth biases parameters of lth  
layer 
η 
Learning rate 
NLay 
Total number of hidden layers 
P, Q, B, θ, V 
 
Vectors of bus active and reactive power 
injection, susceptance matrix, voltage 
magnitude and angel 
Lupp, Lpick,upp, Lpick,low 
 
Upper bound of the total pickup load amount, 
acceptable upper and lower bounds of load 
pickup amount 
sj, εj 
Capacity and frequency response rate of gen-
erator j 
EW,i, EW,i,ini 
 
Expected wind power output of wind node i in 
the current step and last step 
Istr 
The number of combinations in the checklist 
D.  Variables  
XL 
Vector of load pickup decisions 
EL 
Vector of expected load amount 
pG 
Vector of generator outputs 
pL, pW  
Vectors of uncertain load amount and wind 
power output 
V, S 
Vectors of voltage and branch power 
t 
Restoration step time 
λ, μ  
Vectors of Kuhn–Tucker multipliers 
z
+ 
i , z
-
i  
Auxiliary binary variables of node i 
A
+ 
I , A
-
I, B
+ 
I , B
-
I 
 
Auxiliary variables and binary variables for 
linearization 
x
l 
j 
jth input of lth layer 
z
l 
k, y
l 
k 
kth weighted aggregation and output of lth 
layer 
p
s 
L,i, p
s 
W,i, p
s 
G,i, q
s  
G,i 
 
Variables of load and wind active power and 
generator active and reactive power for sth 
sample of node i 
V
s 
I , θ
s 
i  
Variables of voltage magnitude and angel for 
sth sample of node i 
Deep Learning based Model-freeRobust Load 
Restoration to Enhance Bulk System Resilience with 
Wind Power Penetration 
  Jin Zhao, Member, IEEE, Fangxing Li, Fellow, IEEE, Xi Chen, Senior Member, IEEE,  
Qiuwei Wu, Senior Member, IEEE 


---

Page 2

---

 
 
2
I.  INTRODUCTION 
IGH-IMPACT and low-probability events, such as ex-
treme weather events, are occurring with increasing inten-
sity [1], indicating the necessity of enhancing power system 
resilience. After a complete or partial collapse of a power sys-
tem, power system restoration is crucial to bringing the system 
back to normal conditions [2], [3]. Fast load restoration, as the 
final goal of the restoration process, is indispensable to power 
system resilience after outage events [4]. In this process, the 
resilience is defined as the ability to quickly pick up shed loads 
and is measured by recovered load amount. At the bulk system 
level, the essential purpose of large-scale load restoration is to 
efficiently and safely dispatch available power sources to satis-
fy the power demand of load blocks. Since the generation is 
limited in the restoration process [5], the optimal load restora-
tion strategy is pursued to make full use of the available power 
supply in the system. In a step-by-step process, there are three 
major issues for determining the load restoration strategy of 
each step: i) location of load to restore, i.e. where, ii) restora-
ble size of load, i.e. how much, and iii) operation time, i.e. 
when [6]. Mathematically, it is a combination optimization 
problem. With binary variables representing load pickup deci-
sions, the mixed-integer optimization [7], [8] is widely used to 
find the optimal load restoration strategy.  
With increasing integration in power systems, renewable 
energy sources (RESs) have become an indispensable part of 
the power supply in the restoration process. Wind power based 
sources benefit load recovery with fast self-restarts and a flex-
ible power supply [9]. However, because of the intermittency 
of wind power sources and the cold pickup phenomenon, un-
certainties should be considered. Therefore, load restoration 
optimization in a wind power penetrated system requires un-
certainty handling capabilities to guarantee the feasibility of 
the obtained scheme [10]-[13]. In [10], stochastic program-
ming was used to develop an offline restoration planning tool 
for harnessing wind energy to enhance grid resilience. The 
chance-constrained stochastic program was applied in [11] to 
model the load restoration problem considering stochastic en-
ergy variations. The robust optimization method helps realize 
restoration related coordination in a wind power participated 
restoration process [12], [13].  
In order to achieve optimal restoration decision-making, 
model-based methods [7]-[13] have been well studied in recent 
works. However, model-based optimization methods are gen-
erally time-consuming in dealing with uncertainties. The com-
putation efficiency of the stochastic programming is low when 
the number of scenarios is large [10], [11], and robust restora-
tion models require iterative calculation which increases model 
scale in the iteration [12], [13]. The time-consuming model 
solving limits the corresponding strategies to off-line applica-
tions [10], [13], which significantly reduces their practicality. 
Therefore, fast acquisition of a robust load restoration strategy 
is needed to realize on-line robust restoration with real-time 
computation.  
Deep learning (DL) methods, such as deep neural networks 
(DNNs) and deep convolutional neural networks (CNNs), 
promise to realize on-line robust load restoration. In a model-
free way, DL methods automatically extract features from pro-
vided data sets and achieve accurate model regression [14]. 
Well-trained DNN and CNN develop high generalization and 
can be directly applied to new cases without costly numerical 
computation. Accordingly, in recent years, DL methods have 
been applied to help solve various problems in power systems 
[15]-[17]. DNN has been utilized in load and wind power 
forecasting [18], RES modeling [19] and optimization model 
regression [20], and the efficiency of deep CNNs has been 
verified in sparse vector related classification [21] and AC 
power flow (PF) equations related regression [22]. In the field 
of power system restoration, artificial neural networks (ANNs) 
were once popular [23], however, the application of DL meth-
ods is still in the initial stage. With high computational effi-
ciency and considerable accuracy, the DL based method has 
great potential to satisfy the real-time computational require-
ments of on-line robust load restoration.  
Existing model-based methods with uncertainty considered 
are generally limited to off-line applications, while on-line 
load restoration is preferred in the wind power penetrated res-
toration process. Therefore, a new deep learning-based model-
free robust load restoration method is proposed in this paper to 
support the real-time decision-making of the on-line load res-
toration process. First, the two-stage robust optimization of 
load restoration is performed to provide training data for the 
DL process. Then, a DNN and CNN are designed and trained 
to capture the worst-case condition and check the security of 
load pickup decisions under uncertainties. Finally, a load 
pickup checklist generation algorithm (LPCG) and a one-line 
strategy generation (OSG) algorithm are developed to find the 
final optimal robust load restoration strategy in a model-free 
way. The whole methodology contains different approaches, 
although the model-based method is applied to complete the 
training of DL methods, the proposed method finally realizes 
the model-free load restoration process. 
The contributions of this paper can be summarized as fol-
lows: 1) This work applies advanced DL methods in the field 
of bulk power system restoration. Differing from the conven-
tional model-based methods, this paper proposes a new model-
free method for finding the optimal load restoration strategy. 
The well-studied optimization techniques provide training data 
for the DL method, and well-trained neural networks are used 
in the load restoration process to realize the model-free load 
restoration strategy generation. 2) The proposed method is 
with uncertainty handling ability. The original problem is de-
composed into three sub-problems which fit into model-free 
solutions. Then, a series of techniques, including a DNN, a 
CNN, the LPCG algorithm and the OSG algorithm, are de-
signed and combined to fully replace the robust mathematical 
optimization process. With good optimization performance, 
the obtained result is robust to uncertain load pickup amount 
and wind power output, which ensures safe restoration of the 
wind power penetrated system. 3) Finally, this work realizes 
the on-line application of the robust load restoration scheme. 
With high computational efficiency and considerable accuracy, 
H


---

Page 3

---

 
 
3
the proposed method provides the real-time computation of the 
robust strategy. This allows the proposed method to apply at 
the on-line level to better satisfy the changeable restoration 
process. 
The rest of the paper is organized as follows: Section II pro-
vides the two-stage robust load restoration models and the 
corresponding solution method. The DNN and CNN are de-
signed and trained in Section III. Section IV shows the devel-
oped LPCG algorithm and OSG algorithm. Section V provides 
case study results and discussions, followed by the conclusions. 
II.  OPTIMIZATION MODELS OF ROBUST LOAD RESTORATION 
This section introduces the robust optimization of the load 
restoration problem. The two-stage robust optimization model 
is constructed followed by a column and constraint generation 
(C&CG) based iterative calculation process.  
A.  Robust load restoration model 
The goal of load restoration is to quickly restore sufficient 
power supply to all load blocks via a step-by-step process. The 
objective of each step is maximizing the load recovery amount 
in a meshed network considering the limited generation of 
generators, line power flow limits, and voltage and frequency 
securities. In the load restoration process, the cold load pickup 
(CLPU) phenomenon caused by thermostatically controlled 
loads leads to unpredictable inrush load pickup amount. Due 
to uncertainties of wind power output and load amount caused 
by the cold load pickup phenomenon, the robustness of the 
load restoration strategy is enhanced using the two-stage ro-
bust form (1). Model (1) is a single-step optimization model 
which is recursively performed in the step-by-step load resto-
ration process. 


L
G
L
W
T
L
L
G
W
,
,
min
(
) + max min
(
)
(
)


t,
sum
sum
sum
X
p ,  V S
p
p
X E
p
p
(1a) 


1
L
. .
0
s t
F

X
                                      (1b) 



G
2
0
G
F t


p
                           (1c) 


3
L
W
max
,
f
F
f



p
p
                 (1d) 


4
G
L
W
min
max
min
max
[ ,
]
,
,
F
V
V
V
S
S
S










V S
p
p
p
                    (1e) 
The objective (1a) contains two terms. The first term of (1a) 
is the weighted expected load restoration amount and the latter 
term represents the power supply requirement of the restored 
load. In the max-min term, the max finds the worst case condi-
tion w.r.t uncertain variables pL, pW, while min denotes reduc-
ing the power supply requirement under the worst case w.r.t pG, 
t, V, and S. In load pickup constraint (1b), F1(.) represents 
decision variable related functions which describe the practice 
load pickup characteristic. F2(.) and G () provide the function 
relationship between step time and generator outputs. Accord-
ingly, constraint (1c) is used to satisfy generator ramping up 
characteristics [5] as well as the spinning reserve which sur-
vives the largest loss of energy contingency [24]. The frequen-
cy deviation and dynamic reserve limits are presented in (1d) 
which contains F3(.) reflecting the relationship between the 
system active power increment and frequency deviation [25]. 
Voltage and branch flow limits are included in the AC PF re-
lated constraints (1e) where F4(.) denotes power flow functions.  
Normally, power flow calculation will be convexified to re-
alize tractable computation of load restoration optimization. 
Without loss of generality, this paper takes the linearized AC 
PF calculation method as an example [26]. Other convexifica-
tion methods can also be used, and the feasibility of the pro-
posed method will not be influenced. 
B.  Solution of model-based robust load restoration 
Model (2), which is a two-stage robust optimization with a 
polyhedral uncertainty set Φ (2d) for uncertain wind power 
output and load amount [27], is the equivalently transfor-
mation of model (1). Therein, constraint (1b) is represented by 
(2b) and (1c) – (1e) are included in (2c). 


L
L
W
'T
L
L
G
W
,
min
+ max min
(
)
(
)


sum
sum
X
Y
p
p
X E
p
p
(2a) 


L
.
{
: 1b }

s t
X
                                 (2b) 




G
=
(
, ) : 1c , 1d , 1e


Y
p , V S
  (2c) 


L
W
,
,
L
W
(
,
) : p
p
,
&
low i
i
up i
p
i
N
N




p
p
 (2d) 
The first stage includes the first min term of the objective in 
(2a) and load pickup variable related constraints (2b), while 
the second stage contains the max-min term in the objective 
(2a) and all the remaining constraints (2c)-(2d). The robust 
load restoration maximizes load recovery in the first stage and 
minimizes the generation requirement in the worst-case condi-
tion under uncertainties. In order to solve the integer variable 
integrated two-stage problem, the C&CG method is applied 
with an iterative calculation of inner and outer sub-models. 
According to the C&CG method, the inner-level sub-model 
(2) is shown as model (3). In (3), (3b) and (3c) denote equality 
and inequality of the second stage constraint (2c). Model (3) is 
further transformed into model (4) using dual theory for the 
purpose of solution. Note that the dual theory is used when the 
AC PF is linearized. In other convexification cases, the 
Karush–Kuhn–Tucker (KKT) condition can be used to get 
model (4). 


L
W
G
W
(
,
)
max
min
(
)
(
)
sum
sum


Y
P
P
p
p
                (3a) 
*
L
L
W
. .
0




:
s t C
D
E
F
Y
X p
p
    (3b) 
0 :


H
I
Y
           (3c) 
L
W
*
L
L
W
(
,
)
max




D
E
F
I
P
P
X p
p



         (4a) 
. .
0


s t
C
H


                                (4b) 


                                (4c) 
With determined load pickup decision X
* 
L obtained from the 
outer-level problem, the goal of the inner-level problem is 
providing the worst-case condition for the outer-level problem. 
Since it is proven that the worst-case realization of the polyhe-
dral uncertainty is identified at vertices, (5) holds in model (4). 


,
,
L
W
p
p
. .
1,
&
i
i
i
up i
i
low i
i
i
i
p
z
z
s t z
z
i
N
N











                    (5) 


---

Page 4

---

 
 
4
Using the Big M method, (5) is linearized as (6). 
,
,
p
p
i
i
i
up i
i
low i
p
A
A





                                  (6a) 








L
W
M
M
1
M
1
M
. .
M
M
1
M
1
M
1,
&
i
i
i
i
i
i
i
i
i
i
i
i
i
i
i
i
B
A
B
B
A
B
s t
B
A
B
B
A
B
B
B
i
N
N











































                    (6b) 
M is a big enough constant, A
+ 
i  and A
-
i are auxiliary variables to 
linearize (5), and B
+ 
i  and B
-
I are the corresponding binary vari-
ables.  
Accordingly, the inner-level problem is finally transformed 
into the solvable mixed-integer linear programming (MILP) 
problem from (7). 




L
W
*
L,
,
,
,
,
max
D
p
p
p
p
. . (3b), (3c), (6b)
i
i
i
up i
i
low i
i N
i
up i
i
low i
i N
x
A
A
A
A
s t

















F
I

          (7) 
Adding new extra variables in Yl and the corresponding 
constraints in (8c), the outer-level sub-model is shown in (8) 
with the fixed worst-case p
* 
L and p
* 
W provided by the solution of 
the inner-level problem. Therein, Linner represents the number 
of iterative calculations. 
L
'T
L
L
,
min
l




x
Y
X E
                                        (8a) 
L
. .
s t

X
                                                  (8b) 


*
G
W
*
*
L
L
W
(
)
(
)
0
0
1,2...















l
l
l
inner
sum
sum
l
L
C
D
E
F
H
I
p
p
Y
X p
p
Y
               (8c) 
Model (8) provides the determined load pickup decisions X
* 
L 
for model (7), and model (7) feeds back the worst-case condi-
tion for model (8). The final optimal robust result is obtained 
as long as the iterative calculations of (7) and (8) converge. 
It should be noted that the essence of solving the two-stage 
robust optimization is to find the worst-case condition of a 
selected load pickup decision. Then, based on the correspond-
ing constraints, the load pickup decision under the worst-case 
condition is updated. The proposed model-free method is in-
spired by this process. Optimization models in this section 
provide training data for neural networks used in the DL meth-
od that will be elaborated next. 
III.  DL BASED UNCERTAINTY HANDLING METHOD 
In this section, a DNN and CNN are designed and trained to 
replace the model optimization process. The DNN is used to 
determine the worst-case condition of a load pickup decision 
under uncertainties, while the CNN checks the corresponding 
security of the worst-case condition. 
A.  Find worst-case condition using DNN 
According to the Universal Approximation Theorem, the 
neural network has the ability to approximate any continuous 
functions [28]. For the optimization model, there is actually a 
complex function relationship between the input and output 
data. Therefore, theoretically, a DNN can mimic convex model 
optimization with considerable accuracy.  
As shown in Fig. 1, the input data to the DNN is the ex-
pected values of wind power output and the expected load 
pickup amount. The output data includes the worst-case condi-
tion of uncertain load and wind variables (p
* 
L and p
* 
W) and the 
corresponding generator output condition. The goal of the 
DNN is to generate the worst-case condition of a load pickup 
decision under uncertainties. The result will be used for securi-
ty checks. 
……
ReLU
……
ReLU
……
……
ReLU
Forward pass
W,1
E
W
W,N
E
…
L,1
E
W,2
E
L,2
E
…
L
L,N
E
……
W,1
p
W
W,N
p
…
L,1
p
…
L
L,N
p
G,1
p
G
G,N
p
…
G,1
q
G
G,N
q
…
Back-propagate error
min
max min
  
Fig. 1 Structure of DNN for robust load restoration 
1) DNN data processing  
The training data set for the DNN comes from two optimiza-
tion models in Section III. The first one is the inner-level sub-
model (7) and the second one is the original load restoration 
model (1) with fixed X
* 
L, p
* 
L and p
* 
W. The expected values of 
wind power output EW, i are obtained from system data. With a 
selected load pickup decision X
* 
L, the expected values of load 
EL, i can be determined. The selected load pickup decision X
* 
L 
is the one in the load pickup checklist (LPC) which will be in 
introduced later in Section V. A. The worst load amount p
* 
L and 
wind power output p
* 
W are the results of solving (7). Using 
fixed X
* 
L, p
* 
L and p
* 
W, model (1) becomes a linear programming 
(LP) form and provides generator output values pG and qG. 
In 
order 
to 
improve 
computational 
efficiency, 
a 
min_max_scaler transformation in (9) is applied to normalize 
the input and output data. Through the normalization, the val-
ues of the data are within the range of [0,1], which helps create 
a more regular search region for the faster convergence of the 
algorithm. In (9), D means the training data.  
  




0
,
,
L
W
S
min
(
,
)
max
min
i s
i s
D
D
i
N orN
s
N





D
D
D
   (9) 
In the DNN structure of Fig. 1, the neurons realize the affine 
transformation of the input (10), and active functions (11) 
bring nonlinearity. 


l
l
l
l
k
j
j
k
j J
z
x
b





                          (10) 


l
l
k
k
y
f z

                                (11) 
where z is the weighted aggregation of all the features of the 


---

Page 5

---

 
 
5
input x captured by neurons, y is final output of a layer, and w 
and b are weights and biases parameters. In this study, the rec-
tifier linear units (ReLU) function is used as the activation 
function. The ReLU function has the form: f(x) = max(x,0) 
which preserves strong generalization abilities and allows easy 
application of gradient-based methods [14]. 
2) Training DNN 
Getting well trained DNN is to find fine-tuned network pa-
rameters w, b using the back-propagation algorithm. The loss 
function minimizes the deviation between the data obtained 
from optimization models and the estimated value using the 
DNN. In this way, an accurate enough approximation of the 
optimization models can be achieved as long as the loss func-
tion value is small enough. 
The loss function (12), which implies the accuracy of the 
output of the DNN, is defined as the objective of the DNN 
training. Because the outputs are all continuous values, the 
mean squared error (MSE) loss function is applied: 










W
L
S
G
G
DNN
DNN
DNN
2
2
*
*
W,
W,
L, ,
L,
W
L
2
2
*
*
S
G,
G,
G,
G,
G
G
,
1
1
1
1
1
s
s
s
s
i
i
i s
i
i N
i N
s N
s
s
s
s
i
i
i
i
i N
i N
L
p
p
p
p
N
N
N
p
p
q
q
N
N






























b

(12) 
where the sample data p
s* 
L  and p
s* 
W and p
s* 
G  and q
s* 
G  are respec-
tively obtained from MILP model (7) and model (3) in the LP 
form as explained in the previous subsection, 1) DNN data 
processing. 
Accordingly, the first partial derivatives of the loss function 
(12) with respect to w and b are used. Following the chain rule, 
the gradient of updating weights and biases is found by (13). 
Then, the final result can be obtained through the gradient de-
scent search based iteration. 
Lay
Lay
Lay
N
1
1
N
1
N
2 ...


















l
l
l
i
i
i
i
l
i
i
i
y
y
L
y
y
              (13) 
i denotes the iteration number and y
l 
i  is the output of DNN 
layer l. The bias has the same updating form. 
With (13), the back-propagation algorithm uses the gradient 
to guide the updating of the neural network parameters toward 
the global optimum. Consequently, the well trained DNN can 
be built when the weights and biases are determined.  
3) Accuracy improvement 
In Fig.1, the first part of output replaces the result of max-
min optimization. According to the max-min optimization 
theory, the worst-case realization of polyhedral uncertainty is 
identified at the vertices. Therefore, this part of result can be 
further corrected to reach the nearby vertices. In other words, 
the DNN finds the result near the exact optinal point, and then 
the output data can be further moved to the optimal point using 
the optimization theory. In this way, the worst-case load 
amount p
* 
L  and wind power output p
* 
W obtained by the DNN 
can easily reach 100% accuracy. 
B.  Security check of worst-case condition using CNN 
The deep CNN is known for its strong automatic feature 
learning ability in processing data with a grid-like topology, 
e.g., image data. According to the AC PF calculation (14), 
state variables such as bus voltage magnitudes and bus voltage 
angles, are mainly related to neighboring variables and param-
eters. This characteristic makes power system state variables 
sparsely connected, similar to image pixels, which is especially 
suitable for the application of the deep CNN [22]. Accordingly, 
the CNN can provide AC PF results that can be used to check 
voltage and branch power flow securities. 
1) CNN structure 
The structure of the deep CNN for voltage and angle calcu-
lation is illustrated in Fig. 2. It consists of two convolutional 
(Conv) layers and a fully-connected (FC) layer. The convolu-
tional layers use function (15) to conduct convolution opera-
tions for feature extractions. The ReLU active functions (16) 
are used to add non-linearity. 




2
2
,
,
nm
n
nm
n
m
nm
nm
nm
nm
nm
n
nm
n
m
nm
nm
nm
nm
P
=V g
-V V
g
cosθ
+b sinθ
Q
V b
V V
g
sinθ
b cosθ
n m
N n
m








         (14) 


,
,
1,
1
1
1
m
n
i j
u v
i u
j v
u
v
z
x
b








                       (15) 


,
,
i j
i j
y
f
z

                               (16) 
where xi+u-1,j, zi+v-1,j and wu,v are a single unit (a single square in 
Fig. 2) of the input data, output data and convolution kernel 
square. m and n are the height and width of a filter. All the 
output units constitute a feature map which contains the ex-
tracted information using the m×n filter. With more filters, 
more feature maps can be generated to provide sufficient in-
formation for deep CNN model regression. 
...
...
...
ReLU
+
F: [3, 3, 1, 12]
D: [3, N]
Conv1
Paddin
g...
...
...
data
Padding
...
...
...
Input data
...
F: [3, 3, 12, 24]
D: [3, N, 12]
ReLU
+
D: [3, N, 24]
Conv2
Filter
Filter
Reshape
D: [1, 3×N×24]
FC1
...
+
D: [1, 2N]
...
...
...
...
...
...
...
D: [3×N×24, 2N]
B 
P 
Q
...
12
24
...
V
θ
...
 
Fig. 2 Structure of CNN for power flow calculation 
2) CNN data processing  
The input data is obtained by the DNN in the last subsection, 
and it contains bus active power injection vector P, bus 
reactive power injection Q and self-susceptance elements of 
bus susceptance matrix B. The output data contains bus 
voltage magnitude vector V and angel vector θ. Accordingly, 
the size of the input data [P; Q; B] for the deep CNN is 3×N, 
and the size of the output data [θ; V] is 1×2N. The 
min_max_scaler transformation in (9) is applied to normalize 
the data. The technique of zero-padding is applied to maintain 
the original size of the input data. 
3) Training CNN 


---

Page 6

---

 
 
6
The loss function (17) is defined as the objective of the 
CNN training. Therein, V
s* 
i  and θ
s* 
i are obtained by calculating 
(14) based on the system P-Q condition determined according 
to the DNN output data. 






S
CNN
CNN
CNN
2
2
*
*
S
,
1
1
s
s
s
s
i
i
i
i
s N i N
L
V
V
θ
θ
N
N















b
         (17) 
Similar to the DNN training process, the deep CNN is 
trained using the back-propagation method to find the fine- 
tuned network weight parameters and bias parameters. 
In short, the DL based uncertainty handling approach con-
sists of a DNN and a CNN. They are trained to mimic the 
model optimization and AC PF calculation. In a model-free 
way, the well-trained DNN can quickly determine the worst-
case condition, and the well-trained CNN can quickly provide 
the AC PF result of the worst-case condition. 
IV.  OPTIMAL ROBUST LOAD RESTORATION STRATEGY 
Two algorithms are developed in this section. The LPCG 
algorithm is designed to generate the load pickup checklist 
which helps capture the optimality. The OSG algorithm is used 
to realize on-line optimal robust load restoration acquisition in 
a DL based model-free way.  
A.  Load pickup checklist generation 
The load pickup decision takes the form of 0/1 combina-
tions representing the reconnection of load blocks. Therefore, 
a direct idea to find the optimal load pick up decision is to 
enumerate all the combinations and check their security con-
strains using the DL method described in Section III. The op-
timal robust decision is the one with the largest expected load 
pickup amount as well as no security violations. However, the 
number of combinations increases exponentially with the 
number of load blocks. For a large-scale system with numer-
ous load blocks, it is problematic to list and check all the com-
binations. Therefore, the LPCG algorithm is developed to help 
find the optimal robust load restoration strategy within a lim-
ited number of checks.  
In the load restoration process, frequency security is a rela-
tively strict constraint for the optimization model. Normally, 
the optimal result falls near the boundary of the frequency con-
straint. Since the frequency calculation is related to system 
active power, it can be used to find the upper bound of the 
total load pickup amount. In this paper, the linearized frequen-
cy calculation method [10], [24] is used to gives the upper 
bound of the total pickup load amount Lupp in (18). Other func-
tion relationships of load mount and frequency, such as [28], 
can also be effectively applied. 


G
W
max
W
upp
W,
, ,ini
G
,
(
)
j
i
i
j N
j i
i N
j
s
L
E
E
N
f
i










       (18) 
Using the simple optimization model (19), the load pickup 
combination with the smallest distance to the upper bound Lupp 
can be found as X
0 
L. This result is better than or equal to the 
optimal result, and it will be used as the first set of load pickup 
decisions in the LPC. 


L
2
upp
L,
L,
min
i
i
i N
E
x
L









                 (19) 
Holding X
0 
L, an LPC with the decreasing load pickup amount 
is generated using the LPCG algorithm.  
 
LPCG algorithm: Generate LPC 
Input: The maximum load pickup amount Lupp, the ac-
ceptable lower bound Lpick,low and the maximum number of 
combinations Imax. 
Output: LPC 
S1: Set the maximum load pickup amount Lupp as Lpick,upp.
Initialize LPC as{X
0 
L }. Set Istr=0. 
S2: for Istr from 0 to Imax do 
Set Lpick,upp = X
Istr 
L  EL. Solve model (20) 


L
2
pick,upp
L,
L,
min
i
i
i N
E
x
L









                        (20a)


L
pick,low
pick,upp
L,
 L,
. .
-
i
i
i N
s t L
E
x
L





          (20b)
and get the load pickup decision as X 
Istr+1 
L
. 
if X 
Istr+1 
L
is equal to X 
Istr 
L . 
    break; 
else 
    Update the LPC as {X
0 
L,X
1 
L…, X 
Istr+1 
L
}. Set Istr=
Istr +1. 
end 
end 
S3: Obtain the load pickup decision list {X
0 
L,X
1 
L…, X 
Istr 
 L }.  
 
Therein, σ in (20b) is a small enough constant (e.g. 1*10^(-
4)). The finally obtained LPC {} stores load pickup decisions 
with decreasing expected load recovery amounts. 
B.  On-line optimal robust strategy acquisition 
By now, the security check of a load pickup decision under 
uncertainties can be realized by DL methods, and a load 
pickup checklist has been generated. Since the load pickup 
decisions in the LPC are ordered from largest load pickup 
amount to the lowest one, the one-by-one security check can 
be performed, and the first feasible set is the optimal one with 
the largest load pickup amount. Moreover, because the worst-
case conditions of the decisions in LPC are considered using 
the DNN and CNN, the result is with the robustness to handle 
uncertainties. In order to apply the DNN, CNN and LPC in the 
restoration process, the OSG algorithm is designed to support 
the on-line load restoration with fast robust strategy generation. 
The whole methodology of the proposed method is shown in 
Fig. 3. The training of the DNN and CNN and the LPCG algo-
rithm are off-line pre-processing, while the application of the 
well-trained DNN and CNN and generated LPC is on-line. 
Without any optimization model being built and solved, the 
calculations in the OSG algorithm based on-line process can 
be extremely fast. Therefore, the optimal robust strategy ac-
quisition can be a real-time application, and the DL technique 


---

Page 7

---

 
 
7
enables the model-free on-line decision-making process to 
completely replace the two-stage robust optimization. 
 
OSG algorithm: Find the optimal robust result 
Input: LPC and well trained DNN and CNN 
Output: The optimal robust strategy [X 
* 
L, p
* 
G]. 
S1: Organize input data E
 
L and E
 
W for the well trained 
DNN, and get the worst-case condition containing [p
 
L, pw, p
G, q
 
G] for LPC.  
S2: Check frequency security based on (21) which fol-
lows same frequency calculation method of (18) and replac-
es expected values in (18) with corresponding worst-case 
values in [p
 
L, pw, p
 
G, q
 
G]. Delete infeasible load pickup deci-
sions in LPC and obtain an updated LPC2. 




G
ini
w
G
,
L
(
)












j
j N
j i
j
f
sum
s
s
N
um
i
p
p
p
 (21) 
S3: Define system P-Q condition, and apply the well-
trained CNN to get [θ, V] for LPC2. 
S4: for I from 0 to Imax2 do 
Get X 
I 
L from LPC2, and get the corresponding p
 
G,
[θI,VI] and SI of X 
I 
L. 
if voltage, branch flow and generator output limits 
are satisfied 
break; 
else 
                 I = I + 1. 
end 
S5: Obtain the optimal robust load restoration strategy 
from LPC2. 
 
Get LPC and select the first 
combination
Select the next 
vector in LPC2
Well trained DNN 
Well trained CNN
Obtain PF results
Obtain the worst-case P/Q 
conditions under uncertainty
Optimal robust load restoration strategy
N
Y
N
Y
Training 
DNN
Training 
CNN
Model-free on-line 
application
Obtain LPC2
Select the first vector in LPC
Frequency satisfied?
Delete the vector
Y
Select the first vector in LPC2
PF result feasible?
Off-line preprocessing
Obtain well trained DNN
Obtain well trained CNN
LPCG 
algorithm
Obtain LPC
Obtain data using model (7) and (1) 
Obtain data by calculating (14) 
Prepare frequency constraint (18)
OSG algorithm
 
Fig. 3 Flowchart of the DL based robust load restoration method 
 
V.  CASE STUDY 
In this section, the testing performances of the DNN and 
CNN are presented. Then, the LPCG algorithm and OSG algo-
rithm are applied to decide the optimal robust load restoration 
strategy. The results are evaluated and compared with the con-
ventional model-based method to demonstrate the advantages 
of the model-free method. 
Two modified systems are used: the five wind farms inte-
grated IEEE 30-bus system and ten wind farms integrated 
IEEE 118-bus system. 10% and 20% deviations from the ex-
pected values are used to determine the bound of polyhedral 
uncertainty sets of load amount and wind power output, re-
spectively. The optimization models were solved using 
CPLEX V12.5.1 on a computer with Intel(R) Core(TM) i7-
8550U CPU and 16 GB RAM. The DNN and CNN are built 
and trained using TensorFlow 1.15 implemented on Python 3.7. 
A.  Computation performance of DL method 
1) DNN training and test results 
A DNN with 3 hidden layers is designed to find the worst-
case condition. The neuron number is 1000, and the learning 
rate is 0.001. The size of the training data for the IEEE 30-bus 
system is 1500 while the size of the test data is 500. For the 
IEEE 118-bus system, the training data size and test data size 
are 8000 and 2000, respectively. The training/test data is gen-
erated using MILP model (7) and model (1) in LP form as 
explained in Section III A 1). For the IEEE 30-bus system, the 
number of inputs is 35 including expected load pickup 
amounts at 30 nodes and expected wind power output amounts 
at 5 nodes. The corresponding number of outputs is 55 includ-
ing load pickup amount, wind power output and generator out-
put in the worst-case condition. For the IEEE 118-bus system, 
numbers of inputs and outputs are 128 and 166. In the DNN, 
the input data represents a selected load pickup decision and 
the output data shows the worst-case P-Q condition in the sys-
tem under uncertainties.  
Table I shows the training result of the DNN for two sys-
tems. As shown in Fig. 4, after 200 iterations, the training loss 
value for the small-scale first system is 0.000026 which is 
small enough to indicate the training convergence. The final 
accuracies in training set and test set are respectively 99.45% 
and 99.38%, which verify the considerable accuracy of DNN 
regression.  
TABLE I. TRAINING RESULTS OF DNN 
Case 
Iteration Loss value 
Train  
Test 
IEEE-30 
200 
0.000026 
99.45% 
99.38% 
IEEE-118 
 500 
0.000309 
98.40% 
96.48% 
 
Iteration
Loss value of IEEE 30-bus 
system (p.u.)
Loss value per iteration
Iteration
Loss value of IEEE 118-bus 
system (p.u.)
Loss value per iteration
 
Fig. 4 Regression of the worst-case using DNN 
 
Using the same DNN structure, the training loss value for 
the second system is 0.000309 after 500 iterations. The corre-
sponding accuracies are 98.40% and 96.48% for training data 
and test data, respectively. If needed, the test accuracy can be 
further improved by adding L2 regularization in the loss func-
tion. Here, because the worst-case condition will be corrected 


---

Page 8

---

 
 
8
later, this accuracy is acceptable and it has limited effect on 
the final result.  
2) Worst-case condition correction 
The output of the DNN provides a result near the optimal 
point. The result can be further corrected to the strictly optimal 
points of the max-min robust model. According to the optimi-
zation principle, the worst-case realization is identified at the 
vertices for polyhedral uncertainty. Taking five DNN exam-
ples for example, Fig. 5 shows the correction process. The 
DNN results (blue points) are further moved to nearby vertices 
(red points). Through the correction, the accuracy of worst-
case load amount and wind power output can reach 100%, 
which benefits the later security check. 
 
-5
5
15
25
35
DNN result
Corrected result
Sample1
Sample2
Sample3
Sample4
Sample5
Wind power& load amount (MV)
 
Fig. 5. Further correction of DNN result 
 
3) CNN training and test results 
The CNN with two convolutional (Conv) layers and one ful-
ly-connected (FC) layer is designed to realize an AC PF based 
security check. The filter of Conv1 has the size [3, 3, 1, 12] 
and the one of Conv2 has the size [3, 3, 12, 24]. The FC layer 
has 3000 neurons. The learning rate is 0.001. Numbers of input 
and output data are 3×33 and 66 for the first system and 3×118 
and 236 for the second system. The input data is the 
susceptance matrix B and the worst-case P-Q system condition 
obtained according to the output data of DNN. The output is 
the voltage and angle of each node in the system generated 
using MATPOWER.  
 
TABLE II. TRAINING RESULTS OF CNN 
Case 
Train 
size/test size Loss value Train_V Test_V 
Train_θ 
Test_θ 
IEEE-30 
1500/500 
0.000134 
99.82% 99.79% 99.82% 98.92% 
IEEE-118  8000/2000 
0.000199 
99.82% 99.82% 99.82% 99.65% 
 
Iteration
Iteration
train
test
train
test
Voltage error (p.u.)
Theta error (p.u.)
Voltage error per iteration
Theta error per iteration
Fig. 6. Regression of AC PF of IEEE 30-bus system using CNN 
Table II shows the training result of the CNN. Iteration pro-
cesses for the two systems are shown in Fig. 6 and Fig. 7. Af-
ter 500 iterations, the accuracies of obtained voltage and angle 
are around 99% which satisfies the security check.  
 
Iteration
Iteration
train
test
train
test
Voltage error (p.u.)
Theta error (p.u.)
Voltage error per iteration
Theta error per iteration
 
Fig. 7. Regression of AC PF of IEEE 118-bus system using CNN 
B.  Load restoration performance of model-free method 
The off-line training of the DL based model-free method 
can be completed by the process above. Then, the LPCG algo-
rithm is used to generate the LPC. 
1) LPC generation 
As shown in Fig. 8, the LPC gives several combinations of 
load pickup decisions from the largest amount to the lowest 
amount. The combinations become a LPC which will be 
checked one-by-one using the OSG algorithm. The computa-
tion time of generating sixty LPCs is 10.12s for the first sys-
tem, and 1074.15s for the second system. It is acceptable be-
cause the LPC can be prepared off-line.  
 
0
10
20
30
40
50
60
70
80
90
100
110 118
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
Load pickup amount (MW)
LPC number
Fig. 8. Load checkup list for IEEE 118-bus system 
 
2) OSG based strategy generation 
TABLE III. LOAD RESTORATION PERFORMANCE OF IEEE 30-BUS SYSTEM 
 
Method 
Step1 
Step2 
Step3 
Load pickup 
OSG 
 65.68% 
 84.15% 
100% 
 
C&CG 
 63.18% 
 83.81% 
100% 
Comp. time 
OSG 
0.08s 
0.11s 
0.09s 
 
C&CG 
87.67s 
71.42s 
69.54s 
 
Applying the OSG algorithm, the well-trained DNN and 
CNN as well as the LPC will be used to realize the on-line 
robust load restoration strategy acquisition. The load restora-
tion performance of the proposed model-free method is com-
pared with the conventional C&CG based two-stage robust 
optimization in [12], [13]. Table III shows the multi-step per-
formance of the IEEE 30-bus system. As can be seen, the res-
torations using both methods are all completed with three steps, 
while the model-free method is with slightly higher recovered 
load amount. Moreover, the model-free one has the obvious 
advantage in terms of calculation time. The model-based opti-
mization method needs an average 76.21s to solve the two-
stage robust load restoration model using C&CG algorithm,  
 


---

Page 9

---

 
 
9
Model-free
Optimization
Node
Pickup decision
...
LPC1
LPC2
Frequency violation
Load amount
Low
High
0
L
X
str
L
I
X
1
L
X
Voltage/branchflow/generati
on violation
...
...
32
L
X
Selected decision
0
8
16
24
32
40
48
56
64
72
80
88
96
104
112 118
0
1
 
Fig. 9. Load pickup decisions of IEEE 118-bus system 
 
while the model-free one uses DL and LPC to achieve hun-
dreds of times acceleration in computational time (Comp.  
time).  
The calculation benefit is more obvious with large-scale sys-
tems. Fig. 9 shows the load pickup decisions of model-based 
and model-free methods and the process of final decision ac-
quisition of the IEEE 118-bus system. The final strategy is the 
32nd set in the LPC, which is the result of deleting former sets 
because of frequency, voltage, branch flows and generation 
violations. The optimization method takes 1549.71 s to reach 
the optimal robust load pickup strategy which restores 64 load 
blocks totaling 3577 MW. With the same security require-
ments, the proposed model-free method finds that the robust 
strategy restores 62 load blocks totaling 3588 MW in 0.24s. 
Compared with the optimization method, the model-free meth-
od adjusts load pickup decisions in 8 nodes with a 0.31% load 
amount increment. More important, it has more than 6000 
times computational acceleration (Comp. accel) than the opti-
mization one. Accordingly, the proposed model-free method 
has predominant computation speed and good optimization 
ability, which satisfies the on-line application. 
 
TABLE IV. LOAD RESTORATION PERFORMANCE OF IEEE 118-BUS SYSTEM 
 
Load recovery Recovered 
load blocks Comp. time Comp. accel. 
OSG 
3588MW 
62 
0.24s 
6457.13 
times 
C&CG 
3577MW 
64 
1549.71s 
 
VI.  CONCLUSION 
The time-consuming calculation of the conventional model-
based method limits the robust scheme to the off-line applica-
tion. In order to realize on-line robust load restoration, this 
paper proposes a new DL based model-free method. A series 
of techniques, the DNN, deep CNN, LPCG algorithm and 
OSG algorithm, are developed and combined in order to com-
pletely replace the two-stage robust optimization. The de-
signed DL method is with considerable accuracy for the worst-
case condition capture and security check. The proposed 
LPCG algorithm helps maintain the optimization performance, 
and the OSG algorithm realizes fast on-line optimal robust 
load restoration acquisition. The case study results show dis-
tinguished computation benefits and satisfactory load restora-
tion performance of the proposed method. The DL based mod-
el-free method fills the gap between the robust load restoration  
scheme and the on-line application, which further enhances 
bulk system resilience. 
REFERENCES 
[1] Department of Energy (DoE). Insurance as a risk management 
instrument for energy infrastructure security and resilience, Mar. 2013. 
[Online]. 
Available: 
http://energy.gov/oe/downloads/insurancerisk-
management-instrument-energy-infrastructure-security-and-resilience 
[2] M. Adibi, P. Clelland, L. Fink, H. Happ, R. Kafka, J. Raine, D. Scheurer 
and F. Trefny, “Power system restoration - a task force report,” IEEE 
Trans. Power Syst., vol. 2, no. 2, pp. 271-277, 1987.   
[3] N.A. Fountas, N.D. Hatziargyriou, C. Orfanogiannis and A. Tasoulis, 
“Interactive long-term simulation for power system restoration plan-
ning,” IEEE Trans. Power Syst., vol, 12 no. 1, pp. 61 –68, 1997. 
[4] F. Qiu and P. Li, “An integrated approach for power system restoration 
planning,” Proc. IEEE, vol. 105, no. 7, pp. 1234-1252, 2017.  
[5] W. Sun, C.-C. Liu, and L. Zhang, “Optimal start-up strategy for bulk 
power system restoration,” IEEE Trans. Power Syst., vol. 26, no. 3, pp. 
1357–1366, Aug. 2011. 
[6] J. Zhao, H. Wang, Y. Liu, R. Azizipanah-Abarghooee and V. Terzija, 
“Utility-oriented on-line load restoration considering wind power pene-
tration,” IEEE Trans. Sustain. Energy, vol. 10, no. 2, pp. 706–717, 
2019. 
[7] Z. Qin, Y. Hou, C. C. Liu, et al. “Coordinating generation and load 
pickup during load restoration with discrete load increments and reserve 
constraints,” IET Gener. Transm. Distrib., vol. 9, no. 15, pp. 2437-2446, 
2015. 
[8] A. Gholami, F. Aminifar, “A hierarchical response-based approach to 
the load restoration problem,” IEEE Trans. Smart Grid, no. 99, pp. 1-10, 
Dec. 2015. 
[9] L. Sun, C. Peng, J. Hu and Y. Hou, “Application of type 3 wind turbines 
for system restoration,” IEEE Trans. Power Syst., vol. 33, no. 3, pp. 
3040-3051, 2018. 
[10] A. Golshani, W. Sun, Q. Zhou, Q. P. Zheng and Y. Hou, “Incorporating 
wind energy in power system restoration planning,” IEEE Trans. Smart 
Grid, vol. 10, no. 1, pp. 16-28, 2019. 
[11] H. Gao, Y. Chen, Y. Xu and C. C. Liu, “Resilience-oriented critical load 
restoration using microgrids in distribution systems,” IEEE Transac-
tions on Smart Grid, vol. 7, no. 6, pp. 2837-2848, 2017. 
[12] A. Golshani, W. Sun, Q. Zhou, Q. P. Zheng, J. Wong and F. Qiu, “Co-
ordination of wind farm and pumped-storage hydro for a self-healing 
power grid,” IEEE Trans. Sustain. energy, vol. 9, no. 4, pp. 1910-1920, 
2018. 
[13] J. Zhao, H. Wang, Y. Hou, Q. Wu, N. D. Hatziargyriou and W. Zhang, 
"Robust distributed coordination of parallel restored subsystems in wind 
power penetrated transmission system," IEEE Trans. Power Syst., vol. 
35, no. 4, pp. 3213-3223, 2020. 
[14] I. Goodfellow, Y. Bengio, and A. Courville, “Deep Learning,” Cam-
bridge: MIT press, 2016, pp. 152 - 231. 
[15] F. Li and Y. Du, "From AlphaGo to power system AI," IEEE Power and 
Energy magazine, vol. 16, issue 2, pp. 76-84, 2018. 
[16] X. Kou, Y. Du, F. Li, H. Pulgar-Painemal, et al, "Model-Based and 
Data-Driven HVAC Control Strategies for Residential Demand Re-
sponse," IEEE Open Access Journal of Power and Energy, vol. 8, pp. 
186-197, 2021. 


---

Page 10

---

 
 
10
[17] Y. Du, F. Li, H. Zandi, Y. Xue, "Approximating Nash Equilibrium in 
Day-ahead Electricity Market Bidding with Multi-Agent Deep Rein-
forcement Learning," Journal of Modern Power Systems and Clean En-
ergy, vol. 9, no. 3, pp. 534-544, 2021. 
[18] J. Yan, H. Zhang, Y. Liu, S. Han, L. Li, and Z. Lu, “Forecasting the 
high penetration of wind power on multiple scales using multi-to-multi 
mapping,” IEEE Trans. Power Syst., vol. 33, pp. 3276-3284, 2018. 
[19] Y. Chen, Y. Wang, D. Kirschen, and B. Zhang, “Model-free renewable 
scenario generation using generative adversarial networks,” IEEE Trans. 
Power Syst., vol. 33, pp. 3265-3275, 2018. 
[20] Y. Du and F. Li, “Intelligent multi-microgrid energy management based 
on deep neural network and model-free reinforcement Learning,” IEEE 
Transactions on Smart Grid, vol. 11, no. 2, pp. 1066-1076, 2019. 
[21] W. Li, D. Deka, M. Chertkov and M. Wang, “Real-time faulted line 
localization and PMU placement in power systems through convolu-
tional neural networks,” IEEE Trans. on Power Syst., vol. 34, no. 6, pp. 
4640-4651, 2019. 
[22] Y. Du, F. Li, J. Li, and T. Zheng, “Achieving 100x acceleration for N-1 
contingency screening with uncertain scenarios using deep convolution-
al neural network,” IEEE Trans. Power Syst., vol. 34, pp. 3303-3305, 
2019. 
[23] A. S. Bretas and A. G. Phadke, “Artificial neural networks in power 
system restoration,” IEEE Trans. Power Deliv., vol. 18, no.4, pp. 1181-
1186, 2003. 
[24] PJM Manual 36: System Restoration. 2020. [Online]. Available: 
https://www.pjm.com/~/media/documents/manuals/m36.ashx. 
[25] M. M. Adibi, J. N. Borkoski, R. J. Kafka, et al., “Frequency response of 
prime movers during restoration,” IEEE Trans. Power Syst, vol.14, no.2, 
pp. 751-756, May. 1999. 
[26] J. Zhao, H. Wang, Y. Liu, Q. Wu, Z. Wang and Y. Liu, “Coordinated 
restoration of transmission and distribution system using decentralized 
scheme,” IEEE Trans. Power Syst., vol. 34, no. 5, pp. 3428-3442, 2019. 
[27] L. Zhao and B. Zeng, “Robust unit commitment problem with demand 
response and wind energy,” IEEE PES General Meeting, pp. 1-8, 2012. 
[28] A visual proof that neural nets can compute any function. [Online]. 
Available: http://neuralnetworksanddeeplearning.com/chap4.html. 
[29] D. R. Medina, E. Rappold, O. Sanchez, et al. “Fast assessment of fre-
quency response of cold load pickup in power system restoration,” IEEE 
Trans. Power Syst, vol. 31, no. 4, pp. 3249-3256, 2016. 
