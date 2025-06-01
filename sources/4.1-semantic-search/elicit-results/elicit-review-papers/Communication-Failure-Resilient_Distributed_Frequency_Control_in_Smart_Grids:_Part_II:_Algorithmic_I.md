

---

Page 1

---

1
Optimal load-side control for frequency
regulation in smart grids
Enrique Mallada, Changhong Zhao, and Steven Low
Abstract
Frequency control rebalances supply and demand while maintaining the network state within operational margins.
It is implemented using fast ramping reserves that are expensive and wasteful, and which are expected to grow with
the increasing penetration of renewables. The most promising solution to this problem is the use of demand response,
i.e. load participation in frequency control. Yet it is still unclear how to efﬁciently integrate load participation without
introducing instabilities and violating operational constraints.
In this paper we present a comprehensive load-side frequency control mechanism that can maintain the grid within
operational constraints. In particular, our controllers can rebalance supply and demand after disturbances, restore the
frequency to its nominal value and preserve inter-area power ﬂows. Furthermore, our controllers are distributed (unlike
the currently implemented frequency control), can allocate load updates optimally, and can maintain line ﬂows within
thermal limits. We prove that such a distributed load-side control is globally asymptotically stable and robust to
unknown load parameters. We illustrate its effectiveness through simulations.
I. INTRODUCTION
Frequency control maintains the frequency of a power network at its nominal value when demand or supply
ﬂuctuates. It is traditionally implemented on the generation side and consists of three mechanisms that work in
concert [1]–[3]. The primary frequency control, called the droop control and completely decentralized, operates on
a timescale up to low tens of seconds and uses a governor to adjust, around a setpoint, the mechanical power input
to a generator based on the local frequency deviation. The primary control can rebalance power and stabilize the
frequency but does not restore the nominal frequency. The secondary frequency control (called automatic generation
control or AGC) operates on a timescale up to a minute or so and adjusts the setpoints of governors in a control
area in a centralized fashion to drive the frequency back to its nominal value and the inter-area power ﬂows to
their scheduled values. Finally, economic dispatch operates on a timescale of several minutes or up and schedules
the output levels of generators that are online and the inter-area power ﬂows. See [4], [5] for a recent hierarchical
model of power systems and their stability analysis.
This work was supported by NSF NetSE grant CNS 0911041, ARPA-E grant de-ar0000226, Southern California Edison, National Science
Council of Taiwan R.O.C. grant NSC 103-3113-P-008-001, and Caltech Resnick Institute.
The authors are with the Department of Computing + Mathematical Sciences, California Institute of Technology, Pasadena, CA 91125 USA
(e-mail: {mallada,czhao,slow}@caltech.edu).
arXiv:1410.2931v3  [math.OC]  17 Nov 2015


---

Page 2

---

2
Load-side participation in frequency control offers many advantages, including faster response, lower fuel con-
sumption and emission, and better localization of disturbances. The idea of using frequency adaptive loads dates
back to [6] that advocates their large scale deployment to “assist or even replace turbine-governed systems and
spinning reserve.” They also proposed to use spot prices to incentivize the users to adapt their consumption to the
true cost of generation at the time of consumption. Remarkably it was emphasized back then that such frequency
adaptive loads will “allow the system to accept more readily a stochastically ﬂuctuating energy source, such as
wind or solar generation” [6].
This is echoed recently in, e.g., [7]–[13] that argue for “grid-friendly” appliances, such as refrigerators, water or
space heaters, ventilation systems, and air conditioners, as well as plug-in electric vehicles to help manage energy
imbalance. Simulations in all these studies have consistently shown signiﬁcant improvement in performance and
reduction in the need for spinning reserves. A small scale project by the Paciﬁc Northwest National Lab in 2006–
2007 demonstrated the use of 200 residential appliances in primary frequency control that automatically reduce
their consumption when the frequency of the household dropped below a threshold (59.95Hz) [14]. Although these
simulation studies and ﬁeld trials are insightful, they fall short in predicting the (potential) behavior of a large-scale
deployment of frequency control.
This has motivated the recent development of new analytic studies assessing the effect of distributed frequency
control in power systems [15]–[22], and microgrids [23]–[27], which can be grouped into three main approaches.
The ﬁrst approach builds on consensus algorithms to provide efﬁciency guarantees to classical PI controllers [15],
[16], [24]–[27]. It achieves efﬁciency but does not manage congestion, i.e., it does not enforce constraints such
as thermal limits. The second approach reverse engineers the network dynamics as a primal-dual algorithm of an
underlying optimization problem, and then add constraints and modiﬁes the objective function while preserving the
primal-dual interpretation of the network dynamics [19]–[22], [28]. It successfully achieves efﬁciency but it limits
the type of operational constraints that can be satisﬁed. The third approach directly formulates an optimization
problem that encodes all operational constraints and then designs a hybrid algorithm that combines the network
dynamics with a subset of the primal-dual algorithm [17], [18]. It is able to satisfy operational constraints, but the
stability depends on the network parameters.
Contributions of this work: In this paper we develop a method to achieve secondary frequency regulation and
congestion management (bringing line ﬂows to within their limits), in a distributed manner using controllable
loads. To contrast with the generation-side AGC frequency control, we refer to our solution as load-side control.
To our knowledge, this method produces the ﬁrst distributed controllers for demand response that are scalable
and enforce required operational constraints for frequency regulation, such as restoring nominal frequency and
preserving inter-area ﬂows, while respecting line limits.
Our work builds on previous optimization-based approaches [17]–[22], [28]. The crux of our solution is the
introduction of virtual (line) ﬂows that can be used to implicitly constrain real ﬂows without altering the primal-
dual interpretation of the network dynamics. A virtual ﬂow is a cyber quantity on each line that a controller
computes based on information from its neighbors. In steady state, its value equals the actual line ﬂows incident


---

Page 3

---

3
on that controller. This device allows us to impose arbitrary constraints on the (actual) line ﬂows for congestion
management and restoring inter-area ﬂows, while retaining the ability to exploit network dynamics to help carry
out the primal-dual algorithm.
Our contribution with respect to the existing literature is manifold. Unlike [16]–[18], our global asymptotic
stability result (Theorem 10 in Section IV) is independent of the controller gains, which is highly desirable for
fully distributed deployments. Our results hold for arbitrary topologies, in contrast with [17], [25], and can impose
inter-area constraints, thermal limits or any linear equality or inequality constraint in the line ﬂows. Moreover, we
provide a convergence analysis in the presence of unknown parameters (Section V) that is novel in the primal-dual
literature and provides the necessary robustness for large scale distributed deployments. Finally, our framework can
further extend to include intermediate buses without generators or loads – quite common in transmission networks
– which are not considered by the existing literature, and to fully distribute non-local constraints like those imposed
on inter-area ﬂows (Section VI).
A preliminary version of this work has been presented in [29]. This paper extends [29] in several ways. First, the
robustness study of our controllers with respect to uncertain load parameter (Section V) as well as the framework
extensions (Section VI) are new. Second, we include detailed proofs that were omitted in [29] due to space
constraints. Finally, we extend our simulations in Section VII to further illustrate the conservativeness of the
uncertainty bounds of Theorem 14.
II. PRELIMINARIES
Let R be the set of real numbers and N the set of natural numbers. Given a ﬁnite set S ⊂N we use |S|
to denote its cardinality. For a set of scalar numbers ai ∈R, i ∈S, we denote aS to its column vector, i.e.
aS := (ai)i∈S ∈R|S|; we usually drop the subscript S when the set is known from the context. For two vectors
a ∈R|S| and b ∈R|S′| we deﬁne the column vector x = (a, b) ∈R|S|+|S′|. Given a matrix A, we denote its
transpose as AT and use Ai to denote the ith row of A. We will also use AS to denote the sub matrix of A composed
only of the rows Ai with i ∈S. The diagonal matrix of a sequence {ai, i ∈S} is represented by diag(ai)i∈S.
Similarly, for a sequence of matrices {Ah, h ∈S} we let blockdiag(Ah)h∈S denote the block diagonal matrix.
Finally, we use either 1n and 1n×m (0n and 0n×m) to denote the vector and matrix of all ones (zeros), or 1 (0)
when its dimension is understood from the context.
For a function f : Rn →Rn we use f ′(x) :=
∂
∂xf(x) to denote the Jacobian and f −1 to denote its inverse.
When n = 1, f ′′(x) denotes the second derivative
∂2
∂x2 f(x).
For given vectors u ∈Rn and a ∈Rn, and set S ⊆{1, . . . , n}, the operator [a]+
uS is deﬁned element-wise by
([a]+
uS)i =





[ai]+
ui,
if i ∈S,
ai,
if i ̸∈S,
(1)
where [ai]+
ui is equal to ai if either ai > 0 or ui > 0, and 0 otherwise. Whenever u∗
S ≥0, the following relation
holds:
(uS −u∗
S)T [aS]+
uS ≤(uS −u∗
S)T aS
(2)


---

Page 4

---

4
since for any pair (ui, ai), with i ∈S, that makes the projection active ([ai]+
ui = 0) we must have ui ≤0 and
ai ≤0, and therefore (ui −u∗
i )ai ≥0 = (ui −u∗
i )T [ai]+
uS.
A. Network Model
We consider a power network described by a directed graph G(N, E) where N = {1, ..., |N|} is the set of buses,
denoted by either i or j, and E ⊂N × N is the set of transmission lines denoted by either e or ij such that if
ij ∈E, then ji ̸∈E.
We partition the buses N = G ∪L and use G and L to denote the set of generator and load buses respectively. We
assume that a generator bus may also have loads attached to it, but not otherwise. We assume the graph G(N, E)
is connected, and make the following assumptions which are standard and well-justiﬁed for transmission networks
[30]: (i) Bus voltage magnitudes |Vi| = |Vj| = 1pu for i, j ∈N. (ii) Lines ij ∈E are lossless and characterized
by their susceptances Bij > 0. (iii) Reactive power ﬂows do not affect bus voltage phase angles and frequencies.
The evolution of the transmission network is described by
˙θi =ωi
i ∈N
(3a)
Mi ˙ωi =P in
i −(di+Diωi)−P
j∈NiBij(θi−θj)
i ∈G
(3b)
0=P in
i −(di+Diωi)−P
j∈NiBij(θi−θj)
i ∈L
(3c)
where di denotes an aggregate controllable load, Diωi denotes the aggregate frequency sensitive consumption due
to uncontrollable but frequency-sensitive loads and/or generators’ damping loss. Mi denotes the generator’s inertia,
and P in
i
is the difference between mechanical power injected by a generator and the constant aggregate power
consumed by loads. Notice that for load buses (i ∈L) P in
i
< 0.
Equation (3) represents the standard swing equations when the bus frequency ωi and phase θi are close to nominal
values ω0 and θ0
i .1 Given (3), however, our results hold for arbitrary ωi and θi. By letting Pe = Pij := Bij(θi−θj)
for e = ij ∈E, we can equivalently rewrite (3) as
Mi ˙ωi =P in
i
−(di + Diωi) −P
e∈E Ci,ePe
i ∈G
(4a)
0=P in
i
−(di + Diωi) −P
e∈E Ci,ePe
i ∈L
(4b)
˙Pij =Bij(ωi −ωj)
ij ∈E
(4c)
where Ci,e are the elements of the incidence matrix C ∈R|N |×|E| of the graph G(N, E) such that Ci,e = −1
if e = ji ∈E, Ci,e = 1 if e = ij ∈E and Ci,e = 0 otherwise, and the line ﬂows initial condition must satisfy
Pij(0) = Bij(θ0
i −θ0
j).
Remark 1. Our model assumes that every bus has both Di >0 and controllable load di. While this is reasonable
for load and generator buses (for i ∈G the generator can implement −di), it is unreasonable for intermediate
1Without loss of generality, we take here ω0 = 0.


---

Page 5

---

5
buses that have neither generators nor loads. This is addressed in Section VI. Our framework can also handle the
case where di is present only for i ∈S ⊂N. This case is omitted due to space constraints.
B. Operational Constraints
We denote each control area using k and let K := {1, . . . , |K|} be the set of all areas in the network. Let Nk ⊆N
be set of buses in area k and Bk ⊆E the set of boundary edges of area k, i.e. ij ∈Bk iff either i ∈Nk or j ∈Nk,
but not both.
Within each area, the AGC scheme seeks to restore the frequency to its nominal value and preserve a constant
power transfer outside the area, i.e.
P
ij∈Bk ˆCk,ijPij = ˆPk
(5)
where ˆCk,ij is equal to 1, if i ∈Nk, −1, if j ∈Nk, and ˆPk is the net scheduled power injection of area k.
By deﬁning ˆCk,ij to be 0 whenever ij ̸∈Bk we can also relate ˆC ∈R|K|×|E| with C ∈R|N |×|E| using
ˆC = EKC
(6)
where EK := [e1 . . . e|K|]T and ek ∈R|N|, k ∈K, is a vector with elements (ek)i = 1 if i ∈Nk and (ek)i = 0
otherwise.
Finally, the thermal limit constraints are usually given by
P ≤P ≤P
(7)
where P := (Pe)e∈E, P := (P e)e∈E and P := (P e)e∈E represent the line ﬂow limits; i.e. P = −P so that |P| ≤P.
III. OPTIMAL LOAD-SIDE CONTROL
Suppose the system (4) is in equilibrium, i.e. ˙ωi = 0 for all i and ˙Pij = 0 for all ij, and at time 0, there is a
disturbance, represented by a step change in the vector P in := (P in
i )i∈N , that produces a power imbalance. Then,
we are interested in designing a distributed control mechanism that rebalances the system, restores the frequency
to its nominal value while maintaining the operational constraints of Section II-B. Furthermore, we would like this
mechanism to produce an efﬁcient allocation among all the users (or loads) that are willing to adapt.
We use ci(di) to denote the cost or disutility of changing the load consumption by di. This allows us to formally
describe our notion of efﬁciency in terms of the loads’ power share. More precisely, we shall say that a load control
is efﬁcient if in equilibrium solves the Optimal Load Control (OLC) problem:
Problem 1 (OLC).
minimize
d,ω,θ
X
i∈N
ci(di)
(8a)
subject to
P in −(d + Dω) = LBθ
(8b)


---

Page 6

---

6
ω = 0
(8c)
ˆCBCT θ = ˆP
(8d)
P ≤BCT θ ≤P
(8e)
where d = (di)i∈N , ω = (ωi)i∈N , θ = (θi)i∈N , D = diag(Di)i∈N , B = diag(Bij)ij∈E, (BCT θ)ij = Bij(θi −θj)
and LB := CBCT is the Bij-weighted Laplacian matrix.
Throughout this paper we make the following assumptions:
Assumption 1 (Cost function). The cost function ci(di) is α-strongly convex and second order continuously
differentiable (ci ∈C2 with c′′
i (di) ≥α > 0) in the interior of its domain Di := [di, di] ⊆R, such that
ci(di) →+∞whenever di →∂Di.
Assumption 2 (Strict feasibility in D). The OLC problem (9) is feasible and there is at least one feasible (d, ω, θ)
such that d ∈Int D := Π|N|
i=1Int Di.
Assumption 2 guarantees that, even in the presence of Assumption 1, the optimal solution of OLC is ﬁnite, and
therefore allows us to use the KKT conditions [31, Ch. 5.2.3] to characterize it.
Problem 1 is convex and therefore can be efﬁciently solved using several optimization algorithms. However,
unlike standard optimization problems, we can only modify the loads di while θi and ωi react to these changes
according to (3). We overcome these restrictions by formulating an equivalent optimization problem whose primal-
dual optimization algorithm embeds the line ﬂow version of the swing equations (4).
A. Virtual Flows Reformulation
We now proceed to describe the optimization problem that will be used to derive the distributed controllers that
achieve our goals. The crux of our solution comes from implicitly imposing the constraints (8c)-(8e) by using
virtual ﬂows instead of explicitly using ωi and θi. This, together with an additional quadratic objective on ωi and
substituting Bij(θi −θj) with Pe in (8b), allows us to embed the network dynamics as part of the primal-dual
algorithm while preserving all the desired constraints.
Problem 2 (VF-OLC).
minimize
d,ω,φ,P
X
i∈N
ci(di)+Diωi2
2
(9a)
subject to
P in −(d + Dω) = CP
(9b)
P in −d = LBφ
(9c)
ˆCBCT φ = ˆP
(9d)


---

Page 7

---

7
P ≤BCT φ ≤P
(9e)
where φ = (φi)i∈N represents the virtual phases and (BCT φ)ij = Bij(φi −φj) is the corresponding virtual ﬂow
through line ij ∈E.
Although not clear at ﬁrst sight, the constraint (9c) implicitly enforces that any optimal solution of VF-OLC
(d∗, ω∗, φ∗, P ∗) will restore the frequency to its nominal value, i.e. ω∗
i = 0. Thus the additional term on the
objective function does not inﬂuence the optimal solution. Similarly, we will use constraint (9d) to impose (8d) and
(9e) to impose (8e).
We use νi, λi and πk to denote the Lagrange multipliers of constraints (9b), (9c) and (9d), and ρ+
ij and ρ−
ij as
multipliers of the right and left constraints of (9e), respectively. In order to make the presentation more compact
sometimes we will use x = (φ, P) ∈R|N |+|E| and σ = (λ, ν, π, ρ+, ρ−) ∈R2|N |+|K|+2|E|, as well as ρ :=
(ρ+, ρ−).
Using this notation we can write the Lagrangian of VF-OLC as
L(d, ω, x, σ) =
X
i∈N
Å
ci(di) + Diωi2
2
ã
+ νT (P in −(d + Dω)
−CP) + λT (P in −d −LBφ) + πT ( ˆCBCT φ −ˆP)
+ ρ+T (BCT φ −P) + ρ−T (P −BCT φ)
=
X
i∈N
ci(di)−(λi + νi)di+Diωi (ωi/2 −νi)+(νi + λi)P in
i
−P T CT ν −φT (LBλ −CB ˆCT π −CB(ρ+ −ρ−))
−πT ˆP −ρ+T P + ρ−T P
(10)
The next lemmas characterize the optimality conditions of VF-OLC and its equivalence with OLC. Their proofs
can be found in the Appendix.
Lemma 2 (Optimality). Let G(N, E) be a connected graph. Then (d∗, ω∗, φ∗, P ∗, σ∗) is a primal-dual optimal
solution to VF-OLC if and only if (d∗, ω∗, φ∗, P ∗) is primal feasible, ρ+∗, ρ−∗≥0,
ω∗
i = ν∗
i , d∗
i = c′−1
i
(ν∗
i + λ∗
i ), ν∗
i = ˆν, i ∈N,
(11)
where c′−1
i
is the inverse of the derivative of ci, ˆν is some scalar,
P
j∈Ni Bij(λ∗
j −λ∗
i ) + CiB( ˆCT π∗+ ρ+∗−ρ−∗) = 0
(12)
with Ci being the ith row of C, and
ρ+∗
ij (Bij(φ∗
i −φ∗
j) −P ij) = 0,
ij ∈E,
(13a)
ρ−∗
ij (P ij −Bij(φ∗
i −φ∗
j)) = 0,
ij ∈E.
(13b)
Moreover, d∗, ω∗, ν∗and λ∗are unique with ω∗
i = ν∗
i = ˆν = 0.


---

Page 8

---

8
Lemma 3 (OLC and VF-OLC Equivalence). Given any set of vectors (d∗, ω∗, θ∗, φ∗, P ∗) satisfying CT θ∗= CT φ∗
and LBθ∗= CP ∗. Then (d∗, ω∗, θ∗) is an optimal solution of OLC if and only (d∗, ω∗, φ∗, P ∗) is an optimal
solution to VF-OLC.
B. Distributed Optimal Load-side Control
We now show how to leverage the power network dynamics to solve the OLC problem in a distributed way. Our
solution is based on the classical primal dual optimization algorithm that has been of great use to design congestion
control mechanisms in communication networks [32]–[35].
Since by Lemma 3, VF-OLC provides the same optimal load schedule as OLC, we can solve VF-OLC instead.
This will allow us to incorporate the network dynamics as part of an optimization algorithm that indirectly solves
OLC.
To achieve this goal we ﬁrst minimize (10) over d and ω which is achieved by setting ωi = νi and di =
c
′−1
i
(νi + λi) in (10). Thus we get
L(x, σ) = minimize
d,ω
L(d, ω, x, σ)
= ΦN (λ, ν) −P T CT ν −πT ˆP −ρ+T P + ρ−T P
−φT (LBλ −CDB ˆCT π −CDB(ρ+ −ρ−))
(14)
where ΦS(λS, νS) := P
i∈S Φi(λi, νi) and
Φi(λi, νi) :=ci(di(λi + νi)) −(λi + νi)di(λi + νi)
−Di
ν2
i
2 + (λi + νi)P in
i .
(15)
The strict convexity of L(d, ω, x, σ) on (d, ω) and the fact that d and ω only appear in (9b) and (9c) gives rise to
the following lemma whose proof is also in the Appendix.
Lemma 4 (Strict concavity of L(x, σ) in (λ, ν)). The function Φi(λi, νi) in (15) is strictly concave. As a result,
L(x, σ) is strictly concave in (λ, ν).
Next we reduce the Lagrangian L(x, σ) by maximizing it for any νi with i ∈L. We let y = (λ, νG, π, ρ+, ρ−)
and consider the Lagrangian
L(x, y) = maximize
νi:i∈L
L(x, σ).
(16)
Since L(x, σ) is strictly concave in ν by Lemma 4, the minimizer of (16) is unique. Moreover, this also implies
that L(x, y) is strictly concave in (λ, νG).
Finally, the optimal load controllers can be then obtained by considering the primal-dual gradient law of L(x, y)
which is given by
˙y = Y
ï ∂
∂y L(x, y)T
ò+
ρ
and
˙x = −X ∂
∂xL(x, y)T
(17)


---

Page 9

---

9
where Y = diag((ζν
i )i∈G, (ζλ
i )i∈N , (ζπ
k )k∈K, (ζρ+
e )e∈E, (ζρ−
e )e∈E) and X = diag((χP
e )e∈E, (χφ
i )i∈N ), and the
projection [·]+
ρ is deﬁned as in (1) for u = y and uS = ρ. This projection ensures that the vector ρ(t) remains
within the positive orthant, that is ρ+(t) ≥0 and ρ−(t) ≥0 ∀t.
The following theorem shows that this procedure indeed embeds the network dynamics as part of the primal-dual
law (17) while providing a distributed scheme to solve OLC.
Theorem 5 (Optimal Load-side Control). By setting ζν
i = M −1
i
, χP
ij = Bij and νi = ωi, the primal-dual gradient
law (17) is equivalent to the power network dynamics (4) together with
˙λi = ζλ
i

P in
i
−di −P
j∈Ni Bij(φi −φj)

(18a)
˙πk = ζπ
k
 P
ij∈Bk ˆCk,ijBij(φi −φj) −ˆPk

(18b)
˙ρ+
ij = ζρ+
ij
Bij(φi −φj) −P ij
+
ρ+
ij
(18c)
˙ρ−
ij = ζρ−
ijP ij −Bij(φi −φj)+
ρ−
ij
(18d)
˙φi = χφ
i
 P
j∈Ni Bij(λi−λj)−P
k∈K,e∈Bk Ci,eBe ˆCk,eπk
−P
e∈E Ci,eBe(ρ+
e −ρ−
e )

(18e)
di = c′
i
−1(λi + ωi)
(18f)
where (18a), (18e) and (18f) are for i ∈N, (18b) is for k ∈K, and (18c) and (18d) are for ij ∈E.
Proof: By Lemma 4 and (14), L(x, σ) is strictly concave in (λ, ν). Therefore, it follows that there exists a
unique
ν∗
L(x, y) = arg max
νL
L(x, σ).
(19)
Moreover, by stationarity, ν∗
L(x, y) must satisfy
∂L
∂νL
(x, y, ν∗
L(x, y))T = ∂ΦL
∂νL
(λL, ν∗
L(x, y))T −CLP
(20a)
= P in
L −DLν∗
L(x, y)−dL(λL+ν∗
L(x, y))−CLP = 0
(20b)
which is equivalent to (4b), i.e. ν∗
L(x, y) implicitly satisﬁes (4b).
We now iteratively apply the envelope theorem [36] on L(x, y) (16) to compute
∂
∂xL(x, y) and
∂
∂yL(x, y). For
example, to compute
∂
∂xL(x, y) we use
∂
∂xL(x, y) =
∂
∂xL(x, σ)

νL=ν∗
L(x,y)
(21a)
=
Ç
∂
∂xL(d, ω, x, σ)

(d,ω)=(c′−1(λ+ν),ν)
å
νL=ν∗
L(x,y)
,
(21b)
where c′−1(λ + ν) := (c′−1
i
(λi + νi))i∈N , which leads to
∂
∂P L(x, y)T = −(CT
G νG + CT
Lν∗
L(x, y))
(22a)


---

Page 10

---

10
Power Network Dynamics
(ω, P)
...
0
di(λi+ωi)
0
...
Distributed Load Control
(λ, π, ρ+, ρ−, φ)
+
ω
+
λ
d
d
Fig. 1: Control architecture derived from OLC
∂
∂φL(x, y)T = −(LBλ −CB( ˆCT π + ρ+ −ρ−))
(22b)
An analogous computation for
∂
∂yL(x, y) gives
∂
∂νG
L(x, y)T = P in −(dG(λG + νG) + DνG) −CP
(23a)
∂
∂λL(x, y)T = P in −d(λ + ν)|νL=ν∗
L(x,y) −LBφ
(23b)
∂
∂π L(x, y)T = ˆCBCT φ −ˆP
(23c)
∂
∂ρ+ L(x, y)T = BCT φ −P
(23d)
∂
∂ρ−L(x, y)T = P −DBCT φ
(23e)
where, for a set S, we dS(λS + νS) := (di(λi + νi))i∈S and d(λ + ν) = dN (λN + νN ).
Using (22)-(23) and identifying ωi in (4) and (18) with νi in (17), it is easy to see that (17) only differs from
(4a),(4c) and (18) on the locations where ωL must be substituted with ν∗
L(x, y). However, since there is a unique
ωL that satisﬁes (4b) given the remaining state variables, and we showed that ν∗
L(x, y) also satisﬁes (4b), then it
follows that (17) and (4) with (18) are equivalent representations of the same system.
Equations (4) and (18) show how the network dynamics can be complemented with dynamic load control such
that the whole system amounts to a distributed primal-dual algorithm that tries to ﬁnd a saddle point on L(x, y).
We will show in the next section that this system does achieve optimality as intended.
Figure 1 shows the unusual control architecture derived from our OLC problem. Unlike traditional observer-based
controller design architecture [37], our dynamic load control block does not try to estimate the state of the network.
Instead, it drives the network towards the desired state using a shared static feedback loop, i.e. di(λi + ωi).
Finally, Figure 2 shows the communication requirements to implement our distributed load control (18). The


---

Page 11

---

11
Area 1
Area 2
Fig. 2: Power network example (left) and the corresponding communication requirement to implement the distributed
load control (18)
only state that cannot be computed distributedly is πk as it requires information from all boundary buses of area k
and their adjacent buses outside k. This limitation is overcome in Section VI-B by modifying (8d) in Problem 1.
Remark 6. One of the limitations of (18) is that in order to generate the Lagrange multipliers λi one needs to
estimate P in
i
−di which is not easy to obtain from the measurements of P in
i
−Diωi −di without knowing Di. This
problem will be addressed in Section V where we propose a modiﬁed control scheme that can achieve the same
equilibrium without needing to know Di exactly.
Remark 7. The procedure described in this section is independent of the constraints (8d)-(8e). Therefore, such
constraints can be generalized to arbitrary equality and inequality constraints on the line ﬂows BCT θ. This property
will be exploited in Section VI to further extend our framework.
IV. OPTIMALITY AND CONVERGENCE
In this section we will show that the system (4) and (18) can efﬁciently rebalance supply and demand, restore
the nominal frequency, and preserve inter-area ﬂow schedules and thermal limits.
We will achieve this objective in two steps. Firstly, we will show that every equilibrium point of (4) and (18)
is an optimal solution of (9), or equialently (8). This guarantees that a stationary point of the system efﬁciently
balances supply and demand and achieves zero frequency deviation.


---

Page 12

---

12
Secondly, we will show that every trajectory (d(t), ω(t), φ(t), P(t), λ(t), π(t), ρ+(t), ρ−(t)) converges to an
equilibrium point of (4) and (18). Moreover, we will show that since P(0) = BCT θ0 (as shown in Section II-A),
the line ﬂows will converge to a point that satisﬁes (5) and (7).
Theorem 8 (Optimality). A point p∗:= (d∗, ω∗, φ∗, P ∗, λ∗, π∗, ρ+∗, ρ−∗) is an equilibrium point of (4) and (18)
if and only if (d∗, ω∗, θ∗) is an optimal solution of OLC and (d∗, ω∗, φ∗, P ∗, λ∗, ν∗, π∗, ρ+∗, ρ−∗) is a primal-dual
optimal solution to the VF-OLC problem, with
ω∗= ν∗, CP ∗= LBθ∗and CT θ∗= CT φ∗.
(24)
Proof: The proof of this theorem is a direct application of lemmas 2 and 3. Let p∗be an equilibrium of (4)
and (18). Then, by deﬁnition of the projection [·]+
ρ and (18c)-(18d), ρ+∗≥0 and ρ−∗≥0 and thus dual feasible.
Similarly, since ˙ωi = 0, ˙λi = 0, ˙πk = 0, ˙ρ+
ij = 0 and ˙ρ−
ij = 0, then (4a)-(4b) and (18a)-(18d) are equivalent to
primal feasibility, i.e. (d∗, ω∗, φ∗, P ∗) is a feasible point of (9). Finally, by deﬁnition of (4) and (18), conditions
(11), (12) and (13) are always satisﬁed by any equilibrium point. Thus we are under the conditions of Lemma
2 and therefore (d∗, ω∗, φ∗, P ∗, λ∗, ν∗, π∗, ρ+∗, ρ−∗) is primal-dual optimal of VF-OLC satisfying (24). Lemma 3
shows the remaining statement of the theorem.
The rest of this section is devoted to showing that in fact for every initial condition (ω(0), φ(0), P(0), λ(0), π(0),
ρ+(0), ρ−(0)), the system (4) and (18) converges to one such optimal solution. Furthermore, we will show that
P(t) converges to a P ∗that satisﬁes (5) and (7).
Since we showed in Theorem 5 that (4) and (18) is equivalent to (17), we will provide our convergence result for
(17). Our global convergence proof builds on recent results of [38] on global convergence of primal-dual algorithms
for network ﬂow control. Our proof extends [38] in the following aspects. Firstly, the Lagrangian L(x, y) is not
strictly concave in all of its variables. Secondly, the projection (1) introduces discontinuities in the vector ﬁeld that
prevents the use of the standard LaSalle’s Invariance Principle [39].
We solve the latter issue using an invariance principle for Caratheodory systems [40]. We refer the reader to [41]
for a detailed treatment that formalizes its application for primal-dual systems. The former issue is solved in Theorem
10 which makes use of the following additional lemma whose proof can be found in the Appendix.
Lemma 9 (Differentiability of ν∗
L(x, y)). Given any (x, y), the maximizer of (16), ν∗
L(x, y), is continuously
differentiable provided ci(·) is strongly convex. Furthermore, the derivative is given by
∂
∂xν∗
L(x, y)=
φ
P
î
ó
0
−(DL + d′
L)−1CL
νL
(25)
∂
∂y ν∗
L(x, y)=
λL
λG
νG
π
ρ
î
ó
−(DL+d′
L)−1d′
L
0
0
0 0
νL
(26)


---

Page 13

---

13
where DS := diag(Di)i∈S and
d′
S =





diag(d′
i(λi + ν∗
i (x, y)))i∈S
if S ⊆L
diag(d′
i(λi + νi))i∈S
if S ⊆G
We now present our main convergence result. Let E be the set of equilibrium points of (17)
E :=
®
(x, y) : ∂L
∂x (x, y) = 0,
ï∂L
∂y (x, y)
ò+
ρ
= 0
´
,
which by theorems 5 and 8 characterizes the set of optimal solutions of the OLC problem.
Theorem 10 (Global Convergence). The set E of equilibrium points of the primal-dual algorithm (17) is globally
asymptotically stable. Furthermore, each individual trajectory converges to a unique point within E that is optimal
with respect to the OLC problem.
Proof: Following [38] we consider the candidate Lyapunov function
U(x, y) = 1
2(x−x∗)T X−1(x−x∗)+ 1
2(y −y∗)T Y −1(y−y∗)
(27)
where (x∗, y∗) is any equilibrium point of (17).
We divide the proof of this theorem in four steps:
Step 1: We ﬁrst use the invariance principle for Caratheodory systems [40] to show that (x(t), y(t)) converges
to the largest invariance set that satisﬁes ˙U(x, y) ≡0 between transitions of the projection [·]+
ρ , i.e.
(x(t), y(t)) →M ⊆{(x, y): ˙U(x(t), y(t))≡0, t ∈R+\{tk}}
(28)
where {tk, k ∈N} are the time instants when the projection changes between on and off.
Step 2: We show that any invariant trajectory (x(t), y(t)) ∈M must have λ(t) ≡ˆλ and ν(t) ≡ˆν for some
constant vectors ˆλ and ˆν.
Step 3: We show that whenever λ(t) ≡ˆλ and ν(t) ≡ˆν, then whole trajectory (x(t), y(t)) must an equilibrium
point, i.e. M ⊆E.
Step 4: Finally, we show that even though the invariance principle guarantees only convergence to the set E.
The convergence is always to some point within E, i.e. (x(t), y(t)) →(x∗, y∗) ∈E.
Proof of step 1: Differentiating U over time gives
˙U(x, y)=−∂
∂xL(x, y)(x−x∗)+
ï ∂
∂y L(x, y)
ò+
ρ
(y−y∗)
(29)
≤∂L
∂x (x, y)(x∗−x) + ∂L
∂y (x, y)(y −y∗)
(30)
≤L(x∗, y) −L(x, y) + L(x, y) −L(x, y∗)
(31)
= L(x∗, y) −L(x, y∗)
= L(x∗, y) −L(x∗, y∗)
|
{z
}
≤0
+ L(x∗, y∗) −L(x, y∗)
|
{z
}
≤0
(32)


---

Page 14

---

14
where (29) follows from (17) and (30) from (2). Step (31) follows from convexity (resp. concavity) of L(x, y) in
x (resp. y). Finally, equation (32) follows from the saddle property of the equilibrium point (x∗, y∗).
Therefore, since U(x, y) is radially unbounded, the trajectories are bounded, and it follows from the invariance
principle for Caratheodory systems [40] that (x(t), y(t)) →M, i.e. (28) holds. The steps 2 and 3 below basically
characterize M.
Proof of step 2: Notice that in order to have ˙U ≡0, both terms in (32) must be zero. In particular, we must
have
L(x(t), y∗) ≡L(x∗, y∗).
Now, differentiating with respect to time gives
0 ≡
˙
L(x(t), y∗) ≡∂
∂xL(x(t), y∗) ˙x ≡−|| ∂
∂xL(x(t), y∗)||2,
which implies that
∂
∂xL(x(t), y∗) ≡0.
Therefore, the fact that ν∗
G = 0,
∂
∂P L(x(t), y∗) ≡0, and (22a) holds, implies that x(t) must satisfy CT
Lν∗
L(x(t), y∗) ≡
0, which implies that either ν∗
L(x(t), y∗) ≡0 (when CL is full row rank) or ν∗
L(x(t), y∗) ≡1α(t) (when L = N)
where α(t) is a time-varying scalar.
We now show that when L = N we get ν∗
L(x(t), y∗) ≡ˆνL for some constant vector ˆνL. Differentiating
ν∗
L(x(t), y∗) ≡1α(t) with respect to time and using (25) we obtain
(DL + d′
L)−1CL ˙P((t) ≡1 ˙α(t)
which after left multiplying by 1T (DL + d′
L) gives
1T (DL + d′
L)1 ˙α(t) ≡0 =⇒˙α(t) ≡0.
Thus, in either case we obtain
ν∗
L(x(t), y∗) = ν∗
L(CLP(t), λ∗
L) ≡ˆνL
(33)
for some constant vector ˆνL, which implies that CLP(t) ≡CL ˆP for some constant vector ˆP.
Therefore, it follows that ν∗
L(x(t), y(t)) must satisfy
ν∗
L(x(t), y(t)) ≡ν∗
L(ˆx, y(t))
(34)
for some constant vector ˆx.
Now, using (20) with (34) we get
P m
L −DLν∗
L(ˆx, y(t)) −dL(λL(t) + ν∗
L(ˆx, y(t))) −CL ˆP
≡0.
(35)
A similar argument using the fact that L(x∗, y) ≡L(x∗, y∗) gives
∂
∂y L(x∗, y)
ï ∂
∂y L(x∗, y)T
ò+
ρ
≡0.
(36)


---

Page 15

---

15
Since the projection [·]+
ρ only acts on the ρ positions, (36) implies
∂
∂νG L(x∗, y) ≡0,
∂
∂λL(x∗, y) ≡0 and
∂
∂πL(x∗, y) ≡0.
Now
∂
∂νG L(x∗, y) ≡0 together with equation (23a) implies that
P m
G −DGνG(t) −dG(λG(t) + νG(t)) −CGP ∗≡0,
(37)
and
∂
∂λL(x∗, y) ≡0 with (23b) implies
P m
G −dG(λG(t) + νG(t)) −CGP ∗≡0
(38)
P m
L −dL(λL(t) + ν∗
L(x∗, y(t))) −CLP ∗≡0
(39)
Using (37) and (38) together with the fact that di(·) is strictly increasing, we get νG(t) ≡ˆνG and λG(t) ≡ˆλG, for
constant vectors ˆνG and ˆλG. Moreover, since P ∗is primal optimal, Lemma 5 and Theorem 8 imply that νG(t) ≡0
and λG(t) ≡λ∗
G. Finally, now using (35) together with (39), the same argumentation gives ν∗
L(x(t), y(t)) ≡ˆνL and
λL(t) ≡ˆλL for constant vectors ˆνL and ˆλL. This ﬁnishes step 2, i.e. λ(t) ≡ˆλ and ν(t) ≡ˆν.
Proof of step 3: Now, since ˙λ ≡0, it follows from (18a) that CT φ(t) ≡CT ˆφ for some constant vector ˆφ or
equivalently φ(t) ≡ˆφ + β(t)1. Differentiating in time 1T (χφ)−1φ(t) gives 0 ≡1T (χφ)−1 ˙φ ≡(P
i∈N 1/χφ
i ) ˙β
which implies that β(t) ≡ˆβ for constant scalar ˆβ.
Suppose now that either ˙P ̸= 0 or ˙π ̸= 0. Since CT φ(t) ≡CT ˆφ and ν(t) ≡ˆν, ˙P and ˙π are constant. Thus,
since the trajectories are bounded, we must have ˙P ≡0 and ˙π ≡0; otherwise U(x, y) will grow unbounded
(contradiction).
It remains to show that ˙ρ ≡0, i.e. ˙ρ+ ≡˙ρ−≡0. Since φ(t) ≡ˆφ, then the argument inside (18c) and (18d) is
constant.
Now consider any ρ+
e , e = ij ∈E. Then we have three cases: (i) Be(ˆφi−ˆφj)−¯Pe > 0, (ii) Be(ˆφi−ˆφj)−¯Pe < 0
and (iii) Be(ˆφi −ˆφj) −¯Pe = 0. Case (i) implies ρ+
e (t) →+∞which cannot happen since the trajectories are
bounded. Case (ii) implies that ρ+
e (t) ≡0 which implies that ˙ρ+
e ≡0, and case (iii) also implies ˙ρ+
e ≡0. An
analogous argument gives ˙ρ−≡0. Thus, we have shown that M ⊆E.
Proof of step 4: We now use structure of U(x, y) to achieve convergence to a single equilibrium. Since
(x(t), y(t)) →M and (x(t), y(t)) are bounded, then there exists an inﬁnite sequence of time values {tk} such
that (x(tk), y(tk)) →(ˆx∗, ˆy∗) ∈M. Thus, using this speciﬁc equilibrium (ˆx∗, ˆy∗) in the deﬁnition of U(x, y), it
follows that U(x(tk), y(tk)) →0, which by continuity of U(x, y) implies that (x(t), y(t)) →(ˆx∗, ˆy∗).
Thus, it follows that (x(t), y(t)) converges to only one optimal solution within M ⊆E.
Finally, the following theorem shows that the system is able to restore the inter-area ﬂows (5) and maintain the
line ﬂows within the thermal limits (7).
Theorem 11 (Inter-area Constraints and Thermal Limits). Given any primal-dual optimal solution (x∗, σ∗) ∈E,
the optimal line ﬂow vector P ∗satisﬁes (5). Furthermore, if P(0) = BCT θ0 for some θ0 ∈R|N |, then P ∗
ij =
Bij(φ∗
i −φ∗
j) and therefore (7) holds.


---

Page 16

---

16
Proof: By optimality, P ∗and φ∗must satisfy
P m −d∗= CP ∗= LBφ∗= CBCT φ∗
(40)
Therefore using primal feasibility, (6) and (40) we have
ˆP = ˆCBCT φ∗=EKCBCT φ∗=EKCP ∗= ˆCP ∗
which is exactly (5).
Finally, to show that P ∗
ij = Bij(φ∗
i −φ∗
j) we will use (4c). Integrating (4c) over time gives
P(t) −P(0) =
Z t
0
BCT ν(s)ds.
Therefore, since P(t) →P ∗, we have P ∗= P(0) + BCT θ∗where θ∗is any ﬁnite vector satisfying CT θ∗=
R ∞
0
CT ν(s)ds.
Again by primal feasibility CBCT φ∗= LBφ∗= CP ∗= C(P(0) + BCT θ∗) = CBCT (θ0 + θ∗). Thus, we
must have φ∗= (θ0 + θ∗) + α1 and it follows then that P ∗= BCT (θ0 + θ∗) = BCT (φ∗−α1) = BCT φ∗.
Therefore, since by primal feasibility P ≤BCT φ∗≤¯P, then P ≤P ∗≤¯P.
V. CONVERGENCE UNDER UNCERTAINTY
In this section we discuss an important aspect of the implementation of the control law (18). We provide a
modiﬁed control law that solves the problem raised in Remark 6, i.e. that does not require knowledge of Di. We
show that the new control law still converges to the same equilibrium provided the estimation error of Di is small
enough (c.f. (48)).
We propose an alternative mechanism to compute λi. Instead of (18a), we consider the following control law:
˙λi =ζλ
i

Mi ˙ωi+aiωi+
X
e∈E
Ci,ePe−
X
j∈Ni
Bij(φi−φj)

(41a)
where Mi := 0 for i ∈L and ai ∈R is a positive controller parameter that can be arbitrarily chosen. Notice that,
while before Di was an unknown quantity, Mi is usually known and ai is a design parameter. Furthermore, while
equation (41a) requires the knowledge of ˙ωi, this is only needed on generator buses and can therefore be measured
from the generator’s shaft angular acceleration using one of several existing mechanisms, see e.g. [42].
The parameter ai plays the role of Di. In fact, whenever ai = Di then one can use (4a)-(4b) to show that (41a)
is the same as (18a). More precisely, if we let ai = Di + δai, then using (4a)-(4b), (41a) becomes
˙λ=ζλ
i

P in
i −di+δaiωi−
X
j∈Ni
Bij(φi−φj)

,
(42)
which is equal to (18a) when δai = 0. A simple equilibrium analysis shows that ai does not affect the steady state
behavior provided that ai ̸= 0 for some i ∈N. Thus, we focus in this section on studying the stability of our
modiﬁed control law.
Using (42), we can express the new system using
˙x = −X ∂
∂xL(x, y)T
(43a)


---

Page 17

---

17
˙y = Y
ï ∂
∂y L(x, y)T + g(x, y)
ò+
ρ
(43b)
where
g(x, y):=
λL
λG
(νG, π, ρ)
î
ó
(δALν∗
L)T (δAGνG)T
0
T
(44)
with ν∗
L := ν∗
L(x, y) and δAS := diag(δai)i∈S.
The system (43) is no longer a primal-dual algorithm. The main result of this section shows, that under provided
that ai does not depart signiﬁcantly from Di (see (48)), convergence to the optimal solution is preserved.
To show this result, we provide a novel convergence proof that makes use of the following lemmas whose proofs
can be found in the Appendix.
Lemma 12 (Second order derivatives of L(x, y)). Whenever Lemma 9 holds, then we have
∂2
∂x2 L(x, y) =
φ
P
"
#
0
0
φ
0
CT
L(DL + d′
L)−1CL
P
and
(45)
∂2
∂y2 L(x, y)=−
λL
λG
νG
(π, ρ)




DL(DL + d′
L)−1d′
L 0
0
0
λL
0
d′
G
d′
G
0
λG
0
d′
G (DG + d′
G) 0
νG
0
0
0
0
(π, ρ)
(46)
with
∂2
∂x2 L(x, y) ⪰0 and
∂2
∂y2 L(x, y) ⪯0.
Lemma 13 (Partial derivatives of g(x, y)). Whenever Lemma 9 holds, then
∂
∂xg(x, y) =
φ
P
"
#
0
−δAL(DL + d′
L)−1CL
λL
0
0
(νG, λG, π, ρ)
∂
∂y g(x, y) =
λL
λG
νG
(π, ρ)




−δAL(DL + d′
L)−1d′
L 0
0
0
λL
0
0 δAG
0
λG
0
0
0
0
(νG, π, ρ)
Unfortunately, the conditions of Theorem 10 will not sufﬁce to guarantee convergence of the perturbed system.
The main difﬁculty is that d′
i(λi + νi) > 0 can become arbitrarily close to zero. Therefore the sub-matrix of (46)
corresponding to the states λ and νG can become arbitrarily close to singular which makes the system not robust
to perturbations of the form of (44). Thus, we require the following additional assumption.


---

Page 18

---

18
Assumption 3 (Lipschitz continuity of c′
i). The functions c′
i(·) are Lipschitz continuous with Lipschitz constant
L > 0.
Assumption 3 implies that the domain of Di = R in Assumption 1. However, if the systems is designed with
enough capacity so that d∗
i ∈[di + ε, di −ε] ∀i, then one can always modify a cost function ci(·) that satisﬁes
Assumptions 1 and 2 for ﬁnite domains Di = [di, di] and deﬁne a new cost function ˜ci(·) that satisﬁes Assumption
3 without modifying the optimal allocation d∗
i . More precisely, given ci(·), deﬁne ˜ci(·) to be equal to ci(·), inside
[di + ε, di −ε] and modify ˜ci(·) outside the subset so that Assumption 3 holds. It is easy to show then that the
optimal solution will still be d∗
i and therefore we still get di ≤d∗
i ≤di.
Using now Assumptions 1 and 3 we can show that α ≤c′′
i ≤L which implies
d′ := 1/L
≤
d′
i = 1/c′′
i
≤
¯d′ := 1/α.
(47)
Theorem 14 (Global convergence of perturbed system). Whenever assumptions 1, 2 and 3 hold. The system (43)
converges to a point in the optimal set E for every initial condition whenever
δai ∈2( d′ −
»
d′2 + d′Dmin, d′ +
»
d′2 + d′Dmin ).
(48)
where Dmin := mini∈N Di.
Proof: We prove this theorem in three steps:
Step 1: We ﬁrst show that under the dynamics (43), the time derivative of (27) is upper-bounded by
˙U(z) ≤
Z 1
0
(z−z∗)T [H(z(s))](z−z∗)ds
(49)
where z = (x, y), z∗= (x∗, y∗), z(s)=z∗+s(z−z∗), and H(z) is given by (57).
Step 2: We then show that under the assumption (48) H(z) ⪯0, and that for any ˜z = (˜φ, ˜P, ˜λ, ˜νG, ˜π, ˜ρ) ∈
R2|N|+3|E|+|G|+|K|, we have
˜zT H(z)˜z =0, ∀z ⇐⇒˜z ∈{˜z ∈RZ : ˜λ=0, ˜νG =0, CL ˜P =0}
(50)
where Z = 2|N| + 3|E| + |G| + |K|.
Step 3: We ﬁnally use (50) and the invariance principle for Caratheodory systems [40] to show that ν(t) ≡0
and λ(t) ≡λ∗.
The rest of the proof follows from steps 3 and 4 of Theorem 10.
We use z = (x, y) and compactly express (43) using
˙z = Z[f(z)]+
ρ
(51)
where Z = blockdiag(X, Y ) and
f(z) :=


−∂
∂xL(x, y)T
∂
∂yL(x, y)T + g(x, y)

.
Similarly, (27) becomes U(z) = 1
2(z −z∗)T Z−1(z −z∗).


---

Page 19

---

19
Proof of step 1: We now recompute ˙U(z) differenlty, i.e.
˙U(z)= 1
2((z−z∗)T [f(z)]+
ρ +[f(z)]+
ρ
T (z−z∗))
(52)
≤1
2((z−z∗)T f(z)+f(z)T (z−z∗)) = (z−z∗)T f(z)
(53)
=
Z 1
0
(z−z∗)T
ï ∂
∂z f(z(s))
ò
(z−z∗)ds+(z−z∗)T f(z∗)
(54)
≤1
2
Z 1
0
(z−z∗)T
ï ∂
∂z f(z(s))T + ∂
∂z f(z(s))
ò
(z−z∗)ds
(55)
=
Z 1
0
(z−z∗)T [H(z(s))](z−z∗)ds
(56)
where (52) follows from (51), (53) from (2), and (54) form the fact that f(z) −f(z∗) =
R 1
0
∂
∂zf(z(s))(z −z∗)ds,
where
∂
∂z f(z) =

−∂2
∂x2 L(x, y)
−
∂2
∂x∂yL(x, y)
∂2
∂x∂yL(x, y)T
∂2
∂y2 L(x, y)


+


0
0
∂
∂xg(x, y)
∂
∂yg(x, y)

.
Finally, (55) follows from the fact that either fi(z∗) = 0, or (zi −z∗
i ) = zi ≥0 and fi(z∗) < 0, which implies
(z −z∗)T f(z∗) ≤0.
Therefore, H(z) in (49) can be expressed as
H(z) = 1
2
ï ∂
∂z f(z)T + ∂
∂z f(z)
ò
=

−∂2
∂x2 L(x, y)
0
0
∂2
∂y2 L(x, y)


+


0
1
2
∂
∂xg(x, y)T
1
2
∂
∂xg(x, y)
1
2
Ä
∂
∂yg(x, y)T + ∂
∂yg(x, y)
ä


which using lemmas 12 and 13 becomes
H(z) =
φ
(P, λL)
(λG, νG)
(π, ρ)




0
0
0
0
φ
0 HP,λL(z)
0
0
(P, λL)
0
0
HλG,νG(z)
0
(λG, νG)
0
0
0
0
(π, ρ)
(57)
where
HP,λL(z) =
"
#
−CT
L(DL + d′
L)−1CL
−1
2CT
L(DL + d′
L)−1δAL
−1
2δAL(DL + d′
L)−1CL −(DL + δAL)(DL + d′
L)−1d′
L


---

Page 20

---

20
and
HλG,νG(z) =
"
#
−d′
G
1
2δAG −d′
G
1
2δAG −d′
G −(d′
G + DG)
.
It will prove useful in the next step to rewrite HP,λL(z) using
HP,λL(z) = ˜CT ˜D
1
2 (z) ˜H(z) ˜D
1
2 (z) ˜C
(58)
where
˜C =blockdiag(CL, I), ˜D(z) = blockdiag(DL + d′
L, DL + d′
L)−1
and
˜H(z) =


−I
−1
2δAL
−1
2δAL
−(DL + δAL)d′
L

.
Notice that since ˜D(z) ≻0, ˜D
1
2 (z) in (58) always exists.
Proof of step 2: To show that H(z) ⪯0 and (50) holds, it is enough to show that
˜H(z) ≺0
and
HλG,νG(z) ≺0,
∀z.
(59)
To see this, assume for now that (59) holds. Then, using (58) it follows that HP,λL(z) ⪯0, which implies by
(57) and HλG,νG(z) ≺0 that H(z) ⪯0. Moreover, ˜zT H(z)˜z = 0 ∀z if and only if
[ ˜P T ˜λT
L ]HP,λL(z)[ ˜P T ˜λT
L ]T = 0
(60)
and
[ ˜λT
G ˜νT
G ]HλG,νG(z)[ ˜λT
G ˜νT
G ]T = 0.
(61)
Therefore using (58) it follows that (60) and ˜H(z) ≺0 ∀z implies that CL ˜P = 0 and ˜λL = 0. Similarly,
HλG,νG(z) ≺0 ∀z and (61) implies ˜λG = ˜νG = 0. This ﬁnishes the proof of (50). It remains to show that (59)
holds whenever (48) holds.
Proof of ˜H(z) ≺0: By deﬁnition of negative deﬁnite matrices, ˜H(z) ≺0 if and only if all the roots of the
characteristic polynomials
pi(µi) = (µi + 1)(µi + (Di + δai)d′
i) −δa2
i /4
= µ2
i + (1 + (Di + δai)d′
i)µi + (Di + δai)d′
i −δa2
i /4
are negative for every i ∈L and ∀z (recall d′
i depends on z).
Thus, applying Ruth-Hurwitz stability criterion we get the following necessary and sufﬁcient condition:
δa2
i −4(Di + δai)d′
i < 0
(62a)
1 + (Di + δai)d′
i > 0
(62b)
for every i ∈L.


---

Page 21

---

21
Now, equation (62a) can be equivalently rewritten as:
2(d′
i −
»
d′
i(d′
i + Di)) < δai < 2(d′
i +
»
d′
i(d′
i + Di)).
(63)
Since d′
i ∈[d′, ¯d′], Di ≥Dmin and the function x −
p
x(x + y) is decreasing in both x and y for x, y ≥0, then
2(d′
i −
»
d′
i(d′
i + Di)) ≤2(d′ −
»
d′(d′ + Dmin)).
Similarly, since x +
p
x(x + y) is increasing for x, y ≥0,
2(d′
i +
»
d′
i(d′
i + Di)) ≥2(d′ +
»
d′(d′ + Dmin)).
Therefore, (62a) holds whenever δai satisifes (48).
Finally, (62b) holds whenever δai > −1
d′
i −Di which in particular holds if δai > −Dmin. The following
calculation shows that 2(d′ −
»
d′(d′ + Dmin)) > −Dmin which implies that (62b) holds under condition (48):
2(d′ −
»
d′(d′ + Dmin)) > −Dmin
⇐⇒
»
d′(d′ + Dmin) < d′ + Dmin
2
⇐⇒
d′(d′ + Dmin) < d′2+D2
min
4
+ d′Dmin
⇐⇒
0 < D2
min
4
.
Therefore (62) holds whenever (48) holds.
Proof of HνG,λG(z) ≺0: Similarly, we can show that all the eigenvalues of HνG,λG(z) are the roots of the
polynomials
pi(µi) = (µi + Di + d′
i)(µi + d′
i) −(δai
2 −d′
i)2
= µ2
i + (Di + 2d′
i)µi + (Di + δai)d′
i −δa2
i
4
which, since Di + 2d′
i > 0, are negative if and only if (62a) is satisﬁed ∀i ∈G. Therefore, (48) also guarantees
that HνG,λG ≺0.
Proof of step 3: Since by Step 2 H(z) ⪯0 ∀z, (49) implies that ˙U ≤0 whenever (48) holds. Thus, we are left
to apply again the invariance principle for Caratheodory systems [40] and characterize its invariant set M (28).
Let δz = (z(t) −z∗) and similarly deﬁne δP = (P(t) −P ∗), δλL = λL(t) −λ∗
L, δλG = λG(t) −λ∗
G and
δνG = νG(t) −ν∗
G. Then since ˙U ≡0 iff δzT H(z)δz ≡0, then it follows from (50) that z(t) ∈M if and only if
CLδP ≡0, δλ ≡0 and δνG ≡0.
This implies that CLP(t) ≡CLP ∗, λ(t) ≡λ∗and νG(t) ≡ν∗
G = 0, which in particular also implies that
ν∗
L(x(t), y(t)) = ν∗
L(CLP(t), λ(t)) ≡ν∗
L(CLP ∗, λ∗) = 0. Therefore we have shown that z(t) ∈M if and only if
λ(t) ≡λ∗and ν(t) ≡0 which ﬁnalizes Step 3.
As mentioned before, the rest of the proof follows from steps 2 and 3 of Theorem 10.


---

Page 22

---

22
VI. FRAMEWORK EXTENSIONS
In this section we extend the proposed framework to derive controllers that enhance the solution described before.
More precisely, we will show how we can modify our controllers in order to account for buses that have zero power
injection (Section VI-A) and how to fully distribute the implementation of the inter-area ﬂow contraints (Section
VI-B).
A. Zero Power Injection Buses
We now show how our design framework can be extended to include buses with zero power injection. Let Z be
the set of buses that have neither generators nor loads. Thus, we consider a power network whose dynamics are
described by
˙θG∪L =ωG∪L
(64a)
MG ˙ωG =P in
G −(dG+DGωG)−LB,(G,N)θ
(64b)
0=P in
L −(dL+DLωL)−LB,(L,N)θ
(64c)
0=−LB,(Z,N)θ
(64d)
where LB,(S,S′) is the sub-matrix of LB consisting of the rows in S and columns in S′.
We will use Kron reduction to eliminate (64d). Equation (64d) implies that the (θi, i ∈Z) is uniquely determined
by the buses adjacent to Z, i.e. θZ = L−1
B,(Z,Z)LB,(Z,G∪L)θG∪L. Thus we can rewrite (64) using only θG∪L which
gives
˙θG∪L =ωG∪L
(65a)
MG ˙ωG =P in
G −(dG+DGωG)−L♯
B,(G,G∪L)θG∪L
(65b)
0=P in
L −(dL+DLωL)−L♯
B,(L,G∪L)θG∪L
(65c)
where L♯
B = LB,(G∪L,G∪L) −LB,(G∪L,Z)L−1
B,(Z,Z)LB,(Z,G∪L) is the Schur complement of LB after removing
the rows and columns corresponding to Z. The matrix L♯
B is also a Laplacian of a reduced graph G(G ∪L, E♯)
and therefore it can be expressed as L♯
B = C♯T B♯C♯T where C♯is the incidence matrix of G(G ∪L, E♯) and
B♯= diag(B♯
ij)ij∈E♯are the line susceptances of the reduced network.
This reduction allows to use (65) (which is equivalent to (3)) to also model networks that contain buses with
zero power injection. The only caveat is that some of line ﬂows of the vector BCT θ are no longer present in
B♯C♯T θG∪L – when a bus is eliminated using Kron reduction, its adjacent lines Be, e ∈E, are substituted by an
equivalent clique with new line impedances B♯
e′, e′ ∈E♯. As a result, some of the constraints (8d)-(8e) would no
longer have a physical meaning if we directly substitute BCT θ with B♯C♯T θG∪L in (3).
We overcome this issue by showing that each original Bij(θi −θj) in G(N, E) can be replaced by a linear
combination of line ﬂows B♯
i′j′(θi′ −θj′) of the reduced network G(G ∪L, E♯).


---

Page 23

---

23
For any θ satisfying (64d) we have
LBθ =

qG∪L
0|Z|

=

L♯
BθG∪L
0|Z|

.
Thus it follows that
BCT θ = BCT L†
B

qG∪L
0|Z|

= BCT L†
B,(N,G∪L)qG∪L
=BCT L†
B,(N,G∪L)C♯B♯C♯T θG∪L :=A♯B♯C♯T θG∪L
(66)
where L†
B is the pseudo-inverse of LB.
Therefore, by substituting BCT θ with A♯B♯C♯T θG∪L in (8) and repeating the procedure of Section III we
obtained a modiﬁed version of (18) in which (18a)-(18e) becomes
˙λi = ζλ
i

P m
i
−di −
X
j∈N ♯
i
B♯
ij(φi −φj)

(67a)
˙πk = ζπ
k
 X
e∈Bk,ij∈E♯
ˆCk,eA♯
e,ijB♯
ij(φi −φj) −ˆPk

(67b)
˙ρ+
e = ζρ+
e
h X
ij∈E♯
A♯
e,ijB♯
ij(φi −φj) −Pe
i+
ρ+
e
(67c)
˙ρ−
e = ζρ−
e
h
Pe −
X
ij∈E♯
A♯
e,ijB♯
ij(φi −φj)
i+
ρ−
e
(67d)
˙φi = χφ
i
 X
j∈N ♯
i
B♯
ij(λi−λj)−
X
e∈E
C♯
i,eB♯
e
X
e′∈E, k∈K
A♯
e,e′ ˆCk,e′πk
−
X
e∈E
C♯
i,eB♯
e
X
e′∈E
A♯
e,e′(ρ+
e′ −ρ−
e′)

(67e)
where (67a) and (67e) are for i ∈G ∪L, (67b) is for k ∈K, and (67c) and (67d) are for the original lines e ∈E.
It can be shown that the analysis described in Sections IV and V still holds under this extension.
Remark 15. The only additional overhead incurred by the proposed extension is the need for communication
between buses that are adjacent on the graph G(G ∪L, E♯) and were not adjacent in G(N, E) (see Figure 3 for
an illustration).
B. Distributed Inter-area Flow Constraints
We now show how we can fully distribute the implementation of the inter-area ﬂow constraints. The procedure
is analogous to Section VI-A and therefore we will only limit to describe what are the modiﬁcations that need to
be done to (8) in order to obtain controllers that are fully distributed.
We deﬁne for each area k an additional graph G(Bk, Ek) where we associate each boundary edge e ∈Bk with
a node and deﬁne undirected edges {e, e′} ∈Ek that describe the communication links between e and e′. Using


---

Page 24

---

24
Fig. 3: Communication requirements for the power network in Fig. 2 when bus 3 has no injection as described in
Section VI-A (left), and for the distributed inter-area ﬂow constraint formulation of Section VI-B (right).
this formulation, we decompose equation (5) for each k into |Bk| equations
ˆCk,ePe −
ˆPk
|Bk| =
X
e′:{e,e′}∈Bk
(γe −γe′),
e ∈Bk, k ∈K
(68)
where γe is a new primal variable that aims to guarantee indirectly (5). In fact, it is easy to see by summing (68)
over e ∈Bk that
X
e∈Bk
Ç
ˆCk,ePe −
ˆPk
|Bk|
å
=
X
e∈Bk
X
e′:{e,e′}∈Bk
(γk
e −γk
e′) = 0.
which is equal to (5).
Therefore, since whenever (5) holds, one can ﬁnd a set of γe satisfying (68), then we can substitute (8d) with
(68). If we let πk
ij be the Lagrange multiplier associated with (68), then by replacing (18b) and (18e) with
˙πk
ij =ζπ
k,ij

ˆCk,ijBij(φi−φj)−
ˆPk
|Bk| −
X
e:{ij,e}∈Bk
γk
ij−γk
e

(69a)
˙γk
ij =χγ
k,ij
X
e:{ij,e}∈Bk
πk
ij−πk
e

(69b)
˙φi = χφ
i
 X
j∈Ni
Bij(λi−λj)−
X
k∈K, e∈Bk
Ci,eBe ˆCk,eπk
e
−
X
e∈E
Ci,eBe(ρ+
e −ρ−
e )

(69c)


---

Page 25

---

25
1
2
3
4
5
7
6
8
9
10
Area 1
Area 2
1
2
30
25
37
26
28
29
38
35
22
23
36
33
19
21
24
16
15
14
20
34
13
10
32
12
11
31
6
7
8
9
5
4
39
3
18
17
27
Fig. 4: IEEE 39 bus system: New England
we can distribute the implementation of the inter-area ﬂow constraint. Figure 3 shows how the communication
requirements are modiﬁed by this change. If each boundary bus has only one incident boundary edge, i.e. if
P
k∈K, e∈BkCi,eBe ˆCk,eπk
e has at most one term, the convergence results of sections IV and V extend to this case.
VII. NUMERICAL ILLUSTRATIONS
We now illustrate the behavior of our control scheme. We consider the widely used IEEE 39 bus system, shown
in Figure 4, to test our scheme. We assume that the system has two independent control areas that are connected
through lines (1, 2), (2, 3) and (26, 27). The network parameters as well as the initial stationary point (pre fault
state) were obtained from the Power System Toolbox [43] data set.
Each bus is assumed to have a controllable load with Di = [−dmax, dmax], with dmax = 1p.u. on a 100MVA
base with ci(·) and di(·) as shown in Figure 5.
Throughout the simulations we assume that the aggregate generator damping and load frequency sensitivity
parameter Di = 0.2 ∀i ∈N and χφ
i = ζλ
i = ζπ
k = ζρ+
e
= ζρ−
e
= 1, for all i ∈N, k ∈K and e ∈E. These
parameter values do not affect convergence, but in general they will affect the convergence rate. The values of P in


---

Page 26

---

26
−1
−0.5
0
0.5
1
0
5
10
15
20
25
di
ci(di)
−10
−5
0
5
10
−1
−0.5
0
0.5
1
ωi + λi
di(ωi + λi)
Fig. 5: Disutility ci(di) and load function di(ωi + λi)
are corrected so that they initially add up to zero by evenly distributing the mismatch among the load buses. ˆP is
obtained from the starting stationary condition. We initially set P and P so that they are not binding.
0
5
10
15
20
25
30
−0.5
−0.45
−0.4
−0.35
−0.3
−0.25
−0.2
−0.15
−0.1
−0.05
0
0.05
(a) Swing dynamics
ωi rad/s
t
0
5
10
15
20
25
30
−0.5
−0.45
−0.4
−0.35
−0.3
−0.25
−0.2
−0.15
−0.1
−0.05
0
0.05
(c) OLC area−constr
t
0
5
10
15
20
25
30
−0.5
−0.45
−0.4
−0.35
−0.3
−0.25
−0.2
−0.15
−0.1
−0.05
0
0.05
(b) OLC unconstr
t
Fig. 6: Frequency evolution: Area 1
We simulate the OLC-system as well as the swing dynamics (4) without load control (di = 0), after introducing
a perturbation at bus 29 of P in
29 = −2p.u.. In some scenarios we disable a few of the OLC constraints. This is
achieved by ﬁxing the corresponding Lagrange multiplier to be zero.
Figures 6 and 7 show the evolution of the bus frequencies for the uncontrolled swing dynamics (a), the OLC
system without inter-area constraints (b), and the OLC with area constraints (c). It can be seen that while the swing
dynamics alone fail to recover the nominal frequency, the OLC controllers can jointly rebalance the power as well
as recovering the nominal frequency. The convergence of OLC seems to be similar or even better than the swing
dynamics, as shown in Figures 6 and 7.


---

Page 27

---

27
0
5
10
15
20
25
30
−0.5
−0.4
−0.3
−0.2
−0.1
0
0.1
(a) Swing dynamics
ωi rad/s
t
0
5
10
15
20
25
30
−0.5
−0.4
−0.3
−0.2
−0.1
0
0.1
(c) OLC area−constr
t
0
5
10
15
20
25
30
−0.5
−0.4
−0.3
−0.2
−0.1
0
0.1
(b) OLC unconstr
t
Fig. 7: Frequency evolution: Area 2
0
10
20
30
40
50
60
−0.5
−0.4
−0.3
−0.2
−0.1
0
0.1
0.2
0.3
0.4
0.5
LMPs
λi
t
0
10
20
30
40
50
60
0
0.5
1
1.5
2
2.5
3
3.5
Inter area line flows
Pij
t
Fig. 8: LMPs and inter area line ﬂows: no thermal limits
Now, we illustrate the action of the thermal constraints by adding a constraint of P e = 2.6p.u. and P e = −2.6p.u.
to the tie lines between areas. Figure 8 shows the values of the multipliers λi, that correspond to the Locational
Marginal Prices (LMPs), and the line ﬂows of the tie lines for the same scenario displayed in Figures 6c and 7c, i.e.
without thermal limits. It can be seen that neither the initial condition, nor the new steady state satisfy the thermal
limit (shown by a dashed line). However, once we add thermal limits to our OLC scheme, we can see in Figure 9
that the system converges to a new operating point that satisﬁes our constraints.
Finally, we show the conservativeness of the bound obtained in Theorem 14. We simulate the perturbed system
(4), (41a) and (18b)-(18f) with under the same conditions as in Figure 8. We set the scalars ais such that the
corresponding δais are homogeneous for every bus i. We also do not impose the bounds (47) on di(·) and use
instead di as described in Figure 5. This last assumption actually implies that the interval in (48) is empty (because


---

Page 28

---

28
0
10
20
30
40
50
60
−1
−0.5
0
0.5
1
1.5
LMPs
λi
t
0
10
20
30
40
50
60
0
0.5
1
1.5
2
2.5
3
3.5
Inter area line flows
Pij
t
Fig. 9: LMPs and inter area line ﬂows: with thermal limits
d′ = 0).
0
50
100
150
200
−6
−5
−4
−3
−2
−1
0
1
δbi = −0.40
t
ωi
0
50
100
150
200
−0.5
−0.4
−0.3
−0.2
−0.1
0
0.1
0.2
δbi = −0.21
t
0
50
100
150
200
−0.5
−0.4
−0.3
−0.2
−0.1
0
0.1
0.2
δbi = −0.20
t
0
50
100
150
200
−0.5
−0.4
−0.3
−0.2
−0.1
0
0.1
0.2
δbi = −0.19
t
0
50
100
150
200
−0.5
−0.4
−0.3
−0.2
−0.1
0
0.1
0.2
δbi = 0.00
t
Fig. 10: Bus frequency evolution for homogeneous perturbation δai ∈{−0.4, −0.21, −0.2, −0.19, 0.0}
Figures 10 and 11 show the evolution of the frequency ωi and LMPs λi for different values of δai belonging to
{−0.4, −0.21, −0.2, −0.19, 0.0}. Since Di = 0.2 at all the buses, then δai = −0.2 is the threshold that makes ai
go from positive to negative as δai decreases.
Even though condition (48) is not satisﬁed for any δai, our simulations show that the system converges whenever
ai ≥0 (δai ≥−0.2). The case when δai = −0.2 is of special interest. Here, the system converges, yet the nominal
frequency is not restored. This is because the terms δaiωi (42) are equal to the terms Diωi in (4a)-(4b). Thus ˙ωi
and ˙λi can be made simultaneously zero with nonzero ω∗
i . Fortunately, this can only happen when ai = 0 ∀i which
can be avoided since ai is a designed parameter.


---

Page 29

---

29
0
50
100
150
200
−50
0
50
100
150
200
250
300
350
δbi = −0.40
t
λi
0
50
100
150
200
−0.5
−0.4
−0.3
−0.2
−0.1
0
0.1
0.2
0.3
0.4
δbi = −0.21
t
0
50
100
150
200
−0.5
−0.4
−0.3
−0.2
−0.1
0
0.1
0.2
δbi = −0.20
t
0
50
100
150
200
−0.5
−0.4
−0.3
−0.2
−0.1
0
0.1
0.2
δbi = −0.19
t
0
50
100
150
200
−0.5
−0.4
−0.3
−0.2
−0.1
0
0.1
0.2
δbi = 0.00
t
Fig. 11: Location Marginal Prices evolution for homogeneous perturbation δai ∈{−0.4, −0.21, −0.2, −0.19, 0.0}
VIII. CONCLUDING REMARKS
This paper studies the problem of restoring the power balance and operational constraints of a power network
after a disturbance by dynamically adapting the loads. We show that provided communication is allowed among
neighboring buses, it is possible to rebalance the power mismatch, restore the nominal frequency, and maintain inter-
area ﬂows and thermal limits. Our distributed solution converges for every initial condition and is robust to parameter
uncertainty. Several numerical simulations verify our ﬁndings and provide new insight on the conservativeness of
the theoretical sufﬁcient condition.
APPENDIX
A. Proof of Lemma 2
Proof: Assumptions 1 and 2 guarantee that the solution to the primal (OLC) is ﬁnite. Moreover, since by
Assumption 2 there is a feasible d ∈Int D, then the Slater condition is satisﬁed [31] and there is zero duality gap.
Thus, since OLC only has linear equality constraints, we can use Karush-Kuhn-Tucker (KKT) conditions [31]
to characterize the primal dual optimal solution. Thus (d∗, ω∗, P ∗, φ∗, σ∗) is primal dual optimal if and only if we
have:
(i) Primal and dual feasibility: (9b)-(9e) and ρ+∗, ρ−∗≥0.
(ii) Stationarity:
∂
∂dL(d∗, ω∗, x∗, σ∗) = 0,
∂
∂ω L(d∗, ω∗, x∗, σ∗) = 0
and
∂
∂xL(d∗, ω∗, x∗, σ∗) = 0.
(iii) Complementary slackness:
ρ+∗
ij (Bij(v∗
i −v∗
j ) −¯Pij) = 0,
ij ∈E;
ρ−∗
ij (P ij −Bij(v∗
i −v∗
j )) = 0,
ij ∈E.


---

Page 30

---

30
KKT conditions (i) and (iii) are already implicit by assumptions of the lemma.
The stationarity condition (ii) is given by
∂L
∂di
(d∗, ω∗, P ∗, φ∗, σ∗) = c′
i(d∗
i ) −(ν∗
i + λ∗
i ) = 0
(70a)
∂L
∂ωi
(d∗, ω∗, P ∗, φ∗, σ∗) = Di(ω∗
i −ν∗
i ) = 0
(70b)
∂L
∂Pij
(d∗, ω∗, P ∗, φ∗, σ∗) = ν∗
j −ν∗
i = 0
(70c)
∂L
∂φi
(d∗, ω∗, P ∗, φ∗, σ∗) =
X
j∈Ni
Bij(λ∗
j −λ∗
i )
+
X
e∈E
Ci,eBe(
X
k∈K
ˆCk,eπ∗
k + ρ+∗
e
−ρ−∗
e ) = 0
(70d)
Since Di > 0 equation (70b) implies ν∗
i = ω∗
i . Thus, (70b) and (70a) amount to the ﬁrst and second conditions
of (11). Furthermore, since the graph G is connected then (70c) is equivalent to
ν∗
i = ˆν
∀i ∈N.
which is the third condition of (11).
Since ci(di) and Diω2
i
2
are strictly convex functions, it is easy to show that ν∗
i and λ∗
i are unique. To show ˆν = 0
we use (i). Adding (9b) over i ∈N gives
0 =
X
i∈N
 
P m
i
−(d∗
i + Diω∗
i ) −
X
e∈E
CiePe
!
=
X
i∈N
(P m
i
−(d∗
i + Diω∗
i )) −
X
e=ij∈E
(CiePe + CjePe)
=
X
i∈N
(P m
i
−(d∗
i + Diω∗
i ))
(71)
and similarly (9c) gives
0 =
X
i∈N
P m
i
−d∗
i
(72)
Thus, subtracting (71) from (72) gives
0 =
X
i∈N
Diω∗
i =
X
i∈N
Diν∗
i = ˆν
X
i∈N
Di
and since Di > 0 ∀i ∈N, it follows that ˆν = 0.
B. Proof of Lemma 3
Proof: Let (d∗ω∗= 0, θ∗) be an optimal solution of OLC. Then, by letting φ∗= θ∗and P ∗= BCT θ∗, it
follows that (d∗, ω∗= 0, φ∗, P ∗) is a feasible solution of VF-OLC. Suppose that (d∗, ω∗, φ∗, P ∗) is not optimal with
respect to VF-OLC, then the solution ( ˆd∗, ˆω∗, ˆφ∗, ˆP ∗) of VF-OLC has strictly lower cost P
i∈N ci( ˆd∗
i ) + Di ˆω∗2
i
2
<
P
i∈N ci(d∗
i ). By Lemma 2 we have that ˆω∗= 0. Then, it follows that by setting ˆθ∗= ˆφ∗, ( ˆd∗, ˆω∗, ˆθ∗) is a
feasible solution of OLC with strictly lower cost than the supposedly optimal (d∗, ω∗, θ∗). Contradiction. Therefore
( ˆd∗, ˆω∗, ˆφ∗, ˆP ∗) is an optimal solution of VF-OLC. The converse is shown analogously.


---

Page 31

---

31
C. Proof of Lemma 4
Proof: A straightforward differentiation shows that the Hessian of Φi(νi, λi) is given by
∂2
∂(νi, λi)2 Φi(νi, λi) =
νi
λi
"
#
−(d′
i + Di)
−d′
i
νi
−d′
i
−d′
i
λi
(73)
where d′
i is short for d′
i(λi + νi) and denotes de derivative of di(·) = c
′−1
i
(·) with respect to its argument.
Since ci is strictly convex d′
i > 0. Thus, since Di > 0, (73) is negative deﬁnite which implies that Φi(νi, λi) is
strictly concave. Finally, it follows from (14) that L(x, σ) is strictly concave in (ν, λ).
D. Proof of Lemma 9
Proof: We ﬁrst notice that ν∗
i (x, y), i ∈L, depends only on λi and CiP := P
e∈E Ci,ePe. Which means that
∂
∂vν∗
L(x, y) = 0,
∂
∂νG ν∗
L(x, y) = 0,
∂
∂πν∗
L(x, y) = 0,
∂
∂ρν∗
L(x, y) = 0 and
∂
∂λL ν∗
L(x, y) is diagonal.
Now, by deﬁnition of ν∗
L(x, y), for any i ∈L we have
0 =
∂
∂νi
L(x, y, ν∗
L(x, y)) =
=P m
i −(Diν∗
i (x, y)+di(λi + ν∗
i (x, y)))−
X
e∈E
Ci,ePe
(74)
Therefore, if we ﬁx P and take the total derivative of
∂
∂νi L(x, y, ν∗
L(x, y)) with respect to λi we obtain
0 =
d
dλi
Å ∂
∂νi
L(x, y, ν∗
L(x, y))
ã
(75)
= −(Di + d′
i(λi + ν∗
i )) ∂
∂λi
ν∗
i −d′
i(λi + ν∗
i )
(76)
where here we used ν∗
i for short of ν∗
i (x, y).
Now since by assumption ci(·) is strongly convex, i.e. c′′
i (·) ≥α, d′
i(·) =
1
c′′
i (·) ≤1
α < ∞. Thus, (Di + d′
i) is
ﬁnite and strictly positive, which implies that
∂
∂λi
ν∗
i (x, y) = −
d′
i(λi + ν∗
i (x, y))
( Di + d′
i(λi + ν∗
i (x, y)) ),
i ∈L.
Similarly, we obtain
∂
∂P ν∗
i (x, y) = −
1
( Di + d′
i(λi + ν∗
i (x, y)) )Ci,
i ∈L.
where Ci is the ith row of C.
Finally, notice that whenever d′
i(λi + ν∗
i ) exists, then
∂
∂xν∗
i and
∂
∂yν∗
i also exists.
E. Proof of Lemma 12
Proof: Using the Envelope Theorem [36] in (16) we have
∂L
∂x (x, y) = ∂L
∂x (x, y, ν∗
L(x, y))


---

Page 32

---

32
which implies that
∂2L
∂x2 (x, y) = ∂
∂x
ï∂L
∂x (x, y, ν∗
L(x, y))
ò
= ∂2L
∂x2 (x, y, ν∗
L(x, y)) +
∂2L
∂x∂νL
(x, y, ν∗
L(x, y)) ∂
∂xν∗
L(x, y)
=
∂2L
∂x∂νL
(x, y, ν∗
L(x, y)) ∂
∂xν∗
L(x, y).
(77)
where the last step follows from L(x, σ) being linear in x.
Now, by deﬁnition of ν∗
L(x, y) it follows that
∂L
∂νL
(x, y, ν∗
L(x, y)) = 0.
(78)
Differentiating (78) with respect to x gives
0 =
∂2L
∂νL∂x(x, y, ν∗
L(x, y)) + ∂2L
∂ν2
L
(x, y, ν∗
L(x, y)) ∂
∂xν∗
L(x, y)
and therefore
∂2L
∂x∂νL
(x, y, ν∗
L(x, y)) =
ï ∂2L
∂νL∂x(x, y, ν∗
L(x, y))
òT
= −∂
∂xν∗
L(x, y)T ∂2L
∂ν2
L
(x, y, ν∗
L(x, y)).
(79)
Substituting (79) into (77) gives
∂2L
∂x2 (x, y) = −∂
∂xν∗
L(x, y)T ∂2L
∂ν2
L
(x, y, ν∗
L(x, y)) ∂
∂xν∗
L(x, y).
(80)
It follows from (20) and (15) that
∂2L
∂ν2
L
(x, y, ν∗
L(x, y)) = ∂2ΦL
∂ν2
L
(ν∗
L(x, y), λL)
= −(DL + d′
L).
(81)
Therefore, substituting (25) and (81) into (80) gives (45).
A similar calculation using (26) gives (46).
F. Proof of Lemma 13
Proof: By deﬁnition of g(x, y) we have
∂
∂y g(x, y) =
ï
0 δAG
∂
∂y νT
G δAL
∂
∂y ν∗
L(x, y)T 0 0
òT
Thus, using Lemma 9 we obtain
∂
∂xg(x, y). A similar computation gives
∂
∂yg(x, y).


---

Page 33

---

33
REFERENCES
[1] A. J. Wood, B. F. Wollenberg, and G. B. Sheble, “Power generation, operation and control,” John Wiley&Sons, 1996.
[2] A. R. Bergen and V. Vittal, Power Systems Analysis, 2nd ed.
Prentice Hall, 2000.
[3] J. Machowski, J. Bialek, and J. R. Bumby, Power System Dynamics and Stability.
John Wiley & Sons, Oct. 1997.
[4] M. D. Ilic, “From Hierarchical to Open Access Electric Power Systems,” Proceedings of the IEEE, vol. 95, no. 5, pp. 1060–1084, 2007.
[5] A. K. Bejestani, A. Annaswamy, and T. Samad, “A Hierarchical Transactive Control Architecture for Renewables Integration in Smart
Grids: Analytical Modeling and Stability,” IEEE Transactions on Smart Grid, vol. 5, no. 4, pp. 2054–2065, Jul. 2014.
[6] F. C. Schweppe, R. D. Tabors, J. L. J. Kirtley, H. R. Outhred, F. H. Pickel, and A. J. Cox, “Homeostatic Utility Control,” Power Apparatus
and Systems, IEEE Transactions on, vol. PAS-99, no. 3, pp. 1151–1163, May 1980.
[7] D. Trudnowski, M. Donnelly, and E. Lightner, “Power-system frequency and stability control using decentralized intelligent loads,” in
Transmission and Distribution Conference and Exhibition, 2005/2006 IEEE PES, May 2006, pp. 1453–1459.
[8] N. Lu and D. Hammerstrom, “Design considerations for frequency responsive grid friendlytm appliances,” in Transmission and Distribution
Conference and Exhibition, 2005/2006 IEEE PES, May 2006, pp. 647–652.
[9] J. A. Short, D. G. Inﬁeld, and L. L. Freris, “Stabilization of Grid Frequency Through Dynamic Demand Control,” Power Systems, IEEE
Transactions on, vol. 22, no. 3, pp. 1284–1293, 2007.
[10] M. Donnelly, D. Harvey, R. Munson, and D. Trudnowski, “Frequency and stability control using decentralized intelligent loads: Beneﬁts
and pitfalls,” in Power and Energy Society General Meeting, 2010 IEEE, July 2010, pp. 1–6.
[11] A. Brooks, E. Lu, D. Reicher, C. Spirakis, and B. Weihl, “Demand Dispatch,” IEEE Power and Energy Magazine, vol. 8, no. 3, pp. 20–29,
2010.
[12] D. Callaway and I. Hiskens, “Achieving controllability of electric loads,” in Proceedings of the IEEE.
IEEE, 2011, pp. 184–199.
[13] A. Molina-Garcia, F. Bouffard, and D. S. Kirschen, “Decentralized Demand-Side Contribution to Primary Frequency Control,” Power
Systems, IEEE Transactions on, vol. 26, no. 1, pp. 411–419, 2011.
[14] D. Hammerstrom, J. Brous, D. Chassin, G. Horst, R. Kajfasz, P. Michie, T. Oliver, T. Carlon, C. Eustis, O. Jarvegren, W. Marek, R. Munson,
and R. Pratt, “Paciﬁc Northwest GridWise Testbed Demonstration Projects, Part II: Grid Friendly Appliance Project,” Paciﬁc Northwest
National Lab, Tech. Rep., Oct. 2007.
[15] M. Andreasson, D. V. Dimarogonas, H. Sandberg, and K. H. Johansson, “Distributed Control of Networked Dynamical Systems: Static
Feedback, Integral Action and Consensus,” Automatic Control, IEEE Transactions on, vol. 59, no. 7, pp. 1750–1764, 2014.
[16] M. Andreasson, D. V. Dimarogonas, K. H. Johansson, and H. Sandberg, “Distributed vs. centralized power systems frequency control,” in
Control Conference (ECC), 2013 European.
IEEE, 2013, pp. 3524–3529.
[17] X. Zhang and A. Papachristodoulou, “A real-time control framework for smart power networks with star topology,” American Control
Conference (ACC), pp. 5062–5067, 2013.
[18] ——, “A real-time control framework for smart power networks: Design methodology and stability,” Automatica, vol. 58, pp. 43–50, Aug.
2015.
[19] C. Zhao, U. Topcu, N. Li, and S. Low, “Design and Stability of Load-Side Primary Frequency Control in Power Systems,” Automatic
Control, IEEE Transactions on, vol. 59, no. 5, pp. 1177–1189, 2014.
[20] N. Li, L. Chen, C. Zhao, and S. H. Low, “Connecting automatic generation control and economic dispatch from an optimization view,”
American Control Conference ( ..., pp. 735–740, 2014.
[21] E. Mallada and S. H. Low, “Distributed frequency-preserving optimal load control,” in IFAC World Congress, 2014, pp. 5411–5418.
[22] S. You and L. Chen, “Reverse and Forward Engineering of Frequency Control in Power Networks,” in Conference on Decision and Control,
2014.
[23] W. Liu, W. Gu, W. Sheng, X. Meng, Z. Wu, and W. Chen, “Decentralized Multi-Agent System-Based Cooperative Frequency Control for
Autonomous Microgrids With Communication Constraints,” Sustainable Energy, IEEE Transactions on, vol. 5, no. 2, pp. 446–456, Apr.
2014.
[24] Q. Shaﬁee, J. M. Guerrero, and J. C. Vasquez, “Distributed Secondary Control for Islanded Microgrids - A Novel Approach,” Power
Electronics, IEEE Transactions on, vol. 29, no. 2, pp. 1018–1031, 2014.
[25] F. D¨orﬂer, J. Simpson-Porco, and F. Bullo, “Breaking the Hierarchy: Distributed Control & Economic Optimality in Microgrids,” arXiv.org,
Jan. 2014.


---

Page 34

---

34
[26] J. W. Simpson-Porco, F. D¨orﬂer, F. Bullo, Q. Shaﬁee, and J. M. Guerrero, “Stability, power sharing, & distributed secondary control in
droop-controlled microgrids distributed secondary control in droop-controlled microgrids,” 2013 IEEE International Conference on Smart
Grid Communications (SmartGridComm), pp. 672–677, 2013.
[27] F. D¨orﬂer, J. W. Simpson-Porco, and F. Bullo, “Plug-and-Play Control and Optimization in Microgrids,” in Conference on Decision and
Control, 2014.
[28] C. Zhao, U. Topcu, and S. H. Low, “Optimal Load Control via Frequency Measurement and Neighborhood Area Communication,” Power
Systems, IEEE Transactions on, vol. 28, no. 4, pp. 3576–3587, 2013.
[29] E. Mallada, C. Zhao, and S. Low, “Optimal load-side control for frequency regulation in smart grids,” in Communication, Control, and
Computing Allerton, 2014 52nd Annual Allerton Conference on.
IEEE, 2014, pp. 731–738.
[30] P. Kundur, Power System Stability And Control.
McGraw-Hill, 1994.
[31] S. Boyd and L. Vandenberghe, Convex Optimization.
Cambridge University Press, Mar. 2004.
[32] F. P. Kelly, A. K. Maulloo, and D. K. H. Tan, “Rate Control for Communication Networks: Shadow Prices, Proportional Fairness and
Stability,” The Journal of the Operational Research Society, vol. 49, no. 3, pp. 237–252, Mar. 1998.
[33] S. H. Low and D. E. Lapsley, “Optimization ﬂow control. I. Basic algorithm and convergence,” IEEE/ACM Transactions on Networking,
vol. 7, no. 6, pp. 861–874, 1999.
[34] R. Srikant, The Mathematics of Internet Congestion Control, ser. Systems & Control: Foundations & Applications.
Boston, MA: Springer
Science & Business Media, Dec. 2012.
[35] D. P. Palomar and M. Chiang, “A tutorial on decomposition methods for network utility maximization,” Ieee Journal on Selected Areas
in Communications, vol. 24, no. 8, pp. 1439–1451, Aug. 2006.
[36] A. Mas-Colell, M. D. Whinston, and J. R. Green, Microeconomic Theory.
Oxford University Press, USA, 1995.
[37] K. Zhou, J. C. Doyle, K. Glover, and others, Robust and optimal control.
Prentice Hall New Jersey, 1996, vol. 40.
[38] D. Feijer and F. Paganini, “Stability of primal-dual gradient dynamics and applications to network optimization,” Automatica, vol. 46,
no. 12, pp. 1974–1981, Dec. 2010.
[39] H. K. Khalil, Nonlinear systems, 3rd ed.
Prentice Hall, 2002.
[40] A. Bacciotti and F. Ceragioli, “Nonpathological Lyapunov functions and discontinuous Carath´eodory systems,” Automatica, 2006.
[41] A. Cherukuri, E. Mallada, and J. Cort´es, “Convergence of caratheodory solutions for primal-dual dynamics in constrained concave
optimization,” in SIAM conference on control and its applications, July 2015.
[42] A. Tilli and M. Montanari, “A Low-Noise Estimator of Angular Speed and Acceleration from Shaft Encoder Measurements,”
AUTOMATIKA: Journal for Control, Measurement, Electronics, Computing and Communications, vol. 42., no. 3-4, pp. 169–176, Dec.
2001.
[43] J. H. Chow and K. W. Cheung, “A toolbox for power system dynamics and control engineering education and research,” Power Systems,
IEEE Transactions on, vol. 7, no. 4, pp. 1559–1564, 1992.
