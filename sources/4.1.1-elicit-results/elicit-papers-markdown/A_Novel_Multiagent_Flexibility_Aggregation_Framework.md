# A Novel Multiagent Flexibility Aggregation Framework

## Paper Metadata

- **Filename:** A_Novel_Multiagent_Flexibility_Aggregation_Framework_DOI_10-48550_ARXIV-2307-08401.pdf
- **DOI:** 10.48550/ARXIV.2307.08401
- **Authors:** Orfanoudakis, Stavros and Chalkiadakis, Georgios
- **Year:** 2023
- **Journal/Venue:** arXiv.org
- **URL:** https://arxiv.org/abs/2307.08401
- **Extraction Date:** 2025-06-03T15:01:22.000640
- **Total Pages:** 12

## Abstract



## Keywords



---

## Full Text Content



### Page 1

A Novel Multiagent Flexibility Aggregation Framework
Stavros Orfanoudakis
Technical University of Crete
Chania, Greece
sorfanoudakis@tuc.gr
Georgios Chalkiadakis
Technical University of Crete
Chania, Greece
gehalk@intelligence.tuc.gr
ABSTRACT
The increasing number of Distributed Energy Resources (DERs) in
the emerging Smart Grid, has created an imminent need for intelligent multiagent frameworks able to utilize these assets efficiently. In
this paper, we propose a novel DER aggregation framework, encompassing a multiagent architecture and various types of mechanisms
for the effective management and efficient integration of DERs in
the Grid. One critical component of our architecture is the Local
Flexibility Estimators (LFEs) agents, which are key for offloading
the Aggregator from serious or resource-intensive responsibilities—
such as addressing privacy concerns and predicting the accuracy of
DER statements regarding their offered demand response services.
The proposed framework allows the formation of efficient LFE cooperatives. To this end, we developed and deployed a variety of
cooperative member selection mechanisms, including (a) scoring
rules, and (b) (deep) reinforcement learning. We use data from the
well-known Power TAC simulator to systematically evaluate our
framework. Our experiments verify its effectiveness for incorporating heterogeneous DERs into the Grid in an efficient manner.
In particular, when using the well-known probabilistic prediction
accuracy-incentivizing CRPS scoring rule as a selection mechanism,
our framework results in increased average payments for participants, when compared with traditional commercial aggregators.
KEYWORDS
Flexibility Aggregators, Multiagent Systems, Smart Grid, Mechanism Design, Distributed Energy Resources
1
INTRODUCTION
The depletion of fossil fuels has created an imminent need to deploy
even more renewable energy power generators [4]. However, the
state of the current energy grid makes it hard to efficiently optimize
the performance of intermittent assets [1], such as solar panels and
wind turbines; thus, the need for a “smarter” electricity grid has
been created [20, 37]. The Smart Grid, with its bidirectional electricity and information flow, is envisaged to deliver electrical power in
very resourceful ways, and successfully exploit all the Distributed
Energy Resources (DERs) that are continuously emerging. DERs
are the various electricity supply or demand assets that are spread
across the Grid; and which, however small, when combined, can
enhance the Grid’s ability to seamlessly provide power, even if it
largely originates from intermittent renewable energy sources.
Furthermore, recent developments regarding environmental policies and the emergence of a multitude of (distributed) energy markets, have turned the attention of the electricity stakeholders to
the research on DERs’ flexibility [26]. In the literature, flexibility
is defined as the elasticity property of the DERs that can provide
ancillary services to support the stability of the grid [43]. Essentially, flexibility corresponds to the DERs’ ability to either offer
produced/stored energy or consumption reduction services to the
Grid. Thus, many works are studying various ways to estimate
the flexibility of DER assets [18, 55]; while the use of aggregators [14, 32, 33] is one of the most important mechanisms that were
created to utilize the flexibility of the DERs in the Smart Grid.
An aggregator is a mediator between DERs and the energy markets [14], with the mission to trade the flexibility obtained from the
DERs by participating in the markets on behalf of the DERs’ owners [32]. Generally, aggregators offer stability guarantees to the Grid
by offering flexible loads. Currently, the existing legal frameworks
of many countries, especially in the EU and USA, have been updated
to allow the existence of such aggregator mechanisms [6, 48].
Nonetheless, there are still many open research topics regarding
the functionality and mechanisms of the aggregator. For example,
there are privacy concerns about the metering information constantly transmitted between the DERs and the aggregator [13, 52].
Also, there is an interest in designing efficient Demand-Response
(DR) aggregator mechanisms to improve the Smart Grid’s technical,
economic, and market aspects [17, 38].
In this paper, we employ mechanism design and cooperative
game theory ideas to propose a novel aggregator framework for the
efficient integration of DERs in the Grid. Our framework provides
an aggregation architecture along with mechanisms for its effective
and efficient operation and aims to (and, as our experiments show,
succeeds in) increase the flexibility offered by the aggregator to the
Grid and the profits of the participating agents.
In our multiagent architecture 1, we introduce the so-called Local
Flexibility Estimators (LFEs) that allow us to address some severe
aggregator issues, such as privacy concerns and evaluation of the
DERs’ flexibility accuracy. LFEs essentially serve as DER coalition
managers, coordinating their members’ market activities. Given
this, our work’s focus is the creation of efficient LFE cooperatives
intending to increase the profits of every stakeholder. To achieve
this, we have populated our framework with various selection
mechanisms—some of which are scoring rules [15], and some are
(deep) reinforcement learning (RL) [46] techniques. To the best of
our knowledge, using RL for this purpose is entirely novel. An
Aggregator agent can then use these selection mechanisms to decide
which LFEs to include in its (flexibility) offers to the day-ahead
markets. We provide a systematic experimental evaluation using
data from the Power TAC [22] simulator in various experimental
scenarios that we formulated to test the different aspects of our
aggregator framework. Last but not least, our work extends the
Power TAC simulator with aggregator-enabling functionality.
Arguably, our aggregator framework contributes to the smooth
DERs’ integration into the Grid since (a) it allows smaller DERs
1This is the full version of the paper “A Novel Aggregation Framework for the Efficient
Integration of Distributed Energy Resources in the Smart Grid” originally presented at
AAMAS 2023 [34].
ar Xiv:2307.08401v1 [cs.AI] 17 Jul 2023

---


### Page 2

A Novel Multiagent Flexibility Aggregation Framework
Stavros Orfanoudakis and Georgios Chalkiadakis
to participate in the Smart Grid markets; (b) it selects which LFEs
to participate in the energy transactions, increasing the expected
accuracy of the promised offers, thus indirectly aiding the Grid’s
stability; and (c) as verified via our experiments, the use of certain
designed selection and pricing mechanisms leads to higher payments for (at least the competent in terms of prediction accuracy,
but also sometimes the not-so-accurate) LFEs that the aggregator
manages. Specific findings of our systematic experimentation are:
(1) The use of the truthfulness-incentivizing Continuous Ranked
Probability Score (CRPS) [15, 41] mechanism rewards effectively
LFEs that have reliable flexibility estimates and results to the highest
aggregator-to-LFEs payments for those LFEs, compared to those
achieved with other selection mechanisms; or compared to assets’
earnings in “baseline settings” when they either participate in a
“traditional” aggregator that manages all available DERs or when
they trade directly with the Grid.
(2) A Simple Selection mechanism we put forward ranks as a
close second to CRPS. However, this mechanism is easier for nonspecialists to understand. This result implies a trade-off between
using a highly efficient yet complex scoring rule vs. a slightly less
efficient yet easy-to-understand selection mechanism, since using
the latter can motivate the participation of small DERs (e.g., corresponding to small & medium-sized enterprises or private homes).
(3) The DQN Selection mechanisms were better than the aforementioned baseline settings only for certain settings in which DER
accuracy does not fluctuate dynamically over time.
(4) Low-accuracy LFEs prefer to participate in larger LFE cooperatives so their errors can be balanced out by the team.
(5) When using the CRPS Selection mechanism, and regardless of
the LFEs’ prediction accuracy, our framework results in increased
profits for every LFE, compared to those potentially accrued via
participation in functional commercial flexibility aggregators paid
via pricing mechanism in use in the current Smart Grid [12].
2
BACKGROUND AND RELATED WORK
This section provides background and reviews related work.
2.1
Distributed Energy Resources (DERs)
To begin, DERs, are electricity supply or demand resources located
across the Smart Grid. One of the most common DER types are
Battery Energy Storage Systems (BESS). These can be either in the
form of dedicated batteries or embedded batteries within electric
vehicles (EVs) [39, 49]. BESS are essential because they can store
energy to shift the demand at other hours of need [23]; while the
eventual incorporation of millions of EVs in the Grid creates opportunities for their utilization in demand-response and flexibility
aggregation. Furthermore, there are many interruptible load users,
usually households that offer to limit their electricity usage at specified times to contribute to demand-shifting tasks [42]. Finally, many
types of small-scale renewable energy generators exist, the most
common being wind turbines and solar panels that can be located
on the rooftops of both apartments and electric vehicles [51].
2.2
The Role of the Aggregator
DERs are in general too small to be “visible” to the Grid and efficiently participate in energy trading on their own [9, 24]. Thus the
main functionality of an aggregator is to accumulate DER flexibility and perform demand-response and load-balancing to increase
the total profit while supporting the Grid stability. This is possible
since an aggregator is considered a reliable participant in the energy
markets because of the considerable flexibility loads it can control.
The current regulations and the state of the energy markets
allow existing actors, such as energy suppliers [10] and balance
responsible parties [3], to take the role of the aggregator and trade
flexibility. This is possible because, in practice, the aggregator’s
portfolio consists of DER assets usually owned by other stakeholders and utilized by the aggregator to implement its business model.
However, there are also independent aggregators [44] which are not
affiliated with any other entity like suppliers or balancing utilities.
Our framework can support all three types of existing aggregators.
2.3
Power TAC: The Smart Grid simulator
Power TAC [22] is a rich competitive economic simulation of future energy markets featuring several Smart Grid components(e.g.,
DERs, retail and wholesale energy markets, etc.). With the help of
this simulator, researchers can better understand the behavior of
future customer models and experiment with retail and wholesale
market decision-making by creating competitive agents and benchmarking their strategies against each other. In this way, a host of
useful information is extracted, which can be used by policymakers
and industries to prepare for the upcoming market changes.
In our case, we have modified the Power TAC platform so it can
support the addition of aggregator mechanisms, but without altering the behavior of its realistic DER and market models. Another
reason we selected this simulation platform is that it employs a
realistic day-ahead wholesale market simulating the supply and
the demand of future energy markets in a pretty accurate way.
2.4
Related Work
Aggregators and their mechanisms have become a very active research topic because of the rise of flexible loads in the grid. Several
studies about the business models of aggregators and the way they
should operate exist. For example [33], reviews the existing aggregator models’ operational and economic aspects. Another work [26]
proposes a hierarchical control framework that enables the provision of flexible services in power systems through aggregation
entities. Zheng et al. [54] have developed an aggregator-based resource allocation system using an artificial neural network and
other optimization techniques. Finally, [7] proposes, among other
things, a flexibility aggregation architecture that uses so-called
“minimum flexibility units” that operate at a local level and represent single flexibility assets, industrial microgrids, or multiple end
users. These units however always correspond to a single meter and
do not manage heterogeneous DERs nor evaluate their accuracy.
Furthermore, there are many works about the demand response
operations of the aggregators [14, 17, 31]. SEMIAH [19] is an aggregator framework designed to support European demand response
programs. It uses a component-based architecture and focuses on
the functionality of the virtual power plant. Additionally, there are
distributed algorithms developed for large-scale demand response
aggregation [8, 28]. Also, Rawat et al. [38] propose a two-stage

---


### Page 3

A Novel Multiagent Flexibility Aggregation Framework
Stavros Orfanoudakis and Georgios Chalkiadakis
interactive, responsive load scheduling model developed between a
demand response aggregator and the distribution system operator.
One more critical aspect of the aggregator research is the security of information transactions and the integration of electric
vehicles. Wagh et al. [52] address the problem of cybersecurity by
developing a distributed privacy reserving framework that aggregators can adapt. Another study [13] with a similar research focus
proposes an aggregation scheme with local differential privacy that
can efficiently and practically estimate power supply and demand
statistics while preserving any individual participant’s privacy. Finally, there are many studies about the aggregation of EVs [45].
Specifically, many of these studies focus on the charging scheduling
of EVs [16, 47, 50]. Other works study the payment mechanisms
for electric vehicle aggregators [35, 36]. Last but not least, several works in the literature approach the aggregation problem as a
coalition formation one, proposing game-theoretic and mechanism
design solutions to form DER cooperatives so that these are able to
participate in demand-response tasks [2, 9, 41]. Interestingly, [2]
demonstrates that creating larger coalitions, such as the LFEs in
our case, can lead to more efficient energy trading.
3
A NOVEL DER AGGREGATOR FRAMEWORK
Privacy concerns, impartial and fair scoring of the LFEs, and efficient management of all stakeholders’ assets are the main problems
this two-step DER aggregation architecture addresses. In particular, our framework provides an aggregation architecture along
with mechanisms for its effective and efficient operation, increasing the actual flexibility offered by the aggregator to the Grid and
the profits of the participating agents. Additionally, the proposed
architecture can be distinguished into three levels, as depicted in
Fig. 1. The first is the Distributed Energy Resources level consisting
of many Smart Grid assets. Specifically, our framework supports
smaller and bigger scale DERs utilized by the Smart Grid. The second level of this framework is named the Aggregator Level, and it
consists of Local Flexibility Estimators (LFEs) organizing the DERs
into coalitions, and a central Aggregator agent which selects which
LFEs to include in a cooperative to participate in flexibility trading
in the Smart Grid. The third level of this framework represents
the Smart Grid itself—specifically, the energy markets to which
the Aggregator-coordinated LFEs cooperative participates. We now
proceed to describe the key parts of our overall framework in detail.
3.1
Local Flexibility Estimators (LFEs)
An LFE agent acts as a coordinator of a coalition consisting of a
varying number of heterogeneous DERs, effectively offering them
visibility to the Grid. This means that all DER assets, regardless
of size, can now participate indirectly in a flexibility aggregation
process: though originally potentially too small to bid in the energy
markets directly [24], DERs can now form LFE-coordinated coalitions; which in turn can be selected by the Aggregator to participate
in LFE cooperatives to trade the accumulated flexibility.
The rationale and particular method an LFE uses to select its
participating DERs are not absolute, as it depends on a multitude of
constraints, priorities, or other factors. One factor could be locality
limitations. For instance, it might be easier to pick all DER assets
lying close to each other in a physical neighborhood because of
s Electric 
Vehicles
Electric 
Vehicles
PV / Wind 
Generators
PV / Wind 
Generators
Interruptible 
Load Users
Interruptible 
Load Users
Storage
Capacity
Storage
Capacity
LFE
LFE
LFE
Distributed Energy 
Resources (DERs)
Energy Markets / 
Grid
Aggregator Level
• Flexibility Estimations
• Other LFE specific 
metrics
• Payment
Aggregator
LFE
LFE
LFE
...
...
...
...
Day-Ahead
Market
Day-Ahead
Market
Distribution 
System 
Operators
Distribution 
System 
Operators
Distribution 
System 
Operators
...
...
...
Figure 1: The component diagram of the proposed aggregator
architecture consists of three levels; the Distributed Energy
Resources, the Aggregator Level, and the Energy Markets
how the smart meters are placed [21]. Alternatively, an LFE might
be formed for the convenience of or to serve the requirements
of a single stakeholder or a group of stakeholders with the same
goals, like Local Energy Communities [27] or small companies.
LFEs can then employ any cooperative formation method of their
choosing that respects the stakeholders’ requirements; for instance,
they can use the very same member selection mechanisms that an
Aggregator may employ, which we describe in detail in Section 3.4.
One of the primary responsibilities of an LFE is to monitor the
consumption and production of the DERs it controls. Importantly,
it can then use the historical consumption/production data to generate accurate estimations of the total flexibility for all participating
DERs. In addition to the flexibility predictions, an LFE also provides
the aggregator with other necessary metrics, such as confidence in
the predictions (see Section 3.4.2). As a result, each LFE handles a
portion of the total aggregator flexibility estimation problem; LFEs
provide the aggregator with all information necessary for it to participate in the market, thus reducing the computational complexity
of the aggregator optimization process [53]. Note that expanding
the functionality of existing DER agents to ease the aggregator’s
computational burden is not an option in most practical settings,
since DERs (EVs, PV, wind turbines) usually if not always come
with given properties and capabilities; nevertheless, all DERs have
communication capabilities, and thus can participate in LFEs which
take up the additional optimization tasks.
Most importantly, LFEs are key to satisfying privacy requirements: all the DER-related information is constrained and protected under the LFEs, so only the corresponding LFE can access
the private data of each DER. Additionally, the proposed distributed
aggregator scheme enables the usage of Smart Grid blockchain technologies [25, 29], which have been used for Smart Grid applications
to secure the transactions made, while also protecting the private
information required for the transactions.

---


### Page 4

A Novel Multiagent Flexibility Aggregation Framework
Stavros Orfanoudakis and Georgios Chalkiadakis
Summing up, LFEs are end-nodes that only have to publish to
the Aggregator limited information with respect to their flexibility
and availability. Other works try to preserve the privacy of DERs
by introducing new communication protocols and algorithms [13,
52]. We propose a new all-in-one framework that can, on top of
all other benefits, contribute to the privacy concerns that arise
when information flows from DERs toward the Aggregator. For
instance, there are commercial aggregators that group DERs daily in
a relatively simple, straightforward manner, but DERs have to share
operation patterns (i.e., private information) with the Aggregator.
In our case, DERs with common interests could form an LFE and
participate as a multipurpose flexibility entity in any Aggregator,
hiding their details from the (potentially non-trusted) Aggregator.
3.2
The Aggregator agent
The aggregator in our framework possesses all the properties of a
usual Smart Grid aggregator [14]; however, it has some additional
novel properties too, such as the ability to form LFE cooperatives.
The framework we propose is comprised of a single aggregator that
directly controls the assigned LFEs and indirectly manages all the
DERs that the LFEs closely monitor. Additionally, the aggregator is
responsible for gathering all the smart-metering data, e.g., flexibility
estimations already pre-processed by the LFEs, to efficiently manage
the assets and trade their excess flexibility. To address the problem
of increasing the profits of each stakeholder, our Aggregator deploys
a variety of scoring rules so it can fairly rank the LFEs according
to their historic flexibility estimations’ accuracy.
An important benefit of incorporating LFEs is that it enables
the Aggregator agent to use formation mechanisms, so as to create
efficient LFE cooperatives to increase profits, while also incentivizing truthful and accurate predictions contributing to Grid stability.
Ranking and selecting LFEs is key, since LFEs with unreliable (lowaccuracy predictions regarding their) flexibility estimations should
not participate in the Aggregator’s flexibility offers since they can
damage both the Aggregator’s profits and overall reputation. This
does not mean that low-accuracy LFEs will be excluded from the
markets. Instead, they can trade with the Grid directly.2
The Aggregator is thus able to calculate the total energy flexibility it can offer by selecting which LFEs will participate in the
upcoming flexibility trades, using scoring and ranking mechanisms
such as the ones we propose below. Moreover, the Aggregator is
responsible for splitting the profits back to the LFEs, based on their
contribution and appropriate scoring mechanisms that may also
take into account the accuracy of LFE flexibility predictions.
The total communication complexity of the proposed framework certainly increases compared to a traditional aggregator [14].
However, notice that LFEs are local (e.g., managing the assets of
a single company or local energy community); hence the added
communication load with their DERs is expected to be minimal.
Overall, incorporating LFEs within an Aggregator agent allows
us to generalize and scale up, since an Aggregator can serve more
DERs by just adding LFEs to take up some of its optimization processes. Therefore, offloading some of the optimization complexity to
2Notice that though LFEs can trade with the Grid directly, the distinct Aggregator
architectural level is required, because otherwise, it would not be possible for non-local
DERs to group together and reap the benefits of providing large, and potentially highly
diverse, flexible loads.
a lower level (that of LFEs) could mean more accurate and scalable
outcomes in terms of flexibility provided to the Grid.
3.3
Flexibility Estimation
In a Smart Grid context, total aggregator flexibility is its capability
of shifting electrical loads either from itself to the Grid, or in the
opposite direction [26]; and there are many works that deal with
flexibility estimation or forecasting [11, 18]. At a given timeslot 𝑡,
we calculate the flexibility provided by each DER as follows.
To begin, BESS’s available flexibility is proportional to its current
energy level and specific charge/ discharge speed in KWh (Eq. 1).
𝑓𝑙𝑒𝑥𝐵𝐸𝑆𝑆(𝑡) = 𝐶ℎ𝑎𝑟𝑔𝑒(𝑜𝑟𝐷𝑖𝑠𝑐ℎ𝑎𝑟𝑔𝑒) 𝑆𝑝𝑒𝑒𝑑(𝑡)
(1)
The same principle applies to EVs, with the difference that to calculate EVs’ flexibility 𝑓𝑙𝑒𝑥𝐸𝑉(𝑡), one has to account for a minimum
battery level they should maintain in order to continue traveling.
The flexibility that interruptible load users can provide was set
(following [18]), to 10% of the load they are currently using. Hence,
upon request of the aggregator through the LFEs, interruptible load
users can alter their energy consumption by 10%:
𝑓𝑙𝑒𝑥𝐼𝑛𝑡𝑒𝑟𝑟𝑢𝑝𝑡𝑖𝑏𝑙𝑒𝐿𝑜𝑎𝑑𝑈𝑠𝑒𝑟𝑠(𝑡) = 10% 𝐿𝑜𝑎𝑑(𝑡)
(2)
Most renewable energy-producing DERs do not have the ability
to halt their production, so the flexibility of such DER assets is
represented by the amount of energy they produce (Eq. 3):
𝑓𝑙𝑒𝑥𝐸𝑛𝑒𝑟𝑔𝑦𝐺𝑒𝑛𝑒𝑟𝑎𝑡𝑜𝑟𝑠(𝑡) = 𝐸𝑛𝑒𝑟𝑔𝑦𝐺𝑒𝑛𝑒𝑟𝑎𝑡𝑒𝑑(𝑡)
(3)
Then, the total flexibility of an LFE is the aggregate flexibility of
all DER assets it controls. Hence, the flexibility of 𝐿𝐹𝐸𝑖that controls
a set 𝐾of DERs at timeslot 𝑡is defined as follows (Eq. 4):
𝑓𝑙𝑒𝑥𝐿𝐹𝐸𝑖(𝑡) =
∑︁
∀𝑘∈𝐾
𝑓𝑙𝑒𝑥𝐷𝐸𝑅𝑘(𝑡)
(4)
where 𝑓𝑙𝑒𝑥𝐷𝐸𝑅𝑘(𝑡) is calculated given the DER’s type.
Finally, the total flexibility of the Aggregator is calculated as in
Eq. 5 below, where 𝑆is the set of LFEs selected by the Aggregator
to contribute at timeslot 𝑡.
𝑓𝑙𝑒𝑥𝐴𝑔𝑔(𝑡) =
∑︁
∀𝑠∈𝑆
𝑓𝑙𝑒𝑥𝐿𝐹𝐸𝑠(𝑡)
(5)
3.4
Selection mechanisms
A key problem our framework addresses is the formation of efficient LFEs cooperatives to participate in the flexibility trading. To
facilitate this in an impartial manner, the Aggregator first ranks
the LFEs using certain scoring functions. All our proposed scoring
methods calculate the 𝑆𝑐𝑜𝑟𝑒𝐿𝐹𝐸𝑖for each 𝐿𝐹𝐸𝑖of the Aggregator,
regardless of their prior participation in the latest flexibility tradings of the Aggregator. The Aggregator needs to score the LFEs
regularly to have accurate information regarding the performance
of every LFE it controls. Additionally, it is possible that during
some specific periods of the year, the accuracy of the flexibility
predictions can fluctuate [5], so this can also be an essential factor
in the aggregator’s decision process.
In our experiments, the Aggregator selects the LFEs with the
𝐿𝐹𝐸𝑖scores that exceed an Aggregator-specified threshold, in order

---


### Page 5

A Novel Multiagent Flexibility Aggregation Framework
Stavros Orfanoudakis and Georgios Chalkiadakis
to calculate its 𝑓𝑙𝑒𝑥𝐴𝑔𝑔(𝑡) flexibility at time 𝑡. We now present our
scoring mechanisms in detail.
3.4.1
Simple Selection mechanism. The first selection mechanism
we developed uses the Mean Absolute Error (MAE) of the g
𝑓𝑙𝑒𝑥𝐿𝐹𝐸𝑖
flexibility prediction. Specifically, for an 𝐿𝐹𝐸𝑖that estimates its
flexibility for the next 𝑘hours, we calculate the MAE as in Eq. 6,
Similarly, we define the average flexibility of an LFE as in Eq. 7.
𝑀𝐴𝐸𝐿𝐹𝐸𝑖(𝑡) =
Í𝑘
𝑗=1 | g
𝑓𝑙𝑒𝑥𝐿𝐹𝐸𝑖(𝑗) −𝑓𝑙𝑒𝑥𝐿𝐹𝐸𝑖(𝑗)|
𝑘
(6)
𝐴𝑣𝑔𝐹𝑙𝑒𝑥𝐿𝐹𝐸𝑖(𝑡) =
Í𝑘
𝑗=1 |𝑓𝑙𝑒𝑥𝐿𝐹𝐸𝑖(𝑗)|
𝑘
(7)
Then, we calculate the 𝑆𝑐𝑜𝑟𝑒𝐿𝐹𝐸𝑖(𝑡) for each 𝐿𝐹𝐸𝑖of the Aggregator by using Eq. 8. The first step is to divide the 𝑀𝐴𝐸𝐿𝐹𝐸𝑖(𝑡) by
the average actual flexibility, then we subtract that value from 1
to have a straightforward confidence percentage. Finally, to avoid
negative scores, we bound the score value, 𝑆𝑐𝑜𝑟𝑒𝐿𝐹𝐸𝑖(𝑡) ∈[0, 1].
𝑆𝑐𝑜𝑟𝑒𝐿𝐹𝐸𝑖(𝑡) = 𝑚𝑎𝑥

1 −
𝑀𝐴𝐸𝐿𝐹𝐸𝑖(𝑡)
𝐴𝑣𝑔𝐹𝑙𝑒𝑥𝐿𝐹𝐸𝑖(𝑡) , 0

(8)
Thus, the score is at maximum when the predictor is perfect (𝐿𝐹𝐸𝑖
has an MAE of 0). By contrast, the score is 0 when the predictions’
mean absolute error is worse than that of having a “dummy” predictor that always outputs 0 values, i.e., when the prediction MAE
is greater than the average flexibility. In the end, the aggregator
calculates the average score of 𝐿𝐹𝐸𝑖over a time window 𝑤of past
trading cycles (Eq. 9). Then the aggregator checks if the average
score 𝐴𝑣𝑔𝑆𝑐𝑜𝑟𝑒𝐿𝐹𝐸𝑖(𝑡) of 𝐿𝐹𝐸𝑖is over the desired threshold 𝜏. The
central concept of this metric is to get a simple and easy-to-compute
confidence percentage so that we can use it as a “naive” selection
method to compare with other, more sophisticated solutions.
𝐴𝑣𝑔𝑆𝑐𝑜𝑟𝑒𝐿𝐹𝐸𝑖(𝑡) =
Í𝑡
𝑙=𝑡−𝑤𝑀𝐴𝐸𝐿𝐹𝐸𝑖(𝑙)
𝑤
(9)
3.4.2
Continuous Ranked Probability Score (CRPS). The second
selection mechanism we deployed uses the Continuous Ranked
Probability Score (CRPS) [15], which assesses the accuracy of a
probabilistic prediction over the actual occurrence. CRPS has been
previously used for virtual power plant formation [41], and we use
it in our aggregator framework to score the LFEs predictions aiming
to optimize aggregator profits. CRPS is a strictly proper scoring rule,
meaning that the expected score is maximized only if predictors
accurately report their expectation over the prediction error they
can potentially make [15]. CRPS has been shown to incentivize
energy suppliers to be truthful and accurate [41], and we use it here
to incentivize truthful and accurate LFE flexibility predictions.
With the Simple Selection mechanism, the LFEs only had to send
their flexibility predictions to the aggregator. When using the CRPS
Selection mechanism, LFEs also need to provide the uncertainty over
the prediction error, and are rewarded accordingly: estimates that
are both accurate and highly confident will be the ones achieving
higher CRPS scores. The 𝐶𝑅𝑃𝑆𝐿𝐹𝐸𝑖(𝑡) is defined as follows:
𝐶𝑅𝑃𝑆𝑖(𝑡) = 𝜎(𝑡)
 1
√𝜋−2𝜙
𝑒𝑖(𝑡)
𝜎(𝑡)

−𝑒𝑖(𝑡)
𝜎(𝑡) (2Φ
𝑒𝑖(𝑡)
𝜎(𝑡)

−1)

(10)
where 𝜙and Φ denote the probability density and the cumulative
distribution function of a standard Normal variable. In our case, 𝑒𝑖
is the relative prediction error, as shown in Eq. 11.
𝑒𝑖(𝑡) = 𝑓𝑙𝑒𝑥𝐿𝐹𝐸𝑖(𝑡) −g
𝑓𝑙𝑒𝑥𝐿𝐹𝐸𝑖(𝑡)
g
𝑓𝑙𝑒𝑥𝐿𝐹𝐸𝑖(𝑡)
(11)
(which we ensure to take values in [-1,1]). Additionally, along
with every prediction, the LFEs also send a Normal distribution
N (0, 𝜎(𝑡)2) to describe their uncertainty over their error, where
𝜎(𝑡) changes over time according to the LFEs uncertainty on the
predictions. (We assume, as in [41], that random errors, over a long
enough period, will be normally distributed around a mean of 0.)
𝐴𝑣𝑔𝑆𝑐𝑜𝑟𝑒𝐿𝐹𝐸𝑖(𝑡) =
Í𝑡
𝑙=𝑡−𝑤𝐶𝑅𝑃𝑆𝑖(𝑙)
𝑤
(12)
Similarly to the Simple Selection mechanism, the aggregator calculates the average score of each 𝐿𝐹𝐸𝑖over a time window 𝑤resembling past trading cycles (Eq. 12). Then the aggregator checks
if the average score of 𝐿𝐹𝐸𝑖is over a threshold 𝜏.
3.4.3
Reinforcement Learning: DQN. The final selection mechanism we developed deploys the celebrated Q-Networks (DQN) [30]
RL algorithm. We formulate the aggregator’s decision-making problem as a decision process, aiming to find the action with the highest
Q-value—corresponding to the long-term utility of taking a (selection) action, i.e., selecting a set of LFEs at this time step. We
assume a continuous state-space defined via providing as inputs
the 𝐶𝑅𝑃𝑆𝐿𝐹𝐸𝑖(𝑡) and the g
𝑓𝑙𝑒𝑥𝐿𝐹𝐸𝑖(𝑡) for every LFE of the aggregator; and define a discrete action-space containing all the different
possible selections of LFEs, using one-hot encoding. For example,
for 𝑛LFEs, there will be 𝑛bits of information, with 1 meaning the
LFE was selected, and 0 the opposite, so when the aggregator selects
among 𝑛LFEs, the action-space will have 2𝑛possible actions.
N
Dense 
Layer
64 
Dropout
Layer
RELU
Dense 
Layer
128 
Dropout
Layer
RELU
Dense 
Layer
256 
Dropout
Layer
RELU
Dense 
Layer
528 
Dropout
Layer
RELU
Dense 
Layer
2 
n
Flexible Load 
offered x n
CRPS x n
Figure 2: The architecture of the Reinforcement Learning
model used for the selection of the best LFE cooperative.
DQN is a value-based method that does not store any explicit
policy but only a value function in the form of a deep neural network, hence the policy is implicit and can be derived directly from
the neural network as the action with the highest value. In Fig.2,
we can see our neural network architecture. We used five fullyconnected layers with increasing nodes, so we could better handle
this complex optimization problem. Also, we put three "Drop-Out"
layers followed by rectified linear activation units (Re LU) to address
the randomness of the samples during training.
Two reward functions were developed for the training of the
DQN model. The goal of the first reward function is to maximize

---


### Page 6

A Novel Multiagent Flexibility Aggregation Framework
Stavros Orfanoudakis and Georgios Chalkiadakis
the profits of the aggregator during the evaluation time (Eq. 13). 𝑍
is a normalization constant that keeps the reward values closer to
0, but without an upper bound. The term 𝑉𝐺𝑟𝑖𝑑,𝐴𝑔𝑔(𝑡) refers to the
Grid payments towards the Aggregator for the flexibility trading it
has completed in timeslot 𝑡.
𝑅𝑒𝑤𝑎𝑟𝑑1(𝑡) =
𝑉𝐺𝑟𝑖𝑑,𝐴𝑔𝑔(𝑡)
𝑍
(13)
The second reward function we tested tries to balance the profits
of both the Aggregator and the LFEs (Eq. 14). This function takes
values in the [0, 1] interval. Here too, 𝐽is the set of LFEs selected to
participate in the aggregator’s latest flexibility trades, and 𝑆is a set
comprised of every LFE in the aggregator. We define 𝑉𝐴𝑔𝑔,𝐿𝐹𝐸𝑖(𝑡)
to refer to Aggregator payments to each 𝐿𝐹𝐸𝑖for participating in
its flexibility trading. Also, we define 𝑉𝐺𝑟𝑖𝑑,𝐿𝐹𝐸𝑖(𝑡) to refer to the
payments received by 𝐿𝐹𝐸𝑖at 𝑡while trading flexibility directly
with the Grid (when not selected by the Aggregator in timeslot 𝑡).
𝑅𝑒𝑤𝑎𝑟𝑑2(𝑡) =
𝑉𝐺𝑟𝑖𝑑,𝐴𝑔𝑔(𝑡)
𝑉𝐺𝑟𝑖𝑑,𝐴𝑔𝑔(𝑡) + Í
∀𝑖∈{𝑆−𝐽} 𝑉𝐺𝑟𝑖𝑑,𝐿𝐹𝐸𝑖(𝑡)
(14)
3.5
Pricing Mechanisms
Another problem our framework addresses is the distribution of
the aggregators’ profits to each individual LFE. We have deployed
two different pricing mechanisms inspired by previous studies. At
first, using these mechanisms, we calculate the payment from the
energy markets to the aggregator for trading its flexibility and then
payments by the aggregator to its LFEs. The (per KWh) price of
the traded energy in the markets at timeslot 𝑡is denoted as 𝑝(𝑡).
As mentioned earlier, Power TAC simulates the demand and supply
of a day-ahead wholesale market, which means that the price of
the KWh, denoted as 𝑝(𝑡) below, changes dynamically through the
course of the simulations.
3.5.1
Prediction Accuracy mechanism. Our first pricing mechanism
calculates the payments based only on “point estimates” of the
accuracy of the flexibility predictions (i.e., no uncertainty-related
distribution is reported), as in [9]. The more accurate the flexibility
estimators, the higher the payments it awards them.
To begin, Eq. 15 shows how the Aggregator is rewarded for
trading its flexibility in the energy markets.
𝑉𝐺𝑟𝑖𝑑,𝐴𝑔𝑔(𝑡) =
𝑙𝑜𝑔|𝑓𝑙𝑒𝑥𝐴𝑔𝑔(𝑡)| · 𝑓𝑙𝑒𝑥𝐴𝑔𝑔(𝑡)
1 + 𝛼· 𝑒𝐴𝑔𝑔(𝑡)𝛽
· 𝑝(𝑡)
(15)
The logarithmic term increases with the provided flexibility. This
incentivizes the Aggregator to include a large number of LFEs in its
offers. At the same time, the Aggregator has to proceed in its LFEs
selection with caution, as its flexibility prediction error, denoted
by 𝑒𝐴𝑔𝑔and calculated as in Eq. 11, plays a role in its final reward:
notice that the parameters of the denominator resemble a bellshaped function, so the value is maximized when the prediction
error is zero. Parameters 𝛼and 𝛽determine the exact shape of the
curve [9]; in our experiments, we set 𝛼= 1.6 and 𝛽= 4. The LFEs
not selected by the Aggregator trade directly with the Grid, and are
also rewarded according to Eq. 15 by swapping the terms 𝑒𝐴𝑔𝑔(𝑡)
with 𝑒𝐿𝐹𝐸𝑖(𝑡) and 𝑓𝑙𝑒𝑥𝐴𝑔𝑔(t) with 𝑓𝑙𝑒𝑥𝐿𝐹𝐸𝑖(t).
After the Aggregator is paid, it distributes the profits to the
contributing LFEs. Eq. 16 displays the pricing function used to
distribute 𝑉𝐺𝑟𝑖𝑑,𝐴𝑔𝑔to the LFEs based on their prediction error 𝑒𝑖.
𝑉𝐴𝑔𝑔,𝐿𝐹𝐸𝑖(𝑡) =
𝑍
1 + 𝛼· 𝑒𝑖(𝑡)𝛽·
𝑓𝑙𝑒𝑥𝑖(𝑡)
𝑓𝑙𝑒𝑥𝐴𝑔𝑔(𝑡) · 𝑉𝐺𝑟𝑖𝑑,𝐴𝑔𝑔(𝑡)
(16)
The term 𝑓𝑙𝑒𝑥𝑖(𝑡)/𝑓𝑙𝑒𝑥𝐴𝑔𝑔(𝑡) represents the flexibility contribution
percentage of the 𝐿𝐹𝐸𝑖to the Aggregator. Also, 𝑍is a normalization
parameter calculated to split the payment to every LFE completely.
One can adjust 𝑍to allow for some portion of the total payment to
be withheld by the Aggregator.
3.5.2
CRPS based mechanism. The second pricing mechanism [41]
uses the CRPS score. This mechanism encourages the formation of
larger LFE cooperatives while giving incentives for accurate and
truthful flexibility predictions. A key difference with the Prediction
Accuracy-only pricing mechanism, is that the CRPS-based mechanism can be more forgiving to low-accuracy predictors. This is
because LFEs also provide their flexibility predictions’ uncertainty
distributions, accounted for in their CRPS scores (see Sec. 3.4.2).
The "Grid-to-Aggregator" payment shown in Eq. 17 is calculated
similarly to the previous mechanism. However, the accuracy factor
is the aggregator’s CRPS value (normalized to [0, 1] similarly to
what is done in [40, 41]) instead of a bell-shaped function.
𝑉𝐺𝑟𝑖𝑑,𝐴𝑔𝑔(𝑡) = 𝐶𝑅𝑃𝑆𝐴𝑔𝑔(𝑡)·𝑙𝑜𝑔|𝑓𝑙𝑒𝑥𝐴𝑔𝑔(𝑡)|·𝑓𝑙𝑒𝑥𝐴𝑔𝑔(𝑡)·𝑝(𝑡) (17)
Here too, the LFEs that were not selected by the aggregator use
Eq. 17 but with the relevant 𝐿𝐹𝐸𝑖terms to calculate their "Grid-toLFE" payment. After the aggregator is paid, it distributes the profits
to each selected LFE member (set 𝐽of LFEs) using Eq. 18.
𝑉𝐴𝑔𝑔,𝐿𝐹𝐸𝑖(𝑡) =
𝐶𝑅𝑃𝑆𝐴𝑔𝑔(𝑡) · 𝑓𝑙𝑒𝑥𝐿𝐹𝐸𝑖(𝑡) · 𝑉𝐺𝑟𝑖𝑑,𝐴𝑔𝑔(𝑡)
Í
∀𝑗∈𝐽
 𝐶𝑅𝑃𝑆𝐿𝐹𝐸𝑗(𝑡) · 𝑓𝑙𝑒𝑥𝐿𝐹𝐸𝑗(𝑡)
(18)
This pricing mechanism ensures that each participant is awarded
a weighted portion of the total payment based on their contribution
and their individual CRPS score. Additionally, the CRPS is helpful
because it shows how beneficial the LFE estimates were for the
total flexibility trading of the aggregator.
3.5.3
Simple Grid-to-Aggregator payment. The use of CRPS in pricing mechanisms (Sec. 3.5.2) has been proposed in Smart Grid research because CRPS promotes predictors’ truthfulness and accuracy, punishing as it does untruthful and inaccurate predictors,
irrespective of their size [40, 41]. However, currently the CRPS
mechanism is not utilized for the calculation of payments in realworld energy trading. Instead, modern energy markets use simple
mechanisms that are exclusively based on the final flexibility contribution, and not on the accuracy of the prediction [12]. The standard
Grid payments are calculated (Eq. 19) using the promised (predicted)
flexibility g
𝑓𝑙𝑒𝑥𝑖, the actual volume of delivered flexibility, 𝑓𝑙𝑒𝑥𝑖, the
pre-agreed electricity price 𝑝(𝑡), and the current (at delivery) electricity price 𝑝𝑐(𝑡). The difference between the predicted and the
actual flexibility is defined as 𝑓𝑙𝑒𝑥diff (𝑡) = 𝑓𝑙𝑒𝑥𝑖(𝑡) −g
𝑓𝑙𝑒𝑥𝑖(𝑡).

---


### Page 7

A Novel Multiagent Flexibility Aggregation Framework
Stavros Orfanoudakis and Georgios Chalkiadakis
𝑉𝐺𝑟𝑖𝑑,𝑖(𝑡) =
(
𝑓𝑙𝑒𝑥𝑖(𝑡) · 𝑝(𝑡)
𝑓𝑙𝑒𝑥diff (𝑡) ≤0
g
𝑓𝑙𝑒𝑥𝑖(𝑡) · 𝑝(𝑡) + 𝑓𝑙𝑒𝑥diff (𝑡) · 𝑝𝑐(𝑡)
𝑓𝑙𝑒𝑥diff (𝑡) > 0
(19)
With this payment type, the Aggregator is rewarded with a preagreed electricity price 𝑝(𝑡) when it delivers (up to) a promised
amount of flexibility at 𝑡timeslot; and is paid according to the
current energy price for any additional flexibility amount it delivers.
4
EXPERIMENTAL EVALUATION
Here evaluate the performance of the LFEs and the Aggregator
in various scenarios formulated to test different aspects of our
framework. We used five different LFE selection methods, with four
variants each, combining static vs. dynamic LFE accuracy, and CRPS
vs. Simple Grid-to-Aggregator payment.
LFEs Selected
LFEs not Selected
LFEs Selected
The pricing mechanism 
depends on the method:
1. Split based on Prediction 
Accuracy mechanism
2,3,5. Split using CRPS 
mechanism 
Energy Markets
Aggregator
LFEs
Select LFEs to participate in the 
Aggregator​
LFEs not Selected
Monitor the production and 
consumption of the DER
Predict the total Flexibility of 
the DERs for the next 24 hours
Sum up the individual LFEs' 
Flexibilities into the total 
predicted Flexibility​
Participate in the flexibility 
trades using the total Flexibility 
predictions
Simulate the market 
demand and supply 
prices
Calculate Payment 
using the actual 
Flexibility delivered
Split the profits to the selected 
LFEs 
Get Paid
Calculate the new
Scores for all LFEs
Calculate Reward and Train the
 RL-model using data from the 
current round
Monitor the actual 
Flexibility delivered 
and wait for the next 
24hours to pass
This action node is only 
activated during DQN 
Selection method
The LFE selection mechanism depends on 
the method:
1. Select based on the Simple Selection
2. Select using CRPS
3. Select using the DQN RL model
4. No LFE is selected
5. All LFEs are selected
Figure 3: Trading flexibility via various methods.
To lay the ground for our experiments, we first provide a detailed
activity diagram (Fig. 3) depicting the actions taken by the LFEs and
the Aggregator to trade flexibility with the Grid over a 24-timeslot
period starting from 12:00 pm every day. As we can see, the main
activity flow remains the same for all experimental methods, but
some critical variations will be discussed explicitly later.
First, the LFEs monitor and process the production and consumption data of all their DERs, to train their flexibility estimators. At
the start of every trading cycle, the LFEs deliver their flexibility
predictions for the next 24 hours to the Aggregator, to trade in
the day-ahead wholesale market. Then the Aggregator chooses
which LFEs to participate in the upcoming flexibility trades using a
method-specific selection mechanism. Afterward, the Aggregator
calculates its total flexibility estimate and participates in the flexibility tradings. At the same time, Power TAC simulates the demand
and supply prices, so that energy market participants can buy or sell
energy. Once the day-ahead market closes, Power TAC continues to
monitor the actual flexibility delivered until the market opens again.
Then, it calculates the aggregator’s payment based on the delivered
flexibility and the prediction error, as seen in Section 3.5. We make
the assumption that all energy offered to the Grid is always bought.
After the Aggregator has received its payment, it distributes the
profits to the LFEs via a pricing mechanism. Meanwhile, the LFEs
not selected by the Aggregator have also traded their flexibility
directly with the energy markets. The final step for the Aggregator
is to assess the prediction accuracy of every LFE, selected or not,
by re-calculating the Simple Score and the CRPS metrics. After each
trading cycle, one has to re-evaluate to account for possibly fluctuating LFE prediction performance, so the aggregator will know
which LFEs to select for subsequent trades.
The total number of DERs simulated in Power TAC resembles that
of a small city; hence, there are considerable amounts of available
flexible loads to trade: specifically, a total of 13 MWh of renewable
energy can be produced, and a total of 14 MWh can be consumed
at peak hours respectively. Also, there is a total storage capacity
of 7.5 MWh, where BESS are accountable for 2.5 MWh while the
rest derives from EVs. We divided the Power TAC’s DER assets randomly into twelve heterogeneous LFEs consisting of various DER
assets such as solar panels, BESS, electric vehicles, households, and
interruptible consumption users. The LFE heterogeneity makes
the simulations much more realistic since every LFE has different
attributes. Some of these attributes refer to the electricity consumption/production profiles and the total storage capacity.
We use Power TAC’s day-ahead wholesale market to trade flexibility in our experiments. Specifically, a simulated day is divided
into 24 timeslots resembling the hours of the day. Like in many real
day-ahead energy markets, in our experiments all offers should be
submitted before 12:00 pm, so there is a need for each LFE to provide
the Aggregator with at least 24-hour-ahead flexibility predictions.
The LFEs’ flexibility predictions are the outcome of a Gaussian
random process per 𝐿𝐹𝐸𝑖, G(𝜇𝑖, 𝜎𝑖), with 𝜇𝑖being the actual 𝐿𝐹𝐸𝑖
flexibility (𝑓𝑙𝑒𝑥𝐿𝐹𝐸𝑖), and variance 𝜎𝑖an 𝐿𝐹𝐸𝑖-specific parameter.
4.1
Methods Instantiation
As mentioned, we have formulated five methods corresponding to
different LFE selection and pricing mechanisms (distributing the
Aggregator’s profits to the LFEs):
4.1.1
Using Simple Selection. The first method uses the Simple
Selection mechanism to decide which LFEs to participate in the
aggregator. In detail, the aggregator calculates the average score of
𝐿𝐹𝐸𝑖over a time period 𝑤= 3 of past trading cycles as displayed
in Sec. 3.4.1. In our experiments, we set threshold 𝜏= 0.7. Also, we
use the Prediction Accuracy pricing mechanism for this method as
described in Sec. 3.5.1 since we assume that LFEs in this setting
are unable to provide distributions over their prediction error. We
employed the CRPS Pricing mechanism for all other experimental
methods since it provides incentives for truthful and reliable LFE
predictions [40, 41], which makes it a perfect fit for our framework.
4.1.2
CRPS Selection. The second method uses the more sophisticated CRPS Selection. Here too, we calculate the average CRPS

---


### Page 8

A Novel Multiagent Flexibility Aggregation Framework
Stavros Orfanoudakis and Georgios Chalkiadakis
score of a time period 𝑤= 3 and check if the final CRPS score is
higher than a specific threshold (see Sec. 3.4.2). Higher (normalized
to [0, 1]) CRPS values represent LFEs with higher prediction accuracy, while lower CRPS values correspond to less accurate LFEs.
Furthermore, we set the threshold 𝜏= 0.77 since this was observed
empirically to achieve similar selection rates (numbers of LFEs
selected per timeslot) with the previous mechanism.
4.1.3
DQN Selection. This method evaluates DQN Selection using
two different reward functions (see Sec. 3.4.3). Note that here the
aggregator also has to calculate the RL reward and train the RL
selection model using information from the latest trading cycle.
4.1.4
Singleton LFEs. In this method, as the name suggests, every
LFE interacts directly with the energy markets using the CRPS
Pricing mechanism. This use case acts as the first baseline method
depicting how the LFEs would have performed if they had never
participated in our aggregator framework.
4.1.5
All LFEs. Here all LFEs participate in the Aggregator without
any selection criteria. This use case mirrors the current state-ofthe-art aggregation scenario, in which an aggregator incorporates
all available resources at hand.
4.2
Experimental Scenarios
We composed four experimental scenarios to test the performance
of our framework in different use cases. As depicted in Table 1, the
scenarios are dependent: (a) on the stability of the LFE’s prediction
accuracy throughout the simulations, (b) on how the Aggregator
agent is compensated for providing flexibility services to the Grid.
LFE Accuracy
Grid-to-Aggregator
Payment
Scenarios
Static
Dynamic
CRPS
Simple
Scenario 1
✓
✓
Scenario 2
✓
✓
Scenario 3
✓
✓
Scenario 4
✓
✓
Table 1: Configuration of the four experimental scenarios.
We have formed 12 LFEs consisting of various heterogeneous
DERs for our experiments. When the LFE prediction accuracy is
“Static”, the prediction variance 𝜎𝑖of every 𝐿𝐹𝐸𝑖is constant during
the simulations. However, in the real world, the accuracy of flexibility predictions can vary depending on the weather, season, and
type of DER. The “Dynamic” LFE accuracy configuration models a
realistic setting in which the variance 𝜎𝑖of every 𝐿𝐹𝐸𝑖fluctuates
during the simulations. In particular, at each timeslot, the variance
of the flexibility prediction accuracy of each LFE changes by +/-
0.001, following a stochastic trajectory whose direction is generally
downwards for good predictors or upwards for bad predictors.
4.3
Experimental Results
We now present our results in detail. The results are the averages
of 30 simulations with different properties and 2000 timeslots each.
The code for the aggregator framework and all experimental results
will be publicly available online upon acceptance.
4.3.1
Scenario 1: Static LFE accuracy and CRPS Grid-to-Aggregator
Payment. The first scenario investigated in this work maintains the
variance 𝜎𝑖of every 𝐿𝐹𝐸𝑖constant during the simulations and utilizes the CRPS Grid-to-Aggregator payment (Eq. 17). In Fig. 4, 𝐿𝐹𝐸1
resembles the best flexibility predictor with 𝜎1 ≈0, progressing
gradually up to the worse predictor, 𝐿𝐹𝐸12 with 𝜎12 ≈1.
Figure 4: “Scenario 1”: Comparison of the average payment(€)
per MWh sold of every LFE for all methods.
Fig. 4 shows the average flexibility selling price for all the LFEs
for different methods where LFEs’ selection rules differ. At first,
we can notice that the first four LFEs, which are the better predictors, are selling at a higher price than the rest, a result of both the
prediction accuracy and the amount of flexibility they traded. The
most rewarding methods for the “best predictors” are the Simple
Selection or the CRPS ones. The most profitable methods for the
“worse predictors” are when every LFE participates in the Aggregator without any selection mechanism; in this case, they are able
to realize higher average payments due to the high total flexibility
provided by the Aggregator as a whole, despite the fact that these
payments are significantly lower than those of the better predictors
(due to CRPS “punishments”) even in this method.
To complete this analysis, it is necessary to understand how
often the LFEs were selected to participate in the Aggregator, by
observing their flexibility selling channel (Fig. 5). We can see that
the Simple and CRPS Selection methods choose the most accurate
LFE predictors (𝐿𝐹𝐸1,2,3,4,5) to participate and trade flexibility with
the Aggregator; while the rest are not selected because of their low
accuracy. In the DQN Selection methods, most LFEs are participating
in the Aggregator, with DQN being able to distinguish somewhat
better among medium and bad LFE predictors when the second
reward function (𝑅𝑒𝑤𝑎𝑟𝑑2) is used (in which case the “medium”
predictors do get selected to participate in Aggregator trade).
In summary, it is more profitable for the best LFEs to be chosen
via the Simple and CRPS Selection, because these mechanisms reward
truthful and reliable LFEs more. By contrast, less accurate LFEs
receive higher payments when there is no selection mechanism in
place (“All LFEs participate in the Aggregator” method).
4.3.2
Scenario 2: Dynamic LFE accuracy and CRPS Grid-to-Aggregator Payment. The “Dynamic LFE accuracy” use case models a more
realistic setting in which the “worse predictor” LFEs gradually
improve while the best-performing ones degrade. It is obvious in

---


### Page 9

A Novel Multiagent Flexibility Aggregation Framework
Stavros Orfanoudakis and Georgios Chalkiadakis
Figure 5: “Scenarios 1 & 3”: Comparing the flexibility selling
channel (directly to Grid or via the Aggregator).
Fig. 6 that the payments attained by the LFEs are, in general, lower
in this dynamic scenario. The CRPS and Simple Selection methods
result in the best average payments for almost every LFE. Only the
𝐿𝐹𝐸𝑠6,7,8 had another method that was better than the first two
selection mechanisms. In this use case, DQN Selection results in LFE
payments that are, in many cases, comparable to those of the first
two methods. However, this is not due to DQN being able to adapt
to the dynamically changing capabilities of the agents. Indeed, as
seen in Fig. 7, DQN generally selected the same LFEs to participate;
while Simple Selection and CRPS are apparently able to detect the
fluctuations in LFEs’ prediction performance and now give much
more participation chances to almost all LFE agents.
Figure 6: “Scenario 2”: Comparison of the average payment(€)
per MWh sold of every LFE.
Finally, we report that for “Scenario 1” the Aggregator receives
average payments (per MWh) of 151€ using methods 1 and 2, while
it only gets 120€ per MWh in the rest. Similarly, for “Scenario 2”
Figure 7: “Scenarios 2 & 4”: Comparing the flexibility selling
channel (directly to Grid or via the Aggregator).
the aggregator gets an average payment of 168€ per MWh using
the first two methods and only 120€ for the rest. These values
highlight the fact that the Aggregator is able to make a higher
profit per MWh when selecting the most accurate LFEs predictors
via either Simple or CRPS selectors; and this is the case even in
dynamic settings, where the total energy sold via the Aggregator is
lower (specifically ∼2 GWh for both scenarios 1 & 2) than in the
static setting (∼3 GWh). These values make intuitive sense since
with method 5, all LFEs participate in the aggregator, and the DQN
method selects most LFEs to participate in the Aggregator most of
the time (cf. Fig. 5 and Fig. 7); while Simple Scoring and CRPS are
more selective, thus the total amount of Aggregator flexibility (and
thus its average payments) is higher. Apart from these mechanisms’
apparent positive effect on Aggregator efficiency, we note again
that the use of selection mechanisms that incentivize reliable LFEs,
thus promoting Grid stability, results in higher average payments
for those LFEs (while all available flexibility is traded in any case).
Overall, in both scenarios 1 and 2, we can see that it is not efficient
for the LFEs to trade directly with the Grid, judging by the results
of the “Singleton LFEs” method (Fig. 4, Fig. 6). Furthermore, it is
clear from our figures that CRPS Selection leads to higher payments
for selected accurate LFEs. Also, the performance of the Simple
Selection method is comparable to that of CRPS, both for the static
and the dynamic settings. This, as explained in the introduction,
marks an interesting trade-off between simplicity and guaranteed
truthfulness of the selection mechanism to be used.
4.3.3
Scenario 3: Static LFE accuracy and Simple Grid-to-Aggregator
Payment. We also conducted experiments simulating the way the
existing aggregators are paid by the Grid when trading flexibility—
i.e., using the Simple Grid-to-Aggregator Payment (Eq. 19).

---


### Page 10

A Novel Multiagent Flexibility Aggregation Framework
Stavros Orfanoudakis and Georgios Chalkiadakis
Figure 8: “Scenario 3”: Comparison of the average payment(€)
per MWh sold of every LFE.
Fig. 8 presents the average payment per MWh for every LFE.3
This figure verifies the previous findings, clearly depicting the superiority of the CRPS Selection method deployed by our framework.
The Simple Selection method is the runner-up accumulating an
average payment of a few more euros for 𝐿𝐹𝐸3 and 𝐿𝐹𝐸4, while
in every other case, it scores lower than CRPS (albeit by a small
margin). The “Singleton LFEs” baseline method is the third most
efficient option, ranking, however, consistently and clearly lower
than the first two. Notice that it can “score” 20 euros less than CRPS
Selection, a significant difference since each LFE sells many MWh.
The remaining methods rank much lower, with a clearly poorer
performance varying up to 30 euros less than CRPS Selection.
The selection percentages of each LFE by the Aggregator agent
remain the same with those of the“Static LFE Accuracy” (Sec. 4.3.1)
configuration (i.e., are as in Fig. 5), because we maintained the same
random seeds for the respective simulations. It was our intention
to ensure that the offered flexibility of each LFE remains the same
across different experiments so that we can fairly compare the
rankings (in terms of average payments) of the different selection
methods across the various scenarios.
4.3.4
Scenario 4: Dynamic LFE accuracy and Simple Grid-to-Aggregator Payment. Our final experimental scenario is one with “Dynamic” LFE prediction accuracy and Simple Grid-to-Aggregator Payments. Here, the selection percentages of each LFE by the Aggregator are as in Fig. 7). CRPS Selection again consistently results to
the highest average payment per MWh per LFE regardless of its
prediction accuracy (bar LFEs 1 and 12 for which it is tied with
Singleton LFEs). The Singleton LFEs method is a close runner-up,
with payments that range from a few to 10 euros lower. The Simple
Selection method is quite profitable too, rewarding LFEs on average
with 5 euros less per MWh than CRPS Selection. On the other hand,
the DQN Selection methods and, importantly, the All LFEs “traditional” Aggregator method (which essentially includes all available
DERs in the Aggregator, as is current practice in the industry) result
in average payments that are (at least) 30 euros lower per MWh.
3Note that the average payments of Scenarios 1 and 2 are not comparable with the
respective payments of Scenarios 3 and 4, since the Grid-to-Aggregator payments are
completely different (Eq. 17 and 19).
Figure 9: “Scenario 4”: Comparison of the average payment(€)
per MWh sold of every LFE.
The findings of the last two scenarios, in which the Grid pays our
Aggregator with a “simple” pricing mechanism that does not penalize flexibility prediction inaccuracies (Eq. 19) but only considers the
total flexibility delivered, are quite interesting. They demonstrate
that our aggregation framework, in particular when using the CRPS
Selection method, consistently achieves the highest average profit per
LFE, regardless of the LFEs’ prediction accuracy, and regardless of
its dynamic or static nature (cf. Fig. 8 and Fig. 9). Notice that the
aforementioned “simple” pricing mechanism is, in fact, used in the
current day-ahead electricity markets. Also, as mentioned, CRPS
Selection is the clear winner when compared with the currentlyin-use aggregation method that simply collects all available DERs’
flexibility. Therefore, these results indicate that our framework
using CRPS Selection can result in increased profits for LFEs (and
subsequently DERs), if applied in the current Grid.
5
CONCLUSIONS AND FUTURE WORK
In this work, we put forward a novel flexibility aggregation framework comprising a novel multiagent architecture along with various
(existing or novel) selection and pricing mechanisms. We conducted
a systematic experimental evaluation, using data from the highly
realistic Power TAC simulator which we extended to allow for the
incorporation of flexibility aggregators and related entities and
mechanisms. Our results show that our framework and methods
can successfully contribute to the effective integration of DERs in
the Grid, enabling them to increase their profits.
In terms of future work, we intend to experiment with alternative selection and pricing mechanisms; and to study scenarios
(readily supported by our framework) that allow LFEs to replace
inefficient DER assets. Moreover, it would be interesting to incorporate Aggregators that create more than one LFE cooperative,
potentially using different mechanisms for each depending on its
attributes. Finally, enhancing our framework with the ability to
include multiple Aggregators competing for the representation of
efficient LFEs, is also interesting future work.
REFERENCES
[1] Temitope Adefarati and Ramesh C. Bansal. 2016. Integration of renewable distributed generators into the distribution system: a review. Iet Renewable Power
Generation 10 (2016), 873–884.
[2] Charilaos Akasiadis and Georgios Chalkiadakis. 2016. Decentralized Large-Scale
Electricity Consumption Shifting by Prosumer Cooperatives. In Volume 285: ECAI

---


### Page 11

A Novel Multiagent Flexibility Aggregation Framework
Stavros Orfanoudakis and Georgios Chalkiadakis
2016. IOS Press Ebooks, The Netherlands, 175–183.
[3] Mattia Barbero, Cristina Corchero, Lluc Canals Casals, Lucia Igualada, and F.-
Javier Heredia. 2020. Critical evaluation of European balancing markets to enable
the participation of Demand Aggregators. Applied Energy 264 (2020).
[4] Peter Berrill, Anders Arvesen, Yvonne Scholz, Hans Christian Gils, and Edgar G
Hertwich. 2016. Environmental impacts of high penetration renewable energy
scenarios for Europe. Environmental Research Letters 11, 1 (jan 2016), 014012.
[5] Lisa Bosman and Seth Darling. 2016. Difficulties and recommendations for more
accurately predicting the performance of solar energy systems during the snow
season. In 2016 IEEE International Conference on Renewable Energy Research and
Applications (ICRERA). IEEE, „ 567–571.
[6] Zane Broka and K¯arlis Baltputnis. 2020. Handling of the Rebound Effect in
Independent Aggregator Framework. 2020 17th International Conference on the
European Energy Market (EEM) , (2020), 1–5.
[7] Francesco Carducci. 2017. Tools and Methods to study the integration of flexibility
assets in the future Smart Grid. Ph. D. Dissertation. Universit‘a Politecnica delle
Marche.
[8] Alberto Castelo-Becerra, Wente Zeng, and Mo-Yuen Chow. 2017. Cooperative
distributed aggregation algorithm for demand response using distributed energy
storage devices. 2017 North American Power Symposium (NAPS) , (2017), 1–6.
[9] Georgios Chalkiadakis, Valentin Robu, Ramachandra Kota, Alex Rogers, and
Nicholas R. Jennings. 2011. Cooperatives of Distributed Energy Resources for
Efficient Virtual Power Plants. In The 10th International Conference on AAMAS -
Volume 2 (Taipei, Taiwan) (AAMAS ’11). IFAAMAS, Richland, SC, 787–794.
[10] Can Dang, Xifan Wang, Chengcheng Shao, and Xiuli Wang. 2019. Distributed
generation planning for diversified participants in demand response to promote
renewable energy integration. Journal of Modern Power Systems and Clean Energy
, (2019), 1–14.
[11] Dominik Danner, Jan Seidemann, Michael Lechl, and Hermann de Meer. 2021.
Flexibility Disaggregation under Forecast Conditions. In Proceedings of the Twelfth
ACM International Conference on Future Energy Systems (Virtual Event, Italy)
(e-Energy ’21). Association for Computing Machinery, New York, NY, USA, 27–38.
https://doi.org/10.1145/3447555.3464851
[12] Flexible Power 2022.
Flexible Power Payment Mechanism.
https://www.
flexiblepower.co.uk/downloads/52
[13] Na Gai, Kaiping Xue, Peixuan He, Bin Zhu, Jianqing Liu, and Debiao He. 2020.
An Efficient Data Aggregation Scheme with Local Differential Privacy in Smart
Grid. 2020 16th International Conference on Mobility, Sensing and Networking
(MSN) , (2020), 73–80.
[14] Lazaros Gkatzikis, Iordanis Koutsopoulos, and Theodoros Salonidis. 2013. The
Role of Aggregators in Smart Grid Demand Response Markets. IEEE Journal on
Selected Areas in Communications 31 (2013), 1247–1257.
[15] Tilmann Gneiting and Adrian E. Raftery. 2007. Strictly Proper Scoring Rules,
Prediction, and Estimation. J. Amer. Statist. Assoc. 102 (2007), 359 – 378.
[16] Pulkit Goyal, Avinash Sharma, Shashank Vyas, and Rajesh Kumar. 2016. Customer
and aggregator balanced dynamic Electric Vehicle charge scheduling in a smart
grid framework. ICEPES , (2016), 276–283.
[17] Charles Ibrahim, Imad Mougharbel, Hadi Youssef Kanaan, Nivine Abou Daher,
Semaan Wadih Georges, and Maarouf Saad. 2022. A review on the deployment
of demand response programs with multiple aspects coexistence over smart grid
platform. Renewable and Sustainable Energy Reviews 162 (2022), 112446.
[18] Christos Iraklis, Joshua Smend, Ali Almarzooqi, and Ashot Mnatsakanyan. 2021.
Flexibility Forecast and Resource Composition Methodology for Virtual Power
Plants. ICECET , (2021), 1–7.
[19] Rune Hylsberg Jacobsen, Dominique Gabioud, Gillian Basso, Pierre-Jean Alet,
Armin Ghasem Azar, and Emad Samuel Malki Ebeid. 2015. SEMIAH: An Aggregator Framework for European Demand Response Programs. 2015 Euromicro
Conference on Digital System Design , (2015), 470–477.
[20] Malik Ali Judge, Asif Khan, Awais Manzoor, and Hasan Ali Khattak. 2022.
Overview of smart grid implementation: Frameworks, impact, performance and
challenges. Journal of Energy Storage 49 (2022), 104056.
[21] Yasin Kabalci. 2016. A survey on smart metering and smart grid communication.
Renewable & Sustainable Energy Reviews 57 (2016), 302–318.
[22] Wolfgang Ketter, John Collins, and Prashant P. Reddy. 2013. Power TAC: A
competitive economic simulation of the smart grid. Energy Economics 39 (2013).
[23] Alexandros-Michail Koufakis, Emmanouil S. Rigas, Nick Bassiliades, and Sarvapali D. Ramchurn. 2016. Towards an optimal EV charging scheduling scheme
with V2G and V2V energy transfer. Smart Grid Comm , (2016), 302–307.
[24] Merla Kubli and Patrizio Canzi. 2021. Business strategies for flexibility aggregators to steer clear of being “too small to bid”. Renewable & Sustainable Energy
Reviews 143 (2021).
[25] Klaus Kursawe, George Danezis, and Markulf Kohlweiss. 2011. Privacy-Friendly
Aggregation for the Smart-Grid. In PETS. Springer Berlin Heidelberg, Berlin,
Heidelberg, 175–191.
[26] Ioannis C Lampropoulos, Tarek Alskaif, Jelle Blom, and Wilfried G.J.H.M. van
Sark. 2019. A framework for the provision of flexibility services at the transmission and distribution levels through aggregator companies. Sustainable Energy,
Grids and Networks , (2019), 175–191.
[27] Fernando Lezama, João P. Soares, Pablo Hernandez-Leal, Michael Kaisers, Tiago
Pinto, and Zita A. Vale. 2019. Local Energy Markets: Paving the Path Toward
Fully Transactive Energy Systems. IEEE Transactions on Power Systems 34 (2019).
[28] Sleiman Mhanna, Archie C. Chapman, and Gregor Verbi. 2016. A Fast Distributed
Algorithm for Large-Scale Demand Response Aggregation. IEEE Transactions on
Smart Grid 7 (2016), 2094–2107.
[29] Ashot Mnatsakanyan, Hamad Albeshr, A. M. Al Marzooqi, and Endika Bilbao.
2020. Blockchain-Integrated Virtual Power Plant Demonstration. 2nd International Conference on Smart Power & Internet Energy Systems , (2020), 172–175.
[30] Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Alex Graves, Ioannis
Antonoglou, Daan Wierstra, and Martin A. Riedmiller. 2013. Playing Atari
with Deep Reinforcement Learning. Ar Xiv abs/1312.5602 (2013), ,.
[31] Bijay Neupane, Laurynas Siksnys, Torben Bach Pedersen, Rikke Hagensby,
Muhammad Aftab, Bradley Eck, Francesco Fusco, Robert Gormally, Mark Purcell,
Seshu Tirupathi, Gregor Cerne, Saso Brus, Ioannis Papageorgiou, Gerhard Meindl,
and Pierre Roduit. 2022. GOFLEX: Extracting, Aggregating and Trading Flexibility
Based on Flex Offers for 500+ Prosumers in 3 European Cities [Operational Systems Paper]. In Proceedings of the Thirteenth ACM International Conference on Future Energy Systems (Virtual Event) (e-Energy ’22). Association for Computing Machinery, New York, NY, USA, 361–373. https://doi.org/10.1145/3538637.3538865
[32] Ozge Okur. 2021. Aggregators’ business models for flexibility from electricity
consumers. Ph. D. Dissertation. Delft University of Technology.
[33] Ozge Okur, Petra W. Heijnen, and Zofia Lukszo. 2021. Aggregator’s business
models in residential and service sectors: A review of operational and financial
aspects. Renewable and Sustainable Energy Reviews 139 (2021), 110702.
[34] Stavros Orfanoudakis and Georgios Chalkiadakis. 2023. A Novel Aggregation
Framework for the Efficient Integration of Distributed Energy Resources in the
Smart Grid. In Proceedings of the 2023 International Conference on Autonomous
Agents and Multiagent Systems (London, United Kingdom) (AAMAS ’23). International Foundation for Autonomous Agents and Multiagent Systems, Richland,
SC, 2514–2516.
[35] Alvaro Perez-Diaz, Enrico Gerding, and Frank Mc Groarty. 2018. Coordination of
electric vehicle aggregators: a coalitional approach. In 17th International Conference on Autonomous Agents and Multiagent Systems, AAMAS 2018, Vol. 1. International Foundation for Autonomous Agents and Multiagent Systems (IFAAMAS),
Southampton, 676–684.
[36] Alvaro Perez-Diaz, Enrico H. Gerding, and Frank Mc Groarty. 2018. Coordination
and payment mechanisms for electric vehicle aggregators. Applied Energy 212
(2018), 185–195.
[37] Sarvapali D. Ramchurn, Perukrishnen Vytelingum, Alex Rogers, and Nicholas R.
Jennings. 2012. Putting the ’smarts’ into the smart grid. Commun. ACM 55 (2012),
86 – 97.
[38] Tanuj Rawat, Khaleequr Rehman Niazi, Nikhil Gupta, and Sachin Sharma. 2019.
A Two Stage Interactive Framework for Demand Side Management in Smart Grid.
2019 IEEE 16th India Council International Conference (INDICON) , (2019), 1–4.
[39] Emmanouil S. Rigas, Sarvapali D. Ramchurn, and Nick Bassiliades. 2015. Managing Electric Vehicles in the Smart Grid Using Artificial Intelligence: A Survey.
IEEE Transactions on Intelligent Transportation Systems 16 (2015), 1619–1635.
[40] Valentin Robu, Georgios Chalkiadakis, Ramachandra Kota, Alex Rogers, and
Nicholas R. Jennings. 2016. Rewarding cooperative virtual power plant formation
using scoring rules. Energy 117 (2016), 19–28.
[41] Valentin Robu, Ramachandra Kota, Georgios Chalkiadakis, Alex Rogers, and
Nicholas R. Jennings. 2012. Cooperative Virtual Power Plant Formation Using
Scoring Rules. In AAAI, Vol. 117. IEEE, „ 19–28.
[42] Mir Mohammad Reza Sahebi, Esmaeil Abedini Duki, Mohsen Kia, Alireza Soroudi,
and Mehdi Ehsan. 2012. Simultanous emergency demand response programming and unit commitment programming in comparison with interruptible load
contracts. Iet Generation Transmission & Distribution 6 (2012), 605–611.
[43] Helen Sawall, Andreas Scheuriker, and Daniel Stetter. 2018. Flexibility Definition
for Smart Grid Cells in a Decentralized Energy System. In Proceedings of the 7th
International Conference on Smart Cities and Green ICT Systems (Funchal, Madeira,
Portugal). SCITEPRESS, Setubal, PRT, 130–139.
[44] Tim Schittekatte, Vincent Deschamps, and Leonardo Meeus. 2021. The Regulatory
Framework for Independent Aggregators. SSRN Electronic Journal 34 (2021).
[45] Miadreza Shafie-khah, Ehsan Heydarian-Forushani, Gerardo J. Osório, Fabio
A. S. Gil, Jamshid Aghaei, Mostafa Barani, and João P. S. Catalão. 2016. Optimal
Behavior of Electric Vehicle Parking Lots as Demand Response Aggregation
Agents. IEEE Transactions on Smart Grid 7 (2016), 2654–2665.
[46] Richard S. Sutton and Andrew G. Barto. 2005. Reinforcement Learning: An
Introduction. IEEE Transactions on Neural Networks 16 (2005), 285–286.
[47] Stylianos I. Vagropoulos, Dimitrios K. Kyriazidis, and Anastasios G. Bakirtzis.
2016. Real-Time Charging Management Framework for Electric Vehicle Aggregators in a Market Environment. IEEE Transactions on Smart Grid 7 (2016).
[48] Orlando Valarezo, Tomás Gómez, José Pablo Chaves-Avila, Leandro Lind, Mauricio Correa, David Ulrich Ziegler, and Rodrigo Escobar. 2021. Analysis of New
Flexibility Market Models in Europe. Energies 14, 12 (2021), ,.
[49] Emmanouil Valsomatzis, Torben Bach Pedersen, and Alberto Abelló. 2018. DayAhead Trading of Aggregated Energy Flexibility. In Proceedings of the Ninth

---


### Page 12

A Novel Multiagent Flexibility Aggregation Framework
Stavros Orfanoudakis and Georgios Chalkiadakis
International Conference on Future Energy Systems (Karlsruhe, Germany) (e-Energy
’18). Association for Computing Machinery, New York, NY, USA, 134–138. https:
//doi.org/10.1145/3208903.3208936
[50] Marina González Vayá and Göran Andersson. 2016. Self Scheduling of Plug-In
Electric Vehicle Aggregator to Provide Balancing Services for Wind Power. IEEE
Transactions on Sustainable Energy 7 (2016), 886–899.
[51] Peerapat Vithayasrichareon, G. Mills, and Iain Macgill. 2015. Impact of Electric Vehicles and Solar PV on Future Generation Portfolio Investment. IEEE
Transactions on Sustainable Energy 6 (2015), 899–908.
[52] Gaurav S. Wagh, Sahil Gupta, and Sumita Mishra. 2020. A distributed privacy
preserving framework for the Smart Grid. 2020 IEEE Power & Energy Society
Innovative Smart Grid Technologies Conference (ISGT) , (2020), 1–5.
[53] Kun Wang, Yunqi Wang, Xiaoxuan Hu, Yanfei Sun, Der-Jiunn Deng, Alexey V.
Vinel, and Yan Zhang. 2017. Wireless Big Data Computing in Smart Grid. IEEE
Wireless Communications 24 (2017), 58–64.
[54] Yingying Zheng, Berk Celik, Siddharth Suryanarayanan, Anthony A. Maciejewski,
Howard Jay Siegel, and Timothy M. Hansen. 2021. An aggregator-based resource
allocation in the smart grid using an artificial neural network and sliding time
window optimization. IET Smart Grid 4, 6 (2021), 612–622.
[55] Giulia De Zotti, S. Ali Pourmousavi, Juan Miguel Morales, Henrik Madsen, and
Niels Kjølstad Poulsen. 2019. Consumers’ Flexibility Estimation at the TSO Level
for Balancing Services. IEEE Transactions on Power Systems 34 (2019), 1918–1930.

---
