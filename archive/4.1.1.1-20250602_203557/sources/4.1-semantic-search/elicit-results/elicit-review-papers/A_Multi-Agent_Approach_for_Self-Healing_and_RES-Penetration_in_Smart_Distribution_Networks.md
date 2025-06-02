

---

Page 1

---

From Single Agent to Multi-Agent: Improving Traffic Signal
Control
Tislenko Maksim1 and Kisilev Dmitrii2
1ITMO University, Saint-Petersburg, e-mail: makstislenko@gmail.com
2HSE University, Moscow, e-mail: dkiseljov@hse.ru
June 21, 2024
Abstract
Due to accelerating urbanization, the importance of solving the signal control problem increases.
This paper analyzes various existing methods and suggests options for increasing the number of agents
to reduce the average travel time. Experiments were carried out with 2 datasets. The results show that
in some cases, the implementation of multiple agents can improve existing methods. For a fine-tuned
large language model approach there’s small enhancement on all metrics.
Keywords: traffic signal control, multi-agent systems, large language model, traffic control agent, re-
inforcement learning.
1
Introduction
The issue of traffic signal control is more relevant than ever. According to the UN report, ”The urban
population of the world has grown rapidly since 1950, having increased from 751 million to 4.2 billion in
2018. Asia, despite being less urbanized than most other regions today, is home to 54 % of the world’s urban
population, followed by Europe and Africa (13% each).[9]”. In 2014, traffic congestion cost Americans over
$ 160 billion in lost productivity and wasted over 3.1 billion gallons of fuel [4]. Traffic congestion was also
attributed to over 56 billion pounds of harmful CO2 emissions in 2011 [12]. In the European Union, the
cost of traffic congestion was equivalent to 1 % of the entire GDP [11]. Consequently, efficient TSC offers
significant economic and environmental benefits, as well as improvements in societal well-being.
There’re lots of different methods how to get less number of traffic congestions, allow people to reach their
destination faster on average from reinforcement learning methods to algorithms based on large language
models. In lots of these effective algorithms, multi-agent approach was not applied despite the fact that it
showed good results as was proved in [8].
In this article, we’ve created a multi-agent system where agents can utilize different approaches, including
those based on Reinforcement Learning (RL) and Large Language Models (LLMs). Our focus is to adapt
the method from a [7] to the domain of traffic signal control and then conduct experiments with multiple
agents to observe and analyze their performance. Specifically, we hypothesize that the combination of RL or
1


---

Page 2

---

From Single Agent to Multi-Agent: Improving Traffic Signal Control
LLM-based approaches can improve traffic signal control by leveraging the strengths of both methodologies.
By using a majority voting mechanism, we aim to aggregate the decisions of diverse agents to achieve a more
robust and effective traffic signal control system. That’s why we are attempting to implement the method
of majority voting among several agents. The details of these methods and their implementation will be
explained further in the article.
The experiments will involve setting up a simulated traffic environment where different agents control
traffic signals at various intersections. We’ve conducted experiments on 2 datasets with 1, 5, or 10 agents
and compared results for different numbers of agents.
2
Related work
Existing research on Traffic Signal Control (TSC) can be categorized into three main approaches: traditional
transportation methods [5, 6, 13], Reinforcement Learning (RL)-based techniques [1, 10, 16, 17], and methods
based on transformers [7, 18, 20]
Transportation methods focus on developing efficient heuristic algorithms that adapt traffic signal con-
figurations dynamically based on real-time lane-level traffic conditions.
However, these methods require
significant manual design and human effort.
The advent of deep neural networks (DNNs) has led to the adoption of deep RL-based techniques, which
have shown impressive performance in various traffic scenarios. Despite their success, RL-based methods
face several challenges. They often struggle with generalizing to larger road networks or rare high-traffic
situations, as their training data covers only a limited range of traffic scenarios. Additionally, RL-based
methods lack interpretability due to the black-box nature of DNNs, making it difficult to understand the
reasoning behind their control actions in specific traffic conditions.
Our research uses the MPLight algorithm that was introduced in [1]. It leverages the concept of pressure
to coordinate multiple intersections.
Pressure is defined as the difference between the queue lengths of
incoming lanes at an intersection and the queue length of the downstream intersection’s receiving lane.
Chen et al. employed pressure as both the state and reward for a DQN agent, which is shared across all
intersections, built on top of the FRAP [22] model. The authors reported that this approach resulted in up
to a 19.2% improvement in travel times compared to the next best method, PressLight [16].
There are also a few methods based on transformers.
For instance, in [21] transformers are used to
characterize traffic conditions better. With the shared Transformer-based cooperation mechanism, intersec-
tion controllers could adequately exploit spatial-temporal correlations and adaptively capture global traffic
dynamics, guiding them to explore collaborative traffic strategies more efficiently.
Also in [7] proposed a new method based on LLMs. In this study, LLMLight was presented, a novel
framework that utilizes large language models (LLMs) as traffic signal control agents.
Specifically, the
framework begins by instructing the LLM with a knowledgeable prompt detailing real-time traffic condi-
tions. By guiding LLMs to perform a human-like, step-by-step analysis of current traffic conditions, the
intelligent agent can make optimal control decisions, thereby improving overall traffic efficiency at intersec-
tions. Extensive experiments on nine traffic flow datasets demonstrate that the framework equipped with
LightGPT, a backbone training procedure for optimizing a traffic signal control-oriented LLM, significantly
outperforms traditional methods, showcasing its exceptional effectiveness and generalization ability across
various traffic scenarios. Leveraging the advanced generalization capabilities of LLMs, LLMLight engages
a reasoning and decision-making process akin to human intuition for effective traffic control. This work
showed that LLMs show results better than traditional RL and transportation methods in some cases. Also,
Page 2


---

Page 3

---

From Single Agent to Multi-Agent: Improving Traffic Signal Control
it is worth noticing that LLM-powered traffic signal control not only shows superior performance across
diverse traffic scenarios but also provides detailed explanations for each decision, contributing to a more
comprehensible and accountable traffic control system. Thus, there is a reason to use LLM for traffic control
problems and try to improve the performance of LLM using various methods.
There’re lots of different ways to improve the performance of existing large language models. For instance
[2] focus on improvement based on a fine-tuning method called Self-Play fIne-tuNing (SPIN), which starts
from a supervised fine-tuned model. At the heart of SPIN lies a self-play mechanism, where the LLM refines
its capability by playing against instances of itself. More specifically, the LLM generates its own training
data from its previous iterations, refining its policy by discerning these self-generated responses from those
obtained from human-annotated data. The method progressively elevates the LLM from a nascent model
to a formidable one, unlocking the full potential of human-annotated demonstration data for SFT. Some of
the recent studies focus on ensemble methods [14, 15] and multiple LLM-Agents collaboration frameworks
[3, 19]. In these works, multiple LLM agents are used to improve the performance of LLMs. For instance,
LLM-Debate [3] employs multiple LLM agents in a debate form. The reasoning performance is improved
by creating a framework that allows more than one agent to ”debate” the final answer to arithmetic tasks.
They show performance improvements compared to using one single agent. All in all, these researches use
under the hood multiple LLMs to increase the performance.
Our work is based on [8]. In this paper simply via a sampling-and-voting method, the performance of
large language models (LLMs) scales with the number of agents instantiated. Also, this method is orthogonal
to existing complicated methods to further enhance LLMs, while the degree of enhancement is correlated
to the task difficulty. Comprehensive experiments were conducted on a wide range of LLM benchmarks to
verify the presence of their finding and to study the properties that can facilitate its occurrence.
3
Method
In this section, we introduce our method and how it is implemented in different algorithms. It is similar to
the method described in [8]. Our method consists of a two-phase process: sampling and voting. During the
sampling phase, we try to generate N samples from N different agents. After generating these samples, the
most popular answer is chosen for each intersection. In the end, as a result, we have an array of actions,
each of which was chosen by majority voting.
3.1
Problem Statement
During our experiments, there were 12 (for the Jinan dataset) or 16 (for the Hangzhou dataset) intersections
with 4 different phases as mentioned in 3. Below is a picture showing the layout of an intersection.
Lanes with the same colour belong to the same phase. It’s worth noting that a right turn on the right
lane (green colour on the image) is always allowed that’s why there’re 4 phases. Our aim in this research is to
minimize average queue length (AQL), average travel time (ATT), and average waiting time (AWT). Connec-
tivity between intersections wasn’t taken into account because it’s hard for LLMs to generalize information
from several intersections.
Consider an environment E with K states s ∈S corresponding to each of K intersections and actions
a ∈A. In the context of a traffic signal control problem, the environment can be understood as the simulated
or real-world traffic system that the control algorithm interacts with. A state in this context can be described
as a comprehensive representation of the current traffic conditions at each intersection within the network,
Page 3


---

Page 4

---

From Single Agent to Multi-Agent: Improving Traffic Signal Control
Fig. 1: Intersection scheme
such as the number of vehicles in each lane, etc. The state should capture all relevant information needed
for the traffic control algorithm to make informed decisions.
Let us have K states corresponding to each of K intersections {s1,...,sK} ∈S. Then at time step t
we will have {s1t,...,sKt} ∈St. In our implementation, the state at each step contains the current phase
and the number of vehicles on each lane. There may be 4 different phases at each intersection: 1. Left-turn
from east and west, 2. Left-turn from north and south, 3. Go-through traffic from east and west, or 4.
Go-through traffic from north and south.
At every time step, the agent chooses the optimal action. An action refers to a specific signal phase
chosen for traffic signal control. Each action corresponds to activating a particular signal phase, such as
allowing go-through traffic from specific directions or enabling left-turn movements.
Let us have N agents {A1,A2,...,AN}, each of which can propose an action ai at each time step t. Our
goal is to choose the optimal action a∗in each state st using a voting method based on the proposed actions
from all agents.
Let πi(skt) be the policy of the i-th agent, which determines the action ai in state skt. The policy is a
decision-making strategy employed by the model for traffic signal control. At each time step t, each agent
Ai proposes an action ai = πi(skt). After receiving all N proposals, we choose action a∗as follows:
a∗= argmaxa
N
∑
i=1
I(ai = a)
where I is an indicator function that equals 1 if ai = a, and 0 otherwise.
Page 4


---

Page 5

---

From Single Agent to Multi-Agent: Improving Traffic Signal Control
3.2
Process Description
Algorithm 1 Sampling Phase
1: Initialization of agents: Each of N agents Ai is initialized with its policy πi.
2: for each state skt k ∈{1,...,K} do
3:
for each agent Ai do
4:
Generate a new action ai = πi(skt)
5:
end for
6: end for
Algorithm 2 Voting Phase
1: Initialize actions collector a
2: for each agent Ai do
3:
Collect an action ai proposed by Ai to actions collector a
4: end for
5: Choosing an action as illustrated in 3.1: Determine the most popular action a∗from a by majority
voting.
6: Executing the action: Execute the chosen action a∗in the environment E.
3.3
Implementation Differences for agents based on LLM and RL Algorithms
There are small differences in implementation for algorithms based on Large Language Models (LLM) and
Reinforcement Learning (RL).
3.3.1
LLM-Based Algorithms
In LLM algorithms, sampling and voting can be conducted based on textual input, where each agent generates
a textual response, and the most frequent response is chosen for further actions. In detail, every agent
gets a prompt where task and scenario description are contained. It’s worth mentioning that the prompt
contains for large language models some facts based on common sense like ”The traffic congestion is primarily
dictated by the early queued vehicles, with the MOST significant impact” because LLMs basically are not
supposed to solve these kind of tasks. The prompt is taken the same as in [7], the full version of it may
be found in appendix A1. The output of the LLM-based agent is primarily textual data in the form of
a reasoning trajectory and control action descriptions. For LLM agents multiagent approach can be used
besause predictions of every agent aren’t deterministic, in our work the temperature hyperparameter is set
to 0.1. The temperature parameter modifies the probabilities of the next word in the sequence by scaling the
logits (the raw predictions from the model) before applying the softmax function. This output is generated
by the agent to provide insights into the decision-making process and the selected actions for traffic signal
control at intersections.
Page 5


---

Page 6

---

From Single Agent to Multi-Agent: Improving Traffic Signal Control
3.3.2
RL-Based Algorithms
In the realm of Reinforcement Learning (RL), particularly within the multi-agent paradigm, the orchestra-
tion of network updates necessitates a meticulously orchestrated preparation of states for each individual
agent. This preparatory phase is indispensable, serving as the bedrock upon which subsequent algorithmic
operations rest. This was done for each agent in the current paper.
Also in MPlight, unlike the LLM-based approach, training is conducted, learning rate is 0.001. The input
state and target value for each agent are prepared during network updates.
Multi-agent approach which is based on the independence of agents can be used because the recommen-
dations of every agent may vary. The reason of varying recommendations is that during the initialization
of MPLight agents, the weights are initialized randomly. Also when selecting an action, agents may choose
a random action with some probability. When preparing states and target values for each agent, data is
randomly selected from memory (storage of previous interactions with the environment).
3.4
Algorithm pipeline
We propose to create a multi-agent system by integrating several (1, 5 or 10) large language models (LLMs)
or reinforcement learning (RL) models. This approach aims to leverage the strengths of different models,
enhance accuracy, and improve overall system performance by distributing tasks among specialized agents.
To create this system we initialized several identical models which were taken from 3.3. These models
generate different actions for each state. From each model, we receive a recommended signal. Using the
voting method described in Section 3.1, we determine the final action. Each model’s recommendation is
considered a vote, and the action with the most votes is selected as the final action. This approach helps
to aggregate the diverse recommendations from multiple models, ensuring a more robust decision-making
process.
The algorithm below illustrates the whole pipeline of the multi-agent version of the method. It includes
initialization, action generation, voting, final action selection and metrics calculation.
The multi-agent
system is designed to handle various traffic conditions by dynamically adjusting the traffic signals based on
real-time data. By doing so, the system can adapt to varying traffic patterns throughout the day, ensuring
smooth traffic flow even during peak hours.
Moreover, the use of multiple agents for each intersection
allows for scalability, enabling the system to manage traffic in large urban areas with numerous intersections
effectively.
In the algorithm below there’s following variables introduced:
• Qi is the queue length at intersection i.
• Wi is the waiting time at intersection i.
• Ti is the travel time for vehicle i i.
• n is the number of vehicles.
Page 6


---

Page 7

---

From Single Agent to Multi-Agent: Improving Traffic Signal Control
Algorithm 3 Pipeline of the multi-agent version of algorithm
1: Initialize the total run count T and minimum action time τ from the configuration .
2: Reset the environment and obtain the initial for all intersections state S0.
3: for each time step t in range of T/τ do
4:
Initialize empty lists for action A.
5:
for each skt, k ∈{1,...,K} do
6:
Get the information about skt.
7:
end for
8:
Initialize an empty list for prompts P.
9:
for each skt, k ∈{1,...,K} do
10:
Generate a prompt pk from the skt and append the prompt to P.
11:
end for
12:
Initialize an empty list for responses R
13:
for each skt, k ∈{1,...,K} do
14:
Generate response rk from the LLM agents using pk by majority voting.
15:
Decode the response and append to R.
16:
end for
17:
Initialize an empty action list A
18:
for each rk k ∈{1,...,K} do
19:
Get the signal from response
20:
Append the action code corresponding to the signal to A.
21:
end for
22:
Step the environment with A and set state St+1.
23:
Compute
Q = 1
K
K
∑
i=1
Qi
24:
Compute
W = 1
K
K
∑
i=1
Wi
25: end for
26: Compute
Ttotal =
n
∑
i=1
Ti
27: return Ttotal,W,Q
Page 7


---

Page 8

---

From Single Agent to Multi-Agent: Improving Traffic Signal Control
4
Experimental setup
4.1
Datasets
In this research, we have performed a comparison using 2 datasets: Jinan and Hangzhou. For the Jinan
dataset there’s 12 intersections (4x3), for the Hangzhou dataset there’s 16 intersections (4x4). The Jinan
dataset was collected from the Dongfeng subdistrict, Jinan, China, the Hangzhou dataset was collected in
the Gudang subdistrict, Hangzhou, China.
4.2
Metrics
There’re 3 metrics that were used to compare methods with a different number of agents: average travel
time (ATT) which measures the mean duration that vehicles take to travel from their origins to their
respective destinations, average queue length (AQL) which refers to the mean number of vehicles queuing in
the road network, average waiting time (AWT) that quantifies the mean time that vehicles spend queuing
at intersections within the road network.
4.3
Compared methods
There’re 5 methods compared: 2 transportation, 2 based on LLM, and 1 based on reinforcement learning.
Below is a short explanation of these methods.
The Fixed Time Algorithm for traffic signal control is one of the simplest and most widely used methods
for managing traffic flow. The main idea is that traffic lights switch between phases according to a prede-
termined schedule, regardless of the current traffic conditions. This algorithm uses fixed schedules to switch
traffic light phases. It does not consider current traffic conditions. All traffic lights switch according to the
fixed schedule, regardless of the number of vehicles at the intersection. This method is easy to implement
and does not require constant monitoring and updating of traffic data, reducing operational costs.
The Max Pressure algorithm is an advanced traffic signal control method designed to optimize traffic flow
at intersections by dynamically adjusting signal phases. The core idea is to use real-time information about
vehicle queues to make decisions that minimize overall delays and congestion. The algorithm dynamically
adjusts the signal phases at each intersection based on real-time traffic conditions, specifically the vehicle
queues at each approach. The final decision depends on the calculation of pressure a difference between
the incoming and outgoing queues. Unlike some other algorithms, this algorithm does not require prior
knowledge of average traffic demands. It operates solely on current traffic data, making it adaptable to
real-time conditions.
The MPLight algorithm is an advanced traffic signal control method that combines the principles of
the Max Pressure (MP) algorithm with machine learning techniques, specifically reinforcement learning, to
improve traffic management. By setting the reward of RL agents to be the same as max pressure control
objective, each local agent is maximizing its own cumulative reward, which further maximizes the network
throughput under certain constraints. Implementing MPLight may require integration with existing traffic
management systems and sensors, which could involve additional costs and technical challenges.
The main idea of the LLMLight algorithm is to use a Light Language Model (LLM) called LLMLight
for optimized traffic signal control. It leverages LLMs to make effective control actions based on reasoning
trajectories and aligns with long-term traffic flow goals. The algorithm aims to enhance traffic efficiency by
prioritizing lanes with congestion and providing detailed rationales for decision-making in a transparent and
explainable manner. This algorithm requires lots of computational capabilities but for the enhanced version
Page 8


---

Page 9

---

From Single Agent to Multi-Agent: Improving Traffic Signal Control
of LLM fine-tuned specifically for the TSC problem, LightGPT, results on average are better than for any
other method.
5
Experimental results
Below on the table 1 results of performances are introduced. For algorithms based on RL and LLMs to
compare their performance with different numbers of agents this number was 1, 5 or 10. The simulation
time is 1 hour. For fixed and Max pressure algorithms number of agents is constant and equal to 1 because
the larger number of agents doesn’t make sense. The best results for each metric and dataset are highlighted
in bold.
Method
Jinan
Hangzhou
ATT
AQL
AWT
ATT
AQL
AWT
Fixed (1 agent)
481.793
491.033
70.987
616.017
301.325
73.987
Max pressure (1 agent)
282.579
170.708
44.532
325.329
68.992
49.601
MPLight (1 agent)
307.82
215.93
97.88
345.60
84.7
81.97
MPLight (5 agent)
304.987
209.117
99.929
349.054
87.617
98.149
MPLight (10 agent)
298.79
201.20
91.795
353.183
91.342
125.905
Llama 13b (1 agent)
403.67
371.55
135.979
458.95
175.08
199.41
Llama 13b (5 agent)
401.12
371.91
133.524
449.04
161.375
159.192
Llama 13b (10 agent)
404.92
370.575
139.23
441.44
160.901
199.45
LightGPT (1 agent)
277.259
164.275
46.657
312.413
58.433
47.004
LightGPT (5 agent)
277.29
163.5
45.692
312.059
57.65
47.882
LightGPT (10 agent)
274.854
159.775
45.847
311.576
57.53
46.079
Table 1: Performances of models with different number of agents
6
Experimental analysis
As we can see from the table above for some datasets and models multiagent approach shows good results.
For the MPLight algorithm there’s a good advance in results for the Jinan dataset. The reason of it
is that in the Hangzhou dataset number of intersections is more than in the Jinan dataset. For the Jinan
dataset, the number of intersections is one-third less than that of the Hangzhou dataset. In large intersection
datasets, the number of interactions and situations increases, which complicates the learning task. With a
higher number of agents at a single intersection, the complexity grows exponentially, which can lead to a
deterioration in results.
For the LLMLight algorithm based on Llama 13b proposed method doesn’t show any enhancement. The
reason is that this model was not trained for traffic signal control problem and it is too weak for this kind
of task. Because of it during conducting experiments the dispersion of Llama 13b results was bigger than
on any other methods. Unlike Llama13b LightGPT model shows some improvement in most of all metrics
with an increasing number of agents, it showed stable values of metrics.
In the context of LLMs, it is important to note that their effectiveness in specific management tasks
heavily depends on the quality of their pre-training. Models specifically trained on data related to trans-
Page 9


---

Page 10

---

From Single Agent to Multi-Agent: Improving Traffic Signal Control
portation systems and traffic signal control can show significantly better results. Therefore, investing in the
training of specialized models can be a strategically justified decision to improve the performance of traffic
management systems. This is evident when comparing the results of Llama 13b and LightGPT, which is
essentially a fine-tuned version of Llama 13b.
All in all, our results may be summarized using 3 points:
1. The multi-agent approach for RL algorithms shows good results for datasets with a small number of
intersections.
2. For ”weak” LLMs multiagent approach doesn’t show any enhancement because of their instability in
results.
3. For fine-tuned LLMs multiagent approach allows to reach small advance in all metrics.
All in all, for cities that have lots of computational capabilities multi-agent approach with a fine-tuned
LightGPT model can show the best results among all possible options. If there’s not enough computational
resources Max pressure algorithm shows good results on all datasets.
7
Conclusion
In this paper, we’ve successfully created multi-agent system and conducted experiments with it for different
RL and LLM-based algorithms. Our experiments showed that for some cases especially for fine-tuned LLM
models, there’s some enhancement when several agents are used. In future works we are going to provide more
experiments with different RL-based and LLM-based algorithms. Also, we are going to try this approach
with different types of agents and compare it with the results from this paper.
In conclusion, the choice of approach and model for traffic signal control should be based on an analysis
of the number of intersections and available computational resources to ensure optimal system performance.
Considering the specifics of each city, adapting the approach may include tuning algorithms, improving data
quality, and utilizing advanced distributed learning methods. The development of more sophisticated models
and algorithms may also involve integrating real-time data, which will allow for more accurate responses to
changing traffic conditions and enhance the overall efficiency of the management system.
Page 10


---

Page 11

---

From Single Agent to Multi-Agent: Improving Traffic Signal Control
References
[1] Chacha Chen, Hua Wei, Nan Xu, Guanjie Zheng, Ming Yang, Yuanhao Xiong, Kai Xu, and Zhenhui
Li. Toward a thousand lights: Decentralized deep reinforcement learning for large-scale traffic signal
control. Proceedings of the AAAI Conference on Artificial Intelligence, 34:3414–3421, April 2020.
[2] Zixiang Chen, Yihe Deng, Huizhuo Yuan, Kaixuan Ji, and Quanquan Gu. Self-play fine-tuning converts
weak language models to strong language models, 2024.
[3] Yilun Du, Shuang Li, Antonio Torralba, Joshua B. Tenenbaum, and Igor Mordatch. Improving factuality
and reasoning in language models through multiagent debate, 2023.
[4] The Economist. The cost of traffic jams. https://www.economist.com/blogs/economist-explains/
2014/11/economist-explains-1, 2014. November 2014.
[5] PB Hunt, DI Robertson, RD Bretherton, and M Cr Royle. The scoot on-line traffic signal optimisation
technique. Traffic Engineering & Control, 23(4), 1982.
[6] Peter Koonce and Lee Rodegerdts.
Traffic signal timing manual.
Technical report, United States.
Federal Highway Administration, 2008.
[7] Siqi Lai, Zhao Xu, Weijia Zhang, Hao Liu, and Hui Xiong. Llmlight: Large language models as traffic
signal control agents, 2024.
[8] Junyou Li, Qin Zhang, Yangbin Yu, Qiang Fu, and Deheng Ye. More agents is all you need, 2024.
[9] Department of Economic and United Nations Social Affairs. World Urbanization Prospects 2018. United
Nations, New York, 2019.
[10] Afshin Oroojlooy, MohammadReza Nazari, Davood Hajinezhad, and Jorge Silva. Attendlight: Universal
attention-based reinforcement learning model for traffic signal control. In Advances in Neural Infor-
mation Processing Systems 33: Annual Conference on Neural Information Processing Systems 2020,
NeurIPS 2020, virtual, December 2020.
[11] David Schrank, Bill Eisele, and Tim Lomax. Tti’s 2012 urban mobility report. Technical Report 4,
Texas A&M Transportation Institute, The Texas A&M University System, 2012.
[12] David Schrank, Bill Eisele, Tim Lomax, and Jim Bak. 2015 urban mobility scorecard, 2015. Published
by Texas A&M Transportation Institute.
[13] Pravin Varaiya. Max pressure control of a network of signalized intersections. Transportation Research
Part C: Emerging Technologies, 36:177–195, 2013.
[14] Fanqi Wan, Xinting Huang, Deng Cai, Xiaojun Quan, Wei Bi, and Shuming Shi. Knowledge fusion of
large language models, 2024.
[15] Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Huai hsin Chi, and Denny Zhou.
Self-
consistency improves chain of thought reasoning in language models. ArXiv, abs/2203.11171, 2022.
Page 11


---

Page 12

---

From Single Agent to Multi-Agent: Improving Traffic Signal Control
[16] Hua Wei, Chacha Chen, Guanjie Zheng, Kan Wu, Vikash V. Gayah, Kai Xu, and Zhenhui Li. Presslight:
Learning max pressure control to coordinate traffic signals in arterial network. In Proceedings of the
25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, KDD 2019,
pages 1290–1298, Anchorage, AK, USA, August 4-8 2019. ACM.
[17] Hua Wei, Nan Xu, Huichu Zhang, Guanjie Zheng, Xinshi Zang, Chacha Chen, Weinan Zhang, Yanmin
Zhu, Kai Xu, and Zhenhui Li. Colight: Learning network-level cooperation for traffic signal control. In
Proceedings of the 28th ACM International Conference on Information and Knowledge Management,
CIKM 2019, pages 1913–1922, Beijing, China, November 3-7 2019. ACM.
[18] Qiang Wu, Mingyuan Li, Jun Shen, Linyuan L¨u, Bo Du, and Ke Zhang. Transformerlight: A novel
sequence modeling based traffic signaling mechanism via gated transformer. In Proceedings of the 29th
ACM SIGKDD Conference on Knowledge Discovery and Data Mining, KDD 2023, pages 2639–2647,
Long Beach, CA, USA, August 6-10 2023. ACM.
[19] Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Shaokun Zhang, Erkang Zhu, Beibin Li, Li Jiang,
Xiaoyun Zhang, and Chi Wang. Autogen: Enabling next-gen llm applications via multi-agent conver-
sation framework, 08 2023.
[20] Xue Ye, Shen Fang, Fang Sun, Chunxia Zhang, and Shiming Xiang. Meta graph transformer: A novel
framework for spatial-temporal traffic prediction. Neurocomputing, 491, 12 2021.
[21] Chen Zhao, Xingyuan Dai, Xiao Wang, Lingxi Li, Lv Yisheng, and Fei-Yue Wang. Learning transformer-
based cooperation for networked traffic signal control. In 2022 IEEE 25th International Conference on
Intelligent Transportation Systems (ITSC), pages 3133–3138, 10 2022.
[22] G. Zheng, Y. Xiong, X. Zang, J. Feng, H. Wei, H. Zhang, Y. Li, K. Xu, and Z. Li. Learning phase
competition for traffic signal control. In Proceedings of the 28th ACM International Conference on
Information and Knowledge Management, pages 1963–1972, 2019.
Page 12


---

Page 13

---

From Single Agent to Multi-Agent: Improving Traffic Signal Control
A
1
A traffic light regulates a four-section intersection with northern, southern, eastern, and western sections,
each containing two lanes: one for through traffic and one for left-turns. Each lane is further divided into
three segments. Segment 1 is the closest to the intersection. Segment 2 is in the middle. Segment 3 is
the farthest. In a lane, there may be early queued vehicles and approaching vehicles traveling in different
segments. Early queued vehicles have arrived at the intersection and await passage permission. Approaching
vehicles will arrive at the intersection in the future. The traffic light has 4 signal phases. Each signal relieves
vehicles’ flow in the group of two specific lanes. The state of the intersection is listed below. It describes:
- The group of lanes relieving vehicles’ flow under each signal phase.
- The number of early queued vehicles of the allowed lanes of each signal.
- The number of approaching vehicles in different segments of the allowed lanes of each signal.
<<There is information about current state>>
Please answer: Which is the most effective traffic signal that will most significantly improve the traffic
condition during the next phase? Requirements:
- Let’s think step by step.
- You can only choose one of the signals listed above.
- You must follow the following steps to provide your analysis:
Step 1: Provide your analysis for identifying the optimal traffic signal.
Step 2: Answer your chosen signal.
- Your choice can only be given after finishing the analysis.
- Your choice must be identified by the tag: <signal>YOUR CHOICE</signal>.
Page 13
