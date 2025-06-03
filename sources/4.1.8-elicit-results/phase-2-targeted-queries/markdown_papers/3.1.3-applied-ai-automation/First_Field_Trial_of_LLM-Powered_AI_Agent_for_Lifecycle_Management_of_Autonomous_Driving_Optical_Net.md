# First Field Trial of LLM-Powered AI Agent for Lifecycle Management of Autonomous Driving Optical Networks

## Paper Metadata

- **Filename:** First Field Trial of LLM-Powered AI Agent for Lifecycle Management of Autonomous Driving Optical Networks.pdf
- **DOI:** None
- **Authors:** Not available
- **Year:** Not available
- **Journal/Venue:** Not available
- **URL:** Not available
- **Extraction Date:** 2025-06-03T15:04:10.296616
- **Total Pages:** 4

## Abstract

Abstract not available from BibTeX metadata.

## Keywords

Keywords not available from BibTeX metadata.

---

## Full Text Content



### Page 1

First Field Trial of LLM-Powered AI Agent for Lifecycle 
Management of Autonomous Driving Optical Networks 
Xiaomin Liu, Qizhi Qiu, Yihao Zhang, Yuming Cheng, Lilin Yi, Weisheng Hu, and Qunbi Zhuge* 
 
State Key Laboratory of Advanced Optical Communication Systems and Networks, Department of Electronic Engineering, Shanghai Jiao Tong University, Shanghai, China, *qunbi.zhuge@sjtu.edu.cn 
 
Abstract We design and demonstrate the first field trial of LLM-powered AI Agent for ADON. Three 
operation modes of the Agent are proposed for network lifecycle management. The Agent efficiently 
processes wavelength add/drop and soft/hard failures, and achieves comparable performance to human-designed algorithms for power optimization. ©2024 The Author(s) 
Introduction 
Autonomous driving optical networks (ADON) are 
being developed to improve network efficiency, 
reliability and performance [1-2]. However, it is 
extremely challenging to design comprehensive 
solutions in the conventional manner for all possible events throughout a lifecycle of an optical 
network. Recently, the remarkable advances in 
large language models (LLMs) have catalysed 
the emergence of LLM-powered AI Agents [3-4]. 
Such an Agent is an intelligent entity that leverages LLM as its brain to generate strategies and 
employ tools to interact with the physical environment and tackle complex tasks. For optical networks, the Agent holds the potentials to realize a 
full ADON. To date, an AI Agent for the operations of the entire ADON lifecycle has yet to be 
investigated and developed. 
In this paper, we design and demonstrate the 
first field trial of an LLM-powered AI Agent to automate lifecycle-level ADON operations. We develop three distinct operation modes of the Agent, 
tailored to leverage current LLMs’ capabilities in 
addressing diverse optical network events. In the 
field-trial testbed, typical events during a network 
lifecycle are emulated and autonomously handled by the Agent from the beginning of life (Bo L) 
to the end of life (Eo L), covering service establishment, wavelength add/drop, and hard/soft failures. During these events, the Agent autonomously conducts optical amplifier (OA) optimization to achieve a near-optimal Q-factor, constructs a digital twin (DT) model of the link with a 
high accuracy, and successfully localize and 
recover failures including fiber cut and link aging 
within tens of seconds. Moreover, we compare 
the capabilities of various LLMs in directly optimizing OAs, further demonstrating the potential 
of LLM in tackling complex tasks for ADON. 
LLM-powered AI Agent for ADON 
Fig. 1 shows the proposed AI Agent to enable autonomous network operations throughout the 
lifecycle. The central unit of the AI Agent is a 
Planner, which performs strategy and workflow 
generation, information analysis, and decisionmaking. Moreover, the Agent comprises four 
modules: 1) Knowledge Retrieval (K. R.) to provide domain knowledge; 2) Monitoring & Analytics (M. A.) to collect data and conduct data analysis; 3) DT Construction to synchronize digital 
models with the real-time network; 4) Management & Control (M. C.) to conduct network operations such as optical power optimization. 
We define three operation modes of the AI 
Agent based on the LLM’s capability for different 
tasks.1) LLM-native mode: the Agent exclusively relies on LLM for planning, reasoning, and 
execution without any human-designed algorithms; 2) LLM-centric mode: the Agent employs 
LLM for planning and reasoning while leveraging 
some human-designed algorithms; 3) Rule-centric mode: the LLM-powered Agent guides the 
Planner to retrieve and execute pre-defined workflows with existing tools/algorithms. Notably, 
these modes are all autonomous without human 
intervention, and LLM can be designed to perform mode selection for a given task. 
 
Fig. 1. Architecture of the proposed LLM-powered AI Agent for ADON. 
Establish 
Services
Bo L
…
Add/Drop
Events
Failure
Events
Terminate 
Services
LLM
Planner
AI Agent
Eo L
−Transfer learning
synchronization
−Memory-aware synapses
−Routing and wavelength
assignment
−Optical power optimization
Hardware Interface
SDN Controller
ADON Lifecycle
User
Requirements
Physical layer
Hardware
Digital Twin
Construction
Management
& Control
Monitoring 
& Analytics
Knowledge
Retrieval
User Interface
Documents
Expert knowledge
Operation manual
−Real-time telemetry
−System logs
−Historical database
Version submitted to ECOC PDP 2024 
on September 6th

---


### Page 2

In the field trial, we demonstrate the applications of all the three modes, and the flow diagrams are shown in Fig. 2. For dynamic wavelength add/drop operations, we illustrate both the 
LLM-native mode and Rule-centric mode as per 
Fig. 2(a). For the former, the Agent adds or drops 
wavelengths first and then performs power optimization. We propose to use the LLM to directly 
optimize the OA gains based on a Re Act framework with an iterative thought-action-observation 
loop [5]. For the latter, the pre-defined workflow 
and algorithm are based on Auto-DTWave [6], 
which can simultaneously optimize power and 
synchronize DT. 
Fig. 2(b) illustrates how the Agent handles failures in the LLM-centric mode. The process is initiated upon the detection of a Q-factor drop or the 
forecast of power degradation by the M. A. module. The LLM within the Planner then formulates 
a workflow, which involves the LLM analysing 
documents and logs via Retrieval Augmented 
Generation (RAG) [7] ①, localizing the failure ②, 
and generating recovery solutions ③. Notably, 
steps ② and ③ rely solely on the LLM without 
external algorithms. Then, the Planner autonomously executes the recovery process by conducting power optimization ④ while synchronizing the DT accordingly ⑤. 
Field-trial Testbed and Agent Implementation 
Fig. 3 plots our field-deployed testbed with commercial equipment from Shanghai via Jiaxing to 
Hangzhou in China. It consists of a 440-km loop 
link with four spans of G.652.D fibers and six OAs. 
Six transponders operating at 63.9 GBaud and 
200 Gbps are adopted. We emulate a transmission scenario with up to 30 wavelengths in a 75GHz fixed grid. The wavelengths are added or 
dropped in batches. Each batch contains one real 
signal and four dummy signals. 
A software-defined network (SDN) controller 
embedded with the Agent is developed. The 
Agent is built based on Lang Chain using the planand-execute framework [8]. The control commands are launched from the Agent to the hardware through the NETCONF protocol using 
YANG models. Our testbed supports millisecondlevel telemetry data collection, which significantly 
enhances the capability of the Agent. These telemetry data are transmitted through the optical 
supervisory channel (OSC) to the SDN server. 
Plentiful operation and device logs are stored in 
the SDN server for the Agent to generate more 
effective strategies. 
Field-trial Results 
Typical events throughout a network lifecycle 
were emulated as shown in Fig. 4(b), and we 
adopted GPT-4o in the Agent to address them [9]. 
At the Bo L, 4 batches of wavelengths (20 wav.) 
were established. During our experiment, an actual fiber cut truly occurred between Jiaxing and 
Shanghai, and this was included as a hard failure 
event. After the recovery of it, service add/drop 
events were generated by changing the link load 
from 20 to 30, 25, and 15 wavelengths. Then, to 
emulate progressive link aging, we employed variable optical attenuators to gradually increase fiber attenuation. Finally, new services were added 
to increase the link load to 30 wavelengths. 
Rule-centric mode performance. We first 
employ the Agent with the Rule-centric mode for 
the wavelength add/drop events. The Agent autonomously executes the workflow of AutoDTWave [6] for DT synchronization and power 
optimization by adjusting the gain and tilt of each 
OA. Fig. 4(a) shows the Q-factors’ changes during the emulated lifecycle events (Fig. 4(b)). The 
Agent's converged Q-factor deviates <0.3-d B on 
average from the brute-force optimum. To test 
the DT’s accuracy, three sets of 300 data each 
are collected, with different loadings and OA configurations at three stages: 1) before the fiber cut, 
2) after the fiber cut, and 3) after the link aging 
 
Fig. 2. The flow diagrams of the Agent-enabled (a) dynamic wavelength add/drop and (b) failure handling. 
 
Fig. 3. Field-trial testbed. 
Version submitted to ECOC PDP 2024 
on September 6th

---


### Page 3

event. In Fig. 4(c), compared to the offline Gaussian noise model [10] with known parameters, the 
DT constructed by the Agent reduces the root 
mean square error from 1.72 d B to 0.56 d B. 
LLM-centric mode performance. Fig. 4(d)-(f) 
illustrate the Agent's fiber cut management in the 
LLM-centric mode. Based on the LLM aided by 
operation manuals, the Agent autonomously generates a workflow, and then analyses system logs, 
OSC messages, and telemetry data. Finally, it 
successfully identifies the fiber cut between Jiaxing and Shanghai in 13 seconds. Fig. 4(g)-(i) illustrate the AI Agent’s performance in dealing 
with link aging. As shown in Fig. 4(h), the M. A. 
module triggers the failure handling upon predicting a potential 5-d B power loss. The Planner then 
autonomously generates a workflow using the 
LLM. Accordingly, the Agent retrieves datasheets 
and queries optical powers to calculate the attenuation of each span within a minute. Then, it reconfigures the OAs to recover the transmission 
performance degradation. The above results 
show the strong reasoning capability of the LLM 
as it can process diverse failure-related information across multiple sources and formats. 
LLM-native mode performance. Finally, we 
evaluate the capabilities of LLMs in optimizing the 
OA gains in the LLM-native mode. As shown in 
Fig. 5, the 7 LLMs developed by 4 companies 
show very different performance. Impressively, 3 
of them can achieve results comparable to the 
Bayesian optimization (BO) approach [11], 
demonstrating great potential to address intractable tasks that lack solutions today, especially 
considering they are still rapidly evolving. 
Conclusions 
We design and demonstrate the first field trial of 
an LLM-powered AI Agent for ADON lifecycle 
management. It autonomously handles multiple 
representative events in an emulated network 
lifecycle, including wavelength add/drop and failure handling. We further show that LLM has great 
potential in tackling intractable tasks for ADON. 
 
Fig. 4. (a) Q-factor variations during service add/drop, failure occurrence, and failure recovery. (b) The investigated events 
during the emulated lifecycle. (c) The corresponding DT estimation error over various independent test sets. (d-f) The system 
log, real-time telemetry, and AI Agent’s outputs during the real fiber cut event. (g-i) The real-time telemetry, time series forecasting, and AI Agent’s outputs during the link aging event. 
(a) 
(b) 
Fiber
cut,
trigger
failure management.
Trigger failure
management.
Time slot [a.u.]
Optical power [d Bm]
5 d B
-
-
-
Telemetry
Forecast
Fiber3
Fiber4
Fiber1
Fiber2
System Log for fiber cut
Telemetry for fiber cut
OSC link down
Input power failure
Operation log
Planner: To localize the cause of Q -drop, follow 
these steps: 
1. Check the OSC message. If it is not received…
 
2. If the OSC message is received, check the 
EDFA6 input power. If it is greater than -20d Bm… 
3. If the power is less than -20d Bm, analyze… 
Final Answer: 
 A possible fiber cut in the 
Fiber [ID: JX-ODF1-B7-B8]. 
Action:```{"action": " check_osc " …}``` 
Observation: No OSC signal received. 
Thought: Since no OSC signal was received, it … 
Action:```{"action": " query_input_power "…}``` 
Observation: -60.0 
Thought: Since the input power of EDFA6 is … 
Action: ```{“action”: “Final Answer”…}``` 
Telemetry for aging
Planner: 
 To analyze the causes of the power 
degradation, follow these steps: 
1. Check the link configuration … 
2. Calculate the attenuation of… 
3. Compare the calculated attenuation 
values with the standard values from… 
Final Answer: 
 The fibers with errors 
are identified: 
Fiber [ID: JX-ODF2-B7-B8] 
Fiber [ID: HZ-ODF2-B7-B8] 
 
Action: 
```{"action": " search_and_anwser ", 
"action_input ": {"query": … 
Observation: The link configuration 
consists of alternating EDFAs and 
fibers, with the standard … 
Thought: The link configuration… The 
standard attenuation … 
Thought: To optimize the network 
based on the identified errors … 
Action:```{"action": "Optimization 
tool", "action_input ": … 
Agent’s handling 
process for aging 
(d) 
(e) 
(g) 
(i) 
(f) 
(h) 
ILA Input 
power [d Bm]
-5
-10
2024-08-27 17:36:01
2024-08-27 17:36:53
-10
PA Input 
power [d Bm]
-30
-50
2024-08-27 08:46:05
2024-08-27 08:46:18
-60
Agent’s handling 
process for fiber cut 
Time series forecasting 
Triggered
(c) 
EVENTS Add 4 batches
(20 wav.)
Fiber cut recov.
(20 wav.)
Add 2 batches
(30 wav.)
Drop 1 batch
(25 wav.)
Drop 2 batches
(15 wav.)
Aging
(15 wav.)
Aging recov.
(15 wav.)
Add 3 batches
(30 wav.)
Time slot [a.u.]
 
Fig. 5. Comparison of OA gain optimization performance. 
Version submitted to ECOC PDP 2024 
on September 6th

---


### Page 4

Acknowledgements 
This work was supported by Shanghai Pilot Program for Basic Research - Shanghai Jiao Tong 
University (21TQ1400213) and National Natural 
Science Foundation of China (62175145). 
 
References 
[1] A. Richard, “Autonomous networks: empowering digital 
transformation for telecoms industry,” 
https://www.tmforum.org/wp-content/uploads/2019/05 
/22553-Autonomous-Networks-whitepaper.pdf, accessed on 6 September 2024. 
[2] Q. Zhuge, X. Liu, Y. Zhang, M. Cai, Y. Liu, Q. Qiu, X. 
Zhong, J. Wu, R. Gao, L. Yi, W. Hu, “Building a digital 
twin for intelligent optical networks [Invited Tutorial],” 
Journal of Optical Communications and Networking, vol. 
15, no. 8, pp. C242-C262, 2023, DOI: 
10.1364/JOCN.483600. 
[3] Z. Xi, W. Chen, X. Guo, W. He, Y. Ding, B. Hong, M. 
Zhang, J. Wang, S. Jin, E. Zhou, R. Zheng, X. Fan, X. 
Wang, L. Xiong, Y. Zhou, W. Wang, C. Jiang, Y. Zou, X. 
Liu, Z. Yin, S. Dou, R. Weng, W. Cheng, Q. Zhang, W. 
Qin, Y. Zheng, X. Qiu, X. Huang, T. Gui, “The rise and 
potential of large language model based agents: a survey,” ar Xiv, 2309.07864, 2023, DOI: 
10.48550/ar Xiv.2309.07864. 
[4] D. A. Boiko, R. Mac Knight, B. Kline, G. Gomes, “Autonomous chemical research with large language models,” 
Nature, vol. 624, no. 7992, pp. 570-578, 2023, DOI: 
10.1038/s41586-023-06792-0. 
[5] S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, Y. Cao, “Re Act: synergizing reasoning and acting in 
language models,” ar Xiv, 2210.03629, 2023, DOI: 
10.48550/ar Xiv.2210.03629. 
[6] X. Liu, Q. Qiu, Y. Zhang, M. Cai, Y. Liu, M. Fu, L. Yi, W. 
Hu, Q. Zhuge, “Auto-DTWave: demonstration of digital 
twin-aided autonomous optical network operation with 
continuous wavelength loading”, Optical Fiber Communication Conference (OFC) 2024, Paper Th1G.5, 2024, 
DOI: 10.1364/OFC.2024.Th1G.5. 
[7] P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, 
N. Goyal, H. Küttler, M. Lewis, W. Yih, T. Rocktäschel, 
S. Riedel, D. Kiela, “Retrieval-augmented generation for 
knowledge-intensive NLP tasks”, Advances in Neural Information Processing Systems, vol. 33, pp. 9459-9474, 
2020. DOI: 10.5555/3495724.3496517. 
[8] O. Topsakal, T. C. Akinci, “Creating large language 
model applications utilizing Lang Chain: a primer on developing LLM apps fast,” International Conference on 
Applied Engineering and Natural Sciences, vol. 1, no. 1, 
pp. 1050–1056, 2023, DOI: 10.59287/icaens.1127. 
[9] Open AI, “GPT-4o,” https://platform.openai.com 
/docs/models/gpt-4o, accessed on 6 September 2024. 
[10] V. Curri, “GNPy model of the physical layer for open and 
disaggregated optical networking [Invited],” Journal of 
Optical Communications and Networking, vol. 14, no. 6, 
pp. C92-C104, 2022, DOI: 10.1364/JOCN.452868. 
[11] Z. Zhong, M. Ghobadi, M. Balandat, S. Katti, A. Kazerouni, J. Leach, M. Mc Killop, Y. Zhang, “BOW: first realworld demonstration of a Bayesian optimization system 
for wavelength reconfiguration,” Optical Fiber Communication Conference (OFC) 2021, Paper F3B.1, 2021, 
DOI: 10.1364/OFC.2021.F3B.1.

---
