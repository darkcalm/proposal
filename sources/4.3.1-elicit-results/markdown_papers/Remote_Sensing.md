

---

Page 1

---

Remote sensing via ℓ1-minimization
Max H¨ugel∗
Holger Rauhut†
Thomas Strohmer‡
May 4, 2012; revised April 24, 2013
Abstract
We consider the problem of detecting the locations of targets in the far ﬁeld by sending
probing signals from an antenna array and recording the reﬂected echoes. Drawing on key
concepts from the area of compressive sensing, we use an ℓ1-based regularization approach
to solve this, in general ill-posed, inverse scattering problem. As common in compressive
sensing, we exploit randomness, which in this context comes from choosing the antenna
locations at random. With n antennas we obtain n2 measurements of a vector x ∈CN
representing the target locations and reﬂectivities on a discretized grid. It is common to
assume that the scene x is sparse due to a limited number of targets. Under a natural
condition on the mesh size of the grid, we show that an s-sparse scene can be recovered
via ℓ1-minimization with high probability if n2 ≥Cs log2(N). The reconstruction is stable
under noise and under passing from sparse to approximately sparse vectors. Our theoretical
ﬁndings are conﬁrmed by numerical simulations.
AMS Subject Classiﬁcation: 65K05, 65C99, 65F22, 94A99, 90C25
Keywords: Compressive sensing, sparsity, ℓ1-minimization, inverse scattering, regulariza-
tion
1
Introduction
Our aim is to detect the locations and reﬂectivities of remote targets (point scatterers) by send-
ing probing signals from an antenna array and recording the reﬂected signals. This type of
inverse scattering — which has applications in radar, sonar, medical imaging, and microscopy
— is a rather challenging numerical problem. Typically the solution is not unique and insta-
bilities in the presence of noise are a common issue. Standard techniques, such as matched
ﬁeld processing [30] or time reversal methods [1, 18, 19] work well for the detection of very few,
well separated targets. However, when the number of targets increases and/or some targets
are adjacent to each other, these methods run into severe problems. Moreover, these methods
have major diﬃculties when the dynamic range between the reﬂectivities of the targets is large.
In [14] a compressive sensing based approach to the inverse scattering problem was proposed
to overcome the ill-posedness of the problem by utilizing the sparsity of the target scene. Here,
sparsity is meant in the sense that the targets typically occupy only a small fraction of the
∗HausdorﬀCenter for Mathematics and Institute for Numerical Simulation, University of Bonn, Bonn, Ger-
many, max.huegel@hcm.uni-bonn.de
†HausdorﬀCenter for Mathematics and Institute for Numerical Simulation, University of Bonn, Bonn, Ger-
many, rauhut@hcm.uni-bonn.de
‡Department of Mathematics, University of California at Davis, Davis CA, strohmer@math.ucdavis.edu
1
arXiv:1205.1366v3  [cs.IT]  24 Apr 2013


---

Page 2

---

0
10
20
30
40
50
60
70
80
0
10
20
30
40
50
60
70
80
 
resolution cells
 
0
1
2
3
4
5
6
7
8
9
(a)
0
10
20
30
40
50
60
70
80
0
10
20
30
40
50
60
70
80
 
resolution cells
 
1
2
3
4
5
6
7
8
(b)
Fig. 1
(a) Scene with 100 targets in 6400 resolution cells (b) Reconstruction from 900 noisy
measurements with SNR of 20dB
overall region of interest. As common in compressive sensing [13, 4, 15, 26], randomness is used
and in this setup it is realized by placing the antennas at random locations on a square. It
was proved in [14] that under certain conditions it is possible to exactly recover the locations
and reﬂectivities of the targets from noise-free measurements by solving an ℓ1-regularized
optimization problem, also known as basis pursuit in the compressive sensing literature.
While the framework in [14] can lead to signiﬁcant improvements over traditional methods,
it also has several limitations. For instance, the main theoretical result in that article requires
the targets to be randomly spaced, a condition that is quite restrictive and does not match well
with practical scenarios. Also the conditions on the number of targets that can be recovered
are far from optimal. In this paper we will overcome most of these limitations, thus leading
to a theoretical framework that is better adapted to practical applications. In particular, we
also show that recovery is stable with respect to measurement noise and under passing from
sparse to approximately sparse scenes. Figure 1 depicts the reconstruction of a sparse scene of
2


---

Page 3

---

100 targets in 6400 resolution cells with reﬂectivities in the dynamic range from 1 to 8 from
900 noisy measurements, that is with 30 antennas. Both the detection performance and the
approximation of the true values of the reﬂectivities are very good.
What makes the inverse scattering problem with antenna arrays challenging from a com-
pressive sensing viewpoint is that the associated sensing matrix is not a random matrix with
independent rows or columns, but the matrix entries are random variables which are cou-
pled across rows and columns. This in turn means that standard proof techniques from the
compressive sensing literature cannot be applied readily and results developed for structured
sensing matrices [26] are of limited use in our case. In fact, it is an open problem whether the
by now classical and often used restricted isometry property holds for the random scattering
matrix arising in our context. Instead we provide high probability recovery bounds for a ﬁxed
vector and a random choice of the scattering matrix (also referred to as nonuniform recovery
guarantees). We believe that some of the tools that we develop in this paper will potentially
be useful in other compressive sensing scenarios, where the sensing matrix has coupled rows
and columns.
Our paper is organized as follows.
In Section 2 we describe the setup of the imaging
problem and state our main results. As preparation for proving our main theorems, we derive
a general sparse recovery result in Section 3 and condition number estimates for certain random
matrices in Section 4. In Section 5 we prove the recovery of sparse vectors for sensing matrices
with dependent rows and columns which are associated with a class of bounded orthonormal
systems. This type of matrices includes the sensing matrix arising in the inverse scattering
problem as a special case. On the other hand this result assumes that the non-zero coeﬃcients
of the signal to be recovered have random phases. In Section 6 we remove the assumption of
random phases and show sparse recovery for the inverse scattering setup for signals with ﬁxed
deterministic phases. In Section 7 we illustrate our theoretical results by numerical simulations.
Acknowledgements
M.H. and H.R. acknowledge support by the HausdorﬀCenter for Mathematics and by the
ERC Starting Grant SPALORA StG 258926. T.S. was supported by the National Science
Foundation and DTRA under grant dtra-dms 1042939, and by DARPA under grant N66001-
11-1-4090. Parts of this manuscript have been written during a stay of H.R. at the Institute for
Mathematics and Its Applications, University of Minnesota, Minneapolis. T.S. thanks Haichao
Wang for useful comments on an early version of this manuscript. The authors also wish to
thank Axel Obermeier and the anonymous reviewers for helpful comments and corrections.
2
Problem formulation and main results
2.1
Array imaging setup and problem formulation
Suppose an array of n transducers is located in the square [0, B]2, where B > 0 is the array
aperture. The spatial part of a wave of wavelength λ > 0 emitted from some point source
b ∈[0, B]2 and recorded at another point r ∈R3 is given by the Green’s function G of the
Helmholtz equation,
G(r, b) := exp
  2πi
λ ∥r −b∥2

4π ∥r −b∥2
.
(2.1)
Here and in the following ∥· ∥p refers to the usual ℓp-norm.
3


---

Page 4

---

−250
−200
−150
−100
−50
0
50
100
150
200
250
−250
−200
−150
−100
−50
0
50
100
150
200
250
0
100
200
300
400
500
600
700
800
900
1000
distance
targets
at
distance
z0
resolution grid
Targets sparse in the resolution cells
antenna array
Fig. 2
The targets at distance z0 distributed sparsely in the target domain
Assume that we want to image the locations of targets which are at distance z0 > 0. For
the analysis, we make the idealizing assumption that the targets are on a discretized grid of
meshsize d0 > 0 in the target domain TD := [−L, L]2 × {z0}, where L > 0 determines the size
of the target domain. To be more precise, let us assume that each target occupies one of the
points (rj)j∈[N] ⊂TD, where [N] := {1, . . . , N} with N = ⌊2L/d0⌋2 and each rj is of the form
rj = (−L + kd0, −L + ℓd0, z0)T for some (k, ℓ) ∈[
√
N]2. See also Figure 2 for a visualization
of this setup.
In order to be able to analyze the arising sensing mechanism, we approximate the Green’s
function from (2.1) in an adequate way. To this end, we assume to be in the far ﬁeld region,
that is, the distance z0 from antenna to target satisﬁes z0 ≫B + L. Writing r = (x, y, z0)T
and b = (ξ, η, 0)T , the truncated Taylor expansion for ∥r −b∥2 around r0 := (ξ, η, z0) is given
by
∥r −b∥2 ≈z0 + ∥(x, y) −(ξ, η)∥2
2
2z0
.
(2.2)
Under the far ﬁeld assumption we obtain then that
G(r, b) ≈eG(r, b) := exp
2πiz0
λ
 exp

πi
λz0 ∥(x, y) −(ξ, η)∥2
2

4πz0
.
(2.3)
If we choose the meshsize d0 such that the crucial aperture condition [14]
ρ := d0B
λz0
∈N
(2.4)
is fulﬁlled, then the normalized system of functions
bG(b, rℓ) := 4πz0 eG (b, rℓ) ,
b ∈[0, B], ℓ∈[N],
4


---

Page 5

---

satisﬁes the convenient orthonormality relation
1
B2
Z
[0,B]2
bG(b, rm) bG(b, rℓ)db =
exp

πi
λz0

∥(xm, ym)∥2
2 −∥(xℓ, yℓ)∥2
2

B2
×
Z
[0,B]
Z
[0,B]
exp

−2πi
λz0
(xm −xℓ)ξ

exp

−2πi
λz0
(ym −yℓ)η

dξdη
= δℓm.
(2.5)
It is for this relation to hold that we make the approximation (2.3).
Let us now describe the scattering matrix.
Assume we have a vector (xj)j∈[N] ∈CN
of reﬂectivities on the resolution grid.
We sample n antenna positions b1, . . . , bn ∈[0, B]2
independently at random according to the uniform distribution on [0, B]2. If antenna element
bj ∈[0, B]2 transmits and bk ∈[0, B]2 receives, then we model the echo yjk as
yjk =
N
X
ℓ=1
bG(bj, rℓ) bG(rℓ, bk)xℓ,
(j, k) ∈[n]2.
(2.6)
This is called the Born approximation [2].
It amounts to discarding multipath scattering
eﬀects. So if the transmit-receive mode is that one antenna element transmits at a time and
the whole aperture receives the echo, the appropriately scaled sensing matrix A ∈Cn2×N is
given entrywise by
A(j,k),ℓ:= bG(bj, rℓ) bG(rℓ, bk),
(j, k) ∈[n]2, ℓ∈[N].
(2.7)
Then y = Ax by (2.6). Due to the randomness in the bk, k ∈[n], the matrix A is a (structured)
random matrix with coupled rows and columns.
In many scenarios the number of targets is small compared to the grid size. This naturally
leads to sparsity in the vector x ∈CN of reﬂectivities, ∥x∥0 := #{ℓ: xℓ̸= 0} ≤s, where s ≪N.
Compressive sensing suggests that in such a scenario, we can recover x from undersampled
measurements y = Ax ∈Cn2 when n2 ≪N. We note that A contains only n(n+1)/2 diﬀerent
rows due to the symmetries in the sensing setup. Our goal is determine a good bound on the
required minimal number of antennas n in order to ensure recovery of an s-sparse scene. A
small number of antennas has clear advantages such as low costs of imaging hardware.
2.2
Compressive sensing
We brieﬂy describe the basics of compressive sensing in order to place our results outlined below
into context. Given measurements y = Ax ∈Cm of a sparse vector x ∈CN, where A ∈Cm×N
is the so-called measurement matrix, we would like to reconstruct x in the underdetermined
case that m ≪N by taking into consideration the sparsity.
The na¨ıve approach of ℓ0-minimization
min
z∈CN ∥z∥0
subject to Az = y
(2.8)
is NP-hard [21]. Hence several tractable alternatives were proposed including ℓ1-minimization,
also called basis pursuit [10, 13, 4],
min
z∈CN ∥z∥1
subject to Az = y.
(2.9)
5


---

Page 6

---

This can be seen as a convex relaxation of (2.8) and can be solved via eﬃcient convex opti-
mization methods [3, 9]. It is by now well-understood that ℓ1-minimization can recover sparse
vectors under appropriate conditions. Remarkably, random matrices provide (near-)optimal
measurement matrices in this context and good deterministic constructions are lacking to date,
see [26, 15] for a discussion. For instance, an m × N Gaussian random matrix A ensures exact
(and stable) recovery of all s-sparse vectors x from y = Ax using ℓ1-minimization (and other
types of algorithms) with high probability provided
m ≥Cs log(N/s),
(2.10)
where C > 0 is a universal constants. This bound is optimal [13, 16]. It is crucial that m
is allowed to scale linearly in s. The log-factor cannot be removed. Recovery is stable under
passing to approximately sparse vectors and under adding noise to the measurements. In the
latter case, one may rather work with the noise-constrained ℓ1-minimization problem
min
z∈CN ∥z∥1
subject to ∥Az −y∥2 ≤η.
(2.11)
Random partial Fourier matrices [4, 7, 29, 25, 26] (that is, random row-submatrices of the
discrete Fourier matrix) and other types of structured random matrices [26, 27] also provide
s-sparse recovery under similar conditions as in (2.10) (with additional log-factors).
Some of the mentioned recovery results are derived using the restricted isometry property
(RIP) [7, 6]. This leads to uniform guarantees in the sense that once the matrix is selected,
then with high probability every s-sparse vector can be recovered from y = Ax. The RIP,
however, is a rather strong condition which is sometimes hard to verify. In particular, it is
open to verify it for our random matrix in (2.7). Instead, we may work with weaker conditions,
which ensure nonuniform recovery in the sense that a ﬁxed s-sparse vector is recovered with
high probability using a random draw of the matrix.
Our result below for the structured
random matrix in (2.7) is based on the extension of certain general recovery conditions for
ℓ1-minimization [17, 32, 5] to stable recovery using a so-called dual certiﬁcate, see Section 3.
2.3
Main results
We deﬁne the error of best s-term approximation in the ℓ1-norm by
σs(x)1 :=
inf
∥z∥0≤s ∥x −z∥1.
Furthermore, we will assume throughout that the aperture condition
ρ := d0B
λz0
∈N
(2.12)
holds, which can be accomplished by an appropriate choice of the meshsize d0. The further
notation is the one used in Section 2.1.
We will refer to the matrix A ∈Cn2×N in (2.7)
with the antenna positions b1, . . . , bn selected independently and uniformly at random from
[0, B]2 as the random scattering matrix. Note that the aperture condition (2.12) implies that
EA∗A = n2 Id by a similar computation as in (2.5), that is, in expectation the matrix A∗A
behaves nicely, which will be crucial in the proof. Let us now state our nonuniform recovery
result.
6


---

Page 7

---

Theorem 2.1. Let x ∈CN and A ∈Cn2×N be a draw of the random scattering matrix. Let
s ∈N be some sparsity level. Suppose we are given noisy measurements y = Ax + e ∈Cn2 with
∥e∥2 ≤ηn. If, for ε > 0,
n2 ≥Cs log2
cN
ε

(2.13)
with universal constants C, c > 0, then with probability at least 1 −ε, the solution bx ∈CN to
the noise-constrained ℓ1-minimization problem
min
z∈CN ∥z∥1
subject to ∥Az −y∥2 ≤ηn.
(2.14)
satisﬁes
∥x −bx∥2 ≤C1
√sη + C2σs(x)1.
(2.15)
The constants satisfy C ≤
 800e3/42 ≈2.87 · 106, c ≤6, C1 ≤4(1 +
√
2) + 8
√
3 ≈23.513,
C2 ≤4(1 +
√
6) ≈13.798.
Remark 2.2.
(a) The constants appearing in Theorem 2.1 are quite large and reﬂect a worst
case analysis. No attempt has been made to optimize the above bounds. In practice, much
better bounds can be expected, see also the numerical results below.
(b) The scaling of the noise level, ∥e∥2 ≤ηn is natural because e ∈Cn2. Indeed, if we have
a componentwise bound |ej| = |(Ax)j −yj| ≤η for all j ∈[n]2 then it is satisﬁed.
(c) The error bound (2.15) is slightly worse than the one we would get under the RIP. In
fact, if A has the RIP then the associated error bound improves the right hand side of
(2.15) by a factor of s−1/2 [6]. Unfortunately, it is so far unknown whether the random
scattering matrix A obeys the RIP under a similar condition as (2.13), so that the error
bound (2.15) is the best one can presently achieve.
(d) If x is s-sparse, σs(x)1 = 0, and if there is no noise, η = 0, then (2.15) implies exact
reconstruction, bx = x, by equality-constrained ℓ1-minimization (2.9).
(e) We can specialize the error bound in the previous theorem for the case of Gaussian noise.
To this end, assume that the components of e ∈Cn2 are i.i.d. complex Gaussians with
variance η2, where the real and imaginary part of a complex Gaussian are independent
real Gaussians with variance η2/2. A standard calculation shows that the noise satisﬁes
∥e∥2 ≤ηn log(1/ε) with probability at least 1 −ε. Assuming that e is independent of the
matrix A, it follows that the solution ˆx of noise-constrained ℓ1-minimization with bound
∥Az −y∥2 ≤ηn log(1/ε) satisﬁes
∥ˆx −x∥2 ≤C1η√s log(1/ε) + C2σs(x)1
(2.16)
with probability at least (1 −ε)2. The constants C1, C2 satisfy the bounds of Theorem
2.1.
Theorem 2.1 holds for a ﬁxed, deterministic x ∈CN. We deﬁne the sign of a number a ∈C
as
sgn(a) =
( a
|a|
if a ̸= 0,
0
if a = 0.
7


---

Page 8

---

For a vector x ∈CN we denote by sgn(x) := (sgn(xj))j∈[N] the sign pattern of x. On the way
to the proof of Theorem 2.1, we will provide the easier result stated next for the case when
the sign pattern of x restricted to its support set T ⊂[N], sgn(x)T = (sgn(xj))j∈T , forms a
Rademacher or a Steinhaus sequence. The latter amounts to assuming that the phases of the
reﬂectivities are iid uniformly distributed on [0, 2π], which is a common assumption in array
imaging and radar signal processing. Theorem 2.3 below actually establishes sparse recovery
in a more general setting than the inverse scattering problem. It is not only applicable to
the radar-type sensing matrices analyzed above, but to more general sensing matrices whose
rows and columns are not independent, and whose entries are associated with a certain class of
orthonormal systems. Its statement requires the notion of bounded orthonormal systems [26].
Deﬁnition 2.1. Let D ⊂Rd be a measurable set and ν a probability measure on D. A system
of functions {Φk : D →C}k∈[N] is called a bounded orthonormal system (BOS) with respect
to (D, ν) if
Z
D
Φk(t)Φℓ(t)ν(dt) = δkℓ
and if the functions are uniformly bounded by a constant K ≥1,
max
k∈[N] ∥Φk∥∞≤K.
Let now {Φℓ}ℓ∈[N] be a BOS on (D, ν) with bounding constant K = 1 and with the property
that

Φ2
ℓ
	
ℓ∈[N] is also a BOS on (D, ν). Note that due to the orthogonality relation, we then
necessarily have |Φℓ(t)| = 1 for all t ∈D. The functions Φℓ(t) = bG(rℓ, t), t ∈[0, B]2 fall into
this setup when the aperture condition (2.12) is satisﬁed, see also (2.5). Another example is
provided by the Fourier system {Φℓ}ℓ∈Z, where Φℓ(t) = e2πiℓt, ℓ∈Z, t ∈[0, 1]. For b1, b2 ∈D,
set
v(b1, b2) :=

Φℓ(b1) Φℓ(b2)

ℓ∈[N] ∈CN.
Sample now n elements b1, . . . , bn independently at random according to ν from D. Deﬁne the
sampling matrix A via
A := (v(bj, bk)∗)j,k∈[n] ∈Cn2×N,
(2.17)
so that A is the matrix with rows v(bj, bk)∗, (j, k) ∈[n]2. Note that with the system Φℓ(b) =
bG(rℓ, b) we recover the random scattering matrix (2.7) in this way.
Now we can state our main result for random sign patterns. We recall that the entries of
a (random) Rademacher vector ϵ are independent random variables that take the values ±1
with equal probability. Similarly, a Steinhaus vector is a random vector where all entries are
independent and uniformly distributed on the complex torus {z ∈C : |z| = 1}.
Theorem 2.3. Let A ∈Cn2×N be a draw of the random sampling matrix from (2.17). Let
x ∈CN and T ⊂[N] be the index set corresponding to its s largest absolute entries. Assume
that the sign vector sgn(x)T of x restricted to T forms a Rademacher or a Steinhaus sequence.
Suppose we take noisy measurements y = Ax + e ∈Cn2 with ∥e∥2 ≤ηn. If
n2 ≥Cs log
c1(N −s)
ε

log2  c2(N −s)2s/ε

,
(2.18)
8


---

Page 9

---

then with probability at least 1 −ε, the solution bx ∈CN to noise-constrained ℓ1-minimization
(2.14) satisﬁes
∥bx −x∥2 ≤C1
√sη + C2σs(x)1.
(2.19)
The constants satisfy C ≤1024, c1 ≤8, c2 ≤576, C1 ≤4(1 +
√
2) + 8
√
3 ≈23.513, C2 ≤
4(1 +
√
6) ≈13.798.
Remark 2.4. Whereas the bounds on the constants in Theorem 2.1 are quite large, and cer-
tainly improvable, in the case of random sign patterns, the number of antennas required must
satisfy
n ≥32√s log3/2 (cN/ε) ,
which is a reasonable bound, see also the improvement in Remark 4.6 (b).
3
Stable sparse recovery via ℓ1-minimization
In this section we establish a general result for the recovery of an individual vector x ∈CN
from noisy measurements y = Ax + e ∈Cm with A ∈Cm×N. It uses a dual vector in the spirit
of [17, 32] and extends these results to the noisy and non-sparse case. The proof is inspired by
[5] for recovery based on the weak RIP. However, since we actually do not assume the weak
RIP, the error bound in (3.5) below is slightly worse by a factor of √s than the one in [5,
Section 4]. In the noiseless and exact sparse case the theorem below implies exact recovery
similar to [17, 32].
For a set T ⊂[N] and a matrix A ∈Cm×N with columns aj ∈Cm, j ∈[N], we denote
by AT = (aj)j∈T ∈Cm×|T| the column-submatrix of A with columns indexed by T and by
T c := [N] \ T the complement of T in [N]. Similarly, we denote by xT ∈C|T| the vector
x ∈CN restricted to its entries in T. The operator norm of a matrix B on ℓ2 is denoted by
∥B∥2→2.
Theorem 3.1. Let x ∈CN and A ∈Cm×N with ℓ2-normalized columns, ∥aj∥2 = 1, j ∈[N].
For s ≥1, let T ⊂[N] be the set of indices of the s largest absolute entries of x. Assume that
AT is well-conditioned in the sense that
∥A∗
T AT −Id∥2→2 ≤1
2
(3.1)
and that there exists a dual certiﬁcate u = A∗v ∈CN with v ∈Cm such that
uT = sgn(x)T ,
(3.2)
∥uT c∥∞≤1
2,
(3.3)
∥v∥2 ≤
√
2s.
(3.4)
Suppose we are given noisy measurements y = Ax + e ∈Cm with ∥e∥2 ≤η. Then the solution
bx ∈CN to noise-constrained ℓ1-minimization (2.11) satisﬁes
∥x −bx∥2 ≤C1
√sη + C2σs(x)1.
(3.5)
The constants satisfy C1 ≤4(1 +
√
2) + 8
√
3 ≈23.513, C2 ≤4(1 +
√
6) ≈13.798.
9


---

Page 10

---

Remark 3.2. The constants appearing in the conditions above are rather arbitrary and chosen
for convenience.
Proof. Write bx = x + h. Due to (2.11) and the assumption on the noise level, ∥e∥2 ≤η, we
have
∥Ah∥2 = ∥Ax −y −(Abx −y)∥≤∥Ax −y∥2 + ∥Abx −y∥2 ≤2η.
(3.6)
Since x is feasible for the optimization program (2.11) we obtain
∥x∥1 ≥∥bx∥1 = ∥(x + h)T ∥1 + ∥(x + h)T c∥1
≥Re (⟨(x + h)T , sgn(x)T ⟩) + ∥hT c∥1 −∥xT c∥1
= ∥x∥1 + Re (⟨hT , sgn(x)T ⟩) + ∥hT c∥1 −2 ∥xT c∥1 ,
where we applied H¨older’s and the triangle inequality in the second line. Rearranging the
above yields
∥hT c∥1 ≤|Re (⟨hT , sgn(x)T ⟩)| + 2 ∥xT c∥1 .
(3.7)
Let u = A∗v be the dual certiﬁcate. Then, using the Cauchy-Schwarz and H¨older’s inequality
|Re (⟨hT , sgn(x)T ⟩)| = |Re (⟨hT , (A∗v)T ⟩)| ≤|⟨h, A∗v⟩| + |⟨hT c, uT c⟩|
≤∥Ah∥2 ∥v∥2 + ∥hT c∥1 ∥uT c∥∞≤2
√
2sη + 1
2 ∥hT c∥1 ,
where we used (3.3) and (3.4) in the last line. Plugging into (3.7) yields
∥hT c∥1 ≤4
√
2s η + 4 ∥xT c∥1 .
(3.8)
Due to (3.1), we have
1
2 ∥hT ∥2
2 ≤∥AT hT ∥2
2 = ⟨AT hT , Ah⟩−⟨AT hT , AT chT c⟩.
(3.9)
Using H¨older’s inequality, the normalization of the columns of A and (3.6), we obtain
|⟨AT hT , Ah⟩| ≤∥hT ∥1 ∥A∗
T Ah∥∞≤2√sη ∥hT ∥2 .
The triangle inequality and the Cauchy Schwarz inequality give, by noting that (3.1) implies
∥AT ∥2→2 ≤
q
3
2,
|⟨AT hT , AT chT c⟩| ≤
X
j∈T c
|hj||⟨AT hT , aj⟩| ≤
X
j∈T c
|hj|∥AT hT ∥2∥aj∥2 ≤
r
3
2∥hT ∥2∥hT c∥1.
Inserting into (3.9) we obtain
∥hT ∥2 ≤4√sη +
√
6 ∥hT c∥1 .
(3.10)
Combining (3.8) and (3.10) we arrive at
∥h∥2 ≤∥hT ∥2 + ∥hT c∥1
≤(4(1 +
√
2) + 8
√
3)√sη + 4(1 +
√
6) ∥xT c∥1 .
Due to the choice of T we have ∥xT c∥1 = σs(x)1. This completes the proof.
10


---

Page 11

---

4
Conditioning of submatrices
Theorem 3.1 requires to ﬁnd a dual certiﬁcate u = A∗v with uT = sgn(x)T , where A is the
random scattering matrix introduced in Section 2.1 and T ⊂[N] is some support set. Condition
(3.1) in Theorem 3.1 suggests to investigate the conditioning of AT . Recall that
v(bj, bk) =

Φℓ(bj) Φℓ(bk)

ℓ∈[N] ∈CN,
where {Φℓ} is a bounded orthonormal system with constant K = 1 such that {Φ2
ℓ} is also
a bounded orthonormal system. The rows of the random scattering matrix A ∈Cn2×N are
the vectors v(bj, bk)∗∈C1×N, (j, k) ∈[n]2, where the b1, . . . , bn are selected independently at
random according to the orthonormalization measure ν, see (2.17) and Deﬁnition 2.1. The
scattering matrix A in (2.7) is a special case of this setup.
We aim at a probabilistic estimate of the largest and smallest singular value of 1
nAT ∈Cn2×s,
i.e., the operator norm

1
n2 A∗
T AT −Id

2→2
=

1
n2
n
X
j,k=1
v(bj, bk)T v(bj, bk)∗
T −Id

2→2
.
(4.1)
The central result of this section stated next provides an estimate of the tail of this quantity.
Theorem 4.1. Let A ∈Cn2×N be the random matrix described above and let T ⊂[N] be a
(ﬁxed) subset of cardinality |T| = s. If, for δ, ε > 0,
n2 ≥1024δ−2s log2
576s3
ε

(4.2)
then
P

1
n2 A∗
T AT −Id

2→2
≥δ

≤ε.
(4.3)
The proof will be given after some auxiliary results are presented.
4.1
Auxiliary results
The fact that the rows of A are not independent makes the analysis diﬃcult at ﬁrst sight.
In order to increase the amount of independence, we will use a version of the tail decoupling
inequality in Theorem 3.4.1 of [12] . For convenience, we provide a short proof, which essentially
repeats the one in [11] in our slightly more general setup. In this way, we also obtain better
constants than by tracing the ones in the proof of [12, Theorem 3.4.1].
Theorem 4.2. Let (Xi)i∈[n], n ≥2, be independent random variables with values in a mea-
surable space Ω. Let h : Ω× Ω→B be a measurable map with values in a separable Banach
space B with norm ∥·∥. Then there exists a subset S ⊂[n] such that
P



X
i̸=j
h(Xi, Xj)

> t

≤36 P

4

X
i∈S,j∈Sc
h(Xi, Xj)

> t

∨
36 P

4

X
i∈Sc,j∈S
h(Xi, Xj)

> t

,
(4.4)
where for a, b ∈R we denote a ∨b := max {a, b}.
11


---

Page 12

---

The proof of Theorem 4.2 employs Corollary 3.3.8 from [12].
Lemma 4.3. Let (B, ∥·∥) be a separable Banach space and let Y be a B-valued random vector
such that for each ξ ∈B∗, the dual space of B, the map ξ(Y ) is measurable, centered and
square integrable. Then, for every x ∈B,
P (∥x + Y ∥≥∥x∥) > 1
4 inf
ξ∈B∗



E [|ξ(Y )|]

E
h
|ξ(Y )|2i1/2



2
.
(4.5)
Proof of Theorem 4.2. Set D := (Xi)i∈[n] and let ϵ = (ϵ1, . . . , ϵn) be a Rademacher sequence
independent of D. We introduce
Z :=
X
i̸=j
h(Xi, Xj) −
X
i̸=j
ϵiϵjh(Xi, Xj)
(4.6)
and Y := −P
i̸=j ϵiϵjh(Xi, Xj). Observe that
E [Z |D] =
X
i̸=j
h(Xi, Xj).
Let ξ be an element of the dual space B∗. Conditional on D, ξ(Y ) is a homogeneous scalar-
valued Rademacher chaos of order 2. By H¨older’s inequality, we have for an arbitrary random
variable V with ﬁnite fourth moment that
E
h
|V |2i
≤(E [|V |])1/2 
E
h
|V |3i1/2
≤(E [|V |])1/2 
E
h
|V |2i1/4 
E
h
|V |4i1/4
and therefore
E
h
|V |2i

E
h
|V |4i1/2 ≤
E [|V |]

E
h
|V |2i1/2 .
(4.7)
Lemma 2.1 from [11] states that

E
h
|ξ(Y )|4 D
i1/2
≤3E
h
|ξ(Y )|2 D
i
.
Plugging this result into (4.7) gives
E [|ξ(Y )| |D]

E
h
|ξ(Y )|2 |D
i1/2 ≥
E
h
|ξ(Y )|2 |D
i

E
h
|ξ(Y )|4 |D
i1/2 ≥1
3.
Taking into account (4.6), an application of Lemma 4.3 yields
P

∥Z∥≥

X
i̸=j
h(Xi, Xj)

D

≥1
4
1
3
2
= 1
36.
(4.8)
12


---

Page 13

---

Multiplying both sides of (4.8) by the characteristic function χ of the event
nP
i̸=j h(Xi, Xj)
 > t
o
and taking the expectation with respect to D gives
P



X
i̸=j
h(Xi, Xj)

> t

≤36P (∥Z∥> t) = 36Eϵ

E

χ{∥Z∥>t}|ϵ

.
(4.9)
We conclude by noting that there is a vector ϵ∗∈{±1}n such that
E

χ{∥Z∥>t}|ϵ∗
≥Eϵ

E

χ{∥Z∥>t}|(ϵ1, . . . , ϵn)

.
The claim now follows by setting S := {i ∈{1, . . . , n}|ϵ∗
i = 1}.
We will moreover need the following complex version of Hoeﬀding’s inequality from [22],
equation (9).
Theorem 4.4. Let ξ1, . . . , ξn be complex, independent and centered random variables satisfying
|ξk| ≤αk for constants α1, . . . , αn > 0. Set σ2 := Pn
k=1 α2
k. Then
P
 
n
X
k=1
ξk
 > t
!
≤4 exp

−t2
4σ2

.
(4.10)
The ﬁnal tool to prove that submatrices of A are well-conditioned is the noncommutative
Bernstein inequality from [31].
Theorem 4.5. Let X1, . . . , Xn ∈Cs×s be a sequence of independent, mean zero and self-adjoint
random matrices. Assume that, for some K > 0,
∥Xℓ∥2→2 ≤K
a.s. for all ℓ∈[n]
(4.11)
and set
σ2 :=

n
X
ℓ=1
EX2
ℓ

2→2
.
(4.12)
Then, for t > 0, it holds that
P
 
n
X
ℓ=1
Xℓ

2→2
≥t
!
≤2s exp

−
t2/2
σ2 + Kt/3

.
(4.13)
4.2
Proof of Theorem 4.1
Denote by
Dj := diag

Φℓ(bj) : ℓ∈T

∈Cs×s
the diagonal matrix with diagonal consisting of the vector

Φℓ(bj)

ℓ∈T ∈Cs and introduce
g(bk) :=

Φℓ(bk)

ℓ∈T ∈Cs. Since DjD∗
j = Id we observe that
1
n2 A∗
T AT −Id = 1
n2
n
X
j,k=1
[v(bj, bk)T v(bj, bk)∗
T −Id] = 1
n2
n
X
j=1
Dj
 n
X
k=1
[g(bk)g(bk)∗−Id]
!
D∗
j.
(4.14)
13


---

Page 14

---

Let b′ := (b′
1, . . . , b′
n) denote an independent copy of b := (b1, . . . , bn). By the triangle inequal-
ity, we have
P

1
n2 A∗
T AT −Id

2→2
≥δ

≤P

1
n2

X
j̸=k
[v(bj, bk)T v(bj, bk)∗
T −Id]

2→2
≥δ
2


+ P

1
n2

n
X
j=1
[v(bj, bj)T v(bj, bj)∗
T −Id]

2→2
≥δ
2


Using the decoupling inequality of Theorem 4.2, with S ⊂[n] denoting the corresponding set,
and the symmetry relation v(bj, bk) = v(bk, bj), we obtain for the ﬁrst term above
P

1
n2

X
j̸=k
[v(bj, bk)T v(bj, bk)∗
T −Id]

2→2
≥δ
2


≤36P

1
n2

X
j∈S,k∈Sc

v(bj, b′
k)T v(bj, b′
k)∗
T −Id


2→2
≥δ
8

.
(4.15)
We will now estimate the right hand side of (4.15). Introducing
X′ :=
X
k∈Sc

g(b′
k)g(b′
k)∗−Id

∈Cs×s,
we observe that (4.14) together with Fubini’s theorem yields
36P

1
n2

X
j∈S,k∈Sc

v(bj, b′
k)T v(bj, b′
k)∗
T −Id


2→2
≥δ
8


=36P

1
n2

X
j∈S
DjX′D∗
j

2→2
≥δ
8

= Eb′

36Pb

1
n2

X
j∈S
DjX′D∗
j

2→2
≥δ
8



.
(4.16)
As the next step we apply the noncommutative Bernstein inequality, Theorem 4.5, to the inner
probability in (4.16). Since Dj is a unitary matrix and the functions Φℓare orthonormal we
have
DjX′D∗
j

2→2 =
X′
2→2 ,
(4.17)
E

(DjX′D∗
j)2
= diag
 X′2
,
where diag
 X′2
denotes the matrix that coincides with X′2 on the diagonal and is zero
otherwise. Set µ to be the coherence parameter
µ :=
max
ℓ,˜ℓ∈T:ℓ<˜ℓ

X
k∈Sc
Φℓ(b′
k)Φ˜ℓ(b′
k)
 .
A crucial observation is that diag
 X′2
⪯(s −1) diag
 µ2, µ2, . . . , µ2
, where ⪯denotes the
semideﬁnite ordering. Therefore, it holds that

X
j∈S
E

(DjX′D∗
j)2

2→2
≤|S| (s −1)µ2 ≤n(s −1)µ2.
(4.18)
14


---

Page 15

---

Plugging the bounds (4.17) and (4.18) into (4.13) yields
Pb

1
n2

X
j∈S
DjX′D∗
j

2→2
≥δ
8

≤2s exp
 
−
δ2
128(s−1)
n3
µ2 + 16δ
3n2 ∥X′∥2→2
!
.
(4.19)
Set ˜ε = ε/36. Multiplying the inner probability in (4.16) by the characteristic function of the
event E := E1 ∩E2, where
E1 :=
128(s −1)
n3
µ2 ≤
δ2
2 log (8s/˜ε)

,
E2 :=
 16
3n2
X′
2→2 ≤
δ
2 log (8s/˜ε)

,
we obtain, with Ec
1 and Ec
2 denoting the complements of E1 and E2,
36 P

1
n2

X
j∈S
DjX′D∗
j

2→2
≥δ
8

≤ε
4 + 36 (2sP (Ec
1) + 2sP (Ec
2)) .
(4.20)
Therefore, it remains to estimate the probabilities of the events Ec
1 and Ec
2. For the event Ec
1,
the union bound over all s(s −1)/2 ≤s2/2 two element subsets of T implies in the case of a
general BOS that
36 (2sP (Ec
1)) ≤72sP


[
ℓ,˜ℓ∈T,ℓ<˜ℓ



128(s −1)
n3

X
k∈Sc
Φℓ(b′
k)Φ˜ℓ(b′
k)

2
≥
δ2
2 log (8s/˜ε)





≤72s
X
ℓ,˜ℓ∈T,ℓ<˜ℓ
P
 
X
k∈Sc
Φℓ(b′
k)Φ˜ℓ(b′
k)
 ≥
δn3/2
p
256s log (8s/˜ε)
!
(4.21)
≤144s3 exp

−
n2δ2
1024s log (8s/˜ε)

,
(4.22)
where we have applied Hoeﬀding’s inequality in the form of Theorem 4.4 in the last line. The
right hand side of (4.22) is less than ε/4 provided
n2 ≥1024δ−2s log2  576s3/ε

.
(4.23)
As for Ec
2, we are going to apply the noncommutative Bernstein inequality again. Noting that
g(b′
k)g(b′
k)∗−Id

2→2 = s −1,

X
k∈Sc
E
h g(b′
k)g(b′
k)∗−Id
2i
2→2
= |Sc| (s −1) ≤n(s −1),
we obtain
36 (2sP (Ec
2)) ≤144s2 exp
 
−
δ2
  32
3
2 s
n3 log2 (8s/˜ε) + 32
9 δ s
n2 log (8s/˜ε)
!
.
(4.24)
15


---

Page 16

---

Assuming (4.23), the right hand side of (4.24) is less than ε/4. Since

Φ2
k
	
k∈[N] is also a BOS
with respect to (D, ν), Condition (4.23) implies, after another application of the noncommu-
tative Bernstein inequality analogously to (4.24) and the preceding steps, that
P

1
n2

n
X
j=1
[v(bj, bj)T v(bj, bj)∗
T −Id]

2→2
≥δ
2

≤ε
4.
(4.25)
This concludes the proof.
Remark 4.6.
(a) In order to show (4.25), we used the assumption that

Φ2
k
	
k∈[N] is also a
BOS with respect to (D, ν). It might be that (4.25) also holds under weaker assumptions
on the BOS, however, it does not hold if we choose for example the Hadamard system.
(b) Assuming the special case of the scattering matrix (2.7), the terms in (4.21) take the
form
Φℓ(bk)Φ˜ℓ(bk) = exp
 πi
λz0

∥rℓ∥2
2 −
r˜ℓ
2
2

exp
2πi
λz0
⟨(r˜ℓ−rℓ), bk⟩

,
where due to the aperture condition (2.4)
˜θk := exp
2πi
λz0
⟨(r˜ℓ−rℓ), bk⟩

is a Steinhaus random variable and ˜θ := (˜θ1, . . . , ˜θn) is a Steinhaus sequence. We can
therefore apply Hoeﬀding’s inequality for Steinhaus sequences, see [26], Corollary 6.13.
This inequality states that, for arbitrary v ∈Cn and κ ∈(0, 1),
P
⟨v, ˜θ⟩
 > t

≤
1
1 −κ exp
 
−κ t2
∥v∥2
2
!
.
(4.26)
Applying this result with κ = 4/5 instead of Theorem 4.4 in (4.21), one obtains that the
claimed spectral norm estimate (4.3) holds under the slightly improved condition
n2 ≥320δ−2s log
288s
ε

log
720s3
ε

,
(4.27)
where we have also taken into consideration the precise form of (4.22).
5
Nonuniform Recovery of Scatterers with Random Phase
Proof of Theorem 2.3. The key idea of the proof is to apply Theorem 3.1. Note ﬁrst that (2.14)
is equivalent to
argmin
z∈CN ∥z∥1
subject to

1
nAz −1
ny
 ≤η.
(5.1)
Let T ⊂[N] be the index set corresponding to the s largest absolute entries of x and assume
that sgn(x)T is either a Rademacher or a Steinhaus sequence. Suppose we are on the event
E :=

1
n2 A∗
T AT −Id

2→2
≤1
2

.
(5.2)
16


---

Page 17

---

Theorem 4.1 states that P [Ec] ≤ε/2 if
n2 ≥4096s log2  1152s3/ε

.
(5.3)
Set ˜A := 1
nA. The event E means in particular that ˜AT fulﬁlls condition (3.1). We deﬁne the
vector v ∈Cn2 in Theorem 3.1 via
v :=

˜A†∗
sgn(x)T = ˜AT

˜A∗
T ˜AT
−1
sgn(x)T ,
(5.4)
where ˜A† denotes the pseudo-inverse of ˜AT . Setting u := ˜A∗v, we have uT = ˜A∗
T v = sgn(x)T ,
so that (3.2) is satisﬁed. Since we are on the event E, the smallest singular value of ˜AT satisﬁes
σmin( ˜AT ) ≥1/
√
2 and therefore
∥v∥2 ≤∥˜A†∥2→2∥sgn(x)T ∥2 ≤σmin( ˜AT )−1√s ≤
√
2s.
Hence, also (3.4) is satisﬁed. It remains to check (3.3). To this end, note that
∥uT c∥∞= max
ℓ∈T c


˜A∗
T ˜AT
−1 ˜A∗
T ˜aℓ, sgn(x)T
 = max
ℓ∈T c
⟨˜A†
T ˜aℓ, sgn xT ⟩
 .
As in the previous section, we denote b = (b1, . . . , bn).
Since sgn(x)T =: (θℓ)ℓ∈T =: θ is
a Rademacher or a Steinhaus sequence, condition (5.3), Fubini’s Theorem and Hoeﬀding’s
inequality for Rademacher resp. Steinhaus sequences together with the union bound give
P

max
ℓ∈T c
⟨˜A†
T ˜aℓ, sgn(x)T ⟩
 > 1
2

≤P

max
ℓ∈T c
⟨˜A†
T ˜aℓ, sgn(x)T ⟩
 > 1
2

∩E

+ ε
2
≤Eb
"
χE
X
ℓ∈T c
Pθ
⟨˜A†
T ˜aℓ, sgn(x)T ⟩
 > 1
2
#
+ ε
2
≤Eb

χE
X
ℓ∈T c
2 exp


−
1
8
 ˜A†
T ˜aℓ

2
2




+ ε
2
≤2(N −s)Eb

χE exp


−
1
8 maxℓ∈T c
 ˜A†
T ˜aℓ

2
2




+ ε
2.
(5.5)
Since we are on the event E from (5.2), it follows as before that


˜A∗
T ˜AT
−1
2→2
≤
1
σmin( ˜
AT)
2 ≤
2 and therefore
max
ℓ∈T c
 ˜A†
T ˜aℓ

2
2 ≤4 max
ℓ∈T c
 ˜A∗
T ˜aℓ

2
2 ≤4s
max
ℓ∈T c,˜ℓ∈T
⟨˜aℓ, ˜a˜ℓ⟩
2 .
Set
µ :=
max
ℓ∈T c,˜ℓ∈T

n
X
k=1
Φℓ(bk)Φ˜ℓ(bk)
 .
Since
⟨˜aℓ, ˜a˜ℓ⟩
 =

n
X
k=1
Φℓ(bk)Φ˜ℓ(bk)

2
,
17


---

Page 18

---

we have
max
ℓ∈T c
 ˜A†
T ˜aℓ

2
2 ≤4 s
n4 µ4.
We then obtain
2(N −s)Eb

χE exp


−
1
8 maxℓ∈T c
 ˜A†
T ˜aℓ

2
2





≤2(N −s)Eb

χE exp

−
1
32 s
n4 µ4

≤ε
4 + 2(N −s)Pb
 
s1/4
n µ >
1
(32 log (8(N −s)/ε))1/4
!
.
Applying the union bound and Hoeﬀding’s inequality as in (4.22) gives
2(N −s)Pb
 
s1/4
n µ >
1
(32 log (8(N −s)/ε))1/4
!
≤8(N −s)2s exp
 
−
n
16
p
2s log (8(N −s)/ε)
!
.
(5.6)
The condition
n ≥32√s log1/2 (8(N −s)/ε) log
 576(N −s)2s/ε

(5.7)
implies that the right hand side of equation (5.6) is less than ε/4. Assuming s ≤N/3 and
8(N −s)/ε ≥e4, (5.7) implies (5.3) and therefore also P (Ec) ≤ε/2, where E is the event
from (5.2). We have thus veriﬁed that under condition (5.7), all conditions of Theorem 3.1 are
satisﬁed with probability at least 1 −ε. Since we work with the rescaled version (5.1) of A,
the solution ˆx satisﬁes (2.19) with the required probability. This ﬁnishes the proof of Theorem
2.3.
Remark 5.1. In the special case of the scattering matrix (2.7), we can apply the same technique
as in Remark 4.6 (b) to obtain a slight improvement of (5.7). In fact, assuming also the mild
condition 8(N −s)/ε ≥e7, all conditions of Theorem 3.1 are satisﬁed with probability at least
1 −ε under the improved condition
n ≥5
√
2s log1/2 (8(N −s)/ε) log
 576s(N −s)2/ε

.
6
Nonuniform Recovery of Scatterers with Deterministic Phase
6.1
Set partitions
To prove the central result of this section, we will require a few facts on certain partitions
of the set [N], N ∈N. As in [25, Section 2.2] we deﬁne P (N, k) as the set of all partitions
of [N] into exactly k blocks such that each block contains at least two elements. Note that
then necessarily k ≤N/2. The numbers S2(N, k) := |P(N, k)| are called associated Stirling
numbers of the second kind. In [25, Section 3.5] it was shown that
S2(N, k) ≤
3N
2
N−k
.
(6.1)
18


---

Page 19

---

For our purposes, we will also need partitions of [N] in which not necessarily all blocks contain
at least two elements.
Deﬁnition 6.1. For N ≥1, t ≤k ≤N, we deﬁne P (N, k, k −t) as the set of all partitions
of [N] into k blocks such that k −t of these blocks contain at least two elements. Moreover, we
deﬁne Pex (N, k, k −t) as the set of all partitions of [N] into k blocks such that exactly k −t
blocks contain at least two elements and exactly t blocks contain exactly one element.
The above deﬁnition of P (N, k, k −t) implies that necessarily 2(k−t) ≤N −t and therefore
k ≤N + t
2
.
(6.2)
Our next goal is a convenient estimate of the numbers S (N, k, k −t) := |P (N, k, k −t)|. We
ﬁrst observe that
S (N, k, k −t) =
t
X
r=0
|Pex (N, k, k −r)| .
Moreover, we have
|Pex (N, k, k −r)| =
N
r

S2(N −r, k −r) ≤
N
r
 3N
2
N−k
,
(6.3)
where the last inequality follows from the estimate (6.1). Since t ≤N and therefore Pt
r=0
 N
r

≤
2N, this yields
S (N, k, k −t) ≤(3N)N
3N
2
−k
.
(6.4)
This estimate will become crucial in the next section.
6.2
Construction of a dual certiﬁcate
We will use combinatorial estimates inspired by the analysis in [4, 27, 25, 8] in order to construct
a dual certiﬁcate. Hereby, we exploit the estimates on set partitions stated above. In this way,
we will extend the recovery result of Section 2 to a vector x ∈CN with deterministic phase
pattern sgn(x)T – recall that T is the set of indices corresponding to the s largest absolute
entries of x.
Since the phases are now deterministic we can no longer use the additional
concentration of measure coming from the independent randomness in the signs. In particular,
we have to estimate the probability of the event

max
ℓ∈T c
⟨˜A†
T ˜aℓ, sgn(x)T ⟩
 > 1
2

using only the randomness in ˜A. Throughout this subsection, we will assume that the sampling
matrix A ∈Cn2×N is given by (2.7). However, we note that exactly the same proof applies
if we take the Fourier system {Φk} from [25] instead and construct the random matrix as in
(2.17).
Let us state the central result of this section.
19


---

Page 20

---

Theorem 6.1. Let A ∈Cn2×N be the random sampling matrix from (2.7) and let x ∈CN. Let
T ⊂[N] with |T| = s be the index set of the s largest absolute entries of x. Set ˜A := 1
nA. If
n2 ≥Cs log2 (cN/ε) ,
(6.5)
then with probability at least 1 −ε
(i) there is a v ∈Cn2 such that u := ˜A∗v and v satisfy Conditions (3.2),(3.3) and (3.4) of
Theorem 3.1;
(ii) for the matrix ˜A, it holds that
 ˜A∗
T ˜AT −Id

2→2 ≤1
e.
(6.6)
The constants satisfy C ≤
 800e3/42, c ≤6.
Proof. Suppose we are on the event
E :=
 ˜A∗
T ˜AT −Id

2→2 ≤1
e

,
where the constant 1/e in the probability is chosen to ease computations later on. Theorem 4.1
implies that P [Ec] ≤ε/4 if Condition (6.5) holds. Our aim is an estimate for the probability
of the event
eE :=
 ˜A∗
T c ˜AT

˜A∗
T ˜AT
−1
sgn(x)T

∞
> 1
2

.
(6.7)
By expanding the Neumann series, we observe that, for m ∈N,

Id −

Id −˜A∗
T ˜AT
m−1
= Id +
∞
X
r=1

Id −˜A∗
T ˜AT
rm
.
With
Am :=
∞
X
r=1

Id −˜A∗
T ˜AT
rm
we obtain

˜A∗
T ˜AT
−1
=

Id −

Id −˜A∗
T ˜AT
−1
=

Id −

Id −˜A∗
T ˜AT
m−1 m−1
X
k=0

Id −˜A∗
T ˜AT
k
= (Id +Am)
m−1
X
k=0

Id −˜A∗
T ˜AT
k
.
An application to sgn(x)T yields
˜A∗
T c ˜AT

˜A∗
T ˜AT
−1
sgn(x)T = ˜A∗
T c ˜AT
m−1
X
k=0

Id −˜A∗
T ˜AT
k
sgn(x)T
+ ˜A∗
T c ˜AT Am
m−1
X
k=0

Id −˜A∗
T ˜AT
k
sgn(x)T .
20


---

Page 21

---

An application of the pigeon hole principle yields
P

eE

≤P
 
˜A∗
T c ˜AT
m−1
X
k=0

Id −˜A∗
T ˜AT
k
sgn(x)T

∞
> 1
4
!
(6.8)
+ P
 
˜A∗
T c ˜AT Am
m−1
X
k=0

Id −˜A∗
T ˜AT
k
sgn(x)T

∞
> 1
4
!
.
(6.9)
We now choose
m := ⌈2 log (6N/ε)⌉.
(6.10)
For the treatment of the event
E :=
(
˜A∗
T c ˜AT Am
m−1
X
k=0

Id −˜A∗
T ˜AT
k
sgn(x)T

∞
> 1
4
)
,
(6.11)
in (6.9) we denote by aℓthe columns of the unnormalized sampling matrix A and set
µ2 :=
max
ℓ∈T c,˜ℓ∈T
⟨aℓ, a˜ℓ⟩
 .
For a matrix B ∈Cm×k, we denote by
∥B∥∞→∞:=
sup
∥x∥∞=1
∥Bx∥∞= max
ℓ∈[m]
X
n∈[k]
|bℓn|
the operator norm of B on ℓ∞. We then obtain
 ˜A∗
T c ˜AT

∞→∞≤s
n2 µ2.
Moreover, for an arbitrary matrix B ∈Cs×s, it follows from the deﬁnition of ∥·∥∞→∞that
∥B∥∞→∞≤√s ∥B∥2→2. Conditionally on the event E, this inequality gives
∥Am∥∞→∞≤√s ∥Am∥2→2 ≤√s
∞
X
r=1


Id −˜A∗
T ˜AT

rm
2→2 ≤√s
∞
X
r=1
 1
em
r
= √s
1
em −1.
Similarly, we obtain

m−1
X
k=0

Id −˜A∗
T ˜AT
k

∞→∞
≤√s
e
e −1.
Combining these estimates, we obtain, conditionally on the event E,

˜A∗
T c ˜AT Am
m−1
X
k=0

Id −˜A∗
T ˜AT
k
sgn(x)T

∞→∞
≤
 ˜A∗
T c ˜AT

∞→∞∥Am∥∞→∞

m−1
X
k=0

Id −˜A∗
T ˜AT
k

∞→∞
≤s2
n2
e
(e −1)
1
em −1µ2 ≤4 s2
em
1
n2 µ2 ≤ε2
9n2 µ2,
21


---

Page 22

---

where we have applied (6.10) and the fact that s ≤N in the last line. Hence, the probability
of the event E in (6.11) can be bounded by
P
 E

= P
 E ∩E

+ P
 E ∩Ec
≤P
 ε2
9n2 µ2 > 1
4

+ ε
4
≤4s(N −s) exp

−9n
8ε2

+ ε
4 ≤ε
2,
where we have applied Hoeﬀding’s inequality Theorem 4.4 and the union bound together with
(6.5) in the last line. It remains to estimate the term in (6.8). To this end, we deﬁne, for
ℓ∈T c,
Eℓ:=
(
m−1
X
k=0
˜a∗
ℓ˜AT

Id −˜A∗
T ˜AT
k
sgn(x)T
 > 1
4
)
.
(6.12)
Let {βk}k=0,...,m−1 ⊂(0, 1) such that Pm−1
k=0 βk ≤1/4 and let Mk ∈N to be chosen below.
According to the pigeon hole principle, we have
P (Eℓ) ≤
m−1
X
k=0
P
˜a∗
ℓ˜AT

Id −˜A∗
T ˜AT
k
sgn(x)T
 ≥βk

=
m−1
X
k=0
P
 ˜a∗
ℓ˜AT

Id −˜A∗
T ˜AT
k
sgn(x)T

2Mk
≥β2Mk
k
!
≤
m−1
X
k=0
β−2Mk
k
E
"˜a∗
ℓ˜AT

Id −˜A∗
T ˜AT
k
sgn(x)T

2Mk#
,
where we have applied Markov’s inequality in the last step. With r(·) denoting the function
that rounds to the closest integer, we introduce
Mk := r

m
k + 1

for k = 0, . . . , m −1,
qk := 2Mk(k + 1).
Then 2m/3 ≤Mk(k+1) ≤4m/3 and therefore 4m/3 ≤qk ≤8m/3 and also m/Mk ≥3(k+1)/4.
For some β ∈(0, 1), we further set
βk := β
m
Mk .
Then with β = 1/(54/3), we have Pm−1
k=0 βk ≤1/4, so that we have found valid choices for the
βk. The rest of the proof is a straightforward consequence of the following statement.
Lemma 6.2. Let k, M ∈N be given and set q = 2M(k + 1). If
n ≥3q√s,
(6.13)
then
E
"˜a∗
ℓ˜AT

Id −˜A∗
T ˜AT
k
sgn(x)T

2M#
≤6q
6q√s
n
q
.
(6.14)
22


---

Page 23

---

Before we prove Lemma 6.2, let us ﬁrst see how one can deduce Theorem 6.1 from it.
Condition (6.5) implies
n ≥800e3/4√s log
6N
ε

,
which, according to the choice m = ⌈2 log (6N/ε)⌉of m and the deﬁnition of q implies (6.13).
Then (6.14) yields the series of inequalities
m−1
X
k=0
β−2Mk
k
E
"˜a∗
ℓ˜AT

Id −˜A∗
T ˜AT
k
sgn(x)T

2Mk#
≤β−2m
m−1
X
k=0
6qk
6qk
√s
n
qk
≤β−2m
m−1
X
k=0
16m
16m√s
n
 4
3 m
≤16m2
 
16β−3/2m√s
n
! 4
3 m
.
With Eℓdenoting the events from (6.12), we further obtain, using (6.5) once more,
X
ℓ/∈T
P [Eℓ] ≤16(N −s)m2
 
16β−3/2m√s
n
! 4
3 m
≤16(N −s)m2e−m ≤ε
2.
This ﬁnishes the proof of Theorem 6.1.
What remains is the following
Proof of Lemma 6.2. So far, we have not used that the bounded orthonormal system underlying
the random scattering matrix has the speciﬁc structure deﬁned in (2.7). In what follows, we
will use the letter ℓ∈Z2, possibly indexed further, to denote the rescaled positions (without
the distance coordinate) on the resolution grid where the targets can be. We furthermore
identify [N] with [
√
N]2 in the canonical way, thereby recovering the square grid of resolution
cells (recall that we set N := ⌊2L/d0⌋2, where L > 0 is the size of the target domain and d0 > 0
denotes the meshsize of the resolution grid, so that
√
N is actually the number of resolution
cells along one axis of the square array). We ﬁx ℓ∈T c and set ℓ(h)
0
:= ℓfor h = 1, . . . , 2M. A
lengthy but straightforward calculation gives with ω := 2πd0/(λz0)
˜a∗
ℓ˜AT

Id −˜A∗
T ˜AT
k
sgn(x)T

2M
=
1
n4M(k+1)
×
n
X
j(1)
1
,...,j(1)
k+1=1
...
j(2M)
1
,...,j(2M)
k+1 =1
n
X
m(1)
1 ,...,m(1)
k+1=1
...
m(2M)
1
,...,m(2M)
k+1 =1
X
ℓ(1)
1 ,...,ℓ(1)
k+1∈T
...
ℓ(2M)
1
,...,ℓ(2M)
k+1 ∈T
ℓ(p)
h ̸=ℓ(p)
h−1,h∈[k+1]
M
Y
t=1
sgn

xℓ(2t−1)
k+1

sgn

xℓ(2t)
k+1

× exp

iω
2
2M
X
p=1
(−1)p ℓ(p)
k+1

2
2

exp

iω
2M
X
p=1
(−1)p
k+1
X
h=1
D
ℓ(p)
h−1 −ℓ(p)
h

, bj(p)
h
E


× exp

iω
2M
X
p=1
(−1)p
k+1
X
h=1
D
ℓ(p)
h−1 −ℓ(p)
h

, bm(p)
h
E

.
(6.15)
23


---

Page 24

---

In order to evaluate the above term, we will use combinatorial arguments inspired by [4, 25].
To a given word

j(p)
h
p=1,...,2M
h=1,...,k+1 we associate the partition Q of [k+1]×[2M] with the property
that (h, p) and (h′, p′) are in the same block if and only if j(p)
h
= j(p′)
h′ . Analogously, we associate
the partition R to the word

m(p)
h
p=1,...,2M
h=1,...,k+1. To each Q ∈Q resp. R ∈R there exists exactly
one jQ ∈{1, . . . , n} resp. mR ∈{1, . . . , n} such that j(p)
h
= jQ for all (h, p) ∈Q resp. m(p)
h
= mR
for all (h, p) ∈R. We deﬁne
Q ∩R := {(Q, R) ∈Q × R : jQ = mR} ,
Q∩:=

Q ∈Q : there exists R = R(Q) ∈R such that mR(Q) = jQ
	
,
R∩:=

R ∈R : there exists Q = Q(R) ∈Q such that jQ(R) = mR
	
.
With this notation, we can write
E

exp

iω
2M
X
p=1
(−1)p
k+1
X
h=1
D
ℓ(p)
h−1 −ℓ(p)
h

, bj(p)
h
E


× exp

iω
2M
X
p=1
(−1)p
k+1
X
h=1
D
ℓ(p)
h−1 −ℓ(p)
h

, bm(p)
h
E




=E


Y
Q∈Q\Q∩
exp

iω
* X
(h,p)∈Q
(−1)p 
ℓ(p)
h−1 −ℓ(p)
h

, bjQ
+



×E


Y
R∈R\R∩
exp

iω
* X
(h,p)∈R
(−1)p 
ℓ(p)
h−1 −ℓ(p)
h

, bmR
+



×E

Y
Q∈Q∩
exp

iω
* X
(h,p)∈Q
(−1)p 
ℓ(p)
h−1 −ℓ(p)
h

, bjQ
+
+iω
*
X
(h,p)∈R(Q)
(−1)p 
ℓ(p)
h−1 −ℓ(p)
h

, bmR(Q)
+


.
Observe that
E


Y
Q∈Q\Q∩
exp

iω
* X
(h,p)∈Q
(−1)p 
ℓ(p)
h−1 −ℓ(p)
h

, bjQ
+



=
Y
Q∈Q\Q∩
δ

X
(h,p)∈Q
(−1)p 
ℓ(p)
h−1 −ℓ(p)
h


,
where δ is the Kronecker delta, that is δ(0) = 1 and δ(x) = 0 for x ̸= 0. Since ℓ(p)
h
̸= ℓp
h−1, this
implies that each Q ∈Q\Q∩must contain at least two elements in order to provide a nonzero
contribution to the overall expectation of the expression in (6.15). The same is true for each
R ∈R \ R∩. However, the blocks Q ∈Q∩may contain just one element, since they have a
24


---

Page 25

---

corresponding block R(Q) with matching index. Therefore, we can break the evaluation of the
right hand side of (6.15) down to three basic questions.
1. What are the numbers t1 resp. t2 of the distinct indices appearing in the words w1 :=

j(p)
h
p=1,...,2M
h=1,...,k+1 resp. w2 :=

m(p)
h
p=1,...,2M
h=1,...,k+1?
2. What is the number t of indices that the words w1 and w2 have in common?
3. Given 1. and 2., which constraints must be fulﬁlled by the partitions Q and R corre-
sponding to w1 and w2?
In the following, we identify partitions of [k + 1] × [2M] with partitions of [2M(k + 1)] in
the canonical way.
Moreover, if we have a partition Q = {Q1, . . . , Qt, Qt+1, . . . , Qt1}, we
enumerate it without loss of generality such that Qt+1, . . . , Qt1 are the blocks containing at
least two elements and Q1, . . . , Qt are the blocks which might contain just one element. The
same is done for the partition R = {R1, . . . , Rt, Rt+1, . . . , Rt2}. We deﬁne
E := E
"˜a∗
ℓ˜AT

Id −˜A∗
T ˜AT
k
sgn(x)T

2M#
.
Using the triangle inequality and n > 2M(k+1) implied by (6.13) together with the deﬁnitions
from Subsection 6.1 we obtain
E ≤
1
n4M(k+1)
2M(k+1)
X
t=0
M(k+1)+⌊t/2⌋
X
t1=t
M(k+1)+⌊t/2⌋
X
t2=t
X
j1,...,jt1 pw diﬀerent
m1,...,mt2 pw diﬀerent
|{j1,...,jt1}∩{m1,...,mt2}|=t
X
Q∈P(2M(k+1),t1,t1−t)
X
R∈P(2M(k+1),t2,t2−t)
X
ℓ(1)
1 ,...,ℓ(1)
k+1∈T
...
ℓ(2M)
1
,...,ℓ(2M)
k+1 ∈T
ℓ(p)
h ̸=ℓp
h−1,h∈[k+1]
Y
Q∈{Qt+1,...,Qt1}
δ

X
(h,p)∈Q
(−1)p 
ℓ(p)
h−1 −ℓ(p)
h



(6.16)
×
Y
R∈{Rt+1,...,Rt2}
δ

X
(h,p)∈R
(−1)p 
ℓ(p)
h−1 −ℓ(p)
h



(6.17)
×
tY
j=1
δ


X
(h,p)∈Qj
(−1)p 
ℓ(p)
h−1 −ℓ(p)
h

+
X
(h,p)∈Rj
(−1)p 
ℓ(p)
h−1 −ℓ(p)
h


.
(6.18)
For the product Q
Q∈{Qt+1,...,Qt1} δ
P
(h,p)∈Q(−1)p 
ℓ(p)
h−1 −ℓ(p)
h

to be nonzero, we must have
P
(h,p)∈Q(−1)p 
ℓ(p)
h−1 −ℓ(p)
h

= 0 for all Q ∈{Qt+1, . . . , Qt1} , and analogously for the other
two products appearing in (6.17), (6.18). Therefore, the expressions (6.16)-(6.18) give at least
25


---

Page 26

---

t1 ∨t2 := max{t1, t2} linearly independent constraints. Recalling that q = 2M(k + 1), this
observation yields
X
ℓ(1)
1 ,...,ℓ(1)
k+1∈T
...
ℓ(2M)
1
,...,ℓ(2M)
k+1 ∈T
ℓ(p)
h ̸=ℓp
h−1,h∈[k+1]
Y
Q∈{Qt+1,...,Qt1}
δ

X
(h,p)∈Q
(−1)p 
ℓ(p)
h−1 −ℓ(p)
h



×
Y
R∈{Rt+1,...,Rt2}
δ

X
(h,p)∈R
(−1)p 
ℓ(p)
h−1 −ℓ(p)
h



×
tY
j=1
δ


X
(h,p)∈Qj
(−1)p 
ℓ(p)
h−1 −ℓ(p)
h

+
X
(h,p)∈Rj
(−1)p 
ℓ(p)
h−1 −ℓ(p)
h


≤sq−t1∨t2.
Using (6.4), we arrive at
X
j1,...,jt1 pw diﬀerent
m1,...,mt2 pw diﬀerent
|{j1,...,jt1}∩{m1,...,mt2}|=t
X
Q∈P(2M(k+1),t1,t1−t)
X
R∈P(2M(k+1),t2,t2−t)
X
ℓ(1)
1 ,...,ℓ(1)
k+1∈T
...
ℓ(2M)
1
,...,ℓ(2M)
k+1 ∈T
ℓ(p)
h ̸=ℓp
h−1,h∈[k+1]
Y
Q∈{Qt+1,...,Qt1}
δ

X
(h,p)∈Q
(−1)p 
ℓ(p)
h−1 −ℓ(p)
h



×
Y
R∈{Rt+1,...,Rt2}
δ

X
(h,p)∈R
(−1)p 
ℓ(p)
h−1 −ℓ(p)
h



×
tY
j=1
δ


X
(h,p)∈Qj
(−1)p 
ℓ(p)
h−1 −ℓ(p)
h

+
X
(h,p)∈Rj
(−1)p 
ℓ(p)
h−1 −ℓ(p)
h



≤
X
j1,...,jt1 pw diﬀerent
m1,...,mt2 pw diﬀerent
|{j1,...,jt1}∩{m1,...,mt2}|=t
(9q2)q
3q
2
−t1−t2
sq−t1∨t2
≤
n
t1
t1
t
n −t1
t2 −t

(9q2)q
3q
2
−t1−t2
sq−t1∨t2
≤nt1tt
1nt2−t(9q2)q
3q
2
−t1−t2
sq−t1∨t2
≤(9q2s)q  q
n
t
 
n
3
2q
!t1+t2
s−t1∨t2,
26


---

Page 27

---

where we have applied t1 ≤q in the last step. Putting these pieces together, we obtain
E ≤
9q2s
n2
q
q
X
t=0
 q
n
t q/2+⌊t/2⌋
X
t1=t
q/2+⌊t/2⌋
X
t2=t
 
n
3
2q
!t1+t2
s−t1∨t2
=
9q2s
n2
q
q
X
t=0
 q
n
t q/2+⌊t/2⌋
X
t1=t


t1−1
X
t2=t
 
n
3
2q
!t1+t2
s−t1 +
q/2+⌊t/2⌋
X
t2=t1
 
n
3
2q
!t1+t2
s−t2

.
(6.19)
Let us evaluate the inner sums in (6.19). Since n ≥(3/2)q by (6.13) we have
q/2+⌊t/2⌋
X
t2=t1
 
n
3
2q
!t1+t2
s−t2 =
 
n
3
2q
!t1 q/2+⌊t/2⌋
X
t2=t1
 
n
3
2qs
!t2
=
 
n2
  3
2q
2 s
!t1 q/2+⌊t/2⌋−t1
X
t2=0
 
n
3
2qs
!t2
≤2
 
n2
  3
2q
2 s
!q/2+t/2
.
Similarly, using once more (6.13) in the form n ≥(3/2)q√s, we obtain
t1−1
X
t2=t
 
n
3
2q
!t1+t2
s−t1 ≤
 
n2
  3
2q
2 s
!t1
and
q/2+⌊t/2⌋
X
t1=t
 
n2
  3
2q
2 s
!t1
≤2
 
n2
  3
2q
2 s
!q/2+t/2
.
Plugging everything into (6.19) ﬁnishes the proof of the lemma.
6.3
Proof of Theorem 2.1
According to Theorem 6.1, all conditions of Theorem 3.1 are satisﬁed with probability at least
1 −ε provided
n2 ≥Cs log2 (cN/ε) ,
where C, c > 0 are numerical constants satisfying the bounds claimed in Theorem 2.1. This
concludes the proof.
7
Numerical simulations
7.1
Chambolle and Pock’s iterative primal dual algorithm
For the numerical simulations, we use Chambolle and Pock’s primal dual algorithm [9] to com-
pute the solution of (2.9) and (2.11). The algorithm is suited for a general convex optimization
problem of the form
min
x∈CN F(Ax) + G(x)
(7.1)
with A ∈Cm×N, F : Cm →(−∞, ∞] and G : CN →(−∞, ∞] lower semi-continuous convex
functions. The dual problem to (7.1) is given by
max
ξ∈Cm −F ∗(ξ) −G∗(−A∗ξ),
(7.2)
27


---

Page 28

---

where F ∗, G∗denote the convex conjugates of F, G. Here, we recall that the convex conjugate
function F ∗: Cm →(−∞, ∞] is deﬁned as
F ∗(y) := sup
x∈Cm {Re (⟨x, y⟩) −F(x)} .
In the cases of interest to us, strong duality holds, meaning that the optimal values of (7.1)
and (7.2) coincide. For describing Chambolle and Pock’s algorithm, we require the proximal
mappings of F and G deﬁned as
PG(τ; z) := argmin
x∈CN

τG(x) + 1
2 ∥x −z∥2
2

,
and analogously for F. The iterative primal dual algorithm then reads as follows. We select
parameters θ ∈[0, 1], τ, σ > 0 such that τσ∥A∥2→2 < 1 and initial vectors x0 ∈CN, ξ0 ∈Cm,
¯x0 = x0. Then one iteratively computes
ξn+1 := PF ∗(σ; ξn + σA¯xn) ,
xn+1 := PG(τ; xn −τA∗ξn+1) ,
¯xn+1 := xn+1 + θ(xn+1 −xn) .
In [9], it is shown that for the parameter choice θ = 1 the algorithm converges in the sense that
xn converges to the minimizer of the primal problem (7.1) and ξn converges to the solution of
the dual problem (7.2) as n tends to ∞. Moreover, [9] also gives an estimate of the convergence
rate for a partial primal dual gap.
7.2
The algorithm for ℓ1-minimization
Let us now specialize to the case of ℓ1-minimization. We remark that to the best of our knowl-
edge, Chambolle and Pock’s algorithm has not yet been specialized to equality-constrained
and noise-constrained ℓ1-minimization before, so we provide the ﬁrst numerical tests of the
algorithm in this setup.
Let us ﬁrst consider the problem
min
x∈CN ∥x∥1 subject to Ax = y.
This is a special case of (7.1) with G(x) = ∥x∥1 and F(z) = 0 if z = y and ∞otherwise.
Straightforward computations show that for all ξ ∈Cm, ζ ∈CN,
F ∗(ξ) = Re(⟨ξ, y⟩),
G∗(ζ) = χB∥·∥∞(ζ) =
 0
if ∥ζ∥∞≤1,
∞
otherwise ,
PF (σ; ξ) = y,
PF ∗(σ; ξ) = ξ −σy.
The proximal mapping of G(x) = ∥x∥1 can be evaluated coordinatewise, so that it is enough to
compute the proximal of the modulus function |·| on C. The latter is given by the well-known
soft-thresholding operator Sτ deﬁned as
Sτ(z) := P|·|(τ, z) = argmin
x∈C
1
2|x −z|2 + τ|x|

=
 sgn(z)(|z| −τ)
if |z| ≥τ ,
0
otherwise ,
28


---

Page 29

---

so that
PG(τ, z)ℓ= Sτ(zℓ),
ℓ∈[N] .
(7.3)
With these computations at hand, the algorithm for noise-free ℓ1-minimization is given by the
iterations
ξn+1 = ξn + σ(A¯xn −y) ,
xn+1 = Sτ(xn −τA∗ξn+1) ,
¯xn+1 = xn+1 + θ(xn+1 −xn) .
In the noisy case, we aim at solving
min
x∈CN ∥x∥1 subject to ∥Ax −y∥2 ≤η.
In this setup, G(x) = ∥x∥1 and
F(z) = χB(y,η)(z) =
 0
if ∥z −y∥2 ≤η ,
∞
otherwise .
Carrying out analogous computations as in the noise-free case, we ﬁnd that the corresponding
algorithm for the noisy case consists in iteratively computing
ξn+1 =
( 0
if ∥σ−1ξn + A¯xn −y∥2 ≤η ,
 1 −
ησ
∥ξn + σ(A¯xn −y)∥2

(ξn + σ(A¯xn −y))
otherwise ,
xn+1 = Sτ(xn −τA∗ξn+1) ,
¯xn+1 = xn+1 + θ(xn+1 −xn) .
7.3
Numerical results
We apply the above algorithm for ℓ1-minimization to the sensing matrices given by (2.7). We
choose the wavelength λ = 0.03 m, the resolution d0 = 10 m, the distance z0 = 10000 m and
the size of the aperture B = 30 m. Note that in this scenario, we have d0B/(λz0) = 1. To
speed up the algorithm, we exploit the fact that the matrix A ∈Cn2×N from (2.7) can be
factorized into a product of diagonal matrices and a nonequispaced Fourier matrix. In fact,
assuming a square resolution grid, we can write the grid parameter as double index (ℓ, ˜ℓ) with
ℓ, eℓ∈[N1] where N2
1 = N. For j, k ∈[n] and aj = (ξj, ηj), ak = (ξk, ηk) we then have
(Az)jk = exp
 πi
λz0

∥(ξj, ηj)∥2
2 + ∥(ξk, ηk)∥2
2

X
ℓ,˜ℓ∈[N1]
exp

−2πi

(ℓ, ˜ℓ),
ξj + ξk
B
, ηj + ηk
B

exp
2πid0
λz0

ℓ2 + ˜ℓ2
˜z(ℓ,˜ℓ).
Since the nonequispaced Fourier transform can be implemented at computational costs that
are only slightly larger than that of the Fast Fourier Transform, it gives rise to fast approximate
29


---

Page 30

---

matrix-vector multiplication algorithms, see [24] and reference therein. We use an implemen-
tation of S. Kunis, which can be found in the Matlab toolbox associated to the paper [20]. The
algorithm is run with the renormalized matrix ˜A =
1
√
N A and the parameter choices θ = 1,
σ = 1 and τ = 0.5. For ﬁxed sparsity s, we generate a random vector in the following way:
We choose the support set uniformly at random, then we sample a Steinhaus vector on this
support and multiply its nonzero entries independently by a dynamic range coeﬃcient uni-
formly distributed on [1, 10]. With a ﬁxed number of resolution cells, we vary the number n of
antennas and compute empirical recovery rates by choosing the n antenna positions uniformly
at random from the domain [−B/2, B/2]2, where we leave the vector to be recovered ﬁxed for
the whole period.
0
10
20
30
40
50
60
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
number of antennas
probability of recovery
sparsity = 100
# resolution cells = 6400
# trials = 100
(a)
0
10
20
30
40
50
60
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
number of samples
probability of recovery
sparsity = 100
# resolution cells = 16900
# trials = 100
(b)
Fig. 3
Empirical recovery rates for ﬁxed sparsity s = 100 and varying number n of antennas:
(a) N = 6400 resolution cells (b) N = 16900 resolution cells
With the resulting noise-free measurement vector y we compute the ℓ1-minimizer with
Chambolle and Pock’s algorithm (which takes about 300 iterations), and we record whether the
30


---

Page 31

---

original vector is recovered (up to numerical errors of at most 10−3 measured in the ℓ2-norm).
Repeating this test 100 times for each choice of parameters (s, n, N) provides an empirical
estimate of the success probability. In Figure 3, we display the result of noiseless recovery
for ﬁxed sparsity s = 100 and for N = 6400 respectively N = 16900 resolution cells. The
transition from the unsuccessful regime to the successful regime occurs at about 28 antennas,
corresponding to 784 measurements, for N = 6400, so in practice, the algorithm works even
better than predicted by our theoretical results. In the situation with more resolution cells,
the transition occurs at a slightly increased number of antennas. The illustration in Figure 3
was produced with the version of the algorithm for equality constrained ℓ1-minimization.
To test the robustness of our recovery scheme with respect to noise, we compute receiver oper-
ating characteristic curves for various parameter choices, see [28, Chapter 6] and [23, Chapter
II.D], using the noise-constrained version of Chambolle and Pock’s algorithm algorithm. We
start by simulating a target vector x ∈C6400 with ∥x∥0 = 100, that is we simulate 100 targets
in 6400 resolution cells. We do this as described above, that is we select the support uniformly
at random, then simulate random phases on the support and multiply them independently by
a dynamic range coeﬃcient uniformly distributed on [1, 10]. We then leave the vector x ﬁxed,
draw a realization of our random scattering matrix A and run noise constrained basis pursuit
with the noisy measurements y = Ax + e, where e is a complex Gaussian noise vector. The
entries of the recovered solution ˆx are then compared to a threshold τ > 0. If |ˆxk| < τ, then it
is set to zero, otherwise it remains unchanged. We then count how many of the actual targets
in x are detected. The detection probability is the number of detections divided by the true
number of targets, in our case 100. Moreover, we count the number of false alarms, that is the
number of positions k ∈[6400] where ˆxk ̸= 0 but xk = 0. The false alarm probability is the
number of false alarms divided by the number of scatterers. For ﬁxed x and τ, we repeat this
a 100 times and compute the empirical probability of detection Pd and the probability of false
alarm Pf. This is then again repeated for varying values of the threshold τ, resulting in a plot
of Pd versus Pf, which is called the receiver operating characteristic curve.
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.82
0.84
0.86
0.88
0.9
0.92
0.94
0.96
0.98
1
probability of false alarm Pf
 
probability of detection Pd
 
 
Pd versus Pf for an SNR of
15dB and 28 antennas
Pd versus Pf for an SNR of
13dB and 35 antennas
Pd versus Pf for an SNR of
13dB and 31 antennas
Fig. 4
ROC-curves for a ﬁxed 100-sparse vector x in 6400 resolution cells
In Figure 4, the results of the simulation are depicted. We see that if we choose the number
of antennas at the critical value 28 observed in Figure 3, then we get a signiﬁcant number of
missed targets and false alarms. If we however slightly increase the number of antennas, we
31


---

Page 32

---

get almost perfect detection and virtually no false alarms if we choose the threshold correctly,
in our case as τ ≈0.5. So our recovery scheme is in fact very robust with respect to noise in
the sense that the support is very well recovered. However, the quality of the approximation
of the true reﬂectivities decreases with the SNR, as is to be expected.
References
[1] L. Borcea, G. Papanicolaou, and C. Tsogka. Theory and applications of time reversal and
interferometric imaging. Inverse Problems, 19:5139–5164, 2003.
[2] M. Born and E. Wolf. Principles of Optics. Cambridge University Press, Cambridge, 7th
edition, 1999.
[3] S. Boyd and L. Vandenberghe. Convex Optimization. Cambridge Univ. Press, 2004.
[4] E. J. Cand`es, T. Tao, and J. K. Romberg. Robust uncertainty principles: exact signal re-
construction from highly incomplete frequency information. IEEE Trans. Inform. Theory,
52(2):489–509, 2006.
[5] E. J. Cand`es and Y. Plan. A probabilistic and RIPless theory of compressed sensing.
IEEE Trans. Inform. Theory, 57(11):7235 – 7254, 2011.
[6] E. J. Cand`es, J. K. Romberg, and T. Tao. Stable signal recovery from incomplete and
inaccurate measurements. Comm. Pure Appl. Math., 59(8):1207–1223, 2006.
[7] E. J. Cand`es and T. Tao. Near optimal signal recovery from random projections: universal
encoding strategies? IEEE Trans. Inform. Theory, 52(12):5406–5425, 2006.
[8] E. J. Cand`es and T. Tao. The power of convex relaxation: near-optimal matrix completion.
IEEE Trans. Inform. Theory, 56(5):2053–2080, 2010.
[9] A. Chambolle and T. Pock. A ﬁrst-order primal-dual algorithm for convex problems with
applications to imaging. J. Math. Imaging Vision, 40:120–145, 2011.
[10] S. S. Chen, D. L. Donoho, and M. A. Saunders. Atomic decomposition by basis pursuit.
SIAM J. Sci. Comput., 20(1):33–61, 1998.
[11] S. Chr´etien and S. Darses. Invertibility of random submatrices via tail decoupling and a
matrix Chernoﬀinequality. Statistics and Probability Letters, 82:1479–1487, 2012.
[12] V. de la Pe˜na and E. Gin´e. Decoupling: From Dependence to Independence. Springer,
1999.
[13] D. L. Donoho. Compressed sensing. IEEE Trans. Inform. Theory, 52(4):1289–1306, 2006.
[14] A. Fannjiang, P. Yan, and T. Strohmer. Compressed remote sensing of sparse objects.
SIAM J. Imag. Sci., 3:595–618, 2010.
[15] M. Fornasier and H. Rauhut. Compressive sensing. In O. Scherzer, editor, Handbook of
Mathematical Methods in Imaging, pages 187–228. Springer, 2011.
32


---

Page 33

---

[16] S. Foucart, A. Pajor, H. Rauhut, and T. Ullrich.
The Gelfand widths of ℓp-balls for
0 < p ≤1. J. Complexity, 26(6):629–640, 2010.
[17] J. J. Fuchs. On sparse representations in arbitrary redundant bases. IEEE Trans. Inform.
Theory, 50(6):1341–1344, 2004.
[18] F. Gruber, E. Marengo, and A. Devaney. Time-reversal-based imaging and inverse scat-
tering of multiply scattering point targets. J. Acoust. Soc. Am., 118:3129–3138, 2005.
[19] Y. Jin, J. Moura, and N. O’Donoughue. Time reversal transmission in MIMO radar. In 41.
Asilomar Conference on Signals, Systems and Computers, pages 2204 – 2208, Asilomar,
2007.
[20] S. Kunis and H. Rauhut.
Random sampling of sparse trigonometric polynomials II -
orthogonal matching pursuit versus basis pursuit. Found. Comput. Math., 8(6):737–763,
2008.
[21] B. K. Natarajan. Sparse approximate solutions to linear systems. SIAM J. Comput.,
24:227–234, 1995.
[22] J. Nelson and V. Temlyakov. On the size of incoherent systems. J. Approx. Theory,
163(9):1238–1245, 2011.
[23] H. V. Poor. An Introduction to Signal Detection and Estimation. Springer, 1994.
[24] D. Potts, G. Steidl, and M. Tasche. Fast Fourier transforms for nonequispaced data: A
tutorial. In J. Benedetto and P. Ferreira, editors, Modern Sampling Theory: Mathematics
and Applications, chapter 12, pages 247 – 270. Birkh¨auser, 2001.
[25] H. Rauhut. Random sampling of sparse trigonometric polynomials. Appl. Comput. Har-
mon. Anal., 22(1):16–42, 2007.
[26] H. Rauhut. Compressive sensing and structured random matrices. In M. Fornasier, editor,
Theoretical Foundations and Numerical Methods for Sparse Recovery, volume 9 of Radon
Series Comp. Appl. Math., pages 1–92. deGruyter, 2010.
[27] H. Rauhut and G. E. Pfander. Sparsity in time-frequency representations. J. Fourier
Anal. Appl., 16(2):233–260, 2010.
[28] M. Richards. Fundamentals of Radar Signal Processing. McGraw-Hill, 2005.
[29] M. Rudelson and R. Vershynin. On sparse reconstruction from Fourier and Gaussian
measurements. Comm. Pure Appl. Math., 61:1025–1045, 2008.
[30] A. Tolstoy. Matched Field Processing in Underwater Acoustics. World Scientiﬁc, Singa-
pore, 1993.
[31] J. A. Tropp. User-friendly tail bounds for sums of random matrices. Found. Comput.
Math., 12(4):389–434, 2012.
[32] J. A. Tropp. Recovery of short, complex linear combinations via l1 minimization. IEEE
Trans. Inform. Theory, 51(4):1568–1570, 2005.
33
