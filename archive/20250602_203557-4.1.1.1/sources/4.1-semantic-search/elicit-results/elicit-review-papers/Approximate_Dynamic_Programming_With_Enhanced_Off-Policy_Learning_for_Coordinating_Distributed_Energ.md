

---

Page 1

---

Decoupling GPU Programming Models from Resource Management for
Enhanced Programming Ease, Portability, and Performance
Nandita Vijaykumar1
Kevin Hsieh1
Gennady Pekhimenko2,3,1
Samira Khan4
Ashish Shrestha5,1
Saugata Ghose1
Adwait Jog6
Phillip B. Gibbons1
Onur Mutlu7,1
1Carnegie Mellon University
2University of Toronto
3Microsoft Research
4University of Virginia
5Intel
6College of William and Mary
7ETH Zürich
This paper summarizes the idea of Zorua, which was pub-
lished in MICRO 2016 [88], and examines the work’s signiﬁ-
cance and future potential. The application resource speciﬁca-
tion—a static speciﬁcation of several parameters such as the
number of threads and the scratchpad memory usage per thread
block—forms a critical component of modern GPU program-
ming models. This speciﬁcation determines the parallelism, and
hence performance, of the application during execution because
the corresponding on-chip hardware resources are allocated
and managed based on this speciﬁcation. This tight-coupling
between the software-provided resource speciﬁcation and re-
source management in hardware leads to signiﬁcant challenges
in programming ease, portability, and performance. Zorua
is a new resource virtualization framework, that decouples
the programmer-speciﬁed resource usage of a GPU application
from the actual allocation in the on-chip hardware resources.
Zorua enables this decoupling by virtualizing each resource
transparently to the programmer.
The virtualization provided by Zorua builds on two key con-
cepts—dynamic allocation of the on-chip resources, and their
oversubscription using a swap space in memory. Zorua pro-
vides a holistic GPU resource virtualization strategy designed
to (i) adaptively control the extent of oversubscription, and
(ii) coordinate the dynamic management of multiple on-chip
resources to maximize the eﬀectiveness of virtualization. We
demonstrate that by providing the illusion of more resources
than physically available via controlled and coordinated vir-
tualization, Zorua oﬀers several important beneﬁts: (i) Pro-
gramming Ease. Zorua eases the burden on the programmer
to provide code that is tuned to eﬃciently utilize the physically
available on-chip resources. (ii) Portability. Zorua alleviates
the necessity of re-tuning an application’s resource usage when
porting the application across GPU generations. (iii) Perfor-
mance. By dynamically allocating resources and carefully
oversubscribing them when necessary, Zorua improves or re-
tains the performance of applications that are already highly
tuned to best utilize the resources. The holistic virtualization
provided by Zorua has many other potential uses, e.g., ﬁne-
grained resource sharing among multiple kernels, low-latency
preemption of GPU programs, and support for dynamic paral-
lelism.
1. Motivation: Key Challenges in
Modern GPUs
Modern Graphics Processing Units (GPUs) oﬀer high per-
formance and energy eﬃciency for many classes of appli-
cations by concurrently executing thousands of threads. In
order to execute, each thread requires several major on-chip
resources: (i) registers, (ii) scratchpad memory (if used in the
program), and (iii) a thread slot in the thread scheduler that
keeps all the bookkeeping information required for execution.
Today, these resources are statically allocated to threads
based on several parameters—the number of threads per
thread block, register usage per thread, and scratchpad usage
per block. We refer to these static application parameters
as the resource speciﬁcation of the application. This resource
speciﬁcation forms a critical component of modern GPU pro-
gramming models (e.g., CUDA [63], OpenCL [50]). The static
allocation over a ﬁxed set of hardware resources based on
the software-speciﬁed resource speciﬁcation creates a tight
coupling between the program and the physical hardware
resources. As a result of this tight coupling, for each applica-
tion, there are only a few optimized resource speciﬁcations
that maximize resource utilization. Picking a suboptimal
speciﬁcation leads to underutilization of resources and hence,
very often, performance degradation. This leads to three key
diﬃculties related to obtaining good performance on mod-
ern GPUs: programming ease, portability, and performance
degradation.
Programming Ease. First, the burden falls upon the pro-
grammer to optimize the resource speciﬁcation. For a naive
programmer, this is a challenging task because, in addition to
selecting a speciﬁcation suited to an algorithm, the program-
mer needs to be aware of the details of the GPU architecture
to ﬁt the speciﬁcation to the underlying hardware resources.
This tuning is easy to get wrong because there are many
highly suboptimal performance points in the speciﬁcation
space, and even a minor deviation from an optimized spec-
iﬁcation can lead to a drastic drop in performance due to
lost parallelism. We refer to such drops as performance cliﬀs.
Even a small change in one resource can result in a signiﬁ-
cant performance cliﬀ, degrading performance by as much
as 50%. Figure 1 depicts multiple sizable cliﬀs in an example
application, when diﬀerent resource speciﬁcations are used
arXiv:1805.02498v1  [cs.DC]  2 May 2018


---

Page 2

---

1
1.1
1.2
1.3
1.4
1.5
1.6
1.7
1.8
32
128
224
320
416
512
608
704
800
896
992
Normalized Execution Time
Threads/Block
32
38
42
48
Registers
/Thread
Cliffs at 
Different Points
Figure 1: Performance cliﬀs in Minimum Spanning Tree
(MST) when run on the NVIDIA GTX 745.
Reproduced
from [88].
when the program is run on a real modern GPU, the NVIDIA
GTX 745.1
Portability. Second, diﬀerent GPUs have varying quanti-
ties of each of the resources. Hence, an optimized speciﬁca-
tion on one GPU may be highly suboptimal on another. This
lack of portability necessitates that the programmer re-tune
the resource speciﬁcation of the application for every new
GPU generation. This problem is especially signiﬁcant in
virtualized environments, such as data centers, cloud com-
puting, or compute clusters, where the same program may
run on a wide range of GPU architectures. Figure 2 depicts
the 69% performance loss when porting optimized code from
the NVIDIA Kepler [65]/Maxwell [66] architectures to the
NVIDIA Fermi [64] architecture.
0.8
1
1.2
1.4
1.6
1.8
2
2.2
2.4
0
100
200
300
400
500
Normalized Execution Time
Threads/Block
Fermi
Kepler
Maxwell
3.16
Figure 2: Performance variation across diﬀerent GPU genera-
tions from NVIDIA (Fermi, Kepler, and Maxwell) for Discrete
Fourier Transform (DCT). Reproduced from [88].
Performance. Third, for a programmer who chooses to
employ software optimization tools (e.g., auto-tuners [21,
24, 49, 74, 75, 79]) or manually tailor the program to ﬁt the
hardware, performance is still constrained by the ﬁxed, static
resource speciﬁcation. It is well known [27,42,48,62,87,97]
that the on-chip resource requirements of a GPU application
vary throughout execution. Since the program (even after
auto-tuning) has to statically specify its worst-case resource
requirements, severe dynamic underutilization of several GPU
resources ensues [87], leading to suboptimal performance.
1Our MICRO 2016 paper [88] describes the experimental methodology for
collecting these real system results.
2. A Holistic Approach to
Resource Virtualization
To address these three challenges at the same time, we pro-
pose Zorua, a new framework that decouples an application’s
resource speciﬁcation from the available hardware resources
by virtualizing all three major resources (i.e., scratchpad mem-
ory, register ﬁle, and thread slots) in a holistic manner. This
virtualization provides the illusion of more resources to the
GPU programmer and software than physically available, and
enables the runtime system and the hardware to dynamically
manage multiple resources in a manner that is transparent to
the programmer.
2.1. Key Concepts
The virtualization strategy used by Zorua is built upon two
key concepts. First, to mitigate performance cliﬀs when we
do not have enough physical resources, we oversubscribe re-
sources by a small amount at runtime, by leveraging their dy-
namic underutilization and maintaining a swap space (in main
memory) for the extra resources required. Second, Zorua
improves utilization by determining the runtime resource re-
quirements of an application. It then allocates and deallocates
resources dynamically, managing them (i) independently of
each other to maximize each resource’s utilization; and (ii) in
a coordinated manner, to enable eﬃcient execution of each
thread with all its required resources available.
Figure 3 depicts the high-level overview of the virtual-
ization provided by Zorua. The virtual space refers to the
illusion of the quantity of available resources. The physical
space refers to the actual hardware resources (speciﬁc to the
target GPU architecture), and the swap space refers to the
resources that do not ﬁt in the physical space and hence are
spilled to other physical locations. For the register ﬁle and
scratchpad memory, the swap space is mapped to the global
memory space in the memory hierarchy. For threads, only
those that are mapped to the physical space are available for
scheduling and execution at any given time. If a thread is
mapped to the swap space, its state (e.g., the PC) is saved
in memory. Resources in the virtual space can be freely re-
mapped between the physical and swap spaces to maintain
the illusion of the virtual space resources.
Threads
Registers
Scratchpad
Virtual Space
Swap Space
Physical Space
Threads
Threads
Scheduler
Compute 
Units
Registers
Scratchpad
Registers
Scratchpad
Figure 3: High-level overview of Zorua. Reproduced from
[88].
2


---

Page 3

---

2.2. Challenges in Virtualization
Unfortunately, oversubscription means that latency-critical
resources, such as registers and scratchpad, may be swapped
to memory at the time of access, resulting in high overheads
in performance and energy. This leads to two critical chal-
lenges in designing a framework to enable virtualization. The
ﬁrst challenge is to eﬀectively determine the extent of vir-
tualization, i.e., by how much each resource appears to be
larger than its real physical amount, such that we can mini-
mize oversubscription while still reaping its beneﬁts. This is
diﬃcult as the resource requirements continually vary during
runtime. The second challenge is to minimize accesses to
the swap space. This requires coordination in the virtualized
management of multiple resources, so that enough of each
resource is available on-chip at the same time when needed.
2.3. Design Ideas
To solve these challenges, Zorua employs two key ideas.
First, we leverage the software (the compiler) to provide an-
notations with information regarding the future resource
requirements of each phase of the application. This infor-
mation enables the framework to make intelligent dynamic
decisions ahead of time, with respect to both the extent of
oversubscription and the allocation/deallocation of resources.
Second, we use an adaptive runtime system to control the
allocation of resources. This allows us to (i) dynamically alter
the extent of oversubscription; and (ii) continuously coor-
dinate the allocation of multiple on-chip resources and the
mapping between their virtual and physical/swap spaces; de-
pending on the varying runtime requirements of each thread.
We brieﬂy describe each design idea in turn.
2.3.1. Leveraging Software Annotations of Phase Char-
acteristics. We observe that the runtime variation in re-
source requirements typically occurs at the granularity of
phases of a few tens of instructions. This variation occurs
because diﬀerent parts of kernels perform diﬀerent opera-
tions that require diﬀerent resources. For example, loops that
primarily load/store data from/to scratchpad memory tend to
be less register heavy. Sections of code that perform speciﬁc
computations (e.g., matrix transformation, graph manipula-
tion), can either be register heavy or primarily operate out of
scratchpad. Often, scratchpad memory is used for only short
intervals [97], e.g., when data exchange between threads is
required, such as for a reduction operation.
Figure 4 depicts a few example phases from the N-Queens
Solver (NQU) [18] kernel. NQU is a scratchpad-heavy applica-
tion, but it does not use the scratchpad at all during the initial
computation phase. During its second phase, it performs its
primary computation out of the scratchpad, using as much
as 4224B. During its last phase, the scratchpad is used only
for reducing results, which requires only 384B. There is also
signiﬁcant variation in the maximum number of live registers
in the diﬀerent phases, as shown in Figure 4.
__global__ void solve_nqueen_cuda_kernel(…){
.phasechange 16,0;----------------------------------------------------
// initialization phase
const int tid = threadIdx.x;
const int bid = blockIdx.x;
... 
.phasechange 24,4224;-------------------------------------------------
if(idx < total_conditions) {
mask[tid][i] = total_masks[idx];
... 
}
__syncthreads();
.phasechange 12,384;--------------------------------------------------
// reduction phase
if(tid < 64 && tid + 64 < BLOCK_SIZE) 
{ sum[tid] += sum[tid + 64]; } 
...
}
Phase #1: 16 Regs, 0B Scratchpad
Phase #2: 24 Regs, 4224B Scratchpad
Phase #3: 12 Regs, 
384B Scratchpad
Figure 4: Example phases from N-Queens Solver (NQU). Re-
produced from [88].
In order to capture both the resource requirements as well
as their variation over time, we partition the program into a
number of phases. A phase is a sequence of instructions with
suﬃciently diﬀerent resource requirements than adjacent
phases.2 Barrier or fence operations also indicate a change
in requirements for a diﬀerent reason—threads that are wait-
ing at a barrier do not immediately require the thread slot
that they are holding. We interpret barriers and fences as
phase boundaries since they potentially alter the utilization
of their thread slots. The compiler inserts special instructions
called phase speciﬁers to mark the start of a new phase. Each
phase speciﬁer contains information regarding the resource
requirements of the next phase. Phase changes are shown as
“.phasechange” pragmas in Figure 4.
A phase forms the basic unit for resource allocation and
deallocation, as well as for making oversubscription decisions.
It oﬀers a ﬁner granularity than an entire thread to make
such decisions. The phase speciﬁers provide information
on the future resource usage of the thread at a phase bound-
ary. This enables (i) preemptively controlling the extent of
oversubscription at runtime, and (ii) dynamically allocating
and deallocating resources at phase boundaries to maximize
utilization of the physical resources.
2.3.2. Control with an Adaptive Runtime System. Phase
speciﬁers provide information to make oversubscription and
allocation/deallocation decisions. However, we still need a
way to make decisions on the extent of oversubscription and
appropriately allocate resources at runtime. To this end, we
use an adaptive runtime system, which we refer to as the
coordinator. Figure 5 presents an overview of the coordinator.
The virtual space enables the illusion of a larger amount
of each of the resources than what is physically available,
to adapt to diﬀerent application requirements. This illusion
enables higher thread-level parallelism than what can be
achieved with solely the ﬁxed, physically available resources,
by allowing more threads to execute concurrently. The size of
the virtual space at a given time determines this parallelism,
and those threads that are eﬀectively executed in parallel are
referred to as active threads. All active threads have thread
2We refer the reader to Section 4.6 of our MICRO 2016 paper [88] for speciﬁc
details on how phases are identiﬁed.
3


---

Page 4

---

Pending 
Threads
Active Threads
Physical/Swap Space
To Warp Scheduler 
& Compute Units
COORDINATOR
Application Threads
Schedulable 
Threads
Virtual Space
Figure 5:
Overview of the coordinator.
Reproduced
from [88].
slots allocated to them in the virtual space (and hence can
be executed), but some of them may not be mapped to the
physical space at any given time. As discussed previously,
the resource requirements of each application continuously
change during execution. To adapt to these runtime changes,
the coordinator leverages information from the phase speci-
ﬁers to make decisions on oversubscription. The coordinator
makes these decisions at every phase boundary and thereby
controls the size of the virtual space for each resource.
2.4. Zorua: An Overview
To address the challenges in virtualization by leveraging
the above ideas, Zorua employs a software-hardware code-
sign that comprises three components: (i) The compiler an-
notates the program by adding special instructions (phase
speciﬁers) to partition it into phases and to specify the re-
source needs of each phase of the application. (ii) The co-
ordinator, a hardware-based adaptive runtime system, uses
the compiler annotations to dynamically allocate/deallocate
resources for each thread at phase boundaries. The coordina-
tor plays the key role of continuously controlling the extent
of the oversubscription at each phase boundary. (iii) Hard-
ware virtualization support includes a mapping table for
each resource to locate each virtual resource in either the
physically available on-chip resources or the swap space in
main memory, and the machinery to swap resources between
the physical space and the swap space.
Zorua has two key hardware components: (i) the coordi-
nator that contains queues to buﬀer the pending threads and
control logic to make oversubscription and resource manage-
ment decisions, and (ii) resource mapping tables to map each of
the resources to their corresponding physical or swap spaces.
Our MICRO 2016 paper [88] provides the detailed implemen-
tation of Zorua in Section 4. In particular, we describe several
key issues, including how (1) Zorua determines the amount
of oversubscription for each resource (Section 4.4 of [88]),
(2) Zorua virtualizes each resource (Section 4.5 of [88]), and
(3) the compiler identiﬁes each phase (Section 4.6 of [88]).
3. Results
In this section, we evaluate the eﬀectiveness of Zorua in im-
proving programming ease, portability, and performance. Our
detailed experimental methodology is described in Section 5
of our MICRO 2016 paper [88]. More results are provided in
Section 6 of [88].
3.1. Eﬀect on Performance Variation and Cliﬀs
We ﬁrst examine how Zorua alleviates the high variation
in performance by reducing the impact of resource speciﬁca-
tions on resource utilization. Figure 6 summarizes the range
in performance across a wide range of resource speciﬁcations
(indicating an undesirable dependence on the speciﬁcation),
for the baseline architecture, WLM (which allocates resources
at the ﬁner granularity of a warp [91]), and Zorua for a rep-
resentative set of applications, using a Tukey box plot [61].
The boxes in the box plot represent the range between the
ﬁrst quartile (25%) and the third quartile (75%). The whiskers
extending from the boxes represent the maximum and mini-
mum points of the distribution, or 1.5× the length of the box,
whichever is smaller. Any points that lie more than 1.5× the
box length beyond the box are considered to be outliers [61],
and are plotted as individual points. The line in the middle
of the box represents the median, while the “X” represents
the average. We make two major observations from Figure 6.
Figure 6: Normalized performance distribution. Reproduced
from [88].
First, we ﬁnd that Zorua signiﬁcantly reduces the perfor-
mance range across all evaluated resource speciﬁcations. Av-
eraged across all of our applications, the worst resource spec-
iﬁcation for Baseline achieves 96.6% lower performance than
the best performing resource speciﬁcation. For WLM [91],
this performance range reduces only slightly, to 88.3%. With
Zorua, the performance range drops signiﬁcantly, to 48.2%.
We see drops in the performance range for all applications
except SSSP. With SSSP, the range is already small to begin
with (23.8% in Baseline), and Zorua exploits the dynamic un-
derutilization, which improves performance but also adds a
small amount of variation.
Second, while Zorua reduces the performance range, it also
preserves or improves performance of the best performing
points. As we examine in more detail in Section 3.2, the
reduction in performance range occurs as a result of improved
performance mainly at the lower end of the distribution.
To gain insight into how Zorua reduces the performance
range and improves performance for the worst performing
points, we analyze how it reduces performance cliﬀs. We
study the tradeoﬀbetween resource speciﬁcation and exe-
4


---

Page 5

---

0.5
1
1.5
2
2.5
0
200
400
600
Normalized Exec. Time
Threads/Block
Baseline
WLM
Zorua
(a) DCT
0.5
1
1.5
2
200
500
800
1100
Threads/Block
Baseline
WLM
Zorua
(b) MST
0.5
1
1.5
2
9000
29000
49000
Scratchpad/Block
Baseline
WLM
Zorua
(c) NQU
Figure 7: Eﬀect on performance cliﬀs. Reproduced from [88].
cution time for three representative applications: DCT (Fig-
ure 7a), MST (Figure 7b), and NQU (Figure 7c). For all three
ﬁgures, we normalize execution time to the best execution
time under Baseline. We make two observations from the
ﬁgures.
First, Zorua successfully mitigates the performance cliﬀs
that occur in Baseline. For example, DCT and MST are both
sensitive to the thread block size, as shown in Figures 7a
and 7b, respectively. We have circled the locations at which
cliﬀs exist in Baseline. Unlike Baseline, Zorua maintains
more steady execution times across the number of threads
per block, employing oversubscription to overcome the loss
in parallelism due to insuﬃcient on-chip resources. We see
similar results across all of our applications.
Second, we observe that while WLM [91] can reduce some
of the cliﬀs by mitigating the impact of large block sizes,
many cliﬀs still exist under WLM (e.g., NQU in Figure 7c).
This cliﬀin NQU occurs as a result of insuﬃcient scratchpad
memory, which cannot be handled by warp-level manage-
ment. Similarly, the cliﬀs for MST (Figure 7b) also persist with
WLM because MST has a lot of barrier operations, and the
additional warps scheduled by WLM ultimately stall, waiting
for other warps within the same block to acquire resources.
We ﬁnd that, with oversubscription, Zorua is able to smooth
out those cliﬀs that WLM is unable to eliminate.
3.2. Eﬀect on Performance
As Figure 6 shows, Zorua either retains or improves the
best performing point for each application, compared to the
Baseline. Zorua improves the best performing point for each
application by 12.8% on average, and by as much as 27.8%
(for DCT). This improvement comes from the improved par-
allelism obtained by exploiting the dynamic underutilization
of resources, which exists even for optimized speciﬁcations.
Applications such as SP and SLA have little dynamic under-
utilization, and hence do not show any performance improve-
ment. NQU does have signiﬁcant dynamic underutilization,
but Zorua does not signiﬁcantly improve the best performing
point as the overhead of oversubscription outweighs the ben-
eﬁt, and Zorua dynamically chooses not to oversubscribe. We
conclude that even for many speciﬁcations that are optimized
to ﬁt the underlying hardware resources, Zorua is able to
further improve performance.
We also note that, in addition to reducing performance vari-
ation and improving performance for optimized points, Zorua
improves performance by 25.2% on average for all resource
speciﬁcations across all evaluated applications.
3.3. Eﬀect on Portability
Performance cliﬀs often behave diﬀerently across diﬀerent
GPU architectures, and can signiﬁcantly shift the best per-
forming resource speciﬁcation point. We study how Zorua
can ease the burden of performance tuning if an applica-
tion has been already tuned for one GPU model, and is later
ported to another GPU. To understand this, we deﬁne a new
metric, porting performance loss, that quantiﬁes the perfor-
mance impact of porting an application without re-tuning
it. To calculate this, we ﬁrst normalize the execution time
of each speciﬁcation point to the execution time of the best
performing speciﬁcation point. We then pick a source GPU
architecture (i.e., the architecture that the GPU was tuned for)
and a target GPU architecture (i.e., the architecture that the
code will run on), and ﬁnd the point-to-point drop in perfor-
mance (when the code is executed on the target GPU) for all
points whose performance on the source GPU comes within
5% of the performance at the best performing speciﬁcation
point.3
Figure 8 shows the maximum porting performance loss
for each application, across any two pairings of our three
simulated GPU architectures (NVIDIA Fermi, Kepler, and
Maxwell). We ﬁnd that Zorua greatly reduces the maximum
porting performance loss that occurs under both Baseline
and WLM for all but one of our applications. On average,
the maximum porting performance loss is 52.7% for Baseline,
51.0% for WLM, and only 23.9% for Zorua.
Notably, Zorua delivers signiﬁcant improvements in porta-
bility for applications that previously suﬀered greatly when
ported to another GPU, such as DCT and MST. For both of
these applications, the performance variation diﬀers so much
3We include any point within 5% of the best performance as there are often
multiple points close to the best point, and the programmer may choose
any of them.
5


---

Page 6

---

0%
50%
100%
150%
BH
DCT
MST
NQU
RD
SLA
SP
SSSP
AVG
Maximum Porting 
Performance Loss 
Baseline
WLM
Zorua
Figure 8: Maximum porting performance loss. Reproduced
from [88].
between GPU architectures that, despite tuning the applica-
tion on the source GPU to be within 5% of the best achievable
performance, their performance on the target GPU is often
more than twice as slow as the best achievable performance
on the target platform. Zorua signiﬁcantly lowers this porting
performance loss down to 28.1% for DCT and 36.1% for MST.
We also observe that for BH, Zorua actually slightly increases
the porting performance loss with respect to the Baseline.
This is because for Baseline, there are only two points that
perform within the 5% margin for our metric, whereas with
Zorua, we have ﬁve points that fall in that range. Despite
this, the increase in porting performance loss for BH is low,
deviating only 7.0% from the best performance.
We conclude that Zorua enhances portability of applica-
tions by reducing the impact of a change in the hardware
resources for a given resource speciﬁcation. For applications
that have already been tuned on one platform, Zorua sig-
niﬁcantly lowers the penalty of not re-tuning for another
platform, allowing programmers to save development time.
4. Related Work
To our knowledge, our MICRO 2016 paper [88] is the ﬁrst
work to propose a holistic framework to decouple a GPU
application’s resource speciﬁcation from its physical on-chip
resource allocation by virtualizing multiple on-chip resources.
This enables the illusion of more resources than what physi-
cally exists to the programmer, while the hardware resources
are managed at runtime by employing a swap space (in main
memory), transparently to the programmer. We design a new
hardware/software cooperative framework to eﬀectively vir-
tualize multiple on-chip GPU resources in a controlled and
coordinated manner, thus enabling many beneﬁts of virtual-
ization in GPUs.
We brieﬂy discuss prior work related to diﬀerent aspects
of our proposal: (i) virtualization of resources, (ii) improving
programming ease and portability, and (iii) more eﬃcient
management of on-chip resources.
Virtualization of Resources. Virtualization [20, 22, 33,
41] is a concept designed to provide the illusion, to the soft-
ware and programmer, of more resources than what truly
exists in physical hardware. It has been applied to the man-
agement of hardware resources in many diﬀerent contexts
[5,10,20,22,33,41,67,89], with virtual memory [11,22,26,41] be-
ing one of the oldest forms of virtualization that is commonly
used in high-performance processors today. Abstraction of
hardware resources and use of a level of indirection in their
management leads to many beneﬁts, including improved uti-
lization, programmability, portability, isolation, protection,
sharing, and oversubscription.
In this work, we apply the general principle of virtual-
ization to the management of multiple on-chip resources in
modern GPUs. Virtualization of on-chip resources oﬀers the
opportunity to alleviate many diﬀerent challenges in modern
GPUs. However, in this context, eﬀectively adding a level
of indirection introduces new challenges, necessitating the
design of a new virtualization strategy. There are two key
challenges. First, we need to dynamically determine the extent
of the virtualization to reach an eﬀective tradeoﬀbetween
improved parallelism due to oversubscription and the laten-
cy/capacity overheads of swap space usage. Second, we need
to coordinate the virtualization of multiple latency-critical
on-chip resources. To our knowledge, this is the ﬁrst work to
propose a holistic software-hardware cooperative approach
to virtualizing multiple on-chip resources in a controlled and
coordinated manner that addresses these challenges, enabling
the diﬀerent beneﬁts provided by virtualization in modern
GPUs.
Prior works propose to virtualize a speciﬁc on-chip re-
source for speciﬁc beneﬁts, mostly in the CPU context. For
example, in CPUs, the concept of virtualized registers was
ﬁrst used in the IBM 360 [5] and DEC PDP-10 [10] architec-
tures to allow logical registers to be mapped to either fast
yet expensive physical registers, or slow and cheap memory.
More recent works [67,93,94], propose to virtualize registers
to increase the eﬀective register ﬁle size to much larger reg-
ister counts. This increases the number of thread contexts
that can be supported in a multi-threaded processor [67], or
reduces register spills and ﬁlls [93,94]. Other works propose
to virtualize on-chip resources in CPUs (e.g., [15,19,25,31,99]).
In GPUs, Jeon et al. [42] propose to virtualize the register
ﬁle by dynamically allocating and deallocating physical reg-
isters to enable more parallelism with smaller, more power-
eﬃcient physical register ﬁles. Concurrent to this work, Yoon
et al. [98] propose an approach to virtualize thread slots to in-
crease thread-level parallelism. These works propose speciﬁc
virtualization mechanisms for a single resource for speciﬁc
beneﬁts. None of these works provide a cohesive virtual-
ization mechanism for multiple on-chip GPU resources in
a controlled and coordinated manner, which forms a key
contribution of our MICRO 2016 work.
Enhancing Programming Ease and Portability. There
is a large body of work that aims to improve programmability
and portability of modern GPU applications using software
tools, such as auto-tuners [21, 24, 49, 74, 75, 79], optimizing
compilers [17,37,47,59,95,96], and high-level programming
languages and runtimes [23,35,72,85]. These tools tackle a
multitude of optimization challenges, and have been demon-
strated to be very eﬀective in generating high-performance
portable code. They can also be used to tune the resource
6


---

Page 7

---

speciﬁcation. However, there are several shortcomings in
these approaches. First, these tools often require proﬁling
runs [17,21,75,79,95,96] on the GPU to determine the best
performing resource speciﬁcations. These runs have to be
repeated for each new input set and GPU generation. Second,
software-based approaches still require signiﬁcant program-
mer eﬀort to write code in a manner that can be exploited
by these approaches to optimize the resource speciﬁcations.
Third, selecting the best performing resource speciﬁcations
statically using software tools is a challenging task in vir-
tualized environments (e.g., cloud computing, data centers),
where it is unclear which kernels may be run together on the
same SM or where it is not known, a priori, which GPU gener-
ation the application may execute on. Finally, software tools
assume a ﬁxed amount of available resources. This leads to
runtime underutilization due to static allocation of resources,
which cannot be addressed by these tools.
In contrast, the programmability and portability beneﬁts
provided by Zorua require no programmer eﬀort in optimiz-
ing resource speciﬁcations. Furthermore, these auto-tuners
and compilers can be used in conjunction with Zorua to fur-
ther improve performance.
Eﬃcient Resource Management. Prior works aim to
improve parallelism by increasing resource utilization using
hardware-based [6,7,30,42,45,46,55,57,62,71,84,86,91,97],
software-based [32, 36, 53, 58, 68, 92, 97], and hardware-
software cooperative [8, 9, 43, 44, 73, 81, 82, 87] approaches.
Among these works, the closest to ours are [42,98] (discussed
earlier), [97], and [91]. These approaches propose eﬃcient
techniques to dynamically manage a single resource, and
can be used along with Zorua to improve resource eﬃciency
further. Yang et al. [97] aim to maximize utilization of the
scratchpad with software techniques, and by dynamically
allocating/deallocating scratchpad memory. Xiang et al. [91]
propose to improve resource utilization by scheduling threads
at the ﬁner granularity of a warp rather than a thread block.
This approach can help alleviate performance cliﬀs, but not in
the presence of synchronization or scratchpad memory, nor
does it address the dynamic underutilization within a thread
during runtime. We quantitatively compare to this approach
in Section 3 and demonstrate Zorua’s beneﬁts over it.
Other works leverage resource underutilization to improve
energy eﬃciency [2, 27, 28, 29, 42] or perform other useful
work [54,87]. These works are complementary to Zorua.
5. Signiﬁcance and Long-Term Impact
In this section, we describe the signiﬁcance and long-term
impact of our MICRO 2016 work, Zorua, by delineating its
novelty, what it can enable in future systems, and new re-
search directions that it triggers.
5.1. Novelty
• This is the ﬁrst work that takes a holistic approach to de-
coupling a GPU application’s resource speciﬁcation from its
physical on-chip resource allocation via the use of virtual-
ization. We develop a comprehensive virtualization frame-
work that provides controlled and coordinated virtualization
of multiple on-chip resources to maximize the eﬀectiveness
of virtualization.
• Making GPUs easy to program is critical for their
widespread use, and also to achieve the high performance
promised by the massively parallel architecture. A key limit-
ing factor in GPU programming today is the burden placed on
the programmer in ﬁnding a hardware resource speciﬁcation
that achieves very high performance. This is the ﬁrst work
to ease that burden without compromising performance by
virtualizing the major hardware resources programmers are
required to manage today.
• Portability across GPU architectures is vital in environ-
ments such as cloud computing and data centers to achieve
predictably good performance, irrespective of the GPU gener-
ation the application is executing on. This is the ﬁrst work
to tackle the portability challenges that arise from the pro-
grammer’s management of the ﬁxed on-chip resources with
a holistic resource virtualization strategy.
5.2. What Zorua Can Enable in Future Systems
GPUs have emerged as the dominant massively parallel
GPU architecture, used as the platform of choice for a wide
range of parallel applications from machine learning to sci-
entiﬁc simulation. However, there are a number of key chal-
lenges that limit the adoption of GPUs across broader classes
of applications and environments, e.g., data centers, cloud
computing, etc. Programmability and portability of GPU ap-
plications are two such challenges. But future GPUs will
need to address several other challenges before truly becom-
ing ﬁrst-class compute engines. As we describe below, we
believe that our work can help address some of these other
challenges.
Multiprogramming in Virtualized Environments.
Zorua lends itself to easily addressing two key challenges
in enabling multiprogramming in virtualized environments
today:
Fine-grained resource sharing across kernels: Zorua manages
the diﬀerent resources independently and at a ﬁne granular-
ity, using a dynamic runtime system. Hence, Zorua can be
extended to support ﬁne-grained sharing and partitioning of
resources across multiple kernels to enable eﬃcient multipro-
gramming in GPUs. Zorua enables better resource utilization
in these multiprogrammed environments, while providing
the ability to control the partitioning of resources at runtime
to provide QoS, fairness, etc., by leveraging the hardware
runtime system. Zorua can work synergistically with sys-
tems such as Mosaic [8] and MASK [9], which enable eﬃcient
memory virtualization techniques for GPUs, to enable true
full-system multi-kernel execution.
7


---

Page 8

---

Preemptive multitasking: Another key challenge in en-
abling true multiprogramming in GPUs is enabling rapid
preemption of kernels [69, 83, 90]. Context switching on
GPUs incurs a very high latency and overhead, as a result of
the large amount of register ﬁle/scratchpad state that needs
to be saved before a new kernel can be executed. Zorua en-
ables ﬁne-grained management and virtualization of on-chip
resources. It can be naturally extended to enable quick pre-
emption of a task via intelligent management of the swap
space and the mapping tables. It can also work synergisti-
cally with CABA [87], framework for assist warp execution
in GPUs, to provide ﬂexible and eﬃcient support for multi-
tasking and context switching.
Support for Other Parallel Programming Paradigms.
The ﬁxed static resource allocation for each thread in modern
GPU architectures requires statically dictating the parallelism
for the program throughout its execution. Other forms of
parallel execution that are dynamic (e.g., CILK [12]) require
more ﬂexible allocation of resources at runtime, and are hence
more challenging to enable on GPUs. Examples of this include
nested parallelism [56], where a kernel can dynamically spawn
new kernels or thread blocks, and helper threads [87] to utilize
idle resource at runtime to perform diﬀerent optimizations or
background tasks in parallel. Zorua makes it easy to enable
these paradigms by providing on-demand dynamic allocation
of resources.
Energy Eﬃciency, Scalability, and Reliability. To sup-
port massive parallelism, on-chip resources are a precious
and critical resource. However, these resources cannot grow
arbitrarily large as GPUs continue to be area-limited and on-
chip memory tends to be extremely power hungry and area
intensive [2,27,28,42,73,98], which are trends we believe will
become increasingly important for the foreseeable future. Fur-
thermore, complex thread schedulers that can select a thread
for execution from an increasingly large thread pool are re-
quired. Zorua enables using smaller register ﬁles, scratchpad
memory and less complex or fewer thread schedulers to save
power and area while still retaining or improving parallelism.
The indirection oﬀered by Zorua, along with the dynamic
management of resources, could also enable better reliability.
The virtualization framework trivially allows portions of a
resource that contain hard or soft faults to be remapped to
other portions of the resource that do not contain faults, or
to spare structures, thereby increasing the error tolerance of
these resources.
5.3. New Research Directions Zorua Enables
Zorua opens up several new avenues for more research,
which we brieﬂy discuss here.
Flexible Programming Models for GPUs and Hetero-
geneous Systems. By providing a ﬂexible but dynamically
controlled view of the on-chip hardware resources, Zorua
changes the abstraction of the on-chip resources that is of-
fered to the programmer and software. This oﬀers the op-
portunity to rethink resource management in GPUs from the
ground up. One could envision more powerful resource allo-
cation and better programmability with programming mod-
els that do not require static resource speciﬁcation, leaving
the compiler/runtime system and the underlying virtualized
framework to completely handle all forms of on-chip resource
allocation, unconstrained by the ﬁxed physical resources in a
speciﬁc GPU, entirely at runtime. This is especially signiﬁ-
cant in future systems that are likely to support a wide range
of compute engines and accelerators, making it important
to be able to write high-level code that can be partitioned
easily, eﬃciently, and at a ﬁne granularity across any set of
accelerators, without statically tuning any code segment to
run eﬃciently on the GPU.
Virtualization-Aware Compilation and Auto-Tuning.
Zorua changes the contract between the hardware and soft-
ware to provide a more powerful resource abstraction (in
the software) that is ﬂexible and dynamic, by pushing some
more functionality to the hardware, which can more eas-
ily react to runtime resource requirements of the program.
We can re-imagine compilers and auto-tuners to be more
intelligent, leveraging this new abstraction and, hence the
virtualization, to deliver more eﬃcient and high-performing
code optimizations that are not possible with the ﬁxed and
static abstractions of today. They could, for example, leverage
the oversubscription and dynamic management that Zorua
provides to tune the code to more aggressively use resources.
Support for System-Level Tasks on GPUs. As GPUs
become increasingly general purpose, a key requirement is
better integration with the CPU operating system, and with
complex distributed software systems such as those employed
for large-scale distributed machine learning [1,39] or graph
processing [3,4,60]. If GPUs are architected to be ﬁrst-class
compute engines, rather than the slave devices they are today,
they can be programmed and utilized in the same manner as
a modern CPU. This integration requires the GPU execution
model to support system-level tasks like interrupts, excep-
tions, etc. and more generally provide support for access to
distributed ﬁle systems, disk I/O, or network communication.
Support for these tasks and execution models require dy-
namic provisioning of resources for execution of system-level
code. Zorua provides a building block to enable this.
Applicability to General Resource Management in
Accelerators. Zorua uses a program phase as the gran-
ularity for managing resources. This allows handling re-
sources across phases dynamically, while leveraging static
information regarding resource requirements from the soft-
ware by inserting annotations at phase boundaries.
Fu-
ture work could potentially investigate the applicability of
the same approach to manage resources and parallelism
in other accelerators (e.g., processing-in-memory accelera-
tors [3, 4, 13, 14, 34, 38, 40, 51, 52, 70, 77, 78, 80, 100] or direct-
memory access engines [16,55,76]) that require eﬃcient dy-
8


---

Page 9

---

namic management of large amounts of particular critical
resources.
6. Conclusion
We propose Zorua, a new framework that decouples the
application resource speciﬁcation from the allocation in the
physical hardware resources (i.e., registers, scratchpad mem-
ory, and thread slots) in GPUs. Zorua encompasses a holis-
tic virtualization strategy to eﬀectively virtualize multiple
latency-critical on-chip resources in a controlled and coordi-
nated manner. We demonstrate that by providing the illusion
of more resources than physically available, via dynamic man-
agement of resources and the judicious use of a swap space in
main memory, Zorua enhances (i) programming ease (by re-
ducing the performance penalty of suboptimal resource spec-
iﬁcation), (ii) portability (by reducing the impact of diﬀerent
hardware conﬁgurations), and (iii) performance for code with
an optimized resource speciﬁcation (by leveraging dynamic
underutilization of resources). We conclude that Zorua is
an eﬀective, holistic virtualization framework for GPUs. We
believe that the indirection provided by Zorua’s virtualization
mechanism makes it a generic framework that can address
other challenges in modern GPUs. For example, Zorua can
enable ﬁne-grained resource sharing and partitioning among
multiple kernels/applications, as well as low-latency preemp-
tion of GPU programs. We hope that future work explores
these promising directions, building on the insights and the
framework developed in our MICRO 2016 paper.
Acknowledgments
We thank the reviewers and our shepherd for their valuable
suggestions. We thank the members of the SAFARI group for
their feedback and the stimulating research environment they
provide. Special thanks to Vivek Seshadri, Kathryn McKin-
ley, Steve Keckler, Evgeny Bolotin, and Mike O’Connor for
their feedback during various stages of this project. We ac-
knowledge the support of our industrial partners: Facebook,
Google, IBM, Intel, Microsoft, NVIDIA, Qualcomm, Samsung,
and VMware. This research was partially supported by NSF
(grant 1409723), the Intel Science and Technology Center for
Cloud Computing, and the Semiconductor Research Corpora-
tion.
References
[1] M. Abadi et al., “TensorFlow: A System for Large-Scale Machine Learning,” in
OSDI, 2016.
[2] M. Abdel-Majeed et al., “Warped Register File: A Power Eﬃcient Register File
for GPGPUs,” in HPCA, 2013.
[3] J. Ahn et al., “PIM-enabled instructions:
A low-overhead, locality-aware
processing-in-memory architecture,” in ISCA, 2015.
[4] J. Ahn et al., “A scalable processing-in-memory accelerator for parallel graph
processing,” in ISCA, 2015.
[5] G. M. Amdahl et al., “Architecture of the IBM System/360,” IBM JRD, 1964.
[6] R. Ausavarangnirun et al., “Exploiting Inter-Warp Heterogeneity to Improve
GPGPU Performance,” PACT, 2015.
[7] R. Ausavarungnirun et al., “Staged Memory Scheduling: Achieving High Prfor-
mance and Scalability in Heterogeneous Systems,” in ISCA, 2012.
[8] R. Ausavarungnirun et al., “Mosaic: A GPU Memory Manager with Application-
Transparent Support for Multiple Page Sizes.” in MICRO, 2017.
[9] R. Ausavarungnirun, V. Miller, J. Landgraf, S. Ghose, J. Gandhi, A. Jog, C. J. Ross-
bach, and O. Mutlu, “MASK: Redesigning the GPU Memory Hierarchy to Support
Multi-Application Concurrency,” in ASPLOS, 2018.
[10] C. G. Bell et al., “The Evolution of the DEC System 10,” CACM, 1978.
[11] A. Bensoussan et al., “The Multics Virtual Memory,” in SOSP, 1969.
[12] R. D. Blumofe et al., “Cilk: An eﬃcient multithreaded runtime system,” in ASP-
LOS, 1995.
[13] A. Boroumand et al., “Google Workloads for Consumer Devices: Mitigating Data
Movement Bottlenecks,” in ASPLOS, 2018.
[14] A. Boroumand, S. Ghose, M. Patel, H. Hassan, B. Lucia, K. Hsieh, K. T. Malladi,
H. Zheng, and O. Mutlu, “LazyPIM: An Eﬃcient Cache Coherence Mechanism
for Processing-in-Memory,” CAL, 2016.
[15] E. Brekelbaum et al., “Hierarchical scheduling windows,” in MICRO, 2002.
[16] K. K. Chang, P. J. Nair, D. Lee, S. Ghose, M. K. Qureshi, and O. Mutlu, “Low-Cost
Inter-Linked Subarrays (LISA): Enabling Fast Inter-Subarray Data Movement in
DRAM,” in HPCA, 2016.
[17] G. Chen et al., “PORPLE: An extensible optimizer for portable data placement on
GPU,” in MICRO, 2014.
[18] P. Chen, “N-Queens solver,” http://forums.nvidia.com/index.php?showtopic=
76893, 2008.
[19] H. Cook et al., “Virtual local stores: Enabling software-managed memory hier-
archies in mainstream computing environments,” Univ. of California, Berkeley,
EECS Dept., Tech. Rep. UCB/EECS-2009-131, 2009.
[20] R. J. Creasy, “The Origin of the VM/370 Time-sharing System,” IBM JRD, 1981.
[21] A. Davidson et al., “Toward Techniques for Auto-Tuning GPU Algorithms,” in
Applied Parallel and Scientiﬁc Computing.
Springer, 2010.
[22] P. J. Denning, “Virtual memory,” ACM Comput. Surv., 1970.
[23] R. Dolbeau et al., “HMPP: A hybrid multi-core parallel programming environ-
ment,” in GPGPU, 2007.
[24] Y. Dotsenko et al., “Auto-tuning of Fast Fourier Transform on Graphics Proces-
sors,” PPoPP, 2011.
[25] M. Erez et al., “Spills, Fills, and Kills - An Architecture for Reducing Register-
Memory Traﬃc,” Stanford Univ., Concurrent VLSI Architecture Group, Tech.
Rep. TR-23, July 2000.
[26] J. Fotheringham, “Dynamic storage allocation in the Atlas computer, including
an automatic use of a backing store,” CACM, 1961.
[27] M. Gebhart et al., “A Compile-time Managed Multi-level Register File Hierarchy,”
in MICRO, 2011.
[28] M. Gebhart et al., “Energy-eﬃcient Mechanisms for Managing Thread Context
in Throughput Processors,” ISCA, 2011.
[29] M. Gebhart et al., “A hierarchical thread scheduler and register ﬁle for energy-
eﬃcient throughput processors,” TOCS, 2012.
[30] M. Gebhart et al., “Unifying Primary Cache, Scratch, and Register File Memories
in a Throughput Processor,” in MICRO, 2012.
[31] A. Gonzalez et al., “Virtual-physical registers,” in HPCA, 1998.
[32] C. Gregg et al., “Fine-grained resource sharing for concurrent GPGPU kernels,”
in HotPar, 2012.
[33] P. H. Gum, “System/370 Extended Architecture: Facilities for Virtual Machines,”
IBM JRD, 1983.
[34] Q. Guo, N. Alachiotis, B. Akin, F. Sadi, G. Xu, T.-M. Low, L. Pileggi, J. C. Hoe, and
F. Franchetti, “3D-Stacked Memory-Side Acceleration: Accelerator and System
Design,” in WoNDP, 2014.
[35] T. D. Han et al., “hiCUDA: High-Level GPGPU Programming,” TPDS, 2011.
[36] A. B. Hayes et al., “Uniﬁed On-chip Memory Allocation for SIMT Architecture,”
in ICS, 2014.
[37] A. H. Hormati et al., “Sponge: Portable Stream Programming on Graphics En-
gines,” ASPLOS, 2011.
[38] K. Hsieh et al., “Accelerating pointer chasing in 3D-stacked memory: Challenges,
mechanisms, evaluation,” in ICCD, 2016.
[39] K. Hsieh et al., “Gaia: Geo-Distributed Machine Learning Approaching LAN
Speeds,” in NSDI, 2016.
[40] K. Hsieh et al., “Transparent Oﬄoading and Mapping (TOM): Enabling
Programmer-Transparent Near-Data Processing in GPU Systems,” in ISCA, 2016.
[41] B. Jacob et al., “Virtual memory in contemporary microprocessors,” IEEE Micro,
1998.
[42] H. Jeon et al., “GPU register ﬁle virtualization,” in MICRO, 2015.
[43] J. A. Joao et al., “Bottleneck identiﬁcation and scheduling in multithreaded ap-
plications,” in ASPLOS, 2012.
[44] J. A. Joao et al., “Utility-Based Acceleration of Multithreaded Applications on
Asymmetric CMPs,” in ISCA, 2013.
[45] A. Jog et al., “Orchestrated Scheduling and Prefetching for GPGPUs,” in ISCA,
2013.
[46] A. Jog et al., “OWL: Cooperative Thread Array Aware Scheduling Techniques
for Improving GPGPU Performance,” in ASPLOS, 2013.
[47] J. C. Juega et al., “Adaptive Mapping and Parameter Selection Scheme to Improve
Automatic Code Generation for GPUs,” in CGO, 2014.
[48] O. Kayiran et al., “µC-States: Fine-grained GPU Datapath Power Management,”
in PACT, 2016.
[49] M. Khan et al., “A Script-based Autotuning Compiler System to Generate High-
performance CUDA Code,” TACO, 2013.
[50] Khronos Group, “OpenCL,” https://www.khronos.org/opencl/.
9


---

Page 10

---

[51] J. S. Kim, D. Senol, H. Xin, D. Lee, S. Ghose, M. Alser, H. Hassan, O. Ergin,
C. Alkan, and O. Mutlu, “GRIM-Filter: Fast Seed Location Filtering in DNA Read
Mapping Using Processing-in-Memory Technologies,” BMC Genomics, 2018.
[52] P. M. Kogge, “EXECUBE—A New Architecture for Scaleable MPPs,” in ICPP, 1994.
[53] R. Komuravelli et al., “Stash: Have your scratchpad and cache it too,” in ISCA,
2015.
[54] N. B. Lakshminarayana et al., “Spare register aware prefetching for graph algo-
rithms on GPUs,” in HPCA, 2014.
[55] D. Lee et al., “Decoupled direct memory access: Isolating CPU and IO traﬃc by
leveraging a dual-data-port DRAM,” in PACT, 2015.
[56] H. Lee et al., “Locality-aware mapping of nested parallel patterns on GPUs,” in
MICRO, 2014.
[57] M. Lee et al., “Improving GPGPU resource utilization through alternative thread
block scheduling,” in HPCA, 2014.
[58] C. Li et al., “Automatic data placement into GPU on-chip memory resources,” in
CGO, 2015.
[59] Y. Liu et al., “A cross-input adaptive framework for GPU program optimizations,”
in IPDPS, 2009.
[60] Y. Low et al., “Distributed GraphLab: A Framework for Machine Learning and
Data Mining in the Cloud,” Proc. VLDB Endow., 2012.
[61] R. McGill et al., “Variations of box plots,” The American Statistician, 1978.
[62] V. Narasiman et al., “Improving GPU Performance via Large Warps and Two-
level Warp Scheduling,” in MICRO, 2011.
[63] NVIDIA, “CUDA,” https://developer.nvidia.com/about-cuda.
[64] NVIDIA, “Fermi: NVIDIA’s Next Generation CUDA Compute Architecture,”
2011.
[65] NVIDIA, “NVIDIA’s Next Generation CUDA Compute Architecture: Kepler
GK110,” 2012.
[66] NVIDIA, “Maxwell: NVIDIA’s Next Generation CUDA Compute Architecture,”
https://developer.nvidia.com/maxwell-compute-architecture, 2014.
[67] D. W. Oehmke et al., “How to Fake 1000 Registers,” in MICRO, 2005.
[68] S. Pai et al., “Improving GPGPU concurrency with elastic kernels,” in ASPLOS,
2013.
[69] J. Park et al., “Chimera: Collaborative Preemption for Multitasking on a Shared
GPU,” ASPLOS, 2015.
[70] D. Patterson, T. Anderson, N. Cardwell, R. Fromm, K. Keeton, C. Kozyrakis,
R. Thomas, and K. Yelick, “A Case for Intelligent RAM,” IEEE Micro, 1997.
[71] G. Pekhimenko et al., “Toggle-aware compression for GPUs,” in HPCA, 2016.
[72] J. Ragan-Kelley et al., “Halide: a language and compiler for optimizing paral-
lelism, locality, and recomputation in image processing pipelines,” PLDI, 2013.
[73] M. Sadrosadati et al., “LTRF: Enabling High-Capacity Register Files for GPUs via
Hardware/Software Cooperative Register Prefetching,” in ASPLOS, 2018.
[74] K. Sato et al., Automatic Tuning of CUDA Execution Parameters for Stencil Process-
ing.
New York, NY: Springer-Verlag, 2010.
[75] C. A. Schaefer et al., “Atune-IL: An instrumentation language for auto-tuning
parallel applications,” in Euro-Par, 2009.
[76] V. Seshadri et al., “RowClone: Fast and energy-eﬃcient in-DRAM bulk data copy
and initialization,” in MICRO, 2013.
[77] V. Seshadri et al., “Ambit: In-memory accelerator for bulk bitwise operations
using commodity DRAM technology,” in MICRO, 2017.
[78] D. E. Shaw, S. J. Stolfo, H. Ibrahim, B. Hillyer, G. Wiederhold, and J. Andrews,
“The NON-VON Database Machine: A Brief Overview,” IEEE Database Eng. Bull.,
1981.
[79] K. Spaﬀord et al., “Maestro: data orchestration and tuning for OpenCL devices,”
in Euro-Par, 2010.
[80] H. S. Stone, “A Logic-in-Memory Computer,” IEEE TC, 1970.
[81] M. A. Suleman et al., “Data marshaling for multi-core architectures,” in ISCA,
2010.
[82] M. A. Suleman et al., “Accelerating critical section execution with asymmetric
multi-core architectures,” in ASPLOS, 2009.
[83] I. Tanasic et al., “Enabling Preemptive Multiprogramming on GPUs,” in ISCA,
2014.
[84] D. Tarjan et al., “On demand register allocation and deallocation for a multi-
threaded processor,” US Patent Application 20110161616, 2011.
[85] S.-Z. Ueng et al., “CUDA-Lite: Reducing GPU Programming Complexity,” in
LCPC, 2008.
[86] H. Usui et al., “DASH: Deadline-Aware High-Performance Memory Scheduler
for Heterogeneous Systems with Hardware Accelerators,” TACO, 2016.
[87] N. Vijaykumar et al., “ A Case for Core-Assisted Bottleneck Acceleration in GPUs:
Enabling Flexible Data Compression with Assist Warps,” in ISCA, 2015.
[88] N. Vijaykumar et al., “Zorua: A Holistic Approach to Resource Virtualization in
GPUs,” in MICRO, 2016.
[89] C. A. Waldspurger, “Memory Resource Management in VMware ESX Server,” in
OSDI, 2002.
[90] Z. Wang et al., “Simultaneous Multikernel GPU: Multi-tasking Throughput Pro-
cessors via Fine-Grained Sharing,” in HPCA, 2016.
[91] P. Xiang et al., “Warp-level divergence in GPUs: Characterization, impact, and
mitigation,” in HPCA, 2014.
[92] X. Xie et al., “Enabling coordinated register allocation and thread-level paral-
lelism optimization for GPUs,” in MICRO, 2015.
[93] J. Yan et al., “Virtual Registers: Reducing Register Pressure Without Enlarging
the Register File,” in HIPEAC, 2007.
[94] J. Yan et al., “Exploiting Virtual Registers to Reduce Pressure on Real Registers,”
TACO, 2008.
[95] Y. Yang et al., “A GPGPU Compiler for Memory Optimization and Parallelism
Management,” PLDI, 2010.
[96] Y. Yang et al., “A Uniﬁed Optimizing Compiler Framework for Diﬀerent GPGPU
Architectures,” TACO, 2012.
[97] Y. Yang et al., “Shared memory multiplexing: a novel way to improve GPGPU
throughput,” in PACT, 2012.
[98] M. Yoon et al., “Virtual Thread: Maximizing Thread-Level Parallelism beyond
GPU Scheduling Limit,” in ISCA, 2016.
[99] J. Zalamea et al., “Two-level Hierarchical Register File Organization for VLIW
Processors,” in MICRO, 2000.
[100] D. Zhang, N. Jayasena, A. Lyashevsky, J. L. Greathouse, L. Xu, and M. Igna-
towski, “TOP-PIM: Throughput-oriented Programmable Processing in Memory,”
in HPDC, 2014.
10
