

---

Page 1

---

 
Decision Making: Applications in Management and Engineering, Volume 7, Issue 2 (2024) 355-379 
355 
 
 
Decision Making: Applications in 
Management and Engineering 
Journal homepage: www.dmame-journal.org    
ISSN: 2560-6018, eISSN: 2620-0104 
 
Finance-based Scheduling for Cash-flow Management of Maintenance 
Portfolios: Multi-objective Optimization Approach  
 
Ali Fares1, Ashraf Elazouni1*, Mubarak Al-Alawi1   
 
1 
Department of Civil and Architectural Engineering, Sultan Qaboos University, Al-Khoud 123, Muscat, Oman 
 
 
ARTICLE INFO 
ABSTRACT 
Article history: 
Received 10 March 2024 
Received in revised form 3 May 2024 
Accepted 15 May 2024 
Available online 27 May 2024 
Bridge agencies are often challenged to develop maintenance programs under 
given budgets. Numerous studies developed budget-allocation models for 
maintenance programs during defined planning horizons of multiple fiscal years 
while totally ignoring the crucial aspect of cash flow. The payment schedules 
(both timing and amount) for contractors might indicate agencies’ cash needs 
that exceed the available budgets during certain fiscal years, which create cash 
flow problems. While numerous finance-based scheduling (FBS) models were 
developed to manage cash flow for contractors, this function was totally 
overlooked for portfolio owners. Thus, this research reintroduces the FBS from 
the perspective of portfolio owners. A FBS model is developed to schedule the 
activities of the portfolio projects, utilize the schedules to define the payment 
schedules of projects’ contractors, calculate the agencies’ cash needs during the 
fiscal years, and utilize the multi-objective optimization algorithms of NSGA-II, 
SPEA-II, and MOPSO to optimize the projects’ schedules to achieve a balance 
between the cash needs during the fiscal years and the available budgets. The 
anticipated extensions in projects’ completion represent the conflicting 
objectives. Finally, the optimized schedules make the contractors’ payment 
schedules affordable by the agencies’ budgets, which help to complete projects 
successfully and achieve the programs’ strategic goals.  
 
Keywords: Finance-based Scheduling; Multi-
objective optimization; Cash-flow management; 
Budget allocation; Portfolios. 
 
 
1. Introduction 
1.1 Research Background 
Bridges constitute a major component in the highway network, which require large capital 
investments for the construction and maintenance. The continuously increasing traffic volumes have 
resulted in higher loads on bridges than those considered in design. Consequently, many bridges 
exhibited deficiencies including reduced capacity, degraded functional performance, and restricted 
vehicle loads. These deficiencies are completely attributable to inadequate maintenance. Existing 
damages on bridges coupled with high traffic loads and severe environmental conditions cause 
accelerated deterioration and require urgent maintenance actions. The large number of bridges and 
 
* Corresponding author: 
E-mail address: elazouni@squ.edu.om 
 
https://doi.org/10.31181/dmame7220241136   


---

Page 2

---

Decision Making: Applications in Management and Engineering 
Volume 7, Issue 2 (2024) 355-379 
356 
 
 
the high costs of maintenance called for the development of effective approaches for maintenance 
planning and management.  
Bridge management tackles all activities throughout the entire life span starting from 
construction until replacement to ensure safety and functionality of bridges. A bridge management 
system is defined as “a tool for assisting highway and bridge management agencies in their choice of 
optimum improvements to the bridge network that are consistent with the agency’s policies, long 
term objectives and budgetary constraints” [1].  The choice of optimum improvements involves 
assigning priority for maintenance needs, planning activities for carrying out the maintenance, and 
optimizing the life-cycle cost of bridges. One of the fundamental functions of bridge management 
constitutes decision-making regarding the allocation of budget to the maintenance operations. 
Bridge management systems enable highway and bridge agencies to operate within budgetary 
constraints while achieving bridge performance goals [2].  
Effective bridge management employs optimization algorithms to develop optimal maintenance 
and repair (M&R) programs subject to budget constraints. Typically, optimization problems are 
formulated to minimize cost functions subject to budgetary constraints in addition to other 
constraints including bridge reliability thresholds, and bridge elements’ conditions. The cost functions 
include life-cycle cost components of the bridge construction and maintenance in addition to the 
costs of the user throughout the bridge service life. Thus, the required input to the optimization 
involves the cost estimates of alternative maintenance strategies and their effectiveness as 
indicated by the period of service between two successive strategies. The optimization is performed 
considering a number of bridges within a defined planning horizon of multiple fiscal years. The 
outcome represents an optimal maintenance program, which enables highway and bridge agencies 
to make decisions regarding the budget allocation and the selection of maintenance strategies. 
There are two primary types of bridge management systems: network-level or project-level 
systems. While the project-level systems concentrate on the selection of repair techniques for 
individual bridges and their parts, the network-level systems deal with the prioritization of bridges 
for consideration in a planned maintenance, repair, and rehabilitation program. The allocation of 
limited budget is one of the aspects that is predominantly addressed at the network level [3,4]. 
Unfortunately, the developed models in the literature perform budget allocation while totally 
ignoring the crucial and closely-related aspect of cash flow. Cash flow problems are potentially 
aggravated by taking into account the fact that most of the maintenance projects are outsourced and 
the agencies have contractual obligations to make payments to contractors of specific amounts at 
specific times. While the budget allocation ensures that funds are available during the planning 
horizon of multiple fiscal years to cover the overall maintenance costs, the operational plans and 
schedules of executing the maintenance works might indicate contractors’ payments during some 
fiscal years that exceed the budgets available during these fiscal years. If these circumstances arise, 
the agencies will definitely experience negative cash flow which can negatively affect the progress of 
work and compromise the success of the programs during the execution of the maintenance works.  
One remarkable study by Mohammadi et al., [5] offered a model for decision-making that 
integrated lean construction concepts into traditional formalized road maintenance planning and 
scheduling, allowing for a reduction of non-value-adding tasks. During the execution phase, the 
chosen interventions are assigned, which is typically accomplished through outsourcing, and the 
interventions are implemented using operational plans and work scheduling. Mohammadi et al., [5] 
reported that the focal aspects of the execution stage include the cash-flow management, especially 
when most of the work is outsourced to contractors, as well as the other operational requirements. 
Mohammadi et al., [5] emphasized that these aspects should be adequately addressed, otherwise 


---

Page 3

---

Decision Making: Applications in Management and Engineering 
Volume 7, Issue 2 (2024) 355-379 
357 
 
 
the success of the M&R program is potentially compromised. Furthermore, Mohammadi et al., [5] 
stated that there won't be much flexibility in the operational plans to accommodate the necessary 
changes and modifications during the execution phase because the M&R plans were generated in a 
separate phase, possibly by different teams, and based on longer planning periods. In order to 
minimize issues and wastes in the construction phase, Kordestani et al., [6] recommended that the 
viewpoints of the operating team and other concerns should be taken into account during the 
planning stage. Therefore, the current research addresses the problem of setting M&R plans without 
addressing the projects’ cash flow. Despite finance-based scheduling (FBS) models were developed 
in the literature to perform the management of cash flow for contractors, portfolio owners were 
totally overlooked. This research reintroduces the FBS method to perform the cash flow management 
for the owners of maintenance portfolios. 
The objective of this study is to help portfolio owners manage their cash flow. For being sure that 
the allocated budgets during fiscal years are adequate for owners to timely make contractors’ 
payments of the projects selected in the maintenance programs, cash flow management is crucial. 
Specifically, this study proposes a FBS model to schedule the activities of the portfolio projects, utilize 
the schedules to define the payment schedules of the projects’ contractors, calculate the agencies’ 
cash needs during the fiscal years, and use the multi-objective optimization algorithms to optimize 
the projects’ schedules (start times of projects and their activities) to achieve a balance between the 
agencies’ cash needs, which represent the cash-out, during the fiscal years and the allocated budgets, 
which represent the cash-in. Practically, the optimized schedules make the contractors’ payment 
schedules affordable by the agencies’ budgets. 
The sections of the paper are organized as follows: (1) Relevant literature in the areas of budget 
allocation and cash flow management is reviewed in the remaining part of section one. At the end of 
the literature review, the research gap and significance are highlighted and the study objective is 
clearly stated. (2) The methodology is presented in section two including the cash flow model, 
formulation of the optimization model, multi-objective optimization algorithms, representation 
system, and special serial-schedule heuristic. (3) In section three of results and discussions, an 
illustrative case portfolio is presented and solved using the multi-objective optimization algorithms. 
(4) In section four of benchmarking, a rigorous comparison between the multi-objective optimization 
algorithms is conducted. The two measures of elite Pareto front and set coverage are used to 
evaluate the quality of the Pareto fronts of the multi-objective optimization algorithms. In addition, 
four performance metrics are introduced and used to compare the performance of the multi-
objective algorithms. Five more case portfolios of different projects’ sizes are solved and the results 
of the experiments are presented and discussed. (5) In section five, the practical implications of the 
proposed method of balancing the agencies’ cash needs during the fiscal years and the available 
budgets during fiscal years are discussed. (6) Finally, the drawn conclusions of the study and the 
suggestions for future research are provided. 
 
1.2 Literature Review 
This section reviews the studies conducted in the two fields of budget allocation of bridge 
maintenance projects, and cash flow management of construction projects. 
 
1.2.1 Budget Allocation 
Several optimization strategies have been developed by researchers to attain the optimal budget 
allocation for asset maintenance. Multi-attribute utility theory was used by Gharaibeh et al., [7] to 
establish a method for allocating funds to asset classes. Using this method, decision makers can 


---

Page 4

---

Decision Making: Applications in Management and Engineering 
Volume 7, Issue 2 (2024) 355-379 
358 
 
 
evaluate trade-offs between asset classes while taking funding transfers into account. Empirical asset 
condition indexes were used by Mrawira and Amador [8] and Kuhn [9] to solve problems of multiple 
assets and single objective. In order to optimally allocate budget to assets at the network-level, the 
National Cooperative Highway Research Program [10] established a utility maximization approach 
which is based on priority weights. The concept and structure of a two-stage procedure to carry out 
a trade-off analysis, for multiple assets at multiple levels, were introduced by Fwa and Farhan [11]. 
Using a bottom-up approach, Yeo et al., [12] addressed a budget-allocation problem for 
infrastructure systems of heterogeneous nature with a definite planning horizon. A methodology for 
allocating money across several assets while accounting for structural, functional, and environmental 
performance factors was proposed by Dehghani et al., [13]. A methodological approach for resource 
allocation for multiple assets based on the performance was presented by Porras-Alvarado et al., 
[14]. Utility functions were employed to fairly allocate resources for multiple asset classes. 
Subsequently, trade-off analyses between various allocation scenarios were carried out using social 
welfare and collective utility functions. For problems with multi-facility deteriorating infrastructure 
systems, Shi et al., [15] presented an integrated budget allocation and preventative maintenance 
optimization model. In order to reduce the overall carbon emissions of bridge networks that have 
maintenance budget constraints, Xu and Guo [16] designed a maintenance strategy for bridges that 
is based on conditions. To assess the effects of budget levels on maintenance schedules and overall 
carbon emissions, sensitivity analyses were carried out. In order to optimize bridge performance 
while adhering to available annual budgets, Ghafoori et al., [17] proposed a system that employs 
machine learning to forecast the condition of concrete bridge components and a binary linear 
programming optimization technique to determine the optimal selection of maintenance actions and 
their timing. In order to enhance and facilitate the bridge management system, Mohammadi et al., 
[18] provided a thorough approach as an advanced asset management system that makes use of data 
from bridge information modeling. A decision support system is integrated into the bridge 
management system in order to rate the feasible remedies and produce more objective decisions for 
the optimal allocation of funds and remedial planning. 
As discussed above, the developed models in the literature have consistently been performing 
budget allocation while totally ignoring the crucial and closely related aspect representing the project 
cash flow. The construction phase involves the assignments of the selected maintenance projects 
and the implementation of the maintenance strategies through operational plans and scheduling 
tasks. Focal aspect during the construction stage represents the cash flow, especially when most of 
the maintenance projects are being outsourced to contractors. Therefore, cash flow should be 
carefully planned and controlled, otherwise the success of the M&R programs can potentially be 
compromised.  
 
1.2.2 Cash Flow Management 
Numerous research efforts have been exerted to predict, plan, and control cash flow. A model to 
maximize schedule robustness while minimizing project cost with the integration of cash flow has 
been carried out by Cao et al., [19]. A sensitivity analysis was conducted by Tavakolan and Nikoukar 
[20] to investigate the impact of modifications to the characteristics of cash flow on the project 
duration versus financing cost trade-off. Dabirian et al., [21] created a model to predict, plan, and 
manage various policies, such as prepayment and payment delay, by detecting the feedback loops in 
cash flow. A simulation-based methodology was developed by Andalib et al., [22] to predict project 
cash flow taking into account the intertemporal relationship between subsequent progress payments 
and the history of the owners' payment in past projects. A methodology that generates cash flow 


---

Page 5

---

Decision Making: Applications in Management and Engineering 
Volume 7, Issue 2 (2024) 355-379 
359 
 
 
predictions to reduce financing costs while considering various financing options and non-extended 
work schedules was provided by Alavipour and Arditi [23]. Singularity functions were utilized by Su 
and Lucko [24] to accurately compute project cash flow balances. An automated technique was 
presented by Lee et al., [25] to address the uncertainties surrounding the costs and durations of the 
activities and enhance the reliability of project cash flow analysis. An IT system was established by 
Motawa and Kaka [26] to assist all supply chain participants in selecting the most suitable cash flow 
and payment method. A mathematical method, that is fuzzy and entropy-based, was used by Tang 
et al., [27] to handle the objective function weighting problem in the models of cash flow. Lee et al., 
[28] established the causal connection between the causes and effects of nonpayment using a 
decision-making trial and evaluation laboratory technique. The main contributing elements include 
the paymaster's poor financial management, the local way of life and culture, mistakes in documents, 
terms of contracts, and differences in the estimation of completed work. Cash flow problem was one 
of the key repercussions. It is remarkable that, all of the examined research efforts in this section 
considered the cash flow exclusively from contractors’ perspective.  
Few studies were carried out in the literature considering the cash flow from the owners’ 
(agencies’) perspective. An analytical and decision support framework for managing cash flow and 
payments in construction projects was developed by Dorrah and McCabe [29] for a variety of 
stakeholders, including owners, contractors, and subcontractors. The framework incorporates game 
theory and agent-based modeling and simulation to analyze the collaborative decision-making 
process, the cash flow and payment system, while considering the individual and collective features 
of stakeholders. Governments are given a tool provided by Shalaby and Ezeldin [30] to choose work 
packages for large-scale projects supported by the "Results-Based-Finance" mechanism in a way that 
improves project cash flow in terms of early cash-in collection. Based on genetic algorithms and case-
based reasoning, Liang et al., [31] developed a cash flow model to forecast the expenditures of 
transportation agencies' design-build projects. An agent-based simulation model was provided by 
Farshchian et al., [32] to mimic budget allocation and how it affects the progress of construction 
projects in an owner's portfolio. A dynamic threshold cash flow based structural model was used by 
Huang et al., [33] to assist owners in determining each construction contractor's credit quality score 
during the prequalification stage. Jarrah et al., [34] examined TxDoT projects during the period from 
2001 to 2003 in order to develop mathematical models that depict the monthly payments made to 
contractors. An owner who has to manage the budget for several projects has to estimate the 
contractor payments for the upcoming months in order to plan for them. It is remarkable that, none 
of these studies balances the agency's cash-in and cash-out amounts during fiscal years. 
FBS method schedules projects’ activities during the projects’ individual billing periods under the 
limited cash-in while minimizing extensions in projects completion. Cash-in is available during a given 
billing period through two sources: (1) the money received for activities completed and billed during 
earlier billing periods; and (2) the external funds procured through the lines of credit with preset 
credit limits. FBS method balances the contractors’ cash-out representing the project direct and 
indirect costs with the cash-in available during the individual billing periods. FBS method fulfils the 
credit-limit constraints imposed on the amounts of the negative overdraft values, which are realized 
as of the ends of the billing periods. Since FBS was originally introduced by Elazouni and Gab-Allah 
[35], many research efforts in the literature developed models to solve FBS problems [36-41]. 
However, the FBS models developed in the literature adopt the cash flow exclusively from the 
perspective of the contractors. 
The cash flow model of the agencies is completely different from that of the contractors in terms 
of components and structure. The agencies’ cash-out component represents the contractors’ 


---

Page 6

---

Decision Making: Applications in Management and Engineering 
Volume 7, Issue 2 (2024) 355-379 
360 
 
 
payments, which happen at discrete dates as opposed to the cash-out in FBS, which happens in 
continuous mode. The agencies’ cash-in component represents the predetermined budget amount 
available during each fiscal year within the planning horizon as opposed to the cash-in in FBS, which 
is determined based on the activities completed and billed during earlier billing periods. The agencies’ 
cash flow structure is composed of the planning horizons of multiple fiscal years as opposed to the 
short billing periods in FBS. 
The main research gap in this study is that the bridge maintenance agencies set bridge M&R 
programs while completely ignoring the crucial aspect of cash flow. Given the fact that most of the 
maintenance projects are outsourced, cash flow problems could delay progress and potentially 
compromise the success of the M&R programs. Another research gap is that numerous FBS models 
were developed to manage cash flow for contractors while totally overlooking the cash flow of 
portfolio owners. Thus, the objective of this research is to reintroduce FBS to effectively manage the 
cash flow for portfolio owners. A multi-objective optimization method is employed to optimize the 
schedules (start times of projects’ starts activities and the remaining activities) of projects in 
portfolios to achieve a balance between the agencies’ cash needs during the fiscal years and the 
allocated budgets. The employed multi-objective scheduling optimization algorithms minimize the 
anticipated extensions in the completion of the individual projects. The optimization output presents 
to the decision maker a Pareto front with a set of solutions, each solution involves the optimized 
schedules of the individual projects. Thus, the Pareto fronts facilitate decision-making regarding the 
selection of the most appropriate solution based on the set priority of projects for early completion. 
 
2. Methodology 
2.1 Cash Flow Model 
There are multiple projects in a portfolio that make up the current scheduling problem. The 
activities of the project have a single mode of operation and cannot be stopped once it has begun. 
The payments made to contractors represent the agency's cash-out and are determined by the 
contract prices of the activities. It is assumed that the price of activity 𝑎𝑖 is distributed uniformly over 
the activity’s duration and has a rate of 𝑐𝑖 per day.  
Projects in portfolios are typically assigned to various contractors with varying start dates and 
payment terms. Bills from contractors are turned in at the last day of each billing period. The project's 
start date as well as the start date of the first billing period are indicated by the start time of the 
project's start activity. 𝑌𝑖,𝑏 is the contractor's invoiced amount for the portion of activity 𝑎𝑖 that falls 
in billing period b. This amount is determined by applying one of the four cases in Eq. (1), depending 
on the overlap between the activity duration and the billing period, as depicted in Figure 1. 
𝑌𝑖,𝑏= ∑
 𝑐𝑖  
𝐹𝑏 
𝑠𝑖
 
𝐹𝑏 ≥ 𝑠𝑖 ≥ 𝑆𝑏 and 𝑓𝑖 ≥ 𝐹𝑏                                      
(1a) 
𝑌𝑖,𝑏= ∑
 𝑐𝑖  
𝑓𝑖 
𝑆𝑏
 
𝑠𝑖 < 𝑆𝑏 and 𝑆𝑏 ≤ 𝑓𝑖 < 𝐹𝑏                                         
(1b) 
𝑌𝑖,𝑏= ∑
𝑐𝑖  
 𝑓𝑖 
𝑠𝑖 
   
𝑠𝑖 ≥ 𝑆𝑏 and 𝑓𝑖 < 𝐹𝑏                                         
(1c) 
𝑌𝑖,𝑏= ∑
𝑐𝑖  
𝐹𝑏 
𝑆𝑏
 
𝑠𝑖 < 𝑆𝑏 and 𝑓𝑖 ≥ 𝐹𝑏                                       
(1d) 
Where; 𝑐𝑖 is activity’s 𝑎𝑖 price per day; 𝑠𝑖 and 𝑓𝑖  are activity’s 𝑎𝑖 start and finish dates respectively; 
and 𝑆𝑏 and 𝐹𝑏 are the start and end dates of billing period b respectively. Eq. (1) computes 𝑌𝑖,𝑏 for 
every billing period based on 𝑠𝑖 and 𝑓𝑖 in comparison to 𝑆𝑏  and 𝐹𝑏 as shown in Figure 1. 


---

Page 7

---

Decision Making: Applications in Management and Engineering 
Volume 7, Issue 2 (2024) 355-379 
361 
 
 
 
Fig. 1. The earned cash amounts during the billing period b 
 
The sum of the billed amounts of activities 𝑛𝑏, or portions of them, that are completed within the 
billing period b as in Eq. (2), determines the contractor’s billed amount of 𝑌𝑏 during billing period b. 
As in Eq. (3), the contractor’s payment in project j, 𝐸𝑗,𝑏 is computed using the billed amount 𝑌𝑏, 
and a reduction factor r that jointly accounts for the advance payment payback and the retainage 
percentage. One period after the bill is submitted, the contractor receives the payment. 
 
𝐸𝑗,𝑏 = 𝑌𝑏* [1 - r]                                                                                                                                  (3) 
The first term in Eq. (4) indicates how to determine the sum 𝑂𝑡 of contractors’ payments 𝐸𝑗 of 𝑚𝑡 
projects that are underway throughout fiscal year t. The 𝑉𝑡 parameter in Eq. (4) is the sum of all 
projects’ advance payments and retained amounts’ repayments that take place during fiscal year t. 
The agency’s cash-out for fiscal year t is represented by 𝑂𝑡 in Eq. (4). 
 
𝑂𝑡 = ∑
𝐸𝑗 + 𝑉𝑡
𝑚𝑡
𝑗=1
 
                            (4) 
The agency's budget, or cash-in, is linked to a certain planning horizon consisting of several fiscal 
years. The available budget for a given fiscal year t  is represented by 𝐼𝑡, which may or may not remain 
constant for each fiscal year included in the planning horizon. It may become necessary to shift the 
start times of different activities as the scheduling process moves forward year after year in order to 
maintain the sought balance between the budgeted amount 𝐼𝑡 and the cash-out amount 𝑂𝑡.  There 
may be instances where the budgeted amount available for a particular fiscal year is greater than the 
cash-out, resulting in some amount of unused cash. The unused cash is assumed to be rolled over to 
the following fiscal year in the current model. As a result, the cash-in for the following fiscal year is 
modified when all eligible activities within a particular fiscal year are scheduled with some unused 
cash. At the conclusion of a fiscal year t, the agency’s cash-out is represented by 𝑅𝑡 in Eq. (5) and the 
agency’s cash-in is represented by 𝐺𝑡 in Eq. (6). 
𝑅𝑡= ∑𝑂𝑞
𝑡
𝑞=1
 
                         (5) 
𝑌𝑏 = ∑
𝑌𝑖,𝑏 
𝑛𝑏
𝑖=1
 
                                                                                                                          (2) 


---

Page 8

---

Decision Making: Applications in Management and Engineering 
Volume 7, Issue 2 (2024) 355-379 
362 
 
 
𝐺𝑡= ∑𝐼𝑞
𝑡
𝑞=1
 
                         (6) 
2.2 Objective Function  
In principle, extensions in the completion of the individual projects within portfolios are 
anticipated as a result of scheduling multiple projects simultaneously under constrained budgets. 
These anticipated extensions are inversely proportional to the available budget. Therefore, 
anticipated extensions in the completion of individual projects are considered as being the conflicting 
objectives. The multi-objective optimization algorithms minimize the anticipated extensions in the 
completion of the individual projects. 
The minimization of the anticipated extensions in completion of each individual project 𝐷𝑗 is 
achieved by the multi-objective optimization model. Accordingly, the number of the objectives in the 
problem matches the number of projects in the portfolio. The formulation of the objective function 
is given in Eqs. (7) and (8). 
 
Minimize:    Dj (xj),  j = j1,…, jm                                                                                                                           (7) 
xj = (s1,j, …,si,j, … ,sn,j)                                                                                                                                     (8) 
Where; 𝐷𝑗 represents the extension in the completion of project j; m is the number of projects in 
portfolio; 𝑥𝑗 is a vector that represents the start times of the activities of a candidate schedule, 
including the project's start activity which establishes the project's start time; 𝑠𝑖,𝑗 represents the start 
time of activity 𝑎𝑖  in project j; and n represents the number of activities in project j. 
 
2.3 Model Constraints 
The optimization model takes into account the satisfaction of the constraints that describe the 
dependencies between activities and the limited fund available for each fiscal year. This means that, 
if activity’s 𝑎𝑖 predecessors are kept in a set 𝑃𝑖, the start time 𝑠𝑖 of activity 𝑎𝑖 in Eq. (9) is higher than 
or equal to the finish times 𝑓𝑎𝑘  of all its predecessors 𝑎𝑘 in 𝑃𝑖. Additionally, the portfolio′s 𝑅𝑡 as of 
the conclusion of fiscal year t  should be greater than 𝐺𝑡 as in Eq. (10). 
𝑠𝑖 ≥ 𝑓𝑎𝑘 
Ɐ𝑎𝑘 ∈ 𝑃𝑖 
 (9) 
𝑅𝑡 ≤ 𝐺𝑡         Ɐ t 
(10) 
2.4 Multi-objective Algorithms 
This section presents the three employed multi-objective optimization algorithms in this study. 
The Strength Pareto Evolutionary Algorithm (SPEA-II) and the Non-dominated Sorting Genetic 
Algorithm (NSGA-II) are two examples of Multi-Objective Evolutionary Algorithms (MOEA), while the 
Multi-Objective Particle Swarm Optimization algorithm (MOPSO) is a swarm algorithm.                         
 
2.4.1 SPEA-II 
SPEA-II was first proposed by Zitzler et al., [42] as an improved algorithm of SPEA [43]. SPEA-II has 
been recognized as an efficient algorithm to solve different types of multi-objective problems (MOP) 
[44,45]. In SPEA-II, a fine-grained fitness assignment strategy is implemented where the fitness of 


---

Page 9

---

Decision Making: Applications in Management and Engineering 
Volume 7, Issue 2 (2024) 355-379 
363 
 
 
each individual depends on the number of individuals that it dominates and that are dominated by 
it. Also, a fixed-size external repository is used to keep the best solutions. If the number of non-
dominated solutions is smaller than the capacity of the repository, the best dominated solutions may 
be added to fill up. However, having non-dominated solutions more than the capacity of the 
repository, a special archive truncation method is adopted in which boundary solutions are 
preserved. 
 
2.4.2 NSGA-II 
NSGA-II, which was firstly proposed by Deb et al., [46], has been one of the most prominent 
algorithms to solve various MOP. In a survey conducted on the use of multi-objective algorithms in 
construction project management during the period 2012-2016, Alothaimeen and Arditi [47] 
reported that NSGA-II was the most commonly used algorithm. Recent applications of NSGA-II in 
project management included sustainability development, green construction, and carbon emissions 
as optimization objectives [48,49].  In NSGA-II, fitness is assigned according to a two-level criteria, 
the first depends on the dominance rank of the individuals, whereas the second is assigned 
considering the crowding distance of the individuals of the same dominance rank. In contrary to 
SPEA-II, no external repository is used in NSGA-II. However, the best individuals are preserved by 
keeping the best individuals from both the parents and the children after the generation of the 
children in each iteration.  
 
2.4.3 MOPSO 
The main algorithm was adopted from Ünal and Kayakutlu [50]. In the current study, a mutation 
operator of a random immigrant considering a decaying rate of 0.5 similar to that used in Ünal and 
Kayakutlu [50] was implemented. While the MOEA algorithms of SPEA-II, and NSGA-II adopt the 
crossover operator, the MOPSO involves algorithm-related operators to guide the flow of the swarm 
particles. Also, a repository of non-dominated individuals with a maximum capacity was maintained. 
However, the algorithm used in the current study differs from that presented in Ünal and Kayakutlu 
[50] in two aspects. Firstly, in the current study, when having more non-dominated individuals than 
the repository maximum capacity, individuals are eliminated considering the crowding distance. The 
crowding distance of non-dominated individuals was calculated similar to the one used in Deb et al., 
[46]. Secondly, a procedure similar to the one used in Abido [51] was implemented in the current 
study to find the local and the global best guide for each particle. In the current study, the self-
learning and the social learning factors were adopted as 0.5 and one, respectively. 
 
2.5 Representation system 
The random key (RK) indirect representation system, first put forth by Bean [52], was employed in 
the current research. The RK allows for the implementation of the classical operators while ensuring 
the schedules’ feasibility. However, the utilization of RK requires the use of a special serial-schedule 
heuristic to obtain the schedules. Another problem of the RK is that different RK chromosomes in 
MOEA or particles in MOPSO may result in the same schedule. Schedules are indirectly defined using 
RK by giving each activity a relative scheduling priority. The length of the chromosomes in the MOEA 
and the particles in MOPSO is equal to the number of projects’ activities. Every gene in a chromosome 
represents one activity and has an RK value between zero and one. This RK value represents the 
priority of the activity's scheduling in comparison to the other activities. Higher scheduling priority is 
indicated by a bigger RK value. The creation of the initial population in MOEA and swarm in MOPSO 
is done by randomly assigning the RK values. 


---

Page 10

---

Decision Making: Applications in Management and Engineering 
Volume 7, Issue 2 (2024) 355-379 
364 
 
 
2.6 Special serial-schedule heuristic 
In the current study, a special serial-schedule heuristic is developed to obtain schedules from the 
RK chromosomes/particles. There are two stages involved in the heuristic. First, two sets of ordered 
and unordered activities are started, with the unordered set including all of the activities at first. Each 
step is carried out by first determining which activities are eligible, then choosing one activity, and 
finally transferring the chosen activity to the ordered set. The ordered activities are sequentially 
scheduled in the second stage, taking into account budgetary and precedence constraints. It should 
be noted that the implementation of the two stages of the heuristic is computationally expensive. 
Figure 2 shows the flow chart for the special serial-schedule heuristic. 
 
3. Results and Discussions 
Though the budget allocation in real portfolios is typically made based on long planning horizons 
of multiple fiscal years, the illustrative case portfolio adopts a shorter planning horizon of only six 
months to make the problem of manageable size. The case portfolio is composed of two projects A 
and B, which encompass four and six activities respectively. The contractual terms of projects A and 
B are presented in Table 1. The first row in Table 1 shows that projects A and B are initially scheduled 
to start on day zero, which marks the beginning of the six-month planning horizon. The relationships, 
duration, and prices of the activities are presented in Table 2. The activities’ start times in the initial 
schedules of projects A and B are shown in the third column in Table 3. The durations of projects A 
and B span 42 and 51 working days respectively as indicated by the finish times of the terminating 
activities DA and FB of projects A and B respectively. 
Table 4 presents the agency’s monthly cash-out in the first row, which represents the collective 
payment schedule of the contractors of projects A and B during the six-month planning horizon, and 
the agency’s monthly budget amounts, which represent the agency’s monthly cash-in, in the second 
row. The last two rows in Table 4 present the cumulative agency’s cash-out and cash-in, which have 
identical total amount of $261,000. The selection of projects A and B in the portfolio when the budget 
allocation process was performed was based on the fact that the total cost of projects A and B, which 
amounts to $261,000 was exactly matching the agency’s budget available. However, the conducted 
cash flow analysis revealed that the cash-in amounts of $42,000 and $79,350 available during the 
second and third months are inadequate to cover the cash-out amounts of $91,600 and $136,800, 
respectively as presented in Table 4. The budget deficits during the second and third months are huge 
enough to create additional budget deficits during the fourth and fifth months as indicated by the 
cumulative cash-out and cash-in values in the last two rows in Table 4. Unless this cash flow problem 
is resolved, financial issues are anticipated which can potentially compromise the success of the 
projects. To balance the agency’s cash-out and cash-in on a monthly basis, activities of the two 
projects need to be simultaneously rescheduled to achieve the sought balance while minimizing 
possible extensions in the completion of projects A and B. 
 


---

Page 11

---

Decision Making: Applications in Management and Engineering 
Volume 7, Issue 2 (2024) 355-379 
365 
 
 
 
Fig. 2. Special serial-schedule heuristic 
 
 


---

Page 12

---

Decision Making: Applications in Management and Engineering 
Volume 7, Issue 2 (2024) 355-379 
366 
 
 
Table 1  
Contractual terms of projects A and B 
Contract terms 
Project A 
Project B 
Original commencement (day #) 
0 
0 
Advance payment (%) 
5 
5 
Lag of paying advance payment from project’s commencement (day) 
0 
0 
Retained (%) of interim pay requests 
5 
10 
Lag of paying retained money from project’s completion (month) 
1 
1 
Billing period duration (month) 
1 
1 
Lag of paying received bills (month) 
1 
1 
 
                          Table 2 
Activities relationship, duration, and prices of projects A and B 
Project 
Activity ID 
Predecessor 
Duration (day) 
Prices ($) 
A 
AA 
- 
17 
17000 
BA 
AA 
15 
30000 
CA 
AA 
12 
48000 
DA 
BA, CA 
10 
30000 
B 
AB 
- 
15 
30000 
BB 
AB 
10 
20000 
CB 
AB 
15 
30000 
DB 
BB 
12 
24000 
EB 
CB 
11 
22000 
FB 
DB, EB 
10 
10000 
 
Table 3 
Original start times and the start times of the best compromise solutions 
of projects A and B 
Project 
Activity 
Start times 
Original 
SPEA-II 
NSGA-II 
MOPSO 
A 
AA 
0 
0 
1 
1 
BA 
17 
18 
45 
18 
CA 
17 
17 
34 
18 
DA 
32 
41 
65 
33 
B 
AB 
0 
1 
0 
0 
BB 
15 
22 
20 
57 
CB 
15 
44 
15 
15 
DB 
25 
32 
33 
67 
EB 
30 
59 
30 
65 
FB 
41 
70 
45 
79 
 
 Table 4 
 Cash-out and cash-in of the original solution of projects A and B  
Parameters 
One-month fiscal periods 
1 
2 
3 
4 
5 
6 
Cash-out ($) 
13,050 
91,600 
136,800 
19,550 
- 
- 
Cash-in ($) 
13,050 
42,000 
79,350 
63,540 
48,000 
15,060 
Cumulative Cash-out ($) 
13,050  
104,650  241,450  
261,000  
261,000 
261,000 
Cumulative cash-in ($) 
13,050 
55,050 
134,400 
197,940 
245,940 
261,000 
 
The case portfolio was solved using the three multi-objective algorithms. The population/swarm 
sizes of five were selected for the three algorithms while the sizes of the external repository for SPEA-
II and MOPSO were set as five. The five obtained Pareto solutions of the three algorithms are 


---

Page 13

---

Decision Making: Applications in Management and Engineering 
Volume 7, Issue 2 (2024) 355-379 
367 
 
 
presented in Table 5 using the parameters presented in the bottom of Table 5. The Pareto front of 
each algorithm involves five non-dominated solutions. The three algorithms obtained the same 
boundary solutions, i.e., solutions of minimum extensions in completion of projects A and B. The first 
solution, that achieves the global minimum extension of project A to zero, should be selected if the 
decision maker’s preference is to minimize the extension of project A. While the first solution 
minimizes the extension in project B to 44 days, this is not the global minimum extension of project 
B. The 44-day extension in project B is definitely higher than its globally minimum extension of zero 
associated with the fifth solution. On the other hand, the fifth solution globally minimizes the 
extension of project B to zero, and minimizes, but not globally minimizes, the extension of project A 
to 48 days. 
 
 Table 5 
 Extensions of Pareto solutions of projects A and B 
Pareto 
solutions 
Extensions in completion of projects (days) 
SPEA-IIa 
NSGA-IIa 
MOPSOb 
Elite Pareto set 
A 
B 
A 
B 
A 
B 
A 
B 
1 
0 
44 
0 
44 
0 
44 
0 
44 
2 
1 
37 
1 
37 
1c 
38c 
1 
37 
3 
9c 
29c 
13 
29 
13 
29 
9 
29 
4 
33 
7 
33c 
4c 
33 
9 
33 
4 
5 
48 
0 
48 
0 
48 
0 
48 
0 
a 100 iterations, single-point crossover, 80% crossover probability, new-chromosome mutation, 
15% mutation rate.  
b 100 iterations, 0.4 initial weight, 0.5 self-learning factor, 1.0 social-learning factor, new-particle 
mutation, 0.5 mutation probability/decaying rate. 
c Best compromise solutions. 
 
Table 5 presents the trade-off between the minimum extensions of projects A and B, which is 
represented by the three additional solutions that each algorithm offers in addition to the boundary 
solutions. Although the extensions in projects A and B are minimized in each of these three methods, 
they are not globally minimized. Since each of these five solutions consists of two optimized values 
for each of the two objectives, they are all considered to be the best possible solutions. That is, 
concerning the values of the two objectives, no solution is superior than any other. To strike a balance 
between the extensions of the two projects, the best compromise solution, as found by Dhillon et 
al., [53] can be used when there is no reason to favor a specific project. As presented in Table 5, 
different best compromise solutions were attained using the three algorithms. 
To illustrate the RK representation, and the special serial-schedule heuristic, which balances the 
agency’s cash-out with cash-in, one of the obtained solutions is explained in detail. Figure 3 shows 
chromosome a, which characterizes the best compromise solution of SPEA-II in Table 5. As explained 
above, the special serial-schedule heuristic involves two stages; (1) define the scheduling order of 
the activities based on the RK values, (2) determine the activities' earliest start time that fulfills both 
the precedence and the budget constraints. Figure 4 shows the output of the first stage of the 
heuristic which defines the scheduling order of all projects’ activities according to the heuristic flow 
chart shown in Figure 2. In the second stage, the start times are determined for the best compromise 
solutions of the three algorithms, which are presented in Table 3. The fourth column in Table 3 
presents chromosome a of the best compromise solution of SPEA-II which indicates the activities’ 
start times that fulfill the precedence and budget constraints. Table 6 presents the original schedules 
of payments for the contractors of projects A and B and the optimized schedules of payments that 
correspond to chromosome a. The detailed calculations of the amounts of bills in Table 6 are 


---

Page 14

---

Decision Making: Applications in Management and Engineering 
Volume 7, Issue 2 (2024) 355-379 
368 
 
 
presented in Table 7. Figure 5 shows the rescheduled activities of projects A and B of chromosome a 
and the start and finish dates of the billing periods. It should be noted that Figure 5 depicts one-day 
delay in project B's planned start date. 
 
AA 
BA 
CA 
DA 
AB 
BB 
CB 
DB 
EB 
FB 
0.47 
0.39 
0.47 
0.68 
0.40 
0.37 
0.29 
0.40 
0.99 
0.13 
Fig. 3. Chromosome a of the best compromise solution of SPEA-II 
AA 
CA 
AB BA 
DA 
BB 
DB 
CB 
EB 
FB 
Fig. 4. Scheduling order of activities according to chromosome a. 
 
Table 6  
Schedules of payments according to the original schedule and chromosome a 
Solution 
Project 
Parameter 
One-month fiscal periods 
1 
2 
3 
4 
5 
6 
Original 
A 
Bill ($) 
47,000 
78,000 
- 
- 
- 
- 
Payment ($) 
6,250 
42,300 
76,450 
- 
- 
- 
B 
Bill ($) 
58,000 
71,000 
7,000 
- 
- 
- 
Payment ($) 
6,800 
49,350 
60,350 
19,550 
- 
- 
A&B 
Payment ($) 
13,050 
91,600 
136,800 
19,550 
- 
- 
Chromosome a 
A 
Bill ($) 
45,000 
59,000 
21,000 
- 
- 
- 
Payment ($) 
6,250 
40,500 
53,100 
25,150 
- 
- 
B 
Bill ($) 
- 
32,000 
44,000 
40,000 
20,000 
17,000 
Payment ($) 
6,800 
- 
27,200 
37,400 
47,600 
- 
A&B 
Payment ($) 
13,050 
40,500 
80,300 
62,550 
47,600 
17,000 
 
Table 7 
Detailed calculations of the bills and payments of chromosome a 
Project 
Bill 
Activity 
Performed 
duration 
(days) 
 
Daily 
price  
($) 
Bill 
amount 
($) 
Payment 
amount  
($) 
Bill  
period 
Payment 
period 
A 
A1 
AA 
17 
 
1000 
45,000 
40,500 
1 
2 
AB 
4 
 
2000 
AC 
5 
 
4000 
A2 
BA 
11 
 
2000 
59,000 
53,100 
2 
3 
CA 
7 
 
4000 
DA 
3 
 
3000 
A3 
DA 
7 
 
3000 
21,000 
19,800 
3 
4 
B 
B1 
AB 
15 
 
2000 
32,000 
27,200 
2 
3 
BB 
1 
 
2000 
B2 
BB 
9 
 
2000 
44,000 
37,400 
3 
4 
CB 
1 
 
2000 
DB 
12 
 
2000 
B3 
CB 
14 
 
2000 
40,000 
34,000 
4 
5 
EB 
6 
 
2000 
B4 
EB 
5 
 
2000 
20,000 
17,000 
5 
6 
FB 
10 
 
1000 
 


---

Page 15

---

Decision Making: Applications in Management and Engineering 
Volume 7, Issue 2 (2024) 355-379 
369 
 
 
 
Fig. 5. Bar chart of the chromosome a presenting the activities and billing periods of projects A 
and B 
 
The cash-out of chromosome a and the best compromise solutions of the three algorithms during 
the fiscal monthly periods are presented in Table 8. It ought to be noted that the cumulative cash-
out values of the three algorithms in Table 8 are balanced with the cumulative cash-in values in the 
last row in Table 4 during the six fiscal periods. 
Table 8 
Cash-out of the best compromise solutions of SPEA-II, NSGA-II, and MOPSO 
Algorithm 
Cash-out  
($) 
One-month fiscal periods  
1 
2 
3 
4 
5 
6 
SPEA-II 
Period 
13,050 
40,500 
80,300 
62,550 
47,600 
17,000 
Cumulative  
13,050 
53,550 
133,850 196,400 244,000 261,000 
NSGA-II 
Period 
13,050 
40,800 
79,900 
63,400 
36,850 
27,000 
Cumulative  
13,050 
53,850 
133,750 197,150 234,000 261,000 
MOPSO 
Period 
13,050 
37,400 
62,150 
83,800 
48,450 
16,150 
Cumulative  
13,050 
50,450 
112,600 196,400 244,850 261,000 
37 38 39 42 43 44 45 46 49 50 51 52 53 56 57 58 59 60 63 64 65 66 67 70 71 72 73 74 77 78
Tu We Th Su Mo Tu We Th Su Mo Tu We Th Su Mo Tu We Th Su Mo Tu We Th Su Mo Tu We Th Su Mo
27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56
AA
BA
CA
DA
AB
BB
CB
DB
EB
FB
2
3
Month
Calendar day
0
1
2
3
4
7
8
9
10 11 14 15 16 17 18 21 22 23 24 25 28 29 30 31 32 35 36
Day
Su Mo Tu We Th Su Mo Tu We Th Su Mo Tu We Th Su Mo Tu We Th Su Mo Tu We Th Su Mo
Working day
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
10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
AA
BA
CA
DA
AB
BB
CB
DB
EB
FB
1
79 80 81 84 85 86 87 88 91 92 93 94 95 98 99
100
101 102
105
106
107
108
109
112
113
114
115
116
119
Tu We Th Su Mo Tu We Th Su Mo Tu We Th Su Mo Tu We Th Su Mo Tu We Th Su Mo Tu We Th Su
57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85
AA
BA
CA
DA
AB
BB
CB
DB
EB
FB
3
4
A1 
B1 
A2 
B2 
A2 
B2 
A3 
B3 
B4 
A3 


---

Page 16

---

Decision Making: Applications in Management and Engineering 
Volume 7, Issue 2 (2024) 355-379 
370 
 
 
As presented in Table 9, some amounts of cash occasionally remain unutilized at the end of some 
fiscal months, which are rolled over to the following month. For instance, an unutilized cash amount 
of $1,500 during the second month was moved to the third month, which raised the cash-in from 
$79,350 to $80,850 as shown in Table 9. The updated cash-in values are presented in the second row 
in Table 9 for the six fiscal months. Now, it is obvious that the contractors’ payment schedule of 
chromosome a, which is presented in the last row of Table 6, became affordable by the agency’s 
budget, which is presented as the updated cash-in values in the second row in Table 9. Figure 6 shows 
the cumulative cash-in and the cumulative cash-out of the original projects’ schedules. In addition, 
Figure 6 shows the optimized cash-out for the best compromise solutions of SPEA-II, NSGA-II, and 
MOPSO. Figure 6 demonstrates the capability of the algorithms to balance the owners’ cash-out with 
the cash-in during the six-month planning horizon. 
 
Table 9  
Periodical cash-in and utilized cash of chromosome a 
Parameter 
One-month fiscal period 
1 
2 
3 
4 
5 
6 
Cash-in ($) 
13,050 
42,000 
79,350 
63,540 
48,000 
15,060 
Updated cash-in ($) 
13,050 
42,000 
80,850 
64,090 
49,540 
17,000 
Cash-out ($) 
13,050 
40,500 
80,300 
62,550 
47,600 
17,000 
Cumulative unutilized cash ($) 
0 
1,500 
550 
1,540 
1,940 
0 
 
 
 
Fig. 6. Balanced cash-out with cash-in using SPEA-II, NSGA-II, and MOPSO 
 
4. Benchmarking 
To evaluate the quality of the Pareto fronts obtained by the individual algorithms, the Pareto 
solutions of the three algorithms were combined and the elite Pareto front was obtained by applying 
the dominance conditions. The elite set of the Pareto solutions is presented in the last column in 


---

Page 17

---

Decision Making: Applications in Management and Engineering 
Volume 7, Issue 2 (2024) 355-379 
371 
 
 
Table 5. Then, the contributions of the individual algorithms to the elite Pareto front were 
determined. The higher the contribution of a particular algorithm to the elite Pareto front the better 
quality of the algorithm’s Pareto solutions. The results in the last column in Table 5 are such that only 
two of the MOPSO Pareto solutions belong to the elite Pareto front whereas four of the SPEA-II and 
NSGA-II solutions belong to the elite Pareto front. This finding clearly indicates that SPEA-II and NSGA-
II contributed to the elite Pareto front more significantly compared to MOPSO.                
In addition, the measure of “set coverage” was used, which was firstly introduced by Zitzler and 
Thiele [43]. This measure is used to evaluate the quality of the obtained Pareto fronts by calculating 
the percentage of Pareto solutions of each algorithm that is covered by the Pareto solutions of other 
algorithms. Generally, high coverage percentages reflect better quality of Pareto solutions. The set 
coverage percentages were calculated and presented in Table 10, which indicate that SPEA-II 
exhibited the best performance by covering 80% and 100% of the Pareto solutions of NSGA-II and 
MOPSO, respectively. The NSGA-II exhibited comparable performance by covering 80% and 100% of 
the Pareto solutions of SPEA-II and MOPSO, respectively. MOPSO was found to have the worst 
performance by covering only 40% and 60% of the Pareto solutions of SPEA-II and NSGA-II, 
respectively. 
 
Table 10 
Values of the set coverage measure 
Set A 
SPEA-II 
NSGA-II 
MOPSO 
Set B 
NSGA-II 
MOPSO 
SPEA-II 
MOPSO 
SPEA-II 
NSGA-II 
Case program 
80.0 
100.0 
80.0 
100.0 
40.0 
60.0 
 
Further, the quality of the obtained Pareto fronts was evaluated using the performance metrics of 
computational time, diversity Δ, spacing SP, and hypervolume HV where the values are presented in 
Table 11.  The performance metric (Δ) was introduced by Deb et al., [46] to measure the extent of 
the spread of the non-dominated solutions, as well as the uniformity of their distribution. The spacing 
metric (SP), which was first proposed by Schott [54] is a diversity metric that is used to assess the 
spreading uniformity of the solutions in the obtained Pareto front. Another metric is the hypervolume 
(HV) which evaluates both the convergence and the diversity of the obtained Pareto solutions [55]. 
Considering the computational time, the SPEA-II Pareto front was obtained in 0.97 seconds compared 
to 1.02 and 1.28 seconds of NSGA-II and MOPSO, respectively. Regarding diversity, the results are 
such that the three algorithms have identical values of the diversity metric Δ, which indicate similar 
spreading of the Pareto solutions of the three algorithms.  However, a better spacing metric SP value 
was achieved by MOPSO indicating a higher uniformity of MOPSO Pareto solutions. With respect to 
the hypervolume HV metric, SPEA-II and NSGA-II exhibited the same value of 0.77 compared to 0.76 
of MOPSO. This indicates that the obtained Pareto fronts of SPEA-II and NSGA-II have a comparable 
performance regarding convergence/diversity. 
 
Table 11 
Values of the performance metrics 
Parameter 
Algorithm 
SPEA-II 
NSGA-II 
MOPSO 
Computational time (s) 
0.97 
1.02 
1.28 
Diversity metric 
0.96 
0.96 
0.96 
Spacing metric 
9.66 
9.12 
7.91 
Hypervolume metric 
0.77 
0.77 
0.76 
 


---

Page 18

---

Decision Making: Applications in Management and Engineering 
Volume 7, Issue 2 (2024) 355-379 
372 
 
 
The three algorithms of SPEA-II, NSGA-II, and MOPSO were benchmarked using five case portfolios 
of CP-1, CP-2, CP-3, CP-4, and CP-5 each portfolio comprises two large-size projects. The project 
networks of the five case portfolios were developed using MPSPLib. The projects of the case 
portfolios include 20, 30, 90, 120, and 240 activities. Table 12 presents the sizes of the 
population/swarm as well as the external repository set. The same parameters presented in the 
bottom of Table 5 were used to solve the five case portfolios. The experiments were implemented 
on a laptop with Intel(R) Core (TM) i7-4500U CPU@1.80 GHz 2.40 GHz processor and 8 GBs RAM. The 
algorithms were coded using MATLAB 2018a. 
 
Table 12 
Sizes of the population/swarm and external set/archive for the five case portfolios 
Case 
portfolio  
Projects’  
activities 
Size of population/swarm 
Size of the external set/archive 
SPEA-II 
NSGA-II 
MOPSO 
SPEA-II 
MOPSO 
CP-1 
20 
15 
15 
15 
15 
15 
CP-2 
30 
20 
20 
20 
20 
20 
CP-3 
90 
40 
40 
40 
40 
40 
CP-4 
120 
60 
60 
60 
60 
60 
CP-5 
240 
100 
100 
100 
100 
100 
 
The obtained results proved the capability of the algorithms to obtain Pareto fronts of feasible 
solutions. However, due to the nature of the current scheduling problem, solutions of different 
activities’ start times but of identical extension value were encountered in the obtained Pareto 
fronts. Table 13 presents the number of unique solutions of RK chromosomes/particles, schedules, 
and extension values. For all case portfolios, NSGA-II was able to obtain the largest number of 
solutions of unique schedules. In three out of the five case portfolios, NSGA-II obtained identical or 
bigger number of solutions of unique extension values compared to the other algorithms. These 
results indicate that, comparing NSGA-II to SPEA-II and MOPSO, the latter two algorithms have less 
capability of exploring the search space. 
 
Table 13 
Number of unique solutions in the obtained Pareto fronts of the five case portfolios 
Case 
portfolio  
SPEA-II 
NSGA-II 
MOPSO 
RK 
Schedule 
Extension 
RK 
Schedule 
Extension 
RK 
Schedule 
Extension 
CP-1 
15 
15 
15 
15 
15 
13 
15 
15 
15 
CP-2 
16 
12 
9 
20 
20 
11 
20 
12 
8 
CP-3 
26 
15 
15 
40 
40 
16 
40 
26 
16 
CP-4 
36 
19 
12 
56 
56 
18 
60 
21 
15 
CP-5 
75 
47 
29 
100 
100 
36 
100 
80 
39 
 
Evaluating the quality of the obtained Pareto fronts involves comparing the boundary solutions 
based on the extensions presented in Table 14. To compare the boundary solutions obtained by the 
algorithms, the summation of the distance between the boundary solutions of minimum extension 
in project A in the algorithm’s Pareto front and the elite Pareto front, and the distance between the 
boundary solutions of minimum extension in project B in the algorithm’s Pareto front and the elite 
Pareto front was calculated. As presented in Table 15, NSGA-II was able to obtain better boundary 


---

Page 19

---

Decision Making: Applications in Management and Engineering 
Volume 7, Issue 2 (2024) 355-379 
373 
 
 
solutions, which exhibit less distance values, compared to SPEA-II and MOPSO in four out of the five 
case portfolios. 
 
Table 14 
Extensions of projects A and B for the boundary and best compromise solutions of the five case portfolios 
Algorithm 
Solution 
Extensions (days) 
 CP-1 
  CP-2 
 CP-3 
  CP-4 
  CP-5 
A 
B 
A 
B 
A 
B 
A 
B 
A 
B 
SPEA-II 
Boundary solution I 
0 
202 
0 
131 
0 
134 
0 
160 
130 
706 
Best compromise solution 
0 
202 
136 
27 
0 
134 
23 
127 
153 
618 
Boundary solution II 
180 
0 
138 
26 
151 
0 
184 
0 
706 
0 
NSGA-II 
Boundary solution I 
0 
197 
0 
130 
0 
109 
0 
163 
130 
706 
Best compromise solution 
0 
197 
0 
130 
0 
109 
27 
129 
155 
618 
Boundary solution II 
180 
0 
172 
0 
157 
0 
189 
0 
703 
0 
MOPSO 
Boundary solution I 
0 
194 
0 
112 
0 
118 
0 
148 
130 
706 
Best compromise solution 
0 
194 
0 
112 
0 
118 
151 
33 
155 
618 
Boundary solution II 
185 
52 
159 
33 
182 
0 
208 
0 
704 
0 
 
Table 15  
Distance between the boundary solutions of the                                             
algorithm’s Pareto front and the boundary solutions                                              
of the elite Pareto front 
Case 
portfolio 
Distance 
SPEA-II  
NSGA-II  
MOPSO 
CP-1 
8.0 
3.0 
52.2 
CP-2 
61.8 
18.0 
35.5 
CP-3 
25.0 
6.0 
40.0 
CP-4 
12.0 
20.0 
24.0 
CP-5 
3.0 
0.0 
1.0 
 
Further, NSGA-II was found to contribute the most to the set of the elite Pareto solutions in the 
five case portfolios as presented in Table 16. On average, solutions from NSGA-II constitute 52.1% of 
the solutions of the elite Pareto, compared to averages of 27.7% and 20.2% for SPEA-II and MOPSO, 
respectively. Moreover, Table 17 presents the percentage of Pareto solutions of each algorithm that 
is covered by the Pareto fronts of other algorithms. Pareto solutions of NSGA-II were found to cover 
40.0% to 63.8% with an average of 49.5% of the Pareto solutions of SPEA-II, and 41.7% to 96.2% with 
an average of 67.4% of the Pareto solutions of MOPSO. The Pareto solutions of SPEA-II were found 
to cover between 10% to 76% with an average of 48.4% of the Pareto solutions of NSGA-II, and 41.7% 
to 81.3% with an average of 58.8% of the Pareto solutions of MOPSO. The Pareto solutions of MOPSO 
were found to cover between 20.0% to 51.1% with an average of 33.4% of the Pareto solutions of 
SPEA-II, and 2.5% to 40.0% with an average of 24.9% of the Pareto solutions of NSGA-II. Thus, NSGA-
II performance was the best while MOPSO exhibited the worst performance. 
The measured values of the performance metrics of the three algorithms for the five case 
portfolios are presented in Table 18. With respect to the computational time, MOPSO takes 
substantially more time compared to SPEA-II and NSGA-II. This can largely be attributed to the 
implementation of a time-consuming strategy to select the local and global best guide for the 
particles [51].  Regarding the diversity metric Δ, NSGA-II scored lower values compared to SPEA-II and 
MOPSO in case portfolios CP-2, CP-3, and CP-4 which indicates Pareto fronts of better spread and 
distribution. With respect to the spacing metric SP, NSGA-II and MOPSO were better compared to 


---

Page 20

---

Decision Making: Applications in Management and Engineering 
Volume 7, Issue 2 (2024) 355-379 
374 
 
 
SPEA-II. Each of the NSGA-II and MOPSO were found to have the lowest SP value in two case 
portfolios. Thus, the distribution uniformity of the solutions of the obtained Pareto fronts was 
generally better in NSGA-II and MOPSO compared to SPEA-II. With respect to the hyper-volume 
metric HV values, the obtained Pareto fronts of SPEA-II and NSGA-II exhibited slightly higher HV 
values, compared to the MOPSO. This indicates better convergence/diversity for SPEA-II and NSGA-
II compared to MOPSO. Consequently, Pareto fronts of better spread, distribution, and convergence 
are more likely to be obtained using NSGA-II compared to SPEA-II and MOPSO. Generally, MOPSO 
Pareto fronts are of the worst spread, diversity, and convergence. In addition, MOPSO was found to 
consume a substantially higher computational time to solve the optimization problem. 
 
Table 16 
Percent contributions to the elite Pareto front 
Case  
portfolio 
Contributions (%) 
SPEA-II  
NSGA-II  
MOPSO 
CP-1 
27.3 
50.0 
22.7 
CP-2 
21.7 
47.8 
30.4 
CP-3 
42.9 
57.1 
0.0 
CP-4 
24.3 
51.4 
24.3 
CP-5 
22.2 
54.2 
23.5 
Average 
27.7 
52.1 
20.2 
 
Table 17 
Percentages of non-dominated solutions of set B algorithms covered                                     
by those in set A algorithms 
Set A 
SPEA-II 
NSGA-II 
MOPSO 
Set B 
NSGA-II 
MOPSO 
SPEA-II 
MOPSO 
SPEA-II 
NSGA-II 
CP-1 
20.0 
53.3 
60.0 
66.7 
33.3 
26.7 
CP-2 
10.0 
41.7 
41.7 
41.7 
41.7 
40.0 
CP-3 
70.0 
65.4 
40.0 
96.2 
20.0 
2.5 
CP-4 
66.1 
52.4 
42.1 
52.4 
21.1 
32.1 
CP-5 
76.0 
81.3 
63.8 
80.0 
51.1 
23.0 
Average 
48.4 
58.8 
49.5 
67.4 
33.4 
24.9 
 
5. Practical implications 
While the budget allocation ensures that funds are available during the planning horizon of 
multiple fiscal years to support the selected maintenance projects, cash needs to make contractors’ 
payments during some fiscal years might exceed the allocated budgets during these fiscal years. 
Furthermore, variations in the budgets anticipated for the portfolio and modifications in the projects 
occasionally occur, which potentially result in negative cash flow problems that definitely affect the 
progress of the projects. In addition, changes in business environment mandates agencies to 
continually re-assess the priority of projects to conform with the strategic goals of the portfolios. 
Therefore, the cash flow management functions of forecasting, planning, monitoring, and controlling 
of cash flow is very crucial for the achievement of the goals of the programs.  
The merits of the scheduling model include: (1) determine the exact due dates and amounts of 
the contractors’ payments; (2) establish feasible schedules to help owners fully utilize their budgets. 
In addition, the model allows to continually optimize the updated schedules resulting from the 
project monitoring and control process. Furthermore, the information on new projects often change 
in response to factors including the variations in the funding anticipated and the projects’ 


---

Page 21

---

Decision Making: Applications in Management and Engineering 
Volume 7, Issue 2 (2024) 355-379 
375 
 
 
modifications required. The changes in these factors and others require a re-assessment of the 
priority list of projects to conform with the strategic goals of the agency’s portfolio. The proposed 
scheduling model can be continually used during the execution phase to handle these factors through 
changing projects’ priorities and optimizing schedules. 
 
Table 18 
Performance metrics values of SPEAII, NSGA-II, and MOPSO 
Case 
portfolio 
Performance 
metric 
Value 
SPEA-II 
NSGA-II 
MOPSO 
CP-1 
Computational time (s) 
9.77 
11.71 
19.06 
Diversity metric 
0.88 
0.97 
0.88 
Spacing metric 
17.72 
26.43 
15.29 
Hypervolume metric 
0.72 
0.73 
0.72 
CP-2 
Computational time (s) 
24.71 
23.23 
35.35 
Diversity metric 
1.05 
1.04 
1.06 
Spacing metric 
14.70 
17.80 
18.52 
Hypervolume metric 
0.74 
0.73 
0.73 
CP-3 
Computational time (s) 
370.32 
402.03 
473.74 
Diversity metric 
1.09 
1.06 
1.08 
Spacing metric 
12.27 
10.24 
10.79 
Hypervolume metric 
0.73 
0.74 
0.70 
CP-4 
Computational time (s) 
878.86 
1031.01 
1033.82 
Diversity metric 
1.20 
1.12 
1.16 
Spacing metric 
13.98 
10.20 
11.20 
Hypervolume metric 
0.74 
0.73 
0.71 
CP-5 
Computational time (s) 
6734.41 
7051.54 
8907.98 
Diversity metric 
1.43 
1.38 
1.33 
Spacing metric 
31.92 
33.34 
31.00 
Hypervolume metric 
0.74 
0.74 
0.73 
 
6. Conclusions 
This study addresses a significant gap in research and practice representing the fact that highway 
and bridge agencies make budget allocations for M&R projects during the planning stage at the 
network-level while ignoring the closely-related aspect of cash flow. This shortcoming can potentially 
result in cash flow problems during the construction stage, which can delay the progress and 
compromise the successful completion of the projects. Since most M&R projects are outsourced, 
agencies must carefully plan their cash flow. Situations may arise wherein the agency's budget for 
some fiscal years cannot meet the contractors' payment schedules if cash flow is not properly 
planned.  
This research reintroduces the FBS from the perspective of portfolio owners. A FBS model is 
developed to schedule the activities of the portfolio projects, utilize the schedules to define the 
payment schedules of projects’ contractors, calculate the agencies’ cash needs during the fiscal years, 
and utilize the multi-objective optimization algorithms of NSGA-II, SPEA-II, and MOPSO to optimize 
the projects’ schedules to achieve a balance between the cash needs during the fiscal years and the 
available budgets. The output presents to the decision maker a Pareto front with a set of solutions, 
each solution involves the optimized schedules of the individual projects. Thus, the Pareto fronts 
facilitate decision-making regarding the selection of the most appropriate solution based on the set 
priority of projects for early completion. 
Though the three multi-objective optimization algorithms of NSGA-II, SPEA-II and MOPSO 
successfully balanced agencies’ cash-out with cash-in, they were benchmarked using case portfolios 


---

Page 22

---

Decision Making: Applications in Management and Engineering 
Volume 7, Issue 2 (2024) 355-379 
376 
 
 
of different sizes. Generally, NSGA-II was found to outperform SPEA-II and MOPSO. In most of the 
case portfolios, NSGA-II obtained larger Pareto fronts of better convergence and broader spread 
compared to SPEA-II and MOPSO. Generally, MOPSO showed the least favorable performance in 
solving the current problem.  
There are some features in the current study, which can be implemented differently in future 
research. First, the unused amount of the budget in a given fiscal year was rolled over to the following 
fiscal year. Some agencies might not allow to roll the unused budget over to the following fiscal year. 
Second, minimizing the multiple objectives representing the extensions in projects’ completion was 
adopted in the current optimization model. Future research with contextual agencies’ applications 
might consider minimizing the user cost or maximizing the effectiveness of M&R treatments. 
 
Author Contributions 
Conceptualization, A.E.; methodology, A.E. and A.F.; software, A.F.; validation, A.E. and A.F.; formal 
analysis, A.E. and A.F.; investigation, A.E. and A.F.; resources, A.F.; data curation, A.F.; writing—
original draft preparation, A.E.; writing— A.E. and A.F.; visualization, A.F.; supervision, A.E., M.A.A.; 
project administration, A.E., M.A.A.; funding acquisition. All authors have read and agreed to the 
published version of the manuscript. 
 
Funding 
This research received no external funding. 
 
Data Availability Statement 
Any data supporting the reported results will be provided by the authors upon request. 
 
Conflicts of Interest 
The authors declare that they have no known competing financial interests or personal relationships 
that could have appeared to influence the work reported in this paper. 
 
Acknowledgement 
This research was not funded by any grant.  
 
References 
[1]  
OECD. Road transport research. Paris: Bridge Management; 1992. 
[2]   Shim, H., Lee, S., & Kang, B. (2017). Pareto front generation for bridge deck management system using bi-objective 
optimization. KSCE Journal of Civil Engineering, 21, 1563-1572. https://doi.org/10.1007/s12205-016-2569-8   
[3] 
Hegazy, T., Elbeltagi, E., & El-Behairy, H. (2004). Bridge deck management system with integrated life-cycle cost 
optimization. Transportation Research Record: Journal of the Transportation Research Board, 1866, 44-50. 
https://doi.org/10.3141/1866-06  
[4] 
Gao, L., Xie, C., Zhang, Z., & Waller, S. T. (2012). Network‐level road pavement maintenance and rehabilitation 
scheduling for optimal performance improvement and budget utilization. Computer‐Aided Civil and Infrastructure 
Engineering, 27(4), 278-287.  https://doi.org/10.1111/j.1467-8667.2011.00733   
[5] 
Mohammadi, A., Igwe, C., Amador-Jimenez, L., & Nasiri, F. (2022). Applying lean construction principles in road 
maintenance planning and scheduling. International journal of construction management, 22(12), 2364-2374. 
https://doi.org/10.1080/15623599.2020.1788758    
[6] 
Kordestani Ghalenoeei, N., Saghatforoush, E., Athari Nikooravan, H., & Preece, C. (2021). Evaluating solutions to 
facilitate the presence of operation and maintenance contractors in the pre-occupancy phases: a case study of road 
infrastructure 
projects. International 
Journal 
of 
Construction 
Management, 21(2), 
140-152. 
https://doi.org/10.1080/15623599.2018.1512027    


---

Page 23

---

Decision Making: Applications in Management and Engineering 
Volume 7, Issue 2 (2024) 355-379 
377 
 
 
[7]  
Gharaibeh, N. G., Chiu, Y. C., & Gurian, P. L. (2006). Decision methodology for allocating funds across transportation 
infrastructure assets. Journal of infrastructure systems, 12(1), 1-9. https://doi.org/10.1061/(ASCE)1076-
0342(2006)12:1(1)  
[8]  
Mrawira, D., & Amador, L. (2009). Cross-assets trade-off analysis: Why are we still talking about it. Proceedings, 
88th TRB Annual Meeting Compendium of Papers, Transportation Research Board, Washington, DC. 
[9] 
Kuhn, K. D. (2010). Network-level infrastructure management using approximate dynamic programming. Journal 
of Infrastructure Systems, 16(2), 103-111. https://doi.org/10.1061/(ASCE)IS.1943-555X.0000019   
[10] National Cooperative Highway Research Program (2009). An asset-management framework for the interstate 
highway system. National Cooperative Highway Research Program Synthesis Rep. No. 632, Transportation Research 
Board. Washington, DC. 
[11] Fwa, T., & Farhan, J. (2012). Optimal Multiasset Maintenance Budget Allocation in Highway Asset Management. 
Journal of Transportation Engineering, 138, 1179-1187. https://doi.org/10.1061/(ASCE)TE.1943-5436.0000414  
[12] Yeo, H., Yoon, Y., & Madanat, S. (2013). Algorithms for bottom-up maintenance optimisation for heterogeneous 
infrastructure 
systems. Structure 
and 
Infrastructure 
Engineering, 9(4), 
317-328. 
https://doi.org/10.1080/15732479.2012.657649  
[13] Dehghani, M. S., Giustozzi, F., Flintsch, G. W., & Crispino, M. (2013). Cross-asset resource allocation framework for 
achieving 
performance 
sustainability. Transportation 
research 
record, 2361(1), 
16-24. 
https://doi.org/10.3141/2361-03  
[14] Porras-Alvarado, J., Han, Z., & Zhanmin, Z. (2015). A fair division approach to performance-based cross-asset 
resource allocation. In 9th International Conference on Managing Pavement Assets. 
[15] Shi, Y., Xiang, Y., Xiao, H., & Xing, L. (2021). Joint optimization of budget allocation and maintenance planning of 
multi-facility transportation infrastructure systems. European Journal of Operational Research, 288(2), 382-393. 
https://doi.org/10.1016/j.ejor.2020.05.050  
[16] Xu, G., & Guo, F. (2022). Sustainability-oriented maintenance management of highway bridge networks based on 
Q-learning. Sustainable Cities and Society, 81, 103855.  https://doi.org/10.1016/j.scs.2022.103855  
[17]  Ghafoori, M., Abdallah, M., & Ozbek, M. E. (2024). Machine Learning–Based Bridge Maintenance Optimization 
Model for Maximizing Performance within Available Annual Budgets. Journal of Bridge Engineering, 29(4), 
04024011. https://doi.org/10.1061/JBENF2.BEENG-6436  
[18] Mohammadi, M., Rashidi, M., Yu, Y., & Samali, B. (2023). Integration of TLS-derived Bridge Information Modeling 
(BrIM) with a Decision Support System (DSS) for digital twinning and asset management of bridge 
infrastructures. Computers in Industry, 147, 103881. https://doi.org/10.1016/j.compind.2023.103881   
[19] Cao, Q., Zou, X., & Zhang, L. (2022). Multiobjective robust optimization model for generating stable and makespan-
protective repetitive schedules. Journal of construction Engineering and Management, 148(9), 04022099. 
https://doi.org/10.1061/(ASCE)CO.1943-7862.0002348  
[20] Tavakolan, M., & Nikoukar, S. (2022). Developing an optimization financing cost-scheduling trade-off model in 
construction 
project. International 
Journal 
of 
Construction 
Management, 22(2), 
262-277. 
https://doi.org/10.1080/15623599.2019.1619439  
[21] Dabirian, S., Ahmadi, M., & Abbaspour, S. (2021). Analyzing the impact of financial policies on construction projects 
performance using system dynamics. Engineering, Construction and Architectural Management, 30(3), 1201-1221. 
https://doi.org/10.1108/ECAM-05-2021-0431  
[22] Andalib, R., Hoseini, A., & Gatmiri, B. (2018). A stochastic model of cash flow forecasting considering delays in 
owners' 
payments. 
Construction 
Management 
and 
Economics, 
36(10), 
545-564. 
https://doi.org/10.1080/01446193.2018.1433309  
[23] Alavipour, S., & Arditi, D. (2018). Optimizing Financing Cost in Construction Projects with Fixed Project Duration. 
Journal of Construction Engineering and Management, 144(4), 04018012. https://doi.org/10.1061/(ASCE)CO.1943-
7862.0001451  
[24] Su, Y., & Lucko, G. (2015). Synthetic cash flow model with singularity functions. I: Theory for periodic phenomena 
and time value of money. Journal of construction engineering and management, 141(3), 04014078. 
https://doi.org/10.1061/(ASCE)CO.1943-7862.0000938   
 
[25] Lee, D. E., Lim, T. K., & Arditi, D. (2012). Stochastic project financing analysis system for construction. Journal of 
Construction 
Engineering 
and 
Management, 138(3), 
376-389. 
https://doi.org/10.1061/(ASCE)CO.1943-
7862.0000432  
[26] Motawa, I., & Kaka, A. (2009). Modelling payment mechanisms for supply chain in construction. Engineering, 
Construction and Architectural Management, 16(4), 325-336. https://doi.org/10.1108/09699980910970824   


---

Page 24

---

Decision Making: Applications in Management and Engineering 
Volume 7, Issue 2 (2024) 355-379 
378 
 
 
[27] Tang, C. M., Leung, A. Y., & Lam, K. C. (2006). Entropy application to improve construction finance decisions. Journal 
of construction engineering and management, 132(10), 1099-1113. https://doi.org/10.1061/(ASCE)0733-
9364(2006)132:10(1099)  
[28] Lee, C. K., Bujna, M., Abd Jamil, A. H., & Ee, P. T. (2023). A cause and effect of a nonpayment model based on the 
DEMATEL algorithm. Journal of Legal Affairs and Dispute Resolution in Engineering and Construction, 15(1), 
04522050. https://doi.org/10.1061/(ASCE)LA.1943-4170.0000592    
[29] Dorrah, D. H., & McCabe, B. (2023). Integrated Agent-Based Simulation and Game Theory Decision Support 
Framework for Cash Flow and Payment Management in Construction Projects. Sustainability, 16(1), 244. 
https://doi.org/10.3390/su16010244  
[30] Shalaby, A., & Ezeldin, A. S. (2022). A model for work packages optimization in results-based-finance 
projects. Engineering, 
Construction 
and 
Architectural 
Management, 29(7), 
2810-2835. 
https://doi.org/10.1108/ECAM-10-2019-0556  
[31] Liang, Y., Ashuri, B., & Li, M. (2021). Forecasting the construction expenditure cash flow for transportation design-
build projects with a case-based reasoning model. Journal of Construction Engineering and Management, 147(6), 
04021043. https://doi.org/10.1061/(ASCE)CO.1943-7862.0002054   
[32] Farshchian, M. M., Heravi, G., & AbouRizk, S. (2017). Optimizing the owner’s scenarios for budget allocation in a 
portfolio of projects using agent-based simulation. Journal of Construction Engineering and Management, 143(7), 
04017022. https://doi.org/10.1061/(ASCE)CO.1943-7862.0001315    
[33] Huang, W. H., Tserng, H. P., Jaselskis, E. J., & Lee, S. Y. (2014). Dynamic threshold cash flow–based structural model 
for contractor financial prequalification. Journal of construction Engineering and management, 140(10), 04014047. 
https://doi.org/10.1061/(ASCE)CO.1943-7862.0000902  
[34] Jarrah, R. E., Kulkarni, D., & O’Connor, J. T. (2007). Cash flow projections for selected TxDoT highway 
projects. Journal 
of 
construction 
engineering 
and 
management, 133(3), 
235-241. 
https://doi.org/10.1061/(ASCE)0733-9364(2007)133:3(235)  
[35] Elazouni, A. M., & Gab-Allah, A. A. (2004). Finance-based scheduling of construction projects using integer 
programming. Journal 
of 
construction 
engineering 
and 
management, 130(1), 
15-24. 
https://doi.org/10.1061/(ASCE)0733-9364(2004)130:1(15)  
[36] Liu, S. S., & Wang, C. J. (2010). Profit optimization for multiproject scheduling problems considering cash 
flow. Journal 
of 
Construction 
Engineering 
and 
Management, 136(12), 
1268-
1278.https://doi.org/10.1061/(ASCE)CO.1943-7862.0000235  
[37] Alghazi, A., Elazouni, A., & Selim, S. (2013). Improved genetic algorithm for finance-based scheduling. Journal of 
Computing in Civil Engineering, 27(4), 379-394. https://doi.org/10.1061/(ASCE)CP.1943-5487.0000227  
[38] Gajpal, Y., & Elazouni, A. (2015). Enhanced heuristic for finance-based scheduling of construction 
projects. Construction 
Management 
and 
Economics, 33(7), 
531-553. 
https://doi.org/10.1080/01446193.2015.1063676  
[39] Al‐Shihabi, S., & AlDurgam, M. M. (2020). The contractor time–cost–credit trade‐off problem: integer programming 
model, heuristic solution, and business insights. International Transactions in Operational Research, 27(6), 2841-
2877. https://doi.org/10.1111/itor.12764  
[40] Liu, W., Zhang, J., & Liu, W. (2021). Heuristic methods for finance-based and resource-constrained project 
scheduling 
problem. Journal 
of 
Construction 
Engineering 
and 
Management, 147(11), 
04021141. 
https://doi.org/10.1061/(ASCE)CO.1943-7862.0002174  
[41] Liu, W., Zhang, J., Liu, C., & Qu, C. (2023). A bi-objective optimization for finance-based and resource-constrained 
robust 
project 
scheduling. Expert 
Systems 
with 
Applications, 231, 
120623.   
https://doi.org/10.1016/j.eswa.2023.120623  
[42] Zitzler, E., Laumanns, M., & Thiele, L. (2001). SPEA2: Improving the strength Pareto evolutionary algorithm. TIK 
report, 103, 1-18. https://doi.org/10.3929/ethz-a-004284029   
[43] Zitzler, E., & Thiele, L. (1999). Multiobjective evolutionary algorithms: a comparative case study and the strength 
Pareto 
approach. IEEE 
transactions 
on 
Evolutionary 
Computation, 3(4), 
257-271. 
https://doi.org/10.1109/4235.797969  
[44] Gharari, R., Poursalehi, N., Abbasi, M., & Aghaie, M. (2016). Implementation of strength pareto evolutionary 
algorithm ii in the multiobjective burnable poison placement optimization of kwu pressurized water 
reactor. Nuclear Engineering and Technology, 48(5), 1126-1139. https://doi.org/10.1016/j.net.2016.04.004  
[45] Kaucic, M., Moradi, M., & Mirzazadeh, M. (2019). Portfolio optimization by improved NSGA-II and SPEA 2 based on 
different risk measures. Financial Innovation, 5, 26.  https://doi.org/10.1186/s40854-019-0140-6   
[46] Deb, K., Pratap, A., Agarwal, S., & Meyarivan, T. A. M. T. (2002). A fast and elitist multiobjective genetic algorithm: 
NSGA-II. IEEE transactions on evolutionary computation, 6(2), 182-197. https://doi.org/10.1109/4235.996017  


---

Page 25

---

Decision Making: Applications in Management and Engineering 
Volume 7, Issue 2 (2024) 355-379 
379 
 
 
[47] Alothaimeen, I., & Arditi, D. (2020). Overview of Multi-Objective Optimization Approaches in Construction Project 
Management. 
Multicriteria 
Optimization-Pareto-Optimality 
and 
Threshold-Optimality.   
https://doi.org/10.5772/intechopen.88185  
[48]  Wang, Y., Ma, J., & Zhang, Y. (2024). Application of Improved Frog Leaping Algorithm in Multi objective Optimization 
of Engineering Project Management. Decision Making: Applications in Management and Engineering, 7(1), 364-
379. https://doi.org/10.31181/dmame712024896  
[49] Zhang, F. (2024). Constructing a Multi-Objective Optimization Model for Engineering Projects Based on NSGA-II 
Algorithm under the Background of Green Construction. Decision Making: Applications in Management and 
Engineering, 7(1), 37-53. https://doi.org/10.31181/dmame712024895  
[50] Ünal, A. N., & Kayakutlu, G. (2020). Multi-objective particle swarm optimization with random immigrants. Complex 
& Intelligent Systems, 6(3), 635-650.  https://doi.org/10.1007/s40747-020-00159-y   
[51] Abido, M. A. (2010). Multiobjective particle swarm optimization with nondominated local and global sets. Natural 
Computing, 9, 747-766. https://doi.org/10.1007/s11047-009-9171-7  
[52] Bean, J. C. (1994). Genetic algorithms and random keys for sequencing and optimization. ORSA journal on 
computing, 6(2), 154-160. https://doi.org/10.1287/ijoc.6.2.154  
[53] Dhillon, J., Parti, S. C., & Kothari, D. P. (1993). Stochastic economic emission load dispatch. Electric Power Systems 
Research, 26(3), 179-186. https://doi.org/10.1016/0378-7796(93)90011-3  
[54] Schott, J. R. (1995). Fault tolerant design using single and multicriteria genetic algorithm optimization (Doctoral 
dissertation, Massachusetts Institute of Technology). 
[55] El-Abbasy, M. S., Elazouni, A., & Zayed, T. (2020). Finance-based scheduling multi-objective optimization: 
Benchmarking 
of 
evolutionary 
algorithms. Automation 
in 
Construction, 120, 
103392. 
https://doi.org/10.1016/j.autcon.2020.103392  
