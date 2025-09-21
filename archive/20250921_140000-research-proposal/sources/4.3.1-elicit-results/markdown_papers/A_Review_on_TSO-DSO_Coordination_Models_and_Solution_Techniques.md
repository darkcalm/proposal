

---

Page 1

---

The University of Manchester Research
A Review on TSO-DSO Coordination Models and Solution
Techniques
DOI:
10.1016/j.epsr.2020.106659
Document Version
Accepted author manuscript
Link to publication record in Manchester Research Explorer
Citation for published version (APA):
Givisiez, A. G., Petrou, K., & Ochoa, L. F. (2020). A Review on TSO-DSO Coordination Models and Solution
Techniques. Electric Power Systems Research, 189, 106659. Advance online publication.
https://doi.org/10.1016/j.epsr.2020.106659
Published in:
Electric Power Systems Research
Citing this paper
Please note that where the full-text provided on Manchester Research Explorer is the Author Accepted Manuscript
or Proof version this may differ from the final Published version. If citing, it is advised that you check and use the
publisher's definitive version.
General rights
Copyright and moral rights for the publications made accessible in the Research Explorer are retained by the
authors and/or other copyright owners and it is a condition of accessing publications that users recognise and
abide by the legal requirements associated with these rights.
Takedown policy
If you believe that this document breaches copyright please refer to the University of Manchester’s Takedown
Procedures [http://man.ac.uk/04Y6Bo] or contact openresearch@manchester.ac.uk providing relevant details, so
we can investigate your claim.
Download date:03. Jun. 2025


---

Page 2

---

21st Power Systems Computation Conference
 
 
Porto, Portugal — June 29 – July 3, 2020 
 
             PSCC 2020 
A Review on TSO-DSO Coordination Models 
 and Solution Techniques 
Arthur Gonçalves Givisiez1, Kyriacos Petrou1, Luis F. Ochoa1,2 
1 The University of Melbourne, Melbourne, Australia 
2 The University of Manchester, Manchester, United Kingdom 
arthurgivisiez@ieee.org; k.petrou@ieee.org; luis_ochoa@ieee.org 
 
 
Abstract—The volume of services procured by transmission sys-
tem operators (TSOs) through distribution-connected resources, 
aka distributed energy resources (DER), has been increasing in 
recent years. Currently, distribution networks are assumed to be 
fully capable of dealing with the resulting power flows. Howev-
er, this assumption will no longer be valid as the volume of DER 
services become significant. Therefore, distribution system op-
erators (DSOs) need to have a more active role to ensure the 
integrity of the distribution network while facilitating DER ser-
vices. To achieve this, adequate coordination between TSOs and 
DSOs is required. To help stakeholders understand the implica-
tions of different coordination models so they can be adopted or 
tailored to their needs, this paper identifies three core TSO-DSO 
coordination models from the many proposed in the literature, 
discussing the corresponding advantages, disadvantages and 
challenges. Furthermore, a mapping of the proposed solution 
techniques is carried out to identify research trends and gaps. 
Index Terms--Active distribution networks, Distributed Energy 
Resources (DER) Services, Distribution System Operator (DSO), 
TSO-DSO coordination models, TSO-DSO interaction. 
I.INTRODUCTION 
More and more, services procured by transmission system 
operators (TSOs) are being provided through distributed ener-
gy resources (DER), typically connected to medium (MV) and 
even low voltage (LV) distribution networks. Due to the rela-
tive scarcity of DER today, this procurement is done with the 
assumption that distribution networks are fully capable of 
dealing with the resulting time-varying power flows. In par-
ticular, given the rising adoption of photovoltaic (PV) and 
battery energy storage (BES) systems which offer significant 
controllability, the level of services that can be provided by 
consumers that also produce electricity (also known as 
prosumers) is rapidly increasing.  
In distribution networks, large penetrations of DER alone 
can cause technical problems and challenges due to reverse 
power flows, such as network assets congestion [1] and volt-
age excursions [2, 3]. These issues, as demonstrated in [4] can 
be further exacerbated when controllable DER such as BES 
systems participate in the provision of services. In some coun-
tries, like Australia, firm limits on DER exports are being im-
posed to help to deal with these issues. While this could be a 
viable intermediate solution that allows DER participating in 
the provision of services and satisfying network constraints, 
such traditional fit-and-forget approaches could also prove to 
be too prohibitive in the provision of services, effectively lim-
iting the attractiveness of DER providing services through 
distribution networks. 
As documented by reports released by organizations 
around the world in the last few years [1, 5-10], an alternative 
for countries/regions with open markets, is for distribution 
companies to have an active role in managing DER services 
(e.g., energy for balancing purposes, ancillary services, de-
mand response, etc. – provided directly by prosumers or via 
aggregators) whilst also incorporating network constraints. 
This new role is commonly associated with the term Distribu-
tion System Operator (DSO) and has as objective the efficient 
facilitation of DER services by making the most of the exist-
ing infrastructure without compromising distribution network 
integrity [11-14]. The concept of having a DSO to manage 
DER services is similar to that of transactive energy [15]. 
Given that DSOs will inherently affect the way DER ser-
vices will be provided, this new environment requires a para-
digm shift in the way transmission and distribution interact. 
Consequently, having an adequate TSO-DSO coordination 
becomes crucial to ensure not only that the DSO role is ful-
filled, but also the efficient operation of the power system.  
To help stakeholders understand the implications of differ-
ent coordination models so they can be adopted or tailored to 
their needs, this review paper identifies three core TSO-DSO 
coordination models from the many proposed in the literature, 
discussing the corresponding advantages, disadvantages and 
challenges. 
In addition, solution techniques used to assess and solve 
network issues in each of the identified three TSO-DSO core 
models are mapped. These are classified regarding different 
types of optimization algorithms and their corresponding for-
mulation. For completeness, information related to case stud-
ies are also presented, e.g., network information (e.g., MV, 
This study was financed in part by the Coordenação de Aperfeiçoamento de 
Pessoal de Nível Superior – Brasil (CAPES) – Finance Code 001, and The 
University of Melbourne. 


---

Page 3

---

21st Power Systems Computation Conference
 
   
 
Porto, Portugal — June 29 – July 3, 2020 
 
   PSCC 2020 
 
Figure. 1. TSO-managed model 
 
Figure. 2. TSO-DSO hybrid-managed model 
 
Figure. 3. DSO-managed model 
LV, transmission) and DER types and sizes. This mapping is 
important to identify promising techniques and their limita-
tions, so they can be further investigated and improved. 
This paper is structured as follows. In Section II, the TSO-
DSO coordination is discussed, and the three identified mod-
els are presented and discussed in terms of their advantages, 
disadvantages and challenges. In Section III, the solution 
techniques used to assess and solve network issues in each of 
the identified models are mapped and discussed. Finally, the 
conclusions are presented in Section IV. 
II. TSO-DSO COORDINATION MODELS 
At the core of any TSO-DSO coordination model, in open 
market environments, is the consideration of distribution net-
work constraints to facilitate and ensure the effective provi-
sion of DER services to the TSO. By catering for voltage and 
thermal limits (and any other potential limits, e.g., N-1 securi-
ty, fault levels, etc.), it will be possible to validate services 
bids made by DER, i.e., to define which (or to what extent) 
services can be allowed without affecting the integrity of the 
distribution network at a given time. It is worth highlighting 
that in the mid-term, it is likely that all services will be ulti-
mately needed and used by the TSO, i.e., there is only one 
central market for wholesale and ancillary services, as it is the 
case today around the world. However, in the future, certain 
TSO-DSO coordination models will also have to cater for 
distribution-level markets. 
For clarity, it is important to highlight that the term “DER 
bids validation” is used here to refer to a process where DER 
bids (from prosumers and/or aggregators) are validated con-
sidering distribution network constraints. Depending on who 
carries out this task, this validation might be embedded in oth-
er processes. For instance, as it will be explained in the TSO-
managed model (Section II-A), the TSO could do this within 
its dispatch processes. Although the term “DER bids valida-
tion” is not usual, it allows clarifying this new process that 
will be required in all the TSO-DSO coordination models. 
On one hand, the validation of DER services will allow a 
much higher certainty of the feasible volumes, which, in turn, 
allows the TSO to increase its reliance on DER, potentially 
reducing cost for the whole system. On the other hand, the 
adoption of any coordination model can increase both capital 
and operational expenditure of the distribution network. First, 
investments are required to increase network visibility and 
controllability, which at the initial stages will require signifi-
cant investments. From a network asset perspective, costs are 
expected to increase due to quicker deterioration; result of the 
more effective utilization of the assets (i.e., lines and trans-
formers operating closer to their physical limits for longer 
periods). Furthermore, the new active operation of the net-
works is likely to bring added operational costs. 
There are also several socio-techno-economic challenges 
that need to be considered. The most prominent is the in-
creased complexity of system operation and dispatch, due to a 
large number of DER and controllable network assets (e.g., 
on-load tap changers (OLTC), capacitor banks, etc.) to be or-
chestrated. Furthermore, adequate coordination relies on accu-
rate network information, but as it currently stands, there is 
limited observability on distribution networks; especially on 
the LV level. The equitable use of the network is also an inter-
esting challenge as determining the extent to which each DER 
can provide services should also consider some form of fair-
ness. Increased access to network information makes cyber-
security even more important as now the system becomes 
more vulnerable to cyberattacks. Additionally, new policies 
and regulations need to be introduced to allow and facilitate 
for the transition towards TSO-DSO coordination models. 
Although all TSO-DSO coordination model will share the 
aspects discussed above, the specifics of each model will bring 
advantages, disadvantages and challenges of their own. None-
theless, most models available in the literature tend to be tai-
lored to the needs of the individual power system/organization 
that proposed them; making it difficult to establish compari-
sons. Thus, the identification of core models (i.e., not specific 
to a given market structure/regulatory framework) is important 
as it enables researchers and industry alike to understand the 
advantages, disadvantages, and applicability of each model.  
Accordingly, three core TSO-DSO coordination models 
are identified. In the first model, referred to as the TSO-
managed model, the TSO performs the economic dispatch of 
transmission energy resources (TER, conventional bulk gener-


---

Page 4

---

21st Power Systems Computation Conference
 
   
 
Porto, Portugal — June 29 – July 3, 2020 
 
   PSCC 2020 
ation) and DER considering network constraints for both the 
distribution and transmission networks. In the second model, 
referred to as the TSO-DSO hybrid-managed model, the TSO 
performs the economic dispatch of TER and DER once the 
DSO has validated services bids made by DER to the central 
market. In the third model, referred to as the DSO-managed 
model, the DSO is responsible for validating, dispatching (in 
the presence of distribution-level markets) and aggregating all 
DER services. In the following subsections, these three mod-
els are presented and discussed in detail. 
A. TSO-Managed Model 
With this model, the TSO is responsible for the DER and 
TER dispatch [16-19] (i.e., a fully centralised dispatch) while 
accounting for both transmission and distribution networks 
constraints [20-22]. Depending on the energy market design, 
an independent market operator could also be the entity re-
sponsible for this task (e.g., Australian Energy Market Opera-
tor, AEMO, in Australia). Regardless of who performs the 
centralised dispatch, it must be clear that with this model one 
central entity [20-28] will be responsible for the whole system 
dispatch, and it has to ensure that both networks (i.e., trans-
mission and distribution) will not have problems due to dis-
patch decisions.  
The DSO’s primary responsibilities (with regards to the 
coordination) is to provide distribution network real-time op-
erational data to the TSO. Besides that, the DSO functions are 
limited to operating the distribution network, make invest-
ments and perform network maintenance [20]. Therefore, the 
TSO-DSO interaction is limited to the exchange of the real-
time (or close to real-time) state of the distribution network 
participants (demand, generation, etc.) and assets (voltages, 
power flows, etc.). 
Based on the above, the following sequence describes the 
core coordination process for a given service period (aka set-
tlement or market clearance period). This is shown in Fig. 1. 
1. DER send their bids directly to the TSO for a given 
service period (1a). The TSO also receives real-time 
operational data from the DSO (1b). 
2. The TSO performs a centralised validation of DER 
services bids (2a) and computes the dispatch of TER 
and DER. The corresponding dispatch commands are 
sent to DER (2b). 
In this model, the controllability of DER is technology in-
dependent. Since the DER bids are based on the prosumers’ 
power injections (or absorptions), the TSO has only to model 
the injected/absorbed powers, i.e., the detailed modelling of 
the workings of DER by the TSO is not necessary. Of course, 
since the control of DER is done by an aggregator or the 
prosumer, it will be them doing the required detailed model-
ling. Finally, in this model, since all DER services are directed 
to the TSO, the simultaneous use of DER services by the TSO 
and DSO cannot occur. 
1) Advantages: As a central entity, it is responsible for the 
whole system decision processes, simplifying the TSO-DSO 
coordination process. The adoption of new standards can be 
done in a faster and more straightforward way. Furthermore, 
as the TSO has know-how on dispatch processes, it can ex-
pand existing platforms. Finally, as the TSO is not the owner 
of the distribution assets, it is possible to make the most of it 
without any conflict of interest. 
2) Disadvantages and Challenges: Since the DSO does 
not validate or dispatch DER, there is a risk of less efficient 
facilitation of services. In cases where the TSO is not able to 
control (directly or indirectly) DSO assets, there will be a less 
effective orchestration, reducing potential DER services. Vali-
dating and dispatching both the transmission and all distribu-
tion networks at once creates enormous computational and 
modelling challenges. Furthermore, as DER penetration in-
creases, it becomes more difficult to coordinate the system in a 
fully centralised manner. Also, the volumes of real-time op-
erational data to be transferred from the DSOs to the TSO can 
be significant. Finally, the TSO will have to interpret distribu-
tion network requirements, which is an area that the TSO does 
not have know-how. Table I summarizes the discussed points. 
B. TSO-DSO Hybrid-Managed Model 
In this model, seen in Fig. 2, the TSO is responsible for the 
DER and TER dispatch (i.e., a centralised dispatch), but it 
does not consider any distribution network aspect. The DSO is 
the entity responsible for validating DER services bids to 
guarantee network integrity. Accordingly, the process of vali-
dation starts with the visibility of the bids as proposed in [1, 5, 
7, 9, 12, 13, 17, 20, 29-31]. Once the bids are validated, this 
information can be sent to either the TSO or directly to DER, 
or even both at the same time. There is also the possibility of 
the DSO performing the validation before bids are sent to the 
TSO [28, 31-33], i.e., a pre-validation where DER send all 
bids first to the DSO who validates them so DER can directly 
send validated bids to the TSO. 
Furthermore, the literature suggests that the DSO could al-
so use DER services by procuring flexibility from the central 
market for distribution-related purposes such as mitigating 
distribution networks issues (operation) or even for investment 
deferral (planning) [5, 6, 8, 13, 17-19, 22, 29, 31]. 
Based on the aforementioned, the following sequence de-
scribes the core coordination process of this model. 
1. DER send their bids directly to the TSO for a given 
service period.  
2. The DSO is informed about the bids. 
3. The DSO performs the validation of DER services 
bids (3a). Then, it transmits the validated bids and re-
quests to the TSO (3b-red) and/or to DER (3b-blue). 
4. The TSO performs the dispatch and sends the dispatch 
command to DER (4). 
In this model, the controllability of DER is also technology 
independent for the TSO-DSO coordination, and it follows the 
same logic presented for the previous model. Furthermore, 


---

Page 5

---

21st Power Systems Computation Conference
 
   
 
Porto, Portugal — June 29 – July 3, 2020 
 
   PSCC 2020 
given that DER services are offered on the central market, 
both the TSO and DSO could decide to use it (if a specific 
market design allows it). Therefore, a priority has to be estab-
lished (e.g., first the TSO, first the DSO, or based on the tech-
nical or economic criticality of the service). To establish this 
priority, it is important to also consider the type of the offered 
DER services, as it may be more useful to the DSO (e.g., ser-
vices for local voltage problems or congestion) or to the TSO 
(e.g., energy balancing). 
1) Advantages: As the DSO validates all DER bids, the 
know-how on network operation creates the opportunity to 
manage controllable assets in a way that facilitates more DER 
services compared to the TSO-managed model (and the TSO 
does not manage distribution network controllable assets). 
The computational and modelling requirements are reduced 
compared to the TSO-managed model as the assessment is 
restricted to the area of the DSO. The need for the DSO to 
transfer operational data to the TSO is also eliminated. 
2) Disadvantages and Challenges: Since the DSO owns 
network assets and the facilitation of services requires using 
assets closer to their limits, the DSO might not push them as 
close to the limits as it could because this can reduce their 
lifetime. So, there is a possible conflict of interest for the 
DSO while managing network assets and validating DER 
services bids. Although the scale of the distribution networks 
managed by a single DSO cannot be compared with the 
whole power system (both transmission and all distribution 
networks together), there are still significant computational 
and modelling challenges. Furthermore, the coordination be-
tween TSO and DSO becomes more complex as the decision 
processes are not centralised in one entity. 
C. DSO-Managed Model 
This model can be interpreted as twofold, when there is no 
distribution-level market, and when such marketplace is pre-
sent. When there is no distribution-level market, the TSO is 
responsible for TER and aggregated DER dispatch, however, 
the latter is done indirectly via the DSO. The DSO acts as the 
central coordinator of DER [1, 5, 7, 9, 14, 16, 17, 20, 21, 23-
26, 28, 34-42], validating bids and providing them to the TSO 
as an aggregated volume of services [1, 7, 9, 20, 21, 41]. An 
aggregated dispatch command is sent by the TSO to the DSO 
who then dispatches individual DER to match the require-
ment. 
Based on the above, the following sequence describes the 
core coordination process without the presence of distribution-
level markets, which is shown in Fig. 3. 
1. DER send their bids to the DSO for a given service 
period. 
2. The DSO performs validation of DER services bids 
and aggregates them (2a). Aggregated bids are sub-
mitted to the TSO (2b). 
3. The TSO performs the dispatch and sends the aggre-
gated dispatch command to the DSO. 
4. The DSO sends the dispatch command to DER to 
match the aggregated requirement. 
In this case, the controllability of DER depends on whether 
the DSO is the aggregator or not. If it is not, then it follows the 
same logic presented for the previous models. However, if the 
DSO is in fact the aggregator, then, the detailed modelling of 
DER needs to be done by the DSO in combination with the 
distribution network constraints. The complexity of DER 
modelling will depend on the technology (e.g., if only PV sys-
tem is controlled, the modelling might not need to consider 
time aspects, but if there is a battery system, time aspects may 
be important). Furthermore, the core coordination process 
described before will start from a modified step 2, in which 
the DSO does not validate DER service bids but create/decide 
DER service bids and aggregate them (2a). 
Furthermore, the transmission-distribution separation cre-
ated by the DSO-managed model allows the creation of distri-
bution-level markets where only DER participate. Two main 
schemes have been proposed in the literature: 
i. 
The distribution-level market is cleared before DER 
bids are sent to the TSO market [5, 16-20, 43]. For 
this scheme, only steps 2 and 4 are modified. In step 
2, the DSO performs the validation of DER services 
and makes the distribution-level market clearance. 
The remaining DER services bids are aggregated (2a). 
In step 4, both DSO and TSO send dispatch com-
mands. 
ii. 
The TSO sets requirements (or targets) at the TSO-
DSO interface. The DSO is responsible for operating 
the distribution-level market (and corresponding DER 
bids) to achieve the TSO requirement whilst ensuring 
distribution network integrity [16-19, 42, 43]. For this 
scheme, only step 4 is modified. The DSO clears the 
distribution-level market and sends dispatch com-
mands to DER to match the TSO’s target. 
Finally, in this model, the simultaneous use of DER ser-
vices by the DSO and TSO is naturally solved when the DSO 
dispatches the distribution-level market before submitting the 
reminder bids to the TSO. However, in the case when the 
DSO has to follow the target set by the TSO, a priority process 
similar to the one discussed for the previous model should be 
considered. 
1) Advantages: This model has the potential to achieve 
the highest level of efficiency on the orchestration of distribu-
tion network controllable assets and DER dispatch. If the 
TSO decides to request (dispatch) less than the available DER 
services, there is an opportunity for a re-optimization of the 
distribution network assets (e.g., reducing unnecessary con-
trol actions) because that information is processed by the 
DSO before sending the dispatch to DER. Similar to the pre-
vious model, the DSO leverages its know-how on distribution 


---

Page 6

---

21st Power Systems Computation Conference
 
   
 
Porto, Portugal — June 29 – July 3, 2020 
 
   PSCC 2020 
networks operation and there is no exchanges of distribution 
network operational data with the TSO. 
2) Disadvantages and Challenges: A possible conflict of 
interest for the DSO when managing network assets and vali-
dating DER services bids also appears on this model. While 
the computational and modelling challenges of validating 
DER bids are similar to the previous model, the incorporation 
of distribution-level markets can add complexity which is 
aggravated by the lack of experience of the DSO on such 
processes (e.g., market design, market clearance, etc.). 
The challenge of potential conflict of interest for the DSO, 
can be solved with an independent DSO (iDSO) [1, 7, 9, 20]. 
As the iDSO is a third-party entity, it can be neutral and trans-
parent when managing network assets and DER. In this spe-
cial case, the iDSO manages distribution network and/or mar-
kets, but it does not own network assets. In this case, there is 
still the existence of a traditional DSO which is responsible for 
making investments and maintaining the network in opera-
tional conditions, but also exchanges network status with the 
iDSO in real-time to allow the iDSO to operate the network. 
However, independent entities would need to be created in 
each distribution network area. Consequently, more complexi-
ty would be added to the system operation, as the iDSO would 
have to exchange real-time network status with the DSO, and 
simultaneously, exchange market information with the TSO. 
Also, the cost of creating new entities in the system could un-
dermine the benefits brought by iDSOs. Thus, an alternative to 
the iDSO model would be to keep the original DSO-managed 
model but imposing strong neutrality rules or providing regu-
lation incentives to the DSO. The same can be applied to the 
TSO-DSO hybrid-managed model as it has similar challenges. 
III. SOLUTION TECHNIQUES 
As each of the identified TSO-DSO coordination models 
differs in the way that coordination is performed, solution 
techniques that apply to one might not necessarily apply to 
another, or at least has to be tailored accordingly. In order to 
accelerate research and innovation in the field, this section 
first identifies solution techniques and then maps them to each 
applicable model. A summary of solution techniques and sim-
ulation considerations for each model is presented in Table II  
Although there are techniques based on rules using itera-
tive power flows, the most common are based on optimiza-
tion, in particular, using the optimal power flow (OPF). The 
latter are implemented using different optimization algorithms 
which can be classified as follows: 
Distributed Optimization. An originally large-scale prob-
lem is decoupled in smaller problems (named subproblems, 
which are neighbours). For a given decoupled point, original 
variables (e.g., voltage, power) are duplicated, one for each 
neighbouring subproblem. This allows each subproblem to 
perform “local” decisions but maintaining some communica-
tion between neighbouring subproblems. In the end, neigh-
bouring subproblems must match their decoupled variables, 
which in reality represents the same variable. 
Hierarchical Optimization. An originally large-scale 
problem is divided in subproblems, which are organised in a 
hierarchical structure. Each subproblem performs local deci-
sions and communicates them to the next hierarchical level. 
Centralized Optimization. The large-scale problem is 
solved as a single problem. 
Although the above optimization algorithms are applicable 
to all the TSO-DSO coordination models, the centralized op-
timization algorithm is commonly adopted by works investi-
gating the TSO-managed model [22-28]. The corresponding 
problems were formulated using single-phase AC OPF for 
MV distribution networks [22-26, 28], while DC OPF was 
used for transmission networks [22-24, 28]. The exception is 
[27], which used AC OPF for transmission and data-driven 
aggregation of feasible regions for distribution networks. 
In the TSO-DSO hybrid-managed model, the system 
dispatch is under the TSO responsibility and the validation of 
DER services bids is done by the DSO. In [28], validated bids 
are assumed to be given to the TSO, i.e., no actual validation 
process is considered. A centralised DC OPF is used to solve 
the dispatch problem. In [31, 32], only validation aspects are 
investigated, i.e., the TSO dispatch is not considered. An 
TABLE I. TSO-DSO COORDINATION MODELS CHARACTERISTICS 
 
TSO-Managed Model 
TSO-DSO Hybrid-Managed Model 
DSO-Managed Model 
Advantages 
• Simplifies the TSO-DSO coordination process 
• TSO know-how on dispatch 
• TSO has no conflict of interest when pushing 
distribution network assets to the limits 
• Likely to have a more efficient facili-
tation of DER services 
• DSO know-how on distribution net-
works 
• Less computational and modelling 
requirements (restricted to each DSO) 
• No need for operational data transfer 
from DSO to TSO 
• Likely to have the most efficient facili-
tation of DER services 
• DSO know-how on distribution net-
works 
• Less computational and modelling 
requirements (restricted to each DSO) 
• No need for operational data transfer 
from DSO to TSO and less data ex-
changes between TSO and DSO/DER 
Disadvantages 
and  
Challenges 
• Likely to have a less efficient facilitation of 
DER services 
• Huge computational and modelling challenges 
for the TSO (transmission and distribution) 
• High amounts of operational data transfer 
between TSO and DSOs 
• TSO lacks know-how on distribution networks 
• Potential DSO conflict of interest 
• Each DSO still has computational and 
modelling challenges 
• More complex TSO-DSO coordination 
processes 
• Potential DSO conflict of interest 
• Each DSO still has computational and 
modelling challenges with further com-
plexity with distribution-level markets 
• DSO lacks know-how on markets 


---

Page 7

---

21st Power Systems Computation Conference
 
   
 
Porto, Portugal — June 29 – July 3, 2020 
 
   PSCC 2020 
iterative power flow is used to validate DER bids on MV net-
works. A complete process is proposed in [22] using a single-
phase AC OPF for DER validation on distribution networks, 
while a DC OPF is used for system dispatch. In all cases, cen-
tralised optimization algorithms are used to solve the OPF. 
Furthermore, in the DSO-managed model the system dis-
patch responsibility is divided between the TSO and the DSO, 
each one taking care of its own network. In [36, 38, 40, 44], 
the DSO optimizes DER services dispatch in order to send the 
dispatch command to DER (Fig. 3, step 4) and match the tar-
get given by the TSO. This is done using a single-phase AC 
OPF for MV networks and considering both centralized [36, 
38, 40, 44] and distributed [36] optimization algorithms to 
solve the problem. In [35, 37-39, 44, 45], the validation (Fig. 
3, step 2a) and subsequent aggregation of DER services to be 
sent to the TSO (Fig. 3, step 2b) are performed by the DSO 
considering MV networks. In most cases, a centralised optimi-
zation algorithm is used to solve a single-phase AC OPF, but 
[39] proposes an iterative power flow approach. The complete 
process presented in Fig. 3 is captured by the techniques pre-
sented in [23-26, 28] using different optimization algorithms. 
In [23, 24, 28], a distributed approach is used to decouple 
transmission network (DC OPF) from MV networks (single-
phase AC OPF). In [25, 26] a hierarchical optimization algo-
rithm is chosen to solve a single-phase AC OPF in three lev-
els, which are represented by a simplified transmission net-
work, a detailed MV network, and simplified LV networks. 
From a scalability perspective, solution techniques need to 
ensure that TSOs and/or DSOs will be able to solve validation 
and dispatch problems on ultra large or large networks. How-
ever, most of the proposed techniques were tested in relatively 
small networks (≤900 single-phase buses). So, even if some of 
the solution techniques show potential for scalability, it is not 
possible to affirm that such techniques are scalable. Other 
considerations include controllable network assets and the size 
of DER. Only a few papers consider extra flexibility brought 
by devices such as OLTCs on their solution techniques [22, 
35, 37-40, 45]. Similarly, although the largest proportion of 
DER installations correspond to small and medium capacities 
(<100kVA), only a few papers investigate their validation and 
dispatch [27, 31, 32, 36, 44]. 
Based on the above, it is possible to identify trends and 
gaps on the literature of TSO-DSO coordination models. Most 
works adopt AC OPF formulations for distribution networks 
TABLE II. LITERATURE MAPPING 
 
TSO-DSO Coordination Model 
TSO-Managed TSO-DSO Hybrid-Managed 
DSO-Managed 
Conceptual, Discussion, Overview and Pilot Projects 
[16-21] 
[1, 5-7, 9, 10, 12, 13, 16-20, 
29, 30, 33, 34] 
[1, 5, 7, 9, 12, 14, 16-21, 34, 41-43] 
Detailed 
Numerical 
Application 
Solution 
Engine 
Model 
Deterministic 
[23-28] 
[28, 32] 
[23-26, 28, 35-39, 45] 
Stochastic 
 
[31] 
[40],[44]a 
Formulation 
ACOPF Single-Phase 
[22-28] 
[22] 
[23-26, 28, 35-37, 40, 44, 45] 
DCOPFb 
[22-24, 28] 
[22],[28]c 
[23, 24, 28] 
Iterative Power Flow 
 
[31, 32] 
[39] 
Data-driven Aggregation 
of Feasible Regions 
[27] 
 
 
Optimization 
Algorithm 
Centralised 
[22-28] 
[22, 28] 
[35-38, 40, 44, 45] 
Hierarchicald 
 
 
[25, 26] 
Distributede 
 
 
[23, 24, 28, 36] 
Data 
Snapshot 
[23-26, 28] 
[28] 
[23-26, 28, 35, 37-39, 45] 
Time-
series 
< 15 minutes 
[27] 
 
[36] 
from 15 to 59 
minutes 
[22] 
[22, 31] 
[40] 
≥ 1 hour 
 
[32] 
[44] 
DER 
≥ 100kVA 
[23-26, 28] 
[28, 31] 
[23-26, 28, 35-40, 44, 45] 
< 100kVA 
[27] 
[31, 32] 
[36, 44] 
Network 
Modelling 
Only MV (1kV-110kV) 
[25, 26]f  
[31, 32] 
[25, 26, 35-40, 44, 45] 
Transmission-MV (>1kV) [23, 24],[27]g,[28] 
[28]g 
[23, 24, 28] 
Controllable Network 
Assets 
[22] 
[22] 
[35, 37-40, 45] 
Scale 
≤ 900 buses 
[23-28] 
[28, 32, 33] 
[23-26, 28, 35-37, 39, 40, 44, 45] 
Issues 
Voltage 
[22-28] 
[22, 28, 32] 
[23-26, 28, 35-40, 44, 45] 
Assets Congestion 
[22-26, 28] 
[22, 28, 31, 32] 
[23-26, 28, 35, 37, 39, 40, 44, 45] 
 
a If the aggregator is considered as the DSO it can be classified as DSO-Managed Model 
b Transmission 
c It does not perform bids validation on distribution network, but it considers as the validation was performed before, so it makes the DCOPF for transmission 
d Between Transmission-MV-DER 
e Decoupled between Transmission-Distribution or between MV-DER 
f Really simplified transmission and LV network 
g Only transmission network is considered 


---

Page 8

---

21st Power Systems Computation Conference
 
   
 
Porto, Portugal — June 29 – July 3, 2020 
 
   PSCC 2020 
but do not consider their unbalanced nature, (i.e., use single-
phase formulations instead of three-phase). This is important 
for all types of distribution network design. For USA-style 
networks, MV feeders can be single, two or three-phase, 
whereas in the LV, only a few LV customers are directly con-
nected to distribution transformers. For European-style net-
works, MV feeders are mostly three-phase, whereas distribu-
tion transformers supply multiple three-phase LV feeders and 
then dozens to hundreds of customers. Another aspect is that 
most works consider medium-scale DER and, therefore, mod-
el MV networks only. In reality, a large number of DER will 
be small (e.g., residential rooftop PV) and will be connected to 
lower voltages. Therefore, detailed LV networks and their 
interactions with MV networks will also need to be consid-
ered. It is important to highlight that only recently integrated 
MV-LV test feeders have been made available online (for 
instance, the USA-style IEEE 8500-Node Test Feeder made 
available in 2010 [46]). This scarcity of MV-LV test feeders 
might be part of the reason why only a few studies consider 
integrated MV-LV networks. Moreover, the consideration of 
controllable network assets (e.g., OLTCs), and their effects on 
DER validation, etc. is not well investigated. However, ad-
dressing all these aspects will add complexity to the validation 
and dispatch problem, bringing scalability challenges. Conse-
quently, there will be a need for departing from centralized 
approaches and embrace the advantages of distributed optimi-
zation algorithms. 
IV.CONCLUSION 
The volume of services procured by transmission system 
operators (TSOs) through distributed energy resources (DER), 
has been increasing in recent years. Consequently, distribution 
system operators (DSOs) will soon be needed to have a more 
active role to ensure the integrity of the distribution network 
while facilitating DER services. To achieve this, adequate 
coordination between TSOs and DSOs is required. This paper 
first examined the relevant literature, using both academic and 
industry sources. Three core TSO-DSO coordination models 
were identified.  
The first model, referred to as the TSO-managed model, 
can be considered to be the natural evolution of the model 
currently used around the world in which the TSO coordinates 
energy and service providers; with the added visibility of dis-
tribution networks and consideration of the corresponding 
technical constraints to validate DER services bids. However, 
as the volume of DER participating in markets and services 
increases in the future, this will become an ultra-large-scale 
problem significantly more difficult to solve. 
The other two core models identified gives DSOs a more 
active role. In the TSO-DSO hybrid-managed model, the DER 
services bids validation is under the DSO responsibility, while 
the DER dispatch remains responsibility of the TSO. In the 
DSO-managed model, both the responsibility of DER services 
bids validation and DER dispatch falls on the DSO. These two 
models, however, increase the coordination complexity be-
tween the TSO and DSOs. They can also be affected by poten-
tial conflicts of interest from the DSO in regard to facilitating 
more DER services vs. the added cost that this will incur as 
their assets will be pushed to the limits. However, this could 
be addressed with adequate regulation (e.g., rules, incentives). 
In summary, decision makers should evaluate the different 
core models and decide based on the characteristics that better 
fit the reality and needs of the corresponding power system. 
Certainly, the chosen core model will need to be tailored to the 
considered power system reality or its planned future. 
Finally, this paper also mapped the solution techniques 
proposed in the literature for the different TSO-DSO coordina-
tion models. The single-phase AC OPF was the most common 
way of capturing the technical constraints and non-linearities 
of distribution networks when solving validation and dispatch 
problems of (mainly) medium-scale DER connected to MV 
levels. This, however, also highlights the need for comprehen-
sive three-phase approaches that can not only handle the un-
balance nature of distribution networks but also multiple volt-
ages levels (e.g., MV and LV) so as to capture the effects of 
small-scale DER (e.g., residential rooftop PV) as well as con-
trollable assets (e.g., OLTCs). This, in turn, will require ex-
ploring more the use of distributed optimization algorithms to 
solve such large-scale and complex problems. 
REFERENCES 
[1] 
AEMO and E. N. Australia, "Open Energy Networks Consultation 
Response," 2018. 
[2] 
A. Navarro-Espinosa and L. F. Ochoa, "Probabilistic Impact 
Assessment of Low Carbon Technologies in LV Distribution Systems," 
IEEE Transactions on Power Systems, vol. 31, no. 3, pp. 2192-2203, 
2016. 
[3] 
A. T. Procopiou, K. Petrou, L. F. Ochoa, T. Langstaff, and J. 
Theunissen, "Adaptive Decentralized Control of Residential Storage in 
PV-Rich MV–LV Networks," IEEE Transactions on Power Systems, 
vol. 34, no. 3, pp. 2378-2389, 2019. 
[4] 
K. Petrou, A. T. Procopiou, L. F. Ochoa, T. Langstaff, and J. 
Theunissen, "Impacts of Price-Led Operation of Residential Storage on 
Distribution Networks: An Australian Case Study," presented at the 
IEEE Milan PowerTech, Milan, Italy, 2019.  
[5] 
E. N. Association, "Open Networks Project: Opening Markets for 
Network Flexibility," Energy Networks Association2017. 
[6] 
Sweco, "Study on the Effective Integration of Distributed Energy 
Resources for Providing Flexibility to the Electricity System," 2015. 
[7] 
AEMO and E. N. Australia, "Open Energy Networks Project: 
Workshop to Test Required Capabilities, Test Interactive Meta-Models 
and Discuss CBA Methodology," 2019. 
[8] 
M. Miller et al., "Status Report on Power System Transformation: A 
21st Century Power Partnership Report," National Renewable Energy 
Laboratory (NREL)2015. 
[9] 
AEMO and E. N. Australia, "Open Energy Networks: Required 
Capabilities and Recommended Actions," 2019. 
[10] CEDEC, ENTSO-E, GEODE, E.DSO, and EURELETRIC, "TSO-DSO 
Report: An Integrated Approach to Active System Management with 
the Focus on TSO-DSO Coordination in Congestion Management and 
Balancing," 2019. 
[11] L. N. Ochoa, F. Pilo, A. Keane, P. Cuffe, and G. Pisano, "Embracing an 
Adaptable, Flexible Posture: Ensuring That Future European 
Distribution Networks Are Ready for More Active Roles," IEEE Power 
and Energy Magazine, vol. 14, no. 5, pp. 16-28, 2016. 
[12] M. McGranaghan, D. Houseman, L. Schmitt, F. Cleveland, and E. 
Lambert, "Enabling the Integrated Grid: Leveraging Data to Integrate 
Distributed Resources and Customers," IEEE Power and Energy 
Magazine, vol. 14, no. 1, pp. 83-93, 2016. 


---

Page 9

---

21st Power Systems Computation Conference
 
   
 
Porto, Portugal — June 29 – July 3, 2020 
 
   PSCC 2020 
[13] S. Repo et al., "The IDE4L Project: Defining, Designing, and 
Demonstrating the Ideal Grid for All," IEEE Power and Energy 
Magazine, vol. 15, no. 3, pp. 41-51, 2017. 
[14] P. Mallet, P.-O. Granstrom, P. Hallberg, G. Lorenz, and P. Mandatova, 
"Power to the People!: European Perspectives on the Future of Electric 
Distribution," IEEE Power and Energy Magazine, vol. 12, no. 2, pp. 
51-64, 2014. 
[15] D. Forfia, M. Knight, and R. Melton, "The View from the Top of the 
Mountain: Building a Community of Practice with the GridWise 
Transactive Energy Framework," IEEE Power and Energy Magazine, 
vol. 14, no. 3, pp. 25-33, 2016. 
[16] G. Migliavacca et al., "SmartNet: H2020 project analysing TSO–DSO 
interaction to enable ancillary services provision from distribution 
networks," CIRED - Open Access Proceedings Journal, vol. 2017, no. 
1, pp. 1998-2002, 2017. 
[17] H. Gerard, E. I. Rivero Puente, and D. Six, "Coordination between 
transmission and distribution system operators in the electricity sector: 
A conceptual framework," Utilities Policy, vol. 50, pp. 40-48, 2018. 
[18] C. Madina et al., "Cost-Benefit Analysis of TSO-DSO Coordination to 
Operate Flexibility Markets," presented at the 25th International 
Conference on Electricity Distribution, Madrid, Spain, 2019.  
[19] L. Lind, R. Cossent, J. P. Chaves‐Ávila, and T. Gómez San Román, 
"Transmission and distribution coordination in power systems with 
high shares of distributed energy resources providing balancing and 
congestion management services," Wiley Interdisciplinary Reviews: 
Energy and Environment, vol. 8, no. 6, 2019. 
[20] P. D. Martini and L. Kristov, "Distribution Systems in a High 
Distributed Energy Resources Future: Planning, Market Design, 
Operation and Oversight," 2015. 
[21] L. Kristov, "The Bottom-Up (R)Evolution of the Electric Power 
System: The Pathway to the Integrated-Decentralized System," IEEE 
Power and Energy Magazine, vol. 17, no. 2, pp. 42-49, 2019. 
[22] M. Rossi et al., "Testing TSO-DSO Interaction Schemes for the 
Participation of Distributed Energy Resources in the Balancing Market: 
The Smartnet Simulator," presented at the 25th International 
Conference on Electricity Distribution, Madrid, Spain, 2019.  
[23] H. Le Cadre, I. Mezghani, and A. Papavasiliou, "A game-theoretic 
analysis of transmission-distribution system operator coordination," 
European Journal of Operational Research, vol. 274, no. 1, pp. 317-
339, 2019. 
[24] A. Mohammadi, M. Mehrtash, and A. Kargarian, "Diagonal Quadratic 
Approximation for Decentralized Collaborative TSO+DSO Optimal 
Power Flow," IEEE Transactions on Smart Grid, vol. 10, no. 3, pp. 
2358-2370, 2019. 
[25] Z. Yuan and M. R. Hesamzadeh, "Hierarchical coordination of TSO-
DSO economic dispatch considering large-scale integration of 
distributed energy resources," Applied Energy, vol. 195, pp. 600-615, 
2017. 
[26] Z. Yuan, M. R. Hesamzadeh, and D. R. Biggar, "Distribution 
Locational Marginal Pricing by Convexified ACOPF and Hierarchical 
Dispatch," IEEE Transactions on Smart Grid, vol. 9, no. 4, pp. 3133-
3142, 2018. 
[27] E. Polymeneas and S. Meliopoulos, "Aggregate Modeling of 
Distribution Systems for Multi-Period OPF," presented at the Power 
Systems Computation Conference (PSCC), Genoa, Italy, 2016.  
[28] A. Papavasiliou and I. Mezghani, "Coordination Schemes for the 
Integration of Transmission and Distribution System Operations," 
presented at the Power Systems Computation Conference (PSCC), 
Dublin, Ireland, 2018.  
[29] A. Angioni et al., "A distributed automation architecture for 
distribution networks, from design to implementation," Sustainable 
Energy, Grids and Networks, vol. 15, pp. 3-13, 2018. 
[30] U. S. D. o. Energy, "Modern Distribution Grid Decision Guide: 
Volume III," 2017. 
[31] D. Koraki and K. Strunz, "Wind and Solar Power Integration in 
Electricity Markets and Distribution Networks Through Service-Centric 
Virtual Power Plants," IEEE Transactions on Power Systems, vol. 33, 
no. 1, pp. 473-485, 2018. 
[32] J. A. P. Lopes, F. J. Soares, and P. M. R. Almeida, "Integration of 
Electric Vehicles in the Electric Power System," Proceedings of the 
IEEE, vol. 99, no. 1, pp. 168-183, 2011. 
[33] EURELECTRIC, "Designing Fair and Equitable Market Rules for 
Demand Response Aggregation," 2015. 
[34] S. Y. Hadush and L. Meeus, "DSO-TSO cooperation issues and 
solutions for distribution grid congestion management," Energy Policy, 
vol. 120, pp. 610-621, 2018. 
[35] J. Silva et al., "Estimating the Active and Reactive Power Flexibility 
Area at the TSO-DSO Interface," IEEE Transactions on Power 
Systems, vol. 33, no. 5, pp. 4741-4750, 2018. 
[36] E. Dall'Anese, S. S. Guggilam, A. Simonetto, Y. C. Chen, and S. V. 
Dhople, "Optimal Regulation of Virtual Power Plants," IEEE 
Transactions on Power Systems, vol. 33, no. 2, pp. 1868-1881, 2018. 
[37] J. Silva, J. Sumaili, R. J. Bessa, L. Seca, M. Matos, and V. Miranda, 
"The challenges of estimating the impact of distributed energy 
resources flexibility on the TSO/DSO boundary node operating points," 
Computers & Operations Research, vol. 96, pp. 294-304, 2018. 
[38] N. Fonseca et al., "EvolvDSO Grid Management Tools to Support 
TSO-DSO Cooperation," presented at the CIRED Workshop, Helsinki, 
Finland, 2016.  
[39] M. Heleno, R. Soares, J. Sumaili, R. J. Bessa, L. Seca, and M. A. 
Matos, "Estimation of the Flexibility Range in the Transmission-
Distribution Boundary," presented at the IEEE Eindhoven PowerTech, 
Eindhoven, Netherlands, 2015.  
[40] A. Saint-Pierre and P. Mancarella, "Active Distribution System 
Management: A Dual-Horizon Scheduling Framework for DSO/TSO 
Interface Under Uncertainty," IEEE Transactions on Smart Grid, vol. 
8, no. 5, pp. 2186-2197, 2017. 
[41] J. Villar et al., "Flexibility Hub - Multi Service Framework for 
Coordination of Decentralised Flexibilities," presented at the 25th 
International Conference on Electricity Distribution, Madrid, Spain, 
2019.  
[42] M. Pardo, C. Madina, M. Marroquín, and E. Estrade, "Use of Radio 
Base Stations to Provide Ancillary Services to the DSO Through Local 
Flexibility Markets," presented at the 25th International Conference on 
Electricity Distribution, Madrid, Spain, 2019.  
[43] Y. Tohidi, M. Farrokhseresht, and M. Gibescu, "A Review on 
Coordination Schemes Between Local and Central Electricity Markets," 
presented at the 15th International Conference on the European Energy 
Market (EEM), Lodz, Poland, 2018.  
[44] B. Vatandoust, A. Ahmadian, M. A. Golkar, A. Elkamel, A. 
Almansoori, and M. Ghaljehei, "Risk-Averse Optimal Bidding of 
Electric Vehicles and Energy Storage Aggregator in Day-Ahead 
Frequency Regulation Market," IEEE Transactions on Power Systems, 
vol. 34, no. 3, pp. 2036-2047, 2019. 
[45] F. Capitanescu, "TSO–DSO interaction: Active distribution network 
power chart for TSO ancillary services provision," Electric Power 
Systems Research, vol. 163, pp. 226-230, 2018. 
[46] R. C. Dugan and R. F. Arritt, "The IEEE 8500-Node Test Feeder," 
presented at the IEEE PES T&D 2010, New Orleans, LA, USA, 2010.  
 
