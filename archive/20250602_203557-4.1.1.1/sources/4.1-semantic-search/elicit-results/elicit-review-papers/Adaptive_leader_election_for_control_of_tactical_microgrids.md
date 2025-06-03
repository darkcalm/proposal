

---

Page 1

---

SEER: Performance-Aware Leader Election in Single-Leader Consensus
Ermin Sakic
Chair of Communication Networks
Technical University of Munich
Munich, Germany
ermin.sakic@tum.de
Petra Vizarreta
Chair of Communication Networks
Technical University of Munich
Munich, Germany
petra.vizarreta@tum.de
Wolfgang Kellerer
Chair of Communication Networks
Technical University of Munich
Munich, Germany
wolfgang.kellerer@tum.de
Abstract—Modern stateful web services and distributed SDN
controllers rely on log replication to omit data loss in case of
fail-stop failures. In single-leader execution, the leader replica
is responsible for ordering log updates and the initiation of
distributed commits, in order to guarantee log consistency. Net-
work congestions, resource-heavy computation, and imbalanced
resource allocations may, however, result in inappropriate leader
selection and increased cluster response times.
We present SEER, a logically centralized approach to per-
formance prediction and efﬁcient leader election in leader-based
consensus systems. SEER autonomously identiﬁes the replica that
minimizes the average cluster response time, using prediction
models trained dynamically at runtime. To balance the explo-
ration and exploitation, SEER explores replicas’ performance and
updates their prediction models only after detecting signiﬁcant
system changes. We evaluate SEER in a trafﬁc management
scenario comprising [3..7] Raft replicas, and well-known data-
center and WAN topologies. Compared to the Raft’s uniform
leader election, SEER decreases the mean control plane response
time by up to ∼32%. The beneﬁt comes at the expense of
the minimal adaptation of Raft election procedure and a slight
increase in leader reconﬁguration frequency, the latter being
tunable with a guaranteed upper bound. No safety properties
of Raft are invalidated by SEER.
Index Terms—Raft, SDN, distributed leader election, dis-
tributed control plane
I. INTRODUCTION
Critical services are often replicated and coupled into log-
ical clusters, in order to tolerate fail-stop and/or Byzantine
faults. Consensus protocols, such as leader-based Raft [14],
[29], (Fast) Paxos [16], all-leader Mencius [23] and Clock-
RSM [7], ensure sequencing of client requests in an ordered
log and its mirroring to replicas of the logical cluster. In-
coming client requests are then executed in the order of their
acceptance in the distributed log. Higher-layer applications can
hence read and modify the replicated state records without
awareness of the underlying consensus implementation.
Leader-based Raft [14], [29] is often the consensus protocol
of choice in production systems, e.g., in practical Kuber-
netes [28] / etcd [31], Docker Swarm [41] and Software
Deﬁned Networking (SDN) controller deployments, in par-
ticular in OpenDaylight and ONOS platforms [3], [24]. Raft
ensures strong consistent data replication, leader election and
state reconciliation after failures. Prior to committing a log
update, the leader in Raft serializes and proposes the update to
remaining cluster replicas. After the majority of Raft cluster
members have conﬁrmed the update, it is committed by the
leader. Raft assumes the existence of terms, where for each
term, a single leader is elected by the majority of replicas.
In its original speciﬁcation, Raft relies on uniform leader
election, where each replica is equally probable to become
the candidate and eventually propose its leadership for the
upcoming term. The uniform leader election in Raft can,
however, lead to slow or inefﬁciently placed leaders and hence
cause deceleration of the synchronization procedure and incur
response time penalties for client requests. The issue of inefﬁ-
cient leader is exacerbated in geo-separated Raft deployments
where network delays incurred by communication to the leader
can cause high response times [18], [22], [39], [45]. Similarly,
recent IEC/IEEE 802.1 activities have motivated the support
for dynamic network extensions in machine assemblies [6],
[30]. These impose the requirement of Layer2 multicast tree
establishment with response time guarantees using a reliable
network controller (i.e., a Raft-enabled distributed SDN con-
troller [3], [24]). Thus, the response time of the distributed
network control plane must be minimized to guarantee the
upper bound value for tree computation and enforcement of
500ms [30] in those scenarios.
Dynamic network incidents such as network failures or
spanning tree reconﬁgurations [34], as well as high control
plane load [11], [12] may result in leader or network overload
on the path to the leader and thus deteriorate the resulting
cluster performance. The few existing works that propse
efﬁcient leader-election either (i) focus on load balancing of
controller replicas and rely e.g., on round-based leader election
with minimal latency beneﬁts [40], (ii) consider the distributed
commit delay as a function of network latency only [8],
[22] or (iii) attempt to redesign Raft to alleviate the leader
bottleneck [2], [12], [45].
In this work, we instead make a case for model-based
predictions of the best-performing leader (further best-leader)
at runtime and thus attempt to solve the problem of inefﬁcient
leader election. To this end, we implement and evaluate a
minimal adaptation of Raft leader election procedure, allowing
for a remotely initiated candidate role assignment to arbitrary
replicas. We thus remain compatible with the remainder of
Raft protocol speciﬁcation / reference implementations.
A logically centralized SEER Elector component pe-
riodically predicts the best-leader for the upcoming Raft
term based on a dynamically trained per-replica performance
prediction model. The prediction model is trained using the
set of performance observations, related to resource utilization
arXiv:2104.01355v1  [cs.NI]  3 Apr 2021


---

Page 2

---

and observed round-trip and commit delays among replicas.
The metrics are collected from dedicated end-point agents
based on local knowledge only. Thus, we adopt a black-box
approach to metrics collection, without relying on knowledge
of detailed network parameters, in order to generalize SEER’s
applicability to support arbitrary replicated services beyond
SDN control plane. We minimize the number of reconﬁg-
urations necessary to explore and update the performance
models of non-leader Raft replicas at runtime, by means of an
unsupervised system novelty detection procedure that triggers
performance exploration.
A. Our Contribution
Succinctly, our contributions can be summarized as follows:
• We motivate the leader election problem by a practical
demonstration of the impact of resource contention, net-
work dynamics, and heterogeneous resource allocation to
nodes hosting the Raft replicas.
• We propose the usage of an online prediction model for
enforcement of the best-leader. To this end, we evaluate
three state-of-the-art regression methods and introduce
the corresponding scoring metric.
• To tackle the trade-off between exploitation of predicted
best-leader and exploration of non-leader’s performance,
we propose an unsupervised system state novelty detec-
tion method based on Local Outlier Factor (LOF) [4].
Fitting of predictor models is executed only on detection
of signiﬁcant resource / network events.
• We empirically evaluate and conﬁrm the signiﬁcant ad-
vantage of using the proposed prediction-based leader
election compared to the uniform election procedure
proposed by Raft’s speciﬁcation [14], [29], in emulated
Internet2 and Fat-Tree topologies, with varying replica
cluster sizes and system parameterizations. We addition-
ally quantify the tunable increase in observed reconﬁg-
uration frequency, and with it, the imposed increase in
cluster unavailability. Finally, we conﬁrm the advantages
and applicability of our approach in scenarios with im-
balanced and balanced client request arrivals.
The rest of the paper is organized as follows: Sec. II summa-
rizes Raft and discusses the issues related to inefﬁcient leader
selection. Sec. III presents the system model and SEER’s
design. Sec. IV discusses the evaluated parameterizations
and scenarios. Sec. V presents the empirical results. Sec. VI
discusses the related work. Sec. VII concludes the paper.
II. BACKGROUND AND MOTIVATION
Raft is a distributed consensus algorithm that provides safe
and ordered updates in a system comprised of multiple running
replicas. It tries to solve the issues of understandability of
the previous de-facto standard consensus algorithm Multi-
Paxos [20], and additionally standardizes an implementation of
leader election and post-failure replica recovery operations. In
the following, we summarize selected design aspects of Raft.
Autonomous leader election [14], [29]: The replicas in
Raft may acquire the leader, follower or candidate role. Raft
distinguishes terms, i.e., arbitrary time periods during which
a unique leader is responsible for distributing client update
requests to followers and ensuring safe commits. In the case
of a leader failure, after an expiration of an internal follower
timeout, the remaining followers automatically switch to a
candidate role. A candidate is an active replica which offers
to become the new cluster leader in the new Raft term. To
do so, it propagates its candidate status to the other available
replicas. If the cluster majority votes for the same candidate,
the elected replica becomes the leader for the new term.
Committing log updates in Raft: Fig. 1 depicts a successfully
executed log commit procedure. After receiving a command
request, the source replica propagates the command to the
current term leader. The leader proposes the according repli-
cated log update to its followers, and additionally transmits
the current log index (prev_log_idx). The followers with
an up-to-date log respond with an incremented log index
(prev_log_idx++), thus conﬁrming the appended local
log. After collecting the conﬁrmations from at least half the
active followers, the leader commits the update to its commit
log and increments its commit index (commit_idx++). The
leader then notiﬁes the followers of the commit index update,
which in return mark the update as committed and ﬁnally
increment their own commit_idx variable. Depending on
the deployed application model, following a commit update,
all replicas may execute the command and thus update their
state machine (i.e., as replicated state machine instances).
Alternatively, only a single replica or a subset of replicas
execute the related command.
For brevity, we omit the discussion of detailed structural
and behavioral models of Raft in zero- and multiple-failure
cases here, and instead refer the interested reader to [34].
Impact of sub-optimal leader election: Fig. 2 (a) demon-
strates the negative impact of network contentions on the
cluster performance - i.e., the observed per-transaction commit
delay. System-under-test is a 3-replica cluster, each executing
an instance of PySyncObj’s 1 Raft implementation. Indeed,
out-of-ordinary asymmetric network delay in the network
attachment port of the leader replica deteriorates the read/write
performance of the whole cluster. Fig. 2 (b) demonstrates a
similar impact after injecting additional CPU load in the leader
replica’s node, where 85% of available CPU cycles are used by
a contending process. Finally, Fig. 2 (c) showcases the impact
of heterogeneous resource mapping of the replicas. Limiting
the available CPU cycles to 40% of the originally available
capacity in leader replica results in longer commit delays at
each cluster replica, thus making a case for prioritizing high-
performing replicas as leaders.
III. SOLUTION DESIGN
A. Model Overview
We consider a distributed system comprising |R| Raft
replicas, collected in a single cluster and deployed for the
1PySyncObj - A Python library for building fault-tolerant distributed
systems - https://github.com/bakwc/PySyncObj


---

Page 3

---

Client
Source Replica (Follower)
Replica (Leader)
Other Replicas (Followers)
client request(cmd)
proxy request(cmd)
append log(cmd)
commit_idx++ & exec(cmd)
append entries(cmd, prev_log_idx)
append entries(cmd, prev_log_idx)
append log(cmd), prev_log_idx++
append log(cmd),
prev_log_idx++
prev_log_idx
prev_log_idx
commit_idx++ & exec(cmd)
append entries(commit_idx)
append entries(commit_idx)
commit_idx++ &
exec(cmd)
client response(cmd)
Fig. 1: Sequence diagram of a successfully executed Raft log update commit. Assuming stable leadership, committing a log entry requires a single round trip
to half of the cluster. Conﬁrmations require 1.5 round-trips on average, excluding the request transmission delays between the client and source replica.
0
200
400
600
800
1000
1200
Packet Sample Observation
0
20
40
60
80
100
Commit Delay [ms]
Metrics - Replica 1
Metrics - Replica 2
Metrics - Replica 3
0
5
10
15
20
25
30
Injected Link Delay [ms]
(a) Network Delay Injection
0
200
400
600
800
1000
1200
1400
Packet Sample Observation
0
10
20
30
40
50
Commit Delay [ms]
Metrics - Replica 1
Metrics - Replica 2
Metrics - Replica 3
0
20
40
60
80
Injected CPU Contention [%]
(b) Heavy CPU Workload Injection
0
200
400
600
800
1000
1200
Packet Sample Observation
0
50
100
150
200
250
300
Commit Delay [ms]
Metrics - Replica 1
Metrics - Replica 2
Metrics - Replica 3
0
10
20
30
40
CPU Ratio Limit [%]
(c) Heterogeneous CPU Resource Allocation
Fig. 2: Impact of sub-optimal leader election in a 3-replica cluster. Depicted are the observed commit delays for distributed commits for randomly-placed
replicas in a Fat-Tree topology with radix k = 4 and n = 3 levels [37]. Events such as: (a) network contention and delays on the path to Raft leader;
(b) CPU-heavy workloads; and (c) heterogeneous CPU resource allocation in the Raft leader; signiﬁcantly deteriorate the overall cluster performance, thus
motivating the need for adaptive best-leader election. In the depicted demonstrations, Replica 1 is the elected Raft leader (hence having the lowest observed
commit delays), as well as the target of the contention events resulting in cluster performance deterioration.
purpose of fault-tolerant operation. A conﬁguration of |R| =
2F + 1 replicas tolerates a maximum of F replica failures
prior to cluster unavailability. Replicas agree on the order of
updates and eventually commit the update requests in the per
application replicated log, thus providing for strong consis-
tency property (i.e., serializability and linearizability [43]). We
assume a non-Byzantine [8], [33], fail-stop [5] model - replicas
that fail, cease to work correctly.
Network: We assume Raft replicas connected in any-to-
any manner with reliability provided using disjoint paths
enabling for fail-over of replica-to-replica connections in case
of network link/node outages. Alternatively, on link/node fail-
ures, redundant paths are reactively conﬁgured or alternative
spanning trees are activated by e.g., re-converging (R)STP.
We assume arbitrary asymmetric delays between replicas, but
also an eventual synchrony, in order to circumvent the FLP
impossibility [9].
End-Points: We assume loosely synchronized clocks among
replicas (e.g., using NTP [25]). Due to complexity of measur-
ing unicast delay transmissions, we consider each replica to
periodically transmit ICMP Echo requests to remote replicas
and maintain the round trip time (RTT) values per replica
pair. The clients transmit their requests to the closest/arbitrary
replicas, i.e., source replicas, which in return note the time
instance of request arrival in the originating timestamp, and
forward the request to the leader of the current term for a
subsequent majority conﬁrmation. Following a conﬁrmation
of a committed request q, the source replica subtracts the
originating from current timestamp and stores the difference
as the commit delay tuple (q, dq). The replicas periodically
transmit the observed RTTs, CPU/memory utilization metrics
and the commit delay tuple to the logically centralized SEER
Elector component. We assume that each replica is capable
of discovering the SEER Elector’s IP and port number.
SEER Elector: The logically centralized election func-
tion, responsible for:
1) detection of system novelties and exploration of non-
leader replica’s performance;
2) subsequent collection of observation vectors from each
Raft replica and reﬁtting of their individual performance
prediction models;
3) periodic prediction of the best-leader; and
4) enforcement of the best-leader.
We assume reachability between SEER Elector and
each other Raft replica. In case of the failure of the SEER
Elector instance, a backup instance may take over its
management role. In our implementation, SEER instance is
implemented as a replicated process with leader election


---

Page 4

---

provided by a separate Raft session. SEER Elector is
hence bootstrapped without additional user interaction. Failure
of a SEER Elector instance results in no intermediate
unavailability of the monitored / managed Raft sessions.
Fig. 3 gives the overview of concurrent interactions between
the Metrics Collection (MC), the Leader Prediction (LP) and
System State Detection (SSD) processes of SEER Elector.
Note that LP and SSD blocks execute exclusively in SEER,
while MC has a counterpart agent in each Raft replica of the
system dedicated to exposing the reporting samples. We next
discuss the proposed blocks in more detail.
Init
Sample Replica Metrics
Predict Best-Leader
(based on PPM)
Detect System
State Novelties
(based on SSM)
Enforce Best-Leader
Train Leader’s PPM
Enforce r as Leader
Train PPM for r
Train SSM for r
New leader
selected
Collect new
metrics
Concurrently
Concurrently
∀r ∈N
with N ⊆R
Metrics Collection (MC)
Leader Prediction (LP)
System State
Detection (SSD)
each TM
each TP
each TN
Fig. 3: LP predicts the best-leader based on the latest collected samples for
each candidate and periodically elects the best-leader. SSD uses all collected
sample observations during the previous sampling period and periodically
reﬁts the per-replica prediction models (PPMs). Additionally, on detection of
system state novelties, SSD explores each candidate node for which a conﬁgu-
ration novelty was detected (positive triggers for majority of observations) and
similarly retrains the PPMs. It additionally adjusts the System State Model
(SSM) according to the newly observed system state.
B. Prediction of Best-Leader Replica
Metrics
Collection
(MC):
Each
TM
time
instants
replicas
transmit
their
current
observation
vectors
to
SEER Elector.
An
observation
vector
ori = [ocpu
ri , oram
ri
, ortt(ri, r0), . . . , ortt(ri, r|R|)]T comprises
the simple moving average (SMAs) of replica ri’s measured
resource utilization metrics (i.e., in our case, occupied CPU
/ RAM resources) and RTT values to remaining replicas in
set R \ ri := {x ∈R|x ̸= ri}. We chose SMAs in order
to reduce the noise of each report. Additionally, the current
term leader l asynchronously transmits messages ol
q = (ol, q)
to SEER Elector in bulk or whenever a new distributed
commit q is processed by l. For each successfully processed
commit q, the source replica src(q) transmits the measured
commit delay dsrc(q)
q
including its globally unique request
identiﬁer to SEER Elector.
Leader Prediction (LP): Each TP , SEER Elector feeds
the most recent observation vector or from each replica
r into its declared predictor, and a per-replica prediction
model (PPM) is used to predict the resulting commit delay
performance of replica candidate r as potential leader for the
upcoming term t. The sum of predicted commit delays for
replica r as potential leader of term t denotes its ﬁtness score
f(r, t) :
X
∀k∈R
¯yr
k
|R|.
Here, ¯yr
k denotes the predicted delay for a request initiated at
source-replica k, assuming r takes over the leadership.
SEER’s election procedure elects the leader replica Rt
min
set, for target term t that contains the set of best-leaders that
minimize the predicted score, i.e.,
Rt
min = {r|f(r, t) = min
r∈R f(r, t)}.
Term duration (i.e., the leader re-election period) is lower-
bounded by min(TP , TN), where TN represents the period of
system state novelty detection (discussed in Sec. III-D). We
note that TM and TN may be tuned to prevent too frequent /
seldom leader adaptation. We next discuss the PPM training
procedure and introduce exemplary predictors.
C. Training of Per-Replica Performance Prediction Models
After collecting commit delay reports dsrc(i)
i
. . . dsrc(z)
z
from all replicas (at least one commit report from each
replica), SEER Elector computes the means of individ-
ual resource-related features of leader’s observation vectors
ol
i . . . ol
z that match the commit request identiﬁers i..z. It
additionally extracts the RTTs ortt(l, src(i)) . . . ortt(l, src(z))
observed between leader l and source replicas at the time of
request processing. The mapping of pre-processed leader l’s
observation input vector and the commit delay vector then
constitutes a single training sample:
x =


1
|R|
Pz
q=i oCP U
l,q
1
|R|
Pz
q=i oRAM
l,q
ortt
i
(l, src(i))
...
ortt
z (l, src(z))


; y =


dsrc(i)
i
...
dsrc(z)
z

; (l, src(i) .. src(z)) ∈R,
with |x| = |R| + 2 and |y| = |R|.
In the evaluation of the generic model applicability, we train
and leverage the following exemplary predictors:
• Ordinary Least Squares (OLS): OLS identiﬁes a linear
function of the feature vector that minimizes the sum
of squared differences between the observed dependent
variable and the variable predicted by the linear function.
Loss ϵ is characterized by mean squared error (MSE) as
ϵ(y, ¯y) = 1
n
n
X
i=1
(yi −¯yi)2 = 1
n
n
X
i=1
(yi −xiβ)2,
where β denotes the regression coefﬁcients.
• Elastic Net (EN) [46]: EN extends the OLS with LASSO
(L1) [38] and ridge (L2) [10] regularization terms, to
prevent over-ﬁtting
ϵL1,L2(y, ¯y) = ϵ(y, ¯y)+λ((1−α)
m
X
j=0
β2
m +α
m
X
j=0
|βm|).


---

Page 5

---

• Artiﬁcial Neural Network (ANN): ANNs can be trained
to produce predictions by training the weights on in-
put data. Learning is performed via back-propagation
that adjusts the weights and ﬁnds an optimum which
minimizes the prediction error based on observed target
output and predicted variable. Due to their lightweight
implementation and high accuracy, in the past, ANNs
were used in core performance prediction and thread
partitioning strategies [21], [27], [35], [36].
Updates to ANN require adjusting the model weights while
updates to OLS and EN models necessitate recomputation
of regression coefﬁcients. SEER Elector trains the PPMs
dynamically at runtime: (i) current term leader’s PPM are
updated periodically each TP ; (ii) all replicas’ PPMs are
updated periodically each TN time instants whenever system
state novelties have been detected (ref. Section III-D); where
TP ≪TN. The intermediate predictions thus result in new
leader’s election and training of its PPM more frequently than
the full exploration procedure. In the following section, we
discuss the exploration in more detail.
D. Exploration of Followers’ Performance
Raft enforces the leadership of a single replica at any time.
Hence, training of the predictor’s PPM with ground truth com-
mit delay values is efﬁciently possible for the current leader
only. The remaining replicas must eventually be also elected as
leaders in order to guarantee eventual updates of their PPMs.
In case of rare explorations, followers’ PPMs may become
outdated. To provide for a good trade-off between exploration
of replicas’ performance and exploitation of the best-leader,
we propose an unsupervised system change detection process
that guarantees eventual exploration of all replicas.
Note: Indeed, additional |R|−1 parallel Raft sessions could
be executed with each replica as leader in one of the sessions,
in order to allow for parallel collection of ground-truth values
and concurrent PPM adjustment. This would, however, impose
a higher overhead of training and Raft session replications.
We explore the performance of replicas only when the
observed system state of the replica has changed relative to the
previous observation window. Changes in resources (SMAs of
CPU/RAM utilizations and RTTs) are considered the triggers
for system updates. To model the system state we proceed as
follows in the SSD block (ref. Fig. 3).
Populating the initial System State Model (SSM): To dis-
cover system state novelties, we rely on unsupervised outlier
detection using Local Outlier Factor (LOF) [4]. Following
the collection of network metrics during an ongoing term,
per-replica SSM models are generated. For each observation
sample (comprising resource and RTT metrics) submitted by a
replica, an anomaly score is computed, deﬁning the isolation
of the sample to the surrounding neighborhood (i.e., other
input samples). LOF relies on k-nearest neighbors to determine
locality of a sample, whose distance is used to estimate the
local density of the sample. By comparing the local density of
observed samples to those of its k-nearest neighbors, samples
with lower density are identiﬁed and pruned in the ﬁltering
step. After removing the outliers, we store the remaining
neighborhood samples in the replica-speciﬁc SSM model.
System State Detection (SSD): Each TN, outliers are
ﬁltered out of the next set of collected samples. The remaining
non-pruned samples are evaluated against k neighbors in the
current SSM. If sufﬁcient individual deviations are detected in
the new sample set (e.g., > 98.5% of observed samples in our
evaluation), the latest samples constitute the new neighborhood
and thus the new SSM. The new SSM hence deﬁnes the new
active system state. In case a new SSM must be generated,
that replica’s performance as leader is explored, i.e., its PPM
is retrained. To this end, SEER proceeds to elect the triggering
instance as the leader of a temporary term, and evaluates
its performance during a short metrics collection period (as
depicted in SSD block of Fig. 3).
0
20
40
60
80
100
RTT1 [ms]
20
40
60
80
100
RTT2 [ms]
Fig. 4: Visual representation of system states observed by a replica after 15
intentional delay injections in an emulated network deploying 3 Raft replicas.
For brevity, only the two RTT dimensions are depicted. Blue borders are the
frontiers of the identiﬁed neighborhood uniquely describing the current SSM.
Fig. 4 depicts the simplest 2D scatter plot of detected
neighborhoods in a 3-node replica cluster (each representing a
unique system state). The exemplary system states are deﬁned
by the observing replica’s RTT relation to the neighboring
replicas only. Blue borders depict the frontier, delimiting
the distribution of actual system state observations (RTTs).
Samples which are inliers (matching the neighborhood) are
the expected samples, while samples lying outside the borders
of current active state are considered either novelty samples
or outliers. Namely, future arriving samples, lying outside the
current active frontier, are considered novelty samples if the
majority of detected samples density does not deviate from
their k-neighbors. These samples are thus taken into account
in the deﬁnition of the subsequent SSM. The samples not
mapped to either the current system state or neighborhood of
the follow-up state are the outliers and are not depicted here.
In practice, determining the SSM requires evaluating and
comparing multi-dimensional input vectors comprising addi-
tional resource features (i.e., CPU/RAM utilization) and RTT
values to all other replicas as well. For simpler visualization,
we do not depict more than two dimensions of the state
model here. In implementation and evaluation, however, SEER
considers the multivariate observation samples in SSM neigh-
borhood deﬁnition and k-neighbor distance computation.


---

Page 6

---

E. Mitigation of Catastrophic Forgetting
The proposed approach to predictor training aims to incre-
mentally improve its predictions for the current leader’s model
after each leader election, and for all other replicas latest after
each detected novelty. Training the PPMs based on recent
observation samples alone, however, may load to catastrophic
forgetting of previously learned relations. To mitigate this, we
mix the data from earlier sessions with the current session’
samples (”rehearsal learning” [17]). Thus, old samples are
shufﬂed with the new samples so to appear independent in the
training batches. Processing all old data during training would
lead to monotonically increasing computation complexity,
hence we bound the training complexity by randomly sampling
a conﬁgurably-sized subset of old data and subsequently
evaluate the long-term improvement to predictions.
F. Upholding Raft’s Safety Guarantees
The leader of a new Raft term is elected only if it contains
the committed entries from previous terms (ref. §5.4.1 of [29]).
Voters vote for a target leader candidate only if their committed
entries are present on the target candidate. Thus, following the
election of a new leader, there exists no need to transfer any
previously committed entries to the leader.
SEER relies on Raft’s voting process to prevent an inconsis-
tent candidate from winning an election. It does not invalidate
any of the safety guarantees due to how a leader is enforced:
Best-leader candidate elected by SEER attempts collecting the
majority vote for the following term, and in the case of a failed
attempt, increments the term and indeﬁnitely retries the voting
step, until either elected or notiﬁed of cancellation by the
SEER Elector (e.g., due to another replica being elected as
the best-leader). The initial election attempts may hence fail
due to inconsistency of the best-leader log compared to that
of the leader of the previous active term. Eventually, however,
the elected best-leader commits the outstanding updates to its
log and becomes viable for election.
IV. EVALUATION METHODOLOGY
To evaluate the proposed model, we rely on and extend
PySyncObj, a Python library for building distributed fault-
tolerant replicated state machines. PySyncObj implements
the reference Raft speciﬁcation, and provides for straightfor-
ward tuning of Raft parameters (i.e., the candidate/follower
timeout, log compaction frequency etc.). To evaluate the
beneﬁt of best-leader prediction, we extend PySyncObj with
an interface for remote initiation of a replica’s leadership and
compare the prediction-based method with the Raft’s native
leader election relying on uniform timeout [14], [29].
Test Application & Clients: To evaluate the proposed
model, we implement a routing application and replicate it
across |R| = [3..7] Raft replicas. After receiving a user request
(command) comprising two randomly selected end-points,
the current Raft leader distributes the update request to the
commit log and, following a majority conﬁrmation, computes
the corresponding route using Dijkstra’s SP algorithm. For
simplicity, we assume that for each Raft replica, a single client
is hosted on the same server node. Clients correspondingly
select the closest replica as the source replica.
The incoming client request arrivals follow a negative
exponential distribution (n.e.d.) [15]. To reason about the
prediction performance for imbalanced client workloads, we
consider two distributions for the rate parameter λ: (i) a
balanced equal rate for each client / source replica with λr0 =
. . . = λr|R| = λB, ∀r0, ..., r|R| ∈R; and (ii) imbalanced
rates, where rates of individual clients correspond to uniformly
distributed multiples of the base rate λB: λri =
1
mr λB. The
imbalanced arrival rates expose the prediction performance
when availability of client reports is limited.
TABLE I: Evaluation Parameters
Param
Value
Comment
|R|
[3, 5, 7]
Raft cluster size
N/A
ANN, EN, OLS
Predictor selection
I
1 (True), 0 (False)
Imbalance in client requests
P
1 (True), 0 (False)
Intermediate predictions
H
1 (True), 0 (False)
Learning with rehearsals
TI
5s
Period - Delay / CPU workload injections
TP
2s
Period - LP block execution (ref. Fig. 3)
TN
20s
Period - SSD block execution (ref. Fig. 3)
JCP U
|R| = 3 : U(70, 90)%
|R| = 5 : U(65, 85)%
|R| = 7 : U(60, 80)%
Injected per-replica CPU contention
JD
U(5, 35)ms
Injected uplink network delay
JLIM
|R| = 3 : U(10, 50)%
|R| = 5 : U(15, 55)%
|R| = 7 : U(20, 60)%
Per-replica CPU resource bound
1
λB
[50, 70]ms
Per-client request arrival rate
mr
U(2, 5)
Rate multiplier for imbalanced requests
System state change triggers: We distinguish three types of
external triggers: (i) delay injections, i.e., uniformly distributed
asymmetric delays in the attachment port of the target Raft
replica; (ii) contending CPU-heavy workloads, executed on
the same node as the target Raft replica; and (iii) heteroge-
neous resource allocations, that limit the maximum achievable
performance of the target replica.
Intensities of delay, workload injections and resource allo-
cations are uniformly distributed as per Table I. The injections
occur periodically each TI. Each parameterization is evaluated
over a course of 30 state change injections. Each Raft replica
is deployed in a Docker container, with a physical CPU core
allocated exclusive for isolated execution (using cpuset).
To enforce heterogeneous resource allocations, we rely on
cpulimit’s upper bound allocation for the target core (i.e.,
target replica). To achieve a fair comparison of all predictors,
we randomly generate the injection traces and replay them for
different evaluated parameterizations (i.e., a unique injection
/ allocation trace per evaluated Raft cluster size).
Network: SEER was evaluated against an emulated net-
work comprising a number of interconnected Open vSwitch
v2.11.0 instances isolated in individual Docker containers. The
deployed network topologies connecting the distributed Raft
replicas are either Internet2 (34 switches) or Fat-Tree with
radix 4 and 3 levels (20 switches) [37]. To reﬂect the delays
incurred by the length of the optical links in the geographically
scattered Internet2, we assume a travel speed of light of
2·106 km
s in the optical ﬁber links. We derive the link distances


---

Page 7

---

from the publicly available geographical Internet2 data2 and
inject the corresponding propagation delays using Linux’s
tc tool. In contrast, the links of the Fat-Tree only posses
the inherit processing and queuing delays. In the Internet2,
we leverage a Raft replica placement that allows for high
robustness against replica failures according to [13], [33]. In
the case of Fat-Tree, replica / client pairs were placed on leaf-
nodes in Round-Robin order similar to [33].
PPM model computation: If a feature has a variance that is
orders of magnitude larger than others, it might dominate EN’s
objective function due to values with smaller amplitudes being
penalized more by L1 and L2 regularizers, in result making
the estimator unable to learn from all features. Hence, prior to
ﬁtting the models, we standardize the historical data’s metrics
to N(0, 1). To account for non-linear relationship between the
input features and the commit delay output, in case of EN
we extend the feature vector with polynomial and interaction
features. Thus, the transformed input vector used in training
and prediction comprises all polynomial combinations of the
features with a degree less than or equal to 2.
The ANN’s predictor uses the well-known ADAM opti-
mizer [19] on a neural network composed of 3 hidden layers
(ref. Table II). We use exponential linear unit (ELU) as
activation function of hidden units and linear output layer
(predicted commit delay values are unbounded). Mean squared
error (MSE) is used as the error minimization function.
An overview of optimal hyperparameters detected by grid-
search for both ANN and EN predictors is presented in
Table II. The optimal parameters were established by observ-
ing the minimized sum of MSEs of commit delay predictions
after 20 consecutive test runs per conﬁguration.
TABLE II: Grid Search Evaluation of Predictor Parameters
Predictor
Parameter
Value
ANN
No. hidden layers
2, 3, 4
No. hidden units
20, 50, 100
Elastic Net
Intercept
True, False
α (L1-Term Ratio)
0.1, 0.5, 0.9
SSM model computation: To detect k-nearest neigh-
bors, we rely on a neighborhood search algorithm using k-d
trees [26] and the Local Outlier Factor (LOF [4]) implemented
in scikit-learn [32]. The neighborhood size was set to
k = 20 as per general recommendation in [1].
Computing resources: We evaluate SEER on a recent 8-
core AMD CPU comprising one core dedicated to system
processes, and up to 7 cores used in isolated execution of
Docker containers hosting the Raft replicas. Up to 20 (34) Fat-
Tree (Internet2) vSwitches uniformly utilize the unused CPU
resources, but due to a low raw bandwidth utilization by SEER
and Raft synchronization, their impact on CPU resources is
negligible. SEER was fully implemented in Python. Predictors
rely on TF 2.0, Keras and scikit-learn for most operations.
2Internet2 topological data (provided by POCO project) - https://github.
com/lsinfo3/poco/tree/master/topologies
V. RESULTS
A. Impact of System Dynamics
1) Impact of Delay Injections: To depict the impact of
delay injection on the observed commit delay, we inject uni-
formly distributed symmetric delays in the range U(5, 35)ms
in randomly selected replica’s attachment ports and observe
the predictor performance depicted in Fig. 5a. Equal amount
and intensity of injections are applied both for balanced and
imbalanced request arrivals.
The advantage of SEER’s best-leader prediction and election
is observed for all evaluated cluster sizes, with EN’s second
order polynomial regression resulting in a slightly better result-
ing performance than ANN in the case of 7 replicas. For delay
injection case and |R| = 7, we observe absolute performance
advantages of 23.4%, 18.9%, 11.3% (mean commit delay) over
the Raft’s native leader selection (NAT), for EN, ANN and
OLS, respectively. Note that the depicted results are valid for
Internet2 only. Similar trend was observed for Fat-Tree but was
not included here due to space and readability constraints.
2) Impact of Resource Contentions: Fig. 5b depicts the
impact of periodic CPU resource contentions in randomized
replica instances. The use of EN predictor in leader election
results in mean commit delay decrease of 6.25%, 17.1% and
32.07% in 3, 5, and 7-replica case respectively, given the Table
I arrival parametrizations.
Indeed, the beneﬁcial performance impact of predictor-
based leader election approach is more obvious in the case of
a 7-replica cluster than for the 3-replica cluster. This is due to
fact that for our conﬁgured CPU loads, the given combination
of resource utilization and client load was insufﬁcient to
generate a large impact on the commit performance of the
3-replica cluster. On average, the 3-replica cluster generates
3 ·
1
50·10−3 = 60 req
s , while the 7-replica cluster generates
7 ·
1
65·10−3 = 107.7 req
s , under a higher average CPU load
for 3-replica cluster (ref. JCP U in Table II) which, when
coupled with the corresponding CPU contention values, im-
pacts the cluster in the 7-replica case more. While we could
synthetically optimally overload the 3-replica cluster to present
beneﬁcial results for all cases, we instead make a note here that
the beneﬁcial performance of predictor is observed only when
a signiﬁcant CPU load is coupled with sufﬁciently frequent
client request arrivals; or is combined with other imbalance
sources (e.g., network delays).
3) Impact of Heterogeneous Res. Allocations: The CPU
resource bounds injected using cpulimit are depicted in
Table I (ref. JLIM). As depicted in Fig. 5c, EN, ANN and OLS
all lead to a similar performance beneﬁt compared to native
Raft election (NAT), resulting in mean commit time decrease
of 23.9%, 15.2% and 5.4% for 7 replicas, respectively.
B. Impact of Predictor Parametrizations
1) Exploration Trade-Offs: In addition to the resource and
network dynamics; best-leader prediction and novelty detec-
tion intervals TP and TN, respectively (ref. Fig. 3) also dictate
the expected rate of leader reconﬁgurations. Re-elections can


---

Page 8

---

3 Replicas
{
5 Replicas
{
7 Replicas
{
50
100
150
200
250
Commit Delay [ms]
0.0
0.5
1.0
Probability
JD = U(5, 35), JCPU = 0, JLIM = 0, EN
JD = U(5, 35), JCPU = 0, JLIM = 0, OLS
JD = U(5, 35), JCPU = 0, JLIM = 0, ANN
JD = U(5, 35), JCPU = 0, JLIM = 0, NAT
50
100
150
200
250
Commit Delay [ms]
0.0
0.5
1.0
Probability
JD = U(5, 35), JCPU = 0, JLIM = 0, EN
JD = U(5, 35), JCPU = 0, JLIM = 0, OLS
JD = U(5, 35), JCPU = 0, JLIM = 0, ANN
JD = U(5, 35), JCPU = 0, JLIM = 0, NAT
50
100
150
200
250
Commit Delay [ms]
0.0
0.5
1.0
Probability
JD = U(5, 35), JCPU = 0, JLIM = 0, EN
JD = U(5, 35), JCPU = 0, JLIM = 0, OLS
JD = U(5, 35), JCPU = 0, JLIM = 0, ANN
JD = U(5, 35), JCPU = 0, JLIM = 0, NAT
(a) Network Delay Injections
50
100
150
200
250
Commit Delay [ms]
0.0
0.5
1.0
Probability
JD = 0, JCPU = U(70, 90), JLIM = 0, EN
JD = 0, JCPU = U(70, 90), JLIM = 0, OLS
JD = 0, JCPU = U(70, 90), JLIM = 0, ANN
JD = 0, JCPU = U(70, 90), JLIM = 0, NAT
50
100
150
200
250
Commit Delay [ms]
0.0
0.5
1.0
Probability
JD = 0, JCPU = U(65, 85), JLIM = 0, EN
JD = 0, JCPU = U(65, 85), JLIM = 0, OLS
JD = 0, JCPU = U(65, 85), JLIM = 0, ANN
JD = 0, JCPU = U(65, 85), JLIM = 0, NAT
50
100
150
200
250
Commit Delay [ms]
0.0
0.5
1.0
Probability
JD = 0, JCPU = U(60, 70), JLIM = 0, EN
JD = 0, JCPU = U(60, 70), JLIM = 0, OLS
JD = 0, JCPU = U(60, 70), JLIM = 0, ANN
JD = 0, JCPU = U(60, 70), JLIM = 0, NAT
(b) Heavy CPU Workload Injections
50
100
150
200
250
Commit Delay [ms]
0.0
0.5
1.0
Probability
JD = 0, JCPU = 0, JLIM = U(10, 50), EN
JD = 0, JCPU = 0, JLIM = U(10, 50), OLS
JD = 0, JCPU = 0, JLIM = U(10, 50), ANN
JD = 0, JCPU = 0, JLIM = U(10, 50), NAT
50
100
150
200
250
Commit Delay [ms]
0.0
0.5
1.0
Probability
JD = 0, JCPU = 0, JLIM = U(15, 55), EN
JD = 0, JCPU = 0, JLIM = U(15, 55), OLS
JD = 0, JCPU = 0, JLIM = U(15, 55), ANN
JD = 0, JCPU = 0, JLIM = U(15, 55), NAT
50
100
150
200
250
Commit Delay [ms]
0.0
0.5
1.0
Probability
JD = 0, JCPU = 0, JLIM = U(20, 60), EN
JD = 0, JCPU = 0, JLIM = U(20, 60), OLS
JD = 0, JCPU = 0, JLIM = U(20, 60), ANN
JD = 0, JCPU = 0, JLIM = U(20, 60), NAT
(c) Heterogeneous CPU Resource Allocations
Fig. 5: ECDFs of observed commit delay for different predictor parametrizations and resource utilization triggers. EN and ANN predictors proved most
efﬁcient and consistent across all evaluated scenarios. The relation between CPU and response time is non-linear [42], [44], with OLS thus unsurprisingly
performing worse than EN/ANN in scenarios (b) and (c). Interestingly however, OLS underﬁts the training data in the delay injection scenario (a) as well.
ANN, 1, 1
ANN, 1, 0
EN, 1, 1
EN, 1, 0
OLS, 1, 1
OLS, 1, 0
ANN, 0, 1
ANN, 0, 0
EN, 0, 1
EN, 0, 0
OLS, 0, 1
OLS, 0, 0
NAT, 0, 1
NAT, 0, 0
<Predictor, Interm. Predictions (P), Req. Imbalance (I)>
0
10
20
30
40
Reconfiguration 
 Frequency (Ratio)
7 Replicas (Internet2)
3 Replicas (Internet2)
Fig. 6: Impact of predictor, intermediate best-leader predictions (LP block),
and request imbalance on the leader reconﬁguration frequency, normalized
to the native Raft leader election case (NAT). Indeed, periodic best-leader
predictions (P=1) and sparser data collection (I=1) result in less total recon-
ﬁgurations. In return, intermediate predictions beneﬁt the response time (ref.
Fig. 7). Predictor choice does not signiﬁcantly impact the reconf. frequency.
be associated with brief unavailability periods of servicing user
requests. Namely, after announcing a candidate status for an
upcoming term, the Raft term is incremented in each instance
that receives the candidate request. This results in a transient
period during which the requests distributed for conﬁrmation
by the leader of the previous term can become rejected and
should be resubmitted in the next term.
Fig. 6 depicts the reconﬁguration frequency ratio, normal-
ized to the smallest number of reconﬁguration measured for
the NAT case and |R| = 3. Compared to NAT, SEER comes
with the overhead of a higher number of reconﬁgurations, the
actual number linearly scaling with the number of replicas.
This is due to a larger number of replicas that must conﬁrm
the incremented term prior to leader proposing the client
requests. We measure the average leader reconﬁguration time
in Internet2 to 100.81ms, 217ms and 226.55ms for 3, 5 and
7 replicas, respectively. The resulting reconﬁguration time in
Fat-Tree is slightly lower due to smaller propagation delays
associated with the geo-distributed replicas in Internet2.
Compared to the leader election after exploration (i.e., each
TN only), the addition of periodic intermediate predictions
each TP (P=1) results in a better observed commit perfor-
mance. This comes at expense of a higher frequency of updates
to the leader’s SSM and thus more frequent re-elections (by
factor ∼2 for TP , TN, TI parametrizations as per Table I).
In contrast to balanced client request arrival distributions
(I=0), imbalanced distributions (I=1) lead to a lower number
of leader reconﬁgurations, which may be associated with a
smaller resulting number of matching novel delay commit
reports and thus less SSM training samples, leading to less
frequent leader elections. Note: The number of re-elections for
NAT does not equal zero due to potential timeouts of leader
messages (i.e., due to leader overload [11] or network delays).
2) Impact of Frequent Predictions and Rehearsal Learning:
Fig. 7 depicts the impact of intermediate Leader Prediction
block (LP) execution on the resulting commit delay perfor-
mance. The LP block elects the best-leader based on current
performance predictions for non-follower replicas, without
pursuing performance exploration (a task assigned to SSD
block). The shown measurements aggregate all parameter com-
binations, with the uniform Raft leader election mode (NAT)
represented by gray bars. The results for ANN, EN, OLS,


---

Page 9

---

balanced and imbalanced arrivals are aggregated in individual
bars. Compared to Internet2, the reconﬁg. frequency applied
in Fat-Tree is multiplied by 2, so to allow for overloading the
Fat-Tree with remaining parameters unchanged.
Error bars represent the α = 0.95 CIs for the observed
commit delay samples. Based on the width of the CIs, we
conclude that bottlenecks in smaller clusters generally lead to
a larger expected variance of the observed commit delays. A
decrease in expected commit delay is observed for P=1 and
H=1 solutions, an average best-leader result being consistently
offered by P=1,H=1 conﬁguration. H=1 denotes enabled
rehearsal learning during PPM training, where old training
sets are uniformly sampled for training vectors. The considered
sample quantity ratio for old and new training samples is 1 : 1,
new samples being the ones collected during actual term.
We conclude that the application of intermediate prediction
leads to better immediate commit performance on average,
while the inclusion of old historic data in training becomes
beneﬁcial for observed long-term predictor performance.
Note: We have observed no scalability issues during PPM
updating, with the ANN model updates generally ﬁnishing in
≪30ms on a dedicated x64 CPU core, with ≤250 input
observation samples per model.ﬁt() call. Due to paper length
limitations we omit including the training overhead results.
0,0
1,0
0,1
1,1
NAT
0,0
1,0
0,1
1,1
NAT
0,0
1,0
0,1
1,1
NAT
0,0
1,0
0,1
1,1
NAT
0,0
1,0
0,1
1,1
NAT
0,0
1,0
0,1
1,1
NAT
<Interm. Predictions (P), Rehearsals (H)>
20
40
60
80
100
120
140
Mean Commit Delay [ms]
Internet2
Fat-Tree
NAT
3 Replicas
5 Replicas
7 Replicas
Fig. 7: Compared to using intermediate predictions or rehearsal learning
individually (P=1,H=0 or P=0,H=1), enabling both (P=1,H=1) consistently
results in the lowest response time. Performance increase is observed for both
evaluated topologies. The non-NAT bars depict the mean commit delays and
corresponding CIs for aggregated EN, OLS, and ANN predictor results.
VI. RELATED WORK
General Raft protocol optimizations: Hanmer et al. [12]
demonstrate vulnerability of Raft in a DDoS/overload sce-
nario, leading to frequent leader oscillations. They extend Raft
with a ”Pre-Vote” round where replicas with expired election
timeout ﬁrst agree on the leader’s deteriorated performance
prior to electing a new leader to minimize repeated elections.
Arora et al. [2] propose relying on quorum-based instead
of leader-based reads, so to ofﬂoad the leader under read-
heavy workloads. Kim et al. [18] propose an extension to the
Raft protocol, where a centralized admission entity approves
/ rejects per-shard leader elections with the goal of achieving
a balanced distribution of leader roles per data shard. Our
approach is compatible and orthogonal to these optimizations.
Performance optimization via prediction techniques: Li et
al. [21] propose an ANN-based prediction approach to learn
and determine thread prediction strategies for speculative
execution of multi-core programs. Shulga et al. [36] propose
an ML-based approach to select whether CPU or GPU-
based processor should be used for task execution based on
input data size. Shekhar et al. [35] propose an online server
selection process that estimates the expected execution time
of application tasks on fog and edge nodes and selects those
expected to meet the input constraints. The online exploration
issue, time-variant replica performance, and distributed nature
of resources are ignored in these publications.
Leader selection strategies: Vukolic et al. [22] propose a
latency-minimization strategy for imbalanced workloads that
reconﬁgures the leader set of the all-leader protocol Clock-
RSM [7], based on the previous workload and observed
latencies. In [8], clients optimize the selection of their leader
replicas in a BFT setting, by sending special probe messages
used to collect end-to-end response times. In contrast, we focus
on a single-leader consensus protocol, additionally consider
current resources’ utilization as input features, and contrary to
these works, pursue a data-driven approach. We are compatible
with [8] in that special probe messages may be generated by
the replicas to infer the features used in training and prediction
steps when imbalanced per-client arrival distributions are fore-
seen in the system (e.g., by committing no-op log updates).
However, we have showcased the effectiveness of SEER for
imbalanced loads and have thus omitted the synthetic sample
generation. We have also omitted a direct comparison to RTT-
only based approaches due to these ignoring the aspects of
replica’s resource utilization / availability.
VII. CONCLUSION AND OUTLOOK
We have introduced SEER, an approach to prediction-
based leader election in single-leader consensus clusters. SEER
was implemented and validated as an extension to a Raft-
based data-store in a scenario comprising a replicated routing
application, deployed in emulated geo-distributed and local
networks using varied predictors and client arrival distribu-
tions. In the face of network contentions, contending CPU
workloads, and heterogeneous resource allocations, or any
combination of the above, compared to uniform leader elec-
tion, SEER signiﬁcantly decreases the mean expected cluster
response time (by up to ∼32% for evaluated scenarios).
To our best knowledge, this is the ﬁrst regression-based
approach to leader-based election and the ﬁrst approach to
consider non-linear system metrics in the estimation of the
best-leader. Most importantly, SEER is deployable without
complex modiﬁcations to Raft consensus. In fact, it requires
minimal modiﬁcations to the leader election, in order to enable
the external enforcement of candidate roles.
This said, SEER could be improved in two aspects: (i)
We currently assume ﬁxed-periodic performance predictions,
leader re-elections, and non-leader exploration. An adaptive


---

Page 10

---

re-election window could enable additional efﬁciency and
minimize manual parametrization. (ii) We currently observe
Raft performance reports for individual, per-application Raft
sessions, and accordingly adjust the per-term leader. Future
work should exploit common Raft performance metrics across
multiple concurrent Raft sessions. Namely, conﬁrming the
general effectiveness of SEER without the per-session training
observations would possibly beneﬁt its scalability.
FINAL NOTE: SOFTWARE ARTIFACTS
Please contact the authors for: (i) the source code of the
presented approach including the PySyncObj fork; and (ii)
the evaluated data sets and measurement scripts.
REFERENCES
[1] Novelty detection with Local Outlier Factor (LOF).
https://bit.ly/
2PabXTf, 2019. [Online; accessed 7-August-2020].
[2] Vaibhav Arora et al. Leader or Majority: Why have one when you can
have both? Improving Read Scalability in Raft-like consensus protocols.
In 9th USENIX Workshop on Hot Topics in Cloud Computing (HotCloud
17), 2017.
[3] Pankaj Berde et al. ONOS: towards an open, distributed SDN OS. In
Proceedings of the third workshop on Hot topics in software deﬁned
networking. ACM, 2014.
[4] Markus M. Breunig et al.
LOF: Identifying Density-based Local
Outliers.
In Proceedings of the 2000 ACM SIGMOD International
Conference on Management of Data, SIGMOD ’00. ACM, 2000.
[5] Christian Cachin et al. Introduction to reliable and secure distributed
programming. Springer Science & Business Media, 2011.
[6] Josef Dorr. IEC/IEEE P60802 JWG TSN Industrial Proﬁle: Use Cases
Status Update 2018-05-14. IEC/IEEE, 2018.
[7] Jiaqing Du et al.
Clock-RSM: Low-latency inter-datacenter state
machine replication using loosely synchronized physical clocks.
In
2014 44th Annual IEEE/IFIP International Conference on Dependable
Systems and Networks. IEEE, 2014.
[8] Michael Eischer et al.
Latency-Aware Leader Selection for Geo-
Replicated Byzantine Fault-Tolerant Systems.
In 2018 48th Annual
IEEE/IFIP International Conference on Dependable Systems and Net-
works Workshops (DSN-W). IEEE, 2018.
[9] Michael J. Fischer et al. Impossibility of Distributed Consensus with
One Faulty Process. Journal of the ACM, 32(2), April 1985.
[10] Gene H Golub et al. Tikhonov regularization and total least squares.
SIAM Journal on Matrix Analysis and Applications, 21(1), 1999.
[11] Robert Hanmer et al. Friend or Foe: Strong Consistency vs. Overload
in High-Availability Distributed Systems and SDN.
In 2018 IEEE
International Symposium on Software Reliability Engineering Workshops
(ISSREW). IEEE, 2018.
[12] Robert Hanmer et al. Death by Babble: Security and Fault Tolerance of
Distributed Consensus in High-Availability Softwarized Networks. In
IEEE Conference on Network Softwarization (NetSoft). IEEE, 2019.
[13] David Hock et al. POCO-framework for Pareto-optimal resilient con-
troller placement in SDN-based core networks. In 2014 IEEE Network
Operations and Management Symposium (NOMS). IEEE, 2014.
[14] Heidi Howard et al. Raft reﬂoated: Do we have consensus? SIGOPS
Oper. Syst. Rev., 49(1), January 2015.
[15] Xi Huang et al.
Dynamic switch-controller association and control
devolution for SDN systems. In 2017 IEEE International Conference
on Communications (ICC). IEEE, 2017.
[16] Flavio Junqueira et al. Classic Paxos vs. Fast Paxos: Caveat Emptor.
Proceedings of USENIX Hot Topics in System Dependability (HotDep),
2007.
[17] Ronald Kemker et al.
Measuring catastrophic forgetting in neural
networks. In Thirty-second AAAI conference on artiﬁcial intelligence,
2018.
[18] Taehong Kim et al.
Load Balancing of Distributed Datastore in
OpenDaylight Controller Cluster. IEEE Transactions on Network and
Service Management, 16(1), 2019.
[19] Diederik P. Kingma et al. ADAM: A Method for Stochastic Optimiza-
tion. In arXiv cs.LG 1412.6980, 2014.
[20] Leslie Lamport.
The part-time parliament.
ACM Transactions on
Computer Systems (TOCS), 16(2), 1998.
[21] Yuxiang Li et al. Using artiﬁcial neural network for predicting thread
partitioning in speculative multithreading.
In 2015 IEEE 17th Inter-
national Conference on High Performance Computing and Communica-
tions, 2015 IEEE 7th International Symposium on Cyberspace Safety and
Security, and 2015 IEEE 12th International Conference on Embedded
Software and Systems. IEEE, 2015.
[22] Shengyun Liu et al. Leader set selection for low-latency geo-replicated
state machine. IEEE Transactions on Parallel and Distributed Systems,
28(7), 2016.
[23] Yanhua Mao et al.
Mencius: Building Efﬁcient Replicated State
Machines for WANs. In Proceedings of the 8th USENIX Conference
on Operating Systems Design and Implementation, OSDI’08. USENIX
Association, 2008.
[24] Jan Medved et al.
OpenDaylight: Towards a model-driven SDN
controller architecture. In Proceeding of IEEE International Symposium
on a World of Wireless, Mobile and Multimedia Networks 2014. IEEE,
2014.
[25] David L Mills. Internet time synchronization: the network time protocol.
IEEE Transactions on communications, 39(10), 1991.
[26] Marius Muja et al.
Scalable nearest neighbor algorithms for high
dimensional data. IEEE transactions on pattern analysis and machine
intelligence, 36(11), 2014.
[27] Daniel Nemirovsky et al. A machine learning approach for performance
prediction and scheduling on heterogeneous CPUs. In 2017 29th Inter-
national Symposium on Computer Architecture and High Performance
Computing (SBAC-PAD). IEEE, 2017.
[28] Hylson Netto et al. State machine replication in containers managed by
Kubernetes. Journal of Systems Architecture, 73, 2017.
[29] Diego Ongaro et al. In search of an understandable consensus algorithm.
In 2014 USENIX Annual Technical Conference (USENIX ATC 14), 2014.
[30] P60802 Project: TSN Proﬁle for Industrial Automation (TSN-IA). Use
Cases IEC/IEEE 60802 v1.3. IEC/IEEE, 2018.
[31] Sebastian Pedersen et al. An Analysis of Quorum-based Abstractions:
A Case Study using Gorums to Implement Raft.
In Proceedings of
the 2018 Workshop on Advanced Tools, Programming Languages, and
PLatforms for Implementing and Evaluating Algorithms for Distributed
systems. ACM, 2018.
[32] Fabian Pedregosa et al.
Scikit-learn: Machine learning in Python.
Journal of machine learning research, 12, 2011.
[33] Ermin Sakic et al. MORPH: An adaptive framework for efﬁcient and
Byzantine fault-tolerant SDN control plane. IEEE Journal on Selected
Areas in Communications, 36(10), 2018.
[34] Ermin Sakic et al.
Response Time and Availability Study of RAFT
Consensus in Distributed SDN Control Plane. IEEE Transactions on
Network and Service Management, 15(1), March 2018.
[35] S. Shekhar et al.
URMILA: A Performance and Mobility-Aware
Fog/Edge Resource Management Middleware.
In 2019 IEEE 22nd
International Symposium on Real-Time Distributed Computing (ISORC),
2019.
[36] D. A. Shulga et al.
The scheduling based on machine learning
for heterogeneous CPU/GPU systems.
In 2016 IEEE NW Russia
Young Researchers in Electrical and Electronic Engineering Conference
(EIConRusNW), 2016.
[37] Ankit Singla.
Fat-free topologies.
In Proceedings of the 15th ACM
Workshop on Hot Topics in Networks. ACM, 2016.
[38] Robert Tibshirani.
Regression shrinkage and selection via the lasso.
Journal of the Royal Statistical Society: Series B (Methodological),
58(1), 1996.
[39] Alexandru Turcu et al. Be general and don’t give up consistency in
geo-replicated transactional systems.
In International Conference on
Principles of Distributed Systems. Springer, 2014.
[40] Giuliana Santos Veronese et al.
Spin one’s wheels? Byzantine fault
tolerance with a spinning primary. In 2009 28th IEEE International
Symposium on Reliable Distributed Systems. IEEE, 2009.
[41] Deepak Vohra. Using Docker in Swarm Mode. Apress, Berkeley, CA,
2017.
[42] Zhikui Wang et al.
Utilization and slo-based control for dynamic
sizing of resource partitions. In International Workshop on Distributed
Systems: Operations and Management. Springer, 2005.
[43] Doug Woos et al. Planning for change in a formal veriﬁcation of the
raft consensus protocol.
In Proceedings of the 5th ACM SIGPLAN


---

Page 11

---

Conference on Certiﬁed Programs and Proofs, CPP 2016, New York,
NY, USA, 2016. Association for Computing Machinery.
[44] Wei Xu et al.
Predictive control for dynamic resource allocation in
enterprise data centers. In 2006 IEEE/IFIP Network Operations and
Management Symposium NOMS 2006. IEEE, 2006.
[45] Zichen Xu et al. Elastic, Geo-distributed RAFT. In Proceedings of the
International Symposium on Quality of Service. ACM, 2019.
[46] Hui Zou et al. Regularization and variable selection via the Elastic Net.
Journal of the royal statistical society: series B (statistical methodology),
67(2), 2005.
