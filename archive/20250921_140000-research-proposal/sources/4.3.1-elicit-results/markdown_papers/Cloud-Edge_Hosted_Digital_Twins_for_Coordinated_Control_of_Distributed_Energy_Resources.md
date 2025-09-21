

---

Page 1

---

 
 
General rights 
Copyright and moral rights for the publications made accessible in the public portal are retained by the authors and/or other copyright 
owners and it is a condition of accessing publications that users recognise and abide by the legal requirements associated with these rights. 
 
 Users may download and print one copy of any publication from the public portal for the purpose of private study or research. 
 You may not further distribute the material or use it for any profit-making activity or commercial gain 
 You may freely distribute the URL identifying the publication in the public portal 
 
If you believe that this document breaches copyright please contact us providing details, and we will remove access to the work immediately 
and investigate your claim. 
  
 
   
 
 
Downloaded from orbit.dtu.dk on: Jun 03, 2025
Cloud-Edge Hosted Digital Twins for Coordinated Control of Distributed Energy
Resources
Han, Jiaxuan; Hong, Qiteng; Syed, Mazheruddin H.; Khan, Md Asif Uddin; Yang, Guangya; Burt, Graeme;
Booth, Campbell
Published in:
IEEE Transactions on Cloud Computing
Link to article, DOI:
10.1109/TCC.2022.3191837
Publication date:
2023
Document Version
Peer reviewed version
Link back to DTU Orbit
Citation (APA):
Han, J., Hong, Q., Syed, M. H., Khan, M. A. U., Yang, G., Burt, G., & Booth, C. (2023). Cloud-Edge Hosted
Digital Twins for Coordinated Control of Distributed Energy Resources. IEEE Transactions on Cloud Computing,
11(2), 1242-1256. Article 9832814. https://doi.org/10.1109/TCC.2022.3191837


---

Page 2

---

TRANSACTIONS ON CLOUD COMPUTING
1
Cloud-Edge Hosted Digital Twins for
Coordinated Control of Distributed Energy
Resources
Jiaxuan Han, Qiteng Hong, Mazheruddin H. Syed, Md Asif Uddin
Khan, Guangya Yang, Graeme Burt, and Campbell Booth
Abstract—This paper presents a novel approach for realizing coordinated control of Distributed Energy Resources (DERs) based on
cloud-hosted and edge-hosted digital twins (DTs) of DERs. DERs are playing an increasingly important role in supporting the
frequency regulation of power systems with massive integration of renewable resources. However, due to the significant differences in
DERs’ capability and characteristics, individual and un-coordinated responses from DERs could lead to a less effective overall
response with undesirable traits, e.g. slow response, severe overshoots, etc. Therefore, the coordination of DERs is critical to ensure
the desirable aggregated overall response. A major shortcoming of conventional centralized or distributed approaches is their
significant reliance on real-time communications. This paper addresses the challenges by the application of DTs that can be hosted in
the cloud for the centralized control approach and the edge for the distributed approach to minimize the need for real-time
communications, while being able to achieve the overall coordination among DERs. The proposed DT-based coordinated control is
validated using a realistic real-time simulation test setup, and the results demonstrate that the DT-based coordinated control can
significantly improve the aggregated DERs’ response, thus offering effective support to the grid during contingency events.
Index Terms—Cloud computing, distributed energy resources, distributed networks, digital twin, real-time control.
✦
1
INTRODUCTION
P
OWER systems globally are undergoing unprecedented
changes with decentralization and digitization trends
reshaping the energy sector through integration of renew-
able resources to meet the ambitious decarbonization tar-
gets [1]–[3]. According to the Paris agreement on climate
change, the Great Britain (GB) has committed to achieve
“Net Zero” greenhouse gas emission by 2050 and many
other countries also set ambitious decarbonization plans
[4]. Furthermore, the 26th UN Climate Change Conference
of the Parties (COP26) held in 2021 passed the Glasgow
Climate Pact, where the global community has reached
to an agreement with increased ambition to achieve the
target of controlling the global warming within 1.5ºC [5],
meaning continued and more ambitious global efforts on
decarbonization in the coming decades. As a result, massive
renewable generation are being connected to the power
systems, where significant amounts are Distributed Energy
Resources (DERs) integrated in the distribution systems, e.g.
PV cell, wind turbine, energy storage, biomass, etc. [6], [7].
This presents major challenges for power system operators,
as the integration of renewable generation will result in
the decrease of overall system inertia, thus leading to the
system frequency deviating faster during power imbalance
J. Han, Q. Hong, M. Syed, M. Asif, G. Burt, and C. Booth are with the
Institute for Energy and Environment, University of Strathclyde, Glasgow,
G1 1XQ, UK. Corresponding Author: Q. Hong, e-mail: q.hong@strath.ac.uk
G. Yang is with the Centre for Electrical Power and Energy, Technical
University of Denmark, Lyngby, Denmark. e-mail: gyy@elektro.dtu.dk
This
work
is
jointly
funded
by
EPSRC
via
the
RESCUE
project
(EP/T021829/1) and the European Union’s Horizon 2020 research and inno-
vation programme under grant agreement No 870620 - ERIGrid 2.0 project.
events (e.g. loss of generation). This could risk the statutory
frequency limit, (which is typically 49.5 Hz – 50.5 Hz) failing
to be met, and lead to significant increase of operational
costs [8].
While the massive amount of renewable can bring sig-
nificant challenges, the rapid integration of controllable
DERs at the grid edge also opens opportunities for DERs to
provide valuable services to support the future system op-
eration [9], e.g. provision of voltage support [10], frequency
response [11], improved power quality [12], reduction in
power losses [13], release of additional transmission and
distribution capacity [14], and improved reliability [15], etc.
Presently, there are many different control concepts being
proposed for DERs, which can be broadly categorized into
three main control strategies: 1) real and reactive power (PQ)
control; 2) voltage and frequency (V&f) control; and 3) droop
control [16]. The V&f control aims to maintain the voltage
and frequency of the grid at specified values by adjusting
their outputs, while with the droop control, the frequency
and voltage could deviate from the targeted values, but the
DERs will change their active and reactive references based
on the level of deviation and the configured droop setting
to provide the support to the grid. The DERs controlled by
these two types of strategies are generally used to support
islanded operation of microgrids [17]. Presently, the most
widely used control for DERs connected to the power grid
is equipped with the PQ control strategy (thus the focus of
this paper), where the active and reactive power outputs of
the DERs are controlled based on the commanded power set
points. One of the most typical ways for DERs to provide
the ancillary service for the system operators to support
frequency regulation is via commercial aggregators. During
This article has been accepted for publication in IEEE Transactions on Cloud Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TCC.2022.3191837
© 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on July 21,2022 at 09:00:51 UTC from IEEE Xplore.  Restrictions apply. 


---

Page 3

---

TRANSACTIONS ON CLOUD COMPUTING
2
frequency disturbances, DER aggregators will firstly evalu-
ate the active power response required (e.g. via frequency
control schemes as reported in [18]), and send requests
to a set of contracted DERs with PQ control strategies to
change their active power output (either increase or de-
crease power) and then the DERs will respond individually
to the commands to change their power outputs [19].
Due to the significant differences in DERs’ capability and
characteristics, individual and un-coordinated responses
from DERs could lead to a less effective overall response
with undesirable traits, e.g. slow aggregated response, se-
vere overshoots, etc. A coordinated approach where the
individual response characteristics of the DERs is harnessed
for enhanced dynamic cumulative response is desirable for
frequency during frequency events, especially in a system
with low inertia. However, one of the major drawbacks to
enable the effective coordination of the DERs is the require-
ment of high bandwidth real-time communication, which
is not cost-effective and the overall control performance
is highly dependent on the performance of the commu-
nications employed. Therefore, this paper presents a new
approach for realizing the effective coordinated control of
the DERs based on Digital Twins (DTs), which can minimize
the need for real-time communications, while being able to
achieve the overall coordination among DERs.
DT is considered to play a critical role in Industry 4.0,
and it is the core part of many emerging technologies, e.g.
Internet of Things (IoT), Cyber-Physical Systems (CPSs),
Big Data Analytics (BDA) [20]. One of the key features
of Industry 4.0 is the techniques for measuring, collecting
and processing high volume of real-time data (which is
also known as big data) to enable extensive applications
in different domains. The applications of big data typically
rely on a well-constructed five-layers CPSs architecture as
defined in [21] with the aid of cloud computing, which has a
similar structure with general definitions of DT. The concept
of DT was first introduced in [22], where it was defined as
a virtual representation of a physical component/system.
After years of research and development, the definition of
DT has evolved to ”an appropriately synchronized body of
useful information (structure, function, and behaviour) of a
physical entity in virtual space, with flows of information
that enable convergence between the physical and virtual
states” [23]. In the context of power systems, the DT is
more specifically defined as ”software-based abstractions of
complex physical systems or objects which are connected
via a communication link to the real object through a contin-
uous data flow from the real world” based on [24]. Despite
different definitions of the DT concepts, in general, a DT
can be considered as a realistic digital model of a physical
system that is being constantly updated by real-time data of
the physical system. The implementation of a prototype of
a physical component in DT can be achieved by using one
of these three methods: physics-based modelling [25], data-
driven modelling [26], [27] and big data cybernetics [28].
In recent years, the DT technology has been widely used
in different sectors in the industry (e.g. aerospace [29], [30],
smart manufacturing [31], transportation industries [32],
healthcare system [33] etc.). The trends of decarbonization
and digitization in energy sectors also promote the adoption
of the DT technique to facilitate renewable energy manage-
ment and increase energy efficiency, where comprehensive
discussions on the potential benefits of DTs and the associ-
ated advanced digitalization techniques on the energy sector
are presented in [34], covering a wide range of areas, e.g. nu-
clear power plant deployment, efficient energy distribution
and transmission, etc. In [35], a machine-learning driven DT
is applied in a nuclear power plant, which aims to under-
stand the complex interconnections of the nuclear power
plant and predict component failure. Based on [36], the
application of DT technology can significantly improve the
industrial productivity, efficiency, safety of the personnel,
and variability in the products life cycles with reduction in
the capital and operating costs, and health and environment
risks. The DT concept is also gaining increasing interests for
its application in the power industry, with the majority of
current applications in power system mainly focusing on
fault diagnosis and real-time online analysis of power grid.
In [37], a DT-based fault analysis system is developed for PV
systems to identify the fault types once they occur. Another
application on fault diagnosis was proposed in [38], which
aims to use the DTs as reference to monitor and assess the
health conditions of a given system. In [39], a data-driven
DT framework is presented for online analysis of the power
grid. To the authors’ best knowledge, there is very limited
work that has been reported on the application of DTs for
enhancing the control of DERs, which play a critical role
in future smart grid with high penetration of renewable
generation.
In this paper, the concept of DT is adopted to enable the
coordinated control of DERs to provide an optimal overall
response to the power grid, with the minimized need and
reliance on real-time communications. Two conventional
design and implementation approaches of DERs coordi-
nated control, i.e. centralized and distributed coordinated
control, will be firstly presented. It will be illustrated that
both approaches could present a relatively high reliance
on real-time communications, and the performance of the
communication system (e.g. latency) can have severe im-
pact of the control performance. Corresponding to the two
conventional coordinated control design, this paper presents
two new approaches based on the DTs of DERs: for the
centralized coordinated control, the proposed method uses
the DTs of the DERs hosted in a cloud server to estimate
the real-time outputs of the DERs (rather than gathering the
information continuously via communications), which are
used by the controller (also hosted in the cloud) to coor-
dinate the DERs’ response; for the distributed coordinated
control design, the proposed method proposes to have the
DTs of the DERs hosted in the grid edge at individual DERs’
sites, along with the coordinated controller. Similarly, the
DTs are used to to estimate the real-time outputs of the
DERs for the coordinated controller to minimize the need for
real-time communication. It will be demonstrated that for
both centralized and distributed approaches, the proposed
DT-based coordinated control can largely mitigate the need
and reliance on communications, while being capable of
delivering effective support to the grid during contingency
events.
Therefore, the key research motivation of the work is to
provide a solution that is both technically and economically
effective to enable the coordination of DERs in supporting
This article has been accepted for publication in IEEE Transactions on Cloud Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TCC.2022.3191837
© 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on July 21,2022 at 09:00:51 UTC from IEEE Xplore.  Restrictions apply. 


---

Page 4

---

TRANSACTIONS ON CLOUD COMPUTING
3
the frequency control in future power systems. The paper
addresses the research gap of the existing work on coor-
dinated control of DERs, e.g. [40], [41], which has signif-
icant dependence and reliance on high-speed and high-
bandwidth real-time communications between the central
controller and the individual DERs are required, resulting
in poor performance and high costs. The uniqueness of
the solution provided by the paper can be summarised as
follows: 1) through the use of the DTs of DERs, the proposed
DT-based coordinated control enables effective coordination
of DERs, which can deliver an optimal overall response to
support the grid. This provides a promising solution for
DERs to play a critical role in future frequency regulation in
low-inertia power systems; and 2) two approaches to enable
the DT-based coordinated control have been proposed and
presented, i.e. the DT can either be hosted in the cloud
or in the edge, where both approaches demonstrate highly
effective performance with significantly reduced reliance on
real-time communications.
The rest of the paper is organised as follows: Section
2 presents the fundamental principle of the coordinated
control being used in this paper for optimizing the aggre-
gated DERs’ response; Section 3 presents the design and
implementation of the coordinated control based on the DT
of the DERs for both centralized and distributed schemes;
In section 4, the test network and the process of creating
the DTs of the DERs in the test network are presented; In
Section 5, case studies are presented to validate the perfor-
mance the DT-based coordinated control, with comparison
of conventional implementations; In Section 6, the benefits
of the proposed DT-based coordinated control for enterprise
are discussed; and finally, Section 7 provides conclusions of
the paper.
2
COORDINATED CONTROL
AND
ITS CONVEN-
TIONAL IMPLEMENTATION
In this section, a coordinated control scheme is presented
followed by two options for its conventional implemen-
tation in real world, i.e., centralized and distributed ap-
proaches, which will serve as the reference for comparison
of the DT-based design and implementation, which is pre-
sented in Section 3.
2.1
Coordinated Control Method For DERs
Considering an example network, representing either a low
voltage feeder or a microgrid, with N controllable DERs
(denoted by i = 1, 2, ..., N) as shown in Fig. 1, we assume
that M DERs, M ⊂N, are contracted by an aggregator to
provide ancillary services to the system operator at the point
of common coupling (PCC). Given a disturbance within the
network, PM is the total reserve activation requested by
the aggregator from the M contracted DERs, which can be
represented as:
PM =
M
X
i=1
pisp(t)
(1)
where pisp is the set point of the ith participating DER.
If there is no additional coordinated control implemented,
the DERs will simply follow the set points sent by the
aggregate purely with their PQ controllers. However, it will
be demonstrated in Section 5 that the overall aggregated
DERs response can be undesirable due to the significant
differences in DERs capabilities and characteristics.
2.1.1
Improving local response
A simple set point modulation technique can be employed
for improved local response of the DER, i.e. purely based on
each DER’s own actual power output without considering
other DERs. The set point of the ith DER is modified as
p′
isp(t) = pisp + uI
i (t)
(2)
where uI
i is the modulation factor defined as
uI
i (t) = mi × ˆeipred(t).
(3)
where ˆeipred is the predicted active power output error from
a linear error trajectory predictor used in this work. The
error in power over prediction horizon Tpred is
ˆeipred(t0 + Tpred) = ei(t0) + r(t0)Tpred
(4)
where r(t0) is the average rate of change of error calculated
over past measurements based on least squares error and
ei is the measured error in active power output of DER i
calculated as
ei(t) = pisp −pim
(5)
where Pim is the measured active power output of DER i.
2.1.2
Improving global response
A global improved dynamic response, i.e. an improved
aggregated response from all DERs, can be obtained if the
DERs participating in ancillary service provision coordinate
their individual responses. The coordinated control aims to
improve a DERs’ individual response using other M −1
participating DERs in order to ensure fast and optimized
dynamic response from all participating DERs at the PCC.
The set point of the ith DER is therefore modified as:
p′′
isp(t) = pisp + uI
i (t) + uII
i (t)
(6)
where uII
i
is the modulation factor of coordinated control:
uII
i (t) = mi
M
X
j=1,j̸=i
ˆejpred(t)
(7)
where ˆejpred(t) is the predicted output power error of jth
DER. Substituting (2) to (5), the DERs’ set points become:
p′′
isp(t) = p′
isp(t) + uII
i (t)
(8)
The coordinated control is complementary for each DER,
i.e., the response of each DER is adapted to ensure the global
response (at point of common coupling) is improved.
It should be noted that the presented coordinated control
in this section is an example control scheme for demon-
stration purpose only to illustrate the advantage of the
DT-based design and implementation, and the coordinated
algorithm itself is not a contribution of the paper. The main
contribution of the paper is the new design and imple-
mentation approaches in realizing the coordianted control
with the DTs of DERs hosted in the cloud and edge for
minimizing the reliance on real-time communication with
effective overall control performance.
This article has been accepted for publication in IEEE Transactions on Cloud Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TCC.2022.3191837
© 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on July 21,2022 at 09:00:51 UTC from IEEE Xplore.  Restrictions apply. 


---

Page 5

---

TRANSACTIONS ON CLOUD COMPUTING
4
DER1
DER2
DER M
DER1 Control 
DER1 Control 
Coordinated Control
Eq. (2), (7), (8) 
DER2 Control 
DER2 Control 
DER M  Control 
DER M  Control 
...
...
p1sp, p2sp, ... pMsp
p1sp, p2sp, ... pMsp
p1sp
’’
p1sp
’’
p1m
p1m
p2sp
’’
p2sp
’’
p2m
p2m
pMsp
’’
pMsp
’’
pMm
pMm
(a)
DER1 Control 
DER1 Control 
p1sp
’’
p1sp
’’
pMsp
’’
pMsp
’’
p1sp
p1sp
DER2 Control 
DER2 Control 
p2sp
’’
p2sp
’’
DER M Control 
DER M Control 
p2sp
p2sp
pMsp
pMsp
pMm
pMm
p2m
p2m
p1m
p1m
p2m
p2m
pMm
pMm
p1m
p1m
p1m
p1m
Coordinated 
Control 
Coordinated 
Control 
Coordinated 
Control 
Coordinated 
Control 
p2m
p2m
Coordinated 
Control 
Coordinated 
Control 
pMm
pMm
Eq. (2), (7), (8)
Eq. (2), (7), (8)
Eq. (2), (7), (8)
(b)
Controller at the Edge
DT2
DER1 Control 
DER1 Control 
DT M
DT M
...
DT1 
DT1 
Coordinated 
Control 
Coordinated 
Control 
DER M Control 
DER M Control 
...
DT1 
DT1 
DT2
p1sp, p2sp, ... pMsp
p1sp, p2sp, ... pMsp
p2m
p2m
pMm
pMm
p1sp
’’
p1sp
’’
Coordinated 
Control 
Coordinated 
Control 
DER2 Control 
DER2 Control 
DT M
DT M
...
p1m
p1m
pMm
pMm
p2sp
’’
p2sp
’’
Coordinated Control
Eq. (2), (7), (8) 
p1m
p1m
p2m
p2m
pMsp
’’
pMsp
’’
pMm
pMm
p1m
p1m
p2m
p2m
p1sp, p2sp, ... pMsp
p1sp, p2sp, ... pMsp
p1sp, p2sp, ... pMsp
p1sp, p2sp, ... pMsp
(d)
DER Aggregator 
DER Aggregator 
DER Aggregator 
DER1 Control 
DER1 Control 
DT1 
DT2 
DT M 
DT1 
DT2 
DT M 
DER2 Control 
DER2 Control 
DER M  Control 
DER M  Control 
Cloud 
Server
...
DER Aggregator 
p1sp
p1sp
...
Coordinated Control
Eq. (2), (7), (8) 
Coordinated Control
Eq. (2), (7), (8) 
p1sp
’’
p1sp
’’
p2sp
’’
p2sp
’’
pMsp
’’
pMsp
’’
p2sp
p2sp
pMsp
pMsp
(c)
Conventional 
Implementations 
DT-based 
Implementations 
...
DER1
DER2
DER M
...
DER1
DER2
DER M
...
DER1
DER2
DER M
Fig. 1: Conventional and proposed DT-based coordinated control of DERs: (a) conventional implementation: centralized;
(b) conventional implementation: distributed; (c) DT-based implementation: centralized; (d) DT-based implementation:
distributed.
2.2
Conventional Implementation: Centralized Coordi-
nated Control
The coordinated control presented in Section 2.1 can be
realized via a centralized approach with a conventional
implementation as illustrated in Fig. 1.(a). In the conven-
tional centralized approach, it is assumed that the coordi-
nated control is implemented within the aggregator. The
coordinated controller, as evident from Eq (7), requires the
knowledge of the predicted output power error (ˆeipred) of
DERs and therefore each DER sends its measured power
output (Pim) in real time to the aggregator for its calculation.
The coordinated controller will use the desired set points re-
quested by the aggregator and the real-time communicated
power output (Pim) to optimise the set points to be sent
to the DERs. Consequently, as opposed to the aggregator
sending the individual power set point (pisp) to the ith DER,
the modified power set point (p′′
isp) is sent instead. It can
be seen that, in this approach, it requires bi-directional real
time communications between the DER aggregator and the
individual DERs, and this represents 2M communication
links for M DERs participating in the ancillary service. Fur-
thermore, for each time step, the control algorithm relies on
the real-time output from DERs (Pim) to send the modified
power set point (p′′
isp), therefore, the performance of the
communication channels will have a significant impact on
the overall performance. It will be demonstrated in Section 5
that the communication delay could lead to highly unstable
response from the DERs.
2.3
Conventional Implementation: Distributed Coordi-
nated Control
An alternative to the centralized implementation of the
coordinated control is to implement the controller in a
distributed manner. Fig 1.(b). presents the conventional
implementation of the distributed coordinated control for
the DERs. As can be observed, instead of having a single
coordinated controller hosted in the aggregator site, each
of DERs participating the ancillary service will have one
coordinated controller implemented in its site, i.e. there are
M coordinated controllers in the M DER sites distributed
across the network. One of the main benefits for which
is implemented within each of the distributed approach is
that it avoids the total failure of the overall scheme when
one coordinated controller fails (as it will be the case of
This article has been accepted for publication in IEEE Transactions on Cloud Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TCC.2022.3191837
© 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on July 21,2022 at 09:00:51 UTC from IEEE Xplore.  Restrictions apply. 


---

Page 6

---

TRANSACTIONS ON CLOUD COMPUTING
5
the centralized approach presented in Section 2.2). In this
approach, individual DERs will still need to receive the
power set points (pisp) from the aggregator, and then the
DERs will start exchanging their predicted error (ˆeipred) for
the calculation of the modified reference power set point
(p′′
isp) via communications with other DERs. Therefore, each
DER will need bi-directional communication with the rest
of the M −1 DERs, representing a total of M(M −1)
links among DERs and another M links between individual
DERs with the aggregator for the set point. Similar to the
centralized approach, with the distributed implementation,
it will be demonstrated in Section 5 that the communication
delay could significantly compromise the overall aggregated
response from the DERs.
3
PROPOSED DIGITAL TWIN BASED IMPLEMENTA-
TION OF COORDINATED CONTROL
In a step change to conventional control implementation,
this paper proposes the use of DTs of DERs to estimate
the predicted output power error of each participating DER
to realize the proposed coordinated control scheme thereby
largely mitigating the need for real-time communications.
3.1
DT-based Implementation: Centralized Coordinated
Control
The proposed design and implementation of coordinated
control with the centralized scheme using DTs of the DERs
is illustrated in Fig. 1.(c). The coordinated controller and
the DTs of the DERs are all implemented within the cloud
platform of the aggregator (analogous to the conventional
centralized implementation). However, contrary to the con-
ventional centralized approach that requires bi-directional
real-time communication between the central coordinated
controller and individual DERs for exchange of measured
power output pim and modified power set point (p′′
isp), in
this approach, dynamic behaviour of DERs can be estimated
by their DTs at the cloud based on the inputs set point
inputs from the aggregator’s commands rather than relying
on real-time information exchange with DERs.
As the coordinated control is mainly concerned with the
active power dynamic behaviour of the DERs in response to
the set point comments, analytical models of the DERs that
can accurately represent such dynamic characteristics can be
used to served as the the DERs’s DTs. Section 4.2 presents
the details of the development of DTs of the DERs. The DTs
of the DERs are hosted in the could server, enabling access
to the real-time estimated behavior of the DERs to be readily
utilized by the coordinated control strategy. The outputs
from the coordinated controller are modified power set
point (p′′
isp) based on the estimated DERs’ real time power
rather than actual power, and they will be sent from the
cloud to the M individual DERs via communication links,
and the need for communication channel is reduced from
2M to M. This approach has the advantage of using the
computation capability provided by the cloud for running
the coordinated control scheme while largely mitigating the
real-time communications required.
3.2
DT-based Implementation: Distributed Coordinated
Control
The proposed design and implementation of coordinated
control with the distributed scheme using DTs of the DERs
is illustrated in Fig. 1.(d). In this case, both of the DTs
and the coordinated controllers are hosted at the edge in
DERs’ sites (analogous to conventional distributed control
implementation). In contrast to conventional distributed
implementation where the predicted output power error
(ˆeipred) is exchanged through real-time communications, in
this approach, for the the ith DER, the DTs of all other
(M-1) participating DERs will be incorporated in its local
site. This allows for estimation of the real-time behaviour of
other DERs purely using a set points sent by the aggregator,
thus enabling the coordinated control without the need for
real-time communications with other DERs. As illustrated in
Fig. 1.(d), communications between the aggregator and the
DERs will still be required, but this approach eliminates all
the real-time communications among DERs, which largely
mitigates the reliance on communications. This effectively
presents an approach that transforms a distributed control
implementation to a decentralized control implementation
requiring no real-time communications. However, this ap-
proach will present relatively high requirement on the DER
controllers’ computation capability as the DTs and coordi-
nated controllers are run in real time at the edge.
4
TEST NETWORK AND DEVELOPMENT OF DTS
FOR DERS
4.1
Test Network
In this work, the modified benchmark low voltage network
by Conseil International des Grands R´eseaux Electriques
(CIGRE) task force C6.04.02 has been chosen as the test AC
network [42], [43] and is illustrated in both Fig. 4 and Fig. 9.
The network comprises of a number of feeders that supply
residential, commercial and industrial loads with a nominal
voltage of 20 kV. Therefore, five DERs in the network, all
participating the frequency response ancillary service via
a commercial aggregator. The DERs 1-3 represent battery
energy storage units, rated active power of 100 kW, 150 kW,
and 200. DERs 4 and 5 represent electric vehicle charging
stations with rated active power of 250 kW and 300 kW
respectively. For the purpose of demonstrating the DT-based
coordinated control (via both centralized implementation at
the cloud and the distributed implementation at the edge), it
is assumed that all DERs are capable of sourcing and sinking
power to/from the grid.
4.2
Development of DTs for the DERs
As discussed in Section 1, the creation of the models for
DTs can generally be realized via physics-based and data-
driven modelling. For the physics-based approach, good
knowledge and understanding of the DER system and its
inherent controller is required. In practice, this could be
difficult as the information might not be readily available
for the DER aggregator or owners of other DERs. Therefore,
in this paper, the data-driven approach is utilized to capture
the dynamics of the DERs in response to power reference
commands, thus generating the model in the format of
This article has been accepted for publication in IEEE Transactions on Cloud Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TCC.2022.3191837
© 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on July 21,2022 at 09:00:51 UTC from IEEE Xplore.  Restrictions apply. 


---

Page 7

---

TRANSACTIONS ON CLOUD COMPUTING
6
transfer functions. The detailed process is illustrated in Fig.
2.
Time Series Data
(Power command & DER 
response power)
Transfer Function 
Specification
Number of Zeros and Poles
Generate Transfer 
Function
(DER’s analytical model) 
Yes
III
System 
Identification 
Toolbox in 
MATLAB
DER Model 
Accuracy 
Evaluation
No
I
DER Testing
Step Response of 
Active Power
DER Testing
Step Response of 
Active Power
Time
Pm
0.001
0.002
0.003
…
…
Pref
…
Time
Pm
0.001
0.002
0.003
…
…
Pref
…
Data Import
(Import to MATLAB  
workspace)
 Model Accuracy 
Evaluation 
(Compare analytical model with 
actual DER response )
ModelAccuracy 
Acceptable?
Interface DER model with 
real time live data source   
Creation of 
DT of DER
DT of DER created
II
Fig. 2: The process of implementing DTs for the DERs
The process starts with applying a step command to the
active power reference signal of the targeted DER. This can
be done with the physical DER or a detailed DER model,
which could be in a black-box format without the need
to share internal details with aggregator and other DER
owners. The reference power signal and the response active
power will be monitored and recorded in the format of the
time series data, which can be subsequently imported to
system identification tools. In this work, the system identi-
fication toolbox available in MATLAB is used as illustrated
in Stage I in Fig. 2. To perform the system identification,
the anticipated system characteristics should be specified
via defining the number of zeros and poles of the transfer
function. The generated transfer function can be simulated
with the same input power reference step change signal
and the response can be compared with the actual DER’s
behaviour as shown in Stage II in Fig. 2. The process of
stage I and II can be automated via scripts until the model
accuracy meets the pre-defined criteria.
Once the accuracy of the model is considered as ac-
ceptable, the model can be implemented on appropriate
platforms and interfaced with the live data sources so that
it can be updated in real-time as a DT to reflect the actual
behaviour of the DER. Fig. 3 presents the responses from
the DTs created based on the process illustrated in Fig.
2. In comparison of the actual behaviour of the DERs,
Fig. 3 shows that the DTs can accurately reflect the DERs’
dynamics with the supplied set point signals.
Fig. 3: Comparison of the responses from DTs and DERs
5
CASE STUDY
5.1
Case Study 1: Testing of DT-based implementation:
centralized coordinated control
5.1.1
Laboratory Implementation
As illustrated in Fig. 1.(c), in the case of the DT-based
implementation for the centralized coordinated control, the
DTs of the DERs and the coordinated controller are hosted
in the cloud server. Fig. 4 presents a realistic Hardware-in-
the-Loop (HIL) setup, which includes a Real-Time Digital
Simulator (RTDS) for simulating the network with five
DERs as discussed in Section 4.1 and a desktop PC acting as
a cloud server. The real-time simulation in RTDS is commu-
nicated with the sever via an Ethernet switch to exchange
information using the UDP protocol. During a simulated
frequency disturbance event, the commands pisp from the
aggregator are sent to DTs without any communication
delay because DTs are located at the same cloud server as
the aggregator functions. A key benefit of this approach is
that the communication required for sending active outputs
from the DERs to coordinated controller in the cloud can be
avoided. Based on the set points of the aggregator, DTs are
used to estimate the real-time power outputs of the DERs,
This article has been accepted for publication in IEEE Transactions on Cloud Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TCC.2022.3191837
© 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on July 21,2022 at 09:00:51 UTC from IEEE Xplore.  Restrictions apply. 


---

Page 8

---

TRANSACTIONS ON CLOUD COMPUTING
7
which are used by the coordinated controller to generate the
modified set points p′′
isp for optimizing the overall response
as discussed in Section 2. Any error exists in the DTs can
be detected and compensated by the coordinated controller.
In the test setup, a function block emulating communication
delays has also been created in RTDS for testing the impact
of the communication latency between the aggreator and
the DERs on the proposed DT-based centralized coordinated
control for DERs. In the tests presented in this section, the
communication delay is set as 50 ms, which is considered
to be realistic to be realized with low-cost communications
based on the work reported in [44].
5.1.2
Case 1.1: Simultaneous change in set point of DERs
In this case, it is assumed that the aggregator detects a
frequency event and sends power set points to all of the five
DERs simultaneously to request a same amount of increase
in active power output (i.e. 100 kW) at 0.4 s (received by
the DERs at 0.45 s due to the 50 ms communication delay).
Therefore, the overall aggregated increase of active power
from the five DERs is expected to be 500 kW. Fig. 5 and Fig.
6 present the individual and overall aggregated responses of
the DERs with their inherent PQ control (i.e. no coordinated
control deployed), conventional coordinated control, and
the DT-based coordinated control.
It can be clearly seen from Fig. 5 that different DERs have
different responses to set points sent by the aggregator for
requesting the increase in active power. With the inherent
control of the DERs (i.e. no coordinated control), as shown in
6, the aggregated overall response is relatively slow with a
certain level of overshoot. This could be problematic for the
system operator when there are large number of aggregator
with a significant capacity of DERs providing the ancillary
service to the grid.
With the conventional implementation of coordinated
control, due to the communication delay and its high re-
liance on communication performance, significant errors
between the reference power and the actual output for
each DER response can be observed, thus leading to an
0.44
0.46
0.48
0.5
0.52
0.54
0.56
0.58
0.6
0
0.05
0.1
0.15
DER1
0.44
0.46
0.48
0.5
0.52
0.54
0.56
0.58
0.6
0
0.05
0.1
0.15
DER2
Inherent Control
Conventional Coordinated Control
DT-based Coordinated Control
Reference Power
0.44
0.46
0.48
0.5
0.52
0.54
0.56
0.58
0.6
0
0.05
0.1
0.15
Individual Power Output (MW)
DER3
0.44
0.46
0.48
0.5
0.52
0.54
0.56
0.58
0.6
0
0.05
0.1
0.15
DER4
0.44
0.46
0.48
0.5
0.52
0.54
0.56
0.58
0.6
Time (s)
0
0.05
0.1
0.15
DER5
Fig. 5: Individual responses of DERs with simultaneous set
point change - same amount of power requested from all
DERs
undesirable overall response. Furthermore, due to the com-
munication delay, it appears that the coordinated controller
experiences stability issues with severe oscillations in active
power, which will contribute negatively to the the overall
system frequency regulation.
In the case of DT-based coordinated control, since the
coordinated controller receives data from the corresponding
GTNET card
Hardware platforms
Ethernet Switch
UDP Packets
DERs control 
command
Communication Interface
DT1 
Coordinated Control 
Coordinated Control 
DERs control 
command
Real time 
simulation
PCC
Main 
Grid
DER1
DER2
DER3
DER4
DER5
DER Aggregator
Communication 
Delay
Cloud-Hosted 
Digital Twins for 
DER Coordinated 
Control 
DT2 
DT3 
DT4 
DT5 
Server
Fig. 4: Test setup for DT-based implementation: centralized coordinated control of DERs
This article has been accepted for publication in IEEE Transactions on Cloud Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TCC.2022.3191837
© 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on July 21,2022 at 09:00:51 UTC from IEEE Xplore.  Restrictions apply. 


---

Page 9

---

TRANSACTIONS ON CLOUD COMPUTING
8
Fig. 6: Aggregated responses of DERs with simultaneous set
point change - same amount of power requested from all
DERs
DTs located in the cloud, rather than relying on active power
communicated from the DERs, the overall response from
has significantly improved with faster response and shorter
settling time as shown in Fig.6. Examining the individual
DER responses as shown Fig.6, the DT-based coordinated
control refines the individual responses (e.g. DER 2 re-
sponds faster with an overshoot and DER 5 responds slowly
compared to other DERs) so that they can complement with
each other to form an improved overall response.
Similar observations as described above with the case
presented in Fig 7, where the DERs are commanded to
output different amounts of active power to deliver a total of
1 MW response against a frequency event. As it can be seen
that the DT-based coordinated control presents an improved
response compared with the case with DERs inherent con-
trollers. It should be noted that the case with conventional
implementation approach has been demonstrated to be un-
stable in Fig. 6, thus not being shown again in Fig. 7.
Fig. 7: Aggregated responses of DERs with simultaneous set
point change - different amounts of power requested from
all DERs
5.1.3
Case 1.2: Staggered change in set points of DERs
Similar to the previous case as explained in Section 5.1.2,
the aggregator detects a frequency event and sends power
set points to all of the five DERs to request a same amount
of increase in active power output (i.e. 100 kW) but in
this case, at different time (emulating a more realistic case
where the set points are not sent precisely simultaneously
by the aggregator). The overall aggregated increase of active
power from the five DERs is still expected to be 500 kW but
not at the same time. The overall aggregated coordinated
control responses for the DERs inherent control and DT-
based coordinated control are presented in Fig. 8.
Fig. 8: DERs’ Power output with applying staggered power
reference inputs
In the inherent control of the DERs, as shown in 8, the
aggregated overall response from the DERs is relatively
slow and less effective. However, in the case of DT-based
coordinated control, the overall response is comparably
faster and more effetive in tracking the reference power
compared with the inherent control of the DERs.
5.2
Case Study 2: Testing of DT-based implementation:
distributed coordinated control
5.2.1
Laboratory Implementation
The DT-based distributed coordinated control is illustrated
in Fig. 1 (d), from which it can be seen that the DTs of
the DERs are hosted in DERs’ sites. The test setup for
evaluating the DT-based distributed coordinated control is
illustrated in 9, which includes the test network with the
five DERs participating in the ancillary service, a functional
block emulating the aggregator, and the corresponding DTs
of the DERs installed at the DERs sites along with the
coordinated controllers. In this setup, in order to estimate
the dynamic behaviours of other DERs, while avoiding the
need for bi-directional real-time communication with them,
each DER hosts DTs of the other four DERs locally. The DTs
are updated based on the set point signals for all DERs sent
by the aggregator.
Once a frequency event is detected, the aggregator will
send requests of active power changes via power set points
pisp to DERs and their hosted DTs of other DERs. Different
from the DT-based centralized approach, each DER in this
case receives all the power set points pisp rather than the
designated one for themselves in order to provide inputs
for local DTs for estimated other DERs’ outputs. These
estimated DERs’ outputs are used by the coordinated con-
trollers installed at each DER site to generate modulated
reference power p′′
isp for DER and DTs. The DER and DTs
will then output certain power according to the received
p′′
isp(t). As this process only invovlves the use of the set
points communicated from the aggregator without the need
This article has been accepted for publication in IEEE Transactions on Cloud Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TCC.2022.3191837
© 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on July 21,2022 at 09:00:51 UTC from IEEE Xplore.  Restrictions apply. 


---

Page 10

---

TRANSACTIONS ON CLOUD COMPUTING
9
Real time simulation
PCC
Main 
Grid
DER1
DER2
DER3
DER4
DER5
DT2, DT3, 
DT4, DT5 
Coordinated 
Control 
DT Based 
Controller 1
DT Based 
Controller 2 
DT Based 
Controller 3 
DT Based 
Controller 4
DT Based 
Controller 5
DER 
Aggregator
Communication 
Delay
Edge Hosted 
Digital Twins for 
DER Coordinated 
Control 
Fig. 9: Test setup for DT-based implementation: distributed coordinated control of DERs
for communciation with other DERs, the performance of
the proposed DT-based coordinated control scheme can
largely mitigate the reliance on the communications, which
is demonstrated in the following sections.
5.2.2
Case 2.1: Simultaneous change in set point of DERs
In this test case, the aggregrator sends power set points to all
of the five DERs simultaneously to request a same amount
of increase in active power output (i.e. 100 kW) at 0.4 s.
The results for this case are presented in Fig. 10 and Fig.
11 for individual DER responses and overall aggregated
responses respectively. For the comparison purpose, DERs
inherent control, conventional coordinated control and DT-
based coordinated control responses are presented in the
same figures.
As it can be seen form Fig. 10 and 11 that, in the
case of inherent control, the aggregated overall response is
relatively slow due to slow responses from each DER, along
with a certain level of overshoot and relatively long settling
time. Such behaviour is not ideal for the overall frequency
regulation especially with large number of aggregators and
a large capacity of participating DERs.
With the conventional coordinated control, significantly
large errors between the reference power and the actual
power output for each DER can be observed due to commu-
nication delay between the among the DERs (as illustrated
in Fig. 1.(c)). These errors also lead to an oscillation in the
overall response of the DERs, which might could severely
comprise the system’s frequency control performance.
In the case of DT-based distributed coordinated control,
due to the DTs are located in the DERs sites without the need
for communication with other DERs, it has significantly
faster response and shorter settling time compared to the
other two approaches.
Fig. 12 present another case that has been tested with
1 MW total active power requested simultaneously by the
0.38
0.4
0.42
0.44
0.46
0.48
0.5
0.52
0.54
0
0.05
0.1
0.15
DER1
0.38
0.4
0.42
0.44
0.46
0.48
0.5
0.52
0.54
0
0.05
0.1
0.15
DER2
Inherent Control
Conventional Coordinated Control
DT-based Coordinated Control
Reference Power
0.38
0.4
0.42
0.44
0.46
0.48
0.5
0.52
0.54
0
0.05
0.1
0.15
Individual Power Output (MW)
DER3
0.38
0.4
0.42
0.44
0.46
0.48
0.5
0.52
0.54
0
0.05
0.1
0.15
DER4
0.38
0.4
0.42
0.44
0.46
0.48
0.5
0.52
0.54
Time (s)
0
0.05
0.1
0.15
DER5
Fig. 10: Individual responses of DERs with simultaneous set
point change - different amounts of power requested from
all DERs
aggregator but with different amounts for each DER. The
results along with comparison between inherent and DT-
based coordination control are shown in 12. Similar obser-
This article has been accepted for publication in IEEE Transactions on Cloud Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TCC.2022.3191837
© 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on July 21,2022 at 09:00:51 UTC from IEEE Xplore.  Restrictions apply. 


---

Page 11

---

TRANSACTIONS ON CLOUD COMPUTING
10
Fig. 11: Aggregated responses of DERs with simultaneous
set point change - same amount of power requested from all
DERs
vation as motioned above for Fig. 11 can be made for both
DT-based coordinated control and the inherent DER control,
where DT-based coordinated control shows significantly
improved response.
Fig. 12: Aggregated responses of DERs with simultaneous
set point change - different amounts of power requested
from all DERs
Fig. 13: Power output with coordinate control by applying
staggered inputs
5.2.3
Case 2.2: Staggered change in set points of DERs
In this case, the aggregrator sends power set points to all of
the five DERs to request a same amount of increase in active
power output (i.e. 100 kW) but at different time rather than
sending signal simultaneously. The results for this case are
shown in Fig. 13. It can be observed that the overall response
from the DT-based coordinated control is faster with more
effective tracking of the reference power compared to the
inherent control of the DERs.
5.3
Case Study 3: Effectiveness of DT-based coordi-
nated control in supporting grid frequency regulation
In practice, electricity system operators are required to
maintain the frequency close to its nominal value, which
is 50 Hz in the GB network. The ultimate objective of
the coordinated control using DTs of DERs either hosted
in the cloud (centralized) or at the edge (distributed) as
demonstrated in Section 5.1 and 5.2 is to support the control
of grid frequency, which can deviate from its nominal value
during load-generation imbalance events. Based on the cur-
rent National Electricity Transmission System Security and
Quality of Supply Standard [8], the statuary frequency limit
should be maintained between 49.5 Hz – 50.5 Hz. In this
case study, it will be shown how conventional frequency
FH 
FH 
FH 
1 - FH  
1+TRs 
Km 
Km 
Km 
R
1
R
1
2Hss
1
2Hss
1
+
-
+
+
-
+
∑ 
∑ 
+
+
D
+
+
∑ 
∑ 
ΔPset 
ΔPset 
ΔPm 
ΔPm 
ΔP 
ΔP 
PMGs
PMGs
-
Δf 
Δf 
ΔPevent 
ΔPevent 
FH 
1 - FH  
1+TRs 
Km 
R
1
2Hss
1
+
-
+
∑ 
+
+
D
+
+
∑ 
ΔPset 
ΔPm 
ΔP 
PMGs
-
Δf 
ΔPevent 
+
-
+
-
fnfn
 
Microgrid Model
PCC
Frequency 
controlled 
voltage source
DER1
DER2
DER3
DER4
DER5
Microgrid Model
PCC
Frequency 
controlled 
voltage source
DER1
DER2
DER3
DER4
DER5
Scaling Factor n
Scaling Factor n
Scaling Factor n
Scaling Factor n
Scaling Factor n
fgrid
fgrid
Analytical 
Grid Emulator
PMG
PMG
∑ 
PDER4
PDER4
PDER5
PDER5
PDER1
PDER1
PDER2
PDER2
PDER3
PDER3
Fig. 14: Test setup for evaluating DT-based coordinated control in supporting grid frequency regulation
This article has been accepted for publication in IEEE Transactions on Cloud Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TCC.2022.3191837
© 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on July 21,2022 at 09:00:51 UTC from IEEE Xplore.  Restrictions apply. 


---

Page 12

---

TRANSACTIONS ON CLOUD COMPUTING
11
control methods can be inadequate in containing frequency
deviation in future low inertia conditions and how the
DERs with DT-based coordinated control can significantly
improve the frequency regulation performance.
TABLE 1: Description of the parameters in Case 3
Parameters
Description
Value
∆Pset
Change of synchronous genera-
tor’s power set point in p.u.
Variable
FH
Fraction of power generated by
the turbine
0.1
TR
Reheat time constant in seconds
4 s
Km
Mechanical power gain factor
0.95
∆Pm
Change of mechanical power
output in p.u
Variable
∆Pevent
Change of power caused by
events
Variable
Hs
Inertia constant
2 s
R
Droop constant
0.05
D
Damping constant
0.06
fn
Nominal frequency
50 Hz
∆f
Change of grid frequency
Variable
fgrid
Normalized grid frequency
Variable
As shown in Fig. 14, under-frequency events can be
emulated by changing the power imbalance value (∆Pevent)
in the analytical power grid model, which can be used for
representing power grid frequency behaviour during power
imbalance events [45]. The model is used to emulate the
frequency profile during a disturbance. The frequency will
then be applied to the controllable voltage source connected
to the microgrid, acting as a grid emulator. The DER ag-
gregator will monitor the frequency and trigger frequency
response from DERs when the frequency drops below 49.8
Hz. As the aggregated DERs’ active power within a single
microgrid or a distribution network within a certain area
is relatively small compared with the overall grid loading,
in this case study, the total response of all DERs (i.e. PMG)
is scaled up to emulate an scenario, where the proposed
DT-based coordinated control is deployed by many DER
aggregators across the system, to test the effectiveness of
the proposed approach in supporting future grid frequency
regulation when it is rolled out at a large scale. A scaling
factor n is introduced to control the level of scaling of the
frequency response from DERs being controlled. Descrip-
tions of the parameters as presented in Fig. 14 are provided
in Table 1.
5.3.1
Case 3.1: Grid frequency regulation with DT-based
centralized coordinated control (cloud-hosted)
In this test case, a 1000 MW loss of generation is emulated
with 25 GW system loading and an overall system inertia of
50 GVAs. It is assumed that there are five DERs with four
of them representing conventional distributed Synchronous
Generators (SGs) with relatively slow response and one
representing converter-based source (e.g. Battery Energy
Storage System) with a faster response. The scaling factor
for the DERs is set as 100, i.e. assuming there are 100
DER aggregators with same DERs available providing the
ancillary service. Three scenarios are designed to illustrate
the effectiveness of DT-based coordinated control: 1) the
grid only relies on conventional primary frequency response
without support from DERs; 2) DERs purely use their own
inherent controllers to provide support to main grid without
coordinated control; 3) DERs provide support to main grid
with the proposed DT-based coordinated control.
(a)
(b)
Fig. 15: Performance of frequency regulation comparison
with and without DT-based centralized coordinated control
(cloud-hosted): (a) frequency profile; (b) total active power
provided by DERs
(b)
(a)
Fig. 16: Active power outputs of individual DERs: (a) with
DT-based centralized coordinated control; (b) without coor-
dinated control
The test results are shown in Fig. 15 and Fig. 16. In the
case where there is no DERs’ support, the grid frequency
This article has been accepted for publication in IEEE Transactions on Cloud Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TCC.2022.3191837
© 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on July 21,2022 at 09:00:51 UTC from IEEE Xplore.  Restrictions apply. 


---

Page 13

---

TRANSACTIONS ON CLOUD COMPUTING
12
decreases severely to 49.29 Hz. In the second scenario, where
there is DERs support but no DT-based coordinated control
is used, the frequency nadir is improved to 49.48 Hz due
to additional active power from participating DERs. In the
third scenario, where DERs are deployed with the DT-based
coordinated control, the frequency deviation is effectively
contained with a frequency nadir of approximately 49.6 Hz.
The improvement of the frequency is due to the coordinated
actions from DERs with different responding capabilities,
which lead to an overall faster response to contain frequency
deviation as illustrated in Fig. 16.
5.3.2
Case 3.2: Grid frequency regulation with DT-based
distributed coordinated control (edge-hosted)
In this test case, the same test scenario as Case 3.1 is
adopted, but with the edge-hosted DT-based distributed
coordinated control. The test results are presented in Fig.
17 and Fig. 18.
(b)
(a)
Fig. 17: Performance of frequency regulation comparison
with and without DT-based distributed coordinated control:
(a) frequency profile; (b) total active power provided by
DERs
Similar to the observations made in Case 3.1, the coor-
dinated control using DTs hosted at the edge also provide
significant improvement to the frequency regulation per-
formance, where the frequency nadir has been raised from
approximately 49.5 Hz to 49.6 Hz.
5.4
Case Study 4: Robustness against DT synchroniza-
tion errors
In the proposed DT-based coordinated control, synchroniza-
tion between the DERs and their DTs follows two main
principles: 1) discrete event-triggered update, i.e., whenever
there is a power setpoint change in one DER, the synchro-
nization between the DER and its DT needs to be conducted.
This can happen at different time interval depending on
(b)
(a)
Fig. 18: Active power outputs of individual DERs: (a) with
DT-based distributed coordinated control; (b) without coor-
dinated control
(b)
(a)
Fig. 19: Perfromance of the DT-based coordinated control
with different level of estimation errors: (a) cloud-hosted
DTs: centralized approach (b) Edge-hosted DTs: distributed
approach
This article has been accepted for publication in IEEE Transactions on Cloud Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TCC.2022.3191837
© 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on July 21,2022 at 09:00:51 UTC from IEEE Xplore.  Restrictions apply. 


---

Page 14

---

TRANSACTIONS ON CLOUD COMPUTING
13
the energy market conditions driven by the system needs,
but typically the setpoint of DERs will only change when a
settlement period finishes (i.e. every 30 mins); 2) periodic
update, i.e., periodic synchronization to check the DTs’
status and the actual active power output at the DER is also
conducted, typically every minute. This is selected based
on the fact that when a frequency event occurs, typically it
will last over 1 minute, so having 1-minute resolution will
ensure the statuses of the DERs remain updated whenever a
frequency event occurs. In pratice, the periodic synchroniza-
tion can be relaxed to a longer period (e.g. 5 mins) if needed,
as the proposed DT-based coordinated control has a high-
level of tolerance even if there is inconsistency of the DT
estimation and the actual power output occurring between
two synchronization instances, which will be demonstrated
in this case study.
In this test case, errors of 5% to 20% between the DERs’
actual active power outputs and their DTs estimated values
are applied to intentionally introduce the inconsistencies
between DERs and DTs. As shown in Fig. 19, for both of
the grid and edge hosted approaches, the DT-coordinated
control provides most desirable response when there is no
error between the DTs and DERs. With the increase of errors
up to 20%, although the control effectiveness can be slightly
comprised as compared with the case without any error, the
overall performance is still significantly more effective with
faster response and settling time compared with the case
without DT-based coordinated control.
It should be noted that, while the synchronization be-
tween DERs and the DTs do not need to be conducted in real
time, the active power outputs from the DTs are estimated
in real time, which are used as the inputs to the DT-based
coordinated controller to enable the real time control of
DERs to deliver effective frequency control support.
6
DISCUSSIONS
The operation of the future power network with increased
renewable generation and reduced inertia is an imminent
challenge the power industry faces. With the expected pro-
liferation of DERs expected within the network in coming
years, it is increasingly important to reduce the reliance on
communications to realize robust controls that will improve
the resilience of a renewable rich low inertia power system.
Power system controls can be architecturally categorized
as: centralized; decentralized (no communications needed);
and (iii) distributed / hybrid (might still require communi-
cations), which are also discussed within Section 1. In the
paper, the radical change in implementation of centralized
and distributed control solutions through the use of DTs has
been proposed and its effectiveness demonstrated.
•
The use of DTs for implementation of a centralized
control approach effectively eliminates the need for
real-time feedback to be communicated from DERs,
thereby reducing the number of real time communi-
cation links from 2M to M, given there are M DERs
being controlled.
•
The use of DTs for the implementation of a dis-
tributed control eliminates the need for communi-
cations between the DERs, effectively transforming
a distributed control approach to a decentralized
control approach.
•
The use of DTs for decentralized control has not
been explored as they typically do not involve any
communications. However, the use of DTs to further
optimize the performance of decentralized control
approaches can be explored, but remains out of scope
of this paper.
In this paper, the proposed DT-based coordinated control
enables effective coordination of DERs to realise improved
frequency response with significant reduced reliance on
real-time communications, thus providing a promising cost-
effective solution for supporting future frequency regula-
tion. It should be noted that although a frequency control
approach has been demonstrated, the proposed approach
serves as a template for realization of other future central-
ized or distributed control approach.
For utility companies, this brings significant technical
benefits as it will enhance system stability, and also eco-
nomic benefits through the reduced investment required for
communication infrastructure. By enabling more effective
control for DERs, it also provides greater potential for DERs
in providing ancillary services to the grid, which presents
major commercial benefits for DER owners and also DERs
aggregators.
7
CONCLUSIONS
This paper has presented a novel method for realizing
coordinated control of DERs based on cloud and edge-
hosted DTs to optimize the overall aggregated dynamic
response for effectively support frequency regulation in
power grids. The coordinated control of DERs with con-
ventional implementations for both of the centralized and
distributed approaches have been presented and discussed.
It was found that both of the conventional centralized and
distributed approaches present significant reliance on the
real-time communications and the latency of the communi-
cation can severely comprise the overall coordinated control
performance. Through the use of the DTs of DERs, the
real-time status of the DERs can be estimated and used
for supporting coordinated control actions. In the paper,
two DT-based design and implementation approaches for
realizing the coordinated control (corresponding to the two
conventional implementations) have been presented. It has
been demonstrated that the use of DTs of DERs, hosted in
the cloud for the centralized coordinated control, and hosted
in the DERs edge for the distributed coordinated control, can
significantly mitigate the reliance on real-time communica-
tions, while still providing satisfactory control performance.
Therefore, the proposed DT-based coordinated control ap-
proaches represent a promising solution for enabling effec-
tive active power response from DERs to support the future
power grid operation.
REFERENCES
[1]
M.
Jafari,
M.
Korp˚as,
and
A.
Botterud,
“Power
system
decarbonization:
Impacts
of
energy
storage
duration
and
interannual
renewables
variability,”
Renewable
Energy,
vol.
156, pp. 1171–1185, 2020. [Online]. Available: https://www.
sciencedirect.com/science/article/pii/S0960148120306820
This article has been accepted for publication in IEEE Transactions on Cloud Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TCC.2022.3191837
© 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on July 21,2022 at 09:00:51 UTC from IEEE Xplore.  Restrictions apply. 


---

Page 15

---

TRANSACTIONS ON CLOUD COMPUTING
14
[2]
Y. Zhao, S. Xia, J. Zhang, Y. Hu, and M. Wu, “Effect of the digital
transformation of power system on renewable energy utilization
in china,” IEEE Access, vol. 9, pp. 96 201–96 209, 2021.
[3]
G. Fulli, M. Masera, A. Spisto, and S. Vitiello, “A change is com-
ing: How regulation and innovation are reshaping the european
union’s electricity markets,” IEEE Power and Energy Magazine,
vol. 17, no. 1, pp. 53–66, 2019.
[4]
Legislation, “Climate Change Act 2008,” London, 2021. [Online].
Available: https://www.legislation.gov.uk/ukpga/2008/27/data.
pdf
[5]
“Cop26
keeps
1.5c
alive
and
finalises
paris
agree-
ment,”
2021.
[Online].
Available:
https://ukcop26.org/
cop26-keeps-1-5c-alive-and-finalises-paris-agreement/
[6]
Committee
on
Climate
Change,
“Net
Zero:
Technical
Report,”
London,
United
Kingdom,
Tech.
Rep.,
2019.
[Online].
Available:
https://www.theccc.org.uk/publication/
net-zero-technical-report/
[7]
——,
“Net
Zero:
The
UK’s
contribution
to
stopping
global
warming,”
London,
United
Kingdom,
Tech.
Rep.,
2019.
[Online].
Available:
https://www.theccc.org.uk/wp-content/uploads/2019/05/
Net-Zero-The-UKs-contribution-to-stopping-global-warming.
pdf.
[8]
“National
electricity
transmission
system
security
and
quality
of
supply
standard,”
2021.
[Online].
Avail-
able:
https://www.nationalgrideso.com/industry-information/
codes/security-and-quality-supply-standards/code-documents
[9]
R. Dugan and T. McDermott, “Distributed generation,” IEEE In-
dustry Applications Magazine, vol. 8, no. 2, pp. 19–25, 2002.
[10] N. Hosseinzadeh, A. Aziz, A. Mahmud, A. Gargoom, and M. Rab-
bani, “Voltage stability of power systems with renewable-energy
inverter-based generators: A review,” Electronics (Switzerland),
vol. 10, no. 2, pp. 1–27, 2021.
[11] M. A. Uddin Khan, Q. Hong, D. Liu, A. E. Alvarez, A. Dy´sko,
C. Booth, and D. Rostom, “Comparative evaluation of dynamic
performance of a virtual synchronous machine and synchronous
machines,” in The 9th Renewable Power Generation Conference (RPG
Dublin Online 2021), vol. 2021, 2021, pp. 366–371.
[12] G. Pepermans, J. Driesen, D. Haeseldonckx, R. Belmans, and
W.
D’haeseleer,
“Distributed
generation:
definition,
benefits
and
issues,”
Energy
Policy,
vol.
33,
no.
6,
pp.
787–
798, 2005. [Online]. Available: https://www.sciencedirect.com/
science/article/pii/S0301421503003069
[13] P. Dondi, D. Bayoumi, C. Haederli, D. Julian, and M. Suter,
“Network integration of distributed power generation,” Journal of
Power Sources, vol. 106, no. 1, pp. 1–9, 2002, proceedings of the
Seventh Grove Fuel Cell Symposium. [Online]. Available: https://
www.sciencedirect.com/science/article/pii/S037877530101031X
[14] R. Dugan, T. McDermott, and G. Ball, “Distribution planning for
distributed generation,” in 2000 Rural Electric Power Conference.
Papers Presented at the 44th Annual Conference (Cat. No.00CH37071),
2000, pp. C4/1–C4/7.
[15] P. Daly and J. Morrison, “Understanding the potential benefits
of distributed generation on power delivery systems,” in 2001
Rural Electric Power Conference. Papers Presented at the 45th Annual
Conference (Cat. No.01CH37214), 2001, pp. A2/1–A213.
[16] M. A. Uddin Khan, Q. Hong, A. Dy´sko, C. Booth, B. Wang,
and X. Dong, “Evaluation of fault characteristic in microgrids
dominated by inverter-based distributed generators with different
control strategies,” in 2019 IEEE 8th International Conference on
Advanced Power System Automation and Protection (APAP), 2019, pp.
846–849.
[17] M. A. U. Khan, Q. Hong, A. Dy´sko, and C. Booth, “An active
protection scheme for islanded microgrids,” in 15th International
Conference on Developments in Power System Protection (DPSP 2020),
2020, pp. 1–6.
[18] Q. Hong, M. Karimi, M. Sun, S. Norris, O. Bagleybter, D. Wilson,
I. F. Abdulhadi, V. Terzija, B. Marshall, and C. D. Booth, “Design
and validation of a wide area monitoring and control system for
fast frequency response,” IEEE Transactions on Smart Grid, vol. 11,
no. 4, pp. 3394–3404, 2020.
[19] M. D. Galus, S. Koch, and G. Andersson, “Provision of load
frequency control by phevs, controllable loads, and a cogeneration
unit,” IEEE Transactions on Industrial Electronics, vol. 58, no. 10, pp.
4568–4582, 2011.
[20] N. Bazmohammadi, A. Madary, J. C. Vasquez, H. B. Mohammadi,
B. Khan, Y. Wu, and J. M. Guerrero, “Microgrid digital twins:
Concepts, applications, and future trends,” IEEE Access, vol. 10,
pp. 2284–2302, 2022.
[21] M. Di Nardo, “Developing a conceptual framework model of
industry 4.0 for industrial management,” Industrial Engineering
Management Systems, vol. 19, no. 3, pp. 551–560, 2020.
[22] M. Grieves, “Digital Twin: Manufacturing Excellence through
Virtual
Factory
Replication,”
2014.
[Online].
Available:
https://theengineer.markallengroup.com/production/content/
uploads/2014/12/Digital Twin White Paper Dr Grieves.pdf
[23] B. Hicks, “Industry 4.0 and digital twins: Key lessons from
nasa,” 2021. [Online]. Available: https://www.thefuturefactory.
com/blog/24
[24] C. Brosinsky, D. Westermann, and R. Krebs, “Recent and prospec-
tive developments in power system control centers: Adapting the
digital twin technology for application in power system control
centers,” 2018 IEEE International Energy Conference (ENERGYCON),
pp. 1–6, 2018.
[25] K. Mukesh, K. Trond, and J. Kjetil, Andr´e, “Simple a posteriori
error estimators in adaptive isogeometric analysis,” Computers &
Mathematics with Applications, vol. 70, pp. 1555–1582, 2015.
[26] R. Rocchetta, L. Bellani, M. Compare, E. Zio, and E. Patelli,
“A reinforcement learning framework for optimal operation and
maintenance of power grids,” Applied Energy, vol. 241, pp. 291–
301, 2019.
[27] H. Darvishi, D. Ciuonzo, E. R. Eide, and P. S. Rossi, “Sensor-
fault detection, isolation and accommodation for digital twins via
modular data-driven architecture,” IEEE Sensors Journal, vol. 21,
no. 4, pp. 4827–4838, 2021.
[28] Y. Xu, Y. Sun, X. Liu, and Y. Zheng, “A digital-twin-assisted fault
diagnosis using deep transfer learning,” IEEE Access, vol. 7, pp.
19 990–19 999, 2019.
[29] E. J. Tuegel, A. R. Ingraffea, T. G. Eason, and S. M. Spottswood,
“Reengineering aircraft structural life prediction using a digital
twin,” International Journal of Aerospace Engineering, vol. 2011, no.
154798, 2011.
[30] L. Shimin, B. Jinsong, L. Yuqian, L. Jie, L. Shanyu, and S. Xuemin,
“Digital twin modeling method based on biomimicry for machin-
ing aerospace components, journal of manufacturing systems,”
Journal of Manufacturing Systems, vol. 58, pp. 0278–6125, 2021.
[31] Q. Qi and F. Tao, “Digital twin and big data towards smart
manufacturing and industry 4.0: 360 degree comparison,” IEEE
Access, vol. 6, pp. 3585–3593, 2018.
[32] B. Besselink, V. Turri, S. H. van de Hoef, K.-Y. Liang, A. Alam,
J. M˚artensson, and K. H. Johansson, “Cyber–physical control of
road freight transport,” Proceedings of the IEEE, vol. 104, no. 5, pp.
1128–1141, 2016.
[33] Y. Liu, L. Zhang, Y. Yang, L. Zhou, L. Ren, F. Wang, R. Liu, Z. Pang,
and M. J. Deen, “A novel cloud-based framework for the elderly
healthcare services using digital twin,” IEEE Access, vol. 7, pp.
49 088–49 101, 2019.
[34] P. F. Borowski, “Digitization, digital twins, blockchain, and indus-
try 4.0 as elements of management process in enterprises in the
energy sector,” Energies, vol. 7, no. 14, p. 1885, 2021.
[35] P.
Apte,
“Digital
twins
of
nuclear
power
plants,”
2021.
[Online].
Available:
https://www.asme.org/topics-resources/
content/digital-twins-of-nuclear-power-plants
[36] T. R. Wanasinghe, L. Wroblewski, B. K. Petersen, R. G. Gosine,
L. A. James, O. De Silva, G. K. I. Mann, and P. J. Warrian, “Digital
twin for the oil and gas industry: Overview, research trends,
opportunities, and challenges,” IEEE Access, vol. 8, pp. 104 175–
104 197, 2020.
[37] P. Jain, J. Poon, J. P. Singh, C. Spanos, S. R. Sanders, and S. K.
Panda, “A digital twin approach for fault diagnosis in distributed
photovoltaic systems,” IEEE Transactions on Power Electronics,
vol. 35, no. 1, pp. 940–956, 2020.
[38] M. Milton, O. Castulo De La, H. L. Ginn, and A. Benigni,
“Controller-embeddable probabilistic real-time digital twins for
power electronic converter diagnostics,” IEEE Transactions on
Power Electronics, vol. 35, no. 9, pp. 9850–9864, 2020.
[39] M. Zhou, J. Yan, and D. Feng, “Digital twin framework and its
application to power grid online analysis,” CSEE Journal of Power
and Energy Systems, vol. 5, no. 3, pp. 391–398, 2019.
[40] A. Khaled, S. Maarouf, M. Hasan, A. Dalal, and L. Serge, “Devel-
opment of new identification method for global group of controls
for online coordinated voltage control in active distribution net-
works,” IEEE Transactions on Smart Grid, vol. 11, no. 5, pp. 3921–
3931, 2020.
This article has been accepted for publication in IEEE Transactions on Cloud Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TCC.2022.3191837
© 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on July 21,2022 at 09:00:51 UTC from IEEE Xplore.  Restrictions apply. 


---

Page 16

---

TRANSACTIONS ON CLOUD COMPUTING
15
[41] D. Chunxia, Y. Dong, G. Josep M., X. Xiangpeng, and H. Songlin,
“Multiagent system-based distributed coordinated control for ra-
dial dc microgrid considering transmission time delays,” IEEE
Transactions on Smart Grid, vol. 8, no. 5, pp. 2370–2381, 2017.
[42] S. Papathanassiou et al., “Multi-port DC microgrids: Online pa-
rameter adaptation in model predictive control,” in CIGR´e Symp.
‘Power systems with Dispersed Generation: Technologies, Impacts on
Development, Operation and Performances, Athens, Greece, Apr.
2005.
[43] M. Maniatopoulos et al., “Combined control and power hardware
in-the-loop simulation for testing smart grid control algorithms,”
IET Generation, Transmission Distribution, pp. 3009–3018, 2017.
[44] J. Nsengiyaremye, B. C. Pal, and M. M. Begovic, “Microgrid pro-
tection using low-cost communication systems,” IEEE Transactions
on Power Delivery, vol. 35, no. 4, pp. 2011–2020, 2020.
[45] Q. Hong, M. Nedd, S. Norris, I. Abdulhadi, M. Karimi, V. Terzija,
B. Marshall, K. Bell, and C. Booth, “Fast frequency response for
effective frequency control in power systems with low inertia,”
The Journal of Engineering, vol. 2019, pp. 1696–1702, 2019.
Jiaxuan Han Jiaxuan Han received the B.Eng.
(Hons) degree from both University of Strath-
clyde, Glasgow, U.K. and North China Electric
Power University, Baoding, China in 2020. He
is currently pursuing the Ph.D. degree in Elec-
tronic and Electrical Engineering at Universit of
Strathclyde. His research interest is on the digital
twin technology and its application to support
frequency control in future power systems
Qiteng Hong (S’11-M’15-SM’22) is currently a
Senior Lecturer (Associate Professor) at the Uni-
versity of Strathclyde, Glasgow, U.K. His main
research interest is on power system protection
and control in future networks with high pene-
tration of renewables. He received his B.Eng.
(Hons) and Ph.D. degree in Electronic and Elec-
trical Engineering in 2011 and 2015 respectively,
both from the University of Strathclyde. Dr Hong
is a member of IEEE Working Group P2004 and
IEEE Task force on Cloud-Based Control and
Co-Simulation of Multi-Party Resources in Energy Internet, and he also
was a Regular Member of the completed CIGRE WG B5.50.
Mazheruddin Syed (S’11-M’18) received his BE
degree in Electrical and Electronics Engineering
from Osmania University, India, in 2011, MSc de-
gree in Electrical Power Engineering from Mas-
dar Institute of Science and Technology, UAE, in
2013 and PhD degree in Electronic and Electri-
cal Engineering from University of Strathclyde,
Scotland in 2018. He is currently a Strathclyde
Chancellor’s Fellow (Lecturer) with the Institute
for Energy and Environment in the Department
of Electronic and Electrical Engineering at the
University of Strathclyde. He also serves as the manager for the Dy-
namic Power Systems Laboratory at Strathclyde. He leads the Interna-
tional Energy Agency (IEA) ISGAN SIRFN Advanced Laboratory Testing
Methods Working Group and is the Secretary of IEEE Task Force on
Control of Distributed Resources in Energy Internet. He has lead and
contributed to innovative National, European and Industrial power sys-
tem research projects with a strong publication record of over 59 peer-
reviewed scientific papers. His research interests include demand side
management, decentralized and distributed control, real-time controller
and power hardware in the loop simulations, geographically distributed
simulations and systems level validations.
Md Asif Uddin Khan is a PhD student at the De-
partment of Electronic and Electrical Engineer-
ing at the University of Strathclyde, Glasgow,
UK. His research area focused on power system
protection, stability, fault analysis and control of
inverter-interfaced renewable resources. Before
he started his PhD in January 2019, he was
also associated with the Department of Electrical
and Electronic Engineering of BRAC University,
Dhaka, Bangladesh as a Lecturer from Septem-
ber 2015. Md Asif Uddin Khan received his MSc
degree in Electronic and Electrical Engineering from the University of
Strathclyde (2017) and the BSc degree in Electrical and Electronic
Engineering from BRAC University (2015).
Guangya Yang (Senior Member IEEE) is cur-
rently senior researcher with Department of wind
and energy systems at the Technical University
of Denmark (DTU). He obtained PhD in 2008
and since then is affiliated with DTU. In between
he has also been working full time with Ørsted on
electrical system design of large offshore wind
farms. His research is in the field of operation
and control of power systems including devel-
opment and utilization of new digital solutions.
He has been principal investigator of numerous
research projects both at national and EU level. Besides, he is an active
member in IEC TC88 “Wind power generation Systems” with the focus
on connectivity of offshore wind turbines and wind power plants. He has
been editorial board member of several PES transactions and currently
leads the editorial board of the IEEE Access Power and Energy Society
Section.
Graeme M. Burt (M’95) received the B.Eng. de-
gree in electrical and electronic engineering, and
the Ph.D. degree in fault diagnostics in power
system networks from the University of Strath-
clyde, Glasgow, U.K., in 1988 and 1992, respec-
tively. He is currently a Professor of electrical
power systems at the University of Strathclyde
where he co -directs the Institute for Energy and
Environment, directs the Rolls -Royce University
Technology Centre in Electrical Power Systems,
and is lead academic for the Power Networks
Demonstration Centre (PNDC). In addition, he serves as spokesperson
for the board of DERlab e.V., the association of distributed energy
laboratories. His research interests include the areas of power system
protection and control, distributed energy, and experimental validation.
Campbell D. Booth received the B.Eng. and
Ph.D. degrees in electrical and electronic engi-
neering from the University of Strathclyde, Glas-
gow, U.K., in 1991 and 1996, respectively. He
is currently a Professor and the Head of the
Department for Electronic and Electrical Engi-
neering, University of Strathclyde. His research
interests include power system protection; plant
condition monitoring and intelligent asset man-
agement; applications of intelligent system tech-
niques to power system monitoring, protection,
and control; knowledge management; and decision support systems.
This article has been accepted for publication in IEEE Transactions on Cloud Computing. This is the author's version which has not been fully edited and 
content may change prior to final publication. Citation information: DOI 10.1109/TCC.2022.3191837
© 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: Danmarks Tekniske Informationscenter. Downloaded on July 21,2022 at 09:00:51 UTC from IEEE Xplore.  Restrictions apply. 
